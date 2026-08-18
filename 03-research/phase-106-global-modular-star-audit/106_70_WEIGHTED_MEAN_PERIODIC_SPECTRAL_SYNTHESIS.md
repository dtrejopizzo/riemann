# 106.70 — Weighted mean-periodic spectral synthesis

## Purpose and verdict

Document 106.67 isolates the following proposed form-core identity:

\[
 \overline{\bigcup_M V_M}^{\,\|\cdot\|_{\rm form}}
 =\mathcal N_K,
 \qquad
 \mathcal N_K=\{F\in L^2(\omega_K):F*K=0\},          \tag{1}
\]

where \(V_M\) contains the exponential monomials and multiplicity jets at
the zeros of \(\Xi=\widehat K\).  This note audits (1) in the actual
weighted and prime--Gamma topologies.

There are four rigorous conclusions.

1. Every elementary zero mode and multiplicity jet belongs to the operator
   domain of the radically shorted operator \(T_F\).
2. The usual one-dimensional mean-periodic synthesis theorem gives
   compact-open synthesis, but it does **not** imply weighted \(L^2\), form,
   or operator-graph synthesis here.  Every nontrivial translation is an
   unbounded operator on \(L^2(\omega_K)\).
3. Weighted \(L^2\) synthesis is exactly one entire-function division
   theorem: every weighted Fourier transform divisible by \(\Xi\) must lie
   in the closure of \(\Xi\) times the even polynomials.  This division
   theorem is not proved by the local mean-periodic theorem.
4. Even that division theorem would not by itself prove (1).  Form synthesis
   is equivalent to density after applying \((T_F+1)^{1/2}\), and operator
   graph synthesis is equivalent to the vanishing of two explicit
   deficiency spaces.

Thus the form-norm spectral-synthesis input used provisionally in 106.67 is
not yet a theorem.  The exact obstruction is no longer the informal phrase
``upgrade compact convergence to the graph norm'': it is the division
identity (31) together with the deficiency conditions (39).  No RH sign is
used in deriving these gates.

## 1. The three topologies

Recall

\[
 h(x)=\cosh(x/2),\qquad c_K=\frac12,
 \qquad d\omega_K(x)=\frac{K(x)}{c_Kh(x)}\,dx.       \tag{2}
\]

Multiplication by \(h\) is the unitary

\[
 W:L^2(\mu_K)\longrightarrow L^2(\omega_K),
 \qquad Wq=hq.                                      \tag{3}
\]

Let \(L\ge0\) be the full ordinary-prime--Gamma generator and

\[
 T_F=W(L-1/2)W^{-1}\big|_{\mathcal N_K}.            \tag{4}
\]

The closed positive form which defines the required topology is

\[
 \mathfrak s(F,G)
 :=\langle F,G\rangle_{\omega_K}
   +\langle F,T_FG\rangle_{\omega_K}
 =\frac12\langle F,G\rangle_{\omega_K}
   +\mathscr E_K(F/h,G/h).                          \tag{5}
\]

Indeed \(S:=T_F+1=W(L+1/2)W^{-1}\ge1/2\), and

\[
 \|F\|_{\rm form}=\|S^{1/2}F\|_{\omega_K}.         \tag{6}
\]

This is weaker than the operator graph norm

\[
 \|F\|_{\rm gr}^2
 =\|F\|_{\omega_K}^2+\|T_FF\|_{\omega_K}^2.        \tag{7}
\]

Document 106.67 needs (6), not the stronger norm (7).  We audit both so
that they are not conflated.

Let \(\mathcal E\) be the algebraic real-even span of

\[
 F_{z,k}(x)=\partial_z^k\cos(zx),\qquad
 \Xi(z)=0,\quad 0\le k<m_z,                       \tag{8}
\]

with the complete conjugation and \(z\mapsto-z\) orbits understood.

## 2. The elementary modes lie in the full graph domain

Every nontrivial zero in the frequency normalization
\(\Xi(z)=\xi(1/2+iz)\) satisfies \(|\operatorname {Im}z|<1/2\).  For a
fixed finite collection of modes, put

\[
 \delta=\frac12-\max|\operatorname {Im}z|>0,
 \qquad d=\max(m_z-1).                              \tag{9}
\]

Then

\[
 \left|\frac{F_{z,k}(x)}{h(x)}\right|
 +\left|\partial_x\frac{F_{z,k}(x)}{h(x)}\right|
 \le C_{z,k}(1+|x|)^{d+1}e^{-\delta|x|}.           \tag{10}
\]

### Proposition 1 — Graph-domain membership

\[
 \boxed{\mathcal E\subset D(T_F).}                 \tag{11}
\]

