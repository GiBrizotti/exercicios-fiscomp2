#Exercício 1 - Compração do Método de Euler com o Método de Picard


import math
import numpy as np
import matplotlib.pyplot as plt

def euler(y, t, dt, ndim):
  return y+g(y,t,ndim)*dt

def picard(y, t, dt, ndim):
  y1 = y+g(y,t,ndim)*dt
  t1 = t+dt
  return y + (g(y,t,ndim)+ g(y1,t1,ndim))*dt/2

def g(y, t, ndim):
  massa, k = 1.0, 1.0
  g = np.zeros(ndim)
  g[0] = y[1]
  g[1] = -k/massa*y[0]
  return g

def Simulaprograma(tmax, Dt, ndim):
  Nt = int(tmax/Dt)

  t = [0.0]
  y_euler, y_picard = [np.array([2.0,0.0])], [np.array([2.0,0.0])]

  for i in range(Nt-1):
    t.append(t[i]+Dt)
    y_euler.append(euler(y_euler[i], t[i], Dt, ndim))
    y_picard.append(picard(y_picard[i], t[i], Dt, ndim))

  XX_euler = [y_euler[i][0] for i in range(Nt)]
  YY_euler = [y_euler[i][1] for i in range(Nt)]

  XX_picard = [y_picard[i][0] for i in range(Nt)]
  YY_picard = [y_picard[i][1] for i in range(Nt)]

  return t, XX_euler, YY_euler, XX_picard, YY_picard

def plotar_posicao(t, X, Y, dt, metodo, ax, plot_velocidade=True):
    ax.plot(t, X, label=f"Posição (dt = {dt})", color= 'red')
    if plot_velocidade:
        ax.plot(t, Y, label=f"Velocidade (dt = {dt})", linestyle='--', color = 'blue')
    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Posição/Velocidade")
    ax.set_title(f"Método de {metodo}")
    ax.grid(True)
    ax.legend()


def main():
  tmax = 50.0
  Dt = [0.1, 0.01, 0.001]
  ndim = 2

  # Cria subplots para organizar cada combinação em uma grade
  fig, axes = plt.subplots(len(Dt), 2, figsize=(12, 8))  # Ajuste o tamanho da figura se necessário
  fig.suptitle("Oscilações para Diferentes Passos", fontsize=16)

  for i, dt in enumerate(Dt):
      t, XX_euler, YY_euler, XX_picard, YY_picard = Simulaprograma(tmax, dt, ndim)

      ax = axes[i, 0]
      plotar_posicao(t, XX_euler, YY_euler, dt, "Euler", ax)

      ax = axes[i, 1]
      plotar_posicao(t, XX_picard, YY_picard, dt, "Picard", ax)

  plt.tight_layout()
  plt.show()




if __name__ == "__main__":
  main()