import numpy as np
import matplotlib.pyplot as plt
from numba import jit

def parametros_polares(rmin, rmax, Nr, Ntheta):
    dr = (rmax - rmin) / (Nr - 1)
    dtheta = 2 * np.pi / (Ntheta - 1)

    r = np.linspace(rmin, rmax, Nr)
    theta = np.linspace(0, 2 * np.pi, Ntheta)

    R, Theta = np.meshgrid(r, theta)  # Se trocar isso aqui o código quebra

    dr2 = dr**2
    dtheta2 = dtheta**2


    return r, R, Theta, dr, dtheta, dr2, dtheta2

def contorno(V):
    V[:, 0] = 1  # rmin
    V[:, -1] = 5  # rmax
    return V

@jit(nopython=True)
def relaxacao_polar(V,r, Nr, Ntheta, dr, dtheta, dr2, dtheta2):
    V_iter = V.copy()
    for i in range(0, Ntheta):
        for j in range(1, Nr):
            jmais, jmenos = (j + 1), (j - 1)
            imais, imenos = (i + 1) % Ntheta, (i - 1) % Ntheta

            dfdr = (V_iter[i, jmais] - V_iter[i, jmenos]) / (2 * r[j] * dr)
            d2fdr2 = (V_iter[i, jmais] + V_iter[i, jmenos]) / dr2
            dfdtheta = (V_iter[imais, j] + V_iter[imenos, j]) / (r[j]**2 * dtheta2)

            V_iter[i, j] = (dfdr + d2fdr2 + dfdtheta)/ ((2 / dr2) + (2 / (r[j]**2 * dtheta2)))

    return V_iter

def simular(R, Theta, V):
    X, Y = R * np.cos(Theta), R * np.sin(Theta)
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, V, cmap='plasma')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    ax.view_init(azim=(180 + 45))
    plt.show()

def simular2d(R, Theta, V):
    X, Y = R * np.cos(Theta), R * np.sin(Theta)
    plt.figure(figsize=(6, 5))
    plt.contourf(X, Y, V, cmap='plasma')
    plt.colorbar()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solução da Equação de Laplace em Coordenadas Polares')
    plt.show()

def main():
    rmin, rmax = 1, 5
    Nr, Ntheta = 100, 100
    delta = 1e-4

    r, R, Theta, dr, dtheta, dr2, dtheta2 = parametros_polares(rmin, rmax, Nr, Ntheta)
    V = np.zeros((Nr, Ntheta))
    V= contorno(V)

    print("=============================")
    print("Parâmetros do domínio:")
    print("rmax:", rmax)
    print("rmin:", rmin)
    print("Nr:", Nr)
    print("Ntheta:", Ntheta)
    print("=============================")

    kmax = 100000
    for iter in range(kmax):
        V_iter = relaxacao_polar(V, r, Nr, Ntheta, dr, dtheta, dr2, dtheta2)
        V_iter = contorno(V_iter)

        # Convergência
        erro = np.max(np.abs(V - V_iter))
        if erro < delta:
            print("=============================")
            print(f"Convergiu em {iter} iterações.")
            break
        if iter % 10000 == 0:
            print("Número de iterações:", iter, " - Erro Máximo:", erro)

        V = V_iter.copy()

    simular(R, Theta, V)
    simular2d(R, Theta, V)

if __name__ == "__main__":
    main()
