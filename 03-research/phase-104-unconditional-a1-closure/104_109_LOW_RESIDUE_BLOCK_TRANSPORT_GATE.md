# 104_109 — Residuo bajo, barrera por bloques y gate del promedio de transporte

**Pregunta.** Combinar la relajación por bloques de `104_67` con la
fórmula frontera--residuos de `104_33`--`104_41`: ¿basta promediar el
defecto de transporte sobre grados consecutivos y usar la cota

\[
 |\mathcal B_{n,a}|\leq3n\qquad(a\geq4)                    \tag{1}
\]

para obtener la barrera superior
\(\lambda_n\leq e^{\sqrt n}\) en bloques arbitrariamente largos?

**Resultado.** La combinación sí reduce el criterio, con margen
exponencial, a una suma **finita** de residuos exteriores de altura
\(\gamma\leq(2N)^{1/4}\). Ésta es la escala correcta para la barrera
\(e^{\sqrt n}\); la escala \(\sqrt n\) corresponde solo al inicio de la
amplificación radial \(na_\rho\asymp1\), no a este umbral profundo.

El promedio lineal sobre el bloque no conserva, sin embargo, la barrera
grado a grado. Un cuarteto racional con

\[
 w={4i\over5},\qquad
 \rho={1\over1-w}={25+20i\over41}                         \tag{2}
\]

tiene excursiones positivas exponenciales en cada clase
\(n\equiv2\pmod4\), pero posee bloques linealmente promediados de longitud
arbitraria cuyo promedio es negativo. Además, la transformación
binomial negativa de (1) convierte sus dos modos peligrosos en modos
estrictamente contractivos y satisface \(|T_4b_n|\leq3n\) para todo
\(n\geq2\). Así, ni el promedio ordinario del defecto ni (1), aun cuando
la identidad de transformación converge absolutamente, prueban la barrera
de `104_67`.

El blanco mínimo que queda es no lineal: controlar el máximo, o la parte
positiva, de la forma prima--Laguerre completa en un bloque. Este documento
no prueba ese control, A1 ni RH.

---

## 1. Auditoría interna y alcance

Este ataque no vuelve a abrir las rutas ya cerradas:

* `104_65` prueba que todo filtro lineal fijo conserva un modo exterior o
  lo anula artificialmente;
* `104_67` prueba que una barrera **superior** en bloques de longitud no
  acotada equivale a RH;
* `104_74` separa, sobre un bloque, un contorno polinómico de la suma finita
  de polos interiores;
* `104_76` acota absolutamente la cola de altura alta en la escala
  profunda;
* `104_33` y `104_41` identifican el defecto de transporte con el núcleo de
  Fejér meromorfo;
* `104_106` ya prueba la identidad para un filtro finito arbitrario, la
  dualidad con todos los selectores y el gate de la media firmada;
* `104_107` ya obtiene el promedio triangular de Fejér y su cota de fase
  \(O(N/L+1)\), y demuestra que el residuo exterior sobrevive.

Lo nuevo aquí respecto de `104_106`--`104_107` es la localización uniforme
del selector en el **residuo bajo** de altura \(O(N^{1/4})\), con la cola
complementaria separada por un margen exponencial, y el gate adicional de
la transformación binomial negativa que conecta directamente con la cota
en \(a=4\). El ejemplo de promedio de §5 vuelve a registrarse solo porque el
mismo cuarteto satisface además, de manera absolutamente convergente, el
gate de \(a=4\) de §6. No se reclama novedad bibliográfica para la fórmula
de Li ni para esa transformación.

---

## 2. Identidad exacta del residuo exterior bajo

Para un cero \(\rho=\beta+i\gamma\), \(\beta>1/2\), \(\gamma>0\), ponga

\[
 w_\rho=1-{1\over\rho},
 \qquad
 \mathcal F_n(w)=n+\sum_{d=1}^{n-1}(n-d)(w^d+w^{-d}).     \tag{3}
\]

La identidad algebraica de `104_33` es

\[
 {\mathcal F_n(w_\rho)\over\rho(\rho-1)}
 =w_\rho^n+w_\rho^{-n}-2.                                \tag{4}
\]

Sea \(\mathscr Z_+(Y)\) el multiconjunto de ceros con
\(\beta>1/2\), \(0<\gamma\leq Y\), uno por cada miembro derecho de
ordenada positiva. Defina el defecto de transporte truncado

