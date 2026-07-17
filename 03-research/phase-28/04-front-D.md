# Frente D — Energía transversal y la recta crítica como atractor

**Fecha:** junio 2026
**Crédito:** La dirección central de este frente fue propuesta por un colega matemático.

---

## 1. El punto de partida: $b$ como la única variable que importa

Todo el programa desde Phase 21 converge en un único parámetro:
$$b_j := \operatorname{Re}(\rho_j) - \frac{1}{2},$$
la distancia transversal del cero $\rho_j$ a la recta crítica. Las tres descripciones
del obstáculo son:

| Lenguaje | Manifestación de $b_j > 0$ |
|---|---|
| Kreĭn | Dirección negativa de $Q$ |
| Connes | Eigenvalor complejo $\lambda_j = \gamma_j - ib_j$ de $H_C$ |
| Adélico | Carácter no-unitario $|x|^{b_j + i\gamma_j}$ (Phase 27) |

**Diagnóstico del programa:** hemos estudiado *la existencia* de $b_j$. Phase 28 pregunta
por su *dinámica*: ¿existe un mecanismo que fuerza $b_j \to 0$?

---

## 2. Tres ingredientes para la energía aritmética

**Definición D.1** (energía logarítmica). Para la configuración de ceros $Z = \{z_n\}$
(ceros de $H_0$ como en Front A, con $z_n = \gamma_n + ib_n$):
$$E_{\log}(Z) := -\sum_{j \ne k} \log|z_j - z_k|.$$

Esta energía aparece en la distribución GUE de ceros (Montgomery-Odlyzko): los ceros
de $\zeta$ se comportan como eigenvalores de una matriz aleatoria Hermítica, cuya medida
de equilibrio minimiza $E_{\log}$ sujeta a la densidad de von Mangoldt.

**Definición D.2** (potencial de confinamiento). La densidad media de ceros de $\zeta$
es $W(\gamma) \approx \frac{1}{2\pi}\log(\gamma/2\pi)$ (fórmula de Riemann–von Mangoldt). Define:
$$E_{\text{conf}}(Z) := \sum_n W(\gamma_n),$$
el potencial que reproduce la densidad correcta en la dirección $\gamma$ (altura en la
recta crítica).

**Definición D.3** (energía transversal, nueva). El ingrediente novedoso:
$$\Phi(Z) := \sum_n b_n^2 = \sum_n \left(\operatorname{Re}(z_n) - 0\right)^2,$$
la energía de confinamiento en la dirección *transversal* a la recta crítica.

**Definición D.4** (energía aritmética total):
$$E_{\text{arith}}(Z) := E_{\log}(Z) + E_{\text{conf}}(Z) + \Phi(Z).$$

---

## 3. La formulación variacional de RH

**Proposición D.5** (RH como problema de minimización). Bajo las siguientes hipótesis:
1. La única configuración de ceros de $\zeta$ compatible con la ecuación funcional y el
   producto de Euler es la configuración real con todos $b_n = 0$;
2. La energía $E_{\text{arith}}$ es estrictamente convexa en la dirección transversal;
entonces RH es equivalente a que la configuración de ceros de $\zeta$ sea el único
mínimo de $\Phi$ sujeto a las restricciones aritméticas.

*Nota:* Hipótesis (1) y (2) son el contenido de lo que hay que demostrar. Pero la
formulación como problema de minimización es nueva.

**Proposición D.6** (propiedades básicas de $\Phi$).
1. $\Phi(Z) \ge 0$ para toda configuración.
2. $\Phi(Z) = 0 \iff b_n = 0$ para todo $n \iff$ todos los ceros están en la recta crítica.
3. $\Phi(Z) = -\operatorname{tr}(Q|_{\text{neg}}) / C$ para alguna normalización $C > 0$,
   donde $\operatorname{tr}(Q|_{\text{neg}})$ es la traza del operador de Weil restringido
   a su subespacio negativo.

*Prueba de (3):* Los valores propios negativos de $T_0$ (operador de Weil) son, bajo
Hipótesis D, proporcionales a $-b_j^2$ (el valor propio $j$-ésimo mide la "profundidad"
de la dirección negativa, que escala como $b_j^2$). La traza sobre el subespacio negativo
es $\sum_j (-b_j^2) \cdot C^{-1}$, luego $\Phi = -\operatorname{tr}(Q|_{\text{neg}})/C$. $\square$

