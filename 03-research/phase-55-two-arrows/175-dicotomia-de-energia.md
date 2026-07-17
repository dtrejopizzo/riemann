# Documento 175 — La dicotomía de energía: LP-112 ⟹ I ∈ {0, ∞}

**Programa:** Hipótesis de Riemann — Fase 55 (dos flechas)
**Fecha:** 2026-06-11
**Mandato:** formalizar y probar la dicotomía de energía — que la auto-aproximación de ζ (LP-112) fuerza $I\in\{0,\infty\}$ —, cuantificando la réplica de Rouché–Hurwitz (la réplica copia la *distancia a la línea*, no solo el cero); explorar el puente densidad-de-replicación ↔ Teorema 170.5; estado honesto de LP-112; retrato del estado de energía finita.
**Prerrequisitos leídos en fuente:** Doc 112 completo (LP-112, LP-112⁻, Teorema 2.3, Prop. 2.6, Obs. 2.4, §2.6), Doc 113 (LP-112 contra literatura; Bohr 1922; soporte de Bagchi), Doc 170 (coordenadas, Teorema 170.5, Cor. 170.6, Thm 170.8, §5 envolvente), Doc 172 (cabecera, veredicto: la envolvente $T/\log T$ = suelo de ruido).
**Contrato:** [DEFINICIÓN-NUEVA] libre; [TEOREMA]/[PROP]/[LEMA] prueba completa o sin etiqueta; [GAP] declarado con forma de enunciado. Falsa victoria peor que fracaso.

**Coordenadas (idénticas al Doc 170).** Cero off-crítico $\rho=\tfrac12+b+i\gamma$ con $b\in(0,\tfrac12)$, $\gamma>0$; un representante por cuádruplo $\{\rho,\bar\rho,1-\rho,1-\bar\rho\}$ (el del semiplano superior derecho). Energía:
$$I \;=\; I(0^+)\;:=\;\sum_j b_j^2,\qquad E(T):=\sum_{\gamma_j\le T} b_j^2 .$$
$I=0$ ⟺ no hay ceros off ⟺ RH. $N(\sigma,T)$ = nº de ceros con $\beta\ge\sigma$, $0<\gamma\le T$. Nota: todo cero tiene $\beta<1$ (Hadamard–de la Vallée Poussin), luego $b\in(0,\tfrac12)$ estrictamente y siempre hay holgura a ambos lados dentro de la franja abierta $\{\tfrac12<\sigma<1\}$.

---

## 0. Resumen ejecutivo y veredicto

**EL TEOREMA QUEDÓ PROBADO** (condicional a LP-112, declarado como tal):

1. **[TEOREMA 175.2]** LP-112 ⟹ $I\in\{0,\infty\}$. Más fuerte: basta la versión débil LP-112⁻ (un solo $\tau$ por cada $(D,\varepsilon)$), vía una inducción de radios sumables ([COR 175.4]); y basta **precisión fija** $\varepsilon<\eta$ (no hace falta $\varepsilon_k\to0$) en **un solo disco** (el del cero off) ([Obs. 175.3]). El mecanismo: la réplica de Rouché–Hurwitz copia la abscisa con error $\le\delta(\varepsilon)\le C\varepsilon^{1/m_0}\to0$ ([LEMA 175.1], cuantificado con multiplicidad), luego cada réplica aporta $b^2\ge b_0^2/4$ a la energía y la suma diverge.
2. **Nueva arquitectura (mejora estricta de P44/D112):** $\mathrm{RH}\;\Longleftarrow\;\bigl(I(0^+)<\infty\bigr)\;\wedge\;\mathrm{LP\text{-}112}$. Es estrictamente más débil que la vieja $(m<\infty)\wedge$LP-112 porque $m<\infty\Rightarrow I<\infty$ y el recíproco es falso ($b_j=1/j$ da $m=\infty$, $I<\infty$). Además la dicotomía de energía **implica** la dicotomía de cardinal (D-109): $I\in\{0,\infty\}\Rightarrow m\in\{0,\infty\}$.
3. **[TEOREMA 175.6] (incondicional, el puente nuevo):** si ζ tiene un cero off $\rho_0$ con abscisa $\tfrac12+b_0$, el conjunto $A_\varepsilon$ de shifts de auto-aproximación buenos en el disco del cero satisface, para todo $\varepsilon<\eta$,
$$\mathrm{meas}\bigl(A_\varepsilon\cap[0,T]\bigr)\;\ll\; r\,T^{1-b_0/8}\log T \quad\text{y}\quad \mathrm{meas}\bigl(A_\varepsilon\cap[0,T]\bigr)\;\le\;\frac{8r}{b_0^2}\,E(T+\gamma_0+r)\;\ll\;\frac{r}{b_0^2}\cdot\frac{T}{\log T}.$$
Esto **mejora la Prop. 2.6 del Doc 112** (densidad cero sin tasa, vía el teorema límite de Bagchi) a una tasa explícita e incondicional con prueba elemental (Rouché + densidad de Selberg, sin maquinaria distribucional). Lectura: *la auto-aproximación de un ζ con cero off es rara con tasa cuantificada* — el certificado de energía YA limita la teoría de universalidad. La identidad estructural: **$E(T)$ cuenta testigos de auto-aproximación**: todo conjunto $2r$-separado de shifts buenos tiene $\#\le 4E(T)/b_0^2$.
4. **[PROP 175.8] (estado de energía finita):** si $0<I<\infty$, los testigos buenos de CUALQUIER cero off forman un conjunto de **medida total finita** ($\le 8rI/b_0^2$ en todo $(0,\infty)$) con a lo sumo $4I/b_0^2$ elementos separados: el mundo de energía finita es *anti-recurrente* en la ventana de cada cero off, incluso a precisión fija. $I$ es literalmente un **presupuesto de testigos**.
5. **LP-112 sigue siendo el único gap** y este documento lo *agrava cuantitativamente* (§4): sus testigos, bajo ¬RH, no solo tienen densidad cero — tienen densidad $\ll T^{-b_0/8}\log T$. El muro de D112/D113 (producir un elemento de un conjunto excepcional) queda intacto y más afilado.

---

## 1. LP-112: el enunciado preciso, con el disco donde se necesita

