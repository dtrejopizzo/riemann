# AUDIT_200_PIMU_001: audit of PI_MU_001 (phase 200, round 5)

Row D and Lemma L′♯ as independent goals.
ARGUED / OPEN / NO-GO / REF-D / NUMERICAL. Verified against Paper 47 §22 (def:ext l.9601, lem:ext-mob, thm:ext-half,
prop:ext-gauge, prop:ext-consol, prop:ext-univ), Q2_LADDER_001 (Lemma R, l.49), SPEC_003 A.1 and MORI15_EXTREMAL_001
(l.15, 65, 80, 170, 198).

## 1. Π.0 (closed range)

**Correct. PROVED.** The argument is as follows. For even φ supported on [−1/λ,1/λ], ‖Q𝓕φ‖² = ⟨φ,(1−PB_λP)φ⟩ ≥
(1−χ_0)‖φ‖². The positive half gives the factor ½. The time–bandwidth pair ([−1/λ,1/λ], (−λ,λ)) has product 4 for every T, so
χ_0 is an absolute constant. It depends neither on T nor on μ (it is the same rescaling of prop:ext-univ).

L²_0 is the space of even functions, supported on [−1/λ,1/λ] with **zero mean** (∫φ = 𝓕φ(0) = 0). The closure is
correct: the constraint φ(0) = 0 is not L²-closed and disappears; ∫φ = 0 is closed and is retained.

**Objection (precision, not an error).** The phrase "the closure adds no singular objects" is false in the sense that matters. The
closure adds φ with **φ(0) ≠ 0**. For such φ, Poisson no longer gives Ψ̌_φ = Z(𝓕φ|): the term −φ(0)/2·e^{−y/2} appears. Also,
Φ_φ decays like e^{−|y|/2} and not like e^{−3|y|/2}. Hence Φ_φ falls outside the domain of 𝒲 from def:ext. This does not affect ℓ, which is
purely Fourier-based, but it does affect every use of 𝒲 on representatives of the closure (see §6).

## 2. Π.0′ (annihilator)

**Correct. PROVED.** For even φ one has ⟨𝓕φ|_{(λ,∞)}, h⟩ = ½∫φ·Ch, by Parseval. Ch is even, so being orthogonal to all
even zero-mean functions is equivalent to Ch|_{(−1/λ,1/λ)} ∈ span{1}. This is exactly the double condition: ψ = Ch constant on
[−1/λ,1/λ] and ψ̂ = 0 on (−λ,λ).

**Minor objection (citation).** Amrein–Berthier is a *uniqueness* theorem: there is no f ≠ 0 such that both f and f̂ have
finite-measure support. It is not used for the infinite dimension of 𝒦_T, which is trivial because 𝒦_T is the complement of a copy
of L²_0[−1/λ,1/λ] inside L²(λ,∞). The "CITED: Amrein–Berthier" should be removed.

**"Without ℕ"?** Yes. Restricting the datum to (λ,∞) is a band cutoff: Fourier structure, not arithmetic. 𝒟 = {r_f}
is likewise a Paley–Wiener class (rescaled PW_N, prop:ext-univ), without ℕ. ℕ enters in only two places:
- in E and in its Möbius inverse (which choose *which* r corresponds to which g);
- in Z, i.e. Poisson over ℤ with coefficients a_n ≡ 1.

The subspace and its annihilator do not see it. The claim is correct, but it is only half the story (§3).

## 3. Correction to AUDIT_AMU §4

**As a statement about 𝒢̄_T: PROVED, and tautological.** def:ext defines 𝒢_T using only T: support on [−1/λ,1/λ], φ(0) =
𝓕φ(0) = 0. No comb appears.

**But "the same for Beurling, cΛ, DH" needs to be made precise.** For a system with coefficients a_n over a set
of integers 𝒩 (with 1 ∈ 𝒩 and the others > 1), the correct definition is the following:
- the **summation map** is E_𝒩 f(x) = e^{x/2}Σ_{n∈𝒩} a_n f(ne^x);
- the **gauge** is ker E_𝒩 ∩ (admissible functions).

By triangularity (n e^x > 1/λ for x > −T and n ≥ 1), ker E_𝒩 contains the functions supported on [−1/λ,1/λ], and the
Möbius-type inversion (μ_𝒩) gives that two representatives differ exactly by that. Hence **the gauge as a set of
functions and its image 𝒢̄_T ⊂ L²(λ,∞) are indeed the same** for all, and ℓ = 2dist²(r, 𝒢̄_T) holds for all. On this point
the memo is right.

