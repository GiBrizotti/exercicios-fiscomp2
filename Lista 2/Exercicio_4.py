#Exercício 4 - Sistema de Equações Diferenciais

import numpy as np
import matplotlib.pyplot as plt

def picard(y, t, dt, mu):
    y1 = y + g(y, t, mu) * dt
    t1 = t + dt
    return y + (g(y, t, mu) + g(y1, t1, mu)) * dt / 2


def g(y, t, mu):
    # Definindo as equações de Van der Pol
    # dx/dt = y - f_mu(x)
    # dy/dt = -x
    g_v = np.zeros(2)
    g_v[0] = y[1] - (y[0] ** 3 - mu * y[0])  # dx/dt = y - f_mu(x)
    g_v[1] = -y[0]                          # dy/dt = -x
    return g_v

def Simulaprograma(tmax, dt, mu, x_init, y_init):
    Nt = int(tmax / dt)
    t = [0.0]
    y_picard = [np.array([x_init, y_init])]

    for i in range(Nt - 1):
        t.append(t[i] + dt)
        y_picard.append(picard(y_picard[i], t[i], dt, mu))

    XX = [y_picard[i][0] for i in range(Nt)]
    YY = [y_picard[i][1] for i in range(Nt)]

    return t, XX, YY

def plotar_posicao(XX, YY, mu, ax):
    ax.plot(XX, YY, label=f"µ = {mu}", color = 'red')
    ax.set_xlabel("x(t)")
    ax.set_ylabel("y(t)")
    ax.set_title(f"Trajetória no Plano Fase para µ = {mu}")
    ax.grid(True)
    ax.legend()


def main():
    # Valores iniciais do exercício
    mus = [-1, -0.5, 0, 0.5, 1]
    tmax = 20.0
    dt = 0.01
    condicoes_iniciais = [
        (0.0, 1.0),
        (1.0, 0.0),
        (0.0, -1.0),
        (-1.0, 0.0)
    ]

    fig, axes = plt.subplots(len(mus), len(condicoes_iniciais), figsize=(20, 15))
    fig.suptitle("Trajetórias de Van der Pol para Diferentes Valores de µ e Condições Iniciais", fontsize=16)

    for idx_mu, mu in enumerate(mus):
        for idx_cond, (x_init, y_init) in enumerate(condicoes_iniciais):
            t, XX, YY = Simulaprograma(tmax, dt, mu, x_init, y_init)
            ax = axes[idx_mu, idx_cond]
            plotar_posicao(XX, YY, mu, ax)
            ax.set_title(f"µ = {mu}, Cond. Inicial: (x0, y0) = ({x_init}, {y_init})")

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

main()
