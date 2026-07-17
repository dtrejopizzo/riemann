# Phase 67 — Algebra cuántica q-Pick para Omega_7: ¿contracción algebraica o zeta disfrazada?

**Programa:** Hipótesis de Riemann — Phase 67: álgebra cuántica / q-deformación para el defecto terminal
whitened.
**Fecha:** 2026-07-06.
**Rol del documento:** PROPOSICIÓN AUDITABLE, no prueba. Mandato: bajar a tierra la intuición
"Omega_7 se puede modelar de los dos lados por álgebra cuántica" sin repetir Phase 51
(Bost-Connes/KMS: partición = zeta), Phase 53 (Stone/CCR: producto interno = RH) ni Phase 66
(whitening escalar equivocado).

**Contrato de honestidad.** Este documento no prueba RH. Define una álgebra, las relaciones que deberían
forzar la positividad terminal, y el lugar exacto donde la idea vive o muere. Si el operador primo
queda contractivo sólo porque se eligió una norma/métrica que ya contiene zeta, cae en Phase 51/MW-5.
Si la contractividad sale de relaciones algebraicas q-unitarias independientes de ceros, es un nodo
nuevo.

---

## 0. Veredicto adelantado

> **VEREDICTO PROVISIONAL: CAND-67, vivo sólo como compuerta.** La ruta cuántica que no está ya
> destruida es una ruta de **grupo cuántico / q-deformación**, no KMS ni Weyl-CCR. El candidato
> correcto es una **álgebra q-Pick** en la que:
>
> 1. el jet arquimediano `A_N` sea la forma contravariante positiva de una representación q-unitaria
>    de tipo `U_q(su(1,1))`;
> 2. el **prime current** `B_lambda` se construya canónicamente desde relaciones Hopf-* / Mellin /
>    Euler, antes de mirar el Pick primo;
> 3. el jet primo `P_lambda` aparezca después como el jet de ese current, no como su definición;
> 4. Omega_7 sea exactamente la afirmación de que `B_lambda` es un multiplicador de Schur contractivo:
>    `B_lambda^* B_lambda <= I`;
> 5. el índice `m` sea la mitad del índice negativo de `I - B_lambda^* B_lambda`, equivalente al índice
>    de Jantzen/spectral-flow de la representación al cruzar una pared de unitariedad.
>
> La pieza nueva sería que la positividad no vendría de una métrica zeta-pesada, sino de la
> unitarizabilidad q-algebraica del módulo. La pieza faltante se parte en dos:
>
> **QSC-exist.** Existe un cociclo Mellin-q canónico y un compact quantum group `(A_G,Delta,h)` con
> estado de Haar tal que el current de von Mangoldt es un coeficiente de una corepresentación
> fundamental, y su jet `q->1` da `P_lambda` como salida.
>
> **QSC-contract.** Las relaciones Hopf-* / Peter-Weyl / Haar de ese CQG fuerzan
> `B_lambda^*B_lambda <= I`.
>
> **Corrección E67.2/E67.3.** Los generadores primos **no pueden ser group-like**. Eso preserva Euler,
> pero colapsa al esqueleto Bost-Connes/`\mathbb Q_{>0}^\times` y no aporta contractividad. La
> multiplicatividad de Euler debe vivir en la categoría tensorial/de fusión de corepresentaciones no
> triviales.
>
> **Corrección E67.4/E67.7.** El free product estricto por primos tampoco basta: Haar ortogonaliza
> demasiado y destruye la interferencia que mantiene marginal a `P_lambda`. Woronowicz `F` por sí solo
> no arregla esto; sólo pondera la ortogonalidad. La ruta viva requiere un estado modular coherente
> `omega_{z0,q}` que conserve off-diagonal aritmético y una densidad Haar-dominante `D_{z0,q}` canónica.

Si ambas compuertas se prueban, Omega_7 cae: `delta_N >= 0` para todo `N`. Si fallan, esta phase deja
un detector honesto: los autovalores negativos de `I - B_lambda^*B_lambda` leen `m`, pero no lo anulan.

---

## 1. El objeto que se quiere modelar

La entrada P52/P53 es:

$$
\delta_N =
\lambda_{\min}\!\left(A_N^{-1/2}(A_N-P_\lambda)A_N^{-1/2}\right)
= 1-\lambda_{\max}\!\left(A_N^{-1/2}P_\lambda A_N^{-1/2}\right).
$$

