# E77.7h - Feshbach Ritz envelope

**Run:** 2026-07-18.

## 1. Purpose

E77.7h first pass named the missing denominator:

```text
FESHBACH-RITZ-ENVELOPE:
0 <= mu_R-mu_L <= eta_R
```

with the complement coercivity kept explicit.  This note computes the exact
finite Feshbach equation and records the corrected object.

The main correction is:

```text
the useful denominator is not min spec(K_R)-mu_R.
It is the weighted self-energy of the Ritz coupling vector.
```

No closure of `RITZ-BRACKET`, `BTG-DIV-L`, `LP`, or `Omega7` is claimed.

## 2. Exact finite Feshbach equation

Fix a reference section `P_R H_L P_R`.  Let

```text
mu_R=lambda_min(P_R H_L P_R),
v_R=normalized Ritz ground vector.
```

Inside a larger centered finite section `P_M`, decompose

```text
P_M l2 = span{v_R} direct_sum W_RM.
```

In this basis,

```text
P_M H_L P_M =
[[mu_R, h_RM^*],
 [h_RM, K_RM  ]].
```

If `lambda_M=lambda_min(P_M H_L P_M)` and
`lambda_M < inf spec(K_RM)`, the Schur/Feshbach equation is exact:

```text
mu_R-lambda_M
= <h_RM,(K_RM-lambda_M)^(-1)h_RM>.            (F-1)
```

Equivalently, writing

```text
delta_RM=mu_R-lambda_M,
kappa_l=omega_l-mu_R,
c_l=<w_l,h_RM>,
```

for the eigenpairs of `K_RM`,

```text
delta_RM =
sum_l |c_l|^2/(kappa_l+delta_RM).             (F-2)
```

This is an identity, not a bound and not a positivity argument over Weil
data.  It is a scalar Schur complement for one finite self-adjoint matrix.

## 3. Certified envelope implication

The proof-facing version must be infinite and one-sided.  The admissible
target is:

```text
WEIGHTED-FESHBACH-ENVELOPE:
Find eta_R -> 0 and a certified spectral measure alpha_R of the Ritz
coupling vector h_R for the complement K_R such that

1. K_R-(mu_R-eta_R) is positive on the h_R-cyclic support;
2. int (t-mu_R+eta_R)^(-1) d alpha_R(t) <= eta_R.
```

Then the scalar Feshbach monotonicity gives

```text
mu_R-eta_R <= mu_L <= mu_R.                   (F-3)
```

Combining `(F-3)` with the bracketed low-mode lower sum of E77.7h gives:

```text
WEIGHTED-FESHBACH-ENVELOPE
 + bracketed low-mode divergence
=> BRACKETED-LOW-MODE-BTG
=> LOW-MODE-BTG(K)
=> BTG-DIV-L
=> fixed-mu block growth
=> corrected Weyl-disk contraction.           (F-4)
```

This is the required admissibility chain.  The object is smaller than
`RITZ-BRACKET` because it names the only measure that matters: the spectral
measure of the actual coupling vector, not the full complement spectrum.

## 4. Why crude complement coercivity fails

The tempting condition

```text
K_R-mu_R >= kappa_R I,  kappa_R>0
```

is false or useless.

For zeta in the measured windows, the finite complement minimum lies below
`mu_R` by almost exactly the same scale as `mu_R-lambda_M`; thus positive
coercivity at `mu_R` is unavailable.  For the planted build, the complement
is positive after `R=10`, but the crude gap envelope is still one or two
orders of magnitude larger than the actual shift.

The reason is visible in `(F-2)`: the dangerous low complement modes need
not carry the coupling mass.  Replacing the weighted self-energy by
`||h||^2/dist(E,spec K)` erases the only useful structure.

This is not P76.061's ambient bordered inverse wall.  It is the scalar
version of the same lesson: pair with the actual source before bounding.

## 5. Probe

Companion:

```text
E77_7h_feshbach_envelope_probe.py
E77_7h_feshbach_envelope_results.json
```

Command:

```bash
python3 E77_7h_feshbach_envelope_probe.py \
  --lambda 6 --max-modes 18 --refs 8,10,12,14,16 --top-k 6 --dps 70
```

