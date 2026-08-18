# 104_66 — Diagonal regulador--Abel y gate de cancelación superexponencial

**Resultado.** La diagonal sugerida por `104_64` sí puede tomarse
rigurosamente. Si
\[
 q=e^{-h},\qquad \varepsilon(h)=e^{-C/h},                 \tag{1}
\]
entonces, para un \(C>0\) universal explícito, los coeficientes regulados
\(\lambda_{n,\varepsilon(h)}\) aproximan uniformemente a \(\lambda_n\) en
la ventana principal \(n\le h^{-1}\). La media Fermi Abel puede escribirse
con ese único regulador diagonal.

Esto no cierra RH. Antes de cancelar, el polo y el canal primo tienen tamaño
\(\exp(C/h^2)\) para \(n\asymp h^{-1}\), mientras su diferencia emparejada
tiene tamaño a lo sumo \(\exp(O(1/h))\). La fase requiere precisión relativa
\(\exp(-C/h^2+O(1/h))\). Separar los canales es un no-go cuantitativo;
mantenerlos juntos devuelve exactamente el observable Fermi desconocido.

---

## 1. Generatriz emparejada exacta

Sea
\[
 F(s)=(s-1)\zeta(s),\qquad s=s(z)={1\over1-z},\qquad
 \tau={z\over1-z}=s-1.                                    \tag{2}
\]
Con la notación de `104_61`--`104_64`,
\[
 \lambda_{n,\varepsilon}
 =A_n+p_n(\varepsilon)-Q_{n,\varepsilon},\qquad
 Q_{n,\varepsilon}
 =\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m).                                   \tag{3}
\]
Las generatrices exactas de `104_62` se combinan como
\[
\begin{aligned}
 \sum_{n\ge1}{p_n(\varepsilon)-Q_{n,\varepsilon}\over n}z^n
 &=
 \log\!\left(1+{\tau\over\varepsilon}\right)
 -\log\zeta(1+\varepsilon)
 +\log\zeta(1+\varepsilon+\tau)\\
 &=\log F(s+\varepsilon)-\log F(1+\varepsilon).
\end{aligned}                                             \tag{4}
\]
Para \(\varepsilon=0\), el lado derecho es
\(\log F(s)-\log F(1)\). Por tanto, si
\[
 d_{n,\varepsilon}:=\lambda_{n,\varepsilon}-\lambda_n,
\]
entonces
\[
 \boxed{\sum_{n\ge1}{d_{n,\varepsilon}\over n}z^n
 =D_\varepsilon(z)
 :=\log{F(s(z)+\varepsilon)\over F(s(z))}
 -\log{F(1+\varepsilon)\over F(1)}.}                       \tag{5}
\]
La rama se normaliza por \(D_\varepsilon(0)=0\). Ésta es la cancelación
que desaparece al separar \(p_n\) y \(Q_{n,\varepsilon}\).

---

## 2. Disco cero-libre uniforme bajo desplazamiento

Todo cero no trivial \(\rho=\beta+i\gamma\) satisface
\(0<\beta<1\) y \(|\gamma|>14\). La segunda cota es un input
incondicional certificado, mucho más débil que la verificación de
Platt--Trudgian registrada en `104_00`; no localiza aquí ningún cero fuera
de ese rango. Para \(0\le u\le1/2\), el punto singular
de \(F(s+u)\) en la variable \(z\) es
\[
 z_{\rho,u}=1-{1\over\rho-u}.                              \tag{6}
\]
Además,
\[
\begin{aligned}
 |z_{\rho,u}|^2
 &=1+{1-2\beta+2u\over(\beta-u)^2+\gamma^2}\\
 &\ge1-{1\over\gamma^2}>{195\over196}.                    \tag{7}
\end{aligned}
\]
Si el numerador es negativo se usa
\((\beta-u)^2+\gamma^2\ge\gamma^2\) y
\(1-2\beta+2u\ge-1\); si es positivo, la cota es inmediata.
Los ceros triviales \(\rho=-2k\) dan
\[
 z_{\rho,u}=1+{1\over2k+u}>1.                              \tag{8}
\]
Así, con
\[
 r_0=\sqrt{195\over196},\qquad
 v_0=-\log r_0={1\over2}\log{196\over195}<0.00257,         \tag{9}
\]
las funciones \(F(s(z)+u)\) son cero-libres simultáneamente en
\(|z|<r_0\), para \(0\le u\le1/2\), sin suponer RH.

