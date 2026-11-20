# ROUND 024 C — Las tres comprobaciones baratas que dejó el triage de la fila D

Pregunta: ejecutar las tres comprobaciones que `TRIAGE_D_1…5` y la entrada `212-triage-D` (Parte V del índice) dejaron
como «deciden algo»: (a) `n_− ≤ 2` de D.53 (6.7) frente a Thm P y P47 thm:J / cor:nasym; (b) `n_odd(0.80)`; (c) medias
de Fejér de CA_E_001 Cor 1.1. No se toca ningún paper ni el índice.

## 0. Archivos abiertos

Abiertos: `TRIAGE_D_1.md` (ítem 38, §3), `TRIAGE_D_3.md` (ítem 111, §3), `TRIAGE_D_4.md` (ítem 150, §3);
`phase-114-closing-the-four-rows/114_d_53_…GATE.md` §§1–7; P47 `main.tex` §«Bounds on the negative index»
(thm:index l.2518, cor:P3 l.2662, thm:J l.2694, cor:nasym l.2722; parity l.2420–2434);
`phase-155…/R155_052_ROUND8A_INDEX_MULTIBAND.md` (resumen y Thm 5.x), scripts `scripts/r8a/r8a_01_upper.py`, `r8a_lib.py`
y el JSON archivado `r8a_01_0p80_par1_K30_K244_c24.json`; `phase-193…/CA_E_001_COMMUTATIVE_COLLAPSE.md` §§0–4,
`CA_E_001_REVIEW.md` (cabecera); índice maestro: entradas 212-triage-D, 212-20-A y filas l.3688, l.5150.
No abiertos: D.52 (se usa sólo la cita que hace D.53), R155_047/048, BRIEF_CONSTRUCTOR y RULES_AVOID (no hay
construcción en este memo), P48.

## (a) D.53 (6.7) frente a Thm P, thm:J, cor:nasym

**Qué dice cada enunciado (leído contra las definiciones).**
- P47 thm:index (PROVED, certificado): para la forma **arquimediana sola** `A_∞ = 𝔪_T` sobre `P_T`,
  `n_ev, n_odd ≤ 1` en `(0, 0.90]`; `n_−(A_∞|P_T) = 0/1/2` según `T` respecto de `T*_ev ∈ [0.58,0.60]`,
  `T*_odd ∈ [log 2, 0.81]`.
- P47 cor:P3 («Thm P»; PROVED): **misma forma** `A_∞|P_T` y también `𝔪_T` en `L²(I_T)`:
  `n_− ≤ 5` en `T=½log3`, `≤ 7` en `log 2`, `≤ 8` en `0.80` (cota prolata, más débil que thm:index en ese rango).
- P47 thm:J (PROVED): cota inferior `n_−(A_∞|P_T) ≥ ⌈2Tτ_0/π⌉ − 3`, vacía hasta `T ≈ 0.75` y `≥ 3` desde
  `2Tτ_0/π > 5`, es decir `T > 1.249`. cor:nasym (PROVED): `n_−(A_∞|P_T) ~ 4.004·T`, `T → ∞`.
- D.53 (6.1)–(6.7): `A_T = K_{g,T}` sobre `H_T^0` (masa cero) donde, por (1.1)–(1.2), `K_g` es el núcleo **completo**
  (Gamma más todas las bisagras de potencias de primos `a = k log p ≤ 2T`), en el pullback por derivadas:
  `−B_T(F,F) = ⟨K_{g,T}F′, F′⟩`. `N_T` son los momentos `e^{±t/2}`, así `ker N_T` corresponde a `P_T`. (6.7) pide
  `n_−(A_{T,P}) ≤ 2` para toda partición y la igualdad de índices con `𝒢_{T,P}`.

