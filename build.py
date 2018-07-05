# (C) tomGER or something like that /shrug

import os
import shutil
import time
import webbrowser

print("""
                        https://github.com/tumGER/
   _____ _____  ______ _ _            _____                      _ _           
  / ____|  __ \|  ____(_) |          / ____|                    (_) |          
 | (___ | |  | | |__   _| | ___  ___| |     ___  _ __ ___  _ __  _| | ___ _ __ 
  \___ \| |  | |  __| | | |/ _ \/ __| |    / _ \| '_ ` _ \| '_ \| | |/ _ \ '__|
  ____) | |__| | |    | | |  __/\__ \ |___| (_) | | | | | | |_) | | |  __/ |   
 |_____/|_____/|_|    |_|_|\___||___/\_____\___/|_| |_| |_| .__/|_|_|\___|_|   
                                                          | |                  
                                                          |_|  
                        By: @_tomGER (tumGER on Github)

                        Currently only supports Windows

It could be that a permissions error will pop up, fix it by restarting the python script! We don\'t really know why that happens!
""")

wurzel = os.getcwd()

DevkitYes = input("\nHave you installed DevkitPRO with Switch support yet? (1 = Yes, 2 = No) ")
if DevkitYes == 2:
    print("Remember to select \"Switch Development\" in the Installer when asked to choose components!")
    time.sleep(3)
    webbrowser.open("https://github.com/devkitPro/installer/releases/")
    quit()
# I wanted to use wget here until I realized that wget isn't a standard on windows


Thomleg = input("\nDo you want free games and a backup loader? (1 = Yes, 2 = No) ")
if Thomleg == 1:
    webbrowser.open("https://www.youtube.com/watch?v=DLzxrzFCyOs")
    quit()

print("\nUpdating ...")
time.sleep(1)
os.system("pacman -S devkitA64 switch-tools switch-curl switch-bzip2 switch-curl switch-freetype switch-libjpeg-turbo switch-sdl2 switch-sdl2_gfx switch-sdl2_image switch-sdl2_ttf switch-zlib switch-libpng --needed --quiet")

print("\n Getting Dependencies ...")
time.sleep(1)
os.system("git clone https://github.com/tumGER/SDFilesCompiler.git SDFilesCompiler") #So it isn't depended on a full clone and I could just use the .exe as a standalone file

os.chdir(wurzel + "/SDFilesCompiler/src/")
s = os.getcwd()
os.chdir(wurzel)

print("Creating folder structure ...")
time.sleep(1)

if os.path.exists("compiled"):
    shutil.rmtree("compiled")

if os.path.exists("compiled"):
    os.rmdir("compiled")    #Weird error with permissions, seems to be fixed by relaunching the file for whatever reason ...

os.makedirs("compiled")
os.makedirs("compiled/atmosphere")
os.makedirs("compiled/atmosphere/titles")
os.makedirs("compiled/atmosphere/titles/010000000000100D")
os.makedirs("compiled/atmosphere/titles/010000000000100D/exefs")
os.makedirs("compiled/switch")
os.makedirs("compiled/switch/appstore")
os.makedirs("compiled/switch/appstore/res")
os.makedirs("compiled/switch/EdiZon")
os.makedirs("compiled/switch/SDFilesUpdater")
os.makedirs("compiled/modules/")
os.makedirs("compiled/modules/newfirm")
os.makedirs("compiled/modules/oldfirm")
os.makedirs("compiled/modules/atmosphere")
os.makedirs("compiled/modules/oldlayered")

print("Copying precreated file ...")
time.sleep(1)

shutil.copyfile(s + "/settings.cfg", "compiled/switch/SDFilesUpdater/settings.cfg")
shutil.copyfile(s + "/hekate_ipl.ini", "compiled/hekate_ipl.ini")
shutil.copyfile(s + "/rtld.stub", "compiled/atmosphere/titles/010000000000100D/exefs/rtld.stub")
shutil.copytree(s + "/EdiZonPackage", "compiled/EdiZon")

print("Updating Submodules ...")
time.sleep(1)

os.chdir(wurzel + "/SDFilesCompiler/")
os.system("git submodule update --remote --force --init") #Submodule's hate me so much that I literally have to force updates in the most dirty way
os.chdir(wurzel)

