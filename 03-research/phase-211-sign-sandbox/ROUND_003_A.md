# Round 003 A — The near-null pair of a_T on P_T: parity, pinning, rigidity

Notation of STATEMENT_001 and ROUND_002_E: Arch(F) = (1/2π)∫ m|F̂|², Π(F) = Σ_{log n<2T} v_n Re c_F(log n), a_T = Arch − Π,
Φ_T(c) = inf_{S_T}[Arch − cΠ] (S_T the unit sphere of P_T), Θ_T = max_c Φ_T(c) = inf{Arch(F) : F ∈ S_T, Π(F) = 0},
c*_T a maximiser. J F(t) = F(−t). Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 1. Corpus check

- Growing near-kernel of the window form (many eigenvalues in [0, δ], multiplicity growing with the window): recorded as a
  NO-GO quantifier (ROUTES-TRIED-INDEX 05b, L106; AUDIT_ZENODO_FRONTIER B3; the prolate mechanism L06/L39). It is used here
  only as a reading of the numerics, not as a route. Nothing below tries to bound the cluster from below.
- Parity sectors, nodal structure, zero extension: CITED from Paper 46 (prop:nodes, lem:parity, lem:zeroext).
- New here, not in the index or the grid (grep: "pin", "Π-Gram", "indefinite on the near-kernel", "rigidity"): (i) the
  parity assignment of the pair; (ii) the Weyl pin lemma (§3, Lemma 3), which turns "Π indefinite on a near-null pair" into
  a quantitative tangency |c*_T − 1| ≤ gap/|μ|; (iii) the rigidity lemma (Lemma 4), which explains every falsifier failure
  of λ_A and of Θ by one inequality on the near-kernel. These are structural statements, not a sign step; no route of the
  index is retried.

## 2. Validation numerics (NUMERICAL)

Method as in ROUND_002_E §3 (Dirichlet sines, N = 40 and 80, Arch by quadrature on |τ| ≤ 6000, Π exact in t-space), with
one change: P_T is imposed sector by sector. φ_k(−t) = (−1)^{k+1}φ_k(t), so odd k span the even functions and even k the odd
ones; on even F the constraint is ∫F cosh(t/2) = 0, on odd F it is ∫F sinh(t/2) = 0 (Paper 46, parity paragraph). The cross
blocks of Arch and Π between parities vanish to 10⁻¹⁴, as Proposition 1 requires.
Comb correction: the comb generator used in ROUND_002_E lists n ≤ 5 only; for T > ½ log 7 ≈ 0.973 it omits n = 7. All
values below use the exact Λ(n) for every log n < 2T. Values at T ≤ 0.9 of ROUND_002_E are unaffected.

Galerkin values are upper bounds for the true eigenvalues of a_T on P_T (min–max on a subspace of P_T). Values below
about 10⁻¹⁴ are at rounding level and individually meaningless; the subspaces they span are stable from N = 40 to N = 80
(the Π-Gram eigenvalues below agree to 10⁻³).

2.1 The two lowest eigenvalues in each sector, and Π on them (N = 80; N = 40 agrees to two digits in the Π values).

| T | λ_ev,1 | λ_ev,2 | λ_odd,1 | λ_odd,2 |
|---|---|---|---|---|
| log 2 | 1.1·10⁻⁷ | 2.3·10⁻³ | 1.3·10⁻⁵ | 6.9·10⁻² |
| ½log5 − 10⁻³ | 3.8·10⁻¹² | 3.9·10⁻⁷ | 7.9·10⁻¹⁰ | 4.1·10⁻⁵ |
| ½log5 + 10⁻³ | 3.1·10⁻¹² | 3.2·10⁻⁷ | 6.5·10⁻¹⁰ | 3.5·10⁻⁵ |
| 0.9 | ≲10⁻¹⁴ | 1.3·10⁻¹¹ | ≲10⁻¹³ | 2.2·10⁻⁹ |
| 1.0 | ≲10⁻¹⁵ | ≲10⁻¹⁴ | ≲10⁻¹⁵ | ≲10⁻¹⁴ |

