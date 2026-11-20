# Round 14, memo B: Schur–Schoenberg positivity on the Euler product as an independent source of a non-Gram block

Summary. The candidate is a kernel 𝕂 on the window, positive definite because it is a Hadamard (Schur) product
of per-prime factors, or the exponential of a conditionally negative generator (Schoenberg), from which `a_T` would be
recovered by a nonlinear operation (generator at `t = 0`, logarithmic derivative, Loewner matrix,
Schur complement against the archimedean factor). The cross-check finds the idea in the corpus: `ROUND_013_C`
O10, `INV_F_001` (Thm. F1–F2, Cor. F3, row C5) and `RULES_AVOID` M3–M4. In addition I prove, in the class declared
below, that **every Schur product positivity on per-prime factors survives the three checks**
(Lemma 2), and that the Schoenberg variant «for all t» is a local per-prime split (Lemma 1). Verdict:
repetition and selection NO-GO; M4 is improved only partially (§4).

Primary-source reading: `RULES_AVOID` M, Q–W; `ROUND_013_B` (Lemmas 1–3 and «Operation that would reopen the class»);
`ROUND_013_C` §§2–3 (table O1–O14, Lemmas T and K); `ROUND_009_G3` (list P1–P12); `phase-194-invention/
INV_F_001_DLOG_WALL_CONES.md` §§1–4; routes index, README, entries «Total positivity / PF» and INV_F_001.
Grep in `03-research` for Schoenberg, Lévy–Khintchine, Loewner, Pólya frequency, «conditionally negative»:
the relevant hits are INV_F_001, row O10 of ROUND_013_C and the memos 104_21/AUDIT_A cited in the
index (total positivity fails at PF₂ / PF₅). The other hits (phases 78, 163, 186, 206) use the words
in passing; reading by header, ARGUED.

## 0. Four-point filter

1. **Closest antecedent.** `INV_F_001` §2 row C5 and Thm. F2: «every conic premise on log ζ or −ζ′/ζ
   holds for ζ^c», with the infinitely divisible class (Lévy–Khintchine/Schoenberg) among those crossing ∂log;
   hypothesis to break: H_cone (homogeneity in log ζ). `ROUND_013_C` O10: «the exponential (Schoenberg/Fock) of
   a form is positive ⟺ the form is conditionally negative: reformulation; the Schur product S∘W
   needs W ⪰ 0». `RULES_AVOID` M3 (total positivity fails at order 2) and M4.
2. **What is proposed as new.** A 𝕂 that is a Hadamard product over primes, from which `a_T` comes out by a nonlinear
   operation. The only thing not recorded in primary sources is the matrix form of the argument (Lemmas 1–2), not an object.
3. **Does it avoid the difficulty?** No. The difficulty of the antecedent is H_cone: the premise is invariant under
   `log ζ ↦ c log ζ`. In a Schoenberg semigroup the parameter `t` multiplies the generator; if the generator
   contains the prime part, `t` is exactly the check `c` (with the archimedean part scaled at the same time). If only
   a fixed `t` is used, the Schur product is preserved under integer Hadamard powers, and `c = 2` is an integer
   (Lemma 2). In neither case is there a signed step that fails at `c = 2`.
4. **Global link.** The only one would be Schoenberg applied to the generator `ψ = −a_T` (kernel), which is the
   reformulation O10: «ψ conditionally negative» is the sign statement itself. Moreover Schoenberg speaks of
   codimension one (Σ c_i = 0, or ∫Fφ = 0 after conjugating by diag φ), whereas `P_T` has codimension two;
   the codimension-one statement is stronger than the one sought (ARGUED that it is neither needed nor available).

Answer to the central critical question: positivity for all `t > 0` cannot distinguish `t = 1` from
`t = 2`, because it is a property of the generator (cone), and positivity at fixed `t`, if it comes from a Schur
product, is inherited by integer powers. The object is blind to `c = 2` in both readings. By the filter
rule, I stop before building and use the rest to fix the class closure.

## 1. Declared class

Discretization: a finite set of points `t_1, …, t_N` of the window (or any finite family of
tests), and real symmetric matrices. Write `ψ = A − Σ_p P_p`, with `A` the archimedean matrix and `P_p` the
contribution of the powers of the prime `p` (weights `v_{p^k}`). For a general weight `a` (cΛ, deletion,
Beurling) `P_p^a` is the corresponding matrix; for `cΛ`, `P_p^{cΛ} = c P_p`. `J` is the all-ones matrix,
`∘` the Hadamard product, `e^{∘M}` the entrywise exponential.

**Class 𝔖.** Certificates in which the sign is deduced from the positive semidefiniteness of a kernel
`𝕂 = 𝕂_∞ ∘ ∘_p 𝕂_p` obtained by the Schur product theorem from `𝕂_∞ ⪰ 0` and `𝕂_p ⪰ 0`, where
`𝕂_p` depends only on the weights of the powers of `p` and `𝕂_∞` does not depend on the weight.

## 2. Results

