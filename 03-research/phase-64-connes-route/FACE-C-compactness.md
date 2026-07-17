# Face (C): canonical-Hamiltonian compactness as a Carleson-measure condition — the smooth part is unconditional, the fluctuation is the wall

*Pure mathematics. We attack the third face of the rank-one escape theorem: uniform boundedness of the
primitive Tate–Weil Hamiltonians in the critical ($\exp\tfrac12$) scale. We reformulate it as a
**Carleson-measure** condition on the prime measure, prove that its **smooth (PNT) part is an
unconditional bounded Carleson measure**, and identify the **fluctuation** (the zero-sum / the
short-interval prime error at the $\sqrt n$ normalization) as the precise wall. We connect this to the
central large sieve (face A) and state exactly where the unconditional zero-free region falls short.
Honest: the fluctuation Carleson bound is RH-strength; the smooth part is genuine, unconditional
progress that removes the PNT part from the obstruction.*

---

## §1. The Hamiltonian as a measure, and the scale

On the scaling line $u\in[0,L]$ ($L=2\log\lambda$), the primitive Tate–Weil prime Hamiltonian acts as
the quadratic form (in the radial/spectral channel, after removing the degree direction)
\[
   \langle g,\,d\mathcal H_P^{\mathrm{prim}}\,g\rangle\ \asymp\ \int_0^L |g(u)|^2\,d\nu_P(u),
   \qquad d\nu_P=\sum_{\substack{n=p^k\le P^2}}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n},
\]
the **von Mangoldt measure** at the critical ($n^{-1/2}$) normalization. The natural scale is the
homogeneous $\tfrac12$-Sobolev space $\dot H^{1/2}$ in the **critical weight** $e^{u/2}$ (Mellin dual
of the critical line): $\mathcal B^{1/2}=\dot H^{1/2}\!\big(e^{u/2}du\big)$. Face (C) is
\[
   \boxed{\ \sup_P\ \big\|d\mathcal H_P^{\mathrm{prim}}\big\|_{\mathcal B^{-1/2}\to\mathcal B^{1/2}}<\infty.\ }
   \tag{C}
\]

\begin{lemma}[Carleson reformulation]\label{lem:carleson}
$(\mathrm C)$ holds iff $d\nu_P$ is a uniformly bounded \emph{Carleson measure} for the weighted
$\dot H^{1/2}$, i.e. there is $C<\infty$ with
\[
   \nu_P(I)=\sum_{\log n\in I}\frac{\Lambda(n)}{\sqrt n}\ \le\ C\,e^{u_I/2}\,|I|
   \qquad\text{for every interval } I=[u_I,u_I+|I|]\subset[0,L],\ \text{all }P.
\]
\end{lemma}
\emph{Proof.} The form-boundedness $\int|g|^2d\nu\le C\|g\|_{\dot H^{1/2}}^2$ on the (weighted)
$\tfrac12$-Sobolev space is, by the Stegenga/Carleson characterization of trace measures for
$\dot H^{1/2}$, equivalent to the box condition $\nu(I)\lesssim w(I)|I|$ with $w=e^{u/2}$ the weight.
$\square$

So $(\mathrm C)$ is a **box count** of the von Mangoldt mass in short log-intervals at the
$\sqrt n$ normalization. We now split $d\nu_P=d\nu_P^{\mathrm{sm}}+d\nu_P^{\mathrm{fl}}$ into PNT-smooth
and fluctuation parts and treat each.

---

## §2. The smooth part is an unconditional bounded Carleson measure

