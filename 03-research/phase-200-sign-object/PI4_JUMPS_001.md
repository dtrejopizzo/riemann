# PI4_JUMPS_001: Lemma Π.4, jumps of the minimal-leak representative and jump comb (phase 200, round 5b)

Arithmetic on published data is marked NUMERICAL; no new computation was run.
NO-GO / REF-D / NUMERICAL. **No sign is proved. L′♯ OPEN. Row D OPEN.**

**Read.** PI_MU_001 (complete); B1_FLAT_001; AUDIT_200_AMU_001; index l.479 (TEST_KINKS_001), l.487 (FF_001),
l.495 (HH_001); PROOF_L_SHARP_FF_001_EDGE_RECOMBINATION §3 (FF.2); MORI15_EXTREMAL_001 §2 and §4; Paper 46: eq:symbol,
eq:W, lem:roughEF (l.866), def:ext, lem:ext-mob, thm:ext-half, rem:ext-killing, prop:ext-gauge, prop:ext-consol,
prop:ext-univ (l.9601–9745).

## 0. Index check

Grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/README.md` for "jump", "kink", "discontinu", "f♯", "minimal leak",
"jump comb", "HH_001", "TEST_KINKS", "FF.2", "edge jet" and "restriction 26":

| entry | content | relation to this memo |
|---|---|---|
| l.495 HH_001 (NO-GO) | Möbius kink tails K_m at u = λ/m; restriction 26 (renumbered 28): "no splits jump/kink of the edge jet, quadratic forms in (g(T), g′(T))" | **different object**, see below |
| l.479 TEST_KINKS_001 (NO-GO NUMERICAL) | jumps of E⁻¹p at λ/m of size μ(m)(h, mh′, m²h″)(λ); divergent jet series | **different object** |
| l.487 FF_001, Theorem FF.2 | Ψ̌ = c_μμ^{−½}g(2a−x) + [Φ_{φ₀}(−x) + ½φ₀(0)e^{−x/2} − ½f̂(0)e^{x/2}] | the polar term ½φ₀(0)e^{−x/2} **is already on record**. It is used here (§2) and shown to obstruct Π.4 literal |
| l.350 𝖯⋆ | jump measure J_T ≥ 0 (Markov criterion) | another object (window side); unrelated |
| l.524 PI_MU_001 | f♯ with jumps (ARGUED), Π.4 OPEN | starting point |

Searches for "f♯", "minimal leak" and "jump comb" only return PI_MU (l.524).

**New reason written (why this is not HH_001/TEST_KINKS/restriction 28).**
1. *Position.* Here the jump is at the inner edge u = 1/λ of the gauge. Those of HH/TEST_KINKS are at
   u = λ/m ∈ (1/λ, λ].
2. *Origin.* Here the jump is created by the L² orthogonal projection onto 𝒢̄_T (Π.0): the minimizer sees no
   boundary condition. Those of HH are created by the Möbius inversion when the m term switches on.
3. *Existence in the core.* In the core g(±T) = g′(±T) = 0, so the Möbius jumps μ(m)g(T)/√λ **vanish** and only
   jets of order ≥ 2 remain (that is what HH/TEST_KINKS tried to model). By contrast σ(g) ≠ 0 in the core
   (Prop. 1.2, PROVED). σ is not a function of (g(T), g′(T)): it depends on the interior values g(log m − T) and
   on an L² functional of g. So restriction 28 does not cover it.
4. *Image in the tail.* A single jump produces, via summation, a comb at T + log n with weights n^{−½} (a_n ≡ 1,
   no μ). In HH/TEST_KINKS there are many jumps with weights μ(m) and each gives a local tail.

The difference is real. What **is** inherited: the polar term of FF.2 (§2.2).

---

## 1. Exact f♯ and its jump

Notation from PI_MU: I = [−1/λ,1/λ], B = band projection (−λ,λ), f_out = E⁻¹g on 1/λ < |u| ≤ λ (even), f♯ = f − φ*,
with φ* ∈ L²_0 minimizing ‖Q𝓕(f − φ)‖.

### 1.1 Equation for f♯ (PROVED)

The Euler–Lagrange condition is: P𝓕*Q𝓕f♯ ⊥ L²_0 on I, i.e. (1 − B)f♯ ≡ c on I. Call ψ := (1 − B)f♯ = Ch♯.
Then:
- on I: f♯ = c + Bf♯ (B f♯ is entire, so f♯|_I is real-analytic **up to the closed boundary**);
- outside I: f♯ = f_out, which is C² on (1/λ, λ] up to 1/λ⁺ (lem:ext-mob: the term m = N switches on at u = 1/λ,
  where g vanishes to second order);
- c is fixed by ∫f♯ = 0.

The solution is unique and depends on f_out in an L²-bounded way, with constant (1 − χ_0)⁻¹ (Π.0). This is the
equation of PI_MU §2.3. Also r_{f♯} ∈ 𝒦_T, as required by Π.0′ (Ch♯ ≡ c on I).

### 1.2 Proposition 1.2 (the jump exists and is not controlled; PROVED)

Define σ(g) := f♯(1/λ⁺) − f♯(1/λ⁻) = f_out(1/λ⁺) − c − (Bf♯)(1/λ). The following hold:
(a) **closed formula:**
  σ(g) = λ^{½}Σ_{m≤N}μ(m)m^{−½}g(log m − T) − ν(f_out),
  where ν(f_out) = c + (Bf♯)(1/λ) is an **L²-bounded** linear functional of f_out (the value of a band-limited
  function is L²-continuous, |Bh(x)| ≤ (2λ)^{½}‖h‖, and c, f♯ depend L²-continuously on f_out);
(b) σ ≢ 0 in the core;
(c) σ is bounded neither by ‖g‖, nor by ℓ(g), nor by W_T(g): there exists g_ε in the core with ‖g_ε‖, ℓ(g_ε),
  W_T(g_ε) → 0 and σ(g_ε) → −(λ/2)^{½}.

*Proof.* (a): the first term is lem:ext-mob at u = 1/λ (mu ≤ λ ⟺ m ≤ N). (b, c): let g_ε be a C² plateau of height
1 and width ε, centered at x₀ = log 2 − T ∈ (−T, T) (because N ≥ 5), with the core constraints at ±T. For m ≠ 2,
log m − T ∉ supp g_ε if ε is small, so the first term equals μ(2)(λ/2)^{½} = −(λ/2)^{½}. On the other hand
‖f_out‖ ≤ 2√N‖g_ε‖ = O(√ε), so ν → 0. The other quantities also tend to 0:
- ℓ(g_ε) ≤ C₁N²ε, by lem:ext-ellbound;
- W_T(g_ε) ≤ (1/2π)∫|m||ĝ_ε|² + 2|AB| = O(ε log(1/ε)), because ĝ_ε has mass ε up to frequency 1/ε. □

**Answer to task 1.** The jump that PI_MU gave as ARGUED becomes PROVED: f♯ jumps at ±1/λ. Correction of
language: what jumps is **f♯ in the variable u**. f̂♯ does not jump; it has oscillating tail
 r_{f♯}(ξ) = −σ sin(2πξ/λ)/(πξ) + O(ξ^{−2})  (ξ → ∞),  (1.1)
obtained by integrating by parts 2∫f♯cos(2πuξ)du with f♯ even and piecewise C². "Closed formula in the prolate
basis": the part f_out(1/λ⁺) is explicit (Möbius) and ν is the value at 1/λ of the Fredholm solution of §1.1. In
the prolate basis of I × (−λ,λ):
 ν(f_out) = c + Σ_k χ_k(1−χ_k)⁻¹⟨Bf_out, ψ_k⟩ψ_k(1/λ) + (rank 1),
which is PROVED as an identity. It has no shorter form: it is the same resolvent of Π_μ.

### 1.3 Lemma 1.3 (second boundary datum: f♯(0); PROVED / ARGUED)

f♯(0) = c + (Bf♯)(0) is an L²-bounded functional of f_out (PROVED). Nothing forces it to vanish, because the
constraint φ(0) = 0 is not L²-closed (Π.0). That it is **generically** ≠ 0 is ARGUED. There is an indirect
NUMERICAL hint in MORI15 §4: "a₄² = 3.32 fixed by f(0) = 0." The constraint f(0) = 0 is the one that forces 81% of
the leak in the polynomial family; in L² that constraint costs nothing (a spike of width ε has leak O(ε)), so the
free minimizer has f♯*(0) ≠ 0, probably of order 1. **Side consequence:** the ℓ* ∈ [4.4, 8.5]·10⁻⁷⁰ of MORI15 is
an **upper bound** for the ℓ of def:ext, not its value. See §5.

---

## 2. Exact tail of E f♯ and Lemma Π.4

### 2.1 Proposition 2.1 (exact tail; PROVED)

For y > T, with δ = e^{−y} and w = e^{y−T}:
 Ψ̌_{f♯}(y) = e^{−y/2}Σ_{n≥1}f♯(nδ) = e^{−y/2}[−½f♯(0) + σ(g)B̄_1(w) + R(y)],  R(y) = O(e^{−y}),  (2.1)
with B̄_1(t) = {t} − ½ (and mean value at the jumps). In particular:
- Ψ̌_{f♯} jumps **exactly** at y = T + log n (n ≥ 1), and the jump equals −σ(g)λ^{−½}n^{−½};
- the sum Σ_n f♯(nξ) is **finite** for each y (f♯ has support in [−λ,λ]), so there is no convergence issue on the
  u side;
- the Poisson version Zr_{f♯}(e^y) = e^{y/2}Σ_n r_{f♯}(ne^y) converges only **conditionally** (Dirichlet test, by
  (1.1)) and equals, at every point of continuity,
 Zr_{f♯}(e^y) = Ψ̌_{f♯}(y) + ½f♯(0)e^{−y/2} = e^{−y/2}[σB̄_1(w) + R(y)].  (2.2)

*Proof.* Order-1 Euler–Maclaurin for f♯ even and piecewise C². The break points are 0 (where f♯ is smooth), ±1/λ
(jump σ and jump of f′) and λ (jump of f′). With ∫_0^∞f♯ = 0 this gives
 Σ_{n≥1}f♯(nδ) = −½f♯(0) + Σ_{jumps a}σ_aB̄_1(a/δ) + O(δ),
and at a = 1/λ we have a/δ = w. The jump positions are read off directly: nδ crosses 1/λ at y = T + log n. For
(2.2): Poisson with f̂♯(0) = 0 gives Σ_{n≥1}f♯(nδ) = −½f♯(0) + δ⁻¹Σ_{k≥1}f̂♯(k/δ), and k/δ > λ. □

This proves the form conjectured in PI_MU §2.4: there is a jump comb of weight n^{−½} at T + log n. But (2.1) adds
something PI_MU did not see: a **Tate mode** −½f♯(0)e^{−y/2}. It is the polar term ½φ₀(0)e^{−x/2} of FF.2, here
with φ₀ = −φ* not C² at 0.

### 2.2 Π.4 literal: NO-GO if f♯(0) ≠ 0 (PROVED)

thm:ext-half requires |Ψ(y)| ≤ Ce^{−3y/2}. By (2.1), Ψ̌_{f♯} decays only like e^{−y/2}.
- If f♯(0) ≠ 0, the Tate moment of the growing part, ∫_T^∞Ψ̌_{f♯}e^{y/2}dy, **diverges linearly** (−½f♯(0)·∞).
  The comb Σv_q c(log q) also diverges, like Σ_qΛ(q)/q. Moreover Ψ̌_{f♯} ≠ Zr_{f♯}, so the derivation of
  thm:ext-half (which uses Ψ̌ = Zr) does not apply.
- Zero side: Φ_{Ψ_{f♯}}(s) = ζ(s)𝓜f♯(s) − Φ_g(s) has a pole at s = 0 with residue ζ(0)f♯(0) = −½f♯(0). The
  explicit formula receives an infinite polar term. **Φ_{φ*} is not in the radical** when φ*(0) ≠ 0: the L²
  closure of the gauge (Π.0) exits the domain of 𝒲.

**Theorem 2.2 (NO-GO, PROVED).** The formula of thm:ext-half evaluated term by term on Ψ̌_{f♯} is divergent if
f♯(0) ≠ 0. Guo L4.4 does not extend to φ ∈ L²_0 with φ(0) ≠ 0.

### 2.3 Corrected Π.4

**(Π.4-zeros) PROVED.** For **every** bounded, even representative f with support in [−λ,λ] (in particular f♯)
and for every zero ρ: Φ_{Ψ_f}(ρ) = ζ(ρ)𝓜f(ρ) − Φ_g(ρ) = −Φ_g(ρ). The integral converges because Re ρ > 0 and
Ψ_f(x) = O(e^{x/2}). Hence
 W_T(g) = Σ_ρΦ_{Ψ_{f♯}}(ρ)Φ_{Ψ_{f♯}}(1−ρ),
with absolute convergence (Φ_g(ρ) = O(|ρ|^{−2}) in the core). The zero side is blind to the representative. **The
jump comb does not exist on the zero side**: it only redistributes mass among the terms of the prime side.

**(Π.4-primes) CONDITIONAL on (EF♭).** Let Ψ^♮ := Zr_{f♯} (without the mode, by (2.2)). Then:
(i) **all** terms of thm:ext-half converge on Ψ^♮ (PROVED):
- the archimedean term: |Ψ^♮|² ~ σ²e^{−y}/12 at local frequency ~ 2πw, and ∫e^{−y}(y − T)dy < ∞; the Lévy energy
  of a sawtooth of period d and amplitude j is j²log(1/d) per unit length, not per jump;
- A(Ψ^♮) = σ∫_1^∞B̄_1(w)dw/w + (abs. conv.), which converges **conditionally** to σ(½log 2π − 1) + …;
- B(Ψ^♮) converges absolutely;
- the comb converges absolutely: c_J(log q) = O(σ²λ⁻¹q^{−3/2}) because ∫_k^{k+1}F(w)B̄_1(qw)dw = O(1/q) for F of
  class C¹ on [k, k+1] (integration by parts with B̄_2). Hence Σv_q|c(log q)| ≲ ΣΛ(q)q^{−2} < ∞.
(ii) The identity is
 W_T(g) = 𝒲[Ψ^♮] − 2a₀𝒲⁰(g, 𝔪) − a₀²λ⁻¹(2 + γ − log 4π),  a₀ := ½f♯(0),  (2.3)
with 𝔪(x) = e^{x/2}1_{x<−T} (the Tate mode, Φ_𝔪(s) = e^{−sT}/s) and 𝒲⁰ the zero-side pairing:
𝒲⁰(g, 𝔪) := Σ_ρ Φ_g(ρ)e^{−(1−ρ)T}/(1−ρ). That pairing converges absolutely.
*Proof of (ii).* On the zero side, Φ_{Ψ^♮}(ρ) = −Φ_g(ρ) + a₀e^{−ρT}/ρ. One expands Σ_ρΦ(ρ)Φ(1−ρ) and uses
Σ_ρ1/(ρ(1−ρ)) = 2Σ_ρ1/ρ = 2 + γ − log 4π (symmetric sum; CITED, Davenport ch. 12). What is missing is (EF♭): the
explicit formula 𝒲[Ψ] = Σ_ρΦ_Ψ(ρ)Φ_Ψ(1−ρ) for non-compact tails of the form e^{−y/2}×(mean-zero sawtooth) +
O(e^{−3y/2}), with Φ_Ψ(0) and Φ_Ψ(1) as conditionally convergent values, or by analytic continuation (which
exists: §3.1). lem:roughEF only covers compact support. The extension by truncation as Y → ∞ is routine on the
prime side; on the zero side it needs a uniform bound on the Mellin tails. **CONDITIONAL.** □

**Reading of (2.3).** If f♯(0) = 0, Π.4 holds as is on Ψ^♮ = Ψ̌_{f♯} (CONDITIONAL on EF♭): the jump does **not**
obstruct. What obstructs is the Tate mode, and it contributes two explicit corrections: a rank-one one, with the
constant 2 + γ − log 4π, and a cross term with g. **Correction to PI_MU §3.2(ii):** the identity
𝒲̄(Π_μr) = 𝒲[ZΠ_μr] is false in general. It holds only via admissible representatives (Π.3) or with the
corrections of (2.3).

---

## 3. The jump comb in 𝒲

### 3.1 Exact computation of the self-form (CONDITIONAL on EF♭)

Let j(y) := e^{−y/2}B̄_1(e^y)1_{y>0}. By (2.2) and translation invariance, the σ² part of 𝒲[Ψ^♮] is
 𝒲[σλ^{−½}w^{−½}B̄_1(w)] = (σ²/λ)·c_J,  c_J := 𝒲[j].
The number c_J is **universal**: it does not depend on μ, g, or T.

*Mellin (PROVED).* Φ_j(s) = ∫_1^∞B̄_1(w)w^{−s−1}dw =: β(s). By the classical formula
ζ(s) = s/(s−1) − ½ − s∫_1^∞B̄_1w^{−s−1}dw (valid for Re s > −1; CITED) one gets
 β(s) = 1/(s−1) − 1/(2s) − ζ(s)/s.
β is **entire**: the poles at s = 0 and s = 1 cancel. Its values are β(0) = ½log 2π − 1 and β(1) = ½ − γ, and at
the zeros
 β(ρ) = 1/(ρ−1) − 1/(2ρ)  (no ζ).
With p = ρ and q = 1 − ρ: β(ρ)β(1−ρ) = (5/4)/(pq) + ½(p^{−2} + q^{−2}). Summing over ρ (absolute convergence),
 c_J = (5/4)(2 + γ − log 4π) + Σ_ρρ^{−2} = (5/4)(2 + γ − log 4π) + (1 + γ² + 2γ₁ − π²/8),
where Σ_ρρ^{−2} = 1 + γ² + 2γ₁ − π²/8 (CITED, Keiper/Li). Numerically (NUMERICAL arithmetic):
 c_J = 0.0577393 − 0.0461543 = **+0.0115850**.

*Prime-side form (PROVED as identity, convergence per §2.3(i)).* With r_J(ξ) = −σsin(2πξ/λ)/(πξ):
- I_J(m,n) = (σ²/π²λ)(mn)^{−½}·k(m,n), with
 k(m,n) := ∫_1^∞w^{−2}sin(2πmw)sin(2πnw)dw = ½[K(m−n) − K(m+n)],  K(a) := ∫_1^∞w^{−2}cos(2πaw)dw.
- K(0) = 1 and K(a) = O(a^{−2}) for a ∈ ℤ∖{0}, because sin(2πa) = 0 cancels the boundary term.
- Comb term: −2Σ_{m,n}(mn)^{−½}(log n)I_J(m,n) = −(2σ²/π²λ)Σ_{m,n}(mn)^{−1}(log n)k(m,n).
- Its diagonal equals −(σ²/π²λ)Σ(log n)/n²·(1 − K(2n)) ≈ (σ²/π²λ)ζ′(2) ≈ −0.095σ²/λ. It is equivalent to
 −(σ²/6λ)(−ζ′/ζ)(2)·(1 + o(1)) in the Σv_qc(log q) notation (the two agree because ζ′(2)/(2π²) = ζ′(2)/(12ζ(2))).
  The value "≈ 0.095" is ARGUED: it approximates ∫_1^∞t^{−2}P(t)dt by the mean of P.
- The comb term in the Z_log picture is Z_log r_J(w) = −σw^{−½}L(w/λ), with
 L(t) := Σ_{n≥2}(log n)sin(2πnt)/(πn) = log Γ(t) − ½log 2π + ½log(2 sin πt) − (γ + log 2π)(½ − t)  (0 < t < 1),
  which is the Kummer series (CITED). L is real-analytic on (0,1) and has logarithmic singularities **only at
  integers**.

**Answer to "what is k?"** The conjectured form σ²Σ(mn)^{−½}k(log m/n) **is false in two respects**:
- the weight is (mn)^{−1}: one factor (mn)^{−½} comes from the summation and another from the 1/ξ tail;
- the kernel k(m,n) = ½[K(m−n) − K(m+n)] depends on m ± n (the **additive** structure), not on log(m/n).
It is the Gram matrix of {sin(2πm·)} in L²((1,∞), w^{−2}dw), so it is positive semidefinite (PROVED). But it
appears contracted with an asymmetric weight log n. **It is not a quadratic form in free variables: it is a
scalar.** The contribution of the jump comb to 𝒲 is
 σ(g)²·c_J/λ + 2σ(g)·𝒲(J₁, S_g),  (3.1)
with J₁ = λ^{−½}w^{−½}B̄_1(w) and S_g the remainder of (2.2). That is, the quadratic part has **rank one in g,
with universal coefficient**. It is not REF-D and it is not the full window form.

### 3.2 Where does Λ enter? P10-formula (PROVED except where noted)

| ingredient | origin | Λ | cΛ | a_P | Beurling |
|---|---|---|---|---|---|
| weights n^{−½} | summation (a_n ≡ 1) | same | same | same | n_B^{−½}: same in form |
| positions T + log n | summation over ℕ | ℕ | ℕ | ℕ | T + log n_B (non-integer) |
| kernel k(m,n) | 1/ξ tail + summation | same | same | same | summation over n_B: k(m_B,n_B) |
| Z_log of the comb: singularities | **weights Λ∗1 = log** | log-sing. only at t ∈ ℤ (Kummer) | c·L: same positions | **new jumps at t ∈ p^{−k}ℤ∖ℤ** | per Λ_B∗1 |
| c_J | zero side, ζ | +0.01158 | c_J + (c−1)κ_comb, with κ_comb ≈ −0.095 (ARGUED) | no value: radicality fails | — |

*a_P (PROVED, finite P).* With weights a_n = log n − Σ_{p∈P}v_p(n)log p:
 Σ_n v_p(n)sin(2πnt)/(πn) = Σ_{k≥1}p^{−k}Σ_m sin(2πmp^kt)/(πm) = −Σ_{k≥1}p^{−k}B̄_1(p^kt).
The series converges uniformly (|B̄_1| ≤ ½ and Σp^{−k} < ∞). Hence L_P = L + Σ_{p∈P}(log p)Σ_kp^{−k}B̄_1(p^k·), and
jumps of size (log p)p^{−k} appear at t = j/p^k, i.e. at positions T + log(j/p^k) ∉ T + log ℕ. **The jump-comb
formula distinguishes a_P by the positions of the singularities of the image Z_log**, not by the jump comb of Ψ̌,
which is identical.

*cΛ.* Same positions, scaled amplitude. By (3.1), c_J changes linearly in c and would change sign around
c ≈ 1.12 (ARGUED, from the approximation of κ_comb).

*Beurling.* If the summation is done over Beurling integers (the natural version of def:ext for ζ_B), the
positions are T + log n_B. With summation over ℕ and a Beurling comb, the jump comb is that of ℕ, but radicality
fails.

**Where exact Λ enters.** Not in the weights n^{−½} (those come from the summation: comb-generic). Not in the
positions of the jump comb of Ψ̌ either: these too come from the summation, and the summation is the same for Λ,
cΛ and a_P. It enters:
- in the **regularity of the image Z_log** (Kummer's theorem: Λ∗1 = log gives singularities only on ℤ);
- in the **value** c_J = +0.01158, via the ζ constants (γ, γ₁, log 4π) of the zero side.

### 3.3 Is it a sign object? (task 4)

**Theorem 3.3 (NO-GO as a sign object; PROVED given (3.1), which is CONDITIONAL on EF♭).**
(a) The quadratic part of the jump comb is σ(g)²c_J/λ, with c_J = +0.01158 > 0: it is **positive definite**
(rank one).
(b) No inequality W_T(g) ≥ κσ(g)² or ℓ(g) ≥ κσ(g)² holds for κ > 0. By Prop. 1.2(c), on the family g_ε one has
σ²c_J/λ → c_J/2 ≈ 0.0058 while W_T(g_ε) → 0 and ℓ(g_ε) → 0. Hence the cross term 2σ𝒲(J₁, S_g) and 𝒲[S_g]
**cancel** the positive term at scale O(1) while the total tends to 0: this violates P2 (it is not at leak scale),
just like B₊ in PI_MU (B1_FLAT).
(c) The positivity of c_J comes from the zero side (ζ constants), not from an (ℕ,+,·) mechanism visible on the
prime side. On the prime side it is a residue of ≈ 11% of a cancellation (archimedean + AB ≈ +0.107, comb ≈
−0.095; ARGUED), which is not stable under cΛ.
(d) The additive structure k(m ± n) exists, but is **dominated by the diagonal** (K(a) = O(a^{−2})). The
interaction m ≈ kn of the semiring principle does not appear: pairs m ≈ kn with k ≥ 2 enter with weight
K((k ± 1)n) = O(n^{−2}).

**Difference from HH_001/TEST_KINKS (argued).** There the object was many local tails, with weights μ(m) and a
divergent jet series. Here there is **a single scalar σ(g)** with a closed universal coefficient. The failure is
also of a different type:
- HH/TEST_KINKS fail from non-locality (the jets do not resum);
- here the formula is exact and converges, but the term is not at scale (Prop. 1.2(c)).
Both end up in the same place: the representative contributes no sign (Π.3 / R-Π).

---

## 4. What remains of Lemma Π.4

| statement | status |
|---|---|
| f♯ jumps at ±1/λ; formula for σ; σ not bounded by ‖g‖, ℓ nor W | PROVED |
| f♯(0) L²-bounded functional; ≠ 0 generically | PROVED / ARGUED |
| exact tail (2.1); jump comb −σλ^{−½}n^{−½} at T + log n; Tate mode −½f♯(0)e^{−y/2} | PROVED |
| Π.4 literal (thm:ext-half on Ψ̌_{f♯}) if f♯(0) ≠ 0 | NO-GO (PROVED: diverges) |
| Π.4-zeros (zero side blind to the representative) | PROVED |
| convergence of all terms on Ψ^♮ = Zr_{f♯} | PROVED |
| identity (2.3) with mode correction 2 + γ − log 4π | CONDITIONAL (EF♭) |
| c_J = (5/4)(2+γ−log 4π) + Σρ^{−2} = +0.01158 | CONDITIONAL (EF♭); NUMERICAL arithmetic |
| conjectured form σ²Σ(mn)^{−½}k(log m/n) | FALSE in form: (mn)^{−1}, k(m ± n) |
| a_P: jumps of Z_log at p^{−k}ℤ | PROVED |
| jump comb as a sign object | NO-GO (P2; PROVED via Prop. 1.2(c)) |

---

## 5. Test μ = 15

Published data (MORI15 §2, §4): f₁(1/λ⁺) = 1.5257, λ = √15 = 3.873, W* = 4.7634661356·10⁻⁷⁰,
ℓ* ∈ [4.4, 8.5]·10⁻⁷⁰, Legendre polynomial gauge M = 28 with f(0) = 0.

- **σ(g*) of the Mori representative is 0**: its gauge is C² and crosses 1/λ continuously. The σ of f♯* requires
  ν(f_out*), i.e. solving §1.1 without the constraint f(0) = 0. **This is not arithmetic on published data: it is
  not computed.** The only thing available is the formula σ(g*) = 1.5257 − ν(f_out*).
- **Order of magnitude (ARGUED, not NUMERICAL).** If σ(g*)² ~ ℓ* (PI_MU's prediction), the self-contribution is
  c_Jσ²/λ = 2.99·10⁻³·σ² ~ 2·10⁻⁷². That is ≈ 0.4% of W*. But Prop. 1.2(c) shows that σ² can be ≫ ℓ, so the
  hypothesis is not justified.
- **The Tate mode dominates.** By §1.3, if f♯*(0) = O(1) (which is what "a₄ fixed by f(0) = 0" indicates), the
  rank-one correction of (2.3) equals a₀²λ⁻¹(2 + γ − log 4π) = 0.0119·a₀² ~ 10⁻². That is, the prime-side formula
  at the minimal-leak representative is a ≈ 68-digit cancellation between O(1) terms. (2.3) makes it exact, but
  it is not at scale.
- **Resonance (observation, ARGUED).** The mode's constant is Σ_ρ1/(ρ(1−ρ)) = 2·0.0230957, the same as in the
  coincidence W* ≈ J²Σ_{γ>0}|ρ|^{−2} of MORI15 (l.198). Both are edge Tate modes, Φ(s) ∝ e^{∓sT}/s, and their zero
  self-form is ∝ Σ1/(ρ(1−ρ)). This explains the **shape** of MORI15's coincidence (edge channel = Tate mode), not
  its value.
- **Prescribed test (not executed).** Solve §1.1 in the Mori basis and obtain f♯*(0), σ(g*) and the true ℓ.
  Prediction: ℓ_true < ℓ*_Mori, possibly by several orders of magnitude, because ψ₀ has 1 − χ₀ ≪ 1 − χ₄. If
  confirmed, MORI15's κ_emp is **underestimated**.

---

## 6. Final

### Labels
See the table in §4. Also: test μ = 15: no new NUMERICAL result (σ(g*) is not arithmetic on published data);
§5 = ARGUED + prescribed test. **L′♯ OPEN. Row D OPEN.**

### New restriction R-Π4 (HARD)
*The minimal-leak representative is not in the domain of the prime-side formula.* The L² closure of the gauge
drops φ(0) = 0 and creates a Tate mode e^{−y/2} (pole of ζ(s)𝓜φ(s) at s = 0, residue −½φ(0)), and also a jump at
1/λ. The mode breaks thm:ext-half (A diverges). The jump can be computed (universal c_J) but is not bounded by W
nor by ℓ. Therefore, any construction B∘Π_μ that evaluates thm:ext-half's formula on f♯ must:
- add the correction (2.3);
- it cannot take either σ(g)² or f♯(0)² as a leak-scale term.
The zero side is blind to the representative. The jump comb only sees Λ in the regularity of Z_log (Kummer) and
in the value of c_J via ζ constants; not in weights nor positions.

### Entry for the index
- **PI4_JUMPS_001 (phase 200, round 5b; new reason vs HH_001/TEST_KINKS: jump of the L² projection at u = 1/λ,
  not of Möbius at λ/m, and nonzero in the core):** σ(g) = λ^{½}Σμ(m)m^{−½}g(log m−T) − ν(f_out) PROVED ≠ 0 and not
  bounded by ‖g‖, ℓ, W (plateau family). Exact tail Ψ̌_{f♯} = e^{−y/2}[−½f♯(0) + σB̄_1(e^{y−T}) + O(e^{−y})] PROVED
  (jump comb −σλ^{−½}n^{−½} + Tate mode from FF.2). Π.4 literal NO-GO if f♯(0) ≠ 0 (A diverges); zero side blind
  to the representative PROVED; corrected identity (2.3) with 2+γ−log 4π CONDITIONAL (EF♭). Comb:
  c_J = (5/4)(2+γ−log4π)+Σρ^{−2} = +0.01158, kernel k = ½[K(m−n)−K(m+n)] (additive, weight (mn)^{−1}): the form
  σ²Σ(mn)^{−½}k(log m/n) is false; rank one; NO-GO as a sign object (P2). a_P: jumps of Z_log at p^{−k}ℤ.
  Do not retry: prime-side formula at f♯, σ² or f♯(0)² as scale terms. Row D OPEN.

### Next lemma
**Lemma Π.5 (true leak at μ = 15 and scale of the Tate mode; OPEN).** Prove or disprove that |f♯(0)|² ≤ Cℓ(g) in
the core (equivalently: that the functional r ↦ f♯(0) is bounded on 𝒦_T). If false, the Tate mode is a second
falsifier of P2 in the quotient, and R-Π4 becomes a theorem. If true, (2.3) gives an at-scale form of Π_μ, except
for the jump. In parallel, run the prescribed test in §5 (σ(g*), f♯*(0), true ℓ) and the (EF♭) check by
truncation.

---

## Summary (≤250 words)

Lemma Π.4 is constructed.

**The jump (PROVED).** f♯ jumps at ±1/λ. The jump has closed formula
σ(g) = λ^{½}Σμ(m)m^{−½}g(log m−T) − ν(f_out), with ν L²-bounded. σ ≠ 0 in the core and is not bounded by ‖g‖, ℓ nor
W (family of plateaus at log 2 − T). It is f♯ that jumps; f̂♯ has tail −σsin(2πξ/λ)/(πξ). This is a different
object from the Möbius kinks of HH_001/TEST_KINKS: it is at 1/λ, comes from the projection, and does not vanish
in the core.

**Exact tail (PROVED).** Ψ̌_{f♯} = e^{−y/2}[−½f♯(0) + σB̄_1(e^{y−T}) + O(e^{−y})]. There is a jump comb
−σλ^{−½}n^{−½} at T + log n and also a **Tate mode** (the polar term of FF.2).

**Π.4.**
- The literal form is **NO-GO** if f♯(0) ≠ 0: the moment A diverges and Φ_{φ*} is not in the radical.
- The zero side is blind to the representative (PROVED).
- In Zr_{f♯} all terms converge (PROVED). The corrected identity (2.3), with constant 2 + γ − log 4π, is
  CONDITIONAL on an explicit formula for e^{−y/2}·sawtooth tails.

**The jump comb.**
- Universal coefficient c_J = (5/4)(2+γ−log 4π) + Σρ^{−2} = +0.01158.
- Kernel k = ½[K(m−n) − K(m+n)], additive, with weight (mn)^{−1}: the conjectured form
  σ²Σ(mn)^{−½}k(log m/n) is false.
- Rank one. NO-GO as a sign object, because it violates P2.
- Λ enters only in the regularity of Z_log (Kummer; a_P creates jumps at p^{−k}ℤ) and in the value of c_J.

**μ = 15.** σ(g*) cannot be computed with the published data. Hint: f♯*(0) = O(1), in which case ℓ*_Mori is only
an upper bound.

**Restriction R-Π4.** Next: Lemma Π.5. L′♯ OPEN, row D OPEN.
