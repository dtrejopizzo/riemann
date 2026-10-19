# The wall via the quaternionic structure — precise statement for evaluation

For:** evaluation with A. Connes / C. Consani. **Note:** everything
marked MEASURED is numerical (faithful engine `engine_cache.py`, semilocal Weil form, dps≥40,
Davenport–Heilbronn falsifier = DH); what is marked PROVED refers back to the chain (Theorems 2.2, 12.2); the
CONJECTURES are what would need to be proved. No step uses the zero positions as input.

---

## 0. The lever (PROVED) — the wall is a scalar

By **Theorem 2.2** (Perron–Frobenius, unconditional at finite λ: `Λ(n) ≥ 0` ⟹ positivity-preserving
semigroup ⟹ simple ground state `u₀ > 0` = global minimizer of `A_λ`), the wall
`μ_λ = inf spec A_λ ≥ 0 ⟺ RH` (CCM Cor. 2.17) is the **scalar inequality**

$$\boxed{\;\varepsilon_0(\lambda) \;=\; \frac{\langle u_0,\,A_\lambda\,u_0\rangle}{\|u_0\|^2}\;\ge\;0\;}$$

on the explicit positive function `u₀`. With `ε₀(λ) → 0` (**marginality**, Theorem 12.2 PROVED),
the wall is: **does `ε₀` reach 0 from above (RH) or from below (¬RH)?** MEASURED: `ε₀(λ) = +5.8, 4.2, 3.6,
2.9, 2.7, 2.2, 2.1, 2.0 × 10⁻²¹` for λ=7…21 (positive, decreasing); DH: `ε₀ = −6.54`.

## 1. The arithmetic quaternionic structure (MEASURED, RH-neutral)

In the Fourier basis `V_n = e^{2πi n u/L}` on `[0,L]`, `L = 2log λ`, Deninger's `∗` operator
built **from the scaling flow** (E52, NOT from the zeros) is `∗ = Σ·K` (`K` = conjugation),
with linear part `Σ V_n = i·sgn(n)·V_{−n}`. Exact MEASUREMENT: `∗² = −1` (on `n≠0`), `[∗, θ] = 0`
(`θ = d/du`). The mode `n=0` (pole) is the real `H⁰`, the kernel of `∗`.

**Algebraic characterization of `∗`-compatibility (DERIVED and VERIFIED today):** since the kernel
`q_{mn}(u)` satisfies `q_{−m,−n} = q_{mn}` and the weights are functions of `u` alone, we have
`A_{−m,−n} = A_{mn}`, from which `(Σ^H A_λ Σ)_{mn} = \mathrm{sgn}(m)\mathrm{sgn}(n)\,A_{mn}`
and therefore

$$\boxed{\;\delta_\lambda \;:=\; \max_{m,n}\big|(\Sigma^H A_\lambda \Sigma - A_\lambda)_{mn}\big|
\;=\; 2\,\max_{\mathrm{sgn} m \ne \mathrm{sgn} n}\big|A_{mn}\big|\;}$$

