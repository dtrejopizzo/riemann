# 104_67 — Excursiones bilaterales y gate de la barrera superior

**Pregunta.** El criterio de bloques de `104_61` usa las excursiones
negativas. ¿La media Haar cero de los caracteres dominantes produce también
excursiones positivas y permite atacar RH mediante una cota **superior** más
accesible?

**Resultado.** Sí a la primera pregunta, no con las herramientas actuales a
la segunda. Si RH es falsa, \(\lambda_n\) tiene excursiones positivas y
negativas de la misma tasa exponencial máxima, cada una sobre un conjunto
sindético de densidad positiva. Por tanto cualquiera de las condiciones

\[
 \lambda_n\geq-e^{\sqrt n},\qquad
 \lambda_n\leq e^{\sqrt n},\qquad
 |\lambda_n|\leq e^{\sqrt n}                                \tag{1}
\]

en bloques consecutivos de longitud no acotada es, por sí sola, equivalente
a RH.

La barrera superior se traduce en una cota inferior muy débil para el
funcional prima--polo \(B_n=A_n-\lambda_n\). En el semiplano Euler esa cota
ya está disponible: `104_41` prueba \(|\mathcal B_{n,a}|\leq3n\) para
\(a\geq4\). Pero transportarla a \(a=1\) cruza exactamente los residuos de
los ceros a la derecha; esos residuos generan las excursiones positivas
recién probadas. Así la ruta superior llega al mismo gate de homotopía con
un signo distinto. No prueba A1 ni RH.

---

## 1. Teorema bilateral de modos dominantes

Suponga que RH es falsa. En la notación de `104_56`, existen

\[
 R>1,\qquad1<R_1<R,\qquad
 S(n)=\sum_{j=1}^Km_j\cos(n\phi_j),                         \tag{2}
\]

con \(m_j>0\), tales que

\[
 \lambda_n=C_0-R^nS(n)+O(n^2R_1^n+n^2).                   \tag{3}
\]

Los ángulos iguales y opuestos se han agrupado. Sea

\[
 H=\overline{\{n\phi:n\in\mathbb Z\}}\subset\mathbb T^K,
 \qquad F(x)=\sum_{j=1}^Km_j\cos x_j.                       \tag{4}
\]

Cada carácter de (4) es no trivial: un cero no trivial tiene ordenada no
nula. Por ortogonalidad de caracteres,

\[
 \int_HF\,d\mu_H=0.                                        \tag{5}
\]

Además \(F(0)=\sum_jm_j>0\), de modo que \(F\) no es idénticamente cero.
La continuidad y (5) obligan a que \(F\) tome también valores negativos.
Elija \(\eta>0\) tal que los abiertos

\[
 U_-:=\{F>2\eta\},\qquad U_+:=\{F<-2\eta\}                 \tag{6}
\]

sean no vacíos y tengan fronteras de medida de Haar cero. La rotación por
\(\phi\) es mínima y únicamente ergódica en \(H\). Por tanto sus conjuntos
de retornos

\[
 D_-:=\{n:n\phi\in U_-\},\qquad
 D_+:=\{n:n\phi\in U_+\}                                   \tag{7}
\]

tienen densidades naturales positivas. Ambos son sindéticos: las
traslaciones de cada abierto cubren \(H\), y una subcubierta finita acota
los tiempos de retorno.

La brecha \(R_1<R\) en (3) da el siguiente refuerzo de `104_56`.

**Teorema 1.1 (excursiones bilaterales).** Si RH es falsa, existen
\(c>0\), \(n_0\), \(R>1\) y dos conjuntos sindéticos \(D_+,D_-\), cada
uno de densidad natural positiva, tales que

\[
 \boxed{
 \lambda_n\geq cR^n\quad(n\in D_+),\qquad
 \lambda_n\leq-cR^n\quad(n\in D_-),}                       \tag{8}
\]

para \(n\geq n_0\). Los dos conjuntos pueden tener distintas densidades y
distintos gaps; no se afirma una constante universal.

La segunda desigualdad es `104_56`. La primera es el contenido nuevo:
proviene de los retornos a \(U_+\) en vez de los retornos a un entorno del
origen.

---

## 2. Criterios de bloques por arriba y bilateral

Bajo RH, el teorema de Lagarias da

\[
 \lambda_n=A_n+O(\sqrt n\log n)=O(n\log n).                 \tag{9}
\]

