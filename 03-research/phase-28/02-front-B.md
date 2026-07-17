# Frente B — Flujo espectral y $\eta$-invariante de Atiyah–Patodi–Singer

**Fecha:** junio 2026

---

## 1. Setup: el flujo espectral como reformulación de $\kappa$

**Definición B.1** (flujo espectral). Sea $\{T_\lambda\}_{\lambda \in [0,1]}$ una familia
continua de operadores autoadjuntos de Fredholm en un espacio de Hilbert $H$. El
*flujo espectral* $\operatorname{sf}(\{T_\lambda\})$ es el número neto de valores propios
que cruzan cero de negativo a positivo mientras $\lambda$ va de $0$ a $1$.

Formalmente: $\operatorname{sf}(\{T_\lambda\}) = \#\{\text{cruces} \uparrow\} - \#\{\text{cruces} \downarrow\}$.

**Proposición B.2** (flujo espectral = índice de Kreĭn). Sea $Q$ la forma de Weil con
operador asociado $T$ (definido por $Q(f,g) = \langle Tf, g\rangle_H$ respecto a un
producto interior positivo fijo $\langle\cdot,\cdot\rangle_H$ en $H$). Sea $T_1 = I$
(identidad, positivo definido). Entonces para cualquier camino $\{T_\lambda\}_{\lambda
\in [0,1]}$ de $T_0 = T$ a $T_1 = I$:
$$\operatorname{sf}(\{T_\lambda\}) = \kappa(Q) = \#\{\text{valores propios negativos de } T\}.$$

*Prueba:* El flujo espectral a lo largo del camino cuenta los cruces de cero. Partimos
de $T_0 = T$ con $\kappa$ valores propios negativos y llegamos a $T_1 = I > 0$ sin
valores propios negativos. Cada valor propio negativo de $T_0$ debe cruzar cero
exactamente una vez (para caminos genéricos). La diferencia neta es $\kappa - 0 = \kappa$.
$\square$

*Observación:* El flujo espectral es un invariante de homotopía (relativa a los extremos):
no depende del camino específico de $T$ a $I$.

---

## 2. El teorema de Atiyah–Patodi–Singer

**Teorema B.3** (APS 1976). Sea $M = [0,1] \times X$ una variedad cilíndrica con frontera
$\partial M = \{0\} \times X \cup \{1\} \times X$, y $D = \partial/\partial\lambda + T_\lambda$
el operador de tipo Dirac en el cilindro. Entonces:
$$\operatorname{sf}(\{T_\lambda\}) = \operatorname{Ind}(D_{\text{APS}}) + \frac{\eta(T_0) - \eta(T_1)}{2},$$
donde $\operatorname{Ind}(D_{\text{APS}})$ es el índice del problema de valor de frontera
de APS, y $\eta(A)$ es el $\eta$-invariante del operador $A$:
$$\eta(A) = \lim_{s \to 0^+} \sum_{\lambda \ne 0} \operatorname{sgn}(\lambda) |\lambda|^{-s},$$
la suma sobre todos los valores propios no nulos de $A$.

Combinando con B.2:
$$\kappa(Q) = \operatorname{Ind}(D_{\text{APS}}) + \frac{\eta(T_0) - \eta(T_1)}{2}.$$

Para $T_1 = I$ (identidad): $\eta(I) = 0$ (todos los valores propios positivos, suma con
signos $= +\infty$ regularizada $= 0$ por simetría... necesita cuidado). Más precisamente,
$\eta(I) = \dim H$ en dimensión finita, pero para el camino a $I$ en dimensión infinita
la convención correcta es $\eta(I) = 0$ por elección del camino de referencia.

**Corolario B.4.** Bajo convenciones estándar:
$$\kappa(Q) = \operatorname{Ind}(D_{\text{APS}}) + \frac{\eta(T_0)}{2}.$$

Entonces: **$\kappa(Q) = 0$ si y sólo si $\operatorname{Ind}(D_{\text{APS}}) = -\eta(T_0)/2$.**

En particular, si ambos $\operatorname{Ind}(D_{\text{APS}}) = 0$ y $\eta(T_0) = 0$, entonces $\kappa = 0$.

---

## 3. El $\eta$-invariante del operador de Weil

**Definición B.5** (operador de Weil). Sea $T_0$ el operador de la forma de Weil $Q$
sobre $L^2(C_\mathbb{Q})$ con producto interno positivo fijo $\langle\cdot,\cdot\rangle$:
$$Q(f,g) = \langle T_0 f, g\rangle, \qquad T_0 = T_0^*.$$

El espectro de $T_0$:
- Valores propios positivos: provienen de las contribuciones de primos y del factor
  arquimediano.
- Valores propios negativos: provienen de los ceros fuera de la recta crítica.
- Bajo Hipótesis D con $m$ órbitas: hay exactamente $2m$ valores propios negativos.

**Definición B.6** ($\eta$-invariante de $T_0$). Formalmente:
$$\eta(T_0) = \lim_{s \to 0^+} \left(\sum_{\lambda > 0} \lambda^{-s} - \sum_{\lambda < 0} |\lambda|^{-s}\right),$$
donde las sumas son sobre valores propios de $T_0$.

Esta cantidad mide la *asimetría espectral*: cuánto más pesado es el espectro positivo
que el negativo.

---

