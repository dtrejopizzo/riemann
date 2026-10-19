# R184_015 — The "Sonin remainder norm" candidate and the source/form dichotomy theorem — **NO-GO (PROVED, structural): every P of the form «‖Δ_T‖ = e^{o(T)}» is either blind to M_m or E1; the lower half is exactly an equivalent of RH**

Pure mathematics, no numerics. RH is not asserted, nor the closure of D.
Inputs: R184_099, R184_004 (Thm 4, Cor 5, editor's note R184_091), R184_006 (detection law), R183_018 (Son ≥ 0, l.93; E_S = Son + R),
R183_025 (identity (3.1)), R183_029 (R'_S = −∫c_h ε_S, Theorem C, (E′_loc) ⟺ HS), R183_028/033, R169_000/091 (A1–A9),
R166_190 ((G)+(N)), R166_802 ((N′)), R167_101–103 ((WS*), sieve blindness), grid R162_2300 §3/§4/§7, R184_011 Cor 3.4, R162_2601 §6 (O2601.1).*

## 0. Corpus check

grep for «‖R'_S‖», «norm of the compact operator», «e^{o(T)}», «subexponential» in phase-183, phase-184, the grid: the
only mention is the editor's note R184_091 on R184_004 («in M_m the compact operator has norm ~e^{2βT}»). No one has
written the candidate or its analysis. §§1–4 are new; the mechanism of §3 (fluctuation of ψ) is classical (Ingham/Landau)
and is cited as such.

## 1. The candidate, written precisely

Conventions from R184_004: I_T = [−T,T], P_T = {Φ_F(0)=Φ_F(1)=0}, W_T(F) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ), S(T) = {∞} ∪ {p < e^{2T}}.
By R183_029 (identity (3.1) PROVED unconditionally; HS CONDITIONAL on (M)):

    E_{S(T)} = Son_{S(T)} + R'_{S(T)},     R'_S(F) = −∫∫ F(t)F(t') ε_S(t−t') dt dt',   ε_S = ε + Σ_{p∈S} δε_p,

and for S = S(T) the semilocal form E_{S(T)} coincides on C_c^∞(I_T)∩P_T with the global form W_T (only the primes
p^k < e^{2T} see the support of F∗F̃; explicit formula CITED). Son_S ≥ 0 by construction (R183_018 l.93: trace of
ϑ(g)Sϑ(g)^*). Let Δ_T := R'_{S(T)}|_{P_T} and ‖·‖ the operator norm on L²(I_T) (dominated by the HS norm under (M)).

**Candidate (P_src).** ‖Δ_T‖ ≤ e^{o(T)}, where Δ_T is computed from the source: ε (Γ) and δε_p (p < e^{2T}).

**Candidate (P_form) ("in the form" variant).** ‖W^X_T − Son_{S(T)}‖_{P_T} ≤ e^{o(T)}, defined for any
system X with Weil form W^X_T (zeta, falsifier or model).

For ζ both coincide (identity (3.1)). For the falsifiers they do not: that is the whole question.

## 2. What does work: P ⟹ RH in one line (PROVED, conditional only on what is cited)

**Proposition 1.** (P_src) for ζ ⟹ RH.
*Proof.* On P_T: W_T = Son_S + Δ_T ≥ Δ_T ≥ −‖Δ_T‖ ≥ −e^{o(T)}. If there were a quartet ½±β±iγ, β>0, the detection law
(R184_006 Thm 1, qualitative in R162_2501 Prop 1; Gabor packets at the ends of I_T, normalized in L²) gives
λ_min(W_T|P_T) ≤ −c e^{2β′T} + C for some β′ ∈ (0,β] (the maximal β of the cluster; if there is no maximum, take
a β′ < sup β with the version Thm 1′). Contradiction for large T. □
(The "no maximum" case with β_j ↑ ½ only makes the bound worse and is equally contradictory.)

That is, implication (c) of the target exists and is short. The problem lies in (a) and in (b)+(S5).

## 3. What does not work: the dichotomy

**Theorem 2 (source/form dichotomy, PROVED).**
(i) *(P_src is blind to M_m.)* For every m and every T, the Δ_T computed from the source of M_m is the same as that of ζ
(R184_004 Thm 4(b): same A_∞, same B_p, same ε; M_m differs only in Δ^{M}_T of rank ≤ 6m, which is **not** in the
source). Hence P_src(M_m) ⟺ P_src(ζ): P_src does not fail for M_m. Prop 1 does not apply to M_m because for M_m the identity
W^M = Son + R'_S is false (W^M = Son + R'_S + Δ^M). So P_src separates ζ from M_m **only** through identity
(3.1), which is exact and signless (W12) — this is exactly the rigidity Thm H of R162_2601 (E1 by configuration, R184_004 §2.4).
(ii) *(P_form separates, but is E1.)* P_form(X) fails for every X with a quartet off the line and quantitative
detection (Prop 1 with W^X instead of W_T). But P_form = Q ∧ U with
    Q :  W^X_T ≥ −e^{o(T)} on P_T, ∀T ≫ 1,     U :  W^X_T ≤ Son_S + e^{o(T)} on P_T.
