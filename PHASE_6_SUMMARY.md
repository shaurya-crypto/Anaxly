# Phase 6: Enterprise Student Subscriptions, Entitlements & Production Razorpay Integration

## 1. Executive Summary
Phase 6 delivers a production-grade, enterprise subscription and billing architecture for **Anaxly**. The system provides end-to-end management of student subscription tiers, live class quotas, multi-board curriculum access, and real-time AI video avatar entitlements, paired with a secure, zero-leakage Razorpay payment gateway integration.

The architecture is built so that switching from the test sandbox to live production requires **only updating environment variables** (`RAZORPAY_KEY_ID` and `RAZORPAY_KEY_SECRET`) without modifying any application code.

---

## 2. Database Architecture & Schema Specification

### 2.1 Database Schema (`public.subscriptions`)
A dedicated table storing active student subscription state, billing cadence, quotas, and feature flags.

| Column | Type | Constraints / Description |
| :--- | :--- | :--- |
| `id` | `uuid` | Primary Key, `default gen_random_uuid()` |
| `user_id` | `uuid` | Unique Foreign Key referencing `auth.users(id)` ON DELETE CASCADE |
| `plan_tier` | `text` | Check constraint: `'free'`, `'scholar'`, `'topper'`, `'mastery'` |
| `billing_cycle` | `text` | Check constraint: `'monthly'`, `'annual'` |
| `status` | `text` | Check constraint: `'active'`, `'trialing'`, `'past_due'`, `'canceled'`, `'expired'` |
| `current_period_start` | `timestamptz` | Current billing period start timestamp |
| `current_period_end` | `timestamptz` | Current billing period end timestamp |
| `cancel_at_period_end` | `boolean` | Flag for scheduled non-renewal |
| `monthly_classes_limit` | `integer` | Quota of live classes per month (3, 8, 15, 24) |
| `monthly_classes_used` | `integer` | Count of live classes consumed in current month |
| `total_term_classes_limit`| `integer` | Total classes per academic term (30, 80, 150, 240) |
| `total_term_classes_used` | `integer` | Total classes consumed over academic term |
| `is_avatar_enabled` | `boolean` | Face-to-Face AI Video Avatar access (`false` for Free & Scholar, `true` for Topper & Mastery) |
| `allowed_boards` | `text[]` | Array of authorized school boards (`['CBSE']`, `['ICSE']`, or `['CBSE', 'ICSE', 'IB']`) |
| `pyq_access_level` | `text` | Access tier: `'preview'`, `'chapter_30'`, `'10_year'`, `'predicted'` |
| `has_mock_exam_access` | `boolean` | Access to board mock exams |
| `has_camera_scratchpad`| `boolean` | Access to AI camera notebook scanner |
| `has_parent_whatsapp_reports` | `boolean` | Access to automated parent WhatsApp analytics |
| `has_unwatermarked_notes` | `boolean` | Unwatermarked Master PDF notes downloads |
| `has_morning_blitz` | `boolean` | 10-Minute Morning Exam Blitz sprint access |
| `razorpay_customer_id` | `text` | Razorpay Customer ID |
| `razorpay_subscription_id` | `text` | Razorpay Autopay Subscription ID |
| `razorpay_payment_id` | `text` | Last verified Razorpay payment ID (`pay_...`) |
| `razorpay_order_id` | `text` | Associated Razorpay order ID (`order_...`) |
| `created_at` | `timestamptz` | Record creation timestamp |
| `updated_at` | `timestamptz` | Record update timestamp |

### 2.2 Payment Orders Audit Log (`public.payment_orders`)
Immutable audit trail of all checkout sessions and payment transactions.

| Column | Type | Constraints / Description |
| :--- | :--- | :--- |
| `id` | `uuid` | Primary Key, `default gen_random_uuid()` |
| `user_id` | `uuid` | Foreign Key referencing `auth.users(id)` |
| `order_id` | `text` | Unique Razorpay order identifier (`order_...`) |
| `payment_id` | `text` | Associated Razorpay payment identifier (`pay_...`) |
| `plan_tier` | `text` | Target tier ('scholar', 'topper', 'mastery') |
| `billing_cycle` | `text` | Billing cadence ('monthly', 'annual') |
| `amount` | `integer` | Amount in Indian Paise (e.g. 49900 = ₹499.00) |
| `currency` | `text` | Currency code (`'INR'`) |
| `status` | `text` | Order status (`'created'`, `'attempted'`, `'paid'`, `'failed'`, `'refunded'`) |
| `receipt` | `text` | Unique internal receipt reference (`rcpt_...`) |
| `metadata` | `jsonb` | Full gateway responses and tracking metadata |
| `created_at` | `timestamptz` | Order timestamp |
| `updated_at` | `timestamptz` | Status update timestamp |

