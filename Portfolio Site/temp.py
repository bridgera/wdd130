# import the required libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# create a figure
fig = plt.figure()

# create a 3D axes
ax = Axes3D(fig)

# create the data for the torus
R = 1  # radius of the torus
r = 0.5  # radius of the tube
u = v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)

# calculate the x, y, and z coordinates of the torus
x = (R + r * np.cos(v)) * np.cos(u)
y = (R + r * np.cos(v)) * np.sin(u)
z = r * np.sin(v)

# plot the torus
ax.plot_surface(x, y, z, color="r")

# show the plot
plt.show()
