import math as m
import random as r 
import matplotlib.pyplot as plt
import numpy as np

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density): #pixel_density, determines the desired number of pixels per unit. NOT SURE if that's what they mean wih width
    real = np.linspace(xmin, xmax, int((xmax - xmin) *pixel_density))
    imaginary = np.linspace(ymin, ymax, int((ymax - ymin) *pixel_density))
    return real[np.newaxis, :] + imaginary[:, np.newaxis] * 1j
# returns a two-dimensional array of complex numbers enclosed in a rectangular area given by four parameters

def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c 
    return abs(z) <= 2
#  creates a two-dimensional mask of boolean values over the resulting matrix, z

def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]
# returns a one-dimensional array comprised of only those complex numbers that are stable and therefore belong to the Mandelbrot set


# main function to draw mandelbrot:
def draw_mandel(width):
    c = complex_matrix(-1.5, 0.5, -1, 1, width)
    plt.imshow(is_stable(c, num_iterations=30), cmap="binary")
    plt.axis() # if we want pretty plt.axis("off") 
    plt.show()
    return None

# calling function:
draw_mandel(200)



# OR:

# from PIL import Image
# def draw_mandel(width):
#     c = complex_matrix(-1.5, 0.5, -1, 1, pixel_density=width)
#     image = Image.fromarray(~is_stable(c, num_iterations=30)) # ~ inverts all of the Boolean values, aka makes plot black and background white
#     image.show()
#     return None

# draw_mandel(200)