# 104_31 — \(\varepsilon\)-flow and the observability stop-gate at \(1/2\)

**Role.** Audit the attempt to start from a regulator where the Euler
operator converges in norm and transport the hard-edge test backward via the
tridiagonal Laguerre recurrence. The flow is exact and has a very simple
unitary realization: its generator is minus multiplication by \(x\).
Precisely that realization fixes a sharp threshold. The backward-transported
test belongs to the Laguerre space if and only if
\(\varepsilon<1/2\), while the Euler sum as a bounded operator converges in
norm only for \(\varepsilon>1/2\). The point \(1/2\) belongs to neither
domain.

The positive metric \(A_{\rm flag}\), which does exactly interpolate
\(A_{\rm flag}[g_n]=A_n\) for \(n\ge150\), does not remove the collision.
Its space is not invariant under the generator, the generator is not
symmetric for that metric, and even after compressing, the weights
\(\Delta A_k\asymp\log k\) do not change the exponential radius that
produces the threshold.

This document is a stop-gate for **this specific combination**:
"bounded Euler operator + backward Hilbert transport." It does not rule out
a signed renormalized identity in distribution duality, does not prove A1,
and does not prove RH.

## 1. Exact flow of the regulated coefficients

For \(\varepsilon>0\), let

\[
 p_n(\varepsilon)=
 \sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}L_n(\log m),
 \qquad
 j_n(\varepsilon)={ (\varepsilon-1)^n\over\varepsilon^{n+1}},
 \qquad
 c_n=p_n-j_n .                                             \tag{1}
\]

The series obtained by differentiating (1) converge absolutely on every
half-plane \(\varepsilon\ge\varepsilon_0>0\). The ordinary recurrence

\[
 -xL_n(x)=(n+1)L_{n+1}(x)-(2n+1)L_n(x)+nL_{n-1}(x),          \tag{2}
\]

with \(L_{-1}=0\), gives

\[
 p_n'=(n+1)p_{n+1}-(2n+1)p_n+np_{n-1}.                      \tag{3}
\]

The polar term is not an external correction to the flow. It has the
representation

\[
 j_n(\varepsilon)=\int_0^\infty e^{-\varepsilon x}L_n(x)\,dx,             \tag{4}
\]

and by (2) satisfies the same equation. Equivalently, a direct computation
gives

\[
 j_n'={ (\varepsilon-1)^{n-1}\over\varepsilon^{n+2}}
       (n+1-\varepsilon)
 =(n+1)j_{n+1}-(2n+1)j_n+nj_{n-1}.                           \tag{5}
\]

Hence, for every \(n\ge0\), with \(c_{-1}=0\),

