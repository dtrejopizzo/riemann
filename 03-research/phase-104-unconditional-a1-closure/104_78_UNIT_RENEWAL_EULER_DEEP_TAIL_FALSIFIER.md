# 104_78 — Unitary Euler falsifier for the deep tail

**Result.** The exact renewal

\[
 \sum_{D\mid N}\Lambda(D)=\log |N|,
 \tag{1}
\]

the constancy \(\Lambda(P^k)=\log |P|\) over each tower, the positivity of
the weights, an Euler product with non-negative integer prime
multiplicities, a functional equation \(s\leftrightarrow1-s\) and a
**degree** prime law with exponential relative error **do not suffice**,
not even jointly, to prove the deep gate of `104_75`.

A free, fully explicit arithmetic monoid is constructed whose zeta is

\[
 \boxed{
 Z(T)={(1-3T)(1-2T)\over(1-T)(1-6T)},\qquad T=6^{-s}.}
 \tag{2}
\]

Its Euler product has a non-negative integer number of primes at each
degree, all its towers have unit multiplicity and

\[
 Z(1/(6T))=Z(T).                                          \tag{3}
\]

Moreover, if \(\Psi_k\) is the von Mangoldt mass at degree \(k\)
normalized by \(\log6\), then

\[
 \boxed{\Psi_k=6^k+1-3^k-2^k,}                           \tag{4}
\]

so that, coefficient by coefficient in the degree variable, the relative
error is \(O(2^{-k})\). This is the lattice version of the PNT proper to
the model; it is not the ordinary PNT \(\psi(x)\sim x\) in a continuous
norm variable (see §5).

Nevertheless, the zeros

\[
 \beta_+=\log_6 3>{1\over2},\qquad
 \beta_-=\log_6 2=1-\beta_+                              \tag{5}
\]

lie off the central line. The regulated prime--Laguerre form, with pole,
complementary block, primes and prime powers kept to the end, satisfies

\[
 {1\over H_X}\sum_{n\le X}{1\over n}
 \mathbf 1_{\{Q_{n,\varepsilon_X}\ge
 A_n+P_{n,\varepsilon_X}+\log(n+1)+e^{\sqrt X}\}}
 \longrightarrow {1\over4},
 \qquad \varepsilon_X=e^{-X/100}.                        \tag{6}
\]

Thus (6) is a stronger falsifier than the abstract quartet of
`104_75`/`104_77`: it has a positive Euler product, exact renewal and
unitary towers. It is not, however, a counterexample for the ordinary
weights \(\Lambda(m)\): its primes are formal graded primes, with norms
\(6^d\) and multiplicities. The precise verdict is that any proof of the
deep tail for the real zeta must use a property that distinguishes the
placement of the ordinary primes from this system; it cannot be deduced
solely from (1), from the towers, from the degree prime law, from the
functional equation and from positivity.

This document does not prove the limit of `104_75`, A1 or RH.

---

## 1. Formal primes and integer multiplicities

Let

\[
 M_d(r)={1\over d}\sum_{e\mid d}\mu(e)r^{d/e}            \tag{7}
\]

be the number of aperiodic necklaces of length \(d\) over an alphabet of
\(r\) letters. Define

\[
 \boxed{\pi_d=M_d(6)+M_d(1)-M_d(3)-M_d(2).}              \tag{8}
\]

Each \(\pi_d\) is an integer. It is also non-negative: take, within an
alphabet of six letters, two disjoint subalphabets of sizes three and
two. The aperiodic necklaces that use only the first, and those that use
only the second, are disjoint subsets of the necklaces over six letters.
Hence \(M_d(6)\ge M_d(3)+M_d(2)\), and adding \(M_d(1)\ge0\) proves the
claim.

Build the free abelian monoid with \(\pi_d\) prime generators of degree
\(d\), and assign each generator the norm \(6^d\). The classical necklace
identity

\[
 \prod_{d\ge1}(1-T^d)^{-M_d(r)}={1\over1-rT}             \tag{9}
\]

gives, as an identity of formal series,

