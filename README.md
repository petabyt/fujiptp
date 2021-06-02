```
# Install:
pip3 install .
```

sequoia-ptpy rigged to attempt EnableBootDisk for Canon DSLRs.  

Keep running `python3 bootdisk.py` until you get RESPONSECODE=OK.  
It may take 50-30 attempts because of timing issues (?). In half of  
those attempts, the camera might crash with Err 70. Just remove the battery,  
and try again.  

I've been able to disable/enable boot disk on 1300D twice with it.  

See my changes: https://github.com/petabyt/sequoia-ptpy/commit/54a4acc3ff5614215a8cc97e02af42fcb6a765af
