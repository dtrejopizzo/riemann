# 104_71 — Ataque variacional entrópico sobre bloques deterministas

**Resultado.** La función de partición no interactuante de `104_68` admite
una representación probabilística exacta y una dualidad de
Gibbs--Donsker--Varadhan finita. Para

\[
 I_L=\{L^2,L^2+1,\ldots,L^2+L-1\},\qquad
 \pi_n:={1\over n+2},                                    \tag{1}
\]

sea \(\nu_L=\bigotimes_{n\in I_L}\mathrm{Bern}(\pi_n)\), escriba
\(B=(B_n)_{n\in I_L}\), y ponga

\[
 Y_L(B)=\sum_{n\in I_L}B_n\lambda_n,\qquad
 Z_L=\mathbb E_{\nu_L}e^{-Y_L}.                           \tag{2}
\]

Entonces

\[
 \boxed{
 P_L^{-1}=C_LZ_L,\qquad
 C_L={L^2+L+1\over L^2+1}.}                               \tag{3}
\]

En particular,

\[
 \boxed{
 \mathrm{RH}\Longrightarrow Z_L\longrightarrow1,
 \qquad
 \neg\mathrm{RH}\Longrightarrow Z_L\longrightarrow\infty.} \tag{4}
\]

La dualidad entrópica traduce (4) a una cota uniforme sobre perfiles
\(q=(q_n)\), y el lift prima--Laguerre conserva todos los grados dentro del
polinomio combinado

\[
 G_{L,q}(x)=\sum_{n\in I_L}q_nL_{n-1}^{(1)}(x).            \tag{5}
\]

Sin embargo, la auditoría es negativa: la entropía no crea una interacción
entre grados. Toda medida correlacionada paga exactamente su información
total (multiinformación), el maximizador es nuevamente producto, y la función de partición se
refactoriza sitio por sitio. Este documento obtiene una forma
variacional exacta del blanco; no prueba su cota, A1 ni RH.

> **Notación.** La probabilidad Bernoulli \(\pi_n\) es el \(p_n=1/(n+2)\)
> del enunciado del ataque. Se usa \(\mathfrak p_n(\varepsilon)\) para el
> término polar de la identidad prima--Laguerre, evitando la colisión de
> símbolos.

---

## 1. Identidad Bernoulli y telescopía exacta

Recuerde de `104_68` que

\[
 a_n={1\over1+(n+1)e^{\lambda_n}},\qquad
 P_L=\prod_{n\in I_L}(1-a_n).                             \tag{6}
\]

Como

\[
 (1-a_n)^{-1}=1+{e^{-\lambda_n}\over n+1},                \tag{7}
\]

y \(B_n\sim\mathrm{Bern}(\pi_n)\),

\[
\begin{aligned}
 \mathbb E e^{-B_n\lambda_n}
 &=1-\pi_n+\pi_ne^{-\lambda_n}\\
 &={n+1\over n+2}
   \left(1+{e^{-\lambda_n}\over n+1}\right).
\end{aligned}                                             \tag{8}
\]

La independencia da

\[
 Z_L=\prod_{n\in I_L}{n+1\over n+2}\,P_L^{-1}.           \tag{9}
\]

Si \(N=L^2\) y \(M=L^2+L-1\), el prefactor telescópico es

\[
 \prod_{n=N}^{M}{n+1\over n+2}
 ={N+1\over M+2}
 ={L^2+1\over L^2+L+1}=C_L^{-1}.                         \tag{10}
\]

Esto prueba (3) sin límite ni aproximación.

### 1.1 Dicotomía

Bajo RH, `104_68` prueba \(P_L\to1\); además \(C_L\to1\). Por (3),
\(Z_L\to1\). Si RH es falsa, el mismo documento prueba \(P_L\to0\),
mientras \(1<C_L<2\), y por tanto \(Z_L=P_L^{-1}/C_L\to\infty\).
Así (4) se refuerza a la equivalencia

\[
 \boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad Z_L\longrightarrow1.}    \tag{11}
\]

La esperanza no promedia linealmente los coeficientes: una sola excursión
\(\lambda_d\ll0\) produce el factor \(\pi_de^{-\lambda_d}\) y domina todo
el bloque.

---

## 2. Dualidad finita de Gibbs--Donsker--Varadhan

