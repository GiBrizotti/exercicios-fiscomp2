
# Lista 4 - Números Aleatórios na Física Computacional
**Disciplina:** Física Computacional 2 (92444-B)  
**Instituição:** UFSCar  
**Professor:** Matheus Paes Lima  
**Período:** 2º semestre de 2024  

Esta lista explora o uso de **números aleatórios** e **métodos de Monte Carlo** em simulações físicas. Todos os exercícios devem ser implementados em **Python 3**, preferencialmente no **Google Colab**.

---

## ✅ Conteúdo da Lista

### **Exercício 1 - Testando Geradores de Números Aleatórios**
- Implementar método congruencial linear para gerar números uniformes (0 a 1).
- Comparar com `numpy.random.uniform`.
- Gerar gráficos:
  - Valor médio dos números
  - Desvio padrão médio
- Parâmetros: `a = 1664525`, `c = 1013904223`, `m = 2^32`, `seed = 42`.

---

### **Exercício 2 - Integração de Monte Carlo**
- Calcular integrais usando Monte Carlo:
  - \(\int_0^1 x dx\)
  - \(\int_0^1 e^{-x} dx\)
  - \(\int_0^\pi \sin(x) dx\)
  - \(\int_0^1 (x^2 + x^3) dx\)
  - Volume do elipsoide \(x^2/a^2 + y^2/b^2 + z^2/c^2 \leq 1\) (a=1, b=2, c=3)
- Comparar com métodos analíticos ou `scipy.integrate.quad`.

---

### **Exercício 3 - O Passo do Bêbado**
- Simular caminhada aleatória em 3D (1000 passos).
- Gráficos dos deslocamentos em x, y, z.
- Calcular deslocamento máximo e médio.

---

### **Exercício 4 - Simulação de Monte Carlo do Modelo de Ising 2D**
- Implementar modelo de Ising com algoritmo de Metropolis.
- Rede 10x10, condições periódicas.
- Parâmetros: `Nsteps = 100000`, `J = 1`, `μ = 1`, `B = 0.1`.
- Gráficos: energia, magnetização e calor específico vs temperatura (T = 1.6 a 4).
- Determinar temperatura crítica.

---

