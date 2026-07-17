# Audit: did the phase-monotonicity "would-be proof" actually die? — No. It was mis-buried; it is an RH-strength reduction, not a corpse

*Self-audit (2026-06-29), requested before moving to the spectral-shift thread: re-examine the claim
in `FACE-C-structure-function-fork.md` §2 that the phase-monotonicity proof died. Verdict: the **stated
cause of death was an invalid argument**, now withdrawn. The honest status is that the proof is a
**valid reduction of RH to a Hurwitz-safe convergence** $E_P\to\Xi$ — neither dead (no flaw found) nor
complete (the convergence is itself RH-strength). This corrects an over-eager burial. No proof of RH.*

---

## §1. The would-be proof (verbatim)

1. Finite $P$: $H_{\mathrm{vM}}\ge0$ $\Rightarrow$ structure function $E_P$ is Hermite–Biehler (HB)
   $\Rightarrow$ phase $\varphi_P$ non-decreasing (de Branges phase criterion).
2. A pointwise limit of non-decreasing functions is non-decreasing.
3. $\varphi_P\to\varphi_\Xi$ $\Rightarrow$ $\varphi_\Xi$ non-decreasing $\Rightarrow$ $\Xi$ HB
   $\Rightarrow$ RH.

## §2. The buried cause of death — and why it is invalid

I wrote: *"step 3's premise $\varphi_P\to\varphi_\Xi$ is false, because $\det Y_{\mathrm{vM}}\equiv1$
forces $E_P\ne D_P$; the determinant $D_P\to\Xi$, the structure function $E_P\to E_\infty\ne\Xi$."*

\begin{auditbox}
\textbf{Invalid — withdrawn.}
\begin{itemize}
\item $\det Y\equiv1$ holds for \emph{every} canonical system (from $\tr(JH)=0$, since $JH$ is
trace-free for symmetric $H$). It is the Wronskian normalization. It does \textbf{not} relate $E_P$ to
$D_P$ in any way; the entries of $Y$ carry the entire spectrum while $\det Y=1$. Inferring "$E_P\ne
D_P$" from it is a non-sequitur.
\item I never proved $E_P\to E_\infty\ne\Xi$. I asserted it. There is no computation behind it.
\item It contradicts \textbf{Hurwitz's theorem}: if $E_P$ are HB (no zeros in open $\C_+$) and
$E_P\to F\not\equiv0$ locally uniformly, then $F$ has no zeros in open $\C_+$. So HB \emph{is} preserved
under honest locally-uniform limits — the generic "limits don't preserve HB" intuition is false here.
\end{itemize}
\end{auditbox}

## §3. The correct status: a reduction, not a death

The only way the proof fails is if step 3's convergence is not the kind Hurwitz needs.

\begin{proposition}[what is actually true]
$E_P$ HB $+$ $E_P\to\Xi$ \emph{locally uniformly} $\Rightarrow$ RH (Hurwitz). What is \emph{proved} to
converge to $\Xi$ is the \textbf{renormalized perturbation determinant}, $\mathrm{ren\text{-}lim}_P
D_P=\Xi$ (Stage 5). A renormalized limit divides out divergent normalizing factors
($\Tr K_P\sim\tfrac12(\log P)^2\to\infty$); such regularization can move zeros across $\mathbb R$ and is
\textbf{not} locally-uniform convergence. Therefore the Hurwitz hypothesis is not supplied, and the
proof reduces \emph{exactly} to:
\[
   \boxed{\ \text{(open, RH-strength) } E_P\to\Xi\ \text{locally uniformly (Hurwitz-safely).}\ }
\]
\end{proposition}

\textbf{Is the reduction itself circular (i.e. $=$ RH for a trivial reason)?} Partly: Hurwitz-safe
convergence of HB functions to $\Xi$ would prove RH, so it is at least RH-hard. But it is \emph{not}
obviously RH (it is a statement about a specific approximating sequence $E_P$ and the rate/mode of its
convergence), so it is a genuine reformulation, in the same family as every other equivalent the program
has produced — and it has the merit of being a \emph{convergence/regularity} statement rather than a
positivity or a zero-sum bound.

## §4. Net effect on the surrounding claims

- `FACE-C-structure-function-fork.md` §2 auditbox: **corrected** (the $\det Y\equiv1$ death withdrawn;
  replaced by the Hurwitz reduction).
- Floor theorem (§3 of that note): the hard clause "$E_\infty\ne\Xi$" is **withdrawn**; the theorem now
  reads "one canonical system is positive \emph{and} $\Xi$-realizing (Hurwitz-safely) iff RH," which is
  still correct and is the genuine floor. The two-halves picture stands as *complementary known
  certificates*, not as *provably distinct objects*.
- The spectral-shift lead (§4 of that note, Kreĭn $\arg D_P=\pi\xi_K$, $\xi_K\ge0$ free, monotonicity
  open) is **unaffected** — and is arguably the cleaner vehicle, since it uses $D_P$ (which genuinely
  $\to\Xi$) rather than the shakier $E_P$.

## §5. Verdict

The proof did **not** die from a flaw; my obituary used an invalid argument and is retracted. The
honest state: the phase-monotonicity argument is a **valid reduction of RH to the Hurwitz-safe
convergence $E_P\to\Xi$**, which is open and RH-strength. This is the correct, cold status — neither a
crossing nor a corpse. Lesson logged: a reduction-to-RH-strength is not the same as a dead proof; do not
bury a reduction with a hand-waved decoupling. The earlier rigidity-note phrase "signature-blind
determinant" remains valid for what it actually says (the determinant loses Pontryagin-index/signature
information), but it does \emph{not} establish $E_P\not\to\Xi$; only the renormalization argument bears
on the convergence, and it shows the convergence is \emph{unproven}, not \emph{false}.

No false victory, and now no false burial either.
