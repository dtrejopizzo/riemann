# D.121 — Coupled cutoff/support renormalization at prime-power thresholds

## Verdict

Coupling the arithmetic cutoff to the support window by

\[
 X=e^{2T},\qquad T_N={1\over2}\log N                         \tag{0.1}
\]

gives an exact threshold recurrence.  A new prime-power contact is harmless
at the instant it enters: its two translated supports meet only in a null
set, and the increase of its positive jump energy is exactly cancelled by
the increase of the bulk mass \(2A_X\).

The subsequent opening of the overlap is a boundary-capacity problem.  An
exact Schur/Feshbach invariant is formulated below; if its capacity is at
least the entering contact in every cell, row D follows inductively.

The elementary Gamma-capacity mechanism that crosses the first \(p=2\)
hinge does not provide a uniform invariant.  Its high-frequency Gamma
budget consumed at the prime \(p\) is at least of order \(p^{-1/2}\) under
the spatial localization needed to cross a cell of width \(O(p^{-1})\), and
this is not summable over primes.  Choosing a frequency cutoff large enough
to make the Gamma consumption summable makes the spatial leakage
non-summable.

Thus the multiscale recurrence is exact, but closing it requires a sharper
uniform directed-capacity estimate exploiting the joint prime--Gamma Schur
complement.  Such an estimate is not supplied by local Gamma coercivity or
by the product formula alone; proving it is an equivalent local form of the
remaining row-D inequality.

## 1. The exact renormalized operator

On \(I_T=[-T,T]\), let \(P_T\) denote the projection onto the two-moment
primitive space.  For \(N\le e^{2T}\), put

\[
 H_{N,T}=P_T\left(
 L_{\infty,T}-m_0I
 -\sum_{2\le n\le N}{\Lambda(n)\over\sqrt n}
       (S_{\log n}+S_{-\log n})
 \right)P_T.                                             \tag{1.1}
\]

Here \(\Lambda(n)\) is not inserted analytically: it abbreviates the A--B
contact degree, equal to \(\log p\) for \(n=p^k\) and zero otherwise.  By
D.117,

\[
 H_{N,T}=-B_{{\rm nuc},N,T}\quad\text{on }\operatorname{Ran}P_T. \tag{1.2}
\]

Row D is

\[
 H_{N,T}\ge0                                             \tag{1.3}
\]

for every stabilized window, followed by the directed limit.

## 2. Exact threshold update

Let \(w_N=\Lambda(N)/\sqrt N\) and \(a_N=\log N\).  At fixed \(T\), the
positive jump and mass update is

\[
\begin{aligned}
 L_{N,T}&=L_{N-1,T}+w_N(I-S_{a_N})^*(I-S_{a_N}),\\
 c_N&=c_{N-1}+2w_N.
\end{aligned}                                            \tag{2.1}
\]

Consequently

\[
 \boxed{
 H_{N,T}=H_{N-1,T}-w_NP_T(S_{a_N}+S_{-a_N})P_T.}         \tag{2.2}
\]

If \(T=T_N=a_N/2\), the overlap of \(I_T\) and \(I_T+a_N\) has measure
zero.  Hence

\[
 \langle F,S_{a_N}F\rangle=0
 \qquad(F\in L^2(I_{T_N})),                              \tag{2.3}
\]

and the new contact makes no change to the renormalized quadratic form at
birth:

\[
 H_{N,T_N}=H_{N-1,T_N}.                                  \tag{2.4}
\]

This is the basic multiscale cancellation.

## 3. Opening one threshold cell

Write \(T=T_N+\delta\).  The two boundary overlap intervals have total
length \(4\delta\).  The Fourier split used in D.60 gives, for every
\(R>0\),

\[
 |\langle F,S_{a_N}F\rangle|
 \le {2\delta R\over\pi}\|F\|^2
      +{1\over\ell_\infty(R)}
       \langle F,L_{\infty,T}F\rangle,                  \tag{3.1}
\]

where

\[
 \ell_\infty(R)
 =\operatorname{Re}\psi(1/4+iR/2)-\psi(1/4)
 =\log R+O(1).                                          \tag{3.2}
\]

Thus crossing the cell by this local estimate costs

\[
 {2w_N\over\ell_\infty(R)}                              \tag{3.3}
\]

of the available Gamma form and at most

\[
 {4w_N\delta R\over\pi}                                 \tag{3.4}
\]

of scalar gap.

Between consecutive integer thresholds,

\[
 T_{N+1}-T_N={1\over2}\log(1+1/N)=O(N^{-1}).            \tag{3.5}
\]

Only prime powers have \(w_N\ne0\), but primes alone determine whether the
budgets are summable.

