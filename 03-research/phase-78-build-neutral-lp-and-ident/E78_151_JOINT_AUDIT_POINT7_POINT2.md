# E78.151 - Joint audit: point 7 closed (conditional module), point 2 reduced

**Run:** 2026-07-21.
**Scope:** IDENT (OUTER-LIMIT / point 7) and LP interface (point 2).
**Class:** REDUCCION GENUINA (point 2) + CONDITIONAL CLOSURE (point 7).
**Attribution:** results from the program author's joint Phase-76/77/78 audit
(external contribution, 2026-07-21). Verified and integrated here.

## 1. Point 7 (OUTER-LIMIT) -- CLOSED as a module conditional on point 6

Let

```text
A(s) = 2/s + 2/(s-1) - log pi + psi(s/2),
H_L(s) = A(s) - 2 sum_{n <= e^L} Lambda(n) n^{-s}.
```

**Theorem (OUTER-LIMIT, conditional).** Suppose the exact fixed-L cell/Gamma
identification supplies, locally uniformly on `Re s > 1`,

```text
G_L(s - 1/2) - H_L(s) -> 0.                                  (7.2)  [= point 6]
```

Then locally uniformly on `Re(1/2+sigma) > 1`,

```text
G_L(sigma) -> 2 Xi'(1/2+sigma)/Xi(1/2+sigma),               (7.3)
```

and, integrating from a safe `s_0` (`Re s_0 > 1`) on any simply connected
`Omega compact-in {Re s>1}` containing `s_0`,

```text
int_{s_0}^{s} G_L(w-1/2) dw -> 2 log( Xi(s)/Xi(s_0) ),       (7.4)
exp( int ... ) -> ( Xi(s)/Xi(s_0) )^2.
```

**Proof.** P76.039 (theorem-grade, Chebyshev, no RH) gives
`sum_{n>e^L} Lambda(n) n^{-s} -> 0` locally uniformly on `Re s > 1`; with the
absolutely convergent `2 Xi'/Xi = A(s) - 2 sum_{n>=2} Lambda(n) n^{-s}`, this
yields `H_L -> 2 Xi'/Xi`. Combined with `(7.2)`, `(7.3)` follows. `Xi` is
zero-free on `Re s>1` (Euler product), so a holomorphic log exists on `Omega`;
local uniform convergence permits integration along bounded-length paths, giving
`(7.4)`; exponentiation preserves it. QED.

**Verified:** P76.039 states exactly `sum_{n>lambda^2} Lambda(n) n^{-s} =
O_delta(exp(-delta L))` locally uniformly on `Re s >= 1+delta`, and its own
ledger note warns that the cell identity `(ET-3)` must be derived BEFORE
attaching the Euler tail -- which is why `(7.2)` is a genuine hypothesis (point
6), not free. So point 7 adds no new arithmetic obstacle: it is closed the moment
point 6 delivers `(7.2)`.

```text
STATUS point 7: CLOSED as a dependent module (conditional on point 6's (7.2)).
```

## 2. Point 2 (Weyl response) -- ambiguity closed, existence reduced to one residue

**Theorem (residue-normalized Weyl response).** Let `H` be self-adjoint with
compact resolvent, `mu` an isolated eigenvalue, `P_mu` its Riesz projection,
`b` a source, `ell` a bounded normalizing functional. For `z` off spectrum with
`ell((H-z)^{-1}b) != 0` define

```text
u_hat(z) = (H-z)^{-1} b / ell( (H-z)^{-1} b ).
```

(a) `u_hat(z)` is the UNIQUE vector with `(H-z) u_hat in span{b}` and
`ell(u_hat)=1`. (b) If `alpha_mu := ell(P_mu b) != 0`, then as `z -> mu`,

```text
u_hat(z) -> v_mu := P_mu b / ell(P_mu b)   in norm.
```

(c) `v_mu in ker(H-mu)`, `ell(v_mu)=1`, canonical even if `dim ker(H-mu) > 1`
(the SOURCE selects the response, not an eigenbasis). (d) For locally bounded
`C: H -> Hol(V)` (e.g. safe Cauchy rows `r_z v = sum_n v_n/(z-d_n)`, which are
uniformly `l^2` on safe compacta), `C u_hat(z) -> C v_mu` locally uniformly.

**Proof.** Laurent expansion `(H-z)^{-1} = P_mu/(mu-z) + R_mu(z)`, `R_mu`
holomorphic near `mu`; multiply numerator and denominator of `u_hat` by
`(mu-z)`; the pole cancels and `(b)` follows under `alpha_mu != 0`. QED. (This
is standard; verified as correct.)

