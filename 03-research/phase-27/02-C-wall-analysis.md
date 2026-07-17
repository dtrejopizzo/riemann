# Phase 27-C — Análisis del principio local-global

**Fecha:** junio 2026
**Objetivo:** ¿Puede la positividad local de $Q$ en cada prima $p$ implicar la positividad
global de $Q$? ¿Existe siquiera una noción de "forma local $Q_p$"?

---

## 1. La propuesta y su reformulación precisa

La propuesta de Phase 27-C era:
$$Q = Q_\infty \times \prod_p Q_p, \qquad Q_p \ge 0 \text{ para todo } p \implies Q \ge 0 \text{ globalmente.}$$

Antes de preguntarse si la implicación vale, hay que preguntar si el miembro izquierdo
tiene sentido. La auditoría de este documento tiene dos partes:

**Wall A:** ¿Existe una descomposición $Q \rightsquigarrow (Q_\infty, Q_p)$?

**Wall B:** Si existe, ¿la positividad local implica positividad global?

El usuario identificó correctamente que **Wall A es más difícil que Wall B** y que
su resolución es la verdadera puerta de entrada a Phase 27.

---

## 2. Descomposición de la forma de Weil — qué parte factoriza

La forma de Weil $Q(f,g) = \mathcal{W}(f*\tilde{g})$ tiene tres tipos de términos.
Sea $h = f * \tilde{g}$ (convolución de Mellin). Entonces:

$$Q(f,g) = \underbrace{\sum_\rho \hat{h}(\rho)}_{Q_{\text{cero}}}
           \underbrace{- \hat{h}(0)\log\pi - \hat{h}(1)\log\pi + h(1)\log\pi}_{Q_\infty}
           + \underbrace{\sum_{p,n} \frac{\log p}{p^{n/2}} [h(p^n) + h(p^{-n})]}_{Q_{\text{primo}}}.$$

### El término primo: SÍ factoriza

$$Q_{\text{primo}}(f,g) = \sum_p Q_p^{\text{pr}}(f,g),$$
$$Q_p^{\text{pr}}(f,g) := \sum_{n=1}^\infty \frac{\log p}{p^{n/2}} [(f*\tilde{g})(p^n) + (f*\tilde{g})(p^{-n})].$$

Cada $Q_p^{\text{pr}}$ es una forma que depende sólo de los valores de $f*\tilde{g}$
en las potencias de $p$. Es genuinamente local.

**¿Es $Q_p^{\text{pr}}$ positiva-definida?** NO. Contraejemplo directo:
sea $f$ con $\hat{f}(s) \approx 1$ cerca de $s = 1/2$ y cero en otra parte.
Entonces $(f*\tilde{f})(p^n) = \hat{f}(1/2)^2 p^{-n/2}$ aproximadamente, y
$Q_p^{\text{pr}}(f,f) \approx (\log p) \hat{f}(1/2)^2 \sum_n p^{-n} > 0$.
Sin embargo, para $f$ concentrada en frecuencias donde $\hat{f}(\rho) < 0$ para
algunos ceros $\rho$, el término primo puede ser negativo.
**La positividad de $Q_p^{\text{pr}}$ no es automática ni independiente de los ceros.**

### El término archimediano: SÍ es un factor único

$Q_\infty(f,g) = -\hat{h}(0)\log\pi - \hat{h}(1)\log\pi + h(1)\log\pi$.

Es un término único (el lugar $v = \infty$). Su positividad tampoco es automática.

### El término de ceros: NO factoriza

$$Q_{\text{cero}}(f,g) = \sum_\rho \hat{h}(\rho) = \sum_\rho \hat{f}(\rho)\overline{\hat{g}(\bar\rho)}.$$

**Proposición 27-C.1** (Wall A: no-factorización del término de ceros).

El término $Q_{\text{cero}}(f,g)$ no puede escribirse como $\sum_p A_p(f,g)$ donde
cada $A_p(f,g)$ depende sólo de los valores de $f$ y $g$ en las potencias de $p$.

*Prueba.* $\hat{f}(\rho) = \int_0^\infty f(x) x^{\rho-1} dx$ depende de $f$ en TODOS los
puntos de $\mathbb{R}^*_+$, no sólo en $\{p^n : n \in \mathbb{Z}\}$ para ningún primo $p$ fijo.
Si $f$ es una función suave localizada en $[2, 3]$ (lejos de toda potencia de $p$ para $p \ge 5$),
entonces $A_p(f,g) = 0$ para $p \ge 5$ pero $\hat{f}(\rho) \ne 0$ en general.
Por lo tanto $Q_{\text{cero}}$ no puede expresarse como suma de términos locales en $p$. $\square$

