# 104_55 — Palm unitario de tres marcas y gate de orientación cúbica

**Objetivo.** Atacar, antes de tomar el logaritmo, el margen

\[
 B_n\le\kappa A_n,\qquad
 \kappa={1501\over2002},\qquad n\ge150,                  \tag{1}
\]

mediante tres marcas del selector exacto
\(\Lambda(p^k)=\log p\). Se conservan todos los primos y potencias, el
comparador polar y el bloque Gamma arquimediano exacto \(A_n\).

El Palm de tercer orden existe y retiene tuplas de torres distintas:

\[
 m_3(s)\,\mathbb E_s^{[3]}
   \{f(Z_1)g(Z_2)h(Z_3)\}
 =\mathbb E_s\{J_f(N)J_g(N)J_h(N)\}.                     \tag{2}
\]

Sin embargo, ninguna de las tres orientaciones canónicas aporta (1):

1. el tercer momento completado contiene una asimetría central sin signo;
2. el determinante alternante de tres marcas tiene esperanza cero, mientras
   su cuadrado es PSD para cualquier selector;
3. una polarización cúbica canónica que elimina exactamente la asimetría,

   \[
   \mathbb E[(Z^{(1)}-Z^{(2)})^2(Z^{(3)}-c)]
   =2\operatorname{Var}(D_f)\{M_s(f)-c\},                 \tag{3}
   \]

   recupera la orientación correcta, pero su signo es **equivalente** al
   signo del margen buscado.

La uniformidad dentro de una torre sí produce una identidad que el sistema
desplazado pierde: todas las potencias impares de
\(K-(a+1)/2\) promedian cero para \(K\) uniforme en
\(\{1,\ldots,a\}\). Pero después de mezclar torres, incluso el tercer
momento central del selector unitario real tiene ambos signos: es negativo
para \(N=6\) y positivo para \(N=18\). La tercera diferencia de Laguerre
también tiene ambos signos en cada grado \(n\ge5\).

El falsificador \(Z_c(s)=\zeta(s+c)\zeta(s-c)\) conserva (2), la identidad
algebraica (3) y toda positividad determinantal. Su selector local ya viola
la reflexión unitaria racionalmente en \(p=5,5^c=2,a=2\), pero esa
distinción no produce una cota orientada en ninguna de las formas globales
aquí auditadas.

Por tanto queda descartado el mecanismo estrecho

```text
Palm unitario de tres marcas
+ tercer momento / determinante 3x3 / tercera diferencia
+ positividad canónica
    => B_n <= (1501/2002) A_n.
```

No se descarta una desigualdad no lineal no canónica que correlacione la
reflexión local unitaria con el entero total y el test Laguerre. Este
documento no prueba (1), A1 ni RH.

## 0. Relación con los gates anteriores

`104_49` construye una marca uniforme dentro de cada exponente primo.
`104_50` eleva a dos marcas y demuestra que el cuadrado completado pierde
orientación. `104_52`--`104_53` prueban que los cumulantes aditivos eliminan
las interacciones entre torres en todo orden. Aquí no se vuelve a contar ese
teorema: se mantiene el **momento desconectado de orden tres antes del
logaritmo**, se calculan sus polarizaciones orientadas y se somete la
uniformidad local a un falsificador desplazado.

## 1. Palm exacto de tres marcas

Fijemos \(s=1+\varepsilon>1\),

\[
 \mathbb P_s(N=m)={m^{-s}\over\zeta(s)},\qquad
 X=\log N,\qquad m_r(s)=\mathbb E_sX^r.                 \tag{4}
\]

Para un test admisible, sea

\[
 J_f(N)=\sum_{d\mid N}\Lambda(d)f(\log d).               \tag{5}
\]

Sesgue la ley (4) por \(X^3\):

\[
 \mathbb P_s^{[3]}(N^{[3]}=m)
 ={(\log m)^3m^{-s}\over\zeta(s)m_3(s)}.                 \tag{6}
\]

Condicionado a \(N^{[3]}=m>1\), elija \(Z_1,Z_2,Z_3\)
independientes con

\[
 \mathbb P(Z_i=\log d\mid m)
 ={\Lambda(d)\over\log m}\mathbf1_{d\mid m}.            \tag{7}
\]

En \(m=1\) se usa un cementerio; el factor \((\log m)^3\) lo anula.
Como \(\sum_{d\mid m}\Lambda(d)=\log m\), (7) es una probabilidad. Al
cancelar los tres denominadores en la esperanza condicionada se obtiene
(2). Equivalentemente,

\[
 \boxed{
 \mathbb E_s[J_fJ_gJ_h]
 =\sum_{d,e,r\ge2}{\Lambda(d)\Lambda(e)\Lambda(r)
 \over\operatorname{lcm}(d,e,r)^s}
 f(\log d)g(\log e)h(\log r).}                            \tag{8}
\]

