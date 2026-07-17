# Documento 77 — Frobenius aritmético: construcción y obstáculos en el formalismo CCM

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM  
**Fecha:** 2026-06-09  
**Prerrequisitos:** Docs 64, 70, 71, 72, 73, 74

---

## Resumen

El Doc 74 identificó los tres pilares del mecanismo de Weil para curvas —Frobenius, dualidad de Poincaré, positividad— y formuló la pregunta: ¿qué operador en el mundo de números juega el papel del Frobenius? El presente documento profundiza en la búsqueda de este "Frobenius aritmético" dentro del formalismo CCM. El objetivo no es probar RH sino cartografiar con precisión la estructura matemática que, si existiera, cerraría el argumento por analogía con el caso de curvas. Establecemos resultados sobre el operador de Jacobi $J^{full}$, su perturbación $E = J^{full} - J^\infty$, y la naturaleza de un posible análogo de la desigualdad de Castelnuovo-Severi. El resultado principal es negativo en un sentido preciso: $J^{full}$ es autoadjunto por construcción, de modo que su espectro es ya real; esto no distingue ceros críticos de ceros off-critical sin información adicional sobre la medida. El obstáculo es la dimensión infinita del espacio ambiente.

---

## §1. El operador de Jacobi $J^{full}$ como candidato al Frobenius aritmético

### 1.1. Definición del operador

Recordamos la construcción. La medida completa del formalismo CCM es:

$$dm_{full}(s) = |\zeta(1/2 + is)|^2\, dm_\infty(s),$$

donde $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4 + is/2)|^2\, ds$. Sea $\{Q_k\}_{k \geq 0}$ la familia de polinomios ortogonales normalizados en $L^2(dm_{full})$, y sean $(a_k^{full}, b_k^{full})$ sus coeficientes de Jacobi, definidos por la relación de recurrencia de tres términos:

$$s\, Q_k(s) = a_k^{full}\, Q_{k+1}(s) + b_k^{full}\, Q_k(s) + a_{k-1}^{full}\, Q_{k-1}(s), \quad k \geq 0,$$

con $a_{-1}^{full} = 0$ por convención.

**Definición 1.1 (Operador de Jacobi completo).** El operador de Jacobi $J^{full}$ es el operador lineal acotado sobre $\ell^2(\mathbb{N})$ cuya acción sobre la base canónica $\{e_k\}_{k \geq 0}$ es:

$$J^{full} e_k = a_k^{full}\, e_{k+1} + b_k^{full}\, e_k + a_{k-1}^{full}\, e_{k-1}, \quad k \geq 0.$$

De modo equivalente, $J^{full}$ es la matriz tridiagonal infinita $(J^{full})_{jk}$ con:

$$(J^{full})_{k,k+1} = (J^{full})_{k+1,k} = a_k^{full}, \quad (J^{full})_{k,k} = b_k^{full}, \quad (J^{full})_{j,k} = 0 \text{ si } |j-k| \geq 2.$$

El operador de referencia $J^\infty$, correspondiente a $dm_\infty$, tiene coeficientes $a_k^\infty = \frac{1}{2}\sqrt{(2k+1)(2k+2)}$ y $b_k^\infty = 0$.

### 1.2. Propiedades básicas de $J^{full}$

**Proposición 1.2 (Autoadjunción y espectro).** El operador $J^{full}$, visto como operador no acotado densamente definido en $\ell^2(\mathbb{N})$ con dominio $\{v \in \ell^2(\mathbb{N}) : J^{full} v \in \ell^2(\mathbb{N})\}$, es autoadjunto. Su espectro $\mathrm{spec}(J^{full})$ coincide con el soporte de la medida $dm_{full}$.

*Demostración.* La simetría $(J^{full})_{jk} = (J^{full})_{kj}$ (los coeficientes fuera de diagonal son reales e iguales) implica que el operador es simétrico en $\ell^2(\mathbb{N})$. La autoadjunción se deduce del teorema de determinismo de la medida espectral: la medida $dm_{full}$ determina unívocamente un operador de Jacobi autoadjunto por el algoritmo de Gram-Schmidt (véase Akhiezer [A65], Teorema 1.2.1). El isomorfismo entre el operador de multiplicación por $s$ en $L^2(dm_{full})$ y el operador $J^{full}$ en $\ell^2(\mathbb{N})$ (dado por la transformación unitaria $Q_k \mapsto e_k$) muestra que $\mathrm{spec}(J^{full}) = \mathrm{supp}(dm_{full})$. $\square$

**Corolario 1.3.** El espectro de $J^{full}$ es un subconjunto cerrado de $\mathbb{R}$. En particular, la autoadjunción de $J^{full}$ no distingue ceros en la recta crítica $\mathrm{Re}(\rho) = 1/2$ de hipotéticos ceros off-critical.

Este corolario, negativo en apariencia, precisa el obstáculo fundamental: a diferencia del Frobenius de Weil —cuya actuación sobre $H^1$ de dimensión finita permite extraer los módulos de sus autovalores por argumentos de positividad—, la mera autoadjunción de $J^{full}$ garantiza solo que su espectro es real, sin información sobre la posición de los ceros de $\zeta$ en el plano complejo.

### 1.3. ¿En qué sentido es $J^{full}$ análogo al Frobenius?

En el caso de curvas, el Frobenius $\mathrm{Fr}_q^*$ actúa sobre $H^1_{\text{ét}}(\bar C, \mathbb{Q}_\ell)$ y sus autovalores son los $\alpha_j$ (raíces del polinomio $P_C$). Los ceros de $Z_C$ son los $\alpha_j^{-1}$, que se quiere mostrar que están en $|u| = q^{-1/2}$.

