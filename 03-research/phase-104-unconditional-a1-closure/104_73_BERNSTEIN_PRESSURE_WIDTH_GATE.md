# 104_73 — Representación Bernstein de la presión y gate de ancho variable

**Resultado.** La razón de presiones de `104_72`, conservando dentro de
una sola variable la diferencia prima--polo completa,

\[
 \Phi_\tau(D)
 :=\log {1+e^D\over1+e^{D-\tau}},\qquad D=Q-C,
 \tag{1}
\]

admite una representación positiva exacta de Bernstein--Gumbel. Si
\(q=e^{-\tau}\), \(z=e^D\), entonces

\[
 \boxed{
 \Phi_\tau(D)
 =\int_0^\infty(1-e^{-tz})
 {e^{-t}-e^{-t/q}\over t}\,dt.}
 \tag{2}
\]

La medida de (2) es positiva. Sin embargo, esta positividad no produce una
cota del funcional a partir de una media lineal de \(D\): todo mayorante
afín global de \(\Phi_\tau\) es el mayorante trivial \(\tau\), y toda
linealización positiva de (2) por potencias vuelve a las particiones
exponenciales de `104_70`--`104_71`.

Permitir que el ancho \(\tau=\tau_L\) crezca tampoco rompe la pared de
precisión. Todo ancho subexponencial conserva el criterio de bloques.
Poniendo
\(w(\tau)=\tau/\tanh(\tau/4)\), para un factor individual reemplaza la
escala aditiva \(O(1)\) por \(O(w(\tau_L))\); para transportar la suma de
\(L\) factores con un error uniforme hace falta la escala
\(o(w(\tau_L)/L)\). Nótese que \(w(\tau)\to4\) cuando \(\tau\downarrow0\)
y \(w(\tau)\sim\tau\) cuando \(\tau\to\infty\). En ambos casos, en la
diagonal Euler de `104_72` el costo relativo sigue siendo

\[
 \exp\{-X_L^2/100+o(X_L)\}.
 \tag{3}
\]

Un ancho suficientemente grande para absorber el canal polar tiene escala
\(\exp(\Theta(X_L^2))\) y deja de detectar **todo** modo exterior de escala
\(R^{X_L}\). Quedan así descartadas, de forma cuantitativa, tres rutas:

1. monotonicidad afín en la diferencia completa;
2. Jensen/Bernstein seguido de un momento positivo;
3. ensanchamiento de la transición para amortiguar el polo.

Este gate no descarta una desigualdad firmada especial para los pesos
reales \(\Lambda(m)\) que estime directamente (1). No prueba
\(G_L\to0\), A1 ni RH.

---

## 1. Representación Bernstein exacta

Defina

\[
 f_q(z)=\log(1+z)-\log(1+qz),\qquad 0<q<1.
 \tag{4}
\]

Su derivada tiene la transformada de Laplace positiva

\[
\begin{aligned}
 f_q'(z)
 &= {1\over1+z}-{q\over1+qz}\\
 &=\int_0^\infty e^{-zt}\{e^{-t}-e^{-t/q}\}\,dt.
\end{aligned}
\tag{5}
\]

Integrando desde \(0\) hasta \(z\), Tonelli es aplicable porque el
integrando es no negativo. Como \(f_q(0)=0\), se obtiene (2). En
particular, \(f_q\) es una función de Bernstein y

\[
 (-1)^{k-1}f_q^{(k)}(z)
 =(k-1)!\left\{{1\over(1+z)^k}
 -{q^k\over(1+qz)^k}\right\}>0
 \quad(k\ge1).
 \tag{6}
\]

La representación puede leerse probabilísticamente: para cada \(t\),
\(1-e^{-t e^D}\) es la probabilidad de que un Poisson de intensidad
\(t e^D\) no sea cero. Por la fórmula de Frullani,

\[
 \int_0^\infty {e^{-t}-e^{-t/q}\over t}\,dt
 =\log(1/q)=\tau,
\]

