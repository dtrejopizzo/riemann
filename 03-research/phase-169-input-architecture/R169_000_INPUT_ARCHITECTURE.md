# R169_000 — Architecture of the missing input to close D

**Status:** specification (lead). The existence of the input is not asserted. Every required property is forced by a
theorem on record, cited. The goal is for whoever builds it to know exactly what has to be done and what cannot be done.

---

## 1. Where it plugs in (the proof of D with the gap marked)

1. Suppose D does not hold. Then there exists a first contact T_c ∈ (0.8047, min_ρ τ(ρ)] and a real-rooted witness F, of type
   T_c, with nodes X (R163_401 §2; R165_101). **PROVED.**
2. At the cell of the lowest quartet t_q = γ_q − iδ_q, the sign of the quartet is cos 2(Φ_Z ± πω(E) + Ψ_out) < 0 (R165_201).
   **PROVED** (identity).
3. For every test Ψ = G(·+γ_q)²k with k ≥ 0 of type Δ (R167_101 C1), the exact identity holds:
   4 Re 𝒮 = (L/π)I − Q_K − R_K − O_K + polar, with 𝒮 = Σ_{n≤Y} Λ(n) n^{−½+iγ_q} w(log n), Y = Xe^{Δ}, X = e^{2T_c}
   (R167_101 Thm A). **PROVED.**
4. The negative quartet forces Re 𝒮 ≥ B, with B = (1−θ)c_Θ|G(t_q)|²|k(−iδ_q)| − E_K/4 > 0 in the regime of R167_101 Prop E
   (R167_101 Thm B, given (Dom_θ)). **PROVED given (Dom_θ).**
5. **[THE INPUT 𝓘]:** Re 𝒮 < B.
6. Contradiction. No witness. D holds.

The input 𝓘 is line 5. Everything else is written and audited. (The small-y regime, R167_101 Prop E / R168_103, needs
P_gap in addition; see §6.)

## 2. Interface

- **Receives:** the scale X = e^{2T_c}; the space Δ; the weight w (its transform G(s+γ_q)²k(s) ≥ 0, support of length 4T+2Δ,
  |w| ≤ w(0)); the frequency γ_q; the sequence Λ(n), n ≤ Y. **Nothing else.** In particular it does not receive the zeros.
- **Delivers:** Re Σ_{n≤Y} Λ(n) n^{−½+iγ_q} w(log n) < B, with B ≈ L[4c_Θ e^{δΔ} − 0.35(2T+Δ)]·w(0) (R167_291 item 6),
  polylogarithmic in γ_q. That is: an **upper, one-sided, single-scale bound of polylog size**, where the trivial bound
  is ≍ Y^{1/2}.

## 3. Mandatory properties (each with the theorem that forces it)

| # | property | what it excludes | forced by |
|---|---|---|---|
| A1 | It is an **inequality**, not an identity | every reformulation of the explicit formula | E1; R166_201 Thm 1.3 (jets); R167_102 Thm E |
| A2 | It is an **upper** bound on Re 𝒮 (not an Ω bound) | lower bounds, which the zero itself gives | R166_802 C2, Thm 1–2 |
| A3 | It uses Λ **beyond the window** (n ≥ X) | any window-only datum | R166_501 Thm A (f_t); R167_101 Prop W (covers all of [1,Y]) |
| A4 | **It does not use the zeros** | circularity | R166_802 Thm 3 |
| A5 | **It is not positivity or integrality together with the FE** | identification | R164_401 Thm R; Hamburger; R163_1001 Thm O |
| A6 | **It is not a Beurling-class property** (Euler + Λ ≥ 0 + PNT + regular N) | DMV/Zhang systems with zeros off the line | R167_103 Theorem S; R168_102 Thm 5 |
| A7 | **It does not follow from 0 ≤ b ≤ Λ + support + upper bounds + large sieve** | b_θ | R167_102 Thm B′ (+ R167_291) |
| A8 | **It uses an identity for Λ** (Möbius, Selberg, or structure of ℤ beyond support on prime powers) | — (consequence of A6–A7) | R167_102 §8; R168_102 Thm 5 |
| A9 | **It is not uniform in γ** in the range γ ≤ Y^A (that would be RH) and **is not a measure statement** in γ (blind to γ_q) | (U) and large sieve in γ | R168_102 Thms 2, 4 |
| A10 | **It is not cosine-polynomial positivity** (dlVP, Fejér–Egerváry) | trivial cap Y^{1/2} | R168_201 D2-5; R164_601 Thm 3.3 |
| A11 | **It does not use bilinear factorization of the twist** (n^{iγ} = m^{iγ}k^{iγ} gives no gain) | Vaughan/Heath-Brown with multiplicative twist | R168_102 Thm 1 |
| A12 | Holds **with no slack** at the witness (zero margin) or with slack smaller than the margin of B | estimates with slack | Theorem M; W2/M |

