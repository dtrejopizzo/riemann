# E79.57 - The modal-ray amplitude is not just the first-packet geometry renamed

**Scope:** `GAP-Z` only, comparison between the new scalar ray amplitude and the
terminal packet diagnostics already isolated earlier in the phase.  
**Class:** AUTOPSIA FRANCA.  
**What we know after this document that we did not know before:** the scalar
amplitude `rho_N` from E79.56 is related to packet quality in a weak statistical
way, but it is not directly identifiable with the first packet mismatch or with
the sparse packet / extra-root residue. So the modal-ray front and the terminal
packet front are adjacent, not yet unified.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only previously audited finite diagnostics.
E72.16/E77.7az: respected. This is a bookkeeping comparison, not a forcing step.
Circularity: respected. No new endpoint identity enters.
```

## 1. Why compare these objects

After E79.56 the live burden on the sigma-template side is the scalar amplitude
`rho_N` along the fixed modal ray. But phase 79 already had another sharp finite
object: the terminal packet / extra-root geometry from E79.43-E79.45 and
E79.3m-3w.

So the natural question is:

```text
is rho_N really new,
or is it just a repackaging of packet quality / packet residue?            (57-1)
```

If the answer were yes, two threads of the phase would merge at once.

## 2. Probe

Companion files:

```text
E79_57_RAY_PACKET_DECOUPLING_probe.py
E79_57_ray_packet_decoupling_results.json
```

For each zeta row on the audited ladder the probe compares `|rho_N|` against:

```text
- the mean multisigma first-packet mismatch from E79.44;
- the sigma=1 first-packet mismatch;
- the sparse packet residue |packet-extra| from E79.3w;
- its normalized mismatch and its N^2-scaled version.                     (57-2)
```

## 3. Result

There is some moderate anticorrelation, but no identification.

Numerically, with only five audited rows,

```text
corr(|rho_N|, first-packet mean mismatch)     ~ -0.61
corr(|rho_N|, first-packet mismatch at sigma=1) ~ -0.63
corr(|rho_N|, sparse |packet-extra|)          ~ -0.77
corr(|rho_N|, sparse normalized mismatch)     ~ -0.67.                   (57-3)
```

So larger `|rho_N|` often accompanies better packet matching. But the rowwise
data immediately show this is not an equality in disguise:

```text
N=10:  |rho_N| is the largest audited value, while the first packet is best;
N=14:  |rho_N| is also large, but the packet mismatch is back at the ordinary
       2e-2 scale rather than exceptional;
N=12,16: sparse-packet residues are much worse, without a matching blow-up in
         |rho_N| itself.                                                  (57-4)
```

So `rho_N` does not track packet residue shell-by-shell or row-by-row in the way
an actual identification would require.

## 4. Reading

This is a useful decoupling result.

The terminal packet front and the modal-ray front are clearly not unrelated:
they both live in the same zeta-side residual anatomy, and they do move in
compatible directions on part of the audited ladder. But they are not the same
finite statistic.

More candidly:

```text
packet geometry controls part of the residual burden,
modal-ray amplitude controls another part,
and neither one currently subsumes the other.                              (57-5)
```

That is exactly the kind of distinction phase 79 needs to keep clean.

## 5. Consequence

After E79.57, the right next move is not to collapse `rho_N` into packet
quality by fiat. The next admissible target is sharper:

```text
either relate rho_N to a more intrinsic terminal observable than packet error,
or treat it as an independent scalar transport variable and search for its own
law directly.                                                             (57-6)
```

In particular, the obvious packet mismatch scalars are now audited and should
not be revisited as if they solved `rho_N`.

## 6. Status

```text
proved by probe:
  the scalar modal-ray amplitude rho_N is not directly identifiable with the
  first-packet mismatch or sparse-packet / extra-root residue;

observed:
  there is moderate anticorrelation, so the two fronts are adjacent but not the
  same object;

reduced:
  the risk of merging the modal-ray front and the terminal-packet front without
  evidence;

open:
  identify the intrinsic transport law for rho_N itself, or the deeper
  observable that controls it;

next:
  test rho_N against direct shell-profile observables of the common cloud,
  rather than against already-compressed packet mismatch scalars.
```
