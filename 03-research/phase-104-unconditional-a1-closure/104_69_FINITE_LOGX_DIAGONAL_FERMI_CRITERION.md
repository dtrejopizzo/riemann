# 104_69 — Criterio Fermi finito en \(\log X\) y diagonal Euler única

**Resultado.** Defina

\[
 a_n={1\over1+(n+1)e^{\lambda_n}},\qquad
 \mathfrak F(X)={1\over H_X}\sum_{n\le X}{a_n\over n},
 \qquad H_X=\sum_{n\le X}{1\over n}.                       \tag{1}
\]

Entonces

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \mathfrak F(X)\longrightarrow0.}                          \tag{2}
\]

Además, con

\[
 \varepsilon_X=e^{-X/100},                                \tag{3}
\]

todos los grados \(1\le n\le X\) pueden sustituirse simultáneamente por su
forma prima--Laguerre regulada. La diferencia entre las dos medias tiende
exponencialmente a cero y, para cada \(X\), queda una sola fórmula Euler
absolutamente convergente.

Esto normaliza en forma finita el frente de 104_61--104_66. No aporta una
cota superior nueva para (1), A1 ni RH.

**No duplicación interna.** 104_68 usa los mismos \(a_n\) dentro de
ventanas deterministas y conserva el orden
\(\varepsilon\downarrow0\) con la ventana fija. Aquí el observable es la
media logarítmica global y la aportación nueva es eliminar ese límite
interno mediante el regulador único \(\varepsilon_X=e^{-X/100}\), uniforme
en todos los grados \(n\le X\).

---

## 1. Criterio logarítmico finito

La elección \(t=1\), \(b_n=\log(n+1)\) en 104_61 da exactamente

\[
 {1\over1+\exp(\lambda_n+b_n)}
 ={1\over1+(n+1)e^{\lambda_n}}=a_n.                        \tag{4}
\]

**Teorema 1.1.** La equivalencia (2) es incondicional.

**Demostración.** Bajo RH, Li da \(\lambda_n\ge0\), luego

\[
 0\le a_n\le{1\over n+2},\qquad
 0\le\sum_{n\le X}{a_n\over n}
 \le\sum_{n\ge1}{1\over n(n+2)}={3\over4}.                \tag{5}
\]

Como \(H_X\to\infty\), \(\mathfrak F(X)\to0\).

Si RH es falsa, 104_56 produce \(c>0\), \(R>1\) y un conjunto \(D\) de
densidad natural \(d>0\) tales que

\[
 \lambda_n\le-cR^n\qquad(n\in D)                           \tag{6}
\]

desde algún índice. En \(D\),

\[
 (n+1)e^{\lambda_n}\le(n+1)e^{-cR^n}\longrightarrow0,
 \qquad a_n\longrightarrow1.                              \tag{7}
\]

La densidad natural implica la densidad logarítmica,

\[
 {1\over H_X}\sum_{\substack{n\le X\\n\in D}}{1\over n}
 \longrightarrow d,                                       \tag{8}
\]

y por tanto

\[
 \liminf_{X\to\infty}\mathfrak F(X)\ge d>0.                \tag{9}
\]

Esto prueba (2) y también

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \liminf_{X\to\infty}\mathfrak F(X)=0.}                    \tag{10}
\]
\(\square\)

---

## 2. Aproximación simultánea de los primeros \(X\) grados

Use la regularización de 104_66:

\[
\begin{aligned}
 \lambda_{n,\varepsilon}
 &=A_n+p_n(\varepsilon)-Q_{n,\varepsilon},\\
 Q_{n,\varepsilon}
 &=\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m).
\end{aligned}                                             \tag{11}
\]

La generatriz emparejada y el disco desplazado de 104_66 prueban, para

\[
 r={199\over200},\qquad M=M_{199/200}<\infty,
\]

que

\[
 |\lambda_{n,\varepsilon}-\lambda_n|
 \le2Mn\varepsilon r^{-n}
 \qquad(0<\varepsilon\le1/2).                              \tag{12}
\]

Ponga

\[
 C={1\over100},\qquad
 \eta=C-\log{200\over199}>0.                               \tag{13}
\]

Para todo entero \(X\ge70\), \(\varepsilon_X\le1/2\). Si \(n\le X\),

\[
\begin{aligned}
 |\lambda_{n,\varepsilon_X}-\lambda_n|
 &\le2MXe^{-X/100}\left({200\over199}\right)^X\\
 &=2MXe^{-\eta X}.
\end{aligned}                                             \tag{14}
\]

Así,

\[
 \boxed{\sup_{1\le n\le X}
 |\lambda_{n,\varepsilon_X}-\lambda_n|
 \le2MXe^{-\eta X}\longrightarrow0.}                      \tag{15}
\]

No hay cola en el grado: un mismo regulador aproxima todos los sumandos de
(1).

---

## 3. Criterio diagonal finito

Defina

\[
 a_{n,\varepsilon}
 ={1\over1+(n+1)e^{\lambda_{n,\varepsilon}}},
\qquad
 \mathfrak F_\varepsilon(X)
 ={1\over H_X}\sum_{n\le X}{a_{n,\varepsilon}\over n}.     \tag{16}
\]

La derivada de \(x\mapsto(1+e^x)^{-1}\) tiene módulo a lo sumo \(1/4\).
Usando (15),

