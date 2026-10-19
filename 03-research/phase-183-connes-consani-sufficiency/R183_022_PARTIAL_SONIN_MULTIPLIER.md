# R183.022 — Partial Sonin multiplier: Toeplitz / Wiener–Hopf analysis of Q_H

Phase 183. Sources: R183_015–020, Paper 47 (thm:P),
R155_031 (TK ceiling), master grid R162_2300 (log row 13: non-compact truncated
Wiener–Hopf). No web. Neither RH nor the closure of D is claimed.

**Corpus check.** In the grid, "Toeplitz/Wiener–Hopf" appears only as the
structure of the prime term (R183_018 Prop. 4.1, log item 13) and as the
Toeplitz ceiling TK from phase 155 (R155_031 W8: `Ceil(M,T)=sup_β inf λ_min(C_M)`,
a ceiling depending only on order M). "Landau" appears as Landau–Pringsheim and
localized Landau (R166_802), not as a Landau–Widom count. "Multiplier" does not
appear. The symbol-in-frequency angle for (L-Son) is new. The two corpus facts
used are: Paper 47 thm:P (Ky Fan ceiling for Q_T B_s Q_T) and thm:finZ
(no finite zero set carries a certificate).

Notation: I_T=(−T,T), F=ĥ ∈ PW_T, D=−i d/dt, P_T is the restriction to I_T,
m(s)=Re ψ(1/4+is/2)−log π. Numerically (control): m(0)≈−5.372 and the only
positive zero is s_m≈6.290. m(s)=log(|s|/2π)+O(s^{-2}).

---

## 1. Q_H as a Toeplitz compression — PROVED

Let H be measurable, 0≤H≤1, and even. Let S_T={p<e^{2T}}. Define the prime
symbol

    π_T(s) := Σ_{p∈S_T} σ_p(s log p),
    σ_p(θ) = 2log p Σ_{k≥1} p^{-k/2} cos kθ = 2log p (x cosθ−x²)/(1−2x cosθ+x²),  x=p^{-1/2}.

Also set σ_H := (1−H)m − π_T.

**Proposition 1.1.** (a) For h∈C_c^∞(I_T),
Q_H(h) = (1/2π)∫σ_H(s)|ĥ(s)|²ds = ⟨σ_H(D)h,h⟩. The integral converges
absolutely.
(b) On the prime side it is equivalent to sum all k≥1 or to truncate at
k log p<2T, or to add primes p≥e^{2T}. π_T is a bounded almost-periodic
(Bohr) function, with
−A(T) ≤ π_T ≤ B(T), where

    B(T)=Σ_{p<e^{2T}} 2log p/(√p−1),   A(T)=Σ_{p<e^{2T}} 2log p/(√p+1).

Both are ~4e^T by PNT (CITED: Σ_{p≤y} log p/√p ~ 2√y).
(c) **Non-uniqueness of the symbol.** Two tempered symbols σ, σ′ define the
same form on C_c^∞(I_T) if and only if (σ−σ′)ˇ vanishes as a distribution
on (−2T,2T).

*Proof.* (a) One has c_h(x)=(1/2π)∫|ĥ(s)|²e^{isx}ds. Since c_h is real-even in
the part used, Re c_h(a)=(1/2π)∫|ĥ|²cos(sa)ds. The series in k is
geometric and uniform in s, because Σ_k p^{-k/2}<∞ and S_T is finite;
this allows exchanging the sum with the integral. Also m=O(log(2+|s|)) and ĥ
is Schwartz. (b) supp c_h ⊂ [−2T+δ, 2T−δ] for some δ>0, because supp h is
compact in I_T. Hence the terms with k log p ≥ 2T vanish identically.
The bounds come from evaluating σ_p at θ=0 and θ=π. (c) The form is
⟨σ, |ĥ|²⟩/2π = ⟨σˇ, c_h⟩ up to a constant, and the c_h generate a dense
subspace of C_c^∞(−2T,2T): the polarized autocorrelations h₁*h̃₂ generate
that space by Titchmarsh/approximation. ∎

**Corollary 1.2 (Berezin).** For e_u = (2T)^{-1/2}e^{iut}1_{I_T}, in the
limit of the closed form, Q_H(e_u) = (σ_H * F_T)(u) with the Fejér kernel
F_T(v)=sin²(Tv)/(πTv²), of integral 1. Also ⟨e_u,e_v⟩=0 if u−v∈(π/T)ℤ∖{0}.
PROVED (direct computation). The only invariant is the symbol **averaged
at scale 1/T**. The pointwise sign of σ_H is not invariant, by (c).

