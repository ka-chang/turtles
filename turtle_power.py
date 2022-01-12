"""
Cowabunga
"""
import sys
import time

from turtle import Screen

Screen().setup(width=1.0, height=1.0)
time.sleep(1)
Screen().bgcolor("black")
time.sleep(3)
Screen().bgcolor("white")
time.sleep(2)
Screen().bye()

sys.exit("Ghosts cleared")
