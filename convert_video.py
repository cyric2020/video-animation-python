from concurrent.futures import thread
import find_block
import cv2
import yaml
import threading
from tqdm import tqdm
import os

video = 'video.mp4'

relativeX = 0
relativeY = 77
relativeZ = 0

fps = 2
delay = 20/fps

# demo frame.yml
# blocks:
#  'x': 
#    'y':
#      ' z+0': 'minecraft:air'
#      ' z+1': 'minecraft:stone'
#      ' z+2': 'minecraft:stone'
# delay: 1

# loop through each frame of the video
cap = cv2.VideoCapture(video)
directory = './frames/'
success = True
vframe = 0

threads = {}

def async_write(file, contents):
    fileYaml = yaml.safe_load(contents)
    with open(file, 'w') as f:
        yaml.dump(fileYaml, f)

# delete all frames
for file in os.listdir(directory):
    os.remove(directory + file)

while success:
    success, frame = cap.read()

    # if the frame is not empty
    if frame is None:
        success = False
        break

    file = directory + str(vframe) + '.yml'
    fileContents = 'blocks: \n'

    # loop through each pixel in the frame
    pbar = tqdm(total=frame.shape[1])
    pbar.set_description("Processing frame %d" % vframe)
    for i in range(frame.shape[1]):
        pbar.update(1)
        fileContents += '  \'' + str(i + relativeX) + '\':\n'
        for j in range(frame.shape[0]):
            fileContents += '    \'' + str(j + relativeY) + '\':\n'
            # get the pixel color
            color = frame[frame.shape[0]-1-j, frame.shape[1]-1-i]

            # find the closest block to the pixel color
            block = find_block.find_closest_block(color)

            fileContents += '      \'-' + str(relativeZ) + '\': ' + block + '\n'

    fileContents += 'delay: ' + str(delay)

    # write the frame using async_write in a thread
    thread = threading.Thread(target=async_write, args=(file, fileContents))
    thread.start()

    vframe += 1

    pbar.close()