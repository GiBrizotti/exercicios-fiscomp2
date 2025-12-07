#Exercício 7 - Teorema de Bertrand

import numpy as np
import matplotlib.pyplot as plt


def picard(y, t, dt, params):
    y1 = y + g(y, t, params) * dt
    t1 = t + dt
    return y + (g(y, t, params) + g(y1, t1, params)) * dt / 2


def g(y, t, params):
    k, alpha = params
    r = np.sqrt(y[0]**2 + y[1]**2)
    r_hat = y / r  # Versor radial
    force = -k * r**alpha
    g_v = np.zeros(4)
    # dy/dt = y' (atual posição é x e y, e suas derivadas são vx e vy)
    g_v[0] = y[2]  # dx/dt = vx
    g_v[1] = y[3]  # dy/dt = vy
    # dvx/dt e dvy/dt
    g_v[2] = force * r_hat[0]
    g_v[3] = force * r_hat[1]
    return g_v


def Simulaprograma(tmax, dt, params, y_init):
    Nt = int(tmax / dt)
    t = [0.0]
    y_picard = [np.array(y_init)]

    for i in range(Nt - 1):
        t.append(t[i] + dt)
        y_picard.append(picard(y_picard[i], t[i], dt, params))

    XX = [y_picard[i][0] for i in range(Nt)]  # Posição x
    YY = [y_picard[i][1] for i in range(Nt)]  # Posição y
    return XX, YY


def plotar_orbita(XX, YY, titulo, ax, cor):
    ax.plot(XX, YY, label=titulo, color=cor)
    ax.set_xlabel("Posição X (m)")
    ax.set_ylabel("Posição Y (m)")
    ax.set_title(titulo)
    ax.grid(True)
    ax.legend()


def main():
    # Valores do exercício
    k = 1.0  # Constante k
    tmax = 20.0  # Tempo máximo de simulação
    dt = 0.0001  # Passo temporal
    alphas = [2, 1, 0, -1, -2, -3]  # Valores de alpha

    # Lista de cores para cada valor de alpha
    cores = ['b', 'g', 'r', 'c', 'm', 'y']

    # Condições iniciais
    r_init = [1.0, 0.0]  # r_0 = i
    v_init = [0.5, 1.0]  # v_0 = 0.5i + j
    y_init = r_init + v_init  # Estado inicial [x, y, vx, vy]

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle("Demonstração Numérica do Teorema de Bertrand", fontsize=16)

    for idx, alpha in enumerate(alphas):
        params = (k, alpha)
        XX, YY = Simulaprograma(tmax, dt, params, y_init)

        ax = axes[idx // 3, idx % 3]
        plotar_orbita(XX, YY, f"Alpha = {alpha}", ax, cores[idx])

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

main()