For X = ζ: RH ⟹ W_T ≥ 0 ⟹ Q; and Q ⟹ RH by the detection law. **Q ⟺ RH.** Hence every proof of P_form contains a
proof of an equivalent of RH: P_form is not "strictly weaker" at any intermediate step (it fails S5/S11).
(iii) *(P_src ⟹ Q goes through the identity.)* Since P_src(ζ) ⟹ P_form(ζ) ⟹ Q, any proof of P_src(ζ) that does not use
identity (3.1) also proves P_src(M_m) and nothing about W^M; and any use of (3.1) to bound Δ_T rewrites
Δ_T = W_T − Son_S in the zero variable. **A proof of P_src "from the source" is a bound on Σ_p δε_p, and §4 shows
that this bound is that of the fluctuation of ψ, of exponent 2Θ−1.**
*Proof.* (i) R184_004 Thm 4(b). (ii) Prop 1 + RH ⟹ W_T ≥ 0 (Weil). (iii) composition. □

**Corollary 3 (strongest form of W11 to date, PROVED).** Let W_T = Pos_S + Δ_T be any decomposition on P_T with
Pos_S ≥ 0 built from the local source (Sonin or any other: only Pos ≥ 0 is used). Every property
P = «‖Δ_T‖ ≤ g(T)» with g = e^{o(T)}:
  — if Δ_T is defined from the source, P is invariant under X ↦ M_m (fails (b) for M_m, Ξ_a with the same source,
    and every model that modifies ζ by a rational/integer factor without touching Λ and Γ);
  — if Δ_T is defined as W^X − Pos_S, the lower half of P is Q ⟺ RH (E1).
There is no third option: the only bridge between the two definitions is the explicit formula, an exact signless identity.
The positive part contributes nothing: only Pos ≥ 0 is used, and Theorem M (no margin) prevents Pos_S from absorbing an
amount e^{2βT}.

## 4. Computing ‖Δ_T‖ from the source: the growth is that of ψ(x) − x (ARGUED, with the hard step isolated)

Kernel in u = t − t' ∈ (−2T,2T). The source side of W_T on P_T is (explicit formula CITED):
    K_W(u) = −Σ_{n<e^{2T}} Λ(n) n^{−1/2}(δ_{log n} + δ_{−log n}) + Γ-density(u) [+ pole e^{u/2}+e^{−u/2}, which vanishes on P_T].
Son_S has kernel K_Son = (the same atoms, extracted exactly: R183_025/029, "exact prime atom") + s_S(u), with s_S
absolutely continuous. Hence ε_S = −(Γ-density − s_S) and

    Δ_T = convolution by (Γ-density − s_S) on P_T.

