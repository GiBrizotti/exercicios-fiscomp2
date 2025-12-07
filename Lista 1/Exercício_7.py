#Exercício 7 - Trajetória:

import numpy as np
import matplotlib.pyplot as plt

class Projeteis:
  #Resolvendo tudo de uma vez dentro da classe Projeteis.
    def __init__(self, massa, velocidade_inicial, angulo, resistencia_ar, delta_t=0.01):
        self.m = massa
        self.v0 = velocidade_inicial
        self.angulo = np.radians(angulo)  # Converte ângulo para radianos
        self.gamma = resistencia_ar
        self.delta_t = delta_t
        self.g = 9.81  # Aceleração gravitacional em m/s²

        # Inicializa posição e velocidade
        self.posicao = np.array([0, 0], dtype=float)  # [x, y]
        self.velocidade = np.array([
            self.v0 * np.cos(self.angulo),
            self.v0 * np.sin(self.angulo)
        ], dtype=float)

        # Inicializa variáveis das respostas
        self.tempo_total = 0
        self.altura_maxima = 0
        self.distancia_horizontal = 0
        self.velocidade_final = 0

    def forca_gravitacional(self):
        """Retorna o vetor da força gravitacional."""
        return np.array([0, -self.m * self.g])

    def forca_resistencia(self):
        """Retorna o vetor da força de resistência do ar."""
        return -self.gamma * self.velocidade

    def atualizar_posicao_velocidade(self):
        """
        Atualiza a posição e a velocidade do projétil usando o método de Euler.
        v(t + Δt) = v(t) + a * Δt (velocidade)
        p(t + Δt) = p(t) + v * Δt (posição)
        """

        #Calcula a força total (gravidade + resistência do ar)
        forca_total = self.forca_gravitacional() + self.forca_resistencia()
        #Calcula a aceleração: a = F / m
        aceleracao = forca_total / self.m

        #Atualiza a velocidade com método de Euler: v = v + a * Δt
        self.velocidade += aceleracao * self.delta_t
        #Atualiza a posição com método de Euler: p = p + v * Δt
        self.posicao += self.velocidade * self.delta_t

        #Incrementa o tempo total da simulação  t = t + Δt
        self.tempo_total += self.delta_t

        #Registra a altura máxima alcançada até agora
        self.altura_maxima = max(self.altura_maxima, self.posicao[1])

    def simular(self):
        """Executa a simulação até que o projétil caia."""
        posicoes_x = []
        posicoes_y = []

        while self.posicao[1] >= 0:
            posicoes_x.append(self.posicao[0])
            posicoes_y.append(self.posicao[1])
            #Atualiza posição e velocidade
            self.atualizar_posicao_velocidade()

        self.distancia_horizontal = self.posicao[0]
        self.velocidade_final = np.linalg.norm(self.velocidade) #Modulo da velocidade

        # Plot da trajetória
        plt.plot(posicoes_x, posicoes_y, label="Trajetória do Projétil", color = 'red')
        plt.xlabel("Distância Horizontal (m)")
        plt.ylabel("Altura (m)")
        plt.title("Simulação da Trajetória do Projétil")
        plt.legend()
        plt.grid(True)
        plt.show()

        return {
            "distancia_horizontal": self.distancia_horizontal,
            "velocidade_final": self.velocidade_final,
            "altura_maxima": self.altura_maxima,
            "tempo_total": self.tempo_total
        }

    def resposta_em_texto(self):
        """Exibe os resultados da simulação em formato de texto."""
        print("Distância horizontal percorrida:", self.distancia_horizontal)
        print("Velocidade ao atingir o solo:", self.velocidade_final)
        print("Altura máxima alcançada:", self.altura_maxima)
        print("Tempo total de trajetória:", self.tempo_total)


def main():
    # Simulação do exemplo:
    simulador = Projeteis(
        massa=0.7,
        velocidade_inicial= 100 / 3.6,  # Conversão de km/h para m/s
        angulo= 55,
        resistencia_ar=0.8,
        delta_t=0.01
    )
    #Sem sombra de dúvida a melhor parte em usar classes e objetos:
    simulador.simular()
    simulador.resposta_em_texto()

if __name__ == "__main__":
    main()