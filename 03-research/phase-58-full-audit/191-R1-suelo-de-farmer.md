# Documento 191 — La rendija R1 a decisión: el suelo de Farmer, una cota inferior universal del momento molificado, y la frontera exacta θ=1/2

**Programa:** Hipótesis de Riemann — Fase 58 (auditoría total)
**Fecha:** 2026-06-12
**Mandato:** decidir la rendija R1 abierta por la auditoría D188 §5: el techo absoluto de la barrera #2 ([PROP 180.3]) era CONDICIONAL-A-FARMER porque el suelo $c(\theta)\ge1+1/\theta$ no es teorema sobre la clase general de molificadores. Tres partes: inventario exacto del estatus de $c(\theta)$; intento de prueba en las dos direcciones (sello/ruptura); veredicto.
**Prerrequisitos:** [PROP 180.3] (conducto Littlewood–Jensen–molificador: $E(T)\le\frac{c-1}{2\pi a}\frac T{\log T}+O(\log T)$ — el conducto está probado, D188 §1.3); degradación D188 (el techo era condicional); [Thm 170.5] ($E(T)\ll T/\log T$).
**Contrato:** [TEOREMA]/[PROP]/[LEMA] solo con prueba completa; [GAP]/[GAP de literatura] declarados; sin numérica; backward-only; honestidad total.

**Coordenadas.** $E(T)=\sum_{0<\gamma\le T,\beta>1/2}(\beta-\tfrac12)^2$; **A** $\iff E=O(1)$. Molificador: $\varphi(s)=\sum_{n\le X}b_nn^{-s}$, $X=T^\theta$, $b_1=1$. Momento molificado en la línea: $c(\theta):=\liminf_T\inf_\varphi\frac1T\int_0^T|\zeta\varphi(\tfrac12+it)|^2dt$ (ínfimo sobre la clase que se especifique). Romper la barrera #2 exige $(c(\theta)-1)/\theta\ll1/\log T$ para algún $\theta\le1$; sellarla exige un suelo $c(\theta)-1\gg_\theta1$ (o $\ge\theta/\log T\cdot w(T)$, $w\to\infty$) **para todo** $\theta\le1$, como **cota inferior sobre toda la clase**.

---

## 0. Resumen ejecutivo y veredicto

1. **[TEOREMA 191.A] (sello parcial, incondicional).** Para TODA la clase de molificadores con coeficientes divisor-acotados, soporte $[1,T^\theta]$, $b_1=1$: $c(\theta)\ge1+\log\frac{1-\theta}\theta-o(1)$ para $\theta<\tfrac12$, uniforme hasta $\theta\le\tfrac12-C\frac{\log\log T}{\log T}$. **Es la primera cota inferior universal del momento molificado que localizo** (módulo [GAP 191.L1] de novedad). Mecanismo: rigidez de convolución — $(1*b)(p)=1$ exactamente para todo primo $p>X$, sea cual sea $b$.
2. **Consecuencia: la barrera #2 es TEOREMA para $\theta<\tfrac12$.** El conducto entero con molificadores cortos tiene techo $\asymp T/\log T$, ya no condicional a Farmer. La rendija R1 se estrecha de "$\theta\le1$ entero" a **$\theta\in(\tfrac12-o(1),\,1]$** — exactamente el territorio de los *long mollifiers* de Farmer 1993.
3. **[PROP 191.C] (soporte no-inicial: catastrófico).** Molificadores con soporte $\{1\}\cup(T^\alpha,T^\theta]$ tienen $c-1\ge\log(\alpha\log T)-O(1)\to\infty$. La intuición del mandato queda probada en su mitad logarítmica: $\varphi$ DEBE aproximar a $\mu$ en todo su rango inicial; cada primo no molificado cuesta $1/p$ de momento, sin escape de clase.
4. **La frontera $\theta=\tfrac12$ es de RANGO, no de aritmética.** La rigidez $(1*b)(p)=1$ persiste para todo $p>X$ hasta el infinito; lo que muere en $\theta\ge\tfrac12$ es la *ventana observable* del momento (el rango bilineal $XY\le T^{1-\varepsilon}$ de Montgomery–Vaughan). [PROP 191.D]: bajo una hipótesis de rango bilineal (TW$_y$) — dominación diagonal hasta $Y=T^y$, $y>\tfrac12$ — el suelo se extiende y sella $\theta<y$ con $c-1\ge\log(y/\theta)$.
5. **Recalibración del condicional:** la barrera #2 en $\theta\in[\tfrac12,1]$ ya NO está condicionada a la conjetura de OPTIMALIDAD de Farmer ($c(\theta)=1+1/\theta$ exacto) sino solo a una extensión de RANGO de valor medio (mucho más débil: basta que la diagonal domine, no que el molificador estándar sea óptimo). Romperla exigiría $c(\theta)-1\ll1/\log T$: no una falla marginal de Farmer sino una **conspiración off-diagonal negativa de tamaño constante** que borre la masa diagonal forzada — violación catastrófica, no marginal.
6. **Dirección Levinson/Feng (dos piezas):** sale del conducto (no se anula en los ceros off de $\zeta$) o reentra en la clase del teorema; **pesos suaves y adaptativos en $t$:** el suelo es insensible (la rigidez vive en los coeficientes). Ningún truco de clase examinado esquiva el suelo en $\theta<\tfrac12$.
7. **Veredicto R1: SELLADA-POR-TEOREMA en $\theta<\tfrac12$; CONDICIONAL-CALIBRADA (rango-difícil, ya no Farmer-difícil) en $\theta\in[\tfrac12,1]$.** Ninguna mejora de $E(T)\ll T/\log T$ se obtiene (este documento construye barrera, no señal). [GAP-191.1]: el suelo en $\theta\in[\tfrac12,1]$.

