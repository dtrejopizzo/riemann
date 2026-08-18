# 104_98 — Factorización Mellin de la energía prima y gate de monodromía

## Resultado

Ponga

\[
 L_2(x)=\int_2^x{du\over\log u},\qquad
 P_m=\pi(m)-L_2(m),\qquad P_1=0,
 \tag{1}
\]

y \(a_m=P_m-P_{m-1}\). Para \(N\ge2\), defina

\[
 \Phi_N(s)=\sum_{m=2}^N P_m\{m^{-s}-(m+1)^{-s}\}.
 \tag{2}
\]

Hay una factorización espectral finita, exacta e incondicional:

\[
 \boxed{
 \sum_{m=2}^N{P_m^2\over m(m+1)}
 ={1\over2\pi}\int_{-\infty}^{\infty}
 \left|{\Phi_N(\tfrac12+it)\over\tfrac12+it}\right|^2dt.}
 \tag{3}
\]

El borde móvil está contenido exactamente en

\[
 \boxed{
 \Phi_N(s)=\sum_{m=2}^Na_m m^{-s}-P_N(N+1)^{-s}.}
 \tag{4}
\]

Al hacer \(N\to\infty\) inicialmente en \(\Re s>1\), el símbolo literal
de los primos ordinarios es

\[
 \Phi(s)=\mathcal P(s)-D(s),\qquad
 \mathcal P(s)=\sum_p p^{-s},
 \tag{5}
\]

donde

\[
 D(s)=\sum_{m=3}^{\infty}m^{-s}
       \int_{m-1}^{m}{dx\over\log x}.
 \tag{6}
\]

Si \(E_1(z)=\int_z^\infty e^{-u}du/u\), sobre ramas compatibles se
obtiene la continuación regularizada

\[
 \boxed{
 \Phi(s)=
 \sum_{k\ge1}{\mu(k)\over k}\log\zeta(ks)
 -E_1((s-1)\log2)+R(s),}
 \tag{7}
\]

con

\[
 R(s)=\sum_{m=3}^{\infty}\int_{m-1}^{m}
       {x^{-s}-m^{-s}\over\log x}\,dx,
 \qquad R\in\mathcal O(\Re s>0).
 \tag{8}
\]

En el semiplano abierto \(\Re s>1/2\), todos los sumandos \(k\ge2\)
de (7) son regulares. El polo en \(s=1\) se cancela exactamente con
\(E_1\). Por tanto un cero \(\rho\), \(\Re\rho>1/2\), de multiplicidad
\(m_\rho\) produce y solo puede producir allí

\[
 \boxed{
 \Phi(s)=m_\rho\log(s-\rho)+h_\rho(s),\qquad
 h_\rho\ \text{ holomorfa localmente}.}
 \tag{9}
\]

La monodromía es \(2\pi i m_\rho\). Posee una diagonal positiva exacta:
en una circunferencia pequeña alrededor de \(\rho\), para todo \(c\in
\mathbb C\),

\[
 {1\over2\pi}\int_0^{2\pi}
 |\Phi(\rho+re^{i\theta})-c|^2d\theta
 \ \ge\ {\pi^2m_\rho^2\over6}.
 \tag{10}
\]

Pero (10) vive en **todas las hojas** de la continuación. La energía
prima (3) vive en una sola aproximación física por polinomios de
Dirichlet. Si \(\Phi_\pm\) son las dos orillas de un corte y
\(\Phi_0=(\Phi_++\Phi_-)/2\), entonces exactamente

\[
 \begin{aligned}
 { |\Phi_+|^2+|\Phi_-|^2\over2}
   &=|\Phi_0|^2+\pi^2m_\rho^2,\\
 |\Phi_+|^2-|\Phi_-|^2
   &=4\pi m_\rho\,\Im\Phi_0.
 \end{aligned}
 \tag{11}
\]

La primera línea tiene la diagonal buscada; la segunda línea es la
parte firmada que impide transferirla a una sola hoja. No hay una razón
de signo para \(\Im\Phi_0\). La fórmula explícita da la misma obstrucción:
el cuadrado cero--cero es una matriz de Gram positiva como conjunto, pero
sus entradas fuera de la diagonal y aun el término de frecuencia doble
de un solo par conjugado cambian de signo.

