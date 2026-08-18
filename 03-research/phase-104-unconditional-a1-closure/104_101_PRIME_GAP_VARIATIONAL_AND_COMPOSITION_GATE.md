# 104_101 — Coordenada exacta de gaps, convexidad y gate de composición

## Resultado

Ponga

\[
 L(x)=\int_2^x{dt\over\log t},\qquad
 \mathcal E_\pi(N)=\sum_{m=2}^N
 {\{\pi(m)-L(m)\}^2\over m(m+1)}.
 \tag{1}
\]

Si \(p_k\) es el \(k\)-ésimo primo y
\(g_k=p_{k+1}-p_k\), defina

\[
 c_k=k-L(p_k),\qquad
 \ell_{k,r}=L(p_k+r)-L(p_k)\quad(0\le r\le g_k).
 \tag{2}
\]

Entonces, con

\[
 R_k(N)=\min\{g_k-1,N-p_k\},
 \tag{3}
\]

se tiene la identidad finita exacta

\[
 \boxed{
 \mathcal E_\pi(N)=
 \sum_{p_k\le N}\sum_{r=0}^{R_k(N)}
 {\{c_k-\ell_{k,r}\}^2
  \over(p_k+r)(p_k+r+1)}.}
 \tag{4}
\]

Los valores en los extremos satisfacen la recurrencia

\[
 \boxed{c_{k+1}=c_k+1-\ell_{k,g_k}.}
 \tag{5}
\]

En una celda completa, ponga

\[
 w_{k,r}={1\over(p_k+r)(p_k+r+1)},\quad
 W_k=\sum_{r=0}^{g_k-1}w_{k,r}
 ={1\over p_k}-{1\over p_{k+1}},
 \tag{6}
\]

\[
 \bar\ell_k={1\over W_k}\sum_{r=0}^{g_k-1}w_{k,r}\ell_{k,r},\qquad
 V_k=\sum_{r=0}^{g_k-1}w_{k,r}
       (\ell_{k,r}-\bar\ell_k)^2.
 \tag{7}
\]

La contribución de la celda es

\[
 \boxed{
 \mathcal E_k=W_k(c_k-\bar\ell_k)^2+V_k.}
 \tag{8}
\]

Esta es la forma variacional exacta. Es estrictamente convexa en
\(c_k\), pero la convexidad produce un **mínimo**, no una cota superior.
El término que falta controlar es el error acumulado \(c_k\), y (5)
muestra que eso exige cancelación entre los sesgos de muchos gaps.

La condición «los no-primos son compuestos» no suministra esa
cancelación mediante una relajación convexa. Hay una dicotomía exacta:

* imponer simultáneamente «todo seleccionado es primo» y «todo omitido
  es compuesto» deja un conjunto factible de un solo punto, la sucesión
  prima literal;
* la relajación natural que conserva cualquier rueda fija, densidad PNT
  y gaps logarítmicos admite sucesiones \(0\)-\(1\) con energía
  polinomial.

Más precisamente, para todo entero fijo \(W\ge2\), todo
\(1/2<\beta<1\) y todo \(c>0\), existe una sucesión
\(a_n\in\{0,1\}\) tal que, escribiendo

\[
 A(x)=\sum_{n\le x}a_n,\qquad
 S(x)=\sum_{2\le n\le x}{1\over\log n},
 \tag{9}
\]

se cumplen

\[
 a_n=1\Longrightarrow(n,W)=1,\qquad
 A(x)=S(x)+cx^\beta+O_{W,\beta,c}(1),
 \tag{10}
\]

y los gaps consecutivos del soporte son \(O_{W,\beta,c}(\log x)\).
Sin embargo,

\[
 \boxed{
 \sum_{m\le N}{\{A(m)-S(m)\}^2\over m(m+1)}
 ={c^2\over2\beta-1}N^{2\beta-1}+O_{W,\beta,c}(1).}
 \tag{11}
\]

Como \(S(x)-L(x)\) es acotada, (11) vale también con \(L\). Además,
\(x^\beta=o(xe^{-C(\log x)^{3/5}(\log\log x)^{-1/5}})\); por tanto el
modelo satisface PNT y cualquier envelope ordinario de tipo
Vinogradov--Korobov, pese a violar el blanco \(N^{o(1)}\).

**Veredicto.** Reescribir la energía en gaps es exacto y útil: localiza
el obstáculo en el paseo acumulado (5). Pero convexidad celular junto con
una rueda fija, PNT/VK y hasta gaps \(O(\log x)\) no fuerza energía
subpolinomial. `104_99` cubre por separado las cribas estables de nivel
\(x^{1-\eta}\). La composición completa no da una nueva región
variacional: identifica ya la sucesión prima y devuelve exactamente el
problema original. Esto no es un no-go universal para toda desigualdad
específica de los primos. Este documento no prueba (1) acotada,
Deep-\(\Lambda\), A1 ni RH.