**Lemma 1 (Schoenberg by factors = local split; PROVED).** If for all `t > 0` one has
`e^{∘(−tA)} ⪰ 0` and `e^{∘(tP_p)} ⪰ 0` for each `p`, then `A` is conditionally negative and so is each `−P_p`;
hence `ψ = A − Σ_p P_p` is conditionally negative because it is a sum of such matrices, and the same
holds for `A − c Σ_p P_p` with every `c ≥ 0`, for the deletion of the whole factor of a prime `p` and for
any Beurling system whose factors satisfy the hypothesis. (Deletion of a single power `p^k`
is covered if the reduced factor still satisfies the hypothesis.)

*Proof.* Schoenberg (CITED): `e^{∘(−tM)} ⪰ 0` for all `t > 0` ⟺ `M` conditionally negative. Conditionally
negative matrices form a convex cone. ∎

Consequence: the «for all t» variant is a per-atom split with local positivity, i.e. the
closed family Q1/O1 («compensation without per-atom positivity» in the inverse sense: here each atom would have to be
positive on its own). With battery E (CITED: negative direction of `a_T(2Λ)`), the per-factor hypothesis is
false for Λ: if it held, it would hold for `2Λ`.

**Lemma 2 (Schur product at fixed t is blind to integer c; PROVED).** In the class 𝔖, if
`𝕂^Λ = 𝕂_∞ ∘ ∘_p 𝕂_p^Λ ⪰ 0` is deduced from `𝕂_∞, 𝕂_p^Λ ⪰ 0`, and the factors are exponentials of the weights,
`𝕂_p^{a} = e^{∘ P_p^a}`, then:
(i) `𝕂^{2Λ} = 𝕂_∞ ∘ ∘_p (𝕂_p^Λ ∘ 𝕂_p^Λ) ⪰ 0` (and for every `c ∈ ℕ`);
(ii) deleting the factor of a prime (or a power, if the reduced factor is still ⪰ 0) gives `⪰ 0`;
(iii) for Beurling, if each factor is ⪰ 0, the product is ⪰ 0.

*Proof.* `e^{∘ 2P} = e^{∘P} ∘ e^{∘P}`, and the Schur product of semidefinite matrices is semidefinite (CITED,
Schur 1911). (ii) and (iii) are the same theorem with fewer or with other factors. ∎

Thus the signed side never ceases to be `≥ 0` under any check. By Lemma T of `ROUND_013_C` (PROVED in its
class), a deduction `𝕂^a ⪰ 0 ⇒ a_T^a ⪰ 0` uniform in the weight would prove positivity at `c = 2`, against
battery E. Every non-uniform deduction has to use an identity proper to Λ ((PC), `Λ∗1 = log`), and then
the sign comes from the blind object plus an unsigned restriction: Lemma T.

**Observation (exponential of the prime side; CITED/ARGUED).** The Euler product is the exponential in the
frequency variable of `Σ Λ(n)/log n · n^{−s}`, i.e. a convolution product in `log`, not the
Hadamard exponential in `(t,s)` of the kernel `Σ v_n δ(t−s∓log n)`, which is not defined for deltas. In the
variable `τ`, `exp(Σ b_n (cos(τ log n) − 1))` is positive definite if `b_n ≥ 0` (Lévy–Khintchine): it is row
C5 of `INV_F_001`, conic premise, covered by F2. The identification «exp of the prime part = Euler
product» of the brief holds only in this frequency sense.

**Loewner/Pick and total positivity (CITED, repetition).** Positive Loewner matrices ⟺ operator monotone
function ⟺ Pick: it is the cone C6–C7 of `INV_F_001`, zero side (REF-D, thm:Z, not retried). Total
positivity / PF: M3 and the index (fails at PF₂ for the relevant kernel, PF₅ for that of dBN).

## 3. Checks (R3-i)

- `c = 2`: the factors are `⪰ 0` and so is their product (Lemma 2 (i)); what fails is the deduction or the
  equality, never a signed remainder.
- Deletion: Lemma 2 (ii).
- Beurling: Lemma 2 (iii); the formal Beurling Euler product has factors of the same type.

## 4. Status of M4

- PROVED here: class 𝔖 (Schur product with exponential per-prime factors, at fixed `t`) and its
  per-factor Schoenberg variant for all `t` are blind to `c = 2`, to deletion and to Beurling (Lemmas 1–2).
- Still ARGUED: that only the infinitely divisible and Pick classes cross ∂log (the table of `INV_F_001`
  has eleven cones, not a classification).
- Left uncovered by 𝔖 (OPEN, no object): per-prime factors **not** exponential in the weight (e.g.
  `𝕂_p` with positivity only at non-integer exponent, fractional Hadamard of FitzGerald–Horn), and Hadamard
  positivity coupling distinct primes (not factored by prime), which is the only way to break H_cone. Neither
  has a written candidate; the second would have to go through the additive structure (S2: «every recursion must
  couple the additive structure»).

## 5. Verdict

Repetition of O10 (`ROUND_013_C`) and `INV_F_001` F2/C5; selection NO-GO. Lemmas 1–2: PROVED (on
Schoenberg and Schur, CITED). Global sign of `a_T`: OPEN. Next explicit operation, if any: a Hadamard
kernel ⪰ 0 whose factor does not separate by primes and that uses `m ≈ kn` (additive collisions) in the entry
`(t,s)`, with a signed step that fails at `c = 2`; I do not propose it because I do not have its formula.
