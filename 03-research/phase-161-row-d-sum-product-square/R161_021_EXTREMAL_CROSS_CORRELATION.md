# R161_021 — The terminal scattering gate is one extremal cross-correlation

## 0. Verdict

The compressed scattering target of `R161_020` can be weakened once more. Let `C=C_log` be the selfadjoint unitary
logarithmic cosine transform, let `P=P_[T,infinity)`, and let the canonical product port satisfy `Pg=g`. For
`sigma in {+1,-1}` it is enough to prove the single scalar identity

```
Re <g, PCg-sigma g>=0.                                           (0.1)
```

Indeed, (0.1) is equality in the extremal Rayleigh bound for the involution `C`, and therefore forces

```
Cg=sigma g.                                                      (0.2)
```

Thus the finite Poisson--Chebyshev construction does not have to converge to a vector-valued scattering law. It
only has to annihilate one oriented cross-correlation on a first-contact radical. This is the smallest quadratic
target which still retains the sign lost by `||S_N A_M F||^2`.

## 1. Extremal-correlation lemma

**Lemma 1.1 (PROVED).** Let `C=C*=C^(-1)` on a Hilbert space, let `P` be an orthogonal projection, and suppose
`Pg=g`. For `sigma in {+1,-1}` put

```
e=PCg-sigma g.                                                   (1.1)
```

Then

```
Re <g,e>=<g,Cg>-sigma||g||^2,                                  (1.2)
||g-sigma Cg||^2=-2sigma Re<g,e>.                               (1.3)
```

In particular,

```
Re<g,e>=0  if and only if  Cg=sigma g.                           (1.4)
```

*Proof.* Since `Pg=g`, `<g,PCg>=<g,Cg>`. The latter is real because `C` is selfadjoint, proving (1.2). Also

```
||g-sigma Cg||^2
 =2||g||^2-2sigma<g,Cg>
 =-2sigma Re<g,e>,
```

which proves (1.3)--(1.4). No support assertion about `Cg` is used. ∎

This contains the leakage argument of `R161_020`: once (0.1) holds, both the compressed amplitude error and the
left leakage vanish at the same time.

## 2. Sign in the parity convention

For a parity source `RF=epsilon F`, the required product-port relation is

```
(I+epsilon C)g=0,                                                (2.1)
```

so `sigma=-epsilon`. Define the scalar cross defect

```
X_T(F):=||g||^2+epsilon<g,Cg>.                                  (2.2)
```

Because `C` is a selfadjoint involution,

```
X_T(F)=(1/2)||(I+epsilon C)g||^2 >=0.                            (2.3)
```

Consequently

```
X_T(F)=0  if and only if  Cg=-epsilon g.                         (2.4)
```

Unlike the raw phase-161 square, (2.2) is oriented: replacing the target sign changes the cross term. Unlike a
general norm estimate, its zero set is exactly the desired scattering eigenspace.

## 3. Exact Hardy/Mellin form

Let `G_+^0` be the boundary transform of the corrected right-supported port `g`. With the conventions of
`R161_017`, parity gives `R g_-^0=epsilon g`, and the compressed two-port error has boundary transform

```
E_T^sc=G_+^0+H_T^+[chi G_-^0]
      =H_T^+[zeta W_epsilon^0].                                 (3.1)
```

Since `G_+^0` belongs to the right Hardy space, orthogonality of the Hardy projections gives the exact identity

```
X_T(F)
 =Re <G_+^0,E_T^sc>
 =Re <G_+^0,zeta W_epsilon^0>_(critical line),                   (3.2)
```

with the same Plancherel normalization on all three terms.

Indeed, the first equality is the transform of
`<g,g+epsilon PCg>=||g||^2+epsilon<g,Cg>`. The second follows from
`<G_+^0,H_T^+H>=<G_+^0,H>`.

Formula (3.2) is important for typing: the missing theorem is a scalar pairing of the product port with the
unprojected oriented functional-equation defect. Recombining the two orientations before taking this pairing would
again yield the tautological completed commutator of `R161_018`.

## 4. Interaction with first-contact radicality

At a first contact the primitive compressed Weil form is nonnegative and `F` lies in its radical. Hence its
polarization satisfies

```
a_T(F,H)=0                 for every primitive H.                (4.1)
```

Therefore row D would close if one constructs, directly from the finite `(PC-ren)` data, a primitive conjugate
test `H_F` for which

```
a_T(F,H_F)=X_T(F).                                               (4.2)
```

Equations (4.1)--(4.2) give `X_T(F)=0`; (2.4) gives physical scattering; and `R161_019` then gives `F=0` from the
positive odd Gamma-pole lattice.

The content of (4.2) must be checked rather than postulated. Defining `H_F` by applying an inverse of the primitive
compression is circular, while testing against an arbitrary support-preserving modulation supplies only (4.1), as
proved in `P121_HORIZONTAL_MODULATION_RADICAL_NO_GO.md`. The admissible construction must instead come from the
mixed finite pairing before the two Poisson orientations are recombined. The crossed Tate corrections proved in
`R161_009` are precisely what is needed to make that finite test primitive.

## 5. Sharpened finite acceptance target

The previous leakage target asked for convergence of a projected defect norm. The strictly weaker sufficient
target is now:

> **L161.5 (oriented cross-correlation identity; OPEN).** Construct an explicit primitive `H_(M,N,T)F`, using only
> the finite `(PC-ren)` identity and its canonical crossed Tate correction, such that on a first-contact state
>
> ```
> lim a_T(F,H_(M,N,T)F)
>   =Re <G_+^0,zeta W_epsilon^0>
>   =X_T(F).                                                     (5.1)
> ```

The left side is zero termwise by radicality. Hence (5.1), if proved, closes the scattering gate without proving
vector convergence of `E_N^ren`, without a global contraction, and without estimating the leakage separately.

The test is falsifiable. It must satisfy all of the following:

1. retain the cross term between the two causal Poisson orientations;
2. perform the two Tate corrections before taking the limit;
3. produce the sign `epsilon` in (2.2), not an even norm square;
4. be constructed without `A_T^(-1)`, a Douglas contraction, or division by `zeta` on the critical line.

## 6. Status

- scalar extremal-correlation criterion: **PROVED**;
- identification with half the full scattering-defect square: **PROVED**;
- exact Hardy/Mellin cross-pairing formula: **PROVED**;
- closure from the finite radical pairing (5.1): **PROVED CONDITIONALLY**;
- construction and limit of the finite conjugate test in (5.1): **OPEN**;
- row D: **OPEN**.
