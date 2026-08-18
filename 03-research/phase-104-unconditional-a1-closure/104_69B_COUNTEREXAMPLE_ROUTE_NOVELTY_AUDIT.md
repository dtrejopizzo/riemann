# 104_69B — Auditoría de antecedentes de la ruta Fermi por contraejemplo

## Veredicto ejecutivo

La búsqueda primaria dirigida no localizó una fuente que contenga la forma
exacta

\[
 a_n={1\over1+(n+1)e^{\lambda_n}},\qquad
 I_L=\{L^2,\ldots,L^2+L-1\},                              \tag{1}
\]

\[
 \sum_{n\in I_L}a_n\longrightarrow0,
 \qquad
 \prod_{n\in I_L}(1-a_n)\longrightarrow1,                \tag{2}
\]

ni la diagonal prima--Laguerre

\[
 \varepsilon_X=e^{-X/100},\qquad
 \varepsilon_L=e^{-(L^2+L-1)/100}=e^{-(1+o(1))L^2/100}.  \tag{3}
\]

Esto **no prueba prioridad**. El nivel de atribución que permiten las fuentes
revisadas es más modesto:

1. la capa exterior dominante y la negatividad exponencial infinitas veces
   bajo no-RH son conocidas desde Bombieri--Lagarias y están escritas en forma
   trigonométrica explícita por Bucur--Ernvall-Hytönen--Odžak--Smajlović;
2. el posible contenido sustantivo propio es el refuerzo de `104_56` desde
   «infinitas veces» hasta un conjunto de densidad natural positiva y
   sindético, siempre que esa prueba permanezca íntegra;
3. la logística Fermi, el producto finito, la ventana cuadrática y la diagonal
   Euler son *repackagings* o corolarios exactos de ese refuerzo, no una nueva
   estimación sobre los ceros;
4. la equivalencia entre las medias logarítmicas de Cesàro y Abel pertenece a
   la teoría clásica de sumabilidad. Lo no localizado es su aplicación al
   detector Fermi de los coeficientes de Li, no el teorema de sumabilidad.

Por tanto `104_68`--`104_69` deben presentarse como criterios acotados y
normalizaciones finitas de la ruta del modo exterior. No prueban A1 ni RH y no
aportan información nueva sobre la localización de ceros.

---

## 1. Objetos auditados

Además de (1)--(3), se buscaron las dos medias usadas en `104_64` y `104_69`:

\[
 \mathfrak F(X)
 ={1\over H_X}\sum_{n\le X}{a_n\over n},
 \qquad H_X=\sum_{n\le X}{1\over n},                     \tag{4}
\]

\[
 L(h)=-\log(1-e^{-h}),\qquad
 \mathfrak A(h)={1\over L(h)}
 \sum_{n\ge1}{e^{-hn}a_n\over n}.                       \tag{5}
\]

También se auditó la expansión finita llamada «polímero»:

\[
\begin{aligned}
 P_L^{-1}
 &=\prod_{n\in I_L}(1+z_n)\\
 &=\sum_{S\subseteq I_L}
 \exp\!\left(-\sum_{n\in S}
       \{\lambda_n+\log(n+1)\}\right),
 \qquad z_n={e^{-\lambda_n}\over n+1}.                  \tag{6}
\end{aligned}
\]

La identidad (6) es la expansión elemental de un producto finito. Su lift
prima--Laguerre conserva conjuntamente polo, bloque arquimediano, primos y
potencias primas, pero no crea una interacción nueva: el producto vuelve a
factorizar grado por grado.

---

## 2. Tabla de antecedentes