de modo que la medida de (2), dividida por \(\tau\), es una probabilidad.
La mezcla es positiva, pero la
intensidad sigue conteniendo la actividad completa \(e^{Q-C}\); no separa
\(Q\) y \(C\).

Para \(0<\alpha\le1\), la desigualdad
\(1-e^{-u}\le u^\alpha\) y (2) dan el mayorante de Mellin

\[
 \boxed{
 {1\over\tau}\Phi_\tau(D)
 \le {\Gamma(\alpha)(1-e^{-\alpha\tau})\over\tau}
 e^{\alpha D}.}
 \tag{7}
\]

En efecto,

\[
 \int_0^\infty t^{\alpha-1}
 (e^{-t}-e^{-t/q})\,dt
 =\Gamma(\alpha)(1-q^\alpha).
 \tag{8}
\]

Aplicado a \(D_n=-\lambda_n-\log(n+1)\), (7) se convierte en

\[
 G_L
 \le {\Gamma(\alpha)(1-e^{-\alpha\tau})\over\tau}
 \sum_{n\in I_L}{e^{-\alpha\lambda_n}\over(n+1)^\alpha}.
 \tag{9}
\]

Para \(\alpha=1\), (9) es la cota de actividad de `104_72`, con la
constante mejorada \((1-e^{-\tau})/\tau\). Para
\(\alpha=1/\tau\) y \(\tau\to\infty\), su prefactor tiende a
\(1-e^{-1}\), mientras el lado derecho es exactamente una partición de
temperatura \(t=1/\tau\). Por tanto la linealización positiva de la
presión no crea una cantidad aritmética nueva: vuelve al gate de
temperatura variable de `104_70`.

---

## 2. No existe un mayorante afín no trivial

La función (1) satisface

\[
 \Phi_\tau(-\infty)=0,\qquad
 \Phi_\tau(+\infty)=\tau.
 \tag{10}
\]

**Lema 2.1.** Si \(aD+b\ge\Phi_\tau(D)\) para todo
\(D\in\mathbb R\), entonces \(a=0\) y \(b\ge\tau\). Si
\(aD+b\le\Phi_\tau(D)\) para todo \(D\), entonces \(a=0\) y
\(b\le0\).

**Demostración.** Para un mayorante, el límite \(D\to-\infty\)
excluye \(a>0\), mientras \(D\to+\infty\) excluye \(a<0\). Luego
\(a=0\), y (10) obliga \(b\ge\tau\). El argumento para un minorante es
idéntico. \(\square\)

La curvatura local confirma que tampoco existe una orientación global de
Jensen. Con \(\sigma(u)=(1+e^{-u})^{-1}\),

\[
 \Phi_\tau''(D)=\sigma'(D)-\sigma'(D-\tau),
 \tag{11}
\]

que es positiva para \(D<\tau/2\), cero en \(D=\tau/2\) y negativa
para \(D>\tau/2\). Así, conocer
\(\sum_{n\in I_L}(Q_n-C_n)\), incluso exactamente, no da mediante un
mayorante afín global ni mediante una orientación única de Jensen la cota
requerida para la razón de presiones. El dato faltante en esas rutas es la
distribución de las diferencias individuales a través de la transición.

---

## 3. El criterio sobrevive a un ancho variable

Sea

\[
 I_L=\{L^2,\ldots,L^2+L-1\},\qquad X_L=L^2+L-1,
 \tag{12}
\]

y tome cualquier sucesión \(\tau_L>0\) tal que

\[
 \boxed{\log(1+\tau_L)=o(L^2).}
 \tag{13}
\]

Defina

\[
 G_L^{(\tau_L)}
 =\sum_{n\in I_L}{1\over\tau_L}
 \Phi_{\tau_L}(-\lambda_n-\log(n+1)).
 \tag{14}
\]

**Teorema 3.1.** Bajo (13),

