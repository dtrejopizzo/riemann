# 104_102 — Rigidez analítica/racional del transformado de Landau

## Resultado

Ponga

\[
 \ell_j(s)=\left(-{d\over ds}\right)^j
             \left(-{\zeta'(s)\over\zeta(s)}\right)
 =\sum_{m\ge2}{\Lambda(m)(\log m)^j\over m^s},
 \qquad \Re s>1.
 \tag{1}
\]

Este documento extiende `104_95` desde polinomios a transformaciones
analíticas y racionales. El resultado exacto es el siguiente.

> **Teorema A (rigidez analítica).** Sea
> \(\Phi\) un germen holomorfo en
> \(0\in\mathbb C^{r+1}\), y para \(\Re s\) grande defina
> \[
>  F(s)=\Phi(\ell_0(s),\ldots,\ell_r(s))
>      =\sum_{n\ge1}{a_n\over n^s}.
>  \tag{2}
> \]
> La serie de la derecha es la expansión ordinaria inducida por el Taylor
> de \(\Phi\). Suponga \(a_n\ge0\) para todo \(n\ge2\). Si esa serie
> representa a \(F\) para todo \(\Re s>1\) y la misma rama se prolonga
> holomórficamente a \(s=1\), entonces \(\Phi\) es constante.

No se exige que el Taylor de \(\Phi\) tenga coeficientes positivos. La
positividad requerida es únicamente la de los coeficientes de Dirichlet
ya ensamblados.

> **Teorema B (los cocientes singulares no abren una excepción).** Sea
> \(R=P/Q\in\mathbb C(X_0,\ldots,X_r)\), escrito en forma reducida. Si
> \(R(\ell_0(s),\ldots,\ell_r(s))\) posee una serie de Dirichlet
> **ordinaria** en algún semiplano derecho, entonces
> \[
>  Q(0)\ne0.
>  \tag{3}
> \]
> Por tanto \(R\) es ya un germen holomorfo en el origen y queda bajo el
> Teorema A cuando su serie llega a \(\Re s>1\), tiene coeficientes no
> negativos y cancela el polo en \(s=1\).

Hay una salvedad necesaria. «Holomorfa localmente en \(s=1\)» sin pedir
que la serie positiva llegue desde la derecha hasta \(1\) es demasiado
débil. Si \(\sigma_c\) es la abscisa de convergencia de (2), entonces:

> **Corolario C (dicotomía del ancla real).** Si la rama de \(F\) admite
> continuación holomorfa a \(s=1\), \(a_n\ge0\) y \(\Phi\) no es
> constante, necesariamente
> \[
>  \boxed{\sigma_c>1.}
>  \tag{4}
> \]
> Por el teorema de Landau, \(s=\sigma_c\) es una singularidad real de
> \(F\). Está a la derecha de todos los ceros no triviales de \(\zeta\),
> y por ello enmascara cualquier singularidad que el transformado conserve
> en esos ceros.

Así queda cerrada la ampliación analítica/racional natural de `104_95`:
o el transformado positivo alcanza \(s=1\) y es constante, o es no
constante y fabrica antes un ancla real \(\sigma_c>1\). No aparece una
transformación de Landau que cancele el polo, conserve coeficientes no
negativos y fuerce la ausencia de ceros en
\(1/2<\Re s<1\).

El resultado no cubre operadores no locales, shifts del argumento ni
transformaciones que no sean funciones de un jet finito
\((\ell_0,\ldots,\ell_r)\). No prueba Deep-\(\Lambda\), A1 ni RH.

---

## 1. El Taylor infinito sigue teniendo fibras *squarefree*

Escriba el Taylor convergente

\[
 \Phi(X)=\sum_{k\ge0}\Phi_k(X),
 \tag{5}
\]

donde \(\Phi_k\) es homogéneo de grado \(k\). Como cada \(\ell_j\)
tiene término constante nulo, el coeficiente de un entero fijo recibe
contribuciones de solo finitos grados; (5) define formalmente una serie
de Dirichlet. Para \(\Re s\) suficientemente grande la definición es
además absolutamente convergente, porque los \(\ell_j(s)\) están dentro
del polidisco de convergencia de \(\Phi\).

Sea \(n=p_1\cdots p_k\) producto de \(k\) primos distintos. Exactamente
como en `104_95`, ningún grado distinto de \(k\) puede contribuir:
menos de \(k\) factores no cubren todos los primos y más de \(k\)
factores repiten alguno. Por tanto

\[
 \boxed{
 a_{p_1\cdots p_k}
   =(\mathscr S_k\Phi_k)(\log p_1,\ldots,\log p_k),}
 \tag{6}
\]

donde, sobre monomios,

\[
 \mathscr S_k(X_{j_1}\cdots X_{j_k})(x_1,\ldots,x_k)
 =\sum_{\pi\in S_k}\prod_{i=1}^kx_i^{j_{\pi(i)}+1}.
 \tag{7}
\]

La aplicación \(\mathscr S_k\) es inyectiva: sus imágenes son múltiplos
no nulos de los polinomios simétricos monomiales asociados a las
particiones \((j_1+1,\ldots,j_k+1)\).

## 2. Prueba del Teorema A

La holomorfía de la misma rama en \(s=1\), junto con la representación
por (2) para \(\sigma>1\), da

\[
 \lim_{\sigma\downarrow1}\{F(\sigma)-a_1\}<\infty.
 \tag{8}
\]

Como \(a_n\ge0\), la convergencia monótona implica

\[
 \sum_{n\ge2}{a_n\over n}<\infty.
 \tag{9}
\]

Suponga \(\Phi_k\ne0\) para algún \(k\ge1\), y ponga
\(Q_k=\mathscr S_k\Phi_k\). Por inyectividad, \(Q_k\ne0\). La familia
\(\{\log p:p\text{ primo}\}\) es infinita y por ello su producto
cartesiano es Zariski-denso. Se pueden fijar primos distintos
\(q_1,\ldots,q_{k-1}\) de modo que

\[
 q(x)=Q_k(\log q_1,\ldots,\log q_{k-1},x)
 \tag{10}
\]

sea un polinomio no nulo. Para cada primo \(p\) distinto de los fijados,

\[
 q(\log p)=a_{q_1\cdots q_{k-1}p}\ge0.
 \tag{11}
\]

Aunque a priori \(q\) tenga coeficientes complejos, (11) fuerza que su
parte imaginaria sea el polinomio nulo. Su coeficiente principal real es
positivo, o bien \(q\) es una constante positiva. Existen entonces
\(p_0\) y \(c_0>0\) tales que \(q(\log p)\ge c_0\) para todo primo
\(p\ge p_0\). Con \(C=q_1\cdots q_{k-1}\),

\[
 \sum_{n\ge2}{a_n\over n}
 \ge {c_0\over C}
      \sum_{\substack{p\ge p_0\\p\nmid C}}{1\over p}
 =\infty,
 \tag{12}
\]

contradiciendo (9). Luego \(\Phi_k=0\) para todo \(k\ge1\), y \(\Phi\)
es constante. \(\square\)

Esta prueba muestra por qué pasar de un polinomio a una serie de potencias
infinita no crea grados capaces de cancelarse entre sí: el soporte
*squarefree* de \(k\) primos proyecta exactamente el grado \(k\).

## 3. Prueba del Teorema B

Use el álgebra formal de Dirichlet

\[
 \mathscr D=\mathbb C[[x_p:p\text{ primo}]],
 \qquad x_p\longleftrightarrow p^{-s}.
 \tag{13}
\]

En ella

\[
 \mathcal L_j(\mathbf x)
 =\sum_p(\log p)^{j+1}\sum_{\nu\ge1}\nu^j x_p^\nu
 \tag{14}
\]

representa a \(\ell_j\). La unicidad de series de Dirichlet, aplicada a
la identidad \(Q(\ell)F=P(\ell)\), da la identidad formal

\[
 Q(\mathcal L)\,\mathcal F=P(\mathcal L)
 \quad\hbox{en }\mathscr D.
 \tag{15}
\]

Elija \(r+1\) primos distintos \(p_0,\ldots,p_r\) y anule todas las
variables restantes. Se obtiene una identidad en
\(\mathbb C[[x_{p_0},\ldots,x_{p_r}]]\). El jacobiano en el origen de
\(X_j=\mathcal L_j\) es

\[
 J_{j,i}=(\log p_i)^{j+1},
 \qquad
 \det J=\left(\prod_{i=0}^r\log p_i\right)
        \prod_{0\le i<k\le r}(\log p_k-\log p_i)\ne0.
 \tag{16}
\]

El teorema formal de la función inversa convierte entonces (15) en

\[
 Q(X)G(X)=P(X),
 \qquad G\in\mathbb C[[X_0,\ldots,X_r]].
 \tag{17}
\]

Es decir, \(P/Q\) es regular como germen formal en el origen. La
fiel planitud de
\(\mathbb C[[X]]\) sobre el anillo local
\(\mathbb C[X]_{(X)}\) da

\[
 Q\mathbb C[[X]]\cap\mathbb C[X]_{(X)}
 =Q\mathbb C[X]_{(X)}.
 \tag{18}
\]

Por (17), \(Q\) divide a \(P\) en el anillo local. Como \(P,Q\) se
tomaron coprimos, \(Q\) debe ser una unidad local, que equivale a
\(Q(0)\ne0\). Esto prueba el teorema. \(\square\)

Por ejemplo, el cociente aparentemente inocente \(\ell_1/\ell_0\) no
es una serie de Dirichlet ordinaria. En el eje real, si
\(a=\log2\), \(b=\log3\),

\[
 {\ell_1(s)\over\ell_0(s)}
 =a+{b(b-a)\over a}\left({2\over3}\right)^s
   +o\!\left((2/3)^s\right).
 \tag{19}
\]

La frecuencia \(\log(3/2)\) no es \(\log n\) para ningún entero
\(n\). Es la manifestación unidimensional de la obstrucción formal de
(16)--(18).

## 4. La salvedad de la abscisa y un contraejemplo exacto

Sea \(\sigma_c\) la abscisa de convergencia de la serie positiva (2).
Si \(\sigma_c\le1\) y la rama se prolonga holomórficamente a \(1\),
entonces

\[
 \sum_{n\ge2}{a_n\over n}<\infty.
 \tag{20}
\]

En efecto, si la suma diverge, \(F(\sigma)\uparrow\infty\) al bajar
\(\sigma\) a \(1\), incompatible con la holomorfía; si converge, (20)
es literal. El Teorema A vuelve a dar que \(\Phi\) es constante. Esto
prueba (4). Para una serie de Dirichlet no negativa no constante, Landau
afirma además que su abscisa finita \(\sigma_c\) es una singularidad
real.

La necesidad de controlar la abscisa se ve sin ningún cero. Para
\(c>0\), defina

\[
 F_c(s)={1\over c-\ell_0(s)}.
 \tag{21}
\]

En el semiplano donde \(\ell_0(\sigma)<c\),

\[
 F_c(s)=\sum_{k\ge0}{\ell_0(s)^k\over c^{k+1}},
 \tag{22}
\]

y todos sus coeficientes de Dirichlet son no negativos. Sin embargo,
\(\ell_0(\sigma)\) decrece estrictamente desde \(+\infty\) hasta \(0\)
cuando \(\sigma\) va de \(1^+\) a \(+\infty\). Existe un único
\(\sigma_c>1\) con \(\ell_0(\sigma_c)=c\), y (21) tiene allí un polo
real. A la vez,

\[
 \ell_0(s)={1\over s-1}-\gamma+O(s-1)
 \quad\Longrightarrow\quad
 F_c(s)=-(s-1)+O((s-1)^2),
 \tag{23}
\]

de modo que \(F_c\) es holomorfa —y se anula— en \(s=1\).

El ejemplo demuestra que la mera frase «coeficientes positivos y
holomorfía local en \(1\)» no basta. El precio exacto es el polo real
\(\sigma_c>1\). Además, cerca de un cero \(\rho\) de multiplicidad
\(m\), \(\ell_0(s)=-m/(s-\rho)+O(1)\), y por ello
\(F_c(s)=(s-\rho)/m+O((s-\rho)^2)\): este ejemplo borra, en vez de
retener, la singularidad del cero.

## 5. Decisión

```text
probado:
  rigidez para todo germen analítico de un jet finito de ell;
  aislamiento exacto de cada grado de Taylor por fibras squarefree;
  toda transformación racional con serie de Dirichlet ordinaria es
  automáticamente regular en el origen;
  dicotomía: constante si la serie positiva llega a 1, o ancla real
  artificial sigma_c>1 si el transformado es no constante;
  contraejemplo exacto que muestra por qué holomorfía solo local no basta.

no probado:
  una desigualdad global no local para los pesos Lambda reales;
  la energía subpolinomial de 104_93--104_94;
  Deep-Lambda, A1 o RH.
```

## Verificación mecánica

`tools/analytic_rational_landau_rigidity_check.py` verifica con aritmética
racional los determinantes de Vandermonde del cambio de coordenadas, la
recurrencia positiva de la expansión geométrica (22) y la identidad
formal \((c-L)F=1\) en truncaciones finitas. La existencia y unicidad del
polo real se prueban analíticamente por la monotonía estricta de
\(\ell_0(\sigma)\); no se delegan al programa. El programa no usa ceros
de \(\zeta\) ni coma flotante.
