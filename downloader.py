import os
import subprocess

#print(os.listdir('I:\SteamLibrary\steamapps\common\My Winter Car\Radio'))



def searchIndex(path):
    nbr = []
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

def downloadAndConv(path, link):
    index = str(searchIndex(path))

    if index > 200:
        print ("You can't have more than 200 songs on the radio")
        return

    trackName = "track" + index

    audioPath = os.path.join(path, trackName)

    cmdyt = [
        "yt-dlp",
        "-x",
        "--audio-format",
        "vorbis",
        "-o",
        audioPath,
        link
    ]

    cmdffm = [
        "ffmpeg",
        "-h"
    ]

    subprocess.run(cmdyt, check=True)

def main():    
    mwcPath = 'I:\SteamLibrary\steamapps\common\My Winter Car\Radio'
    if(mwcPath[-6:] != '/Radio'){
        print("The radio folder must be something like xxx\zzz\My Winter Car\Radio")
    }
    ytLink = 'https://www.youtube.com/watch?v=TCd6PfxOy0Y'
    downloadAndConv(mwcPath, ytLink)

if __name__ == "__main__":
    main()