## 4. The structural consequence of A4 + A9

A9 says 𝓘 cannot hold for all γ ≤ Y^A (that is RH via Landau) nor for almost all γ (blind to γ_q). A4 says it cannot
use the fact that γ_q is the ordinate of a zero. **So 𝓘 has to hold on a set of frequencies defined with no zeros, that
contains γ_q, and that is small enough for the bound not to imply RH.** The only way to define γ_q with no zeros within
the interface of §2 is **through the window**: γ_q is the frequency the witness selects, and the witness is a function of
Λ(n), n < X (R163_901 Prop 1.1, window locality).

> **Necessary form of 𝓘 (consequence of A3, A4, A9):** a relation between **Λ in the window** [1, X) and **Λ in the tail**
> [X, Y], evaluated at the frequency the window selects. That is, a **decorrelation principle between scales**:
> the window cannot select a frequency at which the tail resonates.

This is what does not exist in the literature: the known results on Λ deal with sums over a range at a given frequency, or
averages over frequency. None relates **the frequency chosen by a range** to **the sum over the next range**.

## 5. Architecture of the input (components)

```
 window Λ(n), n<X ──► [S] selector ──► γ_q, w  ──┐
                                                   ├──► [D] decorrelator ──► Re 𝒮(tail) < B
 tail Λ(n), X≤n≤Y ────────────────────────────────┘
```

- **[S] Selector (exists, PROVED):** the map window ↦ (T_c, F, X, γ_q, w) of the first contact (R163_401 §2, R165_202
  flow). It is deterministic and depends only on Λ in the window and on the archimedean term.
- **[D] Decorrelator (MISSING):** an inequality bounding Re 𝒮_tail(γ) **at the γ's that can come out of [S]**, using
  identities for Λ linking window and tail (A8). Identity candidates linking scales, to be tested:
  - Möbius/Selberg in the tail expressed with divisors in the window: for X ≤ n ≤ Y = Xe^{Δ} with Δ < log 2, every composite n
    has a factor < √Y ≤ X: **the composite tail is determined by the window** (R166_103 B1, 𝒯^det). Only the primes
    p ∈ [X, Y] are new. This is the identity linking scales; A8 requires it.
  - The selector uses Λ up to X; the determined part of the tail uses Λ up to √Y < X: **both use the same datum**. This is
    the only exact dependency between selector and tail that is on record.
- **[D] has to satisfy:** over the new primes p ∈ [X, Y] (the only free ones), a bound on Re Σ_p (log p) p^{−½+iγ_q} w(log p)
  that uses the fact that γ_q was chosen by data that **does not** include those primes. It is a statement of
  **independence**: the primes of [X, Y] do not "know" what frequency the window chose.

## 6. Battery of falsifiers that 𝓘 must fail or respect

| model | what it does with 𝓘 | why |
|---|---|---|
| ζ (if RH) | 𝓘 holds | must |
| M_m | 𝓘 must **fail** at its witness | its β_m pays for the quartet (R167_101 §5) |
| f_t | 𝓘 must fail or be inapplicable | no Euler product, same window (R163_901) |
| DMV/Zhang (± generic perturbation) | 𝓘 must fail | A6 |
| b_θ | 𝓘 must not follow for b_θ | A7 |
| Kronecker-resonant frequencies | irrelevant at the witness's scale | R167_291 (log γ ≳ Y/log Y) |
| Cramér random systems | **decisive test**: random primes independent of the window satisfy the decorrelation on average; 𝓘 has to be deterministic for ζ | §5 |

