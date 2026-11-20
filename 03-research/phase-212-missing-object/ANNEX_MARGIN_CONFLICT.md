# Anexo: el conflicto sobre el margen de λ_A(T)

Nota de referencia. Resuelve la contradicción registrada en `05-meta-and-planning/ROUTES-MASTER-INDEX.md`
(l.66, l.590–592, l.833–837, l.4351, l.4484, l.4724, l.4849, l.4979, l.5306) entre la cota doblemente
exponencial y la cota simplemente exponencial para el fondo `λ_A(T) = λ_min(a_T|P_T)`. Donde una fuente
menciona el enunciado famoso, se escribe «[H]».

Notación de Paper 47 (P47): `a_T(F) = C₀‖F‖² + 𝔈(c_F) − Σ_n v_n c_F(log n)`, `P_T = {A(F) = B(F) = 0}`,
`A(F) = ∫F e^{t/2}`, `B(F) = ∫F e^{−t/2}`, `W_T = a_T + 2AB` (def:W, eq:W), `λ_A = λ_min(a_T|P_T)` (fondo
«primitivo restringido»), `λ_P` = fondo sobre el cono `K_prim` (def:PD), `λ_W = λ_min(W_T)` sobre todo el
dominio (fondo «completo»). Normalización: `‖·‖ = L²(I_T)`.

---

## §1 Enunciados exactos

**(S1) R160_M4_R1, Teorema B(i)** (`03-research/phase-160-row-d-infinite-T/R160_M4_R1.md`, l.334–336):

> «There are absolute effective constants `C, c, T₀` such that for every `T ≥ T₀`:
> (i) *(upper)* `𝔤̃_ev(T), 𝔤̃_odd(T) ≤ Ce^{cT}e^{−2πe^{2T}}`, and
> `λ^W_T ≤ λ^prim_T ≤ λ^A_T ≤ Ce^{cT}e^{−2πe^{2T}}` [both].»

Cantidad: `λ^A_T = λ_min(A_T|P_T)` con las definiciones de P47 «verbatim» (l.157–161; misma `a_T`, mismo
`P_T`, norma `L²`). Rango: `T ≥ T₀` (no explícito). Etiqueta: PROVED, «unconditional» (tabla l.54).
Nota de registro R1 (l.62, Remark B4 l.393–398): la ley doblemente exponencial «is already in 106.09 Thms 2–3».

**(S2) Panel R160_PC_R1** (`R160_PC_R1.md`, l.198–202):

> «Thm B(i): `X_T = Mχ_T − a u_ev ∈ P_T` (even, `ℓ_ev = 0`), `𝔞_T(X_T) = W_*(X_T − M) = W_*(−E^M_T − a u_ev)
> ≤ Ce^{cT}e^{−2πe^{2T}}`, `‖X_T‖ ≥ ½‖M‖`. Verified. Hence `λ^A_T ≤ Ce^{cT}e^{−2πe^{2T}}`, unconditional.»

**(S3) G2_B6_R2, Teorema M / Corolario M1** (`03-research/phase-159-row-d-two-front-construction/G2_B6_R2.md`,
l.15–17, l.191–194):

> «Theorem M (PROVED, unconditional, new): for every `ε > 0` and every `T ≥ T₀(ε)`,
> `λ^W_T ≤ λ^P_T ≤ λ_min(A_T|P_T) ≤ exp(−e^{(2−ε)T})`.»

Misma cantidad `λ_min(A_T|P_T)`. Etiqueta PROVED. (No se re-deriva aquí: (S1) la contiene y la mejora.)

**(S4) 106_09, Teorema 3** (`03-research/phase-106-global-modular-star-audit/106_09_NEAR_RADICAL_CLUSTER_AND_GAP_COLLAPSE.md`,
l.291–301, §6 l.410–416):

> «For all sufficiently large `L`, `μ⁺_{1,L} ≤ ε_L`, `μ⁻_{0,L} ≤ ε_L`», `ε_L = Cλ^M e^{−cλ²}`, `λ = e^L`;
> «Unconditional: the truncated Riemann-kernel derivative spaces have Weil matrices `O(λ^M e^{−cλ²})`».

Cantidad: autovalores (segundo par, primero impar) de la forma completa `QW` en `[−L, L]`, no `λ_A`
directamente. Etiqueta propia: unconditional. Remark B4 de (S1) afirma que el espacio de prueba
`span{v₀, v₂}` contiene un vector con `ℓ_ev = 0`, lo que transfiere la cota a `λ^A`.