Reproducimos las dos versiones del Doc 112 §2.2 y aislamos la instancia mínima que este documento usa.

**Lema LP-112 (casi-periodicidad puntual secuencial; ABIERTO — Doc 112).** *Para todo disco cerrado $D\subset\{\tfrac12<\sigma<1\}$ existe una sucesión $\tau_k\to\infty$ tal que*
$$\sup_{s\in D}\,\bigl|\zeta(s+i\tau_k)-\zeta(s)\bigr|\;\longrightarrow\;0.$$

**Lema LP-112⁻ (versión débil — Doc 112).** *Para todo disco cerrado $D\subset\{\tfrac12<\sigma<1\}$ y todo $\varepsilon>0$ existe UN $\tau>\mathrm{altura}(D)$ con $\sup_D|\zeta(s+i\tau)-\zeta(s)|<\varepsilon$.*

**Tres precisiones sobre el disco (la honestidad pedida):**

(a) *El cuantificador del Doc 112 ya cubre la altura del cero.* LP-112 cuantifica sobre **todos** los discos cerrados de la franja abierta, sin restricción de altura: en particular sobre $D=\bar D(\rho_0,r)$ centrado en un cero off $\rho_0$ a altura $\gamma_0$ arbitraria. No hay que reformular nada: la versión que usamos es una *instancia* de la del Doc 112, no una extensión. (Si $\rho_0$ cayera en el borde de un disco dado, se reemplaza por el disco concéntrico en $\rho_0$ de radio admisible: la franja es abierta y $0<b_0<\tfrac12$ estricto deja holgura por los dos lados.)

(b) *La instancia mínima.* Todo lo que el Teorema 175.2 necesita es:

**[DEFINICIÓN-NUEVA] LP-112[$\rho_0$] (instancia localizada a precisión fija).** Para el disco $D_0:=\bar D(\rho_0,r)$ del §2 (radio $r=r(\rho_0)$ fijado abajo) y para UN $\varepsilon<\eta(r)$ fijo, existe una sucesión **no acotada** $\{\tau_k\}$ con $\sup_{D_0}|\zeta(s+i\tau_k)-\zeta(s)|\le\varepsilon$.

LP-112 ⟹ LP-112[$\rho_0$] trivialmente; LP-112⁻ ⟹ (la conclusión de) LP-112[$\rho_0$] solo tras la inducción del Corolario 175.4 — la versión débil da un $\tau$ por disco, y la no-acotación se recupera cambiando de disco en cada paso.

(c) *Lo delicado es exactamente que $D_0$ contiene un cero del target* (§4): si $D$ no contiene ceros de ζ, LP-112 en $D$ es consecuencia de RH (Bagchi) y, bajo ¬RH, sigue siendo el caso "genérico-amigable"; con un cero dentro, el target sale del soporte de la medida de Bagchi y todo lo distribucional juega EN CONTRA (Prop. 2.6 del D112; aquí Teorema 175.6, con tasa).

---

## 2. El teorema de dicotomía de energía, cuantificado

### 2.1. Rouché–Hurwitz con tasas y multiplicidad

**[LEMA 175.1] (réplica con tasa).** Sea $g$ holomorfa en un entorno de $\bar D(z_0,R)$, con un cero de multiplicidad $m_0\ge1$ en $z_0$ y sin otros ceros en $\bar D(z_0,R)$. Para $0<\delta\le R$ sea
$$\eta(\delta)\;:=\;\min_{|z-z_0|=\delta}|g(z)|\;>\;0 .$$
Entonces:

(i) *(Rouché en el radio $\delta$)* Si $f$ es holomorfa en $\bar D(z_0,R)$ y $\sup_{\bar D(z_0,R)}|f-g|<\eta(\delta)$, entonces $f$ tiene **exactamente $m_0$ ceros** (con multiplicidad) en $D(z_0,\delta)$; en particular al menos un cero $z'$ con $|z'-z_0|<\delta$.

(ii) *(tasa explícita)* Escríbase $g(z)=c\,(z-z_0)^{m_0}h(z)$ con $c=g^{(m_0)}(z_0)/m_0!\ne0$, $h(z_0)=1$. Existe $\delta_1\in(0,R]$ con $|h|\ge\tfrac12$ en $\bar D(z_0,\delta_1)$, y entonces $\eta(\delta)\ge\tfrac{|c|}{2}\delta^{m_0}$ para $\delta\le\delta_1$. Definiendo
$$\delta(\varepsilon)\;:=\;\Bigl(\frac{4\varepsilon}{|c|}\Bigr)^{1/m_0},$$
para todo $\varepsilon\le\tfrac{|c|}{4}\delta_1^{m_0}$ y toda $f$ con $\sup_{\bar D(z_0,R)}|f-g|\le\varepsilon$, $f$ tiene exactamente $m_0$ ceros en $D\bigl(z_0,\delta(\varepsilon)\bigr)$. La réplica está a distancia $\le\delta(\varepsilon)=C\varepsilon^{1/m_0}\to0$ cuando $\varepsilon\to0$.

*Demostración.* (i): en el círculo $|z-z_0|=\delta$ se tiene $|f-g|\le\sup_{\bar D(z_0,R)}|f-g|<\eta(\delta)=\min_{|z-z_0|=\delta}|g|\le|g|$; el teorema de Rouché ([T39, §3.42]; [C78, VIII.3]) aplicado al par $(g,\,f-g)$ en ese círculo da que $f=g+(f-g)$ tiene en $D(z_0,\delta)$ el mismo número de ceros con multiplicidad que $g$, esto es $m_0$ (el cero $z_0$ contado $m_0$ veces; no hay otros por hipótesis). (ii): $h:=g/(c(z-z_0)^{m_0})$ se extiende holomorfa con $h(z_0)=1$; por continuidad existe $\delta_1$ con $|h|\ge\tfrac12$ en $\bar D(z_0,\delta_1)$, de donde $|g(z)|\ge\tfrac{|c|}{2}\delta^{m_0}$ en $|z-z_0|=\delta\le\delta_1$. Con $\varepsilon\le\tfrac{|c|}{4}\delta_1^{m_0}$ se tiene $\delta(\varepsilon)\le\delta_1$ y $\eta(\delta(\varepsilon))\ge\tfrac{|c|}{2}\cdot\frac{4\varepsilon}{|c|}=2\varepsilon>\varepsilon$, y aplica (i). $\square$

