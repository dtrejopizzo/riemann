# 106.123 — Bounded prime generator and the second-log bootstrap

## 1. Purpose and conclusion

Write the complete generator on the exact radical complement as

\[
 A=G+P,
 \tag{1}
\]

where \(G\) is the continuous Gamma jump generator and \(P\) is the
ordinary prime-power jump generator.  Document 106.120 showed that one
logarithmic Gamma moment gives Hilbert compactness but not form-tail
compactness.  This note tests a possible escape: if \(P\) is bounded, an
eigenvector of \(A\) belongs to the operator domain of \(G\), and local
ellipticity should produce a second logarithmic moment.

That escape works locally.

1.  The literal prime generator is bounded on \(L^2(\mu_K)\).
2.  Every normalized subthreshold eigenstate satisfies a uniform local
    second-log-frequency estimate.  Hence its central Gamma form tails are
    uniformly integrable; the ultraviolet obstruction of 106.120 cannot
    occur on an eigenstate.
3.  The remaining nonuniformity is spatial.  For every fixed deficit it is
    removed by finite-rank compactness, but a uniform limit as the deficit
    tends to zero is equivalent to excluding a bilateral threshold-escape
    sequence in the mean-periodic radical complement.  Evenness and the
    equation \(F*K=0\) do not provide that quantitative tightness.

Thus the bounded-prime bootstrap is a genuine improvement, but it does
not by itself prove the physical floor.

## 2. Prior-work audit

The moving-PNT estimate and local logarithmic coercivity are from 106.47.
The fixed-gap finite reduction and first-log nonuniformity are in 106.120.
Document 106.121 proves that complete radical projection preserves upper
logarithmic control but no lower-frame estimate.  The argument below is
different: it uses the operator equation for an actual eigenstate to gain
one full logarithmic derivative.  The remaining spatial condition is the
same threshold compactness not supplied by the spectral-synthesis and
uncertainty attacks of 106.69--106.70.

## 3. Uniform outgoing prime rate

Put

\[
 a_n=\frac{\Lambda(n)}{\sqrt n},
 \qquad h(x)=\cosh(x/2),
 \qquad c_K=\frac12.
 \tag{2}
\]

The total outgoing prime rate in the Doob space is

\[
 \rho_p(x)=\frac{c_K}{h(x)}
 \sum_{n\ge2}a_n
 \{K(x-\log n)+K(x+\log n)\}.
 \tag{3}
\]

### Lemma 1 — Weighted prime convolution

There is an absolute finite constant \(C_K\) such that

\[
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 K(x-\log n)\le C_Ke^{x/2}
 \qquad(x\in\mathbb R).
 \tag{4}
\]

#### Proof

Chebyshev's bound and partial summation give

\[
 \sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\le C\sqrt X
 \qquad(X\ge2).
 \tag{5}
\]

Partition the variable \(y=x-\log n\) into unit intervals
\([j,j+1)\).  The contribution of one nonempty cell is at most

\[
 C e^{(x-j)/2}\sup_{j\le y<j+1}K(y).
 \tag{6}
\]

Riemann's theta kernel decreases double exponentially at both ends, so

\[
 \sum_{j\in\mathbb Z}e^{-j/2}
       \sup_{j\le y<j+1}K(y)<\infty.
 \tag{7}
\]

Summing (6) proves (4).  Empty cells cause no endpoint term. \(\square\)

Since \(K\) is even, the second sum in (3) is the first one with \(x\)
replaced by \(-x\).  Lemma 1 therefore gives

\[
 \boxed{\sup_{x\in\mathbb R}\rho_p(x)<\infty.}
 \tag{8}
\]

### Theorem 2 — The literal prime generator is bounded

The prime form is represented by a bounded positive self-adjoint operator
\(P\), and

\[
 \boxed{\|P\|\le2\|\rho_p\|_\infty.}
 \tag{9}
\]

#### Proof

The prime form is the Dirichlet form of the reversible jump kernel whose
outgoing rate is (3).  Using
\(|r(x)-r(y)|^2\le2|r(x)|^2+2|r(y)|^2\), reversibility, and (8),

\[
 0\le\mathscr E_p(r)
 \le2\|\rho_p\|_\infty\|r\|_{L^2(\mu_K)}^2.
 \tag{10}
\]

The representation theorem for bounded forms gives (9). \(\square\)

## 4. Operator-domain bootstrap

Because \(P\) is bounded, the form sum (1) is an operator sum:

\[
 D(A)=D(G),
 \qquad Gq=Aq-Pq.
 \tag{11}
\]

Consequently every normalized eigenstate

\[
 Aq=\alpha q,qquad 0<\alpha<\frac12,
 \tag{12}
\]

