import numpy as np
from matplotlib import pyplot
from matplotlib import colors


def m_CTF():
    map_CTF = np.ones((64, 121))

    for i in range(map_CTF.shape[1]):
        if (i % 2) == 0:
            map_CTF[:, i] = 0

    map_CTF[:3, :] = 0
    map_CTF[-5:, :] = 0
    map_CTF[-3:, :11] = 1
    map_CTF[25:27, :] = 0
    map_CTF[41:43, :] = 0
    map_CTF[-15:, 29:41] = 0
    map_CTF[11:14, 24] = 1
    map_CTF[45:48, 24] = 1
    map_CTF[11:14, 60] = 1
    map_CTF[11:14, 76] = 1
    map_CTF[9:12, 75] = 0
    map_CTF[14, 75] = 0
    map_CTF[11:13, 77] = 0
    map_CTF[-9:-6, 52] = 1
    map_CTF[-9:-6, 74] = 1
    map_CTF[-6, 70:77] = 0
    map_CTF[11:14, 104] = 1
    map_CTF[45:48, 104] = 1
    map_CTF[9:12, 103] = 0
    map_CTF[14, 103] = 0
    map_CTF[11:13, 105] = 0
    map_CTF[-12:-10, 73] = 0
    map_CTF[46:49, 103] = 0
    map_CTF[43:45, 105] = 0

    map_list = map_CTF.tolist()

    # colormap = colors.ListedColormap(["white", "grey"])
    # pyplot.imshow(map_list, cmap=colormap)
    # pyplot.show()

    map_array = map_CTF

    return map_array, map_list
