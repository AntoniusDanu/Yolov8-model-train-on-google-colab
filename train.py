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
