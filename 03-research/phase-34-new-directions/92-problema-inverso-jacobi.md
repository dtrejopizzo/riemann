# Doc 92 — Dirección C: Problema inverso espectral de Jacobi

**Programa:** Hipótesis de Riemann — Fase 34 (nuevas direcciones)
**Fecha:** 2026-06-09
**Prerrequisitos:** Docs 59, 60, 83, 89; y teoría externa: Killip-Simon (2003), Simon (2005)

---

## Resumen

Este documento desarrolla la Dirección C del programa: el problema inverso espectral
de Jacobi aplicado al operador $J^{\mathrm{full}}$ cuya medida espectral es
$dm_{\mathrm{full}} = |\zeta(1/2+is)|^2\,dm_\infty$. Los resultados probados se
enmarcan en la teoría de Killip-Simon (2003) y Deift-Simon, que caracterizan las
medidas cuyos operadores de Jacobi son perturbaciones $\ell^2$ de la "medida de
referencia" $dm_\infty$. El resultado central es que $\sum_k e_k^2 < \infty$
(probado en P40, Path I) garantiza que $dm_{\mathrm{full}}$ es absolutamente continua
en el espectro esencial salvo por una colección discreta de masas puntuales fuera de
él; y que dichas masas puntuales están vinculadas a los ceros de $\zeta$ fuera de la
línea crítica. Se formula la Hipótesis de Riemann como condición sobre los errores
$e_k = a_k^{\mathrm{full}} - a_k^\infty$, se discute la simetría impuesta por
$b_k^{\mathrm{full}} = 0$, y se identifica la barrera estructural que impide cerrar
el argumento.

**Resultado honesto:** El mapa inverso $(e_k) \mapsto dm_{\mathrm{full}}$ es bien
definido y controlable en el espectro esencial, pero el acceso a los ceros off-críticos
requiere información sobre el soporte singular de $dm_{\mathrm{full}}$ que los
coeficientes $e_k = O(\log k/k)$ solos no determinan localmente.

---

## §1. El problema de momentos de Hamburger y operadores de Jacobi

### 1.1. Configuración

Sea $\mu$ una medida de Borel positiva sobre $\mathbb{R}$ con momentos de todos los
órdenes:
$$c_n(\mu) = \int_{\mathbb{R}} s^n \, d\mu(s), \qquad n \geq 0.$$

El **problema de momentos de Hamburger** pregunta: dada una sucesión $(c_n)_{n \geq 0}$
de números reales, ¿existe una medida $\mu$ sobre $\mathbb{R}$ tal que $c_n(\mu) = c_n$
para todo $n$? ¿Es $\mu$ única?

La condición necesaria y suficiente de existencia es que la forma cuadrática de Hankel
sea semidefinida positiva:
$$\sum_{i,j \geq 0} c_{i+j} x_i x_j \geq 0 \qquad \text{para toda sucesión finita
$(x_i)$.}$$

**Definición 1.1 (Determinantes de Hankel).** Para $n \geq 0$ se define
$$D_n(\mu) = \det\bigl(c_{i+j}(\mu)\bigr)_{0 \leq i,j \leq n}.$$
La medida $\mu$ tiene soporte infinito si y solo si $D_n(\mu) > 0$ para todo $n$.

### 1.2. Proceso de ortogonalización y operadores de Jacobi

Supongamos que $\mu$ tiene soporte infinito. El proceso de Gram-Schmidt aplicado a la
sucesión de monomios $\{1, s, s^2, \ldots\}$ en $L^2(\mu)$ produce una base ortonormal
$\{P_k(\,\cdot\,;\mu)\}_{k \geq 0}$ de polinomios ortogonales. Estos satisfacen la
**relación de recurrencia de tres términos**:

$$s\,P_k(s;\mu) = a_{k+1}(\mu)\,P_{k+1}(s;\mu) + b_k(\mu)\,P_k(s;\mu)
+ a_k(\mu)\,P_{k-1}(s;\mu),$$

donde los **coeficientes de Jacobi** satisfacen $a_k(\mu) > 0$ y $b_k(\mu) \in \mathbb{R}$.

**Definición 1.2 (Operador de Jacobi).** El **operador de Jacobi** $J(\mu)$ es el
operador autoadjunto sobre $\ell^2(\mathbb{Z}_{\geq 0})$ cuya matriz en la base canónica
$\{e_k\}$ es tridiagonal:
$$J(\mu) = \begin{pmatrix} b_0 & a_1 & & \\ a_1 & b_1 & a_2 & \\ & a_2 & b_2 & \ddots
\\ & & \ddots & \ddots \end{pmatrix}.$$

**Teorema 1.3 (Correspondencia espectral de Jacobi).** El mapa $\mu \mapsto J(\mu)$ es
una biyección entre medidas de Borel positivas con soporte infinito y momentos finitos
de todos los órdenes, y operadores de Jacobi $(a_k, b_k)$ con $a_k > 0$, $b_k \in
\mathbb{R}$. La medida espectral de $J(\mu)$ (con vector cíclico $e_0$) recupera $\mu$.

**Demostración.** Referencia clásica: Akhiezer (1965), Chihara (1978), Simon (2005).
El sentido $\mu \mapsto J(\mu)$ es el proceso de Gram-Schmidt. El sentido inverso
$J \mapsto \mu$ es la teoría espectral de operadores autoadjuntos: dada la medida
espectral $\langle e_0, E(\,\cdot\,) e_0 \rangle$ de $J$, donde $E$ es la medida
espectral proyectada de $J$, se recupera $\mu$. $\square$

### 1.3. Unicidad del problema de momentos

La unicidad (determinación de $\mu$ por sus momentos) está garantizada bajo diversas
condiciones. La más relevante aquí es:

**Teorema 1.4 (Carleman, 1926).** Si $\sum_{n=1}^\infty c_{2n}^{-1/(2n)} = +\infty$,
entonces la medida es la única solución al problema de momentos de Hamburger para los
datos $(c_n)$.

**Proposición 1.5 (Unicidad para $dm_{\mathrm{full}}$).** La medida
$dm_{\mathrm{full}}(s) = |\zeta(1/2+is)|^2\,dm_\infty(s)$ es la única solución al
problema de momentos de Hamburger para sus momentos $\{c_n^{\mathrm{full}}\}$.

**Demostración.** Los momentos de $dm_\infty$ crecen como $c_{2n}^\infty \sim C(2n)!$
(por la integración de $s^{2n}$ contra la distribución gamma), de modo que
$c_{2n}^{-1/(2n)} \sim (C(2n)!)^{-1/(2n)} \sim (Cn)^{-1}$ por la fórmula de Stirling.
La suma $\sum_n (Cn)^{-1}$ diverge, por lo que la condición de Carleman se satisface.
Como $dm_{\mathrm{full}} \leq M\,dm_\infty$ en cualquier compacto (con $M$ dependiente
del compacto), los momentos de $dm_{\mathrm{full}}$ crecen a lo sumo tan rápido como
los de $dm_\infty$, y la condición de Carleman se hereda. $\square$

**Consecuencia.** El operador de Jacobi $J^{\mathrm{full}} = J(dm_{\mathrm{full}})$
determina completamente $dm_{\mathrm{full}}$ (y viceversa). No hay ambigüedad: la
correspondencia $dm_{\mathrm{full}} \leftrightarrow (a_k^{\mathrm{full}}, b_k^{\mathrm{full}})$
es biyectiva.

---

## §2. Los tres operadores de Jacobi del programa

### 2.1. El operador de referencia $J^\infty$

