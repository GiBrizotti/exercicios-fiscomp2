
# Lista 2 - Equações Diferenciais Ordinárias (EDO) e Redução da Ordem
**Disciplina:** Física Computacional 2 (92444-B)  
**Instituição:** UFSCar  
**Professor:** Matheus Paes Lima  
**Período:** 2º semestre de 2024  

Esta lista aborda a resolução numérica de **equações diferenciais ordinárias (EDOs)** utilizando **Python 3**. O objetivo é implementar métodos numéricos, como **Euler** e **Picard**, para resolver problemas clássicos da física e matemática. 

---

## ✅ Conteúdo da Lista

### **Exercício 1 - Comparação dos Métodos de Euler e Picard**
- Resolver o oscilador harmônico com:
  - Método de Euler
  - Método de Picard
- Condições:
  - k = 1, m = 1, posição inicial x = 2.0, velocidade inicial = 0
  - Tempo máximo: 50 unidades
- Comparar soluções para:
  - Δt = 0.1
  - Δt = 0.01
  - Δt = 0.001

---

### **Exercício 2 - Soluções de EDOs Variadas**
- Reescrever problemas no formato:
  \[
  \frac{d\vec{y}}{dx} = \vec{g}(y,x)
  \]
- Resolver com método de Picard (Δx = 0.01) e plotar no intervalo [x₀, x₀ + 5].
- Exemplos:
  - (a) \(7y'' + 4y' - 3y = 0\)
  - (b) \(y''' - 8x^3y = 0\)
  - (c) \((x+2)y^{(4)} + 3y' - 2y = 0\)
  - (d) \(y^{(5)} - 9y' = 0\)

---

### **Exercício 3 - Equação de Bessel**
- Resolver:
  \[
  x^2 y'' + xy' + (x^2 - p^2)y = 0
  \]
- Para p = 0,1,2,3,4 no intervalo \(0 < x < 20\).
- Normalizar soluções:
  \[
  \int_0^{20} [y_p(x)]^2 dx = 1
  \]

---

### **Exercício 4 - Sistema de Van der Pol**
- Resolver sistema:
  \[
  \frac{dx}{dt} = y - f_\mu(x), \quad \frac{dy}{dt} = -x
  \]
- Onde:
  \[
  f_\mu(x) = x^3 - \mu x, \quad \mu \in [-1,+1]
  \]
- Determinar trajetórias (x vs y) para diferentes valores de μ.

---

### **Exercício 5 - Órbita do Cometa Halley**
- Usar método de Picard para calcular:
  - Distância mínima ao Sol (periélio)
  - Tempo para uma órbita completa
  - Gráfico da órbita
  - Velocidade máxima
- Basear-se na lei da gravitação universal.

---

### **Exercício 6 - Catenária**
- Resolver:
  \[
  \frac{d^2 f}{dx^2} = \frac{\omega_0}{T_0} \sqrt{1 + \left(\frac{df}{dx}\right)^2}
  \]
- Calcular altura do segundo poste, inclinação inicial e tensão para diferentes condições.

---

### **Exercício 7 - Teorema de Bertrand**
- Simular órbitas com força central:
  \[
  \vec{F} = -kr^\alpha \hat{r}
  \]
- Para α = 2, 1, 0, -1, -2, -3.
- Usar método de Euler para integração.

---
