# R169_091 — Audit of the input architecture (R169_000)

**Status:** audit. Labels PROVED / PROVED-CITED / ARGUED / OPEN / WRONG.
**Sources read:** R169_000; R163_901 Prop 1.1, Thm F; R165_201 Cor 2.2 / Lemma 3.3; R166_103 B1; R167_291 (items 3, 6, F2, F3, K3);
R168_102 Thms 1, 4, 5; R167_101 (L = log(γ/2π), Det+ bound T_c ≤ L/2 + O(1)).

## 0. Verdict in one paragraph

§4–§5 of R169_000 are **WRONG as written**, for two separate reasons. (i) γ_q is **not** a function of the window. The window
determines F, its nodes X and its phase function Φ_F, not the ordinate of an off-line zero (R163_901 Thm F gives a counterexample
inside the corpus). The selector [S] outputs a **set** Γ_S(F) of admissible heights. For fixed δ this set is a union of about
T_cγ/π intervals around the nodes of F: not discrete, not null, and not all of [0,∞). (ii) The "new primes in [X,Y]" are **not
free**. Since Y = Xe^Δ < X² for Δ < log X, primality on [X,Y] is decided by Eratosthenes with the window primes. For ℤ the tail of Λ
is a deterministic function of the window, so the Cramér "independence" model in Lemma D₀ is the wrong model of ζ and does not test
[D]. Corrected, 𝓘 must hold on all of Γ_S(F)∩[0,Y^A], a positive-density union of intervals near the nodes of F. This is not literally
covered by R168_102 Thm 4 (which needs every γ), so RH-equivalence is **not proved**. But every known input class is excluded
(γ-uniform → Thm 4; measure in t → A9; Eratosthenes/Legendre Type I → γ-uniform; bilinear → A11). The only surviving kind of [D]
correlates the Eratosthenes image of the window with **the node set of F**, and no such statement or strategy exists. Interior:
**formally non-empty, practically empty.** The honest label for "𝓘 is weaker than RH" is **OPEN, with no candidate**.

---

## 1. §1 proof skeleton

| step | verdict | note |
|---|---|---|
| 1 (contact, witness) | CORRECT | PROVED per R163_401 §2 / R165_101. |
| 2 (cone sign) | CORRECT | Identity (R165_201 Cor 2.2). Note that the sign is that of Re G(t_q)², and G is a window object (see §3 below). |
| 3 (Thm A identity) | CORRECT | Exact identity. |
| 4 (Re 𝒮 ≥ B) | **FIX** | R167_291 F3: what is proved is B/w(0) ≤ L[4c_Θe^{δΔ} − 0.35(2T+Δ)], an **upper** estimate for B. B > 0 needs 2T+Δ ≲ 11.4 c_Θe^{δΔ}. With T_c up to L/2 + O(1) (Det+), the regime B > 0 is a **bounded-T** (in units of c_Θ) regime. Step 4 must state the regime (Dom_θ + Prop E + this size constraint) explicitly. Without a **lower** bound on B, no comparison "fluctuation ≪ B" can be certified (see §4). |
| 5 (𝓘) | **FIX** | Must read "Re 𝒮(γ) < B(γ,δ) for all (γ,δ) ∈ Γ_S(F)", not "at γ_q" (§3). |
| 6 | CORRECT | Given 5 in the corrected form. |

## 2. A1–A12

| # | verdict | comment |
|---|---|---|
| A1 inequality | CORRECT | Forced by the identity results cited. |
| A2 upper bound | CORRECT | R166_802 C2: the zero itself gives the Ω-direction. |
| A3 uses n ≥ X | CORRECT | f_t (R166_501) shares the window and fails. **Add:** for ℤ, "data beyond the window" means data beyond the window *as a function of ℤ*. Λ on [X,Y] is determined by Λ on [1,X) through Eratosthenes when Y < X² (§5). So A3 really demands **use of integrality of ℤ** (the sieve map), not "extra primes". f_t has the same window but no sieve map, which is consistent. |
| A4 no zeros | CORRECT, **incomplete** | It must also forbid receiving γ_q as an *identified* datum. If the interface "receives γ_q" without knowing what it is, the bound has to hold for every value it could receive, i.e. on Γ_S(F). §2 of R169_000 ("recibe la frecuencia γ_q") is where the leak sits. |
| A5 | CORRECT | — |
| A6 Beurling class | CORRECT | Inherits the (S4) gap-axiom caveat of R167_291 §6. |
| A7 | CORRECT, **FIX wording** | Per R167_291 F2: "upper-bound halves with φ ≥ 0". Two-sided B–V is *not* excluded by A7. |
| A8 uses an identity of Λ | **FIX label** | "Forced" rests on R168_102 Thm 5, which is **ARGUED** (genericity step). So A8 is ARGUED-forced, not PROVED-forced. |
| A9 not uniform, not measure | CORRECT, **FIX scope** | "Not uniform": Thm 4 PROVED (implication). "Not measure": ARGUED (exceptional sets of large-sieve bounds can contain γ_q). **Add:** it must also not be uniform over Γ_S(F) **for every F**. That is a statement over all of [0,Y^A] again as soon as the admissible F's nodes sweep the line, so the bound must use *this* F. |
| A10 | CORRECT | — |
| A11 bilinear | CORRECT | T_γ(a,b) = A(γ)B(γ) factorises, so there is no cancellation from bilinearity (R168_102 Thm 1 PROVED). |
| A12 zero slack | **FIX citation** | "Theorem M; W2/M" has no file reference. Cite the file. Also, since B is only bounded above (step 4), "slack below B's margin" is not quantifiable yet. |

