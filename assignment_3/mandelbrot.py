import numpy as np

def mandelbrot_divergence(c, max_iter=50):
    z_vals = np.zeros(max_iter, dtype=complex)
    z_vals[0] = 0

    for i in range(max_iter - 1):
        z_vals[i + 1] = z_vals[i]**2 + c  # z_{i+1} = z_i^2 + c
        if z_vals[i + 1].real**2 + z_vals[i + 1].imag**2 > 4: # we check if larger than 4 based on the interval x,y<2
            return i + 1  # diverged at step i+1

    return -1  # stayed bounded