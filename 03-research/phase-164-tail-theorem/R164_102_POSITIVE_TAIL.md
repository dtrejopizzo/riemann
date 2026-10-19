# R164_102 — Line L1, questions 2(c) and 3: the non-linear content of a positive tail measure

**Status:** round 1 of L1. No claim of RH or of (★_cell). Pure mathematics, no numerics.
Sources read: R164_000 §0–1, R163_801 Thm 3 / Cor 3.1, R163_101 (Prop 1, Lemma R), R162_2901 (Thms A, B).
Corpus grep "Bernstein / completely monotone / Landau": the only prior uses are R163_701 (sub-Landau zero-free region,
a σ > 1 – side statement) and phase 33 (Li / Nyman–Beurling); none applies Pringsheim–Landau to a *tail* factor. So
Theorem L below is new to the record, but it is a classical one-line argument.

Notation. L = log X = 2T_c. μ_ζ = Σ_n (Λ(n)/log n) δ_{log n}. A *tail system* is ζ_B = ζ·E with
log E(s) = ∫_{(L,∞)} e^{-su} dν(u), ν a real measure, and μ_B = μ_ζ + ν ≥ 0 (Beurling positivity of the tail).
So ν = ν₊ − ν₋, ν₋ ≤ μ_ζ|_{(L,∞)} (negative part sits on prime powers > X, with mass ≤ 1/k at log p^k).

## 0. Status table

| Item | Statement | Label |
|---|---|---|
| Thm L | (Landau–Pringsheim for the tail factor) If ν ≥ 0 and E is meromorphic on ℂ, then E ≠ 0 on Re s > σ_c(ν) and σ_c(ν) is a real pole of E; if E has no real pole, E has no zeros at all. | PROVED |
| Cor L.1 | A *pure addition* above X (ν ≥ 0) that creates no new pole creates no zero. Off-line zeros in a positive-tail system require either a new real pole or a deletion ν₋ ≠ 0 above X. | PROVED |
| Thm A | (no-FE class) For every β∈(½,1), γ>0, L>0 there is ζ_B = ζ·E with ν = r(u)du, r > 0 on (L,∞), and a zero at β+iγ (so anywhere, in particular inside any light cone of the witness). The price is a double real pole at s = 1. | PROVED |
| Cor A.1 | Candidates (a) complete monotonicity/Bernstein, (b) Jensen/Landau/positive-definiteness, read on Z_X alone, are DEAD: Thm A's E satisfies all of them. | PROVED |
| Thm H | (FE class, finite modification) If ζ_B has the completed FE of ζ, Γ_ℝ(s), the same polar data (simple pole at 1 only), finite order, and ζ_B/ζ has finitely many zeros and poles, then ζ_B = ζ. | PROVED |
| Prop I | (FE class, integer support) If moreover μ_B is supported on {log n}, ζ_B = ζ. | PROVED-CITED (Hamburger 1921) |
| Prop W | Same window data + same arch + same polar ⟺ zero measure of ζ_B agrees with ζ's on all tests in 𝒟_{T_c}; hence the witness F of ζ is a witness of ζ_B. | PROVED (Weil formula; witness transfer ARGUED as in R163_801 Lemma 3.0) |
| (c) | The residue identity of R163_801 Thm 3 plus μ_X ≥ 0 plus W(F)=0 gives no constraint on G(t_q)² beyond the tautology Res = −G(t_q)²·mult. | ARGUED (§4) |
| Central test, literal class (Dirichlet data below X + μ_X ≥ 0) | YES, members with off-line zeros in any cone exist (Thm A). L1 as a statement about Z_X alone: **DEAD**. | PROVED |
| Central test, witness class (also same Γ, FE, polar data) | Reduced to: an infinite zero modification paid by a deletion ν₋ ≤ μ_ζ above X. No member constructed, no obstruction proved. | **OPEN** |

**Verdict.** L1 in the form "a non-linear property of μ_X ≥ 0 read on Z_X" is DEAD (falsifier: Thm A). What survives is
exactly one non-linear fact, Thm L, which is not a sign statement on zeros but a *bookkeeping* statement: positive mass
added above X can only produce real poles; zeros must be paid for by removing Euler mass above X. Combined with Thm H/Prop I
the witness-class question collapses to Hamburger (identification) for integer support and to OPEN for Beurling support.

