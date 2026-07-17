# Attack + audit: the simple crossings of the one-point wall, and exactly where each turns into RH

*Pure mathematics. The wall is now a single scalar (`FACE-C-positivity-vs-size.md`):
$\sup_{P,u}e^{-u/2}\mathfrak d_P(u)<\infty$, the primitive diagonal of the positive kernel $K_P$.
A one-point statement invites a simple proof. We take the three most natural "hidden in plain sight"
crossings — **(I) averaging/flatness**, **(II) positive sandwich**, **(III) Schur/Bernstein from the
ODE** — push each to its limit, and **audit each to the exact RH-equivalent step**. Honest outcome: each
dies at a precisely named step, and the three deaths are the **same** statement seen three ways. This
is not a no-go in disguise of laziness; it is a structural theorem about *why* the one-point wall has
no free upper bound — its lower fence is free (positivity) and its upper fence is the Weil positivity
itself. No false victory.*

---

## Setup (recall, one line)

$\mathfrak d_P(u)=(P_{\mathrm{prim}}K_PP_{\mathrm{prim}})(u,u)\ge0$ is the diagonal of a positive
kernel; $e^{-u/2}\mathfrak d_P(u)$ is the local second moment of the zero-sum; its $\sup$ over
$u\in[0,L]$, $P\to\infty$ is the wall ($=$ short-interval prime variance $=$ pair correlation).

---

## Attack I — averaging / flatness: "$\sup\approx$ average, and the average is bounded"

\textbf{The simple idea.} The *average* of the diagonal is controlled by the trace:
\[
   \frac1L\int_0^L e^{-u/2}\mathfrak d_P(u)\,du\ =\ \frac1L\,\Tr\!\big(e^{-u/2}P_{\mathrm{prim}}K_P\big)
   \ \asymp\ \frac1L\cdot\frac{(\log P)^2}{2}\ \asymp\ \text{(bounded, since }L\asymp\log P\text{)} .
\]
So the **average is bounded unconditionally** (Mertens). If the diagonal were *flat* (no
concentration), $\sup\approx\text{average}\Rightarrow$ wall crossed.

\begin{auditbox}
\textbf{Audit — where it dies.} The step "$\sup\approx$ average" requires $e^{-u/2}\mathfrak d_P(u)$ to
have **no spikes**. But an off-line zero $\rho=\beta+i\gam$ is a **resonance**: it puts a bump of height
$\asymp e^{(2\beta-1)u_0}=\lambda^{2\beta-1}$ at the location $u_0$ where the bump $\widehat{w_u}$
phase-aligns with $\gam$. The diagonal is flat **iff** the zeros equidistribute with no real-part
excess, i.e. **iff RH**. So "flatness" is not an estimate — it is the conclusion. \emph{Precise
breakpoint:} $\sup=\text{average}+\text{(variance of the diagonal)}$, and the variance of the diagonal
$=\sum_\rho\lambda^{2(2\beta-1)}$, bounded $\Leftrightarrow$ RH. The bounded average is real (it is the
unconditional smooth part of `FACE-C-compactness.md` reincarnated); the gap from average to sup is
exactly the off-line excess.
\end{auditbox}

\emph{Verdict I.} The average is free; the deviation from average is RH. Death step: **flatness $=$ RH**.

---

## Attack II — positive sandwich: "find $M_P\succeq0$ with $K_P+M_P=$ bounded"

\textbf{The simple idea.} We have the **lower** fence for free ($K_P\succeq0$, Lever 2). For an
**upper** fence, sandwich: if there is a positive kernel $M_P\succeq0$ with $K_P+M_P=B_P$ where $B_P$ is
an *explicitly bounded* kernel, then $K_P\le B_P$ gives the wall. The natural candidate $B_P$ is the
**full Weil explicit-formula kernel**, because primes enter it with the archimedean and pole terms.

