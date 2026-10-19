# R170_874 — The Tate cocycle does not determine the exterior class

## 0. Verdict

> **Correction R170_876.** The pure linear extension proposed in §3 is
> sufficient but not physically compatible: the swap fixes `LS-K`, but
> transforms `A_L=M-(L+L*)` into `A_S=M-(S+S*)`. The correct target is a
> covariant law with the explicit cocycle `S A_L-L A_S`, not an
> involution that literally fixes the physical datum.

R170_873 correctly identifies the virial jet with the derivative of the
Tate cocycle

\[
 c_n(s)={\Lambda(n)\over\sqrt n}(n^s,n^{-s}).              \tag{0.1}
\]

This datum, even together with the swap \(s\leftrightarrow-s\), does not
determine the gauge-invariant class

\[
 \Theta_{\rm ext}(F),\qquad
 g\Delta^{\rm Tate}(F)=\mathfrak W_K(F)+\Theta_{\rm ext}(F).\tag{0.2}
\]

The reason is algebraic: the cocycle acts on the already-factored Tate
port, while \(\Theta_{\rm ext}\) is a coordinate of the boundary
quotient of R170_869. It is proved below that this coordinate can be
varied arbitrarily while preserving the cocycle, its jet, the arithmetic
line \((\Lambda,1)\), linear PC, and diagonal minimality.

Hence the next law cannot be only modular covariance. It must construct
an action of the swap on the **physical exterior port** and prove that
this action is the one induced by PC-ren.

## 1. Independent extension lemma

Let \(E_N=\mathbb R^{N}\oplus\mathbb R\), let

\[
 D_N(a,c)=\big((a*1)(k)-c\log k\big)_{k\le N},             \tag{1.1}
\]

and let \(L_N=\ker D_N=\mathbb R(\Lambda,1)\), by R170_866.
Let \(V_T\) be any physical space and \(J_s\) any family of
operators on a Tate port \(U_T\) realizing (0.1). For every linear
form \(\beta\in V_T^*\), define the enlarged port

\[
 \mathcal E_\beta((a,c)\otimes F)
   =\big(D_N(a,c)\otimes F,\;c\,\beta(F)\big).              \tag{1.2}
\]

Then:

1. the restriction of \(\mathcal E_\beta\) to the normal ideal
   \(\operatorname{im}D_N\) is independent of \(\beta\);
2. its restriction to the arithmetic line is
   \[
   \mathcal E_\beta((\Lambda,1)\otimes F)=(0,\beta(F));     \tag{1.3}
   \]
3. the family \(J_s\), its involution, and its derivative can be kept
   identical for every choice of \(\beta\);
4. any positive form or first-contact family defined only
   on the first component of (1.2) also stays identical.

### Proof

Items 1 and 2 follow from \(D_N(\Lambda,1)=0\). In (1.2), \(J_s\)
acts on a summand distinct from the last coordinate, so changing
\(\beta\) modifies neither \(J_s\) nor its jets. Finally, a form that
factors through \(D_N\) ignores the second coordinate. All statements
are direct identities. \(\square\)

## 2. Application to the exterior defect

R170_868--870 prove, in the coefficient model classified there, that
every row annihilating the arithmetic line factors through the first component
of (1.2), while the boundary-augmented restriction to the radical is the
class

\[
 \beta_{\rm phys}(F)=\mathfrak W_K(F)+\Theta_{\rm ext}(F). \tag{2.1}
\]

Take two functionals \(\beta_1\ne\beta_2\). The lemma builds two
models with:

* the same exact values of \(\Lambda(n)\) up to \(N\);
* the same identity \(\Lambda*1=\log\);
* the same cocycle (0.1) and the same jet
  \(\Lambda(n)\log n/\sqrt n\);
* the same interior operator, radical, and diagonal minimality cone;
* different exterior classes on \(L_N\).

Consequently, that data does not imply
\(\mathfrak W_K+\Theta_{\rm ext}=0\). This counter-model does not refute a
physical law that uses the literal action of PC-ren on the exterior; it
shows that such an action is indispensable additional information.

## 3. Minimal criterion for a valid continuation

Let \(\mathscr J\) be the factor swap in the hyperbolic complex.
The missing piece must construct an operator \(\widehat{\mathscr J}\)
on the full physical port such that, without defining it from
\(\beta_{\rm phys}\), one proves simultaneously

\[
 \widehat{\mathscr J}\,\mathcal E_{\rm phys}
 =\mathcal E_{\rm phys}\,\mathscr J,                       \tag{3.1}
\]

and

\[
 \operatorname{pr}_{\partial}\widehat{\mathscr J}=-1
 \quad\text{on the boundary coordinate},                    \tag{3.2}
\]

while the physical first-contact vector is fixed by the swap.
Then (3.1)--(3.2) would give

\[
 \beta_{\rm phys}(F)=-\beta_{\rm phys}(F)=0.               \tag{3.3}
\]

Equation (3.1) must be verified by expanding the terms
\(H_{M,N},K_N,C_N\), the moving atoms, and the Gamma collar. Postulating
the action \(-1\) on an added coordinate exactly reproduces the
freedom of (1.2) and is circular.

## 4. Status

```text
Tate cocycle and virial jet                                PRESERVED
independence of the boundary class from that data          PROVED
interior factor-swap determines Theta_ext                  REFUTED
criterion for a physical extension (3.1)--(3.2)             FORMULATED
literal extension from PC-ren                               OPEN
VIR--LB / D                                                 OPEN
```

The target is no longer "differentiate the cocycle": that was done. It is to prove
an exterior **naturality** of PC-ren that eliminates the freedom to add
\(\beta\).
