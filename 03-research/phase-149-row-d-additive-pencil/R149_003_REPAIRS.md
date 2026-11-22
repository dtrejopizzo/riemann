# R149.003 — Repairs round: the mathematics behind the labels of record

wording orders (D.59 framing; `k=1` header on the D.60 dichotomy).
Inputs: `R149_000_BLUEPRINT.md`, `R149_001_ROUND1.md`, `R149_002_AUDIT.md`,
`R149_005_CLOSING_DECISION.md` (labels of record; where this file and `R149_005` differ,
`R149_005` governs — this file supplies the mathematics, not the labels).*

**FATAL rule.** Nothing below asserts a new zero-free region, a new moment bound, or a new
cancellation estimate. Every bound used is either proved here from Poisson summation / Hölder /
orthogonality, or is a named classical import (Siegel–Walfisz, Pólya–Vinogradov, the large sieve,
Landau's `Σ_{q≤Q}μ²(q)/φ(q)`), used only as an upper bound. **No sign is claimed. Row D: no label.**

**Summary of what changes.** Two claims of `R149_001` are withdrawn as *proofs* and kept only as
*plausibility*: the assertion that the averaged centering `(C′)` "follows from the large sieve"
(§1.4 below shows the large sieve is, in the disputed range `c ≥ 1/2`, weaker than the main term it
would have to certify), and the `2k`-th-power leg of D.60.7 (§2 replaces it by what
Siegel–Walfisz alone gives, which is strictly less). Two claims are strengthened: condition **(E)**
now holds unconditionally for **all** `c < 1` with error `O_A(N^{-A})`, independently of any
centering hypothesis (§1.2), so Theorem D.59.1 is unaffected by either withdrawal; and the missing
`M_Q` estimate of D.59.3 is computed (§5.2). One headline is restated (§4), one constant corrected
(§4.4), one statement split by level (§4.5), one citation corrected (§5.1).

---

## 0. Framing sentence of record for D.59

Replacing the opening reading of `R149_001` §2.2 ("verbatim the shape of Weil I, 3.2"):

> **D.59 is a Hölder inequality, not a transfer of Weil I 3.2.** The extraction step is
> `‖S̃‖_{ℓ^∞(F_Q)} ≤ ‖S̃‖_{ℓ^{2k}(F_Q)}`, i.e. the inclusion `ℓ^{2k} ↪ ℓ^∞` on a finite set of
> cardinality `#F_Q ≍ Q²`, with the cost `(#F_Q)^{1/2k}` paid by the `2k`-th root. It holds for an
> arbitrary complex sequence `(b_n)` supported in `[N,2N]` and an arbitrary model satisfying (E)
> (Prop. D.59.4: `Ξ_a`-uniformity), and therefore **carries no arithmetic whatsoever**. Calling
> `F_Q` "the family" and `α = 0` "the distinguished fibre" is an analogy, not a construction: there
> is no sheaf, no monodromy group, no weight filtration, and nothing plays the role of "the poles of
> the family's `L`-function do not move with `k`" except the *hypothesis* that the factor `Q²` in
> `H(k,c)` is independent of `k`. **All of the arithmetic sits inside `H(k,c)`**, and D.63.1 shows
> it: `H(k,c)` is false for `Λ_a(n) = Λ(n)(n^a + n^{-a})` as soon as `k > c/a`, while the extraction
> runs unchanged for that sequence.

Any paper-facing version of D.59 must open with that paragraph.

---

## 1. Repair (i) — (E) as a standalone lemma for all `c<1`; (C)/(C′) demoted

### 1.1 What Theorem D.59.1 actually uses

Inspection of the proof of Theorem D.59.1: the chain is
`|S̃(0;N)|^{2k} ≤ M_{2k}(N) ≤ C_k(log N)^{B_k}Q²N^k`, then `2k`-th roots, then
`S̃(0;N) = ψ_w(N) − Σ_n M_Q(n)w(n/N)`. The only property of `M_Q` invoked is the evaluation of
`Σ_n M_Q(n)w(n/N)`, i.e. **(E) at the single point `q_0 = 1`**. Condition (C) at `q_0 > 1` is never
used in the proof; it enters only in the *interpretation* of `H(k,c)` (it is what makes `M_Q` a
centering, i.e. what removes the major-arc main terms `μ(q)/φ(q)` that make `H(k,c)` false for
`M ≡ 1`, Prop. D.59.0a(2)). This separation is what the repair exploits.

### 1.2 Lemma D.59.0c (evaluability, standalone; `PROVED`, all `c<1`)

**Lemma D.59.0c.** Let `w ∈ C_c^∞(0,∞)` with `supp w ⊆ [1,2]`, let `0 < c < 1` be fixed and
`Q = N^c`, and let `M_Q(n) = Σ_{q≤Q}(μ(q)/φ(q))c_q(n)`. Then for every `A > 0`,
```
Σ_n M_Q(n) w(n/N)  =  N ŵ(0)  +  O_{A,w,c}( N^{-A} ).
```
In particular (E) holds, with error `O_A(N^{-A})`, far stronger than the `O(N^{1/2})` demanded by
Definition D.59.0, **for every `c < 1`, with no centering hypothesis and no averaging.**

*Proof.* Expand the Ramanujan sum, `c_q(n) = Σ*_{b mod q} e(nb/q)`, and exchange the (finite) sums:
```
Σ_n M_Q(n) w(n/N)  =  Σ_{q≤Q} (μ(q)/φ(q)) Σ*_{b mod q}  Σ_n e(nb/q) w(n/N).
```
For a real `β`, Poisson summation in the form `Σ_n e(nβ)w(n/N) = N Σ_{m∈Z} ŵ(N(m−β))` together with
`ŵ ∈ 𝒮(R)` (as `w ∈ C_c^∞`) gives, for every `A ≥ 1`,
```
Σ_n e(nβ) w(n/N)  =  N ŵ(0)·1[β ∈ Z]  +  O_A( N (1 + N‖β‖)^{-A} ),            (1.1)
```
where `‖β‖` is the distance to the nearest integer. Apply (1.1) with `β = b/q`, `(b,q)=1`, `q ≤ Q`.

*The trivial frequency.* `‖b/q‖ = 0` occurs only for `q = 1` (`b = 1 ≡ 0`), and contributes exactly
`(μ(1)/φ(1)) N ŵ(0) = N ŵ(0)`.

*Every other frequency.* If `q ≥ 2` and `(b,q) = 1` then `‖b/q‖ ≥ 1/q ≥ 1/Q = N^{-c}`, hence
`N‖β‖ ≥ N^{1-c}`. **Because only `q_0 = 1` is being tested, the two denominators never interact and
the spacing is `Q^{-1}`, not `Q^{-2}`.** With `c < 1` fixed, `N^{1-c} → ∞`, and (1.1) gives each
such term `O_A(N·N^{-A(1-c)})`. Summing over the at most `Σ_{q≤Q}φ(q) ≤ Q²` pairs `(q,b)` and using
`|μ(q)/φ(q)| ≤ 1`:
```
error  ≪_A  Q² · N^{1-A(1-c)}  =  N^{1 + 2c - A(1-c)},
```
which is `O(N^{-A'})` for any prescribed `A'` on choosing `A > (1 + 2c + A')/(1-c)`. ∎ `PROVED`

**Remark.** The lemma is the exact point at which `R149_001` Remark D.59.0b over-retreated: the
`Q^{-2}` spacing, and with it the threshold `c = 1/2`, is a feature of (C) at `q_0 > 1` only. At
`q_0 = 1` there is no threshold, and (E) is unconditional up to `c = 1` (indeed up to
`Q = N^{1-δ}`; for `Q ≥ N` the statement degenerates, since `M_Q` then ceases to be a bounded-level
model).

**Corollary.** Theorem D.59.1, Corollary D.59.1a, Theorem D.59.2 and Prop. D.59.4 are proved for all
`c ∈ (0,1)` with (E) alone, and are **independent of (C), (C′) and of everything in §1.3–1.4 below.**
Nothing downstream of D.59 breaks under the demotion that follows.

### 1.3 (C) at `q_0 > 1`: proved for `c < 1/2`, and only there

**Proposition D.59.0d (`PROVED`).** Let `0 < c < 1/2`. For every `q_0 ≤ Q` and `(a,q_0)=1`,
```
Σ_n M_Q(n) e(na/q_0) w(n/N)  =  (μ(q_0)/φ(q_0)) N ŵ(0)  +  O_{A}( N^{-A} ).
```
*Proof.* As in `R149_001` §2.1(3): the frequency is `β = b/q + a/q_0 mod 1`. If `β ∈ Z` then
`b/q ≡ −a/q_0`, and with `(b,q) = (a,q_0) = 1` this forces `q = q_0`, `b ≡ −a`, contributing
`(μ(q_0)/φ(q_0))Nŵ(0)`. Otherwise `β = (b q_0 + a q)/(q q_0) ∉ Z` with denominator `q q_0 ≤ Q²`, so
`‖β‖ ≥ 1/(q q_0) ≥ Q^{-2} = N^{-2c}` and `N‖β‖ ≥ N^{1-2c} → ∞` precisely because `c < 1/2`; (1.1)
and the count `≤ Q²` of pairs finish as in Lemma D.59.0c. ∎

**Proposition D.59.0e (the obstruction at `c ≥ 1/2` is real, not an artefact; `PROVED`).**
For `c > 1/2` the error term in (C) cannot be `O(N^{1-δ})` uniformly in `(q_0,a)` by this argument,
and not for a removable reason: the Farey points of order `Q` have mean spacing `≍ Q^{-2} = N^{-2c}`,
which is `≪ N^{-1}` once `c > 1/2`, so for a positive proportion of pairs `((q,b),(q_0,a))` one has
`N‖β‖ ≪ 1` and (1.1) returns `N ŵ(0)(1+o(1))`-sized terms with no decay at all. The individual
(C) is therefore **not available** for `c ≥ 1/2` by any Poisson argument, and no other proof is
offered here. `OPEN`.

### 1.4 Demotion of (C′): the large-sieve justification is withdrawn

`R149_001` Remark D.59.0b asserts that the averaged form
```
(C′)      Σ_{q_0≤Q} Σ*_{a mod q_0} | Σ_n M_Q(n)e(na/q_0)w(n/N) − (μ(q_0)/φ(q_0))Nŵ(0) |²  ≪  Q² N^{ε}
```
"follows from the large sieve applied to `M_Q`". **That is false, and the mechanism of the failure is
worth recording.** The large sieve inequality gives, for the coefficient sequence
`u_n := M_Q(n)w(n/N)` supported in `[N,2N]`,
```
Σ_{q≤Q} Σ*_{a mod q} | Σ_n u_n e(na/q) |²  ≤  (N + Q²) Σ_n |u_n|²  ≪  (N + Q²) N (log N)^{O(1)},
```
using (B) (`Σ_n |M_Q(n)|²w(n/N)² ≪ N log N`, proved in `R149_001` §2.1(3)). But the **main terms
alone**, whose smallness is not in question, already weigh
```
Σ_{q≤Q} Σ*_a |(μ(q)/φ(q))Nŵ(0)|²  =  N²ŵ(0)² Σ_{q≤Q} μ²(q)/φ(q)  =  N²ŵ(0)²(log Q + C_0 + o(1)).
```
So the large-sieve upper bound `(N+Q²)N^{1+o(1)}` exceeds the quantity it is supposed to be
controlling the *error* of exactly when `Q² ≥ N`, i.e. `1 + 2c ≥ 2`, i.e.
```
                                  c ≥ 1/2,
```
which is precisely the range where (C) is unavailable (Prop. D.59.0e). **The large sieve is
insufficient in, and only in, the range where it was invoked.** Withdrawn.

**Status of record.** `(C′)` is hereby **demoted to a plausibility clause attached to `H(k,c)`**:

> **Plausibility clause (P-C′), label `OPEN`.** For `c ≥ 1/2`, the model `M_Q` is expected, but not
> proved, to centre the Farey family on average in the sense of `(C′)`. The expectation rests on the
> equidistribution of Farey spacings (the pairs with `N‖β‖ ≪ 1` are heuristically a proportion
> `≍ N^{-1}Q² / Q²`-thin relative to their trivial size) and on `M_Q` being Vaughan's truncated
> singular-series approximant, for which the centring is known in mean-square *for the prime side*
> in the Barban–Davenport–Halberstam range. **No proof is claimed and none is used.** If `(C′)` were
> false, the consequence would be that `H(k,c)` at `c ≥ 1/2` is a hypothesis about an imperfectly
> centred family, i.e. possibly *false for a trivial reason*; that would weaken `H(k,c)`'s
> plausibility, not the validity of Theorem D.59.1, which does not use it.

**Honest label line for the record:** (E) `PROVED` for all `c<1` (Lemma D.59.0c); (C) `PROVED` for
`c<1/2` (Prop. D.59.0d), `OPEN` for `c ≥ 1/2` (Prop. D.59.0e); (C′) `OPEN` (plausibility clause
(P-C′)); the earlier `PROVED` on (C′) is **withdrawn**.

---

## 2. Repair (ii) — D.60.7 rescoped; the `2k`-th-power leg redone with Siegel–Walfisz only

### 2.1 What the old leg (ii) did wrong

`R149_001` Theorem D.60.7(ii) bounded the contribution of the low moduli `q ≤ Q_0 := C_M log log N`
to `M_{2k}` by inserting `|ψ(x,χ)|² ≪ x(log log log x)²`. That inequality is **the size of the
oscillation Fiorilli–Martin construct**, i.e. an `Ω`-statement realised along a sparse sequence
`(q_j,x_j)`; it is not an unconditional upper bound valid for all `χ` of conductor `q ≤ Q_0` and all
`x`. Using it as an upper bound is a category error, and it is the only place in `R149_001` where
one occurs.

### 2.2 What Siegel–Walfisz alone gives

**Import (classical, `IMPORTED`).** *Siegel–Walfisz.* For every `A > 0` there is `c_1 = c_1(A) > 0`
such that for all primitive `χ mod q` with `q ≤ (log x)^A`,
`ψ(x,χ) ≪_A x exp(−c_1 √(log x))` (the constant being ineffective). Since
`Q_0 = C_M log log N = (log N)^{o(1)}`, all moduli `q ≤ Q_0` lie in this range.

**Proposition D.60.7b (low-modulus contribution, honest version; `PROVED`).**
Let `Q_0 = Q_0(N) = (log N)^{o(1)}` and `S̃ = S̃_{M_Q}`. Then
```
Σ_{q ≤ Q_0} Σ*_{a mod q} |S̃(a/q;N)|^{2k}  ≪_{A,k}  Q_0² · N^{2k} exp(−2k c_1 √(log N)).      (2.1)
```
*Proof.* For `q ≤ Q_0` write, by finite Fourier inversion over `(Z/q)^×`,
`S(a/q;N) = φ(q)^{-1} Σ_χ χ̄(a) τ(χ,a)`-type decomposition; concretely
`S(a/q;N) = φ(q)^{-1} Σ_{χ mod q} χ̄(a) Σ_{χ_1} … ` — it suffices to use the standard bound
`|S(a/q;N) − (μ(q)/φ(q))Nŵ(0)| ≪ max_{χ mod q} |ψ_w(N,χ)| ≪_A N exp(−c_1√(log N))`, which is
Siegel–Walfisz after partial summation against `w`, valid uniformly for `q ≤ Q_0`. By
Prop. D.59.0d (legitimate here: `q ≤ Q_0`, so the relevant spacing is `≥ 1/(qQ) ≥ N^{-c-o(1)}` and
`N‖β‖ ≥ N^{1-c-o(1)} → ∞` for every `c<1`) the model contributes the same main term up to
`O_A(N^{-A})`, so `|S̃(a/q;N)| ≪_A N exp(−c_1√(log N))` for every `q ≤ Q_0`. Raise to the `2k`-th
power and count the `≤ Q_0²` pairs. ∎

**Corollary D.60.7c (exactly what is, and is not, established; `PROVED`).**
The bound (2.1) is `o(Q²N^k) = o(N^{k+2c})` **iff**
```
N^{k - 2c} = o( exp(2k c_1 √(log N)) )   ⟺   k < 2c.
```
Hence, **using only Siegel–Walfisz and trivial bounds**, the low-modulus segment is provably
negligible for `H(k,c)` in precisely the range
```
                          k = 1  and  c > 1/2,
```
and for **no** `k ≥ 2` and no `c ∈ (0,1)` (since `k ≥ 2 > 2c`). ∎

**Reading (and it is the same reading as D.60.3).** The one range in which the counterexample
segment can be *proved* harmless is the range in which the extraction is vacuous
(`N^{1/2+c} ≥ N` for `c ≥ 1/2`). This is a third independent instance of the phase's dichotomy, and
it is not a coincidence: both are the statement that unconditional information about primes in
progressions is available only above the large-sieve/BDH threshold `Q ≥ N^{1/2}`.

### 2.3 Theorem D.60.7, rescoped statement of record

> **Theorem D.60.7′ (W-H survival, rescoped; `PROVED`).** Let `c ∈ (0,1)`, `Q = N^c`. Then:
> 1. **(Range.)** The Fiorilli–Martin (JEMS 25 (2023)) and Hayani (arXiv:2407.01045) counterexamples
>    to Hooley's conjecture occur at moduli `q ≍ log log x`, and in the `q`-averaged form only for
>    levels `Q ≤ √(log log x)`. Both lie in an initial segment `[1, N^{o(1)}]` of `[1, N^c]`.
> 2. **(Mechanism.)** The mechanism is Littlewood's `ψ(x,χ) = Ω_±(x^{1/2} log log log x)`, a
>    fluctuation of size `x^{1/2+o(1)}`, hence **compatible with GRH** and with the per-fibre content
>    of `H(k,c)` (`|S̃(a/q;N)| ≈ N^{1/2}` on average). What the counterexamples refute is Hooley's
>    *normalisation* `x log q`, which at `q ≍ log log x` is smaller than the true size; `H(k,c)`'s
>    normalisation is `Q²N^k` for the whole family, i.e. `≈ N^k` per Farey point, which the
>    Littlewood fluctuation exceeds only by `(log log log N)^{2k}` — inside the `(log N)^{B_k}`
>    budget.
> 3. **(Consequence.)** Therefore **the known counterexamples do not refute `H(k,c)` for any `k`**:
>    no Farey point is exhibited at which `|S̃(a/q;N)|` exceeds `N^{1/2+o(1)}`, and no aggregate
>    lower bound of order `Q²N^k(log N)^{ω(1)}` or `N^{k+δ}` follows from them.
> 4. **(Scope limit, new.)** What is **not** established is an unconditional *upper* bound showing
>    the low-modulus segment's contribution to `M_{2k}` is negligible. By Prop. D.60.7b–c, Siegel–
>    Walfisz alone yields that only for `k = 1, c > 1/2`. For `k ≥ 2` the contribution of
>    `q ≤ (log N)^{o(1)}` to `M_{2k}` is **not known to be `o(Q²N^k)`** — though it is expected to
>    be, on GRH. The `2k`-th-power computation of `R149_001` §3.6 is withdrawn.
>
> The distinction between (3) and (4) is the whole content of the rescope: *not refuted* is proved;
> *provably negligible* is not.

---

## 3. Repair (iii) — the unconditional Ω-results for even moments, checked against `H(k,c)`

**Epistemic label.** The two papers below have **not been read in this phase**; their statements are
reported as understood from citation and from Fiorilli's and Harper–Soundararajan's surrounding
literature, and are labelled **`CERTIFIED`** (to be verified against the papers before quotation).
The *comparison* computations in §3.3 are `PROVED` given those shapes.

### 3.1 de la Bretèche–Fiorilli (arXiv:2010.05944) — shape as far as known

*R. de la Bretèche and D. Fiorilli, "Moments of moments of primes in arithmetic progressions"
(arXiv:2010.05944; Proc. LMS).* **`CERTIFIED`.** As understood: for the weighted variance-type
quantity built from `ψ(x;q,a) − x/φ(q)` (or its smoothed/weighted analogues), they establish
**unconditional Ω-results for all even moments**, of the shape
```
  the (2k)-th moment of the normalised error  (ψ(x;q,a) − x/φ(q)) / (x/φ(q))^{1/2}
  is, for a positive-density set of x (or along a sequence x → ∞),  ≫_k  μ_{2k} = (2k−1)!! ,
```
i.e. Ω-results **of Gaussian order**, together with GRH-conditional lower bounds for the "moments of
moments" (moments over `q` of the moments over `a`). The essential point for us: the asserted lower
bounds are of the size predicted by a Gaussian model with variance `x/φ(q)` per residue class — they
assert that the true moments are *not smaller* than Gaussian, never that they are *larger* by a
power of `x` or by an unbounded power of `log x`.

### 3.2 Harper–Soundararajan — shape as far as known

*A. J. Harper and K. Soundararajan, "Lower bounds for the variance of sequences in arithmetic
progressions: primes and divisor functions", Q. J. Math. 68 (2017).* **`CERTIFIED`.** As understood:
unconditionally, for `x^{1/2+ε} ≤ Q ≤ x` (and with a `log` factor reflecting the level),
```
  Σ_{q ≤ Q} Σ*_{a mod q} ( ψ(x;q,a) − x/φ(q) )²   ≫   x Q log(x/Q)          (3.1)
```
— a **lower** bound of the conjectured (Montgomery–Hooley/BDH) order, obtained by a
Diophantine/multiplicative-function argument rather than from zeros. Again: the order asserted is the
*expected* one, not larger.

### 3.3 The comparison with `H(k,c)` — run

`H(k,c)` asserts `M_{2k}(N) ≤ C_k (log N)^{B_k} Q² N^k` with `Q = N^c`.

**(a) The Gaussian prediction saturates `H(k,c)` and does not violate it.** If the centred family
`{S̃(a/q;N)}_{a/q ∈ F_Q}` behaves like `#F_Q ≍ (3/π²)Q²` independent complex Gaussians of variance
`≍ N` (square-root cancellation per fibre), then
```
M_{2k}(N)  ≈  #F_Q · E|Z|^{2k}  ≍  Q² · k! · N^k      (complex Gaussian),
```
which is `≤ C_k (log N)^{B_k} Q² N^k` with `C_k = k!`, `B_k = 0`. **The Gaussian order is exactly the
order `H(k,c)` permits.** Consequently any Ω-result "the even moments are at least of Gaussian
order" is *consistent with `H(k,c)` with no slack consumed at all* beyond the constant `C_k`, which
`H(k,c)` allows to depend on `k`. §3.1's results are therefore **not in conflict with `H(k,c)`**.

**(b) The variance lower bound (3.1), explicitly.** The `k = 1` instance of `H(k,c)` permits
`M_2(N) ≤ C_1(log N)^{B_1} Q² N`. The Harper–Soundararajan lower bound, transported to the additive
square by the Parseval identity of §4.1 (the transport is exact, for each `q`), reads
`M_2(N) ≫ N Q log(N/Q) = N^{1+c}·(1−c)log N`. Comparing,
```
   lower bound / permitted upper bound  ≍  N^{1+c} log N / (N^{1+2c}(log N)^{B_1})  =  (log N)^{1-B_1} N^{-c},
```
which `→ 0` for every fixed `c > 0`. **The margin is a full power `N^{c}`**: the unconditional
variance lower bound is smaller than the `H(1,c)` ceiling by the factor `Q`, and cannot contradict
it. (This is unsurprising — `H(1,c)` at `c ≥ 1/2` *is* the Montgomery–Vaughan large sieve,
Thm D.60.1, which is a theorem; a contradiction here would have refuted the large sieve.)

**(c) The single-modulus Ω of Fiorilli–Martin, for completeness.** `V_Λ(x;q) ≫ M x log q` at
`q ≍ log log x` contributes `≪ M N (log log log N)^{2}·(log log N)^{O(1)} = N^{1+o(1)}` to `M_2`,
against the budget `N^{1+2c}`: negligible, as in Thm D.60.7′(1).

**(d) What an Ω-result would have to look like to refute `H(k,c)`.** Exactly one of:
```
 (α)  M_{2k}(N)  =  Ω( Q² N^{k} (log N)^{ω(1)} )     (unbounded log power, defeating (log N)^{B_k}),
 (β)  M_{2k}(N)  =  Ω( Q² N^{k+δ} )                  (power excess),
 (γ)  M_{2k}(N)  =  Ω( Q^{2+δ} N^{k} )               (family-size excess, i.e. the exponent 2 moves).
```
**None of (α), (β), (γ) is claimed by either paper as understood**: both are of Gaussian order, i.e.
they match rather than exceed the `Q²N^k` shape. Shape (γ) is the interesting one — it is exactly the
failure of "the exponent `2` in `Q²` is independent of `k`", which §0 identifies as the one structural
hypothesis inside `H(k,c)` — and nothing in the literature bears on it.

**Verdict (the check the audit ordered, now run): NO CONTRADICTION.** The unconditional Ω-results
for even moments do not refute `H(k,c)` for any `k` or `c`; they are of Gaussian order, which is the
order `H(k,c)` permits. **The FATAL rule is not triggered from below either.** Label:
`PROVED` for the comparison computations (a)–(d), `CERTIFIED` for the imported statements §3.1–3.2.

---

## 4. Repair (iv) — D.61.10 restated; D.61.7 constant; D.61.4 split by level

### 4.1 The transport that does exist, written out: Parseval over `χ`

**Lemma D.61.10a (exact transport at every `q`; `PROVED`, `CLASSICAL`).** For `q ≥ 2` put
```
V_Λ(x;q) := Σ*_{a mod q} ( ψ(x;q,a) − ψ(x;(·,q)=1)/φ(q) )²,    ψ(x;q,a) := Σ_{n≤x, n≡a(q)} Λ(n),
ψ(x,χ)  := Σ_{n≤x} Λ(n) χ(n).
```
Then
```
                 V_Λ(x;q)  =  φ(q)^{-1} Σ_{χ ≠ χ_0}  |ψ(x,χ)|² .                      (4.1)
```
*Proof.* Plancherel on the finite abelian group `(Z/q)^×`. Set
`f(a) := ψ(x;q,a) − φ(q)^{-1}Σ_{(n,q)=1, n≤x}Λ(n)` for `(a,q)=1`. Its Fourier coefficients at
`χ` are `\hat f(χ) := Σ*_a f(a)\barχ(a) = ψ(x,\barχ)` for `χ ≠ χ_0`, and `\hat f(χ_0) = 0` by
construction. Parseval on `(Z/q)^×`, `Σ*_a |f(a)|² = φ(q)^{-1}Σ_χ |\hat f(χ)|²`, gives (4.1). ∎

**Consequence (and it is why the old headline was false as written).** The left side of (4.1) is a
second moment on the **additive square** (it is, up to the model, the `q`-block of `M_2`: by
`R149_001` Thm D.61.7, `Σ_{q≤Q}Σ*_a |S(a/q;N)|²` is the Farey/additive family moment, and (4.1)
identifies its `q`-th block with a multiplicative-square moment). The right side is a sum of
**Rankin squares** `|ψ(x,χ)|²` on the **multiplicative square**. So:

> **At the level of second moments of counting functions at a fixed `x`, the two squares are
> identified, exactly, for every `q`. A transport exists, it is classical, and `R149_001` itself
> uses it in §3.6.** The sentence "nothing known transports between them" is withdrawn.

### 4.2 The second transport that exists: the Goldston–Montgomery bridge

**Import (`IMPORTED`, `CLASSICAL`).** *Goldston–Montgomery (1987).* Under RH, the two assertions
```
 (GM-1)  ∫_1^X ( ψ(x+δx) − ψ(x) − δx )² dx  ~  (1/2) δ X² ( log(1/δ) − ... )   for X^{ε−1} ≤ δ ≤ X^{−ε},
 (GM-2)  F(X,T) := Σ_{0<γ,γ'≤T} X^{i(γ−γ')} w(γ−γ')  ~  (T/2π) log T          (Montgomery's pair
                                                                               correlation, in the
                                                                               corresponding range),
```
are **equivalent**. Related transports of the same type: Hardy–Littlewood `k`-tuples ⟹ Montgomery's
`F(α)` (Bogomolny–Keating at `n`-level); Montgomery–Soundararajan (*Primes in short intervals*,
CMP 252 (2004)); Goldston–Suriajaya (Nagoya Math. J. 2023), tying Fujii's error term in the average
Goldbach formula to the short-interval variance.

So the additive-side second moment (short-interval / Farey variance) and the multiplicative-side
zero statistics are **connected, RH-conditionally, and the connection is sign-free** (NG-B8: pair
correlation is wrong-signed / invisible to off-line zeros).

### 4.3 Theorem D.61.10′ — statement of record

> **Theorem D.61.10′ (no transport of the polar/positivity structure; `PROVED` for (1)–(3),
> `RESTATEMENT` for the framing).**
>
> *Transports that exist.* (T1) For every `q`, the additive-square second moment at level `q` equals
> a multiplicative-square second moment, exactly: `V_Λ(x;q) = φ(q)^{-1}Σ_{χ≠χ_0}|ψ(x,χ)|²`
> (Lemma D.61.10a). (T2) Under RH, the additive-square short-interval variance and the
> multiplicative-square pair correlation are equivalent (Goldston–Montgomery). **Both are transports
> of *second moments of counting functions at a fixed `x`*; both are RH-conditional or
> unconditional-but-`k=1`; both are sign-free.**
>
> *What they fail to carry.*
> 1. **Positivity / index.** Neither (T1) nor (T2) transports an index or a signature. On the
>    additive square the pairing `κ(d)` and the singular series `𝔖(d)` are **positive-definite**
>    (Thm D.61.5, Bochner — free, hence not progress), so the additive square carries **no index**:
>    a positive-definite form has no negative eigenvalue to count, and "positivity on the square
>    constrains nothing" (fourth corpus instance). On the multiplicative square, `|ψ(x,χ)|² ≥ 0` is
>    twist-stable (Thm D.61.9 contrast) and is exactly the positivity Landau consumes. **The
>    identity (4.1) equates two *numbers*; it does not equate the *structures* that make one of them
>    Landau-usable.**
> 2. **`k ≥ 2`.** (T1) is Parseval, i.e. the `k = 1` invariant theory and nothing more
>    (Prop. D.62.1: for `k=1`, `𝒞_2(0) = Σ|b_n|² ≪ N log N` is trivial). For `k ≥ 2` the additive
>    `2k`-fold energy `𝒞_{2k}(0)` and the `2k`-th moments of `ψ(x,χ)` are related **only by Hölder,
>    in the loss-making direction**: `Σ_χ |ψ_χ|^{2k} ≤ (Σ_χ|ψ_χ|²)^{k}` costs exactly the
>    cancellation one is trying to prove. There is no `k ≥ 2` analogue of (4.1).
> 3. **Polar / Landau structure.** (T1) is an identity of counting functions at fixed `x`, **not** an
>    identity of Dirichlet series in `s`. The family object `Σ_χ |ψ(x,χ)|²` has no Euler product and
>    no functional equation as a function of `s`, hence **no a priori polar divisor**; the additive
>    side does have an a priori polar divisor, but it is dominated by the trivial pole at `s = 2`
>    (Thm D.61.8: exponents **add**, `Re(ρ+ρ') ≤ 2`, so Landau detects only `s = 2` and returns
>    nothing about `β`), whereas the multiplicative pairing `ρ ↔ 1−\barρ` makes exponents
>    **subtract** and puts the top pole at the *critical* value — which is precisely why Paper 47
>    Thm 17.14 works there.
>
> **Statement of the wall.** *The moment-level transport between the two squares is classical
> (Parseval over `χ`; Goldston–Montgomery), RH-conditional or `k=1`, and sign-free. What does not
> transport is the polar/positivity structure: no known construction produces an object that is
> simultaneously (a) a square, hence Landau-positive after every twist, and (b) equipped with an
> a priori polar divisor determined by local data. Over `F_q`, `L(U, F ⊗ F^∨, T)` is both. Over `Z`,
> the singular series `𝔖(d)` and the pairing `κ(d)` exist only as **densities**, never as
> **residues**.* **The missing object is the promotion of the singular series from a density to a
> polar divisor** — additive form of phase-36 Doc 106's Lema Faltante 5.3 — and by Prop. D.62.1 it is
> equivalent to the Hardy–Littlewood `k`-tuple conjecture with square-root error on average. ∎

**Finding of record for D.61 (unchanged, and reaffirmed):** D.61.8–D.61.9, *exponents add on the
additive square and subtract on the multiplicative square*. D.61.10′ is the wall; D.61.10 as
originally worded is withdrawn.

### 4.4 D.61.7: the constant repaired

The display in `R149_001` §4.4,
```
            main term of V(x;Q)  =  x · Q · κ(0) · (1 + o(1)),                    [WITHDRAWN as an
                                                                                   identification]
```
is correct **only at leading order** `log Q` and **false at the constant level**. Precisely, with
```
V(x;Q) := Σ_{q ≤ Q} Σ*_{a mod q} ( ψ(x;q,a) − x/φ(q) )² ,
```
the Montgomery–Hooley theorem gives, for `x(log x)^{-A} ≤ Q ≤ x`,
```
V(x;Q)  =  x Q log Q  −  c_0 x Q  +  O_A( x Q (log x)^{-A} + x² (log x)^{-A} ) ,
c_0 = γ + log 2π + 1 + Σ_p (log p)/(p(p−1))                                      (Hooley's constant),
```
while the additive pairing's diagonal value at level `Q` is (Landau)
```
κ_Q(0)  =  Σ_{q ≤ Q} μ²(q)/φ(q)  =  log Q + C_0 + o(1),
C_0 = γ + Σ_p (log p)/(p(p−1))                                                   (no archimedean term).
```
Hence
```
c_0 − C_0 = log 2π + 1,                and                V(x;Q) = x Q ( κ_Q(0) − log 2π − 1 ) + o(xQ).
```
**Statement of record (D.61.7′):** *the Montgomery–Hooley main term equals `xQ·κ_Q(0)` at leading
order `xQ log Q`, and differs from it at the constant level by exactly `(log 2π + 1)xQ`. The
discrepancy is archimedean: `log 2π + 1` is the contribution of the infinite place (the `Γ`-factor
and the pole of `ζ`), and the additive pairing `κ_Q` — being a sum of finite local densities `1/φ(q)`
— cannot and does not see it.* The `(1+o(1))` of `R149_001` concealed a discrepancy of order `xQ`,
i.e. of the order of the entire content of Hooley I beyond the leading term. `PROVED` (the
subtraction), `CERTIFIED` (the value of `c_0`, §6).

**Reading, and it survives the repair intact.** The point of D.61.7 was that the BDH/Montgomery–
Hooley main term is computed *a priori* from Ramanujan orthogonality and Dirichlet densities, with
no knowledge of any zero — the "`H²_c`/coinvariant block" of the scheme. That stands. The corrected
constant sharpens it: the coinvariant block reproduces the finite part of the main term exactly and
misses precisely the archimedean constant, which is the first sign that the additive pairing is a
purely non-archimedean object.

### 4.5 D.61.4 split by level

`R149_001` Thm D.61.4 states `κ(d) = d/φ(d)` (a `Q = ∞` statement) and
`κ(0) = log Q + C_0 + o(1)` (a finite-level statement) in one breath. Split:

> **Theorem D.61.4′ (`PROVED`).** For `Q ≤ ∞` put `κ_Q(d) := Σ_{q ≤ Q} μ²(q)/φ(q) · 1[q | d]`.
> 1. **(Finite level, `d ≠ 0`.)** If `0 < |d| ≤ Q` then every squarefree `q | d` satisfies `q ≤ Q`,
>    so `κ_Q(d) = Σ_{q | d} μ²(q)/φ(q) = d/φ(d)`, the closed form being the standard multiplicative
>    identity (both sides multiplicative; at `p^a` both equal `p/(p−1)`).
> 2. **(Finite level, `|d| > Q`.)** `κ_Q(d) = Σ_{q | d, q ≤ Q} μ²(q)/φ(q) < d/φ(d)`, a **proper**
>    partial sum; the closed form fails, and `κ_Q(d) ≤ κ_∞(d) = d/φ(d) ≪ log log |d|`.
> 3. **(Finite level, `d = 0`.)** Every `q ≤ Q` divides `0`, so
>    `κ_Q(0) = Σ_{q≤Q} μ²(q)/φ(q) = log Q + C_0 + o(1)`, `C_0 = γ + Σ_p (log p)/(p(p−1))`.
> 4. **(Infinite level.)** `κ_∞(d) = d/φ(d)` for `d ≠ 0`, and `κ_∞(0) = +∞`. **The function `κ_∞`
>    is therefore not defined at `0`, and no statement may quantify over `d ∈ Z` at `Q = ∞`.**
>
> In particular the positive-definiteness of Thm D.61.5 is a statement about `κ_Q` for finite `Q`
> (a finite nonnegative combination of characters of `Z`), and its `Q → ∞` limit exists only in the
> distributional sense, the mass `κ_Q(0) → ∞` escaping to the diagonal. `PROVED`.

Also of record: the squarefree normalisation (with `μ²`) is the correct one — it is the one produced
by the model `M_Q`, whose `μ(q)` factor supports it on squarefree `q` — confirming Remark D.61.4a.

---

## 5. Repair (v) — D.62.2 citations; and the `M_Q` estimate missing in D.59.3

### 5.1 Corollary D.62.2′ (`PROVED`, with the citations in their correct roles)

> **Corollary D.62.2′.** `H(2,c)` implies, by Parseval in `d` (Prop. D.62.1),
> ```
> 𝒞_4(0) = Σ_{|d| ≤ 2N} | 𝒞_2(d) |²  ≪  (log N)^{B_2} N²,
> 𝒞_2(d) = Σ_n (Λ(n) − M_Q(n))(Λ(n+d) − M_Q(n+d)) w(n/N)w((n+d)/N),
> ```
> whence by Cauchy–Schwarz `Σ_{|d| ≤ 2N} |𝒞_2(d)| ≪ N^{3/2+o(1)}`, i.e. the Goldbach/twin
> correlation with square-root cancellation on average. Since `M_Q` is **zero-blind** (Thm D.61.6),
> the zero term `H(x) = −2 Σ_ρ x^{1+ρ}/(ρ(1+ρ))` of the average Goldbach formula is not absorbed by
> the centring, so a zero with `β > 1/2` would contribute `≫ x^{1+β}` and violate the bound. Hence
> **`H(2,c) ⟹ RH`.**
>
> **Citations, in their correct roles.**
> * **Sharp half (equivalence at exponent `3/2`): A. Granville, "Refinements of Goldbach's
>   conjecture, and the generalized Riemann hypothesis", Funct. Approx. Comment. Math. **37**
>   (2007), 159–173, Theorem 1A, together with the Corrigendum, Funct. Approx. **38** (2008),
>   125–127.** This is the statement
>   `Σ_{n ≤ x} R(n) = x²/2 + O(x^{3/2+ε})  ⟺  RH`, the original 2007 proof having been incomplete
>   and the corrigendum supplying the missing implication. The converse direction (RH ⟹ the
>   asymptotic with error `x^{3/2}(log x)^{O(1)}`) is Fujii, and Languasco–Zaccagnini. `IMPORTED`.
> * **Unconditional quasi-RH half: G. Bhowmik and I. Z. Ruzsa, "Average Goldbach and the
>   quasi-Riemann hypothesis", Analysis Mathematica **44** (2018) (arXiv:1711.06442), Theorem 2.1.**
>   This gives **only quasi-RH**: from `Σ_{n≤x}R(n) = x²/2 + O(x^{2−δ})` with `δ > 0` it deduces
>   `β < 1 − δ/6` for every nontrivial zero. At the exponent relevant here, `δ = 1/2`, it yields
>   `β < 11/12` — **not** `β ≤ 1/2`. Its virtue is that the proof is elementary (the square of
>   `F(z) = Σ Λ(n)z^n` plus a Dirichlet-kernel argument, no circle method). `IMPORTED`.
> * **Calibration from below:** Bhowmik–Schlage-Puchta's unconditional `Ω(x log log x)` shows the
>   *unaveraged* error cannot be pushed below `x log log x`. `IMPORTED`.
>
> **Correction of record.** `R149_001` §5.2 attributed the sharp half to Bhowmik–Ruzsa
> ("supplies the missing half"). That is wrong: Bhowmik–Ruzsa is the quasi-RH statement; the
> equivalence at exponent `3/2` is Granville 2007 Thm 1A + Corrigendum 2008.
>
> **Difficulty verdict, unchanged and if anything understated:** `H(2,c)` sits **at or above RH** —
> above, because it additionally demands the off-diagonal `Σ_{d≠0}κ_Q(d)𝒞_4(d)` control and full
> uniformity in `q ≤ Q`, neither of which is implied by RH. `PROVED`. **No FATAL flag: this is a
> lower bound on the difficulty of `H(2,c)`, not a new theorem about zeros.**

### 5.2 The `M_Q` estimate missing in D.59.3 (`PROVED`)

D.59.3's strictness argument applies finite Fourier inversion to the **uncentred** `S`, and left the
model's own contribution unestimated. It is the following, and it is genuinely small.

**Lemma D.59.3a (`PROVED`).** Let `χ` be a primitive character mod `q`, `q ≤ Q = N^c`, and let
`w ∈ C_c^∞`, `supp w ⊆ [1,2]`. Put `Ψ_χ(Y) := Σ_m χ(m) w(m/Y)`. Then
```
 Σ_n M_Q(n) χ(n) w(n/N)  ≪  q^{1/2} · Q · (log N)^{O(1)}  =  q^{1/2} N^{c + o(1)}.
```
Consequently the model contributes `≪ q^{1/2+ε}N^{1/2+ε}` — i.e. is absorbed into the ATRH
conclusion of D.59.3 — **whenever `c ≤ 1/2`**; and for `c > 1/2` D.59.3's implication must be stated
with the weaker conclusion `ψ_w(N,χ) ≪ q^{1/2+ε} N^{c+ε}`.

*Proof.* Use `c_r(n) = Σ_{d | (r,n)} d·μ(r/d)` (Hölder's identity for the Ramanujan sum). Then
```
Σ_n c_r(n) χ(n) w(n/N)  =  Σ_{d | r} d μ(r/d) Σ_{d | n} χ(n) w(n/N)
                        =  Σ_{d | r} d μ(r/d) χ(d) Ψ_χ(N/d),
```
writing `n = dm` and `χ(dm) = χ(d)χ(m)` (terms with `(d,q) > 1` vanish). Hence
```
Σ_n M_Q(n) χ(n) w(n/N)  =  Σ_{r ≤ Q} (μ(r)/φ(r)) Σ_{d | r} d μ(r/d) χ(d) Ψ_χ(N/d).     (5.1)
```
*Bound for `Ψ_χ`.* Since `χ` is non-principal, `Σ_{v mod q} χ(v) = 0`, so partial summation against
the smooth compactly supported `w` and the Pólya–Vinogradov bound
`|Σ_{m ≤ t} χ(m)| ≪ q^{1/2} log q` give
```
              |Ψ_χ(Y)|  ≪_w  q^{1/2} log q       uniformly in Y ≥ 1.                   (5.2)
```
(For `Y ≥ q^{1+ε}` one can do far better — Poisson plus the Gauss-sum evaluation
`Σ_v χ(v)e(−jv/q) = \barχ(−j)τ(χ)` gives `Ψ_χ(Y) ≪_A q^{1/2}(q/Y)^{A}` — but (5.2) suffices and is
uniform, hence is what we use. **Pólya–Vinogradov is a classical import, used only as an upper
bound; no new cancellation is asserted.**)

*Assembly.* Insert (5.2) into (5.1), bound `|μ(r/d)χ(d)| ≤ 1`:
```
| Σ_n M_Q(n)χ(n)w(n/N) |  ≤  q^{1/2}(log q) Σ_{r ≤ Q} (1/φ(r)) Σ_{d | r} d
                          =  q^{1/2}(log q) Σ_{r ≤ Q} σ(r)/φ(r)
                          ≪  q^{1/2}(log q) · Q (log log Q)^{O(1)} ,
```
using `σ(r)/φ(r) ≪ (log log r)^{2}` on average (indeed `Σ_{r≤Q}σ(r)/φ(r) ≍ Q`). This is
`q^{1/2}N^{c+o(1)}`. Comparing with the target `q^{1/2+ε}N^{1/2+ε}`: absorbed iff `c ≤ 1/2`. ∎

**Statement of record (D.59.3′).** *ATRH (`sup_θ|S̃(θ;N)| ≪ N^{1/2+ε}`) implies, for every primitive
`χ mod q` with `q ≤ Q = N^{c}`,*
```
 ψ_w(N,χ)  =  (τ(χ)/q) Σ*_{a mod q} \barχ(a) S̃(a/q;N)  +  Σ_n M_Q(n)χ(n)w(n/N)
            ≪  q^{1/2+ε} N^{1/2+ε}  +  q^{1/2} N^{c+o(1)},
```
*which is GRH-quality uniformly in `q ≤ N^{c}` for `c ≤ 1/2`, and of quality `q^{1/2+ε}N^{c+ε}` for
`c > 1/2`.* The equivalence `H^{cont}(∀k) ⟺ ATRH` (Thm D.59.3) is unaffected — it never involved
`M_Q`'s twisted sums — and the strictness discussion remains `OPEN`/`CANDIDATE` as labelled: ATRH
also asserts square-root cancellation at Diophantine-generic irrational `θ`, where the strongest
unconditional bound remains of Vinogradov type (`N^{4/5+ε}`), far from `N^{1/2}`, and where no
`L`-function conjecture applies at all. `PROVED`.

---

## 6. Repair (vi) — Hooley's `c_0`

**`CERTIFIED`, unchanged.** The value
```
c_0 = γ + log 2π + 1 + Σ_p (log p)/(p(p−1))
```
used in §4.4 is taken from the Montgomery–Hooley literature at second hand. **Hooley, "On the
Barban–Davenport–Halberstam theorem, I / II", J. reine angew. Math. 274/275 (1975), 206–223, has not
been read in this phase.** The label `CERTIFIED` is retained, and the constant must be verified
against Crelle 274/275 before it is quoted in any paper-facing text. Note that §4.4's *structural*
conclusion — that the additive pairing reproduces the finite part of the main term and misses an
archimedean constant — depends only on `c_0 − C_0` being a nonzero archimedean quantity, and would
survive a correction to the exact value; the displayed value `log 2π + 1` would not.

---

## 7. The D.60 dichotomy table, with the `k = 1` header supplied

The executive-summary table of `R149_001` §0 is a **`k = 1` statement** and must be headed as such.
Statement of record:

> **`k = 1` only.** With `Q = N^{c}`, `H(1,c)` is the Farey/large-sieve second moment:
>
> | **`k = 1`** | `c ≥ 1/2` | `c < 1/2` |
> |---|---|---|
> | `H(1,c)` | **PROVED** — it is precisely the Montgomery–Vaughan large sieve (Thm D.60.1) | **OPEN**; follows from GRH; unproved |
> | extraction from `H(1,c)` | `≪ N^{1/2+c+o(1)} ≥ N` — **vacuous** | `≪ N^{1/2+c+o(1)}` — **non-trivial** |
> | low-modulus segment provably negligible (§2.2) | **yes** (Siegel–Walfisz, Cor. D.60.7c) | **no** |
>
> **`k ≥ 2`: there is no dichotomy.** For every `c ∈ (0,1)`:
>
> | **`k ≥ 2`** | all `c ∈ (0,1)` |
> |---|---|
> | `H(k,c)` | **OPEN** — nothing is proved beyond Hölder interpolation from `k = 1`, which returns `≪ Q^{1/k}N^{1−1/(2k)}`, again `≥ N` for `c ≥ 1/2` (Thm D.60.4) |
> | extraction from `H(k,c)` | **non-trivial** for every `c`: `≪ N^{1/2 + c/k + o(1)}` |
> | low-modulus segment provably negligible | **no**, for any `c` (Cor. D.60.7c: requires `k < 2c ≤ 2`) |
> | equivalent content (Prop. D.62.1) | a `2k`-fold additive-energy bound for `Λ − M_Q` with square-root cancellation; for `k=2` this is the Hardy–Littlewood pair correlation on average with square-root error, i.e. (P149) |
>
> **So the `c = 1/2` "sharp block" is a `k = 1` phenomenon.** For `k ≥ 2` the hypothesis is
> simultaneously useful and open at every level, and the obstruction is no longer a threshold in `c`
> but the absence of any invariant theory beyond Parseval (Thm D.61.10′(2)).
>
> **Further, of record:** Hooley VII conjectures higher moments only in the range
> `x(log x)^{-A} ≤ Q = o(x/log x)`, i.e. `c → 1` — *exactly where the extraction is vacuous for
> `k = 1` and marginal for `k = 2`*. **The literature conjectures the hypothesis only where it is
> useless.** `IMPORTED` (the range), `PROVED` (the comparison, D.60.0).

---

## 8. Ledger of changes made by this round

| item | change | new status |
|---|---|---|
| D.59 framing | rewritten: "Hölder, not Weil I 3.2" (§0) | `PROVED` (Hölder), analogy flagged |
| (E) | **upgraded** to standalone Lemma D.59.0c, all `c<1`, error `O_A(N^{-A})` | `PROVED` |
| (C) | split: `PROVED` for `c<1/2` (D.59.0d); `OPEN` for `c ≥ 1/2` (D.59.0e) | `PROVED` / `OPEN` |
| (C′) | **demoted** to plausibility clause (P-C′); large-sieve justification **withdrawn** (§1.4) | `OPEN` |
| D.59.1, D.59.1a, D.59.2, D.59.4 | unaffected (use (E) only) | `PROVED` |
| D.59.3 | `M_Q` estimate supplied (Lemma D.59.3a); conclusion restated by level (D.59.3′) | `PROVED`; strictness `OPEN` |
| D.60 table | `k=1` header supplied; `k ≥ 2` table added (§7) | `PROVED` |
| D.60.7 | **rescoped** (D.60.7′): range + mechanism + "not refuted" proved; "provably negligible" only for `k=1, c>1/2` (D.60.7b–c); `2k`-power leg withdrawn | `PROVED`, scope reduced |
| "nothing unconditional for `k ≥ 2`" | reworded: no unconditional **upper** bounds; Ω-results exist | `IMPORTED` |
| dlB–Fiorilli / Harper–Soundararajan Ω-check | **run** (§3): **no contradiction with `H(k,c)`**; Gaussian order; margin `N^{c}` at `k=1` | `PROVED` (comparison), `CERTIFIED` (imports) |
| D.61.4 | **split by level** (D.61.4′): `d≠0, |d| ≤ Q`; `|d| > Q`; `d=0`; `Q=∞` | `PROVED` |
| D.61.7 | constant **repaired**: `V(x;Q) = xQ(κ_Q(0) − log2π − 1) + o(xQ)`; the `xQκ(0)` display withdrawn | `PROVED` |
| D.61.10 | **restated** as D.61.10′: no transport of the polar/positivity structure; (T1) Parseval written out, (T2) Goldston–Montgomery; three failures (positivity/index, `k≥2`, polar/Landau) | `PROVED` / `RESTATEMENT` |
| D.62.2 | citations corrected (D.62.2′): Granville 2007 Thm 1A + Corrigendum 2008 = sharp half; Bhowmik–Ruzsa = quasi-RH `β < 1−δ/6` | `PROVED` |
| Hooley's `c_0` | kept | `CERTIFIED` |

**Nothing in this round produces a zero-free region, a moment bound, or a cancellation estimate.
No sign is claimed. Row D: no label.** Labels of record are those of `R149_005`.
