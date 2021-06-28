## sequoia-ptpy modified to attempt enabling boot flag for Canon DSLRs.  

**This is not garunteed to be safe - Keep both pieces if you brick anything.**

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

Initial attempt, crashed 70% of the time:  
https://github.com/petabyt/sequoia-ptpy/commit/54a4acc3ff5614215a8cc97e02af42fcb6a765af  

Fixed crashing by adding extra zeros to string:
https://github.com/petabyt/sequoia-ptpy/commit/b5d493b3cb3804e01c40c97213ebc78b63da095d

# PTP Decoder

I wrote a basic PTP decoder for reverse-engineering PTP USB output.  
See `main.c`, and mess with the filters.  
```
make ptp f=usbdump.bin
```

# How it works
This uses an undocumented Canon PTP command (`0x9052`) found via  
reverse engineering. This command allows DryOS eventprocs like `EnableBootDisk`  
to be run via USB rather than UART.

# Windows, Linux portable front-end

I've written a portable front end UI app for this. I've tested it  
on Windows and Linux.  
https://github.com/petabyt/mlinstall