**(S5) Paper 47, thm:margin y cor:margin1** (`04-papers/47-row-d-dual-certificates/main.tex`, l.3530–3580):

> «For every `T ≥ 1`, `λ_W ≤ λ_P ≤ λ_A ≤ 4·10⁹ T e^{−15.449 T}`.»

Cantidad: `λ_A` de P47. Rango `T ≥ 1`. PROVED (prueba vía la fórmula explícita sobre `P_T`, lem:roughEF,
con un vector de prueba que anula sólo el primer cero; nota al pie: «a property of that family, not a sharp
rate»). rem:moriceiling (l.3582–3591): cita una cota `exp(−4π e^{2T})` de Mori **para `λ_W`**, «plausible,
unverified»; «It bounds `λ_W ≤ λ_A` and so does not replace Corollary cor:margin1 as a bound on `λ_A`.»

**(S6) Paper 48 §subsec:margin** (`04-papers/48-row-d-route-map/main.tex`, l.265–276):

> «A doubly exponential upper bound `exp(−e^{(2−ε)T})` for `λ_A` is *not* proved; earlier versions of this
> map stated it as a theorem, and that statement is withdrawn.»

Fuente declarada de la retirada (tabla l.945): «index correction after the shape theorem of P47». Ningún
paso de (S1) ni de (S3) es señalado como fallido.

**(S7) Índice 06, entrada [margin]** (`ROUTES-TRIED-INDEX/06_OPEN_RESIDUES_DEAD_SUBROUTES.md`, l.19 en HEAD):

> «The doubly exponential estimate cited in P47 rem:moriceiling concerns λ_W, is recorded there as
> unverified, and must not be transferred to λ_A (λ_W≤λ_A has the wrong direction for that transfer).»

---

## §2 ¿Es la misma cantidad?

(S1), (S2), (S3), (S5), (S6) hablan todos de `λ_A(T) = λ_min(a_T|P_T)` con la normalización de P47.
(S1) declara usar las definiciones de P47 textualmente, y su `𝔞_*` (D3) restringido a `𝒟_T` coincide con
`a_T` (`Σ (v_n/2)[c(log n) + c(−log n)] = Σ v_n c(log n)` por simetría de `c_F`).

(S7) habla de **otra** estimación: la de Mori citada en rem:moriceiling, que acota `λ_W`. La relación es
`λ_W ≤ λ_P ≤ λ_A` (P47 rem:Kprim: `W_T = a_T` cuando `A·B̄` es imaginario puro, y `P_T ⊂ K_prim`; CITED,
P47). Por tanto una cota superior de `λ_W` no da nada para `λ_A`; (S7) tiene razón **sobre Mori**.

El error está en la propagación: el índice maestro (l.592, l.4351, l.4484, l.5306) y P48 aplicaron la
corrección de (S7) al Teorema M y a (S1), que no pasan por `λ_W`: ambos construyen un vector de prueba
**dentro de `P_T`** y acotan `a_T` directamente. Las dos cotas doblemente exponenciales del corpus son,
pues, distintas: la de Mori (`λ_W`, CITED no verificada) y la de (S1)/(S3) (`λ_A`, memo PROVED).

---

## §3 La prueba de (S1) y su control

Objetos (R160_M4_R1 §1): `K_Pó(t) = Σ_n (4π²n⁴e^{9t/2} − 6πn²e^{5t/2}) e^{−πn²e^{2t}}`, con `Φ_{K_Pó} = ξ`
(P46 Def–Thm 11.7, (11.9)); `M := −K_Pó″ + ¼K_Pó`, de modo que `Φ_M(s) = s(1−s)ξ(s)`, `A(M) = B(M) = 0`,
`M` par y no nulo. Corte `χ_T ∈ C_c^∞(I_T)`, `χ_T = 1` en `[−T+θ, T−θ]`, `θ = e^{−2T}`. Cola
`E := M(1−χ_T)`. `u_ev ∈ C_c^∞(−½,½)` par con `ℓ_ev(u_ev) = 1`; `a := −ℓ_ev(E)`.

**Vector de prueba:** `X_T := Mχ_T − a u_ev ∈ C_c^∞(I_T)`, par, `ℓ_ev(X_T) = 0`, luego `A = B = 0`: `X_T ∈ P_T`.

