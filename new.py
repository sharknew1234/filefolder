import os

while True:
    vibor = input('FOLDER or FILE:')

    if vibor == 'folder':
        folder = input('Enter folder name:')
        os.mkdir( folder )

    elif vibor == 'file':
        filename = input('Enter file name:')
        fi = open(filename, 'w')
        fi.close()