\[
 \boxed{
 D_n(Y):=2\Re\sum_{\rho\in\mathscr Z_+(Y)}
 {m_\rho\mathcal F_n(w_\rho)\over\rho(\rho-1)}.}         \tag{5}
\]

Por (4), el sumando correspondiente a la órbita funcional completa es

\[
 2m_\rho\Re(w_\rho^n+w_\rho^{-n}-2),                     \tag{6}
\]

que es el negativo de la contribución de ese cuarteto al coeficiente de
Li. Si

\[
 C_n(Y)=\sum_{\substack{\rho=1/2+i\gamma\\0<\gamma\leq Y}}
 2m_\rho\{1-\cos(n\theta_\rho)\},
 \qquad w_\rho=e^{i\theta_\rho},                         \tag{7}
\]

y \(H_n(Y)\) es la suma, por órbitas completas, de todos los ceros con
\(\gamma>Y\), la fórmula de Li agrupada funcionalmente da exactamente

\[
 \boxed{\lambda_n=-D_n(Y)+C_n(Y)+H_n(Y).}                \tag{8}
\]

No se ha supuesto RH. Además,

\[
 0\leq C_n(Y)\leq4N_\zeta(Y).                            \tag{9}
\]

Por el Lema 2.1 de `104_76`, uniformemente para \(1\leq n\leq X\) y
\(2\leq Y\leq2X\),

\[
 |H_n(Y)|\ll X\log(X+2)
 \left\{1+\exp\left({X\over2Y^2}\right)\right\}.       \tag{10}
\]

Junto con \(N_\zeta(Y)\ll Y\log(Y+2)\), (8)--(10) prueban

\[
 \boxed{
 \sup_{n\leq X}|\lambda_n+D_n(Y)|
 \ll Y\log(Y+2)+X\log(X+2)
 \left\{1+e^{X/(2Y^2)}\right\}.}                         \tag{11}
\]

La parte crítica se mantuvo con su signo en (8); solo se usó su módulo
para la cota uniforme (11).

---

## 3. El criterio mínimo de bloque

Tome

\[
 X=2N,\qquad Y_N=(2N)^{1/4}.                             \tag{12}
\]

El miembro derecho de (11) es

\[
 O\!\left(N\log(N+2)e^{\sqrt{2N}/2}\right)
 =o(e^{\sqrt N}).                                        \tag{13}
\]

Por tanto existe un \(N_0\) absoluto tal que, para \(N\geq N_0\),

\[
 \sup_{N\leq n\leq2N}|\lambda_n+D_n(Y_N)|
 \leq{1\over2}e^{\sqrt N}.                              \tag{14}
\]

La constante \(1/2\) no es intrínseca: cualquier constante fija entre
\(0\) y \(1\) sirve después de aumentar \(N_0\).

**Teorema 3.1 (criterio de residuo bajo en bloques).** Son equivalentes:

1. RH;
2. existen \(N_j\to\infty\) e intervalos consecutivos
   \(I_j\subset[N_j,2N_j]\), con \(|I_j|\to\infty\), tales que

   \[
   \boxed{
   D_n((2N_j)^{1/4})\geq-{1\over2}e^{\sqrt{N_j}}
   \quad(n\in I_j).}                                    \tag{15}
   \]

*Demostración.* Bajo RH, \(\mathscr Z_+(Y)\) es vacío para cada \(Y\),
de modo que \(D_n(Y)=0\) y (15) vale en cualquier intervalo.

Recíprocamente, (14)--(15) implican, para \(n\in I_j\),

\[
 \lambda_n\leq-D_n(Y_{N_j})+{1\over2}e^{\sqrt{N_j}}
 \leq e^{\sqrt{N_j}}\leq e^{\sqrt n}.                   \tag{16}
\]

Así existen bloques de longitud no acotada que satisfacen la barrera
superior de `104_67`, Corolario 2.1, y por ese corolario vale RH.
\(\square\)

La reducción (15) no pide controlar todos los ceros. Para el nivel
\(e^{\sqrt n}\), toda contribución que aún pueda cruzar el umbral se ha
concentrado en \(\gamma\ll n^{1/4}\). Las otras dos escalas que pueden
confundirse con ésta son:

* \(\gamma\asymp\sqrt n\), donde comienza
  \(na_\rho\asymp1\);
* \(\gamma\asymp\sqrt{n/\log n}\), donde una cota absoluta radial baja
  hasta tamaño polinómico.

Para la barrera profunda usada en `104_67`, la escala pertinente es
\(n^{1/4}\), como muestran (10)--(13).

---

## 4. La forma aritmética que realmente habría que acotar

Use exactamente la regularización de `104_61` y `104_67`:

\[
\begin{aligned}
 Q_{n,\varepsilon}
 &=\sum_{m\geq2}{\Lambda(m)\over m^{1+\varepsilon}}
      L_{n-1}^{(1)}(\log m),\\
 \lambda_{n,\varepsilon}
 &=A_n+p_n(\varepsilon)-Q_{n,\varepsilon},
 \qquad \lambda_{n,\varepsilon}\longrightarrow\lambda_n.
                                                               \tag{17}
\end{aligned}
\]

Para un intervalo finito \(I\), continuidad de la parte positiva da

\[
\boxed{
 \sum_{n\in I}(\lambda_n-e^{\sqrt n})_+
 =\lim_{\varepsilon\downarrow0}
 \sum_{n\in I}
 \left(
 A_n+p_n(\varepsilon)
 -\sum_{m\geq2}{\Lambda(m)\over m^{1+\varepsilon}}
       L_{n-1}^{(1)}(\log m)-e^{\sqrt n}
 \right)_+.}                                             \tag{18}
\]

La barrera en todo el bloque equivale a que (18) sea cero. La expresión
conserva el polo, el bloque arquimediano, los primos, las potencias primas
y la fase Laguerre hasta después de tomar la parte positiva. Probar que el
miembro derecho se anula para bloques de longitud no acotada cerraría RH
por `104_67`.

Un promedio lineal no sustituye (18). La razón no es una desigualdad
perdida, sino el siguiente falsificador exacto.

---

## 5. Falsificador racional del promedio de bloque

Considere (2). Se tiene

\[
 \Re\rho={25\over41}>{1\over2},
 \qquad |w|^2={16\over25}<1.                              \tag{19}
\]

La contribución de su cuarteto a Li es

\[
 q_n=4-2\Re(w^n+w^{-n}).                                  \tag{20}
\]

Escribiendo \(r=5/4\),

\[
 q_n=
 \begin{cases}
 4-2(r^n+r^{-n}),&n\equiv0\pmod4,\\
 4+2(r^n+r^{-n}),&n\equiv2\pmod4,\\
 4,&n\text{ impar}.
 \end{cases}                                             \tag{21}
\]

En particular, cada cuatro enteros consecutivos contienen un índice en el
que

\[
 q_n>2(5/4)^n.                                            \tag{22}
\]

No hay bloques punto a punto para la barrera superior. Sin embargo, para
\(K\geq0\), \(M\geq1\), la suma lineal exacta es

\[
\begin{aligned}
 \sum_{n=4K+1}^{4K+4M}q_n
 ={}&16M-{2\over1+r^2}
 \left\{
 r^2(r^{4(K+M)}-r^{4K})
 +r^{-4(K+M)}-r^{-4K}
 \right\}.                                               \tag{23}
\end{aligned}
\]

Para cada \(M\), (23) tiende a \(-\infty\) cuando \(K\to\infty\).
Por consiguiente hay intervalos tan largos y tan alejados como se quiera
en los que el **promedio** de \(q_n\) es negativo, aunque (22) viola la
barrera en cada subintervalo de longitud cuatro.

Así, una cota para

\[
 {1\over|I|}\sum_{n\in I}D_n(Y)                           \tag{24}
\]

no implica la cota mínima (15). Debe controlarse la parte negativa grado a
grado, equivalentemente el máximo o la parte positiva de (18).

---

## 6. Por qué la cota en \(a=4\) no repara el promedio

Cuando la expansión converge, (4a) de `104_41` puede escribirse como el
promedio binomial negativo

\[
 T_aB(n):=\sum_{k\geq n}\pi_{n,k}^{(a)}B_k,
 \qquad
 \pi_{n,k}^{(a)}=a^{-n}{k-1\choose n-1}
 \left(1-{1\over a}\right)^{k-n},                        \tag{25}
\]

