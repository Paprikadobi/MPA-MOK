import numpy as np
import matplotlib.pyplot as plt
import lattice as lt

L = np.array([[2, 0, 0], [1, 1, 0], [0, 0, 3]])

print(lt.hamdamard_ratio(L))

U = lt.rand_unimod(3, 3)

B = np.matmul(L, U)

print(B)
print(lt.hamdamard_ratio(B))

# EX 2

def distance_LatticeVector(basis, vect):
    cvp = lt.babai(basis, vect)
    print(f'CVP: {cvp}')

    return np.linalg.norm(np.abs(vect - cvp))

def ex2(basis1, basis2, vect):
    dist1 = distance_LatticeVector(basis1, vect)
    dist2 = distance_LatticeVector(basis2, vect)

    if dist1 < dist2:
        print('Basis 1 gives better result')
    elif dist2 > dist1:
        print('Basis 1 gives better result')
    else:
        print('Both basis give same result')

v1 = np.array([-5, 1, 0])
v2 = np.array([-10, 1, 13])

ex2(L, B, v1)
ex2(L, B, v2)

# EX 2.1

def getPoints(x1, y1, z1, x2, y2, z2, x3, y3, z3):
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

v = v2

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

xval, yval, zval = getPoints(L[0, 0], L[0, 1], L[0, 2], L[1, 0], L[1, 1], L[1, 2], L[2, 0], L[2, 1], L[2, 2])
ax.scatter(xval, yval, zval, s=5)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.plot3D(xs=[0, v[0]], ys=[0, v[1]], zs=[0, v[2]], color='black')

ax.plot3D(xs=[0, L[0, 0]], ys=[0, L[0, 1]], zs=[0, L[0, 2]], color='red')
ax.plot3D(xs=[0, L[1, 0]], ys=[0, L[1, 1]], zs=[0, L[1, 2]], color='red')
ax.plot3D(xs=[0, L[2, 0]], ys=[0, L[2, 1]], zs=[0, L[2, 2]], color='red')

b = lt.babai(L, v)
ax.plot3D(xs=[v[0], b[0]], ys=[v[1], b[1]], zs=[v[2], b[2]], color='green')
ax.plot3D(xs=[0, b[0]], ys=[0, b[1]], zs=[0, b[2]], color='brown')

plt.show()