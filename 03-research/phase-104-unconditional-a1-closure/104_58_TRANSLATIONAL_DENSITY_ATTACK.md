# 104_58 — Ataque traslacional y criterio de densidad para el margen cuarto

**Estado.** Este documento explota el objetivo relajado de `104_56A`,

\[
 D_n:=4\lambda_n-A_n>0.                              \tag{1}
\]

Se obtiene un resultado útil pero no un cierre de (1): si RH es falsa,
entonces \(D_n<0\) en un conjunto de enteros de densidad inferior positiva.
Por tanto basta probar (1) fuera de un conjunto de densidad cero. La misma
obstrucción sobrevive a toda ventana traslacional de longitud fija.

También se responde negativamente una pregunta distinta: la cota de fase
\(|\mathcal B_{n,a}|\le3n\) de `104_41`, válida para \(a\ge4\), no puede
transportarse a \(a=1\), ni siquiera «en densidad» o después de promediar en
ventanas fijas, sin controlar los residuos cruzados. Un cuarteto racional lo
prueba exactamente.

Nada de lo siguiente prueba que los \(D_n\) reales sean positivos en
densidad uno. Por tanto este documento no prueba A1 ni RH.

## 1. No duplicación con `104_17`

`104_17` estudia las sumas iniciales
\(\sum_{n\le N}Q_n\), sus medias triangulares y la positividad Abel radial.
Aquí se estudian objetos diferentes:

1. ventanas **trasladadas** \(\sum_{h<L}D_{N+h}\);
2. la densidad natural del conjunto de signos malos;
3. el conjunto finito de singularidades dominantes si RH falla;
4. el cambio exacto de una ventana al mover la homotopía \(a\ge4\to1\).

No se intenta recuperar un coeficiente desde positividad Abel, que ya está
descartado por `104_17`.

## 2. Generatriz exacta de los bloques

Sea

\[
 s(z)={1\over1-z},\qquad
 G(s)=s\pi^{-s/2}\Gamma(s/2),\qquad
 Y_4(s)={\xi(s)^4\over G(s)}.
\]

La identidad local de Li da

\[
 \mathcal H(z):=\log{Y_4(s(z))\over Y_4(1)}
 =\sum_{n\ge1}{D_n\over n}z^n.                    \tag{2}
\]

Por tanto la generatriz ordinaria es

