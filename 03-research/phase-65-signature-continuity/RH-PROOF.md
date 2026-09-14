# RH-PROOF — the closed chain (Signature-Continuity Package, capstone)

> **R3 update (supersedes the decisive step below).** The Connes/Consani round R3 replaced the
> arbitrary-pairing realization with the **log-derivative of the spectral determinant**: `M_P =
> −∂_z log D_P^∘ − E_P'/E_P` is Herglotz because `D_P^∘` has real zeros (self-adjointness G2 = input
> **H1**), and the **trace-log identity** `−∂_z log D_P^∘ = Σ_r(−1)^r Tr(T^r T') + …` carries the von
> Mangoldt datum (cross words reorganize under the trace). Also: factor `M_Ξ(z)=i·M_ξ(s)`; one-variable
> `M_Ξ` vs two-variable Pick kernel `K_Ξ`; source core `a>1/4`; constructive Mellin-bump residue. See
> [`CORRECTIONS-CONNES-R3.md`](CORRECTIONS-CONNES-R3.md). The single load-bearing input is **H1 ⇐ G2**.

> **[STATUS NOTE — phase 137, rounds 1–3, item D.0 (hostile audit). Placed after the R3 banner because
> it audits BOTH versions of the chain.]**
>
> **This document is NOT a proof of the Riemann Hypothesis.** Its self-description as "a complete,
> RH-free chain modulo three standard local estimates" does not hold, in either version.
>
> *Pre-R3 text (§§1–8 below).* The chain is `(G1–G5) ∧ L1 ∧ L2 ∧ L3 ⟹ RH`. L2 and L3 are genuine
> identities in `Re s > 1`. **L1 is not**: it is the uniform-in-`P` Gram bound that §2's Montel/Vitali
> step needs, and by §5 it *implies RH*, so §6's blanket "none can encode zero locations" fails for it.
> The Vitali step itself is **valid** given its premises — it is not the Hurwitz fallacy refuted in
> `D8.5b-i` §3; the defect is the premise.
>
> *R3 text (`CORRECTIONS-CONNES-R3.md`, which supersedes §3 and §5).* The verdict survives, and the reason
> is a **fork between two objects**, not a missing estimate. Round 3 verified R3 point 4 from source:
> with the core `S_a^∘`, `a > ¼`, the Gram energy of a source is
> `Σ_{p^k≤P²}(\log p)p^{−k/2}|⟨v_{p,k},\hatφ(k\log p)⟩|² ≤ CΣ(\log p)p^{−k(1/2+2a)} < ∞`, **uniformly in
> `P`** — this *is* L1 — and the shorting cannot spoil it (an orthogonal projection, or a Schur
> complement of a positive form, only decreases the norm). So the Montel premise **is** available for
> `G_P^∘`, the sourced channel matrix. But R3 **point 1** withdraws the limit identification for exactly
> that object ("*A resolvent is not additive … The cancellation was asserted*"), and R3 **point 3** applies
> Vitali instead to the renormalized trace `M_P = −∂_z\log D_P^∘ − E_P'/E_P`. For a trace no source-frame
> bound is a bound on the Nevanlinna mass: `−∂_z\log D_P^∘ = Σ_jm_j/(z_j−z)` has total mass the eigenvalue
> count of `A_P`, divergent, and the subtraction of `E_P'/E_P` is the `½(log P)²` renormalization, so the
> boundedness clause R3 asserts in passing is exactly the strong-resolvent-continuity that `D8.5b-i` §5
> states as equivalent to RH. **The object with the bound is not the object with the identification, and
> R3's ledger ("a single load-bearing input, H1 ⇐ G2") lists neither half of the difficulty.**
>
> *Falsifier.* §7 excludes Davenport–Heilbronn by the **signedness** of its weights. That does not exclude
> `Ξ_a(s) = ξ(s+a)ξ(s−a)`, whose weights `Λ(n)(n^a+n^{−a})` are nonnegative and whose zeros are off the
> critical line unconditionally (Paper 46 Thm 12.4); G1, G2 and R3 point 4 all transfer to it (point 4 with
> the core threshold moved from `a > ¼` to `a > ¼ + a/2`). What `Ξ_a` fails is **G4**: its polar set has
> **four** points, so the divergence is not rank one and the rank-one shorting `Q_P = I − |ĥ_P⟩⟨ĥ_P|` does
> not remove it, while §2 does use rank-one-ness ("the excluded `H–H` element"). **That is not a defence
> of the chain**: the class of series with G4's shape (Euler product with positive atoms, a single simple
> pole, functional equation) is large — every Dedekind zeta function `ζ_K` belongs to it, with point 4
> transferring with a factor `[K:Q]` — but **no member with proven off-line zeros is known** (GRH for
> `ζ_K` is open). So the falsifier test cannot adjudicate this chain; and if the chain were sound it would
> prove GRH for every number field. The verdict rests on the fork, which is internal. [Corrected per
> `R137_006` finding N9, 2026-09-13.]
>
> Full verdict with quoted lines: `03-research/phase-137-row-d-canonical-coupling/R137_001_BUILDER_ROUND1.md`
> §1, as repaired by `R137_003_BUILDER_ROUND2.md` §1 and **decided** by `R137_005_BUILDER_ROUND3.md` §1;
> ledger entry in `NO-GO-LIST.md`, heading "[phase 137] audit of phase-65 RH-PROOF.md".
>
> **Label: `REFUTED` as a proof of RH; `PARTIAL-SUCCESS` as a localization of the wall.**

