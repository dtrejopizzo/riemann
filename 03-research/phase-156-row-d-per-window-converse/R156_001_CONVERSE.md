# R156_001 — Report, 156c: the per-window converse

Task (blueprint `R156_000`, round 1): at a fixed window `T`, relate the primitive bottom `λ_min(A_T|P_T)` to the
complete bottom `λ^W_T` exactly, identify the 2×2 boundary matrix, decide the converse
`λ_min(A_T|P_T) ≥ 0 ⟹ λ^W_T ≥ 0` or produce a proved counter-mechanism, and state what changes in the reduction chain.

**Verdict (one paragraph).** At every window there is an exact identity (Thm 1.1). Take the complement of `P_T`
that is orthogonal to it for the form (not for `L²`). It is spanned by two vectors `h_+` (even) and `h_-` (odd). On
that plane the complete form is the diagonal matrix `G_T = diag(g_+, g_-)`, and
`In(W_T) = In(A_T|P_T) + In(G_T)`. Hence, when `λ_min(A_T|P_T) > 0`, `λ^W_T ≥ 0 ⟺ g_+ ≥ 0 and g_- ≥ 0`. These are two
scalar inequalities, and the degenerate case adds a range condition. In matrix form `G_T = S_T + J`: here
`J = diag(2,−2)` is the polar block, with the signature `(1,1)` of `lem:polar`, and `S_T` is the Schur complement of
`𝔞_T` over `P_T`. **The converse is not a structural consequence of the window hypotheses.** It fails in two model
families that share every hypothesis of the form and also the zeros and the pole of ζ (P46 `thm:finmod`). [amended per R156_004, A7: the models are comb-level. For them `W_T(a) := 𝔞^{(v(a))}_T + 2Re(AB̄)` is not the zero sum of `ζ_a`, which equals that of ζ, and `ζ_a` has no functional equation. The failures are class statements, as in `cor:void`, not statements about zeros.] The first
is the prime-free/deletion model on `(0.4608, 0.58]`. The second is the one-contact family with weight `θ·v_2` at
`T = ½log 3`, where it fails for every `θ < 0.8148`. Both failures are PROVED by explicit elementary witnesses, with
the primitive side imported from P46 `thm:index`/`cor:Tarch` and `thm:C`. For ζ itself the converse is *true* at
every `T ≤ 0.8`, and trivially so: the conclusion is Zhu's cited certificate. Nowhere is it decided by the identity
alone. After R156 the per-window content of row D is `RD_T` plus the sign of the two polar-capacity constants `g_±(T)`.

Rules followed. Statements use P46's own definitions, quoted below. There is no sign for ζ beyond `T ≤ log 2`
except the cited Zhu range already used by P46 `cor:KEP08`. Zeros appear only through labelled imports. The scripts
are in `scripts/r156/` (README there), each < 60 s, run one at a time. No paper or README was edited.

---

## 0. The paper's definitions (verbatim sources, `04-papers/46-row-d-dual-certificates/main.tex`)

* `eq:symbol`, `eq:form` (l.119–128): `σ_T = m − Σ_{n∈N_T} v_n cos(τ log n)`, `𝔞_T(F) = (2π)^{-1}∫σ_T|F̂|²`, on the form
  domain `D_T = {F ∈ L²(I_T): ∫log(2+|τ|)|F̂|² < ∞}`; `A_T` is the operator of `𝔞_T`.
* Tate moments (l.131–133): `A(F) = ∫F e^{t/2}`, `B(F) = ∫F e^{−t/2}`; `P_T = {A = B = 0}`.
* `eq:W` (l.134–136): **`W_T(F) = 𝔞_T(F) + 2Re(A(F)\overline{B(F)})`** — the complete Weil form. (Caution for integration:
  `def:W`, l.1152, is the *flat-top weight class* `𝒲_T`, not the form.)
* l.144–146 and macros l.38–40: `\lamA` = bottom of `𝔞_T` on the unit sphere of `P_T`; `\lamW` = bottom of `W_T` on the unit
  sphere of `L²(I_T)`; `\lamP` = value of (P) (`thm:A`, `def:PD`, `prop:weak`); `\lamW ≤ \lamP ≤ \lamA` (`rem:Kprim`, l.434–440).
* `eq:Aform` (l.403): `𝔞_T(F) = C_0‖F‖² + 𝔈(c_F) − Σ_{n∈N_T} v_n c_F(log n)`.
* `lem:parity` (l.2615) and the parity paragraph before `lem:strict`: for even `F`, `A = B = ∫F cosh(t/2)`; for odd `F`,
  `A = −B = ∫F sinh(t/2)`; `P_T = P_T^{ev} ⊕ P_T^{odd}` orthogonally for `L²` and for the form.
* `lem:polar` (l.1592): the kernel `2cosh((s−t)/2)` has signature `(1,1)` on every interval.
* `thm:W` (l.643): Euler–Lagrange on `P_T` with the two-dimensional inhomogeneity `α cosh(t/2) + β sinh(t/2)`.
* `\Ainf`, `\laminf`, `\laminfP` (l.2358–2366): `𝒜_∞ = 2AB + C_0‖F‖² + 𝔈(c_F)` (the complete form with the comb deleted),
  with bottoms on `L²(I_T)` and on `P_T`; `T^*_∞`, `T^*_{∞,P}` (`prop:arch`(iv)).
* `RD_T(a)` (l.3207 ff.): `λ_min(A_T(a)|P_T) ≥ 0` for the comb `v_n(a) = 2a(n)/√n`; `thm:finmod` (l.3265), `cor:void` (l.3317).

Notation used here only: `φ_c = cosh(t/2)1_{I_T}`, `φ_s = sinh(t/2)1_{I_T}`, `c(F) = ⟨F,φ_c⟩`, `s(F) = ⟨F,φ_s⟩`. So
`A = c + s`, `B = c − s`, and `2AB = 2c² − 2s²` for real `F`. We work over `ℝ`; `lem:parity`'s closing remark shows that
counts and bottoms agree over `ℂ`. `‖φ_c‖² = sinh T + T` and `‖φ_s‖² = sinh T − T`.

---

## 1. The exact identity at a fixed window

For a parity label `par ∈ {ev, odd}` put `ℓ_ev = c`, `ℓ_odd = s`, `ε_ev = +1`, `ε_odd = −1`, `D^{par} = D_T ∩ L²_{par}`
and `P^{par} = P_T^{par} ∩ D_T = ker(ℓ_par|D^{par})`. By `lem:parity` and the parity formulas for `A,B`:

**Lemma 1.0 (parity splitting of the complete form; PROVED).** `W_T = W^{ev} ⊕ W^{odd}` with
`W^{ev}(F) = 𝔞_T(F) + 2c(F)²` and `W^{odd}(F) = 𝔞_T(F) − 2s(F)²`, the sum being orthogonal for `L²` and for `W_T`.
*Proof.* `𝔞_T(F_e,F_o) = 0` (even symbol; `lem:parity`). For the polar term,
`A(F_e)B(F_o) + B(F_e)A(F_o) = c(F_e)(−s(F_o)) + c(F_e)s(F_o) = 0`. ∎