\[
 \boxed{c_n'=(n+1)c_{n+1}-(2n+1)c_n+nc_{n-1}.}               \tag{6}
\]

The limit \(\varepsilon\downarrow0\) was not separated out: (6) holds
before the pole–prime collision.

## 2. Unitary realization: \(Q=-M_x\)

Let

\[
 \mathcal H=L^2((0,\infty),e^{-x}dx).
\]

The polynomials \(L_0,L_1,\ldots\) are an orthonormal basis of
\(\mathcal H\). The map

\[
 U:\ell^2(\mathbb N_0)\longrightarrow\mathcal H,
 \qquad Ua=\sum_{n\ge0}a_nL_n                                  \tag{7}
\]

is unitary. If \(X=M_x\), with domain

\[
 \mathcal D(X)=\{f\in\mathcal H:xf\in\mathcal H\},
\]

then (2) proves

\[
 U^{-1}(-X)U=Q,
 \qquad
 (Qa)_n=(n+1)a_{n+1}-(2n+1)a_n+na_{n-1}.                    \tag{8}
\]

So \(Q\) is self-adjoint, non-positive, has spectrum
\(( -\infty,0]\), and

\[
 Ue^{tQ}U^{-1}=M_{e^{-tx}}\qquad(t\ge0).                    \tag{9}
\]

The complete sequence \(c(\varepsilon)\) is not claimed here to be a
vector in \(\ell^2\): the prime atoms naturally define a more singular
functional. Equations (7)–(9) say what a Hilbert implementation of the
weak transport would require. For a finite test \(a\), transporting from
\(\varepsilon\) down to zero requires moving the test via the adjoint:

\[
 \langle a,c(0)\rangle
 =\langle e^{-\varepsilon Q}a,c(\varepsilon)\rangle,
 \qquad
 Ue^{-\varepsilon Q}a=e^{\varepsilon x}Ua,                   \tag{10}
\]

if the right-hand side belongs to the domain of the duality used.

## 3. Sharp threshold of the hard-edge prefix

The prefix vector of `104_28` is

\[
 u_n=(\underbrace{1,\ldots,1}_{n},0,\ldots),
 \qquad
 Uu_n=P_n(x):=L_{n-1}^{(1)}(x)=\sum_{k=0}^{n-1}L_k(x).        \tag{11}
\]

Since \(P_n\) is a nonzero polynomial of degree \(n-1\), with leading
coefficient \((-1)^{n-1}/(n-1)!\),

\[
 \|e^{\varepsilon x}P_n\|_{\mathcal H}^2
 =\int_0^\infty |P_n(x)|^2e^{-(1-2\varepsilon)x}\,dx.        \tag{12}
\]

Hence

\[
 \boxed{e^{\varepsilon x}P_n\in\mathcal H
        \quad\Longleftrightarrow\quad\varepsilon<\tfrac12.} \tag{13}
\]

At the boundary \(\varepsilon=1/2\), what remains is the integral of a
squared polynomial; above the boundary, exponential growth appears. The
blow-up from below is likewise exact to leading order. If
\(\delta=1-2\varepsilon\downarrow0\), then

\[
 \boxed{
 \|e^{\varepsilon x}P_n\|_{\mathcal H}^2
 \sim { (2n-2)!\over((n-1)!)^2}\,\delta^{-(2n-1)}
 = {2n-2\choose n-1}\delta^{-(2n-1)}.}                       \tag{14}
\]

So (13) is not a constant-factor loss: it is the maximal domain of the
inverse semigroup for this test function.

## 4. The safe Euler domain touches the boundary from the other side

In the translation realization of `104_28`, the sum one would want to
build before evaluating on \(g_n\) is

\[
 \mathcal E_\varepsilon
 =\sum_{m\ge2}{\Lambda(m)\over m^{1/2+\varepsilon}}
       (S_{\log m}+S_{\log m}^*).                             \tag{15}
\]

For the one-sided translation, \(\|S_a\|=1\) and
\(\|S_a+S_a^*\|=2\). In particular, the term-by-term norm construction is
governed by

\[
 \sum_{m\ge2}{\Lambda(m)\over m^{1/2+\varepsilon}},          \tag{16}
\]

which converges exactly when \(1/2+\varepsilon>1\). Even without
requiring absolute convergence, the positive summands do not give norm
convergence at the boundary: testing the partial sums on functions nearly
constant over intervals much longer than every \(\log m\) present, their
norm is arbitrarily close to twice the corresponding scalar sum. Hence,

\[
 \boxed{\mathcal E_\varepsilon\text{ converges in norm via this sum}
        \quad\Longleftrightarrow\quad\varepsilon>\tfrac12.}  \tag{17}
\]

The inequality is **strict**. At \(\varepsilon=1/2\),
\(\sum\Lambda(m)/m\) appears, which diverges. Combining (13) and (17),

\[
 \{\varepsilon:\text{admissible backward test}\}=(0,1/2),
 \qquad
 \{\varepsilon:\text{safe Euler operator}\}=(1/2,\infty),             \tag{18}
\]

and the apparent common point belongs to neither.

This does not contradict (6b) of `104_28`: after evaluating on ray
\(g_n\), the overlap supplies another factor \(m^{-1/2}\), and the
**scalar form** converges for every \(\varepsilon>0\). What (18) rules out
is separating it first as a bounded operator and then recovering the
boundary via Hilbert transport.

## 5. Audit of the metric \(A_{\rm flag}\)

Set \(M=150\), \(P_M=\sum_{j<M}L_j\), and

\[
 \mathcal H_{\rm flag}
 =\mathrm{span}\,\{P_M,L_M,L_{M+1},\ldots\}\subset\mathcal H.        \tag{19}
\]

The family shown in (19) is orthogonal in \(\mathcal H\). With
\(d_k=\Delta A_k=A_{k+1}-A_k\), define

\[
 \left\|a_0P_M+\sum_{k\ge M}a_kL_k\right\|_{A_{\rm flag}}^2
 =A_M|a_0|^2+\sum_{k\ge M}d_k|a_k|^2.                         \tag{20}
\]

Since \(d_k>0\) well before \(M\), (20) is positive. Moreover,

\[
 P_n=P_M+\sum_{k=M}^{n-1}L_k,
 \qquad
 \boxed{\|P_n\|_{A_{\rm flag}}^2
 =A_M+\sum_{k=M}^{n-1}\Delta A_k=A_n.}                       \tag{21}
\]

Identity (21) genuinely fixes the absence of a positive reference noted in
`104_28`. It is not, however, enough to transport (6).

### 5.1 The flag is not invariant under \(Q\)

Telescoping (2) gives

\[
 QP_M=M(L_M-L_{M-1}).                                         \tag{22}
\]

If \(\Pi_{\rm flag}\) is the orthogonal projection of \(\mathcal H\) onto
(19), then \(\Pi_{\rm flag}L_{M-1}=P_M/M\), and

\[
 \Pi_{\rm flag}QP_M=-P_M+ML_M,                               \tag{23}
\]

\[
 (I-\Pi_{\rm flag})QP_M=P_M-ML_{M-1},
 \qquad
 \boxed{\|(I-\Pi_{\rm flag})QP_M\|_{\mathcal H}^2=M(M-1).} \tag{24}
\]

For \(M=150\), the quadratic leak is \(22350\). Hence the restriction
\(Q|_{\mathcal H_{\rm flag}}\) does not exist as a generator of the exact
flow. Compressing it eliminates (24) and changes the dynamics at the
boundary.

### 5.2 The compression is not unitary for \(A_{\rm flag}\) either

Let \(Q_{\rm flag}=\Pi_{\rm flag}Q\Pi_{\rm flag}\). Its first rows are

\[
 \begin{aligned}
 Q_{\rm flag}P_M&=-P_M+ML_M,\\
 Q_{\rm flag}L_M&=P_M-(2M+1)L_M+(M+1)L_{M+1}.
 \end{aligned}                                                \tag{25}
\]

In the tail it keeps the ordinary tridiagonal matrix. But (20) gives

\[
 \langle Q_{\rm flag}P_M,L_M\rangle_A
 -\langle P_M,Q_{\rm flag}L_M\rangle_A
 =M\Delta A_M-A_M>0,                                         \tag{26}
\]

because \(A_0=0\) and \(\Delta^2A_j>0\) make
\(\Delta A_j\) strictly increasing. For \(k\ge M\),

\[
 \langle QL_k,L_{k+1}\rangle_A-
 \langle L_k,QL_{k+1}\rangle_A
 =(k+1)(\Delta A_{k+1}-\Delta A_k)
 =(k+1)\Delta^2A_k>0.                                        \tag{27}
\]

So changing the metric destroys the self-adjointness that justified
moving the semigroup back and forth in (10). Re-symmetrizing (25) would
change its rates and would no longer realize recurrence (6).

### 5.3 Even the projected version keeps the \(1/2\) threshold

There is a more favorable test: ignore the finite-dimensional leak and ask
only whether the Laguerre tail of \(e^{\varepsilon x}P_n\) has norm (20).
For \(0\le\varepsilon<1\), let

\[
 a_k^{(n)}(\varepsilon)
 =\int_0^\infty e^{-(1-\varepsilon)x}P_n(x)L_k(x)\,dx.         \tag{28}
\]

The ordinary Laguerre generating function and
\(\int_0^\infty e^{-sx}P_n(x)dx=1-((s-1)/s)^n\) give the rational
identity

\[
 \boxed{
 \sum_{k\ge0}a_k^{(n)}(\varepsilon)z^k
 ={1\over1-z}\left[
 1-\left({(1+\varepsilon)z-\varepsilon
             \over1-\varepsilon+\varepsilon z}\right)^n
 \right].}                                                   \tag{29}
\]

The singularity of (29) is at
\(z_0=-(1-\varepsilon)/\varepsilon\). Setting
\(r=\varepsilon/(1-\varepsilon)\), extraction at that pole gives, for fixed
\(n\),

\[
 a_k^{(n)}(\varepsilon)
 =(-1)^{n+k+1}{\varepsilon^{1-n}\over(1-\varepsilon)^n}
   {k+n-1\choose n-1}r^k
   +O_{n,\varepsilon}(k^{n-2}r^k).                            \tag{30}
\]

For \(n=1\) the error term is omitted; for \(\varepsilon=0\) the
sequence is simply the original finite prefix.

By the exact formula of `103_52`,

\[
 \Delta A_k=-{\gamma+\log(4\pi)\over2}
 +\sum_{\ell\ \mathrm{odd}}{1-(1-1/\ell)^k\over\ell},    \tag{31}
\]

one has \(\Delta A_k\asymp\log k\) and, for \(k\ge M\),
\(\Delta A_k\ge\Delta A_M>0\). Equations (30)–(31) prove

\[
 \boxed{
 \sum_{k\ge M}\Delta A_k|a_k^{(n)}(\varepsilon)|^2<\infty
 \quad\Longleftrightarrow\quad\varepsilon<\tfrac12.}       \tag{32}
\]

The positive metric does not move the boundary; it makes it more singular
by a logarithmic factor. Indeed, at \(\varepsilon=1/2\),

\[
 \sum_{M\le k\le K}\Delta A_k|a_k^{(n)}(1/2)|^2
 \asymp_n K^{2n-1}\log K,                                   \tag{33}
\]

and for \(1/2<\varepsilon<1\) it grows like

\[
 \asymp_{n,\varepsilon}r^{2K}K^{2n-2}\log K.                 \tag{34}
\]

From below, the squared norm of the tail has order

\[
 (1-2\varepsilon)^{-(2n-1)}
 \log{1\over1-2\varepsilon}.                                \tag{35}
\]

Consequently \(A_{\rm flag}\) does build the correct scalar denominator
over each prefix, but it creates no overlap between the safe Euler domain
and the domain of the inverse transport.

## 6. Scope of the stop-gate

What is proved:

1. the exact flow (6), before removing the regulator;
2. the self-adjoint realization \(Q=-M_x\);
3. the sharp threshold (13), with blow-up (14);
4. the strict norm-convergence threshold (17);
5. that \(\mathcal H_{\rm flag}\) is not invariant, that \(Q_{\rm flag}\)
   is not \(A_{\rm flag}\)-symmetric, and that even its projected tail
   keeps the same threshold.

Only the following move is ruled out:

> first building the prime channel as a bounded operator in a safe Euler
> regulator and recovering the A1 observable by applying the birth–death
> semigroup backward in a Laguerre Hilbert space.

A theorem that keeps the pole, Gamma, and primes as a single signed
renormalized functional remains open. Such a theorem cannot be justified
by the domain overlap of this flow: that overlap is empty.

## 7. Verification

From `phase-104-unconditional-a1-closure/tools`:

```bash
python3 epsilon_flow_observability_gate_check.py
```

The script uses only `Fraction`. It verifies (2), the polar flow (5), the
generating function (29) against exact integration for several degrees and
regulators, and the leak (24) with value \(22350\) for \(M=150\).
</content>
