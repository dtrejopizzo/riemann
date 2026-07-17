# Doc 107 — Ejecución del Problema 5.4: la fórmula de Weil en dos variables con núcleo diagonal multiplicativo

**Phase 36 — Formas A/B/C · junio 2026**
**Autor: David Alejandro Trejo Pizzo**
**Prerrequisitos:** Doc 106 (§3 Prop. 3.5, §5 Lemas 5.2/5.3, Problema 5.4); Doc 98 (modelo de juguete, Prop. 6.1); Doc 96 (Teorema 8.1); Doc 94 (condición C5); P35 (forma de Weil, Hipótesis D); P41 §7.
**Regla absoluta:** ninguna prueba se fabrica. Cada paso es demostración completa o GAP declarado.

---

## 0. Resumen ejecutivo

Este documento ejecuta el experimento del Problema 5.4 del Doc 106: formular la fórmula
explícita de Weil en dos variables, insertar el núcleo diagonal multiplicativo engrosado
$h(x_1,x_2) = g(x_1x_2)\,\varphi(x_1/x_2)$, y decidir si el funcional resultante
$\mathcal{W}_2$ es un candidato para el Lema Faltante 5.2 (realización analítica del
cuadrado tensorial) o si MW-7 reaparece.

**Hallazgos principales:**

1. **(§2) La fórmula doble existe y es incondicional.** $\mathcal{W}_2 := \mathcal{W}
   \otimes \mathcal{W}$ está bien definida sobre $C_c^\infty((\mathbb{R}_+^*)^2)$ por
   iteración de la fórmula de una variable; el lado de ceros doble converge
   **absolutamente** (Paley–Wiener + densidad de ceros), y la expansión completa del
   producto tiene nueve bloques (polos², polos×primos, polos×∞, primos², primos×∞, ∞²,
   y simétricos), todos escritos en §2.3.

2. **(§3) El núcleo engrosado produce la suma de Minkowski.** La restricción diagonal
   cruda $g(x_1x_2)$ diverge (Lema 3.1: la integral transversal $\int_0^\infty
   v^{s_1-s_2-1}dv$ diverge para todo valor del exponente). Con el engrosamiento
   $h = g(x_1x_2)\varphi(x_1/x_2)$ y el cambio $u = x_1x_2$, $v = x_1/x_2$ (jacobiano
   $dx_1dx_2 = \tfrac{1}{2v}\,du\,dv$, exponente transversal $v^{(s_1-s_2)/2-1}$):
   $$\hat h(s_1,s_2) = \tfrac12\,\hat g\!\left(\tfrac{s_1+s_2}{2}\right)
     \hat\varphi\!\left(\tfrac{s_1-s_2}{2}\right),$$
   y el término de ceros es $\tfrac12\sum_{\rho_1,\rho_2}
   \hat g\bigl(\tfrac{\rho_1+\rho_2}{2}\bigr)\hat\varphi\bigl(\tfrac{\rho_1-\rho_2}{2}\bigr)$:
   exactamente el espectro de $\tfrac12(H_C\otimes I + I\otimes H_C)$ con peso espectral
   en la diferencia. La condición 1 del Lema 5.2 se verifica (§5).

3. **(§4) El lado aritmético es AUTÓNOMO.** El término primos×primos es una
   **transformada ponderada de $\Lambda\star\Lambda$**: $\sum_N g(N)\sum_{d\mid N}
   \Lambda(d)\Lambda(N/d)\,\varphi(d^2/N)$ más tres términos de soporte finito — vive en
   el semigrupo de casi-primos con coeficientes aritméticos explícitos, computable sin
   posiciones de ceros. **Los términos mixtos ceros×primos se reabsorben**: son
   artefactos de la presentación semi-expandida; la aplicación iterada de la fórmula de
   una variable los convierte en términos aritmética×aritmética. **MW-7 NO reaparece en
   el funcional.** Donde sí reaparecería (y se delimita con precisión, §4.5): si se
   exigiera una fórmula explícita *propia de una variable* para el objeto doble en la
   variable suma $\sigma$ sola — la función de multiplicidad $w_\varphi(\sigma)$ depende
   de los ceros. El Lema 5.2 no exige eso.