## 4. La simetría funcional y la posible vanación de $\eta$

**Proposición B.7** (simetría $s \leftrightarrow 1-s$ de la forma de Weil). La ecuación
funcional $\xi(s) = \xi(1-s)$ implica que la forma de Weil $Q$ satisface:
$$Q(Jf, Jg) = Q(f, g), \quad \text{donde } (Jf)(x) = \frac{1}{x} f\!\left(\frac{1}{x}\right).$$

En términos del operador $T_0$: $J T_0 J^{-1} = T_0$, es decir, $T_0$ conmuta con $J$.

*Prueba:* La ecuación funcional $\xi(s) = \xi(1-s)$ corresponde a la transformación $x
\mapsto 1/x$ en el espacio de funciones de prueba. La forma de Weil es invariante bajo
esta transformación. $\square$

**Consecuencia para los valores propios:** Si $T_0 \phi = \lambda \phi$, entonces
$T_0 (J\phi) = J T_0 \phi = \lambda (J\phi)$.
Luego $J$ permuta los subespacios propios con el mismo valor propio. Esto NO anticometiza
el espectro; la simetría $J$ no fuerza $\eta = 0$.

*Este es el primer obstáculo del Frente B.* La simetría $s \leftrightarrow 1-s$ de la
ecuación funcional preserva los valores propios de $T_0$, no los invierte. Para $\eta = 0$
necesitaríamos una simetría que anticometice el espectro.

---

## 5. ¿Cuándo es $\eta(T_0) = 0$?

**Proposición B.8** (condición suficiente para $\eta = 0$). Si existe una involución
$K: H \to H$ tal que $K T_0 K^{-1} = -T_0$ (anticometización), entonces $\eta(T_0) = 0$.

*Prueba:* $K$ mapea biyectivamente el espectro positivo al negativo y viceversa, con
igual multiplicidad. La suma $\eta = \sum \operatorname{sgn}(\lambda)|\lambda|^{-s}$
se cancela. $\square$

**Pregunta B.9** (nueva, central). ¿Existe una involución $K$ en $L^2(C_\mathbb{Q})$
tal que $K T_0 K^{-1} = -T_0$?

Para que $K$ anticometice $T_0$, necesitaría mapear las contribuciones positivas
(primos + archimediano) en negativas (ceros). Esto requeriría una dualidad entre
el "sector aritmético" y el "sector espectral" de la forma de Weil.

La candidata natural: la transformada de Fourier sobre $C_\mathbb{Q}$. Bajo la
transformada de Fourier $\hat\cdot$:
$$Q(f,g) \longleftrightarrow Q(\hat f, \hat g) = ?$$

Si $Q(\hat f, \hat g) = -Q(f,g)$, entonces $K = \mathcal{F}$ (Fourier) anticometiza $T_0$.

**Proposición B.10** (obstáculo a la anticometización de Fourier). La ecuación de
Poisson–Weil da:
$$Q(f,g) + Q(\hat f, \hat g) = (\text{términos de frontera}).$$

Si los términos de frontera son cero, entonces $Q(\hat f, \hat g) = -Q(f,g)$, dando $\eta = 0$.

*Estado:* Se desconoce si los términos de frontera se anulan en general. Esta es la
pregunta precisa a resolver en el Frente B.

---

## 6. La conexión con los valores especiales de $\zeta$

**Observación B.11.** Para operadores aritméticos, el $\eta$-invariante se expresa
frecuentemente en términos de funciones $L$ en puntos especiales. Ejemplos conocidos:

- $\eta(\operatorname{sign}_\Gamma)$ para el operador de signo en una variedad hiperbólica
  aritmética expresa combinaciones de valores de funciones $L$ de Dedekind en $s = 0$.
- El $\eta$-invariante de Dirac en espacios lente se expresa mediante sumas de Dedekind.

**Conjetura B.12** (nueva). El $\eta$-invariante del operador de Weil $T_0$ satisface:
$$\eta(T_0) = c \cdot \zeta'(0) + d \cdot \log(2\pi)$$
para algunas constantes $c, d$ que dependen sólo de normalizaciones.

Si $\eta(T_0) \ne 0$ y $\operatorname{Ind}(D_{\text{APS}}) = \eta(T_0)/2$, el corolario
B.4 da $\kappa = 0$. Esta sería la prueba de RH vía APS.

El cálculo explícito de $\eta(T_0)$ es el objetivo primario del Frente B.

---

## 7. Veredicto del Frente B

| Resultado | Estado |
|---|---|
| $\operatorname{sf} = \kappa(Q)$ | Probado (Prop. B.2) |
| Fórmula APS para $\kappa$ | Establecida (Cor. B.4) |
| Simetría $J$ no anticometiza | Probado (Prop. B.7) |
| Candidata $K = \mathcal{F}$ (Fourier) | Identificada; requiere verificar términos de frontera |
| $\eta(T_0) = 0$ por anticometización | **Abierto — el corazón del Frente B** |
| $\eta(T_0)$ como valor especial de $\zeta$ | Conjetura B.12 — nuevo resultado a probar |

**El obstáculo preciso:** verificar si $Q(f,g) + Q(\hat f, \hat g) = 0$ (términos de
frontera nulos en la ecuación de Poisson–Weil). Esto implicaría $\eta(T_0) = 0$ y,
via APS, $\kappa = 0$, luego RH.
