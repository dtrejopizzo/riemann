# R161_034 — Exact Mellin Gram: the missing interference is the product--ratio channel

## 0. Verdict

The cross-`k` term isolated in `R161_033` can be diagonalized exactly. In Mellin frequency every labelled Poisson
atom is a scalar reflection multiplier. Its Gram splits into two equal-orientation terms depending on `k/l` and
two opposite-orientation terms depending on `kl`. These are precisely the ratio and product channels isolated in
phase 106.

Consequently an unqualified claim that the polar/Tate endpoint simply cancels the cross Gram would return to the
old triangle-current problem. A surviving phase-161 completion must use the first-contact boundary compression:
it must show that the *compressed* ratio channel is the boundary concomitant (or a positive leakage square), not
attempt a translation-invariant full-line cancellation.

## 1. Mellin symbols of the oriented atoms

Put `s=1/2+i tau` and use the reflection-multiplier convention of `R161_003`,

```
(Fcal f)^hat(tau)=u_infty(tau) fhat(-tau),
(Jf)^hat(tau)=fhat(-tau),
|u_infty(tau)|=1.                                        (1.1)
```

For the half-density-normalized atom

```
d_k=k^(-1/2)(tau_(log k)Fcal-Jtau_(log k)),              (1.2)
```

one has

```
(d_kf)^hat(tau)=q_k(tau)fhat(-tau),
q_k(tau)=k^(-s)u_infty(tau)-k^(-(1-s)).                  (1.3)
```

This is the one-atom summand of the finite Poisson multiplier
`D_N(s)u_infty(tau)-D_N(1-s)`.

## 2. Coherent and labelled energies

Let `a_k=log k`. Plancherel gives

```
||sum_(k<=N)a_kd_kf||^2
 =integral |sum_(k<=N)a_kq_k(tau)|^2 |fhat(-tau)|^2 dtau, (2.1)
```

whereas the labelled second moment is

```
sum_(k<=N)a_k^2||d_kf||^2
 =integral sum_(k<=N)a_k^2|q_k(tau)|^2
          |fhat(-tau)|^2 dtau.                            (2.2)
```

Their exact difference is

```
I_N(f)=integral sum_(k!=l)a_ka_l q_k(tau)conj(q_l(tau))
                   |fhat(-tau)|^2 dtau.                    (2.3)
```

No limiting or support argument has been used.

## 3. Product--ratio expansion

Using `|u_infty|=1`, direct expansion gives

```
q_k conj(q_l)
 = (kl)^(-1/2)[
      exp(-i tau log(k/l))
     +exp(+i tau log(k/l))
     -u_infty(tau) exp(-i tau log(kl))
     -conj(u_infty(tau)) exp(+i tau log(kl))
   ].                                                        (3.1)
```

Thus

```
Re(q_k conj(q_l))
 =2(kl)^(-1/2)[
      cos(tau log(k/l))
     -Re{u_infty(tau)exp(-i tau log(kl))}
   ].                                                        (3.2)
```

The first term is the equal-orientation **ratio channel**; the second is the opposite-orientation Fourier
**product channel**. This is the same product--ratio split proved geometrically in
`106_50_TRIANGLE_VARIANCE_AND_PRODUCT_RATIO_SPLIT.md`.

The sum--product construction controls the product coefficient through Dirichlet convolution. It does not group
the ratio term by `Lambda*1=log`.

## 4. Why full-line polar cancellation cannot be asserted

The polar counterterm is a single continuum family parametrized by the cutoff, and the Tate block has rank two
after window compression. Equation (3.2), before compression, contains all ratios `k/l`. There is no coefficientwise
identity which turns those distinct frequencies into a rank-two endpoint term.

This does not rule out a first-contact identity: compression destroys translation invariance and converts
translations into collars. It does rule out deriving the needed cancellation solely in the full-line multiplier
algebra.

## 5. Correct terminal localization

Let `P=P_T`. The object which can still be new is not (2.3) on the full line but the compression commutator

```
[P,d_k]=Pd_k-d_kP.                                           (5.1)
```

For a window-supported source, every failure of the full-line Gram calculation to commute with `P` is an exterior
collar. Therefore the admissible Green completion must be expressed as the exact identity

```
P(sum_k a_kd_k)^*(I-P)(sum_l a_ld_l)P
```

plus its polar continuum analogue. This is already a positive leakage square. Expanding it retains both the ratio
and product cross terms with their correct signs, while localizing them at the physical boundary.

Accordingly the next candidate is the **coherent compressed leakage**, not the diagonal direct-sum energy:

```
L_(N,T)(F)=||(I-P)sum_(k<=N)(log k)d_kPF||^2>=0.          (5.2)
```

The required finite theorem is to identify the polar-renormalized limit of (5.2), including its crossed Tate
endpoint, with the scattering leakage of `R161_020`, and to show that first contact saturates the corresponding
compression norm. Unlike the direct-sum lift, (5.2) belongs to the original coherent `(PC-ren)` Hilbert space.

## 6. Relation to the earlier no-go

Phase 106 retained the full ratio channel but lacked the first-contact exterior compression and encountered the
wrong coherence direction. Phase 161 can differ only at (5.1): the additive Fourier transform, support projection,
and polar layer must be kept together before the norm. Dropping `[P,d_k]` returns exactly to the phase-106
star/triangle variance.

## 7. Status

- Mellin symbol of every oriented atom: **PROVED**;
- exact coherent/direct-sum Gram difference: **PROVED**;
- product--ratio decomposition: **PROVED**;
- collision of the uncompressed Gram route with phase 106: **IDENTIFIED**;
- coherent compressed leakage (5.2): **CANONICAL POSITIVE CANDIDATE**;
- its polar-renormalized identification with physical scattering leakage: **OPEN**;
- first-contact saturation of that leakage: **OPEN / TERMINAL**;
- row D: **OPEN**.
