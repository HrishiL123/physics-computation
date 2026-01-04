import numpy as np

EPSILON_0 = 8.854e-12

def electric_potential(q, r_source, r_point):
   
    r_source = np.array(r_source)
    r_point = np.array(r_point)

    r = np.linalg.norm(r_point - r_source)

    if r == 0:
        raise ValueError("Potential is undefined at the location of the charge.")

    return (1 / (4 * np.pi * EPSILON_0)) * q / r
