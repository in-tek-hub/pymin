#!/usr/bin/env python
from pyStorage import disk_func
import subprocess

def tmp_space():
    tmp_usage = "du"
    tmp_arg = "-hsx"
    path ="/tmp"
    print("Total space occupied by /tmp directory")
    subprocess.call([tmp_usage, tmp_arg, path])

def main():
    disk_func()
    tmp_space()

if __name__ == "__main__":
    main()