\[
 \boxed{\mathrm{RH}\quad\Longleftrightarrow\quad
 G_L^{(\tau_L)}\longrightarrow0.}
 \tag{15}
\]

Más precisamente, bajo RH se tiene \(G_L^{(\tau_L)}\le L^{-1}\),
mientras bajo no-RH existen \(M<\infty\) y \(L_0\) tales que

\[
 \liminf_{L\to\infty}{G_L^{(\tau_L)}\over L}\ge {1\over M}.
 \tag{16}
\]

**Demostración.** La ecuación (7) con \(\alpha=1\) y
\((1-e^{-\tau})/\tau\le1\) da

\[
 {1\over\tau_L}\Phi_{\tau_L}
 (-\lambda_n-\log(n+1))
 \le {e^{-\lambda_n}\over n+1}.
 \tag{17}
\]

Bajo RH, \(\lambda_n\ge0\); sumar (17) sobre (12) da
\(G_L^{(\tau_L)}\le L/(L^2+1)\le L^{-1}\).

Si RH es falsa, `104_56` proporciona \(c>0\), \(R>1\), un conjunto
sindético \(S\) y una cota de huecos \(M\), tales que
\(\lambda_n\le-cR^n\) en \(S\). La condición (13) implica
\(\tau_L=o(R^{L^2})\). Uniformemente para \(n\in S\cap I_L\),

\[
 \lambda_n+\log(n+1)+\tau_L\longrightarrow-\infty.
 \tag{18}
\]

La representación

\[
 {1\over\tau}\Phi_\tau(-x)
 ={1\over\tau}\int_0^\tau {ds\over1+e^{x+s}}
 \tag{19}
\]

muestra entonces que cada sitio de \(S\cap I_L\) aporta \(1-o(1)\).
Cada subintervalo de \(M\) enteros contiene uno de esos sitios; el mismo
conteo que en `104_72` prueba (16). \(\square\)

Por tanto el ancho puede crecer polinómicamente, o incluso como
\(\exp(\sqrt{X_L})\), y en general de cualquier manera subexponencial en
el grado. La relajación del ancho no pierde el falsificador exterior.

---

## 4. Incompatibilidad exacta ancho--polo

En la diagonal de `104_72`,

\[
 \varepsilon_L=e^{-X_L/100},\qquad
 |p_{X_L}(\varepsilon_L)-1|
 =\left({1-\varepsilon_L\over\varepsilon_L}\right)^{X_L},
 \tag{20}
\]

y por tanto

\[
 \log|p_{X_L}(\varepsilon_L)-1|
 ={X_L^2\over100}+o(1).
 \tag{21}
\]

La derivada de la presión normalizada respecto de \(D\) satisface

\[
 0< {d\over dD}\,{\Phi_\tau(D)\over\tau}
 \le {\tanh(\tau/4)\over\tau}< {1\over\tau}.
 \tag{22}
\]

En efecto,

\[
 \Phi_\tau'(D)=\sigma(D)-\sigma(D-\tau)
 ={\sinh(\tau/2)\over
   \cosh(D-\tau/2)+\cosh(\tau/2)},
\]

cuyo máximo se alcanza exactamente en \(D=\tau/2\) y vale
\(\tanh(\tau/4)\).

Sean \(D_{n,L}\) y \(\widetilde D_{n,L}\) dos familias de diferencias.
De (22) se sigue la cota de transporte del bloque

\[
 \left|\sum_{n\in I_L}{\Phi_{\tau_L}(D_{n,L})
                    -\Phi_{\tau_L}(\widetilde D_{n,L})\over\tau_L}\right|
 \le {\tanh(\tau_L/4)\over\tau_L}
      \sum_{n\in I_L}|D_{n,L}-\widetilde D_{n,L}|.
 \tag{22a}
\]

Defina la anchura efectiva

\[
 w(\tau):={\tau\over\tanh(\tau/4)}.
 \tag{22b}
\]