## 1. Theorem L (Landau–Pringsheim for the tail). PROVED

Let ν ≥ 0 on (L,∞) with abscissa σ_c ∈ [−∞,∞) and suppose E := exp(∫e^{-su}dν) continues meromorphically to ℂ.

*Proof.* For σ > σ_c, E(σ+it) = exp(Λ(σ+it)) with Λ the Laplace transform; E ≠ 0 there. By Landau's theorem for Laplace
transforms of positive measures, Λ is singular at s = σ_c (if finite). On the real ray σ↓σ_c, Λ(σ) is increasing,
so log E(σ) ↑ ℓ ∈ (−∞, +∞]. If E were holomorphic and nonzero at σ_c, Λ = log E would be analytic there: contradiction.
If E had a zero at σ_c, log E(σ) → −∞: contradiction with monotonicity. Hence σ_c is a pole of E. If σ_c = −∞, Λ is entire
and E = e^Λ has no zeros. If σ_c > −∞, E ≠ 0 on Re s > σ_c and E has a real pole at σ_c; zeros can lie only in
Re s ≤ σ_c. In particular, if E has no real pole then σ_c = −∞ and E has no zeros (Cor L.1). ∎

**Cor L.1. PROVED.** If ν ≥ 0 and ζ_B = ζE has no pole other than the simple pole at 1 (so E is holomorphic and nonzero
at 1 and has no poles), then σ_c(ν) = −∞ and E has no zeros: ζ_B and ζ have the same zeros. (If E had a pole at σ_c=1
it would raise the pole order of ζ_B.) This is the non-linear content of positivity (it uses exp, not the linear
explicit formula): **positivity above X is sign-blind on zeros but polar-sensitive**. ∎

## 2. Theorem A (falsifier, literal class). PROVED

Fix ρ₀ = β+iγ, ½<β<1, and R(s) = (s−ρ₀)(s−ρ̄₀)/(s−1)². For Re s > 1,
log R(s) = ∫₀^∞ e^{-su} r(u) du, r(u) = (2e^{u} − 2e^{βu}cos γu)/u > 0 for u > 0.
Put E(s) := R(s)·exp(−∫₀^L e^{-su} r(u)du) (the subtracted term is entire). Then log E = ∫_L^∞ e^{-su} r(u)du with
r > 0, ζ_B = ζE has μ_B = μ_ζ on (0,L], μ_B ≥ 0, and zeros at ρ₀, ρ̄₀. γ is free, so ρ₀ can be put in any light cone
{|γ − x₀| < δ} of R163_401 Lemma 3.4, with any δ = β − ½. ∎

Consistent with Thm L: the zeros are paid by the double real pole at 1 (σ_c(ν) = 1). Also the entire factor exp(−∫₀^L…)
changes the archimedean functional, so ζ's witness F is *not* a witness of ζ_B; Thm A kills every statement that uses
only (P_X, μ_X ≥ 0) and **not** the arch/polar data — in particular (a) and (b):