Para probabilidades \(\mu,\nu\) sobre \(\{0,1\}^{I_L}\), use

\[
 D(\mu\Vert\nu)=\sum_b\mu(b)\log{\mu(b)\over\nu(b)},      \tag{12}
\]

con la convención \(0\log0=0\). Como \(\nu_L\) tiene soporte total, la
identidad variacional finita es

\[
 \boxed{
 \log Z_L
 =\sup_{\mu}
 \{-\mathbb E_\mu Y_L-D(\mu\Vert\nu_L)\}.}               \tag{13}
\]

En efecto, para

\[
 {d\mu_L^*\over d\nu_L}(b)={e^{-Y_L(b)}\over Z_L},        \tag{14}
\]

se tiene exactamente

\[
 -\mathbb E_\mu Y_L-D(\mu\Vert\nu_L)
 =\log Z_L-D(\mu\Vert\mu_L^*)\leq\log Z_L.              \tag{15}
\]

### 2.1 Reducción a perfiles de una coordenada

Sea \(q_n=\mathbb E_\mu B_n\) y
\(\nu_q=\bigotimes_{n\in I_L}\mathrm{Bern}(q_n)\). La regla de la
cadena para la entropía da

\[
 D(\mu\Vert\nu_L)
 =D(\mu\Vert\nu_q)
  +\sum_{n\in I_L}d(q_n\Vert\pi_n),                       \tag{16}
\]

donde

\[
 d(q\Vert p)=q\log{q\over p}+(1-q)\log{1-q\over1-p}.     \tag{17}
\]

Como \(\mathbb E_\mu Y_L=\sum_nq_n\lambda_n\), las correlaciones solo
restan el término no negativo \(D(\mu\Vert\nu_q)\). Por tanto (13) es
exactamente

\[
 \boxed{
 \log Z_L
 =\sup_{q\in[0,1]^{I_L}}
 \left\{-\sum_{n\in I_L}q_n\lambda_n
 -\sum_{n\in I_L}d(q_n\Vert\pi_n)\right\}.}              \tag{18}
\]

El funcional es estrictamente cóncavo en el interior y su maximizador es

\[
 q_n^*={\pi_ne^{-\lambda_n}
       \over1-\pi_n+\pi_ne^{-\lambda_n}}
 ={1\over1+(n+1)e^{\lambda_n}}=a_n.                      \tag{19}
\]

Así \(\mu_L^*=\bigotimes_n\mathrm{Bern}(a_n)\), y (18) vuelve a
factorizar:

\[
 \log Z_L
 =\sum_{n\in I_L}\log(1-\pi_n+\pi_ne^{-\lambda_n}).     \tag{20}
\]

La aparente interacción del supremo sobre medidas desaparece exactamente.

---

## 3. Forma prima--Laguerre combinada

Escriba la identidad regulada con la notación separada

\[
\begin{aligned}
 \lambda_{n,\varepsilon}
 &=A_n+\mathfrak p_n(\varepsilon)-Q_{n,\varepsilon},\\
 Q_{n,\varepsilon}
 &=\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
   L_{n-1}^{(1)}(\log m).
\end{aligned}                                             \tag{21}
\]

Defina

\[
 Y_{L,\varepsilon}=\sum_{n\in I_L}B_n\lambda_{n,\varepsilon},
 \qquad Z_{L,\varepsilon}=\mathbb E_{\nu_L}e^{-Y_{L,\varepsilon}}.
                                                                    \tag{22}
\]

Para \(\varepsilon>0\), la suma Euler es absolutamente convergente. Al
sustituir (21) en (18) y reunir primero todos los grados, resulta

\[
 \boxed{
 \log Z_{L,\varepsilon}
 =\sup_{q\in[0,1]^{I_L}}\mathcal V_{L,\varepsilon}(q),}   \tag{23}
\]

con

\[
\begin{aligned}
 \mathcal V_{L,\varepsilon}(q)
 ={}&\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
       G_{L,q}(\log m)\\
 &-\sum_{n\in I_L}q_n
       \{A_n+\mathfrak p_n(\varepsilon)\}
 -\sum_{n\in I_L}d(q_n\Vert\pi_n).
\end{aligned}
\tag{24}
\]

\[
 G_{L,q}(x)=\sum_{n\in I_L}q_nL_{n-1}^{(1)}(x).          \tag{25}
\]

