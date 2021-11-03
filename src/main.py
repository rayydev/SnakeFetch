import os
import colorama
import psutil
import platform
import socket
from logos import LinuxLogo, WindowsLogo
uname = platform.uname()

def ShowLogo():
    LinuxLogo()
    if os.name in ('nt', 'dos'):
        WindowsLogo()

ShowLogo()
print("")
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")
