# Synthesis of the O1 rounds

**Current status:** full goal D active. The final section «Rounds 005–007»
collects the most recent results; the previous rounds remain as history.

2026-10-18. Row D independent. Integration document, without modification
of Paper 46. Final review favourable: AUDIT_001 §8.

## What changed in the assignment

The original question «two-variable K positive and failing when a
prime is deleted» was replaced by a gated test: effective domain; precise
exit from SOS/PD; actual translation to BR, if it exists; independent sign;
failure of a premise or of the link under the relevant falsifiers; link
with Q_T only at the end. The sign of the candidate need not itself fail
under every elimination. A specific identity may be the step
that avoids the transfer, but its proof must contribute content.

## Results and limits

- CONTROL_001: the projection P_T M_a P_T creates a two-variable kernel
  without changing the form on the image of P_T. PROVED and independent review favourable.
- AUDIT_001: thm:sos is not a prohibition of every norm identity.
  Its class is distinguished from def:PD and from the abstract collapse B*B.
- AUDIT_001: the kernel of P36-4, the operator K(t,t′) and the relaxed set W₂ of
  BR are different objects. No wall is transferred by notation.
- The examination of the ansatz J+compact correction is recorded in CONSTRUCTOR_001
  and was accepted by the final review (AUDIT_001 §8). It refers to positivity on a full interval
  of heights or on an explicit dense linear ideal; not to the arithmetic domain
  Euler+FE nor to the global node with its tails.

No kernel with its own sign and a useful arithmetic link has been constructed.
The round does NOT prove nonexistence of the O1 object.

## What continuing after the compact control would mean

Within the ansatz J+K and with positivity on the full space of heights,
a correction would have to escape the compact class. This does not impose non-
compactness on every possible O1 mechanism: another domain or another form of
positivity requires another analysis.

For example, I+J is already positive and non-compact on that space. That only
illustrates that leaving the compact class is not enough: it is a generic positivity,
without arithmetic specificity. The next round needs an explicit
candidate before adding another necessary condition to the catalogue.

**Balance:** improved assignment and first attempt executed; no source of
sign, no closure of the node and no change of status of O1 or of row D.

## Second round — auxiliary positive result with strict sign

The subsequent plan was to continue until a positive result.
C_y was constructed as a divisibility covariance under the discrete Gaussian
without origin, with τ=θ−1. Its generic PSD was not counted as progress. The subsequent
computation produced these additional signs, accepted in AUDIT_003:

1. **Punctured geometric concavity:** (d/dx)²logτ(e^x)<0 for all x.
   Elementary proof with Poisson and uniform rational bounds; it does not depend on
   zeros. No bibliographic priority is claimed.
2. **Strict anticorrelation:** for coprime d,e>1,
   Cov_y(1_{d|N},1_{e|N})<0 for ALL y>0. It is not the automatic PSD of a
   covariance; it determines the sign of its cross interaction.
3. **Prime factors:** Cov_y(v_p,v_q)<0 for p≠q, and
   Var_y(log|N|)<Σ_p(log p)²Var_y(v_p), with proved absolute convergence.
4. For pairwise coprime FINITE families, the matrix C_y is positive
   definite, has negative cross entries and its inverse is positive
   entrywise. That structure is not attributed to the node.

### Critical coprime step

If B_y(d,e)=τ(y)C_y(d,e), the divergent term of B_y at zero is
G₀(d,e)y^(-1/2), G₀=(gcd(d,e)−1)/(de). For coprime indices G₀=0 exactly.
One obtains directly, for α>0,

    A_α(d,e)=−∫₀∞y^(α−1)B_y(d,e)dy >0.

At α=1/4 no COPRIME counterterm is needed. B keeps the quotient
τ(d²y)τ(e²y)/τ(y); denormalising the outer factor does not remove it.
The joint difference converges; do not split its two divergent integrals
without the corresponding continuation.

CONSTRUCTOR_004 and AUDIT_004 further develop the non-exclusive dependence
on the product of the indices and the Mellin extension to all powers of
TWO distinct primes. This does not authorise summing over all primes at the critical
weight without a uniform estimate.

### What was achieved and what was not