**Veredicto.** Se obtuvo la representación Mellin exacta solicitada y se
aisló una diagonal topológica positiva. No cierra la energía porque la
diagonal pertenece al promedio de dos hojas, mientras los pesos
ordinarios seleccionan una sola hoja y dejan el término firmado de
(11). Probar que ese término no destruye la diagonal, uniformemente para
los polinomios \(\Phi_N\), equivale otra vez a demostrar la cota
subpolinomial de `104_93`--`104_94`. Este documento no demuestra esa
cota, Deep-\(\Lambda\), A1 ni RH.

---

## 1. Plancherel finito sin continuación analítica

Para \(\sigma>0\), defina sobre la recta logarítmica

\[
 f_{N,\sigma}(y)=
 \begin{cases}
 e^{-\sigma y}P_m,&\log m\le y<\log(m+1),\quad2\le m\le N,\\
 0,&\text{fuera de esos intervalos}.
 \end{cases}
 \tag{12}
\]

Con la convención
\(\widehat f(t)=\int_{\mathbb R}f(y)e^{-ity}dy\), una integración
elemental en cada intervalo da

\[
 \widehat f_{N,\sigma}(t)
 ={1\over \sigma+it}
 \sum_{m=2}^NP_m\{m^{-\sigma-it}-(m+1)^{-\sigma-it}\}
 ={\Phi_N(\sigma+it)\over\sigma+it}.
 \tag{13}
\]

Plancherel prueba la identidad más general

\[
 \boxed{
 {1\over2\sigma}\sum_{m=2}^NP_m^2
 \{m^{-2\sigma}-(m+1)^{-2\sigma}\}
 ={1\over2\pi}\int_{\mathbb R}
 \left|{\Phi_N(\sigma+it)\over\sigma+it}\right|^2dt.}
 \tag{14}
\]

Tomar \(\sigma=1/2\) da (3). No se intercambian aquí una suma infinita
y una integral, no se usa fórmula explícita y no se presupone RH.

Para obtener (4), escriba \(P_m=\sum_{r=2}^ma_r\) y telescope:

\[
 \begin{aligned}
 \Phi_N(s)
 &=\sum_{r=2}^Na_r\sum_{m=r}^N
   \{m^{-s}-(m+1)^{-s}\}\\
 &=\sum_{r=2}^Na_rr^{-s}-P_N(N+1)^{-s}.
 \end{aligned}
 \tag{15}
\]

Al expandir el cuadrado se recupera, también exactamente,

\[
 \sum_{m=2}^N{P_m^2\over m(m+1)}
 =\sum_{r,q=2}^Na_ra_q
 \left\{{1\over\max(r,q)}-{1\over N+1}\right\}.
 \tag{16}
\]

Así, (3) no es una nueva estimación disfrazada: es la factorización
Mellin exacta del kernel `max` de `104_93`.

## 2. El símbolo infinito de los primos ordinarios

Para \(m\ge3\), ponga

\[
 d_m=L_2(m)-L_2(m-1)=\int_{m-1}^m{dx\over\log x},
 \qquad d_2=0.
 \tag{17}
\]

Entonces \(a_m={\bf1}_{\mathbb P}(m)-d_m\), también en \(m=2\), y
para \(\Re s>1\)

\[
 \Phi(s):=\sum_{m\ge2}a_mm^{-s}=\mathcal P(s)-D(s).
 \tag{18}
\]

En ese semiplano \(P_m=O(m)\), de modo que el borde de (4) tiende a
cero. Por (14), ahora sin cutoff,

\[
 {1\over2\sigma}\sum_{m\ge2}P_m^2
 \{m^{-2\sigma}-(m+1)^{-2\sigma}\}
 ={1\over2\pi}\int_{\mathbb R}
 \left|{\Phi(\sigma+it)\over\sigma+it}\right|^2dt
 \quad(\sigma>1).
 \tag{19}
\]

El comparador continuo satisface

\[
 I(s):=\int_2^\infty{x^{-s}\over\log x}dx
 =E_1((s-1)\log2).
 \tag{20}
\]

Además,

\[
 I(s)-D(s)=\sum_{m=3}^{\infty}\int_{m-1}^{m}
 {x^{-s}-m^{-s}\over\log x}dx=R(s).
 \tag{21}
\]

Si \(K\Subset\{\Re s>0\}\), entonces, uniformemente para \(s\in K\),

\[
 |x^{-s}-m^{-s}|
 =\left|s\int_x^m u^{-s-1}du\right|
 \ll_K m^{-1-\inf_K\Re s}.
 \tag{22}
\]

La serie (21) converge normalmente. Esto prueba la afirmación de
holomorfía de (8). Finalmente, la inversión de Möbius del producto de
Euler da

