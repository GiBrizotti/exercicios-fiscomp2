#-----Exercício 1: Constante de Euler-Mascheroni-----

import numpy as np
import matplotlib.pyplot as plt

def Soma(k_valor: int) -> float:
    """
    Calcula a soma da série harmônica até o valor k_valor.
    """
    Soma = 0
    while k_valor != 0:
        Soma += 1 / k_valor
        k_valor -= 1
    return Soma

def Lista_Gamma(n_lista: list) -> list:
    """
    Calcula a constante de Euler-Mascheroni (γ) para cada valor em n_lista.
    """
    Lista_Gamma = []
    for valor in n_lista:
        temp = Soma(valor) - np.log(valor)
        Lista_Gamma.append(temp)
    return Lista_Gamma

def Lista_Delta(Gamma_calculado: list) -> list:
    """
    Calcula a diferença (Delta) entre o valor teórico da constante de Euler-Mascheroni (γ)
    e os valores aproximados de γ.
    """

    Gamma_teorico = 0.57721566490153286060651209008240
    Lista_Delta = []
    for valor in Gamma_calculado:
        Lista_Delta.append(Gamma_teorico - valor)
    return Lista_Delta

def Geradora_Listas(Gamma: list, Delta: list, n_valor: list) -> None:
    """
    Gera e exibe uma tabela comparando os valores de n, os valores aproximados de γ,
    e a diferença (Delta) entre o valor teórico e o valor calculado.
    """

    # Cria uma lista de listas para a tabela
    Matriz = [[n, g, d] for n, g, d in zip(n_valor, Gamma, Delta)]

    # Cria a figura e o eixo para exibir a tabela
    fig, ax = plt.subplots()

    # Remove as bordas da tabela para uma apresentação mais limpa
    ax.axis('off')

    # Exibe a tabela com as colunas: 'n', 'Gamma', 'Delta'
    Tabela = ax.table(cellText=Matriz, loc='center', colLabels=['n', 'Gamma', 'Delta'])

    # Mostra o gráfico/tabela
    plt.show()

def main():
    # Lista de valores de n para calcular γ
    n_aproximado = [10, 100, 1000, 100000]

    # Gera a tabela comparando valores de γ e Δ para diferentes n
    Geradora_Listas(Lista_Gamma(n_aproximado), Lista_Delta(Lista_Gamma(n_aproximado)), n_aproximado)

if __name__ == "__main__":
    main()