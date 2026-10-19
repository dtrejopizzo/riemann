# R161_014 — Sonin--Gamma coercivity and the final quadratic gate

## 0. Verdict

Once the correctly typed scattering places the product port in a cosine parity sector, the apparently indefinite
Gamma operator becomes strictly positive for purely geometric reasons.  If `g` is supported to the right of `T>0`
and `C_log g=sigma g`, then

```
<D_Gamma g,g>=2<Qg,g>
                >=2T||g||^2.                                    (0.1)
```

This converts the remaining range problem into one scalar, oriented quadratic identity.  To close D it is enough
to prove that a first-contact product port satisfies

```
<D_Gamma g,g>-2T||g||^2<=0.                                     (0.2)
```

The left side is already nonnegative and is zero only for `g=0`.  The missing step is therefore not positivity of
an unknown graph: it is an upper/null balance for one explicitly constructed sum--product port.

## 1. Domain of the product port

Let `g=g_(T,+)^0(F)` be the corrected port and `G(i tau)` its boundary transform.  The phase-121 radical satisfies
`F in H^s` for every `s<1/2`.  Choose `1/4+eta<s<1/2`.  The estimates used in `R161_008` also apply after one
`z`-derivative:

```
G'(i tau) in L2(d tau).                                          (1.1)
```

Indeed, differentiating `-zeta'K_F-zeta Q_+` introduces `zeta''`, `K_F'`, `zeta'`, and `Q_+'`.  Cauchy estimates
give the same convexity power `1/4+eta` with logarithms, while multiplication of the compact source by `t`
preserves `H^s`.  The polar correction is Schwartz on the boundary after removal of the pole.

By Plancherel, (1.1) gives

```
Qg=tg in L2(R).                                                   (1.2)
```

Thus all quadratic pairings below are ordinary Hilbert-space pairings, not formal distributions.

## 2. Coercivity theorem

Let `C_log` be the additive cosine transform in logarithmic coordinates.  It is a selfadjoint unitary and phase 116
proves

```
D_Gamma=Q+C_log Q C_log.                                         (2.1)
```

**Theorem 2.1 (Sonin--Gamma coercivity; PROVED).** Suppose

```
g in Dom(Q),
supp g subset [T,infinity),
C_log g=sigma g,       sigma in {+1,-1}.                          (2.2)
```

Then

```
<D_Gamma g,g>
 =2 integral_T^infinity t|g(t)|^2dt
 =2T||g||^2+2 integral_T^infinity (t-T)|g(t)|^2dt.                (2.3)
```

In particular

```
<D_Gamma g,g>-2T||g||^2>=0,                                     (2.4)
```

and equality holds only for `g=0` in `L2`.

*Proof.* Selfadjoint unitarity gives

```
<C_log Q C_log g,g>=<Q C_log g,C_log g>=<Q(sigma g),sigma g>
                   =<Qg,g>.
```

Insert (2.1), then use the support in (2.2).  The last integral in (2.3) is nonnegative.  If it vanishes, `g` is
supported on the measure-zero set `{T}`, so its `L2` class is zero. ∎

The conclusion is independent of the sign `sigma`; no positivity of row D was used.

## 3. Application to the product port

The typed scattering equation of `R161_011`, once its physical boundary passage is completed, and parity of `F`
give

```
C_log g=sigma_epsilon g.                                         (3.1)
```

The Hardy construction gives `supp g subset[T,infinity)`, and Section 1 supplies the domain.  Hence Theorem 2.1
applies.

**Corollary 3.1 (quadratic closure criterion; PROVED CONDITIONALLY).** Row D follows if every primitive
first-contact port obeys either

```
<D_Gamma g,g><=2T||g||^2,                                        (3.2)
```

or the stronger null identity `<D_Gamma g,g>=0`.

*Proof.* Equations (2.3) and (3.2) force `g=0`.  The critical-jet identity then gives
`zeta'(rho)K_F(rho-1/2)=0` at every simple critical zero.  Cartwright rigidity gives `F=0`, contradicting first
contact. ∎

## 4. Why scalar commutation is insufficient

The strong equality `[Z,D_Gamma]F=0` supplies (3.1) after the oriented port construction, but it does not imply
(3.2).  A nonzero cosine-eigen Sonin function satisfies the same scattering conservation and has strictly positive
left side in (2.4).  Therefore the upper balance must come from the finite Poisson--Chebyshev anomaly or the exact
endpoint transmission, not from commuting Fourier multipliers.

This prevents a circular shortcut: replacing (3.2) by positivity of the full two-contour graph simply reinstates
G40.

## 5. The exact sum--product target

Define the explicit excess energy

```
E_T^PC(F)
 :=<D_Gamma g_(T,+)^0(F),g_(T,+)^0(F)>
   -2T||g_(T,+)^0(F)||^2
 =2||(Q-T)^(1/2)g_(T,+)^0(F)||^2.                                (5.1)
```

Theorem 2.1 proves `E_T^PC(F)>=0` once the typed physical scattering identity places the port in the stated Sonin
sector; that boundary passage remains part of the phase-161 construction.  The sole subsequent quadratic target is

```
P_TA_TF=0  ==>  E_T^PC(F)<=0.                                   (5.2)
```

To be admissible, a proof of (5.2) must expand the mixed, oriented finite identity `(PC)` before taking limits and
retain the crossed Gamma/Tate boundary term.  A norm square of `A_TF` is forbidden by the sign-blindness theorem of
`R161_002`.

In the first chamber, `R161_013` shows that the endpoint contribution entering this balance is the explicit
`2,3,4` field and that its only nonlocal partner is `C_log Q C_log F`.  Thus (5.2), rather than a general Sonin
classification, is the next concrete calculation.

## 6. Status

- one-derivative domain of the product port: **PROVED from the phase-121 `H^s` estimate**;
- Sonin--Gamma coercivity (2.3): **PROVED for every typed Sonin port**;
- placement of the product port in that physical sector: **OPEN boundary passage from `R161_011`**;
- reduction of closure to the upper/null balance (5.2): **PROVED**;
- derivation of (5.2) from `(PC)` and first contact: **OPEN**;
- row D: **OPEN**.
