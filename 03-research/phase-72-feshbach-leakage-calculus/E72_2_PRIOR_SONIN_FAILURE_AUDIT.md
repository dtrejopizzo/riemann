# E72.2 -- Prior Sonin/prolate failures audit

**Date:** 2026-07-08.
**Role:** read the earlier Sonin/CCM material and extract the constraints that Phase 72 must obey.

## Files audited

Core files named by the user:

- `00-MAP.md`
- `phase-4-handoff/proofs/00-PROOF-LOG.md`
- `phase-60-discriminant/00-PLAN.md`
- Phase 32 Docs 59--64:
  - `59-puente-ccm-cinfty.md`
  - `60-decaimiento-discrepancia-jacobi.md`
  - `61-localidad-funcional-ln-desbranges.md`
  - `62-pcn-transformada-stieltjes.md`
  - `63-escala-christoffel-suma-global.md`
  - `64-ctp-equivalencia-rh.md`
- `phase-35-five-fronts/100-maslov-semilocal.md`
- `phase-39-G1G2-interface/120-inventario-CC-fuente.md`
- `phase-40-close-G1/124-positividad-weil-vs-indice-hodge.md`

Also searched the repo for `Sonin/Sonine`.

## 1. What Sonin already gave us

The earlier program already established the useful structural facts:

1. The Sonin space exists and is canonical in the Connes--Consani/CCM framework.
2. The semilocal Sonin space is stable for finite `S`: CCM's `theta_S` is a Hilbert isomorphism
   between the archimedean and semilocal Sonin spaces.
3. The prolate/Sonin model supplies a real self-adjoint operator and the right phase-space language.
4. The archimedean window `(1/2,2)` is the one unconditional positive case, via Yoshida/CC.
5. Feshbach/Schur shorting is the correct way to remove the pole line; naive subtraction is forbidden.

So Phase 72 should use Sonin as a **stable reservoir and coordinate system**, not as an unproved
positivity theorem.

## 2. Why the old Sonin route failed

### Failure A -- locality of the Jacobi perturbation functional

Docs 59--62 tried to bridge off-line zeros to Jacobi discrepancies through a local functional

```text
L_n[f] = (a_n^infty)^2 int (|P_{n+1}|^2-|P_n|^2) f dm_infty.
```

Doc 61 proved the exact formula and then identified the required hidden assumption: `L_n` would have to
act like evaluation at `gamma_n`.

Doc 62 refuted the exact point-local PCN: the Stieltjes transform

```text
F_n(z)=G_{n+1,n+1}(z)-G_{n,n}(z)
```

cannot be a literal pole `c/(z-gamma_n)` because its expansion at infinity has the wrong moment
vanishing. The correct possible object was downgraded to a pseudo-pole.

### Failure B -- the Christoffel scale was wrong

Doc 63 corrected the decisive scale:

```text
lambda_n(gamma_n) = O(1), not O(1/log gamma_n).
```

Reason: the nodes of the orthogonal polynomials for `dm_infty` are not the zeta zeros. The Christoffel
scale is governed by the Freud-type archimedean measure, not by the Riemann-von Mangoldt zero density.

Consequence: any argument that needs the Jacobi kernel to resolve zeta-zero spacing is dead. The kernel
`kappa_n=(a_n^infty)^2(|P_{n+1}|^2-|P_n|^2)` oscillates with many sign changes and is not a positive
localized bump at `gamma_n`.

### Failure C -- the positive trace became an RH-equivalent detector

Docs 63--64 replaced individual locality by the cumulative trace

```text
T_lambda = sum_{gamma_n<=lambda} (Delta_n^full-Delta_n^full,on).
```

This produced a clean equivalence:

```text
RH iff T_lambda=0 for all lambda.
```

But it did not prove `T_lambda=0`; it produced a detector equivalent to RH. This is useful, but it is
not a forcing mechanism.

### Failure D -- semilocal Sonin positivity has no known uniform extension

Doc 100 found the real semilocal obstruction:

```text
O_SL = non-uniform quantitative control of the Weil-Sonine discrepancy.
```

