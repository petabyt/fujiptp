#!/usr/bin/env python
import ptpy
from ptpy import Canon
from time import sleep

camera = ptpy.PTPy()

print("Connected to the camera...")

with camera.session():
    print(camera.eos_dosomething())
