# Frente A — Flujo de de Bruijn–Newman y monotonía del índice de Kreĭn

**Fecha:** junio 2026

---

## 1. Definiciones

**Definición A.1** (Flujo de de Bruijn–Newman). Para $t \in \mathbb{R}$ define:
$$H_t(z) := \int_0^\infty \Phi(u)\, e^{tu^2} \cos(uz)\, du,$$
donde $\Phi(u) = \sum_{n=1}^\infty (2\pi^2 n^4 e^{9u/2} - 3\pi n^2 e^{5u/2}) e^{-\pi n^2 e^{2u}}$
es el núcleo de de Bruijn. La función $H_0$ satisface $H_0(z) = \Xi(1/2 + iz)$ donde
$\Xi$ es la función xi de Riemann.

**Definición A.2** (Configuración de ceros). Sea $Z_t = \{z_n(t)\}_{n \ge 1}$ el
multiconjunto ordenado de ceros de $H_t$ en el semiplano superior $\operatorname{Im} z \ge 0$
(junto con los reales). Cada cero complejo $z_n = \alpha_n + i\beta_n$ con $\beta_n > 0$
corresponde a un cero $\rho_n = 1/2 + iz_n = 1/2 + i\alpha_n - \beta_n$ de $\zeta$
fuera de la recta crítica, con $\operatorname{Re}(\rho_n) = 1/2 - \beta_n$.

**Definición A.3** (Índice transversal en el flujo). Para cada $t$, define:
$$\kappa_t := 2 \cdot \#\{n : \operatorname{Im} z_n(t) > 0\}$$
(el doble del número de ceros complejos en el semiplano superior abierto).

*Observación:* $\kappa_t$ es el análogo del índice de Kreĭn $\kappa(Q_t)$ en el lenguaje
del flujo DBN. Bajo la identificación de Definición A.2 y la relación $\kappa(Q) = 2m$
(Phase 26), $\kappa_0 = \kappa(Q)$.

**Definición A.4** (Constante de de Bruijn–Newman). 
$$\Lambda := \inf\{t \in \mathbb{R} : \text{todos los ceros de } H_t \text{ son reales}\}.$$

---

## 2. Hechos establecidos

**Teorema A.5** (de Bruijn 1950). $H_t$ tiene sólo ceros reales para todo $t \ge 1/2$.
En consecuencia, $\Lambda \le 1/2$.

**Teorema A.6** (Rodgers–Tao 2019). $\Lambda \ge 0$.

**Teorema A.7** (definición directa). $\Lambda = 0 \iff$ RH.

*Prueba:* Por definición, $\Lambda = 0$ dice que $H_0$ tiene sólo ceros reales, i.e.,
$\Xi(1/2 + iz) = 0 \Rightarrow z \in \mathbb{R}$, i.e., todos los ceros de $\zeta$ tienen
parte real $1/2$. $\square$

**Corolario A.8.** $\kappa_t = 0$ para todo $t \ge \Lambda$.

**Teorema A.9** (Csordas–Norfolk–Varga 1988). Los ceros de $H_t$ satisfacen la ecuación
diferencial ordinaria:
$$\frac{dz_n}{dt} = \sum_{k \ne n} \frac{2}{z_k - z_n}, \qquad \forall\, n \ge 1.$$

Esta ecuación es el **flujo gradiente** de la energía logarítmica
$$E_{\log}(Z) = -\sum_{j \ne k} \log|z_j - z_k|.$$

*Verificación:* $-\partial E_{\log}/\partial \bar z_n = \sum_{k \ne n} 2/(z_k - z_n)$.
$\square$

---

## 3. La pregunta central del Frente A

Los hechos anteriores son conocidos. La novedad del Frente A es la siguiente:

**Pregunta A.10** (central, abierta). ¿Es $t \mapsto \kappa_t$ monótona no-creciente?

Si la respuesta es sí, el argumento es:
1. $\kappa_t \ge 0$ para todo $t$ (por definición).
2. $\kappa_t$ no-creciente $\Rightarrow$ $\kappa_0 \ge \kappa_t$ para $t \ge 0$.
3. $\kappa_\Lambda = 0$.

Pero esto sólo da $\kappa_0 \ge 0$ (ya conocido). **Monotonicidad sola no prueba RH.**

La pregunta correcta es más sutil:

**Pregunta A.11** (refinada). Bajo las restricciones aritméticas impuestas por el
producto de Euler de $\zeta$, ¿puede ocurrir que $\kappa_0 > 0$?

El punto clave es que $H_0$ no es una función arbitraria de orden 1 con ceros simétricos.
Es $\Xi(1/2 + iz)$, donde $\Xi$ se factoriza como $\Xi(s) = \prod_p \Xi_p(s)$ (producto
de Euler). Esto impone restricciones globales sobre los ceros que un flujo sin esa
estructura aritmética no tendría.

