# IV.1 — Identificación de `Â_∞`: operador de Sturm–Liouville de 2º orden (oscilación) Consolidación de E13/E14/E15 (mis corridas mpmath) + el frente analítico (IV1star-relative-gap).
La identificación ingenua "Laplaciano de Dirichlet" estaba refutada; la correcta es **clase
Sturm–Liouville / oscilación**, con carrier de borde. Conecta IV.1 con H1 (positividad). Marcadores: **[N]** numérico robusto · **[P]** probado · **[GAP]** residual nombrado. --- ## Hechos sólidos (E13/E14/E15, λ=7,9,11, mpmath dps=30) 1. **[N] El carrier es el borde de banda discreto, exacto:** `ω* = 2πN/(2N+1)` (medido por FFT del fundamental): `0.966π`(N=14), `0.970π`(N=16), `0.973π`(N=18) = `2N/(2N+1)·π` exacto. **No es `π`** (Nyquist) — de ahí el fracaso de de-modular por `(−1)^j` en E12.
2. **[N] Estado fundamental nodeless tras de-modular por `ω*`:** `0` cambios de signo, ∀λ. **Recupera el Perron–Frobenius de H1** (el `v_0` crudo tiene ~`N` cambios de signo = el carrier; quitándolo correctamente, es positivo). La similaridad que vuelve `QW` positividad-preservante es `D=diag(e^{iω*j})` (carrier de borde).
3. **[N] La paridad alterna `(−1)^k`:** modos `k=0,1,2,3,…` son `PAR, IMPAR, PAR, IMPAR,…` (E15, limpio ∀λ). **Firma inequívoca de operador de 2º orden** (autofunciones de un Sturm–Liouville simétrico alternan paridad). Coincide con la reducción analítica `ε_1/ε_0 = μ_O/μ_E` (impar más bajo / par más bajo) del frente IV1★.
4. **[N] Envelopes Sturmianos** (de-mod analítico, E14, λ=7): modos pares `k=0,2,4,6` → `0,2,4,6` nodos. (Ruidoso a λ mayor por mezcla par/impar y fase del Hilbert; el patrón par es limpio.) Consistente con oscilación (`v_n` tiene `n` nodos).
5. **[N] Espectro `n²` sólido:** `ε_k/ε_0 → (k+1)²` (λ=11: 4.02, 9.0, 16.1, 25.2, 36.5, 49.8). ## Lo que `Â_∞` NO es (refutado por overlaps) - **NO** Laplaciano de coef. constante (Dirichlet): node-count correcto pero **forma no sinusoidal** (overlap con `sin((k+1)π·)` sólo 0.1–0.6). Coeficientes variables.
- **NO** Hermite/oscilador armónico (overlap ≤ 0.40).
- **NO** prolato/DPSS (overlap ≈ 0.00). ## Identificación [N→P vía H1] > **`Â_∞` es un operador de Sturm–Liouville de 2º orden (matriz de oscilación,
> Gantmacher–Krein), en la representación de-modulada por el carrier de borde `ω*`:**
> - autofunciones de paridad alternante `(−1)^k`, fundamental nodeless, `v_n` con `n` nodos
> (Sturmianas);
> - espectro `ε_n ∝ n²` (ley de Weyl para operadores de 2º orden);
> - **coeficientes variables** (fijados por el dato arquimediano `θ'` + aritmético `Λ(n)`),
> por eso NO es el Laplaciano de coef. constante. **Por qué es 2º orden / oscilación — la ruta rigurosa (conecta con E1):**
H1 probó que `e^{−tQW}` es **positividad-preservante** (porque `Λ(n)≥0`, vía
Lévy–Khintchine + Schoenberg + Trotter). En la representación de-modulada `D⁻¹QW D`
(`D=diag(e^{iω*j})`), esto es la **propiedad de oscilación total** (Gantmacher–Krein):
una matriz de oscilación tiene autovalores simples `0<λ_1<λ_2<…` y la autofunción de `λ_k`
tiene exactamente `k−1` cambios de signo (Sturm), con paridad alternante. **Eso es
exactamente lo medido** (paridad `(−1)^k`, fundamental nodeless, Sturmianas). **[GAP-IV.1-residual]** Probar que `D⁻¹QW D` es **genuinamente** una matriz de oscilación
(total no-negatividad de los menores, Gantmacher–Krein) **a partir de H1** — H1 da
positividad-preservante (Perron–Frobenius, controla el fundamental); la total-no-negatividad
(que controla TODO el orden de Sturm) es un paso más fuerte, a derivar de la estructura
Loewner de `sin` (§II) + el signo `Λ(n)≥0`. Es la **misma positividad de H1 elevada de
"fundamental" a "todos los modos"**. ## Impacto cruzado en IV.1★ (gap relativo) La identificación **da `γ` directamente**: si `Â_∞` es 2º orden con espectro `n²`, entonces
``` ε_1/ε_0 → 2²/1² = 4 ⟹ γ = 3 > 0.
```
Y `ε_1/ε_0 = μ_O/μ_E` (impar/par) confirmado por la alternancia de paridad (E15). Así
**IV.1 e IV.1★ se cierran juntos** módulo el único residual: que la oscilación
(Gantmacher–Krein) se sigue de H1. La ley `n²` ya no es misteriosa — es **Weyl para el
operador de oscilación**, y el `γ=3` es `2²/1²`. ## Estado tras la identificación | Sub-pieza | Estatus |
|---|---|
| carrier = borde `2πN/(2N+1)` | **[N]** sólido |
| fundamental nodeless (de-mod) = H1 | **[N]+[P]** (H1 probado) |
| paridad alternante `(−1)^k` | **[N]** sólido |
| espectro `n²` (Weyl) | **[N]** sólido |
| autofunciones Sturmianas `n` nodos | **[N]** (par limpio; impar ruidoso) |
| **`Â_∞` = Sturm–Liouville 2º orden / oscilación** | **[N→P]** módulo Gantmacher–Krein |
| **IV.1★ `γ=3>0`** | **se sigue** de la identificación |
| **residual único** | **probar oscilación (Gantmacher–Krein) desde H1 (`Λ≥0`)** | **Veredicto:** IV.1 **identificado** (clase Sturm–Liouville/oscilación, no operador
nombrado de coef. constante), `n²`=Weyl, `γ=3` de regalo para IV.1★. Queda **un** residual,
y es de la familia de H1 (positividad total): elevar "positividad-preservante del
fundamental" a "oscilación total de todo el espectro". Mucho más concreto y conectado que
"identificar un operador misterioso". --- ## IV.1-res atacado: ruta Gantmacher–Krein REFUTADA (E16) Probé si `B = D·QW·D` (`D=diag((−1)^j)`, de-modulación real) es una **matriz de oscilación**
(total no-negatividad ⟹ Sturmian por Gantmacher–Krein). **NO lo es** (E16, λ=7,9):
- entradas `≥0` sólo **50%** (signos mixtos);
- off-diagonales inmediatas `B[i,i+1]` **negativas** (min `−0.66`, `−0.90`) — falla el requisito de oscilación;
- **15–22% de los menores 2×2 consecutivos `<0`** — viola TN. **Consecuencia:** la estructura Sturmiana **NO proviene de positividad total de matriz**
(Gantmacher–Krein). H1 da positividad-preservante (orden 1 = Perron–Frobenius del
fundamental); la total no-negatividad (orden completo) **es estrictamente más fuerte y
FALSA aquí**. La ruta "IV.1-res blando vía H1→TN" está **cerrada en falso**. **De dónde viene entonces la Sturmianidad (paridad `(−1)^k`, fundamental nodeless,
envelopes con `n` nodos):** de la estructura **diferencial de 2º orden (Sturm–Liouville)**
del *operador de borde* que gobierna el bajo-espectro del frame a densidad crítica — el
operador del *plunge* prolato / capa límite (cf. Nota IV.1★: "boundary-layer edge
operator"). Sturm oscilación es teorema para ODEs de 2º orden, **no** requiere TN matricial. ## Estado honesto FINAL de IV.1 **Identificado (numérico sólido):** `Â_∞` = operador de **2º orden tipo Sturm–Liouville**
(boundary-layer del frame crítico), carrier de borde `2πN/(2N+1)`, paridad alternante
`(−1)^k`, fundamental nodeless (= H1), espectro `n²` (Weyl), coef. variables. NO TN-matriz,
NO Dirichlet/Hermite/prolato-estándar. **Residual de IV.1 (no cerrado):**
> **IV.1-res' — Probar que el límite de escala `Â_∞` existe (Conj 2b) y que su bajo-espectro
> es el de un operador de 2º orden Sturm–Liouville (capa límite del frame crítico), con
> espectro `n²` y gap `ε_1/ε_0 → 4` (γ=3).** Es **análisis asintótico** (límite de Toeplitz/Loewner + operador de borde de Landau–Widom +
de Branges/Sturm–Liouville) — **duro pero NO RH-hard** (no es §V; no depende del signo de
`Λ(n)` globalmente, sólo de la geometría del frame a densidad crítica). **Veredicto:** IV.1 **NO se cierra del todo**. Queda **un** residual `IV.1-res'`
(identificación rigurosa del operador de borde 2º-orden + existencia del límite de escala),
de la familia de **teoría de aproximación / Sturm–Liouville**, no de la positividad RH-hard
§V. Pero IV.1 quedó **muy bien caracterizado**: sabemos QUÉ es `Â_∞` (SL 2º orden, n²=Weyl,
γ=3), por qué los autovectores no son Dirichlet (coef. variables), y por qué la ruta TN
falla. El `n²` y el `γ=3` son consecuencias de la estructura SL, condicionadas a `IV.1-res'`. --- ## IV.1b' atacado (idea del colaborador): SL confirmado CUALITATIVO, coef. constantes REFUTADOS Ataqué IV.1b' por reconstrucción de potencial (E17) y por fit carrier×caja (E18). Resultado: **Refutado — ninguna identificación de COEFICIENTE CONSTANTE / base uniforme:**
- E17 (V(x)=μ_k+φ_k''/φ_k común): residuales `0.45–0.87` (grandes), `V_k≈μ_k` (no común). *Confound:* carrier `32π/33` cerca de Nyquist ⟹ envelope vía Hilbert poco fiable.
- E18 (v_k = carrier × modo-caja_m): overlap `0.3–0.56`, best `m` errático, `m=k+1` casi nunca. **NO es caja libre de Dirichlet.**
- Sumado a E12/E14 (no Dirichlet, no Hermite, no prolato) y E16 (no matriz TN). **Confirmado — 2º orden CUALITATIVO (la firma robusta):**
- **Paridad alternante `(−1)^k`** (E15, limpio ∀λ) = firma decisiva de operador de 2º orden.
- Espectro `n²` (Weyl de 2º orden), fundamental nodeless, modos pares Sturmianos. **Lectura coherente:** `Â_∞` es un Sturm–Liouville de 2º orden de **COEFICIENTES VARIABLES**
`−(pφ')'+qφ=μwφ`. Eso explica TODO: el espectro es `n²` (Weyl, robusto a la coordenada),
la paridad alterna (SL simétrico), el fundamental es nodeless — PERO las autofunciones, en
la coordenada-`j` cruda, son **modos de caja DISTORSIONADOS** (por eso overlap ~0.5 repartido
entre varios `m`, y la `V` en coordenada-`j` sale no-constante/mensajosa). Las
identificaciones de coef. constante fallan **porque los coeficientes son variables**. **Residual afinado IV.1-res'':**
> Identificar los coeficientes variables `(p,q,w)` del SL límite (= la coordenada de
> Liouville) vía el límite continuo de la forma Loewner-contra-medida-arquimediana
> (Conj 2b + asintótica). HARD, **análisis** (no RH-hard). **Lo que el chain necesita YA está cualitativo:** "2º orden ⟹ `n²` Weyl ⟹ `ε_1/ε_0→4`,
`γ=3>0`". El `γ>0` se apoya en la naturaleza de 2º orden (paridad alternante + Weyl), que
es robusta; la identificación EXACTA del operador (IV.1-res'') es refinamiento, no bloquea
el `γ>0` cualitativo. **Veredicto IV.1 (honesto, metódico):** IV.1-res' **no cerrado**. Sub-atacado, se afinó a:
(i) 2º orden SL **confirmado cualitativo** (paridad + n² + nodeless); (ii) coef. **variables**
(todas las id. de coef. constante refutadas, con explicación); (iii) residual IV.1-res'' =
pinear `(p,q,w)`, análisis puro. El `γ=3` para IV.1★ se sostiene en (i). El límite de
resolución numérica (N≤20, carrier near-Nyquist) impide pinear (p,q,w) — haría falta N grande
o ataque analítico del operador de borde. --- ## Cierre analítico de IV.1 (sin Python) — estado final **Probado [P]:** (A) `QW` conmuta con paridad `J:j↦−j` ⟹ sectores par/impar; alternancia
`(−1)^k` = entrelazado `ε_0^E<ε_0^O<ε_1^E<…`. (B) En el continuo, `QW_∞` es operador
integral de **núcleo de Loewner acotado** ⟹ **compacto** (autovalores acumulan en 0). **No cerrado [GAP analítico]:** (C) por (B), el operador COMPLETO es suavizante, NO
diferencial — el carácter 2º orden vive en el **operador efectivo de capa límite** del borde
de banda `t=±Ω` tras renormalizar `/ε_0~λ²` (carrier medido `2πN/(2N+1)`=borde confirma).
(D) derivar ese operador de borde y su espectro `n²` (Landau–Widom/semiclásico) NO se logró:
los perfiles conocidos no dan `n²` (plunge prolato=logístico; oscilador=`2n+1`). El `n²`
queda robusto numérico pero analíticamente underivado. **VEREDICTO FINAL IV.1:** probado = PSD + paridad-simetría + forma Loewner compacta.
Fenomenológico (no probado) = 2º orden / `n²` / `γ=3`. Se ACEPTA IV.1 a este nivel
(decisión metódica: no forzar un teorema) y se avanza a IV.2. El residual real de IV.1 es
**análisis de capa límite del frame crítico** (Landau–Widom), NO RH-hard, NO §V.
