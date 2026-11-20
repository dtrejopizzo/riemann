# Ronda 22, memo A — «Deshacer la suma»: ¿un solo objeto?, y la congruencia de Möbius sobre 𝔸_M

Notación de P47 y de la ronda 7. `S_N = Σ_{n≤N} n^{−1/2}τ_{log n}`, `S_ζ = S_∞` (R160_D4_R2 §3),
`Φ_G` transformada de Mellin en la convención de P46 (`Φ_{G⋆H} = Φ_GΦ_H`), `𝒩` el radical de P46 thm:radical,
`𝒲` la forma completa en la recta (P47, definición previa a lem:ext-mob). Retículo: P47 prop:AM (main.tex l.7811),
`𝔸_M = Arch_M − Div_M − Near_M`, `Div_M = Δ + Δᵀ`, `Δ_{mk} = 1_{k|m}Λ(m/k)(m/k)^{−1/2}` (corrección de normalización
registrada en N_BUILD_022 §2).

## Filtro de cuatro puntos

1. **Antecedentes más cercanos (leídos en primaria).**
   Parte 1: `phase-160-row-d-infinite-T/R160_D4_R2.md` Teorema 4.3 (la imagen `S_ζh` de tests con `Φ_h(1) = 0` está en el
   núcleo de `𝒲`; el término `Φ_h(1)e^{−t/2}` de Poisson decide la admisibilidad) y Teorema 5.1 (una línea que entra
   por una identidad de convolución de Dirichlet sobre tests no es la que lleva el signo); P46 thm:radical
   (`𝒩 = {Φ_N(0) = Φ_N(1) = 0, Φ_N(ρ) = 0}`, ideal para `⋆`); P47 lem:ext-mob, thm:ext-half, rem:ext-killing,
   prop:ext-gauge (l.9899–9960; Guo Lema 4.4); `phase-161-row-d-sum-product-square/R161_001` Teoremas 2.1, 3.1 (PC), 4.1;
   `R160_M4_R1` Teorema A, C; `ROUND_020_B` §4.2; `ROUND_021_A` §3(c).
   Parte 2: `phase-188-closing-D/N_BUILD_022` §§1–3 (matriz `Z`, `ZΔ = [L, Z]`, NO-GO para Near);
   `phase-162-.../R162_903` Teorema 3.2 (BCH terminante, `log Z = M_T(Λ/log)`), Teorema 4.1 (colapso de Sylvester bajo
   congruencia unitriangular, válido para Λχ₂, Beurling, borrados), Teorema 4.2 (Moore), §8 (residuo: el paso exacto
   «no debe ser invariante por congruencia integral unipotente»); `R162_1003` Cor. 4.3 (toda representación `Z*DZ` con `Z`
   unipotente es una congruencia); `ROUND_004_A` (R4-a, R4-b), `ROUND_004_C` (R4-d); L2_BUILD_028 §2(c).
2. **Nuevo.** Nada que pase el filtro. Dos piezas de escritura: (a) el enunciado unificado (U) de la Parte 1 como
   corolario explícito de citas existentes, con la observación `K_Pó = S_ζ g_0` (perfil gaussiano); (b) la fórmula
   cerrada, libre de Λ, de `Zᵀ Div_M Z` (Lema 2.1).
3. **Por qué no evita la dificultad.** La congruencia de la Parte 2 es exactamente la clase cerrada por R162_903 Teor. 4.1
   y R162_1003 Cor. 4.3; el bloque Near no es tocado (N_BUILD_022 §3). Ver Parte 3.
4. **Conexión con la positividad global.** `𝔸_M ⪰ 0 ⟺ Zᵀ𝔸_M Z ⪰ 0` (Sylvester); ninguna desigualdad nueva.

**Veredicto del cotejo: repetición en ambas partes.** Siguen el enunciado preciso pedido y lo que queda distinto.

## Parte 1 — ¿Un solo objeto?

**Observación 1.1 (PROVED, cálculo directo).** Con `g_0(t) := (2π²e^{9t/2} − 3πe^{5t/2}) e^{−πe^{2t}}`,
`n^{−1/2}g_0(t + log n) = (2π²n⁴e^{9t/2} − 3πn²e^{5t/2})e^{−πn²e^{2t}}`, luego `K_Pó = S_ζ g_0` (serie de Riemann–Pólya) y,
como `S_ζ` conmuta con traslaciones y derivadas, `M = (−∂² + ¼)K_Pó = S_ζ g`, `g := (−∂² + ¼)g_0`; `M∗φ = S_ζ(g∗φ)`.
`Φ_{g_0}(s) = ½s(s−1)π^{−s/2}Γ(s/2)` (convención de P46 Def–Thm 11.7, ARGUED en la normalización de constantes).
Así la familia de R160_M4_R1 / ROUND_021_A es imagen de `S_ζ`. El gauge es imagen de la misma suma: P47 l.9877,
`Φ_φ` con Mellin `ζ(s)𝓜φ(s)`, `Φ_φ(x) = e^{−x/2}Σ_{k≥1}𝓕φ(ke^{−x})`.

