#!/usr/bin/env python
import ptpy
from ptpy import Canon

# Commands to try:
# EnableBootDisk
# DisableBootDisk
# TurnOffDisplay

camera = ptpy.PTPy()
with camera.session():
    print("Press ctrl+z if you get timeouts")
    r = camera.eos_run_command("EnableBootDisk")
    print(r)
    if r.ResponseCode == "OK":
        print("Command executed")
    else:
        print("Error, try again")
