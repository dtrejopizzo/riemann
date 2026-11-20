# Ronda 21, memo A — La familia casi radical `{Π_T(M∗φ)}`: cuenta y enunciado estructural

Nota de cuenta y de estructura. No es un intento de signo. Notación de la ronda 7:
`a_T(F) = Arch(F) − Σ_n v_n c_F(log n)` en `P_T = {∫F e^{±t/2} = 0}`; `W_*` la forma global (P46 §11);
`K_Pó` el núcleo de Pólya, `M = −K_Pó″ + ¼K_Pó`, `Φ_M(s) = s(1−s)ξ(s)`; `X_T` como en `R160_M4_R1.md` y `ROUND_019_A.md`.

## Filtro de cuatro puntos (cotejo primero)

1. **Antecedentes, leídos en primaria.**
   - `phase-106-global-modular-star-audit/106_09_NEAR_RADICAL_CLUSTER_AND_GAP_COLLAPSE.md`: Lema 1 (continuidad
     ponderada de la forma completa en `𝒳_b`), §3 (truncados suaves `χ_aK^{(j)}`, matriz `O(λ^Me^{−cλ²})`),
     final de §4: «cualquier colección finita fija de derivadas pone cada número fijo de autovalores en un
     cúmulo casi nulo»; §5: la selección dentro del cúmulo es el problema.
   - `phase-160-row-d-infinite-T/R160_M4_R1.md`: Teorema B(i) (`λ_A ≤ Ce^{cT}e^{−2πe^{2T}}`), Observación C1
     (`Q(∂)τ_bK_Pó` en el radical, tasa exacta `π`), Teorema D y su lectura (la restricción muerde hasta la
     altura `≈ 4e^{2T}`).
   - `phase-204-refd-tractability/P2_SCHUR_001.md`: `𝒜 = span{(ζP)(∂)g} ⊂ rad 𝒲`, `𝒲_AA ≡ 0`, `𝒲_AB ≡ 0`,
     Haynsworth `In(𝒲) = (0,0,dim 𝒜) + In(𝒲_BB)`, Lema P2-S.3 (un Schur útil necesita un bloque fuera del radical).
   - `phase-211-sign-sandbox/ROUND_006_A.md` Teorema 5 y `ROUND_006_C.md` (P211-6C): cota SUPERIOR
     `m_δ(T) ≤ exp(2e^T(1+o(1)))`; `ROUND_005_B.md` (P211-5B): tamaños numéricos del cúmulo `2,4,6,9,16,26`;
     `ROUND_005_E.md` l.242: ninguna cota inferior arquimediana del cúmulo; P211-8E, P211-9B, P211-17A.
   - P47 `cor:nasym` (`n_−(Arch|P_T) ≈ 4.004·T`), `thm:coer-schur`, `rem:coer-size` (dimensión `2k−2` doblemente
     exponencial); fase 212: `ROUND_019_A`, `ROUND_020_A`, `ROUND_020_B`, `ANNEX_MARGIN_CONFLICT`.
2. **Lo nuevo.** Sólo (a) la familia escrita con convolución general `φ` (el corpus usa polinomios en `∂`
   y traslaciones, que son el caso `φ` = combinación finita de `δ^{(j)}_b`); (b) una cota INFERIOR de Weyl para
   el cúmulo, `N_T(ε) ≳ (4/(πe))e^{2T}` (ARGUED), que no está registrada (el corpus tiene sólo cotas
   superiores y conteos fijos); (c) la lectura del signo del término principal de defecto.
3. **Por qué no repite.** No propone construcción ni signo; es una cuenta. La parte (3) del encargo
   (cociente + defecto) ES la descomposición de P2_SCHUR_001 a `T = ∞` y la de P211-17A a `T` finito:
   se cita y no se rederiva.
4. **Conexión global.** Ninguna directa; ver §4.

## §1 La familia (PROVED salvo donde se indica; es 106_09 §3 con `φ` general)

Sea `0 < η < δ < T`, `χ` suave par, `χ = 1` en `[−(T−η), T−η]`, soporte en `[−T,T]`. Dominio:
`φ ∈ L¹ ∩ L²`, soporte en `[−(T−δ), T−δ]`. Pongamos `F_φ = M∗φ`, `R_φ = (1−χ)F_φ` y

    Π_T(φ) := χF_φ − A(χF_φ)u_+ − B(χF_φ)u_−,

con `u_±` fijos en `C_c^∞(I)` duales a los momentos `A, B` (`A(u_+)=1, B(u_+)=0`, etc.). Como
`Φ_{F_φ}(0) = Φ_{F_φ}(1) = 0`, `A(F_φ) = B(F_φ) = 0`, luego `A(χF_φ) = −A(R_φ)`, y `Π_T(φ) ∈ P_T`.

**Identidad exacta.** Como `F_φ` está en el radical de `W_*` (su transformada es `Φ_M·φ̂`, divisible por `ξ`;
P46 Thm 11.11, R160 Lema 2(a)) y `a_T = W_*` sobre funciones con soporte en `I` (P47):

    a_T(Π_T φ) = W_*(R_φ + A(R_φ)u_+ + B(R_φ)u_−) =: 𝔡_T(φ).                  (1.1)