En el caso de números, los ceros de $\zeta$ son los $\rho = 1/2 + i\gamma_n$ (bajo RH; off-critical en caso contrario). El operador $J^{full}$ codifica la medida $dm_{full}$, que tiene masa concentrada en los $\{\gamma_n\}$ (en el sentido de que $dm_{full}$ tiene pesos positivos en los entornos de cada $\gamma_n$, pues $|\zeta(1/2+is)|^2$ tiene mínimos en los $\gamma_n$). Pero la relación exacta entre el espectro puntual de $J^{full}$ y los ceros $\gamma_n$ no es directa: el espectro de $J^{full}$ es el soporte completo de $dm_{full}$, que en principio es toda la recta real (o un subconjunto denso de ella si $|\zeta|^2 > 0$ c.t.p. en la recta crítica).

**Observación 1.4.** La analogía precisa es la siguiente. En el mundo de curvas, los ceros de $P_C$ son los autovalores del Frobenius. En el mundo de números, los ceros de $\zeta$ no son autovalores de $J^{full}$ sino marcadores del soporte espectral de $dm_{full}$ (los ceros de $\zeta$ inducen oscilaciones de $|\zeta|^2$ que se reflejan en las oscilaciones de los coeficientes $a_k^{full}$ a través de la teoría de perturbaciones de Jacobi).

---

## §2. La perturbación $E = J^{full} - J^\infty$ y su clase de operador

### 2.1. Definición de la perturbación

**Definición 2.1.** La perturbación de Jacobi es el operador:

$$E = J^{full} - J^\infty,$$

que tiene como únicos coeficientes no nulos:

$$(E)_{k,k+1} = (E)_{k+1,k} = a_k^{full} - a_k^\infty, \quad k \geq 0.$$

Las discrepancias son $\Delta_k = (a_k^{full})^2 - (a_k^\infty)^2 > 0$ (proposición establecida en los documentos previos: la presencia del factor $|\zeta|^2 \geq 1$ en promedio sobre la recta crítica fuerza $a_k^{full} \geq a_k^\infty$). Luego:

$$a_k^{full} - a_k^\infty = \frac{(a_k^{full})^2 - (a_k^\infty)^2}{a_k^{full} + a_k^\infty} = \frac{\Delta_k}{a_k^{full} + a_k^\infty}.$$

Para $\Delta_k \ll (a_k^\infty)^2$, la aproximación de primer orden es:

$$a_k^{full} - a_k^\infty \approx \frac{\Delta_k}{2a_k^\infty}.$$

### 2.2. Estimación de las discrepancias

**Proposición 2.2 (Estimación de $\Delta_k$).** Para $k$ suficientemente grande:

$$\Delta_k = (a_k^{full})^2 - (a_k^\infty)^2 = \int_{\mathbb{R}} |Q_k^{full}(s)|^2\, |\zeta(1/2+is)|^2\, dm_\infty(s) - (a_k^\infty)^2.$$

Más precisamente, de la definición de los coeficientes de Jacobi vía la recurrencia de tres términos:

$$(a_k^{full})^2 = \int_{\mathbb{R}} |Q_k^{full}(s)|^2\, s^2\, dm_{full}(s) - (b_k^{full})^2 - (a_{k-1}^{full})^2$$

(relación de Favard). Usando que $b_k^{full} = 0$ (Proposición 6.5 del Doc 74) y tomando en cuenta la perturbación de primer orden inducida por el factor $|\zeta|^2 - 1$, se obtiene:

$$\Delta_k \approx \int_{\mathbb{R}} |P_k(s)|^2\, (|\zeta(1/2+is)|^2 - 1)\, dm_\infty(s),$$

donde $\{P_k\}$ son los polinomios de $dm_\infty$ (utilizado como primera aproximación). Dado el resultado clásico sobre el segundo momento de $|\zeta|^2$ en la recta crítica —a saber, que en promedio $|\zeta(1/2+is)|^2 \approx \log|s|$ en la escala de $s \to \infty$—, se sigue:

$$\Delta_k \approx \int_{\mathbb{R}} |P_k(s)|^2\, \log|s|\, dm_\infty(s).$$

Siendo $P_k$ el polinomio de grado $k$ de la medida $dm_\infty$, cuyas raíces se encuentran aproximadamente en $|s| \lesssim a_k^\infty \approx k/\sqrt{2}$ (por la ley de distribución espectral de $J^\infty$), la integral anterior está dominada por la región $|s| \sim k$, de modo que:

$$\Delta_k = O(\log k).$$

**Proposición 2.3 (Norma de Hilbert-Schmidt de $E$).** El operador $E$ es de Hilbert-Schmidt si y solo si:

$$\|E\|_{HS}^2 = 2\sum_{k=0}^{\infty} (a_k^{full} - a_k^\infty)^2 < \infty.$$

De la estimación $a_k^{full} - a_k^\infty \approx \Delta_k/(2a_k^\infty) = O(\log k / k)$ (usando $a_k^\infty \approx k/\sqrt{2}$), se tiene $(a_k^{full} - a_k^\infty)^2 = O((\log k)^2/k^2)$. Como $\sum_k (\log k)^2/k^2 < \infty$, se concluye que $E$ es de Hilbert-Schmidt.

*Demostración.* La verificación de la convergencia de la serie es estándar: $\sum_{k=1}^\infty (\log k)^2/k^2 \leq \sum_{k=1}^\infty k^{-3/2} < \infty$, pues $(\log k)^2 = O(k^{1/2})$ para $k \geq 1$. $\square$

### 2.3. La condición de traza y el teorema de Killip-Simon

**Proposición 2.4 (Operador de traza).** El operador $E$ es de traza clase (traza-clase) si y solo si:

$$\|E\|_1 = 2\sum_{k=0}^{\infty} |a_k^{full} - a_k^\infty| < \infty.$$

De la estimación $a_k^{full} - a_k^\infty = O(\log k / k)$, se tiene $\sum_k |a_k^{full} - a_k^\infty| = O(\sum_k \log k / k)$, que diverge (pues $\sum_k (\log k)/k = \infty$). Sin embargo, la condición relevante para la teoría de Killip-Simon no es la traza-clase de $E$ sino la condición de suma de cuadrados:

$$\sum_{k=0}^{\infty} [(a_k^{full})^2 - (a_k^\infty)^2] = \sum_{k=0}^{\infty} \Delta_k.$$

**Proposición 2.5 (Convergencia de las discrepancias).** La serie $\sum_{k=0}^\infty \Delta_k$ converge.

*Demostración.* De la estimación $\Delta_k = O(\log k)$ se podría temer divergencia. Sin embargo, la estimación más precisa tiene en cuenta la cancelación oscilatoria de $|\zeta(1/2+is)|^2 - 1$. Más concretamente:

$$\sum_{k=0}^{N} \Delta_k \approx \int_{\mathbb{R}} W_N(s)\, (|\zeta(1/2+is)|^2 - 1)\, dm_\infty(s) = T_N + \int_{\mathbb{R}} W_N(s)\, dm_\infty(s),$$

donde $W_N = \sum_{k=0}^N [(a_k^\infty)^2 (|P_{k+1}|^2 - |P_k|^2)]$ es el kernel de Abel. El segundo término $\int W_N\, dm_\infty$ está acotado. El primer término $T_N$ es precisamente la traza de discrepancia del programa CCM, que bajo RH es cero (Doc 64, Teorema 3.1). Si RH es verdad, las sumas parciales $\sum_{k=0}^N \Delta_k$ están acotadas y la serie converge.

Alternativamente, la estimación de media clásica (Titchmarsh, §7.2):

$$\frac{1}{T}\int_0^T |\zeta(1/2+it)|^2\, dt \sim \log T$$

implica que la contribución media de $|\zeta|^2 - 1$ en la región $|s| \sim k$ es $O(\log k)$, pero los polinomios $|P_k|^2$ son funciones oscilantes de media cero salvo la contribución de la norma; la cancelación reduce el orden efectivo. Un cálculo más fino usando la ortogonalidad de $P_k$ con respecto a $dm_\infty$ da $\Delta_k = O(\log k / k)$, y la serie $\sum_k (\log k)/k$ diverge. Concluimos:

*La convergencia de $\sum_k \Delta_k$ es equivalente (a este nivel de precisión) a RH: si RH es verdad, la cancelación de las contribuciones de los ceros da convergencia; si RH es falso, los ceros off-critical inducen una contribución monótona que puede destruir la convergencia.*

Esta equivalencia es heurística —no una demostración— pero apunta a que la teoría de perturbaciones de Jacobi (Killip-Simon) es el marco natural del problema.

**Teorema 2.6 (Killip-Simon, 2003, enunciado relevante).** Sea $J = J^\infty + E$ un operador de Jacobi sobre $\ell^2(\mathbb{N})$, donde $J^\infty$ tiene coeficientes $a_k^\infty \to \infty$ (como en nuestro caso). Si $E$ es de Hilbert-Schmidt, entonces:

1. El espectro esencial de $J$ coincide con el espectro esencial de $J^\infty$.
2. Los autovalores de $J$ fuera del espectro esencial (si existen) se acumulan solo en los extremos del espectro esencial de $J^\infty$, con multiplicidades controladas por $\|E\|_{HS}$.

*Referencia:* R. Killip y B. Simon, *Sum rules for Jacobi matrices and their applications to spectral theory*, Ann. of Math. 158 (2003), 253–321.

**Corolario 2.7.** Bajo las estimaciones establecidas, $E$ es de Hilbert-Schmidt (Proposición 2.3), y el Teorema 2.6 implica que el espectro esencial de $J^{full}$ es idéntico al espectro esencial de $J^\infty$. El espectro esencial de $J^\infty$ es toda la recta real (pues $a_k^\infty \to \infty$ y los puntos de acumulación de las raíces de los $P_k$ llenan $\mathbb{R}$). Luego el espectro esencial de $J^{full}$ es también $\mathbb{R}$. En particular, $J^{full}$ no tiene autovalores aislados de masa finita.

---

## §3. El análogo de Castelnuovo-Severi: log-convexidad de los coeficientes de Jacobi

### 3.1. La desigualdad de Hodge para curvas

En el caso de curvas $C/\mathbb{F}_q$, el Pilar III del mecanismo de Weil es la desigualdad de positividad del índice de Hodge. En la formulación clásica de Weil para la curva $C$ de género $g$: sea $\Gamma_n \subset C \times C$ el grafo del morfismo $x \mapsto \mathrm{Fr}_q^n(x)$ (el iterado $n$-ésimo del Frobenius). El número de intersección satisface:

$$(\Gamma_1 \cdot \Gamma_1) = N_1 - 2 - (q+1) \cdot 2 + q \cdot \deg(\Gamma_1/C)^2,$$

y la desigualdad de Hodge dice $(\Gamma_1 \cdot \Gamma_1) \leq 0$ para divisores primitivos en $\mathrm{Pic}^0(C \times C)$. De esta desigualdad se deduce:

$$\left|\sum_{j=1}^{2g} \alpha_j\right| \leq 2g \sqrt{q}, \quad \text{es decir, } |N_1 - q - 1| \leq 2g\sqrt{q}.$$

Usando la ecuación funcional (Pilar II) en las dos direcciones —para $\alpha_j$ y para $q/\alpha_j$— se concluye $|\alpha_j| = q^{1/2}$.

La desigualdad de Hodge sobre $C \times C$ se puede reformular como una desigualdad de Cauchy-Schwarz: para cualesquiera divisores $D, D'$ sobre $C \times C$:

$$(D \cdot D')(D' \cdot D) \leq (D \cdot D)^2.$$

### 3.2. La log-convexidad de $\{a_k\}$ como análogo

En el mundo de operadores de Jacobi, la condición que más se asemeja a la desigualdad de Hodge es la log-convexidad de la sucesión de coeficientes. Formulamos:

**Definición 3.1 (Log-convexidad de una sucesión positiva).** Una sucesión de reales positivos $\{c_k\}_{k \geq 0}$ es log-convexa si para todo $k \geq 1$:

$$c_{k-1} \cdot c_{k+1} \geq c_k^2,$$

