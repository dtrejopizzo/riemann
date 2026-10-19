# CA_A_001 — Candidate (b): positivity from Petersson / Maass–Selberg / Rankin–Selberg on PSL₂(ℤ)\ℍ

Phase 193. Pen and paper; no numerics.

## 0. Corpus / index check
- ROUTES-TRIED-INDEX: R9-15 (Hecke commutes with L; no sign content, LITERATURE-ONLY); G4D-R152_002 / 159 G1 K3
  ("Hecke self-adjoint on L²(Γ\𝔥) excluded", DEAD [no form/K3]); G6B-R162_502 A (Hecke, DEAD [equivariance]);
  G4C-R160_S5 §5#10 (Hecke-type coupled square, OPEN-RESIDUE, none built).
- phase-16-surf-witness-variety `04-MSZ-pairing-hits-CAP.md`, `05-resonance-pairing-definite-THEOREM.md`: the Maass–Selberg pairing of
  Eisenstein *residues* (zero side) is definite for every zero configuration (proved there) — zero-side, [zeros].
- New here: the *norm* side (truncated Eisenstein norm, Rankin–Selberg against positive Eisenstein weights) tested as a
  carrier for 𝔞_T on P_T. Not on record as such.

## 1. Data
E(z,s)=Σ_{Γ∞\Γ} Im(γz)^s, constant term y^s+φ(s)y^{1−s}, φ(s)=ξ(2s−1)/ξ(2s), ξ(s)=π^{−s/2}Γ(s/2)ζ(s) (CITED).
Fourier coefficients 2|n|^{1/2}σ_{2s−1}(|n|)|n|^{½−s}K_{s−½}(2π|n|y)/ξ(2s) (CITED). Hecke: T_nE=n^{s−½}σ_{1−2s}(n)E.

## 2. The line-doubling lemma (PROVED)
**Lemma 1.** In every coefficient of E(·,s) (constant term, Fourier coefficients, Hecke eigenvalues) ζ enters only
through ζ(2s), ζ(2s−1) and the divisor sums σ_{2s−1}. On the unitary axis s=½+iτ this is ζ(1±2iτ); ζ(½+iτ′) is reached
only at Re s=¼.
*Proof.* Read off §1. ∎

**Lemma 2 (no invariant positive form at Re s=¼; PROVED from CITED Bargmann).** For s=¼+it, t≠0, the principal-series
(𝔤,K)-module of PSL₂(ℝ) with Casimir eigenvalue s(1−s) carries no nonzero invariant positive semidefinite Hermitian form.
*Proof.* An invariant positive form makes the Casimir symmetric on the pre-Hilbert quotient, so s(1−s) is real on any
nonzero quotient vector. With s=a+it, s(1−s)=a−a²+t²+it(1−2a), so Im s(1−s)=t/2≠0 at a=¼. The module is irreducible for s∉½+ℤ (Bargmann, CITED), so the quotient is all of it. ∎

**Corollary 3 (NO-GO for the norm class, PROVED).** Every positivity produced by a Hilbert-space norm on
L²(Γ\ℍ) applied to Eisenstein data (Maass–Selberg ‖Λ^YE(·,½+iτ)‖² ≥ 0, Parseval on horocycles, Petersson norms of
spectral projections) is a statement in which ζ appears at abscissa 1 (ζ(1+2iτ), ζ′/ζ(1+2iτ)) or in absolute
convergence. Concretely Maass–Selberg gives, for real τ,
  2log Y − (φ′/φ)(½+iτ) + Re[φ(½−iτ)Y^{2iτ}/(iτ)] ≥ 0,  −(φ′/φ)(½+iτ)=4Re(ξ′/ξ)(1+2iτ) (FE),
whose comb is Σ 4Λ(n)n^{−1}cos(2τ log n): weights Λ(n)/n, not v_n=2Λ(n)/√n.

## 3. Pre-screen against (R) and thm:shape
| clause | verdict | reason |
|---|---|---|
| (1) exact Λ(n), n<e^{2T} | NO | Λ enters at abscissa 1 with weights 1/n; the window-T vector enters through ζ′/ζ(1+2iτ), a bounded functional |
| (2) Euler × FE(Γ(s/2), cond 1) jointly | nominal YES | Hecke eigen + φ satisfies FE |
| (3) non-linear | NO | MS inequality is linear in ζ′/ζ(1+2iτ) |
| (4) | YES | no zeros used |
| (5) not bounded functional | NO | Σ Λ(n)/n · (smooth) is a bounded functional at fixed Y |
| (6)/(7) fluctuation not density | NO | positivity carried by 2log Y (pole/density); PNT-strength input only |
| (8) | NO | no correlation inside P_T at frequencies up to e^{2T} |
| (10) | NO | same inequality on Bianchi / Hilbert modular groups with ξ_K (O12 survives) |
| (11) ζ-specific | NO | evaluation at CM points z_Q turns E(z_Q,s) into Epstein Z_Q(s)/ζ(2s) (CITED); every pointwise positivity in z (e.g. E(z,w)>0, w>1, used in Rankin–Selberg unfolding) holds for every Epstein ⇒ survives O10 |
Key test: survives ζ→ζ_K (O12) and Epstein (O10); Rankin–Selberg weights E(·,w)>0 only for w>1 (absolute convergence;
for w↑1 the residue 3/π dominates with sign of (w−1)^{−1}, so E(·,w)<0 somewhere for w<1 near 1: ARGUED from the Laurent
expansion, CITED constant term). Class closed under O1 in the sense of 𝒞_PNT (lem:shape-del) — excluded by thm:shape(A).

## 4. Result
**NO-GO (PROVED for the norm class as defined in Cor. 3; ARGUED for "any PSL₂(ℤ) Eisenstein positivity").** The
obstruction is *line doubling*: E(z,s)∝ξ(2s)^{−1}, so the window's line ½ for ζ sits at Re s=¼, where Lemma 2 forbids
any invariant positivity. Not a failure of identification: the obstruction is representation-theoretic.
**Escape noted (→ CA_A_003):** half-integral weight (metaplectic, Γ₀(4)) Eisenstein series have n-th coefficients with
L(2s−½,χ_n)/ζ(4s−1) (Goldfeld–Hoffstein, CITED from memory, to verify); for n=□ and s=½+it this is ζ(½+2it)
(up to finite Euler factors) — the line ½ is reached on the unitary axis.

## 5. Self-review
- Lemma 2 kills invariant forms; non-invariant positive forms (e.g. inner products after truncation) are not covered.
  Such forms are generic Hilbert norms: then the only ζ-input is the Eisenstein data of Lemma 1, still abscissa 1. OK.
- "Survives O10 via CM points" applies to pointwise-in-z positivity; integrated positivity (Maass–Selberg) does not
  specialize to a point, but it survives O12 (Bianchi). Verdict stands.
- No negative value for ζ produced. Property moved YES→NO: "Hecke/Petersson positivity carries the window comb at ½" → NO.

## Addendum (after round-1 review)
Line doubling is NOT endorsed as a barrier for all PSL₂(ℤ) positivity. Mellin transforms in y and Rankin–Selberg in w
reach ζ(½+iτ) on the unitary axis. Lemma 2 stands only for invariant Hermitian forms on the (𝔤,K)-module at Re s=¼. The
NO-GO of §4 is restricted to the norm class of Cor. 3; the "ARGUED for any PSL₂(ℤ) positivity" extension is withdrawn.
