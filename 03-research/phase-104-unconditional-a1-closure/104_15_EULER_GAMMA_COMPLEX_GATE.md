# 104_15 — Euler–Gamma complex: Koszul gate on the minimal posets

## Verdict

The minimal graded construction does exist as a positive Hilbert complex. On the
divisor cube it is the Koszul complex

\[
 d_E=\sum_r N_r\otimes\varepsilon_r,
 \qquad d_E^2=0,
\tag{1}
\]

where \(N_r\) removes the prime factor \(r\) and \(\varepsilon_r\) is
exterior multiplication. On \(\{1,p,q,pq\}\), its Hodge Laplacian exactly cancels
the mixed channels \(p/q\) and \(q/p\). The cancellation uses an ordinary positive
metric, not a supertrace or a Krein form.

But the same differential makes the Möbius–divisor cross term vanish in
cohomology:

\[
 M\delta Z=(\log p)N_p+(\log q)N_q,
 \qquad
 N_r=d_E\iota_r+\iota_r d_E.
\tag{2}
\]

Hence \(M\delta Z\) is homotopically null. Already on the poset
\(\{1,p\}\), the hermitized channel one wants to declare a boundary is exactly the
same channel that must survive as a prime current. So the natural Koszul complex
satisfies the ratio cancellation but fails property 1 of 104_12 §8 before property
3's Gamma budget can even appear.

The scope is precise: this is a **no-go for the divisor Koszul complex
and, more generally, for every complex in which each ratio generator
\(N_p\) is null-homotopic**. It does not prove that every imaginable arithmetic
cohomology is impossible. In particular, it does not rule out a nonlocal
differential that kills only quadratic combinations of ratios without making the
\(N_p\) exact; such an object would still have to construct, not postulate, the
exact Gamma term.

The model is the **squarefree/Boolean** cube. It does not by itself represent the
towers \(p^k\). Hence the theorem rules out exactly this natural Koszul complex and
its \(N_p\)-exact variants, not some different graded resolution that incorporates
the prime powers as additional data.

Neither A1 nor RH is proved.

## 1. Boolean divisor algebra

Let \(P=\{p_1,\dots,p_r\}\) be a finite set of primes and let

\[
 {\cal D}_P=\left\{\prod_{p\in S}p:S\subseteq P\right\}.
\tag{3}
\]

On \(V_P=\ell^2({\cal D}_P)\), with its canonical orthonormal basis, we define

\[
 N_p e_n=
 \begin{cases}
 e_{n/p},&p\mid n,\\
 0,&p\nmid n.
 \end{cases}
\tag{4}
\]

Then

\[
 N_p^2=0,
 \qquad N_pN_q=N_qN_p,
 \qquad N_p^*N_q=N_qN_p^*\quad(p\ne q).
\tag{5}
\]

The poset's zeta matrix and its Möbius inverse factor as

\[
 Z_P=\prod_{p\in P}(I+N_p),
 \qquad
 M_P=Z_P^{-1}=\prod_{p\in P}(I-N_p).
\tag{6}
\]

Let \(\delta\) be the derivation determined by
\(\delta N_p=(\log p)N_p\). Applying Leibniz to (6), and using
\((I-N_p)(I+N_p)=I\), one obtains the exact identity

\[
 \boxed{
 M_P\delta Z_P=\sum_{p\in P}(\log p)N_p.}
\tag{7}
\]

This is the finite-divisor version of \(Z^{-1}\delta Z=V_\Lambda\). No zero
localization or inequality has been used.

## 2. The minimal poset \(\{1,p\}\)

In the basis \((e_1,e_p)\), writing \(\ell_p=\log p\),

\[
 N_p=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
 Z=I+N_p=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
 M=I-N_p.
\tag{8}
\]

Hence

\[
 Z^*Z=
 \begin{pmatrix}1&1\\1&2\end{pmatrix}
 =I+(N_p+N_p^*)+N_p^*N_p,
 \qquad
 M\delta Z=\ell_pN_p.
\tag{9}
\]

The off-diagonal ratio channel in \(Z^*Z\) is \(N_p+N_p^*\). The hermitized
physical cross term is

\[
 M\delta Z+(M\delta Z)^*=\ell_p(N_p+N_p^*).
\tag{10}
\]

This gives the minimal falsifier.

**Proposition 1 (channel–current collision).** Let \((C^\bullet,d)\) be a
complex and suppose that the hermitized channel \(N_p+N_p^*\) induces the
zero operator on its physical quotient. Then the hermitized cross term (10)
also induces the zero operator. In particular, that quotient cannot
simultaneously satisfy properties 1 and 2 of 104_12 §8.

**Proof.** The second operator is the first multiplied by the positive
scalar \(\ell_p\). \(\square\)

A holomorphic version, which is what the Koszul complex will use, is even
stronger: if \(N_p=dh+hd\), then \(N_p\) induces zero in cohomology,
and so does \(\ell_pN_p\).

The proposition does not say that the channel \(p/1\) must be killed. It says that
**if** the rule of 104_12 §8 is implemented by declaring every channel of
\(Z^*Z\) exact, the very first channel already destroys the current one wanted to
preserve.

## 3. The square \(\{1,p,q,pq\}\)

In the basis \((e_1,e_p,e_q,e_{pq})\),

\[
 N_p=
 \begin{pmatrix}
 0&1&0&0\\
 0&0&0&0\\
 0&0&0&1\\
 0&0&0&0
 \end{pmatrix},
 \qquad
 N_q=
 \begin{pmatrix}
 0&0&1&0\\
 0&0&0&1\\
 0&0&0&0\\
 0&0&0&0
 \end{pmatrix}.
\tag{11}
\]

