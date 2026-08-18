# 104_106 — Promedios de bloque, residuos y gate exacto de selectores

**Pregunta.** ¿Se puede combinar la relajación por bloques de `104_67`
con la fórmula de residuos de `104_33`--`104_41`, promediando el defecto
de transporte sobre grados consecutivos?

**Resultado.** La combinación tiene una forma cerrada, pero una media
lineal firmada no produce un bloque bueno. Para cualquier filtro finito de
grados, cada cero derecho se transforma mediante el mismo polinomio del
filtro evaluado en \(w_\rho\) y \(w_\rho^{-1}\). En particular, caja,
Cesàro triangular y Fejér conservan el modo exterior; solo cambian su fase
y su amplitud.

La operación correcta para la barrera superior de `104_67` es no lineal:
la parte positiva de \((-\mathscr R_n)\), o equivalentemente un supremo sobre
**todos** los selectores del bloque. Se prueba el criterio exacto

\[
 \mathrm {RH}\quad\Longleftrightarrow\quad
 {e^{-\sqrt{M_L}}\over L}
 \sum_{n=L^2}^{L^2+L-1}(-\mathscr R_n)_+\longrightarrow0,
 \qquad M_L=L^2+L-1.                                    \tag{1}
\]

Aquí \(\mathscr R_n\) es la suma firmada de residuos interiores de
`104_41`, no un resto estimado. La equivalencia (1) localiza con precisión
el target que una estimación aritmética tendría que acotar, pero no lo
acota para los pesos reales \(\Lambda(m)\). El cuarteto racional
\(w=i/2\) demuestra exactamente que sustituir la parte positiva por una
media firmada es inválido incluso en bloques arbitrariamente lejanos.

Este documento no prueba (1) por aritmética, A1 ni RH.

---

## 1. El filtro de bloque exacto

Para un cero no trivial \(\rho\) con \(\Re\rho>1/2\), ponga

\[
 w_\rho=1-{1\over\rho},\qquad |w_\rho|<1.
\]

El defecto de transporte de `104_33`, sumado sobre ambos signos de la
ordenada, es

\[
 \mathscr R_n:=
 \sum_{\Re\rho>1/2}
 {m_\rho\,\mathcal F_n(w_\rho)\over\rho(\rho-1)}.
                                                               \tag{2}
\]

La suma incluye conjugados y es real. La identidad elemental ya usada en
`104_33` es

\[
 \boxed{
 {\mathcal F_n(w_\rho)\over\rho(\rho-1)}
 =w_\rho^n+w_\rho^{-n}-2.}                              \tag{3}
\]

Sea ahora \(I=\{N,N+1,\ldots,N+L-1\}\), sean
\(a_0,\ldots,a_{L-1}\in\mathbb R\), y defina

\[
 A(z)=\sum_{j=0}^{L-1}a_jz^j,qquad A(1)=\sum_ja_j.       \tag{4}
\]

Como el filtro es finito y la serie de residuos converge absolutamente en
cada grado fijo, (3) puede sumarse término a término.

**Lema 1.1 (identidad filtro--residuos).** Se tiene

\[
 \boxed{
 \sum_{j=0}^{L-1}a_j\mathscr R_{N+j}
 =\sum_{\Re\rho>1/2}m_\rho
 \left\{
 w_\rho^N A(w_\rho)
 +w_\rho^{-N}A(w_\rho^{-1})-2A(1)
 \right\}.}                                             \tag{5}
\]

No aparece un signo nuevo al promediar: el modo creciente
\(w_\rho^{-N}\) sigue presente y queda multiplicado por
\(A(w_\rho^{-1})\).

### 1.1 Caja, Cesàro y Fejér

Escriba

\[
 G_L(z)={1-z^L\over L(1-z)}={1\over L}\sum_{j=0}^{L-1}z^j. \tag{6}
\]

La media de caja de la contribución (3) de un cero es

\[
 \boxed{
 w^NG_L(w)+w^{-N}G_L(w^{-1})-2.}                         \tag{7}
\]

Para la media triangular unilateral, con pesos
\(2(L-j)/[L(L+1)]\), el polinomio es

\[
 T_L(z)={2\over L(L+1)}
 {L-(L+1)z+z^{L+1}\over(1-z)^2},                         \tag{8}
\]

y la respuesta es \(w^NT_L(w)+w^{-N}T_L(w^{-1})-2\).

Finalmente, si \(N\ge L\), la media simétrica de Fejér usa

\[
 K_L(z)={1\over L^2}\sum_{|j|<L}(L-|j|)z^j
 ={\mathcal F_L(z)\over L^2}=K_L(z^{-1}).                \tag{9}
\]

Por tanto

\[
 \boxed{
 \sum_{|j|<L}{L-|j|\over L^2}
 \{w^{N+j}+w^{-N-j}-2\}
 =K_L(w)(w^N+w^{-N})-2.}                                 \tag{10}
\]

La no negatividad de \(K_L(e^{i\theta})\) solo vale en el círculo. Para
\(|w|\ne1\), \(K_L(w)\) es en general complejo y no orienta (10).

---

