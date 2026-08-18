# 109.03 — Step 3 (signature): skipped, and why

## 0. The gate

The mission is explicit: Step 3 (compute the inertia $(n_+,n_-)$ of $B$ on
the quotient by its radical, in the style of 107_241 Theorem 3.1) is to be
attempted **only if Step 2 comes out zero-determined**. 109_02 Corollary 4.1
found:

$$\mathrm{rad}\,B=\mathcal V_{PP}=\{f\in\mathcal G_B:\ f(p^k)=0\ \forall
p\text{ prime},k\ge1\},$$

a description in terms of vanishing at the prime powers, with an explicit
proof (109_02 Theorem 3.3) that this space is **not** contained in the
zero-determined space $\{f:\hat f(\rho)=0\ \forall\text{ zeros }\rho\text{
of }\xi\}$: the witness $F(x)=\sin(\pi x)$ lies in $\mathrm{rad}\,B$ while
its (continued) Mellin transform $\hat F(s)=\pi^{-s}\Gamma(s)\sin(\pi s/2)$
is zero-free on the *entire* zero set of $\xi$.

So Step 2's outcome is the refutation branch, not the confirmation branch.
Per the mission's own gating rule, **Step 3 is skipped.**

## 1. Why an inertia computation would not answer anything here

It is worth stating precisely why this is not merely a bureaucratic
skip, in case a computation were attempted anyway.

107_241's signature computation is meaningful because Stage 0's radical is
*exactly* the "trivial" directions of the pairing in the eigenbasis given by
evaluation at $\{0,1,\rho\}$ — i.e. once you quotient by $\mathrm{rad}\,I_{
\mathrm{partial}}$, the residual pairing is diagonal in a basis indexed by
zeros of $\xi$ (plus the two boundary points), and $(n_+,n_-)$ counts how
many of those diagonal blocks are positive/negative, blockwise, in terms of
mirror pairs of zeros. That is a spectral statement: it presupposes the
quotient is organized *by zeros of $\xi$*.

Here, the quotient $\mathcal G_B/\mathrm{rad}\,B$ is organized instead by
**evaluation at prime powers** ($B$ is diagonal in the basis of point masses
at $\{2,3,4,5,7,8,9,11,\dots\}$, weighted by $\Lambda$, as its closed form
$B(f,g)=\sum_n\Lambda(n)f(n)g(n)$ makes manifest). An "inertia" of this
quotient is computable, trivially and without content: on the basis of
point masses $\delta_n$ at prime powers, $B(\delta_n,\delta_n)=\Lambda(n)>0$
for every $n$, so the diagonal form is **positive definite** on that
quotient, full stop — $n_+=\infty$ (countably many positive directions),
$n_-=0$. This is not a typo or a degenerate edge case: it follows
immediately from $\Lambda(n)>0$ for all prime powers $n$ and the pairing's
own closed form, with no computation beyond reading off the sign of
$\Lambda$.

That number carries **no information about row (d)**, because it says
nothing about zeros of $\xi$ — it is exactly as informative as noting that
$\sum_n\Lambda(n)|c_n|^2\ge0$ for any sequence $(c_n)$, which is a fact
about the weight $\Lambda(n)>0$, not about $\zeta$'s analytic structure.
Reporting "$(n_+,n_-)=(\infty,0)$, computed non-circularly" would be true,
but it would be exactly the kind of statement the mission's anti-circularity
clause warns against: technically correct, mathematically empty, because it
was never at risk of coming out any other way once $B$'s diagonal structure
(109_01 Lemma 1.4) and $\Lambda(n)>0$ are on the table. A signature
computation is only worth doing when Step 2 hands it a spectral
decomposition tied to zeros of $\xi$ to be signed block by block (as in
107_241); it is not worth doing here, and doing it anyway would manufacture
the appearance of a positive result out of a closed route.

## 2. Verdict

Step 3: **skipped**, correctly, per the mission's own gate. No `.py` is
attached, since no claim is made that needs a numerical check — attaching a
verifier here would itself violate the instruction never to write a check
that can pass unconditionally: the one computation available
($(n_+,n_-)=(\infty,0)$ from $\Lambda(n)>0$) is unconditionally true by
construction and would tell a reader nothing about whether it passed for a
substantive reason.

## 3. Scope

**Proved here:** the elementary remark that $B$ restricted to
$\mathcal G_B/\mathrm{rad}\,B$ is positive definite in the prime-power basis
(one line, from $\Lambda(n)>0$), offered only to explain *why* a formal
inertia number would be contentless, not as a result toward row (d).

**Not established, and explicitly not claimed:** any inertia computation
tied to zeros of $\xi$; any statement about row (d); anything about RH.
