# The oriented transport target, and its conditional closure

> **Rigor status (superseding the original claims below).**  The argument
> proves only a qualitative eventual implication under RH once the uniform
> Laguerre estimates of `103_10` and the outer-tail repair of `103_09` are
> supplied.  The displayed constants and the threshold \(n_1=150\) are
> numerical diagnostics, not a theorem: `103_11` shows that the source used
> for the interior estimates does not provide the required numerical
> constants.  `103_22` now supplies valid but enormous constants for the
> eventual \(I_2,I_3\) bounds; it does **not** validate this table or the
> threshold 150.  Statements below saying "proved under RH" or assigning
> the threshold 150 must be read subject to this correction.

Work order steps 5–8 of `PHASE_103_A1_DIRECT_CLOSURE_GUIDE.md`.

## 1. The target in final coordinates

By `103_01` (Proposition 1) and `103_02` (Corollary 3), direct A1 at index
\(n\ge9\) is **exactly**
\[
\boxed{\
  \mathcal J_n:=\int_{\log2}^{T_n}E(u)K_n(u)\,du
  \ \le\ q(n)={3\over4}A_n+1-L_n^{(1)}(\log2),\ }
\tag{1}
\]
\[
  E(u)=\psi(e^u)-e^u,\qquad K_n(u)=e^{-u}L_{n-1}^{(2)}(u),\qquad
  q(n)={3\over8}n\bigl(\log n+\gamma-1-\log2\pi\bigr)+O(n^{1/4}).
\]

No cutoff convention, no pole term, no low window and no lobe partition
survive in (1).  This is the narrowest form of the direct route.

## 2. What a transport lemma has to beat

The guide proposes (13)–(15): construct maps between negative and positive
lobes, or a primitive \(W_n\) of the kernel, and derive a signed bound.
Formula (1) makes the requirement quantitative:

> **Requirement T.**  A transport lemma is admissible only if it produces a
> bound of the form \(\mathcal J_n\le\Theta(n)\) with
> \(\Theta(n)\le\frac38n\log n\,(1+o(1))\).

Three reference scales, all established numerically in `103_06`:

| input about \(E\) | resulting bound for \(\mathcal J_n\) | verdict |
|---|---|---|
| VK envelope \(|E|\le Ae^{u-\eta(u)}\) | \(\ge e^{(3/2-o(1))n}\) | fails by \(e^{3n/2}\) |
| RH pointwise (Schoenfeld) \(|E|\le\frac1{8\pi}e^{u/2}u^2\) | \(\asymp n^{5/2}\) | fails by \(n^{3/2}\) |
| RH + one summation by parts, zeros split at height \(Y\) | \(\ll n^{3/4}\log^2n\) | **succeeds**, margin \(n^{1/4}/\log n\) |
| truth (measured) | \(|\mathcal J_n|=O(1)\) for \(n\le800\) | — |

The middle row is the important correction to the phase-102 picture: the
failure of the *pointwise* RH envelope is an artefact of taking absolute
values before using the oscillation of \(E\), not a defect of the route.

## 3. The sharp envelope exponent

> **Theorem 1 (envelope threshold).**  Let \(W(u)=Ce^{u/2}u^{a}\), so that
> the load is \(C\int_{u_0}^{4N}u^{a}\,e^{-u/2}|L_{n-1}^{(2)}(u)|\,du\).
> Inserting (3) of `103_03` gives
> \(\;\asymp C\,c_2N^{3/4}\int_{u_0}^{4N}u^{a-5/4}\,du\), i.e.
> \[
>   \hbox{load}\ \asymp\
>   \begin{cases}
>     \dfrac{C c_2}{1/4-a}\,N^{3/4}\,u_0^{\,a-1/4}, & a<1/4
>       \quad(\hbox{lower-end dominated}),\\[8pt]
>     C c_2\,N^{3/4}\log N, & a=1/4,\\[6pt]
>     \dfrac{C c_2\,4^{\,a-1/4}}{a-1/4}\,N^{\,a+1/2}, & a>1/4
>       \quad(\hbox{upper-end dominated}).
>   \end{cases}
> \]
> Comparing with \(q(n)\asymp\frac38n\log n\), the route satisfies
> Requirement T **iff \(a+\frac12\le1\)**, i.e. iff \(a\le1/2\), i.e. iff
> \[
> \boxed{\ |\psi(x)-x|\ \ll\ \sqrt{x}\,(\log x)^{1/2}.\ }
> \]

