"""
Warning: This code is broken. Don't treat it as model code for your work.

This code generates random pixel art. The values are all integers drawn from a
random uniform distribution. The range of the random distribution increases as 
we go up in the image. 

# Topics we'll cover:
# - pdb
# - setting up debugging configuration in VSCode
# - post mortem debugging
# - inspecting variables
# - breakpoints/conditional breakpoints
# - stepping through lines
# - debug console
# - How to use this when developing for large packages. 
"""

import numpy as np
import matplotlib.pylab as plt

# make a random image
np.random.seed(99999)


def generate_rgb_pixel(x, y):
    """
    Function to generate a RGB color at any given pixel
    """
    red = np.random.uniform(0, y/dim)
    green = np.sqrt(0.4 * np.sin(x/dim2 * np.pi + np.random.uniform(0, y/10)))
    blue = np.random.poisson(lam=100)/255
    return (red, green, blue)

# size of canvas
dim = 105
dim2 = 35

# for each row, we will draw numbers from increasingly large pools of random numbers
new_image = np.zeros([dim, dim2])

for i in range(dim):
    # draw random integers between 0 and 10*(i+1), no repeats!
    for j in range(dim2):
        # generate new RGB pixel
        pixel_rgb = generate_rgb_pixel(j, i)
        new_image[j, i] = pixel_rgb


new_image = np.array(new_image)

# plot the resulting image. 
plt.figure()
plt.imshow(new_image)
plt.gca().invert_yaxis()
plt.title("Art")
plt.show()