Entonces

$$
\Omega_7:\quad \delta_N\ge 0\ \forall N
\quad\Longleftrightarrow\quad
A_N\succeq P_\lambda\ \forall N
\quad\Longleftrightarrow\quad
\left\|A_N^{-1/2}P_\lambda A_N^{-1/2}\right\|\le 1\ \forall N.
$$

La forma cuántica de esto no debe ser "buscar otra forma positiva". Debe ser:

$$
A_N^{-1/2}P_\lambda A_N^{-1/2} = B_{\lambda,N}^* B_{\lambda,N}
\quad\text{y}\quad
\|B_{\lambda,N}\|\le 1
$$

por una razón estructural. Así:

$$
\delta_N\ge0
\quad\Longleftrightarrow\quad
I-B_{\lambda,N}^*B_{\lambda,N}\succeq0.
$$

El álgebra cuántica tiene que producir `B_lambda` como un **coeficiente matricial de una
corepresentación fundamental de un CQG con Haar** o como un **multiplicador contractivo de una bola de
Schur cuántica con relaciones Hopf-* explícitas**. Esa es la diferencia entre una reformulación y una
palanca.

**Advertencia anti-tautología 1.** La igualdad

$$
A_N^{-1/2}P_\lambda A_N^{-1/2}=B_{\lambda,N}^*B_{\lambda,N}
$$

no tiene contenido por sí sola. Como `P_lambda` es positivo semidefinido, siempre hay una raíz
canónica/Cholesky; existe para zeta, para Davenport-Heilbronn y para cualquier control positivo. Con
ese `B`, la frase

$$
\Omega_7\iff I-B^*B\succeq0
$$

es sólo un renombre de `delta_N`. Por tanto `B_lambda` no puede definirse como una raíz de `P_lambda`.
Debe venir antes: de relaciones Hopf-* / Mellin / Euler. El matching con `P_lambda` es una compuerta
posterior (`QSC-exist`), no una definición.

**Advertencia anti-tautología 2.** "Ser esquina de una unitaria" tampoco basta. Por Sz.-Nagy, toda
contracción tiene una dilatación unitaria, y toda esquina de una unitaria es una contracción. Por tanto

$$
B\ \text{es esquina de una unitaria}\quad\Longleftrightarrow\quad \|B\|\le1
$$

no agrega fuerza. La palanca sólo puede ser más rígida: `B_lambda` debe ser un coeficiente de una
corepresentación fundamental de un **compact quantum group** con coproducto, counidad, antipoda y estado
de Haar; las relaciones de ortogonalidad de Haar/Peter-Weyl sí son estructura extra que una dilatación
Sz.-Nagy genérica no posee.

---

## 2. La álgebra propuesta

### 2.1 Sector arquimediano: `U_q(su(1,1))` + Plancherel/q-Gamma

Tomar `0<q<1`, con `q` como parámetro de deformación/regularización, no como temperatura KMS. Definir
la *-álgebra

$$
\mathcal U_q=\langle K,K^{-1},E,F\rangle
$$

con relaciones

$$
K E K^{-1}=qE,\qquad
K F K^{-1}=q^{-1}F,\qquad
[E,F]=\frac{K^2-K^{-2}}{q-q^{-1}},
$$

y estructura de involución

$$
K^*=K,\qquad E^*=F.
$$

Se usa la serie discreta positiva `D_y^+`, `y>=1/2`, sobre la base `e_0,e_1,...`:

$$
K e_n=q^{n+y}e_n,
$$

$$
E e_n=\sqrt{[n+1]_q[n+2y]_q}\,e_{n+1},\qquad
F e_n=\sqrt{[n]_q[n+2y-1]_q}\,e_{n-1}.
$$

La forma contravariante `H_q` determinada por `E^*=F` es positiva en `D_y^+`, pero un solo kernel
coherente de esta representación sólo da el término de Szego:

$$
A_N \sim \log(t_0/2\pi)\,G_{\mathrm{exact}}(N,y).
$$

Esto fue medido en `E67.1`: el mejor fit es `alpha=1`, `tau=1`, `c=log(t0/2pi)`, con residual de
orden `1/(t0 log t0)`. Por tanto el single coherent kernel es **leading only** y no cierra E67.1.

