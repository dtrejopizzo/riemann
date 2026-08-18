# 106.117 — Post-short Möbius bar homotopy and the zero-fibre gate

## 1. Purpose and verdict

The remaining physical surplus is globally signed after the complete
Riemann radical has been anti-shorted. This leaves one algebraic mechanism
which is genuinely different from positivity, martingale routing and local
Hodge theory: resolve the divisor monoid by ordered factorisation chains,
use Möbius signs as a chain homotopy, and transfer the resulting amplitude
nonlocally before taking a Hilbert norm.

The signed construction exists exactly. Put \(Z=I+X\), where \(Z\) is the
Euler zeta element and \(X\) is its nonidentity part. Its canonical
multiplicative bar homotopy is

\[
 Z^{-1}=I-X+X^2-X^3+\cdots .                       \tag{1}
\]

The \(k\)-th term is the sum over ordered \(k\)-factorisations. It gives
Möbius inversion and, after one logarithmic derivative, every literal
ordinary von Mangoldt weight.

There are two exact obstructions to turning (1) into the required bounded
post-short transfer.

1. If distinct factorisation chains are retained as orthogonal Hilbert
   coordinates, the signed collapse on a squarefree integer with \(r\)
   prime factors has norm

   \[
    \left(\sum_{k=1}^r k!S(r,k)\right)^{1/2}
    \geq\sqrt{r!},                                  \tag{2}
   \]

   and is unbounded.
2. If the Möbius cancellation is performed before taking the norm, the
   collapse is precisely \(Z^{-1}\). The radical anti-short does not remove
   the zeta-zero fibres: it isolates them as the mean-periodic complement.
   On any known critical-line zero \(\rho\), the Abel continuation of the
   homotopy has gain \(1/|\zeta(\rho+\varepsilon)|\), while the differentiated
   connection has gain asymptotic to \(m_\rho/\varepsilon\). Hence the
   critical bar complex has nonzero zeroth homology and admits no chain
   contraction on that fibre.

The Gamma and polar factors are analytic and nonzero at every nontrivial
zero. They preserve, rather than cancel, the connection residue. Thus a
completed bounded transfer would have to add a separate zero-fibre map.
Once it is required to interpolate the physical source gradient to the
polar gradient, that map is the unique canonical transfer of 106.105, and
its contractivity is exactly the still-unproved physical surplus.

This is an exact obstruction to the divisor-bar mechanism. It is not a
counterexample to the physical inequality and uses no off-line zero.

## 2. Semantic audit through Phases 1--106

No earlier document constructs the normalized ordered-factorisation bar
homotopy (1) and then specializes it **after** the complete radical
anti-short. The binding neighbouring results are nevertheless substantial.

| document | result already proved | relation to the present gate |
|---|---|---|
| E70.11--E70.12 | \(Z^{-1}\delta Z=V_\Lambda\) and its Riccati jet | supplies the connection, but no chain resolution or post-short norm |
| 104.12 | Möbius--divisor convolution; \(Z^{-1}\) cannot be a positive-metric adjoint of \(Z\) | excludes a Gram realization, not a signed bar homotopy |
| 104.15 | the squarefree Koszul complex makes every \(N_p\) null-homotopic and therefore kills the prime current | excludes local generator-wise homotopies; explicitly leaves a nonlocal complex open |
| 104.80 | every absolutely convergent Möbius regrouping has the same nonremovable zero pole | gives the meromorphic obstruction in the Laguerre coordinate |
| 106.40 and 106.106 | spatial theta--Möbius inversion and divisor-current duplication | identify the literal spatial connection and all its old jets |
| 106.61 | the Möbius inverse is singular on a mean-periodic zero mode | proves the analytic singularity which the homological argument below upgrades to failure of chain contraction |
| 106.63 and 106.94 | one must assemble the full source before shorting; mean periodicity applies only after the correct decomposition | fixes the order of operations used here |
| 106.105 | every exact post-short signed interpolation is the canonical inverse-square-root transfer | fixes the norm of any completed bar construction |
| 106.111 and 106.113 | finite-local and infinite-boundary Hodge flows cannot close the surplus | do not apply to the nonlocal ordered-factorisation complex |

