# 114.a.130 — H7: mixed archimedean boundary detects the anti-lattice

```
+------------------------------------------------------------------------+
| BOUNDARIES  Pull the two literal mixed boundaries back to Y^locreg.      |
| RESTRICT    A_p=L_(p,1)L_(p,2)^(-1) restricts to L_p^(-1) on B_1       |
|             and L_p on B_2, pulled from the arithmetic factor.          |
| DETECTOR    Faithfulness of either mixed-boundary pullback on the prime  |
|             curve Picard lattice implies anti-diagonal faithfulness.    |
| OPEN        Prove that boundary base-change faithfulness theorem.        |
+------------------------------------------------------------------------+
```

## 1. The two literal mixed boundaries

Let `X=overline(Spec Z)` and `S=Spec F{+-1}`.  Haran's real prime is the
coherent family of maximal ideals `eta_N` in the real charts
`A_N=Z[1/N] intersection Z_R`.  Its limit local object is
`Q intersection Z_R`, not all of `Z_R`.  As made explicit in `a_135`, take
the levelwise reduced residue quotients and call the resulting pro-point
`x_infty=Spec kappa_infty`.  Finite limits then give the two mixed
boundaries

\[
 \widetilde B_1=x_\infty\times_S X,\qquad
 \widetilde B_2=X\times_Sx_\infty.                                   \tag{1.1}
\]

The supportwise morphism `i:Y^locreg->Y` is a closed restriction, so these literal
boundaries do not automatically factor through it.  Define the correctly
typed repaired boundaries by inverse image:

\[
 B_i^{\rm locreg}=Y^{\rm locreg}\times_Y\widetilde B_i,\qquad
 j_i:B_i^{\rm locreg}\longrightarrow Y^{\rm locreg}.                  \tag{1.2}
\]

Form these fiber products at compatible pro-levels.  For the supportwise
repair of `a_132`, take the inverse image on every cofinal `(T,N)` tail.
Their existence uses the
levelwise residue-point construction of `a_135`; they are not asserted to
equal the unrepaired `widetilde B_i`, or even to retain all its points.

Write

\[
 \pi_2:B_1^{\rm locreg}\to X,\qquad \pi_1:B_2^{\rm locreg}\to X      \tag{1.3}
\]

for the arithmetic projections.

## 2. Restriction of the prime anti-class

The curve lattice `L_p` is represented idelically by `p^{-1}` at the finite
place `p` and by `1` at every other place, including infinity.  Therefore
its restriction to `x_infty` is the trivial rank-one real unit lattice.

For

\[
 A_p=\mathcal L_{p,1}\otimes\mathcal L_{p,2}^{-1},                    \tag{2.1}
\]

functoriality of pullback gives canonical equivalences

\[
 j_1^*A_p\simeq\pi_2^*L_p^{-1},qquad
 j_2^*A_p\simeq\pi_1^*L_p.                                           \tag{2.2}
\]

For a finite vector `a=(a_p)`, put `L_a=tensor_p L_p^(a_p)`.  Tensoring
(2.2) gives

\[
 j_1^*\delta_{\rm pr}(a)=\pi_2^*L_a^{-1},qquad
 j_2^*\delta_{\rm pr}(a)=\pi_1^*L_a.                                 \tag{2.3}
\]

This is the geometric form of the residual classes `B_p^infty` isolated in
`a128`--`a129`: the finite principal fraction disappears, while the
arithmetic lattice remains on the non-real factor.

## 3. Exact sufficient boundary theorem

Let

\[
 P_{\rm pr}=\bigoplus_p\mathbb Z[L_p]\subset Pic_{\rm cmp}(X).        \tag{3.1}
\]

The curve degree and unique factorization prove that (3.1) is free.

> **H7-MIXED-BDRY-PIC.** At least one of the pullbacks
> \[
> \pi_2^*:P_{\rm pr}\to Pic_{\rm cmp}(B_1^{\rm locreg}),\qquad
> \pi_1^*:P_{\rm pr}\to Pic_{\rm cmp}(B_2^{\rm locreg})              \tag{3.2}
> \]
> is injective.

### Theorem 3.1 (mixed-boundary detector)

H7-MIXED-BDRY-PIC implies that `delta_pr` is injective.  Consequently it
implies H7-ARCH-BDRY on the prime sector and closes the common descent gate
of the RR form, calibrated sections, contact, Green biextension and gauge.

### Proof

If `delta_pr(a)=1`, pullback to both boundaries and apply (2.3).  If, say,
`pi_2^*` is injective, then `L_a=1` in `P_pr`.  Its degree is
`sum_p a_p log p`; unique factorization gives every `a_p=0`.  The other
boundary is symmetric.  QED.

No global unit computation on the whole square and no effective descent
theorem along `X->S` is needed once (3.2) is known.

## 4. What remains to prove

The existence of (1.1)--(1.2) and identities (2.2) are formal base change
and the known real component of `L_p`.  What is not in the audited sources is a
theorem that `pi_i^*` preserves the nonzero prime degree classes.  A proof
could come from any one of:

1. a degree/norm homomorphism on `Pic_cmp(B_i^reg)` extending the curve degree;
2. a retraction or norm functor for `pi_i` on the prime sector;
3. a direct Cech calculation showing that `pi_i^*L_a` is trivial only when
   the real product norm `product_p p^(a_p)` equals one.

`a_136` rules out the base-algebra retraction part of item 2. A Picard norm
or genuine descent theorem is not ruled out and is now H7-RSPH-DESC/NORM.

This is narrower than H7-U3/H7-LD and avoids using the numerical Green form
circularly.  H7-MIXED-BDRY-PIC, two-target Deligne comparison, dynamic
undecorated cycles, row A and RH remain open.

## 5. Verification scope

`114_a_130_h7_mixed_boundary_detector_verify.py` checks the two restriction
identities, tensor laws, the detector implication and source anchors.  It
does not mark the missing injectivity (3.2) as proved.

**Type correction (`a_135`).**  The base object of the real reduced point is
the rational residue object `kappa_infty`, not the full real ball `Z_R` and
not automatically Haran's full sphere object `F_R`.  Accordingly (3.2) is a
conservativity question for base change along
`F{+-1}->kappa_infty`, followed by supportwise reflection.