Π-Gram matrices M_par on the span of the two lowest eigenvectors of each sector (Arch = a_T + Π, so the Arch matrix is
M_par + diag(λ_1, λ_2); the even–odd off-diagonal blocks are exactly 0):

| T | eig M_ev | eig M_odd |
|---|---|---|
| log 2 | −0.095, +0.546 | +0.180, +0.817 |
| ½log5 ± 10⁻³ | −0.155, +0.473 | +0.108, +0.674 |
| 0.9 | −0.183, +0.445 | +0.073, +0.613 |
| 1.0 | −0.204, +0.424 | +0.047, +0.576 |

Π on the individual bottoms: Π(e_ev,1) = 0.088, 0.062, 0.046 at log 2, ½log5, 0.9 (positive); Π(e_odd,1) = 0.274, 0.242,
0.226 (positive). At T = 1 the bottom vectors are not individually resolved; only the span is.

2.2 Answer to "parity degeneracy or same parity". The pair reported in ROUND_002_E (λ₁ = 3.1·10⁻¹², λ₂ = 6.5·10⁻¹⁰ at
½log5 + 10⁻³) is {e_ev,1, e_odd,1}: one even, one odd, ratio ≈ 200, NOT degenerate in any useful sense, and Π is positive
definite on it (diag(0.062, 0.242)). It cannot produce c* = 1. The structure that pins c* is the EVEN pair
{e_ev,1, e_ev,2}: same parity, gap λ_ev,2 − λ_ev,1 ≈ 3·10⁻⁷ at ½log5, ≈ 10⁻¹¹ at 0.9, and Π indefinite on its span
(det M_ev < 0). The odd pair has Π positive definite at every tested T. Correction to the reading of ROUND_002_E §3.

2.3 Track in T (N = 40, T = 0.600 to 1.000, step 0.025). λ_ev,1 < λ_odd,1 at every resolved T (ratio 10–250), so the
bottom of a_T on P_T is even and (numerically) simple. All four of λ_ev,1, λ_ev,2, λ_odd,1, λ_odd,2 decrease
monotonically and super-exponentially (λ_ev,2: 2.2·10⁻¹ at 0.6, 1.7·10⁻³ at 0.7, 6.4·10⁻⁷ at 0.8, 1.9·10⁻¹¹ at 0.9); no
crossing between sectors is seen. The smaller eigenvalue of M_ev changes sign between T = 0.600 (+0.011) and T = 0.625
(−0.018) and then decreases steadily to −0.205 at T = 1. The smaller eigenvalue of M_odd decreases linearly from 0.24 to
0.046 (≈ −0.0066 per 0.025); linear extrapolation puts an odd pin near T ≈ 1.17 (ARGUED, extrapolation only).

2.4 Localisation of |F̂|². Bottom vectors of both sectors live at the lowest Dirichlet frequencies: the peak of |F̂_ev,1|²
is at τ ≈ 1.6–1.9·π/T and of |F̂_odd,1|² at τ ≈ 1.9–2.3·π/T (90 % of the mass below τ ≈ 2.2–3.1·π/T), i.e. on sine modes
k ≈ 3–5, far from the Nyquist frequency πN/(2T) of the section. The mass fraction of |F̂|² (on 0 ≤ τ ≤ 80) lying on the
negative set {s_T < 0} is 0.50–0.52 for every bottom vector at every T ≤ 0.9: the bottom vectors straddle a sign change of
s_T (at ½log5 + 10⁻³ the sign changes of s_T are at τ ≈ 1.59, 3.45, 5.25, 7.03, 8.80, … and the even peak sits at
τ ≈ 6.9, next to 7.03). At T = 1 the fraction is 0.50 as well. No localisation on the negative set.

2.5 Falsifiers per sector (N = 40; Θ_par = max_c λ_min of Arch − cΠ_w on P_T^par).

