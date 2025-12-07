#Exercicio 3 - Caos 3D: Sistema de Lorenz

import numpy as np
import matplotlib.pyplot as plt

# Constantes do Sistema de Lorenz
sigma = 10
B = 8 / 3
tmax = 100
iter_max = 10000
Dt = tmax / iter_max

def lorenz(vet, r, ndim):
    x, y, z = vet
    dx = -sigma * x + sigma * y
    dy = -x * z + r * x - y
    dz = x * y - B * z

    g = np.zeros(ndim)
    g[0] = dx
    g[1] = dy
    g[2] = dz
    return g

def rk4(vet, dt, r, ndim):
    c1 = dt * lorenz(vet, r, ndim)
    c2 = dt * lorenz(vet + c1 / 2, r, ndim)
    c3 = dt * lorenz(vet + c2 / 2, r, ndim)
    c4 = dt * lorenz(vet + c3, r, ndim)
    return vet + (c1 + 2 * c2 + 2 * c3 + c4) / 6

def main():
    """
    Função principal para executar a simulação do sistema de Lorenz.
    """
    ndim = 3  # Dimensão do sistema (x, y, z)
    estados_iniciais = [np.array([10, 10, 10]), np.array([15, 1, -10])]
    r_valores = [0.7, 10, 28]
    cores = ['black', 'blue']  # Cores específicas para as diferentes condições iniciais

    for r in r_valores:
        plt.figure(figsize=(18, 12))

        # Subplots para as três projeções (XY, YZ, XZ)
        for i, estado_inicial in enumerate(estados_iniciais):
            estado = estado_inicial.copy()

            trajetoria_x = [estado[0]]
            trajetoria_y = [estado[1]]
            trajetoria_z = [estado[2]]

            # Simulação com Runge-Kutta 4ª ordem
            for _ in range(iter_max):
                estado = rk4(estado, Dt, r, ndim)
                trajetoria_x.append(estado[0])
                trajetoria_y.append(estado[1])
                trajetoria_z.append(estado[2])

            # Plotar as projeções XY, YZ, e XZ no mesmo gráfico, para comparar as trajetórias
            plt.subplot(3, 3, 1)
            plt.plot(trajetoria_x, trajetoria_y, color=cores[i])
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title(f"Projeção XY (r={r})")
            plt.grid()

            plt.subplot(3, 3, 2)
            plt.plot(trajetoria_y, trajetoria_z, color=cores[i])
            plt.xlabel("y")
            plt.ylabel("z")
            plt.title(f"Projeção YZ (r={r})")
            plt.grid()

            plt.subplot(3, 3, 3)
            plt.plot(trajetoria_x, trajetoria_z, color=cores[i])
            plt.xlabel("x")
            plt.ylabel("z")
            plt.title(f"Projeção XZ (r={r})")
            plt.grid()

        plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
