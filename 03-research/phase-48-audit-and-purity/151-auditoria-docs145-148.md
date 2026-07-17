# Doc 151 — Auditoría adversarial de los Docs 145 y 148

**Programa:** Hipótesis de Riemann — Phase 48: auditoría y pureza.
**Fecha:** junio 2026.
**Mandato:** matar antes de uso. Toda pieza load-bearing de los Docs 145 (espectralidad del objeto semilocal; colapso de H⁺) y 148 (GAP-135.A como problema de frames) se ataca con las herramientas de Bochner, medidas espectrales, y Beurling–Landau. Disciplina post-W_λ: ninguna deferencia.
**Fuentes leídas completas:** Doc 145, Doc 148, Doc 142 (Teoremas A/B, trilema §8, GAP-142.A/B), Doc 135 §1–§7 (normalizaciones exactas, §5 estructura fina, Obs. 5.7), Doc 131 §4–§7 (Def. 4.1 espectral-EF, Teo. 4.4, Def. 6.1 Axioma H, Teo. 6.3, Deseo 6.9 = H⁺), P48 `main.tex` (Conjecture 7.1).
**Contrato:** [TEOREMA]/[PROPOSICIÓN] solo con prueba completa aquí; [PUENTE] con estatus; [GAP] nombrado; [DATO] literatura real; [GAP de literatura] marcado. Sin numéricos: solo forma cerrada.

---

## 0. Veredicto por pieza

| Pieza | Enunciado | Veredicto |
|---|---|---|
| **A.a** (D145 Thm 2.2) | $\mathcal B_w$ representable espectral-positiva $\iff w\ge0$ c.t.p. | **AGUANTA** para la noción continua (Def. 2.1). Erratum de redacción: la frase "equivalentemente, suma de cuadrados de evaluaciones" confunde la noción atómica con la continua (§1.2). La dirección load-bearing (parte negativa ⟹ ninguna medida positiva ⟹ a fortiori ninguna atómica) es la usada y es correcta. |
| **A.b** (D145 Thm 2.4) | $\Omega$ no es transformada de medida positiva; $\mathcal A$ indefinida | **AGUANTA.** $\Omega(0)=\psi(\tfrac14)-\log\pi<0$ verificado por Gauss (forma cerrada exacta); continuidad + Thm 2.2 cierran. |
| **A.c** (D145 Thm 3.4) | $X_S^{\mathrm{ar}}$ no es espectral-positivo, "dos pruebas independientes" | **AGUANTA solo por la prueba (A).** La prueba (B) tiene un [GAP] real (§1.4): el paso "tests de ventana $<\log2$ con $\hat f(1)=0$ realizan $\mathcal A<0$" no está probado y colisiona con GAP-142.A (abierto). "Dos pruebas independientes, ambas completas" es **falso**. Además: lo decidido es espectral-**positivo**; GAP-142.B en su formulación literal (Def. 4.1, espectral-EF) **sigue abierto** (§2.3). |
| **A.d** (D145 Thm 4.1 + Cor 4.2) | clase semilocal-finita de H⁺ vacía; H⁺ colapsa hacia RH | **PARCIAL.** (i) La vacuidad está probada solo para $a=\Lambda\cdot\mathbf 1_S$; la clase de H⁺ a $S$ finito admite cualquier $a\ge0$. **Reparado aquí** ([PROP. R.2], §2.2: prueba completa para todo $a\ge0$). (ii) "La única instancia no vacía con peso $\Gamma$ es $\zeta$ completa": **no probado** (§2.4). (iii) La rama (1) del trilema se excluye por estipulación de lectura, no por teorema (§2.3). (iv) Sobre el mundo puro NO hay sobre-reclamo: H⁺ exige bloque polar estándar, los puros no lo tienen, nunca estuvieron en la clase (§2.1). |
| **B.a** (D148 Prop 1.1+1.3+Obs 1.4) | Weil de dos primos = Gram de $E(\Lambda)$; umbrales = Beurling–Landau | **AGUANTA.** La identificación es **exacta, sin simplificación de pesos**: los pesos aritméticos $2L_p\,p^{m/2}$ se absorben íntegros vía $e^{t/2}$ + Poisson (§4). Densidad $D^{\pm}(\Lambda)=\log(pq)/2\pi$ re-derivada (§3.1). La confusión de dirección de la Prop. 1.3 fue honestamente corregida en Obs. 1.4 y la versión final es correcta. |
| **B.b** (D148 Prop 2.2) | $E(\Lambda)$ nunca es sucesión de Riesz | **AGUANTA.** Re-derivado con forma cerrada (§3.2), para todo $T>0$ y toda elección de fases. |
| **B.c** (D148 Prop 2.4) | $\mu(T)=0$ en toda la región intermedia (no hay frame) | **MUERE.** Doble muerte: (1) el paso "términos cercanos $\asymp\sigma_n^2$" de su esbozo es **falso** — los vecinos de retícula reciben masa $\Theta(1)$, no $O(\sigma_n^2)$ (§3.3); (2) **contraejemplo con prueba completa** ([TEOREMA R.1], §3.4): $\mu(T)>0$ con constante explícita en forma cerrada para $\log q<2T\le\log q+\theta$, $\theta:=\operatorname{dist}(\log q,(\log p)\mathbb Z)>0$. La Prop. 2.4 afirmaba $\mu(T)=0$ en TODA la región: refutada. La Prop. 2.3 (reducción al menor de Gram $2\times2$) cae con ella: error de categoría análisis/síntesis (§3.3). |
| **B.d** (D148 §3.2, §4) | "la aritmética es epifenómeno"; GAP-135.A esencialmente conocido | **MUERE.** La constante y la ventana de validez del Teorema R.1 están gobernadas por $\theta=\min_{m\ge1}\bigl|\log(q/p^m)\bigr|$ — una cantidad **aritmética** (proximidad multiplicativa de $q$ a las potencias de $p$). La Prop. 3.2(b) era condicional a la Prop. 2.4 y cae con ella. La 3.2(a) (el **núcleo** es de densidad pura) sobrevive. El veredicto global "(a) CONOCIDO" se invierte: GAP-135.A se **reabre**, con la respuesta probable **opuesta** a la del Doc 148 (§3.5). |

---

## 1. El Teorema 2.2 del Doc 145: discreto vs. continuo, y la cuantificación de la clase de tests

### 1.1. Las dos nociones, separadas con filo

Hay dos enunciados distintos bajo el nombre "representación espectral positiva":

- **(C) continua:** existe medida de Borel $\mu\ge0$ de crecimiento polinomial con $\mathcal B(f)=\int|\hat F|^2\,d\mu$ para todo $f\in C_c^\infty(G)$. (Def. 2.1 del Doc 145, tal como está escrita.)
- **(D) discreta/del programa:** $\mu=\sum_k m_k\delta_{\xi_k}$ atómica, $m_k\ge0$, densidad polinomial — i.e. $\mathcal B(f)=\sum_k m_k|\hat F(\xi_k)|^2$, el sentido de la Def. 1.2 (divisor en la línea).

Obviamente (D) ⟹ (C). El recíproco es **falso**: $w\equiv1$ satisface (C) con $\mu=$ Lebesgue y no satisface (D) (ninguna medida atómica de densidad polinomial coincide con Lebesgue contra todos los núcleos de Fejér $|\hat F|^2$, $F\in C_c^\infty$; las evaluaciones puntuales no reproducen una densidad absolutamente continua sobre una familia que separa intervalos). Por tanto la cadena lógica correcta del Doc 145 es:

$$\text{(D) falla} \impliedby \text{(C) falla} \iff w\not\ge0 \text{ c.t.p.} \quad\text{(Thm 2.2)}.$$

**Verificación de la dirección usada.** El Thm 2.4 y el Thm 3.4(B) usan exactamente la contrapositiva segura: $\Omega(0)<0$ ⟹ no-(C) ⟹ no-(D). El Thm 3.4(A) ni siquiera pasa por aquí: usa no-positividad de la forma (Prop. 3.1 = Doc 142 Teo. B) contra "(D) ⟹ $Q\ge0$". **Ambos usos son válidos.** Lo que NO es válido es la frase del Thm 2.4 "equivalentemente, $\mathcal A$ no es suma de cuadrados de evaluaciones": la negación de (C) y la de (D) no son equivalentes (la de (C) es estrictamente más fuerte); como aquí se prueba la fuerte y se usa la débil, el error es de redacción, no de contenido. **Erratum no fatal; corregir "equivalentemente" por "en particular".** Lo mismo aplica al paréntesis de la Def. 2.1, que debe leerse como "el caso atómico es una instancia", no como identificación.

### 1.2. La prueba del Thm 2.2, auditada paso a paso

(⟸) $w\ge0$ ⟹ (C) con $d\mu=w\,d\xi/2\pi$: trivial y correcto. (⟹): el argumento del punto de Lebesgue es correcto con dos precisiones que verifiqué:

1. **El test no es $C_c^\infty$ sino Schwartz** ($\hat F_{\delta}$ de soporte compacto ⟹ $F$ entera, no compacta). La aproximación declarada funciona: $|\mathcal B_w(F)-\mathcal B_w(G)|\le\frac1{2\pi}\int(|\hat F|+|\hat G|)\,|\hat F-\hat G|\,|w|$ con $|w|\le C(1+|\xi|)^M$ está controlada por seminormas de Schwartz, y $C_c^\infty$ es denso en $\mathcal S$. Válido.
2. **El límite del promedio:** $\int\hat\phi(u)^2\,[w(\xi_0+\delta u)-w(\xi_0)]\,du\le\|\hat\phi^2\|_\infty\,\delta^{-1}\int_{|v|\le\delta}|w(\xi_0+v)-w(\xi_0)|\,dv\to0$ en cualquier punto de Lebesgue de $w$; c.t.p. punto de $E=\{w<0\}$ es punto de Lebesgue con $w(\xi_0)<0$ si $|E|>0$. Válido. (El subíndice $R$ de $F_{\delta,R}$ es vestigial: nunca se usa. Cosmético.)

**Veredicto A.a: el Teorema 2.2 es correcto como teorema sobre la noción (C), con el erratum de §1.1.** La etiqueta "Bochner del lado del multiplicador" es honesta [DATO: Bochner, *Lectures on Fourier Integrals*, Princeton 1959; Reed–Simon II, Thm IX.9 (Bochner–Schwartz) para la versión distribucional].

### 1.3. La cuantificación de la clase de tests: ¿sobre qué clase se define "espectral-positivo"?

Este era el punto de ataque más peligroso, y lo verifiqué contra las tres fuentes:

- Doc 131, Def. 6.1 (Axioma H): "$Q_X(f,f)\ge0$ **para todo** $f\in C_c^\infty(G)$".
- Doc 131, Def. 4.1 / Doc 145, Def. 1.1 (espectral-EF): la identidad $\sum_{\rho\in Z}\hat f(\rho)=W_X(f)$ se exige **para todo** $f\in C_c^\infty(G)$.
- P48, Conjecture 7.1 (H⁺): hipótesis sobre el objeto, conclusión "$X$ satisfies $H$" — de nuevo todo $C_c^\infty(G)$.

**No hay restricción de clase en ninguna definición** (ni $\hat f(1)=0$, ni ventana). El bloque polar es parte de $W_X$, no una condición sobre los tests. Por tanto el peligro hipotético ("una $w$ con parte negativa invisible para una clase restringida") **no afecta al veredicto del Thm 3.4**, cuya prueba (A) usa un test legítimo de la clase completa (la familia $f_T$ de Doc 142, $f_T\in C_c^\infty(G)$ sin restricciones).

**Pero el peligro se realiza DENTRO de la prueba (B).** Eso es §1.4.

### 1.4. [GAP-151.C] La prueba (B) del Thm 3.4 no es completa

La prueba (B) restringe a la subclase $\mathcal R=\{f:\operatorname{supp}F$ en intervalo de longitud $\ell<\log2$, $\hat f(1)=0\}$, sobre la cual $Q_S=\mathcal A$ exactamente (eso sí es correcto: los lags $mL_p\ge\log2>\ell$ anulan $P_S$, y $\hat f(1)=0$ mata el polar). Luego dice: si $\mu\ge0$ representara $Q_S$ en la clase completa, entonces $\mathcal A(f)=\int|\hat F|^2d\mu\ge0$ en $\mathcal R$ — correcto — y que esto "contradice el Teorema 2.4". **Aquí está el hueco:** el Teorema 2.4 da la indefinitud de $\mathcal A$ sobre la clase **completa**; para la contradicción se necesita $f\in\mathcal R$ con $\mathcal A(f)<0$, es decir, que la negatividad de $\Omega$ en $(-\xi_*,\xi_*)$ sea **alcanzable con ventanas más cortas que $\log2$ y momento exponencial nulo**. Eso:

1. **No está probado** en el documento (la frase "la masa espectral en frecuencias bajas se obtiene con tests anchos" es exactamente lo que la subclase prohíbe: $\ell<\log2$ fuerza anchura espectral $\gtrsim1/\ell$, y la prueba del Thm 2.2 necesita $\delta\to0$, imposible aquí);
2. **colisiona con GAP-142.A**, que es precisamente la pregunta abierta del signo de $\mu_\varnothing(T)$ en ventanas intermedias (Doc 142 prueba positividad para $2T\le\tfrac1{150}$ y negatividad para $T\ge T_1$ grande; el rango $\ell<\log2$ está en tierra de nadie);
3. el "alternativamente la familia $f_T$ ancha" del propio texto abandona $\mathcal R$ ($P_S\ne0$ allí) y reduce (B) a (A).

**Conclusión:** la afirmación "dos pruebas independientes, ambas completas" es falsa. El Teorema 3.4 queda en pie **únicamente** por la vía (A): espectral-positivo ⟹ $Q_S\ge0$ (Doc 131 Prop. 6.2) contra $Q_S(f_T)<0$ (Doc 142 Teo. 5.1, cuya prueba verifiqué línea a línea: $c_T\le C_\eta e^{-T/8}$, convergencia dominada del arquimediano con el dominador del Lema 2.4(b), convergencia del término de primos a $B_S\|\eta\|_2^2$ — sólida). La "localización arquimediana de la obstrucción" que (B) pretendía es un [DESEO] razonable, no un teorema; nómbrese **GAP-151.C** (¿existe $f$ con ventana $<\log2$, $\hat f(1)=0$ y $\mathcal A(f)<0$? — es un fragmento de GAP-142.A).

---

## 2. El alcance real del colapso de H⁺

### 2.1. Qué dice H⁺ exactamente, y el mundo puro

P48, Conjecture 7.1 (idéntica a Doc 131, Deseo 6.9): *"If $X$ is hermitian, spectral, with datum $a\ge0$ supported on prime powers (Euler product), **standard polar block**, and **archimedean weight of $\zeta$-type**, then $X$ satisfies $H$."*

