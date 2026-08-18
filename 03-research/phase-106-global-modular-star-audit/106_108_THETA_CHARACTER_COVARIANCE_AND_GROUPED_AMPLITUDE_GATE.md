# 106.108 — Theta-character covariance and the grouped-amplitude gate

## 1. Purpose and verdict

Document 106.107 evaluates every nonzero residue character of the rational
theta lattice, but leaves open whether the signed reflected masses can be
grouped *before* taking a square root.  This note answers that question
exactly.

For every prime-power displacement and every point in its positive theta
tail, the signed reflected character sums assemble into a positive
semidefinite circulant matrix.  It has a canonical, globally grouped square
root.  Thus the sign changes of the reflected atoms do **not** prevent an
amplitude construction: they prevent only a termwise one.

The grouped square root, however, is unitarily equivalent to the original
positive residue amplitudes.  After the divisible, fractional, central and
Gamma channels are assembled, every exact Hilbert amplitude obtained in
this way is an isometric recoding of the already known complete source
gradient.  Coupling the polar channel to such an amplitude has the fixed
minimal gain

\[
 (2\inf\sigma A)^{-1/2}.
\]

Consequently residue Fourier--Poisson duality supplies a rigorous signed
amplitude, but no additional norm slack.  A joint Hilbert square including
the pole exists exactly when the physical surplus is already true.  This
is a precise gate for the residue-character route, not a proof of the
surplus.

No zero location is used below.

## 2. Positive residue masses

Fix \(n\geq2\) and \(x\geq\log n\).  For
\(r\in\mathbb Z/n\mathbb Z\), define the bilateral residue mass

\[
 M_{n,r}(x)
 :=\sum_{\substack{j\in\mathbb Z\\j\equiv r\ ({\rm mod}\ n)}}
       k_{|j|/n}(x).
 \tag{1}
\]

The term \(j=0\) vanishes because \(k_0=0\).  Every other summand is
strictly positive on the stated domain: indeed

\[
 \frac{|j|}{n}e^x\geq |j|\geq1.
\]

Hence

\[
 M_{n,r}(x)\geq0.                                  \tag{2}
\]

The zero-residue mass and the complete fractional mass are

\[
 M_{n,0}(x)=2K(x),                                  \tag{3}
\]

and

\[
 \sum_{r\ne0}M_{n,r}(x)=2\sqrt n\,R_n(x).          \tag{4}
\]

Equation (4) follows by pairing \(j\) with \(-j\) in the definition of
the fractional remainder of 106.38.

Let \(U_n\) be the unitary finite Fourier matrix

\[
 (U_n)_{a r}=n^{-1/2}e^{2\pi i ar/n},
 \qquad 0\leq a,r<n.                               \tag{5}
\]

## 3. The reflected character covariance

Define

\[
 C_n(x)
 :=U_n\,\mathrm{diag}
       \bigl(M_{n,0}(x),\ldots,M_{n,n-1}(x)\bigr)U_n^*.
 \tag{6}
\]

### Theorem 1 — Signed Poisson sums form a positive circulant covariance

The matrix \(C_n(x)\) is positive semidefinite and its entries are

\[
 \boxed{
 (C_n(x))_{ab}
 =\frac1n\mathcal K_{n,a-b}(x)
 =\sum_{\substack{\ell\in\mathbb Z\\
            \ell\equiv b-a\ ({\rm mod}\ n)}}k_{|\ell|}(-x).}
 \tag{7}
\]

In particular, the individual signed reflected congruence sums in (7)
are the matrix coefficients of one positive operator, even though they
need not be positive separately.

#### Proof

By (6),

\[
 (C_n(x))_{ab}
 =\frac1n\sum_{r=0}^{n-1}M_{n,r}(x)
          e^{2\pi i(a-b)r/n}.
 \tag{8}
\]

