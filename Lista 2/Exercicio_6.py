#Exercício 6 - A Catenária

import numpy as np
import matplotlib.pyplot as plt


def picard(y, t, dt, params):
    y1 = y + g(y, t, params) * dt
    t1 = t + dt
    return y + (g(y, t, params) + g(y1, t1, params)) * dt / 2


def g(y, t, params):
    omega_0, T_0 = params
    g_v = np.zeros(2)
    # dy/dt = y'
    g_v[0] = y[1]
    # dy'/dt = (omega_0 / T_0) * sqrt(1 + (y')^2)
    g_v[1] = (omega_0 / T_0) * np.sqrt(1 + (y[1])**2)
    return g_v


def Simulaprograma(tmax, dt, params, y_init):
    Nt = int(tmax / dt)
    t = [0.0]
    y_picard = [np.array(y_init)]

    for i in range(Nt - 1):
        t.append(t[i] + dt)
        y_picard.append(picard(y_picard[i], t[i], dt, params))

    XX = [t[i] for i in range(Nt)]  # Posição x
    YY = [y_picard[i][0] for i in range(Nt)]  # Posição y
    return XX, YY


def plotar_posicao(XX, YY, titulo, ax):
    ax.plot(XX, YY, label=titulo)
    ax.set_xlabel("Distância Horizontal x (m)")
    ax.set_ylabel("Altura f(x) (m)")
    ax.set_title(titulo)
    ax.grid(True)
    ax.legend()


def main():
    # Valores do exercício
    omega_0 = 0.77  # Densidade linear de massa, kg/m
    T_0 = 150.0     # Tensão da corda, N
    tmax = 25.0     # Distância horizontal entre os postes, m
    dt = 0.1        # Passo, m

    # Condições iniciais
    y_init = [5.0, -0.1445]  # f(x = A) = 5m, f'(x = A) = -0.1445

    # Parâmetros (omega_0, T_0)
    params = (omega_0, T_0)

    # Simular a forma da catenária
    XX, YY = Simulaprograma(tmax, dt, params, y_init)

    # Plot da catenária
    fig, ax = plt.subplots(figsize=(10, 6))
    plotar_posicao(XX, YY, "Forma da Catenária", ax)
    plt.tight_layout()
    plt.show()

    # Item (a): Altura do segundo poste
    altura_segundo_poste = YY[-1]
    print(f"Altura do segundo poste (ponto B): {altura_segundo_poste:.2f} m")

    # Item (b): Novo valor de f'(x = A) para que o segundo poste tenha a mesma altura do primeiro
    y_init_b = [5.0, -0.1]  # Chute inicial para f'(x = A)
    max_iter_b = 10000  # Limite máximo de iterações para evitar loop infinito
    iter_count_b = 0
    while iter_count_b < max_iter_b:
        XX, YY_b = Simulaprograma(tmax, dt, params, y_init_b)
        if abs(YY_b[-1] - 5.0) < 0.01:
            break
        y_init_b[1] += 0.001  # Ajuste incremental
        iter_count_b += 1
    if iter_count_b >= max_iter_b:
        print("Atingido o limite máximo de iterações para o item (b)")
    print(f"Novo valor de f'(x = A) para o segundo poste ter a mesma altura: {y_init_b[1]:.4f}")

    # Item (c): Novo valor de T_0 para que o segundo poste tenha a mesma altura do primeiro
    T_0_min, T_0_max = 100.0, 300.0  # Definindo limites para a busca
    tolerance = 0.01
    while T_0_max - T_0_min > tolerance:
        T_0_c = (T_0_min + T_0_max) / 2
        params_c = (omega_0, T_0_c)
        XX, YY_c = Simulaprograma(tmax, dt, params_c, y_init)
        if YY_c[-1] > 5.0:
            T_0_max = T_0_c
        else:
            T_0_min = T_0_c

    print(f"Novo valor de T_0 para o segundo poste ter a mesma altura: {T_0_c:.2f} N")

    # Item (d): Distância mínima entre a corda e o solo para os itens (a), (b), e (c)
    distancia_minima_a = min(YY)
    distancia_minima_b = min(YY_b)
    distancia_minima_c = min(YY_c)
    print(f"Distância mínima entre a corda e o solo - Item (a): {distancia_minima_a:.2f} m")
    print(f"Distância mínima entre a corda e o solo - Item (b): {distancia_minima_b:.2f} m")
    print(f"Distância mínima entre a corda e o solo - Item (c): {distancia_minima_c:.2f} m")

main()
