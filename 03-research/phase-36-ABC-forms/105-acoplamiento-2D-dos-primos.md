# Documento 105 — El acoplamiento $\partial_t$–$\partial_x$: primera prueba de la Forma A en el aproximante de 2 primos

**Programa:** Hipótesis de Riemann — Fase 36 (Formas A, B, C)
**Fecha:** junio 2026
**Autor:** David Alejandro Trejo Pizzo
**Prerrequisitos:** Docs 63, 64, 69, 70, 71, 72, 99, 103; P39, P41 (§ Form A, Problema 6.2)
**Regla de honestidad:** todo paso no probado se declara GAP ABIERTO; toda afirmación no verificada contra fuente lleva [NO VERIFICADO]. Sin numéricos: todos los valores que aparecen son formas cerradas exactas (aritmética racional y radicales), con verificación algebraica en el Apéndice A.

---

## 0. Resumen ejecutivo

La Forma A de P41 (Problema 6.2) propone una traza conjunta $\mathcal{T}(t,x)$ —el aproximante de Euler finito indexado por $x$, evolucionado por el flujo de De Bruijn–Newman (DBN) hasta tiempo $t$— y pregunta si una desigualdad diferencial que acople $\partial_t$ con $\partial_x$ puede propagar la positividad desde los dos bordes (teoremas incondicionales) hasta la esquina $(t,x)=(0,\infty)$ (RH). Este documento ejecuta el primer test finito y honesto declarado en P41: el aproximante de dos primos $S=\{2,3\}$.

**Resultados principales:**

1. **Teorema de degeneración del interior (§3).** Con la única definición de $\mathcal{T}$ que hace *ambos* bordes teoremas ya probados (la completación CF de Doc 99 + flujo DBN), se tiene $\mathcal{T}(t,x)=0$ para **todo** $x$ finito y **todo** $t\geq 0$, no solo en los bordes. La razón es estructural: el flujo de calor DBN *preserva* la realidad de los ceros hacia adelante en el tiempo (herencia de de Bruijn), y la propiedad que define el borde $\{x\text{ finito}\}$ es exactamente esa realidad. En consecuencia $\partial_t\mathcal{T}=\Delta_x\mathcal{T}=\partial_t\Delta_x\mathcal{T}=0$ idénticamente en el interior del cuadrante: **toda desigualdad parabólica es vacua y nada se propaga a la esquina**, que queda como discontinuidad pura cuya continuidad es, otra vez, el muro 1D de P41 §5.1.

2. **Cálculo exacto del libro mayor de Weil (§5).** En el único lugar donde las variaciones son no triviales (el borde $x=\infty$, vía Doc 72), el incremento por primo se calcula **en forma cerrada**: para la ventana de Abel mínima $N(\lambda_0)=1$,
$$B_{\lambda_0}(r)=\frac{(\cosh r)^{-1/2}}{8}\Bigl(5-78\,\mathrm{sech}^2 r+105\,\mathrm{sech}^4 r\Bigr),$$
de donde los incrementos $\delta_p=-(\log p/\sqrt p)\,B_{\lambda_0}(\log p)$ son **positivos para $p=2,3,5,7$ y negativos para todo $p\geq 11$** (cambio de signo exacto, racional), y la suma sobre primos **diverge marginalmente** como $-(5\sqrt2/8)\log$ (tipo Mertens). El test de signo de la Forma A falla por partida doble: degeneración total en el interior y oscilación de signo sin diagonal monótona en la frontera.

3. **Correcciones a Docs 70–71 (§4).** El flujo DBN satisface $\partial_t H_t=-\partial_{ss}H_t$ (calor *hacia atrás* en la variable espectral), no $+\partial_{ss}H_t$ como está escrito en Doc 70 §5.2; la fórmula de la derivada temporal se rederiva limpia ($\partial_t T|_0 = D(\Xi)-D(\Xi^{on})$ con $D$ explícito) y el análisis de signo del Doc 71 §4 (heurística del "Término I dominante") queda invalidado: omitía la parte on-critical y el término de normalización. El signo de $\partial_t T_\lambda|_{t=0}$ bajo $\neg$RH queda ABIERTO.

**VEREDICTO (§9): RUTA CERRADA** para la Forma A con $\mathcal{T}=$ traza de discrepancia, por degeneración (no por oscilación caótica, que también ocurre en la frontera). Queda nombrado el único objeto de reemplazo no descartado (Forma A′, §8), que ya no es la Forma A y hereda la sospecha E4 de Doc 99.

---

## 1. El objeto conjunto: tres definiciones candidatas y la decisión de diseño

### 1.1. Lo que la Forma A exige

P41 (§ Form A) pide un campo escalar $\mathcal{T}(t,x)$ sobre el cuadrante $\{t\geq 0\}\times\{x\in[2,\infty]\}$ tal que:

- **(B1)** Borde temporal: $\mathcal{T}(t,\infty)=0$ para $t\geq\Lambda$, incondicional (DBN; Docs 70–71).
- **(B2)** Borde aritmético: para $x$ finito, control incondicional ("ceros reales del aproximante", rigidez CF; Doc 99).
- **(C)** Esquina: $\mathcal{T}(0,\infty)=0\iff$ RH.

y pregunta si existe acoplamiento diferencial $\partial_t$–$\partial_x$ que propague la positividad de (B1)+(B2) hacia (C).

### 1.2. Las tres definiciones posibles del aproximante evolucionado

**Definición (a) — flujo de calor sobre el producto de Euler puntual.** $\zeta_x(s):=\prod_{p\leq x}(1-p^{-s})^{-1}$ y $dm_x=|\zeta_x(\tfrac12+is)|^2\,dm_\infty$ (Doc 99, Lema 6.4), evolucionada por calor. **Defecto fatal 1:** $\zeta_x(\tfrac12+is)$ no es entera en $s$ (tiene polos en $\operatorname{Im} s=\tfrac12$, i.e. $\operatorname{Re}\sigma=0$) y *no tiene ceros en absoluto* en la banda crítica: cada factor $(1-p^{-1/2-is})^{-1}$ no se anula nunca para $s$ real ni en ninguna parte ($|p^{-1/2-is}|=p^{-1/2}<1$ sobre $\mathbb{R}$). El "borde de ceros reales" es trivialmente verdadero por vacuidad, pero el flujo DBN no actúa naturalmente sobre un objeto sin representación $\int\Phi(u)\cos(zu)\,du$. **Defecto fatal 2:** la esquina se rompe: $\zeta_x(\tfrac12+is)$ **no converge** puntualmente cuando $x\to\infty$ (el producto de Euler no converge en la línea crítica, ni siquiera bajo RH) — GAP 6.5 de Doc 99. Con (a), (C) ni siquiera está definida como límite del campo. **Descartada.**

**Definición (b) — completación CF del aproximante (Doc 99) + flujo DBN sobre la clase de Paley–Wiener.** Es la elegida; se desarrolla en §2.

**Definición (c) — versión discreta vía el libro mayor de Weil (Doc 72).** $x=$ cota de primos, $\Delta_x=$ incremento al agregar el primo siguiente, leído sobre la descomposición $T_\lambda = A_\lambda^{off}-\sum_p(\log p/\sqrt p)B_\lambda(\log p)$ (Doc 72, Thm. 4.1). **Defecto (que probamos exactamente en §5.4):** esa descomposición es *estrictamente formal* — la suma sobre primos diverge (marginalmente, tipo Mertens), porque la función de prueba $W_\lambda w$ está en la **frontera** de la clase admisible de Weil (los polos de $w(s)=(2\pi)^{-2}|\Gamma(\tfrac14+\tfrac{is}2)|^2$ en $s=\pm i/2$ dan decaimiento de Fourier exactamente $e^{-|r|/2}$, sin margen $\varepsilon$). Por tanto los incrementos $\Delta_x$ de (c) **no son los incrementos de ninguna cantidad convergente**: el "borde aritmético" de (c) no es un teorema sino una serie divergente reordenable. (c) sirve como *libro mayor* para leer la dirección $x$ en la frontera (lo usamos en §5), pero no como definición del campo. **Descartada como definición; retenida como instrumento.**

### 1.3. Decisión declarada

Adoptamos la **Definición (b)**. Es la única bajo la cual (B1), (B2) y (C) son simultáneamente verdaderos por teoremas ya probados (con una hipótesis de no-degeneración finita, verificable, que declaramos). El precio de esa limpieza se revela en §3 y es el resultado central del documento.

---

## 2. La definición elegida y la verificación de los bordes

### 2.1. El aproximante CF-completado (Doc 99 / CCM-ZST)

Fijamos el parámetro multiplicativo $\mu>1$ del marco CCM-ZST (lo llamamos $\mu$ y no $\lambda$ para no colisionar con la escala de Abel $\lambda_0$ del kernel $W_{\lambda_0}$, que es un parámetro **distinto**; véase Doc 99 §6.2-bis sobre el riesgo de identificar los dos lados). El corte aritmético es $x=\mu^2$: por localidad automática de soporte (Doc 99 §2.1), la forma de Weil semilocal $QW_\mu$ sobre $L^2([\mu^{-1},\mu],d^*u)$ solo involucra las potencias de primos $p^m\leq\mu^2$.