Esta es la forma combinada solicitada: el perfil \(q\) se aplica antes de
estimar la suma de Mangoldt, y primos y potencias primas aparecen juntos
contra un único polinomio \(G_{L,q}\).

### 3.1 Una sola diagonal

Use exactamente la diagonal de `104_68`:

\[
 N_L=L^2+L-1,\qquad
 \varepsilon_L=e^{-N_L/100},\qquad
 \eta={1\over100}-\log{200\over199}>0.                   \tag{26}
\]

Existe \(M<\infty\), independiente de \(L\), tal que, para \(L\)
suficientemente grande,

\[
 \sup_{n\in I_L}|\lambda_{n,\varepsilon_L}-\lambda_n|
 \leq2MN_Le^{-\eta N_L}=: \delta_L.                      \tag{27}
\]

Para cualquier configuración \(b\),

\[
 |Y_{L,\varepsilon_L}(b)-Y_L(b)|\leq L\delta_L.           \tag{28}
\]

Comparar término a término las dos sumas exponenciales, o usar (13), da

\[
 \boxed{
 |\log Z_{L,\varepsilon_L}-\log Z_L|
 \leq L\delta_L\longrightarrow0.}                        \tag{29}
\]

En consecuencia,

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \sup_{q\in[0,1]^{I_L}}
 \mathcal V_{L,\varepsilon_L}(q)\longrightarrow0.}       \tag{30}
\]

El perfil \(q=0\) da la cota inferior automática

\[
 \mathcal V_{L,\varepsilon_L}(0)
 =\sum_{n\in I_L}\log(1-\pi_n)
 =-\log C_L\longrightarrow0.                             \tag{31}
\]

### 3.2 El blanco realmente débil

El límite cero de (30) es exacto, pero es mucho más fuerte de lo necesario
para excluir un cero exterior. Bajo no-RH, el conjunto sindético de
excursiones negativas de `104_56` corta cada \(I_L\), para \(L\) grande, en
algún \(d_L\) tal que

\[
 \lambda_{d_L}\leq-cR^{d_L},\qquad R>1.
\]

Todos los factores Bernoulli distintos de \(d_L\) son al menos
\(1-\pi_n\). Usando (10),

\[
 Z_L\geq {e^{-\lambda_{d_L}}\over(d_L+1)C_L},
 \qquad
 \log Z_L\geq cR^{L^2}-O(\log L).                        \tag{32}
\]

La misma cota vale para \(Z_{L,\varepsilon_L}\), salvo \(o(1)\), por
(29). En consecuencia se obtiene el criterio estrictamente más débil

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \liminf_{L\to\infty}\log Z_{L,\varepsilon_L}<\infty.}  \tag{33}
\]

Equivalentemente, basta una cota superior sobre una subsucesión no acotada.
Más generalmente, sea \(B_L\geq0\) cualquier slack prefijado con

\[
 \log(1+B_L)=o(L^2).                                     \tag{34}
\]

Si para una sucesión \(L_j\to\infty\)

\[
 \boxed{
 \sum_{n\in I_{L_j}}q_n\lambda_{n,\varepsilon_{L_j}}
 \geq-\sum_{n\in I_{L_j}}d(q_n\Vert\pi_n)-B_{L_j}
 \quad\text{para todo }q\in[0,1]^{I_{L_j}},}             \tag{35}
\]

entonces RH es verdadera. La jerarquía admisible incluye \(B_L=O(1)\),
todo slack polinómico, y en general \(B_L=\exp(o(L^2))\). No es necesario
probar convergencia a cero.

En las coordenadas aritméticas, (35) es precisamente

\[
\boxed{
 \begin{aligned}
 &\sum_{n\in I_{L_j}}q_n
       \{A_n+\mathfrak p_n(\varepsilon_{L_j})\}
 -\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon_{L_j}}}
       G_{L_j,q}(\log m)\\
 &\hspace{22mm}\geq
 -\sum_{n\in I_{L_j}}d(q_n\Vert\pi_n)-B_{L_j}
 \quad\text{uniformemente en }q.
 \end{aligned}}                                          \tag{36}
\]

La condición con \(B_L=O(1)\) es la forma de coercividad entrópica más
limpia; (34)--(36) registran que incluso ella puede relajarse hasta escala
\(\exp(o(L^2))\). Ninguna de estas cotas se prueba aquí.

