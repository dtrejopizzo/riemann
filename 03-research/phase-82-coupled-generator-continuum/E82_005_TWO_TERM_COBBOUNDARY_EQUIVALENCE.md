# E82.005 - Two-term expansion and coboundary equivalence

## 1. Exact cluster decomposition

Let `M_N` be self-adjoint, let `P_N` be a spectral cluster projection and put
`Q_N=I-P_N`.  For a solution

```text
M_N h_N=f_N,                                           (1.1)
```

write `h_N=p_N+r_N` with `p_N=P_Nh_N` and `r_N=Q_Nh_N`.
Because `P_N` is spectral, it commutes with `M_N`, and therefore

```text
Q_N M_N Q_N r_N=Q_N f_N.                              (1.2)
```

Whenever the complement is invertible,

```text
r_N=(Q_N M_N Q_N)^(-1)Q_N f_N.                        (1.3)
```

Thus a source-retaining second term is exactly a reduced complement response.

## 2. Inverse-free criterion

### Theorem 2.1

Let `C_N=Q_NM_NQ_N` be invertible.  Suppose an independently constructed
vector `u_N in ran Q_N` and an error `e_N` satisfy

```text
Q_N f_N=C_N u_N+e_N.                                  (2.1)
```

Then

```text
r_N-u_N=C_N^(-1)e_N.                                  (2.2)
```

Conversely, every approximation `u_N` to `r_N` defines the exact coboundary
error

```text
e_N=C_N(r_N-u_N),                                     (2.3)
```

and satisfies (2.1).

### Proof

Subtract (2.1) from `C_N r_N=Q_Nf_N` and apply `C_N^{-1}`.  The converse is
the same identity read backward. `QED`

The theorem proves that an inverse-free two-term expansion exists only through
an explicit coboundary decomposition (2.1).  Defining
`u_N=C_N^{-1}Q_Nf_N` is tautological and supplies no estimate.

## 3. Correct topology

For the safe Cauchy functional `ell_{N,z}`, (2.2) gives

```text
ell_{N,z}(r_N-u_N)=ell_{N,z}(C_N^(-1)e_N).             (3.1)
```

Hence the exact sufficient estimate is

```text
sup_{z in K}|ell_{N,z}(C_N^(-1)e_N)| -> 0,             (3.2)
```

together with one derivative when a log-current is required.  This is a
directional graph-norm estimate, not an ambient inverse bound.

## 4. Crosswalk to the earlier endpoint

The previous prolate corrector program required

```text
Q R k=C u+e,
ell_z(C^(-1)e)->0,                                     (4.1)
```

and called its minimal scalar form Weyl-reduced leakage.  Equations
(2.1)--(3.2) are the same mathematical obligation for the coupled-generator
source.  The later Abel analysis of (4.1) reached the resonance barrier: an
inverse-free construction needs a new finite arithmetic spectral coboundary.

Therefore the source-retaining Path B is not independent of the historical
corrector route.  It is its two-generator coordinate form.

## 5. New target after the equivalence

The only admissible new statement is now explicit:

```text
TWO-GENERATOR-ARITHMETIC-COBOUNDARY:
construct u_N directly from the finite Gamma-prime and Euler--Mobius algebra
such that

  Q_N f_N=C_N u_N+e_N,

and prove (3.2) bilaterally and locally uniformly, with the resulting
correction current equal to the independent Euler--Gamma defect.        (5.1)
```

The construction may not use `C_N^{-1}`, a zero filter, fitted residues or
the target logarithmic derivative as its definition.

## 6. Status

```text
proved:
  the exact complement equation (1.2);
  equivalence of a two-term expansion and an explicit coboundary;
  the correct safe topology (3.2);

closed:
  Path B as a new method distinct from the earlier corrector route;

localized:
  all remaining new mathematics to TWO-GENERATOR-ARITHMETIC-COBOUNDARY;

open:
  construction and estimate (5.1).
```

