# R162_1102: the character-family route to Gate 1. **NO-GO (PROVED), with one exact identity and one surviving standard**

Round 11. Pure mathematics, no numerics.
Inputs: README (F1–F4, rounds 1–10), R162_590, R162_1001 (Thm 3.1, Prop 3.2, Thm 5.1), R162_1002 (lesson:
a separating functional must be uniform over a family in which ζ is not isolated).
Conventions follow R162_1001: X = e^{2T}; F real, even or odd, supp F ⊂ [−T,T]; c_F is the autocorrelation;
P^a(F) = Σ_{2≤n≤X} a(n) n^{−1/2} c_F(log n) is the prime term; W^ζ_T = A^∞_0 + Pol − P^Λ.

**Verdict.** The requested statement cannot exist in the form asked for. Summed or averaged over the characters
mod q, the window forms are **exactly independent of the arithmetic coefficients** on the window (Theorem O).
ζ's negativity at a first contact is cancelled term for term by the nontrivial characters. What survives is an
average of the negativity over the other characters, and turning that into a contradiction needs a sign for W^χ at
the same F, which is per-window GRH(χ). The one field-uniform object in the family is ζ_{ℚ(μ_q)}. That is the T1
standard (GRH for all K), OPEN, and it is already on record. No label moves; Gate 1 stays OPEN.

## 0. Corpus check (rule )

- **G2_B8_R2 (phase 159)** already treats this family. Lemma K1: for primes q > X, the window Satake data θ_χ
  equidistribute in the torus 𝕋_T; this is proved by the same orthogonality used here. Proposition K:
  W^χ_T = log q‖F‖² + 𝔞^{v(θ_χ)}_T. §3.2: barycentres are EXCLUDED, because v(0) is an extreme point of the torus
  hull. This memo does not redo those results. What is new here: the **signed sum identity** (Theorem O), which
  shows that the averaging cancels ζ exactly rather than just failing to reach it; the class-function version
  (Theorem O′); the large-sieve/Parseval audit (§3); the character decomposition of Φ_Λ (§4); and the DH audit (§5).
- **P46 T1 / R157_004 #37 / R158_001 C15:** a field-uniform proof is admissible, and it proves GRH for every K
  (here K = ℚ(μ_q)). R155_053: the sieve upper-bound class C_BT = {0 ≤ a ≤ Λ} is closed and gives no sign.
- A grep of phases 150–162 for "orthogonality", "large sieve", "Gauss sum", "cyclotomic" found no signed-sum
  identity of the type in Theorem O.

## 1. Falsifier lines, stated first

| model | where it fails | status |
|---|---|---|
| DH (mod 5) | not in the linear span of {Λχ}; its a_DH is not supported on prime powers (§5) | the family *passes* DH, but vacuously |
| deletion, κ-models, finmod | orthogonality holds for **any** a twisted by χ; Theorem O is a-blind | the family **fails** F3 |
| Beurling | no characters mod q; the twisted family aχ is undefined, although Theorem O's algebra holds on any finite abelian dual | vacuous pass at the object level |
| Λχ₂ | it is a member of the family (χ mod 4); a family-uniform argument must prove GRH(χ₂), which is consistent | no falsifier here |
| F1 | Theorem O makes no use of λ = 0 or of the minimality of T_* | fails |
| F2 | every family identity is linear in c_F, which is even under F ↦ −F and A_M ↦ −A_M | fails |

## 2. The exact family identities (PROVED)

Let q be prime with q > X. Each nontrivial χ mod q is then primitive, and χ(n) ≠ 0 for n ≤ X. Let 𝔞_χ ∈ {0,1}
be the parity of χ. By the Weil explicit formula for Λ(s,χ) (CITED: Weil 1952; Iwaniec–Kowalski Thm 5.12;
normalisation of G2_B8_R2 (K)):

  W^χ_T(F) = log(q/π)‖F‖² + A^∞_{𝔞_χ}(F) − P^{Λ,χ}(F),  P^{Λ,χ}(F) = Σ_{n≤X} Λ(n) n^{−1/2} Re χ(n) c_F(log n),

with no polar term. For χ₀ we use ζ itself. On the window, L(s,χ₀) and ζ differ only by atoms n = q^k > X and by
the zeros of 1 − q^{−s} on Re s = 0; we do not use L(s,χ₀).

**Theorem O (orthogonality blindness).** For every q prime with q > X and every F supported in [−T,T]:

  W^ζ_T(F) + Σ_{χ≠χ₀} W^χ_T(F) = A^∞_0(F) + Pol(F) + (q−2) log(q/π)‖F‖² + N_0 A^∞_0(F) + N_1 A^∞_1(F),

where N_0 = (q−3)/2 and N_1 = (q−1)/2 count the nontrivial even and odd characters. The right side contains no
arithmetic coefficient. More precisely: if Λ is replaced by any a with a(1) = 0 on [2, X] (in both W^ζ and all the
twisted forms), the identity holds with the same right side.

