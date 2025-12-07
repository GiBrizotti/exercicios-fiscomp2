#Exercício 2 - Soluções de EDO's Variadas

import math
import numpy as np
import matplotlib.pyplot as plt

# Função para resolver a EDO utilizando o método de Picard
def picard(y, t, dt, ndim, questao):
    y1 = y + g(y, t, ndim, questao) * dt
    t1 = t + dt
    return y + (g(y, t, ndim, questao) + g(y1, t1, ndim, questao)) * dt / 2

def g(y, t, ndim, questao):
    if questao == 'a':
        # y'' = (-4y' + 3y) / 7
        g_a = np.zeros(ndim)
        g_a[0] = y[1]
        g_a[1] = (-4 * y[1] + 3 * y[0]) / 7
        return g_a
    if questao == 'b':
        # y''' = 8y/x³ * y
        g_b = np.zeros(ndim)
        g_b[0] = y[1]
        g_b[1] = y[2]
        g_b[2] = (8 / t**3) * y[0]
        return g_b
    if questao == 'c':
        # y"" = (-3y' + 2y) / (x+2)
        g_c = np.zeros(ndim)
        g_c[0] = y[1]
        g_c[1] = y[2]
        g_c[2] = y[3]
        g_c[3] = (-3 * y[1] + 2 * y[0]) / (t + 2)
        return g_c
    if questao == 'd':
        # y""' = 9y'
        g_d = np.zeros(ndim)
        g_d[0] = y[1]
        g_d[1] = y[2]
        g_d[2] = y[3]
        g_d[3] = y[4]
        g_d[4] = 9 * y[1]
        return g_d

def Simulaprograma(tmax, Dt, ndim, questao, x_init, y_init):
    Nt = int(tmax / Dt)

    t = [x_init]
    y_picard = [np.array(y_init)]

    for i in range(Nt - 1):
        t.append(t[i] + Dt)
        y_picard.append(picard(y_picard[i], t[i], Dt, ndim, questao))

    XX = [y_picard[i][0] for i in range(Nt)]
    YY = [y_picard[i][1] for i in range(Nt)]

    if ndim == 2:
        return t, XX, YY
    elif ndim == 3:
        ZZ = [y_picard[i][2] for i in range(Nt)]
        return t, XX, YY, ZZ
    elif ndim == 4:
        ZZ = [y_picard[i][2] for i in range(Nt)]
        JJ = [y_picard[i][3] for i in range(Nt)]
        return t, XX, YY, ZZ, JJ
    elif ndim == 5:
        ZZ = [y_picard[i][2] for i in range(Nt)]
        JJ = [y_picard[i][3] for i in range(Nt)]
        KK = [y_picard[i][4] for i in range(Nt)]
        return t, XX, YY, ZZ, JJ, KK
    else:
        raise ValueError("Número de dimensões inválido.")

# Função de fazer gráfico
def plotar_posicao(t, y_data, labels, dt, metodo, ax):
    for data, label in zip(y_data, labels):
        ax.plot(t, data, label=f"{label} (dt = {dt})")
    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Valor")
    ax.set_title(f"Método de {metodo}")
    ax.grid(True)
    ax.legend()

def main():
    questões = ['a', 'b', 'c', 'd']
    x_inicial = [0.0, 1.0, -1.0, 1.0]
    y_inicial = [
        [0.0, 1.0],                # Para questão 'a'
        [1.0, 1.0, 0.0],           # Para questão 'b'
        [3.0, -1.0, 0.0, 1.0],     # Para questão 'c'
        [2.0, 0.0, 0.0, 1.0, 1.0]  # Para questão 'd'
    ]

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle("Soluções das EDOs - Método de Picard", fontsize=16)

    for idx, questão in enumerate(questões):
        ndim = len(y_inicial[idx])
        t, *y_data = Simulaprograma(5, 0.01, ndim, questão, x_inicial[idx], y_inicial[idx])

        ax = axes[idx // 2, idx % 2]

        # Definir rótulos de acordo com a derivada
        labels = ["Função"] + [f"Derivada de {ordem}ª ordem" for ordem in range(1, ndim)]

        plotar_posicao(t, y_data, labels, 0.01, f"Picard - Questão {questão}", ax)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

main()