Thus,

\[
 Z=(I+N_p)(I+N_q)=
 \begin{pmatrix}
 1&1&1&1\\
 0&1&0&1\\
 0&0&1&1\\
 0&0&0&1
 \end{pmatrix},
\tag{12}
\]

and (7) reduces to

\[
 \boxed{M\delta Z=\ell_pN_p+\ell_qN_q.}
\tag{13}
\]

Let \(E=\mathbb C e_p\oplus\mathbb C e_q\), with the standard positive
metric, and let

\[
 K^k=V_P\otimes\Lambda^kE,
 \qquad
 d_E=N_p\otimes\varepsilon_p+N_q\otimes\varepsilon_q.
\tag{14}
\]

Since the \(N\)'s commute and the exterior multiplications anticommute,

\[
 d_E^2=N_pN_q\otimes
 (\varepsilon_p\varepsilon_q+\varepsilon_q\varepsilon_p)=0.
\tag{15}
\]

No sign was introduced in the metric: each \(K^k\) is an ordinary Hilbert
space.

### 3.1. The mixed ratios do cancel

Denote by \(\iota_p,\iota_q\) the contractions, adjoint to
\(\varepsilon_p,\varepsilon_q\). In the Laplacian

\[
 \Delta_E=d_E^*d_E+d_Ed_E^*,
\tag{16}
\]

the coefficient of \(\iota_p\varepsilon_q\) is

\[
 N_p^*N_q-N_qN_p^*=0,
\tag{17}
\]

and the conjugate coefficient is

\[
 N_q^*N_p-N_pN_q^*=0.
\tag{18}
\]

These equalities are exactly the double commutation of (5). Hence the
channels \(p/q\) and \(q/p\), which would appear in a non-graded square, cancel
between the two adjacent degrees. This is an explicit, positive realization of
the cancellation part required by property 2.

### 3.2. The current becomes a boundary

The canonical exterior relations give

\[
 \varepsilon_j\iota_i+\iota_i\varepsilon_j=\delta_{ij}I.
\tag{19}
\]

Consequently,

\[
 \boxed{d_E\iota_p+\iota_p d_E=N_p,\qquad
 d_E\iota_q+\iota_q d_E=N_q.}
\tag{20}
\]

Multiplying by \(\ell_p,\ell_q\) and summing,

\[
 M\delta Z=d_EH+Hd_E,
 \qquad
 H=\ell_p\iota_p+\ell_q\iota_q.
\tag{21}
\]

Hence \(M\delta Z\) induces the zero operator on
\(H^\bullet(K,d_E)\). The complex that correctly cancels the ratio comb does
not leave the Möbius–divisor cross term in cohomology: it turns it into a
boundary together with the comb.

## 4. General theorem and scope

**Theorem 2 (divisor Koszul stop-gate).** For every finite set of
primes \(P\), the positive complex

\[
 K_P^\bullet=V_P\otimes\Lambda^\bullet\mathbb C^P,
 \qquad
 d_E=\sum_{p\in P}N_p\otimes\varepsilon_p
\tag{22}
\]

satisfies:

1. \(d_E^2=0\);
2. the mixed correlations \(N_p^*N_q\), \(p\ne q\), cancel in the Hodge
   Laplacian;
3. the Möbius–divisor connection is null-homotopic:

\[
 M_P\delta Z_P
 =d_E\left(\sum_{p\in P}\log p\,\iota_p\right)
 +\left(\sum_{p\in P}\log p\,\iota_p\right)d_E.
\tag{23}
\]

In particular, this complex cannot simultaneously satisfy properties 1–3 of
104_12 §8: realizing property 2 destroys property 1, regardless of what
Gamma operator is later added on the cohomology.

**Proof.** The first claim uses commutation of the \(N_p\) and exterior
anticommutation. The second is (17)–(18) for each pair. The third follows from
\(d_E\iota_p+\iota_pd_E=N_p\) and from (7). \(\square\)

The same conclusion holds for any complex \((C,d)\) in which there exist
homotopies \(h_p\) with

\[
 N_p=dh_p+h_pd.
\tag{24}
\]

Indeed, \(M\delta Z=dh+hd\), with
\(h=\sum_p(\log p)h_p\). This extension is formal and does not depend on
the choice of metric.

What the theorem does **not** prove must be equally explicit. One could try a
nonlocal differential built from combinations such as
\(N_p^*N_q\), so that the mixed ratios were exact without each
\(N_p\) being so. The argument above does not rule this out. But such a
construction is no longer the Koszul complex of the Möbius inversion and would
still have to:

* produce (7), not merely formally preserve it;
* cancel all repeated channels in larger truncations;
* identify its positive diagonal with the exact archimedean budget
  \(\Delta A_n/2\), without using AHM, A1, or Li positivity.

None of those three tasks is obtained from (22).

## 5. Decision

Proved:

* the minimal positive graded complex of the divisor cube;
* \(d_E^2=0\) on \(\{1,p\}\), \(\{1,p,q,pq\}\), and every Boolean cube;
* exact cancellation of the mixed channels \(p/q\) in the Laplacian;
* exact null-homotopy of \(M\delta Z\).

Ruled out:

* the divisor Koszul complex as the Euler–Gamma complex of 104_12 §8;
* any variant that declares the generators \(N_p\) null-homotopic.

Not ruled out:

* a nonlocal complex that kills only quadratic correlations and not the
  \(N_p\);
* a construction independent of its exact Gamma diagonal.

Not proved: a new bound for the \(\Lambda\) weights, A1, or RH.
</content>