The Sonin reservoir survives as `S` grows, but the Toeplitz/discrepancy estimates do not come with
uniform constants. The first genuinely arithmetic step

```text
S={infty,2}
```

is already open as Conjecture 100.A. The obstruction is quantitative, not structural.

### Failure E -- Sonin/prolate positivity is spectral, not Hodge/intersection

Docs 120 and 124 verify that the Connes--Consani/CCM positivity is not the missing Hodge-index
intersection form on a square. It is spectral Weil positivity on test functions. Extending it globally
is exactly MW-1/RH.

Thus Phase 72 must not rebrand spectral Sonin positivity as the geometric G2 ingredient.

## 3. What this means for Phase 72

The first version of E72.1 proposed an "arithmetic Poisson-Sonin integration-by-parts formula." That
phrasing is dangerous because it can be read as a return to PCN/local evaluation.

The corrected Phase 72 target is:

```text
leakage, not locality.
```

Specifically, Phase 72 should estimate

```text
L_x = Q_x (H_x-H_x^0) k_lambda
```

as a vector norm in the prolate complement. It must not try to show that a Christoffel kernel is a
Poisson kernel centered at a zeta zero.

## 4. The allowed new theorem

The new theorem may use:

- Feshbach shorting of the pole mode;
- the prolate/Sonin slow sector as a coordinate system;
- orthogonality to the prolate ground line;
- cancellation after projection onto the complement;
- a norm-square estimate over complement modes.

It may not use:

- `L_n` as a point-local evaluator at `gamma_n`;
- a PCN exact pole;
- Christoffel scale `1/log gamma`;
- positivity of the full Weil/Sonin discrepancy;
- semilocal uniformity in `S` without proving the constants;
- a Hodge/intersection interpretation of CC positivity.

## 5. Corrected arithmetic leakage target

The first corrected estimate was the **projected residual estimate**:

```text
sum_{j>=1} |<e_{x,j}, (H_x-H_x^0) k_lambda>|^2 = o(g_x^2),
```

where `{e_{x,j}}` are prolate complement modes and `g_x` is the model gap.

E72.3 sharpens this again. The actually necessary Feshbach quantity is the reduced residual:

```text
sum_{j>=1} |<e_{x,j}, (H_x-H_x^0) k_lambda>|^2 / lambda_{x,j}^2 -> 0,
```

where `lambda_{x,j}` are the eigenvalues of the compressed complement `C_x`. Equivalently,

```text
||C_x^{-1}Q_x(H_x-H_x^0)k_lambda|| -> 0.
```

This can be true even if:

```text
||H_x-H_x^0||
```

is large, even if `||Q_x(H_x-H_x^0)k_lambda||/g_x` is not small, and even if every individual
local/Jacobi kernel oscillates. The estimate is global in the complement, measured in the Feshbach graph
norm, and does not require point locality.

## 6. What would count as a non-repeating proof

A valid Phase 72 forcing proof must supply an identity of the form

```text
Q_x(H_x-H_x^0)k_lambda = C_x u_x + r_x,
||u_x|| -> 0,
||C_x^{-1}r_x|| -> 0,
```

where the cancellation happens before taking absolute values but after the correct Feshbach/pole
shorting.

This is different from:

```text
int kappa_n(s) P_delta(s-gamma) dm_infty approx P_delta(gamma_n-gamma),
```

which is the old PCN route and is refuted/scale-blocked.

## 7. Verdict

The Sonin history does not kill Phase 72, but it forces a correction:

```text
Do not prove leakage by localizing Christoffel/Jacobi kernels.
Prove leakage as a reduced Feshbach-projected vector cancellation.
```

If that reduced projected estimate also collapses to the semilocal discrepancy constants of Doc 100,
then Phase 72 is not new and should be archived as another form of `O_SL`. The next test is therefore to
express the functional

```text
v |-> <v,(H_x-H_x^0)k_lambda>
```

in exact CCM/Sonin variables and see whether its dual `C_x`-graph norm is genuinely a one-vector
estimate or secretly the full Weil--Sonine discrepancy again.
