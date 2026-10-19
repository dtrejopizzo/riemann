# R170_846 — Audit of the Ward–PC carrier and transversal corpus filter

> **Successor audit (R170_847).** Carrier (1.1) is well defined, but it
> is not new: on compressing and expanding it reproduces the class of
> anticommutators and Hermitian powers of R161_062--064. Moreover it
> hermitianizes after the hyperbola's legs have been recombined.
> R170_843 §0(3)--(4) shows that this operation does not by itself
> preserve the Wronskian orientation. (4.1)--(4.3) are withdrawn as the
> preferred route. R170_847 first builds the antidiagonal derivative of
> the two legs and only afterward takes the Hermitian part.

## 0. Verdict

The covariant derivative proposed in R170_844 was not yet well
defined. The symbol

\[
 \mathfrak P_{N,N}^{\rm ren}
\]

does not appear defined before equation R170_844 (0.7). The finite PC
identity of Paper 47 is

\[
 Y_{M,N}:=S_NA_M\mathscr F
 =\{X,E_N\}-L_M^*E_N-JH_{M,N}-H_{M,N}\mathscr F=:Z_{M,N}.
 \tag{0.1}
\]

It is an equality `Y=Z`, not a distinguished symmetric operator. There
are three possible interpretations, and none of them directly
authorizes R170_844 (8.2):

1. `mathfrak P=Y-Z`: it is the zero operator in the core; its
   covariant derivative is `0=0`.
2. `mathfrak P=Y` or `Z`: it is an oriented operator, but in general
   not symmetric; the two `dot Pi` terms are not conjugate.
3. a hermitianization of `Y`: it is well typed, but it is a new choice
   whose derivative and falsifiers must be audited.

Hence R170_845 (1.4)--(3.2) remains a correct lemma for the moving
Tate connection, but its §4 was conditional on the existence of a
symmetric carrier with the declared port. It has not been proved that
PC provides that carrier.

## 1. Minimal well-typed carrier

The minimal canonical choice that preserves both orientations is

\[
 \boxed{
  \mathcal W_{M,N}^{\rm ren}
  :={1\over2}\left(
    S_N^{\rm ren}A_M\mathscr F
    +\mathscr F A_M(S_N^{\rm ren})^*
  \right).}
 \tag{1.1}
\]

In the core, `A_M` and `mathscr F` are symmetric, though they do not
commute, and (1.1) is the Hermitian part of the left-hand PC side.
Thus

\[
 (\mathcal W_{M,N}^{\rm ren})^*=\mathcal W_{M,N}^{\rm ren}.
 \tag{1.2}
\]

This definition does not assert a sign. It preserves orientation
because it is linear in `A_M`; it is not the sign-blind square
excluded by R161_002. Nor is a linear limit taken: all
differentiation must be done at finite cutoffs.

The legitimate covariant object is now

\[
 \nabla^{\rm WPC}_{T;M,N}
 =\left.{d\over dr}\right|_{r=1}
  \left(\Pi_{rT}\mathcal W_{M,N}^{\rm ren}(r)\Pi_{rT}\right).
 \tag{1.3}
\]

Its diagonal on a primitive vector `F` is

\[
 \begin{aligned}
 \langle F,\nabla^{\rm WPC}F\rangle
 ={}&2\operatorname{Re}
       \langle\dot\Pi_TF,\mathcal W_{M,N}^{\rm ren}F\rangle\\
 &+\langle F,\dot{\mathcal W}_{M,N}^{\rm ren}F\rangle.
 \end{aligned}
 \tag{1.4}
\]

R170_845 computes exactly the first line once the Tate port of
`mathcal W F` is known.

## 2. The port that must actually be computed

Define

\[
 w_{M,N,T}(F):=R_T\mathcal W_{M,N}^{\rm ren}F.
 \tag{2.1}
\]

For `F` of parity `epsilon`, write the Tate decomposition

\[
 w_{M,N,T}(F)=\omega_{M,N,T}^{\epsilon}(F)b_\epsilon
              +\omega_{M,N,T}^{-\epsilon}(F)b_{-\epsilon},
 \qquad r_F=\rho_Fb_\epsilon.
 \tag{2.2}
\]

Then R170_845 gives, without any informal identification,