print("Copying Appstore Resources ...")
time.sleep(1)
# copytree apperently hates me so much that I need to copy every file ._.
shutil.copyfile(s + "/AppstoreNX/res/.DS_Store", "compiled/switch/appstore/res/.DS_Store")
shutil.copyfile(s + "/AppstoreNX/res/default.png", "compiled/switch/appstore/res/default.png")
shutil.copyfile(s + "/AppstoreNX/res/GET.png", "compiled/switch/appstore/res/GET.png")
shutil.copyfile(s + "/AppstoreNX/res/icon.jpg", "compiled/switch/appstore/res/icon.jpg")
shutil.copyfile(s + "/AppstoreNX/res/icon.png", "compiled/switch/appstore/res/icon.png")
shutil.copyfile(s + "/AppstoreNX/res/icon_small.png", "compiled/switch/appstore/res/icon_small.png")
shutil.copyfile(s + "/AppstoreNX/res/INSTALLED.png", "compiled/switch/appstore/res/INSTALLED.png")
shutil.copyfile(s + "/AppstoreNX/res/LOCAL.png", "compiled/switch/appstore/res/LOCAL.png")
shutil.copyfile(s + "/AppstoreNX/res/noscreen.png", "compiled/switch/appstore/res/noscreen.png")
shutil.copyfile(s + "/AppstoreNX/res/opensans.ttf", "compiled/switch/appstore/res/opensans.ttf")
shutil.copyfile(s + "/AppstoreNX/res/popup.png", "compiled/switch/appstore/res/popup.png")
shutil.copyfile(s + "/AppstoreNX/res/shade.png", "compiled/switch/appstore/res/shade.png")
shutil.copyfile(s + "/AppstoreNX/res/UPDATE.png", "compiled/switch/appstore/res/UPDATE.png")

print("Compiling LibNX")
os.chdir(s + "/libnx/")
os.system("make --silent")
print("Installing LibNX") 
time.sleep(1) #Seems to fix a bug where the system checks the files but windows was too slow to show them
os.system("make install --silent")
os.chdir(wurzel)

print("Compiling hbm")
os.chdir(s + "/hbm/")
os.system("make -f Makefile.nx --silent")
print("Copying hbm") #Uses custom fork, will update once merged :)
time.sleep(1) 
os.chdir(wurzel)
shutil.copyfile(s + "/hbm/hbm.nro", "compiled/hbmenu.nro")

print("Compiling hbl")
os.chdir(s + "/hbl/")
os.system("make --silent")
print("Copying hbl")
time.sleep(1)
os.chdir(wurzel)
shutil.copyfile(s + "/hbl/hbl.nso", "compiled/atmosphere/titles/010000000000100D/exefs/main")
shutil.copyfile(s + "/hbl/hbl.npdm", "compiled/atmosphere/titles/010000000000100D/exefs/main.npdm")
 #There seems to be a bug with the compiler currently, no one could get it to compile ._. I'll just use the one I created 2 or 3 days ago and update it once somebody makes a new commit there

print("Compiling GagOrder")
os.chdir(s + "/GagOrder/")
os.system("make --silent")
print("Copying GagOrder") 
time.sleep(1) 
shutil.copyfile(s + "/GagOrder/GagOrder.nro", "compiled/switch/GagOrder.nro")

print("Compiling Appstore")
os.chdir(s + "/AppstoreNX/")
os.system("make --silent")
print("Copying AppstoreNX")
time.sleep(1)
os.chdir(wurzel)
shutil.copyfile(s + "/AppstoreNX/appstore.nro", "compiled/switch/appstore/appstore.nro")

print("Compiling SDFilesUpdater")
os.chdir(s + "/SDFilesUpdater/")
os.system("make --silent")
print("Copying SDFilesUpdater")
time.sleep(1)
os.chdir(wurzel)
shutil.copyfile(s + "/SDFilesUpdater/SDFilesUpdater.nro", "compiled/switch/SDFilesUpdater/SDFilesUpdater.nro")

print("Compiling EdiZon")
os.chdir(s + "/EdiZon/")
os.system("make --silent")
print("Copying EdiZon")
time.sleep(1)
os.chdir(wurzel)
shutil.copyfile(s + "/EdiZon/out/EdiZon.nro", "compiled/switch/EdiZon/EdiZon.nro")
shutil.copyfile(s + "/EdiZon/out/EdiZon.nacp", "compiled/switch/EdiZon/EdiZon.nacp")