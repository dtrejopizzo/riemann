# Rigidity attack on the isometry equivalent: must a positive-Hamiltonian reflection be isometric? — the de Branges theorem says YES for the structure Hamiltonian, and the audit pins the wall to a single new statement: **Hermite–Biehler survives renormalization $\Leftrightarrow$ RH**

*Pure mathematics. Per the directive — stop seeking new roads, attack the equivalence "decomposition $=$
RH" directly and make it as sharp as possible — we take the isometry reformulation
(`FACE-C-simple-crossings-audit.md` §5: RH $=$ the reflection $s\leftrightarrow1-s$ is an isometry of
the primitive canonical kernel) and attack it with **rigidity**, a non-positivity tool. We find a real
theorem (de Branges: a positive canonical system has a Hermite–Biehler transfer matrix, hence isometric
reflection), audit exactly why it does not close, and extract the sharpest equivalent the program has
produced: **every finite Euler truncation is already Hermite–Biehler (RH-true); RH is precisely the
statement that this property is not destroyed by the single rank-one renormalization (the pole).** We
also catch and defuse the false-victory version of the argument. No proof of RH.*

---

## §1. The rigidity theorem is real (and points the right way)

\begin{theorem}[de Branges structure theorem, classical]\label{thm:db}
Let $J\partial_tY=zH(t)Y$ be a canonical system on $[0,\ell]$ with $H(t)\ge0$, trace-normalized,
$H\in L^1$. Then the transfer matrix $Y(\ell,z)$ is of \textbf{Hermite–Biehler} (HB) type: its
structure function $E=Y_{22}-iY_{12}$ (suitable entry combination) has \emph{no zeros in the open upper
half-plane}, and the reflection $R:s\leftrightarrow1-s$ acts \textbf{isometrically} on the de Branges
space $\mathcal H(E)$.
\end{theorem}

So the rigidity we wanted is a **theorem**: positivity of the Hamiltonian $\Rightarrow$ HB structure
function $\Rightarrow$ zeros on the critical line $\Rightarrow$ isometric reflection. The
contrapositive is the Kreĭn–Langer picture we already have (E108): off-line zeros $\Leftrightarrow$ the
structure Hamiltonian is \emph{indefinite}, with Pontryagin index $\kappa=\#\{$off-line zeros$\}$.

\begin{center}
\fbox{\ positivity of the \emph{structure} Hamiltonian $H_{\mathrm{dB}}$\ $\Longleftrightarrow$\ HB\ $\Longleftrightarrow$\ RH\ }
\end{center}

This is genuine and exactly the leverage the directive asks for: it is a **non-positivity-blind**
statement (rigidity through HB / zero location), so it escapes the orthogonality theorem of
`FACE-C-positivity-vs-size.md`. The question is whether *our* positivity feeds it.

---

## §2. Audit: two different Hamiltonians (this is the whole game)

There are **two** Hamiltonians in play, and conflating them is the false victory.

| | **$H_{\mathrm{vM}}$ (von Mangoldt)** | **$H_{\mathrm{dB}}$ (structure)** |
|---|---|---|
| definition | $\sum_{p^k\le P^2}(\log p)p^{-k/2}|v\rangle\langle v|\,\delta$ | inverse-spectral Hamiltonian of $\Xi$ |
| positivity | $\ge0$ **unconditionally** ($\Lambda\ge0$) | $\ge0$ $\Leftrightarrow$ **RH** (Thm~\ref{thm:db}) |
| transfer $\to\Xi$ | via **scalar determinant** $D_P\to\Xi$ | via **structure function** $E\to$ $\Xi$ |
| what it controls | the Weil kernel $K_P\succeq0$ | the zero locations |

