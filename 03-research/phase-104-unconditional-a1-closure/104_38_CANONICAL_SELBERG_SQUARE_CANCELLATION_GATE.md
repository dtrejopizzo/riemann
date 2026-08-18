# 104_38 — Cancelación del cuadrado Selberg canónico y gate del cuadrado de Schur

**Estado.** Se intentó cerrar el determinante adyacente

\[
 \mathcal T_n=4H_nd_n-(H_n+d_n-H_{n+1})^2
 \tag{1}
\]

con la identidad exacta de Selberg para los pesos canónicos
\(\log p\), manteniendo juntos el término lineal, el término cuadrático,
el bloque arquimediano y las potencias primas superiores. El resultado es
un stop-gate algebraico más estrecho que el menor Hankel de `104_37`:

1. el único cuadrado \(\mu*\mu\) producido por Selberg se cancela
   **idénticamente** contra el cuadrado introducido por la inversión;
2. si, en vez de cancelarlo, se intenta usar ese cuadrado para pagar el
   término de Schur de (1), el núcleo residual tiene diagonal negativa en
   la cola para todo \(n\ge2\);
3. el testigo diagonal puede situarse en \(R=\log p\), con el peso
   canónico \(\log p\), para un primo real arbitrariamente grande.

Esto descarta una completación de cuadrados basada en la primera identidad
de Selberg, incluso después de incorporar exactamente el taper óptimo. No
refuta \(\mathcal T_n\ge0\) para la medida aritmética completa: una prueba
todavía podría usar una cancelación firmada especial entre los términos
lineal y cuadrático **en el valor canónico total**, pero ya no puede
obtenerla declarando positivo el resto cuadrático. No se prueba A1 ni RH.

## 1. Forma regulada con todos los bloques conservados

Fijemos \(a>1\). Usamos la notación de `104_35`:

\[
 d\alpha=\sum_p\log p\,\delta_{\log p},\qquad
 d\beta=e^u\,du,\qquad d\mu=d\alpha-d\beta,
 \tag{2}
\]

\[
 w_{n,a}(u)=ae^{-au}L_{n-1}^{(1)}(au),\qquad
 P_{n,a}=\langle w_{n,a},\beta-\alpha\rangle
        =-\langle w_{n,a},\mu\rangle .
 \tag{3}
\]

Sea la contribución convergente de las potencias superiores, con la misma
regularización,

\[
 C_{n,a}:=a\sum_p\sum_{k\ge2}{\log p\over p^{ka}}
              L_{n-1}^{(1)}(ka\log p).
\]

Entonces

\[
 B_{n,a}=C_{n,a}-P_{n,a},\qquad
 H_{n,a}=\kappa A_n-C_{n,a}+P_{n,a},
 \quad \kappa={1501\over2002}.
 \tag{4}
\]

Pongamos

\[
 d_{n,a}=\kappa\Delta A_n-B_{1,a},\qquad
 x_{n,a}=\Delta B_{n,a}-B_{1,a}.
 \tag{5}
\]

Para \(a\downarrow1\), se tiene

\[
 d_{n,a}\longrightarrow d_n=\kappa\Delta A_n+\gamma>0,
 \qquad
 x_{n,a}\longrightarrow H_n+d_n-H_{n+1}.
 \tag{6}
\]

La polarización exacta de `104_34` vale antes del límite:

\[
 \mathsf M_a[g_n+t\phi_n]
 =H_{n,a}-t x_{n,a}+t^2d_{n,a}.
 \tag{7}
\]

En particular, para \(a>1\) suficientemente cercano a uno,
\(d_{n,a}>0\) y

\[
 \min_t\mathsf M_a[g_n+t\phi_n]
 =H_{n,a}-{x_{n,a}^2\over4d_{n,a}}.
 \tag{8}
\]

No se ha omitido ninguna potencia superior: está toda en \(C_{n,a}\).
Tampoco se separó el polo: está acoplado a \(P_{n,a}\) mediante
\(\beta-\alpha\).

## 2. El funcional de la entrada cruzada

La identidad de Laguerre

\[
 L_n^{(1)}-L_{n-1}^{(1)}=L_n
 \tag{9}
\]

