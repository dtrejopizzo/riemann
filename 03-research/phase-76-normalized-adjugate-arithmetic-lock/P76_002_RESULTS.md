# P76.002 results - multiprecision construction and cutoff cascade

Command:

```text
python3 P76_002_mp_entry_audit.py
```

Unlike E74.016, this probe rebuilds every CCM integral and every matrix entry
at the requested precision.  It uses the exact endpoint limit

```text
lim_{y->0} (e^(y/2)q(y)-q(0))/(2 sinh y)
=(q'(0)+q(0)/2)/2.
```

## Precision separation

For `lambda=6`, `L=3.583518938`, and `N=6`, the 50- and 80-digit runs agree
in all displayed digits:

```text
lowest eigenvalue = 5.67857981289e-23
spectral gap       = 2.73055771723e-20
q(gamma_1)         = 3.86207303800e-15
q(gamma_1+0.125)   = 1.89362964188e-8
```

The eigenpair residual changes from `1.3e-52` to `8.7e-83`, while the
eigenvalues and Cauchy values do not change.  Therefore the observed values
are properties of the finite CCM matrix, not the eigensolver precision
floor.

The lowest eigenvalue is positive and separated in this resolved case.  The
large float64 nullspace in P76.001 is the thresholded image of a genuine
positive spectral cascade, as Phase 62 had reported.

## Fixed-L cutoff sequence

At fixed `lambda=6`, increasing the Fourier cutoff gives:

```text
N     mu_0                 gap                   q(gamma_1)
3     9.98828001369e-15    7.38854828444e-12    1.29523075352e-7
4     3.79740018923e-18    2.90796593060e-15    1.61565380484e-10
5     7.43488086417e-21    3.01881667995e-18    6.54501922885e-13
6     5.67857981289e-23    2.73055771723e-20    3.86207303800e-15
```

The displaced control is:

```text
N     q(gamma_1+0.125)
3     3.37930256615e-7
4     9.03912170339e-8
5     3.40151403750e-8
6     1.89362964188e-8
```

Thus the critical row exhibits much faster, ordinate-selective convergence.
The phenomenon is not caused by importing a zero list or by finite precision.

## What this does and does not prove

This is the strongest clean numerical evidence produced by Phases 74-76:
the finite arithmetic matrix, built from primes and the archimedean kernel,
selects the first critical ordinate through its resolved simple ground
eigenline.

It does not yet prove `NORMALIZED-ARITH-LOCK` because:

```text
1. the displayed sequence varies N at fixed L, whereas closure needs a
   specified joint N(L), L->infinity regime;
2. no uniform analytic estimate for the critical overlap has been proved;
3. deriving a bound on one critical evaluation from the minimum Weil energy
   via a positive zero sum would invoke global Weil positivity and be
   circular.
```

## Next theorem target

The next admissible object is the phase-free simple-projector observable

```text
A_{L,N}(gamma)=r_gamma^* Pi_{0,L,N} r_gamma / ||r_gamma||^2,
```

where `Pi_0` is the resolved ground spectral projector.  Phase 76 must obtain
its cutoff decay from the finite prime/archimedean construction or from an
exact resolvent identity, not from positivity of the zero-side Weil sum.
