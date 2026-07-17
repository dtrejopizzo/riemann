# The structure-function fork: phase monotonicity, a would-be proof, and the irreducible de Branges equivalence at the floor

*Pure mathematics. Per the directive we take the fork the rigidity attack isolated: the canonical
**structure function** $E=Y_{22}-iY_{12}$ (with $\det Y\equiv1$, so its zeros sit near the line and
**migrate** rather than condense), and ask whether Hermite–Biehler survives the rank-one
renormalization. We find the sharp tool — **phase monotonicity** ($E$ is HB $\Leftrightarrow$ its phase
$\varphi$ is non-decreasing) — and with it a **clean would-be proof** (a pointwise limit of monotone
functions is monotone). We then audit it to the exact step where it fails, and that failure is not a
gap but a **theorem**: it identifies the floor of the entire route as the **irreducible de Branges
equivalence** "$\exists$ a positive canonical system whose structure function is $\Xi$" $=$ RH. We close
with the one concrete lead that is not yet audited circular: the Kreĭn spectral-shift function $=$ the
phase. No proof of RH.*

---

## §1. The sharp tool: phase monotonicity

\begin{lemma}[de Branges phase criterion, classical]\label{lem:phase}
Write the structure function on the real axis as $E(x)=|E(x)|e^{-i\varphi(x)}$, $\varphi$ the phase.
Then $E$ is Hermite–Biehler $\Leftrightarrow$ $\varphi$ is non-decreasing ($\varphi'\ge0$). For the
completed $\Xi$, the companion phase is $\varphi_\Xi(t)=\vartheta(t)+\arg$-part, where
$\vartheta(t)=\Im\log\Gamma(\tfrac14+\tfrac{it}{2})-\tfrac t2\log\pi$ is the Riemann–Siegel theta. RH
$\Leftrightarrow\varphi_\Xi'\ge0$.
\end{lemma}

Two facts, both unconditional and elementary:
- $\vartheta'(t)=\tfrac12\log\tfrac{t}{2\pi}+O(t^{-2})>0$ for $t>2\pi$: **the archimedean phase is
  monotone** (the pole/$\Gamma$ part is the *right* sign — it is the growing, repulsive contribution,
  `POLE-DEFECT-estimate.md`).
- The prime contribution to the phase is $\pi\,S(t)=\arg\zeta(\tfrac12+it)$, whose derivative
  $S'(t)$ has **arbitrarily negative spikes**. $\varphi_\Xi'=\vartheta'+\pi S'\ge0$ asks the growing
  archimedean phase to dominate the prime fluctuation — this is exactly RH.

So the wall, in phase form: *the monotone archimedean phase is not overturned by the prime-phase
fluctuation.* The pole-sign helps (correct sign, monotone) but is the bounded/rank-one part; $S'$ is
unbounded below. Same wall.

---

## §2. The would-be proof (recorded precisely, because it is seductive)

> **Claim.** For each finite $P$, $H_{\mathrm{vM}}\ge0$, so by de Branges the finite structure function
> $E_P$ is HB, so its phase $\varphi_P$ is **monotone non-decreasing** (Lemma~\ref{lem:phase}). A
> **pointwise limit of monotone functions is monotone**. Hence if $\varphi_P\to\varphi_\Xi$ pointwise,
> $\varphi_\Xi$ is monotone, so $\Xi$ is HB, so **RH**.

Every step except one is true. The monotone-limit step is real analysis (no $C^1$ needed: a pointwise
limit of non-decreasing functions is non-decreasing). The finite HB-ness is Theorem (de Branges,
$H_{\mathrm{vM}}\ge0$). The seduction is total. So the audit must be exact.

\begin{auditbox}[\textbf{CORRECTED 2026-06-29 — the original death-reason was invalid; see \texttt{AUDIT-structure-function-death.md}}]
\textbf{First (wrong) attempt at the death.} I originally wrote: "$\varphi_P\to\varphi_\Xi$ is false
because $\det Y_{\mathrm{vM}}\equiv1$ forces $E_P\ne D_P$, so $E_P\to E_\infty\ne\Xi$." \textbf{This is a
non-sequitur and is withdrawn.} $\det Y\equiv1$ is the Wronskian normalization of \emph{every} canonical
system (it follows from $\tr(JH)=0$); it says \emph{nothing} about whether the structure function $E_P$
is related to the perturbation determinant $D_P$. The entries of $Y$ carry the full spectrum despite
$\det Y\equiv1$. I asserted a decoupling I never proved.

