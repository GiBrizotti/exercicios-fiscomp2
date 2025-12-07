#Exercício 3 - Solução Numérica da Equação de Bessel

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson


def picard(y, t, dt, p):
    y1 = y + g(y, t, p) * dt
    t1 = t + dt
    return y + (g(y, t, p) + g(y1, t1, p)) * dt / 2

def g(y, t, p):
    # Definindo a equação de Bessel
    # x^2 y'' + x y' + (x^2 - p^2) y = 0
    g_b = np.zeros(2)
    g_b[0] = y[1]  # dy/dt = y'
    g_b[1] = -(t**2 - p**2) * y[0] / t**2 - y[1] / t  # dy'/dt = y''
    return g_b

# Função de Simulação
def Simulaprograma(tmax, dt, p, x_init, y_init):
    Nt = int(tmax / dt)
    t = [x_init]
    y_picard = [np.array(y_init)]

    for i in range(Nt - 1):
        t.append(t[i] + dt)
        y_picard.append(picard(y_picard[i], t[i], dt, p))

    XX = [y_picard[i][0] for i in range(Nt)]
    YY = [y_picard[i][1] for i in range(Nt)]

    return t, XX, YY

# Função para normalizar a solução
def normalizar(t, XX):
    area = simpson(y=np.array(XX) ** 2, x=t)
    C = 1 / np.sqrt(area)
    return [C * x for x in XX]


def plotar_posicao(t, XX, p, ax):
    ax.plot(t, XX, label=f"p = {p}", color = 'red')
    ax.set_xlabel("x")
    ax.set_ylabel("y(x)")
    ax.set_title(f"Solução da Equação de Bessel para p = {p}")
    ax.grid(True)
    ax.legend()

def main():
    # Valores iniciais do exercício
    ps = [0, 1, 2, 3, 4]
    tmax = 20.0
    dt = 0.1
    x_inicial = 0.0001

    y_iniciais = [
        [1.0, -0.0001],  # Condições iniciais para p = 0
        [0.0001, 1.0],   # Condições iniciais para p = 1
        [0.0001, 1.0],   # Condições iniciais para p = 2
        [0.0001, 1.0],   # Condições iniciais para p = 3
        [0.0001, 1.0]    # Condições iniciais para p = 4
    ]

    fig, axes = plt.subplots(3, 2, figsize=(15, 15))
    fig.suptitle("Soluções da Equação de Bessel - Método de Picard", fontsize=16)

    for idx, p in enumerate(ps):
        t, XX, YY = Simulaprograma(tmax, dt, p, x_inicial, y_iniciais[idx])
        XX_normalizado = normalizar(t, XX)

        ax = axes[idx // 2, idx % 2]
        plotar_posicao(t, XX_normalizado, p, ax)



    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

main()
