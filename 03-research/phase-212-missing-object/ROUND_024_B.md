# Ronda 24, memo B — ¿Bloque casi nulo de la 211 = familia casi radical `{Π_T(M∗φ)}`?

Pregunta (índice, Parte V, 212-22-A, «(d) OPEN»): ¿el bloque casi nulo de la fase 211 es el mismo objeto que la
familia `{Π_T(M∗φ)}` de ROUND_021_A/022_A? Etiquetas: PROVED / CITED / ARGUED / OPEN / NUMÉRICO.

## 0. Cotejo
- Abiertos: `ROUND_021_A.md` (íntegro), `ROUND_022_A.md` §§Parte 1–3, `ANNEX_COTEJO_NULLDIR.md` §1.2 y §5;
  211 `ROUND_008_E.md` §§0–2.2, `ROUND_009_B.md` §0, §§2.4–2.6, `ROUND_005_C.md` §1 (Def. 1), `ROUND_017_A.md` (sólo
  encabezados); P47 `def:ext` (l.9867), `thm:ext-half` (l.9913), `prop:ext-gauge` (l.9946); índice 212-22-A.
- No abiertos: P2_SCHUR_001 (sólo por cita de 021_A), 211 ROUND_005_B, ROUND_007_B, ROUND_009_A, R160_D4_R2, P46.
- Grep («Π_T(M», «prolat», «casi nul», «near-null», «E_T» en 211/212): ningún memo escribe la identificación. El
  ANNEX_COTEJO_NULLDIR §5(c) separa «E(prolatos)», «familia de respuestas E_T» y S_T sin relacionarlos con M∗φ.
  Por tanto no se para en el cotejo. No se propone ningún mecanismo de signo; es una pregunta de identificación.

## 1. Definiciones literales
**212 (ROUND_021_A §1; ROUND_022_A Obs. 1.1).** `0<η<δ<T`, `χ` corte suave par (=1 en `|t|≤T−η`, soporte en `I_T`),
`φ ∈ L¹∩L²` con soporte en `[−(T−δ),T−δ]`, `F_φ = M∗φ`, `Π_T(φ) := χF_φ − A(χF_φ)u_+ − B(χF_φ)u_−`. Además
`M∗φ = S_ζ(g∗φ)` con `S_ζh(t) = Σ_{n≥1} n^{−1/2}h(t+log n)`, `g = (−∂²+¼)g_0`, `g_0(t)=(2π²e^{9t/2}−3πe^{5t/2})e^{−πe^{2t}}`.
Identidad (1.1): `a_T(Π_Tφ) = 𝔡_T(φ)` doble-exponencialmente pequeño (PROVED en 021_A).

**211, bloque bajo (ROUND_008_E §2.2; ROUND_009_B §2.5; P47 def:ext).** `λ=e^T`, `N=e^{2T}`, `c=2πN`, `ψ_k` prolatas de
`[−λ,λ]`, `d_k = 1−χ_k(c)`, `Ef(x) = e^{x/2}Σ_n f(ne^x)` en `I_T`. Bloque: `Π_T E·span{ψ_0,ψ_4,ψ_8,…}` (clase `+1` en el
sector par; en el impar clase intercambiada, suelo `d_10`). Ley: `λ_j^{ev} ≈ κ_j d_{4j+8}`, `κ_j∈[0.85,2]`, para `4j+8 ≲ 4N`
(NUMÉRICO); el minimizador está a ángulo `10⁻⁴` de `Π_T E span{ψ_0,…,ψ_8}` (NUMÉRICO).

**211, «bloque alto» (ROUND_009_B §2.4(iii)).** `k > 4N`, `d_k ≈ 1`; el cociente `M/D → 0` porque el tramo alto contiene
aproximaciones del gauge `𝒢_T` (soporte en `(−1/λ,1/λ)`), sobre las cuales `E ≈ 0` (ARGUED allí).

**211, familia `E_T` (ROUND_005_C Def. 1).** `E_T := N′ ⊕ P_𝒞Π(𝒩_η+𝒯)`: bloque de modos con `s_q ≤ 0` más respuestas del
peine; `dim E_T ≤ 2|𝒩|+2`, bloque 11/41/125 en `½log5+ε, 1, 1.25` (NUMÉRICO allí).

## 2. Lema puente (PROVED, una línea)
Sea `ι f(t) := e^{t/2} f(e^t)`. Entonces `E = S_ζ ∘ ι`:
`S_ζ(ιf)(x) = Σ n^{−1/2} e^{(x+log n)/2} f(ne^x) = e^{x/2}Σ f(ne^x) = Ef(x)`. ∎
Con `f_0 := ι^{−1}g_0`, `f_0(u) = (2π²u⁴ − 3πu²)e^{−πu²}` (par, gaussiana por polinomio) y `g∗φ = ι(f_φ)`,
`f_φ(u) := ∫ f_g(ue^{−s}) e^{−s/2}φ(s)ds` (convolución multiplicativa, `f_g := ι^{−1}g`). Así:
- 211 (ambos bloques) `= Π_T S_ζ ι(f)`, `f` par con soporte en `[−λ,λ]` (prolatas);
- 212 `≈ Π_T S_ζ ι(f_φ)` (con el corte `χ`), `f_φ` dilataciones gaussianas a escalas `e^{s}`, `|s| ≤ T−δ`;
- gauge `= S_ζ ι(φ)`, `φ ∈ 𝒢_T`, idénticamente nulo en `I_T` (P47 prop:ext-gauge: `Φ_φ` soportada en `(−∞,−T]`).
Los tres son imágenes del mismo operador `S_ζ`; difieren en la clase de entrada. Esto es (U) de 022_A con `h = ιf`.

## 3. Inclusión aproximada 212 ⊂ bloque bajo 211 (ARGUED; constantes no escritas)
(i) Concentración. Para `|s| ≤ T−δ`, `f_g(ue^{−s})` es gaussiana de escala `e^{s} ≤ λe^{−δ}`: la masa fuera de `[−λ,λ]` es
`≲ poly(λ)e^{−πe^{2δ}}`; por la autodualidad gaussiana la transformada es gaussiana de escala `e^{−s} ≤ λe^{−δ}` y la banda
fuera de `[−λ,λ]` es del mismo orden. Luego `f_φ` está `ε_δ`-concentrada en tiempo y banda en `[−λ,λ]²`,
`ε_δ ≍ poly(λ)e^{−πe^{2δ}}‖φ‖_{L¹}` (ARGUED; es la «localización» que 022_A atribuye a la autodualidad).
(ii) Landau–Pollak (CITED, clásico): una función `ε`-concentrada en tiempo y banda dista `≲ ε/√(1−χ_K)` del span de
`ψ_0,…,ψ_K` si `K` es el último índice con `d_K` acotado lejos de 1; aquí `K ≈ 4N − O(log c · log(1/ε_δ))`.
(iii) `E` en `I_T` suma `≤ N` términos: `‖Ef‖_{L²(I_T)} ≤ poly(N)‖f‖`. Con `Π_T` y `χ` acotados:
**`Π_T(M∗φ) ∈ Π_T E·span{ψ_k : k ≲ 4N} + O(poly(N)e^{−πe^{2δ}}‖φ‖)`** (ARGUED).
Es decir: la familia de 212 vive en la imagen del bloque prolato BAJO (`k ≲ 4N`), no del alto.
(iv) Corrección a ROUND_021_A §2(c): la frase «cúmulo = bloque prolato alto (P211-9B: los vectores gauge viven en el bloque
alto)» confunde dos cosas. Lo que se anula en el bloque alto es `E` sobre entradas cercanas a `𝒢_T` (núcleo de la
entrada), cuyas imágenes en `P_T` son ≈ 0, no direcciones casi nulas de `a_T`. El gauge no aporta ninguna dirección al
cúmulo en `P_T` (PROVED por prop:ext-gauge: imagen idénticamente nula en `I_T`). El «bloque casi nulo» de la 211 que puede
coincidir con `{Π_T(M∗φ)}` es el BAJO.

## 4. Lo que NO se identifica
(a) `E_T` de ROUND_005_C no es este objeto (PROVED por definición): es el bloque de índice negativo de `a_T` en `L²(I_T)`
más respuestas del peine, construido con los valores de `Λ`, de dimensión `≤ 2|𝒩|+2`; no es imagen de `S_ζ` ni casi
nulo (contiene direcciones con `s_q<0`). Queda fuera de la identificación.
(b) Inclusión inversa (bloque bajo 211 ⊂ 212): OPEN. `ιψ_k` tiene Mellin analítico sólo en un semiplano (soporte
`(−∞,T]`); estar en `{g∗φ}` exige `𝓜(ιψ_k)/Φ_g` de tipo exponencial `≤ T−δ`, y `Φ_g ∝ s(s−1)π^{−s/2}Γ(s/2)·(¼−s²…)`
decae como `e^{−π|τ|/4}`: la división crece exponencialmente. No hay inclusión exacta; la aproximada no está probada.
(c) Selección de clase. En la 211 sólo la clase `ε_k = +1` (sector par) es casi nula; la clase `−1` no
(ROUND_009_B Teor. 1.2: defecto de Fourier en `[2,4]` en la clase opuesta; NUMÉRICO 008_E §2.2: el fondo de
`Π_T E span{ψ_0,ψ_2}` es `0.108` en `T=0.8`). **Vector explícito de separación (NUMÉRICO):** `Π_T Eψ_2` está en la imagen
del span prolato bajo de §3(iii) pero tiene cociente de Rayleigh `≥ 0.108` (fondo del span bidimensional, 008_E §2.2),
luego no está cerca del cúmulo. Consecuencia: la inclusión de §3 es en el span prolato bajo COMPLETO; para caer en el
bloque casi nulo de la 211 haría falta que `f_φ` herede la clase `+1`. Como la dilatación conjuga `ℱ` con la dilatación
inversa, `f_φ` no es autofunción de `ℱ` para `φ` general; que su proyección de clase `−1` sea pequeña se deduce sólo de la
casi radicalidad (1.1) más el hecho NUMÉRICO de que la clase `−1` no es casi nula. Como enunciado estructural: OPEN.

## 5. Cuentas
- 212: `N_T(ε) ≳ (4/(πe))e^{2T} ≈ 0.47e^{2T}` (ARGUED en 021_A, falta (2.1)).
- 211 bloque bajo: Landau (CITED) da `≈ 4N` índices con `χ_k ≈ 1`, `≈ 2N` pares, `≈ N` de clase `+1`; con la ley
  `λ_j^{ev} ≈ κ_jd_{4j+8}` (NUMÉRICO) salen `≈ N − 2` direcciones pares y `≈ N − 2` impares por debajo de `ε` fijo, es decir
  `≈ 2e^{2T}` en total (ARGUED: la ley sólo está medida para `j ≤ 4`, `T ≤ 1.2`). Hasta umbral `ε = e^{−πe^{2T}}` el conteo
  baja en `O(log c · πe^{2T}/log…)`; no se calculó.
- 211 `E_T`: 11, 41, 125 (NUMÉRICO), otro objeto (§4a).
- Cota superior común: `exp(2e^T)` (P211-6C, CITED en 021_A). Ambas cuentas son `≍ e^{2T}` y compatibles con que la
  familia de 212 sea un subespacio de dimensión fraccional (`≈ 0.24`) del bloque bajo de 211; no se decide.

## 6. Qué cambia
- Si son el mismo (bloque bajo 211 = `{Π_T(M∗φ)}` a precisión de margen): el bloque bajo de la 211 hereda la descripción
  «imagen de `S_ζ` con entradas gaussianas»; la ley `d_{4j+8}` sería la lectura prolata de la localización gaussiana de
  022_A; la cuenta (2.2) de 021_A se sustituiría por Landau (CITED) más la ley de la 211, y el paso pendiente (2.1) de
  021_A quedaría superfluo. Todos los intentos de signo de la 211 sobre el bloque bajo pasan a ser intentos sobre la
  clase cerrada por R160_D4_R2 Teor. 5.1 (convolución de Dirichlet sobre tests); ningún paso de signo nuevo.
- Si no son el mismo (la inclusión §3 es estricta, o la clase no se hereda): coexisten dos familias casi nulas de
  tamaño `≍ e^{2T}` dentro del mismo span `Π_T E(prolatas bajas)`; su diferencia sería la parte de clase/constrainte, que
  es libre de `Λ` (ROUND_009_B §3: Teor. 1.1–1.2 valen verbatim para todo peso). Tampoco aparece mecanismo de signo.
- En ambos casos el signo sigue en el acople cúmulo–complemento (021_A §3, P211-17A), no en el cúmulo.

## Veredicto
- `E = S_ζ ∘ ι`: PROVED (cálculo de una línea). Ambos objetos son imágenes de `S_ζ`; entradas de soporte compacto en
  `[−λ,λ]` (211) frente a dilataciones gaussianas (212); gauge con imagen nula en `I_T` (PROVED, prop:ext-gauge).
- `{Π_T(M∗φ)} ⊂ Π_T E(span ψ_k, k ≲ 4N) + O(poly(N)e^{−πe^{2δ}})`: ARGUED (Landau–Pollak CITED; constantes no escritas).
- La identificación correcta es con el bloque prolato BAJO, no el alto; corrige ROUND_021_A §2(c): ARGUED con base PROVED.
- Inclusión en el bloque casi nulo de clase `+1` y la inversa: OPEN. `E_T` de 005_C: objeto distinto (PROVED por definición).
- Cuentas: 212 `≳0.47e^{2T}` (ARGUED), 211 `≈2e^{2T}` (ARGUED/NUMÉRICO). Sin mecanismo de signo en ningún caso.
- Siguiente operación única si se quiere cerrar (d): calcular numéricamente el ángulo entre `Π_T(M∗φ)` (φ prolatas de
  `[−(T−δ),T−δ]`) y `Π_T E span{ψ_{4j}}` en `T = 0.8, 1.0`; es identificación, no signo.