---

## 1. Parte 1: inventario exacto

### 1.1. Qué es $c(\theta)$ y la dirección de la desigualdad

$\frac1T\int_0^T|\zeta\varphi|^2(\tfrac12+it)\,dt$ es, tras las evaluaciones asintóticas disponibles, una forma cuadrática $\langle M_Tb,b\rangle$ en los coeficientes; $c(\theta)$ es su mínimo normalizado ($b_1=1$). **Crítico (D188 lo señaló):** el conducto 180.3 necesita la **cota inferior** $c(\theta)\ge1+\delta(\theta)$ sobre TODA la clase — la dirección opuesta a lo que la industria optimiza (la industria construye $\varphi$ con momento PEQUEÑO para Levinson/proporción crítica; nunca necesitó probar que no se puede bajar más, salvo dentro de su propia clase variacional).

### 1.2. Qué es teorema y qué es conjetura

- **Teorema (evaluación):** la asintótica del momento molificado para coeficientes en clases concretas: Balasubramanian–Conrey–Heath-Brown 1985 evalúan $\frac1T\int|\zeta A|^2$ para polinomios de longitud $T^\theta$, $\theta<\tfrac12$ (coeficientes divisor-acotados); Conrey 1989 extiende el rango evaluable a $\theta<\tfrac47$ para las formas usadas en la proporción $\ge2/5$ (coeficientes tipo Selberg–Levinson $\mu(h)h^{\sigma-1/2}P(\log(y/h)/\log y)$). Para el molificador estándar el valor óptimo dentro de su clase variacional es $1+\tfrac1\theta+o(1)$.
- **Conjetura (Farmer 1993, "Long mollifiers of the Riemann zeta-function", *Bull. LMS* 25):** que $c(\theta)=1+\tfrac1\theta$ persiste para TODO $\theta$ — la "conjetura $\theta=\infty$", con consecuencias RH-adyacentes ($\zeta$-momentos, proporciones $\to1$). Es conjetura de **optimalidad** (el suelo es también techo). Literatura posterior sobre equivalencias y consecuencias (Bettin–Gonek y coautores sobre la conjetura $\theta=\infty$): [GAP de literatura 191.L2 — no puedo verificar de memoria los enunciados exactos de esos trabajos; no se usan aquí].
- **Lo que NO localizo como teorema previo:** la cota inferior $c(\theta)\ge1+\delta(\theta)$, $\delta>0$, sobre la clase GENERAL de coeficientes (no solo la variacional estándar). El cálculo variacional de Farmer (y el de Goldston–Gonek en problemas hermanos de mínimos cuadráticos con $\Lambda$/$\mu$) opera sobre clases suaves parametrizadas; que el mínimo de la forma cuadrática completa de BCHB sobre coeficientes ARBITRARIOS sea $1+1/\theta$ es plausible (el problema es cuadrático y resoluble en principio para $\theta<\tfrac12$ donde la forma está evaluada), pero no tengo el enunciado en la literatura. [GAP de literatura 191.L1: si Farmer 1993 §variacional o un sucesor ya prueba el mínimo sobre coeficientes generales para $\theta<\tfrac12$, el Teorema 191.A es redundante en ese rango — aunque su prueba elemental y su uniformidad cerca de $\tfrac12$ tendrían valor propio. Auditar antes de publicación.]
- **$\theta\ge1$:** el teorema del valor medio $\int_0^T|\sum_{n\le N}a_nn^{-it}|^2dt=(T+O(N))\sum|a_n|^2$ pierde el término principal para $N\gg T$; no existe tecnología de momentos con $X>T$ y tampoco teorema de imposibilidad (D188: techo *de facto*, no *de jure*). Sin cambios.

