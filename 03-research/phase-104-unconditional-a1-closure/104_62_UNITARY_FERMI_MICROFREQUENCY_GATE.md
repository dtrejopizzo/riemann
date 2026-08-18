# 104_62 — Transformada Fermi unitaria y gate de microfrecuencia

**Resultado.** La partición Fermi de `104_61` admite una representación
exacta en la que el bloque prima--polo completo aparece dentro de fases de
módulo uno. Esto elimina la explosión artificial que producía separar los
exponentes de la partición no acotada.

La representación no da por sí sola una cota nueva para zeta. El obstáculo
se localiza con una constante explícita: una excursión negativa de
profundidad \(Y\) es detectada en frecuencias \(s=O(Y^{-1})\). En el
cuarteto racional \(w=2i\), esa ventana es \(s=O(2^{-n})\). Por tanto un
ataque a frecuencia fija, o con resolución solo polinómica en el grado,
omite la señal que la partición fue construida para conservar.

La última coordenada auditada no elimina \(s\downarrow0\): usa el cambio
diagonal \(s=e^{-nv}\). Éste lleva una tasa \(Y_n\asymp e^{an}\) al punto
fijo \(v=a\), conserva fases unitarias y alinea su primera variación con la
generatriz exacta de Laguerre. Pero la generatriz solo calcula el producto
geométrico de fases, mientras Fermi exige su media aritmética. En la escala
crítica todos los poderes de Hadamard sobreviven. Por eso la rama diagonal
queda cerrada como stop-gate, no como sucesor ni como prueba de A1 o RH.

---

## 1. Notación y regulador aritmético

Fijemos \(t>0\),

\[
 b_n=\log(n+1),\qquad x_n=\lambda_n+b_n,\qquad
 H_X=\sum_{n\le X}{1\over n}.                              \tag{1}
\]

La partición acotada es

\[
 \mathfrak F_t(X)={1\over H_X}\sum_{n\le X}{1\over n}
 {1\over1+e^{t x_n}}.                                      \tag{2}
\]

Para \(\varepsilon>0\), usemos la convención de `104_61`:

\[
\begin{aligned}
 p_n(\varepsilon)
 &=n\sum_{k=1}^n{n-1\choose k-1}
   {(-1)^{k-1}\over k\varepsilon^k},\\
 \lambda_{n,\varepsilon}
 &=A_n+p_n(\varepsilon)
 -\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m).
\end{aligned}                                               \tag{3}
\]

Entonces

\[
 \lambda_{n,\varepsilon}\longrightarrow\lambda_n
 \qquad(\varepsilon\downarrow0).                            \tag{4}
\]

Para cada \(\varepsilon>0\), la serie de (3) converge absolutamente.
Ningún canal se estimará por separado al pasar al borde.

---

## 2. Fórmula de Fourier de la logística

Sea \(\ell(y)=(1+e^y)^{-1}\).

**Lema 2.1.** Para todo \(y\in\mathbb R\),

\[
 \boxed{\ell(y)={1\over2}-\int_0^\infty
 {\sin(sy)\over\sinh(\pi s)}\,ds.}                         \tag{5}
\]

La integral es absolutamente convergente para cada \(y\) fijo.

**Demostración.** Cerca de cero,
\(\sin(sy)/\sinh(\pi s)\to y/\pi\); en infinito hay decaimiento
exponencial. Además,

\[
 {1\over\sinh(\pi s)}=2\sum_{j\ge0}e^{-(2j+1)\pi s}
 \qquad(s>0).
\]

La integración término a término y el producto de Weierstrass de
\(\cosh(y/2)\) dan

\[
 \int_0^\infty{\sin(sy)\over\sinh(\pi s)}\,ds
 =2y\sum_{j\ge0}{1\over(2j+1)^2\pi^2+y^2}
 ={1\over2}\tanh{y\over2}.
\]

Como \(\ell(y)=(1-\tanh(y/2))/2\), sigue (5). \(\square\)

Defina

\[
 \mathcal C_{t,X}(s):={1\over H_X}\sum_{n\le X}{e^{istx_n}\over n}.
                                                                    \tag{6}
\]

La suma exterior es finita, de modo que (5) implica exactamente

