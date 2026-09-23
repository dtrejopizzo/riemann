# R153.001 — Builder, round 1 (phase 153): does the certified `log 2` endpoint carry sign?

*Builder of record: Claude Opus 5. Date 2026-09-19. Answers Q1, Q2, Q3 of `R153_000_LEAD_BLUEPRINT.md`.
Labels: `PROVED` / `RESTATEMENT` / `DIAGNOSTIC-NUMERIC` / `OPEN` / `REFUTED`. No sign is claimed for `ζ` at any
`T > log 2`.*

## 0. Sources actually read

`04-papers/42-arithmetic-lefschetz-programme/main.tex:4072-4300` (`eq:localizedprimitiveoperator`,
`lem:compactpolarpotential`, `lem:directedFeshbach`, `thm:certifiedendpoints`, `rem:yoshidacalibration`, the
retracted `½log5` endpoint) and `:6330-6360` (`τ_Γ = 0.2860886…`);
`certificates/row_d_log2/README.md`, `114_d_85_LOG2_FULL_SPACE_ENDPOINT_CERTIFICATE.md`,
`114_d_85_capacity_arb_prototype.py` (the stored binary64 `v₁`), `114_d_77_…`;
`03-research/phase-118-…/W4_CERTIFIED_RANGE.md` §§0–5; `03-research/phase-118-…/scripts/rowd_assembly.py`
(the operator assembly reused verbatim); Paper 46 `main.md` Proposition 12.6 and Remarks 12.4a′, 12.3c;
`R137_001` §3–§4, `R137_007` §1; phase 46 Doc 142 §GAP-142.A.

`python-flint` is **not importable** on this machine (`ModuleNotFoundError: flint`), so Tier 2 of the certificate
could not be rerun; per the blueprint I built my own Galerkin assembly (§1.3) on top of the corpus module
`rowd_assembly.py`, whose conventions are `main.tex`'s verbatim.

---

## 1. The `Ξ_a` operator, derived from Prop. 12.6, and the identity that governs everything

**Corpus check.** `grep -rIn "cosh(a t)\|polariz\|e^{at}F\|E_{-a}A" 03-research 04-papers` → hits only on
Definition 11.4's polarization (Paper 46 §11, `R135_003` LF3, `R135_004`); **no hit** on conjugating the
localized operator by `e^{±at}`. `grep -rIn "D.12-α"` → `R137_001:506,611,626`, `R137_003:566`, `R137_002:465`,
`R137_007:15,48` — the item is posed and endorsed, never computed. `grep -rIn "prime-blind"` → phase 14 only
(`M14.3`), a different question (Satake constancy). The construction below is new.

### 1.1 Definition

`Ξ_a(s) := Λ(s+a)Λ(s−a)`, `Λ = π^{−s/2}Γ(s/2)ζ(s)`, `a ∈ (0,½)`. Prop. 12.6's data for `Z = Ξ_a`:
`P = {−a, a, 1−a, 1+a}`, `θ = ½+a`, `c_n = Λ(n)(n^a + n^{−a})`, and the archimedean block is the product of the
two shifted blocks. Reading the explicit formula for `Ξ_a` in the coordinate `F(t) = e^{t/2}f(e^t)` exactly as
`main.tex` reads it for `Λ` gives

> **Definition 1.1.** For `F` supported in `I_T = (−T,T)`,
> `A_T^{(a)} = G^{(a)}_{Γ,T} − m_0^{(a)}I − Σ_{2≤n<e^{2T}} (Λ(n)(n^a+n^{−a})/√n)(S_{\log n}+S_{−\log n})`,
> where `G^{(a)} − m_0^{(a)}` is the multiplier operator with symbol
> `Σ_± [\mathrm{Re}\,ψ(¼ ± a/2 + iτ/2) − \log π]`, and
> `P_T^{(a)} = \{F : Φ_F(p) = 0,\ p ∈ P\} = \{F : ∫F(t)e^{βt}dt = 0,\ β ∈ \{±(½+a), ±(½−a)\}\}` (S1).

