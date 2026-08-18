# 104_15 — Complejo Euler–Gamma: gate de Koszul en los posets mínimos

## Veredicto

La construcción graduada mínima sí existe como complejo de Hilbert positivo. En el
cubo divisor se trata del complejo de Koszul

\[
 d_E=\sum_r N_r\otimes\varepsilon_r,
 \qquad d_E^2=0,
\tag{1}
\]

donde \(N_r\) elimina el factor primo \(r\) y \(\varepsilon_r\) es
multiplicación exterior. En \(\{1,p,q,pq\}\), su laplaciano de Hodge cancela
exactamente los canales mixtos \(p/q\) y \(q/p\). La cancelación usa una
métrica positiva ordinaria, no una supertraza ni una forma de Krein.

Pero el mismo diferencial hace nulo en cohomología el cruce
Möbius--divisor:

\[
 M\delta Z=(\log p)N_p+(\log q)N_q,
 \qquad
 N_r=d_E\iota_r+\iota_r d_E.
\tag{2}
\]

Por tanto \(M\delta Z\) es homotópicamente nulo. Ya en el poset
\(\{1,p\}\), el canal hermitizado que se quiere declarar frontera es
exactamente el mismo canal que debe sobrevivir como corriente prima. Así, el
complejo de Koszul natural satisface la cancelación de cocientes, pero falla la
propiedad 1 de 104_12 §8 antes de que pueda aparecer el presupuesto Gamma de la
propiedad 3.

El alcance es preciso: éste es un **no-go para el complejo de Koszul divisor
y, más generalmente, para todo complejo en el que cada generador de cociente
\(N_p\) sea nulo-homotópico**. No prueba que toda cohomología aritmética
imaginable sea imposible. En particular, no descarta un diferencial no local
que mate solo combinaciones cuadráticas de cocientes sin hacer exactos los
\(N_p\); tal objeto seguiría debiendo construir, y no postular, el término
Gamma exacto.

El modelo es el cubo **squarefree/booleano**. No representa por sí solo las
torres \(p^k\). Por ello el teorema descarta exactamente este Koszul natural y
sus variantes \(N_p\)-exactas, no una resolución graduada distinta que incorpore
las potencias primas como datos adicionales.

No se prueba A1 ni RH.

## 1. Álgebra booleana de divisores

Sea \(P=\{p_1,\dots,p_r\}\) un conjunto finito de primos y sea

\[
 {\cal D}_P=\left\{\prod_{p\in S}p:S\subseteq P\right\}.
\tag{3}
\]

En \(V_P=\ell^2({\cal D}_P)\), con su base ortonormal canónica, definimos

\[
 N_p e_n=
 \begin{cases}
 e_{n/p},&p\mid n,\\
 0,&p\nmid n.
 \end{cases}
\tag{4}
\]

Entonces

\[
 N_p^2=0,
 \qquad N_pN_q=N_qN_p,
 \qquad N_p^*N_q=N_qN_p^*\quad(p\ne q).
\tag{5}
\]

La matriz zeta del poset y su inversa de Möbius factorizan como

\[
 Z_P=\prod_{p\in P}(I+N_p),
 \qquad
 M_P=Z_P^{-1}=\prod_{p\in P}(I-N_p).
\tag{6}
\]

Sea \(\delta\) la derivación determinada por
\(\delta N_p=(\log p)N_p\). Aplicando Leibniz a (6), y usando
\((I-N_p)(I+N_p)=I\), se obtiene la identidad exacta

\[
 \boxed{
 M_P\delta Z_P=\sum_{p\in P}(\log p)N_p.}
\tag{7}
\]

Ésta es la versión divisor-finita de \(Z^{-1}\delta Z=V_\Lambda\). No se
ha usado localización de ceros ni una desigualdad.

## 2. El poset mínimo \(\{1,p\}\)

En la base \((e_1,e_p)\), poniendo \(\ell_p=\log p\),

\[
 N_p=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
 Z=I+N_p=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
 M=I-N_p.
\tag{8}
\]

Por tanto

