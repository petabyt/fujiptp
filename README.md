sequoia-ptpy modified to attempt enabling boot flag for Canon DSLRs.  

## Install, Test
```
git clone https://github.com/petabyt/sequoia-ptpy
cd sequoia-ptpy
pip3 install .
```

Keep running `python3 bootdisk.py` until you get ResponseCode OK.  
It may take 50-30 attempts because of timing issues (?). In half of  
those attempts, the camera might crash with Err 70. Just remove the battery,  
and try again.  

I've been able to disable/enable boot disk on 1300D a few times with it.  

Initial changes from original: https://github.com/petabyt/sequoia-ptpy/commit/54a4acc3ff5614215a8cc97e02af42fcb6a765af

I doubt this will break your camera, but if it does, then you  
get to keep both pieces.  