Este es el teorema de Hurwitz ([C78, VII.2.5]) en forma cuantitativa: los ceros del límite atraen ceros de las aproximantes, con multiplicidad, a velocidad $\varepsilon^{1/m_0}$. La multiplicidad $m_0\ge1$ no estorba: solo ralentiza la tasa, y para la dicotomía basta $\delta(\varepsilon)\le r$ — ni siquiera se necesita la tasa, solo el radio fijo (Obs. 175.3).

### 2.2. El teorema

Fijamos, para un cero off $\rho_0=\tfrac12+b_0+i\gamma_0$ ($b_0\in(0,\tfrac12)$, $\gamma_0>0$), las **constantes del cero**:
$$r\;:=\;\tfrac12\min\Bigl(b_0,\;\tfrac12-b_0,\;\mathrm{dist}\bigl(\rho_0,\,Z(\zeta)\setminus\{\rho_0\}\bigr)\Bigr)\;>\;0,\qquad D_0:=\bar D(\rho_0,r),\qquad \eta:=\eta(r)=\min_{|s-\rho_0|=r}|\zeta(s)|>0.$$
($r>0$ porque los ceros de ζ son aislados; $D_0\subset\{\tfrac12+\tfrac{b_0}2<\sigma<1\}$ porque $r\le b_0/2$ y $r\le\tfrac12(\tfrac12-b_0)$, y $\beta_0=\tfrac12+b_0<1$; ζ no se anula en $D_0\setminus\{\rho_0\}$.) Nótese: **no se asume ninguna finitud** — a diferencia del Teorema 2.3 del D112, que congelaba las constantes con H(m), aquí las constantes son las de UN cero, y un cero existe en cuanto $I>0$. Es la razón por la que la dicotomía de energía es más limpia que la de cardinal.

**[TEOREMA 175.2] (dicotomía de energía).** *Si vale LP-112 (basta su instancia en el disco $D_0$ de un solo cero off), entonces*
$$I(0^+)\;>\;0\;\Longrightarrow\;I(0^+)\;=\;\infty.$$
*Equivalentemente: LP-112 ⟹ $I\in\{0,\infty\}$.*

*Demostración.* Supóngase $I>0$: existe un cero off; fíjese uno, $\rho_0$, con sus constantes $(r,\eta,m_0,c)$ como arriba, donde $m_0$ es la multiplicidad de $\rho_0$ y $c=\zeta^{(m_0)}(\rho_0)/m_0!$. Aplíquese LP-112 al disco $D_0$: existe $\tau_k\to\infty$ con
$$\varepsilon_k\;:=\;\sup_{s\in D_0}\bigl|\zeta(s+i\tau_k)-\zeta(s)\bigr|\;\longrightarrow\;0 .$$

**Paso 1 (réplica con abscisa controlada).** Sea $k_0$ tal que $\varepsilon_k<\eta$ para $k\ge k_0$. Por el Lema 175.1(i) con $g=\zeta|_{D_0}$, $f=\zeta(\cdot+i\tau_k)|_{D_0}$ y $\delta=R=r$: $\zeta(\cdot+i\tau_k)$ tiene exactamente $m_0$ ceros en $D(\rho_0,r)$; equivalentemente, ζ tiene $m_0$ ceros (con multiplicidad) en $D(\rho_0+i\tau_k,\,r)$. Elíjase uno, $\rho_k$. Entonces
$$\bigl|\operatorname{Re}\rho_k-(\tfrac12+b_0)\bigr|\;<\;r\;\le\;\tfrac{b_0}2\qquad\Longrightarrow\qquad b(\rho_k)\;:=\;\operatorname{Re}\rho_k-\tfrac12\;\in\;\bigl(\tfrac{b_0}2,\,\tfrac{3b_0}2\bigr),$$
es decir $\rho_k$ es un cero off con $b(\rho_k)\ge b_0/2$. Más fino, por el Lema 175.1(ii): para $k$ grande ($\varepsilon_k\le\tfrac{|c|}4\delta_1^{m_0}$),
$$\bigl|\rho_k-(\rho_0+i\tau_k)\bigr|\;\le\;\delta(\varepsilon_k)\;=\;\Bigl(\tfrac{4\varepsilon_k}{|c|}\Bigr)^{1/m_0}\;\longrightarrow\;0,\qquad\text{en particular}\qquad b(\rho_k)\;\longrightarrow\;b_0 .$$
**La réplica copia la distancia a la línea crítica con error $O(\varepsilon_k^{1/m_0})\to0$** — la observación del director, ahora cuantificada. (Para la divergencia de la energía basta la versión gruesa $b(\rho_k)\ge b_0/2$, que ya vale con el radio fijo $r$.)

**Paso 2 (las réplicas son cuádruplos distintos).** $\tau_k\to\infty$ no trae cota inferior de separación, y no hace falta: pásese a la subsucesión definida inductivamente por $\tau_{k_{j+1}}:=\min\{\tau_k>\tau_{k_j}+2r+1\}$ (existe porque $\tau_k\to\infty$; reetiquétese). Entonces los intervalos $\bigl(\gamma_0+\tau_j-r,\;\gamma_0+\tau_j+r\bigr)$, que contienen $\operatorname{Im}\rho_j$, son disjuntos dos a dos y están por encima de $\gamma_0$ (para $\tau_j>r$). Dos miembros de un mismo cuádruplo en el semiplano superior ($\rho$ y $1-\bar\rho$) tienen la **misma** parte imaginaria; partes imaginarias en intervalos disjuntos fuerzan cuádruplos distintos, y todos distintos del cuádruplo de $\rho_0$.

**Paso 3 (la energía diverge).** Cada cuádruplo de réplica aporta a $I$ el término $b(\rho_j)^2\ge b_0^2/4$ (el representante del cuádruplo tiene el mismo $b$). Por tanto
$$I\;\ge\;\sum_{j=1}^{\infty} b(\rho_j)^2\;\ge\;\sum_{j=1}^{\infty}\frac{b_0^2}{4}\;=\;\infty.\qquad\blacksquare$$

