# Goal plan: complete row D

## Goal

Prove, without using zeros or an equivalent spectral sign as input,

\[
B_{\rm nuc}(f,f)\le0\qquad(f\in\mathcal T^0),
\]

including the equality case.  Only after this theorem is proved may the
existing Weil criterion be applied.

## Critical execution plan (2026-08-08)

The programme is now organized around one carrying theorem, not around a
collection of endpoint computations.  At the birth of a prime power, use
the notation of D.190 and D.214.  The theorem to be proved is the supported
sharp capacity inequality

\[
 q_N^*D_N^\dagger q_N\leq
 \mathcal M_N,
 \qquad
 \mathcal M_N=I-y_N^*y_N-h_N^*D_Nh_N
       +2\operatorname {Re}(h_N^*q_N),
\]

together with the corresponding range inclusion.  Equivalently, one must
construct from the prime, Gamma, Poisson and support data a contraction
whose defect identity gives the sharp Douglas factorization of D.190(0.3).
The contraction may not be defined using the pseudoinverse in the displayed
inequality, since that would merely rename the theorem.

The order of execution is:

1. finish the correctly typed finite rectangular row-band certificate at
   \(T=\tfrac12\log6\), retaining the exact Green correction;
2. isolate the infinite post-cutoff residual as an operator on the Poisson
   boundary, rather than replacing it by a scalar gap;
3. test whether that residual is a block of a source-defined unitary or
   contractive colligation and derive its exact conservation law;
4. require the resulting identity to fail on the existing off-line Beurling
   surrogate unless it uses the arithmetic Poisson/Gamma coupling specific
   to \(\mathbb Q\);
5. prove the sharp contraction uniformly at every sufficiently large
   prime-power birth, allowing saturation at norm one;
6. interval-certify the finite births below the effective threshold;
7. combine the initial interval, birth identity, nesting and capacity
   inequalities; then classify equality on the primitive space.

The finite rectangular computation in item 1 is a laboratory and a local
certificate.  Even if it succeeds, it does not prove an endpoint until the
infinite residual in item 2 is controlled, and it does not prove row D until
items 3--7 are complete.

The following are rejected as closing arguments: defining effectivity by
the desired capacity inequality; postulating mixed Riemann--Roch with
quadratic term \(B_{\rm nuc}\); choosing the negative spectral subspace;
deducing the unit bound from summability; or extrapolating from any finite
number of Galerkin/interval certificates.

## Epistemic baseline

* Rows A--C are treated under the contracts stated in paper 42.
* The primitive feature factorization, the initial interval
  (0<T\le\log2), the cell Schur equivalence, integer-cell orthogonality,
  return identities and all-depth arithmetic summability are **PROVED** or
  **INTERVAL CERTIFIED** as individually stated.
* Full positivity at (T=\frac12\log5) is **OPEN** because the safe
  finite block--infinite complement coupling is not closed.
* Uniform sharp Douglas capacity at all births is **OPEN** and is
  equivalent, together with the initial interval, to row D.
* Numerical atlases may falsify or suggest identities; they cannot prove
  the global theorem.

## Phase I: operator audit — completed

Deliverables:

* `ROW_D_OPERATOR_MAP.md`;
* `ROW_D_SHARP_DOUGLAS.md`;
* `ROW_D_TWO_PROJECTION_AUDIT.md`.

Outcome: the elementary two-projection identity does not apply because
(Q_T) is not a projection.  Its exact residual has been computed.  This
eliminates the first candidate without hiding the gap.

## Phase II: local Poisson/Hankel route — audited and discarded

D.195--D.197 already perform the required audit.  They construct the exact
local Poisson colligation and show that its boundary space at (p) is

\[
L^2(C_p)^+\oplus L^2(C_p)^-,
\]

not the two scalar Tate jets.  The primitive source image contains both
coordinate axes, and the arithmetic residue form retains inertia
((\infty,\infty)).  Hence no placewise graph contraction can produce the
sharp Douglas factorization.  The global prime--Gamma graph remains
equivalent to the missing polarization and cannot be assumed.

This route is **IMPOSSIBLE locally** and is no longer active.

## Phase III: operator-valued Green multilevel route — active

D.209 refutes replacement of the whole complement Green by the scalar
worst case.  D.210 supplies the exact replacement.  For an intermediate
trial space (W), write