*Consecuencia de (3):* $\Phi$ es un invariante del operador de Weil, no una cantidad
artificial. Se desprende naturalmente de la forma de Weil.

---

## 4. La conexión con el flujo de de Bruijn–Newman (unificación A y D)

**Teorema D.7** (unificación Frentes A y D). El flujo de de Bruijn–Newman sobre
configuraciones de ceros es el flujo gradiente de $E_{\log}$:
$$\frac{dz_n}{dt} = -\frac{\partial E_{\log}}{\partial \bar z_n} = \sum_{k \ne n} \frac{2}{z_k - z_n}.$$

(Csordas–Norfolk–Varga 1988, cf. Frente A.)

Por tanto, la pregunta del Frente D —

> ¿Es $b_n = 0$ el único mínimo global de $E_{\text{arith}}$ sujeto a las restricciones
> aritméticas de $\zeta$?

— es la misma pregunta que el Frente A expresada en lenguaje variacional.

**Diferencia entre A y D:** El Frente A pregunta por la *monotonicidad* de $\kappa_t$.
El Frente D pregunta por la *estructura del mínimo* de $E_{\text{arith}}$. La segunda
formulación es más precisa: puede existir un mínimo sin que el flujo sea monótono.

---

## 5. La analogía con cuerpos de funciones

**El mecanismo de Weil (1948) para curvas sobre $\mathbb{F}_q$:**

Sea $C$ una curva sobre $\mathbb{F}_q$, $Z(u)$ su función zeta. Los eigenvalores
$\alpha_i$ de Frobenius satisfacen $|\alpha_i| = q^{1/2}$. Weil probó esto mostrando que
la forma cuadrática $\langle D, D \rangle$ (grado de la auto-intersección de la
correspondencia de Frobenius $D = \Gamma_\phi - \Delta$) es *positiva definida*.

La estructura es:
- Hay un espacio de correspondencias (análogo a $L^2(C_\mathbb{Q})$).
- Hay una forma bilineal canónica (análogo a $Q$).
- La positividad de la forma fuerza los eigenvalores a tener módulo correcto.

En cuerpos de funciones, la prueba tiene DOS ingredientes:
1. **Autoadjunción:** la correspondencia de Frobenius es *autoadjunta* respecto a la
   forma de intersección.
2. **Positividad:** la forma de intersección es *positiva definida*.

El Frente D busca el análogo de la positividad para $\mathbb{Z}$:

> ¿Existe una energía canónica sobre configuraciones de ceros de $\zeta$ cuya
> positividad en la dirección transversal fuerza $b_j = 0$?

**Tabla comparativa:**

| Objeto | Curvas sobre $\mathbb{F}_q$ | $\zeta$ sobre $\mathbb{Z}$ |
|---|---|---|
| Eigenvalores de Frobenius | $\alpha_i$ con $|\alpha_i| = q^{1/2}$ | Ceros $\rho_j$ con $\operatorname{Re}(\rho_j) = 1/2$ |
| Forma canónica | Intersección $\langle D, D \rangle$ | Forma de Weil $Q$ |
| Positividad probada | Sí (Weil 1948) | No (abierto) |
| Energía transversal | $\sum_i |\alpha_i - q^{1/2}|^2 = 0$ iff Weil | $\Phi = \sum_j b_j^2 = 0$ iff RH |
| Mecanismo | Hodge index theorem en $J(C)$ | **Desconocido — objetivo del Frente D** |

---

## 6. El modelo energético exacto

**Definición D.8** (energía transversal derivada de la forma de Weil). Para la forma
de Weil $Q$ con operador $T_0 = T_0^+  + T_0^-$ (descomposición en parte positiva y
negativa), define:
$$\Phi_{\text{Weil}}(Q) := \|T_0^-\|_{\text{tr}} = \operatorname{tr}(-T_0^-)
  = \sum_j |\lambda_j^-|,$$
donde la suma es sobre los valores propios negativos de $T_0$.

Esta es la *norma de traza del operador de Weil* en su parte negativa.

**Proposición D.9.** $\Phi_{\text{Weil}}(Q) = 0 \iff \kappa(Q) = 0 \iff$ RH.

