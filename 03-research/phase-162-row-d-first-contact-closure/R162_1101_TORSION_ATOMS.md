# R162_1101 — Round 11: non-band-limited torsion tests from the first-contact vector — **NO-GO (PROVED), three new exact structures**

Note. Inputs: README (F1–F4, rounds 1–10), R162_590, R162_1001 (Thm 3.1, Prop 3.2, Thm 5.1),
R162_201 (Thm 2.1, ESB), R162_402 (Thm 1.3, (1.1)). Conventions of R162_1001: ν_d uniform on d-torsion of ℝ/ℤ,
Φ_a = Σ_{d≥2} a(d)(ν_d − Leb), Φ̂_a(k) = (a*1)(|k|) (k≠0), cocycle (3.1) ℒ_pΦ_Λ − Φ_Λ = log p(δ_0 − Leb).
s = ½+z, a_m = 2m+½, K_F(z) = ∫F(t)e^{zt}dt, H_+ = G_+/ζ = −(ζ'/ζ)K_F − Q_+ (R162_402 (e)).

**Status.** The requested object is built: three families of non-band-limited, rational-singular tests from F at finite T_*
(§2 log-port test, §3 Farey/divisor lifts, §4 atomic self-test). None closes Gate 1. Labels:
- Thm 1.1 (duality: every test reads Φ_a as Σ a(d)u_g(d); "atoms" ⟺ infinite support of u_g) PROVED.
- Thm 2.1 (the log port is a torsion pairing: H_+(z)+Q_+(z) = ½K_F(z)⟨Φ_Λ, g_{½+z}⟩, g_s = ζ(s)^{-1}Σ_{k≠0}|k|^{-s}e(kx)) PROVED. **New.**
- Thm 2.2 (atom localisation at the Gamma lattice: the polar part of g_s at s=−2m is a multiple of δ_0^{(2m)}; the
  pole that Gate 1 must kill reads **only the atom 0**, never r/d with r≠0) PROVED. **New; this is the decisive NO-GO.**
- Thm 3.1 (Farey/Hecke lifts collapse by the cocycle to the log channel) PROVED.
- Thm 4.1 (atomic self-test = Smith gcd form: sign, but Λ-free) PROVED. **New.**
- Thm 5.1 (Riesz collapse: linear tests ⟹ Sonin range (4.2); quadratic tests ⟹ c_F-level, F2-blind) PROVED.
- Correction to R162_1001 §5 (non-band-limited ≠ T=∞ data; separable tests escape Theorem M) PROVED.
Gate 1 OPEN. No label moves.

## 0. Corpus check

Grep "torsion", "Li_s", "polylog", "Smith", "gcd matrix", "lcm", "Farey", "δ^{(2m)}" in phases 150–162: only R162_1001
(torsion, cocycle). The log-port representation (Thm 2.1) is R162_402 (e) read on the circle; the Farey lift is the
R162_401 log channel; the Smith form is new to the corpus. The trivial-zero identity Li_{−n}(w)+(−1)^nLi_{−n}(1/w)=0 is
classical (CITED: Lewin, *Polylogarithms*, §7.1; elementary: Li_{−n} is rational in w with this inversion symmetry).

## 1. Failing lines, stated first

| model | object (Φ_a, cocycle) | use step (Thms 2.1–5.1) | where |
|---|---|---|---|
| Λχ₂ | cocycle fails at p=2 (R162_1001 Thm 3.1b) | Thm 2.1 holds verbatim with −L'/L; lattice shifts to the trivial zeros of L(s,χ); Thm 2.2 holds (same Li inversion, parity χ(−1)) | §2 |
| Beurling | Φ_{Λ_B} undefined on ℝ/ℤ | the port H_+ = −(ζ_B'/ζ_B)K_F − Q_+ exists without the circle; Gate-1 content (the pole) is carried by atom 0 = the identity, which every group has | §2.3 |
| DH | a*1 ≠ log, cocycle fails at some p | Thm 2.1 holds for a = coefficients of −L'/L (a(1)=0); DH has first contacts with R_LF≠0 (R162_102), so the pole survives: the route cannot close there — consistent | §2 |
| deletion Λ1_{n≥5}, κ | cocycle fails at p∈{2,3} | defect D_p := ℒ_pΦ_a − Φ_a − log p(δ_0−Leb) is F-free; paired with F-tests it is the Ward defect B_a of R162_204/205 (linear, sign-flipping, zero at Λ) | §3.2 |
| ζ | nothing fails | the separating atoms r/d (r≠0) enter only the regular part; the pole is atom 0 (Thm 2.2) | §2.2 |

So the separating information of Φ_Λ (Thm 3.1 of R162_1001) and the Gate-1 information (the residue at −2m) live on
**disjoint sets of atoms**. That is the NO-GO in one line.

## 2. The log-port test

**Thm 1.1 (duality).** Let g ∈ 𝒟′(ℝ/ℤ) be even with Σ_k (a*1)(|k|)ĝ(k) absolutely (or Abel) summable. Put
u_g(d) := Σ_{j≠0} ĝ(dj) = ⟨ν_d, g⟩ − ĝ(0)... (precisely ⟨ν_d − Leb, g⟩). Then ⟨Φ_a, g⟩ = Σ_{d≥2} a(d)u_g(d), and
u ↦ ĝ, ĝ(k) = ½Σ_{j≥1}μ(j)u(|k|j), is inverse on sequences with Σ|u(n)|n^ε<∞. Hence a test "reads torsion atoms
beyond X" iff u_g is not supported in [1,X]; singularity of g at rationals is the same statement on the circle side.
*Proof.* R162_1001 Prop 3.2 with finite support dropped; Möbius inversion converges absolutely under the decay. ∎

So "reading the atoms" is not a new source of information: it is the choice of an infinitely supported weight u.
The only question is which u can be built from F.

**Thm 2.1 (log port as torsion pairing).** For Re s>1 let g_s(x) := ζ(s)^{-1}Σ_{k≠0}|k|^{-s}e(kx) =
ζ(s)^{-1}[Li_s(e(x))+Li_s(e(−x))]. Then u_{g_s}(d) = 2d^{-s}, ⟨Φ_a, g_s⟩ = 2Σ a(d)d^{-s}, and for a=Λ
    H_+(z) + Q_+(z) = ½ K_F(z) ⟨Φ_Λ, g_{½+z}⟩   (Re z>½),                                       (2.1)
extended meromorphically. g_s is not band-limited and is singular at x=0 (Re s≤1); its values at r/d are
Hurwitz combinations, so ⟨ν_d, g_s⟩ = (1/d)Σ_r g_s(r/d) reads every torsion atom.
*Proof.* ĝ_s(k)=|k|^{-s}/ζ(s); Σ_{j≠0}ĝ_s(dj) = 2d^{-s}ζ(s)/ζ(s). Then Thm 1.1 and −ζ'/ζ = ΣΛ(n)n^{-s}. ∎

This is the concrete answer to the task: the Hardy-space port of R162_201/402 *is* the pairing of Φ_Λ with an
F-independent, rational-singular kernel times the finite-T scalar K_F(z). By R162_402 (1.1),
    Gate 1 ⟺ z ↦ K_F(z)⟨Φ_Λ, g_{½+z}⟩ is regular at z = −a_m (s = −2m), m ≤ L.                  (2.2)

**Thm 2.2 (atom localisation; PROVED).** Near s = −2m (m≥1),
    g_s = (s+2m)^{-1}·(ζ'(−2m))^{-1}(−1)^m(2π)^{-2m} δ_0^{(2m)} + g_m^{reg} + O(s+2m),
where g_m^{reg}(x) = ∂_s[Li_s(e(x))+Li_s(e(−x))]_{s=−2m}/ζ'(−2m) is real-analytic on ℝ/ℤ∖{0}. In particular the
polar coefficient is a distribution **supported at the single point 0**, and the pole in (2.2) is
    Res_{s=−2m}⟨Φ_Λ, g_s⟩ = (regularised) Σ_d Λ(d)·⟨ν_d − Leb, c δ_0^{(2m)}⟩ = Σ_d Λ(d)·(mass of ν_d at 0 = 1/d)·c·δ^{(2m)}(0),
i.e. only the identity atom of each ν_d contributes (its zeta-regularised sum is the residue −1 of −ζ'/ζ... times
the normalisation, reproducing Res H_+ = −εK_F(a_m), R162_402 (e)).
*Proof.* The numerator N_s(x)=Σ_{k≠0}|k|^{-s}e(kx) is entire in s as a distribution. At s=−2m, for x∉ℤ,
N_{−2m}(x) = Li_{−2m}(w)+Li_{−2m}(1/w) = 0 (inversion with n=2m even, w=e(x)≠1); globally
N_{−2m} = Σ_{k∈ℤ}k^{2m}e(kx) = (2πi)^{−2m}δ_0^{(2m)} (differentiate Σe(kx)=δ_0). Since ζ has a simple zero at −2m,
g_s = N_s/ζ(s) has polar part N_{−2m}/(ζ'(−2m)(s+2m)) and regular part ∂_sN_s|_{−2m}/ζ'(−2m) (+ the ζ'' term times
N_{−2m}, again supported at 0). Off 0, ∂_sN_s is the derivative of an analytic family of analytic functions. ∎

**2.3 Consequence.** The atoms r/d with r≠0 — exactly those that do not exist for a Beurling system and that the
cocycle (3.1) uses to separate ℤ (the ring structure: index n = torsion order) — enter (2.2) only through g_m^{reg},
i.e. the finite part of H_+ at −a_m, which R162_402 (1.1) shows is irrelevant to Gate 1. The atom 0 is the identity
element; its contribution is the regularised Σ Λ(d)d^{2m}, a Dirichlet-series datum available verbatim for Beurling
(−ζ_B'/ζ_B), Λχ₂ and DH. The trivial-zero identity ζ(−2m)=0 ⟺ N_{−2m}|_{ℝ/ℤ∖0} = 0 is the circle form of the
R162_305 continuum-renormalisation cancellation: it wipes the rational atoms off the pole. **NO-GO for the lattice.**

Other points of the Gamma lattice or off-lattice analytic continuations of F̂: for s ∉ −2ℕ the kernel g_s is regular in
s and every atom is read, but (2.2) asks nothing there. Odd m (s=−2m−1): N_s is then the odd sum, orthogonal to the
even Φ_Λ — the parity mechanism of eq:residue, no new content.

## 3. Farey / Hecke / modular lifts of c_F

**Thm 3.1.** Let g_0 be any even test with ⟨Φ_Λ,g_0⟩ and S_0 := Σ_{k≠0}ĝ_0(k) = ⟨δ_0−Leb, g_0⟩ defined, u any
finitely supported weight (e.g. u = w_F), and g := Σ_e u(e)·(g_0∘×e) (Farey/Hecke lift; e.g. g_0 = B̄_2 gives the
Davenport–Bernoulli sum Σ_e w_F(e)B̄_2(ex), singular at all rationals of denominator ≤ X in its derivatives). Then
    ⟨Φ_Λ, g⟩ = Σ_e u(e)[ log e · S_0 + ⟨Φ_Λ, g_0⟩ ].                                          (3.1)
*Proof.* (g_0∘×e)^ = ℒ_e^*: ⟨Φ_Λ, g_0∘×e⟩ = ⟨ℒ_eΦ_Λ, g_0⟩; iterate (3.1) of R162_1001 along the prime factorisation
of e (the cocycle is additive: ℒ_{pq}Φ−Φ = (ℒ_p−1)ℒ_qΦ + (ℒ_q−1)Φ, and ℒ_q fixes δ_0−Leb). ∎

So every modular/Farey transform reads Λ only through Λ*1 = log, i.e. the log-weighted channel Σ u(e) log e, which
R162_401 cancels by [X,S_N] = −K_N; and ⟨Φ_Λ,g_0⟩ is an F-free constant. Using the cocycle for **all** p here is
exactly what makes the Λ-dependence disappear.

**3.2 Non-Λ data.** For a ≠ Λ, (3.1) acquires Σ_e u(e)⟨D_e, g_0⟩ with the F-free defect distribution D_e (Thm 3.1b of
R162_1001). It is linear in u, vanishes at Λ, and under u = w_F is the Ward defect B_a = DS(a*1−log) of R162_204 —
F2 and "F3 inverted" (the datum cancels at ζ), as in R162_205.

**3.3 The cocycle is tautological on every test.** For every g in the class of Thm 1.1,
⟨ℒ_pΦ_Λ − Φ_Λ − log p(δ_0−Leb), g⟩ = 0 is an identity in g. Therefore the family "cocycle ∀p" imposes no condition
on F whatever test is built from F; by R162_1001 Thm 3.1b it is equivalent to Φ̂_Λ(k)=log|k|, i.e. to a list of
F-free numbers. Non-perturbatively, all F-information must come from λ=0.

## 4. The atomic self-test (Smith form)

Take the most singular F-built test: g = Φ_{w_F} = Σ_{e≤X} w_F(e)(ν_e − Leb) (atoms at every rational of
denominator ≤ X; ĝ = w_F*1, not band-limited). Atom collisions: ν_d and ν_e share the gcd(d,e)-torsion, so with
Abel regularisation ⟨ν_d−Leb, ν_e−Leb⟩_s := Σ_{k≠0, lcm|k}|k|^{-s} = 2lcm(d,e)^{-s}ζ(s), whose polar part at s=1 is
2/lcm(d,e) = 2gcd(d,e)/(de).

**Thm 4.1.** (a) Res_{s=1}⟨Φ_u,Φ_v⟩_s = 2Σ_{c≥1}φ(c)(Σ_{c|d}u(d)/d)(Σ_{c|e}v(e)/e) (Smith: gcd = Σ_{c|(d,e)}φ(c)).
Hence the atomic self-form u ↦ Res⟨Φ_u,Φ_u⟩ is **positive semidefinite**, a genuine atom-collision sign.
(b) For u = w_F it is a quadratic form in c_F with no Λ in it; for (u,v) = (Λ, w_F) the inner sum Σ_{c|d}Λ(d)/d
diverges for every c, and the Abel-regularised value is −ζ'(s)W_F(s) − ζ(s)W_F'(s) (W_F(s) = Σw_F(d)d^{-s}), which by
(3.1) is again the log channel. Cauchy–Schwarz with ⟨Φ_Λ,Φ_Λ⟩ = ∞ gives nothing.
*Proof.* (a) expand gcd and interchange (finite sums). (b) direct; the divergence is Σ_{p^k≡0 (c)} log p/p^k over
all primes. ∎

The Smith sign is the only positivity produced by torsion atoms in this memo; it is Λ-free (fails F3 as a closing
tool) and depends on F only through c_F (F2-blind).

## 5. Riesz collapse and Theorem M

**Thm 5.1 (Riesz collapse).** (i) If F ↦ g_F is linear and continuous from L²(I_{T_*}) into the class of Thm 1.1, there
is ψ ∈ L²(I_{T_*}) with ⟨Φ_Λ, g_F⟩ = ⟨F, ψ⟩ for all F. The conclusion "⟨Φ_Λ,g_F⟩=0 for every first-contact F" is
equivalent to ψ ∈ (ker H_{T_*})^⊥ = closure ran H_{T_*}; for (2.2), ψ = e^{a_m t}1_{I_{T_*}} (up to the Q_+ history
term), i.e. the Sonin range question R161_011 (4.2). (ii) If g_F is quadratic (built from c_F, w_F, Φ_{w_F}), the pairing
is ⟨F,ΨF⟩ and any conclusion from λ=0 needs an operator inequality Ψ ≼ C·H_{T_*} on I_{T_*}; since Ψ depends on F only
through c_F, it is invariant under F ↦ −F and under the (PC) orientation A_M → −A_M (F2).
*Proof.* Riesz representation; ker of a self-adjoint Fredholm-type H is ran^⊥. (ii) R162_1001 §6. ∎

Thus λ = 0 enters non-perturbatively only as H_{T_*}F = 0 — a band-limited (window) linear system — and the torsion
kernel enters H_{T_*} only through Φ̂_Λ(k)=log k, k ≤ X (R162_1001 Thm 5.1). No combination of the cocycle for all p
with λ = 0 produces K_F(a_m)=0 or a contradiction beyond the range statement.

**Theorem M (correction to R162_1001 §5).** R162_1001 claims every non-band-limited use is a T→∞ limit and dies by
Theorem M. False as stated: the tests of §2–4 are *separable* — an F-free infinite-degree kernel (g_s, g_0, ν_e) times
finitely many finite-T functionals of F (K_F(z), w_F(e), e ≤ X). They are exact at T_*, involve no window limit, and
Theorem M (a statement about margins of window forms as T→∞) does not apply. The construction does not die by M;
it dies by Thm 2.2 (lattice pole reads only atom 0) and Thm 5.1 (range restatement). Non-separable tests (F-data
beyond X) do require T→∞ and fall under M as R162_1001 says.

## 6. F1, F2, F3, F4

- **F1.** Thms 1.1–4.1 hold for every F (λ>0 eigenvectors included). Thm 5.1 uses λ=0 exactly, and reduces to the
  range statement — E1 (Gate 1 restated), not a falsehood. F1 passed only by restatement.
- **F2.** Linear tests: orientation enters only via the causal history Q_+, which Thm 2.2 does not touch (it is killed
  by ζ(−2m)=0, R162_402). Quadratic tests: c_F-level, blind. F2 not passed.
- **F3.** Passed at the object (Φ_Λ, cocycle); failed at the use: the Gate-1 pole is carried by atom 0, identical for
  Beurling/Λχ₂/DH Dirichlet data (Thm 2.2, §2.3); lifts reduce to log (Thm 3.1); Smith sign Λ-free (Thm 4.1).
- **F4.** No graph limit taken; n/a.

## 7. Verdict and residual

**NO-GO (PROVED).** A non-band-limited, rational-singular test from F at finite T_* exists and is natural: the log
port H_+ is ½K_F·⟨Φ_Λ, g_{½+z}⟩ (Thm 2.1), so the Gate-1 residue *is* a torsion pairing. But at the Gamma lattice the
trivial-zero inversion Li_{−2m}(w)+Li_{−2m}(1/w)=0 collapses the polar part of the kernel onto δ_0^{(2m)}: the pole
reads only the identity atom, which carries no ℤ-vs-Beurling or 1-vs-χ₂ information; the separating atoms r/d
(r≠0) sit in the regular part, which Gate 1 does not need (Thm 2.2). The cocycle for all p is tautological on every
test (§3.3) and turns Farey/modular lifts into the log channel (Thm 3.1). The only atom-generated sign (Smith gcd form,
Thm 4.1) is Λ-free. λ=0 enters as H_{T_*}F=0, and every linear torsion test reduces to the Sonin range (4.2) (Thm 5.1).
Theorem M does not kill separable tests; Thm 2.2 does.

**Residual (sharp).** A closing torsion argument must move Gate-1 information off the identity atom: a kernel whose
polar part at s = −2m is not supported at 0, i.e. a test not of the form (F-free kernel)×K_F(z) — equivalently a
first-contact–dependent kernel g_{F,s} whose s-dependence is not through ζ(s)^{-1}. No such kernel is known; by
Thm 5.1(i) any linear one is again the range question.

Add to R162_590 §1c: "torsion-atom tests (log port, Farey lift, Smith self-test) — R162_1101 — pole at Gamma lattice
reads only atom 0 (Li inversion = trivial-zero cancellation); cocycle tautological on tests; Riesz collapse to (4.2);
separable tests escape M | F2, F3 (at use), E1".

Files edited: this file only.
