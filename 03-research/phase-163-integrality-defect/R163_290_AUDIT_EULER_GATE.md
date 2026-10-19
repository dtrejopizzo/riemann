# R163_290 — Audit of the Euler-gate proposal (round 31)

**Scope.** Proposal (U)+(G) from the round-31 brief, against R163_161, R163_162, R162_2001/2190.
The construction files R163_201/202/203 were **not present** when I polled the directory (three checks). They are not audited here.
Cell: Euler gate. Wall it would have to evade: E1 (gate equivalent to the conclusion) together with W2/W4/W5.

## (a) Uniqueness lemma (U): **CORRECT WITH FIXES**

1. **Type.** With supp F ⊂ [−T,T], y ↦ K_F(1+iy) = ∫F(u)e^{u/2}e^{iyu}du is the Fourier transform of F·e^{u/2}, which is supported in [−T,T]. So it is Paley–Wiener of **type T** (spectral interval of length 2T). It is not the autocorrelation.
2. **Which object the modes involve.** By R163_161 (6), P̂_G^{(p)}(k) = K_F(1+iω_k)/[ℓ_p(1+iω_k)], with ω_k = 2πk/ℓ_p. Here the factor 1/(1+iω_k) never vanishes, so mode vanishing is exactly K_F(1+iω_k)=0, an object of type T. The type-2T object (a product of two Mellin lines) appears only in the **pairing** R163_161 (8), ⟨h,H_G⟩ = Σ_k conj(K_F(1+iω_k))K_h(1−iω_k)/(ℓ(1−iω_k)). **Fix:** (G) must be stated as the vanishing of every mode, H_G^{(p)}=0. A vanishing pairing is one scalar equation, and (U) says nothing about it.
3. **Density criterion.** Each lattice {2πk/ℓ_p} has density ℓ_p/2π. The lattices are pairwise disjoint away from 0 because ℓ_p/ℓ_q is irrational. A union of finitely many such lattices is uniformly distributed, so its Beurling–Malliavin density equals θ(P)/2π. Completeness radius: the union is a uniqueness set for PW_T if θ(P)/2π > T/π, i.e. **θ(P) > 2T**. The inequality must be strict. The example sin(ℓ₂y/2)·sin(ℓ₃y/2) has type exactly (ℓ₂+ℓ₃)/2 and vanishes on the union, so the threshold is sharp. At T = 0.8047: log 6/2 = 0.896 > 0.8047, so {2,3} suffice. For the Λχ₂ variant, {3,5} gives (log 15)/2 = 1.354.
4. **k=0.** Removing finitely many points does not change density. With strict inequality, removing k=0 is harmless, and K_F(1)=0 already supplies that point. **Caveat for the elementary proof** (dividing by sin·sin instead of citing BM): y=0 is common to both lattices, so the quotient needs the extra factor y. Do not bound the quotient on the real axis, because near-coincidences 2πk/ℓ₂ ≈ 2πm/ℓ₃ spoil any lower bound for sin·sin there. Bound it on Im y = ±1 and use Phragmén–Lindelöf in the strip.
5. **Stronger and trivial form (important).** For a single prime with ℓ_p > 2T: G = VJF is supported in [−T,T], which is shorter than the period ℓ_p. Its periodization e^{−u/2}G, and hence H_G^{(p)}, then vanishes iff G = 0. No BM argument is needed. Note that ℓ₅ = 1.6094 = 2·(½log 5) exactly, so every prime p > e^{2T_*} forces F=0 on its own. These are exactly the primes that R163_162 (8)–(9) shows are invisible to P_T T_p P_T.

## (b) Gate (G): **CIRCULAR**

- (U) holds for **every** F ≠ 0 supported in [−T,T] with T < θ(P)/2, whether or not F is a contact vector. So (G) is not a property that some nonzero contact vectors could have. It is false for every nonzero F. "(G) at first contact" is therefore equivalent to "F = 0", i.e. no first contact on that window, which is the conclusion D on the window. The gate adds no intermediate content. Any proof of (G) is a proof of F=0 by other means. This is E1 in a new form: like R_LF = 0, it is a restatement of the target, now with a trivial Fourier lemma attached.
- (G) is also **weight-blind**. H^{(p)} depends only on F and log p, not on the Euler weights, the Gamma factor or the contact equation. All the arithmetic would have to enter through the derivation of (G), and none is proposed.
- The only contact information available is R163_161 (9)–(10). It gives ⟨A_loc F,G⟩ = a_F·conj(K_F′(0)) and involves **no** mode with k≠0. R163_161 states this explicitly: imposing H_G = 0 "sería otro gate". By R163_161 (7), the physical solution (the subprincipal signature) is the **unstable** D_+. Claiming that physical equals stable D_− for a nonzero F contradicts (U) outright.
- Verdict: (G) cannot be a lemma. It can only be the last line of a proof of D.

## (c) Falsifiers: they do not separate (U), and cannot test (G) until (G) has a derivation

- **Beurling–DMV (real p).** (U) needs only distinct lattices and θ(P) > 2T. It holds verbatim for generalized primes, so the forcing step does **not** fail in DMV, contrary to what the brief requires. Integrality is not used anywhere in (U). It would have to enter the derivation of (G), which does not exist. Falsifier status: (U) fails the DMV separation test. This is harmless only because (U) is a triviality.
- **Z_K (2-factor raised to K+1).** The homogeneous solutions of (I−U₂)^{K+1} are polynomial × periodic, and their leading coefficient again involves K_F on the same lattice. (U) still forces F = 0. No separation.
- **Λχ₂ (no 2-factor).** Use {3,5}. (U) holds. No separation.
- **Two-atom Type I curve (R162_2001/2190).** Its contacts are at T_c ∈ [0.553, 0.607] with F ≠ 0. That is below log 6/2 = 0.896, and just above log 3/2 = 0.549, so both 2 and 3 are window primes. By (U), the modes of that contact vector **cannot** all vanish. The gate is not "dead by vanishing modes"; in this model (G) is simply false, as it must be. This is consistent, but it shows only that (G) fails wherever a contact exists, which is the circularity of (b). The decisive question is what in the derivation of (G) breaks for weights (s₂^c, s₃) at distance 2.4·10⁻⁴ from ζ. The proposal says nothing about this.
- **Deletion / Epstein–DH.** With no Euler factor, (G) is undefined. Vacuous, not a test.

## (d) Hidden positivity, margins, per-window estimates: **CORRECT (none hidden), with one remark**

(U) uses no positivity, no Theorem M margin and no per-window certificate. It is pure Paley–Wiener / periodization. The input T_* > 0.8047 (½log 5) comes from the certified positivity on T ≤ ½log 5. It only places T_* above that bound and plays no role in (U). Remark: the brief's "p ∈ {2,3} suffice at T ≈ 0.8047" holds only for T_* < 0.896. Since T_* is only bounded **below**, (U) must use the primes p ≤ e^{2T_*}, and then θ(P) > 2T_* holds automatically because θ(x) ≫ log x. That is fine, but the statement should be uniform in T_*.

## Bottom line

(U) is correct, with the fixes above, and elementary. In fact one prime with log p > 2T already forces F=0. (G) is equivalent to the conclusion: it holds for no nonzero F. The proposal moves the whole of row D into "derive (G) from the contact equation", and R163_161 (10) shows the contact equation does not see the k≠0 modes. **NO-GO as a route until a derivation of (G) is supplied that uses integrality and fails on the two-atom curve.** No label change.