Expanding (1) turns the right side into
\(n^{-1}\mathcal K_{n,a-b}(x)\).  The residue-character Poisson identity
of 106.107 gives the second expression in (7).  Positivity follows either
from (6) and (2), or directly from

\[
 z^*C_n(x)z
 =\sum_{r=0}^{n-1}M_{n,r}(x)|(U_n^*z)_r|^2\geq0.
\]

\(\square\)

The fractional covariance is obtained by deleting the divisible residue:

\[
 C_n^\circ(x)
 :=U_n\mathrm{diag}
       \bigl(0,M_{n,1}(x),\ldots,M_{n,n-1}(x)\bigr)U_n^*.
 \tag{9}
\]

If \({\bf1}=(1,\ldots,1)^T\), then

\[
 \boxed{
 C_n^\circ(x)
 =C_n(x)-\frac{2K(x)}n{\bf1}{\bf1}^*,
 \qquad
 \ker C_n^\circ(x)\supseteq\mathbb C{\bf1}.}
 \tag{10}
\]

Moreover,

\[
 \boxed{
 \mathrm{Tr}\,C_n^\circ(x)=2\sqrt n\,R_n(x).}
 \tag{11}
\]

Thus the nonzero residue characters recover the complete fractional theta
mass, not merely a lower estimate for it.

## 4. The canonical grouped signed amplitude

Because the covariance is positive as a whole, it has the explicit square
roots

\[
\begin{aligned}
 B_n(x)
 &=U_n\mathrm{diag}
       \bigl(\sqrt{M_{n,0}(x)},\ldots,
             \sqrt{M_{n,n-1}(x)}\bigr)U_n^*,\\
 B_n^\circ(x)
 &=U_n\mathrm{diag}
       \bigl(0,\sqrt{M_{n,1}(x)},\ldots,
             \sqrt{M_{n,n-1}(x)}\bigr)U_n^*.
\end{aligned}                                      \tag{12}
\]

Their entries are generally signed or complex.  Nevertheless,

\[
 \boxed{
 B_n(x)^2=C_n(x),
 \qquad
 (B_n^\circ(x))^2=C_n^\circ(x).}                  \tag{13}
\]

This is the grouped signed amplitude which is unavailable term by term in
106.107(13).  It preserves the cancellation of the entire reflected
congruence lattice before a norm is taken.

Let

\[
 \Delta_nr(x)=r(x)-r(x-\log n).
\]

Then the fractional tail density has the exact Hilbert--Schmidt amplitude
form

\[
 \boxed{
 \frac{2\Lambda(n)}{\sqrt n}K(x)R_n(x)
       |\Delta_nr(x)|^2
 =\frac{\Lambda(n)}nK(x)
       \|B_n^\circ(x)\Delta_nr(x)\|_{\mathfrak S_2}^2.}
 \tag{14}
\]

#### Proof

Equations (12)--(13) follow by functional calculus in the diagonal residue
basis.  For (14), use

\[
 \|B_n^\circ(x)\|_{\mathfrak S_2}^2
 =\mathrm{Tr}\,C_n^\circ(x)=2\sqrt nR_n(x)
\]

and note that the spatial increment is common to every theta residue.
\(\square\)

The construction is therefore not defeated by the exponential total
variation in 106.107: it never takes absolute values of the reflected
atoms.

## 5. Why the new amplitude is an exact gauge change

The gain in (12) is representational rather than coercive.  In the
positive residue basis the amplitude vector is

\[
 \bigl(\sqrt{M_{n,r}(x)}\,\Delta_nr(x)\bigr)_{r}.
 \tag{15}
\]

Finite Fourier transformation sends (15) isometrically to the character
basis.  Formula (12) is the operator-valued version of precisely this
unitary change of basis.  Therefore

\[
 \sum_r M_{n,r}(x)|\Delta_nr(x)|^2
 =\|U_n(\sqrt{M_{n,r}(x)}\Delta_nr(x))_r\|^2.      \tag{16}
\]

