#!/usr/bin/env python
import ptpy
from ptpy import Canon
from time import sleep

camera = ptpy.PTPy()

print("Connected to the camera...")

with camera.session():
    id = camera.get_storage_ids()[0]
    arr = camera.get_object_handles(id, in_root=True)
    for i in arr:
        print(camera.get_object_info(i))

