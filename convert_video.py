import find_block
import cv2
import yaml

video = 'video.mp4'

relativeX = 0
relativeY = 77
relativeZ = 0

delay = 10

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

    # loop through each pixel in the frame
    for i in range(frame.shape[1]):
        print(i)
        fileContents += '  \'' + str(i + relativeX) + '\':\n'
        for j in range(frame.shape[0]):
            fileContents += '    \'' + str(j + relativeY) + '\':\n'
            # get the pixel color
            color = frame[55-j, i]

            # find the closest block to the pixel color
            block = find_block.find_closest_block(color)

            fileContents += '      \'-' + str(relativeZ) + '\': minecraft:' + block + '\n'

    fileContents += 'delay: ' + str(delay)

    # write the frame to a yml file
    with open(file, 'w') as f:
        fileYaml = yaml.safe_load(fileContents)
        yaml.dump(fileYaml, f)

    vframe += 1