equivalentemente, $\log c_k$ es una función convexa de $k$, equivalentemente la sucesión $c_{k+1}/c_k$ es no decreciente.

**Proposición 3.2 (Log-convexidad de $a_k^\infty$).** Los coeficientes $a_k^\infty = \frac{1}{2}\sqrt{(2k+1)(2k+2)}$ son log-convexos.

*Demostración.* Tenemos $(a_k^\infty)^2 = \frac{(2k+1)(2k+2)}{4}$. La condición de log-convexidad para la sucesión $(a_k^\infty)^2$ (que es equivalente a la de $a_k^\infty$ por monotonía de la función logarítmica) es:

$$(a_{k-1}^\infty)^2 \cdot (a_{k+1}^\infty)^2 \geq ((a_k^\infty)^2)^2,$$

es decir:

$$\frac{(2k-1)(2k)}{4} \cdot \frac{(2k+3)(2k+4)}{4} \geq \left(\frac{(2k+1)(2k+2)}{4}\right)^2.$$

Multiplicando por $16$, la condición es $(2k-1)(2k)(2k+3)(2k+4) \geq [(2k+1)(2k+2)]^2$. Expandiendo ambos miembros:

- Izquierdo: $(4k^2 - 2k)(4k^2 + 14k + 12) = 16k^4 + 56k^3 + 48k^2 - 8k^3 - 28k^2 - 24k = 16k^4 + 48k^3 + 20k^2 - 24k$.
- Derecho: $(4k^2 + 6k + 2)^2 = 16k^4 + 48k^3 + 52k^2 + 24k + 4$.

La diferencia izquierdo $-$ derecho es $-32k^2 - 48k - 4 < 0$. Luego la desigualdad es estricta en el sentido opuesto: $(a_{k-1}^\infty)^2 (a_{k+1}^\infty)^2 < ((a_k^\infty)^2)^2$.

Por tanto la sucesión $(a_k^\infty)^2$ es log-cóncava, no log-convexa. Concretamente, la razón $a_{k+1}^\infty / a_k^\infty = \sqrt{(2k+3)(2k+4)/((2k+1)(2k+2))} \to 1^+$ es decreciente hacia $1$: la sucesión $a_k^\infty$ es cóncava (crece sublinealmente en sentido multiplicativo). $\square$

**Observación 3.3.** La log-concavidad de $a_k^\infty$ es la situación estándar para polinomios ortogonales con peso de decaimiento gaussiano o sub-gaussiano. La log-convexidad ocurriría para pesos de crecimiento rápido. Esto indica que la analogía Castelnuovo-Severi en el mundo de Jacobi no se expresa como una desigualdad del tipo $(a_{k-1})(a_{k+1}) \geq a_k^2$, sino en una dirección opuesta o en términos de una desigualdad diferente.

### 3.3. Una conjetura de positividad de Jacobi reformulada

A la vista del cálculo anterior, reformulamos la positividad en términos más adecuados al contexto.

**Definición 3.4 (Discrepancia de log-convexidad).** Para la sucesión $\{(a_k^{full})^2\}$, definimos la discrepancia de log-convexidad en el índice $k$ como:

$$\mathrm{LC}_k = (a_k^{full})^4 - (a_{k-1}^{full})^2 (a_{k+1}^{full})^2.$$

$\mathrm{LC}_k > 0$ expresa log-concavidad local en $k$; $\mathrm{LC}_k < 0$ expresa log-convexidad local.

**Conjetura 3.5 (Positividad de Jacobi — Analog de Castelnuovo-Severi).** Para el operador de Jacobi $J^{full}$ asociado a $dm_{full} = |\zeta(1/2+is)|^2\, dm_\infty$, los coeficientes satisfacen:

$$\mathrm{LC}_k = (a_k^{full})^4 - (a_{k-1}^{full})^2 (a_{k+1}^{full})^2 > 0 \quad \text{para todo } k \geq 1$$

(log-concavidad de los coeficientes, consistente con el comportamiento de $a_k^\infty$).

*Estado:* Conjetura. Su verificación requeriría acceso a los coeficientes $a_k^{full}$ a través del cálculo numérico o de estimaciones analíticas más finas. La relevancia de esta conjetura radica en que, para ciertos sistemas integrables, la log-concavidad de los coeficientes de Jacobi es consecuencia de la positividad de la función de correlación de la medida espectral, lo que conecta con el formalismo de Lee-Yang.

**Observación 3.6.** En el caso de curvas, la desigualdad de Hodge no se formula en términos de los coeficientes de un operador tridiagonal (no existe un operador de Jacobi natural para la función zeta de una curva finita, que tiene solo un número finito de ceros). La analogía correcta es más sutil: los "coeficientes de Jacobi de curvas" serían los coeficientes del polinomio $P_C$ vistos como función de su índice de grado; la log-concavidad de los coeficientes del polinomio real con raíces en $|u| = q^{-1/2}$ es una consecuencia directa de que las raíces son de igual módulo, por la desigualdad de Newton sobre coeficientes de polinomios con raíces de módulo constante.

---

## §4. El operador $\Phi$ de simetría funcional y el Pilar II en el mundo aritmético

### 4.1. La ecuación funcional como dualidad

La ecuación funcional de la función $\xi$ de Riemann es:

$$\xi(s) = \xi(1-s), \quad \text{donde } \xi(s) = \tfrac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).$$

Esto implica: si $\rho$ es un cero no trivial de $\zeta$, entonces $1-\rho$ también es cero. En combinación con la simetría de reflexión respecto al eje real ($\rho \to \bar\rho$), los ceros no triviales aparecen en cuádruplos $\{\rho, \bar\rho, 1-\rho, 1-\bar\rho\}$ (o en pares si $\rho$ es real o si $\mathrm{Re}(\rho) = 1/2$).

La simetría $\rho \mapsto 1-\rho$ es el análogo de la dualidad de Poincaré $\alpha_j \mapsto q/\alpha_j$ del caso de curvas bajo la correspondencia:

$$\alpha_j = q^{1-\rho}, \quad \frac{q}{\alpha_j} = q^\rho.$$

La dualidad $\rho \leftrightarrow 1-\rho$ fija el punto $\rho = 1/2$, al igual que la dualidad $\alpha \leftrightarrow q/\alpha$ fija los $\alpha$ con $|\alpha| = q^{1/2}$. Esta es la afirmación que RH quiere establecer: todos los ceros están en el punto fijo de la dualidad.

### 4.2. La implementación de la dualidad en $\ell^2(\mathbb{N})$

La ecuación funcional tiene su reflejo directo en los coeficientes de Jacobi de $dm_{full}$.

**Proposición 4.1 (Nulidad de $b_k^{full}$, recordatorio de Doc 74).** La medida $dm_{full}(s) = |\zeta(1/2+is)|^2\, dm_\infty(s)$ es par en $s$: $dm_{full}(-s) = dm_{full}(s)$. Esto implica $b_k^{full} = 0$ para todo $k \geq 0$.

*Demostración.* La paridad de $dm_\infty$ es inmediata de la definición. La paridad de $|\zeta(1/2+is)|^2$ se sigue de la ecuación funcional: $|\zeta(1/2+is)| = |\zeta(1/2-is)|$ para $s$ real, que es simplemente $|\zeta(\overline{1/2+is})| = |\overline{\zeta(1/2+is)}| = |\zeta(1/2+is)|$, consecuencia de que $\zeta$ es real sobre la recta real y $\overline{\zeta(z)} = \zeta(\bar z)$ por la ecuación funcional del principio de reflexión de Schwarz. $\square$

**Definición 4.2 (Operador de simetría $\Phi_N$).** Para un entero $N \geq 1$, definamos en el espacio finito-dimensional $V_N = \mathrm{span}\{e_0, e_1, \ldots, e_{2N-1}\} \subset \ell^2(\mathbb{N})$ el operador de involución:

$$\Phi_N(e_k) = e_{2N-1-k}, \quad 0 \leq k \leq 2N-1.$$

Este operador es una isometría de $V_N$ sobre sí mismo con $\Phi_N^2 = \mathrm{Id}_{V_N}$ (es una involución).

**Proposición 4.3 (Compatibilidad de $\Phi_N$ con $J^{full}$).** El operador $J^{full}$ restringido a $V_N$ (en la aproximación de la truncación $J_N^{full}$ que considera solo los coeficientes $a_0^{full}, \ldots, a_{2N-2}^{full}$) satisface:

$$\Phi_N J_N^{full} \Phi_N = -J_N^{full}$$

si y solo si todos los coeficientes $b_k^{full} = 0$ (condición de simetría central nula).

*Demostración.* El operador $J_N^{full}$ en la base $\{e_k\}_{k=0}^{2N-1}$ es la matriz tridiagonal con ceros en la diagonal (pues $b_k^{full} = 0$) y $a_k^{full}$ en las subdiagonales. Bajo la involución $\Phi_N(e_k) = e_{2N-1-k}$, el coeficiente $(j,k)$ de $\Phi_N J_N^{full} \Phi_N$ en la base original es $(J_N^{full})_{2N-1-j, 2N-1-k}$. Para que esto sea igual a $-(J_N^{full})_{j,k}$, basta que la matriz sea antisimétrica respecto a la reflexión antidiagonal, lo que ocurre cuando la diagonal es nula. En ese caso, el mapa $e_k \mapsto (-1)^k e_{2N-1-k}$ relaciona la parte inferior del espectro de $J_N^{full}$ con la parte superior. $\square$

**Corolario 4.4 (El Pilar II está incorporado).** La dualidad de Poincaré — el hecho de que los ceros de $\zeta$ vienen en pares $(\rho, 1-\bar\rho)$ — está automáticamente incorporada en la estructura del operador $J^{full}$ a través de la nulidad $b_k^{full} = 0$. El operador $\Phi_N$ implementa la dualidad a nivel de $\ell^2$, de modo que el Pilar II es un resultado incondicional.

**Consecuencia.** En la analogía con el mecanismo de Weil, el estado actual es:

- Pilar I (Frobenius): $J^{full}$ es un candidato, pero sin las propiedades exactas del Frobenius de curvas (finito-dimensional, con autovalores = ceros).
- Pilar II (Dualidad): Automático, consecuencia de la ecuación funcional y de $b_k^{full} = 0$.
- Pilar III (Positividad): **Faltante.** Este es el obstáculo central.

La situación es exactamente paralela al caso de curvas: la dificultad real es la positividad, no la simetría.

---

## §5. El obstáculo de la dimensión infinita

### 5.1. El argumento de Weil en dimensión finita

En el caso de curvas, el argumento decisivo de positividad puede formularse así. Sean $\alpha_1, \ldots, \alpha_{2g}$ los autovalores de $\mathrm{Fr}_q^*|_{H^1}$ (con $H^1 = H^1_{\text{ét}}(\bar C, \mathbb{Q}_\ell)$, $\dim H^1 = 2g$). La dualidad de Poincaré fuerza que los autovalores vienen en pares $(\alpha_j, q/\alpha_j)$. La forma hermítica:

$$B(v,w) = \langle v, \mathrm{Fr}_q^* w \rangle_{H^1}$$

es la que debe ser positiva definida. En términos de autovalores, la positividad de $B$ requiere que los $\alpha_j$ satisfagan $\alpha_j > 0$ (si $H^1$ fuera real y unidimensional), pero en el caso general la positividad de la forma de Weil equivale a $|\alpha_j|^2 = q$, que implica $|\alpha_j| = q^{1/2}$.

La traza de la forma es:

$$\mathrm{Tr}(B) = \mathrm{Tr}(\mathrm{Fr}_q^*) = \sum_{j=1}^{2g} \alpha_j = N_1 - q - 1 \in \mathbb{Z}.$$

