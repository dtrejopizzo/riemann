# 104_33 — Símbolo de bandera y gate exacto frontera--residuos

**Rol.** Atacar el primer momento de `104_30` mediante el símbolo Toeplitz
de la forma prima--polo y determinar si una estimación de frontera puede
producir la coercividad proporcional que falta.

El símbolo admite una forma cerrada. Sin embargo, es meromorfo en el disco
exactamente cuando existen ceros a la derecha de la línea crítica. Al
deformar el momento de prefijo hasta la frontera aparece un término de
residuos interiores que no es un error técnico: un cuarteto fuera de la
línea deja invariante el símbolo real de frontera y coloca toda su carga
exponencial en esos residuos.

Por tanto, una prueba que use solamente el símbolo real de frontera es
circular si omite los residuos o supone holomorfía en el disco. Este
documento no descarta una estimación aritmética firmada que controle
conjuntamente frontera y residuos, pero muestra exactamente qué término
RH-strength tendría que controlar.

Este documento no prueba A1 ni RH.

**Pre-registro.** El enunciado ensayado es el techo de primer momento
\(B_n/A_n\le1501/2002\) sobre los prefijos de bandera. Los únicos inputs
son: Euler producto en \(\Re s>1\), continuación meromorfa, ecuación
funcional, conjugación, producto de Hadamard emparejado y las identidades
Laguerre de `104_30`; todos son incondicionales. El falsificador obligatorio
es un cuarteto recíproco fuera de la línea. Una deducción que use solo los
inputs simétricos debe fallar para ese cuarteto; si no falla, ha omitido el
dato transversal de los ceros.

## 1. Auditoría de no duplicación

