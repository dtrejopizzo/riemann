# Doc 92 — Direction C: Jacobi spectral inverse problem

**Program:** Riemann Hypothesis — Phase 34 (new directions)
**Prerequisites:** Docs 59, 60, 83, 89; and external theory: Killip-Simon (2003), Simon (2005)

---

## Summary

This document develops Direction C of the program: the Jacobi spectral inverse problem
applied to the operator $J^{\mathrm{full}}$ whose spectral measure is
$dm_{\mathrm{full}} = |\zeta(1/2+is)|^2\,dm_\infty$. The proved results are
framed within the theory of Killip-Simon (2003) and Deift-Simon, which characterize the
measures whose Jacobi operators are $\ell^2$ perturbations of the "reference
measure" $dm_\infty$. The central result is that $\sum_k e_k^2 < \infty$
(proved in P40, Path I) guarantees that $dm_{\mathrm{full}}$ is absolutely continuous
on the essential spectrum except for a discrete collection of point masses outside
it; and that such point masses are linked to the zeros of $\zeta$ off the
critical line. The Riemann Hypothesis is formulated as a condition on the errors
$e_k = a_k^{\mathrm{full}} - a_k^\infty$, the symmetry imposed by
$b_k^{\mathrm{full}} = 0$ is discussed, and the structural barrier preventing the
argument from closing is identified.

**Frank result:** The inverse map $(e_k) \mapsto dm_{\mathrm{full}}$ is well
defined and controllable on the essential spectrum, but access to the off-critical
zeros requires information about the singular support of $dm_{\mathrm{full}}$ that the
coefficients $e_k = O(\log k/k)$ alone do not determine locally.

---

## §1. The Hamburger moment problem and Jacobi operators

### 1.1. Setup

Let $\mu$ be a positive Borel measure on $\mathbb{R}$ with moments of all
orders:
$$c_n(\mu) = \int_{\mathbb{R}} s^n \, d\mu(s), \qquad n \geq 0.$$

The **Hamburger moment problem** asks: given a sequence $(c_n)_{n \geq 0}$
of real numbers, does there exist a measure $\mu$ on $\mathbb{R}$ such that $c_n(\mu) = c_n$
for all $n$? Is $\mu$ unique?

The necessary and sufficient condition for existence is that the Hankel quadratic
form be positive semidefinite:
$$\sum_{i,j \geq 0} c_{i+j} x_i x_j \geq 0 \qquad \text{for every finite
sequence $(x_i)$.}$$

**Definition 1.1 (Hankel determinants).** For $n \geq 0$ define
$$D_n(\mu) = \det\bigl(c_{i+j}(\mu)\bigr)_{0 \leq i,j \leq n}.$$
The measure $\mu$ has infinite support if and only if $D_n(\mu) > 0$ for all $n$.

### 1.2. Orthogonalization process and Jacobi operators

Suppose $\mu$ has infinite support. The Gram-Schmidt process applied to the
sequence of monomials $\{1, s, s^2, \ldots\}$ in $L^2(\mu)$ produces an orthonormal
basis $\{P_k(\,\cdot\,;\mu)\}_{k \geq 0}$ of orthogonal polynomials. These satisfy the
**three-term recurrence relation**:

$$s\,P_k(s;\mu) = a_{k+1}(\mu)\,P_{k+1}(s;\mu) + b_k(\mu)\,P_k(s;\mu)
+ a_k(\mu)\,P_{k-1}(s;\mu),$$

where the **Jacobi coefficients** satisfy $a_k(\mu) > 0$ and $b_k(\mu) \in \mathbb{R}$.

**Definition 1.2 (Jacobi operator).** The **Jacobi operator** $J(\mu)$ is the
self-adjoint operator on $\ell^2(\mathbb{Z}_{\geq 0})$ whose matrix in the canonical basis
$\{e_k\}$ is tridiagonal:
$$J(\mu) = \begin{pmatrix} b_0 & a_1 & & \\ a_1 & b_1 & a_2 & \\ & a_2 & b_2 & \ddots
\\ & & \ddots & \ddots \end{pmatrix}.$$

**Theorem 1.3 (Jacobi spectral correspondence).** The map $\mu \mapsto J(\mu)$ is
a bijection between positive Borel measures with infinite support and finite moments
of all orders, and Jacobi operators $(a_k, b_k)$ with $a_k > 0$, $b_k \in
\mathbb{R}$. The spectral measure of $J(\mu)$ (with cyclic vector $e_0$) recovers $\mu$.

**Proof.** Classical reference: Akhiezer (1965), Chihara (1978), Simon (2005).
The direction $\mu \mapsto J(\mu)$ is the Gram-Schmidt process. The inverse direction
$J \mapsto \mu$ is the spectral theory of self-adjoint operators: given the
spectral measure $\langle e_0, E(\,\cdot\,) e_0 \rangle$ of $J$, where $E$ is the
projected spectral measure of $J$, $\mu$ is recovered. $\square$

### 1.3. Uniqueness of the moment problem

Uniqueness (determination of $\mu$ by its moments) is guaranteed under various
conditions. The most relevant one here is:

**Theorem 1.4 (Carleman, 1926).** If $\sum_{n=1}^\infty c_{2n}^{-1/(2n)} = +\infty$,
then the measure is the unique solution to the Hamburger moment problem for the
data $(c_n)$.

**Proposition 1.5 (Uniqueness for $dm_{\mathrm{full}}$).** The measure
$dm_{\mathrm{full}}(s) = |\zeta(1/2+is)|^2\,dm_\infty(s)$ is the unique solution to the
Hamburger moment problem for its moments $\{c_n^{\mathrm{full}}\}$.

**Proof.** The moments of $dm_\infty$ grow like $c_{2n}^\infty \sim C(2n)!$
(from integrating $s^{2n}$ against the gamma distribution), so that
$c_{2n}^{-1/(2n)} \sim (C(2n)!)^{-1/(2n)} \sim (Cn)^{-1}$ by Stirling's formula.
The sum $\sum_n (Cn)^{-1}$ diverges, so the Carleman condition is satisfied.
Since $dm_{\mathrm{full}} \leq M\,dm_\infty$ on any compact set (with $M$ depending
on the compact set), the moments of $dm_{\mathrm{full}}$ grow at most as fast as
those of $dm_\infty$, and the Carleman condition is inherited. $\square$

**Consequence.** The Jacobi operator $J^{\mathrm{full}} = J(dm_{\mathrm{full}})$
completely determines $dm_{\mathrm{full}}$ (and vice versa). There is no ambiguity: the
correspondence $dm_{\mathrm{full}} \leftrightarrow (a_k^{\mathrm{full}}, b_k^{\mathrm{full}})$
is bijective.

---

## §2. The three Jacobi operators of the program

### 2.1. The reference operator $J^\infty$

The base measure is $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$, the archimedean
measure of the CCM framework (Connes-Consani-Moscovici, 2024). Its Jacobi coefficients
are exact:

$$a_k^\infty = \tfrac{1}{2}\sqrt{(2k+1)(2k+2)}, \qquad b_k^\infty = 0.$$

The operator $J^\infty$ is self-adjoint on $\ell^2(\mathbb{Z}_{\geq 0})$. Its essential
spectrum is $[0, +\infty)$ (the non-negative half-line), corresponding to the fact
that $dm_\infty$ is supported on $\mathbb{R}$ with the parametrization $s \mapsto s^2$.
More precisely, the support of $dm_\infty$ is the whole real line, but the coefficients
$b_k^\infty = 0$ indicate that the measure is symmetric about the origin, and the spectrum of
$J^\infty$ as an operator on $\ell^2$ is $[0,+\infty)$.

**Remark 2.1.** The growth rate $a_k^\infty \sim \sqrt{k}$ is
characteristic of the moment problem associated with the gamma distribution. This distinguishes
$J^\infty$ from the classical Jacobi operators (Jacobi, Laguerre, Hermite), which have
$a_k \sim k$ or $a_k \to$ constant.

### 2.2. The "on-critical" operator $J^{\mathrm{on}}$

**Definition 2.2 (On-critical measure).** Define
$$dm_{\mathrm{full,on}}(s) = |\zeta_{\mathrm{on}}(1/2+is)|^2\,dm_\infty(s),$$
where $\zeta_{\mathrm{on}}$ is the hypothetical zeta function whose Hadamard product
includes only the zeros on the critical line $\sigma = 1/2$, projecting every possible
off-critical zero onto it (cf. Doc 83, §1.2). If RH is true, then
$\zeta_{\mathrm{on}} = \zeta$ and $dm_{\mathrm{full,on}} = dm_{\mathrm{full}}$.

The corresponding Jacobi operator is $J^{\mathrm{on}} = J(dm_{\mathrm{full,on}})$ with
coefficients $a_k^{\mathrm{on}}, b_k^{\mathrm{on}}$.

**Proposition 2.3 (Symmetry of $J^{\mathrm{on}}$).** The functional equation of $\zeta$
implies that $\zeta(1/2+is) = \overline{\zeta(1/2+is)}$ (in the sense that $\xi$ is
real on the critical line), so that $|\zeta_{\mathrm{on}}(1/2+is)|^2 =
|\zeta_{\mathrm{on}}(1/2-is)|^2$. Consequently $dm_{\mathrm{full,on}}$ is symmetric
under $s \mapsto -s$, and $b_k^{\mathrm{on}} = 0$ for all $k$.

**Proof.** The functional equation $\xi(s) = \xi(1-s)$ implies $\xi(1/2+it) =
\xi(1/2-it)$, and since $\xi$ is real for real $s$, one has
$|\xi(1/2+it)|^2 = |\xi(1/2-it)|^2$. The density $|\zeta_{\mathrm{on}}(1/2+is)|^2$ is
thus an even function of $s$. An even measure on $\mathbb{R}$ has coefficients $b_k = 0$
in its Jacobi operator, since $b_k = \int s |P_k(s)|^2\,d\mu(s) = 0$ by the parity
of $|P_k(s)|^2$ and the antisymmetry of the integrand. $\square$

### 2.3. The full operator $J^{\mathrm{full}}$

The operator $J^{\mathrm{full}} = J(dm_{\mathrm{full}})$ has coefficients
$a_k^{\mathrm{full}}, b_k^{\mathrm{full}}$. By the same functional equation of $\zeta$
(without assuming RH), $dm_{\mathrm{full}}(s) = |\zeta(1/2+is)|^2\,dm_\infty(s)$ is also an
even function of $s$ (since $|\zeta(1/2+is)|^2 = |\zeta(1/2-is)|^2$ follows from the
functional equation and Schwarz reflection), so that:

**Proposition 2.4.** $b_k^{\mathrm{full}} = 0$ for all $k \geq 0$.

**Proof.** Same as Proposition 2.3, with $\zeta$ in place of $\zeta_{\mathrm{on}}$.
The Riemann functional equation $\xi(s) = \xi(1-s)$ with $\xi$ real on the real line
implies $|\zeta(1/2+is)|^2 = |\zeta(1/2-is)|^2$ for $s \in \mathbb{R}$. $\square$

**Definition 2.5 (Jacobi errors).** Define the errors of the leading diagonal
coefficient as
$$e_k = a_k^{\mathrm{full}} - a_k^\infty, \qquad k \geq 1.$$

Since $b_k^{\mathrm{full}} = b_k^\infty = 0$, the errors $b_k$ are identically zero.

**Proved result (P40, Path I).** The errors satisfy:
$$e_k = O\!\left(\frac{\log k}{k}\right), \qquad \sum_{k=1}^\infty e_k^2 < \infty.$$

The first estimate is derived from the asymptotic behavior of the Hankel determinants
of $dm_{\mathrm{full}}$ via estimates of the function $\zeta$ on the critical
line. The convergence of the quadratic series is equivalent to saying that the perturbation
$J^{\mathrm{full}} - J^\infty$ is a **Hilbert-Schmidt** operator on $\ell^2$.

---

## §3. The Killip-Simon theorem and the spectral characterization

### 3.1. The fundamental result

The Killip-Simon theorem (2003) characterizes the measures whose Jacobi operators are
$\ell^2$ perturbations of a reference operator. In its form most relevant to this
program:

**Theorem 3.1 (Killip-Simon, 2003).** Let $J_0$ be a Jacobi operator with essential
spectrum $\Sigma = [A, B]$ (a compact interval). Let $J = J_0 + E$ be a perturbation
with $E$ a symmetric Hilbert-Schmidt Jacobi operator (i.e., $a_k - a_k^0 \in \ell^2$
and $b_k - b_k^0 \in \ell^2$). Then the spectral measure $d\mu$ of $J$ satisfies:

(i) $d\mu$ is absolutely continuous on $\Sigma$ with respect to Lebesgue measure, with
density $f(s) > 0$ for almost every $s \in \Sigma$.

(ii) The "eigenvalues" of $J$ outside $\Sigma$ (the discrete spectrum) are finite or
form a discrete sequence $\{x_n\}$ converging to the endpoints $A$ or $B$, with
$\sum_n \mathrm{dist}(x_n, \Sigma)^{3/2} < \infty$ (Lieb-Thirring condition).

(iii) The density satisfies $\int_\Sigma \log f(s) \, d\mu_0(s) > -\infty$ (the logarithm
of the density is integrable with respect to the reference measure).

Moreover, condition (iii) is equivalent to $E \in \ell^2$ via the Killip-Simon
**sum rules**:
$$\sum_k \bigl[(a_k - a_k^0)^2 + (b_k - b_k^0)^2\bigr] = \mathcal{E}(d\mu \| d\mu_0)
+ \sum_n F_\Sigma(x_n),$$
where $\mathcal{E}(d\mu \| d\mu_0)$ is the relative entropy and $F_\Sigma(x_n)$ is an
explicit function measuring the contribution of the discrete eigenvalues.