satisfies

\[
 \boxed{
 \|Gq\|\le\frac12+\|P\|.}
 \tag{13}
\]

This is uniform in the deficit \(1/2-\alpha\).

## 5. Local logarithmic ellipticity

Let \(I\Subset I_1\) be bounded intervals and choose
\(\chi,\chi_1\in C_c^\infty(I_1)\), with \(\chi_1=1\) near
\(\mathrm{supp}\,\chi\).  Define the translation-invariant
small-jump operator

\[
 (Mf)(x)=\int_0^{u_0}g(u)
 \{2f(x)-f(x-u)-f(x+u)\}\,du,
 \qquad
 g(u)=\frac{e^{-u/2}}{1-e^{-2u}}.
 \tag{14}
\]

Its multiplier is

\[
 m_{u_0}(\xi)=2\int_0^{u_0}g(u)(1-\cos(\xi u))\,du
 =\log(2+|\xi|)+O_{u_0}(1).
 \tag{15}
\]

### Lemma 3 — Local operator ellipticity

There is \(C_\chi<\infty\) such that every \(q\in D(G)\) obeys

\[
 \boxed{
 \int_{\mathbb R}\log^2(2+|\xi|)
 |\widehat{\chi q}(\xi)|^2d\xi
 \le C_\chi\{\|Gq\|^2+\|q\|^2\}.}
 \tag{16}
\]

#### Proof

The Gamma generator has the pointwise difference form

\[
 (Gq)(x)=\frac{c_K}{h(x)}\int_0^\infty g(u)
 \left[
 K(x-u)\{q(x)-q(x-u)\}
 +K(x+u)\{q(x)-q(x+u)\}
 \right]du.
 \tag{17}
\]

For \(x\in I_1\) and \(0<u<u_0\), replace \(K(x\pm u)\) by
\(K(x)\).  The error contains the factor
\(K(x\pm u)-K(x)=O_{I_1}(u)\), which cancels the singularity
\(g(u)=1/(2u)+O(1)\).  It is therefore an \(L^2\)-bounded integral
operator.  The range \(u\ge u_0\) is also bounded by Schur's test, using
the theta tail.  Finally,

\[
 [G,\chi]q(x)=\frac{c_K}{h(x)}\int g(|x-y|)K(y)
 \{\chi(x)-\chi(y)\}q(y)\,dy
 \tag{18}
\]

is bounded from \(L^2(\mu_K)\) to local \(L^2\): the cutoff difference
again cancels the small-jump singularity, and the long-jump tail is
Schur-summable.  Hence, with

\[
 a(x)=\frac{c_KK(x)}{h(x)},
 \qquad \inf_{I_1}a>0,
 \tag{19}
\]

one has

\[
 \|M(\chi q)\|_2
 \le C_\chi\{\|\chi_1Gq\|_2+\|q\|\}.
 \tag{20}
\]

Plancherel and (15) prove (16).  The calculation also proves that
\(\chi q\) belongs to the operator domain of \(M\), so no core-domain
extension is implicit. \(\square\)

Combining (13) and (16) gives the promised uniform estimate.

### Corollary 4 — Uniform second logarithmic moment

Every normalized subthreshold eigenstate satisfies