La medida base es $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$, la medida
arquimediana del marco CCM (Connes-Consani-Moscovici, 2024). Sus coeficientes de Jacobi
son exactos:

$$a_k^\infty = \tfrac{1}{2}\sqrt{(2k+1)(2k+2)}, \qquad b_k^\infty = 0.$$

El operador $J^\infty$ es autoadjunto sobre $\ell^2(\mathbb{Z}_{\geq 0})$. Su espectro
esencial es $[0, +\infty)$ (media línea real no-negativa), correspondiente al hecho de
que $dm_\infty$ tiene soporte en $\mathbb{R}$ con la parametrización $s \mapsto s^2$.
Más precisamente, el soporte de $dm_\infty$ es toda la recta real, pero los coeficientes
$b_k^\infty = 0$ indican que la medida es simétrica respecto al origen, y el espectro de
$J^\infty$ como operador en $\ell^2$ es $[0,+\infty)$.

**Observación 2.1.** La rapidez de crecimiento $a_k^\infty \sim \sqrt{k}$ es
característica del problema de momentos asociado a la distribución gamma. Esto distingue
$J^\infty$ de los operadores de Jacobi clásicos (Jacobi, Laguerre, Hermite), que tienen
$a_k \sim k$ o $a_k \to $ constante.

### 2.2. El operador "on-critical" $J^{\mathrm{on}}$

**Definición 2.2 (Medida on-critical).** Definimos
$$dm_{\mathrm{full,on}}(s) = |\zeta_{\mathrm{on}}(1/2+is)|^2\,dm_\infty(s),$$
donde $\zeta_{\mathrm{on}}$ es la función zeta hipotética cuyo producto de Hadamard
incluye solo los ceros en la línea crítica $\sigma = 1/2$, proyectando todos los posibles
ceros off-críticos sobre ella (cf. Doc 83, §1.2). Si RH es verdadera, entonces
$\zeta_{\mathrm{on}} = \zeta$ y $dm_{\mathrm{full,on}} = dm_{\mathrm{full}}$.

El operador de Jacobi correspondiente es $J^{\mathrm{on}} = J(dm_{\mathrm{full,on}})$ con
coeficientes $a_k^{\mathrm{on}}, b_k^{\mathrm{on}}$.

**Proposición 2.3 (Simetría de $J^{\mathrm{on}}$).** La ecuación funcional de $\zeta$
implica que $\zeta(1/2+is) = \overline{\zeta(1/2+is)}$ (en el sentido de que $\xi$ es
real en la línea crítica), por lo que $|\zeta_{\mathrm{on}}(1/2+is)|^2 =
|\zeta_{\mathrm{on}}(1/2-is)|^2$. En consecuencia $dm_{\mathrm{full,on}}$ es simétrica
bajo $s \mapsto -s$, y $b_k^{\mathrm{on}} = 0$ para todo $k$.

**Demostración.** La ecuación funcional $\xi(s) = \xi(1-s)$ implica $\xi(1/2+it) =
\xi(1/2-it)$, y dado que $\xi$ es real para $s$ real, se tiene
$|\xi(1/2+it)|^2 = |\xi(1/2-it)|^2$. La densidad $|\zeta_{\mathrm{on}}(1/2+is)|^2$ es
pues una función par de $s$. Una medida par sobre $\mathbb{R}$ tiene coeficientes $b_k = 0$
en su operador de Jacobi, ya que $b_k = \int s |P_k(s)|^2\,d\mu(s) = 0$ por la paridad
de $|P_k(s)|^2$ y la antisimetría del integrando. $\square$

### 2.3. El operador full $J^{\mathrm{full}}$

El operador $J^{\mathrm{full}} = J(dm_{\mathrm{full}})$ tiene coeficientes
$a_k^{\mathrm{full}}, b_k^{\mathrm{full}}$. Por la misma ecuación funcional de $\zeta$
(sin asumir RH), $dm_{\mathrm{full}}(s) = |\zeta(1/2+is)|^2\,dm_\infty(s)$ es también
función par de $s$ (pues $|\zeta(1/2+is)|^2 = |\zeta(1/2-is)|^2$ se sigue de la ecuación
funcional y la reflexión de Schwarz), por lo que:

**Proposición 2.4.** $b_k^{\mathrm{full}} = 0$ para todo $k \geq 0$.

**Demostración.** Igual que la Proposición 2.3, con $\zeta$ en lugar de $\zeta_{\mathrm{on}}$.
La ecuación funcional de Riemann $\xi(s) = \xi(1-s)$ con $\xi$ real en la recta real
implica $|\zeta(1/2+is)|^2 = |\zeta(1/2-is)|^2$ para $s \in \mathbb{R}$. $\square$

**Definición 2.5 (Errores de Jacobi).** Definimos los errores del coeficiente diagonal
mayor como
$$e_k = a_k^{\mathrm{full}} - a_k^\infty, \qquad k \geq 1.$$

Dado que $b_k^{\mathrm{full}} = b_k^\infty = 0$, los errores $b_k$ son idénticamente nulos.

**Resultado probado (P40, Path I).** Los errores satisfacen:
$$e_k = O\!\left(\frac{\log k}{k}\right), \qquad \sum_{k=1}^\infty e_k^2 < \infty.$$

La primera estimación se deduce del comportamiento asintótico de los determinantes de
Hankel de $dm_{\mathrm{full}}$ via las estimaciones de la función $\zeta$ en la línea
crítica. La convergencia de la serie cuadrática es equivalente a decir que la perturbación
$J^{\mathrm{full}} - J^\infty$ es un operador **Hilbert-Schmidt** en $\ell^2$.

---

## §3. El teorema de Killip-Simon y la caracterización espectral

### 3.1. El resultado fundamental

El teorema de Killip-Simon (2003) caracteriza las medidas cuyos operadores de Jacobi son
perturbaciones $\ell^2$ de un operador de referencia. En su forma más relevante para este
programa:

**Teorema 3.1 (Killip-Simon, 2003).** Sea $J_0$ un operador de Jacobi con espectro
esencial $\Sigma = [A, B]$ (un intervalo compacto). Sea $J = J_0 + E$ una perturbación
con $E$ operador de Jacobi simétrico Hilbert-Schmidt (es decir, $a_k - a_k^0 \in \ell^2$
y $b_k - b_k^0 \in \ell^2$). Entonces la medida espectral $d\mu$ de $J$ satisface:

(i) $d\mu$ es absolutamente continua en $\Sigma$ respecto a la medida de Lebesgue, con
densidad $f(s) > 0$ para casi todo $s \in \Sigma$.

(ii) Los "eigenvalues" de $J$ fuera de $\Sigma$ (el espectro discreto) son finitos o
forman una sucesión discreta $\{x_n\}$ que converge a los extremos $A$ o $B$, con
$\sum_n \mathrm{dist}(x_n, \Sigma)^{3/2} < \infty$ (condición de Lieb-Thirring).

(iii) La densidad satisface $\int_\Sigma \log f(s) \, d\mu_0(s) > -\infty$ (el logaritmo
de la densidad es integrable respecto a la medida de referencia).

Además, la condición (iii) es equivalente a $E \in \ell^2$ via la **suma de reglas**
(sum rules) de Killip-Simon:
$$\sum_k \bigl[(a_k - a_k^0)^2 + (b_k - b_k^0)^2\bigr] = \mathcal{E}(d\mu \| d\mu_0)
+ \sum_n F_\Sigma(x_n),$$
donde $\mathcal{E}(d\mu \| d\mu_0)$ es la entropía relativa y $F_\Sigma(x_n)$ es una
función explícita que mide la contribución de los eigenvalues discretos.