What is **not** the same is the framework. Ψ̌ = Zr (thm:ext-half) needs Poisson over ℤ with a_n ≡ 1:
- for Beurling (𝒩_B is not a lattice) there is no Z_B expressing the tail in terms of r;
- for cΛ the coefficients are d_c ≠ 1 (AUDIT_AMU §4 itself says so), so Poisson does not apply as is;
- DH has coefficients not ≡ 1 and the same thing happens to it.

Correct reformulation:

> "The exact Λ lives in (a) the inclusion 𝒢̄_T ⊂ rad 𝒲 (Guo L4.4) and (b) the intertwiner Z, which is ℤ
> arithmetic (a_n ≡ 1); it does not live in the subspace, which is the same for all."

With (b) omitted, the correction is PROVED but incomplete. AUDIT_AMU §4 was wrong in the word ("subspace"),
not in the idea ("descent is Λ-exact").

## 4. Π.1, Π.2, Π.3

**Π.1: PROVED.** It is the definition of the projector plus prop:ext-gauge (the distance part, without Guo).

**Closed formula §2.1: PROVED.** With one minor caveat. The "rank-one correction" from ∫φ = 0 is not written down, and
G*G = P(1−PB_λP)P must be read as compressed to L²_0. Both are standard.

**Π.2: PROVED, but its content is lem:ext-mob plus a verification.** The three conditions hold:
- (i) f_P is supported on [1/(dλ), λ/d] ⊂ [−λ,λ] for each d, so it does not touch 0;
- (ii) ∫f_P = P(½)-weighted × A(g) = 0. This is *the same computation* as in Lemma R (Q2 l.63, "∫h = e^{y/2}A(g)");
- (iii) Ef_P = g, because c_N = 0 for 1 < N < μ.

With that, the last sentence of lem:ext-mob ("two admissible representatives differ by an element of 𝒢_T") gives the conclusion.
**It does not use the radicality of Lemma R.** SQ.0/Lemma R is used only in the admissibility check. There is no
"something more": it is a corollary.

**Objection.** For the SQ.0 mollifier, the condition c_N = 0 (1 < N < μ) holds for the *sharp* cutoff Σ_{d|N, d<μ}μ(d). With
smoothed Selberg weights, P_S(log(μ/d)/log μ), one has c_N ≠ 0 for 1 < N < μ, so Ef_P ≠ g and the representative is
**not** in the same fiber. Π.2 must be restricted to ζP with coefficients vanishing on (1, μ).

**Π.3: PROVED.** The uniqueness argument for entire functions is correct: 𝓕(f − f′ − φ) is entire and vanishes on (λ,∞).

**Remark.** For 𝒲̄ to be *well defined* Guo is not needed. Π_μ r_f = Π_μ r_{f′} ⇒ f − f′ ∈ 𝒢_T ⇒
Ef = Ef′ ⇒ W_T(Ef) coincide. Guo is only needed to *identify* 𝒲̄(Π r) with 𝒲[Zr]. The "given Guo" label is superfluous on
half of Π.3.

## 5. R-Π: valid, and it collapses the architecture

**Validity.** Any Π with kernel 𝒢̄_T is U∘Π_orth, with U injective on 𝒦_T. Since 𝒢̄_T depends only on T (§3), the
"kernel" part cannot carry ℕ. Any arithmetic lies in U, and hence in B. **PROVED, and tautological.** "Blind to the comb"
is correct for the kernel. It is incorrect if read as meaning Π cannot be arithmetic: U can be, but that is,
by definition, part of B.

**Does it collapse?** Yes, outright. A_μ = B∘Π_μ with 𝒲̄ = ‖B·‖² − ℰ_μ and ℰ_μ ≤ (1−κ′)‖B·‖² on Π_μ(𝒟) is, by Π.1 and Π.3,
literally

 𝒲̄(k) ≥ 2κN^{−A₀}‖k‖², k ∈ Π_μ(𝒟) ⊂ 𝒦_T,

which is eq:ext-starstar (prop:ext-consol) written in the orthogonal complement. In the prolate basis it is exactly
prop:ext-consol (b) with the infimum over b already resolved. **The "build Π" step has no sign content.** Moreover, the
quotient was already implicit in prop:ext-consol and in prop:ext-univ.

