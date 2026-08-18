# 104_79 — Ley zeta completada y gate de truncación profunda

**Resultado.** El bloque prima--polo de `104_75` posee una representación
probabilística exacta que usa los pesos ordinarios \(\Lambda(m)\) antes de
tomar el logaritmo. Si

\[
 \mathbb P_s(N=m)={m^{-s}\over\zeta(s)},\qquad
 Y\sim\operatorname{Exp}(s-1),
 \tag{1}
\]

son independientes y

\[
 \begin{aligned}
 P_n(u)&=L_{n-1}^{(1)}(u),\\
 J_n(N)&=\sum_{d\mid N}\Lambda(d)P_n(\log d),\\
 U_n(y)&=\int_0^yP_n(u)\,du=1-L_n^{(0)}(y),\\
 Z_{n,s}&=J_n(N)-U_n(Y),
 \end{aligned}                                             \tag{2}
\]

Use las normalizaciones de `104_75`, escritas aquí explícitamente:

\[
 Q_{n,\varepsilon}=\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 P_n(\log m),\qquad
 p_n(\varepsilon)=\int_0^\infty e^{-\varepsilon u}P_n(u)\,du
 =1-\left(1-{1\over\varepsilon}\right)^n.
\]

entonces, con \(s=1+\varepsilon\),

\[
 \boxed{\mathbb E_s Z_{n,s}=Q_{n,\varepsilon}-p_n(\varepsilon).}
 \tag{3}
\]

Esta identidad mantiene juntos todos los exponentes primos y el polo. Sin
embargo, la diagonal

\[
 \varepsilon_X=e^{-X/100},\qquad X/2\le n\le X             \tag{4}
\]

no es uniformemente integrable ni siquiera al nivel extremadamente
permisivo \(e^{\sqrt X}\) de `104_75`. Existe \(X_0\) tal
que, para todo entero \(X\ge X_0\) y todo entero
\(X/2\le n\le X\),

\[
 \boxed{
 \begin{aligned}
 \mathbb E_s\!\left[(Z_{n,s}-e^{\sqrt X})_+\right]
    &\ge e^{X^2/500},\\
 \mathbb E_s\!\left[(-Z_{n,s}-e^{\sqrt X})_+\right]
    &\ge e^{X^2/500}.
 \end{aligned}}                                           \tag{5}
\]

Las dos cotas se prueban sobre fibras aritméticas reales: una fibra prima
da el signo \((-1)^{n-1}\), y una fibra semiprima *squarefree* da el signo
opuesto. Sus probabilidades son solo \(\gg\varepsilon_X\) y
\(\gg\varepsilon_X/n\), respectivamente, pero en ellas
\(|Z_{n,s}|\ge e^{X^2/400}\). Por tanto una transformación acotada puede
asignarles masa tendiente a cero mientras cada una transporta una esperanza
de orden \(e^{cX^2}\).

Esto cierra el ataque estrecho

```text
representar Q-p como esperanza bajo exponentes primos independientes
+ truncar/comprimir Z al nivel exp(sqrt(X))
+ controlar el error por concentración o probabilidad de cola
    => gate profundo de 104_75.
```

No descarta una identidad firmada que calcule conjuntamente la diferencia
de las dos colas hasta precisión relativa \(e^{-cX^2}\). Pero esa diferencia
es exactamente la media (3); recuperarla devuelve la cancelación prima--polo
que se quería demostrar. Este documento no prueba el gate profundo, A1 ni
RH.

**No duplicación interna.** `104_54` prueba para \(n,s\) fijos que el
defecto Palm tiene momentos exponenciales bilaterales infinitos. Aquí el
resultado nuevo es diagonal y cuantitativo: se completa el defecto con una
variable polar independiente, se usa la diagonal exacta de `104_75`, y se
demuestra que ambos **primeros momentos de cola** por encima de
\(e^{\sqrt X}\) crecen como \(e^{cX^2}\), uniformemente en una banda de
grados de longitud proporcional a \(X\).

---

## 1. Representación exacta antes del logaritmo

Bajo (1), para todo entero \(d\ge1\),

\[
 \mathbb P_s(d\mid N)
 ={1\over\zeta(s)}\sum_{k\ge1}(dk)^{-s}=d^{-s}.           \tag{6}
\]

La renovación unitaria

\[
 \sum_{d\mid m}\Lambda(d)=\log m                         \tag{7}
\]

garantiza además que \(J_n\) es precisamente el selector divisor de
`104_43`/`104_49`, sin multiplicidades auxiliares. La convergencia absoluta,
válida porque \(s>1\) y \(P_n\) es un polinomio, permite usar Fubini y da

\[
 \mathbb E_sJ_n(N)
 =\sum_{d\ge2}{\Lambda(d)\over d^s}P_n(\log d)
 =Q_{n,s-1}.                                              \tag{8}
\]

Por otra parte,

\[
 \begin{aligned}
 \mathbb EU_n(Y)
 &=\mathbb E\int_0^Y P_n(u)\,du\\
 &=\int_0^\infty e^{-(s-1)u}P_n(u)\,du
 =p_n(s-1).                                               \tag{9}
 \end{aligned}
\]

