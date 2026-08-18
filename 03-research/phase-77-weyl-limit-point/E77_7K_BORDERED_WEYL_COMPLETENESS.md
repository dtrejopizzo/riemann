# E77.7k - Bordered Weyl completeness and the singular-section correction

**Run:** 2026-07-18.

## 1. Purpose

E77.7i showed that scalar contraction alone does not prove the P76.065
endpoint.  An independent audit sharpened two points:

```text
1. the uniqueness criterion on the ground eigenspace reduces to simplicity
   plus nonzero normalization coupling, because safe Cauchy rows separate l2;
2. the statement "A_N(mu_L) singular infinitely often => radius already
   zero" is false as written.
```

This note records the exact correction and names the minimum admissible
bordered Weyl theorem.

## 2. Separation of safe Cauchy rows

Let

```text
C(v)(z)=r_z v = sum_n v_n/(z-d_n)
```

on the safe axis.  If `C(v)(z)=0` on a safe interval, analytic continuation
and the simple residues at `z=d_n` imply `v_n=0` for every `n`.  Hence:

```text
ker C = {0} on l2.                               (K-1)
```

Therefore the E77.7i uniqueness criterion

```text
E_L cap ker ell_0 subset ker C
```

reduces exactly to

```text
E_L cap ker ell_0 = {0}.                        (K-2)
```

Since `ell_0` is scalar, `(K-2)` is equivalent to:

```text
dim E_L = 1,
r_{z0} e_L != 0                                 (K-3)
```

for a generator `e_L` of `E_L=ker(H_L-mu_L)`.

Compact resolvent does not prove `(K-3)`.

## 3. Singular sections do not collapse automatically

Let

```text
A_N(mu_L)=H_L[I_N,I_N]-mu_L I,
K_N=ker A_N(mu_L).
```

For the regularized resolvent,

```text
||(A_N(mu_L)-i eta)^(-1)b_N||^2
 = ||P_{K_N} b_N||^2 / eta^2
   + sum_{lambda_j != 0}
       |<u_j,b_N>|^2 / (lambda_j^2+eta^2).      (K-4)
```

Thus:

```text
P_{K_N}b_N != 0  => incompatibility of A_N x=b_N and blowup of the
                    regularized norm;
P_{K_N}b_N = 0   => solvability with nonuniqueness and bounded minimum-norm
                    solution as eta->0.
```

So singularity alone does not produce an ordinary radius-zero Weyl disk.
Without projective regularization and center control, a pole may send the
center to infinity rather than collapse the disk in the Euclidean sense.

The shorthand in E77.7g

```text
A_N(mu_L) singular infinitely often => radius already zero
```

is therefore refuted as stated.

## 4. Minimum admissible bridge

The missing theorem is:

```text
BORDERED-WEYL-COMPLETENESS

1. For one fixed pencil and one fixed boundary normalization, the finite
   objects D_N(z) are nonempty, nested bordered Weyl disks attached to the
   same realization H_L.

2. For every compact safe set K,
   sup_{z in K} rad D_N(z) <= C_K / (1 + S_N(mu_L)).

3. The intersection of the closed disks equals exactly
   { C(v) : v solves the infinite equation, v in l2, r_{z0}v=1 }.

4. The mu_L-based family is identified with, or transferred locally
   uniformly to, the mu=0 family used in P76.065.

5. The normalized class is nonempty and satisfies
   dim ker(H_L-mu_L)=1, r_{z0}e_L != 0.
```

Then:

```text
BTG-DIV-L + BORDERED-WEYL-COMPLETENESS
=> radius -> 0 locally uniformly on safe compacts
=> singleton intersection
=> unique normalized safe Cauchy transform.
```

## 5. LP versus IDENT

This audit also clarifies the split with P76.067.

```text
BTG-DIV-L + BORDERED-WEYL-COMPLETENESS
```

can close the **LP uniqueness component** of the safe endpoint.

But the stronger P76.065 wording

```text
namely that of k_L
```

still requires `IDENT`: one must prove that `k_L` belongs to the normalized
class and that its safe transform is the one selected by the LP limit.

So the candid chain is:

```text
BTG-DIV-L + BORDERED-WEYL-COMPLETENESS
=> LP-side uniqueness;

LP-side uniqueness + IDENT
=> SAFE-LIMIT-POINT as stated in P76.065.
```

## 6. Minimal live object

The LP interface target is now:

```text
BORDERED-WEYL-COMPLETENESS.
```

This strictly strengthens the earlier placeholder `SAFE-DISK-IDENT` by
including:

```text
separation,
singular-section regularization,
pencil compatibility,
existence of a normalized class,
simplicity/nonvanishing at mu_L.
```