| T | comb | Θ_ev | Θ_odd |
|---|---|---|---|
| ½log5+10⁻³ | no 2 / no 3 | −0.260 / −0.092 | +0.087 / +0.060 |
| | η = +0.1 / −0.1 | +0.007 / −0.059 | +0.021 / +0.008 |
| | swap / 3→3.2 | −0.002 / −0.084 | +0.039 / +0.049 |
| 0.9 | no 2 / no 3 | −0.411 / −0.337 | +0.016 / +0.058 |
| | η = +0.1 / −0.1 | −0.024 / −0.062 | +0.012 / −0.060 |
| | swap / 3→3.2 | −0.121 / −0.094 | +0.033 / −0.018 |
| 1.0 | no 2 / no 3 | −0.508 / −0.478 | −0.129 / −0.071 |
| | η = +0.1 / −0.1 | −0.038 / −0.068 | −0.001 / −0.114 |
| | swap / 3→3.2 | −0.168 / −0.161 | −0.011 / −0.042 |

The even sector loses first, at every window and for every falsifier except η = +0.1 at ½log5; the odd sector survives
most falsifiers up to 0.9 and loses them at T = 1. This matches the pin: the sector with Π indefinite on its near-kernel
is the sector the falsifiers break.

2.6 The near-kernel alone explains the failures. Let S_T be the span of all Galerkin eigenvectors of a_T with eigenvalue
< 10⁻³ (k = 2, 4, 6, 9 at T = log 2, ½log5, 0.9, 1.0). Π restricted to S_T has inertia (0,2), (1,3), (2,4), (2,7). The
upper bound Θ(w') ≤ max_c λ_min((Arch − cΠ_{w'})|S_T) (Lemma 4(ii)) is already negative at T = 1 for every falsifier
(−0.49 no 2, −0.44 no 3, −0.04/−0.07 η = ±0.1, −0.17 swap, −0.22 3→3.2), at T = 0.9 for no 2, no 3, η = −0.1, swap,
3→3.2, and at ½log5 for η = −0.1 and 3→3.2. Where it is positive the remaining negativity comes from eigenvectors above
10⁻³.

## 3. Pure mathematics

Proposition 1 (PROVED; extends Paper 46 lem:parity from Arch to a_T). P_T = P_T^ev ⊕ P_T^odd, orthogonally for the L²
norm, Arch and Π. Hence λ_A(T) = min(λ^a_ev(T), λ^a_odd(T)), with λ^a_par the bottom of a_T on the unit sphere of P_T^par,
and for every c, Φ_T(c) = min(Φ_ev(c), Φ_odd(c)).
Proof. P_T is J-invariant and splits (lem:parity). Π(F) = (1/2π)∫ σ(τ)|F̂|² dτ with σ(τ) = Σ v_n cos(τ log n) even (since
ĉ_F = |F̂|² and c_F is the inverse transform). For F = F_e + F_o, F̂_e is even and F̂_o odd, so the cross term
(1/2π)∫ σ · 2Re(F̂_e conj F̂_o) has odd integrand and vanishes; the same for m. ∎

Proposition 2 (PROVED, granted the CITED Kato–Danskin formula). a_T on P_T has compact resolvent (Arch has, Paper 46
prop:nodes(i); Π is bounded, |Π(F)| ≤ Σ v_n ‖F‖²). Let E_T = E_ev ⊕ E_odd be the bottom eigenspace. Then
  (i) the one-sided derivatives of the concave function Φ_T at c = 1 are Φ'_±(1) = −max/−min of Π on the unit sphere of
      E_T (CITED: Kato, analytic perturbation of an isolated eigenvalue of finite multiplicity; Danskin);
  (ii) since Π(αf_e + βf_o) = |α|²Π(f_e) + |β|²Π(f_o) for unit f_e ∈ E_ev, f_o ∈ E_odd, the range of Π on the unit
       sphere of E_T is the convex hull of the ranges on the two sectors' bottom spheres;
  (iii) c*_T = 1 is a maximiser iff 0 lies in that hull. If each nonempty sector bottom is simple, with vectors e, o:
       c*_T = 1 iff [λ_ev < λ_odd and Π(e) = 0] or [λ_odd < λ_ev and Π(o) = 0] or [λ_ev = λ_odd and Π(e)Π(o) ≤ 0].