El objeto correcto para el sector arquimediano completo es la **c-función de Plancherel q-deformada**
(equivalentemente el peso Haar/Plancherel) cuyo factor escalar es `Gamma_q`. En el límite `q->1`,

$$
\Gamma_q(x)\longrightarrow \Gamma(x),\qquad
\psi_q(x):=\frac{d}{dx}\log\Gamma_q(x)\longrightarrow \psi(x).
$$

Insertando `x=s/2`, `s=1/2+iz`, se obtiene el input arquimediano exacto del arnés:

$$
h_{A,q}(z)
= i\left[-\left(\frac1s+\frac1{s-1}\right)+\frac12\log\pi-\frac12\psi_q(s/2)\right]
\longrightarrow
h_A(z).
$$

El factor polar `s(s-1)` está incluido porque P52/h8lab lo incluye en `h_A`; esto sigue siendo
arquimediano y zeta-free.

El jet arquimediano se obtiene de los vectores coherentes/Plancherel en el punto `z_0`. Definir

$$
v_i^{(q)}(z_0):=\left.\nabla_z^i v_z^{(q)}\right|_{z=z_0},\qquad i=0,\dots,N-1,
$$

donde `v_z^(q)` es el vector coherente de la serie discreta positiva y `\nabla_z` es la derivada
covariante Mellin-q compatible con `K`. En el límite renormalizado `q->1`, esta forma debe reproducir
el jet arquimediano P52:

$$
G_N^{(q)}=(\langle v_i^{(q)}(z_0),v_j^{(q)}(z_0)\rangle_{H_q})_{i,j<N}
\longrightarrow A_N.
$$

**Compuerta A (archimedean matching).** Hay que probar, con las entradas de poligamma de
`prop:laguerre-entries`, que el bloque finito de la forma contravariante q-renormalizada da exactamente
`A_N`, no sólo su leading scalar. Esto protege contra el fallo de Phase 66: aquí el whitening es
matricial.

**Estado actual.** `E67.1b` pasa esta compuerta a nivel Gamma_q: los jets de `h_{A,q}` convergen a los
jets exactos `A_N`. `E67.1c` ancla la palabra Plancherel/Haar en la literatura de Fourier transforms
on quantum `SU(1,1)` y spherical Plancherel transforms. Por tanto el sector arquimediano vivo de
CAND-67 es Gamma_q / Haar-Plancherel q-special-function data, no el single coherent kernel. El único
bookkeeping pendiente es dar un q-home explícito a la celda polar `s(s-1)` como la dirección rank-one
`H`.

### 2.2 Sector primo: el current `B_lambda`

Agregar una familia de operadores de desplazamiento aritmético `W_u`, `u in log N`, actuando en la misma
representación por traslaciones q-coherentes. Formalmente:

$$
K W_u K^{-1}=e^{-u/2}W_u,
\qquad
W_u^*=W_{-u}
$$

en la completación de multiplicadores.

El esquema ingenuo sería tomar un generador prime-local group-like `U_p` y formar

$$
J(s)=\sum_{p,k\ge1}(\log p)p^{-ks}U_p^k.
$$

Pero esto es **NO-GO**. Los group-like generan el grupo abeliano libre sobre las primas, es decir
`\mathbb Q_{>0}^\times`; en cualquier representación unitaria sólo dan caracteres/desplazamientos
unitarios. Eso reproduce el producto de Euler escalar, pero deja la contractividad enteramente en los
coeficientes clásicos `p^{-k/2}`. Es Phase 51/Bost-Connes en forma Hopf, no un mecanismo CQG nuevo.

La versión viva reemplaza `U_p` por una corepresentación irreducible no trivial:

$$
u^{(p)}=(u^{(p)}_{ab})_{a,b=1}^{d_p},
\qquad
\Delta(u^{(p)}_{ab})=\sum_c u^{(p)}_{ac}\otimes u^{(p)}_{cb},
\qquad
d_q(u^{(p)})>1.
$$

Las potencias primas se leen como palabras tensoriales `(u^(p))^{\otimes k}`, no como potencias de un
carácter. El coeficiente de von Mangoldt debe venir del logaritmo cíclico:

$$
J_C(s)=
\sum_{p,k\ge1}
(\log p)p^{-ks}\,
X_{p,k},
\qquad
X_{p,k}:=
d_q((u^{(p)})^{\otimes k})^{-1/2}
\operatorname{Tr}_{q,\mathrm{cyc}}((u^{(p)})^{\otimes k}).
$$

El factor `1/k` del logaritmo cíclico está implícito antes de derivar: cancela el `k` producido por
`d(p^{-ks})/ds`, y deja `\Lambda(p^k)=\log p`.

El prime current truncado candidato es

$$
B_\lambda
= \sum_{p^k\le e^\lambda}
(\log p)\,p^{-k/2}\,X_{p,k}\,a_{k,p}^{(q)}\,W_{k\log p}.
$$

**Corrección anti-circular.** Los coeficientes `a_{k,p}^{(q)}` no se fijan exigiendo que el Gram sea
`P_lambda`. Eso sería ingeniería inversa: haría `QSC == Omega_7`. En la versión viva, los
`a_{k,p}^{(q)}` deben venir de una de estas fuentes, en este orden de preferencia:

- la covarianza Mellin-q de `W_{log n}` con `U_q(su(1,1))`;
- la multiplicatividad de Euler como ley de fusión/tensor sobre corepresentaciones primo-locales, no
  como group-like;
- la ortogonalidad de Haar de un compact quantum group auxiliar `G_lambda`;
- una normalización arquimediana local dependiente de `y,z_0`, pero no de los ceros.

Sólo después se exige el matching:

$$
(P_\lambda)_{ij}
=\lim_{q\to1}\langle B_\lambda v_j^{(q)}(z_0),\ B_\lambda v_i^{(q)}(z_0)\rangle_{H_q}.
$$

Éste es **QSC-exist**, no una definición. La aritmética entra por `Lambda(n)`, los desplazamientos
`log n` y la estructura de coproducto; los ceros no deben entrar.

### 2.3 La álgebra q-Pick completa

Definir

$$
\mathcal Q_{\Omega_7}
= \mathcal U_q\ \widehat\ltimes\ \mathcal W_{\Lambda}\ \widehat\rtimes\ \mathcal O(G_\lambda)
$$

donde `\mathcal W_\Lambda` es la *-álgebra generada por los `W_{log n}` con:

$$
W_uW_v=\sigma_q(u,v)W_{u+v},\qquad
W_u^*=W_{-u},
$$

y `\sigma_q` es un 2-cociclo q-Mellin elegido para que la representación sea covariante con
`U_q(su(1,1))`. El dato auditable es si existe una elección **canónica** de `\sigma_q` desde el
Mellin arquimediano, no desde zeta.

El nuevo ingrediente no es una dilatación unitaria genérica sino un **compact quantum group**

$$
G_\lambda=(\mathcal O(G_\lambda),\Delta,\varepsilon,S,h)
$$

con coproducto `Delta`, counidad `epsilon`, antipoda `S` y estado de Haar `h`. Debe existir una
corepresentación fundamental

$$
U_\lambda\in M_d(\mathcal O(G_\lambda))
$$

tal que el prime current sea un coeficiente matricial o una compresión algebraicamente especificada:

$$
B_\lambda=(\omega_{\mathrm{out},\mathrm{in}}\otimes \pi)(U_\lambda)
$$

para una representación `pi` de `\mathcal O(G_lambda)` sobre el módulo q-arquimediano. Esta condición es
mucho más fuerte que "B es esquina de alguna unitaria": impone las identidades Hopf-*

$$
\Delta(U_{ij})=\sum_k U_{ik}\otimes U_{kj},\qquad
S(U)=U^*,\qquad
(\mathrm{id}\otimes h)(U^*(I\otimes X)U)=\text{Peter-Weyl projection}.
$$

La relación crucial que se necesita es de bola de Schur, pero ahora como consecuencia de Haar/Peter-Weyl:

$$
B_\lambda^*B_\lambda \le I
\quad\text{en la representación q-unitaria}.
$$

Esta desigualdad no debe probarse por Sz.-Nagy. Debe salir de que los coeficientes de una
corepresentación unitaria de un CQG son contractivos en toda representación C* compatible con `h`, y de
que `B_lambda` es exactamente uno de esos coeficientes aritméticos. Entonces:

$$
\|B_{\lambda,N}\|\le1
\quad\Rightarrow\quad
A_N-P_\lambda\succeq0.
$$

Ésta es la versión cuántica limpia de Omega_7, ya sin la tautología de dilatación.

---

## 3. Cómo lee `m`

Sea

$$
D_N := I - A_N^{-1/2}P_\lambda A_N^{-1/2}
= I-B_{\lambda,N}^*B_{\lambda,N}.
$$

Entonces:

$$
\delta_N=\lambda_{\min}(D_N).
$$

En el límite de ventanas,

$$
\kappa = \operatorname{ind}_-(D_\infty)
$$

es el índice negativo de la forma de Weil/Pontryagin ya identificado en el programa, y

$$
m=\frac{\kappa}{2}.
$$

La lectura q-algebraica es:

$$
m
=\frac12\,\operatorname{ind}_-\!\left(I-B_\lambda^*B_\lambda\right)
=\frac12\,\ell_{\mathrm{Jantzen}}(D_y^+,B_\lambda),
$$

donde `\ell_Jantzen` es la suma de dimensiones de las capas negativas de la filtración de Jantzen de
la forma contravariante deformada por `B_lambda`.

La intuición: los ceros off-line no son "autovalores misteriosos" sino **fallos de unitarizabilidad**.
Cada cuádruplo off-line aporta una capa hiperbólica en la forma total; Witt-trivialmente se cancela
(Phase 52), pero el índice negativo absoluto no se cancela. En lenguaje q-representacional, esa capa es
un cruce de pared de la forma de Shapovalov/Jantzen:

$$
\det H_q(\mu)=0
\quad\leadsto\quad
\text{salto de signatura}.
$$

Así se lee `m` sin introducir una métrica nueva: `m` es el número de fallos de unitarizabilidad del
prime current dentro de la categoría q-unitaria. Pero anular `m` exige probar que el current está en la
bola de Schur, no sólo medir que se salió.

---

## 4. Por qué esto no es Bost-Connes ni Berry-Keating

### 4.1 Diferencia con Bost-Connes/KMS

Aquí no se toma un estado térmico `phi_beta`, ni una traza `Tr(e^{-beta H})`, ni un Hamiltoniano con
espectro `{log n}` usado para definir la métrica. Si aparece

$$
Z(\beta)=\sum n^{-\beta}=\zeta(\beta),
$$

en la definición de la forma positiva, la ruta muere por Phase 51. La forma positiva permitida es la
contravariante estándar de `U_q(su(1,1))`, fijada por `E^*=F`, y su límite arquimediano `A_N`.

La aritmética entra sólo en el operador `B_lambda`, no en la métrica que decide positividad.

### 4.2 Diferencia con Weyl/CCR y Berry-Keating

No se pide un `H=xp` autoadjunto con espectro `{gamma_rho}`. No se invoca Stone para concluir realidad.
El operador central es una contracción:

$$
B_\lambda:\mathcal H_A\to\mathcal H_A.
$$

El problema es de **Schur/contractividad**, no de autoadjunción. Esto evita el inverted-Stone wall de
Phase 53. Si la única manera de obtener la contracción es elegir una extensión/frontera con fase zeta,
la ruta muere por la misma pared; pero la formulación no la presupone.

---

## 5. El test exacto contra la NO-GO-LIST

| Test | Pregunta | Resultado esperado |
|---|---|---|
| T0 | `A_N` viene de la forma q-contravariante exacta, no de whitening escalar | Debe pasar antes de cualquier claim |
| T1 | La positividad de la forma no usa KMS, partición ni `Tr(e^{-beta H})` | Si falla, Phase 51/MW-5 |
| T2 | `B_lambda` no se define por Cholesky/raíz de `P_lambda` | Si falla, QSC-exist es Omega_7 reescrita |
| T3 | `B_lambda` es coeficiente de una corepresentación CQG con Haar, no sólo esquina Sz.-Nagy | Si falla, QSC-contract es tautológica |
| T4 | El DH falsifier viola alguna relación Hopf-* / Haar identificable | Si DH también satisface las relaciones, la ruta probaría algo falso |
| T5 | Las relaciones no codifican los ceros en `sigma_q`, `h` o en una condición de borde | Si los codifican, Phase 52/53 |
| T6 | El límite `q->1`, `N->infty` conserva el índice sin fuga primitiva | Si falla, Phase 66/rank-one escape |