**[Obs. 175.3] (precisión fija basta; un disco basta).** La prueba solo usó $\varepsilon_k<\eta$ para $k$ grande, no $\varepsilon_k\to0$ (la tasa $\delta(\varepsilon_k)\to0$ del Paso 1 es un refinamiento, no un insumo). Por tanto la hipótesis real del Teorema 175.2 es **LP-112[$\rho_0$]** (Def. §1(b)): infinitos shifts a precisión FIJA $\varepsilon<\eta$, en UN disco. Esto es estrictamente menos que LP-112 en dos direcciones (un disco en vez de todos, $\varepsilon$ fijo en vez de $\to0$) y conviene registrarlo: cualquier ataque futuro a la rigidez secuencial tiene este objetivo mínimo. La simetría del cuádruplo no se usa: una réplica por shift basta (el cuádruplo entero se replica, por la ecuación funcional, pero no aporta nada — solo multiplicaría la cota por 4).

**[COR 175.4] (la versión débil LP-112⁻ también basta).** *LP-112⁻ ⟹ $I\in\{0,\infty\}$.*

*Demostración.* Supóngase $I>0$ y constrúyase inductivamente una sucesión de ceros off $\rho^{(k)}=\tfrac12+b^{(k)}+i\gamma^{(k)}$ con alturas estrictamente crecientes y $b^{(k)}\ge b_0/2$ para todo $k$. Base: $\rho^{(0)}:=\rho_0$, $b^{(0)}=b_0$. Paso: dado $\rho^{(k)}$ con $b^{(k)}\ge b_0/2$, defínase el **radio sumable**
$$r_k\;:=\;\min\Bigl(b_0\,2^{-k-2},\;\tfrac12\min\bigl(b^{(k)},\,1-\beta^{(k)},\,\mathrm{dist}(\rho^{(k)},Z(\zeta)\setminus\{\rho^{(k)}\})\bigr)\Bigr)\;>\;0,$$
$D_k:=\bar D(\rho^{(k)},r_k)\subset\{\tfrac12<\sigma<1\}$, $\eta_k:=\min_{\partial D_k}|\zeta|>0$. Aplíquese LP-112⁻ a $(D_k,\,\eta_k/2)$: existe $\tau>\mathrm{altura}(D_k)\;(>2r_k+1)$ con $\sup_{D_k}|\zeta(\cdot+i\tau)-\zeta|<\eta_k/2<\eta_k$, y el Lema 175.1(i) produce un cero $\rho^{(k+1)}$ de ζ con $|\rho^{(k+1)}-(\rho^{(k)}+i\tau)|<r_k$; en particular $\gamma^{(k+1)}>\gamma^{(k)}+\tau-r_k>\gamma^{(k)}$ (alturas estrictamente crecientes ⟹ cuádruplos distintos, como en el Paso 2) y
$$b^{(k+1)}\;\ge\;b^{(k)}-r_k\;\ge\;b_0-\sum_{j=0}^{k}b_0\,2^{-j-2}\;\ge\;b_0\Bigl(1-\tfrac12\Bigr)\;=\;\frac{b_0}{2}.$$
(El punto de la sumabilidad: con radios fijos tipo $r_k=b^{(k)}/2$ la abscisa podría degradarse geométricamente, $b^{(k)}\ge b_0 2^{-k}$, y $\sum (b^{(k)})^2$ podría converger; el presupuesto $\sum_k r_k\le b_0/2$ evita la fuga. También $b^{(k+1)}\le b^{(k)}+r_k\le 2b_0<\tfrac12+b_0$, y $\beta^{(k+1)}<1$ automáticamente por ser cero de ζ.) Entonces $I\ge\sum_k (b^{(k)})^2\ge\sum_k b_0^2/4=\infty$. $\blacksquare$

**[COR 175.5] (las dos dicotomías y la nueva arquitectura).**
1. $I\in\{0,\infty\}\Rightarrow m\in\{0,\infty\}$ (si $m\ge1$ entonces $I>0$, luego $I=\infty$, luego $m=\infty$ porque una suma finita de cuadrados acotados por $\tfrac14$ es finita). La dicotomía de energía **implica** D-109; el Teorema 175.2 subsume al Teorema 2.3 del D112 con la misma hipótesis.
2. $\boxed{\ \mathrm{RH}\;\Longleftarrow\;\bigl(I(0^+)<\infty\bigr)\;\wedge\;\mathrm{LP\text{-}112}\ }$ — en efecto, bajo LP-112, $I\in\{0,\infty\}$; con $I<\infty$ queda $I=0$, i.e. no hay ceros off. Mejora **estricta** de la arquitectura $(m<\infty)\wedge$LP-112 de P44: $m<\infty\Rightarrow I<\infty$ trivialmente, y el recíproco falla ($b_j=1/j$ sobre alturas cualesquiera: $m=\infty$, $I=\pi^2/6-$tipo$<\infty$). La primera flecha (finitud) se debilita de un enunciado de **cardinal** a un enunciado de **momento ℓ²** — exactamente la cantidad sobre la que el programa tiene su único certificado incondicional de segundo orden (Teorema 170.5).

**Honestidad sobre la novedad.** La prueba del Teorema 2.3 del D112 ya producía, bajo LP-112 completo, infinitos ceros off a distancia $<r$ de $\rho_0+i\tau_k$ — la cota $b\ge b_0-r$ estaba *implícita*. Lo nuevo de este documento es: (i) hacer explícito y cuantitativo que la réplica copia la abscisa (Lema 175.1(ii), tasa $\varepsilon^{1/m_0}$, multiplicidad incluida); (ii) que la conclusión correcta es sobre $I$, no sobre $m$, y que eso **debilita la primera flecha de la arquitectura** (Cor. 175.5.2 — este es el contenido estratégico); (iii) que LP-112⁻ también basta, lo que requiere la inducción de radios sumables del Cor. 175.4 (no trivial: sin sumabilidad la abscisa se fuga); (iv) el puente incondicional del §3, que es independiente de LP-112.

---

## 3. El puente: densidad de replicación ↔ el teorema de energía (incondicional)

La pregunta del mandato: ¿el certificado $E(T)\ll T/\log T$ (Teorema 170.5) YA limita cuán buena puede ser la auto-aproximación de un ζ con cero off? **Sí — y la limitación es un teorema incondicional con tasa.**