\[
 2\operatorname{Re}
  \langle\dot\Pi_TF,\mathcal W_{M,N}^{\rm ren}F\rangle
 =-2\operatorname{Re}
  \left(\omega_{M,N,T}^{\epsilon}(F)
    \langle F,tb_\epsilon'\rangle\right).
 \tag{2.3}
\]

The opposite-parity component is orthogonal to `dot Pi_T F` and does
not enter (2.3). The desired Tate virial is the same expression with
`omega^epsilon=rho`. Hence the correct defect is the scalar

\[
 \boxed{\Delta_{M,N,T}^{\rm Tate}(F)
 :=\omega_{M,N,T}^{\epsilon}(F)-\rho_F.}
 \tag{2.4}
\]

This replaces the undefined operatorial defect of R170_845 (4.1). It
can be computed directly via

\[
 \omega_{M,N,T}^{\epsilon}(F)
 ={\langle\mathcal W_{M,N}^{\rm ren}F,b_\epsilon\rangle
    \over\|b_\epsilon\|^2},
 \qquad
 \|b_\epsilon\|^2=4(\sinh T+\epsilon T).
 \tag{2.5}
\]

There is no longer gauge freedom nor a functional unknown.

## 3. Corpus filter: results that must be incorporated

The transversal search across phases 121, 124, 161--166, 170 and
Paper 47 fixes the following requirements.

1. **R161_009:** the polar Hardy residues are the cross Tate collars.
   They serve to evaluate (2.5), but the cross Gram is not the
   orthogonal projection.
2. **R161_018 and R161_023:** every linear limit of PC and the direct
   conjugate test recombine into a tautology. (1.3) must remain
   finite, differentiated and polarized before the limit.
3. **R161_043 and R161_063:** the Tate port of a compressed output
   cannot be replaced by the cross collar. Parity kills the port `X F`
   in the ordering studied there, not the port (2.1).
4. **R161_028:** `partial_a C_a=e^{a/2}tau_a`; the polar velocity and
   the integer births must be preserved together. Removing `C_N`
   before differentiating loses exactly the sought coupling.
5. **R162_305:** a linear variation of PC coefficients is an algebraic
   zero, even with exterior, polar and Tate content. The parameter of
   (1.3) must be the joint window/Fourier/cutoff dilation, not an
   exterior perturbation of `Lambda`.
6. **R162_590:** PC squares, linear limits, twist-covariant arguments
   and the use of `Lambda*1=log` after regularizing are excluded.
   Divisor cancellation must occur inside `dot W`, before
   recombination.
7. **R163_150--151:** independently varying `M/N` creates a
   sign-changing corner anomaly. A synchronized path must be imposed
   and its jumps justified; the ratio must not be chosen depending on
   `F`.
8. **R170_841--844:** the Wronskian of the two legs and the
   synchronized tail have a sign before recombining. Those are the
   positive blocks that the second line of (1.4) must recover.

## 4. What remains to be proved for this carrier

The computation now splits into falsifiable statements:

### WPC--Tate

Compute (2.5) from both sides of PC-ren and prove one of these two
alternatives:

\[
 \Delta_{M,N,T}^{\rm Tate}(F)=0,                               \tag{4.1}
\]

or

\[
 2\operatorname{Re}\left(
  \Delta_{M,N,T}^{\rm Tate}(F)
  \langle F,tb_\epsilon'\rangle\right)
 +\mathcal P_{M,N,T}^{\rm pol}(F)=0.                           \tag{4.2}
\]

### WPC--bulk

Prove, with the synchronized path and its jumps, that

\[
 \langle F,\dot{\mathcal W}_{N,N}^{\rm ren}F\rangle
 =-\mathcal V_{\Lambda,T}^{\rm arch+prime}(F)
  -\mathscr E_{N,T}^{\beta}(F)
  -\mathscr E_{N,T}^{\rm tail}(F)
  +\mathcal P_{N,T}^{\rm pol}(F).                              \tag{4.3}
\]

Neither (4.1)--(4.3) is proved. Unlike the formulation with
`mathfrak P`, all its objects are now defined and each residue has an
explicit scalar test.

## 5. Status

```text
abstract formula for dot Pi and Tate virial (R170_845)      PROVED
application to undefined mathfrak P                          WITHDRAWN
finite Hermitian carrier W_M,N^ren                           DEFINED
scalar Tate defect Delta_M,N,T                               DEFINED
audit against corpus no-gos                                  COMPLETED
WPC--Tate (4.1) or polar cancellation (4.2)                   OPEN
WPC--bulk (4.3)                                               OPEN
Ward--PC / VIR--LB / D                                        OPEN
```

The next computation allowed by the corpus is (2.5) with the finite
formula for `S_N-C_N`, without passing to the limit and without
substituting the cross collar for a projection.
