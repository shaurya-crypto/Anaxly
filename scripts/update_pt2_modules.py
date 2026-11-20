import json

def update_pt2_merged():
    pt2_path = "scripts/physics_class11_modules/class11_physics_pt2_modules.json"
    with open(pt2_path, "r", encoding="utf-8") as f:
        all_pt2_modules = json.load(f)

    # Load updated chapters
    ch_map = {}
    for ch in [11, 12, 13, 14]:
        with open(f"scripts/physics_class11_modules/physics_modules_ch{ch}.json", "r", encoding="utf-8") as f:
            ch_mods = json.load(f)
            for m in ch_mods:
                ch_map[m["order_index"]] = m

    updated_count = 0
    new_pt2_modules = []
    for m in all_pt2_modules:
        oid = m.get("order_index")
        if oid in ch_map:
            new_pt2_modules.append(ch_map[oid])
            updated_count += 1
        else:
            new_pt2_modules.append(m)

    print(f"Updated {updated_count} modules in pt2 merged list out of {len(new_pt2_modules)} total modules.")

    with open(pt2_path, "w", encoding="utf-8") as f:
        json.dump(new_pt2_modules, f, indent=2, ensure_ascii=False)
    print("Successfully updated class11_physics_pt2_modules.json!")

if __name__ == "__main__":
    update_pt2_merged()
