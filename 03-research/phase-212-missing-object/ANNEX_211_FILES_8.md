# Fase 212 — Anexo de lectura completa: archivos de la fase 211, bloque 8

Fuente: `../phase-211-sign-sandbox/`, archivos `*.md` en orden alfabético (`ls *.md | sort`), desde `ROUND_016_B.md`
hasta `TOOL_001_GALERKIN_MP.md` inclusive: 25 archivos, leídos completos. Notación de
`../phase-211-sign-sandbox/STATEMENT_001.md`: (★) es λ_A(T) ≥ 0 para todo T. Etiquetas tal como las registra cada
archivo. Abreviaturas: 𝒯 mapa de colas de Poisson; Ψ_f = 𝒯(ℱf) la cola de Ef en (−∞, −T); Φ_f(x) = e^{x/2}Σ_{n≥1}f(ne^x);
𝒲 forma de colas; 𝒜_∞ forma arquimediana; λ = e^T, N = e^{2T}; d_k = 1 − χ_k (prolatos ψ_k de [−λ, λ]).

## 1. Entradas por archivo

### 1.1 ROUND_016_B.md — colas directas del bloque alto, matriz de chirps, primera celda de Poisson
- Objeto: chirps F_N(x) = 1_{x<−T}e^{−x/2}u(Ne^{−x}), u = ε_kℱ(ψ_k1)|_{|ξ|>λ}; matriz B_{NN′} = (1/π)∫_0^∞ m Re(F̂_NF̂̄_{N′})
  − (log N + log N′)⟨F_N, F_{N′}⟩; métrica de cociente de gauge ℓ_g = 2 dist²(ℱf|_{(λ,∞)}, colas del gauge |y| < 1/λ).
- Lema 2.1 (forma de dilatación) PROVED: F_N = N^{−1/2}τ_{log N}F₁, 𝒯u = 𝔇F₁, ‖F₁‖² = ½‖u‖²; la forma de colas es
  independiente de T en F₁ (marco «universal» del DOSSIER §7.1, usado, no reclamado).
- Lema 2.2 (primera celda de Poisson) PROVED: u soportado en λ < |ξ| < 2λ ⇒ sin peine, 𝒲[𝒯u] = 𝒜_∞[F₁] en longitud log 2.
- Lema 2.3 (forma completa de colas W_T(Ef) = 𝒲[Ψ_f] + 2A(Ψ_f)B(Ψ_f)) CITED + NUMERICAL (5 dígitos en una sonda).
- Observación 2.4 (parte de salto, fórmula J²(1/2π)∫m/(β²+τ²)) PROVED; elección de β ARGUED.
- NUMERICAL: tres métodos concuerdan (unidad D de Galerkin = λ·a_T(Ef)/‖f‖²); la deriva es 100 % B₁₁ = 𝒜_∞[F₁]
  (peso del peine 2 log 1 = 0); no es el salto, ni los pares no resonantes (≤ 5 %, X_eff ≈ 1), ni el peine resonante.
- ARGUED: el bloque alto degenera en unidades D (fuga hacia un gauge de dimensión infinita); (HR) debe enunciarse en ℓ_g:
  (HR_g) 𝒢[b] ≥ κ_T·ℓ_g^S[b] en el bloque alto, κ_T independiente de K — OPEN (valores ≥ 0.80, aún decrecientes).
- Resto sin firmar: el suelo de (HR_g). Falsificadores: todo lo probado es Λ-ciego (no hay paso de signo).
- Fracasos registrados: «la deriva es el salto», «es MV no resonante», suelo uniforme en unidades D; omitir 2AB en el
  problema límite (negativo desde R = 3: no se debe volver a omitir).
- Resultado: PIVOT. Siguiente paso: cota de primera celda 𝒜_∞[F] ≥ μ‖F‖² bajo los funcionales transportados, y ℓ_g con
  el gauge resuelto. Tomado: la primera parte por ROUND_017_C (Teoremas 3.1, 3.3); el ℓ_g resuelto no se retomó en el bloque.

### 1.2 ROUND_017_A.md — vector de acoplamiento del superviviente, corrección de Schur y falsificadores
- Objeto: superviviente f_* = 0.1037ψ_0 − 0.7340ψ_4 + 0.6712ψ_8 (núcleo de f(0), ℱf(0), A(Ef), B(Ef)); F = Ef_*/‖Ef_*‖,
  H = P_T ⊖ F, b(G) = a_T(F, G), ρ = a_T(F), C = a_T|_H.
- Prop. 1.1 (forma de Schur/secular) PROVED: (★) en T ⟺ C ⪰ 0 y ρ ≥ sup_{G∈H} b(G)²/a_T(G).
- Prop. 1.2 PROVED para f admisible con f(λ) = 0, ARGUED para el superviviente: b(G) = ∫_0^∞ h_G dν,
  h_G(u) = ⟨Ψ, G(·+u)⟩, ν = ½K du + Σ_{n≥2}Λ(n)n^{−1/2}δ_{log n} (peine sin colapsar), b_Tate ≡ 0 en P_T; en imágenes E,
  b(Eg) = 𝒲(Ψ_f, Ψ_g) (identidad radical de segundo nivel (1.3), peine colapsado a log N).
- Prop. 1.3 PROVED: parte impar de Ef, f ∈ span{ψ_0, ψ_4, ψ_8}, es −½E(u1_{(λ,∞)}) + O(d), Λ-libre.
- Prop. 3.1 PROVED: bajo cΛ, a_P, e finito, b cambia por el defecto radical X_w = 𝒞_{Λ−w}(Φ_{f*}, ·), O(1).
- NUMERICAL (T = 0.8, 1): ρ/λ_A = 1.58/1.49; parte de Schur 0.366/0.329; partes arch y peine 10²–10³⁸ veces la corrección
  y se cancelan; ≈ la mitad es defecto de paridad Λ-libre, el resto acoplamiento cola–cola a los peldaños pares.
  Umbral c > 1: λ_A/Π_T(F) (5·10⁻²² en T = 1); c < 1: tamaño del peldaño siguiente (corrige el 1.5·10⁻⁴ de ROUND_015_B).
- Fracasos: hipótesis de 015_B §3.5 («términos cruzados dependientes del peine»); modelo de bloque de cinco prolatos.
- OPEN: balance de Schur del superviviente exacto (𝒲[Ψ_*] exacto no calculado); si la desigualdad cola–cola sobrevive a
  c·log N (si sobrevive, (R) es robusto al peine y no es paso de signo).
- Resultado: PIVOT. Siguiente paso: Gram de colas en (Ψ_*, Ψ_g) en coordenadas de dilatación, Schur 2×2 y 3×3, repetir
  con c·log N. No retomado en este bloque (STATE_001/002 lo resumen; ningún archivo posterior del rango lo calcula).

### 1.3 ROUND_017_B.md — márgenes de banda a rango completo T = 2.5–4, forma cerrada sin matriz
- Objeto: A_τ^{(η)} compresión de A_τ a span{e_1..e_K}, e_k = sin(a_k(x+T))/√T, a_k = kπ/2T; margen
  μ_η(τ) = m(τ) − λ_max(A_τ^{(η)}).
- Prop. 1.1 PROVED: A_τ^{(η)} = ½(𝔈 + 𝔈ᵀ), 2T𝔈 = CS − ESCE + ESHE + HS + Dd, C Toeplitz (a_j − a_k)^{−1}, H Hankel
  (a_j + a_k)^{−1}; el peine entra sólo por s_k = Σ c_n sin(a_kℓ_n), d_k = Σ c_n(2T − ℓ_n)cos(a_kℓ_n), c_n = v_n cos(τℓ_n).
- NUMERICAL: mín μ_⅛ = 0.2566 (T = 2.5, rango completo [1.1, 3]·2πN), 0.1140 (T = 3, completo), ≤ 0.1343 (T = 3.25),
  ≤ 0.0782 (T = 3.5), ≤ 0.1341 (T = 4) (rangos parciales); W_T directo = margen a 10⁻⁶; ningún valor negativo; sin
  certificado. El cero extrapolado en T ≈ 3.3 no aparece; el mínimo lo fijan celdas de alineación aisladas.
- Falsificador: cΛ falla (HB_η) en la celda de T = 3.5 para c > 1.0111 (presupuesto c*(T) decreciente).
- Fracasos/«no reusar como atajo»: pantallas g_T (tono de ventana plana), bloque denso k ≤ 96, diagonal — cotas de
  Rayleigh válidas pero 0.2–0.9 por encima; Lanczos con arranque tibio puro (falla en 6 % de puntos).
- Siguiente paso: cubrir [1.2, 3]·2πN en T = 3.5 y [1.11, 3]·2πN en T = 4; localizador de celdas de alineación por fases
  τ log p mod 2π, p ≤ 13; certificar sólo si aparece celda menor. No tomado en el bloque.

### 1.4 ROUND_017_C.md — coercividad de primera celda de la forma arquimediana en longitud log 2
- Objeto: 𝒬[F] = (1/2π)∫m|F̂|² = (C_0 + ∫_L^∞K)‖F‖² + ½∫_0^L K(u)∫|F(x+u) − F(x)|² dx du, L = log 2,
  C_0 + ∫_L^∞K = −2.3784…; hiperplano H₀ = {∫_I F e^{−y/2} = 0}; cuatro funcionales transportados f(0), f(λ), A, B.
- Lema 2.1 (símbolo monótono) PROVED; Lema 2.2 (truncación del símbolo, 𝒬 ≥ M‖F‖² − ⟨GF, F⟩) PROVED; Lema 2.3
  (compresión polinómica con cola HS ≤ L(τ*/π)(M − C_0)(τ*L/2)^n/n!) PROVED; Lema 2.4 (cota inferior con restricciones y
  fuga) PROVED.
- Teorema 3.1 PROVED (asistido por computadora, aritmética de bolas, independiente de T): en toda ventana de longitud log 2,
  ∫F e^{−y/2} = 0 ⇒ (1/2π)∫m|F̂|² ≥ μ₀‖F‖², μ₀ = 0.069611…; verdadero valor en [0.0696, 0.0720].
- Corolario 3.2 PROVED: en longitud log 2 la forma completa 2AB + (1/2π)∫m|F̂|² ≥ μ₀‖F‖² sobre {B(F) = 0}.
- Teorema 3.3 PROVED (asistido, puntual en T): con los cuatro funcionales transportados, μ₄(0.8) ≥ 0.527631,
  μ₄(1.0) ≥ 0.549417.
- §4(i) CONDITIONAL al transporte de 016_B §3.1: κ_T ≥ (λ/2)μ₄ en datos de primera celda.
- OPEN: defecto de transporte; datos en R ≥ 3 celdas (análogo multicelda de Lema 2.4 con el cierre de gauge como W;
  el peine entra vía 𝔇); términos cruzados primera celda–resto.
- Falsificadores: todo vale bajo cΛ, a_P, Beurling, modificaciones finitas ⇒ no es paso de signo.
- Siguiente paso: versión multicelda (R = 3, 4) de Lema 2.4 con el gauge transportado como W; cuantificar el defecto de
  transporte. No tomado en el bloque.

