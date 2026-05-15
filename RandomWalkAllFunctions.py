import numpy as np

# Given iterations, compute the random walk for n iterations in 2D
def random_walk_2D(n):
    steps = np.random.choice([-1, 1], size=(n, 2))
    coords = np.cumsum(steps, axis=0)
    coords = np.insert(coords, 0, [0,0], axis=0)
    return coords[:, 0], coords[:, 1]

# Given iterations, compute the random walk for n iterations in vector 2D
def random_walk_vector_2D(n, r=1):
    theta = np.random.uniform(0, 2*np.pi, size=n)
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    cartesian = [x, y]
    coords = np.cumsum(cartesian, axis=1) # if axis=0 it creates an ellipse shape
    coords = np.insert(coords, 0, [0,0], axis=1)
    return coords[0], coords[1]

# Given iterations, compute the random walk for n iterations in 3D
def random_walk3D(n):
    steps = np.random.choice([-1, 1], size=(n, 3))
    coords = np.cumsum(steps, axis=0)
    coords = np.insert(coords, 0, [0,0,0], axis=0)
    return coords[:, 0], coords[:, 1], coords[:, 2]

# Given iterations, compute the random walk for n iterations in vector 3D
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