**[DEFINICIÓN-NUEVA] (conjunto de shifts buenos).** Para $\rho_0,r,\eta$ como en §2.2 y $0<\varepsilon<\eta$:
$$A_\varepsilon\;:=\;\Bigl\{\tau>0:\ \sup_{s\in \bar D(\rho_0,r)}\bigl|\zeta(s+i\tau)-\zeta(s)\bigr|\le\varepsilon\Bigr\}$$
(el conjunto de la Prop. 2.6 del Doc 112).

**[TEOREMA 175.6] (la auto-aproximación de un ζ con cero off es rara, con tasa).** *Supóngase que ζ tiene un cero off $\rho_0=\tfrac12+b_0+i\gamma_0$, y sean $r\le b_0/2$, $\eta$, $A_\varepsilon$ como arriba, $\varepsilon<\eta$. Entonces, incondicionalmente:*

(i) *(medida, vía Selberg directo)* $\;\mathrm{meas}\bigl(A_\varepsilon\cap[0,T]\bigr)\;\le\;2r\,N\bigl(\tfrac12+\tfrac{b_0}2,\;T+\gamma_0+r\bigr)\;\ll\;r\,T^{\,1-b_0/8}\log T$;

(ii) *(medida, vía energía)* $\;\mathrm{meas}\bigl(A_\varepsilon\cap[0,T]\bigr)\;\le\;\dfrac{8r}{b_0^2}\,E\bigl(T+\gamma_0+r\bigr)\;\ll\;\dfrac{r}{b_0^2}\cdot\dfrac{T}{\log T}$;

(iii) *(conteo separado)* todo subconjunto $2r$-separado $\{\tau_k\}\subset A_\varepsilon$ cumple
$$\#\{k:\tau_k\le T\}\;\le\;\min\Bigl(N\bigl(\tfrac12+\tfrac{b_0}2,\,T+\gamma_0+r\bigr),\;\frac{4}{b_0^2}E(T+\gamma_0+r)\Bigr)\;\ll\;\min\Bigl(T^{1-b_0/8}\log T,\;\frac{T}{b_0^2\log T}\Bigr).$$

*Demostración.* El mapa de réplica: para $\tau\in A_\varepsilon$, como $\varepsilon<\eta$, el Lema 175.1(i) (con $\delta=R=r$) da un cero $\rho$ de ζ con $|\rho-(\rho_0+i\tau)|<r$; ese cero tiene $\operatorname{Re}\rho\in(\tfrac12+b_0-r,\,\tfrac12+b_0+r)\subset(\tfrac12+\tfrac{b_0}2,\,1)$ — es off con $b(\rho)\ge b_0/2$ — y $\operatorname{Im}\rho\in(\gamma_0+\tau-r,\,\gamma_0+\tau+r)$. Como el disco $D(\rho_0+i\tau,r)$ tiene radio $r<b_0/2\le\tfrac14$ y vive en $\{\sigma>\tfrac12\}$, solo el miembro derecho-superior de cada cuádruplo puede caer en él: el cero replicado identifica un cuádruplo. Sea
$$\mathcal Z(T)\;:=\;\bigl\{\text{cuádruplos con } b\ge \tfrac{b_0}{2},\ 0<\gamma\le T+\gamma_0+r\bigr\}.$$
Para cada cuádruplo $z\in\mathcal Z(T)$ (representante $\beta+i\gamma$), el conjunto de $\tau$ a los que ese cuádruplo puede servir de réplica es $T_z=\{\tau:\ |\beta+i\gamma-\rho_0-i\tau|<r\}\subset(\gamma-\gamma_0-r,\ \gamma-\gamma_0+r)$, un intervalo de longitud $\le2r$. Entonces $A_\varepsilon\cap[0,T]\subset\bigcup_{z\in\mathcal Z(T)}T_z$, de donde $\mathrm{meas}(A_\varepsilon\cap[0,T])\le 2r\,\#\mathcal Z(T)$. Ahora, dos cotas para $\#\mathcal Z(T)$:
$$\#\mathcal Z(T)\;\le\;N\bigl(\tfrac12+\tfrac{b_0}2,\,T+\gamma_0+r\bigr)\qquad\text{y}\qquad \#\mathcal Z(T)\;\le\;\sum_{\gamma_j\le T+\gamma_0+r}\frac{b_j^2}{(b_0/2)^2}\;=\;\frac{4}{b_0^2}\,E(T+\gamma_0+r)$$
(la segunda es Chebyshev sobre la energía). El teorema de densidad de Selberg [S46] da $N(\tfrac12+\tfrac{b_0}2,T')\ll T'^{\,1-b_0/8}\log T'$ (exponente $1-\tfrac14\cdot\tfrac{b_0}{2}$), y el Teorema 170.5 da $E(T')\ll T'/\log T'$. Esto prueba (i)–(ii). Para (iii): si $|\tau_k-\tau_{k'}|>2r$, los discos $D(\rho_0+i\tau_k,r)$ y $D(\rho_0+i\tau_{k'},r)$ son disjuntos, luego shifts separados reciben cuádruplos distintos y el mapa de réplica es inyectivo de $\{\tau_k\le T\}$ en $\mathcal Z(T)$. $\blacksquare$

**Lecturas (las cuatro pedidas por el mandato):**

1. **Mejora de la Prop. 2.6 (D112).** Aquélla daba densidad superior **cero** de $A_\varepsilon$ vía el teorema límite de Bagchi + Portmanteau — cualitativo, sin tasa, con maquinaria distribucional. El Teorema 175.6 da la tasa explícita $\mathrm{meas}(A_\varepsilon\cap[0,T])/T\ll r\,T^{-b_0/8}\log T$ con una prueba de dos líneas (Rouché + densidad de ceros). El puente conceptual es la **identidad de conteo (iii)**: *la energía es un contador de testigos de auto-aproximación* — cualquier mejora futura del certificado $E(T)$ se transfiere automáticamente a una cota de rareza de la auto-aproximación. Este es el puente energía ↔ universalidad pedido: dos teorías que el programa llevaba en carriles separados (Docs 170–172 vs Docs 112–113) quedan unidas por una desigualdad incondicional.

