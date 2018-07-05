# (C) tomGER or something like that /shrug

import os
import shutil
import time


wurzel = os.getcwd()

print("""
####################################################################################################################################
# It could be that a permissions error will pop up, fix it by restarting the python script! We don\'t really know why that happens #                                                                                                                      #
####################################################################################################################################
""")

time.sleep(4)

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

shutil.copyfile("src/rtld.stub", "compiled/atmosphere/titles/010000000000100D/exefs/rtld.stub")

os.system("git submodule update --remote --force")

os.chdir("src/hbm/")
os.system("make -f Makefile.nx")
print("Copying hbm") #Uses custom fork, will update once merged :)
time.sleep(1) #Seems to fix a bug where the system checks the files but windows was too slow to show them
os.chdir(wurzel)
shutil.copyfile("src/hbm/hbm.nro", "compiled/hbmenu.nro")

os.chdir("src/hbl/")
os.system("make")
print("Copying hbl")
time.sleep(1)
os.chdir(wurzel)
shutil.copyfile("src/hbl/hbl.nso", "compiled/atmosphere/titles/010000000000100D/exefs/main")
shutil.copyfile("src/hbl/hbl.npdm", "compiled/atmosphere/titles/010000000000100D/exefs/main.npdm")

print("Copying dreport")
shutil.copyfile("src/nx-dreport.kip", "compiled/nx-dreport.kip") #There seems to be a bug with the compiler currently, no one could get it to compile ._. I'll just use the one I created 2 or 3 days ago and update it once somebody makes a new commit there

os.chdir("src/GagOrder/")
os.system("make")
print("Copying GagOrder") #This isn't a special fork I made anymore but you will have to deal with that if you really have to use that compiler since you don't trust our Nightly builds
time.sleep(1) #Seems to fix a bug where the system checks the files but windows was too slow to show them
os.chdir(wurzel)
shutil.copyfile("src/GagOrder/GagOrder.nro", "compiled/switch/gagorder.nro")

os.chdir("src/appstore/")
os.system("make")
print("Copying AppstoreNX")
time.sleep(1) #Seems to fix a bug where the system checks the files but windows was too slow to show them
os.chdir(wurzel)
shutil.copyfile("src/appstore/appstore.nro", "compiled/switch/appstore.nro")