---

## 1. Derivación de la identidad de gaps

Si \(p_k\le m<p_{k+1}\), entonces \(\pi(m)=k\). Escribiendo
\(m=p_k+r\),

\[
 \pi(m)-L(m)
 =k-L(p_k)-\{L(p_k+r)-L(p_k)\}
 =c_k-\ell_{k,r}.
 \tag{12}
\]

Las celdas \([p_k,p_{k+1}-1]\) particionan los enteros \(m\ge2\).
Truncarlas en \(N\) prueba (4). En el siguiente extremo,

\[
 c_{k+1}
 =k+1-L(p_{k+1})
 =c_k+1-\{L(p_{k+1})-L(p_k)\},
 \tag{13}
\]

que es (5).

La suma de los pesos telescopa:

\[
 W_k=\sum_{m=p_k}^{p_{k+1}-1}
 \left({1\over m}-{1\over m+1}\right)
 ={1\over p_k}-{1\over p_{k+1}}.
 \tag{14}
\]

Finalmente, expandir alrededor de la media ponderada da

\[
 \sum_rw_{k,r}(c_k-\ell_{k,r})^2
 =W_k(c_k-\bar\ell_k)^2
  +\sum_rw_{k,r}(\ell_{k,r}-\bar\ell_k)^2,
 \tag{15}
\]

porque el término cruzado es cero. Esto prueba (8).

Existe una versión completamente discreta, más cercana a `104_93`.
Ponga

\[
 d_k=k-S(p_k),\qquad
 h_{k,r}=\sum_{j=1}^r{1\over\log(p_k+j)}.
 \tag{16}
\]

Entonces (4)--(8) valen reemplazando \((c,\ell)\) por \((d,h)\), y

\[
 d_{k+1}=d_k+1-h_{k,g_k}.
 \tag{17}
\]

En particular \(1-h_{k,g_k}\) es el gap normalizado y centrado; el
endpoint \(d_k\) es su suma acumulada, no una función convexa de un solo
gap.

## 2. Lo que la convexidad sí dice

Para \(p_k,p_{k+1}\) fijos, (8) alcanza su mínimo en
\(c_k=\bar\ell_k\), y el mínimo es \(V_k\ge0\). Por consiguiente

\[
 \mathcal E_k\ge V_k.
 \tag{18}
\]

La dirección es opuesta a la necesaria. Una cota superior requiere
controlar \(|c_k-\bar\ell_k|\). Por (5), eso equivale a controlar

\[
 c_1+\sum_{i<k}\{1-\ell_{i,g_i}\}.
 \tag{19}
\]

Saber que todos los enteros interiores de la celda poseen un divisor no
impone signo a (19), ni empareja los sesgos de celdas distintas. La
inclusión--exclusión que conserva todos esos divisores es precisamente la
identidad completa de Eratóstenes de `104_99`; truncarla pierde la
información de paridad, y no aparece una desigualdad convexa adicional.

## 3. Falsificador \(0\)-\(1\) con rueda y gaps logarítmicos

Fije \(W,\beta,c\) como arriba y defina

\[
 F(m)=S(m)+cm^\beta.
 \tag{20}
\]

Enumere, desde un punto suficientemente grande, los enteros coprimos con
\(W\):

\[
 r_1<r_2<\cdots,\qquad(r_j,W)=1.
 \tag{21}
\]

Se tiene \(r_{j+1}-r_j\le W\). Además,

\[
 F(r_{j+1})-F(r_j)
 \le {W\over\log(r_j+1)}+c\beta W r_j^{\beta-1}=o(1).
 \tag{22}
\]

Tras aumentar el punto inicial, (22) es menor que uno. Defina

\[
 a_{r_j}=\lfloor F(r_j)\rfloor-\lfloor F(r_{j-1})\rfloor,\qquad
 a_n=0\quad(n\notin\{r_j\}).
 \tag{23}
\]

Entonces \(a_n\in\{0,1\}\). Si \(r(x)\) es el mayor candidato no mayor
que \(x\), telescopar (23) da

\[
 A(x)=\lfloor F(r(x))\rfloor+C.
 \tag{24}
\]

Como \(0\le x-r(x)<W\), (22) y (24) prueban (10). Para ver el tamaño de
los gaps del soporte, tome \(y=x+3\log x+W\). Para \(x\) grande,

\[
 F(y-W)-F(x)
 \ge {y-W-x\over\log y}>2.
 \tag{25}
\]

Hay un candidato entre \(y-W\) e \(y\); por (23), el piso debe saltar
antes de \(y\). Así todo gap del soporte que empieza cerca de \(x\) es
\(O(\log x)\).