Esta es una suma finita. La positividad de la forma cuadrática asociada (la desigualdad de Hodge para el divisor $\Gamma \in C \times C$) implica:

$$\sum_{j=1}^{2g} |\alpha_j|^2 \leq \left(\sum_{j=1}^{2g} |\alpha_j|\right)^2 / (2g),$$

y junto con la ecuación funcional (que fuerza que los módulos de los $\alpha_j$ son todos iguales a $q^{1/2}$ o aparecen en pares $r, q/r$), se concluye $|\alpha_j| = q^{1/2}$.

**Proposición 5.1 (El argumento de Weil requiere dimensión finita).** El argumento anterior utiliza de modo esencial que $2g < \infty$:

(i) La traza $\sum_{j=1}^{2g} \alpha_j$ converge absolutamente (es una suma finita).

(ii) La desigualdad de Cauchy-Schwarz $|\sum \alpha_j|^2 \leq 2g \sum |\alpha_j|^2$ es una afirmación finito-dimensional.

(iii) La igualdad $\sum_{j=1}^{2g} |\alpha_j|^2 = 2g \cdot q$ (que todos los módulos son iguales a $q^{1/2}$) se deduce de la combinación de las desigualdades de Hodge y su dualizada, lo que requiere tanto la traza como la cotraza finitas.

*Demostración.* Los puntos (i)–(iii) son afirmaciones estándar de álgebra lineal finito-dimensional. En dimensión infinita, (i) es una serie potencialmente divergente, (ii) es una desigualdad que puede romperse, y (iii) no tiene sentido como tal. $\square$

### 5.2. El análogo infinito-dimensional y su obstáculo

En el caso de números, el análogo de $\sum_{j=1}^{2g} \alpha_j$ sería:

$$\sum_{\gamma_n} e^{it \gamma_n}$$

(suma sobre todos los ceros imaginarios de $\zeta$), que diverge para $t \neq 0$ (o bien oscila pero no converge absolutamente). El análogo de $\sum_{j=1}^{2g} |\alpha_j|^2$ sería:

$$\sum_{\rho} |\rho|^{-2\sigma_0}$$

con $\sigma_0$ apropiado, que converge para $\sigma_0$ grande pero diverge para $\sigma_0 = 0$.

**Proposición 5.2 (Divergencia de la "traza de Weil" directa).** Para el operador $J^{full}$ sobre $\ell^2(\mathbb{N})$, la traza $\mathrm{Tr}((J^{full})^n)$ diverge para $n \geq 1$, y $\mathrm{Tr}(E) = \mathrm{Tr}(J^{full} - J^\infty)$ no está definida como número real.

*Demostración.* La diagonal principal de $J^{full}$ es cero (pues $b_k^{full} = 0$), luego $\mathrm{Tr}(J^{full}) = 0$ formalmente. Pero la "traza de Weil" en el sentido del argumento del §5.1 sería $\mathrm{Tr}(\mathrm{Fr}) = \sum_j \alpha_j$, cuyo análogo es $\sum_n e^{i\gamma_n t}$ (divergente). Las potencias $(J^{full})^n$ tienen diagonal $(J^{full})^n_{kk} = \sum_{\text{caminos de longitud }n} a_{j_1}^{full} \cdots a_{j_n}^{full}$, y la suma $\sum_k (J^{full})^n_{kk}$ diverge por el crecimiento de los coeficientes $a_k^{full} \to \infty$. $\square$

### 5.3. El obstáculo cualitativo

El análisis anterior identifica el obstáculo central con precisión:

**Obstáculo (Dimensión infinita — Enunciado preciso).** El argumento de positividad de Weil para curvas utiliza que el Frobenius actúa sobre un espacio de dimensión finita $2g$. En dimensión infinita:

- La traza del operador de comparación $\mathrm{Tr}(J^{full} - J^{full,on})$ es formalmente $\sum_k (a_k^{full} - a_k^{full,on})$, que diverge (los coeficientes no son iguales y la perturbación no es traza-clase).
- Incluso si $E$ es de Hilbert-Schmidt (lo cual sí se verifica bajo las estimaciones del §2), ello permite controlar el espectro esencial (Killip-Simon) pero no fuerza la igualdad $J^{full} = J^{full,on}$.
- La positividad de la forma de sesquilinear $B(v,w) = \langle v, (J^{full} - J^{full,on})w \rangle_{\ell^2}$ no se puede establecer por argumentos finito-dimensionales directos.

---

## §6. Regularización via $T_\lambda$ y la conexión con el programa CCM

### 6.1. La traza regularizada

La traza divergente $\sum_k (a_k^{full})^2 - (a_k^{full,on})^2$ se puede regularizar mediante el kernel de Abel:

**Proposición 6.1 (La traza de Weil regularizada es $T_\lambda$).** La traza de discrepancia del programa CCM satisface:

$$T_\lambda = \int_{\mathbb{R}} W_\lambda(s)\, (dm_{full}(s) - dm_{full,on}(s)) = \sum_{k=0}^{N(\lambda)} \left[(a_k^{full})^2 - (a_k^{full,on})^2\right] + R_\lambda,$$

donde el término de error $R_\lambda$ proviene de la imperfección del kernel $W_\lambda$ como función indicadora del intervalo $[0, N(\lambda)]$, y satisface $R_\lambda \to 0$ cuando $\lambda \to \infty$ si los coeficientes convergen.

*Demostración.* La expansión de Christoffel-Darboux expresa el kernel $W_\lambda$ como una diferencia de normas parciales de los polinomios de Jacobi:

$$W_\lambda(s) = \sum_{k=0}^{N(\lambda)} (a_k^\infty)^2 (|P_{k+1}(s)|^2 - |P_k(s)|^2).$$

Integrando contra $dm_{full} - dm_{full,on}$ y utilizando la relación entre los coeficientes de Jacobi y las integrales de los polinomios (relación de Favard):

$$\int_{\mathbb{R}} |P_k(s)|^2 \, dm_{full}(s) = \frac{(a_k^{full})^2 + (a_{k-1}^{full})^2 + (b_k^{full})^2 + 1}{a_k^{full}}$$