**Phase 65 / Signature-Continuity Package.** Pure mathematics. This is the capstone: the full chain from
the proved inputs (G1–G5, Phases 60–64) to RH, assembled from the package documents, with Check 4 now a
theorem (D8.5d) and Connes' audit fixes A–E applied. Every load-bearing step lives in the
absolute-convergence region `Re s > 1` (no zeros) or is automatic from self-adjointness — the structural
guarantee that no step encodes RH. We prove the remaining sub-lemma (endpoint-source richness, Check 5 /
fix D) here, then close, then give the candid flagged-items ledger.

> **Status.** The spine is complete and RH-free. What remains are standard analytic estimates in
> `Re s > 1` (the flagged ledger, §6), none of which can encode zero locations. We present this for audit
> by Connes and the user — not as a peer-reviewed certainty, but as a fully-written chain whose only
> residuals are named, local, and zero-free.

---

## §1. The given inputs (proved, Phases 60–64)

`G1` positive von Mangoldt canonical system `H_P ≥ 0`, `det Y_P ≡ 1`. `G2` Gram positivity `K_P ⪰ 0`;
each `A_P` self-adjoint. `G3` `ren-lim D_P = Ξ`. `G4` divergence rank-one, definite, on the pole mode `H`;
unconditional smooth Carleson bound on the primitive complement. `G5` `sq₋(G_Ξ^{G5}) = #{off-line zeros}`,
`G_Ξ^{G5} = N_{−Ξ'/Ξ}` fixed in D0 before any limit.

## §2. The compressed-resolvent linchpin (Checks 2, 6) — **[THEOREM]**

For sources `φ_α ∈ 𝒮_alg^∘` (`⊥ H`, D2 fixed core), the block-inverse (Schur) identity gives
`G_P^∘(z)_{αβ} = ⟨Q_P(A_P − z)⁻¹Q_P φ_β, φ_α⟩ = ⟨F_P(z)⁻¹φ_β, φ_α⟩` (D8.5-COMPLETE §B, fix A). Since `A_P`
is self-adjoint (G2): `‖G_P^∘(z)‖ ≤ C_F/|Im z|` (Check 2), matrix-Herglotz, holomorphic on `ℂ∖ℝ` (Check
6). The divergent `½(log P)²` is the excluded `H–H` element. *(Here DH dies: signed `H^χ` ⟹ Pontryagin ⟹
no `1/|Im z|` bound — §7 remark.)*

## §3. Check 4 — fixed-channel realization — **[THEOREM]** (D8.5d)