(For `a = 0` the symbol is `2[\mathrm{Re}\,ψ(¼+iτ/2) − \log π] = 2(g_Γ − m_0)` and the weights are `2Λ(n)/√n`,
i.e. `A_T^{(0)} = 2A_T` — the normalisation check the blueprint demands. `PROVED`, by inspection.)

**Normalisation at `a → 0` on the space, too.** The four exponents `±(½±a)` collide pairwise as `a → 0`, and
`P_T^{(a)} → \{F : M_∓F = 0 \text{ and } ∫F(t)\,t\,e^{∓t/2}dt = 0\} ⊊ P_T`: the `ξ²`-primitive space, with the
polar order doubled at `s = 0` and `s = 1`, exactly as the blueprint anticipated. So the `a → 0` limit of Q1 is
`2A_T` on a **codimension-2 subspace of `P_T`** — positivity there is *weaker* than `A_T ≥ 0`, not stronger.
`PROVED`.

### 1.2 Theorem A (the conjugation identity) — `PROVED`

> **Theorem A.** Let `E_a` be multiplication by `e^{at}`. Then, as quadratic forms on functions supported in `I_T`,
> ```
>      A_T^{(a)} = E_{−a} A_T E_a + E_a A_T E_{−a},
> ```
> equivalently, for every `F`,
> ```
>      ⟨A_T^{(a)}F,F⟩ = 2⟨A_T u, w⟩ · … = 2[ ⟨A_T u,u⟩ − ⟨A_T w,w⟩ ],   u = \cosh(at)F,  w = \sinh(at)F.
> ```
> Moreover `F ∈ P_T^{(a)} ⟺ e^{at}F ∈ P_T` and `e^{−at}F ∈ P_T ⟺ u ∈ P_T` and `w ∈ P_T`.

*Proof.* Write `G_± = e^{±at}F`, so `\hat G_±(s) = \hat F(s±a)`. (i) *Primes.* The bilinear prime part of `A_T`
gives `Σ_n (Λ(n)/√n)∫[G_+(t)G_-(t+\log n) + G_-(t)G_+(t+\log n)]dt =
Σ_n (Λ(n)(n^{a}+n^{−a})/√n)∫F(t)F(t+\log n)dt`, because `e^{at}e^{−a(t+\log n)} = n^{−a}` and symmetrically —
exactly the coefficients `c_n` of Prop. 12.6. (ii) *Archimedean.* `A_T`'s archimedean part is a convolution
kernel `κ` with `\hatκ = g_Γ − m_0`; the bilinear pairing of `G_+` and `G_-` produces
`∫∫κ(t−u)e^{a(t−u)}F(t)F(u)`, and symmetrising gives the kernel `2\cosh(a v)κ(v)`, whose Fourier transform is
`(g_Γ−m_0)(τ+ia) + (g_Γ−m_0)(τ−ia) = Σ_±[\mathrm{Re}\,ψ(¼±a/2+iτ/2) − \log π]` — Definition 1.1's symbol, the
Dirac part included (`2δ ↦ −2m_0`). (iii) *Poles.* `\hat G_+(0) = \hat F(a)`, `\hat G_+(1) = \hat F(1+a)`,
`\hat G_-(0) = \hat F(−a)`, `\hat G_-(1) = \hat F(1−a)`: the four conditions (S1) are precisely
`G_± ∈ P_T`. The polarisation `2⟨AG_+,G_-⟩ = ½[⟨A(G_++G_-),G_++G_-⟩ − ⟨A(G_+−G_-),G_+−G_-⟩]` with
`G_++G_- = 2u`, `G_+−G_- = 2w` gives the displayed form; `u,w ∈ P_T ⟺ G_± ∈ P_T` since the map is invertible. ∎

**Three immediate consequences.**

* **(A1) `PROVED`.** The `Ξ_a` Weil form on `P_T^{(a)}` is *not* a sum of two `ξ`-forms but their **cross term**.
  This is the structural reason `Ξ_a` can falsify: a positive-semidefinite form has no sign on off-diagonal
  entries. It also explains, without computation, why every "transport" of `A_T ≥ 0` to `A_T^{(a)} ≥ 0` must fail.
