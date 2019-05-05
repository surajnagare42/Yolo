import matplotlib.image as mpimg
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

images = []
folder = '/home/nineleaps/helmet/yolov3-Helmet-Detection/test_out'
for filename in os.listdir(folder):
    try:
        img = mpimg.imread(os.path.join(folder, filename))
        if img is not None:
            plt.figure(dpi=200)
            plt.imshow(img)
            plt.show()
    except:
        print('Cant import' + filename)