## 3. Is γ_q window-determined? NO. Characterisation of Γ_S(F)

**Prop 3.1 (γ_q is external). PROVED.** R163_901 Prop 1.1: (T_c, F, G, X) are functions of the window functional. Thm F of R163_901
constructs f = ζ + t·g with ζ's window functional on |u| < log N₀, off-line zeros, and a finite contact. By Prop 1.1, f and ζ (if
ζ has a contact below the window) have the **same** F. Their off-line zero sets differ: g is generic, and the quartets of f are
created by t·g. Hence the window does not determine γ_q; F is consistent with several (γ_q, δ_q). Even without Thm F, γ_q is an
ordinate of a zero of ξ, which depends on Λ over all of ℕ, while F depends on Λ|_{[1,X)}. ∎

**What the window does determine.** By R165_201 Cor 2.2 / Lemma 3.3, the quartet at t = γ − iδ is negative iff
cos 2Φ_F(γ,δ) < 0, where Φ_F(γ,δ) = arg G(γ+iδ) and G is the real entire, real-rooted window function with zeros (nodes) x_k. Define

  Γ_S(F) := {(γ,δ) : 0 < δ < ½, cos 2Φ_F(γ,δ) < 0, (γ,δ) in the Thm B regime (Dom_θ, Prop E, B > 0)}.

W(F) = 0 is not an extra constraint on a single quartet. It is one real equation, and the external rest of the zero set
(multiplicities, other quartets) can absorb it. So Γ_S is cut out by the cone condition and the regime.

**Prop 3.2 (structure at fixed δ).**
(a) PROVED. γ ↦ Φ_F(γ,δ) is strictly increasing. G is real with real zeros, of exponential type and in the Cartwright class (Paley–Wiener), so its Hadamard product gives
∂_γ Φ_F = Σ_k δ/((γ−x_k)² + δ²) > 0. There is no linear term, because G is real.
(b) PROVED. Each increment of Φ_F by π contributes exactly one maximal interval on which 2Φ_F ∈ (π/2, 3π/2) mod 2π. So Γ_S(F)_δ ∩ [0,γ] is
a union of N_F(γ) + O(1) open intervals. By Cartwright–Levinson (PROVED-CITED), N_F(γ) ~ T_cγ/π.
(c) ARGUED (needs node separation ≫ δ). Near an isolated simple node, G(x_k+u+iδ) ≈ G′(x_k)(u+iδ), so the interval is
|u| < δ(1+o(1)). In the sine-type model G = sin(T_c z), Γ_S is exactly {|tan T_cγ| < tanh T_cδ}, with density (2/π)arctan(tanh T_cδ) ∈ (0, ½).
(d) Hence Γ_S(F)_δ is **neither discrete nor null nor co-null**. It is a thickened, asymptotically quasi-periodic set
(step ≈ π/T_c) of positive density ≈ (2/π)arctan(tanh T_cδ) (ARGUED in general, PROVED for sine type). Projected over δ ∈ (0, δ_max),
it covers half-width ≈ δ_max around each node, which is most of the line when δ_max T_c ≳ 1.