* **(A2) `PROVED`.** `A_T^{(a)} ≱ 0` on `P_T^{(a)}` **as soon as** there is `u ∈ P_T` with `\tanh(at)u ∈ P_T` and
  `⟨A_Tu,u⟩ < ⟨A_T(\tanh(at)u),\tanh(at)u⟩`. Since `|\tanh(at)| ≤ \tanh(aT) < 1` on `I_T`, this can only happen if
  `u` is *nearly null* for `A_T`: the falsifier feeds on near-nullity, i.e. exactly on the criticality that the
  `log 2` certificate documents (`v₁`, Rayleigh `≈ ±1.75·10^{−6}`, margin `8.63·10^{−8}`).
* **(A3) `PROVED`, archimedean convexity.** `Σ_±\mathrm{Re}\,ψ(¼±a/2+iτ/2) ≥ 2\mathrm{Re}\,ψ(¼+iτ/2)` for all
  `τ`, `a ∈ (0,½)`: with `h(x) = \mathrm{Re}\,ψ(¼+x+iτ/2) − ψ(¼+x)`,
  `h''(x) = −2Σ_k[\mathrm{Re}(¼+x+k+iτ/2)^{−3} − (¼+x+k)^{−3}] ≥ 0` because `\mathrm{Re}\,z^{−3} ≤ |z|^{−3}`.
  So the `Ξ_a` archimedean channel **gains** relative to `2×` the `ξ` channel, while the prime weights also grow
  (`n^a+n^{−a} ≤ 2.121` at `n=2`, `2.309` at `n=3`, `a=½`). Neither effect decides the sign; (A2) does.

### 1.3 Discretisation (all numerics below)

Piecewise-constant basis on the phase-118 mesh (`rowd_assembly.build_mesh`, `refine` cells per sub-interval);
`A_T` is `rowd_assembly.assemble`'s form matrix (Gamma channel = second differences of
`Ψ(D) = Σ_j e^{−a_jD}/a_j²`, `a_j = 2j+½`, head `j<400` exact + Euler–Maclaurin tail; shifts exact; `m_0` exact).
The four moment functionals are imposed **exactly** (cellwise `∫e^{βt}`), and the minimisation runs on an exact
null-space basis, so every reported `λ_min` is the minimum of a Rayleigh quotient over an **admissible** subspace
of `P_T` (resp. `P_T^{(a)}`) — hence an *upper* bound for the true infimum. `\cosh(at)`, `\sinh(at)` are replaced
by their exact cell averages (second-order). Scripts: `scripts/r153_q1_xi_a.py`, `scripts/r153_q1_astar.py`,
`scripts/r153_q2_mechanism.py`, `scripts/r153_q2b_shift_scan.py`. All labels `DIAGNOSTIC-NUMERIC`.

*Validation.* `λ_min(A_T|P_T)` at `T = \log2`: `2.014·10^{−1}, 7.47·10^{−2}, 2.41·10^{−2}, 7.47·10^{−3},
2.28·10^{−3}, 7.06·10^{−4}, 2.079·10^{−4}` for `refine = 4,8,16,32,64,128,256` (512 cells) — a clean
`O(h^{1.7})` decay to `0` with no positive plateau, i.e. the discretisation *reproduces the near-null direction*
of the certificate (whose true value is `∈ [0, ~2·10^{−6}]`). The minimiser is even (reflection overlap `+1.0000`)
at every refinement, matching `v₁` even, boundary-concentrated (W4 §2(e)).

---

## 2. Q1 — D.12-α at the certified endpoint: **the endpoint does carry sign** (diagnostically)

`λ_min(A_T^{(a)}|P_T^{(a)})`, `T = \log 2` (`scripts/r153_q1_xi_a.py`, `python3 r153_q1_xi_a.py` /
`run_fine.py`); in brackets the two pieces of Theorem A at the minimiser, `‖F‖=1`:

| refine (cells) | `a=0.10` | `a=0.30` | `a=0.45` | `a=0.49` |
|---|---|---|---|---|
| 32 (64) | `+3.324·10⁻²` | `+1.821·10⁻²` | `−4.334·10⁻³` | `−1.462·10⁻²` |
| 64 (128) | `+9.482·10⁻³` | `−6.172·10⁻³` | `−3.576·10⁻²` | `−5.302·10⁻²` |
| 128 (256) | `+2.115·10⁻³` | `−1.376·10⁻²` | `−4.831·10⁻²` | `−6.565·10⁻²` |
| 256 (512) | `+7.65·10⁻⁵` | `−1.585·10⁻²` | `−5.159·10⁻²` | `−6.894·10⁻²` |

At `refine=256`, `a=0.45`: `⟨A_Tu,u⟩ = 2.143·10⁻²`, `⟨A_Tw,w⟩ = 4.722·10⁻²`, `λ = 2(2.143−4.722)·10⁻² =
−5.159·10⁻²`. The negative values **stabilise** under refinement (they are upper bounds for the true infimum, and
they converge, not drift), while the positive value at `a = 0.10` collapses at the same `O(h^{1.7})` rate as
`λ_min(A_T|P_T)` itself. The mechanism is exactly (A2): at the minimiser `⟨A_Tw,w⟩ ≈ 0.097·a²` (measured:
`9.687·10⁻⁴` at `a=0.1`, `9.212·10⁻³` at `a=0.3`, `4.72·10⁻²` at `a=0.45`), essentially independent of the
discretisation, while `⟨A_Tu,u⟩ → λ_min(A_{\log2}|P_{\log2}) = 0^+`.

**Threshold `a*(T)`** (`scripts/r153_q1_astar.py`), the smallest `a` with a negative Galerkin value (an *upper*
bound for the true `a*`):

| `T` | `λ_min(A_T\|P_T)` (refine 256) | `a*` (refine 64 / 128 / 256) | `λ(a=0.45)` (refine 256) |
|---|---|---|---|
| `0.30` | `6.92·10⁻¹` | none / none / none | `+2.414` |
| `0.40` | `2.254·10⁻¹` | none / none / none | `+1.762` |
| `0.50` | `1.202·10⁻²` | none / none / none | `+1.449` |
| `½\log3 = 0.5493` | `1.108·10⁻³` | none / none / none | `+0.7857` |
| `0.60` | `2.53·10⁻⁴` | none / none / none | `+0.0825` |
| `\log 2 = 0.6931` | `2.079·10⁻⁴` | `0.2429 / 0.1446 / 0.1020` | `−0.0516` |

**Answers.**

* **`T = \log 2`: negativity is found**, robustly, for every `a ≳ 0.15`, with `a*` decreasing like `h^{0.85}`
  under refinement — consistent with `a*(\log2) = 0`, i.e. `A^{(a)}_{\log2} ≱ 0` for **every** `a ∈ (0,½)`, since
  the true `λ_min(A_{\log2}|P_{\log2})` is `0` to within `2·10^{−6}` while `⟨A_Tw,w⟩ ≍ 0.1a²`.
  `DIAGNOSTIC-NUMERIC`; the certified version is `OPEN` (§5).
* **`T = ½\log 3`: no negativity for any `a ∈ (0,0.499]`** — and not for the trivial reason. There the two extra
  constraints (`w = \tanh(at)u ∈ P_T`) push the minimiser far from the near-null direction:
  `⟨A_Tu,u⟩ = 4.97·10⁻¹` against `⟨A_Tw,w⟩ = 3.46·10⁻²` at `a = 0.45`. At `\log 2` the same two constraints cost
  almost nothing (`⟨A_Tu,u⟩ = 2.1·10⁻²`, and `1.3·10⁻³` at `a=0.3`), because `\log 2` carries a **near-degenerate
  low cluster** (`λ₁ = 2.079·10⁻⁴`, `λ₂ = 3.020·10⁻⁴` at refine 256) whereas `½\log3` does not
  (`1.11·10⁻³` vs `≫`). `DIAGNOSTIC-NUMERIC`.