La fórmula (8) contiene tres torres distintas cuando \(d,e,r\) son
coprimos. Solo desaparecen al formar el cumulante conectado, como explica
`104_53`; aquí todavía no se ha tomado el logaritmo.

## 2. Comparador polar de tercer orden

Sea \(Y\sim\operatorname{Exp}(\varepsilon)\) y

\[
 C_f(Y)=\int_0^Y f(x)\,dx.                                \tag{9}
\]

Como \(\mathbb EY^3=6/\varepsilon^3\), sesgar por \(Y^3\) produce

\[
 Y^{[3]}\sim\Gamma(4,\varepsilon).                        \tag{10}
\]

Condicionado a \(Y^{[3]}=y\), elija \(U_1,U_2,U_3\)
independientes y uniformes en \([0,y]\). Entonces

\[
 \boxed{
 {6\over\varepsilon^3}\mathbb E^{[3]}
 \{f(U_1)g(U_2)h(U_3)\}
 =\mathbb E\{C_f(Y)C_g(Y)C_h(Y)\}.}                      \tag{11}
\]

El factor \(6\) es obligatorio. Por ejemplo, para
\(f(x)=x^{a-1},g(x)=x^{b-1},h(x)=x^{c-1}\), ambos miembros de (11) son

\[
 {(a+b+c)!\over abc\,\varepsilon^{a+b+c}}.               \tag{12}
\]

Éste es el Gamma probabilístico del size-bias polar. El factor Gamma
arquimediano de \(\xi\) no se sustituye por (10): permanece exactamente en
\(A_n=n[z^n]\log G((1-z)^{-1})\), con
\(G(s)=\tfrac12s\pi^{-s/2}\Gamma(s/2)\), dentro del presupuesto de (1).

## 3. Momento cúbico del defecto completado

Como en `104_50`, defina

\[
 U_f(X)=\int_0^X f(x)\,dx,\qquad
 D_f=J_f-U_f(X),                                          \tag{13}
\]

\[
 T_s(f)=\mathbb E_sU_f(X)-\mathbb E U_f(Y),\qquad
 Z_f=D_f+T_s(f),                                          \tag{14}
\]

y

\[
 M_s(f)=\mathbb E_sZ_f
 =\sum_{d\ge2}{\Lambda(d)\over d^s}f(\log d)
  -\int_0^\infty e^{-\varepsilon x}f(x)\,dx.             \tag{15}
\]

Ponga \(\widetilde D_f=D_f-\mathbb E_sD_f\). Para tres tests,

\[
\boxed{
\begin{aligned}
 \mathbb E_s[Z_fZ_gZ_h]
 ={}&\mathbb E_s[\widetilde D_f\widetilde D_g\widetilde D_h]\\
 &+M_s(f)\operatorname{Cov}_s(D_g,D_h)
  +M_s(g)\operatorname{Cov}_s(D_f,D_h)\\
 &+M_s(h)\operatorname{Cov}_s(D_f,D_g)
  +M_s(f)M_s(g)M_s(h).
\end{aligned}}                                             \tag{16}
\]

Para \(f=g=h\),

\[
 \mathbb E_sZ_f^3
 =\mu_{3,s}(D_f)+3M_s(f)\operatorname{Var}_s(D_f)+M_s(f)^3. \tag{17}
\]

El primer término de (17) no tiene signo. Desplazar por una constante
\(c\) solo reemplaza \(M_s(f)\) por \(M_s(f)-c\):

\[
 \boxed{
 \mathbb E_s(Z_f-c)^3
 =\mu_{3,s}(D_f)+3\{M_s(f)-c\}\operatorname{Var}_s(D_f)
   +\{M_s(f)-c\}^3.}                                     \tag{18}
\]

Así el tercer momento bruto no orienta el margen mientras la asimetría
central permanezca sin control.

## 4. La polarización orientada es exactamente el margen

Sean \(Z_f^{(1)},Z_f^{(2)},Z_f^{(3)}\) copias independientes de \(Z_f\).
La identidad de U-estadística

\[
 \boxed{
 \mathcal O_{s,c}(f):=
 \mathbb E_s[(Z_f^{(1)}-Z_f^{(2)})^2(Z_f^{(3)}-c)]
 =2\operatorname{Var}_s(D_f)\{M_s(f)-c\}}                \tag{19}
\]

elimina exactamente \(\mu_3(D_f)\) y conserva la orientación. Pero no la
determina: la orientación del miembro izquierdo es la de la media que se
quiere acotar.

Esto no es un accidente de la elección cuadrática. Sean
\(Z^{(1)},\ldots,Z^{(k+1)}\) copias independientes y sea
\(H=H(Z^{(1)},\ldots,Z^{(k)})\ge0\) integrable, sin dependencia de la última
copia. Entonces