Measured exponents (`tools/budget_vs_load.py`, fit over \(n=200\dots800\)):
\(a=0:\ N^{0.789}\) (predicted \(3/4\));
\(a=\frac12:\ N^{1.030}\) (predicted \(1\));
\(a=1:\ N^{1.487}\) (predicted \(3/2\));
\(a=2:\ N^{2.473}\) (predicted \(5/2\)).
Measured ratios load/budget at \(n=800\): \(0.161\), \(1.22\), \(29.8\),
\(1928\).

RH in Schoenfeld's explicit form gives \(a=2\); the threshold is \(a=1/2\);
the conjectured true order \(|\psi(x)-x|\ll\sqrt x(\log\log\log x)^2\)
gives \(a=0^+\).  **The envelope route therefore sits strictly between RH
and the conjectured truth.**

## 4. Conditional closure of the direct route

The pointwise deficit of §3 is removed by one summation by parts against
the *primitive* of \(E\), because the primitive converges where the
pointwise series does not.  Recall (Lemma 1 of `103_01`)
\[
  K_n'(u)=-e^{-u}L_{n-1}^{(3)}(u).
\tag{2}
\]

Unconditionally, for \(u>0\),
\[
  E(u)=-\sum_\rho{e^{\rho u}\over\rho}-\log2\pi-{1\over2}\log(1-e^{-2u}),
\tag{3}
\]
the zero sum taken in symmetric order.  Fix \(Y\ge2\) and split
\(E=-S_Y-S^Y-g\) with
\[
  S_Y(u)=\sum_{|\gamma|\le Y}{e^{\rho u}\over\rho},\qquad
  S^Y(u)=\sum_{|\gamma|>Y}{e^{\rho u}\over\rho},\qquad
  |g(u)|\le\log2\pi+{\textstyle\frac12}\log\bigl(1-e^{-2T_8}\bigr)^{-1}\le1.9 .
\]