**Realización exacta de $S=\{2,3\}$.** Tomamos $\mu^2=x\in[3,4)$ (p.ej. $\mu=\sqrt3$). Entonces $\{p^m\leq x\}=\{2,3\}$: entran exactamente los primos $2$ y $3$, ambos con $m=1$ únicamente ($2^2=4>x$). El aproximante de dos primos del título es esta ventana.

Para cada truncación $N$, sea $\xi=\xi^{(\mu,N)}$ el autovector mínimo de la matriz $QW_\mu^N$ (estructura Loewner, Doc 99 §2.3), bajo la hipótesis:

> **(ES$_x$) even-simplicity finita.** El autovalor mínimo de $QW_\mu^N$ es simple con autovector par. — *Verificable para cada $(\mu,N)$ finito por un cómputo de no-degeneración; no es una positividad; es el estatus exacto del Thm. 5.10 de CCM-ZST según Doc 99 §2.5. La asumimos declaradamente para los $(\mu,N)$ usados.*

Definimos la **función entera del aproximante**
$$F_x(z) := \widehat{\xi}(z) = \int_{-L/2}^{L/2}\xi(e^v)\,e^{izv}\,dv = 2\int_0^{L/2}\xi(e^v)\cos(zv)\,dv, \qquad L=2\log\mu,$$
(usamos la paridad $\gamma\xi=\xi$). Propiedades (todas de Doc 99 §2.4 y teoría elemental de Paley–Wiener):

- $F_x$ es entera, **par, real sobre $\mathbb{R}$**, de tipo exponencial $L/2$, con transformada de Fourier de **soporte compacto** $[-L/2,L/2]$;
- (rigidez CF, CvS + CCM-ZST Thm. 5.10(iii), incondicional dado (ES$_x$)): **todos los ceros de $F_x$ son reales**, y coinciden con $\operatorname{spec}(H_x)$ salvo el factor sin ceros $-i\mu^{-iz}$ del determinante regularizado.

### 2.2. El flujo DBN sobre el aproximante

Escribimos $\varphi_x(u):=2\,\xi(e^u)\,\mathbf{1}_{[0,L/2]}(u)$ (núcleo coseno de $F_x$) y definimos la **evolución DBN del aproximante**:
$$F_x^t(z) := \int_0^{L/2} e^{tu^2}\,\varphi_x(u)\cos(zu)\,du, \qquad t\in\mathbb{R}.$$
Como $\varphi_x$ tiene soporte compacto, $F_x^t$ está definida y es entera **para todo $t\in\mathbb{R}$** (a diferencia del caso $\zeta$, donde $t\leq 1/2$). Es la misma receta que define $H_t$ a partir de $\Phi$ (Doc 70 §2.1), aplicada al núcleo del aproximante. Nótese la EDP satisfecha:
$$\partial_t F_x^t(z) = \int u^2 e^{tu^2}\varphi_x\cos(zu)\,du = -\,\partial_{zz}F_x^t(z),$$
es decir, **calor hacia atrás** en la variable espectral $z$ (véase la Observación 4.1 sobre el signo en Doc 70).

### 2.3. El campo conjunto

Para $x$ finito y $t\geq 0$: sea $dm^{(t,x)}(s) := |F_x^t(s)|^2\,dm_\infty(s)\cdot C_{t,x}^{-1}$ (normalizada), y $dm_{on}^{(t,x)}$ su versión on-critical (reflejando a $\mathbb{R}$ los ceros no reales de $F_x^t$, como en Doc 70 §3.1). Para $x=\infty$: $F_\infty^t := H_t$ (el flujo DBN de $\Xi$), $dm^{(t,\infty)}=dm_{full}^t$ de Doc 70.

Fijamos de una vez la escala de Abel **mínima** $\lambda_0$ con $N(\lambda_0)=1$, de modo que (Doc 71 §2.3)
$$W_{\lambda_0}(s) = |P_1(s)|^2 + (a_1^\infty)^2|P_2(s)|^2,$$
con $a_k^\infty=\tfrac12\sqrt{(2k+1)(2k+2)}$, i.e. $(a_0^\infty)^2=\tfrac12$, $(a_1^\infty)^2=3$. Por Doc 103 (Teorema 3.1), **un solo $\lambda_0$ basta**: $T_{\lambda_0}(0)=0\iff$ RH; y $W_{\lambda_0}>0$ en todo punto de $\mathbb{R}$ (Doc 103). Definimos:

$$\boxed{\;\mathcal{T}(t,x) := \int W_{\lambda_0}(s)\,\bigl(dm^{(t,x)}-dm_{on}^{(t,x)}\bigr)(s)\;}$$

### 2.4. Verificación crítica: ¿son los bordes teoremas con esta definición?

**Proposición 2.1 (borde temporal).** $\mathcal{T}(t,\infty)=T_{\lambda_0}(t)=0$ para todo $t\geq\Lambda$.

*Demostración.* Es la Obs. 3.1 de Doc 70 con $\lambda=\lambda_0$: para $t>\Lambda$ todos los ceros de $H_t$ son reales, luego $H_t=H_t^{on}$ y la diferencia de medidas es nula; en $t=\Lambda$ por continuidad de los ceros (Rodgers–Tao garantizan $\Lambda\geq0$; la realidad en $t=\Lambda$ sigue del cierre de $\mathbb{R}$ y Hurwitz). $\square$

**Proposición 2.2 (borde aritmético, $t=0$).** Bajo (ES$_x$): $\mathcal{T}(0,x)=0$ para todo $x$ finito.

*Demostración.* Por la rigidez CF (Doc 99 §3, CCM-ZST Thm. 5.10(iii)), todos los ceros de $F_x=F_x^0$ son reales; luego $F_x^{on}=F_x$, las dos medidas coinciden y la integral es cero. $\square$

**Esquina.** $\mathcal{T}(0,\infty)=T_{\lambda_0}(0)$, y por Doc 64 (CTP) afilado por Doc 103 (Teorema 3.1, un solo $\lambda_0$): $\mathcal{T}(0,\infty)=0\iff$ RH. $\square$

Ambos bordes y la esquina son exactamente los requeridos por P41. La definición pasa el control crítico pedido en la tarea (i). Lo que sigue muestra que pasa *demasiado bien*.

---

## 3. El teorema de degeneración: el interior del cuadrante es idénticamente cero

### 3.1. La herencia de de Bruijn

**Lema 3.1 (preservación de la realidad de ceros bajo el flujo DBN hacia adelante).** Sea $\varphi\in L^1[0,a]$ real, $a<\infty$, y $F^t(z)=\int_0^a e^{tu^2}\varphi(u)\cos(zu)\,du$, no idénticamente nula. Si todos los ceros de $F^{t_1}$ son reales, entonces todos los ceros de $F^t$ son reales para todo $t\geq t_1$.

*Demostración.* Es el Teorema 13 de de Bruijn [de Bruijn 1950, *The roots of trigonometric integrals*, Duke Math. J. **17**, 197–226]: si los ceros de $\int e^{t_1u^2}\varphi(u)\cos(zu)\,du$ están en la franja $|\operatorname{Im}z|\leq\Delta$, los de la evolución a tiempo $t\geq t_1$ están en $|\operatorname{Im}z|\leq\sqrt{\max(\Delta^2-2(t-t_1),0)}$. Con $\Delta=0$ se obtiene realidad para todo $t\geq t_1$. Las hipótesis de regularidad/decaimiento de de Bruijn se satisfacen trivialmente para núcleos de soporte compacto en $[0,a]$ (toda integral converge absolutamente y $F^t$ es entera de orden $\leq1$ y tipo finito en $z$ para cada $t$; el enunciado de de Bruijn cubre esta clase — es la misma cita que usan Rodgers–Tao 2018, §1, para $\Lambda\leq 1/2$ con $\Delta=1/2$). $\square$

### 3.2. El teorema

**Teorema 3.2 (degeneración del interior).** Bajo (ES$_x$) para cada $x$ finito de la familia: 
$$\mathcal{T}(t,x) = 0 \qquad\text{para todo } x<\infty \text{ y todo } t\geq 0.$$
En particular, sobre el interior del cuadrante (y sobre los dos bordes):
$$\partial_t\mathcal{T} \equiv 0,\qquad \Delta_x\mathcal{T} := \mathcal{T}(t,S\cup\{p\})-\mathcal{T}(t,S) \equiv 0,\qquad \partial_t\Delta_x\mathcal{T} \equiv 0.$$

