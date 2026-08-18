# 104_14 — M3 no local: forma completada y stop-gate estacionario

## Veredicto

M3 no produce una desigualdad nueva. La completación no local canónica del test de
Laguerre ya es la autocorrelación de Weil de `103_69`. Para el objetivo **A1**, no para
el margen más fuerte \(D_n\), se obtiene la identidad exacta

\[
 \boxed{
  C_n^\theta(T)
  ={1\over2}\mathcal W_\zeta(f_n*f_n^\#)-\theta A_n-R_n(T).}
 \tag{1}
\]

Por tanto A1 es exactamente la positividad del miembro derecho de (1). En la línea
crítica el símbolo espectral de la autocorrelación es un módulo cuadrado; fuera de la
línea es un producto recíproco de signo indefinido. El mapa estacionario

\[
 \gamma\longmapsto u_\gamma={n\over\gamma^2}
 \tag{2}
\]

retiene la altura, pero pierde la coordenada radial del cero. Esa coordenada es
precisamente la que genera el defecto de signo.

Se da abajo un falsificador exacto dentro del **bulk**, no en un borde: para todo
\(n\ge300\) divisible por \(100\), un cuarteto que satisface la simetría funcional cae en
un único punto estacionario con

\[
 {9\over2500}n<u_\gamma<{1\over225}n,
 \tag{3}
\]

pero aporta una cantidad estrictamente negativa a la autocorrelación completada. Un
divisor crítico con la misma multiconfiguración de alturas aporta una cantidad no
negativa. Luego ningún Gram cuyo signo provenga solamente del apareamiento
cero--lóbulo, la geometría de Laguerre y las simetrías del divisor puede probar A1.

Este stop-gate **no refuta** una desigualdad especial para los pesos reales
\(\Lambda(m)\). Prueba que M3, tal como estaba especificado, no contiene esa desigualdad:
el mapa estacionario organiza los términos pero no aporta el signo aritmético faltante.
No se prueba A1 ni RH.

---

## 1. Forma no local exacta de A1

Póngase, como en `103_69`,

\[
 f_n(x)={\bf1}_{[0,\infty)}(x)L_{n-1}^{(1)}(x),
 \qquad f^\#(x)=e^x\overline{f(-x)},
 \qquad h_n=f_n*f_n^\# .
 \tag{4}
\]

Su transformada de Laplace es, con \(w=(s-1)/s\),

\[
 \mathcal Lh_n(s)
 =\left(1-w^n\right)\left(1-w^{-n}\right)
 =2-w^n-w^{-n}.
 \tag{5}
\]

La fórmula explícita completada, con polo, Gamma, primos, conjugación y bordes
conservados antes de evaluar, da

\[
 \boxed{\mathcal W_\zeta(h_n)=2\lambda_n.}
 \tag{6}
\]

Por otro lado, `104_01`, Teorema 1, prueba sin hipótesis sobre ceros que

\[
 C_n^\theta(T)=\lambda_n-\theta A_n-R_n(T).
 \tag{7}
\]

Las ecuaciones (6)--(7) prueban (1), y `104_01`, Teorema 2, da

\[
 \boxed{
 \mathrm{A1}_\theta(T)
 \iff
 {1\over2}\mathcal W_\zeta(h_n)-\theta A_n-R_n(T)\ge0.}
 \tag{8}
\]

Ésta es ya una factorización no local: \(h_n\) es una autocorrelación sobre toda la
recta aditiva. No se separó el lado primo del arquimediano.

Sobre \(s=\frac12+it\) se tiene \(1-s=\bar s\), y por (5)

\[
 \mathcal Lh_n(s)=|1-w^n|^2\ge0.
 \tag{9}
\]

Fuera de esa recta, \(w^{-1}\ne\bar w\) y (5) no es un módulo cuadrado. La palabra
«autocorrelación» hace positivo el símbolo solamente después de identificar la
involución funcional \(s\mapsto1-s\) con conjugación, identificación equivalente a
estar sobre la recta crítica.

Así, (8) conserva exactamente todos los términos pedidos por M3, pero no da una cota:
la cota faltante es el propio miembro derecho de (8).

---

## 2. Qué conserva y qué pierde el mapa estacionario

En el régimen en que la fase de Laguerre es \(2\sqrt{nu}\), el término de un cero de
altura positiva \(\gamma\) tiene fase

\[
 \gamma u-2\sqrt{nu},
 \qquad
 {d\over du}\left(\gamma u-2\sqrt{nu}\right)
 =\gamma-\sqrt{n/u}.
 \tag{10}
\]

Esto produce (2). La abscisa \(\beta\) no entra en la localización del punto crítico,
pero sí entra en la amplitud \(e^{(\beta-1/2)u}\). En la coordenada de Cayley entra como
el módulo de

\[
 w_\rho=1-{1\over\rho}=e^{-a+i\vartheta}.
 \tag{11}
\]

Un cuarteto no crítico contribuye a (6)

\[
 \boxed{
 8-8\cosh(na)\cos(n\vartheta).}
 \tag{12}
\]

Por tanto (2) descarta justamente \(a\), el parámetro que puede volver (12)
exponencial y de ambos signos. Además el conteo de ceros es
\(N(\sqrt n)\sim(\sqrt n/4\pi)\log n\), mientras hay \(\asymp n\) lóbulos de
Laguerre: (2) no es una biyección y varios ceros pueden caer en un mismo lóbulo.

Nada de esto invalida el método de fase estacionaria como estimación. Sí impide usar su
punto crítico como fuente de positividad exacta.

La fase uniforme de Plancherel--Rotach en todo el bulk no es literalmente
\(2\sqrt{nu}\); (10) es la aproximación de pequeña razón \(u/n\) usada para proponer
(2). El falsificador siguiente concede (2) en sus propios términos. Si se sustituye
por la fase bulk exacta, la conclusión de signo no cambia: la ecuación estacionaria
sigue dependiendo de \(n\) y de la frecuencia \(\gamma\), no de \(\beta\). Los dos
divisores de §3.5 tienen la misma multiconfiguración de \(\gamma\) y por ello también
los mismos puntos críticos para la fase uniforme correcta.

---

## 3. Falsificador off-line dentro del bulk

### 3.1 Construcción

Sea \(n\ge300\) divisible por \(100\), y defínase

\[
 \vartheta={\pi\over50},
 \qquad
 r={1+\cos\vartheta\over2},
 \qquad
 w=re^{i\vartheta},
 \qquad
 \rho={1\over1-w}.
 \tag{13}
\]

Como \(\cos\vartheta<r<1\), el punto \(\rho=\beta+i\gamma\) está estrictamente en
la mitad derecha de la banda crítica. En efecto, con

\[
 D=|1-w|^2=1-2r\cos\vartheta+r^2,
 \tag{14}
\]

se tiene

\[
 \beta={1-r\cos\vartheta\over D},
 \qquad
 \gamma={r\sin\vartheta\over D},
 \tag{15}
\]

y las identidades

\[
 \beta-{1\over2}={1-r^2\over2D}>0,
 \qquad
 1-\beta={r(r-\cos\vartheta)\over D}>0
 \tag{16}
\]

prueban \(1/2<\beta<1\). Se completa el cuarteto con

\[
 \rho,\quad\bar\rho,\quad1-\rho,\quad1-\bar\rho.
 \tag{17}
\]

Satisface conjugación y la simetría funcional. Sus dos miembros de altura positiva
tienen exactamente la misma altura \(\gamma\), de modo que (2) les asigna el mismo
\(u_\gamma\).

### 3.2 La altura está en el bloque \(<\sqrt n\)

Para \(0<r<1\), la función de (15) es estrictamente creciente:

\[
 {d\gamma\over dr}
 ={\sin\vartheta(1-r^2)\over D^2}>0.
 \tag{18}
\]

Evaluando en los extremos \(r=\cos\vartheta\) y \(r\uparrow1\), resulta

\[
 \cot\vartheta<\gamma<{1\over2}\cot{\vartheta\over2}.
 \tag{19}
\]

Las desigualdades elementales
\(\sin x<x\), \(\cos x>1-x^2/2\), \(\tan x>x\),
\(3<\pi<22/7\) dan

\[
 \cot\vartheta>{1\over\vartheta}-{\vartheta\over2}
 >{175\over11}-{11\over350}>15,
 \tag{20}
\]

y

\[
 {1\over2}\cot{\vartheta\over2}
 <{1\over\vartheta}={50\over\pi}<{50\over3}<\sqrt{300}\le\sqrt n.
 \tag{21}
\]

Luego el cuarteto pertenece al bloque incompleto de `104_02`.

### 3.3 El punto estacionario está uniformemente en el bulk

De (20)--(21),

\[
 {9\over2500}n<{n\over\gamma^2}<{1\over225}n.
 \tag{22}
\]

Para \(n\ge300\), el extremo izquierdo es mayor que \(1>\log2\), y el derecho es
menor que \(4n\). Más aún, \(u_\gamma/n\) queda en el intervalo compacto fijo
\((9/2500,1/225)\subset(0,4)\): el ejemplo no usa ni el borde duro ni el borde
blando de Plancherel--Rotach.

Si para un índice particular \(u_\gamma\) coincidiera con un cero de Laguerre, se
reemplaza \(r\) por un punto suficientemente próximo dentro de
\((\cos\vartheta,1)\). Hay solo finitos valores prohibidos, mientras (16),
(20)--(22) y el signo siguiente son abiertos y se conservan.

### 3.4 Signo adverso exacto

Póngase \(a=-\log r>0\). Como \(100\mid n\),

\[
 n\vartheta={n\pi\over50}=2\pi{n\over100},
 \qquad \cos(n\vartheta)=1.
 \tag{23}
\]

La contribución (12) del cuarteto a la forma completada es por tanto

\[
 \boxed{8-8\cosh(na)<0.}
 \tag{24}
\]

Puede repetirse el cuarteto con multiplicidad \(M\), multiplicando (24) por \(M\),
sin alterar sus alturas ni las simetrías usadas por el mapa.

### 3.5 Misma información cero--lóbulo, signo opuesto

Considérese ahora el par crítico \(1/2\pm i\gamma\) con multiplicidad dos. Tiene la
misma multiconfiguración de alturas que (17), por lo que (2) produce exactamente los
mismos puntos estacionarios con la misma multiplicidad. Si

\[
 1-{1\over1/2+i\gamma}=e^{i\phi},
 \tag{25}
\]

su contribución a (6) es

\[
 8\{1-\cos(n\phi)\}\ge0.
 \tag{26}
\]

Las entradas que ve el mapa (2) coinciden; los signos de (24) y (26) no. Por tanto
ninguna regla de signo que dependa solamente de alturas, ocupación de lóbulos,
conjugación y simetría funcional puede representar la forma completada.

El divisor (17) no pretende tener el Euler producto de \(\zeta\). Ésa es precisamente
la frontera lógica del falsificador: descarta todo argumento que no use información
adicional de los pesos reales de von Mangoldt. No descarta un teorema aritmético nuevo
que sí la use.

---

## 4. Obstrucción algebraica a un Gram de las cargas de lóbulo

Hay un stop-gate independiente en el lado primo. En un cutoff finito escribamos las
cargas firmadas por lóbulo como \(c=(c_1,\ldots,c_m)\). A1 es afín en esas cargas:

\[
 \mathcal A(c)=q_{n,\theta}-\sum_{j=1}^m c_j.
 \tag{27}
\]

Supóngase que, en una familia abierta de perturbaciones de las cargas, existiera una
representación de Gram no local

\[
 \mathcal A(c)=
 \begin{pmatrix}1&c^T\end{pmatrix}
 G
 \begin{pmatrix}1\\c\end{pmatrix},
 \qquad G\succeq0.
 \tag{28}
\]

La Hessiana del lado izquierdo es cero. Luego el bloque \(G_{cc}\) es cero. Como
\(G\succeq0\), cada menor principal \(2\times2\) que contiene la primera coordenada
obliga también a \(G_{1c}=0\). El lado derecho de (28) sería constante, contradiciendo
(27).

Así, una forma PSD en el vector de cargas no puede convertir por identidad el
funcional lineal de A1 en un cuadrado. Si se añaden términos firmados para cancelar la
Hessiana, queda una diferencia de Gram y controlar su parte negativa vuelve a ser
(27). Si se usan variables no lineales como \(\sqrt{\Lambda(m)}\), aparecen términos
cruzados; para pesos independientes deben anularse, dejando los pesos diagonales
oscilatorios ya refutados en `103_60` y `103_64`.

Este argumento no prohíbe una identidad especial satisfecha solo por la sucesión real
\(\Lambda\). Dice que tal identidad tendría que ser el nuevo input aritmético; no puede
provenir de la geometría de lóbulos ni de una polarización formal.

---

## 5. Relación con los no-go previos

* `103_64` prueba que el tent matrix colapsa exactamente al sawtooth
  \(t-1-\psi(t)\), y mata PSD local, positividad total, Monge y orden convexo.
* `103_69` construye la autocorrelación completada (4)--(6) y muestra que el
  producto recíproco no es un módulo cuadrado fuera de la línea.
* El presente documento conecta esos dos hechos **directamente con A1** mediante
  (1) y añade el falsificador bulk (13)--(26). El mapa estacionario no repara ninguno
  de los defectos anteriores porque olvida \(a\).

No queda una matriz candidata, una identidad aritmética adicional ni una desigualdad
intermedia más débil que A1 dentro de M3. La afirmación superviviente es literalmente

\[
 {1\over2}\mathcal W_\zeta(h_n)\ge
 \theta A_n+R_n(T_n),
 \tag{29}
\]

que por (8) es A1.

---

## 6. Decisión

```text
probado:
  la forma completada no local exacta (1);
  A1 equivale exactamente a (8), sin sustituirla por el margen D_n;
  el mapa estacionario pierde el parámetro radial que determina el defecto;
  un cuarteto off-line cae uniformemente en el bulk y da signo negativo;
  la misma multiconfiguración de alturas sobre la línea da signo no negativo;
  un Gram PSD del vector de cargas no puede representar un funcional afín no constante.

descartado:
  M3 como signo derivado del apareamiento cero--lóbulo;
  una PSD no local obtenida solo de geometría, simetría funcional y conjugación;
  presentar la autocorrelación de Weil como una positividad incondicional.

no probado:
  una desigualdad especial nueva para los pesos reales de von Mangoldt;
  (29), A1 o RH.

decisión:
  M3 queda cerrado como stop-gate en su especificación actual.
  Solo se reabre si aparece una identidad aritmética concreta que use la sucesión
  real Lambda y que no sea equivalente, tras simplificar, a (29).
```