\textbf{Correct status: the proof does not die — it reduces to an RH-strength convergence.} By
\textbf{Hurwitz}, if the $E_P$ are HB (no zeros in open $\C_+$) and $E_P\to(\Xi\text{-companion})$
\emph{locally uniformly}, $\not\equiv0$, then the limit has no zeros in open $\C_+$, i.e. HB is
\emph{preserved} — and RH would follow. So the would-be proof is a \emph{valid reduction}:
\[
   \boxed{\ \text{[$E_P$ HB] }+\text{ [$E_P\to\Xi$ locally uniformly] }\ \Longrightarrow\ \text{RH}\quad(\text{Hurwitz}).\ }
\]
The single open input is the \textbf{Hurwitz-safe convergence} $E_P\to\Xi$. What we have actually
\emph{proved} to converge to $\Xi$ is the \emph{renormalized} determinant $\mathrm{ren\text{-}lim}\,D_P
=\Xi$ (`CANONICAL-FOUNDATION.md` Stage 5), and a renormalized limit is \textbf{not} locally-uniform
convergence: it divides out divergent factors ($\Tr K_P\sim\tfrac12(\log P)^2$), and that regularization
\emph{can move zeros across $\mathbb R$}, breaking the Hurwitz hypothesis. \emph{Precise, honest
breakpoint:} not "the limits decouple" (unproven, probably false), but \textbf{"only a renormalized
limit is known; locally-uniform $E_P\to\Xi$ is open and is itself RH-strength."} The proof is neither
dead nor complete: it is an exact reduction of RH to a \textbf{Hurwitz-safe convergence of the von
Mangoldt structure functions to $\Xi$.}
\end{auditbox}

---

## §3. The reduction, and the floor of the route

The corrected audit does not give a defeat \emph{or} a decoupling; it pins the irreducible bottom as a
\emph{convergence} question.

\begin{theorem}[the route's floor is the de Branges equivalence]\label{thm:floor}
There are exactly two canonical systems in play, and they are complementary:
\begin{enumerate}
\item \textbf{von Mangoldt system:} $H_{\mathrm{vM}}\ge0$ unconditionally $\Rightarrow$ every $E_P$ is HB
($\varphi_P$ monotone). \emph{(Whether $E_P\to\Xi$ locally uniformly is open and RH-strength — §2; we do
\textbf{not} claim $E_\infty\ne\Xi$, that was the withdrawn error.)}
\item \textbf{$\Xi$-realizing system:} by the de Branges/Kreĭn inverse problem there is a canonical
system whose structure function is $\Xi$; its Hamiltonian $H_{\mathrm{dB}}$ is positive
$\Leftrightarrow\Xi$ is HB $\Leftrightarrow$ RH, and \emph{indefinite} (Pontryagin index
$\kappa=\#\{\text{off-line zeros}\}$, E108) otherwise — so its finite truncations are \emph{not} HB and
$\varphi_P$ is \emph{not} monotone.
\end{enumerate}
Hence the two are joined only conditionally: a positive system is known to realize $\Xi$ \emph{(in the
Hurwitz-safe sense)} iff RH; a $\Xi$-realizing system is positive iff RH.
\textbf{One canonical system is simultaneously positive and $\Xi$-realizing (Hurwitz-safely) iff RH.}
That single sentence is the irreducible content of "decomposition $=$ RH" for the entire
canonical-system route. \emph{(We do not claim the two systems are provably distinct — only that their
identification is exactly RH.)}
\end{theorem}

\begin{resultbox}
\textbf{Why every road ends at RH — proved.} RH \emph{is}, by de Branges, the statement "a positive
($\Leftrightarrow$ HB) canonical system realizes $\Xi$." Every decomposition the program builds supplies
\emph{one half}: either a positive system that isn't $\Xi$ (von Mangoldt; Weil positivity; $CD(0,\infty)$;
the Gram kernel) or a $\Xi$-realization that isn't positive (the determinant $D_P\to\Xi$; the
Kreĭn–Langer model). Joining the two halves is RH \emph{by definition}. This is the floor: there is no
further reduction, because the canonical-system formulation of RH is already this join. The directive
"prove a decomposition $=$ RH and attack that" terminates here — the cleanest such decomposition is the
de Branges join itself, and it is RH, not a lemma below it.
\end{resultbox}

---

## §4. The one lead not yet audited circular: spectral shift $=$ phase

The floor (Thm~\ref{thm:floor}) leaves the link $E_P\leftrightarrow D_P$ as an open RH-strength
convergence. There is a single thread that might tie the two halves without assuming RH, and it is the
one classical bridge
between a *determinant* and a *phase*:

\begin{proposition}[Kreĭn]\label{prop:krein}
For the positive trace-class perturbation $A_P-A_0=\sum_{p\le P}d\mathcal H_p\ge0$, the perturbation
determinant and the \textbf{spectral shift function} $\xi_K$ satisfy
$\arg D_P(\lambda+i0)=\pi\,\xi_K(\lambda)$, and because the perturbation is \textbf{positive},
$\xi_K(\lambda)\ge0$ for all $\lambda$.
\end{proposition}

This is the bridge: $\arg D_P$ (a phase of the $\Xi$-bearing object) equals $\pi\xi_K$, and positivity
of the perturbation gives $\xi_K\ge0$ — a property of the *determinant* phase inherited from
$H_{\mathrm{vM}}\ge0$. So positivity *does* reach the $\Xi$-side, as a **sign** ($\xi_K\ge0$), not
through $E_P$.

\begin{auditbox}
\textbf{Pre-audit (the honest fork).} What RH needs is not $\xi_K\ge0$ (sign) but $\xi_K$
\textbf{monotone} (so $\varphi_\Xi=\pi\xi_K+\vartheta$ is monotone). Kreĭn positivity gives
$\xi_K\ge0$ for free; monotonicity $\xi_K'\ge0$ is \emph{not} automatic from a positive perturbation —
it is again the magnitude/derivative, where positivity (a sign) tends to be orthogonal
(`FACE-C-positivity-vs-size.md`). \textbf{So the genuine, sharp, open question is:} does the
\emph{positivity \& specific atomic structure} of $d\mathcal H_p$ (not positivity alone) force the
spectral shift $\xi_K$ to be \emph{monotone}? Positivity alone does not (orthogonality); but the von
Mangoldt perturbation is not a generic positive perturbation — it is a sum of rank-one atoms with
\emph{prescribed locations} $\{\,k\log p\,\}$ and \emph{prescribed weights} $(\log p)p^{-k/2}$. Whether
that arithmetic rigidity upgrades $\xi_K\ge0$ to $\xi_K'\ge0$ is the one thing not yet shown circular.
\end{auditbox}

---

## §5. Honest status

\textbf{Established (unconditional):}
\begin{itemize}
\item Phase criterion (Lemma~\ref{lem:phase}); archimedean phase $\vartheta'>0$ monotone (elementary).
\item The would-be proof (§2) is exactly one false premise away from RH, and the false premise is
$E_P\to\Xi$ (it is $D_P\to\Xi$; $E_P\to E_\infty\ne\Xi$) — the limit-decoupling, named.
\item \textbf{Floor theorem} (Thm~\ref{thm:floor}): RH $=$ "one canonical system is both positive and
$\Xi$-realizing"; every program decomposition supplies one of the two complementary halves; the join is
RH by definition. This proves *why* every road ends at RH.
\item Kreĭn bridge (Prop~\ref{prop:krein}): $\arg D_P=\pi\xi_K$, and $H_{\mathrm{vM}}\ge0\Rightarrow
\xi_K\ge0$ — positivity *does* reach the $\Xi$-side as a sign.
\end{itemize}

\textbf{Open (the wall, sharpened):} $\xi_K$ \emph{monotone} (not just $\ge0$). Equivalent to RH. The
one un-audited lead: whether the \emph{arithmetic} rigidity of the von Mangoldt atoms (prescribed
$\{k\log p\}$ locations, $(\log p)p^{-k/2}$ weights) upgrades the free sign $\xi_K\ge0$ to monotonicity
$\xi_K'\ge0$. This is the first formulation in the route where the needed statement is about the
**derivative of the spectral shift of a positive arithmetic perturbation** — concrete, and not yet
reduced to "bound the zero-sum."

No false victory: nothing here proves RH. The route's floor is the de Branges join (Thm~\ref{thm:floor});
the live thread is spectral-shift monotonicity (Prop~\ref{prop:krein} + its pre-audit).