\[
 \prod_{d\ge1}(1-T^d)^{-\pi_d}
 ={(1-3T)(1-2T)\over(1-T)(1-6T)}=Z(T).                   \tag{10}
\]

There are no fractional weights or truncated towers in (10). If \(P\) is
one of these primes, define

\[
 \Lambda_{\mathcal P}(P^j)=\deg(P)\log6,
 \qquad \Lambda_{\mathcal P}(N)=0
 \quad\hbox{if \(N\) is not a prime power}.       \tag{11}
\]

For \(N=\prod_P P^{a_P}\),

\[
 \sum_{D\mid N}\Lambda_{\mathcal P}(D)
 =\sum_P a_P\deg(P)\log6=\log|N|,                       \tag{12}
\]

which is the exact unitary renewal, element by element.

Taking the logarithmic derivative in (10),

\[
 \sum_{d\mid k}d\pi_d=6^k+1-3^k-2^k.                  \tag{13}
\]

The unnormalized Mangoldt mass at degree \(k\) is \(\log6\) times the
left-hand side. Hereafter we absorb \(\log6\) into the kernel and call
\(\Psi_k\) the integer in (13). Equation (4) and the strong **degree**
prime law are thereby proved. It will not be identified below with the
continuous PNT for ordinary integers.

---

## 2. Functional equation and the outer zero

A direct substitution proves (3):

\[
 \begin{aligned}
 (1-3/(6T))(1-2/(6T))
   &={(1-3T)(1-2T)\over6T^2},\\
 (1-1/(6T))(1-1/T)
   &={(1-T)(1-6T)\over6T^2}.
 \end{aligned}                                          \tag{14}
\]

Removing the two poles, the completed function may be taken as

\[
 \Xi(s)=6^s(1-3\,6^{-s})(1-2\,6^{-s}).                  \tag{15}
\]

From (14), \(\Xi(1-s)=\Xi(s)\). Its zeros are

\[
 \beta_\pm+{2\pi i k\over\log6},\qquad k\in\mathbb Z, \tag{16}
\]

with \(\beta_\pm\) given by (5). In particular the system violates its
analogue of RH.

Define its Li coefficients by

\[
 \lambda_n^{\mathcal P}
 ={1\over(n-1)!}\left.{d^n\over ds^n}
 \{s^{n-1}\log\Xi(s)\}\right|_{s=1}.                  \tag{17}
\]

Let \(h=\log6\), \(L_{n-1}=L_{n-1}^{(1)}\). Expanding the two logarithms
of (15), the identity

\[
 {1\over(n-1)!}\left.{d^n\over ds^n}
 \{s^{n-1}e^{-us}\}\right|_{s=1}
 =-u e^{-u}L_{n-1}(u)                                    \tag{18}
\]

yields the convergent arithmetic formula

\[
 \boxed{
 \lambda_n^{\mathcal P}
 =hn+h\sum_{k\ge1}{2^{-k}+3^{-k}\}L_{n-1}(kh).}        \tag{19}
\]

The generating function

\[
 \mathcal G_{\mathcal P}(z)
 =z{d\over dz}\log{\Xi(1/(1-z))\over\Xi(1)}
 =\sum_{n\ge1}\lambda_n^{\mathcal P}z^n               \tag{20}
\]

has its singularity of smallest modulus at

\[
 w_0=1-{1\over\beta_+}
 =-{\log2\over\log3},\qquad
 R:=|w_0|^{-1}={\log3\over\log2}>1.                    \tag{21}
\]

It is unique: for \(\rho=\beta_++i\gamma\),

\[
 \left|1-{1\over\rho}\right|^2
 ={(1-\beta_+)^2+\gamma^2\over\beta_+^2+\gamma^2},     \tag{22}
\]

which is strictly minimal at \(\gamma=0\); zeros with real part
\(\beta_-<1/2\) give moduli larger than one. Subtracting the principal
part at \(w_0\) and applying Cauchy's formula on a circle up to the next
singularity gives

