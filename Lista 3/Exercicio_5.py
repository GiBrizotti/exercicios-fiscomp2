#Exercício 5 - Soluções de EDOs oscilatórias

import numpy as np
import matplotlib.pyplot as plt

class RungeKuttaExercicios:
    def __init__(self, h, x_end):
        self.h = h
        self.x_end = x_end

    def g(self, y, t, questao):
        # Compactar os cálculos das derivadas para cada questão
        if questao == 'A':
            g = np.zeros(2)  # [y, dy]
            g[0] = y[1]  # y' = dy
            g[1] = np.sin(2 * t) - 5 * y[1] - 6 * y[0]  # y'
            return g

        elif questao == 'B':
            g = np.zeros(3)  # [y, dy, d2y]
            g[0] = y[1]  # y' = dy
            g[1] = y[2]  # y'' = d2y
            g[2] = np.cos(t) - 4 * y[1] + 2 * y[0]  # y''' 
            return g

        elif questao == 'C':
            g = np.zeros(4)  # [y, dy, d2y, d3y]
            g[0] = y[1]  # y' = dy
            g[1] = y[2]  # y'' = d2y
            g[2] = y[3]  # y''' = d3y
            g[3] = (y[1] - 3 * y[0]) / (t + 1)  # y'''' 
            return g

        elif questao == 'D':
            g = np.zeros(5)  # [y, dy, d2y, d3y, d4y]
            g[0] = y[1]  # y' = dy
            g[1] = y[2]  # y'' = d2y
            g[2] = y[3]  # y''' = d3y
            g[3] = y[4]  # y'''' = d4y
            g[4] = np.sin(3 * t) - 2 * y[2] - y[1]  # y''''' 
            return g

        elif questao == 'E':
            g = np.zeros(3)  # [y, dy, d2y]
            g[0] = y[1]  # y' = dy
            g[1] = y[2]  # y'' = d2y
            g[2] = 4 * y[0] + np.cos(4 * t)  # y''' 
            return g

    def rk4_step(self, y, t, dt, questao):
        # Passo do método de Runge-Kutta de 4ª ordem
        c1 = dt * self.g(y, t, questao)
        c2 = dt * self.g(y + c1 / 2, t + dt / 2, questao)
        c3 = dt * self.g(y + c2 / 2, t + dt / 2, questao)
        c4 = dt * self.g(y + c3, t + dt, questao)
        return y + (c1 + 2 * c2 + 2 * c3 + c4) / 6

    def solve(self, x0, y0, questao):
        t = x0
        y = np.array(y0)  # Vetor inicial [y, y', y'', etc.]
        results_x = [t]
        results_y = [y[0]]

        while t < self.x_end:
            y = self.rk4_step(y, t, self.h, questao)
            t += self.h
            results_x.append(t)
            results_y.append(y[0])

        return results_x, results_y

    def Questão_A(self):
        x0, y0, dy0 = 0, 0, 1  # Valores iniciais para Questão A
        return self.solve(x0, [y0, dy0], 'A')

    def Questão_B(self):
        x0, y0, dy0, d2y0 = -1, 1, -1, 0  # Valores iniciais para Questão B
        return self.solve(x0, [y0, dy0, d2y0], 'B')

    def Questão_C(self):
        x0, y0, dy0, d2y0, d3y0 = 2, 2, 0, 0, 1  # Valores iniciais para Questão C
        return self.solve(x0, [y0, dy0, d2y0, d3y0], 'C')

    def Questão_D(self):
        x0, y0, dy0, d2y0, d3y0, d4y0 = 0, 1, 0, 1, -1, 2  # Valores iniciais para Questão D
        return self.solve(x0, [y0, dy0, d2y0, d3y0, d4y0], 'D')

    def Questão_E(self):
        x0, y0, dy0, d2y0 = -2, 0, 2, 0  # Valores iniciais para Questão E
        return self.solve(x0, [y0, dy0, d2y0], 'E')

    def plot_solutions(self, results):
        for questao, (x_vals, y_vals) in results.items():
            plt.figure(figsize=(10, 6))
            plt.plot(x_vals, y_vals, label=f'Solução numérica para Questão {questao}')
            plt.xlabel('x')
            plt.ylabel('y(x)')
            plt.title(f'Solução da Questão {questao}')
            plt.grid()
            plt.legend()
            plt.show()

def main():
    # Parâmetros do problema
    h = 0.01  # Passo
    x_end = 5  # Intervalo de integração (conforme pedido no exercício)

    # Criar a instância da classe
    edo_solver = RungeKuttaExercicios(h, x_end)

    # Resolver cada questão
    results = {
        'A': edo_solver.Questão_A(),
        'B': edo_solver.Questão_B(),
        'C': edo_solver.Questão_C(),
        'D': edo_solver.Questão_D(),
        'E': edo_solver.Questão_E(),
    }

    # Plotar as soluções
    edo_solver.plot_solutions(results)

if __name__ == "__main__":
    main()

