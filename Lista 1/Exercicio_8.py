#Exercício 8 - Demonstração Numérica do Teorema de Bertrand.

import numpy as np
import matplotlib.pyplot as plt

class Orbita:
    def __init__(self, alpha, k=1, m=1, delta_t=0.0001, t_max=20):
        self.alpha = alpha
        self.k = k
        self.m = m
        self.delta_t = delta_t
        self.t_max = t_max

        # Posição e velocidade iniciais
        self.posicao = np.array([1.0, 0.0])   # r0 = [1, 0] (começa no eixo x)
        self.velocidade = np.array([0.5, 1.0])  # v0 = [0.5, 1]

        # Inicializa lista para armazenar posições ao longo da simulação
        self.historico_posicao = []

    def calcular_forca_central(self):
        """Calcula o vetor da força central com base na posição atual."""
        r = np.linalg.norm(self.posicao)  # Distância ao centro
        direcao = -self.posicao / r       # Vetor unitário radial (direção da força)
        intensidade = self.k * (r ** self.alpha)  # Intensidade da força central
        return intensidade * direcao

    def atualizar_posicao_velocidade(self):
        """Atualiza a posição e a velocidade usando o método de Euler."""
        forca = self.calcular_forca_central()
        aceleracao = forca / self.m
        self.velocidade += aceleracao * self.delta_t
        self.posicao += self.velocidade * self.delta_t

    def simular(self):
        """Executa a simulação até o tempo máximo especificado."""
        tempo = 0.0
        while tempo < self.t_max:
            # Armazena posição atual para traçar a trajetória
            self.historico_posicao.append(self.posicao.copy())
            self.atualizar_posicao_velocidade()
            tempo += self.delta_t

    def plotar_trajetoria(self, cor = 'red'):

        """Plota a trajetória da partícula."""
        posicoes = np.array(self.historico_posicao)
        plt.plot(posicoes[:, 0], posicoes[:, 1], label=f"α = {self.alpha}", color = cor)
        plt.xlabel("Posição X")
        plt.ylabel("Posição Y")
        plt.title("Simulação da Trajetória do Projétil")
        plt.legend()
        plt.axis("equal")
        plt.grid(True)


def main():
    # Configurações para diferentes valores de α
    valores_alpha = [2, 1, 0, -1, -2, -3]
    cores = ['yellow', 'red', 'blue', 'green', 'orange', 'purple']
    plt.figure(figsize=(10, 8))

    # Mostrar o gráfico com todas as trajetórias
    for alpha in valores_alpha:
        simulador = Orbita(alpha=alpha)
        simulador.simular()
        simulador.plotar_trajetoria(cores[(alpha)])
        plt.show()

if __name__ == "__main__":
    main()

