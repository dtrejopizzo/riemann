# 104_95 — Cancelación del polo y rigidez de polinomios diferenciales positivos

## Resultado

Sea

\[
 \ell(s)=-{\zeta'(s)\over\zeta(s)},\qquad
 \delta=-{d\over ds},\qquad
 \ell_j=\delta^j\ell
 =\sum_{m\ge2}{\Lambda(m)(\log m)^j\over m^s}
 \quad(\Re s>1).
 \tag{1}
\]

El intento examinado consiste en fabricar un polinomio diferencial

\[
 F(s)=P(\ell_0(s),\ldots,\ell_r(s))
     =a_1+\sum_{m\ge2}{a_m\over m^s},
 \qquad P\in\mathbb R[X_0,\ldots,X_r],
 \tag{2}
\]

que cancele el polo real de \(\ell\), conserve \(a_m\ge0\) y mantenga
polos en los ceros de \(\zeta\). Entonces Landau convertiría un cero derecho
en una singularidad real. Esta clase natural queda descartada por una
rigidez más fuerte, anterior a cualquier información sobre los ceros.

> **Teorema 1 (rigidez *squarefree*).** Supóngase que los coeficientes de
> Dirichlet de (2) satisfacen
> \(a_m\ge0\) para todo \(m\ge2\). Si \(F\) es holomorfa en \(s=1\), entonces
> \(P\) es constante. En particular, ningún polinomio diferencial no
> constante de coeficientes constantes puede simultáneamente
> 
> 1. cancelar el polo en \(s=1\);
> 2. conservar coeficientes de Dirichlet no negativos;
> 3. retener una singularidad en un cero de \(\zeta\).

Esto incluye todos los polinomios en
\(\ell,-\ell',\ell'',\ldots\), porque son precisamente los polinomios en
los \(\ell_j\) tras cambiar signos fijos.

El teorema no prueba RH. Prueba que el cierre de Landau buscado no existe
en esta clase algebraica. No cubre transformaciones no polinómicas, shifts
del argumento ni operadores que no posean coeficientes de Dirichlet fijos.

---

## 1. El conflicto ya es completo en orden cuadrático

Ponga \(t=s-1\). La expansión

\[
 \ell(s)={1\over t}-\gamma+O(t)
 \tag{3}
\]

da

\[
 \ell'=-{1\over t^2}+O(1),\qquad
 \ell^2={1\over t^2}-{2\gamma\over t}+O(1).
 \tag{4}
\]

Por eso

\[
 -\ell'+\ell^2={\zeta''\over\zeta}
 =\sum_{m\ge1}{\Lambda(m)\log m+(\Lambda*\Lambda)(m)\over m^s}
 \tag{5}
\]

tiene coeficientes no negativos, pero conserva el doble polo
\(2t^{-2}\). El signo opuesto

\[
 \ell'+\ell^2
 \tag{6}
\]

cancela el doble polo, pero deja \(-2\gamma t^{-1}\), y su coeficiente en
un primo \(p\) es \(-\log^2p<0\).

Más generalmente, considere

\[
 F=A\ell'+B\ell^2+C\ell+D.
 \tag{7}
\]

Las condiciones de holomorfía en \(s=1\) son, sucesivamente,

\[
 -A+B=0,\qquad -2\gamma B+C=0.
 \tag{8}
\]

Así, salvo la constante \(D\), la única candidata es

\[
 \boxed{F=A\{\ell'+\ell^2+2\gamma\ell\}+D.}
 \tag{9}
\]

Su coeficiente en un primo es

\[
 a_p=A\log p\,(2\gamma-\log p).
 \tag{10}
\]

Las desigualdades elementales \(\frac12<\gamma<1\), \(\log2<1\) y
\(\log11>2\) muestran que el paréntesis es positivo para \(p=2\) y
negativo para \(p=11\). Si \(A>0\), (10) es negativo en \(11\); si
\(A<0\), es negativo en \(2\); y si \(A=0\), queda solamente una
constante.

La candidata (9) sí habría conservado los ceros: si \(\rho\) tiene
multiplicidad \(m\), entonces

\[
 \ell(s)=-{m\over s-\rho}+O(1),
 \qquad
 F(s)={A\,m(m+1)\over(s-\rho)^2}
       +O\!\left({1\over s-\rho}\right).
 \tag{11}
\]

Por tanto el fallo no es que la cancelación borre los ceros: es exactamente
la pérdida de positividad en los coeficientes primos.

---

## 2. Fibra *squarefree* de un grado homogéneo

Escriba

\[
 P=P_0+P_1+\cdots+P_d,
 \tag{12}
\]

donde \(P_k\) es homogéneo de grado \(k\). Para un monomio de grado \(k\)
el coeficiente de Dirichlet es una convolución de \(k\) copias de pesos
soportados en potencias primas.

Si \(n=p_1\cdots p_k\) es producto de \(k\) primos distintos, solamente
\(P_k\) puede contribuir a \(a_n\): menos de \(k\) factores no cubren los
\(k\) primos y más de \(k\) factores repetirían alguno de ellos.

Defina la aplicación de simetrización

\[
 \mathscr S_k(X_{j_1}\cdots X_{j_k})(x_1,\ldots,x_k)
 :=\sum_{\pi\in S_k}\prod_{i=1}^k x_i^{j_{\pi(i)}+1}.
 \tag{13}
\]

Entonces, exactamente,

\[
 \boxed{
 a_{p_1\cdots p_k}
 =(\mathscr S_kP_k)(\log p_1,\ldots,\log p_k).}
 \tag{14}
\]

La aplicación \(\mathscr S_k\) es inyectiva. En efecto, si el multiconjunto
\(\{j_1,\ldots,j_k\}\) tiene multiplicidades \(\alpha_j\), (13) es
\(\prod_j\alpha_j!\) veces el polinomio simétrico monomial asociado a la
partición \((j_1+1,\ldots,j_k+1)\). Particiones distintas dan una base
linealmente independiente.

---

## 3. Prueba del Teorema 1

La serie (2) converge absolutamente para \(\Re s>1\). Si \(F\) es
holomorfa en \(1\), entonces

\[
 \lim_{\sigma\downarrow1}\{F(\sigma)-a_1\}<\infty.
 \tag{15}
\]

Como \(a_m\ge0\), convergencia monótona aplicada a la serie de Dirichlet
implica

\[
 \sum_{m\ge2}{a_m\over m}<\infty.
 \tag{16}
\]

Suponga ahora que algún \(P_k\ne0\), \(k\ge1\), y ponga
\(Q=\mathscr S_kP_k\). Por la inyectividad anterior, \(Q\ne0\). El
producto cartesiano de cualquier conjunto infinito es Zariski-denso; en
particular se pueden fijar primos distintos
\(q_1,\ldots,q_{k-1}\) de modo que

\[
 q(x):=Q(\log q_1,\ldots,\log q_{k-1},x)
 \tag{17}
\]

sea un polinomio no nulo. Para todo primo \(p\) distinto de los anteriores,
(14) y la hipótesis de signo dan

\[
 q(\log p)=a_{q_1\cdots q_{k-1}p}\ge0.
 \tag{18}
\]

Un polinomio real no nulo que es no negativo sobre una sucesión no acotada
tiene coeficiente principal positivo (o es una constante positiva). Por
tanto existen \(p_0\) y \(c_0>0\) tales que
\(q(\log p)\ge c_0\) para todo primo \(p\ge p_0\). Si
\(C=q_1\cdots q_{k-1}\), resulta

\[
 \sum_m{a_m\over m}
 \ge {c_0\over C}\sum_{\substack{p\ge p_0\\p\nmid C}}{1\over p}
 =\infty,
 \tag{19}
\]

por la divergencia de la suma de los recíprocos de los primos. Esto
contradice (16). Luego \(P_k=0\) para todo \(k\ge1\), y \(P=P_0\) es
constante. \(\square\)

Obsérvese que (15)--(19) contienen el mecanismo de Landau en su forma más
elemental: una serie de Dirichlet no negativa no puede esconder en
\(s=1\) la masa divergente de una fibra de primos. No hizo falta suponer
ni negar RH.

---

## 4. Relación con los gates anteriores

- `104_13` trató la identidad particular
  \(-\ell'+\ell^2=\zeta''/\zeta\), su recurrencia Laguerre y su barrera de
  escala. El Teorema 1 es la extensión genuina: clasifica **todo** polinomio
  diferencial de coeficientes constantes antes de proyectarlo a Laguerre.
- `103_16` descartó positividad coeficiente a coeficiente después de la
  coordenada exponencial de \(\log\xi\) mediante Pringsheim. Aquí la
  variable permanece \(s\), los coeficientes son los de Dirichlet
  aritméticos y la rigidez viene de las fibras *squarefree*.

## 5. Decisión

```text
probado:
  la única combinación cuadrática que cancela todo el polo en s=1;
  su cambio de signo ya entre los coeficientes p=2 y p=11;
  rigidez para todo P(ell,delta ell,...,delta^r ell) de coeficientes constantes;
  imposibilidad de conservar simultáneamente polo cancelado, coeficientes
  no negativos y polos en ceros dentro de esa clase.

no cubierto:
  funciones no polinómicas de ell_j;
  shifts o dilataciones del argumento;
  operadores no locales sobre todas las torres primas.

no probado:
  Deep-Lambda, A1 o RH.
```

## Verificación mecánica

`tools/pole_cancellation_squarefree_rigidity_check.py` comprueba con
aritmética entera las ecuaciones polares de orden cuadrático y la
inyectividad diagonal de (13) para grados y órdenes finitos arbitrarios.
El script no usa valores de ceros ni coma flotante.
