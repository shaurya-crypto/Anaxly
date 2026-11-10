"""
Chapter 5: I’m Up and Down, and Round and Round
Curriculum ID: de83f257-aada-4e27-b420-f7884165c990
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)

100% Complete Curriculum & Problem Solver:
- All in-text Worked Examples & Activities
- All Exercises 5.1, 5.2, 5.3, 5.4, 5.5, 5.6
- All End-of-Chapter Exercises 1 to 26 (all sub-parts)
- Fully calculated step-by-step solutions with zero skipped calculations
- 5 rich concept visuals per module with interactive Mafs graph configurations
"""

from .ch5_m1 import get_m1
from .ch5_m2 import get_m2
from .ch5_m3 import get_m3
from .ch5_m4 import get_m4
from .ch5_m5 import get_m5
from .ch5_m6 import get_m6

def get_ch5_modules():
    return [
        get_m1(),
        get_m2(),
        get_m3(),
        get_m4(),
        get_m5(),
        get_m6()
    ]