El test más importante es T4. Una estructura que acepte tanto zeta como Davenport-Heilbronn y aun así
fuerce `B^*B<=I` no puede ser correcta. Por tanto la relación nueva debe ser una relación
aritmética fina que DH no tenga: no "suavidad de `Lambda`", no envelope, no magnitudes, sino una
identidad de corepresentación ligada al producto de Euler.

---

## 6. Las dos compuertas QSC

**QSC-exist — existencia no circular del current.** Existe un cociclo `sigma_q` canónico, construido
desde la covarianza Mellin arquimediana y la multiplicatividad de Euler en la categoría de fusión, y
existe un CQG
`G_lambda=(O(G_lambda),Delta,h)` tal que:

1. `B_lambda` es un coeficiente matricial de una corepresentación fundamental de `G_lambda`;
2. los generadores primos no son group-like; son bloques de corepresentaciones no triviales con
   `d_q>1`;
3. sus coeficientes `a_{k,p}^{(q)}` no se eligen para reproducir `P_lambda`;
4. el jet coherente arquimediano satisface, como teorema de matching,

$$
(P_\lambda)_{ij}
=\lim_{q\to1}\langle B_\lambda v_j^{(q)}(z_0),B_\lambda v_i^{(q)}(z_0)\rangle_{H_q}.
$$

Esta es la compuerta donde puede reaparecer Phase 51: si identificar `B_lambda` como coeficiente de Haar
exige introducir el producto de Euler completo como una función de partición, o los ceros como dato de
frontera, la ruta muere.

**QSC-contract — contractividad por Haar/Peter-Weyl.** En toda representación C* compatible con el
estado de Haar y con el módulo q-arquimediano, el coeficiente `B_lambda` satisface:

$$
B_\lambda^*B_\lambda\le I
$$

para todo `lambda`, con límite fuerte compatible con el whitening exacto `A_N^{-1/2}`. Esta desigualdad
debe seguir de las relaciones Hopf-* / Peter-Weyl / Haar del CQG, no de Sz.-Nagy ni de asumir que `B` ya
es una contracción.

**Consecuencia si QSC-exist y QSC-contract son verdaderos.**

Para todo `N`,

$$
A_N^{-1/2}P_\lambda A_N^{-1/2}
=B_{\lambda,N}^*B_{\lambda,N}\le I,
$$

luego

$$
\delta_N\ge0.
$$

Por P52/P53:

$$
\Omega_7\quad\Longleftrightarrow\quad\mathrm{RH}.
$$

**Pero ninguna de las dos compuertas puede asumirse.** Si se demuestran usando sólo:

- las relaciones de `U_q(su(1,1))`;
- la covarianza Mellin de los `W_{log n}`;
- la multiplicatividad de Euler como fusión/tensor, no como group-like;
- las relaciones Hopf-* y la ortogonalidad Haar/Peter-Weyl/q-dimensión;

entonces la idea abre un nodo nuevo. Si QSC se demuestra usando:

- una norma definida por `-zeta'/zeta`;
- una condición de borde con fase de zeta;
- un estado KMS cuya partición es zeta;
- una convergencia de índice equivalente a RH;
- una dilatación Sz.-Nagy sin relaciones Hopf-*;

entonces no abrió nada.

---

## 7. Experimentos y falsadores propuestos

### E67.1 — Matching arquimediano exacto

Construir `G_N^(q)` desde la forma contravariante de la representación `D_y^+`, tomar el límite
renormalizado `q->1`, y comparar entrada por entrada con el `A_N` de poligamma. La tolerancia no es
asintótica gruesa: debe reproducir el matrix whitening de P52.

**Go:** `G_N^(q)->A_N` para `N<=24` en el harness exacto.
**No-go:** sólo reproduce `1/log(t0)` o un Toeplitz leading symbol. Eso sería Phase 66 otra vez.

### E67.2 — QSC-exist: current antes del Pick jet

Construir `sigma_q`, `O(G_lambda)` y los coeficientes `a_{k,p}^{(q)}` desde las relaciones Mellin/Euler,
sin usar `P_lambda`. La versión group-like de este punto queda marcada como NO-GO: reproduce Euler pero
colapsa a Bost-Connes. La versión viva exige un current de fusión no conmutativo como en `E67.3`.
Recién después calcular

