#!/usr/bin/env python
import ptpy
from ptpy import Canon
from time import sleep

camera = ptpy.PTPy()

print("Connected to the camera...")

with camera.session():
    while True:
        camera.eos_run_command("EnableBootDisk")
        sleep(2)