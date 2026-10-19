# R163_202 — Euler gate: uniqueness lemma, zero-side meaning, falsifiers (ANALYST, round 31)

**Status:** (U) PROVED, with an elementary support proof and with Cartwright–Levinson as a cross-check. The zero-side reading is exact.
**Verdict on (G): NO-GO as an independent gate.** Given (U), (G) on the window primes is *equivalent* to "no first contact at T", which is row D on that window. It is a restatement of the conclusion, at the same logical level as the Gamma gate R_LF=0. It is not a weaker statement. No RH or D claim. No label change.
Grid cell: row 5 (first contact / Euler side), col G. Wall it tries to evade: W2/W4/W5 (sign). It evades none of them: see §4.
Inputs: R163_161 (resolvent, eq. (5)–(6)), R163_162, R163_147 (Z_K), R162_2001/2190/2101 (two-atom curve).

## 0. Notation (R163_161)

F ∈ C_c^∞([−T,T]), K_F(s)=∫F(u)e^{(s−1/2)u}du, K_F(0)=K_F(1)=0. G=VJF, K_G(s)=K_F(1−s)/(1−s), supp G ⊂ [−T,T].
For a real p>1, ℓ_p=log p, U_p=√p τ_{−ℓ_p}. **Multiplier:** K_{U_pG}(s)=p^{s}K_G(s), because K_{τ_{−ℓ}G}(s)=e^{(s−1/2)ℓ}K_G(s).
So (I−U_p)^{−1} has symbol (1−p^s)^{−1} = −p^{−s}(1−p^{−s})^{−1}. Up to the unit −p^{−s}, this is the local Euler factor, with simple poles at s=iω_k, ω_k=2πk/ℓ_p.
H^{(p)}_G = Σ_{r∈ℤ}U_p^rG has Fourier coefficients K_G(−iω_k)/ℓ_p = K_F(1+iω_k)/[ℓ_p(1+iω_k)].

**(G_p)** :⟺ H^{(p)}_G=0 ⟺ K_F(1+iω_k)=0 ∀k∈ℤ (k=0 holds automatically).

## 1. Three equivalent forms of (G_p) (PROVED)

(a) K_G(iω_k)=0 for all k. Equivalently, K_G(s)/(1−p^s) is entire.
(b) Σ_{r∈ℤ} p^{r/2}G(u−rℓ_p)=0 for all u (zero two-sided weighted periodisation).
(c) G=(I−U_p)D for some D∈C_c^∞ (a compact p-coboundary). Then D=D_+G=D_−G.

Proof. (a)⟺(b) is Fourier series on ℝ/ℓ_pℤ of e^{−u/2}H_G (R163_161 (5)–(6)). For (b)⟹(c): D_+G = Σ_{r≥0}U^rG equals −Σ_{r<0}U^rG = D_−G. The first vanishes far to the left and the second far to the right, so D is compact. (c)⟹(b) is telescoping. ∎

For a finite set P of reals with log p pairwise ℚ-independent, the conditions (G_p), p∈P, hold together iff K_G/∏_{p∈P}(1−p^s) is entire. The reason is that the zero lattices iω_k^{(p)} are pairwise disjoint: 2πk/log p=2πj/log q with kj≠0 would give p^j=q^k. Each zero is simple, so it is removed by a simple zero of K_G.

## 2. Uniqueness lemma (U) (PROVED)

**Lemma U.** Let P be a finite set of reals >1 with log p pairwise ℚ-independent, and θ(P)=Σ_{p∈P}log p. Let supp G ⊂ [a,b]. If (G_p) holds for all p∈P and b−a < θ(P), then G=0, hence F=J(∂+½)G=0. In particular, for supp F ⊂ [−T,T], the condition θ(P)>2T suffices.