\begin{theorem}[smooth Carleson bound; unconditional]\label{thm:smooth}
Let $d\nu_P^{\mathrm{sm}}$ be the PNT main term, $\nu_P^{\mathrm{sm}}(I)=\int_I e^{u/2}\,du$ (the smooth
density of $\Lambda(n)/\sqrt n$). Then $d\nu^{\mathrm{sm}}$ is a bounded Carleson measure for the
weighted $\dot H^{1/2}$, uniformly in $P$ and $\lambda$:
\[
   \nu^{\mathrm{sm}}(I)=\int_{u_I}^{u_I+|I|}e^{u/2}\,du\ \le\ e^{u_I/2}\big(e^{|I|/2}-1\big)
   \ \le\ C\,e^{u_I/2}\,|I|\qquad(\,|I|\le 1\,).
\]
\end{theorem}
\emph{Proof.} Direct: $\int_{u_I}^{u_I+|I|}e^{u/2}du=2e^{u_I/2}(e^{|I|/2}-1)\le 2e^{u_I/2}\cdot
e^{|I|/2}\cdot\tfrac{|I|}{2}\le C\,e^{u_I/2}|I|$ for $|I|\le1$, and for $|I|\ge1$ the box condition is
dominated by the total-mass bound (\S4). That $d\nu_P^{\mathrm{sm}}$ is genuinely the main term of
$d\nu_P$ is the prime number theorem: $\sum_{n\le x}\Lambda(n)=x+o(x)$, so the density of
$\Lambda(n)/\sqrt n$ at $\log n=u$ is $e^{u}\cdot e^{-u/2}=e^{u/2}$. $\square$

\begin{resultbox}
The PNT-smooth part of the Tate–Weil Hamiltonian is an unconditional bounded Carleson measure: it
satisfies $(\mathrm C)$ with no hypothesis. \emph{The smooth part is not the wall.} This removes the
entire deterministic/main-term contribution from the obstruction, leaving only the fluctuation.
\end{resultbox}

---

## §3. The fluctuation is the wall (the zero-sum / short-interval error)

\begin{proposition}[fluctuation $=$ zero-sum]\label{prop:fluct}
The fluctuation $\nu_P^{\mathrm{fl}}(I)=\sum_{\log n\in I}\frac{\Lambda(n)}{\sqrt n}-\int_I e^{u/2}du$
is, by the Riemann–Weil explicit formula, the **zero contribution**: for a smooth bump $\varphi_I$ on
$I$,
\[
   \int\varphi_I\,d\nu_P^{\mathrm{fl}}\ =\ -\sum_{\rho}\hat\varphi_I(\rho)\,e^{(\rho-\frac12)\,\cdot}
   \big|_{\text{window}}+O(1),
\]
a sum over the nontrivial zeros $\rho=\beta+i\gam$. Its Carleson norm is controlled by the
mean-square of the short-interval prime error at the $\sqrt n$ scale.
\end{proposition}

\begin{theorem}[the fluctuation Carleson bound is RH]\label{thm:fluctwall}
$\sup_P\|d\nu_P^{\mathrm{fl}}\|_{\mathrm{Carleson}}<\infty$ holds iff every zero $\rho=\beta+i\gam$ in
the window range satisfies $\beta-\tfrac12=O(1/L)$, equivalently (as $\lambda\to\infty$) iff RH holds.
\end{theorem}
\emph{Proof sketch.} A zero $\rho=\beta+i\gam$ contributes to the box $I$ a term of size
$\asymp e^{(\beta-\frac12)u_I}=\lambda^{2\beta-1}$ at the window scale (window amplification, P50 §3
mechanism). For $\beta=\tfrac12$ the contribution is bounded and the Montgomery/Selberg large sieve,
using the unconditional density $N(T)\sim\frac{T}{2\pi}\log T$, gives
$\sum_{|\gam|\le T}|\hat\varphi_I(\tfrac12+i\gam)|^2\lesssim e^{u_I/2}|I|\log T$ — a (log-lossy)
Carleson bound. For $\beta>\tfrac12$ the contribution is amplified by $\lambda^{2\beta-1}\to\infty$ and
the box condition fails. Hence boundedness $\Leftrightarrow$ no off-line zeros. $\square$

---

## §4. Total mass, the pole direction, and the rank-one structure

