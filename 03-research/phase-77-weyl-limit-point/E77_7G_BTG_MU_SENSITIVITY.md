# E77.7g - BTG-DIV and true-mu sensitivity

**Run:** 2026-07-18.

## 1. Purpose

E77.7f replaced the invalid one-coupling target by the moving boundary
spectral trace

```text
BTG-DIV-L:
S_N(mu_L)=int (t-mu_L)^(-2) d beta_N(t) -> infinity,
beta_N=sum_j |<u_j^(N),b_N>|^2 delta_{nu_j^(N)}.
```

This note attacks `BTG-DIV-L` without identifying `mu_L` with one finite
reference.  It records:

```text
1. the exact first-modes/tail split;
2. the implication BTG-DIV-L => fixed-mu growth => corrected LP;
3. what compact resolvent plus Ritz convergence does and does not certify;
4. a zeta/planted sensitivity probe over several Ritz references.
```

## 2. Exact first-modes/tail split

Let

```text
A_N(mu)=H_L[I_N,I_N]-mu I,
b_N=H_L[I_N,N],
```

and let `(nu_j^(N),u_j^(N))` be the orthonormal eigenpairs of the finite
inner block `H_L[I_N,I_N]`, ordered increasingly.  For any `K>=1`,

```text
S_N(mu_L)
=sum_{j<K} |<u_j^(N),b_N>|^2 / |nu_j^(N)-mu_L|^2
 + sum_{j>=K} |<u_j^(N),b_N>|^2 / |nu_j^(N)-mu_L|^2.       (G-1)
```

This is just the finite spectral theorem.  No positivity of Weil type is
being used; all summands are squared Hilbert coefficients of a finite
self-adjoint block.

The admissible reduced target is therefore:

```text
LOW-MODE-BTG(K):
sum_{j<K} |<u_j^(N),b_N>|^2 / |nu_j^(N)-mu_L|^2 -> infinity.
```

Then

```text
LOW-MODE-BTG(K) => BTG-DIV-L.
```

The tail can also imply BTG, but a tail-only claim must be named separately:

```text
TAIL-BTG(K):
sum_{j>=K} |<u_j^(N),b_N>|^2 / |nu_j^(N)-mu_L|^2 -> infinity.
```

The probe below shows that the bottom mode dominates the measured finite
references, so `LOW-MODE-BTG(1)` is the numerically natural target.  It is
not yet proved at the true `mu_L`.

## 3. Implication to LP

By definition,

```text
BTG-DIV-L <=> S_N(mu_L)=||A_N(mu_L)^(-1)b_N||^2 -> infinity
```

whenever `A_N(mu_L)` is invertible; if it is singular for infinitely many
sections, the Weyl disk radius is already zero along those sections and the
same contraction conclusion holds after the standard finite-section
regularization.  Therefore

```text
BTG-DIV-L
=> FIXED-MU-BLOCK-GROWTH
=> Weyl-disk radius ~ 1/S_N(mu_L) -> 0
=> CORRECTED-LP
```

where `CORRECTED-LP` is the P76.065/P76.066 endpoint: the bordered Weyl disk
for the safe Cauchy transform contracts to a unique normalized safe ratio.
This avoids the E77.7f-refuted wording `ker_l2(H_L-mu_L)=0`.

## 4. Ritz one-sided audit

E77.7d proves compact resolvent, hence finite Ritz values satisfy

```text
mu_R=lambda_min(P_R H_L P_R) decreases to mu_L,
mu_L <= mu_R.
```

This is a genuine one-sided upper bound.  It is not enough by itself for
BTG-DIV.  The BTG denominator is

```text
|nu_j^(N)-mu_L|^2,
```

and replacing `mu_L` by `mu_R` can change the trace by many orders whenever
`mu_R` lies close to `nu_0^(N)`.  Compact-resolvent convergence gives no
effective lower bracket

```text
mu_R - eps_R <= mu_L <= mu_R
```

with `eps_R` small compared with the inner gaps.  E77.7d's diagonal lower
growth can in principle produce such a bracket after a quantified tail form
bound, but that bound is not present in the current ledger.

Thus the shortcut

```text
compact resolvent + Ritz convergence => numerically sufficient true-mu BTG
```

is refuted as a proof step.  The smaller admissible object is:

```text
RITZ-BRACKET:
construct explicit eps_R down to the interlacing scale such that
mu_R-eps_R <= mu_L <= mu_R,
using only the D+B tail form and no ambient inverse norm.
```

Together with a stable low-mode lower bound, `RITZ-BRACKET` would imply
`BTG-DIV-L`.

## 5. Probe

