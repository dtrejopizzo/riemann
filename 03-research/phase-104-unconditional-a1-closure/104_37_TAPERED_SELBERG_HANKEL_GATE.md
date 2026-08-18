# 104_37 — Taper adyacente, inversión Selberg y gate Hankel de dos puntos

**Estado.** Se aplicó la inversión colectiva de Selberg de `104_35` al
vector tapered exacto de `104_34`, incluido el valor óptimo \(t_n^*\). El
test de Laguerre regulado se cierra en una fórmula de un solo polinomio:

\[
 w_{n,t,a}(u)=ae^{-au}
 \{L_{n-1}^{(1)}(au)+tL_n(au)+t(t-1)\}.
 \tag{1}
\]

La inversión se hace antes de tomar signos. Sin embargo, el taper no
convierte la forma de Hankel resultante en una energía coerciva. Para
**todo** \(t\in\mathbb R\), incluido \(t=t_n^*\), una compresión de dos
puntos tiene determinante principal estrictamente negativo en la cola. El
coeficiente principal es \(8^d-9^d<0\), con \(d\ge147\) en el rango de la
fase. El mismo testigo puede colocarse en logaritmos de primos verdaderos.

Esto descarta exactamente el cierre de la compresión adyacente por
positividad Hankel después de la inversión Selberg. No refuta
\(\mathcal T_n\ge0\) para los pesos canónicos \(\log p\): una prueba de ese
enunciado todavía tendría que usar una cancelación firmada especial entre
el término lineal de Selberg, su término cuadrático, el bloque
arquimediano y la corrección de potencias superiores. Por tanto este
documento no prueba A1 ni RH.

## 1. Prerregistro y alcance

Sea

\[
 c={501\over2002},\qquad \kappa=1-c={1501\over2002},
 \qquad H_n=\lambda_n-cA_n,
 \tag{2}
\]

y

\[
 d_n=\kappa\Delta A_n+\gamma,
 \qquad
 \mathcal T_n=4H_nd_n-(H_n+d_n-H_{n+1})^2.
 \tag{3}
\]

El frente de `104_34` es probar \(\mathcal T_n\ge0\) para todo
\(n\ge149\). La única idea ensayada aquí es:

1. escribir exactamente la forma sobre
   \(h_{n,t}=g_n+t\phi_n\);
2. retirar ordinariamente las potencias \(p^k,\ k\ge2\), como en `104_32`;
3. invertir colectivamente la identidad de Selberg de primos simples;
4. intentar obtener el signo en \(t=t_n^*\) de una energía Hankel.

No se usa una cota de valor absoluto, una localización de ceros ni un
resultado condicional. El falsificador off-line de `104_34` sigue siendo
vinculante: un mecanismo que probara \(\mathcal T_n\ge0\) usando solo
simetría funcional tendría que fallar frente a aquel cuarteto. El testigo
de la Sección 5 es más específico: mata la positividad Hankel aun sobre el
soporte de primos reales, sin afirmar que altera los pesos canónicos.

## 2. Forma tapered exacta

Recordemos

\[
 g_n=e^{-x/2}L_{n-1}^{(1)}(x),\qquad
 \phi_n=e^{-x/2}L_n(x),\qquad g_{n+1}=g_n+\phi_n.
 \tag{4}
\]

Para cualquier sucesión \(X_0=0,X_1,X_2,\ldots\), su polarización Toeplitz
sobre el plano \(\mathrm{span}\,\{g_n,\phi_n\}\) da

\[
 \boxed{
 X_{n,t}:=X_n+t(X_{n+1}-X_n-X_1)+t^2X_1.}
 \tag{5}
\]

En efecto, la entrada cruzada es
\((X_{n+1}-X_n-X_1)/2\). Póngase

\[
 P_n:=B_n^{(p+\mathrm{pole})},\qquad
 C_n:=P_{n-1}^{(\ge2)}(1)\quad(n\ge1),qquad P_0=C_0=0.
 \tag{6}
\]

La identidad (24) de `104_32` implica

\[
 B_n=A_n-\lambda_n=C_n-P_n.                                 \tag{7}
\]

Por tanto, sin límite informal ni término omitido,

\[
 \mathsf Q_0[h_{n,t}]=C_{n,t}-P_{n,t}.                       \tag{8}
\]

La ortogonalidad de bandera de `104_34` da a su vez

\[
 \mathsf A_{\rm flag}[h_{n,t}]=A_n+t^2\Delta A_n,             \tag{9}
\]

y la forma de margen es