\[
 \boxed{
 \mathbb E\{H(Z^{(1)},\ldots,Z^{(k)})(Z^{(k+1)}-c)\}
 =\mathbb EH\,\{\mathbb EZ-c\}.}                         \tag{19a}
\]

Si \(\mathbb EH>0\), toda orientación obtenida de esta manera es exactamente
equivalente al signo de la media. El corolario no cubre pesos que dependan
también de la copia orientada \(Z^{(k+1)}\); una correlación de ese tipo
permanece fuera de este no-go.

Para el test de A1,

\[
 f_{n,s}(x)=L_{n-1}^{(1)}(sx),\qquad
 sM_s(f_{n,s})=\mathcal B_{n,s}\longrightarrow B_n.      \tag{20}
\]

Tome el bloque Gamma exacto

\[
 c_{n,s}={\kappa A_n\over s}.                             \tag{21}
\]

Entonces

\[
 \boxed{
 {s\over2}\mathcal O_{s,c_{n,s}}(f_{n,s})
 =\operatorname{Var}_s(D_{f_{n,s}})
   \{\mathcal B_{n,s}-\kappa A_n\}.}                     \tag{22}
\]

Para \(n\ge2\), la varianza de (22) es estrictamente positiva. En efecto,
\(D_{f_{n,s}}(1)=0\). Si también fuera cero en todo primo \(p\), el
polinomio

\[
 H(x)=x f_{n,s}(x)-\int_0^x f_{n,s}(u)\,du                \tag{23}
\]

se anularía en los infinitos puntos \(\log p\), luego sería idénticamente
cero. Pero \(H'(x)=xf'_{n,s}(x)\), lo que forzaría a
\(f_{n,s}\) a ser constante, contradicción para \(n\ge2\). La ley zeta da
masa positiva a \(1\) y a cada primo, así que la varianza es positiva.

Por tanto

\[
 \boxed{
 \mathcal O_{s,c_{n,s}}(f_{n,s})\le0
 \quad\Longleftrightarrow\quad
 \mathcal B_{n,s}\le\kappa A_n.}                        \tag{24}
\]

La forma cúbica orientada existe, pero (24) demuestra que no es un lema
intermedio: es el objetivo mismo multiplicado por una cantidad positiva.

## 5. Determinante de tres marcas

Condicionado a cualquier entero total, sean \(Z_1,Z_2,Z_3\) marcas iid y
sean \(g_1,g_2,g_3\) tests. Por independencia de las columnas,

\[
 \boxed{
 \mathbb E\det[g_i(Z_j)]_{i,j=1}^3
 =\det[\mathbb E g_i(Z_j)]_{i,j=1}^3=0,}                  \tag{25}
\]

porque las tres columnas de la matriz de medias son iguales. Si se cuadra,

\[
 \mathbb E\det[g_i(Z_j)]^2\ge0,                           \tag{26}
\]

pero (26) vale para cualquier distribución de marcas, incluida la
desplazada. El determinante sin cuadrar pierde toda orientación por
intercambiabilidad; el cuadrado pierde el signo por PSD.

## 6. La uniformidad local distingue al desplazado, pero no orienta

Condicionado a haber elegido la torre \(p\) con exponente total \(a\), el
selector de zeta satisface

\[
 K\mid(p,a)\sim\operatorname{Unif}\{1,\ldots,a\}.         \tag{27}
\]

Por reflexión,

\[
 \boxed{
 \mathbb E\left[\left(K-{a+1\over2}\right)^{2j+1}
       \middle|p,a\right]=0\qquad(j\ge0).}                \tag{28}
\]

Esta identidad es específica: para el selector desplazado de `104_49`, con
\(p=5,5^c=2,a=2\),

\[
 \mathbb P(K=1)={25\over42},\qquad
 \mathbb P(K=2)={17\over42},                              \tag{29}
\]

y por tanto

\[
 \mathbb E(K-3/2)^3=-{1\over42},\qquad
 \mathbb E(K-\mathbb EK)^3={425\over9261}>0.             \tag{30}
\]

La primera cantidad de (30) está centrada en el punto medio geométrico
\(3/2\), como exige la reflexión (28); la segunda está centrada en la media
real del selector y es su tercer momento central. No se identifican ambas.

Sin embargo, al mezclar torres reales, el selector unitario tampoco posee
un tercer signo global. Para \(N=6\), escriba
\(x=\log2<y=\log3\). Sus dos átomos tienen probabilidades
\(x/(x+y),y/(x+y)\), y

\[
 \boxed{
 \mathbb E[(Z-\mathbb EZ)^3\mid N=6]
 =-{xy(y-x)^4\over(x+y)^3}<0.}                            \tag{31}
\]

