# 104_99 — Eratóstenes exacto, identidad de paridad y gate energético

## Resultado

Sea

\[
 P(z)=\prod_{p\le z}p,
 \qquad
 \Phi(x,z)=\#\{1\le n\le x:(n,P(z))=1\},
 \tag{1}
\]

donde \(x\ge2\) es real y las funciones de conteo usan
\(n\le\lfloor x\rfloor\). La inclusión--exclusión de Eratóstenes da

\[
 \Phi(x,z)=\sum_{d\mid P(z)}\mu(d)\left\lfloor{x\over d}\right\rfloor.
 \tag{2}
\]

En el corte natural \(z=\sqrt x\), los únicos enteros contados son \(1\)
y los primos de \((\sqrt x,x]\). Por tanto

\[
 \boxed{
 \pi(x)=\pi(\sqrt x)-1+
 \sum_{d\mid P(\sqrt x)}\mu(d)
       \left\lfloor{x\over d}\right\rfloor.}
 \tag{3}
\]

Poniendo

\[
 V(z)=\prod_{p\le z}\left(1-{1\over p}\right),
 \qquad
 R_E(x,z)=\sum_{d\mid P(z)}\mu(d)
 \left(\left\lfloor{x\over d}\right\rfloor-{x\over d}\right),
 \tag{4}
\]

se obtiene la identidad firmada completa

\[
 \boxed{
 \pi(x)-\mathrm{Li}_2(x)
 =R_E(x,\sqrt x)+xV(\sqrt x)+\pi(\sqrt x)-1
  -\mathrm{Li}_2(x).}
 \tag{5}
\]

No se tomó valor absoluto y no se separaron las torres: toda la
correlación de Eratóstenes permanece en \(R_E\). Sin embargo, (5) no da
una estimación nueva. Al insertarla en la energía de `104_94`, la cota
que falta es exactamente

\[
 \sum_{m\le N}{{R_E(m,\sqrt m)+mV(\sqrt m)+\pi(\sqrt m)-1
 -\mathrm{Li}_2(m)}^2\over m(m+1)}=N^{o(1)}.
 \tag{6}
\]

El término \(\pi(\sqrt m)-1\) tiene energía finita, pero la cancelación
entre \(R_E(m,\sqrt m)\), \(mV(\sqrt m)\) y
\(\mathrm{Li}_2(m)\) conserva íntegro el contenido de RH.

Hay además una identidad exacta que localiza la barrera de paridad dentro
del residuo completo. Sea

\[
 \lambda_L(n)=(-1)^{\Omega(n)},
 \qquad
 L(y)=\sum_{n\le y}\lambda_L(n),
 \tag{7}
\]

con \(L(y)=L(\lfloor y\rfloor)\). Entonces

\[
 \boxed{
 \sum_{d\mid P(\sqrt x)}L(x/d)
 =1+\pi(\sqrt x)-\pi(x).}
 \tag{8}
\]

En particular, quitando de nuevo el bloque de energía finita,

\[
 \boxed{
 \mathrm {RH}\Longleftrightarrow
 \sum_{m\le N}{1\over m(m+1)}
 \left\{\mathrm{Li}_2(m)+
 \sum_{d\mid P(\sqrt m)}L(m/d)\right\}^{\!2}=N^{o(1)}.}
 \tag{9}
\]

La equivalencia (9) no es una prueba de su lado derecho. Expone qué debe
cancelarse en una prueba por Eratóstenes: la suma **completa**, hasta el
nivel \(d\asymp x\), de los primitivos de Liouville.

Finalmente, toda truncación estable a nivel
\(D\le x^{1-\eta}\), con \(\eta>0\) fijo, queda descartada por un
falsificador cuantitativo. Las dos sucesiones no negativas

\[
 a_n^+=1+\lambda_L(n),
 \qquad
 a_n^-=1-\lambda_L(n)
 \tag{10}
\]

tienen datos de divisibilidad indistinguibles a cualquier potencia de
\(1/\log x\) en ese nivel, pero sus masas cribadas en \(z=\sqrt x\)
difieren en escala \(x/\log x\). Así, Brun, Selberg o una
inclusión--exclusión lineal cuyos coeficientes crezcan a lo sumo como una
potencia de \(\log x\) no pueden producir (6) desde datos truncados.

Este documento prueba un **no-go de nivel de distribución incompleto** y
la reducción exacta (8)--(9). No prueba que una identidad global y
específica de los primos ordinarios sea imposible. Tampoco prueba (6),
Deep-\(\Lambda\), A1 ni RH.

---

## 1. Eratóstenes sin pérdida de correlación

Para cada \(n\),

\[
 {\mathbf 1}_{(n,P(z))=1}=\sum_{d\mid(n,P(z))}\mu(d).
 \tag{11}
\]