La última igualdad es la transformada de Laguerre usada en `104_61` y
`104_75`. Las ecuaciones (8)--(9) prueban (3). En particular, el target
profundo

\[
 Q_{n,\varepsilon_X}-p_n(\varepsilon_X)
 \ge A_n+\log(n+1)+e^{\sqrt X}                            \tag{10}
\]

es una desigualdad para la **media** de \(Z_{n,s}\), no para una cola de
su ley.

---

## 2. Dos lemas polinómicos uniformes

La expansión exacta es

\[
 P_n(u)=\sum_{k=1}^n(-1)^{k-1}{n\choose k}{u^{k-1}\over(k-1)!},
 \qquad
 U_n(u)=\sum_{k=1}^n(-1)^{k-1}{n\choose k}{u^k\over k!}.
 \tag{11}
\]

### 2.1 Fibra prima

Si \(N=p\), \(x=\log p\) y \(0\le y\le x\), entonces

\[
 xP_n(x)-U_n(y)
 =\sum_{k=1}^n(-1)^{k-1}{n\choose k}
 {kx^k-y^k\over k!}.                                    \tag{12}
\]

El término principal tiene signo \((-1)^{n-1}\) y módulo al menos
\((n-1)x^n/n!\). La suma de los módulos de los términos inferiores,
dividida por ese módulo, es a lo sumo

\[
 {n+1\over n-1}
 \sum_{j=1}^{n-1}{(n^2/x)^j\over j!}
 \le2\{e^{n^2/x}-1\}.                                   \tag{13}
\]

Aquí se usó

\[
 {n!{n\choose n-j}\over(n-j)!}
 =\frac{(n!)^2}{j!\{(n-j)!\}^2}
 \le {n^{2j}\over j!}.                                  \tag{14}
\]

Por tanto, si \(n\ge3\) y \(x\ge8n^2\),

\[
 \boxed{(-1)^{n-1}\{xP_n(x)-U_n(y)\}
 \ge {n-1\over2n!}x^n.}                                 \tag{15}
\]

### 2.2 Fibra semiprima

Sean \(N=pq\), \(p\ne q\), \(x=\log p\), \(z=\log q\),
\(w=x+z\), y suponga

\[
 {1\over1.1}\le{x\over z}\le1.1,
 \qquad w\le y\le(1+1/n)w.                              \tag{16}
\]

Entonces

\[
 xP_n(x)+zP_n(z)-U_n(y)
 =\sum_{k=1}^n(-1)^{k-1}{n\choose k}
 {k(x^k+z^k)-y^k\over k!}.                              \tag{17}
\]

Para \(n\ge5\),

\[
 n(x^n+z^n)\le{w^n\over2},                              \tag{18}
\]

porque \(\max(x,z)/w\le1.1/2.1=11/21\) y
\(2n(11/21)^n\le1/2\) desde \(n=5\). Luego el término
principal de (17) tiene signo \((-1)^n\) y módulo al menos
\(w^n/(2n!)\). Como \(y^k\le e w^k\), la razón entre la suma de los
términos inferiores y ese principal es a lo sumo

\[
 6n\sum_{j=1}^{n-1}{(n^2/w)^j\over j!}
 \le6n\{e^{n^2/w}-1\}.                                  \tag{19}
\]

Además,
\(6n\{e^{1/(100n)}-1\}<1/2\). Así, para \(n\ge5\) y
\(w\ge100n^3\),

\[
 \boxed{(-1)^n\{xP_n(x)+zP_n(z)-U_n(y)\}
 \ge {w^n\over4n!}.}                                    \tag{20}
\]

Las constantes 8 y 100 solo fijan un umbral; en la diagonal (4),
\(x,z\asymp\varepsilon_X^{-1}=e^{X/100}\), de modo que ambas
condiciones valen uniformemente para \(n\le X\).

---

## 3. Masa real de las fibras

Ponga

\[
 L=\varepsilon^{-1},\qquad
 I_\varepsilon=\{p:\ L\le\log p\le1.1L\},
 \qquad
 S_\varepsilon=\sum_{p\in I_\varepsilon}p^{-1-\varepsilon}.
 \tag{21}
\]

El PNT y sumación parcial dan

\[
 S_\varepsilon\longrightarrow
 c_0:=\int_1^{1.1}{e^{-v}\over v}\,dv>0                 \tag{22}
\]

cuando \(\varepsilon\downarrow0\). También
\(\zeta(1+\varepsilon)^{-1}\sim\varepsilon\). Por tanto,
para \(\varepsilon\) suficientemente pequeño,

\[
 \mathbb P_s\{N=p\in I_\varepsilon\}\ge c_1\varepsilon.
 \tag{23}
\]

Como \(Y\) es independiente y, en esa fibra,
\(\mathbb P(Y\le\log p)\ge1-e^{-1}\), (23) y (15) muestran que
el signo \((-1)^{n-1}\) ocurre con probabilidad al menos
\(c_2\varepsilon\).

