import find_block
import cv2
import yaml

video = 'video-bw.mp4'

relativeX = 0
relativeY = 77
relativeZ = 0

delay = 2

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
while success:
    success, frame = cap.read()

    # if the frame is not empty
    if frame is None:
        success = False
        break

    file = directory + str(vframe) + '.yml'
    fileContents = 'blocks: \n'

    print(vframe)

    # loop through each pixel in the frame
    for i in range(frame.shape[1]):
        fileContents += '  \'' + str(i + relativeX) + '\':\n'
        for j in range(frame.shape[0]):
            fileContents += '    \'' + str(j + relativeY) + '\':\n'
            # get the pixel color
            color = frame[frame.shape[0]-1-j, frame.shape[1]-1-i]

            # check if the pixel is black
            if color[0] == 0 and color[1] == 0 and color[2] == 0:
                block = 'black_concrete'
            elif color[0] == 255 and color[1] == 255 and color[2] == 255:
                block = 'white_concrete'
            else:
                block = 'black_concrete_powder'

            fileContents += '      \'-' + str(relativeZ) + '\': minecraft:' + block + '\n'

    fileContents += 'delay: ' + str(delay)

    # write the frame to a yml file
    with open(file, 'w') as f:
        fileYaml = yaml.safe_load(fileContents)
        yaml.dump(fileYaml, f)

    vframe += 1