| objeto o afirmación | clasificación | antecedente y distinción exacta |
|---|---|---|
| Criterio \(\mathrm{RH}\Longleftrightarrow\lambda_n\ge0\) para todo \(n\) | **conocido** | Li, JNT 65 (1997), 325--333, [DOI 10.1006/jnth.1997.2137](https://doi.org/10.1006/jnth.1997.2137) |
| Multiconjunto abstracto, condición inferior subexponencial y excursiones negativas exponenciales i.o. | **conocido** | Bombieri--Lagarias, JNT 77 (1999), 274--287, [DOI 10.1006/jnth.1999.2392](https://doi.org/10.1006/jnth.1999.2392) |
| Término dominante \(-2R^n\sum_j\cos(n\phi_j)\) para \(R>1\) | **conocido** | Bucur--Ernvall-Hytönen--Odžak--Smajlović, ec. (3.9), [PDF primario](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9D6498CFDB802707E1A0EDFFE5B81C34/S1461157016000115a.pdf/on-a-li-type-criterion-for-zerofree-regions-of-certain-dirichlet-series-with-real-coefficients.pdf), [DOI 10.1112/S1461157016000115](https://doi.org/10.1112/S1461157016000115) |
| Criterios \(\tau\)-Li para semiplanos libres de ceros | **conocido** | Freitas, JLMS 73 (2006), 399--414, [arXiv:math/0507368](https://arxiv.org/abs/math/0507368), [DOI 10.1112/S0024610706022599](https://doi.org/10.1112/S0024610706022599) |
| Intervalos finitos de índices que certifican regiones libres de ceros | **adyacente** | Palojärvi, Albanian J. Math. 14 (2020), 47--77, [arXiv:1807.01506](https://arxiv.org/abs/1807.01506), [PDF de revista](https://www.albanian-j-math.com/archives/2020-04.pdf). Sus intervalos explícitos \([N_1,N_2]\) no son las ventanas móviles \(I_L\) ni forman un criterio límite por productos |
| Dicotomía asintótica \(n(A\log n+B)\) frente a oscilación no temperada | **conocido** | Voros, MPAG 9 (2006), 53--63, [arXiv:math/0506326](https://arxiv.org/abs/math/0506326), [DOI 10.1007/s11040-005-9002-8](https://doi.org/10.1007/s11040-005-9002-8) |
| Criterio global \(\ell^2\) para el error de Keiper--Li | **adyacente** | Arias de Reyna, FACA 45 (2011), 7--21, [PDF institucional](https://idus.us.es/bitstream/handle/11441/47018/Asymptotics%20of%20Keiper-Li%20coefficients.pdf?sequence=1), [DOI 10.7169/facm/1317045228](https://doi.org/10.7169/facm/1317045228) |
| Métodos logarítmicos \(\ell\), \(L\) y medias móviles | **conocido como sumabilidad** | Bingham--Gashi, JMAA 421 (2015), 1790--1802, [arXiv:1408.1301](https://arxiv.org/abs/1408.1301), [PDF de autor](https://www.ma.imperial.ac.uk/~bin06/Papers/BiG1.pdf), [DOI 10.1016/j.jmaa.2014.08.031](https://doi.org/10.1016/j.jmaa.2014.08.031) |
| Negatividad exponencial en un conjunto de densidad positiva y sindético | **no localizada explícitamente** | refuerzo topológico-dinámico de `104_56` sobre el término dominante conocido; no es una nueva cota de ceros y no se reclama prioridad |
| Detector fijo \(a_n=[1+(n+1)e^{\lambda_n}]^{-1}\) equivalente a RH | **no localizado exactamente** | corolario funcional de la positividad bajo RH y del refuerzo densidad/sindeticidad bajo no-RH |
| Ventanas deterministas \([L^2,L^2+L)\) | **no localizadas exactamente** | corolario de sindeticidad más \(|I_L|/\min I_L\to0\); Palojärvi es solo adyacente |
| Producto \(P_L\) y expansión de polímeros | **no localizados exactamente; repackaging algebraico** | \(P_L\to1\Longleftrightarrow\sum_{I_L}a_n\to0\) y (6) son identidades elementales para números no negativos |
| Diagonal \(\varepsilon_X=e^{-X/100}\), o \(e^{-cL^2}\) en bloques | **no localizada exactamente; corolario técnico** | procede de la cota uniforme \(|\lambda_{n,\varepsilon}-\lambda_n|\ll n\varepsilon r^{-n}\), no es un criterio RH independiente |
| Aplicación Li--Fermi de las medias log-Cesàro/Abel | **no localizada exactamente** | la maquinaria de sumabilidad es clásica; la sustitución \(s_n=a_n\) y el lift prima--Laguerre son la capa específica del proyecto |

«No localizada» significa exclusivamente «no apareció en esta búsqueda primaria
dirigida». No significa que no exista en toda la literatura.

---

## 3. La ruta de contraejemplo que sí tiene antecedente directo

### 3.1 Li y Bombieri--Lagarias

Los coeficientes completos son

\[
 \lambda_n=\sum_\rho
 \left[1-\left(1-{1\over\rho}\right)^n\right].           \tag{7}
\]

Li prueba que su no negatividad en todos los grados equivale a RH.
Bombieri--Lagarias extiende el mecanismo a multiconjuntos abstractos y prueba
una condición unilateral subexponencial equivalente a la localización. Cuando
existe un punto transformado de módulo mayor que uno, la prueba separa los
modos de radio exterior máximo y obtiene valores negativos exponenciales
infinitas veces mediante aproximación diofántica simultánea.

Ésta es la fuente matemática de la dirección no-RH de `104_56`--`104_69`.
No debe presentarse el mero hecho de que existan excursiones exponenciales como
un resultado nuevo.

### 3.2 Forma trigonométrica publicada

Para los coeficientes \(\tau\)-Li

\[
 \lambda_F(n,\tau)
 =\sum_\rho\left[1-\left({\rho\over\rho-\tau}\right)^n\right], \tag{8}
\]

Bucur et al. prueban que una región libre de ceros equivale, entre otras
formas, a

\[
 \lambda_F(n,\tau)>-c(\delta)e^{\delta n}
 \quad\hbox{para todo }\delta>0,                          \tag{9}
\]

y a una condición de radio espectral

\[
 \limsup_{n\to\infty}|\lambda_F(n+1,\tau)|^{1/n}\le1.    \tag{10}
\]

Si

\[
 R=\max_\rho\left|{\rho\over\rho-\tau}\right|>1,       \tag{11}
\]

su ecuación (3.9) contiene el bloque dominante

\[
 -2R^n\sum_{j=1}^k\cos(n\phi_j),                         \tag{12}
\]

más radios estrictamente menores y términos polinómicos. Aplican aproximación
simultánea para obtener negatividad exponencial infinitas veces. No enuncian
allí densidad positiva, sindeticidad, el detector Fermi ni las ventanas (1).

### 3.3 Qué puede agregar `104_56`

El paso adicional de `104_56` considera el cierre compacto

\[
 H=\overline{\{n\alpha:n\in\mathbb Z\}}\subset\mathbb T^k \tag{13}
\]

y un abierto de nivel regular

\[
 U_\eta=\left\{x\in H:\sum_{j=1}^k\cos x_j>\eta\right\}. \tag{14}
\]

La minimalidad da retornos sindéticos; la única ergodicidad y la elección de
un nivel con frontera de Haar nula dan densidad natural
\(\mu_H(U_\eta)>0\). Si todos los detalles de ese argumento son correctos,
éste es el salto potencialmente sustantivo respecto de las fuentes primarias:

\[
 \neg\mathrm{RH}\Longrightarrow
 \lambda_n\le-cR^n
 \quad\hbox{en un conjunto sindético de densidad positiva}. \tag{15}
\]

Las ventanas (1) y la logística son consecuencias cortas de (15), no una
nueva demostración del modo exterior.

---

## 4. Palojärvi: intervalos finitos, pero no bloques cuadráticos

Palojärvi usa (8) y produce números explícitos \(N_1,N_2\) tales que la no
negatividad de \(\Re\lambda_F(n,\tau)\) para
\(N_1\le n\le N_2\) excluye ceros con

\[
 \left|{\rho\over\rho-\tau}\right|\ge R.                \tag{16}
\]

También da intervalos explícitos \([n_1,n_2]\) en los que un coeficiente
negativo fuerza la existencia de un cero en la región exterior estudiada.
Por tanto es un antecedente directo de **usar varios índices consecutivos**.

No duplica (1)--(2): sus extremos dependen de los parámetros de la región
libre de ceros, el enunciado es finito y computacional, y no aparece una
familia cofinal de intervalos deterministas cortos ni una suma o producto
Fermi sobre ellos.

---

## 5. Bingham--Gashi: la capa log-Cesàro/Abel es clásica

Bingham--Gashi definen el método logarítmico \(\ell\) por

\[
 {1\over\log n}\sum_{i=0}^n{s_i\over i+1}\longrightarrow s, \tag{17}
\]

y el método logarítmico de Abel \(L\) por

\[
 {1\over-\log(1-x)}
 \sum_{i=0}^\infty{s_i\over i+1}x^{i+1}\longrightarrow s
 \qquad(x\uparrow1).                                     \tag{18}
\]

Introducen además la media logarítmica móvil

\[
 {1\over\log n}
 \sum_{n^{1/\lambda}<i\le n}{s_i\over i+1}
 \longrightarrow(1-\lambda^{-1})s,\qquad\lambda>1,       \tag{19}
\]

y prueban su equivalencia con \(\ell\), junto con resultados Abelianos y
Tauberianos. Tomando \(x=e^{-h}\), (18) tiene exactamente el normalizador
de (5), salvo el corrimiento inofensivo de índices.

Para \(0\le a_n\le1\), la equivalencia del **límite cero** usada en
`104_64` también se obtiene directamente por positividad: la dirección
Cesàro--Abel es Abeliana y la inversa sigue tomando \(h=1/X\), pues
\(e^{-hn}\ge e^{-1}\) para \(n\le X\). Por ello no debe reclamarse como
nuevo el puente (4)--(5).

La especialización

\[
 s_n=a_n={1\over1+(n+1)e^{\lambda_n}}                    \tag{20}
\]

y su representación prima--Laguerre regulada no fueron localizadas en las
fuentes revisadas. Son una aplicación específica, no una extensión de la
teoría Tauberiana.

---

## 6. Otros criterios promedio adyacentes

Arias de Reyna usa la normalización de Keiper, en la que los coeficientes de
Li son \(m\lambda_m^{K}\), y escribe

\[
 \lambda_m^{K}
 ={1\over2}\{\log m+\gamma-\log(2\pi)-1\}+y_m.           \tag{21}
\]

Prueba

\[
 \mathrm{RH}\quad\Longleftrightarrow\quad(y_m)\in\ell^2. \tag{22}
\]

Esto muestra que condiciones globales sobre toda la sucesión Li ya existen.
No implica ni contiene el criterio Fermi: (22) mide error cuadrático respecto
de una asintótica, mientras (4) aplica una no linealidad acotada que satura las
excursiones negativas.

---

## 7. Diagonal Euler y producto: alcance correcto

La diagonal (3) procede del estimado ya probado en `104_66`--`104_69`

\[
 |\lambda_{n,\varepsilon}-\lambda_n|
 \le 2Mn\varepsilon r^{-n},\qquad r={199\over200}.        \tag{23}
\]

Para todos los grados \(n\le X\), elegir \(\varepsilon_X=e^{-X/100}\)
da

\[
 \sup_{n\le X}|\lambda_{n,\varepsilon_X}-\lambda_n|
 \le2MXe^{-\eta X},
 \qquad \eta={1\over100}-\log{200\over199}>0.            \tag{24}
\]

En la ventana (1), \(X=L^2+L-1\), y aparece la escala
\(e^{-cL^2}\). Esta elección hace simultáneamente convergentes las fórmulas
Euler de una cantidad finita de grados. No añade una nueva implicación sobre
ceros y no debe anunciarse como criterio independiente.

Análogamente, la equivalencia entre suma y producto usa solo

\[
 {z\over1+z}\le\log(1+z)\le z\qquad(z\ge0),              \tag{25}
\]

y la desigualdad de unión

\[
 1-\sum_{n\in I_L}a_n
 \le\prod_{n\in I_L}(1-a_n)\le1.                        \tag{26}
\]

La terminología de polímero es útil para conservar los canales aritméticos en
la fórmula exacta, pero no debe confundirse con una nueva estimación colectiva.

---

## 8. Alcance de la búsqueda y lenguaje editorial

Hasta el 26 de julio de 2026 se buscaron en arXiv, revistas y repositorios
institucionales combinaciones de *Li/Keiper coefficients* con
*logistic*, *Fermi*, *Fermi--Dirac*, *partition function*, *polymer*,
*product criterion*, *syndetic*, *positive density*, *natural density*,
*logarithmic density*, *arbitrarily long blocks*, *moving blocks*,
*logarithmic Cesàro*, *logarithmic Abel* y regularizaciones diagonales. Se
revisaron los textos primarios citados arriba y sus referencias próximas.

La redacción recomendada para un artículo es:

> Partiendo del término exterior dominante conocido de
> Bombieri--Lagarias y Bucur et al., un argumento de recurrencia en un toro
> compacto refuerza, aparentemente de forma no registrada en las fuentes
> revisadas, las excursiones negativas a un conjunto sindético de densidad
> positiva. Los criterios Fermi, de bloques deterministas, producto finito y
> diagonal Euler son corolarios y normalizaciones exactas de ese refuerzo.
> La equivalencia log-Cesàro/Abel es una instancia de sumabilidad clásica.

No debe usarse «primer criterio», «nuevo en la literatura» ni una afirmación
de prioridad basada solo en esta búsqueda. Una reclamación editorial de
novedad exigiría una búsqueda profesional adicional y consulta a
especialistas.
