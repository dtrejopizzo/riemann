# R161_036 — The coherent orientation difference is the Gamma-covariant critical jet

## 0. Verdict

The two vectors in `R161_035` have an exact Mellin interpretation. Their sum is the derivative of the finite
Poisson defect corrected by the Gamma connection; their difference converges, when the functional equation is
used, to the logarithmic zeta jet plus the same Gamma connection. At a critical zero the Gamma term vanishes and
the difference is exactly a nonzero multiple of `zeta'(rho)`.

Therefore saturation of the coherent parallelogram kills the already known faithful critical conormal detector.
No separate assertion that the direct-sum atoms vanish is required.

## 1. Finite renormalized notation

Put `s=1/2+i tau` and write

```
Z_N(s)=D_N(s)-N^(1-s)/(1-s),
e_N(s)=Z_N(s)u(s)-Z_N(1-s),                            (1.1)
```

where `u=u_infty` is the additive Fourier reflection multiplier. Let

```
K_N^ren(s)=-Z_N'(s).                                    (1.2)
```

This is the Mellin symbol of `K_N^ren=-[X,S_N^ren]` in the phase-161 convention.

The two coherent orientations have reflection symbols

```
U_N(s)=-Z_N'(s)u(s),
V_N(s)=-Z_N'(1-s).                                      (1.3)
```

## 2. Sum as a Gamma-covariant derivative

Differentiate (1.1):

```
e_N'(s)=Z_N'(s)u(s)+Z_N(s)u'(s)+Z_N'(1-s).             (2.1)
```

The final plus sign is from differentiating `-Z_N(1-s)`. Hence

```
boxed: U_N+V_N=-e_N'(s)+Z_N(s)u'(s).                   (2.2)
```

Since the Gamma multiplier in `X+Fcal X Fcal=M` is the logarithmic connection

```
m(s)=u'(s)/u(s),                                       (2.3)
```

equation (2.2) is exactly the Mellin form of

```
U_N+V_N=S_N^ren M Fcal-{X,E_N^ren}                    (2.4)
```

from `R161_035`. This independently checks all signs.

## 3. Difference and the completed jet

The orientation difference is

```
boxed: U_N-V_N=-Z_N'(s)u(s)+Z_N'(1-s).                (3.1)
```

Suppose the renormalized graph limit may be differentiated so that `Z_N->zeta` and `e_N'->0` on the test under
consideration. Differentiating the functional equation

```
zeta(s)u(s)=zeta(1-s)                                  (3.2)
```

gives

```
zeta'(s)u(s)+zeta(s)u'(s)+zeta'(1-s)=0.                (3.3)
```

Substitution into (3.1) yields

```
boxed: U_infty-V_infty
 =-2zeta'(s)u(s)-zeta(s)u'(s).                         (3.4)
```

Thus the coherent orientation square is the norm of the completed first jet, not a sign-blind square of the Weil
operator.

## 4. Evaluation at a critical zero

Let `rho=1/2+i gamma` be a simple nontrivial zero. Since `zeta(rho)=0`, (3.4) becomes

```
(U_infty-V_infty)(rho)=-2zeta'(rho)u(rho).             (4.1)
```

The Fourier factor is unimodular and `zeta'(rho)!=0`. Therefore, when the operator acts on a source with Mellin
transform `K_F(s-1/2)`, vanishing of the coherent difference forces

```
K_F(i gamma)=0.                                        (4.2)
```

This is precisely the critical conormal observation used in `R161_004(4.3)` and the critical-jet theorem of
`R161_007`. Once obtained for the required zero set, the previously proved Cartwright/density argument forces
`F=0`.

## 5. Analytic requirement

The passage from (3.1) to (3.4) is not automatic from pointwise convergence `e_N->0`. It requires convergence of
the differentiated, boundary-compressed renormalized defect in the first-contact graph. This is the same boundary
layer issue as the scattering leakage, now expressed as a first-jet convergence theorem.

The finite identity (2.2) shows exactly what must be controlled: `e_N'` cannot be discarded before its polar/Tate
boundary contribution is extracted. The bulk tends to zero; its compressed boundary germ is the possible anomaly.

## 6. Revised closure chain

It is sufficient to prove the first-contact saturation of `R161_035` together with differentiated graph
convergence:

```
D_N^coh(F)->0
 -> (U_N-V_N)F->0
 -> K_F(i gamma)=0 at every required critical zero
 -> F=0
 -> no first contact
 -> row D.                                                   (6.1)
```

Alternatively, the same limit may be identified with the physical scattering leakage and closed through the
Gamma-pole lattice. Formula (4.1) shows that both routes observe the same oriented jet.

## 7. Status

- finite covariant derivative identity (2.2): **PROVED**;
- finite coherent jet formula (3.1): **PROVED**;
- limiting completed jet (3.4): **PROVED CONDITIONAL ON DIFFERENTIATED GRAPH CONVERGENCE**;
- critical-zero value (4.1): **PROVED under that convergence**;
- faithfulness of the critical conormal observation: **PREVIOUSLY PROVED**;
- first-contact saturation and differentiated boundary convergence: **OPEN / TERMINAL**;
- row D: **OPEN**.
