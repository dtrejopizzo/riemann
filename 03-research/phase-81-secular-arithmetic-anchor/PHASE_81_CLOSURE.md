# Phase 81 closure - Secular loop theorem

## 1. Outcome

The phase closes with a theorem-grade obstruction to the proposed secular
shortcut.

```text
bordered determinant
 = denominator-free secular function
 = symmetrized real spectral shift
 = rank-two displacement residues
 = two-generator numerator.                             (1.1)
```

The equalities are exact.  They provide useful coordinates and remove the
dangerous division by `c`, but they do not construct an Euler--Gamma comparison
object independent of the CCM transfer.

## 2. Proved results

```text
1. F(z)=c-q^T(zI-D)^(-1)x without assuming c!=0.
2. The bilateral core characteristic factors as A(s)G(iu)G(-iu).
3. Its logarithmic derivative is the Poisson transform of the even real
   spectral shift.
4. An even shift is uniquely determined by that transform.
5. Defining the target shift by inverse transform is circular.
6. The residues satisfy a=-alpha_b u-beta_b v exactly.
7. Substitution recovers the old two-generator numerator exactly.
```

## 3. Remaining arithmetic theorem

The open statement is

```text
i G_L'(iu)/G_L(iu)-i G_L'(-iu)/G_L(-iu)
 -[H_L(s)-d/ds log A_L(s)] -> 0                        (3.1)
```

as `L->infinity`, after the fixed-`L` limit has been taken.  Here

```text
G_L(z)=lim_N {1+alpha_b[U_N(z)+U_{b,N}]
                 +beta_b[V_N(z)+V_{b,N}]}.             (3.2)
```

Thus the hard step is the joint continuum limit of the coupled generator
solutions.  Spectral-shift coherence cannot replace it.

## 4. Route decision

The Loewner interpolation residual is not reopened: its off-mesh magnitude was
already shown to grow, so small-remainder estimation is invalid.  The next
phase works directly with

```text
M_N h_N=f_N,
h_N=alpha_b u_N+beta_b v_N,
f_N=alpha_b s_N+beta_b 1,                              (4.1)
```

and with the normalized Cauchy profile of `h_N`.

## 5. Status

```text
phase result:
  closed at obstruction and exact-reduction grade;

refuted:
  the zeros of the bordered determinant as an independent arithmetic measure;

open:
  the coupled generator outer identity (3.1);

next phase:
  direct projective continuum limit of (4.1), with no interpolation-remainder
  estimate.
```

