#Exercício 1 - Comparação dos Métodos Euler Picard RK2 e RK4

import numpy as np
import matplotlib.pyplot as plt

#--------------------------------------------------------------PENDULO-------------------------------------------------
class Pendulo:
    def __init__(self, tmax, ndim, dt, y_inicial, t_inicial):
        self.tmax, self.ndim, self.dt = tmax, ndim, dt
        self.y_inicial = y_inicial
        self.t_inicial = t_inicial

    def g(self, y, t):
        massa, k = 1.0, 1.0
        g = np.zeros(self.ndim)
        g[0] = y[1]
        g[1] = -k / massa * y[0]
        return g

    def euler(self, y, t):
        return y + self.g(y, t) * self.dt

    def picard(self, y, t):
        y1 = y + self.g(y, t) * self.dt
        t1 = t + self.dt
        return y + (self.g(y, t) + self.g(y1, t1)) * self.dt / 2

    def rk2(self, y, t):
        alpha_1, alpha_2, nu_21 = 1 / 3, 2 / 3, 3 / 4
        c1 = self.dt * self.g(y, t)
        c2 = self.dt * self.g(y + c1 * nu_21, t + self.dt * nu_21)
        return y + (alpha_1 * c1 + alpha_2 * c2)

    def rk4(self, y, t):
        c1 = self.dt * self.g(y, t)
        c2 = self.dt * self.g(y + c1 / 2, t + self.dt / 2)
        c3 = self.dt * self.g(y + c2 / 2, t + self.dt / 2)
        c4 = self.dt * self.g(y + c3, t + self.dt)
        return y + (c1 + 2 * c2 + 2 * c3 + c4) / 6

    def Simular(self):
        Nt = int(self.tmax / self.dt)
        t = [self.t_inicial]
        y_euler, y_picard, y_rk2, y_rk4 = [self.y_inicial], [self.y_inicial], [self.y_inicial], [self.y_inicial]

        for i in range(Nt - 1):
            t.append(t[i] + self.dt)
            y_euler.append(self.euler(y_euler[i], t[i]))
            y_picard.append(self.picard(y_picard[i], t[i]))
            y_rk2.append(self.rk2(y_rk2[i], t[i]))
            y_rk4.append(self.rk4(y_rk4[i], t[i]))

        XX_euler = [y_euler[i][0] for i in range(Nt)]
        XX_picard = [y_picard[i][0] for i in range(Nt)]
        XX_rk2 = [y_rk2[i][0] for i in range(Nt)]
        XX_rk4 = [y_rk4[i][0] for i in range(Nt)]

        return t, XX_euler, XX_picard, XX_rk2, XX_rk4

    def Plotar_pendulo(self):
        tempo, EULER_graph, PICARD_graph, RK2_graph, RK4_graph = self.Simular()

        cores = ['red', 'orange', 'blue', 'purple']
        plt.plot(tempo, EULER_graph, label='Euler', color=cores[0])
        plt.plot(tempo, PICARD_graph, label='Picard', color=cores[1], linestyle='--')
        plt.plot(tempo, RK2_graph, label='RK2', color=cores[2], linestyle='dotted')
        plt.plot(tempo, RK4_graph, label='RK4', color=cores[3], linestyle='-.')
        plt.title('PÊNDULO')
        plt.ylabel('Posição')
        plt.xlabel('Tempo')
        plt.legend()
        plt.show()

#--------------------------------------------------------------BESSEL-------------------------------------------------
class BESSELzero:
    def __init__(self, tmax, ndim, dt, y_inicial, t_inicial):
        self.tmax, self.ndim, self.dt = tmax, ndim, dt
        self.y_inicial = y_inicial
        self.t_inicial = t_inicial

    def g(self, y, t):
        g = np.zeros(self.ndim)
        g[0] = y[1]  # dy/dt = y'
        g[1] = -(t**2 - 0**2) * y[0] / t**2 - y[1] / t  # dy'/dt = y''
        return g

    def euler(self, y, t):
        return y + self.g(y, t) * self.dt

    def picard(self, y, t):
        y1 = y + self.g(y, t) * self.dt
        t1 = t + self.dt
        return y + (self.g(y, t) + self.g(y1, t1)) * self.dt / 2

    def rk2(self, y, t):
        alpha_1, alpha_2, nu_21 = 1 / 3, 2 / 3, 3 / 4
        c1 = self.dt * self.g(y, t)
        c2 = self.dt * self.g(y + c1 * nu_21, t + self.dt * nu_21)
        return y + (alpha_1 * c1 + alpha_2 * c2)

    def rk4(self, y, t):
        c1 = self.dt * self.g(y, t)
        c2 = self.dt * self.g(y + c1 / 2, t + self.dt / 2)
        c3 = self.dt * self.g(y + c2 / 2, t + self.dt / 2)
        c4 = self.dt * self.g(y + c3, t + self.dt)
        return y + (c1 + 2 * c2 + 2 * c3 + c4) / 6

    def Simular(self):
        Nt = int(self.tmax / self.dt)
        t = [self.t_inicial]
        y_euler, y_picard, y_rk2, y_rk4 = [self.y_inicial], [self.y_inicial], [self.y_inicial], [self.y_inicial]

        for i in range(Nt - 1):
            t.append(t[i] + self.dt)
            y_euler.append(self.euler(y_euler[i], t[i]))
            y_picard.append(self.picard(y_picard[i], t[i]))
            y_rk2.append(self.rk2(y_rk2[i], t[i]))
            y_rk4.append(self.rk4(y_rk4[i], t[i]))

        XX_euler = [y_euler[i][0] for i in range(Nt)]
        XX_picard = [y_picard[i][0] for i in range(Nt)]
        XX_rk2 = [y_rk2[i][0] for i in range(Nt)]
        XX_rk4 = [y_rk4[i][0] for i in range(Nt)]

        return t, XX_euler, XX_picard, XX_rk2, XX_rk4

    def PlotarBessel(self):
        tempo, EULER_graph, PICARD_graph, RK2_graph, RK4_graph = self.Simular()

        cores = ['red', 'orange', 'blue', 'purple']
        plt.plot(tempo, EULER_graph, label='Euler', color=cores[0])
        plt.plot(tempo, PICARD_graph, label='Picard', color=cores[1], linestyle='--')
        plt.plot(tempo, RK2_graph, label='RK2', color=cores[2], linestyle='dotted')
        plt.plot(tempo, RK4_graph, label='RK4', color=cores[3], linestyle='-.')
        plt.title('BESSEL')
        plt.ylabel('y(x)')
        plt.xlabel('x')
        plt.legend()
        plt.show()


def main():
    pendulo = Pendulo(20, 2, 20 / 200, np.array([2.0, 0.0]), 0.0)
    pendulo.Plotar_pendulo()

    bessel = BESSELzero(20, 2, 20 / 200, np.array([1.0, -0.0001]), 0.0001)
    bessel.PlotarBessel()


if __name__ == "__main__":
    main()