### 2.3 Row-Level Security (RLS) & Isolation Policies
- **`public.subscriptions`**:
  - `SELECT`: `(SELECT auth.uid()) = user_id` (Students can read only their own active subscription record).
  - `ALL`: `service_role` has full administrative access.
- **`public.payment_orders`**:
  - `SELECT`: `(SELECT auth.uid()) = user_id` (Students can audit only their own payment receipts).
  - `ALL`: `service_role` has full administrative access.

### 2.4 Synchronizing Profiles Trigger (`tr_subscriptions_sync_profiles`)
To ensure backwards compatibility with legacy UI queries reading `public.profiles`, a Postgres trigger automatically synchronizes profile fields whenever a subscription is updated:
- `profiles.subscription_tier = NEW.plan_tier`
- `profiles.is_avatar_enabled = NEW.is_avatar_enabled`
- `profiles.monthly_avatar_capsules_limit = NEW.monthly_classes_limit`

---

## 3. Pricing Matrix & Unit Economics

| Plan | Billing Cadence | Price (INR) | Price in Paise | Live Classes / Mo | AI Video Avatar | Target Margin |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Chalkboard Free** | Free Forever | ₹0 | 0 | 3 classes/mo | No (Audio Socratic) | - |
| **Scholar** | Monthly | ₹499 / mo | 49,900 | 8 classes/mo | No (Audio Socratic) | 88.5% |
| **Scholar** | Annual (billed ₹4,788) | ₹399 / mo | 478,800 | 8 classes/mo | No (Audio Socratic) | 85.6% |
| **Topper Pro** | Monthly | ₹1,099 / mo | 109,900 | 15 classes/mo | **100% Face-to-Face Video** | 76.5% |
| **Topper Pro** | Annual (billed ₹10,788) | ₹899 / mo | 1,078,800 | 15 classes/mo | **100% Face-to-Face Video** | 71.3% |
| **Mastery Infinity** | Monthly | ₹1,799 / mo | 179,900 | 24 classes/mo | **100% Face-to-Face Video** | 80.1% |
| **Mastery Infinity** | Annual (billed ₹17,988) | ₹1,499 / mo | 1,798,800 | 24 classes/mo | **100% Face-to-Face Video** | 76.2% |

---

## 4. Razorpay Integration Architecture

### 4.1 Zero-Leakage Security Invariant
- **Server-Only Secret**: `RAZORPAY_KEY_SECRET` is never sent to the client browser or included in frontend bundles.
- **Client Public Key**: The client browser receives only `keyId` (`NEXT_PUBLIC_RAZORPAY_KEY_ID` or server-provided public key id) to initialize the official Razorpay Checkout modal (`Razorpay(options)`).
- **Cryptographic Signature Verification**: HMAC SHA256 digest validation (`order_id + '|' + payment_id`) guarantees that orders cannot be forged or tampered with.

### 4.2 Production Switchover Mandate
To switch from test mode to live payments, only the following environment variables in `.env.local` or hosting configuration need to be changed:
```env
# Switch from rzp_test_ to rzp_live_
RAZORPAY_KEY_ID=rzp_live_XXXXXXXXXXXXXXXXXXXXXXXX
RAZORPAY_KEY_SECRET=YYYYYYYYYYYYYYYYYYYYYYYY
NEXT_PUBLIC_RAZORPAY_KEY_ID=rzp_live_XXXXXXXXXXXXXXXXXXXXXXXX
```
Zero code changes are required. The backend REST client automatically negotiates with `https://api.razorpay.com/v1/orders`.

### 4.3 Webhook Event Processing (`/api/payment/webhook`)
Handles asynchronous server-to-server callbacks from Razorpay:
- Validates the `x-razorpay-signature` header using `RAZORPAY_WEBHOOK_SECRET` or `RAZORPAY_KEY_SECRET`.
- Listens for `order.paid` and `payment.captured` events.
- Performs idempotent database updates: marks `payment_orders.status = 'paid'` and triggers atomic subscription activation via `updateSubscriptionPlan`.

---

## 5. Razorpay MCP Server Integration
Configured in `~/.gemini/config/mcp_config.json`, `~/.gemini/antigravity/mcp_config.json`, and `.agents/mcp_config.json`:
- **Endpoint**: `https://mcp.razorpay.com/mcp`
- **Authentication**: HTTP Basic Auth with encoded credentials.
- **Status**: Tested and verified returning HTTP 200 with complete tool registry (`create_order`, `capture_payment`, `fetch_payment`, `create_customer`, `refund_payment`).

---

## 6. Verification & Quality Sign-Off
- **TypeScript Static Verification**: `npx tsc --noEmit` completed with **0 errors**.
- **Next.js Production Build**: `npm run build` completed successfully with exit code **0**, compiling all 24 static and dynamic routes.
- **Git State**: Local repository clean, changes committed under descriptive commit tags.