\[
 \boxed{
 \mathcal D(z):=z\mathcal H'(z)=\sum_{n\ge1}D_nz^n.} \tag{3}
\]

Para \(L\ge1\), defínase la ventana que termina en \(N\)

\[
 S_{N,L}:=\sum_{h=0}^{L-1}D_{N-h},
 \qquad D_j:=0\quad(j\le0).
\]

Entonces

\[
 \boxed{
 \sum_{N\ge1}S_{N,L}z^N
 ={1-z^L\over1-z}\,\mathcal D(z).}                \tag{4}
\]

Equivalentemente, para la ventana que empieza en \(N\),

\[
 U_{N,L}:=\sum_{h=0}^{L-1}D_{N+h}
 =[z^{N+L-1}],{1-z^L\over1-z}\mathcal D(z).       \tag{5}
\]

Así, promediar sobre una longitud fija solo multiplica cada singularidad
por el polinomio

\[
 A_L(w):=1+w+\cdots+w^{L-1}={1-w^L\over1-w}.       \tag{6}
\]

Si \(|w|>1\), entonces \(A_L(w)\ne0\). Por consiguiente ninguna ventana
fija anula un modo off-line exterior.

## 3. Lema de densidad para un polinomio trigonométrico

**Lema 3.1.** Sean \(0<\theta_j<\pi\), distintos módulo el signo, y
\(c_j>0\). Póngase

\[
 P_n=\sum_{j=1}^Jc_j\cos(n\theta_j),\qquad
 M=\sum_jc_j,\qquad
 \sigma^2={1\over2}\sum_jc_j^2.                  \tag{7}
\]

Entonces, con \(\varepsilon=\sigma^2/(4M)\),

\[
 \boxed{
 \underline{\operatorname {dens}}
 \{n:P_n>\varepsilon\}\ge {\sigma^2\over4M^2}>0.} \tag{8}
\]

**Demostración.** Las identidades elementales de Cesàro

\[
 {1\over N}\sum_{n\le N}e^{in\alpha}\longrightarrow0
 \qquad(\alpha\notin2\pi\mathbb Z)
\]

dan

\[
 {1\over N}\sum_{n\le N}P_n\to0,\qquad
 {1\over N}\sum_{n\le N}P_n^2\to\sigma^2.        \tag{9}
\]

Se agruparon previamente las frecuencias que representan el mismo coseno,
por lo que no quedan términos cruzados constantes. Como
\(|P_n|\le M\), se tiene \(P_n^2\le M|P_n|\). Escribiendo
\(P_n=P_n^+-P_n^-\), (9) implica

\[
 \liminf_{N\to\infty}{1\over N}\sum_{n\le N}P_n^+
 \ge {\sigma^2\over2M}.                           \tag{10}
\]

Finalmente,

\[
 P_n^+\le\varepsilon+M\mathbf1_{\{P_n>\varepsilon\}}.
\]

Se promedia y se usa (10), obteniendo (8). \(\square\)

La misma prueba vale para un polinomio real no nulo
\(\operatorname {Re}\sum_jd_je^{in\theta_j}\), después de agrupar
frecuencias. Lo único que cambia es la constante positiva.

## 4. Teorema dominante: una violación de RH produce densidad mala positiva

**Teorema 4.1.** Si RH es falsa, existen \(r>1\), \(1<r_1<r\), un
polinomio trigonométrico real no nulo \(P_n\), y una constante \(C\), tales
que

\[
 \boxed{
 D_n=-8r^nP_n+O(r_1^n).}                           \tag{11}
\]

En particular,

\[
 \boxed{
 \underline{\operatorname {dens}}\{n:D_n<0\}>0.} \tag{12}
\]

**Demostración.** Los ceros a la derecha de la línea crítica se transforman
en

\[
 z_\rho=1-{1\over\rho},\qquad |z_\rho|<1.          \tag{13}
\]

Si existe alguno, el número

\[
 q:=\min_{\Re\rho>1/2}|z_\rho|<1                  \tag{14}
\]

se alcanza y el conjunto \(\mathcal Z_0\) de ceros que alcanzan el mínimo
es finito: en todo disco compacto de la variable \(z\) hay solo finitos
ceros, y \(|z_\rho|\to1\) cuando \(|\Im\rho|\to\infty\).

Elija \(q<q_1<1\) sin otras singularidades transformadas en
\(|z|\le q_1\). Al retirar de \(Y_4(s(z))\) los factores de los ceros de
\(\mathcal Z_0\), queda una función holomorfa y no nula en ese disco, con
logaritmo holomorfo. De (2), la singularidad logarítmica de un cero de
multiplicidad \(m_\rho\) da

\[
 D_n=-4\sum_{\rho\in\mathcal Z_0}m_\rho z_\rho^{-n}
     +O(r_1^n),                                    \tag{15}
\]

para algún \(1<r_1<q^{-1}\); el factor polinómico de una cota de Cauchy se
absorbe agrandando \(r_1\). Agrupando conjugados y escribiendo
\(z_\rho=q e^{i\theta_\rho}\),

\[
 D_n=-8q^{-n}\sum_{\substack{\rho\in\mathcal Z_0\\Im\rho>0}}
 m_\rho\cos(n\theta_\rho)+O(r_1^n).               \tag{16}
\]

No aparece una frecuencia \(0\) o \(\pi\), pues los ceros no triviales no
son reales. Tras agrupar cosenos iguales, el Lema 3.1 da un conjunto de
densidad inferior positiva donde el polinomio de (16) supera una constante
positiva. Sobre ese conjunto el término principal domina al error para
todo \(n\) suficientemente grande, y \(D_n<0\). \(\square\)

**Corolario 4.2 (criterio de densidad uno).** Si

\[
 D_n>0
 \quad\hbox{para todo }n\notin\mathcal E,\qquad
 \operatorname {dens}(\mathcal E)=0,               \tag{17}
\]

entonces RH es cierta.

No se obtiene de esta prueba una constante universal \(\delta_0>0\) tal
que baste \(\overline{\operatorname {dens}}(\mathcal E)<\delta_0\). La cota
de (8) depende del número y de las multiplicidades de los ceros dominantes;
sin una cota uniforme para ese dato puede ser arbitrariamente pequeña.
La relajación robusta es «excepciones de densidad cero».

## 5. Las ventanas fijas tampoco esconden los residuos dominantes

**Teorema 5.1.** Bajo la negación de RH, para cada longitud fija \(L\ge1\),

\[
 \boxed{
 \underline{\operatorname {dens}}
 \left\{N:\sum_{h=0}^{L-1}D_{N+h}<0\right\}>0.}    \tag{18}
\]

**Demostración.** Se suma (16) en \(n=N,\ldots,N+L-1\). Si
\(w_j=q^{-1}e^{-i\theta_j}\), el término dominante se convierte en

\[
 -8q^{-N}\operatorname {Re}
 \sum_jm_j e^{-iN\theta_j}A_L(w_j).                \tag{19}
\]

Cada \(A_L(w_j)\ne0\) por \(|w_j|>1\). Después de agrupar frecuencias,
(19) es un polinomio trigonométrico real no nulo. Su parte positiva supera
una constante en un conjunto de densidad inferior positiva por la prueba
del Lema 3.1. El error sigue siendo \(O(r_1^N)\), pues \(L\) es fijo, y
queda dominado por \(q^{-N}\). \(\square\)

Por tanto un teorema que probara positividad de una sola longitud fija de
ventanas fuera de un conjunto de densidad cero también probaría RH. Pero
la ventana no reduce el residuo: solo rota y reescala su fase.

## 6. Falsificador racional de toda ventana fija

Tómese el cuarteto de `104_17`

\[
 \rho={1+2i\over5},\qquad w=1-{1\over\rho}=2i.
\]

Su contribución al coeficiente de Li es

\[
 Q_n=4-2\operatorname {Re}(w^n+w^{-n}),            \tag{20}
\]

y al margen (1) es \(D_n^{\mathcal O}=4Q_n\). Por tanto

\[
 \boxed{
 \sum_{h=0}^{L-1}D_{N+h}^{\mathcal O}
 =16L-8\operatorname {Re}\left{
 w^NA_L(w)+w^{-N}A_L(w^{-1})\right}.}             \tag{21}
\]

Escriba \(A_L(2i)=a_L+ib_L\). Es un entero gaussiano no nulo, porque
\((2i)^L\ne1\). Alguna de las cuatro cantidades
\(\operatorname {Re}(i^jA_L(2i))\) es estrictamente positiva. En la clase
\(N\equiv j\pmod4\) correspondiente, el término dominante de (21) es

\[
 -8\,2^N\operatorname {Re}(i^jA_L(2i)),
\]

mientras el término recíproco tiende a cero. Así (21) es negativo para
todo \(N\) suficientemente grande de esa clase, que tiene densidad
exactamente \(1/4\). Esto vale para **cada** \(L\) fijo.

## 7. La cota de fase no se transporta en densidad

Sea \(F(s)=(s-1)\zeta(s)\) y multiplíquese formalmente por
\(Q_\rho(s)^M\), donde \(Q_\rho\) es el polinomio del cuarteto anterior.
Para

\[
 z_{\eta,a}:=1-{a\over\eta},
\]

la fórmula de coeficientes (8) de `104_41` da el cambio exacto

\[
 \boxed{
 \Delta\mathcal B_{n,a}
 =M\sum_{\eta\in\mathcal O(\rho)}
       \left(z_{\eta,a}^{-n}-1\right).}            \tag{22}
\]

Para \(a\ge4\), la identidad

\[
 |z_{\eta,a}|^2-1={a(a-2\Re\eta)\over|\eta|^2}>0  \tag{23}
\]

muestra que (22) es acotada en \(n\) y tiende a \(-4M\). En el extremo
\(a=1\), la simetría recíproca da

\[
 \Delta\mathcal B_{n,1}=-M Q_n,\qquad
 \Delta D_n=4M Q_n.                               \tag{24}
\]

Para \(n\equiv0\pmod4\), \(n\ge4\),

\[
 Q_n=4-2(2^n+2^{-n})<0,                            \tag{25}
\]

de modo que el cambio en \(D_n\) es exponencialmente negativo sobre un
conjunto de densidad \(1/4\), aunque en \(a\ge4\) el cambio de (22) sea
solo acotado. Las ventanas fijas conservan la misma obstrucción por (21).

Para \(M=1\), el factor de cuarteto por sí solo satisface incluso la misma
cota numérica de salida que (19) de `104_41` en todos los grados objetivo.
En \(a=4\), los cuatro módulos cuadrados de \(z_{\eta,4}\) son
\(73,73,13,13\); por (23) solo aumentan al crecer \(a\). Por tanto, para
\(a\ge4\) y \(n\ge2\),

\[
 |\Delta\mathcal B_{n,a}|
 \le4+2\,73^{-n/2}+2\,13^{-n/2}
 \le4+{2\over73}+{2\over13}<6\le3n.               \tag{25a}
\]

Así, ni siquiera conservar la desigualdad escalar exacta
\(|\mathcal B_{n,a}|\le3n\) en el extremo Euler distingue el falsificador
en los grados \(n\ge150\).

Además \(Q_\rho(1/2+it)>0\), así que la fase crítica permanece idéntica,
como prueba `104_41`. Por tanto:

\[
 \boxed{
 \text{fase en el semiplano Euler + promedios traslacionales fijos}
 \not\Longrightarrow
 \text{control en densidad en }a=1}               \tag{26}
\]

sin una estimación separada de los residuos cruzados.

Este falsificador no tiene los pesos Euler exactos \(\Lambda(m)\). Por eso
(26) descarta mecanismos basados solo en fase, homotopía y promediado; no
descarta una desigualdad nueva específica para los pesos reales de zeta.

## 8. Balance

**Probado:**

- generatriz exacta (3)--(5) de ventanas traslacionales;
- criterio de densidad uno, Corolario 4.2;
- persistencia de la obstrucción en toda longitud fija, Teorema 5.1;
- falsificador racional de densidad \(1/4\);
- imposibilidad de transportar \(|\mathcal B_{n,a}|\le3n\) en densidad o
  en ventanas fijas sin controlar residuos.

**No probado:**

- que \(D_n>0\) para una densidad uno de índices reales de zeta;
- una cota de residuos usando los pesos exactos \(\Lambda(m)\);
- A1 o RH.

El avance lógico sí es real: el cuantificador «todo \(n\ge150\)» puede
reemplazarse por «todo \(n\) salvo densidad cero». El obstáculo que queda no
es recuperar cada coeficiente desde un promedio, sino demostrar una cota
media que excluya una **densidad positiva** de fallos.

## 9. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 translational_density_attack_check.py
```

El checker usa únicamente racionales y racionales gaussianos. Verifica
(20)--(25) y las identidades de ventanas en una familia finita de valores;
la densidad para todo \(L\) se prueba algebraicamente arriba, no por
muestreo.
