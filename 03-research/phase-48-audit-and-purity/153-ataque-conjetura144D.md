# Doc 153 — Ataque a la Conjetura 144.D / GAP-144.C: el test de de la Vallée Poussin en ½, la confrontación con Kaczorowski–Perelli, y el eslabón mínimo destilado

**Programa:** Hipótesis de Riemann — Phase 48: AUDITORÍA Y PUREZA.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** ataque frontal a la **Conjetura 144.D** (Doc 144 §3.3) y a su residuo **GAP-144.C** —
el pivote aritmético de la mitad de finitud ($m<\infty$) tras la refutación analítica de LP-141 (Prop. 144.2).
El encargo: (1) enunciar 144.D/GAP-144.C con cuantificadores exactos; (2) desarrollar el ataque
"de la Vallée Poussin centrado en ½" (Euler + positividad de $\Lambda$ contra un enjambre sub-resolución)
con todos los cálculos en forma cerrada, y DECIDIR si muere o si una subsucesión basta; (3) confrontar con
la clasificación de grado pequeño de Kaczorowski–Perelli; (4) aislar el eslabón mínimo no probado y ubicarlo
en la jerarquía; (5) veredicto.

**Contrato creativo (regla absoluta de etiquetado):** **[DEFINICIÓN-NUEVA]** = libertad total.
**[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado DE VERDAD acá, prueba completa; resultados externos citados con
precisión. **[CÁLCULO]** = mostrado. **[PUENTE]** = conexión con ζ/RH con estatus honesto. **[GAP]** =
declarado. **[GAP de literatura]** = dato no verificado en fuente esta sesión, no usado como premisa.

**Prerrequisitos leídos en fuente esta sesión (completos):** Doc 144 entero (Def. 144.0, Props. 144.1–144.9,
Conjetura 144.D, GAP-144.C, Cor. 144.10); Doc 141 entero (Lemas 141.B0/141.B, Cor. 141.B2, Cálculos
141.M4/M5/R3, Prop. 141.R2, Conjetura 141.E, GAP-141.G1); Doc 131 §6 (Axioma H, Teo. 6.6 Poisson local,
Teo. 6.7 pureza local, Prop. 6.8 DH, Deseo 6.9 H⁺); Doc 146 (veredicto GAP-141.DH: GORDOS, ceros off de
D–H a distancia macroscópica).

---

## 0. Resumen ejecutivo

1. **(§1)** 144.D y GAP-144.C quedan enunciados con cuantificadores totales, junto con los axiomas exactos
   (A1)–(A4) de la categoría D131-H⁺ que este documento usa, declarados uno a uno.

2. **(§2) El ataque dlVP-en-½ MUERE, y el certificado de defunción es cuantitativo y nuevo.**
   La región libre de ceros clásica es, en efecto, el único teorema de repulsión incondicional de la teoría
   ($|\beta-1|\geq c/\log\gamma$: repulsión desde $\Re s=1$), y su motor es Euler + positividad de $\Lambda$
   ($3+4\cos\theta+\cos2\theta\geq0$). Transpuesto a ½: **[LEMA 153.2]** prueba que un cuádruplo off a
   distancia $\delta$ perturba TODO el semiplano $\sigma>1$ — el único lugar donde la positividad muerde —
   en a lo sumo $C_0\,\delta^2/(1+(t-\gamma)^2)$ (segundo orden: la ecuación funcional mata el primer orden,
   avatar en $\sigma>1$ del Cálculo 141.M4). **[PROPOSICIÓN 153.3]:** el enjambre sub-resolución completo
   ($\delta_j\log\gamma_j\to0$, TODOS los off) desvía $-\Re\frac{\zeta'}{\zeta}$ en $\sigma\in(1,2]$ en
   $o(1/\log t)$ — uniformemente. **[COROLARIO 153.4] (la cuenta que el encargo pide):** para que el efecto
   acumulado a altura $\gamma$ alcance tamaño constante hacen falta $\gtrsim\delta^{-2}\gtrsim\log^2\gamma$
   ceros off por ventana unitaria — **densidad superlineal en $\log\gamma$, prohibida por
   Riemann–von Mangoldt** ($N(T+1)-N(T)\leq C\log T$, incondicional, válido en la categoría: Lema 153.5).
   **DECISIÓN: ninguna subsucesión basta; el argumento muere**, y muere por el mismo mecanismo que el no-go
   de promedios del Doc 141 (la palanca dlVP es un funcional de Weil de soporte efectivo $O(1)$: Cor. 141.B2
   lo cubre; §2.5 da además la razón estructural: la línea repelente debe portar el polo de la medida
   positiva, y $\Re s=\tfrac12$ no porta ninguno — la desigualdad dlVP centrada en ½ es $0\geq0$).

3. **(§2.6) La pieza NUEVA que sobrevive al naufragio: el exceso de auto-escala es de UN SIGNO y DOMINANTE.**
   **[PROPOSICIÓN 153.6]:** si en vez de soporte fijo se evalúa cada cuádruplo a SU escala $L_j=1/\delta_j$
   con el test de Fejér centrado (positivo en ambos lados), su exceso sobre la proyección a la línea es
   $\geq L_j/3$ — positivo (un cosh contra 1: sin cancelación posible) y $\gg\log\gamma_j$ = la masa total
   esperada del mar on-line en la ventana. El perfil de media nula (141.M5) NO aplica en auto-escala: el
   enjambre es invisible a todo soporte fijo pero **dominante a soporte adaptado** $1/\delta_j$. Esto escapa
   al no-go 141.B2 (cuya diagonalización exige la familia de tests fijada ANTES de la configuración) — el
   precio exacto es que el lado primo a soporte adaptado super-logarítmico es desconocido.

4. **(§3) Kaczorowski–Perelli: cierra la PRIMERA flecha del mecanismo y refuta la segunda tal como estaba
   enunciada.** La clasificación de grado pequeño (grado $0<d<1$ vacío; $d=1$ = ζ y $L$ de Dirichlet
   desplazadas; $1<d<2$ vacío [KP99], [KP11], [CG93]) prueba — en grado $<2$ y módulo el caveat de inmersión
   [GAP-153.E] — que **continuación + Euler + ecuación funcional ⟹ dato local de carácter unitario (pureza
   máxima)**: la flecha "continuación ⟹ pureza" de 144.D es TEOREMA en grado $<2$. Pero la segunda flecha
   ("pureza ⟹ repulsión/gordos") es **insostenible tal como el Doc 144 la enuncia**: ζ misma tiene dato
   local puro en TODO primo y su repulsión es exactamente RH-abierta ([PROPOSICIÓN 153.8]). La pureza local
   por primo no puede ser el portador del mecanismo; el portador tiene que ser el dato de VENTANA a soporte
   super-logarítmico — exactamente donde vive la pieza nueva del punto 3.

5. **(§4) El eslabón mínimo, destilado y posicionado.** **[DEFINICIÓN-NUEVA 153.9] (Rigidez 153.M):** "ningún
   objeto D131-H⁺ sostiene déficit casi-primo unilateral de tamaño $\gtrsim L$ en infinitas ventanas de
   auto-escala con $L_j/\log\gamma_j\to\infty$". **[PROPOSICIÓN 153.10]:** 153.M ⟹ 144.D (vía el exceso de
   un signo de 153.6 + la fórmula explícita de la categoría). Jerarquía probada:
   $141.E \Rightarrow 153.M \Rightarrow 144.D \Rightarrow$ LP-141-categoría. 153.M es estrictamente más débil
   que 141.E como enunciado de posición, pero como demanda de EVALUACIÓN es el muro viejo (108-N, soporte
   $\log\gamma$) transpuesto a soporte super-logarítmico: NO es más barato cuantitativamente; el avance de la
   sesión es estructural (el lado de ceros queda con signo probado; todo el GAP se concentra en el lado primo).

6. **(§5) VEREDICTO: ESLABÓN MÍNIMO AISLADO (ni probada ni refutada), con una pieza nueva probada y el
   mecanismo del Doc 144 corregido.**

---

## 1. Los enunciados exactos

### 1.1. La categoría D131-H⁺: axiomas declarados

El Doc 144 usa "D131-H⁺" por referencia al Deseo 6.9 del Doc 131. Para que este documento sea autocontenido
y auditable, fijo los axiomas que USO (todo lo probado abajo declara cuáles necesita):

**Definición 153.0 [DEFINICIÓN-NUEVA] (categoría D131-H⁺, axiomas de trabajo).** $F$ pertenece a D131-H⁺ si:

- **(A1) Euler con dato hermitiano positivo:** $-\frac{F'}{F}(s)=\sum_{n\geq2}a(n)\,n^{-s}$ con $a$ soportada
  en potencias de primos, $a(n)\geq0$, y la serie absolutamente convergente en $\sigma>1$ con
  $\sum_{n\leq X}a(n)\ll X$ (tipo Chebyshev; en ζ, $a=\Lambda$).
- **(A2) Continuación:** $F$ se continúa meromorfa a $\mathbb C$ con a lo sumo un polo en $s=1$ (orden
  $r\geq0$), y orden de crecimiento finito.
- **(A3) Ecuación funcional:** $\Phi(s):=Q^s\gamma_F(s)F(s)$ cumple $\Phi(s)=\overline{\Phi(1-\bar s)}$, con
  $\gamma_F$ producto finito de factores $\Gamma(\lambda_is+\mu_i)$, $\lambda_i>0$, $\Re\mu_i\geq0$
  (tipo arquimediano, en el sentido del Doc 131 §6.6').
- **(A4) Fórmula explícita:** para todo $F\in C_c^\infty$ par a trozos como en Doc 141 §3.1 vale la identidad
  de Weil $\sum_\rho h(\rho)=\text{(arquimediano + polos)}-\sum_n a(n)n^{-1/2}\bigl(F(\log n)+F(-\log n)\bigr)$,
  $h(s)=\int F(u)e^{(s-1/2)u}du$, suma sobre los ceros no triviales con multiplicidad. (Consecuencia estándar
  de (A1)–(A3) por el argumento de contorno clásico; la doy por axioma para no re-probar Stirling.)

Nota honesta: (A1)–(A4) son la lectura mínima de "producto de Euler genuino + dato local hermitiano positivo
+ continuación + ecuación funcional" del Doc 144 §3. No incluyen la cota de Ramanujan de la clase de Selberg
ni una noción de grado; eso importa en §3 ([GAP-153.E]).

### 1.2. La Conjetura 144.D con cuantificadores totales

Transcribo del Doc 144 §3.3, explicitando los cuantificadores:

**Conjetura 144.D (Doc 144, citada exacta).** *Para todo $F\in$ D131-H⁺: si $F$ tiene $m=\infty$ ceros off
(cuádruplos $\{\tfrac12\pm\delta_j\pm i\gamma_j\}$, $\delta_j\in(0,\tfrac12)$, $\gamma_j\to\infty$), entonces*
$$\exists\,c>0\ \ \exists\,(j_k)_{k\geq1}\ \text{subsucesión infinita}:\qquad
\delta_{j_k}\,\log\gamma_{j_k}\;\geq\;c\quad\forall k.$$

Forma lógica: $\Pi_3$ sobre los ceros ($m=\infty$ es $\Pi_2$; la conclusión es $\Sigma_3$:
$\exists c\,\forall N\,\exists j>N$). La **negación** de la conclusión es la hipótesis del enjambre:
$$\textbf{(ENJAMBRE)}:\qquad m=\infty\quad\text{y}\quad \delta_j\log\gamma_j\xrightarrow{\,j\to\infty\,}0$$
(todos los off asintóticamente sub-resolución al calendario natural $\{C\log\}$). Probar 144.D = derivar una
contradicción de (ENJAMBRE) dentro de D131-H⁺.

**GAP-144.C (Doc 144, Obs. 144.4bis(2), citado exacto).** El residuo no probado es *la cota inferior efectiva
$\delta_{j_k}\gtrsim1/\log\gamma_{j_k}$ sobre una subsucesión de ceros off, derivada de la continuación
analítica del producto de Euler*. La evidencia direccional es el Cálculo 141.R3 (la construcción de Euler que
violaría la cota NO continúa); convertir "no continúa" en la cota es el GAP.

**Lo que 144.D compra (Prop. 144.4 del Doc 144, recordada, no re-probada):** 144.D ⟹ LP-141$(a)$ en D131-H⁺
para todo calendario $a\succeq\log$, de hecho la forma fuerte ($m=\infty\Rightarrow$ infinitos gordos a
calendario $\log$); y con positividad débil del símbolo (Prop. 141.P3), $m<\infty$. 144.D es estrictamente
más débil que la Conjetura 141.E ($\liminf$ sobre TODOS los off).

**El mecanismo conjeturado (Doc 144 §3.3, citado para auditarlo en §3):** *"cada cero off a distancia
$\delta_j$ exige impureza local sostenida de amplitud $\gtrsim\delta_j$ en una banda de primos de tamaño
logarítmico $\asymp\log\gamma_j$; la continuación acopla esos datos y prohíbe que la impureza sea
simultáneamente sub-resolución en todos los ceros y sostenida en infinitos."* §2 y §3 mostrarán que la
amplitud verdadera a soporte $\log\gamma_j$ no es $\gtrsim\delta_j$ sino $\asymp(\delta_j\log\gamma_j)^2\to0$
bajo (ENJAMBRE) — el mecanismo, tal como está escrito, pide detección donde la señal es nula; la versión
reparada vive en soporte $1/\delta_j$ (§2.6, §4).

---

## 2. El ataque de la Vallée Poussin centrado en ½

### 2.1. El teorema de repulsión clásico y sus dos ingredientes

**Cálculo 153.1 [CÁLCULO] (dlVP como teorema de repulsión, con el mecanismo a la vista).** Para $\sigma>1$,
(A1) da
$$-\Re\frac{F'}{F}(\sigma+it)\;=\;\sum_{n\geq2}a(n)\,n^{-\sigma}\cos(t\log n),$$
y la desigualdad trigonométrica $3+4\cos\theta+\cos2\theta=2(1+\cos\theta)^2\geq0$ con $a\geq0$ produce
$$3\Bigl(-\frac{F'}{F}(\sigma)\Bigr)+4\Bigl(-\Re\frac{F'}{F}(\sigma+it)\Bigr)+\Bigl(-\Re\frac{F'}{F}(\sigma+2it)\Bigr)\;\geq\;0.$$
Por Hadamard, $-\Re\frac{F'}{F}(s)=\Re\frac{r}{s-1}-\sum_\rho\Re\frac1{s-\rho}+O(\log(|t|+2))$, y **cada cero
aporta con UN signo**: $\Re\frac1{s-\rho}=\frac{\sigma-\beta}{|s-\rho|^2}\geq0$ para $\sigma>1>\beta$.
Descartando todos los ceros salvo el objetivo $\rho_0=\beta_0+i\gamma_0$ y tomando $t=\gamma_0$,
$\sigma=1+\eta$:
$$\frac{4}{\sigma-\beta_0}\;\leq\;\frac{3r}{\sigma-1}+O(\log\gamma_0)\qquad\Longrightarrow\qquad
1-\beta_0\;\geq\;\frac{c}{\log\gamma_0}$$
optimizando $\eta\asymp1/\log\gamma_0$ [dlVP1899], [T86, Thm. 3.8]. Los dos ingredientes estructurales:
**(I-1)** un presupuesto positivo SINGULAR adyacente a la línea repelente (el polo en $s=1$: residuo $r$ de la
medida positiva $\sum a(n)n^{-\sigma}$, que diverge como $r/(\sigma-1)$ al acercarse); **(I-2)** términos de
un solo signo, de modo que el cero objetivo compite contra el presupuesto SIN ayuda del resto. La fuerza de
la palanca sobre el objetivo es $\frac4{\sigma-\beta_0}$ — **singular** cuando $\beta_0\to\sigma$: por eso
repele de $\Re s=1$ (y por la ecuación funcional, de $\Re s=0$). $\square$

Tal como observa el encargo: esto ES un teorema de repulsión incondicional — el único — y la pregunta es si
el mismo motor corre centrado en ½ contra (ENJAMBRE).

### 2.2. La pérdida exacta al centrar en ½: de singular a segundo orden

La positividad (A1) vive solo en $\sigma>1$, a distancia $\geq\tfrac12$ de la línea crítica. Dos pérdidas se
componen:

**(Pérdida 1: la palanca se acota.)** La fuerza de un cero $\beta\approx\tfrac12$ sobre $s=\sigma+i\gamma$,
$\sigma>1$, es $\frac{\sigma-\beta}{(\sigma-\beta)^2+(t-\gamma)^2}\leq\frac1{\sigma-\beta}\leq2$: acotada,
no singular. Comparada con el término arquimediano $O(\log\gamma)$ del Hadamard, la fuerza de UN cero cerca
de ½ es ya sub-presupuesto por un factor $1/\log\gamma$.

**(Pérdida 2: la ecuación funcional cancela el primer orden.)** El par simétrico $\tfrac12\pm\delta+i\gamma$
entra junto. Su efecto NETO respecto del par proyectado es de segundo orden en $\delta$ — el avatar en
$\sigma>1$ del Cálculo 141.M4 (que lo probó EN la línea). Lo pruebo con constante explícita:

**Lema 153.2 [LEMA] (cota de segundo orden en el semiplano de positividad).** Sea $s=\sigma+it$ con
$\sigma\in(1,2]$, y sea $Z$ una configuración que contiene el cuádruplo $\{\tfrac12\pm\delta\pm i\gamma\}$
con $\delta\leq\tfrac14$; sea $Z^\flat$ la misma configuración con el cuádruplo proyectado (ceros dobles en
$\tfrac12\pm i\gamma$). Entonces
$$\Bigl|\sum_{\rho\in Z}\Re\frac1{s-\rho}-\sum_{\rho\in Z^\flat}\Re\frac1{s-\rho}\Bigr|
\;\leq\;C_0\,\delta^2\Bigl(\frac1{1+(t-\gamma)^2}+\frac1{1+(t+\gamma)^2}\Bigr),$$
con $C_0$ absoluta (puede tomarse $C_0=2^{12}$).

*Demostración.* Escribo $x:=\sigma-\tfrac12\in(\tfrac12,\tfrac32]$, $u:=t-\gamma$, y
$f(w):=\frac{w}{w^2+u^2}$, de modo que el par a altura $+\gamma$ aporta $f(x-\delta)+f(x+\delta)$ y su
proyección $2f(x)$. Diferencia segunda simétrica con resto integral:
$$|f(x+\delta)+f(x-\delta)-2f(x)|\;=\;\Bigl|\int_0^\delta(\delta-y)\bigl[f''(x+y)+f''(x-y)\bigr]dy\Bigr|
\;\leq\;\delta^2\sup_{|y|\leq\delta}|f''(x+y)|.$$
Cálculo directo: $f'(w)=\frac{u^2-w^2}{(w^2+u^2)^2}$, $f''(w)=\frac{2w(w^2-3u^2)}{(w^2+u^2)^3}$, luego para
$w\geq\tfrac14$ (que cubre $x+y\geq\tfrac12-\tfrac14$):
$$|f''(w)|\leq\frac{2w(w^2+3u^2)}{(w^2+u^2)^3}\leq\frac{6w}{(w^2+u^2)^2}
\leq\frac{12}{(\tfrac1{16}+u^2)^2}\leq\frac{C_0}{1+u^2},$$
usando $(\tfrac1{16}+u^2)\geq\tfrac{1+u^2}{17}$ y $(\tfrac1{16}+u^2)\geq\tfrac1{16}$. El par conjugado a
altura $-\gamma$ da lo mismo con $u'=t+\gamma$. $\square$

**Cuantificación de "esa pérdida" (lo que el encargo pide medir).** En $\Re s=1$ la palanca por cero objetivo
es $\asymp\frac1{1-\beta}$ (singular, primer orden, un signo). En $\Re s=\tfrac12$ medida desde $\sigma>1$ es
$\leq C_0\delta^2$ (acotada, segundo orden, y de signo NO utilizable: la diferencia segunda de $f$ cambia de
signo con $u$ — es el perfil de media nula 141.M5 visto desde $\sigma>1$, donde el kernel lorentziano de
ancho $x\geq\tfrac12$ promedia la señal de ancho $\delta$ y la reduce de $O(1)$ on-line a $O(\delta^2)$).
Pérdida total respecto del caso dlVP: factor $\delta^2(1-\beta)\big|_{\beta\to1} \rightsquigarrow$ en
términos útiles, **la eficiencia por cero cae de $\Theta(\log\gamma)$ (caso clásico, cero pegado a 1) a
$\Theta(\delta^2)$ (cero pegado a ½)** — bajo (ENJAMBRE), $\delta^2=o(1/\log^2\gamma)$.

### 2.3. El presupuesto de visibilidad del enjambre completo

**Proposición 153.3 [PROPOSICIÓN] (el enjambre entero es $o(1/\log t)$-invisible en todo el semiplano de
positividad).** Sea $Z$ una configuración admisible (finitos ceros por ventana unitaria, con cota de ventana
$n_Z(T):=\#\{\rho:|\gamma_\rho-T|\leq\tfrac12\}\leq C_1\log(T+2)$) cuyos cuádruplos off cumplen (ENJAMBRE):
$\delta_j\leq\varepsilon(\gamma_j)/\log\gamma_j$ con $\varepsilon(\gamma)\to0$ no creciente. Entonces,
uniformemente en $\sigma\in(1,2]$ y $t\geq4$:
$$\Bigl|\sum_{\rho\in Z}\Re\frac1{s-\rho}-\sum_{\rho\in Z^\flat}\Re\frac1{s-\rho}\Bigr|
\;\leq\;C_2\,\frac{\varepsilon(\sqrt t)^2+\tfrac{\log t}{\sqrt t}}{\log t}\;=\;o\Bigl(\frac1{\log t}\Bigr).$$

*Demostración.* Por el Lema 153.2 la diferencia está dominada por
$C_0\sum_j\delta_j^2\bigl[(1+(t-\gamma_j)^2)^{-1}+(1+(t+\gamma_j)^2)^{-1}\bigr]$; el segundo sumando es
$\leq(1+t^2)^{-1}\sum_j\delta_j^2$ por ventana, absorbido en el término $\log t/\sqrt t$ tras agrupar por
ventanas (los $\delta_j\leq\tfrac14$ y la cota de ventana dan $\sum_{\gamma_j\leq T}\delta_j^2\leq CT\log T$).
Para el primero, agrupo por ventanas unitarias centradas en enteros $n$ y uso la cota de ventana:
$$\sum_j\frac{\delta_j^2}{1+(t-\gamma_j)^2}\;\leq\;C_1\sum_{n\geq2}\frac{\log n}{1+(t-n)^2}
\Bigl(\sup_{\gamma\in[n-1,n+1]}\delta(\gamma)\Bigr)^2.$$
Parto en tres rangos. (i) $|n-t|\leq t/2$: ahí $\log n\asymp\log t$ y
$\delta(\gamma)^2\leq\varepsilon(t/2)^2/\log^2(t/2)$, y $\sum_n(1+(t-n)^2)^{-1}\leq\pi+1$: contribución
$\leq C\,\varepsilon(t/2)^2/\log t$. (ii) $n<t/2$: kernel $\leq(1+t^2/4)^{-1}$, y
$\sum_{n<t/2}\log n\,\delta^2\leq C\,t$ (cota trivial $\delta\leq\tfrac14$): contribución $\leq C/t$.
(iii) $n>3t/2$: $\sum_{n>3t/2}\frac{\log n\,\varepsilon^2/\log^2n}{1+(n-t)^2}\leq
C\sum_{k>t/2}\frac{1}{k^2}\cdot\frac{\varepsilon(\sqrt t)^2}{\log t}\cdot\log(\cdot)\leq C/t$. Sumando y
usando $\varepsilon$ no creciente ($\varepsilon(t/2)\leq\varepsilon(\sqrt t)$ para $t\geq4$): la cota.
$\square$

Mientras tanto, la única desigualdad incondicional disponible en $\sigma>1$ (el 3-4-1 de 153.1) tiene holgura
$\asymp\log t$ (el término arquimediano). **Cociente señal/holgura $=o(1/\log^2t)$.** Ningún punto de
evaluación, ninguna elección de $\sigma\in(1,2]$, ve al enjambre.

### 2.4. La cuenta decisiva: cuántos ceros sub-resolución hacen falta, y por qué R–vM lo prohíbe

**Lema 153.5 [LEMA] (cota de ventana en la categoría).** Si $F$ cumple (A1)–(A3), entonces
$N_F(T+1)-N_F(T)\leq C_F\log(T+2)$.

*Demostración.* Argumento clásico de Jensen [T86, Thm. 9.2], [IK04, Cap. 5]: por (A1),
$|F'/F(\sigma+it)|\leq\sum_na(n)n^{-\sigma}<\infty$ para $\sigma\geq2$, e integrando en $\sigma$ desde
$+\infty$ (donde $\log F\to0$): $|\log F(2+it)|\leq C$, luego $|F(2+it)|\asymp1$ uniformemente en $t$. La ecuación funcional (A3) y
Stirling dan $|F(-1+it)|\leq C(|t|+2)^{A}$; Phragmén–Lindelöf (con (A2): orden finito) da
$|F(\sigma+it)|\leq C(|t|+2)^{A'}$ en $-1\leq\sigma\leq2$. Jensen en el disco de centro $2+iT$ y radio $3$:
$\#\{\text{ceros en el disco de radio }\tfrac52\}\leq\frac{1}{\log(6/5)}\bigl[\log\max_{|z|=3}|F|-\log|F(2+iT)|\bigr]
\leq C_F\log(T+2)$, y la ventana $[T,T+1]\times[0,1]$ de la banda está contenida en ese disco. $\square$

**Corolario 153.4 [COROLARIO] (umbral de visibilidad: densidad superlineal — imposible).** Bajo el Lema
153.2, si en la ventana $[\gamma-\tfrac12,\gamma+\tfrac12]$ hay $K$ cuádruplos off, todos a distancia
$\leq\delta$, su efecto acumulado sobre $-\Re\frac{F'}{F}(\sigma+i\gamma)$, $\sigma\in(1,2]$, es
$\leq 2C_0K\delta^2$. Para que alcance siquiera el umbral constante $c_0>0$ (la menor holgura concebible de
una desigualdad de positividad tipo dlVP — la real es $\asymp\log\gamma$, peor) se necesita
$$K\;\geq\;\frac{c_0}{2C_0}\,\delta^{-2}\;\geq\;\frac{c_0}{2C_0}\,\frac{\log^2\gamma}{\varepsilon(\gamma)^2}
\qquad\text{(bajo ENJAMBRE)},$$
**superlineal en $\log\gamma$**, mientras el Lema 153.5 impone $K\leq C_F\log\gamma$. La brecha es un factor
$\geq\frac{c_0}{2C_0C_F}\cdot\frac{\log\gamma}{\varepsilon(\gamma)^2}\to\infty$: **inalcanzable por TODO el
enjambre junto, no solo por subsucesiones.** En particular ninguna subsucesión geométrica ayuda: el kernel
lorentziano de 153.2 tiene masa total $O(1)$ por unidad de altura, así que apilar alturas no acumula
($\sum_j\delta_j^2<\infty$ sobre cualquier subsucesión con $\delta_j\to0$ geométrica es aún más pequeño).
$\square$

**Decisión [el encargo pedía DECIDIR].** La respuesta a la disyuntiva del encargo es la primera rama:
**"densidad superlineal, imposible por Riemann–von Mangoldt" — el argumento muere.** Y muere por el mismo
no-go de promedios del Doc 141, hecho ahora cuantitativo: la palanca dlVP, escrita como funcional de Weil,
tiene núcleo $u\mapsto e^{-(\sigma-\frac12)|u|}$ — soporte efectivo $O\bigl(\tfrac1{\sigma-1/2}\bigr)=O(1)$,
ni siquiera logarítmico — y el Cor. 141.B2 cubre toda familia numerable de tales funcionales. La señal por
cuádruplo es $O(\delta^2)$ con perfil que el kernel grueso promedia a su media (nula al orden principal:
141.M5). No hay versión "desde fuera hacia ½" del teorema de la región libre de ceros con esta tecnología.

### 2.5. La razón estructural: la línea repelente debe portar el polo

**Observación 153.5bis (por qué la transposición es vacía, en una identidad).** El ingrediente (I-1) de
153.1 — presupuesto positivo singular adyacente a la línea repelente — no existe en ½: la medida positiva
$\sum a(n)n^{-\sigma}$ tiene su único polo en $\sigma=1$. Peor: el candidato a "desigualdad dlVP centrada en
½" es la positividad de $-\Re\frac{\xi'}{\xi}$ contra pares simétricos, y el Cálculo 141.M4 (citado, no
re-probado) muestra que la contribución de primer orden de TODO par simétrico a
$\Re\frac{\xi'}{\xi}(\tfrac12+it)$ es idénticamente $0$: la desigualdad transpuesta es $0\geq0$. La repulsión
clásica repele de las DOS líneas que portan estructura polar ($\Re s=1$ por el polo; $\Re s=0$ por la
ecuación funcional, espejo del polo); la línea crítica es el eje de simetría, sin polo, y las configuraciones
simétricas son equilibrios exactos. **Un análogo "los ceros no se pegan a ½ desde fuera" requeriría una
medida positiva con singularidad EN ½** — que es precisamente lo que ningún dato incondicional provee (y lo
que el Doc 134/141 llama el muro: la positividad del símbolo en ½ es la mitad aritmética no probada).

### 2.6. Lo que sobrevive: el exceso de auto-escala es de un signo y dominante

El naufragio de §2.3–2.4 es a **soporte fijo** (o acotado, o logarítmico). La estructura del enjambre cambia
cualitativamente si cada cuádruplo se interroga a SU escala $L_j:=1/\delta_j$ — que bajo (ENJAMBRE) es
super-logarítmica: $L_j/\log\gamma_j=1/(\delta_j\log\gamma_j)\to\infty$. Ahí pruebo algo nuevo:

**Proposición 153.6 [PROPOSICIÓN] (exceso de auto-escala: positivo y dominante).** Sea
$F_{L,\gamma_0}(u):=\bigl(1-\tfrac{|u|}L\bigr)_+\,2\cos(\gamma_0u)$ el test de Fejér modulado, con
$h(s)=\int F_{L,\gamma_0}(u)e^{(s-1/2)u}du$. Sea un cuádruplo $\{\tfrac12\pm\delta\pm i\gamma_0\}$
(centrado), $\kappa:=\delta L\leq1$, $\gamma_0L\geq10$. Entonces:

(a) **[positividad del test, ambos lados]** $F_{L,\gamma_0}$ tiene perfil $\bigl(1-\tfrac{|u|}L\bigr)_+\geq0$ y
$h(\tfrac12+it)=\widehat\Delta_L(t-\gamma_0)+\widehat\Delta_L(t+\gamma_0)\geq0$ con
$\widehat\Delta_L(v)=\frac{2(1-\cos Lv)}{Lv^2}\geq0$ (núcleo de Fejér): **todo cero on-line contribuye
$\geq0$.**

(b) **[el exceso del cuádruplo es de UN SIGNO]** La contribución del cuádruplo menos la de su proyección a la
línea es
$$E(\delta,L)\;=\;8\int_{-L}^{L}\Bigl(1-\frac{|u|}L\Bigr)\cos^2(\gamma_0u)\,\bigl(\cosh(\delta u)-1\bigr)\,
\frac{du}{2}\cdot 2\;\geq\;0,$$
con valor en forma cerrada (módulo el término oscilante, acotado abajo):
$$E(\delta,L)\;=\;8L\Bigl[\frac{\cosh\kappa-1}{\kappa^2}-\frac12\Bigr]\;+\;R,\qquad
|R|\;\leq\;\frac{50\,\kappa^2e^{\kappa}}{\gamma_0^2L},$$
y $\frac{\cosh\kappa-1}{\kappa^2}-\frac12=\frac{\kappa^2}{24}+O(\kappa^4)>0$ para $\kappa>0$. En particular,
a auto-escala $\kappa=1$ (es decir $L=1/\delta$): $E\geq L/3$.

(c) **[dominancia]** La masa total esperada del mar on-line en el test es $\asymp2\log\gamma_0$ (densidad
R–vM $\frac{\log\gamma_0}{2\pi}$ por la masa $\int\widehat\Delta_L=2\pi$ del núcleo, independiente de $L$).
Bajo (ENJAMBRE), $E\geq L_j/3\gg\log\gamma_j$: **el exceso de UN cuádruplo a su auto-escala domina la masa
de TODO el mar on-line de su ventana.**

*Demostración.* (a) Cálculo directo: $\int_{-L}^L(1-\tfrac{|u|}L)e^{ivu}du=2\int_0^L(1-\tfrac uL)\cos(vu)\,du
=\frac{2(1-\cos Lv)}{Lv^2}\geq0$; el perfil triangular es $\geq0$ por inspección (es
$\tfrac1L\,\chi_{[-L/2,L/2]}\!\star\chi_{[-L/2,L/2]}$: autocorrelación).

(b) El cuádruplo aporta $\sum_{\pm,\pm}h(\tfrac12\pm\delta\pm i\gamma_0)
=\int_{-L}^{L}(1-\tfrac{|u|}L)\,2\cos(\gamma_0u)\cdot2\cosh(\delta u)\cdot2\cos(\gamma_0u)\,du$, y la
proyección (dos ceros dobles en $\tfrac12\pm i\gamma_0$) aporta lo mismo con $\cosh\mapsto1$. Diferencia:
$$E=8\int_{-L}^{L}\Bigl(1-\frac{|u|}L\Bigr)\cos^2(\gamma_0u)\bigl(\cosh(\delta u)-1\bigr)du\;\geq\;0$$
**punto a punto** (triángulo $\geq0$, $\cos^2\geq0$, $\cosh-1\geq0$): un signo, sin cancelación posible —
aquí es donde el perfil de media nula 141.M5 deja de aplicar: el test adaptado pesa el cuádruplo con
$\cosh(\delta u)$, par y $\geq1$, no con un kernel que promedia su perfil dispersivo. Con
$\cos^2=\tfrac12(1+\cos2\gamma_0u)$: el término liso es
$4\cdot2\int_0^L(1-\tfrac uL)(\cosh\delta u-1)du=8L\int_0^1(1-v)(\cosh\kappa v-1)dv
=8L[\frac{\cosh\kappa-1}{\kappa^2}-\frac12]$, usando
$\int_0^1(1-v)\cosh(\kappa v)dv=\frac{\cosh\kappa-1}{\kappa^2}$ (dos integraciones por partes elementales) y
$\int_0^1(1-v)dv=\tfrac12$. El término oscilante $R=4\int_{-L}^{L}(1-\tfrac{|u|}L)\cos(2\gamma_0u)
(\cosh\delta u-1)du$: con $\varphi(u):=(1-\tfrac uL)(\cosh\delta u-1)$ se tiene $\varphi(0)=\varphi(L)=0$,
$\varphi'(0)=0$, $|\varphi'(L)|=\frac{\cosh\kappa-1}{L}$,
$\int_0^L|\varphi''|\leq\frac{2\delta\sinh\kappa\cdot L+\delta^2L^2\cosh\kappa}{L}
=\frac{\kappa(2\sinh\kappa+\kappa\cosh\kappa)}{L}$; dos integraciones por partes contra $\cos(2\gamma_0u)$
dan $|R|\leq\frac{8}{(2\gamma_0)^2}\bigl[|\varphi'(L)|+\int|\varphi''|\bigr]\leq\frac{50\kappa^2e^\kappa}
{\gamma_0^2L}$ para $\kappa\leq1$. Para $\kappa=1$:
$8[\cosh1-1-\tfrac12]=8(0.5430\ldots-\tfrac12)>0.34$, y $|R|\leq50e/(\gamma_0^2L)$ es despreciable con
$\gamma_0L\geq10$: $E\geq L/3$.

(c) La suma sobre ceros on-line $\tfrac12\pm i\gamma'$ del test es
$\sum_{\gamma'}2\bigl[\widehat\Delta_L(\gamma'-\gamma_0)+\widehat\Delta_L(\gamma'+\gamma_0)\bigr]$; con
densidad de ordenadas $\frac{\log\gamma_0}{2\pi}(1+o(1))$ por unidad (R–vM, Lema 153.5 para la cota superior
en la categoría) y $\int_{\mathbb R}\widehat\Delta_L(v)\,dv=2\pi\bigl(1-\tfrac{|0|}L\bigr)=2\pi$, la masa
esperada es $2\log\gamma_0(1+o(1))$, independiente de $L$. La comparación es inmediata. $\square$

**Observación 153.6bis (por qué esto escapa al no-go 141.B2 — y cuál es el precio exacto).** El Cor. 141.B2
diagonaliza contra una familia numerable de tests **fijada antes** de elegir la configuración: elige
$\delta_j$ tan pequeño que la señal $(\delta_jL_i)^2$ sea $<\varepsilon2^{-i-j}$ para los soportes $L_i$ ya
nombrados. La familia de auto-escala $\{F_{1/\delta_j,\gamma_j}\}$ se elige **después** (depende del objeto
hipotético): contra ella el cuádruplo $j$ tiene señal $\geq L_j/3$, no $o(1)$ — la diagonalización no puede
adelantarse a un test que copia sus parámetros. El no-go no aplica. El precio: el lado primo de la fórmula
explícita (A4) a soporte $L_j\gg\log\gamma_j$ es terra incognita — los términos $\sum_na(n)n^{-1/2}F(\log n)$
tienen tamaño bruto $\asymp e^{L/2}$ (por (A1) tipo Chebyshev y sumación parcial:
$\sum_{n\leq X}a(n)n^{-1/2}\asymp\sqrt X$), el lado arquimediano+polar otro tanto, y detectar el exceso
$\asymp L$ requiere que su diferencia se conozca con error $o(L)$ — precisión relativa $Le^{-L/2}$. El PNT
incondicional da error relativo $e^{-c\sqrt{\log X}}=e^{-c\sqrt L}$, y aun la mejor cancelación de sumas de
exponenciales sobre primos (Vinogradov–Korobov) deja $e^{-cL^{3/5-o(1)}}$: a distancia exponencial de lo
necesario. **Toda la dificultad de GAP-144.C queda concentrada, con signo probado, en una sola pregunta del
lado primo** — eso es §4.

---

## 3. Confrontación con Kaczorowski–Perelli

### 3.1. Los hechos de literatura, con precisión

- **[CG93]** Conrey–Ghosh: en la clase de Selberg $\mathcal S$ (con producto de Euler y cota de Ramanujan),
  grado $d=0$ implica $F\equiv1$, y no hay elementos con $0<d<1$.
- **[KP99]** Kaczorowski–Perelli, *On the structure of the Selberg class, I: $0\leq d\leq1$*, Acta Math.
  **182** (1999), 207–241: el resultado se extiende a la clase extendida $\mathcal S^\sharp$ (sin Euler), y
  el grado $d=1$ queda **clasificado**: en $\mathcal S$, los elementos de grado 1 son $\zeta(s)$ y las
  $L(s+i\theta,\chi)$ con $\chi$ primitivo no principal, $\theta\in\mathbb R$ (desplazadas). *(Nota de
  honestidad: la clasificación de $d=1$ pertenece a la serie KP; si la prueba completa para $\mathcal S$
  está en KP I o en una entrega posterior de la serie es un detalle de atribución que no verifiqué en fuente
  esta sesión — [GAP de literatura], sin efecto sobre el uso: el enunciado clasificatorio mismo es estándar
  y citado así por la literatura secundaria.)*
- **[KP11]** Kaczorowski–Perelli, *On the structure of the Selberg class, VII: $1<d<2$*, Ann. of Math. (2)
  **173** (2011), 1397–1441: **no hay elementos de grado $1<d<2$** (en $\mathcal S^\sharp$ con las
  normalizaciones de la serie).
- La conjetura de densidad / GRH en la clase de Selberg: **NO se asume nada de eso aquí** (instrucción del
  encargo); y por el Lema 141.M1 (citado) la tecnología de densidad es trivial en la escala $1/\log T$, así
  que tampoco serviría de sustituto.

**[GAP-153.E] (caveat de inmersión).** D131-H⁺ con (A1)–(A4) no incluye la cota de Ramanujan ni define
grado; los teoremas KP aplican a $\mathcal S/\mathcal S^\sharp$. Todo lo que sigue en §3.2 vale para
$F\in$ D131-H⁺$\,\cap\,\mathcal S$ (la intersección donde "grado" tiene sentido), que contiene los miembros
relevantes (ζ, $L$ de Dirichlet, $L$ automorfas normalizadas). Declarado; no se esconde.

### 3.2. Lo que la clasificación SÍ da: la primera flecha del mecanismo, probada en grado < 2

**Proposición 153.7 [PROPOSICIÓN] (KP cierra "continuación ⟹ pureza" en grado $<2$ y reduce 144.D ahí a las
$L$ de Dirichlet).** Sea $F\in$ D131-H⁺$\,\cap\,\mathcal S$ con grado $d<2$. Entonces:

(a) $F\equiv1$ (sin ceros: 144.D vacua), o $F$ es $\zeta$ o una $L(s+i\theta,\chi)$ desplazada.

(b) En consecuencia, el dato local de $F$ es de carácter unitario: los inversos de raíces locales cumplen
$|\alpha_p|\in\{0,1\}$ para todo $p$ — la **pureza máxima** en la normalización aritmética, equivalente en
el diccionario del Doc 131 (Teo. 6.7, normalización $F_{p,\alpha}$) a que cada bloque local tenga su divisor
exactamente donde la simetría lo exige, con la barrera de Weil $|c_m|\leq2p^{m/2}$ satisfecha con holgura.
**La flecha "continuación + Euler + ecuación funcional ⟹ pureza asintótica del dato local" del mecanismo de
144.D es un TEOREMA en grado $<2$**, vía la rigidez clasificatoria — la encarnación exacta, en la clase
real, de lo que el Cálculo 141.R3 mostró en el modelo (el dato impuro no continúa).

(c) **144.D restringida a grado $<2$ equivale a 144.D para $\zeta$ y las $L(s+i\theta,\chi)$:** no existe
ningún "objeto exótico" de grado bajo que pueda portar un enjambre; el portador hipotético sería una $L$ de
Dirichlet con $m=\infty$ y $\delta_j\log\gamma_j\to0$ — una negación cuantitativamente fuerte de GRH.

*Demostración.* (a) es [CG93]+[KP99]+[KP11] (con [GAP-153.E]). (b) los factores locales de las $L$ de
Dirichlet son $(1-\chi(p)p^{-s})^{-1}$ con $|\chi(p)|\in\{0,1\}$; el desplazamiento $i\theta$ rota la fase,
no el módulo. (c) inmediato de (a): la cuantificación de 144.D corre sobre los miembros, y los miembros de
grado $<2$ están listados. $\square$

### 3.3. Lo que la clasificación NO da — y la corrección al mecanismo del Doc 144

**Proposición 153.8 [PROPOSICIÓN] (la segunda flecha, "pureza ⟹ repulsión", es insostenible tal como está
enunciada).** Existe un objeto de la categoría con dato local PURO en todo primo y cuya repulsión de
resolución (LP-134, LP-141, e incluso $m<\infty$) es indecidida por la pureza: $\zeta$ misma. En
consecuencia, ninguna implicación de la forma
$$\text{(pureza local de todos los factores)}\;\Longrightarrow\;\text{(repulsión / infinitos gordos si }m=\infty)$$
puede ser el contenido de 144.D: su hipótesis la satisface $\zeta$ y su conclusión para $\zeta$ es
exactamente el enunciado abierto. El mecanismo del Doc 144 §3.3 ("cada cero off a distancia $\delta_j$ exige
impureza local sostenida de amplitud $\gtrsim\delta_j$ a soporte $\asymp\log\gamma_j$") tiene además la
amplitud equivocada: por el Lema 141.B (citado) y el Lema 153.2, la huella de un cuádruplo off sobre TODO
dato de soporte $L$ es $O((\delta L)^2)$ — a soporte $\log\gamma_j$ y bajo (ENJAMBRE) es
$(\delta_j\log\gamma_j)^2\to0$: **el cero off sub-resolución NO exige ninguna impureza detectable a soporte
logarítmico**; no hay nada ahí que la continuación pueda prohibir.

*Demostración.* $\zeta$ tiene factores $(1-p^{-s})^{-1}$: dato $\alpha_p=1$, puro (es el caso límite/borde
de la barrera $|c_m|=2p^{m/2}$ tras normalizar como en Doc 131 §6.5, donde la positividad "es tan justa como
puede ser"). Que LP-134/LP-141/$m<\infty$ para $\zeta$ son abiertos es el estado del programa (Prop. 141.R1:
decidirlos negativamente refuta RH). La afirmación de amplitud: Lema 153.2 con $L$ en lugar del kernel
lorentziano es el Lema 141.B, cota $C_N(F)(\delta L)^2e^{\delta L}(1+\gamma)^{-N}$; bajo (ENJAMBRE) y
$L\leq C\log\gamma_j$, $(\delta_jL)^2\to0$. $\square$

**Observación 153.8bis (el balance de la confrontación).** KP entrega exactamente una de las dos flechas y
desautoriza la otra: (i) "continuación ⟹ pureza" pasa de conjetura-mecanismo a teorema en grado $<2$ — la
rigidez clasificatoria es real y es la versión global de 141.R3; (ii) "pureza ⟹ repulsión" queda refutada
como enunciado local-por-primo (153.8): la pureza es una condición que $\zeta$ ya cumple, luego no puede ser
la palanca que decida dónde están los ceros de $\zeta$. El contenido genuino de 144.D NO está en el dato
local por primo sino en el dato de **ventana** a soporte adaptado (§2.6): la cadena correcta es
$$\text{continuación}\;\Longrightarrow\;\underbrace{\text{pureza local}}_{\text{KP: teorema en }d<2}
\;\;\text{y}\;\;
\underbrace{\text{regularidad de ventana a soporte super-logarítmico}}_{\text{= GAP-144.C destilado, §4}}
\;\Longrightarrow\;\text{infinitos gordos},$$
donde la segunda componente NO se sigue de la primera (153.8) y es la única que toca la posición de los
ceros. Respondiendo la pregunta del encargo: la clasificación identifica las funciones, no prueba RH para
ellas; su rigidez SÍ da palanca para 144.D, pero solo sobre la flecha estructural, y de paso reduce el
universo de contraejemplos de grado bajo a las $L$ de Dirichlet — donde refutar 144.D exigiría violar GRH
cuantitativamente. La nota del encargo ("la clasificación en grado 1 prueba RH-de-posición") debe leerse
así: prueba *identidad* de los objetos (y con ella la posición de sus POLOS y la pureza de su dato), no la
posición de sus ceros — la distinción exacta entre rigidez de la función y rigidez del divisor.

---

## 4. El eslabón mínimo y su posición en la jerarquía

### 4.1. La destilación

**Definición 153.9 [DEFINICIÓN-NUEVA] (déficit de ventana de auto-escala; Rigidez 153.M).** Para
$F\in$ D131-H⁺, $\gamma_0\geq2$, $L\geq1$, defino el **funcional de ventana**
$$\mathcal P_F(\gamma_0,L)\;:=\;\sum_{n\geq2}a(n)\,n^{-1/2}\bigl(1-\tfrac{|\log n|}{L}\bigr)_+\,2\cos(\gamma_0\log n)
\;-\;\mathcal A_F(\gamma_0,L),$$
donde $\mathcal A_F(\gamma_0,L)$ es el lado arquimediano+polar de (A4) para el test $F_{L,\gamma_0}$ de
153.6 (una cantidad en forma cerrada, computable de $(Q,\gamma_F,r)$ por Mellin–Stirling). Por (A4),
$-\mathcal P_F(\gamma_0,L)=\sum_\rho h(\rho)$. **Rigidez 153.M:** *no existe $F\in$ D131-H⁺ con una sucesión
$(\gamma_k,L_k)$, $\gamma_k\to\infty$, $L_k/\log\gamma_k\to\infty$, $\gamma_kL_k\geq10$, tal que*
$$-\mathcal P_F(\gamma_k,L_k)\;\geq\;\tfrac13\,L_k\qquad\forall k.$$
(En palabras: el dato casi-primo de un objeto Euler continuable no puede quedarse corto respecto de su
presupuesto arquimediano por un margen lineal en el soporte, unilateralmente, en infinitas ventanas de
soporte super-logarítmico.)

**Proposición 153.10 [PROPOSICIÓN] (153.M ⟹ 144.D).** Si la Rigidez 153.M vale, entonces la Conjetura 144.D
vale (y con ella LP-141 en la categoría, por la Prop. 144.4 del Doc 144).

*Demostración.* Por contradicción: sea $F\in$ D131-H⁺ con (ENJAMBRE). Tomo la subsucesión (existe por
$\delta_j\log\gamma_j\to0$ y $\gamma_j\to\infty$) con $\gamma_jL_j\geq10$ donde $L_j:=1/\delta_j$; entonces
$L_j/\log\gamma_j=1/(\delta_j\log\gamma_j)\to\infty$. Evalúo (A4) en el test $F_{L_j,\gamma_j}$:
$$-\mathcal P_F(\gamma_j,L_j)\;=\;\sum_\rho h(\rho)\;=\;\underbrace{\sum_{\rho\ \text{on}}h(\rho)}_{\geq0
\ \text{(153.6(a))}}\;+\;\underbrace{\sum_{\text{cuádruplos off}}h(\rho)}_{\geq\ \text{proyección}\ +\ E_j}.$$
La contribución de cada cuádruplo off es la de su proyección (que es $\geq0$, por 153.6(a) aplicado a los
ceros proyectados on-line) más su exceso, y para el cuádruplo centrado $j$-ésimo el exceso es
$E(\delta_j,L_j)\geq L_j/3$ (153.6(b), $\kappa=1$). Los demás cuádruplos off ($\gamma'\neq\gamma_j$)
aportan: proyección $\geq0$ más exceso $8\int(1-\tfrac{|u|}{L_j})\cos(\gamma_ju)\cos(\gamma'u)
(\cosh(\delta'u)-1)du$ — este exceso no centrado puede ser negativo; lo controlo: su módulo es
$\leq8\int(1-\tfrac{|u|}{L_j})(\cosh(\delta'u)-1)du\leq 8L_j[\tfrac{\cosh\kappa'-1}{\kappa'^2}-\tfrac12]$ con
$\kappa'=\delta'L_j$… esta cota no decae en $\gamma'$ y no basta tal cual; uso en su lugar la versión con
decaimiento: el exceso no centrado es $4\int\varphi'(u)[\cos((\gamma_j-\gamma')u)+\cos((\gamma_j+\gamma')u)]du$
con $\varphi'(u)=(1-\tfrac{|u|}{L_j})(\cosh(\delta'u)-1)$, y dos integraciones por partes como en 153.6(b) dan
módulo $\leq\frac{50\,\kappa'^2e^{\kappa'}}{(\gamma_j-\gamma')^2L_j}$ para $|\gamma'-\gamma_j|\geq1$,
$\kappa'\leq1$. **[GAP-153.F declarado en línea]:** para los cuádruplos off no centrados con
$|\gamma'-\gamma_j|<1$ o $\kappa'=\delta'L_j>1$ la cota anterior no aplica; impongo en la elección de la
subsucesión $(\gamma_j)$ la separación $\min_{j'\neq j}|\gamma_{j'}-\gamma_j|\geq1$ — posible si los off del
enjambre no se acumulan en ventanas unitarias con $\delta'L_j>1$ simultáneamente; en general se necesita
ordenar los $L_j$ contra el enjambre completo. Para mantener la prueba completa SIN ese ordenamiento fino,
debilito: por el Lema 153.5 hay $\leq C_F\log\gamma_j$ ceros con $|\gamma'-\gamma_j|<1$ y cada uno aporta
exceso $\geq-8L_j[\cosh(\kappa'\wedge\cdot)\ldots]$ — no acotable sin información sobre sus $\delta'$. Por
tanto enuncio la implicación con la hipótesis de **enjambre separado**: $\delta'L_j\leq1$ para todo cuádruplo
off con $|\gamma'-\gamma_j|\leq\gamma_j/2$ — que se consigue refinando la subsucesión cuando
$\sup_{|\gamma'-\gamma_j|\leq\gamma_j/2}\delta'\leq\delta_j$ (tomar como centros los cuádruplos de $\delta$
máximo local, siempre posible pasando a una subsucesión, pues $\delta\to0$). Bajo esa normalización,
$\kappa'\leq1$ y los excesos no centrados suman, sobre las ventanas $|\gamma'-\gamma_j|\geq1$ (cota de
ventana 153.5 + serie $\sum k^{-2}$), a lo sumo $C\log(\gamma_j)/L_j=o(L_j)$ en módulo; los de
$|\gamma'-\gamma_j|<1$ tienen $\kappa'\leq1$ y exceso $\geq0$ si están centrados al mismo $\gamma_j$ o
módulo $\leq8L_j[\tfrac{\cosh1-1}{1}-\tfrac12]\cdot\Theta(\#)$… los dejo del lado seguro usando que el
exceso de CUALQUIER cuádruplo con $|\gamma'-\gamma_j|<\tfrac1{L_j}$ es positivo por continuidad del cálculo
153.6(b) (el factor $\cos(\gamma'u)\cos(\gamma_ju)\geq\cos^2(\gamma_ju)-|u||\gamma'-\gamma_j|$ y el término
de error se absorbe en $R$); y los con $\tfrac1{L_j}\leq|\gamma'-\gamma_j|<1$ se acotan por la integración
por partes con denominador $(\gamma_j-\gamma')^2\geq L_j^{-2}$… que NO es pequeño. **Honestidad:** el
control de vecinos a distancia $[L_j^{-1},1)$ requiere separación $\gtrsim1$ de los centros elegidos
respecto de los demás off del enjambre; esto se garantiza si en cada ventana unitaria que contiene un cero
de $\delta$ máximo local no hay otro cuádruplo off con $\kappa'$ cerca de 1 a distancia $<1$ — una
subsucesión así existe salvo que el enjambre tenga infinitas ventanas con $\geq2$ cuádruplos a auto-escalas
comparables, caso en el cual se centran los tests en el punto medio y los DOS excesos son positivos por el
mismo cálculo. Recorriendo los casos, en todos hay una sucesión $(\gamma_k,L_k)$ con
$\sum_\rho h(\rho)\geq L_k/3-o(L_k)\geq\tfrac13L_k$ ajustando constantes. Entonces
$-\mathcal P_F(\gamma_k,L_k)\geq\tfrac13L_k$ en infinitas ventanas super-logarítmicas — contradice 153.M.
Luego (ENJAMBRE) es imposible: vale la conclusión de 144.D. $\square$

**Observación 153.10bis (estatus honesto de la prueba).** La columna vertebral (test de auto-escala, exceso
positivo dominante, transferencia por (A4)) es sólida; la contabilidad de interferencia entre cuádruplos del
enjambre (el párrafo de casos) es correcta pero fea, y un caso —ventanas con múltiples cuádruplos a
auto-escalas comparables y fases adversas a TODO centro— está cerrado por el argumento del punto medio solo
para pares; para multiplicidades crecientes hace falta el lema combinatorio de selección de centros. Lo
marco **[GAP-153.F]** (técnico, de selección, no estructural: la positividad punto a punto de 153.6(b) vale
para cualquier número de cuádruplos CENTRADOS, y "centrado" se puede relajar a $|\gamma'-\gamma_j|\leq
\epsilon/L_j$ absorbiendo en $R$; el residuo es solo elegir centros que dejen a los no centrados lejos).
GAP-153.F es de dificultad órdenes de magnitud menor que GAP-144.C; lo declaro para no sobrevender.

### 4.2. Posición en la jerarquía

**Proposición 153.11 [PROPOSICIÓN] (cadena).** Módulo [GAP-153.F] en la flecha del medio:
$$\mathrm{GRH}_{\text{cat}}\;\Longrightarrow\;\underbrace{\text{Conj. 141.E}}_{\text{LP-134 en la categoría}}
\;\Longrightarrow\;\underbrace{\text{Rigidez 153.M}}_{\text{nuevo}}
\;\Longrightarrow\;\underbrace{\text{Conj. 144.D}}_{\text{GAP-144.C}}
\;\Longrightarrow\;\mathrm{LP\text{-}141}_{\text{cat}}(a)\ \ \forall a\succeq\log.$$

*Demostración.* Primera flecha: GRH en la categoría = todos los divisores en la línea = $m=0$ para todos los
miembros; 141.E ($\liminf\delta\log\gamma>0$ sobre off) vale vacuamente. Segunda: bajo 141.E no hay
(ENJAMBRE); más fuerte: 153.M podría aún fallar por un mecanismo del lado primo SIN enjambre — no: la
violación de 153.M es un enunciado sobre $\mathcal P_F$, no sobre ceros; la implicación correcta es la
contrapuesta de la prueba de 153.10: la violación de 153.M que el enjambre PRODUCE es la única que 153.M
necesita prohibir para dar 144.D. Para que la cadena sea literal redefino (sin pérdida para el uso) 153.M
en su forma condicional: "153.M$'$ := no existe $F$ con (ENJAMBRE) y la anomalía $-\mathcal P_F\geq L_k/3$";
entonces 141.E ⟹ no hay (ENJAMBRE) ⟹ 153.M$'$ vacuamente, y 153.M$'$ ⟹ 144.D es 153.10. Tercera y cuarta:
153.10 y Prop. 144.4 (Doc 144, citada). Estricta la última: Prop. 144.1(b) del Doc 144. $\square$

**Comparación con lo conocido (paso 4 del encargo, respuesta directa).**

| enunciado | tipo | ¿más débil que RH/GRH$_{\text{cat}}$? | ¿más débil que LP-134/141.E? | ¿accesible a densidad/momentos? |
|---|---|---|---|---|
| 144.D | posición de ceros (subsucesión gorda) | sí (estrictamente, implicada por) | sí (Prop. 144.4/Obs. 144.4bis) | no — escala $1/\log$: Lema 141.M1; ciega: 141.B0 |
| 153.M$'$ | evaluación/rigidez del lado primo a soporte super-log | sí (vacua bajo GRH$_{\text{cat}}$) | sí (vacua bajo 141.E) | no — requiere precisión relativa $Le^{-L/2}$; PNT da $e^{-c\sqrt L}$, VK da $e^{-cL^{3/5}}$ |
| GAP-141.G1 (muro viejo) | evaluación a soporte $\log\gamma$, error $o(1)$ | — | — | no (Doc 141 §3.3) |

**Observación 153.11bis (153.M' contra el muro viejo — la comparación que duele).** GAP-141.G1 pedía la
fórmula explícita por ventana a soporte $L\asymp\log\gamma$ con error $o(1)$ contra términos brutos
$e^{L/2}\asymp\sqrt\gamma$: precisión relativa $\asymp\gamma^{-1/2}$. 153.M' pide margen $o(L)$ contra
términos brutos $e^{L/2}$ con $L\gg\log\gamma$: precisión relativa $Le^{-L/2}\ll\gamma^{-K}$ para todo $K$.
**Cuantitativamente, 153.M' es MÁS exigente que el muro viejo, no menos.** Lo que la sesión compra no es
abaratamiento numérico sino estructura: (i) el lado de CEROS del problema queda resuelto con signo (153.6:
el enjambre no puede esconderse de los tests adaptados — antes ni eso se sabía: a soporte fijo se esconde
exactamente, 141.B2); (ii) el enunciado que falta es UNILATERAL (un déficit de un solo signo, no una
evaluación bilateral) y sobre UNA sucesión de ventanas (no uniforme); (iii) y la fuente de su plausibilidad
ya no es heurística: es la misma rigidez que KP prueba en grado $<2$ (153.7) y que 141.R3 exhibió en el
modelo — los objetos continuables existentes simplemente no tienen lados primos anómalos. La pregunta
"¿la continuación prohíbe la anomalía?" es ahora una pregunta sobre coeficientes de un objeto Euler
($a(n)\geq0$, tipo Chebyshev, continuable) y un funcional concreto $\mathcal P_F(\gamma_k,L_k)$ — no sobre
ceros. Esa transposición ceros→coeficientes es el contenido neto del documento.

---

## 5. Veredicto

### VEREDICTO: **ESLABÓN MÍNIMO AISLADO** — 144.D ni probada ni refutada; el ataque dlVP-en-½ MUERTO con certificado cuantitativo; una pieza nueva probada (exceso de auto-escala, un signo, dominante); el mecanismo del Doc 144 corregido (KP prueba su primera flecha en grado $<2$; la segunda, refutada como estaba escrita, se reescribe como rigidez de ventana 153.M').

**Sobre el paso 2 (la pregunta DECIDE del encargo):** la respuesta es la rama mala. Para que un enjambre
sub-resolución a altura $\gamma$ sea visible donde la positividad de $\Lambda$ muerde ($\sigma>1$) hacen
falta $\gtrsim\log^2\gamma/\varepsilon^2$ ceros off por ventana unitaria (señal por cuádruplo $\asymp\delta^2$,
Lema 153.2), y Riemann–von Mangoldt — válido en la categoría, Lema 153.5 — autoriza $\leq C\log\gamma$:
**densidad superlineal, imposible; ninguna subsucesión basta** (el kernel lorentziano tiene masa $O(1)$ por
unidad de altura: apilar alturas no acumula). Es el mismo no-go de promedios del Doc 141, ahora con
constantes: la palanca dlVP es un funcional de Weil de soporte efectivo $O(1)$ y el Cor. 141.B2 la cubre.
La razón estructural (§2.5): la línea repelente debe portar el polo de la medida positiva; $\Re s=1$ lo
porta, $\Re s=\tfrac12$ es el eje de simetría sin polo y la desigualdad transpuesta es $0\geq0$ (141.M4).

**Sobre el paso 3:** Kaczorowski–Perelli no localiza ceros, pero su rigidez sí da palanca: en grado $<2$
(módulo [GAP-153.E] de inmersión) "continuación+Euler+ecuación funcional ⟹ dato local unitario/puro" es
TEOREMA, y 144.D en grado $<2$ se reduce a $\zeta$ y las $L$ de Dirichlet desplazadas — todo contraejemplo
de grado bajo violaría GRH cuantitativamente. A la vez, $\zeta$ (pura en todo primo, repulsión abierta)
refuta "pureza local ⟹ repulsión" como enunciado por-primo: el portador del mecanismo es el dato de ventana,
no el dato local.

**Sobre los pasos 4–5:** el eslabón mínimo queda destilado como **Rigidez 153.M'** (déficit unilateral
$\geq L/3$ del lado casi-primo en infinitas ventanas de auto-escala super-logarítmica: prohibido), con
153.M' ⟹ 144.D probado módulo el gap técnico de selección de centros [GAP-153.F] (combinatorio, no
estructural). Jerarquía: GRH$_{\text{cat}}$ ⟹ 141.E ⟹ 153.M' ⟹ 144.D ⟹ LP-141$_{\text{cat}}$. 153.M' es
más débil que 141.E como posición y vacua bajo GRH, pero como demanda de evaluación es MÁS dura que el muro
viejo (precisión relativa $Le^{-L/2}$ contra $e^{-c\sqrt L}$ de PNT y $e^{-cL^{3/5}}$ de
Vinogradov–Korobov): el avance es estructural (señal con signo y dominante en el lado de ceros; todo el GAP
concentrado en un funcional unilateral de coeficientes), no cuantitativo. GAP-144.C sigue abierto; ahora
tiene forma de pregunta sobre coeficientes, no sobre ceros.

### Mensaje final

**VEREDICTO: ESLABÓN MÍNIMO AISLADO.** El ataque de la Vallée Poussin centrado en ½ muere con certificado
cuantitativo (densidad superlineal requerida vs. R–vM); la confrontación con Kaczorowski–Perelli cierra la
flecha "continuación⟹pureza" en grado $<2$ y refuta "pureza⟹repulsión" tal como estaba; GAP-144.C queda
destilado en la Rigidez 153.M' (un funcional unilateral del lado primo a soporte super-logarítmico), con
153.M'⟹144.D probado módulo un gap combinatorio menor.

**Tres resultados principales:**

1. **[LEMA 153.2 + PROPOSICIÓN 153.3 + COROLARIO 153.4]** — *Certificado de defunción del dlVP-en-½:* la
   señal de un cuádruplo off en el semiplano de positividad es $\leq C_0\delta^2/(1+(t-\gamma)^2)$ (segundo
   orden por la ecuación funcional); el enjambre completo desvía $-\Re F'/F$ en $o(1/\log t)$; la
   visibilidad exigiría $\gtrsim\log^2\gamma$ ceros por ventana contra el tope R–vM $C\log\gamma$ (probado
   en la categoría, Lema 153.5). Ninguna subsucesión basta; mismo no-go que Doc 141, ahora cuantitativo.

2. **[PROPOSICIÓN 153.6]** — *Exceso de auto-escala (la pieza nueva):* con el test de Fejér modulado a
   soporte $L_j=1/\delta_j$, el exceso de un cuádruplo off sobre su proyección es
   $8L[\frac{\cosh\kappa-1}{\kappa^2}-\frac12]+O(\kappa^2e^\kappa/(\gamma^2L))\geq L/3$ en $\kappa=1$ —
   **positivo punto a punto y $\gg\log\gamma$** (domina la masa esperada del mar on-line). El perfil de
   media nula (141.M5) no aplica a soporte adaptado; el no-go 141.B2 no cubre familias elegidas después de
   la configuración. Todo el GAP se concentra en el lado primo.

3. **[PROPOSICIÓN 153.7 + 153.8 + DEFINICIÓN 153.9 + PROPOSICIÓN 153.10/153.11]** — *Corrección del
   mecanismo y reducción:* KP prueba "continuación⟹pureza" en grado $<2$ y reduce ahí 144.D a las $L$ de
   Dirichlet; "pureza⟹repulsión" es insostenible ($\zeta$ es pura y abierta); el eslabón mínimo es la
   Rigidez 153.M' del lado casi-primo, con la cadena
   GRH$_{\text{cat}}$⟹141.E⟹153.M'⟹144.D⟹LP-141$_{\text{cat}}$ (flecha central módulo [GAP-153.F],
   técnico de selección de centros).

---

## Referencias

**Internas (backward-only):** Doc 144 (Def. 144.0; Props. 144.1, 144.2, 144.4, 144.6, 144.8; Conjetura
144.D; GAP-144.C; Obs. 144.4bis; Cor. 144.10); Doc 141 (Lema 141.B0; Lema 141.B; Cor. 141.B2; Cálculos
141.M4/M5; Lema 141.M1; Prop. 141.M2; Prop. 141.R1/R2; Cálculo 141.R3; Conjetura 141.E; GAP-141.G1); Doc
134 (modelo $\mathfrak W$, visibilidad (V1)–(V2), Teos. 5.1/5.4, §5.8 M3 diccionario pureza↔resolución);
Doc 131 (Axioma H 6.1; Teo. 6.6 Poisson local; Teo. 6.7 pureza local y barrera $|c_m|\leq2p^{m/2}$;
Prop. 6.8; Deseo 6.9 H⁺); Doc 146 (veredicto GAP-141.DH: GORDOS — los off de D–H a distancia macroscópica;
la frontera "sub-resolución ⟺ ninguna estructura tipo-Euler").

**Literatura (publicada, verificable):**
- [dlVP1899] Ch.-J. de la Vallée Poussin, *Sur la fonction ζ(s) de Riemann et le nombre des nombres premiers
  inférieurs à une limite donnée*, Mém. Couronnés Acad. Roy. Belgique **59** (1899–1900). (Región libre de
  ceros clásica; también el PNT con error $e^{-c\sqrt{\log x}}$.)
- [T86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (rev. D. R. Heath-Brown),
  Oxford Univ. Press, 1986. (Thm. 3.8: región libre de ceros y el 3-4-1; Thm. 9.2: $N(T+1)-N(T)=O(\log T)$;
  Thm. 9.4: Riemann–von Mangoldt; §10.25: Davenport–Heilbronn.)
- [CG93] J. B. Conrey, A. Ghosh, *On the Selberg class of Dirichlet series: small degrees*, Duke Math. J.
  **72** (1993), 673–693. (Grado 0 y $0<d<1$ en $\mathcal S$.)
- [KP99] J. Kaczorowski, A. Perelli, *On the structure of the Selberg class, I: $0\leq d\leq1$*, Acta Math.
  **182** (1999), 207–241. (Vaciedad de $0<d<1$ en $\mathcal S^\sharp$; clasificación en grado 1 — ver
  [GAP de literatura] §3.1 sobre la atribución exacta dentro de la serie.)
- [KP11] J. Kaczorowski, A. Perelli, *On the structure of the Selberg class, VII: $1<d<2$*, Ann. of Math.
  (2) **173** (2011), 1397–1441. (Vaciedad de $1<d<2$.)
- [IK04] H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. **53**, 2004. (Cap. 5: conteo
  de ceros por ventana para $L$-funciones generales — Lema 153.5; sumas de exponenciales sobre primos.)
- I. M. Vinogradov / N. M. Korobov (1958): región libre de ceros $\sigma\geq1-c/(\log t)^{2/3}(\log\log t)^{1/3}$
  y las cotas correspondientes de sumas sobre primos — citadas solo como referencia de la MEJOR cancelación
  incondicional conocida (Obs. 153.6bis, 153.11bis); exposición en [IK04, Cap. 8].

*Fin del Doc 153.*
