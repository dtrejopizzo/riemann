# D.142 — No contractive monoidal Fock descent with the arithmetic normalization

## Verdict

A free Fock lift preserves every prime label and supplies a canonical
positive Hilbert space with orthogonal creation ranges.  It therefore looks
like a possible source for the contraction \(C_T\) of D.137.  The descent
to the commutative arithmetic correspondence semigroup is, however,
unbounded.

Let \(\mathcal F_{\rm free}\) have orthonormal basis \(e_w\) indexed by
finite words in the prime alphabet, and let \(\ell^2(\mathbb N^\times)\)
have basis \(\varepsilon_n\).  Any monoidal map retaining each prime
correspondence must satisfy

\[
 Qe_{p_1\cdots p_r}=\varepsilon_{p_1\cdots p_r}.       \tag{0.1}
\]

For \(r\) distinct primes, all \(r!\) permutations are orthogonal in the
free Fock space and have the same image.  Hence

\[
 \left\|Q{1\over\sqrt{r!}}\sum_{\sigma\in S_r}
 e_{p_{\sigma(1)}\cdots p_{\sigma(r)}}\right\|
 =\sqrt{r!}.                                          \tag{0.2}
\]

Thus \(Q\) is unbounded.  Renormalizing words by a length factor does not
help: monoidality forces \(c_{r+s}=c_rc_s\), and preservation of the prime
generators forces \(c_1=1\), hence \(c_r=1\).

The normalized symmetric Fock quotient reverses the problem.  It is
contractive as a Hilbert quotient, but its multiplication carries the
factor

\[
 \sqrt{{(r+s)!\over r!\,s!}},                          \tag{0.3}
\]

so it no longer realizes
\(\Gamma_m\Gamma_n=\Gamma_{mn}\) isometrically or contractively with the
fixed A--B metric normalization.

Therefore neither free nor symmetric Fock positivity produces the required
adelic contraction while retaining composition, every \(p^k\), and the
central weights.  The Gamma channel cannot remove the factorial defect,
which is already present in the finite correspondence algebra before the
archimedean completion.

No zero or sign of \(B_{\rm nuc}\) is used.  The paper is not modified.

## 1. The free positive lift

Let \(\mathcal A\) be an alphabet containing one letter for each prime.
The full Fock space is

\[
 \mathcal F_{\rm free}
 =\ell^2(\mathcal A^*)
 =\mathbb C\Omega\oplus
   \bigoplus_{r\ge1}\ell^2(\mathcal A)^{\otimes r}.    \tag{1.1}
\]

Left creation by \(p\),

\[
 L_pe_w=e_{pw},                                       \tag{1.2}
\]

is an isometry and the ranges of \(L_p,L_q\) are orthogonal for \(p\ne q\).
Consequently row operators formed from finitely many normalized \(L_p\)
are contractions.  This is genuine source-side positivity.

The arithmetic correspondence semigroup is commutative:

\[
 \Gamma_p\Gamma_q=\Gamma_{pq}=\Gamma_q\Gamma_p.       \tag{1.3}
\]

Its regular Hilbert basis has one vector \(\varepsilon_n\) for each
integer.  A descent compatible with (1.2)--(1.3) and the unit must obey

\[
 Q\Omega=\varepsilon_1,\qquad
 QL_{p_1}\cdots L_{p_r}\Omega
 =\varepsilon_{p_1\cdots p_r}.                        \tag{1.4}
\]

This is exactly (0.1).

## 2. Factorial amplification

Choose distinct primes \(p_1,\ldots,p_r\).  The vectors

\[
 e_\sigma=e_{p_{\sigma(1)}\cdots p_{\sigma(r)}},
 \qquad\sigma\in S_r,                                 \tag{2.1}
\]

are orthonormal.  Therefore

\[
 v_r={1\over\sqrt{r!}}\sum_{\sigma\in S_r}e_\sigma,
 \qquad\|v_r\|=1.                                     \tag{2.2}
\]

Every word in (2.1) has the same arithmetic product
\(n_r=p_1\cdots p_r\), so (1.4) gives

