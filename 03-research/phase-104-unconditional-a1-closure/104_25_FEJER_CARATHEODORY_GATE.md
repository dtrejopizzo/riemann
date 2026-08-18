# 104_25 — Gate Fejér--Carathéodory y barrera exacta de holomorfía

**Rol.** Probar el mecanismo analítico más corto que convertiría el cociclo
cúbico en el margen \(3\lambda_n-A_n\), y auditar si aporta información
incondicional. El mecanismo es correcto: una cota de Carathéodory en el disco
produce todos los signos por el kernel de Fejér. Sin embargo, para el cociclo
completado, la mera holomorfía en esos discos cuando
\(\varepsilon\downarrow0\) ya equivale a RH. En discos seguros más pequeños
solo se obtienen medias amortiguadas, insuficientes coeficiente a coeficiente.

Este documento no prueba A1 ni RH.

## 1. Identidad exacta de Fejér

Fijemos \(u>0\), y escribamos

\[
 \Phi(z)=\mathcal S_u^{[3]}(s_\varepsilon(z))
          =\sum_{k\ge0}a_kz^k,
 \qquad s_\varepsilon(z)=1+\varepsilon+{z\over1-z}.       \tag{1}
\]

Definamos la normalización con el signo del margen:

\[
 Q(z):={1-\Phi(z)\over u(1-z)^2}=\sum_{m\ge0}q_mz^m.      \tag{2}
\]

La multiplicación de series da, sin hipótesis analítica adicional,

\[
 \boxed{
 q_m={1\over u}\left[(m+1)-
       \sum_{k=0}^m(m-k+1)a_k\right]
 ={m+1\over u}\bigl(1-\sigma_m(\Phi;1)\bigr),}           \tag{3}
\]

donde

\[
 \sigma_m(\Phi;1)=
 \sum_{k=0}^m\left(1-{k\over m+1}\right)a_k.             \tag{4}
\]

Por `104_22`, sobre \(u=c\varepsilon\),

\[
 \boxed{q_{n-1}\longrightarrow 3\lambda_n-A_n.}          \tag{5}
\]

**Teorema 1.1 (Fejér--Carathéodory).** Supóngase que
\(\Phi\in\mathrm{Hol}(\mathbb D)\), que sus coeficientes son reales y
que

\[
 \Re\Phi(z)\le1\qquad(z\in\mathbb D).                    \tag{6}
\]

Entonces \(q_m\ge0\) para todo \(m\ge0\).

**Demostración.** La función \(g=1-\Phi\) tiene parte real no negativa.
Como \(g(0)=1-a_0\) y todos sus coeficientes son reales, su representación
de Herglotz puede tomarse sin constante imaginaria, con una medida positiva
\(\mu\) normalizada por \(\mu(\mathbb T)=g(0)\). La combinación de (3) es

\[
 \boxed{
 q_m={m+1\over u}\int_{-\pi}^{\pi}F_m(t)\,d\mu(t),}       \tag{7}
\]

con

\[
 F_m(t)=1+2\sum_{k=1}^m
 \left(1-{k\over m+1}\right)\cos(kt)
 ={1\over m+1}\left|\sum_{j=0}^me^{ijt}\right|^2\ge0.   \tag{8}
\]

Luego (7) es no negativa. En particular, la condición más fuerte
\(|\Phi(z)|\le1\) también basta. \(\square\)

## 2. La holomorfía requerida ya equivale a RH

Para \(u_j=c\varepsilon_j\), \(0<c<1\),
\(\varepsilon_j\downarrow0\), sea

\[
 \Phi_j(z)={Y_3(s_{\varepsilon_j}(z)-u_j)
                 \over Y_3(s_{\varepsilon_j}(z))}.        \tag{9}
\]

El mapa de Cayley (1) es una biyección

\[
 s_\varepsilon(\mathbb D)
 =\{s:\Re s>\tfrac12+\varepsilon\},
 \qquad
 z={s-1-\varepsilon\over s-\varepsilon}.                 \tag{10}
\]

**Teorema 2.1.** La siguiente afirmación es equivalente a RH:

> existe una sucesión \(\varepsilon_j\downarrow0\) para la cual cada
> \(\Phi_j\) es holomorfa en \(\mathbb D\).

**Demostración.** Bajo RH, el denominador de (9) no tiene ceros en el
semiplano (10), por lo que (9) es holomorfa.

