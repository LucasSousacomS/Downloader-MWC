import os

#print(os.listdir('I:\SteamLibrary\steamapps\common\My Winter Car\Radio'))

nbr = []
nextIndex = 1

for files in os.listdir('I:\SteamLibrary\steamapps\common\My Winter Car\Radio'):
    if(files[5:-4] == '' or files[0:5] != "track"):
        continue
    nbr.append(int(files[5:-4]))
    
nbr.sort()
#print(nbr)

for i in nbr:
    if (nextIndex < i):
        nextIndex = i        
        break
    nextIndex = i + 1
print(nextIndex)

    # if(nbr > lrgnbr):
    #     lrgnbr = nbr
    # print(lrgnbr)
