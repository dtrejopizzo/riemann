# 104_61 — Criterio subexponencial en densidad y partición aritmética no lineal

**Estado.** Este documento reduce otra vez el cuantificador necesario para
probar RH. El margen cuártico \(4\lambda _n>A_n\) no es necesario: basta una
cota inferior polinómica —incluso la cota constante \(\lambda_n\ge-1\)— fuera
de una excepción de densidad logarítmica cero, o en bloques consecutivos de
longitud no acotada.

También se construyen dos observables no lineales. El principal es una
partición acotada de tipo Fermi--Dirac: detecta una densidad positiva de
excursiones sin exigir una cota en cada grado. El segundo es una partición
exponencial no acotada que admite una factorización aritmética especialmente
simple, pero que sí impone control coeficiente a coeficiente y por tanto es un
criterio auxiliar más fuerte. Ambos conservan juntos polo, factor arquimediano
y todos los pesos \(\Lambda(m)\) antes de aplicar la no linealidad. Las
identidades son exactas; las cotas superiores equivalentes a RH no se prueban.

---

## 1. Único input: los modos dominantes

Usaremos el Teorema 3.1 de `104_56`. Si RH es falsa, existen constantes

\[
 R>1,\qquad c>0,\qquad n_0\ge1                         \tag{1}
\]

y un conjunto \(D\subset\mathbb N\) que es sindético y tiene densidad
natural \(d>0\), tales que

\[
 \boxed{\lambda_n\le-cR^n\qquad(n\in D,\ n\ge n_0).} \tag{2}
\]

La prueba de (2) no supone distribución aleatoria de fases. Parte del número
finito de modos exteriores de módulo máximo y de los retornos de una rotación
en el grupo compacto generado por sus fases. Por sumación parcial, \(D\)
también tiene densidad logarítmica \(d\).

Bajo RH, en cambio, el criterio de Li da

\[
 \lambda_n\ge0\qquad(n\ge1).                       \tag{3}
\]

Todo lo que sigue es una consecuencia de la dicotomía (2)--(3).

---

## 2. Un criterio con cualquier barrera subexponencial

Sea \(b=(b_n)_{n\ge1}\) una sucesión no negativa tal que

\[
 \boxed{\log(1+b_n)=o(n).}                         \tag{4}
\]

Esto incluye \(b_n=1\), \(b_n=Cn^B\) y
\(b_n=\exp(o(n))\).

**Teorema 2.1 (criterio de barrera débil).** Para toda sucesión \(b\) que
satisface (4), son equivalentes:

1. RH;
2. existe \(E\subset\mathbb N\), de densidad logarítmica superior cero,
   tal que

   \[
    \lambda_n\ge-b_n                              \tag{5}
   \]

   para todo \(n\) suficientemente grande fuera de \(E\);
3. existen intervalos enteros consecutivos \(I_j\), con
   \(|I_j|\to\infty\), sobre los que (5) vale en cada índice.

**Demostración.** RH implica (5) con \(E=\varnothing\), por (3), y permite
tomar intervalos arbitrariamente largos.

Supóngase ahora que RH es falsa. Ponga \(r=\log R>0\). De (4), para todo
\(n\) suficientemente grande,

\[
 b_n\le e^{rn/2}<cR^n.                             \tag{6}
\]

La segunda desigualdad solo exige aumentar el umbral para absorber \(c\).
Por (2), (5) falla en todos los elementos suficientemente grandes de \(D\).
Como \(D\) tiene densidad logarítmica \(d>0\), no puede estar contenido,
salvo finitos elementos, en un conjunto \(E\) de densidad logarítmica
superior cero. Esto contradice 2.

Como \(D\) es sindético, existe \(L\) tal que todo intervalo de \(L\)
enteros suficientemente grandes contiene un elemento de \(D\). En ese
elemento falla (5). Por tanto las longitudes de los bloques buenos están
acotadas, contradiciendo 3. \(\square\)

En particular:

\[
 \boxed{
 \mathrm{RH}
 \iff \lambda_n\ge-1\text{ en bloques consecutivos de longitud no acotada}.}
                                                               \tag{7}
\]

Y, para cualesquiera \(C>0\), \(B\ge0\),

\[
 \boxed{
 \mathrm{RH}
 \iff \lambda_n\ge-Cn^B
 \text{ fuera de una excepción de densidad logarítmica cero}.} \tag{8}
\]

