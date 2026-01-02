import os
import subprocess

#print(os.listdir('I:\SteamLibrary\steamapps\common\My Winter Car\Radio'))

nbr = []


mwcPath = 'I:\SteamLibrary\steamapps\common\My Winter Car\Radio'

def searchIndex(path):
    try:
        os.listdir(path)
    except:
        print("Erro")
    nextIndex = 1
    
    for files in os.listdir(path):
        print(files[-4:])
        if(files[5:-4] == '' or files[0:5] != "track" or files[-4:] != ".ogg"):
            continue
        nbr.append(int(files[5:-4]))
        
    nbr.sort()
    #print(nbr)

    for i in nbr:
        print (f'i = {i}, nextIndex = {nextIndex}')
        if (nextIndex < i):     
            return nextIndex
        nextIndex = i + 1
    return nextIndex

trackName = "track" + str(searchIndex(mwcPath))

print(f'Resultado da função: {searchIndex(mwcPath)}')


audioPath = os.path.join(mwcPath, trackName)
# print(audioPath)

cmdyt = [
    "yt-dlp",
    # "-h"
    "-x",
    "--audio-format",
    "vorbis",
    "-o",
    audioPath,
    "https://www.youtube.com/watch?v=TCd6PfxOy0Y"
]

cmdffm = [
    "ffmpeg",
    "-h"
]

subprocess.run(cmdyt, check=True)