### 1.5 ROUND_018_A.md — defecto de transporte en los vectores medidos y forma completa en R celdas contra ℓ_g
- Objeto: Q_R[F] = 𝒲[𝔇_RF] + 2A(𝔇_RF)B(𝔇_RF), 𝔇_RF = Σ_{N<R}N^{−1/2}F(· − log N)1_{I_R}, 𝒲 = 𝒬 − cΠ,
  Π[H] = Σ_{2≤m<R}2Λ(m)m^{−1/2}⟨τ_{log m}H, H⟩; V_R = cuatro funcionales transportados sobre todo F;
  κ_R(T) = inf_{V_R} Q_R/ℓ_g.
- NUMERICAL: masa en banda < 10⁻⁴; defecto de valor siempre ≥ 0 (primera celda es modelo inferior); defecto de restricción
  δ = 0.03–0.16 (f(λ), A, B oscilantes no se transportan; f(0) sí, coseno ≤ 0.007).
- Lema 1.1 (transferencia de cota de codimensión k a datos casi restringidos, por la seminorma de 𝒬 + β) PROVED;
  positivo sólo si δ < δ* = 0.0752.
- Prop. 3.1 (R = 2 en ℓ_g desde 17C) PROVED; Lema 3.2 (compresión por trozos con 𝔇₃ y peine exactos) PROVED; Lema 3.3
  (cota de tres celdas contra familia de gauge finita con todos los términos de fuga) PROVED.
- Teorema 3.4 PROVED (asistido, T ∈ {0.8, 1.0}): Q₃[F] ≥ 0.70·ℓ_g[F] en V₃ (sólo m = 2 actúa en longitud log 3).
- Teorema 4.1: (i) PROVED para datos idealizados R = 2, 3; (ii) CONDITIONAL para el bloque alto (falla por δ);
  (iii) NUMERICAL negativo: κ_R colapsa para R ≥ 5 (T = 0.8), R ≥ 4 (T = 1.0): 0.11–0.17, 0.10, 10⁻⁴, 10⁻¹¹ (R = 5…8).
- NO-GO NUMERICAL (clase: problema idealizado de R celdas con restricciones transportadas, R ≳ 4): «límite equivocado»;
  falta la limitación de banda (tipo exponencial 2πλ de ℱf) como familia de restricciones, OPEN.
- Falsificador: Teorema 3.4 sobrevive c = 0.9 y falla c = 1.1 (γ < 0); en R = 4 fallan c = 0.9 y 1.1. Primera cota
  certificada de la fase destruida por cΛ, c = 1.1 — no reclamada como paso de signo (a_P con P = 3 la sube).
- Siguiente paso: añadir la limitación de banda (p. ej. el span prolato alto transportado celda a celda) y remedir κ_R,
  R = 5…8; correr (b)–(d) sobre el Teorema 3.4. No tomado en el bloque (STATE_002 lo cita como abierto).

### 1.6 ROUND_018_B.md — libro exacto del superviviente, Grams de colas en los primeros peldaños, prueba c·log N
- Objeto: 𝒲̂ = 𝒜_∞ − 𝒞 + 𝒯 sobre colas, 𝒯(F, G) = A(F)B(G) + B(F)A(G); par (Ψ_*, Ψ_g), g peldaños admisibles en
  E(span{ψ_0 … ψ_20}) (y hasta ψ_40).
- Lema 1.1 PROVED: cambiar log N por c log N en las colas es 𝒲̂^c = 𝒜_∞ − c𝒞 + 𝒯; difiere de a^c_T por el defecto radical
  (1 − c)𝒞(Φ_f, ·) = O(1).
- Lema 1.2 PROVED: (4.1) de 17A en span{Ef_*, Eg} ⟺ det de la Gram 2×2 de 𝒲̂ ≥ 0; parte del peldaño s_g = 1 − det/(ρa_T(G)).
- NUMERICAL: ρ = 𝒲̂[Ψ_*] = 8.23·10⁻¹² (T = 0.8), 2.17·10⁻²³ (T = 1); 𝒜_∞ : 𝒞 : 𝒯 ≈ 3.2 : 0.77 : 0; parte de Schur en
  imágenes E 8–13 % (peldaños 2–10 %); el resto (≈ 0.16–0.26 ρ, paridad) no vive en imágenes E de prolatos ψ_0…ψ_40.
- NO-GO (clase: «la pieza de peldaños (R) de la desigualdad de Schur como portadora del signo — positividad 2×2 de la Gram
  completa de colas en {Ψ_*, Ψ_g} con peso colapsado log N»): sobrevive c ∈ [0, 3.5] (det se anula en c ≈ 3.6–4.2);
  genérica en el peine. Falsificador: cΛ (a) basta; (b)–(d) no corridos.
- Lectura registrada: toda la sensibilidad en c de (★) en imágenes E está en la identidad a_T(Ef) = 𝒲̂[Ψ_f] (radicalidad de
  Φ_f), ninguna en la Gram de colas (la ventana muere a |1 − c| ≈ 5·10⁻²², la cola tolera |1 − c| ≈ 3).
- Observación 4.1 (m_eff contra κ_w; enunciado de frecuencia, ciego a la aritmética).
- Siguiente paso: acoplamiento de Schur del superviviente con la pieza de paridad (P) en forma de preimagen E (inversión de
  Möbius en [e^{−T}, λ]) para decidir si (P) también es robusta al peine en forma de cola. No tomado en el bloque.

### 1.7 ROUND_019_A.md — limitación de banda de la cola como familia de restricciones en datos de R celdas
- Objeto: E_λ = {ℱf : f ∈ L²(−λ, λ) par}; 𝔅_R; proyección P_λ de núcleo k_λ(ξ, η) = sin2πλ(ξ−η)/(π(ξ−η)) +
  sin2πλ(ξ+η)/(π(ξ+η)); defecto de banda β[F] = ‖(1 − P_λ)u‖²; operador de concentración B_R = 1_{J_R}P_λ1_{J_R};
  familias S_θ (espectral) y cono {β ≤ ε‖F‖²}; cociente penalizado κ_R(μ) = inf_{V_R}(Q_R + μβ)/ℓ_g^{fam}.
- Prop. 1.1 PROVED + NO-GO (formulación cualitativa): 𝔅_R ∩ V_R es denso en la norma de forma de Q_R; imponer «u es
  restricción de una función de tipo 2πλ» no cambia κ_R.
- Lema 2.1 PROVED: β[u]^{1/2} ≤ ‖g‖_{L²(0,λ)} + ‖g‖_{L²(Rλ,∞)}.
- NUMERICAL: las direcciones de colapso son casi de banda (β/‖F‖² ≤ 10⁻⁷…10⁻¹³) pero β/ℓ_g ≈ 0.8–1.7; con μ ≥ 10² el cociente
  vuelve a 0.45–0.71; con μ = 10⁶ ≥ 0.627 en R = 3…8; no se ve uniformidad en R a μ fijo.
- Teorema 4.1 CONDITIONAL (H_band(μ, κ) y H_lim): forma completa de colas ≥ κℓ_g − μ‖ℱf‖²_{L²(0,λ)}; mueve el déficit a la masa
  en banda (bloque bajo). H_band(10⁶, 0.62) NUMERICAL para R ≤ 8; H_lim ARGUED; transporte falla (18A §1).
- §5.1 PROVED: toda afirmación a R fijo es invariante bajo (c), (d) más allá de la celda R ⇒ pieza de coercividad, nunca
  paso de signo; el signo sólo podría vivir en la uniformidad en R.
- Certificados (arb): Q₃ ≥ 0.60ℓ_g con c₂ = 0 (a_3) en T = 0.8, 1.0; Q₃ ≥ 0.20ℓ_g con c₂ = 1.01 (T = 0.8). Umbral
  c₂* ≈ 1.016 (T = 0.8), 1.008 (T = 1.0): el peso verdadero queda 0.8–1.6 % por debajo del umbral.
- NUMERICAL: en R = 4 el falsificador (a) falla por ambos lados (c = 0.9 y 1.1), primera falla bilateral de la fase.
- OPEN: (1) certificado H_band en R ≥ 4; (2) mecanismo uniforme en R (la celda R+1 sólo crea direcciones casi nulas con
  β/ℓ_g ≳ 1); (3) cota de bloque bajo (LB_μ).
- Resultado: PIVOT. Siguiente paso: medir el lado en banda (LB_μ) para μ = 10², 10⁴, 10⁶ y certificar H_band en R = 4
  (cinco piezas). No tomado en el bloque (ROUND_019_B pivota a la reducción de colas; STATE_002 lo lista abierto).

### 1.8 ROUND_019_B.md — reducción de colas (i)+(ii): densidad de la imagen E; el margen robusto al peine es efecto del representante
- Objeto: admisibles f (par, soporte [−λ, λ], C², f(0) = ℱf(0) = f(λ) = 0); gauge 𝒢_T = {φ admisible, soporte ⊂ [−1/λ, 1/λ]};
  𝒲̂^c = 𝒜_∞ − c𝒞 + 𝒯, 𝒜𝒫 = 𝒜_∞ + 𝒯; radicales de gauge Φ_φ con Φ̃_φ(s) = ζ(s)Mφ(s).
- Prop. 1.1 PROVED (≈ CITED, lem:ext-mob): E(admisibles) ⊇ C_c^∞(I_T) ∩ P_T por inversión de Möbius, fibra f_0 + 𝒢_T.
- Cor. 1.2 PROVED: (★) en T ⟺ 𝒲̂[Ψ_f] ≥ 0 para todo admisible con Ef ∈ P_T ∩ C_c^∞(I_T) — reformulación (REF-D), igual a
  eq:ext-starstar con κ = 0; prob:ext-L es la versión con margen, estrictamente más fuerte.
- Teorema 2.1 PROVED: existen φ_R ∈ 𝒢_T con B(Φ_φ) = 0 y 𝒜𝒫[Φ_{φ_R}] → m(0)ζ(½)²‖η‖² ≈ −11.457‖η‖² y otros con
  → m(10)|ζ(½+10i)|²‖η‖² ≈ +1.114‖η‖² (sin usar ceros; sólo ζ(0) = −½ y dos valores puntuales).
- Cor. 2.2 PROVED: para todo admisible f y todo c ≠ 1, inf_{φ∈𝒢_T}𝒲̂^c[Ψ_{f+φ}] = −∞ (Prop 1.5 de ROUND_001_B, ahora PROVED
  con ambos signos).
- Cor. 2.3 PROVED / NO-GO (clase: cotas robustas al peine o ponderadas «coercividad arquimediana vence al peine que
  solapa» para (ii) sobre toda la clase de colas admisibles): 𝒜_∞ + 𝒯 − c𝒞 ≥ 0 en colas admisibles es falso para todo
  c ≠ 1. El margen c ∈ [0, 3.5] de 18B es propiedad del representante, no de la clase.
- OPEN: (ii_s) 𝒲̂^c[Ψ_{f_G}] ≥ 0 para una sección de gauge fija G ↦ f_G y c ∈ [0, c₁], c₁ > 1; ARGUED que es prob:ext-L en
  otro gauge (densidad de las colas de gauge ARGUED).
- Falsificadores: (a) (i) falla; (b)–(d) (i) falla; análogo de Cor 2.2 para (d) ARGUED.
- Siguiente paso: fijar el gauge por el representante que minimiza la fuga y medir 𝒲̂^c, c ∈ [0.5, 2], con rango de gauge
  ≥ 30. No tomado en el bloque (ROUND_020_A cambia de objeto).

