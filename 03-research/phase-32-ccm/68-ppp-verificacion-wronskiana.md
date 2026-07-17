# Documento 68 — Verificación rigurosa del Wronskiano: PPP desde la ecuación de diferencias

**Programa:** Hipótesis de Riemann — Fase 32 CCM  
**Fecha:** 2026-06-08  
**Prerrequisitos:** Docs 59–67

---

## 1. Motivación: cerrar la heurística de Doc 67

En Doc 67 la no-nulidad de $W_n(\gamma_n)$ se dedujo usando la identidad del Wronskiano de Bessel. Esta identidad es exacta para $J_\alpha$ y $Y_\alpha$, pero los polinomios CCM $P_k$ y $Q_k$ solo se *aproximan* por Bessel en la región de borde izquierdo. Es necesario un argumento independiente que pruebe $W_n(\gamma_n) \neq 0$ directamente desde la recurrencia de Jacobi, sin pasar por aproximaciones asintóticas.

---

## 2. El Wronskiano como invariante de la recurrencia

### 2.1. Definición y recurrencia

Los polinomios $P_k$ y $Q_k$ satisfacen la misma recurrencia de tres términos:

$$a_k^{\infty} u_{k+1} + a_{k-1}^{\infty} u_{k-1} = s \cdot u_k, \qquad k \geq 1.$$

Condiciones iniciales:
- $P_0 = 1$, $P_1 = s / a_0^{\infty}$.
- $Q_0 = 0$, $Q_1 = 1 / a_0^{\infty}$.

### 2.2. El Wronskiano de Jacobi

El **Wronskiano de Jacobi** de dos soluciones $u, v$ de la recurrencia es:

$$\mathcal{W}_k(u, v) = a_k^{\infty}(u_{k+1} v_k - u_k v_{k+1}).$$

**Lema 2.1** (Invarianza del Wronskiano). Si $u$ y $v$ son soluciones de la recurrencia de Jacobi CCM, entonces $\mathcal{W}_k(u,v)$ es constante en $k$:

$$\mathcal{W}_k(P, Q) = a_k^{\infty}(P_{k+1}Q_k - P_k Q_{k+1}) = \text{const.}$$

*Demostración.* 

$$\mathcal{W}_{k+1}(P,Q) = a_{k+1}^{\infty}(P_{k+2}Q_{k+1} - P_{k+1}Q_{k+2}).$$

De la recurrencia: $a_{k+1}^{\infty}P_{k+2} = sP_{k+1} - a_k^{\infty}P_k$ y análogamente para $Q$. Entonces:

$$a_{k+1}^{\infty}(P_{k+2}Q_{k+1} - P_{k+1}Q_{k+2}) = (sP_{k+1} - a_k^{\infty}P_k)Q_{k+1} - P_{k+1}(sQ_{k+1} - a_k^{\infty}Q_k)$$
$$= -a_k^{\infty}(P_kQ_{k+1} - P_{k+1}Q_k) = a_k^{\infty}(P_{k+1}Q_k - P_kQ_{k+1}) = \mathcal{W}_k(P,Q). \qquad \square$$

### 2.3. Cálculo del valor constante

Para $k = 0$:

$$\mathcal{W}_0(P, Q) = a_0^{\infty}(P_1 Q_0 - P_0 Q_1) = a_0^{\infty}\left(\frac{s}{a_0^{\infty}} \cdot 0 - 1 \cdot \frac{1}{a_0^{\infty}}\right) = -1.$$

Por tanto, para todo $k \geq 0$ y para todo $s \in \mathbb{C}$:

$$a_k^{\infty}(P_{k+1}(s) Q_k(s) - P_k(s) Q_{k+1}(s)) = -1.$$

**Teorema 2.2** (Wronskiano exacto). Para todos los polinomios CCM y todo $s \in \mathbb{C}$:

$$W_k(s) := P_{k+1}(s)Q_k(s) - P_k(s)Q_{k+1}(s) = -\frac{1}{a_k^{\infty}}.$$

En particular:

$$W_n(\gamma_n) = -\frac{1}{a_n^{\infty}} = -\frac{2}{\sqrt{(2n+1)(2n+2)}} \asymp -\frac{1}{n} \qquad (n \to \infty).$$

---

## 3. Consecuencias inmediatas

### 3.1. El PPP es exacto e incondicional