Fije \(0<r<r_0\). Por compacidad,
\[
 M_r:=\sup_{\substack{|z|\le r\\0\le u\le1/2}}
 \left|{F'\over F}(s(z)+u)\right|<\infty.                  \tag{10}
\]
La fórmula
\[
 D_\varepsilon(z)=\int_0^\varepsilon
 \left\{{F'\over F}(s(z)+u)-{F'\over F}(1+u)\right\}du    \tag{11}
\]
da \(\sup_{|z|\le r}|D_\varepsilon(z)|\le2M_r\varepsilon\).
Cauchy aplicado a (5) prueba
\[
 \boxed{|d_{n,\varepsilon}|
 \le2M_r\,n\,\varepsilon r^{-n}.}                          \tag{12}
\]

---

## 3. Elección universal de la diagonal

Para \(n\le B/h\), (12) da
\[
 \sup_{n\le B/h}|d_{n,\varepsilon(h)}|
 \le {2BM_r\over h}
 \exp\!\left(-{C-B\log(1/r)\over h}\right).                \tag{13}
\]
Por tanto basta \(C>Bv_0\) para elegir
\(e^{-C/B}<r<r_0\). Para la ventana principal \(B=1\) puede tomarse
\[
 \boxed{r={199\over200},\qquad C={1\over100}.}              \tag{14}
\]
En efecto,
\[
 {199\over200}<\sqrt{195\over196},\qquad
 \eta:={1\over100}-\log{200\over199}>0.                    \tag{15}
\]
Con
\[
 \varepsilon(h)=\exp\!\left(-{1\over100h}\right),          \tag{16}
\]
que pertenece a \((0,1/2]\) para todo \(h\) suficientemente pequeño, se
obtiene incondicionalmente
\[
 \boxed{\sup_{1\le n\le1/h}
 |\lambda_{n,\varepsilon(h)}-\lambda_n|
 \le {2M_{199/200}\over h}e^{-\eta/h}\longrightarrow0.}   \tag{17}
\]
La constante \(M_{199/200}\) es finita sobre un compacto explícito y no
depende de \(h\); su valor numérico no afecta el límite.

---

## 4. Un único límite diagonal para Fermi

Sea
\[
 \ell(y)={1\over1+e^y},\qquad b_n=\log(n+1),
\]
y defina
\[
 \mathfrak A_{t,\varepsilon}(h)
 ={1\over L(h)}\sum_{n\ge1}{e^{-hn}\over n}
 \ell\!\left(t(\lambda_{n,\varepsilon}+b_n)\right),
 \qquad L(h)=-\log(1-e^{-h}).                              \tag{18}
\]
Como \(|\ell'|\le1/4\), el bloque \(n\le1/h\) de la diferencia con la
media no regulada está acotado por \(t/4\) veces (17). En la cola se usa
solo \(0\le\ell\le1\):
\[
 {1\over L(h)}\sum_{n>1/h}{e^{-hn}\over n}
 \le {1\over L(h)}\int_{1/2}^\infty{e^{-u}\over u}\,du=o(1)
 \qquad(0<h\le1/2).                                       \tag{19}
\]
Luego, para todo \(t>0\),
\[
 \boxed{\mathfrak A_t(h)
 -\mathfrak A_{t,\varepsilon(h)}(h)\longrightarrow0.}      \tag{20}
\]
Por `104_64`,
\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \liminf_{h\downarrow0}\mathfrak A_{t,\varepsilon(h)}(h)=0.}
 \tag{21}
\]
El lado derecho contiene, para cada \(h>0\), una serie de Euler
absolutamente convergente y ningún límite interno en \(\varepsilon\).

---

## 5. Pared de precisión al separar los canales

La primera generatriz de (4) da exactamente
\[
\begin{aligned}
 \sum_{n\ge1}{p_n(\varepsilon)\over n}z^n
 &=\log\!\left(1+{\tau\over\varepsilon}\right)\\
 &=\log\!\left(1+{1-\varepsilon\over\varepsilon}z\right)
 -\log(1-z),
\end{aligned}                                             \tag{22}
\]
y por ello
\[
 \boxed{p_n(\varepsilon)
 =1+(-1)^{n-1}\left({1-\varepsilon\over\varepsilon}\right)^n.}
 \tag{23}
\]
En la diagonal (16), para \(n\asymp h^{-1}\),
\[
 \log|p_n(\varepsilon(h))|
 ={1\over100h^2}+o(h^{-2}).                                \tag{24}
\]
Pero (3) equivale a
\[
 Q_{n,\varepsilon}
 =p_n(\varepsilon)+A_n-\lambda_{n,\varepsilon}.            \tag{25}
\]
El bloque completo \(A_n-\lambda_{n,\varepsilon}\) tiene crecimiento
\(\exp(O(n))\) en el disco uniforme anterior, mientras los dos términos
que se cancelan en (25) tienen tamaño \(\exp(C/h^2)\). Recuperar su
diferencia requiere precisión relativa
\[
 \boxed{\exp\{-C/h^2+O(1/h)\}.}                            \tag{26}
\]

