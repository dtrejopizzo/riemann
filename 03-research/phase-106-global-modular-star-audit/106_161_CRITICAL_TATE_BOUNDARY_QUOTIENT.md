# 106.161 — The critical Tate boundary quotient

## 1. Purpose

The Tate midpoint outer factor

\[
 a_r(z)=\frac{\sqrt{1-r^2}}{1-rz}
 \tag{1}
\]

has unit norm for every \(r<1\).  Therefore its direct sum over the primes
cannot converge.  This note identifies and removes the divergence by a
geometric boundary map, rather than by subtracting scalar traces.

For \(s>1/2\), put \(r_{p,s}=p^{-s}\).  The centered local observation
\(a_{r_{p,s}}-1\) is square summable over the primes, but its norm diverges
as \(s\downarrow1/2\).  The divergence lies entirely in the common first
Hardy mode \(r_{p,s}z\).  Quotienting orthogonally by that one boundary
copy of the Hardy space has a positive critical limit.  The limit retains
all higher Taylor information of every literal prime factor.

This constructs the prime part of the gluing differential requested in
106.160.  Gamma and the polar plane still have to be coupled to the
surviving boundary channel.

## 2. The two analysis operators

Let \(H=H^2(\mathbb D)\) and

\[
 \mathcal K=\bigoplus_p H.
 \tag{2}
\]

For \(s>1/2\), define bounded operators \(D_s,B_s:H\to\mathcal K\) by

\[
\begin{aligned}
 (D_sF)_p
   &=\sqrt{\log p}\,(a_{r_{p,s}}-1)F,\\
 (B_sF)_p
   &=\sqrt{\log p}\,r_{p,s}zF.
\end{aligned}
\tag{3}
\]

Boundedness follows from
\(\|a_r-1\|_\infty=O(r)\) uniformly for \(0<r\le2^{-1/2}\) and

\[
 C_s:=\sum_p(\log p)p^{-2s}<\infty
 \qquad(s>1/2).
 \tag{4}
\]

Moreover,

\[
 \boxed{B_s^*B_s=C_sI_H.}
 \tag{5}
\]

Thus \(B_s\) has closed range and the orthogonal projection onto its range
is

\[
 P_s=B_s(C_sI)^{-1}B_s^*.
 \tag{6}
\]

The positive quotient form is

\[
 q_s(F)=\|(I-P_s)D_sF\|_{\mathcal K}^2.
 \tag{7}
\]

No signed subtraction occurs in (7).

## 3. Exact removal of the first boundary mode

Define

\[
 e_r(z)=a_r(z)-1-rz
 \tag{8}
\]

and

\[
 (E_sF)_p=\sqrt{\log p}\,e_{r_{p,s}}F.
 \tag{9}
\]

Then \(D_s=B_s+E_s\).  If \(c_r=\sqrt{1-r^2}\), the Hardy coefficients
of \(e_r\) are

\[
 c_r-1,\quad r(c_r-1),\quad c_rr^2,\quad c_rr^3,\ldots
 \tag{10}
\]

and therefore

\[
\boxed{
 \|e_r\|_{H^2}^2
 =(c_r-1)^2(1+r^2)+r^4.}
\tag{11}
\]

In particular \(\|e_r\|_{H^2}=O(r^2)\).  The stronger multiplier estimate

\[
 \|e_r\|_{H^\infty}\le C r^2
 \qquad(0<r\le2^{-1/2})
 \tag{12}
\]

follows directly from (1) and (8).  Hence

\[
 \sum_p\log p\,\|e_{p^{-1/2}}\|_\infty^2
 \ll\sum_p\frac{\log p}{p^2}<\infty.
 \tag{13}
\]

Consequently \(E_s\) converges in operator norm as \(s\downarrow1/2\) to

\[
 (E_{1/2}F)_p
 =\sqrt{\log p}\,
   \bigl(a_{p^{-1/2}}-1-p^{-1/2}z\bigr)F.
 \tag{14}
\]

## 4. Critical convergence of the quotient

The only remaining term in the projection formula is

\[
 B_s^*E_s=M_{\eta_s},
\qquad
 \eta_s(z)
 =\sum_p(\log p)r_{p,s}
   \frac{e_{r_{p,s}}(z)-e_{r_{p,s}}(0)}{z}.
 \tag{15}
\]

Indeed, if \(S=M_z\) is the Hardy shift and \(\varphi\) is analytic, then

\[
 S^*M_\varphi
 =M_{(\varphi-\varphi(0))/z}.
 \tag{15a}
\]

The subtraction of the constant coefficient in (15) is essential:
\(z^{-1}e_r\) itself is not an analytic Hardy multiplier because
\(e_r(0)=\sqrt{1-r^2}-1\ne0\).

By (12), the series in (15) converges uniformly for \(s\ge1/2\), because

\[
 \sum_p(\log p)p^{-3/2}<\infty.
 \tag{16}
\]

It follows that

\[
 \sup_{1/2<s\le s_0}\|B_s^*E_s\|<\infty.
 \tag{17}
\]

On the other hand,

\[
 C_s=\sum_p(\log p)p^{-2s}\longrightarrow+\infty
 \qquad(s\downarrow1/2).
 \tag{18}
\]

The divergence in (18) follows, for example, from Euler's divergence of
\(\sum_p1/p\) by partial summation; the stronger prime-number theorem is
not needed.

