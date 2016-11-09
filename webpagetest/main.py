#!/usr/bin/env python

import sys
import argparse
from .utils import *

parser = argparse.ArgumentParser(description='CLI to schedule webpagetest.org tests.')
parser.add_argument('-c', '--config', dest='config_file', metavar="CONFIG_FILE", help="Run using specified config file")
parser.add_argument('-n', '--new', dest='new_config_file', metavar="NEW_CONFIG_FILE", help="Create a new config file")
args = parser.parse_args()

def main():
    if args.new_config_file:
        print( 'Creating config file: {}'.format(args.new_config_file) )
    elif args.config_file:
        get_config( args.config_file )
    else:
        parser.print_help()



