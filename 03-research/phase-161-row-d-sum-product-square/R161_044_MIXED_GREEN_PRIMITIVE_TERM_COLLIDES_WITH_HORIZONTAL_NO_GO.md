# R161_044 — Audit: the primitive `Xf` term is the old horizontal-modulation tautology

## 0. Verdict

The primitive component isolated in `R161_042` does not supply a new equality-state law. The test
`Pi_TP_TXf` is the first derivative at zero of the Tate-corrected horizontal modulation family
`Pi_T(e^(sigma t)f)`. Phase 121 proves that pairing a first-contact radical against this family and all its
derivatives merely restates radicality.

Together with `R161_043`, this exhausts the interior part of the proposed mixed Green route:

- the Tate component vanishes by opposite parity;
- the primitive component is an admissible but tautological radical test.

Any new information must therefore be an exterior ordering defect left over before adjoint recombination. This is
exactly the independent reciprocity term of `R161_023(5.3)`.

## 1. Identification with horizontal modulation

Let

```
G_sigma=Pi_T(e^(sigma X)f).                               (1.1)
```

The family is entire and primitive. Differentiating at zero gives

```
G_0=f,
G_0'=Pi_TP_TXf.                                         (1.2)
```

`P121_HORIZONTAL_MODULATION_RADICAL_NO_GO`, Theorem 3.1, proves that for a first-contact radical

```
a_T(f,G_sigma)=0                                        (1.3)
```

and every derivative of (1.3) is only the universal polarization

```
a_T(f,h)=0,             h in P_T.                       (1.4)
```

Thus

```
a_T(f,Pi_TP_TXf)=0                                      (1.5)
```

is true but contains no independent boundary information.

## 2. Consequence for `R161_042`

The mixed term

```
Re<E_Nf,C_NXf>                                          (2.1)
```

cannot be killed merely by observing that `Pi_TP_TXf` is primitive. To use (1.5), one must first prove that the
primitive portion of (2.1) is literally `a_T(f,Pi_TP_TXf)`. Establishing that identification requires moving the
finite causal synthesis across the support projection. The commutator created by that move is the exterior
boundary term sought from the beginning.

If that commutator is silently dropped, (2.1) appears to vanish but the proof is circular. If it is retained, the
interior part reduces to (1.5) and the exterior commutator remains.

## 3. Exact surviving quantity

Let `g_N` be the finite right product port and `w_N` the finite scattering defect. The two full-space orderings are

```
<g_N,S_N^ren w_N>,
<(S_N^ren)*g_N,w_N>.                                    (3.1)
```

They are equal by adjointness before support is split. After inserting the physical projections, their difference
is a sum of Hankel boundary terms of the form

```
P S_N^ren(I-P),          (I-P)S_N^ren P.               (3.2)
```

The interior primitive part of (3.1) is the tautology (1.5); the Tate part vanishes in the `Xf` ordering by
`R161_043`. Hence the only possible new law is an antisymmetric relation among the terms (3.2).

This is precisely L161.6 from `R161_023`, now reached from the mixed Green calculation rather than postulated.

## 4. Minimal scalar gate

The exterior reciprocity need only imply

```
Re<g,e>=0,
e=P_+C_log g+epsilon g.                                 (4.1)
```

By `R161_021`,

```
1/2||(I+epsilon C_log)g||^2
 =Re<g,e>.                                             (4.2)
```

Thus (4.1) forces exact scattering and closes D through `R161_019`. No vector equality or global direct-sum square
is required.

## 5. Status

- identification `Pi_TP_TXf=G_0'`: **PROVED**;
- primitive horizontal-modulation pairing: **KNOWN TAUTOLOGY**;
- opposite-parity Tate component: **ZERO by `R161_043`**;
- reduction of any new content to exterior ordering/Hankel commutators: **PROVED STRUCTURALLY**;
- antisymmetric exterior reciprocity: **OPEN / TERMINAL**;
- row D: **OPEN**.
