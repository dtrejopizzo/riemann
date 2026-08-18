# 104_35 — Canal primos simples--polo y gate Selberg colectivo

**Estado.** La reducción de `104_32` admite una representación exacta en
términos de \(\theta(x)-x\), con el borde \(-n\) conservado. Esto localiza
la obligación cuártica exclusivamente en los primos simples:

\[
 B_n^{(p+\mathrm{pole})}
 =-n-\int_0^\infty(\theta(e^u)-e^u)e^{-u}
             L_{n-1}^{(2)}(u)\,du.                         \tag{1}
\]

Se atacó (1) con la identidad de Selberg construida **solo** con la medida
de primos simples. Su medida no centrada es positiva y está soportada en
primos y semiprimos. Invirtiendo el operador lineal de Selberg antes de
tomar signos se obtiene una identidad colectiva lineal--cuadrática exacta.
El núcleo de Hankel de esa identidad no es coercivo: para todo índice par
es positivo en el origen y negativo en la cola. Además, aun fijando el
soporte en los primos verdaderos, positividad, PNT y la escala de simetría
de Selberg sobreviven al aumento de un solo peso primo, mientras (1) puede
hacerse arbitrariamente negativa para infinitos índices del rango objetivo.

Por tanto, retirar las potencias primas superiores no repara la ruta
Selberg/Vaughan. Una desigualdad proporcional todavía tendría que usar los
valores exactos \(\log p\) de todos los pesos, de manera firmada y global.
No se prueba (26) de `104_32`, A1 ni RH.

## 1. Auditoría de no duplicación y falsificador

`103_17` estudia la positividad local de
\(\Lambda\log+\Lambda*\Lambda\); `103_63` invierte el operador de Selberg
para la medida completa de potencias primas; `103_70` audita Vaughan y la
geometría de fase de sus bloques; `104_13` da la recurrencia Riccati de la
misma medida completa; `104_32` separa finalmente las potencias
\(p^k,\ k\ge2\).

Lo nuevo aquí es:

1. la fórmula exacta (1) para el canal residual de **primos simples--polo**,
   incluidos sus dos bordes;
2. la identidad colectiva de Selberg formada únicamente por primos y
   semiprimos;
3. el signo explícito del núcleo inverso en el origen y en la cola;
4. un testigo que mantiene el soporte en los primos verdaderos y conserva
   las escalas PNT/Selberg, pero cambia sin cota el funcional buscado.

El cuarteto fuera de línea no posee el producto de Euler de primos simples
con pesos \(\log p\). Por eso una futura desigualdad que use realmente esos
pesos no se aplicaría automáticamente al falsificador. En cambio, todo el
paquete más débil probado abajo ---soporte primo, positividad de Selberg y
sus escalas sumatorias--- también vale para el testigo de la Sección 6 y no
determina el signo. Así se evita un falso positivo: no se atribuye a esos
axiomas la información que solo podría estar en los pesos exactos.

## 2. Correlación exacta con \(\theta-x\)

Sea

\[
 \theta(x)=\sum_{p\le x}\log p,
 \qquad N=n-1,
\]

y, para \(a>1\), defínase

\[
 w_{n,a}(u)=a e^{-au}L_N^{(1)}(au),                         \tag{2}
\]

\[
 d\alpha(u)=\sum_p\log p\,\delta_{\log p}(du),
 \qquad d\beta(u)=e^u\,du,
 \qquad d\mu=d\alpha-d\beta.                              \tag{3}
\]

La transformada de Laguerre del continuo se calcula sin aproximaciones:

\[
\begin{aligned}
 \langle w_{n,a},\beta\rangle
 &=a\int_0^\infty e^{-(a-1)u}L_N^{(1)}(au)\,du\\
 &=1+{(-1)^{n+1}\over(a-1)^n}
 =n[z^n]\log\left({a\over1-z}-1\right).             \tag{4}
\end{aligned}
\]

La igualdad central usa la generatriz de Laguerre; equivalentemente, tras
\(v=au\), es la transformada de Laplace elemental de
\(L_N^{(1)}\). Por otra parte,

