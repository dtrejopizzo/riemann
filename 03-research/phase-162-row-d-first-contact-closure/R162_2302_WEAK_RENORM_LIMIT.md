# R162_2302 — Cell 5F: the value and radicality of the weak-renormalization limit (R161_075–079)

Pure math, no numerics. Cell **5F** (integralidad ℤ × transformadas globales en T), ranking #5 of
R162_2300 §7. Nearest routes: R161_075–079 (5F, PARTIAL), R161_018 (W6), R162_803 (E1, Herglotz), R162_1003 (Thm R).

**Verdict: NO-GO as a Gate-1 mechanism, with three PROVED statements.**
- **Theorem N (PROVED).** Missing property (a) holds, but it holds for *every* primitive compact L² source, not only on the
  first-contact radical. The weak limit is **identically zero**, modulo the negative Tate line. With the canonical
  anchor it is exactly zero. The reason is ζ(1−ρ)=0, which is the functional equation (FE) read on the zero atoms of
  A_loc f. This is the proved, weak-carrier form of R161_018's Z A_∞ = 0. R161_075's objection is answered for this
  carrier: A_loc f ≠ 0 there, and each of its atoms is killed by the Poisson multiplier, as in R161_075 (3.1).
- **Theorem V (PROVED).** Missing property (b), read as "the anchored continuum maps the radical into itself", implies
  radical = {0}, because a Volterra operator has no finite-dimensional invariant subspace. So (b) *is* Gate 1. A single
  scalar obstruction c_f blocks it (§4).
- **Prop. O (PROVED).** Before regularisation, the Poisson sampling over ℕ and the right Euler current compose with
  *opposite* orientation. Their product is ζ(1−s)·(ζ′/ζ)(s), not the Dirichlet product ζ′. The only place where
  1∗Λ = log (integrality plus Euler) appears is a finite cross term, which is W7 and passes Beurling. S7 fails.

So (a)+(b) do not close Gate 1. (a) is information-free: it is F1 and FE-level. (b) is Gate 1 restated.

## 0. Falsifier lines (written before the proofs)

| model | (a) value null? | (b) / Thm V | verdict |
|---|---|---|---|
| **DH** (FE, no Euler) | Take the matched object, i.e. sample with the DH Dirichlet coefficients. Then the value is null by L_DH(1−ρ)=0 for every DH zero, including the off-line ones, *wherever the construction converges* | identical | passes ⇒ the value is FE-level (F3) |
| **Epstein** | null by FE with the r_Q(n) sampling | identical | passes (T2) |
| **deletion Λ1_{n≥5}** | Not null. R^del f = Z·(Df) with D = Σ_{n=2,3,4}Λ(n)n^{-1/2}(V_{log n}+V_{−log n}), which is ≠ 0 for generic f | identical | "separates", but uniformly in f: it detects the explicit formula, not the radical |
| **κ / finmod** | same as deletion | identical | same |
| **Λχ₂** | Matched sampling χ₂(n) gives null (FE of L(s,χ₂)). Mismatched sampling 1 gives non-null | identical | The matched system passes. The object checks only that Λ = coefficients of −(log sampling series)′ |
| **Beurling DMV** | Matched sampling over 𝒩_B satisfies the R161_078 PNT input, since DMV systems have exactly the dlVP remainder. There is no FE, so the value is non-null or undefined | identical | Separated by the **FE**, not by ℤ. It is W3-adjacent: a separation that carries no sign |
| **two-atom Type I** s₂δ_{log2}+s₃δ_{log3} | no FE ⇒ non-null for every f | identical | The object cannot see the Type I contact. The spectral content is empty |

Line conclusion: whatever the object separates, it separates for **all** f. It never sees the first-contact
radical. That is F1 before any proof is written.

## 1. Set-up (R161_076/079 conventions)

f ∈ L²[−T,T] with (1.1) ∫e^{−u/2}f = 0. A_loc = 𝓜_Γ − L_∞ − L_∞*. T_N h(t) = Σ_{n≤N} n^{−1/2}h(t+log n) −
∫_1^N x^{−1/2}h(t+log x)dx. v is any solution of (∂+½)v = h, and R(f) := lim_N (T_N − v) A_loc f in D′, modulo
e^{−t/2}. Existence is R161_079. For pairings, put k = f∗φ̌. This is compact and smooth, and K(0) = 0 in the
factored sense of R161_079 (2.1). Write K(s) = ∫k(u)e^{(s−½)u}du, which is entire and of rapid decay on vertical strips.

