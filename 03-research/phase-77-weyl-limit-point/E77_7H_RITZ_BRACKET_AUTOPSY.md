# E77.7h - Ritz bracket and bracketed low-mode BTG

**Run:** 2026-07-18.

## 1. Purpose

E77.7g left the LP front at the scalar localization problem

```text
RITZ-BRACKET:
construct mu_R-eps_R <= mu_L <= mu_R on the inner-gap scale,
using H_L=D_L+B_L and no ambient inverse norm.
```

This note separates three statements:

```text
1. a true but coarse tail bracket from E77.7d;
2. the exact implication from a certified bracket to LOW-MODE-BTG;
3. the obstruction preventing the coarse bracket and naive Temple residual
   from closing BRACKETED-LOW-MODE-BTG.
```

No Omega7, LP, or BTG-DIV-L closure is claimed here.

## 2. Coarse tail Ritz bracket

Let `P_R` be the centered coordinate projection and

```text
mu_R=lambda_min(P_R H_L P_R).
```

E77.7d gives

```text
H_L=D_L+B_L,
D_L(n)->+infinity,
B_L bounded self-adjoint.
```

For the exterior projection `Q_R=I-P_R`, define certified constants

```text
C_L >= ||B_L||,
a_R <= inf spec(Q_R D_L Q_R)-C_L.
```

Then `Q_R H_L Q_R >= a_R Q_R` and
`||P_R H_L Q_R||=||P_R B_L Q_R|| <= C_L`.  For every normalized
`u=x+y`, `x=P_R u`, `y=Q_R u`,

```text
<u,H_L u>
 >= mu_R ||x||^2 + a_R ||y||^2 - 2 C_L ||x|| ||y||.
```

The right side is bounded below by the lower eigenvalue of

```text
[[mu_R, -C_L],
 [-C_L, a_R]].
```

Hence, whenever `a_R>mu_R`,

```text
mu_R-eps_R^tail <= mu_L <= mu_R,              (H-1)

eps_R^tail =
  (sqrt((a_R-mu_R)^2+4 C_L^2)-(a_R-mu_R))/2
 <= C_L^2/(a_R-mu_R).
```

Because `a_R->+infinity`, this proves a genuine bracket with
`eps_R^tail->0`.

This is useful bookkeeping, but it is not the E77.7g `RITZ-BRACKET`: its
scale is at best logarithmic in the tail threshold, while BTG needs control
at the low interlacing scale.

## 3. Bracket implies low-mode BTG

Let `(nu_j^(N),u_j^(N))` be the finite inner-block eigenpairs and let `b_N`
be the moving boundary column.  If

```text
mu_R-eps_R <= mu_L <= mu_R,
```

then for each finite `j`,

```text
|nu_j^(N)-mu_L| <= |nu_j^(N)-mu_R| + eps_R.
```

Therefore

```text
sum_{j<K} |<u_j^(N),b_N>|^2
          / (|nu_j^(N)-mu_R|+eps_R)^2 -> infinity

=> LOW-MODE-BTG(K)
=> BTG-DIV-L
=> fixed-mu block growth
=> corrected Weyl-disk contraction
=> CORRECTED-LP.                               (H-2)
```

This is the required admissibility implication.  A reduced bracketed target
is legitimate only if it supplies such an `eps_R` and verifies the divergent
lower sum in `(H-2)`.

## 4. Probe

Companion:

```text
E77_7h_ritz_bracket_probe.py
E77_7h_ritz_bracket_results.json
```

Command:

```bash
python3 E77_7h_ritz_bracket_probe.py \
  --lambda 6 --max-modes 18 --refs 8,10,12,14,16 --top-k 4 --dps 70
```

The probe rebuilds the zeta and planted matrices from multiprecision
integrals.  It audits:

```text
finite_B_norm_estimate;
tail_diag_min_inside_max_section - finite_B_norm_estimate;
coarse_global_bracket_epsilon;
ritz_tail_residual_norm;
directional_residual_epsilon_proxy;
temple_epsilon_proxy;
low-mode BTG denominators under the chosen finite reference.
```

The finite norm and finite tail quantities are diagnostics, not certified
infinite constants.  They measure scale compatibility.

### Zeta

