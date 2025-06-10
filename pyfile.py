#!/usr/bin/env python3
# 
import datetime
import os
import shutil
import subprocess
import sys
import argparse
import time
# from PIL import Image

import sorter
import pseudonym

execution_start = time.time()

__VERSION__ = "1.4.0"
__AUTHOR__ = "Nicholas Toothaker"
__PATH__ = os.path.dirname(os.path.abspath(__file__))

NO_ARG = "\nERROR: No Valid Argument\nType 'pyfile.py --help' for valid arguments\n"
SOURCE_HELP = "Source directory to sort or rename. Defaults to root directory of module."
DEST_HELP = """Destination directory for sorted files. Not used for Psudonym. Defaults to root directory of module."
If source is given with no destination then destination is set to source."""
MONTHS = {  "01":"January","02":"February","03":"March",
            "04":"April","05":"May","06":"June",
            "07":"July","08":"August","09":"September",
            "10":"October","11":"November","12":"December"}

parser = argparse.ArgumentParser(
                    prog='Pyfile',
                    description='Sorts image files by year and month.',
                    epilog='By Nicholas Toothaker')

parser.add_argument('-s','--sort', action='store_true')
parser.add_argument('-u','--unsort', action='store_true')
parser.add_argument('-r','--rename', action='store_true')
parser.add_argument('-v','--version', action='store_true')
parser.add_argument('--source',dest='source',default=__PATH__, help=SOURCE_HELP)
parser.add_argument('--destination',dest='destination',default=__PATH__)
args = parser.parse_args()

src = args.source
dst = args.destination

if args.source and not args.destination:
    src = os.path.abspath(args.source)
    dst = src
elif not args.source and args.destination:
    src =  os.path.abspath(args.source)
    dst =  os.path.abspath(args.destination) 


### MAIN


# subprocess.call("clear", shell=True)
if args.sort:
    sorter = sorter.Sorter(src, dst)
    sorter.sort()
elif args.unsort:
    sorter = sorter.Sorter(src, dst)
    sorter.unsort()
elif args.rename:
    sorter = pseudonym.rename_files(src)
elif args.version:
    print("Pyfile ",__VERSION__)
else:
    print(NO_ARG)

# print program execution time
print("--- Program Execution Time: %.2f seconds ---" % (time.time() - execution_start))