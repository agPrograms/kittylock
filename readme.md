# KittyLock ![mewo!](https://files.softicons.com/download/animal-icons/cat-force-icons-by-iconka/png/64x64/cat_sleep.png)
### **Don't let your cat type for you. Enable it using the system tray icon and walk away for study without having your cat jump on the keyboard and spam keys.**

---

## Why?
I needed another project to work on while I study for certifications and I haven't spent a lot of time in Python lately. I saw some videos that used [pystray](https://pystray.readthedocs.io/en/latest/index.html) and it peaked my interest. So I got to thinking. Then my cat jumped up on my desk and spammed `ZZZzzxxxXXXcSsssss`, **so I made this.**

## How?
Utilizing multiple python packages, such as pystray, pillow, keyboard, and other python-intergratged packages - I made a single file program (not including the cat PNG) to just lock the keybaord by just blocking input. Nothing special really. The rest of the code is just for looks and the cat icon was found [here](https://www.softicons.com/animal-icons/cat-force-icons-by-iconka/cat-sleep-icon) after a simple google search. I really want to try and somehow make this automatic. As I already have included a button/function dedicated for it, but I found this harder to do especially if I wanted to keep it as a single-file program.

## Can I use it?
Absolutely. Its a single file (not including the cat PNG) application and can be built/compliled rather easily using [pyinstaller](https://pyinstaller.org/en/stable/). I also will upload built .EXEs here if you rather not do it yourself and just want to try it if you found my repo on a whim.

## How do I use it?

When the program is opened, you can see it running by opening the system tray. It should appear as a gray, sleeping cat. **Right click the icon and a menu will appear.** If "Turn on/off KittyLock" is unchecked, it means its off. Click it, and you will receive a windows notification that it has been turned on. The menu item will also be checked off.
It's very striaght forward.

---

### To build it yourself:
**Before you attempt this, you must have at least version Python 3.10 installed as well as [pysintaller](https://pyinstaller.org/en/stable/) installed through `pip`**
1. Download `main.py` and `mewo.png` and place it in a folder/directory of your choosing. Or just download this branch as a ZIP.
2. Open Terminal (Windows 11) or Command Prompt (Windows 10 or older.) and set your directory to the path the files reside in.
3. Execute `pyinstaller --onefile  --windowed --icon "mewo.png" --add-data "mewo.png;." main.py`. It will store the .EXE in the `dist` folder it creates in that path as `main.exe`.

And thats it! Execute it, and it will start in the system tray of your computer. Right click on the gray cat and a menu will appear.

