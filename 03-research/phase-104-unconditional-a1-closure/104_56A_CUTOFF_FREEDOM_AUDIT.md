# 104_56A — Auditoría de libertad del cutoff y margen cuarto estricto

**Objeto.** Auditar la propuesta de reemplazar el gate uniforme

\[
 {2002\over501}\lambda_n-A_n\ge0
\]

por el gate puntual estricto

\[
 \boxed{\;4\lambda_n>A_n.\;}                         \tag{1}
\]

El veredicto tiene dos partes. La mejora de A0 vale para **todo** cutoff
posterior, y (1) permite escoger existencialmente un cutoff que satisface A1.
Pero ese cutoff depende de la holgura
\(\delta_n=\lambda_n-A_n/4\). Por tanto la reducción es correcta como
implicación condicional, no suministra un cutoff a priori con el cual probar
la propia holgura.

## 1. Notación sin la colisión de \(B_n\)

Póngase

\[
 A_n=\lambda_n^{\rm arch}>0,\qquad
 \delta_n:=\lambda_n-{A_n\over4},\qquad
 R_n(T):=-\int_T^\infty E(u)K_n(u)\,du,
\]

\[
 C_n(T)=\lambda_n-{A_n\over4}-R_n(T)
       =\delta_n-R_n(T).                              \tag{2}
\]

En `102_A0_UNIFORM_TAIL_THEOREM.md` la letra \(B_n\) denota una cota
inferior positiva para \(A_n\); en documentos posteriores denota a veces
\(A_n-\lambda_n\). Para evitar esa colisión escribiremos aquí
\(b_n^{\rm A0}\), con

\[
 0<b_n^{\rm A0}\le A_n.                              \tag{3}
\]

Sea \(T_n^0\) cualquier cutoff para el cual la condición (B) de A0 vale:

\[
 \eta(u)\ge(n+1)\log(1+u)+
 \log {12An^2\over b_n^{\rm A0}}
 \qquad(u\ge T_n^0).                                \tag{4}
\]

## 2. Lema cofinal de A0

**Lema 2.1.** Para todo \(T\ge T_n^0\),

\[
 \boxed{
 |R_n(T)|\le {b_n^{\rm A0}\over4(1+T)}
             \le {A_n\over4(1+T)}.}                 \tag{5}
\]

**Demostración.** Si (4) vale para todo \(u\ge T_n^0\), vale a fortiori
para todo \(u\ge T\) cuando \(T\ge T_n^0\). Se repite la última línea de
la prueba de A0 empezando en \(T\):

\[
\begin{aligned}
 |R_n(T)|
 &\le3An^2\int_T^\infty(1+u)^{n-1}e^{-\eta(u)}\,du\\
 &\le {b_n^{\rm A0}\over4}
       \int_T^\infty(1+u)^{-2}\,du
  ={b_n^{\rm A0}\over4(1+T)}.
\end{aligned}
\]

La segunda desigualdad de (5) es (3). \(\square\)

Así, la frase correcta es: **agrandar el cutoff mejora la envolvente
absoluta de A0**. No implica que \(C_n(T)\) sea monótona; de hecho

\[
 C_n'(T)=-E(T)K_n(T)
\]

no tiene signo conocido (`153_CUTOFF_COMPARISON_AND_MONOTONICITY_GATE.md`).

La misma conclusión se lee directamente en `104_01`: su condición
(B\(_\theta\)) se exige para todo \(u\ge T\), de modo que todo cutoff mayor
sigue siendo admisible. Para \(\theta=1/4\), esa normalización corresponde
a tomar \(b_n^{\rm A0}=A_n\).

## 3. Teorema del cutoff adaptado

**Teorema 3.1.** Supóngase \(\delta_n>0\). Toda elección que cumpla

\[
 T\ge T_n^0,\qquad 1+T>{A_n\over4\delta_n}           \tag{6}
\]

satisface \(C_n(T)>0\), y por tanto A1 en ese cutoff.

En particular sirve la elección explícita como número real

\[
 \boxed{
 \widetilde T_n:=\max\left\{T_n^0,{A_n\over4\delta_n}\right\}.} \tag{7}
\]

**Demostración.** Por (2), (5) y (6),

\[
 C_n(T)\ge\delta_n-|R_n(T)|
 \ge\delta_n-{A_n\over4(1+T)}>0.                    \tag{8}
\]

El colapso de A1 está probado para todo cutoff A0 admisible, luego (8) es
exactamente A1\(_n(T)\). \(\square\)

No hay una restricción oculta que obligue a usar el mínimo
\(T_n(1/4)\). El teorema A0 dice «si \(T_n\) es elegido de modo que», y el
colapso de A1 vale para todo cutoff A0. Tampoco hay un problema de endpoint:
la carga del endpoint móvil es cero porque \(\omega_n(T_n)=0\). Si se desea
conservar una sucesión estrictamente creciente, se define recursivamente

\[
 \widetilde T_n=max\left\{T_n^0,\widetilde T_{n-1}+1,
                      {A_n\over4\delta_n}\right\};             \tag{9}
\]

el Lema 2.1 sigue aplicando.

**Corolario 3.2 (cuantificadores exactos).**