*Proof.* Σ_{χ mod q} χ(n) = (q−1)·1_{n≡1 (q)}. For 2 ≤ n ≤ X < q+1 this vanishes, so Σ_{χ≠χ₀} Re χ(n) = −1 and
Σ_{χ≠χ₀} P^{a,χ} = −P^a. This cancels the −P^a in W^ζ_T. The step uses only a(n) for n ≤ X, times the n-independent
count. ∎

**Corollary O.1.** Suppose F is a first-contact vector at T_* and F_δ ∈ L²(I_{T_*+δ}) has W^ζ(F_δ) < 0. Then
Σ_{χ≠χ₀} W^χ(F_δ) = R(F_δ) − W^ζ(F_δ) > R(F_δ), where R is the Λ-free right side. The inequality has the
**harmless direction**: ζ's negativity makes the other characters' forms larger on average, which contradicts
nothing. A contradiction would require an upper bound Σ_{χ≠χ₀} W^χ(F_δ) ≤ R(F_δ). By Theorem O that bound is
equivalent to W^ζ(F_δ) ≥ 0. ∎

**Theorem O′ (general q, class-function form).** Take any q and any complex c = (c_χ)_{χ mod q}. Use primitive
L-functions, with conductor q_χ | q and parity 𝔞_χ. Then

  Σ_χ c_χ W^{χ*}_T(F) = Σ_χ c_χ[log(q_χ/π)‖F‖² + A^∞_{𝔞_χ}(F)] + c_{χ₀}Pol(F) − Σ_{n≤X, (n,q)=1} a(n) n^{−1/2} g_c(n) c_F(log n) + E_q(F),

where g_c(n) = Σ_χ c_χ χ(n) is an arbitrary class function mod q (all class functions arise, by Fourier duality
on (ℤ/q)^×). E_q is the finite list of atoms at n with (n,q) > 1 that come from the imprimitive-to-primitive
correction. It is linear in a restricted to primes dividing q. Hence the family's content on the window is exactly
the **class-sums** P_b(F) = Σ_{n≡b (q)} a(n) n^{−1/2} c_F(log n) together with scalar conductor masses. ζ's
prime term is Σ_b P_b + E_q.

*Proof.* Linearity of the explicit formula in the Dirichlet coefficients, followed by orthogonality. ∎

**Reading.** Orthogonality re-indexes ζ's own window data by residue classes. It adds no identity satisfied by Λ
that a arbitrary does not satisfy. So it is a symbol identity in the sense of R162_403, and it inherits the F1
failure of that entry. The only ζ-specific input would be a **sign** on some family members at the given F. For a
member with c_χ ≥ 0 this is window-GRH(χ); for class indicators the c_χ are complex and not convex. This is the
G2_B8_R2 §3.2 obstruction again, now as an identity instead of an extreme-point remark.

## 3. Large sieve and Parseval: the unconditional positive family objects (PROVED)

The unconditional positivities available over the family are:
(a) Parseval: Σ_χ |Σ_n w_n χ(n)|² = φ(q) Σ_b |Σ_{n≡b} w_n|²;
(b) large sieve: Σ_{q≤Q} (q/φ(q)) Σ*_χ |Σ_{n≤N} w_nχ(n)|² ≤ (N + Q²) Σ|w_n|² (CITED: Montgomery–Vaughan);
(c) Weil positivity for the ζ_K zero side, which is conditional (GRH(K)).

**Prop 3.1.** (a) and (b) are quadratic in a coefficient vector w, and the Weil form is linear in the coefficient
vector a (quadratic only in F). Link them by w_n = a(n) n^{−1/2} φ(log n), with φ any window function built from F.
Then the left side of (a) is a quadratic form in a that is **positive for every a**, including deletion, κ and
finmod coefficients, and Λ-free Beurling analogues on a finite abelian dual. So (a) and (b) are sign statements with
no arithmetic content, and they are λ-blind. Using them against W^ζ needs an inequality of the form
P^Λ(F) ≤ C·(Σ_χ|Σ w χ|²)^{1/2}. That is an **upper bound** on the prime term, which lies in the closed sieve class
C_BT of R155_053: it cannot orient a first contact. Asymptotic use (Q → ∞, zero-density) is a T → ∞ statement
and is dead by Theorem M / R162_801 L5.
*Proof.* (a) is Parseval on (ℤ/q)^×. (b) is cited. Positivity for all a is immediate. The C_BT placement is
R155_053 Prop 1.1. ∎

## 4. The torsion distribution over characters (PROVED)

For (r,d) = 1, e(r/d) = φ(d)^{−1} Σ_{χ mod d} χ̄(r) τ(χ), plus the imprimitive corrections (Gauss sums). Hence
ν_d = Σ_{e|d} ν_e^{prim}, and the primitive d-torsion measure decomposes as

  ν_d^{prim} = φ(d)^{−1} Σ_{χ mod d} τ(χ)·σ_χ,  σ̂_χ(k) = χ̄-twisted Ramanujan coefficient,

