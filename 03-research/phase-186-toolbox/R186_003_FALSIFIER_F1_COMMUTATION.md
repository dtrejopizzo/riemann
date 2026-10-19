# R186.003 — Falsifier F1: does W_{λ,S} commute with P^S_λ? (S = {∞,2})

Pure mathematics; a single high-precision computation (30 digits) marked NUMERICAL.
Sources: [CCM] arXiv 2310.18423v2 (`mainc2m24fine.tex`, line numbers cited); [CM] PNAS 2022; R186.002.
Scripts: `f1.py`, `f1_exact.py` (sympy, exact), `f1_e2.py`.
Only one commutation statement is decided.

## Status

| # | Statement | Label |
|---|---|---|
| 1 | Explicit model: L²(X_S)^{K_S} ≅ L²(ℝ_+, du), 𝔰 = −i(u∂_u+½), **P^S_λ = 1_{(0,λ]}(u)**, ξ_S = h_S(u) = Σ_{n≥0} e^{−π4^n u²} | PROVED (from [CCM] l. 727–790) |
| 2 | Green's lemma: for real e_i, e_j of the kernel, ⟨[W,P^S_λ]e_i,e_j⟩ = λ²[ (e_i e_j′ − e_i′ e_j)(λ) + (c_j − c_i) ∫_0^λ e_i e_j du ] | PROVED |
| 3 | Case S = {∞}: the (0,1) element vanishes ∀λ ⟺ c₁ − c₀ = 8π (= CCM normalization 2π(4N+1)) | PROVED (exact) — reproduces the Slepian miracle [CM Thm 1.6(ii)], CITED |
| 4 | **S = {∞,2}: ⟨[W_{λ,S}, P^S_λ]e₀,e₁⟩ ≢ 0 for EVERY affine normalization** (aW+b, c_S(N) = αN+β, shifts 𝔰 ↦ 𝔰+t) | **PROVED (exact) — NO-GO of the CCM candidate l. 841–843** |
| 5 | Even with arbitrary c_S(N) (non-affine, λ-dependent), the elements (0,1),(1,2),(0,2) are inconsistent at λ = ½ and λ = 1 | NUMERICAL (30 digits; defect 0.18 and 0.006) |
| 6 | Metaplectic candidate (CCM l. 270, §metasect l. 1101): setup and next lemma | OPEN |

## 1. The explicit model (PROVED from CITED)

* X_S = (ℝ × ℚ₂)/Γ, Γ = {±2^n}. Fundamental domain of C_S: ℤ₂^* × ℝ_+^* [CCM l. 729].
 A K_S-invariant function is a function h(u) of u > 0. At the point (1, u) the module is
 |x|_S = |1|₂·u = u [CCM eq. (module)]. Hence **P^S_λ = multiplication by 1_{(0,λ]}(u)**:
 it is *the same* cutoff as in the archimedean case.
* w_S h = u^{1/2}h(u) on L²(ℝ_+^*, d^*u) [CCM eq. (essl0)], so the norm is ∫_0^∞ |h|² du.
* 𝔰 generates the archimedean scale: 𝔰 = −i(u∂_u + ½) (CCM l. 837). −𝔰² = (u∂+½)² = ∂(u²∂) + ¼.
* ξ_S = η_S(e^{−πx²}) restricted to the domain: **h_S(u) = Σ_{n≥0} e^{−π 4^n u²}** [CCM l. 735]
 (irrelevant global constants).
* N_S = grading of E_n = span{𝔰^j ξ_S : j ≤ n} [CCM l. 827; def prolop l. 300 approx.].
 Basis: e₀ = h_S/‖h_S‖, e₁ = (u∂+½)h_S/‖·‖ (= i𝔰ξ_S normalized; orthogonal to e₀ because dm_S is even),
 e₂ = Gram–Schmidt of (u∂+½)²h_S against e₀. All real.
* Lemma 2.1 of R186.002 (F_S = (−1)^{N_S}) matches [CCM Prop z2grad + httransfoS(ii)]: the
 grading is unique and equals exp(iπN). Checked against the source: CITED.
* W_{λ,S} = −𝔰² + λ² c(N_S), c(n) = αn + β (affine normalization; α = 8π, β = 2π, −¼ aside, gives W_λ).

Structural remark. In this model −𝔰² and P^S_λ are literally the archimedean ones; everything
semilocal lives in N_S. By [CM] [W_λ,P_λ] = 0, so
[W_{λ,S}, P^S_λ] = λ²[c(N_S) − 8πN_∞, P_λ]: the candidate commutes iff the difference of Hermite
numbers (semilocal − archimedean) commutes with the cutoff.

