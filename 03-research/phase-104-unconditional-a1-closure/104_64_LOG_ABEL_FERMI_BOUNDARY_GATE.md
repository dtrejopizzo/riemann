# 104_64 — Abel logarítmico y capa Fermi doblemente logarítmica

**Estado.** El promedio Fermi de `104_61` se puede Abelizar sin perder ni
ganar contenido: para el sumando acotado, media logarítmica de Cesàro cero y
media logarítmica de Abel cero son equivalentes. Esto permite insertar el
producto prima--Laguerre exacto en una suma exterior infinita, todavía
acotada, y reduce el objetivo a una sola aproximación radial.

La Abelización no prueba el límite. El cuarteto racional fuera de la línea
produce una obstrucción cuantitativa nueva: su corrección Fermi negativa está
repartida uniformemente en la escala

\[
 \alpha={\log\log(1/s)\over\log(1/h)},\qquad q=e^{-h},
 \quad 0\leq\alpha\leq1.
\]

Controlar frecuencias solo hasta \(s=\exp(-h^{-\alpha})\), con
\(\alpha<1\) fijo, deja escapar una proporción positiva de la corrección de
la clase mala. Para capturarla toda hay que alcanzar
\(s=\exp(-c/h)\). La conclusión es un **stop-gate** para una transferencia
Abel--Fourier truncada; no es un no-go para una cancelación nueva que conserve
simultáneamente todas las clases y todos los canales aritméticos.

**Atribución.** La equivalencia entre los métodos logarítmicos de Cesàro y
Abel pertenece a la teoría clásica de sumabilidad; véase Bingham--Gashi,
[DOI 10.1016/j.jmaa.2014.08.031](https://doi.org/10.1016/j.jmaa.2014.08.031).
Aquí se prueba directamente solo la especialización positiva de límite cero
y se aplica al detector Li--Fermi. No se reclama novedad para el teorema de
sumabilidad.

---

## 1. El criterio Fermi en coordenada Abel

Fije \(t>0\), y escriba

\[
 b_n=\log(n+1),\qquad
 a_n={1\over1+\exp(t(\lambda_n+b_n))},\qquad 0\leq a_n\leq1.
 \tag{1}
\]

Para \(X\geq1\) y \(h>0\), defina

\[
 S(X)=\sum_{n\leq X}{a_n\over n},\qquad
 H_X=\sum_{n\leq X}{1\over n},
 \tag{2}
\]

\[
 L(h)=\sum_{n\geq1}{e^{-hn}\over n}
      =-\log(1-e^{-h}),\qquad
 \mathfrak A_t(h)={1\over L(h)}
 \sum_{n\geq1}{e^{-hn}a_n\over n}.
 \tag{3}
\]

**Teorema 1.1 (Abel--Cesàro para el detector acotado).** Se tiene

\[
 \boxed{
 {S(X)\over H_X}\longrightarrow0
 \quad\Longleftrightarrow\quad
 \mathfrak A_t(h)\longrightarrow0\quad(h\downarrow0).}
 \tag{4}
\]

Además, para los coeficientes de Li,

\[
 \boxed{
 \mathrm {RH}
 \quad\Longleftrightarrow\quad
 \liminf_{h\downarrow0}\mathfrak A_t(h)=0.}
 \tag{5}
\]

**Demostración.** Suponga primero que \(S(X)=o(\log X)\). Sumación de Abel
da

\[
 \sum_{n\geq1}{e^{-hn}a_n\over n}
 =(1-e^{-h})\sum_{N\geq1}e^{-hN}S(N).
 \tag{6}
\]

Dado \(\epsilon>0\), el prefijo donde no se conoce
\(S(N)\leq\epsilon\log N\) aporta \(O_\epsilon(h)\). En el resto se usa

\[
 (1-e^{-h})\sum_{N\geq1}e^{-hN}\log(N+1)
 =\log(1/h)+O(1),
 \tag{7}
\]

mientras \(L(h)=\log(1/h)+O(h)\). Esto prueba la implicación directa de
(4).

Recíprocamente, tome \(h=1/X\). Para \(n\leq X\),
\(e^{-hn}\geq e^{-1}\), y por tanto

\[
 S(X)\leq e\,L(1/X)\mathfrak A_t(1/X).
 \tag{8}
\]

Como \(L(1/X)\sim H_X\), sigue la otra implicación.

Bajo RH, \(\lambda_n\geq0\), luego
\(a_n\leq(n+1)^{-t}\), y el numerador de (3) queda acotado cuando
\(h\downarrow0\). Así \(\mathfrak A_t(h)\to0\). Si RH es falsa, el
Teorema 3.1 de `104_56` da un conjunto \(D\) de densidad natural
\(d>0\) en el que \(a_n\to1\). Sumación parcial da

\[
 \liminf_{h\downarrow0}{1\over L(h)}
 \sum_{n\in D}{e^{-hn}\over n}=d,
 \tag{9}
\]

y por ello \(\liminf\mathfrak A_t(h)\geq d>0\). Esto prueba (5).
\(\square\)

En particular, para probar RH basta encontrar **una** sucesión
\(h_j\downarrow0\) sobre la cual \(\mathfrak A_t(h_j)\to0\). Ésta es una
reducción genuina del cuantificador, pero no una estimación del promedio.
La sucesión puede prefijarse: por ejemplo,

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \mathfrak A_t(2^{-j})\longrightarrow0\quad(j\to\infty).}
 \tag{9a}
