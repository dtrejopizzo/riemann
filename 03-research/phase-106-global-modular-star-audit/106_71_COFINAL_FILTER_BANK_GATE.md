# 106.71 — The cofinal prime filter-bank gate

## Purpose and verdict

The finite-head computations have a natural signal-processing
interpretation. A finite zero-mode space is a finite collection of input
modes, every prime power is one analysis channel, and increasing the prime
cutoff adds channels to the bank. Thus increasing the number of modes must
in general be accompanied by an increasing prime cutoff. This note makes
that statement exact.

The resulting theorem has two sharply separated parts.

1. The **approximation part is proved**. For every mode dimension $M$
   and every tolerance $\varepsilon_M>0$, one can choose a finite cutoff
   $X(M)$ so that the omitted prime bank has operator norm at most
   $\varepsilon_M$. An admissible schedule is

   \[
   X(M)\ge {1\over c}
   \left(\log C_M+\log{1\over\varepsilon_M}\right).       \tag{1}
   \]

   This is the rigorous version of “more modes require more primes.”
2. The **sign part is not produced by the moving cutoff**. Every finite
   bank lies below the complete bank in Loewner order. After normalization,
   the exact unresolved counterterm is the coherent negative-channel
   contraction

   \[
   \left\|
   \begin{pmatrix}C_M^-\\ R_{M,X}^{1/2}\end{pmatrix}
   (A_M^*A_M+\varepsilon I)^{-1/2}
   \right\|\le1.                                    \tag{2}
   \]

   The prime cutoff controls $R_{M,X}$, but neither PNT nor
   multiplicative independence controls $C_M^-$. PNT has already been
   used to put the essential spectrum at $1/2$; the term $C_M^-$ is the
   remaining compact, localized bound-state channel.

Consequently the moving-bank idea is a valid cofinal approximation scheme,
not a sign-producing average. The literal theorem still worth pursuing is
the lower-frame inequality (13) below. Its exact obstruction is (2), not a
missing estimate for the prime tail.

## 1. Semantic audit against Phases 1–106

The search was made over the full research tree using the terms *moving
average*, *filter bank*, *cofinal head*, *frame bound*, *multiplicative
independence*, *sampling*, and *diagonal dominance*. The relevant earlier
results are these.

* Paper 38 studies FIR averages in the Li-index variable. That is a
  different filter: it averages consecutive Li coefficients, not prime
  displacement channels.
* Phase 47 and Phase 50 study incommensurable prime phases and
  Beurling--Landau frames. They prove that rational independence gives
  qualitative transversality on the Bohr torus, but does not transport a
  lower frame bound to Weil inertia. In fact Kronecker near-collisions
  destroy a uniform Riesz lower bound in the unweighted phase coordinate.
* Documents 106.47 and 106.67 contain the two analytic ingredients used
  here: the moving-PNT spatial tail floor and the superexponential
  prime-head remainder on each fixed zero-mode space.
* Documents 106.62–106.64 prove respectively the exact zero-mode Gram
  formula, the all-atoms Loewner flag, and the positive-minus-negative
  Krein factorization.

Thus the generic ideas “add primes with modes” and “average finite heads”
have antecedents. What is added here is their single normalized filter-bank
identity, the explicit cofinal schedule (1), and the exact contraction (2)
which identifies why PNT and rational independence stop on opposite sides
of the missing sign.

## 2. The literal analysis bank

Retain the zero-mode synthesis map of 106.62 and 106.67,

\[
Z_Ma=\sum_{\alpha=1}^{d_M}a_\alpha\chi_\alpha,
\qquad N_M=Z_M^*Z_M>0,                              \tag{3}
\]

where all zero orbits in the chosen rectangle and all multiplicity jets
are retained. No reality of the zero divisor is assumed.

Let \(\mathcal V_{M,X}\) be the direct-sum feature map containing the
continuous Gamma channel and every literal prime-power channel with
\(p^k\le X\):

\[
\|\mathcal V_{M,X}a\|^2
=\mathscr E_\Gamma(Z_Ma)
+\sum_{p^k\le X}{\Lambda(p^k)\over p^{k/2}}
  \mathcal J_{k\log p}(Z_Ma).                       \tag{4}
\]

