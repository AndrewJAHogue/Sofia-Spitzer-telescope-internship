
from os.path import isdir
from os import makedirs
chosenstars = ['B/', 'A/', 'C/']
path = './fits/'
paths = ['ForcastOne/', 'ForcastTwo/', "sgrb/"]
subs = ['convolved/', 'shifted', 'success', 'check']
# chosenstar = 'B/'
# path += chosenstar
# if isdir(path + 'shifted/') == False:
#     makedirs(path + 'shifted/')
# path += 'convolved'
# if isdir(path) == False:
#     makedirs(path)
def Main():
    for p in paths:
        x = path + p
        print(f'newpath => {x}')
        for star in chosenstars:
            y = x + star
            # if isdir(newpath) == False:
                # makedirs(newpath)
                # print(f'Made new folder structure: {newpath}')
            for s in subs:
                sub = y + s
                if isdir(sub) == False:
                    makedirs(sub)
                    print(f'Made new folder structure: {sub}')
                    
def FolderCheck(subfolder):
    top = './fits'
    if isdir(top + subfolder) is False:
        makedirs(top + subfolder)
        print(f'Made subfolder => {top + subfolder}')


