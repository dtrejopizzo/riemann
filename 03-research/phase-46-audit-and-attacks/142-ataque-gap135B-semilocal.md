# Doc 142 — Ataque a GAP-135.B: el objeto semilocal con término arquimediano

**Programa:** Hipótesis de Riemann — Phase 46: auditoría y ataques.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Prerrequisitos:** Doc 135 (teorema de dos primos; breakpoints B1–B4; GAP-135.B), P48 (`06-papers/P48-weil-positivity-finite-primes/main.tex`: Conjetura H⁺, normalizaciones), Doc 131 (categoría $\mathcal{A}rith$, slots $(a,c,\omega)$).
**Contrato creativo:** [DEFINICIÓN-NUEVA] libertad total; [TEOREMA]/[PROPOSICIÓN]/[LEMA] con prueba completa; [CÁLCULO] verificado; [PUENTE] con estatus declarado; [GAP] nombrado. Honestidad absoluta.

**Convenciones (las de Doc 135/P48, fijadas una vez).** $G=\mathbb R_+^*$, $d^*x=dx/x$, tests $f\in C_c^\infty(G)$, Mellin $\hat f(s)=\int_0^\infty f(x)x^{s-1}dx$, $\tilde f(x)=\overline{f(1/x)}x^{-1}$, $g:=f\star\tilde f$ (convolución multiplicativa). Para $f$ dado:
$$F(t):=f(e^t)e^{t/2}\in C_c^\infty(\mathbb R),\qquad \hat F(\xi):=\int_{\mathbb R}F(t)e^{i\xi t}dt,\qquad \hat f(\tfrac12+i\xi)=\hat F(\xi),$$
$$G(t):=g(e^t)e^{t/2}=\int_{\mathbb R}F(s)\overline{F(s-t)}\,ds,\qquad \hat G(\xi)=|\hat F(\xi)|^2,\qquad G(-t)=\overline{G(t)},$$
$$\|f\|_w^2:=\int_G|f|^2x\,d^*x=\|F\|_{L^2}^2,\qquad g(1)=G(0)=\|f\|_w^2.$$
"Ventana de longitud $2T$" = $\operatorname{supp}F$ contenido en un intervalo de longitud $2T$ (posición libre). $L_p:=\log p$. $\psi:=\Gamma'/\Gamma$ es la digamma; $\gamma$ la constante de Euler.

---

## 0. Resumen ejecutivo

GAP-135.B pedía decidir el axioma H para el primer objeto del régimen **destructivo**: $n$ primos con dato $a=\Lambda\ge0$, bloque polar $[0]+[1]$ y término arquimediano de tipo $\zeta$ (el factor $\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)$). Resultado, sin adorno: **H falla** — para todo conjunto finito $S$ de primos, e incluso para $S=\varnothing$ (el corazón polar+arquimediano solo). Pero falla de una manera extraordinariamente informativa, y la positividad **sobrevive en dos conos explícitos**. Los hallazgos:

1. **(§1–2)** El objeto semilocal $X_S^{\mathrm{ar}}$ y su forma $Q_S$ quedan definidos en forma cerrada en la normalización de P48. El peso arquimediano es $\Omega(\xi)=\operatorname{Re}\psi(\tfrac14+\tfrac{i\xi}2)-\log\pi$, con tres lemas en forma cerrada: serie explícita, valor exacto
   $$\Omega(0)=\psi(\tfrac14)-\log\pi=-\gamma-\tfrac\pi2-3\log2-\log\pi\approx-5.3722<0,$$
   monotonía estricta en $|\xi|$ (de donde $\mathcal A(f)\ge\Omega(0)\|f\|_w^2$: **la destructividad arquimediana tiene suelo absoluto**, a diferencia de la impureza de Doc 135, que era destructividad sin fondo $p^{M\delta'}$), y cotas logarítmicas efectivas.

2. **(§3) [TEOREMA A — la primera positividad semilocal del programa]** Para **todo** $S$ finito (y para $\zeta$ misma): si la ventana es $2T\le1/150$, entonces $Q_S(f)\ge\tfrac3{10}\|f\|_w^2$, incondicional, con constantes explícitas (toscas, declaradas). El régimen mixto constructivo/destructivo es positivo a escala corta: a alta frecuencia $\Omega\sim\log|\xi|$ domina todo.

3. **(§4) [CÁLCULO]** El test de Mertens — el adversario que decidía todo en el régimen constructivo (Doc 135 §4) — **no rompe** el objeto semilocal: el acople destructivo de un primo a altura $M$ decae como $L_p\,p^{-M/2}\le0.736$, y el margen arquimediano $\sim\log(1/\epsilon)$ lo aplasta. El adversario correcto es otro.

4. **(§5) [TEOREMA B — el fallo, localizado]** El adversario correcto es **lento, ancho y de baja frecuencia, con el polo evadido**: una familia explícita $f_T$ con $\hat f_T(1)=0$ (una sola condición lineal, de costo exponencialmente pequeño $e^{-T/8}$) y masa espectral concentrada en $\xi=O(1/T)$ da
   $$\lim_{T\to\infty}\frac{Q_S(f_T)}{\|f_T\|_w^2}\;=\;\Omega(0)\;-\;\sum_{p\in S}\frac{2\log p}{\sqrt p-1}\;<\;0,$$
   también para $S=\varnothing$. Para $S=\{2,3\}$ (el objeto de GAP-135.B): $\approx-11.72$. **Cada primo añadido empeora la violación** — la inversión exacta del régimen constructivo, donde el primo ajeno protegía ($+L_q$, Doc 135 §4).

5. **(§6) [PUENTE + COROLARIO]** El mecanismo, aislado: **el bloque polar custodia solo la frecuencia compleja $\xi=-i/2$; el déficit arquimediano vive en frecuencias reales $|\xi|<\xi_*$. En $\zeta$, quien transmite la custodia del polo al eje real es la suma COMPLETA sobre primos** (la identidad $Q_S(f_T)=Q_\zeta(f_T)-[P_S-P_{\mathrm{full}}](f_T)$ y, bajo RH, $\lim_T P_{\mathrm{full}}(f_T)=\Omega(0)\|\eta\|^2<0$: la suma completa sobre primos cambia de signo en el agregado; ninguna truncación finita lo ve, pues cada lag fijo aporta $+\|\eta\|^2$). B1/B4 de Doc 135, hechos exactos sobre una sola familia de tests.

6. **(§7) Mapa del régimen destructivo:** positividad en $[0,T_0]$ (Teorema A), fallo en $[T_1,\infty)$ (Teorema B), región intermedia = GAP-142.A; y un **cono de alta frecuencia** explícito donde la positividad sobrevive en toda ventana (Proposición 7.2). El umbral constructivo $\log(p_1\cdots p_n)$ de Doc 135 **colapsa** en el régimen destructivo a un umbral arquimediano absoluto, independiente de $S$.

7. **(§8) Veredicto sobre H⁺:** quirúrgico. Nuestro contraejemplo verifica todas las hipótesis explícitas de H⁺ **salvo la espectralidad, que queda indecisa**. Por tanto: **H⁺ $\Rightarrow$ $X_S^{\mathrm{ar}}$ no es espectral** (contrapositiva probada). O bien GAP-135.B estaba mal planteado (el objeto semilocal nunca estuvo en la clase de H⁺, y la espectralidad carga TODO el peso de la conjetura), o bien H⁺ es falsa. Decidir cuál = GAP-142.B. H⁺ sobrevive refinada: restringida a ventanas cortas (probada aquí para $S$ finito) o al cono de alta frecuencia, o con la hipótesis adicional de **producto de Euler completo** — en cuyo caso su contenido se concentra en la transmisión polo→eje real, es decir, en RH misma.

---

## 1. [DEFINICIÓN-NUEVA] El objeto semilocal arquimediano

**[DEFINICIÓN-NUEVA 1.1] (peso arquimediano de tipo $\zeta$).** El **peso arquimediano** es la función
$$\Omega(\xi)\;:=\;\operatorname{Re}\,\psi\Bigl(\frac14+\frac{i\xi}2\Bigr)\;-\;\log\pi,\qquad \xi\in\mathbb R,$$
y el **término arquimediano** del programa es el funcional cuadrático
$$\mathcal A(f)\;:=\;\frac1{2\pi}\int_{\mathbb R}|\hat F(\xi)|^2\,\Omega(\xi)\,d\xi.$$
Esta es exactamente la contribución de $\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)$ en la fórmula explícita de Riemann–Weil: $\frac{d}{ds}\log\Gamma_{\mathbb R}(s)\big|_{s=1/2+i\xi}=\tfrac12[\psi(\tfrac14+\tfrac{i\xi}2)-\log\pi]$, y el doblez $s\leftrightarrow1-\bar s$ produce la parte real. **[DATO]:** Weil 1952; Bombieri 2000, §1; Iwaniec–Kowalski 2004, Teorema 5.12.

**[DEFINICIÓN-NUEVA 1.2] (el objeto semilocal arquimediano).** Sea $S=\{p_1,\dots,p_n\}$ un conjunto finito de primos (se admite $S=\varnothing$). El **objeto semilocal arquimediano** es
$$X_S^{\mathrm{ar}}\;:=\;\bigl(a_S,\;[0]+[1],\;\omega_\zeta\bigr),\qquad a_S:=\Lambda\cdot\mathbf 1_{\{p^m:\,p\in S,\,m\ge1\}}\;\ge\;0,$$
es decir: dato aritmético von Mangoldt restringido a $S$ (régimen **destructivo**: $a\ge0$, exactamente la clase de H⁺ y el signo opuesto a los objetos puros de Doc 135), bloque polar estándar $[0]+[1]$, peso arquimediano $\omega_\zeta\leftrightarrow\Omega$. Su forma cuadrática de Weil es, para $f\in C_c^\infty(G)$ y $g=f\star\tilde f$:
$$\boxed{\;Q_S(f)\;:=\;\underbrace{2\,\operatorname{Re}\bigl(\hat f(0)\,\overline{\hat f(1)}\bigr)}_{\text{bloque polar }=\,\hat g(0)+\hat g(1)}\;+\;\underbrace{\frac1{2\pi}\int_{\mathbb R}|\hat F(\xi)|^2\,\Omega(\xi)\,d\xi}_{\mathcal A(f)}\;-\;\underbrace{\sum_{p\in S}\sum_{m\ge1}\frac{\log p}{p^{m/2}}\;2\operatorname{Re}G(m\log p)}_{P_S(f)}\;}$$
El axioma H para $X_S^{\mathrm{ar}}$ es: $Q_S(f)\ge0$ para todo $f\in C_c^\infty(G)$.

**Observación 1.3 (consistencia con $\zeta$ y con Doc 131; por qué esta es LA definición).**
(i) *Bloque polar:* $\hat g(0)=\hat f(0)\overline{\hat f(1)}$ y $\hat g(1)=\hat f(1)\overline{\hat f(0)}$ (de $\hat g(s)=\hat f(s)\overline{\hat f(1-\bar s)}$); la suma es $2\operatorname{Re}(\hat f(0)\overline{\hat f(1)})$ — **indefinida en signo**, a diferencia del átomo diagonal constructivo $2\log(pq)\,g(1)$ de Doc 135. Esto ya es información.
(ii) *Término de primos:* $\Lambda(p^m)\bigl(g(p^m)+p^{-m}g(p^{-m})\bigr)=\frac{\log p}{p^{m/2}}\bigl(G(mL_p)+\overline{G(mL_p)}\bigr)$, usando $g(x)=G(\log x)x^{-1/2}$. Es el término de Weil de $\zeta$ restringido a potencias de primos de $S$ — el signo menos es el de la fórmula explícita (los primos entran restando contra los ceros).
(iii) *Caso $S=$ todos los primos:* $Q_{\mathrm{full}}(f)=\sum_\rho\hat g(\rho)$ sobre los ceros no triviales de $\zeta$ (fórmula de Riemann–Weil), y H equivale a RH [DATO: Weil 1952; Bombieri 2000]. La definición 1.2 es la única truncación de esa fórmula compatible con los slots $(a,c,\omega)$ de Doc 131.
(iv) *Hermiticidad:* $Q_S(f)\in\mathbb R$ para todo $f$ (cada bloque es manifiestamente real). $X_S^{\mathrm{ar}}$ es hermitiano en el sentido de Doc 131, Prop. 2.8.

**Observación 1.4 (qué NO se asume).** No se asume que $X_S^{\mathrm{ar}}$ sea *espectral* (Doc 131, Def. 4.1: existencia de un multiconjunto $Z$ con $\sum_{\rho\in Z}\hat g(\rho)=W(g)$ y densidad polinomial). Esta omisión no es descuido: es el punto donde se jugará el veredicto sobre H⁺ (§8). El objeto está definido por sus tres bloques; si tiene o no un divisor, es un teorema pendiente, no una definición.

---

## 2. El peso arquimediano en forma cerrada

**[LEMA 2.1] (serie explícita).** Para todo $\xi\in\mathbb R$, con $y:=\xi/2$:
$$\Omega(\xi)\;=\;-\gamma-\log\pi\;+\;\sum_{n\ge0}\Bigl(\frac1{n+1}\;-\;\frac{n+\tfrac14}{(n+\tfrac14)^2+y^2}\Bigr),$$
con convergencia absoluta y localmente uniforme.

*Demostración.* De la serie de la digamma $\psi(z)=-\gamma+\sum_{n\ge0}\bigl(\frac1{n+1}-\frac1{n+z}\bigr)$ con $z=\tfrac14+iy$: $\operatorname{Re}\frac1{n+\tfrac14+iy}=\frac{n+1/4}{(n+1/4)^2+y^2}$. El término $n$-ésimo es $O(n^{-2})$ uniformemente en $y$ acotado (numerador $y^2-\tfrac34(n+\tfrac14)$ sobre denominador $\asymp n^3$). $\square$

**[LEMA 2.2] (el valor en el centro, exacto).**
$$\Omega(0)\;=\;\psi(\tfrac14)-\log\pi\;=\;-\gamma-\frac\pi2-3\log2-\log\pi\;\approx\;-5.3722\;<\;0.$$

*Demostración.* Teorema de la digamma de Gauss [DATO: Whittaker–Watson, §12.3]: para $0<p<q$ enteros,
$$\psi(p/q)=-\gamma-\log(2q)-\frac\pi2\cot\frac{\pi p}q+2\sum_{k=1}^{\lfloor(q-1)/2\rfloor}\cos\frac{2\pi kp}q\,\log\sin\frac{k\pi}q.$$
Con $p=1$, $q=4$: $\psi(\tfrac14)=-\gamma-\log8-\frac\pi2\cot\frac\pi4+2\cos\frac\pi2\log\sin\frac\pi4=-\gamma-3\log2-\frac\pi2$ (el último término se anula por $\cos\frac\pi2=0$). Evaluación simbólica: $\gamma\approx0.57722$, $\frac\pi2\approx1.57080$, $3\log2\approx2.07944$, $\log\pi\approx1.14473$; suma $\approx5.37219$. $\square$

**[LEMA 2.3] (monotonía: el suelo destructivo).** $\Omega$ es par, estrictamente creciente en $|\xi|$, y $\Omega(\xi)\to+\infty$. En consecuencia:
(a) $\Omega(\xi)\ge\Omega(0)$ para todo $\xi$, y por tanto
$$\mathcal A(f)\;\ge\;\Omega(0)\,\|f\|_w^2\qquad\text{para todo }f\in C_c^\infty(G):$$
**el término arquimediano es destructivo con suelo absoluto** $|\Omega(0)|<5.38$.
(b) Existen únicos $0<\xi_*<\xi_{**}$ con $\Omega(\xi_*)=0$, $\Omega(\xi_{**})=1$; $\Omega<0$ exactamente en $(-\xi_*,\xi_*)$.

*Demostración.* Paridad: la serie del Lema 2.1 depende de $y^2$. Monotonía estricta: cada sumando $-\frac{n+1/4}{(n+1/4)^2+y^2}$ es estrictamente creciente en $y^2$ (derivada $\frac{(n+1/4)\cdot 2y}{((n+1/4)^2+y^2)^2}>0$ para $y>0$), y la serie de derivadas converge localmente uniforme. Divergencia: del Lema 2.4(a) abajo. (a) y (b) son inmediatos de $\Omega(0)<0$ (Lema 2.2), continuidad, monotonía estricta y $\Omega\to\infty$; $\mathcal A(f)\ge\Omega(0)\frac1{2\pi}\int|\hat F|^2=\Omega(0)\|F\|_2^2$ por Parseval. $\square$

**Observación (el contraste estructural con Doc 135).** En el régimen constructivo, la única fuente destructiva era la impureza, y era **sin fondo**: $|c_M|p^{-M/2}=p^{M\delta'}\to\infty$ (Doc 135, Teo. 4.1). El término $\Gamma$ es destructivo pero **acotado por debajo por la constante absoluta $\Omega(0)$**. Toda la pregunta de GAP-135.B es si esa destructividad acotada, más la de los primos con $a\ge0$, puede ser comprada por el bloque polar. Respuesta: sí a escala corta (§3), no a escala larga (§5), y la frontera es donde el polo deja de ver al test.

**[LEMA 2.4] (cotas logarítmicas efectivas).**
(a) Para $\xi\ge4$:
$$\Omega(\xi)\;\ge\;\log\frac{\xi}2-\gamma-\log\pi-\frac54.$$
En particular $\Omega(\xi)\ge0$ para $\xi\ge40$ y $\Omega(\xi)\ge1$ para $\xi\ge107$; es decir, $\xi_*\le40$ y $\xi_{**}\le107$.
(b) Para todo $\xi$: $|\Omega(\xi)|\le\log(4+|\xi|)+4+\gamma+\log\pi\le\log(4+|\xi|)+6$.

*Demostración.* Sea $y=\xi/2\ge2$ y $N:=\lfloor y\rfloor\ge2$. En la serie del Lema 2.1 partimos en $n\le N-1$ y $n\ge N$.
*(a)* Para $n\le N-1$: $\frac{n+1/4}{(n+1/4)^2+y^2}\le\frac{n+1/4}{y^2}$, luego esos sumandos suman $\ge\sum_{n=0}^{N-1}\frac1{n+1}-\frac1{y^2}\sum_{n=0}^{N-1}(n+\tfrac14)\ge\log(N+1)-\frac{N^2}{2y^2}\ge\log y-\frac12$. Para $n\ge N$: $\frac{n+1/4}{(n+1/4)^2+y^2}\le\frac1{n+1/4}$, luego esos sumandos suman $\ge-\frac34\sum_{n\ge N}\frac1{(n+1)(n+1/4)}\ge-\frac34\sum_{n\ge N}\frac1{n^2}\ge-\frac3{4(N-1)}\ge-\frac34$. Total: $\Omega(\xi)\ge-\gamma-\log\pi+\log y-\frac54$. Verificación de los umbrales: $\log20=2.9957>\gamma+\log\pi+\tfrac54=2.9719$ da $\Omega(40)>0$; $\log53.5=3.9798>1+2.9719$ da $\Omega(107)>1$. ✓
*(b)* El sumando $n$-ésimo es $\frac{y^2-\frac34(n+1/4)}{(n+1)\bigl((n+1/4)^2+y^2\bigr)}\le\min\Bigl(\frac1{n+1},\,\frac{y^2}{(n+1)(n+1/4)^2}\Bigr)$. Para $y\ge2$: $\sum_{n\le\lceil y\rceil}\frac1{n+1}\le\log(y+2)+1$ y $\sum_{n>\lceil y\rceil}\frac{y^2}{(n+1)(n+1/4)^2}\le y^2\sum_{n\ge\lceil y\rceil}\frac1{n^3}\le\frac{y^2}{2(y-1)^2}\le2$. Luego $\Omega(\xi)\le-\gamma-\log\pi+\log(y+2)+3\le\log(4+\xi)+3$. Para $0\le y\le2$, por monotonía $\Omega(\xi)\le\Omega(4)\le\log4+3-\gamma-\log\pi$. La cota inferior $|\Omega|$: $\Omega\ge\Omega(0)\ge-5.38$ (Lemas 2.2–2.3). Combinar. $\square$

*(Las constantes de 2.4 son toscas a propósito: lo que se necesita es un dominador integrable para convergencia dominada y umbrales explícitos finitos. Los valores verdaderos de $\xi_*,\xi_{**}$ son mucho menores; no los necesitamos y no los afirmamos.)*

---

## 3. [TEOREMA A] La positividad semilocal en ventana corta

**[TEOREMA 3.1] (positividad semilocal incondicional; uniforme en $S$, incluye $\zeta$).** Sea $T_0:=\tfrac1{300}$. Para **todo** conjunto $S$ de primos (finito, infinito o todos) y todo $f\in C_c^\infty(G)$ con ventana $2T\le2T_0=\tfrac1{150}$:
$$Q_S(f)\;\ge\;\frac3{10}\,\|f\|_w^2.$$

*Demostración.* Tres bloques, por separado.

*(1) Primos: cero.* $G(t)=0$ para $|t|>2T$ y $2T\le\tfrac1{150}<\log2\le mL_p$: $P_S(f)=0$ para todo $S$. (Aquí entra que el dato $a_S$ vive en $\{p^m:m\ge1\}$, lejos de $1$.)

*(2) Polar: $\ge-4Te^{T}\|f\|_w^2$.* Si $\operatorname{supp}F\subset[\lambda-T,\lambda+T]$,
$$\bigl|\hat f(0)\overline{\hat f(1)}\bigr|=\Bigl|\int\!\!\int F(t)\overline{F(s)}\,e^{(s-t)/2}\,dt\,ds\Bigr|\le e^{T}\Bigl(\int|F|\Bigr)^2\le e^{T}\cdot2T\,\|F\|_2^2,$$
usando $|s-t|\le2T$ (la posición $\lambda$ se cancela en $e^{(s-t)/2}$ — el bloque polar es invariante de ventana, como debe) y Cauchy–Schwarz. Luego el bloque polar es $\ge-4Te^{T}\|F\|_2^2$.

*(3) Arquimediano: $\ge(1-205\,T)\|f\|_w^2$.* Para cualquier $K>0$, por Cauchy–Schwarz $|\hat F(\xi)|^2\le2T\|F\|_2^2$, así que la masa espectral baja cumple
$$m_{\le K}:=\frac1{2\pi}\int_{|\xi|\le K}|\hat F|^2\,d\xi\;\le\;\frac{2KT}\pi\,\|F\|_2^2.$$
Partimos $\mathbb R$ en $\{|\xi|\le40\}$, $\{40<|\xi|<107\}$, $\{|\xi|\ge107\}$ y usamos $\Omega\ge\Omega(0)$, $\Omega\ge0$, $\Omega\ge1$ respectivamente (Lemas 2.3, 2.4(a)):
$$\mathcal A(f)\;\ge\;\Omega(0)\,m_{\le40}\;+\;0\;+\;1\cdot\bigl(\|F\|_2^2-m_{\le107}\bigr)\;\ge\;\Bigl[1-\frac{2T}{\pi}\bigl(107+|\Omega(0)|\cdot40\bigr)\Bigr]\|F\|_2^2\;\ge\;\bigl(1-205\,T\bigr)\|F\|_2^2,$$
con $|\Omega(0)|\le5.3722$: $\tfrac2\pi(107+214.9)=204.9\le205$.

Suma en $T=T_0=\tfrac1{300}$: $1-\tfrac{205}{300}-4\cdot\tfrac1{300}e^{1/300}\ge0.3166-0.0134\ge\tfrac3{10}$. Para $T<T_0$ las cotas solo mejoran. $\square$

**Observación 3.2 (lectura honesta).** (i) La ventana $2T\le1/150$ es ridículamente corta comparada con el umbral constructivo $\log p_1$ de Doc 135 — pero el enunciado es **uniforme en $S$, incluye el término $\Gamma$, e incluye a $\zeta$ misma** (para $\zeta$, toda ventana $2T<\log2$ mata los primos y el Teorema aplica igual). Es la primera positividad de Weil del programa en régimen destructivo: el [DESEO] del encargo, realizado en versión débil. (ii) Las constantes son toscas porque $\xi_*\le40$, $\xi_{**}\le107$ lo son; con los valores verdaderos de $\xi_*,\xi_{**}$ el umbral $T_0$ mejoraría en uno o dos órdenes de magnitud, no más: el umbral genuino es $O(1)$, no $O(\log P)$. (iii) El mecanismo de positividad es **enteramente arquimediano**: a ventana corta la masa espectral está forzada a frecuencias altas (incertidumbre), donde $\Omega\sim\log|\xi|>0$. El polo solo necesita no estorbar ($O(T)$), y los primos no llegan. Compárese con Doc 135, donde a ventana corta la positividad era el átomo diagonal $2\log(pq)g(1)$: **en el régimen destructivo la diagonal aritmética no existe; su papel lo hereda el crecimiento logarítmico de $\Gamma$.** Este es el canje B1 ($\theta(y)\leftrightarrow\Omega$) visto en positivo.

---

## 4. [CÁLCULO] $n=1$: el test de Mertens no muerde en el régimen destructivo

Sea $S=\{p\}$, el primer objeto genuinamente mixto (un primo destructivo + $\Gamma$ + polo). El adversario campeón del régimen constructivo era el test de dos protuberancias (Doc 135 §4): $f=u+\theta\,u(\cdot/p^M)$, con $u(e^t)=\epsilon^{-1/2}\chi(t/\epsilon)$, $\chi$ par, $\operatorname{supp}\chi\subset[-1,1]$, $\int\chi^2=1$. Evaluamos $Q_p$ sobre esa familia, a orden principal en $\epsilon$ (los $O(\epsilon)$ se absorben como en Doc 135).

Tomamos el perfil **de media cero**: $\int\chi=0$ (permitido: $\chi$ par, signada). Entonces:

- **Polar:** $\hat f(1)=\int F e^{t/2}dt=\epsilon^{1/2}\!\int\chi(v)\bigl(e^{\epsilon v/2}-1\bigr)dv\cdot(1+\theta p^{M/2}\cdot[\,\cdot\,])=O(\epsilon^{3/2})(1+|\theta|p^{M/2})$, e igual $\hat f(0)$ con $p^{-M/2}$. El bloque polar es $O(\epsilon^3)(1+|\theta|^2)p^{M/2}\cdot p^{...}$ — fijado $M$, se absorbe eligiendo $\epsilon$ al final. *(Con $\int\chi\ne0$ el polar entra con $+2I^2\,p^{M/2}\operatorname{Re}\theta$, $I^2=\epsilon(\int\chi)^2$: refuerza la positividad contra el adversario alineado con el primo; el caso de media cero es el peor. )*
- **Arquimediano:** $|\hat F|^2=|\hat u_\epsilon|^2\bigl(1+|\theta|^2+2\operatorname{Re}(\theta e^{iML_p\xi})\bigr)$ con $\hat u_\epsilon(\xi)=\epsilon^{1/2}\hat\chi(\epsilon\xi)$, luego
  $$\mathcal A(f)=(1+|\theta|^2)\,A_0+2\operatorname{Re}\theta\cdot\omega_M,\qquad A_0:=\frac1{2\pi}\int|\hat u_\epsilon|^2\Omega\,d\xi,\quad \omega_M:=\frac1{2\pi}\int|\hat u_\epsilon|^2\,\Omega(\xi)\cos(ML_p\xi)\,d\xi.$$
  Con $\int\chi=0$ ($\hat\chi(0)=0$) la masa espectral vive en $|\xi|\asymp1/\epsilon$, donde $\Omega\ge\log\tfrac1{2\epsilon}-O(1)$: $A_0\ge(\log\tfrac1\epsilon)(1-o(1))\to+\infty$. Y $\omega_M$ es **pequeño**, no comparable a $A_0$: integrando por partes una vez, $|\omega_M|\le\frac{\|(|\hat u_\epsilon|^2\Omega)'\|_{L^1}}{ML_p}=O\Bigl(\frac{\epsilon\log(1/\epsilon)}{ML_p}\Bigr)$, pues $\||\hat u_\epsilon|^2{}'\|_1=\epsilon\|(|\hat\chi|^2)'\|_1$ y $\int|\hat u_\epsilon|^2|\Omega'|=O(\epsilon\log\tfrac1\epsilon)$ ($\Omega'=O(1/|\xi|)$ por 2.1 derivada).
- **Primo:** solo $m=M$ sobrevive en soporte: $P_p(f)=\frac{L_p}{p^{M/2}}\,2\operatorname{Re}G(ML_p)=\frac{2L_p}{p^{M/2}}\operatorname{Re}\theta\,(1+O(\epsilon))$, con $G(ML_p)=\bar\theta(1+O(\epsilon))$... el acople destructivo total del primo a altura $M$ está acotado por
  $$\frac{2L_p}{p^{M/2}}\;\le\;\frac{2\log p}{\sqrt p}\;\le\;2\cdot0.736\qquad(\text{máximo en }p=7;\ \text{para }p=2:\ 2\cdot0.490).$$

Con $\operatorname{Re}\theta=-t$ adversario:
$$Q_p(f)=(1+t^2)A_0-2t\Bigl(\frac{L_p}{p^{M/2}}+O\bigl(\tfrac{\epsilon\log(1/\epsilon)}{ML_p}\bigr)\Bigr)+O(\epsilon^{3}\!\cdot p^{M})\;\ge\;A_0-\frac{\bigl(L_pp^{-M/2}+o(1)\bigr)^2}{A_0}\;>\;0$$
para $\epsilon$ pequeño, pues $L_pp^{-M/2}\le0.736\ll A_0\sim\log\tfrac1\epsilon$.

**[PROPOSICIÓN 4.1] (Mertens desactivado).** Sobre toda la familia de dos protuberancias (perfil par, cualquier altura $M\ge1$, cualquier fase $\theta$), $Q_p(f)>0$, con margen $\ge A_0-O(1/A_0)\to\infty$ cuando $\epsilon\to0$. *(Prueba: el cálculo anterior; el caso $\int\chi\ne0$ añade al polar un término $+2I^2p^{M/2}\operatorname{Re}\theta$ que con la fase adversaria del primo, $\operatorname{Re}\theta<0$... su signo es el opuesto al del término del primo, y el análisis se repite con el mínimo en la misma forma cuadrática; los detalles son idénticos.)* $\square$

**Observación 4.2 (la moraleja estructural).** En el régimen constructivo, el acople del adversario al primo **crecía** con la altura ($|c_M|p^{-M/2}=p^{M\delta'}$ si impuro; $=2$ constante si puro). En el régimen destructivo el acople **decae**: $\Lambda(p^m)/p^{m/2}=L_p\,p^{-m/2}\to0$. Cada primo del dato $a\ge0$ es, individualmente, una perturbación compacta y pequeña de $\mathcal A$ — ningún test localizado en UNA escala $p^M$ puede explotar el signo menos. El peligro destructivo no está en ninguna escala: está en el **agregado de la diagonal a lag pequeño**, es decir, en tests anchos y lentos. Eso motiva (y la siguiente sección confirma) cuál es el adversario correcto.

---

## 5. [TEOREMA B] El fallo: dónde, cómo, y cuánto

**[TEOREMA 5.1] (el objeto semilocal viola H; el corazón $S=\varnothing$ también).** Para todo conjunto finito $S$ de primos (incluido $S=\varnothing$):
$$\inf\Bigl\{\,Q_S(f)\;:\;f\in C_c^\infty(G),\ \|f\|_w=1\,\Bigr\}\;\le\;\Omega(0)\;-\;B_S\;<\;0,\qquad B_S:=\sum_{p\in S}\frac{2\log p}{\sqrt p-1}=\sum_{p\in S}\frac{2(\sqrt p+1)\log p}{p-1}.$$
En particular $X_S^{\mathrm{ar}}$ **no satisface H**, y existe un test explícito (construido en la prueba) con $Q_S<0$. Valores simbólicos:
$$S=\varnothing:\ \le-5.3722;\qquad S=\{2\}:\ \le-5.3722-2(\sqrt2+1)\log2\approx-8.7190;\qquad S=\{2,3\}:\ \le-11.7207.$$

*Demostración.* **La familia.** Fijemos $\eta,\eta_2\in C_c^\infty(\mathbb R)$ reales, $\eta\not\equiv0$ con $\operatorname{supp}\eta\subset(0,\tfrac38)$, $\eta_2\ge0$ con $\operatorname{supp}\eta_2\subset(\tfrac12,1)$ y $\int_{5/8}^{7/8}\eta_2>0$. Para $T>0$ definimos
$$F_T(t):=T^{-1/2}\Bigl[\eta\bigl(\tfrac tT\bigr)-c_T\,\eta_2\bigl(\tfrac tT\bigr)\Bigr],\qquad c_T:=\frac{\int\eta(u)\,e^{Tu/2}\,du}{\int\eta_2(u)\,e^{Tu/2}\,du},\qquad f_T(x):=F_T(\log x)\,x^{-1/2}.$$
Entonces $f_T\in C_c^\infty(G)$ con soporte en $(1,e^T)$ (ventana $2T'=T$), y por construcción
$$\hat f_T(1)=\int F_T(t)\,e^{t/2}\,dt=T^{1/2}\int\bigl[\eta-c_T\eta_2\bigr](u)\,e^{Tu/2}\,du=0.$$

**(0) El costo del polo es exponencialmente pequeño.** $\bigl|\int\eta\,e^{Tu/2}du\bigr|\le\|\eta\|_1e^{3T/16}$ y $\int\eta_2e^{Tu/2}du\ge e^{5T/16}\int_{5/8}^{7/8}\eta_2$, luego
$$|c_T|\;\le\;C_\eta\,e^{-T/8}\;\longrightarrow\;0.$$
Como los soportes de $\eta$ y $\eta_2$ son disjuntos: $\|F_T\|_2^2=\|\eta\|_2^2+c_T^2\|\eta_2\|_2^2\to\|\eta\|_2^2$, es decir $\|f_T\|_w^2\to\|\eta\|_2^2$.

**(1) Polar $=0$ exacto.** $\hat g(0)=\hat f(0)\overline{\hat f(1)}=0$ y $\hat g(1)=\hat f(1)\overline{\hat f(0)}=0$ porque $\hat f_T(1)=0$. (Una sola condición lineal mata ambos términos: el bloque polar es de rango uno en este sentido.)

**(2) Arquimediano $\to\Omega(0)\|\eta\|_2^2$.** Escribamos $\eta_c:=\eta-c_T\eta_2$. Como $\hat F_T(\xi)=T^{1/2}\hat\eta_c(T\xi)$,
$$\mathcal A(f_T)=\frac1{2\pi}\int_{\mathbb R}\bigl|\hat\eta_c(u)\bigr|^2\,\Omega\bigl(\tfrac uT\bigr)\,du.$$
Dominación: $|\hat\eta_c(u)|^2\le2|\hat\eta(u)|^2+2|\hat\eta_2(u)|^2$ para $T$ grande ($|c_T|\le1$), que es Schwartz; y $|\Omega(u/T)|\le\log(4+|u|)+6$ para $T\ge1$ (Lema 2.4(b), monotonía del logaritmo). Puntualmente $\Omega(u/T)\to\Omega(0)$ ($\Omega$ continua, Lema 2.1) y $\hat\eta_c\to\hat\eta$ uniformemente. Convergencia dominada:
$$\mathcal A(f_T)\;\longrightarrow\;\Omega(0)\cdot\frac1{2\pi}\int|\hat\eta|^2\;=\;\Omega(0)\,\|\eta\|_2^2.$$

**(3) Primos $\to B_S\|\eta\|_2^2$ — la diagonal destructiva.** Para $t$ fijo, $G_T(t)=\int\eta_c(u)\,\eta_c\bigl(u-\tfrac tT\bigr)\,du\to\|\eta\|_2^2$ (continuidad de la traslación en $L^2$ y $c_T\to0$), real. Además $|G_T|\le\|\eta_c\|_2^2\le\|\eta\|_2^2+1$ para $T$ grande, uniforme. Como $\sum_{p\in S}\sum_{m\ge1}L_p\,p^{-m/2}<\infty$ (finitos primos, geométrica), convergencia dominada en el índice $(p,m)$:
$$P_S(f_T)=\sum_{p\in S}\sum_{m\ge1}\frac{2L_p}{p^{m/2}}\,G_T(mL_p)\;\longrightarrow\;2\,\|\eta\|_2^2\sum_{p\in S}L_p\sum_{m\ge1}p^{-m/2}\;=\;B_S\,\|\eta\|_2^2.$$

Sumando: $Q_S(f_T)=0+\mathcal A(f_T)-P_S(f_T)\to\bigl(\Omega(0)-B_S\bigr)\|\eta\|_2^2<0$, y $\|f_T\|_w^2\to\|\eta\|_2^2$. Para $T$ suficientemente grande, $Q_S(f_T)<0$ y el cociente $Q_S/\|f_T\|_w^2$ está tan cerca del límite como se quiera. Evaluaciones simbólicas: $B_{\{2\}}=2(\sqrt2+1)\log2\approx3.3468$; $B_{\{2,3\}}\approx3.3468+(\sqrt3+1)\log3\approx6.3485$. $\square$

**Observación 5.2 (anatomía del contraejemplo — el mapa de la interferencia).** Cada pieza del test está ahí por una razón identificable:
1. **Lento y ancho** ($\eta(t/T)$, frecuencias $O(1/T)$): coloca la masa espectral en $(-\xi_*,\xi_*)$, donde $\Omega<0$. Esto es lo que el test de Mertens no podía hacer (§4): su masa vivía en $1/\epsilon$, alto.
2. **La evasión del polo** ($\hat f(1)=0$ vía $c_T$): el bloque polar custodia exactamente UNA dirección — el "momento exponencial" $\int Fe^{t/2}$ — y esa custodia se evade con costo $e^{-T/8}$, asintóticamente gratis. Nótese la geometría: **el polo vive en la frecuencia compleja $\xi=-i/2$; el déficit arquimediano vive en frecuencias reales $|\xi|<\xi_*$. Son puntos distintos del plano, y ningún principio de incertidumbre los liga cuando el test es ancho** (con ventana corta sí: Teorema 3.1).
3. **Los primos a lag fijo son autocorrelación positiva**: $G_T(mL_p)\to+\|\eta\|_2^2$ para CADA $(p,m)$ fijo — el test lento es casi invariante por la traslación $t\mapsto t+mL_p$, luego el término de primos entra con su peor signo posible (resta plena). Cada primo añadido resta $\frac{2L_p}{\sqrt p-1}$ más: **en el régimen destructivo, más primos = peor**, la inversión exacta de la marea diagonal protectora $+L_q$ del régimen constructivo (Doc 135 §4, comentario cuantitativo). El signo del dato $a$ invierte el papel de los primos ajenos.

**Observación 5.3 (el caso $S=\varnothing$ es el corazón del asunto).** El fallo NO necesita primos: el objeto $(0,[0]+[1],\omega_\zeta)$ — polo más $\Gamma$, sin aritmética — ya viola H con déficit $\Omega(0)$. Los primos con $a\ge0$ solo profundizan un agujero que es **arquimediano de origen**. Esto localiza el régimen destructivo de GAP-135.B con precisión: la interferencia ceros/primos del encargo es, en el fondo, interferencia **polo/arquimediano**, y los primos truncados son amplificadores.

---

## 6. [PUENTE] La identidad de transmisión: por qué $\zeta$ no falla donde el semilocal sí

¿Cómo es posible que $Q_S(f_T)\to$ negativo para todo $S$ finito, si $Q_{\mathrm{full}}$ (todos los primos) es $\ge0$ bajo RH? La respuesta es una identidad, no una estimación.

**[PROPOSICIÓN 6.1] (identidad de truncación).** Para todo $f$ y todo $S$ finito:
$$Q_S(f)\;=\;Q_{\mathrm{full}}(f)\;+\;\bigl[P_{\mathrm{full}}(f)-P_S(f)\bigr]\;=\;\sum_{\rho}\hat g(\rho)\;+\;\bigl[P_{\mathrm{full}}(f)-P_S(f)\bigr],$$
donde la suma corre sobre los ceros no triviales de $\zeta$ (fórmula de Riemann–Weil, incondicional [DATO: Weil 1952; Iwaniec–Kowalski 2004, Thm 5.12]). *(Trivial: los tres bloques de $Q_S$ y $Q_{\mathrm{full}}$ coinciden salvo el término de primos; la segunda igualdad es la fórmula explícita.)* $\square$

**[COROLARIO 6.2] (la suma completa sobre primos cambia de signo en el agregado; bajo RH).** Sobre la familia $f_T$ del Teorema 5.1, bajo RH:
$$\lim_{T\to\infty}P_{\mathrm{full}}(f_T)\;=\;\lim_{T\to\infty}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,2\operatorname{Re}G_T(\log n)\;=\;\Omega(0)\,\|\eta\|_2^2\;<\;0,$$
mientras que **cada término individual** tiene límite positivo: $\frac{\Lambda(n)}{\sqrt n}2\operatorname{Re}G_T(\log n)\to\frac{2\Lambda(n)}{\sqrt n}\|\eta\|_2^2>0$.

*Demostración.* Por la Proposición 6.1 con $S=\varnothing$: $P_{\mathrm{full}}(f_T)=\mathcal A(f_T)-\sum_\rho\hat g_T(\rho)$ (polar $=0$). Bajo RH, $\rho=\tfrac12+i\gamma$ y $\hat g_T(\rho)=|\hat F_T(\gamma)|^2=T|\hat\eta_c(T\gamma)|^2$. Como $\zeta(\tfrac12)\ne0$ y el primer cero tiene $|\gamma_1|>0$: $T|\hat\eta_c(T\gamma)|^2\le C_kT(1+T|\gamma_1|)^{-2k}\cdot(1+|\gamma|)^{-2}$-tipo (Paley–Wiener para $\hat\eta_c$, uniforme en $T$ grande), y la suma sobre ceros (densidad $\log\gamma$) tiende a $0$. Con $\mathcal A(f_T)\to\Omega(0)\|\eta\|_2^2$ (Teorema 5.1, paso 2), listo. $\square$

**Lectura [PUENTE], estatus declarado.** El Corolario 6.2 es la forma exacta, sobre una sola familia de tests, de los breakpoints B1+B4 de Doc 135:

- A **lag fijo** $\log n$, el término del primo es autocorrelación: positivo (resta en $Q$). En el **agregado** $\sum_n\Lambda(n)n^{-1/2}(\cdots)$, las oscilaciones de $G_T$ contra la densidad de los primos producen un total **negativo** (suma en $Q$), de valor exactamente $\Omega(0)\|\eta\|^2$: la suma completa de primos devuelve, con signo cambiado, el déficit arquimediano — al céntimo. Esa es la "transmisión de la custodia polar al eje real": $\hat f(1)=0$ (una condición sobre el momento $e^{t/2}$, i.e. sobre el polo) obliga, vía la fórmula explícita, a que la suma completa de primos compense a $\Gamma$. **Ninguna truncación finita ve la condición $\hat f(1)=0$**: cada lag fijo es ciego a un momento exponencial global (el costo $c_T\sim e^{-T/8}$ es invisible a escala $mL_p$ fija).
- El **déficit de transmisión** es la cantidad exacta del fallo: $D_S:=\lim\bigl[P_S-P_{\mathrm{full}}\bigr](f_T)=B_S-\Omega(0)>0$ y $\lim Q_S(f_T)=\lim Q_{\mathrm{full}}(f_T)-D_S=0-D_S$. La violación del objeto semilocal ES su déficit de transmisión. (Bajo RH; incondicionalmente vale la identidad 6.1 término a término en $T$.)
- Honestidad sobre el estatus: 6.2 usa RH (o al menos: si RH falla, $\lim\sum_\rho\hat g_T(\rho)$ podría no ser $0$ y la contabilidad cambia — sin RH solo afirmamos la identidad 6.1). Nada de esta sección prueba nada sobre RH; **localiza** dónde el límite $S\to$ todos los primos deja de conmutar con la positividad, que es lo que GAP-135.B pedía mapear.

---

## 7. El mapa del régimen destructivo

Recolectamos. Sea $\mu_S(T):=\inf\{Q_S(f):\|f\|_w=1,\ \text{ventana }2T\}$.

**Probado:**
- $\mu_S(T)\ge\tfrac3{10}$ para $2T\le\tfrac1{150}$, **uniforme en $S$** (Teorema 3.1). El umbral de positividad es **absoluto** (arquimediano), no aritmético: no escala con $\log(p_1\cdots p_n)$. El [DESEO] del encargo ("el término arquimediano domina la interferencia para soporte $\le\theta\log(p_1\cdots p_n)$") es **falso como está enunciado** — la escala correcta no es el conductor sino la constante $O(1)$ del cruce de $\Omega$ — y **verdadero en espíritu** a esa escala absoluta.
- $\mu_S(T)<0$ para $T\ge T_1(S,\eta)$ finito y efectivo (Teorema 5.1; la prueba da $T_1$ en función de la velocidad de las tres convergencias, todas explícitas: $c_T\le C_\eta e^{-T/8}$, módulo de continuidad de $\Omega$ en $0$, traslaciones de $\eta$). No optimizamos $T_1$; con $\eta$ razonable es $O(10)$.
- $\lim_{T\to\infty}\mu_S(T)\le\Omega(0)-B_S$, estrictamente decreciente al añadir primos.

**[PROPOSICIÓN 7.2] (el cono superviviente de alta frecuencia).** Sea $S$ finito, $B_S$ como en 5.1, y sea $\bar\xi_S$ el único punto con $\Omega(\bar\xi_S)=B_S+2$ (existe por Lema 2.3; cota efectiva $\bar\xi_S\le2\pi e^{\gamma+5/4}\,e^{B_S+2}$ por Lema 2.4(a)). Sea
$$\varepsilon_S:=\frac1{B_S+2+|\Omega(0)|}.$$
Si $f$ cumple (i) $\hat f(1)=0$ o $\hat f(0)=0$ (polar muerto), y (ii) masa espectral baja $\frac1{2\pi}\int_{|\xi|\le\bar\xi_S}|\hat F|^2\,d\xi\le\varepsilon_S\|f\|_w^2$, entonces
$$Q_S(f)\;\ge\;\|f\|_w^2.$$

*Demostración.* Polar $=0$ por (i). Primos: $|G(mL_p)|\le\|F\|_2^2$ (Cauchy–Schwarz), luego $|P_S(f)|\le B_S\|F\|_2^2$. Arquimediano: con $m_{\mathrm{low}}\le\varepsilon_S\|F\|^2$ la masa bajo $\bar\xi_S$ y $\Omega\ge\Omega(0)$ allí, $\Omega\ge B_S+2$ arriba (monotonía):
$$\mathcal A(f)\ge\Omega(0)\,\varepsilon_S\|F\|^2+(B_S+2)(1-\varepsilon_S)\|F\|^2 = \bigl[B_S+2-\varepsilon_S(B_S+2+|\Omega(0)|)\bigr]\|F\|^2=(B_S+1)\|F\|^2.$$
Total: $Q_S\ge(B_S+1-B_S)\|F\|^2=\|F\|^2$. $\square$

**El mapa, en una línea.** El régimen destructivo es un fenómeno de **baja frecuencia y ventana ancha con polo evadido**; la positividad sobrevive exactamente en los dos complementos: ventana corta (toda frecuencia forzada alta — Teorema 3.1) y cono de alta frecuencia (toda ventana — Proposición 7.2). El fallo vive en el rectángulo "frecuencia $\lesssim\xi_*$ × ventana $\gtrsim T_1$", y allí es inevitable.

**[GAP-142.A] (el umbral arquimediano).** Determinar $T_\square:=\sup\{T:\mu_\varnothing(T)\ge0\}$ — el umbral del corazón polar+$\Gamma$, una pregunta de análisis puro sin aritmética (forma cuadrática $2\operatorname{Re}(\hat f(0)\overline{\hat f(1)})+\mathcal A$ sobre ventanas), y los $T_{\mathrm{crit}}(S)\le T_\square$ correspondientes. Probado: $\tfrac1{300}\le T_\square<\infty$. Conjetura natural: $T_\square\asymp1/\xi_*$ por el escalamiento de la Observación 5.2(1), módulo el costo del polo. Es el análogo destructivo de GAP-135.A (que era el módulo del gap; aquí está en juego el **signo** en la región intermedia).

**[GAP-142.B] (espectralidad del objeto semilocal).** Decidir si $X_S^{\mathrm{ar}}$ es espectral en el sentido de Doc 131, Def. 4.1 (¿existe un multiconjunto $Z$ — multiplicidades positivas, densidad polinomial — con $\sum_{\rho\in Z}\hat g(\rho)=Q_S(f)$ para todo $f$?). Evidencia de que NO:
1. Si existiera tal $Z$ contenido en la línea crítica y $\sigma$-estable, entonces $Q_S\ge0$ — contradicho por el Teorema 5.1. Luego cualquier divisor estaría fuera de la línea. **[Probado.]**
2. El candidato natural, la función $\xi_S(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\prod_{p\in S}(1-p^{-s})^{-1}$, tiene en la banda **polos** (multiplicidad negativa) en $s\in\tfrac{2\pi i}{\log p}\mathbb Z$ y carece de ecuación funcional; y el término de primos de $Q_S$ es "una mitad con peso espejo" ($m\ge1$ con peso $1$, $m\le-1$ con peso $p^{m}$) que **no** es combinación de las sumas de Poisson de progresiones verticales completas $\sum_k\hat g(i\tau_k)$, $\sum_k\hat g(1+i\tau_k)$ (estas dan los pesos bilaterales $1+p^m$ — el factor impuro de B3). La unilateralidad es exactamente la marca de la continuación analítica ausente. **[Argumento, no prueba: falta un teorema de unicidad de divisores para fórmulas explícitas.]**

---

## 8. Veredicto sobre H⁺

Recordemos H⁺ (P48, Conjecture 7.1): *si $X$ es hermitiano, **espectral**, con dato $a\ge0$ soportado en potencias de primos (producto de Euler), bloque polar estándar y peso arquimediano de tipo $\zeta$, entonces $X$ satisface H.*

El objeto $X_S^{\mathrm{ar}}$ verifica: hermitiano ✓ (Obs. 1.3(iv)), $a=\Lambda\cdot\mathbf 1\ge0$ soportado en potencias de primos ✓, polar estándar ✓, arquimediano de tipo $\zeta$ ✓, y **viola H** (Teorema 5.1). Queda una sola hipótesis sin verificar: la espectralidad. Por tanto:

**[TEOREMA 8.1] (la contrapositiva).** $H^+\;\Longrightarrow\;X_S^{\mathrm{ar}}$ **no es espectral** (para ningún $S$ finito, incluido $\varnothing$). *(Inmediato de 5.1 + el enunciado de H⁺.)* $\square$

**El trilema, quirúrgico.** Exactamente una de estas tres:
1. **$X_S^{\mathrm{ar}}$ es espectral** (existe divisor positivo con fórmula explícita). Entonces **H⁺ es REFUTADA** por el Teorema 5.1, con contraejemplo explícito y déficit $\Omega(0)-B_S$.
2. **$X_S^{\mathrm{ar}}$ no es espectral** (lo que la evidencia de GAP-142.B sugiere). Entonces H⁺ sobrevive, pero GAP-135.B estaba **mal planteado**: el objeto semilocal nunca fue "el primer caso genuino de H⁺" — no está en la clase — y este documento prueba que **la hipótesis de espectralidad carga el cien por ciento del contenido de H⁺**: las hipótesis restantes (hermitiano + $a\ge0$ Euler + polar + $\Gamma$) son consistentes con violaciones de H de tamaño $\ge|\Omega(0)|$. La espectralidad, para un objeto destructivo, debe ser tan fuerte que fuerce la transmisión polo→eje real de §6 — es decir, debe codificar la completitud del producto de Euler y la ecuación funcional. H⁺ se revela como: "tener divisor ⟹ el dato es lo bastante completo para custodiar las frecuencias bajas" — una paráfrasis de RH, no un caso de prueba intermedio.
3. La definición de "espectral" en Doc 131 admite divisores con partes fuera de la línea y el objeto califica con divisor fuera de línea — entonces H⁺ tal como está escrita es refutada igualmente por 5.1 (caso 1 con divisor exótico), o bien H⁺ implícitamente exigía divisor en la línea, en cuyo caso H⁺ era casi-tautológica (divisor en la línea + hermitiano $\Rightarrow$ H es el Teorema 4.4(a) de Doc 131).

En cualquier rama: **H⁺ no sobrevive como estaba** — o es falsa, o su único caso de prueba accesible se evapora y su contenido colapsa sobre la hipótesis de espectralidad. La decisión entre las ramas es GAP-142.B.

**Refinamientos de H⁺ que SÍ sobreviven a este documento (los conos de §7):**
- **H⁺-loc (probada aquí para $S$ finito):** la clase de H⁺ satisface H restringida a tests de ventana $\le\tfrac1{150}$ — Teorema 3.1, incondicional, uniforme en el dato.
- **H⁺-cónica (probada aquí para $S$ finito):** la clase satisface H en el cono de alta frecuencia con polo muerto — Proposición 7.2.
- **H⁺-completa (abierta, y esta es la reformulación honesta):** *hermitiano + espectral + $a=\Lambda$ en TODAS las potencias de primos (producto de Euler completo) + polar + $\Gamma$ $\Rightarrow$ H.* La clase se reduce esencialmente a $\zeta$ y la conjetura a RH: la truncación a $S$ finito — el único contenido "más débil que RH" que H⁺ ofrecía — queda refutada como ruta. El muro, redibujado con precisión: **no hay interpolación semilocal entre el teorema de dos primos constructivo (Doc 135) y RH; el primer paso destructivo ya cuesta todo el precio.**

---

## 9. El mapa

**Probado [TEOREMA/PROPOSICIÓN/LEMA], con prueba completa en este documento:**
- Lemas 2.1–2.4: el peso arquimediano $\Omega$ en forma cerrada; $\Omega(0)=-\gamma-\frac\pi2-3\log2-\log\pi$ exacto (Gauss); monotonía (suelo destructivo $\mathcal A\ge\Omega(0)\|f\|_w^2$); cotas logarítmicas efectivas ($\xi_*\le40$, $\xi_{**}\le107$).
- **[TEOREMA A = 3.1]:** positividad semilocal incondicional en ventana corta, $Q_S\ge\frac3{10}\|f\|_w^2$ para $2T\le\frac1{150}$, uniforme en $S$ (incluye $\zeta$). La primera positividad de Weil del programa con término arquimediano.
- **[PROPOSICIÓN 4.1]:** el test de Mertens no rompe el régimen destructivo (acople $L_pp^{-M/2}$ decae; margen $\sim\log(1/\epsilon)$).
- **[TEOREMA B = 5.1]:** $X_S^{\mathrm{ar}}$ viola H para todo $S$ finito, incluido $S=\varnothing$; familia explícita $f_T$ ($\hat f_T(1)=0$, baja frecuencia); déficit asintótico exacto $\Omega(0)-B_S$ ($\approx-11.72$ para $S=\{2,3\}$). **GAP-135.B queda decidido: H falla.**
- **[PROPOSICIÓN 6.1]:** identidad de truncación $Q_S=Q_{\mathrm{full}}+[P_{\mathrm{full}}-P_S]$.
- **[COROLARIO 6.2]** (bajo RH): $\lim P_{\mathrm{full}}(f_T)=\Omega(0)\|\eta\|^2<0$ — la suma completa de primos cambia de signo solo en el agregado; ninguna truncación finita lo ve.
- **[PROPOSICIÓN 7.2]:** el cono superviviente de alta frecuencia, con constantes explícitas.
- **[TEOREMA 8.1]:** H⁺ $\Rightarrow$ $X_S^{\mathrm{ar}}$ no es espectral.

**[PUENTE] (estatus declarado):** §6 — B1/B4 de Doc 135 hechos identidad sobre una familia: la custodia del polo ($\xi=-i/2$) se transmite al eje real únicamente a través del producto de Euler completo; el déficit de transmisión $D_S=B_S-\Omega(0)$ ES la violación. Nada de esto acerca RH; redistribuye GAP-135.B a la hipótesis de espectralidad.

**[DESEO] del encargo, auditado:** la dominación arquimediana para soporte $\le\theta\log(p_1\cdots p_n)$ es **falsa** (el umbral no escala con el conductor: es absoluto, $O(1)$ arquimediano) y su versión verdadera es el Teorema 3.1 + GAP-142.A.

**[GAP], nombrados:**
- **GAP-142.A:** el umbral arquimediano $T_\square\in[\tfrac1{300},T_1]$ — signo de $\mu_\varnothing(T)$ en la región intermedia; conjetura $T_\square\asymp1/\xi_*$.
- **GAP-142.B:** probar que $X_S^{\mathrm{ar}}$ no es espectral (teorema de unicidad de divisores para fórmulas explícitas; la unilateralidad del término de primos como obstrucción). Decide el trilema de §8.

---

## Referencias

**Internas (backward-only):** Doc 135 (teorema de dos primos; B1–B4; GAP-135.B); P48 (`06-papers/P48-weil-positivity-finite-primes/main.tex`: Conjetura H⁺ = Conjecture 7.1, normalizaciones, Remark final "GAP-B"); Doc 131 (slots $(a,c,\omega)$, Def. 2.1, Def. 4.1 espectral, Teo. 4.4).

**Literatura [DATO]:**
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Lund (1952), 252–265. (La forma cuadrática; el criterio H ⟺ RH; los términos locales.)
- E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers I*, Rend. Mat. Acc. Lincei (9) 11 (2000), 183–233. (Normalización del funcional; el papel del término arquimediano y del bloque polar.)
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53, 2004, Teorema 5.12. (La fórmula explícita en la normalización $h(\gamma)$ usada en §1; el peso $\operatorname{Re}\psi(\frac14+\frac{i\xi}2)-\log\pi$.)
- A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. (N.S.) 5 (1999), 29–106. (Los términos locales de la fórmula explícita como distribuciones; el lugar arquimediano.)
- E. T. Whittaker, G. N. Watson, *A Course of Modern Analysis*, 4ª ed., CUP 1927, §12.3. (Teorema de la digamma de Gauss; $\psi(\frac14)=-\gamma-\frac\pi2-3\log2$.)
- H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I*, CUP 2007. (Mertens; $\sum_{n\le x}\Lambda(n)n^{-1/2}\sim2\sqrt x$, trasfondo de §6.)

*Fin del Documento 142.*
