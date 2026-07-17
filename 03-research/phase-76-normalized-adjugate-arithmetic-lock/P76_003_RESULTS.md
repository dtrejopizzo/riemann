# P76.003 results - stable normalized observable

The product-free observable was evaluated independently as

```text
A_eigen
= |r_gamma^T xi|^2/||r_gamma||^2,

A_border
= -det [[mu I-H,r_gamma],[r_gamma^T,0]]
  /(p_H'(mu)||r_gamma||^2),

A_residue
= Res_{lambda=mu}
  r_gamma^T(lambda I-H)^(-1)r_gamma/||r_gamma||^2.
```

For the 80-digit `lambda=6`, `N=5` CCM matrix:

```text
mu               7.434880864165442e-21
gap              3.018816679951714e-18
A_eigen          4.2837276705974113353e-25
A_border         4.2837276705974113353e-25
A_residue        4.2837276705251792958e-25
border error     4.2e-81
residue error    7.2e-36
```

The bordered identity agrees to the working precision.  The resolvent value
uses a finite residue step and agrees to its predicted `O(delta/gap)` error.

This closes the P76.003 algebraic gate.  Direct products `D_L`, explicit
cofactor matrices, and an arbitrary eigenvector phase are unnecessary.  The
bordered determinant is valid only for a resolved simple eigenvalue; the
resolvent projector remains the canonical multiplicity-safe definition.