Proof. (ii) is Proposition 1. (iii): c = 1 maximises the concave Φ_T iff Φ'_+(1) ≤ 0 ≤ Φ'_−(1). ∎
Reading. Exact tangency is a codimension-one coincidence. The computed bottom is even, simple, with Π(e_ev,1) > 0, so the
exact maximiser satisfies c*_T < 1 strictly; what is observed is approximate tangency, explained by Lemma 3.

Lemma 3 (Weyl pin; PROVED). Let F_1, F_2 ∈ P_T be orthonormal, let A_2 and M_2 be the 2 × 2 matrices of a_T and Π on their
span, λ_1 = λ_A(T) and Λ_2 := λ_max(A_2), and suppose M_2 is indefinite with eigenvalues μ_− < 0 < μ_+. Then
  (i) λ_A(T) ≤ Θ_T ≤ Λ_2, indeed Θ_T ≤ min{a_T(F) : F ∈ span, ‖F‖ = 1, Π(F) = 0} ≤ Λ_2;
  (ii) every maximiser satisfies −(Λ_2 − λ_1)/μ_+ ≤ 1 − c*_T ≤ (Λ_2 − λ_1)/|μ_−|.
Proof. (i) Θ_T ≥ Φ_T(1) = λ_A(T). M_2 indefinite gives a unit F in the span with Π(F) = 0, and Arch(F) = a_T(F) + Π(F) =
a_T(F) ≤ Λ_2. (ii) Put s = 1 − c. Arch − cΠ = a_T + sΠ, so by min–max on the span and Weyl's inequality
Φ_T(c) ≤ λ_min(A_2 + sM_2) ≤ λ_max(A_2) + λ_min(sM_2), which equals Λ_2 + sμ_− for s ≥ 0 and Λ_2 + sμ_+ for s ≤ 0. Since
Φ_T(c*) = Θ_T ≥ λ_1, the stated bounds follow. ∎
Instances (NUMERICAL inputs, Galerkin span inside P_T): with the even pair, |1 − c*| ≤ 2.4·10⁻², 2.0·10⁻⁶, 7·10⁻¹¹, 2·10⁻¹⁴
at T = log 2, ½log5 + 10⁻³, 0.9, 1.0 (observed: 1.7·10⁻³, 1.3·10⁻⁷, rounding, rounding); and Θ_T − λ_A(T) ≤ λ_ev,2.
So "c* = 1 to eight digits" is not a coincidence of Λ: it is forced by two facts, both about a_T itself, (P1) a second
eigenvalue of a_T in the even sector that is tiny, (P2) Π indefinite on the span of the two lowest even eigenvectors.

Lemma 4 (rigidity of a near-null form; PROVED). Let S ⊂ P_T be a k-dimensional subspace with a_T|_S ≤ ε (as a form), and
let δ be any finite weight vector on the window positions, Π_δ its form, a_T^{w+δ} = a_T − Π_δ. Then
  (i) λ_A(T; w + δ) ≤ ε − λ_max(Π_δ|_S);
  (ii) Θ_T(w + δ) ≤ max_c λ_min((Arch − cΠ − cΠ_δ)|_S) ≤ ε + max_c λ_min(((1 − c)Π − cΠ_δ)|_S).