Estas condiciones son estrictamente más débiles, como enunciados sobre una
sucesión arbitraria, que \(4\lambda_n>A_n\). Se vuelven equivalentes a RH
solo por la rigidez exponencial de los modos dominantes de los coeficientes
de Li.

Una forma intrínseca de (8) es

\[
 \mathrm{RH}\iff
 \exists E,\ \overline\delta_{\log}(E)=0:\quad
 \limsup_{\substack{n\to\infty\\n\notin E}}
 {1\over n}\log\bigl(1+\lambda_n^-\bigr)=0,
 \qquad \lambda_n^-:=\max\{-\lambda_n,0\}.          \tag{9}
\]

---

## 3. Detector logarítmico no lineal

Defina

\[
 x_n(b):=(-\lambda_n-b_n)_+,
 \qquad
 \Phi(x):={x\over1+x},                              \tag{10}
\]

y, con \(H_X=\sum_{n\le X}1/n\),

\[
 \boxed{
 \mathfrak M_b(X):={1\over H_X}
 \sum_{n\le X}{1\over n}\Phi\!\left(x_n(b)\right).} \tag{11}
\]

Éste no es un promedio Abel de la generatriz. Primero aplica una barrera
no lineal al coeficiente completo y después promedia en el **grado** \(n\).

**Teorema 3.1 (criterio promedio acotado).** Para todo \(b\) que satisface
(4),

\[
 \boxed{\mathrm{RH}\iff \mathfrak M_b(X)\longrightarrow0.}   \tag{12}
\]

**Demostración.** Bajo RH, \(x_n(b)=0\) para todo \(n\), así que (11) es
idénticamente cero. Si RH es falsa, entonces (2) y (6) dan
\(x_n(b)\to\infty\) a lo largo de \(D\). Por tanto
\(\Phi(x_n(b))\to1\) sobre \(D\). Como \(D\) tiene densidad logarítmica
\(d\),

\[
 \liminf_{X\to\infty}\mathfrak M_b(X)\ge d>0.       \tag{13}
\]

Esto contradice el lado derecho de (12). \(\square\)

El detector (11) solo pide excluir una proporción logarítmica positiva de
excursiones subexponencialmente profundas. No intenta recuperar el signo de
cada coeficiente.

### 3.1 Partición acotada de Fermi--Dirac

Suponga además que \(b_n\to\infty\), y fije \(t>0\). Defina

\[
 \boxed{
 \mathfrak F_{t,b}(X):={1\over H_X}\sum_{n\le X}{1\over n}
 {1\over1+\exp\!\bigl(t(\lambda_n+b_n)\bigr)}.}     \tag{13a}
\]

**Teorema 3.2 (partición acotada).** Para toda barrera no negativa que
satisfaga (4) y \(b_n\to\infty\), y para cualquier \(t>0\),

\[
 \boxed{\mathrm{RH}\iff\mathfrak F_{t,b}(X)\longrightarrow0.} \tag{13b}
\]

**Demostración.** Bajo RH, \(\lambda_n\ge0\), luego el sumando acotado de
(13a) es a lo sumo \((1+e^{tb_n})^{-1}\to0\). Su media logarítmica tiende
a cero. Si RH es falsa, (2) y (4) dan
\(\lambda_n+b_n\to-\infty\) sobre \(D\). El sumando tiende entonces a uno
sobre un conjunto de densidad logarítmica \(d\), y

\[
 \liminf_{X\to\infty}\mathfrak F_{t,b}(X)\ge d>0.  \tag{13c}
\]

Esta formulación es suave y, a diferencia de la partición exponencial de la
sección siguiente, está acotada por uno. Por eso un pico aislado no puede
reemplazar una densidad positiva de picos. La elección concreta
\(b_n=\log(n+1)\) ya satisface todas las hipótesis.

La relajación es genuina para sucesiones arbitrarias. Por ejemplo, defina

\[
 a_n=n\quad(n\ne2^k),\qquad a_{2^k}=-e^{2^k}.     \tag{13d}
\]

Al sustituir \(\lambda_n\) por \(a_n\) en (13a), los índices excepcionales
aportan a la suma no normalizada a lo sumo
\(\sum_k2^{-k}<\infty\), y los restantes aportan una serie convergente.
Por tanto la media Fermi tiende a cero, aunque (13d) tiene excursiones
negativas exponenciales infinitas. Lo que excluye esas excursiones para los
coeficientes de Li no es el detector por sí solo, sino el Teorema 3.1 de
`104_56`: bajo \(\neg\mathrm{RH}\) no pueden ser dispersas, sino que
contienen un conjunto de densidad logarítmica positiva.