A **genuine partial positive result** was achieved: a signed cross
interaction, valid at all scales, whose coprime Mellin transform keeps the sign
at α=1/4 without subtraction. The global PSD form that would close O1 was not constructed.
Positivity of entries is not positivity of the form; the diagonal and same
prime, the exact link with Q_T, the identification of the polar term and control of all
tests/modes are missing. α=1/4 by itself does not verify the weight law of the node.
The anticorrelation could be inherited by an incomplete Euler product: the complete
specificity required of the final mechanism was not proved.

The first round left negative controls; the second leaves this sign
lemma and an explicit object. The node and D remain OPEN. No
closure was written in Paper 46 and no cells of the grid were repainted.

Final review of the second round: AUDIT_003 and AUDIT_004 favourable; no
pending objections. The positive milestone achieved is auxiliary and signed,
not the major milestone of the O1 kernel with complete link.

## Rounds 005–007 — auxiliary completion and functional link

**CONSTRUCTOR_005 / AUDIT_005: PROVED.** The whole canonical kernel −Rα
is SPD on finite coefficients of distinct divisors ≥2:

    −Rα(A)=κ E_s|A−μ₁(A)|²+∫y^{α−1}τ|E_yA−μ₁(A)|²dy,
    s=2α∈(0,1), κ=−2π^{−α}Γ(α)ζ(2α)>0.

The diagonal of R and the same-prime blocks ARE ALREADY paid for that
object. No favourable diagonal was assigned nor was positivity of Q assumed.
No normalisable ζ law at s<1 was used: P_s lives on finitely many valuations.
Positivity is inherited under finite deletion; it is not specific by itself.

**CONSTRUCTOR_006 / AUDIT_006: PROVED.** With m=y^{−1/2}−τ,
0<m<1 and m(y)=y^{−1/2}m(1/y), the FE of Π transforms α into 1/2−α,
with explicit fractional dilations and the same parameter at 1/4.
For a deleted law, the dual profile m_P^∨ differs from m_P by an explicit
nonzero Δ_P. That single-profile identity does fail under deletion;
it has not yet been proved that it contributes the sign of Q. No
non-Hankel property at fixed α is attributed to Π merely by writing two scales.

**CONSTRUCTOR_007:** in the Haar-centred kernel of the completion of −R,
D_nA=1_{n|N}A(N/n) preserves the centring. V_n=n^{s/2}D_n is a semigroup
of contractions. The geometric factor is isometric and the norm defect
is exactly

    ∫u^{α−1}τ(u)[1−q_n(u/n²)]|E_uA|²du ≥(1−1/n)Π(A).

The computation of adjoints in the Gaussian factor does not transfer automatically
to the graph subspace. The monoid properties alone may be generic;
the FE and the integer interpretation must intervene in the concrete link.

**Goal D active.** Next step: realise the inversion of 006 in the
space of 007 and verify the form/trace it produces, with domain and
convergence. A trace is not taken as existing nor is its sign identified
with Q by similarity. That link, all modes/windows, tails and
the sectors/polar required by the declared carrier are missing.

## Round 008 — inversion defect verified

CONSTRUCTOR008/AUDIT008: in the Gaussian factor the inversion U satisfies
UGnU=M_bGn*, b²=r(y/n²)/r(y), r=τyτ1/y. b crosses 1 at y=n.
A simple conjugation with adjoint cannot be imported into the module.
The primorial sequence that seemed to produce a vertical component
converges only pointwise: its Gaussian norm diverges. Elementary arithmetic
proof; no Mertens nor new zero hypothesis.

Determining the closure and its invariance remains pending; the computation of 008
decides neither closability nor vertical components. The map to Q_T
was not constructed. Full goal D active.

## Round 009 — outcome of the direct proof of the link

LINK009/AUDIT009 discard a C0 semigroup interpolating n^beta V_n at log n
for any beta, also D_n. The proof uses a concrete vector of 007,
not a support argument nor zero information. A fixed unitary compression
of V_n is excluded; for D_n that second conclusion is not claimed.

Hence one cannot pass from the module to a continuous Mellin generator by
simple interpolation of its actions. Another realisation/map and the
identity with Q_T are missing. SCOPE_P44_009 separates this result from the overreach
of rem:nointerp about arbitrary weak* interpolation. Goal D active.