\[
 \left[\forall n\ge150:\ 4\lambda_n>A_n\right]
 \Longrightarrow
 \left[\exists(\widetilde T_n)_{n\ge150}\quad
       \forall n\ge150:\ {\rm A1}_n(\widetilde T_n)\right]. \tag{10}
\]

Junto con los certificados \(1\le n\le149\), cualquiera de los dos lados
de la implicación conduce a \(\lambda_n>0\) para todo \(n\), y por Li a RH.
De hecho el desvío por A1 no es lógicamente necesario una vez probado el
lado izquierdo: \(A_n>0\) y \(4\lambda_n>A_n\) ya dan \(\lambda_n>0\).

## 4. Qué pasa con el cutoff fijado de antemano

Si se conserva un cutoff **prescrito** \(T_n^0\), A0\(^+\) solo suministra
el suficiente

\[
 \lambda_n\ge
 \left({1\over4}+{1\over4(1+T_n^0)}\right)A_n
 ={T_n^0+2\over4(T_n^0+1)}A_n.                    \tag{11}
\]

Equivalentemente,

\[
 r\lambda_n-A_n\ge0,\qquad
 r\le r_{\max}(T_n^0):={4(1+T_n^0)\over T_n^0+2}. \tag{12}
\]

Por tanto `104_23` es correcto, pero \(2002/501\) es únicamente la mejor
constante **uniforme deducida del piso bruto** \(T_n^0\ge1000\). No es la
mejor constante de los cutoffs computados índice por índice. Con la versión
actual de `theta_family_check.py` se obtiene diagnósticamente

\[
 T_{1000}(1/4)\simeq6.9160\times10^8,\qquad
 {1\over r_{\max}}\simeq0.2500000003615,
\]

y el sobrecosto A0 correspondiente es aproximadamente
\(8.40\times10^{-7}\). Estas cifras son coma flotante y no intervienen en
el teorema.

Hay que distinguir tres objetos:

1. la condición exacta en un cutoff fijado es
   \(C_n(T)\ge0\iff\delta_n\ge R_n(T)\);
2. la condición (11) es un suficiente sin signo obtenido sustituyendo
   \(R_n(T)\) por \(|R_n(T)|\);
3. con cutoff adaptado y \(\delta_n>0\), el Lema 2.1 permite hacer ese
   suficiente verdadero moviendo \(T\) hacia infinito.

Por ello no es exacto llamar a
\(A_n-\lambda_n<3A_n/4\) «la A1 exacta»: es el **umbral cofinal suficiente
sin información de signo**. A1 puede valer en un cutoff concreto incluso
si ese umbral falla, por ejemplo si \(R_n(T)<0\) compensa el déficit.

## 5. Auditoría de circularidad

La elección (7) no es circular dentro de la implicación (10): bajo la
hipótesis \(\delta_n>0\), el número \(\widetilde T_n\) está bien definido y
la prueba es válida. Una elección puede depender de \(n\); A0 nunca exige
un cutoff uniforme en \(n\).

Sí sería circular usar (7) como **mecanismo para probar**
\(\delta_n>0\):

- (7) presupone el signo y el tamaño de la misma holgura que queda por
  demostrar;
- sin una cota inferior independiente para \(\delta_n\), no produce un
  cutoff numérico a priori derivado únicamente de PNT;
- probar A1 en ese cutoff no retroprueba \(4\lambda_n>A_n\): A1+A0 solo
  entrega \(\lambda_n\ge0\).

En resumen, la libertad del cutoff elimina correctamente el slack
proporcional fijo de `104_23`, pero no elimina el teorema RH-strength. Lo
reemplaza por el gate estricto

\[
 \boxed{
 4\lambda_n>A_n\quad(n\ge150)
 \quad\Longleftrightarrow\quad
 A_n-\lambda_n<{3\over4}A_n\quad(n\ge150),}       \tag{13}
\]

como suficiente cofinal. La novedad es cuantitativa: ya no hace falta una
holgura proporcional uniforme. La dificultad lógica central permanece.

## 6. Veredicto

| Afirmación propuesta | Veredicto |
|---|---|
| A0\(^+\) vale para todo \(T\ge T_n^0\) | **Correcta** |
| El cutoff puede depender de \(n\) | **Correcta; ya estaba permitido** |
| \(4\lambda_n>A_n\) permite escoger un cutoff que cierre A1 | **Correcta, existencialmente** |
| Ese cutoff puede fijarse desde PNT sin conocer la holgura | **No demostrado** |
| \(4\lambda_n>A_n\) prueba RH con los certificados finitos | **Correcta, incluso sin pasar por A1** |
| \(B_n<3A_n/4\) es equivalente a la A1 de un cutoff canónico fijo | **Falsa en general** |
| \(2002/501\) es el frente intrínseco | **Falsa; es el frente uniforme del piso \(T\ge1000\)** |

## Estado

- **Probado:** Lema 2.1, Teorema 3.1 y Corolario 3.2.
- **Corrección aceptada:** el margen proporcional \(A_n/1001\) no es
  intrínseco si se permite un cutoff adaptado.
- **Salvedad vinculante:** la adaptación usa la holgura RH-strength y no
  constituye una prueba de ella.
- **A1/RH:** permanecen abiertos.