*Demostración.* Por la rigidez CF (Prop. 2.2), los ceros de $F_x^0$ son todos reales. Por el Lema 3.1 con $t_1=0$, los ceros de $F_x^t$ son todos reales para todo $t\geq 0$. Entonces $F_x^t=(F_x^t)^{on}$, $dm^{(t,x)}=dm_{on}^{(t,x)}$ y $\mathcal{T}(t,x)=0$. Las tres variaciones nulas son inmediatas (diferencias y derivadas de la función idénticamente nula; la derivada $\partial_t$ existe porque $t\mapsto F_x^t$ es real-analítica en $t$ con núcleo de soporte compacto). $\square$

### 3.3. Lectura estructural: por qué la Forma A se degeneró

El mecanismo es exacto y vale la pena aislarlo:

> **La propiedad que define el borde aritmético (realidad de los ceros del aproximante) es invariante bajo el flujo que define el borde temporal.** El flujo DBN hacia adelante no puede sacar ceros de la recta real (Lema 3.1). Por tanto, el borde $\{x\text{ finito}, t=0\}$ no es un borde: es una *fuente* cuya propiedad inunda todo el semiplano $t\geq0$ a $x$ fijo. El campo $\mathcal{T}$ resulta idénticamente nulo en $[0,\infty)\times\{x<\infty\}$, y todo el contenido de RH queda comprimido en el comportamiento del campo sobre la recta frontera $\{x=\infty\}$: allí $\mathcal{T}(t,\infty)=T_{\lambda_0}(t)$, que bajo $\neg$RH es $>0$ para $t\in[0,\Lambda)$ y $0$ para $t\geq\Lambda$.

Consecuencias inmediatas para el Problema 6.2 de P41:

1. **Toda desigualdad parabólica es vacuamente cierta en el interior.** $\partial_t\mathcal{T}\leq c\,\Delta_x\mathcal{T}$, log-convexidad en diagonales $t=\alpha/\log p_x$, monotonía de cualquier $M(t,x)$ construida con $\mathcal{T}$ y sus derivadas: todas se cumplen como $0\leq 0$ y **no transportan información alguna** hacia la esquina.

2. **La esquina es una discontinuidad pura.** Bajo $\neg$RH, $\mathcal{T}\equiv 0$ en el interior pero $\lim_{x\to\infty}\mathcal{T}(t,x)=0\neq T_{\lambda_0}(t)=\mathcal{T}(t,\infty)$ para cada $t<\Lambda$: el campo es discontinuo en **todo el segmento** $\{x=\infty,\,0\leq t<\Lambda\}$, no solo en la esquina. Ningún principio del máximo, fórmula de monotonía tipo Almgren ni log-convexidad ve una discontinuidad concentrada en la frontera del dominio: esos mecanismos propagan información de los bordes al interior **de funciones que satisfacen una EDP en el interior y son continuas hasta el borde**. Aquí la dirección necesaria es la opuesta (del interior trivial hacia el valor de borde no trivial), y eso es exactamente **continuidad del campo en la frontera aritmética**, es decir, el muro 1D de P41 §5.1 (continuidad $\equiv$ RH), del que la Forma A pretendía escapar.

3. **La degeneración no es un accidente de la definición (b): es una dicotomía.** Si se modifica la definición para que el interior no sea trivial, hay que romper una de las dos invarianzas: o el borde aritmético deja de ser el teorema CF (entonces (B2) deja de ser teorema — exactamente lo que pasa con las definiciones (a) y (c), §1.2), o el flujo temporal deja de ser el calor DBN hacia adelante (entonces (B1) deja de ser teorema, porque la extinción en $t\geq\Lambda$ es un hecho del calor). Formalmente:

**Proposición 3.3 (dicotomía de la Forma A para trazas de discrepancia).** Sea $\mathcal{T}(t,x)=\int W_{\lambda_0}\,(dm^{(t,x)}-dm^{(t,x)}_{on})$ cualquier campo cuyo aproximante a $x$ finito sea una función entera real par $G_x$ con todos sus ceros reales (condición (B2) tipo CF) y cuya evolución temporal sea $G_x^t=$ multiplicación del núcleo coseno por $e^{tu^2}$ (condición (B1) tipo DBN). Entonces $\mathcal{T}\equiv 0$ en $\{x<\infty,\,t\geq0\}$.

*Demostración.* Idéntica al Teorema 3.2: (B2) da realidad en $t=0$, (B1)+Lema 3.1 la propagan a todo $t\geq0$, y la realidad anula la discrepancia. $\square$

La dicotomía es: **(bordes teoremas) $\Rightarrow$ (interior trivial)**; contrapositivamente, (interior no trivial) $\Rightarrow$ (al menos un borde no es teorema). La Forma A pedía las dos cosas a la vez para la traza de discrepancia; son incompatibles.

---

## 4. (ii) La derivada temporal $\partial_t\mathcal{T}$ en $t=0$ para $S=\{2,3\}$

Aunque el Teorema 3.2 ya da la respuesta ($\partial_t\mathcal{T}(0,x_2)=0$ exactamente, con $x_2\in[3,4)$ el corte de dos primos), ejecutamos el cálculo por la maquinaria de Doc 71 como pide la tarea, porque el cálculo (i) revela **dos errores en Docs 70–71** que deben quedar corregidos en el corpus, y (ii) muestra con precisión *qué* se cancela y por qué la cancelación a $x$ finito no contiene aritmética.

### 4.1. Corrección de signo al flujo (Doc 70 §5.2)

**Observación 4.1 (signo de la ecuación del calor).** Con la definición estándar $H_t(z)=\int e^{tu^2}\Phi(u)\cos(zu)\,du$ (Doc 70 §2.1), se tiene
$$\partial_t H_t(z) = \int u^2 e^{tu^2}\Phi(u)\cos(zu)\,du = -\,\partial_{zz}H_t(z),$$
porque $\partial_{zz}\cos(zu)=-u^2\cos(zu)$. Doc 70 §5.2 escribe "$\partial_t H_t=\partial_{ss}H_t$ (ecuación del calor)": el signo es el **opuesto** (el flujo DBN es el calor hacia atrás en la variable espectral; por eso *afila* la función y empuja los ceros hacia $\mathbb{R}$, mientras que $e^{-tu^2}$ — calor hacia adelante — la suaviza). En consecuencia, la Prop. 8.2 de Doc 70 y la fórmula encajonada de Doc 71 §3.3 llevan el signo global opuesto. Las conclusiones *estructurales* de Doc 71 (forma cuadrática en $c_k$, cancelación bajo RH, limitación del §6) sobreviven porque son invariantes de signo; el análisis de signo de Doc 71 §4 **no** sobrevive (véase Obs. 4.3).

### 4.2. La derivada limpia

