#!/usr/bin/env python
import ptpy
from ptpy import Canon

camera = ptpy.PTPy()
with camera.session():
    print(camera.eos_run_command("EnableBootDisk"))