**Conclusión del inventario:** la auditoría D188 tenía razón y se quedó corta: sin cota inferior universal, la barrera #2 era condicional **incluso para $\theta$ pequeño**. La Parte 2 repara exactamente eso.

---

## 2. Parte 2, dirección sello: la cota inferior universal

### 2.1. El mecanismo: rigidez de convolución en los primos

**[LEMA 191.1].** Sea $b$ cualquier sucesión con $b_1=1$ y $b_n=0$ para $n>X$. Sea $A=1*b$, es decir $A_k=\sum_{n\mid k}b_n$ (los coeficientes de Dirichlet de $\zeta\varphi$). Entonces $A_p=1$ **para todo primo $p>X$**.

*Prueba.* $A_p=b_1+b_p=1+0=1$. $\square$

Esto es una identidad combinatoria, ciega a la clase de $b$: la cola de $\zeta\varphi-1$ tiene coeficiente EXACTAMENTE $1$ en cada primo más allá del soporte. Toda la cuestión es cuánta de esa masa forzada **ve** el momento sobre $[0,T]$.

### 2.2. El teorema

**[TEOREMA 191.A].** Fijos $\kappa\in\mathbb N$, $A_0>0$. Sea $\varphi(s)=\sum_{n\le X}b_nn^{-s}$ con $b_1=1$, $|b_n|\le d_\kappa(n)(\log T)^{A_0}$, $X=T^\theta$. Existe $C_0=C_0(\kappa,A_0)$ tal que para $0<\theta\le\tfrac12-C_0\frac{\log\log T}{\log T}$ y todo $\eta\in[C_0\frac{\log\log T}{\log T},\tfrac12]$ con $\theta+\eta\le\tfrac12$... más precisamente, con $Y=T^{1-\theta-\eta}$:
$$\frac1T\int_0^T\big|\zeta\varphi(\tfrac12+it)\big|^2dt\;\ge\;1+\sum_{X<p\le Y}\frac1p\;-\;O\!\big(e^{-\eta\log T/3}(\log T)^{B}\big)\;=\;1+\log\frac{1-\theta-\eta}{\theta}-o_\eta(1).$$
En particular, para todo $\theta\le\tfrac12-\delta$ con $\delta\ge C_0\frac{\log\log T}{\log T}$: $\;c(\theta)-1\ge\delta$ (tomando $\eta=\delta$, pues $\log\frac{1-\theta-\delta}{\theta}\ge\log\frac{1/2}{1/2-\delta}\ge2\delta$, y el error es $\le\delta$ por la elección de $C_0$).

*Prueba.* Escribimos $F(t)=\zeta\varphi(\tfrac12+it)$ y $G=F-1$.

