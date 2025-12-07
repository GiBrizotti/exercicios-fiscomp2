#Questão 9 - Força Restauradora

import numpy as np
import matplotlib.pyplot as plt

class Oscilador:
    def __init__(self, alpha, k=1, massa=1, delta_t=0.001, t_max=100, x0=1.0):
        self.alpha = alpha
        self.k = k
        self.m = massa
        self.delta_t = delta_t
        self.t_max = t_max
        self.x0 = x0

        # Estado inicial
        self.x = x0  # posição inicial
        self.v = 0   # velocidade inicial
        self.tempo = 0

        # Histórico de tempo e posição para análise
        self.historico_tempo = []
        self.historico_posicao = []

    def calcular_forca(self):
        """Calcula a força restauradora em função de x."""
        return -self.k * (self.x ** self.alpha)

    def atualizar_estado(self):
        """Atualiza a velocidade e a posição usando o método de Euler-Cromer."""
        aceleracao = self.calcular_forca() / self.m
        self.v += aceleracao * self.delta_t
        self.x += self.v * self.delta_t
        self.tempo += self.delta_t

        # Armazena o tempo e a posição
        self.historico_tempo.append(self.tempo)
        self.historico_posicao.append(self.x)

    def simular(self):
        """Executa a simulação até o tempo máximo especificado."""
        while self.tempo < self.t_max:
            self.atualizar_estado()

    def plotar_posicao(self, ax, cor='blue'):
        """Plota a posição x(t) ao longo do tempo em um eixo específico."""
        ax.plot(self.historico_tempo, self.historico_posicao, label=f"x0 = {self.x0}", color=cor)
        ax.set_xlabel("Tempo (s)")
        ax.set_ylabel("Posição (m)")
        ax.set_title(f"Oscilador com α = {self.alpha}, x0 = {self.x0}")
        ax.legend()
        ax.grid(True)

    def calcular_frequencia(self):
        """Calcula a frequência da oscilação baseada no tempo entre zeros sucessivos de x(t)."""
        cruzamentos = [i for i in range(1, len(self.historico_posicao)) if self.historico_posicao[i-1] * self.historico_posicao[i] < 0]

        # Calcula o período como o tempo entre cruzamentos consecutivos de zero
        periodos = [self.historico_tempo[cruzamentos[i]] - self.historico_tempo[cruzamentos[i-1]] for i in range(1, len(cruzamentos))]

        if periodos:
            periodo_medio = np.mean(periodos)
            frequencia = 1 / periodo_medio
        else:
            frequencia = None  # Caso não haja cruzamentos suficientes

        return frequencia

# Configuração dos valores de α e amplitudes iniciais
alfa_valores = [1, 3, 5]
amplitudes_iniciais = [1, 2, 3]
cores = ['blue', 'green', 'purple']  # Cores para repetir a cada 3 gráficos

# Cria subplots para organizar cada combinação de α e x0 em uma grade
fig, axes = plt.subplots(len(alfa_valores), len(amplitudes_iniciais), figsize=(15, 12))
fig.suptitle("Oscilações para Diferentes α e Amplitudes Iniciais", fontsize=16)

# Itera sobre cada valor de α e x0, e plota em subplots organizados
for i, alpha in enumerate(alfa_valores):
    for j, x0 in enumerate(amplitudes_iniciais):
        oscilador = Oscilador(alpha=alpha, x0=x0)
        oscilador.simular()
        ax = axes[i, j]
        cor = cores[(i * len(amplitudes_iniciais) + j) % len(cores)]  # Define a cor com base no índice
        oscilador.plotar_posicao(ax, cor=cor)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# Calcula e exibe a frequência para α = 5 e amplitudes entre 1 e 10
amplitudes_para_frequencia = range(1, 11)
frequencias = []
for x0 in amplitudes_para_frequencia:
    oscilador = Oscilador(alpha=5, x0=x0)
    oscilador.simular()
    frequencia = oscilador.calcular_frequencia()
    frequencias.append(frequencia)

# Plotando a dependência da frequência com a amplitude inicial para α = 5
plt.figure()
plt.plot(amplitudes_para_frequencia, frequencias, 'o-', label="α = 5")
plt.xlabel("Amplitude Inicial (m)")
plt.ylabel("Frequência (Hz)")
plt.title("Dependência da Frequência com a Amplitude (α = 5)")
plt.legend()
plt.grid(True)
plt.show()