---

## 4. Criterio exponencial auxiliar

Para \(t>0\), ponga

\[
 \boxed{
 \mathcal Z_t(X):=\sum_{n\le X}{e^{-t\lambda_n}\over n}.}     \tag{14}
\]

**Teorema 4.1 (criterio de partición).** Son equivalentes:

1. RH;
2. para todo \(t>0\) y todo \(X\ge1\),
   \(\mathcal Z_t(X)\le H_X\);
3. existe \(t>0\) tal que

   \[
    \boxed{\mathcal Z_t(X)=O_t(\log X).}             \tag{15}
   \]

**Demostración.** La ecuación (3) implica
\(e^{-t\lambda_n}\le1\), de donde 1 implica 2, y 2 implica 3. Si RH es
falsa, elija una sucesión \(n_j\to\infty\) en \(D\). Por (2),

\[
 \mathcal Z_t(n_j)\ge{1\over n_j}
 \exp\!\left(tcR^{n_j}\right),                    \tag{16}
\]

lo que contradice (15) para cada \(t>0\). \(\square\)

A diferencia de (11) y (13a), (14) no es un detector acotado: amplifica una
sola excursión negativa. De hecho, (15) implica para cada grado

\[
 {e^{-t\lambda_n}\over n}\ll_t\log n,
 \qquad
 \lambda_n\ge-{1\over t}
 \bigl(\log n+\log\log n+O_t(1)\bigr).             \tag{16a}
\]

Por tanto (14)--(15) **no explotan** la relajación de densidad: constituyen
un criterio coeficiente a coeficiente, aunque más débil que positividad.
Su ventaja es exclusivamente algebraica: admiten la factorización exacta
de la sección siguiente.

---

## 5. Forma aritmética exacta antes del límite de Abel

Para \(\varepsilon>0\), defina

\[
 p_n(\varepsilon)
 :=n\sum_{k=1}^n{n-1\choose k-1}
 {(-1)^{k-1}\over k\varepsilon^k},                 \tag{17}
\]

\[
 \mathscr E_{n,\varepsilon}
 :=p_n(\varepsilon)
 -\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m).                            \tag{18}
\]

La identidad prima--Laguerre del ledger da

\[
 \lambda_n=A_n+\lim_{\varepsilon\downarrow0}
 \mathscr E_{n,\varepsilon}.                       \tag{19}
\]

La letra nueva es deliberada. En `104_30`,
\(P_{n,\varepsilon}\) denota la diferencia opuesta
\(\sum_m\Lambda(m)m^{-1-\varepsilon}L_{n-1}^{(1)}(\log m)
-p_n(\varepsilon)\), cuyo límite es \(A_n-\lambda_n\). Por tanto
\(\mathscr E_{n,\varepsilon}=-P_{n,\varepsilon}^{\text{`104_30`}}\);
(19) coincide exactamente con `104_28`--`104_30` y no introduce una segunda
convención de signo para \(P\).

Para \(\varepsilon>0\), la serie de (18) converge absolutamente. Como la
suma exterior es finita, (14) y (19) implican la identidad rigurosa

\[
\boxed{
\begin{aligned}
 \mathcal Z_t(X)
 &=\lim_{\varepsilon\downarrow0}
 \sum_{n\le X}{e^{-t(A_n+p_n(\varepsilon))}\over n}
 \exp\!\left(
 t\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m)\right)\\
 &=\lim_{\varepsilon\downarrow0}
 \sum_{n\le X}{e^{-t(A_n+p_n(\varepsilon))}\over n}
 \prod_{m\ge2}
 \exp\!\left(
 {t\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m)\right).
\end{aligned}}                                                   \tag{20}
\]

La segunda línea es un producto absolutamente convergente para cada
\(\varepsilon>0\). Todos sus factores son números reales positivos, aunque
sus exponentes cambian de signo con el kernel de Laguerre.

Esta representación es efectivamente truncable. En efecto,

\[
 L_{n-1}^{(1)}(u)=
 \sum_{k=0}^{n-1}{n\choose k+1}{(-u)^k\over k!}
\]

da, para \(u\ge0\),

\[
 |L_{n-1}^{(1)}(u)|
 \le 3\,2^n(1+u)^{n-1}.                            \tag{20a}
\]

