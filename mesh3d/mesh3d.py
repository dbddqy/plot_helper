from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
from pandas import read_excel
import numpy as np
import yaml


with open("config/mesh3d.yml", 'r') as file:
    conf = yaml.safe_load(file.read())

data_path = conf["data_path"]   # number of photos
k = conf["k"]
b = conf["b"]
divide = conf["divide"]
method = conf["method"]

figure = plt.figure()
ax = plt.axes(projection="3d")

data = np.array(read_excel(data_path))
x_surf = data.T[0]
y_surf = data.T[1]
z_surf = data.T[2]

# data = reorganize_y(data)
x_seg = np.linspace(-1., 1., num=divide)
y_seg = x_seg * k + b
z_seg = griddata(data[:, 0:2], data[:, 2], np.vstack((x_seg, y_seg)).T, method=method)

ax.plot_trisurf(x_surf, y_surf, z_surf, cmap="rainbow", alpha=0.5)
ax.plot(x_seg, y_seg, z_seg)

plt.show()
