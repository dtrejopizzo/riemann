# D.25 — The renormalized polarization gate

## Purpose

The finite prime-root pages and the Gamma oscillator carry candid positive
polarizations.  This note determines exactly what is, and what is not,
automatic when those finite polarizations are passed to the resonant
degree-one quotient used by the nuclear Lefschetz formula.

The conclusion is a useful reduction, not a proof of the Hodge sign.  A
compatible complex structure exists automatically for every *strong*
symplectic Hilbert realization.  The force-bearing assertion is that the
renormalized scale action is uniformly bounded on one such realization and
that the resonant quotient is closed in its norm.  That assertion implies
RH and therefore must not be smuggled into the construction of the norm.

## 1. Polar decomposition on a strong symplectic Hilbert space

Let `(H,g_0)` be a real Hilbert space and let `Omega` be a continuous
alternating form.  Write

```text
Omega(x,y)=g_0(Ax,y),
```

where `A*=-A`.  Assume that `A` is boundedly invertible (equivalently,
`Omega` is strong symplectic).  Put

```text
|A|=(-A^2)^(1/2),             J=-A|A|^(-1).
```

Then

```text
J^2=-I,       J*J=I,          Omega(x,Jy)=g_0(|A|x,y).
```

In particular `g_Omega(x,y)=Omega(x,Jy)` is a faithful positive Hilbert
metric equivalent to `g_0`.

### Proof

Since `A` is normal, `A` commutes with every bounded Borel function of
`-A^2`, hence with `|A|`.  Therefore

```text
J^2=A^2|A|^(-2)=-I,
J*J=|A|^(-1)(-A)A|A|^(-1)=I.
```

Finally

```text
Omega(x,Jy)=g_0(Ax,-A|A|^(-1)y)
            =g_0(x,-A* A|A|^(-1)y)
            =g_0(x,|A|y).
```

This proves all claims.

The finite root-graph pages satisfy these hypotheses.  Thus no finite-level
Hodge theorem is missing: the finite complex structures can also be
recovered canonically by polar decomposition.

## 2. Equivariant polar decomposition

Let `U_t` be a strongly continuous group on `H` preserving `Omega`.  If
`U_t` is unitary for `g_0`, then it commutes with `A`, `|A|`, and `J`.

Indeed,

```text
g_0(AU_t x,U_t y)=Omega(U_t x,U_t y)=Omega(x,y)=g_0(Ax,y),
```

and unitarity gives `U_t^* A U_t=A`.  Functional calculus gives the other
commutations.  Consequently the polar metric `g_Omega` is also
`U_t`-invariant.

This identifies a sufficient construction of row D:

1. construct a Hilbert norm `g_0` on the separated resonant quotient;
2. prove the normalized scale group is unitary (or first uniformly bounded);
3. prove the descended alternating form is strong symplectic.

Step 2 is not formal.

## 3. Amenable unitarization and its exact hypothesis

For completeness, suppose only that

```text
sup_(t in R) ||U_t|| <= M < infinity.                 (3.1)
```

Because `R` is amenable, choose an invariant mean `m` and define

```text
g_1(x,y)=m_t g_0(U_t x,U_t y).
```

Then

```text
M^(-2) g_0(x,x) <= g_1(x,x) <= M^2 g_0(x,x),
```

and `U_t` is unitary for `g_1`.  Applying the equivariant polar
decomposition to `g_1` produces the desired invariant polarization.

Thus a uniformly bounded Hilbert realization is enough; an initially
unitary one is not required.

## 4. Why uniform boundedness is already the critical-line gate

Let a nonzero resonant class `v_rho` satisfy

```text
theta_t v_rho = exp(t rho) v_rho,
U_t=exp(-t/2) theta_t.
```

Then

```text
||U_t v_rho||=exp(t(Re rho-1/2)) ||v_rho||.
```

If (3.1) holds for positive and negative `t`, necessarily
`Re rho=1/2`.  Hence uniform boundedness on a faithful completion already
implies that every represented zeta resonance lies on the critical line.

This proves the following exact gate.

### Theorem (renormalized polarization gate)

Assume the A--B--C resonant quotient has a faithful Hilbert realization
with:

* a continuous strong symplectic descended Lefschetz form;
* a normalized scale group `U_t` that is uniformly bounded for all real
  `t`;
* a closed quotient map, so that no nonzero resonant class is killed by
  completion.

Then the polar-decomposition construction above gives a global Hodge
polarization, and all nontrivial zeros of zeta have real part `1/2`.

Conversely, any proposed direct-limit construction of the polarization
must prove these three bullets without using the location of the zeros.

## 5. Audit of the Poisson renormalization

The local outer factor

```text
a_r(z)=sqrt(1-r^2)/(1-rz)
```

unitarily trivializes the Poisson measure at a single prime.  A finite
product therefore changes coordinates unitarily.  At the critical Euler
boundary,

```text
sum_p r_p^2 = sum_p 1/p = infinity.
```

Hence the infinite tensor product relative to the unweighted vacuum is not
a bounded perturbation of the reference product.  Choosing a new vacuum
does produce an infinite tensor product representation, but comparison
with the resonant quotient then requires precisely:

```text
sup_t ||U_t|| < infinity
```

and closedness of the quotient map.  Local outer-factor positivity alone
does not establish either statement.

## 6. Consequence for the next construction

The remaining admissible route is narrower than a generic direct limit.
One needs a **source-side norm**, defined before the zeta resonances are
read, for which:

```text
(i)  the prime and Gamma boundary are renormalized jointly;
(ii) translations act with a uniform two-sided bound;
(iii) the Meyer/CCM quotient has closed range;
(iv) Omega is boundedly nondegenerate on that quotient.
```

The signed Poisson factorization of D.23 supplies (i) at every finite
support.  It does not yet supply (ii)--(iv).  Those are the next precise
targets; none may be replaced by an assumption of positivity or by an
invariant mean before uniform boundedness has been proved.