La versión unitaria no cambia el requisito. El factor polar contiene
\(\exp\{istp_n(\varepsilon(h))\}\). Incluso para la microfrecuencia
\(s=\exp(-c/h)\) de `104_64`,
\[
 s|p_n(\varepsilon(h))|
 =\exp\{C/h^2-c/h+o(h^{-2})\}\longrightarrow\infty.        \tag{27}
\]
El factor primo tiene la fase opuesta con la precisión (26). Tomar módulos,
variación total o truncar una fase pierde la cancelación. Multiplicar primero
de manera exacta da
\[
 e^{ist(A_n+b_n+p_n-Q_{n,\varepsilon})}
 =e^{ist(\lambda_{n,\varepsilon}+b_n)},                    \tag{28}
\]
el observable desconocido de (18). Esto descarta una estimación separada,
no una identidad nueva para el producto completo.

### 5.1 Incompatibilidad con la amortiguación absoluta VK

El regulador tampoco convierte en útil la cota absoluta descartada en
`103_56`. Allí, en

\[
 U_n=n^{5/3}(\log n)^{1/3},
\]

la carga positiva sin regulador satisface

\[
 \log\mathcal B_n\ge
 {2\over3}n\log n+{1\over3}n\log\log n-O(n).               \tag{28a}
\]

El factor \(m^{-\varepsilon}=e^{-\varepsilon u}\) solo resta
\(\varepsilon U_n+O(\varepsilon)\) a ese exponente sobre
\([U_n,U_n+1]\). Para reducir la propia carga absoluta a escala
subexponencial sería necesario, como mínimo,

\[
 \varepsilon U_n\ge
 {2\over3}n\log n+{1\over3}n\log\log n-O(n),
\]

es decir,

\[
 \boxed{\varepsilon\gtrsim
 n^{-2/3}(\log n)^{2/3}.}                                  \tag{28b}
\]

En la ventana \(n\asymp h^{-1}\), la diagonal que aproxima los coeficientes
usa en cambio

\[
 \varepsilon(h)=e^{-C/h}=e^{-Cn},
\]

que es menor que toda potencia de \(n^{-1}\). Por tanto ninguna elección
cubierta por la garantía uniforme incondicional (13) puede ser
simultáneamente:

1. suficientemente pequeña para la aproximación uniforme obtenida por
   Cauchy; y
2. suficientemente grande para reparar por módulo la carga VK--Laguerre.

Esta incompatibilidad no afecta una estimación firmada del producto
completo. Sí cierra la posibilidad de que el mero hecho de mantener
\(\varepsilon>0\) vuelva viable el argumento de valores absolutos.

---

## 6. El regulador no borra un modo off-line

Si hipotéticamente existe \(\rho\) con \(\Re\rho>1/2\), ponga
\[
 u_\rho={\rho\over\rho-1},\qquad |u_\rho|>1.
\]
El desplazamiento cambia el modo por
\[
 u_{\rho-\varepsilon}
 ={\rho-\varepsilon\over\rho-\varepsilon-1},\qquad
 \log u_{\rho-\varepsilon}-\log u_\rho=O_\rho(\varepsilon).
 \tag{29}
\]
Para \(n\le1/h\) y (16),
\[
 n\{\log u_{\rho-\varepsilon(h)}-\log u_\rho\}
 =O_\rho(h^{-1}e^{-1/(100h)})=o(1).                        \tag{30}
\]
El regulador diagonal conserva la amplitud y la fase exponenciales del
modo off-line. Aproxima el criterio: no lo suaviza hasta volverlo verdadero.

En contraste, la expansión exacta de primer orden es

\[
 \log u_{\rho-\varepsilon}-\log u_\rho
 ={\varepsilon\over\rho(\rho-1)}+O_\rho(\varepsilon^2).
 \tag{31}
\]

Con una amortiguación polinómica del tamaño (28b), se tiene
\(n\varepsilon\to\infty\). Tal regulador altera el modo dominante por un
factor exponencial no uniforme y no puede sustituirse en el detector
coeficiente a coeficiente. Ésta es la misma incompatibilidad vista desde
los ceros en vez de la carga VK.

---

## 7. Veredicto

**Probado:** la generatriz (5), el disco desplazado (7)--(9), la cota
\(2M_rn\varepsilon r^{-n}\), la diagonal explícita (16), la equivalencia
Fermi diagonal (20)--(21) y la pared (26).

**Ganancia:** el frente Abel queda enteramente dentro del semiplano de
convergencia absoluta de Euler, con un único regulador ligado a \(h\).

**No probado:** una cota para la fase completa (28), el límite Fermi, A1 o
RH. La diagonal elimina un problema de intercambio de límites, no la
cancelación aritmética.

---

## 8. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 diagonal_abel_regulator_gate_check.py
```

El checker verifica (23) contra la suma binomial con aritmética racional,
las desigualdades de (14)--(15), la escala \(C/h^2\) y la estabilidad de
un modo exterior desplazado. Las cotas analíticas se prueban en el texto.
