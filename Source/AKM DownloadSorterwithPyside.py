import PIL.Image
import os
import shutil
from PySide2 import QtWidgets,QtGui
import sys

scriptpath=__file__
scriptdirname=os.path.dirname(scriptpath)
username=os.getlogin()
downloadpath=f"C:\\Users\\{username}\\Downloads"
os.chdir(downloadpath)

image_formats = ["jpg","jpeg","svg","png","bmp","gif","gifv","webm","swf","tga","tiff","exr","psd"]
document_formats= ["txt","nfo","rtf","pptx","docx","doc"]
pdf_formats= ["pdf"]
music_formats= ["mp3","flac","wav"]
video_formats= ["avi","mpg","mpeg","mov","mp4","mkv","wmv"]
program_formats= ["exe","msi","jar","cmd","bat","ahk", "iso"]
compressed_formats= ["zip","7z","rar","r00","001"]


def folderSortFunc():
    files=os.listdir(downloadpath)
    # print(files)

    for file in files:
        # print(file)
        if os.path.isfile(file): # if they are files and not folder
            ext = (file.split(".")[-1]) # split func returns list, so we only want last element of list,(making sure extension are lowercase wasnt working)
            
            if ext in image_formats:
                if not os.path.exists(f"{downloadpath}\\Images"):
                    os.makedirs(f"{downloadpath}\\Images")
                shutil.move(file,"Images\\"+file)
            elif ext in document_formats:
                if not os.path.exists(f"{downloadpath}\\Documents"):
                    os.makedirs(f"{downloadpath}\\Documents")
                shutil.move(file,"Documents\\"+file)
            elif ext in pdf_formats:
                if not os.path.exists(f"{downloadpath}\\Pdf"):
                    os.makedirs(f"{downloadpath}\\Pdf")
                shutil.move(file,"Pdf\\"+file)
            elif ext in music_formats:
                if not os.path.exists(f"{downloadpath}\\Music"):
                    os.makedirs(f"{downloadpath}\\Music")
                shutil.move(file,"Music\\"+file)
            elif ext in video_formats:
                if not os.path.exists(f"{downloadpath}\\Video"):
                    os.makedirs(f"{downloadpath}\\Video")
                shutil.move(file,"Video\\"+file)
            elif ext in program_formats:
                if not os.path.exists(f"{downloadpath}\\Programs"):
                    os.makedirs(f"{downloadpath}\\Programs")
                shutil.move(file,"Programs\\"+file)
            elif ext in compressed_formats:
                if not os.path.exists(f"{downloadpath}\\Compressed"):
                    os.makedirs(f"{downloadpath}\\Compressed")
                shutil.move(file,"Compressed\\"+file)
            else:
                if not os.path.exists(f"{downloadpath}\\Others"):
                    os.makedirs(f"{downloadpath}\\Others")
                shutil.move(file,"Others\\"+file)


def download_fold_func():
    os.startfile(downloadpath)

# _________________________________________________
# System Tray
# _________________________________________________
class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self,icon,parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self,icon,parent)
        self.setToolTip("AKM Download Sorter")
        menu=QtWidgets.QMenu(parent)

        organize=menu.addAction("Organize")
        organize.triggered.connect(folderSortFunc)
        organize.setIcon(QtGui.QIcon(scriptdirname+"\\icon\\filtering.png"))

        download_folder=menu.addAction("Open Download Folder")
        download_folder.triggered.connect(download_fold_func)
        download_folder.setIcon(QtGui.QIcon(scriptdirname+"\\icon\\folder.png"))

        menu.addSeparator()
        
        exit=menu.addAction("Exit")
        exit.triggered.connect(lambda: sys.exit())
        exit.setIcon(QtGui.QIcon(scriptdirname+"\\icon\\cross2.png"))

        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)
    
    def onTrayIconActivated(self,reason):
        if reason==self.Trigger:
            download_fold_func()

def main():
    app= QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon(scriptdirname+"\\icon\\sorter.png"))
    tray_icon.show()
    tray_icon.showMessage("AKM Download Sorter","Download sorter")
    sys.exit(app.exec_())

if __name__=='__main__':
    main()