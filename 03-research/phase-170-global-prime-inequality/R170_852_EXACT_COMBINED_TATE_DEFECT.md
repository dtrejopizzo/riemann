# R170_852 — Exact Tate defect of the extracted combined port

## 0. Result

R170_851 showed that `dot S_N PAF` and `dot S_N QAF` must not be
projected separately. Here the Tate coordinate of their combination is
computed.

Fix a parity `epsilon` and write

\[
 b_\epsilon(t)=e^{-t/2}+\epsilon e^{t/2},
 \qquad q_\epsilon=\|b_\epsilon\|_{L^2(-T,T)}^2
 =4(\sinh T+\epsilon T).                                    \tag{0.1}
\]

Let

\[
 B=B_{N,T}=(PS_NP)^{-1},
 \qquad h_\epsilon:=B^*b_\epsilon.                           \tag{0.2}
\]

Then

\[
 \boxed{PS_N^*P h_\epsilon=b_\epsilon.}                     \tag{0.3}
\]

For a first-contact vector `F` of parity `epsilon`, set

\[
 PA_MF=r_F=\rho_Fb_\epsilon,
 \qquad QA_MF=\ell_F.                                       \tag{0.4}
\]

The parity-`epsilon` coordinate of the combined port of R170_851 is

\[
\boxed{
\begin{aligned}
 \omega_{N,T}^{\rm comb}(F)
 ={1\over q_\epsilon}\{&
 \rho_F\langle P\dot S_N^*Ph_\epsilon,b_\epsilon\rangle\\
 &+\langle Q\dot S_N^*Ph_\epsilon,\ell_F\rangle\\
 &-\langle QS_N^*Ph_\epsilon,Q\dot A_MF\rangle\}.
\end{aligned}}                                               \tag{0.5}
\]

Hence the defect relative to Tate forcing is

\[
\boxed{
 \Delta_{N,T}^{\rm Tate}(F)
 =(\kappa_{N,T}^\epsilon-1)\rho_F
   +\mathcal E_{N,T}^{\rm ext,1}(F)
   -\mathcal E_{N,T}^{\rm ext,2}(F),}                         \tag{0.6}
\]

where all terms are defined explicitly in §2. This is the typed
version of the defect that R170_845 tried to formulate using the
nonexistent operator `mathfrak P`.

## 1. Derivation without separating atoms

The combined port is

\[
 \mathcal P_{N,T}^{\rm comb}(F)
 =BP\dot S_NA_MF-BPS_NQ\dot A_MF.                            \tag{1.1}
\]

Its parity-`epsilon` Tate coordinate is

\[
 \omega_{N,T}^{\rm comb}(F)
 ={\langle b_\epsilon,\mathcal P_{N,T}^{\rm comb}(F)\rangle
    \over q_\epsilon}.                                      \tag{1.2}
\]

Use `h_epsilon=B^*b_epsilon` and move adjoints **before** inserting
`I=P+Q`:

\[
\begin{aligned}
 q_\epsilon\omega^{\rm comb}
 ={}&\langle\dot S_N^*Ph_\epsilon,A_MF\rangle
 -\langle S_N^*Ph_\epsilon,Q\dot A_MF\rangle.               \tag{1.3}
\end{aligned}
\]

Only now insert (0.4). In the second term, the interior component of
`S_N^*Ph_epsilon` is `b_epsilon` by (0.3), and is orthogonal to
`Q dot A_MF`. This leaves

\[
\begin{aligned}
 q_\epsilon\omega^{\rm comb}
 ={}&\rho_F\langle P\dot S_N^*Ph_\epsilon,b_\epsilon\rangle\\
 &+\langle Q\dot S_N^*Ph_\epsilon,\ell_F\rangle\\
 &-\langle QS_N^*Ph_\epsilon,Q\dot A_MF\rangle,
\end{aligned}
 \tag{1.4}
\]

which proves (0.5). The atoms of R170_851 have already cancelled
inside (1.3); (1.4) is interpreted by duality in the common core.

## 2. The three coefficients of the defect

Define the geometric scalar, independent of `F`,

\[
 \boxed{
 \kappa_{N,T}^\epsilon
 :={\langle P\dot S_N^*Ph_\epsilon,b_\epsilon\rangle
       \over q_\epsilon}.}                                  \tag{2.1}
\]

And the two exterior residues

\[
\begin{aligned}
 \mathcal E_{N,T}^{\rm ext,1}(F)
 &:={\langle Q\dot S_N^*Ph_\epsilon,\ell_F\rangle
       \over q_\epsilon},\\
 \mathcal E_{N,T}^{\rm ext,2}(F)
 &:={\langle QS_N^*Ph_\epsilon,Q\dot A_MF\rangle
       \over q_\epsilon}.
\end{aligned}                                                \tag{2.2}

Then (0.6) is just (0.5) minus `rho_F`. It has not been assumed that
`kappa=1` nor that the exterior residues vanish.

All objects in (2.1)--(2.2) are finite on the window: `B=PMP` by
R170_850, and only `n<e^(2T)` can contribute after compression. Thus
the formula is uniform as a law, even though the number of active
terms grows with `T`.

## 3. Comparison with the moving connection

R170_845 proves

\[
 2\operatorname{Re}\langle\dot\Pi_TF,r_F\rangle
 =-2\operatorname{Re}\langle F,t r_F'\rangle.                \tag{3.1}
\]

If the Tate port of the curvature were exactly `r_F`, the two
connection terms would cancel the Tate virial. The correct formula is
now

\[
\begin{aligned}
 2\operatorname{Re}
 \langle\dot\Pi_TF,
   \omega_{N,T}^{\rm comb}(F)b_\epsilon\rangle
 ={}&-2\operatorname{Re}\langle F,t r_F'\rangle\\
 &+\mathfrak R_{N,T}^{\rm Tate}(F),                           \tag{3.2}
\end{aligned}
\]

where

\[
 \mathfrak R_{N,T}^{\rm Tate}(F)
 :=2\operatorname{Re}\langle\dot\Pi_TF,
       \Delta_{N,T}^{\rm Tate}(F)b_\epsilon\rangle.          \tag{3.3}
\]

Full Tate cancellation amounts to showing that (3.3) cancels against
the derived polar port and the support concomitant of the same PC
balance. It is no longer equivalent to asserting without proof that a
static output is `r_F`.

## 4. Falsification tests

The formula allows three mandatory checks:

1. **No nontrivial comb.** For `N=1`, `S_1=I`, `dot S_1=0`,
   `B=I`; then `kappa=0` and the residues of (2.2) reduce to the
   second port. There is no automatic Tate cancellation. This
   prevents (0.6) from being a purely projective identity.
2. **Change of prime coefficients.** `kappa` depends only on the
   integer comb, while `ell_F` and `Q dot A_MF` depend on the
   arithmetic operator. Hence a valid cancellation must use the
   exterior residues, the line along which it can fail for DH or
   `a_kappa`.
3. **No exterior.** Deleting `Q` leaves `(kappa-1)rho_F`, which is
   not known to vanish. So a proof that compresses before
   differentiating cannot close the Tate term.

## 5. Status

```text
causal dual h_epsilon and equation P S* P h=b                PROVED
Tate coordinate of the combined port, equation (0.5)          PROVED
full scalar defect, equation (0.6)                             PROVED
compatibility with boundary atoms                              PROVED
connection residue R_Tate                                       DEFINED
cancellation with polar + support                               OPEN
VIR--LB / D                                                     OPEN
```