`103_26_INTEGRATED_STRONG_MARGIN_AUDIT.md` contiene la identidad de Fejér
para otro margen completado y descarta positividad puntual del símbolo.
`phase-102/175_LOG_DERIVATIVE_RH_EQUIVALENCE.md` identifica la positividad
de \(\xi'/\xi\) en el semiplano con RH. `104_30` construye la referencia
positiva de bandera y calcula las entradas \(q_d\).

Lo que se añade aquí es:

1. la suma cerrada exacta del símbolo **prima--polo** de `104_30`;
2. una fórmula de deformación frontera--residuos para su momento de
   prefijo;
3. el residuo cerrado de cada cero a la derecha;
4. un falsificador de cuarteto que conserva exactamente la frontera y
   cambia exponencialmente el cociente de bandera.

## 2. El símbolo prima--polo exacto

Sea

\[
 h_\varepsilon(z)
 :=q_0(\varepsilon)+2\sum_{d\ge1}q_d(\varepsilon)z^d,
 \qquad s=s(z):={1\over1-z}.
 \tag{1}
\]

La identidad triangular (18) de `104_30` da

\[
 \sum_{n\ge1}P_{n,\varepsilon}z^{n-1}
 ={h_\varepsilon(z)\over(1-z)^2}.                    \tag{2}
\]

Por otro lado,

\[
 \sum_{n\ge1}L_{n-1}^{(1)}(x)z^{n-1}
 ={1\over(1-z)^2}
   \exp\!\left(-{xz\over1-z}\right).                \tag{3}
\]

Aplicando (3) primero en el semiplano de convergencia absoluta del Euler
producto,

\[
\begin{aligned}
 \sum_{n\ge1}P_{n,\varepsilon}z^{n-1}
 ={1\over(1-z)^2}\left[
 -{\zeta'\over\zeta}\!\left(1+\varepsilon+{z\over1-z}\right)
 -{1\over\varepsilon+z/(1-z)}\right].
\end{aligned}                                                 \tag{4}
\]

Como \(1+z/(1-z)=s\), (2)--(4) prueban

\[
 \boxed{
 h_\varepsilon(z)
 =-{\zeta'\over\zeta}(s+\varepsilon)
  -{1\over s+\varepsilon-1}.}
 \tag{5}
\]

Al retirar el regulador, la singularidad en \(s=1\) se cancela y queda el
germen regular

\[
 \boxed{
 h(z)=q_0+2\sum_{d\ge1}q_dz^d
 =-{\zeta'\over\zeta}(s)-{1\over s-1},
 \qquad h(0)=-\gamma.}
 \tag{6}
\]

La ecuación (6) es primero una identidad de gérmenes en \(z=0\) y luego
una continuación meromorfa. No se ha supuesto RH.

Si \(B_n=A_n-\lambda_n\), entonces

\[
 \boxed{
 B_n=nq_0+2\sum_{d=1}^{n-1}(n-d)q_d.}
 \tag{7}
\]

Por (24) y (30) de `104_30`, (7) es exactamente el primer momento de la
bandera en cualquier sección finita \(K_{M,N}\) con \(N\ge n\):

\[
 {B_n\over A_n}=\langle u_n,K_{M,N}u_n\rangle.       \tag{8}
\]

## 3. Lema meromorfo de Fejér

Definamos el polinomio de Fejér como polinomio de Laurent

\[
 \mathcal F_n(z)
 :=n+\sum_{d=1}^{n-1}(n-d)(z^d+z^{-d})
 ={(1-z^n)(1-z^{-n})\over(1-z)(1-z^{-1})}.          \tag{9}
\]

En \(|z|=1\),

\[
 \mathcal F_n(e^{i\theta})
 =\left|\sum_{j=0}^{n-1}e^{ij\theta}\right|^2\ge0.  \tag{10}
\]

**Lema 3.1 (frontera más residuos).** Sea \(H\) un germen con
coeficientes reales en cero que continúa meromórficamente a un entorno del
disco cerrado, sin polos en el círculo, y con polos simples \(p\) en el
disco, de residuos \(r_p\). Si

\[
 H(z)=a_0+\sum_{d\ge1}a_dz^d
\]

en su disco local de Taylor, entonces

\[
\begin{aligned}
 &na_0+\sum_{d=1}^{n-1}(n-d)a_d\\
 &\quad={1\over2\pi}\int_{-\pi}^{\pi}
   \Re H(e^{i\theta})\,\mathcal F_n(e^{i\theta})\,d\theta
   -\sum_{|p|<1}r_p{\mathcal F_n(p)\over p},
\end{aligned}                                                 \tag{11}
\]

donde los polos no reales se agrupan con sus conjugados. En particular,
el lado derecho es real.

*Demostración.* Reste las partes principales y aplique ortogonalidad de
Fourier a la parte holomorfa. Solo hay que calcular un polo
\(r/(z-p)\). Su expansión local y su expansión sobre el círculo son,
respectivamente,

\[
 {r\over z-p}=-\sum_{d\ge0}{r\over p^{d+1}}z^d,
 \qquad
 {r\over z-p}=\sum_{d\ge1}rp^{d-1}z^{-d}.           \tag{12}
\]

La diferencia entre el momento local de la primera serie y el momento de
frontera de la segunda es

\[
 -r\left[
 {n\over p}+\sum_{d=1}^{n-1}(n-d)
       (p^{d-1}+p^{-d-1})\right]
 =-r{\mathcal F_n(p)\over p}.                       \tag{13}
\]

Sumando los polos se obtiene (11). \(\square\)

La hipótesis de finitud puede retirarse por límites meromorfos siempre que
la suma de (13) converja absolutamente. Eso es precisamente lo que ocurre
para el logaritmo derivado de \(\xi\) con \(n\) fijo, como se verifica en
la sección siguiente. Los polos sobre el círculo se incorporan mediante el
límite radial/parte finita simétrica; en particular, los ceros críticos
forman parte de la distribución de frontera y no se descartan tomando el
valor puntual fuera de sus ordenadas.

## 4. Especialización a los ceros de \(\zeta\)

Para un cero no trivial \(\rho\), escribamos

\[
 w_\rho=1-{1\over\rho}.
\]

Entonces

\[
 |w_\rho|^2
 =1+{1-2\Re\rho\over|\rho|^2}.                     \tag{14}
\]

Así \(w_\rho\) está dentro del disco exactamente cuando
\(\Re\rho>1/2\). Si \(m_\rho\) es la multiplicidad, (6) y
\(ds/dz=s^2\) dan

\[
 \boxed{
 \mathop{\rm Res}_{z=w_\rho}h(z)=-{m_\rho\over\rho^2}.}
 \tag{15}
\]

Para fijar sin ambigüedad el primer término de la fórmula siguiente, se
toman sumas parciales del logaritmo derivado de \(\xi\) por órbitas
funcionales completas y altura creciente. En cada suma finita se usa la
traza interior de distribución en el círculo: valor ordinario fuera de los
polos críticos y límite Abel normal en esos polos. Se aplica el Lema 3.1,
con pequeñas indentaciones simétricas, y luego se hace tender la altura a
infinito. Denotamos el límite resultante por
\(\mathcal I_n^\partial(h)\). La convergencia local del producto de
Hadamard fija sus coeficientes en cero, y la convergencia absoluta indicada
en (17) fija separadamente los residuos interiores. No se supone soporte
crítico en esta definición.

Por tanto (11), en ese límite simétrico, se vuelve

\[
 \boxed{
 B_n=\mathcal I_n^\partial(h)
 +\sum_{\Re\rho>1/2}
   {m_\rho\over\rho(\rho-1)}\,\mathcal F_n(w_\rho).}
 \tag{16}
\]

Aquí \(\mathcal I_n^\partial(h)\) denota el momento de la distribución
radial de frontera, incluyendo los polos correspondientes a ceros sobre la
línea. Para \(n\) fijo la suma de residuos de (16) converge absolutamente:
\(w_\rho\to1\), \(\mathcal F_n(w_\rho)=n^2+O_n(|\rho|^{-1})\), y

\[
 \sum_\rho {m_\rho\over1+|\Im\rho|^2}<\infty.        \tag{17}
\]

La fórmula de bandera queda, sin abreviaturas,

\[
 \boxed{
 \langle u_n,K_{M,N}u_n\rangle
 ={\mathcal I_n^\partial(h)\over A_n}
 +{1\over A_n}\sum_{\Re\rho>1/2}
   {m_\rho\mathcal F_n(w_\rho)\over\rho(\rho-1)}.}
 \tag{18}
\]

El techo suficiente de Phase 104 es

\[
 \langle u_n,K_{M,N}u_n\rangle
 \le {1501\over2002}\qquad(n\ge150).                \tag{19}
\]

La suma de (18), no una norma de operador, es el término que cualquier
prueba de (19) debe conservar.

## 5. Qué contiene realmente la frontera

De la definición completada

\[
 \xi(s)={1\over2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

se deduce

\[
 h(z)={1\over s}-{1\over2}\log\pi
       +{1\over2}\psi(s/2)-{\xi'\over\xi}(s).       \tag{20}
\]

Sobre \(z=e^{i\theta}\ne1\),

\[
 s={1\over2}+{i\over2}\cot{\theta\over2}.          \tag{21}
\]

La función \(\xi(1/2+it)\) es real. Fuera de sus ceros,
\(\xi'/\xi(1/2+it)\) es puramente imaginaria. Por ello el valor puntual
real de frontera es solamente

\[
 \Re h(e^{i\theta})
 =\Re\left[{1\over s}-{1\over2}\log\pi
                  +{1\over2}\psi(s/2)\right].       \tag{22}
\]

Esto no autoriza a borrar la parte de \(\xi'/\xi\): los ceros críticos
aparecen como masa en el límite radial de (22), y los ceros a la derecha
aparecen en la suma de residuos de (16).

En particular,

\[
 h\text{ holomorfa en }\mathbb D
 \quad\Longleftrightarrow\quad
 \zeta\text{ no tiene ceros con }\Re\rho>1/2
 \quad\Longleftrightarrow\quad \mathrm{RH},          \tag{23}
\]

donde la última equivalencia usa la simetría funcional. Tratar (6) como un
símbolo de Hardy holomorfo en todo el disco ya importa RH.

## 6. Falsificador exacto: misma frontera, distinta coercividad

Sea \(\rho\) un punto con \(1/2<\Re\rho<1\), y sea

\[
 \mathcal O(\rho)=\{\rho,\bar\rho,1-\rho,1-\bar\rho\},
 \qquad
 Q_\rho(s)=\prod_{\eta\in\mathcal O(\rho)}(s-\eta). \tag{24}
\]

Multiplicar el divisor completado por \(Q_\rho^M\) conserva conjugación y
la ecuación funcional. En el símbolo produce

\[
 \widetilde h(z)=h(z)-M{Q_\rho'\over Q_\rho}(s(z)).  \tag{25}
\]

Si \(s=1/2+it\), entonces \(Q_\rho(s)\) es real y no nulo. Por tanto

\[
 \boxed{
 \Re\widetilde h(e^{i\theta})=\Re h(e^{i\theta})}
 \tag{26}
\]

en toda la frontera, también en sentido distribucional: el cuarteto no
añade ceros sobre la línea.

Póngase \(w=w_\rho\), de modo que \(|w|<1\). La identidad elemental

\[
 {\mathcal F_n(w)\over\rho(\rho-1)}
 ={(1-w)^2\over w}\mathcal F_n(w)
 =w^n+w^{-n}-2                                      \tag{27}
\]

prueba que los residuos de los dos ceros derechos aportan

\[
\begin{aligned}
 2M\Re\left({\mathcal F_n(w)\over\rho(\rho-1)}\right)
 &=2M\Re(w^n+w^{-n}-2)\\
 &=-M Q_n,
\end{aligned}                                                 \tag{28}
\]

donde

\[
 Q_n=4-2\Re(w^n+w^{-n})
 =4-4\cosh(n\alpha)\cos(n\vartheta),
 \quad w=e^{-\alpha+i\vartheta}.                    \tag{29}
\]

Aquí \(Q_n\) es la contribución del cuarteto al **coeficiente de Li**. La
forma de Weil \(2\Re\lambda_n\) la duplica y lleva el factor \(8\) usado en
otros documentos; ambas normalizaciones no se mezclan en (28)--(29).

Esto coincide exactamente con el cambio
\(\widetilde B_n-B_n=-M Q_n\), ya que el cuarteto suma \(M Q_n\) al
coeficiente de Li y no cambia \(A_n\).

Use ahora el falsificador ya fijado en `104_26`,

\[
 w={1\over2}e^{74\pi i/75},\qquad \rho={1\over1-w}. \tag{30}
\]

En \(n=150\), \(\cos(150\cdot74\pi/75)=1\), y

\[
 -Q_{150}=4\bigl(\cosh(150\log2)-1\bigr)>0.         \tag{31}
\]

La cantidad (31), multiplicada por \(M\), supera cualquier múltiplo fijo
de \(A_{150}\), mientras (26) deja invariante toda estimación que vea solo
el símbolo real de frontera. Por consiguiente:

> ninguna cota uniforme de (19) puede deducirse exclusivamente de
> \(\Re h|_{\partial\mathbb D}\), de la ecuación funcional y de la
> simetría. Debe controlar la suma firmada de residuos en (18), o usar
> aritmética que rechace el cuarteto.

El resultado no afirma que tal control aritmético sea imposible. Afirma que
reemplazarlo por una cota de símbolo de frontera borra exactamente el dato
que decide RH.

## 7. Verificación racional

El archivo `tools/flag_symbol_residue_check.py` usa el cuarteto racional

\[
 w={i\over2},\qquad \rho={1\over1-w}={4+2i\over5},
\]

y comprueba con `Fraction`, sin punto flotante:

1. la identidad (27) para \(1\le n\le20\);
2. que el residuo del par derecho es \(-Q_n\);
3. que \(Q_\rho'/Q_\rho(1/2+it)\) tiene parte real cero para una malla
   racional de \(t\).

Se reproduce con

    cd 03-research/phase-104-unconditional-a1-closure/tools
    python3 flag_symbol_residue_check.py

## Estado

* **Probado:** símbolo cerrado (5)--(6), lema frontera--residuos (11),
  residuo de cada cero (15), fórmula de primer momento (16)--(18) e
  invariancia de frontera del cuarteto (26)--(31).
* **Descartado:** obtener (19) de una cota sobre el símbolo real de
  frontera, o invocar teoría de Hardy/Toeplitz suponiendo sin prueba que
  \(h\) es holomorfa en el disco.
* **Sobrevive:** una estimación aritmética firmada, específica de
  \(\zeta\), para el miembro completo de (18). Debe rechazar el cuarteto y
  no puede separar la frontera de sus residuos por valores absolutos.
* **No probado:** (19), A1 y RH.