\[
 \boxed{\mathfrak F_t(X)={1\over2}-\int_0^\infty
 {\operatorname {Im}\mathcal C_{t,X}(s)\over\sinh(\pi s)}\,ds.}
                                                                    \tag{7}
\]

Ésta no es una linealización: \(\lambda_n\) permanece dentro de la fase.

---

## 3. Producto prima--Laguerre unitario exacto

Antes de tomar el borde, ponga

\[
\boxed{
\begin{aligned}
 \mathcal C_{t,X,\varepsilon}(s)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 &e^{ist(A_n+b_n+p_n(\varepsilon))}\\[-2mm]
 &\times\prod_{m\ge2}
 \exp\!\left(-{ist\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m)\right).
\end{aligned}}                                               \tag{8}
\]

Cada factor del producto tiene módulo uno. Para \(\varepsilon>0\), su
logaritmo es absolutamente sumable por `104_61`, (20b). Por (3),

\[
 \mathcal C_{t,X,\varepsilon}(s)
 ={1\over H_X}\sum_{n\le X}{e^{ist(\lambda_{n,\varepsilon}+b_n)}\over n},
 \qquad |\mathcal C_{t,X,\varepsilon}(s)|\le1.              \tag{9}
\]

Para \(X\) fijo, (4) da convergencia uniforme en compactos de \(s\). También
permite pasar al límite dentro de (7): para \(\varepsilon\) pequeño los
finitos \(\lambda_{n,\varepsilon}+b_n\), \(n\le X\), están uniformemente
acotados, lo que domina el integrando cerca de cero; en infinito se usa
\(|\mathcal C|\le1\) y el decaimiento de \(1/\sinh(\pi s)\). Así,

\[
 \boxed{\mathfrak F_t(X)={1\over2}
 -\lim_{\varepsilon\downarrow0}\int_0^\infty
 {\operatorname {Im}\mathcal C_{t,X,\varepsilon}(s)
 \over\sinh(\pi s)}\,ds.}                                  \tag{10}
\]

La cola de frecuencias es uniformemente explícita:

\[
 \int_S^\infty{ds\over\sinh(\pi s)}
 ={1\over\pi}\log\coth{\pi S\over2}.                        \tag{11}
\]

Por tanto (8) resuelve un problema real de condicionamiento de (20c): no
aparecen productos gigantes que luego deban cancelarse. No resuelve la
región \(s\downarrow0\).

Para separar el baseline, sea

\[
 \mathcal D_{t,X}(s)={1\over H_X}\sum_{n\le X}{e^{istb_n}\over n}
 \left(e^{ist\lambda_n}-1\right).                           \tag{12}
\]

Como

\[
 {1\over H_X}\sum_{n\le X}{1\over n(1+(n+1)^t)}\longrightarrow0,
\]

el Teorema 3.2 de `104_61` y (7) dan la equivalencia exacta

\[
 \boxed{\mathrm {RH}\iff
 \int_0^\infty{\operatorname {Im}\mathcal D_{t,X}(s)
 \over\sinh(\pi s)}\,ds\longrightarrow0.}                  \tag{13}
\]

La ecuación (13) es una equivalencia, no la estimación buscada.

---

## 4. Teorema cuantitativo de microfrecuencia

**Teorema 4.1.** Sean \(S\ge1\), \(Y\ge\pi S\), y

\[
 J(Y,S):=\int_0^{S/Y}{\sin(sY)\over\sinh(\pi s)}\,ds.
\]

Entonces

\[
 \boxed{\left|J(Y,S)-{1\over2}\right|
 \le {2\over\pi S}+{\pi S^2\over2Y^2}.}                    \tag{14}
\]

Además, para todo \(\delta>0\),

\[
 \boxed{\left|\int_\delta^\infty
 {\sin(sY)\over\sinh(\pi s)}\,ds\right|
 \le {2\over Y\sinh(\pi\delta)}.}                          \tag{15}
\]

**Demostración.** En (14), haga \(u=sY\). Para \(0\le u\le S\), ponga
\(z=\pi u/Y\le1\). La serie de \(\sinh z\) da

\[
 z\le\sinh z\le z(1+z^2),
\]

y por ello

\[
 0\le {1\over\pi u}-{1\over Y\sinh(\pi u/Y)}
 \le {\pi u\over Y^2}.                                     \tag{16}
\]