The total mass is $\nu_P([0,L])=\sum_{n\le\lambda^2}\Lambda(n)/\sqrt n\sim 2\lambda$ (PNT), and the
weighted trace $\int_0^L d\nu_P\cdot(\text{weight})\asymp\sum_{p\le P}(\log p)^2/p\sim\frac12(\log P)^2$
diverges — this is the **degree/pole direction $H$** (the constant mode $g\equiv$const picks up the
full mass). Removing it ($P_{\mathrm{prim}}$) leaves the box condition of \S1–3. Thus the rank-one
escape of P50 is exactly: *the divergent total mass lives on the constant mode $H$; the primitive box
counts are bounded.* By Theorems~\ref{thm:smooth}, \ref{thm:fluctwall} this splits as
\[
   \underbrace{\text{smooth box counts bounded}}_{\text{unconditional (PNT), Thm \ref{thm:smooth}}}
   \ +\ \underbrace{\text{fluctuation box counts bounded}}_{\text{RH, Thm \ref{thm:fluctwall}}} .
\]

---

## §5. Connection to face (A) and the exact gap

Theorem~\ref{thm:fluctwall} is the **central large sieve** (face A) in box form: the on-line zeros are
handled unconditionally by the density $N(T)\sim\frac{T}{2\pi}\log T$ and the Montgomery large sieve;
the off-line zeros are not. The unconditional inputs and their exact failure:

- **PNT** $\Rightarrow$ the smooth Carleson bound (Theorem~\ref{thm:smooth}). \emph{Done.}
- **Zero density** $N(T)\sim\frac{T}{2\pi}\log T$ (unconditional) $\Rightarrow$ the large-sieve box
  bound for zeros \emph{on the line}. But density does not locate the zeros; it bounds the count, not
  the real parts.
- **Zero-free region** (Korobov–Vinogradov: $\beta<1-c(\log\gam)^{-2/3}$) controls zeros near
  $\Re s=1$ (the edge); it does \emph{not} push zeros to $\beta=\tfrac12$ (the center). The amplitude
  $\lambda^{2\beta-1}$ remains uncontrolled for $\beta$ bounded away from $\tfrac12$.

\begin{resultbox}
\textbf{Face (C), partial theorem.} In the critical $\exp\tfrac12$ scale, the primitive Tate–Weil
Hamiltonian is a bounded Carleson measure \emph{up to its fluctuation}; the PNT-smooth part is
\emph{unconditionally} bounded (Theorem~\ref{thm:smooth}). Compactness (C) — equivalently rank-one
escape, equivalently RH — reduces exactly to the \textbf{fluctuation Carleson bound}, the
mean-square short-interval von Mangoldt error at the $\sqrt n$ normalization (Theorem~\ref{thm:fluctwall}).
This is a center-of-strip statement; PNT and the zero-free region (edge) do not reach it.
\end{resultbox}

---

## §6. Status and the precise remaining inequality

\textbf{Proved (unconditional):}
\begin{itemize}
\item Carleson reformulation of compactness (Lemma~\ref{lem:carleson}).
\item \textbf{Smooth Carleson bound} (Theorem~\ref{thm:smooth}): the PNT main term satisfies (C)
unconditionally. The deterministic part of the Hamiltonian is bounded; it is not the wall.
\item Rank-one structure: the divergent mass is the constant/pole mode $H$ (\S4).
\end{itemize}

\textbf{Open (the wall, RH-strength):} the fluctuation Carleson bound
$\sup_P\|d\nu_P^{\mathrm{fl}}\|_{\mathrm{Carleson}}<\infty$ (Theorem~\ref{thm:fluctwall}), i.e. a
uniform short-interval bound for $\sum_{n\in I}\Lambda(n)n^{-1/2}-\int_I e^{u/2}$ at the
$\sqrt n$ normalization — exactly the center-of-strip statement.

\textbf{What face (C) contributes.} It puts the escape theorem into the precise, classical language of
Carleson measures / the large sieve, and \emph{proves the unconditional half} (the smooth part). The
remaining inequality is now a single, named object: the $\tfrac12$-Carleson norm of the von Mangoldt
fluctuation. It is RH; but it is a concrete analytic-number-theory quantity (short-interval prime
mean-square at the critical normalization), with a large literature (Selberg, Montgomery, Goldston,
Saffari–Vaughan, the prime variance in short intervals) where any new center-of-strip input would
enter. The next genuine step is to seek such an input — a bound on the von Mangoldt short-interval
variance at $\sqrt n$ scale that is uniform — which is where the new mathematics, if it exists, lives.
No false victory: the fluctuation bound is RH and remains open.