## 2. La parte de frontera es subexponencial

Sea \(\lambda_n^{\rm crit}\) la contribución de los ceros situados en la
línea crítica, agrupados por conjugación:

\[
 \lambda_n^{\rm crit}
 =2\sum_{\substack{\rho=1/2+i\gamma\\\gamma>0}}
 m_\rho\{1-\cos(n\theta_\rho)\},
 \qquad
 1-{1\over\rho}=e^{i\theta_\rho}.                       \tag{11}
\]

Separando la fórmula de Li por órbitas críticas y cuartetos exteriores,
(3) da la identidad exacta

\[
 \boxed{\lambda_n=\lambda_n^{\rm crit}-\mathscr R_n.}  \tag{12}
\]

Además,

\[
 \boxed{0\le\lambda_n^{\rm crit}\ll n\log(n+2).}       \tag{13}
\]

En efecto, los ceros críticos con \(\gamma\le n\) aportan a lo sumo
cuatro cada uno y \(N(n)\ll n\log(n+2)\). Para \(\gamma>n\),

\[
 |\theta_\rho|=2\arctan{1\over2\gamma}\le{1\over\gamma},
 \qquad
 2\{1-\cos(n\theta_\rho)\}\le {n^2\over\gamma^2}.
\]

La sumación parcial de Riemann--von Mangoldt da

\[
 \sum_{\gamma>n}{m_\rho\over\gamma^2}
 \ll {\log(n+2)\over n},
\]

lo cual prueba (13). Así todo crecimiento exponencial positivo de
\(\lambda_n\) está en la parte negativa de \(\mathscr R_n\); la frontera
crítica no puede producirlo ni cancelarlo.

---

## 3. Qué promedio sí sería suficiente

La parte positiva posee la dualidad finita exacta

\[
 \boxed{
 \sum_{j=0}^{L-1}(-\mathscr R_{N+j})_+
 =\sup_{0\le a_j\le1}
 \left\{-\sum_{j=0}^{L-1}a_j\mathscr R_{N+j}\right\}.}   \tag{14}
\]

Insertando (5), el miembro derecho es un supremo sobre todos los
polinomios selectores (A(z)=\sum a_jz^j), no la evaluación de un único
polinomio caja o Fejér. De modo análogo,

\[
 \max_{0\le j<L}(-\mathscr R_{N+j})
 =\sup_{\substack{a_j\ge0\\\sum a_j=1}}
 \left\{-\sum_ja_j\mathscr R_{N+j}\right\}.             \tag{15}
\]

Por (12)--(13), un certificado local que produce un bloque completo de la
barrera superior de `104_67` es

\[
 \boxed{
 \sum_{n=N}^{N+L-1}(-\mathscr R_n)_+
 \le {1\over2}e^{\sqrt N}.}                              \tag{16}
\]

En efecto, sea \(M=N+L-1\) y suponga
\(M\log(M+2)=o(e^{\sqrt N})\). Para \(N\) suficientemente grande,
\(\lambda_n^{\rm crit}\le e^{\sqrt N}/2\) en todo el bloque. La cota
sobre la suma de partes positivas en (16) implica, en particular, que cada
sumando es a lo sumo \(e^{\sqrt N}/2\). Entonces (12) da
\(\lambda_n\le e^{\sqrt n}\) grado por grado. La hipótesis sobre \(M\)
vale, en particular, para \(N=L^2\) y longitud \(L\).

La formulación más débil que aún detecta todo cero exterior es (1).

**Teorema 3.1 (criterio de bloque positivo).** Con

\[
 I_L=\{L^2,\ldots,L^2+L-1\},\qquad M_L=L^2+L-1,
\]

se tiene la equivalencia (1). Más precisamente, si RH es falsa, el miembro
izquierdo de (1) tiende a \(+\infty\).

*Demostración.* Bajo RH no hay ceros con \(\Re\rho>1/2\), luego
\(\mathscr R_n=0\) para todo \(n\).

Si RH es falsa, el Teorema 1.1 de `104_67` proporciona \(c>0\), \(R>1\)
y un conjunto sindético \(D_+\) tales que

\[
 \lambda_n\ge cR^n\qquad(n\in D_+)
\]

desde un índice fijo. Por (12)--(13), reduciendo \(c\) si hace falta,

\[
 (-\mathscr R_n)_+\ge {c\over2}R^n\qquad(n\in D_+).      \tag{17}
\]

Sea \(G\) un gap de sindeticidad. Para \(L\ge G\), los últimos \(G\)
lugares de \(I_L\) contienen un \(d_L\in D_+\), de modo que

\[
 {e^{-\sqrt{M_L}}\over L}
 \sum_{n\in I_L}(-\mathscr R_n)_+
 \ge {c\over2L}R^{M_L-G}e^{-\sqrt{M_L}}\longrightarrow\infty.
                                                               \tag{18}
\]

Esto prueba la dicotomía. \(\square\)

Para una excepción de densidad logarítmica cero basta, por la misma razón,
probar

\[
 {1\over\log X}\sum_{n\le X}
 {(-\mathscr R_n)_+\over n e^{\sqrt n}}\longrightarrow0. \tag{19}
\]

