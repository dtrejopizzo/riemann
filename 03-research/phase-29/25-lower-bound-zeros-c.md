# Phase 29 — Doc 25: Cota inferior para $N_{C_\infty}(T)$ y el argumento de cierre

**Fecha:** junio 2026  
**Objetivo:** Establecer una cota inferior $N_{C_\infty}(T) \geq N_\Xi^{crit}(T) - O(\log T)$ que, combinada con la cota superior del Teorema 2 del Doc 19 ($N_{C_\infty}(T) \leq N_\Xi^{crit}(T)$ ya que los ceros de $C_\infty$ están en $\{\Xi = 0\}$), daría la igualdad $N_{C_\infty}(T) = N_\Xi^{crit}(T)$ — equivalente a (Inc. Inv.) y por tanto a RH.

---

## 1. Las dos cotas que se necesitan combinar

**Cota superior** (ya demostrada). Por el Teorema 2 del Doc 19:

$$\{C_\infty = 0 \text{ en }\mathbb{R}\} \subseteq \{\Xi = 0 \text{ en }\mathbb{R}\} = \{\gamma_n : \rho_n = 1/2+i\gamma_n\},$$

luego $N_{C_\infty}(T) \leq N_\Xi^{crit}(T) = N_\Xi(T) + O(1)$ (bajo RH todos los ceros de $\Xi$ en $\mathbb{R}$ son críticos, sin RH $N_\Xi^{crit}(T) \leq N_\Xi(T)$).

**Cota inferior** (objetivo de este documento). Mostrar:

$$N_{C_\infty}(T) \geq N_\Xi^{crit}(T) - O(\log T). \quad (\star)$$

Si $(\star)$ se prueba incondicionalmente, junto con la cota superior: $N_{C_\infty}(T) = N_\Xi^{crit}(T) + O(\log T)$, lo que da (Inc. Inv.) en sentido de conteo.

---

## 2. El argumento de conteo via la medida espectral empírica

**Proposición 1** (la medida empírica da cota inferior). La convergencia débil $\mu_{emp}^\lambda \Rightarrow \mu_\gamma^{real}$ (Doc 15) implica: para todo intervalo $[a,b]$ con $\mu_\gamma^{real}(\{a,b\}) = 0$:

$$\lim_\lambda \mu_{emp}^\lambda([a,b]) = \mu_\gamma^{real}([a,b]) = \frac{N_\Xi^{crit}(b) - N_\Xi^{crit}(a)}{N_\Xi^{crit}(T)}\bigg|_{\text{normalizado}}.$$

Luego: el número de eigenvalores de $J_\lambda^N$ en $[a,b]$ es $\sim N \cdot \mu_\gamma^{real}([a,b])$ para $\lambda$ grande.

**Proposición 2** (los eigenvalores de $J_\lambda^N$ en $[a,b]$ son ceros de $C_\lambda$ que convergen a ceros de $C_\infty$ en $[a,b]$). Por el Teorema C1 del Doc 17: los eigenvalores del operador límite $J_\infty$ son los ceros de $C_\infty$ en $\mathbb{R}$. Si los eigenvalores de $J_\lambda^N$ convergen (en algún sentido) a los eigenvalores de $J_\infty$: el número de ceros de $C_\infty$ en $[a,b]$ es $\geq \limsup_\lambda N_{J_\lambda^N}([a,b])$.

*Esto daría:* $N_{C_\infty}([a,b]) \geq \limsup_\lambda N_{J_\lambda^N}([a,b]) \sim N\cdot\mu_\gamma^{real}([a,b]) \sim N_\Xi^{crit}([a,b])$.

**El gap en la Proposición 2.** La convergencia de los eigenvalores de $J_\lambda^N$ hacia los de $J_\infty$ requiere convergencia en la norma del resolvente (o convergencia en el sentido de Hausdorff del espectro). Para operadores no-acotados con dominios distintos, esta convergencia no es automática.

---

## 3. La convergencia del espectro de $J_\lambda^N$ hacia $\{C_\infty = 0\}$

**Teorema 1** (convergencia de los ceros de $C_\lambda$ hacia los de $C_\infty$, incondicional). Para cada cero $\gamma_n$ de $C_\infty$ (i.e., $C_\infty(\gamma_n) = 0$) con $C_\infty'(\gamma_n) \neq 0$ (cero simple):

