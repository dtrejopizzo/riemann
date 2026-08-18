# 108.35 — The normalization producing $\log p$, and the Weil coefficient

## 0. Result

108_34 constructs $\Gamma_{p,k}$ and proves the pairing formula in 108_06's
unit-mass normalization, where every shell has $d^\times u$-mass $1$ and **no
factor $\log p$ appears**.  The Weil coefficient carries one.  This note
fixes the normalization, and the coefficient then comes out exactly.

No zero of $\xi$ enters any definition.

## 1. The two normalizations

**(N1) Unit mass** (used in 108_06 and 108_34).  Normalize $d^\times u$ on
$\mathbb Q_p^\times$ by $\mathrm{vol}(\mathbb Z_p^\times)=1$.  Then each
shell $p^n\mathbb Z_p^\times$ has mass $1$, and
\[
 \Gamma_{p,k}(f_s)=p^{-ks}\quad(k\ge1).
\]

**(N2) Adelic / Tate.**  Normalize instead so that the valuation map
$|\cdot|_p:\mathbb Q_p^\times\to p^{\mathbb Z}$ pushes $d^\times u$ to the
measure assigning $\log p$ to each step of the value group.  This is the
normalization under which the finite places are commensurate with the
archimedean one, where the value group is $\R_{>0}$ with $dt/t$ and a
"step" is continuous.  Then each shell has mass $\log p$ and
\[
 \Gamma^{\mathrm{Tate}}_{p,k}=(\log p)\,\Gamma_{p,k},
 \qquad
 \Gamma^{\mathrm{Tate}}_{p,k}(f_s)=(\log p)\,p^{-ks}.
\]

We adopt **(N2)**, because it is the normalization in which the local terms
of Weil's explicit formula are stated, and because (N1) cannot produce
$\log p$ by any rescaling of $\Gamma_{p,k}$ that is uniform in $p$.

## 2. The Weil coefficient

> ### Theorem 2.1
> At the central weight $s=\tfrac12$,
> \[
>  \boxed{\;\Gamma^{\mathrm{Tate}}_{p,k}(f_{1/2})
>  =(\log p)\,p^{-k/2}
>  =\frac{\Lambda(p^{k})}{\sqrt{p^{k}}}\;}
> \]
> for every prime $p$ and every $k\ge1$, where $\Lambda$ is the von Mangoldt
> function.

**Proof.**  By 108_34's pairing formula in (N2),
$\Gamma^{\mathrm{Tate}}_{p,k}(f_s)=(\log p)p^{-ks}$; put $s=\tfrac12$.  Since
$\Lambda(p^k)=\log p$ and $\sqrt{p^k}=p^{k/2}$, the right-hand side is
$\Lambda(p^k)/\sqrt{p^k}$. $\square$

Verified to machine precision for $p\in\{2,3,5,7,11\}$ and $k\in\{1,2,3\}$.

> ### Corollary 2.2
> The mirror shells $k\le-1$ give, at $s=\tfrac12$, the same value
> $(\log p)p^{-|k|/2}$.  These are the $h(p^{k})$ and $h(p^{-k})$ terms of the
> Weil local term
> $W_p(h)=(\log p)\sum_{k\ge1}p^{-k/2}\big[h(p^{k})+h(p^{-k})\big]$,
> which is therefore recovered term by term.

**Proof.**  $\Gamma_{p,-m}(f_s)=p^{m(s-1)}$, which at $s=\tfrac12$ is
$p^{-m/2}$. $\square$

The coincidence of the two families at $s=\tfrac12$ is exactly the fixed-point
property of the mirror involution recorded in the Stage-0 signature analysis.

## 3. Scope

Proved: Theorem 2.1 and Corollary 2.2 in normalization (N2); the explicit
statement of both normalizations and the reason for adopting (N2).

Not established: that (N2) is forced rather than conventional — it is the
standard adelic choice and the one in which the explicit formula is stated,
but no uniqueness theorem is proved here; and nothing about the archimedean
place, which is Stage 4.

`ROW_A_STATUS` unchanged.  Nothing here bears on RH.

## 4. Verifier

`108_35_the_log_p_normalization.py` checks the identity of Theorem 2.1 for
five primes and three exponents to machine precision, the mirror statement of
Corollary 2.2, and that normalization (N1) does **not** produce the Weil
coefficient.
