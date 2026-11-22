# R170_886 — Euler--Maclaurin anchor and the exact range law

> **Audit R170_887.** The fusion identities and the range criterion
> are correct for the frozen jet. The criterion
> `omega_EM in Ran H_T` is, however, the Fredholm criterion for the
> sought vanishing and not a strict reduction relative to RES--WARD.
> It also does not represent the derivative of the minimal branch: there,
> `P_T`, the primitive projection, `h`, and `F` all move. R170_887 adds that connection and corrects
> the scope of the comparison with minimality.

## 0. Result

The identity of R170_885 can be written with a single physical anchor. Let

\[
 e_{\rm EM}:=q_N-C_N^*h,
 \qquad q_N=QS_N^*h.                                      \tag{0.1}
\]

Then, on the common core,

\[
\boxed{
 \mathfrak W_{\rm ext}+(h,P\mathcal P_{C,A_M}F)
 =W(e_{\rm EM},A_MF).}                                   \tag{0.2}
\]

Hence the vanishing of the exterior residue on the whole first-contact
radical is equivalent to a range equation for an explicit vector:

\[
\boxed{
 \omega_{\rm EM}:=\Pi_{\mathcal P_T}
   \bigl(A_M^*\dot e_{\rm EM}-\dot A_M^*e_{\rm EM}\bigr)
 \in\overline{\operatorname{Ran}H_T}.}                   \tag{0.3}
\]

When zero is an isolated eigenvalue of `H_T`, the range is closed and the
closure may be dropped. This is an exact reformulation as a Poisson
equation `H_Tg=omega_EM`; it does not by itself constitute a proof nor
a reduction independent of the Fredholm criterion.

## 1. Fusion of the two Wronskians

R170_885 gives

\[
 W(QZ_N^*h,\ell)-W(PC_N^*h,r),                            \tag{1.1}
\]

where `ell=QA_MF`, `r=PA_MF`, and `Z_N=S_N-C_N`. Since `P,Q`
are fixed in the frozen derivation,

\[
 QZ_N^*h=Qq_N-QC_N^*h=q_N-QC_N^*h.                       \tag{1.2}
\]

Moreover,

\[
 Pe_{\rm EM}=-PC_N^*h,\qquad
 Qe_{\rm EM}=q_N-QC_N^*h.                                \tag{1.3}
\]

Orthogonality of `P,Q`, also for the frozen velocities,
implies

\[
 W(e_{\rm EM},A_MF)
 =W(QZ_N^*h,\ell)+W(-PC_N^*h,r),                          \tag{1.4}
\]

which proves (0.2). No projection is moved across `S_N`,
`C_N`, or `A_M`.

## 2. Riesz representative

Let `Pi_(mathcal P_T)` be the projection onto the fixed primitive space on
which `H_T` acts. For `F` primitive in the core of the four operators,

\[
\begin{aligned}
 W(e_{\rm EM},A_MF)
 &=(\dot e_{\rm EM},A_MF)
   -(e_{\rm EM},\dot A_MF)\\
 &=(\Pi_{\mathcal P_T}
     [A_M^*\dot e_{\rm EM}-\dot A_M^*e_{\rm EM}],F)\\
 &=(\omega_{\rm EM},F).                                  \tag{2.1}
\end{aligned}
\]

On the form domain, (2.1) defines `omega_EM` as a functional on the
dual; the range statement is then interpreted via the form
operator. No operator regularity not already proved in Paper 46 is assumed.

The disintegration of R170_885 makes `omega_EM` fully arithmetic:
`dot e_EM` contains simultaneously

\[
 L_M^*b+R_M^*b+\mathcal E_{N,T}b
 -\mathcal L^{\rm cont}_{N,T}b,                           \tag{2.2}
\]

while `e_EM` keeps the discrete--continuous mass defect. Thus
equation (0.3) uses the exact integers, `U_N`, `R_M`, and the polar term.

There is also a non-disintegrated operator formula. With `h` frozen,

\[
 e_{\rm EM}=(QS_N^*-C_N^*)h,
 \qquad
 \dot e_{\rm EM}=(Q\dot S_N^*-\dot C_N^*)h.              \tag{2.3}
\]