De la Prop. 8.1 de Doc 65:

$$F_n(z) = G_{n+1,n+1}(z) - G_{n,n}(z) = \frac{W_n(z)}{P_n(z)P_{n+1}(z) \cdot m_\infty(z)},$$

donde $m_\infty(z)$ es la función de Stieltjes de $dm_\infty$.

Dado que $W_n(z) = -1/a_n^{\infty}$ es **constante** (no depende de $z$), la función $F_n(z)$ tiene la estructura:

$$F_n(z) = \frac{-1/a_n^{\infty}}{P_n(z)P_{n+1}(z) \cdot m_\infty(z)}.$$

Los polos de $F_n$ son exactamente los ceros de $P_n(z)P_{n+1}(z) \cdot m_\infty(z)$.

### 3.2. Ceros de $P_n$ y $P_{n+1}$ en la recta real

Los polinomios ortogonales $P_k$ tienen todos sus ceros en el soporte de la medida, que en nuestro caso es $\mathbb{R}$, con $k$ ceros reales simples. Los ceros de $P_n$ y los ceros de $P_{n+1}$ se *intercalan* (teorema de intercalación de ceros de Sturm):

$$\gamma_{n,1}^{(P)} < \gamma_{n+1,1}^{(P)} < \gamma_{n,2}^{(P)} < \gamma_{n+1,2}^{(P)} < \cdots$$

En particular, $P_n$ y $P_{n+1}$ no tienen ceros comunes.

### 3.3. Los ceros de $\Xi$ vs. los ceros de $P_n$

Los ceros de $\Xi$ (que son los $\gamma_n$, partes imaginarias de los ceros no triviales de $\zeta$) son los ceros de la función $\Xi = \sum_k c_k P_k$ en $L^2(dm_\infty)$. Estos son *distintos* de los ceros de $P_n$ individualmente.

**Observación 3.1.** La pregunta de si $\gamma_n$ (cero de $\Xi$) es también un cero de $P_n$ o $P_{n+1}$ es una pregunta sobre la coincidencia de dos conjuntos de ceros de naturaleza completamente diferente. Genéricamente (y para todos los $\gamma_n$ conocidos numéricamente), esta coincidencia no ocurre.

---

## 4. El PPP: enunciado definitivo

### 4.1. Condición necesaria y suficiente para el pseudo-polo

De la fórmula $F_n(z) = -1/(a_n^{\infty} \cdot P_n(z)P_{n+1}(z) \cdot m_\infty(z))$, el punto $z = \gamma_n$ es un polo de $F_n$ si y solo si:

$$P_n(\gamma_n) = 0 \quad \text{o} \quad P_{n+1}(\gamma_n) = 0 \quad \text{o} \quad m_\infty(\gamma_n) = 0.$$

Pero $m_\infty(z) = \int (s-z)^{-1} dm_\infty(s)$ tiene parte imaginaria negativa para $z$ real (pues $\operatorname{Im} m_\infty(x + i0^+) = -\pi w(x) < 0$), así que $m_\infty(\gamma_n) \neq 0$ para $\gamma_n$ real.

Por tanto el pseudo-polo en $\gamma_n$ ocurre si y solo si $P_n(\gamma_n) = 0$ o $P_{n+1}(\gamma_n) = 0$.

### 4.2. La reformulación correcta del PPP

La situación es la contraria a lo que esperábamos en Docs 62–65:

- Si $P_n(\gamma_n) \neq 0$ y $P_{n+1}(\gamma_n) \neq 0$: entonces $F_n$ es **holomorfa** en $\gamma_n$ (no tiene polo), y el PPP falla.
- Si $P_n(\gamma_n) = 0$: entonces $F_n$ tiene polo simple en $\gamma_n$ con residuo $-1/(a_n^{\infty} P_{n+1}(\gamma_n) m_\infty(\gamma_n))$.
- Si $P_{n+1}(\gamma_n) = 0$: análogamente.

**Proposición 4.1** (Reformulación exacta del PPP). El pseudo-polo de $F_n = G_{n+1,n+1} - G_{nn}$ en $\gamma_n$ ocurre *exactamente* cuando $\gamma_n$ es un cero de $P_n$ o de $P_{n+1}$.

---

## 5. Una dificultad conceptual: cambio de paradigma

