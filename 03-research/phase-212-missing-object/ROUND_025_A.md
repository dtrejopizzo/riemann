# ROUND_025_A — Cotejo de antecedentes: esquema «existencia + rigidez» (WF)/(R)/(E) contra Paper 47 y fases 153–160, 197

Etiquetas: PROVED / CITED / CONDITIONAL / OPEN / NO-GO. Revisión de novedad y lógica; no se deriva nada nuevo.

## 0. Qué se abrió
- Paper 47 (`04-papers/47-row-d-dual-certificates/main.tex`): def:PD (l.668), def:W y thm:Z (l.1224–1300),
  prop:finite (l.3156–3180), rem:regimes, lem:cpos, thm:finmod (l.3228–3258), rem:resweights (l.3260–3292),
  lem:degen (l.3294–3313), prop:finsupp (l.3316–3334), cor:void (l.3336–3362), rem:twohalves (l.3364–3378).
- `phase-155-.../R155_053_ROUND8B_P6_ALIGNMENT.md` §1 (Prop 1.1, 1.3); README fila R155_053.
- `phase-197-barrier-theorem/BARRIER_Y_001_...md` (completo; 102 líneas).
- `phase-159-.../G2_B9_R3.md` §3 (Teoremas N, R′, Cor R1′, Rem 3.1–3.4), §4.
- `phase-160-row-d-infinite-T/R160_M2_R1.md` §0, §2 (T1, T8), §4 (Thm 4.1–4.3), §6 (Prop 6.1), §7.
- Índice maestro: l.5205–5211, 4733, 4778, 12192.
- No abiertos íntegramente: fases 153–154 más allá del grep (sólo multiplicadores de Lagrange de la restricción de
  Tate y β₀=2, que son otra cosa); thm:TK/prop:TK, Theorem X, prop:nearfree, rem:bar-arith, prop:spec del paper (grep
  sin relación con peso libre en el peine). G2_B6_R5 (Prop C) no abierto.

## 1. ¿Peso fijo o libre en el paper?
- El LP de certificados (def:PD, l.668; thm:Z, l.1240) tiene el peine **fijo** en v: «Fix T and the weights v»
  (l.665). La «weight» w de def:W/thm:Z es un peso flat-top del **lado del test** (w≡1 en [−2T,2T]), no un peso del
  peine; Theorem Z/TK no varían el peine.
- El peine **libre** aparece en el §«A fixed window is a finite condition»: prop:finite(ii) (l.3159–3163) define
  𝒱_T = {v ∈ ℝ^{N_T}: 𝔞^{(v)}_T ≥ 0 en P_T}, cerrado y convexo, como intersección de semiespacios — es exactamente
  el K_T de la propuesta. lem:degen (l.3294–3302) introduce μ_T(v) cóncava y el caso «minimizador con c_F(log n)=0
  ∀n ∈ N_T» ⟹ v_T(Λ) maximiza μ_T. R155_053 Prop 1.1/1.3: el contenido aritmético es la uniformidad en T de v_T ∈ 𝒟_T.

## 2. (WF) — enunciado sin peso
**Está, con otro nombre.** R160_M2_R1:
- D5 (l.110–113): test «prime-blind» si c_F(log n)=0 ∀n ∈ N_T; Z^A_T (puro) y Z^prim_T (relajado, estados mixtos /
  autocorrelaciones positivas definidas) = ínfimo de la energía arquimediana sobre tests prime-blind.
- Thm 4.1 (l.240–256, PROVED): dualidad fuerte max_v V^prim_T(v) = Z^prim_T, con 𝒪^prim_T = ∂g_T(0): «the best possible
  comb at window T is the Lagrange multiplier of a problem in which the primes enter only through their positions»
  (l.259–260). Es la frase «v como multiplicador de Lagrange» de la propuesta.
- Thm 4.3(a) (l.272, PROVED): 𝒱_T ≠ ∅ ⟺ V*_T ≥ 0; 𝒱^prim_T ≠ ∅ ⟺ Z^prim_T ≥ 0. Esto es (WF) (versión mixta = prim).
  Thm 4.2 sandwich Z^prim_T ≤ V*_T ≤ Z^A_T: para estados puros sólo hay desigualdad; la propuesta debe usar la versión
  relajada para tener Farkas exacto (el corpus lo hace así; la versión pura no es un dual exacto).
- §7.1 (l.398–402): (PBP_T) «prime-blind positivity» registrado como OPEN para T > log 2 (puro) y T > 0.8 (relajado).
- Índice l.5209 / l.12192: «Función valor cóncava V_T / caracterización variacional de Λ» → **DEAD [F3: Λχ₂]**:
  𝒱_T, V*_T, Z^A_T, Z^prim_T son ciegos a los primos (Rem 4.6, l.304–305: Λχ₂ comparte 𝒱_T con ζ y falla).