**Cor A.1. PROVED.** For ζ_B: Z_X^B(σ) is completely monotone in σ > 1 (Bernstein: log Z_X^B is the Laplace transform of a
positive measure, hence Z_X^B too); t ↦ Z_X^B(σ+it)/Z_X^B(σ) is positive-definite (characteristic function) for σ > 1;
|Z_X^B(σ+it)| ≤ Z_X^B(σ); Jensen/Landau inequalities for exp of positive series hold. None of these continues past
σ_c = 1 (Landau's real singularity), and ζ_B has an off-line zero. So no property of type (a)/(b) reaches the strip. ∎

Remark on the cone geometry (b). The sign condition Re G(γ−iδ)² < 0 ⟺ phase of G(γ−iδ) ∈ (π/4,3π/4) depends only on F
(window) and on the location of the zero. Since Thm A places zeros anywhere, any argument of type "positive tail ⟹ phase
outside (π/4,3π/4)" would have to use the polar/arch data, which is exactly what Thm A changes. DEAD as tail-only.

## 3. The witness class: FE + Γ_ℝ + same polar data

**Prop W. PROVED.** If ζ_B has ζ's Γ-factor, FE and polar data, and μ_B = μ_ζ on (0,L], then for every h with
supp ĥ ⊂ (−L,L) Weil's formula gives Σ_{ρ_B} h = Σ_{ρ_ζ} h. Thus W_{T_c}^B = W_{T_c}^ζ on 𝒟_{T_c}, the first contact and
the witness coincide (transfer to the closure 𝒟_T: ARGUED, R163_801 Lemma 3.0 type). So the honest central test is in this class.

**Thm H. PROVED.** Let Q = ζ_B/ζ. Q = exp(∫_L^∞ e^{-su}dν) is bounded and → 1 as σ → +∞ uniformly in t (|ν| e^{-λσ}
summable for σ ≥ 1+ε since μ_B and μ_ζ both converge there, and ≤ e^{-(σ−1−ε)L}·C). By the FE (same completion),
Q(s) = Q(1−s), so Q → 1 as σ → −∞ too. If Q has finitely many zeros/poles, multiply by the polynomial P of its poles:
PQ is entire of finite order, polynomially bounded on σ ≥ 1+ε and σ ≤ −ε, hence (Phragmén–Lindelöf in the strip) a
polynomial; Q is rational with Q = 1 + O(e^{-Lσ}), hence Q ≡ 1. ∎

So in the witness class an off-line member must move **infinitely many** zeros; no finite (Lemma-R-type, R163_101) or
"M_m-type with finitely many quadruples" modification exists *with window data equal to ζ's*. (M_m itself has finitely many
extra quadruples but different window data: R163_801 Thm 5, consistent with Thm H.)

**Prop I. PROVED-CITED (Hamburger).** If μ_B is supported on {log n} (integer Dirichlet series), FE + Γ_ℝ + simple pole
force ζ_B = ζ. So with prime-power support and multiplicativity the class is {ζ}: L1 becomes an identification, W3/Thm O
territory (R163_1001), not a mechanism. Beurling support (real frequencies) is the only non-trivial case.

**Reduction (PROVED from Thm L, Thm H).** A witness-class member with an off-line zero needs ν₋ ≠ 0 (by Cor L.1, since no
new poles are allowed), ν₋ ≤ μ_ζ on prime powers > X, and infinitely many zero displacements. Partial deletions of the
form ∏_{p∈P'}(1−c_p p^{-s}), 0<c_p≤1, have zeros only on Re s ≤ 0 (outside the strip, PROVED: each factor's zeros satisfy
p^{-σ} = 1/c_p ≥ 1); Chebotarev-type deletions give branch points (non-meromorphic, ARGUED). Whether a positive Beurling
system with ζ's window, Γ, FE, polar data and an off-line zero exists: **OPEN (O164.102.1)**. This is a Beurling–Hamburger
problem (FE-rigidity for Beurling frequencies), adjacent to L2 (R164_000 §2) and to Fourier-quasicrystal Dirichlet series.

## 4. Question (c): residues at off-line poles. ARGUED (negative)

In (3.1), at an off-line zero ordinate t_q, the residue of −iG²𝒯_X is −G(t_q)²·mult(q), a tautology (Cor 3.1(a)).
μ_X ≥ 0 makes x ↦ 𝒯_X(iy), y > ½, completely monotone in y and makes 𝒯_X(x+iy) a positive-definite function of x for each
y > ½ (as Fourier–Stieltjes transform of e^{-(½+y)u}dΛ_X). Both are statements on Im x > ½ only; Landau puts the first
singularity of the ray at y = ½ (the pole, cancelled by C_T), and the off-line poles sit behind it. Neither the witness
condition W(F) = 0 (an equality on the band, where 𝒯_X drops out: Cor 3.1(b)) nor positivity links the band to the
residues; Thm A exhibits positive tails with arbitrary residues once polar data are free, and in the witness class the
residues are those of ζ's own zeros (Prop W), so (c) restates (TC). No constraint found.

## 5. Mandatory falsifiers