\[
C^*A^{-1}C=G_W+R_W^*S_W^{-1}R_W
\le G_W+\delta_W^{-1}R_W^*R_W.
\]

The route is:

1. build the complete directed primitive compression on a nested space
   (V_{m_0}\subset V_{m_1});
2. eliminate the intermediate block exactly, retaining (G_W);
3. construct the corrected residual (R_W), not the raw coupling (C);
4. prove a lower bound (S_W\ge\delta_WI) only on the final tail;
5. use the endpoint-flat/Plancherel estimates solely on (R_W);
6. verify the final finite Schur matrix by outward rounding;
7. derive a uniform rule (m_1=m_1(N)) and uniform residual estimate for
   all sufficiently large prime-power births.

This is strictly sharper than the scalar-gap route and does not assume the
desired sign.  The Beurling falsifier remains mandatory for any claimed
uniform asymptotic theorem.

D.211 now supplies a canonical choice of the finite/infinite filtration.
For \(R_T=X_T^*X_T\), \(L_T=Y_T^*Y_T\leq M_TI\), and
\(P_\Lambda={\bf1}_{[0,\Lambda)}(R_T)\) with \(\Lambda>M_T\),

\[
(I-P_\Lambda)(R_T-L_T)(I-P_\Lambda)
\geq(\Lambda-M_T)(I-P_\Lambda).
\]

The projection has finite rank because \(R_T\) has compact resolvent, and
the same gap survives every later Schur shorting.  Hence the uncontrolled
infinite-tail coercivity problem is **completed**.  The active obligation
is now the uniform finite-Schur theorem at large prime-power births, with
directed Green enclosures from D.210--D.211.

D.212 audits the asymptotic estimates D.164--D.189.  They prove the
pure-Gamma coefficient \(\tfrac12\log N\) and uniform summability of the
reference/Witt majorants, but cannot transfer that bound through the old
defect.  The exact extra cost is

\[
b_N^*K_N(I-K_N)^{-1}b_N
=\int_{(0,1]}{1-d\over d}\,d\mu_{N}(d).
\]

The active uniform theorem is therefore a source-defined defect-layer
Carleson estimate for the exact centered column, after the D.211
reference-high block has been eliminated.  Norm-only and scalar-gap
routes are excluded by an exact one-dimensional counterexample.

D.213 converts a sufficient defect-layer target into the exact return
estimate

\[
y_N^*(A_NA_N^*)^ky_N
\ll {\varepsilon_N\log N\over
(k+1)(1+\log(k+1))^2},
\]

for the complete centered born column.  This is quantitatively equivalent
to the stated defect-layer Carleson estimate and sums to \(o(\log N)\).
The raw Witt and long-time reference estimates of D.183/D.187/D.188 are
inputs, but their cross terms must remain inside the complete return.  The
displayed decay is a strong sufficient theorem, not a claim of logical
necessity; the sharp necessary and sufficient condition is the total
capacity budget.

D.214 audits the defect-difference identity \(q=Dh-u\).  The push-through
formula proves

\[
y^*D_{\rm out}^\dagger y=y^*y+u^*D^\dagger u
=y^*y+h^*Dh-2\operatorname {Re}(h^*q)+q^*D^\dagger q.
\]

Hence factoring \(u\) is equivalent to the original output gate and is
not a new route.  The exact remaining budget is

\[
q^*D^\dagger q\le
I-y^*y-h^*Dh+2\operatorname {Re}(h^*q).
\]

All future asymptotic estimates must be compared to this operator-valued
budget, not merely to an unnamed \(O(\log N)\) margin.

D.220 completes a native-Arb two-column rebuild at
\(T=\frac12\log6\).  It certifies the complete primitive \(V_{200}\)
compression and the restricted graph-plus-\(V_{200}^{\perp}\) gate

\[
 K-0.2199^{-1}H_G>0.
\]

The audit also prevents a false endpoint claim.  In the exact three-block
matrix the safe block still couples to \(V_{200}^{\perp}\).  With

\[
 \Sigma_Q=A_{QQ}-C_S^*B_{SS}^{-1}C_S,
\]

the remaining local theorem is

\[
 \Sigma_Q\ge0,
 \qquad K-C_G\Sigma_Q^\dagger C_G^*\ge0,
\]

