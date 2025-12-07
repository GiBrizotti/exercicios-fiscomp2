import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def parametros(intervalo, subdivisoes):
    # Coordenadas
    x = np.linspace(intervalo[0, 0], intervalo[0, 1], subdivisoes[0]) #Lembrete: Não usar essa lógica na prova. Ficou mto ruim
    y = np.linspace(intervalo[1, 0], intervalo[1, 1], subdivisoes[1])
    X, Y = np.meshgrid(x, y)

    # Tamanho da mesh
    Dx = (intervalo[0, 1] - intervalo[0, 0]) / subdivisoes[0]
    Dy = (intervalo[1, 1] - intervalo[1, 0]) / subdivisoes[1]

    return X, Y, Dx, Dy

def deriva_funcao(funcao, X, Y, Dx, eixo):
    if eixo == 'x':
        derivada = (funcao(X + Dx, Y) - funcao(X, Y)) / Dx
    elif eixo == 'y':
        derivada = (funcao(X, Y + Dx) - funcao(X, Y)) / Dx
    else:
        raise ValueError("Eixo deve ser 'x' ou 'y'")

    return derivada

def simular(X, Y, Z, titulo):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='gist_rainbow')
    ax.set_title(titulo)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    ax.view_init(azim=(180+45))
    plt.show()

def main():
    # Funções fornecidas no exercício
    questoes = {
        "(a) f(x, y) = x^2 + y^2": lambda x, y: x**2 + y**2,
        "(b) f(x, y) = sin(x) + cos(y)": lambda x, y: np.sin(x) + np.cos(y),
        "(c) f(x, y) = x^2 - y^2": lambda x, y: x**2 - y**2,
        "(d) f(x, y) = exp(-x^2 - y^2)": lambda x, y: np.exp(-x**2 - y**2),
        "(e) f(x, y) = x^2 + y^3 - 3xy": lambda x, y: x**2 + y**3 - 3*x*y
    }

    # Parâmetros do domínio
    intervalo = np.array([[-5, 5], [-5, 5]])
    subdivisoes = np.array([100, 100])

    X, Y, Dx, Dy = parametros(intervalo, subdivisoes)

    for titulo, funcao in questoes.items():
        Z = funcao(X, Y)

        # Gráfico da função original
        simular(X, Y, Z, f"Superfície: {titulo}")

        # Derivada numérica em relação a x
        derivada_x = deriva_funcao(funcao, X, Y, Dx, eixo='x')
        simular(X, Y, derivada_x, f"Derivada em x: {titulo}")

if __name__ == "__main__":
    main()