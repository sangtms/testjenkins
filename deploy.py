import os
import sys
import subprocess
import codecs
import json
import builder
#import pypyodbc
from builder import MsBuilder
import shutil
from distutils.dir_util import copy_tree
import logging

webapi_site_name = "webapinew.omnicasa.com"
app_pool_name = "DefaultAppPool"

lst_deploy_servers = [
    'localhost'
]
lst_deployment_tool_server_paths = [
    r'\\apiserver1\C$\OmnicasaNET\deployment',
    r'\\apiserver2\C$\OmnicasaNET\deployment',
    r'\\apiserver3\C$\OmnicasaNET\deployment'
]

SEPERATE_LINE = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

environment = ""
if len(sys.argv) > 1:
    environment = sys.argv[1]

print "environment %s" %environment

api_version = environment.replace("release/", "")
print u"ApiVersion = %s" % api_version

root_folder_path = os.path.dirname(os.path.realpath(__file__))
print "root_folder_path %s" %root_folder_path

solution_relative_file_path = r"TestJenkins.sln"

project_relative_folder_path = r"NetCore"
project_relative_file_path = project_relative_folder_path + r'\NetCore.csproj'

output_relative_folder_path =  'bin\Release\\' + api_version
output_absolute_folder_path = root_folder_path + r'\\' + project_relative_folder_path + r'\\' + output_relative_folder_path

print SEPERATE_LINE
print "Build solution %s" % solution_relative_file_path

dotnet_builder = MsBuilder()
if not dotnet_builder.build_net_core(solution_relative_file_path):
	sys.exit(100)

print SEPERATE_LINE
print "Publish application"

if not dotnet_builder.deploy_net_core(project_relative_file_path, output_relative_folder_path):
	sys.exit(100)
	
print SEPERATE_LINE
print "Copy artifact to servers"

deploy_root_path_template = r"\\%s\C$\inetpub\wwwroot\%s"
for server_name in lst_deploy_servers:
	builder.stop_app_pool(server_name, app_pool_name)
	deploy_root_path = deploy_root_path_template % (server_name, webapi_site_name)
    dest_folder_path = deploy_root_path + r'\\' + api_version
    print 'Copy output to ' + dest_folder_path
    copy_tree(output_absolute_folder_path, dest_folder_path)