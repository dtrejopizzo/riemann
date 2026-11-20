# Ronda 031 A — Cotejo de antecedentes: desigualdad de funciones enteras con ceros en ±i/2 para (PBP_T)

Tipo: cotejo de lectura. No se construye nada. Etiquetas tal como figuran en la fuente.

## 0. Operación cotejada

Acotar por arriba `μ(|τ| < 6.29)` (o `∫m dμ` por abajo) para `μ = Σ|F̂_i|²dτ/2π`, `F_i ∈ P_T`, usando a la vez
(i) tipo exponencial `T` (densidad de tipo `2T`), (ii) ceros dobles de la densidad en `±i/2`, y posiblemente
(iii) `Φ(log n) = 0`, `n ≥ 2`.

## 1. Qué se abrió

- Paper 47 (`04-papers/47-row-d-dual-certificates/main.tex`): thm:A y su prueba (l.444–477), rem:Kprim (l.479),
  prop:arch (l.2323–2350), thm:index y su prueba (l.2518–2560), prop:NC, cor:P3, rem:P4, thm:J y la observación
  que sigue (l.2638–2780), thm:nyq-cone con prueba y rem:nyq-dual (l.6320–6360). Por grep: lem:polarelim,
  prop:sharp (l.7330–7361), prop:haynsworth (l.10992), lem:KyFan (l.10802).
- Fase 155: R155_033 (§§ «τ = 0 cap», §3 índice, l.110, 272–363), R155_047 (Thm P, Cor P3, Remark PA/P4).
  R155_052 sólo encabezado. R155_023/024/027/048–051: NO abiertos (cubiertos por P47 thm:index/cor:P3, que los integra).
- Fase 160: R160_M2_R1 (tabla de resultados, §§ definiciones, Thm 4.1, Thm 4.2); R160_PC_R1 por grep (l.129, 271).
  R160_D4_R2 y R160_M4_R1: sólo grep (aparecen «primitiv/P_T», sin Paley–Wiener); no leídos enteros.
- Fase 186: R186_052 §3 (Thm 3.1 cono primal, Cor 3.2, Thm 3.3, Thm 3.4). Fase 195: VERIFY_CLAMPED_AND_EDGE_LAW (enunciado).
- Fase 211: ROUND_007_B §§0–1.3 (pieza 𝔢, forma en el potencial `G ∈ H²_0`); ROUND_008_E, 009_A, 009_B sólo por grep
  (concentraciones prolatas de `[−λ,λ]` en la construcción de extensión; otro objeto).
- Fase 212: ROUND_026_B §§1–3, ROUND_030_B §§2–3 y cierre; entradas 212-26-B (l.31333) y 212-30-B (l.31398) del índice.
- Índice maestro: grep de la lista pedida; leídas las familias «prolato / Thm P» (l.250–253, 3688, 3717, 4645, 5150),
  «capacidad polar» (l.256, 4731, 5194), «Paley–Wiener» (l.2035, 2172, 2212, 5330), «Slepian» (l.3298, 3625, 4713),
  «Blaschke» (l.4551, 4685), «de Branges» (l.2151, 4521–4530), «Sonin/prolato» (l.2133–2141, 5141–5163, 5994, 6028).
- NO abiertos: fases 153, 154, 156, 159, 183–185 (salvo grep), 197, 199 (sólo lista de archivos con «prolat»: KK_001,
  C_001, BB_001, U_001; no leídos), 201, 204. Grep en 183: «entire/prescribed» sólo da soporte prescrito y condiciones
  de Tate sobre `h_1` (R183_002 l.77), no una desigualdad de concentración.

## 2. Antecedentes reales

**A1. P47 thm:nyq-cone (l.6320; PROVED, Akhiezer CITED) = R186_052 Thm 3.1 + Cor 3.2.** El cono de densidades
`{|F̂|²: F ∈ P_T}` es exactamente `{f ≥ 0 en ℝ, entera de tipo ≤ 2T, L¹, ceros de orden ≥ 2 en ±i/2}`, y
`P_T = (¼ − ∂²)H²_0(I_T)`, `F̂ = (τ² + ¼)Ĝ`. Herramienta: Akhiezer + Paley–Wiener + factor de Blaschke
`(z − i/2)/(z + i/2)`. Es la caracterización exacta de (i)+(ii); no da cotas de masa. Clase (β): misma herramienta,
usada como reformulación del cono, no como desigualdad.
*Consecuencia inmediata (PROVED, una línea a partir de A1):* toda densidad mixta `Σ|F̂_i|²` con `F_i ∈ P_T` está en
el cono, luego es `|F̂|²` de un solo `F ∈ P_T`; como `Φ(log n)` es lineal en la densidad, **(PBP_T) sobre estados
mixtos de P_T coincide con el problema puro `Z^A_T`** de R160_M2_R1 (l.111). En cambio ROUND_026_B/030_B trabajan
con `Z^prim_T` (relajación `K^prim` de eq:Kprim: dos condiciones lineales sobre `Φ`), que es estrictamente más débil
que «ceros dobles». La afirmación de ROUND_030_B §3 («primitividad no es funcional acotada sobre μ») es correcta
para `K^prim`, pero en la versión de ceros dobles la primitividad es un **peso**: `μ = (τ²+¼)² ν`, `ν` densidad de
`G ∈ H²_0(I_T)` (R186_052 Cor 3.2: «Tate = weight»).