De (10),

\[
 A(m)-S(m)=cm^\beta+O(1).
 \tag{26}
\]

Como \(1/2<\beta<1\), los términos cruzados son sumables y

\[
\begin{aligned}
 \sum_{m\le N}{\{A(m)-S(m)\}^2\over m(m+1)}
 &=c^2\sum_{m\le N}m^{2\beta-2}+O(1)\\
 &={c^2\over2\beta-1}N^{2\beta-1}+O(1),
\end{aligned}
\tag{27}
\]

que prueba (11).

Este falsificador no pretende que sus puntos sean primos: prueba
exactamente que toda relajación que solo ve una rueda finita, densidad y
gaps está demasiado abierta.

## 4. Por qué la composición completa no deja variaciones

Para \(n\ge2\), sea \(q_n=\mathbf1_{\mathbb P}(n)\). La factorización
elemental da

\[
 \boxed{
 q_n=\prod_{p\le\sqrt n}(1-\mathbf1_{p\mid n}).}
 \tag{28}
\]

Sea \(a_n\in\{0,1\}\). Las dos implicaciones exactas son

\[
 a_n=1\Longrightarrow q_n=1 \quad(a_n\le q_n),
 \qquad
 a_n=0\Longrightarrow q_n=0 \quad(a_n\ge q_n).
 \tag{29}
\]

Imponer ambas da \(a_n=q_n\) coordenada por coordenada. El politopo
factible es el singleton \(\{q\}\); por tanto no existe una comparación
variacional con otra configuración que conserve la composición exacta.
Evaluar una desigualdad no trivial en ese singleton es ya estimar la
sucesión prima literal.

Cada mitad de (29), incluso acompañada por PNT, es insuficiente. Esto se
ve sin modelos probabilísticos:

* añada a todos los primos una subsucesión de enteros pares compuestos
  cuya función de conteo sea
  \(C(x)\sim x/\log^2x\). Entonces todo entero omitido es compuesto y
  \(A^+(x)-L(x)\sim x/\log^2x\);
* borre los primos de índices
  \(k_j=\lfloor j\log j\rfloor\). La cantidad borrada hasta \(x\) es
  \(D(x)\sim\pi(x)/\log\pi(x)\sim x/\log^2x\). Entonces todo punto
  seleccionado es primo y
  \(A^-(x)-L(x)\sim-x/\log^2x\).

En ambos casos la PNT sigue válida, pero

\[
 \sum_{m\le N}{\{A^\pm(m)-L(m)\}^2\over m(m+1)}
 \sim {N\over\log^4N},
 \tag{30}
\]

que no es \(N^{o(1)}\). Para el primer caso puede elegirse el punto par
\(2j\) cada vez que el piso de \(2j/\log^2(2j)\) aumenta; esto da
\(C(x)=x/\log^2x+O(1)\). La inversión elemental de
\(j\log j\) prueba la asintótica del segundo caso. La PNT con región
libre de ceros hace \(\pi(x)-L(x)=o(x/\log^A x)\) para todo \(A\), de
modo que no puede cancelar los términos añadidos.

## 5. Auditoría de no duplicación

`104_93` prueba la identidad max para los incrementos
\((\Lambda(n)-1)/\log n\) y la equivalencia energética con RH.
`104_94` elimina las potencias primas propias. `104_99` conserva la
inclusión--exclusión completa y prueba el no-go de nivel
\(x^{1-\eta}\) mediante las sucesiones \(1\pm\lambda_L\).

El contenido adicional de este documento es distinto y más estrecho:

1. la identidad celular exacta (4)--(5) en gaps consecutivos;
2. la completación cuadrática (8), que decide la dirección de la
   convexidad;
3. el falsificador **\(0\)-\(1\)** (10)--(11), con rueda arbitraria fija,
   PNT/VK y gaps \(O(\log x)\);
4. la dicotomía singleton (28)--(29) y los falsificadores PNT de cada
   relajación unilateral.

No se reclama como nuevo el hecho general de que una criba incompleta no
caracteriza a los primos, ni la barrera de paridad. El resultado nuevo
dentro de la fase es ubicar exactamente por qué la convexidad en gaps no
da la cota de `104_93`.

## 6. Reproducción

Desde `tools/`:

```bash
python3 prime_gap_energy_variational_check.py
```

El checker verifica numéricamente, hasta \(N=200000\), (4), (8) y el
telescopado (6). Después construye el modelo (23) con
\(W=30\), \(\beta=3/4\), verifica soporte, tracking acotado y gaps
logarítmicos hasta \(10^6\). La prueba asintótica es (20)--(27), no una
inferencia del rango finito.
