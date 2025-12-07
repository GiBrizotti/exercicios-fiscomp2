#-----Exercício 2: Somatórios:-----

import math
import matplotlib.pyplot as plt

class Somatorio:
  def __init__(self, n_aproximado):
    self.valor_n = n_aproximado
    self.SomaA, self.SomaB, self.SomaC, self.SomaD, self.SomaE = 0, 0, 0, 0, 0 #Inicializa os somatórios como zero

  def Questão_A(self) -> float:
    n_Questão_A = self.valor_n
    while n_Questão_A != -1:
      self.SomaA += 1/ (math.factorial(n_Questão_A)) #Calcula o somatório da questão A
      n_Questão_A -= 1
    return self.SomaA

  def Questão_B(self) -> float:
    n_Questão_B = self.valor_n
    while n_Questão_B != -1:
      self.SomaB += ((-1)**(n_Questão_B)) / (2*n_Questão_B + 1) #Calcula o somatório da questão B
      n_Questão_B -= 1
    self.SomaB = 4*self.SomaB
    return self.SomaB

  def Questão_C(self) -> float:
    n_Questão_C = 10
    while n_Questão_C != 0:
      self.SomaC += ((2)**(n_Questão_C) +3*n_Questão_C + 1) #Calcula o somatório da questão C
      n_Questão_C -= 1
    return self.SomaC

  def Questão_D(self) -> float:
    n_Questão_D = self.valor_n
    while n_Questão_D != 0:
      self.SomaD += 1/ (n_Questão_D*(1+ n_Questão_D)) #Calcula o somatório da questão D
      n_Questão_D -= 1
    return self.SomaD

  def Questão_E(self) -> float:
    n_Questão_E = 10
    while n_Questão_E != 0:
      self.SomaE +=  ((2)**(n_Questão_E) - 40*n_Questão_E) #Calcula o somatório da questão E
      n_Questão_E -= 1
    return self.SomaE

def Geradora_Listas(Questao: list, Somatorio: list) -> None:
    # Cria uma lista de listas para a tabela
    Matriz = [[q, s] for q, s in zip(Questao, Somatorio)]

    # Cria a figura e o eixo para exibir a tabela
    fig, ax = plt.subplots()

    # Remove as bordas da tabela 
    ax.axis('off')

    # Exibe a tabela com as colunas: 'Questão', 'Valor de Convergência'
    Tabela = ax.table(cellText=Matriz, loc='center', colLabels=['Questão', 'Valor de Convergência'])

    # Mostra o gráfico/tabela
    plt.show()

def main():
  N_limite = 10000
  Convergencia = Somatorio(N_limite)
  Questoes = ['A', 'B', 'C', 'D', 'E']
  Somatorios = [Somatorio.Questão_A(Convergencia), Somatorio.Questão_B(Convergencia), Somatorio.Questão_C(Convergencia), Somatorio.Questão_D(Convergencia), Somatorio.Questão_E(Convergencia)]
  Geradora_Listas(Questoes, Somatorios)

if __name__ == "__main__":
    main()