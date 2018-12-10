import os
import sys
import subprocess
import codecs
import json
import shutil
import logging

print "sang test sang test"

environment = ""
if len(sys.argv) > 0:
    environment = sys.argv[0]

print "environment %s" %environment
