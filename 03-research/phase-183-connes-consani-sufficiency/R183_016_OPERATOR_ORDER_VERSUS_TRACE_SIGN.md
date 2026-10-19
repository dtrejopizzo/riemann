# R183.016 — The comparison must be of traces: operator order fails

## Scope and corpus

R183.015 fixes the modulus sector and proves trace class for smooth
tests. Phase 116's memo `previous-phase-114/114_d_138_FREDHOLM_TATE_DEFECT_AND_JULIA_GATE.md`
already distinguishes between the existence of a Fredholm object and the
sign of its form. Its operator is not the localized operator of this
file; its Schatten obstruction does not transport to this one. The
determinant is not presented here as a new proof of the sign.

Here we check R183.013 §5's proposal: comparing the two positive
operators B_1 and B_0 by order. That proposal is too strong even
after fixing a primitive test.

## Theorem — PROVED

Let S be a finite set of places containing infinity, u_S the Tate
product of R183.015, and h a nonzero function in C_c^∞(R). Let φ be its
Fourier transform and D_h=M_φ*(u_S* P u_S-P)M_φ. Then D_h, a compact
self-adjoint trace-class operator, has at least one positive and one
negative eigenvalue.

This remains true if h satisfies the two Tate moments and if
its support lies within the semilocal conjecture's window.

### Proof 1: kernel diagonal

Write u_S=e^{iθ_S}. By R183.015,

    K_h(s,s) = -|φ(s)|² θ'_S(s)/(2π),
    θ'_S(s) = m(s) - 2 Σ_{p in finite S} Σ_{k≥1}
                             (log p)p^(-k/2) cos(ks log p).

At zero, m(0)=ψ(1/4)-log π=-γ-π/2-3 log 2-log π<0.
All the prime summands being subtracted are positive. Hence θ'_S(0)<0,
and θ'_S is negative on some open interval around zero.

On the other hand, the prime sum is uniformly bounded in s for fixed S,
while m(s)=log(|s|/(2π))+o(1) as |s|→∞. Hence θ'_S(s)>0
for |s| large enough.

φ is entire and not identically zero, so it does not vanish on any
real interval. There exist real a,b with K_h(a,a)>0 and K_h(b,b)<0.
The kernel K_h is continuous. For a smooth, compactly supported real
function η with nonzero integral, take f_ε(s)=ε^(-1/2)η((s-a)/ε). Then

    <f_ε,D_h f_ε> = ε K_h(a,a)|∫η|² + o(ε).

It is positive for small ε. Centering at b gives a negative value.
By the spectral theorem for compact self-adjoint operators, D_h has
eigenvalues of both signs. The moment conditions on h do not alter any
step of this proof.

### Independent verification: dense range

φ only has isolated real zeros; M_φ has dense range in L²(R).
If M_φ* A M_φ≤0 for bounded A=u_S*Pu_S-P, continuity of A's form
on that dense range would imply A≤0. The same diagonal proof with a
nonzero Schwartz localizer near zero produces a positive vector for
A, a contradiction. The analogous argument at high frequencies excludes
A≥0. This confirms that no scalar condition on the moments of h can
turn the full sandwich into a fixed-sign operator.

## Precise consequence

The two proposals B_1≤B_0 and B_0≤B_1 both fail for every nonzero h of
this class. Hence a vector-by-vector contraction implying those
operator inequalities must not be sought.

This result does NOT refute Tr D_h≤0, does NOT refute a positive
representation of the scalar -Tr D_h, and does NOT refute the
Connes–Consani conjecture. The trace sums the eigenvalues of both
signs. The pending statement is

    Tr (D_h)_+ ≤ Tr (D_h)_-,

but defining these parts via spectral calculus does not constitute a
prespectral proof. An admissible proof must derive the total budget from
the Euler–Poisson data. Replacing the budget with operator order
incorrectly rules out the real possibility the conjecture leaves open.

## Status

Indefiniteness for every nonzero smooth test: PROVED, with two
verifications.
Operator order as a closing mechanism: NO-GO in this construction.
Scalar trace comparison from Euler–Poisson: OPEN.
Row D: OPEN.