*Proof 1 (Paley–Wiener–Schwartz, sharp).* By §1, Φ(s)=K_G(s)/∏(1−p^s) is entire. Put s=σ+iy.
- For σ≥1, |K_G(s)| ≤ C e^{σb} and |∏(1−p^s)| ≥ ∏(p^σ−1) ≥ c e^{σθ(P)}. So |Φ| ≤ C′e^{σ(b−θ(P))}.
- For σ≤−1, |K_G| ≤ Ce^{σa} and |∏(1−p^s)| ≥ ∏(1−p^{σ}) ≥ c. So |Φ| ≤ C′e^{σa}.
- In the strip |σ|≤1, Φ is entire and |K_G|(1+|y|)^N is bounded. The denominator is an almost-periodic trigonometric polynomial with simple zeros. Φ is a ratio of two exponential-type functions, so it has exponential type, and Phragmén–Lindelöf on the strip bounds it polynomially from the bounds on the boundary lines σ=±1.
By Paley–Wiener–Schwartz (two-sided Laplace version; Hörmander, ALPDO I, Thm 7.3.1) Φ=K_D with D∈E′ and supp D ⊂ [a, b−θ(P)]. That interval is empty, so D=0 and G=(∏(I−U_p))D=0. ∎

*Proof 2 (elementary, via §1(c)).* From the joint condition, G=∏_{p∈P}(I−U_p)D with D compact. Let [α,β] be the hull of supp D. Expanding the product, the top term (−1)^{|P|}(∏√p) D(u−θ(P)) is the only one reaching u=β+θ(P). Every other term ends at β+θ(P′), P′⊊P. Likewise D(u) is the only term reaching u=α. Hence, if D≠0, then b−a ≥ (β−α)+θ(P) ≥ θ(P), a contradiction. ∎
(Proof 2 still needs the joint compact D. With pairwise disjoint simple lattices, that comes from Proof 1's Paley–Wiener step. For a single p it is §1(c) directly.)

*Cross-check via density (same threshold).* K_F(1+iy)=ĝ(−y) with g=e^{u/2}F, so y ↦ K_F(1+iy) is in PW_T. The zero set ⊃ Λ=∪_p{2πk/log p: k≠0} has the disjoint-union density Σ log p/2π = θ(P)/2π. By Cartwright–Levinson (Levin, *Lectures on entire functions*, Lect. 17, Thm 1), a nonzero Cartwright-class function with indicator width ≤ 2T has real-zero density ≤ 2T/2π·… precisely n(r)/r → (h(π/2)+h(−π/2))/π ≤ 2T/π. Λ counted on [−r,r] has n(r)/r → θ(P)/π. So θ(P)>2T forces f≡0. Removing the k=0 points changes n(r) by O(1), so the density is unaffected. Beurling–Malliavin is **not** needed: Λ has a genuine uniform density, and the Cartwright–Levinson count is enough. Separation of Λ is not needed either: the points from different p accumulate (Kronecker), but they are distinct.

**Thresholds on T∈[0.8047,1.5].** θ({2,3})=log 6=1.7918, which works for T<0.8959. θ({2,3,5})=log 30=3.4012, which works for T<1.7006. So {2,3} covers [0.8047,0.8959) and {2,3,5} covers [0.8047,1.5]. **Correction to the brief:** {2,3} alone does not reach 1.5.
**Window primes always suffice (PROVED).** For x=e^{2T}≥3, ∏_{p≤x}p > x. By Bertrand the largest prime p≤x has p>x/2, and 2p>x. So θ(x)>2T. For χ-type systems without 2 one needs x≥5, and then 3p>x. So for every T≥½log 3, the primes visible in the window [−T,T] already form a uniqueness set.

## 3. Zero-side meaning (PROVED identities)

1. The points 1+iω_k lie on Re s=1. They are the images, under the reflection s↦1−s built into V J (R163_161 (1)), of the local Euler poles −iω_k of (1−p^{−s})^{−1} on Re s=0. They are **not** zeros or poles of ζ. By de la Vallée Poussin ζ(1+iω_k)≠0 for k≠0, and by the functional equation ζ(−iω_k)≠0 as well. So K_F(1+iω_k) is not a zero-side quantity of ζ. It is a Mellin value of F alone at the reflected local-pole lattice.
2. Relation to the explicit formula. The p-term of the Weil explicit formula is the **one-sided, decaying** sum ℓ_pΣ_{m≥1}p^{−m/2}[f(mℓ_p)+f(−mℓ_p)]. The modes of (G_p) are Poisson-dual to the **two-sided, growing** sum Σ_{m∈ℤ}p^{m/2}G(u−mℓ_p) of §1(b). The two differ by the unstable branch U_p^r, r→+∞ (R163_162 (4)). The explicit formula only ever contains T_p=U_p^{−1*}-type weights. **(G) is therefore not encoded in the explicit formula**, and in particular not in any zero sum Σ_ρ K(ρ).
3. Functional form. (G_P) ⟺ K_F(w)·∏_{p∈P}ζ_p(1−w) is entire, with ζ_p(s)=(1−p^{−s})^{−1}. This is a divisibility statement for F against a finite Euler product. The constraint involves no ζ data beyond P.

## 4. Is (G) a restatement of RH/E1? (PROVED: yes, per window)

Let 𝒞_T be the set of primitive first-contact vectors at T, and P_T the window primes. By §2, the following are equivalent:
(i) every F∈𝒞_T satisfies (G_p) for all p∈P_T;
(ii) 𝒞_T={0};
(iii) λ_A(T)>0, i.e. D holds at window T.
The proof is (i)⟹(ii) by Lemma U plus Bertrand, and (ii)⟹(i) vacuously. Hence "(G) at a first contact" is the per-window conclusion itself. It is equivalent to E1 restricted to windows, by the same chain that makes R_LF=0 equivalent.
Moreover, (G) is a property of F alone that only 0 satisfies. So **no identity valid for general F can yield (G)**. Any derivation must use the contact equation. But R163_161 (9)–(10) shows that the contact equation sees only the Tate concomitant a_F K_F′(0) and none of the K_F(1+iω_k). The missing input is exactly a law that turns contact into vanishing of infinitely many Mellin values. That law is equivalent to the conclusion. **Walls not evaded: W2/W4/W5.** (G) trades the sign for a uniqueness statement, but proving the vanishing at contact still needs the sign.

## 5. Falsifiers

- **Beurling–DMV (real p).** Lemma U holds verbatim for ℚ-independent real logs, and integrality plays no role. Distinctness fails only when log p/log q∈ℚ: then the lattices collide, the zeros become double, simple vanishing no longer suffices, and the threshold drops. DMV systems have off-line zeros, so a genuine first contact with θ(P)>2T exists for windows beyond their first failure, and (G) is **false** there. So any proof of (G) must use the integrality of the log ℕ comb. Lemma U cannot supply it. ✔ (consistent: the forcing step is not where integrality enters, which is a warning sign).
- **Z_K = ζ(1−2^{−s})^{−K}.** Its 2-factor has symbol (1−2^s)^{−K−1}. H^{(2)} becomes a sum of u^j·e^{u/2}·(ℓ-periodic), j≤K, and the Z_K-gate needs vanishing to order K+1 on the 2-lattice. The first contact is at T_*^K∈(½log2,½log3) (R163_147). There P_T={2} and θ=log2<2T, so Lemma U does **not** apply, and (G_2) is neither forced nor excluded. UNDECIDED without numerics (not run here). This test is too weak to discriminate.
- **Λχ₂ (no 2-factor).** P_T ⊂ odd primes. For T≥½log5, θ_odd>2T (§2). Under GRH for that L the set 𝒞_T is {0}, so (G) holds vacuously. Consistent, not discriminating.
- **Two-atom Type I curve (R162_2001/2190/2101).** The symbol has only the factors 2,3 and a genuine (float-level) Type I contact F≠0 at T_*≈0.55–0.61. Wherever T_*≥½log3=0.5493, P_T={2,3}, θ=log6>1.22≥2T, and Lemma U gives **(G) FAILS for that F** (theorem, conditional only on the float existence of F). The fired falsifier is decisive: any purported proof of (G) using only the local 2- and 3-factors plus the contact equation is refuted. A proof must use the full ℕ comb (n=4,5,…) and the functional equation. Where T_*<½log3 on the curve, only p=2 is visible and the test is undecided.
- **Deletion of a prime q.** Lemma U still holds with P_T∖{q} once θ>2T. The deleted system is generically non-RH, so (G) fails at its contacts. ✔
- **Epstein / Davenport–Heilbronn.** There is no Euler product, so (G) cannot even be formulated. The gate cannot be checked there. ✔ (no false positive possible)

## 6. Conclusion

(U) is PROVED and sharp (θ(P)>2T). Window primes always suffice (Bertrand). (G) ⟺ D on the window: it is a restatement, not a weaker statement. The two-atom curve shows that local 2,3 data cannot prove it. The DMV line shows that the integrality must enter in the *derivation* of (G), not in (U), and no candidate derivation exists: R163_161 (10) contains none of the modes. **Route: NO-GO (restatement), with a reusable tool (Lemma U).**

## 7. Addendum after  R163_290

**(U) is trivial (accepted).** Take one prime with log p > b−a. The translates in §1(b) then have disjoint supports, so a zero periodisation forces G=0. Lemma U holds for **every** F≠0, so (G) ⟺ F=0 is circular, exactly as §4 already concluded. §2 stays only as a record of the sharp joint threshold.

**Does the contact equation constrain the modes? No. The obstruction is exact (PROVED).**
Let A_T be the compressed self-adjoint form on the window, H_T the primitive subspace (orthogonal to e^{±u/2}), and Π its projection. A first contact means A_T ≥ 0 on H_T with F ∈ ker(ΠA_TΠ). The full content of the contact equation (R163_161 (9)) is

 ⟨F, A_Tψ⟩ = 0 for all ψ∈H_T, i.e. F ⊥ Ran(ΠA_TΠ).     (★)

Each mode is a linear functional of F: K_F(1+iω)=⟨F,χ_ω⟩, with χ_ω=1_{[−T,T]}e^{(1/2−iω)u} (conjugation convention aside). Split Πχ_ω = r_ω + κ_ω, with r_ω ∈ closure Ran(ΠA_TΠ) and κ_ω ∈ ker(ΠA_TΠ) (orthogonal decomposition for the self-adjoint operator). Then (★) gives

 K_F(1+iω) = ⟨F, κ_ω⟩ + (Tate terms a_F, b_F already fixed by primitivity).

So (★) controls exactly the range component and is blind to the kernel component κ_ω. If the kernel is simple, ker = span(F), and κ_ω = ⟨χ_ω,F⟩F/‖F‖². The "constraint" is then K_F(1+iω)=K_F(1+iω): **a tautology**.

The mode would be forced to vanish iff Πχ_ω ∈ Ran(ΠA_TΠ), i.e. iff the inhomogeneous problem A_Tψ_ω = χ_ω (mod Tate) is solvable in H_T. By the Fredholm alternative that is again ⟨F,χ_ω⟩=0, which is circular. By (U) the family {χ_ω} over the window lattices is complete in L²[−T,T], so not all χ_ω can lie in Ran A_T unless ker=0. The obstruction is thus: **every linear consequence of a first contact is orthogonality to Ran A_T, and the Euler modes are coordinates of F along ker A_T, which a linear contact equation cannot see.** This is the precise form of R163_161 (10).

Consequences of a first contact that go beyond (★) are second-order:
(a) Hellmann–Feynman dλ/dT|_{T_*} ≤ 0. This involves only the boundary data F(±T), the Tate concomitants and the kernel at the endpoints (window derivative of the compression), not Mellin values on Re s=1.
(b) Second variation λ''. This involves ⟨F,·⟩ against Ran-resolvents, which brings the same blindness to κ_ω.
(c) Exterior/global identities: the full Weil form over ℝ, including Q_T-leakage (R163_162 (8)–(9)) and the unstable branch U_p^r. Only these contain the two-sided p-lattice of §1(b). Using them is exactly the missing sign law (W2/W4/W5).

**Recorded obstruction (O202).** A constraint on K_F(1+2πik/log p), k≠0, at a first contact must come from a non-compressed (exterior) identity that pairs F with the growing branch Σ_{r≥0}U_p^r. Within the compressed problem there is none: (★) is orthogonality to the range, and the modes live in the kernel. Any derivation of (G) is therefore a global identity on the full line, and that is equivalent to the conclusion.
