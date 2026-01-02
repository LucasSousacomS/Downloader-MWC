import os
import subprocess

#print(os.listdir('I:\SteamLibrary\steamapps\common\My Winter Car\Radio'))

MAX_TRACKS = 200

def searchIndex(path):
    used = set()
    try:
        os.listdir(path)
    except:
        print("Erro")
    nextIndex = 1
    
    for files in os.listdir(path):
        print(files[-4:])
        if(files[5:-4] == '' or files[0:5] != "track" or files[-4:] != ".ogg" or not files[5:-4].isdigit()):
            continue
        used.add(int(files[5:-4]))

    for i in range(1, MAX_TRACKS + 1):
        if i not in used:
            return i
    return None
        
    # nbr.sort()
    #print(nbr)

    # for i in nbr:
    #     print (f'i = {i}, nextIndex = {nextIndex}')
    #     if (nextIndex < i):     
    #         return nextIndex
    #     nextIndex = i + 1
    # return nextIndex

def downloadAndConv(path, link):
    index = searchIndex(path)

    if index == None or index > MAX_TRACKS:
        print ("You can't have more than 200 songs on the radio")
        return

    trackName = f"track{index}"

    audioPath = os.path.join(path, trackName)

    print("Starting download...")

    cmdyt = [
        "yt-dlp",
        "-x",
        "--audio-format",
        "vorbis",
        "--embed-metadata",
        "-o",
        audioPath,
        link
    ]
    try:
        subprocess.run(cmdyt, check=True)
    except subprocess.CalledProcessError:
        print("Error downloading or converting audio")

def main():    
    mwcPath = r'I:\SteamLibrary\steamapps\common\My Winter Car\Radio'
    if(mwcPath[-6:] != '/Radio'):
        print("The radio folder must be something like xxx\zzz\My Winter Car\Radio")
    ytLink = 'https://www.youtube.com/watch?v=TCd6PfxOy0Y'
    downloadAndConv(mwcPath, ytLink)

if __name__ == "__main__":
    main()
