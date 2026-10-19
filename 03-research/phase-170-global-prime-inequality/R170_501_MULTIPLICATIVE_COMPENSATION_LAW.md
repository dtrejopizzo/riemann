# R170_501 — Multiplicative compensation law and its sign limit

**Covariance and rigidity laws proved. The requested arithmetic
positivity law is not proved. D remains OPEN.**

No external literature was consulted. The attempt was checked against
R161_058 (double commutator), R162_205 (divisor defect in Green) and
R170_401 (response and tangency). No scientific priority is claimed.

## 1. Statement of the attempt

We seek to repair the quadratic defect of R170_401 without requiring
that the first variation alone annihilate the whole kernel. The
candidate is a coherent deformation: vary simultaneously the
multiplicative phases, Gamma, and the polar moments, preserving the
divisor identities.

An exact compensation law is obtained, but the audit shows that it is
a symmetry of the problem. It does not generate a new inequality.

## 2. Deformation that respects multiplication

For real θ, χ_θ(n)=n^{iθ} is completely multiplicative. If * denotes
Dirichlet convolution, then

$$ (a\chi_\theta)*(b\chi_\theta)=(a*b)\chi_\theta.$$

In particular, the exact divisor identity transports as

$$\boxed{(\Lambda\chi_\theta)*(\mathbf1\chi_\theta)
=(\log)\chi_\theta.}\tag{1}$$

This is a finite identity at each integer: in the term d|n,
χ_θ(d)χ_θ(n/d)=χ_θ(n). Changing only Λ and leaving the other factor
fixed would not be (1).

In H_T, let X be multiplication by t and U_θ=e^{iθX}. We define

$$W_\theta(F)=W_T(U_\theta F),\qquad
H_\theta=U_\theta^*HU_\theta,$$

where H is the operator associated with W_T. The full physical
expansion is

$$W_\theta(F)=\frac1{2\pi}\int m(\tau-\theta)|\widehat F(\tau)|^2d\tau
-2\sum_{n<e^{2T}}a_n\Re\big(n^{i\theta}c_F(\log n)\big)
+2\Re\big(A_\theta(F)\overline{B_\theta(F)}\big),\tag{2}$$

with A_θ(F)=∫F(t)e^{t/2+iθt}dt and B_θ(F)=∫F(t)e^{−t/2+iθt}dt.
Hence Gamma, the primes and the pole deform in the same form.

The modulations preserve 𝒟_T: shifting the frequency by θ changes
log(2+|τ|) by a comparable weight. Moreover m', m'', m''' are bounded
on ℝ: the derived series are uniformly majorized by multiples of
Σ_{j≥0}(j+1/4)⁻², ⁻³ and ⁻⁴, respectively. The difference H_θ−H admits
an expansion in bounded operators up to second order with remainder
O(|θ|³). The prime terms are finite and the polar moments have
bounded support.

## 3. The second-order compensation law

We write

$$H_\theta=H+\theta V+\theta^2R+O(|\theta|^3),$$
$$V=i[H,X],\qquad
R=XHX-\tfrac12(HX^2+X^2H).\tag{3}$$

These formulas can first be read as forms. The boundedness of their
commutators allows them to be extended to the bounded operators of the
earlier expansion; X preserves the domain of the operator H.

Assume conditionally a contact point: H≥0, P projects onto ker H,
Q=I−P and H_Q≥ηI on QH. Then

$$PVP=0,\qquad QVP=iH_QQXP.$$

**Theorem 1 — Exact compensation.**

$$\boxed{PRP=PVQH_Q^{-1}QVP.}\tag{4}$$

**Proof.** From HP=PH=0 we obtain PRP=PXHXP. On the other hand,
QVP=iH_QQXP and PVQ=(QVP)*. Substituting into the right-hand side
gives PXQH_QQXP=PXHXP. ∎

The right-hand side is precisely the cost of the coupling to the
complement. In the Schur expansion of H_θ over the kernel,

$$\theta PVP+\theta^2
\big(PRP-PVQH_Q^{-1}QVP\big)+O(|\theta|^3),$$

both coefficients vanish. This answers the quadratic loss of
R170_401: a nonlinear deformation can compensate it without requiring
VP=0.

