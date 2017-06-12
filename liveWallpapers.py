import sys
import os
import glob
import shutil
from PIL import Image
import traceback

try:
    for dirName, subdirList, fileList in os.walk("./"):
        # This was my location of the directory, I'd imagine it can vary.
        originalFiles = glob.glob("..\..\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager\LocalState\Assets\*")
        
        # Copy files from original directory to new directory.
            shutil.copy(file, "./")
                
        wallpapers = glob.glob("./*")
        
        for wallpaper in wallpapers:
            if not wallpaper.endswith(".py") and not wallpaper.endswith(".jpg"):
                newWallpaper = wallpaper + ".jpg"
                
                # Check if the file already exists and delete it if it does, otherwise rename with jpg.
                if not os.path.isfile(newWallpaper):
                    os.rename(wallpaper, newWallpaper)
                else:
                    os.remove(wallpaper)

                # Using this due to a bug with PIL where it with throw an error if the file
                # is not an image, but it won't close the file. This causes some problems.
                newWallpaperFile = open(newWallpaper, 'rb')
                    
                try:
                    image = Image.open(newWallpaperFile)
                    width, height = image.size
                    image.close()
                except Exception as e:
                    print e
                    newWallpaperFile.close()
                    image.close()
                    os.remove(newWallpaper)  
                    continue                  
                
                newWallpaperFile.close()

                # Check if the wallpaper is the right orientation and delete if it isn't.
                if not (width > height):
                    os.remove(newWallpaper)

except Exception as e:
    print e
    traceback.print_exc()
                