Por consiguiente,

\[
 \left|J(Y,S)-\int_0^S{\sin u\over\pi u}\,du\right|
 \le{\pi S^2\over2Y^2}.
\]

Una integración por partes da
\(\left|\int_S^\infty\sin u/u\,du\right|\le2/S\), y
\(\int_0^\infty\sin u/u\,du=\pi/2\). Esto prueba (14).

Para (15), aplique integración por partes a
\(f(s)=1/\sinh(\pi s)\). La función es positiva, decreciente y tiende a
cero; el término de borde y la variación total de \(f\) cuestan cada uno a
lo sumo \(f(\delta)/Y\). \(\square\)

Si \(x=-Y\), entonces

\[
 \ell(-Y)={1\over2}+\int_0^\infty
 {\sin(sY)\over\sinh(\pi s)}\,ds.
\]

La ecuación (14) dice que, primero tomando \(Y\to\infty\) y luego
\(S\to\infty\), toda la saturación \(\ell(-Y)\to1\) ya está codificada en
\(0<s<S/Y\). La frecuencia relevante es inversa a la profundidad, no al
grado.

### 4.1 Falsificador racional

Para el cuarteto de `104_17`, \(w=2i\),

\[
 Q_n=4-2\operatorname {Re}(w^n+w^{-n}),
\]

y, si \(n\equiv0\pmod4\),

\[
 Q_n=4-2(2^n+2^{-n}).                                      \tag{17}
\]

Con \(Y_n=-(Q_n+\log(n+1))\), la cota
\(\log(n+1)\le n\) da, para \(n\equiv0\pmod4\), \(n\ge4\),

\[
 \boxed{Y_n\ge2^n.}                                        \tag{18}
\]

Por (15), para cada \(B>0\),

\[
 \left|\int_{n^{-B}}^\infty
 {\sin(sY_n)\over\sinh(\pi s)}\,ds\right|
 \le {2n^B\over\pi2^n}\longrightarrow0.                   \tag{19}
\]

Sin embargo, \(\ell(Q_n+b_n)\to1\) en esa clase, de densidad natural y
logarítmica \(1/4\). Por tanto

\[
 \boxed{\text{una resolución }s\ge n^{-B}\text{ pierde el detector Fermi
 en un falsificador off-line exacto}.}                      \tag{20}
\]

Esto no prohíbe estimar la integral completa. Sí prohíbe afirmar que la
unitariedad de (8), junto con control lejos de cero, cierra (13): la parte
omitida contiene exactamente la excursión exponencial.

---

## 5. Dos representaciones positivas que tampoco cierran

### 5.1 No existe mezcla de Laplace positiva de la logística

No hay una medida positiva finita \(\mu\) sobre \([0,\infty)\) tal que

\[
 \ell(x)=\int_0^\infty e^{-sx}\,d\mu(s)
 \qquad(x\in\mathbb R).                                    \tag{21}
\]

Si \(\mu([a,\infty))>0\) para algún \(a>0\), el lado derecho crece al menos
como \(e^{a|x|}\mu([a,\infty))\) cuando \(x\to-\infty\), mientras
\(\ell(x)\to1\). Luego \(\mu\) estaría soportada en \(0\), lo cual
produciría una constante. La mayorización \(\ell(x)\le e^{-x}\) sí existe,
pero devuelve exactamente la partición no acotada \(\mathcal Z_t\) y su
control coeficiente a coeficiente.

### 5.2 La forma variacional exige selectores de grado arbitrarios

Sea

\[
 h(q)=-q\log q-(1-q)\log(1-q),\qquad0\le q\le1.
\]

La identidad de Fenchel

\[
 \log(1+e^{-y})=\sup_{0\le q\le1}\{h(q)-qy\}                \tag{22}
\]

corresponde al observable distinto

\[
 \mathfrak V_t(X):={1\over H_X}\sum_{n\le X}{1\over n}
 \log(1+e^{-tx_n}).                                        \tag{22a}
\]

