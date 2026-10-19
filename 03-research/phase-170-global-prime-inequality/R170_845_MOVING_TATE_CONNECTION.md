# R170_845 — The moving Tate connection: exact computation and remaining Ward–PC gate

> **Scope correction (R170_846).** Formulas (1.4)--(3.2) for the
> moving projection and for a symmetric operator are proved. The
> application of §4 to `mathfrak P_{N,N}^{ren}` was only conditional:
> R170_844 did not define that symbol as an operator. It cannot be
> identified with "the PC identity" without choosing one of its sides
> and a polarization. Defect (4.1) is therefore not defined until that
> choice is made.

## 0. Result

This record computes the term that R170_844 left formal under the
name `dot Pi_T`. After transporting `L^2(-rT,rT)` to the fixed window
`L^2(-T,T)`, the derivative of the primitive projection is
finite-dimensional. In each parity sector it has a single coordinate
on a primitive vector.

If `F` is primitive, has parity `epsilon`, and the first-contact
forcing is

\[
 r_F=\rho b_\epsilon,\qquad
 b_\epsilon(t)=e^{-t/2}+\epsilon e^{t/2},
\]

then

\[
 \boxed{
  2\operatorname{Re}\langle \dot\Pi_TF,r_F\rangle
  =-2\operatorname{Re}\langle F,t r_F'\rangle .}
 \tag{0.1}
\]

Hence the two exterior terms of the covariant derivative exactly
cancel the Tate virial when the Tate port of the differentiated PC
identity is literally `r_F`. The cancellation needs neither an
estimate nor a sign on the cross matrix.

What is still missing is not computing `dot Pi_T`: it is proving the
port equality

\[
 R_T\mathfrak P_{N,N}^{\rm ren}F=r_F                       \tag{0.2}
\]

in the relevant Ward--PC ordering, or computing its defect. Records
R161_063 and R170_844 forbid assuming (0.2) from a static compression.

## 1. Transport to the fixed window

Use the dilation unitary from `L^2(-rT,rT)` to `L^2(-T,T)`. A common
scalar factor does not change the Tate subspace, so its two
transported columns can be taken as

\[
 \phi_-(r,t)=e^{-rt/2},\qquad
 \phi_+(r,t)=e^{rt/2}.
 \tag{1.1}
\]

Let `Phi_r:C^2 -> L^2(-T,T)` be the synthesis of these columns and

\[
 G_r=\Phi_r^*\Phi_r,
 \qquad R_r=\Phi_rG_r^{-1}\Phi_r^*,
 \qquad \Pi_r=I-R_r.
 \tag{1.2}
\]

At `r=1`,

\[
 G_T=2\begin{pmatrix}\sinh T&T\\T&\sinh T\end{pmatrix},
 \tag{1.3}
\]

which is the positive Gram of R161_023, not the cross Gram.

Differentiating (1.2) gives

\[
 \dot\Pi
 =-\dot\Phi G^{-1}\Phi^*
   -\Phi G^{-1}\dot\Phi^*
   +\Phi G^{-1}\dot G G^{-1}\Phi^*.
 \tag{1.4}
\]

If `F` is primitive, `Phi^*F=0`, and two terms vanish:

\[
 \boxed{\dot\Pi F=-\Phi G^{-1}\dot\Phi^*F.}
 \tag{1.5}
\]

This is the complete formula for the connection on the primitive
fiber. It also verifies `Pi dotPi Pi=0`: the velocity of a primitive
vector points into the Tate space.

## 2. Reduction by parity

In the sector `epsilon in {+1,-1}` set

\[
 b_\epsilon(r,t)=e^{-rt/2}+\epsilon e^{rt/2}.
 \tag{2.1}
\]

At `r=1`,

\[
 q_\epsilon(T):=\|b_\epsilon\|^2
 =4(\sinh T+\epsilon T)>0,
 \tag{2.2}
\]

and

\[
 \dot b_\epsilon(t)
 ={t\over2}(-e^{-t/2}+\epsilon e^{t/2})
 =t b_\epsilon'(t).
 \tag{2.3}
\]

Although the expression in parentheses has opposite parity, the
factor `t` returns it to sector `epsilon`. For `F` primitive of that
parity, (1.5) becomes

\[
 \boxed{
  \dot\Pi F
  =-b_\epsilon\,{\langle\dot b_\epsilon,F\rangle
                    \over q_\epsilon(T)}.}
 \tag{2.4}
\]

The term containing `dot q_epsilon` does not appear because
`<b_epsilon,F>=0`.

## 3. Exact identity with the Tate virial

Let `r_F=rho b_epsilon`. Using (2.4), the polarization identity of the
inner product, and (2.3), one obtains

\[
 \begin{aligned}
 2\operatorname{Re}\langle\dot\Pi F,r_F\rangle
 &=-2\operatorname{Re}\langle F,\rho\dot b_\epsilon\rangle\\
 &=-2\operatorname{Re}\langle F,t r_F'\rangle.
 \end{aligned}
 \tag{3.1}
\]

This proves (0.1), independently of the convention for which variable
of the inner product is linear, because only the real part is taken.

For a symmetric operator `A` whose Tate port on `F` is `r_F`, the two
connection terms satisfy

\[
 \begin{aligned}
 &\langle F,\dot\Pi A\Pi F\rangle
  +\langle F,\Pi A\dot\Pi F\rangle\\
 &\hspace{25mm}=-2\operatorname{Re}\langle F,t r_F'\rangle.
 \end{aligned}
 \tag{3.2}
\]

This proves the Tate part of the Ward law for the full first-contact
operator.

## 4. Audit of the PC port

Applying (3.2) to `mathfrak P_{N,N}^{ren}` requires identifying its
Tate output. Define the typed defect

\[
 d_{N,T}^{\rm Tate}(F)
 :=R_T\mathfrak P_{N,N}^{\rm ren}F-r_F.
 \tag{4.1}
\]

Then the two connection terms in (8.2) of R170_844 are

\[
 -2\operatorname{Re}\langle F,t r_F'\rangle
 +2\operatorname{Re}\langle\dot\Pi F,
                  d_{N,T}^{\rm Tate}(F)\rangle,
 \tag{4.2}
\]

with the overall sign adjusted to the chosen orientation of
`mathfrak P`. Formula (4.2) is an exact acceptance test:

* if `d_N,T^Tate=0`, the Tate cancellation proposed in R170_844 is a
  theorem;
* if it does not vanish, an explicit rank-one scalar remains that must
  be combined with the polar port of `dot C_N`;
* replacing that scalar with the cross collar without proving the
  equality repeats the type error of R161_063.

Consequently, the next computation to perform before recombining the
hyperbola is to expand `R_T mathfrak P_N,N^ren F` in the basis
`(phi_-,phi_+)`, insert the canonical residues of R161_009, and
compare each coefficient with the first-contact system. There is no
longer a functional unknown: only two coefficients remain, or one
after fixing parity.

## 5. State of the puzzle

```text
exact derivative of the primitive projection                  PROVED
reduction to rank one in each parity                           PROVED
identity dotPi = minus Tate virial for the full operator       PROVED
Tate defect of Ward--PC, equation (4.1)                         DEFINED
vanishing/polar cancellation of that defect                     OPEN
Fourier derivative = archimedean virial                          OPEN
arithmetic Wronskian and synchronized tail                      PROVED (R170_843--844)
full Ward--PC                                                   OPEN
VIR--LB                                                          OPEN
D                                                                OPEN
```

The real progress is that one of the three open Ward--PC ports has
been reduced to a finite scalar identity and its desired contribution
has been computed with the correct sign. The global law is not yet
asserted.