### 1.9 ROUND_020_A.md — desigualdad de colas con gauge fijado: representantes, cuádrica nula del peine, secciones canónicas
- Objeto: V_T = {Ψ_f : f admisible, Ef ∈ P_T}, R_T = {Φ_φ : φ ∈ 𝒢_T}; fibras Ψ_f + R_T; cuádrica {𝒞 = 0}; Rep(I) =
  representantes con 𝒲̂^c ≥ 0 para c ∈ I; secciones Λ-libres (none, ell = mín ℓ, f2 = mín ∫_0^{1/λ}f², tail = mín ‖Ψ‖²).
- Lema 1.1 PROVED: 𝒞[Ψ + Φ] = 𝒞[Ψ] + 2𝒜𝒫(Ψ, Φ) + 𝒜𝒫[Φ]. Lema 1.2 PROVED: toda fibra corta {𝒞 = 0}.
- Teorema 1.3 PROVED: para c ≠ 1 aislado siempre hay buen representante; para todo intervalo I ∋ 1, Rep(I) ≠ ∅ ⟺ 𝒲̂ ≥ 0.
- Cor. 1.4 PROVED: (★) ⟺ 𝒜𝒫 ≥ 0 en V_T ∩ {𝒞 = 0} (reformulación invariante bajo escala del peso; Λ-específica sólo vía (A)).
- Teorema 1.5 PROVED en secciones de dimensión finita (ARGUED en general; S-lema de Finsler CITED): el multiplicador está
  forzado a μ = 1 por los radicales de gauge de ambos signos.
- NO-GO PROVED (clase: versión existencial «elegir el representante con positividad robusta al peine» = (★)).
- NUMERICAL: secciones canónicas sin margen uniforme: ell δ = 0.027 → 0.0035; f2 0.73 → 0.24; tail 1.29 → 0.37 al refinar.
  Mecanismo ARGUED: minimizantes tipo L² no se alcanzan si el gauge es denso.
- OPEN: (B_δ, s) 𝒜𝒫[Ψ] − c𝒞[Ψ] ≥ 0 en Ran s, c ∈ [1 − δ, 1 + δ], s sección lineal Λ-libre; ARGUED no más débil que prob:ext-L.
- Falsificadores: (A) falla para (a), (b), (d); (c) sin Poisson. (B) por sí misma es robusta al peine y no lleva signo.
- Resultado: NO-GO (existencial) + PIVOT (secciones). Siguiente paso: w = 0.025, 0.018 y ajustar δ(w); si δ → 0 registrar el
  cierre de la línea de colas con gauge fijado; si estabiliza, norma de cola tipo H¹. No tomado en el bloque.

### 1.10 ROUND_021_A.md — ventana de positividad J_R(T) de la forma completa de R celdas
- Objeto: Q_R^{(w)}[F] = 𝒜[𝔇_RF] − Π_w[𝔇_RF] + 2A(𝔇_RF)B(𝔇_RF), Π_w = Σ w_nΠ_n; J_R = {c : Q_R^{(c·1)} ≥ 0 en V_R}; ventanas
  por primo y por átomo; álgebra de Dirichlet truncada Φ_R(α) = Σ_{n<R}α_n n^{−1/2}τ^I_{log n}.
- Lema 1.1 PROVED: cada ventana es un intervalo cerrado. §2.1 PROVED: las ventanas de Galerkin son cotas exteriores.
- §3.1 PROVED: Φ_R homomorfismo (convolución de Dirichlet → desplazamientos comprimidos), núcleo {α_n = 0, n < R};
  [M_x, Φ_R(α)] = Φ_R(α·log).
- Prop. 3.2 PROVED: P_w𝔇_R = [M_x, 𝔇_R] ⟺ w ≡ 1 en potencias de primos < R; Q_R^{(c)} = Q₀ − c𝒦_R,
  𝒦_R[F] = 2⟨𝔇_RF, [M_x, 𝔇_R]F⟩ = 2Σ_{m,n<R}(log n)(mn)^{−1/2}⟨τ_{log m}F, τ_{log n}F⟩; Λ desaparece.
- Lema 3.3 PROVED (sándwich): λ₀/‖𝒦‖ ≤ c_+ − 1 ≤ λ₀/K₀ y análogos para c_−.
- NUMERICAL: J_R → {1} bilateralmente y superexponencialmente (δ_+ = 1.7·10⁻², 5·10⁻⁵, 6.7·10⁻⁸, 1.3·10⁻¹¹, 7.4·10⁻¹⁶,
  6.9·10⁻¹⁹, R = 3…8); a_P falla por O(1) desde R = 4; ventanas por primo encogen igual.
- NO-GO (clase: ventanas de positividad en el peso del peine sobre datos idealizados de R celdas, uniformes o por primo):
  el encogimiento equivale a λ₀(R) → 0 (Lema 3.3), sin cota inferior; el mecanismo (Prop. 3.2) sobrevive al
  falsificador (c) Beurling (estructural PROVED, numérico ARGUED). NO-GO NUMERICAL de κ_R uniforme en R (ya en P211-18A).
- Resto sin firmar: Q₀ − 𝒦_R ≥ 0 en V_R (Λ-libre), fondo ~ exp(−2.9R log R) (ajuste).
- Siguiente paso: dirección casi nula de Q₀ − 𝒦_R y prueba de si es la 𝔇_R-preimagen (𝔇_R^{−1} = Φ_R(μ)) del fondo de 𝒜 − Π
  en la ventana. No tomado en el bloque (ROUND_021_B estudia la ventana nativa, no esa comparación).

### 1.11 ROUND_021_B.md — márgenes de banda en celdas de alineación de primos pequeños, T = 3.5–4.5
- Objeto: margen de banda μ_η(τ) = m(τ) − λ_max(A_τ^{(η)}); localizadores h₄(τ) = Σ_{p∈{2,3,5,7}}(1 − cos(τ log p)),
  δ(τ) = max_p‖τ log p/2π‖, y g_T (tono de ventana plana); r = τ/2πN.
- Todo NUMERICAL (vigilancia de contraejemplos; no hay paso de signo ni falsificador aplicable).
- Resultados: ningún margen negativo ni < 0.02; mínimo hallado 0.0631 (T = 4.2, τ = 30775.05574, r = 1.10); cotas
  superiores por T: 0.114 (3.0), ≤ 0.134 (3.25), ≤ 0.078 (3.5), ≤ 0.106 (3.75), ≤ 0.084 (4.0), ≤ 0.071 (4.1), ≤ 0.063
  (4.2), ≤ 0.084 (4.25), ≤ 0.083 (4.5).
- Corrección a ROUND_017_B: τ = 7713.88 no es alineación simultánea (p = 3 a un cuarto de ciclo); el mínimo de T = 3.25 está
  antialineado. Alineación ni necesaria ni suficiente; la posición r ≈ 1.1 predice la profundidad; en celda fija el margen
  decrece monótonamente en T.
- Fracasos: localizadores h₄ y g_T no localizan mínimos; ventana de pulido ±0.1 demasiado estrecha en algunas celdas.
- Resultado: PIVOT. Siguiente paso: barrido completo de Lanczos de la franja r ∈ [1.1, 1.3] en T = 4.0, 4.25, 4.5 y
  seguimiento en T. No tomado en el bloque.

### 1.12 ROUND_022_A.md — la forma de R celdas sobre sistemas de enteros generalizados
- Objeto: sistema 𝒩 (clausura multiplicativa de generadores g > 1), Λ_𝒩 por Σ_{de=x}Λ_𝒩(d) = log x;
  𝔇^𝒩 = Σ_{x∈𝒩,x<R}x^{−1/2}τ^I_{log x}, Π^𝒩, Q^𝒩 = Q₀^𝒩 − 𝒦_R^𝒩; λ₀(R; 𝒩); conjunto de sumación S de las restricciones A/B.
- Lema 3.1 PROVED: el homomorfismo Φ_R^𝒩 y [M_x, Φ^𝒩(α)] = Φ^𝒩(α log) valen para todo sistema multiplicativamente cerrado.
- Prop. 3.2 PROVED (perturbación CITED Rellich–Kato): ∂_{η_i}𝔇 = −G_i𝔇(½ + ∂), ∂_{η_i}P = G_i − η_iG_i^{(1)}(½ + ∂);
  dirección exponente ∂_t𝔇 = −[M_x, 𝔇](½ + ∂) = −P𝔇(½ + ∂), ∂_tP = P − Φ(Λ log)(½ + ∂); pendientes de Hellmann–Feynman.
- Prop. 3.3 PROVED (parte estructural: ℕ^{1+t} ≅ ℕ como monoides ordenados, Λ escalado por 1 + t; ℕ único aditivamente
  cerrado) + NUMERICAL (signo): positivo para t ∈ [−10⁻³, 0], negativo para t > 0 (10⁻⁶…10⁻³); el signo de R celdas no es
  invariante de monoide; ℕ en la punta de una cuña fina a lo largo de ℕ^{1−ε}.
- NUMERICAL: perturbaciones genéricas (2 → 2 ± δ, 3 → 3 ± δ, primo extra 2.5, sistema libre en {2, 3}, √p, ℕ ∪ √2ℕ)
  negativas desde la primera R en que difieren; el conjunto de sumación de las restricciones no influye en el signo.
- Falsificador (c): la positividad de R celdas SOBREVIVE en el rayo Beurling ℕ^{1−ε} para ε ≤ ε₀(R) ≈ 0.1, 0.05, 0.02,
  0.005 (R = 5…8); ningún enunciado a R fijo es paso de signo; un mecanismo debe producir ε₀(R) → 0.
- OPEN: signo de ∂_tQ en el racimo casi nulo (δ_tQ[u_k] < 0, NUMERICAL, sin prueba).
- Fracasos: «perturbados negativos ⇒ signo ℕ-específico» (falso en ℕ^{1−ε}); «el espaciado entero vía Poisson en las
  restricciones es responsable» (sin efecto).
- Siguiente paso: probar o refutar ∂_tQ[u] < 0 en los vectores casi nulos; medir ε₀(R), R = 9, 10; aislar casi coincidencias
  con un sistema que preserve los log-huecos hasta un tamaño y rompa una relación m = kn. Parcialmente tomado: ROUND_022_B
  estudia ∂_tQ en el racimo casi nulo.

### 1.13 ROUND_022_B.md — barrido completo de Lanczos de la franja r ∈ [1.1, 1.3], T ≥ 4
- Objeto: el margen de banda μ_⅛(τ) de 017_B/021_B; malla τ ∈ w₀ + δℤ, δ = h/m, h = π/2T, con S(w), D(w) tabulados
  (herramienta strip_scan.py).
- Todo NUMERICAL; nada probado. Cobertura: T = 4.0 r ∈ [1.100, 1.158] (mín 0.07979, τ = 20948.73412); T = 4.5 sólo
  r ∈ [1.1000, 1.1008] (0.1377); T = 5.0 sólo r ∈ [1.10000, 1.10005] (0.1226 de malla, sin pulir).
- Seguimiento de cinco celdas en T: decrecen monótona y casi linealmente en log r (convexas, se aplanan en el extremo
  bajo); valores en r = 1.1: 0.0631, 0.0713, 0.0773, 0.0789, 0.0849; extrapolación lineal del cero en r ≈ 0.29–0.39 (fuera de
  la ventana). Mínimo visto 0.0589 en r = 0.997 (fuera de ventana).
