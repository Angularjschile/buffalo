import os, readline
from pprint import pprint
from flask import *
from app import *

print '''
 -----------------------------
|  Buffalo Interactive Shell  |
 -----------------------------
|  All assets have been put   |
|  into this shell. Please be |
|  responsible as the data is |
|  live!!!                    |
 -----------------------------\n'''
os.environ['PYTHONINSPECT'] = 'True'