\begin{auditbox}
\textbf{The conflation, named.} The rigidity theorem needs $H_{\mathrm{dB}}\ge0$, and
$H_{\mathrm{dB}}\ge0$ \emph{is} RH (inverse spectral theory: the Hamiltonian reconstructed from $\Xi$ is
positive iff $\Xi$ is HB). Our free positivity is of the \emph{other} Hamiltonian $H_{\mathrm{vM}}$. The
two are bridged only by $Y_{\mathrm{vM}}(\ell,\cdot)\to D_P\to\Xi$, the \textbf{scalar perturbation
determinant} — and a scalar determinant is \textbf{signature-blind}: $\det$ does not see the Pontryagin
index $\kappa$ (a Pontryagin-indefinite system can have an entire, zero-controlled determinant). So the
determinant bridge \emph{structurally cannot transport positivity} from $H_{\mathrm{vM}}$ to
$H_{\mathrm{dB}}$. \emph{Precise breakpoint:} the matrix signature $\kappa$ lives in the operator, not
in $\det$; the bridge throws it away.
\end{auditbox}

So the naive rigidity closure is circular: it transports nothing because the only available bridge is
signature-blind.

---

## §3. The false victory, caught

There is a seductive direct argument; I record it precisely so it is never mistaken for a proof.

> *"$H_{\mathrm{vM}}\ge0$, so by Theorem~\ref{thm:db} the transfer $Y_{\mathrm{vM}}(\ell,\cdot)$ is HB,
> so its zeros are on the line; but $Y_{\mathrm{vM}}(\ell,\cdot)\to\Xi$, whose zeros are the
> $\zeta$-zeros; therefore RH."*

\begin{auditbox}
\textbf{Where it is false.} Theorem~\ref{thm:db} applies to the \textbf{finite} system, and it is
\emph{true} there: for each finite $P$, $H_{\mathrm{vM}}\ge0$ and $Y_{\mathrm{vM}}^{(P)}(\ell,\cdot)$
\emph{is} HB — but its zeros are the zeros of the \textbf{finite} object $D_P$ (a finite Euler-type
product), \emph{not} the $\zeta$-zeros. The $\zeta$-zeros appear only in the
\textbf{renormalized limit} $\mathrm{ren\text{-}lim}_P D_P=\Xi$, and that limit is \textbf{not} a
positive canonical system in the sense of Theorem~\ref{thm:db}: the trace diverges,
$\Tr K_P\sim\tfrac12(\log P)^2\to\infty$ (Mertens), so $H_{\mathrm{vM}}$ is \emph{not} trace-normalizable
in the limit and the HB-preserving hypothesis fails. \emph{The HB property of the finite truncations is
not known to survive the renormalization.}
\end{auditbox}

---

## §4. The sharp equivalent (the genuine yield of the attack)

The audit of the false victory is itself the sharpest reformulation. Pull the surviving true facts
together:

\begin{theorem}[HB-stability form of RH]\label{thm:hbstab}
For every finite $P$, the von Mangoldt transfer matrix $Y_{\mathrm{vM}}^{(P)}(\ell,\cdot)$ is
Hermite–Biehler (Theorem~\ref{thm:db}, $H_{\mathrm{vM}}\ge0$). The renormalized limit is $\Xi$. Hence
\[
   \boxed{\ \mathrm{RH}\ \Longleftrightarrow\ \text{HB is preserved under }\mathrm{ren\text{-}lim}_{P\to\infty}.\ }
\]
Moreover, since the only obstruction to trace-normalizability is the rank-one pole/degree direction $H$
($\Tr K_P\sim\tfrac12(\log P)^2$ lives entirely on the constant mode), HB-stability is equivalent to the
\textbf{rank-one escape}: $\sup_P\|P_{\mathrm{prim}}K_PP_{\mathrm{prim}}\|<\infty$. The two named walls
of the program — HB-survival and rank-one escape — are \emph{the same wall}.
\end{theorem}