**Step 4.1 (PROVED).** The atoms have Fourier transform on the real line
Σ_{n<X} Λ(n) n^{−1/2−iξ} = X^{1/2−iξ}/(½−iξ) − Σ_ρ X^{ρ−1/2−iξ}/(ρ−½−iξ) + O(log), X = e^{2T}
(truncated explicit formula, CITED). The first term (size e^{T}/|½−iξ| — the "trivial e^{T}" of the target) is
that of the pole and its form on P_T is null: the pole cancels against the mean of the atoms. **No e^{T} is left**: the
trivial count Σ_{p<e^{2T}} p^{−1/2} log p ~ 2e^{T} of the target measures the mean, not the fluctuation, and the mean is
absorbed by the primitive restriction (Tate).
**Step 4.2 (PROVED).** Since Son_S ≥ 0 and the atoms of K_Son are exact, s_S must make the measure "atoms + s_S" PD
(on I_T, in the Kreĭn sense). What remains of the atoms on P_T after removing the mean is the fluctuation
f_T(ξ) = −Σ_ρ X^{ρ−1/2−iξ}/(ρ−½−iξ), of size X^{Θ−1/2} = e^{(2Θ−1)T} (trivial upper bound; lower bound in mean
square by Landau/Ingham if Θ>½, CITED).
**Step 4.3 (ARGUED; the hard step).** "s_S compensates exactly the non-PD part of the fluctuation, and nothing more", in
the sense ‖Γ − s_S‖ ≍ sup_{|ξ|≲T^{-1}-resolution} |f_T| in the operator norm on P_T. If true, then
    ‖Δ_T‖ ≍ e^{(2Θ−1)T}   (mod polynomial factors in T),
and P_src ⟺ Θ = ½ ⟺ RH. The exponent is exactly that of (N′) (R166_802: Θ − ½ in Σ Λ(n)n^{−1/2−iγ}, here with the
window convention 2T). Step 4.3 is the only thing not proved; it depends on the microlocal form of r_p ((M), R183_029
Theorem C) and on the Sonin compensation being "minimal". **But Theorem 2 does not depend on 4.3**: even if s_S
compensated in some other way, P_src ⟹ Q ⟺ RH by Prop 1.

**Reading.** The target's suspicion is confirmed with the correction from 4.1: the e^{T} growth of the trivial computation is
the pole, which Tate removes; what survives is e^{(2Θ−1)T}, and "e^{o(T)}" is literally "Θ = ½". The sub-bound
Σ_p ‖δε_p‖_∞ ≲ Σ p^{−1/2} log p is a bound *without cancellation* and so it sees neither the pole nor the fluctuation: it is
useless in both directions. A bound with cancellation of Σ_p δε_p(e^x) is, by 4.1–4.2, a bound on the twisted prime sum
Σ_{n<X} Λ(n) n^{−1/2−iξ} *after subtracting the polar term*, uniform in ξ: ψ(x) − x = O(x^{1/2+o(1)}) smoothed,
a classical equivalent of RH. E1.

## 5. Grid §4 falsifiers (for P_src and P_form)

| falsifier | P_src | P_form | reason |
|---|---|---|---|
| DH | undefined/≠ | fails | no Euler product (source ≠ prime atoms); zeros off the line ⟹ Q fails |
| Ξ_a | = ζ (same source if built on Λ, Γ) | fails | modification by factors in the zero variable; Prop 1 |
| M_m | **= ζ (blind)** | fails | R184_004 Thm 4(b); Δ^M of rank ≤6m outside the source |
| Λ̃ (R162_2601) | different source; P_src not defined (no log-derivative, no local Son) | fails | no identity (3.1) |
| f_t | = ζ or undefined | fails | analytic deformation, same source or none |
| P_{a,c} | undefined | fails | no local structure |
| ζ_θ | undefined | fails | idem |
| BFdisc / Beurling DMV / b_θ | **fails** (if Son is defined by rescalings g, Son ≥ 0) | fails | they have their own explicit formula; with zeros off the line, Prop 1 applied to their own identity: P_src fails. Their fluctuation ψ_g − x has exponent Θ_g > ½ (§4.1 with their zeros) |

Conclusion: P_src fails where there is an identity of type (3.1) with zeros off the line (Beurling) and is blind where the
zeros are modified without touching the source (M_m, Ξ_a, f_t); P_form fails in all cases but is E1. Exactly the
dichotomy of Theorem 2.

## 6. Is any non-E1 formulation left? What the theorem leaves open