* Therefore, **modulo the certificate of §5, D.12-α is answered affirmatively by `(S,T) = (\{∞,2,3\}, \log 2)`
  and not by `(\{∞,2\}, ½\log3)`**: the `log 2` endpoint distinguishes `ξ` from `Ξ_a` at finite `T`, and the
  corpus is, in that precise sense, ahead of Connes–Consani in substance and not only in range (CC's window
  `T = ½\log2` lies far inside the region where the table shows no negativity at all). It is **not** a sign for
  `ζ`: it is a sign-carrying *statement*, i.e. an inequality that is false for a falsifier with off-line zeros.

---

## 3. Q2 — the mechanism: the endpoint is **not** prime-blind (Outcome B)

`scripts/r153_q2_mechanism.py`, `python3 r153_q2_mechanism.py`. All `DIAGNOSTIC-NUMERIC`, `T = \log 2`,
refine 256 (512 cells) unless stated.

**(i) `A^{abs}`.** `λ_min(G_{Γ,T} − m_0 | P_T) = −1.5416·10⁻¹` (`−1.525·10⁻¹`, `−1.538·10⁻¹`, `−1.5416·10⁻¹` at
refine 64/128/256) and `2Σ_{n<4}Λ(n)n^{−1/2} = 2.248826`. Hence
`λ_min(A^{abs}_{\log 2}|P_T) ≤ −2.40298`. **Outcome A is refuted**: the archimedean channel does not dominate the
primes at `\log 2` — it is not even positive on `P_T` by itself. (At `½\log3`: `+8.268·10⁻²` against `0.980258`,
so `A^{abs} ≤ −0.8976`; also negative.) This is the local form of phase 46 Doc 142's GAP-142.A (absolute prime
control is `O(1)` and loses); the new content is that it already loses at the *certified* endpoint. `PROVED` in
the weak sense that a single admissible test vector certifies a negative Rayleigh quotient of `A^{abs}` once the
enclosure is redone in interval arithmetic; as printed, `DIAGNOSTIC-NUMERIC`.

**(ii) Sign flips and a generic contact.** `λ_min(·|P_T)` at `T = \log2`, refine 256:

| perturbation | `λ_min` |
|---|---|
| none (true data) | `+2.079·10⁻⁴` (`→ 0⁺`) |
| `Λ(3) → −Λ(3)` | `−2.5734·10⁻¹` |
| drop `n=3` | `−8.258·10⁻²` |
| `Λ(2) → −Λ(2)` | `−9.183·10⁻¹` |
| drop `n=2` | `−4.403·10⁻¹` |

and, replacing the **shift** `\log 3` by `b` (weight `Λ(3)/√3` unchanged, `scripts/r153_q2b_shift_scan.py`):

| `b` | 1.000 | 1.050 | 1.080 | 1.0900 | **1.0986123 = `\log3`** | 1.1006 | 1.120 | 1.200 | 1.380 |
|---|---|---|---|---|---|---|---|---|---|
| `λ_min` | `−0.1714` | `−0.0770` | `−0.0164` | `−0.00732` | **`+2.079·10⁻⁴`** | `−1.58·10⁻³` | `−0.0483` | `−0.1672` | `−0.0826` |

The curve `b ↦ λ_min(b)` has a **sharp isolated maximum at `b = \log 3`** (argmax within `3·10⁻⁴` of `\log3`;
half-width `≈ 2·10⁻³`; one-sided slopes `≈ +0.9` and `≈ −1.2`), and the maximum value is itself `0⁺`. So:

> **Outcome B.** At `T = \log 2` positivity on `P_T` is *tangential in the arithmetic data*: it is destroyed by a
> relative displacement of the second contact of order `10⁻³`, by dropping either contact, and by flipping either
> sign. The certificate is **not** Yoshida's Lemma 2 with constants: it is a three-channel cancellation
> (archimedean `+5.89·10⁻²`, `n=2` contact `+3.01·10⁻²`, `n=3` contact `+2.86·10⁻²` at the minimiser, refine 256;
> the three are `O(10⁻²)` and cancel to `2·10⁻⁴ → 0`), and the cancellation is exact only at the true
> `(\Lambda(2),\log2;\Lambda(3),\log3)`. `DIAGNOSTIC-NUMERIC`.