**A2. P47 prop:arch(ii) (l.2323; PROVED).** `λ_inf,P(T) ≤ C_0 + φ((3π/2T)²)` y `λ_inf,P(T) ↓ C_0` cuando `T → ∞`.
Es decir: **(i)+(ii) sin (iii) no acotan la masa baja de forma uniforme en T**; hay estados primitivos con
`∫m dμ → C_0 = −5.372`. Clase (α) para la parte (i)+(ii): resultado negativo PROVED. Prueba: modos de Dirichlet +
concavidad de φ (cor:mono); la restricción a `P_T` cuesta a lo sumo dos modos (`λ_3`).

**A3. P47 thm:index (l.2518; PROVED con intervalos certificados).** Valor exacto del problema (i)+(ii) en ventanas
chicas: `n_-(A_∞|P_T) = 0` para `T < T*_ev`, `0.58 ≤ T*_ev ≤ 0.60`, `T*_odd ∈ [log 2, 0.81]`, índice ≤ 2 en `(0, 0.90]`.
Herramienta: minorante multibanda de `m` (28 bandas), sección de Legendre finita por paridad, cola por la traza
(lem:KyFan), certificados de Haynsworth (prop:haynsworth) y planos negativos explícitos (prop:negplane). Las dos
restricciones `e^{±t/2}` se imponen en la sección finita; **no** se usa una desigualdad de funciones enteras con
ceros prescritos. Clase (α) en lo que se refiere al resultado (i)+(ii); (β)/(γ) en la herramienta.

**A4. P47 prop:NC, cor:P3, rem:P4; R155_047 Thm P (PROVED).** Concentración prolata `S_{T,τ_1}` + minorante de dos
valores: `n_- ≤ 5/7/8` en `½log3, log2, 0.80`. R155_047 l.155: «las dos restricciones de Tate sólo quitan
direcciones … y no se usan». rem:P4: el piso 5 se debe al minorante de dos valores y a `codim P_T = 2`, no a la teoría
prolata. Clase (β): (i) sin (ii). Ruta «prolata de dos valores» CERRADA (índice l.3688, 3717, 5150).

**A5. P47 observación tras thm:J (l.2770–2776).** Enuncia que una cota inferior de la forma arquimediana exige «una
estimación explícita no asintótica de concentración prolata» y que la concavidad (Jensen) sólo da cotas superiores.
Es la misma pregunta (i), sin (ii) ni (iii); declarada, no resuelta. Clase (β).

**A6. R155_033 «τ = 0 cap» (l.110, 350; PROVED).** Cota sobre certificados duales `f_w(0)`; otro objeto (pesos `w`), (β/γ).
R155_033 l.332: «las dos restricciones de primitividad restan a lo sumo 2» del índice (PROVED): (ii) es codimensión 2.

**A7. ROUND_007_B (211) §1.3 / P47 lem:polarelim, prop:sharp (PROVED/CITED).** En el potencial `G ∈ H²_0`:
`Arch = 𝔞^♯ − 𝔢`, `m^♯ = m + 1/(¼+τ²)`, `m^♯(0) = C_0 + 4`, `𝔢 = ∫|F̂|²/(¼+τ²) ≤ 4‖F‖²`. Usa (ii) como peso
`(τ²+¼)`, con el peso verdadero de la forma completa; el residuo (N) quedó OPEN. Clase (β): misma herramienta
(peso de Tate), otro objeto (con `v_n` fijo, sin `Φ(log n) = 0`).

**A8. R160_M2_R1 Thm 4.1–4.2 (PROVED).** Define `Z^A_T` (puro, primitivo, ciego a primos) y `Z^prim_T` (relajado),
dualidad fuerte y sándwich `Z^prim ≤ V* ≤ Z^A`. Ninguna cota inferior de ninguno; H1 (l.26) es HEURISTIC.
R160_PC_R1 (l.129, 271): el objetivo `Z^prim_T ≥ e^{−(2π−η)e^{2T}}` quedó como enunciado a probar, OPEN.

