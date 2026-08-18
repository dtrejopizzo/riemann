# 104_86 — Kernel Bose positivo y autorreflexión seno de Mellin

**Resultado.** La continuación de \(\zeta\) en la franja crítica admite una
representación de Mellin de signo único. Ponga

\[
 q(x)={1\over x}-{1\over e^x-1}>0.                     \tag{1}
\]

Para \(0<\Re s<1\),

\[
 \boxed{
 \int_0^\infty x^{s-1}q(x)\,dx=-\Gamma(s)\zeta(s).}    \tag{2}
\]

La ecuación funcional es equivalente a la autorreflexión exacta

\[
 \boxed{
 q(x)={1\over\pi}\int_0^\infty
 q(t)\sin\left({xt\over2\pi}\right)\,dt,}              \tag{3}
\]

con la integral entendida en el sentido impropio de Dirichlet.

Sin embargo, (1)--(3) no fuerzan los ceros a \(\Re s=1/2\). El kernel no es
completamente monótono ni PF\(_\infty\), y existe un kernel positivo,
decreciente, con los mismos asintóticos y la misma reflexión seno, cuya
transformada posee cuartetos estrictamente fuera de la línea. Por tanto
signo único, monotonicidad, log-concavidad, simetría funcional y
autorreciprocidad no prueban Deep-\(\Lambda\) ni RH.

---

## 1. Representación de signo único

La fórmula clásica de Mellin,

\[
 \Gamma(s)\zeta(s)=\int_0^\infty {x^{s-1}\over e^x-1}\,dx
 \qquad(\Re s>1),                                      \tag{4}
\]

se renormaliza restando \(1/x\). La integral de (2) converge en
\(0<\Re s<1\): cerca de cero,

\[
 q(x)={1\over2}-{x\over12}+{x^3\over720}
       -{x^5\over30240}+\cdots,                         \tag{5}
\]

y en infinito \(q(x)=x^{-1}+O(e^{-x})\). La continuación desde (4), o una
integración por partes con corte, prueba (2). El signo es coherente con
\(\zeta(\sigma)<0\) para \(0<\sigma<1\).

Hay además una ley de probabilidad exacta. Con \(x=e^u\), defina

\[
 Q(u)=1-{e^u\over e^{e^u}-1}=e^u q(e^u),               \tag{6}
\]

y

\[
 p(u)=Q'(u)
 ={x\{(x-1)e^x+1\}\over(e^x-1)^2}>0.                  \tag{7}
\]

Se tiene \(Q(-\infty)=0\), \(Q(+\infty)=1\), de modo que
\(\int_\mathbb R p=1\). Integrar por partes en (2) da

\[
 \boxed{
 (s-1)\Gamma(s)\zeta(s)
 =\int_\mathbb R p(u)e^{(s-1)u}\,du.}                  \tag{8}
\]

Así los ceros de \(\zeta\) en la franja son ceros complejos de la función
generadora de momentos de una probabilidad explícita. La positividad de
una ley no excluye tales ceros.

## 2. Derivación de la reflexión seno

La ecuación funcional aplicada a (2) da

\[
 M(s)=R(s)M(1-s),\qquad M(s)=-\Gamma(s)\zeta(s),         \tag{9}
\]

con

\[
 R(s)=2^s\pi^{s-1}\Gamma(s)\sin{\pi s\over2}
 ={(2\pi)^s\over2\cos(\pi s/2)\Gamma(1-s)},
 \qquad R(s)R(1-s)=1.                                  \tag{10}
\]

La función

\[
 r(x)={1\over\pi}\sin{x\over2\pi}                    \tag{11}
\]

tiene transformada de Mellin \(R(s)\), por continuación desde su franja
fundamental. Además,

\[
 \mathcal M[x^{-1}q(1/x)](s)=M(1-s).                    \tag{12}
\]

La convolución multiplicativa de (10)--(12), seguida del cambio
\(t=1/y\), prueba (3). El núcleo \(r\) cambia de signo; la ecuación
funcional es una simetría firmada, no un operador positivo.

## 3. Stop-gates de positividad

La expansión (5) da

\[
 q'''(0^+)={1\over120}>0,                               \tag{13}
\]

en contradicción con \((-1)^3q'''\ge0\), necesaria para complete
monotonicity. Incluso el menor log-convexo de una transformada de Laplace
positiva falla:

\[
 \lim_{x\downarrow0}\{q(x)q''(x)-q'(x)^2\}
 =-{1\over144}<0.                                      \tag{14}
\]

En la coordenada logarítmica,

\[
 K_a(u)=e^{au}q(e^u),\qquad0<a<1,                       \tag{15}
\]

sí es estrictamente log-cóncava; esto solo proporciona PF\(_2\). Su
transformada bilateral es

\[
 \int_\mathbb R K_a(u)e^{zu}\,du
 =-\Gamma(a+z)\zeta(a+z).                              \tag{16}
\]

Para \(a=1/2\), (16) posee infinitos ceros sobre el eje imaginario por el
teorema de Hardy. Una función de frecuencia de Pólya PF\(_\infty\) tendría
transformada cero-libre en su franja fundamental. Por tanto el kernel real
no es PF\(_\infty\); alguna menor superior debe fallar.

## 4. Falsificador con la misma simetría

Fije \(0<\eta<1/2\) y \(a>0\). Sea

\[
 \nu=\delta_{-a}+\delta_a
      +\eta(\delta_{-2a}+\delta_{2a}),                  \tag{17}
\]

y elija \(c>0\) de modo que

\[
 d\mu(v)=c e^{-v/2}\,d\nu(v)                           \tag{18}
\]

tenga la normalización requerida. Defina

\[
 \widetilde q(x)=\int q(xe^{-v})\,d\mu(v)>0.           \tag{19}
\]

Es decreciente, tiene \(\widetilde q(0^+)=1/2\) tras normalizar y
\(x\widetilde q(x)\to1\). Su Mellin es

\[
 \widetilde M(s)=M(s)X(s),                             \tag{20}
\]

donde

\[
 X(s)=2c\left\{
 \cosh(a(s-\tfrac12))
 +\eta\cosh(2a(s-\tfrac12))\right\},
 \qquad X(1-s)=X(s).                                   \tag{21}
\]

Por (9) y (21), \(\widetilde M\) satisface la misma ecuación funcional y
\(\widetilde q\) la misma autorreflexión (3). No obstante, escribiendo
\(y=a(s-1/2)\), sus ceros adicionales cumplen

\[
 2\eta\cosh^2y+\cosh y-\eta=0.                         \tag{22}
\]

La raíz

\[
 x_-={-1-\sqrt{1+8\eta^2}\over4\eta}<-1               \tag{23}
\]

produce

\[
 y=\pm\operatorname {arcosh}(-x_-)+(2k+1)\pi i.        \tag{24}
\]

Si \(a>2\operatorname {arcosh}(-x_-)\), esos ceros satisfacen
\(0<\Re s<1\) y \(\Re s\ne1/2\).

## 5. Decisión

```text
probado:
  representación Mellin positiva (2) y probabilística (8);
  autorreflexión seno exacta (3);
  q no es CM, Stieltjes ni PF-infinito;
  un kernel positivo con los mismos asintóticos y la misma reflexión
  admite cuartetos off-line.

descartado:
  signo único + monotonía/log-concavidad + FE seno => RH.

no probado:
  una propiedad adicional específica del q aritmético que implique
  Deep-Lambda, A1 o RH.
```
