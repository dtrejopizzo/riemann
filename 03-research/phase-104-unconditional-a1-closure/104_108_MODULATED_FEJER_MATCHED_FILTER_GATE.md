# 104_108 — Fejér modulado, filtros emparejados y gate resonante

**Pregunta.** El selector malo bajo no-RH no es arbitrario: es un Bohr set
determinado por el polinomio trigonométrico de los modos dominantes.
¿Permite esa estructura reemplazar el cubo completo de selectores de
`104_106` por filtros de Fourier y transportar la cota de fase de
`104_41`?

**Resultado.** Sí hay una reducción estructural de los tests. Basta una
familia uniparamétrica de filtros de Fejér modulados. Para \(N\ge L\),
\(a\ge4\) y todo \(\phi\in\mathbb R\), se prueba

\[
 \boxed{
 |\mathcal B^{\triangle}_{N,L,a}(\phi)|
 \le 3\pi {N\over L}+4.}                                \tag{1}
\]

Esta cota es uniforme en la frecuencia y conserva polo, todos los primos y
todas las potencias primas dentro de la fase completa.

Además, Parseval muestra que controlar estos filtros uniformemente en
\(\phi\) controla todos los grados del bloque en norma cuadrática. En
particular,

\[
 \mathrm {RH}\quad\Longleftrightarrow\quad
 \sup_\phi|\mathcal B^{\triangle}_{2L,L,1}(\phi)|
 \le e^{\sqrt L}\quad\hbox{eventualmente}.               \tag{2}
\]

Pero al bajar \(a\) hasta \(1\), un cero derecho produce exactamente un
filtro resonante. Si \(w_\rho=re^{i\theta}\), la elección
\(\phi=-\theta\) contiene el factor positivo
\(K_L(r^{-1})\ge r^{-L+1}/L^2\), y el residuo conserva tamaño
\(r^{-N-L+1}/L^2\). Así (1) no se transporta: el único término que falta
es nuevamente el residuo que (2) excluiría.

La ganancia respecto de `104_106` es precisa: para detectar un
coeficiente exponencial no hace falta controlar todos los selectores
\(a_j\in[0,1]\); una sola frecuencia continua basta por Parseval. Esto
reduce la familia de tests, pero no debilita la dificultad lógica: (2)
sigue siendo equivalente a RH. El documento no prueba la cota (2) en
\(a=1\), A1 ni RH.

---

## 1. No duplicación interna

`104_62`, §5.2, ya prueba que el selector variacional óptimo puede
concentrarse en clases periódicas y que los selectores geométricos no
controlan ese supremo. `104_58` y `104_65` prueban que
ventanas y filtros locales fijos conservan los modos exteriores.
`104_107` obtiene la cota de fase para el Fejér **no modulado**.

Por tanto no se reclama como nueva la observación general «hacen falta
selectores periódicos». Las piezas nuevas de este documento son exactamente:

1. la cota de fase uniforme en la modulación \(\phi\), (1);
2. la reducción por Parseval desde todos los grados a esa familia
   uniparamétrica, (11)--(12);
3. la fórmula de transporte modulado (15) y su resonancia exacta (16);
4. el falsificador del cuarteto completo, sin cancelación conjugada,
   (18)--(19).

---

## 2. El filtro modulado

Ponga

\[
 \alpha_{L,k}={L-|k|\over L^2}\quad(|k|<L),
 \qquad
 H_L(x)=\sum_{|k|<L}\alpha_{L,k}e^{ikx}
 =\left({\sin(Lx/2)\over L\sin(x/2)}\right)^2.           \tag{3}
\]

Para una frecuencia real \(\phi\), defina

\[
 \begin{aligned}
 \mathcal B^{\triangle}_{N,L,a}(\phi)
   &:=\sum_{|k|<L}\alpha_{L,k}e^{-ik\phi}
       \mathcal B_{N+k,a},\\
 V_{N,L,\phi}(t)
   &:=\sum_{|k|<L}\alpha_{L,k}e^{-ik\phi}W_{N+k}(t).
 \end{aligned}                                           \tag{4}
\]