## 2. Green's lemma (PROVED)

For real, smooth, decaying f, g: ∫_0^λ (f ∂(u²∂g) − ∂(u²∂f) g) du = λ²(f g′ − f′ g)(λ)
(the boundary u = 0 vanishes: u²·(f g′−f′g) → 0 because h_S ~ log(1/u)/log 4 and u h_S′ = O(1)).
Since W is symmetric on the kernel and N e_j = j e_j:

 E_{ij}(λ) := ⟨[W,P]e_i,e_j⟩ = ⟨Pe_i, We_j⟩ − ⟨We_i, Pe_j⟩ = λ²[ W_{ij}(λ) + (c_j−c_i) J_{ij}(λ) ],
 W_{ij} = e_i e_j′ − e_i′ e_j, J_{ij} = ∫_0^λ e_i e_j du.

Freedoms: aW + b multiplies E by a; β cancels; the shift 𝔰 ↦ 𝔰 + t adds
−2t[𝔰,P] whose (0,1) element is t·i·λ e₀e₁(λ)·(real), purely imaginary relative to the
previous part (which is real). Hence E₀₁ = 0 requires t = 0 and **W₀₁ + α J₀₁ ≡ 0 in λ**. Sole unknown: α.

## 3. Exact decision (PROVED)

Let F(λ) := W₀₁(λ) + αJ₀₁(λ). If E₀₁ ≡ 0 then F′ ≡ 0, and
 n₀n₁ F′(u) = Σ_{n,m≥0} B(f_n, L f_m), f_n = e^{−π4^n u²}, L = u∂+½, B(f,g) = f g″ − f″ g + α f g.

Symbolic computation (`f1_exact.py`):
* General pair (a,b): B(f_a, Lf_b) + B(f_b, Lf_a) = e^{−(a+b)u²}·[−8(a³+b³−a²b−ab²)u⁴ + (20a²+20b²−8ab−2α(a+b))u² + α − 4(a+b)].
* **S = {∞}** (only n = m = 0): B(f₀,Lf₀) = −½(α − 8π)(4πu² − 1) e^{−2πu²}. Vanishes iff α = 8π.
 Together with F(∞) = 0 (e₀ ⟂ e₁ and decay), F ≡ 0: **Slepian reproduced exactly**.
* **S = {∞,2}**: the exponents (4^n + 4^m)π are 2π (only (0,0)), 5π (only (0,1),(1,0)), 8π, ….
 Functions e^{−cu²}·polynomial with distinct c are linearly independent (compare
 asymptotics as u → ∞; the tail c ≥ 8π is O(e^{−8πu²}u⁴) uniformly, the series converges with its
 derivatives). The coefficient of e^{−2πu²} forces α = 8π. With α = 8π the coefficient of e^{−5πu²} is

 **−12π(30π²u⁴ − 19πu² + 1) ≢ 0.**

 So F′ ≢ 0 for every α, and **E₀₁ ≢ 0 for every affine normalization. NO-GO PROVED.** ∎

Values (NUMERICAL, `f1.py`, 30 digits): α*(λ) := −W₀₁/J₀₁ — the α that would make E₀₁ vanish at a given λ.
| λ | S = {∞} | S = {∞,2} |
|---|---|---|
| 0.25 | 25.1327412287183459077011470662 (= 8π) | 23.2867688268675264273532039985 |
| 0.5 | 8π | 17.5843406999514924766588654332 |
| 1 | 8π | 25.0814885858886709212345433599 |
| 1.5 | 8π | 25.1327402883549632187587079811 |
| 2 | 8π | 25.132741228718229311821839107 |
Example: λ = 1, α = 8π: E₀₁/λ² = W₀₁ + 8πJ₀₁ = −0.0228367887855… + 8π·0.000910503724980… ≈ −4.67·10^{−5} ≠ 0.
α*(λ) → 8π as 8π − O(e^{−3πλ²}·poly) (the 5π term crossing the leading 2π term): the
defect is invisible for large λ and of order 1 for λ ≲ 1, precisely the window λ = 1 of [CC].

## 4. Stronger result: not even an arbitrary c(N) works (NUMERICAL)

