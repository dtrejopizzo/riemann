# R182.201 — Audit of the rectangular tunnel and the nonlocal joint gate

## 0. Result

The audit separates three statements.

1. The positive Gram corner annihilating its cross block on the radical is
   `PROVED`, but it already appears as the bordered null anchor in R170_862.
2. The conservative rectangular coligation of the prime channels was
   already built in D.244--D.247.
3. A local orthogonal realization on the fibers \(dm=k\) cannot be glued
   to Paper 47's primitive space. The remaining coherent channel has infinite
   rank, while Tate removes only two modes. This is `PROVED` below.

The piece still alive is a **nonlocal** common factor of the joint
Chebyshev--Gamma column after support and Tate compression, built before
any pseudo-inverse. Its existence is not proved.

## 1. The rank theorem that kills the local version

Let \(I_T=(-T,T)\), \(J_T:L^2(I_T)\to L^2(\mathbb R)\) the extension by zero,
\(\mathcal F\) the Fourier transform, and \(\Pi_T\) the projection onto the
space defined by the two Tate equations. Then

\[
 \mathcal P_T=\operatorname{Ran}\Pi_T
\]

has codimension two and infinitely many dimensions.

For a nonempty finite set of primes \(S\), let \(m_S(\tau)\) be the
multiplier of the coherent channel obtained by summing the local
coordinates with the oriented weights \(\sqrt{\log p}\). In the natural
Euler realization, \(m_S\ne0\) almost everywhere. Define

\[
 C_{S,T}=M_{m_S}\mathcal FJ_T\Pi_T.                       \tag{1.1}
\]

### Theorem 1. `PROVED`

If \(m_S\ne0\) almost everywhere, then

\[
 \boxed{\operatorname{rank}C_{S,T}=\infty.}              \tag{1.2}
\]

In particular, the two Tate equations do not turn the coherent channel into
a null coordinate, and no law applying prime-local primitivization
fiber by fiber can produce the second null vector required by the tunnel.

**Proof.** \(J_T\) and \(\mathcal F\) are injective. Multiplication by
\(m_S\), nonzero almost everywhere, is also injective. Its composition is
injective on the infinite-dimensional space \(\mathcal P_T\), hence it has
infinite rank. `QED`

This argument reproduces and applies D.258--D.259 to R182's specific ansatz.

### Corollary 1.1. `PROVED`

Suppose a local construction requires

\[
 \sum_{p\in S}\sqrt{\log p}\,z_p(F,\tau)=0
 \quad\text{for almost every }\tau                         \tag{1.3}
\]

for every \(F\in\mathcal P_T\). If the left-hand side is
\(m_S(\tau)\widehat{J_TF}(\tau)\), then (1.3) forces \(F=0\).

Hence the local condition does not describe Paper 47's primitive space;
it collapses it. The identity \(\Lambda*1=\log\) fixes the sum of coefficients
on each arithmetic fiber, but it does not turn two global moments into
the pointwise condition (1.3).

## 2. Second audit: Schur and Douglas

Let

\[
 \mathbb M=\begin{pmatrix}H&R^*\\R&C\end{pmatrix}.
\]

The statement \(\mathbb M\succeq0\) implies
\(\ker H\subseteq\ker R\). Conversely, in finite dimension such a block can
be completed once that inclusion is known. Hence:

* an abstract completion of the corner is equivalent to the sought
  vanishing;
* a completion with a fixed physical Schur complement is the pure
  congruence classified in R170_861;
* an admissible construction must deliver the factor from the source,
  before knowing the radical and before applying \(D_N^\dagger\).

This confirms R182's circularity test and corrects its claim of novelty.

## 3. The exact column that must be factored

With the notation of D.260--D.262, set

\[
 A(x)=\Psi(x)-x+1,
\]

and let \(q_{N,\infty}\) be the full Gamma column, with the constant, the
pole, and the two Tate jets included. The nonlocal column is

\[
 \boxed{
 \mathfrak q_N
 =q_{N,\infty}
  -\int_{[1,N]}\mathcal K_N(x)\,dA(x).
 }                                                        \tag{3.1}
\]

The subtraction in (3.1) must stay within the same operator. The Gamma
multiplier changes sign; hence neither its part nor the centered measure
admits the separate positive budget required to pay for the other.

For \(\varepsilon>0\), the exact target is

\[
 \boxed{
 \mathcal M_N-
 \mathfrak q_N^*(D_N+\varepsilon I)^{-1}\mathfrak q_N
 =\mathscr Z_{N,\varepsilon}^*\mathscr Z_{N,\varepsilon}.
 }                                                        \tag{NGF}
\]

The admissibility condition is that \(\mathscr Z_{N,\varepsilon}\) be
defined directly via Poisson on \(\mathbb Z\), the factorization
of the atoms of \(d\Psi\), and the paired Gamma measure. Defining it as the
square root of the left-hand side, or via
\(D_N^{\dagger/2}\mathfrak q_N\), is circular.

If `NGF` is proved uniformly in \(N,T,\varepsilon\), the monotone limit
\(\varepsilon\downarrow0\) gives the range condition and the Douglas
inequality with constant one. The chain D.170--D.190 and Paper 47 turn that into
the vanishing at first contact.

## 4. External priority audit

A search by expression and by structure found related prior work, but
not the `NGF` factor:

* Connes--Consani, *The Scaling Hamiltonian*, arXiv:1910.14368, propose a
  semilocal operator framework and conjecture that the semilocal
  framework suffices for Weil on windows. It does not build the joint
  factorization (NGF).
* Works on the Weil/Suzuki quadratic-form operator realize or discretize the
  positivity criterion. The numerical article arXiv:2607.24830 explicitly
  states that it does not prove RH and that its results are
  realizations of classical identities.
* General block-completion and Douglas theorems explain the abstract
  equivalence between positivity and factorization. They do not provide
  an arithmetic factor prior to the spectrum.

It is not possible to exhaustively certify that no one has written an
equivalent idea under different notation. The search carried out found no
construction of `NGF`; the priority that can be claimed is internal: the
rectangular lemma and the local coligation were already in the corpus, while
the nonlocal joint factor remains open there.

## 5. Status

```text
null Gram corner                                       PROVED / CITED R170_862
prime-local rectangular coligation                      PROVED / CITED D.244--247
null anchor via pointwise primitivization                REFUTED
remaining coherent channel has infinite rank              PROVED
two Tate conditions close that channel                     REFUTED
separating positive Euler and Gamma budgets                REFUTED / D.262
joint Chebyshev--Gamma column (3.1)                         PROVED / CITED
nonlocal source factor (NGF)                                OPEN
row D                                                        OPEN
```
