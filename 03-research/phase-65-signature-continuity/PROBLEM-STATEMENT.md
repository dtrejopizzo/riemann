# Phase 65 — The Signature-Continuity Problem: precise statement, the object to build, and the new mathematics

**Status:** open · started 2026-06-29 · pure mathematics only (no computation) · the sole objective of
this phase is to construct one new mathematical object and prove one theorem, which together are RH.

> **Governing principle (unchanged).** A false victory is worse than failure. Every conjecture is
> labelled. Nothing here is claimed proven. The phase succeeds only if the object is genuinely
> constructed and the theorem genuinely proved; otherwise it documents exactly what was and was not
> achieved.

---

## 0. Orientation: what Phase 65 is, in one paragraph

Phases 60–64 reduced RH, through a chain of *proved, unconditional* steps, to a single irreducible
statement: the negative (Kreĭn–Langer) index of a certain explicit family of positive canonical systems
must be **continuous** through one **rank-one, definite-signed renormalization**. The ordinary tools of
spectral theory and complex analysis cannot express this continuity, because the only available bridge —
the scalar perturbation determinant — is *signature-blind*. Phase 65 builds the missing tool: a
**signature-preserving (index-graded) regularized determinant** and the **topology on generalized
Nevanlinna functions** in which it is continuous. We isolate this as new mathematics worth developing
for its own sake; RH is its first theorem.

---

## 1. The given data (all proved in Phases 60–64; inputs, not to be re-derived)

Fix the scaling parameter and write $L=2\log\lambda$. The following are established and may be used
freely.

\textbf{(G1) The positive von Mangoldt canonical system.} For each finite $P$ there is a canonical
system on $[0,\ell_P]$,
\[
   J\,\partial_t Y_P(t,z)=z\,H_P(t)\,Y_P(t,z),\qquad Y_P(0,z)=I,\qquad
   J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix},
\]
with Hamiltonian
\[
   H_P=d\mathcal H_{\mathrm{vM}}^{(P)}=\sum_{p^k\le P^2}(\log p)\,p^{-k/2}\,|v_{p,k}\rangle\langle v_{p,k}|\,
   \delta_{k\log p}\ \ge\ 0 .
\]
$H_P\ge0$ unconditionally (von Mangoldt $\Lambda\ge0$). $\det Y_P\equiv1$.

\textbf{(G2) Free positivity (canonical Gram identity).} The reproducing kernel
$K_P(z,w)=\int_0^{\ell_P}Y_P(t,w)^*H_P(t)Y_P(t,z)\,dt\ \succeq\ 0$ for all $P$
(`CANONICAL-FOUNDATION.md`, Thm). Hence each $E_P$ (the structure function of the system) is
Hermite–Biehler: $\kappa(E_P)=0$.

\textbf{(G3) Transfer to $\Xi$.} The regularized perturbation determinant satisfies
$\mathrm{ren\text{-}lim}_{P\to\infty}D_P(z)=\Xi(z)$ (`CANONICAL-FOUNDATION.md`, Stage 5; Tate local
factors $\times$ archimedean Binet cell). Here $\Xi$ is Riemann's entire function.

\textbf{(G4) The divergence is rank-one and definite.} $\Tr K_P\sim\tfrac12(\log P)^2\to\infty$, carried
\emph{entirely} by the constant/degree mode $H$ (the pole of $\zeta$ at $s=1$); on the primitive
complement $P_{\mathrm{prim}}=I-|H\rangle\langle H|/\|H\|^2$ the masses are the bounded box counts
(`FACE-C-compactness.md`). The pole has definite ($+$) sign (repulsive barrier,
`POLE-DEFECT-estimate.md`).

\textbf{(G5) Index $=$ off-line zeros.} For the limiting structure function, the Kreĭn–Langer negative
index equals the number of zeros off the critical line: $\kappa(\Xi)=\#\{\rho:\zeta(\rho)=0,\ \Re\rho\ne
\tfrac12\}$ (E108, Pontryagin/Kreĭn–Langer). RH $\Leftrightarrow\kappa(\Xi)=0$.

---

## 2. The precise gap (what is *not* available)

\textbf{(N1) Signature-blindness.} The map $A_P\mapsto D_P$ (operator to scalar determinant) does not
determine $\kappa$: there exist canonical systems with the *same* entire determinant and *different*
$\kappa$. Equivalently, $\kappa$ is not a function of $D_P$.