\[
 Z^*Z=
 \begin{pmatrix}1&1\\1&2\end{pmatrix}
 =I+(N_p+N_p^*)+N_p^*N_p,
 \qquad
 M\delta Z=\ell_pN_p.
\tag{9}
\]

El canal no diagonal de cociente en \(Z^*Z\) es \(N_p+N_p^*\). El cruce
físico hermitizado es

\[
 M\delta Z+(M\delta Z)^*=\ell_p(N_p+N_p^*).
\tag{10}
\]

Esto da el falsificador mínimo.

**Proposición 1 (colisión canal--corriente).** Sea \((C^\bullet,d)\) un
complejo y supóngase que el canal hermitizado \(N_p+N_p^*\) induce el
operador cero en su cociente físico. Entonces el cruce hermitizado (10)
también induce el operador cero. En particular, ese cociente no puede
satisfacer simultáneamente las propiedades 1 y 2 de 104_12 §8.

**Prueba.** El segundo operador es el primero multiplicado por el escalar
positivo \(\ell_p\). \(\square\)

Una versión holomorfa, que será la que use el complejo de Koszul, es todavía
más fuerte: si \(N_p=dh+hd\), entonces \(N_p\) induce cero en cohomología,
y también lo hace \(\ell_pN_p\).

La proposición no dice que deba matarse el canal \(p/1\). Dice que **si** la
regla de 104_12 §8 se implementa declarando exactos todos los canales de
\(Z^*Z\), ya el primer canal destruye la corriente que se quería conservar.

## 3. El cuadrado \(\{1,p,q,pq\}\)

En la base \((e_1,e_p,e_q,e_{pq})\),

\[
 N_p=
 \begin{pmatrix}
 0&1&0&0\\
 0&0&0&0\\
 0&0&0&1\\
 0&0&0&0
 \end{pmatrix},
 \qquad
 N_q=
 \begin{pmatrix}
 0&0&1&0\\
 0&0&0&1\\
 0&0&0&0\\
 0&0&0&0
 \end{pmatrix}.
\tag{11}
\]

Así,

\[
 Z=(I+N_p)(I+N_q)=
 \begin{pmatrix}
 1&1&1&1\\
 0&1&0&1\\
 0&0&1&1\\
 0&0&0&1
 \end{pmatrix},
\tag{12}
\]

y (7) se reduce a

\[
 \boxed{M\delta Z=\ell_pN_p+\ell_qN_q.}
\tag{13}
\]

Sea \(E=\mathbb C e_p\oplus\mathbb C e_q\), con la métrica positiva
estándar, y sea

\[
 K^k=V_P\otimes\Lambda^kE,
 \qquad
 d_E=N_p\otimes\varepsilon_p+N_q\otimes\varepsilon_q.
\tag{14}
\]

Como los \(N\) conmutan y las multiplicaciones exteriores anticonmutan,

\[
 d_E^2=N_pN_q\otimes
 (\varepsilon_p\varepsilon_q+\varepsilon_q\varepsilon_p)=0.
\tag{15}
\]

No se introdujo ningún signo en la métrica: cada \(K^k\) es un espacio de
Hilbert ordinario.

### 3.1. Los cocientes mixtos sí se cancelan

Denote por \(\iota_p,\iota_q\) las contracciones, adjuntas de
\(\varepsilon_p,\varepsilon_q\). En el laplaciano

\[
 \Delta_E=d_E^*d_E+d_Ed_E^*,
\tag{16}
\]

el coeficiente de \(\iota_p\varepsilon_q\) es

\[
 N_p^*N_q-N_qN_p^*=0,
\tag{17}
\]

y el coeficiente conjugado es

\[
 N_q^*N_p-N_pN_q^*=0.
\tag{18}
\]

Las igualdades son exactamente la doble conmutación de (5). Por ello los
canales \(p/q\) y \(q/p\), que aparecerían en un cuadrado no graduado, se
cancelan entre los dos grados adyacentes. Ésta es una realización positiva y
explícita de la parte de cancelación pedida en la propiedad 2.

### 3.2. La corriente se vuelve frontera

Las relaciones canónicas exteriores dan