This is the rank-one parity channel decomposition of D.50 §1 (`R_2 = |u_e⟩⟨u_e| − |u_o⟩⟨u_o|`, `u = √2 φ`), written with
P46's normalisation.

**Theorem 1.1 (parity Schur–Haynsworth identity; PROVED).** Fix `T` and `par`.

(a) *Non-degenerate case.* Suppose that the self-adjoint operator of the closed semibounded form `𝔞_T|P^{par}` does not
have `0` in its spectrum. This covers `λ_par := bottom of 𝔞_T on P^{par} > 0`. Then there is a unique `h_par ∈ D^{par}`
with `ℓ_par(h_par) = 1` and `𝔞_T(h_par, G) = 0` for all `G ∈ P^{par}`. Moreover:
  1. `D^{par} = P^{par} ⊕ ℝh_par`, orthogonal for `𝔞_T` **and** for `W_T`. The `W`-orthogonal complement of `P^{par}`
     equals its `𝔞`-orthogonal complement, because the polar term vanishes against `P_T`.
  2. For `F = G + x h_par`: `W^{par}(F) = 𝔞_T(G) + g_par x²`, where `g_par := W_T(h_par) = 𝔞_T(h_par) + 2ε_par`.
  3. `n_-(W^{par}) = n_-(𝔞_T|P^{par}) + [g_par < 0]` and `ker W^{par} = ℝh_par` if `g_par = 0`, `= 0` otherwise.
     Here `n_-` is the maximal dimension of a negative subspace of the form domain, the convention of `lem:parity`.
  4. If `λ_par > 0`, then `𝔞_T(h_par) = κ_par := inf{𝔞_T(F): F ∈ D^{par}, ℓ_par(F) = 1}`, attained at `h_par`, and
     `g_par = min{W_T(F): F ∈ D^{par}, ℓ_par(F) = 1}`.
  5. `λ^W_{par} ≤ g_par/‖h_par‖²`. If `λ_par > 0` and `g_par > 0`, then `λ^W_{par} ≥ ½ min(λ_par, g_par/‖h_par‖²)`.
     Hence, **if `λ_par > 0`, `g_par > 0`** and `2λ^W_{par} < λ_par`: **`λ^W_{par} ≤ g_par/‖h_par‖² ≤ 2λ^W_{par}`**. Also
     `‖h_par‖² ≥ 1/‖φ_par‖²`. [amended per R156_004, A2: the right-hand inequality is proved only for `g_par > 0`; it
     is false in general for `g_par < 0` (DIAGNOSTIC: prime-free, `½log 3`, odd sector: `g_-/‖h_-‖² = −0.352`,
     `2λ^W_odd = −0.861`).]

(b) *Degenerate case (`λ_par = 0`).* Let `N = ker(𝔞_T|P^{par}) ≠ 0`. It is finite-dimensional, and the bottom is
attained because the resolvent is compact (`lem:strict`, attainment part). For `F_0 ∈ N` there is a unique `α(F_0) ∈ ℝ`
with `𝔞_T(F_0, G) = α(F_0) ℓ_par(G)` for all `G ∈ D^{par}`. This is `thm:W` at `λ = 0`, per parity. Then:
  * if `α ≢ 0` on `N`, then `W^{par}` is unbounded below, so `λ^W_T < 0` strictly and `κ_par = −∞`;
  * if `α ≡ 0` on `N`, then `N ⊂ ker W^{par}`, and (a) applies on the `L²`-orthogonal complement of `N` in `D^{par}`,
    with the same `h_par` and `g_par`. So `W^{par} ≥ 0 ⟺ g_par ≥ 0`.

  The condition `α|_N ≡ 0` is exactly the range condition of `P124_011` (4.4)/(6.2), `Π_{ker L_T} ρ = 0` (i.e.
  `ρ ∈ Ran L_T^{1/2}`). Here the column is `ρ(G) = 𝔞_T(H_0, G)` for any `H_0` with `ℓ(H_0) = 1`, since
  `ρ(F_0) = 𝔞_T(H_0,F_0) = α(F_0)`. [amended per R156_004, A3: this is a bordered-Schur range condition *of the
  same shape* as `P124_011` (4.4)/(6.2). The P124 column `ρ_{+,T} = P_T(e^{t/2}Φ_{+,T})` is not shown here to coincide
  with `ρ`, and no identity of the two is claimed. The "i.e." `Π_{ker}ρ = 0 ⟺ ρ ∈ Ran L^{1/2}` holds here because
  `𝔞|P^{par}` has compact resolvent, hence a spectral gap above `0`. Without a gap only `⟸` holds.]

(c) *Assembled.* Put `G_T := diag(g_+, g_-)`, where `+ = ev` and `− = odd`. If `0 ∉ spec(A_T|P_T)`, then
`n_-(W_T) = n_-(A_T|P_T) + n_-(G_T)` and `n_0(W_T) = n_0(G_T)`; `n_+` is infinite on both sides. In particular:
> **If `λ_min(A_T|P_T) > 0`, then `λ^W_T ≥ 0 ⟺ G_T ⪰ 0 ⟺ κ_+ ≥ −2 and κ_- ≥ 2`.**
>
> **Per window, unconditionally: `λ^W_T > 0 ⟺ [λ_min(A_T|P_T) > 0 and g_+(T) > 0 and g_-(T) > 0]`.**
>
> **`λ^W_T ≥ 0 ⟺ λ_min(A_T|P_T) ≥ 0` plus, in each sector with `λ_par = 0`, `α|_N ≡ 0`, plus `g_+ ≥ 0` and `g_- ≥ 0`.**

*Proof.* (a) Let `Q = P^{par}` with the form norm. Nondegeneracy means that the operator `L` of `𝔞|Q` is an
isomorphism `Q → Q*`. This is Kato VI §2, first representation theorem, together with the bounded inverse of `L` on
its spectral gap. [amended per R156_004, A1: self-contained version of this step. `𝔞_T = Γ_T + Π_T` with `Π_T`
bounded (`‖Π_T‖ ≤ 𝐀`), so `𝔞_T` is closed, bounded below by `−M`, with the form domain of `Γ_T`, which embeds
compactly in `L²(I_T)` (proof of P46 `prop:nodes`(i)). `Q` is closed in the form norm (`ℓ` is `L²`-continuous) and
dense in the `L²`-closed subspace `H_Q := ker ℓ ∩ L²_{par}` (if `x ∈ H_Q`, `d_n ∈ D^{par}`, `d_n → x`, and `e ∈ D^{par}`
has `ℓ(e) = 1`, then `d_n − ℓ(d_n)e ∈ Q → x`), so `𝔞|Q` is a closed semibounded form in `H_Q` with compact resolvent.
Its spectrum is discrete and its negative spectral subspace `Q_-` is finite-dimensional. If `0 ∉ spec`, then on the
spectral complement `Q_+ = Q ⊖ Q_-` one has `𝔞 ≥ δ‖·‖²` with `δ > 0`, hence
`𝔞(x) ≥ (δ/(δ+M+1))·(𝔞(x) + (M+1)‖x‖²)`: `𝔞` is coercive on `Q_+` in the form norm, and Lax–Milgram applies there,
while on `Q_-` the form is a negative definite finite matrix. `Q_-` and `Q_+` are `𝔞`-orthogonal, so `𝔞(Y,·) = f`
is uniquely solvable in `Q` for every form-bounded functional `f`. The functional `G ↦ 𝔞(H_0,G)` is form-bounded
because `H_0` lies in the form domain (Cauchy–Schwarz for the nonnegative form `𝔞 + M‖·‖²`). No further density or
Kato input is needed.] Fix any `H_0 ∈ D^{par}` with `ℓ(H_0) = 1`, for example an even or odd smooth bump. Solve
`𝔞(Y,G) = 𝔞(H_0,G)` for all `G ∈ Q`, with `Y ∈ Q`, and put `h = H_0 − Y`. Uniqueness holds because a difference of two
solutions lies in `Q ∩ Q^{⊥𝔞} = ker L = 0`.