Pasos y control:

1. **`W_*` en el radical (Lema 2(a),(c)).** Para `X, Y` en la clase de Weil `D^W`,
   `W_*(X,Y) = Σ_ρ Φ_X(ρ)Φ_Y(1−ρ)` (fórmula explícita, P46 Thm 11.3; CITED). Como `Φ_M` se anula en todo
   cero de `ξ` **dondequiera que esté**, `W_*(M, ·) ≡ 0`. No usa ninguna información sobre la posición de
   los ceros: correcto. La extensión a `Z ∈ 𝒟_T` usa densidad de `C_c^∞(I_T)` y la cota 2(b).
   *Control:* para `Z ∈ C_c^∞(I_T) ⊂ D^W` la identidad es directa; 2(b) es Cauchy–Schwarz más
   `m ≤ C₀ + c(1+|τ|)` y Plancherel. Correcto.
2. **Coincidencia de formas.** Para `X_T ∈ C_c^∞(I_T)`, `c_{X_T}(log n) = 0` si `log n ≥ 2T`, así que la
   suma sobre todo `n ≥ 2` de `W_*` coincide con la suma truncada de `a_T`; y `W_T(X_T) = a_T(X_T)` porque
   `AB = 0`. Es la misma identidad que P47 usa en el paso (2) de thm:margin (lem:roughEF). Correcto.
3. **Reducción a la cola.** `X_T − M = −(E + a u_ev) =: −Y`, `Y ∈ D^W`, par, `ℓ_ev(Y) = 0`. Por el paso 1,
   `a_T(X_T) = W_*(X_T) = W_*(Y) = W_*(E) + 2a W_*(u_ev, E) + a² W_*(u_ev)`. Correcto (bilinealidad).
4. **Tamaño de la cola (Lema 3).** `|K_Pó^{(j)}(t)| ≤ c_j e^{(9/2+2j)|t|} e^{−πe^{2|t|}}`; en el soporte de
   `E`, `e^{2|t|} ≥ e^{2T} − 2`, y `|χ_T^{(k)}| ≤ c_k e^{2kT}`. De ahí `‖E‖_{H¹}, ∫|E|e^{|t|/2}, |a| ≤
   Ce^{cT}e^{−πe^{2T}}`. *Control:* correcto; el factor `θ^{−k}` es sólo `e^{2kT}`, absorbido en `e^{cT}`.
5. **`|W_*(E)| ≤ Ce^{cT}e^{−2πe^{2T}}`.** Término `2AB(E)`: producto de dos cantidades `O(e^{cT}e^{−πe^{2T}})`.
   Término arquimediano: `≤ C‖E‖²_{H¹}`. Primos con `log n ≤ 2T+1`: `Σ v_n ≤ Ce^T` por `‖E‖²`. Primos con
   `log n > 2T+1`: `|c_E(log n)| ≤ ‖E‖_{L¹} sup_{|s| ≥ (log n)/2}|E(s)|`, y el supremo es `≤ e^{−πn^{…}}`;
   la memoria escribe «`O(e^{−πe^{2T+1}})`» para la suma, lo que es descuidado (falta el factor `‖E‖_{L¹}`),
   pero con ese factor el término es `≤ Ce^{cT}e^{−πe^{2T}}·e^{−πe^{2T+1}} ≤ Ce^{cT}e^{−2πe^{2T}}`; y aun
   sin él, `e^{−πe^{2T+1}} ≤ e^{−2πe^{2T}}` porque `e > 2`. Correcto.
6. **Términos cruzados.** `|W_*(u_ev, E)| ≤ Ce^{T/2}‖u_ev‖ 𝔪_T(E)` (Lema 2(b)) y `|a| ≤ Ce^{cT}e^{−πe^{2T}}`
   dan `O(e^{cT}e^{−2πe^{2T}})`; `a² W_*(u_ev)` idem (`u_ev` fijo). Correcto.
7. **Normalización.** `‖X_T‖ ≥ ‖M‖ − ‖E‖ − |a|‖u_ev‖ ≥ ½‖M‖` para `T ≥ T₀`, luego
   `λ_A ≤ a_T(X_T)/‖X_T‖² ≤ 4Ce^{cT}e^{−2πe^{2T}}/‖M‖²`. Correcto.