In particular, for the scaling δ = (c − 1)Λ: λ_A(T; cΛ) ≤ ε − |c − 1|·|μ_∓(Π|_S)|, with μ_− for c > 1 and μ_+ for
c < 1. If Π|_S is indefinite, every c ≠ 1 with |c − 1| > ε/min(|μ_−|, μ_+) gives λ_A(T; cΛ) < 0.
Proof. Min–max on S: a_T^{w+δ}|_S = a_T|_S − Π_δ|_S ≤ ε − Π_δ|_S, and the bottom on S is ≤ ε − λ_max(Π_δ|_S). (ii) is the
same with Arch − c(Π + Π_δ). For δ = (c − 1)Λ, Π_δ = (c − 1)Π. ∎
Reading. Lemma 4 is the mechanism of the falsifier failures (rule 4 (a) and (d)): a nonnegative form with a k-dimensional
near-kernel S tolerates only perturbations δ with Π_δ|_S ⪯ ε (for λ_A), or with a c making ((1 − c)Π − cΠ_δ)|_S ⪰ −ε
(for Θ). As k grows with T (k = 2, 4, 6, 9 below 10⁻³ at the four windows) and the inertia of Π|_S stays mixed, the
admissible set of δ shrinks; for the even pair alone the admissible set for Θ is a set of positive measure (the plane
spanned by M_ev and Δ meets the 2 × 2 positive cone for an open set of Δ), which is why η = +0.1 survives at ½log5; with
k = 9 at T = 1 every tested δ is excluded (§2.6).

What can be said about simplicity of the bottom (OPEN). Perron–Frobenius (Paper 46 prop:nodes(i)) gives a simple bottom
for Arch on L²(I_T) only; on P_T the bottom changes sign (prop:nodes(ii)), and Π destroys positivity preservation, so no
Perron–Frobenius argument is available for a_T on P_T or on a sector. Whether λ^a_ev(T) ≠ λ^a_odd(T) for all T, and whether
each sector bottom is simple, is OPEN. Nothing in Paper 46 forces or forbids it; the numerics say the bottom is even and
simple with a sector ratio of 10–250.

## 4. Statements

Sharpest PROVED statement. For every T: (a) the bottom of a_T on P_T splits by parity (Proposition 1); (b) tangency
c*_T = 1 holds iff 0 is in the convex hull of Π on the two sector bottom spaces (Proposition 2); (c) for any orthonormal
pair in P_T on which Π is indefinite, λ_A(T) ≤ Θ_T ≤ Λ_2 and |1 − c*_T| ≤ (Λ_2 − λ_A)/min(|μ_−|, μ_+) (Lemma 3); (d) any
near-kernel S of a_T bounds λ_A and Θ of every modified comb by ε minus an explicit eigenvalue of Π_δ|_S (Lemma 4).

Sharpest conjectural statement (OPEN; NUMERICAL support T ∈ [0.6, 1.0]).
(C1) For every T > T_pin (≈ 0.61) the two lowest eigenvectors of a_T on P_T^ev span a plane on which Π is indefinite, with
     μ_−(T) ≤ −c_0 < 0 uniformly for T ≥ 0.7.
(C2) λ^a_ev,2(T) → 0 faster than any exponential as T grows.
(C3) The bottom of a_T on P_T is even and simple: λ^a_ev,1(T) < λ^a_odd,1(T).
Under (C1)–(C2), Lemma 3 gives Θ_T − λ_A(T) → 0 and c*_T → 1; under (★), Θ_T ≥ 0 is then automatic up to λ_ev,2.

Inequality on the exact Λ that makes the pair's two values nonnegative. With S = span{e_ev,1, e_ev,2} and the 2 × 2
matrices Arch_S, R_n(S)_{ij} = Re c_{e_i, e_j}(log n) (symmetrised cross-autocorrelations), the pair values are ≥ 0 iff

    Σ_{log n < 2T} (2Λ(n)/√n) R_n(S) ⪯ Arch_S   (2 × 2 matrix order; equivalently trace and determinant of the difference ≥ 0).

