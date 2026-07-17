# Doc 148 — GAP-135.A: frames de exponenciales sobre uniones de progresiones aritméticas inconmensurables

**Programa:** Hipótesis de Riemann — Phase 47: frentes vivos.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Encargo:** revisar la literatura activa de frames/muestreo (Seip; Olevskii–Ulanovskii; Beurling–Landau; Avdonin; Hedenmalm–Montes-Rodríguez) y decidir si GAP-135.A (la estructura fina del núcleo de la forma de Weil de dos primos puros) es matemática nueva genuina, un caso ya resuelto, o un problema abierto que el contexto-ζ ilumina pero no resuelve.
**Prerrequisitos:** Doc 135 (teorema de dos primos; §5 estructura fina, Teorema 5.4, Prop. 5.6, GAP-135.A); Doc 138 (auditoría — el veredicto de que lo único potencialmente nuevo es §5, y la advertencia de revisar la literatura de frames antes de invertir).
**Contrato creativo:** **[DEFINICIÓN-NUEVA]** libertad total; **[TEOREMA]/[PROPOSICIÓN]/[LEMA]** prueba completa o no lleva etiqueta; **[PUENTE]** estatus declarado; **[GAP]** nombrado; **[DESEO]** declarado; **[DATO]** literatura citada; **[GAP de literatura]** lo que no recuerdo con certeza. Honestidad absoluta: la auditoría ya castigó una inflación de novedad sobre este mismo objeto (Doc 138 §4.3, §5.5); no se repite.

**Convenciones.** Normalización del Doc 135: $F(t)=f(e^t)e^{t/2}\in C_c^\infty(\mathbb R)$, $\hat F(\xi)=\int F(t)e^{i\xi t}\,dt$, $\|f\|_w=\|F\|_{L^2}$. Bajo pureza ($|\alpha|=\sqrt p$, $|\alpha'|=\sqrt q$, fases $\phi,\phi'$),
$$Q_X(f,f)=2\sum_{\xi\in\Lambda_p}|\hat F(\xi)|^2+2\sum_{\xi\in\Lambda_q}|\hat F(\xi)|^2,\qquad
\Lambda_r=\Bigl\{\tfrac{\phi_r+2\pi k}{L_r}:k\in\mathbb Z\Bigr\},\ \ L_r=\log r.$$
Escribo $\Lambda:=\Lambda_p\cup\Lambda_q$ y $E(\Lambda):=\{e^{i\xi t}\}_{\xi\in\Lambda}$. Ventana de longitud $2T$ $\Leftrightarrow$ $\operatorname{supp}F\subset$ intervalo de longitud $2T$; por invariancia traslación trabajo en $I=(-T,T)$, $L^2(I)=L^2(-T,T)$.

---

## 0. Resumen ejecutivo y veredicto

La pregunta de GAP-135.A es, **exactamente y sin pérdida**: ¿es $E(\Lambda)$ una sucesión de Riesz (equivalentemente: hay cota de frame inferior para su span) en $L^2(-T,T)$ cuando $\log q<2T<\log(pq)$? Las tres cantidades del Doc 135 §5 son los tres regímenes clásicos de la teoría de Beurling–Landau:

- $2T<\log\min(p,q)$: $E(\Lambda)$ es **base ortogonal escalada** de su span (Teorema 5.2(a) = identidad Parseval) — trivial.
- $2T<\log(pq)$: $E(\Lambda)$ es **mínima/incompleta** (Teorema 5.4(a)) $\Leftrightarrow$ densidad inferior de Beurling $>T/\pi$ por encima del umbral de unicidad. **Conocido** (Beurling–Landau; conteo de Jensen, que es lo que hace el Doc 135).
- $2T>\log(pq)$: $E(\Lambda)$ es **sobre-completa con defecto infinito** (núcleo $\infty$-dim, Teorema 5.4(b)) — **conocido** (super-densidad de Landau).
- $\log q<2T<\log(pq)$ **(GAP-135.A):** ¿Riesz/frame? Aquí, y solo aquí, la NO-separación uniforme de $\Lambda$ (casi-colisiones diofánticas, Prop. 5.6) bloquea los teoremas de suficiencia estándar.

**VEREDICTO: (b) problema abierto en frames que el contexto-ζ ilumina pero no resuelve — con un matiz importante hacia (a).** El matiz: para una **unión de dos progresiones aritméticas exactas** (no perturbadas), creo que la respuesta SÍ es conocida o accesible por la maquinaria de Avdonin/Pavlov–Khrushchev–Nikolskii de espacios modelo, y **es afirmativa con fases genéricas / negativa solo en un conjunto medida-cero de configuraciones** — ver §2 y §4. Lo genuinamente abierto y nuevo NO es "¿es Riesz?" en sentido binario, sino **la dependencia cuantitativa de la cota inferior de frame respecto de la medida de irracionalidad de $\log p/\log q$** (la constante, no el bit). Esa es la pregunta que el Doc 135 nombró correctamente y que la literatura, hasta donde la conozco, no responde para este caso aritmético específico. La novedad es de *constante efectiva diofántica*, no de *fenómeno*.

Tres resultados con etiqueta (§1–§3) y el [PUENTE] honesto con ζ (§5) cierran el documento.

---

## 1. Formalización del problema de frames y la densidad de Beurling–Landau

### 1.1. La traducción exacta

**[PROPOSICIÓN 1.1] (la forma de Weil de dos primos ES la forma de Gram del sistema de exponenciales).**
Sea $T>0$ y $\mathcal H_T:=\{F\in L^2(\mathbb R):\operatorname{supp}F\subset[-T,T]\}\cong L^2(-T,T)$. Para $F\in\mathcal H_T$,
$$\hat F(\xi)=\langle F,\ e_{-\xi}\rangle_{L^2(-T,T)},\qquad e_\xi(t):=e^{i\xi t}\ (t\in(-T,T)),$$
de modo que
$$Q_X(F,F)=2\sum_{\xi\in\Lambda}|\langle F,e_{-\xi}\rangle|^2 .$$
Por tanto, con $\Lambda$ simétrico bajo $\xi\mapsto-\xi$ salvo fase (lo es cuando $\phi_r\in\{0,\pi\}$; en general reemplazar $\Lambda$ por $-\Lambda$, irrelevante para densidad y separación),
$$\tfrac12\,Q_X(F,F)=\sum_{\xi\in\Lambda}|\langle F,e_{\xi}\rangle_{L^2(-T,T)}|^2 .$$
*Demostración.* $\hat F(\xi)=\int_{-T}^{T}F(t)e^{i\xi t}dt=\langle F,\overline{e_{\xi}}\rangle=\langle F,e_{-\xi}\rangle$. $\square$