#### Proof

Write \(q=F_{z,k}/h\).  For the Gamma channel, (10) gives

\[
 |q(x)-q(x-u)|\le C u
 \sup_{y\in[x-u,x]}(1+|y|)^{d+1}e^{-\delta|y|}
 \qquad(0<u<1).                                    \tag{12}
\]

Since \(g(u)=1/(2u)+O(1)\), both the Gamma form and the pointwise Gamma
generator are locally integrable at zero.  For \(u\ge1\), the theta
overlap estimate of 106.67 gives

\[
 \int K(x)K(x-u)
   \{|q(x)|^2+|q(x-u)|^2\}\,dx
 \le C_{z,k}e^{-ae^u}.                             \tag{13}
\]

At \(u=\log n\), (13) is \(O(e^{-an})\); hence its sum against
\(\Lambda(n)/\sqrt n\) converges absolutely.  The same estimates applied
to the joint star current in 106.49 show that \(Lq\in L^2(\mu_K)\): the
small-Gamma part uses (12), while every large Gamma or prime displacement
is bounded by (13), followed by Cauchy--Schwarz in the finite local rate.
Thus \(q\in D(L)\).  Conjugation by \(W\) proves (11). \(\square\)

This proposition validates every finite Gram matrix in 106.62 and 106.67.
It does not prove that their union is a core.

## 3. Why compact-open synthesis does not upgrade automatically

The classical one-dimensional mean-periodic theorem says that a continuous
solution of a convolution equation on \(\mathbb R\) is approximable,
uniformly on compact sets, by exponential monomial solutions of the same
equation.  Applied locally to \(F*K=0\), it yields precisely the modes (8).

The ambient topology here is different.  If \(\tau_aF(x)=F(x-a)\), then

\[
 \|\tau_a\|_{L^2(\omega_K)\to L^2(\omega_K)}^2
 =\operatorname*{ess\,sup}_{x\in\mathbb R}
   \frac{\omega_K(x+a)}{\omega_K(x)}.               \tag{14}
\]

The theta asymptotic is

\[
 \omega_K(x)
 =\exp\{-\pi e^{2|x|}+4|x|+O(1)\}
 \qquad(|x|\to\infty).                             \tag{15}
\]

For \(a>0\), take \(x=-R\).  Then

\[
 \log\frac{\omega_K(-R+a)}{\omega_K(-R)}
 =\pi(1-e^{-2a})e^{2R}+O(R)\longrightarrow+\infty. \tag{16}
\]

Reflection handles \(a<0\).  Therefore

\[
 \boxed{\tau_a\text{ is unbounded on }L^2(\omega_K)
 \quad(a\ne0).}                                    \tag{17}
\]

In particular, \(L^2(\omega_K)\) is not a translation-invariant Banach
function space, and \(\mathcal N_K\) is not a variety in its Hilbert
topology.  The compact-open spectral-synthesis theorem cannot be invoked in
that topology.  The same issue remains in (6), since the prime energy
contains every translation \(\log p^k\).

The failure is topological, not a statement about the zero locations.  For
example, normalized bumps translated to \(R\) converge to zero on every
fixed compact set while retaining unit \(L^2(\omega_K)\) norm.  Thus no
inequality can bound the global norm by finitely many compact-open
seminorms.

## 4. The exact weighted \(L^2\) division problem

Define the weighted Fourier transform

\[
 (\mathcal BF)(z)
 :=\int_{\mathbb R}F(x)e^{-izx}\,d\omega_K(x).      \tag{18}
\]

Cauchy--Schwarz gives, for every \(y\in\mathbb R\),

\[
 |\mathcal BF(t+iy)|
 \le\|F\|_{\omega_K}
 \left(\int e^{2yx}\,d\omega_K(x)\right)^{1/2}.   \tag{19}
\]

The double-exponential decay of \(\omega_K\) makes the last integral
finite for every \(y\); hence \(\mathcal BF\) is entire and every point
derivative is a continuous functional on \(L^2(\omega_K)\).

Let

\[
 \mathcal R_W=W(\mathbf1\oplus\mathcal R).          \tag{20}
\]

Using \(r_j=K^{(2j)}/K\), one obtains exactly

\[
 \begin{aligned}
 \mathcal B(h)(z)&=c_K^{-1}\Xi(z),\\
 \mathcal B(hr_j)(z)&=c_K^{-1}(-1)^jz^{2j}\Xi(z).
 \end{aligned}                                      \tag{21}
\]

Thus \(\mathcal B\mathcal R_W\) is the closure, in the transform norm, of

