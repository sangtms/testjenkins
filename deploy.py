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

environment = ""
if len(sys.argv) > 1:
    environment = sys.argv[1]

print "environment %s" %environment

root_folder_path = os.path.dirname(os.path.realpath(__file__))
print "root_folder_path %s" %root_folder_path

solution_relative_file_path = r"TestJenkins.sln"

project_relative_folder_path = r"ConsoleApp"
project_relative_file_path = project_relative_folder_path + r'\ConsoleApp.csproj'

output_absolute_folder_path = root_folder_path + r'\\' + project_relative_folder_path + r'\bin\Release\\'

print SEPERATE_LINE
print "Build solution %s" % solution_relative_file_path

dotnet_builder = MsBuilder()
if not dotnet_builder.build_net_core(solution_relative_file_path):
	sys.exit(100)

print SEPERATE_LINE
print "Publish application"

if not dotnet_builder.deploy_net_core(project_relative_file_path, 'bin\Release\aaa\\'):
	sys.exit(100)