Theorem 2 covers every property whose connection to W_T is "W ≥ Pos + Δ with Pos ≥ 0 and a norm bound on Δ". What is left
out, and only these could satisfy (a)–(c):
(O184.015a) properties that use **the structure of Son_S, not just Son_S ≥ 0** — e.g. that Δ_T be "small
relative to Son_S" in the Gabor directions at the ends (Δ ≥ −η·Son with η < 1), not in absolute norm.
But on P_T and over endpoint packets, Son_S of a normalized packet is bounded by Γ + O(1) (the packet does not see
primes: R184_004 §2.5), so the relative bound becomes absolute again: it falls into Theorem 2. ARGUED.
(O184.015b) properties that are **not** about norms: distributional ones (nonlinear in Λ, S2/S7) that force the
cancellation of 4.2 without going through the zeros — e.g. Möbius-disjunction-type pseudorandomness at logarithmic scale.
Every known version (Sarnak, Matomäki–Radziwiłł) gives o(·), not x^{−δ}: it does not give the exponent Θ−½ of (N′) (R166_802,
W4: unconditional = lower bound). No statement.
There is no candidate. The goal "write P(ζ) with (a)–(c)" is answered with the negative theorem, within the class of
Sonin-remainder-norm properties.

## State

| statement | label |
|---|---|
| Definition of P_src, P_form (§1) | — |
| Prop 1: P_src(ζ) ⟹ RH | PROVED (from (3.1) PROVED R183_029, Son ≥ 0 R183_018, detection R184_006/R162_2501 CITED) |
| Theorem 2(i): P_src blind to M_m | PROVED (R184_004 Thm 4(b)) |
| Theorem 2(ii): P_form = Q ∧ U, Q ⟺ RH | PROVED |
| Corollary 3 (source/form dichotomy; strong form of W11 for norm properties) | PROVED |
| 4.1 the trivial e^{T} is the pole, null on P_T | PROVED (truncated explicit formula CITED) |
| 4.2 remaining fluctuation of size e^{(2Θ−1)T} | PROVED above; Ω on average CITED (Landau/Ingham) |
| 4.3 ‖Δ_T‖ ≍ e^{(2Θ−1)T}, P_src ⟺ RH | ARGUED (depends on (M) and on minimality of s_S) |
| Table §5 | ARGUED (one line per model) |
| O184.015a | ARGUED (falls into Thm 2) |
| O184.015b | OPEN, no statement |
| Candidate P(ζ) with (a)–(c) | NO-GO in the class of remainder norms; OPEN outside |
| Row D | OPEN; no grid label moves |

## For the audit

1. **E_{S(T)} = W_T on P_T.** Verify that the semilocal form with S = {p < e^{2T}} and F supported in I_T reproduces the
   global form: the atoms at log p^k with p^k < e^{2T} and p ∈ S are all of them; the p^k with p ∉ S are > e^{2T}, outside
   supp F∗F̃. That R183_029's convention is [1, e^{2T}] and not [1, e^{T}] changes constants, not the exponent.
2. **Prop 1 and normalization.** The detection law is stated for λ_min with packets normalized in L²(I_T); Δ_T
   bounded in L² operator norm is the correct comparison. If R'_S is HS only under (M), Prop 1 is CONDITIONAL
   on Δ_T being bounded (it is if ε_S ∈ L¹(−2T,2T), Young).
3. **Thm 2(i).** Depends on "the source of M_m" being defined as (Λ, Γ). If someone defines the source of M_m including
   the a.c. density E_m of R162_2501 Thm 3, then P_src(M_m) fails — but E_m is exactly the zero difference:
   that definition is P_form. There is no intermediate definition.
4. **4.1: "the pole vanishes on P_T".** It does via the exact term e^{±u/2}; the truncated mean of the atoms differs from the
   pole by boundary terms (ψ(X) − X at the endpoint) which are again fluctuation. Check that no residual boundary e^{T}
   uncanceled by P_T appears: if it did, P_src would be FALSE for ζ (even better for the NO-GO).
5. **Theorem M.** Use: Son_S has no uniform margin to absorb Δ_T; it is only used in the remark of Cor 3, not in
   the proofs.
6. **It is not claimed** that RH holds, nor that D is closed, nor that P_src is false; only that its proof contains an
   equivalent of RH or is blind to M_m. 4.3 is ARGUED and the audit may downgrade it to OPEN without affecting Theorem 2.