(1) Write `F = (F − ℓ(F)h) + ℓ(F)h`. For `G ∈ Q`, `W(h,G) = 𝔞(h,G) + 2ε ℓ(h)ℓ(G) = 0`.

(2) Expand, using `ℓ(G) = 0` and `ℓ(h) = 1`.

(3) Let `Q_-` be the span of the finitely many negative eigenvectors of `L`, and `Q_≥` its `𝔞`-orthogonal complement in
`Q`, on which `𝔞 ≥ 0`. Then `D^{par} = (Q_- ⊕ [ℝh if g<0]) ⊕ (Q_≥ ⊕ [ℝh if g≥0])`, orthogonally for `W`. The first
summand is negative definite and the second is `W ≥ 0`. A negative subspace meets the second summand trivially, so its
dimension is at most that of the first. The kernel statement follows from (2) and `ker L = 0`.

(4) With `λ_par > 0`: `𝔞(G + h) = 𝔞(G) + 𝔞(h) ≥ 𝔞(h)`, and the same holds with `W`.

(5) The upper bound is the Rayleigh quotient at `h`. For the lower bound,
`W(G + xh) ≥ λ_par‖G‖² + g x² ≥ min(λ_par, g/‖h‖²)(‖G‖² + x²‖h‖²) ≥ ½ min(…)‖G + xh‖²`. The sandwich follows since
`λ^W_par < ½λ_par` forces the minimum to be `g/‖h‖²`. Cauchy–Schwarz gives `1 = ℓ(h) ≤ ‖h‖‖φ‖`.

(b) `𝔞|Q ≥ 0` gives `𝔞(F_0,G) = 0` for `G ∈ Q` (Cauchy–Schwarz for a nonnegative form). So `𝔞(F_0,·)` is a functional
on `D^{par}` that vanishes on the codimension-one subspace `ker ℓ`, hence a multiple of `ℓ`. Since `ℓ(F_0) = 0`,
`W(F_0,H) = 𝔞(F_0,H) = α(F_0)ℓ(H)`. So `W(xF_0 + H) = W(H) + 2xα(F_0)ℓ(H)`, which tends to `−∞` if `α(F_0)ℓ(H) ≠ 0`.
If `α ≡ 0`, then `N` is `𝔞`- and `W`-orthogonal to all of `D^{par}`. On `N^{⊥} ∩ Q` the bottom is the next eigenvalue,
`> 0`, and (a) applies with the same `h`, which can be chosen `⊥ N`.

(c) Add over the parities (Lemma 1.0). The sufficiency direction of the unconditional "`>`" statement is (a5). For
necessity, `λ^W > 0` gives `λ^A ≥ λ^W > 0` (`rem:Kprim`), and then `g_par = W(h_par) ≥ λ^W‖h_par‖² > 0`. ∎

**Remark 1.2 (relation to D.47; PROVED, bookkeeping).** D.47 Thm 2.1 is the identity `In(A|_K) = In(A) − In(MA^{-1}M^*)`.
It requires the *full* form to be invertible, and D.47 applies it to the local part `B_nuc = −𝔞_T` in the Hodge sign.
Applied here with `A = 𝔞_T`, it reads `In(𝔞_T) = In(𝔞_T|P_T) + In(S_T)` with `S_T := diag(𝔞(h_+), 𝔞(h_-))`, and this
`S_T` is D.47's Green matrix up to congruence. Theorem 1.1 is the same congruence applied to `W_T = 𝔞_T + M^*CM`,
with the complement taken over `P_T`. Only `𝔞_T|P_T` has to be invertible, which is the right hypothesis for a
converse whose premise is on the primitive side. Since the polar term depends only on the moments,
**`G_T = S_T + J`, `J = diag(2, −2)`**. In the moment coordinates `(A,B)`, `J` is `[[0,1],[1,0]]`, D.49 (1.4)/D.47
(1.2), and `G_T^{AB} = ¼[[g_++g_-, g_+−g_-],[g_+−g_-, g_++g_-]]`. When `𝔞_T` itself is invertible on `D^{par}`,
`𝔞(h_par) = 1/⟨𝔞_{par}^{-1}φ_par, φ_par⟩`. When `W_T` is invertible,
`g_par = 1/⟨W_{par}^{-1}φ_par, φ_par⟩`, i.e. `G_T = (M W_T^{-1} M^*)^{-1}` up to congruence (Sherman–Morrison).
Here `h_par` solves the finite-interval Wiener–Hopf equation `𝒜h = 𝔞(h)·φ_par` on `I_T`, `thm:W` at `λ = 0`, with
multiplier `μ = 𝔞(h)`.

---

## 2. What `G_T` is

**Proposition 2.1 (`G_T` is the polar capacity; PROVED).** Suppose `λ_min(A_T|P_T) ≥ 0`, and in the degenerate case
the range condition of Thm 1.1(b) holds. For `(β,α) ∈ ℝ²` put
`E_T(β,α) := inf{W_T(F): F ∈ D_T real, Φ_F(0) = B(F) = β, Φ_F(1) = A(F) = α}`. Then
`E_T(β,α) = (α,β) G_T^{AB} (α,β)^T`, attained. So `λ^W_T ≥ 0 ⟺ E_T ≥ 0 on ℝ²`. In words: **the converse at `T` says
that the complete Weil energy needed to prescribe the values of `Φ_F` at the pole `s ∈ {0,1}` is nonnegative.**
*Proof.* Theorem 1.1(a4) per sector, with `c = (α+β)/2` and `s = (α−β)/2`. ∎

