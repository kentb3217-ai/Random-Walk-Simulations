# %%
import numpy as np, matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import ffmpeg

# Iterations
n = 5000

# Input: iterations (n), initial x, initial y, and initial z
# Output: Array of size n x 3
def random_walk3D(n, init_x = 0, init_y = 0, init_z = 0):
    steps = np.random.choice([-1, 1], size=(n, 3))
    coords = np.cumsum(steps, axis=0) 
    coords = np.insert(coords, 0, [init_x, init_y, init_z], axis=0)
    return coords[:, 0], coords[:, 1], coords[:, 2]

# Extract x, y, and z coordinates from random_walk_3D function
x, y, z = random_walk3D(n)

# Create empty graph
fig, ax = plt.subplots(2, 1, subplot_kw={'projection': '3d'})
fig.suptitle(f'Random Walk 3D, n = {n}')

# Adjust spacing
fig.subplots_adjust(hspace=.4)

# Create animator graph
ax[0].set_title('Animated')
ax[0].set(xlim=(np.min(x), np.max(x)), ylim=(np.min(y), np.max(y)), zlim=(np.min(z), np.max(z)))

# Create static graph
ax[1].plot(x, y, z, lw=1)
ax[1].set_title('Static')
ax[1].scatter(x[0], y[0], z[0], c='lime', s=10, label='start', zorder=2)
ax[1].scatter(x[-1], y[-1], z[-1], c='r', s=10, label='end', zorder=2)
ax[1].legend()

# Create empty line and point objects with no data. Will be updated during animation
my_line, = ax[0].plot([], [], [], lw=1) # Line shows path, make sure to add comma at end to unpack it
my_point, = ax[0].plot([], [], [], 'ro', ms=5) # Dot to show current position, make sure to add comma at end to unpack it

# Update line and point for each iteration for the animator
def get_step(n, x, y, z, this_line, this_point):
    this_line.set_data_3d(x[:n+1], y[:n+1], z[:n+1])
    this_point.set_data_3d([x[n]], [y[n]], [z[n]])
    return this_line, this_point

# Call animator
random_walk_movie = FuncAnimation(fig, get_step, frames=n, fargs=(x, y, z, my_line, my_point)) # fargs specifies the data, line, and point objects to use when updating the frame

# Save animation and static graph in current directory
random_walk_movie.save('RandomWalk3D.mp4', fps=30, dpi=300)