\[
 Qv_r=\sqrt{r!}\,\varepsilon_{n_r}.                   \tag{2.3}
\]

It follows that

\[
 \|Q\|\ge\sqrt{r!}\quad\text{for every }r.            \tag{2.4}
\]

Hence no bounded, and a fortiori no contractive, monoidal descent exists.
The argument only uses squarefree products; prime-power conventions cannot
repair it.

## 3. Length renormalization is incompatible with row B

Suppose more generally that

\[
 Qe_w=c_{|w|}\varepsilon_{\pi(w)},                    \tag{3.1}
\]

where \(\pi(w)\) is the integer product of the letters.  Compatibility with
concatenation and arithmetic multiplication requires

\[
 c_{r+s}=c_rc_s,\qquad c_0=1.                         \tag{3.2}
\]

Thus \(c_r=c_1^r\).  Row B fixes the generator:
\(Qe_p=\varepsilon_p\), so \(c_1=1\) and \(c_r=1\).  Equation (2.4)
returns unchanged.

Choosing \(|c_1|<1\) could suppress the factorial growth only
exponentially, which is still insufficient because
\(\sqrt{r!}|c_1|^r\to\infty\).  More importantly, it would replace the
metric label \(p^{-1/2}\) by \(|c_1|p^{-1/2}\) at every prime and destroy
the exact contact comparison with B and C.

No scalar multiplicative renormalization solves the problem.

## 4. The symmetric Fock alternative

Let

\[
 s_{p_1,\ldots,p_r}
 ={1\over\sqrt{r!}}\sum_{\sigma\in S_r}e_\sigma       \tag{4.1}
\]

for distinct labels.  These normalized symmetrizations form the natural
bosonic basis.  Identifying \(s_{p_1,\ldots,p_r}\) with
\(\varepsilon_{p_1\cdots p_r}\) is isometric.

But normalized symmetric tensor multiplication satisfies

\[
 s_r\odot s_s
 =\sqrt{{(r+s)!\over r!\,s!}}\,s_{r+s}                \tag{4.2}
\]

when the labels are disjoint.  The coefficient in (4.2) is larger than one
and unbounded.  Thus the multiplication is not the arithmetic law with
unit structure constants:

\[
 \varepsilon_m\varepsilon_n=\varepsilon_{mn}.         \tag{4.3}
\]

Using unnormalized symmetric tensors restores (4.3) but restores the
factorial Hilbert norms and the unbounded quotient of Section 2.

## 5. Why Gamma cannot absorb the defect

The contradiction occurs in the finite span of the \(r!\) words attached
to finitely many distinct primes.  The Gamma/Poisson object is a common
archimedean summand and does not distinguish those permutations.

Any orthogonal direct sum with a Gamma Hilbert space leaves (2.3)
unchanged.  A nonorthogonal correction cancelling it would have to identify
the permutation directions before descent; that is precisely the
symmetric quotient, with multiplication anomaly (4.2).  Assigning Gamma
norms depending on the word length would introduce the arithmetic function
\(\Omega(n)\), which is absent from the exact row-C character and would
alter all mixed correspondences.

Therefore the archimedean term cannot be used as a factorial counterterm
without changing the already proved A--B--C comparison.

## 6. Consequence for the positive-feature route

The Fock construction separates two requirements which cannot be met
simultaneously by this lift:

\[
\begin{array}{c|c|c}
 &\text{Hilbert descent}&\text{monoidal arithmetic law}\\ \hline
\text{free Fock}&\text{unbounded by }\sqrt{r!}&\text{yes before quotient}\\
\text{symmetric normalized Fock}&\text{isometric}&
 \text{factor }\sqrt{(r+s)!/(r!s!)}\\
\text{symmetric unnormalized Fock}&\text{factorial norms}&\text{yes}
\end{array}
\]

Thus a completely positive free dilation cannot be the independent source
of \(C_TX_T=Y_T\).  The live construction must use the commutative
periodic--Witt category from the outset and obtain its positivity from a
non-product adelic mechanism, not by symmetrizing an orthogonal free lift.
