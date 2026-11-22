# Phase 104 — close A1

**Phase closed.** The objective was not proved. The binding balance,
the permanent pieces, and what passes to Phase 105 are in
[`PHASE_104_CLOSURE.md`](PHASE_104_CLOSURE.md). No document in this
folder can be cited as proof of RH.

Single objective: prove, unconditionally and for all \(n\ge150\),

\[
\text{(A1)}\qquad
\int_{\log 2}^{T_n}\bigl(\psi(e^u)-e^u\bigr)e^{-u}L^{(2)}_{n-1}(u)\,du
\ \le\ q_n=\tfrac34A_n+1-L_n^{(1)}(\log 2).
\]

With A0, the finite certificates \(1\le n\le149\) and the identity
\(C_n(T)=\lambda_n-\frac14A_n-R_n(T)\) —the three already proved— this closes \(\Omega_7\)
and therefore RH. The stable chain is in the subsection
`The Phase 102--103 direct route`, labels `prop:li-compact-tail`,
`thm:a1-direct-collapse` and `cor:a1-to-omega7` of the obstruction ledger.

**Closure restriction.** A conditional closure for \(n\ge n_{\rm eff}\) plus a finite range
never completes RH. A1 must be proved unconditionally for all remaining indices.

## Binding correction 104_56A: the cutoff is cofinal

The A0 condition is imposed on the whole ray \(u\ge T\). Therefore, if one cutoff is
admissible, every larger cutoff is too, and for all \(T\ge T_n^0\)
\[
 |R_n(T)|\le \frac{A_n}{4(1+T)}.
\]
Consequently, if \(\delta_n:=\lambda_n-A_n/4>0\), one can choose
\[
 T>\max\left\{T_n^0,\frac{A_n}{4\delta_n}-1\right\}
\]
and then \(C_n(T)>0\). The sufficient cofinal front is, therefore,
\[
 \boxed{\;4\lambda_n>A_n\;},
\]
not the fixed margin \(4\lambda_n-A_n\ge A_n/1001\). The constant
\(2002/501\) remains correct as a uniform sufficient value obtained from the raw floor
\(T\ge1000\), but it is not intrinsic. The adapted choice uses exactly the slack that is
yet to be proved and does not constitute a mechanism for obtaining it.

There is also a logical distinction that the previous record did not make: proving
\(4\lambda_n-A_n\ge0\) for all \(n\ge150\) already gives \(\lambda_n>0\) and proves RH directly,
even though equality does not suffice to deduce A1 at a finite cutoff using only the
bilateral ceiling of A0. Therefore the general claim that a semidefinite conclusion
can never close the master objective is withdrawn; it was only insufficient for the
A1 transfer with a prefixed cutoff.

## Quantifier correction 104_56: density and blocks

If RH is false, the transformed modes of maximal modulus produce excursions
\(4\lambda_n-A_n<0\) on a syndetic set of positive natural density. From this
two criteria equivalent to RH are deduced:

1. \(4\lambda_n>A_n\) outside an exception of upper logarithmic density zero;
2. \(4\lambda_n>A_n\) on consecutive blocks of unbounded lengths.

There is no positive universal constant for the bad density deducible from the
abstract Bombieri--Lagarias axioms; an explicit family of Fejér phases makes that
density arbitrarily small. This relaxation reduces the master objective, but does not yet
prove any new good block for zeta. The literal objective of Phase 104 —A1 for every
\(n\ge150\)— remains open.

## Binding erratum: sign of the incomplete coefficient