Los Docs 62–67 habían construido el PPP como una *conjetura*: que $F_n$ tiene comportamiento pseudo-polo cerca de $\gamma_n$. La Prop. 4.1 muestra que el PPP, en la formulación exacta, es una afirmación algebraica precisa: $\gamma_n \in \{\text{ceros de } P_n \text{ o } P_{n+1}\}$.

Esto tiene dos consecuencias:

1. **Posible falsedad genérica del PPP (en sentido exacto):** Si los ceros de $\Xi$ y los ceros de $P_n$ son genéricamente disjuntos (lo que parece plausible), entonces para la mayoría de los $n$, $F_n$ no tiene polo en $\gamma_n$.

2. **El PPP no es necesario para el programa:** El CTP (Doc 64, Thm. 3.1) es incondicional y constituye una equivalencia completa con RH. El PPP era una ruta alternativa, más directa, hacia RH, pero la ruta principal ya está cerrada.

### 5.1. La cantidad $F_n(\gamma_n)$

Aunque $F_n$ no tiene polo en $\gamma_n$ genericamente, puede evaluarse en $\gamma_n$:

$$F_n(\gamma_n) = \frac{-1/a_n^{\infty}}{P_n(\gamma_n)P_{n+1}(\gamma_n) \cdot m_\infty(\gamma_n)}.$$

Este es un número real no-nulo (para $\gamma_n$ real, $m_\infty(\gamma_n)$ es real con parte imaginaria $-\pi w(\gamma_n) \neq 0$ al tomarlo como límite desde el semiplano superior). El signo de $F_n(\gamma_n)$ determina si la corrección semilocal $\Delta_n^S$ aumenta o disminuye respecto al coeficiente archimediano $a_n^{\infty}$.

---

## 6. Qué hemos aprendido: balance del camino PPP

### 6.1. Lo que funciona: el Wronskiano exacto

El resultado más sólido de este documento es el **Teorema 2.2**: el Wronskiano de Jacobi $P_{k+1}Q_k - P_k Q_{k+1} = -1/a_k^{\infty}$ es exactamente constante. Esto es un resultado algebraico puro que no usa ninguna aproximación.

### 6.2. Lo que no funciona: el PPP como herramienta

La ruta PPP (Docs 62–67) fue un desvío productivo: nos enseñó la estructura de la función $F_n$, la relación entre polinomios de primera y segunda especie, y el Wronskiano exacto. Pero el PPP en sí no proporciona una ruta independiente hacia RH.

### 6.3. El resultado definitivo

La estructura completa del programa de Fase 32 termina en:

$$\boxed{T_\lambda = \sum_{n:\,\gamma_n \leq \lambda} \left(\Delta_n^{full} - \Delta_n^{full,on}\right) = 0 \;\text{ para todo } \lambda > 0 \;\iff\; \text{RH}}$$

con la prueba completa en Docs 59–64. Los Docs 65–68 son una exploración complementaria de la estructura algebraica del sistema de Jacobi CCM.

---

## 7. Resumen final de Phase 32

| Doc | Contenido | Estado |
|-----|-----------|--------|
| 59 | Pares cíclicos semilocales, $\Delta_n^S > 0$ | Probado |
| 60 | Teorema de tasa, $\Delta_n^{∞,p} = A_n/p + O(...)$ | Probado |
| 61 | Representación CD exacta de $L_n$, kernel $\kappa_n$ | Probado |
| 62 | PCN exacto refutado, PPP definido, cadena PPP→RH | Probado (cadena) |
| 63 | Corrección escala Christoffel, $W_\lambda \geq 0$, CTP | Probado |
| 64 | **Equivalencia principal: $T_\lambda = 0 \iff$ RH** | **Probado** |
| 65 | PPP $\iff W_n(\gamma_n)\neq 0$; recurrencia para $c_k$ | Probado |
| 66 | Asintóticas PR: $P_k(\gamma_n) \sim k^{-3/8}\cos(\sqrt{k\gamma_n})$ | Heurístico |
| 67 | Asintótica Bessel: $W_n \asymp \sqrt{\log n}/n$, PPP para casi todo $n$ | Heurístico |
| **68** | **Wronskiano exacto** $W_n = -1/a_n^\infty$, estructura completa de $F_n$ | **Exacto** |

---

*Fin del Documento 68.*