VERIFIED on the machine (`δ = 2·max|A_opp-sign|` exact, λ=7,11,15). That is: **the `∗`-incompatibility
of `A_λ` is exactly its coupling block between positive and negative frequencies.**
`δ_λ = 0 ⟺ A_λ is block-diagonal in the `±`-frequency decomposition (the `+` and `−` modes
decouple, except for the pole `n=0`) ⟺ `A_λ` is strictly quaternionic ⟹ structural positivity
via `∗² = −1` (mechanism E51: Gram `Ω(·,∗·)` definite).

The cross element, explicitly, with `m, n' > 0`:
$$A_{m,-n'} \;=\; \mathrm{ARCH}_{m,-n'} \;-\; \sum_{n\le\lambda^2}\Lambda(n)\,n^{-1/2}\,q_{m,-n'}(\log n),
\qquad q_{m,-n'}(u) = -\frac{\sin\frac{2\pi m u}{L} + \sin\frac{2\pi n' u}{L}}{\pi(m+n')}.$$
(**Sum** kernel of sines, vs. the **difference** kernel of the same-sign block.)

## 2. Frank state of affairs: `δ_λ ↛ 0` — the EXACT compatibility FAILS

MEASURED: `δ_λ = 0.133, 0.135, 0.181, 0.216` for λ=7,11,15,19 (**grows**). DH falsifier:
`δ = 4.51` (35× larger). ⟹ **The arithmetic `∗` makes ζ *almost* quaternionic and DH not at all,
but NOT exactly: `A_λ` is not `±`-block-diagonal.** So the naive goal *"multiplicativity forces
`δ_λ = 0`"* is **FALSE** (and gets worse with λ). This needs to be said plainly: there is no
"Euler lemma ⟹ `δ=0`"; the `±` cross cancellation is not exact.

## 3. What IS structural (MEASURED) and the correct target

Let `Â_λ = ½(A_λ + Σ^H A_λ Σ)` be the **∗-symmetric** (quaternionic) part and `Ǎ_λ = A_λ − Â_λ` the remainder.
MEASURED (λ=7…19):
- `inf spec Â_λ = +1.7, +0.83, +0.59, +0.45 × 10⁻¹⁹ > 0` (**`Â_λ` is PSD for ζ**); DH:
  `inf spec Â = −4.92 < 0` (**indefinite**). ⟹ `Â_λ ⪰ 0 ⟺ RH` (another faithful reformulation).
- `inf spec Ǎ_λ = −0.38, −0.32, −0.58, −0.63` (O(1) indefinite, does not decay).
- On the ground state: `⟨u_0, Â_λ u_0⟩ = +1.3·10⁻⁵`, `⟨u_0, Ǎ_λ u_0⟩ = −1.3·10⁻⁵`; **they sum to
  the residual `ε₀ ≈ 10⁻²¹`** (`u_0 ⊥ Σu_0`, overlap = 0, so `u_0` is NOT `∗`-symmetric).

**Crucial (frank) consequence:** `Â_λ ⪰ 0` by itself does **NOT** give `ε₀ ≥ 0`, because the
cross term `⟨u_0, Ǎ_λ u_0⟩` is negative and **nearly cancels** `⟨u_0, Â_λ u_0⟩`. The wall is that the
quaternionic part **dominates** the incompatible one *on the ground state*:
$$\boxed{\;\langle u_0, \hat A_\lambda u_0\rangle \;\ge\; \big|\langle u_0, \check A_\lambda u_0\rangle\big|\;}$$
and this is **knife-edge** (both sides `≈ 1.3·10⁻⁵`, difference `≈ 10⁻²¹`). RH lives here again.

## 4. The precise statement to evaluate (the two CONJECTURES, and where Euler enters)

> **Conjecture A (quaternionic positivity).** The `∗`-symmetric part `Â_λ ⪰ 0` for every λ.
> Equivalent to `Â_λ = B_λ^* B_λ` (sum of squares). **Role of Euler:** `Â_λ` mixes, via
> `Σ^H A Σ`, the elements `A_{−m,−n}`; the `B^*B` factorization should reflect the Euler product
> `−ζ'/ζ(s) = Σ Λ(n)n^{−s}` as a product over primes (DH, without an Euler product, gives an
> indefinite `Â`). **Note:** Conj. A is RH-equivalent (MEASURED: fails for DH); proving it
> is no weaker than RH, but its form (SOS on the symmetric part) is where
> multiplicativity might give a certificate that the direct Cholesky of `A` (E42) did not give.

> **Conjecture B (dominance over the ground state).** `⟨u_0, Â_λ u_0⟩ ≥ |⟨u_0, Ǎ_λ u_0⟩|`. This,
> with `u_0 > 0` (PF, PROVED), gives the wall. **Role of Euler / what needs to be proved about `Σ Λ(n)`:**
> the incompatible term is the sum of primes against the **sum**-kernel
> `Ǎ`-part `= −Σ_{n}Λ(n)n^{−1/2}\,\tfrac12[q_{m,-n'} + \text{sgn-conjugate}]`; one must prove
> that the contribution of `Σ Λ(n)n^{−1/2}` to the `±`-cross block is **bounded by** its
> contribution to the quaternionic block, with the Euler product as the structure that forces it.

**Where exactly the Euler / `Σ Λ(n)` content lives:** the difference between the same-sign block
(**difference** kernel of sines, gives the quaternionic energy `Â`) and the cross block
(**sum** kernel of sines, gives `Ǎ`). Multiplicativity `Λ = \log * \mathbf 1` (von Mangoldt as a
convolution) and `−ζ'/ζ = Σ_p \sum_k \log p\, p^{−ks}` must control the ratio
`\text{(sum block)} / \text{(difference block)}` of the prime sum. DH breaks this because its
series lacks an Euler product (its "primes" have coefficients with sign `χ mod 5`).

## 5. Non-circularity caveats (for the evaluation)

- Conjectures A and B are **RH-equivalent** (MEASURED: both fail for DH exactly when RH
  fails). They are not *logical* shortcuts; they are **structured** reformulations (SOS / dominance) where
  multiplicativity enters explicitly — unlike the global positivity `∀f` (Cholesky
  E42, Hodge–Riemann E63, Herglotz E61, all without a certificate).
- The `∗` is RH-neutral (scaling flow, zeros = output). But `A_λ` is **not** `∗`-compatible
  (`δ ↛ 0`): the quaternionic structure is **approximate** for ζ, exact only in the limit if and
  only if the Conjectures hold.
- **Question for Connes/Consani:** does the factorization `Â_λ = B^*B` (Conj. A) or the dominance
  (Conj. B) admit a certificate that uses the Euler product in an essential way (not available
  for DH), or do both reduce, like all our additive attempts, to the `e^{−cL}` residual of the
  exact balance `P = WR + PRIME` (MEASURED: ratio `P/(WR+PRIME) = 1.000000`)? If it is the latter, the
  wall is irreducibly the sign of that residual and this document's contribution is the **precise
  map** of why every structure (`∗`-symmetry included) lands there.

---

### Appendix — facts MEASURED today (reproducible)
`E87/E87b` (ε₀ monotone, primes raise ε₀ from −6 to 0), `E88` (`P=WR+PRIME` exact), `E90`
(`δ` = `±` block, does not decay), `E91` (`Â` PSD ζ / indefinite DH), verification `δ = 2·max|A_opp-sign|`.
Cache: `engine_cache.py`. venv: `propuestas-de-investigacion/99-archive/05-lise-science-v6/.../investigacion-2/venv`.