Se tiene \(\ell(y)\le\log(1+e^{-y})\). Bajo RH, el numerador de
\(\mathfrak V_t\) está acotado por
\(\sum_n n^{-1}(n+1)^{-t}<\infty\). Si RH es falsa, una excursión
\(\lambda_n\le-cR^n\) hace que un solo sumando crezca como \(R^n/n\).
Por tanto \(\mathfrak V_t(X)\to0\) también equivale a RH, pero es un target
cuantitativamente más fuerte: vuelve a amplificar picos individuales y no
conserva la relajación de densidad de Fermi.

La fórmula (22) convierte exactamente el numerador de (22a) en

\[
\begin{aligned}
 \sup_{\boldsymbol q\in[0,1]^X}\lim_{\varepsilon\downarrow0}
 \Bigg\{&
 \sum_{n\le X}{h(q_n)\over n}
 -t\sum_{n\le X}{q_n(A_n+b_n+p_n(\varepsilon))\over n}\\
 &+t\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 K_{\boldsymbol q,X}(\log m)\Bigg\},                       \tag{23}\\
 K_{\boldsymbol q,X}(u)&:=
 \sum_{n\le X}{q_n\over n}L_{n-1}^{(1)}(u).
\end{aligned}
\]

La igualdad es exacta para \(\mathfrak V_t\), no para \(\mathfrak F_t\):
la suma exterior es finita y el supremo separa en cada \(n\). Probar que
(23) es \(o(H_X)\) probaría RH mediante el criterio más fuerte (22a), pero
la fórmula no reduce los selectores a una familia radial positiva.

En efecto, si \(0<z<1\) y \(y=z/(1-z)\), Laguerre da

\[
 \boxed{\sum_{n\ge1}{z^n\over n}L_{n-1}^{(1)}(u)
 ={1-e^{-uy}\over u},}                                     \tag{24}
\]

con el valor \(y\) en \(u=0\). También

\[
\begin{aligned}
 \sum_{n\ge1}{z^n\over n}p_n(\varepsilon)
 &=\log\!\left(1+{y\over\varepsilon}\right),\\
 \sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 {1-m^{-y}\over\log m}
 &=\log\zeta(1+\varepsilon)-\log\zeta(1+\varepsilon+y).
\end{aligned}                                               \tag{25}
\]

La primera serie de (25) converge inicialmente para
\[
 |z|<\min\!\left(1,{\varepsilon\over|1-\varepsilon|}\right)
\]
(con radio \(1\) si \(\varepsilon=1\)); su miembro derecho da la
continuación real sobre \(0<z<1\). Esta distinción es obligatoria cuando
\(\varepsilon\downarrow0\): no se intercambia ese límite con la serie
infinita. Los selectores geométricos tienen, dentro de su dominio seguro,
una forma cerrada. Pero para el cuarteto
(17), `104_17` prueba

\[
 \sum_{n\ge1}Q_nz^n>0\qquad(0<z<1/2),                      \tag{26}
\]

mientras su partición Fermi tiende a \(1/4\). Toda mezcla **positiva** de
los datos radiales seguros de (26) conserva el signo incorrecto y no
controla el supremo de (23), cuyo selector óptimo se concentra en una clase
periódica. La generatriz (24) es exacta; restringir a ella los selectores no
lo es.

---

## 6. Coordenada diagonal por tasa exponencial

En (5), haga para cada sumando

\[
 s=e^{-nv},\qquad-\infty<v<\infty.
\]

El jacobiano cancela el peso armónico y da

\[
 \boxed{\mathfrak F_t(X)={1\over2}-{1\over H_X}
 \int_{-\infty}^{\infty}\sum_{n\le X}
 {e^{-nv}\sin(t e^{-nv}x_n)\over\sinh(\pi e^{-nv})}\,dv.}  \tag{27}
\]

La integral es absolutamente convergente para cada \(X\): cuando
\(v\to-\infty\), el denominador domina doblemente; cuando
\(v\to\infty\), el seno aporta otro factor \(e^{-nv}\).

La versión aritmética regulada usa

\[
\boxed{
\begin{aligned}
 U_{n,\varepsilon}(v)
 :=&\ e^{it e^{-nv}(A_n+b_n+p_n(\varepsilon))}\\
 &\times\prod_{m\ge2}\exp\!\left(
 -{it e^{-nv}\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m)\right),
 \qquad |U_{n,\varepsilon}(v)|=1.
\end{aligned}}                                               \tag{28}
\]

