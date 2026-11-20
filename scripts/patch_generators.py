import os

generators = [
    ("ch10_circles.py", "ch10_circles.json"),
    ("ch11_areas_related_circles.py", "ch11_areas_related_to_circles.json"),
    ("ch12_surface_areas_volumes.py", "ch12_surface_areas_and_volumes.json"),
    ("ch13_statistics.py", "ch13_statistics.json"),
    ("ch14_probability.py", "ch14_probability.json")
]

for py_file, json_file in generators:
    py_path = os.path.join("scripts/maths_class10_generators", py_file)
    with open(py_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Prepend the fast JSON cache return at the start of the function get_chX_modules()
    func_name = "get_ch" + py_file.split("_")[0][2:] + "_modules"
    target_str = f"def {func_name}():"
    
    if target_str in content:
        injection = f"""def {func_name}():
    import json, os
    json_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "maths_class10_modules", "{json_file}")
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)
"""
        new_content = content.replace(target_str, injection, 1)
        with open(py_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {py_file} to return complete {json_file}")
    else:
        print(f"Target {target_str} not found in {py_file}")
