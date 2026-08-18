# 104_53 — Teorema de cancelación conectada entre torres primas

**Resultado.** Toda identidad polinómica natural en los momentos que sea
aditiva respecto de sumas independientes es necesariamente una combinación
lineal de cumulantes. Para la ley zeta, cada cumulante es una suma sobre una
sola torre prima. Por consiguiente, cualquier elevación polinómica exacta
que recomponga aditivamente

\[
 B_n=A_n-\lambda_n
\]

a momentos conjuntos puede introducir pares o tuplas de torres distintas,
pero todos esos términos desconectados se cancelan al recomponer el
funcional logarítmico. El fenómeno observado en segundo orden en
`104_50`--`104_52` no es accidental: vale en todo orden cumulante de esta
jerarquía aditiva.

Esto no prueba

\[
 B_n\le {1501\over2002}A_n,\qquad n\ge150,                 \tag{1}
\]

ni A1 ni RH. Sí descarta como mecanismo autónomo toda *identidad polinómica
aditiva* de momentos multi-torre que espere conservar, después de la
recomposición, una reserva positiva formada por correlaciones entre primos
distintos. Un sucesor viable tendría que aplicar una desigualdad no aditiva
**antes** de la proyección conectada y demostrar que la reserva desconectada
que se descarta paga un margen proporcional para el test Laguerre fijo.

## 1. Álgebra universal de momentos

Sea

\[
 \mathcal H=\mathbb Q[m_1,m_2,\ldots],\qquad m_0=1,
\]

con coproducto

\[
 \boxed{
 \Delta m_r=\sum_{j=0}^r {r\choose j}m_j\otimes m_{r-j}.}  \tag{2}
\]

La ecuación (2) codifica exactamente los momentos de una suma de variables
independientes. Introduzcamos las series exponenciales

\[
 M(t)=1+\sum_{r\ge1}m_r{t^r\over r!},\qquad
 K(t)=\log M(t)=\sum_{r\ge1}\kappa_r{t^r\over r!}.          \tag{3}
\]

De (2),

\[
 \Delta M(t)=M(t)\otimes M(t),
\]

y por tanto

\[
 \boxed{
 \Delta K(t)=K(t)\otimes1+1\otimes K(t),\qquad
 \Delta\kappa_r=\kappa_r\otimes1+1\otimes\kappa_r.}       \tag{4}
\]

Los \(\kappa_r\) son los cumulantes universales.

## 2. Clasificación de observables polinómicos aditivos

**Teorema 2.1.** Sea \(P\in\mathcal H\) un polinomio que satisface

\[
 \Delta P=P\otimes1+1\otimes P.                            \tag{5}
\]

Entonces existen solo finitos escalares \(c_r\in\mathbb Q\) tales que

\[
 \boxed{P=\sum_r c_r\kappa_r.}                             \tag{6}
\]

Si además \(P\) es homogéneo de peso \(r\), con
\(\deg m_j=j\), entonces \(P=c\kappa_r\).

**Demostración.** El cambio triangular (3) es un automorfismo

\[
 \mathbb Q[m_1,m_2,\ldots]
 =\mathbb Q[\kappa_1,\kappa_2,\ldots].                     \tag{7}
\]

Escribamos \(P=Q(\kappa_1,\ldots,\kappa_R)\). Por (4), la condición
(5) es la identidad polinómica

\[
 Q(x_1+y_1,\ldots,x_R+y_R)=Q(x_1,\ldots,x_R)+Q(y_1,\ldots,y_R). \tag{8}
\]

Sobre un cuerpo de característica cero, un polinomio aditivo es lineal:
en efecto, sustituir \(y=x\) muestra que cada componente homogénea de
grado ordinario \(d\) satisface \(2^dQ_d=2Q_d\), y por ello se anula si
\(d\ne1\). Esto prueba (6). La última afirmación sigue de los pesos.
\(\square\)

La misma prueba vale sobre cualquier cuerpo de característica cero. En la
aplicación siguiente se puede fijar \(s>1\), o extender escalares de
\(\mathbb Q\) a \(\mathbb Q(s)\); por tanto los coeficientes racionales en
\(s\) de (15) no quedan fuera del teorema.

