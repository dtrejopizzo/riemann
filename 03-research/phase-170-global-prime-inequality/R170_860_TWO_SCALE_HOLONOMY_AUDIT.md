# R170_860 — Audit of the alleged two-scale holonomy

## 0. Verdict

R170_859 leaves the intrinsic defect

\[
 g\Delta^{\rm Tate}=\mathfrak W_K(f)+\Theta_{\rm ext}(f). \tag{0.1}
\]

It is tempting to interpret the right-hand side as the circulation around
the rectangle formed by the Euler scale `r` and the integer comb scale
`q`. With the objects currently constructed, that interpretation
is false:

1. the rectangle of the mixed exterior function is an exact differential
   and its circulation is identically zero;
2. the physical spectral family depends on `r`, not on `q`, so that its
   `r-q` Berry curvature is zero;
3. `S(q)A(r)` does depend on both parameters, but it is neither self-adjoint
   nor does it define the positive radical whose minimality is used;
4. turning the `q` leg into an invertible congruence of the physical
   operator only transports the kernel and produces a pure gauge connection.

Therefore `Theta_ext` is, for now, a gauge-invariant connection
defect, not a proved holonomy. A Stokes law on the existing
families would repeat a signless identity. This record specifies the
additional object that would have to be constructed for a two-scale
curvature to have arithmetic content.

## 1. The scalar rectangle is exact

R170_854 introduces, with independent scales,

\[
 \mathscr B(r,s)=(q_r,z_s),                                \tag{1.1}
\]

and proves

\[
 (\partial_r-\partial_s)\mathscr B(1,1)
 = (\dot q^0,z)-(q,\dot z^0).                              \tag{1.2}
\]

The one-form `d mathscr B` is exact. For every rectangle `R` contained
in the domain of differentiability,

