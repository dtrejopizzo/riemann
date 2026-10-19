# R161_032 — Parity turns the crossed Tate block into the missing positive square

## 0. Verdict

The crossed Tate matrix is indefinite on the full two-dimensional Tate space, as emphasized in `R161_023`, but a
first-contact state does not explore that full space: it lies in a fixed parity line. On that line the exchange
matrix is the scalar `epsilon`. Consequently the parity-oriented crossed pairing is exactly the positive Tate norm.

This is the algebraic sign conversion required by the scattering defect, whose target eigenvalue is
`sigma=-epsilon`. It removes the wrong-sign obstruction if the finite Green expansion produces the oriented
concomitant `+epsilon<v,j>`.
It does not by itself prove that the full `(PC-ren)` boundary pairing equals the sum of the already identified
Poisson, Gamma and Tate squares; that final bookkeeping identity remains to be written without losing the source
labels.

## 1. Gram and crossed matrices

In the ordered Tate basis

```
phi_- = exp(-t/2),          phi_+ = exp(t/2),
```

let

```
G_T=2[[sinh T,T],[T,sinh T]],
C  = [[0,1],[1,0]].                                      (1.1)
```

Then `G_T` is the positive Gram matrix and the collar system uses

```
A_T^cross=G_TC=2[[T,sinh T],[sinh T,T]].                (1.2)
```

The matrices commute because both are linear combinations of `I` and `C`.

## 2. Parity-line positivity

Let `F` have parity `epsilon in {+1,-1}`. The first-contact forcing

```
r=alpha phi_-+beta phi_+
```

has the same parity, so its coefficient vector `v=(alpha,beta)^t` satisfies

```
Cv=epsilon v.                                             (2.1)
```

### Theorem 2.1 (parity-oriented crossed Gram identity)

For every `v` satisfying (2.1),

```
epsilon <v,G_TCv> = <v,G_Tv> = ||r||_(L2(-T,T))^2.        (2.2)
```

In particular the left side is nonnegative and vanishes if and only if `r=0`.

*Proof.* From (2.1), `G_TCv=epsilon G_Tv`. Multiply by `epsilon`, use `epsilon^2=1`, and recall that `G_T` is the
Gram matrix of `(phi_-,phi_+)`. QED.

Explicitly, for `v=c(1,epsilon)^t`,

```
||r||^2=4|c|^2(sinh T+epsilon T)>0                    (2.3)
```

for `c!=0`; when `epsilon=-1`, positivity follows from `sinh T>T`.

## 3. Relation with the collar current

The exact phase-121 collar equation is

```
j=(J_+,J_-)^t=G_TCv.                                  (3.1)
```

Parity gives `Cj=epsilon j`. Pairing (3.1) with `v` and applying (2.2) yields

```
boxed: epsilon <v,j>=||r||^2.                         (3.2)
```

Thus the crossed endpoint concomitant must not be discarded and must not be treated as an indefinite error. With
the same parity sign appearing in the physical scattering square, it is a positive endpoint energy.

This does not contradict `R161_023`: on the full Tate plane `G_TC` is indefinite. The new statement uses the proved
first-contact parity restriction before taking the sign.

## 4. Compatibility with the scattering sign

`R161_021` proves that the desired physical equation is

```
C_log g=-epsilon g
```

and that its defect is

```
X_T(F)=||g||^2+epsilon<g,C_log g>
      =(1/2)||(I+epsilon C_log)g||^2.                 (4.1)
```

The endpoint conversion (3.2) carries exactly the same `epsilon`. Therefore, if the oriented finite Green identity
has the following sign,
the form

```
0=X_T(F)+||r||^2+D_T^orient(F)+2D_(T,delta)^Gamma(F)  (4.2)
```

would be a sum of nonnegative terms and would immediately force

```
X_T(F)=0,      r=0,      D_T^orient(F)=0,
D_(T,delta)^Gamma(F)=0.                                 (4.3)
```

Either the first or fourth equality closes the physical scattering/Gamma-pole gate already proved in
`R161_019`--`R161_021`.

Equation (4.2) is a candidate finite bookkeeping theorem. The content of this note is that a Tate term occurring as
`+epsilon<v,j>` has the correct sign and normalization once parity is inserted. `R161_033` records that both this
occurrence/sign and the cross-`k` Gram completion still have to be derived.

## 5. Acceptance boundary

To prove (4.2), the next calculation must begin with the two unrecombined orientations of `(PC-ren)`, polarize
with the parity-reflected port, and retain the endpoint vector `j` until the last line. Substitution of (3.2) is
allowed only after the full boundary Green identity has produced `epsilon<v,j>`.

It would be circular to insert `X_T` by definition or to infer (4.2) from primitive radicality alone. The required
new statement is equality of the finite source pairing with the four displayed energies.

## 6. Status

- parity restriction `Cv=epsilon v`: **PROVED in phase 121**;
- parity-oriented crossed Gram identity (2.2): **PROVED**;
- exact endpoint conversion `epsilon<v,j>=||r||^2`: **PROVED**;
- conditional compatibility with the scattering sign: **PROVED**;
- full finite Green bookkeeping identity (4.2): **OPEN / TERMINAL**;
- row D: **OPEN**.