En efecto, cada \(u^k/k!\le(1+u)^{n-1}\) para
\(0\le k\le n-1\), y
\(\sum_{k=0}^{n-1}{n\choose k+1}=2^n-1\); el factor \(3\) de (20a) es,
por tanto, holgura y no una constante asintótica oculta.

Usando \(\Lambda(m)\le\log m\), para todo entero
\(M\ge e^n\) la cola del exponente satisface

\[
\boxed{
 \sum_{m>M}{\Lambda(m)\over m^{1+\varepsilon}}
 |L_{n-1}^{(1)}(\log m)|
 \le3\,2^n\int_{\log M}^{\infty}
 e^{-\varepsilon u}u(1+u)^{n-1}\,du.}              \tag{20b}
\]

Para cerrar el test integral, ponga
\(f(x)=x^{-1-\varepsilon}\log x(1+\log x)^{n-1}\). Si
\(u=\log x\ge n\), entonces

\[
 {d\over du}\log f(e^u)
 ={1\over u}+{n-1\over1+u}-(1+\varepsilon)
 \le-\varepsilon<0,                                \tag{20b'}
\]

porque \(u^{-1}+(n-1)/(1+u)\le1\) equivale a
\(u(u-n+1)\ge1\). Por tanto
\(\sum_{m>M}f(m)\le\int_M^\infty f(x)\,dx\); el cambio
\(x=e^u\) produce exactamente (20b), sin factor omitido. El miembro derecho
es una combinación finita de gammas incompletas y tiende efectivamente a
cero. Así, para
\(X,\varepsilon,M\) finitos, (20) admite aritmética de intervalos con una
cola explícita; lo no uniforme está únicamente en
\(\varepsilon\downarrow0\).

La partición acotada (13a) posee la representación regulada paralela

\[
\boxed{
 \mathfrak F_{t,b}(X)
 =\lim_{\varepsilon\downarrow0}{1\over H_X}
 \sum_{n\le X}{1\over n}
 \left[1+e^{t(A_n+b_n+p_n(\varepsilon))}
 \prod_{m\ge2}\exp\!\left(
 -{t\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m)\right)\right]^{-1}.}        \tag{20c}
\]

Para cada \(\varepsilon>0\), el producto de (20c) converge absolutamente
en el sentido \(\sum_m|\log(\text{factor}_m)|<\infty\); la cola de su
logaritmo está acotada por \(t\) veces (20b). El paso al límite es legítimo
porque la suma exterior es finita y la función logística es continua.
Esta es la representación que conserva el contenido de densidad de
`104_56`: demostrar directamente que (20c) tiende a cero probaría RH sin
producir una cota individual para cada \(\lambda_n\).

Las ecuaciones (20) y (20c) son los puentes aritméticos exactos:

* conserva el polo \(p_n(\varepsilon)\), el bloque arquimediano \(A_n\),
  los primos y todas las potencias primas hasta después de formar el
  observable;
* no toma valores absolutos del kernel;
* crea interacciones multiplicativas entre potencias primas antes de
  promediar en \(n\);
* está fuera del clasificador polinómico-aditivo de `104_53` y fuera del
  promedio Abel lineal de `104_17`.

Por el Teorema 3.2, el frente que explota la densidad consiste en demostrar
directamente desde (20c), para un \(t>0\) fijo y por ejemplo
\(b_n=\log(n+1)\),

\[
 \boxed{\mathfrak F_{t,b}(X)\longrightarrow0.}       \tag{20d}
\]

Como criterio auxiliar más fuerte, el Teorema 4.1 permite intentar en (20)

\[
 \boxed{\mathcal Z_t(X)\ll_t\log X.}               \tag{21}
\]

Las afirmaciones (20d) y (21) son incondicionalmente equivalentes a RH;
las representaciones no demuestran ninguna de las dos.

---

## 6. Tres puentes inmediatos que fallan

### 6.1 Jensen tiene el sentido incorrecto

La función \(x\mapsto e^{-tx}\) es convexa. Jensen da una **cota inferior**

\[
 {1\over H_X}\sum_{n\le X}{e^{-t\lambda_n}\over n}
 \ge
 \exp\!\left(-{t\over H_X}\sum_{n\le X}{\lambda_n\over n}\right), \tag{22}
\]

no la cota superior (21). Controlar una media lineal de \(\lambda_n\) no
controla la partición.

### 6.2 Separar polo y potencias primas destruye el límite

Para \(n\) fijo,

\[
 L_{n-1}^{(1)}(u)
 ={(-1)^{n-1}\over(n-1)!}u^{n-1}+O_n(u^{n-2}).      \tag{23}
\]

El PNT y sumación parcial dan

\[
 \sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 \left|L_{n-1}^{(1)}(\log m)\right|
 \asymp_n\varepsilon^{-n}\qquad(\varepsilon\downarrow0).     \tag{24}
\]

Por tanto una mayorización factor a factor o por el valor absoluto del
exponente de (20) cuesta

\[
 \exp(c_nt\varepsilon^{-n}),                       \tag{25}
\]

mientras el límite emparejado de (20) es finito. La cancelación entre
\(p_n(\varepsilon)\) y la suma de Mangoldt debe conservarse dentro del
exponente; no puede recuperarse después de (25).

### 6.3 La positividad Abel previa no controla la partición

El falsificador racional de `104_17`,

\[
 \rho={1+2i\over5},\qquad w=2i,                    \tag{26}
\]

tiene coeficientes de cuarteto

\[
 Q_n=4-2\mathrm{Re}(w^n+w^{-n}),             \tag{27}
\]

y su germen Abel racional es positivo en todo \(0<q<1\). Sin embargo,

\[
 Q_{4k}=4-2(2^{4k}+2^{-4k})<-16k^2=-(4k)^2         \tag{28}
\]

para todo \(k\ge1\). En particular, la versión de (14) del cuarteto tiene
picos doblemente exponenciales sobre una clase de densidad \(1/4\). Así,
la información radial positiva de `104_17` no puede implicar (21), ni
siquiera después de permitir una excepción de densidad cero. La partición
acotada también detecta el falsificador: para toda \(b_n\to\infty\) con
\(\log(1+b_n)=o(n)\), el sumando de (13a), con \(\lambda_n\) reemplazado
por \(Q_n\), tiende a uno en \(n\equiv0\pmod4\) y a cero en las otras tres
clases. Por consiguiente su media logarítmica tiende a \(1/4\), no a cero.
La positividad Abel tampoco implica (20d).

La desigualdad estricta de (28) es elemental: si
\(F(k)=2\,16^k-4-16k^2\), entonces \(F(1)=12>0\) y

\[
 F(k+1)-F(k)=30\,16^k-16(2k+1)>0\qquad(k\ge1).
\]

Además \(Q_{4k}<4-2\,16^k=-16k^2-F(k)\).

Los tres puntos anteriores son no-gos para transferencias concretas. No son
un teorema de imposibilidad para una desigualdad nueva aplicada directamente
al funcional emparejado de (20c).

---

## 7. Resultado y frente nuevo

**Probado:**

\[
\boxed{
\begin{gathered}
 \mathrm{RH}
 \iff \lambda_n\ge-b_n
 \text{ fuera de una excepción de densidad logarítmica cero},\\
 \mathrm{RH}
 \iff \lambda_n\ge-b_n
 \text{ en bloques consecutivos de longitud no acotada},\\
 \mathrm{RH}
 \iff \mathfrak M_b(X)\to0,\\
 \mathrm{RH}
 \iff \mathfrak F_{t,b}(X)\to0
 \quad(b_n\to\infty),\\
 \mathrm{RH}
 \iff \mathcal Z_t(X)\ll_t\log X\quad\text{para algún }t>0,
\end{gathered}}
\tag{29}
\]

para toda barrera \(b_n\) que satisfaga \(\log(1+b_n)=o(n)\).

**Conexión aritmética probada:** las particiones exactas (20) y (20c), con
todos los canales emparejados.

**No probado:** la cota (21), los límites (12) o (20d) para los coeficientes
reales de zeta, A1 o RH.

La casilla principal no pide positividad, coercividad proporcional ni
control coeficiente a coeficiente. Pide la desaparición de la partición
acotada prima--polo (20c), una cota de densidad logarítmica en el grado.
La partición exponencial (20)--(21) queda como auxiliar algebraico más
fuerte y no debe confundirse con esa relajación. Ninguna de las dos sale de
los generadores descartados; ambas siguen teniendo fuerza RH y necesitan
una idea aritmética nueva.

---

## 8. Verificación reproducible

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 subexponential_density_partition_check.py
```

La herramienta usa `Fraction`. Verifica (27)--(28), la clase mala de
densidad \(1/4\), la ausencia de bloques buenos de longitud cuatro en el
falsificador y la positividad racional del germen Abel en varios puntos. La
equivalencia general y la identidad límite (20) están demostradas en el
texto, no por muestreo.
