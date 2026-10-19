# R183.014 — Second audit: restoring the limit and the no-go's scope

## Theorem 1 — PROVED

Let H be a separable Hilbert space, P an orthogonal projection, U unitary,
and M bounded. Suppose D=M*(U*PU-P)M is trace class. For any sequence of
finite-rank orthogonal projections E_n with E_n → I strongly,

    Tr D = lim_n (||PUM E_n||_HS² - ||PM E_n||_HS²).

Proof. At finite rank the difference is Tr(E_n D E_n). To show
||E_n D E_n-D||_1 → 0, approximate D in trace norm by a finite-rank
operator K. The contribution of D-K is bounded by 2||D-K||_1. For K,
strong convergence of the projections implies uniform convergence on
its finite-dimensional range and corange spaces, hence convergence in
trace norm. Continuity of Tr concludes the proof.

Consequence: R183.012 improperly withdrew this limit on a supposed need
for cutoff compatibility. Under the hypothesis that D is trace class,
R183.002 recovers its limit with no additional renormalization. If only a
regularized trace is available, the hypothesis must be proved before
applying this theorem. A regularized trace is not automatically
identified with an ordinary trace.

## Theorem 2 — PROVED: exact scope of the cancellation

Suppose in addition that U commutes with M and M*. Write B=M*PM. Then

    M*U*PUM = U* B U,    D=U*BU-B.

If B is trace class, Tr D=0 by unitary invariance. This proves
R183.013's cancellation result without invoking cyclicity of products
whose trace-class membership was not justified.

It does not prove that D has no sign factorization, nor that a new
column Z with -Tr D=||Z||_HS² is impossible. Nor does it prove that only
determinants or indices remain. Those exclusions from R183.013 are
withdrawn.

## Exact sign control: abstract example — PROVED

In l²(Z), let P be the projection onto {e_k:k≥0}, U e_k=e_{k+1}, M=I.
Then U*PU-P is the projection onto e_{-1}, of trace +1. With U inverse,
the difference is minus the projection onto e_0, of trace -1. Both pairs
have B≥0, unitary equivalence, and a rank-one difference.

Their relative determinants are, respectively, 1+z and (1+z)^(-1), z≥0.
Hence positivity of B, unitary equivalence, and existence of the relative
determinant admit both signs. This example is NOT an arithmetic
falsifier: it only refutes an abstract deduction of the sign from those
three properties.

## Next obligation and status

The limit over columns is repaired. The pending construction remains
an Euler–Poisson source identity that signs Tr D on the Tate tests.
The relative determinant has derivative Tr D at zero; renaming that
derivative adds no inequality. There is no proof that this route closes D
nor a proof of impossibility for the route. D remains OPEN.

The semilocal application requires explicitly verifying the trace class
of the sandwich in the character sector and test domain used. The above
theorems are conditional on that hypothesis and do not replace it.

## Corpus update: the equality lift is already formulated

Phase 116's version `row_d_gamma_fourier_tate_v94_audit.tex` contains:

* (280)–(287): equivalence between the L² energy of the tails and an
  explicit bilateral Hardy condition, including its uniform budget;
* (298): the interior equation only determines the reflected symmetric
  part;
* (300)–(303): a Poisson lift only on the first-contact kernel suffices,
  conditionally, to close the reduction;
* (304)–(306): that lift requires equality of two semi-lifts on the
  common Meyer domain;
* (695)–(696): the interior, integer prehistory does not eliminate the
  critical residues of the tail's Abel energy.

Hence that lift is not proposed as a new R183 construction. Sonin
stability transports an already built lift, but does not prove its
existence. The formal equality H_F/ζ does not prove membership in the
source space nor the Hardy estimates (287). R183.015 resolves trace
class in the smooth modulus sector; it proves none of those three
points.

Comparing traces and lifting on the kernel are distinct sufficient
goals. No operator equivalence between them has been proved. Nor has a
new inequality been obtained via the determinant. The next advance must
supply one of these estimates or build the lift, not re-register its
definition.

## Balance of the candidates actually examined

1. Contractive return on each vector: incompatible with the
   indefiniteness proved in R183.016. The trace inequality is not thereby
   refuted.
2. Physical Poisson–Möbius factorization: not built; the formal
   inversion proves neither domains, boundedness, nor the identification
   with the scattering.
3. Relative determinant: well defined on R183.015's core, but the
   first derivative is the original goal. The second derivative is the
   semilocal energy of h*h (R183.013 §8), with no additional sign
   proved.
4. Monotonicity upon adding a prime with a fixed test: refuted by
   R183.015's two explicit primitive tests.
5. Transport via a prime's causal resolvent: bounded in L², but
   preserves neither compact support nor the positive-moment domain.
   The necessary cancellation is a whole periodization, not just its
   average.
6. Sonin transport: does not by itself give the equality lift nor the
   physical comparison; that obligation was already open in phase 116.

The domain checks and audit corrections are done within the stated
scopes. The goal's central requirement — building a positive
Euler–Poisson mechanism — is not met. None of these proofs is an
impossibility theorem for the Connes route in general. No additional
candidate is currently available whose construction completes that
requirement. Repeating the six formulations above with no new proved
hypothesis is not a sign advance.
