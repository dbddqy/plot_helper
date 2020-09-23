import pandas as pd
import numpy as np


# read excel data
def read_excel(path):
    return np.array(pd.read_excel(path))


# # organize xyz values into a dict according to y values
# def reorganize_y(data):
#     dict = {}
#     last_y = data[0, 1]
#     x_list, z_list = [], []
#     for i in range(data.shape[0]):
#         x, y, z = data[i]
#         if y != last_y:
#             dict[last_y] = {'x': x_list, 'z': z_list}
#             x_list, z_list = [x], [z]
#         else:
#             x_list.append(x)
#             z_list.append(z)
#         last_y = y
#     dict[last_y] = {'x': x_list, 'z': z_list}
#     return dict
