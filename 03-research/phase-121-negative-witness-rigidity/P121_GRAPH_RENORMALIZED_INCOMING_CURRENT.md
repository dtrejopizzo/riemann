# P121 -- graph-renormalized incoming current

## Status

This note closes the existence and uniqueness of the **completed** incoming
boundary attached to a first-contact state.  It removes the conditional
wording in Section 3 of `P121_STRONG_COMMUTATOR_AND_FLUX_NO_GO.md` at the
level at which the global commutator is actually defined: the common closed
graph of the zeta observation and the Gamma generator.

It does not assert convergence of the literal one-sided series v94 (452).
That series separates two individually divergent Euler orientations and is
not the definition of the completed boundary.  Any realization of that
series which is compatible with the closed graph is, however, forced to
equal the current constructed here.

## 1. Data already proved

Let `F` be a parity first-contact state on `I_T=(-T,T)`, let `u=E_TF` be
its zero extension, and write

\[
 \mathfrak Z=\zeta(\tfrac12+iD),\qquad
 D_\Gamma=d_\Gamma(D),\qquad
 h=\mathcal Z_{T,+}F.                              \tag{1.1}
\]

Phase 121 proves the simultaneous graph membership

\[
 u\in\operatorname {Dom}(\mathfrak ZD_\Gamma)
       \cap\operatorname {Dom}(D_\Gamma\mathfrak Z)       \tag{1.2}
\]

and the strong identity

\[
 [\mathfrak Z,D_\Gamma]u=0\quad\hbox{in }L^2(\mathbb R).
                                                               \tag{1.3}
\]

The compressed zero-mode equation is

\[
 P_T\mathcal A_\infty u=r_\varepsilon,              \tag{1.4}
\]

where `r_epsilon` is in the two-dimensional Tate space (one-dimensional
after parity is fixed).  The local causal operator `mathcal Z_(T,+)` is a
bounded finite sum on `L2(I_T)`.

## 2. Canonical completed split

### Theorem 2.1 -- graph-renormalized incoming current

For every parity first-contact state define

\[
 \boxed{
 \mathcal L^{\rm gr}_{T,-}(F)
 :=P_T[\mathfrak Z,D_\Gamma]u
   -\mathcal Z_{T,+}P_T\mathcal A_\infty u.}        \tag{2.1}
\]

Then `mathcal L^(gr)_(T,-)(F)` is a canonically defined element of
`L2(I_T)` and

\[
 \boxed{
 \mathcal L^{\rm gr}_{T,-}(F)
 =-\mathcal Z_{T,+}r_\varepsilon.}                  \tag{2.2}
\]

In particular the completed incoming current belongs to the image of the
Tate forcing space.  Its dimension is at most two before parity and at most
one in either parity sector.

#### Proof

The first term in (2.1) is defined in `L2(R)` by the common closed graph
(1.2), and restriction to `I_T` is bounded.  The second term is defined in
`L2(I_T)` because (1.4) belongs to `L2(I_T)` and
`mathcal Z_(T,+)` is bounded.  Thus (2.1) is well typed and independent of
any choice of smooth approximation or contour.

Equation (1.3) makes the first term zero.  Substitution of (1.4) proves
(2.2).  The rank statement follows because the right side is the image of
the two-dimensional Tate space, and parity reduces that space to the line
spanned by `cosh(t/2)` or `sinh(t/2)`.  QED.

### Corollary 2.2 -- uniqueness of every compatible causal realization

Suppose a regularization of the literal incoming series in v94 (452)
produces an `L2(I_T)` boundary `L_(T,-)(F)` and satisfies the physical split

\[
 P_T[\mathfrak Z,D_\Gamma]u
 =\mathcal Z_{T,+}P_T\mathcal A_\infty u
  +\mathcal L_{T,-}(F).                              \tag{2.3}
\]

Then

\[
 \mathcal L_{T,-}(F)=\mathcal L^{\rm gr}_{T,-}(F)
 =-\mathcal Z_{T,+}r_\varepsilon.                   \tag{2.4}
\]

#### Proof

Subtract the local term in (2.3).  The result is exactly the definition
(2.1), and Theorem 2.1 applies.  QED.

## 3. What this closes

The incoming boundary is no longer an unspecified infinite-dimensional
leakage.  On an equality state its completed value exists, is unique, and is
finite-rank:

```text
first-contact radical
 -> common zeta--Gamma graph
 -> unique completed incoming current
 -> current = -Z_(T,+) r_epsilon.
```

Thus a future annular theorem cannot obtain rigidity by merely defining,
regularizing, estimating, or choosing the incoming current.  Its value is
already forced.

## 4. What remains open

Equation (2.2) is a conservation law.  It does not imply `h=0`; substituting
it into the global commutator recovers the zero identity.  The remaining
theorem must establish an Euler-specific compatibility between the forced
Tate current (2.2) and the observed amplitude `h` solving v94 (445).

Nor does Theorem 2.1 prove that the unregularized series (452) converges.
The separated orientations are not expected to possess independent `L2`
limits.  The theorem says that their completed physical boundary is already
defined by the closed source graph, and that every legitimate separated
realization has the same value.

The global square and row (d) remain open.
