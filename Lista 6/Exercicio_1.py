import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numba import njit

def inicializar_corda(L, Nx, a0, x0, sigma):
    x = np.linspace(0, L, Nx + 1)
    y0 = a0 * np.exp((-(x - x0) ** 2) / sigma)
    return x, y0

@njit
def contorno(y):
    y[:, 0] = 0  # Extremidade esquerda fixa
    y[:, -1] = 0  # Extremidade direita fixa
    return y

@njit
def resolver_onda(y0, Nx, Nt, dt, dx, v):
    y = np.zeros((Nt + 1, Nx + 1))
    y = contorno(y)
    y[0, :] = y0
    y[1, :] = y0
    dt2 = dt ** 2
    v2 = v ** 2

    for n in range(1, Nt):
        for i in range(1, Nx):
            yxx = (y[n, i + 1] - 2 * y[n, i] + y[n, i - 1]) / dx ** 2
            y[n + 1, i] = dt2 * v2 * yxx + 2 * y[n, i] - y[n - 1, i]
        y = contorno(y)
    return y

def plotar_onda(x, y, dt, Nt):
    t = np.linspace(0, dt * Nt, Nt + 1)
    X, T = np.meshgrid(x, t)

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, T, y, cmap='plasma')
    ax.view_init(elev=90, azim=(180+45))
    ax.set_xlabel('Posição (m)')
    ax.set_ylabel('Tempo (s)')
    ax.set_zlabel('Deslocamento (m)')
    plt.show()

def main():
    #Espaço:
    L = 1
    Nx = 100
    dx = L / Nx
    x0 = 0.5

    #Tempo:
    tmax = 6
    dt = 0.01
    Nt = int(tmax / dt)

    #Corda:
    T = 1
    rho = 1
    v = np.sqrt(T / rho)
    a0 = 1e-3
    sigma = 0.01

    x, y0 = inicializar_corda(L, Nx, a0, x0, sigma)
    y = resolver_onda(y0, Nx, Nt, dt, dx, v)
    plotar_onda(x, y, dt, Nt)

if __name__ == "__main__":
    main()