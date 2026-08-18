# E79.85 - Residual balance already appears as near-symmetry of the finite cloud

**Scope:** `DISCRIMINANT`, continuation of the bridge opened in E79.84.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the
package-level residual balance from E79.84 is not merely an algebraic curiosity.
It is already visible in the finite `K_N` cloud through a two-part regime:

```text
one sharply separated farthest outlier
+ a low-defect approximately symmetric remaining cloud.                  (85-0)
```

The zeta ladder exhibits this regime stably. The planted off-line controls can
imitate one part of it on isolated rows, but not the conjunction.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / IDENT side only.
MW-3:  respected. No per-prime/local-to-global assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform gap hypothesis.
K1-K5: respected. Uses only the exact finite K_N spectra.
E72.16/E77.7az: respected. This is an IDENT-side discriminant reduction.
Circularity: respected. The cloud is read from K_N, independent of the target
  arithmetic derivative.
```

## 1. Why this is the next candid test

E79.84 reduced the bridge problem to a concrete finite object:

```text
small |c_N|
  -> near-perfect signed balance of the secular residues r_j = q_j x_j. (85-1)
```

The next unavoidable question is whether that balance is already reflected in
the geometry of the roots of the secular package, not only in the coefficients.

Phase 78 already told us the candid cloud picture:

```text
- zeta has one huge farthest outlier plus a near-symmetric cloud,
- the outlier is negligible for the transfer,
- the hard content lives in the cloud itself.                            (85-2)
```

So the right next audit is:

```text
after removing the single farthest outlier,
how symmetric is the remaining finite cloud under kappa -> -kappa?      (85-3)
```

## 2. Probe

Companion files:

```text
E79_85_cloud_symmetry_bridge_probe.py
E79_85_cloud_symmetry_bridge_results.json
```

On the audited `lambda=6`, `N=8,10,12`, `dps=60` ladder and the same three
builds as E79.84, the probe:

```text
1. builds spec(K_N),
2. removes the single farthest eigenvalue by |kappa|,
3. pairs the remaining positive and negative eigenvalues by increasing
   magnitude,
4. records the pair defect
     |p_j - n_j| / (p_j + n_j),                                         (85-4)
5. summarizes by the mean and max pair defect on the section.           (85-5)
```

It also records the ratio

```text
outlier_fraction = |kappa_max| / |kappa_second|,                        (85-6)
```

to confirm that one outlier is indeed sharply separated from the rest.

## 3. Result

The zeta cloud already exhibits a stable two-part geometry.

### Zeta

On the audited zeta ladder:

```text
N= 8: outlier_fraction ~ 13.89, mean_pair_defect ~ 0.0178,
N=10: outlier_fraction ~ 11.11, mean_pair_defect ~ 0.0178,
N=12: outlier_fraction ~ 11.83, mean_pair_defect ~ 0.0141.              (85-7)
```

So zeta shows both:

```text
1. one very large outlier separated from the cloud by a factor ~11-14,
2. an internal cloud whose paired `+-` defect stays around 1.4%-1.8%.   (85-8)
```

So the residual-balance regime of E79.84 is not merely coefficient-side. It is
already visible as a concrete geometric near-symmetry of the finite cloud.

### Planted off-line controls

The planted controls do not sustain that **same regime**.

For `gamma1 = 14.1347...`:

```text
N= 8: outlier_fraction ~ 1.23, mean_pair_defect ~ 0.131,
N=10: outlier_fraction ~ 1.57, mean_pair_defect ~ 0.0227,
N=12: outlier_fraction ~ 1.16, mean_pair_defect ~ 0.0119.              (85-9)
```

For `gamma2 = 21.0220...`:

```text
N= 8: outlier_fraction ~ 6.15, mean_pair_defect ~ 0.237,
N=10: outlier_fraction ~ 1.10, mean_pair_defect ~ 0.215,
N=12: outlier_fraction ~ 1.16, mean_pair_defect ~ 0.0158.              (85-10)
```

So the planted builds can hit one part of the picture on an isolated row:

```text
- a relatively small mean pair defect at one section, or
- a moderately enlarged outlier at one section,                          (85-11)
```

but they do not keep the **zeta conjunction**

```text
large outlier separation + low-defect symmetric remainder               (85-12)
```

across the audited ladder.

That is the candid discriminating content.

## 4. Reading

This is the first genuinely operational chain inside the discriminant front.

After E79.84 we had:

```text
small |c_N|
  -> residual balance
  -> ?                                                                   (85-9)
```

Now the `?` is no longer abstract. The next visible object is:

```text
one-outlier separation plus near-symmetry of the remaining finite cloud. (85-13)
```

That is exactly the kind of geometry that can feed E79.6:

```text
if the cloud is nearly symmetric, then the cumulative spectral-shift profile
M_N should be odd-like and M_N * x should become single-signed.          (85-14)
```

This is still not a theorem, but it is now a concrete finite route rather than
an interpretive slogan.

## 5. What this does and does not prove

This note does **not** yet prove:

```text
residual balance  =>  cloud symmetry  =>  M_N * x single-signed         (85-12)
residual balance  =>  cloud symmetry  =>  M_N * x single-signed         (85-15)
```

in theorem-grade form.

But it does reduce the gap one more time:

```text
the bridge from E79.84 survives direct contact with the root geometry.   (85-16)
```

So the live object is now much sharper than at the start of E79.83.

## 6. Consequence

After E79.85, the discriminant front is best read as:

```text
small |c_N|
  -> residual balance of r_j = q_j x_j
  -> one-outlier separation plus near-symmetry of the remaining cloud
  -> odd/coherent cumulative profile M_N
  -> M_N * x single-signed.                                             (85-17)
```

The last two arrows remain open, but the first three now have named finite
objects and numerical support.

So the next admissible move is to attack:

```text
cloud symmetry  =>  odd/coherent M_N,                                   (85-15)
cloud symmetry  =>  odd/coherent M_N,                                   (85-18)
```

which is already much closer to the actual spectral-shift object than the
packet-side branches were.

## 7. Status

```text
proved by audit:
  the zeta ladder exhibits a stable two-part regime:
  one sharply separated farthest outlier together with a low-defect
  approximately symmetric remaining cloud;

proved by audit:
  the planted off-line controls do not sustain that same conjunction across
  the audited ladder, even when one of its two parts appears on an isolated
  row;

clarified:
  the bridge from E79.84 survives on the root geometry side, not just on the
  residue side;

reduced:
  the live discriminant chain to
    (small |c_N|, residual balance, cloud symmetry regime, coherence);

open:
  prove that near-symmetry of the cloud forces the odd/coherent profile M_N;

next:
  attack the passage from paired cloud geometry to the sign structure of M_N.
```