En particular, las tres desigualdades de (1) valen eventualmente. Si RH es
falsa, (8) vence \(e^{\sqrt n}\) en \(D_+\) y \(D_-\). Como ambos conjuntos
son sindéticos, ninguna de las tres desigualdades puede valer en bloques de
longitud no acotada.

**Corolario 2.1.** Son equivalentes:

1. RH;
2. existen bloques consecutivos de longitud no acotada en los que
   \(\lambda_n\leq e^{\sqrt n}\) para cada índice;
3. existen tales bloques con \(|\lambda_n|\leq e^{\sqrt n}\);
4. existen tales bloques con \(\lambda_n\geq-e^{\sqrt n}\).

La versión 4 es más débil que la barrera \(-1\) de `104_61`; se incluye
para exhibir la simetría de tasas. La versión 2 es lógicamente independiente
del signo de Li: no pide positividad, sino ausencia local de crecimiento
positivo exponencial.

El mismo argumento permite excepciones. Cada una de las barreras de (1),
fuera de un conjunto de densidad logarítmica superior cero, equivale a RH.
No basta que la excepción tenga densidad pequeña fija: las densidades de
retorno dependen de las fases dominantes.

---

## 3. Detectores de tasa positiva, negativa y bilateral

Para \(V>0\), defina

\[
\begin{aligned}
 \Psi^+_{V,n}(x)
   &=\min\!\left\{V,{1\over n}\log\max(1,x)\right\},\\
 \Psi^-_{V,n}(x)
   &=\min\!\left\{V,{1\over n}\log\max(1,-x)\right\},\\
 \Psi^{\pm}_{V,n}(x)
   &=\min\!\left\{V,{1\over n}\log\max(1,|x|)\right\}.
                                                               \tag{10}
\end{aligned}
\]

Sus identidades de capa son

\[
\begin{aligned}
 \Psi^+_{V,n}(x)&=\int_0^V{\bf1}_{\{x>e^{nv}\}}\,dv,\\
 \Psi^-_{V,n}(x)&=\int_0^V{\bf1}_{\{x<-e^{nv}\}}\,dv,\\
 \Psi^{\pm}_{V,n}(x)&=\int_0^V{\bf1}_{\{|x|>e^{nv}\}}\,dv.
                                                               \tag{11}
\end{aligned}
\]

Con \(H_X=\sum_{n\leq X}1/n\), ponga

\[
 \mathfrak R_V^\sigma(X)={1\over H_X}
 \sum_{n\leq X}{\Psi^\sigma_{V,n}(\lambda_n)\over n},
 \qquad\sigma\in\{+,-,\pm\}.                               \tag{12}
\]

**Teorema 3.1 (criterio bilateral acotado).** Para cada \(V>0\) y cada
\(\sigma\in\{+,-,\pm\}\),

\[
 \boxed{
 \mathrm {RH}\quad\Longleftrightarrow\quad
 \liminf_{X\to\infty}\mathfrak R_V^\sigma(X)=0.}           \tag{13}
\]

**Demostración.** Bajo RH, (9) implica

\[
 \Psi^+_{V,n}(\lambda_n),\qquad
 \Psi^{\pm}_{V,n}(\lambda_n)\ll{\log n\over n},
 \qquad \Psi^-_{V,n}(\lambda_n)=0.                         \tag{14}
\]

Como \(\sum_{n\geq2}(\log n)/n^2<\infty\), las medias (12) tienden a
cero. Bajo no-RH, (8) y la densidad logarítmica positiva de \(D_+\) y
\(D_-\) dan

\[
\begin{aligned}
 \liminf_X\mathfrak R_V^+(X)
   &\geq d_+\min(V,\tfrac12\log R)>0,\\
 \liminf_X\mathfrak R_V^-(X)
   &\geq d_-\min(V,\tfrac12\log R)>0,
                                                               \tag{15}
\end{aligned}
\]

y la versión bilateral domina ambas. \(\square\)

Para el cuarteto \(w=2i\) de `104_17`,

\[
 Q_{4k}=-2^{4k+1}+O(1),\qquad
 Q_{4k+2}=2^{4k+3}+O(1),\qquad
 Q_{2k+1}=4.                                                  \tag{16}
\]

Por tanto

