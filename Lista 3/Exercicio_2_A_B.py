#Exercício 2 - Problema dos Três Corpos: Influência da órbita de Júpiter na órbita da Terra
#Itens A e B

import numpy as np
import matplotlib.pyplot as plt

def rk4(y, t, dt, ndim):
    c1 = dt * g(y, t, ndim)
    c2 = dt * g(y + c1 / 2, t + dt / 2, ndim)
    c3 = dt * g(y + c2 / 2, t + dt / 2, ndim)
    c4 = dt * g(y + c3, t + dt, ndim)
    return y + (c1 + 2 * c2 + 2 * c3 + c4) / 6

def g(y, t, ndim):
    # m * r'' = G(M * m) / r**2
    G, M = 6.67430e-11, 1.989e30  # Constante gravitacional e massa do Sol

    g = np.zeros(ndim)

    # Ordem: [x, y, vx, vy]
    r = np.sqrt(y[0]**2 + y[1]**2)

    g[0] = y[2]  # dx/dt = vx
    g[1] = y[3]  # dy/dt = vy
    g[2] = -G * M * y[0] / r**3  # Força gravitacional em x
    g[3] = -G * M * y[1] / r**3  # Força gravitacional em y
    return g

def Simular(tmax, dt, ndim, R_P, V_P):
    Nt = int(tmax / dt)

    t = [0.0]
    y_rk4 = [np.array([R_P, 0.0, 0.0, V_P])]
    for i in range(Nt - 1):
        t.append(t[i] + dt)
        y_rk4.append(rk4(y_rk4[i], t[i], dt, ndim))

    XX_rk4 = [y_rk4[i][0] for i in range(Nt)]
    YY_rk4 = [y_rk4[i][1] for i in range(Nt)]

    RK4 = [XX_rk4, YY_rk4]

    return t, RK4

def Plotar_questao_a():
    ANO_s = 365.25 * 24 * 60 * 60
    t_terra = ANO_s
    R_T = 1.496e11
    V_T = (2 * np.pi * R_T) / t_terra
    tempo, RK4_graph = Simular(t_terra, ANO_s * 10**-5, 4, R_T, V_T)  # Simular Terra

    plt.plot(RK4_graph[0], RK4_graph[1], label='Órbita da Terra', color='red')
    plt.scatter(0, 0, color="orange", label="Sol", s=10)
    plt.ylabel('y (m)')
    plt.xlabel('x (m)')
    plt.title("Órbita da Terra ao redor do Sol (RK4)")
    plt.legend()
    plt.grid()
    plt.axis('equal')
    plt.show()

    return tempo, RK4_graph

def Plotar_questao_b(t_terra, RK4_terra):
    # Dados de Júpiter
    R_T = 1.496e11
    R_J = 5.2 * R_T  # Distância média de Júpiter ao Sol
    G = 6.67430e-11
    M = 1.989e30  # Massa do Sol
    V_J = np.sqrt(G * M / R_J)  # Velocidade orbital inicial de Júpiter

    ANO_Jupiter = 11.86 * 365.25 * 24 * 60 * 60  # Tempo de 1 ano jupiteriano

    # Simular Júpiter
    tempo_jupiter, RK4_graph_jupiter = Simular(ANO_Jupiter, ANO_Jupiter * 10**-5, 4, R_J, V_J)

    # Plotar órbitas da Terra e Júpiter
    plt.plot(RK4_terra[0], RK4_terra[1], label='Órbita da Terra', color='red')
    plt.plot(RK4_graph_jupiter[0], RK4_graph_jupiter[1], label='Órbita de Júpiter', color='blue')
    plt.scatter(0, 0, color="orange", label="Sol", s=10)
    plt.ylabel('y (m)')
    plt.xlabel('x (m)')
    plt.title("Órbitas da Terra e de Júpiter ao redor do Sol (RK4)")
    plt.legend()
    plt.grid()
    plt.axis('equal')
    plt.show()

def main():
    terrat, terraxy = Plotar_questao_a()  # Simula e plota a Terra
    Plotar_questao_b(terrat, terraxy)  # Adiciona a órbita de Júpiter

if __name__ == '__main__':
    main()