4. **(§5) La signatura $(8,8)$ del bloque tensorial SOBREVIVE.** En el modelo de juguete
   ($m=1$, cuádruplo $\{1/2\pm\delta\pm i\gamma_0\}$), los 16 pares $(\rho_i,\rho_j)$
   se aparean bajo la involución $(\rho_1,\rho_2)\mapsto(1-\bar\rho_1,1-\bar\rho_2)$ en
   **8 órbitas libres de puntos fijos** = 8 planos hiperbólicos: signatura $(8,8)$,
   índice negativo $8 = (4m)^2/2$, exactamente la Proposición 3.5 del Doc 106. El peso
   $\hat\varphi$ **no degenera** la signatura — al contrario, es lo que la salva: dentro
   de los autoespacios degenerados de la suma ($\sigma = 0, \pm i\gamma_0$) solo la
   variable de diferencia separa los pares. Y la conjetura del enunciado ("¿las sumas
   reales $\pm 2\delta$ llevan el índice negativo?") resulta **falsa de modo
   instructivo**: las sumas reales llevan solo $2$ de los $8$ negativos; **la mitad del
   índice negativo vive en sumas puramente imaginarias** ($\rho_i+\rho_j-1 \in
   i\mathbb{R}$), donde la off-criticidad está almacenada en la variable de diferencia
   que solo $\hat\varphi$ ve.

5. **(§6) Balance contra los Lemas 5.2/5.3.** Lema 5.2: condición 1 ✓, condición 2 ✓ —
   **el Lema 5.2 tiene candidato**: $X_2 = \mathcal{W}_2$ restringido a núcleos
   engrosados. El peso íntegro se transfiere al Lema 5.3 (cota de finitud), donde el
   análisis identifica por primera vez en el programa una fuente de cotas genuinamente
   no espectral e incondicional: **las cotas superiores de criba en el semigrupo
   casi-primo** (Selberg; el problema de paridad bloquea asintóticas, no cotas
   superiores). El gap exacto que queda es el **puente criba→índice** (Lema Faltante
   7.2). Riesgo de transmutación documentado: si la cota requerida resultara necesitar
   la *asintótica* de $\Lambda\star\Lambda$, el muro es correlación de
   pares/Hardy–Littlewood (vía Montgomery / Goldston–Montgomery) — un muro de paridad,
   **no** CAP.

**VEREDICTO: CANDIDATO VIVO** (§8). El Lema 5.2 tiene candidato explícito; MW-7 no
reaparece ni en los términos mixtos ni en el lado casi-primo; el bloque $(8,8)$ se
verifica sin degeneración. El siguiente lema a probar queda enunciado con precisión
(Lema Faltante 7.2).

---

## 1. Normalización: la fórmula explícita de Weil en una variable

### 1.1. Clase de prueba y transformada

**Definición 1.1 (clase de prueba).** En todo el documento, la clase de funciones de
prueba es $C_c^\infty(\mathbb{R}_+^*)$ (suaves de soporte compacto en $(0,\infty)$); en
dos variables, $C_c^\infty((\mathbb{R}_+^*)^2)$. Para $f \in C_c^\infty(\mathbb{R}_+^*)$,
la transformada de Mellin es
$$\hat f(s) = \int_0^\infty f(x)\,x^{s-1}\,dx,$$
entera en $s$ (soporte compacto). La involución es $\tilde f(x) =
\overline{f(1/x)}\,x^{-1}$, con $\widehat{\tilde f}(s) = \overline{\hat f(1-\bar s)}$.

**Lema 1.2 (Paley–Wiener multiplicativo y convergencia absoluta del lado de ceros).**
Sea $f \in C_c^\infty(\mathbb{R}_+^*)$ con $\mathrm{supp}\,f \subseteq [e^{-a}, e^{a}]$.
Entonces para todo $N \geq 0$ y todo $\sigma$ en un compacto de $\mathbb{R}$:
$$|\hat f(\sigma+it)| \;\leq\; C_N(f,\sigma)\,(1+|t|)^{-N}.$$
En consecuencia, $\sum_\rho |\hat f(\rho)| < \infty$, donde $\rho$ recorre los ceros no
triviales de $\zeta$ (con multiplicidad).

*Demostración.* Con $x = e^u$: $\hat f(\sigma+it) = \int_{\mathbb{R}}
f(e^u)e^{\sigma u}\,e^{itu}\,du$ es la transformada de Fourier de la función
$u \mapsto f(e^u)e^{\sigma u} \in C_c^\infty([-a,a])$; integración por partes $N$ veces
da la cota, uniforme para $\sigma$ en compactos porque $e^{\sigma u} \leq e^{|\sigma| a}$
sobre el soporte. Para la suma sobre ceros: todo $\rho = \beta + i\gamma$ tiene
$\beta \in (0,1)$ (compacto) y el número de ceros con $|\gamma| \leq T$ es
$N(T) \ll T\log T$ (von Mangoldt; [IK04], Thm. 5.8 o Titchmarsh Cap. IX). Entonces
$\sum_\rho |\hat f(\rho)| \ll \sum_\rho (1+|\gamma|)^{-3} \ll \int_1^\infty
\frac{\log T}{T^3}\,dT\cdot C + C' < \infty$. $\square$

### 1.2. La fórmula explícita

**Definición 1.3 (los tres bloques aritméticos).** Para $f \in
C_c^\infty(\mathbb{R}_+^*)$:
$$D(f) := \hat f(0) + \hat f(1) \qquad \text{(polos: } s=1 \text{ de } \zeta
\text{ y el reflejo } s=0\text{)},$$
$$P(f) := \sum_{n\geq 2} \Lambda(n)\,\bigl[f(n) + n^{-1} f(1/n)\bigr]
\qquad \text{(primos; } \Lambda = \text{von Mangoldt; suma FINITA por soporte
compacto)},$$
$$A(f) := \frac{1}{2\pi}\int_{-\infty}^{\infty} \hat f\!\left(\tfrac12 + it\right)
\Omega(t)\,dt, \qquad
\Omega(t) := \log\pi - \mathrm{Re}\,\frac{\Gamma'}{\Gamma}\!\left(\tfrac14 +
\tfrac{it}{2}\right) \quad \text{(arquimediano)}.$$
$\Omega$ es real, par en $t$ y $\Omega(t) = -\log|t| + O(1)$; la integral converge
absolutamente por el Lema 1.2.

**Teorema 1.4 (Weil 1952; normalización declarada).** Para todo $f \in
C_c^\infty(\mathbb{R}_+^*)$:
$$\boxed{\;\mathcal{W}(f) \;:=\; \sum_\rho \hat f(\rho)
\;=\; D(f) \;-\; P(f) \;-\; A(f).\;}$$

*Estado de la prueba y de la normalización.* Es la fórmula explícita clásica
[Weil 1952; Bombieri 2000; IK04, Thm. 5.12 especializado a $\zeta$ y reescrito en
variable multiplicativa $x = e^u$ con peso trivial]: se obtiene integrando
$-\frac{\xi'}{\xi}(s)\hat f(s)$ sobre un contorno que encierra la banda crítica, usando
$\xi(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)$, $-\frac{\zeta'}{\zeta}(s) = \sum_n
\Lambda(n)n^{-s}$ en $\mathrm{Re}(s) = 2$, la ecuación funcional para la línea
$\mathrm{Re}(s) = -1$ (que produce el término espejo $n^{-1}f(1/n)$ vía
$\frac{1}{2\pi i}\int \hat f(s)n^{s-1}ds = n^{-1}f(1/n)$ sobre la línea reflejada), y
el factor $\Gamma_{\mathbb{R}}$ para $A$. **Declaración de precisión:** la forma exacta
de $\Omega$ (constantes $\log\pi$, $\gamma$, y la versión en $x$-espacio del término
arquimediano como valor principal) varía entre presentaciones equivalentes
[Weil 1952, Bombieri 2000]; en este documento **solo** se usan dos propiedades de $A$:
(A1) es computable sin posiciones de ceros; (A2) es la integral de $\hat f$ sobre la
línea crítica contra un peso fijo par de crecimiento logarítmico. Ningún resultado de
§§2–8 depende de las constantes exactas de $\Omega$. La normalización del P35
(Def. weil, con peso $p^{-n/2}$) corresponde al cambio unitario $f \mapsto x^{1/2}f$;
los resultados estructurales son invariantes bajo ese cambio.

**Observación 1.5 (la distribución de Weil).** El Teorema 1.4 dice que la distribución
temperada (en $u = \log x$)
$$W \;=\; \underbrace{\delta_{\hat\cdot=0} + \delta_{\hat\cdot=1}}_{D}
\;-\; \underbrace{\textstyle\sum_n \Lambda(n)\,[\delta_n + n^{-1}\delta_{1/n}]}_{P}
\;-\; \underbrace{A}_{\text{núcleo suave}}$$
tiene como "transformada espectral" la medida de conteo sobre los ceros. Todo el
documento explota una asimetría: **el lado derecho (aritmético) no menciona los ceros**.

---

## 2. (i) La fórmula de Weil en dos variables: expansión completa

### 2.1. Definición iterada y buena definición

**Definición 2.1 (funcional doble).** Para $h \in C_c^\infty((\mathbb{R}_+^*)^2)$:
$$\mathcal{W}_2(h) \;:=\; \mathcal{W}^{(1)}\Bigl[\,x_1 \longmapsto
\mathcal{W}^{(2)}\bigl[h(x_1,\cdot)\bigr]\Bigr],$$
donde $\mathcal{W}^{(i)}$ es el funcional de Weil (Teorema 1.4) aplicado en la variable
$i$-ésima.

**Lema 2.2 (buena definición, simetría y dos presentaciones).** Para todo
$h \in C_c^\infty((\mathbb{R}_+^*)^2)$:

(a) La función $F(x_1) := \mathcal{W}^{(2)}[h(x_1,\cdot)]$ pertenece a
$C_c^\infty(\mathbb{R}_+^*)$, de modo que la Definición 2.1 tiene sentido, y el
resultado es simétrico: iterar en el orden opuesto da el mismo valor.

(b) **Presentación espectral:**
$$\mathcal{W}_2(h) = \sum_{\rho_1}\sum_{\rho_2} \hat h(\rho_1,\rho_2),
\qquad \hat h(s_1,s_2) := \int_0^\infty\!\!\int_0^\infty
h(x_1,x_2)\,x_1^{s_1-1}x_2^{s_2-1}\,dx_1\,dx_2,$$
con convergencia **absoluta** de la suma doble.

(c) **Presentación aritmética:** $\mathcal{W}_2(h) = \langle (D-P-A)\otimes(D-P-A),\,
h\rangle$, expandida en §2.3, **sin posiciones de ceros**.

*Demostración.* (a) Usamos la presentación aritmética de $\mathcal{W}^{(2)}$:
$F(x_1) = D^{(2)}h - P^{(2)}h - A^{(2)}h$ donde
$D^{(2)}h = \int h(x_1,x_2)\,\frac{dx_2}{x_2} + \int h(x_1,x_2)\,dx_2$,
$P^{(2)}h = \sum_n \Lambda(n)[h(x_1,n) + n^{-1}h(x_1,1/n)]$ (suma finita: solo los $n$
con $n$ o $1/n$ en la proyección del soporte), y $A^{(2)}h$ es la integral del núcleo
arquimediano contra la transformada parcial $\int h(x_1,x_2)x_2^{-1/2+it}dx_2$, que es
suave de soporte compacto en $x_1$ y de decaimiento rápido en $t$ con todas las derivadas
en $x_1$ (Lema 1.2 con parámetro, derivación bajo el signo integral con dominación
uniforme sobre el soporte compacto). Cada uno de los tres bloques es $C_c^\infty$ en
$x_1$ con soporte contenido en la proyección del soporte de $h$. La simetría del orden
se sigue de (b)–(c): ambas presentaciones son manifiestamente simétricas y se prueban
para la definición iterada en cualquier orden. (b) Aplicando el Teorema 1.4 en la
variable 1 a $F$: $\mathcal{W}_2(h) = \sum_{\rho_1}\hat F(\rho_1)$, y
$\hat F(\rho_1) = \mathcal{W}^{(2)}[\,x_2 \mapsto \int h(x_1,x_2)x_1^{\rho_1-1}dx_1\,]
= \sum_{\rho_2}\hat h(\rho_1,\rho_2)$, donde el intercambio
$\int dx_1 \leftrightarrow (D-P-A)^{(2)}$ es legítimo (sumas finitas e integrales
absolutamente convergentes sobre soportes compactos). La convergencia absoluta de la
suma doble: por el argumento del Lema 1.2 en dos variables,
$|\hat h(\rho_1,\rho_2)| \ll_N (1+|\gamma_1|)^{-N}(1+|\gamma_2|)^{-N}$ uniformemente en
las partes reales (compactas), y $N(T) \ll T\log T$ en cada factor. (c) Aplicar la
presentación aritmética en ambas variables; cada término cruzado es una suma finita o
integral absolutamente convergente. $\square$

**Observación 2.3 (factorización).** Si $h(x_1,x_2) = f_1(x_1)f_2(x_2)$, entonces
$\hat h(s_1,s_2) = \hat f_1(s_1)\hat f_2(s_2)$ y $\mathcal{W}_2(h) =
\mathcal{W}(f_1)\,\mathcal{W}(f_2)$: la fórmula doble factoriza como
$\mathcal{W}\otimes\mathcal{W}$, como pide el experimento. El contenido no trivial de la
Definición 2.1 es que extiende $\mathcal{W}\otimes\mathcal{W}$ a núcleos **no
factorizables** — que es lo que el núcleo diagonal necesita.

### 2.2. Notación para la expansión

Escribimos la fórmula de una variable como $\mathcal{W} = D - P - A$ y expandimos el
producto tensorial. Con signos:
$$\mathcal{W}_2 = (D-P-A)\otimes(D-P-A)
= D{\otimes}D - D{\otimes}P - D{\otimes}A - P{\otimes}D + P{\otimes}P + P{\otimes}A
- A{\otimes}D + A{\otimes}P + A{\otimes}A.$$

### 2.3. Los nueve bloques, explícitos

Para $h \in C_c^\infty((\mathbb{R}_+^*)^2)$ general:

**(1) Polos×polos:**
$$D{\otimes}D(h) = \hat h(0,0) + \hat h(0,1) + \hat h(1,0) + \hat h(1,1).$$

**(2) y (2') Polos×primos:**
$$D{\otimes}P(h) = \sum_{n}\Lambda(n)\Bigl[\hat h_1(0;n) + \hat h_1(1;n)
+ n^{-1}\hat h_1(0;1/n) + n^{-1}\hat h_1(1;1/n)\Bigr],$$
donde $\hat h_1(s;y) := \int_0^\infty h(x_1,y)\,x_1^{s-1}dx_1$ (Mellin parcial en la
primera variable, segunda evaluada). $P{\otimes}D$ es el simétrico.

**(3) y (3') Polos×arquimediano:** $D{\otimes}A(h) = \frac{1}{2\pi}\int \Omega(t)
\bigl[\hat h(0,\tfrac12+it) + \hat h(1,\tfrac12+it)\bigr]dt$; simétrico para
$A{\otimes}D$.

**(4) Primos×primos:**
$$P{\otimes}P(h) = \sum_{n_1,n_2}\Lambda(n_1)\Lambda(n_2)\Bigl[
h(n_1,n_2) + n_2^{-1}h(n_1,\tfrac{1}{n_2}) + n_1^{-1}h(\tfrac{1}{n_1},n_2)
+ (n_1n_2)^{-1}h(\tfrac{1}{n_1},\tfrac{1}{n_2})\Bigr],$$
suma finita (soporte compacto en ambas variables).

**(5) y (5') Primos×arquimediano:** $P{\otimes}A(h) = \frac{1}{2\pi}\sum_n
\Lambda(n)\int\Omega(t)\bigl[\hat h_2(n;\tfrac12+it) + n^{-1}
\hat h_2(\tfrac1n;\tfrac12+it)\bigr]dt$, con $\hat h_2(y;s) := \int h(y,x_2)
x_2^{s-1}dx_2$; simétrico para $A{\otimes}P$.

**(6) Arquimediano×arquimediano:**
$$A{\otimes}A(h) = \frac{1}{4\pi^2}\iint \Omega(t_1)\Omega(t_2)\,
\hat h\!\left(\tfrac12+it_1,\,\tfrac12+it_2\right)dt_1\,dt_2.$$

**Teorema 2.4 (fórmula de Weil en dos variables).** Para todo
$h \in C_c^\infty((\mathbb{R}_+^*)^2)$:
$$\sum_{\rho_1,\rho_2}\hat h(\rho_1,\rho_2)
= D{\otimes}D(h) - D{\otimes}P(h) - P{\otimes}D(h) - D{\otimes}A(h) - A{\otimes}D(h)$$
$$\qquad\qquad + P{\otimes}P(h) + P{\otimes}A(h) + A{\otimes}P(h) + A{\otimes}A(h),$$
con todos los bloques absolutamente convergentes y **ninguno dependiente de las
posiciones de los ceros**.

*Demostración.* Lema 2.2(b)(c) con la expansión de signos de §2.2. $\square$

**Observación 2.5 (dónde viven los términos mixtos ceros×primos).** En el producto de
dos fórmulas de una variable para $h = f_1 f_2$ factorizable, uno puede escribir
$\mathcal{W}(f_1)\mathcal{W}(f_2) = \bigl(\sum_{\rho_1}\hat f_1(\rho_1)\bigr)\cdot
\bigl(D-P-A\bigr)(f_2)$: aparecen términos "ceros×primos"
$-\sum_{\rho_1}\hat f_1(\rho_1)\cdot P(f_2)$. Esa es una **presentación
semi-expandida**: mezcla el lado espectral de un factor con el aritmético del otro. El
Teorema 2.4 muestra que la expansión **totalmente aritmética** existe y no contiene
ceros. El análisis fino de esta reabsorción para el núcleo no factorizable — el punto
donde el experimento decide — está en §4.4.

---

## 3. (ii) El núcleo diagonal multiplicativo

### 3.1. La restricción cruda diverge

**Lema 3.1 (divergencia de la diagonal cruda).** Sea $g \in
C_c^\infty(\mathbb{R}_+^*)$, $g \not\equiv 0$, $g \geq 0$, y $h_0(x_1,x_2) :=
g(x_1x_2)$. Entonces la integral de Mellin doble
$$\int_0^\infty\!\!\int_0^\infty g(x_1x_2)\,x_1^{s_1-1}x_2^{s_2-1}\,dx_1\,dx_2$$
**diverge para todo** $(s_1,s_2) \in \mathbb{C}^2$.

*Demostración.* Cambio $u = x_1x_2$, $v = x_1$: $x_2 = u/v$, jacobiano
$dx_1\,dx_2 = \frac{du\,dv}{v}$, integrando $g(u)\,v^{s_1-1}(u/v)^{s_2-1} =
g(u)\,u^{s_2-1}\,v^{s_1-s_2}$. La integral se separa:
$$\Bigl(\int_0^\infty g(u)u^{s_2-1}du\Bigr)\cdot\Bigl(\int_0^\infty
v^{s_1-s_2-1}\,dv\Bigr),$$
y $\int_0^\infty v^{c-1}dv$ diverge para todo $c \in \mathbb{C}$ (en $0$ si
$\mathrm{Re}\,c \leq 0$, en $\infty$ si $\mathrm{Re}\,c \geq 0$; en ambos si
$\mathrm{Re}\,c = 0$). El defecto es geométrico: $h_0$ es constante a lo largo de las
hipérbolas $x_1x_2 = \mathrm{const}$, que son las órbitas no compactas del flujo
anti-diagonal $(x_1,x_2)\mapsto(\lambda x_1,\lambda^{-1}x_2)$; $h_0 \notin
C_c^\infty((\mathbb{R}_+^*)^2)$ y no está en el dominio de $\mathcal{W}_2$. $\square$

### 3.2. El núcleo engrosado y el cambio de variables exacto

**Definición 3.2 (núcleo engrosado).** Para $g, \varphi \in
C_c^\infty(\mathbb{R}_+^*)$:
$$h_{g,\varphi}(x_1,x_2) := g(x_1x_2)\,\varphi(x_1/x_2)
\;\in\; C_c^\infty((\mathbb{R}_+^*)^2),$$
(soporte compacto: $x_1 = \sqrt{uv}$, $x_2 = \sqrt{u/v}$ con $u \in \mathrm{supp}\,g$,
$v \in \mathrm{supp}\,\varphi$ compactos).

**Lema 3.3 (coordenadas suma/diferencia).** El mapa $\Phi(x_1,x_2) := (u,v) =
(x_1x_2,\,x_1/x_2)$ es un **isomorfismo de grupos** $(\mathbb{R}_+^*)^2 \to
(\mathbb{R}_+^*)^2$, con inverso $x_1 = (uv)^{1/2}$, $x_2 = (u/v)^{1/2}$, y
$$dx_1\,dx_2 = \frac{du\,dv}{2v}, \qquad
\frac{dx_1\,dx_2}{x_1x_2} = \frac{1}{2}\,\frac{du\,dv}{u\,v}.$$

*Demostración.* Biyección y homomorfismo: inmediato ($u,v$ son caracteres
multiplicativos de $(x_1,x_2)$ y el inverso está definido globalmente porque
$\mathbb{R}_+^*$ admite raíz cuadrada única). Jacobiano: con $x_1 = u^{1/2}v^{1/2}$,
$x_2 = u^{1/2}v^{-1/2}$,
$$\frac{\partial(x_1,x_2)}{\partial(u,v)} = \det\begin{pmatrix}
\tfrac12 u^{-1/2}v^{1/2} & \tfrac12 u^{1/2}v^{-1/2}\\[2pt]
\tfrac12 u^{-1/2}v^{-1/2} & -\tfrac12 u^{1/2}v^{-3/2}\end{pmatrix}
= -\tfrac14 v^{-1} - \tfrac14 v^{-1} = -\frac{1}{2v},$$
luego $dx_1dx_2 = \frac{du\,dv}{2v}$; dividiendo por $x_1x_2 = u$ se obtiene la medida
de Haar: $\Phi$ empuja $d^*x_1\,d^*x_2$ a $\tfrac12\,d^*u\,d^*v$. $\square$

**Teorema 3.4 (Mellin doble del núcleo engrosado).** Para todo $(s_1,s_2) \in
\mathbb{C}^2$:
$$\hat h_{g,\varphi}(s_1,s_2)
= \frac{1}{2}\;\hat g\!\left(\frac{s_1+s_2}{2}\right)\,
\hat\varphi\!\left(\frac{s_1-s_2}{2}\right).$$

*Demostración.* Con el Lema 3.3:
$$x_1^{s_1-1}x_2^{s_2-1} = (uv)^{\frac{s_1-1}{2}}\,(u/v)^{\frac{s_2-1}{2}}
= u^{\frac{s_1+s_2}{2}-1}\;v^{\frac{s_1-s_2}{2}},$$
de modo que el integrando completo respecto de $du\,dv$ es
$$g(u)\,\varphi(v)\;u^{\frac{s_1+s_2}{2}-1}\;v^{\frac{s_1-s_2}{2}}\cdot\frac{1}{2v}
= \frac{1}{2}\,g(u)\,u^{\frac{s_1+s_2}{2}-1}\;\varphi(v)\,v^{\frac{s_1-s_2}{2}-1}.$$
**Verificación del exponente de $v$ pedida por el experimento: es exactamente
$v^{(s_1-s_2)/2\,-\,1}$** (el $-1$ proviene del jacobiano $\frac{1}{2v}$). Integrando,
las variables se separan en dos transformadas de Mellin de una variable. $\square$

**Observación 3.5 (la normalización $\hat g(\rho_1+\rho_2-1)$ del enunciado).** El
enunciado del Problema 5.4 esperaba $\hat g(\rho_1+\rho_2-1)$. Las dos formas son la
misma información: poniendo $G(t) := g(t^2)$, la sustitución $u = t^2$ da
$\hat g\bigl(\tfrac{s_1+s_2}{2}\bigr) = 2\,\hat G(s_1+s_2-1)$. Usamos la forma simétrica
$\hat g\bigl(\tfrac{s_1+s_2}{2}\bigr)$ porque tiene la virtud de que **el eje crítico
del objeto doble es el mismo eje $\mathrm{Re} = 1/2$**: si $\rho_1,\rho_2$ están sobre
la línea crítica, $\tfrac{\rho_1+\rho_2}{2}$ también. La versión cruda con $u = x_1x_2$
y $v = x_1$ (Lema 3.1) habría dado $\hat g(s_2)\cdot(\text{divergente})$; el
engrosamiento simétrico es lo que produce la variable suma genuina.

### 3.3. El término de ceros doble: suma de Minkowski con peso espectral

**Corolario 3.6 (lado espectral del funcional diagonal).** Para $h = h_{g,\varphi}$:
$$\mathcal{W}_2(h_{g,\varphi})
= \frac{1}{2}\sum_{\rho_1,\rho_2}
\hat g\!\left(\frac{\rho_1+\rho_2}{2}\right)
\hat\varphi\!\left(\frac{\rho_1-\rho_2}{2}\right),$$
con convergencia absoluta (Lema 2.2(b)).

En el parámetro espectral $z = \rho - \tfrac12$ (autovalor de $H_C$; Doc 96,
Prop. 4.10): $\tfrac{\rho_1+\rho_2}{2} = \tfrac12 + \tfrac{z_1+z_2}{2}$ y
$\tfrac{\rho_1-\rho_2}{2} = \tfrac{z_1-z_2}{2}$, luego
$$\mathcal{W}_2(h_{g,\varphi}) = \frac{1}{2}\sum_{z_1,z_2}
\hat g\!\left(\tfrac12 + \tfrac{z_1+z_2}{2}\right)
\hat\varphi\!\left(\tfrac{z_1-z_2}{2}\right):$$
**$\hat g$ ve la suma de Minkowski de los espectros** $\{z_1+z_2\}$ (reescalada por el
factor inocuo $\tfrac12$) **y $\hat\varphi$ pone un peso espectral en la diferencia**
$z_1 - z_2$, exactamente como anticipó el Problema 5.4.

**Proposición 3.7 (identificación con $H_C\otimes I + I\otimes H_C$).** El flujo de
escala diagonal $U^{(2)}_\lambda h(x_1,x_2) := h(\lambda x_1, \lambda x_2)$ actúa sobre
los núcleos engrosados por $g(u) \mapsto g(\lambda^2 u)$, $\varphi$ invariante; su
generador es $H^{(2)} = H_C\otimes I + I\otimes H_C$ (con $H_C = -ix\partial_x$ en cada
variable), que en coordenadas $(u,v)$ es $2\,H_C^{(u)}\otimes I_v$. Sobre los vectores
espectrales formales $v_{z_1}\otimes v_{z_2}$ (funcionales residuales $\hat h \mapsto
\hat h(\rho_1,\rho_2)$, cf. Doc 98 Obs. 6.3), $H^{(2)}$ tiene autovalor $z_1+z_2$. El
Corolario 3.6 dice que el lado espectral del funcional diagonal es la suma, sobre el
espectro de $H^{(2)}$, de $\hat g$ evaluada en $\tfrac12 + \tfrac{z_1+z_2}{2}$
(equivalentemente: $\hat G$ en $1 + (z_1+z_2)$ con $G(t) = g(t^2)$, Obs. 3.5), con
multiplicidades resueltas por el peso transversal $\hat\varphi\bigl(\tfrac{z_1-z_2}{2}
\bigr)$. **Este es el espectro que la condición 1 del Lema 5.2 exige.** La verificación
de que el bloque tensorial $(Q|_{\mathcal{K}_{\mathrm{off}}})^{\otimes 2}$ aparece con
su signatura completa requiere la estructura cuadrática y se hace en §5. $\square$

**Observación 3.8 (conexión con la correlación de pares de Montgomery).** Si todos los
ceros están sobre la línea ($z_j = i\gamma_j$), el Corolario 3.6 se vuelve
$$\frac{1}{2}\sum_{\gamma_1,\gamma_2} \hat g\!\left(\tfrac12 +
i\tfrac{\gamma_1+\gamma_2}{2}\right)\hat\varphi\!\left(i\tfrac{\gamma_1-\gamma_2}{2}
\right):$$
una forma de **correlación de pares suavizada con ventana**, de la familia estudiada por
Montgomery [Mon73] ($F(\alpha,T)$ es el caso de ventana lorentziana y peso exponencial
puro $\hat\varphi(it) = T^{i\alpha t}$-tipo). No es casual y se explota en §7: la
identidad "lado de ceros doble = lado casi-primo" que este documento establece para el
núcleo engrosado es la generalización con dos funciones de prueba del diccionario
correlación-de-pares ↔ primos de Montgomery y Goldston–Montgomery [GM87].

---

## 4. (iii) El lado aritmético del funcional diagonal: la pregunta decisiva

Evaluamos los nueve bloques del Teorema 2.4 en $h = h_{g,\varphi}$. Notación:
$\sigma := \tfrac{s_1+s_2}{2}$, $\tau := \tfrac{s_1-s_2}{2}$.

### 4.1. Bloques polares y arquimedianos

**(1) Polos×polos.** Por el Teorema 3.4 con $(s_1,s_2) \in \{0,1\}^2$:
$$D{\otimes}D(h_{g,\varphi}) = \tfrac12\Bigl[\hat g(0)\hat\varphi(0)
+ \hat g\bigl(\tfrac12\bigr)\hat\varphi\bigl(-\tfrac12\bigr)
+ \hat g\bigl(\tfrac12\bigr)\hat\varphi\bigl(\tfrac12\bigr)
+ \hat g(1)\hat\varphi(0)\Bigr].$$

**Observación 4.1 (resonancia polo-polo sobre el eje crítico doble).** Los pares mixtos
$(s_1,s_2) = (0,1), (1,0)$ contribuyen en $\sigma = \tfrac12$: **los polos cruzados del
objeto doble caen sobre el mismo eje $\mathrm{Re}\,\sigma = \tfrac12$ donde viven las
sumas de ceros on-line**. En el objeto doble, "polo" y "espectro crítico" dejan de estar
separados por una banda: cualquier análisis de positividad del bloque espectral debe
restar primero esta contribución polar interior, de rango $\leq 2$. Se registra como
rasgo estructural (no es una obstrucción: es rango finito y computable).

**(3)(3') Polos×arquimediano y (6) arquimediano².** Por el Teorema 3.4:
$$D{\otimes}A + A{\otimes}D = \frac{1}{4\pi}\int\Omega(t)\Bigl[
\hat g\bigl(\tfrac14{+}\tfrac{it}{2}\bigr)\hat\varphi\bigl({-}\tfrac14{+}\tfrac{it}{2}\bigr)
+ \hat g\bigl(\tfrac34{+}\tfrac{it}{2}\bigr)\hat\varphi\bigl(\tfrac14{-}\tfrac{it}{2}\bigr)
+ (\text{simétricos en } \tau \mapsto -\tau)\Bigr]dt,$$
$$A{\otimes}A(h_{g,\varphi}) = \frac{1}{8\pi^2}\iint\Omega(t_1)\Omega(t_2)\,
\hat g\bigl(\tfrac12 + i\tfrac{t_1+t_2}{2}\bigr)\,
\hat\varphi\bigl(i\tfrac{t_1-t_2}{2}\bigr)\,dt_1\,dt_2.$$
Integrales absolutamente convergentes de datos explícitos ($\Omega$, $\hat g$,
$\hat\varphi$): **computables sin ceros**.

### 4.2. El bloque primos×primos: la transformada de $\Lambda\star\Lambda$

Evaluamos los cuatro sumandos de $P{\otimes}P$ en $h_{g,\varphi}$. Con
$h(y_1,y_2) = g(y_1y_2)\varphi(y_1/y_2)$:
$$h(n_1,n_2) = g(n_1n_2)\,\varphi(n_1/n_2), \qquad
h(n_1,\tfrac1{n_2}) = g(n_1/n_2)\,\varphi(n_1n_2),$$
$$h(\tfrac1{n_1},n_2) = g(n_2/n_1)\,\varphi\bigl(\tfrac{1}{n_1n_2}\bigr), \qquad
h(\tfrac1{n_1},\tfrac1{n_2}) = g\bigl(\tfrac{1}{n_1n_2}\bigr)\,\varphi(n_2/n_1).$$

**Teorema 4.2 (estructura casi-prima del bloque $P{\otimes}P$).** Sea
$h = h_{g,\varphi}$. Entonces
$$P{\otimes}P(h) = \Sigma_{\mathrm{I}} + \Sigma_{\mathrm{II}} + \Sigma_{\mathrm{III}}
+ \Sigma_{\mathrm{IV}},$$
con:

**(I) Término principal — transformada ponderada de $\Lambda\star\Lambda$:**
$$\Sigma_{\mathrm{I}} = \sum_{n_1,n_2 \geq 2}\Lambda(n_1)\Lambda(n_2)\,
g(n_1n_2)\,\varphi(n_1/n_2)
\;=\; \sum_{N \geq 4} g(N)\;(\Lambda\star_\varphi\Lambda)(N),$$
$$\text{donde}\quad (\Lambda\star_\varphi\Lambda)(N)
:= \sum_{d \mid N}\Lambda(d)\,\Lambda(N/d)\,\varphi\!\left(\frac{d^2}{N}\right).$$
El soporte de $\Sigma_{\mathrm{I}}$ es el semigrupo de **casi-primos**
$\{p_1^{k_1}p_2^{k_2}\}$ (enteros con a lo sumo dos factores primos distintos),
intersecado con $\mathrm{supp}\,g$, y con la restricción de excentricidad
$d^2/N \in \mathrm{supp}\,\varphi$.

**(II)–(IV) Términos de soporte finito (con $g$ y $\varphi$ intercambiados):**
$$\Sigma_{\mathrm{II}} = \sum_{n_1,n_2}\frac{\Lambda(n_1)\Lambda(n_2)}{n_2}\,
g(n_1/n_2)\,\varphi(n_1n_2), \quad
\Sigma_{\mathrm{III}} = \sum_{n_1,n_2}\frac{\Lambda(n_1)\Lambda(n_2)}{n_1}\,
g(n_2/n_1)\,\varphi\!\bigl(\tfrac{1}{n_1n_2}\bigr),$$
$$\Sigma_{\mathrm{IV}} = \sum_{n_1,n_2}\frac{\Lambda(n_1)\Lambda(n_2)}{n_1n_2}\,
g\!\bigl(\tfrac{1}{n_1n_2}\bigr)\,\varphi(n_2/n_1).$$
En cada uno, la variable $n_1n_2$ (o su inversa) está confinada al soporte compacto de
$\varphi$ (resp. $g$): solo finitamente muchos pares $(n_1,n_2)$ contribuyen, con cotas
de corte explícitas $n_1n_2 \leq \max(\mathrm{supp})$.

Todos los coeficientes son aritméticos explícitos ($\Lambda$, pesos racionales);
**ninguno requiere posiciones de ceros**.

*Demostración.* Sustitución directa de las cuatro evaluaciones de $h$ en la fórmula del
bloque (4) de §2.3. Para (I): agrupar por $N = n_1n_2$; la pareja $(n_1,n_2)$ con
$n_1n_2 = N$ y $\Lambda(n_1)\Lambda(n_2) \neq 0$ recorre los divisores $d = n_1$ de $N$
que son potencias de primos con cofactor potencia de primo, y $\Lambda(d)\Lambda(N/d) =
0$ en caso contrario, luego la suma interior es exactamente $\sum_{d\mid N}\Lambda(d)
\Lambda(N/d)\varphi(d^2/N)$ con $n_1/n_2 = d/(N/d) = d^2/N$. El soporte casi-primo:
$\Lambda(d)\Lambda(N/d) \neq 0$ exige $d = p_1^{k_1}$, $N/d = p_2^{k_2}$. La finitud en
(II)–(IV): p.ej. en (II), $\varphi(n_1n_2) \neq 0$ exige $n_1n_2 \in
\mathrm{supp}\,\varphi$ compacto, y solo hay finitos enteros $\geq 4$ en un compacto.
$\square$

### 4.3. Bloques polos×primos

**Proposición 4.3.** Con $M_0(y) := \int_0^\infty g(t)\,\varphi(y^2/t)\,\tfrac{dt}{t}$ y
$M_1(y) := \tfrac1y\int_0^\infty g(t)\,\varphi(y^2/t)\,dt$ (convoluciones
multiplicativas explícitas de $g$ y $\varphi$, suaves de soporte compacto en $y$):
$$D{\otimes}P(h_{g,\varphi}) + P{\otimes}D(h_{g,\varphi})
= \sum_n \Lambda(n)\Bigl[c_0(n) + c_1(n) + n^{-1}c_0(1/n) + n^{-1}c_1(1/n)
+ (\text{simétricos})\Bigr],$$
donde $c_0(y) = \hat h_1(0;y) = \int h(x_1,y)\tfrac{dx_1}{x_1}$ y $c_1(y) =
\hat h_1(1;y) = \int h(x_1,y)\,dx_1$ se computan en forma cerrada: con $t = x_1y$,
$$c_0(y) = \int_0^\infty g(x_1y)\,\varphi(x_1/y)\,\frac{dx_1}{x_1}
= \int_0^\infty g(t)\,\varphi(t/y^2)\,\frac{dt}{t},
\qquad c_1(y) = \frac{1}{y}\int_0^\infty g(t)\,\varphi(t/y^2)\,dt.$$
(Las $c_i$ y $M_i$ difieren por $\varphi \mapsto \check\varphi(v) := \varphi(1/v)$;
ambas son convoluciones multiplicativas de datos de prueba.) Suma finita sobre $n$
(soporte compacto en $y = n$ o $1/n$): **computable sin ceros**. $\square$

### 4.4. Los términos mixtos ceros×primos: reabsorción (el punto que decide)

Planteamos el riesgo con precisión. En la presentación semi-expandida del funcional
doble (aplicar la fórmula explícita SOLO en la variable 2), se obtiene
$$\mathcal{W}_2(h) = \sum_{\rho_2}\,\mathcal{W}^{(1)}\bigl[x_1 \mapsto
\hat h_2'(x_1;\rho_2)\bigr]
\quad\leadsto\quad \text{términos } -\sum_{\rho_2}\sum_n \Lambda(n)\,
\bigl[\cdots(\rho_2, n)\cdots\bigr],$$
que mezclan un cero con un primo. Para el núcleo engrosado, explícitamente: la Mellin
parcial en la variable 2 es
$$\hat h_2'(x_1;s) := \int_0^\infty g(x_1x_2)\,\varphi(x_1/x_2)\,x_2^{s-1}\,dx_2
\;\overset{t = x_1x_2}{=}\; x_1^{-s}\int_0^\infty g(t)\,\varphi(x_1^2/t)\,t^{s-1}\,dt,$$
de modo que el término mixto ceros×primos de esa presentación es
$$-\sum_{\rho_2}\sum_n \Lambda(n)\Bigl[n^{-\rho_2}\,J_{\rho_2}(n)
+ n^{\rho_2-1}\,J_{\rho_2}(1/n)\Bigr], \qquad
J_s(y) := \int g(t)\,\varphi(y^2/t)\,t^{s-1}dt.$$
Las potencias $n^{-\rho_2}$ **sí** involucran posiciones de ceros: si este término fuera
irreducible, MW-7 reaparecería exactamente aquí.

**Teorema 4.4 (reabsorción de los términos mixtos).** Para todo $h \in
C_c^\infty((\mathbb{R}_+^*)^2)$ — en particular para $h_{g,\varphi}$ — los términos
mixtos de cualquier presentación semi-expandida se reabsorben: la suma sobre $\rho_2$
a $n$ fijo es, por la fórmula de una variable aplicada a la función de prueba
$x_2 \mapsto h(n, x_2)$ (resp. $h(1/n, x_2)$), igual a
$$\sum_{\rho_2} n^{-\rho_2} J_{\rho_2}(n) = \sum_{\rho_2}\widehat{h(n,\cdot)}(\rho_2)
= (D - P - A)\bigl[h(n,\cdot)\bigr],$$
que es un dato aritmético puro (Definición 1.3 aplicada a la rebanada). Sumando sobre
$n$ con pesos $\Lambda(n)$ se recuperan exactamente los bloques $P{\otimes}D$,
$P{\otimes}P$, $P{\otimes}A$ del Teorema 2.4. En consecuencia:

**(1)** los términos mixtos SÍ se reabsorben — no en el lado espectral, sino en el
aritmético: son la presentación a medio expandir de bloques
aritmética×aritmética;

**(2)** el funcional completo $\mathcal{W}_2(h_{g,\varphi})$ es computable sin
posiciones de ceros (Teorema 2.4 + Teorema 4.2 + Proposición 4.3 + §4.1);

**(3)** no queda ningún término irreducible mixto. **MW-7 no reaparece en el
funcional diagonal engrosado.**

*Demostración.* La rebanada $x_2 \mapsto h(n,x_2)$ está en
$C_c^\infty(\mathbb{R}_+^*)$ para cada $n$ fijo (restricción de una función
$C_c^\infty$ de dos variables a una recta coordenada), y su Mellin es
$\widehat{h(n,\cdot)}(s) = n^{-s}J_s(n)$ por el cálculo anterior (con $y = n$). El
Teorema 1.4 aplicado a esa rebanada da la identidad mostrada, término a término en $n$;
la suma sobre $n$ es finita (soporte compacto). La identificación con los bloques del
Teorema 2.4 es la definición iterada (Lema 2.2). $\square$

### 4.5. Delimitación honesta: dónde reaparecería MW-7

El Teorema 4.4 no es un truco: es la observación de que el objeto $\mathcal{W}_2 =
\mathcal{W}\otimes\mathcal{W}$ hereda **dos** presentaciones (espectral y aritmética)
de cada factor, y por tanto tiene presentación totalmente aritmética. Pero hay un
enunciado vecino, más fuerte, que sigue siendo falso/inaccesible, y conviene
delimitarlo para que el veredicto no se malinterprete:

**Observación 4.5 (la fórmula explícita "propia" del objeto doble no existe como
objeto de una variable).** El lado espectral del Corolario 3.6 puede reescribirse como
suma sobre la variable suma sola:
$$\mathcal{W}_2(h_{g,\varphi}) = \frac12\sum_{\sigma \in S}
\hat g\bigl(\tfrac12+\sigma\bigr)\,w_\varphi(\sigma), \qquad
S := \Bigl\{\tfrac{z_1+z_2}{2}\Bigr\}, \quad
w_\varphi(\sigma) := \sum_{\substack{(z_1,z_2):\\ z_1+z_2 = 2\sigma}}
\hat\varphi\bigl(\tfrac{z_1-z_2}{2}\bigr).$$
Una "fórmula explícita propia" del objeto doble — análoga a la de una función L, con
espectro $S$ y multiplicidades — requeriría conocer la **función de multiplicidad**
$w_\varphi(\sigma)$, que depende de las posiciones relativas de los ceros: ahí
reaparecería MW-7 (es la versión cuantitativa del GAP ABIERTO 3.8 del Doc 106: el
objeto suma-de-Minkowski no es una función L). **El punto del experimento es que el
Lema 5.2 no necesita ese enunciado**: pide un funcional $\mathcal{W}_2$ con (1) bloque
espectral tensorial y (2) lado aritmético autónomo — y ambos existen sin resolver
$w_\varphi$. La multiplicidad no se computa: se **transporta** (las dos presentaciones
del Teorema 2.4 son iguales como números, no término a término).

**Respuestas explícitas a (iii):**
(a) ¿Computable sin posiciones de ceros? **Sí** (Teorema 4.4(2)).
(b) ¿Vive en el semigrupo casi-primo con coeficientes explícitos? **Sí**: el bloque
dominante es $\sum_N g(N)(\Lambda\star_\varphi\Lambda)(N)$, una transformada ponderada
de $\Lambda\star\Lambda$ — exactamente el segundo término de la función de von Mangoldt
de segundo orden de Selberg $\Lambda_2(N) = \Lambda(N)\log N + (\Lambda\star\Lambda)(N)$
[Sel49]. Diferencia precisa con $\Lambda_2$: el funcional diagonal pesa cada
factorización $N = d\cdot(N/d)$ con $\varphi(d^2/N)$ (localización en la
*excentricidad* de la factorización), mientras $\Lambda_2$ suma con peso 1; el término
$\Lambda(N)\log N$ de $\Lambda_2$ (que detecta potencias de primos puras) no aparece en
$\Sigma_{\mathrm{I}}$ — su análogo es el sector diagonal $n_1 = n_2$ ($\varphi$
evaluada en 1) ya incluido en la suma. Nótese que $\Lambda_2 = \mu \star \log^2$
[Sel49]: el bloque casi-primo está, como $\Lambda_2$, a distancia de convolución finita
de funciones completamente elementales.
(c) Términos mixtos: **opción (1)+(2) simultáneamente** — se reabsorben en el lado
aritmético y el total es computable sin ceros (Teorema 4.4); la opción (3) (MW-7) queda
confinada al enunciado vecino de la Observación 4.5, que el Lema 5.2 no requiere.

---

## 5. (iv) Estructura de forma cuadrática: el bloque tensorial del cuádruplo

### 5.1. La forma cuadrática diagonal $Q_2$

**Definición 5.1.** Sobre $C_c^\infty((\mathbb{R}_+^*)^2)$, con la convolución
multiplicativa $(h_1\star h_2)(x) = \int_{(\mathbb{R}_+^*)^2} h_1(y)\,h_2(x/y)\,d^*y$
($d^*y = \frac{dy_1dy_2}{y_1y_2}$, cocientes componente a componente) y la involución
$\tilde h(x_1,x_2) := \overline{h(1/x_1,1/x_2)}\,(x_1x_2)^{-1}$:
$$Q_2(h_1,h_2) := \mathcal{W}_2(h_1 \star \tilde h_2).$$
Es el análogo exacto de $Q(f,g) = \mathcal{W}(f\star\tilde g)$ de P35 (Def. weil).

**Lema 5.2 (cierre de la clase engrosada y lado espectral de $Q_2$).**

(a) En coordenadas $(u,v) = \Phi(x_1,x_2)$ del Lema 3.3, los núcleos engrosados son
exactamente las funciones producto $g(u)\varphi(v)$; como $\Phi$ es isomorfismo de
grupos, la clase engrosada es cerrada bajo $\star$ y bajo $\widetilde{(\cdot)}$:
$$h_{g_1,\varphi_1} \star h_{g_2,\varphi_2} = \tfrac12\, h_{\,g_1\star g_2,\;
\varphi_1\star\varphi_2}, \qquad
\widetilde{h_{g,\varphi}} = h_{\,\tilde g,\;\varphi^\vee}, \quad
\varphi^\vee(v) := \overline{\varphi(1/v)},$$
(el peso $u^{-1} = (x_1x_2)^{-1}$ de la involución cae íntegramente en el factor $g$;
$\widehat{\varphi^\vee}(\tau) = \overline{\hat\varphi(-\bar\tau)}$).

(b) Mellin de la involución doble: $\widehat{\tilde h}(s_1,s_2) =
\overline{\hat h(1-\bar s_1,\,1-\bar s_2)}$. En consecuencia, el lado espectral de la
forma es
$$Q_2(h,h) = \sum_{\rho_1,\rho_2} \hat h(\rho_1,\rho_2)\;
\overline{\hat h\bigl(1-\bar\rho_1,\,1-\bar\rho_2\bigr)},$$
suma absolutamente convergente, hermitiana porque el conjunto de ceros es estable bajo
$\rho \mapsto 1-\bar\rho$ (ecuación funcional + reflexión de Schwarz).

*Demostración.* (a) Cálculo directo: $u(1/x_1,1/x_2) = 1/u$, $v(1/x_1,1/x_2) = 1/v$ y
$(x_1x_2)^{-1} = u^{-1}$, luego $\tilde h$ corresponde a
$\overline{g(1/u)}u^{-1}\cdot\overline{\varphi(1/v)} = \tilde g(u)\varphi^\vee(v)$. El
factor $\tfrac12$ de la convolución es el empuje de Haar del Lema 3.3. (b) Con
$y_i = 1/x_i$: $x_i^{s_i-1}dx_i = y_i^{-s_i}\,dy_i\cdot y_i^{\,0}$ tras
$dx_i = dy_i/y_i^2$, da $\widehat{\tilde h}(s) = \overline{\int h(y)\,
y_1^{-\bar s_1}y_2^{-\bar s_2}\,dy} = \overline{\hat h(1-\bar s_1, 1-\bar s_2)}$.
Entonces $\widehat{h\star\tilde h} = \hat h\cdot\widehat{\tilde h}$ y se aplica el
Lema 2.2(b). Consistencia con (a): $\sigma(1-\bar s_1, 1-\bar s_2) = 1 - \bar\sigma$,
$\tau \mapsto -\bar\tau$, que es exactamente $(\widehat{\tilde g},
\widehat{\varphi^\vee})$. $\square$

**Observación 5.3 (positividad bajo RH y los dos lados).** Si todos los ceros cumplen
$\rho = 1-\bar\rho$ (RH), el apareamiento del Lema 5.2(b) es diagonal y
$Q_2(h,h) = \sum |\hat h(\rho_1,\rho_2)|^2 \geq 0$. El funcional $Q_2(h,h)$ tiene
además presentación aritmética (Teorema 2.4 aplicado a $h\star\tilde h$, que sigue en
la clase engrosada por (a)): la igualdad de ambas presentaciones es la versión
cuadrática del diccionario de §4.

### 5.2. El modelo de juguete: los 16 pares del cuádruplo

Sea ahora la configuración del Doc 98: ceros off-críticos exactamente
$\{1/2\pm\delta\pm i\gamma_0\}$, simples; en parámetro $z = \rho-\tfrac12$:
$$z_1 = \delta+i\gamma_0,\quad \bar z_1 = \delta-i\gamma_0,\quad
z_2 = -\delta+i\gamma_0,\quad \bar z_2 = -\delta-i\gamma_0.$$
Los 16 vectores espectrales del bloque doble off×off son $v_{ij} := v_{z_i}\otimes
v_{z_j}$, funcionales $h \mapsto \hat h(\rho_i,\rho_j)$. Sobre la clase engrosada,
$\hat h(\rho_i,\rho_j) = \tfrac12\,\hat g(\tfrac12+\sigma_{ij})\,
\hat\varphi(\tau_{ij})$ con $\sigma_{ij} = \tfrac{z_i+z_j}{2}$,
$\tau_{ij} = \tfrac{z_i-z_j}{2}$.

**Enumeración completa (tarea (iv)).** Los valores $(\sigma,\tau)$ de los 16 pares
ordenados — equivalentemente $\rho_i+\rho_j-1 = 2\sigma$, que recorre
$\{\pm2\delta\pm2i\gamma_0,\ \pm2\delta,\ \pm2i\gamma_0,\ 0\}$ como pedía el enunciado:

| # | par $(z_i,z_j)$ | $\sigma = \frac{z_i+z_j}{2}$ | $\tau = \frac{z_i-z_j}{2}$ | tipo de suma |
|---|---|---|---|---|
| 1 | $(z_1,z_1)$ | $\delta+i\gamma_0$ | $0$ | off plena |
| 2 | $(\bar z_1,\bar z_1)$ | $\delta-i\gamma_0$ | $0$ | off plena |
| 3 | $(z_2,z_2)$ | $-\delta+i\gamma_0$ | $0$ | off plena |
| 4 | $(\bar z_2,\bar z_2)$ | $-\delta-i\gamma_0$ | $0$ | off plena |
| 5 | $(z_1,\bar z_1)$ | $\delta$ | $i\gamma_0$ | **real** $+2\delta$ |
| 6 | $(\bar z_1,z_1)$ | $\delta$ | $-i\gamma_0$ | **real** $+2\delta$ |
| 7 | $(z_2,\bar z_2)$ | $-\delta$ | $i\gamma_0$ | **real** $-2\delta$ |
| 8 | $(\bar z_2,z_2)$ | $-\delta$ | $-i\gamma_0$ | **real** $-2\delta$ |
| 9 | $(z_1,z_2)$ | $i\gamma_0$ | $\delta$ | imaginaria |
| 10 | $(z_2,z_1)$ | $i\gamma_0$ | $-\delta$ | imaginaria |
| 11 | $(\bar z_1,\bar z_2)$ | $-i\gamma_0$ | $\delta$ | imaginaria |
| 12 | $(\bar z_2,\bar z_1)$ | $-i\gamma_0$ | $-\delta$ | imaginaria |
| 13 | $(z_1,\bar z_2)$ | $0$ | $z_1$ | nula |
| 14 | $(\bar z_2,z_1)$ | $0$ | $-z_1$ | nula |
| 15 | $(\bar z_1,z_2)$ | $0$ | $\bar z_1$ | nula |
| 16 | $(z_2,\bar z_1)$ | $0$ | $-\bar z_1$ | nula |

El mapa $(z_i,z_j) \mapsto (\sigma,\tau)$ es biyectivo lineal: los 16 puntos
$(\sigma_{ij},\tau_{ij}) \in \mathbb{C}^2$ son **distintos** (aunque los $\sigma$ solos
se repiten: $\sigma = 0$ cuatro veces, $\sigma = \pm\delta, \pm i\gamma_0$ dos veces
cada uno — la degeneración que $\hat\varphi$ resuelve).

**Qué ve $\hat g$ en cada clase (pregunta del enunciado):** en las sumas off plenas,
puntos genuinamente fuera del eje doble ($\mathrm{Re}\,\sigma = \pm\delta$,
$\mathrm{Im}\,\sigma = \pm\gamma_0$); en las sumas **reales** $\pm2\delta$, los puntos
$\tfrac12 \pm \delta$ **del eje real** — el detector directo del desplazamiento
$\delta$, sin frecuencia; en las sumas imaginarias y nulas, puntos **sobre el eje
crítico doble** $\tfrac12 \pm i\gamma_0$ y $\tfrac12$: para $\hat g$ son
indistinguibles de sumas de ceros on-line — ahí la off-criticidad es invisible para
$\hat g$ y solo $\hat\varphi(\tau)$ con $\mathrm{Re}\,\tau \neq 0$ la registra
(filas 9–16: $\tau \in \{\pm\delta, \pm z_1, \pm\bar z_1\}$, todas con parte real
$\pm\delta \neq 0$).

### 5.3. La matriz de Gram del bloque: 8 planos hiperbólicos

**Lema 5.4 (independencia de las 16 evaluaciones sobre la clase engrosada).** Los 16
funcionales $h_{g,\varphi} \mapsto \hat g(\tfrac12+\sigma_{ij})\,
\hat\varphi(\tau_{ij})$ son linealmente independientes sobre el span (combinaciones
lineales finitas) de núcleos engrosados; equivalentemente, el mapa de evaluación
$\mathrm{ev}: \mathrm{span}\{h_{g,\varphi}\} \to \mathbb{C}^{16}$,
$h \mapsto (\hat h(\rho_i,\rho_j))_{ij}$, es **sobreyectivo**.

*Demostración.* Supóngase $\sum_{ij} c_{ij}\,\hat g(\tfrac12+\sigma_{ij})
\hat\varphi(\tau_{ij}) = 0$ para todos $g,\varphi \in C_c^\infty(\mathbb{R}_+^*)$.
Paso 1 (separar por $\sigma$): tómese $g = g_{c,\epsilon}$ una aproximación suave de la
delta multiplicativa en $x = e^c$; entonces $\hat g(\tfrac12+\sigma) \to
e^{c(\sigma-1/2)}\cdot e^{c}\,(1+o(1))$ — más precisamente, $\hat g_{c,\epsilon}
(\tfrac12+\sigma) = e^{c(\sigma+1/2)}(1+O_\sigma(\epsilon))$ — de modo que la condición
implica, para todo $c \in \mathbb{R}$ y todo $\varphi$:
$\sum_{\sigma \in \Sigma} e^{c\sigma}\,\bigl[\sum_{ij:\,\sigma_{ij}=\sigma}
c_{ij}\hat\varphi(\tau_{ij})\bigr] = 0$, donde $\Sigma$ es el conjunto de los 9 valores
distintos de $\sigma$. Las funciones $c \mapsto e^{c\sigma}$ con $\sigma$ distintos son
linealmente independientes sobre $\mathbb{R}$ (independencia de caracteres de Artin, o
wronskiano de Vandermonde), luego cada corchete se anula. Paso 2 (separar por $\tau$
dentro de cada grupo): dentro de cada valor de $\sigma$, los $\tau_{ij}$ son distintos
(tabla §5.2), y el mismo argumento con $\hat\varphi$ y deltas aproximadas en $e^{d}$ da
$c_{ij} = 0$. La sobreyectividad de $\mathrm{ev}$ es la afirmación dual en dimensión
finita. $\square$

**Teorema 5.5 (signatura del bloque doble del cuádruplo: $(8,8)$).** Sea $B$ la forma
hermitiana inducida por $Q_2$ sobre $\mathbb{C}^{16} = \mathrm{ev}(\mathrm{span}\,
\{h_{g,\varphi}\})$ vía la contribución del bloque off×off del lado espectral
(Lema 5.2(b)), es decir, para $a = (a_{ij}) = \mathrm{ev}(h)$:
$$B(a,a) = \sum_{i,j} a_{ij}\,\overline{a_{i^*j^*}}, \qquad
\text{donde } z_{i^*} := -\bar z_i \;\;(\text{i.e. } \rho_{i^*} = 1-\bar\rho_i).$$
Entonces:

(a) La involución $(i,j) \mapsto (i^*,j^*)$ es **libre de puntos fijos** sobre los 16
pares (un punto fijo exigiría $z_i, z_j \in i\mathbb{R}$, imposible con
$\mathrm{Re}\,z = \pm\delta \neq 0$), y los aparea en exactamente **8 órbitas**:
$$\{1,3\},\;\{2,4\},\;\{5,7\},\;\{6,8\},\;\{9,10\},\;\{11,12\},\;\{13,16\},\;
\{14,15\}$$
(numeración de la tabla §5.2; se verifica con $z_1^* = z_2$, $\bar z_1^{\,*} =
\bar z_2$ y viceversa).

(b) Sobre cada órbita $\{(ij),(i^*j^*)\}$, $B$ restringe al plano hiperbólico
$a\,\bar b + b\,\bar a$: signatura $(1,1)$.

(c) Por tanto
$$\boxed{\;\mathrm{sig}(B) = (8,8), \qquad \mathrm{neg.ind}(B) = 8
= \frac{(4m)^2}{2}\Big|_{m=1},\;}$$
**exactamente la predicción de la Proposición 3.5 del Doc 106** para
$(Q|_{\mathcal{K}_{\mathrm{off}}})^{\otimes 2}$ con $\mathrm{sig}(2,2)^{\otimes 2}
= (2\cdot2+2\cdot2,\;2\cdot2+2\cdot2)$.

(d) El peso $\hat\varphi$ **no rompe ni degenera** la signatura: por el Lema 5.4 el
mapa de evaluación es sobreyectivo, luego $B$ se realiza con su rango completo 16 sobre
la clase engrosada. Más aún, $\hat\varphi$ es **necesario** para la no-degeneración:
las órbitas $\{9,10\}$, $\{11,12\}$, $\{13,16\}$, $\{14,15\}$ viven dentro de
autoespacios degenerados de la variable suma ($\sigma$ idéntico para ambos miembros, o
$\sigma = 0$ compartido por cuatro vectores); un funcional que solo viera $\hat g$
(olvidando $\varphi$) colapsaría esas direcciones y perdería 4 de los 8 negativos.

*Demostración.* (a) Cálculo directo con la tabla: p.ej. $(z_1,z_1)^* = (z_2,z_2)$
(órbita $\{1,3\}$); $(z_1,\bar z_1)^* = (-\bar z_1, -z_1)\,\hat=\,(z_2,\bar z_2)$
(órbita $\{5,7\}$, pues $-\bar z_1 = z_2$ y $-z_1 = \bar z_2$); $(z_1,z_2)^* =
(z_2,z_1)$ (órbita $\{9,10\}$); $(z_1,\bar z_2)^* = (z_2,\bar z_1)$ (órbita
$\{13,16\}$); $(\bar z_2, z_1)^* = (\bar z_1, z_2)$ (órbita $\{14,15\}$); las restantes
por conjugación. Punto fijo: $(i^*,j^*) = (i,j)$ exige $z_i = -\bar z_i$, i.e.
$\mathrm{Re}\,z_i = 0$: excluido. (b) En la base de la órbita, $B = \bigl(
\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$ (los pesos son 1: ceros simples,
multiplicidad 1 en la suma espectral), autovalores $\pm1$. (c) Suma ortogonal de 8
planos $(1,1)$. (d) Lema 5.4 y la tabla. $\square$

**Corolario 5.6 (localización del índice negativo — respuesta a la pregunta central de
(iv)).** La distribución de los 8 negativos por tipo de suma $\rho_i+\rho_j-1 =
2\sigma$:

| tipo de suma | órbitas | negativos |
|---|---|---|
| off plena ($\pm2\delta\pm2i\gamma_0$) | $\{1,3\},\{2,4\}$ | $2$ |
| **real** ($\pm2\delta$) | $\{5,7\},\{6,8\}$ | $2$ |
| imaginaria ($\pm2i\gamma_0$) | $\{9,10\},\{11,12\}$ | $2$ |
| nula ($0$) | $\{13,16\},\{14,15\}$ | $2$ |

**La conjetura del enunciado ("las contribuciones con $\rho_i+\rho_j-1 = \pm2\delta$
son las que llevan el índice negativo") es FALSA de modo instructivo**: las sumas
reales llevan solo $2$ de los $8$ negativos. La mitad del índice negativo ($4$) vive en
sumas **puramente imaginarias o nulas** — es decir, $\hat g$ las ve sobre el eje
crítico doble, indistinguibles de pares on-line, y la off-criticidad está almacenada
exclusivamente en la variable de diferencia $\tau$ con $\mathrm{Re}\,\tau = \pm\delta$,
visible solo para $\hat\varphi$. Lección estructural: **en el objeto doble, la variable
transversal $\varphi$ no es un mero regularizador del engrosamiento — es portadora de
la mitad del índice**. Cualquier intento de colapsar $\varphi$ (p.ej. tomar
$\hat\varphi \to 1$, des-engrosar) no solo diverge (Lema 3.1): pierde la mitad de la
señal espectral negativa.

**Observación 5.7 (caveats declarados del Teorema 5.5).** (i) El enunciado es sobre la
forma $B$ inducida por el **bloque off×off del lado espectral** de $Q_2$ sobre el
cociente de evaluación — el análogo doblado de la localización
$\mathcal{K} = \mathcal{K}_{\mathrm{crit}}\oplus_Q\mathcal{K}_{\mathrm{off}}$ (Doc 96,
Teorema 8.1) no se re-demuestra aquí para el objeto doble; la separación del bloque
respecto del resto del espectro doble usa el mismo argumento de proyección espectral de
$H^{(2)}$ y queda como estructura heredada módulo V.1-doblado (mismo estatus que en
Doc 98 §6, GAP G4/G5 allí declarados). (ii) Los pesos de los planos son 1 por ceros
simples (hipótesis T1 del juguete); con multiplicidades, los pesos son
$m_{\rho_i}m_{\rho_j} > 0$ y la signatura no cambia. (iii) La identificación de $B$
con la matriz de Gram de $(Q|_{\mathcal{K}_{\mathrm{off}}})^{\otimes 2}$ usa la
convención de apareamiento $z \leftrightarrow -\bar z$ ($\rho \leftrightarrow
1-\bar\rho$), que es la que la involución $\tilde h$ de la Definición 5.1 produce; el
Doc 98 (Obs. 6.2) ya registró que ambas convenciones dan dos planos hiperbólicos por
cuádruplo en una variable — aquí la convención queda **fijada por el cálculo del
Lema 5.2(b)**, lo que de paso responde el GAP G5 del Doc 98 para la forma doble: la
involución natural de $Q_2$ aparea $\rho \leftrightarrow 1-\bar\rho$.

---

## 6. (v) Balance contra los Lemas Faltantes 5.2 y 5.3 del Doc 106

### 6.1. Lema 5.2, condición 1 (bloque espectral tensorial): SATISFECHA

El candidato es
$$X_2 := \Bigl(\,\mathcal{W}_2\ \text{restringido a la clase engrosada}\
\{h_{g,\varphi}\},\ \ Q_2(h,h') = \mathcal{W}_2(h\star\tilde h')\,\Bigr).$$
Por el Corolario 3.6 y la Proposición 3.7, su lado espectral está indexado por los
autovalores $z_1+z_2$ de $H_C\otimes I + I\otimes H_C$; por el Teorema 5.5, en el
modelo de juguete el bloque off×off es exactamente
$(Q|_{\mathcal{K}_{\mathrm{off}}})^{\otimes 2}$ con signatura $(8,8)$ y sin
degeneración. La condición 1 del Lema Faltante 5.2 se verifica (módulo la herencia
estructural declarada en la Obs. 5.7(i)).

### 6.2. Lema 5.2, condición 2 (lado aritmético autónomo): SATISFECHA

Por el Teorema 4.4: $\mathcal{W}_2(h_{g,\varphi})$ — y por el Lema 5.2(a) también
$Q_2(h,h)$, pues $h\star\tilde h$ sigue siendo engrosado — tiene presentación
íntegramente aritmética: polos (§4.1), casi-primos con coeficientes
$\Lambda(d)\Lambda(N/d)\varphi(d^2/N)$ (Teorema 4.2), convoluciones polo-primo
(Prop. 4.3) y términos arquimedianos explícitos. Sin posiciones de ceros. **El Lema
Faltante 5.2 tiene candidato.** Este era el resultado binario que el Problema 5.4 pedía.

### 6.3. La advertencia estructural: el índice del objeto doble completo es infinito

Antes de declarar la victoria parcial, lo que el candidato NO da. La clase engrosada,
vía $\Phi$, es densa en $C_c^\infty((\mathbb{R}_+^*)^2)$ (las sumas
$\sum g_\alpha(u)\varphi_\alpha(v)$ aproximan cualquier función de prueba de dos
variables en la topología de Schwartz sobre compactos). Por tanto $Q_2$ es la forma
$Q\otimes Q$ sobre (un denso de) $\mathcal{K}\otimes\mathcal{K}$ completo, y la
Proposición 3.4 del Doc 106 aplica:

**Proposición 6.1 (el índice global de $Q_2$ es $0$ o $\infty$).** Bajo RH,
$Q_2 \geq 0$ (Obs. 5.3). Bajo ¬RH (juguete), $\kappa(Q_2) = \infty$: los pares mixtos
off×on $(\rho_{\mathrm{off}}, \tfrac12+i\gamma_j)$, $j \geq 1$, forman para cada cero
on-line una familia de 4 vectores espectrales con la misma involución libre de puntos
fijos en la primera componente ($(z_i, i\gamma_j)^* = (z_{i^*}, i\gamma_j)$), i.e. 2
planos hiperbólicos por cada $\gamma_j$: infinitos negativos.

*Demostración.* Idéntica al Teorema 5.5(a)(b) con $z_j = i\gamma_j$ fijo en la segunda
ranura: la involución actúa solo en la primera, sin puntos fijos porque
$\mathrm{Re}\,z_i = \pm\delta \neq 0$; cada órbita $\{(z_i,i\gamma_j),
(z_{i^*},i\gamma_j)\}$ es un plano hiperbólico. La independencia de las evaluaciones
para cualquier subfamilia finita es el Lema 5.4 (los puntos $(\sigma,\tau)$ siguen
siendo distintos). $\square$

**Consecuencia.** El invariante útil para la amplificación NO es $\kappa(Q_2)$ global
(que es $0/\infty$, binario) sino el **índice del bloque relativo off×off** — finito,
igual a $8 = (4m)^2/2$ — exactamente la regularización (R2) del Doc 106 §3.1.3. Esto
es consistente con el diseño del Candidato 2 (tensor relativo), pero significa que el
Lema 5.3 (cota) debe acotar el índice **del bloque**, y el lado aritmético es un
funcional global que no viene pre-localizado. La brecha entre "funcional aritmético
global computable" y "cota del índice de un bloque espectral" es donde vive ahora toda
la dificultad.

### 6.4. Lema 5.3: ¿hay fuente de finitud no espectral en el lado casi-primo?

Esta es la pregunta del análogo de la racionalidad de Deligne. Tres observaciones, en
orden de honestidad creciente.

**(α) Existe por primera vez un candidato a segunda fuente que pasa I2a.** El lado
casi-primo $\sum_N g(N)(\Lambda\star_\varphi\Lambda)(N)$ admite **cotas superiores
incondicionales de criba**: para el problema modelo (correlaciones
$\sum_{n\leq x}\Lambda(n)\Lambda(n+h)$, y igualmente para sumas cortas ponderadas de
$\Lambda\star\Lambda$) el método de Selberg da cotas superiores del orden de magnitud
correcto con constante absoluta [HR74, Cap. 3; el valor de la constante no es
load-bearing aquí]. El problema de paridad de las cribas — el muro del Arc A — bloquea
las **asintóticas** y las cotas **inferiores** no triviales, pero NO las cotas
superiores. Y lo que el esqueleto de Deligne necesita (Doc 106, Teorema 1.4(b)) es una
COTA, no una asintótica. Es la primera vez en el programa que aparece un input
incondicional, independiente de los ceros, del lado correcto de la desigualdad, que no
es una positividad CAP: una cota de criba es un conteo mayorado, no una forma cuadrática
no negativa. El patrón de transmutación del Doc 99 no aplica de forma automática.

**(β) El gap real: el puente criba→índice.** Una cota superior
$|P{\otimes}P(h\star\tilde h)| \leq C(\mathrm{supp})\cdot\|\cdot\|$ del bloque
casi-primo NO acota por sí sola $\mathrm{neg.ind}$ de un bloque espectral: el índice
negativo es una propiedad de rango/inercia, no de tamaño. El mecanismo que convierte
cotas del lado aritmético en cotas de índice existe en el corpus — es la condición C5
del Doc 94 (el defecto de positividad está concentrado en una "cabeza" finita
controlada) — pero su instancia para $Q_2$ no está probada. Lo que falta exactamente
se enuncia como Lema 7.2 abajo.

**(γ) El riesgo de transmutación, localizado.** Si el puente (β) exigiera no una cota
sino la **asintótica** del funcional casi-primo uniforme en $(g,\varphi)$ — p.ej. para
separar el bloque off×off de la cola on×on dentro del funcional global —, entonces el
input requerido es exactamente la asintótica de correlaciones de
$\Lambda\star\Lambda$, que por el diccionario de Montgomery / Goldston–Montgomery
[Mon73; GM87] es inter-derivable con la correlación de pares de los ceros y de fuerza
tipo Hardy–Littlewood (primos gemelos generalizados). Nótese con precisión qué muro es
ese: **no es CAP** (no es una positividad RH-equivalente; la correlación de pares no
implica RH ni viceversa), **es el muro de paridad/asintótica casi-prima** — el mismo
que bloqueó el Arc A, pero atacado ahora desde el lado opuesto: el Arc A necesitaba
distinguir $\omega(n) \bmod 2$ (asintótica con signo); aquí se necesitaría a lo sumo
mayorar un funcional bilineal casi-primo. La distinción mayorar/asintotizar es
exactamente la frontera entre lo que la criba da y lo que la paridad prohíbe. El
experimento deja la dificultad en el lado bueno de esa frontera **si y solo si** el
puente (β) se puede cerrar con cotas unilaterales; si no, transmuta a paridad (patrón
Doc 99, con destino distinto de CAP — un dato nuevo en sí mismo).

### 6.5. Presupuesto para potencias $k \geq 3$ (esbozo, no se reclama prueba)

El mismo cálculo se itera: el núcleo $k$-engrosado $h = g(x_1\cdots x_k)\,
\Phi(\vec v)$, con $\vec v$ las $k-1$ coordenadas transversales ($\Phi \in
C_c^\infty((\mathbb{R}_+^*)^{k-1})$), da por el isomorfismo de grupos análogo al
Lema 3.3:
$$\hat h(s_1,\dots,s_k) = \frac{1}{k}\;\hat g\!\left(\frac{s_1+\cdots+s_k}{k}\right)
\widehat\Phi(\text{combinaciones de diferencias}),$$
término de ceros $\frac1k\sum_{\rho_1..\rho_k}\hat g(\frac{\sum\rho_i}{k})
\widehat\Phi(\cdots)$ — el espectro de $\sum_i H_C^{(i)}$ —, y lado aritmético soportado
en $k$-casi-primos $p_1^{a_1}\cdots p_k^{a_k}$ con coeficientes
$\Lambda^{\star k}$-ponderados, más bloques mixtos de soporte finito. La reabsorción de
mixtos (Teorema 4.4) se itera ranura por ranura. El presupuesto de la contradicción
final sería: índice del bloque $(4m)^k/2$ (Doc 106, Prop. 3.5) contra una cota de criba
del lado $k$-casi-primo; las cotas superiores de criba para correlaciones de orden $k$
crecen típicamente como $C^k$ (constantes geométricas en $k$ [HR74]). La comparación
$C^k$ vs $(4m)^k/2$ requiere $C < 4m$ con $m$ desconocido: para que la contradicción
mate todo $m \geq 1$ se necesita $C < 4$. **No se afirma nada aquí**: ni que el puente
(β) exista, ni el valor de $C$; se registra que el presupuesto es geométrico contra
geométrico — la forma cuantitativa precisa queda dentro del Lema 7.2. (Recordatorio del
Doc 106 §5.2: por la fuerza exponencial de (a), basta $f(k)$ subexponencial; eso relaja
$C < 4$ a $C$ cualquiera si la cota de criba fuera $C^{o(k)}\cdot$polinomial, cosa que
tampoco se afirma.)

---

## 7. El siguiente lema

### 7.1. Lo que este documento deja probado

**Teorema 7.1 (resumen ejecutable).** Incondicionalmente (sin RH, sin Hipótesis D para
(i)–(iii); con la configuración del juguete para (iv)):

(i) $\mathcal{W}_2 = \mathcal{W}\otimes\mathcal{W}$ está bien definida sobre
$C_c^\infty((\mathbb{R}_+^*)^2)$ con doble presentación espectral/aritmética
(Teorema 2.4).

(ii) Sobre el núcleo engrosado, el lado espectral es la suma de Minkowski de espectros
con peso transversal: $\tfrac12\sum\hat g(\tfrac{\rho_1+\rho_2}{2})
\hat\varphi(\tfrac{\rho_1-\rho_2}{2})$ (Teorema 3.4, Corolario 3.6).

(iii) El lado aritmético es autónomo: transformada $\varphi$-ponderada de
$\Lambda\star\Lambda$ sobre casi-primos + bloques de soporte finito + polos +
arquimediano; los términos mixtos ceros×primos se reabsorben (Teoremas 4.2, 4.4).

(iv) En el juguete, el bloque off×off de $Q_2$ tiene signatura $(8,8)$, confirmando la
Prop. 3.5 del Doc 106, con el peso $\hat\varphi$ como portador necesario de la mitad
del índice (Teorema 5.5, Corolario 5.6); el índice global de $Q_2$ es $\infty$ bajo
¬RH (Prop. 6.1).

### 7.2. El enunciado exacto que falta

**Lema Faltante 7.2 (puente criba→índice; la nueva encarnación del Lema 5.3).** *Probar
que existe una función $f$ con $f(2) < \infty$ proveniente solo de datos aritméticos
(cotas de criba del bloque casi-primo, polos, término arquimediano — sin posiciones de
ceros) tal que el defecto de positividad de $Q_2$ sobre la clase engrosada es de rango
acotado por $f(2)$: existe un subespacio $\mathcal{H}_2 \subseteq
\mathrm{span}\{h_{g,\varphi}\}$ de codimensión $\leq f(2)$ con
$Q_2|_{\mathcal{H}_2} \geq -\varepsilon$-pequeño en el sentido C5 del Doc 94 — o, en la
versión por bloques: el índice negativo de todo bloque espectral de $Q_2$ asociado a
una ventana compacta de la variable suma está acotado por $f(2)$ uniformemente en la
ventana. Y su extensión a $k$: $f(k)$ subexponencial en $k$ con la misma fuente.*

Dos formas de morir y una de vivir, para el Lema 7.2: (muerte 1) si toda prueba de la
cota requiere la asintótica casi-prima uniforme, transmuta a paridad/correlación de
pares (§6.4(γ)) — patrón Doc 99 con muro nuevo; (muerte 2) si requiere positividad del
bloque crítico del objeto doble, transmuta a CAP — patrón Doc 99 clásico; (vida) si las
cotas superiores unilaterales de criba bastan para el control de rango tipo C5 — el
único escenario en que el esqueleto de Deligne se cierra. El discriminador I2a debe
aplicarse a cada intento.

**Observación 7.3 (por qué la Prop. 6.1 no mata al candidato).** Que
$\kappa(Q_2) = \infty$ bajo ¬RH no es el modo de muerte de la Prop. 3.4 del Doc 106
(colapso del invariante): el dato de amplificación de la Forma B usa el índice del
**bloque relativo** (tensor sobre $\mathcal{K}_{\mathrm{off}}$, regularización R2 ya
adoptada), y este documento muestra que ese bloque está **realizado dentro de un
funcional con lado aritmético autónomo** — que era lo que faltaba. La infinitud global
es la razón por la que el Lema 7.2 pide cota *por bloques/por ventanas*, no global.

---

## 8. VEREDICTO

**VEREDICTO: CANDIDATO VIVO.**

**Razón precisa.** El experimento del Problema 5.4 tenía dos salidas: "si el lado
aritmético del funcional diagonal resulta expresable en casi-primos con coeficientes
computables, el Lema 5.2 tiene candidato; si requiere las posiciones de los ceros,
MW-7 reaparece y el Candidato 2 muere". Ocurrió lo primero, con prueba:

1. **Los términos mixtos ceros×primos — el punto designado de reaparición de MW-7 — se
   reabsorben** (Teorema 4.4): son artefactos de la presentación semi-expandida, y el
   funcional completo $\mathcal{W}_2(h_{g,\varphi})$ es computable sin posiciones de
   ceros. MW-7 queda confinado al enunciado vecino (fórmula explícita *propia* de una
   variable para el objeto suma, Obs. 4.5), que el Lema 5.2 no necesita.

2. **El lado casi-primo es autónomo y estructurado** (Teorema 4.2): transformada
   $\varphi$-ponderada de $\Lambda\star\Lambda$ — el pariente exacto del término
   casi-primo de la $\Lambda_2$ de Selberg — más bloques de soporte finito.

3. **La signatura tensorial $(8,8)$ sobrevive a la restricción diagonal engrosada**
   (Teorema 5.5): 8 planos hiperbólicos, sin degeneración, confirmando la Prop. 3.5
   del Doc 106 en su primera realización analítica. Hallazgo no anticipado: la mitad
   del índice negativo vive en sumas puramente imaginarias y es portada por el peso
   transversal $\hat\varphi$ (Corolario 5.6) — la conjetura "los negativos están en las
   sumas reales $\pm2\delta$" es falsa.

**Calificación honesta del "VIVO".** Vivo significa: el Lema Faltante 5.2 del Doc 106
pasó de gap nombrado a **candidato con construcción explícita y verificación en el
juguete**. No significa que la Forma B esté cerca de cerrar: todo el peso está ahora en
el Lema Faltante 7.2 (puente criba→índice, heredero del 5.3), con sus dos modos de
transmutación documentados (paridad, CAP) y un escenario de vida preciso (cotas
unilaterales de criba ⇒ control de rango C5). La novedad estratégica real de este
documento: por primera vez en el programa, la fuente candidata de finitud es un input
incondicional no espectral y no-CAP (cotas superiores de criba en el semigrupo
casi-primo), y el muro potencial identificado (paridad/asintótica) es **distinto** de
CAP — el programa gana un segundo frente independiente en lugar de reencontrar el
mismo muro con otro nombre.

**Siguiente paso:** Lema 7.2, empezando por su caso de ventana única en el juguete:
¿acota la cota de criba de $\sum_N g(N)(\Lambda\star_\varphi\Lambda)(N)$ el índice
negativo del bloque de $Q_2$ en una ventana compacta de $\sigma$ que contenga
$\{\pm\delta, \pm i\gamma_0, 0, \pm\delta\pm i\gamma_0\}$?

---

## Referencias

**Internas (backward-only):** Doc 106 (Prop. 3.5: $\mathrm{neg.ind}(Q_1\otimes Q_2) =
p_1q_2+q_1p_2$, $\kappa(\psi^{\otimes k}) = (4m)^k/2$; Prop. 3.4: colapso a
$\kappa=\infty$; Lemas Faltantes 5.2/5.3; Problema 5.4); Doc 98 (modelo de juguete,
Prop. 6.1: dos planos hiperbólicos, $\kappa=2$; Obs. 6.2: convenciones de apareamiento;
Obs. 6.3: generadores residuales); Doc 96 (Teorema 8.1: localización
$\mathcal{K}_{\mathrm{off}}$; Prop. 4.10: autovalores $\rho-1/2$ de $H_C$); Doc 94
(condición C5: defecto de positividad concentrado en cabeza finita); Doc 99 (patrón de
transmutación; discriminador I2a); P35 (Def. weil: $\mathcal{W}$, $Q(f,g) =
\mathcal{W}(f\star\tilde g)$, Hipótesis D, $\kappa = 2m$); P41 §7 (Forma B).

**Literatura verificada:**
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm.
  Sém. Math. Univ. Lund (1952), 252–265. (Fórmula explícita y criterio de positividad.)
- E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers I*,
  Rend. Mat. Acc. Lincei (9) **11** (2000), 183–233. (Formas equivalentes del término
  arquimediano; funcional cuadrático de Weil.)
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53, 2004,
  Cap. 5 (Thm. 5.12: fórmula explícita general; Thm. 5.8: $N(T)$).
- H. L. Montgomery, *The pair correlation of zeros of the zeta function*, en Analytic
  Number Theory, Proc. Sympos. Pure Math. **24**, AMS (1973), 181–193. [Mon73]
- D. A. Goldston, H. L. Montgomery, *Pair correlation of zeros and primes in short
  intervals*, en Analytic Number Theory and Diophantine Problems, Birkhäuser Progr.
  Math. **70** (1987), 183–203. [GM87] (Equivalencia correlación de pares ↔ varianza de
  primos en intervalos cortos; el diccionario ceros-dobles/casi-primos.)
- A. Selberg, *An elementary proof of the prime-number theorem*, Ann. of Math. (2)
  **50** (1949), 305–313. [Sel49] ($\Lambda_2(n) = \Lambda(n)\log n +
  \sum_{d\mid n}\Lambda(d)\Lambda(n/d) = \sum_{d\mid n}\mu(d)\log^2(n/d)$.)
- H. Halberstam, H.-E. Richert, *Sieve Methods*, Academic Press, 1974. [HR74] (Cotas
  superiores de criba para correlaciones de $\Lambda$; constantes absolutas. El valor
  exacto de las constantes citadas en §6.5: [NO VERIFICADO en detalle; no load-bearing
  — ningún resultado de este documento depende de él].)

*Fin del Doc 107.*