**Resultado.** Los enunciados son **compatibles y no se tocan**: thm:index, cor:P3, thm:J y cor:nasym cuentan
direcciones negativas de la parte arquimediana sola; (6.7) acota las del núcleo completo con el peine. Ninguna cota
de Arch falsa ni prueba (6.7), salvo en el tramo sin primos `2T < log 2` (`T < 0.3466`), donde el núcleo de D.53 es
sólo el término Gamma: allí thm:index da índice `0` sobre `P_T` (`T < 0.58`), coherente con (6.7).
Etiqueta: **PROVED** (lectura de enunciados) para «no hay contradicción ni falsificador disponible»; la
identificación de signos `n_−(A_T)` ↔ direcciones negativas de la forma completa en `H^1_0` es **ARGUED** (depende de la
convención de D.52, no abierto).
- Consecuencia de crecimiento: cor:nasym obliga a que, si (6.7) vale para `T > 1.25`, el peine de primos haya
  eliminado al menos `⌈2Tτ_0/π⌉ − 5` de las direcciones negativas de Arch sobre `P_T` (se ganan a lo sumo 2 al pasar de
  `P_T` a `H_T^0`). Esto es la misma observación de 212-20-A, ahora aplicada a (6.7): no es falsificador.
- Qué decidiría (6.7) de verdad: sólo un cálculo de la matriz por celdas **con el peine** a `T` fijo y `n_− ≥ 3`. Ese
  cálculo no es «barato» en el sentido del triage (valores exactos de Λ, cotas certificadas del núcleo completo) y no
  se corrió. Etiqueta de (6.7): **OPEN**.

**Correcciones al índice/triage.**
1. `TRIAGE_D_1.md` l.88: la condición «si Thm P es del mismo operador A_T restringido a la masa cero, el ítem 38
   pasa a CERRADA» se resuelve en negativo: **no es el mismo operador** (Arch sola vs núcleo completo). Ítem 38 queda REF.
2. Índice, entrada 212-triage-D, viñeta «Cómputos que deciden algo»: quitar «cotejar antes con el Teorema P, “cuenta
   5 en log 2”»; sustituir por «Thm P / thm:J / cor:nasym son de Arch y no deciden (6.7)».
3. Índice l.5150 («DEAD [cuenta 5 en log 2]») y l.3688 («n₋ ≤ 5/6/7 (5/7/8 serie)»): según P47 cor:P3 la cota es
   `5` en `½log3`, `7` en `log 2`, `8` en `0.80`. «5 en log 2» y «5/6/7» son discrepancias de transcripción.

## (b) `n_odd(0.80)`

**Qué decide.** Por monotonía estricta de `λ_odd` (P47 thm:index / R155_052 Lema 4.3) y `T*_odd ∈ [log 2, 0.81]`:
`n_odd(0.80) = 0` ⟺ `T*_odd > 0.80` ⟺ (H1) vale en `0.80`. Es un dato del lado arquimediano; no decide el signo de `a_T`.
Estado previo: P47 thm:index fija sólo `n_odd(0.80) ≤ 1` (l.2532, 2552); R155_052 punto 5: OPEN, segundo autovalor
de la matriz certificante `−0.0047` (`τ_N` por defecto), `−0.0019` (`τ_N = 30`); extrapolación heurística `τ_N ≈ 60`.

**Ejecución.** Script de registro `r8a_01_upper.py` sin modificar, copiado a
un directorio temporal
(aritmética de intervalos mpmath, 40 dígitos). Corridas a `T = 0.80`, sector impar:
| K, K2, c_N objetivo | τ_N | resultado | 2.º autovalor (punto medio) |
|---|---|---|---|
| 30, 44, 40 | — | falla `γ > 0` (K insuficiente) | — |
| 44, 60, 40 | 50 | cota certificada `≤ 1`, margen `0.1644` | `−0.000299` |
| 56, 76, 60 | — | falla de la librería («series did not converge; enlarge KM») | — |
Salida: `r8a_run/r8a_01_0p80_par1_K44_K260_c40.json` y los `.log` en la misma carpeta.

