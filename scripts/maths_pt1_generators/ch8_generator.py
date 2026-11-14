"""
Chapter 8: Predicting What Comes Next: Exploring Sequences and Progressions
Curriculum ID: b45d590f-323e-4263-b899-23d95b2094a7
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .ch8_m1 import get_m1
from .ch8_m2 import get_m2
from .ch8_m3 import get_m3
from .ch8_m4 import get_m4
from .ch8_m5 import get_m5
from .ch8_m6 import get_m6

def get_ch8_modules():
    return [get_m1(), get_m2(), get_m3(), get_m4(), get_m5(), get_m6()]
