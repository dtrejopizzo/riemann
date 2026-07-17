# Briefing for A. Connes — the Signature-Continuity Package, and the one open point

> **⚠ UPDATED after Connes' round-2 reply (`CORRECTIONS-CONNES-R2.md`).** The open point is **not**
> D8.5b-ii. By the interior no-emergence lemma (Cauchy), and because the finite Green matrices are
> **bounded resolvents** (`‖G_P^∘(z)‖ ≤ ‖φ‖‖ψ‖/|Im z|`, a normal family), an off-real pole *cannot*
> emerge from a locally-uniform limit — so D8.5b-ii is **trivial**, and Part III below is **wrong**
> (withdrawn). **The real wall is D8.5b-i / the reach of D8.5a:** the marked sum converges only for
> `Im z < −½` (below the critical strip, where Ξ has no zeros); extending the resolvent convergence
> *across the strip* into `ℂ⁺` is the analytic continuation, valid **iff the limit operator `A_∞^∘` is
> essentially self-adjoint iff RH** (Hilbert–Pólya in resolvent-convergence form). The genuine ask is
> Connes' #4: **build the pole-relative self-adjoint completion.** Parts I–II below stand; Parts III–IV
> are superseded by `CORRECTIONS-CONNES-R2.md`.

**Phase 65. Pure mathematics. Nothing committed.** This is a self-contained statement of where the
Witt–Nevanlinna sourced-determinant package stands: everything from D0 to D12 is proved **except one
point, D8.5b-ii**, which is equivalent to RH and is the precise place where new mathematics is needed. We
give the full chain, state the open point as a clean problem, prove why every standard tool fails on it,
and ask explicitly how to prove it. It is **not** impossible — it is sharply localized — but it requires
constructing something new.

---

## Part I. What is proved (D0–D12), in one page

The package realizes RH as a **signature-continuity** statement for a family of positive canonical
systems, via sourced determinants and Feshbach shorting. All of the following are proved
\emph{unconditionally} (three flagged routine technical facts aside), with no use of RH or zero locations.

