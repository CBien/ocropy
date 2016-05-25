#!/usr/bin/env python

import sys,time,urllib,traceback,glob,os,os.path

assert sys.version_info[0]==2 and sys.version_info[1]>=7,\
    "you must install and use OCRopus with Python version 2.7 or later, but not Python 3.x"

from distutils.core import setup


if not os.path.exists("models/en-default.pyrnn.gz"):
    print
    print "Warning : you will need to download the model 'en-default.pyrnn.gz'"
    print "and put it into ./models if you want to use it as default model."
    print
    print "Check https://github.com/tmbdev/ocropy for the location"
    print "of model files."
    print

scripts = [c for c in glob.glob("ocropus-*") if "." not in c and "~" not in c]

setup(
    name = 'ocropy',
    version = 'v0.2',
    author = "Thomas Breuel",
    description = "The OCRopy RNN-based Text Line Recognizer",
    packages = ["ocrolib"],
    scripts = scripts,
    )
