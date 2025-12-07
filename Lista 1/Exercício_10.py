#Questão 10 - Dinâmica de Populações com o Método de Euler:

import numpy as np
import matplotlib.pyplot as plt

class PopulacaoSimulator:
    def __init__(self, alfa, beta, delta, gama, x0, y0, delta_t=0.01, t_max=400):

        self.alfa = alfa
        self.beta = beta
        self.delta = delta
        self.gama = gama
        self.x = x0
        self.y = y0
        self.delta_t = delta_t
        self.t_max = t_max

        # Histórico para armazenar populações ao longo do tempo
        self.historico_tempo = []
        self.historico_presas = []
        self.historico_predadores = []

    def atualizar_populacoes(self):
        """Atualiza as populações de presas e predadores usando o método de Euler."""
        dx_dt = self.alfa * self.x - self.beta * self.x * self.y
        dy_dt = self.delta * self.x * self.y - self.gama * self.y

        # Atualização das populações usando o método de Euler
        self.x += dx_dt * self.delta_t
        self.y += dy_dt * self.delta_t

    def simular(self):
        """Executa a simulação da dinâmica populacional."""
        tempo = 0.0
        while tempo < self.t_max:
            # Armazena as populações atuais e o tempo para plotagem
            self.historico_tempo.append(tempo)
            self.historico_presas.append(self.x)
            self.historico_predadores.append(self.y)

            # Atualiza as populações para o próximo passo de tempo
            self.atualizar_populacoes()

            # Incrementa o tempo
            tempo += self.delta_t

    def plotar_populacoes(self):
        """Plota as populações de presas e predadores ao longo do tempo."""
        plt.plot(self.historico_tempo, self.historico_presas, label="Presas (Coelhos)", color = 'blue', linewidth = 2)
        plt.plot(self.historico_tempo, self.historico_predadores, label="Predadores (Raposas)", color = 'red')
        plt.xlabel("Tempo")
        plt.ylabel("População")
        plt.title("Dinâmica Populacional de Presas e Predadores")
        plt.legend()
        plt.grid(True)
        plt.show()

    def resultados_estatisticos(self):
        """Calcula e exibe os valores máximos e mínimos das populações."""
        max_presas = max(self.historico_presas)
        min_presas = min(self.historico_presas)
        max_predadores = max(self.historico_predadores)
        min_predadores = min(self.historico_predadores)

        print(f"População máxima de presas: {max_presas}")
        print(f"População mínima de presas: {min_presas}")
        print(f"População máxima de predadores: {max_predadores}")
        print(f"População mínima de predadores: {min_predadores}")


def main():
    # Parâmetros fornecidos para a simulação
    alfa = 0.1       # taxa de crescimento das presas
    beta = 0.02      # taxa de predação
    delta = 0.01     # taxa de crescimento dos predadores devido ao consumo de presas
    gama = 0.1       # taxa de mortalidade dos predadores
    x0 = 80          # população inicial de presas (coelhos)
    y0 = 30          # população inicial de predadores (raposas)

    # Cria e executa a simulação
    simulador = PopulacaoSimulator(alfa, beta, delta, gama, x0, y0)
    simulador.simular()
    simulador.plotar_populacoes()
    simulador.resultados_estatisticos()

if __name__ == "__main__":
    main()