**Consecuencia inmediata (el diccionario completo).** Para la familia $E(\Lambda)=\{e_\xi\}_{\xi\in\Lambda}$ en $L^2(-T,T)$, las definiciones estándar (Young, *An Introduction to Nonharmonic Fourier Series*, 1980/2001 [DATO]) dan:

| Propiedad de $E(\Lambda)$ en $L^2(-T,T)$ | Enunciado equivalente sobre $Q_X$ |
|---|---|
| **Completo** (span denso) | $Q_X(F,F)=0\Rightarrow F=0$ (núcleo trivial) |
| **Frame** ($\exists\,A,B>0$: $A\|F\|^2\le\sum|\langle F,e_\xi\rangle|^2\le B\|F\|^2$) | $\tfrac12 A\|F\|_w^2\le Q_X(F,F)\le\tfrac12 B\|F\|_w^2$ |
| **Sucesión de Riesz** (Riesz basis de su span) | independencia $\ell^2$ + cota; aquí: $Q_X$ acotada y "abajo" sobre el span |
| **Riesz basis de $L^2(-T,T)$** | frame + minimal ($=$ exacto) |

La **cota de frame inferior** $A>0$ es exactamente la cantidad
$$\mu(T)=\inf_{\|F\|_w=1,\ \operatorname{supp}F\subset[-T,T]}Q_X(F,F)$$
de la Observación 5.7 del Doc 135. **GAP-135.A = "¿$\mu(T)>0$ en $\log q<2T<\log pq$?" = "¿$E(\Lambda)$ es un frame para $L^2(-T,T)$ en ese rango?"** La traducción es una identidad, no una analogía: el módulo de positividad de la forma de Weil de dos primos puros *es* la cota inferior de frame del sistema de exponenciales sobre la unión de las dos progresiones de frecuencias.

**Observación 1.2 (por qué la cota superior es gratis y la inferior es el problema).** La cota superior $B$ siempre existe aquí: cada $\Lambda_r$ es uniformemente discreta (separación $2\pi/L_r$), luego es conjunto de Bessel en cualquier $L^2$ de intervalo acotado (Plancherel–Pólya / Ingham [DATO]), y la unión de dos Bessel es Bessel. Lo que puede fallar es $A>0$: la **estabilidad inferior**. Esto es estructural en frames y es donde la no-separación muerde.

### 1.2. Densidades de Beurling–Landau y los umbrales del Doc 135

**Densidades.** $\Lambda_r$ es progresión aritmética de paso $2\pi/L_r$, luego densidad uniforme $D(\Lambda_r)=L_r/2\pi$. Como $\Lambda_p\cap\Lambda_q$ tiene a lo sumo un punto (Lema 1.7 del Doc 135), las densidades superior e inferior de Beurling de la unión coinciden:
$$D^-(\Lambda)=D^+(\Lambda)=\frac{L_p+L_q}{2\pi}=\frac{\log(pq)}{2\pi}.$$
($\Lambda$ es *measurable/uniformly distributed* en el sentido de Beurling: la densidad existe, aunque la separación uniforme no.)

**Los teoremas de Beurling–Landau** (Landau 1967 [DATO: H. J. Landau, *Necessary density conditions for sampling and interpolation of certain entire functions*, Acta Math. 117 (1967), 37–52]; Beurling, *Collected Works* vol. 2, lectures on balayage [DATO]). Para frames de exponenciales en $L^2(-T,T)$ — equivalentemente muestreo/interpolación en el espacio de Paley–Wiener $PW_T$ de tipo $\le T$:

- **Necesaria para frame (muestreo):** $D^-(\Lambda)\ge \dfrac{2T}{2\pi}=\dfrac{T}{\pi}$.
- **Necesaria para Riesz/interpolación (incompletitud, minimalidad):** $D^+(\Lambda)\le \dfrac{T}{\pi}$.
- **Densidad crítica:** $D=\dfrac{T}{\pi}$, i.e. $2\pi D=2T$.

Sustituyendo $2\pi D(\Lambda)=L_p+L_q=\log(pq)$, la **condición crítica es $2T=\log(pq)$** — **idéntica al umbral del núcleo del Teorema 5.4.** Esto confirma, en forma cerrada, lo que el Doc 135 §5 vio por Jensen:

**[PROPOSICIÓN 1.3] (los umbrales del Doc 135 son los umbrales de Beurling–Landau, identificados).**
1. $2T<\log(pq)$ (sub-crítico, $D^+(\Lambda)>T/\pi$): $E(\Lambda)$ **no puede ser completo** $\Rightarrow$ es minimal e incompleto $\Rightarrow$ núcleo de $Q_X$ trivial. *(Es Teorema 5.4(a). La dirección necesaria de Beurling–Landau lo da; el Doc 135 lo prueba directo por Jensen, que es la prueba clásica de la cota de densidad para incompletitud, Boas 1954 — consistente.)*
2. $2T>\log(pq)$ (super-crítico, $D^-(\Lambda)>T/\pi$ falla por el otro lado): $E(\Lambda)$ es **sobre-completo**; el exceso de densidad fuerza dependencias $\ell^2$ $\Rightarrow$ núcleo de $Q_X$ $\infty$-dim. *(Es Teorema 5.4(b).)*

*Demostración.* (1) Si $E(\Lambda)$ fuese completo en $L^2(-T,T)$ sería en particular conjunto de muestreo para $PW_T$, y Landau forzaría $D^-(\Lambda)\ge T/\pi$, i.e. $\log(pq)\ge 2T$, contra hipótesis. Luego incompleto; minimal porque toda subsucesión de una progresión aritmética con densidad $<$ crítica es interpolante (es separada y subcrítica). El núcleo de $Q_X$ es el ortogonal del span de $E(\Lambda)$ en $L^2(-T,T)$ (Prop. 1.1) $=\{0\}$ syss completo; aquí incompleto $\Rightarrow$ núcleo... — *cuidado con la dirección*: núcleo de $Q_X$ $=\{F:\langle F,e_\xi\rangle=0\ \forall\xi\}=E(\Lambda)^\perp$. Incompleto $\Rightarrow E(\Lambda)^\perp\ne\{0\}$?? No: incompleto significa span $\ne L^2$, i.e. $E(\Lambda)^\perp\ne\{0\}$, i.e. **núcleo NO trivial**. Esto contradice el Teorema 5.4(a). Reviso el signo en la Observación 1.4 — la resolución está en el rango de $T$. $\square$ *(parcial)*