da

\[
 \ell_{n,a}(u)
 :=w_{n+1,a}(u)-w_{n,a}(u)-w_{1,a}(u)
 =ae^{-au}\{L_n(au)-1\}.
 \tag{10}
\]

Si

\[
 c_{n,a}:=\Delta C_{n,a}-C_{1,a},
 \tag{11}
\]

entonces (3)--(5) producen, sin estimación,

\[
 \boxed{x_{n,a}=c_{n,a}+\langle\ell_{n,a},\mu\rangle.}
 \tag{12}
\]

Así el cuadrado que hay que pagar en (8) es un cuadrado de un funcional
lineal de la medida centrada real, junto con el borde ordinariamente
convergente de las potencias superiores.

## 3. La cancelación exacta del cuadrado Selberg

Definamos

\[
 d\mathcal B_p=u\,d\mu+2\beta*\mu+\mu*\mu,
 \tag{13}
\]

y sea \(G_{n,a}\) la solución decreciente de

\[
 (\mathcal TG)(v)
 :=vG(v)+2\int_0^\infty G(v+u)\,d\beta(u)
 =w_{n,a}(v).
 \tag{14}
\]

La identidad (23) de `104_35` es

\[
 P_{n,a}=-\langle G_{n,a},\mathcal B_p\rangle
          +\mathcal Q_{G_{n,a}}(\mu),
 \qquad
 \mathcal Q_G(\mu)=\iint G(u+v)\,d\mu(u)d\mu(v).
 \tag{15}
\]

Aquí no queda un cuadrado positivo escondido. En efecto, al insertar
(13), Fubini da la identidad de formas

\[
\begin{aligned}
 -\langle G,\mathcal B_p\rangle+\mathcal Q_G(\mu)
 &=-\langle uG,\mu\rangle
   -2\langle G,\beta*\mu\rangle\\
 &=-\langle\mathcal TG,\mu\rangle.
\end{aligned}
 \tag{16}
\]

El sumando \(-\langle G,\mu*\mu\rangle\) de la primera línea se
cancela coeficiente por coeficiente con
\(+\mathcal Q_G(\mu)\). Para \(\mathcal TG=w_{n,a}\), (16) vuelve
exactamente a (3). La cancelación usa los pesos reales de (2), no una
envolvente ni una medida competidora.

Por tanto hay solo dos opciones contables:

* expandir (13), en cuyo caso el cuadrado Selberg desaparece y (8) vuelve
  al funcional lineal original menos el cuadrado de Schur;
* conservar \(\mathcal Q_G\), en cuyo caso hay que estudiar el núcleo
  cuadrático residual de la sección siguiente.

## 4. El núcleo residual tiene diagonal negativa

Insertando (12) y (15) en (8), y sin separar ningún bloque, obtenemos

\[
\begin{aligned}
 \min_t\mathsf M_a[g_n+t\phi_n]
={}&\kappa A_n-C_{n,a}
 -\langle G_{n,a},\mathcal B_p\rangle
 +\mathcal Q_{G_{n,a}}(\mu)\\
 &-{\{c_{n,a}+\langle\ell_{n,a},\mu\rangle\}^2
       \over4d_{n,a}}.
\end{aligned}
 \tag{17}
\]

Los dos términos cuadráticos que una completación intentaría comparar,
\(\mathcal Q_{G_{n,a}}(\mu)\) y el cuadrado de la entrada cruzada,
tienen como diferencia el kernel

\[
 \boxed{
 K_{n,a}(u,v)=G_{n,a}(u+v)
 -{\ell_{n,a}(u)\ell_{n,a}(v)\over4d_{n,a}}.}
 \tag{18}
\]

No es la parte cuadrática total de (17): al expandir
\(-\langle G,\mathcal B_p\rangle\), su término
\(-\langle G,\mu*\mu\rangle\) cancela \(\mathcal Q_G\), como prueba
(16). Precisamente por eso, conservar \(\mathcal Q_G\) como una supuesta
reserva exige que la diferencia (18) tenga signo, mientras el término
restante se controla sin volver a usar el mismo cuadrado. Esa diferencia
no es semidefinida positiva. Para \(n\ge2\), (10) da

