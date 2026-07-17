# E73.009 - Coefficient-law audit

## 1. Purpose

E73.008 asks for explicit coefficients in the structured primitive identity.  A first test extracted
least-squares coefficients in the `RAT-DD_2` basis.

## 2. Result

The image residual is small, but the individual least-squares coefficients are not stable across
`L`.  The dominant coefficient labels move, and normalized coefficient vectors have low cosine
similarity between consecutive windows.

Thus:

```text
the current RAT-DD basis is numerically redundant;
least-squares coefficients are not a canonical proof object.
```

## 3. Consequence

The next proof should not try to guess a coefficient law from the raw least-squares vector.  The
stable object is the subspace image:

```text
Image((C_E-mu I) RAT-DD_p).
```

The finite certificate should be formulated by canonical projection or by an orthogonalized basis,
not by raw coefficients.

## 4. Status

```text
observed: coefficient extraction is ill-conditioned;
redirect: use subspace-angle / orthogonal projection certificates for IMAGE-ID.
```

