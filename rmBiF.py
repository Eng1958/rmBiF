#!/usr/bin/env python3
"""

*** Description ***

    rmBiF.py: remove blank in file(s)
    Removes all blanks from a filename and change
    the first character of the word to uppercase (if you want)

    Example:
        "foo bar foo bar.mp2" => "FooBarFooBar.mp3"

    Copyright (C) 2017  Dieter Engemann <dieter@engemann.me>

    24.01.2017  Version 1.0     First version

"""
import os 
import os .path
import argparse
import re

def main():

    print( "Hello Python")

    parser = argparse.ArgumentParser(description='Remove blanks from filename(s)')
    parser.add_argument('--verbose', '-v', action='store_true', help='verbose mode')
    parser.add_argument('--camelcase', '-c', action='store_true', help='camelcase flag ' + \
        '(change first char to uppercase)')
    parser.add_argument('--dryrun', '-d', action='store_true', help='run command without changing')
    parser.add_argument('--file', '-f', nargs='*', action='append', required=True, help='file pattern')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    args = parser.parse_args()
    print(args.file)
    for f in args.file:
        for filename in f:
            print(filename + ' ', end="")
            print(os.path.exists(filename))
            if (os.path.exists(filename)):
                print('Basename: ' + os.path.basename(filename))
                print('Dirname:  ' + os.path.dirname(filename))
                print('Basename: ' + os.path.basename(filename).title())
                basename = os.path.basename(filename).title()
                new_filename = ''
                for p in basename.split():
                    new_filename += p
                print(new_filename)
            print()
        
    # get the current working directory
    cwd = os.getcwd()
    print(cwd)





if __name__ == '__main__':

    main()