The same statement holds after the zero-residue sector is removed.  On its
own spatial interval, the far endpoint of the central crossing channel has
the exact zero-congruence expansion

\[
 K(\log n-x)=\sqrt n\sum_{m\geq1}k_{nm}(-x),
 \qquad0\leq x\leq\log n,
\]

but the central channel remains an orthogonal positive edge fiber; adding
it does not alter (16).  The Gamma channel is likewise already a positive
continuous amplitude.
Consequently, direct integration of (12), together with the central and
Gamma amplitudes, produces a closed gradient

\[
 \widetilde{\mathcal G}=W\mathcal G                \tag{17}
\]

on the source-gradient range, where \(W\) is an isometry and

\[
 \boxed{
 \widetilde{\mathcal G}^{,*}\widetilde{\mathcal G}
 =\mathcal G^*\mathcal G=A.}                      \tag{18}
\]

Thus all fractional phases, the central channel and Gamma can be assembled
in one grouped Hilbert amplitude, but the operation leaves the physical
generator unchanged.

## 6. Exact no-go for a pole-coupled grouped square

The pole is the negative polar variance channel.  On the centered shorted
space,

\[
 D_\mu^*D_\mu=\frac12I.                            \tag{19}
\]

The next theorem covers not only the explicit Fourier square root (12),
but every exact regrouping of the complete positive source channels.

### Theorem 2 — Grouping cannot change the transfer gain

Let \(\mathcal B\) be any closed Hilbert amplitude on the shorted form
domain such that

\[
 \mathcal B^*\mathcal B=A.                         \tag{20}
\]

On \(\mathrm{ran}\,\mathcal B\), let \(T\) satisfy the exact polar
interpolation equation

\[
 T\mathcal Bf=D_\mu f.                             \tag{21}
\]

Then the closure of \(T\) is unique and

\[
 \boxed{
 \|T\|=(2\inf\sigma A)^{-1/2}.}                  \tag{22}
\]

In particular,

\[
 \boxed{
 \|T\|\leq1
 \quad\Longleftrightarrow\quad
 A\geq\frac12I.}                                  \tag{23}
\]

#### Proof

The polar decomposition of (20) is

\[
 \mathcal B=V A^{1/2},                             \tag{24}
\]

where \(V\) is an isometry on the closure of the range of \(A^{1/2}\).
Also \(D_\mu=2^{-1/2}U_D\) with \(U_D\) an isometry.  Equation (21)
therefore forces

\[
 T=2^{-1/2}U_DA^{-1/2}V^*                         \tag{25}
\]

on the defining range.  Spectral calculus gives

\[
 \|T\|^2=\frac12\|A^{-1}\|
          =\frac1{2\inf\sigma A}.
\]

This proves (22)--(23).  \(\square\)

### Corollary 3 — A Hilbert square including the pole is equivalent to the
surplus

There exists a closed operator \(H\) such that

\[
 \boxed{
 A-\frac12I=H^*H}                                  \tag{26}
\]

if and only if \(A\geq\frac12I\).  Equivalently, the block covariance

\[
 \boxed{
 \begin{pmatrix}I&T^*\\T&I\end{pmatrix}\geq0}     \tag{27}
\]

for the exact source-to-polar transfer is positive if and only if
\(\|T\|\leq1\), hence if and only if the physical surplus holds.

Therefore no cyclic covariance or square-root identity at the source
level can make the pole coupling positive automatically.  The only new
possible estimate would have to use the literal arithmetic to prove the
positivity of (27); constructing its Cholesky factor without that estimate
would assume the desired conclusion.

## 7. Heat and hybrid rows do not create a hidden range gain

The grouped amplitude can also be tested only on the faithful heat rows,
rather than on the whole form domain.  This restriction gives a strict
finite-time improvement over the global transfer norm, but not an
improvement relative to the required threshold.

Let