Los pesos ya no son reales, pero la identidad de fase de `104_41` es
lineal y puede aplicarse a partes real e imaginaria:

\[
 \mathcal B^{\triangle}_{N,L,a}(\phi)
 =-{1\over2\pi}\int_{\mathbb R}V_{N,L,\phi}(t)\,
 d\vartheta_a(t).                                        \tag{5}
\]

En la variable \(\theta\), donde
\(W_n=2-e^{in\theta}-e^{-in\theta}\), la suma de (4) es

\[
 \boxed{
 V_{N,L,\phi}(\theta)
 =2H_L(\phi)
 -e^{iN\theta}H_L(\theta-\phi)
 -e^{-iN\theta}H_L(\theta+\phi).}                       \tag{6}
\]

En particular \(V_{N,L,\phi}(0)=0\), como exige el borde
\(|t|\to\infty\).

---

## 3. Cota uniforme de variación y fase

La integral de \(H_L\) en un período es \(2\pi/L\). La cota de variación
probada en `104_107` implica

\[
 \operatorname {TV}_{[0,2\pi]}(H_L)
 \le {8\over3}\left(1-{1\over L^2}\right)<{8\over3}.   \tag{7}
\]

Diferenciando (6), usando \(H_L\ge0\), y extendiendo cada intervalo de
longitud \(\pi\) a un período completo,

\[
 \begin{aligned}
 \int_0^\pi|V'_{N,L,\phi}(\theta)|\,d\theta
 &\le N\int_0^\pi
   \{H_L(\theta-\phi)+H_L(\theta+\phi)\}\,d\theta\\
 &\quad+\int_0^\pi
   \{|H_L'(\theta-\phi)|+|H_L'(\theta+\phi)|\}\,d\theta\\
 &\le {4\pi N\over L}+{16\over3}.                       \tag{8}
 \end{aligned}
\]

Las dos semirrectas de \(t\) dan entonces

\[
 \operatorname {TV}_{\mathbb R}(V_{N,L,\phi})
 \le {8\pi N\over L}+{32\over3}.                        \tag{9}
\]

Para \(a\ge4\), `104_41` da
\(|\vartheta_a(t)|<3\pi/4\). Integrando (5) por partes y usando (9),

\[
 |\mathcal B^{\triangle}_{N,L,a}(\phi)|
 \le {1\over2\pi}{3\pi\over4}
       \operatorname {TV}_{\mathbb R}(V_{N,L,\phi})
 \le3\pi {N\over L}+4,                                  \tag{10}
\]

uniformemente en \(\phi\). Esto prueba (1). No se tomó módulo dentro de
\(M_\Lambda\); el módulo aparece solo después de integrar la fase completa.

---

## 4. Parseval reemplaza el cubo de selectores

Para cualquier sucesión real \(x_n\), ortogonalidad en \(\phi\) da

\[
 \boxed{
 {1\over2\pi}\int_0^{2\pi}
 \left|\sum_{|k|<L}\alpha_{L,k}e^{-ik\phi}x_{N+k}\right|^2
 \,d\phi
 =\sum_{|k|<L}\alpha_{L,k}^2x_{N+k}^2.}                 \tag{11}
\]

Por tanto

\[
 \sup_\phi
 \left|\sum_{|k|<L}\alpha_{L,k}e^{-ik\phi}x_{N+k}\right|
 \ge\max_{|k|<L}\alpha_{L,k}|x_{N+k}|.                 \tag{12}
\]

Esta es la versión rigurosa de la intuición de Bohr/matched filter. No es
necesario aproximar el indicador discontinuo del Bohr set: si un modo
exterior crea una excursión en cualquier grado del bloque, alguna frecuencia
de (4) la detecta automáticamente. (11) es una identidad de promedio
\(L^2\) en \(\phi\); (12) pasa de ese promedio al supremo. Ninguna de las
dos afirma que una media firmada produzca un bloque bueno. Para eso sigue
haciendo falta la parte positiva de `104_106`, (16).

