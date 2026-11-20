# ROUND 032 B — Puerta de selección: (PBP_T) como problema de medidas representantes del origen en el polidisco infinito

Objeto: estado sin peso de (PBP_T) (ROUND_030_B, 031_A, 031_B). Propuesta: levantar μ al toro 𝕋^∞ por la recta
de Kronecker ι(τ) = (p^{−iτ})_p y leer Φ(log n) = 0 (n ≥ 2) como «ν = ι_*μ representa al origen para el álgebra
del polidisco». Sólo cotejo, corrección y selección; ninguna derivación nueva.

## 1. Cotejo (fuentes abiertas, no por coincidencia de palabras)

**1.1 CA_E_001 (fase 193) §§1–2, Lema 1 y Teorema 2 (PROVED).** Misma operación sobre el objeto con el peso:
φ(q) = 𝖡(log q) en G = ℚ_{>0}^× es PD ⟺ objetivo (Lema 0); la medida de Bochner de φ en Ĝ ≅ ∏_p S¹ es ι_*ν,
Radon, concentrada en la recta de Kronecker (Lema 1, σ-compacidad de ι(ℝ)); toda traslación de la recta es
Haar-nula. Concluye: reformulación exacta (REF-D, clase lem:shape-restate), «válida para todo peine», sin paso de signo.
Elimina factorizaciones producto/Schur. No cerró porque la recta es Haar-nula: nada de la estructura de toro
(independencia de lugares) llega a una medida de la recta.

**1.2 CA_C_002 §3, Prop. 2(a)–(d) (PROVED).** Misma herramienta sobre la forma con peso: sᵀ𝔸_M s =
∫ m |P_s∘ι|² dμ_line − ∫(Σ_pδ_p)|P_s|² dθ − (μ_line∘ι^{−1} − Haar)(…). «Local = Haar en 𝕋^S; acople global = recta
de Kronecker». Concluye identidad sin signo; el término Near es el defecto de equidistribución de la recta.

**1.3 CA_H_002 §3 (Teor. 3.1–3.2, Prop. 3.3–3.4, Cor. 3.5).** Extiende 1.2 al solenoide completo: Div = integral
de Haar, Div + Near = integral sobre la recta, Near = recta − Haar; Kronecker–Weyl como límite exacto (§3.4).
Cor. 3.5: la forma «defecto de Kronecker» del objetivo es REF-D. No cerró: identidad lineal en Λ, sin signo.

**1.4 CA_M_001 Teor. 3.1/Cor. 3.2.** La aritmética de sitios (p − np′) es «information-free»: la conclusión
sólo usa la PD del 𝖡 libre de sitios; NO-GO para toda ruta de aritmética de sitios. Pertinente al control
«Beurling libre»: allí ya se probó que el lado de sitios no distingue ℕ de un peine Beurling.

**1.5 AUDIT_204_TRACT_F_001 §3 (l.123–125).** Sólo vocabulario: levantamiento de Bohr a H²(𝔻^∞) para la cuestión
de ciclicidad de Báez-Duarte; [H] en su formulación; no toca el estado sin peso ni medidas representantes.

**1.6 NEAR_DOSSIER (212) ítem 8 y fila N_BUILD_022 §4 / L2_BUILD_028 §2(c).** NO-GO PROVED: «en el toro con fases
independientes sólo Div es diagonal; Near y Arch viven en la diagonal θ_p = θ log p». Es exactamente el punto en que
la propuesta deja la aritmética («la dirección de la recta frente a m»).

**1.7 Montgomery–Vaughan / Hilbert.** ANNEX_211_FILES_7 l.288 y l.464: control de pares no resonantes por la desigualdad
de Hilbert generalizada en el modelo de Poisson; da cota de magnitud del término fuera de diagonal, no signo.
Índice ANNEX_INDEX_04 l.498 «Magnitude bounds RFB/Carleson/sampling» [DEAD]; l.503 «evaluación por ventana más fina
que Montgomery–Vaughan» [OPEN] (es justamente lo que faltaría).

