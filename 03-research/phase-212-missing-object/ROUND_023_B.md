# ROUND_023_B — Gate: (PC) compressed before pairing and orientation of the terminal jump

Question. Is there an operation outside 𝒞_w, not a square, that orients the jump
h_p(p) − h_{p−1}(p) = −log p (R161_002 Cor. 8.2) using the non-commutation of P_T with 𝓕, through
C_T = (1−P_T)𝓕P_T, C_T^{(N)} = (1−P_T)S_N𝓕Π_T and E_{N,T} = P_T(S_N𝓕 − JS_N)Π_T?

Verdict: **DOES NOT PASS (no mechanism).** It is not a literal repetition: the terrain is listed as open
(RULES_AVOID K7; ROUND_004_A, «Not excluded»; master index B.2 item 27). But I cannot write a
formula that orients the jump without falling into a format affine in the weight, into a square or into a
weight that installs the answer.

## (1) Closest antecedent (open and read)

- R161_002 §3: defines C_T, C_T^{(N)} and E_{N,T}; the only declared escape = «keep the boundary compression
  before taking the square or the oriented pairing»; the remainder without compression returns to R160_D4_R2 Thm. 5.1.
- R161_002 §4 (SP-161) and §5 (L161.1): a_T = Σ w_N Re⟨R_{M,N}F, S_N𝓕F⟩ + B_T(F); rules: the norm
  fails by Thm. 1.1, spectral weights install the answer and a Douglas factorization is EQUIV.
- R161_002 §8: Thm. 8.1 (NO-GO, w ≥ 0) and Cor. 8.2 (−log p as terminal derivative).
- ROUND_004_A Lemma 1, Cor., Prop. 2: in 𝒞_w (real w) there is no interior telescoping plus tail
  cancellation (Σw = 1 versus Σw = 0); the pure derivative δ_{N+1} − δ_N gives coefficient G(1) = 0 (a_T does not appear).
- R161_032 §§4–6: (4.2) 0 = X_T + ‖r‖² + D^orient + 2D^Γ, OPEN/TERMINAL; RULES_AVOID K1 («reopening requires
  an identity connecting a leakage square with the PC defect, not another leakage square»), K2
  (oriented variance 030, generic), U2 (oriented L161.3 OPEN; R161_029 monotonicity false).

## (2) What can be written and what cannot

Observation (ARGUED, support computation, not derived beyond this). For a prime p > e^{2T}, the
jump in N of E_{N,T} is

  E_{p,T} − E_{p−1,T} = p^{−1/2} P_T(τ_{log p}𝓕 − Jτ_{log p})Π_T = p^{−1/2} P_T τ_{log p}(1−P_T)𝓕Π_T,

because Jτ_{log p}Π_T and τ_{log p}P_T𝓕Π_T are supported outside (−T,T). That is: after compression,
**the terminal jump at large primes lives entirely in the leakage** (1−P_T)𝓕Π_T, and what does not commute
(P_T with 𝓕) is the only thing that sees it. This is exactly what R161_002 §3 had announced.

What the requested operation would need: a functional Φ_T(F), not a square, outside 𝒞_w, with
Φ_T = a_T(F) + (terms ≥ 0), in which the sum of those jumps weighted by Λ enters with fixed sign.
The three routes of the assignment give:

- (i) Tests other than S_N𝓕F: the pairing ⟨G, Σ_p Λ(p)p^{−1/2}P_Tτ_{log p}(1−P_T)𝓕F⟩ is linear in Λ for
  fixed G (affine in the weight: F3); with G = G(F) quadratic or normalized a square reappears (Thm. 1.1) or
  the test collapses into the mixed pairing of (PC-ren) (R161_023; K1). I do not have a G that escapes both.
- (ii) Weights w_N(F): for each fixed F the identity is scalar and the weight is one real per F; choosing it so
  that the identity closes is solving a_T(F) inside the weight (SP-161: «installs the answer»). Without a
  canonical rule prior to Λ (requirement of L161.1) there is no formula.
- (iii) R161_032 (4.2): still not derived; the source requires starting from the two non-recombined
  orientations and polarizing with the reflected port. I do not have the boundary Green identity that
  produces ε⟨v,j⟩ together with D^orient and D^Γ; I do not invent it.

## (3) Why it does not avoid the failure of the antecedent

The failure of 𝒞_w is arithmetic in the index N: any fixed weight gives log p·Σ_{N<p}w_N at p. The
compression changes the carrier of the jump (it moves to the leakage) but not its shape: it is still
Λ(p)·(fixed operator independent of Λ). Orienting it requires degree ≥ 2 in Λ (F3: the affine is blind)
and the only known degree-2 term in this architecture is the divisor variance (K2), which
vanishes for every weight (generic). None of (i)–(iii) provides a non-generic degree-2 term.

## (4) Connection with 𝔸_M ⪰ 0 and controls

Necessary identity (not available): a_T(F) = Φ_T(F) − (sum of leakage squares of C_T, C_T^{(N)})
with Φ_T ≥ 0 by an oriented sign of the compressed jump; via Paper 47 prop:AM it would give 𝔸_M ⪰ 0 for M ≥ e^{2T}.
Controls: with the observation of (2) the compressed jump is p^{−1/2}·w(p)·(fixed operator) for
any weight w; hence (a) substituted weight 2Λ, (b) deleted power and (c) Beurling pass through the
same step without breaking: **no named step fails** under the three controls (F1 not met). That is
the reason for the verdict.

## Status

- Observation of the jump in the leakage: ARGUED (support; not used as proof).
- Orienting operation outside 𝒞_w and not a square: OPEN, without formula.
- K7 remains open; this gate neither closes nor excludes it.
- Record: the index is not edited here (it is updated separately).