Sumar (11) para \(1\le n\le x\) prueba (2), con sumas finitas. Si
\(z=\sqrt x\) y \(1<n\le x\) es compuesto, posee un divisor primo
\(p\le\sqrt n\le\sqrt x\), y por ello no es contado por \(\Phi\). Si es
primo y excede \(\sqrt x\), sí es contado. Luego

\[
 \Phi(x,\sqrt x)=1+\pi(x)-\pi(\sqrt x),
 \tag{12}
\]

que junto con (2) prueba (3).

Al separar en (2) piso y término continuo,

\[
 \sum_{d\mid P(z)}{\mu(d)\over d}=V(z),
 \qquad
 \Phi(x,z)=xV(z)+R_E(x,z).
 \tag{13}
\]

Las ecuaciones (12)--(13) prueban (5). Es importante no estimar
\(R_E\) término a término: la cota

\[
 |R_E(x,\sqrt x)|\le 2^{\pi(\sqrt x)}
 \tag{14}
\]

destruye exactamente la cancelación buscada. Tampoco basta Mertens:
\(xV(\sqrt x)\sim2e^{-\gamma}x/\log x\), de modo que el residuo debe
cancelar ya un término de orden \(x/\log x\) antes de ver la fluctuación
de escala crítica.

## 2. Identidad exacta de paridad

Considere los datos de divisibilidad de (10),

\[
 A_d^\pm(x)=\sum_{\substack{n\le x\\d\mid n}}a_n^\pm.
 \tag{15}
\]

La función de Liouville es completamente multiplicativa, y por tanto

\[
 \boxed{
 A_d^\pm(x)=\left\lfloor{x\over d}\right\rfloor
 \pm\lambda_L(d)L(x/d).}
 \tag{16}
\]

Cribe ahora ambas sucesiones con todos los primos \(p\le\sqrt x\):

\[
 S^\pm(x)=\sum_{\substack{n\le x\\(n,P(\sqrt x))=1}}a_n^\pm.
 \tag{17}
\]

Por (12), solo sobreviven \(1\) y los primos mayores que \(\sqrt x\).
Como

\[
 a_1^+=2,\quad a_1^-=0,\qquad
 a_p^+=0,\quad a_p^-=2,
 \tag{18}
\]

se tiene exactamente

\[
 S^+(x)=2,\qquad
 S^-(x)=2\{\pi(x)-\pi(\sqrt x)\}.
 \tag{19}
\]

Por otro lado, inclusión--exclusión y (16) dan

\[
\begin{aligned}
 S^-(x)-S^+(x)
 &=\sum_{d\mid P(\sqrt x)}\mu(d)
       \{A_d^-(x)-A_d^+(x)\}\\
 &=-2\sum_{d\mid P(\sqrt x)}
       \mu(d)\lambda_L(d)L(x/d).
\end{aligned}
 \tag{20}
\]

Cada divisor de \(P(\sqrt x)\) es *squarefree*, luego
\(\lambda_L(d)=\mu(d)\) y \(\mu(d)\lambda_L(d)=1\). Comparar
(19) y (20) prueba (8).

Éste es el lugar exacto de la paridad: los signos de Möbius de
Eratóstenes son absorbidos por los signos de Liouville y dejan una suma
global sin coeficientes. Truncarla antes del nivel completo pierde la
masa que distingue (19).

## 3. Traducción a la energía ordinaria

Defina

\[
 T_m=\sum_{d\mid P(\sqrt m)}L(m/d),
 \qquad H_m=1+\pi(\sqrt m).
 \tag{21}
\]

La identidad (8) equivale a

\[
 \pi(m)-\mathrm{Li}_2(m)
 =H_m-\{T_m+\mathrm{Li}_2(m)\}.
 \tag{22}
\]

La cota elemental de Chebyshev da

\[
 H_m\ll1+{\sqrt m\over\log(2m)}.
 \tag{23}
\]

Por consiguiente

\[
 \sum_{m=2}^\infty{H_m^2\over m(m+1)}<\infty.
 \tag{24}
\]

La desigualdad triangular en el espacio de Hilbert con pesos
\(1/[m(m+1)]\) muestra que añadir o quitar \(H\) preserva tanto energía
acotada como crecimiento \(N^{o(1)}\). La equivalencia (9) sigue de
`104_93` y `104_94`.

Observe que (8) no ha ganado una desigualdad: insertada en (22), recupera
exactamente \(\pi(m)\). Su utilidad es adversarial: cualquier prueba que
declare pequeño \(T_m+\mathrm{Li}_2(m)\) debe exhibir una
cancelación global entre todos los \(L(m/d)\), no una cota de cada uno.