\[
 \Gamma_t=e^{-t(A+1/2)/2}V e^{-t(A+1/2)/2},
\]

where \(V>0\) is injective and trace class, and let \(\mathcal B\) be any
grouped exact amplitude satisfying (20).  Then

\[
\begin{aligned}
 \|\mathcal B\Gamma_t^{1/2}\|_{\mathfrak S_2}^2
 &=\mathrm{Tr}(A\Gamma_t),\\
 \|D_\mu\Gamma_t^{1/2}\|_{\mathfrak S_2}^2
 &=\frac12\mathrm{Tr}\,\Gamma_t.
\end{aligned}                                      \tag{28}
\]

Consequently the exact transfer gain on the heat row is

\[
 \boxed{
 g_V(t)^2
 :=\frac{\|D_\mu\Gamma_t^{1/2}\|_{\mathfrak S_2}^2}
          {\|\mathcal B\Gamma_t^{1/2}\|_{\mathfrak S_2}^2}
 =\frac1{2R_V(t)},
 \qquad
 R_V(t)=\frac{\mathrm{Tr}(A\Gamma_t)}
                   {\mathrm{Tr}\,\Gamma_t}.}
 \tag{29}
\]

By the faithful spectral-measure calculation of 106.103,

\[
 R_V'(t)=-\mathrm{Var}_t(\lambda)\leq0,
 \qquad
 R_V(t)\downarrow\alpha:=\inf\sigma(A).           \tag{30}
\]

Thus

\[
 \boxed{g_V(t)\longrightarrow(2\alpha)^{-1/2}.}    \tag{31}
\]

If the heat measure is not supported entirely at its spectral bottom,
then \(R_V(t)>\alpha\) for every finite \(t\), and hence the finite-time
gain is strictly below the global gain (22).  This strictness disappears
in the cofinal limit.  If \(\alpha<1/2\), then \(g_V(t)>1\) for all
sufficiently large \(t\); if \(\alpha=1/2\), then \(g_V(t)\to1\) and no
uniform strict defect survives.

The same computation applies after adjoining finitely many hybrid rows and
then shorting their exact radical component: it uses only the Gram identity
\(\mathcal B^*\mathcal B=A\).  Hence heat covariance imposes no additional
cofinal range restriction absent from the canonical transfer norm.

## 8. Radical and subthreshold stress tests

On every exact radical multiplier the unshorted generator has eigenvalue
\(1/2\).  Equations (22)--(23) give gain one, so the grouped residue
amplitude preserves radical equality exactly.

If a hypothetical shorted eigenvector satisfies

\[
 Aq=\alpha q,
 \qquad0<\alpha<\frac12,
\]

then every grouped exact amplitude satisfies

\[
 \frac{\|D_\mu q\|}{\|\mathcal Bq\|}
 =\frac1{\sqrt{2\alpha}}>1.                       \tag{32}
\]

The cyclic covariance identities (7)--(14) remain valid in that
counterfactual.  Hence the construction passes the required falsifier: it
does not turn Poisson duality into a false proof of contractivity.

## 9. Status

Proved here:

* the exact positive circulant covariance of all signed reflected residue
  characters;
* its explicit grouped signed square root;
* the exact Hilbert--Schmidt amplitude for the complete fractional theta
  channel;
* compatibility of the grouped amplitude with central and Gamma channels;
* unitary equivalence with the original complete source gradient;
* invariance of the exact source-to-polar gain under every such grouping;
* exact convergence of the heat-row gain to the same canonical gain;
* equivalence between a pole-coupled Hilbert square and the physical
  surplus itself.

Not proved here:

\[
 A\geq\frac12I.
\]

The residue-character route has nevertheless been exhausted at the
amplitude level: the missing square root exists and is explicit, but it is
an isometric recoding of the source.  A successor must prove a genuinely
arithmetic lower bound for the block covariance (27), rather than seek a
different square root of its already positive source corner.