---

## 4. Auditoría de interacción

La dualidad entrópica parece introducir una competencia colectiva entre
grados. La identidad (16) decide el punto exactamente:

\[
 \underbrace{-\mathbb E_\mu Y_L
 -D(\mu\Vert\nu_L)}_{\text{funcional correlacionado}}
 =\underbrace{-\sum_nq_n\lambda_n
 -\sum_nd(q_n\Vert\pi_n)}_{\text{funcional producto}}
 -\underbrace{D(\mu\Vert\nu_q)}_{\text{costo de correlación}}. \tag{37}
\]

Toda interacción probabilística disminuye el funcional. Equivalentemente,
el Hessiano de (18) es diagonal,

\[
 {\partial^2\over\partial q_n\partial q_k}
 \left[-\sum_jq_j\lambda_j-\sum_jd(q_j\Vert\pi_j)\right]
 =-{\mathbf1_{n=k}\over q_n(1-q_n)}.                     \tag{38}
\]

El polinomio \(G_{L,q}\) de (25) es útil para conservar grados juntos al
aplicar una hipotética cota aritmética, pero no cambia este hecho: la suma
Euler de (24) es lineal en \(G_{L,q}\), por tanto lineal en \(q\). Al
resolver el supremo se recuperan las actividades independientes de
`104_68`.

**Veredicto del gate.** La entropía produce una penalización convexa y una
formulación uniforme legítima, pero no una reserva conectada entre grados.
No evita la cancelación polo--primos dentro de cada
\(\lambda_{n,\varepsilon_L}\), cuyo condicionamiento ya fue cuantificado en
`104_66`--`104_69`.

---

## 5. Falsificador off-line

Considere otra vez el cuarteto racional

\[
 Q_n=4-2\mathrm{Re}\,\{(2i)^n+(2i)^{-n}\}.           \tag{39}
\]

Cada \(I_L\), para \(L\geq4\), contiene un índice
\(d_L\equiv0\pmod4\), y

\[
 -Q_{d_L}\geq2^{d_L}.                                    \tag{40}
\]

El factor Bernoulli de ese sitio, junto con la cota
\(1-\pi_n\) para todos los demás, da

\[
 Z_L^Q\geq {e^{-Q_{d_L}}\over(d_L+1)C_L}
 \geq{e^{2^{d_L}}\over(d_L+1)C_L}\longrightarrow\infty. \tag{41}
\]

La misma obstrucción aparece dentro de la dualidad. Tome
\(q_{d_L}=1\) y \(q_n=0\) para \(n\neq d_L\). Entonces

\[
 -\sum_nq_nQ_n-\sum_nd(q_n\Vert\pi_n)
 =-Q_{d_L}-\log(d_L+1)-\log C_L
 \geq2^{d_L}-\log(d_L+1)-\log C_L.                       \tag{42}
\]

Por tanto el supremo diverge y el criterio rechaza el modelo off-line en
cada ventana grande. El falsificador pasa; no suministra la cota (32) para
los pesos reales \(\Lambda(m)\).

---

## 6. Balance

**Probado.** La identidad telescópica (3), la dicotomía (4), la dualidad
finita (13), su reducción exacta a perfiles (18), el maximizador (19), la
forma combinada prima--Laguerre (23)--(25), el transporte por la diagonal
(29), y el falsificador (39)--(42).

**Ganancia.** El objetivo de bloque queda convertido en una sola cota
unilateral uniforme sobre polinomios Laguerre \(G_{L,q}\), con una suma
Euler absolutamente convergente para cada \(L\). Basta esa cota en una
subsucesión y con slack tan grande como \(\exp(o(L^2))\).

**No-go.** La entropía relativa no crea interacción: la información mutua
penaliza todas las correlaciones y el optimizador es producto. La función de
partición refactoriza exactamente a los mismos sitios de `104_68`.

**No probado.** La cota uniforme (36), el límite (30), un bloque nuevo de
coeficientes reales, A1 o RH.

---

## 7. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 entropic_block_variational_check.py
```

El checker usa `Fraction` para (3), (8)--(10) y una enumeración Bernoulli
finita. En punto flotante verifica (13), (16), (18)--(20), la identidad
prima--Laguerre combinada sobre una suma Euler finita de prueba, la caída de
la envolvente diagonal y el testigo off-line. No comprueba (36).
