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
            print(filename + ' ')
            ## print(os.path.exists(filename))
            if (os.path.exists(filename)):
                print('Basename (old): ' + os.path.basename(filename))
                print('Dirname:  ' + os.path.dirname(filename))
                print('Basename (new): ' + os.path.basename(filename).title())
                ## basename = os.path.basename(filename).title()
                fullname = os.path.basename(filename)
                basename, extension = os.path.splitext(fullname)
                basename = basename.title()
                print(basename + "      " + extension)
                packed_filename = ''
                for p in basename.split():
                    packed_filename += p
                print(packed_filename)
                packed_filename += extension
                new_filename = os.path.join(os.path.dirname(filename), packed_filename)
                print(new_filename)
                os.rename(filename, new_filename)
            print()
        
    # get the current working directory
    cwd = os.getcwd()
    print(cwd)





if __name__ == '__main__':

    main()

