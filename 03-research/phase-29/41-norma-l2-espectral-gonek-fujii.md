# Phase 29 — Doc 41: La Energía $L^2$ Espectral y el Teorema de Gonek-Fujii

**Fecha:** junio 2026  
**Fase:** 32  
**Objetivo:** Atacar Inc. Inv. vía la norma $L^2$ espectral
$$E_2(\lambda, T) := \sum_{\gamma_n \leq T} |C_\lambda(\gamma_n)|^2,$$
usando el Teorema de Gonek-Fujii sobre sumas de Dirichlet evaluadas en los ceros de $\zeta$. La hipótesis de trabajo: el traslado del problema de convergencia puntual a un promedio cuadrático lo pone en el territorio donde la Teoría Analítica de Números ha tenido todos sus éxitos (Selberg, Montgomery, Goldston-Yıldırım).

---

## 1. El problema y su atractivo

La equivalencia RH $\iff$ Inc. Inv. (Theorem 9.1, Doc 40/paper) dice que demostrar Inc. Inv. equivale a demostrar RH. Inc. Inv. en forma puntual requiere: $C_\lambda(\gamma_n) \to 0$ para **cada** $n$ cuando $\lambda \to \infty$.

La convergencia puntual es la versión más fuerte. Pero si logramos demostrar

$$E_2(\lambda, T) \to 0 \quad \text{cuando } \lambda \to \infty, \quad \forall T,$$

entonces por el **Lema de la convergencia cuadrática**:

$$\frac{1}{N_\Xi(T)}\sum_{\gamma_n \leq T} |C_\lambda(\gamma_n)|^2 \to 0 \implies C_\lambda(\gamma_n) \to 0 \text{ para casi todo } n.$$

Aunque "casi todo" no es "todo", el ataque $L^2$ puede:
1. Dar asintóticas precisas de $E_2(\lambda,T)$ en términos de aritmética de primos.
2. Identificar el mecanismo de cancelación.
3. Producir una cota $E_2(\lambda,T) = o(N_\Xi(T) \cdot w(T)^2)$ que es una versión promediada de Inc. Inv.
4. En el mejor caso: probar $E_2(\lambda,T) \to 0$ — lo que implica Inc. Inv. (y por tanto RH) si la convergencia es uniforme en $n$.

**La razón estratégica:** la norma $L^2$ promedia sobre todos los ceros $\gamma_n \leq T$. En este promedio, las herramientas de TAN (correlaciones de pares de ceros, fórmulas explícitas, lema de Landau) son más potentes que para preguntas puntuales.

---

## 2. Expansión de $E_2(\lambda, T)$: los tres términos

Escribimos $C_\lambda(\gamma_n) = w(\gamma_n) - D_\lambda(\gamma_n)$ donde

$$D_\lambda(\gamma_n) = 2\sum_{m \leq \lambda^2} \Lambda(m)\, m^{-1/2}\cos(\gamma_n\log m).$$

Entonces:

$$|C_\lambda(\gamma_n)|^2 = |w(\gamma_n) - D_\lambda(\gamma_n)|^2 = w(\gamma_n)^2 - 2w(\gamma_n)D_\lambda(\gamma_n) + D_\lambda(\gamma_n)^2.$$

Sumando sobre $\gamma_n \leq T$:

$$\boxed{E_2(\lambda, T) = \underbrace{\sum_{\gamma_n \leq T} w(\gamma_n)^2}_{A(\lambda,T)} - 2\underbrace{\sum_{\gamma_n \leq T} w(\gamma_n) D_\lambda(\gamma_n)}_{B(\lambda,T)} + \underbrace{\sum_{\gamma_n \leq T} D_\lambda(\gamma_n)^2}_{C(\lambda,T)}.}$$

Inc. Inv. equivale a $E_2(\lambda,T) \to 0$, lo que requiere:

$$B(\lambda,T) \to \frac{A(\lambda,T) + C(\lambda,T)}{2},$$

es decir, el término cruzado $B$ debe cancelar casi completamente los términos diagonales $A$ y $C$.

---

## 3. El Teorema de Gonek-Fujii

**Teorema de Gonek-Fujii (1995).** Para una suma de Dirichlet $P_N(t) = \sum_{n \leq N} a_n n^{-it}$ con coeficientes $a_n$:

$$\sum_{0 < \gamma_j \leq T} |P_N(\gamma_j)|^2 = \frac{T}{2\pi}\log T \sum_{n \leq N} |a_n|^2 - \frac{T}{2\pi}\sum_{n \leq N} |a_n|^2 \log n + \text{(Landau terms)} + E(N,T),$$

donde el error $E(N,T) = O((T+N)\log^c(TN))$ para alguna constante $c$.

Los **términos de Landau** provienen de la correlación entre las sumas de Dirichlet evaluadas en los ceros de $\zeta$ y los coeficientes de la derivada logarítmica $-\zeta'/\zeta$. La versión precisa:

$$\sum_{0 < \gamma_j \leq T} \left|\sum_{n \leq N} a_n n^{-i\gamma_j}\right|^2 = \frac{T}{2\pi}\log\frac{T}{2\pi} \sum_{n\leq N}|a_n|^2 - 2\operatorname{Re}\sum_{n\leq N}a_n\bar{a}_n\sum_{m\leq N}\frac{a_m\bar{a}_m}{m^{i(\gamma_j - \cdot)}} + \ldots$$

Para los coeficientes $a_n = 2\Lambda(n)n^{-1/2}$ que corresponden a $D_\lambda$:

$$C(\lambda,T) = \sum_{\gamma_n \leq T} D_\lambda(\gamma_n)^2 = \sum_{\gamma_n \leq T}\left|2\sum_{m\leq\lambda^2}\Lambda(m)m^{-1/2-i\gamma_n}\right|^2.$$

---

## 4. Cálculo del término diagonal $C(\lambda,T)$

**Proposición 1** (Asintótica de $C(\lambda,T)$ via Gonek-Fujii). Bajo las hipótesis del Teorema de Gonek-Fujii:

$$C(\lambda,T) = \frac{T}{2\pi}\log T \cdot 4\sum_{m\leq\lambda^2}\Lambda(m)^2 m^{-1} - \frac{T}{2\pi}\cdot 4\sum_{m\leq\lambda^2}\Lambda(m)^2 m^{-1}\log m + \mathcal{L}(\lambda,T) + O((T+\lambda^2)\log^c(T\lambda)),$$

donde el término de Landau es:

$$\mathcal{L}(\lambda,T) = \frac{T}{\pi}\sum_{m\leq\lambda^2}\Lambda(m)^2 m^{-1} \cdot \frac{\Lambda(m^2)}{m} + \ldots$$

Simplificando con $4\sum_{m\leq\lambda^2}\Lambda(m)^2/m \sim 8\log\lambda$:

$$\boxed{C(\lambda,T) \sim \frac{T}{2\pi}\log T \cdot 8\log\lambda - \frac{T}{2\pi} \cdot S_1(\lambda) + \mathcal{L}(\lambda,T),}$$

donde $S_1(\lambda) = 4\sum_{m\leq\lambda^2}\Lambda(m)^2\log(m)/m \sim 8(\log\lambda)^2$ (la suma de Chebyshev ponderada).

*Prueba.* Aplicación directa del Teorema de Gonek-Fujii con $a_n = 2\Lambda(n)n^{-1/2}$. Los coeficientes satisfacen: $\sum_{n\leq N}|a_n|^2 = 4\sum_{n\leq N}\Lambda(n)^2/n \sim 8\log\lambda$ (Doc 39 Proposición 3). $\square$

**Observación 1.** El término dominante de $C(\lambda,T)$ es $\frac{4T\log T\log\lambda}{\pi}$. Crece como $T(\log T)(\log\lambda)$.

---

## 5. Cálculo del término aritmético $A(\lambda,T)$

**Proposición 2** (Asintótica de $A(\lambda,T)$). Por el Teorema de von Mangoldt:

$$N_\Xi(T) = \frac{T}{2\pi}\log\frac{T}{2\pi} - \frac{T}{2\pi} + O(\log T).$$

Y $w(\gamma_n) \sim \frac{1}{2}\log\gamma_n \sim \frac{1}{2}\log\frac{n\cdot 2\pi}{\log n}$ para $n$ grande (con $\gamma_n \sim 2\pi n/\log n$).

Por la fórmula de Abel-Stieltjes:

$$A(\lambda,T) = \sum_{\gamma_n \leq T} w(\gamma_n)^2 \approx \int_0^T w(t)^2 \,dN_\Xi(t) \sim \int_0^T \frac{(\log t)^2}{4} \cdot \frac{\log T}{2\pi}\,dt \sim \frac{T(\log T)^3}{24\pi}.$$

**Observación 2.** El término $A(\lambda,T) \sim \frac{T(\log T)^3}{24\pi}$ crece mucho más rápido que $C(\lambda,T) \sim \frac{4T\log T\log\lambda}{\pi}$ cuando $\log\lambda \ll (\log T)^2$.

Este contraste de escala es la clave de la estrategia $L^2$: para que $E_2 \to 0$, el término cruzado $B$ debe cancelar $A + C$, pero $A$ domina para $\lambda$ fijo y $T$ grande. Esto indica que el ataque $L^2$ debe tomarse en el régimen $\lambda \to \infty$ primero, con $T$ grande pero fijo, no viceversa.

---

## 6. El término cruzado $B(\lambda,T)$: el corazón del problema

**Proposición 3** (Expansión de $B(\lambda,T)$). Intercambiando (condicionalmente) la suma sobre primos:

$$B(\lambda,T) = \sum_{\gamma_n \leq T} w(\gamma_n) D_\lambda(\gamma_n) = 2\sum_{m\leq\lambda^2}\Lambda(m)m^{-1/2}\sum_{\gamma_n \leq T} w(\gamma_n)\cos(\gamma_n\log m).$$