**Signature reading (answers blueprint item 2).** `J` carries exactly the one negative square of `lem:polar`, in the odd
(`sinh`) direction, and one positive square, in the even (`cosh`) direction. The converse is the pair of inequalities
`𝔞(h_-) ≥ 2`, where the primitive Schur complement must beat the negative polar square, and `𝔞(h_+) ≥ −2`, where the
positive polar square may absorb a negative Schur value down to `−2`. Neither is automatic. `S_T` itself is hyperbolic
whenever `n_-(𝔞_T) = 1`, `𝔞_T` is nondegenerate and `𝔞_T|P_T > 0`: DIAGNOSTIC for ζ at `½log 3`, with
`S_T ≈ diag(−1.99999991, +2.00135)` [amended per R156_004, A4: the printed `−2.0000001` was a typo. It would mean
`g_+ < 0`. The script value is `κ_+ = g_+ − 2` with `g_+ = +8.7·10^{-8}`]. **For ζ, `S_T ≈ −J`.**
The primitive Schur complement nearly cancels the polar block, and `G_T = S_T + J` is tiny: DIAGNOSTIC
`g_+ ≈ 8.6·10^{-8}`, `g_- ≈ 1.35·10^{-3}` at `½log 3` (§7). This is quantified by Thm 1.1(a5). Wherever
`λ^W ≪ λ^A`, the even entry is `g_+ ≍ λ^W_{ev}‖h_+‖²`, within a factor 2. Combined with P46 `cor:margin1`,
`λ^W ≤ 4·10^9 T e^{−15.449T}` for `T ≥ 1` (PROVED, P46). *If* in addition `λ^A` is not also that small, then
`g_+(T)/‖h_+‖² ≤ 2λ^W_T → 0`. That last step is HEURISTIC, since no lower bound on `λ^A` is known. [amended per
R156_004, A4: `cor:margin1` bounds `λ^A` by the same `4·10^9 T e^{−15.449T}`, so the premise `2λ^W < λ^A` is itself
undecided at every `T ≥ 1`. The sandwich also needs `g_+ > 0` (A2).] Under Zhu's
conjectural law `−log λ^W ≍ e^{2T}` (P46 `rem:margin`), the converse is a doubly-exponentially thin 2×2 inequality
(HEURISTIC).

**Remark 2.2 (zero side; labelled import).** By `lem:roughEF`, `g_par = W_T(h_par) = Σ_ρ Φ_h(ρ)Φ_h(1−ρ)` whenever the zero
sum converges absolutely. Under RH this is `Σ_γ|ĥ_par(γ)|²`, and `E_T` becomes a Paley–Wiener interpolation energy: the
least `ℓ²(zeros)` mass of a type-`T` transform with prescribed values at `τ = ∓i/2`. This is a reading only; nothing in
§§3–6 uses it.

---

## 3. The converse is not structural: two proved counter-mechanisms

All values below are exact closed forms. The only estimate is `K(u) = 1/(2sinh(u/2)) + 1/(2cosh(u/2)) ≤ 1/u + 1/2` on
`(0,2T)`, used against `g_F(u) := c_F(0) − c_F(u) ≥ 0` (Cauchy–Schwarz) in `eq:Aform`. Also used:
`C_0 = −γ − π/2 − 3log 2 − log π` and `∫_{2T}^∞K = log coth(T/2) + π − 2arctan e^T` (`thm:S`(iii)). For odd `F`,
`2AB = −2s(F)²`.

**Theorem 3.1 (the prime-free complete form is negative from `T = 0.4608`; PROVED, elementary).** Let `F_T(t) = t` on
`I_T`. Then `c_{F_T}(u) = (2T−u)(2T²−2Tu−u²)/6` and `g(u) = u(6T²−u²)/6 ≥ 0`, with `‖F_T‖² = 2T³/3` and
`s(F_T) = 4T cosh(T/2) − 8 sinh(T/2)`. So
`𝒜_∞(F_T) ≤ U(T) := (2T³/3)(C_0 + log coth(T/2) + π − 2arctan e^T) + 2T³(3T+7)/9 − 2s(F_T)²`.
`U(½log 3) = −0.0200526…`; the exact value, by quadrature, is `−0.0268769`, matching the Galerkin cross-check to 14
digits. `U(0.461) = −3.6·10^{-5}` and `U(0.47) = −1.40·10^{-3}`. Hence `\laminf(T) < 0` for every `T ≥ 0.461`, by
monotonicity (`prop:arch`(i)). In particular **`T^*_∞ ≤ 0.461` (PROVED)**, where P46 records only the DIAGNOSTIC
`T^*_∞ ≤ 0.3716`. Scripts: `r156_odd_witness.py`, `r156_witness_threshold.py`. [amended per R156_004, A5: (1) wording.
This is the first *proved* upper bound on `T^*_∞` below the `0.60` that follows from `T^*_∞ ≤ T^*_{∞,P} ≤ 0.60`
(`prop:arch`(iv), `cor:Tarch`). It is numerically *weaker* than the DIAGNOSTIC Galerkin bound `0.3716`, and it
certifies the strict separation `T^*_∞ ≤ 0.4608 < 0.58 ≤ T^*_{∞,P}`. (2) Rigour. Outward-rounded mpmath interval
arithmetic (`scripts/r156/audit_r156_witness_t.py`) gives `U(0.461) ∈ [−3.59383·10^{-5}, −3.59382·10^{-5}]`,
`U(0.4608) ∈ −7.01596·10^{-6} ± 10^{-40}` and `U(½log 3) ∈ −0.0200526439746…`. It also re-derives `c_F`, `g`, the body
integral and `s(F)` exactly (sympy). So the statement holds for every `T ≥ 0.4608`, and "`= −3.6·10^{-5}`" should
read `−3.59·10^{-5}`. The sign conventions (`2AB = −2s²` for odd `F`) are confirmed by an independent Fourier-side
evaluation `(2π)^{-1}∫m|F̂|² + 2AB = −0.026876865` at `½log 3` (DIAGNOSTIC), which bypasses the Lévy representation.]

**Corollary 3.2 (deletion model; PROVED, primitive side imported machine-verified).** Let `a = Λ·1_{n≥5}`
(`thm:finmod`(i)). Its `ζ_a` has exactly the zeros and the pole of ζ, `ψ_a − ψ` is constant for `x ≥ 5`, and
`0 ≤ a ≤ Λ`. For every `T ∈ [0.461, 0.58]`:
* `RD_T(a)` holds, strictly: `λ_min(A_T(a)|P_T) = \laminfP(T) > 0` (`thm:index`(i), `cor:Tarch`; PROVED machine-verified);
* `λ^W_T(a) = \laminf(T) < 0` (Thm 3.1).

So **the per-window converse fails for `a` on `[0.461, 0.58]`**. It fails already in the odd sector alone on
`[0.461, log 2]`, since `λ_odd(T) > 0` for `T ≤ log 2` (`thm:index`(i)) while `W^{odd}(F_T) < 0`. At `½log 3` the
DIAGNOSTIC Galerkin gives `G_T = diag(−0.451, −20.08)` and `n_-(W_∞) = 2`, so both channels fail.

