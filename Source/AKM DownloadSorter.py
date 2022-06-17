import PIL.Image
import os
import shutil
import pystray

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



# _________________________________________________
# System Tray
# _________________________________________________
mainicon=PIL.Image.open(scriptdirname+"\\icon\\sorter.png")

def on_clicked(icon,item):
    if str(item)=="Organize":
        folderSortFunc()
    elif str(item)=="Open Folder":
        os.startfile(downloadpath)
    elif str(item)=="Exit":
        sysTray.stop()

sysTray=pystray.Icon("Akm Download Sorter",mainicon,menu=pystray.Menu(
    pystray.MenuItem("Organize",on_clicked),
    pystray.MenuItem("Open Folder",on_clicked),
    pystray.MenuItem("Exit",on_clicked)
))

sysTray.run()