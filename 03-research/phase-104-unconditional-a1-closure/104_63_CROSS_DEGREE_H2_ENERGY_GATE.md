# 104_63 — Energía entre grados, Parseval (H^2) y gate de Christoffel--Darboux

**Pregunta.** ¿Se puede evitar el control grado a grado de A1 sumando una
energía positiva del coeficiente *completo*, por ejemplo

\[
 \mathcal E_N:=\sum_{N<n\le 2N}{\lambda_n^2\over n},             \tag{1}
\]

y usando Parseval o Christoffel--Darboux antes de separar polo, bloque
arquimediano, primos y potencias primas?

**Veredicto.** La energía (1) da un criterio exacto y cuantitativo, pero no una
cota nueva. Su serie de Hardy tiene un polo interior exactamente cuando RH
falla. La identidad de Christoffel--Darboux existe y conserva toda la suma
prima, pero sus tres piezas reguladas divergen como
\(\varepsilon^{-4N}\) y solo su cancelación completa tiene límite. Por tanto
la positividad del kernel no produce una cota superior: para usarla haría falta
estimar el mismo defecto prima--polo que determina \(\lambda_n\).

Este documento cierra el ataque **Parseval/CD desnudo**. No prueba A1 ni RH y
no presenta otra equivalencia como progreso hacia su demostración.

---

## 1. Auditoría de no duplicación

La búsqueda interna encontró antecedentes adyacentes, no este argumento:

* `phase-33-dbn/78-transformada-li-ccm.md`, §5.3, eleva un coeficiente
  individual a \(\lambda_n^2\), con una constante que depende de los ceros
  off-line; no suma grados ni obtiene Parseval aritmético;
* `phase-55-two-arrows/173-representacion-de-I.md`, §5.2, estudia normas
  cuadráticas de funcionales holomorfos para la energía transversal de los
  ceros, no la energía de los coeficientes de Li;
* `104_28`--`104_30` construyen la forma prima--polo regulada y ya prueban que
  sus dos canales no se pueden estimar por separado. Aquí ese colapso se hace
  exacto en la dirección de los grados.

En la literatura primaria citada por la fase, Lagarias da el crecimiento de
los coeficientes bajo RH y Suzuki representa coeficientes individuales como
normas condicionales. Una búsqueda dirigida no encontró la energía diádica
(1). No se reclama novedad: el criterio de la sección siguiente es una
consecuencia elemental de Cauchy--Hadamard y Parseval.

---

## 2. Teorema exacto de radio y energía diádica

Ponga