2. **¿Cuál de las dos cotas manda?** Para $b_0$ **fijo** (la situación del teorema: el cero off es un objeto fijo), Selberg directo (i) gana con ahorro de potencia $T^{-b_0/8}$. La versión por energía (ii) es la conceptualmente nueva pero numéricamente más débil ($T/\log T$ es la envolvente $b_0$-uniforme — coherente con el veredicto del Doc 172: la envolvente de Selberg ES el suelo $T/\log T$ leído en energía; (ii) no puede superar a (i) porque 170.5 se prueba CON [S46]). El valor de (ii) es estructural, no cuantitativo: hace visible que el objeto que limita la replicación es exactamente el objeto de la primera flecha de la arquitectura ($I$, vía $E$).

3. **El fortalecimiento dimensional, con su gap declarado.** La réplica da la cota inferior exacta dual de (iii): si $\{\tau_k\}\subset A_\varepsilon$ es $2r$-separado, entonces $E(T)\ge\tfrac{b_0^2}{4}\,\#\{k:\tau_k\le T-\gamma_0-r\}$ — *densidad positiva de testigos ⟹ densidad positiva de energía*. **LP-112 NO trae densidad gratis** (es puramente secuencial: $\tau_k\to\infty$ sin cota de conteo — dicho explícitamente, como pide el mandato). Si se postulara densidad positiva de testigos (i.e. recurrencia fuerte en $D_0$), la contradicción con (iii) es inmediata — pero eso no es nuevo: es la mitad fácil de Bagchi (recurrencia fuerte + cero off = absurdo), aquí re-probada con tasa: **cualquier familia $2r$-separada de testigos con conteo $\gg T^{1-b_0/8}\log T$ es incondicionalmente imposible.** El hueco entre lo que LP-112 necesita (conteo no acotado: $\#\to\infty$, tan lento como se quiera) y lo que el puente prohíbe (conteo $\gg T^{1-b_0/8}\log T$) es abismal: **el puente no cierra LP-112 ni lo amenaza** — coherente con la Prop. 2.7 del D112 (la versión secuencial no se auto-bloquea). El puente acota al enemigo por arriba; no toca su no-vacuidad.

4. **Dirección inversa del puente.** (iii) leído al revés: si alguien probara que la auto-aproximación en el disco de un cero off hipotético tiene SIEMPRE conteo separado $\gg T/(b_0^2\log T)$ (una "recurrencia débil cuantitativa universal"), entonces $E(T)\gg T/\log T$, contradiciendo... nada: 170.5 es $\ll$, compatible. Para una contradicción se necesitaría $\gg T^{1-b_0/8+\delta}$ contra (i). [GAP 175.B, forma de enunciado: *"toda función del espacio de Bagchi con un cero en $D_0$ que sea límite de traslados verticales de sí misma a lo largo de una sucesión no acotada lo es a lo largo de una sucesión de conteo $\ge\Phi(T)$"* para algún $\Phi$ explícito — un teorema de "automaticidad de densidad" para recurrencia secuencial. No conocemos nada parecido en la literatura de universalidad; la recurrencia de Birkhoff da retornos sindéticos para sistemas compactos, pero el flujo de traslaciones de ζ no es compacto ni el target es recurrente-genérico. Si $\Phi$ pudiera tomarse $\gg T^{1-b_0/8}\log T$, LP-112[$\rho_0$] sería **falso** bajo ¬RH y la arquitectura entera colapsaría a "RH ⟸ I<∞" — demasiado bueno; lo esperable es que tal $\Phi$ no exista.]

---

## 4. Estado honesto de LP-112

Resumen verificado contra Docs 112–113 y la literatura citada allí en fuente.

**Lo que es teorema.**
- **RH ⟹ LP-112.** Bajo RH, ζ no se anula en $\{\tfrac12<\sigma<1\}$; para todo disco $D$ de la franja, $\zeta|_D$ es no-nula, luego pertenece al soporte de la medida de Bagchi, y la recurrencia fuerte (mitad "fácil-bajo-RH" de [Bag87]; exposición [Ste07, §8.3]) da densidad inferior **positiva** de $\{\tau:\sup_D|\zeta(\cdot+i\tau)-\zeta|<\varepsilon\}$ para todo $\varepsilon>0$ — mucho más que una sucesión.
- **Recurrencia fuerte ⟺ RH (Bagchi).** *RH ⟺ para todo compacto admisible $K\subset\{\tfrac12<\sigma<1\}$ y todo $\varepsilon>0$, el conjunto de $\tau$ con $\sup_K|\zeta(\cdot+i\tau)-\zeta|<\varepsilon$ tiene densidad inferior positiva.* [Bag81] (tesis, Indian Statistical Institute, Calcuta), [Bag87] (Acta Math. Hungar. 50, 227–240); exposición moderna [Ste07, Thm. 8.3]. La dirección ⟹ es la del punto anterior (soporte pleno = genericidad); la dirección ⟸ es el amplificador Rouché × densidad: recurrencia fuerte + cero off produce $\ge cT$ ceros off hasta altura $T$, contra $N(\sigma,T)=o(T)$ — exactamente la versión "densidad positiva" de nuestro Teorema 175.6(iii). **Verificado: la equivalencia es con la recurrencia FUERTE (densidad positiva, todos los compactos); el precedente es Bohr 1922 para $L(s,\chi)$ (D113 §2.1).**
- **Bajo ¬RH, los testigos de LP-112 en el disco del cero son excepcionales con tasa** (Prop. 2.6 del D112: densidad cero; Teorema 175.6 de aquí: $\ll T^{-b_0/8}\log T$).

**Lo que NO se sabe.**
- LP-112 **no se sabe equivalente a RH**: es secuencial (no pide densidad) y por eso escapa al amplificador de Bagchi (Prop. 2.7 del D112: una familia numerable rala de ceros replicados no contradice ningún teorema de densidad). Tampoco se sabe refutar bajo ¬RH: densidad cero ≠ vacío. Estado: RH ⟹ LP-112 ⟹ $I\in\{0,\infty\}$ (este doc) ⟹ $m\in\{0,\infty\}$; ninguna flecha se sabe revertir.