including the supported-range condition.  Thus the direct graph-to-tail
load is paid rigorously, while the safe-short change of Green remains the
minimal endpoint obligation.  This is a concrete instance of the D.210
operator-valued Green problem, not a new scalar-gap route.

D.221 compresses that local obligation to one normalized capacity

\[
 \rho_6=\|A_{QQ}^{-1/2}C_S^*B_{SS}^{-1/2}\|^2.
\]

An exact Schur argument proves that the full endpoint follows if
\(\rho_6\le0.7\).  Independently, Arb certifies the corresponding remaining
two-column budget

\[
 K-[0.2199(1-0.7)]^{-1}H_G>0.
\]

The sole local target at \(T=\frac12\log6\) is therefore the D.210
operator-Green enclosure \(\rho_6\le0.7\), with the intermediate Green kept
exactly and the scalar tail gap applied only to its corrected residual.

D.222 builds the correctly typed orthogonal primitive trial band

\[
 W=(V_{260}^{\rm prim})\ominus(V_{200}^{\rm prim})
\]

and, writing \(E=W^*A_TW\) and \(C=S^*A_TW\), certifies with native Arb
blocks

\[
 CE^{-1}C^*\le0.09\,B_{SS}
\]

for its finite Galerkin Green contribution.  D.210--D.211 then reduce the
remaining local target to the corrected residual estimate

\[
 R_W^*R_W\le0.134139\,B_{SS}.
\]

This residual contains all Gamma/contact cross terms after the exact band
solve.  It is the active endpoint obligation; raw-coupling or sampled FFT
bounds do not substitute for it.

D.223 applies the numerical falsifier before enlarging the interval
calculation.  The fixed \(260\)-corrected source has projected residual
centres \(0.3057,0.2778,0.2553,0.2218\) at cutoffs
\(260,320,400,600\); these are heuristic because the Green is not recomputed.
An attempted recomputation by FFT is rejected: its supposedly whitened safe
block has spectrum spanning \(3.75\,10^{-4}\) to \(4.39\,10^4\).
Consequently raw FFT is removed from the proof route.

The selected local route is now the endpoint-flat multilevel decomposition
of D.205--D.208, inserted into the D.210 Green identity.  A fresh directed
run of D.207--D.208 certifies the \(78\)-dimensional flat-safe block and a
post-\(600\) trace below \(3.156\,10^{-27}\).  The next
construction must assemble its finite \(200{:}600\) Green and the finite
boundary complement without changing the original D.221 capacity.

D.225 completes the latter finite construction.  It gives the exact
source-defined decomposition

\[
 V_{200}^{\rm prim}=D_{\rm bdry}^{120}\dotplus S_{\rm flat}^{78}
\]

and certifies both the flat block and the flat-shorted \(120\)-dimensional
boundary block with native Arb congruences.  The boundary graph is exactly
\(A_T\)-orthogonal to the flat channel.  The remaining endpoint work is
therefore the finite \(200{:}600\) flat Green, conversion of the D.208 raw
tail into its corrected residual, and the final boundary-graph/tail Schur
gate.

The D.208 Plancherel certificate has now been rerun at cutoff \(400\):

\[
 \operatorname{tr}(R_{400}A_TS_{\rm flat}B_{\rm flat}^{-1}
 S_{\rm flat}^*A_TR_{400})
 <5.220\,10^{-6}.
\]

Thus the finite Green only needs the \(200\)-dimensional band
\(200{:}400\).  D.226 constructs that trial band inside the same order-60
endpoint-flat primitive ideal.  Its Galerkin-corrected source therefore
remains endpoint-flat, so applying the post-\(400\) certificate is correctly
typed **for the flat channel relative to its own orthogonal complement**.
Native Gamma/contact \(400\times400\) caches and the directed Green Schur
are the active computation.

There is an essential integration caveat.  The D.226 band is orthogonal to
the old flat source, but not to the whole primitive \(V_{200}\).  It is
therefore not a subspace of the \(V_{200}^{\perp}\) high block on which
D.185 proves the \(0.2199\) gap.  That gap may not be applied directly after
the D.226 solve.  The next exact object is the four-block form on

\[
 D_{\rm bdry}^{120}\dotplus S_{\rm flat}^{78}
 \dotplus W_{\rm flat}^{200}\dotplus V_{400}^{\perp}.
\]