Por tanto es suficiente que la suma de errores sea \(o(w(\tau_L))\);
bajo una cota uniforme por sitio esto exige
\(\sup_{n\in I_L}|D_{n,L}-\widetilde D_{n,L}|
=o(w(\tau_L)/L)\). Esta escala es además la correcta para una garantía
uniforme basada solo en los errores absolutos: la derivada alcanza el
máximo de (22) en \(D=\tau/2\), y errores del mismo signo en los \(L\)
sitios saturan la cota a primer orden. Separar dos canales de tamaño (21)
con esa tolerancia uniforme exige la escala de precisión relativa

\[
 \boxed{
 {w(\tau_L)\over L|p_{X_L}(\varepsilon_L)-1|}
 =\exp\{-X_L^2/100+\log w(\tau_L)-\log L+o(1)\}.}
 \tag{23}
\]

Para que una sucesión de anchos prescrita de antemano detecte cualquier
radio exterior posible \(R>1\) hace falta

\[
 \tau_L=o(R^{X_L})\quad\hbox{para todo }R>1,
 \tag{24}
\]

que es equivalente a \(\log(1+\tau_L)=o(X_L)\). Como
\(w(\tau)\to4\) en cero y \(w(\tau)\sim\tau\) en infinito, (24) implica
\(\log w(\tau_L)=o(X_L)\). Por tanto (23) es precisamente

\[
 \exp\{-X_L^2/100+o(X_L)\}.                               \tag{25}
\]

En la dirección contraria, si el ancho hiciera que el costo logarítmico
de (23) dejara de tener escala cuadrática, en el sentido preciso de que
el logaritmo de (23) fuera \(-o(X_L^2)\), entonces (23) da primero
\(\log w(\tau_L)=X_L^2/100-o(X_L^2)\). En particular
\(w(\tau_L)\to\infty\), luego \(\tau_L\to\infty\),
\(w(\tau_L)\sim\tau_L\), y necesariamente

\[
 \log\tau_L={X_L^2\over100}-o(X_L^2).
 \tag{26}
\]

Pero (26) implica \(R^{X_L}/\tau_L\to0\) para todo \(R>1\). Una
excursión exterior \(-cR^{X_L}\) queda dentro de la región casi lineal
de ancho \(\tau_L\) y su contribución normalizada tiende a cero. El
detector ha sido destruido.

Para resolver un solo factor se omiten los dos factores \(L\) en (22a) y
(23); esto solo suprime \(-\log L=o(X_L)\) y no cambia (25)--(26).
Esta incompatibilidad es independiente de la forma en que se estimen los
dos canales por separado: compara solamente la tolerancia máxima
compatible con el criterio y el tamaño polar exacto. No es un no-go para
una estimación directa de la diferencia ya cancelada \(Q-C\).

---

## 5. Veredicto

**Probado:** la representación positiva (2), el mayorante de Mellin (7),
la clasificación afín del Lema 2.1, el cambio de curvatura (11), el
criterio de ancho variable (15)--(16) y la incompatibilidad cuantitativa
(23)--(26).

**Descartado:** obtener \(G_L\to0\) exclusivamente mediante un mayorante
afín global de la media lineal de \(Q-C\), mediante una orientación global
de Jensen sobre la representación positiva, o haciendo crecer el ancho
hasta que el polo regulado sea numéricamente benigno.

**Sobrevive:** una desigualdad aritmética firmada que controle directamente
la distribución de las diferencias completas
\(Q_{n,\varepsilon_L}-C_{n,\varepsilon_L}\) para los pesos exactos
\(\Lambda(m)\), sin separar los canales ni reemplazar la presión por un
momento exponencial.

**No probado:** ese control directo, \(G_L\to0\), A1 o RH.

---

## 6. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 bernstein_pressure_width_check.py
```

El checker verifica numéricamente (2), los signos de (6), la cota de
Mellin, el cambio de curvatura, el criterio en el cuarteto y las escalas
de (23)--(26). Las afirmaciones asintóticas y la clasificación afín se
prueban en el texto.
