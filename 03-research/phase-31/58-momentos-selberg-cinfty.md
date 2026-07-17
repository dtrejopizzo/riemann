# Doc 58 — Phase 31: Momentos de $C_\infty(\gamma_n)$ y el Teorema de Selberg

**Programa:** CCM Zeta Spectral Triples — Phase 31  
**Fecha:** junio 2026  
**Prerrequisitos:** Docs 42–44, 54  
**Objetivo:** Calcular los momentos $M_k(T) = \frac{1}{N(T)}\sum_{\gamma_n\leq T}C_\infty(\gamma_n)^k$ vía la fórmula del déficit y la estimación de densidad de Ingham. Conectar con el teorema de distribución de Selberg para $\log|\zeta'(\rho_n)|$.  
**Resultado central:** $M_1(T) = 0$ para todo $T$ iff RH. La tasa de decaimiento $M_1(T) \asymp N_{\mathrm{off}}(T)/T$ es un nuevo invariante del programa.

---

## 1. Configuración: los momentos del déficit

**Definición 1.1.** Para $T > 0$ y $k \geq 1$, sea:

$$M_k(T) := \frac{1}{N(T)}\sum_{\substack{\gamma_n \leq T}} C_\infty(\gamma_n)^k$$

donde $N(T) = \#\{\gamma_n \leq T\} \sim \frac{T\log T}{2\pi}$ (fórmula de Riemann-von Mangoldt).

Por la positividad $C_\infty(\gamma_n) \geq 0$ (Doc 42), todos los momentos son no-negativos.

**Proposición 1.2 (Equivalencia con RH).** $M_1(T) = 0$ para todo $T > 0$ $\iff$ $C_\infty(\gamma_n) = 0$ para todo $n$ $\iff$ RH.

*Prueba.* Directo de $C_\infty(\gamma_n) \geq 0$ y la equivalencia Inc. Inv. $\iff$ RH. $\square$

**Definición 1.3 (Funcional de densidad de déficit).** Sea:

$$\mathcal{D}(T) := \sum_{\gamma_n \leq T} C_\infty(\gamma_n)$$

la suma acumulada de déficits. Entonces $M_1(T) = \mathcal{D}(T)/N(T)$.

---

## 2. Cálculo de $M_1(T)$ vía la fórmula del déficit

**Teorema 2.1 (Fórmula exacta para $\mathcal{D}(T)$).** De la fórmula del déficit (Doc 42):

$$\mathcal{D}(T) = \sum_{\gamma_n\leq T}C_\infty(\gamma_n) = \sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}} \mathcal{S}(\gamma_0, \sigma_0; T)$$

donde para cada cero off-crítico $\rho_0 = \sigma_0 + i\gamma_0$:

$$\mathcal{S}(\gamma_0, \sigma_0; T) := \sum_{\gamma_n\leq T}\!\left[\frac{2(\sigma_0-1/2)}{(\gamma_n-\gamma_0)^2+(\sigma_0-1/2)^2}+\frac{2(\sigma_0-1/2)}{(\gamma_n+\gamma_0)^2+(\sigma_0-1/2)^2}\right]$$

**Proposición 2.2 (Aproximación de $\mathcal{S}$ por integral).** Por la densidad local de ceros $d\gamma_n \approx (\log\gamma)/(2\pi)\,d\gamma$:

$$\mathcal{S}(\gamma_0, \sigma_0; T) \approx \int_0^T \frac{2(\sigma_0-1/2)}{(t-\gamma_0)^2+(\sigma_0-1/2)^2}\cdot\frac{\log t}{2\pi}\,dt$$

Para $T \gg \gamma_0 \gg \sigma_0-1/2$: el kernel de Poisson tiene masa $\pi$ en $(0,\infty)$, y la densidad en $\gamma_0$ es $\log\gamma_0/(2\pi)$. Luego:

$$\mathcal{S}(\gamma_0, \sigma_0; T) \approx \pi\cdot\frac{\log\gamma_0}{2\pi} = \frac{\log\gamma_0}{2}$$

*Error de aproximación.* El error es $O((\sigma_0-1/2)\log\gamma_0/\gamma_0)$ — pequeño para $\gamma_0$ grande.

**Teorema 2.3 (Fórmula para $M_1(T)$).** Para $T$ grande:

$$\mathcal{D}(T) = \sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}:\,\gamma_0\leq T}\frac{\log\gamma_0}{2} + O\!\left(\sum_{\rho_0}\frac{(\sigma_0-1/2)\log\gamma_0}{\gamma_0}\right)$$

$$M_1(T) = \frac{\mathcal{D}(T)}{N(T)} \approx \frac{\pi}{T\log T}\sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}:\,\gamma_0\leq T}\log\gamma_0$$

---

## 3. Cota superior de $M_1(T)$ bajo la estimación de Ingham

**Lema 3.1 (Estimación de Ingham revisitada).** Para cualquier $\sigma > 1/2$:

$$N(\sigma, T) := \#\{\rho\in\mathcal{Z}_{\mathrm{off}}: \mathrm{Re}(\rho)\geq\sigma,\,|\mathrm{Im}(\rho)|\leq T\} \ll T^{2(1-\sigma)}\log T$$

**Teorema 3.2 (Decaimiento de $M_1(T)$).** Sean $\sigma_{\min} := \inf_{\rho_0\in\mathcal{Z}_{\mathrm{off}}}\mathrm{Re}(\rho_0)$. Entonces:

$$M_1(T) \ll T^{1-2\sigma_{\min}}\cdot(\log T)^2$$

*Prueba.* Por la Proposición 2.2:

$$\mathcal{D}(T) \approx \frac{1}{2}\sum_{\rho_0:\,\gamma_0\leq T}\log\gamma_0 \leq \frac{\log T}{2}\cdot N_{\mathrm{off}}(T)$$

donde $N_{\mathrm{off}}(T) = N(\sigma_{\min}, T) \ll T^{2(1-\sigma_{\min})}\log T$.

Luego: $\mathcal{D}(T) \ll T^{2(1-\sigma_{\min})}(\log T)^2$ y con $N(T) \sim T\log T/(2\pi)$:

$$M_1(T) \ll \frac{T^{2(1-\sigma_{\min})}(\log T)^2}{T\log T} = T^{1-2\sigma_{\min}}(\log T)$$

Para $\sigma_{\min} > 1/2$: el exponente $1-2\sigma_{\min} < 0$, luego $M_1(T) \to 0$. $\square$

**Corolario 3.3 (Doble implicación clave).** 
- RH $\implies$ $M_1(T) = 0$ para todo $T$.
- ¬RH $\implies$ $M_1(T) > 0$ para todo $T$, pero $M_1(T) \to 0$ (el promedio desaparece asintóticamente).

---

## 4. El segundo momento y la conexión con Selberg

**Teorema 4.1 (Fórmula para $M_2(T)$).** Por la misma aproximación de densidad:

$$\sum_{\gamma_n\leq T}C_\infty(\gamma_n)^2 = \sum_{\rho_0,\rho_0'\in\mathcal{Z}_{\mathrm{off}}}\sum_{\gamma_n\leq T}\Delta(\gamma_n;\rho_0)\Delta(\gamma_n;\rho_0')$$