\[
 \ell_{n,a}(R)
 ={(-1)^na^{n+1}\over n!}e^{-aR}R^n
   \{1+O_{n,a}(R^{-1})\}.                                  \tag{19}
\]

Por el Lema 5.1 de `104_37`, aplicado al test no tapered,

\[
 G_{n,a}(2R)
 ={(-1)^{n-1}a^n\over(n-1)!}
 e^{-2aR}(2R)^{n-2}\{1+O_{n,a}(R^{-1})\}.                  \tag{20}
\]

Como \(2n>n-2\), (18)--(20) implican

\[
 \boxed{
 K_{n,a}(R,R)
 =-{a^{2n+2}\over4d_{n,a}(n!)^2}
   e^{-2aR}R^{2n}\{1+O_{n,a}(R^{-1})\}<0}                 \tag{21}
\]

para todo \(R\) suficientemente grande. Esto es un testigo de **un solo
punto**, no el menor Hankel de dos puntos de `104_37`.

Hay primos arbitrariamente grandes. Por consiguiente puede elegirse un
primo real \(p\) con \(R=\log p\) dentro del rango de (21), y entonces

\[
 \mathcal Q_{K_{n,a}}
   ((\log p)\delta_{\log p})
 = (\log p)^2K_{n,a}(\log p,\log p)<0.                      \tag{22}
\]

El átomo de (22) está en el soporte primo verdadero y lleva exactamente
el peso canónico \(\log p\). Así ni siquiera el cuadrado residual exigido
por el Schur adyacente es una energía sobre las direcciones atómicas
canónicas.

## 5. Defecto de colisión: por qué el cuadrado de Schur no es Hankel

Existe una obstrucción local independiente de la cola. Todo kernel
producido por una convolución Selberg depende de \(u+v\). En cambio, el
kernel de rango uno que aparece en (18) no es Hankel. De (10),

\[
 \ell_{n,a}(0)=0,\qquad \ell_{n,a}'(0)=-na^2.               \tag{23}
\]

Tomando dos descomposiciones del mismo número \(5x\), resulta

\[
 \boxed{
 \lim_{x\downarrow0}{
 \ell_{n,a}(x)\ell_{n,a}(4x)
 -\ell_{n,a}(2x)\ell_{n,a}(3x)\over x^2}
 =-2n^2a^4<0.}                                             \tag{24}
\]

Si existiera una función \(J\) con
\(J(u+v)=\ell_{n,a}(u)\ell_{n,a}(v)\) en un entorno, los dos productos
de (24) serían idénticos. Por tanto el cuadrado escalar de la entrada
cruzada no puede identificarse con la convolución cuadrática de Selberg.
La diferencia no es una constante pequeña: ya aparece a orden \(x^2\)
con coeficiente explícito \(-2n^2a^4\).

## 6. Decisión

```text
probado incondicionalmente:
  forma regulada completa (7)--(8), con polo y potencias superiores;
  respuesta exacta de la entrada cruzada (10)--(12);
  cancelación identidad del término mu*mu de Selberg (16);
  kernel residual exacto (18);
  diagonal negativa (21) para todo n>=2;
  testigo de un átomo con soporte y peso primo canónicos (22);
  defecto de colisión cuantitativo (24).

descartado:
  usar el cuadrado Selberg como reserva positiva para pagar el Schur;
  representar exactamente el cuadrado de la entrada cruzada por un
  kernel de convolución/Hankel;
  cerrar T_n>=0 declarando PSD el resto cuadrático de (17).

permanece abierto:
  una desigualdad de valor para la medida canónica completa que conserve
  la cancelación entre la parte lineal de (17), su parte cuadrática
  indefinida, el bloque arquimediano y C_{n,a};
  T_n>=0 para todo n>=149, A1 y RH.
```

`tools/canonical_selberg_square_gate_check.py` verifica con `Fraction` la
cancelación (16) en medidas atómicas formales, la identidad (10), los
coeficientes principales de (19)--(21) y el coeficiente de colisión (24).
