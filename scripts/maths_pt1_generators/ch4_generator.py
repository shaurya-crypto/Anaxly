"""
Chapter 4: Exploring Algebraic Identities
Curriculum ID: cef5b4c4-9fad-4f5b-8201-372cce5f4f61
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)

100% Complete Curriculum & Problem Solver:
- All in-text Worked Examples 1 to 18
- All Exercises 4.1, 4.2, 4.3, 4.4, 4.5
- All End-of-Chapter Exercises 1 to 13 (all sub-parts)
- Fully calculated step-by-step solutions with zero skipped calculations
- 5 rich concept visuals per module with interactive Mafs graph configurations
"""

from .ch4_m1 import get_m1
from .ch4_m2 import get_m2
from .ch4_m3 import get_m3
from .ch4_m4 import get_m4
from .ch4_m5 import get_m5
from .ch4_m6 import get_m6

def get_ch4_modules():
    return [
        get_m1(),
        get_m2(),
        get_m3(),
        get_m4(),
        get_m5(),
        get_m6()
    ]