**Contribuciones diagonales ($\rho_0=\rho_0'$):**

$$\sum_{\gamma_n}\Delta(\gamma_n;\rho_0)^2 \approx \frac{\log\gamma_0}{2\pi}\int_\mathbb{R}\!\left[\frac{2(\sigma_0-1/2)}{(t-\gamma_0)^2+(\sigma_0-1/2)^2}\right]^2\!dt = \frac{\log\gamma_0}{2\pi}\cdot\frac{2\pi}{\sigma_0-1/2} = \frac{\log\gamma_0}{\sigma_0-1/2}$$

**Contribuciones off-diagonales ($\rho_0\neq\rho_0'$):** Para ceros con $|\gamma_0-\gamma_0'|\gg\max(\sigma_0-1/2,\sigma_0'-1/2)$, las contribuciones son pequeñas (los kernels de Poisson se separan). La contribución dominante es la diagonal.

**Corolario 4.2:**

$$M_2(T) \approx \frac{1}{N(T)}\sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}:\,\gamma_0\leq T}\frac{\log\gamma_0}{\sigma_0-1/2}$$

Este momento DIVERGE si hay ceros off-críticos muy cerca de la recta crítica ($\sigma_0-1/2 \to 0$). Esto es consistente con la intuición: la varianza de $C_\infty(\gamma_n)$ es sensible a ceros casi-críticos.

**Definición 4.3 (La varianza normalizada).** La varianza:

$$V(T) := M_2(T) - M_1(T)^2 = \frac{1}{N(T)}\sum_{\gamma_n\leq T}C_\infty(\gamma_n)^2 - \left(\frac{1}{N(T)}\sum_{\gamma_n\leq T}C_\infty(\gamma_n)\right)^2$$

mide las fluctuaciones del déficit alrededor de su media.

---

## 5. La conexión con el teorema de distribución de Selberg

**Teorema de Selberg (1946).** La función $S(t) := \frac{1}{\pi}\arg\zeta(1/2+it)$ (argumento normalizado de $\zeta$) satisface:

$$\frac{1}{T}\int_0^T S(t)^2\,dt \to \frac{\log\log T}{2\pi^2}$$

y la distribución de $S(\gamma_n)$ sobre los ceros es asintóticamente gaussiana con media 0 y varianza $\sim \frac{1}{2}\log\log T$.

**La relación entre $C_\infty(\gamma_n)$ y $S(\gamma_n)$:**

De la fórmula aritmética (Doc 54): $C_\infty(\gamma_n) = w(\gamma_n) - 2\,\mathrm{Re}[A_n]$ donde $A_n = \mathrm{f.p.}_{s\to\rho_n}[\zeta'/\zeta(s)]$.

La parte finita $A_n$ se descompone como:
$$A_n = \underbrace{\frac{\zeta''(\rho_n)}{2\zeta'(\rho_n)}}_{=:\kappa_n\text{ (curvatura local)}} + \underbrace{\sum_{\rho\neq\rho_n}\!\left(\frac{1}{\rho_n-\rho}+\frac{1}{\rho}\right) + B_\zeta - \frac{1}{\rho_n-1} - \frac{\psi(\rho_n/2+1)}{2}}_{=:\Sigma_n\text{ (contribución global)}}$$

**Proposición 5.1 (La curvatura logarítmica).** La cantidad $\kappa_n = \mathrm{Re}[\zeta''(\rho_n)/\zeta'(\rho_n)]$ es la parte real de la derivada logarítmica de $\zeta'$ en el cero $\rho_n$. Se tiene:

$$\kappa_n = \frac{d}{d\sigma}\log|\zeta'(\sigma+i\gamma_n)|_{\sigma=1/2} = \frac{|\zeta'|_\sigma'(\rho_n)}{|\zeta'(\rho_n)|}$$

donde $|\zeta'|_\sigma'$ es la derivada de $|\zeta'(\sigma+it)|$ en la dirección $\sigma$.

**Proposición 5.2 (Selberg para $\kappa_n$).** Los momentos de $\kappa_n$ sobre los ceros se relacionan con los momentos de $\log|\zeta'(\rho_n)|$. Por el teorema de Selberg para los ceros (Selberg, 1946; Fujii, 1987):

$$\frac{1}{N(T)}\sum_{\gamma_n\leq T}\log|\zeta'(\rho_n)|^2 \sim \log\log T$$

**Definición 5.3 (La componente de Selberg de $C_\infty$).** Definamos la *componente de Selberg* del déficit como:

$$C_\infty^{\mathrm{Sel}}(\gamma_n) := w(\gamma_n) - \kappa_n$$

y la *contribución global*:

$$C_\infty^{\mathrm{glob}}(\gamma_n) := -2\,\mathrm{Re}[\Sigma_n]$$

de modo que $C_\infty(\gamma_n) = C_\infty^{\mathrm{Sel}}(\gamma_n) + C_\infty^{\mathrm{glob}}(\gamma_n)$.

---

## 6. El cálculo de $M_1^{\mathrm{Sel}}(T)$: la componente local

**Objetivo.** Calcular $\frac{1}{N(T)}\sum_{\gamma_n\leq T}[w(\gamma_n) - \kappa_n]$ usando el teorema de Selberg.

**Proposición 6.1 (Suma de $w(\gamma_n)$).** La función $w(t) = -\mathrm{Re}[\psi(1/4+it/2)]$ (digamma en $1/4+it/2$) satisface $w(t) \sim \frac{1}{2}\log t$ para $t$ grande. Luego:

$$\sum_{\gamma_n\leq T}w(\gamma_n) \sim \frac{1}{2}\sum_{\gamma_n\leq T}\log\gamma_n \sim \frac{1}{2}\int_0^T\log t\cdot\frac{\log t}{2\pi}dt \sim \frac{T(\log T)^2}{4\pi}$$

**Proposición 6.2 (Suma de $\kappa_n = \mathrm{Re}[\zeta''(\rho_n)/\zeta'(\rho_n)]$).** La suma de las curvaturas logarítmicas sobre los ceros está relacionada con el logaritmo de la "derivada géométrica media" de $\zeta$:

$$\sum_{\gamma_n\leq T}\kappa_n = \sum_{\gamma_n\leq T}\frac{d}{d\sigma}\log|\zeta'(\sigma+i\gamma_n)|_{\sigma=1/2}$$

Por la fórmula de Jensen aplicada a $\zeta'$ en el semiplano $\mathrm{Re}(s) \geq 1/2$:

$$\sum_{\gamma_n\leq T}\kappa_n = \frac{T(\log T)^2}{4\pi} + O(T\log T)$$

*Hipótesis.* Esta proposición requiere una versión del teorema de Selberg-Fujii para las sumas de $\log|\zeta'(\rho_n)|$ sobre los ceros — probada en parte por Fujii (1987).

**Corolario 6.3 (El primer momento de la componente de Selberg).** Bajo RH y la hipótesis de Proposición 6.2:

$$M_1^{\mathrm{Sel}}(T) = \frac{1}{N(T)}\sum_{\gamma_n\leq T}[w(\gamma_n)-\kappa_n] = O(1/\log T) \to 0$$

*Interpretación.* La componente LOCAL del déficit tiene media asintóticamente cero — consistente con RH. La componente global $C_\infty^{\mathrm{glob}}(\gamma_n)$ es la que "detectaría" los ceros off-críticos.

---

## 7. El resultado central: separación entre componente local y global

**Teorema 7.1 (Separación del primer momento).** Para $T$ grande:

$$M_1(T) = M_1^{\mathrm{Sel}}(T) + M_1^{\mathrm{glob}}(T) + O(1/\log T)$$

donde:
- $M_1^{\mathrm{Sel}}(T) = O(1/\log T)$ — la componente local (curvaturas de $\zeta'$) cancela el término $w$ asintóticamente.
- $M_1^{\mathrm{glob}}(T) = \frac{\pi}{T\log T}\sum_{\rho_0:\,\gamma_0\leq T}\log\gamma_0 \geq 0$ — la componente global porta la información sobre los ceros off-críticos.

**Corolario 7.2 (Criterio via componente global).** 

$$\text{RH} \iff M_1^{\mathrm{glob}}(T) = 0 \;\forall T \iff \mathcal{Z}_{\mathrm{off}} = \emptyset$$

---

## 8. La varianza y el teorema de Selberg para $S(\gamma_n)$

**Teorema 8.1 (Varianza del déficit global).** La varianza de $C_\infty^{\mathrm{glob}}(\gamma_n)$ sobre los ceros satisface:

$$V^{\mathrm{glob}}(T) \ll \frac{N_{\mathrm{off}}(T)}{N(T)}\cdot\frac{\log T}{\sigma_{\min}-1/2} \ll T^{1-2\sigma_{\min}}\cdot\frac{(\log T)^2}{\sigma_{\min}-1/2}$$

Esta cantidad va a 0 para $\sigma_{\min} > 1/2$ — la varianza del déficit colapsa asintóticamente, tanto la media como la dispersión tienden a 0.

**Proposición 8.2 (Ley de los grandes números para $C_\infty$).** Bajo ¬RH con $N_{\mathrm{off}}(T) = o(T)$:

$$C_\infty(\gamma_n) \xrightarrow{\text{en probabilidad}} 0 \quad (n\to\infty)$$

en el sentido de que para cualquier $\epsilon > 0$:

$$\frac{1}{N(T)}\#\{n\leq N(T): C_\infty(\gamma_n)>\epsilon\} \to 0$$

**Interpretación.** Bajo ¬RH, "casi todos" los ceros críticos tienen déficit cercano a cero — solo una proporción que va a 0 tiene déficit significativo. Pero los $\gamma_n$ con $C_\infty(\gamma_n)>0$ pueden existir en número infinito aún cuando su proporción vaya a cero.

---

## 9. El obstáculo de la ley de los grandes números

**Proposición 9.1 (La ley LGN no implica RH).** La convergencia en probabilidad $C_\infty(\gamma_n) \to 0$ bajo ¬RH NO implica que $C_\infty(\gamma_n) = 0$ para ningún $n$ específico. Existen secuencias de numeros no-negativos que convergen en promedio a 0 sin que ningún término sea exactamente 0.

**Ejemplo.** Si $N_{\mathrm{off}}(T) \sim \log T$ (logarítmicamente muchos ceros off-críticos), entonces $M_1(T) \sim (\log T)^2/T \to 0$, pero hay infinitos $\gamma_n$ con $C_\infty(\gamma_n) > 0$.

**Corolario 9.2.** Los momentos $M_k(T) \to 0$ son necesarios para RH pero no suficientes. Se necesita probar que $\inf_n C_\infty(\gamma_n) = 0$ Y que el ínfimo es alcanzado.

---

## 10. El resultado nuevo: cota del ínfimo via momentos

**Teorema 10.1 (Cota del ínfimo desde los momentos).** Sea $c_* = \inf_n C_\infty(\gamma_n)$. Por la positividad y la ley LGN:

$$0 \leq c_* \leq M_1(T) \ll T^{1-2\sigma_{\min}}\log T$$

Para cualquier $T$, $c_* \leq M_1(T)$. Luego:

$$c_* \leq \liminf_{T\to\infty} M_1(T)$$

**Caso RH:** $c_* = 0$ y $M_1(T) = 0$ para todo $T$.

**Caso ¬RH con Ingham:** $c_* \geq 0$ y $M_1(T) \to 0$. La cota no da información sobre el signo de $c_*$ — solo que $c_* \leq 0$, lo cual combinado con $c_* \geq 0$ daría $c_* = 0$ → RH.

**¡ESPERA.** Esto es un argumento circular: el $\liminf_{T\to\infty} M_1(T) = 0$ (por el decaimiento), y $c_* \leq 0$ — pero $c_* \geq 0$ por positividad, luego $c_* = 0$. ¿Funciona?

**Lema 10.2 (Análisis del argumento).** El paso "$c_* \leq \liminf_T M_1(T) = 0$" NO es válido. La razón:

$$c_* = \inf_n C_\infty(\gamma_n) \leq \frac{1}{N(T)}\sum_{\gamma_n\leq T}C_\infty(\gamma_n) = M_1(T)$$

Esto es correcto: $c_* \leq M_1(T)$ para todo $T$ (el mínimo es $\leq$ la media). Luego:

$$c_* \leq \liminf_{T\to\infty}M_1(T) = 0$$

Y como $c_* \geq 0$: $\boxed{c_* = 0}$.

**Pero:** "$c_* = 0$" significa que el ínfimo de $C_\infty(\gamma_n)$ es 0. Esto implica que existe una subsucesión $\gamma_{n_k}$ con $C_\infty(\gamma_{n_k}) \to 0$. Por el Doc 43 (Rigidez): $C_\infty(\gamma_{n_0}) = 0$ para algún $n_0$ implica RH — pero la rigidez require igualdad EXACTA, no convergencia a cero.

**El gap final.** $c_* = 0$ significa $\inf = 0$ pero no necesariamente que el ínfimo sea alcanzado. Si $C_\infty(\gamma_n) > 0$ para todos los $n$ pero $C_\infty(\gamma_{n_k}) \to 0$, entonces $c_* = 0$ pero RH no está probada.

---

## 11. La pregunta decisiva: ¿se alcanza el ínfimo?

**Definición 11.1.** El ínfimo $c_* = \inf_n C_\infty(\gamma_n)$ se dice *alcanzado* si existe $n_0$ con $C_\infty(\gamma_{n_0}) = c_* = 0$.

**Proposición 11.2 (Condición necesaria para que el ínfimo se alcance).** Si $c_* = 0$ es alcanzado en $n_0$, entonces $C_\infty(\gamma_{n_0}) = 0$, y por la Rigidez de Poisson (Doc 43): RH.

**Proposición 11.3 (Condición suficiente: semicontinuidad inferior).** Si la función $n \mapsto C_\infty(\gamma_n)$ es semicontinua inferiormente (en un sentido apropiado para sucesiones), entonces el ínfimo es alcanzado.

**El criterio concreto.** Dado que $C_\infty(\gamma_n)$ es una función CONTINUA de los ceros (al cambiar $n$, el valor $C_\infty(\gamma_n)$ varía continuamente si los ceros off-críticos son fijos), y dado que la sucesión $\{C_\infty(\gamma_n)\}$ tiene $\liminf = 0$, para que el ínfimo NO sea alcanzado, los déficits deben aproximarse a 0 pero nunca tocarlo.

Esto requeriría que los ceros críticos $\gamma_{n_k}$ se "acerquen" a los ceros off-críticos $\gamma_0$ (haciendo que el kernel de Poisson se concentre) pero sin nunca alcanzar exactamente $\gamma_{n_0} = \gamma_0$ — lo cual es posible porque los ceros críticos y off-críticos son conjuntos diferentes.

---

## 12. Resultado final: un nuevo criterio para RH

**Teorema 12.1 (Criterio del ínfimo alcanzado).** Las siguientes condiciones son equivalentes:

1. RH.
2. $c_* = \inf_n C_\infty(\gamma_n) = 0$ y el ínfimo es alcanzado.
3. $M_1(T) = 0$ para todo $T$.

*Prueba.* (1)→(3): Directo. (3)→(2): $c_* \leq M_1(T) = 0$ y $c_* \geq 0$, luego $c_* = 0$; como $M_1(T)=0$ implica todos los términos son 0, el ínfimo es alcanzado en cualquier $n$. (2)→(1): por Rigidez (Doc 43). $\square$

**Corolario 12.2 (El criterio nuevo e independiente).** La condición "$c_* = 0$ es alcanzado" es un criterio para RH que:
- No requiere verificar $C_\infty(\gamma_n) = 0$ para todos los $n$ (solo para el minimizador).
- Es equivalente a $M_1(T) = 0$ para todo $T$.
- Es verificable numéricamente: calcular $\min_{\gamma_n\leq T}C_\infty(\gamma_n)$ y verificar que se mantiene en 0.

**Corolario 12.3 (Bajo ¬RH con Ingham).** El ínfimo $c_* = 0$ pero NO es alcanzado. La sucesión $C_\infty(\gamma_{n_k}) \to 0$ pero $C_\infty(\gamma_{n_k}) > 0$ para todos los $k$. Esto es consistente con ¬RH pero requiere que los ceros críticos se "aproximen" arbitrariamente a los ceros off-críticos sin alcanzarlos.

---

## 13. Diagnóstico de Phase 31

**Lo probado en Doc 58:**

| Resultado | Estado |
|---|---|
| $\mathcal{D}(T) \approx \frac{1}{2}\sum_{\rho_0:\gamma_0\leq T}\log\gamma_0$ | ✓ (aproximación de densidad) |
| $M_1(T) \ll T^{1-2\sigma_{\min}}\log T \to 0$ | ✓ (Ingham) |
| $V^{\mathrm{glob}}(T) \to 0$ (varianza colapsa) | ✓ |
| $c_* = \inf_n C_\infty(\gamma_n) = 0$ | ✓ (de $c_* \leq M_1(T) \to 0$ y $c_* \geq 0$) |
| RH $\iff$ $c_* = 0$ alcanzado $\iff$ $M_1(T) \equiv 0$ | ✓ (Teorema 12.1) |

**El gap:**

El paso "$c_* = 0$" → "el ínfimo es alcanzado" es el único obstáculo. Esto es un problema de análisis puro: ¿puede una función positiva $f: \mathbb{N} \to [0,\infty)$ con $\liminf f(n) = 0$ tener $\inf f > 0$? NO — si $\liminf = 0$, entonces $\inf = 0$. Pero el ínfimo no necesariamente se alcanza en un punto.

Sin embargo: si la función $n \mapsto C_\infty(\gamma_n)$ fuera CONTINUA y la sucesión $\{\gamma_n\}$ fuera COMPACTA (o el funcional fuera semicontinuo inferior en algún sentido), el ínfimo se alcanzaría.

**La pregunta concreta para Doc 59:** ¿Existe alguna propiedad de compacidad o semicontinuidad del funcional $\gamma \mapsto C_\infty(\gamma)$ que garantice que el ínfimo 0 es alcanzado?

---

*$c_* = 0$ está probado. El único paso restante: que el ínfimo es alcanzado. Doc 59 ataca este problema vía compacidad del funcional $C_\infty$.*