- Ningún valor negativo, ninguno < 0.02; regla de parada no disparada. El arranque tibio puro vuelve a fallar.
- Fracaso: barrido completo inviable por costo del autosolver (K = 6.6·10³ … 6·10⁴).
- Siguiente paso: (a) terminar T = 4.0 en r ∈ (1.158, 1.3] y parar; o (b) localizador certificado por cota de Lipschitz de
  λ_max(A_τ) en τ (dλ/dτ = ⟨∂_τA x, x⟩). No tomado en el bloque.

### 1.14 ROUND_023_A.md — el rayo de exponentes ℕ^{1+t}: bordes del segmento positivo y primera variación en t = 0
- Objeto: familia ℕ^{1+t}, variantes powfix (conjunto de celdas fijo), sig (pesos n^{−(1+t)/2}), pos (posiciones
  (1+t)log n), lam (peine (1+t)Λ); D = ½ + ∂; U_s(F)(y) = s^{1/2}F(sy).
- Lema 2.1 PROVED: Φ(Λ·log) = [M, P] = 𝔇⁻¹[M,[M,𝔇]] − P², 𝔇⁻¹ = Φ(μ) (identidad de Selberg Λ·log + Λ∗Λ = μ∗log² en
  forma de operadores, CITED).
- Prop. 2.2 PROVED: ∂_t = δ_lam + δ_sig + δ_pos; δ_lamλ_k = −𝒦_R[u_k] (Hellmann–Feynman CITED).
- Prop. 2.3 PROVED (imagen de dilatación): ℕ^{1+t} en ventana log R es unitariamente la forma de R^{1/s} celdas de ℕ con peine
  ×s, exponente de peso s/2, datos arquimedianos y restricciones dilatados.
- Prop. 2.4 PROVED (identidad virial): δ_posλ_k = −ℓ∂_ℓλ_k + δ_∞λ_k + δ_Cλ_k; δ_∞ es la forma de (uk_∞(u))′ en 𝔇u, indefinida.
- Lema 4.1 PROVED (cotas de borde de primer orden) y fórmula 2×2 de acoplamiento del racimo (PROVED, elemental).
- NUMERICAL: λ₀(9) = 1.33·10⁻²², λ₀(10) = 1.06·10⁻²⁴ (T = 0.8); pendientes casi nulas en [−3.4, −0.9], ≈ 90 % δ_pos; borde
  derecho t₊ ≈ 1.05λ₀; borde izquierdo |t₋| ≈ λ₀^{0.10…0.13}; la celda prima que entra extiende el segmento.
- ARGUED: la unicidad de ℕ en el rayo = [positividad en ℕ] + [corolario genérico del colapso]; no es caracterización que
  aísle la suma; ℕ es el punto de margen mínimo del segmento: no hay palanca variacional; aun probado ∂_tλ₀ < 0 no da
  λ₀(0) ≥ 0. Declarado: «el rayo de exponentes no debe seguir como ruta a (★)».
- OPEN: signo de ∂_tQ en el racimo; si ∂_tλ₀ → −1 es exacto (curiosidad estructural).
- Falsificadores: (a) la misma unicidad en c = 1; (b), (d) fallan O(1); (c) ℕ^{1−ε} finalmente rechazado por el mecanismo
  genérico.
- Resultado: PIVOT. Siguiente paso: evaluar δ_∞, δ_C, ℓ∂_ℓ en u₀ para R = 4…10 (sólo curiosidad). No tomado.

### 1.15 ROUND_024_A.md — tres diseños portadores de signo en el eje de ancho de banda; lema de entrada de contacto
- Objeto: eje N continuo, contactos que entran en T_n = ½ log n (Λ(n) ≠ 0); diseño A (libro de entradas), diseño B
  (relación de piso de Chebyshev Σ ε_k⌊y/k⌋ ∈ [0, 1], ε = (1, −1, −1, −1, 1) en k = 1, 2, 3, 5, 30, a la truncación exacta
  log n < 2T), diseño C (extremalidad prolata con conteo de restricciones de índice 8).
- Prop. 2.1 PROVED / NO-GO (clase: finitas relaciones de piso estrictas, cualquier precisión): el conjunto de pesos que las
  cumple con holgura es abierto en c alrededor de Λ en todo rango acotado; sin holgura es R10 (Λ ∗ 1 = log).
- Lema 4.1 PROVED: |c_F(2T − δ)| ≤ ‖F‖_{L²(T−δ,T)}‖F‖_{L²(−T,−T+δ)}. Lema 4.2 PROVED: c_F(2T − δ) = δF(T⁻)conj F(−T⁺) + o(δ)
  (O(δ^{3/2}) en H¹).
- Prop. 4.3 PROVED: en una entrada, −v_n Re c_F(log n) = −2hv_nF(T⁻)² + o(h) < 0 para F real par; > 0 para F real impar.
- Cor. 4.4: (i) PROVED |a_T − a_T^{∖n}| ≤ v_n × producto de franja de borde; (ii) CONDITIONAL a (R_edge) (fondo simple,
  continuidad en el borde): salto de la derivada derecha de λ_A en T_n igual a −2v_nF*(T_n)².
- NO-GO (clase: positividad propagada a través de entradas de contactos a lo largo de N): ley de entrada de signo
  definido y genérica en el peso (sobrevive (a) c > 0, (b), (c), (d)); toda propagación se reduce a la cota de tasa (EB_C)
  de P211-8C, OPEN (clase reformulación).
- Diseño C: reintento de L′/L′♯, muere en las direcciones de gauge (ARGUED, no perseguido).
- ARGUED: por la identidad de Slepian el salto de entrada ≈ (2v_nc/(Tκ₈))·λ_A: salto en la derivada logarítmica, no
  impulso aditivo; explica la invisibilidad de contactos en log λ_A.
- Siguiente paso: probar (R_edge) y la ley de entrada numéricamente en n = 7, 8, 9 (derivadas logarítmicas en T_n ± 10⁻⁴) y
  registrar el residuo de (EB_C) como única pieza en el eje de ancho de banda. No tomado en el bloque.

### 1.16 ROUND_025_B.md — el enunciado sin primos como núcleo sobre una función: razón coprima, factores locales, prueba de producto de Schur
- Objeto: 𝒬[F] = 𝒜𝒫[Ψ] − 𝒞[Ψ] = ∫∫F(y)F(y′)K_ℕ(y, y′), K_ℕ = Σ_{N,N′}(NN′)^{−1/2}{k(y − y′ + log(N/N′))1[N < ξ/λ]1[N′ < ξ′/λ]
  − log(NN′)δ(y − y′ + log(N/N′))1[N < ξ/λ]} + α⊗β + β⊗α, α = e^{y/2}⌊ξ/λ⌋, β = e^{−y/2}H(⌊ξ/λ⌋), ξ = e^{−y}.
- Teorema 1.1 PROVED (bajo (H) de sumabilidad): núcleo exacto sin primos. Teorema 2.1 PROVED (= Thm E.1′ de la fase 199
  en la variable de cola): descomposición por razón coprima con pesos (ab)^{−1/2}H(min(M_a, M_b)) y
  (ab)^{−1/2}[2L(M) + log(ab)H(M)], M_a(y) = ⌊ξ/(λa)⌋.
- Prop. 3.1 PROVED: w(a/b) = (ab)^{−1/2} = Π_p p^{−|v_p|/2} es definida positiva en ℚ^×_{>0} (producto de núcleos de Poisson);
  D_σ(τ) = |ζ(½ + σ + iτ)|²/ζ(1 + 2σ) > 0, σ > ½.
- Teorema 3.2 PROVED (σ > ½; límite CITED): en el modelo de dilatación sin corte el cofactor es m + 2Re(ζ′/ζ)(½ + σ + iτ),
  que en σ = 0 es nulo idénticamente (identidad de símbolo, fase 199 Thm F.1).
- NO-GO PROVED (clase: productos de Schur/Hadamard de un peso local PD multiplicativo en ℚ^×_{>0} con un núcleo arquimediano
  independiente de q): con m no es ⪰ 0; con m + 2Re ζ′/ζ es nulo; el signo vive en el corte/polar, que no es de tipo producto.
- NUMERICAL: cada clase coprima indefinida; toda truncación por altura o por soporte primo negativa por O(1); la positividad
  aparece sólo con el conjunto completo de clases y el término polar es esencial.
- Resto sin firmar: K_cut := Σ_{(a,b)=1}(ab)^{−1/2}{k(z)[H(min M) − valor regularizado] − δ(z)[2(L(M) − ½log²M − γ₁) +
  log(ab)(H(M) − log M − γ)]} + polar (forma de sierra F.2 en la variable de cola).
- Siguiente paso: atacar K_cut + polar directamente (no reintentar «la sierra decide el signo en la región de transición»,
  F.2/J.3). No tomado en el bloque.

### 1.17 ROUND_026_A.md — certificado inferior asistido por computadora para λ_A más allá de ½log5
- Objeto: certificado de P47 prop:lowercert (símbolo truncado en frecuencia, bloque de Legendre, inercia de Haynsworth),
  con suelo s_∞ certificado por barrido de intervalos de s_T en [τ_N, τ_B], g = (s_∞ − s_T)1_{|τ|<τ_N}, 𝒢 = Q_Tg(D)Q_T,
  a_T(F) ≥ s_∞‖F‖² − ⟨𝒢F, F⟩, 0 ≤ 𝒢_± ≤ ω_±S_c, c = Tτ_N; positividad por Gershgorin de XSXᵀ con X ≈ L⁻¹ exacta.
- §1.1–1.4 PROVED (forma inferior, cotas de cuadratura de elipse de Bernstein, encierros de Bessel, criterio de positividad).
- §1.5 NUMERICAL: reproduce thm:log5A (par 2.5·10⁻¹², impar 3.0·10⁻¹⁰).
- Teorema 26A.1 PROVED (asistido): λ_A(1) ≥ 1.0·10⁻²³, luego λ_A(T) ≥ 1.0·10⁻²³ en 0 < T ≤ 1 (contactos {2,3,4,5,7}).
- Teorema 26A.2 PROVED (asistido): λ_A(207/200) ≥ 2·10⁻²⁶, luego en 0 < T ≤ 1.035 (última ventana antes del contacto 8).
- §3.1 PROVED (dos tamaños forzados): τ_N ≥ τ_0(T; s_∞) y dim E ≥ #{λ_j(S_c) > ½} ≈ (2/π)Tτ_0 (Ky Fan, Landau–Widom CITED).
- §3.3 NO-GO para esta máquina, no en principio (NUMERICAL): en ½log15 + 0.01 hace falta dim E ≥ 1.1·10⁵; τ_0 crece doblemente
  exponencial en T. Lo que cambiaría la clase: una cota del complemento sin suelo positivo del símbolo a toda frecuencia
  más allá de τ_N (promedio de s_T sobre ventanas de ancho ≈ π/T; Q12 de STATE_002), no intentado.
- Sin falsificadores (es certificado de ventana). Sin «siguiente paso» explícito al final. Dentro del rango citado.

### 1.18 ROUND_027_A.md — ¿es el vector de pesos del peine el maximizador global de μ_T?
- Objeto: μ_T(v) = fondo de Arch − Σ_n v_nΠ_n en P_T, v ∈ ℝ^{N_T}, cóncava (P47 lem:degen), μ_T(v_T(Λ)) = λ_A(T); hipótesis
  (A) v_T(Λ) = argmax μ_T y (B) existe v̂ explícito con μ_T(v̂) ≥ 0.
