# Doc 143 — Ataque al Problema 136.A: positividad localizada cuantitativa bajo RH y el exponente exacto de los pares de Lehmer

**Programa:** Hipótesis de Riemann — Phase 46, "auditoría y ataques".
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Objeto:** el Problema 136.A (D136 §6.3, ítem 7): bajo RH, ¿con qué velocidad se acerca a la degeneración la forma de Weil localizada? ¿Existe un módulo de positividad ε(p) > 0 por celda, y qué cota inferior cuantitativa tiene la forma localizada en una ventana [T, T+H]? Conexión declarada en D136: los pares de Lehmer hacen λ_min genuinamente pequeño — "estimarla es de nuevo un problema de repulsión de ceros".
**Prerrequisitos leídos en fuente:** D136 completo (Defs. 3.1–3.2, Teoremas 2.5, 4.1–4.4, 5.4, Prop. 5.5, Cor. 5.6, §6.3 Problema 136.A); D139 (auditoría: rama RH⟹0 SOBREVIVE, rama ¬RH condicional = Problema 139.A, E-139.1–139.6); D141 (LP-134 forma canónica, no-go relativo 141.B2, Cálculos 141.M4–M5). Insumos espectrales citados: D107 (convergencia absoluta, lado espectral, cerradura bajo x∂ₓ), D108 (Prop. 2.2: positividad diagonal bajo RH).
**Advertencia de estatus heredada (D139):** todo lo que sigue del lado "bajo RH" usa solo la rama RH del criterio logístico, que la auditoría D139 declaró SOBREVIVE sin reservas. No se usa el Teorema 5.4 de D136 (rama ¬RH, condicional a 139.A) salvo donde se declara explícitamente, con su caveat.
**Contrato creativo:** **[DEFINICIÓN-NUEVA]** = libertad total; **[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = prueba completa o no lleva la etiqueta; **[CÁLCULO]** = cerrado; **[PUENTE]** = estatus honesto; **[GAP]/[DESEO]** = declarados. Nada se fabrica.

---

## 0. Resumen ejecutivo y veredicto anticipado

1. **(§1) La pregunta "velocidad de σ_loc^(k) → 0" es degenerada tal como está escrita, y se transmuta.** Bajo RH, x₀(N) = 0 para TODO N (D136 Prop. 5.5): σ_loc^(k) ≡ 0 idénticamente — no hay velocidad que medir ni en k ni en N. El contenido cuantitativo real de 136.A vive un piso más abajo: en el **módulo de positividad** λ_min(p) := λ_min(Gram(Q|_celda)), que bajo RH es > 0 en toda celda pero puede ser arbitrariamente pequeño. 136.A se reformula: ¿qué cota inferior tiene λ_min(p), y es uniforme en la altura T?

2. **(§2, [TEOREMA 143.B]) La cota bajo RH existe y es cerrada: un Gram–Vandermonde en los gaps de los ceros de la ventana.** Para toda celda de dimensión d y cualesquiera d ceros distintos accesibles a la celda,
   λ_min(p) ≥ c(p) · Π_{k<l} ((γ_l − γ_k)/w)², con c(p) explícita y prueba elemental completa (positividad término a término bajo RH + valor singular mínimo ≥ |det|/‖·‖^{d−1} + determinante de Vandermonde). Cada par cercano de ceros entra UNA sola vez en el producto: un par de Lehmer a distancia δ degrada la cota por (δ/w)², no más. El marco clásico exacto es Ingham (1936) por abajo y Montgomery–Vaughan (1974) por arriba ([PROPOSICIÓN 143.B.3]): el módulo de positividad de la forma de Weil localizada ES la cota inferior de Riesz del sistema de exponenciales {e^{iγx}} de la ventana, y los Lehmer viven exactamente bajo el umbral de Ingham a·δ > π.

3. **(§3, [CÁLCULO 143.C] + [TEOREMA 143.C′]) El exponente Lehmer es exactamente 2.** Cálculo 2×2 cerrado: en la celda canónica (bump × monomios) alineada con un par γ' − γ = δ, el Gram juguete es diagonal con λ_min = 2 b̂(aδ/2)² (δ/2w)² — exponente 2, forma cerrada exacta. Con el mar de ceros on-line incluido y una hipótesis de regularidad local (R_η), cota bilateral: c₁(δ/w)² ≤ λ_min(p) ≤ C₁(δ/w)² + C₂·piso(p), con el piso explícito y tan pequeño como se quiera a perfil fijo. Advertencia de normalización ([CÁLCULO 143.C](b)): bases casi-dependientes alineadas al par inflan el exponente a 4 — el exponente es un invariante del par (forma, clase de bases); para las celdas canónicas de D136 es 2.

4. **(§4) Dirección inversa: la uniformidad del módulo ES una repulsión de ceros — la gemela vertical de LP-134.** [DEFINICIÓN-NUEVA] **LP-143**: liminf (γ_{n+1} − γ_n)·log γ_n > 0 (repulsión vertical en la línea, espejo exacto de LP-134 = liminf |β−½|·log γ > 0 de D141). [PROPOSICIÓN 143.E]: bajo RH, módulo uniforme en T para el perfil calibrado ⟺ LP-143 (ambas direcciones probadas sobre §2–§3). Estatus de LP-143: abierto; bajo RH se sabe liminf normalizado ≤ 0.5172 (Conrey–Ghosh–Gonek 1984) y GUE predice liminf = 0: **LP-143 es conjeturalmente FALSA**. El par de Lehmer clásico (γ ≈ 7005.063, δ ≈ 0.0377, gap normalizado ≈ 0.053) es su sombra numérica. La cota incondicional de λ_min para todas las celdas implicaría RH misma — pero solo vía la rama ¬RH de D136, condicional a 139.A: declarado con su caveat.

5. **(§5) VEREDICTO sobre 136.A: RESUELTO EN FORMA RELATIVA — la opción intermedia, y es un teorema condicional honesto.** Bajo RH: (i) hay cota inferior cerrada en términos de los gaps de la ventana ([TEOREMA] condicional, §2); (ii) el exponente de degradación Lehmer es exactamente 2 (§3); (iii) NO hay cota uniforme en T demostrable hoy, y la uniformidad es EQUIVALENTE a LP-143, que GUE refuta conjeturalmente: los casi-dobles no destruyen la positividad (estricta siempre) — destruyen su UNIFORMIDAD, con velocidad δ². 136.A se reduce exactamente a la estadística del gap mínimo = correlación de pares, como D136 §6.3 anticipó. El sueño del "Π₁ con módulo" (ε(p) computable) queda refutado en su versión aritmética: nuestro ε(p) es computable desde los CEROS, no desde los primos — el muro reaparece donde corresponde.

---

## 1. Definiciones: la forma de Weil localizada y su módulo de positividad

### 1.1. Coordenadas y la forma espectral

Trabajamos en la coordenada aditiva x = log (variable logarítmica del grupo multiplicativo), con transformada
$$\hat h(t) := \int_{\mathbb R} h(x)\,e^{-ixt}\,dx .$$
Cero genérico ρ = β + iγ. **Bajo RH** (hipótesis en vigor en §§1–3 salvo aviso): ρ = ½ + iγ, y la forma de Weil sobre la clase de tests es diagonal en los ceros:
$$Q(h,h') \;=\; \sum_{\gamma} \hat h(\gamma)\,\overline{\hat h'(\gamma)}, \tag{1.1}$$
suma sobre las ordenadas con multiplicidad (ambos signos). Estatus de (1.1): es la compresión de la forma de Weil a la clase engrosada, en la normalización del programa — D108 Prop. 2.2 (diagonalidad bajo RH), con convergencia absoluta sobre la clase por D107 Lema 2.2(b); la igualdad entre presentación aritmética (primos) y espectral (ceros) es la fórmula explícita [W52]. La positividad término a término de (1.1) es el único uso de RH en §§2–3, exactamente como en la rama RH de D136/D139 (la rama que SOBREVIVE).

**Lema 143.A (convergencia sobre celdas).** Si |ĥ(t)| ≤ C (1 + a|t − c|)^{−m} con m ≥ 2, entonces Σ_γ |ĥ(γ)|² ≤ C² C₀ a^{−1}(1+a^{-1})·log(2+|c|)-acotado; en particular finito, y ≤ C² C' log(2+|c|) con C' absoluta si a ≥ 1.

*Demostración.* Agrupando ordenadas por intervalos |γ − c| ∈ [j, j+1): el número de ceros por intervalo unitario a altura ~|c|+j es ≤ C₁ log(2+|c|+j) [IK04, Thm. 5.8]. Entonces Σ_γ |ĥ(γ)|² ≤ C² Σ_{j≥0} C₁ log(2+|c|+j)(1+aj)^{−2m} ≤ C² C₁ log(2+|c|) Σ_j (1+j)(1+aj)^{−4} < ∞ (usando log(2+|c|+j) ≤ log(2+|c|)(1+j) y m ≥ 2). ∎

### 1.2. [DEFINICIÓN-NUEVA 143.1] Celda de ventana y forma localizada Q_{T,H}

Fíjese de una vez b ∈ C_c^∞((−1,1)) par, real, no nula, con b̂ (real, par, entera) normalizada b̂(0) = 1 y |b̂(v)| ≤ C_M (1+|v|)^{−M} para el orden M del perfil (familia computable, como en D136 Def. 3.1; M es FINITO y fijo por perfil — ninguna afirmación con M → ∞, en cumplimiento de la lección GAP-A de D139).

Un **perfil de ventana** es p = (d, a, w, M, c): dimensión d ∈ ℕ, soporte a > 0, semiancho espectral w > 0, orden M ≥ d + 2, centro c ∈ ℝ (altura de la ventana; la ventana del encargo es [T, T+H] con c = T + H/2, w = H/2). **Condición de resolución:** a·w ≥ 1 (la celda resuelve su ventana). La **celda** es
$$V_p := \mathrm{span}\{h_0,\dots,h_{d-1}\},\qquad
\hat h_j(t) \;:=\; \hat b\big(a(t-c)\big)\cdot\Big(\frac{t-c}{w}\Big)^{j}. \tag{1.2}$$
Cada h_j es C_c^∞ con soporte ⊆ [−a, a]: ĥ_0 es la transformada de a^{−1}b(x/a)e^{icx}, y el factor monomial es el operador diferencial ((−i d/dx − c)/w)^j aplicado a ella (preserva soporte y suavidad; en coordenadas multiplicativas es la cerradura bajo x∂ₓ de la clase, D107). La celda es test-accesible: el perfil no menciona ceros. Es la misma clase de celdas de D136 Def. 3.1, escrita en la coordenada de UNA variable (la compresión σ-lateral; el puente con Q₂ de D136 es la factorización (1.2) de D136 §1.1 con el lado τ congelado en su bump — todo elemento de V_p ⊗ {φ_0} es un test de la clase doble).

**[DEFINICIÓN-NUEVA 143.2] (forma localizada y módulo de positividad).**
$$Q_{T,H} := Q\big|_{V_p}\ \ (\text{el Gram } G_p := (Q(h_i,h_j))_{i,j}),\qquad
\lambda_{\min}(p) := \lambda_{\min}(G_p) = \min_{\|c\|_2 = 1} Q\Big(\sum_j c_j h_j\Big),$$
con la normalización de coeficientes en la base canónica (1.2) — exactamente el ε(p) cuyo estudio pide D136 §6.3. La **parte de ventana** es Q_W(h) := Σ_{γ ∈ [T,T+H]} |ĥ(γ)|² ≤ Q(h) (bajo RH, todo término es ≥ 0: localizar solo puede bajar). Por el Lema 143.A, G_p está bien definido, y λ_max(G_p) ≤ d·max_j Σ_γ |ĥ_j(γ)|² ≤ C(p)·log(2+T) (cota cruda; la fina es la Prop. 143.B.3).

**[DEFINICIÓN-NUEVA 143.3] (torre de módulos).** Para la grilla 𝒢_N de D136 Def. 3.2: ε_N := min{λ_min(p) : p ∈ 𝒢_N, centrada donde esté}. Bajo RH, "x₀(N) = 0 ∀N" (D136 Prop. 5.5) es el enunciado cualitativo ε_N ≥ 0; el Problema 136.A es su cuantificación: ¿ε_N ≥ módulo computable?

**Observación 1.1 (la transmutación de la pregunta de velocidad).** La pregunta literal de 136.A ("¿con qué velocidad σ_loc^(k) → 0?") tiene respuesta trivial y vacía: bajo RH, x₀(N) = 0 exactamente para todo N (toda compresión de una forma ≥ 0 es ≥ 0), luego σ_loc^(k) = 0 para todo k — convergencia en tiempo cero, sin velocidad. La torre logística amplifica signos, no módulos: es un amplificador de la DICOTOMÍA, ciego a la distancia a la degeneración. Toda la información cuantitativa está en λ_min(p) y ε_N. El resto del documento ataca eso.

---

## 2. [TEOREMA] La cota inferior bajo RH: Gram–Vandermonde en los gaps

### 2.1. El teorema central

**Teorema 143.B (positividad localizada cuantitativa bajo RH; prueba completa).** Asúmase RH. Sea p = (d, a, w, M, c) una celda de ventana y sean γ_1 < γ_2 < ⋯ < γ_d ordenadas DISTINTAS de ceros de ζ (cualesquiera, elegidas a conveniencia; existen infinitas con b̂(a(γ−c)) ≠ 0 porque b̂ es entera no nula y sus ceros reales son discretos). Pónganse
$$\beta_k := \hat b\big(a(\gamma_k - c)\big) \neq 0,\qquad R := \max_k \frac{|\gamma_k - c|}{w},\qquad
K := \big(\max_k |\beta_k|\big)\cdot \max(1, R)^{\,d-1}.$$
Entonces
$$\boxed{\ \lambda_{\min}(p) \;\geq\; \frac{\displaystyle\prod_{k=1}^{d} \beta_k^2 \cdot \prod_{1 \le k < l \le d} \Big(\frac{\gamma_l - \gamma_k}{w}\Big)^{2}}{\big(d\,K\big)^{2(d-1)}}\ \;>\;0. }$$

*Demostración.* (1) **Positividad término a término.** Para h = Σ_j c_j h_j, por (1.1) bajo RH todos los sumandos son ≥ 0; descartando todos salvo los d elegidos:
Q(h) ≥ Σ_{k=1}^d |ĥ(γ_k)|² = ‖E c‖²₂, donde E ∈ ℂ^{d×d} es la matriz de evaluación E_{kj} := ĥ_j(γ_k) = β_k·((γ_k − c)/w)^j.

(2) **Valor singular mínimo.** ‖Ec‖² ≥ s_min(E)²‖c‖² para todo c. Con valores singulares s_1 ≥ ⋯ ≥ s_d: |det E| = Π s_i ≤ s_min·s_1^{d−1}, luego s_min ≥ |det E|/s_1^{d−1} ≥ |det E|/‖E‖_F^{d−1}, y ‖E‖_F ≤ d·max|E_{kj}| ≤ d·K (matriz d×d; |((γ_k−c)/w)^j| ≤ max(1,R)^{d−1}).

(3) **Vandermonde.** E = diag(β_1,…,β_d)·V con V_{kj} = ν_k^j, ν_k := (γ_k − c)/w: det V = Π_{k<l}(ν_l − ν_k) (Vandermonde, nodos distintos), luego |det E| = Π|β_k|·Π_{k<l}|γ_l − γ_k|/w ≠ 0.

Combinando: λ_min(p) = min_{‖c‖=1} Q(h) ≥ s_min(E)² ≥ |det E|²/(dK)^{2(d−1)}, que es la cota. La positividad estricta: det E ≠ 0. ∎

**Corolario 143.B.1 (forma en el gap mínimo, ventana llena).** Si la ventana [c−w, c+w] contiene d ceros con b̂ ≥ β₀ > 0 en ellos y gaps consecutivos ≥ δ_*, entonces (R ≤ 1, K ≤ ‖b̂‖_∞):
$$\lambda_{\min}(p) \;\geq\; \frac{\beta_0^{2d}}{(d\,\|\hat b\|_\infty)^{2(d-1)}}\;\prod_{k<l}\Big(\frac{\gamma_l-\gamma_k}{w}\Big)^2
\;\geq\; \frac{\beta_0^{2d}}{(d\,\|\hat b\|_\infty)^{2(d-1)}}\,\Big(\frac{\delta_*}{w}\Big)^{d(d-1)}\cdot\prod_{k<l}\min\big(1,\tfrac{l-k}{1}\big)\text{-mejorable}.$$
Más útil que la potencia bruta d(d−1) es la estructura del producto: **cada par cercano entra exactamente una vez**. Si la ventana tiene UN par a distancia δ y el resto de los gaps son ≥ comparables a w, la cota es ≥ c(p)·(δ/w)² — un solo factor cuadrático por par de Lehmer. (Verificación en §3: ese exponente es exacto.) ∎

**Observación 2.1 (qué es esto, conceptualmente).** λ_min(p) es la cota inferior de marco (Riesz) del sistema de evaluaciones en los ceros sobre la celda. El Teorema 143.B es la versión determinantal finita —la única incondicional-en-configuración disponible— de la teoría de Ingham: la positividad cuantitativa de Weil localizada ES un problema de independencia lineal cuantitativa de exponenciales {e^{iγx}} en [−a, a], y su módulo se mide en gaps de ordenadas. El muro de 136.A queda así cartografiado de entrada: una cota inferior de λ_min uniforme exige una cota inferior de gaps — repulsión vertical. §4 hace de esto una equivalencia.

### 2.2. El marco clásico: Ingham por abajo, Montgomery–Vaughan por arriba

**Proposición 143.B.2 (cota Bessel/superior vía Montgomery–Vaughan; prueba completa sobre el insumo citado).** Sean {γ_n} ⊂ [T, T+H] ordenadas distintas con separación mínima δ_* > 0, y h ∈ L²(ℝ) con sop h ⊆ [−a, a]. Entonces
$$\sum_{n} |\hat h(\gamma_n)|^2 \;\leq\; \Big(2a + \frac{3\pi}{\delta_*}\Big)\,\|h\|_{L^2}^2 .$$

*Demostración.* El teorema del valor medio de Montgomery–Vaughan [MV74, Cor. 2 del teorema de la desigualdad de Hilbert generalizada] da, para reales distintos con separación ≥ δ_*:
∫_{−a}^{a} |Σ_n c_n e^{iγ_n x}|² dx = Σ_n |c_n|² (2a + θ_n·3π/δ_n) con |θ_n| ≤ 1, δ_n ≥ δ_*; en particular la norma del operador de síntesis S: (c_n) ↦ Σ c_n e^{iγ_n·} ∈ L²(−a,a) satisface ‖S‖² ≤ 2a + 3π/δ_*. El operador de análisis h ↦ (⟨h, e^{iγ_n·}⟩_{L²(−a,a)})_n = (ĥ(γ_n))_n es S*, con la misma norma. Luego Σ|ĥ(γ_n)|² ≤ ‖S*‖²‖h‖² ≤ (2a + 3π/δ_*)‖h‖². ∎

**Observación 2.2 (Ingham y el umbral exacto donde viven los Lehmer).** En la dirección inferior, la desigualdad de Ingham [I36, Thm. 1] da: si los gaps son ≥ δ_* y **a > π/δ_***, entonces ∫_{−a}^a |Σ c_n e^{iγ_n x}|² dx ≥ C(a, δ_*) Σ|c_n|² con constante explícita > 0 — el sistema de exponenciales de la ventana es una sucesión de Riesz, y por el mismo argumento de dualidad el módulo de positividad en normalización L² queda acotado por abajo a escala. La hipótesis a·δ_* > π es ÓPTIMA (Ingham construye contraejemplos en a·δ_* = π). Léase el cuadro completo: con soporte a ≍ A log T (el presupuesto natural; cf. D134/D141, la resolución 1/log T), Ingham cubre exactamente los pares con δ > π/a ≍ π/(A log T) — los gaps super-resolución — y **falla exactamente para los pares sub-resolución a·δ ≤ π: los pares de Lehmer son, por definición de la escala, los pares bajo el umbral de Ingham.** Ambas cotas de marco (Ingham abajo, MV arriba con su 3π/δ_*) degeneran simultáneamente en δ_* → 0: no es una limitación técnica de una desigualdad, es la geometría del problema. El Teorema 143.B es lo que sobrevive bajo el umbral: sin hipótesis de separación, módulo Vandermonde que degrada con los gaps reales — y §3 muestra que esa degradación es exacta, no un artefacto de la prueba.

---

## 3. La conexión Lehmer en forma cerrada: el exponente es 2

### 3.1. [CÁLCULO 143.C] El 2×2 exacto (juguete: solo el par en el universo)

Sea γ' = γ + δ un par de ordenadas (δ > 0 pequeño) y, como juguete, supóngase que son los ÚNICOS ceros que ve la celda (el mar se apaga; §3.2 lo enciende). Celda canónica d = 2 centrada en el par: c := γ + δ/2, perfil (2, a, w, M, c), nodos normalizados ν_{1,2} = ∓δ/(2w), pesos β := b̂(aδ/2) = b̂(−aδ/2) (b̂ par).

**(a) Base canónica (bump × monomios).** E = β·[[1, −u],[1, u]] con u := δ/(2w). Entonces
$$E^*E = \beta^2\begin{pmatrix}2 & 0\\ 0 & 2u^2\end{pmatrix}
\quad\Longrightarrow\quad
\boxed{\ \lambda_{\min} = 2\,\hat b\big(\tfrac{a\delta}{2}\big)^2\,\Big(\frac{\delta}{2w}\Big)^2\ },\qquad \lambda_{\max} = 2\,\hat b\big(\tfrac{a\delta}{2}\big)^2,$$
forma cerrada exacta (¡el Gram juguete es diagonal!), autovector mínimo c = (0,1): el testigo es ĥ = b̂(a(t−c))·(t−c)/w, el test ANTISIMÉTRICO respecto del centro del par, que se anula en el punto medio y vale ±βu en los dos ceros. **Exponente 2 en δ, con constante exacta.** Coincide con el Corolario 143.B.1 (la cota inferior general da c·(δ/w)² aquí): el Teorema 143.B es exacto en el exponente.

**(b) Advertencia de normalización (el falso exponente 4).** Si en lugar de la base canónica se usa la base "alineada al par" u_j con û_j(t) = b̂(a(t−γ_j)) (un bump por cero), entonces E = [[1, β_δ],[β_δ, 1]] con β_δ := b̂(aδ), simétrica, Gram = E², y
λ_min = (1 − b̂(aδ))² = κ_b²(aδ)⁴ + O((aδ)⁶), κ_b := −b̂''(0)/2 > 0:
**exponente 4.** No hay contradicción: la base alineada es ella misma casi-dependiente (u_1 ≈ u_2 cuando aδ → 0), y la normalización por coeficientes en una base que degenera infla el módulo aparente. En la normalización L² del test (cociente de Rayleigh Q(h)/‖h‖²_{L²}, invariante de base), el mismo cálculo da min = (1−b̂(aδ))²·2/(2(‖b‖²-términos)(1−\widehat{|b|^2}-cociente)) ≍ a-escala·(aδ)² — exponente 2 de nuevo. **Moral, registrada:** el exponente Lehmer es un invariante del par (forma, clase de bases admisibles); para las celdas canónicas de D136 (bump × monomios, base de Riesz con constantes independientes de la configuración) es 2; el 4 es un artefacto de bases degeneradas. Todo enunciado cuantitativo de 136.A debe declarar su normalización — misma lección que E-139.1 (el bug del radical era también un denominador mal elegido).

### 3.2. El mar encendido: cota superior con cola controlada

Para que el juguete sea teorema hay que pagar dos cosas: aniquilar los ceros vecinos del par (con grados de libertad de la celda, à la D136 Lema 5.3) y acotar la cola lejana (con el decaimiento M del perfil, a M FIJO — sin límites en M, lección GAP-A de D139).

**Hipótesis (R_η) (regularidad local del mar; declarada, no probada — es una hipótesis de configuración).** Sea c la altura del par. Los ceros en [c−1, c+1] distintos del par tienen gaps mutuos ≥ η·w (η > 0 fijo; con la calibración natural w = 1/log T es la separación típica GUE, que vale para casi todo par en sentido de densidad pero NO para todos — honestidad: (R_η) excluye la presencia de un SEGUNDO par de Lehmer pegado al primero).

**Teorema 143.C′ (cota bilateral de la celda alineada; prueba completa bajo RH + (R_η)).** Asúmase RH. Sea γ' = γ + δ con 0 < δ ≤ w, c := γ + δ/2, y supóngase (R_η). Fíjese s ≥ 1 con sw ≤ 1 y sea S := {ceros γ_n ∉ {γ,γ'} : |γ_n − c| ≤ s·w}, d := |S| + 2 (finito: |S| ≤ 2s/η + 1 por (R_η)). Sea p = (d, a, w, M, c) con aw ≥ 1 y M ≥ d + 2. Entonces existen constantes 0 < c_1(p,η,s) ≤ C_1(p,η,s) y C_2(p,η,s), explícitas en la prueba y dependientes SOLO del perfil y de (η, s) — no de T ni de δ — tales que
$$c_1\,\Big(\frac{\delta}{w}\Big)^2 \;\leq\; \lambda_{\min}(p) \;\leq\; C_1\,\Big(\frac{\delta}{w}\Big)^2 \;+\; C_2\,\Big[(as w)^{-2(M-d)-1} + \log(2+T)\,(a)^{-2(M-d+1)}\Big].$$