\[
 \boxed{\oint_{\partial R}d\mathscr B=0.}                  \tag{1.3}

This does not imply that (1.2) is zero. For example,
`mathscr B(r,s)=r` has zero circulation around every rectangle and
`(partial_r-partial_s)mathscr B=1`. The scalar Stokes identity does not
sign nor cancel the antidiagonal Wronskian.

The mixed derivatives also commute:

\[
 \partial_r\partial_s\mathscr B
 =\partial_s\partial_r\mathscr B,                          \tag{1.4}

but (1.2) contains different first derivatives. Confusing (1.4) with
the exterior law would be exactly assuming the reciprocity being sought.

## 2. There is still no second spectral family

In R170_847,

\[
 A(r)=\mathcal M_r-L(r)-L(r)^*                             \tag{2.1}
\]

is self-adjoint and contains the physical form. The comb parameter only
appears in

\[
 S(q),\quad E(r,q),\quad H(r,q),\quad K(r,q).               \tag{2.2}

Therefore the physical primitive compression `H_r` and its radical
projection `Z_r` satisfy

\[
 \partial_qH_r=0,\qquad \partial_qZ_r=0.                   \tag{2.3}

The two-parameter Berry curvature would be

\[
 \Omega_{rq}=Z[\partial_rZ,\partial_qZ]Z,                  \tag{2.4}

and (2.3) gives

\[
 \boxed{\Omega_{rq}=0.}                                    \tag{2.5}

The two-scale PC is an operator identity with two legs; it is not
a two-dimensional family of contact operators.

## 3. Why `S(q)A(r)` does not fix the problem

The quantity differentiated in R170_848 is

\[
 \mathcal K(r,q)=S(q)A(r),                                 \tag{3.1}

with antidiagonal curvature

\[
 \partial_-\mathcal K=S\dot A-\dot SA.                    \tag{3.2}

Although (3.2) contains the correct Wronskian, `mathcal K(r,q)` is not
self-adjoint. In general,

\[
 \mathcal K(r,q)^*=A(r)S(q)^*\ne S(q)A(r).                 \tag{3.3}

There is then no order `mathcal K>=0`, no orthogonal spectral projection
at zero, nor a variational principle to which minimality could be applied.

Hermitianizing (3.1) simultaneously introduces the adjoint orientation and
the support concomitants. R161_062--064 and R170_843--846 prove that
that recombination does not carry the Wronskian sign. Taking a square
produces the comb ratio or a sign-blind metric. For this reason (3.1) does not define
the missing connection.

## 4. Pure-gauge congruence theorem

The most natural candidate is to use the causal inverse to convert the
comb into a metric change. The following fact shows the limit of
that operation.

**Proposition 4.1.** Let `H(r)` be a family of self-adjoint forms and let
`G(q)` be a `C1` family of bounded invertible operators that transports
their form domains. Define the congruence

\[
 \widetilde H(r,q)=G(q)^*H(r)G(q).                         \tag{4.1}

Then:

1. `widetilde H(r,q)>=0` if and only if `H(r)>=0`;
2. `ker widetilde H(r,q)=G(q)^{-1}ker H(r)`;
3. every `q` variation of the radical is transport by `G(q)^{-1}` and
   imposes no new restriction on `H(r)`;
4. the `q` direction can locally be trivialized by the coordinate
   change `u mapsto G(q)u`.

**Proof.** For every `u`,

\[
 (u,\widetilde Hu)=(G(q)u,H(r)G(q)u),                      \tag{4.2}

which proves 1. The equality is zero exactly when `G(q)u` is in
the kernel of `H(r)`, proving 2. Points 3--4 follow by applying the
invertible trivialization `G(q)`; under it (4.1) becomes `H(r)` again and does
not depend on `q`. QED.

In particular, using `G(q)=PS(q)P` or its Mobius inverse, when they are
defined on the window and preserve the relevant domain, only changes coordinates. It may redistribute
the sandwich of R170_858 and the connection of R170_859, but it does not prove (0.1)=0.

The congruence also does not by itself introduce the unique factorization:
any invertible causal comb would have the same property. The exact
values of `mu` appear when writing the coordinates, not in an intrinsic
curvature.

## 5. Specification of a non-trivial arithmetic connection

For a two-dimensional construction to be able to close (0.1), it must produce
a family `mathbb H(r,q)` satisfying at least:

1. **Self-adjointness and common domain.** `mathbb H(r,q)` is a family of
   self-adjoint `C1` forms near `(1,1)`.
2. **Physical fiber.** `mathbb H(r,1)=H_r`, including the Tate and polar
   correction.
3. **Non-congruent arithmetic leg.** The dependence on `q` cannot be
   `G(q)^*H_rG(q)` nor a unitary conjugation.
4. **Exact divisors.** Its mixed curvature uses `Lambda*1=log` at the
   level of integers and preserves the incomplete hyperbola.
5. **Typed boundary.** The contraction of its curvature on the contact
   vector is exactly `mathfrak W_K+Theta_ext`, with all the
   ports of R170_856.
6. **Orientation.** Some property valid before first contact
   orients the curvature integral; a Stokes identity alone is not
   enough.
7. **Falsifiers.** The property fails for DMV/DH and for the
   finite modifications that have first contact.

No current object satisfies 1--7 simultaneously. This list is not
declared a construction; it is the verifiable criterion that prevents calling
the already-known two-dimensional PC a "holonomy."

## 6. Reduction of the next search

After this audit, two non-equivalent options remain:

* directly prove the scalar identity (0.4) of R170_859 through
  a boundary law acting on `Theta_ext`;
* construct a family `mathbb H(r,q)` satisfying §5 whose curvature
  produces that identity.

The second option requires a new operator. Altering only `S(q)`, applying
Mobius, or hermitianizing `S(q)A(r)` belongs to the classes refuted in
§§3--4.

## 7. Status

```text
scalar rectangle dB has zero circulation                   PROVED
zero circulation implies zero antidiagonal Wronskian       REFUTED
r-q Berry curvature of the physical family                 ZERO
S(q)A(r) defines a self-adjoint contact family              FALSE
congruence by causal comb contributes new curvature         REFUTED
criteria 1--7 for a second connection                       FORMULATED
identity W_K+Theta_ext=0                                    OPEN
VIR--LB / D                                                 OPEN
```
