# ROUND_024_D — Puerta: objeto de grado ≥ 2 con el Möbius del sistema μ_a y la fuga de borde

Pregunta. ¿Hay una fórmula explícita de grado ≥ 2 en el peso a, construida con μ_a (inversa de Dirichlet
de b_a, donde −ζ_a′/ζ_a = Σ a(n)n^{−s} y ζ_a = Σ b_a(n)n^{−s}) y con el salto comprimido de ROUND_023_B
  D_p := E_{p,T} − E_{p−1,T} = p^{−1/2} P_T τ_{log p}(1−P_T)𝓕Π_T,
que no sea varianza de divisores (K2), identidad de Selberg/Riccati, congruencia ni cuadrado?

Veredicto: **NO PASA (repetición en lo algebraico; sin mecanismo en lo demás).** Las fórmulas se pueden
escribir, pero cada una cae en una de las cuatro clases excluidas, y ninguna falla bajo los controles.

## (1) Antecedentes más cercanos (abiertos)

- phase-163 R163_144 §1, ec. (2): familia r_{a,u} = μ_a∗(b_a·(·)^{−u}) para peso a GENERAL; derivadas
  r′ = −a, r″ = W_a := a·log + a∗a = μ_a∗(b_a·log²). Es exactamente «grado 2 en el peso construido con
  μ_a»; §2 da positividad (6) sólo escalar en puntos Gamma; §3: no llega al núcleo físico. Índice
  maestro l.14210–14214 (registrada como ausente, falla por «positividad escalar, modelos κ igual»).
- ROUND_004_A, observación ARGUED tras (iv) y «NO excluido» 3: con μ_a, M^{(a)}S^{(a)} = I + exterior vale
  para toda la familia (patrón B1); E_N^{(a)} pierde Poisson para a ≠ Λ. REVIEW_004 l.59 (R4-b).
- R166_502 §5 (Riccati δV + V² = Z⁻¹δ²Z = Selberg; §5.2: V∗V = Σ_p V_p∗V_p + Σ_{p≠q}V_p∗V_q, el peine
  de cocientes es la parte cruzada hermítica que el álgebra de convolución no toca); fase 70 E70_10–12;
  ROUND_002_C l.31, l.111–154 (canal lineal y homogéneo: γ_{cΛ} = c·γ_Λ).
- ROUND_023_B §§2–3: el salto comprimido es a(p)·(operador fijo); orientarlo exige grado ≥ 2 (F3).
- RULES_AVOID K1 (cuadrados de fuga), K2 (varianza ½ΣΣΛ(d)Λ(e)‖m_d − m_e‖², genérica).

## (2) Lo que se puede escribir

Sea J_a := Σ_n a(n) n^{−1/2} P_T τ_{log n}(1−P_T)𝓕Π_T (suma de saltos ponderada; lineal en a).
Los objetos de grado 2 que se pueden formar con J_a, μ_a, b_a y log son, agotando los tipos de producto:

(A) Producto hermítico: ⟨J_aF, J_aF⟩ = Σ_{m,n} a(m)a(n)(mn)^{−1/2}⟨τ_{log m}C_TF, P_Tτ_{log n}C_TF⟩,
    con C_T = (1−P_T)𝓕Π_T. Es un cuadrado de fuga (R161_002 Teor. 1.1; K1); su parte fuera de la
    diagonal m ≠ n es la varianza/Gram cruzado de K2 (030–034) y la parte cruzada de R166_502 §5.2.
(B) Composición: J_a∘J_a = Σ_{m,n} a(m)a(n)(mn)^{−1/2} P_Tτ_{log m}C_T P_Tτ_{log n}C_T. Sin la compresión
    intermedia (C_T P_T → 𝓕) los traslados componen τ_{log m}τ_{log n} = τ_{log mn} y el coeficiente es
    a∗a = μ_a∗(b_a·log²) − a·log: Riccati (R163_144 (2); R166_502 §5). Con la compresión, el coeficiente
    de (m,n) depende de m y n por separado (no es función de mn): no hay identidad de convolución; es
    una forma bilineal en a sin signo escrito, y su único control conocido es (A) por Cauchy–Schwarz
    (cuadrado).
(C) Conjugación por μ_a: X ↦ M^{μ_a} X S^{(a)} (S^{(a)} con coeficientes b_a). Es una congruencia/
    semejanza (R162_903, N_BUILD_022, ROUND_022_A); su exactitud interior M^{μ_a}S^{(a)} = I + exterior
    vale para todo a (ROUND_004_A Lema 3 generalizado), luego no distingue el peso.
(D) Desarrollos de μ_a de orden superior (Faà di Bruno: μ_a∗(b_a·log^k) = polinomio en a, a·log, a∗a,…)
    son consecuencia de μ_a∗b_a = δ_1 y μ_a∗(b_a·log) = a; el único término de grado 2 nuevo en cada
    orden es otra instancia de la misma ecuación de Riccati.

No sé escribir un quinto tipo: μ_a sólo entra por convolución (C,D) y J_a por producto o composición (A,B).

## (3) Por qué no evita el motivo de fracaso

- Motivo de R163_144: W_a ≥ 0 es positividad escalar del lado Euler, válida para todo peso con medida
  de Euler positiva (modelos κ incluidos). (B) sin compresión es W_a mismo; con compresión pierde la
  estructura de convolución que daba W_a y no gana signo.
- Motivo de ROUND_004_A/B1: toda identidad construida desde μ_a vale idénticamente en a (μ_a∗b_a = δ_1
  para todo a); usar μ_a en vez de μ convierte la identidad de Λ en una identidad de familia.
- Motivo de K2/R166_502 §5.2: la parte cruzada m ≠ n (peine de cocientes m ≈ kn) no la ve el álgebra de
  convolución; (A) la ve sólo como Gram (cuadrado, sin orientación, F3).
Ningún tipo cambia la hipótesis que causó el fracaso; sólo cambian la notación (μ → μ_a) o el portador
(traslado → salto comprimido), lo que el filtro no acepta.

## (4) Conexión con 𝔸_M ⪰ 0 y controles

Identidad que haría falta (no disponible): a_T(F) = Φ_T(F) − ‖C-fugas‖² con Φ_T ≥ 0 por un término de
grado 2 en a que se anule exactamente en a = 2Λ (o Λ) y no en los controles; vía Paper 47 prop:AM daría
𝔸_M ⪰ 0 para M ≥ e^{2T}.
Pasos con nombre bajo los controles:
- peso cΛ / peso sustituido: (C),(D) Riccati y μ_a∗b_a = δ_1 valen para todo a: no fallan. (A) ≥ 0
  para todo a: no falla. (B) comprimido: sin signo para ningún a: no hay paso que falle.
- borrado de una potencia de primo: mismas identidades para el peso borrado (μ_a se recalcula): no fallan.
- Beurling: las identidades de convolución usan sólo el semigrupo libre generado; valen en Beurling
  (R167_103 Teor. S para la clase de criba): no fallan.
(F1) incumplido; (F2) tampoco: Arch entra sólo por P_T/𝓕 en J_a, no por μ_a.

## Estado

- Inventario (A)–(D): ARGUED (agotamiento de tipos de producto, no teorema de clase).
- Residuo «Möbius del sistema» de ROUND_004_A «NO excluido» 3: queda reducido a R163_144 + (C); no
  aparece mecanismo nuevo. Sigue sin prueba de imposibilidad general (OPEN como clase), pero no hay
  candidata escrita que pase la puerta.
- Pendiente de registro en la Parte V del índice (lo hace quien coordina); no edité el índice.