Para la fibra semiprima, escriba

\[
 \sum_{\substack{p<q\\p,q\in I_\varepsilon}}(pq)^{-s}
 ={1\over2}\left{S_\varepsilon^2-
       \sum_{p\in I_\varepsilon}p^{-2s}\right}
 \ge c_3>0.                                              \tag{24}
\]

La última suma tiende a cero porque cada \(p\ge e^L\). Si
\(w=\log(pq)\), entonces \(2\le\varepsilon w\le2.2\), y

\[
 \begin{aligned}
 \mathbb P\{w\le Y\le(1+1/n)w\}
 &=e^{-\varepsilon w}{1-e^{-\varepsilon w/n}\}\\
 &\ge {c_4\over n}.                                      \tag{25}
 \end{aligned}
\]

De (24)--(25), la fibra de signo \((-1)^n\) tiene probabilidad al
menos \(c_5\varepsilon/n\).

---

## 4. Explosión bilateral por encima del gate profundo

**Teorema 4.1 (falla bilateral de uniformidad profunda).** Tome (4). Para
\(X/2\le n\le X\), Stirling elemental
\(n!\le n^n\) da, uniformemente,

\[
 \log{L^n\over n!}
 \ge n\left({X\over100}-\log X\right)
 \ge {X^2\over400}                                      \tag{26}
\]

desde un \(X_0\) absoluto. En la fibra prima, (15) es al menos
\(L^n/n!\) para \(n\ge3\); en la semiprima, (20) es al menos
\((2L)^n/(4n!)\ge L^n/n!\). Por tanto, sobre las fibras de §§2--3,

\[
 |Z_{n,s}|\ge e^{X^2/400}>e^{\sqrt X}.                   \tag{27}
\]

Una de ellas da la cola positiva y la otra la negativa, según la paridad
de \(n\). Como
\(e^{X^2/400}-e^{\sqrt X}\ge\tfrac12e^{X^2/400}\) para \(X\)
grande, multiplicar el exceso sobre el umbral por las probabilidades de
(23)/(25) produce

\[
 {c\varepsilon_X\over n}e^{X^2/400}
 \ge e^{X^2/500}                                        \tag{28}
\]

para \(X\) grande, lo que prueba simultáneamente las dos desigualdades
de (5).

Obsérvese la separación de escalas:

\[
 \underbrace{\mathbb P(\text{fibra testigo})}_{\to0}
 \times
 \underbrace{|Z_{n,s}|}_{\exp(\Theta(X^2))}
 =\underbrace{\text{momento de cola}}_{\exp(\Theta(X^2))}.
 \tag{29}
\]

Una cota de probabilidad, una mediana o una compresión acotada ve el primer
factor; la media exacta (3) depende del producto y de la cancelación entre
los dos signos.

---

## 5. Alcance lógico

Para toda variable integrable y todo \(a>0\),

\[
 \mathbb EZ
 =\mathbb E\operatorname{clip}_{[-a,a]}(Z)
  +\mathbb E(Z-a)_+-\mathbb E(-Z-a)_+,                 \tag{30}
\]

Tome \(a=e^{\sqrt X}\). Los dos términos de exceso de (30) son, por
(5), al menos \(e^{X^2/500}\), mientras el término recortado tiene módulo
a lo sumo \(e^{\sqrt X}\). Por ello, un argumento que intente recuperar
la diferencia estimando **por separado** ambos términos positivos con
errores relativos uniformes debe alcanzar la escala
\(\exp\{-X^2/500+\sqrt X\}\). Truncarlos por separado, usar valor
absoluto, o sustituirlos por una probabilidad acotada no controla ese
error aditivo.

Este resultado no afirma que toda transformación acotada imaginable sea
inútil ni que toda estimación conjunta de las colas requiera esa precisión
relativa. Afirma el no-go preciso que se ha probado: la ley zeta completada
no satisface uniformidad de primeros momentos de cola al nivel del target
profundo, de modo que concentración más un error de truncación separado no
transporta (3) a `104_75`. Un sucesor tendría que aportar una identidad
aritmética firmada
que cancele las fibras prima y semiprima junto con todas las demás; por
(3), su salida es otra vez \(Q-p\).

El mismo test también explica por qué la multiplicidad unitaria no basta
como principio probabilístico aislado. Las fórmulas de las fibras prima y
semiprima usan exactamente \(\Lambda(p)=\log p\), pero el selector
desplazado de `104_54` coincide con ellas en esas dos fibras. Para distinguir
la zeta real sigue haciendo falta una interacción global que no se reduzca
a concentración de sus exponentes independientes.

---

## 6. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 zeta_law_deep_truncation_check.py
```

El checker usa `Fraction` para verificar las expansiones (11)--(12)/(17),
los signos de los términos principales, las cotas de dominancia en puntos
racionales y la separación de escalas de (26)--(28). La estimación de masa
prima (22) se prueba analíticamente por PNT; no se sustituye por una suma
numérica de primos astronómicos.
