# 104_49 — Renovación divisora unitaria y cancelación momento--cumulante

**Resultado.** La factorización de la ley zeta en exponentes geométricos
permite refinar el selector divisor de `104_43`: primero se elige una torre
prima y después, condicionado al exponente total de esa torre, se elige
uniformemente una de sus alturas. Esta uniformidad usa exactamente

\[
 \Lambda(p^k)=\log p.                                      \tag{1}
\]

Al conservar la diferencia de medias contra el split Gamma se obtiene una
identidad firmada global. Para cada momento de orden \(r\), el bloque del
selector vale

\[
 \kappa_r(s)-{\mathbb E_sX^r\over r},
\]

y el bloque que transporta la ley total al polo vale

\[
 {\mathbb E_sX^r\over r}-(r-1)!(s-1)^{-r}.
\]

Por tanto el momento total \(\mathbb E_sX^r\) se cancela **exactamente** y
queda

\[
 \kappa_r(s)-(r-1)!(s-1)^{-r}.                             \tag{2}
\]

La combinación Laguerre de (2) es precisamente
\(\mathcal B_{n,s}\to B_n=A_n-\lambda_n\). No aparece un término coercivo
adicional. Además, el defecto condicionado antes de promediar tiene ambos
signos para el propio test \(P_{151}=L_{150}^{(1)}\), entre primos reales.
Así quedan descartados tanto el signo punto a punto como una cota obtenida
separando los dos bloques de momentos.

El sistema desplazado \(\omega_c\) no posee el selector uniforme: ya en una
torre de exponente dos, sus probabilidades difieren de \(1/2\). Esto confirma
que (1) sí distingue al falsificador. Pero, al promediar un test que depende
solamente del divisor marcado, la uniformidad no deja un **término de defecto
adicional**: produce \(\kappa_r(s)\), y la forma momento--cumulante resultante
es genérica para derivadas logarítmicas (aunque sus cumulantes cambien al
cambiar los pesos). Por ello este ataque no prueba

\[
 B_n\le {1501\over2002}A_n,\qquad n\ge150,                 \tag{3}
\]

ni A1 ni RH.

## 1. Palm geométrico y marca uniforme exacta

Fijemos \(s=1+\varepsilon>1\). Bajo la ley zeta

\[
 \mathbb P_s(N=m)={m^{-s}\over\zeta(s)},
 \qquad N=\prod_p p^{A_p},                                 \tag{4}
\]

los exponentes son independientes y, con \(q_p=p^{-s}\),

\[
 \mathbb P(A_p=a)=(1-q_p)q_p^a,qquad a\ge0.               \tag{5}
\]

Sea