Recíprocamente, supóngase que \(\xi(\rho)=0\) con
\(\Re\rho>1/2\). Para todo \(j\) suficientemente grande, \(\rho\) pertenece
al semiplano (10). Como \(G\) es regular y no nulo en el strip crítico, la
removibilidad en (9) fuerza

\[
 \xi(\rho-c\varepsilon_j)=0.                              \tag{11}
\]

Una subsucesión da infinitos ceros distintos que convergen a \(\rho\), en
contradicción con el aislamiento de los ceros de una función entera no
nula. No hay, por tanto, ceros a la derecha de la línea. La ecuación
funcional y la conjugación excluyen también los de la izquierda. \(\square\)

Así, aplicar directamente el Teorema 1.1 a una sucesión que retire el
regulador introduciría la conclusión buscada ya en la hipótesis de
holomorfía, antes de usar la desigualdad (6).

## 3. Incluso el signo eventual a regulador fijo fuerza el disco

Hay una versión coeficiente a coeficiente de la misma barrera. Fijado
\(\varepsilon>0\), supóngase que los coeficientes de (2) satisfacen
\(q_m\ge0\) para todo \(m\) suficientemente grande. El cociclo es regular
para \(0<z<1\), porque allí \(s_\varepsilon(z)>1\). Si la cola fuera un
polinomio, el radio de \(Q\) sería infinito. En otro caso, si el radio fuera
\(R<1\), el teorema de Pringsheim, aplicado tras quitar el prefijo finito,
obligaría a una singularidad en el punto real positivo \(z=R\). Pero la
fórmula meromorfa de \(\Phi\) es holomorfa en un entorno de cada punto de
\((0,1)\); por solapamiento continúa el germen hasta ese entorno, una
contradicción. Por tanto \(R\ge1\), y (2) prolonga holomórficamente
\(\Phi\) a \(\mathbb D\).

En consecuencia, probar ese signo eventual para cada miembro de una
sucesión \(\varepsilon_j\downarrow0\) vuelve a implicar RH por el Teorema
2.1. Esto no hace circular al límite (5); muestra que una prueba que intente
fortalecerlo a todos los coeficientes con regulador fijo ya contiene RH.

## 4. El disco seguro no transfiere el signo

La serie de Dirichlet Euler solo está garantizada en
\(\Re s>1+u\). Poniendo \(\delta=\varepsilon-u\), para
\(0<\delta<1/2\) el mayor disco centrado en cero que el mapa (1) coloca
completamente en ese semiplano tiene radio

\[
 R_\varepsilon={\varepsilon-u\over1-\varepsilon+u}
 \sim(1-c)\varepsilon\longrightarrow0.                    \tag{12}
\]

En general el radio es \(\min\{1,\delta/(1-\delta)\}\); la fórmula mostrada
es la que rige el régimen usado aquí,
\(u=c\varepsilon\), \(\varepsilon\downarrow0\).

Incluso concediendo una cota de Schur en \(|z|\le R_\varepsilon\), Fejér
solo controlaría medias con factores \(R_\varepsilon^k\). No existe una
transferencia formal al coeficiente sin amortiguar. El siguiente testigo lo
prueba exactamente.

Sea \(0<R<1\), elíjase \(N\) de modo que \(R^{-N}>N+1\), y tome

\[
 \Phi(z)=a+Mz^N,\qquad
 (N+1)(1-a)<M\le(1-a)R^{-N},\quad0\le a<1.       \tag{13}
\]

Entonces \(|\Phi(z)|\le1\) para \(|z|\le R\), pero

\[
 q_N={(N+1)(1-a)-M\over u}<0.                    \tag{14}
\]

Por tanto la información en cualquier disco estrictamente menor no basta,
sin una nueva desigualdad especial para el cociclo aritmético.

## Estado

- **Probado:** identidad (3), mecanismo Fejér--Carathéodory y equivalencia
  exacta entre la holomorfía de los discos regulados y RH.
- **Descartado:** obtener el margen cúbico aplicando Carathéodory/Schur en el
  disco completo como input independiente; y transferir formalmente el signo
  desde el pequeño disco de convergencia Euler.
- **Abierto:** una desigualdad firmada que actúe directamente sobre el límite
  (5), sin exigir holomorfía global ni signo eventual a regulador fijo.