[amended per R156_004, A7/A8. (i) *Definition.* P46 defines `RD_T(a)` (l.3207 ff.) but no complete form for a
general comb. Here `W_T(a) := 𝔞^{(v(a))}_T + 2Re(AB̄)` and `λ^W_T(a)` is its bottom on `L²(I_T)`. (ii) *Validity on
the range.* For `T ∈ [0.461, 0.58]`, `N_T ⊂ {2,3}` (`e^{1.16} = 3.19`) and `a = 0` on `N_T`. Indeed the comb of `a` is
empty for every `T < ½log 5 = 0.8047`. So `RD_T(a)` is *literally* `thm:finmod`(i), `λ^A_T(a) = \laminfP(T) > 0`, and
`W_T(a) = 𝒜_∞`. The construction of `thm:finmod`(i),(iii) applies verbatim (`N = 5`). (iii) *Scope.* `ζ_a = ζ·E` has the
zeros and the pole of ζ, but `W_T(a)` is **not** the explicit-formula functional of `ζ_a`. The zero sum over the
zeros of `ζ_a` is the zero sum of ζ, i.e. `W_T(Λ)`, and `W_T(a) = W_T(Λ) + Σ_{n∈N_T, n<5} v_n c_F(log n)`; the
difference is the `E'/E` term. Together with the missing functional equation (`thm:finmod`(iii)), this means
`λ^W_T(a) < 0` says nothing about zeros. The counter-model refutes the *comb-level implication*
`RD_T(a) ⟹ λ^W_T(a) ≥ 0` for nonnegative combs, as `cor:void` refutes comb-level derivations of `RD_T`. (iv) *Novelty.*
For the empty comb the failure is exactly `T^*_∞ < T^*_{∞,P}`. P46 already shows this DIAGNOSTICALLY
(`0.3716` vs `0.5958`, after `cor:Tarch`). What is new is the proof (Thm 3.1 with `cor:Tarch`). (v) *The odd-sector
sentence* is sector-wise. On `(T^*_{∞,P}, log 2]` the full converse is vacuous for `a`, because `RD_T(a)` fails, and
only the odd-sector implication `λ_odd > 0 ⟹ W^{odd} ≥ 0` is refuted there.]

**Theorem 3.3 (one-contact family at `½log 3`; PROVED, with imports).** Let `T = ½log 3`, so `N_T = {2}`, and for
`θ ∈ [0,1]` let `a_θ = Λ − (1−θ)Λ(2)1_{n=2}`. It is nonnegative with `a_θ ≤ Λ`, has the zeros and the pole of ζ, and
its comb on `N_T` is `θv_2`.
(i) `λ_min(A_T(a_θ)|P_T) > 0` for all `θ ∈ [0,1]`. This bottom is an infimum of affine functions of `θ`, hence
    concave. It is positive at `θ = 0` (`cor:Tarch`) and at `θ = 1` (`thm:C`: `≥ λ^P ≥ 8.8577·10^{-5}`). Both imports
    are PROVED machine-verified.
(ii) `λ^W_T(a_θ) < 0` for every `θ < 0.8148`. Witness: the odd quintic
    `F = t − (2634299/500000)t³ + (1919331/250000)t⁵`, with `𝒜_∞(F) ≤ −0.0061378` (elementary bound) and prime form
    `−v_2 c_F(log 2) = +0.0075328` (exact). So `W_θ(F) < 0` for `θ < 0.81480`. The bare witness `F = t` gives
    `θ < 0.4741`, with `c_t(log 2) = −0.043147`. Script: `r156_theta_witness.py`. [amended per R156_004, A6: the
    bound is `𝒜_∞(F) ≤ U_0 ∈ [−0.00613778443569004, −0.00613778443569003]`, so "`≤ −0.0061378`" was rounded in the
    unsafe direction. Read `≤ −0.00613778`. Interval re-verification (`scripts/r156/audit_r156_theta_quintic.py`,
    exact rationals, outward rounding, `T = iv.log(3)/2`): `Π(F) ∈ 0.00753283781432786…`,
    `−U_0/Π ∈ 0.814803741561464…`, and `U_0 + 0.8148·Π ∈ −2.8185·10^{-8}` (negative; the margin at the stated threshold
    is `2.8·10^{-8}`, not `6·10^{-3}`); for `F = t`: `−U_0/Π ∈ 0.474113847…`. `W_θ(F) = 𝒜_∞(F) + θΠ(F)` with
    `Π(F) = −v_2 c_F(log 2)` is P46's `W_T = \Ainf + Π_T` with comb `θv_2` (`log 2 < 2T`, so `c_F(log 2)` is the polynomial
    branch). The claim holds as stated for every `θ ≤ 0.8148`. `W_T(a_θ)` is a comb-level form (see the note after
    Cor 3.2).]
(iii) `θ ↦ λ^W_T(a_θ)` is concave and, by Zhu (cited, as in `cor:KEP08`), positive at `θ = 1`. So the failure set in
    `[0,1]` is an interval `[0, θ_*)` with `0.8148 ≤ θ_* < 1`. DIAGNOSTIC (§7): `θ_* ≈ 0.99991`, and the even channel
    fails just above `θ = 1` (`g_+(1.001) ≈ −4.9·10^{-5}`). The complete form at `½log 3` survives only in a
    `θ`-window of width about `10^{-4}` around the true `Λ(2)`. The primitive form survives on `[0, ≈1.0065]`.

**Corollary 3.4 (method constraint for the converse; PROVED, in the sense of P47 Thm 18.1 / P46 `cor:void`).** Let `𝒞` be a
class of nonnegative arithmetic functions containing `Λ` and closed under deletion of finitely many terms. Examples are
`𝒞_zeros`, `𝒞_PNT(ε)` and `𝒞_BT`, per `cor:void`, and `𝒞_BT` and `𝒞_zeros` also contain every `a_θ`. Then no derivation of
"`RD_T ⟹ λ^W_T ≥ 0`" whose only prime input is `𝒞`-membership exists at any `T ∈ [0.461, 0.58]`. At `T = ½log 3`, a
sound derivation must see `Λ(2)` to relative precision better than `18.5%` (PROVED). The DIAGNOSTIC figure is about
`10^{-4}`.
*Proof.* Such a derivation proves the implication for `Λ·1_{n≥5}` (resp. for `a_{0.8}`), where it is false (Cor 3.2,
Thm 3.3). ∎

[amended per R156_004, A9. (i) The `½log 3` clause needs a different class hypothesis. Closure under deletion
gives `a_0` but not `a_{0.8}`. Assume instead that `𝒞 ∋ a_θ` for some `θ < 0.8148`, e.g. `𝒞` closed under lowering
one term within `[0, Λ(n)]`. `𝒞_BT`, `𝒞_zeros` and `𝒞_PNT(ε)` all have this property: `ζ_{a_θ} = ζ·exp(−(1−θ)2^{-s})`
and `ψ_{a_θ} − ψ` is constant for `x ≥ 2`. (ii) "Relative precision better than 18.5%" means that the derivation
must distinguish the true weight `Λ(2)` from `θΛ(2)` for every `θ < 0.8148`, i.e. from weights at least `18.52%`
*below* it. Nothing is claimed about weights above `Λ(2)`. (iii) As with `cor:void`, this is a statement about
derivations and classes, not about ζ (see the note after Cor 3.2).]

