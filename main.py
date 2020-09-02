import ctypes
import os

run_path = __file__.split("main.py")[0]
SPI_SETDESKWALLPAPER = 20

class StartScript:
    backgroundPath = os.path.normpath(run_path + "\\background.png")
    bluejPath = "D:\Program Files\BlueJ"

    def __init__(self):
        self.setBackground()
    
    def setBackground(self):
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, self.backgroundPath, 3)

    def setBluejTemplateClass(self):
        f = open(os.path.normpath(self.bluejPath + "\\lib\german\\templates\\newclass\\stdclass.tmpl"), "w")
        f.write(open(os.path.normpath(run_path + "classtemplate.txt")).read())

s = StartScript()