One must either (i) short the boundary block together with the flat band
and prove a directed lower bound for the resulting true tail, or (ii)
replace the trial band by the correctly typed band
\(V_{400}^{\rm prim}\ominus V_{200}^{\rm prim}\) and certify the complete
corrected residual.  Until one of these factorizations is closed, the D.226
and D.208 bounds are local ingredients and do not prove \(\rho_6\le0.7\).

D.227--D.235 refine this integration.  The blindly enlarged correctly
typed band captures only centre capacity (0.088356\ldots), essentially
the already certified D.222 allowance (0.09), so that route is rejected as
a source of a new scalar margin.  The exact polynomial decomposition

\[
 \mathcal P_{199}=\mathcal P_{119}
 \oplus(1-u^2)^{60}\mathcal P_{79}
\]

separates a stable (120)-jet lift from the endpoint-flat ideal.  The lift
has been reconstructed in Arb with maximum coefficient (4.492), avoiding
the (10^8)-scale coefficients produced by eliminating the nearly singular
flat block first.  Monomial action Grams are nevertheless rejected because
their interval dependency reaches (10^{284}).

The active directed replacement evaluates the post-Galerkin residual in the
Legendre basis itself.  D.232 and D.233 construct the exact rectangular
Gamma/contact block

\[
 A_T[V_{400:600},V_{0:400}],
\]

and D.235 tests its corrected residual against the remaining (0.134139B)
budget.  Square, adjoint, and known-contact subblock regressions pass.  This
finite row-band certificate does not replace the still required infinite
Poisson-boundary transport of D.190.

D.236 packages every tower (p,p^2,\ldots) into one exact source operator.
For (U_p=S_{\log p}), (r_p=p^{-1/2}),

\[
 V_p=\sqrt{1-r_p^2}(I-r_pU_p)^{-1},\qquad
 -\sum_{k\ge1}(\log p)r_p^k(U_p^k+U_p^{*k})
 =(\log p)(I-V_p^*V_p).
\]

This is a proved Euler--Poisson defect identity and retains all prime
powers after support compression.  It also proves that a scalar sign gauge
cannot realize the reduced prime-power contact compatibly with monoidal
composition.  The identity is now the preferred source packaging for the
prime part of a candidate colligation.  It is not yet a contraction after
the Gamma, Tate and support shortings; proving that completed conservation
law remains the global target.

D.237 spectrally factors both balanced prime Grams, not only their
difference.  The whole antisymmetric and symmetric tower is represented by
one rational filter per prime with common denominator
((I-p^{-1/2}S_{\log p})).  This is an exact reduction of state
multiplicity and has passed independent cyclic-unitary regressions.  D.238
then proves that the raw old/shell cross is the negative of one common
positive Gamma--resolvent--Euler kernel, up to the finite-rank Tate
correction.  On an integer born shell the positive identity and Poisson
diagonals cancel exactly, each having artificial total size
(\vartheta(N)\sim N).  Therefore a valid colligation must retain this
lossless cancellation; estimating the two positive pieces separately is
excluded.  The remaining candidate is a conservative prime--Gamma network
whose off-diagonal block is the common feature of D.238 and whose finite
Tate correction removes the two polar modes.

D.239 identifies the rational Poisson state with the normalized semilocal
cyclic density

\[
 (1-p^{-1})|L_p(\tfrac12+i\tau)|^2,
\]

and proves that the complete (p^k)-tower is its transverse logarithmic
score.  This gives an exact bridge to the semilocal prolate programme.  The
primary literature proves the cyclic-pair and Sonin infrastructure but
does not prove the required global score monotonicity.  The structurally
distinct candidate theorem is now monotonicity of the support-localized
Christoffel--Darboux/prolate filtration under this score, after the two
Tate characters are removed, with its defect identity matched to D.190.
Positivity of the semilocal measure itself is not sufficient.

D.240 uses the two semilocal embeddings themselves.  The Euler map and the
inverse-Euler/Sonin map preserve an exact dual pairing, and differentiation
produces the prime scores with opposite signs.  Adding
\(L_\infty(s)=\pi^{-s/2}\Gamma(s/2)\) proves the closed-form identity