\[
 \boxed{
 \lambda_n^{\mathcal P}=-w_0^{-n}+O(R_1^n),
 \qquad 1<R_1<R.}                                       \tag{23}
\]

In particular, for even \(n\),

\[
 \lambda_n^{\mathcal P}=-(1+o(1))R^n.                  \tag{24}
\]

---

## 3. Fully coupled prime--pole form

The falsifier can be written exactly in the form of the arithmetic gate.
For \(\varepsilon>0\), set

\[
 \begin{aligned}
 P_{n,\varepsilon}
   &=h\sum_{k\ge1}6^{-\varepsilon k}L_{n-1}(kh),\\
 Q_{n,\varepsilon}
   &=h\sum_{k\ge1}\Psi_k\,6^{-(1+\varepsilon)k}
       L_{n-1}(kh),                                      \tag{25}\\
 A_n&=hn+h\sum_{k\ge1}6^{-k}L_{n-1}(kh),\\
 \lambda_{n,\varepsilon}^{\mathcal P}
   &=A_n+P_{n,\varepsilon}-Q_{n,\varepsilon}.
 \end{aligned}
\]

All series in (25) converge absolutely. Using (4), without separating
any tower,

\[
 \begin{aligned}
 \lambda_{n,\varepsilon}^{\mathcal P}
 ={}&hn+h\sum_{k\ge1}6^{-k}L_{n-1}(kh)\\
 &+h\sum_{k\ge1}{-6^{-k}+2^{-k}+3^{-k}\}
       6^{-\varepsilon k}L_{n-1}(kh).                    \tag{26}
 \end{aligned}
\]

By (19), \(\lambda_{n,\varepsilon}^{\mathcal P}\to
\lambda_n^{\mathcal P}\) for each \(n\). What matters more here is the
diagonal \(\varepsilon_X=e^{-X/100}\). The dominant zero of the
contribution \(2^{-k}6^{-\varepsilon_Xk}\) shifts from \(\beta_+\) to
\(\beta_+-\varepsilon_X\); hence

\[
 w_X=1-{1\over\beta_+-\varepsilon_X}=w_0+O(\varepsilon_X).
 \tag{27}
\]

The remaining singularities stay uniformly separated from \(w_X\). To
make explicit that no factor was lost, (26) is the Li coefficient of the
meromorphic function

\[
 \Xi_\varepsilon(s)=6^s(1-6^{-s})
 {\{1-3\,6^{-(s+\varepsilon)}\}
  \{1-2\,6^{-(s+\varepsilon)}\}
  \over 1-6^{-(s+\varepsilon)}}.                        \tag{27a}
\]

Indeed, expanding its four logarithms reproduces (26) term by term. The
outer zero is at \(\beta_+-\varepsilon\), the artificial pole is at
\(-\varepsilon\), and the remaining fixed zero is at \(0\), in each case
together with its translates by \(2\pi i\mathbb Z/h\). The families with
real part \(0\) or \(-\varepsilon\) are sent by \(s=(1-z)^{-1}\) outside
the unit disk; so is the family with real part \(\beta_--\varepsilon<1/2\).
The non-real singularities of the family \(\beta_+-\varepsilon\) remain
uniformly farther from the origin than \(w_X\). Hence, after subtracting
the principal part at \(w_X\), there is a fixed disk, larger than
\(|w_X|\), on which the remainder is holomorphic and uniformly bounded
for small \(\varepsilon\). Cauchy's formula then gives, now uniformly as
\(\varepsilon_X\to0\),

\[
 \boxed{
 \lambda_{n,\varepsilon_X}^{\mathcal P}
 =-w_X^{-n}+O(R_1^n),\qquad
 1\le n\le X,}                                           \tag{28}
\]

for some \(1<R_1<R\), with an absolute constant uniform in \(n\) and in
large \(X\). Since \(n\varepsilon_X\to0\) uniformly for \(n\le X\),

\[
 |w_X|^{-n}=R^n(1+o(1)).                                 \tag{29}
\]

Equations (28)--(29) keep the polar channel and the whole Euler sum: they
are an evaluation of its exact difference (25), not a separate bound.