**What remains for phase 200, concretely:**
1. The factorization A_μ = B∘Π_μ is no longer a program. It closes as architecture. Its only useful product is the
   *scenario*: 𝒦_1 is μ-universal and explicit (double vanishing).
2. The sign object is a form inequality on 𝒦_1 ∩ (rescaled PW_N), where the arithmetic input is
   identified in two places: the inclusion 𝒢̄ ⊂ rad 𝒲, and Z. Any B that does not use one of the two is comb-generic, and
   the corresponding falsifier (a_P, cΛ, Beurling) kills it (R-Q6).
3. Hence the admission criterion for any future B is: *name which property of Z or of Guo L4.4 it uses and that
   fails for Beurling.* Without that, it is REF-D or a duplicate.

## 6. f♯ and the jump comb

**The jumps are real (ARGUED → almost PROVED).** The Euler–Lagrange equation of the minimum over φ ∈ L²_0 gives
f♯_in = (PB_λf♯)_in + c on [−1/λ,1/λ]. B_λf♯ is entire, so f♯_in is analytic *up to the boundary*. f♯(1/λ⁺) = f_can(1/λ⁺)
is fixed by g. At μ = 15 it equals 1.5257 (MORI15 l.80): it is ≠ 0 and has no reason to coincide with (B_λf♯)(1/λ) + c. The
penalty for a jump σ is only σ²/(π²λ) in the leak, which is finite, so the L² minimum does not impose continuity. A single
example would suffice to upgrade it to generic PROVED.

**Defect omitted, and more serious: f♯(0) ≠ 0.** The analytic f♯_in has no reason to vanish at 0. With f♯(0) ≠ 0:
- Ψ̌_{f♯} ≠ Zr_{f♯}, because the term f♯(0)/2·e^{−y/2} is missing;
- Φ_{f♯} decays like e^{−y/2}, outside the domain of 𝒲;
- this is exactly the pole at s = 0 of the Mellin transform of f, which Guo L4.4 excludes by requiring f(0) = 0.

Hence **the "Domain Warning" of §3.1 underestimates the problem**: it is not just jumps.

**Is the comb arithmetic?** No. Positions T + log n, weights n^{−½}·1: it is the fingerprint of the summation E with
a_n ≡ 1, the same as rem:ext-killing (ii) (Λ∗1 = log). For Beurling it gives the comb at log n_B with the same weights. The
form σ²Σ(mn)^{−½}k(log m/n) is of Toeplitz type over log ℕ, with no (+,·) interaction at m ≈ kn. **It is comb-generic and
does not pass the semiring-principle filter.** The "new reason" against TEST_KINKS is valid as a distinction, but not as a
source of sign.

## 7. Test μ = 15

- ℓ* ∈ [4.4, 8.5]e−70 comes from MORI15 l.15/l.170, and the ½ is arithmetic. But the lower end is written as "4.4·10⁻⁷⁰
  ≲ ℓ" and described as "the structured part": it is an estimate, not a bound. The upper one, 8.45, is a bound from the
  family of gauges, legitimate because ℓ is an infimum.
- [2.2, 4.25]e−70 and [1.12, 2.16] are derived from published data with a heuristic endpoint: they are NUMERICAL-with-assumption, not
  pure NUMERICAL.

**Internal inconsistency.** The table applies Π.1/Π.3 to r* ("𝒲̄(Πr*) = W* (Π.3)"). But g* **is not in the core**: g*(T) =
−1.42e−34 ≠ 0 (MORI15 l.65), as the memo itself admits in §3.2(iii). Π.1 and Π.3 do not apply to r* as stated. The
row must say "by continuity/heuristic".

The coincidence W* ≈ ℓ* ≈ J²Σ|ρ|^{−2} is a single-μ observation. It is recorded as NUMERICAL and not used.

## 8. Verdict

**Label for PI_MU_001: ACCEPTED as a tool, with the following corrections. No sign. L′♯ OPEN. Row D OPEN.**

