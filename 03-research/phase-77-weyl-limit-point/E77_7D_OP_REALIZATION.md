# E77.7d - Fixed-L Operator Realization

**Run:** 2026-07-18.

## 1. Verdict

The proposed pure-frequency Loewner factorization is correct, but the full
Gamma-prime operator is not bounded.  The archimedean diagonal grows like
`log|n|`.  The correct theorem is stronger than the gate actually required:

```text
H_L=D_L+B_L,
D_L self-adjoint diagonal and lower bounded,
D_L(n)=log(1+|n|)+O_L(1),
B_L bounded and self-adjoint.
```

Consequently `H_L` has a canonical lower-semibounded self-adjoint realization,
`c00` is an operator and form core, and the min--max theorem of E77.7c closes
`MU-LIMIT`.

## 2. Pure-Frequency Loewner Block

For `d_n=2 pi n/L` and one frequency `omega`, define

```text
L_omega(m,n)
=(exp(i omega d_m)-exp(i omega d_n))/(d_m-d_n).
```

Then

```text
L_omega=U_omega T_omega U_omega,
U_omega(n,n)=exp(i omega d_n/2),
T_omega(m,n)=2i sin(omega(d_m-d_n)/2)/(d_m-d_n).
```

`U_omega` is unitary.  On the arithmetic mesh, `T_omega` is Toeplitz and its
Fourier multiplier is a band indicator.  For `0<=omega<=L`,

```text
||T_omega||<=L,
||(2/L)L_omega||<=2.                           (OR-1)
```

The probe verifies the factorization to `1.37e-61`; the scaled finite-section
norm is `1.99999994` against the bound `2`.

## 3. Arithmetic and Planted Parts

At fixed `L`, the prime-power package is a finite sum of cell operators:

```text
-sum_{p^k<=lambda^2} log(p)p^(-k/2) Q_{k log p}.
```

Since `||Q_y||<=2(1-y/L)`, it is bounded and self-adjoint.  The planted
addition is another finite-interval frequency package and is bounded and
self-adjoint as well.  This proof is falsifier-neutral.

At `lambda=6,N=12`, the measured norms are

```text
zeta:          3.70794,
plant:        23.58569,
plant extra:  19.91830,
symmetry defect: 0.
```

## 4. Why Finite Total Variation Is the Wrong Archimedean Proof

For the sine symbol, the archimedean density contains

```text
g_L(y)=2 cosh(y/2)-exp(y/2)/(2 sinh y)
      =-1/(2y)+O_L(1),  y->0.
```

Thus its total variation is infinite.  Numerically,

| lower cutoff | truncated variation |
|---:|---:|
| 1e-2 | 10.5829 |
| 1e-4 | 12.8682 |
| 1e-6 | 15.1706 |
| 1e-8 | 17.4731 |
| 1e-10 | 19.7757 |

Therefore the estimate `pi |nu|(R)` cannot be applied to the complete WR
measure.  The singular package must be treated after its Dirichlet
cancellation.

## 5. Bounded Off-Diagonal Part

The sampled sine symbol is uniformly bounded.  Indeed, split its
archimedean density into `-1/(2y)` plus an `L1[0,L]` remainder.  Then

```text
int_0^L sin(d_n y)/y dy
```

is uniformly bounded by the Dirichlet integral, while the regular remainder,
the finite prime package, and the plant package are bounded absolutely.
Hence

```text
sup_n |S_L(d_n)|<infinity.                     (OR-2)
```

Let `K` be the discrete Hilbert transform,

```text
K_mn=1/(m-n),  m!=n,  K_nn=0,
```

which is bounded on `l2(Z)`.  The off-diagonal Loewner part is exactly

```text
H_L^off=-(1/pi)[diag(S_L),K].                  (OR-3)
```

Equations `(OR-2)--(OR-3)` prove that `H_L^off` is bounded.  This keeps the
entire almost-periodic prime potential; it is not treated as a compact tail.