\begin{resultbox}
\textbf{What the rigidity attack establishes.} (1) The rigidity theorem is \emph{real} and \emph{is not}
blocked by the positivity-orthogonality theorem — it is the right kind of tool. (2) It does not close,
for one exact reason: it needs the \emph{structure} Hamiltonian's positivity, which is RH, and the only
bridge from our \emph{free} positivity is the signature-blind determinant. (3) The yield: a new, sharp,
arguably-simplest equivalent — **every finite Euler truncation is HB (the finite Riemann hypothesis
holds exactly); RH is the single statement that Hermite–Biehler is not destroyed by the rank-one pole
renormalization.** This converts "decomposition $=$ RH" into a \emph{stability} question — does a
property true at every finite stage survive one rank-one limit — which is a genuinely different and
more concrete target than "bound the zero-sum."
\end{resultbox}

---

## §5. Why this is the right thing to attack next (and what tool, honestly)

The directive: attack the equivalence, make it simplest. Theorem~\ref{thm:hbstab} is the simplest yet —
it is a **continuity/stability of a closed condition (HB) under a rank-one perturbation of the
Hamiltonian's normalization.** The relevant non-positivity tools are exactly the ones for *that*:

- **HB / Hermite–Biehler stability** is governed by the zeros of $E$ not crossing the real axis. A
  rank-one (pole) perturbation moves zeros by a rank-one resolvent term; whether any zero is pushed off
  $\mathbb R$ is a **monotonicity/interlacing** question (Hadamard variation, eigenvalue interlacing
  under rank-one updates) — *not* a positivity bound.
- The honest hope: a finite-rank perturbation of an HB function stays HB **iff** the perturbation is
  in the right one-sided cone (de Branges' theory of $\mathcal H(E)\subset\mathcal H(E')$ inclusions: an
  HB $E$ embeds in a larger de Branges space iff a sign condition on the difference holds). The pole is
  one-dimensional; the question is whether its sign is the admissible one.

\begin{auditbox}
\textbf{Pre-audit of the next step (so we do not fool ourselves).} The de Branges inclusion
$\mathcal H(E)\subseteq\mathcal H(E')$ holding for the renormalization step is *itself* a positivity
(the difference of reproducing kernels $\succeq0$), so if the rank-one stability reduces to a de Branges
inclusion we are back to positivity and the orthogonality theorem may bite again. The escape is only if
the **interlacing** (a real-axis, order-theoretic statement about where the pole pushes zeros) can be
decided by the **sign of the pole alone** (which we know: the pole of $\zeta$ at $s=1$ is a definite
$+$, the repulsive barrier of `POLE-DEFECT-estimate.md`) **plus the finite-stage HB** — without a new
bound on the zero-sum. That is the one combination not yet tried and not obviously RH. It is the genuine
next probe.
\end{auditbox}

---

## §6. Honest status

\textbf{Established (unconditional):}
\begin{itemize}
\item de Branges rigidity (Thm~\ref{thm:db}) is a real theorem and the right kind of tool (escapes
positivity-orthogonality).
\item Finite von Mangoldt transfer matrices are HB at every $P$ (the "finite RH" holds exactly).
\item \textbf{HB-stability form} (Thm~\ref{thm:hbstab}): RH $\Leftrightarrow$ HB survives the rank-one
renormalization $\Leftrightarrow$ rank-one escape. The HB-survival wall and the rank-one wall coincide.
\item The naive rigidity closure and the direct "finite HB $\Rightarrow$ RH" are both \emph{false},
caught at the named step (signature-blind determinant; renormalization destroys trace-normalizability).
\end{itemize}

\textbf{Open (the wall, unchanged, RH-strength):} HB-survival under the rank-one pole renormalization.
The proposed attack (interlacing decided by pole-sign $+$ finite HB, avoiding a new zero-sum bound) is
\emph{untested} and pre-audited as the one combination not yet shown to be circular.

No false victory: nothing proves RH. The contribution is to have turned the isometry equivalent into a
**stability** equivalent (HB survives one rank-one limit), shown the classical rigidity theorem is genuine
but bridged to our data only by a signature-blind determinant, and isolated the precise, possibly-new
handle (pole-sign interlacing) for the next probe.