**(i) Reducción a polinomios (Hardy–Littlewood).** Para $1\le t\le T$, la aproximación de Hardy–Littlewood (Titchmarsh, Thm 4.11) con $x=T$: $\zeta(\tfrac12+it)=\sum_{m\le T}m^{-1/2-it}+\frac{T^{1/2-it}}{\tfrac12+it-1}+O(T^{-1/2})$. Sea $Z(t)=\sum_{m\le T}m^{-1/2-it}$ y $F_0=Z\varphi$, polinomio de Dirichlet de longitud $TX$ con coeficientes $\alpha_N=\sum_{n\mid N,\,n\le X,\,N/n\le T}b_n$, que satisfacen $|\alpha_N|\le d_{\kappa+1}(N)(\log T)^{A_0}$ y $\alpha_1=1$, $\alpha_p=1$ para $X<p\le T$. El término corrector: $|F-F_0|\ll(T^{1/2}/t+T^{-1/2})\,|\varphi(\tfrac12+it)|\ll(T^{1/2}/t)\,X^{1/2}(\log T)^{B_1}$ para $t\ge1$; su contribución a cualquier forma bilineal contra un polinomio $D$ de longitud $Y$ acotado por $\sup|D|\ll Y^{1/2}$ es $\ll T^{1/2}X^{1/2}Y^{1/2}(\log T)^{B_2}=T^{1-\eta/2}(\log T)^{B_2}$; el segmento $0\le t\le1$ contribuye $\ll\sup_{t\le1}|FD|\ll T^{1/2+\theta}$ trivialmente (convexidad y $|\varphi|\le X^{1/2+o(1)}$). Ambos absorbidos en el error del enunciado.

**(ii) El test.** Sea $D(t)=\sum_{X<p\le Y}p^{-1/2-it}$ (suma sobre primos). Por Cauchy–Schwarz,
$$\frac1T\int_0^T|G|^2dt\;\ge\;\frac{\big|\frac1T\int_0^TG\,\overline D\,dt\big|^2}{\frac1T\int_0^T|D|^2dt}.$$

**(iii) Denominador.** Montgomery–Vaughan (valor medio): $\frac1T\int_0^T|D|^2dt=\sum_{X<p\le Y}\frac1p\big(1+O(p/T)\big)=\big(1+O(Y/T)\big)\sum_{X<p\le Y}\frac1p$.

**(iv) Numerador.** $\int_0^TG\overline D=\int_0^T(F_0-1)\overline D+\text{(correctores de (i))}$. La forma bilineal $\int_0^T(F_0-1)\overline D\,dt$ tiene frecuencias $\log(N/k)$, $N\le TX$, $k\in(X,Y]$ primo. La desigualdad de Hilbert generalizada de Montgomery–Vaughan (1974) da
$$\int_0^T(F_0-1)\overline D\,dt\;=\;T\sum_{X<p\le Y}\frac{\alpha_p}{p}\;+\;O\Big(\big(\textstyle\sum_{N\le TX}|\alpha_N|^2\big)^{1/2}\big(\sum_{X<p\le Y}1\big)^{1/2}\Big),$$
(diagonal $N=k=p$; el término $-1$ no tiene diagonal porque $D$ no contiene $n=1$). Por [LEMA 191.1], $\alpha_p=1$ en todo el rango. El error: $\sum_{N\le TX}|\alpha_N|^2\ll TX(\log T)^{B_3}$, luego error $\ll(TXY)^{1/2}(\log T)^{B_3}=T^{1-\eta/2}(\log T)^{B_3}$.

**(v) Ensamblaje.** Con $\mathcal P:=\sum_{X<p\le Y}1/p=\log\frac{1-\theta-\eta}\theta+O(1/\log X)$ (Mertens):
$$\frac1T\int_0^T|G|^2dt\;\ge\;\frac{\big(\mathcal P-O(T^{-\eta/2}(\log T)^{B})\big)^2}{\mathcal P\,(1+O(Y/T))}\;=\;\mathcal P-O\big(T^{-\eta/3}\big).$$
**(vi) Del cuadrado de $G$ al momento.** $\frac1T\int|F|^2=1+\frac2T\mathrm{Re}\int G+\frac1T\int|G|^2$, y el primer momento $\frac1T\int_0^TG\,dt=o(1)$ con ahorro de potencia: por (i) y Montgomery–Vaughan con $D\equiv1$, la diagonal es $\alpha_1-1=0$ y el error es $\ll T^{-1/2}(TX)^{1/2}(\log T)^{B}=T^{\theta/2-\dots}$… con más cuidado: $\frac1T\int_0^T(F_0-1)dt=\frac1T\sum_{N\ge2}\alpha_NN^{-1/2}\frac{N^{-iT}-1}{-i\log N}\ll\frac1T\sum_{2\le N\le TX}|\alpha_N|N^{-1/2}\ll T^{-1}(TX)^{1/2}(\log T)^{B}=T^{(\theta-1)/2}(\log T)^B=o(1)$ (ahorro de potencia para $\theta<1$). Los correctores de (i) contra $1$: $\ll T^{-1/2}X^{1/2}(\log T)^{B}=o(1)$ igual. Juntando: $\frac1T\int|F|^2\ge1+\mathcal P-o(1)$ con todos los errores $\le e^{-\eta\log T/3}(\log T)^B$ salvo el Mertens $O(1/\log X)=O(1/(\theta\log T))$, absorbido eligiendo $C_0$ grande. $\square$