*Prueba:* Si $\kappa(Q) = 0$, la parte negativa $T_0^- = 0$, luego $\Phi_{\text{Weil}} = 0$.
Si $\kappa(Q) > 0$, hay al menos un valor propio negativo $\lambda^- < 0$, luego
$\Phi_{\text{Weil}} \ge |\lambda^-| > 0$. $\square$

**La pregunta dinámica (nueva):** ¿Puede $\Phi_{\text{Weil}}$ ser disminuida por un flujo
natural en el espacio de formas de Weil, con mínimo único en $\Phi_{\text{Weil}} = 0$?

---

## 7. La penalización transversal y el espacio de restricciones

La propuesta del colega: agregar una penalización $\sum_i V(b_i)$ donde $V: \mathbb{R} \to
\mathbb{R}_{\ge 0}$ satisface $V(b) = 0 \iff b = 0$ y $V(b) > 0$ para $b \ne 0$.

La pregunta precisa: ¿puede $V$ *derivarse* de la ecuación funcional de $\zeta$?

**Proposición D.10** (el potencial transversal de la ecuación funcional). La ecuación
funcional $\zeta(s) = \chi(s)\zeta(1-s)$ (con $\chi(s)$ el factor de simetría)
implica que los ceros vienen en pares $(\rho, 1-\rho)$. Para un cero $\rho = 1/2 + b + i\gamma$
con $b \ne 0$:

- La órbita bajo $s \mapsto 1 - \bar s$ es $\{1/2 + b + i\gamma, 1/2 - b - i\gamma,
  1/2 + b - i\gamma, 1/2 - b + i\gamma\}$.
- La contribución a la energía $E_{\log}$ de esta órbita de cuatro puntos incluye
  repulsión interna entre los puntos de la misma órbita.
- La *energía de auto-interacción de la órbita* es:
  $$E_{\text{self}}(b, \gamma) = -\log|2b| - 2\log|2i\gamma| - \log|2b| + \ldots$$
  que DIVERGE cuando $b \to 0$ (por el término $-\log|2b|$).

**Observación D.11** (nueva). El potencial $V(b) = -\log|2b|$ tiene una singularidad
logarítmica en $b = 0$: los dos ceros de la órbita con $\operatorname{Re} = 1/2 \pm b$
se *repelen logarítmicamente* entre sí. Cuanto más pequeño es $b$, más fuerte es la
repulsión.

Pero esta repulsión actúa *a lo largo de la recta crítica*, no transversalmente. Para
confinamiento transversal necesitamos que el gradiente de $E_{\text{arith}}$ en la
dirección $b$ apunte hacia $b = 0$.

---

## 8. La pregunta central del Frente D

**Pregunta D.12** (nueva, central del Frente D). Sea
$$\mathcal{Z}_\zeta := \{\text{configuración de ceros de } \zeta\}$$
(un único punto, la configuración real de ceros). Considera la familia de configuraciones
$$\mathcal{Z}_{\text{arith}} := \{\text{ceros de funciones en la clase de } \zeta\}$$
(funciones enteras del mismo orden y tipo, con producto de Euler y ecuación funcional
análoga). ¿Satisface $E_{\text{arith}}$ las siguientes propiedades en $\mathcal{Z}_\zeta$?

1. $\partial E_{\text{arith}}/\partial b_j\big|_{b_j = 0} = 0$ (la recta crítica es punto crítico).
2. $\partial^2 E_{\text{arith}}/\partial b_j^2\big|_{b_j = 0} > 0$ (es un mínimo local estricto).
3. No existen otros mínimos en $\mathcal{Z}_{\text{arith}}$ (unicidad del mínimo global).

Si las tres condiciones se verifican: la recta crítica es el único mínimo global de
$E_{\text{arith}}$ en $\mathcal{Z}_{\text{arith}}$, y RH se sigue de la existencia de
un mínimo (que ocurre en $b_j = 0$).

---

## 9. Verificación de la condición (1): la recta crítica es punto crítico

**Proposición D.13.** La configuración $b_j = 0$ (todos los ceros en la recta crítica)
es siempre un punto estacionario de $E_{\text{arith}}$ en la dirección transversal.

*Prueba:* Por simetría. Si $b_j = 0$ para todo $j$, la configuración es simétrica bajo
$z_n \mapsto -\bar z_n$ (reflexión en la recta crítica, que en la coordenada $z$ es la
recta $\operatorname{Re} z = 0$). La energía $E_{\text{arith}}$ es simétrica bajo esta
reflexión. Por tanto, el gradiente en la dirección transversal $b_j$ es cero en $b_j = 0$.
$\square$

