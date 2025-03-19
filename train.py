from google.colab import drive
drive.mount('/content/gdrive')

ROOT_DIR = '/content/gdrive/My Drive/Plat_sepeda_motor_yolov8/train'

!pip install ultralytics

import os
from ultralytics import YOLO
# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
results = model.train(data=os.path.join('/content/gdrive/My Drive/Plat_sepeda_motor_yolov8/train', "google_collab.yaml"), epochs=100)  # train the model

# use the code below on separate cell to download model to your gdrive
import locale
import os

def getpreferredencoding(do_setlocale = True):
    return "UTF-8"

locale.getpreferredencoding = getpreferredencoding

!scp -r /content/runs '/content/gdrive/My Drive/Plat_sepeda_motor_yolov8'
