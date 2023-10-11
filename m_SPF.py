import numpy as np
from matplotlib import pyplot
from matplotlib import colors


def m_SPF():

    map_SPF = np.ones((57, 165), dtype=int)

    for i in range(map_SPF.shape[1]):
        if (i % 2) == 0:
            map_SPF[:, i] = 0

    map_SPF[0, :] = 0  # Empty row 0
    map_SPF[11:13, :] = 0  # Empty thick row
    map_SPF[30:32, :] = 0  # Empty thick row
    map_SPF[:, 160:165] = 0  # Empty end thick column
    map_SPF[53:57, 0:38] = 0  # Empty lower left zone
    map_SPF[48:57, 38:42] = 0  # map_SPF[48:57, 38:42] = 0 # Lower left empty
    map_SPF[43:47, 42:57] = 0  # map_SPF[43:47, 42:57] = 0 # map_SPF[47:57] = 0
    map_SPF[47:57, 43:55] = 1  # "Outside" occupied slot
    map_SPF[48:57, 56:63] = 0  # map_SPF[48:50] = 0 # map_SPF[48:50] = 0
    map_SPF[48:50, 63:156] = 0  # Rows separating the pickup zone empty
    map_SPF[48:57, 156:164] = 0  # map_SPF[50:57, 56:63] = 0
    map_SPF[50:57, 63:156] = 1  # Pickup zone occupied
    map_SPF[51, 7:10] = 0  # Gap above a staircase
    # Gaps interleaved:
    map_SPF[16:20, 32:37] = 0  # Gap a.
    map_SPF[16:20, 58:63] = 0  # Gap b
    map_SPF[16:20, 88:93] = 0  # Gap e
    map_SPF[16:20, 114:119] = 0  # G-gap
    map_SPF[16:20, 146:151] = 0  # Gap i
    map_SPF[37:41, 32:37] = 0  # Gap d
    map_SPF[37:41, 58:63] = 0  # Gap c
    map_SPF[37:41, 88:93] = 0  # Gap f
    map_SPF[37:41, 114:119] = 0  # Gap h
    map_SPF[37:41, 146:151] = 0  # Gap j
    # Stairs:
    map_SPF[7:11, 10:12] = 1
    map_SPF[7:11, 38:40] = 1
    map_SPF[7:11, 74:76] = 1
    map_SPF[7:11, 90:92] = 1
    map_SPF[7:11, 118:120] = 1
    map_SPF[7:11, 154:156] = 1
    map_SPF[52:56, 7:10] = 1
    map_SPF[41:45, 38:40] = 1
    map_SPF[42:46, 118] = 1
    # Blue squares right:
    map_SPF[2:4, 162:165] = 1.0
    map_SPF[22:24, 162:165] = 1
    map_SPF[38:40, 162:165] = 1
    map_SPF[53:55, 162:165] = 1
    # Blue squares below:
    map_SPF[50:52, 40:43] = 1
    map_SPF[50:52, 56:59] = 1
    # Green columns:
    map_SPF[16:18, 6:9] = 1
    map_SPF[16:18, 33:36] = 1
    map_SPF[16:18, 60:63] = 1
    map_SPF[16:18, 89:92] = 1
    map_SPF[16:18, 116:119] = 1
    map_SPF[16:18, 149:152] = 1
    map_SPF[38:40, 6:9] = 1
    map_SPF[38:40, 33:36] = 1
    map_SPF[38:40, 60:63] = 1
    map_SPF[38:40, 89:92] = 1
    map_SPF[38:40, 116:119] = 1
    map_SPF[38:40, 149:152] = 1

    map_list = map_SPF.tolist()

    # colormap = colors.ListedColormap(["white", "grey"])
    # pyplot.imshow(map_list, cmap=colormap)
    # pyplot.show()

    map_array = map_SPF

    return map_array, map_list
