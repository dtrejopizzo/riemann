# R170_601 — Nonlocal compensation via divisor paths

**Construction and cost theorem proved;
global arithmetic inequality OPEN.** No external literature.

## 1. Candidate that departs from the modulations

We use R=R_T, Y=B_T⁻¹ᐟ²C_T¹ᐟ² from R170_301. These are explicit
operators of Gamma, the pole, and the window weights Λ; R is
self-adjoint and ‖R‖<1, without assuming RH. The sought contraction is

$$K=Y^*(I-R)^{-1}Y\le I.$$

The new candidate is a bounded self-adjoint operator Z, not necessarily
local nor commuting with R, that controls the energy along the paths.
We require two separate inequalities:

$$Z-RZR\ge I+R,\qquad Y^*ZY\le I.\tag{L}$$

The first pays for each step; the second bounds the energy that enters
the system. This formulation allows nonlocal mixing between primes and
Gamma. It is not a unitary conjugation of the physical operator.

However, (L) is for now a **certificate candidate**, not a proved
arithmetic law. What follows computes exactly what it costs to satisfy
it.

## 2. Minimum-cost theorem, even without commutativity

Let G=(I−R)⁻¹. Then G−RGR=I+R. If Z satisfies the first inequality,
define S=Z−RZR−(I+R)≥0.

**Theorem 1.** Every such Z necessarily has the form

$$\boxed{Z=G+\sum_{j=0}^\infty R^jSR^j\ge G.}\tag{1}$$

The series converges in norm. Conversely, for every bounded S≥0,
(1) defines a solution of Z−RZR=I+R+S.

**Proof.** D=Z−G satisfies D−RDR=S. Iterating M times,
D=Σ_{j=0}^{M−1}R^jSR^j+R^MDR^M. The last term converges to zero
because ‖R‖<1. Each term of the series is positive. Direct
substitution proves the converse. ZR=RZ was not assumed. ∎

Consequently, the second inequality of (L) is exactly

$$\boxed{K+O_S\le I,\qquad
O_S=\sum_{j\ge0}Y^*R^jSR^jY\ge0.}\tag{2}$$

**Interpretation.** A positive nonlocal compensation does not lower K:
it consumes part of I−K. Nonlocality alone does not create that
margin. The existence of some Z satisfying (L) is equivalent to K≤I,
because S=0 recovers Z=G. This equivalence is not presented as a proof
of K≤I.

## 3. The version that would detect a contact point

If Kx=x and (2) holds, then

$$0=\langle O_Sx,x\rangle
=\sum_{j\ge0}\|S^{1/2}R^jYx\|^2.$$

Hence all vectors S¹ᐟ²R^jYx vanish. An arithmetic construction of S
that detected every possible contact vector, together with an
independent proof of (2), would exclude the contact.

These are two distinct requirements: detecting the contact does not
pay the cost O_S. A correction S>0 chosen for its detection ability may
precisely violate the budget inequality still to be proved.

## 4. A concrete operator with divisor responses

For d=2,3 and N=ceil(e^{2T})−1, we form the operators from R170_401:

$$M_d=\sum_{k\le N/d}\frac{\mu(k)}{\sqrt{dk}}H_{dk},\qquad
A_d=B_T^{-1/2}M_dB_T^{-1/2}.$$

M_d is the vector response to a unit error in the divisor identity of
index d. Each M_d is a finite self-adjoint sum; A_d incorporates the
same Gamma/polar mediator from all paths. We define

$$D=[A_2,A_3],\qquad S_0=D^*D\ge0.\tag{3}$$

This candidate preserves the interactions between the two arithmetic
responses; it does not orthogonally separate their channels before the
commutator. If S₀≠0, one can normalize S=S₀/‖S₀‖ and test
Z_η=G+ηΣR^jSR^j, η≥0. Its cost is exactly

$$Y^*Z_\eta Y=K+\eta O_S.\tag{4}$$

The divisor identity justifies M_d, but it **does not** give the sign
of I−K−ηO_S. Nor has it been proved that S detects every possible
contact. The commutator may be zero or have a nontrivial kernel.

## 5. Construction test in finite models

`verify_nonlocal_storage.py` uses the same indicator subspaces as
R170_301. It solves the matrix equation exactly up to rounding: if
R=U diag(r_i) U*, the ij entry of the internal cost operator is

$$\left[U^*\Big(\sum_{j\ge0}R^jSR^j\Big)U\right]_{ab}
=\frac{(U^*SU)_{ab}}{1-r_ar_b}.$$

The equation Z−RZR=I+R+ηS, the positivity of the increment, and
equality (4) are checked. T=1 and 3/2 are tested with 24 and 48 cells.

In every matrix where the observed margin g=1−λ_max(K) is positive, we
choose η=g/(2‖O_S‖). Then (4) satisfies the matrix bound by
construction. **This choice uses the already computed margin:** it is
not an independent proof of its positivity nor a uniform formula for
the real primes. Refining the mesh requires re-evaluation.

The falsifier a₂=100 from R170_301 is also tested. There λ_max(K)>1,
and any η≥0 only increases K by the order of forms. The candidate
cannot repair the negative sign of that model. That checks the cost
theorem, not the inequality for Λ.

The floating-point results are stored in
`nonlocal_storage_diagnostics.json`. There is no certified control of
the Galerkin complement. An operator S built after discretizing must
also not be identified, without proof, with the continuum's compressed
S.

## 6. Relation to earlier attempts and result

The operator equation used is a Stein equation; no new general theorem
is claimed. The corpus already contains energy operators and passivity
arguments (106.133–135), and 106.105 fixes the cost of an exact
transfer. This note proves the minimum cost of this candidate in the
path variables of phase 170 and tests it with specific Möbius
operators. It does not change the status of those earlier results.

**Result of the attempt:** the nonlocal compensation was constructed
and its cost computed unambiguously. Adding a positive detection term
first requires proving a sufficient margin in I−K; it does not produce
one. The arithmetic identity that would pay that cost is still
unproved.

This rules out using (1) as a free improvement of the sign. It does
not rule out every nonlocal construction, nor does it prove that a new
arithmetic law is impossible. The global goal of phase 170 remains
OPEN.
