#-----Exercício 3: Integral Numérica:-----
import numpy as np


def IntegralTrapézio(intervalo: list, n_de_pontos: int) -> float:
  #Função do Exercício 3:
  funcao_y = lambda y: np.exp(-y**2)
  #Define o tamanho do passo da integral:
  h = (intervalo[1] - intervalo[0]) / n_de_pontos
  #Cria uma lista ingualmente espaçada com o tamanho do numero de pontos, do ponto A até o Ponto B, para ser usada como Eixo X:
  xgraf = np.linspace(intervalo[0],intervalo[1],n_de_pontos)
  #Mapeia a função no Eixo X:
  listafuncao = list(map(funcao_y,xgraf))

  integraltrapezio = 0
  #Cálculo da Integral:
  for i in range(1,n_de_pontos-1,2):
    integraltrapezio += (h/2)*(listafuncao[i-1]+2*listafuncao[i]+listafuncao[i+1])
  return integraltrapezio


def Newton_Raphson(Precisao: float = 10**(-16)):
  chute_inicial =  843.7
  #Função do Exercício 3:
  funcao = lambda x: 5 - IntegralTrapézio([0, x], 100000)
  iteração = 1
  while abs(funcao(chute_inicial)- chute_inicial) >= Precisao:
    chute_inicial = funcao(chute_inicial)
    iteração += 1

  return chute_inicial, Precisao, iteração

def main():
  x, precisão, iterações = Newton_Raphson()
  print("\nO valor de x encontrador é de {}, com {} de precisão. Para isso, foram necessárias {} iterações.\n" .format(x, precisão, iterações))


if __name__ == "__main__":
    main()