### Phase 209 — LINK010: regularity of a compression of D_n (2026-10-19)

LINK_010_SPECTRAL_REGULARITY computes, for each nonzero centred finite
observable A, increments with liminf ||D_mA−D_nA||²/log(m/n)^s>0,
s=2alpha, via n=1+kL, m=n+L outside the prime support of A.
Every realisation D_n=P U(log n)J with fixed bounded maps and C0 unitary U
requires INFINITE spectral moment s for JA: not in Dom(|B|^(s/2)).
At alpha 1/4, moment 1/2 and domain power 1/4. PROVED, independent
review favourable in AUDIT_010. It only excludes compressions with that
regularity; the general compression remains OPEN, as does the Q_T link.
The normalised compression 009 is not reopened and the status of D is not modified.


### Phase 209 — LINK011: first continuous map computed and cross-checked (2026-10-19)

LINK_011_MELLIN_GAUSS_MAP constructs UF=Σ a_d(F)(X_d−1/d), with
 a_d=2∫ e^(x/2)F(x)W_d(e^(2x))dx at alpha 1/4.
Convergence in H by a_d=O_T(||F||/d), Sdd=O(d^-s); compact operator,
C∞ feature and smooth effective kernel. FEcoef for even F recovers exactly
C(F)=∫Fcosh(x/2). Do not sum the separate polar vector: it diverges; cancel
coefficients first. The equality Q_T=||UF||² on the continuous carrier is
FALSE for THIS map: polar-corrected high-frequency tests have
Q_T~logλ and ||UF||→0. The domination Q_T≥||UF||² remains OPEN, as do other
non-smoothing maps. No general NO-GO for O1, nor proof of D. Review favourable in AUDIT_011.
Precision on 006: piece-by-piece G/Π/v correspondences are not required; a
TOTAL identity or domination on a dense core for the form norm suffices.


### Phase 209 — LINK012: domination 011 refuted by a certified test (2026-10-19)

LINK_012_DOMINATION_FALSIFIER keeps exactly the map U of 011 and
tests the inequality that had remained OPEN, without retrying the equality.
Explicit test T=4/5, ω=5π/8, r=3(ω²+1/4)/(9ω²+1/4),
F=(cos3ωx+r cosωx)/sqrt(T(1+r²)), even, H0¹ and EXACTLY polar-free.
Arb128 certification and analytic tails: Q(F)<.002351, while the positive
rank one of 005 gives ||UF||²≥κ|Σa_dv_d|²>.26134304. Remainder<−.25899.
Exact Laplace transform of the autocorrelation and the expansion K=2Σexp(−(2j+.5)u)
provide an independent check without gamma/comb quadrature:
Qupper<.001647953. Data/code in LINK012_data. Polar-corrected H1 approximation
extends the falsifier to the C_c∞ core. AUDIT_012 favourable, both scripts reproduced.
Only the EXACT scale of U011: no exclusion of small rescalings,
other maps/O1 nor D. This concrete domination is no longer an OPEN residue.
No P46 integration nor change of cells/counts. Full goal D active.


### Phase 209 — LINK013: every fixed scale of U011 fails for large windows (2026-10-19)

New written difference from 012: it does not change U nor retry scale 1;
it computes the response of the same map on the EXPLICIT family of P46
lem:testfam as T→∞, and tests the previously open class of arbitrary constants.
The profile M(F)=∫Fh satisfies h(−∞)=−κ, h(+∞)=0, by Riemann sum and positive
Mellin transform of m=y^−1/2−τ. For G_T=ω_k(x/T), k=ceil21T/e, F_T=P(D)G_T,
the mass of G_T/T escapes compact sets, the L1 derivatives are o(T), and
M(F_T)/T→γ1²κ/8. Thus E_T≥κM²≥c0T². The proof of P46 thm:margin/cor:margin1
(CITED, inputs Z1/Z2 and explicit formula only for this falsifier) gives
|Q_T(F_T)|/||F_T||²≤4e9Texp(−15.449T) for THIS FAMILY, not by inferring
a test from an infimum. Norm F² O(T^1.5) => |Q|/E=O(√Texp(−15.449T))→0.
There is no fixed c>0 with Q_T≥cE_T in all windows. Any possible c(T)
requires c(T)≤C√Texp(−15.449T); its existence is not proved.
Analytic proof without new numerical computation; AUDIT_013 favourable, explicit CITED input.
No exclusion of other maps, nor new sign of D. No P46/cells/counts integration.