Normalize the coefficient space by

\[
S_{M,X}=\mathcal V_{M,X}N_M^{-1/2},                \tag{5}
\]

where the synthesis map $Z_M$ is included in the definition of
\(\mathcal V_{M,X}\). The normalized signed Gram matrix is

\[
\boxed{
G_{M,X}
:=N_M^{-1/2}H_{M,X}N_M^{-1/2}
=S_{M,X}^*S_{M,X}-{1\over2}I.}                     \tag{6}
\]

This is an exact filter-bank formula. The desired compensated lower bound
is precisely a lower frame bound for \(S_{M,X}\):

\[
G_{M,X}\ge-\varepsilon I
\quad\Longleftrightarrow\quad
s_{\min}(S_{M,X})^2\ge {1\over2}-\varepsilon.      \tag{7}
\]

There is no scalar averaging approximation in (6): all Gamma, prime,
prime-power, polar, and cross-mode terms remain in the same Hermitian
matrix.

## 3. The exact moving-head law

Write

\[
\mathcal R_{M,X}
:=N_M^{-1/2}(H_{M,\infty}-H_{M,X})N_M^{-1/2}.       \tag{8}
\]

The all-atoms flag and the theta overlap estimate of 106.67 give

\[
\boxed{
0\le\mathcal R_{M,Y}\le\mathcal R_{M,X}
\le C_Me^{-cX}I
\qquad (Y\ge X).}                                  \tag{9}
\]

In particular,

\[
G_{M,X}=G_{M,\infty}-\mathcal R_{M,X}              \tag{10}
\]

and

\[
\delta_M-C_Me^{-cX}
\le\lambda_{\min}(G_{M,X})\le\delta_M,
\qquad
\delta_M=\lambda_{\min}(G_{M,\infty}).            \tag{11}
\]

### Theorem 1 — Cofinal filter-bank approximation

For arbitrary \(\varepsilon_M\downarrow0\), choose \(X(M)\) satisfying

\[
C_Me^{-cX(M)}\le\varepsilon_M.                    \tag{12}
\]

Then the finite literal prime bank approximates the complete bank in
normalized operator norm by at most \(\varepsilon_M\). Formula (1) is a
sufficient explicit choice.

#### Proof

Equation (9) gives the assertion immediately. Solving (12) for $X(M)$
gives (1), after increasing the cutoff to the next integer. \(\square\)

The constant \(C_M\) contains the conditioning of the mode norm Gram
matrix. It need not remain bounded as modes are added. Therefore no fixed
prime head is expected to work for all $M$, and no universal growth law
for $X(M)$ follows without a quantitative conditioning theorem. This is
the precise content of the moving-average intuition.

## 4. The candidate lower-frame theorem

The direct, literal target is

\[
\boxed{
\begin{aligned}
&\mathscr E_\Gamma(q)
+\sum_{p^k\le X(M)}{\Lambda(p^k)\over p^{k/2}}
      \mathcal J_{k\log p}(q)\\
&\hspace{35mm}\ge
\left({1\over2}-\varepsilon_M\right)
\|q\|_{L^2(\mu_K)}^2,
\qquad q\in V_M,
\end{aligned}}                                     \tag{13}
\]

for one cofinal choice $X(M)\to\infty$ and one
\(\varepsilon_M\downarrow0\). It uses the ordinary values
\(\Lambda(p^k)=\log p\), not a PNT surrogate.

By (10), the cutoff can only remove a known positive remainder. Hence
(13) decomposes into two logically different estimates:

\[
\underbrace{G_{M,\infty}\ge-o(1)I}_{\text{complete signed sign}}
\qquad\text{and}\qquad
\underbrace{\|\mathcal R_{M,X(M)}\|=o(1)}_{\text{proved cutoff error}}.
                                                               \tag{14}
\]

The second assertion is Theorem 1. It does not imply the first.

If the form-norm synthesis identity

\[
\overline{\bigcup_MV_M}^{\,\|\cdot\|_{\rm form}}
=\{q:(hq)*K=0\}                                    \tag{15}
\]