\]

No hay selección posterior favorable escondida en (9a): bajo
\(\neg\mathrm {RH}\), la cota inferior de (9) vale uniformemente cuando
\(h\downarrow0\), y por tanto sobre toda sucesión prescrita.

---

## 2. Forma prima--Laguerre exacta de la media Abel

Use la regularización emparejada de `104_61`:

\[
 \lambda_{n,\varepsilon}
 =A_n+p_n(\varepsilon)
 -\sum_{m\geq2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m),
 \qquad
 \lambda_{n,\varepsilon}\to\lambda_n.
 \tag{10}
\]

Como la logística está entre cero y uno y
\(\sum e^{-hn}/n=L(h)<\infty\), convergencia dominada da la identidad

\[
\boxed{
\begin{aligned}
 \mathfrak A_t(h)
 =\lim_{\varepsilon\downarrow0}{1\over L(h)}
 \sum_{n\geq1}{e^{-hn}\over n}
 \Bigg[1+e^{t(A_n+b_n+p_n(\varepsilon))}
 \prod_{m\geq2}\exp\!\left(
 -{t\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m)\right)\Bigg]^{-1}.
\end{aligned}}
 \tag{11}
\]

Para cada \(\varepsilon>0\), el producto interior converge absolutamente.
La ecuación (11) conserva juntos polo, bloque arquimediano, primos y
potencias primas hasta después de aplicar la no linealidad. A diferencia de
`104_61`, (20c), la suma exterior ya es infinita; su paso al borde es
legítimo precisamente porque el observable es acotado.

También hay una versión unitaria. Para \(N<\infty\), ponga

\[
 \mathcal C_{h,N,\varepsilon}(s)
 ={1\over L(h)}\sum_{n\leq N}{e^{-hn}\over n}
 e^{ist(\lambda_{n,\varepsilon}+b_n)}.
 \tag{12}
\]

La fórmula de Fourier de `104_62` implica, con el orden de límites escrito,

\[
 \boxed{
 \mathfrak A_t(h)
 ={1\over2}-\lim_{N\to\infty}\lim_{\varepsilon\downarrow0}
 \int_0^\infty
 {\operatorname {Im}\mathcal C_{h,N,\varepsilon}(s)
  \over\sinh(\pi s)}\,ds.}
 \tag{13}
\]

En (12), cada exponencial tiene el producto unitario prima--Laguerre de
`104_62`, (8). No se permutan en (13) el borde
\(\varepsilon\downarrow0\), la suma infinita y \(s\downarrow0\): esa
permutación es justamente la capa que se audita a continuación.

---

## 3. Cuarteto off-line y ley de la capa anidada

Use el falsificador exacto

\[
 Q_n=4-2\operatorname {Re}\{(2i)^n+(2i)^{-n}\}.
 \tag{14}
\]

Si \(4\mid n\), defina

\[
 Y_n=-\{Q_n+\log(n+1)\}
 =2(2^n+2^{-n})-4-\log(n+1).
 \tag{15}
\]

Para \(n\geq4\), \(Y_n\geq2^n\). Sea