\[
 \boxed{
 \int\log^2(2+|\xi|)|\widehat{\chi q}(\xi)|^2d\xi
 \le C_\chi',}
 \tag{21}
\]

where \(C_\chi'\) is independent of \(\alpha<1/2\).  Consequently

\[
 \int_{|\xi|>\Omega}\log(2+|\xi|)
 |\widehat{\chi q}(\xi)|^2d\xi
 \le\frac{C_\chi'}{\log(2+\Omega)}.
 \tag{22}
\]

The same local parametrix, with a smooth Fourier cutoff and nested spatial
cutoffs, converts (22) into local Gamma-form tail compactness.  Since \(P\)
is bounded, its error is controlled by the corresponding Hilbert tail.
Thus the high-frequency packets of 106.120 cannot occur in a normalized
subthreshold eigenstate.

More explicitly, if \(S_\Omega\) is a smooth Fourier cutoff equal to one on
\(|\xi|\le\Omega\), and \(I\Subset I_1\) are fixed, then the preceding
parametrix gives

\[
 \boxed{
 \mathscr E_{\Gamma,I}
 \bigl((I-S_\Omega)(\chi q)\bigr)
 \le \frac{C_I}{\log(2+\Omega)}.}
 \tag{23}
\]

Indeed, the principal part is the multiplier \(m_{u_0}(\xi)\), so (22)
controls its tail.  The frozen-coefficient remainder and the two cutoff
commutators are bounded on \(L^2\), and their tails tend to zero by (21).
The prime contribution changes by at most
\(2\|P\|\|(I-S_\Omega)(\chi q)\|_2\), uniformly on the normalized family.
Thus (23) is a form-norm, not merely Hilbert-norm, compactness statement.

## 6. What remains: spatial threshold tightness

For a fixed \(\delta>0\), the finite-dimensional space

\[
 \mathcal H_\delta
 =\mathrm{Ran}\,\mathbf1_{(0,1/2-\delta]}(A)
 \tag{24}
\]

is uniformly tight in both Hilbert and form norm.  Corollary 4 then gives
a finite central/low-frequency block with form error smaller than
\(\delta\).  This recovers Theorem 1 of 106.120 with an actual frequency
tail estimate, rather than abstract form-core density.

Uniformity as \(\delta\downarrow0\) is now equivalent to the spatial
condition

\[
 \boxed{
 \lim_{R\to\infty}
 \sup_{\substack{Aq=\alpha q,\ 0<\alpha<1/2\\
                  \|q\|=1}}
 \|(1-\chi_R)q\|_{D(\mathfrak a)}=0.}
 \tag{25}
\]

If (25) holds, Corollary 4 and Rellich compactness give one cofinal family
of finite blocks whose errors are smaller than the individual deficits.
If it fails, fixed-gap compactness forces a sequence

\[
 \alpha_j\uparrow\frac12,
 \qquad q_j\rightharpoonup0\text{ locally},
 \tag{26}
\]

after extraction: a bilateral threshold-escape sequence.  Evenness merely
places equal packets at the two ends; it does not prevent (26).

In the mean-periodic coordinate \(F=hq\), exact radical shorting says

\[
 F*K=0.
 \tag{27}
\]

This is a closed translation-invariant linear constraint.  It supplies no
weight-sensitive estimate comparing the global form norm with restriction
to a fixed central interval: translating a mean-periodic solution preserves
the equation, and evenness only pairs the two translated packets.  What is
missing is a quantitative theorem showing that the Doob weight and the
literal prime--Gamma equation forbid such paired escape.  Promoting (27) to
(25) is precisely the weighted form-synthesis/observability problem left
open in 106.70, not a formal consequence of mean periodicity.

The relevant spectral alternatives are as follows.  If

\[
 \inf\sigma_{\rm ess}(A)>\frac12,
 \tag{28}
\]

then (25) follows for all eigenstates below \(1/2\).  If
\(1/2\in\sigma_{\rm ess}(A)\), Weyl's criterion supplies a sequence in the
mean-periodic radical complement with

\[
 \|(A-\tfrac12)q_j\|\to0,
 \qquad q_j\rightharpoonup0,
 \tag{29}
\]

and local compactness forces its mass to escape every fixed central block.
This generic Weyl sequence need not consist of subthreshold eigenstates, so
it does not by itself disprove (25).  It shows exactly why the proved
essential floor does not imply the desired uniform reduction.  Failure of
(25) would produce the stronger object (26): a Weyl sequence made of actual
subthreshold eigenstates.  The theorem currently proved in 106.47 is only
\(\sigma_{\rm ess}(A)\subset[1/2,\infty)\); it neither opens a strict gap as
in (28) nor excludes this stronger threshold escape.

## 7. Off-line stress test

For a centered off-line sample \(s=\gamma+ib\), a real analytic test with
\(F(\gamma)=0\) has negative orbit contribution

\[
 -4m_sb^2F'(\gamma)^2+O(b^4).
 \tag{30}
\]

Thus an off-line channel can approach the threshold with a quadratically
vanishing visible margin as \(b\to0\).  Corollary 4 still controls its
local ultraviolet content uniformly; it does not supply the spatial
tightness (25).  Any claimed uniform finite block must therefore be tested
against both limits simultaneously:

\[
 b\to0,
 \qquad \alpha\uparrow\frac12.
 \tag{31}
\]

## 8. Result

The literal prime generator is bounded, and this fact removes the exact
frequency obstruction isolated in 106.120: subthreshold eigenstates have a
uniform local second logarithmic moment and uniformly integrable local
Gamma form tails.

The surviving issue is not ultraviolet.  It is the spatial threshold
tightness (25), equivalently exclusion of an escaping sequence of actual
subthreshold eigenstates as in (26).  A generic Weyl sequence (29) explains
why the essential-floor theorem alone is insufficient, but is not itself a
counterexample.  Evenness and the equation \(F*K=0\) do not prove the needed
tightness.  A closing successor must establish a quantitative central
observability inequality for the literal mean-periodic prime--Gamma
operator, after complete radical anti-shorting.
