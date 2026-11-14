"""
Comprehensive audit of Class 9 Mathematics Part 1 modules against raw NCERT PDFs.
"""
import importlib
import json
import os
import re
import sys
import pypdfium2 as pdfium

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def audit_ch4():
    print("=================== CHAPTER 4 AUDIT ===================")
    ch4_mods = []
    for i in range(1, 7):
        m = importlib.import_module(f'scripts.maths_pt1_generators.ch4_m{i}')
        data = getattr(m, f'get_m{i}')()
        ch4_mods.append(data)
        print(f"Module {i}: '{data.get('title')}' - {len(data.get('worked_examples', []))} worked examples")
        for ex in data.get('worked_examples', []):
            print(f"   [{ex.get('id')}] {ex.get('problem')[:80]}")

def audit_ch2():
    print("=================== CHAPTER 2 AUDIT ===================")
    for i in range(1, 7):
        m = importlib.import_module(f'scripts.maths_pt1_generators.ch2_m{i}')
        data = getattr(m, f'get_m{i}')()
        print(f"Module {i}: '{data.get('title')}' - {len(data.get('worked_examples', []))} worked examples")
        for ex in data.get('worked_examples', []):
            p = ex.get('problem', '')
            lbl = p.split(':')[0] if ':' in p else p[:40]
            print(f"   {lbl}")

def print_all_ch4_problems():
    from scripts.maths_pt1_generators.ch4_generator import get_ch4_modules
    for i, m in enumerate(get_ch4_modules(), 1):
        print(f"=== M{i}: {len(m.get('worked_examples', []))} ===")
        for ex in m.get('worked_examples', []):
            print("  ", ex['problem'][:90])

def print_all_ch5_problems():
    from scripts.maths_pt1_generators.ch5_generator import get_ch5_modules
    for i, m in enumerate(get_ch5_modules(), 1):
        print(f"=== CH5 M{i}: {len(m.get('worked_examples', []))} ===")
        for ex in m.get('worked_examples', []):
            print("  ", ex['problem'][:90])

def print_all_ch6_problems():
    from scripts.maths_pt1_generators.ch6_generator import get_ch6_modules
    for i, m in enumerate(get_ch6_modules(), 1):
        print(f"=== CH6 M{i}: {len(m.get('worked_examples', []))} ===")
        for ex in m.get('worked_examples', []):
            print("  ", ex['problem'][:90])

def print_all_ch7_problems():
    from scripts.maths_pt1_generators.ch7_generator import get_ch7_modules
    for i, m in enumerate(get_ch7_modules(), 1):
        print(f"=== CH7 M{i}: {len(m.get('worked_examples', []))} ===")
        for ex in m.get('worked_examples', []):
            print("  ", ex['problem'][:90])

def print_all_ch8_problems():
    from scripts.maths_pt1_generators.ch8_generator import get_ch8_modules
    for i, m in enumerate(get_ch8_modules(), 1):
        print(f"=== CH8 M{i}: {len(m.get('worked_examples', []))} ===")
        for ex in m.get('worked_examples', []):
            print("  ", ex['problem'][:90])

def print_all_ch1_ch3_problems():
    from scripts.maths_pt1_generators.ch1_generator import get_ch1_modules
    print("=================== CHAPTER 1 ===================")
    for i, m in enumerate(get_ch1_modules(), 1):
        print(f"=== CH1 M{i}: {len(m.get('worked_examples', []))} ===")
        for ex in m.get('worked_examples', []):
            print("  ", ex['problem'][:90])

    from scripts.maths_pt1_generators.ch3_generator import get_ch3_modules
    print("\n=================== CHAPTER 3 ===================")
    for i, m in enumerate(get_ch3_modules(), 1):
        print(f"=== CH3 M{i}: {len(m.get('worked_examples', []))} ===")
        for ex in m.get('worked_examples', []):
            print("  ", ex['problem'][:90])

if __name__ == '__main__':
    print_all_ch1_ch3_problems()