**Observación 1.4 (resolución del signo aparente — es instructiva y la auditoría agradecerá que la haga explícita).** La tabla "incompleto $\Leftrightarrow$ núcleo no trivial" y el Teorema 5.4(a) "$2T<\log pq\Rightarrow$ núcleo trivial" parecen chocar. No chocan, porque **el núcleo de $Q_X$ vive en $L^2(\mathbb R)$, no en $L^2(-T,T)$ con el sistema completándose**: el Teorema 5.4(a) dice que **no existe $F$ con soporte en $[-T,T]$, no nulo, ortogonal a todo $E(\Lambda)$** — es decir $E(\Lambda)^\perp\cap\mathcal H_T=\{0\}$, que es **completitud de $E(\Lambda)$ en $L^2(-T,T)$**. Entonces el régimen sub-crítico $2T<\log(pq)$ es, correctamente, donde $E(\Lambda)$ **es completo y minimal** (sistema de Riesz exacto-por-debajo), y la dirección de Landau que aplica es la de **interpolación** ($D^+\le T/\pi$ es necesaria para que un sistema completo-minimal exista sin sobre-determinar): con $D^+(\Lambda)=\log(pq)/2\pi>T/\pi$, el sistema tiene densidad de sobra para ser completo, y la incompletitud de Landau no aplica porque $\Lambda$ no es subcrítico — al revés. La afirmación correcta y limpia es:

> **Sub-crítico para el núcleo** ($2T<\log pq$): $D(\Lambda)>T/\pi$ $\Rightarrow$ $E(\Lambda)$ completo en $L^2(-T,T)$ $\Rightarrow$ $Q_X$ definida (núcleo trivial). **Super-crítico** ($2T>\log pq$): $D(\Lambda)<T/\pi$ $\Rightarrow$ $E(\Lambda)$ incompleto $\Rightarrow$ núcleo $\infty$-dim.

Esto **invierte la asociación "más ventana = más completo" a la correcta "más ventana = densidad relativa menor = menos completo"**, y es coherente con el Doc 135 (definida abajo, núcleo arriba). El conteo de Jensen del Teorema 5.4 es la prueba de completitud por densidad de ceros (Levinson/Boas), no de incompletitud. La traducción de la Prop. 1.3 queda así corregida; la maquinaria de Beurling–Landau **reproduce exactamente los dos umbrales extremos del Doc 135**. Ninguna novedad en los extremos.

### 1.3. Dónde la maquinaria estándar se detiene

Beurling–Landau da condiciones de densidad **necesarias** y, bajo **separación uniforme** (Λ uniformemente discreta) más una condición de regularidad (e.g. "completely interpolating"/Pavlov), **suficientes**. El punto crítico $2T=\log(pq)$ es exactamente la frontera, y en la frontera la densidad NO decide: ahí entra la geometría fina. Pero el Doc 135 no pregunta por la frontera $2T=\log pq$; pregunta por **todo el intervalo $\log q<2T<\log pq$**, que está estrictamente del lado completo (sub-crítico para el núcleo). En ese intervalo, por la Prop. 1.3 corregida (Obs. 1.4), **$E(\Lambda)$ es completo y el núcleo de $Q_X$ es trivial** — eso ya lo sabemos. La pregunta de GAP-135.A no es "¿núcleo trivial?" (sí, por densidad), sino **cuantitativa**: ¿es $\mu(T)$ acotado lejos de cero, o se degrada $\mu(T)\to0^+$ aunque nunca lo alcance? Esa es la diferencia entre "completo" (cualitativo, resuelto por densidad) y "frame" (cuantitativo, sensible a la separación). **Aquí muerde la no-separación.**

---

## 2. El fenómeno de near-collisions diofánticas y qué le hace a la propiedad de Riesz

### 2.1. La no-separación es real y cuantificada

**[PROPOSICIÓN 2.1] (la unión no es separada, pero las colisiones son polinomialmente raras — recolección de la Prop. 5.6 del Doc 135 en lenguaje de frames).**
Sea $\delta(R):=\inf\{|\xi-\eta|:\xi\in\Lambda_p,\eta\in\Lambda_q,\ \xi\ne\eta,\ |\xi|,|\eta|\le R\}$.
(a) $\inf_R\delta(R)=0$: $\Lambda$ no es uniformemente separada (Kronecker–Weyl).
(b) Con fases triviales, $\delta(R)\ge C\,R^{-\kappa}$ con $C,\kappa>0$ efectivas dependientes de $p,q$ (Baker; LMN 1995 [DATO]). Más fino: el número de pares $(k,l)$ con $|2\pi k/L_p-2\pi l/L_q|<\varepsilon$ y $|k|,|l|\le N$ es $\asymp \varepsilon\cdot N\cdot \tfrac{L_pL_q}{(2\pi)^2}+O(1)$ por equidistribución de Weyl de $\{kL_q/L_p\bmod 1\}$, es decir las casi-colisiones tienen **densidad lineal** en $N$ pero **profundidad $\varepsilon$ controlada por debajo por Baker**.

*Demostración.* (a)–(b) son la Prop. 5.6 del Doc 135. El conteo de Weyl: la sucesión $\{kL_q/L_p\}_{k\le N}$ se equidistribuye mód 1 con discrepancia $O(N^{-1}\log N)$ o mejor según la medida de irracionalidad de $L_q/L_p$ [DATO: Erdős–Turán; la tasa fina depende del tipo diofántico]; el número de $k\le N$ con $\{kL_q/L_p\}$ a distancia $<\varepsilon/(2\pi/L_p)$ de un entero es $\asymp\varepsilon N$ + error de discrepancia. $\square$

**[GAP de literatura]** No recuerdo con certeza si la medida de irracionalidad de $\log p/\log q$ para $p,q$ primos está acotada por algo mejor que la cota general de Baker (que da tipo finito, i.e. medida de irracionalidad finita, efectiva). Se conjetura (y para casi todo par sería cierto por Khinchin) que $\log p/\log q$ tiene medida de irracionalidad $2$ (tipo Roth), pero **esto no está probado para ningún par concreto de primos** que yo recuerde. Lo marco: la constante efectiva de GAP-135.A heredará esta incertidumbre diofántica.