Tome ahora \(x_n=B_n=A_n-\lambda_n\), \(N=2L\). Bajo RH,
\(B_n=O(n\log n)\), luego el supremo de (2) es \(O(L\log L)\). Si RH es
falsa, `104_67` produce un conjunto sindético \(D_+\) y constantes
\(c>0,R>1\) con \(\lambda_n\ge cR^n\) en \(D_+\). Para todo \(L\) grande
existe \(d_L\in D_+\cap[2L,2L+G]\), donde \(G\) es un gap fijo. Entonces

\[
 |B_{d_L}|\ge {c\over2}R^{d_L},
 \qquad
 \alpha_{L,d_L-2L}\ge {L-G\over L^2}.                  \tag{13}
\]

Las ecuaciones (12)--(13) muestran que el supremo de (2) es
\(\gg R^{2L}/L\), y por tanto supera \(e^{\sqrt L}\). Esto prueba (2).

Equivalentemente, se puede tomar \(x_n=\mathscr R_n\) de `104_106`:
la parte crítica es \(O(n\log n)\), de modo que no cambia la dicotomía
subexponencial/exponencial.

El criterio (2) usa valor absoluto y es bilateral. Grado por grado es más
fuerte que pedir solo la barrera superior de `104_67`, y el
supremo de Fourier no construye por sí mismo un bloque bueno. Su
equivalencia con RH proviene de las excursiones **bilaterales** de
`104_67`: bajo no-RH, cualquiera de los dos signos produce un
coeficiente exponencial que (11)--(12) detectan. Por tanto (2) es una
reexpresión estructurada de fuerza RH, no un nuevo debilitamiento lógico
del objetivo.

---

## 5. Transporte exacto y resonancia

Introduzca el polinomio de Laurent

\[
 K_L(z)=\sum_{|k|<L}\alpha_{L,k}z^k
 ={(1-z^L)(1-z^{-L})\over L^2(1-z)(1-z^{-1})}.           \tag{14}
\]

Para un cero derecho \(\rho\), con \(w=w_\rho\), la identidad

\[
 {\mathcal F_n(w)\over\rho(\rho-1)}=w^n+w^{-n}-2
\]

da, sin resto,

\[
\boxed{
 \begin{aligned}
 \mathscr R^{\triangle}_{N,L}(\phi)
 :=\sum_{|k|<L}\alpha_{L,k}e^{-ik\phi}\mathscr R_{N+k}
 =\sum_{\Re\rho>1/2}m_\rho\{&
 w_\rho^N K_L(w_\rho e^{-i\phi})\\
 &+w_\rho^{-N}K_L(w_\rho^{-1}e^{-i\phi})
 -2H_L(\phi)\}.
 \end{aligned}}                                         \tag{15}
\]

Escriba \(w=re^{i\theta}\), \(0<r<1\). En la frecuencia emparejada
\(\phi=-\theta\),

\[
 w^{-1}e^{-i\phi}=r^{-1}>1,
\]

y todos los términos de \(K_L(r^{-1})\) son positivos. En particular,

\[
 \boxed{
 K_L(r^{-1})\ge {r^{-L+1}\over L^2},
 \qquad
 |w^{-N}K_L(w^{-1}e^{-i\phi})|
 \ge {r^{-N-L+1}\over L^2}.}                            \tag{16}
\]

La frecuencia conjugada empareja el conjugado del mismo cero. Un filtro
modulado detecta, no cancela, la parte principal exterior.

La falta de selectividad angular fuera del círculo es también explícita.
Si \(z=Re^{i\delta}\), \(R>1\), entonces el término extremo de \(K_L(z)\)
tiene tamaño \(R^{L-1}/L^2\). Una desalineación fija de \(\delta\) solo
cambia la fase; no aporta decaimiento exponencial. La localización de Bohr
vive en el polinomio trigonométrico normalizado \(R^{-n}B_n\), mientras un
promedio no normalizado queda dominado por el extremo radial del bloque.

