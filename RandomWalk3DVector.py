# %%
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation

# Initialize
n = 5000

# Input: iterations (n), length of each line (r)
# Output: Cumulative sum of all three coordinates (x, y, z)
def random_walk_3D_vector(n, r=1):
    phi = np.random.uniform(0, 2*np.pi, n)
    theta = np.random.uniform(0, 2*np.pi, n)
    x = r*np.sin(phi)*np.cos(theta)
    y = r*np.sin(phi)*np.sin(theta)
    z = r*np.cos(phi)
    cartesian = [x, y, z]
    coords = np.cumsum(cartesian, axis=1)
    coords = np.insert(coords, 0, [0,0,0], axis=1)
    return coords[0], coords[1], coords[2]

# Extract x, y, z from function
x, y, z = random_walk_3D_vector(n)

# Create empty graph
fig, ax = plt.subplots(2, 1, subplot_kw={'projection': '3d'})
fig.suptitle(f'Random Walk Vector 3D, n = {n}')

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
random_walk_movie.save('RandomWalkVector3D.mp4', fps=30, dpi=300)