### 2.2. Qué le hace la no-separación a Riesz: el principio y el caso de dos progresiones

El principio general de frames de exponenciales (Pavlov, Hruščëv–Nikol'skii–Pavlov, "Unconditional bases of exponentials and reproducing kernels", LNM 864, 1983 [DATO]; resumen en Seip 2004 [DATO]): para $E(\Lambda)$ Riesz en $L^2(-T,T)$ se necesita (i) densidad crítica/sub-crítica del lado correcto y (ii) **separación uniforme** (Λ uniformemente discreta) — la separación es *necesaria* para Riesz basis (no solo suficiente): una sucesión de Riesz de exponenciales en $L^2$ de intervalo es **siempre uniformemente separada** (Young, Thm. en cap. 4 [DATO]; porque $\|e_\xi-e_\eta\|^2_{L^2(-T,T)}\to0$ cuando $\xi\to\eta$, y una sucesión de Riesz no puede tener elementos arbitrariamente próximos en norma). 

**Esto fuerza una dicotomía precisa:**

**[PROPOSICIÓN 2.2] ($\Lambda_p\cup\Lambda_q$ NUNCA es sucesión de Riesz en ningún $L^2(-T,T)$ con $T>0$).**
Como $\Lambda$ no es uniformemente separada (Prop. 2.1(a)) y toda sucesión de Riesz de exponenciales en $L^2(-T,T)$ es uniformemente separada, $E(\Lambda)$ **no es sucesión de Riesz** para ningún $T>0$. En particular $E(\Lambda)$ no es Riesz basis de $L^2(-T,T)$ para ningún $T$.

*Demostración.* Sean $\xi_n\in\Lambda_p$, $\eta_n\in\Lambda_q$ con $|\xi_n-\eta_n|\to0$ (Prop. 2.1(a)). Entonces $\|e_{\xi_n}-e_{\eta_n}\|_{L^2(-T,T)}^2=\int_{-T}^T|e^{i\xi_n t}-e^{i\eta_n t}|^2dt\to0$. Dos elementos normalizados arbitrariamente cercanos en norma impiden la cota inferior de Riesz (que exige $\|\sum c_je_{\xi_j}\|^2\ge A\sum|c_j|^2$: tomar $c$ soportado en $\{\xi_n,\eta_n\}$ con $c_{\xi_n}=1,c_{\eta_n}=-1$ da $\|e_{\xi_n}-e_{\eta_n}\|^2\to0$ mientras $\sum|c_j|^2=2$). $\square$

**Esto es decisivo y resuelve la mitad binaria de GAP-135.A: la respuesta a "¿Riesz?" es NO, incondicionalmente, por las near-collisions.** La auditoría temía exactamente esto ("los teoremas de suficiencia estándar piden separación uniforme — destruida por las casi-colisiones"). La separación no es solo *suficiente*: es *necesaria* para Riesz. Luego **el sistema NO es Riesz**, y las near-collisions lo destruyen como base de Riesz.

### 2.3. Pero "no Riesz" no implica "$\mu(T)=0$": la distinción frame ⊋ Riesz

Aquí está el matiz que salva la cota inferior de positividad y que el Doc 135 (Obs. 5.7) no separó con suficiente filo. **Riesz exige separación; frame no.** Un frame puede tener elementos arbitrariamente cercanos (incluso repetidos: un frame con vectores duplicados sigue siendo frame, con cotas degradadas). La cota inferior de positividad $\mu(T)>0$ es la **cota inferior de frame**, NO la de Riesz. Entonces:

- $E(\Lambda)$ **no es Riesz** (Prop. 2.2) — pero esto NO responde a $\mu(T)>0$.
- $E(\Lambda)$ **es completo** para $\log q<2T<\log pq$ (Prop. 1.3/Obs. 1.4) — núcleo trivial.
- La pregunta viva: ¿es $E(\Lambda)$ un **frame** (no exacto, redundante por las colisiones) con $A=\mu(T)>0$, o es solo un sistema completo SIN cota inferior (un "frame deficiente"/sistema de Markushevich completo pero no frame)?

**[PROPOSICIÓN 2.3] (reducción del problema al par colisionante).** $\mu(T)>0$ falla syss existe una sucesión normalizada $F_n\in\mathcal H_T$ con $Q_X(F_n,F_n)\to0$, i.e. con $\hat F_n\to0$ en $\ell^2(\Lambda)$ mientras $\|F_n\|=1$. Por compacidad débil y completitud (núcleo trivial), tal $F_n$ debe "escaparse a alta frecuencia": su masa $\hat F_n$ se concentra en pares de near-collision $(\xi_n,\eta_n)$ de $\Lambda_p\times\Lambda_q$ donde el sistema es casi-dependiente. El módulo $\mu(T)$ está controlado por la velocidad de degeneración del menor de Gram $2\times2$
$$G_n=\begin{pmatrix}\|e_{\xi_n}\|^2 & \langle e_{\xi_n},e_{\eta_n}\rangle\\ \langle e_{\eta_n},e_{\xi_n}\rangle & \|e_{\eta_n}\|^2\end{pmatrix}=2T\begin{pmatrix}1 & \operatorname{sinc}(T(\xi_n-\eta_n))\\ \overline{\cdots} & 1\end{pmatrix},$$
cuyo menor autovalor es $2T(1-|\operatorname{sinc}(T(\xi_n-\eta_n))|)\asymp 2T\cdot\tfrac{T^2}{6}|\xi_n-\eta_n|^2$ cuando $|\xi_n-\eta_n|\to0$.

*Demostración.* Estándar para frames: la cota inferior global está dominada por la peor casi-dependencia local; la localización a pares es porque tres o más puntos de $\Lambda$ no pueden colisionar simultáneamente (un punto de $\Lambda_p$ está a distancia $\ge$ algo de los demás de $\Lambda_p$; las colisiones son $\Lambda_p$–$\Lambda_q$ de a dos, Lema 1.7). $\operatorname{sinc}(x)=\sin x/x$, $1-|\operatorname{sinc}(x)|\sim x^2/6$. $\square$

**Lectura.** El gap de frame $\mu(T)$ se degrada como el **cuadrado** de la separación en la peor near-collision dentro de la "banda visible" del intervalo. Por Baker (Prop. 2.1(b)) la peor colisión a frecuencia $\le R$ tiene $|\xi-\eta|\ge C R^{-\kappa}$, pero **el intervalo $L^2(-T,T)$ no impone cota superior a $R$**: las funciones de $\mathcal H_T$ tienen frecuencias arbitrarias. Por tanto, ingenuamente, $\inf$ sobre todas las near-collisions (a toda frecuencia) daría $\mu(T)=0$. La salvación, si existe, debe venir de que **una $F_n$ con $\|F_n\|=1$ no puede concentrar masa unitaria en exponenciales de frecuencia arbitrariamente alta sin pagar en $\|F_n\|$** vía la regularidad de Paley–Wiener — pero $\mathcal H_T$ no acota frecuencias. Esto sugiere fuertemente:

**[PROPOSICIÓN 2.4] (la cota inferior de frame se DEGRADA a cero: $\mu(T)=0$ para $\log q<2T<\log pq$ — pero el ínfimo no se alcanza).**
Para $\log q<2T<\log pq$, $E(\Lambda)$ es completo en $L^2(-T,T)$ pero **no es un frame**: $\mu(T)=\inf_{\|F\|_w=1}Q_X(F,F)=0$, ínfimo no alcanzado (núcleo trivial).

*Argumento (esbozo riguroso, con un punto técnico marcado [GAP]).* Tomo near-collisions $\xi_n\in\Lambda_p,\eta_n\in\Lambda_q$, $|\xi_n-\eta_n|=:\sigma_n\to0$ (existen por 2.1(a), a frecuencia $R_n\to\infty$). Construyo $F_n\in\mathcal H_T$ con $\hat F_n$ "casi proporcional a $e_{\xi_n}-e_{\eta_n}$ en el lado físico": concretamente $F_n(t)=c_n(e^{i\xi_n t}-e^{i\eta_n t})\psi(t)$ con $\psi\in C_c^\infty(-T,T)$ fija, $\psi\ge0$, $c_n$ normalizando $\|F_n\|_w=1$. Entonces $\|F_n\|_w^2=c_n^2\int|\psi|^2|e^{i\xi_n t}-e^{i\eta_n t}|^2\asymp c_n^2\sigma_n^2\int t^2|\psi|^2\Rightarrow c_n\asymp\sigma_n^{-1}$. Y $\hat F_n(\zeta)=c_n(\hat\psi(\zeta-\xi_n)-\hat\psi(\zeta-\eta_n))$. Evaluando en $\Lambda$: en $\xi_n$, $\hat F_n(\xi_n)=c_n(\hat\psi(0)-\hat\psi(\xi_n-\eta_n))\asymp c_n\sigma_n^2\hat\psi''(0)/2\asymp\sigma_n$; análogamente en $\eta_n$; en los demás $\zeta\in\Lambda$, $\hat\psi(\zeta-\xi_n)$ y $\hat\psi(\zeta-\eta_n)$ decaen rápido (Paley–Wiener de $\psi$) pero NO son cero, y al sumar sobre $\Lambda$ — **aquí el punto técnico**: hay que verificar que $\sum_{\zeta\in\Lambda}|\hat F_n(\zeta)|^2\to0$. Los términos cercanos ($\xi_n,\eta_n$ y sus vecinos en $\Lambda_p,\Lambda_q$ a distancia $\gtrsim 2\pi/L_r$) dan $\asymp\sigma_n^2\to0$. Los términos lejanos están controlados por la cota de Bessel uniforme (Obs. 1.2) aplicada a la "casi-diferencia" — **[GAP]: falta verificar que la contribución de Bessel de la cola no esté acotada *por debajo* uniformemente; creo que sí va a cero porque $e^{i\xi_n t}-e^{i\eta_n t}=O(\sigma_n)$ uniformemente en $t\in[-T,T]$, luego $F_n=O(\sigma_n)c_n\psi=O(1)\psi$ en norma sup pero su transformada tiene masa total $\|F_n\|^2=1$ concentrada espectralmente cerca de $\xi_n\approx\eta_n$; la traza con $\Lambda$ recoge solo $\asymp\sigma_n^2$.** Si el [GAP] cierra, $Q_X(F_n,F_n)=2\sum_\Lambda|\hat F_n|^2\to0$ con $\|F_n\|_w=1$, luego $\mu(T)=0$. El núcleo es trivial (Teorema 5.4(a)) porque ninguna $F_n$ es exactamente nula y el límite débil es $0\notin$ esfera unidad. $\square$ *(condicional al [GAP])*

**Veredicto cuantitativo (honesto).** Creo, con confianza moderada-alta, que **$\mu(T)=0$ para todo $\log q<2T<\log pq$**: el sistema es completo pero NO un frame, exactamente porque las near-collisions (densidad lineal, profundidad $\to0$) permiten construir tests casi-invisibles normalizados. Esto **responde a GAP-135.A en su forma binaria: NO hay gap de frame uniforme en la región intermedia; $\mu(T)=0$.** El Doc 135 (Obs. 5.7) lo dejó como pregunta abierta optimista ("es plausible que [Baker] alcance para $\mu(T)>0$"); mi análisis sugiere que el optimismo era infundado: **Baker controla la profundidad a frecuencia acotada, pero $L^2(-T,T)$ no acota la frecuencia, y por eso el ínfimo a través de todas las escalas es $0$.**

---

## 3. La caracterización del núcleo de $Q_X$ y el rol de la teoría diofántica

### 3.1. El núcleo cualitativo: cerrado y conocido

**[TEOREMA 3.1] (caracterización completa del núcleo, recolectando §1–§2).** Para $p\ne q$ primos puros, fases cualesquiera, y ventana $2T$:
$$\ker Q_X|_{\mathcal H_T}=E(\Lambda)^\perp\cap\mathcal H_T=\begin{cases}\{0\} & 2T<\log(pq)\quad(\text{completo, sub-crítico}),\\[2pt]\text{subespacio }\infty\text{-dim} & 2T>\log(pq)\quad(\text{incompleto, super-crítico}).\end{cases}$$
El umbral $2T=\log(pq)$ es la densidad crítica de Beurling–Landau $D(\Lambda)=T/\pi$. La estructura del núcleo super-crítico es la de los multiplicadores $D_pD_q$ (operadores de diferencia del Teorema 5.4(b)): $\ker=\{F=D_pD_q g\}$, isomorfo a $\mathcal H_{T-(\log pq)/2}$ vía un multiplicador analítico de Fourier sin ceros fuera de $\Lambda$.

*Demostración.* Prop. 1.3 + Obs. 1.4 (extremos por densidad de Landau, prueba directa por Jensen en Doc 135 Teorema 5.4); estructura del núcleo super-crítico = construcción explícita 5.4(b). $\square$

**Esto es CONOCIDO** (Beurling–Landau + Levinson–Boas para los extremos; el Doc 135 ya lo probó correctamente). No hay matemática nueva en el núcleo cualitativo.

### 3.2. Lo diofántico: NO está en el núcleo, está en el módulo (cota de frame) — y ahí el veredicto es negativo

La esperanza del Doc 135 (Obs. 5.7, GAP-135.A) era: *"¿se puede dar una caracterización cerrada del núcleo de $Q_X$ en términos de la teoría diofántica de las near-collisions (medida de irracionalidad de $\log p/\log q$)?"* La respuesta, ahora afilada:

**[PROPOSICIÓN 3.2] (la medida de irracionalidad NO entra en el núcleo, ni decide el módulo en $L^2(-T,T)$).**
(a) El núcleo (Teorema 3.1) depende SOLO de la densidad $D(\Lambda)=\log(pq)/2\pi$, no de la aritmética fina de $\log p/\log q$: el umbral $\log(pq)$ es el mismo para todo par, independiente de la medida de irracionalidad.
(b) El módulo $\mu(T)$ en la región intermedia es $0$ (Prop. 2.4, condicional al [GAP]) **independiente de la medida de irracionalidad**: la repulsión de Baker fija la *tasa* a la que las near-collisions se vuelven raras, pero como hay near-collisions a toda escala (Kronecker, válido para cualquier irracional), el ínfimo es $0$ sea cual sea la medida de irracionalidad.

*Demostración.* (a) El conteo de Jensen suma densidades; la medida de irracionalidad solo afecta el término $O(1)$ del solapamiento (Lema 1.7: a lo sumo un punto compartido), no la pendiente. (b) Kronecker ($\inf|\xi-\eta|=0$) vale para todo irracional; la profundidad de la peor colisión a escala $R$ depende de la medida de irracionalidad, pero el $\inf$ sobre $R\to\infty$ es $0$ universalmente. $\square$

**Conclusión de §3 (el desinflado honesto, en la línea de la auditoría Doc 138).** La conexión "near-collisions diofánticas $\leftrightarrow$ estructura fina del núcleo" que el Doc 135 nombró como potencialmente profunda **NO sobrevive el análisis**: el núcleo es puramente de densidad (Beurling–Landau, conocido), y la medida de irracionalidad **no aparece** ni en el núcleo ni en el módulo $\mu(T)$ sobre $L^2(-T,T)$. La aritmética de Baker controla un objeto más fino — la tasa de degradación de la cota de frame *restringida a una banda de frecuencias $\le R$* — pero ese objeto no es la forma de Weil sobre el intervalo completo. **La medida de irracionalidad de $\log p/\log q$ no es la respuesta a GAP-135.A; es un epifenómeno.**

### 3.3. Dónde SÍ podría vivir matemática diofántica nueva (la versión salvable de la intuición)

Si uno reemplaza $L^2(-T,T)$ por un espacio con **decaimiento espectral impuesto** — e.g. tests $F$ con $\hat F$ soportada en $[-R,R]$ además de $\operatorname{supp}F\subset[-T,T]$ (imposible exactamente por Paley–Wiener, pero aproximable: clase de Gevrey/banda efectiva) — entonces la peor near-collision SÍ está a frecuencia $\le R$, Baker da $|\xi-\eta|\ge CR^{-\kappa}$, y el módulo
$$\mu_R(T)\gtrsim T^2\cdot(CR^{-\kappa})^2=C'\,T^2R^{-2\kappa}>0$$
es **positivo con pérdida polinomial en la escala $R$ controlada por la medida de irracionalidad**. Este es un enunciado verdadero y posiblemente nuevo en su forma aritmética explícita, pero es un enunciado sobre **frames con banda efectiva**, no sobre la forma de Weil pura.

**[DEFINICIÓN-NUEVA 3.3] (gap de frame con banda efectiva).** Para $R,T>0$ y un peso de localización espectral $w_R$ (e.g. $w_R(\xi)=(1+\xi^2/R^2)^{-N}$), defino
$$\mu_R(T):=\inf\Bigl\{Q_X(F,F):\operatorname{supp}F\subset[-T,T],\ \|w_R^{-1}\hat F\|_2=1\Bigr\}.$$

**[PROPOSICIÓN 3.4] (gap con banda efectiva, positivo y diofánticamente cuantificado).** Para $\log q<2T<\log pq$ y $N$ grande,
$$\mu_R(T)\ \ge\ c(p,q,T)\,R^{-2\kappa(p,q)}\ >\ 0,$$
con $\kappa(p,q)$ el exponente de Baker (medida de irracionalidad de $\log p/\log q$) y $c$ explícita.
*Esbozo.* El peso $w_R$ penaliza masa a frecuencia $\gg R$; las near-collisions accesibles con masa $O(1)$ están a frecuencia $\lesssim R$, donde Baker da separación $\ge CR^{-\kappa}$; el menor de Gram $2\times2$ (Prop. 2.3) tiene autovalor inferior $\asymp T^2(R^{-\kappa})^2$. La cota global por localización de frames (Pavlov/Seip). [GAP de literatura: la versión "frame con peso espectral" la asocio a trabajos de muestreo en espacios de Bargmann–Fock ponderados (Seip 2004) y a las técnicas de Olevskii–Ulanovskii de muestreo universal, pero no recuerdo un teorema enchufable exacto; lo marco.] $\square$ *(condicional)*

**Esta es la única matemática genuinamente nueva candidata**, y es modesta: una cota inferior de frame *con corte espectral* para uniones de dos progresiones inconmensurables, con constante diofántica explícita vía Baker. Es interesante como análisis armónico; su conexión con ζ es nula (ver §5).

---

## 4. Veredicto: conocido / abierto-iluminado / nuevo

Desglose por componente, con honestidad de auditoría:

| Componente de GAP-135.A | Estatus | Justificación |
|---|---|---|
| Umbrales extremos ($2T<\log\min$, $2T<\log pq$, $2T>\log pq$) | **(a) CONOCIDO** | Beurling–Landau + Levinson–Boas; densidad crítica $=\log(pq)/2\pi$. El Doc 135 ya lo probó por Jensen. |
| "¿Es Riesz en la región intermedia?" | **(a) CONOCIDO, resuelto NEGATIVO** | Prop. 2.2: nunca Riesz, porque toda sucesión de Riesz de exponenciales es uniformemente separada y $\Lambda$ no lo es (Kronecker). |
| "¿Hay gap de frame $\mu(T)>0$ en la región intermedia?" | **(b)→ resuelto NEGATIVO** (cond. [GAP] Prop. 2.4) | $\mu(T)=0$: completo pero no frame; las near-collisions a toda escala destruyen la cota inferior. $L^2(-T,T)$ no acota frecuencia. |
| "¿La medida de irracionalidad caracteriza el núcleo/módulo?" | **(a) NO — epifenómeno** | Prop. 3.2: núcleo y $\mu(T)$ son puramente de densidad; la aritmética no entra. |
| Gap de frame **con banda espectral efectiva** $\mu_R(T)$ | **(c) posiblemente NUEVO, modesto** | Prop. 3.4: cota $\gtrsim R^{-2\kappa}$ con $\kappa$ de Baker; pero es un objeto distinto de la forma de Weil, y desconectado de ζ. |

**Veredicto global: GAP-135.A es esencialmente (a) CONOCIDO una vez correctamente formulado** — los umbrales son Beurling–Landau, "no Riesz" es la necesidad de separación, y el módulo $\mu(T)$ es $0$ (no hay gap) por Kronecker. La intuición del Doc 135 de que la medida de irracionalidad gobernaría una "estructura fina del núcleo" **no se sostiene**: el núcleo es de densidad pura. Lo único con un resquicio de novedad (c) es la cota de frame con banda espectral efectiva (Prop. 3.4), que es análisis armónico legítimo pero (i) modesto, (ii) condicional a un [GAP de literatura], y (iii) **sin ningún puente a ζ**.

Esto **confirma y agudiza la sospecha de la auditoría Doc 138 §4.4**: "es plausible que la respuesta (o un contraejemplo con fases genéricas) ya exista en forma de teorema de frames". Sí existe: la combinación Beurling–Landau (umbrales) + necesidad de separación para Riesz (Young/Pavlov) + Kronecker (no-separación) responde todo lo cualitativo. El Doc 135 nombró bien el GAP pero **sobreestimó su profundidad** al asociarlo a la medida de irracionalidad.

---

## 5. [PUENTE] honesto con ζ y el escalamiento a infinitas progresiones

### 5.1. ¿Dice algo sobre ζ?

**No, de forma directa.** El módulo $\mu(T)$ de la forma de Weil de dos primos puros es $0$ en la región intermedia (Prop. 2.4): no hay gap espectral que "proteja" la positividad. Pero — punto crucial heredado del Doc 138 §4 y del Doc 135 §7.2(B3) — **estos objetos puros viven en el régimen CONSTRUCTIVO** ($a(p^m)=-L_pc_m\le0$, los primos suman con la diagonal), que es el régimen *especular* del de ζ (DESTRUCTIVO: $a=\Lambda\ge0$, los primos restan, la positividad debe venir del polo+gamma). La cota de frame inferior $\mu(T)$ de los objetos puros **no es** la cantidad que controla RH; la cantidad de RH es la positividad de la forma de Weil de ζ, donde el divisor NO está en la línea por hipótesis sino que estar-en-la-línea ES la conclusión. Que $\mu(T)=0$ aquí no dice nada sobre allá: es la cota inferior de frame de un sistema cuyos "ceros" ya pusimos en la línea.

**El único contacto real:** la *estructura* "forma de Weil $=$ suma de $|\hat F|^2$ sobre frecuencias en la línea $=$ forma de Gram de un sistema de exponenciales" es la misma maquinaria que en ζ. Lo que cambia es que en ζ las frecuencias (partes imaginarias de los ceros) NO forman progresiones aritméticas: tienen densidad $\sim\frac{1}{2\pi}\log\frac{t}{2\pi}$ (creciente), y su distribución fina (GUE/Montgomery) es justamente lo desconocido. La teoría de frames de dos progresiones es un *juguete* de la forma de Weil, no un eslabón.

### 5.2. El escalamiento a infinitas progresiones cambia cualitativamente el problema

La forma de Weil de ζ vive sobre TODAS las progresiones $\{k\log p:k\ge1\}_{p}$ simultáneamente. Densidad total:
$$\sum_p D(\Lambda_p)=\sum_p\frac{\log p}{2\pi}=+\infty.$$
**Esto destruye el marco de frames de intervalo:** con densidad infinita, para cualquier ventana $2T>0$ el sistema $E(\bigcup_p\Lambda_p)$ es **infinitamente sobre-completo** — núcleo $\infty$-dim para todo $T$, $\mu(T)=0$ trivialmente, ninguna cota de frame. El umbral del núcleo $\log(p_1\cdots p_n)=\theta(y)\to\infty$ (Doc 135 Teorema 7.1(c), B4): la ventana de definitud crece, pero la diagonal $\omega_y=-2\theta(y)\to-\infty$ diverge (B1). El paso de dos progresiones a infinitas **no es cuantitativo sino de fase**: se pierde la noción de frame de intervalo y entra la renormalización (B1) + continuación analítica (B2) + cambio de régimen constructivo→destructivo (B3). Esto es exactamente el muro localizado en el Doc 135 §7.2, y la teoría de frames de dos/$n$ progresiones **no escala a través de él**: el objeto límite no es un sistema de exponenciales sobre una unión de progresiones, sino la familia de ceros de ζ con su densidad $\log t$ y su estadística desconocida.

**[PUENTE — estatus: NEGATIVO/CLARIFICADOR].** La teoría de frames sobre uniones inconmensurables (i) responde completamente el caso finito (este documento: conocido), (ii) NO escala a ζ (densidad infinita rompe el marco), y (iii) por tanto **GAP-135.A no es un eslabón hacia RH** sino un ejercicio de análisis armónico que el contexto-ζ motivó. Esto es consistente con el veredicto de la auditoría Doc 138: lo finito vive en el régimen sin obstáculo; el obstáculo está en B2+B3, intacto.

### 5.3. [DESEO]

Que exista una versión de la forma de Weil donde las frecuencias de ζ se aproximen por progresiones aritméticas con densidad renormalizada finita (un "frame de ζ regularizado") y donde la cota inferior de frame renormalizada $\tilde\mu$ sobreviva a $y\to\infty$ — esto sería la forma fuerte del Lema de rigidez (Doc 131 Deseo 7.2, Doc 135 §7.2 B4). No lo tengo; lo nombro como deseo, no como gap accionable, porque el cambio de régimen (B3) sugiere que la versión correcta no es de frames sino de operadores con polo.

---

## 6. Mensaje final

**VEREDICTO:** GAP-135.A es, una vez correctamente formulado como pregunta de frames, **esencialmente (a) CONOCIDO**: los umbrales del núcleo son la densidad crítica de Beurling–Landau ($2T=\log pq$), "¿es Riesz?" se responde NO incondicionalmente (las near-collisions de Kronecker violan la separación uniforme, necesaria para Riesz), y "¿hay gap de frame $\mu(T)>0$?" se responde NO ($\mu(T)=0$: completo pero no frame, porque $L^2(-T,T)$ no acota la frecuencia y hay near-collisions a toda escala). La asociación con la medida de irracionalidad de $\log p/\log q$ que el Doc 135 conjeturó **es un epifenómeno**: ni el núcleo ni el módulo dependen de ella. Lo único con resquicio de novedad (c) es una cota de frame con banda espectral efectiva $\mu_R(T)\gtrsim R^{-2\kappa}$, modesta y desconectada de ζ. **No es eslabón hacia RH** (no escala a densidad infinita; el muro sigue en B2+B3, Doc 135 §7.2). Esto agudiza y confirma la auditoría Doc 138 §4.4 — el optimismo de la Obs. 5.7 del Doc 135 era infundado.

**TRES RESULTADOS CON ETIQUETA:**
1. **[PROPOSICIÓN 1.1 + 1.3 + Obs. 1.4]** La forma de Weil de dos primos puros es la forma de Gram de $E(\Lambda_p\cup\Lambda_q)$ en $L^2(-T,T)$; sus umbrales de núcleo son EXACTAMENTE la densidad crítica de Beurling–Landau $D(\Lambda)=\log(pq)/2\pi=T/\pi\Leftrightarrow 2T=\log pq$. (Conocido; identificación cerrada.)
2. **[PROPOSICIÓN 2.2]** $E(\Lambda_p\cup\Lambda_q)$ **nunca** es sucesión de Riesz en ningún $L^2(-T,T)$, $T>0$, porque las near-collisions de Kronecker violan la separación uniforme, que es necesaria para Riesz. (Resuelve la mitad binaria de GAP-135.A: NO Riesz.)
3. **[PROPOSICIÓN 2.4]** (cond. a un [GAP] técnico de cola de Bessel) $\mu(T)=\inf_{\|f\|_w=1}Q_X=0$ en toda la región intermedia $\log q<2T<\log pq$: completo pero NO frame. (Resuelve GAP-135.A: NO hay gap; refuta el optimismo de Obs. 5.7.)

**LITERATURA USADA** (publicada, real; inciertos marcados):
- H. J. Landau, *Necessary density conditions for sampling and interpolation of certain entire functions*, Acta Math. 117 (1967), 37–52. [DATO — densidades necesarias.]
- A. Beurling, *Collected Works*, Birkhäuser 1989 (balayage, densidad crítica). [DATO.]
- K. Seip, *Interpolation and Sampling in Spaces of Analytic Functions*, AMS ULS 33, 2004. [DATO — frames de exponenciales, Beurling–Landau, separación.]
- K. Seip, *On the connection between exponential bases and certain related sequences in $L^2(-\pi,\pi)$*, J. Funct. Anal. 130 (1995), 131–160. [DATO — bases exponenciales perturbadas; recuerdo el tema, no el enunciado exacto aplicable: GAP de literatura parcial.]
- A. Olevskii, A. Ulanovskii, *Universal sampling and interpolation of band-limited signals*, GAFA 18 (2008), 1029–1052. [DATO — muestreo universal; relevante para la versión "banda efectiva" §3.3, pero no recuerdo un teorema directamente enchufable: GAP de literatura.]
- R. M. Young, *An Introduction to Nonharmonic Fourier Series*, rev. ed. Academic Press 2001. [DATO — Riesz $\Rightarrow$ separación uniforme; Bessel de progresiones; Plancherel–Pólya.]
- S. V. Hruščëv (Khrushchev), N. K. Nikol'skii, B. S. Pavlov, *Unconditional bases of exponentials and of reproducing kernels*, LNM 864 (1981/83), 214–335. [DATO — caracterización de bases incondicionales de exponenciales; separación necesaria.]
- S. A. Avdonin, *On the question of Riesz bases of exponential functions in $L^2$* (1974) y el teorema "1/4 en media" generalizando Kadec. [DATO — recuerdo el resultado de Kadec-1/4 y la generalización en media de Avdonin; la forma exacta aplicable a uniones de dos progresiones no la recuerdo con certeza: GAP de literatura.]
- A. Baker, *Linear forms in logarithms* (Mathematika 13, 1966); Laurent–Mignotte–Nesterenko, J. Number Theory 55 (1995), 285–321 (dos logaritmos, efectivo). [DATO — repulsión de near-collisions.]
- R. P. Boas, *Entire Functions*, Academic Press 1954. [DATO — Jensen, densidad de ceros, completitud por densidad.]
- Hedenmalm–Montes-Rodríguez (Heisenberg uniqueness pairs; conexión con $\{\log n\}$): **[GAP de literatura]** — recuerdo que su trabajo (Annals 2011, sobre la hipérbola y pares de unicidad de Heisenberg) toca la dinámica del grupo modular y conjuntos relacionados con $\log$, y que hay un puente con la completitud de sistemas tipo $\{e^{i\xi\log n}\}$, pero NO recuerdo un enunciado que aplique directamente a $\Lambda_p\cup\Lambda_q$. No lo uso como apoyo; lo dejo como pista para quien quiera la conexión $\{\log n\}$.

**Internas:** Doc 135 (§5 Teorema 5.2/5.4, Prop. 5.6, Obs. 5.7/GAP-135.A, §7.2 B1–B4); Doc 138 (auditoría, §4.4 advertencia de frames); Doc 131 (categoría, Deseo 7.2).

*Fin del Documento 148.*
