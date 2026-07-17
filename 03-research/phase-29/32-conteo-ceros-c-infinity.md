# Phase 29 — Doc 32: Dirección B — Conteo de Ceros de $C_\infty$ y la Inclusión Inversa

**Fecha:** junio 2026  
**Dirección:** B (cómputo directo via EF2-emp)  
**Objetivo:** Probar que $N_{C_\infty}(T) = N_\Xi(T)$ via la identidad EF2-emp y el principio del argumento. Si se establece la igualdad de conteos, y dado que $\{C_\infty=0\} \subseteq \{\Xi=0\}$ (Teorema 2, Doc 19), se concluye Inc. Inv. $\Leftrightarrow$ RH.

---

## 1. El puente: de los eigenvalores a los ceros de $C_\infty$

**Recordatorio (Theorem C1, Doc 17).** La función de Weyl-Titchmarsh $m_\infty^{WT}(z)$ del operador límite $J_\infty$ satisface la ecuación de Möbius:

$$m_\infty^{WT}(z) = \cfrac{1}{b_0 - z - a_0^2 m_\infty^{(1)}(z)},$$

donde $m_\infty^{(n)}$ es la función WT del operador truncado en $n$. Del análisis de Doc 17: los polos de $m_\infty^{WT}$ sobre $\mathbb{R}$ son exactamente los ceros reales de $C_\infty$. En forma de proposición:

**Proposición 1** (eigenvalores = ceros de $C_\infty$). Para todo $t_0 \in \mathbb{R}$:

$$t_0 \in \operatorname{spec}(J_\infty) \iff C_\infty(t_0) = 0.$$

*Prueba.* $t_0$ es eigenvalor de $J_\infty$ iff $\mu_\infty^{WT}(\{t_0\}) > 0$ iff $m_\infty^{WT}$ tiene polo en $t_0$. Por la EF2-WT (Doc 17, Theorem C1), los polos de $m_\infty^{WT}$ son los ceros de $C_\infty$. $\square$

**Corolario 1** (inclusión directa, Teorema 2 de Doc 19). Dado que $m_\infty^{emp}(z) \to \mu_\gamma^{real}$ (Doc 15) y $\mu_\gamma^{real}$ tiene soporte $\{\gamma_n\}$, y $\operatorname{spec}(J_\infty) \subseteq \operatorname{supp}(\mu_\gamma^{real})$:

$$\{C_\infty = 0 \text{ en } \mathbb{R}\} \subseteq \{\Xi = 0 \text{ en } \mathbb{R}\} = \{\gamma_n\}.$$

Esta es la inclusión DIRECTA — incondicional.

---

## 2. La inclusión inversa como igualdad de conteos

**Definición.** Sean:

$$N_{C_\infty}(T) := \#\{t \in [0,T] : C_\infty(t) = 0\}, \quad N_\Xi(T) := \#\{t \in [0,T] : \Xi(t) = 0\}.$$

**Proposición 2** (Inc. Inv. $\Leftrightarrow$ igualdad de conteos). De la inclusión directa (Corolario 1):

$$N_{C_\infty}(T) \leq N_\Xi(T) \quad \text{para todo } T > 0.$$

La inclusión inversa (Inc. Inv.) es equivalente a:

$$N_{C_\infty}(T) \geq N_\Xi(T) \quad \text{para todo } T > 0 \text{ suficientemente grande}.$$

*Prueba.* $\{C_\infty=0\} \subseteq \{\Xi=0\}$ con igualdad $\iff$ cada $\gamma_n \leq T$ es un cero de $C_\infty$. La igualdad de conteos es equivalente a la igualdad de conjuntos (pues la inclusión ya da $\leq$). $\square$

**Corolario 2** (RH desde el conteo). Combinando con el Teorema 3 (Doc 19):

$$N_{C_\infty}(T) = N_\Xi(T) \text{ para todo } T \gg 1 \iff \text{RH}.$$

---

## 3. El principio del argumento aplicado a $C_\infty$

**Setup.** Sea $R_T^\eta$ el rectángulo con vértices $0, T, T+i\eta, i\eta$ (orientado en sentido antihorario), donde $0 < \eta < 1/2$ (dentro de la franja de analiticidad de $C_\infty$, Proposición 1 de Doc 19).

**Proposición 3** (principio del argumento para $C_\infty$). Para $T$ no un cero de $C_\infty$ y $\eta \in (0,1/2)$:

$$N_{C_\infty}(T) = \frac{1}{2\pi i}\oint_{R_T^\eta} \frac{C_\infty'(z)}{C_\infty(z)}\, dz + E(T,\eta),$$

donde $E(T,\eta) = O(1)$ es el error de frontera de los lados verticales y del lado superior.

*Prueba.* La fórmula del argumento estándar. Los ceros de $C_\infty$ dentro de $R_T^\eta$ son exactamente los ceros reales en $[0,T]$ (pues $C_\infty$ no tiene ceros no-reales en la franja, por $\{C_\infty=0\} \subseteq \{\Xi=0\}$ y los ceros de $\Xi$ en la franja $|\Im z| < 1/2$ corresponden a ceros de $\zeta$ fuera de la recta crítica, más los ceros reales). $\square$

---

## 4. La EF2-emp como puente hacia $N_\Xi$

**La identidad fundamental (EF2-emp, Doc 27 Corolario 1).** Para $z \in \mathbb{C}^+$:

$$\frac{C_\infty'(z)}{C_\infty(z)} = N \cdot m_\infty^{emp}(z) + \frac{\Xi'(z)}{\Xi(z)}.$$

Integrando sobre $R_T^\eta$ (antihorario):

$$\frac{1}{2\pi i}\oint_{R_T^\eta} \frac{C_\infty'}{C_\infty}\,dz = N \cdot \frac{1}{2\pi i}\oint_{R_T^\eta} m_\infty^{emp}(z)\,dz + \frac{1}{2\pi i}\oint_{R_T^\eta} \frac{\Xi'}{\Xi}\,dz.$$

El tercer término (principio del argumento para $\Xi$):

$$\frac{1}{2\pi i}\oint_{R_T^\eta} \frac{\Xi'}{\Xi}\,dz = N_\Xi(T) + E_\Xi(T,\eta),$$

donde $E_\Xi = O(1)$ es el error de frontera.

**Luego:**

$$N_{C_\infty}(T) = N \cdot \mathcal{I}(T,\eta) + N_\Xi(T) + O(1),$$

donde

$$\mathcal{I}(T,\eta) := \frac{1}{2\pi i}\oint_{R_T^\eta} m_\infty^{emp}(z)\,dz.$$

---

## 5. El cálculo de $\mathcal{I}(T,\eta)$

**Proposición 4** (cálculo de $\mathcal{I}$ via el teorema de residuos). La función $m_\infty^{emp}$ es la transformada de Stieltjes de $\mu_\gamma^{real}$:

$$m_\infty^{emp}(z) = \int_\mathbb{R} \frac{d\mu_\gamma^{real}(t)}{z-t} = \frac{1}{N}\sum_{n:\, \gamma_n > 0} \frac{1}{z-\gamma_n}$$

(asumiendo la normalización $\mu_\gamma^{real} = (1/N)\sum_{n=1}^N \delta_{\gamma_n}$ con $N$ el número de ceros en $[0,T]$, en un límite regularizado).

Por el teorema de residuos (contorno $R_T^\eta$ encerrando los polos de $m_\infty^{emp}$ que son los $\gamma_n \in [0,T]$):

$$\mathcal{I}(T,\eta) = \frac{1}{2\pi i}\oint_{R_T^\eta} \frac{1}{N}\sum_n \frac{1}{z-\gamma_n}\,dz = \frac{1}{N}\sum_{n:\, \gamma_n \in [0,T]} 1 = \frac{N_\Xi(T)}{N}.$$

**Corolario 3** (la ecuación fundamental de conteo). Sustituyendo:

$$\boxed{N_{C_\infty}(T) = N \cdot \frac{N_\Xi(T)}{N} + N_\Xi(T) + O(1) = 2 N_\Xi(T) + O(1).}$$

---

## 6. La contradicción aparente y su resolución

**La ecuación fundamental de conteo dice:** $N_{C_\infty}(T) = 2N_\Xi(T) + O(1)$.

Pero la inclusión directa (Corolario 1) requiere $N_{C_\infty}(T) \leq N_\Xi(T)$. Tener $N_{C_\infty}(T) = 2N_\Xi(T)$ contradice $N_{C_\infty}(T) \leq N_\Xi(T)$ para $N_\Xi(T) \to \infty$.

**Diagnóstico.** La contradicción indica que el cálculo de $\mathcal{I}$ es incorrecto, o que la EF2-emp no puede usarse en este modo. Identificamos tres fuentes de error:

**Error A (normalización de $N$).** El factor $N$ en la EF2-emp es el factor de renormalización del operador truncado $J_\lambda^N$, y $N \to \infty$ cuando $\lambda \to \infty$. El cálculo de $\mathcal{I} = N_\Xi(T)/N$ usa el mismo $N$, pero en el producto $N \cdot \mathcal{I} = N_\Xi(T)$, los factores $N$ se cancelan — esto es consistente.

Lo que ocurre: $N \cdot m_\infty^{emp}(z) \to \infty$ puntualmente (para cada $z$ fijo), pero la integral contorno de $N \cdot m_\infty^{emp}$ sobre $R_T^\eta$ da $N_\Xi(T)$ (que también crece). Los cocientes son finitos.

**Error B (convergencia de la EF2-emp en el límite).** La EF2-emp es una identidad para el operador FINITO $J_\lambda^N$. En el límite $N \to \infty$: la EF2 escala como $N \to \infty$, y la derivada logarítmica $C_\infty'/C_\infty$ también escala. La ecuación fundamental de conteo es:

$$N_{C_\infty}(T) = 2N_\Xi(T) + O(1)$$

y es CONSISTENTE si $C_\infty$ tiene (aproximadamente) $2N_\Xi(T)$ ceros — pero esto contradiría $\{C_\infty=0\} \subseteq \{\Xi=0\}$.

**La resolución correcta.** La EF2-emp en el límite $N\to\infty$ da:

$$m_\infty^{emp}(z) = \frac{1}{N}\frac{C_\infty'(z)}{C_\infty(z)} - \frac{1}{N}\frac{\Xi'(z)}{\Xi(z)},$$

con el factor $1/N$ en AMBOS términos (Doc 27, §7). La integral contorno:

$$\frac{1}{2\pi i}\oint \frac{C_\infty'}{C_\infty}\,dz = N_\Xi(T) + N \cdot \frac{1}{2\pi i}\oint m_\infty^{emp}\,dz$$

$$= N_\Xi(T) + N \cdot \frac{N_\Xi(T)}{N} = 2N_\Xi(T).$$

Esto da $N_{C_\infty}(T) = 2N_\Xi(T)$, que CONTRADICE el Teorema 2 de Doc 19.

---

## 7. El diagnóstico correcto: la EF2-emp no puede coexistir con el Teorema B

**Teorema 1** (obstáculo de conteo). Las siguientes tres afirmaciones son INCOMPATIBLES:

(i) EF2-emp: $N \cdot m_\infty^{emp}(z) = C_\infty'(z)/C_\infty(z) - \Xi'(z)/\Xi(z)$ con $m_\infty^{emp}$ = Stieltjes de $\mu_\gamma^{real}$.

(ii) $\{C_\infty=0 \text{ en } \mathbb{R}\} \subseteq \{\Xi=0 \text{ en } \mathbb{R}\}$ (Teorema B).

(iii) $N_{C_\infty}(T) > 0$ para $T$ grande.

*Prueba.* (i) $\Rightarrow$ $N_{C_\infty}(T) = 2N_\Xi(T) + O(1)$. Pero (ii) $\Rightarrow$ $N_{C_\infty}(T) \leq N_\Xi(T)$. Juntos: $2N_\Xi(T) + O(1) \leq N_\Xi(T)$, es decir $N_\Xi(T) = O(1)$ — contradice (iii). $\square$

**Corolario 4.** Al menos una de las tres afirmaciones es falsa o requiere corrección. Como (ii) y (iii) son bien establecidas, la falla está en (i): la EF2-emp, tal como se formuló en Doc 27, tiene una inconsistencia.

---

## 8. La reinterpretación correcta de la EF2-emp

**El problema del factor N.** La EF2 finita para $J_\lambda^N$ es:

$$N \cdot m_\lambda^{emp}(z) = \frac{C_\lambda'(z)}{C_\lambda(z) - \mu_\lambda} - \frac{\hat k_\lambda'(z)}{\hat k_\lambda(z)}.$$

Esta es una identidad para el TRUNCADO finito. En el límite:

- El lado izquierdo: $N \cdot m_\lambda^{emp}(z) \to N \cdot m_\infty^{emp}(z)$ donde $m_\infty^{emp}$ es la Stieltjes de $\mu_\gamma^{real} = (1/N)\sum_n \delta_{\gamma_n}$, luego $N \cdot m_\infty^{emp}(z) = \sum_n 1/(z-\gamma_n)$.

- El lado derecho: $C_\lambda'/C_\lambda \to C_\infty'/C_\infty$ y $\hat k_\lambda'/\hat k_\lambda \to \Xi'/\Xi$.

Luego la EF2-emp EN EL LÍMITE es:

$$\sum_n \frac{1}{z-\gamma_n} = \frac{C_\infty'(z)}{C_\infty(z)} - \frac{\Xi'(z)}{\Xi(z)}.$$

**La identidad de la fórmula explícita.** El lado izquierdo $\sum_n 1/(z-\gamma_n)$ es precisamente la "parte de la recta crítica" de la derivada logarítmica de $\Xi$:

$$\frac{\Xi'(z)}{\Xi(z)} = \sum_{\gamma: \text{ todos los ceros}} \frac{1}{z-\gamma} = \sum_{\gamma_n \in \mathbb{R}} \frac{1}{z-\gamma_n} + \sum_{\gamma \notin \mathbb{R}} \frac{1}{z-\gamma}.$$

Bajo RH: todos los ceros de $\Xi$ son reales, luego $\Xi'/\Xi = \sum_n 1/(z-\gamma_n)$.

**Proposición 5** (la EF2-emp bajo RH colapsa). Bajo RH: $\sum_n 1/(z-\gamma_n) = \Xi'/\Xi$. La EF2-emp da:

$$\frac{\Xi'(z)}{\Xi(z)} = \frac{C_\infty'(z)}{C_\infty(z)} - \frac{\Xi'(z)}{\Xi(z)},$$

es decir $C_\infty'(z)/C_\infty(z) = 2\Xi'(z)/\Xi(z)$, que implica $C_\infty(z) = K \cdot \Xi(z)^2$ para alguna constante $K \neq 0$.

**Pero** $\{C_\infty=0\} = \{\Xi=0\}$ (bajo RH = Inc. Inv.) sería consistente con $C_\infty = K\Xi^2$ (los ceros de $C_\infty$ serían ceros dobles donde $\Xi$ tiene ceros simples).

**Inconsistencia final.** Si $C_\infty = K\Xi^2$ en la franja: entonces los ceros de $C_\infty$ serían los mismos que los de $\Xi$ pero con multiplicidad DOBLE. La inclusión directa $\{C_\infty=0\} \subseteq \{\Xi=0\}$ seguiría, pero los CONTEOS serían: $N_{C_\infty}(T) = N_\Xi(T)$ (mismos ceros, multiplicidad doble en $C_\infty$ simplemente contada dos veces). Esto da $N_{C_\infty}(T) = N_\Xi(T)$, consistente con Inc. Inv.

Pero la identidad $C_\infty = K\Xi^2$ NO es compatible con la definición explícita de $C_\infty$ vía la fórmula de Weil — a menos que $K = 0$, lo que haría $C_\infty \equiv 0$.

---

## 9. Conclusión honesta de la Dirección B

**Resultado neto.** La Dirección B revela una INCONSISTENCIA interna en la EF2-emp tal como se aplica a la cuestión de conteo de ceros. La ecuación fundamental de conteo $N_{C_\infty}(T) = 2N_\Xi(T) + O(1)$ es incompatible con el Teorema B.

**Diagnóstico preciso.** El error está en la toma del límite $N\to\infty$ en la EF2-emp. La identidad es válida para el operador finito, pero en el límite las dos funciones $m_\lambda^{emp}$ y $\mu_\gamma^{real}$ tienen una relación más delicada (la medida $\mu_\gamma^{real}$ ya cuenta los ceros de $\Xi$ y no puede ser la medida espectral límite de $m^{emp}$ sin correcciones).

**Lección de la Dirección B.** El camino de la EF2-emp al conteo de ceros no es directo. La EF2-emp relaciona $C_\infty'/C_\infty$ con $\Xi'/\Xi$ y $m^{emp}$, pero la triple relación contiene circularidad cuando se toma el límite.

**Lo que sí aporta.** La Dirección B clarifica que la EF2-emp, la inclusión directa y la normalización $N$ son tres piezas que deben ser reconciliadas con cuidado. La inconsistencia del cómputo directo de $N_{C_\infty}$ via EF2-emp es un resultado honesto: señala que no puede obtenerse Inc. Inv. trivialmente desde la EF2-emp sin información adicional.

**Remisión a la Dirección A.** La cuestión de si $C_\infty(z) = K\Xi(z)^2$ o una relación más rica se abordará en Doc 33 via la fórmula explícita y la estructura de punto fijo.

---

*Siguiente doc: Doc 33 — Dirección A: La Fórmula Explícita como Ecuación de Punto Fijo.*