| System | Positive tail? | Same window as ζ? | Same Γ/FE/polar? | Off-line zeros? | What it kills |
|---|---|---|---|---|---|
| Λχ₂ (a(n)=Λ(n)χ₂(n), χ₂ real quadratic; Paper 48 tab:falsifiers) | **no**: mixed signs (χ₂(p)=±1 on primes > X) | no | conductor q, Γ_ℝ(s+κ) | per GRH-type status of L(s,χ₂); as a falsifier it sits outside the positive-tail class | positivity of μ_X already separates it; it cannot test any statement of this file, which only concerns positive tails (the Thm L / Cor A.1 conclusions are vacuous for it) |
| deletion Λ·1_{n≥5} | yes | no | no FE | zeros on Re s=0 only | any tail-only statement must use the window; illustrates §3 deletion zeros at Re s ≤ 0 |
| ζ_θ (Broucke) | yes (dΠ ≥ 0) | no | no Γ_ℝ FE | yes, Re s=(1+θ)/2 | positivity alone ⟹ nothing (R162_2901, R163_101) |
| Thm A ζ·E | yes | **yes** | no (double pole, new arch term) | yes, anywhere | (a), (b), tail-only L1 |
| f_t (R163_901) | **no, generically** (ARGUED, §5 note) | yes | yes | yes | positivity separates f_t; O164.102.1 not closed by f_t |
| f_χ (R163_1001) | no (−f_χ′/f_χ has mixed-sign coefficients) | no | conductor q | yes | positivity is a real separator from f_χ |
| M_m (R163_801 Thm 5) | depends on m (density β_m sign-changing in window) | no | yes | yes | Thm H consistent: finite change ⟹ window must differ |
| Λ̃ | not positive | — | — | — | excluded by positivity |

**Note on f_t (settles O164.102.2 at ARGUED level).** log f_t = log ζ + log(1+t g/ζ), so above X the tail measure is μ_ζ + ν_t with ν_t the Dirichlet measure of log(1+tg/ζ) = Σ_k (−1)^{k+1}(tg/ζ)^k/k. ν_t is not supported on prime powers and has oscillating coefficients (g/ζ = g·Σμ(n)n^{-s}); at n > X that are not prime powers μ_ζ has no mass, so any negative coefficient of ν_t there makes μ_X fail to be ≥ 0. Generically (t ≠ 0, g not specially tuned) such n exist: ARGUED, not PROVED (no coefficient computed).

## 6. Grid cells

- **4F (Euler product × global transforms in T):** tail-only positivity DEAD (Thm A). Surviving content: Thm L (positive
  addition ⟹ only real poles), Thm H (finite modification impossible with fixed window/FE/polar), Prop I (integer
  support ⟹ identification). Residual O164.102.1 (Beurling–Hamburger with positive tail).
- **7F (tail through zeros):** (c) DEAD as a constraint (tautological residue, §4).

## 7. Walls

- W-Landau: every positivity property of μ_X lives on σ > σ_c and is stopped by Landau's real singularity at s = 1; it reaches
  the strip only through meromorphic bookkeeping (Thm L), never as an inequality.
- W-polar: off-line zeros in positive-tail systems are paid either by polar data (Thm A) or by deletions; the witness fixes
  polar data, so only deletions remain — a statement about Euler mass removed above X, not about signs.
- W-identification: with integer support, the witness class is {ζ} (Hamburger) — closes nothing (Thm O pattern).

## 8. Ledger

| Id | Content | Label |
|---|---|---|
| R164_102.L | Thm L, Cor L.1 | PROVED |
| R164_102.A | Thm A, Cor A.1 | PROVED |
| R164_102.W | Prop W | PROVED (transfer ARGUED) |
| R164_102.H | Thm H | PROVED (finite order assumed, as for every system in the record) |
| R164_102.I | Prop I | PROVED-CITED (Hamburger) |
| R164_102.c | (c) gives no constraint | ARGUED |
| O164.102.1 | positive Beurling system with ζ's window, Γ_ℝ FE, simple pole, off-line zero in a cone | OPEN |
| O164.102.2 | tail of −f_t′/f_t above X has mixed sign generically (§5 note) | ARGUED |
| Decision | L1 as "non-linear property of μ_X ≥ 0 on Z_X": DEAD; L1 survives only as O164.102.1 | PROVED / OPEN |