**1.8 «Medida representante» en 211.** ROUND_001_D, STATE_001, POWER_REDUCTION_AUDIT_044: otra medida (la de B en un
problema de momentos de Hamburger/Stieltjes), NO-GO «ciego al peine». Sólo vocabulario. «Jensen» en 104/119: medida
de Jensen de masa interior, otro objeto. Ningún archivo formula Φ(log n) = 0 como «ν representa a 0 en A(𝔻^∞)».

**Clasificación.** Levantamiento + recta de Kronecker + Haar vs recta: misma operación ya hecha (1.1–1.3, con peso;
la versión sin peso es caso particular: poner w = 0 en 𝖡 no cambia el Lema 1). Lectura «medida representante del
origen»: frase nueva en el corpus, pero es la traducción literal de la restricción del estado sin peso (§2).

## 2. Corrección de la formulación

(a) **Medida de Borel.** ι: ℝ → 𝕋^∞ continua e inyectiva (factorización única + independencia ℚ-lineal de los log p);
ι(ℝ) σ-compacto ⟹ Borel; ν := ι_*μ es Radon positiva finita (CA_E_001 Lema 1). ∫χ_r dν = ∫ r^{−iτ}dμ = Φ(log r) con la
convención μ̂(x) = ∫e^{−ixτ}dμ. Correcto. Normalizar ν(𝕋^∞) = Φ(0) = 1.

(b) **Momentos.** Φ real y par ⟹ ∫z^a dν = ∫z̄^a dν = 0 para todo a ≥ 0, a ≠ 0. Eso es exactamente «ν representa al
0 para el álgebra del polidisco» (equivalentemente para su cierre en C(𝕋^∞)). Los momentos mixtos z^a z̄^b
(a, b de soportes disjuntos) son Φ(log(n/m)), cocientes no enteros: libres. Correcto.

(c) **Ventana finita.** Φ = μ̂ es la autocorrelación de F ∈ P_T, con soporte en [−2T, 2T]. Para n ≥ e^{2T},
Φ(log n) = 0 es automático. La restricción efectiva son los monomios con n < e^{2T}, un número finito. Por tanto, para
T finito ν **no** representa al origen por imposición: lo hace por soporte compacto de Φ, que es propiedad de la clase
Paley–Wiener y no de ℕ. Además, en una variable (un primo p) sólo se imponen los momentos k < 2T/log p: la medida
imagen en S¹ no está forzada a ser Lebesgue a ventana finita. «Unicidad en una variable = optimalidad de un generador»
vale sólo en el límite de todos los momentos, no en la ventana. Hay que corregir ese enunciado de la propuesta.

(d) **Densidades de la ventana en 𝕋^∞.** ν es singular respecto de Haar (concentrada en una traslación Haar-nula de la
recta). La clase «μ = |F̂|²dτ/2π con F ∈ P_T» no tiene descripción intrínseca en 𝕋^∞: es la imagen de un espacio
de Paley–Wiener de la recta; el tipo exponencial 2T y los ceros dobles en ±i/2 son condiciones sobre ℝ, no sobre el toro.

(e) **El funcional.** m(τ) = Re ψ(¼ + iτ/2) − log π crece como log|τ| y no es casi periódica: no es restricción a la recta
de ninguna función continua (ni Borel acotada razonable) sobre 𝕋^∞ de la que dependa ∫m dν como funcional de ν en el
toro. ∫m dν sólo tiene sentido como ∫m dμ en ℝ. El objetivo no vive en el polidisco.

## 3. Herramientas disponibles y enunciado mínimo

- Teoría de medidas representantes/de Jensen del polidisco (Rudin, *Function theory in polydiscs*): describe el
  convexo de medidas en 𝕋^n que anulan momentos analíticos; sus cotas inferiores son para funcionales del tipo
  ∫ log|f| dν ≥ log|f(0)| (Jensen), con f analítica en el polidisco. m∘ι^{−1} no es log|f| de ninguna f analítica en
  𝔻^∞ (sería log|f(p^{−iτ})| sobre la recta: una serie de Dirichlet); habría que exhibir f = Σ a_n n^{−s} con
  log|f(½·?+iτ)| ≤ m(τ) en la recta y f(0) = a_1 controlado. Eso es reescribir m como subarmónica de una serie de
  Dirichlet: objeto no construido y no motivado por la propuesta.