Plus the small-y regime: if δ_q log γ_q < y₀, 𝓘 is not enough (R167_101 Prop E); **P_gap** is also needed (R168_103): a zero
on the line at distance between c₂δ and c₁/Λ from the quartet. P_gap is an input on the zero side that M_m violates; its
architecture is the same question on the dual side.

## 7. The first lemma to prove (falsifiable)

> **Lemma D₀ (decorrelation of a prime).** Let γ = γ(Λ|_{[1,X)}) be any frequency measurable with respect to the σ-algebra
> of the window. For the Cramér model (primes in [X, Y] independent of the window with probability 1/log n), prove
> E|Σ_{p∈[X,Y]} (log p) p^{−½+iγ} w(log p)|² ≍ Σ (log p)²/p |w|² ≍ Δ·w(0)²·log X, i.e. **size √(Δ log X), polylog**:
> the input holds in the random model with margin relative to B.
> **Then:** identify which deterministic property of the real primes replaces "independence of the window". Candidates:
> (a) sieves of primes in [X, Y] with moduli < X (Bombieri–Vinogradov bounds primes in progressions with modulus ≤ X^{½}: this
> is exactly window information about the tail, and is **specific to ℤ**, A8); (b) the Vaughan identity restricted
> so that the small factors lie in the window.

Lemma D₀ is likely provable in the Cramér model (it is a variance computation). The new content is the deterministic step: **a
version of Bombieri–Vinogradov "at a frequency selected by the window"**. That is what does not exist.

## 8. What the architecture does NOT guarantee

- That 𝓘 is true for ζ without RH. Under RH it is true (the sum is O(log² Y)). Without RH its truth is exactly what is
  at stake.
- That 𝓘 is weaker than RH. A9 forces it to not be uniform in γ; if the class of frequencies [S] can produce turns out
  to be dense in [0, Y^A], 𝓘 becomes RH again (R168_102 Thm 4). **First mandatory check:** the size of the image set of [S].

---

## v2 — Corrections from audit R169_091 (accepted) and final reading

**Corrections.** (1) γ_q is **not** determined by the window (PROVED: R163_901 Thm F gives the same window, the same F and
different zeros). What the window determines is Γ_S(F) = {(γ,δ): cos 2 arg G(γ+iδ) < 0} ∩ regime of Thm B: a union of ≈ T_cγ/π
intervals (one per node), positive density ≈ (2/π)arctan(tanh T_cδ) (PROVED for sine type, ARGUED in general). §1 step 5
should read "𝓘 holds on all of Γ_S(F)". (2) "Free new primes" is FALSE for ℤ: since Y < X², the primes in [X, Y] are
determined by the primes of the window via the sieve of Eratosthenes (PROVED). (3) Lemma D₀: the conditional mean M(γ) is not
zero; it is only an upper bound on the variance; the Cramér model satisfies the bound uniformly in γ and gives no information
about [D]. (4) A8 remains ARGUED-forced (it rests on R168_102 Thm 5 ARGUED); the "measure" part of A9 is ARGUED; A12 has no
file reference.

**Reading of the lead (ARGUED, to be audited).** With (1) and (2), for each scale X the quantity 𝒮(γ), γ ∈ Γ_S(F), is a
**function of the window alone**: Λ on [X, Y] is Eratosthenes of the primes < X, and G, w, Γ_S(F) are functions of the window.
So, at a fixed scale X, 𝓘 is an inequality about a finite, explicit Dirichlet polynomial on a compact set of heights:
**verifiable by certified computation**, like the certificates of Paper 46 up to ½log5. The infinite content of 𝓘 lies solely
in the quantifier over X (all scales up to e^{2T_max}), which is the **master quantifier W2 / Theorem M** of the grid.
Conclusion: the interior of the architecture, once corrected, coincides with the per-window certificate program; the "new"
input reduces to a law guaranteeing, uniformly in X, the outcome of a finite per-window computation — exactly the form of
row D. f_t does not satisfy it because its tail is not the Eratosthenes sieve of its window (no Euler product). The only new
structural piece this phase leaves behind is the **window→tail Eratosthenes link** as a datum specific to ℤ at the level of
a single scale.
</content>