Thus the bar construction is not a duplicate, but its two analytic inputs
and its final norm obstruction have exact predecessors. The new content is
the chain-level dichotomy (2) versus the zero-fibre homology below.

## 3. The normalized multiplicative bar contraction

For \(\varepsilon\geq0\), write

\[
 T_{n,\varepsilon}
 :=n^{-1/2-\varepsilon}S_{\log n},
 \qquad
 T_{m,\varepsilon}T_{n,\varepsilon}=T_{mn,\varepsilon}. \tag{3}
\]

On the theta cyclic orbit, or first as a formal Dirichlet series, put

\[
 Z_\varepsilon=\sum_{n\geq1}T_{n,\varepsilon}
 =I+X_\varepsilon.                                  \tag{4}
\]

Consider the two-term Euler mapping-cone complex

\[
 0\longrightarrow\mathcal V
 \xrightarrow{\,Z_\varepsilon\,}
 \mathcal V\longrightarrow0 .                     \tag{5}
\]

Where \(Z_\varepsilon\) is invertible, a chain contraction of (5) is
unique and is given in both degrees by

\[
 H_\varepsilon=Z_\varepsilon^{-1}.                 \tag{6}
\]

Indeed \(Z_\varepsilon H_\varepsilon=I\) in degree zero and
\(H_\varepsilon Z_\varepsilon=I\) in degree one. Expanding (6) gives

\[
 \boxed{
 H_\varepsilon
 =\sum_{k\geq0}(-1)^kX_\varepsilon^k
 =\sum_{N\geq1}\mu(N)T_{N,\varepsilon}.}          \tag{7}
\]

The coefficient identity in (7) is the normalized multiplicative bar
resolution. For \(N>1\), let

\[
 \mathrm{Fact}_k(N)
 =\{(n_1,\ldots,n_k):n_i>1,\ n_1\cdots n_k=N\}.    \tag{8}
\]

The coefficient of \(T_{N,\varepsilon}\) in (7) is