This is (★) restricted to S and is circular as stated, since S depends on Λ. The non-circular content is Lemma 4: at a
window with near-kernel S of size ε, the exact Λ must satisfy this matrix inequality while every finite modification δ
with λ_max(Π_δ|_S) > ε violates it. Numerically det(Arch_S − Π_S) = λ_ev,1·λ_ev,2 ≈ 10⁻¹⁸ at ½log5: the inequality is
saturated to 18 digits.

## 5. Falsifier test (rule 4)

No sign step is proposed. The statements of §4 are structural and hold for every weight vector; they do not separate Λ.
What separates Λ in the numerics is the input (P1)–(P2) (a tiny second even eigenvalue with Π indefinite on the pair),
which is a property of the nonnegative form a_T at the exact comb. (a) cΛ: Lemma 4 forces λ_A(cΛ) < 0 for |c − 1| beyond
ε/|μ|, consistent with STATEMENT §4; Θ is scale-invariant, so (a) is not a test for Θ. (b), (c) deletions and the Beurling
shift and (d) finite modifications: break (P1) (their λ_A is −0.06 to −0.5, so there is no near-null pair), and the even
sector is the one that fails first (§2.5). The mechanism for "Λ sits at tangency" is therefore not a monotonicity in a
sector (none was found: Θ_par is not monotone under deletion, cf. ROUND_002_E Remark) but Lemma 3: tangency is a consequence
of a near-degenerate nonnegative bottom with Π indefinite on it, and any perturbation that does not preserve both loses it.

## Result

PROVED piece (structural; no sign): parity splitting of a_T and of the tangency criterion (Propositions 1–2), the Weyl pin
lemma (Lemma 3) and the rigidity lemma (Lemma 4). The pin pair is identified numerically as two EVEN eigenvectors, not an
even–odd degeneracy.

## What was proved

- Proposition 1: a_T commutes with parity on P_T; λ_A = min of the sector bottoms; Φ_T = min of the sector Φ's.
- Proposition 2: exact tangency ⟺ 0 ∈ conv(Π on the sector bottom spaces); with simple sector bottoms, an explicit
  three-case criterion; exact tangency is a codimension-one coincidence.
- Lemma 3: an orthonormal pair in P_T with Π indefinite pins Θ_T to [λ_A, Λ_2] and c*_T to 1 within (Λ_2 − λ_A)/min|μ_±|.
- Lemma 4: a near-kernel S of a_T bounds λ_A and Θ of every modified comb; explains falsifier (a) for λ_A and the
  observed failures of Θ.
- NUMERICAL: the ROUND_002_E pair is even + odd with Π definite on it; the pinning pair is {e_ev,1, e_ev,2}, Π-indefinite
  from T ≈ 0.61 on; bottoms decrease super-exponentially with no sector crossing; mass of |F̂|² splits 50/50 across
  {s_T < 0}; the even sector loses first under every falsifier. The ROUND_002_E comb generator omits n = 7 for T > ½log7.

## What failed and why

- Parity degeneracy as the mechanism: false; λ_odd,1/λ_ev,1 ≈ 10–250 and Π is positive on both parity bottoms.
- Simplicity of the bottom: not provable with the available tools (no Perron–Frobenius for a_T on P_T); OPEN.
- A sector monotonicity explaining tangency: none found; Lemma 3 replaces it, but its inputs (P1)–(P2) are statements
  about the spectrum of a_T at the exact comb that are as strong as the positivity they would serve.
- No inequality on Λ(n) independent of the eigenvectors was obtained; the pair inequality is circular as stated.

## Next concrete step

Make (P2) independent of the comb: test whether Π is indefinite on the span of the two lowest eigenvectors of the
archimedean form Arch on P_T^ev (a Λ-free plane), and if so compute the 2 × 2 Schur complement of a_T on that fixed plane.
If the fixed Arch-plane captures the pin (Π-Gram eigenvalues within 10⁻² of M_ev), the pair inequality of §4 becomes a
non-circular 2 × 2 matrix inequality in the exact values Λ(n), n < e^{2T}, to be attacked directly at T = 1.