## 6. Diagonal Asymptotic

For `q_nn(y)=2(1-y/L)cos(d_n y)`, isolate the singular WR term:

```text
- integral_0^L
  [exp(y/2)q_nn(y)-2]/[2 sinh y] dy
= integral_0^L [1-cos(d_n y)]/y dy + O_L(1).
```

All discarded terms have an `L1` majorant independent of `n`; W02 is bounded
by its finite-interval `L1` kernel; and the prime/plant diagonal packages are
bounded trigonometric sums.  The classical cosine-integral asymptotic gives

```text
int_0^L [1-cos(d_n y)]/y dy
=log(1+|d_n|)+O_L(1).
```

Therefore

```text
H_L(n,n)=log(1+|n|)+O_L(1).                   (OR-4)
```

The probe shows the slow emergence of this law:

| n | archimedean diagonal | value/log(n) |
|---:|---:|---:|
| 20 | 1.7174 | 0.5733 |
| 100 | 3.3287 | 0.7228 |
| 200 | 4.0220 | 0.7591 |
| 500 | 4.9383 | 0.7946 |
| 1000 | 5.6215 | 0.8138 |

This refutes boundedness but proves the lower-bounded diagonal structure.

## 7. Self-Adjoint Realization

Let `D_L` be multiplication by the real sequence `H_L(n,n)` on

```text
Dom(D_L)={u in l2: (H_L(n,n)u_n)_n in l2}.
```

By `(OR-4)`, `D_L` is self-adjoint and lower bounded, and `c00` is an operator
and form core.  By `(OR-3)`, the remainder `B_L=H_L-D_L` is bounded and
self-adjoint.  The bounded perturbation theorem gives a unique self-adjoint
lower-semibounded operator

```text
H_L=D_L+B_L,  Dom(H_L)=Dom(D_L).               (OR-5)
```

The same proof applies to the planted build.

## 8. MU-LIMIT Closure

The finite CCM matrices are exactly the nested compressions of `(OR-5)` to
the centered coordinate spaces.  Since `c00` is a form core, E77.7c applies:

```text
mu_{L,N}=lambda_min(P_N H_L P_N)
decreases to
mu_L=inf spec(H_L) in R.                       (OR-6)
```

Thus `OP-REALIZATION` and `MU-LIMIT` are closed for zeta and planted builds.

## 9. Probe

```text
E77_7d_op_realization_probe.py
E77_7d_op_realization_results.json
```

The finite norms through `N=24` are compatible with the decomposition.  They
are not used as a proof of boundedness; the diagonal asymptotic explicitly
shows that the full infinite operator is unbounded above.

## 10. Next Object

With `MU-LIMIT` closed, the directional identity is

```text
r_z[x_N(mu_N)-x_N(mu_L)]
=(mu_N-mu_L)
 r_z A_N(mu_N)^(-1)A_N(mu_L)^(-1)b_N.          (OR-7)
```

The next finite object is the declared interlacing denominator:

```text
DIR-GAP-PAIR:
the product in (OR-7), after the Cauchy pairing, is
o(1/|mu_N-mu_L|)
on an admissible resonance-avoiding block subsequence.
```

No ambient inverse norm is allowed.  If the plant requires a subsequence,
the zero-filter audit must precede any use of that distinction as arithmetic
information.

## 11. Status

```text
proved:    pure-frequency Loewner factorization and bound;
proved:    bounded prime and planted packages;
refuted:   finite total variation of the complete archimedean measure;
refuted:   boundedness of the full fixed-L operator;
proved:    H_L=D_L+B_L, D_L~log(1+|n|), B_L bounded;
proved:    OP-REALIZATION and MU-LIMIT for both builds;
open:      DIR-GAP-PAIR, FIXED-MU-BLOCK-GROWTH, SHELL-CAUCHY-GROWTH;
next:      E77.7e paired interlacing-gap audit.
```

