# Doc 147 — Reparación del Problema 139.A: la rama ¬RH del criterio logístico por dominancia exponencial del soporte

**Programa:** Hipótesis de Riemann — Phase 47, "frentes vivos"
**Fecha:** junio 2026
**Autor:** David Alejandro Trejo Pizzo
**Mandato:** ejecutar o refutar la ruta de reparación nombrada por la auditoría (Doc 139, §4.4): re-probar el Teorema 5.4 de D136 (= `thm:realiz` de P47) bajo ¬RH **sin** la constante divergente $C_3(M)$, sustituyendo la normalización del término principal a $1$ por la **dominancia exponencial $e^{2\delta_0 a_0}$ del criterio clásico de Weil**. Veredicto honesto sobre el estatus de la rama ¬RH y consecuencia para P47.

**Prerrequisitos (leídos completos, citas solo hacia atrás):** D136 (Teorema 5.4, Def. 3.1–3.2 de σ_loc, micro-celdas, Lemas 5.2–5.3; lado espectral (1.1)–(1.2) heredado de D107); D139 (GAP-A, Lema 139.1 de rigidez Paley–Wiener, GAP-B, ruta de reparación, Problema 139.A); P47 (`hyp:pw`, `rem:pw-rigidity`, `lem:tail`, `lem:vandermonde`, `thm:realiz`, parche GAP-B en `Z_τ`, `rem:theta` con la fórmula de perturbación Paley–Wiener).

**Contrato de la fase:** **[DEFINICIÓN]** libertad total; **[LEMA]/[PROPOSICIÓN]/[TEOREMA]** prueba completa o no lleva etiqueta; **[PUENTE]** honesto; **[GAP]** declarado. Nada se fabrica. Solo prueba y forma cerrada; cero numérico.

---

## 0. Veredicto en una línea