*Honest caveat.* The peak height at `b = \log3` tends to `0` under refinement, so the correct reading is **not**
"positivity has a margin at `\log3` and none elsewhere" but "the operator is exactly critical at `T = \log2`, the
critical point sits at the arithmetic contact, and every perturbation of that contact is first-order adverse."
Since a perturbed `b` no longer corresponds to *any* Weil form, a sceptic may call this "criticality plus
genericity"; what is not generic is the *location* of the maximum, which is `\log 3` to 4 digits, and which
therefore identifies the coupling `S_{\log2}`–`S_{\log3}` as load-bearing.

**(iii) The near-null direction's budget.** With `v₁` the Galerkin minimiser (even at every refinement), the
three channel values at `‖v₁‖=1` are refinement-*unstable* in their split (refine 64/128/256:
archimedean `−2.66·10⁻²`, `+1.53·10⁻²`, `+5.89·10⁻²`; `n=2`: `−1.176·10⁻¹`, `−3.98·10⁻²`, `+3.01·10⁻²`;
`n=3`: `+8.87·10⁻²`, `+5.44·10⁻²`, `+2.86·10⁻²`) while their sum is stable and `→ 0`. The direction rotates
inside a near-degenerate cluster; no single channel annihilates `v₁`. `DIAGNOSTIC-NUMERIC`. What is stable is the
*conclusion*: `|{\rm each\ channel}| ≫ |{\rm sum}|`, i.e. the endpoint lives on cancellation, not on domination.

---

## 4. Q3 — the delicate direction and `T`

**(i) Monotonicity. `PROVED`.** For `0 < T < T'`, extension by zero embeds `P_T ↪ P_{T'}` (the two moment
functionals are the same integrals), and for `F` supported in `I_T` every extra contact `\log n ∈ [2T, 2T')`
contributes `∫F(t)F(t+\log n)dt = 0` (disjoint supports), while the archimedean and polar parts are
support-blind. Hence `⟨A_{T'}F,F⟩ = ⟨A_TF,F⟩` on `P_T`, and
`λ_{\min}(T') = \inf_{P_{T'}} ≤ \inf_{P_T} = λ_{\min}(T)`: `T ↦ λ_{\min}(A_T|P_T)` is non-increasing. This is
`main.tex`'s nesting lemma made explicit for the eigenvalue. Continuity in `T` is
`RESTATEMENT` (Suzuki, `SuzukiScrew` Thm 1.4 — cited, not reproved). The same argument applies verbatim to
`A_T^{(a)}` on `P_T^{(a)}`, so `a ↦` negativity, once found at `T = \log2`, persists for all `T ≥ \log2`
(where nothing is claimed for `ζ`).

**(ii) Is `v₁` the minimal-archimedean-energy primitive function?** No, not to the accuracy available. The
overlap of the `A_T`-minimiser with the first eigenfunction of the compression of `g_Γ − m_0` to `P_T` is
`0.8549` (refine 128) and `0.8118` (refine 256) at `T = \log 2` — decreasing, i.e. `v₁` is *not* the prolate-type
archimedean ground state; at `T = ½\log3` the overlap is `0.9536`/`0.9535` — stable and much closer, consistent
with `½\log3` being the regime where CC's Sonin-space picture is adequate. `DIAGNOSTIC-NUMERIC`. This is a second,
independent signal of the same phenomenon as §3: `log 2` is arithmetic, `½log3` is (nearly) archimedean.