The probe constructs the orthogonal decomposition
`span{v_R} direct_sum W_RM`, diagonalizes the complement, and checks `(F-2)`.

### Zeta

| R | delta=mu_R-mu_18 | eta weighted | kmin-mu_R | crude gap eta | Feshbach defect |
|---:|---:|---:|---:|---:|---:|
| 8  | 3.6786e-28 | 3.6786e-28 | -3.6786e-28 | inf | 1.19e-73 |
| 10 | 8.9295e-33 | 8.9295e-33 | -8.9295e-33 | inf | 2.08e-73 |
| 12 | 2.4032e-37 | 2.4032e-37 | -2.4032e-37 | inf | 1.12e-73 |
| 14 | 1.7090e-41 | 1.7090e-41 | -1.7090e-41 | inf | 1.09e-72 |
| 16 | 1.5411e-45 | 1.5411e-45 | -1.1568e-45 | inf | 6.50e-73 |

The exact weighted equation reproduces the finite Ritz shift.  The crude
positive-gap condition is refuted in every zeta row.

Dominant self-energy contributors are not simply the minimum-gap modes.  At
`R=16`, for example, the largest contributor has

```text
kappa ~= 4.98e-38,
|c| ~= 8.23e-42,
fraction ~= .882.
```

while the minimum complement undershoot is `-1.16e-45`.

### Planted build

| R | delta=mu_R-mu_18 | eta weighted | kmin-mu_R | crude gap eta | Feshbach defect |
|---:|---:|---:|---:|---:|---:|
| 8  | 1.0243 | 1.0243 | -0.9227 | inf | 0 |
| 10 | 1.0071e-1 | 1.0071e-1 | 8.8453e-4 | 5.1593e-1 | 1.69e-70 |
| 12 | 3.5234e-2 | 3.5234e-2 | 6.6358e-2 | 2.5738e-1 | 1.01e-70 |
| 14 | 2.0548e-2 | 2.0548e-2 | 8.1044e-2 | 1.9035e-1 | 2.16e-70 |
| 16 | 4.6750e-3 | 4.6750e-3 | 9.6917e-2 | 6.5025e-2 | 1.21e-70 |

The plant again passes the algebraic/Feshbach front.  It is not filtered out
by `A`; its expected failure remains in `B`/IDENT or in later radical tails.

## 6. Autopsy and next object

`FESHBACH-RITZ-ENVELOPE` is not closed as an infinite theorem.  The finite
identity is exact, but a proof still needs a certified envelope for the
coupling spectral measure:

```text
alpha_R = sum_l |<w_l,h_R>|^2 delta_{omega_l}.
```

The next strictly smaller live object is:

```text
WFE-CYCLIC-TAIL:
Construct, from the D+B realization and the exact cell/Hilbert entries, a
certified majorant alpha_R^# for alpha_R such that the fixed point

eta = int (t-mu_R+eta)^(-1) d alpha_R^#(t)

has a solution eta_R -> 0 on a cofinal R=R(N), and this eta_R is small
en the E77.7h bracketed-low-mode denominator.
```

Then

```text
WFE-CYCLIC-TAIL
=> WEIGHTED-FESHBACH-ENVELOPE
=> RITZ-BRACKET
=> BRACKETED-LOW-MODE-BTG
=> BTG-DIV-L
=> corrected LP.
```

This remains a convergence/identity target.  It is not a sign theorem, not a
zero filter, and not an ambient inverse estimate.

## 7. Status

```text
proved:    exact finite Feshbach identity (F-1)/(F-2);
proved:    WEIGHTED-FESHBACH-ENVELOPE plus bracketed low-mode divergence
           implies BTG-DIV-L and corrected Weyl-disk contraction;
refuted:   positive complement gap at mu_R as a zeta proof premise;
refuted:   crude ||h||^2/gap envelope as BTG-scale certificate;
observed:  zeta weighted eta equals finite Ritz shift to ~1e-72 defect;
observed:  planted weighted eta equals finite Ritz shift to ~1e-70 defect;
observed:  front remains falsifier-neutral;
open:      infinite weighted self-energy majorant;
open:      RITZ-BRACKET, BRACKETED-LOW-MODE-BTG, BTG-DIV-L, corrected LP;
live:      WFE-CYCLIC-TAIL.
```