---

## 3. La razón profunda: los ceros de $\zeta$ son objetos globales sin factorización local

**Proposición 27-C.2** (no-existencia de "ceros locales en $p$").

El factor de Euler $L_p(s) = (1-p^{-s})^{-1}$ no tiene ceros. En consecuencia:

1. No existe una noción de "ceros de $\zeta$ en la prima $p$".
2. Los ceros no-triviales de $\zeta$ son objetos genuinamente globales, sin localización
   en ningún primo.
3. El término $Q_{\text{cero}}$ no tiene factores locales en $p$ porque ningún primo
   "posee" ningún cero de $\zeta$.

*Prueba.* $(1-p^{-s})^{-1}$ es holomorfa en todo $\mathbb{C}$ excepto por un polo en
$s = 0$ (si $p = \infty$: el factor $\Gamma$ tiene polos en $\mathbb{Z}_{\le 0}$). Para
$p < \infty$: $(1-p^{-s})^{-1}$ nunca se anula. $\square$

**Corolario 27-C.3** (contraste con el caso de cuerpos de funciones).

Para una curva $C/\mathbb{F}_q$, los ceros de la función $\zeta$ de $C$ son los
eigenvalores del Frobenius $\text{Frob}_p$ actuando en $H^1(C, \mathbb{Q}_\ell)$.
El Frobenius en cada punto cerrado $P \in C(\mathbb{F}_{q^n})$ ES un objeto local.
La Hipótesis de Riemann para curvas (Weil 1948, Deligne 1974) sigue de la positividad
de la forma de intersección en $H^1$, que factoriza localmente.

Para $\zeta(s)$ sobre $\mathbb{Q}$: no existe el análogo del "Frobenius en una prima".
El espacio cohomológico $H^1$ que contendría los ceros de $\zeta$ como eigenvalores
de Frobenius es exactamente el objeto que el programa de Connes–Consani intenta construir
(el "sitio aritmético"). No existe como teorema.

---

## 4. Wall A: diagnóstico preciso

**Definición 27-C.4** (Wall A).

Wall A es la afirmación:

> Existe una descomposición $Q = Q_\infty + \sum_p Q_p$ (como suma aditiva sobre lugares)
> tal que $Q_p \ge 0$ para todo $p$ y $Q_\infty \ge 0$ en algún sentido geométrico.

**Proposición 27-C.5** (Wall A está bloqueada por la ausencia del sitio aritmético).

Wall A equivale a construir:
1. Una cohomología aritmética $H^1(\operatorname{Spec}\mathbb{Z},\mathcal{F})$ sobre $\mathbb{Z}$;
2. Un operador de Frobenius aritmético $\phi_p: H^1 \to H^1$ en cada prima $p$;
3. Una forma de intersección en $H^1$ que: (a) factoriza como $Q = Q_\infty + \sum_p Q_p$, y
   (b) su positividad sea equivalente a RH.

*Observación.* Este es el programa de Connes–Consani (2010–2016): el "sitio de escalado"
y la geometría aritmética sobre $\mathbb{F}_1$ intentan construir exactamente estos objetos.
Su construcción existe como framework pero no como teorema (la positividad de la forma
de intersección, análoga al teorema de índice de Hodge, es el equivalente de RH, no su prueba).

**Estado de Wall A:** OPEN. Su resolución equivale a establecer el sitio aritmético de
Connes–Consani como objeto matemático riguroso con una forma de intersección $\ge 0$.

---

## 5. Wall B: análisis condicional

**Suposición.** Aceptamos provisionalmente que Wall A está resuelta: existen formas
locales $Q_p$ tal que $Q = Q_\infty + \sum_p Q_p$.

**Wall B:** ¿$Q_p \ge 0$ para todo $p$ implica $Q \ge 0$?

Esta sería la versión infinito-dimensional del teorema de Hasse–Minkowski.

**Teorema de Hasse–Minkowski clásico** (formas cuadráticas sobre $\mathbb{Q}$):
Una forma cuadrática $Q$ con coeficientes en $\mathbb{Q}$ es positiva-definida sii
su localización $Q \otimes_\mathbb{Q} \mathbb{R}$ y $Q \otimes_\mathbb{Q} \mathbb{Q}_p$
son positivas-definidas para todo primo $p$.

