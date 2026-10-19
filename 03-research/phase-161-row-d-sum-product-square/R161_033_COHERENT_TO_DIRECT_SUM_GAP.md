# R161_033 — Audit: `(PC-ren)` is coherent in `k`; the direct-sum square needs a proved dilation

## 0. Verdict

`R161_031` correctly identifies the two path outputs over every completed factorization fibre `de=k`. It does not,
by itself, realize the direct-sum norm appearing in `R161_030`. The finite operator identity `(PC-ren)` sums the
outputs coherently in the physical Hilbert space. Passing from the norm of that sum to the sum of the individual
norms deletes all cross-`k` interference and is not an algebraic consequence of `(PC-ren)`.

Therefore the claim in `R161_031` that the discrete source realization is complete is withdrawn. The path vectors
are constructed, but the second-moment/dilation map which would make their labels orthogonal remains open. This is
not a cosmetic distinction: it is exactly the information needed for the variance saturation.

## 1. What `(PC)` actually contains

On the completed interior, the two unrecombined Chebyshev orientations are

```
J K_N f=sum_(2<=k<=N)(log k)/sqrt(k) Jtau_(log k)f,
K_N Fcal f=sum_(2<=k<=N)(log k)/sqrt(k) tau_(log k)Fcal f. (1.1)
```

Their difference is the coherent vector

```
Y_N(f)=sum_(2<=k<=N)(log k)/sqrt(k) Delta_k f,
Delta_k=tau_(log k)Fcal-Jtau_(log k).                     (1.2)
```

The corresponding physical norm is

```
||Y_N(f)||^2
 =sum_(k,l<=N)(log k)(log l)/sqrt(kl)
   <Delta_k f,Delta_l f>.                                (1.3)
```

By contrast, `R161_031(4.2)` introduced

```
D_N^orient(f)
 =1/4 sum_(k<=N)(log k)^2/k ||Delta_k f||^2,             (1.4)
```

which is the diagonal of (1.3), with every `k!=l` term removed.

## 2. The missing operator

Let

```
H_N^src=direct_sum_(2<=k<=N) H
```

and define the labelled analysis map

```
Af=((log k)/sqrt(k) Delta_k f)_k.                       (2.1)
```

Then `(1.4)=||Af||^2/4`. The physical `(PC)` vector is instead

```
Y_N=S Af,       S((u_k)_k)=sum_k u_k.                   (2.2)
```

The synthesis map `S` is not an isometry. In particular

```
||SAf||^2=||Af||^2
```

is equivalent to the vanishing of the total cross-`k` Gram term. No such orthogonality is present for translated
copies of a general compactly supported source, and additive Fourier does not make distinct logarithmic
translations orthogonal.

Hence retaining a formal source label is legitimate bookkeeping, but taking its direct-sum norm requires an
additional Parseval/Naimark identity or a compensating boundary Gram.

## 3. Finite counterexample to an automatic lift

The gap already occurs with two labels. Take any nonzero `u in H` and set the two labelled outputs equal:

```
u_2=u_3=u.
```

Then

```
||u_2+u_3||^2=4||u||^2,
||u_2||^2+||u_3||^2=2||u||^2.                         (3.1)
```

Taking `u_2=-u_3` makes the coherent norm zero while the direct-sum norm remains positive. Thus no identity between
the two quantities follows from a coherent vector equation. The actual `Delta_k f` are constrained, but proving
the requisite Gram identity for them is additional mathematics, not a consequence of their labels.

## 4. Corrected status of the oriented divisor gate

The valid conclusions of `R161_030`--`R161_031` are:

1. the two-level variance identity is exact in a genuinely labelled Hilbert space;
2. the path outputs supplied by `J L_MS_N` and `L_MS_NFcal` are independent of `d` on a completed fibre;
3. the divisor seam therefore vanishes within each fibre;
4. the surviving fibre energy is the diagonal expression (1.4).

The unproved conclusion is that finite `(PC-ren)` supplies the labelled second moment or saturates it at first
contact.

## 5. Where the missing Gram may live

There are only two noncircular possibilities inside the current architecture:

### A. A source dilation

Construct an explicit isometry `V_N:H->H_N^src` from additive Poisson/Fourier data such that its physical synthesis
is the coherent `(PC-ren)` port and its norm is (1.4). This would be a genuine Naimark/Parseval theorem and would
justify the direct-sum square.

### B. Exact compensation of the cross Gram

Keep the interference

```
I_N(f)=sum_(k!=l)(log k)(log l)/sqrt(kl)
       Re<Delta_kf,Delta_lf>                               (5.1)
```

and prove that the polar/Gamma and parity-oriented Tate boundary concomitants equal `-I_N` plus the desired
positive boundary squares. In this reading the endpoint term is not an error: it is the missing Gram completion.

Route B is closer to `(PC-ren)`, because the latter already contains the coherent synthesis and its polar boundary.

## 6. Consequence for `R161_032`

The algebraic identity

```
epsilon<v,G_TCv>=||r||^2                                  (6.1)
```

remains correct. What is not yet proved is that the finite Green expansion produces the concomitant with the sign
`+epsilon<v,j>`. The ordering and sign must be derived while retaining (5.1). Thus parity resolves the sign of a
correctly oriented endpoint term, but does not prove that this is the endpoint term appearing in the source
identity.

## 7. Revised terminal statement

The next exact theorem must be one of:

```
source Parseval dilation:       ||V_NF||^2=D_N^orient(F),
```

or

```
coherent Green completion:
I_N(F)+B_N^polar(F)+B_T^Tate(F)
 =2D_(T,delta)^Gamma(F)+D_N^boundary(F),
D_N^boundary(F)>=0,                                      (7.1)
```

with the first-contact equation annihilating the complete coherent left side. Neither statement is presently
proved.

## 8. Status

- pathwise factorization over `de=k`: **PROVED**;
- direct-sum variance identity as abstract algebra: **PROVED**;
- derivation of its second moment from `(PC-ren)`: **OPEN / PREVIOUS CLAIM WITHDRAWN**;
- parity-oriented crossed Gram identity: **PROVED**;
- occurrence of that Gram with the required sign in finite Green bookkeeping: **OPEN**;
- row D: **OPEN**.