- NUMERICAL: fondo simple en T = 0.8, 1.0, 1.2, gradiente g = (c_{F*}(log n))_n ≠ 0, luego 0 ∉ ∂μ_T(v_T(Λ));
  M_{0.8} = 0.04735, maximizador v* = (0.0843, −0.858, −1.820)·v_T(Λ); M_{1.0} = 0.02968 con fondo séxtuple.
- NO-GO NUMERICAL (con mecanismo PROVED de lem:degen; clase: maximización cóncava global del fondo sobre vectores de pesos
  en las posiciones log 𝒩_T). μ_T no depende del peine; v* no separa el peine de los falsificadores.
- Nada nuevo probado. Siguiente paso: ninguno; una variante restringida (v ≥ 0, o conjunto que separe falsificadores)
  necesitaría su propia razón.

### 1.19 SQUARE_COMPLETENESS_AUDIT.md — auditoría de la completitud parcial en potencias perfectas
- Objeto: auditoría literal de SQUARE_COMPLETENESS_OBSTRUCTION §§1–11 (familia F_p = (1 + c_pz)/(1 − z²), 0 ≤ c_p ≤ 1;
  exponente fijo F_m = ζ(1 − 2^{−s})/(1 − 2^{−ms}); miembro simultáneo con factor local en 2 (1 − z/2 + z²/2)/(1 − z);
  reparación del residuo con P_δ = 1 + δz − δz²).
- Aprueba (sin ejecución nueva): N(n²) = 1, coeficientes logarítmicos ≥ 0, testigo primitivo de ROUND_007_C con
  W_{a3}/‖F‖² ≤ −0.50528; W_nuevo = W_{a3} − 2log2·C_F(log 4) < 0; residuo exacto 1 dentro del ansatz fuerza c_p = 1;
  exponente m ≥ 3 da W_m = W_{a3} < 0; miembro simultáneo con W_nuevo < −0.00528‖F‖²; identificación entera §10 correcta;
  reparación del residuo §11 correcta (N(2) = ½ no entero, N(p) > 1 en primos compensadores).
- Alcance registrado: falsificador de la clase DECLARADA (completitud en cuadrados / en todas las potencias con los requisitos
  declarados), no exclusión global de todo uso de cuadrados; no prueba de signo para Λ. El extremo 2 → 4 ya figuraba en
  R163_102 Cor F / R163_191.
- Sin siguiente paso; «no quedan auditorías pendientes».

### 1.20 SQUARE_COMPLETENESS_OBSTRUCTION.md — completitud en cuadrados y potencias perfectas: falsificadores de suficiencia
- Objeto: forma primitiva de fondo arquimediano fijo con pesos v_n = 2ℓ(n)/√n (ROUND_007_C/P47); familias de Euler
  F_p(z) = (1 + c_pz)/(1 − z²) (§2), F_square = ζ(s)/(1 + 2^{−s}) (§3), F_m = ζ(s)(1 − 2^{−s})/(1 − 2^{−ms}) (§8),
  F_all = ζ(s)[1 − 2^{−s}/2 + 2^{−2s}/2] (§9), F_norm = ζ(s)R(s) con factores altos (1 + δz − δz²)/(1 − z) (§11).
- §2 PROVED: N_c(n²) = 1 para todo n, 0 ≤ N_c ≤ 1, ℓ_c(p^k)/log p = c_p^k (k impar), 2 − c_p^k (k par), ℓ_c ≥ 0.
- §5 PROVED (analítico): C_F(log 4) > 0 sobre el testigo certificado de ROUND_007_C (T₀ = ½log5 + 10⁻⁴, x > 1).
- §6 PROVED (transferencia del certificado CERT007 ≤ −0.50528): a^{ℓ_square}_{T₀}(F) < −0.50528‖F‖²; falsificador de la suficiencia
  de {ℓ ≥ 0, soporte en potencias de primos, N multiplicativa, 0 ≤ N ≤ 1, N(n²) = 1, polo simple con residuo positivo no
  impuesto 1}; negativo para todo T ≥ T₀.
- §7 PROVED: dentro de ESTE ansatz, residuo exacto 1 fuerza c_p = 1 para todo p (identificación, no signo).
- §8 PROVED: para cada m ≥ 2 fijo, N(n^m) = 1 no basta (m ≥ 3: W_m = W_{a3} ≤ −0.50528‖F‖²; residuo 1/[2(1 − 2^{−m})]).
- §9 PROVED: ALL-POWERS simultáneo con N(2) = ½ no entero, ℓ ≥ 0 (raíces r_± = (1 ± i√7)/4): a < −0.00528‖F‖²; residuo 7/8.
- §10 PROVED (identificación, no NO-GO): N multiplicativa, N(n^m) = 1 ∀m ≥ 2, N(p) entero ≥ 0, ℓ ≥ 0 ⇒ N ≡ 1, ℓ = Λ.
- §11 PROVED: residuo exacto 1, conteo x + O(1), N ≥ 0 multiplicativa acotada por C, ALL-POWERS, ℓ ≥ 0 tampoco bastan
  (primos compensadores ≥ 7 invisibles al testigo; N(p) > 1 en ellos, N(2) = ½).
- NO-GO (clase declarada: completitud parcial en cuadrados / potencias fijas / todas las potencias, con las hipótesis
  positivas escritas, sin integridad ni N ≤ 1 ni ecuación funcional): falsificadores explícitos. No excluye todo uso de
  completitud parcial; no toca Λ.
- Reapertura implícita: una hipótesis adicional que excluya ℓ_square/ℓ_all/ℓ_norm (integridad, N ≤ 1, compatibilidad
  funcional) especificada y probada por separado; con integridad + ALL-POWERS + ℓ ≥ 0 el dato queda identificado (§10).
- Sin «siguiente paso» (memo de clausura).

### 1.21 STATE_001.md — estado de la fase tras las rondas 1–3 (con anexo de ronda 4)
- Objeto: síntesis. Formas reducidas de (★): (L2) S_{T,k} ⪰ 0; (S) 𝔸_M = Arch_M − Div_M − Near_M ⪰ 0; (B) B definida positiva
  y forma de Chebyshev suavizada; banda 2×2 |B(d)| ≤ B(0) (necesaria); (L2′) con desplazamiento α y gauge c (dim 11 en
  ½log5 + ε, 41 en T = 1, NUMERICAL); división Candidate-I (★) ⟺ Θ_T ≥ 0 ∧ 1 ∈ J_T; cono 𝒦_T; supresión de Schur t*_M = 0.
- PROVED (tabla P1–P35, con veredictos de revisión): P1 m = 2θ′ y signo del peine como truncación de +2Re ζ′/ζ; P2–P5
  (Lema 1, Thm 1 de ROUND_001_A); P7 lema radical e identidad de media recta sin ceros (σ₂ ∈ (−½, 0)); P8 defecto
  𝒲^w = 𝒲 + 𝒫_{Λ−w}; P9 sin vector radical común para c ≠ 1; P10 (último paso ARGUED); P11 positividad de celda para w ≤ Λ;
  P12; P14–P15 (L2′); P16 el signo no es función de las muestras de bloque; P17 germen de B en 0 libre de peine; P18 Lema P;
  P19 Thm F (suelo de coercividad); P20 Prop S/L; P21 Prop M (muestra profunda ⇒ casi coincidencia n′^{q_n} ≈ n^{q_{n′}});
  P22–P23 parte coherente del peine monótona y PSD; P24 Thm 1 de ROUND_002_D; P25; P26; P28 (ROUND_003_B, alcance
  reducido); P32–P35 (ROUND_003_A, sin revisar); P29 cuadrados aritméticos en (½log2, ½log3) ⟺ λ^{∞,P}_min(T) ≥ √2log2;
  P30; P31. CONDITIONAL: P6, P13, P27; DOWNGRADES registrados (Q_M ARGUED, Prop 2.3 ARGUED, etc.).
- NO-GO (§3): C1 familia suave s_w (ARGUED); positividad de celda como paso completo; lectura fusionada (ARGUED); bordes de capa
  (residuo vacío); C5 criterios sólo por momentos (germen de B) PROVED; C3 desigualdades de Schur sólo con suelo (NUMERICAL);
  C2 dependencia del peine en el sector prolato (ARGUED, asintótico); C9 dos prescripciones concretas de Schur (división,
  Div/Near) PROVED con alcance reducido; C10 dominado por C8; Candidate I como paso universal PIVOT.
- Anexo ronda 4: NO-GO (Prop B PROVED): ninguna condición en un subespacio finito Λ-libre fijo con margen positivo puede
  llevar el signo (sobrevive cambios pequeños y cΛ); el objeto siguiente debe tener dimensión creciente con T.
- Correcciones a P47 (12 ítems; aplicar sólo al cierre): eq:coer-sandwich, normalización de F_0, prop:H, §ext-constraints,
  rem:directbound, thm:nyq-schur(ii), etiquetas, thm:ext-half, signo del peine, rango de σ₂, término K3, lectura de ROUND_001_C §4.
- Abierto (§5.5): (a) Θ_T(Λ) ≥ 0 (forma de Lévy ≥ 0 en la cuádrica nula del peine); (b) 1 ∈ J_T; (c) mecanismo que produzca
  el par casi degenerado; (P1) segundo autovalor par casi nulo; (P2) Π indefinida en el par par.
- §6 candidatos con primer lema (ver §D): C11/C8, C3, forma exterior a baja frecuencia de Mellin, C6, C4, C7, P6.
- Veredicto: nada cambia el estado de (★).

### 1.22 STATE_002.md — estado de la fase tras las rondas 5–20 (veredictos de REVIEW_004–010)
- Objeto: síntesis. Reformulaciones R1–R16: E_T (bloque de Nyquist + respuestas del peine) R1 PROVED; presupuesto de signo
  a_T = σ_T‖F‖² + κ − ℛ (σ_T > 0 sólo para T < 0.0520) R2; (L2′) con dos parámetros R3; reducción de banda (HR)(a) R4
  (necesidad PROVED); forma cerrada sin matriz R5; conteos de Weyl R6; ley de margen e índice R7; ley prolata de índice 8
  R8; regla de selección de Fourier R9; identidad radical/media recta R10 («único insumo Λ-específico de toda ruta»);
  forma de colas R11; reducción de colas R12; formulación nula del peine R13; división (A) + (B_δ, s) R14; Neumann/Schur
  R15 (CONDITIONAL a (H₋)); funcional de Schur del superviviente R16.
- PROVED Q1–Q27 (con alcance): Q1 falsificadores certificados (a_3 y Beurling 3 → 3.2 negativos en ½log5 + 10⁻⁴ y todo T
  mayor; 1.1Λ negativo en T = 1); Q2 cota superior λ_A(T) ≤ 3.2·10²³N^{33/2}e^{−2πN} (N ≥ 1.6·10⁶, dado thm:ext-half);
  Q3 primera celda; Q4 tres celdas; Q5–Q27 según la tabla (Q7, Q8 CONDITIONAL; Q11 valor rebajado; Q13 reformulación).