\[
 J_n(\delta)=\int_\delta^\infty
 {\sin(stY_n)\over\sinh(\pi s)}\,ds.
 \tag{16}
\]

La integral completa satisface

\[
 J_n(0)={1\over2}\tanh{tY_n\over2}\longrightarrow{1\over2}.
 \tag{17}
\]

Además,

\[
 \left|J_n(\delta)\right|\leq1,
 \tag{18}
\]

porque, si \(\delta tY_n\leq1\), se resta de (17) una integral de módulo a
lo sumo \(tY_n\delta/\pi\), y, si \(\delta tY_n>1\), la integración por
partes de `104_62`, (15), da
\(2/(tY_n\sinh(\pi\delta))<2/\pi\).

Para \(0<\alpha<1\), ponga

\[
 \delta_\alpha(h)=\exp(-h^{-\alpha})
 \tag{19}
\]

y considere solo la corrección de Fourier de la clase negativa:

\[
 T_\alpha(h)={1\over L(h)}
 \sum_{\substack{n\geq4\\4\mid n}}{e^{-hn}\over n}
 J_n(\delta_\alpha(h)).
 \tag{20}
\]

**Teorema 3.1 (ley doblemente logarítmica).** Para todo
\(0<\alpha<1\),

\[
 \boxed{T_\alpha(h)\longrightarrow{\alpha\over8}
 \qquad(h\downarrow0).}
 \tag{21}
\]

Los valores de borde, entendidos por límite, son \(0\) para
\(\alpha=0\) y \(1/8\) para \(\alpha=1\).
En particular, la ventana descartada \(0<s<\delta_\alpha(h)\) contiene
exactamente la proporción complementaria:

\[
 {1\over L(h)}
 \sum_{\substack{n\geq4\\4\mid n}}{e^{-hn}\over n}
 \{J_n(0)-J_n(\delta_\alpha(h))\}
 \longrightarrow {1-\alpha\over8}.
 \tag{21a}
\]

**Demostración.** Para \(0<\beta\leq1\), la progresión \(4\mid n\) cumple

\[
 {1\over L(h)}\sum_{\substack{n\leq h^{-\beta}\\4\mid n}}
 {e^{-hn}\over n}\longrightarrow{\beta\over4}.
 \tag{22}
\]

Si \(\beta<1\), esto sigue de \(e^{-hn}=1+o(1)\) uniformemente en el
rango y de la suma armónica en una progresión; para \(\beta=1\), la cola
con \(n\asymp h^{-1}\) solo altera el término \(O(1)\), no el coeficiente de
\(\log(1/h)\).

Fije \(0<\eta<\min(\alpha,1-\alpha)\). Uniformemente para
\(n\leq h^{-(\alpha-\eta)}\), se tiene

\[
 \delta_\alpha(h)tY_n
 \leq\exp\{-h^{-\alpha}+O(h^{-(\alpha-\eta)})\}\longrightarrow0,
 \tag{23}
\]

por lo que \(J_n(\delta_\alpha(h))=1/2+o(1)\), salvo un prefijo de peso
normalizado nulo. Uniformemente para
\(n\geq h^{-(\alpha+\eta)}\), la cota de integración por partes da

\[
 |J_n(\delta_\alpha(h))|
 \leq {2\over\pi tY_n\delta_\alpha(h)}=o(1).
 \tag{24}
\]

Por (18), la franja intermedia cuesta a lo sumo

\[
 {1\over4}\{(\alpha+\eta)-(\alpha-\eta)\}+o(1)
 ={\eta\over2}+o(1).
 \tag{25}
\]

La parte hasta (h^{-(\alpha-\eta)}) aporta
\((\alpha-\eta)/8+o(1)\). Como (J_n(\delta)) no tiene signo fijo, la
franja intermedia debe restarse también en la cota inferior. Las ecuaciones
(22)--(25) dan precisamente

\[
 {\alpha-\eta\over8}-{\eta\over2}+o(1)
 \leq T_\alpha(h)\leq
 {\alpha-\eta\over8}+{\eta\over2}+o(1).
\]