**Consequence for §8's mandatory check.** The image of [S] is **large**: positive density in every [0,Y^A]. R168_102 Thm 4 does not apply
verbatim, because it needs all γ, and an off-line zero at γ₀ makes Re 𝒮 ≥ B only on part of a unit window around γ₀ (its phase rotates
at rate ≈ 2T+Δ). Whether that part must meet Γ_S(F) is **OPEN**. So "𝓘 on Γ_S(F) ⟺ RH at scale" is **not proved**. It is ARGUED to be RH-strength in
practice, because any proof has to tell Γ_S(F) from its complement, and Γ_S is defined only by proximity to F's nodes.

**Corrected §4–§5.**

```
window Λ|[1,X) + arch ──[S]──► F, G, nodes x_k ──► Γ_S(F) (set of admissible (γ,δ))
                         └──Eratosthenes (Y<X²)──► Λ|[X,Y] (deterministic)
[D] must give:  sup_{(γ,δ)∈Γ_S(F), γ≤Y^A} ( Re 𝒮_Y(γ) − B(γ,δ) ) < 0
```

## 4. Lemma D₀ in the Cramér model

**Setting.** ξ_n ∈ {0,1} independent with P(ξ_n = 1) = 1/log n for X ≤ n ≤ Y. ℱ_W is any σ-algebra independent of (ξ_n). γ is ℱ_W-measurable.
S(γ) = Σ_n ξ_n (log n) n^{−½+iγ} w(log n).

**Lemma D₀ (corrected). PROVED.** Conditionally on ℱ_W:
E[S | ℱ_W] = M(γ) := Σ_{X≤n≤Y} n^{−½+iγ} w(log n), and
Var[S | ℱ_W] = Σ_n (1/log n)(1 − 1/log n)(log n)² n^{−1}|w(log n)|² ≤ w(0)² Σ_{X≤n≤Y} (log n)/n ≤ w(0)²(Δ(log X + Δ/2) + O(log Y/X)).
*Proof.* Independence plus measurability: freeze γ and compute the variance of a sum of independent terms. The bound uses |w| ≤ w(0) and
Σ (log n)/n = ∫_{log X}^{log Y} u du + O(log Y/X). ∎
The sum is bounded and Bernoulli, so Hoeffding gives P(|S − M| > λ | ℱ_W) ≤ 4exp(−λ²/(2Σ_n (log n)²n^{−1}w(0)²)).

**Fixes to R169_000 §7.**
1. "≍" is **WRONG**; only "≤" holds. Nothing bounds |w| from below on [log X, log Y] (R167_291 K3).
2. The **mean M(γ)** was dropped. It is an integer sum at height γ. It is small (≪ Y^{1/2}γ^{−k}‖w^{(k)}‖) only for smooth w and γ ≫ derivative scale. Every bound must state this.
3. **The model is not a test of [D].** With N ≍ γ(2T+Δ) effectively independent heights, a union bound gives
   sup_{γ≤γ₁} |S − M| ≲ w(0)√(2Δ(2T+Δ) log γ₁) a.s.-eventually. So D₀ holds **uniformly in γ**: the model proves (U), the RH-strength
   statement, for itself. The selection by the window plays no role. The model cannot tell a good [D] from (U).
4. **The model is the wrong model of ζ.** In ζ, γ_q is not ℱ_W-measurable (Prop 3.1), and Λ|[X,Y] is ℱ_W-measurable through Eratosthenes
   (§5). Both hypotheses of D₀ fail for ζ.

**Size vs B.** The fluctuation is ≈ w(0)√(2TΔ) (with log X = 2T) and does not depend on γ. B ≤ L w(0)[4c_Θe^{δΔ} − 0.35(2T+Δ)], with
L = log(γ/2π), and B > 0 only for 2T+Δ ≲ 11.4c_Θe^{δΔ}. In that bounded-T regime both quantities are O(L w(0)) or smaller, and only an **upper**
bound on B is known. So "margin against B" is **ARGUED at best and uncertifiable as stated**. It needs a lower bound on B (OPEN).

## 5. Tail of Λ, B1, and "new primes"

**Prop 5.1. PROVED.** Let Y = Xe^Δ with Δ < log 2 and X ≥ 4. On [X,Y], Λ is supported on primes p ∈ [X,Y] and on prime powers p^k ∈ [X,Y]
with k ≥ 2, so p ≤ √Y < X. The power part is window data with total weight ≤ w(0)Σ_{p≤√Y, p^k∈[X,Y]} log p·p^{−k/2} = O(w(0)Δ).
Composite non-prime-powers carry Λ = 0, so "the composite tail is window-determined" says nothing about Λ.
R166_103 B1 is **CORRECT** and is bookkeeping (𝒯^det = powers of window primes). It puts **no** constraint on the new primes.
§5's "identity linking scales" is trivial: **FIX**.