- BARRIER_Y_001 es Farkas para otra clase (cono de mayorización {0,1}); no es (WF).

## 3. (R) — rigidez
**Está.** G2_B9_R3 Theorem R′ (l.204–219, PROVED, incondicional): para b ∈ 𝒯_meas∖{0} (incluye b ∈ ℓ¹_w, Σ|b_n|n^{−1/2}<∞),
Λ+b no es ∀T-positivo (primitiva y completa); el conjunto ∀T-positivo en Λ+𝒯_meas es {Λ} o ∅ (Thm N(iii), l.181).
La prueba usa D_b(τ)=Σ b_n n^{−1/2}·2cos(τ log n) y sup D_b > 0 por media casi periódica (l.218–219): el mismo
mecanismo «polinomio de Dirichlet sin término constante ≤ 0 ⟹ nulo» del esbozo. Rem 3.3 (l.243–249): interior vacío
en toda dirección sumable. Índice l.5210, l.4778.
Diferencia: la propuesta enuncia (R) para **todo** w real; el corpus sólo para w − v ∈ 𝒯_meas. El esbozo de la propuesta
tampoco cubre más: para d no sumable D(τ) no está definido como función casi periódica, y vectores radicales con
a^v pequeño no controlan Σ d_n c_X(log n) cuando d crece. **Ese hueco es exactamente el paso (iii) del corpus.**

## 4. (E) — pegado existencia ⟹ signo
**Está.** R160_M2_R1 Prop 6.1 (l.359–367, PROVED como implicación): si (i) Z^prim_T ≥ 0 ∀T [= K_T ≠ ∅ ∀T], (ii) una
selección de multiplicadores v*_T converge coordenada a coordenada a un peine a*, (iii) a* − Λ ∈ 𝒯, entonces la
positividad ∀T de a*, y a* = Λ si a* − Λ ∈ 𝒯_meas. T1 (l.16): 𝒱_T compacto; T8 (l.24, Prop 2.4): la restricción
π^{T′}_T lleva 𝒱_{T′} en 𝒱_T — el «límite inverso» de la propuesta.
Única pieza técnica que la propuesta mejora: (ii). El corpus pide una selección convergente y declara OPEN la cota
uniforme (§7.6, l.412). La propuesta usa el límite inverso de compactos no vacíos (π^{T′}_T(K_{T′}) encajados), que da un
w ∀T-positivo **sin** cota uniforme. Es correcto y elimina (ii), pero es un detalle de compacidad estándar.

## 5. Por qué no cerró en la fuente
- R160_M2_R1 §6 (l.369–376): «(iii) is where the whole of the arithmetic sits: Λ ∉ 𝒯 (masa ≍ √X) … la proposición
  reubica el signo en (iii) sin debilitarlo»; «shape, not a mechanism». §7.7 (l.414–415): la ubicación exacta del muro.
- G2_B9_R3 Rem 3.2 (l.238–241): R′ «fija el candidato pero no decide su pertenencia»: la existencia de un elemento ∀T-positivo
  es todo el contenido [H].
- Falsificador Λχ₂ (Rem 4.6): K_T es ciego a los primos; (WF) es idéntico para Λ y Λχ₂. No refuta (E) lógicamente
  (el w producido no tiene por qué ser Λχ₂), pero confirma que (WF) no usa los valores exactos de Λ, y que todo el
  peso aritmético pasa a la rigidez (R) para w arbitrario, que es (iii) sin debilitar.
- cor:void / thm:finmod / prop:finsupp del paper: rigidez parcial por ventana (peines finitos fallan para T grande);
  coherentes con (R), no la amplían.

## 6. Observaciones lógicas adicionales
1. (WF) con estados mixtos requiere cierre del cono (κ_T(ρ), Arch(ρ)); el corpus lo resuelve con 0 ∈ int dom g_T
   (Thm 4.1 paso 2). Con estados puros sólo hay sandwich.
2. Acotación de K_T: corpus T1 (V_T ≤ C_T − c_T|v|), PROVED; no es problema por ventana.
3. El peine w obtenido por límite inverso es arbitrario (posiblemente no tempered); sin (R) global el esquema no cierra.

## 7. Veredicto
**REPETICIÓN** (con un ajuste técnico menor). (WF) = R160_M2_R1 Thm 4.1/4.3 + (PBP_T); (R) = G2_B9_R3 Thm R′/N en
Λ+𝒯_meas; (E) = R160_M2_R1 Prop 6.1, ya calificada en la fuente como «forma, no mecanismo», con la aritmética en (iii),
y la entrada del índice l.5209 la marca DEAD [F3: Λχ₂]. Lo único no registrado es sustituir (ii) por el límite
inverso de compactos, que no toca (iii). Reabrir exige una prueba de (R) para pesos **no** tempered (fuera de 𝒯),
que es justamente el paso abierto §7.7 de R160_M2_R1; sin ese mecanismo la propuesta no pasa el filtro.
