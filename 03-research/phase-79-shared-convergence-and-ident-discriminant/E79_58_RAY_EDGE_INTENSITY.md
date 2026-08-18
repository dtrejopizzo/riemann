# E79.58 - The modal-ray amplitude is not controlled by crude edge size, but it does respond to edge intensity

**Scope:** `GAP-Z` only, first comparison between the scalar modal-ray amplitude
and primitive shell observables of the common cloud.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** `rho_N` is not
explained by coarse edge size statistics such as total common mass, active width,
or effective width. The strongest audited signal is instead an anticorrelation
with the average `N^2`-scaled shell intensity on the active edge.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only primitive shell observables already audited earlier.
E72.16/E77.7az: respected. This is a diagnostic reduction, not a forcing step.
Circularity: respected. No new endpoint identity enters.
```

## 1. Why this comparison matters

E79.57 showed that `rho_N` is not just the packet residual under another name.
So the next candid question is whether it is controlled by more primitive edge
data from the common cloud itself:

```text
mass,
width,
peak shell size,
or average shell intensity on the active edge.                           (58-1)
```

If one of those wins clearly, the amplitude front stops being mysterious.

## 2. Probe

Companion files:

```text
E79_58_RAY_EDGE_INTENSITY_probe.py
E79_58_ray_edge_intensity_results.json
```

On the audited zeta ladder `N=8,10,12,14,16`, the probe compares `|rho_N|` from
E79.56 against primitive sigma=`1.0` edge observables from E79.3f/E79.3g/E79.3i:

```text
- total common mass;
- the first few terminal shell sizes (N^2-scaled);
- N|ZERO^common|;
- raw active width m90 and m90/N;
- average N^2 shell size on the 90% edge;
- peak N^2 shell size;
- effective width and effective width / N.                               (58-2)
```

## 3. Result

The coarse size variables do **not** explain `rho_N`.

Representative correlations with `|rho_N|` are:

```text
common_total            ~  0.11
edge0_N2                ~  0.09
edge1_N2                ~  0.28
effective_width         ~ -0.34
m90                     ~ -0.23
m90/N                   ~  0.22.                                         (58-3)
```

So neither total common mass nor raw/effective edge width gives a convincing
control law for the modal amplitude.

The strongest audited signal is different:

```text
corr(|rho_N|, avg_N2_shell on the 90% edge) ~ -0.85.                     (58-4)
```

There is also a weaker but still visible anticorrelation with the peak shell
size:

```text
corr(|rho_N|, peak_N2_shell) ~ -0.54.                                    (58-5)
```

So the amplitude is responding more to how intense the active edge is, shell by
shell, than to how wide that edge is.

## 4. Reading

This is the first primitive localization of `rho_N`.

The modal-ray amplitude is not a count or width statistic. It reacts to an
intensity statistic:

```text
larger average N^2 shell intensity on the active edge
  -> smaller |rho_N|, on the audited zeta ladder.                        (58-6)
```

That does not yet prove a law, but it changes the search space materially. The
next candidate should be a signed or weighted shell moment built from edge
intensities, not another width or packet-size scalar.

## 5. Consequence

After E79.58, the next admissible target is sharper:

```text
test whether rho_N is controlled by a signed edge-intensity moment,
or by a normalization of the edge profile that keeps intensity and discards
raw width.                                                               (58-7)
```

In particular, revisiting crude edge width or total mass as if they were the
missing scalar law would now be wasted motion.

## 6. Status

```text
proved by probe:
  the modal-ray amplitude rho_N is not controlled by crude edge size
  observables, but shows its strongest audited link to the average N^2 shell
  intensity on the active edge;

reduced:
  the next scalar-law search from width/mass variables to intensity-based edge
  observables;

open:
  identify the signed or weighted edge-intensity moment behind rho_N;

next:
  audit signed edge moments on the active edge and test whether they stabilize
  rho_N better than the unsigned intensity average.
```