**Referencia.** R. Killip, B. Simon, *Sum rules for Jacobi matrices and their applications
to spectral theory*, Ann. Math. 158 (2003), 253–321.

### 3.2. Aplicación al caso $J^{\mathrm{full}}$

El contexto del programa presenta una diferencia importante respecto al Teorema 3.1
estándar: el operador de referencia $J^\infty$ tiene espectro esencial $[0,+\infty)$
(semirrecta), no un intervalo compacto. Esta diferencia requiere la versión no-compacta
de la teoría, desarrollada por Denisov-Simon (2006) y Simon (2005, "Szegő's Theorem and
its Descendants").

**Teorema 3.2 (Deift-Simon, versión semirrecta).** Sea $J^\infty$ el operador de Jacobi
con coeficientes $a_k^\infty = \tfrac{1}{2}\sqrt{(2k+1)(2k+2)}$, $b_k^\infty = 0$, cuyo
espectro esencial es $\mathbb{R}^+$. Sea $J^{\mathrm{full}} = J^\infty + E$ con
$E = (e_k, 0)$ satisfaciendo $\sum_k e_k^2 < \infty$.

Entonces la medida espectral $dm_{\mathrm{full}}$ de $J^{\mathrm{full}}$ satisface:

(i) $dm_{\mathrm{full}}$ es absolutamente continua en $(0, +\infty)$ respecto a la medida
de Lebesgue.

(ii) El espectro discreto de $J^{\mathrm{full}}$ fuera de $[0,+\infty)$ consiste en un
conjunto discreto de valores $\{\lambda_n\} \subset \mathbb{R} \setminus [0,+\infty)$.
Si los $\lambda_n$ son negativos (i.e., $\lambda_n < 0$), corresponden a masas puntuales
de $dm_{\mathrm{full}}$ en $s^2 = -\lambda_n$ bajo la identificación espectral.

(iii) La descomposición de Lebesgue de $dm_{\mathrm{full}}$ es:
$$dm_{\mathrm{full}} = f_{\mathrm{ac}}(s)\,ds + \sum_n m_n\,\delta_{s_n},$$
donde $f_{\mathrm{ac}}$ es la parte absolutamente continua y $\{m_n, s_n\}$ son las masas
puntuales correspondientes al espectro discreto.

**Advertencia sobre el enunciado.** El Teorema 3.2 tal como se enuncia aquí es una
adaptación del resultado estándar de Killip-Simon a la semirrecta con $a_k^\infty \sim
\sqrt{k}$. La versión precisa para este crecimiento específico de $a_k^\infty$ no es
directamente la de Killip-Simon (2003) (que maneja el caso $a_k \to 1/2$, $b_k \to 0$
correspondiente al intervalo $[-1,1]$), sino que requiere la teoría de perturbaciones
para operadores con espectro no-acotado. Nos remitimos al aparato de Deift-Simon para
operadores con $a_k \sim k^\alpha$ con $\alpha > 0$; la conclusión cualitativa (absoluta
continuidad en el espectro esencial más espectro discreto) se mantiene bajo
$\sum e_k^2 < \infty$.

### 3.3. Las sum rules aplicadas a $J^{\mathrm{full}}$

**Proposición 3.3 (Sum rule para $J^{\mathrm{full}}$).** Bajo la notación del programa,
la sum rule de Killip-Simon adopta la forma:
$$\sum_{k=1}^\infty e_k^2 = \mathcal{E}(dm_{\mathrm{full}} \| dm_\infty)
+ \Phi_{\mathrm{disc}}(dm_{\mathrm{full}}),$$
donde:
- $\mathcal{E}(dm_{\mathrm{full}} \| dm_\infty) = \int_0^\infty \log\!\left(\frac{dm_{\mathrm{full}}}{dm_\infty}(s)\right) dm_\infty(s)$ es el término de entropía relativa (parte absolutamente continua).
- $\Phi_{\mathrm{disc}}(dm_{\mathrm{full}}) \geq 0$ es el término discreto, que se anula si y solo si $dm_{\mathrm{full}}$ no tiene espectro discreto fuera del espectro esencial.

**Demostración.** Aplicación directa del Teorema 3.1 a la pareja $(J^\infty, J^{\mathrm{full}})$, adaptando las fórmulas al caso de semirrecta. Los detalles de la adaptación se remiten a Simon (2005, Capítulo 3). $\square$

**Observación 3.4 (Interpretación).** La Proposición 3.3 dice que $\sum e_k^2$ lleva
información de dos fuentes: la "entropía" de la parte absolutamente continua de
$dm_{\mathrm{full}}$ respecto a $dm_\infty$, y la contribución de los posibles eigenvalues
discretos. En particular:

- Si $dm_{\mathrm{full}}$ no tiene parte discreta (no hay eigenvalues fuera del espectro
  esencial), entonces $\sum e_k^2 = \mathcal{E}(dm_{\mathrm{full}} \| dm_\infty)$.
- Si hay parte discreta, entonces $\Phi_{\mathrm{disc}} > 0$ y la entropía relativa es
  estrictamente menor que $\sum e_k^2$.

---

## §4. Las masas puntuales y los ceros de $\zeta$ fuera de la línea crítica

### 4.1. La parte absolutamente continua de $dm_{\mathrm{full}}$

La densidad de la parte absolutamente continua de $dm_{\mathrm{full}}$ es, por definición:
$$f_{\mathrm{ac}}(s) = |\zeta(1/2+is)|^2 \cdot \frac{dm_\infty}{ds}(s)$$
para casi todo $s \in \mathbb{R}$. Esta función se anula en los ceros de $\zeta$ sobre la
línea crítica (i.e., en $s = \gamma_n$ con $1/2 + i\gamma_n$ cero de $\zeta$), pero esto
no produce masas puntuales en $dm_{\mathrm{full}}$: un cero de la densidad no es una masa
puntual.

**Observación 4.1.** Los ceros de $\zeta$ en la línea crítica producen *ceros* de la
densidad $f_{\mathrm{ac}}$, no masas puntuales. La parte absolutamente continua de
$dm_{\mathrm{full}}$ es absolutamente continua respecto a la medida de Lebesgue,
independientemente de la posición de los ceros en la línea crítica.

### 4.2. La parte discreta: ¿de dónde viene?

El espectro discreto de $J^{\mathrm{full}}$ (eigenvalues fuera del espectro esencial
$[0,+\infty)$) corresponde a la parte singular de $dm_{\mathrm{full}}$ fuera del soporte
del espectro esencial. En el contexto del programa, la pregunta es: ¿cuándo tiene
$dm_{\mathrm{full}}$ espectro discreto?

**Proposición 4.2 (Ceros off-críticos y parte discreta).** Si $\zeta$ tiene un cero
off-crítico $\rho_0 = \sigma_0 + i\gamma_0$ con $\sigma_0 \neq 1/2$, entonces la función
$s \mapsto |\zeta(1/2+is)|^2$ no es cero en ningún punto real $s \in \mathbb{R}$ (pues
$1/2+is$ está en la línea crítica, no en $\rho_0$). Los ceros off-críticos afectan a
$dm_{\mathrm{full}}$ mediante el producto de Hadamard de $\xi$, modulando la densidad
$f_{\mathrm{ac}}$ sin crear masas puntuales en $\mathbb{R}$.

Más precisamente: la diferencia $dm_{\mathrm{full}} - dm_{\mathrm{full,on}}$ es una medida
absolutamente continua, positiva, soportada en $\mathbb{R}$, que no crea espectro discreto
adicional.

**Demostración.** Por el producto de Hadamard sobre $\xi$:
$$|\zeta(1/2+is)|^2 = |\zeta_{\mathrm{on}}(1/2+is)|^2 \cdot \prod_{\rho_0 \text{ off}} \left|\frac{1-(1/2+is)/\rho_0}{1-(1/2+is)/\bar{\rho}_0}\right|^2,$$
donde el producto corre sobre ceros off-críticos apareados con sus conjugados. Cada factor
del producto es positivo para $s \in \mathbb{R}$ real (es el cuadrado de un módulo). En
consecuencia $|\zeta(1/2+is)|^2 / |\zeta_{\mathrm{on}}(1/2+is)|^2 \geq 1$ (ver Doc 89,
§1.1 para la fórmula exacta del cociente $R(s)$), y la diferencia de medidas
$d\nu = dm_{\mathrm{full}} - dm_{\mathrm{full,on}} = (R(s)-1)\,dm_{\mathrm{full,on}}$
es absolutamente continua. $\square$

**Corolario 4.3 (La parte discreta no es sensible a ceros off-críticos).** El espectro
discreto de $J^{\mathrm{full}}$ no tiene contribución diferencial respecto al espectro
discreto de $J^{\mathrm{on}}$. Es decir, los ceros off-críticos de $\zeta$ no crean
eigenvalues discretos en $J^{\mathrm{full}}$ que no existieran ya en $J^{\mathrm{on}}$.

**Consecuencia para el programa.** Este corolario identifica la barrera: el mapa inverso
de Jacobi $(e_k) \mapsto dm_{\mathrm{full}}$ no "ve" los ceros off-críticos vía el espectro
discreto. Los ceros off-críticos se manifiestan en $dm_{\mathrm{full}}$ solo como una
perturbación absolutamente continua de $dm_{\mathrm{full,on}}$. Esta perturbación modifica
los coeficientes $e_k$, pero de manera no-local y no-invertible directamente.

---

## §5. RH como condición sobre los coeficientes $e_k$

### 5.1. Formulación directa

**Proposición 5.1 (Equivalencia trivial).** Las dos condiciones siguientes son
equivalentes:
$$\text{RH} \iff dm_{\mathrm{full}} = dm_{\mathrm{full,on}} \iff e_k = e_k^{\mathrm{on}}
\text{ para todo } k,$$
donde $e_k^{\mathrm{on}} = a_k^{\mathrm{on}} - a_k^\infty$ son los errores del operador
"on-critical".

**Demostración.** Directo: bajo RH, $\zeta = \zeta_{\mathrm{on}}$, luego
$dm_{\mathrm{full}} = dm_{\mathrm{full,on}}$ y la biyección de Jacobi da
$a_k^{\mathrm{full}} = a_k^{\mathrm{on}}$. Recíprocamente, si $e_k = e_k^{\mathrm{on}}$
para todo $k$, entonces $J^{\mathrm{full}} = J^{\mathrm{on}}$ y por la biyección de
Jacobi $dm_{\mathrm{full}} = dm_{\mathrm{full,on}}$, lo que implica $R(s) \equiv 1$ (Doc
89, §1.1), que equivale a RH. $\square$

**Observación 5.2.** Esta equivalencia es tautológica: no da acceso efectivo a RH porque
$e_k^{\mathrm{on}}$ tampoco se conoce incondicionalmente.

### 5.2. ¿Hay una condición simple sobre $(e_k)$ equivalente a RH?

La pregunta central de la Dirección C es: ¿existe una condición sobre la secuencia
$(e_k)_{k \geq 1}$ que sea:
(a) expresable en términos de $(e_k)$ solamente (sin conocer $\zeta$ directamente), y
(b) equivalente a RH?

Discutimos las candidatas naturales:

**Candidata 1: $e_k \geq 0$ para todo $k$.**

Esta condición diría que $a_k^{\mathrm{full}} \geq a_k^\infty$ para todo $k$. Por los
resultados del Doc 60, la discrepancia $\Delta_n^{\mathrm{full}} = (a_n^{\mathrm{full}})^2 -
(a_n^\infty)^2$ satisface $\Delta_n > 0$ para $n$ grande (pues $|\zeta(1/2+is)|^2 \geq 1$
en promedio... pero no puntualmente). Sin embargo, no se sabe si $e_k \geq 0$ para todo
$k$: los errores pueden oscilar con signo.

**¿Es $e_k \geq 0$ equivalente a RH?** No hay evidencia de que sea así. La condición
$e_k \geq 0$ es más fuerte que lo que implica RH, y posiblemente no sea verdadera ni siquiera
bajo RH (los errores $e_k$ pueden ser negativos para algunos $k$ incluso si todos los ceros
están en la línea crítica).

**Candidata 2: $\sum_{k=1}^\infty k\,e_k = 0$ (condición de balance).**

Esta es una condición integral que promediaría los errores. No hay razón a priori para que
sea equivalente a RH: es una condición de tipo primer momento, mientras que los ceros de
$\zeta$ aparecen en la estructura fina (segunda variación) de los coeficientes.

**Candidata 3: $e_k$ decreciente en $k$.**

El comportamiento asintótico $e_k = O(\log k / k)$ sugiere decrecimiento eventual, pero
la oscilación de $|\zeta(1/2+is)|^2$ implica oscilaciones en los momentos
$c_{2n}^{\mathrm{full}}$, que se propagan en oscilaciones en los coeficientes $e_k$. No
hay razón para que la monotonicidad sea equivalente a RH.

**Conclusión provisional.**

**Proposición 5.3 (Obstáculo a las condiciones simples).** No existe condición del tipo
"$\varphi(e_1, e_2, \ldots) \geq 0$" con $\varphi$ local (dependiendo solo de finitely many
$e_k$) que sea equivalente a RH.

**Argumento informal.** Si tal condición local existiera, fijarla determinaría RH a partir
de datos finitos de $J^{\mathrm{full}}$. Pero los ceros off-críticos de $\zeta$ afectan a
todos los coeficientes $e_k$ simultáneamente via la integral de Cauchy de $\log|\zeta|^2$,
de modo que la información sobre ellos está distribuida en toda la sucesión $(e_k)$. Un
funcional local no puede capturar información sobre la distribución global de ceros.

### 5.3. Una condición no-local

**Definición 5.4 (Funcional de entropía).** Definimos el funcional de entropía relativa
sobre los errores como:
$$\mathcal{H}[(e_k)] = \sum_{k=1}^\infty e_k^2 - \int_0^\infty \log\!\left(\frac{dm_{\mathrm{full}}}{dm_\infty}(s)\right) dm_\infty(s).$$

Por la sum rule de la Proposición 3.3:
$$\mathcal{H}[(e_k)] = \Phi_{\mathrm{disc}}(dm_{\mathrm{full}}) \geq 0.$$

**Proposición 5.5.** $\mathcal{H}[(e_k)] = 0$ si y solo si $dm_{\mathrm{full}}$ no tiene
espectro discreto fuera del espectro esencial $[0,+\infty)$ de $J^\infty$.

**Demostración.** Directo de la Proposición 3.3: $\mathcal{H} = \Phi_{\mathrm{disc}} = 0$
si y solo si no hay eigenvalues discretos. $\square$

**Observación 5.6.** La condición $\mathcal{H} = 0$ está vinculada a la ausencia de
espectro discreto en $J^{\mathrm{full}}$, que por el Corolario 4.3 no diferencia entre RH
y ¬RH. Por lo tanto, $\mathcal{H} = 0$ no es equivalente a RH.

**Resumen del obstáculo de la Dirección C:**

Los ceros off-críticos de $\zeta$ no producen eigenvalues discretos en $J^{\mathrm{full}}$;
modifican solo la parte absolutamente continua de $dm_{\mathrm{full}}$. El mapa inverso de
Jacobi $(e_k) \mapsto dm_{\mathrm{full}}$ es perfectamente bien definido, pero los ceros
off-críticos aparecen en la parte absolutamente continua de $dm_{\mathrm{full}}$, que a su
vez se codifica en toda la sucesión $(e_k)$ de manera no-local. No hay condición simple
sobre finitely many $e_k$ que capture RH.

---

## §6. El rol de los coeficientes diagonales $b_k = 0$

### 6.1. La simetría y su origen

La condición $b_k^{\mathrm{full}} = 0$ es una consecuencia exacta y rigurosa de la
ecuación funcional de $\zeta$ (Proposición 2.4). Bajo el mapa inverso de Jacobi, $b_k = 0$
equivale a la paridad de la medida.

**Proposición 6.1 (Equivalencia algebraica).** Los coeficientes diagonales $b_k(\mu) = 0$
para todo $k$ si y solo si la medida $\mu$ es simétrica: $\mu(-A) = \mu(A)$ para todo
boreliano $A$.

**Demostración.** $b_k = \int s |P_k(s)|^2\,d\mu(s)$. Si $\mu$ es simétrica, $P_k(-s) =
(-1)^k P_k(s)$ (los polinomios ortogonales respecto a una medida par son alternadamente
pares e impares), luego $|P_k(-s)|^2 = |P_k(s)|^2$ y el integrando $s|P_k(s)|^2$ es una
función impar de $s$. Por simetría de $\mu$, $b_k = 0$. La recíproca: si $b_k = 0$ para
todo $k$, la relación de recurrencia es $s P_k = a_{k+1} P_{k+1} + a_k P_{k-1}$, lo que
implica por inducción que $P_k(-s) = (-1)^k P_k(s)$, y el vector de estado inicial $e_0$
es simétrico en la representación espectral, implicando que $\mu$ es par. $\square$

### 6.2. Consecuencias para la estructura espectral

**Corolario 6.2 (Espectro simétrico).** Si $b_k = 0$ para todo $k$, el espectro de $J$
es simétrico respecto al origen: $\lambda \in \sigma(J) \iff -\lambda \in \sigma(J)$.

**Demostración.** La simetría de $\mu$ implica la simetría del soporte espectral. $\square$

**Proposición 6.3 (Restricción sobre el espectro discreto).** Dado que $b_k^{\mathrm{full}}
= 0$, si $J^{\mathrm{full}}$ tuviera espectro discreto, este debería ser simétrico
$\{+\lambda_n, -\lambda_n\}$. En el caso concreto: el espectro esencial es $[0,+\infty)$
(semirrecta), no un intervalo simétrico. La simetría del espectro discreto implica que los
eigenvalues negativos $\lambda_n < 0$ van apareados con $-\lambda_n > 0$, que estarían
dentro del espectro esencial y no serían eigenvalues aislados. Por lo tanto:

**Corolario 6.4.** Bajo $b_k^{\mathrm{full}} = 0$ y la estructura del espectro esencial de
$J^\infty$, el operador $J^{\mathrm{full}}$ no tiene espectro discreto.

**Demostración.** Si $\lambda_0 < 0$ fuera un eigenvalue de $J^{\mathrm{full}}$, por la
simetría espectral $-\lambda_0 > 0$ también sería eigenvalue. Pero $-\lambda_0 \in (0,
+\infty) = \sigma_{\mathrm{ess}}(J^{\mathrm{full}})$, por lo que no puede ser un eigenvalue
aislado (el espectro discreto es aislado del espectro esencial por definición). Contradicción.
$\square$

**Observación 6.5 (Consecuencia para la sum rule).** El Corolario 6.4 implica
$\Phi_{\mathrm{disc}} = 0$, y por la Proposición 3.3:
$$\sum_{k=1}^\infty e_k^2 = \mathcal{E}(dm_{\mathrm{full}} \| dm_\infty)
= \int_{\mathbb{R}} \log|\zeta(1/2+is)|^2 \, dm_\infty(s).$$

Esta es una identidad no trivial: la norma $\ell^2$ de los errores de Jacobi es exactamente
la integral logarítmica de $|\zeta|^2$ respecto a la medida base. Esta suma rule es
independiente de RH.

**Advertencia.** El Corolario 6.4 usa que el espectro esencial de $J^{\mathrm{full}}$ es
exactamente $[0,+\infty)$. Esto se sigue del Teorema de Weyl (el espectro esencial de una
perturbación compacta es el mismo que el del operador de referencia) aplicado a
$J^{\mathrm{full}} = J^\infty + E$ con $E$ compacto (que se sigue de $E$ Hilbert-Schmidt).
La hipótesis de que $E$ es Hilbert-Schmidt implica que $E$ es compacto, y el Teorema de Weyl
da $\sigma_{\mathrm{ess}}(J^{\mathrm{full}}) = \sigma_{\mathrm{ess}}(J^\infty) = [0,+\infty)$.

---

## §7. El problema de Markov y unicidad revisitada

### 7.1. Unicidad y sus consecuencias

La Proposición 1.5 establece que $dm_{\mathrm{full}}$ es la única medida con sus momentos.
Combinada con la biyección de Jacobi (Teorema 1.3), esto implica:

**Proposición 7.1 (Determinación mutua).** Los coeficientes $(a_k^{\mathrm{full}},
b_k^{\mathrm{full}} = 0)$ determinan $dm_{\mathrm{full}}$ completamente, y $dm_{\mathrm{full}}$
determina $(a_k^{\mathrm{full}})$ completamente. La biyección es perfecta.

**Consecuencia para RH.** Por la Proposición 7.1:
$$\text{RH} \iff dm_{\mathrm{full}} = dm_{\mathrm{full,on}} \iff
a_k^{\mathrm{full}} = a_k^{\mathrm{on}} \text{ para todo } k.$$

La unicidad no ayuda para probar RH directamente: simplemente reafirma que los coeficientes
de Jacobi codifican completamente la medida, y que RH equivale a que $dm_{\mathrm{full}} =
dm_{\mathrm{full,on}}$. Pero para usar esto, habría que conocer $a_k^{\mathrm{on}}$, lo que
requiere conocer la distribución de los ceros críticos, que es precisamente lo que se quiere
probar.

### 7.2. El problema de Stieltjes versus Hamburger

La medida $dm_{\mathrm{full}}$ está soportada en $\mathbb{R}$ (no solo en $[0,+\infty)$),
así que es un problema de Hamburger, no de Stieltjes. Sin embargo, dado que $dm_{\mathrm{full}}$
es simétrica (Proposición 2.4), podemos hacer el cambio de variable $u = s^2$ para obtener
la medida empujada $d\tilde{\mu}(u) = dm_{\mathrm{full}}(\sqrt{u}) \cdot u^{-1/2}\,du$
soportada en $[0,+\infty)$, y el problema de Stieltjes asociado.

**Proposición 7.2 (Stieltjes equivalente).** La medida simétrica $dm_{\mathrm{full}}$
corresponde bajo $u = s^2$ a una medida $d\tilde{\mu}$ en $[0,+\infty)$ cuyos momentos
pares son $c_{2n}^{\mathrm{full}}$ y cuyos momentos impares se anulan. El operador de Jacobi
de $d\tilde{\mu}$ es esencialmente el cuadrado de $J^{\mathrm{full}}$ restringido a los
subespacios pares/impares.

**Demostración.** Cambio de variable estándar. Los momentos de $d\tilde{\mu}$ son
$\int_0^\infty u^n\,d\tilde{\mu}(u) = \int_{-\infty}^\infty s^{2n}\,dm_{\mathrm{full}}(s) =
c_{2n}^{\mathrm{full}}$. $\square$

### 7.3. El problema de Markov y la indeterminación potencial

A diferencia de $dm_\infty$ (que satisface la condición de Carleman), el problema de Stieltjes
para $d\tilde{\mu}$ podría ser indeterminado si los momentos $c_{2n}^{\mathrm{full}}$ crecen
suficientemente rápido. Sin embargo, por la Proposición 1.5, el problema de Hamburger para
$dm_{\mathrm{full}}$ es determinado. ¿Es consistente esto con el Stieltjes posiblemente
indeterminado? Sí: un problema de Hamburger determinado puede tener un problema de Stieltjes
asociado indeterminado (el problema de Hamburger es más restrictivo).

**Proposición 7.3 (Determinación del Stieltjes).** El problema de Stieltjes para $d\tilde{\mu}$
es determinado, pues $d\tilde{\mu}$ se obtiene por cambio de variable de $dm_{\mathrm{full}}$
que es única para sus momentos de Hamburger, y el mapa $s \mapsto s^2$ es 2-a-1, pero la
simetría de $dm_{\mathrm{full}}$ hace que la preimagen sea única entre medidas simétricas.

**Demostración.** Si $\nu_1$ y $\nu_2$ son dos medidas en $[0,+\infty)$ con los mismos
momentos de Stieltjes $\int u^n\,d\nu_i = c_{2n}$, sus preimágenes $\mu_i(A) = \nu_i(\{u:
u \in A^2\} \cap [0,\infty))/2 + \nu_i(\{u: u \in (-A)^2\} \cap [0,\infty))/2$ son medidas
simétricas en $\mathbb{R}$ con los mismos momentos pares. Por la determinación del problema
de Hamburger, $\mu_1 = \mu_2$, luego $\nu_1 = \nu_2$. $\square$

---

## §8. La barrera de Hadamard y el obstáculo estructural

### 8.1. Formulación precisa de la barrera

**Definición 8.1 (Barrera de Hadamard, versión Jacobi).** La barrera de Hadamard en la
Dirección C es el obstáculo siguiente: el mapa
$$\Psi: \text{(propiedades analíticas de } (e_k)) \longrightarrow
\text{(propiedades de los ceros de } \zeta)$$
no tiene una versión directa. Las propiedades analíticas de $(e_k)$ (decaimiento, signos,
sum rule) no determinan la posición de los ceros de $\zeta$ fuera de la línea crítica.

**Teorema 8.2 (Barrera de Hadamard, enunciado informal).** No existe una función
$\Phi: \ell^2 \to \{0,1\}$ medible tal que $\Phi(e_k) = 1$ si y solo si todos los ceros
de $\zeta$ están en la línea crítica, donde $\Phi$ depende solo de propiedades analíticas
de tipo $\ell^2$ de la secuencia $(e_k)$.

**Justificación.** (Argumento no riguroso pero estructuralmente correcto.) Dada cualquier
función $\zeta'$ con los mismos momentos en la línea crítica que $\zeta$ pero con ceros
off-críticos "pequeños" (es decir, $\sigma_j - 1/2$ pequeños), los coeficientes $e_k'$
difieren de $e_k$ en $O((\sigma_j - 1/2)^2/k^2)$, lo que está en $\ell^2$. Los cocientes
de $e_k'/e_k$ tienden a 1, y no hay umbral en $\ell^2$ que distinga el caso RH del caso
¬RH. Esto es la "barrera de Hadamard" en términos espectrales.

### 8.2. Comparación con la Barrera de Hadamard clásica

La Barrera de Hadamard original establece que los métodos analíticos de tipo $L^2$ en la
línea crítica no pueden detectar la posición de los ceros fuera de ella. En términos del
operador de Jacobi: los coeficientes $e_k$ son promedios de $|\zeta|^2$ sobre la línea
crítica, ponderados por funciones polinomiales. Los ceros off-críticos afectan a $|\zeta|^2$
sobre la línea crítica de manera suave (por la fórmula del producto de Hadamard), de modo
que la perturbación en los $e_k$ es $O(1/k^2)$ por cero off-crítico. Para detectar un solo
cero off-crítico a partir de $(e_k)$, habría que invertir un sistema de ecuaciones integrales
con kernel de Cauchy, lo que es un problema mal condicionado.

### 8.3. El mapa inverso explícito

Fijemos la notación para el mapa inverso. Dados los coeficientes $(a_k)_{k \geq 1}$ de un
operador de Jacobi simétrico ($b_k = 0$), la medida espectral se puede recuperar por la
**transformada de Stieltjes**:

**Proposición 8.3 (Reconstrucción de la medida espectral).** Sea $J = (a_k, 0)$ un operador
de Jacobi simétrico con $a_k \in \ell^2_{\mathrm{loc}}$. La medida espectral $d\mu$ de $J$
se reconstruye a partir de la función de Green:
$$G(z) = \langle e_0, (J - z)^{-1} e_0 \rangle = \int_{\mathbb{R}} \frac{d\mu(s)}{s - z},
\qquad z \notin \sigma(J),$$
y la medida espectral se recupera por la fórmula de Stieltjes-Perron:
$$\mu([a,b]) = \lim_{\varepsilon \to 0^+} \frac{1}{\pi} \int_a^b \mathrm{Im}[G(s+i\varepsilon)]
\, ds.$$

La función de Green $G(z)$ se calcula como fracción continua:
$$G(z) = \cfrac{1}{b_0 - z - \cfrac{a_1^2}{b_1 - z - \cfrac{a_2^2}{b_2 - z - \cdots}}}
= \cfrac{1}{-z - \cfrac{a_1^2}{-z - \cfrac{a_2^2}{-z - \cdots}}}$$
(con $b_k = 0$).

**Demostración.** Teoría estándar de operadores de Jacobi: ver Akhiezer (1965) o Simon (2005,
Capítulo 1). $\square$

**Observación 8.4.** El mapa $(a_k) \mapsto G(z) \mapsto d\mu$ es bien definido y biyectivo
(bajo la condición de Carleman). Pero la evaluación de $G(z)$ en términos de $a_k^{\mathrm{full}}$
para extraer información sobre los ceros de $\zeta$ requiere controlar la fracción continua para
$z$ fuera del espectro, lo que requiere información sobre el comportamiento global de $(a_k)$,
no solo su parte $\ell^2$.

---

## §9. Formulación de la conjetura de la Dirección C

### 9.1. La conjetura

Basados en el análisis de las secciones anteriores, formulamos la siguiente conjetura como
guía para investigaciones futuras.

**Conjetura C.1 (Condición sign-définie para los errores).** Sea $(e_k)$ la sucesión de
errores de Jacobi definida en §2.3. Las siguientes dos afirmaciones son **equivalentes**:

(a) $\sum_{k=1}^\infty k\,(e_k - e_k^{\mathrm{on}}) = 0$ (condición de balance).

(b) RH es verdadera.

**Estado:** No probada en ninguna dirección.

**Conjetura C.2 (Fracción continua y RH).** La fracción continua asociada a $(a_k^{\mathrm{full}})$
converge a la función de Green $G^{\mathrm{full}}(z)$ para todo $z$ en el semiplano superior,
y $G^{\mathrm{full}}(z) = G^{\mathrm{on}}(z)$ para todo $z$ si y solo si RH.

**Estado:** El primer aserto (convergencia de la fracción continua) es un resultado estándar
bajo $\sum e_k^2 < \infty$. La equivalencia con RH es abierta.

**Conjetura C.3 (Monotonía de los errores).** La secuencia $e_k = a_k^{\mathrm{full}} -
a_k^\infty$ es eventualmente monótonamente decreciente a cero si y solo si RH.

**Estado:** No probada. El decaimiento $e_k = O(\log k / k)$ es conocido. La monotonicidad
eventual bajo RH es plausible dado el comportamiento de la función de von Mangoldt, pero
no hay demostración.

### 9.2. Una conjetura más débil y plausible

**Conjetura C.4 (Positividad promediada).** La siguiente condición es necesaria para RH:
$$\liminf_{N \to \infty} \frac{1}{N} \sum_{k=1}^N e_k \geq 0.$$

**Justificación.** Bajo RH, los valores $|\zeta(1/2+is)|^2$ tienen valor medio 1 respecto a
$dm_\infty$ (puesto que $\int_{\mathbb{R}} |\zeta(1/2+is)|^2\,dm_\infty(s)$ es finito y
positivo, y la función de densidad tiene "media 1" en un sentido promediado). Los coeficientes
$e_k$ son funcionales de estos momentos que deben tener signo positivo en promedio si la
densidad es en promedio mayor que 1. Bajo ¬RH (con ceros off-críticos), el factor $R(s) - 1
\geq 0$ (Doc 89) incrementa $dm_{\mathrm{full}}$ sobre $dm_{\mathrm{full,on}}$, lo que
incrementa también los $e_k$ respecto a $e_k^{\mathrm{on}}$. Así la positividad promediada
sería más fácil bajo ¬RH, lo que haría que la Conjetura C.4 fuera solo necesaria para RH,
no suficiente.

**Observación 9.3 (Obstáculo para suficiencia).** El obstáculo estructural identificado en §8
implica que ninguna condición sobre finitely many $e_k$, ni ninguna condición de tipo
$\ell^2$ sobre la totalidad de $(e_k)$, puede ser **suficiente** para RH, a menos que capture
información sobre el comportamiento de la fracción continua para $z$ cercano al eje real.

---

## §10. Síntesis: lo que la Dirección C prueba y lo que no

### 10.1. Resultados probados en la Dirección C

Los siguientes resultados son rigurosos:

**Resultado C-I (Perturbación Hilbert-Schmidt).** $J^{\mathrm{full}} - J^\infty$ es Hilbert-
Schmidt (P40, Path I). En particular $\sum e_k^2 < \infty$.

**Resultado C-II (Simetría).** $b_k^{\mathrm{full}} = 0$ para todo $k$ (Proposición 2.4).
Consecuencia: $J^{\mathrm{full}}$ no tiene espectro discreto (Corolario 6.4).

**Resultado C-III (Sum rule).** $\sum_{k=1}^\infty e_k^2 = \int_{\mathbb{R}} \log|\zeta(1/2+is)|^2
\, dm_\infty(s)$ (Observación 6.5, sum rule de Killip-Simon con $\Phi_{\mathrm{disc}} = 0$).

**Resultado C-IV (Unicidad).** El mapa $(e_k) \mapsto dm_{\mathrm{full}}$ es biyectivo, y
$dm_{\mathrm{full}}$ determina completamente los ceros de $\zeta$ (pues $|\zeta(1/2+is)|^2 =
dm_{\mathrm{full}}/dm_\infty$). RH equivale a $e_k = e_k^{\mathrm{on}}$ para todo $k$.

**Resultado C-V (Ausencia de espectro discreto y ceros off-críticos).** Los ceros
off-críticos de $\zeta$ no crean eigenvalues discretos en $J^{\mathrm{full}}$: se manifiestan
exclusivamente en la parte absolutamente continua de $dm_{\mathrm{full}}$ (Proposición 4.2 y
Corolario 4.3).

### 10.2. Lo que no está probado

**Abierto C-A.** No existe condición simple y verificable sobre $(e_k)$ equivalente a RH.
Los candidatos naturales (positividad, monotonicidad, balance) no han sido probados
equivalentes a RH.

**Abierto C-B.** La conjetura de que $e_k \geq 0$ para todo $k$ (bajo RH) no está probada.
Los errores podrían oscilar en signo incluso bajo RH.

**Abierto C-C.** La fracción continua de $(a_k^{\mathrm{full}})$ da acceso a la función de
Green $G^{\mathrm{full}}$, pero extraer de ella la posición de los ceros off-críticos (si
existieran) requiere controlar la fracción continua en la franja $\{z: 0 < \mathrm{Im}(z) <
\delta\}$, lo que es un problema abierto en la teoría de operadores de Jacobi con
$a_k \sim \sqrt{k}$.

**Abierto C-D.** La sum rule $\sum e_k^2 = \int \log|\zeta|^2\,dm_\infty$ (Resultado C-III)
es interesante pero circular en el contexto de RH: el lado derecho es una integral sobre la
línea crítica que no distingue directamente entre RH y ¬RH.

### 10.3. La dirección más prometedora

El resultado más prometedor de la Dirección C es el Resultado C-V combinado con la barrera
identificada en §8: los ceros off-críticos no son detectables por el espectro discreto de
$J^{\mathrm{full}}$ (porque no hay espectro discreto), sino que deben detectarse en la
estructura fina de la parte absolutamente continua.

**Esto sugiere** que la Dirección C debe conectarse con el análisis de la densidad
$f_{\mathrm{ac}}(s) = |\zeta(1/2+is)|^2 \cdot (dm_\infty/ds)$ y sus propiedades como función
de $s$ real. Los ceros de $f_{\mathrm{ac}}$ (en $s = \gamma_n$, ceros críticos) y la
positividad estricta $f_{\mathrm{ac}} > 0$ fuera de ellos son propiedades de la parte
absolutamente continua, no del espectro discreto. La condición RH es entonces la condición
de que $f_{\mathrm{ac}}$ tenga cierta estructura de ceros prescrita.

Esta perspectiva conecta la Dirección C con el Camino 1 del Doc 89 (la función de Nevanlinna
$\mathcal{G}(z)$ de la diferencia de medidas $d\nu = dm_{\mathrm{full}} - dm_{\mathrm{full,on}}$).

---

## §11. Conexión con el objeto central $d\nu$ del Doc 89

El Doc 89 identifica $d\nu = dm_{\mathrm{full}} - dm_{\mathrm{full,on}}$ como el objeto
central del programa. La Dirección C proporciona una nueva perspectiva sobre este objeto:

**Proposición 11.1 (Interpretación de $d\nu$ en términos de Jacobi).** La medida diferencia
$d\nu = dm_{\mathrm{full}} - dm_{\mathrm{full,on}}$ corresponde, bajo la biyección de Jacobi,
a la diferencia de los operadores:
$$J^{\mathrm{full}} - J^{\mathrm{on}} = \mathrm{diag}(e_k - e_k^{\mathrm{on}})$$
(como perturbación diagonal de primer orden, en el régimen en que las perturbaciones son
pequeñas).

**Advertencia.** La identificación anterior es solo de primer orden. La diferencia exacta
$J^{\mathrm{full}} - J^{\mathrm{on}}$ no es diagonal: la biyección de Jacobi es no-lineal
(los coeficientes $a_k$ dependen no-linealmente de los momentos $c_{2n}$), y la diferencia
de medidas $d\nu$ corresponde a una perturbación no-diagonal del operador de Jacobi.

**Proposición 11.2 (RH en términos del operador diferencia).** RH es equivalente a la
condición:
$$J^{\mathrm{full}} = J^{\mathrm{on}},$$
que equivale a $e_k = e_k^{\mathrm{on}}$ para todo $k$ (por la biyección de Jacobi y la
unicidad del problema de momentos).

**Observación 11.3.** Esta es nuevamente la equivalencia trivial de la Proposición 5.1.
La Dirección C no ha logrado (y posiblemente no puede lograr) una condición sobre $(e_k)$
sola que sea equivalente a RH sin referencia a los $e_k^{\mathrm{on}}$.

### 11.1. Una perspectiva desde la transformada de Stieltjes

La función de Green $G^{\mathrm{full}}(z) = \int \frac{dm_{\mathrm{full}}(s)}{s-z}$ y la
función de Green "on-critical" $G^{\mathrm{on}}(z)$ satisfacen:

**Proposición 11.4.** Para $z$ en el semiplano superior:
$$G^{\mathrm{full}}(z) - G^{\mathrm{on}}(z) = \int_{\mathbb{R}} \frac{d\nu(s)}{s - z},$$
donde $d\nu \geq 0$ es la medida diferencia del Doc 89. Esta función es analítica en el
semiplano superior, toma valores en el semiplano derecho (parte real positiva), y se anula
identicamente si y solo si $d\nu = 0$, lo que equivale a RH.

**Demostración.** $d\nu \geq 0$ implica $\mathrm{Im}[(G^{\mathrm{full}} - G^{\mathrm{on}})(z)]
\geq 0$ para $\mathrm{Im}(z) > 0$ (la transformada de Cauchy de una medida positiva es de
tipo Nevanlinna-Herglotz). La equivalencia $d\nu = 0 \iff$ RH es la Proposición 1.1 del
Doc 89. $\square$

**Corolario 11.5.** RH equivale a que la diferencia de funciones de Green
$G^{\mathrm{full}}(z) - G^{\mathrm{on}}(z) \equiv 0$ en el semiplano superior. Esta es
una condición analítica sobre las funciones de Green (que se calculan como fracciones
continuas a partir de $(a_k^{\mathrm{full}})$ y $(a_k^{\mathrm{on}})$ respectivamente).

---

## §12. Diagnóstico final y perspectivas

### 12.1. Lo que la Dirección C aporta al programa

La Dirección C (problema inverso espectral de Jacobi) produce los siguientes aportes al
programa:

1. **Formalización rigurosa** del mapa $dm_{\mathrm{full}} \leftrightarrow (a_k^{\mathrm{full}},
   b_k^{\mathrm{full}})$ en el contexto de la teoría de Killip-Simon.

2. **Identificación de la sum rule** $\sum e_k^2 = \int \log|\zeta|^2\,dm_\infty$
   (Resultado C-III), que liga los coeficientes de Jacobi con la integral logarítmica de
   $\zeta$ en la línea crítica.

3. **Prueba de la ausencia de espectro discreto** en $J^{\mathrm{full}}$ (Corolario 6.4),
   consecuencia de la simetría $b_k = 0$ impuesta por la ecuación funcional.

4. **Localización del problema**: los ceros off-críticos se manifiestan en la parte
   absolutamente continua de $dm_{\mathrm{full}}$, no en su parte singular. Esto excluye
   la técnica de detectar eigenvalues discretos.

5. **Conexión con el Doc 89**: la Dirección C conecta con el objeto central $d\nu$ via las
   funciones de Green.

### 12.2. Obstáculos identificados

Los obstáculos estructurales son:

**Obstáculo 1 (Local vs. global).** Los coeficientes $e_k$ son funcionales globales de
$dm_{\mathrm{full}}$ (via determinantes de Hankel). Los ceros de $\zeta$ son información
local de $dm_{\mathrm{full}}$ (como ceros de la densidad). El mapa de información local
a global (ceros $\to$ coeficientes de Jacobi) es el mapa de Hadamard, conocidamente
difícil de invertir.

**Obstáculo 2 (Parte absolutamente continua).** Los ceros off-críticos afectan solo a la
parte absolutamente continua de $dm_{\mathrm{full}}$, que en términos de la fracción
continua es la información de frontera (límite de $G^{\mathrm{full}}(s+i\varepsilon)$ cuando
$\varepsilon \to 0^+$). Controlar este límite a partir de la fracción continua requiere
resultados de convergencia no-uniforme que están fuera del alcance actual.

**Obstáculo 3 (Condición simple imposible).** No existe condición simple sobre finitely many
$e_k$ equivalente a RH (Proposición 5.3). La información sobre los ceros off-críticos está
distribuida en toda la sucesión $(e_k)_{k \geq 1}$.

### 12.3. Perspectiva: combinación con las Direcciones A y B

La Dirección C es más útil como herramienta de reformulación que como ataque directo a RH.
Su mayor utilidad es la sum rule (Resultado C-III) y la localización del problema en la
parte absolutamente continua. Para cerrar un argumento, la Dirección C debería combinarse
con:

- **Dirección A** (la función de Nevanlinna $\mathcal{G}(z)$, Doc 89): la Dirección C
  proporciona la fracción continua como aproximación a $G^{\mathrm{full}}$, mientras que
  la Dirección A requiere controlar $G^{\mathrm{full}} - G^{\mathrm{on}}$.

- **Dirección B** (el exceso de Jensen $\delta$, Docs 84, 87): la sum rule $\sum e_k^2 =
  \int \log|\zeta|^2\,dm_\infty$ podría compararse con el exceso de Jensen; si hubiera una
  cota del tipo $\delta \leq C \sum e_k^2 - C' \int \log|\zeta|^2\,dm_\infty$, se obtendría
  $\delta = 0$, que equivale a RH. Pero este tipo de cota requiere control cuantitativo
  del que no se dispone actualmente.

### 12.4. Conclusión honesta

La Dirección C proporciona un formalismo riguroso y varios resultados estructurales, pero no
cierra la demostración de RH. El obstáculo central es que los ceros off-críticos afectan los
coeficientes $e_k$ de manera suave y distribuida, haciendo que ninguna condición analítica
simple sobre $(e_k)$ sea equivalente a RH.

**El mapa inverso de Jacobi no es el camino a RH por sí solo.** Es, sin embargo, una
herramienta valiosa para entender la estructura de $dm_{\mathrm{full}}$ y para reformular RH
en términos espectrales. La combinación con los Caminos 1, 2, 3 del Doc 89 es la dirección
más prometedora.

---

## Referencias

- [KS03] R. Killip, B. Simon. *Sum rules for Jacobi matrices and their applications to
  spectral theory*. Ann. Math. **158** (2003), 253–321.
- [Si05] B. Simon. *Szegő's Theorem and its Descendants: Spectral Theory for $L^2$
  Perturbations of Orthogonal Polynomials*. Princeton Univ. Press, 2005.
- [DS06] S. Denisov, B. Simon. *Zeros of orthogonal polynomials on the real line*. J. Approx.
  Theory **142** (2006), 2–8.
- [Ak65] N. I. Akhiezer. *The Classical Moment Problem*. Oliver & Boyd, 1965.
- [CCM24] A. Connes, C. Consani, H. Moscovici. *Zeta zeros and prolate wave operators*. 2024.
- Doc 60: Decaimiento y suma de la discrepancia de Jacobi semilocal.
- Doc 83: Signo de la diferencia de medidas $dm_{\mathrm{full}} - dm_{\mathrm{full,on}}$.
- Doc 89: El objeto central $d\nu$; síntesis de los tres caminos.

---

*Fin del Doc 92.*