## 2. Landau–Widom count: upper bound on n₋ — PROVED (+CITED)

**Theorem 2.1.** Suppose σ ≥ ε>0 for |s|≥s_0 and σ ≥ −M for |s|<s_0. Then

    n₋(P_T σ(D) P_T) ≤ N(T,s_0,M/ε) := #{k : λ_k(S_c) > ε/(M+ε)},   c=Ts_0,

where S_c = Q_T B_{s_0} Q_T is Paper 47 thm:P's time–band concentration
operator. By Landau–Widom (CITED, PROLATE-REFERENCES no. 3),
N = 2Ts_0/π + (1/π²) log(Ts_0) log((M+ε)/ε)·(1+o(1)). Paper 47 thm:P also
gives the non-asymptotic bound N ≤ #{k: Λ_k(c) > ε/(M+ε)}.

*Proof.* Pointwise σ ≥ ε − (M+ε)1_{|s|<s_0}. Hence
Q ≥ ε‖h‖² − (M+ε)⟨S_c h,h⟩. Let V be a subspace on which Q<0. If dim V
exceeded N, V would intersect S_c's spectral subspace {λ ≤ ε/(M+ε)} (by
Cauchy/minimax). There Q ≥ ε‖h‖² − ε‖h‖² = 0, a contradiction. For a
strict version, take ε′<ε. ∎

**Corollary 2.2 (pointwise bound on s_0 — PROVED).** For H≡0, σ_0 = m − π_T ≥ ε
on |s|≥s_0 holds if m(s_0) ≥ B(T)+ε. One has m(s_0)=log(s_0/2π)+O(s_0^{-2}), so

    s_0(T) = 2π exp(B(T)+ε)(1+o(1)) ≈ 2π exp(4e^T).

The bound is essentially optimal for **pointwise** positivity. The
log p are linearly independent, so by Kronecker/Bohr the set
{s : π_T(s) > B(T)−ε′} is relatively dense. Hence σ_0 takes negative
values in every sufficiently long interval below m^{-1}(B(T)−ε′). Theorem
2.1 then gives n₋ ≤ ~(2T/π)·2π e^{4e^T}, a doubly exponential and
**useless** bound.
Conclusion: the pointwise representative of the symbol is the wrong one
(Prop. 1.1(c)). The spectral representative must be used.

## 3. The spectral representative and the NO-GO for H depending only on frequency

**Proposition 3.1 (explicit formula in the window — CITED: Weil;
R183_015 normalization).** For h∈C_c^∞(I_T) primitive (ĥ(±i/2)=0), with
S ⊇ S_T,

    E_S(h) = Q_0(h) = Σ_ρ ĥ(γ_ρ) conj ĥ(conj γ_ρ),   ρ=½+iγ_ρ, with multiplicity.

In other words, σ_0 ds/2π ≡ Σ_ρ δ_{γ_ρ} modulo symbols invisible in the
window (Prop. 1.1(c)). The archimedean term is the smooth Riemann–von
Mangoldt density, m/2π ≈ (1/2π)log(|s|/2π) = N′_smooth. The prime term is
the oscillating part. The zero set is symmetric under γ↦conj γ (ρ↦1−conj ρ),
without assuming RH.

Hence, for every H,

    Q_H(h) = Σ_ρ F(γ_ρ)conj F(conj γ_ρ) − (1/2π)∫ H m |F|²,   F=ĥ.   (3.1)