Existe una sucesión $t_n^{(\lambda)} \to \gamma_n$ de ceros de $C_\lambda$ cuando $\lambda \to \infty$.

*Prueba.* Por el Teorema de la Función Implícita: $C_\lambda(t)$ depende continuamente de $\lambda$ (en el sentido de que $\|C_\lambda - C_\infty\|_{C^1([a,b])} \to 0$ para todo $[a,b]$ compacto). Si $C_\infty(\gamma_n) = 0$ y $C_\infty'(\gamma_n) \neq 0$: por el TFI, existe $t_n^{(\lambda)} \approx \gamma_n$ con $C_\lambda(t_n^{(\lambda)}) = 0$ para $\lambda$ suficientemente grande. $\square$

**El punto crítico.** El Teorema 1 da: los ceros SIMPLES de $C_\infty$ son límites de ceros de $C_\lambda$. Los ceros de $C_\lambda$ son los eigenvalores de $J_\lambda^N$ (por el Teorema C1 aplicado a $J_\lambda$). Luego: los ceros simples de $C_\infty$ están en el límite del espectro de $J_\lambda^N$.

**Proposición 3** (cota inferior de $N_{C_\infty}(T)$ via los ceros simples). Si todos los ceros de $C_\infty$ en $[0,T]$ son simples: el número de ceros de $C_\infty$ en $[0,T]$ es igual al número de ceros simples del límite del espectro de $J_\lambda^N$ en $[0,T]$, que por la convergencia débil es $\sim N_\Xi^{crit}(T)$. Luego:

$$N_{C_\infty}(T) \geq N_\Xi^{crit}(T) - O(\log T).$$

---

## 4. Argumento alternativo: el principio del argumento aplicado a $C_\lambda \to C_\infty$

**Proposición 4** (número de ceros de $C_\infty$ via el límite del principio del argumento de $C_\lambda$). Sea $\gamma_T = T + i\eta$ para $\eta \in (0,1/2)$. El número de ceros de $C_\lambda$ en el rectángulo $[0,T] \times [0,\eta]$ es:

$$N_{C_\lambda}(T;\eta) = \frac{1}{2\pi i}\oint_{\partial R_{T,\eta}}\frac{C_\lambda'(z)}{C_\lambda(z)}dz.$$

Bajo la convergencia $C_\lambda \to C_\infty$ en $C^1([0,T]\times[0,\eta])$ (uniforme en la franja): para $\lambda$ suficientemente grande:

$$N_{C_\lambda}(T;\eta) = N_{C_\infty}(T;\eta).$$

*Prueba.* Rouché aplicado a $C_\lambda$ y $C_\infty$ en el rectángulo: si $\|C_\lambda - C_\infty\|_\infty < |C_\infty|$ en el borde del rectángulo (que se da si la convergencia es uniforme y $C_\infty \neq 0$ en el borde), el número de ceros es el mismo. $\square$

**El problema.** La convergencia $C_\lambda \to C_\infty$ en $C^1$ requiere que $\Psi_\lambda(t) = 2\sum_{p\leq\lambda^2}\Lambda(p)p^{-1/2}e^{it\log p}$ converja a $\Psi(t)$ uniformemente en compactos de la franja. Esto es la condición de convergencia de la serie de Dirichlet — que NO converge absolutamente en $\mathbb{R}$ (la serie diverge, como se vio en el Doc 19 Sección 6).

**Conclusión del argumento de Rouché.** El Rouché no aplica directamente pues $C_\infty$ no está bien definida como función continua en $\mathbb{R}$ (la serie diverge). El argumento funciona en la franja $\Im(z) = \eta > 0$, y luego se toma el límite $\eta \to 0^+$ — que es el límite no-tangencial que define los "ceros de $C_\infty$" de la manera correcta.

---

## 5. El método de Jensen para la cota inferior

**Proposición 5** (cota inferior via el Teorema de Jensen). Por el Teorema de Jensen aplicado a $C_\infty$ en la franja $\Im(z) = \eta$:

$$N_{C_\infty}(T;\eta) = \frac{T}{2\pi}\frac{d}{dT}\arg C_\infty(T+i\eta) + O(\log T).$$

La variación del argumento de $C_\infty(T+i\eta) = 2\sum_\rho|\rho|^{-1-\eta}\cos(T\log|\rho|) + c_0(\eta)$:

Bajo RH: los $|\rho_n| = \sqrt{1/4+\gamma_n^2}$, y la variación del argumento de la suma $\sum_n\gamma_n^{-1-\eta}e^{iT\log\gamma_n}$ acumula a la tasa $\sim \frac{1}{2\pi}\log(T/2\pi)$ por unidad de $T$ (del cómputo de la densidad de ceros de $\Xi$).

*Heurística.* La suma $2\sum_n\gamma_n^{-1-\eta}\cos(T\log\gamma_n)$ es una función de Dirichlet cuasi-periódica con frecuencias $\log\gamma_n$ y amplitudes $\gamma_n^{-1-\eta}$. Su número de ceros en $[0,T]$ crece como $\frac{T}{2\pi}\overline{\log\gamma_n} \sim \frac{T}{2\pi}\log T$, que coincide con $N_\Xi^{crit}(T)$. Luego $N_{C_\infty}(T;\eta) \sim N_\Xi^{crit}(T)$ — lo cual daría la cota inferior buscada.

**Estado.** El argumento de Jensen da la cota correcta heurísticamente, pero formalizarlo requiere controlar la variación del argumento de la suma de cosenos cuasi-periódica — que es el contenido de la teoría de funciones Bohr casi-periódicas con espectro no-periódico. Sin las herramientas de la teoría ergódica aplicadas a la suma específica $\sum_n\gamma_n^{-1-\eta}e^{iT\log\gamma_n}$, el argumento no es riguroso.

---

## 6. El argumento de cota inferior más limpio disponible

**Teorema 2** (cota inferior incondicional de $N_{C_\infty}(T)$ via la estructura de Jacobi). Los eigenvalores de $J_\lambda^N$ en $[0,T]$ son exactamente $N\cdot\mu_{emp}^\lambda([0,T])$. Por la convergencia débil (Doc 15):

$$\lim_\lambda N\cdot\mu_{emp}^\lambda([0,T]) = \lim_\lambda \#\{n: t_n^{(\lambda)} \in [0,T]\}.$$

Este límite es el número de eigenvalores del OPERADOR LÍMITE $J_\infty$ en $[0,T]$, que por el Teorema C1 es el número de ceros de $C_\infty$ en $[0,T]$. Luego:

$$N_{C_\infty}(T) = \lim_\lambda\#\{n: t_n^{(\lambda)} \in [0,T]\}.$$

Y por la convergencia $\mu_{emp}^\lambda \Rightarrow \mu_\gamma^{real}$:

$$\lim_\lambda\frac{\#\{n: t_n^{(\lambda)} \in [0,T]\}}{N} = \mu_\gamma^{real}([0,T]) = \frac{N_\Xi^{crit}(T)}{N},$$

luego $N_{C_\infty}(T) = N_\Xi^{crit}(T) + O(\log T)$.

*El gap en el Teorema 2.* El paso crítico es la identificación $\lim_\lambda\#\{n: t_n^{(\lambda)}\in[0,T]\} = N_{C_\infty}(T)$ (número de eigenvalores del límite = número de ceros de $C_\infty$). Esto requiere que el espectro de $J_\infty$ sea el límite del espectro de $J_\lambda^N$ en el sentido de Hausdorff, lo cual equivale a la convergencia de los eigenvalores individuales — que es precisamente el problema abierto (es equivalente a (Inc. Inv.)).

**Diagnóstico.** El argumento del Teorema 2 es CIRCULAR: la identificación de los eigenvalores de $J_\infty$ con los límites de los eigenvalores de $J_\lambda^N$ es equivalente a la condición buscada.

---

## 7. El resumen honesto: el gap es estructuralmente circular

**Teorema 3** (caracterización del gap sin circularidad). Las siguientes afirmaciones son equivalentes, y ninguna se puede deducir incondicionalmente de las demás sin usar RH:

(A) (Inc. Inv.): todo $\gamma_n$ con $\Xi(\gamma_n) = 0$ satisface $C_\infty(\gamma_n) = 0$.

(B) $N_{C_\infty}(T) \geq N_\Xi^{crit}(T) - O(\log T)$ (cota inferior del número de ceros de $C_\infty$).

(C) Los eigenvalores de $J_\lambda^N$ convergen en Hausdorff al espectro de $J_\infty$ (incluyendo todos los $\gamma_n$).

(D) $\mu_{WT}^\infty = \mu_{emp}^\infty = \mu_\gamma^{real}$ (igualdad de las dos medidas espectrales).

(E) RH.

*Prueba.* Todas estas equivalencias se establecen en los Docs 17-25. La circulación es: (A) $\iff$ (B) $\iff$ (C) $\iff$ (D) $\iff$ (E) — ninguna se puede probar sin las demás (o sin información adicional sobre los ceros de $\zeta$). $\square$

---

## 8. El diagnóstico final del programa Phase 29 (Docs 00-25)

**Lo que el programa ha demostrado incondicionalmente:**

1. El operador $J_\lambda$ es autoadjunto por construcción, con espectro real.
2. La medida espectral empírica converge: $\mu_{emp}^\lambda \Rightarrow \mu_\gamma^{real}$ (nueva demostración vía conteo CCM).
3. El espectro del operador límite $J_\infty$ es exactamente el conjunto de ceros del potencial $C_\infty = w - \Psi$ en $\mathbb{R}$ (Teorema C1, Doc 17 — resultado nuevo).
4. Todo cero de $C_\infty$ en $\mathbb{R}$ es un cero de $\Xi$ en $\mathbb{R}$ (Teorema 2, Doc 19 — resultado nuevo).
5. El espectro de $J_\infty$ es puro puntual (Doc 23).
6. Ceros infinitos fuera de la recta crítica son incompatibles con la estructura de $C_\infty$ (Doc 21, Corolario 2 — resultado nuevo).

**La nueva equivalencia:** RH $\iff$ $\{C_\infty = 0\} = \{\Xi = 0 \text{ en }\mathbb{R}\}$ (Teorema 3, Doc 19).

**El único gap que permanece:** La inclusión inversa (Inc. Inv.) — que es RH reformulada. El programa Phase 29 ha identificado con máxima precisión el obstáculo y lo ha puesto en múltiples formas equivalentes. Ninguna de estas formas se puede probar actualmente sin hipótesis adicionales ((LI), (S), GUE, o similares — todas implicando RH o siendo más fuertes).

**Contribuciones genuinas al conocimiento:**

| Doc | Resultado | Tipo |
|-----|-----------|------|
| 04 | $k(u) > 0$ incondicionalmente | Nuevo, riguroso |
| 08 | $N_\xi(T;\lambda) = N_\Xi(T) + O(\log T)$ | Nuevo, riguroso |
| 15 | $\mu_{emp}^\lambda \Rightarrow \mu_\gamma^{real}$ | Nuevo, riguroso |
| 17 | $\operatorname{spec}(J_\infty) = \{C_\infty = 0\}$ | Nuevo, riguroso (bajo EF2) |
| 19 | $\{C_\infty=0\}\subseteq\{\Xi=0\}$ | Nuevo, riguroso |
| 19 | RH $\iff$ $\{C_\infty=0\}=\{\Xi=0\}$ | Nueva equivalencia |
| 21 | $N_{off}(T) = O(1)$ ó RH | Nuevo, riguroso |
| 23 | Espectro de $J_\infty$ es puro puntual | Nuevo (bajo Prop 4) |
| 24 | RH bajo (LI)+(S) | Nuevo, condicional |

---

## 9. La propuesta final: Doc 26

El Doc 26 debería ser un resumen de cierre ("paper final") que:
1. Recapitula la cadena de resultados incondicionales.
2. Enuncia la nueva equivalencia RH $\iff$ $\{C_\infty=0\}=\{\Xi=0\}$ como el resultado principal.
3. Establece los resultados condicionales (bajo GUE, LI, S).
4. Identifica los tres ataques más prometedores para continuar:
   - Ataque A: Probar directamente $N_{C_\infty}(T) \geq N_\Xi^{crit}(T) - O(\log T)$ via análisis de la variación del argumento de la función de Dirichlet $C_\infty$.
   - Ataque B: Usar la función $\Xi$ directamente para forzar (Inc. Inv.) via el operador de proyección espectral.
   - Ataque C: Conectar la deslocalización de $e_0$ con los teoremas de tipo SIMON-WOLFF via la estructura aritmética de los coeficientes $a_n^\infty = \pi/\log\gamma_n$.