**La sutileza del disco con ceros (el corazón del estatus).** La universalidad de Voronin [Vor75] y toda su descendencia aproximan **targets no-nulos**: el soporte de la medida de Bagchi en $H(D')$ es $S=\{f:\ f\ne0\text{ en }D'\}\cup\{0\}$ (límites de productos de Euler aleatorios no-nulos son no-nulos o $\equiv0$ — teorema de Hurwitz; [Bag81], [Lau96, cap. 6], [Ste07]). Auto-aproximar ζ en un disco SIN ceros es, bajo RH, un caso particular de esa genericidad. Auto-aproximar ζ en un disco que CONTIENE un cero off es categóricamente otra cosa: el target está **fuera del soporte**, y:
1. **Rouché no lo prohíbe** — conviene decirlo con precisión, porque es un malentendido posible. Rouché solo dice: toda aproximante $\varepsilon$-buena ($\varepsilon<\eta$) debe anularse en $D(\rho_0,r)$; i.e. $\zeta$ debe tener un cero cerca de $\rho_0+i\tau$. Bajo ¬RH eso es *posible* (hay ceros off disponibles — de hecho el Teorema 175.2 EXPLOTA exactamente esa necesidad: la obstrucción de Rouché es el mecanismo de replicación, no un impedimento). La auto-aproximación con ceros no es analíticamente imposible; es **distribucionalmente excepcional**.
2. La obstrucción real es de genericidad/medida: todo lo que produce shifts buenos (equidistribución de Kronecker–Weyl, teorema límite de Bagchi, momentos) produce shifts *genéricos*, y el genérico no se anula cerca de $\rho_0+i\tau$ (medida cero). Producir UN elemento de un conjunto de densidad cero definido por una condición individual es el Principio 3.1 de P43 — el muro, en instancia secuencial (D112 §2.4–2.5). El Teorema 175.6 agrava la excepcionalidad con tasa de potencia.
3. **Precedente positivo que calibra:** la auto-aproximación SÍ es teorema para la zeta de Hurwitz $\zeta(s,\alpha)$ ($\alpha$ trascendente, o racional $\ne\tfrac12,1$) — [GK14] (Garunkštis–Karikovas, *Self-approximation of Hurwitz zeta-functions*) y la universalidad fuerte de [Bag81] —, **incluso en discos con ceros**, porque su medida tiene soporte pleno en $H(D)$ (sin producto de Euler no hay compresión de soporte): el punto es genérico para su propio flujo. Para ζ, **Euler comprime el soporte y convierte el mismo enunciado en excepcional** (D113 §3.1). LP-112 es, exactamente, la pregunta de si la compresión de Euler deja o no una sucesión residual. Sin precedente en la literatura en ninguna dirección (D113, veredicto).

**Referencias.** [Vor75] S.M. Voronin, *Теорема об «универсальности» дзета-функции Римана*, Izv. Akad. Nauk SSSR Ser. Mat. 39 (1975), 475–486. [Bag81] B. Bagchi, *The statistical behaviour and universality properties of the Riemann zeta-function and other allied Dirichlet series*, tesis, Indian Statistical Institute, Calcuta, 1981. [Bag87] B. Bagchi, *Recurrence in topological dynamics and the Riemann hypothesis*, Acta Math. Hungar. 50 (1987), 227–240. [Ste07] J. Steuding, *Value-Distribution of L-Functions*, Springer Lecture Notes in Math. 1877, 2007 (cap. 8: recurrencia fuerte y auto-aproximación). [Lau96] A. Laurinčikas, *Limit Theorems for the Riemann Zeta-Function*, Kluwer, 1996. [GK14] R. Garunkštis, E. Karikovas, *Self-approximation of Hurwitz zeta-functions*, Funct. Approx. Comment. Math. 51 (2014). [S46] A. Selberg, *Contributions to the theory of the Riemann zeta-function*, Arch. Math. Naturvid. 48 (1946). [T39] E.C. Titchmarsh, *The Theory of Functions*, 2ª ed., Oxford, 1939, §3.42 (Rouché). [C78] J.B. Conway, *Functions of One Complex Variable*, 2ª ed., Springer GTM 11, 1978 (VII.2.5 Hurwitz, VIII.3 Rouché). [T86] E.C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2ª ed. (Heath-Brown), Oxford, 1986. Universalidad discreta: A. Reich, *Werteverteilung von Zetafunktionen*, Arch. Math. 34 (1980), 440–451.

---

## 5. El retrato del estado de energía finita (sin asumir LP-112)

¿Qué dice $0<I<\infty$ por sí solo? (La "Fase C" del director, versión replicación.)

**[PROP 175.7] (estructura ℓ²).** Si $I<\infty$:
1. *(finitos gordos por nivel)* para todo $b>0$, $\;\#\{j:\ b_j\ge b\}\;\le\;I/b^2\;<\;\infty$;
2. *(acumulación en la línea)* $b_j\to0$ para cualquier enumeración (colas de una serie convergente); si $m=\infty$, los ceros off se acumulan en $\{\operatorname{Re}=\tfrac12\}$ y solo en ella;
3. $m=\infty$ sigue siendo posible ($b_j=1/j$ realiza $I<\infty$, $m=\infty$, y configuraciones así son indistinguibles por datos de promedio — Teorema 170.8); $I<\infty$ NO implica $m<\infty$: la primera flecha nueva es genuinamente más débil que la vieja.

*Demostración.* (1) Chebyshev. (2) inmediato. (3) Doc 170 §5. $\square$

**[PROP 175.8] (anti-recurrencia del estado de energía finita).** *Si $0<I<\infty$, entonces para TODO cero off $\rho_0$ (con sus constantes $r\le b_0/2$, $\eta$) y todo $\varepsilon<\eta$:*
$$\mathrm{meas}\bigl(A_\varepsilon\bigr)\;\le\;\frac{8r}{b_0^2}\,I\;<\;\infty\quad\text{(medida total en }(0,\infty)\text{)},\qquad \#\{\text{subconjunto }2r\text{-separado de }A_\varepsilon\}\;\le\;\frac{4I}{b_0^2}\;<\;\infty .$$
*En particular NO existe ninguna sucesión no acotada de shifts $\varepsilon$-buenos en el disco de ningún cero off: el estado de energía finita es anti-recurrente en cada una de sus ventanas off, incluso a precisión fija.*

