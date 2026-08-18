# 104_13 — M5 Selberg–Riccati: recurrencia exacta y barrera de escala

**Estado.** La identidad positiva de Selberg

\[
 b=\Lambda\log+\Lambda*\Lambda=\mu*\log ^2\geq0
\]

sí induce una recurrencia exacta en el grado Laguerre para el correlador
regulado de `104_12`. Sin embargo, no induce una desigualdad unilateral. Al
separar el doble polo, el coeficiente de Selberg centrado cancela un término
de la recurrencia de tamaño \(\varepsilon^{-n-1}\). La estimación sumatoria
clásica \(O(x)\) controla ambas piezas solamente a esa misma escala; con
\(\varepsilon=1/n\), su norma dual es al menos
\(n(n-1)^n-1\), frente al presupuesto \(O(\log n)\).

Por tanto, **la positividad de \(b\), su fórmula sumatoria efectiva y la
identidad de Riccati no producen la nueva cota incondicional**. Una estimación
del residuo acoplado que sí fuera suficiente volvería a contener explícitamente
el correlador \(C_{n,\varepsilon}\). Este documento es un stop-gate del uso
autónomo de Selberg–Riccati; no descarta un teorema aritmético nuevo sobre los
pesos reales de von Mangoldt y no prueba A1 ni RH.

## 1. Notación regulada

Fíjese

\[
 a=1+\varepsilon>1,\qquad t={z\over1-z},\qquad s=a+t,
\]

y póngase

