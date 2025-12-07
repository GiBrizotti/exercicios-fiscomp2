
# Lista 5 - Solução Numérica da Equação de Laplace
**Disciplina:** Física Computacional 2 (92444-B)  
**Instituição:** UFSCar  
**Professor:** Matheus Paes Lima  
**Período:** 2º semestre de 2024  

Esta lista aborda a resolução numérica da **Equação de Laplace** em diferentes coordenadas e condições de contorno. Todos os exercícios devem ser implementados em **Python 3**.

---

## ✅ Conteúdo da Lista

### **Exercício 1 - Gráficos de Funções de Duas Variáveis**
- Plotar superfícies para:
  - \(f(x,y) = x^2 + y^2\)
  - \(f(x,y) = \sin(x) + \cos(y)\)
  - \(f(x,y) = x^2 - y^2\)
  - \(f(x,y) = e^{-x^2 - y^2}\)
  - \(f(x,y) = x^2 + y^3 - 3xy\)
- Domínio: x,y ∈ [-5,5], grid 100x100.
- Calcular e plotar derivada parcial em relação a x.

---

### **Exercício 2 - Equação de Laplace 2D**
- Resolver numericamente em domínio retangular (100x100 pontos).
- Casos:
  - (a) Condições periódicas em y e Dirichlet homogêneas em x.
  - (b) Quadrado interno com V=1 e bordas externas V=0.
  - (c) Duas linhas internas com V=1 e bordas externas V=0.

---

### **Exercício 3 - Equação de Laplace em Coordenadas Polares**
- Resolver em região circular entre r_min e r_max.
- Condições:
  - (a) V(r_min,θ)=1, V(r_max,θ)=5
  - (b) V(r_min,θ)=0, V(r_max,θ)=cos(mθ), m=1,2,7
- Discretização: N_r = N_θ = 100.

---
