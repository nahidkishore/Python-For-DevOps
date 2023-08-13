"""
Python packages
A package is a collection of modules.

Python modules
A module is a file containing Python definitions and statements.
"""


import os
print (os.getcwd())

import sys
print(sys.path)

#import shutil
# print(shutil.disk_usage("/"))

import shutil

total, used, free = shutil.disk_usage("/")

print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))