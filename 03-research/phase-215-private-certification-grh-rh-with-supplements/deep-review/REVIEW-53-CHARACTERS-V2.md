# Independent review of the characters of P53, corrected version

Date: 2026-11-28. Source: `04-papers/53-covolume-theorem-exchange-identities-chain-determinant/main.tex`, SHA256 `ef430fe477fe53621578202a8f735b31933cba5f6299e35b6ec5c429df2d1d5a`. The diff was read and the passages indicated were reconstructed; no papers were modified. The verdicts here are limited to the tensor identity, its three applications, the computation of scalars and the propagation of this question. They do not by themselves constitute a new certification of all the analytic lemmas of P53.

## Result and rectification of the previous report

The modification of `pcu:product` **corrects the character problem**, also in the actual application of `pcu:period` and `pcu:coeff`. No equal-rank period weighted by an additional character remains. The applications in integrability (line 4119) and `pct:vantop` (5655) are also compatible with the new formula. For this version, the propagation of the former character error to MAP-53, non-vanishing and exchange is withdrawn.

There is an independent precision: the explicit scalar `κ₀` of line 3631 omits, with the printed formula (U2), the fixed positive factor `|det(s₀x_U)|_f^j`. The reconstruction gives the complete adelic modulus. This requires correcting that intermediate formula; **it does not invalidate the existential statement of `pcu:coeff`, nor introduce dependence on the modulus/twist, nor change the calibrated quotients of exchange**. Both the computation and the scope of this correction are detailed below.

| Obligation | Localised verdict |
|---|---|
| `pcu:product`, 3347–3370 | (a) corrected identity, reconstructed directly |
| `pcu:period`, 3387–3435 | (a) characters and archimedean constant exact, under the slice/vacuum properties cited there |
| `pcu:coeff`, cancellation of characters, 3622–3648 | (a) reconstructed, including the two components of each split place |
| Explicit formula for `κ₀`, 3631 | (b) the finite modulus is missing unless the additional normalisation `|d₀|_f=1`, not imposed, holds; explicit correction below |
| Statement of `pcu:coeff` | (a) reconstructed after that fixed correction; do not assert that the intermediate formula is correct as written |
| Application of `product` in integrability, 4119 | (a) characters compatible; its use in absolute values leaves no growth factor |
| Application of `product` in `pct:vantop`, 5655 | (a) the equal-rank factor is exactly the one that the hypothesis annihilates |
| Propagation to `P-top` and calibration `twice` | (a) inference reconstructed, conditional on the other inputs of those propositions, audited separately |

## 1. Conventions and product

By 1732, `ω_{α,β}(g,h)=α(det g)^{-1}β(det h)ω_Hom(g,h)`. The corrected formula is

`vartheta^{αα′,β}_{f⊠F}(g,y⊕l)=vartheta^{α′,β}_{f}(g,y) θ^{W₀,W₀}_{α,β}(g,l)`.

The source character on the right is `(αα′)(det g)^{-1}`; the target character is `β(det y)β(det l)=β(det(y⊕l))`. The untwisted representation and the theta functional factor through the orthogonal sum. The Heisenberg translation is `(x;0)` and hence acts only on the first factor. No additional constant appears in this factorisation.

Put `rank W₀=2j`, `rank U=b`, `X=H^b⊕W₀`, `γ=ν^{-1}υ^j`, `γ_X=γυ^b`. The instance employed is **`(α,α′,β)=(γ,υ^b,γ)`**. It produces the characters `(υ^b,γ)` on `(W₀,U)` and `(γ,γ)` on `(W₀,W₀)`. The assignment of indices of the previous version must not be reused.

## 2. The archimedean constant of period

The integral of the equal-rank factor is exactly `I₀(ν)`, constant in `g` by `pcx:const`; its finite datum is `F₁=χ_S^{-1}∘det` on `GL_{2j}(O_S)`, and vacuum outside that set. It is not replaced by a period with another character.

For `ζ=det B_∞`, write `P=∏τ ζτ`, `Q=∏τ ζτ^{μτ}`. The formulas for the vectors Φ and Λ, 3306–3337, give

`ν_bc(ζ)=Q²/|Q|²`, `N(ζ)^j=|P|^{2j}`,

`|P^j Q|² / (ν_bc(ζ)N(ζ)^j)=conj(Q)²`.

This is exactly the power of the determinant that remains on moving `ph` to the real section and applying the Fock vacuum. The powers of `υ` correspond to the target character `γ`; no constant that was needed exactly has been merely estimated. The scalar of period is, therefore,

`ρ(h) I₀(ν) / (ν_bc(ζ_B) N(ζ_B)^j)`.

The cases outside the support are zero identities by the frame/support lemmas; one does not divide by a cut-off function that could vanish.

## 3. (U2) and finite cancellation, sign by sign

The reduction (U2), 3458–3470, preserves the source character and divides the target by `υ^b`. Its Levi factor is `χ_V(det q)^{-1}|det q|^{a/2}`, with

`χ_V(t)=α_V(t/bar t)υ(t)^{-a}`.

Using `υ(t/bar t)=υ(t)^2`:

| Side | `a` | source before/after | target after | `χ_V(t)` |
|---|---:|---|---|---|
| large | `b+2j` | `γ_X=ν^{-1}υ^{b+j}` | `γ=ν^{-1}υ^j` | `ν_bc(t)^{-1}υ(t)^b` |
| small | `b` | `υ^b` | `νυ^j` | `υ(t)^b` |

The large/small Levi quotient is `ν_bc(det q)|det q|^j`. After product, the quotient between the target characters on `y∈U(U)` is `ν(det y)^{-2}`.