Haciendo \(\eta\downarrow0\) se obtiene (21). Para \(\alpha=0\),
\(\delta_0=e^{-1}\) es fija y la integración por partes hace acotado el
numerador de (20), de modo que el cociente tiende a cero. Para
\(\alpha=1\), el rango (n\leq h^{-(1-\eta)}) aporta
\((1-\eta)/8+o(1)\); la franja restante hasta la escala Abel
(n\asymp h^{-1}) tiene masa armónica normalizada a lo sumo
\(\eta/4+o(1)\), y la cola (n\gg h^{-1}) aporta (O(1/L(h))).
Dejar \(\eta\downarrow0\) da (1/8). \(\square\)

Equivalentemente, la corrección está distribuida de manera uniforme en la
coordenada

\[
 \alpha={\log\log(1/s)\over\log(1/h)}.
 \tag{26}
\]

Una cota que solo controle \(s\geq h^B\) corresponde a
\(\alpha\to0\) y no ve asintóticamente ninguna parte de (20). Para captar
toda la corrección de la clase mala hay que llegar a
\(\alpha=1\), es decir, \(s=\exp(-c/h)\) en la escala de Abel.

---

## 4. Qué cancela y qué no cancela en el cuarteto completo

La ley (21) se refiere deliberadamente a la clase \(n\equiv0\pmod4\). En
el cuarteto completo,

\[
 \begin{array}{c|c|c}
 n\bmod4&Q_n&[1+e^{t(Q_n+b_n)}]^{-1}\\ \hline
 0&-2^{n+1}+O(\log n)&1+o(1)\\
 1,3&4&(n+1)^{-t}(1+o(1))\\
 2&+2^{n+1}+O(\log n)&o(1).
 \end{array}
 \tag{27}
\]

Por tanto la media de Abel del falsificador satisface

\[
 \boxed{
 {1\over L(h)}\sum_{n\geq1}{e^{-hn}\over n}
 {1\over1+e^{t(Q_n+b_n)}}\longrightarrow{1\over4}.}
 \tag{28}
\]

En efecto, las clases \(1,3\) dan una serie convergente, la clase \(2\)
da \(O(1)\), y el defecto respecto de uno en la clase \(0\) también es
sumable. El numerador es, por tanto,

\[
 \sum_{4\mid n}{e^{-hn}\over n}+O_t(1)
 =-{1\over4}\log(1-e^{-4h})+O_t(1)
 ={1\over4}L(h)+O_t(1).
 \tag{28a}
\]

Las correcciones de microfrecuencia de las clases \(0\) y \(2\) tienen la
misma ley (21) y signos opuestos dentro de la fórmula de Fourier; se
cancelan en la media completa. Esta cancelación es importante: (21) no
autoriza a separar clases, ceros ni canales en una prueba para zeta. Lo que
sí prueba es que cualquier argumento que descarte la región
\(s<\exp(-h^{-\alpha})\) **antes** de demostrar esa cancelación pierde una
cantidad de orden uno en un falsificador admisible.

Así, la Abelización no convierte (11) en una estimación lineal ni permite
usar la continuación radial de `104_17`. El cuarteto tiene germen Abel
lineal positivo, media Fermi \(1/4\) y una capa no lineal anidada hasta
\(e^{-c/h}\).

---

## 5. Veredicto

**Probado.** La equivalencia Abel--Cesàro (4), el criterio de subsecuencia
(5), la forma prima--Laguerre Abel exacta (11), la fórmula unitaria con
orden de límites (13), la ley de capa (21) y el valor off-line (28).

**Ganancia.** El objetivo puede buscarse sobre una única sucesión radial
\(h_j\downarrow0\), y el observable aritmético exterior puede hacerse
infinito sin perder convergencia dominada. La variable correcta para una
auditoría de baja frecuencia es doblemente logarítmica, no \(s\), ni
\(s/h\), ni la tasa diagonal fija de `104_62`.

**No probado.** Una cota superior para (11), la desaparición de
\(\mathfrak A_t(h)\), A1 o RH. La capa (21) muestra que una estimación de
frecuencia truncada necesita una cancelación uniforme antes de truncar; no
construye esa cancelación para los pesos reales \(\Lambda(m)\).

---

## 6. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 log_abel_fermi_boundary_check.py
```

El checker ilustra numéricamente la tendencia al límite \(1/4\) de (28),
la ley armónica (22) y la aproximación de (21) mediante la transición exacta
\(J_n(0)=\tfrac12\tanh(tY_n/2)\). Las demostraciones de los límites están
en el texto; el muestreo no se usa como certificado.
