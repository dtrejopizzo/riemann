# R131.006 — Blueprint, round 3: the Frobenius family, the integral shadow, and the Weil interface

Status: `BLUEPRINT` (to be
proved in Paper 44 by the construction, attacked by the audit). Decision:
B.4 amendment ACCEPTED; instruction: resolve the recorded
reservations of R131.005 with new mathematics, no relabeling.

Reservations to dissolve: (R1) the norm classes forget factorization; (R6)
B.6 vacuous for composite `n`; (R3) the source has no dagger, unit is a
projector; (R2) `Z/Φ_n(1)` is not the value of anything on the objects —
"integral carrier" needed; (R4) `Λ`-as-shell-volume inherited; (R5) no
interface with the sign. Conventions of Paper 43/44; `j_p(p^k w) = (p^{−k}; w
at p; p^{−k} at r ≠ p)`, `j_∞(x) = (x; 1,…,1)` (Paper 43 (9.5b)).

---

## 0. The insight: the Frobenii are the fixed-point strata, and they remember `n`

Paper 44 used two objects: the element class `E_{a_S(n)}` (class `(1/n;1,…,1)
= j_∞(1/n)`, on the **archimedean** slice — hence its finite contact is `0`
and its "unit factors" were artifacts) and the norm class `Γ_n^{rad}` (the
whole level set, which forgets factorization). Neither is Frobenius. Define,
for a prime power, the **local Frobenius**

    Frob_{p^k} := ∫_{Z_p^×} E_{j_p(p^k u)} du   (probability Haar on Z_p^×),

the Haar measure of the fixed-point stratum `j_p(p^kZ_p^×) = {(p^{−k}; u at p;
p^{−k} at r ≠ p) : u ∈ Z_p^×}` of the local dilation action at `p` — the
correspondence of the local prime-power ideal `p^kZ_p`, with the other
coordinates as row A's canonical representative dictates. For general
`n = ∏ p^{k_p}` define the **arithmetic Frobenius**

    Frob_n := ⋆_{p|n} Frob_{p^{k_p}} = ∫_{∏_{p|n}Z_p^×} E_{ι(n)·u} du ,
    ι(n) := (1 at ∞ ; p^{v_p(n)} at every finite p) ,