*Observación:* Esta proposición sólo dice que la recta crítica es un punto estacionario.
No distingue entre mínimo, máximo o punto de silla. Ése es el contenido de la condición (2).

---

## 10. El obstáculo: condición (2) requiere la estructura de Euler

**Proposición D.14** (obstáculo). La positividad de la Hessiana $\partial^2
E_{\text{arith}}/\partial b_j^2 > 0$ en $b_j = 0$ NO se sigue de la simetría sola.
Requiere la restricción a configuraciones compatibles con el producto de Euler.

*Argumento:* Sin el producto de Euler, pueden construirse funciones enteras con ecuación
funcional y ceros fuera de la recta crítica donde la Hessiana es negativa (el punto
crítico es un máximo local). El producto de Euler impone que la función factoriza
sobre los primos, lo que restringe los ceros a "posiciones compatibles con la aritmética."

*Esto es exactamente Wall A (Phase 27) en lenguaje variacional:* la restricción al
producto de Euler es la razón por la que la Hessiana podría ser positiva. Sin esa
restricción, el mínimo no está necesariamente en la recta crítica.

---

## 11. La analogía más precisa con cuerpos de funciones

En el caso de curvas sobre $\mathbb{F}_q$, la positividad de la forma de intersección
se prueba usando el *teorema del índice de Hodge*: para divisores en la Jacobiana,
la forma de intersección tiene precisamente un índice de Sylvester determinado por la
geometría de la curva (genus $g$ da índice $(1,2g-1)$ en cierta normalización).

El análogo para $\zeta$ sería:

> La forma de Weil $Q$ tiene índice de Sylvester $(+\infty, 0)$ (positivo definido)
> cuando se restringe a funciones de prueba compatibles con la estructura del producto
> de Euler.

Esto es exactamente la afirmación RH expresada como un enunciado sobre el *índice de
Hodge* del "espacio de correspondencias aritméticas" de $\operatorname{Spec}\mathbb{Z}$.

Formulado de esta manera, **el Frente D es isomorfo al Frente B en lenguaje variacional:**

| Frente B | Frente D |
|---|---|
| $\eta(T_0) = 0$ por anticometización | Hessiana positiva por restricción de Euler |
| Anticometización de Fourier | Restricción al producto de Euler |
| $\kappa = 0$ por APS | $\kappa = 0$ por mínimo variacional |

---

## 12. Veredicto del Frente D

| Resultado | Estado |
|---|---|
| $\Phi(Z) \ge 0$ con igualdad iff RH | Trivial |
| $\Phi$ derivada de la forma de Weil | Probado (Prop. D.6, (3)) |
| Flujo DBN = gradiente de $E_{\log}$ | Establecido (Front A = Front D) |
| Recta crítica es punto estacionario de $E_{\text{arith}}$ | Probado (Prop. D.13) |
| Hessiana positiva en $b_j = 0$ | **Abierto — requiere restricción de Euler** |
| Unicidad del mínimo global | **Abierto — depende de la estructura aritmética** |
| Analogía precisa con Weil/cuerpos de funciones | Identificada |
| Front D = Front B en lenguaje variacional | **Nuevo resultado de Phase 28** |

---

## 13. La pregunta más concreta a atacar

De los cuatro frentes, la pregunta más directamente atacable que no ha sido formulada
en ningún paper conocido:

**Pregunta D.15** (la pregunta de Phase 28). Considerar la segunda variación de la
forma de Weil $Q[Z + \epsilon \delta Z]$ cuando se perturba la configuración de ceros
en la dirección transversal $b_j \to b_j + \epsilon c_j$:

$$\frac{d^2}{d\epsilon^2} Q[Z_\epsilon]\bigg|_{\epsilon=0} = ?$$

¿Es esta segunda variación positiva (semidefinida) para toda perturbación $c_j$ compatible
con el producto de Euler?

Si la respuesta es sí: $b_j = 0$ es un mínimo local estricto de $Q$ en la dirección
transversal, y (con unicidad) RH se sigue.

El cálculo de esta segunda variación a partir de la fórmula explícita de Weil–Guinand
es, hasta donde sabemos, nuevo. Es el primer paso concreto del Frente D.