**(iii) Is D.76 `T`-uniform? `PROVED` (as a multiplier statement).** D.76 (`B = 320.5`, `c = B/4`) asserts
`Σ_{j≥160} E_{b_j} ≥ (B/4)E_B` for the Gamma-resolvent energies `E_b(F) = (1/2π)∫ \frac{2b}{b²+τ²}|\hat F(τ)|²dτ`.
Because both sides are integrals of `|\hat F|²` against explicit non-negative multipliers, the inequality is
implied by — and, being required for all `F`, equivalent to — the **pointwise** inequality
`Σ_{j≥160} \frac{2b_j}{b_j²+τ²} ≥ \frac{B}{4}\cdot\frac{2B}{B²+τ²}` for all `τ ∈ R`. That statement mentions
neither `T` nor the support, hence: **the capacity constant of D.76 is `T`-independent, and the capacity step of
the `log 2` certificate transfers verbatim to every `T`.** Consequently the `½\log5` obstruction is *not* in
D.76: it is exactly the two uncomputed cross terms `κ = ‖A_{QS}A_{SS}^{−1/2}‖²` and
`C_D = A_{DQ} − A_{DS}A_{SS}^{−1}A_{SQ}` of `main.tex:3990-4010` (W4 §3), i.e. the coupling of the five-dimensional
graph block to the *whole* complement. `PROVED` (the multiplier reduction) + `RESTATEMENT` (the `½log5` diagnosis).

---

## 5. What a `PROVED` answer to Q1 needs (the single remaining step)

By Theorem A, a certified `A^{(a)}_{\log2} ≱ 0` needs one explicit `u` supported in `I_{\log2}` with
`u, \tanh(at)u ∈ P_{\log2}` and interval enclosures giving

```
      ⟨A_T u,u⟩  <  ⟨A_T (tanh(at)u), tanh(at)u⟩ .
```

Both sides are computable with Arb balls in the corpus's own framework:

* the **upper** bound on the left is the quantity the certificate already produces for `v₁`
  (`−⟨v₁,A₀v₁⟩ < 1.746475·10⁻⁶` plus the positive tail, final margin `8.63386·10⁻⁸`), once `v₁` is corrected to
  satisfy the two additional moment conditions (a rank-2 correction; it costs `O(‖correction‖²)` in the Rayleigh
  quotient, and §2's tables show the cost at `\log2` is small);
* the **lower** bound on the right is the genuinely missing item. It is not supplied by `A_T ≥ 0` (which gives
  only `≥ 0`). It is, however, an ordinary directed computation: in the assembly used here
  `⟨G_{Γ,T}w,w⟩ = Σ_j [\tfrac{2}{a_j}‖w‖² − E_{a_j}(w)]` is a sum of **non-negative** terms, so truncation gives a
  rigorous lower bound, and the prime terms are exact overlaps. Target: `⟨A_T(\tanh(at)v₁),\tanh(at)v₁⟩ ≳ 0.1a²`,
  i.e. `≈ 2·10⁻²` at `a = 0.45` — five orders of magnitude above the left-hand side. The margin is enormous; only
  the bookkeeping is missing, and it needs `python-flint`, absent here.

Until that is done, Q1's answer is `DIAGNOSTIC-NUMERIC` and the acceptance test D.12-α remains formally `OPEN`.

---

## 6. Verdict table

| Question | Answer | Label |
|---|---|---|
| Definition of `A_T^{(a)}`, `P_T^{(a)}` from Prop. 12.6; `a→0` normalisation (`→ 2A_T` on the `ξ²`-primitive, codim-2 subspace of `P_T`) | done, §1.1 | `PROVED` |
| Theorem A: `A_T^{(a)} = E_{−a}A_TE_a + E_aA_TE_{−a}`; `⟨A^{(a)}F,F⟩ = 2[⟨A_Tu,u⟩−⟨A_Tw,w⟩]`, `u=\cosh(at)F`, `w=\sinh(at)F`, both in `P_T` iff `F ∈ P_T^{(a)}` | new; governs the whole question | `PROVED` |
| (A1) the `Ξ_a` form is the **cross term** of two `ξ` forms, never a sum of squares | §1.2 | `PROVED` |
| (A2) `A_T^{(a)} ≱ 0` whenever a near-null `u ∈ P_T` has `\tanh(at)u ∈ P_T` with larger energy | §1.2 | `PROVED` |
| (A3) archimedean convexity `Σ_±\mathrm{Re}ψ(¼±a/2+iτ/2) ≥ 2\mathrm{Re}ψ(¼+iτ/2)` | §1.2 | `PROVED` |
| **Q1 at `T = \log 2`**: is there `a` with `A^{(a)} ≱ 0` on `P^{(a)}_T`? | **yes**, for all `a ≳ 0.15` at the finest grid (`λ = −5.16·10⁻²` at `a=0.45`), with `a*(\log2) → 0` under refinement | `DIAGNOSTIC-NUMERIC` |
| **Q1 at `T = ½\log 3`** | **no**, for every `a ≤ 0.499` (`λ(0.45) = +0.786`); the four-moment space excludes the near-null direction there | `DIAGNOSTIC-NUMERIC` |
| D.12-α with `(S,T) = (\{∞,2,3\},\log2)` | affirmative modulo one interval certificate (§5) | `OPEN` (was `OPEN`) |
| `a*(T)` | `none` for `T ≤ 0.60`; finite and `→0` only at `T = \log2` | `DIAGNOSTIC-NUMERIC` |
| **Q2(i)** `A^{abs} > 0` on `P_T`? | **no**: `≤ −2.403` at `\log2`, `≤ −0.898` at `½\log3`; the archimedean form alone is `−0.154` at `\log2` | `DIAGNOSTIC-NUMERIC` (Outcome A **refuted**) |
| **Q2(ii)** sign flips / generic contact | positivity destroyed by all of them; `λ_min(b)` has a sharp isolated maximum at `b = \log 3` (argmax within `3·10⁻⁴`) | `DIAGNOSTIC-NUMERIC` (Outcome **B**) |
| **Q2(iii)** which operator nearly annihilates `v₁` | none; the three channels are `O(10⁻²)` each and cancel to `→0`; the split is refinement-unstable, the cancellation is stable | `DIAGNOSTIC-NUMERIC` |
| **Q3(i)** `T ↦ λ_min(A_T\|P_T)` non-increasing | zero extension + disjoint supports of the new contacts | `PROVED` (continuity: `RESTATEMENT`, Suzuki Thm 1.4) |
| **Q3(ii)** `v₁` = archimedean ground state? | no at `\log2` (overlap `0.855 → 0.812`, decreasing); nearly yes at `½\log3` (`0.9535`, stable) | `DIAGNOSTIC-NUMERIC` |
| **Q3(iii)** D.76 `T`-uniform? | yes: it is a pointwise multiplier inequality, support-free, hence `T`-independent; the `½\log5` wall is the two uncomputed cross terms, not the capacity | `PROVED` + `RESTATEMENT` |
| "The corpus is not ahead of CC in substance" (kill criterion) | **not triggered**: Q1 is positive and Q2 is Outcome B | — |

## 7. Open

1. **The interval certificate of §5** — one explicit vector, two enclosures, `python-flint` required. Until then
   D.12-α is not `PROVED`.
2. **`a*(\log 2) = 0`?** The extrapolation `a* ∼ h^{0.85}` is consistent with `0` but is an extrapolation. A
   theorem would follow from: `\inf\{⟨A_Tu,u⟩ : u,\tanh(at)u ∈ P_T, ‖u‖=1\} = 0` at `T = \log2`, i.e. the
   near-null direction survives the two extra moment conditions.
3. **Why `½\log3` does not carry sign** — is the obstruction structural (a genuine spectral gap in the
   four-moment space) or an accident of the near-null's shape? Q1's table poses it; nothing here answers it.
4. **The sharp maximum at `b = \log 3`** — is `\mathrm{argmax}_b λ_{\min}(b) = \log 3` exactly? A proof (or a
   refutation at the `10^{−4}` level) would turn §3 into a theorem about the endpoint.
5. **Beyond `\log 2`** nothing is claimed. Theorem A applies at every `T`, but `A_T ≥ 0` is certified only for
   `T ≤ \log 2`, and the `½\log5` cross terms (Q3(iii)) remain uncomputed.
6. **`Ξ_Q` (Epstein, T2) and Beurling (T3)** were not tested; Theorem A is specific to the two-shift structure of
   `Ξ_a` and does not transfer to them as written.
