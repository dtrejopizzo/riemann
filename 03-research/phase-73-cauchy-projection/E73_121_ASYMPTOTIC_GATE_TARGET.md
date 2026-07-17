# E73.121 - Asymptotic Gate Target after the Finite Manifest

Date: 2026-07-12.

E73.120 gives a finite machine-checkable gate for the declared scale boxes.
It does not prove the uniform theorem.  The remaining target is now precise:

```text
Asymptotic Standard-Box Theorem.
There exists L0 <= L_24 and constants C_LOCK,C_TAIL,C_OUT,C_MAIN
such that every natural-height standard box B(L) satisfies

LOCK^+(B,L) <= C_LOCK L^-5,
TAIL^+(B,L) <= C_TAIL L^-5,
OUT^+(B,L)  <= C_OUT  L^-9,
MAIN^+(B,L) <= C_MAIN < 1

for all L>=L0.
```

Here `L_24=2 log(24)`.

## 1. Why this is the right theorem

After E73.117--E73.120:

```text
lambda=16 is a finite low-scale base case;
lambda=20 is a finite transition cover;
lambda=24,28 wide standard boxes pass with slack.
```

The local and selection issues are no longer open:

```text
NLC/Gloc are exact by nearest-zero cell enumeration;
OUT is a compatible-FAR-triple maximum;
MAIN is a possible-set box certificate;
LOCK at low scale has an exact local base replacement.
```

Thus the only remaining uniform burden is an asymptotic majorant for the
standard-box quantities.

## 2. Candidate majorant structure

The verified standard-box quantities have the form

```text
S_FAR^+(B,L)             [three-row FAR envelope],
NLC^+(B,L)               [finite local Cauchy/root lock],
Gloc^+(B,L)              [finite local nodal tail],
OUT^+(B,L)               [finite complement after FAR triple],
MAIN^+(B,L)              [weighted Cauchy rational main].
```

The target factorization is:

```text
S_FAR^+(B,L) <= C_F L^-a,
NLC^+(B,L)   <= C_N L^-b,
Gloc^+(B,L)  <= C_G L^-c,
OUT^+(B,L)   <= C_O L^-9,
MAIN^+(B,L)  <= C_M < 1,
```

with

```text
a+b >= 5,
a+c+2 >= 5 + 2m_M,
```

where `M ~ m_M L` is the active Fourier cutoff entering `TAIL`.

Empirically the wide-box verifier gives:

```text
lambda=24:
LOCK <= L^-8.699,  TAIL <= L^-10.725, OUT <= L^-13.590, MAIN <= 0.2542

lambda=28:
LOCK <= L^-8.378,  TAIL <= L^-10.108, OUT <= L^-13.083, MAIN <= 0.2050
```

These margins suggest that the asymptotic theorem should not be tight.

## 3. The real analytic sublemma

E73.122 corrects the first version of this target.  The nearest-root
distance is not the stable quantity: it oscillates from very small to
order-one scale across the tested boxes.  The stable quantity is the
Cauchy small-value itself.

Thus the sublemma that would close the asymptotic theorem is a Cauchy
small-value majorant:

```text
CSV(L):
For every natural-height local window W and every row gamma in W,

|C_x(-gamma)| <= C_C L^-17.
```

Root-lock remains a useful explanation in rows where the nearest Cauchy
root is close, but it is not the uniform invariant.  The proof should
target `|C_x(-gamma)|` directly.

This is the only part still depending on the arithmetic spectral vector
`xi`.  Everything else is an elementary Hermite/mesh/enumeration envelope.

## 4. What to prove next

The next proof-oriented experiment should not add new gates.  It should
extract the exponents of the CRL quantities from the existing rows:

```text
|C_x(-gamma)|,
dist(-gamma, nearest root),
sup |C_x'|,
S_FAR^+,
NLC^+,
Gloc^+,
MAIN^+,
OUT^+,
```

for increasing `lambda`, and fit them against powers of `L` only as a guide
to the analytic inequalities.

The proof target is:

```text
CSV(L) + elementary Hermite envelopes => Asymptotic Standard-Box Theorem.
```

Together with E73.120 finite base/transition certification, this would
give:

```text
Uniform GATE-73
=> scalar WRL
=> Omega7
=> RH.
```