\[
 \boxed{
 \mathsf M[h_{n,t}]
 =\kappa(A_n+t^2\Delta A_n)-C_{n,t}+P_{n,t}.}
 \tag{10}
\]

Al recomponer (7), (10) es exactamente

\[
 \mathsf M[h_{n,t}]
 =H_n-t(H_n+d_n-H_{n+1})+t^2d_n.                            \tag{11}
\]

En particular,

\[
 t_n^*={H_n+d_n-H_{n+1}\over2d_n},\qquad
 \boxed{\mathsf M[h_{n,t_n^*}]={\mathcal T_n\over4d_n}.}     \tag{12}
\]

Así el taper no aproxima el determinante de Schur: lo evalúa exactamente.

## 3. Test Laguerre de primos simples

Con las medidas de `104_35`,

\[
 d\alpha=\sum_p\log p\,\delta_{\log p},\qquad
 d\beta=e^u\,du,\qquad d\mu=d\alpha-d\beta,                 \tag{13}
\]

sea, para \(a>1\),

\[
 w_{n,a}(u)=ae^{-au}L_{n-1}^{(1)}(au),\qquad
 P_{n,a}=\langle w_{n,a},\beta-\alpha\rangle.                \tag{14}
\]

Aplicando (5) antes de retirar el regulador,

\[
 w_{n,t,a}
 =w_{n,a}+t(w_{n+1,a}-w_{n,a}-w_{1,a})+t^2w_{1,a}.           \tag{15}
\]

La identidad
\(L_n^{(1)}-L_{n-1}^{(1)}=L_n\) convierte (15) en la fórmula
(1), y por tanto

\[
 \boxed{
 P_{n,t,a}=\langle w_{n,t,a},\beta-\alpha\rangle,
 \qquad P_{n,t}=\lim_{a\downarrow1}P_{n,t,a}.}               \tag{16}
\]

Obsérvese el término \(t(t-1)\). Omitirlo equivaldría a olvidar la entrada
diagonal de \(\phi_n\) o el término \(-X_1\) de la polarización cruzada.

## 4. Inversión colectiva antes del signo

Definamos, como en `104_35`,

\[
 (\mathcal Tg)(v)=vg(v)+2e^{-v}\int_v^\infty e^ug(u)\,du,
 \qquad
 \mathcal Q_g(\nu)=\iint g(u+v)\,d\nu(u)d\nu(v),             \tag{17}
\]

y

\[
 d\mathcal B_p=u\,d\mu+2\beta*\mu+\mu*\mu.                 \tag{18}
\]

La solución decreciente de
\(\mathcal TG_{n,t,a}=w_{n,t,a}\) es

\[
 \boxed{
 G_{n,t,a}(v)={1\over v}\left[w_{n,t,a}(v)
 -2v^2e^{-v}\int_v^\infty{e^uw_{n,t,a}(u)\over u^3}\,du
 \right].}                                                  \tag{19}
\]

Primero se usa (18), y solo después se examina el signo. Esto da la
identidad completamente acoplada

\[
 \boxed{
 P_{n,t,a}
 =-\langle G_{n,t,a},\mathcal B_p\rangle
   +\mathcal Q_{G_{n,t,a}}(\mu).}                            \tag{20}
\]

Al insertar (20) en (10) no se ha separado ningún primo ni el polo:

\[
 \mathsf M[h_{n,t}]
 =\kappa(A_n+t^2\Delta A_n)-C_{n,t}
  +\lim_{a\downarrow1}
   \{-\langle G_{n,t,a},\mathcal B_p\rangle
       +\mathcal Q_{G_{n,t,a}}(\mu)\}.                      \tag{21}
\]

La pregunta precisa es si el valor \(t=t_n^*\) convierte el último término
en una energía con cota inferior proporcional. La respuesta para la
positividad Hankel es no, uniformemente en \(t\).

## 5. Testigo Hankel cuantitativo de dos puntos

Usaremos un hecho elemental que evita decidir el signo puntual de
\(G_{n,t,a}\).

**Lema 5.1.** Sea
\(w(v)=ae^{-av}P(av)\), \(a>1\), donde \(P\) es un polinomio real de grado
\(D\ge2\) y coeficiente principal \(p_D\ne0\). Si \(G\) es (19), entonces,
con \(d=D-1\) y \(C=p_Da^{D+1}\),

\[
 G(v)=Ce^{-av}v^d\{1+O_{P,a}(v^{-1})\}.                     \tag{22}
\]

En consecuencia,

