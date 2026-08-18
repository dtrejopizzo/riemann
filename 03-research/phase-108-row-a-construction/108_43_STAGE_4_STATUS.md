# 108.43 — Stage 4 status: the geometry, closed with a negative result

## 0. Verdict table

| Item | Ask | Outcome | Where |
|---|---|---|---|
| G1 | Explicit archimedean space + explicit symmetric form, built from $\Theta/\Gamma_\R$ only | **Constructed, but stipulated.** $W_\infty=A\oplus A^-\oplus B\oplus B^*$ and $B_\infty$ are fully written down; the Gram entries are hand-specified, not derived | 108_41 §3 |
| G2 | Polar page as a proved isomorphism of forms, or a proved non-isomorphism | **Not proved.** The matching is **by construction**: $B_\infty$ is *defined* to make $\{b_0,b_0^*\}$ hyperbolic, so "the Gram matrices coincide" is a normalization, not a theorem | 108_41 §4, Prop. 4.1 |
| G3 | Full inertia of $B_\infty$, blockwise | **Proved.** $n_+=n_-=\aleph_0$ unconditionally; $\mathrm{rad}\,B_\infty=\{0\}$. Content: the archimedean form has **no arithmetic invariant** | 108_42 §2, Thm 2.1 |
| G4 | Recover $\pi\cot(\pi a/2)$ from $B_\infty$ on explicit vectors, or prove it cannot | **Not proved as geometry.** Reduces to the Mittag-Leffler expansion of $\cot$; the vector $U$ was reverse-engineered from the target. Retracted in full | 108_42 §3.4, Thm 3.6 |
| **NEW** | — | **Proved: the embedding no-go.** If RH holds, there is no isometric injection $(W_\infty,B_\infty)\hookrightarrow(V,\overline I_\partial)$ | 108_42 §4, Thm 4.3 / Cor. 4.4 |

> **Stage 4 geometry is closed — with a negative result on two of the four
> original deliverables, one genuine proved theorem (G3), and one genuine new
> structural theorem (the embedding no-go) that was not among the original
> deliverables and is the most useful thing the stage produced.**

This is not "all four closed positively." An earlier draft of this note said
so; that is corrected here.

## 1. Why G2 and G4 do not count

Both failed the same way, and it is worth naming the failure mode because it
is cheap to repeat.

**G2.** Proposition 4.1's content is: $B_\infty(b_0,b_0)=0$,
$B_\infty(b_0,b_0^*)=1$ *by Definition 3.2*. The form was defined to be the
hyperbolic plane and is then observed to be the hyperbolic plane. The residue
computation of 108_41 §2 (Corollary 2.2) establishes only that the residues
$r_n=-1$, $r_n^*=+1$ are **constant in $n$**; it supplies no derivation of the
isotropy $B_\infty(b_n,b_n)=0$, which is the entire content of "hyperbolic."

**G4.** Theorem 3.6 is true, and its proof is correct, but it produces no
information. As 108_42 §3.4 sets out: for *any* bounded coefficient sequence
$(c_n)$ the same construction yields an arbitrary meromorphic function with
simple poles on $2\Z$ and residues $2c_n$. Choosing $U$ to be all-ones is
precisely the choice making the residues constant, which is precisely what
reproduces $\cot$. And the resulting identity — that $\cot$ has poles on $2\Z$
with constant residue — is 108_40 Proposition 6.1, i.e. the **input**, since
$\mathrm{spec}\,\Theta$ was read off $\Gamma_\R$'s poles in the first
place. Nothing came out that did not go in.

**A structural symptom, recorded.** G2 lives on $B\oplus B^*$ and G4 on
$A\oplus A^-$, and 108_41 §3 proves these sectors are *forced apart*: $b_0$
must be isotropic for G2 while $a_0$ must be non-isotropic for G4, and no
single scalar $B(e_0,e_0)$ is both $0$ and $2$. So $W_\infty$ is not one
geometric object; it is two unrelated constructions in a direct sum, each
built to hit one target. That is a further reason not to read either as
geometry.

## 2. What Stage 4 did establish

**G3, and its meaning.** $n_+(B_\infty)=n_-(B_\infty)=\aleph_0$, computed
blockwise and unconditionally, with $\mathrm{rad}\,B_\infty=\{0\}$. The
point is the *unconditionality*: 107_241 Corollary 3.3 makes
$n_+(\overline I_\partial)=1$ equivalent to RH, so on the Stage-0 side the
size of $n_+$ is exactly where the arithmetic lives. On the archimedean side
there is no such quantity to measure — $n_+$ is forced to $\aleph_0$ by the
mere existence of infinitely many eigenvectors $a_n$, with no arithmetic
input anywhere. This is the geometric face of the fact that $\Phi$ is
prime-free (108_91 Corollary 1.4).

**The embedding no-go (108_42 §4).** From Theorem 2.1 together with 107_241
Theorem 3.1:

> If there is an isometric injection $(W_\infty,B_\infty)\to
> (V,\overline I_\partial)$, then $n_+(\overline I_\partial)\ge
> n_+(B_\infty)=\aleph_0$, hence $\#P=\infty$: infinitely many off-line
> zeros of $\xi$. Contrapositively, **if RH holds no such injection exists.**

This is a structural incompatibility, **not** a proof of RH or of its
negation, and 108_42 §4 says so explicitly and prominently.

Its value is that it constrains Stage 6. The archimedean form is *too
positive* to sit inside the corner form. If the archimedean fibre is to
appear in Stage 0's geometry at all, it cannot enter as a **sub-object**; it
must enter as a quotient, an orthogonal complement, or with the opposite
sign. Stage 6 should be set up accordingly.

## 3. What remains open

Everything at the algebro-geometric level, exactly as 108_40 §7 flagged and
unchanged by this pair of notes. Neither note constructs:

* an algebraic variety, scheme, or motive of which $W_\infty$ is a
  cohomology group;
* a correspondence (a "Frobenius at infinity" in the Serre/Deninger sense)
  realizing $\Theta$, $\Theta^-$ or $\Theta^*$ as an endomorphism of an
  actual geometric object;
* an intersection pairing arising from algebraic cycles, as opposed to a
  bilinear form given by a hand-specified Gram matrix.

Given §1, the candid statement is that Stage 4 did **not** narrow the gap
between "operator with a determinant" and "correspondence with an
intersection pairing." What it did instead was prove (G3, no-go) that the
purely archimedean object cannot carry the invariant the programme needs,
which is a different and more useful kind of progress: it removes a route
rather than advancing along it.

## 4. Verifier status

All three verifiers run to completion; each prints per-check PASS/FAIL and
exits 0 only if every check passed.

| File | Result | Exit code |
|---|---|---|
| `108_41_stage_4_the_archimedean_intersection_form.py` | `VERDICT: ALL CHECKS PASS` | 0 |
| `108_42_stage_4_signature_and_the_local_term.py` | `VERDICT: ALL CHECKS PASS` | 0 |
| `108_43_stage_4_status.py` | `VERDICT: ALL CHECKS PASS` | 0 |

`108_43_stage_4_status.py` does not re-derive G1–G4; it re-runs the two prior
verifiers as subprocesses from a fresh interpreter, and separately checks the
closed form for $\Phi$ against its anchor values
$\Phi(1/2)=-2.2305907656358723438$ and the root
$0.30169238816042209152$ at 45-digit precision.

Note that a passing verifier does **not** upgrade G2 or G4. Both are
arithmetically correct statements whose *content* is the problem, and no
numerical check can detect that; the defect was found by unwinding the
definitions, not by running code. This is recorded as a limitation of the
verification discipline used throughout this phase.

## 5. Scope

**Proved across 108_41–108_42.** Lemma 1.2 and Corollary 2.2 (pole/residue
data of the two mirrors of $\Gamma_\R$); Proposition 1.1 (bounded, boundedly
invertible Gram operator; nondegeneracy); Theorem 2.1 (G3, exact inertia);
Lemma 3.2, 3.4 and Theorem 3.6 (the $\cot$ identity — correct, but see §1);
Lemma 4.2, Theorem 4.3 and Corollary 4.4 (the embedding no-go).

**Constructed but not derived.** Definitions 3.1–3.2 of $W_\infty$ and
$B_\infty$; Proposition 4.1's matching (§1).

**Read from source, not re-derived.** 108_39 Theorem 1.1 / Corollary 1.2;
108_40 Definition 1.1 and Proposition 6.1; 107_241 Lemma 2.2, Theorem 3.1 and
Corollary 3.3; the classical Mittag-Leffler expansion of $\cot$; the closed
form for $\Phi$ and its anchor values (proved in 108_91, verified against
here).

**Not established, and explicitly not claimed.** Any algebro-geometric
realization of $W_\infty$ or $\Theta$ (§3); G2 and G4 as theorems (§1); any
isomorphism of the whole forms $(V,\overline I_\partial)$ and
$(W_\infty,B_\infty)$ — disproved unconditionally at the level of inertia,
and disproved under RH at the level of embeddings (§2); anything about $\RH$.
No zero of $\zeta$ or $\xi$, no Li coefficient, and no positive part of a
Weil-type form enters any definition in 108_41 or 108_42.

`ROW_A_STATUS` is unchanged. Nothing here bears on $\RH$.

## 6. Verifier

`108_43_stage_4_status.py` re-runs the two prior verifiers as subprocesses,
checking both exit 0 and both print `VERDICT: ALL CHECKS PASS`; and checks
the closed form for $\Phi$ against its two supplied 20-digit anchor values at
45-digit working precision using `mpmath`. All checks print PASS/FAIL
individually; the script exits 0 with `VERDICT: ALL CHECKS PASS` only if
every check passes.
