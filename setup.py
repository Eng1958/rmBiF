#!/usr/bin/env python3

from distutils.core import setup

setup( 
    name = "rmBiF", 
    version = "1.1", 
    description = "Remove Blanks in Filename",
    long_description = "This script removes alle blanks in a filename. The words of the filename"
    "be converted to camel case",
    author = "Dieter Engemann", 
    author_email = "dieter@engeman.me", 

    # The project's main homepage.
    url='https://github.com/Eng1958/rmBiF',

    py_modules = ["rmBiF"] 
    )
