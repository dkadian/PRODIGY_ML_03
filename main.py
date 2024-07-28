import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

dir = 'C:\\Users\\deepa\\OneDrive\\Pictures\\Desktop\\intern\\PRODIGY_ML_03\\dogs-vs-cats\\train'

categories = ['Cat' , 'Dog']

data = []

for category in categories:
    path = os.path.join(dir, category)
    label = categories.index(category)
    
    for img in os.listdir(path):
        imgpath = os.path.join(path, img)
        pet_img =  cv2.imread(imgpath)
        pet_img = cv2.resize(pet_img,(90,90))
        image = np.array(pet_img).flatten()
        
        
        