| item | auditor's verdict |
|---|---|
| Π.0 | PROVED. "Adds no singular objects" withdrawn (it adds φ(0) ≠ 0) |
| Π.0′ | PROVED. The Amrein–Berthier citation withdrawn |
| correction to AUDIT_AMU §4 | PROVED but incomplete. The intertwiner Z (ℤ-Poisson, a_n ≡ 1) must be added as a second Λ/ℕ-specific site; the r/Z framework does not exist for Beurling/cΛ/DH |
| Π.1, prolate formula | PROVED |
| Π.2 | PROVED (corollary of lem:ext-mob). Restrict to ζP with coefficients vanishing on (1, μ); smoothed mollifiers are excluded |
| Π.3 | PROVED. Well defined without Guo; the identification with 𝒲[Zr] requires Guo |
| ⊗_pΠ_p NO-GO, B (i)–(iii) | confirmed |
| R-Π | PROVED, tautological. Collapses A_μ = B∘Π_μ to eq:ext-starstar on 𝒦_T |
| f♯ jumps | ARGUED (an explicit example is still missing) + **new defect f♯(0) ≠ 0** |
| jump comb | comb-generic: not a source of sign |
| μ = 15 | NUMERICAL with heuristic endpoint. g* outside the core, so Π.1/Π.3 do not apply literally |

**Π.4: not worth pursuing as it stands.** It is poorly posed: the identity 𝒲[Ψ̌_{f♯}] = 𝒲[Ψ̌_f] requires f♯(0) = 0, and the
generic minimizer does not satisfy it, which takes it out of the domain of 𝒲.

If the gauge is restricted to φ(0) = 0, the infimum is not attained: that class is not closed. Moreover, even if it were proved, it
would only give a comb-generic form.

It would only hold in the weak version: "Guo L4.4 for φ ∈ L²_0 with φ(0) = 0 and boundary jumps". It is a technical lemma
whose only use would be B₊, which is already NO-GO by P2. **Recommendation: do not launch it.**

**The sign object, after R-Π.** It stops being a "factorization" and becomes a form inequality on the
universal scenario 𝒦_1. Its arithmetic input must be declared and verifiable in one of two places:
- (a) a property of Z = Poisson over ℤ with a_n ≡ 1 that fails for Beurling and cΛ;
- (b) a quantitative property of the inclusion 𝒢̄ ⊂ rad 𝒲 (Guo L4.4) finer than mere radicality.

Every proposal must name (a) or (b) and the falsifier that separates it. If it does not, it is REF-D or a duplicate of
E.4/DD.

## Entry for the index

- **AUDIT_200_PIMU_001.** Π.0, Π.0′, Π.1, Π.2 and Π.3 are accepted (PROVED), with corrections:
  - the closure of the gauge adds φ(0) ≠ 0, outside the domain of 𝒲;
  - Π.2 holds only for ζP with coefficients vanishing on (1, μ);
  - the correction to AUDIT_AMU §4 is completed: Λ/ℕ live in the inclusion rad *and* in Z.
- R-Π is tautological and collapses A_μ = B∘Π_μ to eq:ext-starstar on 𝒦_T. **Factorization architecture: closed.**
- Π.4: poorly posed (f♯(0) ≠ 0); not to be launched.
- Jump comb of f♯: comb-generic, not a source of sign.
- μ = 15: heuristic lower endpoint; g* outside the core.
- Do not retry: Π by relations, B as a function of Z or of the symbol, extension of Guo to minimal-leak representatives.
- L′♯ OPEN. Row D OPEN.

## Summary (≤200 words)

Π.0, Π.0′, Π.1 and Π.3 are PROVED. Π.2 too, but it is a corollary of lem:ext-mob and holds only for ζP with coefficients
vanishing on (1, μ); smoothed mollifiers are excluded.

Corrections:
- the closure of the gauge adds φ(0) ≠ 0, and those elements fall outside the domain of 𝒲;
- the Amrein–Berthier citation should be removed;
- the correction to AUDIT_AMU §4 is correct for the subspace, but omits the second arithmetic site: Z (Poisson over
  ℤ, a_n ≡ 1), which does not exist for Beurling/cΛ/DH.

R-Π is valid and tautological. A_μ = B∘Π_μ collapses to eq:ext-starstar on 𝒦_T, so the factorization architecture
is closed.

The jumps of f♯ are real (ARGUED). There is also an omitted defect, f♯(0) ≠ 0, which leaves Π.4 poorly posed; it is
recommended not to launch it. The jump comb is comb-generic.

At μ = 15 the lower endpoint of ℓ* is heuristic, and g* is not in the core.

The sign object becomes a form inequality on 𝒦_1 whose arithmetic is declared in Z or in Guo L4.4, with an
explicit falsifier. L′♯ OPEN. Row D OPEN.