---

## 4. The deep tail has density \(1/4\)

The event in (6) is exactly equivalent to

\[
 \lambda_{n,\varepsilon_X}^{\mathcal P}+\log(n+1)
 \le-e^{\sqrt X}.                                       \tag{30}
\]

Fix \(\delta>0\). By (28)--(29), for large \(X\), every even integer

\[
 n\ge {1+\delta\over\log R}\sqrt X                     \tag{31}
\]

satisfies (30), and no odd integer in that range satisfies it. On the
other side, (28) together with a uniform Cauchy bound for the smaller
degrees show that (30) fails to hold when

\[
 n\le {1-\delta\over\log R}\sqrt X.                    \tag{32}
\]

The strip between (31) and (32) has harmonic mass \(O_\delta(1)\), which
is \(o(H_X)\). Finally,

\[
 \sum_{\substack{c\sqrt X\le n\le X\\2\mid n}}{1\over n}
 ={1\over2}\log{X\over c\sqrt X}+O(1)
 ={1\over4}\log X+O_c(1).                              \tag{33}
\]

Dividing by \(H_X=\log X+O(1)\), and then letting \(\delta\downarrow0\),
proves (6).

---

## 5. Exact scope of the no-go

System (2) simultaneously satisfies:

1. non-negative Mangoldt weights, constant on each tower;
2. unit multiplicity of each formal prime;
3. exact divisor renewal (12);
4. Euler product with \(\pi_d\in\mathbb Z_{\ge0}\);
5. exact functional equation (3);
6. a degree prime law with relative error \(O(2^{-k})\);
7. the same Laguerre phase and the same pole--Euler coupling of (25).

And yet it fails the deep limit, with exact value \(1/4\). Hence no
**universal** inequality derived solely from those seven inputs can prove
`104_75`.

The system does not share several essential features of the Riemann
zeta: the norm spectrum consists of powers of six with multiplicity, not
all integers with ordinary factorization; its completion does not
contain the real Gamma factor of \(\zeta\); and it is a graded system, so
it has vertical periodicity and poles along the whole progression
\(1+2\pi i\mathbb Z/\log6\), not a single pole on the line
\(\Re s=1\).

In particular, it also fails the ordinary PNT in the continuous norm
variable. If

\[
 \psi_{\mathcal P}(x)
   =\sum_{|N|\le x}\Lambda_{\mathcal P}(N),
\]

then

\[
 \psi_{\mathcal P}(6^k)
 =h\sum_{j\le k}(6^j+1-3^j-2^j)
 ={6h\over5}\,6^k+O(3^k+k),                             \tag{34}
\]

while the same function remains constant on \([6^k,6^{k+1})\). Thus
\(\psi_{\mathcal P}(x)/x\) oscillates between distinct limits (from
\(h/5\) to \(6h/5\), up to the convention at the endpoints) and does not
tend to \(1\).

These features are not hidden defects of the falsifier: they mark
exactly its scope. The document rules out a universal theorem based on
the seven degree inputs listed above; it does **not** rule out an
argument that uses the continuous PNT, the non-lattice support
\(\{\log m:m\in\mathbb N\}\), the multiplicity-one property of every
ordinary integer norm, or the Gamma factor. A proof for the real weights
\(\Lambda(m)\) must essentially use at least one property that the model
does not preserve.

**Verdict.** The unitary selector and the multiplicative interactions of
`104_20`/`104_48`/`104_49` cannot, as abstract axioms, give the requested
one-sided bound. The only surviving front remains a specific inequality
about the ordinary placement \(\{\log p\}\) and about Riemann's Gamma
factor. That inequality was not obtained here.

---

## 6. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 unit_renewal_euler_deep_tail_falsifier.py
```

The checker verifies exactly the multiplicities, (13), the renewal on
formal test elements, and (14). It numerically verifies the dominant
singularity of (20) by Cauchy extraction and the convergence of the
model's dominant harmonic density to \(1/4\). The proof of the statements
for every degree is in the text.