**The archimedean analogue (blueprint item, decided).** For `v = 0` the converse holds on `(0, T^*_∞)`, where both sides
are positive, and holds vacuously for `T > T^*_{∞,P}`. It fails on `[0.461, T^*_{∞,P})`, which contains `[0.461, 0.58]`
(PROVED). With strict decrease of `\laminf`, noted but not used in P46 after `lem:strict`, it fails on all of
`(T^*_∞, T^*_{∞,P})`. [amended per R156_004, A10: P46 states the strict decrease of `\laminf` in the unnumbered
paragraph after `lem:strict`, with its argument: the same Euler–Lagrange/moment argument, tested against `G_0` with
vanishing Tate moments, so the pole term drops out. The `R155_061` closing note confirms that the argument goes
through on all of `L²`. Label: PROVED, resting on that unnumbered paragraph. It needs a numbered statement before
it is cited from a paper.] DIAGNOSTIC: that is `(≈0.372, ≈0.596)`, and the odd channel fails first, at `≈0.372`; the even
channel fails at `≈0.44`. Reading: for the primitive form the primes are a cost up to `≈0.58` (P46 after `cor:Tarch`).
For the complete form they are a *necessity* from `≤ 0.461` (PROVED), `≈0.372` DIAGNOSTIC. The first contact enters
at `½log 2 = 0.3466`, just before (DIAGNOSTIC, HEURISTIC reading).

---

## 4. Windows where the sign is known (consistency, blueprint item 3)

**Proposition 4.1 (PROVED, resting on the stated imports).**
(i) `0 < T ≤ log 2`: `λ_min(A_T|P_T) > 0`. This is Paper 42 `cor:certifiedinitialinterval`, a *primitive* statement,
    and also `λ^A ≥ λ^W > 0` from Zhu. So Theorem 1.1(a) applies, and `λ^W_T ≥ 0 ⟺ g_+(T) ≥ 0 and g_-(T) ≥ 0`.
(ii) `0 < T ≤ 0.8`: Zhu's `W_{0.8} ≥ 8.9·10^{-18}` (cited, not re-verified; as in `cor:KEP08`) and monotonicity give
    `λ^W_T > 0`, hence **`g_+(T) > 0` and `g_-(T) > 0`** by Thm 1.1(c). The converse holds at these `T` because its
    conclusion is known, and not through the identity.
(iii) `2T < log 2`: the comb is empty, `W_T = 𝒜_∞`, and `λ^∞ ≥ 0` (Yoshida/Bombieri, `prop:arch`(iii)). With
    `\laminfP > 0` (`thm:index`(i)) this gives `κ^∞_+ ≥ −2` and `κ^∞_- ≥ 2`, the archimedean channels at the smallest
    windows. DIAGNOSTIC at `T = 0.3466`: `g_+ = +0.0024` and `g_- = +12.2`, consistent. [amended per R156_004, A11:
    Yoshida 1992 Thm 1 (strict positivity at `a = ½log 2`, a finite-matrix hand computation) is known on record only
    from secondary reports (`R154_013` l.20: the volume is not in `00-references`). Bombieri 2000 Thm 12 covers
    `|I| < log 2`. The certified backstop for `λ^∞ ≥ 0` at `2T < log 2` is Zhu 2026 Thm 1.2 (cited, not re-verified),
    since `W_T = 𝒜_∞` there. The conclusion is unaffected.]
(iv) `T = ½log 3`: `thm:C` gives `λ^A ≥ λ^P ≥ 8.8577·10^{-5}` *without* Zhu, so the nondegenerate case of Thm 1.1
    holds unconditionally. The identity then says exactly what `thm:C` lacks for the complete form: the two numbers
    `g_±(½log 3) ≥ 0`. `thm:C` cannot supply them. Its `β ≠ (2,0)`, and its certificate proves positivity of
    `W_T + (β_0−2)Re(AB̄) + β_1Re(A'B̄ − AB̄')`. That differs from `W_T` by a form of rank `≤ 4` supported on the
    functionals `A, B, A', B'`, i.e. exactly on the directions `G_T` measures. [amended per R156_004, A11b: this is
    not "exactly". `G_T` sees only the directions of `A` and `B`. The `β_1` term also involves `A', B'`, which `G_T`
    does not measure.] DIAGNOSTIC: `g_+ ≈ 8.6·10^{-8}` is four
    orders below `λ^A ≈ 9.5·10^{-4}`. This is the quantitative content of P46's remark after `cor:KEP08` (defect
    `5.9·10^{-3}` versus margin `8.86·10^{-5}`). The complete form at `½log 3` rests on Zhu.

---

## 5. Consequences for the reduction chain (blueprint item 4)

P46 §9.1 (l.2950–2957):
`RH ⟺ ∀T λ^W ≥ 0 ⟺ ∀T λ^P ≥ 0 ⟺ ∀T ∃ finite certificate ⟺ ∀T ∃ w_T flat-top`.
After R156 the per-window status of each link is:

1. **`λ^W_T > 0 ⟺ λ^A_T > 0 ∧ g_+(T) > 0 ∧ g_-(T) > 0`** — new, PROVED, per window (Thm 1.1(c)). Combined with `thm:Al`(b)
   and `thm:KEP3`(a), for `T ≥ ½log 2`: ~~[∃ flat-top certificate at `T`] ⟺ [`KEP(T)` indeterminate] ⟺
   [`RD_T` strictly and `G_T ≻ 0`]~~. This is per window. [amended per R156_004, A12 (FAIL as stated): `thm:KEP3`(a)
   gives only `λ^W > 0 ⟹ KEP(T) indeterminate ⟹ λ^W ≥ 0`. Indeterminacy is *not* known to be equivalent to
   `λ^W > 0`; the two can differ on `{T: λ^W = 0}`. Correct chain, for `T ≥ ½log 2`:
   [∃ `w ∈ 𝒲`: `Al_T(w)`] ⟺ `λ^W_T > 0` ⟺ [`λ^A_T > 0` ∧ `G_T ≻ 0`] ⟹ [`KEP(T)` indeterminate] ⟹ `λ^W_T ≥ 0`
   ⟺ [`RD_T` ∧ range ∧ `G_T ⪰ 0`].]
2. **`λ^W_T ≥ 0 ⟺ RD_T ∧ [range condition where λ^A_par = 0] ∧ G_T ⪰ 0`** — PROVED, per window. This refines the open
   "`RD_T ⟹ λ^W_T ≥ 0`" (P46 l.3549–3552, `R155_053` §(v), `R155_060` row 14) to a single explicit obstruction: the
   2×2 polar-capacity matrix. The converse is **equivalent** to `RD_T ⟹ G_T ⪰ 0 (+ range)`.
3. The primitive-certificate link (`λ^P > 0 ⟹` finite certificate `⟹ λ^A > 0`, `thm:D1`) is per window and
   unchanged. `λ^P ≥ 0 ⟸ λ^W ≥ 0` per window. Whether `RD_T ⟹ λ^P_T ≥ 0` remains OPEN. Side DIAGNOSTIC:
   in both computed cases the real-test part of `𝒦^{prim}` (`A = A' = 0`) does not go below `λ^A`. The bottom of
   `𝔞` on `ker{A}` alone, where `W = 𝔞`, is `−0.416` in the prime-free model.