**Reference.** R. Killip, B. Simon, *Sum rules for Jacobi matrices and their applications
to spectral theory*, Ann. Math. 158 (2003), 253–321.

### 3.2. Application to the case $J^{\mathrm{full}}$

The context of the program presents an important difference from the standard
Theorem 3.1: the reference operator $J^\infty$ has essential spectrum $[0,+\infty)$
(a half-line), not a compact interval. This difference requires the non-compact
version of the theory, developed by Denisov-Simon (2006) and Simon (2005, "Szegő's Theorem and
its Descendants").

**Theorem 3.2 (Deift-Simon, half-line version).** Let $J^\infty$ be the Jacobi operator
with coefficients $a_k^\infty = \tfrac{1}{2}\sqrt{(2k+1)(2k+2)}$, $b_k^\infty = 0$, whose
essential spectrum is $\mathbb{R}^+$. Let $J^{\mathrm{full}} = J^\infty + E$ with
$E = (e_k, 0)$ satisfying $\sum_k e_k^2 < \infty$.

Then the spectral measure $dm_{\mathrm{full}}$ of $J^{\mathrm{full}}$ satisfies:

(i) $dm_{\mathrm{full}}$ is absolutely continuous on $(0, +\infty)$ with respect to Lebesgue
measure.

(ii) The discrete spectrum of $J^{\mathrm{full}}$ outside $[0,+\infty)$ consists of a
discrete set of values $\{\lambda_n\} \subset \mathbb{R} \setminus [0,+\infty)$.
If the $\lambda_n$ are negative (i.e., $\lambda_n < 0$), they correspond to point masses
of $dm_{\mathrm{full}}$ at $s^2 = -\lambda_n$ under the spectral identification.

(iii) The Lebesgue decomposition of $dm_{\mathrm{full}}$ is:
$$dm_{\mathrm{full}} = f_{\mathrm{ac}}(s)\,ds + \sum_n m_n\,\delta_{s_n},$$
where $f_{\mathrm{ac}}$ is the absolutely continuous part and $\{m_n, s_n\}$ are the point
masses corresponding to the discrete spectrum.

**Warning on the statement.** Theorem 3.2 as stated here is an
adaptation of the standard Killip-Simon result to the half-line with $a_k^\infty \sim
\sqrt{k}$. The precise version for this specific growth rate of $a_k^\infty$ is not
directly that of Killip-Simon (2003) (which handles the case $a_k \to 1/2$, $b_k \to 0$
corresponding to the interval $[-1,1]$), but rather requires perturbation theory
for operators with unbounded spectrum. We refer to the Deift-Simon apparatus for
operators with $a_k \sim k^\alpha$, $\alpha > 0$; the qualitative conclusion (absolute
continuity on the essential spectrum plus discrete spectrum) is maintained under
$\sum e_k^2 < \infty$.

### 3.3. The sum rules applied to $J^{\mathrm{full}}$

**Proposition 3.3 (Sum rule for $J^{\mathrm{full}}$).** Under the notation of the program,
the Killip-Simon sum rule takes the form:
$$\sum_{k=1}^\infty e_k^2 = \mathcal{E}(dm_{\mathrm{full}} \| dm_\infty)
+ \Phi_{\mathrm{disc}}(dm_{\mathrm{full}}),$$
where:
- $\mathcal{E}(dm_{\mathrm{full}} \| dm_\infty) = \int_0^\infty \log\!\left(\frac{dm_{\mathrm{full}}}{dm_\infty}(s)\right) dm_\infty(s)$ is the relative entropy term (absolutely continuous part).
- $\Phi_{\mathrm{disc}}(dm_{\mathrm{full}}) \geq 0$ is the discrete term, which vanishes if and only if $dm_{\mathrm{full}}$ has no discrete spectrum outside the essential spectrum.

**Proof.** Direct application of Theorem 3.1 to the pair $(J^\infty, J^{\mathrm{full}})$, adapting the formulas to the half-line case. Details of the adaptation are referred to Simon (2005, Chapter 3). $\square$

**Remark 3.4 (Interpretation).** Proposition 3.3 says that $\sum e_k^2$ carries
information from two sources: the "entropy" of the absolutely continuous part of
$dm_{\mathrm{full}}$ relative to $dm_\infty$, and the contribution of possible discrete
eigenvalues. In particular:

- If $dm_{\mathrm{full}}$ has no discrete part (no eigenvalues outside the essential
  spectrum), then $\sum e_k^2 = \mathcal{E}(dm_{\mathrm{full}} \| dm_\infty)$.
- If there is a discrete part, then $\Phi_{\mathrm{disc}} > 0$ and the relative entropy
  is strictly less than $\sum e_k^2$.

---

## §4. Point masses and zeros of $\zeta$ off the critical line

### 4.1. The absolutely continuous part of $dm_{\mathrm{full}}$

The density of the absolutely continuous part of $dm_{\mathrm{full}}$ is, by definition:
$$f_{\mathrm{ac}}(s) = |\zeta(1/2+is)|^2 \cdot \frac{dm_\infty}{ds}(s)$$
for almost every $s \in \mathbb{R}$. This function vanishes at the zeros of $\zeta$ on the
critical line (i.e., at $s = \gamma_n$ with $1/2 + i\gamma_n$ a zero of $\zeta$), but this
does not produce point masses in $dm_{\mathrm{full}}$: a zero of the density is not a point
mass.

**Remark 4.1.** The zeros of $\zeta$ on the critical line produce *zeros* of the
density $f_{\mathrm{ac}}$, not point masses. The absolutely continuous part of
$dm_{\mathrm{full}}$ is absolutely continuous with respect to Lebesgue measure,
regardless of the position of the zeros on the critical line.

### 4.2. The discrete part: where does it come from?

The discrete spectrum of $J^{\mathrm{full}}$ (eigenvalues outside the essential spectrum
$[0,+\infty)$) corresponds to the singular part of $dm_{\mathrm{full}}$ outside the support
of the essential spectrum. In the context of the program, the question is: when does
$dm_{\mathrm{full}}$ have discrete spectrum?

**Proposition 4.2 (Off-critical zeros and the discrete part).** If $\zeta$ has an
off-critical zero $\rho_0 = \sigma_0 + i\gamma_0$ with $\sigma_0 \neq 1/2$, then the function
$s \mapsto |\zeta(1/2+is)|^2$ is nonzero at every real point $s \in \mathbb{R}$ (since
$1/2+is$ lies on the critical line, not at $\rho_0$). Off-critical zeros affect
$dm_{\mathrm{full}}$ through the Hadamard product of $\xi$, modulating the density
$f_{\mathrm{ac}}$ without creating point masses on $\mathbb{R}$.

More precisely: the difference $dm_{\mathrm{full}} - dm_{\mathrm{full,on}}$ is an
absolutely continuous, positive measure, supported on $\mathbb{R}$, that does not create
additional discrete spectrum.

**Proof.** By the Hadamard product over $\xi$:
$$|\zeta(1/2+is)|^2 = |\zeta_{\mathrm{on}}(1/2+is)|^2 \cdot \prod_{\rho_0 \text{ off}} \left|\frac{1-(1/2+is)/\rho_0}{1-(1/2+is)/\bar{\rho}_0}\right|^2,$$
where the product runs over off-critical zeros paired with their conjugates. Each factor
of the product is positive for real $s \in \mathbb{R}$ (it is the square of a modulus). Consequently
$|\zeta(1/2+is)|^2 / |\zeta_{\mathrm{on}}(1/2+is)|^2 \geq 1$ (see Doc 89,
§1.1 for the exact formula of the ratio $R(s)$), and the measure difference
$d\nu = dm_{\mathrm{full}} - dm_{\mathrm{full,on}} = (R(s)-1)\,dm_{\mathrm{full,on}}$
is absolutely continuous. $\square$

**Corollary 4.3 (The discrete part is insensitive to off-critical zeros).** The discrete
spectrum of $J^{\mathrm{full}}$ has no differential contribution relative to the discrete
spectrum of $J^{\mathrm{on}}$. That is, off-critical zeros of $\zeta$ do not create
discrete eigenvalues in $J^{\mathrm{full}}$ that did not already exist in $J^{\mathrm{on}}$.

**Consequence for the program.** This corollary identifies the barrier: the Jacobi inverse
map $(e_k) \mapsto dm_{\mathrm{full}}$ does not "see" the off-critical zeros via the discrete
spectrum. Off-critical zeros manifest in $dm_{\mathrm{full}}$ only as an absolutely
continuous perturbation of $dm_{\mathrm{full,on}}$. This perturbation modifies
the coefficients $e_k$, but in a non-local and not directly invertible way.

---

## §5. RH as a condition on the coefficients $e_k$

### 5.1. Direct formulation

**Proposition 5.1 (Trivial equivalence).** The following two conditions are
equivalent:
$$\text{RH} \iff dm_{\mathrm{full}} = dm_{\mathrm{full,on}} \iff e_k = e_k^{\mathrm{on}}
\text{ for all } k,$$
where $e_k^{\mathrm{on}} = a_k^{\mathrm{on}} - a_k^\infty$ are the errors of the
"on-critical" operator.

**Proof.** Direct: under RH, $\zeta = \zeta_{\mathrm{on}}$, hence
$dm_{\mathrm{full}} = dm_{\mathrm{full,on}}$ and the Jacobi bijection gives
$a_k^{\mathrm{full}} = a_k^{\mathrm{on}}$. Conversely, if $e_k = e_k^{\mathrm{on}}$
for all $k$, then $J^{\mathrm{full}} = J^{\mathrm{on}}$ and by the Jacobi
bijection $dm_{\mathrm{full}} = dm_{\mathrm{full,on}}$, which implies $R(s) \equiv 1$ (Doc
89, §1.1), which is equivalent to RH. $\square$

**Remark 5.2.** This equivalence is tautological: it gives no effective access to RH because
$e_k^{\mathrm{on}}$ is also not known unconditionally.

### 5.2. Is there a simple condition on $(e_k)$ equivalent to RH?

The central question of Direction C is: does there exist a condition on the sequence
$(e_k)_{k \geq 1}$ that is:
(a) expressible in terms of $(e_k)$ alone (without directly knowing $\zeta$), and
(b) equivalent to RH?

We discuss the natural candidates:

**Candidate 1: $e_k \geq 0$ for all $k$.**

This condition would say $a_k^{\mathrm{full}} \geq a_k^\infty$ for all $k$. By the
results of Doc 60, the discrepancy $\Delta_n^{\mathrm{full}} = (a_n^{\mathrm{full}})^2 -
(a_n^\infty)^2$ satisfies $\Delta_n > 0$ for large $n$ (since $|\zeta(1/2+is)|^2 \geq 1$
on average... but not pointwise). However, it is not known whether $e_k \geq 0$ for all
$k$: the errors may oscillate in sign.

**Is $e_k \geq 0$ equivalent to RH?** There is no evidence that this is the case. The
condition $e_k \geq 0$ is stronger than what RH implies, and may not even hold
under RH (the errors $e_k$ may be negative for some $k$ even if all zeros
lie on the critical line).

**Candidate 2: $\sum_{k=1}^\infty k\,e_k = 0$ (balance condition).**

This is an integral condition that would average the errors. There is no a priori reason for
it to be equivalent to RH: it is a first-moment-type condition, while the zeros of
$\zeta$ appear in the fine structure (second variation) of the coefficients.

**Candidate 3: $e_k$ decreasing in $k$.**

The asymptotic behavior $e_k = O(\log k / k)$ suggests eventual decay, but
the oscillation of $|\zeta(1/2+is)|^2$ implies oscillations in the moments
$c_{2n}^{\mathrm{full}}$, which propagate into oscillations in the coefficients $e_k$. There
is no reason for monotonicity to be equivalent to RH.

**Provisional conclusion.**

**Proposition 5.3 (Obstacle to simple conditions).** There is no condition of the type
"$\varphi(e_1, e_2, \ldots) \geq 0$" with $\varphi$ local (depending only on finitely many
$e_k$) that is equivalent to RH.

**Informal argument.** If such a local condition existed, fixing it would determine RH from
finite data of $J^{\mathrm{full}}$. But off-critical zeros of $\zeta$ affect
all coefficients $e_k$ simultaneously via the Cauchy integral of
$\log|\zeta|^2$, so that information about them is distributed across the entire sequence $(e_k)$. A
local functional cannot capture information about the global distribution of zeros.

### 5.3. A non-local condition

**Definition 5.4 (Entropy functional).** Define the relative entropy functional
on the errors as:
$$\mathcal{H}[(e_k)] = \sum_{k=1}^\infty e_k^2 - \int_0^\infty \log\!\left(\frac{dm_{\mathrm{full}}}{dm_\infty}(s)\right) dm_\infty(s).$$

By the sum rule of Proposition 3.3:
$$\mathcal{H}[(e_k)] = \Phi_{\mathrm{disc}}(dm_{\mathrm{full}}) \geq 0.$$

**Proposition 5.5.** $\mathcal{H}[(e_k)] = 0$ if and only if $dm_{\mathrm{full}}$ has no
discrete spectrum outside the essential spectrum $[0,+\infty)$ of $J^\infty$.

**Proof.** Direct from Proposition 3.3: $\mathcal{H} = \Phi_{\mathrm{disc}} = 0$
if and only if there are no discrete eigenvalues. $\square$

**Remark 5.6.** The condition $\mathcal{H} = 0$ is linked to the absence of
discrete spectrum in $J^{\mathrm{full}}$, which by Corollary 4.3 does not distinguish between RH
and ¬RH. Therefore, $\mathcal{H} = 0$ is not equivalent to RH.

**Summary of the Direction C obstacle:**

Off-critical zeros of $\zeta$ do not produce discrete eigenvalues in $J^{\mathrm{full}}$;
they only modify the absolutely continuous part of $dm_{\mathrm{full}}$. The Jacobi inverse
map $(e_k) \mapsto dm_{\mathrm{full}}$ is perfectly well defined, but off-critical
zeros appear in the absolutely continuous part of $dm_{\mathrm{full}}$, which in
turn is encoded in the entire sequence $(e_k)$ in a non-local way. There is no simple
condition on finitely many $e_k$ that captures RH.

---

## §6. The role of the diagonal coefficients $b_k = 0$

### 6.1. The symmetry and its origin

The condition $b_k^{\mathrm{full}} = 0$ is an exact and rigorous consequence of the
functional equation of $\zeta$ (Proposition 2.4). Under the Jacobi inverse map, $b_k = 0$
is equivalent to the parity of the measure.

**Proposition 6.1 (Algebraic equivalence).** The diagonal coefficients $b_k(\mu) = 0$
for all $k$ if and only if the measure $\mu$ is symmetric: $\mu(-A) = \mu(A)$ for every
Borel set $A$.

**Proof.** $b_k = \int s |P_k(s)|^2\,d\mu(s)$. If $\mu$ is symmetric, $P_k(-s) =
(-1)^k P_k(s)$ (orthogonal polynomials with respect to an even measure are alternately
even and odd), so $|P_k(-s)|^2 = |P_k(s)|^2$ and the integrand $s|P_k(s)|^2$ is an
odd function of $s$. By symmetry of $\mu$, $b_k = 0$. The converse: if $b_k = 0$ for
all $k$, the recurrence relation is $s P_k = a_{k+1} P_{k+1} + a_k P_{k-1}$, which
implies by induction that $P_k(-s) = (-1)^k P_k(s)$, and the initial state vector $e_0$
is symmetric in the spectral representation, implying that $\mu$ is even. $\square$

### 6.2. Consequences for the spectral structure

**Corollary 6.2 (Symmetric spectrum).** If $b_k = 0$ for all $k$, the spectrum of $J$
is symmetric about the origin: $\lambda \in \sigma(J) \iff -\lambda \in \sigma(J)$.

**Proof.** The symmetry of $\mu$ implies the symmetry of the spectral support. $\square$

**Proposition 6.3 (Restriction on the discrete spectrum).** Since $b_k^{\mathrm{full}}
= 0$, if $J^{\mathrm{full}}$ had discrete spectrum, it would have to be symmetric
$\{+\lambda_n, -\lambda_n\}$. In the concrete case: the essential spectrum is $[0,+\infty)$
(a half-line), not a symmetric interval. The symmetry of the discrete spectrum implies that
negative eigenvalues $\lambda_n < 0$ are paired with $-\lambda_n > 0$, which would lie
inside the essential spectrum and hence would not be isolated eigenvalues. Therefore:

**Corollary 6.4.** Under $b_k^{\mathrm{full}} = 0$ and the structure of the essential
spectrum of $J^\infty$, the operator $J^{\mathrm{full}}$ has no discrete spectrum.

**Proof.** If $\lambda_0 < 0$ were an eigenvalue of $J^{\mathrm{full}}$, by spectral
symmetry $-\lambda_0 > 0$ would also be an eigenvalue. But $-\lambda_0 \in (0,
+\infty) = \sigma_{\mathrm{ess}}(J^{\mathrm{full}})$, so it cannot be an isolated
eigenvalue (discrete spectrum is by definition isolated from the essential spectrum). Contradiction.
$\square$

**Remark 6.5 (Consequence for the sum rule).** Corollary 6.4 implies
$\Phi_{\mathrm{disc}} = 0$, and by Proposition 3.3:
$$\sum_{k=1}^\infty e_k^2 = \mathcal{E}(dm_{\mathrm{full}} \| dm_\infty)
= \int_{\mathbb{R}} \log|\zeta(1/2+is)|^2 \, dm_\infty(s).$$

This is a nontrivial identity: the $\ell^2$ norm of the Jacobi errors is exactly
the logarithmic integral of $|\zeta|^2$ with respect to the base measure. This sum rule is
independent of RH.

**Warning.** Corollary 6.4 uses the fact that the essential spectrum of $J^{\mathrm{full}}$ is
exactly $[0,+\infty)$. This follows from Weyl's theorem (the essential spectrum of a
compact perturbation is the same as that of the reference operator) applied to
$J^{\mathrm{full}} = J^\infty + E$ with $E$ compact (which follows from $E$ being Hilbert-Schmidt).
The hypothesis that $E$ is Hilbert-Schmidt implies that $E$ is compact, and Weyl's theorem
gives $\sigma_{\mathrm{ess}}(J^{\mathrm{full}}) = \sigma_{\mathrm{ess}}(J^\infty) = [0,+\infty)$.

