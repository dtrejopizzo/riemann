# R161_067 — Dichotomy for finite oriented Laurent observations

## 1. Two possible finite germs

Fix `s_m=2m+1`, `m>=1`, and a small circle `C_m` contained in `Re s>1`.  Every finite Dirichlet polynomial,
finite hyperbola remainder, Muntz discrepancy and Tate correction occurring in `(PC-ren)` is holomorphic on and
inside `C_m`.  The only term with a pole at `s_m` is the completed Gamma logarithmic derivative

    d_Gamma(s)K_F(s-1/2).                                     (1.1)

Consequently a proposed separated finite germ has exactly two cases.

### Case A: the Gamma factor is not inserted

Then the germ `G_(M,N)^-` is holomorphic inside `C_m` and

    (1/(2 pi i)) integral_(C_m) G_(M,N)^-(s) ds=0              (1.2)

for every `M,N` and every source.  If these germs converged locally uniformly on `C_m` and its interior punctured
at `s_m` to `zeta W_epsilon^0`, Cauchy's formula would give

    zeta(s_m)K_F(2m+1/2)=0.                                   (1.3)

Thus the claimed topology already contains the desired moment annihilation.  Finite holomorphy does not prove
that topology.

### Case B: the Gamma factor is inserted

By R161_025,

    Res_(s=s_m)[zeta(s)d_Gamma(s)K_F(s-1/2)]
      =zeta(s_m)K_F(2m+1/2).                                  (1.4)

All other finite pieces have zero residue.  Hence every correctly completed finite germ already has contour
observation (1.4), independently of `M,N`.  Requiring its weighted square to tend to zero is exactly requiring
`D_T^pole(F)=0`; no finite limiting mechanism has been constructed.

## 2. Verdict on OAL

The oriented annihilation law proposed in R161_066 is not a new source law as written:

- without Gamma it moves the theorem into an unjustified locally uniform convergence across the pole;
- with Gamma it states the faithful moment energy itself is zero.

Therefore OAL(4.1) is withdrawn as a candidate derivation.  The contour realization (R161_066(3.3)) remains a
correct coordinate for the Gamma energy, but not its annihilation.

## 3. What kind of input could still be new

A genuine input cannot be a linear germ or a contour limit.  It must compare two finite **quadratic** quantities
whose difference has a Gamma-pole energy as an explicitly computed remainder.  Schematically it must have the
form

    Q_(M,N,T)^out(F)-Q_(M,N,T)^in(F)
      =sum_(m<=L) omega_m |K_F(2m+1/2)|^2+R_(M,N,L,T)(F),       (3.1)

where

1. first-contact radicality proves the left side is nonpositive or zero;
2. the right side is nonnegative;
3. `R` has a proved nonnegative sign or tends to zero uniformly before `L -> infinity`;
4. neither `Q^out` nor `Q^in` is defined using the desired moments.

This is exactly the extra equality-state inequality missing from the corpus.  R161_026 identifies the infinite
right side as the negative displacement derivative of the Gamma-Hankel norm, but no reverse displacement law is
currently proved.

## 4. Status

- finite-germ dichotomy (1.2)/(1.4): **proved**;
- OAL as a new annihilation mechanism: **withdrawn / circular or topologically equivalent to the target**;
- contour representation of the faithful pole energy: **still valid**;
- independent quadratic comparison law (3.1): **open**;
- D: **open**.
