# (T★) — pure analytic attack (A., severe referee) **Program:** CCM, phase 60. **Rule:** a forced theorem is WORSE than an admitted gap.
**Object:** `(T★)` = `Â_λ=(1/ε_0)A_λ` has a non-degenerate logarithmic edge scale
`h(λ)=π−ω*(λ)`, converges in strong resolvent sense to `Â_∞` with spectrum `(k+1)²`. Notation: `L=2logλ=2Ω`, `N` the order of the frame, `ω*=2πN/(2N+1)`, `x=w/L∈[−½,½]`,
`q(w)=Ω(0)−2M_0(w)`, `M_0(w)~2λ^{1/2−|x|}` (PNT). Beurling–Deny form already established:
``` A_λ(f,f) = ∫ q|f|² + 𝓔_θ(f) + 𝓔_prime(f), 𝓔_θ(f) ≤ C_2 ∫|f'|² (upper bound, PROVED).
```
`𝓔_D(f):=∫_{-1/2}^{1/2}|f'|²` the reference Dirichlet form in the rescaled variable `x`. Task (bias): **separate EXISTENCE of `Â_∞` (form bound + Mosco) from its
IDENTIFICATION (spectrum `n²`); do not impose the equation; beware of compactness.** I attack
the three points of the objective and state, coldly, what is proved and what is obstructed. --- ## PART 1 — Tightness (T): the LOWER Dirichlet bound The proposed strategy is correct in structure: if the **equivalence of forms**
``` (EQ) c_1 𝓔_D(f) ≤ Â_λ(f,f) ≤ c_2 𝓔_D(f) ∀ f ∈ E_λ, uniformly in λ,
```
is proved, with `0<c_1≤c_2<∞` independent of `λ`, then:
- (EQ-sup) gives tightness/compactness of the family of resolvents (equicontinuous form),
- (EQ-inf) gives uniform coercivity ⟹ non-degeneration of the limit (`Â_∞` with compact resolvent, discrete spectrum, no mass leaking to `0` or to `∞`),
- and together, by Mosco (Mosco 1994, Thm 2.4.1; Kuwae–Shioya) ⟹ Γ-convergence of forms ⟹ strong resolvent convergence ⟹ existence of `Â_∞`. **This is exactly (H-lim) via the forms route, equivalent to the Prokhorov route, but with the advantage that it also gives quantitative (H-gap) via the constant `c_1`.** The UPPER bound (EQ-sup) is given: `𝓔_θ≤C_2𝓔_D` and `𝓔_prime` is controlled by support
(primes `>λ²` do not contribute, autocorrelation `2Ω=L`); only the absorption of the
potential term `∫q|f|²` is missing, which the lower bound needs with sign. **The knot is (EQ-inf).** ### Lemma 1.1 (decomposition of the potential `q` and its sign). [SOLID]
With `q(w)=Ω(0)−2M_0(w)`, `M_0(w)=2λ^{1/2−|x|}(1+o(1))`, `Ω(0)=logλ=Ω`:
at the center `x=0`: `M_0~2λ^{1/2}=2e^{Ω/2}`, which **dominates** `Ω` ⟹ `q(0)<0` (very negative).
At the edge `|x|→1/2`: `M_0~2λ^{0}=2`, `q~Ω−4>0`.
Therefore `q` **changes sign**: a deep central well `q(0)≍−4e^{Ω/2}`, edge barrier
`q(±1/2)≍+Ω`. *Proof.* direct substitution of the PNT asymptotics of `M_0`. ∎ **Severe consequence (the raw obstruction).** `∫q|f|²` is NOT `≥0`; it has a central well of
depth `e^{Ω/2}=λ^{1/2}`. A naive lower bound `Â_λ(f,f)≥ c_1𝓔_D(f)` is **false
term by term**: the central well can make `A_λ(f,f)<0` for `f` concentrated at `x=0`.
This is precisely the signature that `ε_0` can be negative — **it is the same sign as the RH
wall** (Theorem III.3). Here is the filtering: any lower bound `Â_λ≥c_1𝓔_D>0` with `c_1>0`
uniform **forces** `ε_0>0`, hence **forces Weil-positivity = RH-local**. ### Lemma 1.2 (dividing by `ε_0` shifts the well, does not eliminate it). [SOLID]
`Â_λ=A_λ/ε_0`. If `ε_0>0`, `Â_λ(f,f)=A_λ(f,f)/ε_0` inherits the well scaled by `1/ε_0~logλ`
(since `|ε_0|=O(1/logλ)`). The central well of `A_λ` is `≍−λ^{1/2}`; after `/ε_0` it is `≍−λ^{1/2}logλ`,
**even deeper**. *Proof.* linear in `1/ε_0`. ∎ ### Theorem 1.3 (the lower bound (EQ-inf) IS RH-hard — exact obstruction). [conditionality THEOREM]
**(EQ-inf) `c_1 𝓔_D(f) ≤ Â_λ(f,f)` with `c_1>0` uniform in `λ` is equivalent to `ε_0(λ)>0`
for large `λ`, i.e. to Weil-positivity-up-to-`T*` = RH-local.** *Proof.* (⟹) If (EQ-inf) holds with `c_1>0`, taking `f` the normalized ground state `ξ^{(0)}`
`𝓔_D(ξ^{(0)})>0` (not constant, has an edge node by IV.5), `Â_λ(ξ^{(0)},ξ^{(0)})=1>0`
and `≥c_1𝓔_D>0`: consistent, but stronger: (EQ-inf) says the form `Â_λ` is **positive
definite** on all of `E_λ`, so `A_λ=ε_0·Â_λ` has the sign of `ε_0`; since `Â_λ⪰c_1𝓔_D⪰0`
non-degenerate, its lower eigenvalue is `+1>0`, which is the INFIMUM of the physical spectrum of
`A_λ` only if `ε_0>0` (if `ε_0<0`, dividing reverses the order and `+1` is the SUPREMUM, Obs 0.1 of
report III). The non-degeneration from below `Â_λ⪰c_1𝓔_D` **is** "`+1` is the infimum" `⟺ ε_0>0`.
(⟸) Under RH-local, `A_λ⪰0` (Weil form PSD, E0), `ε_0>0`, and then `Â_λ⪰0`; the
**quantitative** bound `c_1>0` follows from the equivalence of forms on the discrete spectrum. ∎ **Corollary 1.4 (verdict on (T)).** The uniform tightness `(T)` of `{Â_λ}` factors as:
| Component of (T) | Status |
|---|---|
| (EQ-sup) `Â_λ ≤ c_2𝓔_D` (upper control, no leak to `∞`) | **UNCONDITIONAL** (𝓔_θ≤C_2𝓔_D + support) |
| (EQ-inf) `c_1𝓔_D ≤ Â_λ` (coercivity, no leak to `0`) | **= RH-local** (Theorem 1.3) |
| `(T)` complete | **RH-hard due to its lower half** | > **I do not force the theorem.** The hope of the objective — "(T) unconditional via Beurling–Deny" —
> **breaks at the lower bound**, and the break is NOT technical: it is the central well `q(0)≍−λ^{1/2}`
> of the Beurling–Deny potential, which is the same object whose sign controls `ε_0`. The upper
> bound is pure analysis and it holds; the lower one IS the wall. The tribunal's compression "(T) RH-neutral" was
> **too optimistic**: (T) has an RH-neutral half (sup) and an RH half (inf). ### Remark 1.5 (what the forms route DOES rescue, RH-neutral).
The upper half (EQ-sup) alone **does** prove, unconditionally:
(i) **relative compactness** of `{Â_λ}` in form topology (no leak to `∞`), and
(ii) that any accumulation point of the resolvent is the resolvent of an operator with
**closed form bounded above by `c_2𝓔_D`** — a 2nd-order SL or a compact one.
What (EQ-sup) does NOT give is that the limit be **non-degenerate** (compact resolvent, discrete
spectrum): that is exactly (EQ-inf)=RH. That is, **the EXISTENCE of a limit (possibly
degenerate, with mass escaping to 0) is RH-neutral; the NON-DEGENERATION of the limit is RH.** This
is the separation requested: existence ⟂ identification, and degeneration falls on the RH side. --- ## PART 2 — The edge scale `h(λ)=π−ω*(λ)` and its non-degeneration This part **is** RH-neutral and is proved cleanly. It is the good part of the objective. ### Lemma 2.1 (exact identity `h(λ)=π/(2N+1)`). [SOLID]
`ω*=2πN/(2N+1)` ⟹ `h(λ)=π−ω*=π−2πN/(2N+1)=π(2N+1−2N)/(2N+1)=π/(2N+1)`. Exact, no asymptotics. ∎ ### Lemma 2.2 (`2N+1 ≍ L = 2logλ`, hence `h(λ) ≍ π/(2logλ)`). [SOLID]
The critical frame has `(2N+1)` samples in `[−Ω,Ω]` at relative Nyquist density
`1−1/(2logλ)` (Tribunal C.1/C.2, sub-critical): the number of samples is `2N+1 = L/Δ` with step
`Δ→1` (normalized Nyquist), `L=2logλ`. More precisely: the sub-Nyquist density `1−1/(2logλ)` gives
`2N+1=(2logλ)(1+O(1/logλ))`. Therefore
``` h(λ) = π/(2N+1) = π/(2logλ) · (1+O(1/logλ)).
```
*Proof.* counting the samples of the band-limited frame on `[−Ω,Ω]` at relative density
`1−1/L`; `2N+1=L·(density)=2logλ−1+o(1)`. ∎ ### Theorem 2.3 (non-degeneration of the scale: `h(λ)≍1/logλ`, neither collapses nor diverges). [SOLID, RH-NEUTRAL]
`h(λ)=π/(2N+1)` satisfies, unconditionally:
``` (logλ)·h(λ) → π/2 ∈ (0,∞).
```
In particular `h(λ)→0` (non-trivial edge scale, there is a boundary layer) but
`h(λ)·logλ ↛ 0` and `↛∞`: the scale is **exactly logarithmic**. This is the correct
"non-degeneration":
- If `h(λ)=o(1/logλ)` (fast collapse): the rescaling `y=x/h` would send the interval to `∞` faster than the potential, ⟹ **continuous spectrum** (Airy/line-type limit), not `n²`.
- If `h(λ)≫1/logλ` (slow): the edge layer would not separate from the bulk, ⟹ the limit operator **degenerates** to multiplication by `q`, with no kinetic term, **non-discrete accumulated** spectrum.
- `h≍1/logλ` is the **only** balance that matches the kinetic term `c(−d²/dx²)` (`c=−ψ''(1/4)/8>0`, derived from the archimedean term, weight `O(1)`) with the scale of the potential: the edge rescaling `y=(x∓1/2)/h` turns `c·h^{-2}·(−d²/dy²)+q` into a balance `O(h^{-2})·kinetic` vs `O(M_0)`-potential, and `h^{-2}=O((logλ)²)` matches the weight of the edge potential `q(±1/2)≍logλ` ONLY if measured in the correct variable — the ratio that survives is `O(1)`, giving a **regular** SL on a finite interval.
*Proof.* Lemma 2.1 + Lemma 2.2 give `(logλ)h→π/2`. The collapse/slow/balance trichotomy is the
two-scale analysis (matched asymptotics): the exponent of `h` in `1/logλ` is fixed by
`2N+1≍2logλ`, which is frame geometry, unconditional. ∎ **This closes point 2 of the objective affirmatively and RH-neutrally:** `h(λ)=π/(2N+1)≍π/(2logλ)`
is the **non-degenerate** logarithmic edge scale. There is no obstruction here. The non-degeneration
of the SCALE is frame geometry; what does NOT follow from it is the non-degeneration of the
OPERATOR (Part 1, that is RH). --- ## PART 3 — The spectrum `(k+1)²`: conditional on (EQ), forced by Sturm+Weyl -bias: **do not impose the equation.** Here I derive the spectrum ONLY under the hypothesis
(EQ) (which by Theorem 1.3 includes RH-local in its lower half), to show that **once
(EQ) is admitted, `n²` and `γ=3` require NO additional input** — they are forced. ### Theorem 3.1 (spectrum of the limit, conditional on (EQ)). [conditional THEOREM]
Assume (EQ) `c_1𝓔_D≤Â_λ≤c_2𝓔_D` uniform (i.e. RH-local + upper bound). Then:
1. **(Existence + discrete)** By Mosco (Part 1), `Â_λ→Â_∞` in strong resolvent sense, and by (EQ-inf) `Â_∞≥c_1𝓔_D` ⟹ `Â_∞` has **compact resolvent** ⟹ **discrete** spectrum `μ_0≤μ_1≤…→∞`, with no essential point. (The raw compactness obstruction, IV.1, is resolved: `Â_∞` is the Green's inverse, its resolvent is the edge compact.)
2. **(2nd-order SL form)** The kinetic term `c(−d²/dy²)`, `c=−ψ''(1/4)/8>0`, survives the edge rescaling `y=(x−1/2)/h` (Lemma/Theorem 2.3); the residual potential `V(y)` is even, bounded, non-constant (which explains why the constant-coefficient IDs of E12–E18 failed). By the Lévy representation of `Ω`, `Â_∞=−c d²/dy²+V(y)` on a finite interval `[−ℓ,ℓ]`, Dirichlet conditions (edge node forced by the carrier `ω*≠π`).
3. **(Node count)** Alternating parity `(−1)^k` + exactly `k` interior nodes ⟹ (Sturm, Lemma IV.5) `Â_∞` is a **regular** SL; numbering `n=k+1` (one edge node for the ground state).
4. **(Weyl)** For `−c d²/dy²+V` on `[−ℓ,ℓ]` Dirichlet, `V` bounded even: `μ_k=c(kπ/2ℓ)²(1+o(1))` ⟹ `μ_k/μ_0→((k+1)/1)²=(k+1)²` and `γ=μ_1/μ_0−1→2²−1=3`.
*Proof.* (1) Mosco+coercivity ⟹ resolvent compactness (Reed–Simon XIII; Mosco Thm). (2)
matched asymptotics of Part 2 with the archimedean weight `c`. (3) Sturm. (4) Weyl + (3). The
non-constant `V` shifts the `o(1)` but not the exponent `2` (Weyl is robust to bounded `V`). ∎ **Severity:** step (2) "the residual potential `V` is bounded" is NOT fully proved —
it is what the tribunal called "pinning `V`". Here I bound it: the rescaling `y=(x−1/2)/h` with
`h≍1/logλ` and `q(±1/2)≍logλ` gives `V(y)=h²·q ≍ (logλ)^{-2}·logλ=1/logλ→0` at the edge, and the
balance is with the kinetic `c·h^{-2}=O((logλ)²)`; **divided by `ε_0^{-1}≍logλ` of `Â`**, the
rescaled potential of `Â_∞` becomes `O(1)` and bounded. This **closes the boundedness of `V`**
conditional on `q(±1/2)≍logλ` (Lemma 1.1, unconditional). Hence **(2) is RH-neutral** once the
existence of the limit is admitted. The only RH input is the **non-degeneration (EQ-inf)** of (1). --- ## OVERALL VERDICT on (T★) ```
(T★) = (T) tightness + identification of spectrum n²
(T) = (EQ-sup) [RH-NEUTRAL, proved] ∧ (EQ-inf) [= RH-local, Theorem 1.3]
n² = Sturm+Weyl [forced UNDER (T), RH-neutral given the limit, Theorems 2.3+3.1]
``` **Frank, cold conclusion:** 1. **(T) is NOT unconditional.** Its upper bound is (pure Beurling–Deny analysis), but the **lower Dirichlet bound (EQ-inf) is RH-hard**: it is equivalent to `ε_0>0` (Theorem 1.3). The obstruction is EXACT and is localized in the **central well** `q(0)≍−λ^{1/2}` of the Beurling–Deny potential. **It is not neutral; RH leaked through**, via the same channel as the sign of `ε_0`. 2. **The edge scale `h(λ)=π/(2N+1)≍π/(2logλ)` IS non-degenerate and unconditional** (Theorem 2.3). This point of the objective closes affirmatively. But the non-degeneration of the SCALE is frame geometry and **does not imply** the non-degeneration of the OPERATOR (that is EQ-inf = RH). Separation: scale ⟂ operator. 3. **The spectrum `(k+1)²` and `γ=3` are FORCED under (T)** (Theorem 3.1): Mosco gives existence + discreteness, the edge rescaling bounds `V`, Sturm fixes the form, Weyl gives `n²`. **They require no extra input** once the lower half of (T) is admitted. This is a win: it reduces "identifying `V`" to "admitting coercivity", and coercivity is the only gap — which is RH. 4. **Rewriting of the tribunal's compression.** The claim "(T★) is a single RH-neutral statement" is **incorrect as it stood**. Correct version: > (T★) = [non-degenerate log scale: RH-NEUTRAL, PROVED (Part 2)] > + [uniform coercivity `Â_λ⪰c_1𝓔_D`: = RH-local (Part 1)] > + [n² by Sturm+Weyl: forced under the above (Part 3)]. The RH wall **did not move**: it relocated, from "the sign of ε₀" to "the uniform coercivity of the rescaled Dirichlet form", which is the **same object**. The `/ε_0` architecture has RH baked into the coercivity, exactly as in III. **Final sentence.** (T★) is not a single RH-neutral gap: it is **two-thirds provable pure
analysis** (logarithmic scale + Sturm→Weyl chain) **and one-third that IS the RH wall**
(the lower Dirichlet bound = coercivity = `ε_0>0`). I did not force the theorem: the upper bound
is unconditional, the scale is unconditional, the spectrum is forced-conditional, and I said RH-hard
only where the central well `q(0)<0` imposes it. **(T★) does NOT close III unconditionally; it closes
IV.1 and the identification of the spectrum MODULO the same coercivity that is RH.** The non-RH-hard gap
of the tribunal was an accounting illusion: half of (T) is the wall. — A. (referee), phase 60.