- NO-GO N1–N26 (clase y estado): N1 Krylov a grado acotado; N2 Schur sólo-suelo sobre ampliaciones; N3 mecanismos de identidad en
  E_T (Selberg, factores de Euler locales, núcleo de Lévy) PROVED; N4 transformación de estado fundamental (ARGUED); N5 familias
  homogéneas de palabras en {M, Π_P} PROVED; N6 cotas de Weyl desde Arch − θ; N7 presupuestos por minimizante; N8 Neumann de
  grado finito; N9 Grönwall en T (𝒦_H); N10 PEψ₀ solo; N11 clase 𝒦_S de masa del peine; N12 Logvinenko–Sereda/Kovrijkine;
  N13 ensamblajes de Schur de dos y tres bloques; N14 cota trivial de perfil fijo, paquetes cortos, MV + Sobolev para (U);
  N15 Vaughan/Heath-Brown + proceso B (clase 𝒱); N16 símbolo en eje de índices en unidades D; N17–N26 (rondas 18–24, ver
  entradas 1.5–1.15).
- NUMERICAL: tabla λ_A (Galerkin) de ½log3 a 1.5; ley −ln λ_A ≈ c₁e^{2T} + c₂T + c₃, c₁ → 4π por arriba; ley κ₈; márgenes
  de paquete; anomalía de T = 1.5 resuelta; tres celdas a 0.8–1.6 % del umbral; libro del superviviente.
- Mapa del obstáculo (§5): toda ruta termina en (a) enunciado genérico en el peine o (b) reformulación cuyo contenido
  Λ-específico es exactamente R10, usado siempre como identidad, nunca como desigualdad.
- Objetivos abiertos en orden (ver §C/§D): (B_δ, s); uniformidad en R con banda cuantitativa; (HB_η) uniforme en T;
  (ii_s); (H₋) y (EB_C); mitad inferior de prob:ext-L y (HR) en ℓ_g.
- Correcciones a P47 añadidas 8–13. Veredicto: estado de (★) sin cambios.

### 1.23 STATEMENT_001.md — enunciado de registro de la fase
- Objeto: a_T(F) = (1/2π)∫s_T|F̂|², s_T = m − Σ_{log n<2T}v_n cos(τ log n), P_T = {A(F) = B(F) = 0}, λ_A(T); forma de Lévy
  K(u) = 1/(2sinh(u/2)) + 1/(2cosh(u/2)), C_0 = ψ(¼) − log π = −5.3721834…; perfil único F_0 = (¼ − ∂²)G_0 y función B(d);
  matrices 𝔸_M = [B(log m − log k)] = Arch_M − Div_M − Near_M (2T_0 < log 2).
- PROVED (citado de P47): forma de Lévy (lem:K, thm:A); continuidad y monotonía no creciente de λ_A; thm:oneprofile ((★) ⟺ B
  definida positiva); prop:AM ((★) ⟺ 𝔸_M ⪰ 0 ∀M); banda 2×2 |B(d)| ≤ B(0) necesaria (Bochner). CITED: forma de fluctuación de
  Chebyshev suavizada B(log x) = −x^{−1/2}ΣΛ(n)φ(n/x) − Σ_{j≥1}γ_jx^{−(2j+½)}, ∫φ = ∫φ/y = 0. NUMERICAL: B(0) = 0.01492,
  |B(d)| ≤ 0.0122 en 0 < d ≤ 13 (a = 0.15, b = 1).
- Estado declarado: PROVED (certificado) T ≤ ½log5; CITED T ≤ ½log15 y T ≤ 17/16 (preprint); OPEN más allá.
- §4 requisitos (i)–(vi) del paso de signo y cláusula abierta (objeto que acople (Λ(n))_{n<N} con la ecuación funcional por
  una vía distinta del factor común ζ(½ + iτ)); §5 reformulaciones internas permitidas ((L2), (N), (S), (B), Kreĭn, fuga).
- No es memo de construcción: sin teoremas nuevos, sin NO-GO, sin siguiente paso.

### 1.24 SURVEY_001.md — auditoría de los Papers 01–42 como caja de herramientas para a_T
- Objeto: lectura de 42 papers anteriores buscando técnicas reutilizables sobre a_T, S_{T,k} y la matriz Toeplitz
  [Ξ_{F0}(log(m/k))] de (S). Etiquetas por paper (PROVED/CITED/CONDITIONAL/NUMERICAL/ARGUED de cada fuente).
- Descartes registrados (familias cerradas del índice, no proponer): Papers 01–06, 08, 10, 11, 13, 14, 16 (lado espectral,
  excluido), 17, 18, 19 (condicional a una hipótesis sin análogo), 21, 23, 25, 27, 28, 30, 31, 32, 33, 34, 37, 40, 41, 42; Paper 12
  como palanca (NO-GO: sin margen aritmético por limitación de banda sola).
- Top 10 nunca aplicados al objeto finito (ver §D): (1) P26 álgebra Weil–Toeplitz/corona y símbolo σ(Q); (2) P38
  coercividad de ventanas adyacentes |H_L|² + |H_{L+1}|² ≥ ½|z|^{2L}; (3) P39 defecto de transporte exacto (dos canales de
  rango uno + integral doble de operadores); (4) P07 thm:trunc η(X) ≤ A exp(−α(log X)²); (5) P22 determinación de Carleman;
  (6) P15 thm:crit (positividad eventual → uniforme); (7) P24 medida de dominancia (analogía); (8) P09 thm:concave
  (reducción a puntos extremos de cajas de coeficientes); (9) P35 cota de curvatura de Bakry–Émery de la parte prima tras
  conjugación de Doob; (10) P36 thm:mirror-criterion y nodos H1–H5 (cotejo de una ronda).
- Ningún teorema propio; sin falsificadores; sin siguiente paso salvo la lista.

### 1.25 TOOL_001_GALERKIN_MP.md — motor de Galerkin multiprecisión para a_T
- Objeto: base de N senos de Dirichlet en (−T, T), Arch por forma de Lévy (tres momentos de K en [0, 2T] + cola cerrada),
  Π (peine verdadero o suministrado), A, B, proyector sobre P_T, fondos por paridad, Θ_T = max_μ λ_min(Arch − μΠ) y c*.
- Todo NUMERICAL (cotas superiores de λ_A). Validación: ½log3 1.008·10⁻³; log 2 1.1137·10⁻⁷; ½log5 + 10⁻³ 3.088·10⁻¹²;
  0.9 6.03·10⁻¹⁷ (el valor doble 4.5·10⁻¹⁵ era redondeo). T = 1.0: 1.74·10⁻²³ (N = 120); T = 1.2, 1.4 no convergidos en N
  (cotas superiores; 1.26·10⁻⁴¹, 5.67·10⁻⁶⁵ a 80 dígitos).
- Lecturas: fondo par siempre; impar 10²–10³ más alto; racimo casi nulo 7, 14, 20–25 (T = 1.0, 1.2, 1.4); cor:margin1 sin
  contenido para T ≤ 1.4; Θ_T con c* = 1 a 10⁻³⁰ para T ≥ 1.2 (máximo en μ es un pliegue: tolerancia fina obligatoria; una
  corrida con tolerancia 10⁻¹² dio Θ < 0 espurio, descartada).
- Límites: sin aritmética de intervalos; convergencia en N no alcanzada para T ≥ 1.2. Sin siguiente paso formal.

## A. Lista deduplicada «no reintentar» de estos archivos, con condición de reapertura

Marca: [AUSENTE] no figura en `RULES_AVOID.md`; [IMPRECISO] figura con un enunciado que no coincide con la fuente
(se citan ambos); [PRESENTE] figura de forma compatible.

A1. Omitir el término polar 2A(Ψ)B(Ψ) en la forma de colas o en problemas límite de celdas (ROUND_016_B §3.1, «recorded
    so that no later round drops it»). Sin reapertura: es un error, no una ruta. [AUSENTE]
A2. Suelo uniforme en K del bloque alto en unidades D; símbolo en el eje de índices con error de banda/Toeplitz en unidades
    D (ROUND_016_B §4(i); STATE_002 N16). Reapertura: normalizar por la fuga de cociente de gauge ℓ_g completa (barridos
    normalizados en ℓ_g no cubiertos por el NO-GO). [AUSENTE]
A3. Atribuir la deriva del bloque alto al salto en x = −T, a los pares de chirps no resonantes (régimen MV) o al peine
    resonante (ROUND_016_B §1.3). Sin reapertura (falsos medidos). [AUSENTE]
A4. Transferir la constante de primera celda μ₄ por lema de transferencia a vectores con defecto de restricción δ ≥ 0.075
    (ROUND_018_A §1; «the fix is not a better transfer lemma but exact constraints»). Reapertura: restricciones exactas
    sobre todo el F₁. [AUSENTE]
A5. Constante κ_R uniforme en R para la forma completa de R celdas contra ℓ_g en la clase idealizada con restricciones
    transportadas (ROUND_018_A Thm 4.1(iii); ROUND_019_A; STATE_002 N17). Reapertura: limitación de banda cuantitativa con
    penalización μβ y un argumento de que la celda R+1 sólo crea direcciones casi nulas con β/ℓ_g ≳ 1, más (LB_μ) en el
    bloque bajo. [AUSENTE]
A6. Limitación de banda cualitativa («u es restricción de una función de tipo 2πλ») o cota absoluta β ≤ ε‖F‖² como
    restricción en datos de R celdas (ROUND_019_A Prop 1.1, §3.2(c)): densa, no impone nada. Sin reapertura en esa forma.
    [AUSENTE]
A7. Desigualdad de peldaños (R) de la desigualdad de Schur del superviviente como portadora de signo (Gram 2×2 de colas con
    peso colapsado log N) (ROUND_018_B; STATE_002 N18): sobrevive c ∈ [0, 3.5]. Sin reapertura salvo mecanismo Λ-específico
    distinto de R10. [AUSENTE]
A8. Cotas «coercividad arquimediana vence al peine que solapa» / 𝒜𝒫 − c𝒞 ≥ 0 sobre toda la clase de colas admisibles para
    c ≠ 1 (ROUND_019_B Cor 2.3; N19), incluida la prueba «cruda» (decaimiento más allá de la primera celda + cota de Schur
    del peine + m_eff > κ). Reapertura: sólo usando la identidad radical en las direcciones de gauge (c = 1 exacto).
    [PRESENTE, IMPRECISO] RULES_AVOID D17: «𝒜𝒫 − c𝒞 con c ≠ 1» — la fuente precisa «on the class of admissible tails …
    unbounded below for c < 1 and for c > 1»; sobre un representante fijo (prolato) sí vale para c ∈ [0, 3.5] (18B), y
    D17 no distingue clase de representante.
A9. Elegir «el representante adecuado» de cada fibra de gauge con positividad robusta al peine (versión existencial) y la
    variante por S-lema con multiplicador ≠ 1 (ROUND_020_A Thm 1.3, Thm 1.5; N20): es (★) exactamente. Sin reapertura.
    [PRESENTE parcialmente] D8 «colas con gauge — sólo con hipótesis nueva que resuelva el fallo identificado»: no registra
    que la versión existencial es una reformulación exacta probada ni que el multiplicador queda fijado en 1.
A10. Secciones canónicas Λ-libres (mín ℓ, mín ∫_0^{1/λ}f², mín ‖Ψ‖²) con margen δ uniforme (ROUND_020_A §2; N21, PIVOT).
     Reapertura: que δ(w) se estabilice al refinar (w = 0.025, 0.018) o una sección en norma de cola ponderada tipo H¹ en la
     que el radical sea cerrado. [AUSENTE]