Let `B=y^{-1}Y`, `x_f=B_f`. The large slice has factor `εχ_S^{-1}(det x_f)`; the small one, `χ_S^{-1}(det bar x_f)`. For each pair `w,bar w`, write `t=(det x_f)_w`, `u=(det bar x_f)_w`. They are units where the slice is non-zero. **`u=t^{-1}` is not assumed**: `x_f` is not a unitary element. The factors are respectively `χ(t)^{-1}` and `χ(u)^{-1}`; their quotient is

`χ(u)/χ(t)=ν_bc(det x_f)^{-1}`.

Outside `S∪bar S` the character is unramified and `det x_f` is a unit. Hence the global identity. With `det B=ζ_B det x_f`, the product of the finite phase and the phase of period is `ν_bc(det B)^{-1}`.

Finally `q=s₀x_UY`, `d₀=det(s₀x_U)`, `det B=(det y)^{-1}det Y`, and `ν_bc(det y)=ν(det y)^2`. Therefore, exactly:

`ν_bc(det q) · ν_bc(det B)^{-1} · ν(det y)^{-2} = ν_bc(d₀)`.

No dependence on `y`, `g` remains, nor a character in the equal-rank period. `|ν_bc(d₀)|=1`.

## 4. Fixed modulus: the correction of κ₀

The same computation, keeping the moduli and the factors already defined in (U2), gives

`κ̂₀ = ε_T ε_U^{-1} |d₀|_{A_E}^j`,

not only `ε_T ε_U^{-1} N((d₀)_∞)^j` as at 3631. Indeed, the non-character factor after period is

`|det q|_{A_E}^j / N(ζ_B)^j`.

One has `|det y|_{A_f}=1` by unitarity (product of the two components at split places), `|det x_f|=1` by integrality and unimodular Gram, and thus `|det Y_f|=1`; moreover `N(ζ_B)=N(det Y_∞)`. Substituting `det q=d₀det Y` leaves `|d₀|_{A_E}^j`.

The printed equality would additionally require `|d₀|_f=1`. This does not follow from `x_f` being a unit: `d₀` contains `s₀`, not `x_f`. P49, 3316–3325, fixes `s₀O_hat=αO_hat`, where `α=1/P′(ζ_q1)` at the indicated places of the different, and does not assume that it is a unit. For a standard space with identity frame, `d₀=s₀^b`; the omitted factor is then `|s₀|_f^{bj}`. The factors `ε_T,ε_U` are those already appearing in (U2), so they cannot be absorbed again inside the equality that keeps them with that definition.

**Uniformity:** the spaces, their frames and their lattices are fixed at 656–664; `s₀` is fixed by the Weil data of P49. None depends on `S`, on its modulus or on `ν`. An integral change of frame has finite modulus one; changing `s₀` by a unit does not modify this factor either. Consequently, replacing `κ₀` by `κ̂₀` preserves the uniformity required for all the admissible moduli, not only for a fixed modulus.

With `R=∫_{H\G}ρ′`, the proof gives `Cν=R κ̂₀ ε ν_bc(d₀)I₀(ν)` when `R<∞`, and `K=R|κ̂₀|`. If `R=∞`, (U3) forces `I₀(ν)·small_coef=0` and both coefficients are zero; one can take `Cν=κ̂₀ ε ν_bc(d₀)I₀(ν)`, `K=|κ̂₀|`. There is no need to divide by `I₀` nor to assume here that it is non-zero.

## 5. Two other applications and non-vanishing

At 4119 the coherent expansion factors with the same instance `(γ,υ^b,γ)`. The second factor has characters `(γ,γ)` and the datum `F₁` supported on invertible matrices. The characters are unitary; the absolute decay estimate acquires no additional power of the height. This verifies the use of product; the analytic estimates of moments and convergence are separate obligations.

In `pct:vantop`, 5634–5664, the inner integral over `l∈[U(W₀)]` contains exactly

`θ^{W₀,W₀}_{γ,γ}(g,l;ρ(y₂)e⊗F₁)`.

Its integral is the equal-rank lift which is assumed to be zero for all vectors of finite moments. The coherent ones satisfy that condition. No new non-vanishing theorem for a twisted period is required. The Fubini step uses the decay bound with polynomial weight in `y₂` and the moments of φ, as set out.

Thus the contradiction of `pcx:P-nonvan`, 5666–5678, again has its correct premise: Van descends to `(J,0)` and there the datum is `χ^{-1}(det 1)=1`, with non-zero integral. This review validates the character step in that chain; the lemmas on descent and on negative coefficients remain the proof's own lemmas, not consequences of a formal cancellation.

## 6. Consequences for the final constants

In `pcx:P-top`, 3753–3773, exclusively `|Cν|=K|I₀(ν)|` is used; with the corrected K,

`|Cν|²=K² L_*(m,ν,j) r_{W₀}(ν;z)`.

The constant RC is taken to be `K^{-2}`. There is no prescribed numerical constant that is contradicted by the fixed finite factor.

In `pcx:twice`, 2191–2230, the two applications give `B|c₁|²=L_*(k)r`, `C|c₂|²=L_*(-k)r`. Fubini gives exactly `ξ=c₁c₂`, and `L_*(k)L_*(-k)=1`; hence `r²=BC|ξ|²`, independent of ν. A fixed modification of the auxiliary coefficients is reflected in B and C; no ν-dependent factor remains uncancelled. `P-nonvan` and non-negativity fix the common positive value. This is the calibration employed for exchange.

Localised conclusion: the present correction resolves the substantial character objection of the previous version, also in the applications needed for non-vanishing. There remains an intermediate formula of positive normalisation which must be written with the complete adelic modulus; once this is repaired, it does not constitute an obstruction to exchange nor to the results that import it. This file does not replace the separate audits of the other inputs of P53.