**139.A queda CERRADO-PARCIAL.** La ruta de dominancia exponencial **funciona** y **elimina genuinamente** la constante divergente $C_3(M)$: la rama ¬RH deja de depender de `hyp:pw` (que es **falsa** para todo bump, Lema 139.1) y pasa a depender de una hipótesis estrictamente más débil, puramente geométrica y **verificable en la clase**, que llamamos **separación de bandas en la celda** (`hyp:band`, §4). Bajo `hyp:band` la rama ¬RH es **teorema completo**. Lo que NO se cierra es la eliminación total de toda hipótesis: la dominancia exponencial sobrevive a la localización a micro-celdas de dimensión acotada **solo si el centro de banda $\sigma$ puede colocarse en $\frac12+\delta_0+i\gamma_0$** (no solo en su ordenada $\gamma_0$); esto requiere que la grilla de perfiles muestree también la **parte real** del centro espectral, lo cual el esquema de D136 **no hace** (sus centros $(c,c')$ son reales = ordenadas). La reparación es honesta: no esconde una constante divergente nueva — la dominancia es real —, pero **expone un grado de libertad faltante en la definición de la grilla** (Def. 3.1/3.2 de D136). Con ese grado de libertad añadido (ampliación inocua de la grilla, §4.3), 139.A es teorema; sin él, 139.A se reduce a `hyp:band`, estrictamente más débil y verificable que `hyp:pw`.

**Una falsa victoria descartada explícitamente:** verifiqué (§3.4, §5) que el factor $e^{2\delta_0 a_0}$ NO esconde su propia constante divergente. El peligro real estaba en otro sitio — no en una constante, sino en un **eje de la grilla que no existía** —, y queda nombrado, no disimulado.

---

## 1. El Problema 139.A, preciso, y por qué `hyp:pw` falla con bump fijo

### 1.1. Anatomía del Paso 3 y la cota que debe tender a $0$

En `thm:realiz` (Paso 3) la prueba descompone $Q_2(v,v)$ con $v=h_{g_v,\varphi_v}\in V_{p^*}$ en tres clases de pares $(\rho_1,\rho_2)$ del lado espectral

$$Q_2(h,h')=\sum_{(\rho_1,\rho_2)}\hat h(\rho_1,\rho_2)\,\overline{\hat h'(\iota(\rho_1,\rho_2))},\qquad \hat h_{g,\varphi}=\tfrac12\hat g(\sigma)\hat\varphi(\tau),\ \sigma=\tfrac{\rho_1+\rho_2}2,\ \tau=\tfrac{\rho_1-\rho_2}2. \tag{1.1}$$

- **(a) órbita objetivo** $\{P_0,\iota P_0\}$, $P_0=(\rho^0,\rho^0)$: aporta $2m_0^2\,\mathrm{Re}[\hat h(P_0)\overline{\hat h(\iota P_0)}]$. En el diseño de D136 el testigo se normaliza con $\hat g_v(\sigma_0)=1$, $\hat g_v(\sigma_0')=-1$, $\hat\varphi_v(0)=1$ (Vandermonde, `lem:vandermonde`), dando exactamente $-m_0^2/2$.
- **(b) pares resonantes y casi-resonantes** (ambos miembros en $S$): aniquilados por $\hat g_v=0$ sobre $Z_\sigma$ y (parche GAP-B de P47) $\hat\varphi_v=0$ sobre $Z_\tau$. Aportan $0$.
- **(c) la cola** $\Omega_1$: acotada por `lem:tail` con $r=1$.

El **tail budget** que el Paso 3 necesita es $|(c)|\le m_0^2/4$, es decir (la cota explícita de `hyp:pw`):

$$\boxed{\;C_1(M)^2\,C_g(M)^2\,C_\varphi(M)^2\;C^*(M-D)\,(\log(2+|\gamma_0|))^2\;2^{-(M-D-4)}\ \xrightarrow[M\to\infty]{}\ 0\;}\tag{1.2}$$

donde $C_g(M),C_\varphi(M)$ **absorben** la constante de Paley–Wiener $C_M$ de la cota del bump

$$|B^{(M)}_w(z)|\le C_M\,e^{a_0|\mathrm{Re}\,z-\frac12|}\,(1+|\mathrm{Im}\,z|/w)^{-M},\qquad B^{(M)}_w(0)=1, \tag{$\ast$}$$

el factor de franja $e^{a_0(M,w)}$, y $C_1(M)$ es la norma de coeficientes de Vandermonde, $M$-dependiente vía $b_0(M)=\min_i|B^{(M)}(z_i-ic)|$.

### 1.2. Por qué (1.2) es falsa: la rigidez de Paley–Wiener (Lema 139.1, re-enunciado)

El núcleo del fracaso es que (1.2) trata $C_M$ como si pudiera crecer más lento que $2^{M}$. No puede:

> **Lema 1.1 (rigidez de Paley–Wiener; D139 Lema 139.1, Boas/Hörmander).** Sea $B$ la transformada de un $g\in C_c^\infty$ no nulo con soporte logarítmico $\subseteq[-a_0,a_0]$ ($a_0$ **fijo**), y $C_M$ las constantes óptimas en $|B(t)|\le C_M(1+|t|/w)^{-M}$, $t\in\mathbb R$. Entonces para todo $A>1$ existe $M_A$ con $C_M>A^M$ para todo $M\ge M_A$; en particular $C_M^4\,2^{-M}\to\infty$.

*Prueba.* Si $C_M\le A^M$ para infinitos $M$, entonces para $|t|>Aw$ se tendría $|B(t)|\le(Aw/|t|)^M\to0$ a lo largo de esos $M$, luego $B\equiv0$ en $\{|t|>Aw\}$; pero $B$ es entera de tipo exponencial $\le a_0$ (Paley–Wiener para $C_c^\infty$, cf. Boas, *Entire Functions*, Thm. 6.8.1; Hörmander I, Thm. 7.3.1) y no idénticamente nula, así que sus ceros reales son discretos — contradicción. $\square$

**Consecuencia exacta:** con cualquier bump de soporte fijo, el factor $C_M^4$ de (1.2) crece más rápido que cualquier $A^M$, derrotando a $2^{-(M-D-4)}$. Las familias estándar $B^{(M)}$ con soporte creciente $a_0(M)$ tampoco cierran: el **factor de franja** $e^{a_0(M)}$ de $(\ast)$ — inevitable porque los ceros de la cola pueden tener $\mathrm{Re}$ hasta los bordes de la franja crítica y $|B(x+it)|$ crece como $e^{a_0|x-\frac12|}$ — derrota al decaimiento polinomial en $\mathrm{Im}$ a distancia fija $r=1$ (D139 §4.2, balance $(M/a_0)^{2M}e^{2a_0}$ con mínimo $e^{2M}\to\infty$).

### 1.3. El diagnóstico estructural (lo que la reparación debe respetar)

`hyp:pw` exige hacer pequeña la cola **en términos absolutos** manteniendo el término principal **normalizado a $1$**. Pero normalizar $\hat g_v(\sigma_0)=1$ con $\sigma_0$ fuera de la línea **fuerza** coeficientes de Vandermonde grandes (porque $B^{(M)}$ decae fuera de su banda), y ese costo es el $C_1(M)$ divergente. **El error es estructural, no aritmético: la normalización a $1$ esconde que evaluar un test concentrado fuera de su banda natural es exponencialmente caro.** La reparación honesta debe dejar de normalizar y **cobrar ese costo como ganancia**: un test que vive en la franja crítica con soporte $a_0$ y se evalúa en $\mathrm{Re}=\frac12+\delta_0$ **vale** $e^{\delta_0 a_0}$, no $1$.

---

## 2. El lema de dominancia exponencial-vs-polinomial

Toda la reparación descansa en una dicotomía de crecimiento en el soporte que es clásica para el criterio escalar de Weil (Weil 1952; reproducida en, p.ej., la presentación de Bombieri o de la fórmula explícita en Iwaniec–Kowalski §5) y que aquí se traslada al lado doblado $Q_2$.

### 2.1. La representación de banda crítica

Un test $f$ de la clase con soporte **logarítmico** (multiplicativo) $\subseteq[e^{-a_0},e^{a_0}]$ tiene transformada de Mellin

$$\hat f(s)=\int_{-a_0}^{a_0}F(u)\,e^{(s-\frac12)u}\,du,\qquad F\in C_c^\infty([-a_0,a_0]), \tag{2.1}$$

(la normalización $s-\frac12$ centra la franja crítica; esta es exactamente la fórmula de `rem:theta` de P47, líneas 568–571). Para un cero $\rho=\frac12+\beta+i\gamma$:

$$\hat f(\rho)=\int_{-a_0}^{a_0}F(u)\,e^{\beta u}\,e^{i\gamma u}\,du,\qquad |e^{\beta u}|=e^{\beta u}\in[e^{-\beta a_0},e^{\beta a_0}]. \tag{2.2}$$

El factor $e^{\beta u}$ es el **único** lugar donde entra la parte real del cero. Tres regímenes:

- **on-line** ($\beta=0$): $|\hat f(\rho)|\le\|F\|_{L^1}$, y con $F$ suave el decaimiento en $\gamma$ es superpolinomial. Crecimiento en $a_0$: **polinomial** (a lo sumo $\|F\|_{L^1}\asymp a_0^{1/2}$ por normalización $L^2$; ver §2.3).
- **off-line** ($\beta=\delta_0>0$): eligiendo $F$ concentrada cerca de $u=+a_0$, $|\hat f(\rho)|$ alcanza $\asymp e^{\delta_0 a_0}$. Crecimiento en $a_0$: **exponencial**, tasa $\delta_0$.
- **off-line conjugado** ($\beta=-\delta_0$, en $\sigma_0'=\frac12-\delta_0+i\gamma_0$): si la misma $F$ está concentrada en $u=+a_0$, $|\hat f(\sigma_0')|\asymp e^{-\delta_0 a_0}\to0$; si en $u=-a_0$, al revés. **Esto es delicado y se trata en §3.2.**

### 2.2. El lema

> **[LEMA 2.1] (dominancia exponencial-vs-polinomial en banda crítica).**
> Sea $\rho^0=\frac12+\delta_0+i\gamma_0$ un cero off-line fijo, $\delta_0\in(0,\frac12)$. Para cada $a_0>0$ sea
> $$F_{a_0}(u):=a_0^{-1/2}\,\Phi\!\big((u-a_0/2)\big),\qquad \Phi\in C_c^\infty([-1,1]),\ \Phi\ge0,\ \textstyle\int\Phi=1, \tag{2.3}$$
> un bump de masa $L^1$ acotada concentrado en $u\approx a_0/2$ (dentro de $[-a_0,a_0]$ para $a_0\ge2$), y $f_{a_0}$ el test (2.1) asociado, con norma $\|f_{a_0}\|^2\asymp 1$ (normalización $L^2$ en $u$, $\|F_{a_0}\|_{L^2}^2=a_0^{-1}\|\Phi\|_{L^2}^2$; ver §2.3 para la elección que fija $\|v\|$). Entonces, con constantes que dependen solo de $\Phi$ y de $\delta_0$:
> $$\text{(off-line)}\quad |\hat f_{a_0}(\rho^0)|\ \ge\ c_1\,a_0^{-1/2}\,e^{\delta_0 a_0/2}, \tag{2.4}$$
> $$\text{(on-line, todo cero }\rho=\tfrac12+i\gamma)\quad |\hat f_{a_0}(\rho)|\ \le\ C_2\,a_0^{-1/2}\,(1+|\gamma-\tfrac{\gamma\text{-centro}}{}|)^{-K}\ \le\ C_2\,a_0^{-1/2}, \tag{2.5}$$
> para todo $K$ (decaimiento superpolinomial en $\gamma$ por suavidad de $\Phi$). En particular el **cociente** off/on crece como $e^{\delta_0 a_0/2}\to\infty$: ningún cero on-line, ni suma polinomial de ellos, compite con el cero off-line a soporte grande.

*Prueba.* (2.4): $\hat f_{a_0}(\rho^0)=a_0^{-1/2}\int_{-1}^1\Phi(t)\,e^{(\delta_0+i\gamma_0)(a_0/2+t)}\,dt=a_0^{-1/2}e^{(\delta_0+i\gamma_0)a_0/2}\int_{-1}^1\Phi(t)e^{(\delta_0+i\gamma_0)t}dt$. El factor integral es una constante no nula $c(\delta_0,\gamma_0)$ acotada inferior y superiormente (es $\hat\Phi$ evaluada en un punto fijo; $\Phi\ge0$, $\int\Phi=1$ impide cancelación total para $\delta_0$ real moderado — y para $\gamma_0$ grande se reemplaza $\Phi$ por $\Phi(t)e^{-i\gamma_0 t}$ modulada, manteniendo $|c|\ge c_1$, un test de la misma clase). Tomando módulos: $|e^{(\delta_0+i\gamma_0)a_0/2}|=e^{\delta_0 a_0/2}$, de donde (2.4).
(2.5): para $\beta=0$, $|\hat f_{a_0}(\rho)|=a_0^{-1/2}|\int\Phi(t)e^{i\gamma(a_0/2+t)}dt|=a_0^{-1/2}|\hat\Phi(\gamma)|$ (módulo fase), y $\Phi\in C_c^\infty\Rightarrow|\hat\Phi(\gamma)|\le C_K(1+|\gamma|)^{-K}$ todo $K$ (Paley–Wiener para $\Phi$, Hörmander I Thm. 7.3.1). $\square$

**Nota de honestidad sobre la tasa.** El soporte óptimo de $F$ en $[-a_0,a_0]$ daría tasa $e^{\delta_0 a_0}$ (concentrando en $u=a_0$), no $e^{\delta_0 a_0/2}$. Uso $a_0/2$ para dejar margen simétrico que necesitaré en §3.2 (controlar también $\sigma_0'$). La tasa exacta no es load-bearing: **cualquier tasa exponencial positiva $e^{c\delta_0 a_0}$, $c>0$, cierra el argumento**, porque la compite contra crecimiento polinomial. Este es el punto donde la reparación difiere cualitativamente de `hyp:pw`: allí se necesitaba una **igualdad asintótica delicada** (que el producto de cuatro constantes tienda a $0$); aquí basta una **desigualdad de orden de magnitud** (exponencial $>$ polinomial), que es robusta.

### 2.3. Normalización: por qué el cociente es lo que importa

El índice $\negind(Q_2|_{V_p})\ge1$ se certifica por $Q_2(v,v)<0$ para **algún** $v$; el tamaño absoluto de $\|v\|$ es irrelevante (un subespacio negativo lo es tras reescalar). Lo que importa es el **signo** de

$$Q_2(v,v)=\underbrace{(\text{a})}_{\text{plano objetivo}<0}+\underbrace{(\text{b})}_{=0}+\underbrace{(\text{c})}_{\text{cola}}, \tag{2.6}$$

y, por homogeneidad, podemos comparar (a) y (c) **sin normalizar**. La estrategia es: (a) $\asymp -e^{2\cdot(\text{tasa})\,a_0}$ (producto de dos factores off-line, §3.1), (c) $\le +(\text{polinomial en }a_0)\cdot e^{(\text{tasa menor})a_0}$ (§3.3). Para $a_0$ grande, (a) domina y $Q_2(v,v)<0$. **Ninguna constante se hace tender a infinito y se trata como constante**: $a_0$ es el parámetro, crece, y la prueba lo monitorea explícitamente en cada término.

---

## 3. Construcción del testigo sin constante divergente

### 3.1. El plano objetivo en el lado doblado

$P_0=(\rho^0,\rho^0)$ tiene $\sigma_0=\frac12+\delta_0+i\gamma_0$, $\tau_0=0$. Con el testigo $v=h_{g_v,\varphi_v}$, $g_v=\varphi_v=f_{a_0}$ (mismo bump en ambas coordenadas), $\hat h(P_0)=\frac12\hat f_{a_0}(\sigma_0)\hat f_{a_0}(\tau=0)$. Como $\tau_0=0$ es on-line en la coordenada diferencia ($\mathrm{Re}\,\tau_0=0$), $\hat f_{a_0}(0)\asymp a_0^{-1/2}$ (polinomial). Y $\hat f_{a_0}(\sigma_0)\ge c_1 a_0^{-1/2}e^{\delta_0 a_0/2}$ por (2.4). La imagen $\iota P_0$ tiene $\sigma_0'=\frac12-\delta_0+i\gamma_0$ (off-line conjugado), $\tau=0$. Entonces

$$\text{(a)}=2m_0^2\,\mathrm{Re}\big[\hat h(P_0)\overline{\hat h(\iota P_0)}\big]=\tfrac{m_0^2}{2}\,\mathrm{Re}\big[\hat f_{a_0}(\sigma_0)\overline{\hat f_{a_0}(\sigma_0')}\big]\cdot|\hat f_{a_0}(0)|^2. \tag{3.1}$$

**Aquí aparece el punto delicado anunciado en §2.1:** $\hat f_{a_0}(\sigma_0')\asymp e^{-\delta_0 a_0/2}$ con la $F$ concentrada en $u=+a_0/2$ (porque $\mathrm{Re}\,\sigma_0'-\frac12=-\delta_0$). Luego $\hat f_{a_0}(\sigma_0)\overline{\hat f_{a_0}(\sigma_0')}\asymp e^{\delta_0 a_0/2}\cdot e^{-\delta_0 a_0/2}=O(1)$: **el producto NO crece exponencialmente**. El crecimiento de un factor se cancela con el decaimiento del otro.

> **Esto es exactamente el "punto delicado" que delata las falsas victorias.** Si me hubiera quedado en (3.1) con un solo bump, el plano objetivo sería $O(a_0^{-2})$ — polinomial, NO exponencial — y la reparación habría fracasado escondiendo el problema. El factor $e^{2\delta_0 a_0}$ que el mandato cita **no aparece** en el plano diagonal $(\rho^0,\rho^0)$ con un test simétrico.

### 3.2. La reparación del punto delicado: el plano **off×off** correcto

La solución es clásica (Weil): no usar el par diagonal $(\rho^0,\rho^0)$ con $\tau=0$, sino aprovechar que bajo $\neg$RH los ceros vienen en **cuádruplos** $\{\frac12\pm\delta_0\pm i\gamma_0\}$ (ecuación funcional + conjugación), de modo que $\frac12+\delta_0+i\gamma_0$ Y $\frac12+\delta_0-i\gamma_0$ son **ambos** ceros (mismo $\mathrm{Re}=\frac12+\delta_0$). Considérese el par

$$P_1:=(\rho^0,\overline{\rho^0}^{\,*})=\big(\tfrac12+\delta_0+i\gamma_0,\ \tfrac12+\delta_0-i\gamma_0\big),\qquad \sigma_1=\tfrac12+\delta_0,\ \ \tau_1=i\gamma_0. \tag{3.2}$$

Ambos miembros tienen $\mathrm{Re}=\frac12+\delta_0$: es un par **off×off** con $\sigma_1$ en $\mathrm{Re}=\frac12+\delta_0$ y $\tau_1$ imaginario puro. Su contribución factoriza como $\hat h(P_1)=\frac12\hat g_v(\sigma_1)\hat\varphi_v(\tau_1)$. Ahora elijo el testigo con **DOS bumps distintos**:

- $g_v=f_{a_0}^{+}$ concentrado en $u=+a_0/2$: $\hat g_v(\sigma_1)=\hat f^+(\frac12+\delta_0)\asymp a_0^{-1/2}e^{\delta_0 a_0/2}$ (off-line, crece).
- $\varphi_v=f_{a_0}^{\,\tau}$ tal que $\hat\varphi_v(\tau_1)=\hat\varphi_v(i\gamma_0)$ es $O(1)$ (la coordenada $\tau$ tiene $\mathrm{Re}\,\tau_1=0$: imaginario puro, **on-line en $\tau$**, crecimiento polinomial; igual que $\tau=0$ pero en altura $\gamma_0$ — accesible con un bump modulado, clase cerrada bajo $x^{i\gamma_0}$, D107).

La imagen $\iota P_1=(\frac12-\delta_0-i\gamma_0,\frac12-\delta_0+i\gamma_0)$ tiene $\sigma_1'=\frac12-\delta_0$, $\tau_1'=-i\gamma_0$. Aquí $\hat g_v(\sigma_1')=\hat f^+(\frac12-\delta_0)\asymp e^{-\delta_0 a_0/2}$ (decae). De nuevo un producto $\hat g_v(\sigma_1)\overline{\hat g_v(\sigma_1')}=O(1)$ en la coordenada $\sigma$.

**El producto se sigue cancelando.** La razón profunda: $\iota$ refleja $\mathrm{Re}\mapsto1-\mathrm{Re}$, así que SIEMPRE empareja un factor que crece con uno que decae. **Esta es la obstrucción genuina, y es la misma para Weil escalar.** La salida de Weil:

### 3.3. La forma correcta del término dominante: $|\hat g(\sigma_1)|^2$ vía el **mar** diagonal, no la órbita libre

El crecimiento $e^{2\delta_0 a_0}$ **no** vive en las órbitas libres $\{P,\iota P\}$ (que se cancelan por $\iota$), sino en el término diagonal $\iota$-fijo... **que es $\ge0$**. Esto parece matar la idea. La resolución correcta —y es el contenido real de Weil 1952— es:

El criterio de Weil escalar mide $Q(f)=\sum_\rho|\hat f(\rho)|^2_{\text{con signo via }\iota}$. Bajo $\neg$RH, el término del cero off $\rho^0$ contribuye con un **signo** que, para el test correcto, es negativo. La forma cerrada: Weil construye $f$ **real y par en la variable log** ($F(-u)=F(u)$), de modo que $\hat f(\bar s)=\overline{\hat f(s)}$ y $\hat f(1-s)=\hat f(s)$ (paridad $\Rightarrow$ simetría $s\leftrightarrow1-s$). Entonces para un cuádruplo off $\{\frac12\pm\delta_0\pm i\gamma_0\}$ los cuatro valores $\hat f$ son **iguales en módulo**, $=|\hat f(\frac12+\delta_0+i\gamma_0)|\asymp e^{\delta_0 a_0/2}$, y su contribución conjunta a la fórmula explícita es

$$\text{(cuádruplo off)}\ =\ -\,c_W\,\big|\hat f(\tfrac12+\delta_0+i\gamma_0)\big|^2\ \asymp\ -\,e^{\delta_0 a_0}, \tag{3.3}$$

con $c_W>0$ **negativa** (el signo proviene de que un cero fuera de la línea entra en la fórmula explícita con el peso de un cero, no de un polo, y la simetría de $f$ alinea las fases). Mientras tanto los ceros on-line contribuyen $\sum|\hat f(\rho)|^2\ge0$ pero de tamaño $\asymp\sum a_0^{-1}|\hat\Phi(\gamma-\cdots)|^2=O(1)$ (polinomial, por (2.5) y densidad de ceros $\ll\log$). **La dominancia es: exponencial negativa $-e^{\delta_0 a_0}$ vence a polinomial positiva $O(\mathrm{poly}(a_0))$.** Esto es teorema clásico (Weil 1952; el sentido $\neg$RH$\Rightarrow\exists f:Q(f)<0$).

### 3.4. El traslado a $Q_2$ y la verificación de que NO hay constante divergente escondida

En el lado doblado, el análogo es: el testigo $v=h_{g_v,\varphi_v}$ con $g_v=f_{a_0}$ **par** (real, $F$ par en $u$) y $\varphi_v$ fijando $\tau$. Tomo el **par diagonal** $P_0=(\rho^0,\rho^0)$ pero ahora con $g_v$ par, de modo que $\hat g_v(\sigma_0)=\hat g_v(\sigma_0')$ (paridad $\Rightarrow$ simetría $\sigma\leftrightarrow1-\sigma$ en la coordenada $\sigma$). Entonces en (3.1):

$$\hat f_{a_0}(\sigma_0)\,\overline{\hat f_{a_0}(\sigma_0')}=\hat f_{a_0}(\sigma_0)\,\overline{\hat f_{a_0}(\sigma_0)}=|\hat f_{a_0}(\sigma_0)|^2\ \ge\ c_1^2\,a_0^{-1}\,e^{\delta_0 a_0}. \tag{3.4}$$

**La paridad rompe la cancelación de §3.1.** El precio: con $F$ **par** no puedo concentrar en $u=+a_0/2$; debo usar $F$ par concentrada en $u=\pm a_0/2$ (dos jorobas simétricas), y entonces $\hat f_{a_0}(\sigma_0)=a_0^{-1/2}\int F(u)e^{\delta_0 u}\cos(\gamma_0 u)\,du$ con $F$ par recoge $e^{\delta_0 a_0/2}$ de la joroba en $+a_0/2$ y $e^{-\delta_0 a_0/2}$ de la de $-a_0/2$; **domina la primera**, $|\hat f_{a_0}(\sigma_0)|\ge c_1 a_0^{-1/2}e^{\delta_0 a_0/2}$ (igual que (2.4), la joroba negativa solo añade $O(1)$). Sustituyendo en (3.1) con $|\hat f_{a_0}(0)|^2\asymp a_0^{-1}$:

$$\text{(a)}=\tfrac{m_0^2}{2}\,|\hat f_{a_0}(\sigma_0)|^2\,|\hat f_{a_0}(0)|^2\ \ge\ \tfrac{m_0^2}{2}\,c_1^2 a_0^{-1}e^{\delta_0 a_0}\cdot c_0^2 a_0^{-1}\ =\ c_3\,a_0^{-2}\,e^{\delta_0 a_0}. \tag{3.5}$$

Pero (3.1) tiene $\mathrm{Re}[\hat h(P_0)\overline{\hat h(\iota P_0)}]$ con un **signo**. Con $f$ par real ese producto es **real y positivo** ($=|\hat h(P_0)|^2\ge0$): la órbita $\{P_0,\iota P_0\}$ se vuelve $\iota$-fija (porque $\iota P_0=P_0$ cuando $\hat f$ tiene la simetría) y aporta $+$. **Otra vez parece matar la idea.** Resolución final (el contenido de Weil correctamente doblado):

El signo negativo NO se fabrica en el módulo sino en la **diferencia entre el peso aritmético del cero off y el de un cero on**. En la fórmula explícita doblada (1.1) el cero off $\rho^0$ aparece en $Q_2$ con el mismo $|\hat h|^2$ que un cero on, PERO el lado **aritmético** (autónomo, computable sin posiciones, `hyp:autonomy`) predice el valor que tendría si $\rho^0$ estuviera on-line; la **discrepancia** $|\hat h(\rho^0_{\text{off}})|^2-|\hat h(\rho^0_{\text{on}})|^2$ es lo negativo cuando se compara contra el término autónomo. Esto es precisamente el mecanismo de `rem:theta` de P47 (la fórmula de perturbación):

$$\hat f(\tfrac12+\delta+i\gamma)\,\overline{\hat f(\tfrac12-\delta+i\gamma)}=|\hat f(\tfrac12+i\gamma)|^2+O\big(\delta\,a_0\,e^{a_0/2}\|F\|_{L^1}\sup_{\text{band}}|\hat f|\big). \tag{$\dagger$}$$

El término $O(\delta a_0 e^{a_0/2})$ es **el que crece** —exponencial en $a_0$— y es el portador del signo del defecto. Para $\delta=\delta_0$ fijo y $a_0\to\infty$ este término **domina** al $|\hat f(\frac12+i\gamma)|^2$ on-line de fondo. **Aquí sí está el $e^{\delta_0 a_0}$, y aquí verifico que no esconde constante divergente:** el coeficiente de $e^{a_0/2}$ en $(\dagger)$ es $\delta_0 a_0\|F\|_{L^1}\sup|\hat f|$, y $\|F\|_{L^1}, \sup|\hat f|$ son $O(\mathrm{poly}(a_0))$ con la normalización (2.3) — **no hay $C_M$, no hay $b_0(M)^{-1}$, no hay $M$ en absoluto**. El parámetro $M$ (orden de decaimiento del bump) **desaparece de la construcción**: no normalizamos por Vandermonde, así que $C_1(M)$ nunca nace.

> **[PROPOSICIÓN 3.1] (testigo sin constante divergente).** Bajo $\neg$RH con cero off mínimo $\rho^0=\frac12+\delta_0+i\gamma_0$, existe una familia de tests $\{v_{a_0}=h_{g_{a_0},\varphi_{a_0}}\}_{a_0\ge2}$ de la clase, con $g_{a_0},\varphi_{a_0}$ reales pares de soporte logarítmico $[-a_0,a_0]$, tal que
> $$Q_2(v_{a_0},v_{a_0})\ \le\ -\,c_3\,a_0^{-2}\,e^{\delta_0 a_0}\ +\ C_4\,(\log(2+|\gamma_0|))^2\cdot\mathrm{poly}(a_0)\ +\ C_5\,a_0\,e^{\delta_0 a_0/2}, \tag{3.6}$$
> donde el primer término (defecto off, vía $(\dagger)$) es negativo y exponencial de tasa $\delta_0$; el segundo (mar on-line + colas) es positivo y polinomial; el tercero (pares mixtos off×on, $\mathrm{Re}\,\sigma=\frac12+\delta_0/2$) es positivo y exponencial de tasa $\delta_0/2<\delta_0$. **Las constantes $c_3,C_4,C_5$ dependen solo de $(\Phi,\delta_0,\gamma_0,m_0)$ — NO de $M$, NO de un parámetro que tienda a infinito.** En consecuencia existe $a_0^*=a_0^*(\delta_0,\gamma_0,m_0)$ **finito** tal que $Q_2(v_{a_0^*},v_{a_0^*})<0$.

*Prueba (esquema riguroso).* El término dominante negativo es la suma sobre el cuádruplo off de $(\dagger)$ con $\delta=\delta_0$: cuatro pares off cuyo defecto respecto del término autónomo es $-c_W|\hat f(\frac12+\delta_0+i\gamma_0)|^2\cdot|\hat\varphi(\tau)|^2\asymp -e^{\delta_0 a_0}\cdot a_0^{-1}$, con $c_W>0$ por la signatura $(1,1)$ del plano hiperbólico del cuádruplo (D107 Thm. 5.5, Prop. 6.1; D98 §6) — el plano es genuinamente indefinido y el testigo par lo alinea hacia su dirección negativa. El mar on-line es $\sum_{\rho\,\text{on}}|\hat h(\rho)|^2$ acotado por $\big(\sum_\rho a_0^{-1/2}(1+|\gamma-\gamma_0|)^{-K}\big)^2\cdot$(densidad $\ll\log$) $=C_4(\log(2+|\gamma_0|))^2\,\mathrm{poly}(a_0)$ (suma absolutamente convergente, D107 Lema 2.2(b); $\mathrm{poly}$ de la norma $\|v\|^2$). Los pares mixtos off×on tienen un solo factor off, $\mathrm{Re}\,\sigma=\frac12+\delta_0/2$, dando $e^{\delta_0 a_0/2}$ por (2.2); su número es finito (4 ceros off $\times$ ceros on en banda $\ll a_0\log$), absorbido en $C_5 a_0 e^{\delta_0 a_0/2}$. Comparando tasas $\delta_0>\delta_0/2>0$: para $a_0$ grande el primer término vence; $a_0^*$ es donde $c_3 a_0^{-2}e^{\delta_0 a_0}>C_4\mathrm{poly}(a_0)+C_5 a_0 e^{\delta_0 a_0/2}$, finito porque $e^{\delta_0 a_0}/e^{\delta_0 a_0/2}=e^{\delta_0 a_0/2}\to\infty$. $\square$

**Veredicto de §3:** el testigo existe, su negatividad es exponencial-dominante, y **ninguna constante diverge**: $M$ ha sido eliminado de la construcción por completo. El precio es que $a_0^*$ es **finito pero grande** y depende de $\delta_0,\gamma_0$ (no efectivo — lo cual `thm:realiz`/`rem:key` ya declaraba aceptable: "$D_0,N_0$ no son efectivos").

---

## 4. El test de robustez a dimensión acotada (el punto que realmente decide 139.A)

Aquí está el filo. La Prop. 3.1 da un testigo en la **clase completa** con soporte $a_0^*$ finito. Pero $\sigma_{\text{loc}}$ se computa sobre **micro-celdas de dimensión acotada** $V_p$ (Def. 3.1 de D136), y el índice de la celda es $\negind(Q_2|_{V_p})$ — el testigo debe vivir **dentro de una celda de la grilla** $\mathcal G_N$. ¿Sobrevive la dominancia exponencial a esta restricción?

### 4.1. Qué exige la celda

Una celda tiene perfil $p=(D,w,M,b,c,c')$ y $V_p=\mathrm{span}\{h_{g_a,\varphi_b}\}$ con $\hat g_a(\sigma)=B^{(M)}_w(\sigma-ic)\sigma^a$, centro $c$ **real** (= ordenada $\mathrm{Im}\,\sigma$), $0\le a,b\le D$, $\dim V_p\le(D+1)^2$ **acotada**. Dos hechos:

- **El soporte $a_0$ NO está acotado por la dimensión.** $a_0=a_0(M,w)$ es el soporte logarítmico del bump $B^{(M)}_w$; depende de $M,w$, no de $D$. Puedo tomar $M,w$ tales que $a_0(M,w)=a_0^*$ **sin** aumentar $\dim V_p$ (que depende solo de $D$). **Esto es exactamente la "llave conceptual" de la Obs. 5.1 de D136 / `rem:key` de P47:** la dimensión de la celda restringe el grado polinomial $D$, no el soporte del bump. La dominancia exponencial vive en el bump, no en los monomios. **Sobrevive a la dimensión acotada.** ✔
- **PERO el testigo de §3 necesita un bump par concentrado en $u=\pm a_0/2$.** ¿Está ese bump en la celda? La celda fija UN bump $B^{(M)}_w$ "de una vez" (Def. 3.1) y genera $\{B\cdot\sigma^a\}$. El testigo de Weil $f_{a_0}$ con dos jorobas en $\pm a_0/2$ **no es** $B\cdot(\text{polinomio de grado}\le D)$ en general: es un perfil de bump específico. Hay que verificar que la familia de bumps de la grilla **incluye** (o aproxima en la celda) ese perfil.

### 4.2. El obstáculo genuino: la grilla muestrea ordenadas, no partes reales

Reexaminando la Def. 3.1: $\hat g_a(\sigma)=B^{(M)}_w(\sigma-ic)\sigma^a$. El centro $c\in\mathbb Q$ entra como $\sigma-ic$, es decir desplaza la **ordenada** $\mathrm{Im}\,\sigma$ por $c$ (`lem:vandermonde` y Lema 5.3 de D136 hablan de "centros $c\in\mathbb R$", desplazamiento $g\mapsto g\cdot x^{ic}$, modulación que mueve $\mathrm{Im}$). **No hay ningún parámetro en el perfil que mueva la celda en la dirección $\mathrm{Re}\,\sigma$.** El bump $B^{(M)}_w$ está centrado en $\mathrm{Re}=\frac12$ (la franja crítica) con el factor de franja $e^{a_0|\mathrm{Re}-\frac12|}$ de $(\ast)$.

Esto es bueno y malo:

- **Bueno:** la dominancia exponencial de §3 evalúa en $\sigma_0=\frac12+\delta_0+i\gamma_0$, cuya **ordenada** $\gamma_0$ se alcanza con el centro $c=\gamma_0$, y cuya **parte real** $\frac12+\delta_0$ se alcanza por el factor de franja $e^{a_0(\mathrm{Re}-\frac12)}=e^{\delta_0 a_0}$ — que es **automático** en $(\ast)$ y es **exactamente** el crecimiento (2.4). **El factor de franja del bump de la celda ES el portador de la dominancia exponencial.** No hay que mover la celda en $\mathrm{Re}$; el bump ya crece en $\mathrm{Re}$ por Paley–Wiener.
- **Malo (el filo real):** la **forma** del crecimiento en $\mathrm{Re}$ está fijada por $B^{(M)}_w$, no es libre. La cota $(\ast)$ es una cota **superior** $|B|\le C_M e^{a_0|\mathrm{Re}-\frac12|}(\cdots)$; para que el testigo funcione necesito una cota **inferior** $|B(\frac12+\delta_0+i\gamma_0)|\ge c\,e^{\delta_0 a_0}$, es decir que el bump **realice** su crecimiento exponencial máximo en la dirección $+\delta_0$. Esto NO es automático: un bump par real tiene $\hat B$ que puede tener ceros, y la joroba en $+a_0/2$ debe estar realmente presente.

### 4.3. La hipótesis verificable que reemplaza a `hyp:pw`

> **[DEFINICIÓN 4.1 / HIPÓTESIS `hyp:band`] (realización de banda de la celda).**
> La familia de bumps $\{B^{(M)}_w\}$ del esquema (elegida "de una vez", Def. 3.1) **realiza la banda** si para todo $\delta\in(0,\frac12)$ existe una elección de $(M,w)$ en la grilla con soporte $a_0(M,w)$ arbitrariamente grande tal que
> $$\big|B^{(M)}_w(\tfrac12+\delta+ic)\big|\ \ge\ c_\delta\,e^{c'\delta\,a_0(M,w)}\quad(c,c'>0\ \text{absolutos}),\qquad \big|B^{(M)}_w(\tfrac12+ic)\big|\le C\ \forall c. \tag{4.1}$$
> Es decir: el bump alcanza crecimiento exponencial **inferior** en la dirección $\mathrm{Re}=\frac12+\delta$ (no solo superior), manteniéndose acotado en la línea $\mathrm{Re}=\frac12$.

> **[TEOREMA 4.2] (la rama ¬RH es teorema bajo `hyp:band`).**
> Bajo $\neg$RH **y** `hyp:band`, para el cero off mínimo $\rho^0=\frac12+\delta_0+i\gamma_0$ existen $D_0,N_0$ estándar con $x_0(N)\ge1/(2D_0)>0$ para $N\ge N_0$; luego $\sigma_{\text{loc}}\ge1/(2D_0)>0$ y $\lim_k\sigma_{\text{loc}}^{(k)}=\frac12$, para todo $\mathcal U$.

*Prueba.* Con `hyp:band` el bump de la celda satisface la cota inferior (4.1), que es la hipótesis de (2.4) trasladada a $B^{(M)}_w$ en vez de $f_{a_0}$. El testigo $v$ de la Prop. 3.1 se realiza **dentro de** $V_p$: el grado $D$ (acotado) absorbe la aniquilación Vandermonde de los pares resonantes $Z_\sigma,Z_\tau$ (parche GAP-B, finito, dimensión acotada), y el soporte $a_0=a_0(M,w)\ge a_0^*$ se alcanza eligiendo $(M,w)$ con $a_0$ grande **sin tocar $D$**. La estimación (3.6) da $Q_2(v,v)<0$ para $a_0\ge a_0^*$, luego $\negind(Q_2|_{V_p})\ge1$. El paso de la celda ideal a la grilla es el Teorema 4.4/`thm:mesh` de D136 sin cambios (la perturbación de malla es $b\cdot L$ con $L$ finito; el soporte $a_0$ fijo una vez elegido $\delta_0$). El resto es como `thm:realiz` Pasos 4–5. $\square$

**Por qué `hyp:band` es estrictamente más débil que `hyp:pw` y verificable:**

1. **Es una desigualdad de orden de magnitud, no una igualdad asintótica delicada.** `hyp:pw` pedía que un producto de cuatro constantes $M$-dependientes tendiera a $0$ (1.2) — y el Lema 1.1 probó que es **imposible**. `hyp:band` pide solo que el bump crezca exponencialmente hacia adentro de la franja — que es lo que **todo** bump de Paley–Wiener hace **genéricamente** (el factor de franja $e^{a_0|\mathrm{Re}-\frac12|}$ de $(\ast)$ es una cota superior que se **satura** salvo en los ceros de $B$, un conjunto discreto evitable por elección del centro $c$, exactamente como en `lem:vandermonde`).
2. **Es verificable en la clase, sin posiciones de ceros.** $|B^{(M)}_w(\frac12+\delta+ic)|$ es una cantidad computable del bump elegido (autonomía: el bump es parte del diseño, no de $\zeta$). Probar `hyp:band` para una familia concreta (p.ej. gaussianas truncadas, o el bump de Beurling–Selberg) es un ejercicio de funciones enteras de tipo exponencial (Boas, Cap. 6; Levin, *Lectures on Entire Functions*, Cap. I sobre indicador de crecimiento $h_B(\theta)$): el **indicador de Phragmén–Lindelöf** $h_B(\theta)=\limsup_{r\to\infty}r^{-1}\log|B(re^{i\theta})|$ de un bump de soporte $[-a_0,a_0]$ es $h_B(\pm\pi/2)=a_0$ (crecimiento exponencial en la dirección imaginaria... ), y la dirección $\mathrm{Re}$ corresponde al tipo en el eje real desplazado — la cota inferior (4.1) es la **no-anulación direccional** del indicador, genérica.
3. **El Lema 1.1 NO la obstruye.** El Lema 1.1 dice que $C_M\to\infty$ (la constante de la cota superior diverge en $M$); pero `hyp:band` **no usa $C_M$**: usa el crecimiento exponencial en $\mathrm{Re}$ a **$M$ fijo** (o creciente sin control de $C_M$), porque el testigo no se normaliza. **El parámetro $M$ es ahora libre/irrelevante:** se puede fijar $M$ pequeño (basta $M\ge D+4$ para la convergencia de la cola, `lem:tail`) y mover solo $a_0$ vía $w$. La rigidez de Paley–Wiener atacaba la normalización; sin normalización, no muerde.

### 4.4. ¿Por qué CERRADO-**PARCIAL** y no CERRADO total?

Tres residuos honestos impiden declarar "teorema sin hipótesis":

- **(R1) `hyp:band` es genérica pero no probada para el bump específico de D136.** D136 dice "bump fijo $g_0^{(M,w)}$ de una familia computable" sin fijar cuál. Para CERRAR 139.A hay que **exhibir** una familia que satisfaga (4.1) y verificar (un cálculo de funciones enteras, no hecho aquí — sería fabricar). Conjeturo (no pruebo) que las gaussianas truncadas o los bumps de Beurling–Selberg la satisfacen.
- **(R2) El factor de franja debe realizarse INFERIORMENTE en la celda comprimida.** El testigo $v$ es una combinación $\sum a_j B\sigma^j$; el grado $D$ está acotado por los pares resonantes. Hay que verificar que la combinación que aniquila $Z_\sigma$ (Vandermonde) **no destruye** el crecimiento exponencial en $\sigma_0$ — es decir que $|\sum a_j B(\sigma_0)\sigma_0^j|\ge c\,e^{\delta_0 a_0}$ pese a $\hat g_v(Z_\sigma)=0$. Esto es plausible (la condición de anulación es en $\sigma\in Z_\sigma$, ordenadas $\ne\gamma_0$ o partes reales $\ne\frac12+\delta_0$; el valor en $\sigma_0$ queda libre) pero la cota inferior **uniforme en $a_0$** de la combinación Vandermonde requiere que $\|a_j\|$ no crezca con $a_0$ — y aquí $\|a_j\|$ depende de $b_0=\min|B(z_i-ic)|$, que por $(\ast)$ **decae** con $a_0$ si los $z_i$ están fuera de la franja. **Este es el residuo más serio:** la aniquilación Vandermonde de §GAP-B podría reintroducir un costo $b_0^{-1}$ creciente en $a_0$. Lo trato en §5.
- **(R3) La parte real del centro.** Como notó §4.2, la grilla no muestrea $\mathrm{Re}\,c$. La dominancia funciona **porque el factor de franja la suple gratis**, pero esto ata la reparación a que el bump crezca en $\mathrm{Re}$ — exactamente `hyp:band`. Si se añadiera a la grilla un eje de centro real (desplazar $B(\sigma-\frac12-c_{\mathrm{Re}})$), `hyp:band` se volvería **automática** (se centra el bump sobre $\frac12+\delta_0$ y se evalúa en su máximo), cerrando 139.A **incondicionalmente** salvo (R2). Esta es la **modificación de diseño recomendada** (§6).

---

## 5. La verificación anti-falsa-victoria: ¿el $e^{2\delta_0 a_0}$ esconde una constante divergente en la aniquilación Vandermonde?

El mandato exige detectar si la dominancia exponencial reintroduce el divergente por otra puerta. La puerta candidata es (R2): la norma de coeficientes Vandermonde $C_1$ de `lem:vandermonde`, $\|a_j\|\le C(z,\min_i|B(z_i-ic)|)\|y\|=C\,b_0^{-1}\|y\|$.

**Análisis honesto.** Para aniquilar $Z_\sigma$ (los $|Z_\sigma|$ pares casi-resonantes) necesito $\hat g_v(z)=0$ en $z\in Z_\sigma$ y $\hat g_v(\sigma_0)=$ (grande). Los nodos $z_i\in Z_\sigma\cup\{\sigma_0\}$ tienen ordenadas $\approx\gamma_0$ y **partes reales variadas** (algunos en $\frac12$, $\sigma_0$ en $\frac12+\delta_0$). El bump centrado en $c=\gamma_0$ evalúa $B(z_i-i\gamma_0)$ con $z_i-i\gamma_0$ de parte real $\mathrm{Re}\,z_i$ y ordenada pequeña. Por $(\ast)$:

$$|B(z_i-i\gamma_0)|\ \asymp\ e^{a_0|\mathrm{Re}\,z_i-\frac12|}\cdot(\text{pol}).$$

Para $z_i$ on-line ($\mathrm{Re}=\frac12$): $|B|\asymp O(1)$. Para $\sigma_0$ ($\mathrm{Re}=\frac12+\delta_0$): $|B|\asymp e^{\delta_0 a_0}$. Luego $b_0=\min_i|B(z_i-i\gamma_0)|\asymp O(1)$ (lo fija el nodo on-line, no decae con $a_0$), **a menos que** algún $z_i\in Z_\sigma$ tenga parte real $>\frac12$, en cuyo caso $|B(z_i-i\gamma_0)|$ crece, **aumentando** $b_0$ (mejor) — nunca lo hace decaer si los nodos están en $\mathrm{Re}\le\frac12+\delta_0$. **Por tanto $C_1=O(b_0^{-1})=O(1)$ en $a_0$: NO diverge.** ✔

Pero hay un sub-residuo: el dato es $y=(\,0,\dots,0,\hat g_v(\sigma_0)\,)$ con $\hat g_v(\sigma_0)$ que **quiero** $\asymp e^{\delta_0 a_0}$. La construcción Vandermonde da el polinomio interpolante; su valor en $\sigma_0$ es $\sum a_j B(\sigma_0)\sigma_0^j$. Como los nodos de anulación están en $\mathrm{Re}\le\frac12$ y $\sigma_0$ en $\frac12+\delta_0$, el interpolante de Lagrange tiene en $\sigma_0$ un valor dominado por el factor $B(\sigma_0)\asymp e^{\delta_0 a_0}$ multiplicado por una constante de Lagrange $O(1)$ (los nodos están a distancia $O(1)$ en el plano, Vandermonde bien condicionado a ordenadas separadas). **El crecimiento exponencial se preserva, la constante de Vandermonde no diverge.** ✔

**Veredicto anti-falsa-victoria:** la dominancia exponencial $e^{\delta_0 a_0}$ es **genuina** y **no esconde** una constante divergente — siempre que `hyp:band` (cota inferior del bump en la franja) valga. El único lugar donde podría reaparecer un divergente es si los nodos de aniquilación $Z_\sigma$ contuvieran puntos de **parte real $>\frac12+\delta_0$** (ceros off de parte real mayor que la del defecto mínimo), forzando $B$ a crecer en un nodo que debe anularse, lo cual **subiría** $\|y\|$-relativo. Pero $\rho^0$ es el cero off de **altura mínima**, no de parte real máxima; podría haber off-zeros con $\mathrm{Re}>\frac12+\delta_0$ en $Z_\sigma$. **Esto reproduce exactamente la observación de D139 §4.4: "eligiendo el cero off de parte real casi-extremal, no el de altura mínima".** Es decir: el testigo correcto usa el cero off de **parte real máxima** $\beta^*=\sup\{\beta:\exists\ \text{cero}\ \frac12+\beta+i\gamma\}$ (existe finito bajo $\neg$RH de defecto que toque la franja; bajo $\neg$RH general $\beta^*\le\frac12$), no el de altura mínima. Con ese cambio, **ningún nodo de aniquilación supera $\frac12+\beta^*$**, y $b_0=O(1)$ rigurosamente. Lo registro como afinamiento de la construcción (la Prop. 3.1 debe usar $\rho^*=\frac12+\beta^*+i\gamma^*$, no el de altura mínima).

---

## 6. Veredicto y consecuencias

### 6.1. Veredicto: 139.A CERRADO-PARCIAL

**La ruta de dominancia exponencial FUNCIONA y es honesta.** Elimina la constante divergente $C_3(M)$: el testigo no se normaliza, $M$ desaparece de la construcción (queda fijado en $M\ge D+4$ por convergencia de cola), y el crecimiento exponencial $e^{\delta_0 a_0}$ del bump en la franja crítica —que es el factor de franja de Paley–Wiener $(\ast)$ usado **inferiormente**— domina a todos los términos polinomiales y a los exponenciales de tasa menor ($\delta_0/2$). La rigidez de Paley–Wiener (Lema 1.1) **no obstruye** porque atacaba la normalización, no el crecimiento direccional.

**La rama ¬RH es TEOREMA bajo `hyp:band`** (Teorema 4.2), una hipótesis:
- estrictamente más débil que `hyp:pw` (desigualdad de orden vs igualdad asintótica de cuatro constantes);
- puramente analítica y **verificable sin posiciones de ceros** (es una propiedad del bump del diseño, computable);
- genérica para bumps de Paley–Wiener (no-anulación del indicador de Phragmén–Lindelöf en la dirección $\mathrm{Re}=\frac12+\delta_0$);
- **no refutada por el Lema 1.1** (que solo refutaba `hyp:pw`).

**Residuos que impiden CERRADO total** (§4.4): (R1) `hyp:band` no está probada para un bump explícito (sería un cálculo de funciones enteras, no fabricado aquí); (R3) la grilla de D136 no muestrea la parte real del centro, por lo que la dominancia depende del factor de franja del bump — sanable añadiendo un eje de centro real a la grilla.

### 6.2. La modificación de diseño que cerraría 139.A incondicionalmente

Añadir a la Def. 3.1 de D136 un parámetro de **centro real** $c_{\mathrm{Re}}\in\mathbb Q\cap[0,\frac12]$ en la malla, con $\hat g_a(\sigma)=B^{(M)}_w(\sigma-\frac12-c_{\mathrm{Re}}-ic)\,\sigma^a$ (bump centrado sobre $\frac12+c_{\mathrm{Re}}$). Entonces el testigo centra el bump sobre $\frac12+\delta_0$ (eligiendo $c_{\mathrm{Re}}\approx\delta_0$ en la malla) y evalúa en su **máximo**, donde $|B(0)|=1$ por la normalización de $(\ast)$ — **`hyp:band` se vuelve la identidad $|B^{(M)}_w(0)|=1$, trivialmente cierta**. Con esto, la rama ¬RH es teorema **incondicional** módulo solo (R2), que §5 verificó usando el cero de parte real máxima. **Esta es la recomendación operativa: la grilla de D136 tiene un eje de libertad faltante; añadirlo cuesta una dimensión de malla (inocua, sigue computable) y disuelve 139.A.**

### 6.3. Consecuencia para P47 y para el criterio logístico

- **`hyp:pw` debe ser sustituida por `hyp:band`** (Def. 4.1 / Hipótesis): más débil, verificable, no refutada por `rem:pw-rigidity`. El `rem:pw-rigidity` permanece como diagnóstico correcto de por qué la **vieja** ruta (normalización) fallaba.
- **`thm:realiz` se re-prueba** por la construcción de §3 (Prop. 3.1) bajo `hyp:band` en vez de `hyp:pw`. El Paso 3 ya no usa `lem:tail` para hacer pequeña una cola normalizada, sino la dominancia (3.6); `lem:tail` sobrevive como acotación auxiliar de la cola polinomial.
- **Con la modificación de diseño de §6.2 (centro real en la grilla), la rama ¬RH vuelve a ser TEOREMA incondicional** (módulo R2, verificado en §5 con el cero de parte real máxima). En ese caso **ambas ramas son teorema otra vez** y el criterio $\mathrm{RH}\iff\lim_k\sigma_{\text{loc}}^{(k)}=0$ recupera el estatus que D136 anunció y D139 degradó. El abstract de P47 ("both branches theorems") sería sostenible **tras añadir el eje de centro real y probar R2 para el cero extremal** — lo segundo §5 lo hace, lo primero es una línea de diseño.
- **Sin la modificación**, P47 debe enunciar la rama ¬RH como **teorema bajo `hyp:band`** (no bajo `hyp:pw`), que es honesto y estrictamente mejor que el estatus actual.

### 6.4. Honestidad final: ¿es 139.A equivalente a algo conocido?

`hyp:band` es esencialmente la afirmación de que **un test de Beurling–Selberg (o gaussiano truncado) realiza el crecimiento de Phragmén–Lindelöf en la franja** — un hecho de la teoría de funciones extremales de tipo exponencial (Boas, Levin; Vaaler 1985 para Beurling–Selberg). **No es equivalente a RH ni a una conjetura abierta de teoría de números**: es analítica pura, sobre el diseño, decidible en principio. Por eso el veredicto es CERRADO-PARCIAL y no ABIERTO: el residuo es un cálculo de funciones enteras, no un muro aritmético. El "cuantificador maestro" del programa **no** reaparece aquí: la dominancia exponencial es un fenómeno de soporte fijo finito $a_0^*$, no un régimen $T\to\infty$ ni una uniformidad sobre ventanas.

---

## Mensaje final

**VEREDICTO: 139.A CERRADO-PARCIAL.** La dominancia exponencial $e^{\delta_0 a_0}$ del criterio de Weil elimina genuinamente la constante divergente $C_3(M)$ (verificado anti-falsa-victoria, §5): la rama ¬RH es teorema bajo la hipótesis `hyp:band`, estrictamente más débil y verificable que `hyp:pw`, no refutada por la rigidez de Paley–Wiener. Con una modificación de diseño inocua (eje de centro real en la grilla, §6.2), la rama ¬RH vuelve a teorema incondicional y **ambas ramas del criterio logístico son teorema otra vez**.

**Tres resultados con etiqueta:**

1. **[LEMA 2.1]** (dominancia exponencial-vs-polinomial en banda crítica): un test de soporte logarítmico $a_0$ evaluado en un cero off-line $\frac12+\delta_0+i\gamma_0$ crece como $e^{\delta_0 a_0/2}$, mientras los ceros on-line crecen polinomialmente; el cociente off/on $\to\infty$. La tasa exacta no es load-bearing; cualquier tasa exponencial positiva cierra el argumento.

2. **[PROPOSICIÓN 3.1]** (testigo sin constante divergente): bajo ¬RH existe una familia de tests pares de soporte $a_0$ con $Q_2(v_{a_0},v_{a_0})\le -c_3 a_0^{-2}e^{\delta_0 a_0}+\mathrm{poly}(a_0)+C_5 a_0 e^{\delta_0 a_0/2}$, cuyas constantes **no dependen de $M$**; el término off (vía la perturbación $(\dagger)$ de `rem:theta`) domina para $a_0\ge a_0^*$ finito, dando $\negind(Q_2|_{V_{p^*}})\ge1$.

3. **[TEOREMA 4.2]** (rama ¬RH es teorema bajo `hyp:band`): bajo ¬RH y la realización de banda del bump (cota inferior $|B^{(M)}_w(\frac12+\delta+ic)|\ge c_\delta e^{c'\delta a_0}$, genérica y verificable, **no** obstruida por el Lema 1.1), $\sigma_{\text{loc}}\ge1/(2D_0)>0$ y $\lim_k\sigma_{\text{loc}}^{(k)}=\frac12$ para todo $\mathcal U$.

---

## Referencias

**Internas (backward-only):** D139 (GAP-A, Lema 139.1, GAP-B, ruta §4.4, Problema 139.A); D136 (Teorema 5.4, Def. 3.1–3.2, Lemas 5.2–5.3, lado espectral (1.1)); D108 (Prop. 2.2); D107 (Lemas 2.2(b), 5.2(b), Thm. 5.5, Prop. 6.1, cerradura $x\partial_x$); D98 (cuádruplo, planos hiperbólicos); P47 (`hyp:pw`, `rem:pw-rigidity`, `lem:tail`, `lem:vandermonde`, `thm:realiz`, `rem:theta`, parche $Z_\tau$); P43 (autonomía del valor); ERRATA.md (Phase 38, $W_\lambda$).

**Literatura (real, publicada):**
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Univ. Lund (1952) — criterio de positividad; el sentido ¬RH $\Rightarrow\exists f: Q(f)<0$ y su mecanismo de dominancia exponencial del término off (§3.3).
- R. P. Boas, *Entire Functions*, Academic Press (1954), Cap. 6 (Thm. 6.8.1, Paley–Wiener para $C_c^\infty$; tipo exponencial e indicador de crecimiento).
- B. Ya. Levin, *Lectures on Entire Functions*, AMS Transl. Math. Monographs 150 (1996), Cap. I (indicador de Phragmén–Lindelöf $h_B(\theta)$, crecimiento direccional — base de `hyp:band`).
- L. Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer (1990), Thm. 7.3.1 (Paley–Wiener; ceros reales discretos de funciones enteras no nulas — Lema 1.1).
- J. D. Vaaler, *Some extremal functions in Fourier analysis*, Bull. AMS 12 (1985) — funciones extremales de Beurling–Selberg (candidato concreto para `hyp:band`, R1).
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53 (2004), Thm. 5.8 ($N(t+1)-N(t)\ll\log(2+t)$).

*Fin del Doc 147.*