Companion:

```text
E77_7g_btg_mu_sensitivity_probe.py
E77_7g_btg_mu_sensitivity_results.json
```

Command:

```bash
python3 E77_7g_btg_mu_sensitivity_probe.py \
  --lambda 6 --max-modes 18 --refs 12,14,16,18 \
  --min-modes 6 --top-k 6 --dps 70
```

Every `mu_ref` is a finite Ritz upper bound surrogate, not `mu_L`.

### Zeta

| ref R | mu_R | N=R log10 S_R(mu_R) | dominant mode | dominant fraction | ground fraction |
|---:|---:|---:|---:|---:|---:|
| 12 | 2.4032e-37 | 21.2257 | 0 | 0.987535 | 0.987535 |
| 14 | 1.7090e-41 | 21.7393 | 0 | 0.990668 | 0.990668 |
| 16 | 1.5414e-45 | 23.7099 | 0 | 0.992605 | 0.992605 |
| 18 | 2.5272e-49 | 27.9644 | 0 | 0.993883 | 0.993883 |

For common `N<=12`, changing the reference from `R=12` to `R=18` produces
small spread:

```text
N=6:  spread log10 S = 2.72e-17
N=8:  spread log10 S = 1.79e-12
N=10: spread log10 S = 1.11e-7
N=12: spread log10 S = 4.81e-3
```

The anatomy is stable: the bottom inner mode dominates and its fraction
increases down the chain.  This supports `LOW-MODE-BTG(1)` as the right
object, but it does not prove it at the true `mu_L`.

### Planted build

Standard plant:

```text
gamma=14.134725141734693790, beta=.30, strength=5.
```

| ref R | mu_R | N=R log10 S_R(mu_R) | dominant mode | dominant fraction | ground fraction |
|---:|---:|---:|---:|---:|---:|
| 12 | -1.709459386 | 2.4470 | 0 | 0.994415 | 0.994415 |
| 14 | -1.724145652 | 3.4785 | 0 | 0.999951 | 0.999951 |
| 16 | -1.740018688 | 2.3431 | 0 | 0.997161 | 0.997161 |
| 18 | -1.744693689 | 2.4347 | 0 | 0.994851 | 0.994851 |

For common `N<=12`, the reference spread is larger:

```text
N=6:  spread log10 S = 0.0180
N=8:  spread log10 S = 0.0226
N=10: spread log10 S = 0.1191
N=12: spread log10 S = 1.3053
```

The same low-mode anatomy appears in the plant.  Therefore low-mode
dominance is falsifier-neutral and cannot be the proof target by itself.
The zeta/plant scale separation remains a diagnostic only.

## 6. Autopsy

BTG-DIV is not closed in E77.7g.  The obstruction is precise:

```text
Ritz values converge from above, but BTG requires denominators at the true
mu_L.  Without a certified lower bracket for mu_L on the scale of the
inner-block ground gap, finite-reference blowup does not imply true-mu
blowup.
```

This is not the P76.061 ambient inverse wall.  It is a scalar spectral
localization problem for `mu_L`, and it must be solved before the finite
`coeff/gap` tables can become a theorem.

The minimum next object is:

```text
BRACKETED-LOW-MODE-BTG:
there exist K, eps_R->0 and a cofinal relation R=R(N) with
mu_R-eps_R <= mu_L <= mu_R
such that
sum_{j<K}
 |<u_j^(N),b_N>|^2
 / max(|nu_j^(N)-mu_R|+eps_R, lower_gap_floor_N)^2
 -> infinity.
```

The denominator must be stated with a certified bracket, not with a chosen
finite reference.  This object implies `LOW-MODE-BTG(K)`, hence
`BTG-DIV-L`, hence fixed-mu block growth and corrected LP.

## 7. Status

```text
proved:    first-modes/tail split (G-1);
proved:    LOW-MODE-BTG(K) => BTG-DIV-L;
proved:    BTG-DIV-L => fixed-mu block growth => corrected Weyl-disk LP;
proved:    Ritz mu_R decreases to mu_L from above under compact resolvent;
refuted:   Ritz convergence alone as a sufficient certified true-mu bound;
observed:  zeta low-mode dominance 0.9875--0.9939 across R=12,14,16,18;
observed:  zeta log10 S_R rises to 27.9644 at R=18;
observed:  planted also low-mode dominated, so dominance is A-neutral;
open:      RITZ-BRACKET;
open:      BRACKETED-LOW-MODE-BTG;
open:      BTG-DIV-L and corrected LP.
```

No Weil positivity, pseudoinverse, ambient inverse norm, or zero list is used.