\[
 \Xi(z)\,\mathbb C[z^2].                            \tag{22}
\]

On the other hand, orthogonality to every zero mode and multiplicity jet is
equivalent to

\[
 (\mathcal BF)^{(k)}(z)=0
 \quad(\Xi(z)=0,\ 0\le k<m_z).                     \tag{23}
\]

Therefore \(\mathcal BF/\Xi\) is entire.  Put

\[
 \mathcal D_\Xi
 :=\{F\in L^2_{\rm even}(\omega_K):
          \mathcal BF/\Xi\text{ is entire}\}.       \tag{24}
\]

### Theorem 2 — Exact \(L^2\)-synthesis criterion

\[
 \boxed{
 \overline{\mathcal E}^{\,L^2(\omega_K)}=\mathcal N_K
 \quad\Longleftrightarrow\quad
 \mathcal D_\Xi=\mathcal R_W.}                     \tag{25}
\]

#### Proof

The zero-jet calculation gives

\[
 \mathcal E^\perp=\mathcal D_\Xi.                  \tag{26}
\]

The exact radical shorting identity gives

\[
 \mathcal N_K^\perp=\mathcal R_W.                  \tag{27}
\]

Since \(\mathcal E\subset\mathcal N_K\), one already has
\(\mathcal R_W\subset\mathcal D_\Xi\).  Equality of the two closed spans
is equivalent, by taking orthogonal complements, to equality in
(25). \(\square\)

Equation (25) is the missing **division/cyclicity theorem**.  It is not a
consequence of the formal support relation
\(\Xi\widehat F=0\), because \(\mathcal B\) is the transform of
\(F\omega_K\), not the distributional transform of \(F\), and because the
weighted topology is not translation invariant.

## 5. The sharp vertical growth budget

The weight in (2) lets one quantify what division by \(\Xi\) can cost.
For \(y\to+\infty\), \(h(x)^{-1}\le2e^{-x/2}\) on \(x>0\) and evenness
give

\[
 \int e^{2yx}\,d\omega_K(x)
 \le C\,\Xi\!\left(i(2y-1/2)\right).                \tag{28}
\]

On the imaginary axis \(\Xi(iy)=\xi(1/2-y)=\xi(1/2+y)>0\).  Stirling's
formula and \(\zeta(1/2+y)=1+o(1)\), followed by the duplication formula
for Gamma, give

\[
 \frac{\Xi(i(2y-1/2))^{1/2}}{\Xi(iy)}
 \le C(1+y)^C2^{y/2}.                               \tag{29}
\]

Consequently, if \(F\in\mathcal D_\Xi\) and
\(H=\mathcal BF/\Xi\), then

\[
 \boxed{
 |H(iy)|\le C_F(1+|y|)^C
 e^{(\log2)|y|/2}.}                                 \tag{30}
\]

The constant

\[
 a_0=\frac12\log2                                  \tag{31}
\]

is sharp for this Cauchy--Schwarz comparison.  It is also the exact real
translation radius visible directly in the theta tails.  For
\(|a|<a_0\), define

\[
 F_a(x)=\frac{h(x)}{2K(x)}\{K(x-a)+K(x+a)\}.        \tag{32}
\]

Then \(F_a\in L^2(\omega_K)\),

\[
 \mathcal BF_a(z)=c_K^{-1}\Xi(z)\cos(az),          \tag{33}
\]

and the Banach-valued Taylor series

\[
 F_a=h\sum_{j\ge0}\frac{a^{2j}}{(2j)!}r_j          \tag{34}
\]

converges in \(L^2(\omega_K)\).  Indeed, the leading theta term gives

\[
 \frac{h(x)K(x-a)^2}{K(x)}
 =\exp\{\pi(1-2e^{-2a})e^{2x}+O(x)\},              \tag{35}
\]

which is integrable precisely for \(a<a_0\); reflection treats the other
tail.  Local uniform analyticity plus the same bound on compact
subintervals of \((-a_0,a_0)\) proves the Hilbert-valued Taylor
convergence.

Thus the nonpolynomial quotient \(H(z)=\cos(az)\) does not contradict
(25): it already lies in the radical closure.  Conversely, the vertical
type bound (30) alone does not prove (25), because it supplies no control
of \(H\) on horizontal lines or of approximation by polynomials in the
transform norm.  The missing assertion is precisely that every admissible
quotient, not just the translation vectors (32), is cyclically generated
by the polynomial quotients.

## 6. Form synthesis and graph synthesis are separate

Assume provisionally that the division identity in (25) has been proved,
so that \(\mathcal E\) is dense in \(\mathcal N_K\) in the ambient Hilbert
norm.  This still does not prove the form-core identity (1).