**Qué paso declara fallido P48 u otra fuente:** ninguno. P48 retira el enunciado sin señalar un paso; su
única fuente declarada es la corrección del índice (S7), que se refiere a la cota de Mori sobre `λ_W`.
Ninguna memoria posterior localizada objeta el Lema 2, el Lema 3 o el vector `X_T`.

**Paso más débil, según este control:** el Lema 2(a) aplicado a pares en `D^W` sin soporte compacto: la
fórmula explícita para funciones de decaimiento `O(e^{−(1+ε)|t|})` con dos derivadas, con la suma de primos
sobre todo `n` y la suma sobre ceros absolutamente convergente. Es la versión estándar de la fórmula
explícita de Weil (P46 Thm 11.3, (11.2), (E3d)); la convergencia absoluta de `Σ_ρ Φ_X(ρ)Φ_Y(1−ρ)` para
`X, Y ∈ D^W` se sigue de `Φ_{g″}(s) = (s−½)²Φ_g(s)` (dos integraciones por partes) y de la densidad de
ceros. Lo considero correcto; queda como dependencia CITED de P46, no re-derivada aquí línea por línea.
Las constantes `C, c, T₀` no son explícitas: la cota no es numéricamente utilizable en una ventana dada.

---

## §4 Veredicto y consecuencias para OBJECT_SPEC

**Veredicto: (b).** Para `λ_A(T)` sobre `P_T` tal como lo define P47, está probado (memoria R160_M4_R1,
Teorema B(i); verificado por el panel R160_PC_R1; re-controlado paso a paso en §3):

  `λ_A(T) ≤ C e^{cT} e^{−2π e^{2T}}`  para `T ≥ T₀`, con constantes absolutas efectivas no explicitadas.

Etiqueta honesta: **PROVED (en el corpus de memorias), dependiente de P46 Thm 11.3 (CITED)**, no integrado
en P47. Lo que P47 contiene como teorema del paper es sólo la cota simple (S5), PROVED con constantes
explícitas para `T ≥ 1`. La retirada de P48 y las entradas del índice que dicen «doble exponencial no
probada para `λ_A`» proceden de transferir a (S1)/(S3) una corrección escrita para la cota de Mori sobre
`λ_W` (S7); esa transferencia es incorrecta. (S7) sigue siendo correcto respecto de Mori. El Teorema M
(S3) queda superado por (S1) y no se re-deriva aquí. 106_09 (S4) es una cota de autovalores de la forma
completa; su transferencia a `λ_A` depende de Remark B4 (vector con `ℓ_ev = 0` en el espacio de prueba),
que no se re-controla aquí y no es necesaria, porque (S1) da directamente el vector `X_T ∈ P_T`.

Mientras P47 no incorpore (S1), lo citable en un paper es (S5); en las notas de la fase 212 se usa (S1).

**Consecuencias para el objeto.**

- Con (S1): una identidad «`a_T = expresión no negativa + resto`» que pretenda dar el signo debe controlar
  el resto con precisión relativa por debajo de `Ce^{cT}e^{−2πe^{2T}}` en la ventana `T`; ya en `T = 2`
  eso es del orden de `e^{−340}`. Toda cota perturbativa, de compacidad o de brecha más grosera no decide el
  signo. En particular el término «manifiestamente no negativo» no puede tener mínimo sobre `P_T` acotado
  inferiormente por nada mayor; tiene que anularse (a esa escala) sobre el truncado `Mχ_T` del núcleo de
  Riemann, que es un casi-vector nulo explícito del objeto. Esto es un falsificador interno útil: el
  objeto debe evaluar `X_T` en `O(e^{cT}e^{−2πe^{2T}})`.
- Con sólo (S5): el umbral sería `4·10⁹Te^{−15.449T}`, mucho más permisivo; diseñar con ese umbral
  subestimaría la precisión necesaria en una escala doblemente exponencial. Por (S1), el umbral de diseño
  correcto es el doblemente exponencial.
- (S1) es sólo cota superior: no da información sobre el signo (B(ii) de la misma memoria da la
  dirección inversa sólo hasta un defecto `e^{cT}e^{−πe^{2T}}`, sin signo).

**Corrección pendiente (para quien edite el índice y P48, no hecha aquí):** las entradas l.592, l.837,
l.4351, l.4484, l.5306 del índice maestro y P48 l.275–276 deben distinguir la cota de Mori (`λ_W`, CITED no
verificada) de la de R160_M4_R1 B(i) (`λ_A`, PROVED en memoria, no integrada en P47).