\textbf{(N2) Non-closedness of $\mathcal N_0$.} In the topology of locally uniform convergence, the
class $\mathcal N_0$ of Hermite–Biehler functions is *not* closed: a sequence $E_P\in\mathcal N_0$ can
converge to $E\notin\mathcal N_0$ (zeros migrating across $\mathbb R$). So "$E_P\in\mathcal N_0$ for all
$P$" does not give $E\in\mathcal N_0$.

\textbf{(N3) The renormalization is not locally uniform.} $\mathrm{ren\text{-}lim}$ divides out the
divergent rank-one factor (G4); it is not convergence in any classical topology on entire functions, so
neither Hurwitz nor (N2)-type Rouché arguments apply to it as given.

These three are the precise reasons every prior route stalls. Phase 65 must supply objects that remove
all three simultaneously.

---

## 3. The object to construct

\begin{definition*}[the index-graded regularized determinant $\widetilde D$ — TO BE CONSTRUCTED]
A functor (or assignment)
\[
   A\ \longmapsto\ \widetilde D(A)=\big(D(A),\ \kappa(A),\ \text{(grading datum)}\big)
\]
from the class $\mathcal C_{1}$ of canonical operators with a single rank-one, definite-signed trace
divergence, to a target category $\mathcal G$ (an \emph{index-graded} refinement of entire functions /
generalized Nevanlinna functions), satisfying:
\begin{itemize}
\item[\textbf{(A1)}] \textbf{Compatibility.} On finite positive systems $A_P$ (G1–G2),
$\widetilde D(A_P)$ recovers $(E_P,\,0)$: the structure function with index $0$.
\item[\textbf{(A2)}] \textbf{Signature-continuity.} $\widetilde D$ is continuous in the topology
$\tau_\kappa$ of $\mathcal G$ (Def., §4) under the rank-one renormalization $A_P\to A_\infty$; in
particular the index component is continuous: $\kappa(A_\infty)=\lim_P\kappa(A_P)$.
\item[\textbf{(A3)}] \textbf{Realization.} $\widetilde D(A_\infty)=(\Xi,\ \kappa(\Xi))$, with the
*genuine* index of $\Xi$ (G5).
\end{itemize}
\end{definition*}

\begin{definition*}[the signature topology $\tau_\kappa$ — TO BE CONSTRUCTED]
A topology on $\mathcal G$ such that
\begin{itemize}
\item[\textbf{(T1)}] $\mathcal N_0$ (index $0$) is \emph{closed} in $\tau_\kappa$;
\item[\textbf{(T2)}] the arithmetic renormalization of (G3)–(G4) \emph{converges} in $\tau_\kappa$
(i.e. $\widetilde D(A_P)\to\widetilde D(A_\infty)$ in $\tau_\kappa$).
\end{itemize}
\end{definition*}

The entire novelty lives in making (T1) and (T2) hold *simultaneously*: the ordinary topology gives (T2)
but not (T1) (N2); a topology fine enough to force (T1) classically destroys (T2) (N3). The construction
must use the structural specifics of (G4): the divergence is **rank-one**, **definite-signed**, and
**arithmetically explicit**, so $\tau_\kappa$ may be a *pole-relative* topology that quotients by the
one divergent mode while retaining the index of the primitive complement.

---

## 4. The theorem to prove

\begin{theorem*}[Signature-Continuity Theorem $=$ RH — TO BE PROVED]
The object $\widetilde D$ and topology $\tau_\kappa$ of §3 exist and satisfy (A1)–(A3), (T1)–(T2).
Consequently
\[
   \kappa(\Xi)\ \overset{(A3)}{=}\ \kappa(A_\infty)\ \overset{(A2)}{=}\ \lim_{P}\kappa(A_P)
   \ \overset{(A1)}{=}\ \lim_P 0\ =\ 0,
\]
and therefore, by (G5), \textbf{the Riemann Hypothesis holds}.
\end{theorem*}

The logical structure is deliberately rigid: once the object and topology are built with (A1)–(A2)–(T1),
RH is a one-line corollary. \emph{All the mathematics is in the construction, none in the deduction.}
This is why Phase 65 is a *construction* phase, not an *estimation* phase — and why no computation can
contribute: there is nothing to estimate, only an object to define and its continuity to prove.

---

## 5. The construction program (sub-problems, pure-math milestones)

A proposed decomposition of the construction into provable milestones. Each is a self-contained
pure-mathematics task; order is logical, not strict.

\textbf{M1 — The index-graded category $\mathcal G$.} Define entire (or meromorphic) functions
\emph{graded by} a Kreĭn–Langer index, with morphisms that track index. Likely substrate: generalized
Nevanlinna classes $\mathcal N_{\le\kappa}$ with the de Branges–Pontryagin space $\Pi_\kappa$ attached.
Deliverable: a category in which $(E_P,0)$ and $(\Xi,\kappa)$ are objects and the renormalization is a
morphism-limit.