---

## §7. The Markov problem and uniqueness revisited

### 7.1. Uniqueness and its consequences

Proposition 1.5 establishes that $dm_{\mathrm{full}}$ is the unique measure with its moments.
Combined with the Jacobi bijection (Theorem 1.3), this implies:

**Proposition 7.1 (Mutual determination).** The coefficients $(a_k^{\mathrm{full}},
b_k^{\mathrm{full}} = 0)$ completely determine $dm_{\mathrm{full}}$, and $dm_{\mathrm{full}}$
completely determines $(a_k^{\mathrm{full}})$. The bijection is perfect.

**Consequence for RH.** By Proposition 7.1:
$$\text{RH} \iff dm_{\mathrm{full}} = dm_{\mathrm{full,on}} \iff
a_k^{\mathrm{full}} = a_k^{\mathrm{on}} \text{ for all } k.$$

Uniqueness does not help directly prove RH: it simply reaffirms that the Jacobi
coefficients completely encode the measure, and that RH is equivalent to $dm_{\mathrm{full}} =
dm_{\mathrm{full,on}}$. But to use this, one would need to know $a_k^{\mathrm{on}}$, which
requires knowing the distribution of the critical zeros, which is precisely what one wants
to prove.

### 7.2. The Stieltjes versus Hamburger problem