**Obstáculos para la versión infinito-dimensional:**

**(B.1)** El Hasse–Minkowski clásico aplica a formas cuadráticas en dimensión FINITA.
La forma de Weil $Q$ actúa en el espacio de dimensión infinita $\mathcal{S}(\mathbb{R}^*_+)$.
No existe un teorema de Hasse–Minkowski para formas hermitianas en dimensión infinita.

**(B.2)** En dimensión infinita, la positividad local no implica positividad global incluso
para formas simples. Ejemplo: sea $Q(f,f) = \int_0^\infty f(x)^2 w(x) dx$ donde $w$ cambia
de signo. Localmente (en intervalos pequeños) $Q$ puede ser positiva, pero globalmente puede
ser indefinida.

**(B.3)** Las formas locales $Q_p$ (si existen) serían hermitianas infinito-dimensionales
sobre $\mathbb{Q}_p$. La teoría de dichas formas no tiene versión de Hasse–Minkowski.

**Proposición 27-C.6** (Wall B no tiene prueba conocida).

No existe en la literatura un teorema de Hasse–Minkowski para formas hermitianas
infinito-dimensionales. En particular, la implicación
$$Q_p \ge 0 \text{ para todo } p \implies Q \ge 0 \text{ globalmente}$$
no se sigue de ningún resultado conocido de la teoría de formas cuadráticas.

**Sin embargo:** Si el sitio aritmético de Connes–Consani existiese como objeto
matemático riguroso, el análogo del teorema de índice de Hodge para superficies (que es
FINITO-DIMENSIONAL) podría aplicar y dar Wall B como consecuencia. Esto sería el
argumento de Weil-Deligne para curvas elevado a $\operatorname{Spec}\mathbb{Z}$.

---

## 6. La jerarquía de dificultad

| Muro | Contenido | Estado | Relación con RH |
|---|---|---|---|
| Wall A (factorización) | Existen $Q_\infty, Q_p$ con $Q = Q_\infty + \sum_p Q_p$ | **ABIERTO** — equivale al sitio aritmético de Connes–Consani | RH-equivalente (positiv. de la forma de intersección) |
| Wall B (local→global) | $Q_p \ge 0 \forall p \implies Q \ge 0$ | **ABIERTO** — versión infinito-dim del HM | RH-equivalente (si Wall A se resuelve) |
| Wall W4-RSRP (Phase 25) | Prop. aritmética de Re(s)>1 → ceros en franja crítica | ABIERTO | RH-equivalente |

**Conclusión:** Los tres muros son RH-equivalentes, formulados en lenguajes diferentes.

Wall A es una reformulación de Wall W4-RSRP en términos de cohomología aritmética:
"la información aritmética local (factores de Euler, $Q_p$) no se propaga globalmente
(hacia los ceros de $\zeta$, hacia $Q \ge 0$) sin la cohomología global del sitio aritmético."

---

## 7. Lo que Phase 27 establece

**Resultado positivo de Phase 27-C:**

Phase 27-C identifica con precisión que Wall A es equivalente a la construcción del
sitio aritmético de Connes–Consani. Esto es:

1. Una reformulación más precisa de Wall W4-RSRP que cualquier formulación anterior.
2. La conexión entre el programa de este arco (Kreĭn + Connes) y el programa de
   Connes–Consani (geometría aritmética sobre $\mathbb{F}_1$).
3. La identificación del objeto matemático necesario: un espacio cohomológico $H^1$ sobre
   $\mathbb{Z}$ con un operador de Frobenius en cada prima y una forma de intersección positiva.

**Resultado negativo de Phase 27-C:**

Phase 27-C no prueba $\operatorname{neg.ind}(H_C) = 0$. Los dos muros (Wall A y Wall B)
están abiertos. El muro más difícil es Wall A.

**El diagnóstico preciso:** Phase 27 reformula RH como la positividad de una forma de
intersección en una cohomología aritmética sobre $\mathbb{Z}$, que es exactamente el
programa de Connes–Consani. La cadena es:
$$\operatorname{neg.ind}(H_C) = 0
\iff Q \ge 0
\iff \text{positividad de la forma de intersección en } H^1(\operatorname{Spec}\mathbb{Z})
\iff \text{RH.}$$
