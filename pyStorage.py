#!/usr/bin/env python

import subprocess

def kernel_func():
    uname = "uname"
    uname_arg = "-a"
    print("Gathering system information using %s command: \n")
    subprocess.call([uname, uname_arg])

def disk_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print("Gathering hard disk information using %s command: \n")
    subprocess.call([diskspace, diskspace_arg])

def main():
    kernel_func()
    disk_func()

if __name__ =="__main__":
    main()