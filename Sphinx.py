import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_triangle(ax, points, phases, colors, recursion_depth, max_depth):
    if recursion_depth > max_depth:
        return
    
    # Plot the phases at the triangle vertices
    for i, (phase, point) in enumerate(zip(phases, points)):
        ax.text(point[0], point[1], point[2], phase, ha='center', va='center', fontsize=12, bbox=dict(facecolor=colors[i], edgecolor='black', boxstyle='round,pad=0.5'))

    # Plot the edges of the triangle
    for i in range(3):
        for j in range(i + 1, 3):
            ax.plot([points[i][0], points[j][0]], [points[i][1], points[j][1]], [points[i][2], points[j][2]], 'k-')

    # Calculate midpoints for recursive triangles
    midpoints = [(points[i] + points[j]) / 2 for i in range(3) for j in range(i + 1, 3)]
    
    # Plot smaller triangles recursively
    new_triangles = [
        (points[0], midpoints[0], midpoints[1]),
        (points[1], midpoints[0], midpoints[2]),
        (points[2], midpoints[1], midpoints[2]),
        (midpoints[0], midpoints[1], midpoints[2])
    ]
    
    for triangle in new_triangles:
        plot_triangle(ax, triangle, phases, colors, recursion_depth + 1, max_depth)

# Define the phases and colors
phases = ['Genesis', 'Fallout', 'Exodus']
colors = ['green', 'red', 'blue']

# Create the sphere
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Define the sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 1 * np.outer(np.cos(u), np.sin(v))
y = 1 * np.outer(np.sin(u), np.sin(v))
z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the sphere
ax.plot_surface(x, y, z, color='c', alpha=0.3, rstride=5, cstride=5)

# Define initial triangle points on the sphere
points = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

# Plot initial triangle and recursive triangles
plot_triangle(ax, points, phases, colors, 0, 2)  # Adjust max_depth for more recursion

# Set the aspect of the plot to be equal
ax.set_box_aspect([1, 1, 1])

# Hide the axes
ax.axis('off')

# Title
plt.title('Fractal Representation of Historical Revolutions in the Sphinx Sphere', fontsize=16)

# Show the plot
plt.show()