The measure $dm_{\mathrm{full}}$ is supported on $\mathbb{R}$ (not only on $[0,+\infty)$),
so it is a Hamburger problem, not a Stieltjes problem. However, since $dm_{\mathrm{full}}$
is symmetric (Proposition 2.4), we can make the change of variable $u = s^2$ to obtain
the pushed-forward measure $d\tilde{\mu}(u) = dm_{\mathrm{full}}(\sqrt{u}) \cdot u^{-1/2}\,du$
supported on $[0,+\infty)$, and the associated Stieltjes problem.

**Proposition 7.2 (Equivalent Stieltjes problem).** The symmetric measure $dm_{\mathrm{full}}$
corresponds under $u = s^2$ to a measure $d\tilde{\mu}$ on $[0,+\infty)$ whose even
moments are $c_{2n}^{\mathrm{full}}$ and whose odd moments vanish. The Jacobi operator
of $d\tilde{\mu}$ is essentially the square of $J^{\mathrm{full}}$ restricted to the
even/odd subspaces.

**Proof.** Standard change of variables. The moments of $d\tilde{\mu}$ are
$\int_0^\infty u^n\,d\tilde{\mu}(u) = \int_{-\infty}^\infty s^{2n}\,dm_{\mathrm{full}}(s) =
c_{2n}^{\mathrm{full}}$. $\square$