**Prop 5.2 (the real link, missed by R169_000 and B1). PROVED.** If Y < X², then n ∈ [X,Y] is prime iff no prime p < X with p ≤ √n divides n.
So Λ|[X,Y] is a deterministic function of {p < X} and the integers. The "new primes are free / independent of the window" picture of §5 is false for ℤ.
The real content of [D] is a property of the **Eratosthenes map** window → tail at heights in Γ_S(F).

**Can that map carry [D]?** Expand with Legendre: Σ_{p∈[X,Y]} p^{−s} = Σ_{d|P(√Y)} μ(d)d^{−s} Σ_{m∈[X/d,Y/d]} m^{−s} (+ window terms).
The twist factorises: (dm)^{iγ} = d^{iγ}m^{iγ}. The inner sums are ζ-partial sums (Type I). Every known estimate for them (van der Corput, exponent
pairs, Vinogradov–Korobov) is uniform in γ, so it lands in R168_102 Thm 4 (RH-strength). The outer sum over d has 2^{π(√Y)} terms (Legendre
blow-up). Truncating it (Brun/Selberg) brings the parity problem and turns the bound into an upper sieve with φ ≥ 0, which A7 excludes.
ARGUED: no sieve truncation is sensitive to Γ_S(F).

## 6. Proof strategies for "the tail does not resonate at heights chosen by the window"

- **Bombieri–Vinogradov** is additive: it controls primes in progressions to moduli ≤ X^{1/2}, i.e. Dirichlet characters averaged over q. The
  twist n^{iγ} is the archimedean character. The archimedean analogue of "average over moduli" is **average over t**: the Gallagher /
  Montgomery large sieve ∫_0^{γ₁}|Σ a_n n^{it}|²dt ≤ (γ₁ + O(Y))Σ|a_n|² (PROVED-CITED). It bounds |𝒮| ≤ K outside a set of measure
  ≲ γ₁·polylog/K². That is a **measure statement**. The exceptional set can contain Γ_S(F)'s component around γ_q, so A9 excludes it.
  Zero-density estimates are the same kind of statement.
- **Restricting the large sieve to Γ_S(F)**: Γ_S has positive density, so the restricted mean square is the same order. Still a measure statement. Excluded.
- **Using quasi-periodicity of Γ_S** (step π/T_c, X = e^{2T_c}): the shifts γ ↦ γ + πk/T_c multiply n^{iγ} by e^{2πik log n/log X}. A bound on a
  thickened progression is still an average over k. ARGUED: no pointwise gain.
- **Surviving form**: a statement correlating {Λ(n)}_{X≤n≤Y} = Erat(window) with the **specific** nodes of the window function G. Nothing of this kind
  is known. No method in the corpus or the literature (BV, large sieve, Type I/II, Diophantine) reads the nodes of G.

**Final verdict.** With §3's correction, A4 + A9 do not *prove* that 𝓘 is RH-strength: the uniform-over-Γ_S version is OPEN as to equivalence.
But they leave as interior only inputs of the form "the Eratosthenes image of the window does not resonate on the node neighbourhoods of the window's own
witness function". That class is formally non-empty, contains no known statement, and has no proof strategy. Lemma D₀ is PROVED in the Cramér model
but is uniform in γ there, so it is uninformative about [D]. R169_000 §4–§5 must be rewritten with Γ_S(F) in place of γ_q and with Eratosthenes
(Prop 5.2) in place of "new primes are free".

## Ledger

| item | label |
|---|---|
| Prop 3.1 γ_q not window-determined | PROVED (via R163_901 Prop 1.1 + Thm F) |
| Prop 3.2 (a)(b) structure of Γ_S | PROVED / PROVED-CITED (Cartwright–Levinson) |
| Prop 3.2 (c)(d) positive density ≈ (2/π)arctan tanh(T_cδ) | PROVED for sine type, ARGUED in general |
| 𝓘 on Γ_S ⟺ RH at scale | OPEN (ARGUED RH-strength in practice) |
| Lemma D₀ (upper bound, with mean) | PROVED in model; "≍" WRONG |
| D₀ margin against B | ARGUED / uncertifiable (B only bounded above) |
| Prop 5.1 B1 is bookkeeping | PROVED |
| Prop 5.2 tail = Eratosthenes(window) for Y < X² | PROVED |
| R169_000 §4–§5 as written | WRONG |
| existence of a candidate [D] | OPEN, no candidate |
