# StarvingArtists-Cheat

> Using this script does not count as exploiting as you don't inject scripts but instead simply mimick mouse and keyboard events

**Setup**
1. `git clone https://github.com/wa1ker38552/StarvingArtists-Cheat`
2. cd into `StarvingArtists-Cheat`
3. Download [AutoHotKey](https://www.autohotkey.com/) **YOU HAVE TO DOWNLOAD VERSION 1.1**
4. Run the setup and copy the _executable path_ or move the executable into the `StarvingArtists-Cheat` directory
5. If you copied the _executable path_, paste the path into line **18** of `main.py` where it says `<YOUR PATH HERE>`
6. In `canvas.py` **YOU MUST CHANGE THE STATIC VARIABLES** they are located on lines 9-13 and ensure that the program will work on your own screen*
7. You need to install `ahk`, `pillow`, and `requests`
   
`*` To get coordinates, you can run the following script:
```py
from ahk import AHK

ahk = AHK()

ahk.add_hotkey('^x', lambda: print(ahk.mouse_position))
ahk.start_hotkeys()
ahk.block_forever()
```
Use `ctrl` + `x` to print the current location of your cursor

**Running**
1. If you don't hvae the image saved in `image.png` already, pass in the `url='<your url>'` parameter into line 18 of `main.py` to specify an image URL
2. Click run. The program will alert you with an estimated time (which should be slightly higher than actual time) and it will automatically focus your Roblox screen after you click OK
