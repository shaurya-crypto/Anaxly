"""
Chapter 2: Introduction to Linear Polynomials
Curriculum ID: cd14fc20-13b7-4d96-98fb-956720dc0f23
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)

100% Complete Curriculum & Problem Solver:
- All in-text Worked Examples 1 to 16
- All Exercises 2.1, 2.2, 2.3, 2.4, 2.5, 2.6
- All End-of-Chapter Exercises 1 to 14 (all sub-parts)
- Fully calculated step-by-step solutions with zero skipped calculations
- 5 rich concept visuals per module with interactive Mafs graph configurations
"""

from .ch2_m1 import get_m1
from .ch2_m2 import get_m2
from .ch2_m3 import get_m3
from .ch2_m4 import get_m4
from .ch2_m5 import get_m5
from .ch2_m6 import get_m6

def get_ch2_modules():
    return [
        get_m1(),
        get_m2(),
        get_m3(),
        get_m4(),
        get_m5(),
        get_m6()
    ]