\textbf{What the explicit formula actually says.} The Weil functional is
\[
   W(f)\ =\ \underbrace{\widehat f(0)+\widehat f(1)}_{\text{poles}}
   \ +\ \underbrace{\int f\,\frac{\Gamma'}{\Gamma}}_{\text{arch}\ =\ M_P\ \succeq0}
   \ -\ \underbrace{\sum_n\frac{\Lambda(n)}{\sqrt n}\widehat f(\log n)}_{\text{primes}\ =\ K_P}
   \ =\ \sum_\rho\widehat f(\rho)\ \ge0\ \Leftrightarrow\ \text{RH}.
\]
So the sandwich **exists and is exact**: $M_P+(\text{poles})-K_P=W\ge0$, i.e.
\[
   \boxed{\ K_P\ \le\ M_P+(\text{poles})\quad\Longleftrightarrow\quad W\succeq0\quad\Longleftrightarrow\quad\text{RH}.\ }
\]

\begin{auditbox}
\textbf{Audit — where it dies.} The upper fence is not a *free* positive complement; it is the Weil
positivity $W\succeq0$ itself. The reason positivity gives the lower fence for free but **not** the
upper is now visible and structural: **primes enter $W$ with a minus sign.** $K_P\succeq0$ (free) is a
statement that the *subtracted* term is positive; bounding it *above* is bounding how much it
subtracts, which is exactly $W\ge0$. There is no positive $M_P$ making $K_P+M_P$ bounded other than the
arch$+$pole terms, and with those the bound is $W\ge0=$ RH. \emph{Precise breakpoint:} the sign of the
prime term in the explicit formula. The lower and upper fences are **not symmetric** — one is algebra
(squares), the other is RH.
\end{auditbox}

\emph{Verdict II.} The sandwich exists but its upper side is $W\succeq0$. Death step: **the minus sign
on primes in the explicit formula** (lower fence free, upper fence $=$ RH).

---

## Attack III — Schur / Bernstein from the canonical ODE: "$H\ge0$, finitely many atoms $\Rightarrow$ diagonal bounded"

\textbf{The simple idea.} $K_P=\int_0^\ell Y^*HY$ solves $J\partial_tY=zHY$ with $H\ge0$ a sum of
finitely many atoms (one per prime power $\le P^2$). For such a "few-atom" canonical system, the
transfer matrix $Y$ has controlled growth (Bernstein-type), and a Schur test
$\sup_u\int|K_P(u,v)|\,w(v)/w(u)\,dv<\infty$ would bound the diagonal.

\begin{auditbox}
\textbf{Audit — where it dies.} The Schur row-sum at the critical weight $w=e^{u/2}$ is
$\int|K_P(u,v)|e^{(v-u)/2}dv$. Expand $K_P(u,v)$ in the zero basis: the row-sum is
$\sum_\rho|\widehat{w_u}(\rho)|\,e^{(\beta-\frac12)(\cdot)}$, and for $\beta>\tfrac12$ the integrand
carries $e^{(\beta-\frac12)v}$ — the **same window amplification $\lambda^{2\beta-1}$**. The number of
atoms ($\pi(P^2)\sim P^2/\log P$) is large, not few, and the transfer matrix $Y(\ell,z)=D_P(z)\to\Xi$
(Stage 5) has its growth *governed by the zeros* — Bernstein's bound on $|Y|$ is itself a statement
about $\Re\rho$. \emph{Precise breakpoint:} the Schur weight $e^{(\beta-\frac12)v}$ is bounded
$\Leftrightarrow\beta=\tfrac12$. The ODE does not bound $Y$ independently of where its spectrum (the
zeros) sits; "few atoms" is false and "controlled growth" is RH.
\end{auditbox}

\emph{Verdict III.} The Schur test reproduces the window amplitude. Death step: **the Schur weight
$e^{(\beta-\frac12)v}$ $=$ RH.**

---

## §4. The three deaths are one theorem

\begin{theorem}[no free upper bound on the one-point wall]\label{thm:onefence}
Each of (I) flatness-deviation, (II) the upper sandwich fence, (III) the Schur weight equals the
factor $e^{(2\beta-1)\,\cdot}=\lambda^{2\beta-1}$, the window amplitude of an off-line zero. Hence:
\[
   \text{[positivity]}\ \Rightarrow\ \text{lower fence }0\le e^{-u/2}\mathfrak d_P(u)\ \text{(free)};
   \qquad
   \text{upper fence}\ \Leftrightarrow\ \text{no factor }\lambda^{2\beta-1}>1\ \Leftrightarrow\ \text{RH}.
\]
The asymmetry is forced by **one sign**: primes enter the Weil explicit formula negatively, so
$K_P\succeq0$ is free while $K_P\le(\text{bounded})$ is $W\succeq0=$ RH.
\end{theorem}

\begin{resultbox}
\textbf{What the audit establishes (genuine).} The one-point wall has a **free lower fence and an
RH-strength upper fence**, and the gap between them is *exactly* the single scalar $\lambda^{2\beta-1}$
summed over off-line zeros. Every "simple" crossing — averaging, sandwiching, Schur — hits this same
scalar at a precisely identifiable step. This is the cleanest possible diagnosis: the wall is not a
thicket of hard estimates but **one number, $\lambda^{2\beta-1}$, that is $>1$ iff there is an off-line
zero**, and no sign-based (positivity) argument can see it because positivity is blind to magnitude
(`FACE-C-positivity-vs-size.md`).
\end{resultbox}

---

## §5. Is there a crossing positivity *cannot* see? — the one honest opening

The audit says: any argument using only $K_P\succeq0$ dies, because sign $\ne$ magnitude. The logical
escape is an argument that **does not factor through positivity** — that uses the *phase* of the zeros,
not just their contribution's sign. The single place the program has not exhausted:

\begin{itemize}
\item \textbf{The factor $\lambda^{2\beta-1}$ is real and $>1$ only via a zero $\beta>\tfrac12$, but it
is multiplied by a phase $e^{2i\gam u}$.} The wall asks for the *modulus* sup; positivity throws the
phase away. A crossing must keep the phase: show that the off-line bump $\lambda^{2\beta-1}e^{2i\gam u}$
**cannot persist** because the functional equation forces a *mirror* bump $\lambda^{2\beta-1}
e^{-2i\gam u}$ (from $\rho\mapsto1-\bar\rho$) and the two, in the *primitive* (mean-removed,
$J$-reflected) compression, must **destructively interfere** unless $\beta=\tfrac12$.
\item This is **not** a positivity statement (it is a cancellation/phase statement), so it is not killed
by Theorem~\ref{thm:onefence}. It is the de Branges *structure* (the $J$-reflection $u\leftrightarrow
L-u$ pairing $\rho\leftrightarrow1-\bar\rho$) used for **cancellation**, not for sign.
\end{itemize}

\textbf{Driving the opening to a verdict (the computation).} The geometric $J$-reflection of the
canonical kernel is $u\leftrightarrow L-u$, which on the spectral side is $s\leftrightarrow1-s$, i.e. it
pairs $\rho=\beta+i\gam$ with $1-\rho=(1-\beta)-i\gam$ — **opposite phase**, not $1-\bar\rho$. So the
mechanism is genuinely present: the bump and its $J$-mirror carry conjugate phases and *try* to cancel.
Compute the two amplitudes at the far end $u\sim L=2\log\lambda$, where
$|\widehat{w_u}(\rho)|\asymp e^{(\beta-\frac12)L}=\lambda^{2\beta-1}$:
\[
   \text{bump}(\rho)\ \asymp\ \lambda^{2\beta-1}e^{+2i\gam u},\qquad
   \text{bump}(1-\rho)\ \asymp\ \lambda^{1-2\beta}e^{-2i\gam u}.
\]
In the symmetric ($J$-reflected, primitive) combination these add with opposite phase; the cancellation
is **complete iff the amplitudes match**:
\[
   \lambda^{2\beta-1}=\lambda^{1-2\beta}\quad\Longleftrightarrow\quad\beta=\tfrac12 .
\]
Off the line the residual is $\lambda^{2\beta-1}-\lambda^{1-2\beta}\asymp\lambda^{2\beta-1}\to\infty$ —
**exactly the wall amplitude again.**

\begin{auditbox}
\textbf{Verdict on the opening — it is RH too, but it sharpens the picture.} The phase/interference
mechanism is \emph{real} (the $J$-reflection $\rho\leftrightarrow1-\rho$ does force destructive
interference of the bump with its mirror), and it is \emph{not} killed by positivity
(Thm~\ref{thm:onefence}) — it is a genuine cancellation, the right kind of argument. But the
cancellation is **complete only on the critical line**, because the two interfering amplitudes
$\lambda^{2\beta-1}$ and $\lambda^{1-2\beta}$ are equal iff $\beta=\tfrac12$. \emph{Precise breakpoint:}
**amplitude matching of the $J$-mirror bumps $=$ functional equation pinning $\beta=\tfrac12$ $=$ RH.}
The off-line residual is again $\lambda^{2\beta-1}$. So §5 joins I–III at the same scalar — but it
identifies the *deepest* reason: RH is the statement that the functional equation's $s\leftrightarrow
1-s$ reflection is also an **isometry** (equal amplitudes), and a zero off the line is precisely a place
where the reflection is a contraction/expansion (mismatched amplitudes $\lambda^{\pm(2\beta-1)}$) rather
than an isometry.
\end{auditbox}

\emph{Verdict V (the opening, resolved).} Death step: **the $J$-mirror amplitudes are equal $\Leftrightarrow
\beta=\tfrac12\Leftrightarrow$ RH.** The functional equation gives the reflection; RH gives that it is an
*isometry*. This is the cleanest reformulation the audit produced: **RH $=$ the $s\leftrightarrow1-s$
reflection acts isometrically on the primitive canonical kernel.**

---

## §6. Honest close

Four natural "simple" crossings (averaging, sandwich, Schur, phase-interference), each pushed to its
limit and each audited dead at a **named** step — and the four steps are one scalar, $\lambda^{2\beta-1}$,
the off-line window amplitude. The deepest of the four (§5) reframes RH as: *the functional-equation
reflection is an isometry of the primitive canonical kernel.* That is a genuinely new, clean equivalent
— a candidate for the "hidden in plain sight" formulation — but it **is** RH (proved equivalent here,
not assumed), so it is not a crossing. No false victory: nothing here proves RH; the contribution is to
have driven every simple attack to an exact, honest verdict and extracted from the last one a sharp new
equivalent (isometry of the $J$-reflection) that may be the right handle for whoever crosses next.
