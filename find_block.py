import json

colord = [50, 90, 106]
rgbL = ['r', 'g', 'b']

# json format: "acacia_leaves.png": {"r": 85, "g": 85, "b": 86}

with open('averages.json') as f:
    averages = json.load(f)

colorChache = {}

def find_closest_block(color):
    """
    Find the closest block to the given color.
    """
    # if the color is already in the cache, return it
    if str(color) in colorChache:
        return colorChache[str(color)]

    closest_block = None
    closest_distance = None
    for block in averages:
        distance = 0
        for i in range(3):
            distance += (color[i] - averages[block][rgbL[i]]) ** 2
        if closest_distance is None or distance < closest_distance:
            closest_distance = distance
            closest_block = block

    colorChache[str(color)] = remove_suffix(closest_block)
    return remove_suffix(closest_block)

# funciton to remove _side* and .png from the filename
def remove_suffix(filename):
    # e.g. "acacia_leaves_side3.png" -> "acacia_leaves"
    new_filename = None
    for suffix in ['_top', '_bottom', '_side', '_front', '_back', '_side0', '_side1', '_side2', '_side3', '_side4']:
        if filename.endswith(suffix + '.png'):
            new_filename = filename[:-len(suffix + '.png')]
    if filename.endswith('.png') and new_filename is None:
        new_filename = filename[:-len('.png')]
    return new_filename

# print(find_closest_block(colord))