- Carlson: lim (1/2X)∫_{−X}^{X} |Σa_n n^{−it}|² dt = Σ|a_n|² = recta → Haar en el límite: es CA_H_002 §3.4.
- Montgomery–Vaughan: ∫_{−X}^{X}|Σa_n n^{−it}|² = Σ|a_n|²(2X + O(n/δ_n)): cota de magnitud del defecto recta − Haar
  = Near; es 1.7, sin signo, y a escala de ventana finita el error O(n/δ_n) domina.
- Inmersión local de H²(𝔻^∞) (series de Dirichlet en intervalos): da ∫_I |f(it)|² ≲ ‖f‖²_{H²}; de nuevo magnitud.

**Enunciado mínimo que habría que probar.** Para toda μ = |F̂|²dτ/2π, F ∈ P_T, con Φ(log n) = 0 (n < e^{2T}):
∫ m dμ ≥ 0. Expresado en el toro no se simplifica: hace falta una cota que use a la vez ι (las frecuencias log p) y m,
es decir, una estimación del defecto recta − Haar con signo frente a m. Es (PBP_T) idéntico.

## 4. Filtro de cuatro puntos

1. **Antecedente más cercano:** CA_E_001 Lema 1 + CA_H_002 Teor. 3.1/Cor. 3.5 (levantamiento a Ĝ, recta de Kronecker,
   recta − Haar), con el NO-GO de NEAR_DOSSIER ítem 8 (Arch y Near viven en la diagonal θ_p = θ log p).
2. **Qué es nuevo:** sólo la etiqueta «medida representante del origen» para la restricción Φ(log n) = 0, y la observación
   de que en dimensión ≥ 2 el convexo es grande. Ninguna desigualdad nueva.
3. **¿Evita la dificultad del antecedente?** No. La dificultad de 1.1–1.3 es que la recta es Haar-nula y que m no es
   función del toro; la propuesta conserva ambas cosas (§2(d)–(e)) y además la condición representante es, a ventana
   finita, consecuencia del soporte de Φ (§2(c)).
4. **Desigualdad que conectaría con el signo global:** ninguna nombrada. Las herramientas del polidisco o acotan funcionales
   de tipo Jensen (que m no es) o dan magnitudes (Carlson, Montgomery–Vaughan) que ya figuran como DEAD/OPEN sin signo.

**Controles.** Sistema Beurling libre {q_j}: mismo grupo ⊕ℤ, mismo polidisco, mismo convexo de medidas
representantes, misma m; cambia sólo ι_q(τ) = (q_j^{−iτ}). Impares: un polidisco con una variable menos, mismo esquema.
¿En qué paso con nombre entra la dirección exacta (log p)_p? En ninguno de los enunciados del polidisco: entra sólo en
∫m dμ evaluada en ℝ, que es el problema original. CA_M_001 ya probó que el lado de sitios es «information-free».

## 5. Veredicto

**NO PASA (repetición; además sin mecanismo).** El levantamiento a 𝕋^∞ por la recta de Kronecker y la lectura recta − Haar
están hechos (CA_E_001, CA_C_002, CA_H_002; la versión sin peso es caso particular). La relectura como medida representante
del origen es otro lenguaje: a ventana finita es consecuencia del soporte de Φ, el funcional m no es definible en el toro,
y ninguna herramienta del polidisco usa la dirección (log p)_p. Corrección registrada: a ventana T la unicidad de una
variable no se aplica (sólo los momentos k < 2T/log p están impuestos).
Reapertura sólo con una f analítica explícita en 𝔻^∞ (serie de Dirichlet) tal que log|f∘ι| ≤ m sobre la recta con f(0)
controlado, o con una cota firmada del defecto recta − Haar frente a m; ninguna de las dos la aporta la propuesta.
