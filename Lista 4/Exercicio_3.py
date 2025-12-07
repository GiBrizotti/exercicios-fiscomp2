import numpy as np
import matplotlib.pyplot as plt

def passo_bebado(N_passos):
    x, y, z = 0, 0, 0
    np.random.seed(42)
    deslocamentos_x, deslocamentos_y, deslocamentos_z = [0], [0], [0]
    for i in range(N_passos):
        deslocamento_x = np.random.choice([-1, 1])
        deslocamento_y = np.random.choice([-1, 1])
        deslocamento_z = np.random.choice([-1, 1])
        x += deslocamento_x
        y += deslocamento_y
        z += deslocamento_z
        deslocamentos_x.append(x)
        deslocamentos_y.append(y)
        deslocamentos_z.append(z)

    return deslocamentos_x, deslocamentos_y, deslocamentos_z

def grafico_3d(deslocamentos_x, deslocamentos_y, deslocamentos_z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(0, 0, 0, color='black', label='Início')
    ax.scatter(deslocamentos_x[-1], deslocamentos_y[-1], deslocamentos_z[-1], color='red', label='Fim')
    ax.plot(deslocamentos_x, deslocamentos_y, deslocamentos_z, color='purple')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Deslocamento do bêbado em 3D')
    plt.legend()
    plt.show()

def grafico_2d(deslocamentos_x, deslocamentos_y, deslocamentos_z):
    plt.figure()
    plt.plot(deslocamentos_x, label='x')
    plt.plot(deslocamentos_y, label='y')
    plt.plot(deslocamentos_z, label='z')
    plt.xlabel('Número de passos')
    plt.ylabel('Deslocamento acumulado')
    plt.title('Deslocamento do bêbado em 2D')
    plt.legend()
    plt.grid()
    plt.show()

def calcular_metricas(deslocamentos_x, deslocamentos_y, deslocamentos_z):
    # Deslocamento lateral máximo
    max_x = np.max(np.abs(deslocamentos_x))
    max_y = np.max(np.abs(deslocamentos_y))
    max_z = np.max(np.abs(deslocamentos_z))

    # Deslocamento lateral médio
    mean_x = np.mean(np.abs(deslocamentos_x))
    mean_y = np.mean(np.abs(deslocamentos_y))
    mean_z = np.mean(np.abs(deslocamentos_z))

    print("Deslocamento lateral máximo:")
    print(f"x: {max_x:.2f}, y: {max_y:.2f}, z: {max_z:.2f}")
    print("\nDeslocamento lateral médio:")
    print(f"x: {mean_x:.2f}, y: {mean_y:.2f}, z: {mean_z:.2f}")

def main():

    N_passos = 1000
    deslocamentos_x, deslocamentos_y, deslocamentos_z = passo_bebado(N_passos)
    grafico_3d(deslocamentos_x, deslocamentos_y, deslocamentos_z)
    grafico_2d(deslocamentos_x, deslocamentos_y, deslocamentos_z)
    calcular_metricas(deslocamentos_x, deslocamentos_y, deslocamentos_z)

if __name__ == "__main__":
    main()
