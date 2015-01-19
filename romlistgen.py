import os
import sys

romfiles = []
home = os.path.expanduser("~")

try:
    romdir = sys.argv[1]
    romext = sys.argv[2]
    emuexec = sys.argv[3]
except:
    print 'usage:\ngenromlist [roms dir] [roms extension] [emulator exec]'
    print 'extensions must be 3 characters long'
    quit()

if romdir[0] != '/':
    romdir = home+'/'+romdir

print 'searching in '+romdir+' for "'+romext+'" roms to launch with '+emuexec

for root,dirs,files in os.walk(romdir):
    for romfile in files:
        #print 'ext '+romfile[-3:]
        if romfile[-3:] == romext:
            romfiles.append(romfile)
            print 'found '+romfile

for rom in romfiles:
    launcher = "[Desktop Entry]\nName="+rom[:-4]+"\nExec="+emuexec+' "'+romdir+rom+"\"\nType=Application\nCategories=Game;Emulator;\n"
    launcher = launcher+"Icon="+home+"/.gameicons/"+rom[:-4]+".png\n\n"
    lfile = open (home+'/.gameapps/'+rom[:-4],'w')
    lfile.write(launcher)
    lfile.close()

def quit():
    global root
    root.destroy()