Para \(N=18=2\cdot3^2\), los átomos son \(x,y,2y\), con pesos
\(x/L,y/L,y/L\), \(L=x+2y\). Poniendo \(r=y/x\),

\[
 \mathbb E[(Z-\mathbb EZ)^3\mid N=18]
 ={x^3r\over(1+2r)^3}
 \{-2+13r-33r^2+33r^3-9r^4\}.                            \tag{32}
\]

Las desigualdades enteras

\[
 2^3<3^2,\qquad 3^5<2^8
\]

dan \(3/2<r<8/5\). Si \(r=3/2+t\), \(0<t<1/10\), el polinomio entre
llaves en (32) es

\[
 {145\over16}+{61\over4}t-6t^2-21t^3-9t^4>0.             \tag{33}
\]

En efecto, aun omitiendo el término lineal positivo, su lado derecho es
mayor que
\(145/16-6/100-21/1000-9/10000>0\). Por (31)--(33), la tercera
asimetría condicionada tiene ambos signos dentro de la aritmética real.

## 7. Tercera diferencia de la fase Laguerre

Para incrementos positivos \(u,v,w\), defina

\[
 \Delta_{u,v,w}^{(3)}P_n(t)
 =\Delta_u\Delta_v\Delta_wP_n(t),\qquad
 P_n=L_{n-1}^{(1)}.                                      \tag{34}
\]

Como

\[
 P_n'''(x)=-L_{n-4}^{(4)}(x),
\]

se tiene

\[
 \boxed{
 \Delta_{u,v,w}^{(3)}P_n(t)
 =-\int_0^u\!\int_0^v\!\int_0^w
 L_{n-4}^{(4)}(t+a+b+c)\,dc\,db\,da.}                   \tag{35}
\]

Para \(n\ge5\), \(L_{n-4}^{(4)}\) tiene \(n-4\) ceros positivos simples y
alterna signo. Tomando un cubo suficientemente pequeño dentro de intervalos
sucesivos, (35) adopta ambos signos. Esto incluye todo \(n\ge150\). Por
consiguiente, la tercera diferencia no convierte la reflexión (28) en una
cota término a término para el vector Laguerre.

## 8. Falsificador desplazado y alcance

Para

\[
 Z_c(s)=\zeta(s+c)\zeta(s-c),\qquad0<c<1/2,               \tag{36}
\]

los coeficientes son positivos y la renovación

\[
 (\log n)a_c(n)=\sum_{d\mid n}\omega_c(d)a_c(n/d),\qquad
 \omega_c(d)=2\Lambda(d)\cosh(c\log d)>0                \tag{37}
\]

produce un Palm de tres marcas idéntico a (2), con su selector condicionado
correspondiente. Las identidades (16), (19), (25) y la positividad (26) son
puramente probabilísticas y siguen siendo válidas. Pero la completada
\(\xi(s+c)\xi(s-c)\) posee ceros fuera de \(\Re s=1/2\) y coeficientes de Li
exponencialmente negativos en una subsucesión (`104_48`).

La reflexión local (28) sí rechaza el sistema desplazado por (29)--(30).
Lo que falla es promover esa reflexión a una desigualdad global: (31)--(33)
muestran que ni siquiera la tercera asimetría del selector unitario real
tiene signo, y (35) muestra que el test Laguerre tampoco lo aporta.

## 9. Veredicto

Queda probado incondicionalmente:

1. el Palm unitario de tres marcas y el kernel `lcm` triple (2), (6)--(8);
2. el comparador polar \(\Gamma(4,\varepsilon)\) con el factor exacto seis
   (10)--(12);
3. la descomposición cúbica completada (16)--(18);
4. la forma orientada (19) y su equivalencia exacta con el margen
   (22)--(24);
5. el colapso del determinante alternante y la genericidad de su cuadrado
   (25)--(26);
6. la reflexión unitaria y su falla desplazada racional (28)--(30);
7. los dos signos aritméticos reales (31)--(33);
8. los dos signos de la tercera diferencia Laguerre (35).

Queda descartado usar estas formas cúbicas canónicas como fuente autónoma de
la cota (1). El sucesor tendría que correlacionar la reflexión local (28) con
la factorización global de \(N\) de una manera que no se reduzca ni al tercer
momento central ni a (19), y que conserve un signo después de promediar el
Laguerre oscilatorio. No se ha construido tal desigualdad.

## 10. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 three_mark_unit_palm_orientation_check.py
```

El checker usa solo enteros y `Fraction`. Verifica el Palm condicionado, el
factor seis del Gamma polar, las identidades cúbicas, el U-estadístico
orientado, el determinante alternante, el falsificador racional local, los
dos signos de (31)--(33) y las terceras diferencias Laguerre en
\(n=150,151,152\). No evalúa zeta, A1 ni RH.
