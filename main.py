import pystray as pt
from pystray import MenuItem as item
import PIL.Image as pi
import sys
import keyboard as kb
import time as t
import os
png: str = 'mewo.png' # make it whateva
global klstate
klstate: bool = False
autostate: bool = False
kps: int = 0 # Key Presses. future use.

def resource_path(png): # load image
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, png)
image = pi.open(resource_path(png))

def on_quit():
    icon.visible = False
    kb.unhook_all() # Dont want to keep it running now, just for saftey - as exit should kill it anyway.
    icon.stop()
    os._exit(0) # Kills remaining process.

def kl_calc(state, key): #this may need to be an outside func....
    # For future use. Still in dev.
    pass # for now to make it work

def kl_active_timed(state):
    try:
        while state == True:
            print(f'klactive triggered, state: eh')
            for i in range(150):
                kb.block_key(i)
            else:
                t.sleep(10)
                kb.unhook_all()
                break
    except:
        icon.notify('Error! Failed auto-lock keyboard. Please quit KittyLock.', title='KittyLock')

def kl_active(state):
    try:
        while state == True:
            print(f'klactive triggered, state: {state}')
            global autostate # disable autostate to break its loop if its currently running.
            autostate = False
            for i in range(150):
                kb.block_key(i)
            else:
                icon.notify('Keyboard disabled! Kitty cant type. Autolock was also disabled.', title='KittyLock')
                break
    except:
        icon.notify('Error! Failed to lock keyboard. Please quit KittyLock.', title='KittyLock')

def kl_inactive(state):
    try:
        while state == False: # could be an if statment...
            kb.unhook_all()
            icon.notify('Keyboard renabled! Keep kitty away.', title='KittyLock')
            break
    except:
        icon.notify('Error! Failed to unhook keyboard. Please quit KittyLock.', title='KittyLock')

def on_toggle1():
    global klstate
    if klstate:
        klstate = False
        print(f'I switched it to false, it reads: {klstate}')
        kl_inactive(klstate)
    else:
        klstate = True
        print(f'I switched it to true, it reads: {klstate}')
        kl_active(klstate)

def on_toggle2():
    global autostate
    if autostate:
        autostate = False
        print(f'I continue set autostate to: {autostate}')
    else:
        autostate = True
        print(f'I continue set autostate to: {autostate}')

menu = (
    item('Turn on/off KittyLock', on_toggle1, checked=lambda item: klstate),
    item('Enable Auto-Lock', on_toggle2, checked=lambda item: autostate),
    item('Mew?', lambda: icon.notify('Mew! .. is that what you wanted?')),
    item('Version 0.1.4', None),
    item('Quit', on_quit)
)

icon = pt.Icon(png, image, 'KittyLock', menu)
icon.run()