**Explicit formula as a distribution identity (classical, Weil).** Apply the explicit formula to the translates of k:

  A_loc k(t) = a_k e^{t/2} + b_k e^{−t/2} + Σ_ρ K(ρ) e^{(ρ−½)t},   (1.2)

up to the fixed normalisation constants. The sum runs over the nontrivial zeros with multiplicity; the Γ factor and the
trivial zeros are absorbed into 𝓜_Γ. The sum converges absolutely and locally uniformly in t, and each term is
O(e^{(β−½)|t|}). This is also why A_loc k lies in X_η for η > ½ (R161_076 §2). Primitivity gives b_k = 0.

## 2. Theorem N (value null on every primitive source)

**Theorem N.** For every f satisfying (1.1), R(f) ≡ 0 mod span{e^{−t/2}}. With the canonical anchor
v = e^{−t/2}∫_{−∞}^t e^{y/2}A_loc f, R(f) = 0 exactly. That anchor converges because b = 0 and β > 0.

*Proof.* Put w = 1−ρ, so 0 < Re w < 1. Euler–Maclaurin gives
Σ_{n≤N}n^{−w} = ζ(w) + N^{1−w}/(1−w) + E_N(w), with |E_N(w)| ≤ (1+|w|/Re w) N^{−Re w}.
Hence T_N e^{(ρ−½)·}(t) = e^{(ρ−½)t}[ζ(1−ρ) + 1/ρ + E_N(1−ρ)]. The solution of (∂+½)v = e^{(ρ−½)t} is
v_ρ = e^{(ρ−½)t}/ρ. Therefore

  (T_N − v)e_ρ → ζ(1−ρ) e_ρ = 0,

because the zero set is symmetric, ρ ↦ 1−ρ (FE). The same holds in the opposite orientation: ζ(ρ) = 0.

For the Tate mode e^{t/2}: T_N gives 1·e^{t/2} and v = e^{t/2}, so the difference is 0. The term e^{−t/2} is the
quotient.

Interchange with the ρ-sum: the classical zero-free region gives 1/Re w ≪ log|ρ|. Then
|E_N| ≪ |ρ| log|ρ| uniformly in N, while |K(ρ)| ≪_A |ρ|^{−A} on the strip. Dominated convergence applies. ∎

*Remarks.*
(i) This gives a second convergence proof of R161_079 that needs no PNT remainder. It uses only the explicit formula
and the zero-free region at Re s = 1.
(ii) On the first-contact radical the statement is the same. The radical plays no role (**F1**).
(iii) This is the physical, weak-carrier version of R161_018 (2.6). R161_075's L² injectivity does not apply, since
A_loc f ≠ 0 is a sum of zero atoms and each atom is annihilated by ζ, exactly as in R161_075 (3.1). **W6 is restored
for this limit.** The row in R162_2300 §3 W6 no longer needs the caveat for the weak carrier.

## 3. Prop. O — where ℤ and Euler enter, and in which order

Expand the finite stage T_N applied to L_∞ k(0) and to L_∞* k(0) in Mellin form.

- **Right current** l₊. It produces k(log n − log m), whose Mellin factors as n^{a}m^{−a}. We would need
  Σ n^{a−½} (Re a < −½) and Σ Λ(m)m^{−a−½} (Re a > ½) at the same time, and no a satisfies both. So the product has
  symbol ζ(½−a)·(−ζ′/ζ)(½+a). This is an FE-type pairing of opposite orientations. It is **not** a Dirichlet
  convolution, and it is defined only after the continuum renormalisation. The Euler product enters only through
  "no zeros on Re s = 1", which is where R161_078 uses the PNT.
- **Left current** l₋. It produces k(log(nm)), which is a *finite* sum at each output point:
  Σ_q q^{−½}k(log q)(Λ∗1)(q) = Σ_q q^{−½} log q · k(log q). This is the only place where integrality and Euler meet
  multiplicatively before regularisation. It is Λ∗1 = log, i.e. W7, and it holds verbatim for Beurling with 𝒩_B.
- **Integrality of ℤ** enters through the sampling set {log n}, n ∈ ℕ. Its only effect on the value is to make the
  multiplier equal to ζ itself, the function whose logarithmic derivative is ΣΛn^{−s}. Nothing in the value uses
  integrality beyond this matching (see the Λχ₂ and Epstein lines).

