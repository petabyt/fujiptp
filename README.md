## sequoia-ptpy modified to attempt enabling boot flag for Canon DSLRs.  

**I doubt this will break your camera, but if it does, then you  
get to keep both pieces.**

# Test

```
git clone https://github.com/petabyt/sequoia-ptpy
cd sequoia-ptpy
pip3 install .
```

Make sure camera is not mounted. I would recommend removing SD card
first, so it doesn't automatically mount.  

Run `python3 bootdisk.py`.

# Major Revisions

Initial attempt, crashed:  
https://github.com/petabyt/sequoia-ptpy/commit/54a4acc3ff5614215a8cc97e02af42fcb6a765af  

Fixed crash by adding extra bytes to string:
https://github.com/petabyt/sequoia-ptpy/commit/b5d493b3cb3804e01c40c97213ebc78b63da095d

# PTP Decoder

I wrote a PTP decoder for reverse-engineering PTP USB output.  
See `main.c`, and mess with the filters.  
```
make ptp f=usbdump.bin
```

# TODO:
- Use pyinstaller to make windows, linux, macos app
- Make android app to enable boot disk and install ML???
