import os
import sys
import subprocess
import codecs
import json
import builder
#import pypyodbc
from builder import MsBuilder
import shutil
import logging

SEPERATE_LINE = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

print "sang test sang test"

environment = ""
if len(sys.argv) > 1:
    environment = sys.argv[1]

print "environment %s" %environment

root_folder_path = os.path.dirname(os.path.realpath(__file__))
print "root_folder_path %s" %root_folder_path

solution_relative_file_path = r"TestJenkins.sln"
print "Build solution %s" % solution_relative_file_path

print SEPERATE_LINE

#build and publish
dotnet_builder = MsBuilder()
buildOk = dotnet_builder.build_net_core(solution_relative_file_path)
if not buildOk:
	sys.exit(100)