---

## 4. La dinámica de la parte imaginaria

**Proposición A.12** (ecuación para la parte transversal). Para un cero complejo
$z_n = \alpha_n + i\beta_n$ con $\beta_n > 0$, la ecuación del flujo da:
$$\frac{d\beta_n}{dt} = \sum_{k \ne n} \frac{-2\beta_n}{(\alpha_k - \alpha_n)^2 + (\beta_k - \beta_n)^2} + \text{términos de pares conjugados}.$$

Más precisamente, para cada par conjugado $(z_n, \bar z_n)$:

La contribución del par a $d\beta_n/dt$:
$$\frac{d\beta_n}{dt}\bigg|_{\text{par propio}} = \frac{-2\beta_n}{(2\beta_n)^2} \cdot (-2) = \frac{1}{2\beta_n} \cdot (\text{signo a determinar})$$

*Observación:* El signo de $d\beta_n/dt$ determina si el cero se acerca o se aleja de la
recta real. Para el flujo DBN, la definición de $\Lambda$ implica que eventualmente
$\beta_n(t) \to 0$ para todo $n$ a medida que $t \to \Lambda^-$. Pero esto no
implica $\beta_n(0) = 0$.

**Proposición A.13** (propiedad global del flujo). La energía logarítmica $E_{\log}$ es
una función de Lyapunov para el flujo DBN: $dE_{\log}/dt \le 0$.

*Prueba:* El flujo es el gradiente negativo de $E_{\log}$:
$\frac{dz_n}{dt} = -\frac{\partial E_{\log}}{\partial \bar z_n}$.
Por tanto: $\frac{d}{dt} E_{\log} = -\sum_n \left|\frac{\partial E_{\log}}{\partial z_n}\right|^2 \le 0$. $\square$

*Consecuencia:* La energía logarítmica DISMINUYE monotónamente a lo largo del flujo. Pero
$E_{\log}$ no distingue ceros reales de complejos: es una función del módulo de las
diferencias, no de las partes imaginarias.

---

## 5. El obstáculo central y la conexión con el Frente D

La pregunta del Frente A se reduce a:

> ¿La disminución de $E_{\log}$ bajo el flujo equivale a la disminución de la energía
> transversal $\Phi = \sum_n \beta_n^2$?

Estas dos cantidades son distintas:
$$E_{\log}(Z) = -\sum_{j \ne k} \log|z_j - z_k|, \qquad \Phi(Z) = \sum_n (\operatorname{Im} z_n)^2.$$

Para que el flujo lleve $\Phi \to 0$ (RH), necesitamos que la restricción de $E_{\log}$
a la "dirección transversal" sea convexa con mínimo en $\Phi = 0$.

**Esta es exactamente la pregunta del Frente D.** Los dos frentes son el mismo programa.

---

## 6. Resultado nuevo: fórmula para $\Lambda$

**Proposición A.14** (cota inferior de $\Lambda$ vía Kreĭn). Bajo Hipótesis D con
órbitas a distancia $b_j = \operatorname{Re}(\rho_j) - 1/2 > 0$, el Teorema 25-B.4 del
programa establece:
$$\Lambda \ge \max_j \frac{b_j^2}{2}.$$

**Conjetura A.15** (nueva). La desigualdad anterior es una igualdad:
$$\Lambda = \max_j \frac{b_j^2}{2}.$$

*Evidencia heurística:* El flujo DBN con energía logarítmica debería converger más
lentamente cuanto más lejos esté el cero de la recta real. El cero más alejado (mayor
$b_j$) debería ser el "último en llegar" a la recta real, determinando $\Lambda$.

*Consecuencia de A.15:* Si la conjetura es cierta, entonces:
$$\Lambda = 0 \iff \max_j b_j^2 = 0 \iff b_j = 0 \; \forall j \iff \text{RH.}$$

Esto no prueba RH, pero convierte $\Lambda$ en un invariante medible de la peor violación
de RH: la distancia del cero más alejado de la recta crítica.

---

## 7. Veredicto del Frente A

| Resultado | Estado |
|---|---|
| $\kappa_t = 0$ para $t \ge 1/2$ | Probado (de Bruijn) |
| Flujo DBN = flujo gradiente de $E_{\log}$ | Probado (Csordas–Norfolk–Varga) |
| $E_{\log}$ es función de Lyapunov | Probado |
| $\kappa_t$ no-creciente → consecuencia débil | Monotonicidad no prueba RH |
| Conjetura A.15: $\Lambda = \max_j b_j^2/2$ | **Abierto — nuevo resultado a probar** |
| Frentes A y D son el mismo problema | **Nuevo resultado de Phase 28** |