\[
 \langle w_{n,a},\alpha\rangle
 =a\sum_p{\log p\over p^a}L_N^{(1)}(a\log p).                \tag{5}
\]

Por (22) de `104_32`, (4)--(5) prueban

\[
 B_{n,a}^{(p+\mathrm{pole})}
 :=\langle w_{n,a},\beta-\alpha\rangle,
 \qquad
 B_n^{(p+\mathrm{pole})}=\lim_{a\downarrow1}B_{n,a}^{(p+\mathrm{pole})}.
                                                                    \tag{6}
\]

Para exhibir el borde, póngase
\(E_\theta(u)=\theta(e^u)-e^u\). La primitiva de \(\mu\) desde cero es

\[
 \mu([0,u])=E_\theta(u)+1.                                  \tag{7}
\]

La integración de Stieltjes de (6), primero con \(a>1\), no tiene borde
en cero porque (7) se anula allí. Además,

\[
 {d\over du}\{e^{-u}L_N^{(1)}(u)\}
 =-e^{-u}L_N^{(2)}(u).                                       \tag{8}
\]

La cota PNT efectiva usada en `104_01` justifica el límite dominado después
de la cancelación en (7). Como

\[
 \int_0^\infty e^{-u}L_N^{(2)}(u)\,du=N+1=n,                 \tag{9}
\]

(6)--(9) dan exactamente (1). En particular, el borde es \(-n\), no
\(-1\).