The earlier import from Lagarias, eq. (1.15)--(1.17), had the sign of the incomplete block
inverted. With
\[
 k_n(s)=\left(1+\frac1s\right)^n-1,
\]
the residue of \(k_n(s)(-L'/L)(s+1,\pi)\) at \(s=\rho-1\) is
\(-m_\rho k_n(\rho-1)\). Keeping also the orientation of the contour, the
corrected translation in the \(\zeta\) case is
\[
 \lambda_n=A_n+\lambda_n(\sqrt n)+O(\sqrt n\log n),
\]
not \(A_n-\lambda_n(\sqrt n)+O(\sqrt n\log n)\). Hence the correct small remainder is
\[
 \widetilde\varepsilon_n:=A_n-\lambda_n+\lambda_n(\sqrt n)
 =O(\sqrt n\log n).
\]
The quantity used before,
\[
 \varepsilon_n^-:=A_n-\lambda_n-\lambda_n(\sqrt n),
\]
is still an exact identity, but
\(\varepsilon_n^-=\widetilde\varepsilon_n-2\lambda_n(\sqrt n)\) and does **not** have an
unconditional bound \(O(\sqrt n\log n)\). Every corollary that used such a bound, including the finite range
derived from \(C_*\), is withdrawn. This erratum does not touch the prime--Laguerre identity nor A0--A1.
The contour proof additionally needs the printed horizontal stretch repaired:
one first takes \(T=2\sqrt n+\varepsilon_n\), where the geometric ratio is
\(e^{1/4}/2<1\), and returns to \(\sqrt n\) bounding the intermediate band by
\(O(\sqrt n\log n)\).

## Where the new content is

`104_00`–`104_03` are gate, normalization and audit: they consolidate the ground and translate with
rigor what already exists in the literature, without claiming it as a front.
**The new mathematical work started at `104_10` (M1).** `104_11` closed that
mechanism with an exact stop-gate. `104_12` audited the successor M5: it preserves the
signed Möbius--divisor convolution, but does not produce a positive metric or a
new bound. `104_13` specifically rules out **Selberg positivity + \(O(x)\)
summation formula + Riccati** as an autonomous source; it does not rule out every possible
special coupled theorem for the real weights. `104_14` also closes M3 in its current specification: the
stationary map organizes heights, but loses the radial parameter that determines the
sign. `104_15` proves that the positive Koszul complex of the divisor cube
cancels the \(p/q\) quotients, but simultaneously makes the
\(M\delta Z\) connection null-homotopic; it is not the missing mechanism either. The next front must contribute a concrete arithmetic identity for
the real weights \(\Lambda\), not another polarization of the same forms.
`104_16` tests precisely the complete hierarchy of the Jordan cocycle:
it proves \(\mu*\log^k\ge0\) for all \(k\), but its first polar--Euler jet is
the same cost \(C_{n,\varepsilon}\) and loses the sign already at degrees \(1,6\).
The Gamma completion produces a Schur family equivalent to RH and the completion
half has coefficient exactly \(-\Delta D_n/2\); no intermediate bound appears.
After correcting the sign of the incomplete block, `104_17`
directly attacks its lower bound via Abel--Fejér averages. It proves
that the radial Abel germ of each quartet is strictly positive even
off the line, while its coefficients and triangular averages can
be exponentially negative. Therefore the radial positivity does not transfer
the sign A1 needs. `104_18` keeps finite and correlated
\(u=c\varepsilon\) in the Jordan cocycle: it derives an exact recurrence and
renewal, but the limit is again
\(C_n=\lambda_n^{\rm prime}-\lambda_{n+1}^{\rm prime}\). The real order, the
monotonicity in \(c\), and the identical vanishing of the explicit channel via
constant weights fail with exact witnesses. `104_19` incorporates the Gamma factor and eliminates the root of the
half-cocycle: it derives three exact finite channels, but its polar measure is
signed for all \(c>0\), the isolated channels diverge, and the limit returns to
\(-\Delta D_n\).
`104_20` combines each prime tower and the three channels before estimating. The
formula factors as an exact algebraic square \(\mathsf C_p^2\),
but not as \(\mathsf C_p^*\mathsf C_p\): the real arithmetic blocks
have both signs. The tower-by-tower sign dies; the inequality of the global
multiplicative sum stays alive.
`104_21` runs that global gate: the normalized multiplicative law is
compound-Poisson and convolution-ordered, but fails PF2 with a rational minor
from the primes 2 and 3. More decisively, the completed real cocycle
is not completely monotone: its inverse Laplace density is negative at
\(x=\frac12\log2\), before the first arithmetic atom. The PF/TP routes,
decreasing variation, and global positive measure all die; the successor left
is the signed Stein--Mecke global identity.
`104_22` retains the factor \((1+T_n)^{-1}\) that the last line of A0
discarded. With it, the original A1 no longer requires
\(2\lambda_n-A_n\ge0\): the strictly weaker margin \(3\lambda_n-A_n\ge0\)
suffices. The corresponding exact cocycle is
\(H_u^3K_u^2\); three Euler channels and two Gamma channels are positive, and the only
remaining front is globally controlling the coupled cubic pole.
`104_23` additionally uses \(T_n\ge1000\): the sufficient margin drops to the fixed value
\(r_*\lambda_n-A_n\ge0\), \(r_*=2002/501\), almost quartic. Euler and Gamma
remain positive for this real exponent by infinite divisibility;
the pole adds up as a signed hypergeometric density. `104_56A` corrects its
interpretation: it is the uniform sufficient value associated with the raw floor, not the
intrinsic front when the cutoff can be increased index by index.
`104_24` runs Stein--Mecke on the cubic cocycle. It obtains four direct
channels with \(L_k^{(1)}\) and a global recurrence that preserves all the
other primes, but the completed generator is already negative at
\(\frac12\log2\), before the first prime atom. The positive order of the
generator dies, not the special signed inequality.
`104_25` applies Fejér--Carathéodory to the same cocycle. The identity produces
exactly \(3\lambda_n-A_n\), but the holomorphy needed on a sequence
of full disks is already equivalent to RH. The safe disk of the Euler series
shrinks like \((1-c)\varepsilon\) and only controls damped averages.
`104_26` proves that moving to integer exponent four also does not create a sum
of squares: the local fourth power is still algebraic, fails PF2, and
its quadratic part vanishes in the direct limit. Its slack
\(4\lambda_n-A_n\ge A_n/1001\) remains exactly the cost of the
transfer that fixes only \(T\ge1000\), but `104_56A` withdraws the
claim that this slack is necessary for RH or for an adapted cofinal
cutoff: the non-negative sign suffices for RH and the strict sign for the
cofinal transfer to A1.
`104_27` rules out recovering that slack by declaring the tail sign favorable:
under the same VK envelope there are smooth, monotone discrepancies with
\(R_n(T)\) of both signs. Any real sign must use the weights
\(\Lambda(m)\).
`104_56`--`104_61` change the quantifier for the first time, instead of
reformulating the same pointwise inequality again. Under \(\neg\mathrm{RH}\),
the dominant outer modes force exponential excursions on a
syndetic set. Hence it suffices to exclude, on some long intervals, a
positive density of excursions deeper than any subexponential barrier.
`104_60` expresses this via a saturated one-sided barrier;
`104_61` obtains the still weaker criterion \(\lambda_n\ge-1\) on blocks
of unbounded length and a bounded Fermi--Dirac partition that measures the
logarithmic density of excursions. Its prime--Laguerre representation
keeps pole, Gamma, and all weights \(\Lambda(m)\) coupled inside the non-
linearity. The exponential partition
\(\sum_{n\le X}e^{-t\lambda_n}/n\) remains as a stronger algebraic auxiliary:
its bound \(O(\log X)\) already forces a lower bound in each degree and does not exploit
the density relaxation. Neither limit is proved.
`104_62` carries Fermi to a unitary prime--Laguerre product and localizes
its signal exactly at microfrequencies \(s\asymp e^{-an}\). The
diagonal coordinate \(s=e^{-nv}\) fixes that rate, but the generating function only controls
the geometric product of phases: at the boundary all Hadamard powers
survive and the arithmetic Fermi average remains open. `104_63` also closes
the cross-degree energy rescue: Parseval and
Christoffel--Darboux exist, but their regulated pieces diverge like
\(\varepsilon^{-4N}\) and only the complete functional cancels.
`104_64` replaces the Cesàro logarithmic average by an exact Abel average:
a prefixed radial subsequence suffices, although the falsifier shows that the
Fourier layer must reach \(s=\exp(-c/h)\). `104_65` proves that no
difference, moving average, or fixed local filter removes the dominant
excursions unless it also annihilates the counterexample. `104_66` diagonalizes
the regulator with \(\varepsilon(h)=e^{-1/(100h)}\), so that each scale
uses an absolutely convergent Euler series; separating pole and primes still
costs a precision \(\exp(-C/h^2+O(1/h))\). `104_67` reinforces the
obstruction: under non-RH there are exponential excursions of both signs, each
syndetic and of positive density. Finally, `104_68` eliminates the
existential block selector: the fixed windows
\(I_L=[L^2,L^2+L-1]\) distinguish RH via a Fermi sum or a
finite product tending to \(1\) under RH and to \(0\) under non-RH. `104_69` gives the
finite global version in \(\log X\), also on a single Euler diagonal.
The `104_69B` audit separates these repackagings from the
Bombieri--Lagarias antecedents and from classical summability. `104_70` proves that lowering the
Fermi temperature subexponentially preserves the detector, but cannot
damp the pole with a regulator tending to the boundary: both obligations
are quantitatively incompatible. `104_71` gives the exact entropic duality
of the windows: correlations pay their multi-information and the optimizer
refactors, but a variational bound with slack
\(\exp(o(L^2))\) on a single subsequence suffices to prove RH. `104_72` returns
to the bounded detector via a pressure ratio: each deep excursion
contributes only a factor \(e^\tau\), so density is preserved but not
depth. The gain is real, but the transition still depends on the
complete prime--pole difference with additive precision \(O(1)\).
`104_73` proves that neither the positive Bernstein representation nor a
variable width removes that wall: any width that detects every outer mode leaves
a relative cost \(\exp\{-X^2/100+o(X)\}\). `104_74` reformulates the same
pressure via a Hadamard semigroup and Jensen potentials; the outer contour
becomes polynomial, but every exponential rate resides exactly in the
finite sum of interior residues. Finally, `104_75` replaces the
\(O(1)\) transition by the weakest one-sided target obtained so far:
it suffices that prime--pole overshoots of size \(e^{\sqrt X}\) have
logarithmic density zero. The first-order Poissonized transform closes in
Bessel form, but the quartet shows that it does not control that rare event.
`104_76` shows that the tail of zeros with
\(\gamma>X^{1/4}\) is \(O(X\log X\,e^{\sqrt X/2})\), uniformly in
\(n\le X\): every possible deep violation is localized in the block
\(\gamma\le X^{1/4}\). `104_77` obtains the complementary localization by
contour: the outer part is polynomial and the whole difficulty is a
finite sum of interior residues; Jensen, Cartan, and Turán detect those
residues but do not eliminate them.
`104_78` constructs a lattice Euler falsifier with unitary renewal,
complete towers, positive weights, functional equation, and a prime degree law:
its deep tail has density \(1/4\). It does not preserve the continuous PNT nor the
Gamma factor, and so it delimits —without replacing— the real problem.
`104_79` returns to the ordinary \(\Lambda(m)\): the exact representation
by the zeta law has prime and semiprime tails of both signs with first
excesses \(\ge e^{X^2/500}\). Thus, truncating or concentrating each tail
separately loses the cancellation that determines the mean.

## Documents

| file | role | content |
|---|---|---|
| `104_00_BIBLIOGRAPHY_GATE.md` | gate (blocking) | duplicates / does-not-duplicate verdict by mechanism, with explicit conditional/unconditional label |
| `104_01_THETA_FAMILY.md` | normalization | family \(C_n^\theta\), reserve \(q_{n,\theta}\), effective \(T_n(\theta)\), signed transport \(\Delta_{n,\theta}\) |
| `104_02_LAGARIAS_TRANSLATION.md` | **binding sign erratum** | corrected coordinate \(-\lambda_n(\sqrt n)+\widetilde\varepsilon_n\); the old Theorem A and the finite corollary based on \(C_*\) are withdrawn |
| `104_03_CONTOUR_RESIDUE_AUDIT.md` | audit | contour of \(R(t)\), trivial poles, Cayley identity, stationary map |
| `104_10_M1_COLLECTIVE_KERNEL.md` | audited mechanism | collective identity and local-PSD no-go |
| `104_11_M1_GLOBAL_MAX_STOP_GATE.md` | **exact stop-gate** | the compensator is the `max` energy; cancellation of Hessians and collapse to the original linear functional |
| `104_12_M5_MOBIUS_DIVISOR_AUDIT.md` | **exact identity + Gram stop-gate** | Möbius--divisor convolution by degree; comparison with E70.11--12 and 103_71; the Möbius inverse cannot be a positive adjoint |
| `104_13_M5_SELBERG_RICCATI_GATE.md` | **exact recurrence + scale stop-gate** | Selberg--Riccati recurrence by degree; the regulated collision costs \(\varepsilon^{-n-1}\) and the \(O(x)\) summation loses \(\exp((1+o(1))n\log n)\) |
| `104_14_M3_NONLOCAL_STOP_GATE.md` | **completed form + bulk stop-gate** | A1 as Weil autocorrelation minus reserve and tail; an off-line quartet and a critical divisor with the same heights give opposite signs |
| `104_15_EULER_GAMMA_COMPLEX_GATE.md` | **minimal construction + cohomological stop-gate** | positive Koszul complex on the posets \(\{1,p\}\), \(\{1,p,q,pq\}\); cancels mixed quotients, but makes \(M\delta Z\) exact |
| `104_16_JORDAN_COCYCLE_ATTACK.md` | **positive hierarchy + Cayley/Schur stop-gate** | cocycle \(\zeta(s-u)/\zeta(s)\), \(\mu*\log^k\ge0\); the polar pairing loses sign, the budget is \(-\Delta D_n/2\), and the completed contractivity is equivalent to RH |
| `104_17_INCOMPLETE_LI_ABEL_STOP_GATE.md` | **Abel theorem + Tauberian stop-gate** | exact formulas for the incomplete quartet and its averages; radial Abel positivity compatible with exponentially negative coefficients |
| `104_18_CORRELATED_SHIFT_STOP_GATE.md` | **finite identity + order stop-gate** | exact recurrence for \(u=c\varepsilon\), signed renewal form; the limit returns to \(C_n\), the real order does not control coefficients, and finite constant weights do not identically annihilate the explicit channel |
| `104_19_THREE_CHANNEL_BRANCH_FREE_GATE.md` | **exact expansion + polar stop-gate** | cocycle \(Y(s-u)/Y(s)\) in three Jordan--Beta channels; signed polar measure, divergence upon separating, and exact limit \(-\Delta D_n\) |
| `104_20_LOCAL_TOWER_SQUARE_AND_GLOBAL_GATE.md` | **local factorization + live global gate** | exact second difference of \(b_u(p^k)\), operational square \(\mathsf C_p^2\), witness of both signs by backgrounds; the cancellation across all towers remains as the front |
| `104_21_GLOBAL_COMPOUND_POISSON_TP_GATE.md` | **global product + PF/CM stop-gate** | exact compound-Poisson law over all primes; rational PF2 minor \(-1/2916\); completed inverse density negative before \(\log2\); Stein--Mecke identified as successor |
| `104_22_CUBIC_MARGIN_REDUCTION.md` | **new reduction + live cubic gate** | retained A0 gives \(|R_n|\le A_n/[4(1+T_n)]\); \(3\lambda_n-A_n\ge0\) implies the original A1; cocycle \(H_u^3K_u^2\) and direct normalization with limit \(-(3\lambda-A)\) |
| `104_23_NEAR_QUARTIC_REAL_MARGIN.md` | **uniform reduction from the A0 floor + live real gate** | \(r_*=2002/501\) is sufficient using only \(T_n\ge1000\); real Euler--Gamma powers positive; exact pole \(-rce^{-q}{}_1F_1(1-r;2;cq)\) |
| `104_24_DIRECT_CHANNELS_AND_STEIN_GATE.md` | **global identity + positive Stein stop-gate** | four channels \(L_k^{(1)}\), base \(k+1\), Stein--Mecke recurrence; completed density negative before \(\log2\), without refuting the special global sign |
| `104_25_FEJER_CARATHEODORY_GATE.md` | **analytic positivity + holomorphy stop-gate** | Fejér turns \(\Re\Phi\le1\) into the cubic margin; holomorphy of the regulated disks \(\Longleftrightarrow\) RH; exact witness against transfer from smaller disks |
| `104_26_QUARTIC_SQUARE_STOP_GATE.md` | **fourth power + square stop-gate** | local fourth difference, exact PF2 minor, real block of both signs and off-line falsifier; \(D_n^{[4]}\ge A_n/1001\) is only the sufficient cost of the cutoff fixed by the floor \(T\ge1000\), not an intrinsically necessary coercivity |
| `104_27_TAIL_SIGN_NO_GO.md` | **A0+ audit + sign stop-gate** | two discrepancies under the same VK envelope produce opposite tails; smooth version compatible with eventual monotonicity |
| `104_28_FIXED_VECTOR_BRIDGE_AND_WHITENING_STOP_GATE.md` | **exact hard-edge bridge + whitening stop-gate** | \(g_n=e^{-x/2}L_{n-1}^{(1)}=\sum_{k<n}e^{-x/2}L_k\); prime--pole form on a single ray; the archimedean Toeplitz has \(A_1<0\), so the proposed spectral quotient does not exist |
| `104_29_LOG2_COMPENSATED_SPLIT_GATE.md` | **exact cut at the first prime + mass stop-gate** | compensated generator, blocks \(J_n^<+J_n^\ge\); the mass comparison gives a false positive and the outer weighted inequality recomposes exactly \(D_n^{[r]}\ge0\) |
| `104_30_FLAG_HARD_EDGE_REFERENCE_AND_SCHUR_GATE.md` | **exact positive reference + spectral gate** | the diagonal flag satisfies \(A_{\rm flag}[g_n]=A_n\); exact prime--pole polarization and finite whitening; the spectral diagnostic is favorable but Schur/Gershgorin requires controlling \(\Delta^2(A-\lambda)\) |
| `104_31_EPSILON_FLOW_OBSERVABILITY_STOP_GATE.md` | **exact birth--death flow + domain stop-gate** | \(c'=Qc\), \(Q=-M_x\); the backward test requires \(\varepsilon<1/2\) and the separated Euler operator requires \(\varepsilon>1/2\); \(A_{\rm flag}\) is neither invariant nor does it move the threshold |
| `104_32_HIGHER_PRIME_POWER_BUDGET.md` | **exact separation + explicit budget** | \(H_{\ge2}=-\sum_{j\ge2}\mu(j)(-\zeta'/\zeta)(js)\); pole \(j=2\) at \(z=-1\), bound \(\lvert P_{n-1}^{(\ge2)}(1)\rvert<14n+1\) and exact quartic reduction to the prime--pole channel |
| `104_33_FLAG_SYMBOL_BOUNDARY_RESIDUE_GATE.md` | **exact symbol + boundary--residue stop-gate** | \(h(z)=-\zeta'/\zeta((1-z)^{-1})-1/(s-1)\); the flag moment is boundary plus off-line residues; a quartet preserves the real boundary and changes the moment exponentially |
| `104_34_FLAG_PREFIX_CURVATURE_AND_ADJACENT_SCHUR_GATE.md` | **curvature refuted + adjacent Schur gate** | the outward certificate proves \(\nabla_c^2(\lambda-501A/2002)_{220}<0\); the compression \(\mathrm{span}\,\{g_n,\phi_n\}\) gives the sufficient coercive criterion \(4H_nd_n\ge(H_n+d_n-H_{n+1})^2\), still open uniformly |
| `104_35_SIMPLE_PRIME_POLE_SELBERG_GATE.md` | **exact \(\theta\) correlation + simple Selberg stop-gate** | \(B_n^{(p+\mathrm{pole})}=-n-\int(\theta(e^u)-e^u)e^{-u}L_{n-1}^{(2)}\); collective identity for primes/semiprimes only; non-coercive inverse kernel and witness on real prime support |
| `104_36_SIMPLE_PRIME_CHOLESKY_DOMAIN_GATE.md` | **exact collective Cholesky + domain stop-gate** | \(B_{n,a}^{(p+\mathrm{pole})}=\langle V_{n,a},g_n\rangle\) and exact large-sieve norm for \(a>2\); zero residues prevent continuing the norm to \(a=1\), with divergence \(\gg(a-1)^{-1}\) even from critical zeros |
| `104_37_TAPERED_SELBERG_HANKEL_GATE.md` | **exact Schur taper + two-point Hankel stop-gate** | the optimal test is \(ae^{-au}[L_{n-1}^{(1)}+tL_n+t(t-1)]\); after inverting Selberg, every \(t\) has a tail minor with leading term \(8^d-9^d<0\), also over real prime logarithms |
| `104_38_CANONICAL_SELBERG_SQUARE_CANCELLATION_GATE.md` | **exact Schur completion + canonical square stop-gate** | the Selberg \(\mu*\mu\) term identically cancels the square of the inversion; if reserved to pay for Schur, the residual kernel has diagonal \(-a^{2n+2}e^{-2aR}R^{2n}/[4d(n!)^2](1+o(1))<0\), even on a single atom \((\log p)\delta_{\log p}\) |
| `104_39_ADJACENT_RICCATI_TRIANGLE_STOP_GATE.md` | **exact triangular factorization + sufficiency stop-gate** | the adjacent determinant is equivalent to triangular inequalities among \(\sqrt{H_n},\sqrt{d_n},\sqrt{H_{n+1}}\); a critical quartet keeps the scalar margin and breaks the gate, so the gate is strictly stronger than the objective |
| `104_40_CANONICAL_EULER_RESOLVENT_STOP_GATE.md` | **fixed-ray resolvent + modulus stop-gate** | optimization over every positive multiplier preserves prime--pole up to the last step, but its optimal cost is \(\int|\widehat g_n|^2|M|\), which diverges logarithmically from critical zeros; off-line zeros appear earlier as crossing residues |
| `104_41_FULL_MANGOLDT_PHASE_HOMOTOPY_GATE.md` | **complete Mangoldt phase + homotopy stop-gate** | for \(M_\Lambda=(s-1)^{-1}+\zeta'/\zeta\), pole and all \(p^k\) coupled, the exact phase proves \(|\mathcal B_{n,a}|\le3n\) for \(a\ge4\); lowering to \(a=1\), each right zero crosses at \(a=2\Re\rho\) and contributes the residue from `104_33`; a rational quartet preserves the whole critical phase and changes the moment exponentially |
| `104_42_DEGREE_ADAPTED_NONCOMMUTATIVE_PRECONDITIONER_GATE.md` | **non-commutative quadratic optimum + degree stop-gate** | the algebraic infimum over every positive preconditioner is exactly \(|\langle v,g\rangle|\); the projection onto the first \(n\) Laguerre terms preserves phase, but the new datum reappears with factor \(\sqrt{n/2}>1\) |
| `104_43_ZETA_SIZE_BIAS_DIVISOR_MARTINGALE_GATE.md` | **exact size-biased factorization + probabilistic stop-gate** | \(N^*=DN'\), with \(D\) of law \(\Lambda(d)d^{-s}\) and selector \(\Lambda(d)/\log N\); the polar comparator is a uniform split Gamma, but the order changes sign, the marginal comparison is exactly \(R\), and separated Efron--Stein loses \(\varepsilon^{-2n+2}\) |
| `104_44_DIVISOR_MARKOV_LAGUERRE_TRANSPORT_GATE.md` | **transport \(\Lambda*1=\log\) + scale stop-gate** | the divisor operator is Markov but has zero gap even at mean zero; Laguerre addition preserves the full convolution and its Gamma continuum contracts by degree, but switching to the unscaled test costs exactly \((2/\varepsilon-1)^{n-1}\) |
| `104_45_CROSSED_DIVISOR_GAMMA_STEIN_GATE.md` | **exact crossed Stein + canonical signed kernel** | any coupling recomposes the same tail kernel \(K_s\), which changes sign around \(\log2\); over exponentials \(R(q)<0\) does hold, but there is no complete monotonicity, and over Laguerre the identity returns exactly to \(B_n\) |
| `104_46_FIXED_LAGUERRE_MARKOV_EXTREMAL_GATE.md` | **specific fixed-vector stop-gate** | for \(s>1\) close to one, the centered arithmetic Laguerre itself satisfies \(Q_r(s)\to1\) at the divisor selector, while the Gamma comparator satisfies \(Q_r^\Gamma(s)\to0\); a Markov gap cannot give the sought coercivity |
| `104_47_SIZE_BIASED_HOMOTOPY_FLUX_GATE.md` | **exact homotopy flow** | \(a\partial_a\mathcal B_{n,a}=n(\mathcal B_{n+1,a}-\mathcal B_{n,a})\); its integrated flow is equivalent without remainder to the margin, and the off-line quartet appears as an exponential pulse |
| `104_48_PRIME_TOWER_SIGNED_COERCIVITY_GATE.md` | **closure by tower + unit multiplicity gate** | \(\Phi_n\) has a Poisson formula and a one-sided bound in a useless direction; tower constancy + PNT admits a witness at \(n=151\), so only the global unit renewal \(\Lambda*{\bf1}=\log\) survives |
| `104_49_UNIT_DIVISOR_RENEWAL_SIGNED_GATE.md` | **unit Palm + moment--cumulant stop-gate** | the marked exponent is uniform within each tower and distinguishes \(\omega_c\), but selector and transport exactly cancel the total moment degree by degree; its Laguerre combination returns to \(B_n\) |
| `104_50_SECOND_ORDER_UNIT_PALM_COVARIANCE_GATE.md` | **second-order unit Palm + orientation gate** | the centered covariance cancels all distinct towers; the uncentered defect retains them, but its completed square is variance plus the square of the margin and loses exactly the orientation |
| `104_51_MOBIUS_INVERTED_LCM_RESERVE_GATE.md` | **double Möbius inversion of the `lcm` Gram + reserve gate** | \(K=Z^TWZ\) and \(M^TKM=W\) exactly diagonalize the kernel; the infinite reserve is indefinite on a two-level vector, and its local cutoff has opposite signs for the real Laguerre \(P_{150}\) at \(p=2,7\) |
| `104_52_CONNECTED_TWO_TOWER_FLUX_GATE.md` | **completed Hessian + connected cancellation** | the exact margin has a tower--pole--Gamma Hessian, but all pairs between distinct primes and the prime--pole crossings cancel; the Hessian and the Laguerre cocycle have both signs |
| `104_53_CONNECTED_CUMULANT_CANCELLATION_THEOREM.md` | **Hopf classification of additive identities** | every additive polynomial observable in the moments is a linear combination of cumulants; for the zeta law each cumulant stays within a single tower, so no exact multi-tower identity can leave a disconnected reserve |
| `104_54_GIBBS_CHERNOFF_UNIT_PALM_GATE.md` | **non-additive Gibbs--Chernoff gate** | for all \(n\ge4\), \(s>1\) and \(t\ne0\), \(\mathbb E_s e^{tD_{n,s}}=\infty\); prime and semiprime fibers produce opposite tails of order \((\log N)^n\), and the variational bound is infinite |
| `104_55_THREE_MARK_UNIT_PALM_ORIENTATION_GATE.md` | **three-mark Palm + cubic gate** | third moment, determinant and third difference lack a sign; the oriented polarization is exactly positive variance times the unknown margin, and the real unit asymmetry already changes sign between \(N=6\) and \(N=18\) |
| `104_56_DENSITY_RELAXED_LI_CRITERION.md` | **relaxed-quantifier theorem** | if RH fails, the quartic margin fails on a syndetic set of positive density; RH is equivalent to the margin outside logarithmic density zero or on unbounded good blocks; there is no universal density from the BL axioms |
| `104_56A_CUTOFF_FREEDOM_AUDIT.md` | **intrinsic-front erratum** | A0 is cofinal in the cutoff; \(4\lambda_n>A_n\) allows an adapted cutoff closing A1, while \(2002/501\) only encodes the floor \(T\ge1000\) |
| `104_56B_DENSITY_NOVELTY_AUDIT.md` | **specific bibliographic gate** | dominant modes and exponential negativity i.o. are known; the positive-density/syndeticity/blocks reinforcements and the prime--Laguerre Fermi lift were not located in the primary sources reviewed, without claiming exhaustive priority |
| `104_57_LOW_ZERO_BLOCK_BUDGET.md` | **quantitative map of the low block** | the regularized tail \(|\gamma|\ge\sqrt n\) reproduces \(A_n\) with error \(O(\sqrt n\log n)\); the remaining block has \(\asymp\sqrt n\log n\) labels and the exact budget of every successor is fixed |
| `104_58_TRANSLATIONAL_DENSITY_ATTACK.md` | **degree windows + homotopy no-go** | every fixed translational window preserves a class of off-line failures of positive density; the phase bound at \(a\ge4\) does not transport to \(a=1\) without the crossed residues |
| `104_59_PRELOG_MAJORISATION_GATE.md` | **Schur/Karamata audit** | the classical pre-log majorization was already contained in 104_21/43/44; the Laguerre test has curvature of both signs and the real divisor selector reverses orientation |
| `104_60_NONLINEAR_DEGREE_BARRIER_CRITERION.md` | **large-deviation criterion in the degree** | RH is equivalent to a saturated barrier of the excursions \(4\lambda_n-A_n\le-b_n\), \(b_n=e^{o(n)}\), having mean tending to zero on some long intervals |
| `104_61_SUBEXPONENTIAL_DENSITY_AND_NONLINEAR_PARTITION.md` | **weak criterion + paired partitions** | \(\lambda_n\ge-1\) on unbounded blocks suffices; the bounded Fermi partition detects exactly positive logarithmic density and has a complete prime--Laguerre representation; the exponential partition is a coefficient-by-coefficient auxiliary criterion |
| `104_62_UNITARY_FERMI_MICROFREQUENCY_GATE.md` | **unitary lift + microfrequency stop-gate** | Fourier preserves every channel as unit-modulus phases, but an excursion of depth \(Y\) lives at \(s=O(Y^{-1})\); diagonal scaling only controls the geometric product, not the Fermi mean |
| `104_63_CROSS_DEGREE_H2_ENERGY_GATE.md` | **cross-degree Parseval/CD + quantitative no-go** | the dyadic energy detects exactly the first interior pole; the CD kernel is positive, but pole², primes², and cross terms are of order \(\varepsilon^{-4N}\) and cannot be separated |
| `104_64_LOG_ABEL_FERMI_BOUNDARY_GATE.md` | **logarithmic Abel criterion + layer gate** | the Cesàro and Abel Fermi averages are equivalent and a fixed subsequence suffices; the falsifier requires microfrequencies up to \(s=\exp(-c/h)\) |
| `104_65_LOCAL_FILTER_LONG_BLOCK_GATE.md` | **classification of local filters** | every difference, moving average, or finite filter preserves syndetic negative excursions unless it also annihilates the dominant modes; the quartet exhibits that loss of information |
| `104_66_DIAGONAL_ABEL_REGULATOR_GATE.md` | **exact Euler diagonal + separation stop-gate** | \(\varepsilon(h)=e^{-1/(100h)}\) uniformly approximates the degrees \(n\le1/h\) within a convergent Euler series; separating pole and primes requires superexponential relative cancellation |
| `104_67_TWO_SIDED_EXCURSION_GATE.md` | **two-sided excursions** | under non-RH there exist syndetic sets of positive density with \(\lambda_n\ge cR^n\) and with \(\lambda_n\le-cR^n\); subexponential upper, lower, or two-sided barriers on unbounded blocks are equivalent to RH |
| `104_68_DETERMINISTIC_BLOCK_POLYMER_CRITERION.md` | **deterministic windows + finite partition** | RH is equivalent to the Fermi sum over \([L^2,L^2+L-1]\) tending to zero, or its product tending to one; \(\varepsilon_L=e^{-(L^2+L-1)/100}\) gives a single convergent Euler sequence, but the gas refactors and creates no new cancellation |
| `104_69_FINITE_LOGX_DIAGONAL_FERMI_CRITERION.md` | **finite criterion in \(\log X\) + Euler diagonal** | RH is equivalent to a single logarithmic Fermi mean; \(\varepsilon_X=e^{-X/100}\) simultaneously replaces the first \(X\) degrees by an absolutely convergent prime--Laguerre formula, with exponential error |
| `104_69B_COUNTEREXAMPLE_ROUTE_NOVELTY_AUDIT.md` | **Fermi/blocks bibliographic gate** | separates the known outer mode and classical log-Cesàro/Abel summability from the potentially substantive syndeticity/density; Fermi, product, quadratic windows, and Euler diagonal are recorded as corollaries or repackagings not located exactly, without claiming priority |
| `104_70_VARIABLE_TEMPERATURE_FERMI_GATE.md` | **variable temperature + polar no-go** | subexponential temperatures preserve the detector of every outer mode, but any scale that damps the pole with \(\varepsilon_n\to0\) necessarily loses that sensitivity; relative conditioning does not improve |
| `104_71_ENTROPIC_BLOCK_VARIATIONAL_ATTACK.md` | **Bernoulli--entropy duality + interaction gate** | the block partition is a Bernoulli expectation with a telescoping factor; Gibbs converts it into a uniform bound over \(G_{L,q}\), admissible with slack \(\exp(o(L^2))\), but multi-information eliminates all correlation and the optimizer refactors |
| `104_72_BOUNDED_PRESSURE_RATIO_ATTACK.md` | **saturated pressure ratio + transition gate** | a ratio of two partitions limits each site to \([1,e^\tau]\) and preserves only the excursion density; the diagonal lift is exact, but deciding the transition \(z\asymp1\) requires the prime--pole difference with additive error \(O(1)\) |
| `104_73_BERNSTEIN_PRESSURE_WIDTH_GATE.md` | **exact Bernstein + variable-width gate** | the pressure is a positive mixture of Poisson probabilities; it admits no non-trivial global affine majorant, and any width that preserves every outer mode keeps the quadratic prime--pole conditioning |
| `104_74_HADAMARD_JENSEN_PRESSURE_GATE.md` | **Hadamard semigroup + Jensen + interior residues** | the Hadamard exponential has positive radius exactly under RH; Jensen represents the pressure by ring crossings, while a safe contour leaves every exponential rate in a finite sum of interior poles |
| `104_75_POISSON_LOGX_HARD_TRANSITION_GATE.md` | **hard transition + deep density gate** | RH is equivalent to zero logarithmic density of prime--pole overshoots \(\ge e^{\sqrt X}\); Poissonization localizes the degrees and gives a Bessel identity for the first moment, but the quartet proves that moment does not control the nonlinear tail |
| `104_76_DEEP_TAIL_HEIGHT_LOCALIZATION.md` | **height localization + moment gate** | zeros with \(\gamma>X^{1/4}\) contribute \(O(X\log X\,e^{\sqrt X/2})\); under partial RH up to \(X^{1/4}\) the deep observable is identically zero, and every obstacle remains in the low block |
| `104_77_CARTAN_TURAN_DEEP_TAIL_GATE.md` | **safe contour + Cartan--Turán gate** | the outer error is \(O(n^5\log^2n)\) and every deep tail resides in a finite sum of interior poles; Jensen, Cartan, and Turán do not annihilate it, and a quartet with positive continuation on the real ray preserves deep density \(1/8\) |
| `104_78_UNIT_RENEWAL_EULER_DEEP_TAIL_FALSIFIER.md` | **lattice unit Euler falsifier** | renewal, unit towers, positivity, functional equation, and an exponentially precise prime degree law still allow off-line zeros and deep density \(1/4\); the model does not satisfy the continuous PNT nor contain Riemann's Gamma |
| `104_79_ZETA_LAW_DEEP_TRUNCATION_GATE.md` | **exact zeta law + truncation gate** | \(Q-p\) is the expectation of a prime--pole defect with real \(\Lambda\); its positive and negative excesses above \(e^{\sqrt X}\) are at least \(e^{X^2/500}\) on the diagonal, so separate concentration or truncation does not transport the mean |
| `104_80_MAXIMAL_SIGNED_LAMBDA_IDENTITY_GATE.md` | **maximal signed identity + non-removable pole** | Möbius--Laguerre exactly recomposes \(-\partial_z\log\{(s-1)\zeta(s)\}\); each zero \(\Re\rho>1/2+\varepsilon\) leaves an interior pole of residue \(-m_\rho\) and coefficients \(m_\rho z_\rho^{-n}\), so no exact regrouping removes the obstruction |

| 104_81_ON_OFF_LINE_DEEP_OBSERVABLE_CONTROLS.md | **validated on/off-line controls of the deep observable** | a critical quartet gives density \(0\) exactly and an outer one gives \(1/8\), even with the diagonal regulator; two positive Euler models give \(0\) and \(1/4\) respectively, validating the detector but without proving the limit for the ordinary \(\Lambda(m)\) |

## Process rules

1. Pre-registration: statement + **explicit enumeration of axioms and inputs** + off-line
   falsifier constructed to satisfy exactly those axioms.
2. Never absolute values on the kernel. Pole + Γ + primes + conjugation + boundary coupled
   until after estimating.
3. Exact \(q_n\), never the asymptotic form \(\frac38 n\log n\).
4. Binding erratum: \(\lambda_n^{\rm prime}=-n+\int(\psi-y)f'=\int(\psi-y+1)f'\).
   The boundary term \(-n\) is not discarded.
5. Explicit conditional/unconditional labeling on every imported statement.
6. Rational arithmetic with outward intervals in every certificate.
7. Adversarial ledger at closure, `103_13` style.

## Tools

`cd tools && python3 <file>` — pure Python + numpy, no external dependencies, same as
phase-103. `m1_global_hessian_check.py` and `jordan_cocycle_sign_gate.py` use
only `Fraction` rational arithmetic for their sign decisions;
`incomplete_abel_stop_gate_check.py` does the same for the `104_17` witness.
`three_channel_cocycle_check.py` verifies with `Fraction` the convolution on
prime powers and the polar identities of `104_19`.
`local_tower_square_check.py` exactly verifies the operators and the
local sign threshold of `104_20`.
`global_cocycle_probe.py` reproduces the Cauchy/Borwein diagnostic of the
global sum; it is `float64`, not a certificate.
`global_compound_poisson_tp_check.py` uses `Fraction` for the PF2 minor of two
primes and records the exact integral certificate of the `atanh` inequality
of `104_21`; it makes no sign decisions in floating point.
`cubic_cocycle_probe.py` compares two Cauchy radii for the cocycle
\(Y_r(s-u)/Y_r(s)\); it is a `float64` diagnostic, never a certificate. For
\(r\notin\mathbb Z\) it uses pointwise principal logarithms, not an unwound
analytic branch; that is why its non-integer rows are only exploratory and
are not cited as evidence.
`near_quartic_margin_check.py` verifies with `Fraction` the value
\(r_*=2002/501\), the limiting equality of A0, the binomial signs of the pole, and
twelve coefficients of its hypergeometric sum; it does not prove the global sign.
`fejer_caratheodory_gate_check.py` verifies with `Fraction` the coefficient
identity of `104_25` and the witness \(R=1/2\), \(\Phi(z)=6z^4\), for which
the local norm is \(3/8\) but \(q_4=-1\).
`quartic_square_stop_gate_check.py` verifies with `Fraction` the degree-two
quartic witness, the exact relation between \(D^{[r_*]}\) and \(D^{[4]}\),
and the off-line phase of index \(150\).
`fixed_vector_bridge_check.py` verifies with `Fraction` the
Laguerre--prefix identity and the Toeplitz--Fejér telescoping.
`log2_compensated_split_check.py` verifies the compensation at zero, the
exact order \(\varepsilon^{-n}\) of the separated moments, and the strict
sign of the density before the first prime.
`flag_hard_edge_spectrum.py` builds and diagonalizes the whitened sections
of `104_30`; it uses two Cauchy/FFT extractions in `float64` and is only a
diagnostic, never a certificate.
`epsilon_flow_observability_gate_check.py` uses exclusively `Fraction` to
verify the Laguerre recurrence, the polar flow, the rational generating
function of the transported test, and the exact leak \(M(M-1)=22350\) of the flag at
\(M=150\).
`higher_prime_power_budget_check.py` verifies with `Fraction` the
decomposition of the pole \(j=2\), its parity coefficients, and the
rational slack of the thresholds \(e^{28032}\) and \(e^{112116}\).
`flag_symbol_residue_check.py` verifies with Gaussian rationals the
exact boundary--residue identity for the quartet \(w=i/2\), including
that its right pair contributes \(-Q_n\) and that the quartet's derived logarithm
is purely imaginary on the critical line.
`flag_prefix_curvature_gate.py` uses the outward Hasse--eta generator of
`103_51` to certify \(\nabla_c^2H_{220}<0\) and, in the same range,
\(\mathcal T_{219}>2220\), without `float` in the signs.
`flag_prefix_adjacent_schur_diagnostic.py` compares two Cauchy/FFT radii,
locates the blocks of negative curvature, and measures the adjacent Schur
determinant; it is only a `float64` diagnostic.
`simple_prime_pole_selberg_check.py` verifies with `Fraction` the Laguerre
boundary identity, its exact mass \(n\), and the centered Selberg expansion
for the simple-primes channel.
`simple_prime_cholesky_gate.py` verifies with Gaussian rationals and
`Fraction` the Laguerre Laplace transforms, the continuous pole, and
the quartet \(w=i/2\), \(\rho=(4+2i)/5\): at \(n=152\) the residue has
amplitude \(1-2^{-152}\), growth \(e^{3x/10}\), and a negative Li
contribution.
`tapered_selberg_hankel_gate_check.py` verifies with `Fraction` the
tapered polarization, the mandatory term \(t(t-1)\), the Schur identity
in both gauges, and the principal minor \(8^d-9^d<0\); it uses no signs
in floating point.
`canonical_selberg_square_gate_check.py` verifies with `Fraction` the
exact cancellation of the Selberg square, the Laguerre response of the
crossed entry, the negative dominant degree of the residual Schur kernel,
and the collision defect \(-2n^2a^4\); it approximates neither primes nor \(\zeta\).
`adjacent_riccati_gate_check.py` verifies with `Fraction` the triangular
factorization of the adjacent determinant, a critical quartet that preserves
all positive margins but breaks that determinant, and the exact crossing
of the rational off-line quartet
\(\rho=16/41+(20/41)i\).
`canonical_euler_resolvent_gate_check.py` verifies with Gaussian
rationals the off-line crossing, the residual multiplier, and the Young
optimization for positive resolvents; its `asinh` table only illustrates
the logarithmic divergence proved in `104_40`.
`full_mangoldt_phase_homotopy_gate_check.py` verifies with `Fraction` the
rational phase bound, the count \(\mathrm{TV}(W_n)=8n\), the
crossing law \(a=2\Re\rho\), the invariant critical phase of the quartet \(w=i/2\), and
its exponential defect at \(n=152\).
`degree_adapted_noncommutative_gate_check.py` verifies with `Fraction` the
non-commutative quadratic optimum for inner products of both signs,
the Toeplitz compression by degree, the defective coefficient \(n/2\), and the
rational off-line quartet of `104_42`.
`zeta_size_bias_martingale_gate_check.py` verifies with integers and `Fraction`
the size-biased decomposition, the opposite signs of the divisor selector at
\(2\) and \(30\), and the leading constants of the Efron--Stein loss.
`divisor_markov_laguerre_check.py` verifies with `Fraction` the divisor
identity, the Laguerre addition and dilation, and the exact contraction of
the Gamma comparator; it does not evaluate zeros nor make floating-point decisions.
`crossed_divisor_gamma_stein_gate_check.py` verifies the oriented segment
identity, the Laguerre derivative, the symbol cancellation, and the exact
failure of complete monotonicity recorded in `104_45`.
`fixed_laguerre_markov_extremal_check.py` verifies the dilation identities
and the exact Gamma quotient of `104_46`; the PNT transfer of the
saddle is proved analytically in the document.
`size_bias_homotopy_flux_gate_check.py` verifies the differential law, the
polar channel, and the rational Gaussian pulse of the `104_47` quartet.
`prime_tower_signed_coercivity_gate_check.py` verifies the tower
identities, the shifted phase atoms, and the alternating witness at \(n=151\).
`unit_divisor_renewal_signed_gate_check.py` verifies the uniform Palm mark,
the moment--cumulant cancellation, the two signs of the unit defect at
degree 151, and the loss of uniformity of the shifted selector.
`second_order_unit_palm_covariance_check.py` verifies the quadratic Palm, the
`lcm` kernel, the completed bilinear decomposition, and the rational falsifier.
`mobius_inverted_lcm_reserve_gate_check.py` verifies \(K=Z^TWZ\), its double
inversion, the indefiniteness of the infinite kernel, and the two certified local
signs of the vector \(P_{150}\) on real prime towers.
`connected_two_tower_flux_gate_check.py` verifies the connected cancellation,
the tower--pole--Gamma Hessian, its sign change, and the Laguerre cocycle.
`connected_cumulant_cancellation_check.py` verifies with `Fraction` the
additivity of cumulants up to order twelve and the disconnected cancellations
at low orders; the general classification is proved in `104_53`.
`gibbs_chernoff_unit_palm_gate_check.py` verifies the leading coefficients of
the prime and semiprime fibers that force the bilateral Gibbs divergence.
`three_mark_unit_palm_orientation_check.py` verifies the cubic Palm, the
polar factor six, the oriented polarization, the two arithmetic biases, and the signs
of the third Laguerre difference.
`cutoff_freedom_audit_check.py` verifies with `Fraction` the monotonicity of
\(r_{\max}(T)\), the identity \(r_{\max}(1000)=2002/501\), and the adapted cutoff.
`density_relaxed_li_criterion_check.py` verifies the Cayley orientation, the
rational quartet, and the periodic Fejér family that prevents a universal
bad density. `low_zero_block_budget_check.py` verifies the equivalences of the
block \(|\gamma|<\sqrt n\) and the activation bounds by quartet.
`translational_density_attack_check.py` exactly verifies that every fixed
window preserves the falsifier \(w=2i\). `prelog_majorisation_gate_check.py`
certifies the two curvature signs and the arithmetic orientation inversion.
`nonlinear_degree_barrier_check.py` verifies with Gaussian rationals that the
saturated barrier exactly detects the class \(n\equiv0\pmod4\) of the quartet and
that its mean tends to \(1/4\). `subexponential_density_partition_check.py`
certifies the polynomial barrier, the absence of good blocks of length
four, and the incompatibility with the positive Abel germ of the same quartet.
`unitary_fermi_microfrequency_check.py` verifies the harmonic and
non-harmonic Laguerre generating functions, the regulated pole, and the exponential
scale of the quartet; its Fourier quadrature is diagnostic. `cross_degree_h2_energy_check.py`
exactly certifies Christoffel--Darboux and the Laplace pole, and diagnostically
checks the fourth-root normalization for an interior pole.
`log_abel_fermi_boundary_check.py` verifies the Fermi limit \(1/4\) of the
quartet, the harmonic mass by progressions, and the doubly logarithmic
transition of the new Abel coordinate; its limits are proved
in `104_64`.
`diagonal_abel_regulator_gate_check.py` verifies the closed polar formula,
the diagonal constant \(C=1/100\), the scale \(C/h^2\), and the stability of
a shifted outer mode from `104_66`.
`local_filter_long_block_check.py`, `two_sided_excursion_check.py`, and
`deterministic_block_polymer_check.py` verify, respectively, the
classification of finite filters, the two signs of the quartet, and the
exact sum--product--polymer identities of the quadratic windows.
`finite_logx_diagonal_fermi_check.py` verifies the finite version of the
diagonal, the threshold \(X=70\), the value \(1/4\) of the quartet, and the
polar cost \(e^{X^2/100}\) of `104_69`.
`variable_temperature_fermi_gate_check.py` verifies the exact
characterization of the polar regulator, the temperature--detection
incompatibility, the quartet, and the diagonal scale of `104_70`.
`entropic_block_variational_check.py` verifies with rationals the telescoping
Bernoulli identity of `104_71`, and numerically the Gibbs duality, the
entropic chain rule, the combined Laguerre polynomial, and the falsifier.
`bounded_pressure_ratio_check.py` verifies the finite identities of the
bounded ratio of `104_72`, the sharp sensitivity constant
\(\tanh(\tau/4)\), the density \(1/4\) of the quartet, and the diagonal cost
\(e^{-X^2/100+O(1)}\) of resolving the transition when separating channels.
`bernstein_pressure_width_check.py` verifies the Bernstein identity, its
signs, the Mellin majorant, the curvature change, and the width--pole
incompatibility of `104_73`. `hadamard_jensen_pressure_check.py` checks the
Hadamard--Jensen identities and the exponential truncation cost of `104_74`.
`poisson_logx_hard_transition_check.py` verifies the level sandwiches, the
Bessel transform, the Poisson average of the pole, and the limits
\(4,1/4,1/8\) of the quartet in `104_75`.
`deep_tail_height_localization_check.py` verifies the quartet geometry,
the scale \(X^{1/4}\), the very high tail, and the exponential separation of
`104_76`. `cartan_turan_deep_tail_check.py` verifies the positive
rational continuation, the signs by residue classes, and the deep density
\(1/8\) of `104_77`.
`unit_renewal_euler_deep_tail_falsifier.py` verifies the collar
multiplicities, renewal, functional equation, dominant Li mode, density
\(1/4\), and the failure of the continuous PNT for the `104_78` model.
`zeta_law_deep_truncation_check.py` certifies with rationals the prime/
semiprime fibers, their opposite signs, and the quadratic scales of `104_79`;
the mass of the fibers uses PNT in the proof, not floating-point primes.

## Status

| doc | status |
|---|---|
| `104_00` | **closed.** Two routes eliminated by duplication (lcm/Stieltjes ← Coffey; model space ← Suzuki). The finite range with verified height is mostly bibliographic ground: it is not the front |
| `104_01` | **closed** (algebra + explicit Johnston--Yang PNT bound + diagnostic). Lowering \(\theta\) **gains nothing**: \(-2\theta A_n\le\mathcal N_n\le\frac12A_n\), indeterminate sign. **\(\theta=\frac14\) is fixed** |
| `104_02` | **corrected by erratum.** The bound for \(\varepsilon_n^-=A_n-\lambda_n-\lambda_n(\sqrt n)\) and its old corollaries are withdrawn. The correct small coordinate is \(\widetilde\varepsilon_n=A_n-\lambda_n+\lambda_n(\sqrt n)\); by itself it does not produce a uniform unconditional bound for A1, because now the incomplete block must be controlled from below |
| `104_03` | **closed.** Local contour and signs audited; the bare sum of trivial residues diverges and the exact canonical sum is \(\Delta A_n+(\gamma+\log4\pi)/2-1\) |
| `104_10` | **closed as local no-go.** Finite identity and exact blocks; the local-PSD version died because crossings/boundaries have no sign and the real \(H_j\) changes sign |
| `104_11` | **closed as global stop-gate.** The surviving correlator has zero Hessian: the two `max` energies cancel with the exact boundary and what remains is \(-\int E\tau'\). M1 does not contribute the inequality |
| `104_12` | **closed as M5 audit.** The degree convolution is the Laguerre pullback of \(Z^{-1}\delta Z\); Riccati adds no sign and separating norms reproduces 103_71. There is no positive metric realizing \(Z^{-1}=Z^\dagger\) on a non-trivial divisor poset. M5 contributes no new bound today |
| `104_13` | **closed as Selberg--Riccati stop-gate.** The exact recurrence preserves the pole--primes collision, but its centered coefficient cancels another piece of order \(\varepsilon^{-n-1}\). The positivity of \(\Lambda\log+\Lambda*\Lambda\) does not survive the pullback and its \(O(x)\) summation has dual norm at least \(n(n-1)^n-1\) for \(\varepsilon=1/n\) |
| `104_14` | **closed as M3 stop-gate.** Directly for A1, \(C_n^\theta=\frac12\mathcal W_\zeta(f_n*f_n^\#)-\theta A_n-R_n\). The falsifier stays within the bulk and proves the zero--lobe map contributes no sign; a special theorem for the real sequence \(\Lambda\) is still missing |
| `104_15` | **closed as minimal-complex stop-gate.** The divisor Koszul complex has a positive metric and \(d_E^2=0\); anticommutation cancels \(p/q\), but \(N_p=d_E\iota_p+\iota_pd_E\), so \(M\delta Z\) induces zero in cohomology. The scope does not include non-local complexes that do not make the \(N_p\) exact |
| `104_16` | **closed as Jordan-cocycle stop-gate.** The hierarchy \(\mu*\log^k\) is non-negative, but the pole converts it into \(D_k-kD_{k-1}/(s-1)\). The first Cayley jet satisfies \(C_1<0<C_6\) with rational intervals; the falsifier \(\xi(s+a)\xi(s-a)\) preserves the positive Euler hierarchy and functional equation with off-line zeros. The completed family \(\xi(s-u)/\xi(s)\) is Schur for all \(u\downarrow0\) if and only if RH, and its half-budget returns exactly to \(\Delta D_n\ge0\) |
| `104_17` | **closed as Abel--Fejér stop-gate of the incomplete block.** For every quartet, the radial Abel germ is positive even off-line. The exact witness \(w=2i\) has \(Q_4=-225/8\), \(F_8=-10885/128\) and, nevertheless, a positive Abel germ. No fixed-order radial average contributes the coefficient-by-coefficient lower bound |
| `104_18` | **closed as correlated-shift stop-gate.** Keeping \(u=c\varepsilon\) produces a finite non-divergent identity, but removing the regulator brings back exactly \(C_n\). The real monotonicity of \((s-1)\zeta(s)\) is compatible with \(C_6>0\); the third difference in \(c\) has the sign opposite to Hausdorff's, and the uniqueness of Dirichlet series prevents identically annihilating the explicit channel with a non-trivial finite system of constant weights |
| `104_19` | **closed as immediate-positivity stop-gate; global cocycle not ruled out.** \(A_u^2\) has coefficients \(J_u*J_u\ge0\) and Gamma a positive Beta measure, but the squared polar factor has measure \(\delta_0+c(cr-2)e^{-r}dr\), negative near zero for all \(c>0\). The three channels converge only when coupled and their limit is the strong gate \(-\Delta D_n\). The shifted falsifier shows that Jordan + Beta + functional equation do not by themselves determine the Cayley sign |
| `104_20` | **closed locally; global gate active.** The identity \(b_u(p^k)=\nabla^2((k+1)p^{ku})\) absorbs tower and channels into \(\mathsf C_p^2\), but the square is not a norm. The degree-one block changes sign as the background \(m\) varies, and every even degree has infinitely many positive blocks. An uncertified diagnostic keeps \(g_n<0\) up to 1200; proving the sign of the global sum, preserving interactions between primes, is the live front |
| `104_21` | **closed as global PF/TP/CM stop-gate.** \(\log N\) has an exact compound-Poisson measure increasing in \(u\), but the exponent lattice fails PF2 with minor \(-1/2916\). For \(u=1,\varepsilon=2\), the inverse Laplace of the full arithmetic--Gamma--polar cocycle has negative density at \(\frac12\log2\); there is no positive probabilistic representation that transfers the order to the gate. The global sign of \(g_n\) is neither refuted nor proved; the concrete successor is a signed Stein--Mecke inequality for the completed Laguerre test |
| `104_22` | **reduction closed; cubic gate active.** The exact A0 estimate preserves \((1+T_n)^{-1}\), so \(D_n^{[3]}=3\lambda_n-A_n\ge0\) implies \(C_n(T_n)\ge0\) for \(T_n\ge2\). It is strictly weaker than the quadratic margin. The cocycle \(Y_3(s-u)/Y_3(s)=H_u^3K_u^2\), normalized by \(u(1-z)^2\), converges directly to \(-D_n^{[3]}\); the diagnostic remains negative up to index 1201, but proving its global sign is still missing |
| `104_23` | **reduction closed; near-quartic gate active.** Since \(T_n\ge1000\), it suffices that \(D_n^{[r_*]}=r_*\lambda_n-A_n\ge0\), \(r_*=2002/501\), equivalent to requiring only \(\lambda_n/A_n\ge501/2002\). The real powers of Euler and Gamma preserve positive measures; the real pole is signed. It is the weakest uniform margin obtained so far using only the declared cutoff floor; absolute optimality is not claimed |
| `104_24` | **four channels closed; positive Stein ruled out.** The direct normalization has base \(k+1\) and exact limit \(-(3\lambda_{k+1}-A_{k+1})\). The Lévy measure \(\nu_A^{[3]}+2\nu_K-3\nu_P\) enters a global Stein--Laguerre recurrence, but is negative on an interval before \(\log2\), even in the regulated limit. Only a specific non-local signed cancellation remains open |
| `104_25` | **Fejér closed; circular global gate ruled out.** If \(\Re\Phi\le1\) on the disk, Herglotz--Fejér gives all the signs of the cubic margin. But the holomorphy of \(Y_3(s-u)/Y_3(s)\) on those disks as \(\varepsilon\downarrow0\) is already equivalent to RH. The safe Euler radius tends to zero and an exact polynomial witness prevents transferring its sign to the coefficient without damping |
| `104_26` | **quartic attack closed as SOS no-go.** \(J_u^{*4}\) gives an exact fourth difference, but fails PF2 and the complete blocks change sign. The formal square \(H_u^4K_u^3=(H_u^2K_u^{3/2})^2\) linearizes when \(u\) is removed. The margin \(4\lambda_n-A_n\ge A_n/1001\) corresponds to the fixed cutoff based only on \(T\ge1000\); `104_56A` withdrew its claimed intrinsic necessity |
| `104_27` | **tail sign ruled out from A0/VK.** Beyond the last Laguerre zero, two functions saturating the same envelope give \(R_n(T)\) strictly positive and strictly negative. The witness can be smoothed and preserve eventual monotonicity; it does not preserve prime support, which is precisely the new input that would be needed |
| `104_28` | **fixed-vector bridge closed; \(v_{\max}\) diagnostic ruled out.** The Li test is exactly the hard-edge reproducing-kernel state \(g_n/\sqrt n\) and the prime sum is an Abel-renormalized form on that ray. The old whitened operator lives in another gauge; the natural polarization of \(A_n\) is indefinite, and the reference Gram normalizes by \(n\), not by \(A_n\). There is no faithful almost-extremal projector without first constructing a new closed renormalized form |
| `104_29` | **\(\log2\) cut closed as identity, mass balance ruled out.** The valid version uses \(\varphi_n=L_{n-1}^{(1)}-n\) against the compensated generator. The outer block preserves all primes, but the bound needed on it is algebraically \(D_n^{[r]}\ge0\). Separating pole and primes costs \(\varepsilon^{-n}\) and repeats 103_53--103_57 |
| `104_30` | **flag reference closed; spectral inequality open.** The diagonal positive form evaluates \(A_n\) exactly over every prefix and allows the faithful finite-section quotient. The mass diagnostic is favorable, but not certified; the Schur/Gershgorin bounds lose the cancellation and require the signed control of \(\Delta^2(A_n-\lambda_n)\), which is not proved |
| `104_31` | **flow in \(\varepsilon\) closed as Hilbert stop-gate.** The unitary realization is \(Q=-M_x\). There is no regulator simultaneously safe for the separated Euler operator and for the inverse prefix transport. The reference \(A_{\rm flag}\) leaks outside its flag, does not symmetrize \(Q\), and preserves exactly the boundary \(1/2\). The coupled, renormalized form of `104_30` is not ruled out |
| `104_32` | **higher powers removed from the regularization; prime--pole gate open.** The block \(k\ge2\) converges ordinarily and satisfies \(\lvert P_{n-1}^{(\ge2)}(1)\rvert<14n+1=o(A_n)\). In the quartic margin it enters with factor \(-4\), and its absorption by absolute value into \(A_n/1001\) is only proved from \(n\ge e^{112116}\), not from \(150\). The remaining exact obligation is the prime--pole inequality (26) of `104_32` |
| `104_33` | **symbol closed; boundary-only proof ruled out.** Every zero with \(\Re\rho>1/2\) contributes exactly \(m_\rho\mathcal F_n(w_\rho)/[\rho(\rho-1)]\) to the moment. A reciprocal quartet leaves the real boundary identical and changes \(B_n/A_n\) exponentially; a proof must control the signed sum of residues with specific arithmetic, not assume Hardy holomorphy |
| `104_34` | **curvature domination ruled out; adjacent compression open.** The ansatz \(q_d(B)\le(1501/2002)q_d(A)\) fails rigorously at \(d=220\), already within the infinite range. The exact flag compression produces \(\mathcal T_n=4H_nd_n-(H_n+d_n-H_{n+1})^2\); proving \(\mathcal T_n\ge0\) for all \(n\ge149\) propagates the finite certificate and closes the margin, but that signed theorem is not proved |
| `104_35` | **\(\theta\) channel closed as identity; simple Selberg ruled out as coercivity.** The correct boundary is \(-n\), and obligation (26) of `104_32` becomes an exact \(\theta-x\) correlation. The Selberg measure of primes/semiprimes is positive, but its Hankel inverse has both signs. Even with support on the real primes, PNT and the Selberg scale do not fix the functional if a weight is altered; only a global theorem for the canonical weights \(\log p\) remains open |
| `104_36` | **prime--pole Cholesky built and ruled out as norm closure.** For \(a>2\) the norm preserves all interactions within \(\lvert(s-1)^{-1}-Q(s)\rvert^2\). Its Laplace transform has, at \(z=\rho/a-1/2\), residue \(m_\rho[1-(1-a/\rho)^n]\): two consecutive \(L^2\) prefixes already exclude \(\Re\rho>a/2\), and critical zeros force \(\|V_{n,a}\|_2^2\gg(a-1)^{-1}\). Only a one-sided bound of the signed projection survives, not of the norm |
| `104_37` | **the adjacent taper is closed as identity and ruled out as Hankel energy.** The form in \(g_n+t\phi_n\) preserves exactly the archimedean block, higher powers, and prime--pole. The collective inversion gives a kernel whose minor on \(\{R,2R\}\) is \(C^2e^{-6aR}R^{2d}(8^d-9^d+O(R^{-1}))<0\) for all \(t\), including \(t_n^*\). \(\mathcal T_n\ge0\) remains open via a special cancellation of the canonical weights, not via Hankel PSD |
| `104_38` | **the Selberg completion of the Schur square is ruled out.** Keeping the full centered identity, \(-\langle G,\mu*\mu\rangle+\mathcal Q_G(\mu)=0\) exactly. If \(\mathcal Q_G\) is reserved to dominate the crossed entry, the difference kernel is already negative on a single canonical prime atom in the tail; moreover the square of the crossed response is not Hankel, with collision defect \(-2n^2a^4x^2+O(x^3)\). Only the joint signed value for the whole canonical measure remains open |
| `104_39` | **adjacent Riccati closed as necessity stop-gate.** The determinant is equivalent to the triangular inequalities for \(\sqrt{H_n},\sqrt{d_n},\sqrt{H_{n+1}}\). An on-line quartet keeps \(H_n>0\) and breaks the gate exactly, so the gate is stronger than the objective; under RH it is indeed positive for all sufficiently large \(n\). Optimizing the reference gives the circular optimum \(D=H_n+H_{n+1}\), and the orthogonal-prefix reference only changes \(\Delta B_n\) by \(B_n+B_{n+1}\). The gate for zeta is not ruled out, but it stops being the only front |
| `104_40` | **canonical Euler resolvent ruled out as commutative quadratic bound.** On the fixed ray, the optimal positive preconditioner replaces \(\Re M\) by \(-|M|\). Its cost diverges like \(\log(1/(a-1))\) from a non-resonant critical zero, while an off-line zero forces adding the residue upon crossing \(a=2\Re\rho\). Only a signed/non-commutative estimate or the criterion \(\mathcal T_n\ge0\) survives |
| `104_41` | **complete phase bound proved on the Euler half-plane; transport ruled out without residues.** With \(F=(s-1)\zeta(s)\), \(\mathcal B_{n,a}=-(2\pi)^{-1}\int W_n\,d\arg F\), \(\mathrm{TV}(W_n)=8n\), and \(|\arg F|<3\pi/4\) give \(|\mathcal B_{n,a}|\le3n\) for \(a\ge4\). Transport to \(a=1\) crosses exactly the zeros with \(\Re\rho>1/2\); the defect is the signed sum of residues. The quartet \(w=i/2\) leaves the whole on-line phase identical and contributes \(2(2^{152}+2^{-152})-4>0\) to the defect. A specific theorem for the exact weights \(\Lambda(m)\) controlling those residues is still missing |
| `104_42` | **non-commutative quadratic optimization ruled out; degree compression closed as stop-gate.** For the full Euler--pole operator, with all \(\Lambda(p^k)\), the algebraic infimum over every positive preconditioner is exactly \(|B_n|\); in the dangerous regime it returns the objective itself. If the vector continuation is in \(L^2\), every bounded cost requires \(\mathrm{cond}\,R\gg(a-1)^{-1}\). Projecting the first \(n\) states preserves phase and gives an exact formula in \(\Delta B_j\), but the new datum enters with gain \(\sqrt{n/2}>1\). A new arithmetic bound for an explicit \(R\) is not ruled out; optimization alone does not supply it |
| `104_43` | **size-biased factorization closed; order and separate energy ruled out.** The canonical divisor selector preserves exactly all the \(\Lambda(p^k)\), but lies above the uniform selector at \(n=2\) and below it at \(n=30\). Its marginal error is exactly \(R\), and the Efron--Stein energy of the unscaled Laguerre diverges like \(\{\binom{2n-2}{n-1}-1\}\varepsilon^{-2n+2}\). Only a cross, signed, non-monotone comparison remains open |
| `104_44` | **divisor--Markov transport closed as operator and scale stop-gate.** The `104_43` disintegration has norm one even at mean zero, so no global gap exists. The Gamma continuum does contract \(L_r(\varepsilon x)\), but recomposing \(L_r(x)\) carries a charge \((2/\varepsilon-1)^r\); for \(\varepsilon=1/n\) this reproduces the wall \(\exp(n\log n)\). A special estimate preserving the whole alternating sum is not ruled out |
| `104_45` | **crossed coupling closed as identity and local stop-gate.** The Stein kernel is unique and independent of the coupling. It has pattern \(-,+,-\) around \(\log2\). The order \(R(q)<0\) holds for exponentials and their positive mixtures, but \(-R\) is not completely monotone; the Laguerre test recomposes exactly \(B_n\) |
| `104_46` | **fixed-vector non-alignment ruled out.** For all \(s\in(1,s_0)\), the centered arithmetic Laguerre ratio converges to one; the split-Gamma one converges to zero. The centered ratios are also translation-invariant and do not observe the signed mean difference |
| `104_47` | **size-biased flow closed as stop-gate.** The homotopy satisfies an exact equation between degrees, but integrating the flow gives \(\mathcal B_{n,a_0}-B_n\); requiring the needed sign is exactly the original margin. Generic positivity/Markov also holds for \(\zeta(s+c)\zeta(s-c)\) with off-line zeros |
| `104_48` | **tower-by-tower phase closed; local multiplicity ruled out.** The Poisson formula gives only a non-summable minorant and also accepts the shifted weights. A full tower of multiplicity \(1+t\) preserves support, constancy, and PNT, but violates any proportional ceiling at \(n=151\). The only unfalsified input is the full unit renewal \(\Lambda*{\bf1}=\log\) |
| `104_49` | **unit renewal closed as linear identity; coercivity still open.** The geometric Palm uniformly selects one height of the tower, a property \(\omega_c\) loses. However, at each degree the selector defect \(\kappa_r-m_r/r\) and the transport \(m_r/r-(r-1)!\varepsilon^{-r}\) exactly cancel \(m_r\), and the Laguerre recomposes \(B_n\). The conditioned defect already has both signs at \(n=151\). Only a non-linear correlation between several towers that does not vanish upon averaging survives |
| `104_50` | **Palm covariance closed as stop-gate.** The centered kernel diagonalizes by tower. Keeping the total defect gives \(\mathrm{Cov}(D_f,D_g)+M_s(f)M_s(g)\); for the real test, completing the square produces variance plus \((\mathcal B_{n,s}-\kappa A_n)^2\). Derivative, primitive, and score revert to unknown coefficients or to the already open flow |
| `104_51` | **quadratic Möbius inversion closed as stop-gate.** The congruence \(M^TKM=W\) eliminates every `lcm` correlation. For the infinite kernel, the difference between the energies is indefinite on a two-level vector; for \(P_{150}\), the local divisor cutoff has opposite signs at \(p=2,7\). That sign is not claimed for the infinite form on the fixed Laguerre. Polarizing the diagonal returns to a difference of squares without orientation |
| `104_52` | **connected two-tower flow ruled out.** The exact Hessian of the margin preserves tower, pole, and Gamma, but the logarithmic projection cancels every pair of distinct towers with coefficient zero. It changes sign between \(s=1\) and \(s=10\), and its Laguerre cocycle also has both signs |
| `104_53` | **additive polynomial hierarchy classified.** In the universal algebra of moments, the primitives are exactly the linear combinations of cumulants. Since the zeta cumulants are sums over a single tower, no finite-order additive polynomial identity can preserve a multi-tower reserve. The theorem does not cover arbitrary non-additive inequalities |
| `104_54` | **Gibbs/Chernoff rigorously ruled out.** The unit Laguerre defect has arithmetic tails of both signs and order \((\log N)^n\), while the zeta law only decays like \(e^{-s\log N}\). All its non-trivial exponential moments diverge; adding pole or budget only shifts by a constant |
| `104_55` | **canonical cubic forms ruled out.** The three-mark Palm preserves the disconnected moment, but the third central moment has no sign, the alternating determinant averages to zero, and its square is generic. Every orientation obtained by multiplying an independent copy by a positive energy factors exactly as energy times the margin. Only a non-canonical non-additive inequality correlating the local unit reflection with the total integer before the connected projection remains outside the no-go |
| `104_56` | **quantifier rigorously reduced.** Under \(\neg\mathrm{RH}\), the margin failures contain a syndetic set of positive density. It suffices to prove good blocks of unbounded length or an exception of logarithmic density zero. This reduces the objective, but does not yet supply those blocks for zeta |
| `104_56A` | **cofinal correction closed.** The cutoff can grow with \(n\) and with the slack; \(4\lambda_n>A_n\) closes A1 at an adapted cutoff. \(A_n/1001\) is not an intrinsic slack. The adaptation does not prove the slack it uses |
| `104_56B` | **antecedent audit closed.** The dominant-mode/infinite-excursion part is already in Bombieri--Lagarias and later works. The topological reinforcement to positive density/syndeticity and the prime--Laguerre Fermi lift did not appear explicitly in the directed primary search; they are recorded as not located, not as established priority |
| `104_57` | **low block isolated.** The RH-strength obligation stays at \(\asymp\sqrt n\log n\) labels below \(\sqrt n\), with transport error of the same scale and an explicit budget criterion. No new lower bound was obtained |
| `104_58` | **fixed translational average ruled out.** Every fixed window preserves the outer modes and fails on positive density under \(\neg\mathrm{RH}\). The Euler phase at \(a\ge4\) also fails to control those failures when crossing to \(a=1\) |
| `104_59` | **classical majorization ruled out.** The unlabeled masses lose \(m\mapsto\log m\), the Laguerre terms have no global curvature, and the divisor selector reverses orientation. Only the same specific signed global comparison for \(\Lambda\) survives |
| `104_60` | **non-linear barrier built; estimate open.** For any \(b_n=e^{o(n)}\), RH is equivalent to the saturated negative depth having mean zero on a sequence of long intervals. The criterion passes the quartet and stays outside 104_17/104_53, but proving its mean for zeta is still missing |
| `104_61` | **exact partitions built; bounds open.** RH is already equivalent to \(\lambda_n\ge-1\) on unbounded blocks and to the bounded Fermi partition \(\mathfrak F_{t,b}(X)\) tending to zero. Its paired prime--Laguerre form is exact and preserves the density relaxation. \(\mathcal Z_t(X)=O_t(\log X)\) remains as a stronger auxiliary criterion that does imply a degree-by-degree bound |
| `104_62` | **unitary Fermi lift built; diagonal branch closed.** The signal of an excursion \(-Y\) lives at \(s=O(Y^{-1})\), so every polynomial resolution fails on the quartet. The change \(s=e^{-nv}\) fixes that rate, but the radial generating function sees a geometric product, not the arithmetic mean; at the boundary there is no finite-order truncation |
| `104_63` | **cross-degree energy closed as no-go.** \(\limsup \mathcal E_N^{1/(4N)}=1/r_0\) localizes exactly the first transformed pole. Parseval/CD preserves the complete square, but every separated estimate loses a cancellation of order \(\varepsilon^{-4N}\) |
| `104_64` | **exact logarithmic Abel; microfrequency truncation closed.** The Cesàro Fermi average tends to zero if and only if its Abel average does; even a radial subsequence suffices. The infinite outer prime--Laguerre lift is exact. In the quartet, the bad correction obeys a uniform law in \(\alpha=\log\log(1/s)/\log(1/h)\), and capturing it completely requires reaching \(s=\exp(-c/h)\). A prior cancellation among all channels is not ruled out |
| `104_65` | **local filters classified and closed.** Every finite filter that does not annihilate the outer modes preserves negative exponential excursions on a syndetic set; fixed differences and moving averages do not fabricate good blocks. An exact annihilator can hide the quartet, so it is not a faithful detector either |
| `104_66` | **regulator--Abel diagonal proved; separation closed.** With \(\varepsilon(h)=e^{-1/(100h)}\), \(\lambda_{n,\varepsilon(h)}\to\lambda_n\) uniformly for \(n\le1/h\), and the Fermi criterion can be formulated with a single absolutely convergent Euler series. Separating pole and primes requires relative precision \(\exp(-C/h^2+O(1/h))\); the full product returns to the unknown Fermi phase |
| `104_67` | **two-sided dichotomy proved.** If RH is false, there are positive and negative excursions of the same maximal exponential rate on respective syndetic sets of positive density. Consequently an upper, lower, or two-sided subexponential barrier on blocks of unbounded length suffices; transporting the upper Euler bound from \(a\ge4\) to \(a=1\) crosses the same off-line residues |
| `104_68` | **block selector and double limit eliminated.** The deterministic windows \(I_L=[L^2,L^2+L-1]\) suffice: the Fermi sum tends to zero and the associated product to one under RH, while under non-RH the sum has \(\liminf\ge1\) and the product tends to zero. With \(\varepsilon_L=e^{-(L^2+L-1)/100}\) a single convergent Euler family remains. The prime--Laguerre gas is still non-interacting; proving its bound is open |
| `104_69` | **finite \(\log X\) criterion and Euler diagonal proved.** RH is equivalent to \(H_X^{-1}\sum_{n\le X}[n\{1+(n+1)e^{\lambda_n}\}]^{-1}\to0\). With \(\varepsilon_X=e^{-X/100}\), the first \(X\) coefficients are uniformly approximated and a single absolutely convergent prime--Laguerre formula remains. The quartet gives \(1/4\); separating pole and primes costs precision \(e^{-X^2/100+O(X)}\) |
| `104_69B` | **novelty audit closed.** Li/Bombieri--Lagarias/Bucur et al. already contain the exponential-excursion mechanism, Palojärvi is adjacent via finite intervals, and Bingham--Gashi contains the log-Cesàro/Abel layer. The exact Fermi--block--product--diagonal form was not located; it is recorded as a repackaging/corollary, not as a priority. The potentially substantive piece is the density/syndeticity reinforcement of `104_56`, if its proof remains intact |
| `104_70` | **variable temperature built; polar saving ruled out.** \(t_n=e^{-\sqrt n}\), \(b_n=e^{2\sqrt n}\) preserves a Fermi criterion equivalent to RH. In general, if \(\varepsilon_n\to0\) and \(t_n|p_n(\varepsilon_n)-1|\) stays bounded, then \(t_nR^n\to0\) for all \(R>1\); this contradicts the sensitivity required to every off-line mode. The coupled lift exists, but the relative cost remains \(e^{-X^2/100+O(X)}\) |
| `104_71` | **exact entropic duality; interaction refactored.** \(P_L^{-1}=C_L\mathbb E_{\nu_L}e^{-\sum B_n\lambda_n}\) and Gibbs reduces the full supremum to Bernoulli profiles \(q_n\). Entropy creates no interaction: every correlation pays multi-information. Under non-RH the logarithm grows at least like \(cR^{L^2}\); hence a uniform bound with slack \(\exp(o(L^2))\) on a subsequence suffices. The bound for the real weights remains open |
| `104_72` | **bounded pressure ratio built; paired transition open.** For \(g_\tau(x)=\tau^{-1}\log\{(1+e^{-x})/(1+e^{-x-\tau})\}\), RH is equivalent to \(\sum_{n\in I_L}g_\tau(\lambda_n+\log(n+1))\to0\). Each site contributes a factor between \(1\) and \(e^\tau\), so, unlike `104_71`, exponential depth saturates and only the excursion density survives. The diagonal prime--Laguerre lift is exact, but the band \(z\asymp1\) requires the prime--pole difference with additive error \(O(1)\), i.e. relative precision \(e^{-X^2/100+O(1)}\) if channels are separated. The quartet gives density \(1/4\); the bound for the real weights remains open |
| `104_73` | **Bernstein representation closed; affine, Jensen, and variable-width rescues ruled out.** The positive measure has mass \(\tau\), but its moments return to the exponential partitions. The effective width is \(w(\tau)=\tau/\tanh(\tau/4)\); transporting a block of \(L\) sites requires uniform error \(o(w/L)\). Any width sensitive to every \(R^X\) preserves the cost \(e^{-X^2/100+o(X)}\); a width that absorbs the pole destroys that sensitivity |
| `104_74` | **Hadamard--Jensen built; interior residue isolated.** \(\sum e^{-t\lambda_n}z^n\) is entire of order \(2/t\) under RH and has zero radius under non-RH. The pressure is an exact mixture of Jensen increments. A common contour for \(N\le n\le2N\) leaves a term \(O(N^5\log^2N)\) and the finite sum of poles \(|w_\rho|<r_N\); no estimate obtained eliminates that sum. The Hadamard truncation needs order \(\Theta(2^n)\) in the quartet |
| `104_75` | **hard, deep criterion proved; arithmetic bound open.** For any \(0<\alpha<1\), RH is equivalent to the indices with \(\lambda_n+\log(n+1)\le-e^{X^\alpha}\) having logarithmic density tending to zero. With \(\alpha=1/2\) and \(\varepsilon_X=e^{-X/100}\), this is exactly the event \(Q_{n,\varepsilon_X}\ge A_n+p_n(\varepsilon_X)+\log(n+1)+e^{\sqrt X}\). Poisson and Bessel close the first moment, but the quartet gives first moment \(4\) and nonlinear tails \(1/4\) and \(1/8\); the density estimate for the real weights is not proved |
| `104_76` | **high tail closed in absolute value; low block open.** By functional quartets, \(\sup_{n\le X}|\lambda_n^{(\gamma>X^{1/4})}|\ll X\log X\,e^{\sqrt X/2}\). If RH is verified up to \(X^{1/4}\), the deep indicator is zero at every degree \(n\le X\). Markov and the second moment already have margin after removing that block; without removing it, a single fixed outer quartet produces positive density |
| `104_77` | **complex reduction closed; sum of residues open.** A safe radius gives \(\lambda_n=C_{n,n}-Z_n\) with \(C_{n,n}=O(n^5\log^2n)\), so the deep criterion is equivalent to a one-sided tail of the finite sum \(Z_n\). Jensen measures the interior mass, Cartan can remove it, and Turán forces its excursions; none proves it is zero. The quartet \(w=2i\) has positive continuation on \(0<r<1\) and deep density \(1/8\) |
| `104_78` | **lattice Euler falsifier validated; scope delimited.** The formal monoid has primes with integer multiplicity, unit towers, exact renewal, FE, and a degree law \(6^k+1-3^k-2^k\), but off-line zeros and deep density \(1/4\). It does not satisfy continuous \(\psi(x)\sim x\): it is lattice-based and has periodic poles on \(\Re s=1\). Hence it rules out only universal theorems based on the preserved discrete axioms |
| `104_79` | **exact zeta-law representation; separate truncation ruled out.** \(Q_{n,\varepsilon}-p_n(\varepsilon)=\mathbb E[J_n(N)-U_n(Y)]\). On the diagonal and for \(X/2\le n\le X\), the positive and negative excesses above \(e^{\sqrt X}\) are \(\ge e^{X^2/500}\), already over real prime and semiprime fibers. This prevents concentration plus separate truncation error over the tails; it does not exclude a signed identity cancelling them jointly |
| `104_80` | **joint identity found; negative closure.** \(\sum_{n\ge1}(Q_{n,\varepsilon}-p_n(\varepsilon))z^{n-1}=-\partial_z\log\{(s_\varepsilon(z)-1)\zeta(s_\varepsilon(z))\}\). The Möbius involution cancels the multiprime fibers, but a zero \(\rho\) produces the pole \(z_{\rho,\varepsilon}=(\rho-1-\varepsilon)/(\rho-\varepsilon)\) with coefficients \(m_\rho z_{\rho,\varepsilon}^{-n}\). An exact regrouping cannot erase it by meromorphic uniqueness; the deep limit remains unproved |

| 104_81 | **adversarial detector validated.** For the quartet \(\{i,-i,i,-i\}\), \(\ell_n=4-4\cos(\pi n/2)\ge0\) and the deep density is \(0\). For \(\{Ri,-Ri,i/R,-i/R\}\), \(R=201/200\), only \(4\mid n\) produces \(-\Theta(R^n)\) and the density is \(1/8\); \(R<e^{1/100}\) preserves the result under \(\varepsilon_X=e^{-X/100}\). An additional pair of Euler products with non-negative prime multiplicities separates \(0\) (all zeros on-line) from \(1/4\) (off-line zeros). This rules out tautology and sign error, but does not establish the limit for the real zeta |

**Objective, in its exact form** (independent of Lagarias, \(\theta=\frac14\)):
\[
\int_{\log2}^{T_n}\bigl(\psi(e^u)-e^u\bigr)e^{-u}L_{n-1}^{(2)}(u)\,du
\ \le\ \tfrac34A_n+1-L_n^{(1)}(\log2)
\qquad(n\ge150),\ \text{unconditionally},
\]
equivalently
\[
 A_n-\lambda_n+R_n(T_n)\le\tfrac34A_n
 \iff
 \lambda_n\ge\tfrac14A_n+R_n(T_n).
\]
In the corrected incomplete coordinate, the same inequality is
\[
 -\lambda_n(\sqrt n)+\widetilde\varepsilon_n+R_n(T_n)
 \le\tfrac34A_n.
\]

**Two recorded traps, not to be repeated:**
1. There is no unconditional bound
   \(|A_n-\lambda_n-\lambda_n(\sqrt n)|\ll\sqrt n\log n\). The small remainder has the
   opposite sign, \(A_n-\lambda_n+\lambda_n(\sqrt n)\), and using the old remainder as the small one introduces
   exactly RH-strength content.
2. For A1, \(\lambda_n>0\) is not enough: the exact condition is
   \(\lambda_n\ge A_n/4+R_n(T_n)\). The old coarse bound of A0 made
   the **strong margin** \(2\lambda_n-A_n\ge0\) sufficient, but not necessary.
   For a prescribed cutoff, retaining the A0 factor, the margin depending
   on \(T_n\) suffices; the value \(r_*=2002/501\) is only the uniform version
   obtained from the floor \(T\ge1000\). If the cutoff is allowed to grow after
   a positive slack is known, \(4\lambda_n>A_n\) is sufficient. Separately,
   \(4\lambda_n-A_n\ge0\) for all indices already proves RH directly and does
   not need to go through A1.

**New master front.** To close the literal statement of this phase, A1
is still needed for every \(n\ge150\). To prove RH, a much weaker
objective now suffices: for example \(\lambda_n\ge-1\) on consecutive blocks of
unbounded lengths, or, for \(b_n=\log(n+1)\) and some \(t>0\), the limit
\[
 \mathfrak F_{t,b}(X)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 {1\over1+e^{t(\lambda_n+b_n)}}\longrightarrow0.
\]
`104_61` gives an exact arithmetic representation of that partition keeping
pole, Gamma, primes, and prime powers coupled. No current document
yet proves the limit for the real zeta. The bound
\(\mathcal Z_t(X)\ll_t\log X\) remains available as an auxiliary target, but it is
coefficient-by-coefficient and not the density front. `104_62` and
`104_63` record that unitary Fourier, diagonal scaling, Parseval, and
Christoffel--Darboux do not contribute that estimate either. `104_64` allows searching
for the limit over a single Abel subsequence, but proves that truncating the layer
before \(s=\exp(-c/h)\) loses an order-one contribution in the
falsifier. `104_68` eliminates even the choice of intervals: it suffices to
prove
\[
 \sum_{n=L^2}^{L^2+L-1}{1\over1+(n+1)e^{\lambda_n}}\longrightarrow0,
\]
equivalently that the complementary product tends to one. `104_69`
eliminates the double limit of the global front: with \(\varepsilon_X=e^{-X/100}\),
RH is equivalent to a single finite average over \(n\le X\) tending to zero, whose
prime--Laguerre input is absolutely convergent for each \(X\). The
bound for either of these two expressions for the real weights
\(\Lambda(m)\) remains open and is exactly the RH-strength content.
`104_71` weakens the window target even further: proving the zero
limit is not needed. It suffices to bound, on a subsequence, the combined entropic
supremum against \(G_{L,q}=\sum q_nL_{n-1}^{(1)}\) by any
\(B_L=\exp(o(L^2))\). The duality proves this formulation is exact, but
also that entropy alone does not supply the bound.
`104_72` better preserves the original relaxation: it suffices to prove
\[
 \sum_{n\in I_L}{1\over\tau}\log
 {1+e^{-(\lambda_n+\log(n+1))}
  \over1+e^{-(\lambda_n+\log(n+1)+\tau)}}\longrightarrow0.
\]
The observable is a pressure ratio with uniformly bounded factors;
under non-RH it grows linearly in the number of bad sites. Its diagonal
Euler form is closed, but the bound for \(\Lambda(m)\) remains the only
RH-strength input.
`104_73` and `104_74` directly audit that last claim: Bernstein,
Jensen, variable width, and Hadamard exponentiation give exact representations,
but not an upper bound for the already-cancelled difference. `104_75` reduces the
target even further. With
\[
 \varepsilon_X=e^{-X/100},\qquad
 Q_{n,\varepsilon}
 =\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m),
\]
it suffices to prove
\[
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\left\{
 Q_{n,\varepsilon_X}\ge
 A_n+p_n(\varepsilon_X)+\log(n+1)+e^{\sqrt X}
 \right\}}\longrightarrow0.                              \tag{Deep-\Lambda}
\]
This statement only excludes overshoots of size \(e^{\sqrt X}\) in positive
logarithmic density; it asks for no sign, no \(O(1)\) transition, and no
degree-by-degree control. It is the weakest arithmetic target in the ledger and is
equivalent to RH.
The Poissonized Bessel identity controls only the first moment;
the quartet gives an innocuous first moment and, simultaneously, a deep tail of
positive density. No current document proves (Deep-\(\Lambda\)) for the
real weights.
`104_76` does unconditionally eliminate the tail
\(\gamma>X^{1/4}\) with margin \(e^{\sqrt X/2}\): if the zeros of the block
\(\gamma\le X^{1/4}\) are on the line, the indicator is zero at every
degree \(n\le X\). `104_77` confirms from the contour that this low block
is exactly the finite sum of interior residues; Jensen, Cartan, and Turán
detect it but do not contribute the one-sided bound. Hence the front no longer
contains high zeros, a conditional tail, or a first-moment problem:
it contains only the arithmetic exclusion of a low interior pole.
`104_78` shows that unit renewal, towers, positivity, FE, and a
strong prime **degree** law still allow that pole; the model stops being
comparable exactly at the continuous PNT, ordinary support, and Gamma. `104_79`
already uses the zeta law and the real \(\Lambda(m)\), but proves that its prime
and semiprime tails before averaging have bilateral excesses
\(e^{\Theta(X^2)}\). Hence truncating or concentrating them
separately does not work either. Only a joint signed cancellation, specific
to the ordinary location \(\{\log p\}\), the pole, and Gamma, survives.
`104_80` carries out that joint cancellation at the identity level:
\[
 \sum_{n\ge1}(Q_{n,\varepsilon}-p_n(\varepsilon))z^{n-1}
 =-\partial_z\log\{(s_\varepsilon(z)-1)
                     \zeta(s_\varepsilon(z))\}.
\]
The Möbius involution exactly eliminates the multiprime fibers, but leaves
the towers \(p^k\), and every outer zero reappears as an interior pole of
positive residue. By meromorphic uniqueness, no exact rewriting of that
convolution can supply the bound: the successor would have to be a
new inequality on the location of the ordinary primes, not another
algebraic identity.

**Source policy** (`104_00` §7): arXiv, Zenodo, institutional repositories, and peer-reviewed
journals are admissible for importing results. ResearchGate, Academia.edu, and
viXra do not justify any lemma, but are recorded and compared as possible
priority antecedents.

104_81 subjects that observable to two adversarial controls. The critical
quartet annihilates it exactly, while the outer quartet of radius
\(201/200\) produces density \(1/8\) and remains stable under the diagonal
\(\varepsilon_X=e^{-X/100}\). A second pair with Euler products and
non-negative prime multiplicities likewise separates density \(0\)
(all zeros on the line) from \(1/4\) (zeros off it). This
verifies that the gate detects the correct phenomenon and is not a tautology
of the normalization. These controls do not prove its vanishing for the
ordinary weights \(\Lambda(m)\).

`104_82` eliminates the rational independence of the lengths as a possible
missing input. The toral lift gives Haar and Parseval, but the
*untwisted* evaluation is unbounded; moreover, the outer Euler model can be deformed
to totally \(\mathbb Q\)-independent lengths without losing its positive
deep density. `104_83` performs the complementary theta audit: all
cumulants enter Deep-\(\Lambda\), the theta tail pointwise smaller
than \(1/300\) cancels one hundred percent of the first mode's boundary
jets, and neither modal dominance, finite PF, nor a one-sided imaginary part
control the complete transform.

`104_84` canonically identifies the remaining obstruction. For
\(E(z)=(s(z)-1)\zeta(s(z))\), \(s(z)=(1-z)^{-1}\), Deep-\(\Lambda\) is equivalent
to the absence of its interior Blaschke factor. Jensen gives exactly
\[
 {1\over2\pi}\int_{-\infty}^{\infty}
 {\log|\zeta(1/2+it)|\over t^2+1/4}\,dt
 =-\log B(0)\ge0,
\]
and RH is equivalent to equality. The same document proves that every local
analytic Euler identity —Möbius, *squarefree*, \(\zeta(2s)\), or a
finite combination— preserves that interior factor or also erases the
observable. Hence the only successor not ruled out is a genuinely non-local
inequality for the ordinary primes proving \(B(0)=1\).

`104_85` proves that the two immediate non-local realizations preserve
exactly the same obstruction. A renormalized *all-primes* product is
entire, zero-free, and converges to \((s-1)\zeta(s)\) up to \(\Re s=1\); its
uniform local convergence on \(\Re s>1/2\) is equivalent to RH by Hurwitz. The
Nyman--Báez-Duarte form keeps all interactions via the
PSD kernel \(1/\max(m,n)\), but every right-hand zero forces a distance
\((2\beta-1)/|\rho|^2\). Proving that distance vanishes again amounts
exactly to \(B\equiv1\).

`104_86` tests a different single-sign coordinate. The Bose kernel
\(q(x)=x^{-1}-(e^x-1)^{-1}>0\) satisfies
\(-\Gamma(s)\zeta(s)=\int x^{s-1}q(x)dx\) and the exact self-reflection
\[
 q(x)={1\over\pi}\int_0^\infty q(t)
       \sin\!\left({xt\over2\pi}\right)dt.
\]
The sine operator is necessarily signed. The kernel is PF2/log-concave
on a logarithmic scale, but fails complete monotonicity with the exact minor
\(-1/144\), and is not infinitely PF. An explicit positive mixture preserves
sign, monotonicity, asymptotics, and the same self-reflection, but introduces
off-line quartets. Hence these properties do not force the
Deep-\(\Lambda\)=0 case either.

`104_87` closes the audit of the Nyman finite section without reopening
Hurwitz as a front. The inversion of \(1/\max(m,n)\) is tridiagonal and the
identity \(\mu*1=\delta\) exactly annihilates the residual on
\((1/N,1]\). All the energy stays in a positive tail of floors. Its
first block contains exactly
\(M(m)-M(N)+N\sum_{k\le N}\mu(k)/k\); PNT does not control the quadratic scale
needed. The inverse resolves the prefix, not the tail.

`104_88` returns to the direct observable and produces a reproducible
visualization. The ordinary zeta has deep indicator zero in the stable
diagnostic range \(n\le2000\); the outer quartet grows toward its exact
limit \(1/8\). It also proves the relevant uniqueness: any meromorphic
function with the logarithmic derivative of the ordinary \(\Lambda(m)\) and the
same normalization is \(\zeta\) itself. Hence there is no
distinct counter-model with **all** the exact weights; excluding that zeta
itself has an outer zero remains precisely Deep-\(\Lambda\).

`104_89` normalizes the global Euler truncations of `104_85` and proves
that their log-modulus has exactly zero Poisson mean for every cutoff.
The mean of the limit \((s-1)\zeta(s)\) is the BSY defect
\(D_B=-\log|B(0)|\). From this follows the exact one-sided target
\[
 D_B\le\int
 \bigl(\log|(s-1)\zeta(s)|-\log|\widehat F_X(s)|\bigr)_+\,d\nu.
\]
Proving that the right-hand side tends to zero for some sequence of cutoffs
would prove RH. An explicit Poisson sink shows that interior convergence,
almost-everywhere boundary convergence, and zero mean do not suffice; a
family \(\xi(s-a)\xi(s+a)\) shows the same even with a positive Euler channel
over the ordinary prime powers. The unproved piece remains
preventing that escape using the **exact** heights \(\Lambda(m)\).
The same document now proves the conditional converse direction:
under RH, the Cramér energy allows choosing a subsequence of cutoffs with
\(L^1(\nu)\) convergence. Thus the gate with a subsequence is equivalent to RH,
not an accidentally stronger condition.

104_90 makes the direct attack on the deep scale effective. A verified
height \(H\), VK, and the count \(\mathcal N(T)\le25T\log T\) give
\[
 \lambda_n\ge-500n(\log(2n)+1)(1+e^{a_Hn}),
 \qquad a_H<{1\over2H^2},
\]
and therefore only
\(\limsup\mathcal D_X\le1/2\), not the zero limit. For
\(H=3\cdot10^{12}\), the regime change appears near
\(3.24\cdot10^{50}\). The same document subordinates the outer lattice
model to the tower \(7^k\): it preserves non-negative Euler weights, PNT of
VK type, and a symmetric integer completion, but has outer zeros.
Its additional Euler poles and its modified weights prevent calling it a
counterexample to RH; it proves exactly that this broad package does not substitute for
the literal ordinary values.

`104_91` audits the dual form of `104_89`. By Bochner, requiring
\(K\) and \(e^{-|y|/2}-K\) to be positive definite is exactly
equivalent to \(K=\widehat{\varphi\nu}\) with
\(0\leq\varphi\leq1\): the PD minimax does not relax the one-sided selector. The
Euler--comparator part is written as a single integral against
\(d(J-\mathrm{Li})\). Moreover, for each prefix \(M\) a
counter-model is built that preserves all the ordinary weights up to \(M\) and
all but one remote prime tower, together with
positivity, PNT/VK, and functional symmetry, but has a right-hand zero and
an explicit Jensen defect. This rules out closures by prefix
compactification or by the PD constraints alone; it does not rule out an inequality that
literally uses all the towers and the exact Riemann completion.

`104_92` directly smooths the Euler cutoff, without returning to Hurwitz or
Nyman. The Riesz--Cesàro averages and the arithmetic Abel
\(e^{-\varepsilon m}\) preserve the literal ordinary weights, are
zero-free, and have zero Poisson mean. The Abel average in \(\log X\) computes
exactly as \(H(s+\eta)/H(1+\eta)\), so its barrier
\(\eta=1/2\) is another form of the RH boundary. An aligned spike demonstrates
that every regular positive matrix can preserve the one-sided leak intact.
A continuous model with positive Mangoldt measure, PNT
\(x+O(x^\beta)\), simple pole, and symmetric zeros \(\beta,1-\beta\)
quantifies the failure: the Cesàro and Abel defects grow respectively like
\(X^{\beta-1/2}/\log^2X\) and
\(\varepsilon^{1/2-\beta}/\log^2(1/\varepsilon)\). The model preserves
neither the support nor the ordinary values; hence it closes the general
tightness principle, not the exact target for \(\Lambda(m)\).

`104_93` records the exact discrete energy
\[
 \mathcal E(N)=\sum_{m\le N}{1\over m(m+1)}
 \left\{\sum_{2\le n\le m}{\Lambda(n)-1\over\log n}\right\}^{\!2}
\]
and proves
\(\mathrm{RH}\Longleftrightarrow\sup_N\mathcal E(N)<\infty
\Longleftrightarrow\mathcal E(N)=N^{o(1)}\). A zero of real part
\(\beta>1/2\) forces an energy exponent of at least \(2\beta-1\). The
finite kernel identity is
\(1/\max(r,s)-(N+1)^{-1}\): the missing term lives in the quotient
\(r/s\), while the whole Selberg hierarchy pushes the marks toward the product
\(rs\). Upon centering, the second coefficient already satisfies
\(r(2)<0<r(3)\); without centering, positivity loses the cancellation with the
comparator. Hence varying the Selberg order or applying Vaughan with
diagonal norms does not prove the bound: preserving the signed correlation leaves
exactly a condition equivalent to RH. The document does not establish that
bound unconditionally. The underlying continuous \((L^2)\) equivalence is
classical (the Cramér--Ingham--Titchmarsh framework); the external gate
with exact references remains pending, and no novelty is claimed for that equivalence or
for its standard discretization. This coordinate stays outside the
active front because it loses the Li--Laguerre compact--tail scaffolding.

`104_94` separates for the first time that energy into the ordinary-prime
channel and the proper-power channel. The exact identity
\(\Lambda(p^k)/\log(p^k)=1/k\) gives
\[
 B_m=\pi(m)-\sum_{n=2}^m{1\over\log n}
     +\sum_{k\ge2}{1\over k}\pi(m^{1/k}).
\]
Using only Chebyshev, the last summand is
\(O(\sqrt m/\log m+m^{1/3})\), and hence has finite discrete
energy. It follows that \(\mathcal E(N)=N^{o(1)}\) is exactly equivalent to
the same bound for \(\pi(m)-\mathrm{Li}_2(m)\). Möbius
inversion also shows that \(J\leftrightarrow\pi\) is a finite, invertible
change of coordinates; lcm versus the factorial's radical adds
precisely the finite-energy power block. This rules out the exact
accounting of prime powers being the missing inequality: the
obstacle already lives in the placement of the ordinary primes. It does not prove the
subpolynomial bound or RH.

`104_95` closes the Landau variant based on differential polynomials of
\(\ell=-\zeta'/\zeta\). At quadratic order, the only non-constant
combination that cancels both polar terms at \(s=1\) is
\(A(\ell'+\ell^2+2\gamma\ell)\); its prime coefficient
\(A\log p(2\gamma-\log p)\) already changes sign between \(p=2\) and
\(p=11\). More generally, if
\(P(\ell,\delta\ell,\ldots,\delta^r\ell)\) has non-negative Dirichlet
coefficients and is holomorphic at \(1\), then \(P\) is constant. The
proof isolates each degree over *squarefree* products of exactly that
number of primes and uses the divergence of \(\sum_p1/p\). Hence no
constant-coefficient differential polynomial can cancel the pole,
preserve positivity, and retain poles at the zeros. The theorem extends the
particular Riccati gate of `104_13`; it does not cover non-polynomial or
non-local operators, and it does not prove RH.

`104_102` closes the analytic/rational extension of that gate. For an
arbitrary holomorphic germ
\(\Phi(\ell_0,\ldots,\ell_r)\), the *squarefree* support of exactly
\(k\) primes still isolates degree \(k\) of the infinite Taylor expansion. If the
assembled Dirichlet series has non-negative coefficients, reaches
\(\Re s>1\), and the same branch is holomorphic at \(1\), the divergence of
\(\sum_p1/p\) forces all positive degrees to vanish. For
rational quotients it is further proved that possessing an ordinary Dirichlet
series already forces regularity at the origin: projecting onto
\(r+1\) primes, the Jacobian
\((\log p_i)^{j+1}\) is Vandermonde and invertible. The exact caveat is
that holomorphy merely local at \(1\) is not enough:
\(1/(c-\ell_0)\) has positive coefficients and a zero at \(1\), but
produces a real pole \(\sigma_c>1\). In general, every non-constant transform
of this class has abscissa \(\sigma_c>1\), which Landau turns
into a real singularity located before the non-trivial zeros. No
proof of the energy bound or of RH arises.

`104_96` computes the literal discrete energy up to \(N=10^7\) and splits
it into dyadic blocks. In the range \(9\le j\le23\), one observes
\(0.0519<j^2\Delta_j<0.0982\), which proposes the falsifiable, summable
target \(\Delta_j\le1/(8j^2)\). Proving it for all blocks would imply
RH via `104_93`; the finite computation does not prove it. Prescribed controls with
primitive \(m^\beta\cos(7\log m)/\log m\) verify constant scale at
\(\beta=1/2\) and growth \(2^{(2\beta-1)j}\) at \(\beta=0.65\). The
same diagnostic refutes monotonicity of \(j^2\Delta_j\) and the stronger bound
\(1/(20j^2)\). The prime-power table, `float64` versus
`longdouble`, and chunk independence are audited; proving a
summable bound for all blocks is still missing.

`104_97` adversarially audits the candidate constant \(1/8\). For the
exact critical primitive
\(B_m=c\sqrt m\cos(\gamma\log m+\phi)/\log m\), it proves
\[
 j^2\Delta_j={c^2\over\log^22}
 \int_{(j-1)\log2}^{j\log2}\cos^2(\gamma t+\phi)\,dt+o(1).
\]
With \(c=1,\gamma=7\), the liminf exceeds \(0.574>1/8\); with the
residue normalization of a critical pair of multiplicity four at the
first ordinate, it exceeds \(0.222>1/8\). Hence \(1/8\) is not a
constant imposed by the scale or by mere spectral localization on
the line. These are critical controls, not the ordinary zeta: they do not refute
the bound for its weights. The `104_96` target remains an additional
arithmetic conjecture of strength at least RH, not an automatic
consequence of RH; the general control valid under RH is only the
summability of the blocks.

`104_98` exactly factors the literal energy of
\(P_m=\pi(m)-\mathrm{Li}_2(m)\) on the Mellin line:
\[
 \sum_{m\le N}{P_m^2\over m(m+1)}
 ={1\over2\pi}\int_{\mathbb R}
 \left|{\Phi_N(1/2+it)\over1/2+it}\right|^2dt,
\]
with the moving boundary
\(\Phi_N(s)=\sum_{m\le N}(P_m-P_{m-1})m^{-s}
-P_N(N+1)^{-s}\). Its infinite symbol is the prime zeta minus the
discretized comparator; the difference with
\(E_1((s-1)\log2)\) is holomorphic on \(\Re s>0\). On
\(\Re s>1/2\), an outer zero of multiplicity \(m\) produces
exactly the branch \(m\log(s-\rho)\). The monodromy has a positive Hardy
floor \(m^2\pi^2/6\), but that floor belongs to the average of the two
sheets. On a single sheet, the signed term
\(\pm2\pi m\,\Im\Phi_0\) remains. The explicit formula reproduces the same loss:
positive zero-zero diagonal plus interferences of both signs. This
exactly localizes the missing sign, but does not prove the
subpolynomial energy bound or RH.

`104_99` runs the exact Eratosthenes attack on the `104_94` kernel. With
\(P(z)=\prod_{p\le z}p\), it proves
\[
 \pi(x)=\pi(\sqrt x)-1+
 \sum_{d\mid P(\sqrt x)}\mu(d)\lfloor x/d\rfloor
\]
and keeps, without moduli, the complete signed residue. The parity
pair \(a_n^\pm=1\pm(-1)^{\Omega(n)}\) additionally produces the exact
identity
\[
 \sum_{d\mid P(\sqrt x)}L(\lfloor x/d\rfloor)
 =1+\pi(\sqrt x)-\pi(x),
 \qquad L(y)=\sum_{n\le y}(-1)^{\Omega(n)}.
\]
Since \(1+\pi(\sqrt m)\) has finite energy, RH is equivalent to subpolynomial
energy of
\(\mathrm{Li}_2(m)+\sum_{d\mid P(\sqrt m)}L(\lfloor m/d\rfloor)\).
This does not prove that bound, but localizes the complete cancellation. For every
level \(D\le x^{1-\eta}\), the divisibility data of \(a^+\) and
\(a^-\) differ by \(O_A(x/\log^A x)\) for every \(A\), while their
sieved masses differ by \(\sim2x/\log x\). Hence no stable
inclusion--exclusion/sieve at a sub-complete level can close the
energy; the full level escapes the falsifier, but there the identity
exactly recomposes the original prime error.

`104_100` runs the two-sheet average of `104_98` with the
exact completion. Writing
\(\Phi=\log\xi+G\), the functional equation and conjugation center the sheets of
\(\log\xi\), but in the prime symbol exactly
\[
 |\Phi_+|^2-|\Phi_-|^2=4\pi m\,\Im G(1/2+i\gamma)
\]
remains. The symmetries preserve, rather than invert, the monodromy
character. In the real prefixes, the average reduces exactly to the
Pythagorean decomposition between \(\Re\Phi_N\) and \(\Im\Phi_N\); both
polynomials remain single-valued and do not contain the diagonal.
A functionally symmetric polynomial quartet with integer corrector
\(c(s-1/2)\) exactly cancels one sheet and doubles the other, so
the average does not select the arithmetic sheet. For the real zeta, the
corrector is also not a finite perturbation:
\(\Re G(1/2+it)=\pi|t|/4+O(\sqrt{|t|}+\log|t|)\), and its energy on
\([T,2T]\) is \((\pi^2/16+o(1))T\). BSY preserves the interior Blaschke
factor and Weil preserves the signed radial defect of the quartet. Hence
the completion does not deliver the subpolynomial bound nor prove RH.

`104_101` carries the `104_94` energy over to consecutive gaps without loss. In
each cell \([p_k,p_{k+1})\) it obtains
\[
 \mathcal E_k=W_k(c_k-\bar\ell_k)^2+V_k,
 \qquad W_k=p_k^{-1}-p_{k+1}^{-1},
 \qquad c_{k+1}=c_k+1-\ell_{k,g_k}.
\]
The quadratic completion decides the sign of the variational attempt: the
convexity gives a cellular minimum, while the upper bound requires
controlling the accumulated walk of the normalized gaps. For any
fixed wheel \(W\), \(1/2<\beta<1\), and \(c>0\), it constructs a
\(0\)-\(1\) sequence, supported on \((n,W)=1\), with PNT/VK, gaps
\(O(\log x)\), and
\[
 A(x)-\sum_{n\le x}{1\over\log n}=cx^\beta+O(1),\qquad
 \mathcal E_A(N)\sim{c^2\over2\beta-1}N^{2\beta-1}.
\]
Thus the relaxed restrictions on composition, density, and gap do not
force subpolynomial energy. Imposing simultaneously "selected implies
prime" and "omitted implies composite" leaves the singleton of the
literal primes; no independent convex comparison remains and estimating it is
the original problem.

`104_103` adversarially reinforces that diagnostic up to abstract Euler
composition. For any prescribed zero
\(\rho=\beta+i\gamma\), \(1/2<\beta<1\), and any fixed wheel,
it rounds the density
\[
 {1-2x^{\beta-1}\cos(\gamma\log x)\over\log x}
\]
into a literal \(0\)-\(1\) staircase, with integer norms and gaps
\(O(\log x)\). By declaring its generating points to form a free
commutative monoid, it obtains weights \(\Lambda_{\mathcal P}\ge0\), an exact Euler
product, and the coefficient-by-coefficient identity
\[
 g(m)\log m=\sum_{d\mid m}g(m/d)\Lambda_{\mathcal P}(d),
\]
but the resulting zeta has simple zeros at \(\rho,\bar\rho\) and its
energy grows like \(N^{2\beta-1}/\log^2N\). Hence integrality,
step structure, gaps, PNT/VK, and abstract Euler factorization do not
exclude an outer excursion. The property not preserved is
identified exactly: that the generating norms be the
ordinary irreducibles of \((\mathbb N,\cdot)\), without norm
collisions. An internal rigidity theorem proves that an injective
norm forces \(P_{\mathcal Q}(x)\le\pi(x)\), and that a bijective norm forces
exactly the ordinary prime system. Imposing it returns the singleton
of the literal primes and, with
it, the original energy target. This falsifier does not prove the bound
for the ordinary primes nor RH.

`104_104` directly attacks the block criterion from the real values and
derivatives of
\(\mathcal F(z)=\log(2\xi((1-z)^{-1}))\). It proves the exact criterion
\[
 \mathrm {RH}\iff
 \limsup_{k\to\infty}
 \left({|\mathcal F^{(k)}(r)|\over k!}\right)^{1/k}
 \le {1\over1-r}\qquad(0<r<1),
\]
with even \(r\in\mathbb Q\cap(0,1/2)\) sufficing. The Euler identity
with the ordinary \(\Lambda(m)\) gives absolutely convergent formulas
for each jet, but directly certifies the required disks only within
the horodisk \(|z-1/2|<1/2\), equivalent to \(\Re s>1\). For
\(r<1/2\), moving from the safe radius \(r\) to radius \(1-r\) is exactly the
continuation that excludes interior zeros. An explicit polynomial factor
\(P_{\beta,\gamma}\), positive on the real axis and compatible with the functional
equation, reality, and order one, becomes \(C^J\)-arbitrarily invisible
on any real compact while adding an off-line quartet and syndetic
negative excursions. It is the qualitative falsifier of `104_84` refined
quantitatively, not a new family of completions. This rules out
stable inferences from a finite
number of jets. A second factor
\(1+c[s(s-1)]^{2M_0}\prod_j((s-1/2)^2-a_j^2)^{2M_j}\)
also **exactly** matches any prescribed finite family of real jets
and still introduces a zero with \(1/2<\Re\rho<1\); the explicit caveat
is that it may introduce other zeros on \(\Re s>1\). Neither is
a counter-model with the same primes. Having exactly
the same \(\Lambda(m)\) forces the same \(\zeta\) by uniqueness of the
derived logarithm. The gate proves neither the blocks, Deep, A1, nor RH.

`104_106` computes the general block filter on the residue
defect:
\[
 \sum_ja_j\mathscr R_{N+j}
 =\sum_{\Re\rho>1/2}m_\rho
 \{w_\rho^NA(w_\rho)+w_\rho^{-N}A(w_\rho^{-1})-2A(1)\}.
\]
Box, Cesàro, and Fejér are just choices of \(A\) and do not orient the outer
mode. The rational quartet \(w=i/2\) has, on every block starting
at \(N\equiv2\pmod4\),
\[
 q_N>2^{N+1},\qquad
 \sum_{j=0}^3q_{N+j}
 =16-6\,2^N+\tfrac32\,2^{-N}<0.
\]
So a favorable signed average does not fabricate a good block. The
correct operation is
\(\sum(-\mathscr R_n)_+=\sup_{0\le a_j\le1}-\sum a_j\mathscr R_{N+j}\).
An exact deterministic criterion is obtained on
\([L^2,L^2+L-1]\), but the bound for that supremum with the
ordinary \(\Lambda(m)\) is not proved.

`104_107` returns to the Li--Laguerre coordinate and combines for the first time the
phase bound of `104_41` with the block relaxation of `104_67`. For
the triangular weights
\(\alpha_{L,k}=(L-|k|)/L^2\), \(|k|<L\), it proves
\[
 |\mathcal B^\triangle_{N,L,a}|
 \le {3\pi\over2}{N\over L}+2(1-L^{-2}),\qquad a\ge4.
\]
So a block of \(2L-1\) degrees with \(N\asymp L\) has absolute phase
cost, instead of \(O(N)\). The residue transport is also closed
exactly:
\[
 {1\over\rho(\rho-1)}
 \sum_{|k|<L}\alpha_{L,k}\mathcal F_{N+k}(w_\rho)
 =T_{N,L}(w_\rho)+T_{N,L}(w_\rho^{-1})-2,
\quad
 T_{N,L}(w)=w^{N-L+1}
 \left({1-w^L\over L(1-w)}\right)^2.
\]
The multiplier has no zeros on \(|w|<1\), and the reciprocal term
preserves size \(\asymp |w|^{-N-L}/L^2\). The quartet \(w=i/2\)
produces both exponential signs while preserving the critical phase.
Hence averaging removes the boundary cost but not the
off-line defect. Moreover, a bounded signed average does not give a good block
coefficient by coefficient: applying `104_67` would still require controlling
the positive part, the maximum, or every degree. The coupled one-sided bound
for the ordinary \(\Lambda(m)\) remains unproved.

`104_108` reduces that cube of tests to a one-parameter family
of modulated Fejér. For \(a\ge4\), uniformly in \(\phi\),
\[
 |\mathcal B^\triangle_{N,L,a}(\phi)|
 \le3\pi N/L+4.
\]
Parseval identifies its \(L^2\) average with
\(\sum\alpha_{L,k}^2B_{N+k}^2\), so a uniform subexponential bound
in \(\phi\) would detect any outer excursion and is
equivalent to RH. Transporting to \(a=1\), the residue is
\[
 w_\rho^NK_L(w_\rho e^{-i\phi})
 +w_\rho^{-N}K_L(w_\rho^{-1}e^{-i\phi})-2H_L(\phi).
\]
The paired frequency preserves size
\(|w_\rho|^{-N-L+1}/L^2\). For the full quartet \(w=i/2\),
\(N=2L\), and \(L\) even, the filter is at least
\(2^{3L}/L^2-4\), with no conjugate cancellation. This is a structured
reduction of coordinates, not a weakening of RH-strength or a
proof: the uniform arithmetic bound at the boundary remains open.

`104_109` combines the residue of `104_33`--`104_41`
with the high localization of `104_76`. For
\[
 D_n(Y)=2\Re\sum_{\substack{\Re\rho>1/2\\0<\Im\rho\le Y}}
 {m_\rho\mathcal F_n(w_\rho)\over\rho(\rho-1)}
\]
it uniformly proves
\[
 |\lambda_n+D_n(Y)|
 \ll Y\log Y+X\log X\{1+e^{X/(2Y^2)}\}\qquad(n\le X).
\]
So RH is equivalent to the existence of blocks
\(I\subset[N,2N]\), of unbounded lengths, on which
\(D_n((2N)^{1/4})\ge-\tfrac12e^{\sqrt N}\) degree by degree. The
correct scale of the deep gate is \(N^{1/4}\), not \(\sqrt N\). The quartet
\(w=4i/5\) proves that a signed average can be favorable over blocks
of arbitrary length while exponential positive excursions persist, and
that the binomial average with \(a=4\) makes both modes contractive.
Hence the phase bound and a linear average do not deliver the
barrier; a bound for the maximum or the positive part of the exact
prime--Laguerre form is still missing.

`104_110` returns to the literal prime form of the modulated filter of
`104_108`. If
\[
 P_{L,\phi}=\sum_{|k|<L}\alpha_{L,k}e^{-ik\phi}
 L_{2L+k-1}^{(1)},\qquad
 Q_{L,\phi}=\sum_{|k|<L}\alpha_{L,k}e^{-ik\phi}
 L_{2L+k-1}^{(2)},
\]
it proves the complete identity
\[
 \mathcal B^\triangle_{2L,L,1}(\phi)
 =P_{L,\phi}(0)+\int_0^\infty
 E(e^u)e^{-u}Q_{L,\phi}(u)\,du,
\]
together with a closed contour with
\(M_\Lambda((1-z)^{-1})K_L(e^{-i\phi}/z)\). For
\(\phi=\pi\), all degrees have exactly the same sign on the
outer ray. At the scale
\(U_L=L^{5/3}(\log L)^{1/3}\), the VK majorant is at least
\[
 \exp\{(4/3)L\log L+(2/3)L\log\log L-O(L)\}.
\]
Thus PNT/VK, even preserving pole and prime powers through integration
by parts and even adding monotonicity, do not deliver the uniform
subexponential barrier. This rules out that estimation method, not the bound
for the literal weights \(\Lambda(m)\), whose signed cancellation remains
open.

No document in this phase can be cited as proof of RH.

104_111 directly audits the Deep limit of 104_75 via the
canonical factorization of
\(E(z)=((1-z)^{-1}-1)\zeta((1-z)^{-1})\). It proves
\[
 \lambda_n=C_n-Z_n,\qquad C_n=O(n^2\log(n+1)),
\]
where \(Z_n\) contains exactly the coefficients of the Blaschke
product of the zeros with \(\Re\rho>1/2\). Consequently, \(\Omega_X\)
is trapped between the events
\(Z_n\ge(1\pm o(1))e^{\sqrt X}\), and
\(\Omega_X\to0\iff B\equiv1\iff\mathrm{RH}\). It also fixes an expository
gap in 104_75: the diagonal lift of the hard indicator is proved by
inclusions with thresholds \(e^{\sqrt X}\pm1\), not just by comparing scales.
The result localizes exactly the pending interior factor; it does not
cancel it and does not prove RH.

`104_112` closes the Markov interpretation of the Deep limit. For an
outer quartet
\[
 q_n(\rho)=4-4\cosh(na_\rho)\cos(n\theta_\rho),
 \qquad
 a_\rho={1\over2}\log {|\rho|^2\over|\rho-1|^2},
\]
the threshold \(e^{\sqrt X}\) triggers at returns with
\(\cos(n\theta_\rho)\ge1/2\) exactly when
\[
 a_\rho>2X^{-1/2}+o(X^{-1/2}).
\]
Since \(a_\rho\asymp(\beta-\tfrac12)/\gamma^2\), the deep observable
is operationally equivalent to excluding zeros in the box
\[
 0<\gamma\lesssim X^{1/4},\qquad
 \beta-\tfrac12\gtrsim \gamma^2X^{-1/2}.
\]
The boundary of that box touches \(\Re s=1/2\) as \(X\to\infty\). Moreover,
if \(D_n(Y)\) is oriented so that the outer quartets contribute a positive
part, then under RH \(D_n(Y)_+\equiv0\), while a single zero
in the box forces
\[
 \sum_{n\le X}{D_n(X^{1/4})_+\over n}
 \gg e^{Xa_\rho/2}-O(X^{1/4}\log X).
\]
Hence Markov has no slack: it is either zero or fails above the threshold.
It is also recorded that a bound
\(\limsup\Omega_X\le c\) with any \(c>0\) does not rule out the dominant-phase
models of `104_56`. The Deep limit remains an exact criterion,
not a proof; the missing mechanism would have to exclude the box using the
literal ordinary primes and fail for the outer Euler models.

`104_113` rescales that box with \(T=X^{1/4}\):
\[
 0<\gamma\lesssim T,\qquad
 \beta-\tfrac12\gtrsim\gamma^2/T^2.
\]
This shows why the classical inputs do not close the Deep limit. The
zero-free regions live near \(\Re s=1\), while the box touches
\(\Re s=1/2\) for \(\gamma=o(T)\). Density theorems give positive
counts at \(\sigma=1/2+o(1)\), not the absence of a single zero. The
verification up to height \(H\) only covers \(X\le H^4\), never the
asymptotic limit. The front is reduced to a literal arithmetic exclusion of
the box, not to counting, finite height, or improved constants.

`104_114` builds the exact local detector of that box on the Cayley
disk. With
\[
 E(z)=((1-z)^{-1}-1)\zeta((1-z)^{-1})=B(z)O(z),
\]
the quantity
\[
 \mathcal J(z)=P_z(\log|E^*|)-\log|E(z)|
 =\sum_{\Re\rho>1/2}m_\rho
 \log\left|{1-\overline{a_\rho}z\over z-a_\rho}\right|
\]
is precisely the Green potential of the interior Blaschke factor. A
zero in the box produces a local peak \(\gg1\), and
\(\mathcal J\equiv0\iff B\equiv1\iff\mathrm{RH}\). This proves that the
Poisson--Jensen route detects the box without loss, but contributes no new
sign: the inequality that annihilates \(\mathcal J\) is exactly the removal of
the interior factor, i.e. Weil/RH on that family of tests.

`104_115` audits the scalar resolvent certificate over the lattice of
factorizations. The generator that exchanges all towers has infinite
exit rate for \(0<\varepsilon\le1\), the crossed term
\(\langle i[X,S]g_n,g_n\rangle\) is exactly zero for the real
Laguerre vector, and \(Cg_n\) does not in general satisfy the Poisson
compatibility with the constants of each layer \(\Omega\). Pivoting to
consecutive primes, with diffusive rate
\(\log(p_{j+1}/p_j)^{-2}\), repairs the domain and makes the
resolvent positive after projecting the kernel. A complex twist recovers the
phase but changes sign with \(n\). The minimal successor is fixed as a
two-degree Laguerre lift and a conservative current over cycles of
three nearby towers; the original scalar certificate is withdrawn.
The finite current satisfies an exact Schur bound with a computable constant;
the only bridge not yet obtained is a second-order Mecke identity
that would turn that two-degree crossed term into the real linear functional
\(B_{n,\varepsilon}\).

`104_116` proves the requested exchange Mecke identity. For
an antisymmetric current \(\omega\), its form is
\[
 \langle F,J_\omega G\rangle_s
 =\sum_{p,q}{\omega_{pq}\over(pq)^{s/2}}
   \mathbb E_s\{\overline{F(qN)}G(pN)\}.
\]
The conservative condition \(J\mathbf1=0\) is
\(\omega(p^{-s/2})_p=0\); over three primes it fixes a unique circulation and
the form becomes a cyclic determinant of the three shifts.
The exact comparison closes the `104_115` bridge negatively: the
current is alternating and bilinear, while \(B_{n,s}\) is the
linear prime--pole source. Opening the current toward the continuous comparator
exactly reproduces \(M_s(f)\), and closing it to obtain positivity
eliminates it. Hence Mecke is proved, but it does not supply the positive remainder
required for A1.

## Other files in this folder

Files not described above:

- `104_100_FUNCTIONAL_TWO_SHEET_COMPLETION_GATE.md` — 104_100 — Functional two-sheet average and completion-corrector gate
- `104_101_PRIME_GAP_VARIATIONAL_AND_COMPOSITION_GATE.md` — 104_101 — Exact gap coordinate, convexity, and composition gate
- `104_102_ANALYTIC_RATIONAL_LANDAU_RIGIDITY.md` — 104_102 — Analytic/rational rigidity of the Landau transform
- `104_103_INTEGRAL_STEP_EULER_OFFLINE_FALSIFIER.md` — 104_103 — Integer-step Euler falsifier with an off-line zero
- `104_104_REAL_JET_TANGENT_DISK_GATE.md` — 104_104 — Real jets, tangent discs, and the Li-block gate
- `104_105_DEEP_AND_DISCRETE_ENERGY_ADVERSARIAL_AUDIT.md` — 104_105 — Adversarial audit of Deep-Λ and of the discrete energy
- `104_106_BLOCK_RESIDUE_SELECTOR_GATE.md` — 104_106 — Block averages, residues, and the exact selector gate
- `104_107_FEJER_BLOCK_PHASE_TRANSPORT_GATE.md` — 104_107 — Fejér blocks and the exact phase-transport gate
- `104_108_MODULATED_FEJER_MATCHED_FILTER_GATE.md` — 104_108 — Modulated Fejér, matched filters, and the resonance gate
- `104_109_LOW_RESIDUE_BLOCK_TRANSPORT_GATE.md` — 104_109 — Low residue, block barrier, and the transport-average gate
- `104_110_LITERAL_PRIME_FEJER_VK_GATE.md` — 104_110 — Literal prime Fejér kernel and the exterior-ray VK gate
- `104_111_DEEP_BLASCHKE_FACTOR_REDUCTION.md` — 104_111 — Exact reduction of Deep to the Blaschke factor
- `104_112_DEEP_MARKOV_HEIGHT_BOX_GATE.md` — 104_112 — Deep height box and the no-slack Markov gate
- `104_113_HEIGHT_BOX_CLASSICAL_INPUTS_GATE.md` — 104_113 — Classical-inputs gate for the deep box
- `104_114_BOX_BLASCHKE_POISSON_DETECTOR.md` — 104_114 — Blaschke–Poisson detector of the deep box
- `104_115_NEIGHBOR_PRIME_RESOLVENT_GATE.md` — 104_115 — Global resolvent gate and pivot to neighboring prime towers
- `104_116_TRIANGLE_EXCHANGE_MECKE_IDENTITY.md` — 104_116 — Triangular-exchange Mecke identity and the source–circulation gate
- `104_82_Q_INDEPENDENT_TORUS_UNTWISTED_GATE.md` — 104_82 — Independence of prime lengths and the untwisted-point gate
- `104_83_XI_FOURIER_DEEP_GATE.md` — 104_83 — Fourier gate for \(\Xi\): exact cumulants and modular boundary cancellation
- `104_84_BLASCHKE_EULER_RIGIDITY_GATE.md` — 104_84 — Inner Blaschke factor and rigidity of local Euler identities
- `104_85_NONLOCAL_PRIME_HURWITZ_NYMAN_GATE.md` — 104_85 — Global renormalization of primes, Hurwitz, and non-local Nyman form
- `104_86_BOSE_MELLIN_SINE_REFLECTION_GATE.md` — 104_86 — Positive Bose kernel and Mellin sine self-reflection
- `104_87_NYMAN_FLOOR_MOBIUS_TAIL_GATE.md` — 104_87 — Finite Nyman section, `max` inversion, and Möbius tail
- `104_88_DIRECT_DEEP_VISUAL_AND_ORDINARY_PRIME_UNIQUENESS.md` — 104_88 — Direct diagnostic of Deep-\(\Lambda\) and uniqueness of ordinary primes
- `104_89_BSY_ONE_SIDED_EULER_BOUNDARY_GATE.md` — 104_89 — One-sided BSY gate for real Euler truncations
- `104_90_DEEP_SCALE_EFFECTIVE_BOUND_AND_PNT_COUNTERMODEL.md` — 104_90 — Effective bound on the Deep scale and PNT countermodel
- `104_91_DUAL_PD_AND_REMOTE_TOWER_PREFIX_GATE.md` — 104_91 — Exact PD duality and the remote tower gate
- `104_92_ABEL_CESARO_EULER_TIGHTNESS_GATE.md` — 104_92 — Euler tightness gate under Abel--Cesàro smoothings
- `104_93_DISCRETE_CRAMER_ENERGY_AND_VARIABLE_SELBERG_GATE.md` — 104_93 — Discrete Cramér energy and variable-order Selberg gate
- `104_94_ORDINARY_PRIME_CORE_AND_PRIME_POWER_FINITE_ENERGY_GATE.md` — 104_94 — Core of ordinary primes and finite energy of the powers
- `104_95_POLE_CANCELLATION_POSITIVE_DIFFERENTIAL_NO_GO.md` — 104_95 — Pole cancellation and rigidity of positive differential polynomials
- `104_96_DISCRETE_CRAMER_ENERGY_VISUAL_DIAGNOSTIC.md` — 104_96 — Dyadic visual diagnostic of the discrete Cramér energy
- `104_97_DYADIC_ONE_EIGHTH_CRITICAL_LINE_ADVERSARIAL_GATE.md` — 104_97 — Critical adversarial gate for the dyadic constant $1/8$
- `104_98_PRIME_ENERGY_MELLIN_MONODROMY_GATE.md` — 104_98 — Mellin factorization of the prime energy and monodromy gate
- `104_99_ERATOSTHENES_PARITY_ENERGY_GATE.md` — 104_99 — Exact Eratosthenes, parity identity and energy gate
- `deep_lambda_visual_diagnostic.png` — figure
- `deep_lambda_visual_diagnostic.svg` — figure
- `discrete_cramer_energy_dyadic.csv` — data (CSV)
- `discrete_cramer_energy_visual.png` — figure
- `discrete_cramer_energy_visual.svg` — figure
