import numpy as np
from matplotlib import pyplot
from matplotlib import colors


def m_SES():
    map_Ses = np.zeros((91, 137), dtype=int)
    index = 2
    while index < map_Ses.shape[1] - 5:
        map_Ses[:, index] = 1
        index += 3

    map_Ses[0:3, :] = 0
    map_Ses[18:20, :] = 0
    map_Ses[35:37, :] = 0
    map_Ses[52:54, :] = 0
    map_Ses[69:71, :] = 0
    map_Ses[86:, :] = 0

    map_Ses[0, 28] = 1
    map_Ses[10, 28] = 1
    map_Ses[20, 28] = 1
    map_Ses[29, 28] = 1
    map_Ses[39, 28] = 1
    map_Ses[48, 28] = 1
    map_Ses[58, 28] = 1
    map_Ses[68, 28] = 1
    map_Ses[78, 28] = 1
    map_Ses[87, 28] = 1

    map_Ses[0, 57] = 1
    map_Ses[10, 57] = 1
    map_Ses[20, 57] = 1
    map_Ses[29, 57] = 1
    map_Ses[39, 57] = 1
    map_Ses[48, 57] = 1
    map_Ses[58, 57] = 1
    map_Ses[68, 57] = 1
    map_Ses[78, 57] = 1
    map_Ses[87, 57] = 1

    map_Ses[0, 85] = 1
    map_Ses[10, 85] = 1
    map_Ses[20, 85] = 1
    map_Ses[29, 85] = 1
    map_Ses[39, 85] = 1
    map_Ses[48, 85] = 1
    map_Ses[58, 85] = 1
    map_Ses[68, 85] = 1
    map_Ses[78, 85] = 1
    map_Ses[87, 85] = 1

    map_Ses[0, 114] = 1
    map_Ses[10, 114] = 1
    map_Ses[20, 114] = 1
    map_Ses[29, 114] = 1
    map_Ses[39, 114] = 1
    map_Ses[48, 114] = 1
    map_Ses[58, 114] = 1
    map_Ses[68, 114] = 1
    map_Ses[78, 114] = 1
    map_Ses[87, 114] = 1

    map_Ses[0, -1] = 1
    map_Ses[10, -1] = 1
    map_Ses[20, -1] = 1
    map_Ses[29, -1] = 1
    map_Ses[39, -1] = 1
    map_Ses[48, -1] = 1
    map_Ses[58, -1] = 1
    map_Ses[68, -1] = 1
    map_Ses[78, -1] = 1
    map_Ses[87, -1] = 1

    map_Ses[50, 41] = 0
    map_Ses[50, 44] = 0
    map_Ses[51, 44] = 0
    map_Ses[55, 41] = 0
    map_Ses[55, 44] = 0
    map_Ses[54, 44] = 0

    map_Ses[51, 42] = 1
    map_Ses[51, 43] = 1
    map_Ses[52, 41] = 1
    map_Ses[53, 41] = 1
    map_Ses[52, 42] = 1
    map_Ses[53, 42] = 1
    map_Ses[52, 43] = 1
    map_Ses[53, 43] = 1
    map_Ses[54, 42] = 1
    map_Ses[54, 43] = 1

    map_list = map_Ses.tolist()

    # colormap = colors.ListedColormap(["white", "grey"])
    # pyplot.imshow(map_list, cmap=colormap)
    # pyplot.show()

    map_array = map_Ses

    return map_array, map_list
