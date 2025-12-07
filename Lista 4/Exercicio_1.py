import numpy as np
import matplotlib.pyplot as plt

def congruencial_linear(m, a, c, seed, tamanho):
    X = np.zeros(tamanho)
    X[0] = seed

    for i in range(1, tamanho):
        X[i] = (a * X[i - 1] + c) % m

    return X / m

def aleatorio_numpy(n):
    return np.random.uniform(0, 1, n)

def grafico(m, a, c, seed):
    """Gera gráficos de valor médio e desvio padrão dos números gerados."""
    n_passos = np.arange(10000, 100000 + 1, 10000)
    cl_medias, np_medias = [], []
    cl_desvios, np_desvios = [], []

    for passos in n_passos:
        # Gera números usando os dois métodos
        cl_dados = congruencial_linear(m, a, c, seed, passos)
        np_dados = aleatorio_numpy(passos)

        # Calcula as métricas
        cl_medias.append(np.mean(cl_dados))
        np_medias.append(np.mean(np_dados))
        cl_desvios.append(np.std(cl_dados))
        np_desvios.append(np.std(np_dados))

    # Gráfico do valor médio
    plt.figure()
    plt.plot(n_passos, cl_medias, label='Congruencial Linear', color='red')
    plt.plot(n_passos, np_medias, label='Numpy', color='blue')
    plt.xlabel('Quantidade de números gerados')
    plt.ylabel('Valor médio')
    plt.title('Valor médio dos números gerados')
    plt.legend()
    plt.grid()
    plt.show()

    # Gráfico do desvio padrão
    plt.figure()
    plt.plot(n_passos, cl_desvios, label='Congruencial Linear', color='red')
    plt.plot(n_passos, np_desvios, label='Numpy', color='blue')
    plt.xlabel('Quantidade de números gerados')
    plt.ylabel('Desvio padrão')
    plt.title('Desvio padrão dos números gerados')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    # Parâmetros do método congruencial linear
    np.random.seed(42)
    m, a, c, seed = 2**32, 1664525, 1013904223, 42
    grafico(m, a, c, seed)

if __name__ == "__main__":
    main()
