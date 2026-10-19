# P124.014 -- the shifted pair realizes case 2 of the shielding dichotomy

Status: `COMPUTATIONAL-CERTIFICATE` with the declared scope of Section 3.
It is a **model observation**, not an interval certificate and not a theorem
about the continuum operator.  Its role is to instantiate case 2 of
[P124.013](P124_013_ENTIRE_FORM_AND_SHIELDING_DICHOTOMY.md) Theorem 3.1 and
thereby to **refute** the hypothesis that Gate R could be a structural theorem
of the functional-equation-plus-Tate-compression class.

## 1. Why the falsifier is usable here, and why it had not been used

`P122_D_SPECIFICATION` section 5 and `P3_COMMON_FAILURE_ARCHITECTURE` section
8 require every candidate row-(d) law to fail, for a visible reason, on
Davenport--Heilbronn and on the shifted pair `Xi_a(s)=xi(s+a)xi(s-a)`.
`P121_BOMBIERI_SUZUKI_XIA_AUDIT` correctly observed that `Xi_a` is a *typing*
falsifier and that "running it before the candidate exists cannot reveal the
missing source identity", because the first-contact state for `Xi_a` was not
explicit.

That objection does not apply to the quantities of P124.013.  `Xi_a` has zeros
off the critical line for `0<a<1/2`, so its primitive form **must** lose its
sign at a finite window; its first contact is a genuine object, and the gate
functionals `J_\sigma` and the seam energies are evaluated on it directly.
The gates have never been measured on a genuine first contact before, because
for `zeta` no first contact is available without assuming RH false.

## 2. The model

`Xi_a` has the same analytic shape as `xi` with

* prime weights `w_n=\Lambda(n)(n^a+n^{-a})/\sqrt n` (still nonnegative, still
  supported on prime powers);
* archimedean multiplier
  `g_{1/4+a/2}(\tau)+g_{1/4-a/2}(\tau)-m_0(a)`,
  `m_0(a)=2\log\pi-\psi(\tfrac14+\tfrac a2)-\psi(\tfrac14-\tfrac a2)`;
* four poles, at `s=1\pm a` and `s=\mp a`, hence four Tate characters
  `e^{\pm(1/2+a)t}`, `e^{\pm(1/2-a)t}` and a rank-four primitive constraint
  `\Phi(1+a)=\Phi(1-a)=\Phi(a)=\Phi(-a)=0`;
* polar packet `2[\Phi(a)\Phi(1-a)+\Phi(-a)\Phi(1+a)]`.

At `a=0` this is `xi^2`, i.e. exactly twice the `zeta` data, so the family
degenerates to the audited case.  All of P124.013 Sections 1--3 applies
verbatim with `k=4` instead of `k=2`; nothing in those proofs used the Euler
product or the number of poles.

## 3. What was computed, and its exact scope

Piecewise-constant Galerkin discretization on the mesh of
`rowd_assembly.build_mesh` (breakpoints at every `\pm\log n` inside the
window), `refine=2` subdivisions per interval, double precision, **one
resolution only**.  No convergence study, no interval arithmetic, no
certified enclosure.  The generalized assembly reproduces the audited
phase-118 `zeta` matrices exactly (`max|dA|=0`), which controls transcription
but not discretization error.

**Control (`zeta`).**  Over `T\in[0.50,2.40]`, `\lambda_{\min}(L_T)>0`
throughout, `\Pi_{\ker}X=0` trivially, and `\Sigma(T)>0` with
`\lambda_{\min}\Sigma(T)` decreasing from `6.8\cdot10^{-2}` to
`9.0\cdot10^{-4}`.  No first contact appears, as it must not.

**Falsifier (`Xi_a`).**  The primitive form loses its sign at a finite window
for every tested shift, and the first contact moves out as the shift shrinks:

| `a` | first contact `T_*` bracketed | `|J(F_*)|` at `T_*` |
|---|---|---|
| 0.45 | [1.5369, 1.5380] | 9.0e-2 |
| 0.40 | [1.7267, 1.7278] | 4.4e-2 |
| 0.35 | [1.7413, 1.7425] | 3.4e-2 |
| 0.30 | [1.9605, 1.9617] | 1.4e-1 |
| 0.25 | [2.1323, 2.1334] | 3.5e-2 |
| 0.20 | [2.4599, 2.4610] | 4.0e-2 |

The trend `T_*(a)\uparrow` as `a\downarrow` is the expected one and is the
main sanity check on the family; the near-coincidence at `a=0.40,0.35` is at
the resolution of the scan and is not interpreted.

**The gate reading.**  At the first contact the collar vector `J(F_*)` has
components of two very different sizes.  For `a=0.35`,

```text
J(F_*) = ( -1.2e-14,  -3.34e-2,  -2.4e-15,  -1.97e-3 ),
```

ordered as `u=+(1/2+a), +(1/2-a), -(1/2+a), -(1/2-a)`.  The components against
the outer pair of Tate characters vanish to machine zero; those against the
inner pair do not, by twelve orders of magnitude.  The same split occurs at
every tested `a`, with the surviving pair being the outer one for `a=0.45`
and `a=0.20`.  Whichever pair survives, **Gate R fails**: the collar of a
genuine first-contact radical is nonzero.

Consistently with P124.013 Theorem 3.1, the unconstrained form breaks first:
for `a=0.35`, `\lambda_{\min}(\mathcal W)` is still positive
(`3.2\cdot10^{-3}`) at `T=1.68`, and negative at `T=1.80`, bracketing
`T_{\mathcal W}<T_q\approx1.742`.  This is case 2, "shielding", observed
directly.