**Resultado.** `n_odd(0.80) ≤ 1` re-certificado (**PROVED**, ya estaba en P47); `n_odd(0.80) = 0` sigue **OPEN**.
La serie `−0.0047 → −0.0019 → −0.0003` al crecer `τ_N` es compatible con que el residuo lo fija el minorante constante
más allá de `τ_N` y con certificar `0` a `τ_N` algo mayor (**NUMÉRICO**, diagnóstico). Ir más allá exige ampliar `KM`
en `r8a_lib.moments`, es decir modificar el script de registro; no se hizo.
Corrección: ninguna en el índice (ítem 111 ya decía «decide algo local»); añadir al ítem 111 de `TRIAGE_D_3.md` y a
la entrada 212-triage-D el dato `τ_N = 50: −0.0003, sigue ≤ 1`.

## (c) Medias de Fejér de CA_E_001 Cor 1.1 fuera de `ι(ℝ)`

**Qué afirma el triage** (`TRIAGE_D_4.md` ítem 150, l.40 y l.66): un negativo fuera de `ι(ℝ)` mostraría que
(eq:target) es más fuerte que la positividad en `P_T` y falsaría esa reformulación.

**Resultado (PROVED, sin cómputo).** A `S` y `N` fijos la media de Fejér
`Φ_{S,N}(y) = Σ_{q∈G_S, |v_p(q)|<N} φ(q) \overline{y(q)} Π_p(1−|v_p(q)|/N)` es una suma finita, luego continua en
`y ∈ Ĝ`, y sólo depende de la proyección `y|_{G_S} ∈ 𝕋^S`. Los `log p`, `p ∈ S`, son ℚ-linealmente independientes, así
que `τ ↦ (p^{iτ})_{p∈S}` tiene imagen densa en `𝕋^S` (Kronecker). Por tanto
`inf_{y∈Ĝ} Φ_{S,N}(y) = inf_{τ∈ℝ} Φ_{S,N}(ι(τ))`. Un punto «fuera de la recta» nunca da un valor que no esté ya
aproximado por puntos de la recta: la búsqueda fuera de `ι(ℝ)` **no decide nada nuevo**. La distinción recta/fuera de
la recta sólo existe en `Ĝ` completo (Lemma 1, soporte de `μ_φ`), no a nivel finito.
Además, por el propio Cor 1.1 un negativo en cualquier `y` falsaría (eq:target) entero, que por thm:oneprofile /
prop:AM(i) es una consecuencia de la positividad sobre los `P_T` de todo `T` (no una forma «más fuerte» de ella):
la lectura del triage está invertida (**ARGUED** en cuanto a la dirección exacta de thm:oneprofile, no reabierto aquí).
Etiqueta del ítem 150: **NO-GO** como comprobación que decide algo; las cajas sobre la recta son la familia `s_w`
torcida ya usada (CA_E_001 Cor 1.1, última frase).
Correcciones: `TRIAGE_D_4.md` ítem 150 (l.40, l.66) pasa de «LOCAL/NUMÉRICA — decide algo» a «no decide: equivale por
densidad a la recta»; quitar «medias de Fejér fuera de ι(ℝ)» de la viñeta «Cómputos que deciden algo» de 212-triage-D.

## Resumen
| ítem | resultado | etiqueta | corrección |
|---|---|---|---|
| (a) 38 | compatibles; Thm P/J/nasym son de Arch, (6.7) del núcleo completo; nada lo falsa | PROVED (lectura); (6.7) OPEN | TRIAGE_D_1 l.88; 212-triage-D; índice l.3688, l.5150 (5/7/8) |
| (b) 111 | `≤ 1` re-certificado; `= 0` no alcanzado (−0.0003 a τ_N=50) | PROVED ≤1; OPEN =0; NUMÉRICO tendencia | añadir dato a ítem 111 / 212-triage-D |
| (c) 150 | fuera de ι(ℝ) ≡ sobre ι(ℝ) por densidad a S finito | PROVED; ítem NO-GO | TRIAGE_D_4 ítem 150; 212-triage-D |
Ninguna de las tres toca el signo de `a_T`.