$$
\widehat P_{\lambda,ij}^{(q)}
=\langle B_\lambda v_j^{(q)}(z_0),B_\lambda v_i^{(q)}(z_0)\rangle_{H_q}
$$

y comparar `lim_{q->1} \widehat P_\lambda^{(q)}` contra el `P_lambda` exacto.

**Go:** el matching aparece entrada por entrada sin ajustar coeficientes desde `P_lambda`.
**No-go:** hay que usar Cholesky, raíz canónica o ajuste posterior. Entonces QSC-exist es circular.

### E67.2b — K2-mech: separar reproducción de mecanismo

`K2-repro` pregunta si el current reproduce `P_lambda`. Esto es necesario, pero no basta: el caso
group-like también puede reproducir el Euler clásico.

`K2-mech` pregunta si el bound de Schur cambia porque aparecen pesos de Haar/q-dimensión de una
corepresentación no trivial.

**Go:** el número CQG usa explícitamente la normalización `d_q^{-1/2}` / Peter-Weyl y no coincide con el
baseline group-like.
**No-go:** el resultado es idéntico al counit/group-like; no hay mecanismo nuevo.

### E67.3 — QSC-contract: relaciones Haar/Peter-Weyl

$$
\Delta(U_{ij})=\sum_k U_{ik}\otimes U_{kj},\qquad
(\mathrm{id}\otimes h)(U_{ij}^*U_{kl})=\text{orthogonality constants}
$$

Verificar que esas relaciones fuerzan `||B_lambda||<=1` como coeficiente de corepresentación, no por una
dilatación abstracta.

**Go:** la contractividad se deduce de la estructura CQG y sobrevive al whitening exacto.
**No-go:** sólo se obtiene una unitaria dilatada ad hoc. Eso es Sz.-Nagy y no aporta contenido.

### E67.4 — Interference no-go para free products estrictos

El modelo `*_{p<=e^lambda} U_N^+(F_p)` es ahora baseline/falsifier, no candidato final. Su Haar
ortogonaliza los bloques `X_{p,k}`:

$$
h(X_{p,k}^*X_{q,l})=0\quad((p,k)\ne(q,l)),
$$

y por tanto convierte el Gram del current en una suma absoluta/diagonal. Pero `P_lambda` es una suma
lineal oscilatoria con fases `n^{\pm it_0}`; la interferencia entre prime powers es parte del operador,
no ruido.

La medición existente `omega7_operator_interference.py` da en `t0=10,y=1`:

```text
N=4  ||S P S|| = 0.99999993423   S_abs =   219.4407   I =   219.441
N=8  ||S P S|| = 1.0             S_abs = 18683.3261   I = 18683.326
```

Así que matar interferencia infla la norma por factores enormes. Cualquier CQG vivo debe preservar esa
interferencia.

### E67.5 — Ruta modular/Woronowicz, debilitada por E67.7

La ruta Woronowicz reemplazó "Haar puro" por dos canales:

```text
f_z  = caracteres modulares de Woronowicz  -> evaluación Mellin/Euler, fases e^{-it log p};
h,F  = Haar con matriz F                  -> Peter-Weyl/q-dimensión, cota.
```

El mismo dato modular `F_p` debe producir:

```text
f_{-s}(u^(p)) ~ p^{-s},
d_q(p) = Tr(F_p),
h((u_ij^(p))^*u_kl^(p)) = F_p-weighted / d_q(p).
```

Pero E67.7 muestra que esto todavía no basta. La desigualdad modular simple

```text
|Phi_{t0,y,q}(X)|^2 <= C(t0,y,q) * h(X^* F_p X) / d_q(p),
```

sumada término a término vuelve al techo incoherente `S_abs`. Para escapar hace falta una fuente
off-diagonal:

```text
omega_{z0,q}(X_a^*X_b) != 0
```

que reproduzca las fases aritméticas, junto con una dominación no circular:

```text
|omega_{z0,q}(Y)|^2 <= h(Y^* D_{z0,q} Y).
```

El dato `D_{z0,q}` no puede ser `P_lambda`, `-zeta'/zeta`, ni una densidad KMS con partición `zeta`.

### E67.6 — Normalización Woronowicz

