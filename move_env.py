import os
def change_name(filenamestr):
    filename = filenamestr.replace('"', "")

    id = os.environ.get('id')
    version = os.environ.get('version')
    title = os.environ.get('title')
    authors = os.environ.get('authors')
    owners = os.environ.get('owners')
    description = os.environ.get('description')

    fin = open(filename, "rt")
    #read file contents to string
    data = fin.read()

    #replace all occurrences of the required string
    data = data.replace('$id$', id)
    data = data.replace('$version$', version)
    data = data.replace('$title$', title)
    data = data.replace('$author$', authors )
    data = data.replace('$owner$', owners)
    data = data.replace('$description$', description)

    #close the input file
    fin.close()

    #open the input file in write mode
    fin = open(filename, "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()
    
    return print(os.popen("cat " + filename).read())