\[
 \ell(s)=-{\zeta'(s)\over\zeta(s)}
       =\sum_{m\ge2}{\Lambda(m)\over m^s}.
\tag{1}
\]

Definimos

\[
 p_n=\sum_{m\ge2}{\Lambda(m)\over m^a}L_n(\log m),
 \qquad
 j_n=\int_1^\infty x^{-a}L_n(\log x)\,dx
     ={(\varepsilon-1)^n\over\varepsilon^{n+1}},
\tag{2}
\]

\[
 c_n=p_n-j_n.
\tag{3}
\]

Así, \(c_n=C_{n,\varepsilon}\) en la normalización de `104_11`–`104_12`.
Sus generatrices son

\[
 P(z)=\sum_{n\ge0}p_nz^n={1\over1-z}\ell(a+t),
 \quad
 J(z)=\sum_{n\ge0}j_nz^n={1\over(1-z)(\varepsilon+t)},
 \quad C=P-J.
\tag{4}
\]

La identidad de Selberg es

\[
 {\zeta''\over\zeta}(s)=-\ell'(s)+\ell(s)^2
  =\sum_{m\ge1}{b(m)\over m^s},
\qquad
 b(m)=\Lambda(m)\log m+(\Lambda*\Lambda)(m)\ge0.
\tag{5}
\]

La última igualdad también es \(b=\mu*\log^2\). En particular,

\[
 b(p^k)=(2k-1)(\log p)^2,
 \qquad
 b(p^rq^s)=2\log p\log q\quad(p\ne q),
\tag{6}
\]

y \(b(m)=0\) si \(m\) tiene al menos tres divisores primos distintos.

Sean

\[
 \beta_n=\sum_{m\ge1}{b(m)\over m^a}L_n(\log m),
 \qquad
 {\mathcal B}(z)=\sum_{n\ge0}\beta_nz^n
 ={1\over1-z}{\zeta''\over\zeta}(a+t).
\tag{7}
\]

El doble polo de (7) tiene generatriz

\[
 Q(z)={2\over(1-z)(\varepsilon+t)^2}
     ={2(1-z)\over\{\varepsilon+(1-\varepsilon)z\}^2}
     =\sum_{n\ge0}q_nz^n.
\tag{8}
\]

Escribimos

\[
 d_n=\beta_n-q_n,
 \qquad D(z)={\mathcal B}(z)-Q(z).
\tag{9}
\]

## 2. Recurrencia exacta en el grado

Para dos sucesiones \(x,y\), denote

\[
 (x*y)_n=\sum_{k=0}^nx_ky_{n-k},
 \qquad x_{-1}=0.
\]

**Teorema 1 (recurrencia Selberg–Riccati).** Para todo
\(n\ge0\) y \(\varepsilon>0\),

\[
\boxed{
\begin{aligned}
 d_n={}&-(n+1)c_{n+1}+(2n+1)c_n-nc_{n-1}\\
 &+2\{(j*c)_n-(j*c)_{n-1}\}
   +\{(c*c)_n-(c*c)_{n-1}\}.
\end{aligned}}
\tag{10}
\]

En particular,

\[
\boxed{
\begin{aligned}
 (n+1)c_{n+1}={}&(2n+1)c_n-nc_{n-1}\\
 &+2\{(j*c)_n-(j*c)_{n-1}\}
  +\{(c*c)_n-(c*c)_{n-1}\}-d_n.
\end{aligned}}
\tag{11}
\]

**Prueba.** De (4), \(\ell=(1-z)P\), mientras
\(ds/dz=(1-z)^{-2}\). Por tanto

\[
 {1\over1-z}\{-\ell'(s)+\ell(s)^2\}
 =(1-z)P-(1-z)^2P'+(1-z)P^2.
\tag{12}
\]

La misma identidad con \(P\) reemplazado por \(J\) da exactamente \(Q\),
porque para \(r=s-1\)

\[
 -\left({1\over r}\right)'+{1\over r^2}={2\over r^2}.
\]

Restando ambas identidades y usando \(P=J+C\),

\[
 D=(1-z)C-(1-z)^2C'
       +2(1-z)JC+(1-z)C^2.
\tag{13}
\]

Extraer \([z^n]\) en (13) prueba (10), y despejar \(c_{n+1}\) prueba
(11). \(\square\)

La recurrencia es triangular, pero no es una inducción con signo: el nuevo
input \(d_n\) es un coeficiente Laguerre firmado de la medida de Selberg.

## 3. La colisión del polo ocurre dentro de la recurrencia

Póngase

\[
 h(s)=\ell(s)-{1\over s-1}.
\tag{14}
\]

La función \(h\) es analítica en \(s=1\) y

\[
 h(1)=-\gamma.
\tag{15}
\]

La identidad centrada detrás de (13) es

\[
 {\zeta''\over\zeta}(s)-{2\over(s-1)^2}
 =-h'(s)+{2h(s)\over s-1}+h(s)^2.
\tag{16}
\]

Como

\[
 {2h(s)\over s-1}=-{2\gamma\over s-1}+\text{función analítica en }s=1,
\]

para cada \(n\) fijo se tiene

\[
 \boxed{d_n=-2\gamma j_n+O_n(1)
 \qquad(\varepsilon\downarrow0).}
\tag{17}
\]

Por otra parte, \(c_0=h(1+\varepsilon)=-\gamma+O(\varepsilon)\), y entonces

\[
 2\{(j*c)_n-(j*c)_{n-1}\}
 =-2\gamma j_n+O_n(\varepsilon^{-n}).
\tag{18}
\]

Las dos cantidades principales de (17)–(18), cada una de orden
\(\varepsilon^{-n-1}\), se cancelan en (10). Los órdenes inferiores también
se cancelan exactamente porque el miembro restante de (10) tiene límite
finito. Estimar \(d_n\) y \((j*c)_n\) por separado destruye la
renormalización polo–primos que hizo finito a \(c_n\).

El coeficiente del doble polo en (8) es explícito. Si
\(r=(1-\varepsilon)/\varepsilon\),

\[
 q_n={2(-1)^n\over\varepsilon^2}
 \left\{(n+1)r^n+n r^{n-1}\right\},
\tag{19}
\]

donde el segundo sumando se interpreta como cero para \(n=0\). En
particular,

\[
 \beta_n=q_n-2\gamma j_n+O_n(1)
 =2(n+1)(-1)^n\varepsilon^{-n-2}{1+O_n(\varepsilon)\}.
\tag{20}
\]

Así, aun para los coeficientes aritméticos reales y positivos \(b(m)\), el
pullback Laguerre alterna de signo cerca del límite crítico.

## 4. Falsificador de signo dentro de la medida aritmética real

La pérdida de signo no requiere una medida competidora. Para \(n=1\), (20)
da

\[
 \beta_1<0
\]

cuando \(a>1\) está suficientemente cerca de \(1\). En cambio, cuando
\(a\to\infty\), el término \(m=2\) domina la serie absolutamente convergente
y

\[
 \beta_1
 =b(2)2^{-a}L_1(\log2)+O(3^{-a}\operatorname{poly}(a))>0,
\tag{21}
\]

porque \(b(2)=(\log2)^2\) y \(L_1(\log2)=1-\log2>0\). Por continuidad,
\(\beta_1(a)\) cambia de signo en \((1,\infty)\).

Por consiguiente, \(b(m)\ge0\) no proporciona ni siquiera el signo del
primer coeficiente transformado a lo largo del regulador real. Cualquier
uso de (11) necesita información firmada adicional.

## 5. Precio exacto de la fórmula sumatoria de Selberg

Sea

\[
 S_b(x)=\sum_{m\le x}b(m),
\qquad
 R_b(x)=S_b(x)-2\{x\log x-x+1\}.
\tag{22}
\]

El término sustraído es exacto, pues

\[
 \int_1^\infty 2\log x\,x^{-s}\,dx={2\over(s-1)^2}.
\]

La fórmula de simetría de Selberg da la escala

\[
 |R_b(x)|\le Kx
\tag{23}
\]

con una constante efectiva después de agrandarla para el rango inicial. La
integración de Stieltjes por partes, con
\(f_{n,a}(x)=x^{-a}L_n(\log x)\), da

\[
 d_n=-\int_1^\infty R_b(x)f_{n,a}'(x)\,dx.
\tag{24}
\]

Por tanto, el uso de (23) por dualidad produce exactamente la carga

\[
 |d_n|\le K\,\mathcal N_n(\varepsilon),
\quad
 \mathcal N_n(\varepsilon)
 =\int_0^\infty e^{-\varepsilon u}
   |L_n'(u)-aL_n(u)|\,du.
\tag{25}
\]

Esta es la norma operatorial del funcional (24) en la bola
\(|R_b(x)|\le Kx\): el signo de \(R_b\) puede aproximar el signo de
\(-f_{n,a}'\). No es solamente una cota elegida de manera torpe.

La carga tiene el siguiente límite inferior exacto. Integrando una vez por
partes y usando (2),

\[
 \int_0^\infty e^{-\varepsilon u}
 \{L_n'(u)-aL_n(u)\}\,du
 =-1-j_n.
\tag{26}
\]

Luego

\[
 \boxed{\mathcal N_n(\varepsilon)\ge |1+j_n|.}
\tag{27}
\]

En la elección diagonal \(\varepsilon=1/n\), \(n\ge2\),

\[
 j_n=(-1)^n n(n-1)^n,
\]

y por tanto

\[
 \boxed{
 \mathcal N_n(1/n)\ge n(n-1)^n-1
       =\exp\{(1+o(1))n\log n\}.}
\tag{28}
\]

El presupuesto del gate de primera diferencia es
\(\frac12\Delta A_n=O(\log n)\). Así, la fórmula sumatoria \(O(x)\) pierde
un factor superexponencial en el grado. La positividad no repara (28): la
Sección 4 muestra que el pullback de la medida positiva real ya tiene ambos
signos, y `103_63` construye además modelos de medida positiva que satisfacen
la escala sumatoria de Selberg y dan ambos signos al funcional cuantílico.

## 6. Certificado de no circularidad

La única resta que elimina la divergencia principal de (10) es

\[
 \widetilde d_n
 :=d_n-2\{(j*c)_n-(j*c)_{n-1}\}.
\tag{29}
\]

Pero (29) contiene la sucesión original \(c\). La recurrencia se convierte
en

\[
 \widetilde d_n
 =-(n+1)c_{n+1}+(2n+1)c_n-nc_{n-1}
  +\{(c*c)_n-(c*c)_{n-1}\}.
\tag{30}
\]

Por ello, postular una cota firmada para \(\widetilde d_n\) suficientemente
fuerte como para controlar \(c_{n+1}\) no es una consecuencia de la
positividad o la sumatoria de \(b\): es un nuevo teorema acoplado que ya
reintroduce el correlador A1. Las identidades (10) y (30) son válidas y
pueden servir de coordenada para tal teorema, pero no aportan su signo.

## 7. Decisión

```text
probado:
  recurrencia Selberg–Riccati exacta en el grado Laguerre;
  cancelación interna de escala epsilon^(-n-1) en esa recurrencia;
  cambio de signo del primer pullback para la medida b real;
  carga dual >= |1+j_n| para todo uso de la sumatoria O(x);
  carga >= n(n-1)^n-1 al tomar epsilon=1/n.

descartado:
  positividad de b como signo coeficiente a coeficiente;
  fórmula sumatoria de Selberg + parcial summation como cota A1;
  Riccati como inducción unilateral autónoma;
  estimación separada del coeficiente centrado y la colisión polo–primos.

no descartado:
  un nuevo teorema firmado para la aritmética real que estime directamente
  el residuo acoplado (29) sin asumir la cota buscada.

no probado:
  la cota de primera diferencia, A1 o RH.
```

## Verificación mecánica

`tools/m5_riccati_degree_check.py` verifica (10), (19) y la resta del doble
polo con aritmética `Fraction` para una serie de Dirichlet atómica formal. No
usa valores de \(\zeta\), punto flotante ni localización de ceros.