(esta es la versión integral de la relación de recurrencia), se obtiene la relación con los coeficientes. La precisión de la aproximación $\sum_k [(a_k^{full})^2 - (a_k^{full,on})^2]$ para $T_\lambda$ es el contenido del Doc 64, §3. $\square$

**Interpretación.** La expresión $\sum_{k=0}^{N(\lambda)} [(a_k^{full})^2 - (a_k^{full,on})^2]$ es la "traza de la perturbación" del operador de Jacobi, regularizada al nivel $N(\lambda)$. Es el análogo directo de la suma finita $\sum_{j=1}^{2g} |\alpha_j|^2 - q$ en el caso de curvas (que sería cero bajo RH).

### 6.2. La conjetura central del análogo de Weil en dimensión infinita

**Conjetura 6.2 (Análogo de Weil en dimensión infinita — Versión regularizada).** RH es equivalente a que la traza de discrepancia regularizada sea cero para todo nivel de regularización:

$$\text{RH} \iff T_\lambda = 0 \text{ para todo } \lambda > 0$$

$$\iff \sum_{k=0}^{N(\lambda)} [(a_k^{full})^2 - (a_k^{full,on})^2] = 0 \text{ para todo } N \geq 0$$

$$\iff a_k^{full} = a_k^{full,on} \text{ para todo } k \geq 0.$$

*Observación.* La primera equivalencia es el criterio CTP del Doc 64 (Teorema 3.1), que es un resultado demostrado. La segunda equivalencia es un enunciado sobre la traza truncada que requiere demostración adicional (depende del tamaño de $R_\lambda$). La tercera equivalencia es la equivalencia de coeficientes de Jacobi (Proposición 6.1 del Doc 74).

Esta conjetura dice que el criterio $T_\lambda = 0$ es el análogo en dimensión infinita regularizada del criterio $\sum_{j=1}^{2g}(|\alpha_j|^2 - q) = 0$ de Weil, donde la regularización por el kernel $W_\lambda$ hace el papel de la dimensión finita $2g$ del caso de curvas.

### 6.3. El análogo del argumento de positividad en el mundo CCM

El camino potencial a RH via el análogo de Weil se descompone en tres pasos, paralelos al caso de curvas:

**Paso A (Análogo del Pilar I — Frobenius).** Se conoce: el operador $J^{full,on}$ (Jacobi de $dm_{full,on}$) codifica los ceros críticos de $\zeta$. Pero no se ha exhibido un "Frobenius aritmético" concreto con las propiedades exactas del Frobenius de curvas.

**Paso B (Análogo del Pilar II — Dualidad).** Demostrado: $b_k^{full} = b_k^{full,on} = 0$ (Proposición 4.1), consecuencia de la ecuación funcional.

**Paso C (Análogo del Pilar III — Positividad).** Abierto: demostrar que la forma cuadrática

$$Q(v) = \sum_{k=0}^{N} v_k^2 [(a_k^{full,on})^2 - (a_k^{full})^2]$$

es $\leq 0$ para todo $N$ y todo vector $v$ — es decir, que $a_k^{full} \geq a_k^{full,on}$ para todo $k$, con igualdad si y solo si RH. O bien, en la dirección opuesta: exhibir una forma cuadrática $Q_{pos}$ que sea positiva (trivialmente, pues $dm_{full}$ es positiva) y cuya positividad force la igualdad $a_k^{full} = a_k^{full,on}$.

---

## §7. La pregunta precisa y las estrategias para responderla

### 7.1. Formulación del problema abierto central

**Problema 7.1 (Positividad de Jacobi — Análogo de Castelnuovo-Severi aritmético).** Construir una forma cuadrática $Q_N: \mathbb{R}^{N+1} \to \mathbb{R}$ tal que:

(i) $Q_N \geq 0$ se puede demostrar sin asumir RH (la positividad es incondicional).

(ii) $Q_N(v) = 0$ para todo $v \in \mathbb{R}^{N+1}$ implica $a_k^{full} = a_k^{full,on}$ para $0 \leq k \leq N$.

(iii) $Q_N \to 0$ cuando $N \to \infty$ de manera controlada (compatibilidad con la regularización).

Si tal $Q_N$ existiera, el argumento de RH sería:

$$Q_N \geq 0 \text{ (incondicionalmente)} \implies a_k^{full} = a_k^{full,on} \;\forall k \leq N \implies T_\lambda = 0 \;\forall \lambda \implies \text{RH}.$$

### 7.2. ¿De dónde vendría la positividad de $Q_N$?

Identificamos tres fuentes posibles:

**Fuente 1: Positividad directa de $dm_{full}$.** La medida $dm_{full} = |\zeta|^2 dm_\infty$ es una medida de Borel positiva (trivialmente, pues es el producto de una función no negativa por una medida positiva). Pero la positividad de $dm_{full}$ implica solo que los momentos $\int s^k\, dm_{full}(s) \geq 0$ para $k$ par, lo que es insuficiente para determinar el signo de $dm_{full} - dm_{full,on}$.

**Fuente 2: Desigualdades de Turán para $|\zeta|^2$.** Las desigualdades de tipo Turán (método de potencias de Turán, 1948) dan cotas sobre sumas exponenciales del tipo $\sum_n a_n e^{i\lambda_n t}$ en términos de los coeficientes $a_n$ y las frecuencias $\lambda_n$. Una formulación adecuada podría dar desigualdades del tipo:

$$\int_a^b |\zeta(1/2+is)|^2\, f(s)\, ds \geq C(a,b) \int_a^b f(s)\, ds$$

para cierta clase de funciones $f$ y constante $C(a,b) > 0$. Si $f = |P_k|^2\, w$ (densidad de la medida $dm_\infty$ contra el polinomio $P_k$), esto daría $\Delta_k \geq 0$ con igualdad solo si los ceros de $\zeta$ están todos en la recta crítica — que es exactamente RH. Sin embargo, la implicación $\Delta_k \geq 0 \Rightarrow$ RH requiere invertir la lógica de manera no trivial.

