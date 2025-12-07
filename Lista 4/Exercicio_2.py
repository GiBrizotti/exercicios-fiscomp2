import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

#------------------Classe orientada para resolver qualquer integral pelo Método de Monte Carlo---------------------
class IntegracaoMonteCarlo:
  def __init__(self, f, a, b, N_points):
    self.f = f
    self.a = a
    self.b = b
    self.N_points = N_points

  def integral_montecarlo(self):
    x = np.random.uniform(self.a, self.b, self.N_points)
    y = self.f(x)
    return np.mean(y) * (self.b - self.a)

  def integral_numpy(self):
    return quad(self.f, self.a, self.b)[0]

#------------------Classe orientada para calcular o volume de um elipsoide pelo Método de Monte Carlo---------------------
class Elipsoide:
  def __init__(self, a, b, c, N_points):
    self.a = a
    self.b = b
    self.c = c
    self.N_points = N_points

  def dentro_elipsoide(self, x, y, z):
    return (x**2 / self.a**2) + (y**2 / self.b**2) + (z**2 / self.c**2) <= 1

  def volume_teorico(self):
    return (4/3) * np.pi * self.a * self.b * self.c

  def volume_elipsoide(self):
    x = np.random.uniform(-self.a, self.a, self.N_points)
    y = np.random.uniform(-self.b, self.b, self.N_points)
    z = np.random.uniform(-self.c, self.c, self.N_points)

    dentro = self.dentro_elipsoide(x, y, z)

    volume_total = (2 * self.a) * (2 * self.b) * (2 * self.c)
    return np.mean(dentro) * volume_total

#--------------------------------------------------Função Principal-----------------------------------------------------
def main():
  N_points = 10**8

  # Integrais a serem calculadas e seus intervalos:
  a,b,c,d = lambda x: x, lambda x: np.exp(-x), lambda x: np.sin(x), lambda x: x**2 + x**3
  intervalo_a, intervalo_b, intervalo_c, intervalo_d = [0,1],[0,1],[0,np.pi],[0,1]
  #Parâmetros do elipsoide
  a_elip, b_elip, c_elip = 1, 2, 3

  QuestãoA = IntegracaoMonteCarlo(a, intervalo_a[0], intervalo_a[1], N_points)
  QuestãoB = IntegracaoMonteCarlo(b, intervalo_b[0], intervalo_b[1], N_points)
  QuestãoC = IntegracaoMonteCarlo(c, intervalo_c[0], intervalo_c[1], N_points)
  QuestãoD = IntegracaoMonteCarlo(d, intervalo_d[0], intervalo_d[1], N_points)
  QuestãoE = Elipsoide(a_elip, b_elip, c_elip, N_points)

  print("Questão A:\n O resultado pelo método de MonteCarlo é: ", QuestãoA.integral_montecarlo(), "\n O resultado pelo numpy quad é: ", QuestãoA.integral_numpy(),'\n')
  print("Questão B:\n O resultado pelo método de MonteCarlo é: ", QuestãoB.integral_montecarlo(), "\n O resultado pelo numpy quad é: ", QuestãoB.integral_numpy(),'\n')
  print("Questão C:\n O resultado pelo método de MonteCarlo é: ", QuestãoC.integral_montecarlo(), "\n O resultado pelo numpy quad é: ", QuestãoC.integral_numpy(),'\n')
  print("Questão D:\n O resultado pelo método de MonteCarlo é: ", QuestãoD.integral_montecarlo(), "\n O resultado pelo numpy quad é: ", QuestãoD.integral_numpy(),'\n')
  print("Questão E:\n O volume do elipsoide pelo método de MonteCarlo é: ", QuestãoE.volume_elipsoide(),"\n O resultado teórico é: ", QuestãoE.volume_teorico())

if __name__ == "__main__":
  main()