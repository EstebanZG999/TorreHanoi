# Análisis Teórico — Torre de Hanoi

## Enunciado del Problema
La Torre de Hanoi consiste en trasladar una pila de \(n\) discos de un poste origen a un poste destino, utilizando un poste auxiliar, respetando dos reglas:
1. Solo se puede mover un disco a la vez.  
2. Nunca colocar un disco más grande sobre uno más pequeño.

El objetivo es minimizar el número de movimientos necesarios.

---

## 1️⃣ Divide and Conquer

### 1.1 Justificación del Enfoque
El problema se descompone naturalmente: para mover \(n\) discos de A a C se deben:
1. Mover los primeros \(n-1\) discos de A a B.  
2. Mover el disco más grande de A a C.  
3. Mover los \(n-1\) discos de B a C.

Esto corresponde exactamente a la estrategia Divide & Conquer.

### 1.2 Recurrencia
Sea \(T(n)\) el número mínimo de movimientos para resolver el problema con \(n\) discos. Entonces:

\[
T(n) = 
\begin{cases}
0, & n = 0,\\[4pt]
2\,T(n-1) + 1, & n > 0.
\end{cases}
\]

### 1.3 Resolución de la Recurrencia

#### Método de Substitución (Expansión)

\[
\begin{aligned}
T(n) &= 2T(n-1) + 1\\
     &= 2\bigl(2T(n-2)+1\bigr) + 1 = 2^2T(n-2) + 2 + 1\\
     &= 2^3T(n-3) + 2^2 + 2 + 1\\
     &\;\;\vdots\\
     &= 2^nT(0) + (2^{n-1} + 2^{n-2} + \dots + 1)\\
     &= 0 + (2^n - 1)\\
     &= 2^n - 1.
\end{aligned}
\]

#### Conclusión
\[
T(n) = 2^n - 1 \quad\Longrightarrow\quad T(n) \in \Theta(2^n).
\]

---

## 2️⃣ Programación Dinámica

### 2.1 Justificación del Enfoque
Aunque la solución clásica de Torre de Hanoi no mejora en complejidad con DP, se puede expresar el mismo problema usando una tabla de estados (bottom‑up) para calcular repetidamente \(T(i)\) a partir de \(T(i-1)\), evitando recálculos innecesarios.

### 2.2 Recurrencia y Tabla

\[
\text{dp}[0] = 0,\quad
\text{dp}[i] = 2\,\text{dp}[i-1] + 1,\quad 1 \le i \le n.
\]

### 2.3 Análisis de Complejidad

| Medida | Complejidad |
|--------|-------------|
| Tiempo | \(\sum_{i=1}^n O(1) = O(n)\) |
| Espacio| \(O(n)\) para el arreglo dp |

#### Conclusión
La versión DP corre en **tiempo lineal** \(O(n)\) y usa **espacio lineal** \(O(n)\).

---

## 3️⃣ Comparación de Tasas de Crecimiento

| Algoritmo | Complejidad Asintótica |
|-----------|------------------------|
| Divide & Conquer | \(\Theta(2^n)\) |
| Programación Dinámica | \(O(n)\) |

Aunque DP es exponencialmente más eficiente, el enfoque DaC refleja la naturaleza recursiva clásica del problema.  

---

## Referencias

1. “Tower of Hanoi,” _Wikipedia_, https://en.wikipedia.org/wiki/Tower_of_Hanoi  
2. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). _Introduction to Algorithms_.
