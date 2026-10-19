# R170_862 — Correct homogeneity: the law needs a bordered null anchor

## 0. Result

The Tate defect of R170_856--859 is linear in the first-contact vector.
In a real sector of fixed parity, set

\[
 \mathfrak L_T(f):=mathfrak W_K(f)+\Theta_{\rm ext}(f)
                  =g_\epsilon\Delta^{\rm Tate}(f).         \tag{0.1}
\]

All operators, the Tate residue `rho`, the outer port, and the
connections depend linearly on `f`; hence

\[
 \mathfrak L_T(cf_1+df_2)
 =c\mathfrak L_T(f_1)+d\mathfrak L_T(f_2).                 \tag{0.2}

By contrast, for a self-adjoint deformation `mathcal R`,

\[
 f\longmapsto(f,\dot{\mathcal R}f)                         \tag{0.3}

is quadratic. The diagonal provisionally proposed in R170_861(6.3)
cannot represent (0.1) uniformly on the radical.

The correct homogeneous encoding is a mixed block

\[
 \boxed{\mathfrak L_T(f)=(a,\dot{\mathbb H}f)}             \tag{0.4}

against a boundary anchor `a`. The positivity of a family around the
contact point forces (0.4)=0 only if `a` also belongs to the kernel in
the contact fiber. The canonical Tate port has positive Gram and is not
that second null vector. Hence the new piece reduces to constructing,
from exact arithmetic, a **bordered null anchor** whose mixed jet is
the defect (0.1).

## 1. Linearity of the defect

R170_856(8.7) gives

\[
 g_\epsilon\Delta^{\rm Tate}(f)
 =(b,P\dot Af)-(h,P\mathcal C f)-\rho_f g_\epsilon.        \tag{1.1}

Here `b,h,g_epsilon` depend on the window and on parity, not on `f`;
`rho_f` is the linear coordinate determined by `PAf=rho_f b`; and
`mathcal C` is linear. This proves (0.2) directly, without REG.

Under REG/C1, R170_859 rewrites exactly the same functional as
`mathfrak W_K+Theta_ext`; the gauge transformation does not change its
degree of homogeneity. So any quadratic representation over `f` could
only hold after a nonlinear normalization or for a single vector, not
as a law of the radical.

## 2. Derivative lemma at the boundary of the positive cone

**Lemma 2.1.** Let `mathbb H(s)` be a `C1` family of self-adjoint forms
with common domain such that

\[
 \mathbb H(s)\ge0\qquad(|s|<s_0).                          \tag{2.1}

Let `N=ker mathbb H(0)`. Then

\[
 \boxed{P_N\dot{\mathbb H}(0)P_N=0.}                      \tag{2.2}

**Proof.** For `u in N`, the real function

\[
 \varphi_u(s)=(u,\mathbb H(s)u)                            \tag{2.3}

is non-negative on both sides and `varphi_u(0)=0`; hence
`varphi_u'(0)=0`. This cancels the diagonal of
`P_N dot{mathbb H}(0)P_N`. Real polarization cancels all of its mixed
entries. QED.

For a family positive only on `s<=0`, the same argument gives

\[
 P_N\dot{\mathbb H}(0)P_N\preceq0,                         \tag{2.4}

which is the minimality law used in R170_857. The cancellation requires
two sides or an equivalent second orientation.

## 3. Why the anchor must be null

If `f in N` and `a in N`, (2.2) implies

\[
 (a,\dot{\mathbb H}(0)f)=0.                               \tag{3.1}

This has exactly the homogeneity of (0.1). By contrast, if `a` is not
in `N`, bilateral positivity does not control the mixed term.

The following model is exact. In `R^2`, take

\[
 \mathbb H_c(s)=
 \begin{pmatrix}s^2c^2&sc\\sc&1\end{pmatrix}
 =\binom{sc}{1}\begin{pmatrix}sc&1\end{pmatrix}\ge0.      \tag{3.2}

At `s=0`, `f=e_1` is null and `a=e_2` has energy one. However,

\[
 (a,\dot{\mathbb H}_c(0)f)=c,                             \tag{3.3}

which can be any real number. Neither bilateral positivity nor the
Gram factorization signs the kernel--complement block.

This is the bordered analogue of the transverse falsifier of
R170_857.

## 4. Minimal boundary that would force the law

Formally enlarge the primitive space by a boundary coordinate:

\[
 \widehat{\mathfrak P}=\mathfrak P\oplus\mathbb R e_T,\qquad
 \widehat H_0=H\oplus0.                                   \tag{4.1}

Then

\[
 \ker\widehat H_0=\ker H\oplus\mathbb R e_T.             \tag{4.2}

A self-adjoint velocity with mixed block

\[
 (e_T,\dot{\widehat H}_0 f)=\mathfrak L_T(f)              \tag{4.3}

would be cancelled by Lemma 2.1 if a family
`widehat H(s)>=0` existed for both signs of `s`.

But artificially adding `0` and declaring (4.3) proves nothing. The
arithmetic obligation is to simultaneously construct:

1. a coordinate `e_T` produced by the integer comb and the ports, not
   added by hand;
2. the exact nullity `widehat H_0 e_T=0` from
   `Lambda*1=log` and the finite hyperbola;
3. the jet equality (4.3), including polar, Tate, and outer terms;
4. bilateral positivity at the new scale, or two orientations whose
   combination yields (2.2).

This is the **bordered null anchor law**. If constructed, (3.1) proves
`mathfrak L_T(f)=0` without estimates and closes the Tate defect.

## 5. The known Tate port is not the anchor

At fixed parity, the Tate column is `b=b_epsilon` and

\[
 g_\epsilon=\|b\|^2=4(\sinh T+\epsilon T)>0               \tag{5.1}

in the relevant windows. The causal dual `h=(PS^*P)^{-1}b` is also not
null in the physical metric. Using `b` or `h` as `e_T` falls exactly
into case (3.2): a positive-energy anchor does not receive the
cancellation of (2.2).

The first-contact equation

\[
 PAf=\rho_fb                                               \tag{5.2}

turns the port into a Lagrange multiplier, not a second radical
vector. Differentiating (5.2) as if `b` were null again assumes the
tangency that VIR--LB is trying to prove.

## 6. Where an arithmetic anchor could arise

The finite divisor identity does produce an exact zero:

\[
 H_{M,N}=L_MS_N-K_N
\quad\hbox{has no coefficients at }k\le N\quad(M\ge N).  \tag{6.1}

However, (6.1) is a nullity of interior coefficients, not a null vector
of a positive form. R170_856 also shows that its jet `K_-` cancels in
the full PC. Hence one cannot simply take
`e_T=H_{M,N}`.

The only route compatible with §4 would be a positive, bordered
realization of (6.1) in which:

* the cancelled interior channel becomes the null coordinate `e_T`;
* the tail `k>N` remains as a boundary flow;
* the mixed interior--boundary jet is exactly (1.1), not an isolated
  `K2`;
* the reflected orientation supplies the second side of positivity.

This acts on the hyperbola before recombining it, as the map of
R170_840 requires, but adds a condition that was previously missing:
the port must be null in the **same positive form**, not merely cancel
as a coefficient.

## 7. Falsifiers

A construction of `e_T` must fail in systems with first contact:

* for DH/DMV, the bordered positive identity or its nullity must break;
* for finite modifications of `Lambda`, the divisor defect in
  (6.1) must remove `e_T` from the kernel;
* for a positive eigenvector in an earlier window, `f` does not belong
  to the kernel and Lemma 2.1 does not cancel the mixed block.

So the mechanism, if it exists, passes filters F1 and F3: it uses both
minimality and the exact values of the integers.

## 8. Status

```text
linearity of g Delta_Tate in f                            PROVED
diagonal encoding via <f,Rdot f>                          REFUTED
bilateral lemma P_N dotH P_N=0                            PROVED
anchor outside the kernel receives cancellation           REFUTED
null boundary forces the mixed functional to zero         PROVED
Tate column b is a null anchor                            FALSE
interior cancellation of the hyperbola gives a null vector NOT PROVED
bordered null anchor law                                  SPECIFIED / OPEN
VIR--LB / D                                               OPEN
```
