"""
Chapter 3: The World of Numbers
Curriculum ID: 09ca99d2-0489-48f2-8d39-8b26ca7885c9
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)

100% Complete Curriculum & Problem Solver:
- All in-text Worked Examples 1 to 9
- All Exercises 3.1, 3.2, 3.3, 3.4, 3.5
- All End-of-Chapter Exercises 1 to 16 (all sub-parts)
- Fully calculated step-by-step solutions with zero skipped calculations
- 5 rich concept visuals per module with interactive Mafs graph configurations
"""

from .ch3_m1 import get_m1
from .ch3_m2 import get_m2
from .ch3_m3 import get_m3
from .ch3_m4 import get_m4
from .ch3_m5 import get_m5
from .ch3_m6 import get_m6

def get_ch3_modules():
    return [
        get_m1(),
        get_m2(),
        get_m3(),
        get_m4(),
        get_m5(),
        get_m6()
    ]
