# R170_875 — Static Tate port: type repair and falsifier

## 0. Verdict

The provisional defect `R_T mathfrak P F-r_F` of R170_845 is not a
well-typed PC port. R170_837 defines

\[
 \mathfrak P_{M,N}^{\rm ren}=Z_NA_M\mathscr F,             \tag{0.1}
\]

so that its application to `F` contains `A_M mathscr F F`, while the
first-contact equation knows `P A_M F=r_F`. The oriented repair is

\[
 \widehat{\mathfrak P}^{\rm ren}
 :=\mathfrak P^{\rm ren}\mathscr F=Z_NA_M.                 \tag{0.2}
\]

Even repaired, its Tate port is not `r_F`. The literal formula of
R161_006 gives a finite, generally nonzero defect.

## 1. Exact formula

Let `P=P_T`, `R=P-Pi`, `Q=I-P`, and write

\[
 A_MF=r_F+\ell_F,\qquad r_F=PA_MF,\qquad \ell_F=QA_MF.
\]

Then

\[
\boxed{
 RZ_NA_MF-r_F
 =(RPZ_Nr_F-r_F)+R\Delta^R_{N,T}\ell_F
   -\phi_-a_-(\ell_F).}                                   \tag{1.1}
\]

The reflected orientation is

\[
 (RPJZ_NJr_F-r_F)+R\Delta^L_{N,T}\ell_F
 -\phi_+a_+(\ell_F).                                      \tag{1.2}
\]

It is not legitimate to replace (1.1) with the crossed collar: the latter has type
`RPZ_N^*g_N` by R161_064(1.1), while (1.1) contains `RZ_NA_MF`.
R161_063 §3 already rejected that identification.

## 2. Finite coefficients and falsifier

Set

\[
 \Phi=(\phi_-,\phi_+),\qquad
 G=\Phi^*\Phi=2\begin{pmatrix}\sinh T&T\\T&\sinh T\end{pmatrix}.
\]

For `N>=e^(2T)`, `r=alpha phi_-+beta phi_+`, let

\[
 A_+=2T\alpha+2\sinh(T)\beta.
\]

The coordinates of `PZ_Nr` are

\[
\begin{aligned}
 v_-^r={}&\sum_{1\le n<e^{2T}}
 \left[\alpha\left({e^T\over n}-e^{-T}\right)
       +\beta(2T-\log n)\right]-2\sinh(T)A_+,\\
 v_+^r={}&\sum_{1\le n<e^{2T}}
 \left[\alpha{2T-\log n\over n}
       +\beta\left({e^T\over n}-e^{-T}\right)\right]-2TA_+.
                                                               \tag{2.1}
\end{aligned}
\]

The exterior part adds

\[
 v^\ell=\binom{
 \langle\phi_-,\Delta^R\ell\rangle-2\sinh(T)a_-(\ell)}{
 \langle\phi_+,\Delta^R\ell\rangle-2Ta_-(\ell)},          \tag{2.2}
\]

and (1.1) holds as

\[
 \Phi\left[G^{-1}(v^r+v^\ell)-{\alpha\choose\beta}\right].\tag{2.3}
\]

For `T=(log 5)/2`, `ell=0` and `r=b_+`, the coordinates of `RZ_Nr` are
approximately

\[
 (0.95543,-1.03070)\ne(1,1).                              \tag{2.4}
\]

Thus the static equality is refuted already at the first threshold.

## 3. Remaining legitimate object

The factor swap of R170_871 does not yet have a Tate component; R170_872
leaves its extension open. The typed object is the combined port of
R170_852. With

\[
 h=(PS^*P)^{-1}b,\quad q=QS^*Ph,\quad z=QAF-\rho q,
\]

one has, in the real sector,

\[
 g\Delta^{\rm Tate}
 =\rho(\kappa-1)g+\big((\dot q,z)-(q,\dot z)\big).          \tag{3.1}
\]

For PC-ren the full polar port must also be preserved:

\[
 P\dot AF=BP(Z\dot A-\dot ZA)F
  +BP\mathcal P_{C,A}F+\mathcal P^{\rm comb}(F).            \tag{3.2}
\]

The correct target is to jointly orient the Wronskian of (3.1) and
`mathcal P_C,A`; the static port cannot replace that computation.

## 4. Status

```text
original operator defect of R170_845                       MISTYPED
oriented repair Z_N A_M                                    PROVED
finite formula for the repaired port                        PROVED
static equality R Z_N A_M F = r_F                           REFUTED
combined derived port + polar                                OBJECT STILL VALID
sign law for its Wronskian                                   OPEN
VIR--LB / D                                                  OPEN
```