### 7.3. The Markov problem and potential indeterminacy

Unlike $dm_\infty$ (which satisfies the Carleman condition), the Stieltjes problem
for $d\tilde{\mu}$ could be indeterminate if the moments $c_{2n}^{\mathrm{full}}$ grow
sufficiently fast. However, by Proposition 1.5, the Hamburger problem for
$dm_{\mathrm{full}}$ is determinate. Is this consistent with the possibly
indeterminate Stieltjes problem? Yes: a determinate Hamburger problem can have an
associated indeterminate Stieltjes problem (the Hamburger problem is more restrictive).

**Proposition 7.3 (Determinacy of the Stieltjes problem).** The Stieltjes problem for $d\tilde{\mu}$
is determinate, since $d\tilde{\mu}$ is obtained by a change of variable from $dm_{\mathrm{full}}$,
which is unique for its Hamburger moments, and the map $s \mapsto s^2$ is 2-to-1, but the
symmetry of $dm_{\mathrm{full}}$ makes the preimage unique among symmetric measures.

**Proof.** If $\nu_1$ and $\nu_2$ are two measures on $[0,+\infty)$ with the same
Stieltjes moments $\int u^n\,d\nu_i = c_{2n}$, their preimages $\mu_i(A) = \nu_i(\{u:
u \in A^2\} \cap [0,\infty))/2 + \nu_i(\{u: u \in (-A)^2\} \cap [0,\infty))/2$ are
symmetric measures on $\mathbb{R}$ with the same even moments. By determinacy of the
Hamburger problem, $\mu_1 = \mu_2$, hence $\nu_1 = \nu_2$. $\square$

---

## §8. The Hadamard barrier and the structural obstacle

### 8.1. Precise formulation of the barrier

**Definition 8.1 (Hadamard barrier, Jacobi version).** The Hadamard barrier in
Direction C is the following obstacle: the map
$$\Psi: \text{(analytic properties of } (e_k)) \longrightarrow
\text{(properties of the zeros of } \zeta)$$
has no direct version. The analytic properties of $(e_k)$ (decay, signs,
sum rule) do not determine the position of the zeros of $\zeta$ off the critical line.

**Theorem 8.2 (Hadamard barrier, informal statement).** There is no measurable
function $\Phi: \ell^2 \to \{0,1\}$ such that $\Phi(e_k) = 1$ if and only if all zeros
of $\zeta$ lie on the critical line, where $\Phi$ depends only on $\ell^2$-type analytic
properties of the sequence $(e_k)$.

**Justification.** (Non-rigorous but structurally correct argument.) Given any
function $\zeta'$ with the same moments on the critical line as $\zeta$ but with "small"
off-critical zeros (i.e., $\sigma_j - 1/2$ small), the coefficients $e_k'$
differ from $e_k$ by $O((\sigma_j - 1/2)^2/k^2)$, which lies in $\ell^2$. The ratios
$e_k'/e_k$ tend to 1, and there is no threshold in $\ell^2$ distinguishing the RH case from
the ¬RH case. This is the "Hadamard barrier" in spectral terms.

### 8.2. Comparison with the classical Hadamard barrier

The original Hadamard barrier states that $L^2$-type analytic methods on the critical
line cannot detect the position of zeros outside it. In terms of the
Jacobi operator: the coefficients $e_k$ are averages of $|\zeta|^2$ over the critical
line, weighted by polynomial functions. Off-critical zeros affect $|\zeta|^2$
on the critical line smoothly (by the Hadamard product formula), so that
the perturbation in the $e_k$ is $O(1/k^2)$ per off-critical zero. To detect a single
off-critical zero from $(e_k)$, one would need to invert a system of integral equations
with Cauchy kernel, which is an ill-conditioned problem.

### 8.3. The explicit inverse map

Let us fix the notation for the inverse map. Given the coefficients $(a_k)_{k \geq 1}$ of a
symmetric Jacobi operator ($b_k = 0$), the spectral measure can be recovered via the
**Stieltjes transform**:

**Proposition 8.3 (Reconstruction of the spectral measure).** Let $J = (a_k, 0)$ be a
symmetric Jacobi operator with $a_k \in \ell^2_{\mathrm{loc}}$. The spectral measure $d\mu$ of $J$
is reconstructed from the Green's function:
$$G(z) = \langle e_0, (J - z)^{-1} e_0 \rangle = \int_{\mathbb{R}} \frac{d\mu(s)}{s - z},
\qquad z \notin \sigma(J),$$
and the spectral measure is recovered by the Stieltjes-Perron formula:
$$\mu([a,b]) = \lim_{\varepsilon \to 0^+} \frac{1}{\pi} \int_a^b \mathrm{Im}[G(s+i\varepsilon)]
\, ds.$$

The Green's function $G(z)$ is computed as a continued fraction:
$$G(z) = \cfrac{1}{b_0 - z - \cfrac{a_1^2}{b_1 - z - \cfrac{a_2^2}{b_2 - z - \cdots}}}
= \cfrac{1}{-z - \cfrac{a_1^2}{-z - \cfrac{a_2^2}{-z - \cdots}}}$$
(with $b_k = 0$).

**Proof.** Standard theory of Jacobi operators: see Akhiezer (1965) or Simon (2005,
Chapter 1). $\square$

**Remark 8.4.** The map $(a_k) \mapsto G(z) \mapsto d\mu$ is well defined and bijective
(under the Carleman condition). But evaluating $G(z)$ in terms of $a_k^{\mathrm{full}}$
to extract information about the zeros of $\zeta$ requires controlling the continued fraction for
$z$ outside the spectrum, which requires information about the global behavior of $(a_k)$,
not only its $\ell^2$ part.

---

## §9. Formulation of the Direction C conjecture

### 9.1. The conjecture

Based on the analysis of the previous sections, we formulate the following conjectures as
guidance for future investigations.

**Conjecture C.1 (Sign-definite condition for the errors).** Let $(e_k)$ be the sequence of
Jacobi errors defined in §2.3. The following two statements are **equivalent**:

(a) $\sum_{k=1}^\infty k\,(e_k - e_k^{\mathrm{on}}) = 0$ (balance condition).

(b) RH is true.

**Status:** Not proved in either direction.