## 4. Failure of a fixed Gamma-reserve induction

Suppose one tries to reserve a fixed positive fraction of
\(L_{\infty,T}\) and pay (3.3) independently at each prime.  To make the
spatial loss (3.4) summable over primes, the elementary choice

\[
 R_p\le p^{1/2-\varepsilon}                              \tag{4.1}
\]

is already near the largest polynomial scale available, because
\(w_p\asymp(\log p)/\sqrt p\) and \(\delta_p=O(1/p)\).  But (3.2) then gives

\[
 {w_p\over\ell_\infty(R_p)}\gg {1\over\sqrt p}.         \tag{4.2}
\]

The series

\[
 \sum_p{1\over\sqrt p}                                  \tag{4.3}
\]

diverges.  Hence a finite Gamma reserve is exhausted.

Conversely, making (3.3) summable requires, for example,
\(\log R_p\gg p^{1/2+\varepsilon}\).  Then \(R_p\) is exponential in a
positive power of \(p\), and

\[
 w_p\delta_pR_p                                         \tag{4.4}
\]

is not summable.  The two errors in the elementary uncertainty split cannot
be made simultaneously summable.

This no-go concerns the D.60 local estimate, not every possible capacity
argument.  It shows exactly why repeating the successful first-hinge proof
does not globalize.

## 5. The exact Schur-capacity invariant

Let the enlarged primitive window at the end of the \(N\)-th cell decompose
as

\[
 \mathcal P_{T_{N+1}}=\mathcal C_N\oplus\mathcal A_N,   \tag{5.1}
\]

where \(\mathcal C_N\) is the transported old core and \(\mathcal A_N\) is
the new two-sided annulus after imposing the two moment equations.  In this
decomposition write

\[
 H_{N,T_{N+1}}=
 \begin{pmatrix}A_N&B_N\\B_N^*&D_N\end{pmatrix}.       \tag{5.2}
\]

Assuming \(A_N\ge0\), positivity propagates if and only if

\[
 \operatorname{Ran}B_N\subseteq\operatorname{Ran}A_N^{1/2}
 \quad\text{and}\quad
 \boxed{
 \operatorname{Cap}_N:=D_N-B_N^*A_N^\dagger B_N\ge0.} \tag{5.3}
\]

This is the operator-valued shorted capacity of D.79.  It retains the whole
positive complement and does not replace the directed contact by its
operator norm.

An inductive proof of D would follow from the source-defined invariant

\[
 \boxed{
 \operatorname{Cap}_N\ge0\quad\text{for every }N,
 \text{ uniformly in the directed smoothing.}}          \tag{5.4}
\]

At a prime-power birth the direct contact part of \(D_N\) starts at zero by
(2.3); as the annulus opens, \(D_N\) contains the Gamma tail and all earlier
contacts, while \(B_N\) records the new overlap with the core.  Therefore
(5.4) is precisely the proposed statement that the Gamma/old-contact
capacity absorbs the entering A--B contact.

## 6. Why (5.4) is the missing arithmetic estimate

The finite-threshold calculations D.59--D.60 verify (5.4) at the first
hinge and on a nonempty interval beyond it.  The D.79 capacity--Feshbach
lemma gives a rigorous way to verify it from:

1. a lower bound on the complementary gap;
2. a directed upper bound on the entering residual;
3. a lower bound on the positive shorted Gamma/old-contact capacity.

What is absent globally is a uniform lower bound for item 3 after all prior
prime-power contacts have been included.  The local Gamma estimate loses a
nonsummable amount by Section 4.  Product-formula cancellation fixes the
trace of (5.2), but not its Schur complement.  Ordinary Cheeger positivity
also cannot provide (5.4), by D.120.

Moreover, (5.3) is not a weaker surrogate for D.  Iterated block
congruence shows that the family (5.4), together with the positive initial
cell, is equivalent to positivity of every \(H_{N,T_N}\), hence by (1.2) to
the row-D inequalities on the cofinal union of compact supports.

## 7. Exact conclusion

The multiscale programme reaches a sharper frontier:

\[
 \boxed{
 \text{new contact is zero at birth}
 \quad+\quad
 \text{uniform annular Schur capacity (5.4)}
 \quad\Longrightarrow\quad D.}
\]

All threshold updates, prime-power coefficients, two Tate constraints and
Gamma terms are exact.  The missing theorem is the uniform nonnegativity of
the operator-valued capacities \(\operatorname{Cap}_N\).

The elementary frequency/localization proof cannot establish it because of
the nonsummable tradeoff (4.2)--(4.4).  A successful continuation must use
joint arithmetic cancellation inside the Schur complement, rather than pay
for each prime independently from a fixed Gamma reserve.