En (27), \(\sin(t e^{-nv}x_n)\) es el límite de
\(\operatorname {Im}U_{n,\varepsilon}(v)\). Polo, bloque arquimediano,
primos y potencias primas permanecen acoplados hasta después de aplicar la
no linealidad.

Si \(Y_n\asymp e^{an}\), su transición ya no está en una frecuencia
exponencialmente pequeña:

\[
 e^{-nv}Y_n\asymp1\iff v\asymp a.                           \tag{29}
\]

Para \(w=2i\), el borde es \(v=\log2\).

La primera variación en la región segura se alinea con

\[
\begin{aligned}
 \sum_{n\ge1}z^nL_{n-1}^{(1)}(u)
 &={z\over(1-z)^2}e^{-uz/(1-z)},\\
 \sum_{n\ge1}{z^n\over n}L_{n-1}^{(1)}(u)
 &={1-e^{-uz/(1-z)}\over u},
 \qquad z=e^{-v}.                                           \tag{30}
\end{aligned}
\]

Los órdenes superiores de \(\sin(tz^n x_n)\) retienen productos entre
torres primas y no se reducen a cumulantes aditivos; (27)--(28) quedan fuera
del clasificador de `104_53`.

### 6.1 La franja no lineal tiene ancho explícito

Usemos el hecho certificado de que cada cero no trivial satisface
\(|\operatorname {Im}\rho|>14\). Si
\(z_\rho=1-1/\rho\), \(\rho=\beta+i\gamma\), entonces

\[
 |z_\rho|^2
 =1+{1-2\beta\over\beta^2+\gamma^2}
 \ge1-{1\over\gamma^2}>{195\over196}.                       \tag{31}
\]

Ponga

\[
 r_0=\sqrt{195\over196},\qquad
 v_0=-\log r_0={1\over2}\log{196\over195}<0.00257.           \tag{32}
\]

La generatriz de Li

\[
 \log\xi\!\left({1\over1-z}\right)-\log\xi(1)
 =\sum_{n\ge1}{\lambda_n\over n}z^n                         \tag{33}
\]

es holomorfa en \(|z|<r_0\). Por Cauchy, para todo \(r<r_0\)
existe \(M_r<\infty\) tal que

\[
 |\lambda_n|\le nM_r r^{-n}.                                \tag{34}
\]

Fije \(\eta>0\), tome \(r=r_0e^{-\eta/2}\), y suponga
\(v\ge v_0+\eta\). Entonces

\[
 e^{-nv}|\lambda_n|\le nM_r e^{-\eta n/2}.                  \tag{35}
\]

La misma conclusión trivial vale para \(e^{-nv}b_n\). En cada semirrecta
\(v\ge v_0+\eta\), la expansión completa del seno de (27) converge de
manera uniforme y absoluta después de sumar en \(n\). La transición de un modo
exponencial off-line queda confinada a

\[
 0\le v\le v_0.                                             \tag{36}
\]

Esto no controla la integral total: los límites \(v\downarrow0\) y
\(\eta\downarrow0\) no son uniformes. Sí transforma
\(s\asymp e^{-an}\) en una franja de ancho menor que \(0.00257\) sin
suponer RH. Una verificación de ceros más alta estrecharía la cifra, pero no
eliminaría el borde \(v=0\), y no se cuenta como cierre por rango finito.

### 6.2 La generatriz diagonal solo ve el producto geométrico

La limitación anterior puede hacerse exacta. Para
\(z=e^{-v}\), \(\tau=z/(1-z)\), y

\[
 Q_{n,\varepsilon}:=
 \sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m),
\]

las ecuaciones (24)--(25) dan, inicialmente dentro del radio común de
convergencia,

\[
\begin{aligned}
 \sum_{n\ge1}{z^n\over n}Q_{n,\varepsilon}
 &=\log\zeta(1+\varepsilon)
   -\log\zeta(1+\varepsilon+\tau),\\
 \sum_{n\ge1}{z^n\over n}
 \{p_n(\varepsilon)-Q_{n,\varepsilon}\}
 &=\log\!\left(1+{\tau\over\varepsilon}\right)
   -\log\zeta(1+\varepsilon)
   +\log\zeta(1+\varepsilon+\tau).
\end{aligned}                                               \tag{36a}
\]