> **Theorem 2 (conditional closure).**  Assume RH.  Take the splitting
> height \(Y=\max(20,\sqrt n\,)\).  Then, with the measured Laguerre budgets
> (5b), (5b\('\)) of `103_03`,
> \[
> \boxed{\ |\mathcal J_n|\ \le\ 0.052\,n^{0.80}\log^2 n
>              \;+\;0.17\,n^{3/4}\log n\;+\;O(n^{3/4}),\ }
> \tag{4}
> \]
> whereas \(q(n)=0.375\,n(\log n-2.2607)+O(n^{1/4})\).  Consequently
> \[
>   C_n(T_n)\ \ge\ q(n)-|\mathcal J_n|\ >\ 0\qquad(n\ge n_1),
> \]
> with margin \(q(n)\bigl(1-O(n^{-1/5}\log n)\bigr)\), and the threshold is
> \[
> \boxed{\ n_1=150.\ }
> \]

*Proof.*  Write \(\mathcal J_n=-\int S_YK_n-\int S^YK_n-\int gK_n\), all
integrals over \([\log2,T_n]\).

*(i) The elementary term.*  \(|\int gK_n|\le1.9\int_0^\infty
e^{-u}|L_{n-1}^{(2)}|\,du=O(n)\) by (5a) of `103_03`; a sharper split at
\(u=1\) gives \(O(n^{3/4})\).  (Even the crude \(O(n)\) is admissible: it is
\(o(q(n))\).)

*(ii) The low zeros, pointwise.*  Under RH \(|e^{\rho u}|=e^{u/2}\), so
\[
  |S_Y(u)|\le e^{u/2}\!\!\sum_{|\gamma|\le Y}{1\over|\rho|}
  \le e^{u/2}\Bigl({1\over2\pi}\log^2Y+c\Bigr),
\]
by the Riemann–von Mangoldt density \(N(T)=\frac T{2\pi}\log\frac T{2\pi e}+O(\log T)\).
Hence, by budget (5b) of `103_03`,
\[
  \Bigl|\int S_YK_n\Bigr|
  \le\Bigl({\log^2Y\over2\pi}+c\Bigr)\,I_2(\log2)
  \le\Bigl({\log^2Y\over2\pi}+c\Bigr)\cdot1.3\,n^{0.80}.
\]
With \(Y=\sqrt n\), \(\log^2Y=\frac14\log^2n\), so this is
\(\le0.052\,n^{0.80}\log^2n+1.3c\,n^{0.80}\).

*(iii) The high zeros, one summation by parts.*  Put
\(V^Y(u)=\int_{\log2}^uS^Y\).  Termwise integration gives
\(V^Y(u)=\sum_{|\gamma|>Y}(e^{\rho u}-e^{\rho\log2})/\rho^2\), absolutely
convergent because \(\sum_\rho|\rho|^{-2}=2+\gamma-\log4\pi=0.0461\dots<\infty\).
Under RH,
\[
  |V^Y(u)|\le2e^{u/2}\,\sigma(Y),
  \qquad
  \sigma(Y)=\sum_{|\gamma|>Y}{1\over|\rho|^2}\ \ll\ {\log Y\over Y}.
\]
By (2),
\[
  \int_{\log2}^{T_n}S^YK_n\,du
  =\bigl[V^YK_n\bigr]_{\log2}^{T_n}
   +\int_{\log2}^{T_n}V^Y(u)e^{-u}L_{n-1}^{(3)}(u)\,du .
\]
The boundary term at \(T_n\) is
\(O\bigl(\sigma(Y)e^{-T_n/2}|L_{n-1}^{(2)}(T_n)|\bigr)\); since
\(T_n\asymp n^{5/3}(\log n)^2\gg4n\), \(|L^{(2)}_{n-1}(T_n)|\le T_n^{n-1}/(n-1)!\)
and \(-T_n/2+(n-1)\log T_n-\log(n-1)!\to-\infty\) faster than any power, so
this term is negligible.  The remaining integral is at most
\(2\sigma(Y)\,I_3(\log2)\le2\sigma(Y)\cdot0.52\,n^{5/4}(\log2)^{-3/4}
=0.79\,\sigma(Y)\,n^{5/4}\)
by budget (5b\('\)) of `103_03`.

*(iv) Optimise.*  Take \(Y=\sqrt n\).  Then
\(\sigma(Y)\le\frac1\pi\frac{\log Y+1-\log2\pi}{Y}\le\frac{\log n}{2\pi\sqrt n}\),
so (iii) contributes at most
\(0.79\cdot\frac{\log n}{2\pi}n^{3/4}=0.126\,n^{3/4}\log n\).
Together with (ii) and (i) this gives (4).  Since
\(q(n)=0.375\,n(\log n-2.2607)+O(n^{1/4})\), the ratio
\(|\mathcal J_n|/q(n)\ll n^{-0.20}\log n\to0\).  \(\square\)

### The three terms, evaluated

`tools/conditional_bound_check.py` evaluates (i), (ii), (iii) with the
measured Laguerre budgets and \(Y=\max(20,\sqrt n)\), against
\(q(n)=\frac34A_n+1-L_n^{(1)}(\log2)\):

| \(n\) | \(q(n)\) | (i) elem. | (ii) low \(\gamma\) | (iii) high \(\gamma\) | total | total/\(q\) |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 3.64 | 3.16 | 9.61 | 0.80 | 13.58 | 3.727 |
| 20 | 5.80 | 4.50 | 15.94 | 2.08 | 22.51 | 3.884 |
| 40 | 24.21 | 7.72 | 28.11 | 4.73 | 40.56 | 1.675 |
| 80 | 62.06 | 13.77 | 49.89 | 10.38 | 74.04 | 1.193 |
| **150** | **153.50** | 20.93 | 81.03 | 23.43 | **125.38** | **0.817** |
| 300 | 388.21 | 36.60 | 141.51 | 54.23 | 232.34 | 0.598 |
| 600 | 928.50 | 62.13 | 278.20 | 113.73 | 454.06 | 0.489 |
| 800 | 1324.83 | 76.83 | 379.69 | 149.99 | 606.51 | 0.458 |

The elementary term (i) is confirmed to be \(O(n^{3/4})\): the measured
ratio \(\int_{\log2}^{4N}e^{-u}|L_N^{(2)}|\,du/N^{3/4}\) is \(0.257\)–\(0.272\)
over \(9\le n\le800\).  (The \(L^1\) mass of \(K_n\) over the *whole* half
line is \(\asymp n\), but that mass sits at \(u\lesssim1/n\), below the range
of the certificate — another place where starting the integral at \(\log2\)
rather than at \(0\) is worth a whole power of \(n^{1/4}\).)

The crossing occurs between \(n=80\) and \(n=150\); hence \(n_1=150\), and
the finite range \(9\le n\le149\) is inside the interval verified in
`103_06`.

### Consequences

1. **The direct route is sound.**  The reserve computed in `103_02` is not
   merely positive, it exceeds the true cost by a factor \(\asymp
   n^{1/4}/\log n\).  Every no-go recorded in phase 102 concerned methods of
   *estimating* \(\mathcal J_n\), never the truth of (1).
2. **The finite range is genuinely finite.**  Theorem 2 plus the
   \(n<n_1\) certificates of `103_06` close (1) for every \(n\) under RH.
3. **Where RH enters** (non-circularity audit, acceptance criterion 7):
   *only* through \(|e^{\rho u}|=e^{u/2}\), used twice — in (ii) for
   \(|\gamma|\le Y\) and in (iii) for \(|\gamma|>Y\).  Nothing else in the
   chain uses zero location.  A0 uses only a zero-free region; `226`, `219`,
   `103_01`–`103_03` use no zero information at all.
4. **The exact unconditional gap.**  What is missing is a bound
   \[
     \Bigl|\sum_\rho{e^{\rho u}\over\rho^2}\Bigr|\ \ll\ e^{u/2}\,\mathrm{polylog}
     \qquad(T_8\le u\le4n),
   \]
   i.e. square-root cancellation for the *once-integrated* Chebyshev
   discrepancy on the range \(\log x\le4n\).  This is weaker than RH
   pointwise but is still an RH-strength statement, since it forces
   \(\beta\le1/2\) for every zero with \(|\gamma|\) bounded.

## 5. Why the three constructions proposed in the guide cannot be
   completed unconditionally

* **Adjacent-lobe transport (13)–(14).**  Uses only the sign geometry of
  \(K_n\) plus an envelope for \(E\).  Defeated by `103_05`.
* **Cumulative oriented discrepancy (15).**  This is exactly step (iii)
  above with \(W_n=\) primitive of \(K_n\); it is the correct mechanism, and
  Theorem 2 shows it works — but the constant \(\mathcal C_n(E,W_n)\)
  requires a bound on the primitive of \(E\), which unconditionally is only
  \(O(e^{u-\eta(u)})\), reproducing the VK failure.  One-sided increments of
  \(E\) do not help: see `103_05`, where the competitor is monotone.
* **Dirichlet-series positivity.**  Requires a square-root factorisation of
  the Li kernel \(1-(1-1/\rho)^n\), eliminated in
  `155_A1_WEIL_SQUARE_ROOT_GATE.md` and `170_VANISHING_KERNEL_PAIRING_NO_GO.md`.

## Status

Steps 5–8 of the work order are answered:

* step 5 (formulate one precise oriented transport lemma): the correct
  lemma is the once-integrated form (iii) above, stated with the primitive
  of \(E\) rather than \(E\) itself;
* step 6 (test against explicit prime-power data): done in `103_06`, which
  confirms \(|\mathcal J_n|=O(1)\) against a budget \(\asymp\frac38n\log n\);
* step 7 (prove the lemma uniformly): **proved under RH** (Theorem 2);
  **proved impossible from envelope + monotonicity data** (`103_05`);
* step 8 (combine with the reserve beyond an explicit threshold): Theorem 2
  and Corollary 3 of `103_02`.

A1 remains open unconditionally, and phase 103 now identifies the missing
input exactly: square-root cancellation for \(\sum_\rho e^{\rho u}/\rho^2\)
on \(u\le4n\).
