# Turtles

Turtle powered eink screen scrubber, busting ghosts to your specifications (and sometimes on a timer, if you wish). 

:ghost: :zap: :turtle:

# Instructions

1. Download the zip file containing the turtle code by clicking on the green CODE button.
2. Save the zip file in an easily accessible directory
3. Unzip/extract the contents of the zip file
4. When you want to bust ghosts, open your choice of terminal. Change (`cd`) to the turtles directory and run the turtle_power.py script by typing `python turtle_power.py`. Depending on your Python install, you may need to use `python3 turtle_power.py`

Expected behavior should include your eink screen flashing black, and then flashing white. It should take about 6 seconds. Eink ghosts should be cleared.

# What is my purpose?

## Problem
Ghosting is a significant quality of life hurdle with eink screens, particularly for screens being used as external monitors or primary monitors. Eink monitors and raw panels often contain physical buttons to reset the screen and eliminate ghosting, but sometimes the users may not want to stop their workflow to physically reset the screen. 

Or at least I didn't want to do that. I use a raw eink panel and I needed to build the display interface PCB into the body of a laptop, where the display reset button is difficult to access. 

## Solution
This repo contains a Python script that flashes a black screen and then a white screen to reset the eink screen and eliminate ghosting. It's helpful for users working in the command line. It can also be set on a timer to flash every X minutes if users don't want to manually run the script every time.

## Why Turtles? 
The Python script uses Python's built in [turtle graphics library](https://docs.python.org/3/library/turtle.html) to generate a black and white window to eliminate ghosts.