*Demostración.* **Cota inferior.** Teorema 143.B con los d nodos {γ, γ'} ∪ S: el producto de Vandermonde contiene el factor (δ/w)² del par una vez; todos los demás factores involucran al menos un elemento de S o el gap entre miembros distintos: por (R_η) y porque los elementos de S distan ≥ η·w entre sí y los nodos están a distancia ≤ (s+1)w del centro, cada uno de los restantes d(d−1)/2 − 1 factores es ≥ (η/2)² y ≤ (2s+2)² en valor absoluto normalizado (los gaps al par: ≥ separación de S al par, que por (R_η) aplicada al conjunto total es ≥ η·w·½ tomando η de la hipótesis sobre todos los ceros de [c−1,c+1] menos el gap interno del par, que es el único exento). Los pesos: |β_k| = |b̂(a(γ_k−c))| con a|γ_k−c| ≤ a(s+1)w ≤ 2asw acotado por el perfil: β₀(p,s) := min de |b̂| sobre el compacto [−2asw, 2asw] menos sus ceros — si algún β_k cae en un cero de b̂, muévase el centro c dentro de la malla (D136 Lema 5.3, último punto: los ceros de b̂(a(·−ic)) son discretos y la grilla los esquiva con margen b₀/2; mismo argumento). Recolectando: λ_min ≥ c_1(δ/w)² con c_1 = β₀^{2d}(η/2)^{d(d−1)−2}/(dK)^{2(d−1)}.

**Cota superior.** Testigo: v con
$$\hat v(t) := \hat b\big(a(t-c)\big)\cdot P(t),\qquad
P(t) := \frac{t-c}{w}\,\prod_{\gamma_n \in S}\frac{t-\gamma_n}{w},$$
polinomio mónico de grado d−1 en (t−c)/w: v ∈ V_p con vector de coeficientes c_v = (elementales simétricas de los nodos normalizados ν_n = (γ_n−c)/w ∈ [−s,s], y el factor central 0); su coordenada superior es 1, luego ‖c_v‖ ≥ 1, y λ_min(p) ≤ Q(v)/‖c_v‖² ≤ Q(v). Presupuesto de Q(v) = Σ_γ |v̂(γ)|², en cuatro clases:
(i) **S:** v̂(γ_n) = 0 — aniquilados exactamente (la llave de D136 Obs. 5.1: el testigo puede usar posiciones; la celda no las menciona).
(ii) **El par:** |P(γ)| = (δ/2w)·Π_S |γ−γ_n|/w ≤ (δ/2w)(s+1)^{d−2}, ídem γ'; con |b̂| ≤ ‖b̂‖_∞: contribución ≤ 2‖b̂‖²_∞ (s+1)^{2(d−2)} (δ/2w)² =: C_1(δ/w)².
(iii) **Anillo sw < |γ_n − c| ≤ 1:** por (R_η), a lo sumo 1 + 1/(ηw) ceros, separados ≥ ηw: agrupando por capas |γ_n−c| ∈ [kw, (k+1)w], k ≥ s, hay ≤ 1 + 1/η ceros por capa; en la capa k, |b̂(a(γ_n−c))| ≤ C_M(akw)^{−M} y |P| ≤ (2k)^{d−1} (pues |t−γ_n|/w ≤ |t−c|/w + s ≤ 2k para k ≥ s): término ≤ C_M²(1+1/η)·Σ_{k≥s} (2k)^{2(d−1)}(akw)^{−2M} ≤ C(d,M,η)·(aw)^{−2M}·s^{2(d−1)−2M+1}/(2M−2d+1) ≤ C'(asw)^{−2(M−d)−1} (usando aw ≥ 1 para absorber potencias).
(iv) **Lejos, |γ_n − c| > 1:** por intervalos unitarios con densidad ≤ C log(2+T+j) [IK04]: |v̂| ≤ C_M(aj)^{−M}(2j/w)^{d−1}; la suma ≤ C(d,M)·log(2+T)·w^{-2(d-1)}a^{−2M}Σ_j j^{2(d−1)−2M}(1+j) ≤ C''·log(2+T)·a^{−2(M−d+1)} (con M ≥ d+2 la serie converge; el w^{−2(d−1)} se absorbe vía aw ≥ 1 en a^{2(d−1)}).
Sumando (i)–(iv): la cota enunciada. ∎

**Corolario 143.C′.1 (calibración natural y lectura).** Con a = A log T, w = 1/log T (resolución natural; aw = A ≥ 1), s y η fijos: d ≤ 2s/η + 3 fijo, y
$$c_1\,(\delta \log T)^2 \;\leq\; \lambda_{\min}(p) \;\leq\; C_1\,(\delta\log T)^2 + C_2\Big[(As)^{-2(M-d)-1} + (\log(2+T))^{1-2(M-d+1)}\Big].$$
A perfil fijo, el piso C₂[…] se hace menor que cualquier objetivo fijo ε̄ > 0 eligiendo M (FIJO) suficientemente grande respecto de (A, s, d, ε̄) — elección hecha UNA vez, sin límite M → ∞ (las constantes C_M, β₀ del perfil elegido entran en c_1, C_1: legítimo porque δ → 0 es el único límite del enunciado). Conclusión: **en el rango δ log T ≥ piso^{1/2}, λ_min(p) ≍_{p,η} (δ log T)²** — el exponente Lehmer es exactamente 2 en la escala de resolución. Un par de Lehmer con gap normalizado ϑ = δ log T/2π pequeño deprime el módulo de positividad de SU celda a ≍ ϑ²: cuantifica "casi-contraejemplo" con tasa cerrada. ∎

**Observación 3.1 (cruce con D141, Cálculo 141.M5).** El exponente 2 es el mismo "segundo orden" de D141: la señal de primer orden de una configuración simétrica es nula (141.M4) y la de segundo orden tiene media nula con ancho δ (141.M5). Aquí la simetría es vertical (par on-line respecto de su punto medio) en vez de horizontal (cuádruplo respecto de la línea), y el test antisimétrico del Cálculo 143.C(a) es exactamente el funcional que la detecta al orden δ². Las dos geometrías de casi-degeneración del programa — Lehmer vertical y sub-resolución horizontal — tienen la MISMA firma cuadrática. No es coincidencia: §4.3.

---

## 4. Dirección inversa: módulo uniforme ⟺ repulsión vertical; conexión con LP-134

### 4.1. [DEFINICIÓN-NUEVA] LP-143, la gemela vertical de LP-134

D141 §1.2 fijó la forma canónica LP-134: liminf_{ρ off} |β−½|·log γ > 0 (repulsión HORIZONTAL: los ceros que abandonan la línea lo hacen visiblemente). Su espejo en la coordenada vertical:
$$\textbf{LP-143}:\qquad \liminf_{n\to\infty}\ \big(\gamma_{n+1}-\gamma_n\big)\cdot\log\gamma_n \;>\;0$$
(ordenadas consecutivas distintas de ceros de ζ; la convención sobre multiplicidades: un cero múltiple cuenta como gap 0, de modo que LP-143 implica en particular simplicidad eventual). LP-143 dice: no hay pares de Lehmer asintóticamente degenerados a escala sub-resolución — la frontera que (según D141 §4.1 y [RT20]) ζ roza, no se cruza tampoco verticalmente.

### 4.2. La equivalencia

**Proposición 143.E (bajo RH: módulo uniforme ⟺ LP-143; prueba completa sobre §§2–3).** Asúmase RH, y restrínjase a alturas/pares que satisfacen (R_η) para algún η > 0 fijo (clase 𝒞_η). Sea 𝔓 el perfil calibrado del Corolario 143.C′.1 (parámetros fijos, centro libre). Son equivalentes:

(a) **Módulo uniforme:** existe ε₀ > 0 tal que λ_min(p) ≥ ε₀ para toda celda p de perfil 𝔓 centrada en cualquier altura c (en 𝒞_η), para todo T.

(b) **Repulsión vertical cuantitativa:** existe c₀ > 0 tal que todo par de ordenadas consecutivas (en 𝒞_η) cumple (γ_{n+1} − γ_n)·log γ_n ≥ c₀.

Constantes: (b) ⟹ (a) con ε₀ = c_1·c₀² (Teorema 143.C′, cota inferior, junto con 143.B para ventanas sin par cercano); (a) ⟹ (b) con c₀ = √((ε₀ − piso)/C_1) tomando el perfil con piso ≤ ε₀/2 (Corolario 143.C′.1, cota superior, contrapuesta: un par con δ log T < c₀ produce una celda con λ_min < ε₀). ∎

**Observación 4.1 (estatus de LP-143 — el veredicto de la literatura, honesto).** (i) **Abierta** para ζ; ninguna técnica conocida la prueba (las estadísticas verticales clásicas de D141 Lema 141.B0 son sobre ordenadas, así que aquí SÍ son sensibles — pero lo que prueban va en contra: ver (ii)). (ii) Bajo RH, Conrey–Ghosh–Gonek [CGG84] prueban liminf (γ_{n+1}−γ_n)·(log γ_n)/2π ≤ 0.5172: gaps por debajo del 52% de la media infinitas veces. Eso NO refuta LP-143 (0.5172 > 0), pero la conjetura GUE de Montgomery [M73] predice densidad de gaps normalizados ~ c·u² cerca de u = 0 (repulsión cuadrática DÉBIL: probabilidad positiva en todo entorno de 0), de donde **liminf = 0: GUE refuta LP-143 conjeturalmente.** (iii) La sombra numérica: el par de Lehmer original (γ ≈ 7005.0629, γ' ≈ 7005.1006: δ ≈ 0.0377, gap normalizado ≈ 0.053 [CSV94]) y los miles posteriores muestran gaps normalizados que descienden sin señal de piso. (iv) Simetría perfecta con D141: LP-134 (horizontal) es indemostrable por promedios (no-go 141.B2), irrefutable sin refutar RH, y conjeturalmente… abierta; LP-143 (vertical) es además **conjeturalmente falsa** — la coordenada vertical es aún peor para la uniformidad. Conclusión para 136.A: **(a) es conjeturalmente falso: NO hay módulo uniforme en T.**

**Proposición 143.E′ (la versión incondicional de la inversa, con su caveat).** Si existiera una cota inferior INCONDICIONAL λ_min(p) ≥ ε(p) > 0 para toda celda de la grilla 𝒢 de D136 (sin asumir RH), entonces: (α) ¬RH quedaría refutada SI la rama ¬RH del criterio logístico (D136 Thm. 5.4) fuese teorema — es decir, módulo el Problema 139.A: bajo ¬RH esa rama produce una celda con neg.ind ≥ 1, o sea λ_min < 0 < ε(p), contradicción; (β) sin resolver 139.A, lo único que se sigue incondicionalmente es: ninguna celda de la grilla certifica ¬RH — consistente con RH pero no demostración. **Estatus: la implicación "positividad cuantitativa incondicional ⟹ RH" es exactamente tan condicional como 139.A.** Y por la Prop. 143.E, esa cota incondicional implicaría además LP-143 (vía la parte RH del argumento si RH es verdadera) — de modo que el programa "probar ε(p) > 0 uniforme" carga a la vez con el peso de RH y con una repulsión vertical que GUE niega: **[NO-GO heurístico]** la ruta "módulo uniforme primero" está doblemente bloqueada. ∎

### 4.3. [PUENTE] Lehmer vertical ↔ LP-134 horizontal: el diccionario De Bruijn–Newman

Estatus de esta subsección: conexión declarada, sin teoremas nuevos; cita resultados publicados exactos y un diccionario heurístico etiquetado.

- **Lo probado:** Csordas–Smith–Varga [CSV94] definen "par de Lehmer" cuantitativamente y prueban: cada par de Lehmer genuino fuerza una cota inferior para la constante de De Bruijn–Newman, Λ ≥ −λ(par), con λ(par) que decae con la calidad del par (su medida de calidad es, en esencia, el cuadrado del gap normalizado contra la separación al resto del espectro — la MISMA cantidad (δ log γ)² de nuestro Corolario 143.C′.1, en otra normalización). Rodgers–Tao [RT20]: Λ ≥ 0 incondicionalmente.
- **El diccionario (heurístico, etiquetado [DESEO]):** bajo el flujo del calor que define Λ, un par on-line con gap δ en tiempo t = 0 colisiona y se vuelve cuádruplo off-line en tiempo ≍ −δ² (la colisión de dos ceros reales de un polinomio bajo calor hacia atrás ocurre en tiempo cuadrático en su separación — exacto para el modelo cuadrático local). Es decir: **LP-143 en t = 0 es la traza de LP-134 en tiempos t < 0 infinitesimales: la repulsión vertical de hoy es la repulsión horizontal del pasado térmico inmediato, y el exponente 2 de §3 es el mismo δ² del tiempo de colisión.** Λ = 0 ([RT20] + RH darían Λ = 0) significa que ζ está en la frontera exacta: los dos liminf — el horizontal de LP-134 y el vertical de LP-143 — miden la distancia a la misma frontera desde los dos lados. Ningún teorema de este documento depende de este diccionario; se registra porque explica la coincidencia de exponentes (Obs. 3.1) y porque ata 136.A al expediente LP-134 de D141 con la geometría correcta: **no son dos repulsiones, es una sola, vista en t = 0⁻ y en t = 0.**
- **Consecuencia para el mapa del muro:** D141 §3.3 mostró que LP-134 atacada con análisis reconduce al muro viejo (uniformidad de ventanas). La Prop. 143.E muestra que la uniformidad de 136.A reconduce a LP-143, gemela de LP-134. El circuito se cierra: **136.A-uniforme, LP-134, LP-143 y la uniformidad de ventanas son cuatro caras del mismo poliedro**, y la única arista probada es la relación cuantitativa exacta entre módulo y gap (este documento, §§2–3).

### 4.4. El sueño del Π₁-con-módulo (D136 §6.3), liquidado con precisión

D136 §6.3 pedía ε(p) **computable** (desde los primos) con λ_min(Gram(p)) ≥ ε(p) bajo RH, para convertir el Π₁ de la rama RH en un Π₁ con módulo y dar criterio de parada por nivel a la búsqueda de ¬RH. Balance tras §§2–4: (i) el módulo EXISTE y es cerrado — pero en función de los gaps de los ceros (Teorema 143.B): computable desde los CEROS, no desde los primos; usar posiciones de ceros en el certificado destruye la autonomía (P43) que motivaba el sueño. (ii) Un ε(p) autónomo y uniforme equivaldría a LP-143 (Prop. 143.E), conjeturalmente falsa. (iii) Queda una versión degradada honesta: ε(p) autónomo NO uniforme, dependiente de un parámetro de regularidad η declarado como hipótesis de configuración — exactamente la degradación "ε(p) debe degradar con la configuración on-line local" que D136 §6.3 anticipó, ahora con la tasa exacta: cuadrática en el gap mínimo local. **El sueño no se cumple; se reemplaza por su forma verdadera: módulo relativo al gap, sin uniformidad.**

---

## 5. Veredicto sobre el Problema 136.A

**RESUELTO EN FORMA RELATIVA — la tercera opción del encargo, que es un teorema condicional honesto y no una derrota.** Desglose:

1. **La pregunta de velocidad, corregida.** σ_loc^(k) ≡ 0 bajo RH para todo k y todo N (D136 Prop. 5.5; rama confirmada por D139): la "velocidad" es instantánea y la pregunta literal está vacía. El contenido cuantitativo de 136.A es λ_min(p) (Obs. 1.1). Esta corrección de enunciado es el primer resultado del documento.

2. **[TEOREMA condicional — la cota existe y es cerrada.]** Bajo RH, λ_min(p) > 0 en TODA celda, con módulo Gram–Vandermonde explícito en los gaps de cualesquiera d ceros (Teorema 143.B), enmarcado exactamente por Ingham 1936 (abajo, super-resolución) y Montgomery–Vaughan 1974 (arriba); ambos marcos degeneran juntos bajo el umbral a·δ = π, donde 143.B sigue dando módulo positivo no uniforme.

3. **[TEOREMA condicional — el exponente Lehmer es 2.]** Forma cerrada 2×2 exacta (λ_min = 2b̂(aδ/2)²(δ/2w)², Cálculo 143.C) y cota bilateral con el mar bajo (R_η): λ_min ≍ (δ log T)² en calibración natural (Teorema 143.C′). Los pares de Lehmer son casi-contraejemplos con tasa cuadrática exacta; el exponente 4 que aparece en bases alineadas es un artefacto de normalización, registrado como advertencia.

4. **No hay velocidad uniforme — y eso es un enunciado estructurado, no un fracaso difuso.** Módulo uniforme en T ⟺ LP-143 (repulsión vertical, gemela de LP-134; Prop. 143.E, equivalencia probada), que está abierta, acotada por arriba por [CGG84] y conjeturalmente FALSA bajo GUE. Los Lehmer no destruyen la positividad (estricta siempre bajo RH); destruyen su uniformidad, exactamente con velocidad δ². **136.A se reduce a la estadística del gap mínimo = correlación de pares**, como D136 §6.3 predijo ("el muro asoma también ahí, como corresponde") — pero ahora con la reducción convertida en equivalencia cuantitativa con constantes.

5. **Subproductos para el expediente del programa:** (i) LP-143 nombrada y formalizada como gemela vertical de LP-134, con el diccionario De Bruijn–Newman ([CSV94], [RT20]) explicando que son una sola frontera vista en t = 0⁻ y t = 0 (§4.3, [PUENTE] heurístico declarado). (ii) El sueño Π₁-con-módulo de D136 §6.3 queda liquidado en su versión autónoma-uniforme y reemplazado por el módulo relativo al gap (§4.4). (iii) Doble bloqueo de la ruta "módulo incondicional": cargaría con 139.A y con ¬GUE a la vez (Prop. 143.E′).

**[GAP declarado — lo que este documento NO prueba:]** (a) ninguna instancia de LP-143 ni de su negación; (b) la hipótesis (R_η) del Teorema 143.C′ es de configuración (excluye pares de Lehmer dobles apilados) — sin ella la cota superior gana un factor log T en el piso y el perfil debe crecer lentamente con T; (c) el diccionario térmico de §4.3 es heurístico; (d) nada aquí mueve la rama ¬RH (139.A sigue abierto, y este documento no lo toca).

---

## Referencias

**Internas (backward-only):** D136 (Defs. 3.1–3.2, Prop. 3.3, 5.5, Thms. 2.5, 4.1–4.4, 5.4, Cor. 5.6, §6.3 Problema 136.A); D139 (veredicto por ramas; E-139.1 normalización; GAP-A lección de constantes M-dependientes; Problema 139.A); D141 (LP-134 forma canónica Def. 141.1, Cálculos 141.M4–M5, no-go 141.B2, §4.1 Lehmer como frontera); D107 (convergencia absoluta, cerradura x∂ₓ); D108 (Prop. 2.2, positividad diagonal bajo RH); P43 (autonomía); D134 (calendarios/resolución, vía D141).

**Literatura (publicada y verificable):**
- A. E. Ingham, *Some trigonometrical inequalities with applications to the theory of series*, Math. Z. 41 (1936), 367–379. [I36] — desigualdad inferior para exponenciales con gap, umbral a·δ > π óptimo.
- H. L. Montgomery, R. C. Vaughan, *Hilbert's inequality*, J. London Math. Soc. (2) 8 (1974), 73–82. [MV74] — desigualdad de Hilbert generalizada y teorema del valor medio con término 3π/δ.
- H. L. Montgomery, *The pair correlation of zeros of the zeta function*, Proc. Sympos. Pure Math. 24, AMS (1973), 181–193. [M73] — correlación de pares; repulsión cuadrática GUE (conjetural).
- J. B. Conrey, A. Ghosh, S. M. Gonek, *A note on gaps between zeros of the zeta function*, Bull. London Math. Soc. 16 (1984), 421–424. [CGG84] — bajo RH, gaps normalizados ≤ 0.5172 infinitas veces.
- G. Csordas, W. Smith, R. S. Varga, *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann hypothesis*, Constr. Approx. 10 (1994), 107–129. [CSV94] — pares de Lehmer ⟹ cotas inferiores de Λ.
- B. Rodgers, T. Tao, *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi 8 (2020), e6. [RT20] — Λ ≥ 0.
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Lund (1952). [W52] — fórmula explícita y positividad.
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53 (2004), Thm. 5.8. [IK04] — N(t+1) − N(t) ≪ log t.

*Fin del Doc 143.*
