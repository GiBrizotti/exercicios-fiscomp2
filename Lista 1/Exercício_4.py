#-----Exercício 4: Função Arcsen:-----

import math
import numpy as np
import matplotlib.pyplot as plt


def minha_arcsen(x: float, N_max:int = 20) -> float:
  Soma = 0
  for n in range(N_max+1):
    Soma += ( math.factorial(2*n) / (4**n * (math.factorial(n))**2 * (2*n+1) ) ) * x**(2*n + 1)
  return Soma


def Grafico_de_funcao(intervalo: list, n_de_pontos: int) -> None:
  minha_funcao =  lambda x_1: minha_arcsen(x_1)
  funcao_real = lambda x_2: math.asin(x_2)

  #Cria uma lista ingualmente espaçada com o tamanho do numero de pontos, do ponto A até o Ponto B, para ser usada como Eixo X:
  xgraf = np.linspace(intervalo[0],intervalo[1],n_de_pontos)

  #Mapeia a função no Eixo X:
  lista_minha_funcao = list(map(minha_funcao,xgraf))
  lista_funcao_real = list(map(funcao_real,xgraf))

  plt.plot(xgraf, lista_minha_funcao, label='Minha Arcsen', color='red', linewidth = 3 )
  plt.plot(xgraf, lista_funcao_real,  label='Arcsen Real', color='black')
  plt.title("Comparação entre Minha Arcsen e Arcsen Real")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.legend(["Minha Arcsen", "Arcsen Real"])
  plt.grid(True)
  plt.show()


def main():
    Grafico_de_funcao([-1,1], 1000)

if __name__ == "__main__":
    main()