import json
import os
import cv2

# get average r, g, b values for each image in the textures folder
def calculate_averages():
    textures = './textures'
    averages = {}
    for filename in os.listdir(textures):
        if filename.endswith('.png'):
            img = cv2.imread(os.path.join(textures, filename))
            averages[filename] = {
                'r': int(cv2.mean(img)[0]),
                'g': int(cv2.mean(img)[1]),
                'b': int(cv2.mean(img)[2])
            }
            
    return averages

# write averages to the averages.json file
with open('averages.json', 'w') as f:
    json.dump(calculate_averages(), f)