4. The only non-per-window link is `∀T RD_T ⟹ ∀T G_T ⪰ 0`. It holds, but only through RH (P45 `thm:sufficiency`,
   non-effective), and by Cor 3.4 it is **not** a class consequence at any single window of `[0.461, 0.58]`. So
   `prop:uniform` ("the arithmetic content of row D is uniformity in `T`") is now sharp on both sides. Per window, the
   complete form needs `RD_T` plus two scalar polar-capacity inequalities, each of which pins the actual `Λ(n)`,
   `n ∈ N_T`.
5. A window-shift converse "`RD_{T'} ⟹ λ^W_T ≥ 0`" valid for all nonnegative combs needs `T' ≥ T^*_{∞,P} ≥ 0.58`
   whenever `T ≥ 0.461`. This is PROVED by Cor 3.2: `RD_{T'}(Λ1_{n≥5})` holds for all `T' ≤ 0.58`. Whether some
   effective shift exists for ζ is OPEN. [amended per R156_004, A13: for `max(T,T') ≥ ½log 5` use
   `a = Λ1_{n≥N}` with `N ≥ max(5, e^{2max(T,T')})`, as in `cor:void`. Then both combs are empty,
   `RD_{T'}(a) ⟺ \laminfP(T') ≥ 0` and `λ^W_T(a) = \laminf(T) < 0`. The statement is precisely: "needs
   `T' ≥ T^*_{∞,P}`", and `T^*_{∞,P} ≥ 0.58` is PROVED.]

---

## 6. Corpus check (novelty)

Grep of `03-research/` and P46 for `per-window converse`, `κ_±`, channel constants, `0.3716`, and deletion
counter-models of the complete form. Hits: `R155_053/058/060`, `README` of phase 155 and `R156_000`, all saying OPEN.
`0.3716` appears only in P46 as a DIAGNOSTIC Galerkin bound. The linear algebra is on record: D.47 Thm 2.1 (Haynsworth),
D.50 §1–2 (rank-one parity channels, secular functions) and P124_011 §4 (range condition). **New here:**
* the complement taken over `P_T`, so that only `𝔞_T|P_T` has to be invertible, and the resulting exact per-window
  equivalences of Thm 1.1(c);
* `G_T = S_T + J` and the polar-capacity characterisation (Prop 2.1);
* the sandwich `λ^W ≤ g/‖h‖² ≤ 2λ^W`;
* the elementary proof of `\laminf < 0` for `T ≥ 0.461`;
* the two proved counter-models to the converse and Cor 3.4.

D.50 §4's gate `A_o − E > 0 ⟺ m_o(E) < 1` needs positivity of the odd Lévy operator on all of `L²_odd`. That fails in
the prime-free model at `½log 3`, where the odd bottom of `𝔞` on `L²` is `−0.38` (DIAGNOSTIC). The `P_T`-based
version is the one that applies.

---

## 7. Diagnostics (float64 Legendre–Galerkin; upper bounds on every infimum; prove nothing)

| T, comb | λ^A ev / odd | g_+ | g_- | λ^W ev / odd |
|---|---|---|---|---|
| ½log3, v=0 (N=30) | +0.0825 / +0.3816 | −0.451 | −20.08 | −0.074 / −0.430 |
| ½log3, ζ (N=16/24/32) | 9.84e-4 / 9.66e-4 / 9.52e-4 (ev) | 1.01e-7 / 8.70e-8 / 8.64e-8 | 1.38e-3 / 1.35e-3 / 1.35e-3 | 5.6e-8 (ev) |
| ½log2 = 0.3466, v=0 | +0.547 / +0.843 | +0.0024 | +12.2 | +0.0013 / +0.073 |
| θ-family at ½log3 | see `r156_theta_family.py` | +2.6e-6 (θ=.9999), −4.9e-5 (θ=1.001) | −3.1e-4 (θ=.9999) | — |

The inertia identity `n_-(W) = n_-(𝔞|P) + n_-(G)` was checked on Galerkin matrices at 6 cases, including the
indefinite-nondegenerate `T = 0.7` and `0.9` (prime-free), with `2 = 1+1` and `3 = 2+1`. The P46 value
`\laminfP(½log3) ≈ +0.083` is reproduced. At `log 2` and above the ζ values are `< 10^{-7}` and not stable, as in
P46 `rem:galerkin`, and are not quoted. [amended per R156_004, A16: (i) On finite Galerkin matrices the inertia
identity is Haynsworth's theorem, so it holds exactly. The 6-case check tests the code, not the theorem. (ii) Galerkin
`κ_±`, hence `g_±`, are *upper* bounds on the true constants. A negative Galerkin `g` is evidence of a true negative
(up to float64 and quadrature error). A positive one, e.g. `g_+ ≈ 8.6·10^{-8}` for ζ, is no evidence that the true
`g` is positive. For ζ at `T ≤ 0.8`, `g_± > 0` rests on Zhu (Prop 4.1(ii)), not on this table.]

---

## 8. Labelled statement list

| # | statement | label |
|---|---|---|
| L1.0 | parity splitting `W = (𝔞+2c²) ⊕ (𝔞−2s²)` | PROVED |
| T1.1(a) | nondegenerate `𝔞|P`: `D = P ⊕ span(h_+,h_-)`, `In(W) = In(𝔞|P) + In(G_T)` | PROVED |
| T1.1(a5) | `λ^W ≤ g/‖h‖²`; `λ^W ≥ ½min(λ^A, g/‖h‖²)`; sandwich when `2λ^W < λ^A` **and `g > 0`** [amended per R156_004, A2] | PROVED |
| T1.1(b) | degenerate case: `λ^W ≥ 0` forces the Lagrange multipliers to vanish on `ker(𝔞|P)`, which is P124's range condition | PROVED |
| T1.1(c) | `λ^W > 0 ⟺ λ^A > 0 ∧ g_± > 0`; `λ^W ≥ 0 ⟺ RD_T ∧ range ∧ G_T ⪰ 0` | PROVED |
| R1.2 | `G_T = S_T + J`; resolvent formulas; relation to D.47/D.49/D.50 | PROVED |
| P2.1 | `G_T` = polar capacity `E_T(Φ(0),Φ(1))` | PROVED |
| §2 | `S_T ≈ −J` for ζ; `g_+ ≍ λ^W` doubly-exponentially thin | DIAGNOSTIC / HEURISTIC |
| R2.2 | zero-side interpolation reading of `g_±` | HEURISTIC (import `lem:roughEF`, RH) |
| T3.1 | `𝒜_∞(t·1_{I_T}) ≤ U(T) < 0` for `T ≥ 0.461`; `T^*_∞ ≤ 0.461` | PROVED (elementary closed form; interval-verified, `audit_r156_witness_t.py`, valid from `0.4608`) [amended per R156_004, A5] |
| C3.2 | deletion model `Λ1_{n≥5}`: converse fails on `[0.461, 0.58]` (odd sector: `[0.461, log 2]`) | PROVED (primitive side: machine-verified import) |
| T3.3 | one-contact family at `½log3`: converse fails for `θ < 0.8148`; failure set `[0,θ_*)`, `θ_* < 1` | PROVED (imports `thm:C`, `cor:Tarch`, Zhu for `θ_*<1`; quintic interval-verified, `audit_r156_theta_quintic.py`; comb-level form) [amended per R156_004, A6/A7] |
| T3.3 | `θ_* ≈ 0.99991`; complete-form window of width about `10^{-4}` | DIAGNOSTIC |
| C3.4 | no derivation of the converse from deletion-closed class membership at `T ∈ [0.461, 0.58]`; at `½log3` for classes containing some `a_θ`, `θ < 0.8148` | PROVED (method constraint) [amended per R156_004, A9] |
| §3 | archimedean converse fails exactly on `(T^*_∞, T^*_{∞,P})` | PROVED on `[0.461, 0.58]`; rest uses strict decrease of `\laminf` (P46 unproved remark) |
| P4.1 | `g_±(T) > 0` for ζ, `T ≤ 0.8` | PROVED resting on Zhu (cited) |
| §5.1 | chain certificate ⟺ `λ^W>0` ⟺ `λ^A>0 ∧ G_T ≻ 0` ⟹ KEP indeterminate ⟹ `λ^W ≥ 0` | PROVED as corrected; the original "⟺ KEP indeterminate" FAILS as stated [amended per R156_004, A12] |
| §5.3 | `RD_T ⟹ λ^P_T ≥ 0` per window | OPEN |
| §5.5 | effective window-shift converse for ζ | OPEN |
| — | per-window converse for ζ at `T > 0.8` | OPEN (equivalent to `RD_T ⟹ G_T ⪰ 0`) |

---

## 9. Doubts for the audit

1. **Infinite-dimensional step in Thm 1.1(a).** I use that a closed semibounded form with compact resolvent, restricted to
   the closed subspace `P^{par}`, with `0 ∉ spec`, gives an isomorphism from the form space to its dual, and that
   `G ↦ 𝔞(H_0, G)` lies in that dual. The first is Kato VI plus the spectral gap; the second holds because `H_0` is in
   the form domain. Check that `P^{par} ∩ D_T` is the form domain of the restricted closed form: it is closed in the
   form norm, since `c` and `s` are `L²`-continuous. Check also that density is not needed.
2. **Sign bookkeeping.** For odd `F`, `A = s`, `B = −s`, so `2AB = −2s²`. The `t`-witness value depends on this. It was
   cross-checked against the independent Galerkin code (`−0.02687686527705946` both ways), and the Galerkin code
   reproduces P46's `+0.083`.
3. **Witness rigour.** The bounds are exact symbolic expressions evaluated at 30 digits, with margins `≥ 3.6·10^{-5}`
   (at `0.461`) and `6·10^{-3}` (quintic). This is not interval arithmetic. Also check `K ≤ 1/u + 1/2` and the direction
   of the inequality: `g ≥ 0`, so an upper bound on `K` gives an upper bound on `𝔈`.
4. **Legitimacy of the models.** `Λ1_{n≥5}` and `a_θ` share every hypothesis of P46's form-level setting and the zeros
   and pole of ζ, but *not* the functional equation (`thm:finmod`(iii)). The counter-mechanism is therefore a class
   statement (Cor 3.4), not a statement about ζ. For ζ the converse is true at `T ≤ 0.8` (Zhu). A model with the
   functional equation (Epstein/Dedekind, P46 `rem:twohalves`) was not attempted.
5. **Imports.** `thm:index`/`cor:Tarch` (machine-verified, P46 archive), `thm:C` (machine-verified), Zhu Thm 1.2 (cited,
   not re-verified), Paper 42 `cor:certifiedinitialinterval`.
6. **Citation imprecisions noticed (not edited).** (a) P46 `prop:arch`(iii) (l.2376–2377) cites
   `[Paper42, Yoshida, Bombieri]` for positivity of **`W_T`** for `T ≤ log 2`. But Paper 42
   `cor:certifiedinitialinterval` (42/main.tex l.4354–4360) is a statement about the **primitive** operator on `P_T`.
   Yoshida/Bombieri cover autocorrelation support `log 2`, i.e. `T ≤ ½log 2`, which is all `prop:arch`(iii) needs, since
   `2T < log 2`. (b) The blueprint's "`T ≤ log 2` (Yoshida/Bombieri — `λ^W ≥ 0` known)" has the same slip. The
   complete form on `(½log 2, 0.8]` rests on Zhu. [amended per R156_004, A14: (a) CONFIRMED. P42
   `thm:certifiedendpoints`/`cor:certifiedinitialinterval` (42/main.tex l.4164–4172, 4355–4360) assert strict
   positivity on `P_T` of the operator with the *complete prime comb* ("complete" in P42 means all contacts, not
   the complete form `W_T`), so they are primitive statements. The same slip occurs at P46 l.308 ("Positivity at
   `T ≤ log 2` is known [Paper42, Yoshida, Bombieri]"), in `R155_031` l.51 and in `R155_023` l.87, 328. P46 l.148–150
   (intro) is correct as worded. (b) The quoted blueprint phrase was **not found verbatim** in `R156_000` or in the
   plan file. Remove the attribution, or give its location. Ruling: `R156_004` §"Citation ruling".]
   [amended per R156_004, A15, notation for integration: P46 already uses `G_T(t) = g(t/T)` and `F_T` in
   `prop:finsupp`, `S_{T,τ_1}`/`S_c` for time–band limiting, `Γ_T` for the pole-free archimedean form and `κ(x)` for
   the killing density. For the paper, rename `G_T → 𝔊_T` (or `G^{\mathrm{pol}}_T`), `S_T → S^{\mathrm{Sch}}_T`,
   `F_T → F^{\mathrm{odd}}_T`.]
7. **Tiny Galerkin numbers.** `g_+ ≈ 8.6·10^{-8}`, `θ_* ≈ 0.99991` and `g_+(θ)` non-monotone near `θ = 1` are float64
   Galerkin values: stable in `N ∈ {16,24,32}` but uncertified. `g_+(θ)` has a pole where `λ^A_ev(θ)` crosses 0
   (`θ ≈ 1.0065`), so its behaviour near `θ = 1` is plausible but unproved.
8. **D.47 hyperbolic `In(G) = (1,1)` versus this note's `G_T ≻ 0`.** They are different matrices. D.47's is `S_T` (the
   Green matrix of the local part), which is hyperbolic when `n_-(𝔞_T) = 1`. `G_T = S_T + J` must be positive for
   `λ^W ≥ 0`. Check that no corpus statement conflates them.
9. **`def:W` naming trap.** `def:W` is the weight class `𝒲_T`, while the complete form is `eq:W`. Any integration must
   cite `eq:W` for `W_T`.