\[
\begin{aligned}
 |\mathfrak F_{\varepsilon_X}(X)-\mathfrak F(X)|
 &\le {1\over4H_X}\sum_{n\le X}{1\over n}
 |\lambda_{n,\varepsilon_X}-\lambda_n|\\
 &\le {M\over2}Xe^{-\eta X}.
\end{aligned}                                             \tag{17}
\]

**Teorema 3.1 (criterio diagonal finito).**

\[
 \boxed{
 \mathfrak F_{\varepsilon_X}(X)-\mathfrak F(X)\to0,\qquad
 \mathrm {RH}\Longleftrightarrow
 \liminf_{X\to\infty}\mathfrak F_{\varepsilon_X}(X)=0.}    \tag{18}
\]

La constante exponencial es explícita; \(M\) es un factor fijo sobre el
compacto cero-libre de 104_66 y no afecta el límite.

---

## 4. Una sola fórmula Euler prima--Laguerre

Sustituyendo (11) en (16), para cada \(X\ge70\),

\[
\boxed{
\begin{aligned}
 \mathfrak F_{\varepsilon_X}(X)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 \Bigg[1
 &+(n+1)e^{A_n+p_n(\varepsilon_X)}\\
 &\times\prod_{m\ge2}
 \exp\!\left(
 -{\Lambda(m)\over m^{1+\varepsilon_X}}
 L_{n-1}^{(1)}(\log m)\right)
 \Bigg]^{-1}.
\end{aligned}}                                            \tag{19}
\]

Como \(\varepsilon_X>0\),

\[
 \sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon_X}}
 |L_{n-1}^{(1)}(\log m)|<\infty\qquad(n\le X).             \tag{20}
\]

El producto converge absolutamente y la suma exterior es finita. La
fórmula conserva juntos Gamma, polo, primos y potencias primas hasta después
de formar la logística. No contiene un límite
\(\varepsilon\downarrow0\). La cola efectiva de 104_61 permite truncarla,
pero no da una cota uniforme útil cuando \(X\to\infty\).

---

## 5. Falsificador off-line

Para

\[
 Q_n=4-2\mathrm{Re}\,\{(2i)^n+(2i)^{-n}\},            \tag{21}
\]

ponga \(a_n^Q=[1+(n+1)e^{Q_n}]^{-1}\). Entonces

\[
\begin{array}{c|c|c}
 n\bmod4&Q_n&a_n^Q\\ \hline
 0&-2^{n+1}+O(1)&1+o(1)\\
 1,3&4&O(1/n)\\
 2&+2^{n+1}+O(1)&o(1).
\end{array}                                                \tag{22}
\]

Los errores son sumables después de multiplicar por \(1/n\), mientras

\[
 \sum_{\substack{n\le X\\4\mid n}}{1\over n}
 ={1\over4}H_{\lfloor X/4\rfloor}
 ={1\over4}H_X+O(1).
\]

Por consiguiente,

\[
 \boxed{{1\over H_X}\sum_{n\le X}{a_n^Q\over n}
 \longrightarrow{1\over4}.}                              \tag{23}
\]

El criterio rechaza el divisor off-line. Una prueba basada solo en
convergencia absoluta, positividad de pesos o módulos unitarios no puede
declarar automáticamente que (19) tiende a cero.

---

## 6. Costo de separar polo y primos

El término polar exacto es

\[
 p_n(\varepsilon)
 =1+(-1)^{n-1}
 \left({1-\varepsilon\over\varepsilon}\right)^n.           \tag{24}
\]

En \(n=X\),

\[
\begin{aligned}
 \log|p_X(\varepsilon_X)-1|
 &=X\log(e^{X/100}-1)\\
 &={X^2\over100}+X\log(1-e^{-X/100})
 ={X^2\over100}+o(1).
\end{aligned}                                             \tag{25}
\]

Pero

\[
 Q_{n,\varepsilon_X}
 =p_n(\varepsilon_X)+A_n-\lambda_{n,\varepsilon_X}.       \tag{26}
\]

El residuo emparejado crece como máximo \(\exp(O(X))\), mientras los dos
canales separados alcanzan \(\exp(X^2/100+o(1))\). Recuperar su diferencia
exige precisión relativa

\[
 \boxed{\exp\{-X^2/100+O(X)\}.}                            \tag{27}
\]

Tomar módulos, truncar un canal o estimar sus fases por separado destruye
esta precisión. Combinarlos exactamente devuelve (19). Es un costo de
condicionamiento, no un no-go para toda identidad firmada futura.

---

## 7. Veredicto

**Probado:** (2)/(10), la aproximación uniforme (15), el criterio diagonal
(18), la fórmula Euler absoluta (19), el valor \(1/4\) del cuarteto y el
costo (27).

**Ganancia:** la formulación final no necesita Abel, suma exterior infinita
ni límite del regulador. Para cada \(X\) es finita en el grado y
absolutamente convergente en la aritmética.

**No probado:** que (19) tienda a cero para los pesos reales
\(\Lambda(m)\), A1 o RH.

---

## 8. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 finite_logx_diagonal_fermi_check.py
```

El checker verifica la constante diagonal, la identidad polar, el límite
\(1/4\) del cuarteto y las escalas (15), (25). Los teoremas analíticos se
prueban en el texto.
