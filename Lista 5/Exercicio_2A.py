import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numba import jit

def parametros(Lx, Ly, Nx, Ny):
    # Coordenadas
    x = np.linspace(-Lx/2, Lx/2, Nx)
    y = np.linspace(-Ly/2, Ly/2, Ny)
    X, Y = np.meshgrid(x, y)

    # Tamanho da mesh
    Dx = Lx / Nx
    Dy = Ly / Ny

    #Constante
    Dx2 = (Dx**2)
    Dy2 = (Dy**2)
    DT = ((Dx2)*(Dy2))/(2*(Dx2+Dy2))

    return X, Y, Dx, Dy, Dx2, Dy2, DT

def contorno(V, Nx, Ny):
    # Condições de Dirichlet homogêneas em x
    V[0, :] = -1
    V[Nx-1, :] = 1

    # Condições periódicas em y
    V[:, 0] = V[:, Ny-1]

    return V

@jit(nopython=True) #Tmj nathan, o numba salva muito
def relaxacao(V, V_iter, Nx, Ny, Dx, Dy,Dx2, Dy2, DT):
    for j in range(1, Ny):
        for i in range(1, Nx):
            imais, imenos, jmais, jmenos = (i+1)%Nx, (i-1)%Nx, (j+1)%Ny, (j-1)%Ny,
            V_iter[i, j] = DT * ((V[imais, j] + V[imenos, j]) / Dx2 + (V[i, jmais] + V[i, jmenos]) / Dy2)
    return V_iter

def simular(X, Y, Z):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='summer')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    ax.view_init(azim=(180+45))
    plt.show()

def simular2d(X, Y, Z):
    plt.figure(figsize=(5, 4))
    plt.contourf(X, Y, Z, cmap='summer')
    plt.colorbar()
    plt.xlabel('x')
    plt.ylabel('y')

def main():
    # Parâmetros do domínio
    Lx, Ly = 1.0, 1.0
    Nx, Ny = 100, 100
    delta = 1e-6

    V = np.zeros((Ny, Nx))
    V_iter = np.zeros((Ny, Nx))

    X, Y, Dx, Dy, Dx2, Dy2, DT = parametros(Lx, Ly, Nx, Ny)

    #Print paramentro
    print("=============================")
    print("Parâmetros do domínio:")
    print("Lx:", Lx)
    print("Ly:", Ly)
    print("Nx:", Nx)
    print("Ny:", Ny)
    print("Delta:", delta )
    print("=============================")

    kmax = 100000
    for iter in range(kmax):
        V_iter = relaxacao(V, V_iter, Nx, Ny, Dx, Dy, Dx2, Dy2, DT)
        V_iter = contorno(V_iter, Nx, Ny)  # Aplicar condições de contorno

        #Convergência
        deps = np.max(np.abs(V - V_iter))
        if deps < delta:
            print("=============================")
            print(f"Convergiu em {iter} iterações.")
            break
        if(iter%1000==0):
            print("Número de iterações:", iter, " - Erro Máximo:", deps)
        V = V_iter.copy()

    # Visualizar a solução
    simular(X, Y, V)
    simular2d(X, Y, V)

if __name__ == "__main__":
    main()