
from os.path import isdir
from os import makedirs
import json
chosenstars = ['B/', 'A/', 'C/']
path = ''
computer_path = ''
# fits folder now kept out of repo; too large to upload; make fits.json with fits path
with open('./fits.json', 'r+') as j:
    data = json.load(j)
    path = data['fits path']
    computer_path = data['computer path']
    # print(path)
paths = ['ForcastOne/', 'ForcastTwo/', "sgrb/"]
subs = ['convolved/', 'shifted', 'success', 'check']

def Main():
    for p in paths:
        x = path + p
        print(f'newpath => {x}')
        for star in chosenstars:
            y = x + star
            for s in subs:
                sub = y + s
                if isdir(sub) == False:
                    makedirs(sub)
                    print(f'Made new folder structure: {sub}')
                    
def FolderCheck(subfolder, create=False, verbose=False):
    top = path
    if isdir(top + subfolder) is False:
        if verbose:
            print(f'Doesnt EXIST:: {top + subfolder}')
        if create:
            makedirs(top + subfolder)
            print(f'Made subfolder => {top + subfolder}')
    else:
        if verbose:
            print(f'path {top + subfolder} => already exists')

def FitsFolder():
    return computer_path + path

def ComputerPath():
    return computer_path()