Markov aplicado a (19) muestra que
\(\{n:(-\mathscr R_n)_+>e^{\sqrt n}/2\}\) tiene densidad logarítmica
superior cero; (12)--(13) y `104_67` cierran entonces RH. Bajo no-RH, (17)
prueba que el miembro de (19) no solo deja de tender a cero, sino que es no
acotado.

---

## 4. Por qué la media firmada no basta

Considere el cuarteto racional de `104_41`, parametrizado por

\[
 w={i\over2},\qquad
 \rho={1\over1-w}={4+2i\over5}.
\]

Su contribución al coeficiente de Li es

\[
 q_n=4-2\Re(w^n+w^{-n})=-2\Re\{w^n+w^{-n}-2\}.           \tag{20}
\]

Para \(N\equiv2\pmod4\),

\[
 q_N=4+2(2^N+2^{-N})>2^{N+1},                            \tag{21}
\]

pero la caja de cuatro grados satisface

\[
 \boxed{
 \sum_{j=0}^3q_{N+j}
 =16-6\,2^N+{3\over2}\,2^{-N}<0
 \qquad(N\ge2, N\equiv2\!\!\pmod4).}                 \tag{22}
\]

Así hay bloques arbitrariamente lejanos cuya **media firmada** cumple una
cota superior incluso negativa, aunque el primer grado del mismo bloque
tiene una excursión positiva exponencial. El promedio no ha producido un
bloque bueno; el grado malo fue pagado por una excursión del signo opuesto.

El fenómeno no es especial a la caja. Para cualquier filtro finito no nulo
con pesos reales no negativos, sea \(j_*\) el mayor índice con
\(a_{j_*}>0\). Si \(w=re^{i\theta}\) y \(r\downarrow0\), el término
dominante de (5) es

\[
 a_{j_*}r^{-N-j_*}e^{-i(N+j_*)\theta}.                   \tag{23}
\]

Eligiendo dos ángulos no reales con cosenos de signos opuestos, (23) toma
ambos signos y domina todos los demás términos. Ambos puntos corresponden
a ceros con \(\Re\rho>1/2\). Por tanto ningún filtro lineal fijo posee una
orientación unilateral universal sobre los cuartetos exteriores. Caja,
Cesàro y Fejér no son excepciones.

Este falsificador no conserva el producto de Euler exacto de \(\zeta\).
Su función es lógica: prueba que el paso «media firmada pequeña
\(\Rightarrow\) bloque bueno» es falso antes de usar aritmética. Una prueba
específica de los pesos reales debe controlar (14), no solamente (5) para
un selector prefijado.

---

## 5. Consecuencia para la homotopía de `104_41`

En el semiplano Euler,

\[
 |\mathcal B_{n,a}|\le3n\qquad(a\ge4).
\]

Por linealidad, para cualquier selector \(0\le a_j\le1\),

\[
 \left|\sum_ja_j\mathcal B_{N+j,a}\right|
 \le3\sum_ja_j(N+j).                                    \tag{24}
\]

Al transportar \(a\downarrow1\), el defecto es exactamente el miembro
derecho de (5). Para deducir (14) habría que transportar (24)
**uniformemente en el cubo completo** \([0,1]^L\). El selector extremo se
adapta a los signos de los residuos; un único filtro caja/Fejér no lo
controla.

Ésta es la combinación precisa de `104_33`, `104_41` y `104_67`:

* la frontera aporta solo \(O(n\log n)\);
* la suma firmada de residuos tiene la fórmula filtrada (5);
* la relajación por bloques permite reemplazar el control de todos los
  grados por (1), (16) o (19);
* pero cualquiera de esos targets exige la parte positiva, equivalente al
  supremo de selectores (14).

No queda una inferencia desde un promedio lineal. El teorema aritmético que
falta es una cota uniforme sobre (14) para los residuos producidos por los
pesos ordinarios \(\Lambda(m)\).

---

## 6. Veredicto

**Probado:** identidad exacta de filtro (5); fórmulas caja, Cesàro y Fejér
(7)--(10); descomposición
\(\lambda_n=\lambda_n^{\rm crit}-\mathscr R_n\) con
\(0\le\lambda_n^{\rm crit}\ll n\log n\); dualidad de selectores
(14)--(15); criterio determinista (1); y falsificador racional (21)--(22).

**Ganancia:** la propuesta de promediar el defecto queda separada en dos
objetos que no deben confundirse. La media firmada es un solo filtro y no
basta. La media de la parte positiva sí es equivalente a RH y admite la
fórmula variacional exacta (14)--(5).

**Descartado:** concluir bloques completos o excepción de densidad cero a
partir de una media signed de caja, Cesàro o Fejér.

**No probado:** una cota aritmética para el supremo (14), (1), A1 o RH.

## 7. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 block_residue_selector_gate_check.py
```

El checker usa `Fraction` y racionales gaussianos. Verifica (3), (5),
(7)--(10), la dualidad finita (14)--(15), y el falsificador (21)--(22) en
una familia de bloques arbitrariamente lejanos. No certifica el límite
aritmético (1).