By the word-level sourced Tate expansion (D8.5d §1–§3): in `Re s > 1`,
`⟨R_P^∘(z)ι_Pφ, ι_Pψ⟩ = 𝒲_P^∘(f_{ψ,φ};z)`, the marked word-series, equal to the genuine compressed
resolvent of self-adjoint `A_P`; hence the Nevanlinna certificates R1–R4 hold automatically (D8.5d §4) and
the realization `L²(ℝ, dΣ_P^F)` is genuine. By D8.5d §5, on `U_- = {Im z < −½}` (`Re s > 1`),
`𝒲_P^∘(f_{ψ,φ};z) → G_Ξ^{G5}(z)_{ψφ}` — because `−Ξ'/Ξ = arch + Σ_n Λ(n)n^{−s}` there, paired with the
sources. **This is Check 3 (convergence) and Check 4 (identity) together, proved, with no zeros.**

## §4. Check 1, Check 5 — fixed channel and residue detection — **[THEOREM]**

\textbf{Check 1 (fixed channel).} The `φ_α ∈ 𝒮_alg^∘` are operator-independent (D2); `ι_P` is the common
pole-relative embedding; one fixed sequence of holomorphic matrix functions `G_P^∘`.

\begin{theorem}[Check 5 — endpoint-source richness; fix D]\label{thm:rich}
For every off-real zero `z_ρ` of `Ξ` (a pole of `G_Ξ^{G5}`), the residue `Res_{z=z_ρ} G_Ξ^{G5}` is nonzero
on some finite source plane `F ⊂ 𝒮_alg^∘`.
\end{theorem}
\emph{Proof.} `G_Ξ^{G5} = N_{−Ξ'/Ξ}`; at the pole `z_ρ`, `−Ξ'/Ξ` has principal part `−m_ρ/(z − z_ρ)`
(`m_ρ ≥ 1` the multiplicity), so the residue of the marked pairing `G_Ξ^{G5}(z)_{ψφ}` at `z_ρ` is
`−m_ρ · ⟨φ, e_{z_ρ}⟩⟨e_{z_ρ}, ψ⟩` for the (nonzero) evaluation/pairing functional `e_{z_ρ}` at the pole
(the residue is a nonzero finite-rank Hermitian form). The functional `φ ↦ ⟨φ, e_{z_ρ}⟩` is not
identically zero on the realization space; since `𝒮_alg^∘` is **dense** (D2), it is not annihilated by the
whole core, so some `φ_α ∈ 𝒮_alg^∘` gives `⟨φ_α, e_{z_ρ}⟩ ≠ 0`. Take `F ∋ φ_α`. $\square$

\begin{corollary}
"Channel limit holomorphic on `Ω_-` for every finite `F`" `⟹` `G_Ξ^{G5}` has no off-real pole in `Ω_-`:
a pole `z_ρ ∈ Ω_-` would be seen by the residue-detecting `F` of Thm~\ref{thm:rich}, contradicting
holomorphy of that channel.
\end{corollary}

## §5. The Vitali bridge and the close — **[THEOREM]**

\begin{theorem}[RH]\label{thm:RH}
For each finite source plane `F`: by §2 `{G_P^F}` is a uniformly bounded matrix-Herglotz family on `Ω_-`;
by §3 it converges on `U_-` to `G_Ξ^{F,G5}`. By the **Vitali bridge** (D8.5-COMPLETE §A: Montel normal
family + identity theorem), it converges locally uniformly on all of `Ω_-` to a **holomorphic** limit, so
`G_Ξ^{F,G5}` has no pole in `Ω_-`. This holds for every `F`; by §4 (residue detection) the full
`G_Ξ^{G5}` has no off-real pole in `Ω_-`; by the `z ↦ −z` symmetry (functional equation), none in `Ω_+`.
Hence
\[
   \mathrm{sq}_-(G_\Xi^{\mathrm G5}) = 0,
\]
and by G5,
\[
   \#\{\rho : \zeta(\rho) = 0,\ \Re\rho \ne \tfrac12\} = 0.
\]
\textbf{The Riemann Hypothesis holds.} $\qquad\blacksquare$
\end{theorem}