A11. Ventanas de positividad J_R en el peso del peine (uniforme, por primo, por átomo) sobre datos idealizados de R celdas
     como fuente de signo (ROUND_021_A; N22): equivalen a λ₀(R) → 0. Sin reapertura. [PRESENTE] D17 «ventanas en c».
A12. «Identidad + resto coercitivo» en datos de R celdas: tras Prop 3.2 no hay resto, Q_R = Q₀ − 𝒦_R Λ-libre (ROUND_021_A
     §3.4). [AUSENTE]
A13. Signo de R celdas como invariante de monoide; caracterización aditiva de ℕ en el rayo ℕ^{1+t}; probar ∂_tλ₀ < 0 como paso
     hacia (★) (ROUND_022_A, ROUND_023_A §5(iii); N23). Fuente: «the exponent ray should not be pursued further as a route to
     (★)». Sin reapertura. [AUSENTE]
A14. Atribuir el signo de R celdas a las restricciones transportadas por Poisson sobre ℤ (conjunto de sumación) (ROUND_022_A
     §2.3). [AUSENTE]
A15. Cualquier enunciado a R fijo (o subespacio finito Λ-libre fijo con margen) como paso de signo (ROUND_019_A §5.1; STATE_001
     anexo ronda 4, Prop B). Reapertura: dimensión creciente con T / uniformidad en R. [PRESENTE] D17 «planos Λ-libres E_k»
     (sólo los planos, no la invariancia general de §5.1).
A16. Finitas relaciones de piso de Chebyshev estrictas a la truncación exacta (ROUND_024_A Prop 2.1; N24, CONDITIONAL al ancho
     numérico de J_T según REVIEW_010). Reapertura: ninguna; sin holgura es R10. [AUSENTE]
A17. Propagar positividad a través de las entradas de contactos a lo largo de N (ROUND_024_A §4; N25). Reapertura: una cota
     inferior de la tasa total de descenso (EB_C). [AUSENTE] (RULES_AVOID C1 menciona «Grönwall» del programa L♯; no esta
     clase.)
A18. Extremalidad prolata con conteo de índice 8 como principio variacional (ROUND_024_A diseño C; N26, ARGUED): reintento
     de L′/L′♯. [AUSENTE como tal]
A19. Productos de Schur/Hadamard de peso local PD multiplicativo en ℚ^×_{>0} con núcleo arquimediano independiente de q;
     sumas de cuadrados por clases de razón coprima; truncaciones por altura o por soporte primo (ROUND_025_B; también fase
     199 E.5). Reapertura: trabajar sobre K_cut + polar directamente (sin «la sierra decide el signo en la región de
     transición», F.2/J.3). [AUSENTE]
A20. Maximización cóncava global del fondo μ_T(v) sobre vectores de pesos en las posiciones log 𝒩_T (ROUND_027_A).
     Reapertura: una variante restringida (v ≥ 0 o conjunto que separe falsificadores) con razón propia. [AUSENTE]
A21. Completitud parcial en cuadrados, en potencias de orden fijo m o en todas las potencias, con las hipótesis positivas
     escritas (SQUARE_COMPLETENESS_OBSTRUCTION §§6, 8, 9, 11). Reapertura: hipótesis adicional que excluya los ejemplos,
     especificada y probada (integridad, N ≤ 1, compatibilidad funcional); con integridad + todas las potencias + ℓ ≥ 0 el
     dato queda identificado (§10), lo que no es signo. [IMPRECISO] RULES_AVOID D14: «la integralidad identifica, no firma;
     los falsificadores de potencias valen también sin integralidad». Fuente: los falsificadores de orden FIJO (F_square, F_m)
     tienen N ∈ {0, 1}, es decir valen CON integridad; el de todas las potencias simultáneas (F_all, F_norm) necesita
     N(2) = ½ no entero; la identificación exige integridad + todas las potencias + ℓ ≥ 0. Falta además §11: residuo
     exacto 1 y conteo x + O(1) tampoco bastan.
A22. Localizadores baratos de mínimos del margen de banda: función de tono g_T, bloque denso k ≤ 96, diagonal, alineación de
     primos pequeños h₄ (ROUND_017_B §2.3; ROUND_021_B; «not reused as a shortcut»); Lanczos con arranque tibio puro.
     Reapertura: localizador certificado por cota de Lipschitz en τ (ROUND_022_B). [AUSENTE] (operativo, no matemático)
A23. Certificados inferiores de la clase de P47 prop:lowercert (suelo constante del símbolo) más allá del contacto 8 en la
     máquina disponible (ROUND_026_A §3.3; NO-GO de máquina, no de principio). Reapertura: cota del complemento sin suelo
     positivo a toda frecuencia (promedio de s_T en ventanas de ancho π/T). [AUSENTE]
A24. De STATE_001 (rondas 1–3): C1 familia suave s_w (ARGUED) [PRESENTE D8]; C5 criterios sólo por momentos de la medida
     representante (germen de B) [PRESENTE C1 «criterios de germen de Carleman»]; C3 Schur sólo-suelo [PRESENTE D17]; C2 sector
     prolato monótono (ARGUED, asintótico) [AUSENTE]; C9 prescripciones división y Div/Near de la factorización de Schur
     (PROVED, alcance reducido) [AUSENTE: D8 cita «Arch − Div − Near por Poisson/divisores», otra cosa]; positividad de celda
     como paso completo [AUSENTE].
A25. De STATE_002 (rondas 5–16, no cubiertas arriba): N3 mecanismos de identidad en E_T (Selberg, factores de Euler locales,
     núcleo de Lévy) PROVED [IMPRECISO: B1 cita «identidades tipo Selberg NODE_001», otra fuente; N3 de 211 no figura]; N4
     transformación de estado fundamental / Poincaré pesado 𝒦_gap (ARGUED) [AUSENTE]; N7 presupuestos por minimizante
     [AUSENTE]; N8 Neumann de grado finito [AUSENTE]; N9 Grönwall en T (𝒦_H) [PRESENTE parcial]; N10 PEψ₀ solo [AUSENTE];
     N11 clase 𝒦_S de masa del peine [AUSENTE]; N12 Logvinenko–Sereda/Kovrijkine y momentos bajo log τ ≈ 8T² [AUSENTE];
     N14 cota trivial de perfil fijo, paquetes cortos, MV + Sobolev para (U) [AUSENTE]; N1, N2, N5, N6, N13, N15 [PRESENTES en D17].

## B. Resultados positivos PROVED, con alcance exacto

B1. Lema 2.1/2.2 de ROUND_016_B: F_N = N^{−1/2}τ_{log N}F₁, forma de colas independiente de T en F₁; primera celda sin peine
    (u en (λ, 2λ) ⇒ 𝒲[𝒯u] = 𝒜_∞[F₁]). Λ-ciegos.
B2. ROUND_017_C Teorema 3.1 (asistido, aritmética de bolas): toda ventana de longitud log 2, ∫F e^{−y/2} = 0 ⇒
    (1/2π)∫m|F̂|² ≥ 0.069611‖F‖² (independiente de T); Cor 3.2 forma completa ≥ μ₀ en {B = 0}; Teorema 3.3 con cuatro
    funcionales transportados, μ₄(0.8) ≥ 0.527631, μ₄(1.0) ≥ 0.549417 (puntual en T). Herramienta: Lemas 2.1–2.4 (símbolo
    monótono, truncación, compresión polinómica con cola HS, cota con restricciones).
B3. ROUND_018_A: Lema 1.1 (transferencia por seminorma); Lemas 3.2–3.3; Teorema 3.4: Q₃ ≥ 0.70·ℓ_g en V₃, T ∈ {0.8, 1.0}
    (asistido); ROUND_019_A §5.2: Q₃ ≥ 0.60ℓ_g con c₂ = 0 (T = 0.8, 1.0), ≥ 0.20ℓ_g con c₂ = 1.01 (T = 0.8). Coercividad, no signo.
B4. ROUND_019_A Prop 1.1 (densidad de restricciones de Paley–Wiener en la norma de forma) y Lema 2.1 (defecto de banda).
B5. ROUND_017_A Props 1.1–1.3, 3.1 (forma de Schur/secular; b = ∫h_G dν, b_Tate ≡ 0; identidad radical de segundo nivel en
    imágenes E; defecto radical X_w bajo cΛ, a_P, e) — PROVED para datos con f(λ) = 0; superviviente ARGUED.
B6. ROUND_018_B Lemas 1.1–1.2 (peso colapsado c log N = 𝒜_∞ − c𝒞 + 𝒯 en colas; Schur 2×2 = determinante).
B7. ROUND_017_B Prop 1.1: forma cerrada A_τ^{(η)} = ½(𝔈 + 𝔈ᵀ), 2T𝔈 = CS − ESCE + ESHE + HS + Dd (cualquier peso real).
B8. ROUND_019_B Prop 1.1/Cor 1.2 (E(admisibles) ⊇ C_c^∞(I_T) ∩ P_T; (★) ⟺ 𝒲̂ ≥ 0 en imágenes E del núcleo); Teorema 2.1
    (radicales de gauge con 𝒜𝒫 → −11.457‖η‖² y → +1.114‖η‖², sin ceros); Cor 2.2 (𝒲̂^c no acotada inferiormente en cada fibra,
    c ≠ 1).
B9. ROUND_020_A Lemas 1.1–1.2, Teorema 1.3, Cor 1.4 ((★) ⟺ 𝒜𝒫 ≥ 0 en V_T ∩ {𝒞 = 0}), Teorema 1.5 (secciones finitas).
B10. ROUND_021_A §3.1 y Prop 3.2: Φ_R homomorfismo de la convolución de Dirichlet truncada a desplazamientos comprimidos,
     [M_x, Φ_R(α)] = Φ_R(α log); P_w𝔇_R = [M_x, 𝔇_R] ⟺ w ≡ 1; Q_R^{(c)} = Q₀ − c𝒦_R; Lema 1.1 (ventanas intervalos);
     §2.1 (ventanas de Galerkin exteriores); Lema 3.3 (sándwich). ROUND_022_A Lema 3.1 (todo sistema multiplicativo) y
     Prop 3.2 (primeras variaciones). ROUND_023_A Lema 2.1 (Φ(Λ log) = [M, P] = 𝔇⁻¹[M,[M,𝔇]] − P²), Props 2.2–2.4 (2.4 debe
     incluir los funcionales polares, REVIEW_010), Lema 4.1, fórmula 2×2.
B11. ROUND_024_A Lemas 4.1–4.2, Prop 4.3 (ley de entrada), Cor 4.4(i); Prop 2.1 (pisos estrictos abiertos en c).
B12. ROUND_025_B Teorema 1.1 (núcleo sin primos K_ℕ bajo (H)), Teorema 2.1, Prop 3.1 ((ab)^{−1/2} PD en ℚ^×_{>0}), Teorema 3.2
     (cofactor nulo en σ = 0, cita del símbolo).
B13. ROUND_026_A Teoremas 26A.1 y 26A.2 (asistidos): λ_A(T) ≥ 1.0·10⁻²³ para T ≤ 1; λ_A(T) ≥ 2·10⁻²⁶ para T ≤ 1.035. Dentro del
     rango citado; amplía el rango certificado propio desde ½log5. §3.1 cotas de tamaño forzadas de la clase.