## 4. Gate cuantitativo para todo nivel subcompleto

Fije \(0<\eta<1\) y \(D=x^{1-\eta}\). La región libre de ceros clásica
aplicada a

\[
 \sum_{n\ge1}{\lambda_L(n)\over n^s}
 ={\zeta(2s)\over\zeta(s)}
 \tag{25}
\]

da, incondicionalmente, para todo \(A>0\),

\[
 |L(y)|\ll_A {y\over(\log y)^A}.
 \tag{26}
\]

Solo se necesita esta consecuencia débil de la cota efectiva tipo
Vinogradov--Korobov. Para \(d\le D\), \(x/d\ge x^\eta\); usando (16),

\[
\begin{aligned}
 \sum_{d\le D}|A_d^+(x)-A_d^-(x)|
 &\le2\sum_{d\le D}|L(x/d)|\\
 &\ll_{A,\eta}{x\over(\log x)^A}
                  \sum_{d\le D}{1\over d}\\
 &\ll_{A,\eta}{x\over(\log x)^{A-1}}.
\end{aligned}
 \tag{27}
\]

En particular, el lado izquierdo es
\(O_{B,\eta}(x/\log^B x)\) para cada \(B>0\). Pero PNT y (19) dan

\[
 S^-(x)-S^+(x)
 =2\{\pi(x)-\pi(\sqrt x)-1\}
 \sim {2x\over\log x}.
 \tag{28}
\]

De aquí resulta el siguiente enunciado preciso.

**Teorema de no-distinción.** No existe una familia de formas lineales

\[
 \mathcal F_x(A)=\sum_{d\le x^{1-\eta}}c_d(x)A_d,
 \qquad |c_d(x)|\le(\log x)^K,
 \tag{29}
\]

que aproxime \(S(A,\sqrt x)\) con error \(o(x/\log x)\), uniformemente
para toda sucesión no negativa \(A=(a_n)\). En efecto, (27) con
\(B>K+2\) daría

\[
 |\mathcal F_x(A^+)-\mathcal F_x(A^-)|=o(x/\log x),
 \tag{30}
\]

en contradicción con (28). El mismo argumento cubre cualquier funcional
uniformemente Lipschitz, con constante \(O((\log x)^K)\), para la norma
\(\ell^1\) de los datos \((A_d)_{d\le D}\).

Esto incluye las truncaciones lineales de inclusión--exclusión y las
salidas estables de Brun/Selberg apoyadas en ese nivel. No incluye la suma
exacta (2), que usa datos hasta \(d\asymp x\). Precisamente allí
\(x/d\) puede ser \(O(1)\), (27) deja de ser pequeño y la información de
paridad reaparece.

## 5. Veredicto

El ataque por Eratóstenes produce dos resultados exactos:

1. la energía buscada se convierte en (6), conservando toda la suma
   firmada;
2. la identidad (8) muestra que esa suma completa es una cancelación de
   Liouville, y (27)--(30) descartan todas sus truncaciones estables de
   nivel \(x^{1-\eta}\).

No queda un error técnico de Bonferroni ni una constante por optimizar.
Para avanzar desde esta coordenada hace falta una desigualdad global que
use los divisores \(d\) hasta escala \(x\) y que sea específica de los
pesos ordinarios. Demostrarla sería demostrar (9), y por tanto RH.

## 6. Auditoría de no duplicación

El `No-go NG-A4` de las fases iniciales y del *obstruction ledger* trata
la imposibilidad de separar clases de \(\omega(n)\bmod2\) mediante una
criba estándar. No contiene (8), no trabaja con la energía de Cramér y no
cuantifica el nivel \(x^{1-\eta}\). `104_94` usa inversión de Möbius entre
potencias primas y primos ordinarios, pero tampoco usa el par
\(1\pm\lambda_L\). El contenido adicional aquí es:

* la identidad de Eratóstenes completa (5) en la norma exacta de
  `104_93`;
* la identidad de paridad sin coeficientes (8);
* la equivalencia energética (9);
* el falsificador cuantitativo (27)--(30) para todo nivel
  subcompleto fijo.

No se reclama como nueva la barrera de paridad general de la teoría de
cribas. Lo nuevo dentro del proyecto es su localización exacta en el
observable que se está intentando acotar.

## 7. Reproducción

Desde `tools/`:

```bash
python3 eratosthenes_parity_energy_gate_check.py
```

El checker verifica, con enteros y fracciones exactas, (2)--(5),
(8), (16), (19)--(20) para todos los enteros \(2\le x\le300\). También
muestra en una tabla la separación de la masa cribada y la concentración
de la diferencia de datos de divisibilidad al acercarse al nivel completo.
La parte asintótica (26)--(30) es el argumento analítico anterior, no una
inferencia numérica.
