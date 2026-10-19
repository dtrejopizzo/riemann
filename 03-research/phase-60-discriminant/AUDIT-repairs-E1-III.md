# Repair of the two points of maximum severity: E1 and III Audit → repair, pure mathematics. Frank: III is repaired as a clean conditional theorem;
E1 turns out MORE serious than the flag indicated (the recorded proof is false and the
correct one is non-trivial). --- ## E1 — real-rootedness: the recorded proof is FALSE (counterexample) and the correct one is hard ### The counterexample that kills the recorded proof `rh-proof.tex` Thm 3.1 says: *"with `ξ_k>0`, `f(s)=Σξ_k/(s−d_k)` goes `+∞→−∞` between consecutive
poles ⟹ one real root per gap."* The step uses **`ξ_k>0`**. But the real fundamental
eigenvector is **not** of definite sign (E12: 14–18 sign changes in dim 29–33,
because `v_0(k) ≈ u_k cos(ω*k+φ)`, edge carrier `ω*=0.966π`). **Concrete counterexample** that without `ξ_k>0` the argument fails: take `ξ=(−1,2,−1)` on
`d=(−1,0,1)` (even, with sign changes). Then
``` f(s) = −1/(s+1) + 2/s − 1/(s−1) = −2/(s³−s).
```
The numerator is the **constant `−2`**: `f` has **no** finite root. An even
vector with sign changes produces a secular function **with no real roots**. ⟹ The interlacing
argument **does not apply** to the real `ξ`, and real-rootedness **does not follow** from it. ### Why real-rootedness is nonetheless true — and why proving it is hard Empirically the roots ARE real (the engine reproduces the zeros of ζ). The true
structure: `ξ_k = u_k cos(ω*k+φ)` with `u_k>0` (positive envelope from H1) and edge
carrier `ω*≈0.966π`. Evaluating `ξ̂` on the lattice, `ξ̂(d_j)=ξ_j(L/2)(−1)^j`, which does **not
simply alternate** (near-Nyquist carrier) — so the old picture "one root per
gap" does not describe reality either. **The correct framework is Hermite–Biehler / de Branges:** a real entire function `ξ̂` has
only real zeros ⟺ it belongs to the HB class (⟺ `|E(s̄)|<|E(s)|` in the upper half-plane,
with `ξ̂` the real part of the structure function `E`). Real-rootedness must follow from
**the positivity of H1** (Perron–Frobenius, `Λ(n)≥0`) **translated into the HB property** — but: - H1 gives a positive eigenvector in the **de-modulated** representation (envelope `u_k>0`), not in the raw sinc basis.
- Connecting "PF-positivity of the envelope" to "HB of `ξ̂` (including the near-Nyquist carrier)" is **non-trivial** and **not done** in the program. ### Frank status of E1 after the audit
- Real-rootedness is **empirically true** and is **CCM Thm 1.1(iii)** given H1+H2 (hypotheses the program proved). But **the proof we recorded in the `.tex` is false** (counterexample above) — it was a mistaken oversimplification.
- The correct proof (HB/de Branges from the positivity of H1, with the edge carrier) **remains an open repair**. Until it is closed, E1 drops from ✅ to **🔧**: real-rootedness true, self-contained proof **pending** (or CCM Thm 1.1(iii) is cited as a black box, which is legitimate but is not "we proved it ourselves").
- **Impact:** E1 feeds Hurwitz (E3) and N5c. Both inherit the "🔧": they are correct **modulo real-rootedness**, which is true but whose own proof is missing. **Real severity: HIGH.** This is not an expository detail — it is that we do NOT have our
own proof of real-rootedness; we depend on CCM Thm 1.1(iii). We must (a) cite it
frankly as a black box, or (b) prove HB-from-H1 ourselves (real mathematical repair). --- ## III — relative stability: repaired as a clean CONDITIONAL THEOREM III was marked ✅ but rests on two unproved hypotheses. I repair it by stating it
correctly as conditional, with explicit hypotheses and checking that, **given
them**, the proof is correct. ### Why the absolute form fails (reminder)
Naive Davis–Kahan: `‖δξ̂‖ ≤ ‖δA‖/(ε_1−ε_0)`. But `ε_1−ε_0 ≈ 3ε_0 ≈ 10^{−20}`
(poly/exponentially small absolute gap) ⟹ useless bound. The renormalization `Â=A/ε_0` fixes it
**only if** the relative gap is `O(1)`. ### Theorem III (conditional, correct statement) **Hypotheses:**
- **(H-gap)** `inf_λ ε_1(λ)/ε_0(λ) = 1+γ` with `γ>0` (uniform relative gap). [= IV.1★]
- **(H-lim)** the renormalized ground states form a Cauchy family: `‖ξ̂_λ − ξ̂_{λ'}‖_{L²} → 0` as `λ,λ'→∞` (equivalently: `Â_λ` converges on the low block). [= Conj 2b] **Thesis:** `ξ̂_∞:= lim ξ̂_λ` exists and
``` ε_loc(λ) ≤ (C/γ)·√(logλ)·η(λ) + C λ³ e^{−πλ²},
```
with `η(λ):=‖Â_λ−Â_∞‖_{low}→0` the modulus of convergence. **Proof [P, given (H-gap)+(H-lim)]:** By (H-gap) the bottom of `Â_λ` is isolated with gap
`γ>0`; Davis–Kahan gives `‖ξ̂_λ−ξ̂_∞‖_{L²} ≤ η(λ)/γ`. Nikolskii (`‖g‖_∞≤C√(logλ)‖g‖_{L²}`,
`logλ` type) ⟹ `‖ξ̂_λ−ξ̂_∞‖_∞ ≤ (C/γ)√(logλ)η(λ)`. Adding `‖Ξ_T−Ξ‖≤Cλ³e^{−πλ²}` (Thm 1)
and, **if moreover `ξ̂_∞=Ξ`** (= IV.2, RH-equivalent), the bound on `ε_loc` is obtained. ∎ ### Frank status of III after the repair
- **(H-gap)**: only numerical (`ε_1/ε_0→4`). **Not proved.** It is IV.1★.
- **(H-lim)**: only numerical (relative spectrum converges). **Not proved.** It is Conj 2b.
- The thesis also uses **`ξ̂_∞=Ξ`** = IV.2, which is **RH-equivalent**.
- ⟹ III drops from ✅ to a **conditional theorem** `[(H-gap) ∧ (H-lim) ⟹ bound]`, with the bound useful only given IV.2 as well. **Frank:** III is correct as an implication; its hypotheses are not proved; it is not an unconditional theorem. **Repair achieved:** III is now **correctly stated** (conditional, explicit
hypotheses, valid proof given them). The **normalization** loose end (`ξ̂` up to scale vs
`Ξ`) is fixed here by requiring `‖ξ̂_λ‖_{L²}=1` and comparing against `Ξ_T/‖Ξ_T‖_{L²}` — the bound
`η(λ)` and `ε_loc` are understood with that common L² normalization. (This resolves the 🟠 loose end of
normalization for III/N2/Thm 2.) --- ## Summary of the two repairs | | before | after the audit/repair |
|---|---|---|
| **E1** | ✅ PROVED | **🔧 real-rootedness true but own proof FALSE**; correct one = HB/de Branges-from-H1 (open) or cite CCM Thm 1.1(iii) as a black box |
| **III** | ✅ PROVED | **CONDITIONAL theorem** `[(H-gap)+(H-lim) ⟹ bound]`, hypotheses only numerical; L² normalization fixed | **Lesson of the audit:** two ✅ drop to a frank status. E1 is the more serious one: we believed
we had real-rootedness proved and it turns out the recorded proof is refutable by a
counterexample; real-rootedness is true (CCM) but **proving it ourselves via
HB-from-positivity is real mathematical work still pending**. III is saved as a clean
conditional and along the way fixes the normalization.