\[
 Q_T=-B_{{\rm nuc},T}^{\rm prim}
 =\Pi_TJ_T^*
 \left.\partial_\sigma\log|E_{S,\sigma}|^2
 \right|_{\sigma=1/2}J_T\Pi_T.
\]

Thus the full A--B--C form is exactly the logarithmic metric derivative of
the semilocal cyclic Hilbert bundle.  The scalar-form port, including Gamma,
all \(p^k\) and Tate, is complete.  The new porting theorem is sharper:
prove that the derivative of the **localized dual-pair conservation law**
has the D.190 positive defect factorization.  The unlocalized pairing
identity alone is indefinite and does not supply that sign.

D.241 completes the renewed two-projection audit in this enlarged metric
space.  If \(\mathsf P_\sigma\) is the orthogonal projection onto
\(G_\sigma^{1/2}P\mathcal H\), then

\[
 (I-P)\dot{\mathsf P}_{1/2}P={1\over2}(I-P)Q_TP.
\]

Thus the D.190 commutator really is a tangent block of a projection.
However, the exact two-projection identity pays the second-order angle Gram
\(\frac14PQ_T(I-P)Q_TP\), while sharp Douglas requires the first-order
born score after the old-score Green.  A two-dimensional counterexample
proves that ambient metric positivity and the projection identity do not
imply that first-order Schur sign.  The exact residual remains

\[
 B_E-(P_OQ_TP_E)^*(P_OQ_TP_O)^\dagger(P_OQ_TP_E).
\]

The projection route is therefore **PARTIAL**: it constructs and
normalizes the coupling, but the remaining theorem is a source-specific
semilocal curvature/monotonicity identity for this residual.

D.242 now proves that the natural Euler \(\sigma\)-deformation is not a
differentiable family of self-Fourier Sonin embeddings.  For
\(v_c=\epsilon_0-c\epsilon_1\),

\[
 \mathcal F_pv_c-v_c=(c-p^{-1})w_p,\qquad
 w_p=\epsilon_0+\epsilon_1-(p-1)\sum_{j\le-1}\epsilon_j.
\]

The inverse-Euler numerator at weight \(\sigma\) requires
\(c=p^{-\sigma-1/2}\), so self-duality holds only at
\(\sigma=\tfrac12\).  Its exact first anomaly is
\(-(\log p)p^{-1}w_p\), with
\(\mathcal F_pw_p=-w_p\) and
\(\|w_p\|^2=2(p-1)\).  Distinct prime anomaly summands are orthogonal before
adelic quotient and support compression.  Therefore generic monotonicity
of a family of Sonin spaces is removed from the route.  The active source
comparison is sharper: transport this explicit anti-self-dual anomaly
through quotient, support and Gamma, and compare its corrected Gram with
the D.190 residual.  Any remaining term is the next strictly smaller
obstruction.

D.243 constructs the canonical dual-Euler oblique projection
\(\mathsf E_\sigma=\eta_\sigma P\eta_\sigma^{-1}\).  Its tangent has the
correct first-order type:

\[
 P Q_T(I-P)
 =P(\dot{\mathsf E}^{\,*}-\dot{\mathsf E})(I-P).
\]

Thus the complete D.190 coupling is now derived from a source-defined
idempotent, including Gamma and all prime powers.  A \(2\times2\)
counterexample proves that idempotence alone does not control the diagonal
score blocks and hence does not imply the sharp Schur sign.  The active
calculation is the Fourier-compatible/anti-self-dual decomposition of this
tangent after quotient and support, with the D.242 anomaly as the explicit
finite-prime part.

D.244 proves a new source-side Hodge theorem.  Splitting the first local
Euler tangent into additive-Fourier parity channels gives equal local
energies.  After tensoring over a finite prime set, the odd channels are
mutually orthogonal and the even channels have coherent cross-prime
couplings.  Their signed Gram is

\[
 A_S\bigl(xx^*-\operatorname{diag}(|x_p|^2)\bigr),
 \qquad x_p=-{\log p\over p+1},
\]

and has inertia \((1,|S|-1,0)\) for \(|S|\ge2\), proved without zeros or a
sign assumption.  This is not yet row D because it is an unlocalized
second-order tangent form.  The active port is now precisely the
Fisher-normalized, support-compressed, old-shorted comparison of this form
with the D.190 residual, including Gamma and the two Tate equations.