⇒ **S7 fails.** Euler never enters before regularisation in a non-W7 way.
⇒ **S2 fails.** f ↦ R(f) is linear in the source and in the test. As a global transform in the shift/Poisson
variable, it collapses even below the Herglotz level of R162_803: to the FE identity ζ(1−ρ)=0, which is true and
carries no information.

## 4. Theorem V — radicality preservation is Gate 1

Let 𝓡 = ker H_T at first contact, H_T = P_T A_loc P_T. As in P46, H_T is the Γ multiplier plus a compact operator, so
𝓡 is finite-dimensional. Let (Vf)(t) = e^{−t/2}∫_{−T}^t e^{y/2}f(y)dy on L²[−T,T]. This is the canonical preimage
of the anchor: v = A_loc(Vf) + (exterior).

**Lemma V1 (PROVED).** For f ∈ 𝓡, P_T A_loc(Vf) = c_f e^{−t/2}|_{[−T,T]}, where
c_f := −∫_{−∞}^{−T} e^{y/2}(A_loc f)(y)dy is the left-exterior Tate moment.
*Proof.* (∂+½) commutes with A_loc, and for f ∈ 𝓡 the compressed part vanishes. Integrate from −∞ and split at −T. ∎

So "(b): the anchored continuum preserves radicality", meaning V𝓡 ⊂ 𝓡, is equivalent to c_g = 0 along 𝓡 and its
V-iterates (with the Tate moments needed to stay compact).

**Theorem V (PROVED).** If 𝓡 is finite-dimensional and V𝓡 ⊂ 𝓡, then 𝓡 = {0}.
*Proof.* Suppose 𝓡 ≠ {0}. Then V|_𝓡 has an eigenvector g ≠ 0 with Vg = μg. μ = 0 is impossible because V is
injective. If μ ≠ 0, then g = μ^{−1}Vg is absolutely continuous and satisfies (∂+½)g = μ^{−1}g, so
g = Ce^{(1/μ−½)t}. Also g(−T) = μ^{−1}(Vg)(−T) = 0, so C = 0, a contradiction. ∎

The converse is trivial: if 𝓡 = {0}, (b) holds vacuously. **Hence (b) on the first-contact radical ⟺ radical
trivial ⟺ Gate 1.** This is a restatement, E1-type. It is *more precise* than "radicality not preserved", though:
the whole obstruction is the scalar c_f, the exterior Tate moment that R161_077 §4 removed. By (1.2),
c_f = Σ_ρ F(ρ)e^{−ρT}/ρ + (Tate), which is a zero-side scalar. Forcing c_f = 0 is a zero-side statement, so it is E1.

## 5. F1, F2, M

- **F1:** fails. Theorem N holds on every vector, and Theorem V holds for every finite-dimensional invariant subspace.
  Neither uses λ = 0.
- **F2:** the value is orientation-symmetric (ζ(ρ) = ζ(1−ρ) = 0) and carries no sign, so there is nothing to orient.
  Theorem V is sign-free. Not killed by F2, but no sign is present.
- **M:** does not apply, since there is no margin or per-window gap. Only c_f carries content, and c_f is a zero sum
  (E1 before M).

## 6. Status and residual

- PROVED: Theorem N, Lemma V1, Theorem V, Prop. O. Cited classical inputs: the explicit formula for C_c^∞ tests, the
  zero-free region, and finite-dimensionality of 𝓡 (P46).
- Cell 5F: ◧ → **◩**. Killers: F1 (value), E1 (radicality = Gate 1), S2/S7 failure.
- **Residual O2302.1** (formulated, not attacked): the finite-N remainder Σ_ρ K(ρ)E_N(1−ρ) ~ Σ_ρ K(ρ)N^{ρ−1}(…).
  It is the only nonzero content of the construction. Paired quadratically, it is a Li/Keiper-type zero sum, so E1 is
  expected.
- **Residual O2302.2:** the exterior Tate scalar c_f on 𝓡. Gate 1 ⟺ no nonzero f ∈ 𝓡 has c_{V^j f} = 0 for all j. A
  proof of c_f ≠ 0 from integrality would be new, but by (1.2) it is a zero-side functional.
- Grid note: the §3 W6 caveat ("R161_018 unproved as written") now holds only for L² and meromorphic carriers. In the
  weak distribution carrier, R161_018's conclusion is PROVED by Theorem N.
