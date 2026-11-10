"""
Chapter 6: Measuring Space: Perimeter and Area
Curriculum ID: 2ca7b10a-3fb9-484f-8116-30d7b586c526
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)

100% Complete Curriculum & Problem Solver:
- All in-text Worked Examples & Activities
- All Exercises 6.1, 6.2, 6.3
- All End-of-Chapter Exercises 1 to 27 (all sub-parts)
- Fully calculated step-by-step solutions with zero skipped calculations
- 5 rich concept visuals per module with interactive Mafs graph configurations
"""

from .ch6_m1 import get_m1
from .ch6_m2 import get_m2
from .ch6_m3 import get_m3
from .ch6_m4 import get_m4
from .ch6_m5 import get_m5
from .ch6_m6 import get_m6

def get_ch6_modules():
    return [
        get_m1(),
        get_m2(),
        get_m3(),
        get_m4(),
        get_m5(),
        get_m6()
    ]