**[phase 134 — resolution note of record, from Paper 46 §9.3(3)
and `R134_002` §6(3), each an independent re-run.  Section 3 already declares
"one resolution only, no convergence study", so this note is **within** the
declared scope and does not contradict it; it records what that disclaimer
costs.]**

*The Galerkin eigenvalues above are variational upper bounds.*  The
piecewise-constant space of `rowd_assembly.build_mesh` is a **subspace** of
the test space, and the primitive constraint is imposed exactly inside it, so
the computed `lambda_min(L_T)` is `>=` the true infimum.  Consequently **a
negative computed eigenvalue certifies a genuine negative direction; a
positive one certifies nothing.**  The same holds for `Sigma(T)`, which is
itself an infimum.

*The brackets in the table above are therefore not brackets.*  Two independent
re-runs at `a = 0.35` give

```text
T = 1.68    lambda_min(L_T) = +1.31e-1 (refine 2), -1.58e-1 (refine 3), -4.33e-1 (refine 4)
T = 1.7419  lambda_min(L_T) = +6.58e-3 (refine 2), -2.27e-1 (refine 3), -4.69e-1 (refine 4)
```

and `T = 1.7419` lies **inside** the printed bracket `[1.7413, 1.7425]`.  By
the variational remark, the refined values are certificates **up to quadrature
error** (the same caveat the phase-118 note carries, and the same one this
note's Section 3 already declares for its own resolution): `T_q(Xi_0.35)
<= 1.68`, i.e. **outside and below the printed bracket**, and the first
contact moves down as the mesh refines.  The four printed decimals of the
`T_*` column must **not** be cited as a bracket, and the `Sigma(T)` sign flip
observed near `T = 1.70` at `refine = 2` does not persist in the same place
under refinement.

*What is unaffected.*  Every **qualitative** conclusion of this note stands,
and stands on negative eigenvalues, which are certificates up to quadrature
error: the primitive form
of `Xi_a` does lose its sign at a finite window; a genuine first contact
exists; `J(F_*) != 0` there, so **Gate R fails**; case 2 of P124.013
Theorem 3.1 is realized; and the `zeta` scan exhibits no first contact.  The
last of these is, by the same remark, **incapable by construction** of
supporting any conclusion about `zeta` — as it should be, and as Section 3's
own scope sentence intends.  Paper 46 Theorem 7.1 supplies the structural
reason behind the separation: `Xi_a`'s local contacts are not shell volumes,
so its would-be Frobenius is not a partial isometry (Paper 44 Theorem 3ter.6).

**Gate S.**  At the same first contact every pairwise seam energy
`\|(E_{p}-E_{q})\mathfrak h_{F_*}\|^2/\log(q/p)` of P122.028 (4.2) is nonzero
and of order `10^{-2}` to `10^{0}` (largest on the small primes, e.g.
`(2,3)\mapsto8.6\cdot10^{-1}`).  So Gate S is also false for `Xi_a`, as it
must be: `P121_TRANSVERSE_SEAM_FIRST_CELL_RIGIDITY` Theorem 2.2 would
otherwise force `F_*=0`.  The seam is nonzero here for the structurally right
reason -- the local weights of `Xi_a` are `p^{-1/2\pm a}` rather than
`p^{-1/2}`, so its channels are not the unitary half-density channels of an
Euler product.

Davenport--Heilbronn was **not** run.  It has no poles, hence no Tate block
and no Gate R to test, and `RH1_RH9_AUDIT` retires it as a quantitative
control; it remains a qualitative contrast only.

## 4. What this changes

1. `REFUTED`: "Gate R is a general theorem for forms with a functional
   equation and a finite Tate compression."  The falsifier has exactly that
   structure and violates Gate R at a genuine first contact.  Any proof of
   Gate R for `zeta` must use unimodularity of the local roots, i.e. the same
   arithmetic input Gate S needs.  The hope of discharging R by soft analysis
   and leaving S as the sole arithmetic obligation is closed.
2. `CONFIRMED` (as an instance, not a proof): case 2 of P124.013 Theorem 3.1
   is realized, with `T_{\mathcal W}<T_q` bracketed numerically.  The
   dichotomy is not vacuous on either side.
3. The constraint-free target (3.2) of P124.013, `\Sigma(T)\ge0` for all
   `T<T_q`, is the surviving formulation of Gate R.  For `Xi_a` it fails
   before `T_q`; for `zeta` it held throughout the scanned range.  That
   contrast is now the concrete separation any candidate law must reproduce,
   and it is stated entirely in terms of explicit objects.

No new positivity is proved here, and no window of `zeta` beyond the certified
`T=\log2` endpoint is certified by this note.  **[phase 134: and by the
resolution note in Section 3, no window of `zeta` is certified by the `zeta`
control either, in principle; positive Galerkin eigenvalues certify
nothing.]**

## 5. Reproduction

```text
cd scripts
python3 p124_013_schur_verify.py                  # regression + algebra, PASS
python3 p124_lab_sweep.py --model zeta  --refine 2 --tmin 0.5  --tmax 2.4
python3 p124_lab_sweep.py --model xi_a --a 0.35 --refine 2 --tmin 0.72 --tmax 1.8
```

A resolution-convergence study and an interval version are **not** part of
this note and would be required before any of Section 3 is cited as more than
a model observation.