\textbf{M2 — The pole-relative completion.} Construct the Hilbert/Pontryagin completion of the primitive
domain in which the single rank-one definite divergence (G4) is quotiented but the index of the
complement is retained. Deliverable: a metric/uniformity making the renormalization (G3) a genuine
limit (T2) — the analytic heart.

\textbf{M3 — Closedness of $\mathcal N_0$ (T1).} Prove that, in $\tau_\kappa$, a limit of index-$0$
objects has index $0$. This is where the **definite sign** of the pole must enter: a definite-signed
rank-one perturbation cannot create a negative square (it can only add a positive one), so the index
cannot increase across it. Deliverable: the signature-monotonicity/closedness lemma — the conceptual
heart.

\textbf{M4 — Compatibility and realization (A1, A3).} Identify $\widetilde D(A_P)=E_P$ on finite systems
and $\widetilde D(A_\infty)=\Xi$ in the limit, with genuine indices. Uses (G2), (G3), (G5). Deliverable:
the two endpoints pinned to the known data.

\textbf{M5 — Assembly.} (A1)+(A2 via M2)+(T1 via M3) $\Rightarrow\kappa(\Xi)=0\Rightarrow$ RH.

\emph{The decisive milestone is M3:} it is the precise place where "the divergence is definite-signed"
(a fact we have, G4) becomes "the index cannot jump" (the thing we need). M2 makes M3 expressible; M1
gives the language; M4 ties to $\zeta$.

---

## 6. Falsification / honesty hooks (so the phase cannot self-deceive)

- If M3 \emph{fails} — if a definite-signed rank-one renormalization *can* raise the index in the
  required setting — then the construction is impossible *as posed*, an off-line zero is consistent with
  all (G1)–(G4), and we must document this as a no-go and report exactly which axiom is unattainable.
- The **Davenport–Heilbronn** control must survive: the analogous construction with the *signed* DH
  Hamiltonian must \emph{fail} M1–M3 (its finite systems are not index-$0$; $\kappa$ jumps). Any
  $\widetilde D$ that "proves RH" but does not distinguish DH is wrong by construction — a built-in
  falsifier.
- No step may use the conclusion: M3 must not assume $\kappa(\Xi)=0$, M2 must not assume locally-uniform
  convergence of $E_P$ to $\Xi$ (only the renormalized determinant, G3).

---

## 7. Why this is new mathematics (and likely foundational)

The object asked for does not exist in current mathematics:
\begin{itemize}
\item \textbf{Determinants are signature-blind.} Fredholm/perturbation/$\zeta$-regularized determinants
are scalar; none carries a Kreĭn–Langer index functorially. An \emph{index-graded determinant} would be
a new invariant — a determinant valued in a category that remembers negative squares.
\item \textbf{Generalized Nevanlinna theory has no renormalization-stable topology.} $\mathcal N_\kappa$
(Kreĭn–Langer, Pontryagin spaces) is classical, but a topology in which the index is continuous under a
\emph{divergent} (renormalized) limit is not part of the theory. Building it would extend
Pontryagin-space spectral theory to renormalized limits — relevant well beyond $\zeta$ (any operator
family with a rank-one definite divergence: random matrices at criticality, QFT with one divergent mode,
inverse spectral problems with growing trace).
\item \textbf{Signature-continuity as a principle.} The lemma "a definite-signed rank-one renormalization
preserves the index" (M3), if proved in the right generality, is a new \emph{rigidity principle} sitting
between Pontryagin-space perturbation theory, de Branges spaces, and renormalization. It is the kind of
statement that, once isolated, tends to recur.
\end{itemize}

\textbf{Working name for the field:} \emph{index-graded (signed) spectral determinants and their
renormalization} — the study of regularized determinants that retain Kreĭn–Langer signature data through
divergent limits, with RH as the motivating first theorem.

---

## 8. The single sentence to pin on the wall

\begin{quote}
\textbf{Build an index-graded regularized determinant $\widetilde D$ and a topology $\tau_\kappa$ in
which (i) the Hermite–Biehler class is closed and (ii) the rank-one definite-signed pole renormalization
of the positive von Mangoldt canonical system converges; prove the index is continuous there. That
continuity is the Riemann Hypothesis.}
\end{quote}

Next document in this phase: `M1-index-graded-category.md` (begin the construction at the language
level), unless a milestone reordering is chosen.
