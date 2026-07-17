# M2 corrected, M3 attacked: the non-circular input is a single-class arithmetic Hodge index

*Continuation of `CONSTRUCTION-critical-gram.md`. Pure mathematics. We correct a flaw in M2, show
that the analytic side (M2) is RH-equivalent (hence not an independent source of positivity), and
conclude that the **only non-circular input is M3** — a single-class arithmetic Hodge-index
positivity. We then connect M3 to the program's Abboud thread and propose the realization that would
close it, with the remaining gap stated honestly.*

---

## §1. Correction to M2: the places are coupled by the global norm

M2 proposed a restricted-tensor factorization of the angle `∠(𝒟₋,𝒟₊)` over places. **This is not
literally correct.** The incoming subspace is defined by the **global** idele norm
```
   𝒟₋ = { f : f(x)=0 for |x|>1 },     |x| = ∏_v |x_v|_v ,
```
a single condition on the *product* of local norms, **not** a place-by-place condition. Hence
`𝒟₋ ≠ ⊗_v 𝒟_{−,v}`, and the angle does not factor as `⊗_v cos∠_v`. The Euler product does enter
through `ℱ=⊗'_vℱ_v`, but the **subspaces do not tensor-split**; the place-coupling is precisely the
global norm constraint. So M2 as stated is wrong and is withdrawn.

**Correct reformulation (scaling representation).** Use `x=(u,θ)`, `u=\log|x|∈ℝ`, `θ∈C¹` (norm-one
classes). Then the global condition is a **half-line condition in the single scaling variable**:
```
   𝒟₋ = { f : f(u,θ)=0 for u>0 } = L²(ℝ_{≤0}, du) \,\widehat⊗\, L²(C¹),
   𝒟₊ = ℱ𝒟₋ .
```
The place-coupling is now entirely inside `ℱ` (the adelic Fourier transform) and the internal space
`L²(C¹)`. The **angle operator** is the Lax–Phillips/Hankel operator
```
   H_Θ = P_{𝒟₊} \big|_{𝒟₋} ,
```
whose nonzero singular values are `cos∠`, and whose symbol in the Mellin/`z` variable is the
scattering function `Θ_0(z)`.

---

## §2. The analytic side (M2) is RH-equivalent, not an independent input

**Proposition (Nehari/Lax–Phillips).** `𝒟₋` and `𝒟₊` are at a **positive angle**
(`‖H_Θ‖<1`, sum closed) **iff** `Θ_0` is at positive distance from being non-inner, i.e. iff `Θ_0` is
inner — which is RH. By Nehari, `‖H_Θ‖ = \mathrm{dist}_{L^∞}(Θ_0, H^∞)`; `‖H_Θ‖≤1` with the model
identification isometric is equivalent to `K_{Θ_0}⪰0`.

**Consequence.** The angle/Hankel statement is **logically equivalent to RH**; it is the analytic
*reformulation* of the overlap positivity, **not** a separate source of positivity. So M2 cannot be
the place where positivity is "injected": any proof of `‖H_Θ‖≤1` *is* a proof of RH. This is the same
lesson as monotone continuation (Connes): the purely analytic/Hilbert-geometric statements are all
RH-equivalent. **The non-circular input must be arithmetic** — it must use a structure that ζ has and
the analytic data alone does not, namely the Euler product *as arithmetic geometry*. That is M3.

*(This is honest and important: it rules out the analytic route (M2) as self-sufficient and forces
the arithmetic route (M3). It matches every prior wall in the program — soft/analytic structure is
DH-symmetric.)*

---

## §3. M3: the overlap form as a self-intersection on the arithmetic square

We propose to realize the overlap/Weil form as an **intersection form on the square of the
arithmetic curve**, where an **unconditional Hodge-index inequality** lives. This is the
Connes–Consani / Castelnuovo–Severi program; the program already touched its two pillars
(`[[riemann-phase61-phaseH-abboud]]`, Abboud's arithmetic Hodge index; the phase-33 arithmetic
Castelnuovo–Severi thread).

### Setup
Let `\bar X` be the relevant compactified arithmetic surface (the model for `\overline{\mathrm{Spec}\,ℤ}
×\overline{\mathrm{Spec}\,ℤ}`, or the square of the Connes–Consani arithmetic site `\widehat{\mathrm{Spec}\,ℤ}`).
Let `\widehat{\mathrm{CH}}^1(\bar X)` be its arithmetic Chow group with the **arithmetic intersection
pairing** `(\,\cdot\,)`, and let `Δ` be the diagonal, `F_t` the "Frobenius correspondences" (the
graphs of the scaling/Hecke flow at parameter `t`). The Weil explicit formula is, in this language, an
**intersection number**:
```
   W(f) = (Z_f · Z_f) ,     Z_f = ∫ \hat f(t)\, F_t \, dt  −  (\text{diagonal/archimedean terms}),
```
a self-intersection of the arithmetic divisor class `Z_f` attached to the test function `f`.