Sólo entran el resto `R_φ` y la corrección de Tate. **Cota** (106_09 Lema 1 y (15)):
`|M(s)| ≤ C e^{M_0|s|}e^{−πe^{2|s|}}`, luego en `|t| ≥ T−η`, `|F_φ(t)| ≤ ‖φ‖_{L¹}·C e^{c}e^{−πe^{2(δ−η)}}`, y

    0 ≤ |𝔡_T(φ)| ≤ C e^{cT} e^{−2πe^{2(δ−η)}} ‖φ‖²_{L¹} ≤ C′ T e^{cT} e^{−2πe^{2(δ−η)}} ‖φ‖²_{L²}.   (1.2)

La norma relevante es `‖φ‖_{L¹}` (o `L²` con factor `√(2T)`), no `‖F_φ‖`.

**Denominador.** `‖Π_Tφ‖² = ‖F_φ‖² + O(tail) = (1/2π)∫|Φ_M(½+iτ)|²|φ̂(τ)|²dτ + O(tail)`, con
`|Φ_M(½+iτ)| ≍ τ^{2}|Ξ(τ)| ≈ τ^{15/4}e^{−πτ/4}|ζ(½+iτ)|`. El cociente de Rayleigh es por tanto

    a_T(Π_Tφ)/‖Π_Tφ‖² ≲ T e^{cT} e^{−2πe^{2(δ−η)}} · ‖φ‖²/∫|Φ_M|²|φ̂|².                (1.3)

## §2 La cuenta

**Proposición 2.1 (ARGUED; el paso no probado es la cota inferior (2.1)).** Sea `V_{L,Ω}` el espacio
de las primeras `⌊LΩ/π⌋(1−o(1))` funciones prolatas de soporte de longitud `L = 2(T−δ)` y banda `[−Ω,Ω]`.
Suponiendo

    ∫|Φ_M|²|φ̂|² ≥ e^{−(π/2)Ω − o(Ω)}‖φ‖²  en V_{L,Ω}                                   (2.1)

(promedio de `|ζ|²` en la banda frente a ceros de `ζ`: un elemento de `V_{L,Ω}` tiene `φ̂` de tipo `T−δ`
y no puede concentrarse en los ceros; es una desigualdad de tipo Remez/Logvinenko–Sereda, no verificada aquí),
min–max da `μ_j(a_T|P_T) ≤ ε` para `j < dim V_{L,Ω}` siempre que

    Ω ≤ Ω_max(δ, ε) := 4e^{2(δ−η)} − (2/π)log(1/ε) − O(T).

Optimizando `(T−δ)e^{2δ}` en `δ = T − ½`:

    N_T(ε) ≥ (2(T−δ)/π)Ω_max ≈ (4/(πe)) e^{−2η} e^{2T} − (2/π²)log(1/ε)   (ε fijo, T grande).     (2.2)

Para `ε = e^{−πe^{2T}}` (la mitad del exponente del margen) la misma cuenta da todavía `≍ e^{2T}` autovalores.
La altura `4e^{2T}` coincide con la de R160 Teorema D (lectura). Orden de magnitud `0.47e^{2T}`: `3.5, 5.1, 7.7`
en `T = 1, 1.2, 1.4`, comparable con los tamaños `P211-5B` (NUMÉRICO allí, no rederivado).

**Comparaciones.**
(a) `n_−(Arch|P_T) ≈ 4.004 T` (P47 `cor:nasym`, CITED): el cúmulo casi radical, `≍ e^{2T}`, es mucho más
grande; no es el espacio negativo arquimediano (coherente con P211-7B: «bloque = resonancias del peine»).
(b) `S_{T,k}`: tamaño `2k−2 ≥ exp(c e^T)` (`rem:coer-size`, CITED), y `c(T,k) > 0` en el complemento
`𝒱_k ∩ 𝒟_T` obliga a que todo el cúmulo `≍ e^{2T}` (autovalores `≤ ε < c`) quede, salvo un ángulo
controlado por `‖𝖪‖`, dentro de `E_k` (PROVED como consecuencia de min–max + `thm:coer-schur`). La cota
superior `exp(2e^T)` (P211-6C) y la inferior (2.2) dejan el tamaño real del cúmulo entre `e^{2T}` y `exp(2e^T)` (OPEN).
(c) Ley P211-8E (`λ_A ≈ κ₈(1−χ_8)`, test de índice fijo 8 en la imagen exterior `E`): describe el FONDO del
cúmulo (un vector), no el cúmulo. La identificación «cúmulo = bloque prolato alto» (P211-9B: los vectores gauge
viven en el bloque alto, `k > 4N`) queda ARGUED/OPEN; la cuenta (2.2) muestra que el cúmulo producido por
`{M∗φ}` crece como `e^{2T}`, no es de tamaño fijo.

## §3 Estructura y signo del término de defecto