con \(\sum_{k\geq n}\pi_{n,k}^{(a)}=1\), y

\[
 \mathcal B_{n,a}=T_aB(n).                               \tag{26}
\]

Para un modo geométrico \(v^k\),

\[
 \boxed{
 T_a(v^k)(n)=\tau_a(v)^n,
 \qquad
 \tau_a(v)={v\over a-(a-1)v},}                           \tag{27}
\]

si \(|(1-1/a)v|<1\).

En el cuarteto (2), el defecto de \(B=A-\lambda\) es

\[
 b_n=-q_n=-4+2\Re(w^n+w^{-n}).                           \tag{28}
\]

Para \(a=4\), incluso el modo dominante está dentro del dominio de
convergencia, pues

\[
 {3\over4}|w^{-1}|={15\over16}<1.                         \tag{29}
\]

No obstante,

\[
\begin{aligned}
 |4w-3|^2&={481\over25}>1,\\
 |\tau_4(w)|^2&={1\over34},\\
 |\tau_4(w^{-1})|^2&={25\over481},
 \qquad \tau_4(w^{-1})=(4w-3)^{-1}.                      \tag{30}
\end{aligned}
\]

Por (27)--(28),

\[
 T_4b(n)=-4+2\Re\{\tau_4(w)^n+\tau_4(w^{-1})^n\}.       \tag{31}
\]

Los dos modos de (31) son contractivos. En particular,

\[
\begin{aligned}
 |T_4b(n)|
 &\leq4+2\left(34^{-n/2}+(25/481)^{n/2}\right)\\
 &\leq4+2\left({1\over34}+{25\over481}\right)<6\leq3n
 \qquad(n\geq2),
\end{aligned}                                             \tag{31a}
\]

es decir,

\[
 \boxed{|T_4b(n)|\leq3n\qquad(n\geq2),}                 \tag{32}
\]

mientras (22) conserva excursiones positivas de tamaño \((5/4)^n\) con
huecos cuatro. El transporte hasta \(a=4\) ha amortiguado precisamente el
modo que la barrera debía detectar. Invertirlo es inestable y vuelve a
cruzar el polo interior de `104_41`.

El cuarteto (2) no tiene los pesos de Euler de los primos ordinarios. Por
ello (19)--(32) no refutan (18) para la \(zeta\) real. Sí refutan la
inferencia

\[
 |\mathcal B_{n,4}|\leq3n
 \quad+\quad\text{promedio lineal en }n
 \quad\Longrightarrow\quad\text{barrera de bloque}.      \tag{33}
\]

Una prueba para los \(\Lambda(m)\) reales debe usar información aritmética
que no está contenida en (1), (25) ni en el promedio (24).

---

## 7. Veredicto

**Probado.** La identidad de residuo bajo (8), la cota uniforme (11), el
criterio equivalente de bloques (15), la escala \(n^{1/4}\), la forma
prima--Laguerre mínima (18), el promedio engañoso (23) y la contracción
exacta bajo \(T_4\) (30)--(32).

**Ganancia.** Al volver de la energía de Cramér al andamiaje Li--Laguerre,
la barrera superior queda localizada en una suma finita de residuos de
altura \(O(n^{1/4})\), mientras todo el bloque alto posee margen
\(e^{-(1-1/\sqrt2)\sqrt n+O(\log n)}\).

**Gate exacto.** `104_67` requiere una desigualdad para cada grado del
bloque. Un promedio lineal puede tener el signo correcto en bloques
arbitrariamente largos y simultáneamente fallar cada cuatro grados. La
cota de fase en \(a=4\) también puede coexistir con ese fallo porque la
transformación (27) vuelve contractivo el modo exterior.

**Sobrevive.** Probar que (18) se anula en bloques de longitud no acotada,
o directamente (15), usando una identidad no lineal y específica de los
pesos ordinarios \(\Lambda(m)\).

**No probado.** (15) para la zeta ordinaria sin asumir RH, la anulación de
(18), A1 o RH.

---

## 8. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 low_residue_block_transport_gate_check.py
```

El checker usa únicamente `Fraction`. Verifica (2), (19), (21)--(23), los
dos factores contractivos de (30), (31)--(32), la excursión positiva en
cada clase \(2\pmod4\) y la existencia de promedios negativos sobre bloques
de longitudes crecientes.