is available, (13) is equivalent to nonnegativity of the complete
mean-periodic quotient and hence to RH. Without (15), it proves the sign
on the elementary spectral-synthesis closure. This is the same logical
boundary as 106.67; the present formulation specifies what an attempted
filter-bank proof must estimate.

## 5. Exact coherent counterterm

The complete Krein factorization of 106.64, restricted and normalized to
\(V_M\), is

\[
G_{M,\infty}=A_M^*A_M-(C_M^-)^*C_M^-.              \tag{16}
\]

Here \(A_M\) contains the critical and positive real-evaluation channels,
whereas \(C_M^-\) is the imaginary evaluation channel of hypothetical
off-line zero orbits. Combining (10) and (16) gives

\[
\boxed{
G_{M,X}
=A_M^*A_M-(C_M^-)^*C_M^- -\mathcal R_{M,X}.}       \tag{17}
\]

For \(\varepsilon>0\), the positive operator
\(A_M^*A_M+\varepsilon I\) is invertible. The Douglas factorization
criterion applied to (17) yields the following exact statement.

### Theorem 2 — Filter-bank contraction criterion

\[
\boxed{
G_{M,X}\ge-\varepsilon I
\quad\Longleftrightarrow\quad
\left\|
\begin{pmatrix}C_M^-\\ \mathcal R_{M,X}^{1/2}\end{pmatrix}
(A_M^*A_M+\varepsilon I)^{-1/2}
\right\|\le1.}                                    \tag{18}
\]

#### Proof

By (17), the left side is equivalent to

\[
(C_M^-)^*C_M^-+\mathcal R_{M,X}
\le A_M^*A_M+\varepsilon I.                        \tag{19}
\]

Put \(B=(C_M^-,\mathcal R_{M,X}^{1/2})^{\mathsf T}\) and
\(P=A_M^*A_M+\varepsilon I\). Then (19) is
\(B^*B\le P\), which is equivalent to
\(\|BP^{-1/2}\|\le1\). \(\square\)

Equation (18) is the requested precise counterterm. Taking more primes
makes only the second row smaller. It does not change the coherent ratio

\[
\boxed{
\Theta_M(\varepsilon)
=\|C_M^-(A_M^*A_M+\varepsilon I)^{-1/2}\|^2.}      \tag{20}
\]

An unconditional proof of \(\limsup_M\Theta_M(\varepsilon_M)\le1\),
together with the tail budget, would close (13). An off-line evaluation
channel is exactly a state on which this absorption fails.

### 5.1. The diagonal-dominance attempt

Choose any $N_M$-orthonormal mode basis $e_1,\ldots,e_{d_M}$. A
Gershgorin certificate for (13) would be

\[
 (G_{M,X})_{ii}+\varepsilon_M
 \ge\sum_{j\ne i}|(G_{M,X})_{ij}|
 \qquad(1\le i\le d_M).                            \tag{20a}
\]

Using (17), every off-diagonal entry contains the coherent counterterm

\[
 -\langle C_M^-e_i,C_M^-e_j\rangle.                \tag{20b}
\]

Neither positivity of the prime weights nor Cauchy--Schwarz fixes the sign
of the sum of (20b). Cauchy--Schwarz merely replaces it by the product of
the two negative-channel diagonal masses, and summing those products over
the row can lose a factor $d_M$. PNT estimates the positive spatial-tail
quadrature; it supplies no cancellation for (20b).

There is also no basis-free content hidden in (20a). In an eigenbasis of
$G_{M,X}$, (20a) is exactly the desired eigenvalue inequality, while in a
different mode basis it is strictly stronger and can fail for a positive
matrix. Thus diagonal dominance is a possible computational certificate
after all entries are enclosed, but not a mechanism which derives the sign
from prime density. The invariant form of the same question is (18).

## 6. What multiplicative independence proves

For every proper finite head, the omitted bank is strictly positive on a
nonzero finite zero-mode vector:

\[
q^*\mathcal R_{M,X}q>0.                             \tag{21}
\]

Indeed, vanishing on two omitted primes would make $q$ periodic with
periods \(\log p\) and \(\log r\); rational independence of these periods
makes a continuous $q$ constant, and centering makes it zero. This is
the exact use of unique factorization in the present problem.