Por (15), bajar \(a:4\to1\) en (10) cruza exactamente la contribución
resonante (16). Una continuación que conservara la cota polinómica (10)
probaría (2), y por tanto RH. No existe una deducción de esa continuación a
partir de la fase en \(a\ge4\): es el teorema aritmético faltante.

---

## 6. Falsificador racional

Tome

\[
 w={i\over2},\qquad \rho={4+2i\over5},\qquad
 \phi=-{\pi\over2}.
\]

Entonces \(e^{-i\phi}=i\) y

\[
 w^{-1}e^{-i\phi}=(-2i)i=2,
 \qquad
 K_L(2)\ge{2^{L-1}\over L^2}.                            \tag{17}
\]

Para auditar el cuarteto completo, sume también el conjugado. Si
\(4\mid N\), la contribución conjunta a (15) es exactamente

\[
\begin{aligned}
 \mathscr R^{\triangle,\mathcal O}_{N,L}(-\pi/2)
 ={}&2^{-N}\{K_L(1/2)+K_L(-1/2)\}\\
 &+2^N\{K_L(2)+K_L(-2)\}-4H_L(\pi/2).                  \tag{18}
\end{aligned}
\]

Como \(0\le H_L(\pi/2)\le1\), y el mayor exponente par menor que \(L\)
da en ambos casos de paridad

\[
 K_L(2)+K_L(-2)
 =2\sum_{\substack{|k|<L\\k\ {\rm par}}}\alpha_{L,k}2^k
 \ge {2^L\over L^2},
\]

se obtiene la cota firmada

\[
 \boxed{
 \mathscr R^{\triangle,\mathcal O}_{N,L}(-\pi/2)
 \ge {2^{N+L}\over L^2}-4.}                              \tag{19}
\]

En particular, con \(N=2L\) y \(L\) par, el cuarteto completo produce
\(\ge2^{3L}/L^2-4\). No hay cancelación escondida al añadir el conjugado.
El mismo cuarteto deja idéntica la fase sobre la línea crítica, como en
`104_41`, y la frecuencia conjugada \(+\pi/2\) da la orientación
conjugada. Esto pasa el falsificador off-line obligatorio.

El cuarteto no posee el Euler producto de los primos ordinarios. No refuta
una cota específica de \(\Lambda(m)\); refuta transportar (10) sin la suma
de residuos (15).

---

## 7. Veredicto

**Probado:** identidad del test modulado (6), cota uniforme de fase (1),
Parseval (11), criterio uniparamétrico (2), transporte exacto (15) y
resonancia (16).

**Ganancia:** el target de selectores de `104_106` se reduce a una
familia continua de una sola frecuencia. La norma uniforme de filtros
emparejados es una condición subexponencial concreta, conserva el andamiaje
Li--Laguerre y detecta cualquier excursión exterior por Parseval. Es una
reducción de coordenadas, no una prueba ni un debilitamiento de la fuerza
RH del target.

**Descartado:** que la estructura de Bohr, una modulación de Fourier o el
promedio de Fejér permitan trasladar automáticamente la cota de fase desde
\(a\ge4\) hasta \(a=1\).

**Sobrevive:** una cota aritmética uniforme en \(\phi\) para
\(\mathcal B^{\triangle}_{2L,L,1}(\phi)\), obtenida de los pesos literales
\(\Lambda(m)\), con crecimiento \(e^{o(L)}\). Por (2), tal cota probaría
RH.

**No probado:** esa cota en \(a=1\), A1 o RH.

## 8. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 modulated_fejer_matched_filter_check.py
```

El checker usa `Fraction` y racionales gaussianos. Verifica (6),
(11), (14)--(19) en familias finitas exactas. La cota analítica de variación
(8)--(10) está demostrada en el texto y no se sustituye por muestreo.
