#Exercício 5 - Solução de Sistemas Lineares com Métodos Iterativos

import numpy as np

class GaussJacobi:
    def __init__(self, A, B, epsilon=1e-6, max_iter=100):
        self.A = A
        self.B = B
        self.epsilon = epsilon
        self.max_iter = max_iter
        self.x_k = np.zeros_like(B, dtype=float)  # Chute inicial x0 = [0, 0, 0,...]

    def solve(self):
        # Obter a matriz diagonal e fora da diagonal
        D = np.diag(self.A)                   # Diagonal principal de A
        Ad_inv = np.diag(1 / D)               # Inversa da diagonal principal
        A_off = self.A - np.diagflat(D)       # Matriz fora da diagonal

        # Iterações de Gauss-Jacobi
        for k in range(self.max_iter):
            x_new = Ad_inv @ (self.B - A_off @ self.x_k)  # (@ É a multiplicação matricial)

            # Verificar critério de parada
            if np.all(np.abs(x_new - self.x_k) < self.epsilon):
                print(f"Convergência atingida em {k+1} iterações.")
                self.x_k = x_new
                return x_new

            self.x_k = x_new  # Atualizar x_k para próxima iteração

        print("Máximo de iterações atingido sem convergência.")
        return self.x_k

# Definindo os sistemas lineares como uma lista de pares (A, B)
sistemas = [
    (np.array([[10, 1, -1], [1, 10, 1], [2, -1, 10]], dtype=float), np.array([10, 12, 11], dtype=float)),
    (np.array([
        [16, 1, 1, 1, 1, 1, 1],
        [1, 18, 1, 1, 1, 1, 1],
        [1, 1, 20, 1, 1, 1, 1],
        [1, 1, 1, 22, 1, 1, 1],
        [1, 1, 1, 1, 24, 1, 1],
        [1, 1, 1, 1, 1, 26, 1],
        [1, 1, 1, 1, 1, 1, 28]
    ], dtype=float), np.array([56, 75, 94, 113, 132, 151, 170], dtype=float)),
    (np.array([
        [31, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 34, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 37, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 40, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 43, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 46, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 49, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 52, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 55, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 58]
    ], dtype=float), np.array([93, 102, 111, 120, 129, 138, 147, 156, 165, 174], dtype=float))
]

# Resolvendo cada sistema com a classe
for i, (A, B) in enumerate(sistemas, start=1):
    solver = GaussJacobi(A, B)
    solution = solver.solve()
    print(f"Solução do sistema ({i}): {solution}\n")

