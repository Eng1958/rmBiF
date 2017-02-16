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
    04.02.2017  Version 1.1     Bearbeitung Optionen (dryrun, camelcase)
    16.02.2017  Version 1.2     Bearbeitung Optionen (char)

"""
import os 
import os .path
import argparse
import re

VERSION = 'v1.2 (12.02.2017)'

def main():

    parser = argparse.ArgumentParser(description='Remove blanks from filename(s)')
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose mode')
    parser.add_argument('-c', '--camelcase', action='store_true', help='camelcase flag ' + \
        '(change first char to uppercase)')
    parser.add_argument('-d', '--dryrun', action='store_true', help='run command without changing')
    parser.add_argument('-f', '--file', nargs='*', action='append', required=True, help='file pattern')
    parser.add_argument('-s', '--sub', nargs='*', action='append', help='substitution char for blank')
    parser.add_argument('--version', action='version', version='%(prog)s ' + VERSION)

    args = parser.parse_args()
    if (args.verbose): print('Argumente: ' + str(args))
    for f in args.file:
        for filename in f:
            if (os.path.exists(filename)):
                if (args.verbose):
                    print('Basename (old): ' + os.path.basename(filename))
                    print('Dirname       : ' + os.path.dirname(filename))
                    print('Basename (new): ' + os.path.basename(filename).title())
                fullname = os.path.basename(filename)
                basename, extension = os.path.splitext(fullname)

                # Convert to uppercase
                if (args.camelcase):
                    basename = basename.title()

                packed_filename = ''
##                for p in basename.split():
##                    packed_filename += p
                print("basename " + basename)
                packed_filename = re.sub('\s+', '', basename)
                packed_filename += extension
                new_filename = os.path.join(os.path.dirname(filename), packed_filename)
                if (args.verbose or args.dryrun): 
                    print(filename + ' => ' + new_filename)
                if not (args.dryrun):
                    os.rename(filename, new_filename)
        



if __name__ == '__main__':

    main()