### Phase 209 — LINK014: removing positive pieces does not repair U011 either (2026-10-19)

Written difference: 013 discarded a LARGER form via κvv*; it did not imply
failure of subforms. Here each piece is tested directly with the SAME a_d 011.
For Π, the profile K_y(x)=2e^.5xΣWd(e2x)(qd(y)−1/d) is positive, L1 and
∫K_y=C(y)=κΣvd(1/d−qd)>0. Local CLT via Fourier for G_T and sup bounds on derivatives
=> B_FT(y)/√T→−γ1²g0 C(y)/4. Fatou on [1,2] gives EΠ(F_T)≳T.
For G_s, G(d,2)=(1−1/√2)d^−.5 1_even; profile h2 bounded with limits
−κ(1−1/√2)/2 and 0. Even Riemann sums + escaping mass give L2(F_T)≍T; Cauchy covariance
=> E_G(F_T)≳T². κvv* already gave ≳T² in 013. With the CITED Q(F_T) of the paper decreasing
exponentially, EVERY fixed non-negative nonzero combination AκG+Bκvv*+CΠ
with the SAME a_d 011 has |Q|/E→0. No positive uniform constant of domination.
No inferences from larger to smaller; new proof for both subforms.
No new numerics. AUDIT_014 and addendum favourable for the whole class.
Other maps, signed cancellations and T-dependent factors are not excluded.
Full goal D active/OPEN; no P46/cells/counts integration.


### Phase 209 — CONSTRUCTOR015: split domain and exact PSD cone (2026-10-19)

New difference from 008: small positive tilts over many large primes,
not the primorial whose Gaussian norm diverged. For H=Σp^-s→∞, t=H^-2/3,
Z_u=∏(1+tp^-u), A=∏(1+tXp)/Z_s−Z_1/Z_s is Haar-centred and satisfies
Es|A−1|²→0, ||TA||≤C(Z_r−1)/Z_s→0, r=(s+1)/2>s, by Πdd of 011.
This produces (√κ1,0)∈H. The bounded actions Dn of 007 generate pure Xd and give
H=L²(P_s)⊕V, V=closure TA0. T densely defined NOT closable, with
explicit sequence f2−(D2A_j−A_j/2)→0 arithmetically, image→q2−1/2≠0.
The 3 forms κG, κvv*, Π are energies of 3 genuine orthogonal projections.
The PSD cone in their REAL span over ALL of A0 is exactly a,b,c≥0.
With 014 it also closes globally PSD signed combinations of that span with the
SAME map 011. It does not classify forms positive only on its image nor other maps.
Ps is a product of valuations, NOT a zeta law on N. Not V=all Gaussian nor FE invariance.
No new numerics nor new zero input. AUDIT_015 favourable to the three theorems.
No sign of Q/D; full goal active, no P46/cells/counts integration.


### Phase 209 — LINK016: dense even polar-free image (2026-10-19)

New difference from 015: global PSD is no longer assumed; the
annihilator of U_T 011 on ALL even polar-free tests is computed. At α 1/4,
for each T>0, closure U_T(P_Tev)=H, also for the polar-corrected C_c∞ core.
Proof: ηd=<fd,h>=O(d^-1/4), c=Σηd/d converges; the analytic profile b_h of the
annihilator satisfies b_even=λcosh. Integer atomic comb μ, a_n=Σd|nηd−c, a0=0;
μ'=μ−λδ0/2 is anti-Fourier by Gaussian injectivity on even S' (full lemma
included). The Fourier transform of an integer comb is periodic => μ' periodic => constant coeff;
Thetaμ'(1)=0 forces 0; divisor induction ηd 0 => h 0. No new zero input.
Thus every H-continuous Hermitian form PSD on U_T(core) is globally PSD.
With 015+014 it also closes continuous signed combinations of the span of the 3 pieces
positive only on that image, with the SAME map 011. Not finite block E_N, not
discontinuous H-forms, not other maps/T-dependent coefficients nor sign of Q. Favourable
independent audit in AUDIT_016.md. Full D active/OPEN.