so Φ_Λ = Σ_{p^k} log p·Σ_{χ mod p^k} (τ(χ)/φ(p^k)) σ_χ + (Leb-correction). This decomposition is exact.
**Prop 4.1.** Pair it with any window test h_F, which is a trigonometric polynomial of degree ≤ X. The pairing reads
only Φ̂_Λ(k) = log|k| for |k| ≤ X, whatever the character decomposition (R162_1001 Thm 5.1). Summing over χ mod p^k
with the Gauss-sum weights reconstructs c_{p^k}(k), and ⟨Φ_Λ,h_F⟩ = P^Λ(F) (Prop 3.2). So the character
decomposition of the cocycle ℒ_pΦ−Φ = log p(δ₀−Leb) is a Fourier rewrite of the same finitely many numbers. It is
linear in c_F (F1, F2 fail). The characters in this decomposition are mod p^k for **each** support point: they
form a family indexed by Λ's support, not a family in which ζ sits as one member. The ×p cocycle does not
propagate to the twisted forms W^χ: for Λχ, the analogue of (3.1) has χ(p)log p on the right, and it holds at no p
with χ(p) ≠ 1 (Thm 3.1(b)). ∎

## 5. DH, carefully (PROVED)

The DH function is D = ½(1−iκ)L(s,χ) + ½(1+iκ)L(s,χ̄), with χ mod 5, χ(2) = i and κ = (√(10−2√5)−2)/(√5−1). Its
window form uses a_DH = −(D′/D) coefficients.
(i) a_DH is **not** in the span of {Λχ' : χ' mod q, any q}. Every element of that span is supported on prime
powers, while a_DH(n) ≠ 0 for some composite n that is not a prime power: in −D′/D = Σ a_DH(n)n^{−s}, the n = 6
coefficient comes from the product of the n = 2 and n = 3 terms of D, and it does not vanish because D's
coefficients are not completely multiplicative.
(ii) So Theorems O and O′ do not apply to DH, and a family-uniform argument over {L(s,χ)} says nothing about D. The
DH line is passed. The pass is **vacuous**: it is the same pass that "Euler product" gives, since D has none. It
is not a mechanism that meets DH at a declared step.
(iii) Warning, PROVED: the forms are linear in a, so the **form** W[a_χ + a_χ̄] = W^χ + W^χ̄ does belong to the
family. It is the form of L(χ)L(χ̄), not of D, and GRH-consistent. A family argument that works with forms
"linear in L" instead of "linear in log L" would absorb DH and prove a falsehood. Every family step must be
written at the log-derivative level.

## 6. What survives: the cyclotomic form (T1 standard, OPEN)

Σ_{χ mod q} W^{χ*}_T = W^{ζ_K}_T with K = ℚ(μ_q). This is the only positive-coefficient family combination with a
natural Weil criterion: W^{ζ_K} ≥ 0 for all T ⟺ GRH(K). It is field-uniform (T1: admissible, and it proves GRH
for all K). A first contact for ζ at T_* does **not** force a first contact for ζ_K at T_*: by Corollary O.1 the
other characters raise the sum. And T_*(K) ≥ T_*(ζ) is not provable without per-window GRH(χ) (OPEN). So the
family converts Gate 1 for ζ into Gate 1 for ζ_K, a strictly larger target. This is not a separating
functional (R162_1002): ζ sits inside ζ_K as a factor, but the window form does not isolate it, by Theorem O.

## 7. F1, F2, Theorem M

- **F1:** Theorems O, O′ and Props 3.1, 4.1 hold for every F and every λ. λ = 0 is used nowhere. Fails.
- **F2:** every identity is linear in c_F. Fails.
- **Theorem M:** q → ∞, Q → ∞ and equidistribution (Lemma K1) are T-uniform statements only at fixed T. Any use
  with q = q(T) → ∞ that reads a defect is a T → ∞ limit and is subject to the doubly exponential dilution. Nothing
  here needs it.

## 8. Verdict and residual

**NO-GO (PROVED).** Orthogonality makes the family sum Λ-free on every window (Theorem O). A general combination
reads only class sums of the same coefficients (Theorem O′). The unconditional family positivities are
coefficient-blind Parseval or large-sieve upper bounds in C_BT (Prop 3.1). The Gauss-sum decomposition of Φ_Λ
collapses to the prime term (Prop 4.1). DH is passed only vacuously, and only if the family is written at the
log-derivative level (§5(iii)). The surviving object, ζ_{ℚ(μ_q)}, is the T1 standard.

**Lesson for the dead-end map (add to R162_590 §1c).** "Character family / orthogonality: R162_1102; the sum over
χ mod q is Λ-free on the window (Theorem O), so ζ's negativity is absorbed with the harmless sign; the only positive
combination is ζ_{ℚ(μ_q)} (T1); F1, F2, F3 (a-blind)." A family in which ζ is not isolated must also **not be
related to ζ by an exact linear identity on the window**. Otherwise the family sum reproduces ζ's data (Theorem
O′), and uniformity over it is a restatement.
