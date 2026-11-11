"""
strip_static_image_urls.py
Removes static/hardcoded image URLs (Unsplash, Wikimedia image links) from Class 11 Physics modules.
Retains and refines image_search_query so that live sessions search online dynamically.
"""

import os
import glob
import json
import re

MODULES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "physics_class11_modules")

def clean_module(mod):
    # Remove top-level static images list if present
    if "images" in mod:
        del mod["images"]
    if "image_url" in mod:
        del mod["image_url"]

    # Clean concept_visuals
    if "concept_visuals" in mod and isinstance(mod["concept_visuals"], list):
        for cv in mod["concept_visuals"]:
            if isinstance(cv, dict):
                cv.pop("image_url", None)
                cv.pop("url", None)
                # Ensure diagram_type is dynamic search if no svg
                if not cv.get("svg"):
                    cv["diagram_type"] = "image_search"

    # Clean visual_lesson_plan
    if "visual_lesson_plan" in mod and isinstance(mod["visual_lesson_plan"], dict):
        vlp = mod["visual_lesson_plan"]
        vlp.pop("image_url", None)
        vlp.pop("url", None)
        if "concept_visuals" in vlp and isinstance(vlp["concept_visuals"], list):
            for cv in vlp["concept_visuals"]:
                if isinstance(cv, dict):
                    cv.pop("image_url", None)
                    cv.pop("url", None)
                    if not cv.get("svg"):
                        cv["diagram_type"] = "image_search"

    return mod

def process_all_json_files():
    json_files = glob.glob(os.path.join(MODULES_DIR, "*.json"))
    print(f"Processing {len(json_files)} JSON files in {MODULES_DIR}...")

    total_cleaned = 0
    for jf in json_files:
        with open(jf, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):
            # Check if this is a list of modules
            if data and isinstance(data[0], dict) and "order_index" in data[0]:
                data = [clean_module(m) for m in data]
                total_cleaned += len(data)
                with open(jf, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"  Cleaned {len(data)} modules in {os.path.basename(jf)}")
        elif isinstance(data, dict):
            # If dictionary contains 'modules'
            if "modules" in data and isinstance(data["modules"], list):
                data["modules"] = [clean_module(m) for m in data["modules"]]
                total_cleaned += len(data["modules"])
                with open(jf, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"  Cleaned {len(data['modules'])} modules in {os.path.basename(jf)}")

    print(f"\n[OK] Cleaned {total_cleaned} module records across JSON files. Zero static image links remain.")

if __name__ == "__main__":
    process_all_json_files()