\[
 G(z):=z{d\over dz}\log\xi\!\left({1\over1-z}\right)
      ={z\over(1-z)^2}{\xi'\over\xi}\!\left({1\over1-z}\right)
      =\sum_{n\ge1}\lambda_nz^n.                            \tag{2}
\]

Para un cero no trivial \(\rho\), escriba

\[
 w_\rho=1-{1\over\rho}.
\]

Se tiene

\[
 |w_\rho|<1\quad\Longleftrightarrow\quad\Re\rho>{1\over2}. \tag{3}
\]

Si existe un cero a la derecha de la recta, defina

\[
 r_0:=\min_{\Re\rho>1/2}|w_\rho|<1;                          \tag{4}
\]

el mínimo existe porque \(|w_\rho|\to1\) cuando
\(|\Im\rho|\to\infty\). Bajo RH adopte \(r_0=1\).

**Teorema 2.1 (ley exacta de crecimiento entre grados).** Con (1) y (4),

\[
 \boxed{\displaystyle
  \limsup_{N\to\infty}\mathcal E_N^{1/(4N)}={1\over r_0}.}  \tag{5}
\]

En particular, son equivalentes:

\[
 \mathrm{RH},\qquad
 \log(1+\mathcal E_N)=o(N),\qquad
 \limsup_N\mathcal E_N^{1/(4N)}=1.                          \tag{6}
\]

Bajo RH, el teorema efectivo de Lagarias usado en `104_02` da más:

\[
 \mathcal E_N\ll N^2\log^2N.                               \tag{7}
\]

**Demostración.** La transformación \(s=1/(1-z)\) lleva el disco unidad al
semiplano \(\Re s>1/2\). Si \(\rho\) tiene multiplicidad \(m_\rho\), (2)
tiene en \(w_\rho\) un polo simple de residuo

\[
 \mathop{\rm Res}_{z=w_\rho}G(z)=m_\rho w_\rho\ne0.         \tag{8}
\]

Por tanto el radio de convergencia de (2) es exactamente \(r_0\). Cauchy--
Hadamard da

\[
 \limsup_n|\lambda_n|^{1/n}=r_0^{-1}.                       \tag{9}
\]

Para la cota superior en (5), fije \(r<r_0\). Cauchy da
\(|\lambda_n|\le M_r r^{-n}\), de donde
\(\limsup_N\mathcal E_N^{1/(4N)}\le r^{-1}\); haga
\(r\uparrow r_0\). Para la inferior, tome una subsucesión que alcance (9) y
\(N=\lceil n/2\rceil\). Entonces \(N<n\le2N\) y
\(\mathcal E_N\ge\lambda_n^2/n\), lo que da el sentido contrario. Bajo RH,
\(r_0=1\); la estimación (7) sigue de
\(\lambda_n=\frac12n\log n+O(n)\). \(\square\)

La versión Abel/Hardy es igualmente exacta. Para \(0<r<r_0\),

\[
 {1\over2\pi}\int_0^{2\pi}|G(re^{it})|^2dt
   =\sum_{n\ge1}\lambda_n^2r^{2n}.                          \tag{10}
\]

Si \(W_0=\{w_\rho:|w_\rho|=r_0\}\), la expansión principal (8) da

\[
 {1\over2\pi}\int_0^{2\pi}|G(re^{it})|^2dt
 ={\sum_{w\in W_0}m_w^2\over1-(r/r_0)^2}+O(1)
 \qquad(r\uparrow r_0<1).                                  \tag{11}
\]

Así, el supuesto "bound de Hardy" choca literalmente con el primer polo
interior, no con una pérdida de constantes.

---

## 3. Representación aritmética exacta antes del cuadrado

Use la convención de `104_61`. Para \(\varepsilon>0\), defina

\[
\begin{aligned}
 p_n(\varepsilon)
 &=n\sum_{j=1}^n{n-1\choose j-1}{(-1)^{j-1}\over j\varepsilon^j},\\
 Q_{n,\varepsilon}
 &=\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
        L_{n-1}^{(1)}(\log m),\\
 \lambda_{n,\varepsilon}
 &=A_n+p_n(\varepsilon)-Q_{n,\varepsilon}.
\end{aligned}                                                \tag{12}
\]

Entonces \(\lambda_{n,\varepsilon}\to\lambda_n\). Como el bloque exterior
es finito, Parseval da la identidad rigurosa

\[
\boxed{
 \mathcal E_N=
 \lim_{\varepsilon\downarrow0}{1\over2\pi}
 \int_0^{2\pi}\left|
 \sum_{N<n\le2N}{\lambda_{n,\varepsilon}\over\sqrt n}e^{int}
 \right|^2dt.}                                               \tag{13}
\]

La fórmula (13) mantiene juntos el bloque arquimediano, el polo, todos los
primos y todas las potencias primas hasta después de formar el cuadrado.

Hay también una forma de medida firmada. Sea

\[
 d\nu_\varepsilon(x)=e^{-\varepsilon x}\,dx-
 \sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
       \delta_{\log m}(dx).                                  \tag{14}
\]

Entonces

\[
 p_n(\varepsilon)-Q_{n,\varepsilon}
 =\int_0^\infty L_{n-1}^{(1)}(x)\,d\nu_\varepsilon(x).       \tag{15}
\]

Esta es la forma exacta del acoplamiento polo--primos; \(\nu_\varepsilon\)
es firmada, no positiva.

---

## 4. Christoffel--Darboux existe, pero no acota el límite

La ortogonalidad de Laguerre de parámetro uno es

\[
 \int_0^\infty xe^{-x}L_j^{(1)}(x)L_k^{(1)}(x)dx
 =(k+1)\delta_{jk}.                                          \tag{16}
\]

Por ello el peso \(1/n\) de (1) produce exactamente el kernel

\[
\begin{aligned}
 \mathcal K_N(x,y)
 &:=\sum_{n=N+1}^{2N}{L_{n-1}^{(1)}(x)L_{n-1}^{(1)}(y)\over n}\\
 &=K_{2N-1}^{(1)}(x,y)-K_{N-1}^{(1)}(x,y),                   \tag{17}
\end{aligned}
\]

donde

\[
 K_M^{(1)}(x,y)
 =\sum_{k=0}^M{L_k^{(1)}(x)L_k^{(1)}(y)\over k+1}
 ={L_M^{(1)}(x)L_{M+1}^{(1)}(y)
       -L_{M+1}^{(1)}(x)L_M^{(1)}(y)\over x-y}.              \tag{18}
\]

La última fracción se entiende por continuidad cuando \(x=y\).

En particular,

\[
 \sum_{n=N+1}^{2N}{Q_{n,\varepsilon}^2\over n}
 =\sum_{m,\ell\ge2}{\Lambda(m)\Lambda(\ell)\over
 (m\ell)^{1+\varepsilon}}
 \mathcal K_N(\log m,\log\ell).                            \tag{19}
\]

Más precisamente, si
\[
 a_{m,\varepsilon}={\Lambda(m)\over m^{1+\varepsilon}},
 \qquad
 c_{n,\varepsilon}=A_n+p_n(\varepsilon),
 \qquad
 \mathcal S_{N,\varepsilon}(x)
 =\sum_{n=N+1}^{2N}{c_{n,\varepsilon}\over n}
 L_{n-1}^{(1)}(x),
\]
entonces la energía regulada completa de (13) es
\[
\boxed{
\begin{aligned}
 \mathcal E_{N,\varepsilon}
 ={}&\sum_{n=N+1}^{2N}{c_{n,\varepsilon}^2\over n}
 -2\sum_{m\ge2}a_{m,\varepsilon}
       \mathcal S_{N,\varepsilon}(\log m)\\
 &+\sum_{m,\ell\ge2}a_{m,\varepsilon}a_{\ell,\varepsilon}
       \mathcal K_N(\log m,\log\ell),
 \qquad
 \mathcal E_N=\lim_{\varepsilon\downarrow0}
       \mathcal E_{N,\varepsilon}.
\end{aligned}}                                               \tag{19a}
\]
Así (19a), no solo (19), conserva explícitamente \(A_n\), el polo y todos
los pesos \(\Lambda(m)\) antes de cualquier estimación.

Las series son absolutamente convergentes para \(\varepsilon>0\). La
positividad de Gram de \(\mathcal K_N\) hace no negativo (19), pero no da
una cota superior para la combinación firmada (13).

El fracaso es cuantitativo. De (12), para cada \(n\) fijo,

\[
 p_n(\varepsilon)=(-1)^{n-1}\varepsilon^{-n}
 \bigl(1+O_n(\varepsilon)\bigr),
 \qquad
 Q_{n,\varepsilon}=p_n(\varepsilon)+A_n-\lambda_n+o(1).      \tag{20}
\]

Por tanto, con el \(c_{n,\varepsilon}\) de (19a),

\[
\begin{aligned}
 \sum_{N<n\le2N}{c_{n,\varepsilon}^2\over n}
   &={\varepsilon^{-4N}\over2N}(1+O_N(\varepsilon)),\\
 \sum_{N<n\le2N}{Q_{n,\varepsilon}^2\over n}
   &={\varepsilon^{-4N}\over2N}(1+O_N(\varepsilon)),\\
 \sum_{N<n\le2N}{c_{n,\varepsilon}Q_{n,\varepsilon}\over n}
   &={\varepsilon^{-4N}\over2N}(1+O_N(\varepsilon)).        \tag{21}
\end{aligned}
\]

Sin embargo,

\[
 \sum_{N<n\le2N}{(c_{n,\varepsilon}-Q_{n,\varepsilon})^2\over n}
 \longrightarrow\mathcal E_N<\infty.                       \tag{22}
\]

Los dos términos positivos y el término cruzado de (22) cancelan todas las
potencias negativas hasta orden \(\varepsilon^{-4N}\). Una estimación
separada necesitaría precisión relativa \(O_N(\varepsilon^{4N})\) para
recuperar siquiera una cota \(O_N(1)\). La desigualdad triangular, Bessel o
el descarte del término cruzado da en cambio una cantidad que diverge como
\(\varepsilon^{-4N}\).

Equivalentemente, (15)--(18) escriben el cuadrado prima--polo como

\[
 \iint\mathcal K_N(x,y)\,d\nu_\varepsilon(x)d\nu_\varepsilon(y), \tag{23}
\]

pero ninguna cota por variación total sobrevive al límite. Controlar (23)
con signo y uniformemente en \(N\) sería un teorema aritmético nuevo; por el
Teorema 2.1, una cota subexponencial para la energía **completa** ya implica
RH.

---

## 5. Cierre del ataque

Se obtienen dos identidades útiles: Parseval completo (13) y el kernel
cross-degree (17)--(19). No se obtiene la cota buscada.

* El lado analítico vuelve al polo interior \(w_\rho\), con tasa exacta
  \(r_0^{-1}\) en (5) y explosión (11).
* El lado aritmético vuelve a la cancelación prima--polo: CD solo controla
  una de tres piezas de tamaño \(\varepsilon^{-4N}\).
* La positividad de la energía elimina el signo de A1 y por ello exige una
  cota superior RH-strength, no una desigualdad automática.

**Estado:** no-go cuantitativo para el ataque cross-degree basado únicamente
en Parseval, ortogonalidad de Laguerre o positividad de
Christoffel--Darboux. Un sucesor tendría que aportar una estimación firmada
de (23) que conserve la compensación de \(\nu_\varepsilon\); esas identidades
por sí solas no la contienen.
