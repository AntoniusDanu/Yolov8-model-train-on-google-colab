# use the code below on separate cell to download model to your gdrive
import locale
import os

def getpreferredencoding(do_setlocale = True):
    return "UTF-8"

locale.getpreferredencoding = getpreferredencoding

!scp -r /content/runs '/content/gdrive/My Drive/Plat_sepeda_motor_yolov8'