**Consequence.** The apparent "four Weyl responses" ambiguity is a non-issue:
the normalized off-spectrum response is unique and canonical. Point 2's
`(d) existence of normalized l2 class` reduces to the SINGLE scalar residue

```text
alpha_mu = ell(P_mu b)  (finite section: ell_N(P_N b_N)),
```

either non-vanishing, OR the weaker projective statement that
`P_N b_N / ell_N(P_N b_N)` converges in the safe Cauchy topology even if the
residue -> 0.

```text
STATUS point 2: response ambiguity CLOSED; existence reduced to the residue
alpha_mu (non-vanishing) or its projective-convergence analogue.
```

## 3. Cross-link: the point-2 residue IS the c_0 object (E78.145/146)

For a 1-dimensional cluster with unit eigenvector `e_N`,

```text
ell_N(P_N b_N) = ell_N(e_N) * <e_N, b_N> = ell_N(e_N) * c_0^{(N)},
```

where `c_0^{(N)} = <e_N, b_N>` is exactly the bottom-mode boundary coupling of
E78.144/145 -- the object that COLLAPSES geometrically for zeta (E78.145: c_0
decays ~14 orders over N=6..16) and whose lower bound is the hard open problem
that NO-DEMOCRATIC-WITNESS (E78.146) showed is unavoidable. So:

- the "non-vanishing residue" route (option i) is the c_0 lower-bound problem in
  disguise -- known hard;
- the "projective convergence even as residue -> 0" route (option ii) is
  potentially NEW and BETTER: it asks only that the direction converge, not that
  the residue stay bounded below.

The cluster-residue probe (`E78_cluster_residue_probe.py`) supports option (ii):
for zeta the residue `alpha` collapses (~1e-18..1e-25) while the normalized
`v_N^res` stays controlled (norm ~2.5-2.9) and the safe profile `C_{2i}(v^res)`
stabilizes (0.198, 0.191, 0.186, 0.183). Plant `alpha` does NOT collapse
(0.0148, 0.294, 0.058, 0.028) and its profile also stabilizes (~0.87-0.95).
Both stabilize -> this experiment supports EXISTENCE (option ii) but is NOT the
arithmetic discriminant (build-neutral direction convergence).

```text
LIVE (point 2): PROJECTIVE-SOURCE-CONVERGENCE -- prove P_N b_N/ell_N(P_N b_N)
converges in the safe Cauchy topology even as the residue collapses. This
sidesteps the c_0 lower bound (E78.146) and is the recommended route.
```

## 4. Corrections folded in

```text
- E78.150 reclassified: relative projective flatness against an INTEGRATED Gamma
  primitive is a REFORMULATION (locally equivalent to the derivative defect by
  Borel-Caratheodory both ways), NOT independent forcing. Point 6 needs an
  INDEPENDENT cell/Gamma object (determinant / Schur-complement / finite-product).
- Moving boundary pole d_{b,N}=2piN/L: confirmed (E78.149), summable O(1/N^2).
```

## 5. Revised map (after joint audit)

```text
Point 2: response ambiguity CLOSED; existence reduced to residue alpha_mu.
         Recommended route: PROJECTIVE-SOURCE-CONVERGENCE (option ii), which
         sidesteps the c_0 lower bound.
Point 5: projective shell cross-ratio = valid fixed-L convergence candidate;
         summable collar estimate (ZERO-SIDE-BOUNDEDNESS, E78.147) still open.
Point 6: THE hard arithmetic gap. Projective flatness is only a reformulation;
         requires an INDEPENDENT cell/Gamma object. Unchanged in difficulty.
Point 7: CLOSED as a dependent module, conditional only on point 6's (7.2).
```

Two ambiguity sources (Weyl response, outer limit) are eliminated. Omega7 and RH
are NOT closed. The gap is now concentrated cleanly in the INDEPENDENT
cell/Gamma construction of point 6.

## 6. Status

```text
proved (verified):
  point 7 OUTER-LIMIT closed conditional on point 6 (7.2), via P76.039;
  point 2 residue-normalized Weyl response canonical (Laurent expansion);
reduced:
  point 2 existence -> single residue alpha_mu = ell(P_mu b), or projective
  convergence (option ii, recommended, sidesteps c_0 lower bound);
cross-link:
  alpha_mu = ell_N(e_N) c_0^{(N)} -- the E78.145/146 c_0 object;
corrected:
  E78.150 = reformulation not forcing; moving pole confirmed summable;
open:
  point 6 INDEPENDENT cell/Gamma object (the hard gap);
  point 2 PROJECTIVE-SOURCE-CONVERGENCE;
  point 5 ZERO-SIDE-BOUNDEDNESS (E78.147);
next:
  point 6: build A^cell_{L,N} as an exact determinant/Schur-complement quotient
  independent of the target derivative identity.
```
