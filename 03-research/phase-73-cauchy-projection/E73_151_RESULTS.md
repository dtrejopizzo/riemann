# E73.151 Results - Forced Row Spectral Profile

Date: 2026-07-12.

Script:

```text
E73_151_forced_row_spectral_profile.py
```

Purpose:

Decompose forced signed rows into spectral bands of

```text
E=H-mu I.
```

Bands:

```text
null,
tiny <= L^-8,
small L^-8..L^-4,
mid L^-4..L^-1,
bulk > L^-1.
```

Representative output:

```text
 lam     L gamma row    nullB   tinyB  smallB    midB   bulkB status
  16   5.545   14.13   0  -17.832 -10.638  -6.158  -3.670   0.593 PASS
  20   5.991   21.02   0  -18.703  -8.299  -5.763  -1.886   1.695 PASS
  24   6.356   25.01   0  -18.790 -10.566  -5.213  -3.394   0.732 PASS
  28   6.664   14.13   0  -16.536  -9.262  -3.713  -1.525   2.599 FAIL
  32   6.931   14.13   0  -16.812 -10.731  -6.493  -2.891   0.663 FAIL
  32   6.931   14.13   1  -17.388 -10.731  -6.493  -2.891   0.663 PASS
```

## Reading

The forced rows are not small in bulk.  Their bulk mass is polynomial.
The desired estimate is entirely about suppressing the null spectral
coefficient.

Near-null complement mass exists, typically around:

```text
tiny ~= L^-8 to L^-12,
small ~= L^-4 to L^-7.
```

This explains why the full pseudoinverse is the wrong proof object: those
near-null complement bands are harmless for rowspace distance but expensive
for `E^+`.

## Consequence

The next exact statement should be a spectral-cutoff version of SFRL:

```text
forced row = bulk rowspace + near-null complement tail + alpha xi^*,
|alpha| <= C L^-17.
```

The analytic theorem must bound `alpha` directly.  It need not invert the
near-null complement.

This is compatible with the earlier cofactor audits: adjugate/pseudoinverse
certificates are useful for finite verification, but not by themselves a
source of the cancellation.