**Lema (U) (CONDITIONAL sólo en la verificación de dominios; contenido CITED).** Sea `h` con `S_ζh ∈ D_W` y
`Φ_h` holomorfa en una franja que contiene `0 ≤ Re s ≤ 1`, con `ζ(s)Φ_h(s)` nula en `s = 0` y `s = 1`. Entonces
`S_ζh ∈ 𝒩` y `𝒲(S_ζh, G) = 0` para todo `G ∈ D_W`.
*Prueba.* Para `Re s > 1`, `Φ_{S_ζh} = Σ_m m^{−s}Φ_h = ζΦ_h` (R160_D4_R2 Lema 3.1(a)); continuación; se anula en cada
`ρ` y en `0, 1` por hipótesis; P46 thm:radical. ∎ Casos: `h = g∗φ` (familia de `M`), `h = φ ∈ 𝒢_T` del lado multiplicativo
(Guo Lema 4.4 / prop:ext-gauge), `h = c_F` con `F ∈ P_T` (R160_D4_R2 Teor. 4.3(c), identidad (C′′)).

**Qué distingue las clases de entrada (PROVED salvo donde se indica).** La radicalidad NO distingue: el mismo lema
(fórmula explícita sobre un Mellin divisible por ζ) sirve para todas. Por tanto la afirmación de ROUND_020_B §4.2
«el radical de `M` usa la ecuación funcional y el del gauge no» es inexacta como enunciado sobre la radicalidad: en
ambos casos la prueba es P46 thm:radical, cuyo lado geométrico ya contiene Euler, EF y Γ. Lo que sí es correcto
es `M ∉ 𝒢_T` (soporte). Lo que distingue las entradas es **dónde vive `S_ζh` respecto de la ventana**:
- `h` de soporte compacto (gauge; R160_D4_R2 Teor. 4.3(a)): `S_ζh` se anula exactamente de un lado y del otro es
  `Φ_h(1)e^{−t/2} + O(e^{Nt})` por Poisson: el defecto de Poisson es el término polar.
- `h` gaussiana (autodual bajo Fourier): por inversión de theta `S_ζh` decae doble-exponencialmente en ambos lados;
  truncar a `[−T, T]` cuesta `e^{−πe^{2T}}` (R160_M4_R1 Teor. A/C). Ésta es la única entrada en la que la
  autodualidad interviene: en la localización, no en el radical.
- `S_N` finito (PC): el defecto es `E_N = S_N𝓕 − JS_N` (Poisson finito) más `H_{M,N}` (hipérbola, sin coeficientes
  `k ≤ N` por Λ∗1 = log, R161_001 Teor. 2.1). (PC) es la versión de operadores truncados del mismo lema.
- (d) bloque prolato alto de la 211: NO identificado. ROUND_021_A §3(c) lo deja OPEN; no tengo prueba.

**¿Está ya escrito como un solo enunciado?** Casi: R160_D4_R2 Teor. 4.3 es (U) para `h ∈ C_c^∞` con el defecto de
Poisson explícito, y su Teor. 5.1 cierra la clase «identidad de convolución de Dirichlet sobre tests» como portadora
del signo. P46 thm:radical (ideal) da el caso `M∗φ`. Lo único no escrito es juntar `K_Pó = S_ζg_0` con ese teorema; es
una línea, no un resultado nuevo. Respuesta a la hipótesis del owner: **(a), (b), (c) son un objeto en el sentido de
(U) (CITED); (d) OPEN.** La forma sobre la imagen es «términos de borde» por (U) + truncación, y esos bordes son
exactamente defecto de Poisson + cola de hipérbola; ninguno lleva signo por R160_D4_R2 Teor. 5.1.

## Parte 2 — La congruencia `𝔹_M = Zᵀ𝔸_M Z`

`Z_{mk} = 1_{k|m}(m/k)^{−1/2}` es la matriz de `S_M` en coordenadas de retículo: `s ↦ Zs` corresponde a
`Σ_k s_kτ_{log k}F_0 ↦ Σ_m(Zs)_mτ_{log m}F_0`, i.e. a `S_{M/k}` aplicado al átomo `k` (truncación triangular, no
uniforme en `N`). `Z⁻¹_{mk} = 1_{k|m}μ(m/k)(m/k)^{−1/2}` (N_BUILD_022).