*Demostración.* Las del Teorema 175.6(ii)–(iii) con $T\to\infty$: $\#\mathcal Z(\infty)\le 4I/b_0^2$ (Chebyshev sobre la serie completa), $A_\varepsilon\subset\bigcup_{z}T_z$ con $\le 4I/b_0^2$ intervalos de longitud $\le2r$; un conjunto contenido en finitos intervalos acotados no admite sucesión no acotada. $\square$

**El retrato completo.** El mundo $0<I<\infty$ es: *casi todos los ceros off sub-resolución* (a cada distancia fija de la línea, finitos — Prop 175.7.1, con presupuesto explícito $I/b^2$; la envolvente incondicional 170.5 dice además que incluso la energía total hasta $T$ crece como $T/\log T$ a lo sumo, en CUALQUIER mundo), *acumulación pura en la línea* (175.7.2), *posiblemente con infinitos ceros* (175.7.3), y **anti-recurrente**: cada cero off es un punto del que ζ se aleja definitivamente — pasada una altura finita, ζ no vuelve a parecerse a sí misma en esa ventana ni siquiera con error fijo $\varepsilon<\eta$ (175.8). $I$ funciona como presupuesto contable: cada retorno $\varepsilon$-bueno separado consume $\ge b_0^2/4$ unidades de energía, y solo hay $I$.

**¿La replicación PARCIAL ($\varepsilon$ fijo, no $\to0$) contradice el retrato?** Empujado hasta el final: la Prop. 175.8 ES la contrapositiva exacta de la versión fuerte del Teorema 175.2 (Obs. 175.3). La frontera precisa:
- recurrencia a precisión $\varepsilon<\eta$ con sucesión **no acotada** en UNA ventana off ⟹ $I=\infty$ (incompatible con $0<I<\infty$);
- recurrencia a precisión $\varepsilon\ge\eta$ no dice nada (Rouché necesita ganar en la frontera: con $\varepsilon\ge\eta$ la aproximante puede no anularse — el umbral $\eta$ es exacto, no mejorable por este método: $f=\zeta-\zeta(\,\cdot\,)\cdot$(corrección que tape el cero) ilustra que con margen $\ge\eta$ se puede esquivar el cero);
- finitos retornos buenos son siempre compatibles ($\le 4I/b_0^2$ de presupuesto).

No hay contradicción interna alcanzable sin LP-112: el retrato es consistente. Pero queda nítido **qué lo rompería** — y es el objetivo mínimo:

**[GAP 175.A] (la instancia mínima de LP-112, forma de enunciado).** *Sea $\rho_0$ un cero de ζ con $\operatorname{Re}\rho_0\in(\tfrac12,1)$, $r=r(\rho_0)$, $\eta=\eta(r)$ como en §2.2. Probar: existe una sucesión no acotada $\{\tau_k\}$ con $\sup_{|s-\rho_0|\le r}|\zeta(s+i\tau_k)-\zeta(s)|<\eta$.* — Esto, junto con $I(0^+)<\infty$, implica RH (de hecho implica $I=\infty$, contradiciendo $I<\infty$ y forzando que no exista tal $\rho_0$). Es estrictamente más débil que LP-112 (un disco, un $\varepsilon$) y sus testigos, si existen, viven en un conjunto de medida-densidad $\ll T^{-b_0/8}\log T$ (Teorema 175.6): el muro de P43 §3.1, ahora con la tasa de su propia excepcionalidad escrita.

---

## 6. Mensaje final

**¿El teorema quedó probado? SÍ**, con prueba completa y cuantificada, **condicional a LP-112 y declarado así**: la hipótesis es exactamente LP-112 (de hecho basta LP-112⁻, y de hecho basta la instancia mínima LP-112[$\rho_0$] a precisión fija en un solo disco — Obs. 175.3, GAP 175.A). Ningún paso de la prueba es condicional a nada más; toda la incertidumbre del programa sigue comprimida en LP-112, que este documento no prueba y cuyos testigos quedan, bajo ¬RH, cuantitativamente más excepcionales que antes (tasa $T^{-b_0/8}\log T$).

**La nueva arquitectura se sostiene:**
$$\boxed{\;\mathrm{RH}\;\Longleftarrow\;\bigl(I(0^+)<\infty\bigr)\;\wedge\;\mathrm{LP\text{-}112}\;}$$
mejora estricta de la vieja $(m<\infty)\wedge\mathrm{LP\text{-}112}$ de P44/D112: la primera flecha baja de cardinal (m<∞, sin certificado parcial alguno) a momento ℓ² ($I<\infty$, cuya envolvente $E(T)\ll T/\log T$ ES el único certificado incondicional de segundo orden del programa, Teorema 170.5 — la flecha que falta es "tasa→total", no "nada→todo"). La segunda flecha queda intacta e idéntica.

**Tres resultados con etiquetas:**
1. **[TEOREMA 175.2 + COR 175.4]** (condicional a LP-112, incluso a LP-112⁻): $I(0^+)\in\{0,\infty\}$ — la dicotomía de energía; la réplica de Rouché–Hurwitz copia la distancia a la línea con error $\le(4\varepsilon_k/|c|)^{1/m_0}\to0$ y cada réplica cuesta $\ge b_0^2/4$ de energía. Subsume la dicotomía de cardinal D-109 y convierte el Problema B del director ($I<\infty\Rightarrow I=0$) en teorema condicional a LP-112.
2. **[TEOREMA 175.6]** (incondicional, nuevo): si ζ tiene un cero off, su auto-aproximación en el disco del cero es rara con tasa — $\mathrm{meas}(A_\varepsilon\cap[0,T])\ll r\,T^{1-b_0/8}\log T$ y todo conjunto separado de testigos tiene $\#\le 4E(T)/b_0^2\ll T/(b_0^2\log T)$. Puente energía ↔ universalidad; mejora con tasa y prueba elemental la Prop. 2.6 del D112; cualquier mejora futura de $E(T)$ se transfiere sola.
3. **[PROP 175.8]** (incondicional): el estado $0<I<\infty$ es anti-recurrente — medida total de shifts buenos $\le 8rI/b_0^2$, a lo sumo $4I/b_0^2$ testigos separados en TODO $(0,\infty)$; $I$ = presupuesto de testigos. Contrapositiva exacta del teorema; fija el objetivo mínimo GAP 175.A.
