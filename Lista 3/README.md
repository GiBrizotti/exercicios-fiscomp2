
# Lista 3 - Equações Diferenciais Ordinárias (EDO) com Runge-Kutta
**Disciplina:** Física Computacional 2 (92444-B)  
**Instituição:** UFSCar  
**Professor:** Matheus Paes Lima  
**Período:** 2º semestre de 2024  

Esta lista aborda a resolução numérica de **EDOs** utilizando métodos de **Runge-Kutta (RK2 e RK4)**, comparando-os com outros métodos como Euler e Picard. 

---

## ✅ Conteúdo da Lista

### **Exercício 1 - Comparação de Métodos**
- Implementar:
  - Euler
  - Picard
  - Runge-Kutta de 2ª ordem (RK2)
  - Runge-Kutta de 4ª ordem (RK4)
- Comparar soluções para:
  - Oscilador harmônico
  - Equação de Bessel (ordem zero)
- Domínio: [0, 20] com 200 pontos.
- Apresentar gráficos comparativos.

---

### **Exercício 2 - Problema de Três Corpos**
- Simular órbitas usando RK4:
  - (a) Terra-Sol (1 ano terrestre)
  - (b) Júpiter-Sol (1 ano jupiteriano)
  - (c) Terra e Júpiter simultaneamente → comparar órbita da Terra com e sem influência de Júpiter.
  - (d) Repetir com massa de Júpiter 100× e 1000× maior → análise qualitativa do impacto no clima.
- Apresentar gráficos das órbitas e estimar desvios.

---

### **Exercício 3 - Sistema de Lorenz (Caos 3D)**
- Resolver:
  \[
  \frac{dx}{dt} = -\sigma x + \sigma y,\quad
  \frac{dy}{dt} = -xz + rx - y,\quad
  \frac{dz}{dt} = xy - bz
  \]
- Parâmetros: σ = 10, b = 8/3.
- Condições iniciais: (10,10,10) e (15,1,-10).
- Tarefas:
  - (a) Simular até t = 100 com 10.000 passos.
  - (b) Identificar polos atratores para r = 0.7 e r = 10.
  - (c) Analisar comportamento para r = 28.
- Criar gráficos das projeções xy, yz e zx.

---

### **Exercício 4 - Correções Relativísticas na Órbita de Mercúrio**
- Força modificada:
  \[
  \vec{F} = \frac{GM_sM_m}{r^3}\left(1 + \frac{\alpha}{r^2}\right)\vec{r}
  \]
- Simular órbita de Mercúrio por 1 ano terrestre usando RK4 (2000 passos).
- Apresentar:
  - Código
  - Gráfico da trajetória (x vs y)

---

### **Exercício 5 - Soluções de EDOs Oscilatórias**
- Resolver problemas de ordem superior com RK4 (h = 0.01):
  - (a) \(y'' + 5y' + 6y = \sin(2x)\)
  - (b) \(y''' + 4y' - 2y = \cos(x)\)
  - (c) \((x+1)y^{(4)} - y'' + 3y = 0\)
  - (d) \(y^{(5)} + 2y''' + y' = \sin(3x)\)
  - (e) \(y'' - 4y = \cos(4x)\)
- Apresentar gráficos das soluções.

---