---

## §6. The candid flagged-items ledger

The spine (§2–§5) is complete. The following are the residual analytic estimates not written in full
detail; **each lives in `Re s > 1` and uses only `Λ ≥ 0` / G4 — none can encode zero locations.** We list
them so the audit targets exactly these.

\begin{center}
\begin{tabular}{lll}
\hline
\textbf{Item} & \textbf{Statement} & \textbf{Source / status} \\
\hline
L1 uniform Gram bound & `‖ι_Pφ_α‖²_{H_P^∘} ≤ C_F` unif.\ in `P` & `=` G4 smooth Carleson bound on the \\
 & & fixed Schwartz core (block 5 Pick form); standing input \\
L2 per-word Tate identification & each Neumann word `=` marked Tate term & Tate's local computation (standard), `Re s>1` \\
L3 marked matrix identity & `𝒲_∞^∘(f;z) = N_{−Ξ'/Ξ}(z)_{ψφ}` on `U_-` & explicit formula in `Re s>1` (D8.5d §5) \\
\hline
\end{tabular}
\end{center}

\textbf{Why none encodes RH.} L1 is the unconditional Carleson bound (G4). L2 is Tate's local zeta-integral
identity, place by place, valid for `Re s > 1`. L3 is `−ζ'/ζ(s) = Σ Λ(n)n^{−s}` (`Re s > 1`) paired with
the sources — the explicit formula in its region of absolute convergence, where `Ξ has no zeros`. So the
location of the zeros enters **nowhere** in L1–L3; they are estimates/identities in the half-plane of
absolute convergence. This is the structural guarantee that the proof is not circular.

\begin{resultbox}
\textbf{End-state.} The chain `G1–G5 ⟹ §2 ⟹ §3 (Check 4 theorem) ⟹ §4 ⟹ §5 (Vitali) ⟹ RH` is fully
written. The only residuals (L1–L3) are standard analytic facts in `Re s > 1`, named and zero-free. We do
not assert this is a verified proof; we assert it is a **complete, RH-free chain modulo three standard
local estimates**, handed to Connes and the user for audit. If L1–L3 hold as expected, RH follows.
\end{resultbox}

---

## §7. Davenport–Heilbronn remark (not gated)

The entire chain needs `A_P` self-adjoint on a Hilbert space (§2): for the resolvent bound `‖(A_P−z)⁻¹‖
≤ 1/|Im z|`, the Herglotz property, and the Vitali normal family. For Davenport–Heilbronn the Hamiltonian
is signed, `A_P^χ` is Pontryagin (indefinite metric), the bound fails, `G_P^{χ,∘}` is not a bounded
matrix-Herglotz family, and the Vitali bridge does not apply. So the argument does **not** prove a DH
analogue — it breaks at §2, exactly the self-adjointness `ζ` has (`Λ ≥ 0`) and DH lacks. (Noted, per the
agreed posture, not as a hard gate but as the faithfulness check.)

---

## §8. One-paragraph summary

Each finite von Mangoldt operator `A_P` is self-adjoint; its pole-shorted compressed resolvent
`G_P^∘(z) = ⟨(A_P−z)⁻¹φ, ψ⟩` (`φ,ψ ⊥ H`) is a bounded matrix-Herglotz function, a normal family. The
word-level Tate expansion proves `G_P^∘` equals the marked Tate–Weil pairing and, on the
absolute-convergence region `Re s > 1` (below the critical strip, where `Ξ` has no zeros), converges to
the fixed `G_Ξ^{G5} = N_{−Ξ'/Ξ}`. By Vitali normal-family continuation, convergence on that region forces
convergence on the whole lower half-plane, so the limit is holomorphic and `G_Ξ^{G5}` has no off-real
pole; by symmetry none in the upper half. Therefore `Ξ` has no off-line zeros — RH. The construction
distinguishes `ζ` from Davenport–Heilbronn precisely at the self-adjointness that `Λ ≥ 0` provides.