**Remark 3.2 (direction of the give-up — PROVED).** (L-Son) requires that
the given-up part (1/2π)∫Hm|F|² be ≥0 (it is η·Son). Then Q_H ≤ E_S and
n₋(Q_H) ≥ n₋(E_S). Hence:
(L-Son) with any H ⟹ n₋(E_S|primitives) ≤ 1 ⟹ (R183_017's threshold)
E_S ≥ 0 in window T. The lemma is **never weaker** than D_T.

**Theorem 3.3 (NO-GO for H in frequency on the sub-Landau band) — PROVED
(non-optimal constant).** Fix g∈C_c^∞(I_T), g=φ(·/T), φ∈C_c^∞(−1,1).
There exists C_φ≥1 such that the following holds. Let J=[a,b] with
a>s_m+1 and log(b/2π) < 2T/C_φ. Suppose H ≥ η > 0 on J^{+1}=[a−1,b+1].
Then

    n₋(Q_H |_{primitives ∩ ker ∫h}) ≥ (b−a)(T/(πC_φ) − log(b/2π)/2π) − C′_φ log(2+b) − 3.

This holds without assuming RH. In particular, for every η>0 there exists
T_1(η,φ) such that if H≥η on an interval of length ≥1 within
[s_m+1, 2π e^{2T/C_φ}], with T≥T_1, there are two negative directions.
Moreover, n₋ → ∞ like T·|J|.

*Proof.* Take the packets h_j(t)=e^{i(a+jκ)t}g(t), j=0,…,N−1, with
κ=C_φ π/T and N=⌊(b−a)/κ⌋. First, the Gram matrix is T·(|φ|²)^(C_φ π(j−k)),
and by the rapid decay of |φ|²'s transform it is ≈ T‖φ‖²Id if C_φ is
large. So dim V = N. Second, F_j=ĝ(·−a−jκ) with
|ĝ(z)| ≤ C_K T(1+T|Re z|)^{-K}e^{T|Im z|}. Impose F(γ)=0 for every zero
with Re γ∈[a−R,b+R]. There are
Z ≤ (b−a+2R)log(b/2π)/2π + O(log b) of them (CITED: Riemann–von Mangoldt
with S(t)=O(log t)). The conditions F(±i/2)=0 and F(0)=0 are added. This
leaves W⊂V of dim ≥ N−Z−3. On W, by (3.1), the zero sum only sees
|Re γ−s|≥R for s∈J. By the packets' decay and |Im γ|≤½, that sum is
≤ δ_R‖h‖², with δ_R→0 as R grows (R depending only on φ and η). The
given-up part is ≥ η m(a−1)(1−δ′)‖h‖²/(norm) > δ_R‖h‖², because m>0 on
J^{+1} and F's mass outside J^{+1} is ≤ δ′. Hence Q_H<0 on W∖{0}. Since
conj γ is also a zero, annihilating F at γ also covers the cross terms. ∎

**Reading.** The band [s_m, 2πe^{2T}] is exactly where the zero density
(1/2π)log(s/2π) falls below PW_T's Landau density T/π. There, there are
more degrees of freedom than zeros, and giving up any fixed fraction of
m produces negative directions in number ∝ T·|J|. With the optimal
constant (prolates instead of Gabor packets; Landau–Widom) the threshold
would be log(b/2π)<2T; this is ARGUED, not proved here. Control remark:
for T=½log 2, 2πe^{2T}=4π≈12.57 < 14.13 (first zero). So the useful band
[6.29,12.57] gives (T/π)·6.3≈0.69 degrees: less than one extra direction.
This is consistent with the ½log 2 frontier of R183_018/019, though it
does not explain it.

**Corollary 3.4 (dichotomy for H depending only on frequency) —
PROVED/OPEN.** Let H=H(|s|) with 0≤H≤1 and the given-up Hm ≥0.
(i) If H ≥ η>0 on an interval of length ℓ_0(η,T) within
[s_m+1, 2πe^{2T/C_φ}]: n₋(Q_H) ≥ 2 for T≥T_1. It is NO-GO (Thm 3.3),
PROVED.
(ii) If H vanishes (almost) below 2πe^{2T}: (L-Son) is equivalent to
E_S ≥ −rank one + η·∫_{|s|>Ω}m|F|²/2π. By Remark 3.2 this implies D_T,
plus a **Beurling–Landau sampling inequality for the zero set** at
heights >2πe^{2T}:
Σ_ρ F(γ)conj F(conj γ) ≥ η(1/2π)∫_{|s|>Ω} m|F|² − rank one. It is
strictly stronger than D_T (OPEN). Under RH and with average zero
spacing it is plausible (sampling above critical density, CITED Landau
1967 for separated sets), but the zeros of ζ are not known to be
uniformly separated.
**Verdict:** with H depending only on frequency, (L-Son) is either
NO-GO or a **strengthened reformulation** of D_T. It is never weaker.

## 4. The minimal H non-diagonal in frequency

By Remark 3.2, no H gives anything for free: everything given up comes
out of the surplus Σ_ρ|F(γ)|² − (negative part). The only H with a real
chance is one that gives up **only the high-frequency modes above the
critical density**, commuting with the time–band concentration.

Set Ω_T=2πe^{2T}(1+δ). Let Π_T be the spectral projection of
Q_T(1−B_{Ω_T})Q_T onto eigenvalues ≥½ ("high" prolates). It is
complementary, up to O(log) modes, to the ≈2TΩ_T/π = 4T e^{2T}(1+δ)
"low" prolates. Take H=ηΠ_T. This commutes with I_T's prolate operator,
not with D.

**Open lemma (L-Son′).** For T>½log 2 there exist δ,η>0 and b≥0 such
that, for every primitive h∈C_c^∞(I_T),

    E_S(h) − η·(1/2π)∫ m |(Π_T h)^|² ≥ −b|⟨v,h⟩|²,

with R183_017's threshold. It decomposes into two pieces:
(a) **low piece** = E_S restricted to a finite-dimensional space
≈4Te^{2T}(1+δ) (low prolates). It is a finite matrix inequality of the
certificate/TK-ceiling type from Paper 47. thm:finZ forbids certifying it
with a finite number of zeros: all primes p<e^{2T} must be used
(R162_2602 Thm 4(b)). OPEN.
(b) **high piece** = Beurling–Landau sampling of the zero set with
weight m at supercritical density, with constant 1−η. It is the "easy"
part of R183_018 §6(iii). CONDITIONAL on RH at heights >Ω_T and on a
separation/clustering bound. Without RH: OPEN.
(c) **cross term** between the pieces. It is controlled by the prolate
leakage O(e^{-c·log}) from Landau–Widom in the transition zone. ARGUED.

Honest comment: (a) is D_T on a subspace of dimension ~4Te^{2T}, which
contains all the low-frequency difficulty (m<0, the ĝ(0) direction).
(L-Son′) does **not** reduce the difficulty. It translates it into a
finite problem that is row D in the window. It is a reformulation, not
a weakening.

---

## Status

```
Prop 1.1  Q_H = Toeplitz compression; exact prime truncation; symbol non-uniqueness   PROVED
Cor 1.2   Berezin symbol = σ_H * Fejér_T                                               PROVED
Thm 2.1   n₋ ≤ #{λ_k(S_{Ts0}) > ε/(M+ε)} (asymptotic Landau–Widom)                    PROVED (+CITED)
Cor 2.2   pointwise s_0(T) ≈ 2π exp(4e^T); doubly exponential, useless count           PROVED
Prop 3.1  E_S = Σ_ρ F(γ)F̄(γ̄) on window primitives                                    CITED (Weil)
Remark 3.2   (L-Son), with any H, ⟹ D_T                                                PROVED
Thm 3.3   H≥η on sub-Landau band ⟹ n₋ ≳ T|J|(1/πC_φ − ...) → ∞; without RH              PROVED (non-optimal constant)
          optimal threshold log(b/2π) < 2T via prolates                                 ARGUED
Cor 3.4   H depending only on frequency: NO-GO, or strengthened reformulation of D_T     NO-GO / OPEN
Lemma (L-Son′) H = ηΠ_T (high prolates): (a) finite ≈ D_T, (b) sampling, (c) cross     OPEN / CONDITIONAL(RH) / ARGUED
E_S ≥ 0 / row D                                                                            OPEN
```
No symbol of the program changes. D OPEN.

## Review points

1. **Normalization of (3.1).** It must be checked against R183_015 that
   the constant in front of Σ_ρ is 1 (not 2π or ½) and that no polar
   term remains on primitives. A constant factor shifts Thm 3.3's
   constants but not the NO-GO.
2. **Thm 3.3, Gram condition.** The claim "Gram≈T‖φ‖²Id for large C_φ"
   uses that |φ|²'s transform decays rapidly. It must be checked that the
   off-diagonal errors, summed over N indices, stay small (Schur bound
   with decay ≥ |j−k|^{-2}).
3. **Sum of distant zeros.** δ_R is bounded via ĝ's Schwartz decay in the
   strip |Im|≤½ and via N(t+1)−N(t)=O(log t). Uniformity in the band
   size must be checked: R's bound depends on b only logarithmically.
4. **Prop. 1.1(c).** The density of polarized autocorrelations in
   C_c^∞(−2T,2T) is used for the "only if". For the NO-GO, the "if"
   suffices.
5. **Remark 3.2** assumes the given-up part is ≥0 as a form. If
   (L-Son) allowed giving up a form of indefinite sign, the implication
   (L-Son) ⟹ D_T would fail. But then the given-up part would no longer
   be a piece of Son ≥0, contrary to R183_018 §6.
6. **Risk of tautology in (L-Son′)(a).** It is D_T in finite dimension.
   It must be treated as a reformulation, not as progress.

## Note (R183_027)

* Thm 3.3: downgraded from PROVED to **CONDITIONAL(RH)**. The bound on
  distant zeros uses |ĝ(γ)| ≤ … e^{T|Im γ|}; without RH the factor
  e^{T/2} is not compensated by an R depending only on φ and η.
* Remark 3.2: the given-up part ∫Hm|F|² is not η·Son, because Son's
  density is m + ε̂, not m. §3's NO-GO treats an object different from
  (L-Son) of R183_018 §6.
