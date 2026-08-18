# E77.7f - Fixed-mu block growth and boundary-trace autopsy

**Run:** 2026-07-18.

## 1. Purpose

E77.7e removed `DIR-GAP-PAIR` from the required chain.  The live LP route is
now the fixed-point Weyl disk target:

```text
FIXED-MU-BLOCK-GROWTH:
S_N(mu_L)=||A_N(mu_L)^(-1)b_N||^2 -> infinity
=> finite Weyl-disk radius -> 0
=> SAFE-LIMIT-POINT interface used by P76.065--P76.067.
```

This note audits three points:

```text
1. what H_L=D_L+B_L with D_n->+infinity actually implies;
2. how that corrects the old "ker_l2(H_L-mu_L)=0" wording;
3. whether block growth reduces to one nonzero coupling with the ground mode.
```

The answer to (3) is no as stated: `b_N` is a moving boundary column, not a
fixed `l2` source.

## 2. Compact-resolvent consequence

From E77.7d,

```text
H_L=D_L+B_L,
D_L(n)=log(1+|n|)+O_L(1),
B_L bounded self-adjoint.
```

Since `D_L(n)->+infinity`, for any sufficiently negative real `z`,
`(D_L-z)^(-1)` is compact.  Also

```text
H_L-z = (I+B_L(D_L-z)^(-1))(D_L-z),
```

and for `z` far enough below the lower bound the first factor is invertible
by Neumann.  Hence `(H_L-z)^(-1)` is compact.

Therefore:

```text
COMPACT-RESOLVENT:
H_L has purely discrete spectrum, finite eigenvalue multiplicities, and
lambda_j(H_L)->+infinity.
```

In particular,

```text
mu_L=inf spec(H_L)
```

is an actual isolated eigenvalue of finite multiplicity.  This is proved for
the zeta and planted fixed-L operators, because E77.7d proved the same
`D+B` decomposition for both.

## 3. Ledger correction: the old kernel statement is false

P76.067 stated LP as:

```text
the semi-infinite rectangular CCM system is in the Weyl limit-point case;
its l2 kernel is trivial;
equivalently S_N->infinity.
```

The literal homogeneous-kernel clause cannot be right at the realized
spectral point `mu_L`.  By compact resolvent,

```text
ker_l2(H_L-mu_L) != {0}.
```

This is not a cosmetic wording issue.  The object used by P76.065/P76.066 is
not absence of the ground eigenfunction.  It is:

```text
CORRECTED-LP:
the bordered Weyl disks for the safe Cauchy transform contract to one point;
equivalently the canonical finite boundary energy S_N diverges; equivalently
the normalized safe Cauchy transform selected by r_{z0}v=1 is unique.
```

Thus the admissible implication is

```text
FIXED-MU-BLOCK-GROWTH => Weyl-disk contraction => CORRECTED-LP
```

and the phrase `ker_l2(H_L-mu_L)=0` is refuted for this endpoint.  If an
older proof used that phrase literally, that proof must be reread through the
bordered/Weyl-disk formulation.

## 4. Why one fixed coupling is the wrong reduction

The tempting reduction was:

```text
S_N(mu_L)->infinity  <=>  <v0,b> != 0,
```

where `v0` is a ground eigenvector of `H_L`.  This is not a well-formed
infinite statement for the actual bordered system.  The source is

```text
b_N = H_L[I_N,N],
I_N={-N+1,...,N-1},
```

so it moves with the boundary and has no fixed `l2` limit.

Moreover, the ground-state equation itself predicts possible decay of the
boundary overlap.  For a finite reference eigenpair `(mu_*,v_*)` and right
boundary index `N`, the exact row identity is

```text
<v_*|I_N,b_N>
 = (mu_*-H_NN)v_N
   - H_{N,-N}v_{-N}
   - sum_{|j|>N} H_{N,j}v_j.                  (BT-1)
```

In the infinite limit, if `v0 in Dom(D_L)` and the bounded off-diagonal row
tail is controlled, the right side may tend to zero.  Thus nonzero
stabilization of `<P_N v0,b_N>` is not expected and is not the right target.

The probe verifies `(BT-1)` against the finite reference eigenvector to
`~1e-70` relative defect.

## 5. Minimal correct object: boundary-trace/gap divergence

Let

```text
A_N(mu)=H_L[I_N,I_N]-mu I,
b_N=H_L[I_N,N].
```

If `A_N(mu_L)` is singular, the corresponding Weyl radius has already
collapsed at that section.  Otherwise, by the spectral theorem for the finite
inner block,

```text
S_N(mu_L)
 = ||A_N(mu_L)^(-1)b_N||^2
 = sum_j |<u_j^(N),b_N>|^2 / |nu_j^(N)-mu_L|^2.       (BTG)
```

