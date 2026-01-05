import numpy as np
def electric_field_point_charge(q, r_charge, r_point):
    """
    Compute the electric field produced by a point charge.

    Parameters
    ----------
    q : float
        Charge magnitude.
    r_charge : numpy array
        Position vector of the charge.
    r_point : numpy array
        Position vector where the field is evaluated.

    Returns
    -------
    numpy array
        Electric field vector at r_point.
    """
    k = 8.9875517923e9  # Coulomb constant (N m^2 / C^2)

    r = r_point - r_charge
    r_mag = np.linalg.norm(r)

    if r_mag == 0:
        return np.zeros_like(r)

    E = k * q * r / r_mag**3
    return E
def electric_field(charges, points):
    """
    Compute total electric field at points due to multiple charges.

    Parameters
    ----------
    charges : list of tuples
        Each tuple: (q, r_charge), q in C, r_charge as [x, y]
    points : list of numpy arrays
        Locations to evaluate E

    Returns
    -------
    list of numpy arrays
        Electric field vectors at each point
    """
    E_total = []
    for r_point in points:
        E_point = np.zeros(2)  # assuming 2D
        for q, r_charge in charges:
            E_point += electric_field_point_charge(q, np.array(r_charge), np.array(r_point))
        E_total.append(E_point)
    return E_total

if __name__ == "__main__":
    q = 1e-9  # 1 nC
    r_charge = np.array([0.0, 0.0])
    r_point = np.array([1.0, 0.0])

    E = electric_field_point_charge(q, r_charge, r_point)
    print("Electric field:", E)