R can also be written using only the physical data. With
A_j=∫t^jF(t)e^{t/2}dt and B_j=∫t^jF(t)e^{−t/2}dt,

$$R(F)=\frac1{4\pi}\int m''(\tau)|\widehat F(\tau)|^2d\tau
+\sum_n a_n(\log n)^2\Re c_F(\log n)
+2\Re(A_1\overline{B_1})
-\Re(A_2\overline{B_0}+A_0\overline{B_2}).\tag{5}$$

None of the terms of (5) is eliminated by an assumed isolated
positivity of the prime channel or of the pole.

## 4. Why the law does not force the sign

Exactly, for every θ,

$$\sigma(H_\theta)=\sigma(H),\qquad
\ker H_\theta=U_\theta^*\ker H.\tag{6}$$

The contact is not destroyed: it is transported. The compensation of
(4) has no positive excess and cannot be used as a contradiction.
The covariance (2), the expansion (3) and the invariance (6) also
hold for artificial weights that produce a negative form. The proof of
(4) does not use (1), only unitary conjugation and the contact
hypothesis.

Thus (1) is genuinely a multiplicative identity, but it is not the
step that produces the spectral balance. The candidate does not meet
the requirement of using the arithmetic of ℤ to impose a new sign.

This also does not authorize requiring a "positive excess" in (4): on
this orbit that excess is identically zero. A different law would have
to step outside this class of conjugations.

## 5. There are no independent local prime phases in this class

Unique factorization allows assigning independent phases χ(p)∈S¹ to
each prime and extending χ completely multiplicatively to ℕ. Can we
realize them via a local multiplication in the coordinate t and thus
obtain more directions than θ?

**Theorem 2 — Rigidity of global local phases.** Let v:ℝ→ℂ be
measurable, |v|=1 almost everywhere. Suppose

$$v(t+\log p)=\chi(p)v(t)\quad\text{almost everywhere, for every prime }p.$$

Then there exist real θ,φ such that

$$\boxed{v(t)=e^{i\phi}e^{i\theta t},\qquad\chi(p)=p^{i\theta}.}\tag{7}$$

**Proof.** Since v is bounded, it defines a tempered distribution. The
translation equations for p=2 and p=3 force its Fourier transform to
be supported in the intersection of the sets

$$\{\tau:e^{-i\tau\log2}=\chi(2)\},\qquad
\{\tau:e^{-i\tau\log3}=\chi(3)\}.$$

This intersection has at most one point: two distinct points would
imply log2/log3 rational, contradicting unique factorization in
2^a=3^b. It cannot be empty because v is not the zero distribution. A
distribution supported at a point is a finite combination of
derivatives of delta. By inverse transform, v is a polynomial times an
exponential. Boundedness forces that polynomial to be constant; |v|=1
fixes its modulus. The remaining equations give χ(p)=p^{iθ}. ∎

**Scope.** The theorem deals with local multipliers defined on the
whole of ℝ, compatible with every support. It does not deal with
nonlocal operators, auxiliary matrices, or different realizations for
each window. Nor does it claim that every family of phases has a local
realization: most assignments χ(p) do not have one.

Hence, within this class, introducing independent phases per prime
does not repair (4): every admissible local realization returns to the
modulation that preserves the spectrum.

## 6. What can and cannot be called an "arithmetic law"

A **compensation law** has been formulated and proved, with an
explicit multiplicative deformation. It is a kernel transport identity.
It is not the positivity law the problem asks for: using that name
without this distinction would hide the pending link.

R161_058 already contains the positivity of the double commutator in
the radical; R162_205 shows that inserting a divisor defect into a
Green identity does not create the missing sign. The present note
applies those warnings to the phase-170 coupling and adds the
classification of the admissible local multipliers in this
formulation. No claim is made of having created a new arithmetic
theory.

The outcome of the proof of this candidate is conclusive within its
scope: **local multiplicative modulation only preserves whatever sign
was already there; it does not determine it**. The contraction of
R170_301 for Λ and every T remains OPEN. No proof of the requested
sign law is available.

## 7. Verification

`verify_multiplicative_compensation.py` checks the twisted convolution,
the Schur compensation in a contact model, and the conservation of a
negative eigenvalue under conjugation. It includes an exact rational
check of the diagonal compensation. The remaining matrix checks are
floating-point and prove algebraic consistency, not RH.