D.245 fixes the first-order normalization.  If
\(h_p=I-p^{-1/2}U_p\) is the central inverse-Euler state and \(d_{p,+}\)
its Fourier-even tangent, then

\[
 (\log p)(P_{p^{-1/2}}-I)
 =2d_{p,+}(h_p^*)^{-1}.
\]

The right side is the even-tangent/dual-central pairing and expands to all
\((\log p)p^{-k/2}(U_p^k+U_p^{*k})\).  Thus the tangent construction now
ports exactly to the first-order A--B--C prime score; the wrong
\((\log p)^2\) scaling arose only when the tangent was squared.  The
remaining carrying theorem is the multi-place tensor/Gamma/support
comparison of the D.244 contraction with D.190.

D.246 proves the archimedean analogue.  For the self-Fourier Gaussian
\(g_0=e^{-\pi x^2}\), its logarithmic tangent
\(d_\infty=(\log|x|)g_0\), and
\(d_{\infty,+}=(d_\infty+\mathcal Fd_\infty)/2\),

\[
 {2\mathcal Md_{\infty,+}(s)\over\mathcal Mg_0(s)}
 =2\operatorname{Re}{L_\infty'(s)\over L_\infty(s)}
 \quad(\operatorname{Re}s=\tfrac12).
\]

This is the complete Gamma/digamma score.  Hence the source tangent--dual
pair now recovers all finite places and infinity, and necessarily uses
the local Tate functional equations.  The remaining theorem has been
narrowed to compatibility of this already-complete local port with
support/Tate compression and old-core Schur shorting.

D.247 upgrades the D.244 signature to an exact conservative colligation.
With \(\mathcal E_\pm\) the odd/even tangent maps,

\[
 \|\widetilde{\mathcal E}_-z\|^2
 +\left|\sum_p\sqrt{\log p}\,z_p\right|^2
 =
 \|\widetilde{\mathcal E}_+z\|^2
 +\sum_p(\log p)|z_p|^2.
\]

The equality defines a canonical partial isometry before any
pseudoinverse.  On the degree-zero hyperplane it yields a sharp
contraction whose positive defect is exactly the reduced row-B contact,
including all powers through the orbit coordinate.  The sole carrying
comparison is now whether its support-compressed transfer colligation,
after adjoining D.246 Gamma and removing the two Tate channels, is the
D.190 old/born colligation.

D.248 identifies the prime component as a genuine scattering system.  The
Blaschke factor

\[
 b_p(U)={U-p^{-1/2}\over1-p^{-1/2}U}
\]

has positive Wigner--Smith delay
\(-i\partial_\theta\log b_p=P_{p^{-1/2}}\).  The arithmetic score is this
delay minus the free unit delay, explaining exactly the contact
cancellation of D.238.  The Gamma score is likewise the boundary phase
derivative of the local Tate scattering ratio.  The active carrying
theorem is therefore the differentiated support-defect identity for the
finite semilocal cascade.  Boundary unitarity alone is not enough, and
global completed-zeta causality is not assumed.

D.249 constructs the missing Gamma scattering network.  For
\(a_n=2n+\tfrac52\),

\[
 \operatorname{Re}\psi(\tfrac54+\tfrac{i\tau}{2})-\psi(\tfrac54)
 =\sum_{n\ge0}
 \left({2\over a_n}-{2a_n\over\tau^2+a_n^2}\right),
\]

and each \(2a_n/(\tau^2+a_n^2)\) is the positive delay of a half-plane
Blaschke colligation.  The load resolvent
\((\tau^2+1/4)^{-1}\) is the delay at \(a=1/2\), while the remaining scalar
is exactly \(\beta\).  Hence all local prime--Gamma conservative components
are explicit.  Their orthogonal sum is unitary, but the balanced Redheffer
wiring that couples degree, contact, prime score and Gamma score has not yet
been constructed.  After that wiring, the remaining comparison is its
support-compressed, Tate-shorted transfer defect versus the D.190 Schur
residual.

D.250 audits the attempted transport from the source tangent contraction
to the balanced D.137 features.  The exact odd intertwiner is

\[
 T_-={(\log p)p^{-1/2}\over2c_{p,-}}(I+U_p^*),
\]

which vanishes at \(U_p=-1\) although \(W_{p,-}\) does not.  The even
intertwiner likewise vanishes at \(\operatorname{Re}U_p=p^{-1/2}\).
Therefore the tangent contraction cannot be moved to \(X_T,Y_T\) through a
bounded inverse.  The full four-port colligation—odd plus degree versus
even plus contact—must be compared by state-space elimination, with Gamma
included.  This is the next exact algebraic target.

D.251 proves the abstract unitary transfer-defect theorem.  Any correctly
wired conservative network has a positive kernel satisfying sharp Douglas
with constant one and the supported-range condition.  It does not yet
construct the balanced wiring.  Once that wiring is available, the unique
carrying comparison is

\[
 B_E-X_{OE}^*A_O^\dagger X_{OE}
 =
 P_E\Pi_TK_S^{\rm tr}\Pi_TP_E,
\]

with old states and the two Tate ports eliminated in the same order.  The
next calculation must derive this equality or compute its exact residual;
no norm estimate is admissible before the state-elimination algebra is
fixed.

D.252 eliminates the naive version of that wiring.  For a prime
Blaschke factor \(b_r\), removing the free unit delay gives
\(c_r(z)=b_r(z)/z\), which has a pole at \(z=0\); its boundary delay
\(P_r-1\) changes sign.  Hence the relative Euler score is not a local
causal Schur defect, and orthogonally summing the local colligations cannot
produce D.190.  The only surviving transfer route is a global four-port
Redheffer feedback retaining the coherent degree/contact ports, the paired
Gamma renormalization and both Tate ports until the final short.

D.253 identifies the correct replacement category.  The relative factor
\(b_r/z\) has de Branges--Rovnyak kernel
\(u_r(w)^*u_r(z)-\bar w^{-1}z^{-1}\), hence exactly one negative square.
The next finite algebra is a degree/contact port change followed by a
Potapov--Ginzburg transform of this Pontryagin system, not an ordinary
Schur cascade.

D.254 then gives the exact prime cross-port wiring without a singular
inverse: the complete score is \(D^*B+B^*D\), and a fixed Hadamard
rotation of the dual central and even-tangent ports realizes it as a
difference of positive Grams, including all \(p^k\).  The remaining
prime-side task is to compose this rotation with the D.247
degree/contact colligation before closing any global port.

D.255 proves that the scalar product of the relative factors has negative
index equal to the number of active primes.  Hence neither a scalar
Euler-product cascade nor its rank-two Tate correction can be the desired
Schur system.  The growing matrix-valued contact port of D.247 is forced by
the index count.

D.256 identifies the only well-typed matrix port exchange.  Degree is the
coherent scalar component of the contact vector; the full degree/contact
pivot is rectangular and impossible.  Exchange the coherent rank-one
component and retain its orthogonal contact complement as the primitive
positive defect.

D.257 proves that the tensor dual-central state selects precisely this
single coherent prime port: spectator Euler factors cancel exactly, and
the remaining weighted covector is the torsion-normalized arithmetic
degree.  The finite prime port diagram is therefore complete before the
semilocal/Gamma/support/Tate transport.

D.258 separates prime-index rank from Hilbert rank.  The coherent channel
is a single prime-index port but an injective infinite-rank \(L^2\) map on
every primitive support window.  Tate removes only two feature directions;
the remaining feedback is necessarily operator-valued.

D.259 proves that the pointwise degree-zero condition of the finite tangent
Hodge theorem is strictly stronger than the two global Tate moments.
Therefore D.244 pays the primitive contact component but not the coherent
\(L^2\) boundary channel; the latter is the exact remaining capacity.

D.260 identifies that coherent channel as one centered arithmetic measure:
\(E_N(s)=\int_{[1,N]}x^{-s}\,d(\Psi(x)-x+1)\), including its endpoint
Volterra term.  The carrying theorem is now a Green-energy transport of
this measure, not a sum of independent prime-power estimates.

D.261 writes the exact remaining inverse as the Green energy of that
measure, including its cross with the complete Gamma/endpoint column.  The
only admissible next manipulation is a joint square completion with the
born budget; separate estimates would lose the sharp cancellation.

### Referee-proposal triage after D.214

Five external reports were compared with the typed reductions D.190--D.214.
Their suggestions have the following status.

* Defining ``sections'' as vectors whose return load already satisfies the
  resolvent identity does not create effectivity: membership requires the
  range/capacity assertion being proved.  The resulting mixed
  Riemann--Roch argument is circular and is **DISCARDED**.
* Taking a formal pushout with a mixed nuclear module constructs an object,
  but does not prove that its determinant is \(B_{\rm nuc}\), that its
  section dimensions are effective, or that it satisfies mixed
  Riemann--Roch.  Those assertions restate row D and are **NOT INPUTS**.
* PNT, shift-chain coercivity and separate Witt-moment bounds are shared by
  counterfactual Beurling systems.  They may estimate pieces but cannot by
  themselves prove the sharp sign.  Every proposed closing lemma must pass
  the existing counterfactual harness.
* The viable structural requirement is equality-critical: an exact defect
  identity, sum rule, or Poisson/adelic dilation must produce the constant
  one without assuming the spectral sign.  Gamma must enter coupled to the
  complete centered column, not merely as a scalar positive majorant.

Accordingly the next porting lemma is not an abstract ``mixed section
functor''.  It is the source-level estimate

\[
 q_N^*D_N^\dagger q_N\le \mathcal M_N,
 \qquad
 \mathcal M_N=I-y_N^*y_N-h_N^*D_Nh_N
       +2\operatorname {Re}(h_N^*q_N),
\]

for the complete Poisson--prime--Gamma centered column at every birth.  A
candidate proof is admissible only if it gives a factorization of the
difference \(\mathcal M_N-q_N^*D_N^\dagger q_N\) by source-defined
operators and survives domain, range and completion checks.

## Phase IV: exact atlas, after the symbolic model exists

At consecutive prime-power births (q_j=p^k), compute with adaptive
precision:

* the sharp regularized Douglas constant;
* principal angles of old defect and born load ranges;
* the spectrum of (A_NA_N^*);
* the residual of the proposed colligation identity;
* the effect of removing Tate, Gamma, or one contact at a time;
* the equality candidates.

The atlas is used to falsify the proposed identity and detect the correct
normalization.  Every entry is labelled **NUMERICAL EVIDENCE** unless an
interval enclosure proves a finite statement.

## Phase V: asymptotic theorem

After the exact colligation is identified, reparametrize exclusively by
the ordered prime powers

\[
q_1<q_2<\cdots,\qquad \tau_j=\tfrac12\log q_j.
\]

Prove that no operator change is lost between consecutive births.  Then
prove the sharp contraction for every sufficiently large (j).  The
target is (\|v_{q_j}\|\le1), not a uniform strict gap.  If equality is
possible, identify its structural subspace during this phase.

## Phase VI: finite remainder

1. Complete the corrected three-block Feshbach certificate at
   (T=\frac12\log5), including (A_{SQ}),
   (C_D=A_{DQ}-A_{DS}A_{SS}^{-1}A_{SQ}), and the full complement loss.
2. Interval-certify every birth below the effective asymptotic threshold.
3. Freeze all bases, interval matrices, congruences, tail bounds and hashes
   needed for independent reproduction.

These certificates prove only the finite remainder; they do not replace
the asymptotic theorem.

## Phase VII: propagation and equality

Combine:

1. the proved initial interval (0<T\le\log2);
2. zero-extension nesting;
3. the exact birth identity;
4. the source-defined sharp Douglas contraction at every birth;
5. the finite interval certificates.

This yields (Q_T\ge0) for every (T).  Then classify

\[
\ker Q_T
\]

from the equality kernel of the colligation.  Verify that only the known
polar/radical modes remain and that they are removed on (\mathcal T^0).

## Phase VIII: paper integration

Only after Phases II--VI are proved:

* add the global theorem to paper 42;
* include all operator domains, range conditions and completion arguments;
* distinguish algebraic identities, interval certificates and analytic
  theorems;
* state the RH consequence as an application of the already proved Weil
  criterion, without using it in the construction.

## Stop/go rules

* The local Hankel/Poisson route is already abandoned by D.195--D.197.
* Do not define a contraction by (D_{\rm out}^{\dagger/2}y_N); that is
  the theorem, not its construction.
* Do not infer the unit bound from summability.
* Do not seek a uniform strict gap if the sharp constants approach one.
* Test every structural lemma on a Beurling surrogate with off-line zeros;
  if it survives unchanged, it cannot alone close D.
* Do not modify the paper while the central contraction remains open.