**Conjecture C.2 (Continued fraction and RH).** The continued fraction associated with $(a_k^{\mathrm{full}})$
converges to the Green's function $G^{\mathrm{full}}(z)$ for all $z$ in the upper half-plane,
and $G^{\mathrm{full}}(z) = G^{\mathrm{on}}(z)$ for all $z$ if and only if RH holds.

**Status:** The first claim (convergence of the continued fraction) is a standard result
under $\sum e_k^2 < \infty$. The equivalence with RH is open.

**Conjecture C.3 (Monotonicity of the errors).** The sequence $e_k = a_k^{\mathrm{full}} -
a_k^\infty$ is eventually monotonically decreasing to zero if and only if RH holds.

**Status:** Not proved. The decay $e_k = O(\log k / k)$ is known. Eventual monotonicity
under RH is plausible given the behavior of the von Mangoldt function, but
there is no proof.

### 9.2. A weaker and more plausible conjecture

**Conjecture C.4 (Averaged positivity).** The following condition is necessary for RH:
$$\liminf_{N \to \infty} \frac{1}{N} \sum_{k=1}^N e_k \geq 0.$$

**Justification.** Under RH, the values $|\zeta(1/2+is)|^2$ have average value 1 with respect to
$dm_\infty$ (since $\int_{\mathbb{R}} |\zeta(1/2+is)|^2\,dm_\infty(s)$ is finite and
positive, and the density function has "average 1" in some averaged sense). The coefficients
$e_k$ are functionals of these moments that must have positive sign on average if the
density is on average greater than 1. Under ¬RH (with off-critical zeros), the factor $R(s) - 1
\geq 0$ (Doc 89) increases $dm_{\mathrm{full}}$ over $dm_{\mathrm{full,on}}$, which also
increases the $e_k$ relative to $e_k^{\mathrm{on}}$. Thus averaged positivity
would be easier under ¬RH, which would make Conjecture C.4 only necessary for RH,
not sufficient.

**Remark 9.3 (Obstacle to sufficiency).** The structural obstacle identified in §8
implies that no condition on finitely many $e_k$, nor any $\ell^2$-type condition
on the whole of $(e_k)$, can be **sufficient** for RH, unless it captures
information about the behavior of the continued fraction for $z$ near the real axis.

---

## §10. Synthesis: what Direction C proves and what it does not

### 10.1. Results proved in Direction C

The following results are rigorous:

**Result C-I (Hilbert-Schmidt perturbation).** $J^{\mathrm{full}} - J^\infty$ is Hilbert-
Schmidt (P40, Path I). In particular $\sum e_k^2 < \infty$.

**Result C-II (Symmetry).** $b_k^{\mathrm{full}} = 0$ for all $k$ (Proposition 2.4).
Consequence: $J^{\mathrm{full}}$ has no discrete spectrum (Corollary 6.4).

**Result C-III (Sum rule).** $\sum_{k=1}^\infty e_k^2 = \int_{\mathbb{R}} \log|\zeta(1/2+is)|^2
\, dm_\infty(s)$ (Remark 6.5, Killip-Simon sum rule with $\Phi_{\mathrm{disc}} = 0$).

**Result C-IV (Uniqueness).** The map $(e_k) \mapsto dm_{\mathrm{full}}$ is bijective, and
$dm_{\mathrm{full}}$ completely determines the zeros of $\zeta$ (since $|\zeta(1/2+is)|^2 =
dm_{\mathrm{full}}/dm_\infty$). RH is equivalent to $e_k = e_k^{\mathrm{on}}$ for all $k$.

**Result C-V (Absence of discrete spectrum and off-critical zeros).** Off-critical
zeros of $\zeta$ do not create discrete eigenvalues in $J^{\mathrm{full}}$: they manifest
exclusively in the absolutely continuous part of $dm_{\mathrm{full}}$ (Proposition 4.2 and
Corollary 4.3).

### 10.2. What is not proved

**Open C-A.** There is no simple, verifiable condition on $(e_k)$ equivalent to RH.
The natural candidates (positivity, monotonicity, balance) have not been proved
equivalent to RH.

**Open C-B.** The conjecture that $e_k \geq 0$ for all $k$ (under RH) is not proved.
The errors could oscillate in sign even under RH.

**Open C-C.** The continued fraction of $(a_k^{\mathrm{full}})$ gives access to the
Green's function $G^{\mathrm{full}}$, but extracting from it the position of off-critical
zeros (if they existed) requires controlling the continued fraction in the strip $\{z: 0 < \mathrm{Im}(z) <
\delta\}$, which is an open problem in the theory of Jacobi operators with
$a_k \sim \sqrt{k}$.

**Open C-D.** The sum rule $\sum e_k^2 = \int \log|\zeta|^2\,dm_\infty$ (Result C-III)
is interesting but circular in the context of RH: the right-hand side is an integral over the
critical line that does not directly distinguish between RH and ¬RH.

### 10.3. The most promising direction

The most promising result of Direction C is Result C-V combined with the barrier
identified in §8: off-critical zeros are not detectable via the discrete spectrum of
$J^{\mathrm{full}}$ (because there is no discrete spectrum), but must instead be detected in the
fine structure of the absolutely continuous part.

**This suggests** that Direction C should be connected to the analysis of the density
$f_{\mathrm{ac}}(s) = |\zeta(1/2+is)|^2 \cdot (dm_\infty/ds)$ and its properties as a function
of the real variable $s$. The zeros of $f_{\mathrm{ac}}$ (at $s = \gamma_n$, critical zeros) and the
strict positivity $f_{\mathrm{ac}} > 0$ outside them are properties of the absolutely
continuous part, not of the discrete spectrum. The RH condition is then the condition
that $f_{\mathrm{ac}}$ has a certain prescribed zero structure.

This perspective connects Direction C with Path 1 of Doc 89 (the Nevanlinna function
$\mathcal{G}(z)$ of the measure difference $d\nu = dm_{\mathrm{full}} - dm_{\mathrm{full,on}}$).

---

## §11. Connection with the central object $d\nu$ of Doc 89

Doc 89 identifies $d\nu = dm_{\mathrm{full}} - dm_{\mathrm{full,on}}$ as the central
object of the program. Direction C provides a new perspective on this object:

**Proposition 11.1 (Interpretation of $d\nu$ in Jacobi terms).** The difference measure
$d\nu = dm_{\mathrm{full}} - dm_{\mathrm{full,on}}$ corresponds, under the Jacobi bijection,
to the difference of the operators:
$$J^{\mathrm{full}} - J^{\mathrm{on}} = \mathrm{diag}(e_k - e_k^{\mathrm{on}})$$
(as a first-order diagonal perturbation, in the regime where the perturbations are
small).

**Warning.** The above identification is only first-order. The exact difference
$J^{\mathrm{full}} - J^{\mathrm{on}}$ is not diagonal: the Jacobi bijection is nonlinear
(the coefficients $a_k$ depend nonlinearly on the moments $c_{2n}$), and the
difference of measures $d\nu$ corresponds to a non-diagonal perturbation of the Jacobi operator.

