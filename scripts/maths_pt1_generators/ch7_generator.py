"""
Chapter 7: The Mathematics of Maybe: Introduction to Probability
Curriculum ID: 257078e3-5cf0-4286-a1e3-661ce480edc3
CBSE Class 9 Mathematics (NCERT Ganita Manjari Grade 9 Part 1)
"""

from .ch7_m1 import get_m1
from .ch7_m2 import get_m2
from .ch7_m3 import get_m3
from .ch7_m4 import get_m4
from .ch7_m5 import get_m5

def get_ch7_modules():
    return [get_m1(), get_m2(), get_m3(), get_m4(), get_m5()]
