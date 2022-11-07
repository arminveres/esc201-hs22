import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage, signal


def apply_stencil(U) -> np.ndarray:
    weight = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    out = np.zeros_like(U)
    return ndimage.convolve(U, weight, mode="constant", cval=0)
    # ndimage.convolve(U, weight, output=out, mode='constant', cval=0)
    # return out


"""
N = 100
setup w, U ((N, N)) and W 
set boundaries to 0 of  array R

U[int(n/2), int(n/4):int(3*n/4)] = 1000
R[int(n/2), int(n/4):int(3*n/4)] = 0
B = np.ones_like(U, dtype=bool)
B[::2, ::2] = False
B[1::2, 1::2] = False

nsteps = 0
add another board array and checkerboard set values
iterate until:
while np.max(np.abs(m)) >= 0.1:
    step 1 for black
    M = multiply  R,C
    U[B] = U[B] + M[B]

    step 2 for white
    M = multiply  R,C
    U[~B] = U[~B] + M[~B]

    nsteps += 1
"""

if __name__ == "__main__":
    N = 500
    weight = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    omega = 2 / (1 + np.pi / N)

    # working matrix/grid of PHI
    U = np.zeros((N, N))
    # correction matrix for stencil
    R = U.copy()
    R.fill(omega / 4)
    R[0] = 0
    R[-1] = 0
    R[:, 0] = 0
    R[:, -1] = 0

    U[int(N / 2), int(N / 4) : int(3 * N / 4)] = 1000
    R[int(N / 2), int(N / 4) : int(3 * N / 4)] = 0

    B = np.ones_like(U, dtype=bool)
    B[::2, ::2] = False
    B[1::2, 1::2] = False

    M = np.ones_like(U)
    nsteps = 0
    while np.max(np.abs(M)) >= 0.1:
        # step 1 for black
        C = ndimage.convolve(U, weight, mode='constant')
        M = np.multiply(R, C)
        U[B] = U[B] + M[B]

        # step 2 for white
        C = ndimage.convolve(U, weight, mode='constant')
        M = np.multiply(R, C)
        U[~B] = U[~B] + M[~B]

        nsteps += 1

    fig = plt.figure()
    # plt.scatter(U)
    # plt.imshow(U)
    plt.imsave("sweep.png", U)
    # plt.show()