B14. SQUARE_COMPLETENESS_OBSTRUCTION §§2, 5–11: identidades algebraicas de las familias, C_F(log 4) > 0 analítico, falsificadores
     PROVED de las clases declaradas; §10 identificación por integridad + todas las potencias + ℓ ≥ 0.
B15. Heredados en STATE_001/STATE_002 (rondas 1–16, ya registrados en anexos previos): P1–P35, Q1–Q27; en particular Q1
     (falsificadores certificados a_3, Beurling 3 → 3.2, 1.1Λ) y Q2 (cota superior doblemente exponencial dado thm:ext-half).

## C. Obligaciones abiertas (enunciado matemático preciso y lo intentado)

C1. (HR_g): existe κ_T > 0 independiente de K con 𝒢[b] ≥ κ_Tℓ_g^S[b] para todo b ∈ S𝒜 sobre índices altos (ROUND_016_B §4).
    Intentado: primera celda (17C), tres celdas (18A), R celdas idealizadas (colapso R ≥ 5), banda (19A).
C2. H_band(μ, κ): para todo R ≥ 2 y F ∈ V_R, Q_R[F] + μβ[F] ≥ κℓ_g[F]; junto con H_lim y (LB_μ): la parte en banda de la forma
    completa domina μ‖ℱf‖²_{L²(0,λ)} en admisibles módulo gauge (ROUND_019_A Thm 4.1, §4). Intentado: numérico R ≤ 8; certificado
    sólo R = 2, 3 con μ = 0.
C3. (ii_s) / (B_δ, s): para una sección lineal Λ-libre s, 𝒲̂ ≥ δ|𝒞| en Ran s (ROUND_019_B, ROUND_020_A §3). Intentado: tres
    secciones, δ decreciente con la resolución.
C4. Balance de Schur del superviviente exacto y pieza de paridad (P): decidir si (P) tiene forma de cola robusta al peine
    (ROUND_017_A, ROUND_018_B siguiente paso). Intentado: peldaños (robustos), imágenes E de prolatos ψ_0…ψ_40 (no alcanzan (P)).
C5. Q₀ − 𝒦_R ≥ 0 en V_R para todo R (forma Λ-libre de R celdas, ROUND_021_A §3.4(iii)), con λ₀(R) ~ exp(−2.9R log R)
    numérico; y si la dirección casi nula es la 𝔇_R-preimagen del fondo de 𝒜 − Π en la ventana.
C6. Signo de ∂_tQ en el racimo casi nulo y si ∂_tλ₀ → −1 (ROUND_022_A, 023_A) — declarado inútil para (★).
C7. (EB_C): cota inferior de la tasa total de descenso de λ_A a lo largo de N (≤ 8πe^{2T}hλ_A en P211-8C); (R_edge) (fondo
    simple, continuidad en el borde) para Cor 4.4(ii) (ROUND_024_A).
C8. K_cut + polar ⪰ 0 (resto de corte de sierra de Thm 2.1 de ROUND_025_B en la variable de cola).
C9. (HB_η) uniforme en T con lema de término cruzado; cobertura del margen de banda en [1.2, 3]·2πN (T = 3.5), [1.11, 3]·2πN
    (T = 4), franja r ∈ [1.1, 1.3] (T ≥ 4) (ROUND_017_B, 021_B, 022_B). Pieza genérica para c < 1.
C10. Cota del complemento en certificados inferiores sin suelo positivo de símbolo (promedio de s_T sobre ventanas π/T; Q12
     probado sólo T ≤ log 2) (ROUND_026_A §3.3).
C11. De STATE_001 §5.5: Θ_T(Λ) ≥ 0 (forma de Lévy ≥ 0 en la cuádrica {F ∈ P_T : Σv_n Re c_F(log n) = 0}); 1 ∈ J_T; (P1) segundo
     autovalor par casi nulo y (P2) Π indefinida en el par par, desde los Λ(n) exactos; simplicidad del fondo.
C12. De STATE_002 §5: (H₋) para la expansión de Neumann; mitad inferior de prob:ext-L (rango prolato intermedio 10 ≲ k ≲ 4N);
     (HR) en normalización ℓ_g completa.
C13. P6 (STATE_001): cota o(M) del resto para la condición necesaria 𝒜(w) ≥ 0 fuera de P_{T′}.

## D. Objetos, pasos siguientes o ideas nombrados y nunca retomados

Siguientes pasos de memos no tomados por ningún archivo del rango: ROUND_016_B (ℓ_g con gauge resuelto MIN ≥ 30, Nb ≥ 370);
ROUND_017_A (en parte tomado por 18B); ROUND_017_B (cobertura y localizador por fases p ≤ 13); ROUND_017_C/018_A (multicelda R = 4
con penalización μ(1 − B_R), cinco piezas, desplazamientos log 2, log 3; falsificadores (b)–(d) sobre Thm 3.4: (b) hecho en 19A);
ROUND_018_B (paridad (P) por preimagen de Möbius); ROUND_019_A ((LB_μ) para μ = 10², 10⁴, 10⁶; certificado H_band en R = 4);
ROUND_019_B (sección que minimiza la fuga, c ∈ [0.5, 2], rango ≥ 30); ROUND_020_A (δ(w) en w = 0.025, 0.018); ROUND_021_A
(preimagen 𝔇_R^{−1} = Φ_R(μ) del fondo de 𝒜 − Π); ROUND_021_B/022_B (franja completa; localizador por cota de Lipschitz de
λ_max(A_τ)); ROUND_022_A (sistema que preserve log-huecos hasta un tamaño y rompa una sola relación m = kn: aislar casi
coincidencias — idea nombrada, nunca ejecutada); ROUND_024_A (prueba de (R_edge) en n = 7, 8, 9); ROUND_025_B (K_cut + polar).

STATE_001 §6, candidatos con primer lema:
D1. C11/C8 par casi nulo y tangencia: probar si Π es indefinida en el plano Λ-libre E_T de los dos autovectores más bajos de
    Arch en P_T^ev y calcular el Schur 2×2 de a_T en él (si captura el pin, desigualdad 2×2 no circular en los Λ(n)). (ROUND_004_A
    trató planos E_k; Prop B cierra planos fijos con margen.)
D2. C3 continuado: A_𝒞𝒞 ⪰ R ⊕ c_floor(1 − Π) con Π proyección en span{P_𝒞Ae_k : k ∈ 𝒩} ∪ modos de W_{t_1}; requiere versión
    certificada del bloque de 11 modos.
D3. Forma exterior a baja frecuencia de Mellin: escribir ℬ_n en una base de colas admisibles de baja frecuencia y decidir si
    Σ log n·ℬ_n tiene un patrón de signo que falle para W = c log y W_{a_P}.
D4. C6 defecto de transporte M → M+1 (Paper 39) / coercividad de ventanas adyacentes (Paper 38). NOT STARTED. Primer lema:
    fórmula exacta de 𝔸_{M+1} ⪰ 0 dado 𝔸_M ≻ 0 como complemento de Schur escalar en la fila nueva B(log((M+1)/k)).
D5. C4 lente corona/símbolo (Paper 26) sobre M ↦ 𝔸_M. NOT STARTED. Primer lema: identificar el símbolo límite del campo y si
    𝔸_M − (límite) es compacto con fórmula exacta.
D6. C7 ruta N de la fase 160 (Carathéodory–Fejér de ventana finita). NOT STARTED. Primer lema: responder la objeción «muere en el
    límite» con un enunciado a T fijo.
D7. P6: cota o(M) del resto (O(M^{−7/3+ε}) basta); sólo condición necesaria.
SURVEY_001 (herramientas nunca apuntadas a los objetos finitos; sin primer lema salvo indicación):
D8. Paper 26: álgebra Weil–Toeplitz, ideal J ≅ c₀, corona W/J, símbolo σ(Q), estados de Cesàro frente a norma, sobre
    [Ξ_{F0}(log(m/k))] (= D5).
D9. Paper 38: coercividad de ventanas adyacentes |H_L|² + |H_{L+1}|² ≥ ½|z|^{2L} para el par (S_{T,k}, S_{T,k+1}) (= D4).
D10. Paper 39: defecto de transporte exacto (dos canales de rango uno de paridad opuesta + corrección por integral doble de
     operadores) y traza del segundo resolvente para S_{T,k} → S_{T,k+1} (= D4).
D11. Paper 07 thm:trunc: η(X) ≤ A exp(−α(log X)²) como estimación del margen entre contactos. (Caveat: cae en B2 de RULES_AVOID
     si se usa como cota con resto.)
D12. Paper 22: determinación de Carleman sobre la medida de s_T|F̂|² o de Near_M. (Caveat: C5 de STATE_001 y «criterios de
     germen de Carleman» de RULES_AVOID C1 cierran el uso sólo por momentos.)
D13. Paper 15 thm:crit: positividad eventual → uniforme para la torre S_{T,k} (umbral acotado / tipo finito). Nunca aplicado.
D14. Paper 24: medida de dominancia como analogía de Arch_M − Div_M − Near_M.
D15. Paper 09 thm:concave: reducción a puntos extremos de cajas de Λ(n) admisibles (relacionado, no idéntico, con ROUND_027_A).
D16. Paper 35: cota de curvatura de Bakry–Émery de la parte prima tras conjugación de Doob sobre S_{T,k}. (Caveat: Bakry–Émery
     Γ₂ figura cerrado, INV_N_001, citado en ROUND_024_A §0.)
D17. Paper 36: cotejo de una ronda de thm:mirror-criterion y nodos H1–H5 con S_{T,k}.
STATE_002 §5 (objetivos abiertos en orden): 1 (B_δ, s) — ver C3; 2 uniformidad en R con banda cuantitativa — C2; 3 (HB_η) — C9;
4 (ii_s) — C3; 5 (H₋), (EB_C) — C7, C12; 6 prob:ext-L inferior y (HR) en ℓ_g — C12. Ninguno retomado en el rango salvo (EB_C),
que ROUND_024_A identifica como el residuo y no ataca.

## E. Cobertura

Rango: `ls *.md | sort` en `../phase-211-sign-sandbox/`, desde `ROUND_016_B.md` hasta `TOOL_001_GALERKIN_MP.md` inclusive:
25 archivos (ROUND_016_B, ROUND_017_A, ROUND_017_B, ROUND_017_C, ROUND_018_A, ROUND_018_B, ROUND_019_A, ROUND_019_B,
ROUND_020_A, ROUND_021_A, ROUND_021_B, ROUND_022_A, ROUND_022_B, ROUND_023_A, ROUND_024_A, ROUND_025_B, ROUND_026_A,
ROUND_027_A, SQUARE_COMPLETENESS_AUDIT, SQUARE_COMPLETENESS_OBSTRUCTION, STATE_001, STATE_002, STATEMENT_001, SURVEY_001,
TOOL_001_GALERKIN_MP). Leídos completos: 25 de 25. Ningún archivo ni tramo sin leer. Orden: el de `sort` en la configuración
regional del sistema (STATEMENT_001 tras STATE_002). Los resúmenes de STATE_001/STATE_002 sobre rondas anteriores a
ROUND_016_B se registran tal como los dan esos archivos, sin releer las rondas fuente (cubiertas por otros anexos).
