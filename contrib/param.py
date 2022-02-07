# Written by CHDK user srsa_4c
# https://chdk.setepontos.com/index.php?topic=4338.msg147738#msg147738
import sys
import struct
import ptpy
from ptpy import Canon

class buildp:
    def __init__(self):
        self.n = 0
        self.longpars = 0
        self.data = bytes()
        self.short = bytes()
        self.long = bytes()
        self.name = bytes()
    def addname(self, s):
        self.name = s.encode() + bytes(b'\x00')
    def addint(self,s):
        self.n += 1
        self.short += bytes(b'\x00\x00\x00\x00')
        self.short += struct.pack('<I',int(s,0))
        self.short += bytes(b'\x00\x00\x00\x00')
        self.short += bytes(b'\x00\x00\x00\x00')
        self.short += bytes(b'\x00\x00\x00\x00')
    def addstr(self,s):
        self.n += 1
        self.longpars += 1
        encs = s.encode()
        self.short += bytes(b'\x04\x00\x00\x00')
        self.short += bytes(b'\x00\x00\x00\x00')
        self.short += bytes(b'\x00\x00\x00\x00')
        self.short += bytes(b'\x00\x00\x00\x00')
        self.short += struct.pack('<I',len(encs)+1)
        self.long += bytes(b'\x00\x00\x00\x00')
        self.long += encs
        self.long += bytes(b'\x00')
    def addfile(self,s):
        with open(s,'rb') as f:
            fcont = f.read()
            if len(fcont) > 0:
                self.n += 1
                self.longpars += 1
                self.short += bytes(b'\x04\x00\x00\x00')
                self.short += bytes(b'\x00\x00\x00\x00')
                self.short += bytes(b'\x00\x00\x00\x00')
                self.short += bytes(b'\x00\x00\x00\x00')
                self.short += struct.pack('<I',len(fcont))
                self.long += bytes(b'\x00\x00\x00\x00')
                self.long += fcont
    def finalize(self):
        self.data = self.name + struct.pack('<I',self.n) + self.short + struct.pack('<I',self.longpars)
        if (self.longpars > 0):
            self.data += self.long

argc = len(sys.argv)

if argc < 2:
    print("\nExecute a registered event procedure on a Canon camera connected via USB\n")
    print("Usage: ",sys.argv[0],"<eventproc_name> [Async] [Ret] [arg1] [...]\n")
    print("Options:")
    print("  Async: execute eventproc in a separate task")
    print("  Ret  : eventproc to generate data in return buffer")
    print("         With this option active, eventproc will receive the arguments")
    print("         shifted by 3. The first three args of eventproc will become:")
    print("         1st arg: result buffer's size in bytes (camera generation dependent)")
    print("         2nd arg: pointer to actual data length (eventproc should set this)")
    print("         3rd arg: buffer pointer")
    print("Eventproc arguments can be:")
    print("  Integer, prefixed with capital I, for example: I123")
    print("  String, prefixed with capital S, for example: \"SJust a string argument\"")
    print("  File, prefixed with capital F, for example: Fmyfile.bin\n")
    print("The return value of the eventproc is printed upon finish\n")
    sys.exit()

bp = buildp()

bp.addname(sys.argv[1])

aflag = 0
rflag = 0
n = 1

for s in sys.argv[2:]:
    if len(s)>1 and s[0]=='I':
        bp.addint(s[1:])
        print("int ",s[1:])
    elif len(s)>1 and s[0]=='S':
        bp.addstr(s[1:])
        print("str ",s[1:])
    elif len(s)>1 and s[0]=='F':
        bp.addfile(s[1:])
        print("file ",s[1:])
    elif len(s)>1 and s[0]=='A':
        aflag = 1
        print("Async execution selected")
    elif len(s)>1 and s[0]=='R':
        rflag = 1
        print("Eventproc generates return data")
    else:
        print("ERR arg #",n,"not processed: ",s)
        sys.exit()
    n += 1

bp.finalize()

print (bp.data)

camera = ptpy.PTPy()

print("Connected to the camera...")

with camera.session():
    camera.eos_enable_command()
    camera.eos_enable_command()
    camera.eos_enable_command()
    x = camera.eos_run_command(bp.data,aflag,rflag)
    if len(x.Parameter) < 1:
        print('No return value received')
    else:
        print('Return value:',x.Parameter[0])
