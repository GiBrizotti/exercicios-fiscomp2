#Exercício 6 - Matrizes:

import numpy as np

def criar_matriz(n:int):
    #n: dimensão da matriz.

    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i < j:
                A[i, j] = 2 * (i + 1) + 7 * (j + 1) + 2
            elif i == j:
                A[i, j] = (3 * (i + 1))**2
            else:
                A[i, j] = 4 * ((i + 1)**3) + 5 * ((j + 1)**2) + 1
    return A

def criar_vetor_B():
    return np.array([37, 26, -9, -122, -107, -602, -257, -1606, -459, -3326], dtype=float)



def main():
    # Utilização das funções
    n = 10
    A = criar_matriz(n)
    B = criar_vetor_B()
    x = np.linalg.solve(A, B) #Resolve Sistema

    print("Matriz A:")
    print(A)
    print("\nVetor B:")
    print(B)
    print("\nSolução do sistema Ax = B, vetor x:")
    print(x)


if __name__ == "__main__":
    main()