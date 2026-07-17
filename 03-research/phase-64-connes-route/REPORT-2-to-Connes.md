# Second report: your route, validated end-to-end — and where we now need a direction for RH

*Following your second reply (de Branges–Livšic colligation, shifted scattering `Θ_ω`, positive
reference, contractivity→no-pole, detector nonvanishing). Honest throughout: every positive result
for ζ is **marginal** (a faithful detector), flagged as such; all marginal claims checked at dps≥40
(float64 is insufficient at the boundary — see the audit note). Davenport–Heilbronn (DH) and planted
off-line zeros are the falsifiers and break every test at the predicted location.*

---

## 1. Everything you proposed checks out on the genuine ζ

| object (your sections) | test | result |
|---|---|---|
| §1 de Branges kernel `K_κ`, `E_κ=Ξ'−iκΞ` | Gram PSD (dps=40) | **ζ genuinely PSD** (rel margin `+3.4e-14`, κ=1,5,20); off-line **fails** |
| Herglotz `m=−Ξ'/Ξ` | `Im φ≤0` on `ℂ_+` | **ζ Herglotz**; archimedean part **alone is not** (it is the on-line zeros that restore it); off-line breaks it |
| §7 shifted scattering `Θ_ω`, **Pick matrix** | interior passivity, `ω↓0` | **ζ Pick-PSD for all ω down to 0.002**; off-line **fails exactly at `ω*=β−½`** (confirmed β=0.55,…,0.90) |
| §3 Tate factorization (`ω>½`) | `Θ_ω=Θ_∞∏_pΘ_p`, passivity | factorization confirmed; assembled product **passive** |
| §6 detector nonvanishing | DH growth exponent | bulk Jacobi functionals: ζ bounded (`≈0`), DH grows `≈2β−1` |

Two findings we want to flag specifically:

- **(A. the regularized continuation exists and is positive.)** The *absolute* margin → 0 as `ω↓0`
  (the de Branges space degenerates at the critical line), **but the relative/regularized margin
  `r(ω)=min/max` converges to a positive constant** `R≈6.1e-8` for ζ on every fixed configuration
  (E107). So your "regularized continuation to `ω=0`" is realized: `lim_{ω↓0} r(ω)` exists and is
  `>0`. `R` is configuration-dependent (the inf over configurations → 0, the boundary degeneracy);
  the invariant RH statement is `r(ω)≥0` for **all** configurations.

- **(B. the Tate factors are passive only collectively.)** The scalar local factors `Θ_p` are
  unimodular on `ℝ` but **not individually inner** (`|Θ_p|>1` occurs); passivity is a property of the
  **`J`-unitary matrix colligation product**, not the scalar factors. So the restricted product must
  be assembled at the matrix level — which matches your "restricted tensor product of local Tate
  *colligations*".

We have written the resulting RH-strength statement as **Theorem 3** in
`THEOREM-adelic-colligation.md`: the unconditional `ω>½` colligation + boundary unitarity (U,
functional equation) are in hand; the open crux is **interior passivity (P) continued to `ω=0`** =
positivity of the critical de Branges kernel = RH.

---

## 2. The precise gap, in your language

We have rigorously / unconditionally:
- the conservative unitary colligation for `ω>½` (Tate/Euler restricted product);
- boundary unitarity `S_κ^*S_κ=1` on `ℝ` (functional equation);
- the equivalences `RH ⟺ K_κ⪰0 ⟺ m` Herglotz `⟺ Θ_ω` passive `∀ω⟺ R≥0`.

The single missing statement is the **continuation of positivity** from the safe region `ω>½`
through `ω↓0`: that the positive Gram structure (no `ℂ_+` poles for `ω>½`) is **preserved** to the
critical value. An eigenvalue of the Gram/Pick kernel can cross 0 only at an off-line-zero pole; DH
exhibits exactly such a crossing at `ω=β−½`. So the theorem is a **no-crossing / monotone-continuation
of passivity**, powered by the Euler product (which DH lacks).

---

## 3. Our questions — where to push for RH

We can build and falsify-test any concrete construction at dps≥40. We would value your direction on:

1. **Which mechanism for (P)?** Of the three we see —
   (i) an **arithmetic index / Riemann–Roch positivity** identifying `R` (or a regularized relative
   determinant against the PNT model `K^0`) with a manifestly `≥0` index;
   (ii) a **no-eigenvalue-crossing / operator-monotone continuation** of the Gram structure on
   `(0,∞)` using passivity to forbid a crossing from the safe region;
   (iii) a **restricted-tensor passivity theorem** (each local Tate colligation passive on the adelic
   `L²`, product preserves passivity in the limit) —
   which is the right primary route, and is any of them reducible to a statement we could test
   numerically (e.g. a finite-prime truncation of (iii), or a sign/monotonicity invariant of (ii))?

2. **The index (your `μ_max=1`).** Is the marginal `μ_max=1` (boundary norm-one) the **index-zero**
   case of a Riemann–Roch/Euler-characteristic identity on the arithmetic site, and is there a
   **positivity of that index** (a Hodge-index/Castelnuovo analogue over Spec ℤ) that would force
   `R≥0`? This is exactly the point where our program has repeatedly hit the absence of a Weil
   cohomology over Spec ℤ (our "MW-5"). Does the adelic colligation give that positivity *without*
   needing the full cohomology — i.e. as a **scattering/passivity** statement rather than a
   geometric intersection one?

3. **A finite, falsifiable sub-theorem.** Is there an intermediate **unconditional** statement,
   stronger than `ω>½` but short of RH, that the colligation should satisfy — e.g. passivity of the
   restricted product down to some explicit `ω_0<½` (a zero-density / zero-free-region analogue), or
   passivity of a **finite-prime** colligation against the archimedean factor — that we could prove
   and that would be a genuine step, with DH failing it?

4. **Where exactly must the Euler product enter?** In (P), the only DH-distinguishing input is
   multiplicativity. Is the cleanest entry point the **restricted tensor product structure** of the
   colligation (so that passivity is multiplicative over places), or the **positivity of the local
   Tate Gram kernels** assembled adelically? In other words: is RH here a statement about the
   *product* of passive local pieces, or about the *positivity of each local piece on the right
   Hilbert space*?

We are ready to implement and falsify-test whichever direction you point to.

*Files:* `phase-64-connes-route/` — E103 (Herglotz), E104 (Pick `ω↓0`), E105 (Tate factorization),
E106 (de Branges kernel), E107 (regularized continuation margin), AUDIT.md,
THEOREM-adelic-colligation.md; first report `REPORT-BACK-to-Connes.md`.