**Comentarios de honestidad.** (1) La clase divisor-acotada cubre todo molificador jamás usado (Selberg–Levinson, Conrey, Feng con piezas $\mu*\Lambda^{*j}$, Radziwiłł–Soundararajan); coeficientes verdaderamente arbitrarios (e.g. $|b_n|\sim e^{\sqrt n}$) quedan fuera, pero solo afectan a las constantes $B_i$ del error vía $\sum|\alpha_N|^2$ — la prueba tolera $|b_n|\le n^{\varepsilon_0}$ con $\varepsilon_0$ pequeño fijo a costa de reducir el rango de $\eta$. (2) La tasa $\log\frac{1-\theta}\theta$ es **más débil** que el suelo de Farmer $1/\theta$ cuando $\theta\to0$ (logaritmo vs. recíproco): nuestro test solo ve los primos de la cola, no toda la masa de $1*b$; el $1/\theta$ completo requeriría los términos off-diagonal/swap que solo las evaluaciones tipo BCHB capturan. Para la barrera esto es irrelevante: basta un suelo $\ge\delta>0$ constante. (3) En $\theta\to\tfrac12$ el suelo degenera linealmente — y eso es real, no artefacto: ver §3.2.

**[COROLARIO 191.B] (la barrera #2 es teorema para molificadores cortos).** Para toda familia $\varphi_T$ de la clase de 191.A con $\theta\le\tfrac12-\delta$, $\delta\ge C_0\frac{\log\log T}{\log T}$, el conducto de [PROP 180.3] produce $E(T)\le\frac{c-1}{2\pi a}\frac T{\log T}$ con $c-1\ge\delta$ y $a\asymp\theta\le\tfrac12$: **ninguna elección da $E(T)=o(\delta\cdot T/\log T)$ por el conducto**; en particular ganar un log ($(c-1)/\theta\ll1/\log T$) es imposible en este rango. Más aún, el suelo vale también en los desplazamientos: la misma prueba con $\zeta\varphi(\tfrac12+s+it)$ pone $p^{-2s}$ en la diagonal ($\alpha_p\,p^{-s}\cdot p^{-s}$), dando $\text{mean}(s)-1\ge\sum_{X<p\le Y}p^{-1-2s}-o(1)$, que reproduce exactamente la forma exponencial (M) de 180.3 con tasa $a\le2(1-\theta)$ POR DEBAJO: la entrada del conducto no puede ser menor que esto. *Prueba:* sustitución en 180.3 + repetición literal de 191.A con el desplazamiento (los errores son uniformes en $0\le s\le\tfrac12$ porque solo mejoran). $\square$

### 2.3. Soporte no-inicial: peor, no mejor

**[PROP 191.C].** Si además $b_n=0$ para $1<n\le T^\alpha$ (soporte $\{1\}\cup(T^\alpha,T^\theta]$, $\theta<\tfrac12$), entonces $c-1\ge\sum_{p\le T^\alpha}\frac1p-o(1)=\log(\alpha\log T)-O(1)\to\infty$.

*Prueba.* [LEMA 191.1] da ahora $A_p=1$ también para todo primo $p\le T^\alpha$ (pues $b_p=0$); se aplica 191.A con el test $D=\sum_{1<p\le T^\alpha}p^{-1/2-it}$ (longitud $T^\alpha\le Y$, mismos errores). $\square$

**Lectura.** El mecanismo conjeturado por el mandato ("$\varphi$ debe aproximar $1/\zeta$; la cola no aproximada tiene masa") queda PROBADO en su mitad logarítmica y con localización exacta: **cada primo no molificado cuesta $1/p$, identidad sin escape de clase.** Los huecos en el soporte son catastróficos; la única libertad está en CÓMO se molifica el rango inicial, no en SI se molifica.

---

## 3. Parte 2, dirección ruptura: las cuatro variantes y la frontera $\theta=\tfrac12$

### 3.1. Las variantes del mandato

- **(i) Soporte no-inicial:** muerto por [PROP 191.C] — dirección contraria a la ruptura.
- **(ii) Molificadores adaptativos en $t$ (por ventanas).** El conducto 180.3 los admite: el lema de Littlewood se aplica por sub-rectángulos $t\in[T_j,T_{j+1}]$ (la integración en $\sigma$ no se toca) y $E=\sum_jE_j$. Pero el suelo también localiza: Hardy–Littlewood y Montgomery–Vaughan funcionan sobre $[T_j,T_{j+1}]$ siempre que la ventana sea $\ge X^{2}$-ish (rango bilineal relativo a la ventana), y entonces $c_j-1\ge\log\frac{1-\theta_j'}{\theta_j'}$ con $\theta_j'=\log X_j/\log|ventana|\ge\theta$. Ventanas más cortas que el cuadrado del molificador caen en el mismo régimen abierto que $\theta\ge\tfrac12$ global: **la adaptatividad no crea resquicio nuevo, reparametriza el mismo.**
- **(iii) Dos piezas tipo Levinson/Feng ($\psi_1+\psi_2\zeta'$ etc.).** Distinción crucial: el conducto 180.3 exige $f$ que se ANULE en los ceros off de $\zeta$ (paso (i): $E_\zeta\le E_f$). $f=\zeta\varphi_1+\zeta'\varphi_2$ NO se anula en $\rho$ ($f(\rho)=\zeta'(\rho)\varphi_2(\rho)\ne0$ genéricamente): esa familia detecta ceros de combinaciones — útil para proporción en la línea (Levinson 1974, Conrey 1989, Feng 2012), **inútil para acotar $E$**: sale del conducto. La forma general admisible es $f=\zeta G$; si $G$ es cualquier serie con coeficientes divisor-acotados de longitud efectiva $\le T^\theta$ (incluidas combinaciones con pesos $\log n$, trozos $\mu*\Lambda$, etc.), [TEOREMA 191.A] se aplica VERBATIM (la prueba nunca usa multiplicatividad ni signo de $b$). Si $G$ tiene longitud $>T^{1/2}$ (e.g. trunca $\zeta'/\zeta$ a rango largo): reentra en la rendija de §3.2, no la esquiva.
- **(iv) Pesos suaves en $t$ (Radziwiłł–Soundararajan).** El suelo es insensible: la rigidez vive en los coeficientes, y un peso $w(t/T)\ge0$ solo multiplica diagonal y denominador por la misma masa $\widehat w(0)$ (Cauchy–Schwarz pasa igual). Pesos NO multiplicativos en $n$ ya están dentro de la clase de 191.A.

**Síntesis: ningún truco de clase examinado toca el suelo en $\theta<\tfrac12$.** El mecanismo es información-teórico como el mandato intuía, con precisión: la mitad probada es la **rigidez en primos** (logarítmica); la mitad $1/\theta$ (masa total de la cola de $1/\zeta$) sigue siendo la conjetura de Farmer.

### 3.2. Dónde está realmente la frontera: rango, no aritmética

La rigidez $(1*b)(p)=1$ vale para TODO $p>X$ hasta el infinito — la obstrucción aritmética no termina en $\theta=\tfrac12$. Lo que termina es la **ventana observable**: la prueba necesita extraer la diagonal de la forma bilineal $\int\zeta\varphi\overline D$ con $D$ de longitud $Y>X$, y el tratamiento incondicional (HL con $x=T$ + MV) exige $XY\le T^{1-\eta}$, luego $Y>X\Rightarrow\theta<\tfrac12$. Más allá, los términos swap (parte $\chi$ de la ecuación funcional, saddle en $t\approx2\pi mn/k$) son del tamaño de la diagonal y nadie sabe sumarlos para coeficientes generales — el mismo muro del rango $\theta<\tfrac47$ de Conrey, visto del lado de las cotas inferiores.

**[PROP 191.D] (condicional, extensión de rango).** Fijo $y\in(\tfrac12,1)$. Hipótesis (TW$_y$): para polinomios $D$ de longitud $T^y$ con coeficientes divisor-acotados soportados en primos, $\int_0^T\zeta\varphi(\tfrac12+it)\overline{D(\tfrac12+it)}\,dt=T\sum_p\alpha_pp^{-1}+O(T^{1-\varepsilon})$ uniformemente en la clase de 191.A. Entonces $c(\theta)\ge1+\log(y/\theta)-o(1)$ para todo $\theta<y$, y la barrera #2 queda sellada en $\theta<y$. *Prueba:* idéntica a 191.A sustituyendo el paso (iv) por (TW$_y$). $\square$

**Calibración del condicional residual ($\theta\in[\tfrac12,1]$).** Romper la barrera ahí exige $c(\theta)-1\le\theta/\log T\le1/\log T$. Bajo la conjetura de Farmer, $c(\theta)-1=1/\theta\ge1$: la ruptura no es "Farmer falla un poco" sino **Farmer falla por un factor $\log T$** — y además, por la estructura de la prueba de 191.A, exigiría que los términos swap CANCELEN la masa diagonal forzada $\sum_{X<p\lesssim T}1/p\asymp\log(1/\theta)+O(1)$ hasta $O(1/\log T)$: una correlación negativa exacta entre la parte $\chi$ y la diagonal de primos, uniforme en $T$, para la cual no existe ni mecanismo candidato. La barrera #2 en $\theta\ge\tfrac12$ queda como **rango-difícil**: implicada por (TW$_y$) — un enunciado de valor medio del género que la industria considera más accesible que cualquier optimalidad — no equivalente a la conjetura de Farmer entera. (No probamos la implicación inversa: la ruptura no refuta formalmente (TW$_y$) en toda su fuerza, solo su consecuencia diagonal. La equivalencia exacta queda abierta.)

---

## 4. Test anti-circularidad

| Pieza | ¿ζ-libre? | Dónde entra ζ |
|---|---|---|
| [LEMA 191.1] rigidez | Sí (combinatoria de convolución pura) | — |
| [TEOREMA 191.A] | No | Solo vía Hardy–Littlewood (aproximación de $\zeta$, incondicional) y Mertens; **no usa RH, ni A, ni LP-112, ni densidades de ceros** |
| [PROP 191.C], [COR 191.B] | Heredan 191.A | ídem |
| [PROP 191.D] | Condicional a (TW$_y$), hipótesis de valor medio NO de ceros | — |

Sin circularidad: ninguna pieza supone nada sobre la posición de los ceros; el output es una barrera sobre técnicas, compatible con RH y con ¬RH.

## 5. Parte 3: veredicto

| Etiqueta | Enunciado | Estatus |
|---|---|---|
| [LEMA 191.1] | $(1*b)(p)=1$ para todo $p>X$: rigidez universal | Probado (trivial, decisivo) |
| [TEOREMA 191.A] | $c(\theta)\ge1+\log\frac{1-\theta}\theta-o(1)$, clase divisor-acotada, uniforme en $\theta\le\tfrac12-C_0\frac{\log\log T}{\log T}$ | **Probado, incondicional** |
| [COR 191.B] | Barrera #2 = TEOREMA en $\theta<\tfrac12$ (incluida la forma desplazada (M)) | Probado |
| [PROP 191.C] | Soporte no-inicial: $c-1\gg\log\log T$ | Probado |
| [PROP 191.D] | (TW$_y$) ⟹ sello hasta $\theta<y$ | Probado condicional |

**R1 queda: SELLADA-POR-TEOREMA en $\theta<\tfrac12$ (clase divisor-acotada, que agota la industria), CONDICIONAL-CALIBRADA en $\theta\in[\tfrac12,1]$** — condicional ya no a la optimalidad de Farmer sino a la extensión de rango (TW$_y$), y la ruptura requeriría una violación por factor $\log T$ del suelo conjetural más una cancelación swap-diagonal sin mecanismo conocido. En la terminología del programa: la barrera #2 sube de "apuesta sociológica con forma de teorema" (D188) a **teorema-en-rango-corto + rango-difícil-en-rango-largo**. La frase correcta para la arquitectura: *el conducto molificador está cerrado por teorema salvo por los long mollifiers de Farmer, y abrirlo por ahí exigiría refutar catastróficamente la conjetura $\theta=\infty$, no esquivarla.*

**¿Mejora de $E(T)\ll T/\log T$?** No — y no podía: este documento construye la cota inferior de la entrada del conducto (barrera), que es lógicamente opuesta a la señal. Ninguna afirmación de mejora se hace.

**GAPs numerados:**
- **[GAP-191.1]** (la rendija residual): suelo $c(\theta)\ge1+\delta(\theta)$ para $\theta\in[\tfrac12,1]$, clase general. Implicado por (TW$_y$); estatus = abierto, género "rango bilineal más allá de la raíz cuadrada".
- **[GAP-191.2]**: la tasa — nuestro suelo es $\log(1/\theta)$, Farmer es $1/\theta$; cerrar el hueco para $\theta<\tfrac12$ exigiría evaluar el mínimo de la forma cuadrática completa de BCHB sobre coeficientes arbitrarios (posiblemente ya implícito en la literatura variacional: ver 191.L1). Irrelevante para la barrera, relevante para publicación.
- **[GAP de literatura 191.L1]**: novedad de 191.A (¿Farmer 1993 / Goldston–Gonek / sucesores contienen ya una cota inferior universal?); **[191.L2]**: enunciados exactos de Bettin–Gonek sobre la conjetura $\theta=\infty$; **[191.L3]**: el rango exacto de la asintótica de BCHB 1985 para coeficientes generales ($\theta<\tfrac12$, citado de memoria) y el $\tfrac47$ de Conrey 1989 (clase restringida).

**Dirección sucesora.** (1) Auditar 191.A (es elemental: un auditor debe reconstruir (i)–(vi) en una sesión); si sobrevive, es candidato a nota publicable por sí mismo — primera cota inferior universal de mollificación — previa resolución de 191.L1. (2) La rendija R2 (flujo de borde, Doc 189) y este sello son independientes; con R1 calibrada, el residuo vivo del muro vuelve a ser único: $\mu_2=o(1)$ ([GAP-180.1], género 141.G1). (3) Tarea de literatura 188.L2 (Fujii sobre $\int S_1$) sigue pendiente y es previa a cualquier intento sobre $\mu_2$.

---

## Referencias

- N. Levinson, "More than one third of zeros of Riemann's zeta-function are on $\sigma=1/2$", *Adv. Math.* 13 (1974).
- R. Balasubramanian, J. B. Conrey, D. R. Heath-Brown, "Asymptotic mean square of the product of the Riemann zeta-function and a Dirichlet polynomial", *J. reine angew. Math.* 357 (1985). [Evaluación, $\theta<\tfrac12$; GAP 191.L3.]
- J. B. Conrey, "More than two fifths of the zeros of the Riemann zeta function are on the critical line", *J. reine angew. Math.* 399 (1989). [$\theta<\tfrac47$, clase restringida.]
- D. W. Farmer, "Long mollifiers of the Riemann zeta-function", *Bull. London Math. Soc.* 25 (1993). [Conjetura $\theta=\infty$; suelo $1+1/\theta$ como optimalidad.]
- H. L. Montgomery, R. C. Vaughan, "Hilbert's inequality", *J. London Math. Soc.* (2) 8 (1974). [Valor medio y forma bilineal; pasos (iii)–(iv).]
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed., Oxford 1986. [Thm 4.11, aproximación de Hardy–Littlewood.]
- S. Feng, "Zeros of the Riemann zeta function on the critical line", *J. Number Theory* 132 (2012). [Molificador de dos piezas; §3.1(iii).]
- M. Radziwiłł, K. Soundararajan, trabajos sobre momentos con pesos suaves. [§3.1(iv); uso calibratorio.]
- D. A. Goldston, S. M. Gonek, trabajos sobre mínimos de formas cuadráticas con $\mu$/$\Lambda$. [GAP 191.L1.]
- S. Bettin, S. M. Gonek, sobre la conjetura $\theta=\infty$. [GAP 191.L2: no verificado.]
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS 2004, cap. sobre molificadores/valores medios. [Trasfondo.]

**Documentos internos:** D170 (Thm 170.5), D176 (176.9), D180 (180.3, auditado), D188 (auditoría; rendija R1), D189 (R2), D190.