Antes del falsador DH queda una compuerta de normalización: el canal Woronowicz no puede contar dos
veces el factor `p^{-k/2}` ni esconderlo fuera del CQG. Hay que decidir si `f_z` porta el peso Dirichlet
completo o sólo la fase Mellin, y en ambos casos verificar:

```text
N1: f_z reproduce exactamente la dependencia p,z;
N2: Haar mide el mismo X_{p,k} con pesos F_p/d_q;
N3: reemplazar X_{p,k} por la counidad cambia el bound.
```

Ésta es `E67.6` en los documentos auxiliares.

### E67.7 — Auditoría off-diagonal Woronowicz

El test decisivo ya no es `mech != 0`, sino:

```text
offdiag_error =
  ||offdiag(G_mod)-offdiag(G_exact)|| / ||offdiag(G_exact)||.
```

Si el Gram modular es diagonal entre prime powers, es E67.4 otra vez. Si reproduce el off-diagonal pero
la densidad dominante es KMS-zeta, es Phase 51 otra vez. Sólo queda vivo si el off-diagonal viene de
`omega_{z0,q}` canónico y la cota viene de `D_{z0,q}` zeta-free.

### E67.8 — DH falsifier

Repetir E67.2/E67.3 con DH o con un cero off-line plantado. La prueba de vida de la idea es que DH debe
romper alguna relación Hopf-* / Haar antes de romper sólo la positividad.

**Go:** DH viola la relación de corepresentación/cociclo o la unitaridad cuántica.
**No-go:** DH satisface las mismas relaciones y sólo tiene `||B||>1`. Entonces la álgebra sólo detecta
RH, no la explica.

---

## 8. Diagnóstico final

La idea queda así:

$$
\boxed{
\Omega_7
\iff
I-B_\lambda^*B_\lambda\succeq0
\iff
B_\lambda\ \text{es Schur-contractivo}
}
$$

con

$$
\boxed{
m=\frac12\operatorname{ind}_-(I-B_\lambda^*B_\lambda).
}
$$

La ruta cuántica legítima no es "hacer una métrica positiva para zeta"; eso ya está muerto. Es más
afilada:

> construir primero una corepresentación CQG modular no group-like que produzca el **operador primo** sin
> mirar `P_lambda`, usando un estado coherente `omega_{z0,q}` para conservar la interferencia Mellin, y
> después probar que ese estado está dominado por Haar mediante una densidad canónica `D_{z0,q}`; no por
> dilatación, caracteres group-like ni KMS-zeta.

Esto sí modela "los dos lados":

- lado arquimediano: forma contravariante `U_q(su(1,1))` = `A_N`;
- lado primo: current de von Mangoldt = logaritmo cíclico tensorial evaluado por un estado modular
  coherente;
- lado Hopf: `Delta,h,S,epsilon` fuerzan restricciones que una raíz de Cholesky no tiene;
- lado RH: índice negativo del defecto de Schur = `2m`;
- lado Omega_7: contractividad finita de todos los jets = `delta_N>=0`.

**Puntos de auditoría exactos:**

1. `E67.1`: demostrar el matching arquimediano exacto `G_N^(q)->A_N` con matrix whitening, no símbolo
   leading.
2. `QSC-exist`: construir `sigma_q`, `G_lambda` y `B_lambda` sin Cholesky ni ajuste a `P_lambda`; luego
   obtener `P_lambda` como salida.
3. `E67.4`: descartar free-product Haar estricto como candidato final por pérdida de interferencia.
4. `E67.5`: usar Woronowicz `f_z/F_p` sólo como vocabulario modular, no como prueba suficiente.
5. `E67.6`: fijar normalización sin doble conteo del factor `p^{-k/2}` ni colapso a counit.
6. `E67.7`: construir o refutar `omega_{z0,q}` off-diagonal y `D_{z0,q}` Haar-dominante.
7. `QSC-contract`: deducir `B_lambda^*B_lambda<=I` desde esa dominación modular, no desde
   Sz.-Nagy ni desde group-like.
8. `DH`: mostrar que Davenport-Heilbronn rompe alguna relación Hopf-* / Haar específica.

Hasta ahí, Phase 67 es un buen lenguaje y un detector. Cruzar `QSC-exist + QSC-contract` sería
matemática nueva.
