#!/usr/bin/env python
import ptpy
from ptpy import Canon
from time import sleep

# Commands to try:
# EnableBootDisk
# DisableBootDisk
# TurnOffDisplay

command = "EnableBootDisk"

camera = ptpy.PTPy()

print("Connected to the camera...")

with camera.session():
    #print("You can kill the script (ctrl+z) if you get timeouts.")
    print("Waiting for a good time to send command...")
    while True:
        evt = camera.event()
        if not evt:
            result = camera.eos_run_command(command)
            print(result)
            if result.ResponseCode == "OK":
                print("DryOS command run successfully, if no errors.")
                break
            else:
                print("Bad ResponseCode. Turn off the camera and try again.")
                print("Will keep running.")