whose class support is `{(1/n ; u_p ∈ Z_p^× for p|n ; 1/n at r ∤ n)}` — a
proper sub-orbit of the level set `|x| = 1/n` that records **which** primes
divide `n` (the averaged coordinates) and `n` itself (the modulus and the
fixed coordinates `1/n` at `r ∤ n`). Checked by the review:

  (a) *Monoid with true unit.* `Frob_m ⋆ Frob_n = Frob_{mn}` for all `m,n`
      (Haar on `Z_p^×` is convolution-idempotent; `ι(m)ι(n) = ι(mn)`), and
      `Frob_1 = E_{ι(1)} = Δ` — the diagonal itself, not a projector.
  (b) *Weil's degree relation.* `Frob_n ⋆ Frob_n^† = Δ^{(n)} := ∫_{∏_{p|n}Z_p^×}
      E_{j(u)} du`, the diagonal averaged over the local units at the primes of
      `n` — the normalized form of `Γ_F ⋆ Γ_F^t = q·Δ`, with the half-density
      having absorbed `q` and the averaging projector `Δ^{(n)}` playing the
      role of the degree. Hence the family closed under `†` is
      `{Frob_r : r ∈ Q_{>0}^×}`, `Frob_{a/b} := Frob_a ⋆ Frob_b^†`, a
      commutative inverse semigroup with idempotents `Δ^{(n)}` (the
      Bost–Connes relations in commutative, averaged form).
  (c) *Contact.* For `n = p^k` the support of `Frob_n` **is** `Im j_p` on the
      shell `k`, so its finite contact is the shell volume × half-density,
      `(log p)p^{−k/2} = Λ(n)n^{−1/2}`; for composite `n` the support meets no
      `Im j_q` (modulus `1/n` is no `q^{−m}`), so the contact is `0 = Λ(n)`.
      **Now the object knows it is composite and the theorem says its contact
      vanishes** — (R1), (R6) dissolved.
  (d) *The archimedean Frobenius.* `Frob_∞(t) := E_{j_∞(e^{−t})}`: Paper 44's
      element class is `Frob_∞(log n)`. Its contact is the archimedean density
      `K(t)`. So the two slices of row A's trace are the two Frobenius flows:
      finite (discrete, at prime powers) and archimedean (continuous).
  (e) *Smearing into `D_A`.* `Frob_n^{(ε,N)} := Frob_n ⋆ ρ_ε ⋆ 1_{U_N}` with
      `ρ_ε` a bump at `1 ∈ R^×` and `U_N = ∏_{r∤n}(1+r^NZ_r)` (level-`N`
      neighbourhood of the fixed coordinates) lies in `D_A ∩ D_A^0` for `n ≥ 2`,
      and its finite contact is **exactly** `Λ(n)n^{−1/2}·∫ρ_ε` for every `N`
      and small `ε` (no limit needed at the finite places; the archimedean
      term is `∫K(|t|)ρ_ε(t − log n)`-type). Point classes `Frob_n ∈ N_A^{dist}`
      as in Thm 8.3.

## 1. The integral shadow on the objects (dissolves R2)

P123.022 §2 forbids an **additive `C`-linear** functor carrying `Z/p`; its
Scope paragraph explicitly allows "an integral or lattice category with a
complex realization … such additional structure must be constructed". The
lattice `L_S = ∏_{p∈S_f}Z_p ⊂ X_S` is part of the declared coefficient
geometry (P123.038 §2) and the arithmetic anchor `b_S(a) = a_f/a_∞` is
gauge-invariant. Define the **integral shadow** on the arithmetic monoid

    Sh_Z(Frob_n) := Cone( L_S →^{ι(n)} L_S ) = Q_{S,n} ,   (multiplication by ι(n)_f)

(`ι(n)L_S = nL_S`, so this is P123.038's `Q_{S,n}`, now attached to the object
`Frob_n` through its own action on the lattice, not to a label). Prove:
  * well defined on classes (gauge invariance of `b_S`; averaging over
    `∏Z_p^×` acts trivially on `nL_S`);
  * the transitivity exact triangle `Sh_Z(Frob_m) → Sh_Z(Frob_{mn}) →
    Sh_Z(Frob_n)` (P123.038 §3's lattice sequence) — `Sh_Z` is multiplicative
    in **degree**, `deg_det Sh_Z(Frob_{mn}) = log m + log n`, and not monoidal
    on the nose (P123.037 §5, Paper 44 Thm 5.4);
  * `H⁰ Sh_Z(Frob_n) = L_S/nL_S ≅ Z/n`, and the Möbius cofiber over the divisor
    poset is `Prim_n = [Z →Φ_n(1)→ Z]` (P123.038 (4.1)), i.e. **the integral
    cyclotomic contact is the primitive part of the integral shadow of the
    Frobenius object**, exactly as `H^1` is the value of a functor on `Γ_F`
    and not an object of `Corr(C)`;
  * **Comparison theorem (the amended B.4, now on objects):** for `n ≥ 2`,
    `contact_fin(Frob_n) = n^{−1/2}·deg_det Prim(Sh_Z)_n`, and
    `deg_det Sh_Z(Frob_n) = log n = Σ_{d|n} d^{1/2}contact_fin(Frob_d)`.
    Both sides are functorial in the object; the equality is of degrees; say
    that a complex-linear identification is impossible (P123.022) and that
    `Sh_Z` is the integral structure P123.022 §2 said had to be constructed.

## 2. The Weil interface (dissolves R5 honestly, without a sign)

  * *Gram matrix of the family.* For the smeared Frobenii,
    `I_A(Frob_m^{sm}, Frob_n^{sm}) = T(Frob_{m/n}^{sm})`; its finite part is
    `Λ(m/n)|m/n|^{−1/2}`-type (nonzero iff `m/n = p^{±k}`), its archimedean
    part is the density at `log(m/n)`, and on the diagonal `m = n` the
    self-pairing `T(Δ^{(n)} ⋆ ρ_ε⋆ρ_ε^†)` **diverges to `−∞` like
    `−2 log(1/ε)`** as `ε → 0` (Paper 43 Thm 9.7: `Ŵ_∞ ~ −log|τ|`). Record this
    as the theorem **"the self-intersection of the diagonal is `−∞`: the
    arithmetic curve has infinite genus"** — Weil's `Δ·Δ = 2−2g` with
    `g = ∞`, consistent with spec §1's "finite rank is inadmissible".
  * *Interface theorem (CLASSICAL in one direction).* The Hodge-index
    inequality `I_∂ ≤ 0` on primitive finite combinations of smeared
    Frobenii (Dirichlet-polynomial tests) is equivalent to Weil's positivity
    criterion, hence to RH: density of `{Σ c_n ρ_ε(t − log n)}` in
    `C_c^∞((0,∞))` because `{log n}` has gaps `→ 0`, plus `†` for `t<0`, plus
    Paper 45's Thm 10.4 (primitivization). State exactly which direction uses
    the explicit formula and label it `CLASSICAL`; state that **row B's
    deliverable is the object whose Hodge index is RH — the Gram form of the
    Frobenius family — and not the sign**, which is row D.

## 3. `Λ` as shell volume is now earned, not inherited (R4)

In row A, `Λ` appeared as the Fourier coefficient of a symbol (Rem 9.7a). Here
it is the contact of a named object: `contact_fin(Frob_{p^k}) = vol(j_p(p^kZ_p^×))
·p^{−k/2}`, with `Frob_{p^k}` the Haar measure of that very stratum. Say so.

## 4. Deliverables

Paper 44 new §3ter "The Frobenius family" (Defs, Thms for 0(a)–(e)), §6bis
"The integral shadow" (§1), §8bis "The Weil interface" (§2, with the infinite
genus theorem), contract table and §10 re-issued (B.1: source `(N,×)` and its
inverse semigroup; B.2–B.3 for `Frob`; B.4 amended on objects; B.6 both halves
non-vacuous), §9bis extended, README, `R131_007_ROUND3.md`. Every
claim above must be re-proved; if any is false, say so with the counterexample.
Do not claim a sign, `𝓝_∞ = 0`, or anything about zeros beyond the labelled
CLASSICAL equivalence.
