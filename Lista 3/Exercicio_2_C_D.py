#Exercício 2 - Problema dos Três Corpos: Influência da órbita de Júpiter na órbita da Terra
#Itens C e D

import numpy as np
import matplotlib.pyplot as plt

def rk4(y, t, dt, ndim, M_jupiter):
    c1 = dt * g(y, t, ndim, M_jupiter)
    c2 = dt * g(y + c1 / 2, t + dt / 2, ndim, M_jupiter)
    c3 = dt * g(y + c2 / 2, t + dt / 2, ndim, M_jupiter)
    c4 = dt * g(y + c3, t + dt, ndim, M_jupiter)
    return y + (c1 + 2 * c2 + 2 * c3 + c4) / 6

def g(y, t, ndim, M_jupiter=0):
    G = 6.67430e-11
    M_sun = 1.989e30
    epsilon = 1e-10  # Pequeno valor para evitar divisão por zero KKKKKKKKKKKK

    g = np.zeros(ndim)

    # Ordem: [x_terra, y_terra, vx_terra, vy_terra, x_jupiter, y_jupiter, vx_jupiter, vy_jupiter]
    r_terra = np.sqrt(y[0]**2 + y[1]**2)
    r_jupiter = np.sqrt(y[4]**2 + y[5]**2)

    # Terra ao redor do Sol
    g[0] = y[2]  # dx/dt = vx
    g[1] = y[3]  # dy/dt = vy
    g[2] = -G * M_sun * y[0] / (r_terra**3 + epsilon)
    g[3] = -G * M_sun * y[1] / (r_terra**3 + epsilon)

    # Júpiter ao redor do Sol
    g[4] = y[6]  # dx/dt = vx
    g[5] = y[7]  # dy/dt = vy
    g[6] = -G * M_sun * y[4] / (r_jupiter**3 + epsilon)
    g[7] = -G * M_sun * y[5] / (r_jupiter**3 + epsilon)

    # Interação Terra-Júpiter
    r_TJ = np.sqrt((y[4] - y[0])**2 + (y[5] - y[1])**2)
    if M_jupiter != 0:
        g[2] += -G * M_jupiter * (y[0] - y[4]) / (r_TJ**3 + epsilon)  # Aceleração da Terra devido a Júpiter
        g[3] += -G * M_jupiter * (y[1] - y[5]) / (r_TJ**3 + epsilon)
        g[6] += -G * M_jupiter * (y[4] - y[0]) / (r_TJ**3 + epsilon)  # Aceleração de Júpiter devido à Terra
        g[7] += -G * M_jupiter * (y[5] - y[1]) / (r_TJ**3 + epsilon)

    return g

def Simular(tmax, dt, ndim, R_T, V_T, R_J, V_J, M_jupiter=0):
    Nt = int(tmax / dt)

    t = [0.0]
    y_rk4 = [np.array([R_T, 0.0, 0.0, V_T, R_J, 0.0, 0.0, V_J])]
    for i in range(Nt - 1):
        t.append(t[i] + dt)
        y_rk4.append(rk4(y_rk4[i], t[i], dt, ndim, M_jupiter))

    XX_rk4_terra = [y_rk4[i][0] for i in range(Nt)]
    YY_rk4_terra = [y_rk4[i][1] for i in range(Nt)]
    XX_rk4_jupiter = [y_rk4[i][4] for i in range(Nt)]
    YY_rk4_jupiter = [y_rk4[i][5] for i in range(Nt)]

    RK4_terra = [XX_rk4_terra, YY_rk4_terra]
    RK4_jupiter = [XX_rk4_jupiter, YY_rk4_jupiter]

    return t, RK4_terra, RK4_jupiter

def calcular_desvio_maximo(RK4_terra_com_jupiter, RK4_terra_sem_jupiter):
    desvio_maximo = 0
    for i in range(len(RK4_terra_com_jupiter[0])):
        desvio = np.sqrt((RK4_terra_com_jupiter[0][i] - RK4_terra_sem_jupiter[0][i])**2 +
                         (RK4_terra_com_jupiter[1][i] - RK4_terra_sem_jupiter[1][i])**2)
        if desvio > desvio_maximo:
            desvio_maximo = desvio
    return desvio_maximo / 1000  # Converter para quilômetros

def plotar_orbitas(RK4_terra_sem_jupiter, RK4_terra_com_jupiter, title, desvio_maximo):
    plt.figure(figsize=(10, 8))
    plt.plot(RK4_terra_sem_jupiter[0], RK4_terra_sem_jupiter[1], label='Terra sem Júpiter', color='red', linewidth = 4)
    plt.plot(RK4_terra_com_jupiter[0], RK4_terra_com_jupiter[1], label='Terra com Júpiter', color='blue', )
    plt.scatter(0, 0, color="orange", label="Sol", s=100)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title(f'{title}\nDesvio Máximo = {desvio_maximo:.2f} km')
    plt.legend()
    plt.axis('equal')
    plt.grid()
    plt.show()

def Plotar_resultados_cd():
    R_T = 1.496e11
    V_T = (2 * np.pi * R_T) / (365.25 * 24 * 60 * 60)  # Velocidade orbital média da Terra
    R_J = 5.2 * R_T
    G = 6.67430e-11
    M_sun = 1.989e30
    V_J = np.sqrt(G * M_sun / R_J)  # Velocidade orbital média de Júpiter

    # Tempos de simulação
    ANO_Jupiter = 11.86 * 365.25 * 24 * 60 * 60

    # Simulação sem Júpiter
    t_sem_jupiter, RK4_terra_sem_jupiter, _ = Simular(ANO_Jupiter, ANO_Jupiter * 10**-4, 8, R_T, V_T, 0, 0, M_jupiter=0)

    # Questão (c) - Terra e Júpiter com interação normal
    t_com_jupiter, RK4_terra_com_jupiter, RK4_jupiter_com_jupiter = Simular(ANO_Jupiter, ANO_Jupiter * 10**-4, 8, R_T, V_T, R_J, V_J, M_jupiter=1.898e27)
    desvio_maximo_c = calcular_desvio_maximo(RK4_terra_com_jupiter, RK4_terra_sem_jupiter)
    plotar_orbitas(RK4_terra_sem_jupiter, RK4_terra_com_jupiter, "Questão C: Terra e Júpiter com Interação Normal", desvio_maximo_c)

    # Questão (d) - Massa de Júpiter 100x maior
    t_d1, RK4_terra_d1, RK4_jupiter_d1 = Simular(ANO_Jupiter, ANO_Jupiter * 10**-4, 8, R_T, V_T, R_J, V_J, M_jupiter=100 * 1.898e27)
    desvio_maximo_d1 = calcular_desvio_maximo(RK4_terra_d1, RK4_terra_sem_jupiter)
    plotar_orbitas(RK4_terra_sem_jupiter, RK4_terra_d1, "Questão D: Júpiter com Massa 100x Maior", desvio_maximo_d1)

    # Questão (d) - Massa de Júpiter 1000x maior
    t_d2, RK4_terra_d2, RK4_jupiter_d2 = Simular(ANO_Jupiter, ANO_Jupiter * 10**-4, 8, R_T, V_T, R_J, V_J, M_jupiter=1000 * 1.898e27)
    desvio_maximo_d2 = calcular_desvio_maximo(RK4_terra_d2, RK4_terra_sem_jupiter)
    plotar_orbitas(RK4_terra_sem_jupiter, RK4_terra_d2, "Questão D: Júpiter com Massa 1000x Maior", desvio_maximo_d2)

def main():
    Plotar_resultados_cd()

if __name__ == '__main__':
    main()