If c(N_S) is allowed to be arbitrary (even λ-dependent), each pair fixes c_j − c_i = −W_ij/J_ij and
consistency requires d₀₂ = d₀₁ + d₁₂ (`f1_e2.py`):
| | d₀₁ | d₁₂ | d₀₂ | defect |
|---|---|---|---|---|
| ∞, λ=½ and 1 | 8π | 8π | 16π | < 10^{−27} |
| {∞,2}, λ=½ | 17.584340699951492505 | 10.08362393373399613 | 27.84875827005571738 | **0.1808** |
| {∞,2}, λ=1 | 25.081488585888676199 | 25.424653259050284513 | 50.512145796614846492 | **0.0060** |
No function of the number N_S, added to −𝔰², commutes with P^S_λ (at λ = ½, 1). Making this
PROVED only requires the same exponent-expansion argument of §3 with e₂ (pending; the defect is 10^{25}
times the precision).

## 5. What remains: the metaplectic candidate (OPEN)

CCM (l. 270) only announces the version with the Weil representation of Mp(SL₂(𝔸_S)); in
§metasect (l. 1101–1150) is the archimedean version: ϖ(h) = x∂+½, ϖ(e₊) = iπx²,
ϖ(e₋) = (i/4π)∂², ϖ(k) = πx² − ∂²/(4π). Since 2π(4N+1) = 4π·ϖ(k)·… on L²(ℝ)^{ev}, the number N
is expressed with **x² and its conjugate under F** (−∂²/(4π²) = F x² F^{−1}); this matches
[CCM Rem. care (ii)]. The exact expression of W_λ in the enveloping algebra is in [CCM §metasect];
it is not reproduced here.

Semilocal candidate in the model of §1:
 W^{mp}_{λ,S} = −𝔰² + λ²·κ(π u² + F_S π u² F_S^{−1}) + const,
where u² = |x|²_S is a multiplier (trivially commutes with P^S_λ) and F_S is the semilocal Fourier
transported to the u-model (Mellin: multiplier L_S(½−is)/L_S(½+is)·γ_∞(s)). By [CCM Rem care (iii)]
|x|²_S η_S ≠ η_S|x|², so W^{mp} ≠ W_{λ,S}: it is a genuinely different candidate.

**Next lemma L1^{mp} (OPEN).** Compute ⟨[W^{mp}_{λ,S}, P^S_λ] e₀, e₁⟩. Since u² commutes with P,
it reduces to ⟨[−𝔰² + κλ² F_S u² F_S^{−1}, P] e₀,e₁⟩; the missing ingredient is the explicit form
of F_S u² F_S^{−1} in the u-model (a second-order operator "in Mellin" with the factor
(1−2^{−½∓is}), i.e. a combination of ∂² with dilations by 2). Expected: it fails by the
same locality argument of R186.002 §2.2 unless the dilations cancel at the boundary u = λ.

## Audit notes

1. **The model.** Check that at the representative (1,u) of the fundamental domain the module is u
 and that P^S_λ = 1_{|x|_S ≤ λ} [CCM Prop groundstate (ii)] is exactly 1_{(0,λ]}(u). The whole
 result depends on this; if P^S_λ were defined otherwise, F1 must be redone.
2. **Symmetry and domain.** e_i ∈ polynomial kernel; P e_i is not in the domain of 𝔰², but only
 the form ⟨Pe_i, We_j⟩ − ⟨We_i, Pe_j⟩, which is well defined, is used. Boundary u = 0: h_S has a
 logarithmic singularity; u²(f g′ − f′ g) → 0. To be verified.
3. **Linear independence in §3.** The argument uses an infinite sum; the tail is dominated
 uniformly (terms O(2^{−n}) and derivatives). Check that no other pair (n,m) gives 4^n+4^m = 5.
4. **Normalizations.** The Haar constants, ‖h_S‖ and the phase of e₁ only rescale E₀₁: they do
 not affect "≡ 0".
5. **Scope.** NO-GO for W = −𝔰² + λ²(αN_S+β) (with aW+b and 𝔰+t). The claim with arbitrary c(N)
 is NUMERICAL. No other candidate is ruled out (metaplectic, or −𝔰² replaced by another
 function of 𝔰). No sign is claimed.
6. **Consistency with [CM].** The test reproduces α = 8π for S = {∞} with defect < 10^{−27}; this
 validates the model and Green's lemma.

## Note (R186_092)

* NO-GO F1 PROVED with scope "(α,β) constants independent of λ"; the case α=α(λ) is only NUMERICAL (defects 0.1808 / 0.0060 reproduced). Model confirmed against CCM l.720–850; coefficient of e^{−5πu²} recomputed.
</content>