### Theorem 3 — Exact form-core criterion

With \(S=T_F+1\ge1/2\),

\[
 \boxed{
 \overline{\mathcal E}^{\,\|\cdot\|_{\rm form}}
 =\mathcal N_K\cap D(S^{1/2})
 \quad\Longleftrightarrow\quad
 \overline{S^{1/2}\mathcal E}^{\,L^2(\omega_K)}
 =\mathcal N_K.}                                    \tag{36}
\]

Equivalently, the obstruction space is

\[
 \boxed{
 \mathcal D_{\rm form}
 :=\{G\in\mathcal N_K:
       \langle G,S^{1/2}E\rangle=0
       \text{ for every }E\in\mathcal E\}.}        \tag{37}
\]

The desired form synthesis holds exactly when
\(\mathcal D_{\rm form}=\{0\}\).

#### Proof

The map \(S^{1/2}\) is an isometry from the form domain equipped with
(6) onto \(\mathcal N_K\), because \(S\ge1/2\) is self-adjoint and
surjective after applying the bounded inverse \(S^{-1/2}\).  Taking the
image of the closure proves (36); taking orthogonal complements gives
(37). \(\square\)

### Theorem 4 — Exact operator-graph criterion

Let \(T_0=T_F|_{\mathcal E}\).  Then

\[
 \boxed{
 \overline{\mathcal E}^{\,\|\cdot\|_{\rm gr}}=D(T_F)
 \quad\Longleftrightarrow\quad
 \ker(T_0^*-i)=\ker(T_0^*+i)=\{0\}.}               \tag{38}
\]

Equivalently,

\[
 \boxed{
 \overline{(T_F+i)\mathcal E}
 =\overline{(T_F-i)\mathcal E}
 =\mathcal N_K.}                                    \tag{39}
\]

#### Proof

Graph synthesis says exactly that the symmetric restriction \(T_0\) is
essentially self-adjoint with closure \(T_F\).  Von Neumann's range and
deficiency criteria give (38)--(39). \(\square\)

In terms of zero modes, a nonzero deficiency vector is a
\(G\in\mathcal N_K\) satisfying

\[
 \boxed{
 \langle G,(T_F\pm i)F_{z,k}\rangle_{\omega_K}=0
 \quad\text{for every zero }z\text{ and every }k<m_z.} \tag{40}
\]

Formula (9) of 106.64 expands every entry in (40) using the literal
\(\Lambda(n)\), Gamma and theta factors.  Mean periodicity alone does not
make (40) impossible: it constrains \(F_{z,k}*K\), whereas \(T_F\) acts on
\((K/h)F_{z,k}\) through a Toeplitz--Hankel convolution.

## 7. The exact theorem still required by the cofinal-head route

For the finite-mode spaces \(V_M\) of 106.67, the needed assertion is the
following two-part statement:

\[
 \boxed{
 \begin{aligned}
 &\mathcal D_\Xi=\mathcal R_W,\\
 &\mathcal D_{\rm form}=\{0\}.
 \end{aligned}}                                     \tag{41}
\]

The first line proves ambient weighted synthesis.  The second upgrades it
to the prime--Gamma form core.  If the stronger operator graph claim is
wanted, the second line must be replaced by the two deficiency conditions
in (38).

A directly checkable version is: for every
\(F\in\mathcal N_K\cap D(S^{1/2})\), there must exist
\(F_M\in V_M\) such that

\[
 \boxed{
 \|F-F_M\|_{\omega_K}^2
 +\mathscr E_K\!\left(\frac{F-F_M}{h}\right)
 \longrightarrow0.}                                \tag{42}
\]

Compact-open convergence controls neither term in (42).  The
superexponential omitted-prime estimate of 106.67 controls the Euler tail
*after a fixed finite mode space has been chosen*; it does not control the
conditioning or the global tails of the synthesizing vectors as
\(M\to\infty\).

## 8. Consequence

The zero modes and jets are valid graph-domain test vectors, and finite
prime heads approximate their complete Gram matrices superexponentially.
What remains unproved is their global completeness in the topology in
which the complete operator is closed.

Accordingly, the implication used in 106.67,

\[
 \neg\mathrm {RH}\Longrightarrow
 \delta_M<0\text{ for some elementary }V_M,         \tag{43}
\]

cannot yet be inferred from compact-open mean-periodic synthesis.  It
becomes valid after (41), or equivalently after the approximation theorem
(42).  Proving (41) would be a genuine analytic advance, but it would not
by itself prove RH: the remaining sign would still be the cofinal Gram
inequality of 106.67.