Las hipótesis incluyen el bloque polar $[0]+[1]$ y el peso arquimediano de tipo $\zeta$. Los objetos puros de Doc 135 ($F_{p,\alpha}\star F_{q,\alpha'}$, pureza bilateral) tienen $c=0$ (sin bloque polar) y $\omega\equiv-2\log(pq)$ constante (Doc 131, Prop. 6.6'): **no satisfacen las hipótesis de H⁺**. P48 mismo llama a su teorema de dos primos "the constructive **sibling** of $H^+$", no una instancia. Por tanto, en el eje que el encargo señalaba: **"H⁺ colapsa" no borra contenido del mundo puro, porque H⁺ nunca dijo nada sobre él.** El teorema de dos primos, el de $n$ primos y toda la familia constructiva quedan intactos e independientes del veredicto del Doc 145. Sin sobre-reclamo aquí.

### 2.2. El sobre-reclamo real del Corolario 4.2, y su reparación

El Cor. 4.2 dice "la clase semilocal de H⁺ es vacía", pero lo probado (Thm 3.4) cubre solo los objetos $X_S^{\mathrm{ar}}$ con $a=\Lambda\cdot\mathbf 1_S$. La clase de H⁺ a $S$ finito es $\{(a,[0]+[1],\omega_\zeta):a\ge0$ soportada en $\{p^m:p\in S\}\}$ con $a$ **arbitraria**. El Teorema B de Doc 142 no se cita para $a$ general, y de hecho su prueba no se aplica tal cual ($G_T$ no es $\ge0$ término a término, y un $a$ gigante en un solo primo podría, en principio, dominar). La laguna es real pero **reparable**, y la reparación es la siguiente, con prueba completa.

**[LEMA R.2.a] (Ramanujan espectral: la espectralidad en la línea acota el dato).** Sea $X=(a,[0]+[1],\omega_\zeta)$ hermitiano, $a\ge0$ soportada en potencias de primos, **espectral-positivo** (Def. 1.2: divisor $Z\subset\{\operatorname{Re}=\tfrac12\}$, densidad polinomial, $\sum_{\rho\in Z}\hat f(\rho)=W_X(f)$ con convergencia absoluta, $\forall f\in C_c^\infty(G)$). Entonces existe $C_X<\infty$ con
$$a(p^m)\;\le\;C_X\,p^{m/2}\qquad\text{para todo }p^m.$$

*Demostración.* Fijo $b\in C_c^\infty(\mathbb R)$ real, $\operatorname{supp}b\subset(-\tfrac14\log2,\tfrac14\log2)$, y defino $h:=-b''+\tfrac14 b$, de modo que $\hat h(z)=(z^2+\tfrac14)\hat b(z)$ es entera con ceros en $z=\pm\tfrac i2$. Elijo $b$ con $h(0)=-b''(0)+\tfrac14b(0)\ne0$ (posible: un bump par con $b''(0)<0$). Para cada $p^m$ sea $F_m(t):=h(t-mL_p)$ y $f_m$ el test correspondiente. Entonces: (i) $\hat f_m(1)=\hat F_m(-\tfrac i2)=e^{mL_p/2}\hat h(-\tfrac i2)=0$ y $\hat f_m(0)=\hat F_m(\tfrac i2)=0$: **bloque polar $=0$ exacto para todo $m$** (la traslación multiplica la transformada por una fase que no mueve los ceros). (ii) El soporte de $F_m$ tiene longitud $<\log2$ y está centrado en $mL_p$: el lado aritmético de $W_X(f_m)$ toca solo $n=p^m$, con contribución $-a(p^m)\,p^{-m/2}\cdot 2h(0)$ (normalización de Doc 142, Obs. 1.3(ii); el espejo $F_m(-mL_p)=0$). (iii) El término arquimediano lineal es $\frac1{2\pi}\int\hat F_m(\xi)\Omega(\xi)\,d\xi$ con $|\hat F_m|=|\hat h|$ Schwartz y $|\Omega(\xi)|\le\log(4+|\xi|)+6$ (Doc 142, Lema 2.4(b)): acotado por $\|\hat h\,\Omega\|_{L^1}$, **uniforme en $m$**. (iv) El lado espectral: $\bigl|\sum_{\rho\in Z}\hat f_m(\rho)\bigr|\le\sum_{\gamma}|\hat h(\gamma)|\le C_k\sum_\gamma(1+|\gamma|)^{-k}<\infty$ por densidad polinomial y decaimiento de Paley–Wiener, **uniforme en $m$** (la fase $e^{i\gamma mL_p}$ es unimodular: aquí es crucial que $Z$ esté EN la línea; con divisor off-line el factor sería $e^{(\beta-1/2)mL_p}$ y la cota se pierde). Despejando en la fórmula explícita: $a(p^m)p^{-m/2}\,2|h(0)|\le$ (iii) + (iv) $=:2|h(0)|\,C_X$. $\square$

**[PROPOSICIÓN R.2] (la vacuidad, reparada para todo $a\ge0$).** No existe ningún objeto hermitiano $X=(a,[0]+[1],\omega_\zeta)$ con $a\ge0$ soportada en potencias de primos de un conjunto **finito** $S$ que sea espectral-positivo.

*Demostración.* Supóngase que existe. Por Prop. 6.2 de Doc 131, $Q_X\ge0$ en toda la clase. Por el Lema R.2.a, $a(p^m)\le C_Xp^{m/2}$. Tomo la familia $f_T$ de Doc 142 Teo. 5.1 con el refuerzo $\eta\ge0$ (permitido: $\eta\in C_c^\infty(0,\tfrac38)$, $\eta\ge0$, $\eta\not\equiv0$; $\eta_2\ge0$ como allí). Entonces $G_T(t)=\int\eta_c(u)\eta_c(u-\tfrac tT)\,du$ con $\eta_c=\eta-c_T\eta_2$ satisface, para todo $t$,
$$G_T(t)\;\ge\;\underbrace{\int\eta\,\eta(\cdot-\tfrac tT)}_{\ge0}\;-\;2c_T\|\eta\|_2\|\eta_2\|_2\;+\;\underbrace{c_T^2\int\eta_2\,\eta_2(\cdot-\tfrac tT)}_{\ge0}\;\ge\;-2c_T\|\eta\|_2\|\eta_2\|_2$$
(las autocorrelaciones de funciones $\ge0$ son $\ge0$ en todo lag). El término de primos de $Q_X(f_T)$, con lags activos $mL_p\le T$, cumple
$$P^{(a)}(f_T)\;=\;\sum_{p\in S}\sum_{mL_p\le T}\frac{a(p^m)}{p^{m/2}}\,2\operatorname{Re}G_T(mL_p)\;\ge\;-4c_T\|\eta\|_2\|\eta_2\|_2\cdot C_X\cdot\#\{(p,m):mL_p\le T\}\;\ge\;-C'_X\,c_T\,T,$$
y $c_T\,T\le C_\eta Te^{-T/8}\to0$. El polar es $0$ exacto, y $\mathcal A(f_T)\to\Omega(0)\|\eta\|_2^2$ como en Doc 142. Luego $\limsup_T Q_X(f_T)\le\Omega(0)\|\eta\|_2^2<0$: contradicción con $Q_X\ge0$. $\square$

Con R.2, el enunciado del Cor. 4.2 pasa de sobre-reclamo a teorema. **Nótese qué lo salvó:** la hipótesis espectral-positiva se usó DOS veces (positividad de la forma Y cota de Ramanujan sobre el dato) — la segunda no estaba en el Doc 145 y es necesaria para $a$ general.

### 2.3. El trilema: la rama (1) se cierra por estipulación, no por teorema

GAP-142.B, tal como Doc 142 §7 lo formuló, pregunta por la espectralidad **en el sentido de Doc 131, Def. 4.1** (espectral-EF: divisor en cualquier sitio, multiplicidades positivas, densidad polinomial). El Doc 145 responde una pregunta distinta (espectral-**positivo**) tras argumentar (Obs. 1.3) que esa es "la única lectura sustantiva de H⁺". Tres observaciones de auditoría:

1. **Lo probado es exactamente:** $X_S^{\mathrm{ar}}$ no es espectral-positivo (Thm 3.4 vía (A); ahora R.2 para todo $a\ge0$). Bajo la lectura adoptada, la rama operante del trilema es la (2) y el razonamiento de Doc 145 es válido.
2. **Lo NO probado:** que $X_S^{\mathrm{ar}}$ no sea espectral-EF. La Obs. 3.5 del propio Doc 145 lo concede ("Espectral-EF: posiblemente"), pero el titular ("el objeto semilocal NO es espectral") y el "Mensaje final" lo suprimen. Bajo la lectura EF de H⁺, la rama (1) — H⁺ refutada por el Teorema B — **sigue lógicamente abierta**: depende de si existe divisor EF, que es precisamente el "teorema de unicidad de divisores" que Doc 142 dejó como falta. La Obs. 1.3 descarta la lectura EF alegando que haría a H⁺ "trivialmente falsa por razones ajenas al semilocal"; pero esa falsedad requiere exhibir un objeto de la clase espectral-EF con divisor off-line — cuyo único candidato es el propio $X_S^{\mathrm{ar}}$. El argumento de lectura es entonces una **estipulación razonable**, no una demostración; el documento debió decirlo.
3. **Dos fricciones internas que la versión final debe corregir:** (i) la Obs. 1.4 afirma "divisor off-line ⟹ $Q_X$ indefinida" citando el Lema 4.3 de Doc 131, pero Doc 131 declara el transporte bloque→forma completa como [PUENTE] salvo divisores finitos o de retícula (§6.1, paréntesis tras Teo. 6.3); para divisores infinitos generales sigue siendo Hipótesis-D-tipo. (ii) La Obs. 2.5/3.5 propone como divisor EF los ceros triviales $s=-2,-4,\dots$ — que tienen **partes reales no acotadas** y por tanto ni siquiera son admisibles bajo la Def. 1.1 (que exige partes reales acotadas). Esto, lejos de dañar el veredicto, es **evidencia a favor** de la no-espectralidad-EF en banda acotada; pero hay que decidirlo, no insinuarlo. Nómbrese **GAP-151.B**: ¿admite $W_{X_S^{\mathrm{ar}}}$ un divisor EF en banda $|\operatorname{Re}\rho-\tfrac12|\le A$ con densidad polinomial? (El contenido superviviente de GAP-142.B literal. La obstrucción esperable: una medida atómica en banda no puede reproducir la densidad continua $\Omega\,d\xi$ más los átomos "a media asta" de los primos truncados — el tipo de unicidad que falta.)

### 2.4. "La única instancia no vacía es $\zeta$ completa": no probado

El Thm 4.1(c) infiere de la vacuidad finita que la clase de H⁺ con peso $\Gamma$ se reduce a $\zeta_{\mathrm{ob}}$. Con R.2 lo que se obtiene es: **todo objeto de la clase debe tener $a$ soportada en infinitos primos.** De ahí a "es $\zeta$" hay un salto: la clase podría contener otros datos $a\ge0$ de soporte infinito con el peso exacto $\Omega$ (la analogía con la clasificación de grado 1 de la clase de Selberg — [DATO: Kaczorowski–Perelli, *On the structure of the Selberg class, I: $0\le d\le1$*, Acta Math. 182 (1999), 207–241] — sugiere que con peso exactamente $\Gamma_{\mathbb R}$ y polo estándar el objeto es esencialmente $\zeta$, pero ese teorema vive en la clase de Selberg con continuación analítica y ecuación funcional, hipótesis que la categoría EF no incluye; **no es enchufable**). El enunciado honesto y probado es:

> **H⁺ no tiene instancias con $S$ finito (R.2). Toda instancia tiene producto de Euler de soporte infinito, y para la instancia $\zeta_{\mathrm{ob}}$, espectral-positivo ⟺ RH (Weil). No existe el escalón semilocal.**

El eslogan "H⁺ colapsa hacia RH" es defendible como resumen de esto; la frase "única instancia" debe degradarse o probarse. Asimismo, bajo la lectura adoptada H⁺ es trivialmente **verdadera** (espectral-positivo ⟹ H es la Prop. 6.2: la "conjetura" tiene la conclusión dentro de la hipótesis), como la Obs. 4.3 ya nota: el resultado neto de los Docs 142+145 es que **H⁺ estaba mal planteada como conjetura** — trivial bajo una lectura, indecisa-y-probablemente-vacía-de-candidatos bajo la otra. Ese es el enunciado de poda correcto.

---

## 3. Doc 148: densidad, separación, y la muerte de la Prop. 2.4

### 3.1. La densidad de Beurling–Landau, re-derivada

Definición [DATO: Beurling; Landau 1967; Seip 2004, cap. 2]: $D^+(\Lambda)=\lim_{r\to\infty}\sup_{x}\frac{\#(\Lambda\cap[x,x+r])}{r}$, $D^-$ con $\inf$. Para $\Lambda_r=\{(\phi_r+2\pi k)/L_r:k\in\mathbb Z\}$: $\#(\Lambda_r\cap[x,x+r])=\frac{rL_r}{2\pi}+O(1)$ **uniforme en $x$**. Para la unión: $\Lambda_p\cap\Lambda_q$ tiene a lo sumo un punto (dos coincidencias darían $L_p/L_q\in\mathbb Q$; Doc 135, Lema 1.7), luego
$$\#(\Lambda\cap[x,x+r])=\frac{r(L_p+L_q)}{2\pi}+O(1)\ \text{uniforme}\implies D^-(\Lambda)=D^+(\Lambda)=\frac{\log(pq)}{2\pi}.$$
Ambas densidades existen y coinciden **aunque $\Lambda$ no sea separada** (las definiciones de Beurling no piden separación). Las condiciones necesarias de Landau (muestreo: $D^-\ge T/\pi$; interpolación: $D^+\le T/\pi$) y la identificación del crítico $2T=\log(pq)$ del Doc 148 son correctas; la dirección de completitud que el doc usa en la región sub-crítica no necesita Landau: la prueba de Jensen del Doc 135 (Teo. 5.4(a)) es rigurosa y verifiqué su contabilidad ($n(r)\ge\frac{L_p+L_q}{\pi}r-C_0$ contra tipo $\frac{2TR}\pi$; correcta). La auto-corrección de la Obs. 1.4 (sub-crítico = completo, super-crítico = núcleo $\infty$-dim) es la asociación correcta. **B.a aguanta.**

### 3.2. La separación y Riesz, re-derivadas

Para $\xi\ne\eta$ y cualquier $T>0$:
$$\|e_\xi-e_\eta\|_{L^2(-T,T)}^2=\int_{-T}^{T}\bigl|1-e^{i(\eta-\xi)t}\bigr|^2dt=4T-\frac{4\sin((\eta-\xi)T)}{\eta-\xi}=4T\Bigl(1-\operatorname{sinc}\bigl((\eta-\xi)T\bigr)\Bigr)\xrightarrow[\eta\to\xi]{}0,$$
con asíntota $\tfrac23T^3(\eta-\xi)^2$. Si $E(\Lambda)$ fuera sucesión de Riesz con cota inferior $A$, el vector de coeficientes $(1,-1)$ soportado en $\{\xi,\eta\}\subset\Lambda$ daría $\|e_\xi-e_\eta\|^2\ge2A$ — imposible si $\Lambda$ contiene pares distintos arbitrariamente próximos. Y los contiene, **para toda elección de fases**: el conjunto de diferencias $\bigl\{\tfrac{\phi_p+2\pi k}{L_p}-\tfrac{\phi_q+2\pi l}{L_q}\bigr\}$ es un trasladado del subgrupo denso $\tfrac{2\pi}{L_p}\mathbb Z+\tfrac{2\pi}{L_q}\mathbb Z$ (denso porque $L_p/L_q\notin\mathbb Q$, Kronecker), luego acumula en $0$ con pares $\xi\ne\eta$ (la igualdad ocurre a lo sumo una vez). Esto vale para **todo $T>0$** — las casi-colisiones están a frecuencia alta, pero la cota de Riesz es uniforme sobre todos los pares, así que la frecuencia es irrelevante. La cita a Young es correcta en espíritu [DATO: R. M. Young, *An Introduction to Nonharmonic Fourier Series*, ed. rev. 2001, cap. 4: separación necesaria para bases/sucesiones de Riesz de exponenciales], y de todos modos el cálculo anterior es autosuficiente. **B.b aguanta.**

### 3.3. La Prop. 2.4: el paso muerto exacto, y el error conceptual

**El paso muerto.** El esbozo toma $F_n(t)=c_n\bigl(e^{i\xi_nt}-e^{i\eta_nt}\bigr)\psi(t)$, $\sigma_n=|\xi_n-\eta_n|\to0$, y normaliza: $\|F_n\|_2^2=c_n^2\int4\sin^2(\sigma_nt/2)|\psi|^2\sim c_n^2\sigma_n^2\int t^2|\psi|^2$, luego $c_n\asymp\sigma_n^{-1}$. Afirma que "los términos cercanos (vecinos en $\Lambda_p,\Lambda_q$ a distancia $\gtrsim2\pi/L_r$) dan $\asymp\sigma_n^2$". **Falso.** En el vecino $\zeta_0=\xi_n+2\pi/L_p\in\Lambda_p$:
$$\hat F_n(\zeta_0)=c_n\Bigl[\hat\psi\bigl(\tfrac{2\pi}{L_p}\bigr)-\hat\psi\bigl(\tfrac{2\pi}{L_p}+\sigma_n\bigr)\Bigr]=-c_n\,\sigma_n\,\hat\psi'\bigl(\tfrac{2\pi}{L_p}\bigr)+O(c_n\sigma_n^2)\;\xrightarrow[n\to\infty]{}\;-\frac{\hat\psi'(2\pi/L_p)}{\bigl(\int t^2|\psi|^2\bigr)^{1/2}}\;\ne\;0$$
para $\psi$ genérica: la amplificación $c_n\asymp\sigma_n^{-1}$ convierte el lóbulo lateral $O(\sigma_n)$ en $\Theta(1)$. Por tanto $Q_X(F_n)\ge2|\hat F_n(\zeta_0)|^2\to\mathrm{const}>0$: **la familia no atestigua $\mu(T)\to0$**. (El propio [GAP] que el doc marcó estaba en la cola de Bessel; el error fatal está antes, en los vecinos inmediatos. Nótese además que el esbozo necesita $\hat\psi'(0)=0$, i.e. $\psi$ par, para su estimación en $\xi_n$ — no declarado; menor al lado de lo anterior.)

**El error conceptual (por qué nunca iba a funcionar).** $\mu(T)$ es la cota inferior de **frame** (operador de análisis): $\sum_{\xi\in\Lambda}|\langle F,e_\xi\rangle|^2$ es **monótona creciente al añadir puntos a $\Lambda$**. Una colisión exacta (vector duplicado) AÑADE un término $\ge0$: mejora el frame y destruye Riesz. Las casi-colisiones degradan las cotas de **síntesis** (Riesz, menor de Gram — que es lo que la Prop. 2.3 calcula) pero no empujan hacia abajo la desigualdad de análisis. La Prop. 2.3 ("$\mu(T)$ está controlado por el menor de Gram $2\times2$"; "estándar para frames") trasplanta una cantidad de síntesis a una cota de análisis: **error de categoría**; no existe tal hecho estándar (el estándar es para sucesiones de Riesz). La Prop. 2.3 cae con la 2.4.

### 3.4. [TEOREMA R.1] El contraejemplo: hay gap de frame en una sub-ventana explícita

**[TEOREMA R.1].** Sean $p<q$ primos, $L_p=\log p$, $L_q=\log q$, fases $\phi_p,\phi_q$ arbitrarias, $\Lambda=\Lambda_p\cup\Lambda_q$, y
$$\theta\;:=\;\operatorname{dist}\bigl(L_q,\;L_p\mathbb Z\bigr)\;=\;\min_{m\ge1}\bigl|\log\tfrac{q}{p^m}\bigr|\;>\;0\qquad(\text{irracionalidad de }\tfrac{L_q}{L_p}).$$
Para toda ventana $2T$ con $\log q<2T\le\log q+\theta$ y todo $f\in C_c^\infty(G)$ con soporte de $F$ en un intervalo de longitud $2T$:
$$Q_X(f,f)\;\ge\;c(p,q,T)\,\|f\|_w^2,\qquad c(p,q,T)\;=\;\min\Bigl(\frac{L_q}{2N},\;(2-\sqrt3)\,L_p\Bigr)\;>\;0,\quad N:=\Bigl\lfloor\frac{2T}{L_p}\Bigr\rfloor+2.$$
En particular $\mu(T)>0$ en $(\log q,\;\log q+\theta\,]$: **la Proposición 2.4 del Doc 148 es falsa.**

*Demostración.* Por invariancia de $|\hat F|$ bajo traslación de la ventana, supongo $\operatorname{supp}F\subset[-T,T]$, $\|F\|_2=1$, y escribo $\varepsilon:=Q_X(f,f)$, $s:=2T-L_q\in(0,L_p]$ (nótese $s\le\theta\le L_p/2<L_p$).

**(0) Periodización con fases.** Para $r\in\{p,q\}$ sea $F_r(t):=F(t)e^{i\phi_rt/L_r}$ (así $\hat F\bigl(\tfrac{\phi_r+2\pi k}{L_r}\bigr)=\hat F_r\bigl(\tfrac{2\pi k}{L_r}\bigr)$, y $|F_r|=|F|$) y $P_r(t):=\sum_{m\in\mathbb Z}F_r(t+mL_r)$ su periodización. Parseval de la serie de Fourier de $P_r$ en $\mathbb R/L_r\mathbb Z$ da, sin ninguna hipótesis de no-solapamiento,
$$\sum_{\xi\in\Lambda_r}|\hat F(\xi)|^2\;=\;L_r\int_{\mathbb R/L_r\mathbb Z}|P_r|^2,\qquad\text{luego}\qquad \varepsilon\;=\;2L_p\!\int|P_p|^2+2L_q\!\int|P_q|^2 .$$

**(1) Lado $q$: la masa se concentra en los bordes.** Como $2T=L_q+s<2L_q$, cada clase módulo $L_q$ tiene a lo sumo dos representantes en $[-T,T]$. Defino los bordes $A:=(-T,-T+s)$, $B:=(T-s,T)$ — nótese la identidad exacta $B=A+L_q$ (pues $-T+L_q=T-s$) — y el centro $M:=[-T+s,\,T-s]$, de longitud $L_q-s>0$. Para c.t.p. $\tau\in M$: $\tau\pm L_q\notin(-T,T)$, así que $P_q(\tau)=F_q(\tau)$ (un solo sumando). Entonces
$$\|F\mathbf 1_M\|_2^2\;=\;\int_{M}|P_q|^2\;\le\;\int_{\mathbb R/L_q\mathbb Z}|P_q|^2\;\le\;\frac{\varepsilon}{2L_q}\;=:\;\varepsilon_1,\qquad \|F\mathbf 1_A\|_2^2+\|F\mathbf 1_B\|_2^2\;\ge\;1-\varepsilon_1 .$$

**(2) Lado $p$: los dos bordes no pueden cancelarse módulo $L_p$.** Descompongo $F=F_A+F_B+F_M$ (restricciones a $A,B,M$) y $P_p=P_p[F_A]+P_p[F_B]+P_p[F_M]$. Como $|A|=|B|=s<L_p$, la proyección $\mathbb R\to\mathbb R/L_p\mathbb Z$ es inyectiva sobre $A$ y sobre $B$: $P_p[F_A]$ y $P_p[F_B]$ son trasplantes **isométricos** a sendos arcos $\bar A,\bar B$ de longitud $s$ del círculo. Como $B=A+L_q$, se tiene $\bar B=\bar A+\delta$ con $\delta\equiv L_q\ (\mathrm{mod}\ L_p)$, y la distancia circular del desplazamiento es $\min(\delta,L_p-\delta)=\theta$. Dos arcos de longitud $s$ desplazados por $\theta\ge s$ son **disyuntos** (módulo medida nula si $s=\theta$). Por soportes disyuntos,
$$\bigl\|P_p[F_A]+P_p[F_B]\bigr\|_{L^2(\mathbb R/L_p\mathbb Z)}^2=\|F_A\|_2^2+\|F_B\|_2^2\;\ge\;1-\varepsilon_1 .$$
Para el centro: $P_p[F_M]$ suma a lo sumo $N=\lfloor 2T/L_p\rfloor+2$ trasladados, luego (Cauchy–Schwarz en la suma finita) $\|P_p[F_M]\|^2\le N\|F_M\|_2^2\le N\varepsilon_1$. Por la desigualdad triangular,
$$\Bigl(\int|P_p|^2\Bigr)^{1/2}\;\ge\;\sqrt{1-\varepsilon_1}-\sqrt{N\varepsilon_1}.$$

**(3) Dicotomía.** Si $\varepsilon>\tfrac{L_q}{2N}$, ya está. Si $\varepsilon\le\tfrac{L_q}{2N}$, entonces $\varepsilon_1\le\tfrac1{4N}\le\tfrac14$ y $N\varepsilon_1\le\tfrac14$, luego $\bigl(\int|P_p|^2\bigr)^{1/2}\ge\sqrt{3}/2-1/2$ y
$$\varepsilon\;\ge\;2L_p\Bigl(\frac{\sqrt3-1}{2}\Bigr)^2\;=\;(2-\sqrt3)\,L_p .$$
En ambos casos $\varepsilon\ge c(p,q,T)$. $\square$

**Comentarios exactos.** (i) Para $p=2,q=3$: $\theta=\min(\log\tfrac32,\log\tfrac43)=\log\tfrac43$, y el teorema da gap de frame en $\log3<2T\le\log4$ — una sub-ventana de longitud $\log\tfrac43$ de la región intermedia $(\log3,\log6)$, con $c=\min(\tfrac{\log3}{8},(2-\sqrt3)\log2)$ en forma cerrada. (ii) La prueba NO usa Baker ni la medida de irracionalidad: usa solo $\theta>0$ y geometría de soportes; las casi-colisiones de alta frecuencia son invisibles para ella porque solo tocan las **fases** de las periodizaciones, nunca los soportes. Esto explica estructuralmente por qué el mecanismo de la Prop. 2.4 no existía. (iii) [GAP de literatura] No conozco un teorema publicado que cubra exactamente "frames de exponenciales sobre $\alpha\mathbb Z\cup\beta\mathbb Z$ inconmensurables en ventanas super-críticas para una progresión y sub-críticas para la unión"; el argumento de doble periodización es elemental y podría ser folclore de muestreo periódico no uniforme (Kohlenberg es el caso conmensurable), pero no puedo señalar la referencia. Se reclama modestia, no prioridad.

**[PUENTE R.1′] (el resto de la región intermedia; estatus: argumento, no teorema).** Para $\theta<s<L_p$ (es decir $\log q+\theta<2T<\log pq$) los arcos $\bar A,\bar B$ se solapan en longitud $s-\theta$, y las dos condiciones de casi-anulación se componen en: (a) $|F_A|$ pequeña en una franja de borde de anchura $\theta$ (parte de $\bar A$ no cubierta por $\bar B$); (b) $F_A(u)\approx e^{i\gamma}F_A(u\mp\theta)$ en el solape (cuasi-invariancia por el desplazamiento $\theta$, con fase fija). Iterando (b) desde la franja (a) en $\lceil s/\theta\rceil$ pasos, cada uno con error $O(\sqrt\varepsilon)$, se obtiene $\|F_A\|\lesssim(s/\theta)\sqrt\varepsilon$, de donde $\mu(T)\gtrsim(\theta/s)^2$ — **frame en toda la región intermedia, con constante que degrada polinomialmente en $s/\theta$** y cae a $0$ exactamente en el crítico $2T=\log pq$ (donde aparece el núcleo $D_pD_qg$), replicando la discontinuidad del caso de una progresión ($\mu=L_q$ constante hasta $2T=L_q$, luego $0$). Falta el bookkeeping de los casos de envoltura del círculo y la acumulación rigurosa de errores. Nómbrese **GAP-151.A**: probar $\mu(T)\asymp_{p,q}\min\bigl(1,(\theta/s)^2\bigr)$-tipo en $\log q<2T<\log pq$. Es exactamente GAP-135.A reabierto, ahora con la dirección de la respuesta invertida respecto del Doc 148 y con la cantidad diofántica correcta identificada ($\theta$ y la órbita de $L_q$ módulo $L_p$ — el aparato natural es el de los tres-distancias/fracciones continuas de $L_q/L_p$ [DATO: teorema de las tres distancias, Sós–Świerczkowski 1957–58], no la medida de irracionalidad).

### 3.5. Consecuencias para los veredictos B.c y B.d

- **B.c muere dos veces:** esbozo roto en un paso identificado (§3.3) y enunciado refutado por el Teorema R.1 en la sub-ventana $(\log q,\log q+\theta]$. La Obs. 5.7 del Doc 135 (optimismo de $\mu(T)>0$) queda **parcialmente vindicada con teorema**, no refutada.
- **B.d muere:** la aritmética NO es epifenómeno. La cantidad $\theta=\min_m|\log(q/p^m)|$ — cuán cerca está $q$ de una potencia de $p$ — gobierna la ventana probada y (vía R.1′) la constante en el resto. Lo que sí sobrevive de la Prop. 3.2 es la parte (a): el **núcleo** (signo, no módulo) es de densidad pura; eso ya era de Doc 135. La Prop. 3.4 (banda efectiva, $\mu_R(T)\gtrsim R^{-2\kappa}$) queda **superada** en la sub-ventana (R.1 es más fuerte: sin banda y sin Baker) y desmotivada en el resto si R.1′ cierra; su premisa retórica ("solo la versión con banda es positiva") es falsa.
- El veredicto global del Doc 148 — "GAP-135.A es esencialmente conocido" — **se invierte**: las partes que eran conocidas (umbrales de densidad, no-Riesz) el Doc 135 ya las tenía o son elementales; la parte que el Doc 148 creyó resolver en negativo ($\mu(T)=0$) es falsa; y lo que queda (GAP-151.A y la determinación exacta de $\mu(T)$) es plausiblemente **matemática nueva modesta y genuina**. El [PUENTE] negativo del §5 del Doc 148 (no escala a $\zeta$: densidad total infinita rompe el marco de frames de intervalo) **sobrevive** — no dependía de la Prop. 2.4 — así que la reapertura de GAP-135.A no lo convierte en eslabón hacia RH.

---

## 4. Los pesos en la identificación Gram ↔ Weil (ataque resuelto a favor del Doc 148)

Se temía que la identificación de la Prop. 1.1 ignorara los pesos $\log p/p^{m/2}$ de la forma de Weil. Verificado contra las normalizaciones exactas: **no hay tal pérdida; la identificación es una identidad.** La contabilidad, paso a paso:

1. **Lado aritmético (Doc 131, Prop. 6.6′; Doc 135 §6):** el objeto puro tiene $W_X(f)=L_p\sum_m c_mf(p^m)+L_q\sum_nc'_nf(q^n)$ con $c_m=2\alpha^m$, $|c_m|=2p^{m/2}$ bajo pureza. Los pesos exponenciales $p^{m/2}$ y los prefactores $L_p$ están ahí.
2. **El cambio unitario:** $F(t)=f(e^t)e^{t/2}$ — el factor $e^{t/2}$ convierte $p^{m/2}f(p^m)$ en $F(mL_p)$ (con la fase $\phi$ absorbida en el torcido): los pesos de Ramanujan se **cancelan exactamente** contra el peso del cambio de variable. Es la misma cancelación que hace $\|f\|_w=\|F\|_{L^2}$.
3. **Poisson (Doc 131, Teo. 6.6):** $\sum_{\rho\in Z(\alpha)}\hat f(\rho)=L\sum_m\alpha^mf(p^m)$ — el prefactor $L$ vive en el lado aritmético; el lado espectral es la suma **sin pesos** sobre la progresión. Aplicado a $g=f\star\tilde f$ bajo pureza: $Q_X(f,f)=2\sum_{\Lambda_p}|\hat F|^2+2\sum_{\Lambda_q}|\hat F|^2$ — que es la fórmula con la que abre el §5 del Doc 135 (línea de su Teo. 3.1). El "2" es multiplicidad ($Z(\alpha)=Z(p/\bar\alpha)$ bajo pureza), no un peso que decae.

Conclusión: el sistema de exponenciales del Doc 148 es genuinamente **no ponderado**, los umbrales no se mueven, y la cota de frame $A$ es exactamente $2\mu(T)$ con la $\mu(T)$ del Doc 135 (Obs. 5.7). Los pesos $\log p/p^{m/2}$ que el ataque recordaba pertenecen a la normalización del régimen **destructivo** (el $P_S$ de Doc 142, dato $a=\Lambda$), que es otro objeto. **B.a certificado también en este frente.**

---

## 5. Consecuencias para los Docs 145/148 y el mapa del programa

### 5.1. Doc 145 — correcciones requeridas (el veredicto central sobrevive)

1. **Thm 2.4 y Def. 2.1:** degradar "equivalentemente" a "en particular" (discreto vs. continuo, §1.1). No fatal.
2. **Thm 3.4:** eliminar "dos pruebas independientes, ambas completas"; la prueba (B) baja a [PUENTE/GAP-151.C] (§1.4). El teorema queda en pie por (A).
3. **Titular y Mensaje final:** "NO es espectral" debe decir "NO es espectral-positivo"; la espectralidad-EF (la pregunta literal de GAP-142.B) sigue abierta como **GAP-151.B** (§2.3), con la observación nueva de que la Def. 1.1 (partes reales acotadas) descalifica el divisor "ceros triviales" de la Obs. 2.5.
4. **Cor. 4.2:** ampliar de $a=\Lambda\mathbf 1_S$ a todo $a\ge0$ usando [LEMA R.2.a] + [PROP. R.2] de esta auditoría (§2.2) — con esto el enunciado "clase semilocal-finita vacía" pasa a ser verdadero tal como está escrito.
5. **Thm 4.1(c):** "única instancia no vacía es $\zeta$" → "toda instancia tiene soporte de Euler infinito; el escalón semilocal no existe; para $\zeta_{\mathrm{ob}}$, espectral-positivo ⟺ RH" (§2.4).
6. **Intactos:** Thm 2.2 (con erratum), Thm 2.4, los supervivientes §5 (Teorema A, transmisión, cono — verificado que ninguno usa representación), y la poda de la ruta de interpolación semilocal, que con R.2 queda **más fuerte** que antes.

### 5.2. Doc 148 — retractaciones requeridas (el veredicto central cae)

1. **Retractar** Prop. 2.3, Prop. 2.4, Prop. 3.2(b), el "veredicto cuantitativo" del §2.3, la fila 3 y 4 de la tabla del §4, y el eslogan "la aritmética es epifenómeno".
2. **Registrar** el Teorema R.1 (gap de frame en $(\log q,\log q+\theta]$, constante en forma cerrada) y GAP-151.A (región restante, ruta de cuasi-invariancia).
3. **Sobreviven:** Prop. 1.1 (identificación exacta, §4), Prop. 1.3+Obs. 1.4 (umbrales), Prop. 2.2 (nunca Riesz), Prop. 3.2(a) (núcleo de densidad pura), Teorema 3.1 (núcleo cualitativo), y el §5 completo (no-escalamiento a $\zeta$).
4. El estado correcto de GAP-135.A: **abierto, parcialmente resuelto en positivo (R.1), con candidata a respuesta completa "frame en toda la región intermedia" (R.1′), y gobernado por la órbita de $L_q$ mód $L_p$ — no por la medida de irracionalidad (contra Doc 135) ni por nada trivial (contra Doc 148).**

### 5.3. Para `06-papers/ERRATA.md` y el mapa

- Erratum E-145.1 (discreto/continuo), E-145.2 (prueba (B) incompleta), E-145.3 (alcance de Cor. 4.2 — reparado por Doc 151 R.2), E-148.1 (Prop. 2.3/2.4 falsas; contraejemplo Doc 151 R.1), E-148.2 (veredicto global invertido).
- GAPs nuevos: **GAP-151.A** (frame en toda la región intermedia; cuasi-invariancia por $\theta$), **GAP-151.B** (espectralidad-EF en banda acotada de $X_S^{\mathrm{ar}}$; unicidad de divisores), **GAP-151.C** (negatividad arquimediana en ventana $<\log2$ con polo muerto; sub-pregunta de GAP-142.A).
- Ninguna de las correcciones toca los teoremas estructurales del arco (Teorema A de ventana corta, identidad de transmisión, teorema de dos primos, pureza local): todos re-verificados en sus puntos de contacto durante esta auditoría.

---

## Mensaje final

**Veredictos.** **A.a AGUANTA** (con erratum discreto/continuo: la equivalencia del Thm 2.2 es para medidas positivas generales; la versión atómica solo hereda la dirección negativa — que es la usada). **A.b AGUANTA** ($\Omega(0)=-\gamma-\tfrac\pi2-3\log2-\log\pi<0$, Gauss verificado). **A.c AGUANTA SOLO POR LA PRUEBA (A)** — la prueba (B) tiene un hueco real (la negatividad de $\mathcal A$ en ventanas $<\log2$ con $\hat f(1)=0$ no está probada y es territorio de GAP-142.A); y lo decidido es espectral-*positivo*: la pregunta literal de GAP-142.B (espectral-EF, Def. 4.1) sigue abierta. **A.d PARCIAL**: vacuidad probada solo para $a=\Lambda\mathbf 1_S$ — **reparada aquí con prueba completa para todo $a\ge0$** (Lema R.2.a "Ramanujan espectral" + Prop. R.2); "única instancia = $\zeta$" no probado; sobre el mundo puro no hay sobre-reclamo (H⁺ exige bloque polar; los puros no lo tienen). **B.a AGUANTA** (identificación Gram↔Weil **exacta**: los pesos $2L_pp^{m/2}$ se cancelan íntegros vía $e^{t/2}$+Poisson; $D^\pm(\Lambda)=\log(pq)/2\pi$ re-derivado). **B.b AGUANTA** (nunca Riesz, para todo $T$ y toda fase; forma cerrada $\|e_\xi-e_\eta\|^2=4T(1-\operatorname{sinc})$). **B.c MUERE** (esbozo roto + contraejemplo con teorema). **B.d MUERE** (la aritmética gobierna: $\theta=\min_m|\log(q/p^m)|$). El veredicto global del Doc 148 ("GAP-135.A esencialmente conocido") **se invierte**; el del Doc 145 (rama (2) del trilema, poda de la interpolación semilocal) **sobrevive con alcance corregido y reforzado**.

**Tres hallazgos.**
1. **[TEOREMA R.1] La Prop. 2.4 del Doc 148 es FALSA:** para $\log q<2T\le\log q+\theta$, con $\theta=\operatorname{dist}(\log q,(\log p)\mathbb Z)>0$, la forma de dos primos tiene gap de frame $\mu(T)\ge\min\bigl(\tfrac{\log q}{2N},(2-\sqrt3)\log p\bigr)>0$ (prueba completa por doble periodización; para $p=2,q=3$: frame en $\log3<2T\le\log4$). El error del Doc 148 era de categoría: las casi-colisiones degradan la síntesis (Riesz), pero el funcional de frame es **monótono al añadir puntos** — los duplicados lo mejoran. GAP-135.A se reabre con la respuesta probable invertida (frame en TODA la región intermedia, vía cuasi-invariancia por $\theta$: GAP-151.A) y con la cantidad diofántica correcta ($\theta$ y las tres-distancias de $L_q/L_p$, no la medida de irracionalidad).
2. **El Doc 145 decide menos de lo que titula pero su núcleo es sólido:** "no espectral" = "no espectral-**positivo**" (la EF-espectralidad de la Def. 4.1 — la pregunta literal de GAP-142.B — queda abierta: GAP-151.B, con la observación nueva de que los ceros triviales ni siquiera son un divisor admisible por partes reales no acotadas); la prueba (B) del Thm 3.4 no es completa ("dos pruebas independientes" es falso); la rama (1) del trilema se cierra por estipulación de lectura, no por teorema. Nada de esto tumba el veredicto: la prueba (A) + Doc 142 Teo. B bastan.
3. **[PROP. R.2] El colapso de H⁺, reparado y reforzado:** la vacuidad de la clase semilocal-finita de H⁺ vale para **todo** dato $a\ge0$ (no solo $a=\Lambda\mathbf 1_S$), vía un lema nuevo con valor propio — **Ramanujan espectral**: espectralidad con divisor en la línea fuerza $a(p^m)\le C\,p^{m/2}$ (la cota de Ramanujan emerge de la espectralidad, no se asume) — más el refuerzo $\eta\ge0$ del Teorema B. Queda como enunciado honesto: H⁺ no tiene instancias de Euler finito; toda instancia requiere soporte infinito; el escalón semilocal no existe; y H⁺ como conjetura estaba mal planteada (trivialmente verdadera bajo la lectura espectral-positiva, indecisa bajo la EF).

---

## Referencias

**Internas (backward-only):** Doc 145; Doc 148; Doc 142 (Teoremas A/B, Lemas 2.1–2.4, §7–§8); Doc 135 (Teo. 3.1, §5: Lema 5.1, Teo. 5.2/5.4, Prop. 5.6, Obs. 5.7, Lema 1.7; §6 normalización del juguete; §7.2 B1–B4); Doc 131 (Def. 4.1, Teo. 4.4, Lema 4.3, Def. 6.1, Prop. 6.2, Teo. 6.3, Teo. 6.6, Prop. 6.6′, Teo. 6.7, Deseo 6.9, §7.1); P48 `06-papers/P48-weil-positivity-finite-primes/main.tex` (Conjecture 7.1, breakpoints B1–B2).

**Literatura [DATO]:**
- S. Bochner, *Lectures on Fourier Integrals*, Annals of Math. Studies 42, Princeton, 1959. (Funcionales de tipo positivo y medidas espectrales.)
- M. Reed, B. Simon, *Methods of Modern Mathematical Physics II*, Academic Press, 1975, Thm IX.9. (Bochner–Schwartz.)
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Lund (1952), 252–265.
- E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers I*, Rend. Mat. Acc. Lincei (9) 11 (2000), 183–233.
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS, 2004, Thm 5.12. (Fórmula explícita, peso arquimediano.)
- E. T. Whittaker, G. N. Watson, *A Course of Modern Analysis*, 4ª ed., CUP, 1927, §12.3. (Digamma de Gauss.)
- H. J. Landau, *Necessary density conditions for sampling and interpolation of certain entire functions*, Acta Math. 117 (1967), 37–52.
- A. Beurling, *Collected Works*, vol. 2, Birkhäuser, 1989. (Balayage; densidad.)
- K. Seip, *Interpolation and Sampling in Spaces of Analytic Functions*, AMS Univ. Lect. Ser. 33, 2004.
- R. M. Young, *An Introduction to Nonharmonic Fourier Series*, ed. revisada, Academic Press, 2001. (Separación necesaria para Riesz; Bessel.)
- R. P. Boas, *Entire Functions*, Academic Press, 1954. (Jensen; completitud por densidad.)
- J. Kaczorowski, A. Perelli, *On the structure of the Selberg class, I: $0\le d\le1$*, Acta Math. 182 (1999), 207–241. (Citada SOLO como analogía no enchufable en §2.4.)
- V. T. Sós, S. Świerczkowski (1957–58): teorema de las tres distancias. (Citado como aparato natural para GAP-151.A.)
- [GAP de literatura] A. Kohlenberg, *Exact interpolation of band-limited functions*, J. Appl. Phys. 24 (1953): muestreo periódico no uniforme, caso conmensurable; no conozco la versión inconmensurable del Teorema R.1 en la literatura — podría ser folclore.

*Fin del Documento 151.*