But (21) is injectivity, not a lower frame bound. It gives a positive
smallest singular value for each fixed finite-dimensional problem, with no
uniform control as $M\to\infty$. Phase 50 already shows why the usual
upgrade fails: Kronecker independence also produces arbitrarily close
phase returns, and the corresponding unweighted prime-character system
has zero uniform Riesz lower bound. The physical theta weight changes the
operator, so that observation is not a counterexample to (13); it is a
counterexample to the inference

\[
\text{rational independence}\Longrightarrow
\text{uniform quantitative lower frame bound}.     \tag{22}
\]

In (18), multiplicative independence sees only the strict positivity of
\(\mathcal R_{M,X}\). It gives no estimate for \(\Theta_M\).

## 7. What PNT proves, and the compact term it leaves

The moving-PNT quadrature of 106.47 proves the spatial tail floor

\[
\mathscr E_K(f)\ge(1/2-o(1))\|f\|^2
\quad\text{for states escaping to }|x|\to\infty.   \tag{23}
\]

Together with local Gamma compactness, this gives

\[
\sigma_{\rm ess}(L|_{\mathbf1^\perp})\subset[1/2,\infty).           \tag{24}
\]

This is precisely the part of the filter-bank picture that PNT can prove:
far out in the physical coordinate, primes in a moving multiplicative
window become a continuum average. It already rules out a diffuse or
essential subthreshold channel.

What remains below $1/2$ is an isolated finite-multiplicity bound state
localized in the central region. Increasing the real part of a zero mode
increases its oscillation in that central region; it does not move the mode
to large physical $x$, where PNT quadrature applies. Meanwhile a new
prime $p>X$ enters at displacement \(\log p\), and its theta overlap is
\(O(e^{-cp})\). Thus the asymptotic prime density controls the already
small remainder \(\mathcal R_{M,X}\), whereas the localized coherent
alignment is \(C_M^-\) in (18).

This is the precise geometric mismatch:

\[
\boxed{
\begin{array}{c|c}
\text{PNT / more large primes}&\text{physical tail and cutoff error}\\
\hline
\text{missing sign}&\text{compact central bound-state alignment}
\end{array}}                                       \tag{25}
\]

The positive atomic resonance model of 105.05 and the ordinary-prime-
support deformation of 104.90 further show that PNT/VK, positivity and
prime support do not control this central alignment. They do not refute
the literal weights \(\Lambda(n)\); they prove that a successful argument
must use the exact joint correlations of all ordinary prime towers, not a
PNT envelope.

## 8. Why positive moving averages cannot improve the largest head

Let (X_1,\ldots,X_J\le X_*\), let \(\alpha_j\ge0\), and
\(\sum_j\alpha_j=1\). Then

\[
\begin{aligned}
\overline G_M
&=\sum_j\alpha_jG_{M,X_j}
=G_{M,\infty}-\sum_j\alpha_j\mathcal R_{M,X_j}\\
&\le G_{M,\infty}-\mathcal R_{M,X_*}
=G_{M,X_*}.                                        \tag{26}
\end{aligned}
\]

Thus Cesàro, exponentially weighted, trimmed, and other positive averages
can stabilize a numerical estimate, but none can outperform the largest
prime head already present. This is not a failure of the signal analogy:
it says the bank is **nested**, so averaging partial banks reintroduces a
portion of the omitted positive channels.

Signed extrapolation weights could overshoot the complete bank, but would
destroy the positive-square decomposition and would require a new signed
remainder theorem. No such extrapolation is used here.

## 9. The surviving theorem

The moving-mode insight therefore has a rigorous final form:

\[
\boxed{
\begin{gathered}
M\uparrow\infty\quad\Longrightarrow\quad
X(M)\uparrow\infty\text{ chosen by (1)},\\
\|G_{M,X(M)}-G_{M,\infty}\|\le\varepsilon_M,\\
\text{and the sole remaining estimate is }\Theta_M(\varepsilon_M)\le1
\text{ with the tail row included as in (18).}
\end{gathered}}                                     \tag{27}
\]

The first two lines are proved. The last line is the literal ordinary-
prime coherent-absorption inequality. It is not a diagonal consequence of
PNT or multiplicative independence; it is the compact signed theorem which
would exclude every subthreshold bound state.