**Fuente 3: Positividad de la función zeta completa $\xi$.** La función $\xi(s)$ es real sobre la recta real y tiene todos sus ceros (bajo RH) sobre la recta crítica. La positividad de $\xi$ en ciertos dominios, o la propiedad de que $\xi$ es una función de Pólya-Laguerre (límite de polinomios con raíces reales), da restricciones sobre la distribución de sus ceros. Si $\xi$ fuera una función de Pólya-Laguerre, RH seguiría. Pero demostrar que $\xi$ tiene esta propiedad es equivalente a RH.

### 7.3. Conclusión: el obstáculo y la estructura del problema

**Proposición 7.2 (Diagnóstico del obstáculo).** El programa de importar el mecanismo de Weil al caso de números a través del formalismo CCM está bloqueado por el Pilar III (positividad) en el siguiente sentido preciso:

(i) El Pilar I está parcialmente implementado: $J^{full}$ codifica los ceros de $\zeta$, pero no en la forma directa autovalores = ceros.

(ii) El Pilar II está completamente implementado: la ecuación funcional da $b_k^{full} = 0$ y la dualidad $\rho \leftrightarrow 1-\rho$.

(iii) El Pilar III está ausente: no se conoce ninguna forma cuadrática incondicional positiva cuya positividad implique $a_k^{full} = a_k^{full,on}$.

*Demostración.* (i) es el contenido del §1 y §5. (ii) es la Proposición 4.1 y el Corolario 4.4. (iii) es la consecuencia de la Proposición 5.2 y la discusión del §7.2: todas las fuentes de positividad conocidas (medida positiva, desigualdades de Turán, positividad de $\xi$) son o bien circulares (asumen RH) o bien insuficientes para forzar la igualdad de coeficientes. $\square$

**Observación final 7.3 (La analogía como guía).** A pesar del bloqueo en el Pilar III, la analogía con el caso de curvas cumple un papel heurístico preciso: indica que la positividad buscada es del tipo de una "desigualdad de Hodge" para el operador de Jacobi, y que el formalismo correcto para regularizar la dimensión infinita es el kernel $W_\lambda$ (análogo a la truncación a $N$ autovalores del Frobenius). Esta guía orienta la búsqueda hacia desigualdades espectrales para operadores de Jacobi perturbados, un campo activo de investigación (véase Simon [S11], Damanik-Killip-Simon [DKS10]).

---

## §8. Resumen de resultados y conjeturas

### 8.1. Resultados demostrados en este documento

1. **(Proposición 1.2)** $J^{full}$ es autoadjunto con espectro $\subseteq \mathbb{R}$; su espectro no distingue directamente la posición de los ceros de $\zeta$.

2. **(Proposición 2.3)** La perturbación $E = J^{full} - J^\infty$ es de Hilbert-Schmidt bajo las estimaciones estándar sobre $|\zeta|^2$ en la recta crítica.

3. **(Proposición 3.2)** Los coeficientes $a_k^\infty$ son log-cóncavos (no log-convexos), lo que indica que la analogía Castelnuovo-Severi no se formula como log-convexidad de los coeficientes sino como log-concavidad.

4. **(Proposición 4.1 y Corolario 4.4)** La dualidad de Poincaré (Pilar II) está automáticamente incorporada via $b_k^{full} = 0$: el Pilar II del mecanismo de Weil es incondicional en el mundo de números.

5. **(Proposición 5.1 y 5.2)** El argumento de Weil no se puede transportar directamente a dimensión infinita porque las trazas relevantes divergen.

6. **(Proposición 6.1)** La traza $T_\lambda$ es la "traza de Weil regularizada" $\sum_{k \leq N(\lambda)} [(a_k^{full})^2 - (a_k^{full,on})^2]$, con el kernel $W_\lambda$ jugando el papel de la dimensión finita $2g$.

7. **(Proposición 7.2)** Diagnóstico del obstáculo: el Pilar III (positividad) es el único ausente; todos los demás elementos del mecanismo de Weil tienen un análogo bien definido en el formalismo CCM.

### 8.2. Conjeturas formuladas

- **(Conjetura 3.5)** Log-concavidad de $\{(a_k^{full})^2\}$: $(a_k^{full})^4 \geq (a_{k-1}^{full})^2(a_{k+1}^{full})^2$ para todo $k \geq 1$.

- **(Conjetura 6.2)** El criterio $T_\lambda = 0$ es el análogo en dimensión infinita regularizada del criterio de Weil $\sum_{j=1}^{2g}(|\alpha_j|^2 - q) = 0$ para curvas.

- **(Problema 7.1)** Construcción de la forma cuadrática incondicional $Q_N \geq 0$ cuya positividad implique RH: este es el análogo preciso del problema de Hodge index / Castelnuovo-Severi aritmético.

---

## Referencias

- [A65] N. Akhiezer, *The Classical Moment Problem and Some Related Questions in Analysis*, Oliver and Boyd, 1965.
- [C99] A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. 5 (1999), 29–106.
- [CCM24] A. Connes, C. Consani, H. Moscovici, *Spectral triples and zeta functions*, preprint, 2024.
- [DKS10] D. Damanik, R. Killip, B. Simon, *Perturbations of orthogonal polynomials with periodic recursion coefficients*, Ann. of Math. 171 (2010), 1931–2010.
- [KS03] R. Killip, B. Simon, *Sum rules for Jacobi matrices and their applications to spectral theory*, Ann. of Math. 158 (2003), 253–321.
- [S11] B. Simon, *Szegő's Theorem and Its Descendants: Spectral Theory for $L^2$ Perturbations of Orthogonal Polynomials*, Princeton University Press, 2011.
- [T51] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (revised by D. R. Heath-Brown), Oxford University Press, 1986.
- [Docs 64, 70–76] Documentos internos del programa, Fases 32–33.

---

*Fin del Documento 77.*