\[
 \boxed{
 \mu(N)=\sum_{k\geq1}(-1)^k
             \#\mathrm{Fact}_k(N).}         \tag{9}
\]

This is locally finite and follows simply by reading the coefficient of
\(T_N\) in \((I+X)^{-1}(I+X)=I\). Applying the logarithmic derivation

\[
 \delta T_{n,\varepsilon}=(\log n)T_{n,\varepsilon} \tag{10}
\]

gives the exact connection

\[
 \boxed{
 H_\varepsilon\delta Z_\varepsilon
 =\sum_{N\geq2}\Lambda(N)T_{N,\varepsilon}.}       \tag{11}
\]

Thus (7) retains all ordered factorisations, while (11) retains every
ordinary prime power with its literal weight
\(\Lambda(p^a)=\log p\). No positivity or \(j_2\) argument is being used.

## 4. Orthogonal bar chains have factorial norm

Let \(N=p_1\cdots p_r\) be squarefree. An ordered factorisation of \(N\)
into \(k\) factors is exactly an ordered partition of the \(r\) primes into
\(k\) nonempty blocks. Hence

\[
 \#\mathrm{Fact}_k(N)=k!S(r,k),             \tag{12}
\]

where \(S(r,k)\) is a Stirling number of the second kind. Equation (9)
becomes the familiar exact cancellation

\[
 \sum_{k=1}^r(-1)^k k!S(r,k)=(-1)^r=\mu(N).        \tag{13}
\]

Let \(\mathcal B_N\) be the Hilbert space with orthonormal basis indexed by
all chains in \(\bigcup_k\mathrm{Fact}_k(N)\), and define the signed
bar collapse

\[
 \mathfrak m_N(c)
 =\sum_{k=1}^r(-1)^k
   \sum_{\mathbf n\in\mathrm{Fact}_k(N)}c_{\mathbf n}. \tag{14}
\]

### Theorem 1 — Exact factorial obstruction

\[
 \boxed{
 \|\mathfrak m_N\|^2
 =F_r:=\sum_{k=1}^r k!S(r,k)\geq r!.}              \tag{15}
\]

Consequently the orthogonal direct sum of the maps
\(\mathfrak m_N\) over squarefree \(N\) is unbounded.

#### Proof

The Riesz vector of (14) has one coordinate of modulus one for each
ordered factorisation, so its squared norm is their number, which is
\(F_r\) by (12). The \(k=r\) term equals \(r!\), proving the lower bound.
\(\square\)

The conclusion is unchanged by the physical multiplicative factor in
(3). Every chain over a fixed \(N\) carries the same product weight
\(N^{-1/2-\varepsilon}\); scaling both the chain basis and its endpoint by
that common factor leaves (15) unchanged.

Theorem 1 has a precise scope. It excludes a Hilbert resolution which
keeps distinct bar chains orthogonal until the last signed collapse. One
can avoid the factorial norm only by correlating and cancelling the chains
before taking the norm. But then the resulting operator is exactly the
Möbius inverse (7), to which the next obstruction applies.

## 5. Radical anti-shorting isolates the singular fibre

Let

\[
 \mathscr C=(\mathbf1\oplus\mathcal R)^\perp
 \subset L^2(\mu_K).                                \tag{16}
\]

By 106.43, \(\mathscr C\) is the mean-periodic space

\[
 q\in\mathscr C
 \quad\Longleftrightarrow\quad
 (hq)*K=0,
 \qquad h(x)=\cosh(x/2).                            \tag{17}
\]

Choose any rigorously known critical-line zero

\[
 \rho=\frac12+i\gamma
\]

of multiplicity \(m\geq1\), and use its conjugate
\(\bar\rho=1/2-i\gamma\). The even elementary mode

\[
 q_\gamma(x)=\frac{\cos(\gamma x)}{h(x)}           \tag{18}
\]

belongs to \(\mathscr C\), because
\((h q_\gamma)*K=\cos(\gamma\cdot)*K=0\). It also belongs to
\(L^2(\mu_K)\), by the double-exponential decay of \(K\).

On the complex component \(F_\gamma(x)=e^{i\gamma x}\), the Euler
translation character is

\[
 \chi_\gamma(T_{n,\varepsilon})
 =n^{-1/2-\varepsilon+i\gamma}.                    \tag{19}
\]

Thus, initially in the half-plane of absolute convergence and then by
unique meromorphic continuation,

\[
 \boxed{
 \chi_\gamma(Z_\varepsilon)
 =\zeta(\bar\rho+\varepsilon),
 \qquad
 \chi_\gamma(H_\varepsilon)
 ={1\over\zeta(\bar\rho+\varepsilon)}.}           \tag{20}
\]

Since \(\bar\rho\) is a zero of order \(m\),

\[
 \zeta(\bar\rho+\varepsilon)
 ={\zeta^{(m)}(\bar\rho)\over m!}\varepsilon^m
 +O(\varepsilon^{m+1}).                            \tag{21}
\]

### Theorem 2 — No critical post-short bar contraction

Every Euler-compatible chain contraction of (5), restricted to the
one-dimensional character fibre generated by \(F_\gamma\), has gain

\[
 \boxed{
 |\chi_\gamma(H_\varepsilon)|
 ={m!\over|\zeta^{(m)}(\bar\rho)|}\varepsilon^{-m}
 (1+O(\varepsilon)).}                              \tag{22}
\]

In particular it has no uniformly bounded critical limit. At
\(\varepsilon=0\), the specialized differential in (5) is zero and

\[
 H_0(\mathcal V\xrightarrow{Z_0}\mathcal V)
 \supset\mathbb C F_\gamma\ne0.                    \tag{23}
\]

Therefore the critical specialized complex is not contractible.

#### Proof

On a one-dimensional character fibre, both left and right contraction
identities reduce to

\[
 \zeta(\bar\rho+\varepsilon)h_\varepsilon=1.
\]

This forces (20), and (21) proves (22). At \(\varepsilon=0\), the
differential is multiplication by \(\zeta(\bar\rho)=0\), giving the
nonzero homology (23). A contractible complex has zero homology, so no
critical contraction exists. \(\square\)

The real even pair in (18) contains the conjugate character fibres and has
the same lower bound. Thus the obstruction lies inside the actual
post-short space, not in an inadmissible exponential direction.

## 6. Differentiation and completion do not remove the pole

The bar homotopy was introduced to recover the von Mangoldt current. On
the same character, (11) gives

\[
 \boxed{
 \chi_\gamma(H_\varepsilon\delta Z_\varepsilon)
 =-{\zeta'\over\zeta}(\bar\rho+\varepsilon)
 =-{m\over\varepsilon}+O(1).}                     \tag{24}
\]

Thus differentiating improves neither the domain nor the norm: it turns
the order-\(m\) inverse pole into the universal logarithmic-connection pole.
Equation (24) contains the real weights \(\Lambda(p^a)=\log p\), not a
relaxed Euler model.

Now write

\[
 \xi(s)=G(s)\zeta(s),
 \qquad
 G(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2).          \tag{25}
\]

At a nontrivial zero, \(G\) is analytic and nonzero. Therefore

\[
 -{\xi'\over\xi}(s)
 =-{\zeta'\over\zeta}(s)-{G'\over G}(s)           \tag{26}
\]

has the same residue \(-m\) at \(\bar\rho\). The complete Gamma factor and
both polar factors change only the \(O(1)\) term in (24). They cannot
cancel the bar pole.

This is the chain-level version of the nonremovable-pole theorem of 104.80.
Its force here is more specific: the pole occurs on a mode which the exact
radical anti-short deliberately retains.

## 7. Why a residue repair returns to the canonical transfer

One could abandon contraction of the critical bar complex, retain its
zero-fibre homology, and prescribe a separate map from that homology to the
polar edge space. Such a prescription is no longer determined by the
divisor boundary or by Möbius inversion. To be a physical closure it must
satisfy, on the complete post-short source-gradient range,

\[
 C\mathcal Gq=D_\mu q,
 \qquad q\in\mathscr C.                             \tag{27}
\]

The uniqueness theorem of 106.105 then forces

\[
 \boxed{
 C=2^{-1/2}U_DA^{-1/2}U_A^*,
 \qquad
 \|C\|=(2\inf\sigma A)^{-1/2}.}                   \tag{28}
\]

Consequently

\[
 \|C\|\le1
 \quad\Longleftrightarrow\quad
 A\ge\frac12I.                                    \tag{29}
\]

The zero-fibre repair is logically admissible, but its norm inequality is
exactly the physical surplus. Neither the bar contraction nor the analytic
Gamma completion provides an additional estimate for (28).

There is therefore a complete dichotomy for the proposed mechanism:

\[
\begin{array}{c|c}
\text{bar chains kept orthogonal}&
\text{factorial norm growth (15)}\\
\text{bar signs cancelled before the norm}&
\text{zero-fibre pole and noncontractible limit (22)--(24)}\\
\text{zero-fibre residue supplied separately}&
\text{canonical transfer, whose bound is (29).}
\end{array}                                         \tag{30}
\]

## 8. Status

Proved here:

* the exact normalized ordered-factorisation bar homotopy (7);
* recovery of all literal von Mangoldt weights by (11);
* the exact factorial Hilbert norm (15) on squarefree fibres;
* the zero-character lower bound (22) after radical anti-shorting;
* noncontractibility of the critical specialized complex;
* persistence of the logarithmic pole after Gamma and polar completion;
* reduction of every separate homology repair to the canonical transfer.

Not proved here:

\[
 A\ge\frac12I.
\]

The divisor-bar resolution is therefore closed as a mechanism for the
heat/hybrid physical surplus. A successor cannot be another exact Möbius
chain contraction. It must estimate the already-completed zero-fibre map
by a genuinely quantitative signed correlation of the ordinary prime,
Gamma and polar placements.
