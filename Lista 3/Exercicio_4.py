#Exercício 4 - Correções relativísticas na órbita de Mercúrio

import numpy as np
import matplotlib.pyplot as plt

def rk4(y, t, dt, ndim):
    c1 = dt * g(y, t, ndim)
    c2 = dt * g(y + c1 / 2, t + dt / 2, ndim)
    c3 = dt * g(y + c2 / 2, t + dt / 2, ndim)
    c4 = dt * g(y + c3, t + dt, ndim)
    return y + (c1 + 2 * c2 + 2 * c3 + c4) / 6

def g(y, t, ndim):
    G = 6.67e-11  # Constante gravitacional (Nm^2 kg^-2)
    M_s = 1.99e30  # Massa do Sol (kg)
    M_m = 3.285e23  # Massa de Mercúrio (kg)
    R_T = 1.496e11  # Distância média Terra-Sol (m)
    alpha = 0.010 * R_T**2  # Valor de alpha

    g = np.zeros(ndim)

    # Ordem: [x, y, vx, vy]
    r = np.sqrt(y[0]**2 + y[1]**2)

    # Correção relativística na força gravitacional
    F_rel = (G * M_s * M_m) / (r**3) * (1 + alpha / r**2)

    # Equações diferenciais
    g[0] = y[2]  # dx/dt = vx
    g[1] = y[3]  # dy/dt = vy
    g[2] = -F_rel * y[0] / M_m  # dvx/dt
    g[3] = -F_rel * y[1] / M_m  # dvy/dt

    return g

def Simular(tmax, dt, ndim, x0, y0, vx0, vy0):
    Nt = int(tmax / dt)

    t = [0.0]
    y_rk4 = [np.array([x0, y0, vx0, vy0])]
    for i in range(Nt - 1):
        t.append(t[i] + dt)
        y_rk4.append(rk4(y_rk4[i], t[i], dt, ndim))

    XX_rk4 = [y_rk4[i][0] for i in range(Nt)]
    YY_rk4 = [y_rk4[i][1] for i in range(Nt)]

    RK4 = [XX_rk4, YY_rk4]

    return t, RK4

def Plotar_orbita_mercurio():
    # Valores iniciais
    x0 = 0.703120e11  # Posicao inicial em x (m)
    y0 = 0  # Posicao inicial em y (m)
    vx0 = 0  # Velocidade inicial em x (m/s)
    vy0 = 3.8899e4  # Velocidade inicial em y (m/s)

    # Tempo de simulação
    ANO_TERRA = 365.25 * 24 * 60 * 60  # Tempo de um ano terrestre em segundos
    dt = ANO_TERRA / 2000  # Passo de tempo

    # Simular órbita de Mercúrio
    tempo, RK4_graph = Simular(ANO_TERRA, dt, 4, x0, y0, vx0, vy0)

    # Plotar resultado
    plt.figure(figsize=(10, 8))
    plt.plot(RK4_graph[0], RK4_graph[1], label='Órbita de Mercúrio', color='blue')
    plt.scatter(0, 0, color="orange", label="Sol", s=100)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Órbita de Mercúrio com Correções Relativísticas')
    plt.legend()
    plt.axis('equal')
    plt.grid()
    plt.show()

def main():
    Plotar_orbita_mercurio()

if __name__ == '__main__':
    main()