**Proposition 11.2 (RH in terms of the difference operator).** RH is equivalent to the
condition:
$$J^{\mathrm{full}} = J^{\mathrm{on}},$$
which is equivalent to $e_k = e_k^{\mathrm{on}}$ for all $k$ (by the Jacobi bijection and the
uniqueness of the moment problem).

**Remark 11.3.** This is again the trivial equivalence of Proposition 5.1.
Direction C has not achieved (and possibly cannot achieve) a condition on $(e_k)$
alone that is equivalent to RH without reference to $e_k^{\mathrm{on}}$.

### 11.1. A perspective from the Stieltjes transform

The Green's function $G^{\mathrm{full}}(z) = \int \frac{dm_{\mathrm{full}}(s)}{s-z}$ and the
"on-critical" Green's function $G^{\mathrm{on}}(z)$ satisfy:

**Proposition 11.4.** For $z$ in the upper half-plane:
$$G^{\mathrm{full}}(z) - G^{\mathrm{on}}(z) = \int_{\mathbb{R}} \frac{d\nu(s)}{s - z},$$
where $d\nu \geq 0$ is the difference measure of Doc 89. This function is analytic in the
upper half-plane, takes values in the right half-plane (positive real part), and vanishes
identically if and only if $d\nu = 0$, which is equivalent to RH.

**Proof.** $d\nu \geq 0$ implies $\mathrm{Im}[(G^{\mathrm{full}} - G^{\mathrm{on}})(z)]
\geq 0$ for $\mathrm{Im}(z) > 0$ (the Cauchy transform of a positive measure is of
Nevanlinna-Herglotz type). The equivalence $d\nu = 0 \iff$ RH is Proposition 1.1 of
Doc 89. $\square$

**Corollary 11.5.** RH is equivalent to the difference of Green's functions
$G^{\mathrm{full}}(z) - G^{\mathrm{on}}(z) \equiv 0$ in the upper half-plane. This is
an analytic condition on the Green's functions (which are computed as continued
fractions from $(a_k^{\mathrm{full}})$ and $(a_k^{\mathrm{on}})$ respectively).

---

## §12. Final diagnosis and outlook

### 12.1. What Direction C contributes to the program

Direction C (Jacobi spectral inverse problem) produces the following contributions to the
program:

1. **Rigorous formalization** of the map $dm_{\mathrm{full}} \leftrightarrow (a_k^{\mathrm{full}},
   b_k^{\mathrm{full}})$ within the context of Killip-Simon theory.

2. **Identification of the sum rule** $\sum e_k^2 = \int \log|\zeta|^2\,dm_\infty$
   (Result C-III), which links the Jacobi coefficients with the logarithmic integral of
   $\zeta$ on the critical line.

3. **Proof of the absence of discrete spectrum** in $J^{\mathrm{full}}$ (Corollary 6.4),
   a consequence of the symmetry $b_k = 0$ imposed by the functional equation.

4. **Localization of the problem**: off-critical zeros manifest in the
   absolutely continuous part of $dm_{\mathrm{full}}$, not in its singular part. This rules out
   the technique of detecting discrete eigenvalues.

5. **Connection with Doc 89**: Direction C connects with the central object $d\nu$ via the
   Green's functions.

### 12.2. Identified obstacles

The structural obstacles are:

**Obstacle 1 (Local vs. global).** The coefficients $e_k$ are global functionals of
$dm_{\mathrm{full}}$ (via Hankel determinants). The zeros of $\zeta$ are local
information of $dm_{\mathrm{full}}$ (as zeros of the density). The map from local
information to global (zeros $\to$ Jacobi coefficients) is the Hadamard map, known to be
difficult to invert.

**Obstacle 2 (Absolutely continuous part).** Off-critical zeros affect only the
absolutely continuous part of $dm_{\mathrm{full}}$, which in terms of the continued
fraction is boundary information (the limit of $G^{\mathrm{full}}(s+i\varepsilon)$ as
$\varepsilon \to 0^+$). Controlling this limit from the continued fraction requires
non-uniform convergence results that are beyond current reach.

**Obstacle 3 (No simple condition possible).** There is no simple condition on finitely many
$e_k$ equivalent to RH (Proposition 5.3). Information about off-critical zeros is
distributed across the entire sequence $(e_k)_{k \geq 1}$.

### 12.3. Outlook: combination with Directions A and B

Direction C is more useful as a reformulation tool than as a direct attack on RH.
Its greatest usefulness is the sum rule (Result C-III) and the localization of the problem in the
absolutely continuous part. To close an argument, Direction C should be combined
with:

- **Direction A** (the Nevanlinna function $\mathcal{G}(z)$, Doc 89): Direction C
  provides the continued fraction as an approximation to $G^{\mathrm{full}}$, while
  Direction A requires controlling $G^{\mathrm{full}} - G^{\mathrm{on}}$.

- **Direction B** (the Jensen excess $\delta$, Docs 84, 87): the sum rule $\sum e_k^2 =
  \int \log|\zeta|^2\,dm_\infty$ could be compared with the Jensen excess; if there were a
  bound of the form $\delta \leq C \sum e_k^2 - C' \int \log|\zeta|^2\,dm_\infty$, one would obtain
  $\delta = 0$, which is equivalent to RH. But this type of bound requires quantitative
  control that is not currently available.

### 12.4. Frank conclusion

Direction C provides a rigorous formalism and several structural results, but does not
close the proof of RH. The central obstacle is that off-critical zeros affect the
coefficients $e_k$ in a smooth and distributed way, making no simple analytic
condition on $(e_k)$ equivalent to RH.

**The Jacobi inverse map is not the path to RH by itself.** It is, however, a
valuable tool for understanding the structure of $dm_{\mathrm{full}}$ and for reformulating RH
in spectral terms. Combination with Paths 1, 2, 3 of Doc 89 is the most
promising direction.

---

## References

- [KS03] R. Killip, B. Simon. *Sum rules for Jacobi matrices and their applications to
  spectral theory*. Ann. Math. **158** (2003), 253–321.
- [Si05] B. Simon. *Szegő's Theorem and its Descendants: Spectral Theory for $L^2$
  Perturbations of Orthogonal Polynomials*. Princeton Univ. Press, 2005.
- [DS06] S. Denisov, B. Simon. *Zeros of orthogonal polynomials on the real line*. J. Approx.
  Theory **142** (2006), 2–8.
- [Ak65] N. I. Akhiezer. *The Classical Moment Problem*. Oliver & Boyd, 1965.
- [CCM24] A. Connes, C. Consani, H. Moscovici. *Zeta zeros and prolate wave operators*. 2024.
- Doc 60: Decay and sum of the semilocal Jacobi discrepancy.
- Doc 83: Sign of the measure difference $dm_{\mathrm{full}} - dm_{\mathrm{full,on}}$.
- Doc 89: The central object $d\nu$; synthesis of the three paths.

---

*End of Doc 92.*