**Lema 2.1 (PROVED; NUMÉRICO de control a `10⁻¹⁴` en `M = 60`).** `ZΔ = ΔZ = LZ − ZL` (convolución de Dirichlet
conmutativa sobre un conjunto cerrado por divisores; `1∗Λ = log`), luego
`Zᵀ Div_M Z = 2ZᵀLZ − (LG + GL)`, `G := ZᵀZ`, y entrada a entrada, con `l = mcm(a,b)`, `g = mcd(a,b)`:

    (ZᵀDiv_M Z)_{ab} = (√(ab)/l) Σ_{j ≤ M/l} [log(l/g) + 2 log j] / j  ≥ 0.

*Prueba.* `G_{ab} = Σ_{l|m≤M} √(ab)/m`; `(ZᵀLZ)_{ab} = Σ_{l|m≤M} √(ab)log m/m`; `2log(lj) − log(ab) = log(l/g) + 2log j`. ∎
Λ desaparece por completo: es N_BUILD_022 §1 (= R162_903 B2.1) leído como congruencia. Con `cΛ`:
`Zᵀ Div^{(c)} Z = c·(lo anterior)`, que no es libre de peso (`(c−1)ZᵀDivZ` sobrante) — automático, sin signo (F1).

**Estructura de `𝔹_M`.** `𝔹_M = ZᵀArch_MZ − [2ZᵀLZ − {L, G}] − ZᵀNear_MZ`. (i) Lo que cancela: sólo la parte de
coincidencias exactas (Div), y la cancelación la paga una cola de hipérbola `Σ_{j≤M/l} log j/j ≍ ½log²(M/l)` que crece
con `M`: el «interior» no queda en cero, queda transportado a una función de `(a,b,M)` sin aritmética.
(ii) Lo que no cambia: `ZᵀNear_MZ`, sin identidad exacta (N_BUILD_022 §3, NO-GO PROVED: el defecto es el propio Near).
(iii) **No aparece un bloque ≈ 0.** Las entradas `e_k` de la base de átomos son `τ_{log k}F_0` con `F_0` de soporte
`2T_0 < log 2`: entrada compacta, no gaussiana, con `Φ_{F_0}(1) ≠ 0` en general, de modo que por R160_D4_R2 Teor. 4.3(a)
la imagen `S` crece al ritmo polar; la cercanía al radical de la Parte 1 requiere entradas gaussianas en la variable
continua, que en el retículo no son vectores de soporte finito. El bloque casi nulo de la 211 no se vuelve un bloque
explícito de `𝔹_M` por esta congruencia (ARGUED; no hice el cálculo espectral).

**Controles.** La congruencia vale para todo peso (R162_903 Teor. 4.1(c)): inercia de `𝔹^{(w)}` = inercia de `𝔸^{(w)}`.
`2Λ`: aparece `−ZᵀDivZ` adicional, entrada a entrada ≤ 0 por el Lema 2.1; borrar `p^k`: `Zᵀ(δ_{p^k}-diagonal)Z`;
Beurling: `Z` cambia de soporte (enteros generalizados). Ningún paso NOMBRADO pierde signo porque ningún paso tiene
signo: por Sylvester la congruencia es un isomorfismo de formas.

## Parte 3 — Veredicto

- **Parte 2: repetición / NO-GO de clase ya registrado.** Clase: congruencias unitriangulares enteras sobre el orden
  de divisibilidad (R162_903 Teor. 4.1–4.2, §8; R162_1003 Cor. 4.3; N_BUILD_022 §§1–3). Lo «distinto» propuesto (suma
  exacta en el retículo, no peso ni inverso aproximado) está literalmente dentro de esa clase: `Z` es la matriz de la
  suma exacta.
- **Parte 1: el enunciado unificado es CITED** (R160_D4_R2 Teor. 4.3 + P46 thm:radical + Obs. 1.1), con corrección a
  ROUND_020_B §4.2: la autodualidad gaussiana entra en la localización, no en la radicalidad. (d) OPEN.
- Intermedios: Lema 2.1 (forma cerrada, libre de Λ y entrada a entrada ≥ 0, de `ZᵀDivZ`) es una reescritura de
  N_BUILD_022 §1; no es nuevo en contenido.
- **Siguiente operación: ninguna** desde esta postura. La única pregunta abierta que deja es (d): si el cúmulo
  casi nulo de la 211 está en `Π_T S_ζ(gaussianas)`; es un enunciado de identificación, sin signo (R160_D4_R2 Teor. 5.1).