### Theorem 4.1 — Positive critical Tate quotient

For every \(F\in H\),

\[
\boxed{
 \lim_{s\downarrow1/2}q_s(F)
 =\|E_{1/2}F\|_{\mathcal K}^2.}
\tag{19}
\]

The convergence is locally uniform on bounded subsets of \(H\), and the
limit is a positive closed quadratic form represented by the bounded
operator \(E_{1/2}^*E_{1/2}\).

#### Proof

Using \(D_s=B_s+E_s\) and (6),

\[
\begin{aligned}
 (I-P_s)D_sF
 &=(I-P_s)E_sF,\\
 q_s(F)
 &=\|E_sF\|^2
   -C_s^{-1}\|B_s^*E_sF\|^2.
\end{aligned}
\tag{20}
\]

The first term converges to \(\|E_{1/2}F\|^2\) by the operator-norm
convergence following (13).  The second tends to zero by (17)--(18).
This proves (19), uniformly for \(\|F\|\) bounded.  Since \(E_{1/2}\) is
bounded, its quadratic form is closed and positive. \(\square\)

## 5. Faithfulness on the coefficient boundary

The local multiplier \(e_r\) is not identically zero for any \(r>0\).
Moreover its first nonzero Hardy coefficient is

\[
 [z^2]e_r=\sqrt{1-r^2}\,r^2>0.
 \tag{21}
\]

### Corollary 5.1 — No boundary coefficient is lost

\[
 \boxed{\ker E_{1/2}=\{0\}.}
 \tag{22}
\]

#### Proof

If \(E_{1/2}F=0\), then \(e_{p^{-1/2}}F=0\) in \(H^2\) for every prime
\(p\).  Each \(e_{p^{-1/2}}\) is a nonzero analytic function.  Since the
ring of analytic functions on the disk has no zero divisors, \(F=0\).
\(\square\)

Thus the critical prime quotient is not merely semidefinite: it is
faithful on the common Hardy boundary module.

## 6. Interpretation

The operator \(B_s\) is the rooted-divisor boundary map.  It inserts one
common boundary function \(F\) into every Tate page through the first
harmonic mode, with the literal coefficient
\(\sqrt{\log p}\,p^{-s}\).  Formula (7) is the Hilbert mapping-fibre norm
after eliminating that boundary image.

Theorem 4.1 proves three facts which were not available in the prime-wise
relative-trace construction:

1. the cofinal prime limit exists at the critical exponent after an
   orthogonal quotient;
2. positivity survives the limit without subtracting divergent scalar
   traces;
3. all higher prime modes remain jointly faithful.

The quotient deliberately removes the first Euler layer.  That layer is
not discarded: it is the boundary space \(\operatorname {Ran}B_s\).
The next gluing step must identify its renormalized critical limit with the
Gamma spin page and the \(H^0/H^2\) polar plane of 106.160.  Only after
that identification can the resulting mapping fibre be compared with CCM
degree one.

## 7. Remaining gluing equation

Let \(\mathcal H_{\rm bd}=H^2(\mathbb D)\) denote the common boundary
module.  The unfinished part of the global differential is a source-defined
map

\[
 B_\infty:\mathcal H_{\rm bd}
 \longrightarrow
 \mathcal H_\Gamma\oplus\mathcal H^{\rm triv}
 \tag{23}
\]

whose graph norm is the finite part of the divergent first-layer norm
\(C_s\|F\|^2\), and which is compatible with the Fourier--Poisson
differential.  The required identity is

\[
\boxed{
 \operatorname {FP}_{s\downarrow1/2}
 \|B_sF\|^2
 +\|B_\infty F\|_{\rm graded}^2=0}
\tag{24}
\]

at the chain level, followed by the positive mapping-fibre norm (19).
Equation (24) is a graded Lefschetz cancellation, not a positive norm
identity by itself.  Its normalization is fixed by (3), (5), and the
Gamma/polar traces of 106.160.

## 8. Status

Proved without zero input:

* the explicit rooted-divisor boundary operator \(B_s\);
* exact orthogonal shorting of its range;
* norm convergence of the higher Tate modes at \(s=1/2\);
* positivity and closedness of the critical quotient;
* faithfulness on the common Hardy coefficient module.

Still required:

* construct \(B_\infty\) and prove the graded finite-part identity (24);
* identify the resulting resonant mapping fibre with CCM degree one.

## 9. Scope correction: this is a separable coefficient sector

The common Hardy vector \(F\) in (3) assigns one coefficient sequence to
every prime tower.  A general CCM test, however, has local values
\[
 f(k\log p)
\]
which vary jointly with \(p\) and \(k\); they are not the coefficients of
one prime-independent Hardy function.  Consequently Theorem 4.1 is a
genuine positive quotient theorem for the separable diagonal coefficient
sector, but it is not by itself a localization theorem for the full CCM
test space.  In particular, Corollary 5.1 proves faithfulness only on
\(H^2(\mathbb D)\), not on resonant CCM degree one.

The full construction must replace the common Hardy module by a nuclear
generic-length module on which the prime orbits act by the literal
translations \(u=k\log p\).  The associated quadratic terms are
autocorrelations, so their direct difference-square factorization is the
Carleson/Bessel route already audited in Phases 5, 7, and 64.  Therefore
the global comparison cannot be inferred from (19); it still requires a
cohomological boundary map whose source is the actual adelic summation
complex.
