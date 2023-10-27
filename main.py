from ahk import MsgBoxButtons
from canvas import Canvas
from ahk import AHK
import sys

EXIT_PROGRAM = False
PAUSE_PROGRAM = False

def ex():
    global EXIT_PROGRAM
    EXIT_PROGRAM = True

def pause():
    global PAUSE_PROGRAM
    PAUSE_PROGRAM = not PAUSE_PROGRAM


ahk = AHK(executable_path=r'C:\Program Files\AutoHotkey\AutoHotkey.exe')
cnvs = Canvas(ahk, 32, 32)

ahk.add_hotkey('^x', callback=ex) # stop
ahk.add_hotkey('^p', callback=pause) # pause
ahk.start_hotkeys()

im = Canvas.fetch_image()
pixels = Canvas.get_pixels(im)

estimated_time = len(pixels)+sum([len(pixels[k])*0.3 for k in pixels])
s = str(round(estimated_time/60, 2)).split('.')
ahk.msg_box(text=f'Estimated: {s[0]} min {round(int(s[1])*0.01*60)} sec', title='Task', buttons=MsgBoxButtons.YES_NO)

win = ahk.win_get(title='Roblox')
win.activate()

# actually draw onto canvas
for color in pixels:
    c = Canvas.rgb_to_hex(color)
    cnvs.change_color(c)
    for pixel in pixels[color]:
        if EXIT_PROGRAM: sys.exit()
        if PAUSE_PROGRAM:
            while PAUSE_PROGRAM: pass
        cnvs.paint(pixel[0], pixel[1])
