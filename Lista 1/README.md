
# Lista 1 - Revisão de Física Computacional 2
**Disciplina:** Física Computacional 2 (92444-B)  
**Professor:** Matheus Paes Lima  
**Período:** 2º semestre de 2024  

Esta lista tem como objetivo revisar conceitos fundamentais de programação em Python aplicados à Física Computacional.

---

## ✅ Conteúdo da Lista

### **Exercício 1 - Constante de Euler-Mascheroni**
- Calcular numericamente a constante γ definida como:
  \[
  \gamma = \lim_{n \to \infty} \left( \sum_{k=1}^n \frac{1}{k} - \ln(n) \right)
  \]
- Criar uma tabela com valores para n = 10, 100, 1000, 100000.
- Comparar com o valor real: γ ≈ 0.5772156649.

---

### **Exercício 2 - Somatórios**
- Calcular numericamente:
  - \(\sum_{i=0}^{\infty} \frac{1}{i!}\)
  - \(\sum_{i=0}^{\infty} \frac{(-1)^i}{2i+1}\)
  - \(\sum_{i=1}^{10} (2^i + 3^i + 1)\)
  - \(\sum_{i=1}^{\infty} \frac{1}{i(1+i)}\)
  - \(\sum_{i=1}^{10} (2^i - 40^i)\)

---

### **Exercício 3 - Integral Numérica**
- Resolver numericamente:
  \[
  x + \int_0^x e^{-y^2} dy = 5
  \]
- Usar método dos trapézios e equação recursiva.

---

### **Exercício 4 - Funções e Gráficos**
- Implementar aproximação para \(\arcsin(x)\) via série:
  \[
  \arcsin(x) = \sum_{n=0}^{N_{max}} \frac{(2n)!}{4^n (n!)^2 (2n+1)} x^{2n+1}
  \]
- Comparar com `math.asin(x)` e plotar no intervalo [-1, 1].

---

### **Exercício 5 - Sistemas Lineares (Método Iterativo)**
- Resolver sistemas Ax = B usando método de Gauss-Jacobi.
- Implementar algoritmo iterativo e aplicar aos sistemas fornecidos.

---

### **Exercício 6 - Matrizes**
- Criar matriz A (10x10) com regras específicas para elementos.
- Resolver Ax = B usando `numpy.linalg.solve`.

---

### **Exercício 7 - Trajetória com Resistência do Ar**
- Simular movimento de projétil com resistência do ar usando método de Euler.
- Determinar distância, velocidade final, altura máxima, tempo e gráfico da trajetória.

---

### **Exercício 8 - Teorema de Bertrand**
- Simular órbitas com força central \(\vec{F} = -kr^\alpha \hat{r}\).
- Mostrar gráficos para diferentes valores de α.

---

### **Exercício 9 - Osciladores Harmônicos**
- Simular osciladores com força restauradora \(F(x) = -kx^\alpha\).
- Comparar casos α = 1, 3, 5 e analisar dependência da frequência com amplitude.

---

### **Exercício 10 - Dinâmica Populacional (Lotka-Volterra)**
- Implementar equações de Lotka-Volterra com método de Euler.
- Analisar evolução das populações e condições para extinção.