\[
 \mathcal P(s)=\sum_{k\ge1}{\mu(k)\over k}\log\zeta(ks),
 \qquad \Re s>1,
 \tag{23}
\]

y (7) sigue de (18)--(23).

## 3. Los únicos puntos de ramificación derechos

En \(\Re s>1/2\), para \(k\ge2\) se tiene \(\Re(ks)>1\). Por tanto
\(\log\zeta(ks)\) admite una rama holomorfa allí y la suma de esos
términos converge normalmente en compactos. Cerca de \(s=1\),

\[
 \log\zeta(s)=-\log(s-1)+O(1),
 \qquad
 E_1((s-1)\log2)=-\gamma-\log((s-1)\log2)+O(s-1),
 \tag{24}
\]

así que su diferencia tiene singularidad removible.

Equivalentemente, derivando (7),

\[
 \boxed{
 \Phi'(s)=
 \sum_{k\ge1}\mu(k){\zeta'(ks)\over\zeta(ks)}
 +{2^{1-s}\over s-1}+R'(s).}
 \tag{25}
\]

Los residuos \(-1\) y \(+1\) en \(s=1\) se cancelan. En un cero
\(\rho\) derecho de multiplicidad \(m_\rho\), (25) tiene residuo
\(m_\rho\). Esto prueba (9) y muestra que las potencias propias no
contaminan el diagnóstico: sus singularidades \(\rho/k\), \(k\ge2\),
quedan en \(\Re s<1/2\). Es la versión de continuación analítica de la
separación energética elemental de `104_94`.

## 4. Una diagonal positiva de monodromía

Elija \(r>0\) de modo que el disco cerrado alrededor de \(\rho\) esté
en \(\Re s>1/2\) y no contenga otra singularidad. Sobre el recubrimiento
universal del disco perforado,

\[
 \Phi(\rho+re^{i\theta})
 =m_\rho(\log r+i\theta)+h_\rho(\rho+re^{i\theta}),
 \quad0\le\theta<2\pi.
 \tag{26}
\]

Con
\(\widehat g(n)=(2\pi)^{-1}\int_0^{2\pi}g(\theta)e^{-in\theta}d\theta\),

\[
 \widehat{i\theta}(n)=-{1\over n}\quad(n\ne0).
 \tag{27}
\]

La traza de una función holomorfa en el disco solo tiene modos
\(n\ge0\). Por consiguiente, para todo \(k\ge1\), el modo \(-k\) del
lado derecho de (26) vale exactamente \(m_\rho/k\). Ninguna elección de
la parte holomorfa ni de la constante \(c\) puede cancelarlo. Parseval da

\[
 {1\over2\pi}\int_0^{2\pi}|\Phi-c|^2d\theta
 \ge m_\rho^2\sum_{k\ge1}{1\over k^2}
 ={\pi^2m_\rho^2\over6},
 \tag{28}
\]

que prueba (10).

Este sí es un mecanismo diagonal positivo, pero no es todavía una cota
de los pesos primos en la recta física. Para rodear \(\rho\) se deben
recorrer todas las determinaciones de \(\log(s-\rho)\). Los polinomios
\(\Phi_N\) de (2) son enteros y monovaluados; la monodromía solo emerge
en un límite no uniforme fuera del semiplano de convergencia. Demostrar
que ese límite es de Hardy en todo \(\Re s>1/2\) ya es la continuación
que `104_93` obtiene **suponiendo** energía subpolinomial.

La contabilidad de las dos orillas hace visible la pérdida. Escriba

\[
 \Phi_\pm=\Phi_0\pm\pi i m_\rho.
 \tag{29}
\]

Expandir los cuadrados prueba (11). La diagonal
\(\pi^2m_\rho^2\) aparece solo después de promediar ambas hojas; en una
hoja queda el término \(\pm2\pi m_\rho\Im\Phi_0\), sin signo.

## 5. La misma parte firmada en la fórmula explícita

Sea \(\Pi_0(x)\) la función de Riemann que cuenta \(p^k\) con peso
\(1/k\), usando medio peso en un salto. Para \(x>1\), con la suma sobre
ceros tomada simétricamente,

\[
 \Pi_0(x)=\mathrm{li}(x)
 -\sum_\rho^{*}\mathrm{li}(x^\rho)
 -\log2+\int_x^\infty{du\over u(u^2-1)\log u}.
 \tag{30}
\]

Fuera de los saltos, si

\[
 Q(x)=\sum_{k\ge2}{1\over k}\pi(x^{1/k}),
 \tag{31}
\]

entonces \(\Pi_0(x)=\pi(x)+Q(x)\), y por ello

\[
 \boxed{
 \pi(x)-L_2(x)=C_0(x)-Q(x)
 -\sum_\rho^{*}\mathrm{li}(x^\rho),}
 \tag{32}
\]

donde

\[
 C_0(x)=\mathrm{li}(x)-L_2(x)-\log2
       +\int_x^\infty{du\over u(u^2-1)\log u}
 \tag{33}
\]

es completamente explícita. El bloque \(Q\) tiene energía finita por
`104_94`; los saltos y la convención de medio peso no alteran una
integral en \(x\).

Para un conjunto finito de ceros \(\rho_j=\beta+i\gamma_j\), cerrado
por conjugación, la parte de exponente \(\beta\) satisface, con
\(x=e^y\),

\[
 -\sum_j\mathrm{li}(e^{\rho_jy})
 ={2e^{\beta y}\over y}\Re\sum_{\gamma_j>0}
 c_je^{i\gamma_jy}+O_{\mathcal Z}(e^{\beta y}/y^2),
 \qquad c_j=-{1\over\rho_j}.
 \tag{34}
\]

Ponga \(\alpha=2\beta-1\) y, para un peso positivo \(w(y)\),

\[
 K_w(\omega)=\int {w(y)\over y^2}e^{\alpha y}e^{i\omega y}dy.
 \tag{35}
\]

El cuadrado ponderado del término principal de (34), incluido el factor
de energía \(e^{-y}\), es exactamente

\[
 2\Re\sum_{j,k}
 \left\{c_j\overline{c_k}K_w(\gamma_j-\gamma_k)
       +c_jc_kK_w(\gamma_j+\gamma_k)\right\}.
 \tag{36}
\]

La matriz completa es Gram y el total es no negativo. Sin embargo:

* \(K_w(0)\sum_j|c_j|^2\) es solo una parte de (36);
* las entradas de diferencia con \(j\ne k\) tienen ambos signos;
* ya para un solo par conjugado queda

\[
 2|c|^2K_w(0)+2\Re\{c^2K_w(2\gamma)\},
 \tag{37}
\]

y el segundo sumando cambia de signo al trasladar la ventana.

Así, la fórmula explícita y la monodromía localizan el mismo residuo:
**diagonal positiva más una interferencia firmada de igual origen**. La
positividad del cuadrado completo no permite descartar la interferencia,
pues estimar el cuadrado completo desde arriba para los pesos ordinarios
es justamente la energía que falta.

## 6. No duplicación interna

* `104_93` prueba la equivalencia energética y la forma `max`, pero no
  factoriza la energía literal de \(\pi-L_2\) sobre la recta Mellin ni
  calcula sus ramas.
* `104_94` elimina las potencias propias por una perturbación de energía
  finita; (25) da la contraparte analítica: \(\rho/k\), \(k\ge2\), queda
  estrictamente a la izquierda de la frontera.
* `104_89` usa Mellin--Plancherel para la cola de
  \(J-L_2\) **bajo RH**. Aquí (3) es finita e incondicional y (7)--(11)
  describen exactamente qué ocurre si hay un cero derecho.
* `phase-49/157` registra la identidad de Cramér para \(\psi-x\) a nivel
  de exponente. No contiene el símbolo de prime-zeta discretizado, el
  borde (4), el piso Hardy (10) ni la separación de hojas (11).
* Los usos de prime-zeta de `phase-14` son autorreferenciales y no están
  acoplados a esta energía.

Por tanto el documento no reclama como nueva la fórmula de Riemann ni
Mellin--Plancherel. Lo nuevo dentro del programa es la cadena exacta
(2)--(11) para el observable literal de `104_94`, y el diagnóstico de
que la diagonal positiva disponible es un promedio de hojas, no una
desigualdad unilateral sobre la hoja aritmética.

## 7. Reproducción

Desde `tools/`:

```bash
python3 prime_energy_mellin_monodromy_check.py
```

El checker:

1. verifica (4) y (16) exactamente con `Fraction`;
2. reconstruye \(\pi(m)-L_2(m)\) y el borde móvil para un prefijo real;
3. exhibe una ventana donde el término de frecuencia \(2\gamma\) de
   (37) es estrictamente negativo;
4. certifica por cotas de la cola de \(\sum k^{-2}\) el piso
   \(m^2\pi^2/6\) de (10).

Las evaluaciones numéricas ilustran identidades ya demostradas; no son
evidencia asintótica ni un certificado de RH.
