import numpy as np

EPSILON_0 = 8.854e-12

def electric_potential(q, r_source, r_point):
   
    r_source = np.array(r_source)
    r_point = np.array(r_point)

    r = np.linalg.norm(r_point - r_source)

    if r == 0:
        raise ValueError("Potential is undefined at the location of the charge.")

    return (1 / (4 * np.pi * EPSILON_0)) * q / r
def total_potential(charges, points):
    """
    Compute total electric potential at points due to multiple charges.

    Parameters
    ----------
    charges : list of tuples
        Each tuple: (q, r_charge)
    points : list of numpy arrays
        Locations to evaluate V

    Returns
    -------
    list of floats
        Potentials at each point
    """
    V_total = []
    for r_point in points:
        V_point = 0.0
        for q, r_charge in charges:
            V_point += electric_potential(q, np.array(r_charge), np.array(r_point))
        V_total.append(V_point)
    return V_total