| # | result | status |
|---|---|---|
| **D0** | Fix the endpoint kernel $\mathsf K_\Xi^{\mathrm G5}=\mathsf N_{M_\Xi}$, $M_\Xi=-\Xi'/\Xi$ (Herglotz), **before any limit**; $\operatorname{sq}_-(\mathsf K_\Xi^{\mathrm G5})=\#\{$off-line zeros$\}$ | proved |
| **D1** | HB / Schur / Nevanlinna / Pontryagin charts give one index $\kappa$ and one Kreĭn–Langer divisor $\mathfrak b$; $\mathfrak b_\Xi=1\Leftrightarrow$ RH | proved |
| **D2** | **Sourced determinant** $\mathcal D_A^{\mathrm{src}}(V)=\det_{\mathrm{reg}}(I+A+V)$; its source Hessian recovers the Kreĭn–Langer kernel ⟹ **defeats signature-blindness (N1)** | proved |
| **D3** | The index-graded category $\mathcal G$; index is a **functor**; Witt principle (a positive pole is a positive line: $\kappa=0$ despite divergent scalar norm) | proved |
| **D4** | **Feshbach/Schur shorting** of the one positive divergent pole (\emph{not} subtraction — subtraction makes a spurious negative square); $D_P=\Delta_P\,D_P^\circ$ | proved |
| **D5** | The signature topology $\tau_\kappa$; source-germ convergence ⟹ kernel convergence | proved |
| **D6** | **Closedness:** a limit of positive shorted kernels is positive ($\operatorname{sq}_-=0$ closed) — clean Schur positivity, no RH, no norm bound | proved |
| **D7** | The finite von Mangoldt systems are positive: $\kappa(A_P)=0$, $\mathfrak b_P=1$, from $\Lambda\ge0$ | proved |
| **D8.5a** | **Marked Tate–Binet convergence:** the Feshbach-shorted primitive Green matrices converge, $G_P^\circ(z)\to G^{\lim}(z)$, via the marked local Tate identity, primitive pole cancellation, the **primitive marked tail estimate** (G4 + Schur–Cauchy–Schwarz, $\Lambda\ge0$), the source-level Binet identity, additive assembly | proved, **genuinely local** |
| **D8.5b-i** | **Identification:** $G^{\lim}=G_\Xi^{\mathrm G5}$ **as meromorphic objects** (both equal the marked global Tate–Weil distribution $=\mathsf N_{-\Xi'/\Xi}$) — the limit is the genuine $\Xi$-resolvent | proved |
| **D10** | **Davenport–Heilbronn falsifier fires:** the signed Hamiltonian gives $\kappa(A_P^\chi)>0$ at finite $P$, so DH never enters $\mathcal G_0$ (dies at D7); the construction distinguishes $\zeta$ from DH | proved |
| **D11/D12** | Assembly + audit: five forbidden inferences avoided; single point of failure isolated | proved |

The logical chain to RH:
$$
\underbrace{\kappa(A_P)=0}_{\text{D7}}\xrightarrow{\text{D4}}\operatorname{sq}_-(\mathsf K_P^\circ)=0
\xrightarrow{\text{D8.5a}}G_P^\circ\to G^{\lim}\xrightarrow{\text{D8.5b-i}}G^{\lim}=G_\Xi^{\mathrm G5}
\xrightarrow{\textbf{D8.5b-ii}}\operatorname{sq}_-(G_\Xi^{\mathrm G5})=0\xrightarrow{\text{D0/G5}}\text{RH}.
$$
Every arrow is proved **except the last structural one, D8.5b-ii.**

---

## Part II. The one open point — D8.5b-ii — as a clean problem

\begin{problem}[D8.5b-ii]
We are given, for each finite $P$, an $m\times m$ \textbf{matrix Herglotz (Nevanlinna $\mathcal N_0$)}
function
\[
   G_P^\circ(z)=\big(\langle (A_P^\circ-z)^{-1}\phi_\beta,\phi_\alpha\rangle\big)_{\alpha\beta},
   \qquad z\in\C\setminus\R,
\]
the Feshbach-shorted primitive resolvent of the \emph{positive} von Mangoldt canonical system
$A_P^\circ$ (self-adjoint; $\Im G_P^\circ(z)\cdot\operatorname{sgn}\Im z\succeq0$; holomorphic on
$\C\setminus\R$). We are given (D8.5a + D8.5b-i) that
\[
   G_P^\circ\ \longrightarrow\ G_\Xi^{\mathrm G5}=\mathsf N_{-\Xi'/\Xi}\quad\text{\textbf{meromorphically}},
\]
i.e. uniformly on compacta of $\C\setminus\R$ \emph{avoiding} a discrete limit divisor, where
$G_\Xi^{\mathrm G5}\in\mathcal N_\kappa$ has exactly $\kappa$ poles in $\C\setminus\R$ — at the off-line
zeros of $\Xi$ — carrying its $\kappa$ negative squares.

\textbf{To prove:} $\kappa=0$ — the limit has no poles in $\C\setminus\R$ (its divisor is real). By D0,
this is exactly RH.
\end{problem}

The extra structure available (beyond bare Herglotz convergence): the $G_P^\circ$ are the marked global
Tate–Weil distributions of a \emph{positive arithmetic} family ($\Lambda\ge0$); the convergence carries
the **primitive marked tail estimate** of D8.5a (effective rates); and the whole tower has the
functional-equation symmetry $z\mapsto-z$ (the $J$-reflection $s\mapsto1-s$), with the off-line poles
occurring in mirror quadruples.

---

## Part III. Why every standard tool fails (the precise obstruction)

\begin{proposition}[positivity is compatible with off-$\R$ poles in a non-uniform limit]
A sequence of matrix Herglotz functions $G_P^\circ\in\mathcal N_0$ can converge \emph{meromorphically} to
$G\in\mathcal N_\kappa$ with $\kappa>0$. Hurwitz/normal-family closedness of $\mathcal N_0$ holds only
under \emph{locally uniform} convergence on $\C\setminus\R$; here a pole \emph{emerges} in $\C\setminus\R$
exactly by the failure of uniform convergence at that point. Hence:
\end{proposition}
\begin{itemize}
\item \textbf{D6 (closedness) cannot see it.} D6 transfers positivity only at finite configurations
$z_1,\dots,z_m$ \emph{avoiding} the poles; but $\operatorname{sq}_-(G_\Xi^{\mathrm G5})$ is attained only
at configurations \emph{meeting} the off-line poles (the negative directions live in the residues), where
the $G_P^\circ$ do not converge. So $\operatorname{sq}_-=0$ is not delivered.
\item \textbf{Herglotz positivity cannot exclude the pole.} $\Im G_P^\circ\succeq0$ in $\C^+$ forbids a
$\C^+$ pole \emph{under uniform convergence}; an emergent pole is precisely the non-uniform case, and the
emergent negative square is the signature of that non-uniformity. Positivity is therefore \emph{compatible}
with the off-$\R$ pole.
\item \textbf{The scalar determinant cannot see it} (N1, the whole reason for D2): $D_P^\circ\to\Xi$ holds
regardless of where the zeros are.
\end{itemize}

This is the same wall the program met repeatedly (the M3 finding), now at its finest resolution:
\textbf{the index lives exactly on the locus where the positive approximants stop converging.} No
argument using only (i) finite-stage positivity, (ii) scalar determinant convergence, or (iii) uniform
convergence away from the poles, can cross it. Something genuinely new is required at the off-$\R$ locus.

---

## Part IV. The explicit ask — how to prove D8.5b-ii (new mathematics needed)

We believe this is **not impossible** — it is one sharply-stated phenomenon — but it needs a new
principle that converts finite-stage positivity into control of the limit's principal parts at the
off-$\R$ locus, \emph{without} assuming uniform convergence there. We ask Connes specifically:

\begin{enumerate}
\item \textbf{An effective (quantitative) Herglotz no-emergence theorem.} The D8.5a marked tail estimate
gives \emph{rates}: $\|\sum_{Q<p^k\le P}G_{p,k}^\circ(z)\|\to0$ effectively on pole-free compacta. \emph{Is
there a quantitative form of Herglotz/Nevanlinna closedness} — bounding how large an emergent $\C^+$ pole
residue can be in terms of the approximants' $\C^+$ growth and the convergence rate — that forces the
residue to vanish? Equivalently: can the marked tail estimate be pushed \emph{up to and across} the
candidate off-$\R$ pole, contradicting its existence?

\item \textbf{A sign principle on emergent residues.} The residue of $G_\Xi^{\mathrm G5}$ at an off-$\R$
pole $z_\rho$ is the rank-one (or finite-rank) negative-square direction. \emph{Is this residue's sign/
structure forced, by the positivity of the approximants and the explicit formula, to be one the arithmetic
forbids?} (For a limit of Herglotz functions, an emergent $\C^+$ pole and its $\C^-$ mirror have linked
residues; the von Mangoldt positivity may constrain them.)

\item \textbf{The $J$-reflection $\times$ positivity.} The tower is symmetric under $z\mapsto-z$
($s\mapsto1-s$), and off-line poles come in mirror quadruples $\{z_\rho,-z_\rho,\bar z_\rho,-\bar z_\rho\}$.
\emph{Does the combination of the reflection symmetry with finite-stage positivity forbid an off-$\R$
pole}, in a way that on-line ($z_\rho\in\R$) poles survive? This is the "reflection is an isometry"
formulation; can it be made to act on the marked Green matrices?

\item \textbf{Realize the limit as self-adjoint in a genuine Hilbert space.} $\kappa=0$ is exactly the
statement that $G^{\lim}$ is the resolvent of a \emph{self-adjoint} operator in a Hilbert space (not a
Pontryagin space). \emph{Is there a completion of the primitive tower — a "pole-relative Hilbert
limit" — in which $A_\infty^\circ$ is essentially self-adjoint?} The divergence is rank-one and
definite-signed (G4); the question is whether that single definite mode is the only obstruction to
self-adjointness of the limit, and whether it can be removed by the right (signature-preserving)
completion. This is the original Phase-65 goal; D8.5b-ii is its irreducible core.

\item \textbf{Is D8.5b-ii provably equivalent to RH with no easier content, or is one of (1)–(4) genuinely
weaker?} We have been honest that, as a theorem implying RH, D8.5b-ii \emph{is} RH-strength. The question
is whether any of the structural inputs above is a \emph{new, independently provable} principle (so that
D8.5b-ii becomes a corollary), or whether each collapses back to the off-$\R$ divisor statement. \emph{We
ask for a verdict on which, and — if a new object is needed — what it should be.}
\end{enumerate}

---

## Summary

Everything from D0 to D12 is proved unconditionally except **D8.5b-ii**:

> \textbf{D8.5b-ii.} A meromorphic limit of \emph{positive} (matrix-Herglotz, $\mathcal N_0$) primitive
> resolvents — the marked Tate–Weil distribution of the positive von Mangoldt tower — has \textbf{no
> poles off the real axis}; equivalently its Kreĭn–Langer index is $0$; equivalently the off-$\R$
> principal parts of the marked Weil distribution vanish. \emph{This is RH.}

The obstruction is exact and the same one the program has circled: positivity controls the limit only
where it converges, and the index lives exactly where it does not. We ask Connes how to build the missing
principle — a quantitative Herglotz no-emergence theorem, a residue sign principle, a reflection-isometry
mechanism, or a pole-relative self-adjoint completion — that forces the off-$\R$ divisor to be empty. It
is one well-posed problem, and it is where the new mathematics must be created.