\[
 \varepsilon_j\iota_i+\iota_i\varepsilon_j=\delta_{ij}I.
\tag{19}
\]

Consecuentemente,

\[
 \boxed{d_E\iota_p+\iota_p d_E=N_p,\qquad
 d_E\iota_q+\iota_q d_E=N_q.}
\tag{20}
\]

Multiplicando por \(\ell_p,\ell_q\) y sumando,

\[
 M\delta Z=d_EH+Hd_E,
 \qquad
 H=\ell_p\iota_p+\ell_q\iota_q.
\tag{21}
\]

Por tanto \(M\delta Z\) induce el operador cero en
\(H^\bullet(K,d_E)\). El complejo que cancela correctamente el peine de
cocientes no deja el cruce Möbius--divisor en cohomología: lo convierte en
una frontera junto con el peine.

## 4. Teorema general y alcance

**Teorema 2 (stop-gate de Koszul divisor).** Para todo conjunto finito de
primos \(P\), el complejo positivo

\[
 K_P^\bullet=V_P\otimes\Lambda^\bullet\mathbb C^P,
 \qquad
 d_E=\sum_{p\in P}N_p\otimes\varepsilon_p
\tag{22}
\]

satisface:

1. \(d_E^2=0\);
2. las correlaciones mixtas \(N_p^*N_q\), \(p\ne q\), se cancelan en el
   laplaciano de Hodge;
3. la conexión Möbius--divisor es nulo-homotópica:

\[
 M_P\delta Z_P
 =d_E\left(\sum_{p\in P}\log p\,\iota_p\right)
 +\left(\sum_{p\in P}\log p\,\iota_p\right)d_E.
\tag{23}
\]

En particular, este complejo no puede satisfacer simultáneamente las
propiedades 1--3 de 104_12 §8: al realizar la propiedad 2 destruye la
propiedad 1, independientemente de qué operador Gamma se agregue después
sobre la cohomología.

**Prueba.** La primera afirmación usa la conmutación de los \(N_p\) y la
anticomutación exterior. La segunda es (17)--(18) para cada par. La tercera
sigue de \(d_E\iota_p+\iota_pd_E=N_p\) y de (7). \(\square\)

La misma conclusión vale para cualquier complejo \((C,d)\) en el que
existan homotopías \(h_p\) con

\[
 N_p=dh_p+h_pd.
\tag{24}
\]

En efecto, \(M\delta Z=dh+hd\), con
\(h=\sum_p(\log p)h_p\). Esta extensión es formal y no depende de la
elección de métrica.

Lo que **no** prueba el teorema debe quedar igualmente explícito. Podría
intentarse un diferencial no local construido a partir de combinaciones como
\(N_p^*N_q\), de modo que los cocientes mixtos fueran exactos sin que cada
\(N_p\) lo fuera. El argumento anterior no lo excluye. Pero tal construcción
ya no es el complejo de Koszul de la inversión Möbius y todavía tendría que:

* producir (7), no solo conservarlo formalmente;
* cancelar todos los canales repetidos en truncaciones mayores;
* identificar su diagonal positiva con el presupuesto arquimediano exacto
  \(\Delta A_n/2\), sin usar AHM, A1 ni positividad de Li.

Ninguna de esas tres tareas se obtiene de (22).

## 5. Decisión

Probado:

* el complejo graduado positivo mínimo del cubo divisor;
* \(d_E^2=0\) en \(\{1,p\}\), \(\{1,p,q,pq\}\) y todo cubo booleano;
* cancelación exacta de los canales mixtos \(p/q\) en el laplaciano;
* nulhomotopía exacta de \(M\delta Z\).

Descartado:

* el complejo de Koszul divisor como complejo Euler--Gamma de 104_12 §8;
* cualquier variante que declare nulo-homotópicos los generadores \(N_p\).

No descartado:

* un complejo no local que mate solo correlaciones cuadráticas y no los
  \(N_p\);
* una construcción independiente de su diagonal Gamma exacta.

No probado: una cota nueva para los pesos \(\Lambda\), A1 o RH.
