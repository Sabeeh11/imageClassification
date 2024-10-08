
from google.colab import drive
drive.mount('/content/drive')

# List files in a specific folder
!ls /content/drive/My\ Drive/Data/weather_Dataset

!pip install ultralytics

from ultralytics import YOLO

model = YOLO("yolov8n-cls.pt")

results = model.train(data='/content/drive/My Drive/Data/weather_Dataset', epochs=20, imgsz=64)

!scp -r /content/runs /content/drive/My\ Drive/Data/weather_Dataset#saving the results to gdrive

import os

results_path = '/content/runs/classify/train3/results.csv'

results = pd.read_csv(results_path)

print(results.columns)#to get column names exaclty

import pandas as pd
import matplotlib.pyplot as plt
plt.figure()
plt.plot(results['                  epoch'], results[       '  metrics/accuracy_top1']*100)
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Accuracy')
plt.show()

model = YOLO("/content/runs/classify/train3/weights/best.pt")  # load a custom model

!ls /content/drive/My\ Drive/Data/weather_Dataset/train/shine/

file_path = '/content/drive/My Drive/Data/weather_Dataset/train/shine/shine68.jpg'#the image path in gdrive

results = model(file_path)#we can understand from the probabilites

