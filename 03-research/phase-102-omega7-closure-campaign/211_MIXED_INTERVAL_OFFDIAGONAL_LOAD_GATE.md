# Mixed-interval off-diagonal load gate

## Purpose

`197_CUMULATIVE_KERNEL_INTERVAL_FORM.md` shows that the terminal interval of
\(\mathcal H_n\) is a single Laguerre polynomial, while every earlier
interval is a cumulative mixture.  `207`--`210` then refine the terminal
absolute route.

This note isolates the remaining nonterminal obstruction for the absolute
\(L^1\) route: on \((T_j,T_{j+1})\), the kernel contains Laguerre
polynomials with degrees larger than the local cutoff index \(j\).  Thus
the A0 decay attached to \(T_j\) does not automatically control the whole
mixed load for large \(n\).

## Exact mixed load

For \(7\le j\le n-2\), `197` gives
\[
\begin{aligned}
  \mathcal H_n(u)
  &=
  u\sum_{k=j+1}^{n-1}w_{n,k}L_{k-1}^{(2)}(u)\\
  &\quad
  -1_{j\ge8}\,w_{n,j}\,j\,L_j^{(2)}(u)
  +
  w_{n,j+1}(j+2)L_{j-1}^{(2)}(u),
  \qquad T_j<u<T_{j+1}.
\end{aligned}
\tag{1}
\]

Define the mixed load
\[
\boxed{
  \mathcal M_n(\varepsilon)
  =
  \sum_{j=7}^{n-2}
  \int_{T_j}^{T_{j+1}}
  \varepsilon(u)|\mathcal H_n(u)|\,du.
}
\tag{2}
\]

The absolute diagonal theorem requires
\[
\boxed{
  \mathcal B_n
  \ge
  \mathcal M_n(\varepsilon)+\mathcal T_n(\varepsilon).
}
\tag{3}
\]

`208` controls \(\mathcal T_n\) for canonical VK cutoffs only up to a
remaining comparison with \(\mathcal B_n\).  The new problem is
\(\mathcal M_n\).

## Why A0 does not automatically control mixed intervals

On \((T_j,T_{j+1})\), the A0 condition naturally available from the cutoff
\(T_j\) is calibrated to degree \(j\)-scale kernels.  But (1) contains the
whole off-diagonal sum
\[
  u\sum_{k=j+1}^{n-1}w_{n,k}L_{k-1}^{(2)}(u),
\tag{4}
\]
including degrees \(k-1\) much larger than \(j\).

Consequently, the implication
\[
  u\ge T_j
  \quad\Longrightarrow\quad
  \varepsilon(u)
  |L_{k-1}^{(2)}(u)|
  \hbox{ is small uniformly for all }k\le n-1
\]
is false without an additional off-diagonal Laguerre estimate.  A0 supplies
decay in \(u\); it does not by itself supply cancellation or smallness for
all larger degrees appearing in (4).

This is the precise reason why controlling the terminal interval is not
enough for Theorem B of `196`.

## Sufficient off-diagonal theorem

The absolute route would pass the mixed intervals if one proved, for the
chosen PNT profile and cutoffs,
\[
\boxed{
  \mathcal M_n(\varepsilon)
  \le
  \mathcal B_n-\mathcal T_n(\varepsilon)
  \qquad(n\ge9).
}
\tag{5}
\]

Using (1), a more explicit sufficient theorem is
\[
\boxed{
\begin{aligned}
  &\sum_{j=7}^{n-2}
  \int_{T_j}^{T_{j+1}}
  \varepsilon(u)
  \Bigg|
  u\sum_{k=j+1}^{n-1}w_{n,k}L_{k-1}^{(2)}(u)
  -1_{j\ge8}w_{n,j}jL_j^{(2)}(u)\\
  &\hspace{35mm}
  +w_{n,j+1}(j+2)L_{j-1}^{(2)}(u)
  \Bigg|\,du
  \le
  \mathcal B_n-\mathcal T_n(\varepsilon).
\end{aligned}
}
\tag{6}
\]

This is not a new formulation of A1; it is the exact remaining sufficient
condition for the absolute route after the terminal audits.

## Crude triangle route and its cost

If one applies the triangle inequality inside (1), then (6) is implied by
\[
\begin{aligned}
  &\sum_{j=7}^{n-2}
  \int_{T_j}^{T_{j+1}}
  \varepsilon(u)
  \left[
    u\sum_{k=j+1}^{n-1}w_{n,k}|L_{k-1}^{(2)}(u)|
    +1_{j\ge8}w_{n,j}j|L_j^{(2)}(u)|
    +w_{n,j+1}(j+2)|L_{j-1}^{(2)}(u)|
  \right]du\\
  &\hspace{35mm}
  \le
  \mathcal B_n-\mathcal T_n(\varepsilon).
\end{aligned}
\tag{7}
\]

This is a valid but stronger requirement.  It discards possible
cancellations among the Laguerre mixture in (1), just as the absolute route
already discards the arithmetic sign of \(E\).

Thus a successful proof must choose between:

1. a sharp mixed-polynomial \(L^1\) theorem for (1);
2. a cruder but strong enough off-diagonal Laguerre bound for (7);
3. a return to a signed proof of A1, avoiding the absolute loss.

## Exact remaining theorem

After `207`--`210`, Theorem B of `196` is equivalent to proving all three
items:

1. a positive lower bound for the full budget \(\mathcal B_n\);
2. terminal domination, for example via the VK estimate of `208`;
3. the mixed off-diagonal domination (5) or (6).

No one of these three implies the others.

## Status

Closed as the mixed-interval off-diagonal load gate.

A1 remains open.  The terminal interval is no longer the only obstruction
in the absolute route; the earlier cumulative Laguerre mixtures require a
separate uniform \(L^1\) theorem or a signed replacement.
