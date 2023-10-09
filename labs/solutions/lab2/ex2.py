import numpy as np
import matplotlib.pyplot as plt
import lattice as lt

def distance_lattice_vector(basis: np.ndarray, v: np.ndarray) -> float:
    """Compute distance between vector v and closest vector in basis.

    :param basis: Basis defining lattice.
    :param v: Vector v.
    :return: Computed distance.
    """
    cvp = lt.babai(basis, v)
    print(f'CVP: {cvp}')

    return np.linalg.norm(np.abs(v - cvp))

def check_bases(basis1: np.ndarray, basis2: np.ndarray, v: np.ndarray) -> int:
    """Check, which basis is better for provided vector v.

    :param basis1: First basis defining lattice.
    :param basis2: Second basis defining lattice.
    :param v: Vector v.
    :return: -1 if basis1 is better, 1 if basis2 is better, 0 if both have same distance
    """
    dist1 = distance_lattice_vector(basis1, v)
    dist2 = distance_lattice_vector(basis2, v)

    if dist1 < dist2:
        print('Basis 1 gives better result')
        return -1
    elif dist2 < dist1:
        print('Basis 2 gives better result')
        return 1
    else:
        print('Both basis give same result')
        return 0

def get_lattice_points(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    """Generate points of the lattice defined by provided basis.
    """
    xval=[]
    yval=[]
    zval=[]

    for a in range(-7, 3):
        for b in range(-1, 3):
            for c in range(-1, 6):
                xval.append(a * x1 + b * x2 + c * x3)
                yval.append(a * y1 + b * y2 + c * y3)
                zval.append(a * z1 + b * z2 + c * z3)

    return xval, yval, zval

def plot_lattice(basis: np.ndarray, v: np.ndarray):
    """Plot lattice points, provided vector and closest vector to it found using Babai's algorithm.
    """
    ax = plt.figure().add_subplot(projection='3d')

    # get lattice points and plot them
    xval, yval, zval = get_lattice_points(basis[0, 0], basis[0, 1], basis[0, 2], basis[1, 0], basis[1, 1], basis[1, 2], basis[2, 0], basis[2, 1], basis[2, 2])
    ax.scatter(xval, yval, zval, s=5)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # plot base vectors
    ax.plot3D(xs=[0, basis[0, 0]], ys=[0, basis[0, 1]], zs=[0, basis[0, 2]], color='red')
    ax.plot3D(xs=[0, basis[1, 0]], ys=[0, basis[1, 1]], zs=[0, basis[1, 2]], color='red')
    ax.plot3D(xs=[0, basis[2, 0]], ys=[0, basis[2, 1]], zs=[0, basis[2, 2]], color='red')

    # find closest vector in lattice
    b = lt.babai(basis, v)

    # plot given vector
    ax.plot3D(xs=[0, v[0]], ys=[0, v[1]], zs=[0, v[2]], color='black')

    # plot closest vector in lattice
    ax.plot3D(xs=[0, b[0]], ys=[0, b[1]], zs=[0, b[2]], color='brown')

    # plot distance between given vector and closest vector in lattice
    ax.plot3D(xs=[v[0], b[0]], ys=[v[1], b[1]], zs=[v[2], b[2]], color='green')

    plt.show()

if __name__ == '__main__':
    L = np.array([[2, 0, 0], [1, 1, 0], [0, 0, 3]])

    print(f'hamdamard ratio of good basis: {lt.hamdamard_ratio(L)}')

    U = lt.rand_unimod(3)
    B = np.matmul(L, U)

    print(f'bad basis: {B}')
    print(f'hamdamard ratio of bad basis: {lt.hamdamard_ratio(B)}')

    v1 = np.array([-5, 1, 0])
    v2 = np.array([-10, 1, 13])

    check_bases(L, B, v1)
    check_bases(L, B, v2)

    plot_lattice(L, v1)
    plot_lattice(L, v2)