Llame \(\mathscr G_\varepsilon^{\mathrm{cont}}(z)\) a la continuación
real dada por el miembro derecho de la segunda línea. En consecuencia,

\[
 \lim_{\varepsilon\downarrow0}
 \mathscr G_\varepsilon^{\mathrm{cont}}(z)
 =\log\{\tau\zeta(1+\tau)\}.                                \tag{36b}
\]

Para \(z>0\) fijo, el radio de la serie polar se encoge como
\(\varepsilon/(1-\varepsilon)\); por tanto (36b) **no** es un intercambio
del límite con la serie escrita en (36a). Es una identidad de continuación.
En el dominio donde la serie de Li sí converge, la identidad lineal calcula

\[
 \exp\!\left(iu\sum_{n\ge1}{z^n\lambda_n\over n}\right)
 =\prod_{n\ge1}\exp\!\left({iu z^n\lambda_n\over n}\right), \tag{36c}
\]

un **producto geométrico** de fases. La ecuación (27) necesita, en cambio,
la **media aritmética**

\[
 \sum_{n\le X}
 {z^n\sin(tz^n x_n)\over\sinh(\pi z^n)}.                   \tag{36d}
\]

No hay paso algebraico de (36c) a (36d).

El cuarteto muestra que tampoco hay truncación perturbativa en la frontera.
Si un modo dominante tiene tasa \(R>1\), entonces:

* para \(v>\log R\), \(z^n\lambda_n\to0\) y la expansión es segura;
* para \(v=\log R\), cada potencia de Hadamard
  \((z^n\lambda_n)^k\) es de orden uno; una truncación a cualquier orden
  fijo deja un resto que no es \(o(1)\) por el mero límite \(n\to\infty\);
* para \(v<\log R\), la serie radial de \(\lambda_n\) no converge.
  Evaluar allí (36b) por continuación analítica no es sumar la serie.

En particular, permutar en esa región la suma infinita en \(n\) con
\(\varepsilon\downarrow0\) afirmaría precisamente la ausencia del polo
interior \(z_\rho\), es decir, introduciría el dato RH-strength que se quería
probar. La coordenada diagonal localiza el muro, pero no lo atraviesa.

La estimación que habría que probar sigue siendo

\[
 \boxed{\int_{-\infty}^{\infty}\sum_{n\le X}
 {e^{-nv}\operatorname {Im}U_{n,0}(v)
  \over\sinh(\pi e^{-nv})}\,dv
 ={1\over2}H_X+o(H_X).}                                    \tag{37}
\]

Aquí \(U_{n,0}\) significa el límite **emparejado** de (28), nunca los
factores por separado. La ecuación (37) implica
\(\mathfrak F_t(X)\to0\), luego RH. No está probada, y (36a)--(36d) muestran
que la generatriz lineal no la aproxima en la escala crítica. No se abre un
sucesor desde esta rama: controlar todos los poderes de Hadamard en
\(zR=1\) solo renombra el hueco.

---

## 7. Veredicto

**Probado.** Las fórmulas unitarias (8)--(10), la localización cuantitativa
(14)--(15), el no-go de resolución polinómica (17)--(20), el gate de mezcla
positiva (21)--(26), la representación diagonal (27)--(30), la franja
segura (31)--(36) y el colapso producto--media (36a)--(36d).

**Ganancia.** La explosión de la partición exponencial no es necesaria:
existe un lift prima--Laguerre acotado, unitario y truncable en frecuencia
alta. La microfrecuencia y la variable diagonal identifican exactamente
dónde vive la obstrucción.

**No probado.** La estimación (37), el límite de Fermi, A1 o RH. La capa de
microfrecuencia demuestra por qué la sola unitariedad no basta; la auditoría
diagonal impide presentar (27) como un frente nuevo ya simplificado.

---

## 8. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 unitary_fermi_microfrequency_check.py
```

El checker usa `Fraction` para verificar (17)--(18), la densidad \(1/4\), y
las generatrices de Laguerre y del polo coeficiente a coeficiente. La
identidad integral y sus cotas se prueban en el texto; el muestreo de Fourier
que imprime la herramienta es solo diagnóstico.
