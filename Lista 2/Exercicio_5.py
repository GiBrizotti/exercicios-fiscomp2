#Exercício 5 - Determinação numérica das órbitas de corpos celestes

import numpy as np
import matplotlib.pyplot as plt


def picard(y, t, dt, params):
    y1 = y + g(y, t, params) * dt
    t1 = t + dt
    return y + (g(y, t, params) + g(y1, t1, params)) * dt / 2

# Função g para calcular a dinâmica orbital considerando a força gravitacional
def g(y, t, params):
    G, M = params
    r = np.sqrt(y[0]**2 + y[2]**2)  # Distância radial
    g_v = np.zeros(4)
    # dx/dt = vx
    g_v[0] = y[1]
    # dvx/dt = -G*M * x / r^3
    g_v[1] = -G * M * y[0] / r**3
    # dy/dt = vy
    g_v[2] = y[3]
    # dvy/dt = -G*M * y / r^3
    g_v[3] = -G * M * y[2] / r**3
    return g_v


def Simulaprograma(tmax, dt, params, y_init):
    Nt = int(tmax / dt)
    t = [0.0]
    y_picard = [np.array(y_init)]

    for i in range(Nt - 1):
        t.append(t[i] + dt)
        y_picard.append(picard(y_picard[i], t[i], dt, params))

    XX = [y_picard[i][0] for i in range(Nt)]  # Posição x
    YY = [y_picard[i][2] for i in range(Nt)]  # Posição y
    return t, XX, YY


def plotar_posicao(XX, YY, titulo, ax):
    ax.plot(XX, YY, label=titulo, color='purple')
    ax.set_xlabel("Posição X (m)")
    ax.set_ylabel("Posição Y (m)")
    ax.set_title(titulo)
    ax.grid(True)
    ax.legend()


def main():
    # Valores iniciais do exercício
    G = 6.67430e-11  # Constante gravitacional, m^3 kg^-1 s^-2
    M = 1.989e30     # Massa do Sol, kg
    anos_orbita = 76  # Período orbital em anos

    # Convertendo o período orbital para segundos
    tmax = anos_orbita * 365.25 * 24 * 60 * 60  # Convertendo anos para segundos
    dt = 1e5         # Passo temporal em segundos

    # Condições iniciais do cometa no afélio
    x0 = 5.28e12     # Distância ao sol no afélio, m
    y0 = 0.0
    vx0 = 0.0
    vy0 = 9.12e2     # Velocidade no afélio, m/s
    y_init = [x0, vx0, y0, vy0]

    # Parâmetros (G, M)
    params = (G, M)

    # Simular a órbita do cometa Halley
    t, XX, YY = Simulaprograma(tmax, dt, params, y_init)

    # Cálculo da distância mínima (periélio)
    distancias = [np.sqrt(x**2 + y**2) for x, y in zip(XX, YY)]
    distancia_minima = min(distancias)
    print(f"Distância mínima ao Sol (periélio): {distancia_minima:.2e} m")

    # Cálculo da velocidade máxima
    velocidades = [np.sqrt(y_pic[1]**2 + y_pic[3]**2) for y_pic in [np.array([x, vx, y, vy]) for x, vx, y, vy in zip(XX, [y_init[1]]*len(XX), YY, [y_init[3]]*len(YY))]]
    velocidade_maxima = max(velocidades)
    print(f"Velocidade máxima do cometa: {velocidade_maxima:.2e} m/s")

    # Tempo de uma órbita completa em anos
    print(f"Tempo necessário para uma órbita completa: {anos_orbita} anos")

    # Plotagem da órbita
    fig, ax = plt.subplots(figsize=(10, 10))
    plotar_posicao(XX, YY, "Órbita do Cometa Halley", ax)
    plt.tight_layout()
    plt.show()

main()