This gives the exact replacement:

```text
BTG-DIV:
sum_j |<u_j^(N),b_N>|^2 / |nu_j^(N)-mu_L|^2 -> infinity.
```

Then

```text
BTG-DIV <=> FIXED-MU-BLOCK-GROWTH
         => Weyl-disk contraction
         => CORRECTED-LP.
```

If the bottom inner mode is simple and dominates, `(BTG)` may be measured by
one coefficient-over-gap term.  But the theorem must remain the spectral
boundary-trace statement, because it is stable under moving sources and
finite multiplicity.

## 6. Probe

Companion:

```text
E77_7f_fixed_mu_block_growth_probe.py
E77_7f_fixed_mu_block_growth_results.json
```

Command:

```bash
python3 E77_7f_fixed_mu_block_growth_probe.py \
  --lambda 6 --reference-modes 18 --min-modes 6 --dps 70
```

The frozen point is the largest measured finite-section value.  It is only a
finite surrogate for the abstract `mu_L`.

### Zeta, finite reference N=18

```text
mu_ref = 2.527196445239004e-49
reference ground gap = 3.843448995117970e-46
```

| N | S_N(mu_ref) | radius proxy | ground gap | ground coeff | coeff/gap | ground energy frac | ref boundary overlap |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 6  | 1.0465261e7  | 9.5554e-8  | 7.4349e-21 | 2.3680e-17 | 3.1850e3  | 0.9693 | 3.8788e-4 |
| 12 | 1.6630705e21 | 6.0130e-22 | 4.3015e-35 | 1.7431e-24 | 4.0523e10 | 0.9874 | 7.6303e-9 |
| 18 | 9.2132330e27 | 1.0854e-28 | 2.3314e-47 | 2.2310e-33 | 9.5692e13 | 0.9939 | 5.2718e-15 |

Reading: the energy grows violently, but the projected reference-boundary
overlap decays.  The one-coupling stabilization picture is false even in the
case where block growth is strongest.  The operative quantity is
`coeff/gap`.

### Planted build, gamma=14.134725141734693790, beta=.30, strength=5

```text
mu_ref = -1.744693689057264
reference ground gap = 0.1015921928631942
```

| N | S_N(mu_ref) | radius proxy | ground gap | ground coeff | coeff/gap | ground energy frac | ref boundary overlap |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 6  | 1.1262e-3 | 8.8792e2   | 1.7065 | 3.3716e-2 | 1.9758e-2 | 0.3466 | 1.8319e-2 |
| 12 | 1.3857e1  | 7.2165e-2  | 4.4854e-2 | 1.6050e-1 | 3.5782 | 0.9240 | 1.6293e-1 |
| 18 | 2.7206e2  | 3.6756e-3  | 4.5540e-3 | 7.4922e-2 | 1.6452e1 | 0.9949 | 8.3548e-2 |

Reading: the plant does not show zeta-scale contraction under this finite
reference.  This is a diagnostic only, not a proof mechanism.  It is
consistent with P76.066/E77.6: the plant can stall in the Weyl/IDENT
architecture, but a separator by itself is not an admissible target.

## 7. Status

```text
proved:    H_L=D_L+B_L with D_n->+infinity implies compact resolvent;
proved:    mu_L is an isolated finite-multiplicity eigenvalue;
refuted:   literal old LP clause ker_l2(H_L-mu_L)=0;
corrected: LP endpoint is bordered Weyl-disk contraction / unique safe
           normalized Cauchy transform;
refuted:   FIXED-MU-BLOCK-GROWTH <=> one fixed nonzero <v0,b>;
proved:    finite spectral equivalence BTG-DIV <=> fixed-mu block growth;
observed:  zeta S_N(mu_ref) grows to 9.21e27 at finite reference N=18;
observed:  zeta reference boundary overlap decays to 5.27e-15;
observed:  planted S_N(mu_ref) reaches 2.72e2 at N=18 and stalls relative
           to zeta;
open:      BTG-DIV at the true mu_L, hence CORRECTED-LP;
open:      SHELL-CAUCHY-GROWTH / RDP-SHELL after corrected LP.
```

## 8. Next admissible target

The next proof target should not be a scalar overlap.  It should be:

```text
BTG-DIV-L:
for the true fixed-L ground point mu_L, the moving boundary spectral measure
beta_N=sum_j |<u_j^(N),b_N>|^2 delta_{nu_j^(N)}
satisfies
int (t-mu_L)^(-2) d beta_N(t) -> infinity.
```

This target has the required implication to the previous endpoint and does
not use Weil positivity, a pseudoinverse, ambient inverse norms, or a zero
filter.