\[
 X=\log N=\sum_p A_p\ell_p,qquad
 \ell_p=\log p,qquad
 \mathfrak m(s)=\mathbb E_sX=-{\zeta'\over\zeta}(s).      \tag{6}
\]

Al size-biasar por \(X\), primero se elige una coordenada \(P=p\) con

\[
 \mathbb P(P=p)={\ell_pq_p/(1-q_p)\over\mathfrak m(s)},    \tag{7}
\]

y se reemplaza \(A_p\) por su versión size-biased \(A_p^*\). Si
\(G_p,G_p'\) son geométricas como en (5), independientes, entonces

\[
 \boxed{A_p^*\ \buildrel d\over=\ 1+G_p+G_p'.}            \tag{8}
\]

En efecto, ambos lados tienen función generatriz
\(t(1-q_p)^2/(1-q_pt)^2\). Definamos

\[
 K=1+G_p,qquad A_p^*-K=G_p'.                               \tag{9}
\]

Condicionado a \(A_p^*=a\), cada \(k=1,\ldots,a\) tiene antes de
normalizar la misma masa

\[
 (1-q_p)^2q_p^{a-1}.
\]

Por consiguiente

\[
 \boxed{\mathbb P(K=k\mid A_p^*=a,P=p)={1\over a}.}       \tag{10}
\]

Condicionado ahora al entero completo
\(N^*=\prod p^{a_p}\), el primer selector tiene probabilidad
\(a_p\ell_p/\log N^*\). Combinándolo con (10),

\[
 \boxed{
 \mathbb P(P=p,K=k\mid N^*)
 ={\ell_p\over\log N^*}\mathbf1_{1\le k\le a_p}.}       \tag{11}
\]

Para \(D=P^K\), (11) es exactamente
\(\Lambda(D)/\log N^*\). Esta construcción retiene simultáneamente todos
los primos y todas las potencias, pero refina el selector de `104_43`; no
produce una ley marginal diferente.

## 2. Identidad firmada sin centrar las medias

Para una función polinómica \(f\), defina sobre
\(m=\prod p^{a_p}\), \(L=\log m\),

\[
 (\mathsf U f)(m)
 ={1\over L}\sum_{p^{a_p}\Vert m}\ell_p
          \sum_{k=1}^{a_p}f(k\ell_p),                      \tag{12}
\]

y el split continuo

\[
 (\mathsf C f)(L)={1\over L}\int_0^L f(x)\,dx.            \tag{13}
\]

Sea \(X_0^*\sim\Gamma(2,\varepsilon)\). Condicionado a
\(X_0^*=L\), una de sus dos coordenadas exponenciales es uniforme en
\([0,L]\), de modo que (13) es su selector. La identidad conjunta, sin
retirar constantes ni medias, es

\[
\begin{aligned}
 \mathfrak M_\varepsilon(f)
 :={}&\sum_{d\ge2}{\Lambda(d)\over d^s}f(\log d)
      -\int_0^\infty e^{-\varepsilon x}f(x)\,dx\\
 ={}&\mathfrak m(s)\,\mathbb E_s^*
       \{\mathsf U f(N^*)-\mathsf C f(\log N^*)\}\\
 &+\mathfrak m(s)\,\mathbb E_s^*\mathsf C f(\log N^*)
      -{1\over\varepsilon}\mathbb E\mathsf C f(X_0^*).
                                                               \tag{14}
\end{aligned}
\]

Equivalente y más directamente, si

\[
 \Delta_f(m)=
 \sum_{p^{a_p}\Vert m}\ell_p\sum_{k=1}^{a_p}f(k\ell_p)
 -\int_0^{\log m}f(x)\,dx,                                 \tag{15}
\]

entonces los dos renglones firmados de (14) son

\[
 \boxed{
 \mathscr S_s(f)={1\over\zeta(s)}
       \sum_{m\ge1}{\Delta_f(m)\over m^s},}               \tag{16}
\]

\[
 \boxed{
 \mathscr T_s(f)=\mathbb E_s\int_0^X f(x)\,dx
       -\int_0^\infty e^{-\varepsilon x}f(x)\,dx,}         \tag{17}
\]

y \(\mathfrak M_\varepsilon=\mathscr S_s+\mathscr T_s\).
En particular, para \(f\equiv1\), (16) vale cero y (17) conserva la
diferencia de masas \(\mathfrak m(s)-1/\varepsilon\). No se ha perdido el
término constante por centrar.

## 3. Cancelación exacta momento--cumulante

Sean

\[
 m_r(s)=\mathbb E_sX^r,
 \qquad
 \kappa_r(s)=\left.{d^r\over dt^r}
       \log\mathbb E_se^{tX}\right|_{t=0}.                 \tag{18}
\]

La independencia geométrica y la renovación unitaria dan

\[
 \boxed{
 \kappa_r(s)=
 \sum_{p}\ell_p^r\sum_{k\ge1}k^{r-1}p^{-ks}
 =\sum_{d\ge2}{\Lambda(d)(\log d)^{r-1}\over d^s}.}       \tag{19}
\]

Para \(f(x)=x^{r-1}\), Tonelli en (15) y
\(\mathbb P(A_p\ge k)=q_p^k\) producen

\[
 \boxed{
 \mathscr S_s(x^{r-1})=\kappa_r(s)-{m_r(s)\over r},
 \qquad
 \mathscr T_s(x^{r-1})={m_r(s)\over r}
                         -(r-1)!\varepsilon^{-r}.}         \tag{20}
\]

Por tanto los momentos completos, que contienen todas las interacciones
entre primos distintos, se cancelan grado por grado:

\[
 \boxed{
 \mathfrak M_\varepsilon(x^{r-1})
 =\kappa_r(s)-(r-1)!\varepsilon^{-r}.}                     \tag{21}
\]

Sea ahora

\[
 P_n(x)=L_{n-1}^{(1)}(x),\qquad
 c_{n,r}(s)=(-1)^{r-1}{n\choose r}{s^{r-1}\over(r-1)!}.
                                                                    \tag{22}
\]

Como \(P_n(sx)=\sum_{r=1}^nc_{n,r}(s)x^{r-1}\), (20)--(21) dan

\[
\boxed{
 {\mathcal B_{n,s}\over s}
 =\sum_{r=1}^nc_{n,r}(s)
   \{\kappa_r(s)-(r-1)!\varepsilon^{-r}\}.}               \tag{23}
\]

Si

\[
 R(q)=-{\zeta'\over\zeta}(1+q)-{1\over q},                \tag{24}
\]

entonces

\[
 \kappa_r(s)-(r-1)!\varepsilon^{-r}
 =(-1)^{r-1}R^{(r-1)}(\varepsilon),                        \tag{25}
\]

y (23) se reduce a

\[
 \boxed{
 \mathcal B_{n,s}
 =s\sum_{j=0}^{n-1}{n\choose j+1}{s^j\over j!}
       R^{(j)}(\varepsilon).}                              \tag{26}
\]

La ecuación (26) es la misma forma escalar de `104_03` y `104_45`.
Además \(\mathcal B_{n,s}\to B_n\) cuando \(s\downarrow1\). Así, usar
una desigualdad separada sobre los dos miembros de (20) rompe una
cancelación exacta; mantenerla recompone el target original.

La misma recomposición se ve simultáneamente en todos los grados. Con
\(t=s/(1-z)\), \(\tau=t-s=sz/(1-z)\) y

\[
 A_s(\tau)={1-\zeta(s+\tau)/\zeta(s)\over\tau},
 \qquad A_s(0)=\mathfrak m(s),                              \tag{27}
\]

se tiene

\[
 \sum_{n\ge1}\mathscr S_s(P_n(s\,\cdot))z^{n-1}
 ={\mathcal L(t)-A_s(\tau)\over(1-z)^2},                  \tag{28}
\]

\[
 \sum_{n\ge1}\mathscr T_s(P_n(s\,\cdot))z^{n-1}
 ={A_s(\tau)-1/(\varepsilon+\tau)\over(1-z)^2}.           \tag{29}
\]

El término intermedio se cancela y (28)+(29) vale
\((1-z)^{-2}R(\varepsilon+\tau)\).

## 4. El defecto unitario no tiene signo, ya en grado 151

Para el test real de A1 escribamos

\[
 \Delta_{n,s}(m)=
 \sum_{p^{a_p}\Vert m}\ell_p\sum_{k=1}^{a_p}P_n(sk\ell_p)
 -{1-L_n(s\log m)\over s}.                                \tag{30}
\]

Es (15), pues \((L_n)'=-L_{n-1}^{(1)}\). Fijado \(s>1\), el término
homogéneo principal de (30), para \(n=151\), es una constante positiva
por

\[
 \sum_p\ell_p^{151}\sum_{k=1}^{a_p}k^{150}
 -{(\log m)^{151}\over151}.                               \tag{31}
\]

Si \(m=p\) es primo, (31) es
\((1-1/151)(\log p)^{151}>0\). Por tanto

\[
 \Delta_{151,s}(p)>0                                      \tag{32}
\]

para todo primo suficientemente grande.

Si \(m=pq\), con \(p\ne q\) primos y
\(x=\log p,y=\log q\), (31) es

\[
 x^{151}+y^{151}-{(x+y)^{151}\over151}.                   \tag{33}
\]

En \(x=y\), (33) vale
\(x^{151}(2-2^{151}/151)<0\), y el signo persiste cuando
\(x/y\to1\). Por Bertrand, para cada \(J\) existen primos

\[
 2^J<p_J<2^{J+1},qquad
 2^{J+1}<q_J<2^{J+2}.                                     \tag{34}
\]

Entonces \(\log p_J/(J\log2)\to1\) y
\(\log q_J/(J\log2)\to1\). Dividiendo (30) por
\((J\log2)^{151}\), los términos de grado menor desaparecen y (33)
implica

\[
 \Delta_{151,s}(p_Jq_J)<0                                 \tag{35}
\]

para todo \(J\) suficientemente grande. Las ecuaciones (32) y (35)
descartan ambas desigualdades punto a punto para el selector unitario real.

## 5. El falsificador desplazado pierde la marca uniforme

Para

\[
 Z_c(s)=\zeta(s+c)\zeta(s-c),qquad r=p^c>1,               \tag{36}
\]

el coeficiente del factor local en \(p^a\) es

\[
 b_a(r)=\sum_{j=0}^a r^{2j-a},                             \tag{37}
\]

y el peso logarítmico de \(p^k\) es
\(\ell_p(r^k+r^{-k})\). La renovación local es

\[
 a b_a(r)=\sum_{k=1}^a(r^k+r^{-k})b_{a-k}(r).              \tag{38}
\]

Por ello, condicionado al exponente total \(a\), el selector desplazado es

\[
 \pi_{a,c}(k)={(r^k+r^{-k})b_{a-k}(r)\over a b_a(r)}.      \tag{39}
\]

Para \(a=2\),

\[
 b_2=r^2+1+r^{-2},qquad
 \boxed{
 \pi_{2,c}(1)={1\over2}+{1\over2b_2},\quad
 \pi_{2,c}(2)={1\over2}-{1\over2b_2}.}                  \tag{40}
\]

Así (10) es una propiedad aritmética que el falsificador no satisface.
Pero al tomar esperanza de \(f(p^K)\), (39) vuelve a producir sus pesos
\(\omega_c(p^k)\); la identidad momento--cumulante análoga es entonces la
identidad genérica de su derivada logarítmica. En otras palabras, la marca
uniforme reconstruye los cumulantes correctos de zeta, pero no deja tras el
promedio una penalización separada que pueda dar coercividad; para el sistema
desplazado ocurre lo mismo con sus cumulantes distintos.

Una prueba futura tendría que retener una correlación adicional entre esa
marca uniforme y la factorización completa. Las dos correlaciones lineales
más inmediatas no sirven: el defecto (30) cambia de signo por (32)--(35), y
su promedio exacto cancela los momentos por (20).

## 6. Veredicto

Queda probado incondicionalmente:

1. el Palm geométrico unitario (8)--(11);
2. la identidad firmada global sin centrar (14)--(17);
3. la cancelación exacta momento--cumulante (20)--(26);
4. el cambio de signo real de \(\Delta_{151,s}\) (32)--(35);
5. la falla explícita de uniformidad del falsificador (40).

Queda descartado:

```text
marca uniforme dentro de cada exponente
+ signo punto a punto del defecto selector/Gamma
=> cota proporcional;

separar momentos del selector y del total
=> ganancia (los momentos se cancelan exactamente).
```

El único sucesor no refutado es una desigualdad firmada global que use una
correlación no lineal de la marca uniforme con varias torres simultáneamente,
sea falsa para (39), y sobreviva al promedio sin reducirse a (26). No se ha
obtenido esa desigualdad en este ataque.

## 7. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 unit_divisor_renewal_signed_gate_check.py
```

El checker usa solo enteros y `Fraction`. Verifica el Palm uniforme, la
primitiva Laguerre, la cancelación momento--cumulante, los dos signos
algebraicos del defecto en grado 151 y la renovación desplazada (38)--(40).
