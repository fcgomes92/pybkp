#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
import sys
import glob
import zipfile

parser = argparse.ArgumentParser(
    description="Creates a backup file / dir of a requested file / dir.")
parser.add_argument('origin',
                    metavar='origin', type=str,
                    help="absolute / relative path to the file / dir")
parser.add_argument('-o', '--output',
                    metavar='output', type=str, default=None,
                    help="")
# parser.add_argument('',
#                     metavar='print', type=bool,
#                     const=True, nargs='?',
#                     help="should I print the .env?")

args = parser.parse_args()


def get_abs(path):
    if not os.path.isabs(path):
        return os.path.abspath(path)
    return path


if __name__ == '__main__':
    # first it checks if it is a file or directory
    origin = get_abs(args.origin)

    # the we get the file / dir name
    name = os.path.basename(origin)

    # the we check if the user wants a output path
    if not args.output:
        output = os.path.dirname(origin)
    else:
        output = get_abs(args.output)

    if os.path.isdir(origin):
        # the origin arg is a dir
        # zips the original file
        output_file = os.path.join(output, '{}.bkp.zip'.format(name))
        os.chdir(os.path.dirname(origin))
        with zipfile.ZipFile(output_file,'w') as myzip:
            for f in glob.iglob(os.path.join(name, '**'), recursive=True):
                myzip.write(f)
            myzip.close()
    elif os.path.isfile(origin):
        # the origin arg is a file
        output_file = os.path.join(output, '{}.bkp'.format(bkp_name))
    else:
        # maybe it doesn't exist
        pass
    sys.exit(0)