Sea $G$ entera, real sobre $\mathbb{R}$, par, con $G^t$ su evolución DBN, y sea $T(t)=\int W_{\lambda_0}(s)(|G^t|^2-|G^{t,on}|^2)\,dm_\infty\cdot C_t^{-1}$ la traza de discrepancia normalizada. Sobre $\mathbb{R}$, $\partial_t|G^t|^2 = 2G^t\,\partial_tG^t = -2\,G^t (G^t)''$, y con la identidad puntual $GG''=\tfrac12(G^2)''-(G')^2$ e integración por partes dos veces (los términos de frontera se anulan por el decaimiento $e^{-\pi|s|/2}$ de $w$ contra crecimiento polinomial-exponencial tipo finito de $G^2$ cuando $G$ es de tipo $<\pi/2$; para $G=F_x$ el tipo es $L/2=\log\mu<\pi/2$ si $\mu<e^{\pi/2}\approx 4.81$, lo que cubre $\mu=\sqrt3$; para $\mu$ mayores la justificación exige tipo $<\pi/2$ o un mollifier — lo declaramos como condición de validez):
$$\int W GG''\,dm_\infty = \tfrac12\int (W w)''\,G^2\,ds - \int W (G')^2\,dm_\infty.$$
Por tanto:

**Proposición 4.2 (derivada temporal, forma corregida).**
$$\partial_t T\Big|_{t=0} = D(G) - D(G^{on}) - \frac{\dot C_0}{C_0}\,T(0), \qquad
D(G) := 2\int W_{\lambda_0}(G')^2\,dm_\infty - \int (W_{\lambda_0}\,w)''\,G^2\,ds.$$

Comparación con Doc 71 §3.3: (1) el signo global está corregido (Obs. 4.1); (2) los tres términos de Doc 71 se reagrupan en $(W w)''= W''w + 2W'w' + Ww''$, que coincide con los Términos II–III de Doc 71 **más** el término de curvatura $W\cdot((\log w)''+((\log w)')^2)w$ que Doc 71 §3.2 omitió; (3) Doc 71 omitió la resta del bloque on-critical $D(G^{on})$ y el término de normalización $-(\dot C_0/C_0)T(0)$. La forma cuadrática $Q^{(\lambda)}(c,c)$ de Doc 71 §5.1 debe leerse, en rigor, como $D(G)$ solo — no como $\partial_tT|_0$.

### 4.3. La derivada en el aproximante de dos primos

**Teorema 4.3.** Bajo (ES$_{x_2}$), para el aproximante $F_{x_2}$ de $S=\{2,3\}$:
$$\partial_t\mathcal{T}(t,x_2)\Big|_{t=0} = D(F_{x_2}) - D(F_{x_2}^{on}) - \frac{\dot C_0}{C_0}\,\mathcal{T}(0,x_2) = 0,$$
y la cancelación es **término a término**: $F_{x_2}^{on}=F_{x_2}$ (rigidez CF) y $\mathcal{T}(0,x_2)=0$, de modo que los tres sumandos se anulan *individualmente como diferencias*, no por compensación de tres integrales no nulas.

*Demostración.* Inmediata de la Prop. 4.2 con $G=F_{x_2}$, $G^{on}=G$ (Prop. 2.2) y $\mathcal{T}(0,x_2)=0$. $\square$

**Observación 4.4 (qué contiene y qué no contiene esta cancelación).** El presupuesto $D(F_{x_2})$ es una cantidad finita, computable y genuinamente no trivial: su primer término $2\int W_{\lambda_0}(F_{x_2}')^2dm_\infty>0$ estrictamente, porque $W_{\lambda_0}>0$ en todo punto (Doc 103) y $F_{x_2}'\not\equiv0$. Pero $\partial_t\mathcal{T}=D(F_{x_2})-D(F_{x_2})=0$ es la resta de la **misma** cantidad consigo misma: la anulación de la derivada a $x$ finito es un corolario directo de la realidad de los ceros, y **no codifica ninguna cancelación aritmética**. Esto corrige una lectura optimista posible de Doc 71 §5.2: la "cancelación exacta de los tres términos bajo RH" es, vista correctamente (con el bloque on-critical restaurado), la identidad trivial $D(\Xi)-D(\Xi)=0$, no una condición algebraica no trivial sobre los $c_k$. La condición no trivial es $T_{\lambda_0}(0)=0$ misma — como ya concluía, por otra vía, el §6 de Doc 71.

**Observación 4.5 (el signo de $\partial_tT_{\lambda}|_{t=0}$ en $x=\infty$ bajo $\neg$RH queda ABIERTO).** El análisis de Doc 71 §4 ("Término I dominante $\Rightarrow\dot T>0$") usaba solo el bloque $D(\Xi)$, con el signo de la EDP equivocado y sin el bloque $D(\Xi^{on})$. Con la fórmula corregida, el signo de $\partial_tT|_0=D(\Xi)-D(\Xi^{on})-(\dot C_0/C_0)T(0)$ bajo $\neg$RH depende de comparar la energía ponderada $2\int W(\Xi')^2dm_\infty$ con la de $\Xi^{on}$ (cuyo cero real adicional en $\gamma_0$ *aumenta* localmente $|(\Xi^{on})'|$ cerca de $\gamma_0$ a la vez que $|\Xi^{on}|\le|\Xi|$ puntualmente sobre $\mathbb{R}$): los dos bloques compiten y no hay desigualdad puntual entre los integrandos. Declaramos: **GAP ABIERTO** (signo de $\dot T(0)$ bajo $\neg$RH). La "aparente contradicción" de Doc 71 §4.3 se disuelve: no había evidencia del signo $+$.

---

## 5. (iii) El incremento discreto $\Delta_x\mathcal{T}$ y el libro mayor de Weil en forma cerrada

Por el Teorema 3.2, $\Delta_x\mathcal{T}(t=0)=\mathcal{T}(0,S\cup\{p\})-\mathcal{T}(0,S)=0-0=0$ exactamente. El contenido no trivial de la dirección $x$ vive, pues, únicamente en el **libro mayor de Weil** (Doc 72): la descomposición formal $T_\lambda=A_\lambda^{off}-\sum_p\sum_{m\ge1}(\log p/p^{m/2})B_\lambda(m\log p)+\text{arquim.}$, donde el término del primo $p$ es el "incremento $\partial_x$ discreto" declarado en P41. En esta sección calculamos ese libro mayor **en forma cerrada exacta** para la ventana $N(\lambda_0)=1$, y extraemos tres consecuencias (signos, cambio de signo en $p=11$, divergencia marginal).

### 5.1. La transformada de Fourier de $dm_\infty$ en forma cerrada

**Lema 5.1.** Para $a>0$ y $u\in\mathbb{R}$:
$$\int_{-\infty}^{\infty}|\Gamma(a+it)|^2 e^{iut}\,dt = \frac{2\pi\,\Gamma(2a)}{(2\cosh(u/2))^{2a}}.$$

*Demostración.* De la integral beta $B(p,q)=\int_0^\infty y^{p-1}(1+y)^{-p-q}dy$ con $p=a+it$, $q=a-it$ y el cambio $y=e^v$:
$$\Gamma(a+it)\Gamma(a-it) = \Gamma(2a)\,B(a+it,a-it) = \Gamma(2a)\int_{-\infty}^{\infty}\frac{e^{av}e^{itv}}{(1+e^v)^{2a}}\,dv = \Gamma(2a)\int_{-\infty}^{\infty}\frac{e^{itv}}{(2\cosh(v/2))^{2a}}\,dv,$$
usando $e^{av}(1+e^v)^{-2a}=(e^{-v/2}+e^{v/2})^{-2a}$. Es decir, $|\Gamma(a+it)|^2$ es la transformada de Fourier de $\Gamma(2a)(2\cosh(v/2))^{-2a}\in L^1$; la inversión de Fourier (ambos lados pares, reales, integrables) da el enunciado. $\square$

**Corolario 5.2.** Con $dm_\infty(s)=(2\pi)^{-2}|\Gamma(\tfrac14+\tfrac{is}2)|^2ds$ y $a=\tfrac14$, $s=2t$:
$$\widehat w(r):=\int e^{irs}\,dm_\infty(s) = \frac{1}{\sqrt{2\pi}}\,(\cosh r)^{-1/2} =: \frac{g(r)}{\sqrt{2\pi}},\qquad g(r)=(\cosh r)^{-1/2}.$$
En particular la masa total es $\int dm_\infty=(2\pi)^{-1/2}$ (la normalización del programa no es de probabilidad; el polinomio ortonormal de grado 0 es $P_0=(2\pi)^{1/4}$). El decaimiento $\widehat w(r)\sim \pi^{-1/2}e^{-|r|/2}$ refleja los polos de $w$ en $s=\pm i/2$ (polo de $\Gamma(\tfrac14+\tfrac{is}{2})$ en $s=i/2$): la anchura de analiticidad es **exactamente** $1/2$, sin margen.

**Verificación de consistencia (Apéndice A.1):** los momentos $\int s^2\,d\widetilde m=-g''(0)/g(0)=\tfrac12=(a_0^\infty)^2$ y $\int s^4\,d\widetilde m=g''''(0)/g(0)=\tfrac74=(a_0^\infty)^4+(a_0^\infty)^2(a_1^\infty)^2$ reproducen exactamente los coeficientes de Jacobi $a_k^\infty=\tfrac12\sqrt{(2k+1)(2k+2)}$ del programa: la medida y la recurrencia son consistentes. Esto valida el Lema 5.1 contra los datos CCM de forma independiente.

### 5.2. $B_{\lambda_0}(r)$ en forma cerrada

Con $N(\lambda_0)=1$: $W_{\lambda_0}=|P_1|^2+3|P_2|^2$, y de la recurrencia ($b_k=0$): $P_1=sP_0/a_0$, $P_2=(s^2-\tfrac12)P_0/(a_0a_1)$, con $a_0^2=\tfrac12$, $a_1^2=3$, $P_0^2=\sqrt{2\pi}$. Los bloques $G_n(r):=\int|P_n(s)|^2\cos(rs)\,dm_\infty(s)$ se reducen a derivadas de $g$ (momentos pares contra coseno), y un cálculo directo (Apéndice A.2) da, con $c:=\cosh r$:
$$G_1(r) = -2g''(r) = -\tfrac12\,c^{-1/2}+\tfrac32\,c^{-5/2},\qquad
G_2(r) = \tfrac38\,c^{-1/2}-\tfrac{15}4\,c^{-5/2}+\tfrac{35}8\,c^{-9/2}.$$

**Teorema 5.3 (forma cerrada del coeficiente de Weil para la ventana mínima).**
$$B_{\lambda_0}(r) = G_1(r)+3G_2(r) = \frac{c^{-1/2}}{8}\,Q(\mathrm{sech}^2 r),\qquad Q(y) := 105\,y^2 - 78\,y + 5,\qquad c=\cosh r.$$
Verificaciones: $B_{\lambda_0}(0)=\tfrac{5-78+105}{8}=4=\int W_{\lambda_0}\,dm_\infty$ (= $1+(a_1^\infty)^2$, ortonormalidad) ✓; $G_1(0)=G_2(0)=1$ ✓.

Las raíces de $Q$ son $y_\pm=\dfrac{39\pm2\sqrt{249}}{105}$, con $y_-=0.0709\ldots$, $y_+=0.6724\ldots$ Por tanto:
$$B_{\lambda_0}(r) < 0 \iff y_-<\mathrm{sech}^2 r<y_+ \,;\qquad B_{\lambda_0}(r)>0 \text{ para } r \text{ grande } (\mathrm{sech}^2r<y_-).$$

### 5.3. Los incrementos por primo: signos exactos

Para el primo $p$ (término $m=1$), el incremento del libro mayor es $\delta_p := -\dfrac{\log p}{\sqrt p}\,B_{\lambda_0}(\log p)$. Como $\cosh(\log p)=\tfrac{p+p^{-1}}2$, se tiene $\mathrm{sech}^2(\log p)=\Bigl(\tfrac{2p}{p^2+1}\Bigr)^2$, racional. Evaluación exacta de $Q$:

| $p$ | $\mathrm{sech}^2(\log p)$ | $Q(\mathrm{sech}^2\log p)$ | signo de $B_{\lambda_0}(\log p)$ | signo de $\delta_p$ |
|---|---|---|---|---|
| $2$ | $16/25$ | $-239/125$ | $-$ | $+$ |
| $3$ | $9/25$ | $-1184/125$ | $-$ | $+$ |
| $5$ | $(5/13)^2=25/169$ | $-121120/28561$ | $-$ | $+$ |
| $7$ | $(7/25)^2=49/625$ | $-183520/390625$ | $-$ | $+$ |
| $11$ | $(11/61)^2=121/3721$ | $+35647712/13845841$ | $+$ | $-$ |
| $p\geq11$ | $<y_-$ | $>0$ | $+$ | $-$ |

(Para $p\geq11$: $\tfrac{2p}{p^2+1}\leq\tfrac{22}{122}=0.1803\ldots<\sqrt{y_-}=0.2663\ldots$, decreciente en $p$; para $p=7$: $\tfrac{14}{50}=0.28>\sqrt{y_-}$, de ahí el último signo $-$ de $Q$. Verificación racional completa en Apéndice A.3.) Los dos incrementos del aproximante de dos primos, en forma cerrada:
$$\delta_2 = \frac{\log 2}{\sqrt2}\cdot\frac{239}{500\sqrt5} \;(>0), \qquad
\delta_3 = \frac{\log 3}{\sqrt3}\cdot\frac{148}{125}\sqrt{\tfrac35} \;(>0).$$
Las potencias de primos siguen el mismo polinomio: $\mathrm{sech}^2(2\log2)=(8/17)^2$ da $Q<0$ ($\delta_{2^2}>0$), mientras $\mathrm{sech}^2(3\log2)=(16/65)^2<y_-$ y $\mathrm{sech}^2(2\log3)=(9/41)^2<y_-$ dan $Q>0$ ($\delta_{2^3}<0$, $\delta_{3^2}<0$): en la escala $p^m$, el cambio de signo ocurre en la única solución de $\mathrm{sech}^2(\log u)=y_-$, $u_*\in(7,8)$.

**Teorema 5.4 (oscilación del incremento discreto).** Para la ventana $N(\lambda_0)=1$, el incremento del libro mayor de Weil es estrictamente positivo para $p^m\in\{2,3,4,5,7\}$ y estrictamente negativo para todo $p^m\geq8$ (en particular para todo primo $p\geq11$): el cruce exacto está en $\mathrm{sech}^2(\log u_*)=y_-=\tfrac{39-2\sqrt{249}}{105}$, con $u_*\in(7,8)$. En particular, $\Delta_x$ (en su única lectura no trivial) **cambia de signo en la familia y no es monótona en $x$ a lo largo de ninguna diagonal**.

*Demostración.* Tabla anterior + monotonía de $\mathrm{sech}^2(\log\cdot)$ + signo de $Q$ fuera/dentro de $(y_-,y_+)$; todos los valores son racionales y el cálculo es aritmética exacta (Apéndice A.3). $\square$

### 5.4. La divergencia marginal: el Teorema 4.1 de Doc 72 es estrictamente formal

**Teorema 5.5 (divergencia de Mertens del libro mayor).** Para $r\to\infty$, $B_{\lambda_0}(r)=\tfrac{5\sqrt2}{8}\,e^{-r/2}\,(1+O(e^{-2r}))$. Por tanto el término del primo $p$ satisface
$$\frac{\log p}{\sqrt p}\,B_{\lambda_0}(\log p) = \frac{5\sqrt2}{8}\cdot\frac{\log p}{p}\,\bigl(1+O(p^{-2})\bigr),$$
y la suma $\sum_{p\leq X}\frac{\log p}{\sqrt p}B_{\lambda_0}(\log p)$ **diverge** como $\tfrac{5\sqrt2}{8}\log X$ (Mertens: $\sum_{p\le X}\log p/p=\log X+O(1)$). La serie de primos en el Thm. 4.1 de Doc 72 no converge absolutamente ni condicionalmente (términos de signo eventualmente constante): la descomposición $T_\lambda=A^{off}_\lambda-\sum_p(\log p/\sqrt p)B_\lambda(\log p)$ es **estrictamente formal** y requiere regularización (apareamiento con el bloque arquimediano divergente antes de sumar).

*Demostración.* $c^{-1/2}=(\cosh r)^{-1/2}=\sqrt2\,e^{-r/2}(1+e^{-2r})^{-1/2}$ y $Q(\mathrm{sech}^2r)\to Q(0)=5$; Mertens es clásico. La no convergencia condicional: los términos tienen signo constante para $p\geq11$. $\square$

**Observación 5.6 (la raíz del fenómeno y su consistencia con Doc 99).** La función de prueba $h_{\lambda_0}=W_{\lambda_0}w$ es analítica exactamente en $|\operatorname{Im}s|<\tfrac12$ (polos de $w$ en $\pm i/2$): está en la **frontera** de la clase de Weil, que exige $|\operatorname{Im}s|<\tfrac12+\varepsilon$. El decaimiento $\widehat{h}(r)\asymp e^{-r/2}$ compensa exactamente el peso $p^{1/2}$ de los primos y deja la divergencia logarítmica desnuda. Esto es la versión en el marco Jacobi de la divergencia de la cola prima del Doc 99 (Lema 5.1: $\sum_{p\le\lambda}\log p/\sqrt p\gtrsim\sqrt\lambda$ para la función carpa): distinta tasa porque distinta función de prueba, **misma lección** — MW-2 reaparece cuantitativamente en la dirección $x$, y la dirección $x$ del cuadrante no es la suma de incrementos absolutamente convergentes de ninguna cantidad. Notamos también que esto refina el comentario "formalmente" de Doc 72 §4.1: ahora la obstrucción tiene constante exacta ($\tfrac{5\sqrt2}{8}$) y mecanismo identificado (frontera de la clase de Weil). Que la suma de Mertens del Doc 60/72 §7 aparezca aquí no es casual: es el mismo término.

### 5.5. Por qué la oscilación es genérica en $N$ (no un accidente de la ventana mínima)

**Proposición 5.7.** Para todo $\lambda_0$ con $N(\lambda_0)\geq1$, la función $r\mapsto B_{\lambda_0}(r)$ es definida positiva en el sentido de Bochner (es la transformada de Fourier de la medida finita no negativa $W_{\lambda_0}w\,ds\geq0$, estrictamente positiva en todo punto por Doc 103). En consecuencia $|B_{\lambda_0}(r)|\leq B_{\lambda_0}(0)$ y $B_{\lambda_0}(0)>0$; pero la positividad de Bochner **no** implica positividad puntual de $B_{\lambda_0}$, y de hecho falla: $\int_{\mathbb{R}} B_{\lambda_0}(r)\,dr = 2\pi\,W_{\lambda_0}(0)\,w(0)$ es finita mientras $B_{\lambda_0}(0)=\int W_{\lambda_0}dm_\infty$ crece como $\sim N^2$ (pesos de Abel), de modo que para $N$ grande la masa positiva en $r=0$ debe compensarse con oscilación: $B_{\lambda_0}$ tiene cambios de signo para todo $N$ suficientemente grande, con primer cruce $r_*(\lambda_0)$ que se mueve con la escala (heurísticamente $r_*\sim1/\lambda_0$ por el principio de incertidumbre; no lo necesitamos). Para $N=1$ el cruce está calculado exactamente (Teorema 5.3–5.4).

*Demostración (de lo afirmado, no de la heurística).* Bochner: estándar, $W_{\lambda_0}w\in L^1$, $\geq0$. La fórmula $\int B=2\pi W(0)w(0)$ es inversión de Fourier en $r=0$ (ambas funciones integrables: $B$ decae como $e^{-r/2}$ por el Cor. 5.2 término a término, $W_{\lambda_0}w$ es Schwartz-decreciente exponencial). El crecimiento $B_{\lambda_0}(0)=\sum_{n=1}^N n\|P_n\|^2+(a_N^\infty)^2=\tfrac{N(N+1)}2+(a_N^\infty)^2\sim N^2$: ortonormalidad y Doc 71 §2.3. La conclusión "cambios de signo para $N$ grande" sigue de: si $B\geq0$ en todo $\mathbb{R}$, entonces $\sup B=B(0)\leq\ldots$ no acota; el argumento correcto es: $B\geq0$ y $\int B<\infty$ fija, con $B(0)\to\infty$ y $B$ uniformemente Lipschitz en escalas $O(1/N)$... — esta línea exige cuantificar la concentración; la dejamos como **afirmación probada solo para $N=1$ (exacta) y plausible para $N$ general [argumento incompleto — GAP menor declarado]**. Lo que el §6 usa es únicamente el caso $N=1$, que es exacto. $\square$

La consecuencia para la Forma A no depende del GAP: ya con una sola ventana (la mínima, que por Doc 103 basta para la esquina) el incremento $\Delta_x$ oscila con cruce exacto.

---

## 6. (iv) El test de signo: respuesta a la pregunta central

La pregunta de P41 (Problema 6.2) era: ¿hay relación de signo fija entre $\partial_t\mathcal{T}$ y $\Delta_x\mathcal{T}$ que soporte (a) una desigualdad parabólica, (b) log-convexidad en diagonales, o (c) una cantidad monótona $M(t,x)$ controlable en ambos bordes? La respuesta tiene dos niveles, y en ambos la Forma A muere — pero por mecanismos distintos del previsto por el falsador, lo cual conviene registrar con precisión.

### 6.1. Nivel interior: degeneración total (no oscilación)

En el interior del cuadrante (todo $x$ finito, todo $t\geq0$):
$$\partial_t\mathcal{T}=0,\qquad \Delta_x\mathcal{T}=0,\qquad \partial_t\Delta_x\mathcal{T}=0 \qquad\text{(Teorema 3.2)}.$$
El falsador de P41 contemplaba la muerte por *oscilación* ("la variación mixta cambia de signo sin diagonal monótona"). Lo que ocurre es más fuerte y más definitivo: la variación mixta no cambia de signo — es idénticamente nula — y precisamente por eso **toda** desigualdad parabólica, toda log-convexidad y toda cantidad monótona construida de $\mathcal{T}$ se satisfacen vacuamente sin transportar nada. Un principio del máximo sin función no trivial a la que aplicarse no es un mecanismo de propagación; es un enunciado sobre el conjunto vacío. La Forma A no falla porque el acoplamiento sea caótico: falla porque **no hay nada que acoplar**.

### 6.2. Nivel frontera: oscilación exacta sin diagonal monótona

Las únicas variaciones no triviales viven sobre la recta $\{x=\infty\}$ (donde $\mathcal{T}(t,\infty)=T_{\lambda_0}(t)$) y en el libro mayor de Weil que lee la dirección $x$ en esa recta. Allí el test de signo da:

- **Dirección $x$ (Teorema 5.4):** los incrementos $\delta_p$ cambian de signo (positivos para $p^m\in\{2,3,4,5,7\}$; negativos para todo $p^m\geq8$, en particular todo primo $p\geq11$), con cruce exacto en $\mathrm{sech}^2(\log u_*)=y_-=(39-2\sqrt{249})/105$, $u_*\in(7,8)$. Además la serie diverge (Teorema 5.5): no hay cantidad acumulada cuyos incrementos sean los $\delta_p$. El punto de cruce **depende de la ventana $\lambda_0$** (los coeficientes $105,-78,5$ son los de $N=1$; para $N$ mayores el polinomio cambia y el cruce se mueve), de modo que ninguna diagonal $t=\alpha/\log p_x$ puede ser monótona uniformemente en la escala.
- **Dirección $t$ (Observación 4.5):** el signo de $\partial_tT_{\lambda_0}(0)$ bajo $\neg$RH es un GAP ABIERTO; la única evidencia previa (Doc 71 §4) queda invalidada por el signo de la EDP y el bloque on-critical omitido.

Conclusión del test: **no existe relación de signo fija** $\partial_t\mathcal{T}\lessgtr c\,\Delta_x\mathcal{T}$ ni en el interior (donde es $0=0$, vacua) ni en la frontera (donde un lado oscila con cruce dependiente de la escala y el otro tiene signo desconocido). El primer test finito y honesto declarado en P41 §Form A se ejecutó y **el falsador se activa**, en modo degenerado (interior) y en modo oscilatorio (frontera) simultáneamente.

### 6.3. ¿Puede salvarse con otra cantidad monótona $M(t,x)$?

Para la clase "trazas de discrepancia con bordes-teorema", no: la Proposición 3.3 muestra que cualquier $M$ funcional de $\mathcal{T}$ y sus derivadas es funcional de la función nula en el interior. Cualquier salvataje requiere cambiar de objeto (§8), y entonces deja de ser la Forma A de P41 con sus dos bordes ya probados.

---

## 7. (v) El riesgo de transmutación de circularidad, pasado por el patrón del Doc 99

El patrón del Doc 99 (§4.3): *la circularidad no se elimina; se transmuta en no-uniformidad del paso al límite, donde reaparece con su nombre de siempre (MW-1/MW-6)*. Verificamos que la Forma A lo instancia exactamente, en cada una de sus encarnaciones:

| Definición del campo | ¿Borde $x$ teorema? | ¿Borde $t$ teorema? | ¿Interior no trivial? | Dónde queda RH |
|---|---|---|---|---|
| (b) CF + DBN (este doc) | Sí (CF, mod. ES$_x$) | Sí (DBN) | **No** (Thm. 3.2: $\equiv0$) | Discontinuidad del campo en $\{x=\infty,\,t<\Lambda\}$: continuidad en la esquina $\equiv\lim_x\mathcal{T}(0,x)=T_{\lambda_0}(0)\equiv$ C2/MW-6/MW-1 (Doc 99 §5) |
| (a) Euler puntual + calor | Vacuo (sin ceros) | No definible | — | La esquina ni existe (GAP 6.5 Doc 99: $\zeta_x\not\to$ en la línea) = MW-2 |
| (c) libro mayor de Weil | **No** (serie divergente, Thm. 5.5) | Sí | Sí (los $\delta_p$) | En la regularización de la serie: la cancelación entre bloque primo divergente y bloque arquimediano divergente es la fórmula explícita con $W_\lambda w$, cuya positividad total es el criterio de Weil = MW-1 |
| híbrido con tasa (cualquier interior no trivial + borde $x$ cuantitativo) | tasa, no teorema | Sí | Sí | E4 del Doc 99: **toda tasa uniforme finito$\to$pleno es RH efectiva** — circular |

La fila clave es la última. Por la dicotomía (Prop. 3.3), un interior no trivial exige degradar el borde aritmético de "teorema = 0" a "control cuantitativo de tamaño"; pero el Doc 99 (E4) ya demostró que cualquier cota uniforme de la distancia espectral aproximante–pleno implica una versión efectiva de C2, luego RH efectiva. Es decir:

> **El acoplamiento $\partial_t$–$\partial_x$, en cualquier versión no vacua, requiere en el paso del borde aritmético una positividad/tasa RH-equivalente.** La Forma A no encuentra un mecanismo nuevo: re-presenta el muro MW-1/MW-6 (vía C2) o MW-2 (vía la divergencia de la cola prima, ahora con constante exacta $\tfrac{5\sqrt2}{8}$ en el marco Jacobi). La transmutación del Doc 99 se reproduce sin residuo.

Un punto fino de honestidad en la dirección opuesta: nada de lo anterior usa positividad RH-equivalente *en los pasos probados de este documento*. Los Teoremas 3.2, 4.3, 5.3, 5.4, 5.5 son incondicionales (módulo ES$_x$, que es no-degeneración finita verificable, no positividad). La circularidad no contamina los resultados; contamina —como siempre— el único paso que falta, y la contribución de este documento es demostrar que ese paso no puede ser un principio de propagación 2D sobre la traza de discrepancia.

---

## 8. Lo que sobrevive: el objeto de reemplazo (Forma A′), declarado como problema nuevo

La degeneración del Teorema 3.2 indica con precisión qué clase de objeto habría que usar para que un cuadrante $(t,x)$ tenga interior no trivial con algún control de borde:

**Candidato A′ (presupuesto de energía).** $M(t,x):=D(F_x^t)=2\int W_{\lambda_0}((F_x^t)')^2dm_\infty-\int(W_{\lambda_0}w)''(F_x^t)^2ds$ — el presupuesto cuya *diferencia* con su versión on-critical es $\partial_t\mathcal{T}$ (Prop. 4.2). Es estrictamente no trivial a $x$ finito ($D\neq0$ en general), computable, y su incremento $\Delta_xM$ se lee en la forma semilocal de Weil (agregar el primo $p$ agrega $-W_p$ a la forma, con entradas explícitas tipo Doc 99 Lema 5.1). Su evolución en $t$ es la de una energía de Dirichlet bajo calor hacia atrás, para la cual existen fórmulas de monotonía/log-convexidad clásicas (Agmon; frecuencia de Almgren). **Advertencias declaradas:** (i) $M$ no tiene signo ni anulación ligada a RH en los bordes — el vínculo con RH pasa por $D(F)-D(F^{on})$, que reintroduce los ceros; (ii) cualquier control de $|M(t,x)-M(t,\infty)|$ uniforme es una tasa finito$\to$pleno, bajo sospecha E4. No es la Forma A: es un problema nuevo, y su auditoría de circularidad está pendiente.

**Candidato A″ (paquete negativo).** $\kappa(t,x):=\#\{\text{autovalores negativos de }QW^N_{\mu(x)}\text{ deformada al tiempo }t\}$ — la versión $(t,x)$ del E5 de Doc 99 y del índice $\kappa=2m$ de P35/Doc 96. Es entero, lo que conecta con la Forma B (amplificación) más que con la A. Fuera del alcance de este documento.

**Próximo paso concreto si se insiste en esta dirección:** calcular $\Delta_2 M(0,\cdot)$ y $\partial_tM(0,x_2)$ para $S=\{2,3\}$ con la misma maquinaria cerrada del §5 (las entradas de $W_p$ contra la base de Fourier son explícitas; la evolución $e^{tu^2}$ sobre soporte compacto es exacta), y pasar el resultado por el filtro E4 **antes** de invertir más esfuerzo. Si $\Delta_xM$ y $\partial_tM$ tampoco exhiben relación de signo estable, la familia entera de Formas A sobre funcionales cuadráticos del aproximante queda cerrada.

---

## 9. VEREDICTO

### RUTA CERRADA

**(para la Forma A de P41, Problema 6.2, con $\mathcal{T}=$ traza de discrepancia CCM del aproximante evolucionado — la formulación literal del paper).**

**Razón precisa.** (1) La única definición de $\mathcal{T}(t,x)$ que hace de ambos bordes teoremas ya probados (completación CF de Doc 99 para el borde aritmético, flujo DBN para el temporal) anula el campo **idénticamente en todo el interior del cuadrante** (Teorema 3.2), porque el flujo de calor DBN hacia adelante preserva la realidad de los ceros (herencia de de Bruijn, Lema 3.1) y la realidad de los ceros es exactamente la propiedad que define el borde aritmético. Con interior idénticamente nulo, $\partial_t\mathcal{T}=\Delta_x\mathcal{T}=\partial_t\Delta_x\mathcal{T}=0$: toda desigualdad parabólica, log-convexidad diagonal o cantidad monótona es vacua, y la esquina $(0,\infty)$ queda como discontinuidad pura del campo sobre la frontera $\{x=\infty\}$, cuya remoción es el muro 1D de continuidad (P41 §5.1) que la Forma A debía evitar. (2) La dicotomía es estructural (Prop. 3.3): interior no trivial $\Rightarrow$ algún borde deja de ser teorema, y entonces el control de ese borde es una tasa finito$\to$pleno, que por E4 (Doc 99) es RH efectiva — la circularidad se transmuta al paso límite exactamente según el patrón del Doc 99, sin residuo. (3) En el único libro mayor no trivial (lado Weil, §5), el test de signo pedido por P41 se ejecutó en forma cerrada exacta: los incrementos por primo cambian de signo en $p=11$ para la ventana mínima (positivos en $2,3,5,7$; negativos en adelante), el punto de cruce depende de la escala $\lambda_0$, la serie diverge como $\tfrac{5\sqrt2}{8}\log X$ (la función de prueba CCM está en la frontera exacta de la clase de Weil), y el signo de $\partial_tT|_0$ bajo $\neg$RH es un GAP ABIERTO tras corregir Docs 70–71. **No hay relación de signo fija ni diagonal monótona: el falsador declarado en P41 se activa, simultáneamente en modo degenerado (interior) y oscilatorio (frontera).**

**Lo que queda en pie (y no es la Forma A):** los resultados incondicionales nuevos de este documento — Teorema 3.2 (degeneración), Teorema 5.3 (forma cerrada $B_{\lambda_0}(r)=\tfrac{c^{-1/2}}8(105\,\mathrm{sech}^4r-78\,\mathrm{sech}^2r+5)$), Teoremas 5.4–5.5 (signos exactos y divergencia de Mertens con constante $\tfrac{5\sqrt2}{8}$), las correcciones de signo y completitud a Docs 70–71 (Obs. 4.1, Prop. 4.2, Obs. 4.4–4.5) — y el problema nuevo A′ (§8), con su filtro E4 obligatorio antes de cualquier inversión. Para el mapa del programa: la Forma A se tacha; la presión se desplaza íntegramente a la Forma B (amplificación de índice, Doc 106) y a los enunciados E1/E2 del Doc 99.

---

## Apéndice A — Verificaciones algebraicas (forma cerrada, sin numéricos)

### A.1. Derivadas de $g(r)=(\cosh r)^{-1/2}$ y consistencia con los $a_k^\infty$

Con $c=\cosh r$, $\sigma=\sinh r$, $\sigma^2=c^2-1$:
$$g'=-\tfrac12c^{-3/2}\sigma;\qquad g''=\tfrac34c^{-5/2}\sigma^2-\tfrac12c^{-1/2}=\tfrac14c^{-1/2}-\tfrac34c^{-5/2};$$
$$g'''=\tfrac14g'+\tfrac{15}8c^{-7/2}\sigma;\qquad g''''=\tfrac14g''+\tfrac{15}8\bigl[c^{-5/2}-\tfrac72c^{-9/2}\sigma^2\bigr]=\tfrac1{16}g-\tfrac{78}{16}c^{-5/2}+\tfrac{105}{16}c^{-9/2}.$$
(Paso intermedio: con $\sigma^2=c^2-1$, $g''''=\tfrac14g''-\tfrac{75}{16}c^{-5/2}+\tfrac{105}{16}c^{-9/2}$ y $\tfrac14g''=\tfrac1{16}g-\tfrac3{16}c^{-5/2}$.) Valores en $r=0$ ($c=1$): $g(0)=1$, $g''(0)=\tfrac14-\tfrac34=-\tfrac12$, $g''''(0)=\tfrac{1-78+105}{16}=\tfrac{28}{16}=\tfrac74$. Momentos normalizados de $dm_\infty$: $\langle s^2\rangle=-g''(0)=\tfrac12$ y $\langle s^4\rangle=g''''(0)=\tfrac74$. Lado Jacobi ($b_k=0$): $(J^2)_{00}=(a_0^\infty)^2=\tfrac{1\cdot2}4=\tfrac12$ ✓; $(J^4)_{00}=(a_0^\infty)^4+(a_0^\infty)^2(a_1^\infty)^2=\tfrac14+\tfrac12\cdot3=\tfrac74$ ✓. Consistencia exacta medida–recurrencia.

### A.2. Los bloques $G_1, G_2$

$\int s^{2j}\cos(rs)\,dm_\infty=(-1)^j\widehat w^{(2j)}(r)$ con $\widehat w=(2\pi)^{-1/2}g$. Con $P_0^2=\sqrt{2\pi}$:
$$G_1=\frac{P_0^2}{a_0^2}\int s^2\cos(rs)\,dm_\infty=\sqrt{2\pi}\cdot 2\cdot\bigl(-(2\pi)^{-1/2}g''\bigr)=-2g''=-\tfrac12g+\tfrac32c^{-5/2};$$
$$G_2=\frac{P_0^2}{a_0^2a_1^2}\int(s^2-\tfrac12)^2\cos(rs)\,dm_\infty=\tfrac23\bigl[g''''+g''+\tfrac14g\bigr]=\tfrac1{24}\bigl[9g-90c^{-5/2}+105c^{-9/2}\bigr],$$
usando $(s^2-\tfrac12)^2=s^4-s^2+\tfrac14$, $\int s^4\cos\to+g''''$, $-\int s^2\cos\to+g''$. Chequeos: $G_1(0)=-\tfrac12+\tfrac32=1$ ✓, $G_2(0)=\tfrac{9-90+105}{24}=1$ ✓ (ortonormalidad). Suma:
$$B_{\lambda_0}=G_1+3G_2=\bigl(-\tfrac12+\tfrac98\bigr)g+\bigl(\tfrac32-\tfrac{45}4\bigr)c^{-5/2}+\tfrac{105}8c^{-9/2}=\tfrac58c^{-1/2}-\tfrac{39}4c^{-5/2}+\tfrac{105}8c^{-9/2},$$
que es $\tfrac{c^{-1/2}}8(5-78y+105y^2)$ con $y=c^{-2}=\mathrm{sech}^2r$. En $r=0$: $\tfrac{5-78+105}8=4=1+(a_1^\infty)^2=\int W_{\lambda_0}dm_\infty$ ✓.

### A.3. Evaluaciones racionales de $Q(y)=105y^2-78y+5$

- $p=2$: $c=\tfrac54$, $y=\tfrac{16}{25}$. $Q=\tfrac{105\cdot256-78\cdot16\cdot25+5\cdot625}{625}=\tfrac{26880-31200+3125}{625}=-\tfrac{1195}{625}=-\tfrac{239}{125}<0$.
- $p=3$: $c=\tfrac53$, $y=\tfrac9{25}$. $Q=\tfrac{8505-17550+3125}{625}=-\tfrac{5920}{625}=-\tfrac{1184}{125}<0$.
- $p=5$: $c=\tfrac{13}5$, $y=\tfrac{25}{169}$. $Q=\tfrac{105\cdot625-78\cdot25\cdot169+5\cdot169^2}{169^2}=\tfrac{65625-329550+142805}{28561}=-\tfrac{121120}{28561}<0$.
- $p=7$: $c=\tfrac{25}7$, $y=\tfrac{49}{625}$. $Q=\tfrac{105\cdot2401-78\cdot49\cdot625+5\cdot625^2}{625^2}=\tfrac{252105-2388750+1953125}{390625}=-\tfrac{183520}{390625}<0$.
- $p=11$: $c=\tfrac{61}{11}$, $y=\tfrac{121}{3721}$. $Q=\tfrac{105\cdot14641-78\cdot121\cdot3721+5\cdot3721^2}{3721^2}=\tfrac{1537305-35118798+69229205}{13845841}=+\tfrac{35647712}{13845841}>0$.
- Monotonía: $y_p=\bigl(\tfrac{2p}{p^2+1}\bigr)^2$ es estrictamente decreciente en $p\geq1$; $y_{11}<y_-<y_7$ porque $Q(y_{11})>0>Q(y_7)$ y $y_\pm$ son las únicas raíces. Para todo primo $p\geq11$, $y_p\leq y_{11}<y_-\Rightarrow Q(y_p)>0$.
- Potencias: $2^2$: $c=\tfrac{17}8$, $y=\tfrac{64}{289}\in(y_-,y_+)\Rightarrow Q<0$. $2^3$: $c=\tfrac{65}{16}$, $y=\tfrac{256}{4225}=0.0606<y_-\Rightarrow Q>0$. $3^2$: $c=\tfrac{41}9$, $y=\tfrac{81}{1681}=0.0482<y_-\Rightarrow Q>0$.
- $B_{\lambda_0}(\log2)=\tfrac18\cdot\tfrac2{\sqrt5}\cdot\bigl(-\tfrac{239}{125}\bigr)=-\tfrac{239}{500\sqrt5}$; $B_{\lambda_0}(\log3)=\tfrac18\sqrt{\tfrac35}\cdot\bigl(-\tfrac{1184}{125}\bigr)=-\tfrac{148}{125}\sqrt{\tfrac35}$.

### A.4. Nota sobre el dominio de validez de la integración por partes (Prop. 4.2)

Los términos de frontera $[W w\,GG']_{\pm\infty}$ y $[(Ww)'G^2]_{\pm\infty}$ se anulan si $G^2(s)e^{-\pi|s|/2}\to0$, lo que vale para $G$ de tipo exponencial $<\pi/2$ con crecimiento polinomial sobre $\mathbb{R}$ (Paley–Wiener: $|G(s)|$ acotada sobre $\mathbb{R}$ para núcleo $L^1$). Para $F_{x_2}$ (tipo $\log\sqrt3<\pi/2$) y su evolución (mismo tipo) la condición se cumple. Para $G=\Xi$ (orden 1, tipo infinito en la dirección real... el decaimiento real de $\Xi$ es más rápido que cualquier exponencial) la integral converge por el decaimiento de $\Xi$ misma; lo señalamos porque Doc 71 no verificó la frontera. GAP menor declarado: la verificación uniforme en $t$ de los términos de frontera para $H_t$, $t>0$, no está escrita (decaimiento de $H_t$ sobre $\mathbb{R}$: estándar por la representación integral, no incluido aquí).

---

## Apéndice B — Fuentes y citas (backward-only)

| Fuente | Uso | Estatus |
|---|---|---|
| Doc 64 (CTP), Doc 103 (Thm. 3.1, $W_\lambda>0$ estricto y un solo $\lambda_0$) | Definición de $\mathcal{T}$, esquina = RH | Programa, probado |
| Doc 70 (flujo DBN sobre la traza; Obs. 3.1) | Borde temporal; convención $H_t$ | Programa; **corregido aquí** el signo de §5.2 (Obs. 4.1) |
| Doc 71 (derivada temporal, forma cuadrática) | §4; **corregida** (bloque on-critical, normalización, término de curvatura, signo) | Programa |
| Doc 72 (traza vía fórmula de Weil, $B_\lambda$) | Libro mayor §5; su Thm. 4.1 se demuestra aquí **estrictamente formal** (Thm. 5.5) | Programa |
| Doc 99 (rigidez CF, $H_x$, GAPs 6.2/6.5, E1–E6, transmutación §4.3) | Definición (b); dicotomía §7; filtro E4 | Programa |
| P41 §Form A (Problema 6.2, falsador) | Enunciado del problema y del test | Programa |
| N. G. de Bruijn, *The roots of trigonometric integrals*, Duke Math. J. **17** (1950), 197–226, Thm. 13 | Lema 3.1 (herencia de realidad bajo $e^{tu^2}$, franja $\sqrt{\Delta^2-2t}$) | Literatura clásica, verificada por uso reiterado en la literatura DBN (es la cita estándar de Rodgers–Tao) |
| B. Rodgers, T. Tao, *The De Bruijn–Newman constant is non-negative*, arXiv:1801.05914 (Forum Math. Pi 8 (2020)) | $\Lambda\geq0$; contexto del Lema 3.1 | Literatura, verificada en Doc 70 |
| Integral beta / $\int|\Gamma(a+it)|^2e^{iut}dt=2\pi\Gamma(2a)(2\cosh\tfrac u2)^{-2a}$ | Lema 5.1 | **Probado aquí** desde la integral beta (autocontenido; no requiere tabla) |
| CCM-ZST arXiv:2511.22755; CvS CMP 406:312 (2025) | Rigidez CF, $H_x$, even-simplicity | Verificadas en Doc 99 (Apéndice A de Doc 99); usadas solo a través de los enunciados allí cotejados |

Resultados nuevos de este documento: Lema 3.1 (aplicación), Teorema 3.2, Proposición 3.3 (dicotomía), Observación 4.1 (corrección de signo a Doc 70), Proposición 4.2 (derivada corregida con bloque on-critical y normalización), Teorema 4.3, Observaciones 4.4–4.5, Lema 5.1 (prueba autocontenida), Corolario 5.2, Teorema 5.3 (forma cerrada de $B_{\lambda_0}$), Teorema 5.4 (cambio de signo en $p=11$), Teorema 5.5 (divergencia de Mertens con constante $\tfrac{5\sqrt2}8$), Observación 5.6, la tabla de transmutación §7 y la clasificación A′/A″ del §8.

---

## Apéndice C — Posición del Doc 105 en el mapa del programa

```
P41 — formas lógicas restantes tras el no-go 1D
  │
  ├─ Forma A (propagación 2D, Problema 6.2)  ──►  Doc 105: RUTA CERRADA
  │     │
  │     ├─ mecanismo de muerte 1 (interior): herencia de de Bruijn
  │     │     (B2: ceros reales CF) es invariante bajo (B1: flujo DBN)
  │     │     ⟹ 𝒯 ≡ 0 en {x<∞, t≥0}  [Thm 3.2; dicotomía Prop 3.3]
  │     │     ⟹ la esquina es el muro 1D de continuidad (P41 §5.1)
  │     │
  │     ├─ mecanismo de muerte 2 (frontera): libro mayor de Weil
  │     │     B_{λ0}(r) = (c^{-1/2}/8)(105 sech⁴r − 78 sech²r + 5)  [Thm 5.3]
  │     │     δ_p > 0 para p^m ∈ {2,3,4,5,7};  δ_p < 0 para p^m ≥ 8  [Thm 5.4]
  │     │     Σ_p diverge ~ (5√2/8) log X  (frontera de la clase de Weil) [Thm 5.5]
  │     │     signo de ∂_t T|₀ bajo ¬RH: GAP ABIERTO  [Obs 4.5]
  │     │
  │     └─ transmutación de circularidad (patrón Doc 99 §4.3): verificada
  │           sin residuo — toda versión no vacua cae en C2/MW-1/MW-6,
  │           MW-2 (constante exacta 5√2/8) o E4 (tasa = RH efectiva)  [§7]
  │
  ├─ Forma A′ (presupuesto positivo M(t,x) = D(F_x^t)): problema NUEVO,
  │     no auditado; filtro E4 obligatorio antes de invertir  [§8]
  │
  └─ Forma B (amplificación de índice): no afectada por este doc → Doc 106

Correcciones al corpus: Doc 70 §5.2 (signo de la EDP del flujo DBN),
Doc 71 §§3–5 (bloque on-critical, normalización, término de curvatura;
el análisis de signo §4 queda invalidado; la "condición algebraica sobre
los c_k" de §5.2 es la identidad trivial D(Ξ)−D(Ξ)=0)  [Obs 4.1, Prop 4.2, Obs 4.4]
```

---

*Fin del Documento 105.*