| R | mu_R-mu_18 | eps_tail | eps_dir proxy | Temple proxy | gap0 to mu_R | log10 S_R(mu_R) |
|---:|---:|---:|---:|---:|---:|---:|
| 8  | 3.6786e-28 | inf | 4.3701e-15 | 3.1982e-4  | 1.1374e-25 | 13.061 |
| 10 | 8.9295e-33 | inf | 4.6122e-27 | 3.8653e-6  | 1.8416e-30 | 13.703 |
| 12 | 2.4032e-37 | inf | 1.5901e-37 | 2.7192e-9  | 4.2775e-35 | 21.226 |
| 14 | 1.7090e-41 | inf | 5.1294e-48 | 2.0981e-13 | 2.2450e-39 | 21.739 |
| 16 | 1.5411e-45 | inf | 4.6504e-60 | 8.1057e-19 | 1.5569e-43 | 23.710 |

The coarse tail bracket is not active in the measured finite window.  The
directional residual proxy can be tiny, but it is not a certified upper
bound: by `R=14` it is far below the observed finite delta to `mu_18`, so it
has dropped a missing denominator.

### Planted build

Standard plant:

```text
gamma=14.134725141734693790, beta=.30, strength=5.
```

| R | mu_R-mu_18 | eps_tail | eps_dir proxy | Temple proxy | gap0 to mu_R | log10 S_R(mu_R) |
|---:|---:|---:|---:|---:|---:|---:|
| 8  | 1.0243    | inf | inf        | inf       | 3.0910e-1 | 1.715 |
| 10 | 1.0071e-1 | inf | 1.7259e-1 | 1.4838    | 1.4693e-1 | 0.795 |
| 12 | 3.5234e-2 | inf | 4.9576e-2 | 5.7281e-1 | 9.6199e-3 | 2.447 |
| 14 | 2.0548e-2 | inf | 2.9964e-2 | 3.7762e-1 | 7.0786e-4 | 3.478 |
| 16 | 4.6750e-3 | inf | 5.0362e-3 | 9.2917e-2 | 4.4917e-3 | 2.343 |

The front remains falsifier-neutral in the intended sense: the same bracket
mechanisms apply to both builds, and the plant does not get excluded by a
sign, zero filter, or Weil-positivity surrogate.  It merely shows resonant
finite scales.

## 5. Autopsy

`RITZ-BRACKET` is not closed in E77.7h.

The failed denominator is exact.  A residual estimate for the padded Ritz
ground vector `v_R` has the schematic form

```text
mu_R-mu_L
 <= ||Q_R H_L P_R v_R||^2 / kappa_R,
```

but the required `kappa_R` is not the exterior diagonal tail alone.  It is
the Feshbach rest coercivity after removing the Ritz ground direction:

```text
kappa_R(E)
= inf spec of the complement block coupled from
   (P_R v_R)^perp plus Q_R, at energy E near mu_L.
```

If this `kappa_R` is replaced by the exterior tail only, the estimate ignores
coupling through the other low Ritz modes.  If it is replaced by the finite
second Ritz gap, the denominator is tiny and the Temple proxy is useless for
BTG scale.  This is why the zeta directional residual can look excellent
while still failing as a proof.

The obstruction is not the P76.061 ambient inverse norm.  It is a scalar
Feshbach/coercivity problem for the Ritz ground shift.

## 6. Smaller live object

The next admissible object is:

```text
FESHBACH-RITZ-ENVELOPE:
For a cofinal choice R=R(N), prove
0 <= mu_R-mu_L <= eta_R
by the scalar Feshbach equation for the Ritz ground direction, with the
orthogonal complement coercivity kappa_R(E) kept explicit, and with

sum_{j<K} |<u_j^(N),b_N>|^2
          / (|nu_j^(N)-mu_R|+eta_R)^2 -> infinity.
```

Then

```text
FESHBACH-RITZ-ENVELOPE
=> BRACKETED-LOW-MODE-BTG
=> LOW-MODE-BTG(K)
=> BTG-DIV-L
=> fixed-mu block growth
=> corrected Weyl-disk contraction.
```

This does not change discriminant.  It only replaces an unspecified lower
bracket by the exact scalar self-energy and its complement denominator.

## 7. Status

```text
proved:    coarse tail Ritz bracket (H-1) from H_L=D_L+B_L;
proved:    any certified bracket plus divergent bracketed low-mode sum
           implies BTG-DIV-L and corrected Weyl-disk LP (H-2);
observed:  coarse finite tail bracket is inactive through max_modes=18;
observed:  zeta low-mode BTG remains strong under finite references;
observed:  planted obeys the same bracket audit and stays A-neutral;
refuted:   directional Ritz residual alone as a certified bracket;
open:      interlacing-scale RITZ-BRACKET;
open:      BRACKETED-LOW-MODE-BTG;
live:      FESHBACH-RITZ-ENVELOPE with explicit complement coercivity
           kappa_R(E).
```