If `A_M` and `dot A_M` are symmetric on the real core, then

\[
\boxed{
 \omega_{\rm EM}=\Pi_{\mathcal P_T}
 \left[
   (\dot S_NQA_M-S_NQ\dot A_M)
  -(\dot C_NA_M-C_N\dot A_M)
 \right]^*h.}                                            \tag{2.4}
\]

The first bracket is the discrete exterior curvature and the second its
continuous counterpart. The intermediate `Q` of the first cannot be erased:
it contains precisely the routes that leave the window before returning.

## 3. Equivalence with the exterior law

Let `mathsf Z_T` be the orthogonal projection onto `ker H_T`. For every vector
`omega` of the Hilbert space,

\[
 (\omega,F)=0\quad(F\in\ker H_T)
 \Longleftrightarrow
 \mathsf Z_T\omega=0
 \Longleftrightarrow
 \omega\in(\ker H_T)^\perp
 =\overline{\operatorname{Ran}H_T}.                       \tag{3.1}
\]

Applied to (2.1), this identity proves the equivalence between the
vanishing of (0.2) on the whole radical and (0.3). If zero is isolated,

\[
 \boxed{H_Tg_{\rm EM}=\omega_{\rm EM}}                    \tag{3.2}
\]

for some `g_EM` is an equivalent and verifiable formulation of the
exterior law.

For a single extremal vector `F_c`, the scalar condition
`(omega_EM,F_c)=0` suffices; (0.3) is the uniform version that does not depend on choosing
an orientation of the radical.

Formally taking `g_EM=H_T^dagger omega_EM` would be circular: the
pseudo-inverse solves (3.2) only when orthogonality to the radical
already holds. An explicit construction not using that orthogonality would
indeed be a new law.

## 4. What minimality does and does not provide

Under REG/C1, minimality gives

\[
 \mathsf Z_T\dot H_T\mathsf Z_T\preceq0.                 \tag{4.1}
\]

This information is quadratic and even. By contrast
`F mapsto (omega_EM,F)` is linear and odd. Hence (4.1) does not imply
(0.3). The boundary-augmented model of R170_870 allows that
linear class to be varied arbitrarily without changing (4.1).

The only path compatible with minimality is to construct, using the exact
arithmetic identity, a solution of (3.2), or a positive extension in
which `e_EM` produces a second null vector and (2.1) is its mixed block.
R170_862 shows that a positive-energy anchor is not enough.

## 5. New arithmetic obligation

The equation to be built is now fixed unambiguously:

\[
\boxed{
 H_Tg_{\rm EM}
 =\Pi_{\mathcal P_T}\left[
   A_M^*\dot{(q_N-C_N^*h)}
  -\dot A_M^*(q_N-C_N^*h)\right].}                       \tag{5.1}
\]

It must be proved on the form domain, uniformly in `T`, with the finite
cutoffs and their tails. An identity that only manipulates `Lambda*1=log` before
applying `A_M^*` is not enough: it must show that the full representative
falls in the physical range of `H_T`.

By (2.4), a sufficient and already fully typed factorization would be

\[
 \Pi_{\mathcal P_T}
 \left[
   (\dot S_NQA_M-S_NQ\dot A_M)
  -(\dot C_NA_M-C_N\dot A_M)
 \right]^*h
 =H_T\mathcal G_{N,M,T}h,                                \tag{5.2}
\]

for an operator `G_(N,M,T)` built before recombining the routes.
This is the concrete operator version of the missing arithmetic law.

## 6. Status

```text
fusion of the exterior and polar terms into one anchor      PROVED
representative omega_EM                                     PROVED ON THE CORE
exterior law <=> radical projection of omega_EM vanishes     PROVED
exterior law <=> range equation H_T g=omega_EM               PROVED IF 0 IS ISOLATED
range equation as a strictly new reduction                   NO: FREDHOLM CRITERION
quadratic minimality implies the range equation               REFUTED IN GENERAL
arithmetic construction of g_EM                                OPEN
VIR--LB / D                                                     OPEN
```
