# THE TARGET: the one theorem that is RH, the exact obstruction, and the new object to create

*This consolidates the entire phase-64 route into the single irreducible statement that must be proven,
why nothing we have reaches it, and the precise new mathematical object whose construction would cross
it. Everything else in the program is established or surrounding; this is the only thing left. Honest:
this statement IS RH (not a lemma below it). It is stated this sharply so that building the object is a
well-posed task.*

---

## §1. The target, in one sentence

\begin{quote}
\textbf{Realize $\Xi$ as the structure function of a \emph{positive} canonical system} — equivalently,
prove that the unconditionally-positive von Mangoldt canonical system's structure functions converge to
$\Xi$ in a way that \textbf{preserves the negative (Kreĭn–Langer) index} $\kappa$.
\end{quote}

Because the finite systems are positive ($\kappa=0$) and $\kappa(\Xi)=\#\{\text{off-line zeros}\}$,
index-preserving convergence forces $\kappa(\Xi)=0$, i.e. **RH**.

## §2. The target, formally (three equivalent faces of the *same* statement)

Let $A_P$ be the self-adjoint canonical operator of the positive von Mangoldt Hamiltonian
$H_{\mathrm{vM}}=\sum_{p^k\le P^2}(\log p)p^{-k/2}|v\rangle\langle v|\,\delta_{k\log p}\ge0$, with
perturbation determinant $D_P\to\Xi$ (Stage 5), structure function $E_P$, and phase $\varphi_P$.

\begin{theorem*}[the target — any one of these is RH]
\begin{enumerate}
\item[\textbf{(O)}] \textbf{Operator form.} The renormalized limit $A_\infty=\mathrm{ren\text{-}lim}_P
A_P$ is \textbf{self-adjoint} in the de Branges metric (equivalently essentially self-adjoint on the
primitive domain). \emph{Self-adjoint $\Rightarrow$ real spectrum $\Rightarrow$ zeros on the line.}
\item[\textbf{(I)}] \textbf{Index form.} The negative index is \textbf{continuous} through the
renormalization: $\kappa(\Xi)=\lim_P\kappa(E_P)=0$. \emph{(Each $E_P\in\mathcal N_0$; need $\Xi\in
\mathcal N_0$.)}
\item[\textbf{(C)}] \textbf{Convergence form.} $E_P\to\Xi$ \textbf{locally uniformly} (Hurwitz-safe),
not merely as a renormalized determinant. \emph{Then Hurwitz $\Rightarrow$ $\Xi$ Hermite–Biehler.}
\end{enumerate}
\end{theorem*}

These are one statement: (O)$\Leftrightarrow$(I)$\Leftrightarrow$(C), all $\Leftrightarrow$ RH. Their
common scalar shadow is the pointwise inequality
\[
   \tfrac12\log\tfrac{\lambda}{2\pi}+\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\cos(\lambda\log n)\ \ge\ 0
   \quad(\text{regularized, }\forall\lambda),
\]
but the scalar form throws away the structure; the **index/operator form is the one to build for.**

## §3. The exact obstruction (why nothing we have reaches it)

The whole program reduces to one structural fact, proven across four levels (operator norm, Carleson
box, diagonal sup, phase derivative):

\begin{quote}
\textbf{Everything we can prove for free is 0th-order (integrated, positivity-type); RH is 1st-order
(pointwise/index/derivative). Positivity is orthogonal to the 1st-order control.}
\end{quote}

Concretely, the only bridge from the free positivity to $\Xi$ is the **scalar perturbation determinant
$D_P\to\Xi$**, and a scalar determinant is **signature-blind**: it cannot see $\kappa$ (a
Pontryagin-indefinite system has an entire, zero-controlled determinant). The index $\kappa$ lives in
the **operator/matrix**, and it can only change in the limit through the **single rank-one divergence**
(the pole/degree mode, $\Tr K_P\sim\tfrac12(\log P)^2$). So:

\begin{center}
\fbox{\textbf{The wall $=$ the negative index may jump $0\to\kappa$ through the rank-one pole
renormalization, and the scalar determinant cannot detect it.}}
\end{center}

## §4. The new object to create

To cross, one must replace the signature-blind scalar determinant by an object that **carries the index
through the limit**. Its required axioms:

\begin{quote}
\textbf{An index-preserving regularized determinant (equivalently, a de Branges metric / Hilbert
completion) $\widetilde D$ for canonical systems with a single rank-one trace divergence, such that:}
\begin{enumerate}
\item[(A1)] on \emph{finite} positive systems it agrees with the data we have ($\widetilde D(A_P)$
recovers $E_P$, $\kappa=0$);
\item[(A2)] it is \textbf{continuous in $\kappa$} under the rank-one renormalization $A_P\to A_\infty$
(the negative index does not jump across the pole mode);
\item[(A3)] its limit is $\Xi$: $\widetilde D(A_\infty)=\Xi$ with its genuine index $\kappa(\Xi)$.
\end{enumerate}
\textbf{Any object satisfying (A1)–(A3) proves RH}, because (A1)+(A2) give $\kappa(\Xi)=0$.
\end{quote}

What is genuinely new in (A2): a **topology on generalized Nevanlinna ($\mathcal N_\kappa$) /
de Branges functions in which $\mathcal N_0$ is closed *and* the arithmetic renormalization converges.**
The ordinary (locally-uniform) topology fails on both counts ($\mathcal N_0$ not closed; ren-lim not
locally-uniform). The object must be **adapted to the specific rank-one pole** of the arithmetic system
— it is not a generic functional-analytic completion but one that uses that the divergence is
**rank-one and of definite ($+$) sign** (the pole of $\zeta$ at $s=1$, the repulsive barrier).

\emph{This is the lever the program uniquely supplies:} the divergence is **not generic** — it is
rank-one, definite-signed, and arithmetically explicit. A signature-continuity theorem for rank-one,
definite-signed renormalizations of positive canonical systems is a concrete, well-posed,
possibly-new theorem. If it is true in the needed form, RH follows; if it is false, there is an
off-line zero and the failure is exactly the index jump.

## §5. What this is, honestly

- It **is** RH (the de Branges join; not a sub-lemma). The program has proven this is the irreducible
  bottom — every road ends here because the canonical-system formulation of RH *is* this join (§Floor
  theorem, `FACE-C-structure-function-fork.md`).
- It is, however, **a sharper target than generic Hilbert–Pólya**: the program has localized the entire
  difficulty to **one rank-one, definite-signed renormalization** and to the **index-continuity** of a
  determinant there. The new object is not "a self-adjoint operator with the zeros as spectrum" in the
  abstract — it is **an index-continuous regularized determinant for a rank-one definite divergence**,
  with axioms (A1)–(A3).
- Everything feeding it is **proved and unconditional**: $H_{\mathrm{vM}}\ge0$, the Gram positivity
  $K_P\succeq0$, finite HB-ness, $D_P\to\Xi$, $\xi_K\ge0$, the curvature $CD(0,\infty)$. The single
  missing piece is (A2): index-continuity through the pole.

\textbf{The task to commit to:} construct $\widetilde D$ (axioms A1–A3), i.e. prove the
\textbf{signature-continuity of the regularized determinant under the rank-one definite-signed pole
renormalization of the von Mangoldt canonical system.} That is the whole of RH, and it is the place to
put the full effort.
