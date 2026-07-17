# P75.013-P75.015 - Theorem assembly or mandatory autopsy

## Theorem attempt

The intended proof was:

```text
ARITH-LOCK
=> CRIT-NUM-DIV
=> CCM-ROOT-LOCK
=> CAUCHY-EIG-LOC
=> HPR-DIV
=> Omega7.
```

P75.002 and P75.003 successfully canonicalized the finite numerator:

```text
C_L(z)=P_L(z)/D_L(z),
P_L(z)=-det [[diag(z-d),xi],[1^T,0]],
|P_L(z)|^2=|D_L(z)|^2 r_z^* adj(H_L-mu_L I)r_z/tr adj(H_L-mu_L I).
```

This proves that the problem can be posed without fitting to `xi_L` or using
a pseudoinverse.  It does not prove divisibility.

P75.004-P75.006 then inserted the finite Euler/Gamma decomposition into the
adjugate/minor expression.  The only exact signed recombination obtained is
the old endpoint:

```text
REM_L(gamma)=EG_LOCK_L(gamma)=TPW/scalar-WRL endpoint.
```

No independent `ARITH-REM` estimate was found.

P75.007-P75.009 audited the escape routes:

```text
cutoff smoothing: either changes CCM or returns to EG_LOCK;
derivative separation: transports smallness but does not create it;
Schur conditioning: finite numerics are benign, theorem-grade lower bound
requires CAUCHY-COMP/global signed positivity.
```

P75.010-P75.012 confirmed that the falsifiers still discriminate the zeta
case numerically, but no candidate theorem survived as a proof input.

## Assembly status

The following conditional chain remains valid:

```text
ARITH-LOCK
=> CRIT-NUM-DIV
=> CCM-ROOT-LOCK
=> CAUCHY-EIG-LOC
=> HPR-DIV
=> E72.396 NAT-PROJ
=> E72.326 PW-Cauchy
=> SQB => CB => RNS => MC-NZ => NZ-MSD
=> scalar WRL
=> Omega7.
```

The missing theorem is exactly:

```text
ARITH-LOCK:
r_gamma^* adj(H_L-mu_L I) r_gamma
has a critical Xi divisor up to O_M(L^-M)
in resolved windows.
```

## Mandatory autopsy

Phase 75 does not close Omega7.  It produces the following P75.015 outcomes:

```text
C. the cota requerida equivale exactamente a TPW/scalar WRL;
D. the cutoff needed for all-orders tails destroys or rebuilds the CCM chain;
E. Schur compression needs the unresolved global signed positivity/CAUCHY-COMP.
```

The most explicit surviving finite object is sharper than E74's named
`EG_LOCK`:

```text
ADJ-ARITH-LOCK_L(gamma):
r_gamma^* adj(H_L-mu_L I) r_gamma
= O_M(L^-M) / |D_L(gamma)|^2
```

after the fixed normalization of `Q_gamma`.

Equivalently:

```text
P_L(gamma)=O_M(L^-M)D_L(gamma).
```

This object is finite, phase-free, and falsifier-stable.  It is the correct
next target if the program continues, because it is the first formulation in
which the eigenline has been eliminated without weakening the endpoint.

## Final conclusion

Omega7 remains open.  Phase 75 completed the planned attack and reduced the
endpoint from an eigenline cancellation statement to a phase-free adjugate
minor divisibility theorem.  No admissible proof of the required all-orders
arithmetic remainder was obtained.

