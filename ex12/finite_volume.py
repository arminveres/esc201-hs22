import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------------------------------
# Globals
# --------------------------------------------------------------------------------------------------
Nx = 200
Ny = 200
dx = 1.0 / Nx
dy = 1.0 / Ny
sigma_x = 10 * dx
sigma_y = 10 * dy
x0 = 2 * sigma_x
y0 = 2 * sigma_y
ca = 0.48
cb = 0.48


# --------------------------------------------------------------------------------------------------
# Methods
# --------------------------------------------------------------------------------------------------
def ctu(rho):
    rhoJminus1 = np.roll(rho, 1, axis=0)  # to calculate the x-axis term in rhoTmp
    rho_st = (1 - ca) * rho + ca * rhoJminus1
    rho_stLminus1 = np.roll(rho_st, 1, axis=1)  # to calculate the y-axis term in rhoNew
    return (1 - cb) * rho_st + cb * rho_stLminus1


def cir(rho):
    rhoJminus1 = np.roll(rho, 1, axis=0)  # to calculate the x-axis term in rhoTmp
    rhoLminus1 = np.roll(rho, 1, axis=1)  # to calculate the y-axis term in rhoNew
    return rho - (ca * (rho - rhoJminus1) + cb * (rho - rhoLminus1))


def initialCondition():
    rho = np.zeros((Nx, Ny))
    for j in range(Nx):
        for l in range(Ny):
            x = j * dx
            y = l * dy
            rho[j, l] = np.exp(
                -((x - x0) ** 2) / (2 * sigma_x**2)
                - (y - y0) ** 2 / (2 * sigma_y**2)
            )
    return rho


# --------------------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    fig, axs = plt.subplots(2, 2, layout='constrained')
    rounds = 500
    step_h = 50

    rho = initialCondition()
    for i in range(rounds):
        if i % step_h == 0:
            axs[0, 0].contour(rho)
        rho = cir(rho)
    axs[0, 0].set_title("C.I.R.")
    axs[0, 1].imshow(rho)

    rho = initialCondition()
    for i in range(rounds):
        if i % step_h == 0:
            axs[1, 0].contour(rho)
        rho = ctu(rho)
    axs[1, 0].set_title("C.T.U.")
    axs[1, 1].imshow(rho)

    fig.savefig('finite_volume.png')
    # plt.show()