**A9. ROUND_026_B / ROUND_030_B (212).** Kreĭn (techo 3.0–3.4) y un generador (`𝔈 ≥ −1.4979 − 5.0434/(J+1)`, óptima
para un generador). Ninguna usa (i)+(ii). 026_B l.59–62: la primitividad vía `cosh(u/2)` tiene aporte asintótico
nulo (ARGUED).

**Coincidencias sólo de vocabulario (γ):** Paley–Wiener en índice l.2035 (base PW fija como detector, FALSIFIED),
l.2172 (ξ-divisibilidad, NO-GO), l.2212 (pivote LP-141), l.5330 (tests nodales PW leen `Φ_Λ` sólo en `log k`, DEAD);
Slepian l.3298/3625/4713 (ley de decaimiento, predicción refutada; otro objeto); Blaschke l.4551/4685 (bloques de
Fejér, testigo de primer contacto; DEAD); de Branges l.2151/4521 (reformulaciones, Conrey–Li); prolato–Sonin
(fase 183, CC_001, triples de borde: concentración de `[−λ,λ]` en la construcción de extensión, sin `Φ(log n)=0`).
No hay coincidencias para Logvinenko–Sereda, Kovrijkine, Remez, Nazarov, Turán, Beurling–Malliavin aplicado a
masa baja (l.2796 y 5163 son densidad BM en `p^{iτ}`, otro objeto).

## 3. ¿Se aplica el motivo de fracaso a la operación?

- (i)+(ii) solos: **sí, cerrado**. A2 prueba que no hay cota uniforme en `T` (ínfimo → `C_0`); A3 da el valor exacto
  en ventanas chicas. Cualquier desigualdad PW con ceros en `±i/2` sin (iii) está acotada por A2 y debe reproducir
  `T*_ev ∈ [0.58, 0.60]` (cota más fuerte ⇒ contradicción con prop:negplane).
- Motivo estructural: (ii) es codimensión 2 (R155_033 l.332; prop:arch prueba con `λ_3`); su peso `(τ²+¼)²` sólo
  penaliza `|τ| ≲ ½`, mientras la masa a controlar (ROUND_030_B §2.3) está en `π/log 2 < |τ| < 6.29`, donde
  `(τ²+¼)²` es casi constante relativo. Por tanto (ii) no puede aportar del orden del déficit `1.498`; ARGUED
  (esta ronda), coherente con 026_B l.59–62.
- (i)+(ii)+(iii) juntos: **no hecho**. Nadie acotó `Z^A_T` ni `Z^prim_T` por abajo con tipo exponencial.

## 4. Veredicto

**PARCIALMENTE HECHO.** (i)+(ii): repetición (α) — resuelto negativamente para `T` grande (prop:arch(ii)) y
exactamente en `T ≤ 0.90` (thm:index). (iii) con un generador y Kreĭn: 212-26-B, 212-30-B. La combinación
(i)+(iii) [tipo exponencial con anulación en `log n`] y (i)+(ii)+(iii) no está hecha.

Lo realmente nuevo que quedaría: una desigualdad que use el **tipo `2T` junto con `Φ(log n) = 0` para varios
generadores** (cocientes no enteros libres, ROUND_030_B §2.3) para controlar `μ(π/log 2 < |τ| < 6.29)`; la
primitividad sólo como corrección de codimensión 2 / peso `(τ²+¼)²` cerca de 0, no como mecanismo.

Resultados que el constructor DEBE respetar:
1. thm:nyq-cone: (PBP_T) en estados mixtos de `P_T` = problema puro `Z^A_T`; no confundir con `Z^prim_T` (eq:Kprim).
2. prop:arch(ii): sin (iii), ínfimo → `C_0 = −5.3722`; toda cota debe degradarse a esto si se borra (iii).
3. thm:index: con (i)+(ii) y sin contactos efectivos, positividad exactamente hasta `T*_ev ∈ [0.58, 0.60]`;
   índice 1 en `log 2`, 2 en `0.81–0.90`.
4. cor:P3/rem:P4: el minorante de dos valores no baja de 5 en `log 2`; usar minorantes multibanda.
5. ROUND_030_B §2.3: un generador es óptimo en `−1.4979`; la mejora debe venir de generadores en interacción.
6. R160_PC_R1: el umbral útil para `Z^prim_T` es `exp(−(2π−η)e^{2T})`; R160_M2_R1 T6: `Z^prim_T ≤ λ^A_T`.
7. P47 (observación tras thm:J): Jensen/concavidad sólo da cotas superiores; hace falta concentración no asintótica.
