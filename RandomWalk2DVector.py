# %%
import numpy as np, matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Iterations
n = 5000

# Input: iterations (n), length of each line (r)
# Output: x and y coordinates of the cumulative sum of the randomly generated paths.
def random_walk_vector_2D(n, r=1):
    theta = np.random.uniform(0, 2*np.pi, size=n)
    x = r*(np.cos(theta))
    y = r*(np.sin(theta))
    cartesian = [x, y]
    coords = np.cumsum(cartesian, axis=1) # if axis=0 it creates an ellipse shape
    coords = np.insert(coords, 0, [0,0], axis=1)
    return coords[0], coords[1]

# Extract x and y coordinates from random_walk_vector_2D function
x, y = random_walk_vector_2D(n)

# Create empty graph for animator and static graph
fig, ax = plt.subplots(2, 1)
fig.suptitle(f'Random Walk Vector 2D, n = {n}')

# Adjust vertical spacing
fig.subplots_adjust(hspace=.4)

# Create animator graph
ax[0].set(xlim=(np.min(x), np.max(x)), ylim=(np.min(y), np.max(y)))
ax[0].set_title('Animated')

# Create static graph
ax[1].plot(x, y, lw=1)
ax[1].set_title('Static')
ax[1].scatter(x[0], y[0], c='lime', s=10, label='start', zorder=2)
ax[1].scatter(x[-1], y[-1], c='r', s=10, label='end', zorder=2)
ax[1].legend()

# Create empty line and point objects with no data for animator
my_line, = ax[0].plot([], [], lw=1) # Line shows path, make sure to add comma at end to unpack it
my_point, = ax[0].plot([], [], 'ro', ms=5) # Dot to show current position, make sure to add comma at end to unpack it

# Update line and point for each iteration for the animator
def get_step(n, x, y, this_line, this_point):
    this_line.set_data(x[:n+1], y[:n+1])
    this_point.set_data([x[n]], [y[n]])
    return this_line, this_point

# Call animator
random_walk_movie = FuncAnimation(fig, get_step, frames=n, fargs=(x, y, my_line, my_point)) # fargs specifies the data, line, and point objects to use when updating the frame

# Save animation and static graph in current directory
random_walk_movie.save('RandomWalkVector2D.mp4', fps=30, dpi=300)