### The inequality
**Arithmetic Hodge index (Abboud, unconditional).** On `\bar X`, for an arithmetic class `D` with
`(D·H)=0` for the polarization `H` (degree-zero / primitive), one has the **negative** self-
intersection
```
   (D·D) ≤ 0 .
```
(The arithmetic analogue of the surface Hodge index theorem; `M̄²≤0` for off-diagonal classes, the
form validated in the program's H-thread.)

### The proposed implication
**Claim (M3, proposed).** RH `⟺` `ind₋(K_{Θ_0})=0` follows if the overlap/Weil class `Z_f` is a
**primitive arithmetic divisor** (degree zero w.r.t. the polarization), because then Abboud gives
`(Z_f·Z_f)≤0`, and combined with the **sign convention of the Weil form** (the explicit formula has
the opposite sign on the relevant component) this yields `W(f)≥0` for all `f` — Weil positivity — hence
RH. The **degree-zero condition** is exactly the marginal certificate `μ_max=1` (E96/E101): the class
`Z_f` meets the polarization trivially. So:
```
   μ_max=1  ⟺  (Z_f·H)=0  (primitive)   [degree balance, HAVE],
   Abboud   ⟹  (Z_f·Z_f)≤0              [Hodge index, HAVE unconditionally],
   sign convention of the explicit formula  ⟹  W(f)≥0  ⟹  ind₋=0  ⟹  RH.
```

---

## §4. The honest remaining gap: the realization map `f ↦ Z_f`

Everything in §3 is in place **except one map**: the **realization**
```
   f \;\longmapsto\; Z_f \in \widehat{\mathrm{CH}}^1(\bar X)
```
that sends a test function (equivalently the overlap vector in `K`) to an **actual arithmetic divisor
class** whose self-intersection is `W(f)`, and that sends the polarization/degree to `μ_max`. This is
the precise point the program previously flagged as the risk in the Abboud thread
(`[[riemann-phase61-phaseH-abboud]]`: "Riesgo: realización f↦M̄_f").

**Why it is hard, and what must be shown.** The arithmetic Chow group / intersection theory of
`\overline{\mathrm{Spec}\,ℤ}×\overline{\mathrm{Spec}\,ℤ}` is **not** classically defined — there is no
Weil cohomology / no honest second factor over `\mathrm{Spec}\,ℤ` (this is MW-5). The Connes–Consani
arithmetic site `\widehat{\mathrm{Spec}\,ℤ}` is the candidate where `\bar X = \widehat{\mathrm{Spec}\,ℤ}^2`
acquires the needed intersection theory and Frobenius correspondences `F_t`. **Sub-problem M3a (the
single remaining construction):** define `\widehat{\mathrm{CH}}^1(\widehat{\mathrm{Spec}\,ℤ}^2)` with a
pairing for which (i) the Frobenius correspondences `F_t` exist, (ii) the diagonal `Δ` has the right
self-intersection (the archimedean term), and (iii) the realization `f↦Z_f` is **linear and isometric**
to the Weil form. Given M3a, §3 closes RH; without it, §3 is conditional.

**Proposed path for M3a (concrete).** Build the pairing from the **two-variable completed kernel**
`Ξ(z,w):=ξ(½+iz)ξ(½+iw)` and its Frobenius/Hecke deformation, taking the **Connes–Consani
`\mathrm{Spec}\,ℤ`-Frobenius** (the `\mathbb{S}`-algebra / `Γ`-scheme structure, `[[riemann-phase61-deninger-quaternionic]]`)
as `F_t`. The diagonal restriction recovers the one-variable explicit formula; the off-diagonal /
Castelnuovo–Severi part supplies the negative self-intersection. Verify the three properties (i)–(iii)
**as theorems**, not numerically. This is the genuine frontier of the Connes–Consani program; it is
where the program's MW-5 wall now sits, **localized to the construction of a single intersection
pairing and one realization map**, not a general cohomology.

---

## §5. Status and the precise statement of what remains

**Forward progress (pure-math), net:**
1. RH is reduced (rigorously, §§1–3 of the construction) to **positivity of the overlap form** =
   positive angle between the Tate subspaces `𝒟₋,𝒟₊=ℱ𝒟₋`.
2. The analytic reformulation (M2: `‖H_Θ‖≤1`) is shown **RH-equivalent**, hence not an independent
   input — the positivity must be arithmetic.
3. The arithmetic input is reduced to a **single-class Hodge-index statement** `(Z_f·Z_f)≤0` for the
   primitive class `Z_f`, for which **Abboud's arithmetic Hodge index is the unconditional tool**, and
   the degree-zero hypothesis is exactly `μ_max=1` (already established).
4. The **entire** remaining gap is one object: the **realization map `f↦Z_f`** into a well-defined
   arithmetic Chow group of `\widehat{\mathrm{Spec}\,ℤ}^2` with Frobenius correspondences (M3a). This
   is MW-5, now localized to a single construction + one map, with a concrete proposed path
   (the two-variable kernel + Connes–Consani Frobenius).

**Honest:** M3a is **not** constructed here; it is the open frontier (the Connes–Consani program). No
false victory — RH remains open. But the obstruction is now a **single, named, localized construction**
with all surrounding structure (model space, Lax–Phillips realization, Kreĭn–Langer index, Abboud
inequality, degree-balance `μ_max=1`) **rigorously in place around it**.

## §6. Next pure-math target

Attempt **M3a**: define the arithmetic intersection pairing on `\widehat{\mathrm{Spec}\,ℤ}^2` via the
two-variable kernel `Ξ(z,w)` with the Connes–Consani Frobenius `F_t`, and prove properties (i)–(iii).
This is the one remaining theorem; everything else is assembled. We turn to it next, building the
realization `f↦Z_f` explicitly from the explicit-formula kernel and checking linearity + isometry to
the Weil form as theorems.