Debajo del primer primo, \(E_\theta(u)=-e^u\). Usando
\((L_n^{(1)})'=-L_{n-1}^{(2)}\), (1) tiene también la forma

\[
 \boxed{
 B_n^{(p+\mathrm{pole})}
 =1-L_n^{(1)}(\log2)
 -\int_{\log2}^\infty E_\theta(u)e^{-u}
                       L_{n-1}^{(2)}(u)\,du.}                 \tag{10}
\]

No se ha separado una cantidad divergente en (1) o (10).

## 3. La obligación proporcional en coordenada \(\theta\)

Sea \(R_N=P_N^{(\ge2)}(1)\), la corrección absolutamente convergente de
`104_32`. Su ecuación (26) es

\[
 3A_n+4B_n^{(p+\mathrm{pole})}
 \ge {A_n\over1001}+4R_N.                                   \tag{11}
\]

Al insertar (10), (11) equivale a una sola correlación de primos simples:

\[
\boxed{
 \int_{\log2}^\infty E_\theta(u)e^{-u}L_{n-1}^{(2)}(u)\,du
 \le
 \left({3\over4}-{1\over4004}\right)A_n
 +1-L_n^{(1)}(\log2)-R_N.}                                  \tag{12}
\]

El término \(R_N\) satisface \(|R_N|<14n+1\), pero no se omite ni se
absorbe para \(150\le n<e^{112116}\). Probar (12) uniformemente es
exactamente el frente proporcional; (10) no lo abarata por sí sola.

## 4. Selberg formado solo por primos y semiprimos

Para \(\Re s>1\), sea

\[
 Q(s)=\int e^{-su}\,d\alpha(u)=\sum_p{\log p\over p^s}.
                                                                    \tag{13}
\]

La identidad prima--Selberg es

\[
 -Q'(s)+Q(s)^2=\int e^{-su}\,d\mathcal A_p(u),                \tag{14}
\]

\[
 d\mathcal A_p=u\,d\alpha+\alpha*\alpha\ge0.                \tag{15}
\]

La medida de (15) está soportada únicamente en primos y semiprimos. Sus
pesos son

\[
 \begin{array}{c|c}
 \text{punto}&\text{peso}\ \\ \hline
 \log p&(\log p)^2,\\
 2\log p&(\log p)^2,\\
 \log p+\log q&2\log p\log q\quad(p\ne q).
 \end{array}                                                   \tag{16}
\]

Como \((\beta*\beta)(du)=u e^u du=u\,d\beta\), la referencia continua
de (15) es \(2u\,d\beta\). Definiendo

\[
 d\mathcal B_p=d\mathcal A_p-2u\,d\beta,                     \tag{17}
\]

la sustitución \(\alpha=\beta+\mu\) produce, sin estimar ninguna pieza,

\[
 \boxed{d\mathcal B_p=u\,d\mu+2\beta*\mu+\mu*\mu.}         \tag{18}
\]

Esta es la identidad de Selberg centrada después de retirar todas las
potencias primas superiores.

## 5. Inversión colectiva y pérdida exacta de coercividad

Para una función \(g\) de decaimiento suficiente, (18) da

\[
 \langle g,\mathcal B_p\rangle
 =\langle\mathcal Tg,\mu\rangle+\mathcal Q_g(\mu),             \tag{19}
\]

\[
 (\mathcal Tg)(v)
 =vg(v)+2e^{-v}\int_v^\infty e^t g(t)\,dt,
 \qquad
 \mathcal Q_g(\mu)=\iint g(u+v)\,d\mu(u)d\mu(v).             \tag{20}
\]

En vez de separar los tres sumandos de (18), resolvemos

\[
 \mathcal Tg=w_{n,a}.                                         \tag{21}
\]

La solución que decae en infinito es explícita:

\[
\boxed{
 g_{n,a}(v)={1\over v}\left[
 w_{n,a}(v)-2v^2e^{-v}\int_v^\infty
 {e^t w_{n,a}(t)\over t^3}\,dt\right].}                     \tag{22}
\]

La singularidad aparente en cero es removible. La prueba consiste en
diferenciar

\[
 H(v)=v^2e^{-v}\int_v^\infty{e^tw_{n,a}(t)\over t^3}\,dt
\]

y comprobar que \(H'=(2/v-1)H-w/v\). Entonces
\(g=-H'-H\), y una integración desde infinito recupera (20)--(21).
Todas las integrales son absolutamente convergentes para \(a>1\).

Al insertar (21) en (19), el canal regulado queda acoplado exactamente:

\[
 \boxed{
 B_{n,a}^{(p+\mathrm{pole})}
 =-\langle g_{n,a},\mathcal B_p\rangle
   +\mathcal Q_{g_{n,a}}(\mu).}                               \tag{23}
\]

La identidad (23) es el ataque sin valores absolutos solicitado. No
produce una cota inferior porque su forma cuadrática no es positiva. En
efecto, de \(L_N^{(1)}(0)=n\) y
\(L_N^{(2)}(0)=n(n+1)/2\) se obtiene

\[
 \boxed{
 g_{n,a}(0)=an\left({a(n+1)\over2}-1\right)>0.}               \tag{24}
\]

Para \(N=n-1\ge1\), el término principal en infinito es

\[
 \boxed{
 g_{n,a}(v)
 ={(-1)^N a^{N+1}\over N!}e^{-av}v^{N-1}
   \{1+O_{n,a}(v^{-1})\}.}                                   \tag{25}
\]

Por tanto, para cada \(n\) par existe \(R_{n,a}\) tal que

\[
 g_{n,a}(2R)<0\qquad(R\ge R_{n,a}).                           \tag{26}
\]

Tomando \(\sigma=c\delta_R\), \(c>0\),

\[
 \mathcal Q_{g_{n,a}}(\sigma)=c^2g_{n,a}(2R)<0.               \tag{27}
\]

Así, ni siquiera en el canal exclusivamente primo la convolución de
Selberg es una energía coerciva. La pérdida ocurre después de mantener
acoplados el término lineal y el cuadrático; no es consecuencia de haber
tomado valores absolutos.

## 6. Testigo sobre el soporte primo real

La falta de signo tampoco puede repararse usando solo que los átomos están
en primos. Fíjese un primo real \(p_0\), \(R=\log p_0\), y aumente solo su
peso:

\[
 d\alpha_c=d\alpha+c\delta_R,
 \qquad c>0.                                                   \tag{28}
\]

La medida sigue siendo positiva y su soporte sigue siendo exactamente un
subconjunto de los primos verdaderos. Su función de Chebyshev cambia por
el escalón acotado \(c\mathbf1_{u\ge R}\); por tanto conserva el mismo
orden y toda relación asintótica eventual de tipo PNT. No se afirma que
conserve las mismas constantes efectivas ni el mismo rango inicial de una
desigualdad PNT fijada.

La medida Selberg no centrada permanece positiva y su variación es

\[
 d\mathcal A_{p,c}-d\mathcal A_p
 =cR\delta_R+2c\,\alpha*\delta_R+c^2\delta_{2R}.               \tag{29}
\]

Usando la cota elemental
\(\theta(x)\le2(\log2)x\), su masa acumulada hasta \(U\) es a lo sumo

\[
 cR+4c(\log2)e^{U-R}+c^2=O_{c,R}(e^U).                         \tag{30}
\]

Por ello también conserva la escala \(O(x)\) de la simetría centrada de
Selberg.

Sin embargo, (6) cambia exactamente en

\[
 B_{n,a}[\alpha_c]-B_{n,a}[\alpha]=-c\,w_{n,a}(R).             \tag{31}
\]

Como la perturbación es un solo átomo, el límite crítico es ordinario y

\[
 B_n[\alpha_c]-B_n[\alpha]
 =-{c\over p_0}L_{n-1}^{(1)}(\log p_0).                        \tag{32}
\]

Si \(n\) es impar, entonces \(N=n-1\) es par y (2) es positiva para todo
\(R\) suficientemente grande. Hay primos arbitrariamente grandes, de modo
que para cada índice impar ---en particular para infinitos
\(n\ge150\)--- se puede elegir un primo real en la cola y hacer (32)
arbitrariamente negativa aumentando \(c\).

Este testigo no conserva el valor canónico \(\log p_0\); ése es
precisamente su contenido lógico. Prueba que **soporte en primos +
positividad + PNT + escala Selberg** no implican una cota proporcional.
Un teorema que cierre (12) debe distinguir los pesos exactos \(\log p\)
de (28).

## 7. Por qué Vaughan no gana una dirección nueva

Para cualquier peso \(W\), la separación tautológica es

\[
 \sum_p\log p\,W(p)
 =\sum_m\Lambda(m)W(m)
  -\sum_p\sum_{k\ge2}\log p\,W(p^k).                          \tag{33}
\]

En el peso Laguerre de este frente, el segundo término es exactamente
\(R_N\), ya retirado y acotado por `104_32`. Aplicar Vaughan al primer
término devuelve los bloques de `103_70`: en coordenadas logarítmicas su
fase depende solo de la suma de las variables y su Hessiana tiene rango
uno. La sustracción de \(R_N=O(n)\) no crea curvatura en las direcciones
planas ni una estimación firmada entre shells. Por tanto, el canal simple
no desbloquea el Type I/II estándar; el input que faltaría sigue siendo una
cota conjunta sobre los pesos exactos.

## 8. Decisión

```text
probado incondicionalmente:
  fórmula θ--Laguerre exacta (1) y borde -n;
  forma exterior exacta (10) y obligación proporcional (12);
  Selberg positivo solo-primos/semiprimos (14)--(18);
  identidad colectiva sin valores absolutos (23);
  signo g(0)>0 y signo negativo de cola para todo n par;
  testigo sobre soporte primo que conserva PNT y escala Selberg.

descartado:
  positividad de la medida Selberg simple como coercividad de (23);
  soporte primo + escala PNT/Selberg como sustituto de los pesos log p;
  Vaughan estándar como nueva dirección oscilatoria tras retirar p^k.

permanece abierto:
  una desigualdad firmada y global que use los pesos exactos log p y
  pruebe (12), equivalentemente (26) de 104_32.

no probado:
  la cota proporcional, A1 o RH.
```

`tools/simple_prime_pole_selberg_check.py` comprueba con `Fraction` las
identidades polinómicas de borde de (8)--(9) y la expansión algebraica de
la medida centrada en (18).