\[
\boxed{
\begin{aligned}
 \mathfrak R_V^+(X)&\longrightarrow{1\over4}\min(V,\log2),\\
 \mathfrak R_V^-(X)&\longrightarrow{1\over4}\min(V,\log2),\\
 \mathfrak R_V^{\pm}(X)&\longrightarrow{1\over2}\min(V,\log2).
                                                               \tag{17}
\end{aligned}}
\]

Así el detector superior pasa el falsificador con el mismo margen que el
inferior; el bilateral ve las dos clases exponenciales.

---

## 4. Traducción prima--Laguerre de la barrera superior

Ponga, como en `104_60`,

\[
 B_n:=A_n-\lambda_n.                                        \tag{18}
\]

La barrera superior de (1) equivale exactamente a

\[
 \boxed{B_n\geq A_n-e^{\sqrt n}.}                           \tag{19}
\]

Como \(A_n=O(n\log n)\), el lado derecho es
\(-e^{\sqrt n}(1+o(1))\). Esto parece mucho más débil que A1: solo pide que
el funcional primo completo no tenga una cola negativa de tasa exponencial
fija.

Con el regulador de `104_61`,

\[
 B_n=\lim_{\varepsilon\downarrow0}
 \left\{
 \sum_{m\geq2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m)-p_n(\varepsilon)
 \right\}.                                                  \tag{20}
\]

La positividad de \(\Lambda(m)\) no da (19), porque
\(L_{n-1}^{(1)}\) cambia de signo y los dos términos de (20) son de orden
\(\varepsilon^{-n}\). Separarlos por valor absoluto vuelve a perder la
parte finita, exactamente como en `104_61`, `104_63` y `104_65`.

---

## 5. Por qué la cota fuerte del semiplano Euler no se transporta

La orientación superior sí encaja con una estimación ya probada. Para la
deformación completa prima--polo de `104_41`,

\[
 |\mathcal B_{n,a}|\leq3n\qquad(a\geq4).                    \tag{21}
\]

En particular, \(\mathcal B_{n,a}\geq-3n\), mucho más fuerte que (19).
El problema completo se concentra al mover \(a\downarrow1\). La fórmula
exacta es

\[
 B_n=\mathcal P_n+
 \sum_{\Re\rho>1/2}
 {m_\rho\mathcal F_n(w_\rho)\over\rho(\rho-1)},
 \qquad w_\rho=1-{1\over\rho}.                             \tag{22}
\]

La fase crítica \(\mathcal P_n\) no ve un cuarteto recíproco off-line; la
suma de residuos sí. En las clases donde ese cuarteto aporta
\(\lambda_n\gg R^n\), cambia \(B_n\) en \(-\lambda_n\ll-R^n\) y viola
(19). Por el Teorema 1.1, esas clases forman en general un conjunto
sindético, no una excepción dispersa que un criterio de bloques pueda
ignorar.

Por tanto transportar solo la cota inferior
\(\mathcal B_{n,a}\geq-3n\) hasta el borde probaría ya la barrera superior
equivalente a RH. La homotopía no se simplifica al cambiar el signo del
objetivo: el residuo que antes producía una excursión negativa ahora produce
la positiva.

---

## 6. Veredicto

**Probado.** Excursiones bilaterales sindéticas (8), criterios de bloques
superior y bilateral, detectores acotados (10)--(17), y traducción exacta de
la barrera superior al canal prima--polo.

**Ganancia.** Ya no es necesario atacar la positividad de Li: una cota
superior subexponencial en bloques también cerraría RH. La formulación
bilateral identifica la tasa exterior sin escoger signo.

**No-go distinto.** La cota inferior necesaria para \(B_n\) está probada en
el semiplano Euler con margen enorme, pero su transporte a \(a=1\) falla
exactamente por las excursiones positivas del nuevo Teorema 1.1. No es una
pérdida de constante ni de módulo; es la misma suma firmada de residuos.

**No probado.** Un bloque nuevo para la barrera superior, el límite cero de
cualquiera de (12), (19), A1 o RH.

---

## 7. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 two_sided_excursion_check.py
```

El checker usa `Fraction`. Verifica las dos clases exponenciales de (16),
la ausencia de bloques unilaterales de longitud cuatro en el cuarteto, y las
densidades armónicas \(1/4,1/4,1/2\) de (17). La prueba de retornos
sindéticos se encuentra en §1 y no depende de muestreo.