**Cociente (CITED, P2_SCHUR_001).** A `T = ∞`, `In(𝒲) = (0,0,dim 𝒜) + In(𝒲_BB)`; a `T` finito, la familia
es casi radical y la forma es `𝔡_T` sobre la familia más el cociente más el acople (P211-17A: la corrección
de Schur no es atribuible a ninguna parte; se cancelan). El cociente `P_T/{Π_Tφ}` es de codimensión infinita
(106_09: las direcciones casi radicales no son densas). La matriz `S_{T,k}` vive en `E_k`, que contiene el
cúmulo: el problema del signo está en el **acople cúmulo–complemento** y en `𝔡_T`, no en el cociente solo
(el complemento es coercivo con `c(T,k)`).

**Término principal de `𝔡_T(φ)` (ARGUED).** `R_φ` está concentrado en dos piezas en `|t| ≈ T−η + O(e^{−2(T−η)})`
(producto de `1−χ`, que se anula en orden finito, por un perfil `e^{−πe^{2t}}`), de anchura `w ≍ e^{−2T}`, luego
con frecuencia `≍ e^{2T}`. En `W_*(R_φ)`:
- diagonal arquimediana `(1/2π)∫m|R̂_φ|² ≈ (2T + O(1))‖R_φ‖² > 0` (`m(τ) ≈ log τ`);
- peine: autodesplazamientos `log n ≤ w` imposibles; cruce entre las dos piezas sólo para `log n ∈ 2T ± w`,
  `O(1)` enteros con `v_n ≈ 4Te^{−T}`: `|·| ≤ 4Te^{−T}‖R_φ‖²`, con signo `−` (coincide con ROUND_019_A (iii));
- Tate: `|A(R_φ)| ≤ e^{T/2}√w‖R_φ‖ ≍ e^{−T/2}‖R_φ‖`; aporte `O(e^{−T/2})‖R_φ‖²`.

Por lo tanto, a primer orden, `𝔡_T(φ) = (2T + O(1))‖(1−χ)(M∗φ)‖²·(1 + O(e^{−T/2}))`: **positivo**, dominado por
la diagonal arquimediana por un factor `≳ e^{T/2}`; la cola de primos con signo `−` pierde. Esto corrige la lectura
de ROUND_019_A (ii) en el sentido de que, con corte suave, las tres fuentes NO tienen la misma constante: la
arquimediana domina (ARGUED; el cálculo de ROUND_019_A usaba el corte de `X_T` y no fue rederivado).
Para la familia el término es la forma diagonal `φ ↦ ∫ 2T|(1−χ)(M∗φ)|²`, manifiestamente `≥ 0`.

**Pero no es una positividad útil.** (i) Es positividad del término principal de `a_T` sobre `{Π_Tφ}`, que ya es
`≥ 0` hasta `e^{−2πe^{2T}}`; el fondo `λ_A` lo fija el acople con el complemento (P211-17A), no `𝔡_T`.
(ii) El término principal es ciego al peso: la diagonal arquimediana del resto no ve `Λ`; `Λ` entra sólo en la
radicalidad de `M∗φ`.

## §4 Controles y lectura OBJECT_SPEC

Bajo `cΛ`: `a^{(c)}_T(Π_Tφ) = 𝔡_T(φ) + (1−c)·Arch_*(M∗φ)`, y `Arch_*(M∗φ) = Σ v_n c_{M∗φ}(log n)` es indefinido en
`φ` (`Arch_*(M) = −1.71`, positivo a frecuencia alta): el resto pierde el signo en el paso nombrado «`M∗φ` en el
radical» (F1 se cumple en el paso, ROUND_020_B §3). Borrar 2 o mover un generador: defecto
`Σ(w_n−v_n)c_{M∗φ}(log n)`, de orden `‖M∗φ‖²`, sin signo. Un enunciado de signo sobre la familia usaría O3
(producto de Euler + ecuación funcional + Γ en una línea: la radicalidad), O11/O12 (se rompe en los tres controles
en el paso de radicalidad); pero lo que daría (`𝔡_T ≥ 0` a primer orden) no toca el acople que fija el signo global.

## Veredicto

- Familia e identidad (1.1)–(1.2): PROVED (106_09 §3 con `φ` general; R160 Obs. C1). CITED en su núcleo.
- Cuenta inferior (2.2) `N_T(ε) ≳ (4/(πe))e^{2T}`: ARGUED (falta (2.1)); nueva en el corpus.
- Cúmulo dentro de `E_k` de (L2): PROVED como consecuencia de `thm:coer-schur`.
- Descomposición cociente + defecto: CITED (P2_SCHUR_001, P211-17A); no es nueva.
- Signo del término principal del defecto: positivo, arquimediano, ciego al peso: ARGUED; no es un paso de signo.
- Identificación con el bloque prolato alto de P211-8E/9B: OPEN.

**Siguiente operación única:** probar (2.1) (cota inferior de `∫|Ξ|²|φ̂|²` sobre prolatos de banda `Ω`), lo que
convierte (2.2) en PROVED y da el tamaño mínimo `≍ e^{2T}` del bloque que cualquier objeto de la fase debe resolver.
No se propone construcción de signo.