## 3. Aplicación exacta a la ley zeta

Fijemos \(s=1+\varepsilon>1\) y

\[
 \mathbb P_s(N=m)={m^{-s}\over\zeta(s)},\qquad X=\log N.   \tag{9}
\]

Su función generatriz de momentos es

\[
 \mathbb E_se^{tX}={\zeta(s-t)\over\zeta(s)}.              \tag{10}
\]

Como los exponentes primos son geométricos independientes, (3) y el
producto de Euler dan, para cada \(r\ge1\),

\[
\boxed{
 \kappa_r(s)
 =\sum_p(\log p)^r\sum_{k\ge1}k^{r-1}p^{-ks}
 =\sum_{m\ge2}{\Lambda(m)(\log m)^{r-1}\over m^s}.}        \tag{11}
\]

No queda en (11) ninguna tupla de primos distintos. En cambio los momentos
\(m_r(s)=\mathbb E_sX^r\) contienen todos los productos de cumulantes. El
Teorema 2.1 prueba que esos productos deben cancelarse en cualquier
observable aditivo exacto.

El comparador polar \(X_0\sim\mathrm{Exp}(\varepsilon)\) tiene

\[
 \kappa_r^{(0)}=(r-1)!\varepsilon^{-r}.                    \tag{12}
\]

Con

\[
 R(q)=-{\zeta'\over\zeta}(1+q)-{1\over q},                 \tag{13}
\]

se obtiene

\[
 \boxed{
 \kappa_r(1+\varepsilon)-\kappa_r^{(0)}
 =(-1)^{r-1}R^{(r-1)}(\varepsilon).}                       \tag{14}
\]

Finalmente, para

\[
 P_n(x)=L_{n-1}^{(1)}(x),\qquad
 c_{n,r}(s)=(-1)^{r-1}{n\choose r}{s^{r-1}\over(r-1)!},   \tag{15}
\]

la recomposición Laguerre es

\[
 \boxed{
 {\mathcal B_{n,s}\over s}
 =\sum_{r=1}^n c_{n,r}(s)
 \{\kappa_r(s)-(r-1)!\varepsilon^{-r}\},
 \qquad \mathcal B_{n,s}\longrightarrow B_n.}            \tag{16}
\]

Así, toda elevación exacta polinómica que conserve la aditividad y represente
este mismo funcional vuelve a la combinación de cumulantes (16). Una forma
cuadrática no aditiva puede retener términos multi-torre y queda fuera del
Teorema 2.1. En la construcción PSD concreta de `104_50`, su parte
desconectada es una energía o varianza que pierde la orientación del margen;
no se afirma que toda forma cuadrática imaginable tenga esa estructura o
carezca de un signo útil.

## 4. Alcance del no-go

El teorema descarta el esquema

```text
introducir momentos conjuntos de varias torres
+ recomponer exactamente un observable aditivo
=> conservar una reserva cruzada positiva.
```

No descarta una desigualdad genuina que use, antes de recomponer:

1. la marca unitaria uniforme de `104_49`;
2. una reserva no aditiva entre varias torres;
3. un signo específico del vector Laguerre;
4. una estimación que falle para el selector desplazado (39) de `104_49`.

Pero esa desigualdad no puede ser una identidad cumulante disfrazada. Debe
probar que una parte concreta de los momentos desconectados domina, con el
signo correcto, el observable conectado (16). Ése es contenido aritmético
nuevo de fuerza RH, no una consecuencia formal de la renovación.

La misma advertencia se aplica al falsificador
\(Z_c(s)=\zeta(s+c)\zeta(s-c)\): también es un producto de campos
geométricos independientes en su semiplano de Euler, y toda identidad
universal de cumulantes vuelve a linealizar sus factores. Por tanto un
mecanismo que solo use (2)--(6) no distingue la línea crítica.

## 5. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 connected_cumulant_cancellation_check.py
```

El checker usa `Fraction`. Verifica exactamente la convolución de momentos,
la aditividad de los cumulantes hasta orden doce y la cancelación de todos
los términos cruzados en órdenes bajos. Es una verificación de las
identidades, no un sustituto de la prueba algebraica del Teorema 2.1.
