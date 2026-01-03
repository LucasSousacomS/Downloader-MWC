import os
import subprocess
import tkinter as tk
from tkinter import ttk

#print(os.listdir('I:\SteamLibrary\steamapps\common\My Winter Car\Radio'))



MODES = {
    "radio": {
        "path": r"I:\SteamLibrary\steamapps\common\My Winter Car\Radio",
        "max_tracks": 200  
    },
    "cd1": {
        "path": r"I:\SteamLibrary\steamapps\common\My Winter Car\CD1",
        "max_tracks": 15
    },
    "cd2": {
        "path": r"I:\SteamLibrary\steamapps\common\My Winter Car\CD2",
        "max_tracks": 15
    },
    "cd3": {
        "path": r"I:\SteamLibrary\steamapps\common\My Winter Car\CD3",
        "max_tracks": 15
    }
}

mode = "radio"

MAX_TRACKS = MODES[mode]["max_tracks"]

def searchIndex(path):
    used = set()
    try:
        os.listdir(path)
    except OSError:
        print("Error acessing the radio file. Make sure the file exists. It should look like xxx\zzz\My Winter Car\Radio or xxx\zzz\My Summer Car\Radio")
        return None
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

    root = tk.Tk()
    root.title("My Summer Car Downloader")
    root.geometry("700x450")

    
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(3, weight=1)

    
    frame_title = tk.Frame(root)
    frame_title.grid(row=0, column=0, sticky="ew", pady=5)

    title_label = tk.Label(
        frame_title,
        text="My Summer Car Radio Downloader",
        font=("Arial", 16, "bold")
    )
    title_label.pack()

    
    frame_menu = tk.Frame(root, relief="groove", bd=2)
    frame_menu.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

    mode = tk.StringVar(value="radio")

    options = [("Radio", "radio"), ("CD1", "cd1"), ("CD2", "cd2"), ("CD3", "cd3")]

    for i, (text, value) in enumerate(options):
        rb = tk.Radiobutton(
            frame_menu,
            text=text,
            variable=mode,
            value=value
        )
        rb.grid(row=0, column=i, padx=20)

    
    frame_controls = tk.Frame(root)
    frame_controls.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

    frame_controls.grid_columnconfigure(1, weight=1)

    
    tk.Label(frame_controls, text="Pasta:").grid(row=0, column=0, sticky="w", pady=2)
    entry_folder = tk.Entry(frame_controls)
    entry_folder.grid(row=0, column=1, sticky="ew", padx=5)

    
    tk.Label(frame_controls, text="Link:").grid(row=1, column=0, sticky="w", pady=2)
    entry_link = tk.Entry(frame_controls)
    entry_link.grid(row=1, column=1, sticky="ew", padx=5)

    
    btn_download = tk.Button(frame_controls, text="Download", width=12)
    btn_download.grid(row=0, column=2, rowspan=2, padx=10, sticky="ns")

    
    frame_log = tk.Frame(root, relief="sunken", bd=2)
    frame_log.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

    frame_log.grid_rowconfigure(0, weight=1)
    frame_log.grid_columnconfigure(0, weight=1)

    text_log = tk.Text(frame_log, wrap="word")
    text_log.grid(row=0, column=0, sticky="nsew")

    scrollbar = tk.Scrollbar(frame_log, command=text_log.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    text_log.config(yscrollcommand=scrollbar.set)

    # =====================
    root.mainloop()

   
    # mwcPath = MODES[mode]["path"]
    # if(mwcPath[-6:] != '/Radio'):
    #     print("The radio folder must be something like xxx\zzz\My Winter Car\Radio or xxx\zzz\My Summer Car\Radio")
    # ytLink = 'https://www.youtube.com/watch?v=TCd6PfxOy0Y'
    # downloadAndConv(mwcPath, ytLink)


if __name__ == "__main__":
    main()

