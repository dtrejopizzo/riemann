# R170_848 — PC curvature with right Fourier removed: joint appearance of the archimedean virial and the Wronskian

## 0. Result

The two-scale PC identity of R170_847 contains `mathscr F_r` on its
left-hand side. Differentiating it directly introduces an extra jet of
`mathscr F_r`. There is an exact elimination: multiply the whole
identity by `mathscr F_r` on the right before differentiating.

Since `mathscr F_r^2=I`, the left-hand side becomes

\[
 S_N(q)A_M(r).
\]

Its antidiagonal derivative is

\[
 \boxed{
 \partial_-[S_N(q)A_M(r)]_{1,1}
 =S_N\dot A_M-\dot S_NA_M.}
 \tag{0.1}
\]

This expression simultaneously contains:

* `dot mathcal M`, whose symbol is `-tau m'(tau)`;
* minus the causal Wronskian
  `dot L_M S_N-L_M dot S_N`;
* the adjoint orientation;
* the mixed term `dot S_N mathcal M`, which must cancel from the
  Poisson side of PC and cannot be discarded.

This yields a real finite carrier of the archimedean jet and the
arithmetic sign of R170_843 in the same identity.

## 1. PC identity with no right Fourier

Start from R170_847 Theorem 4.1 and multiply by `mathscr F_r`:

\[
\begin{aligned}
 S_N(q)A_M(r)
 ={}&\{X_r,E_N(r,q)\}\mathscr F_r
  -L_M(r)^*E_N(r,q)\mathscr F_r\\
 &-JH_{M,N}(r,q)\mathscr F_r-H_{M,N}(r,q).
\end{aligned}
 \tag{1.1}
\]

This is an exact identity in the core for all `r,q>0`.
Consequently, its `partial_-` derivative is also exact. Neither first
contact nor a limit has been used.

## 2. Expansion of the left-hand side

Since

\[
 A_M(r)=\mathcal M_r-L_M(r)-L_M(r)^*,
\]

(0.1) gives

\[
\begin{aligned}
 S_N\dot A_M-\dot S_NA_M
={}&S_N\dot{\mathcal M}-\dot S_N\mathcal M\\
 &-\bigl(S_N\dot L_M-\dot S_NL_M\bigr)\\
 &-\bigl(S_N\dot L_M^*-\dot S_NL_M^*\bigr).
\end{aligned}
 \tag{2.1}
\]

The causal sums `S_N,L_M` commute. Hence

\[
 S_N\dot L_M-\dot S_NL_M
 =\dot L_MS_N-L_M\dot S_N
 =\mathcal A_{M,N}^{\rm raw}.
 \tag{2.2}
\]

The second line of (2.1) is exactly
`-mathcal A_raw`, with the sign required to turn the negative energy
of R170_843 into a positive contribution on the opposite side of the
balance.

The orientation with `L_M^*` is not identified with (2.2): it must be
preserved until reflection, parity and compression are applied.
Replacing it beforehand by the adjoint of (2.2) would lose the support
collars flagged in R161_057--065.

## 3. The archimedean jet is literal

For the dilation

\[
 U_rf(t)=r^{-1/2}f(t/r),
\]

the conjugated multiplier `mathcal M_r=U_r^{-1}mathcal MU_r` has
symbol

\[
 m_r(\tau)=m(\tau/r).
\]

Hence

\[
 \boxed{\dot m(\tau)=-\tau m'(\tau).}                         \tag{3.1}
\]

In particular, for every `F` in the corresponding form domain,

\[
 \boxed{
 \langle F,\dot{\mathcal M}F\rangle
 =-{1\over2\pi}\int_{\mathbb R}
       \tau m'(\tau)|\widehat F(\tau)|^2\,d\tau.}
 \tag{3.2}
\]

This is exactly the negative of the archimedean term of
`mathcal V_{Lambda,T}`. It is not obtained by analogy nor inserted as
a later correction.

## 4. Relation with the prime virial

The same conjugation gives

\[
 \dot L_M
 =-\sum_{n\le M}{\Lambda(n)\log n\over\sqrt n}
       \partial_t\tau_{\log n}.
 \tag{4.1}
\]

On the diagonal of the compressed Weil form, (4.1) and its adjoint
produce

\[
 \sum_{n<e^{2T}}{2\Lambda(n)\over\sqrt n}
       \log n\,c_F'(\log n),                                 \tag{4.2}
\]

with the convention of R170_841. Together with (3.2), the interior
derivative of `A_M(r)` is the negative of the first two lines of the
virial. The third line, Tate, is the moving connection computed in
R170_845.

Hence, at the level of the Weil operator alone, one has the form
balance

\[
 \left.{d\over dr}\right|_{1}
 \langle F,\Pi_{rT}A_M(r)\Pi_{rT}F\rangle
 =-\mathcal V_{\Lambda,T}(F),                                \tag{4.3}
\]

under the regularity hypothesis used in R162_407/R170_841 and for
`M>=e^(2T)`. Formula (4.3) is the known virial identity; (1.1)--(2.2)
now inserts it into PC before the hyperbola is recombined.

## 5. Extraction gate and remaining residues

Equation (2.1) contains `S_N dot A_M`, not isolated `dot A_M`. Hence
(4.3) identifies the virial that must emerge, but **does not
authorize** replacing

\[
 \langle F,G_\delta S_N\dot A_MF\rangle
 \quad\hbox{by}\quad
 \langle F,\dot A_MF\rangle.                                 \tag{5.1}
\]

Doing so would require inverting or omitting `S_N` and would be
precisely a version of the residue extraction warned against in Paper
47. The Wronskian block, on the other hand, is observed with sign
because R170_843 proves directly that

\[
 -\operatorname{Re}\langle F,
       G_\delta\mathcal A_{N,N}^{\rm raw}F\rangle
 =+\mathscr E_{N;T,\delta}^{\beta}(F).                         \tag{5.2}
\]

The new, precise gate is to show, from the right-hand side of (1.1),
without inverting `S_N`, that the block `S_N dot A_M` minus its ports
reduces to the scalar (4.3). For this, the following must be
preserved and grouped literally:

1. `-dot S_N mathcal M`;
2. the `L_N^*` orientation of (2.1);
3. `partial_-K_N(r,q)=2K_N+K_N^(2,partial)`;
4. the synchronized tail of `dot H_N,N`;
5. the continuum `C_N` when replacing `S_N` by `Z_N`;
6. the two support concomitants;
7. the Tate coordinate of the PC output.

The differentiated identity of the right-hand side of (1.1) determines
all of these terms. The next step is to group them without using
adjunction through `P_T` and check whether they extract (4.3),
together with the non-negative synchronized energy and the polar
residue that cancels `dot Pi_T`. This is the extraction gate; it
remains open.

## 6. Status

```text
two-scale PC with no right Fourier                             PROVED
curvature S dotA-dotS A                                        PROVED
appearance of -A_raw with correct orientation                    PROVED
dot M = multiplier -tau m'                                       PROVED
identification of the interior jet of A with arch+prime          PROVED
moving connection with Tate                                      INHERITED from R170_845
extraction of dot A from S_N dot A without inverting S_N           OPEN
exact grouping of the seven residues of §5                        OPEN
PC--curvature / VIR--LB / D                                        OPEN
```