La suma interna es:

$$\mathcal{I}(\lambda,T;m) := \sum_{\gamma_n \leq T} w(\gamma_n)\cos(\gamma_n\log m).$$

**Proposición 4** (Descomposición de $\mathcal{I}$). Escribamos $\cos(\gamma_n\log m) = \frac{1}{2}(m^{i\gamma_n} + m^{-i\gamma_n})$:

$$\mathcal{I}(T;m) = \frac{1}{2}\sum_{\gamma_n\leq T}w(\gamma_n)(m^{i\gamma_n} + m^{-i\gamma_n}).$$

La suma $\sum_{\gamma_n\leq T}w(\gamma_n)m^{i\gamma_n}$ es una **suma de von Mangoldt ponderada sobre los imaginarios de los ceros** — el objeto central del **Lema de Landau**.

---

## 7. La Fórmula de Landau y la suma cruzada

**Lema de Landau** (versión para zeta). Para $m$ entero positivo y $T$ grande:

$$\sum_{0 < \gamma_n \leq T} m^{i\gamma_n} = -\frac{T}{2\pi}\frac{\Lambda(m)}{\sqrt{m}} + O(\sqrt{m}\log^2 T).$$

*Prueba.* De la fórmula explícita de Riemann para $\psi(x)$: tomando $x = e^{2\pi t/T}$ y sumando apropiadamente, la suma $\sum_\rho x^\rho$ produce el resultado. El coeficiente $\Lambda(m)/\sqrt{m}$ viene del residuo del polo de $-\zeta'/\zeta$ en $s = 1/2 + i\gamma_n$ modulado por $m^{-1/2+i\gamma_n}$. Ver Goldston [Gol95] o Conrey-Goldston [CG93]. $\square$

**Proposición 5** (Asintótica de $\mathcal{I}(T;m)$ via Landau). Usando el Lema de Landau:

$$\sum_{\gamma_n\leq T}w(\gamma_n)m^{i\gamma_n} = \sum_{\gamma_n\leq T}w(\gamma_n)m^{i\gamma_n}.$$

Necesitamos la versión **ponderada por $w(\gamma_n)$**. Por Abel:

$$\sum_{\gamma_n\leq T}w(\gamma_n)m^{i\gamma_n} = w(T)\sum_{\gamma_n\leq T}m^{i\gamma_n} - \int_0^T w'(t)\sum_{\gamma_n\leq t}m^{i\gamma_n}\,dt.$$

Usando el Lema de Landau para $\sum_{\gamma_n\leq t}m^{i\gamma_n} \approx -\frac{t\Lambda(m)}{2\pi\sqrt{m}}$:

$$\sum_{\gamma_n\leq T}w(\gamma_n)m^{i\gamma_n} \approx -\frac{\Lambda(m)}{2\pi\sqrt{m}}\left[w(T)\cdot T - \int_0^T w'(t)\cdot t\,dt\right].$$

La integral $\int_0^T w'(t)\cdot t\,dt = [w(t)\cdot t]_0^T - \int_0^T w(t)\,dt \approx w(T)\cdot T - \frac{T}{2}\log T$.

Luego:

$$\sum_{\gamma_n\leq T}w(\gamma_n)m^{i\gamma_n} \approx -\frac{\Lambda(m)}{2\pi\sqrt{m}}\cdot\frac{T}{2}\log T + O(T\log\log T).$$

**Corolario 1** (Asintótica de $\mathcal{I}(T;m)$). Para $m$ entero positivo fijo:

$$\mathcal{I}(T;m) = \sum_{\gamma_n\leq T}w(\gamma_n)\cos(\gamma_n\log m) \approx -\frac{\Lambda(m)}{2\pi\sqrt{m}}\cdot\frac{T\log T}{2} + O(T\log\log T).$$

---

## 8. La asintótica de $B(\lambda,T)$

**Teorema 1** (Asintótica del término cruzado). Para $\lambda$ fijo y $T \to \infty$:

$$B(\lambda,T) = 2\sum_{m\leq\lambda^2}\frac{\Lambda(m)}{\sqrt{m}}\cdot\mathcal{I}(T;m) \approx 2\sum_{m\leq\lambda^2}\frac{\Lambda(m)}{\sqrt{m}}\cdot\left(-\frac{\Lambda(m)}{2\pi\sqrt{m}}\cdot\frac{T\log T}{2}\right).$$

$$= -\frac{T\log T}{2\pi}\sum_{m\leq\lambda^2}\frac{\Lambda(m)^2}{m} + O(T\log\log T\cdot\log\lambda).$$

Como $\sum_{m\leq\lambda^2}\Lambda(m)^2/m \sim 2\log\lambda$:

$$\boxed{B(\lambda,T) \approx -\frac{T\log T\cdot 2\log\lambda}{\pi} + O(T\log\log T).}$$

*Verificación de signo.* $B(\lambda,T) < 0$ para $T$ y $\lambda$ grandes. Esto tiene sentido: $D_\lambda(\gamma_n)$ es una suma de cosenos con coeficientes $\Lambda(m)/\sqrt{m} > 0$, y el Lema de Landau dice que la suma $\sum m^{i\gamma_n}$ es NEGATIVA (proporcional a $-\Lambda(m)/\sqrt{m}$). Luego $D_\lambda(\gamma_n) < 0$ en promedio pesado por $w$, y $B = \sum w(\gamma_n)D_\lambda(\gamma_n) < 0$.

---

## 9. El balance de $E_2(\lambda,T)$

**Proposición 6** (Expansión asintótica de $E_2$). Para $\lambda$ fijo y $T \to \infty$:

$$E_2(\lambda,T) = A(\lambda,T) - 2B(\lambda,T) + C(\lambda,T).$$

Con los términos calculados:
- $A(\lambda,T) \sim \dfrac{T(\log T)^3}{24\pi}$
- $B(\lambda,T) \approx -\dfrac{2T\log T\log\lambda}{\pi}$
- $C(\lambda,T) \approx \dfrac{4T\log T\log\lambda}{\pi}$

Luego:

$$E_2(\lambda,T) \sim \frac{T(\log T)^3}{24\pi} - 2\cdot\left(-\frac{2T\log T\log\lambda}{\pi}\right) + \frac{4T\log T\log\lambda}{\pi}$$

$$= \frac{T(\log T)^3}{24\pi} + \frac{4T\log T\log\lambda}{\pi} + \frac{4T\log T\log\lambda}{\pi}$$

$$= \frac{T(\log T)^3}{24\pi} + \frac{8T\log T\log\lambda}{\pi}.$$

**Observación crítica.** Para $\lambda$ fijo y $T \to \infty$: $E_2(\lambda,T) \sim \frac{T(\log T)^3}{24\pi} \to \infty$.

¡$E_2$ NO tiende a cero con $T$ fijo y $\lambda$ fijo! El promedio cuadrático de $C_\lambda(\gamma_n)$ sobre los ceros crece como $(\log T)^2 / (24\pi/T \cdot N_\Xi(T))$... Calculemos el promedio normalizado:

$$\frac{E_2(\lambda,T)}{N_\Xi(T)} \approx \frac{T(\log T)^3/(24\pi)}{T\log T/(2\pi)} = \frac{(\log T)^2}{12}.$$

El promedio cuadrático de $|C_\lambda(\gamma_n)|$ sobre los ceros es $\sim \frac{\log T}{\sqrt{12}}$ — del orden $w(\gamma_n)/2$ como se esperaba (ya que $C_\lambda(\gamma_n) \approx w(\gamma_n)$ para $\lambda$ fijo).

**Diagnóstico:** Para $\lambda$ FIJO y $T \to \infty$, $E_2$ crece inevitablemente porque la mayoría de los $C_\lambda(\gamma_n) \approx w(\gamma_n) \neq 0$ (Inc. Inv. requiere $C_\infty(\gamma_n) = 0$ en el límite $\lambda \to \infty$, no $\lambda$ fijo).

---

## 10. El régimen correcto: $\lambda \to \infty$ con $T$ función de $\lambda$

**Propuesta de régimen.** En lugar de fijar $\lambda$ y tomar $T \to \infty$, debemos tomar:

$$\lambda \to \infty, \quad T = T(\lambda) \to \infty, \quad \text{con la relación } \lambda^2 \gg T \text{ (muchos primos por cero)}.$$

En este régimen, $C_\lambda(\gamma_n)$ se acerca al valor límite $C_\infty(\gamma_n)$ (que es 0 bajo Inc. Inv.) para los primeros $N_\Xi(T(\lambda))$ ceros.

**Definición 1.** Para una función $T = T(\lambda)$ que satisface $T(\lambda) \to \infty$ y $\lambda^2 \geq e^{c\sqrt{\log T(\lambda)}}$:

$$E_2(\lambda, T(\lambda)) = \sum_{\gamma_n \leq T(\lambda)} |C_\lambda(\gamma_n)|^2.$$

**Proposición 7** (Reformulación en el régimen $\lambda \to \infty$). Para $\gamma_n \leq T(\lambda)$ fijo:

$$C_\lambda(\gamma_n) = C_\infty(\gamma_n) - 2\sum_{m > \lambda^2}\frac{\Lambda(m)}{m^{1/2}}\cos(\gamma_n\log m)$$

$$= C_\infty(\gamma_n) - R_\lambda(\gamma_n),$$

donde la cola $R_\lambda(\gamma_n) = 2\sum_{m > \lambda^2}\Lambda(m)m^{-1/2}\cos(\gamma_n\log m) \to 0$ cuando $\lambda \to \infty$ para cada $\gamma_n$ fijo (convergencia condicional de la serie de Dirichlet).

**Luego:**

$$E_2(\lambda, T) = \sum_{\gamma_n \leq T}|C_\infty(\gamma_n) - R_\lambda(\gamma_n)|^2$$

$$= \sum_{\gamma_n\leq T}C_\infty(\gamma_n)^2 - 2\sum_{\gamma_n\leq T}C_\infty(\gamma_n)R_\lambda(\gamma_n) + \sum_{\gamma_n\leq T}R_\lambda(\gamma_n)^2.$$

**Proposición 8** (Rol del término de cola $R_\lambda$). La norma $L^2$ del término de cola:

$$\sum_{\gamma_n\leq T}R_\lambda(\gamma_n)^2 = 4\sum_{\gamma_n\leq T}\left|\sum_{m>\lambda^2}\Lambda(m)m^{-1/2}e^{i\gamma_n\log m}\right|^2.$$

Por Gonek-Fujii aplicado a la suma sobre $m > \lambda^2$:

$$\sum_{\gamma_n\leq T}R_\lambda(\gamma_n)^2 \approx \frac{T}{2\pi}\log T\cdot 4\sum_{m>\lambda^2}\Lambda(m)^2/m.$$

Como $\sum_{m>\lambda^2}\Lambda(m)^2/m$ diverge (la cola de la serie), este término es grande. La convergencia de $R_\lambda(\gamma_n) \to 0$ para cada $\gamma_n$ fijo (condicional) NO implica convergencia $L^2$.

**Este es el obstáculo estructural central de la norma $L^2$.**

---

## 11. El obstáculo $L^2$: divergencia de la norma de la cola

**Proposición 9** (Divergencia de $\|R_\lambda\|_{L^2}^2$). Para la cola:

$$\sum_{m>\lambda^2}\frac{\Lambda(m)^2}{m} \sim \log\lambda + O(1) \to \infty.$$

Por tanto, para $T = T(\lambda) \gg \lambda^2$:

$$\sum_{\gamma_n\leq T}R_\lambda(\gamma_n)^2 \sim \frac{T\log T}{\pi}\log\lambda \to \infty.$$

La norma $L^2$ del término de cola DIVERGE cuando $T/\lambda^2 \to \infty$.

**Diagnóstico:** La norma $L^2$ de $C_\lambda(\gamma_n) - C_\infty(\gamma_n)$ no va a 0 cuando $T \to \infty$ para $\lambda$ fijo, porque la convergencia de la serie de Dirichlet en los $\gamma_n$ es condicional (no $L^2$).

Para que $E_2(\lambda,T) \to 0$: se necesita simultáneamente:
1. $C_\infty(\gamma_n) = 0$ (Inc. Inv.) — lo que queremos probar.
2. $R_\lambda(\gamma_n) \to 0$ en norma $L^2$ — que falla incondicionalmente.

---

## 12. Recalibración: la energía $L^2$ relativa

El obstáculo del §11 surge del mal régimen. Reformulemos el problema correctamente.

**Definición 2** (Energía $L^2$ relativa). Para $\lambda$ grande y $T \leq \lambda$ (régimen donde la serie converge bien):

$$\tilde{E}_2(\lambda, T) := \sum_{\gamma_n \leq T}\left|C_\lambda(\gamma_n)\right|^2$$

pero tomado en el régimen $T = T(\lambda)$ donde $N_\Xi(T) = N_\Xi(T(\lambda))$ es el número de ceros que aproxima el operador $D_\lambda^N$ (con $N = N_\Xi(T)$).

En este régimen: $\lambda^2 \gg \gamma_{N_\Xi(T)}$ — hay muchos más primos que ceros, y la serie $\Psi_\lambda(\gamma_n)$ es una buena aproximación de $\Psi_\infty(\gamma_n)$.

**Proposición 10** (Estimación en el régimen correcto). Para $T \leq \lambda/(2\pi)$ (equivalente: $\gamma_n \lesssim \lambda/(2\pi)$ para los ceros en cuestión):

La diferencia entre $C_\lambda(\gamma_n)$ y $C_\infty(\gamma_n)$ es:

$$C_\lambda(\gamma_n) - C_\infty(\gamma_n) = 2\sum_{m > \lambda^2}\frac{\Lambda(m)}{m^{1/2}}\cos(\gamma_n\log m).$$

Para $\gamma_n \leq T \ll \lambda^2$: la suma de la cola está controlada por el error del PNT:

$$\left|\sum_{m>\lambda^2}\frac{\Lambda(m)}{m^{1/2+i\gamma_n}}\right| = \left|-\zeta'/\zeta(1/2+i\gamma_n) + \sum_{m\leq\lambda^2}\Lambda(m)m^{-1/2-i\gamma_n}\right|.$$

El valor de $-\zeta'/\zeta$ en $1/2+i\gamma_n$ (un polo) diverge, pero la suma truncada $\sum_{m\leq\lambda^2}\Lambda(m)m^{-1/2-i\gamma_n}$ aproxima el polo con error $O(1/(\lambda^2)^{1/2-\epsilon})$ para $\gamma_n \ll \lambda^2$.

---

## 13. La conexión con el segundo momento de la función Zeta

**Proposición 11** (Conexión con el segundo momento de $|\zeta'|$). La energía $E_2$ está relacionada con el segundo momento de la derivada de la función zeta en la línea crítica.

De Inc. Inv. $\iff$ $\Re[g_n(\rho_n)] = w(\gamma_n)/2$ (Proposición 7.3 del paper Doc 40):

$$C_\infty(\gamma_n) = 0 \iff -\Re[\zeta'/\zeta(1/2+i\gamma_n)] = w(\gamma_n)/2.$$

La energía espectral es:

$$E_2(\lambda,T) = \sum_{\gamma_n\leq T}|C_\lambda(\gamma_n) - C_\infty(\gamma_n)|^2 + 2\operatorname{Re}\sum_{\gamma_n\leq T}(C_\lambda(\gamma_n)-C_\infty(\gamma_n))\overline{C_\infty(\gamma_n)} + \sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2.$$

El término $\sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2$ es exactamente la energía en los ceros del potencial límite — que bajo Inc. Inv. es 0, y en general mide cuánto fallan los ceros de $\Xi$ en ser ceros de $C_\infty$.

**Proposición 12** (Inc. Inv. implica $E_2 \to 0$ en el régimen correcto). Si Inc. Inv. es verdadera (es decir, $C_\infty(\gamma_n) = 0$ para todo $n$), entonces:

$$E_2(\lambda, T) = \sum_{\gamma_n\leq T}|C_\lambda(\gamma_n) - C_\infty(\gamma_n)|^2 = \sum_{\gamma_n\leq T}|R_\lambda(\gamma_n)|^2.$$

Este término mide la velocidad de convergencia de $C_\lambda \to C_\infty$ en los ceros.

---

## 14. La pregunta correcta: convergencia $L^2$ de la cola en los ceros

De la Proposición 12: si Inc. Inv. es verdadera, entonces $E_2(\lambda,T) = \sum_{\gamma_n\leq T}|R_\lambda(\gamma_n)|^2$ donde $R_\lambda(\gamma_n)$ es la cola de la serie.

**Proposición 13** (Cota de la cola en los ceros via Gonek-Fujii). Por el Teorema de Gonek-Fujii aplicado a la suma de Dirichlet con coeficientes $a_m = 2\Lambda(m)m^{-1/2}\mathbf{1}_{m > \lambda^2}$:

$$\sum_{\gamma_n\leq T}|R_\lambda(\gamma_n)|^2 = \frac{T}{2\pi}\log T\cdot 4\sum_{m>\lambda^2}\frac{\Lambda(m)^2}{m} + \mathcal{L}^{\mathrm{tail}}(\lambda,T) + O((T+\lambda^2)\log^c(T\lambda)).$$

El término principal: $4\sum_{m>\lambda^2}\Lambda(m)^2/m \sim 4\log\lambda'$ donde $\lambda' \to \infty$ pero más lentamente. Este término sigue divergiendo.

**Diagnóstico final sobre la norma $L^2$:**

La norma $\sum_{\gamma_n\leq T}|R_\lambda(\gamma_n)|^2$ diverge cuando $T \to \infty$ para $\lambda$ fijo, **pero** el promedio normalizado por $N_\Xi(T)$:

$$\frac{1}{N_\Xi(T)}\sum_{\gamma_n\leq T}|R_\lambda(\gamma_n)|^2 \approx \frac{\log T \cdot \log\lambda}{N_\Xi(T)/T} \cdot \frac{1}{T} = \frac{\log T \cdot \log\lambda \cdot 2\pi}{\log T} = 2\pi\log\lambda$$

¡Sigue creciendo! El promedio cuadrático de la cola no va a 0.

---

## 15. La ruta genuina: energía $L^2$ con $T$ fijo y $\lambda \to \infty$

El análisis de las secciones anteriores revela que el régimen correcto para el ataque $L^2$ es:

$$\textbf{Fijar } T > 0 \textbf{ y tomar } \lambda \to \infty.$$

En este régimen: para cada $\gamma_n \leq T$ fijo, $R_\lambda(\gamma_n) \to 0$ cuando $\lambda \to \infty$ (convergencia condicional de la serie de Dirichlet). El número de términos $N_\Xi(T)$ es FIJO.

**Teorema 2** (Convergencia $L^2$ puntual en $T$ fijo). Para $T > 0$ fijo:

$$E_2(\lambda, T) = \sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2 + O\!\left(\sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|\cdot|R_\lambda(\gamma_n)| + \sum_{\gamma_n\leq T}|R_\lambda(\gamma_n)|^2\right).$$

Para cada $\gamma_n$ fijo:
- $|R_\lambda(\gamma_n)| \to 0$ cuando $\lambda \to \infty$ (por convergencia condicional de la serie $\sum\Lambda(m)m^{-1/2-i\gamma_n}$ a $-\zeta'/\zeta(1/2+i\gamma_n)$).
- La suma $\sum_{n=1}^{N_\Xi(T)}|R_\lambda(\gamma_n)|^2 \to 0$ (suma finita de términos que van a 0).

**Por tanto:**

$$\lim_{\lambda\to\infty} E_2(\lambda, T) = \sum_{\gamma_n \leq T}|C_\infty(\gamma_n)|^2. \quad (*)$$

**Teorema 3** (Inc. Inv. $\iff$ $E_2 \to 0$ en $T$ fijo). Para $T > 0$ fijo:

$$\lim_{\lambda\to\infty} E_2(\lambda, T) = 0 \quad \forall T \iff C_\infty(\gamma_n) = 0\;\forall n \iff \text{Inc. Inv.}$$

*Prueba.* De $(*)$: $\lim_\lambda E_2(\lambda,T) = \sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2$. Esta suma es 0 iff $C_\infty(\gamma_n) = 0$ para todo $\gamma_n \leq T$ — que es Inc. Inv. restringida a $[0,T]$. Como $T$ es arbitrario, la condición para todos los $T$ equivale a Inc. Inv. completa. $\square$

**Corolario 1** (Reformulación de Inc. Inv. via $E_2$). Las siguientes condiciones son equivalentes:

(i) Inc. Inv.: $C_\infty(\gamma_n) = 0$ para todo $n$.

(ii) $\displaystyle\lim_{\lambda\to\infty}E_2(\lambda,T) = 0$ para todo $T > 0$ fijo.

(iii) $\displaystyle\sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2 = 0$ para todo $T > 0$.

---

## 16. El problema reformulado: ¿vale $\sum |C_\infty(\gamma_n)|^2 = 0$?

El Teorema 3 nos dice que atacar $E_2 \to 0$ (en el régimen $T$ fijo, $\lambda\to\infty$) es exactamente equivalente a Inc. Inv. — ninguna información nueva.

El genuino avance sería probar directamente que $\sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2 = 0$ sin asumir Inc. Inv. Para eso necesitamos analizar $C_\infty(\gamma_n)$ directamente.

**Proposición 14** (Conexión con la derivada logarítmica en los polos). De la Proposición 7.3 del paper:

$$C_\infty(\gamma_n) = 0 \iff \Re[g_n(\rho_n)] = w(\gamma_n)/2,$$

donde $g_n(\rho_n) = \lim_{s\to\rho_n}[-\zeta'/\zeta(s) - 1/(s-\rho_n)]$.

Y:

$$|C_\infty(\gamma_n)|^2 = \left(w(\gamma_n) - 2\Re[g_n(\rho_n)]\right)^2 \cdot 4.$$

**La energía:**

$$\sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2 = 4\sum_{\gamma_n\leq T}\left(w(\gamma_n)/2 - \Re[g_n(\rho_n)]\right)^2.$$

Esta expresión involucra la distribución de los valores de $\Re[g_n(\rho_n)]$. Bajo RH, cada término es 0 (Lema 8.1 del paper). Incondicionalmente, cada término podría ser no-nulo.

---

## 17. Un resultado incondicional: la varianza de $\Re[g_n]$

**Proposición 15** (Varianza de los residuos regulares). Define:

$$\sigma^2(\lambda,T) := \frac{1}{N_\Xi(T)}\sum_{\gamma_n\leq T}\left(w(\gamma_n)/2 - \Re[g_n(\rho_n)]\right)^2 = \frac{E_2(\infty,T)}{4N_\Xi(T)}.$$

Esta es la **varianza muestral** de los residuos regulares $\Re[g_n(\rho_n)]$ alrededor de $w(\gamma_n)/2$.

Inc. Inv. equivale a $\sigma^2(\infty,T) = 0$ para todo $T$ — que es la condición de que los residuos regulares sean TODOS exactamente $w(\gamma_n)/2$.

**Proposición 16** (Cota incondicional de la varianza). El valor medio de $\Re[g_n(\rho_n)]$ sobre los ceros es:

$$\frac{1}{N_\Xi(T)}\sum_{\gamma_n\leq T}\Re[g_n(\rho_n)] = \frac{1}{N_\Xi(T)}\sum_{\gamma_n\leq T}\frac{w(\gamma_n)}{2} - \frac{1}{N_\Xi(T)}\frac{E_2(\infty,T)}{4 \cdot N_\Xi(T)}\cdot N_\Xi(T).$$

Bajo RH: el valor medio es exactamente $\frac{1}{N_\Xi(T)}\sum w(\gamma_n)/2$ (la varianza es 0). Incondicionalmente: la varianza podría ser positiva.

---

## 18. La pregunta clave para Doc 42: la varianza de los residuos

**El problema reformulado** (apropiado para el siguiente documento):

¿Puede acotarse incondicionalmente

$$\sigma^2(T) := \frac{1}{N_\Xi(T)}\sum_{\gamma_n\leq T}\left(\Re[g_n(\rho_n)] - w(\gamma_n)/2\right)^2?$$

**Ruta A (incondicional):** Usar la representación de Hadamard $(g_n)$ para expresar $\Re[g_n(\rho_n)] - w(\gamma_n)/2$ como una suma sobre los ceros off-críticos (si los hay):

$$\Re[g_n(\rho_n)] - w(\gamma_n)/2 = \operatorname{Re}\!\left[\sum_{\rho\neq\rho_n}\frac{1}{\rho_n-\rho}\right].$$

Incondicionalmente: si hay ceros con $\Re(\rho) \neq 1/2$, contribuyen con $\Re[1/(\rho_n-\rho)] = \frac{\Re(\rho_n-\rho)}{|\rho_n-\rho|^2} = \frac{1/2-\Re(\rho)}{|\rho_n-\rho|^2} \neq 0$.

**Observación fundamental.** La cantidad $\Re[g_n(\rho_n)] - w(\gamma_n)/2 = \operatorname{Re}\sum_{\rho\neq\rho_n}1/(\rho_n-\rho)$ es:
- = 0 si y solo si RH (Lema 8.1 del paper).
- $\neq 0$ si hay ceros off-críticos.

Luego $\sigma^2(T) = 0 \iff$ RH — es otra reformulación, no un avance.

**Ruta B (condicional mejorada):** Demostrar bajo hipótesis más débiles (por ejemplo: $\zeta$ no tiene ceros en $\Re(s) > 1/2 - \delta$ para algún $\delta < 1/2$) que $\sigma^2(T) = O(1/T^\epsilon)$ — una cota cuantitativa de cuánto puede desviarse Inc. Inv.

---

## 19. Diagnóstico final de la ruta $L^2$

**Resultado positivo de este documento:**

1. **Teorema 3** (Reformulación exacta): $\lim_\lambda E_2(\lambda,T) = \sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2$. La energía $L^2$ converge a una cantidad determinada — no diverge.

2. **Corolario 1** (Equivalencia): Inc. Inv. $\iff$ $E_2(\lambda,T) \to 0$ (en el régimen $T$ fijo, $\lambda\to\infty$).

3. **Proposición 14** (Conexión con residuos): La energía $E_2$ mide la varianza de los residuos regulares $\Re[g_n(\rho_n)]$ alrededor de su valor prescrito $w(\gamma_n)/2$.

**Obstáculo honesto:**

La norma $L^2$ no proporciona, por sí sola, una ruta incondicional a Inc. Inv. El lema de Landau y el Teorema de Gonek-Fujii son herramientas para calcular la asintótica de $E_2$ CONDICIONALMENTE a la distribución de los ceros — lo que produce círculos o hipótesis adicionales.

**La diferencia con Selberg y el PNT:** En el Teorema de los Números Primos, la norma $L^2$ de $\psi(x) - x$ va a 0 porque la región libre de ceros de $\zeta$ garantiza que los ceros NO estén en $\Re(s) = 1$. El análogo aquí sería: demostrar que los ceros off-críticos de $\zeta$ (si los hay) no afectan la suma $\sum_{\rho\neq\rho_n}1/(\rho_n-\rho)$ en promedio. Pero eso es equivalente a que no haya ceros off-críticos — i.e., RH.

---

## 20. Resumen y propuesta para Doc 42

**Resultado principal de Doc 41:**

La energía $L^2$ espectral $E_2(\lambda,T)$ converge a $\sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2$ cuando $\lambda\to\infty$ (para $T$ fijo). Inc. Inv. equivale a $E_2(\lambda,T)\to 0$ en este régimen. La conexión con Gonek-Fujii revela que la norma $L^2$ no es más atacable que Inc. Inv. misma — la barrera estructural del Doc 40 §10 se manifiesta también en el enfoque $L^2$.

**La lección:** Todas las reformulaciones del tipo "Inc. Inv. $\iff$ [condición sobre sumas sobre $\gamma_n$]" son equivalentes y comparten la misma barrera. La información sobre RH está "encoded" en la distribución de los $\gamma_n$, y cualquier aproximación que utilice esa distribución circularmente no puede probar RH.

**Propuesta para Doc 42:** Explorar si existe una cota $E_2(\lambda,T) \leq f(\lambda,T)$ INCONDICIONAL (sin usar la distribución de los $\gamma_n$ como input) que fuerce $E_2 \to 0$. Esto requeriría que la función $\sum_{\gamma_n\leq T}|C_\infty(\gamma_n)|^2$ tenga una cota superior incondicional que vaya a 0 — lo que equivale a demostrar RH. La pregunta es si hay una ruta "de vuelta" desde la cota a la prueba.

---

**Estado del programa después de Doc 41:**

| Implicación | Estado |
|---|---|
| Inc. Inv. $\Rightarrow$ RH | Probada (Teorema D, Doc 19) |
| RH $\Rightarrow$ Inc. Inv. | Probada (Teorema 4, Doc 39) |
| $E_2(\lambda,T)\to 0 \iff$ Inc. Inv. | Probada (Teorema 3, Doc 41) |
| Inc. Inv. [sin hipótesis] | **Abierta** — cuello de botella |

---

*Siguiente doc: Doc 42 — Exploración de la barrera estructural: ¿puede una cota incondicional de $E_2$ forzar Inc. Inv.?*
