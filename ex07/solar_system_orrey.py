from ReadPlanets import *

import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import dateutil.parser
import astropy.time


def get_julian_date(curr_date):
    """
    returns the current date converted to the julian date
    """
    dt = dateutil.parser.parse(curr_date)
    time = astropy.time.Time(dt)
    return time.jd


def accel(pos_r, masses):
    """
    returns accelerations for positions r and masses m
    """
    K = 0.01720209895
    F_i = 0
    n = len(pos_r)
    accels = np.zeros((n, 3))
    for i in range(n):
        for j in range(i + 1, n):
            F_i = (
                (np.power(K, 2) * masses[i] * masses[j]) * (pos_r[j] - pos_r[i])
            ) / np.power(np.linalg.norm(pos_r[j] - pos_r[i]), 3)
            # calculate force between i and j
            accels[i] += F_i / masses[i]
            accels[j] -= F_i / masses[j]
    return accels


def solar_leap_frog(r0, v0, h, accel_func):
    r_half = r0 + 0.5 * h * v0
    v_n1 = v0 + h * accel_func(r_half, m)
    r_sec_half = r_half + 0.5 * h * v_n1
    return v_n1, r_sec_half


# 1. Read Solar system data

# h = 4
# end time = 1000 * h
# 2. for time in 0 to end time:
#    3. First drift to give r1/2
#    4. Calculate forces and accels at position r1/2
#    5. Kick: v1 = v0 + ... using accels from step 4.
#    6. Second drift to give r1
#    7. Store r1 for graphics
# 8. Plot all planets
#

if __name__ == "__main__":
    """
    name:   Name of Planet
    r:      direction vector
    v:      velocity
    m:      mass
    """
    # name, r, v, m = readPlanets("SolSystData.dat")
    name_orig, r_orig, v_orig, m_orig = readPlanetsNp("SolSystData.dat")

    fig, axs = plt.subplots(2, 2)
    fig.tight_layout(pad=1.5)

    N = len(r_orig)

    print("Plotting Inner Planets...")
    # steps_large = days_until_today
    steps_inner = 687 * 2
    h_timestep = 0.5  # 4 days as timesteps
    r=r_orig.copy()
    v=v_orig.copy()
    m=m_orig.copy()
    rx = np.zeros((steps_inner, N))
    ry = np.zeros((steps_inner, N))
    rz = np.zeros((steps_inner, N))
    for i in range(steps_inner):
        vi1, ri1 = solar_leap_frog(r, v, h_timestep, accel)
        rx[i] = ri1[:, 0]
        ry[i] = ri1[:, 1]
        rz[i] = ri1[:, 2]
        v, r = vi1, ri1
    axs[0][0].plot(rx[:, 0:5], ry[:, 0:5])
    axs[0][0].set_title("Inner Planets XY")
    axs[1][0].plot(rx[:, 0:5], rz[:, 0:5])
    axs[1][0].set_title("Inner Planets XZ")

    print("Plotting Outer Planets...")
    steps_outer = 165 * 365
    h_timestep = 4
    r=r_orig.copy()
    v=v_orig.copy()
    m=m_orig.copy()
    rx = np.zeros((steps_outer, N))
    ry = np.zeros((steps_outer, N))
    rz = np.zeros((steps_outer, N))
    for i in range(steps_outer):
        vi1, ri1 = solar_leap_frog(r, v, h_timestep, accel)
        rx[i] = ri1[:, 0]
        ry[i] = ri1[:, 1]
        rz[i] = ri1[:, 2]
        v, r = vi1, ri1
    axs[0][1].plot(rx[:, 5:9], ry[:, 5:9])
    axs[0][1].set_title("Outer Planets XY")
    axs[1][1].plot(rx[:, 5:9], rz[:, 5:9])
    axs[1][1].set_title("Inner Planets XZ")

    plt.savefig("orrery-planets.png")

    print("Plotting Barycentre...")
    # NOTE: calculate from 2008 until today
    today = str(date.today())
    days_until_today = int(get_julian_date(today) - get_julian_date("2008-03-18"))
    end_time = days_until_today // h_timestep

    r=r_orig.copy()
    v=v_orig.copy()
    m=m_orig.copy()
    fig2, axs2 = plt.subplots()
    axs2.set_title("Solar system barycentre")
    rx = np.zeros((end_time, N))
    ry = np.zeros((end_time, N))
    rz = np.zeros((end_time, N))
    center = np.zeros((end_time, 3))
    m_av = sum(m)
    for i in range(end_time):
        vi1, ri1 = solar_leap_frog(r, v, h_timestep, accel)
        center_of_m = np.zeros(3)
        for j in range(len(m)):
            center_of_m += ri1[j] * m[j]
        center_of_m /= m_av
        center[i] = center_of_m
        rx[i] = ri1[:, 0]
        ry[i] = ri1[:, 1]
        rz[i] = ri1[:, 2]
        v, r = vi1, ri1
    new_cx = center[:, 0] - rx[:, 0]
    new_cy = center[:, 1] - ry[:, 0]
    new_cz = center[:, 2] - rz[:, 0]

    sun = plt.Circle((0, 0), 0.00465047, color="gold")
    axs2.add_patch(sun)
    axs2.plot(-new_cx, -new_cy, "-", color="black")
    axs2.set_aspect("equal")

    # plt.show()
    plt.savefig("orrery-barycentre.png")
