#!/usr/bin/env python
import ptpy
from ptpy import Canon
from time import sleep

camera = ptpy.PTPy()

print("Connected to the camera...")

with camera.session():
    result = camera.eos_run_command("EnableBootDisk")
    if result.ResponseCode == 'OK':
        print("Boot flag enabled.")
    else:
        print("Error running command")