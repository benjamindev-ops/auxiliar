import os 
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str, dest="name", required=True )
args = parser.parse_args()
filename = args.name

nuspec_raw= os.popen("cat " + filename).read()

id_var = os.environ.get('id')
version = os.environ.get('version')
title = os.environ.get('title')
authors = os.environ.get('authors')
owners = os.environ.get('owners')
description = os.environ.get('description')

remove_id = re.sub('\$id\$', id_var, nuspec_raw)
remove_version = re.sub('\$version\$', version, remove_id)
remove_title = re.sub('\$title\$', title, remove_version)
remove_author = re.sub('\$author\$', authors, remove_title)
remove_owners = re.sub('\$owners\$', owners, remove_author)
remove_description = re.sub('\$description\$', description, remove_owners)

print(remove_description)