\[
 \boxed{
 \begin{aligned}
 &G(2R)G(4R)-G(3R)^2\\
 &\quad=C^2e^{-6aR}R^{2d}
       \{8^d-9^d+O_{P,a}(R^{-1})\}<0
 \end{aligned}}                                             \tag{23}
\]

para todo \(R\) suficientemente grande.

**Prueba.** El primer sumando de (19) es
\(Ce^{-av}v^{D-1}\{1+O(v^{-1})\}\). Como \(a-1>0\), integración por
partes en el segundo sumando muestra que éste es
\(O(e^{-av}v^{D-2})\). Esto prueba (22). Sustituir \(2R,3R,4R\) produce
(23), y \(8^d-9^d<0\) para \(d\ge1\). \(\square\)

Para (1), el grado y el coeficiente son

\[
 \begin{array}{c|c|c|c}
 &D&d&C\\ \hline
 t\ne0&n&n-1&t(-1)^n a^{n+1}/n!\\
 t=0&n-1&n-2&(-1)^{n-1}a^n/(n-1)!.
 \end{array}                                                \tag{24}
\]

Por tanto (23) vale para todo \(n\ge3\) y **todo** \(t\in\mathbb R\).
En particular vale para el número aritmético \(t_n^*\), sea éste cero o
no. En el rango \(n\ge149\), el exponente satisface \(d\ge147\).

El determinante (23) es el menor principal de la matriz Hankel

\[
 \begin{pmatrix}G(2R)&G(3R)\\G(3R)&G(4R)\end{pmatrix}.       \tag{25}
\]

Luego la forma \(\mathcal Q_G\) es indefinida en medidas soportadas en
\(\{R,2R\}\). Esto no es la observación anterior de que \(G\) cambia de
signo: incluso si ambas entradas diagonales de (25) son positivas, el
determinante negativo produce una dirección estrictamente negativa.

El testigo puede vivir en el soporte primo real. Sean \(p\to\infty\)
primos y, por Bertrand, elíjase un primo \(q\) con
\(p^2<q<2p^2\). Si \(R=\log p\), \(S=\log q\), entonces
\(S/R\to2\), y (22) da

\[
 \begin{aligned}
 &G(2R)G(2S)-G(R+S)^2\\
 &\quad=C^2e^{-2a(R+S)}R^{2d}
 \left\{\left(4{S\over R}\right)^d
 -\left(1+{S\over R}\right)^{2d}+O(R^{-1})\right\}<0.      \tag{26}
 \end{aligned}
\]

La desigualdad principal es estricta porque
\((R+S)^2-4RS=(R-S)^2>0\). Así la restricción del kernel a
\(\{\log p:\ p\text{ primo}\}\) tampoco es semidefinida positiva.

## 6. Decisión y frente restante

La identidad (21) muestra exactamente qué ocurre. La positividad de la
medida no centrada de Selberg no convierte por sí sola
\(\mathcal Q_{G_{n,t,a}}\) en una energía. El taper óptimo aumenta en
general el grado de la cola de \(n-2\) a \(n-1\), pero no cambia el menor
negativo (23). El bloque arquimediano y \(C_{n,t}\) son escalares fijos y
no reparan una afirmación de semidefinitud del kernel.

No se concluye que (21) sea negativo para la medida aritmética real. En
esa medida, los términos lineal y cuadrático de (20) pueden cancelarse de
manera especial; de hecho, esa cancelación es lo único que todavía podría
probar \(\mathcal T_n\ge0\). Lo descartado es inferirla de una coercividad
Hankel producida por Selberg, incluso después de optimizar el taper.

```text
probado incondicionalmente:
  forma tapered exacta de bandera (10)--(12);
  test Laguerre simple-prime exacto (1), incluido t(t-1);
  inversión colectiva (19)--(21) antes de tomar signos;
  menor Hankel negativo con término principal 8^d-9^d;
  el mismo gate restringido a logaritmos de primos verdaderos;
  cobertura de todo t, incluido t_n^* y el caso t_n^*=0.

descartado:
  cerrar el Schur adyacente por positividad/PSD del kernel Selberg tapered;
  atribuir al taper una energía Hankel ausente en el vector original.

permanece abierto:
  una cota firmada conjunta que use los pesos exactos log p en ambos
  términos de (20), junto con C_{n,t} y el bloque arquimediano;
  T_n >= 0 para todo n >= 149, A1 y RH.
```

`tools/tapered_selberg_hankel_gate_check.py` verifica con `Fraction` la
identidad polinómica (1), los coeficientes principales de (24) y el menor
modelo \(8^d-9^d<0\), sin decisiones de signo en coma flotante.
