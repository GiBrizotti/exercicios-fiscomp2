
# Lista 6 - Solução Numérica da Equação de Onda
**Disciplina:** Física Computacional 2 (92444-B)  
**Instituição:** UFSCar  
**Professor:** Matheus Paes Lima  
**Período:** 2º semestre de 2024  

Esta lista aborda a resolução numérica da **Equação de Onda** em uma corda com extremidades fixas. Todos os exercícios devem ser implementados em **Python 3**.

---

## ✅ Condições Gerais
- Comprimento da corda: L = 1 m
- Divisão: 100 partes
- Extremidades fixas
- Passo temporal: Δt = 0.01 s
- Tração: T = 1 N
- Densidade linear: ρ = 1 kg/m
- Tempo máximo: t_max = 6 s
- Velocidade da onda: v = √(T/ρ)

---

## ✅ Conteúdo da Lista

### **Exercício 1 - Solução Estacionária**
- Condições iniciais:
  - y(x,0) = a₀ e^{-(x-x₀)²/σ}, com a₀ = 10⁻³ m, x₀ = 0.5 m, σ = 0.1.
- Corda inicialmente parada.

---

### **Exercício 2 - Perturbação em Movimento**
- Condições iniciais:
  - y(x,0) = a₀ e^{-(x-x₀)²/σ}, com a₀ = 10⁻³ m, x₀ = 0.5 m, σ = 0.1.
- Corda em movimento com velocidade v.

---

### **Exercício 3 - Harmônicos**
- Condições iniciais:
  - y(x,0) = a₀ sin(kx), com a₀ = 10⁻³ m, k = nπ/L, n = 1,2,3.
- Corda inicialmente parada.

---