# 106.150 — Threshold counting and the non-Schatten Birman--Schwinger gate

## 1. Purpose and verdict

After the complete radical anti-short, put

\[
 \mathscr C=(\mathbf 1\oplus\mathcal R)^\perp,
 \qquad A=L|_{\mathscr C}.
 \tag{1}
\]

The essential-threshold theorem gives

\[
 \sigma_{\rm ess}(A)\subset[1/2,\infty),
 \tag{2}
\]

but it permits isolated eigenvalues in \((0,1/2)\), possibly infinitely
many and accumulating at \(1/2\).  This note tests whether a counting
argument can be stronger than the sharp form inequality.  The answer is
negative, for three independent and exact reasons.

1. The faithful localized Birman--Schwinger operator of 106.59 is compact,
   but, for every ordinary local boost, it is in no Schatten class.  This
   remains true after the complete radical anti-short.  Thus neither its
   trace nor any power trace is available for a CLR-type estimate.
2. If the boost is replaced by a smoothing trace-class boost, counting is
   restored, but the statement that no Birman--Schwinger eigenvalue reaches
   one is exactly the original physical surplus.
3. There is no parity improvement.  A single hypothetical off-line orbit
   has a two-dimensional real residue plane of signature \((1,1)\), hence
   contributes exactly one negative direction.

The strongest unconditional counting result remains fixed-gap finiteness.
Decay of the PNT discrepancy and of the Gamma boundary correction does not
make the total subthreshold count finite: an exact threshold model with
arbitrarily fast decaying wells can still have infinitely many bound
states accumulating at \(1/2\).  Literal arithmetic must therefore assign
the sign, not merely the size, of the moving boundary correction.

## 2. The exact counting identity

Fix \(0<\lambda<1/2\).  Choose the compactly supported boost of 106.59,

\[
 V=M Q M_vQ\geq0,
 \qquad Q=P_{\mathscr C},
 \tag{3}
\]

so that

\[
 C=A+V-\lambda>0.
 \tag{4}
\]

The faithful Birman--Schwinger operator is

\[
 \mathcal K_\lambda=C^{-1/2}VC^{-1/2}.
 \tag{5}
\]

It is positive and compact, and the form factorization

\[
 A-\lambda=C^{1/2}(I-\mathcal K_\lambda)C^{1/2}
 \tag{6}
\]

gives the exact min--max count

\[
 \boxed{
 N_{(0,\lambda)}(A)=N_{(1,\infty)}(\mathcal K_\lambda),}
 \tag{7}
\]

with the usual harmless endpoint modification when \(\lambda\) is an
eigenvalue.  In particular,

\[
 N_{(0,\lambda)}(A)=0
 \quad\Longleftrightarrow\quad
 \|\mathcal K_\lambda\|\leq1.
 \tag{8}
\]

Equation (8) is already the physical floor at \(\lambda\).  A counting
method can help only if it supplies an independently computable quantity
strictly below one.

## 3. Critical-line modes survive the complete short

Let \(\gamma\) be the ordinate of a zero of \(\Xi\) on the real axis and
put

\[
 q_\gamma(x)={\cos(\gamma x)\over h(x)},
 \qquad h(x)=\cosh(x/2).
 \tag{9}
\]

The exact identities in 106.62 give

\[
 q_\gamma\in\mathscr C.
 \tag{10}
\]

There are infinitely many such \(\gamma\).  This fact is unconditional.
Write

\[
 \omega_0(x)={K(x)\over c_Kh(x)},
 \qquad
 \omega_v(x)={v(x)K(x)\over c_Kh(x)}.
 \tag{11}
\]

Both are smooth and rapidly decreasing; \(\omega_0>0\), and \(\omega_v\)
is nonzero when the boost is nontrivial.  Hence

\[
 \begin{aligned}
 \langle q_\gamma,q_\eta\rangle
 &=\int\omega_0(x)\cos(\gamma x)\cos(\eta x)\,dx,\\
 M^{-1}\langle q_\gamma,Vq_\eta\rangle
 &=\int\omega_v(x)\cos(\gamma x)\cos(\eta x)\,dx.
 \end{aligned}
 \tag{12}
\]

### Lemma 1 — A linearly numerous radical-complement Riesz sequence

There is a sequence of real zeros \((\gamma_j)\), constants
\(0<a<b<\infty\), and \(C<\infty\), such that

\[
 \gamma_j\leq Cj
 \tag{13}
\]

and, for every finitely supported scalar sequence \((z_j)\),

\[
 \begin{aligned}
 a\sum_j|z_j|^2
 &\leq\left\|\sum_jz_jq_{\gamma_j}\right\|^2
 \leq b\sum_j|z_j|^2,\\
 a\sum_j|z_j|^2
 &\leq M^{-1}\left\langle\sum_jz_jq_{\gamma_j},
 V\sum_kz_kq_{\gamma_k}\right\rangle.
 \end{aligned}
 \tag{14}
\]

#### Proof

Choose a large separation \(D\).  Use the unconditional positive-proportion
theorem for critical-line zeros,

\[
 N_0(T)\gg T\log T,
 \tag{15a}
\]

together with the standard local upper bound
\(N(T+1)-N(T)=O(\log T)\).  These two estimates permit a
\(D\)-separated subsequence with \(\gg T\) members below \(T\).  Enumerate
it to obtain (13).  Indeed, partition a dyadic interval into cells of
length \(D\); each occupied cell contains \(O_D(\log T)\) zeros, whereas
the critical-line zeros in the whole interval number \(\gg T\log T\).
Keeping alternate occupied cells leaves \(\gg T\) separated ordinates.

The two Gram matrices in (12) have diagonal limits

\[
 {1\over2}\int\omega_0>0,
 \qquad {1\over2}\int\omega_v>0.
 \tag{15}
\]

Their off-diagonal entries are sums of Fourier transforms evaluated at
\(\gamma_j-\gamma_k\) and \(\gamma_j+\gamma_k\).  Those transforms decrease
faster than every power.  Taking \(D\) large makes the sum of the absolute
off-diagonal entries in every row smaller than half the corresponding
diagonal lower bound.  Schur's test, or Gershgorin applied to every finite
section, proves (14).  \(\square\)

## 4. The local Birman--Schwinger operator is not trace class

### Lemma 2 — Logarithmic energy of a zero mode

Uniformly for real \(\gamma\geq2\),

\[
 \boxed{\langle q_\gamma,Cq_\gamma\rangle
 \leq C_0\log(2+\gamma).}
 \tag{16}
\]

#### Proof

The literal prime generator is bounded by 106.123.  The boost and the
scalar \(-\lambda\) are bounded.  For the Gamma form, the small-displacement
difference obeys

\[
 J_u(q_\gamma)\leq C\min\{1,\gamma^2u^2\},
 \qquad 0<u\leq1,
 \tag{17}
\]

while the remaining range is uniformly integrable because of the theta
weights.  Since the Gamma density is \((2u)^{-1}+O(1)\) at zero,

\[
 \int_0^1{\min(1,\gamma^2u^2)\over u}\,du
 =O(\log(2+\gamma)).
 \tag{18}
\]

This proves (16).  \(\square\)

### Theorem 3 — Non-Schatten obstruction after complete anti-shorting

For every nontrivial local boost (3),

\[
 \boxed{\mathcal K_\lambda\notin\mathfrak S_p
 \quad\text{for every }0<p<\infty.}
 \tag{19}
\]

In particular,

\[
 \boxed{\operatorname {Tr}\mathcal K_\lambda=\infty.}
 \tag{20}
\]

#### Proof

Let \(F_N=\operatorname {span}\{q_{\gamma_1},\ldots,q_{\gamma_N}\}\).
In the coefficient basis denote the compressions of the forms of \(C\)
and \(V\) by \(C_N\) and \(V_N\).  Lemma 1 gives

\[
 V_N\geq aM I,
 \tag{21}
\]

and Lemma 2, (13), and positivity give

\[
 \operatorname {Tr}C_N
 \leq C\sum_{j\leq N}\log(2+\gamma_j)
 \leq CN\log(2+N).
 \tag{22}
\]

Compress \(\mathcal K_\lambda\) to \(C^{1/2}F_N\).  Its trace there is
the generalized trace

\[
 \operatorname {Tr}(C_N^{-1}V_N).
 \tag{23}
\]

By (21), the arithmetic--harmonic mean inequality, and (22),

\[
 \begin{aligned}
 \sum_{j=1}^Ns_j(\mathcal K_\lambda)
 &\geq\operatorname {Tr}(C_N^{-1}V_N)\\
 &\geq aM\operatorname {Tr}(C_N^{-1})\\
 &\geq {aMN^2\over\operatorname {Tr}C_N}
 \geq c{N\over\log(2+N)}.
 \end{aligned}
 \tag{24}
\]

Ky Fan's principle justifies the first inequality.  Letting \(N\to\infty\)
proves (20).  For \(p\geq1\), convexity gives

\[
 \sum_{j\leq N}s_j(\mathcal K_\lambda)^p
 \geq N\left({c\over\log(2+N)}\right)^p\longrightarrow\infty.
 \tag{25}
\]

For \(0<p<1\), membership in \(\mathfrak S_p\) would imply trace-class
membership because \(s_j\to0\).  This contradicts (20).  \(\square\)

The obstruction is not the absence of compactness: 106.59 proves that
\(\mathcal K_\lambda\) is compact.  Its eigenvalues merely decrease too
slowly for trace counting.  The logarithmic Gamma kinetic energy is the
exact source of the rate in (24).

## 5. Smoothing the boost does not weaken the missing theorem

One can choose an injective smoothing boost \(V_s\) for which

\[
 V_s^{1/2}(A+V_s-\lambda)^{-1}V_s^{1/2}
 \tag{26}
\]

is trace class.  Then the sufficient estimate

\[
 \operatorname {Tr}\mathcal K_{\lambda,s}<1
 \tag{27}
\]

would exclude a bound state.  It is not supplied by positivity or by heat
regularization.  The exact factorization still gives

\[
 N_{(0,\lambda)}(A)=N_{(1,\infty)}(\mathcal K_{\lambda,s}).
 \tag{28}
\]

Thus an eigenstate below \(\lambda\) forces an eigenvalue larger than one
in (26), and hence forces its trace to exceed one.  Proving (27) is already
a bound-state exclusion estimate for the literal joint form.  Changing
the singular-value summability of the coordinate does not create sign
slack.

The relative-heat observable has the same limitation.  A trace-class heat
boost gives finite weighted spectral mass, but an escaping eigenvector can
have arbitrarily small boost weight.  Document 106.101 proves that once a
bottom cluster is seen, its large-time coefficient is its integer
multiplicity; positivity of that coefficient does not exclude the cluster.

## 6. The maximal fixed-gap phase-space count

There is a quantitative count at every fixed distance from the threshold.
It does not extend to the complete interval.

Put

\[
 \mathscr H_\delta
 =\operatorname {Ran}\mathbf1_{(0,1/2-\delta]}(A),
 \qquad 0<\delta<1/2.
 \tag{28a}
\]

The tail floor and the nonlocal IMS estimate give a compactly supported
cutoff \(\chi_\delta\) and a number \(m_\delta>0\) such that

\[
 \|\chi_\delta q\|_{L^2(dx)}^2
 \geq m_\delta\|q\|_{L^2(\mu_K)}^2
 \qquad(q\in\mathscr H_\delta).
 \tag{28b}
\]

Let \(C_\delta\) be the local second-log constant supplied by 106.123 on
the support of \(\chi_\delta\).  The eigen-equation and boundedness of the
prime generator imply, for every \(q\in\mathscr H_\delta\),

\[
 \int\log^2(2+|\xi|)
 |\widehat{\chi_\delta q}(\xi)|^2d\xi
 \leq C_\delta\|q\|^2.
 \tag{28c}
\]

Choose

\[
 \log^2(2+\Omega_\delta)\geq {2C_\delta\over m_\delta}.
 \tag{28d}
\]

Then the Fourier projection \(P_{\Omega_\delta}\) satisfies

\[
 \|P_{\Omega_\delta}(\chi_\delta q)\|_2^2
 \geq {m_\delta\over2}\|q\|^2
 \qquad(q\in\mathscr H_\delta).
 \tag{28e}
\]

If \(w=d\mu_K/dx\), the operator
\(P_{\Omega_\delta}M_{\chi_\delta}:L^2(\mu_K)\to L^2(dx)\)
is Hilbert--Schmidt and

\[
 \|P_{\Omega_\delta}M_{\chi_\delta}\|_{\rm HS}^2
 ={\Omega_\delta\over\pi}
 \int_{\mathbb R}{|\chi_\delta(x)|^2\over w(x)}dx.
 \tag{28f}
\]

Summing (28e) over an orthonormal basis of \(\mathscr H_\delta\) gives the
explicit phase-space estimate

\[
 \boxed{
 N_{(0,1/2-\delta]}(A)
 \leq {2\Omega_\delta\over\pi m_\delta}
 \int_{\mathbb R}{|\chi_\delta(x)|^2\over w(x)}dx.}
 \tag{28g}
\]

No numerical constant has been inferred from sampling: every quantity in
(28g) is a proved localization or ellipticity constant.  The estimate
improves the first-log scale of 106.120 from an exponential in
\(1/\delta\) to the second-log scale
\(\Omega_\delta=\exp O(\sqrt{C_\delta/m_\delta})\).  It is necessarily
nonuniform: the existing theorems give neither a positive lower bound for
\(m_\delta\) nor a bounded \(C_\delta\) as \(\delta\downarrow0\).

## 7. No parity or quartet-count shortcut

The real residue plane associated with one hypothetical off-line orbit is
the plane of 106.45.  Its matrix is

\[
 M_{s_0}=
 \begin{pmatrix}\alpha&\beta\\-\beta&-\kappa\end{pmatrix},
 \qquad
 \det M_{s_0}=\beta^2-\alpha\kappa<0.
 \tag{29}
\]

Therefore its real signature is

\[
 \boxed{\operatorname {sig}M_{s_0}=(1,1).}
 \tag{30}
\]

A conjugate/reflection quartet supplies one negative real channel, not an
even number of negative channels.  Hence an estimate

\[
 N_{(0,1/2)}(A)\leq1
 \tag{31}
\]

would not exclude the minimal off-line falsifier.  The required integer
bound is exactly

\[
 \boxed{N_{(0,1/2)}(A)=0.}
 \tag{32}
\]

## 8. Why discrepancy decay does not control the total count

The following model isolates the logical content of tail decay.  Let
\(\varepsilon_j>0\) decrease to zero at an arbitrarily prescribed rate.
Take mutually orthogonal boundary cells, give each cell one normalized
constant mode \(e_j\), and define

\[
 A_{\rm mod}e_j=(1/2-\varepsilon_j)e_j.
 \tag{33}
\]

On the orthogonal internal modes of the \(j\)-th cell, put an unbounded
logarithmic Gamma operator with eigenvalues \(1/2+\log(2+n)\).  Add an
independent threshold radical on which the operator equals \(1/2\), and
then short that radical exactly.

This model has all of the soft properties used by a threshold-counting
argument:

* local logarithmic compactness;
* essential threshold \(1/2\);
* a tail floor \(1/2-o(1)\);
* an arbitrarily rapidly decaying signed boundary correction;
* an exact removable threshold radical.

Nevertheless

\[
 \boxed{N_{(0,1/2)}(A_{\rm mod})=\infty.}
 \tag{34}
\]

This is a methodological falsifier, not a replacement for the ordinary
primes.  It proves that PNT-envelope decay, Gamma compactness and exact
anti-shorting cannot imply a finite total count.  In the literal problem,
106.127 identifies the missing extra datum: the sign of the compressed
moving Abel flux on \(\operatorname {Ran}Q_R\).  The theta boundary width
\(\varepsilon_R\asymp e^{-2R}\) tends to zero, so strong smallness of the
boundary correction gives no norm or counting smallness on those moving
ranges.

## 9. Result

For every fixed \(\delta>0\), 106.120 already proves

\[
 N_{(0,1/2-\delta]}(A)<\infty.
 \tag{35}
\]

The present note proves that the faithful local Birman--Schwinger operator
cannot sharpen (35) by a trace or power-trace estimate, even after the
complete radical anti-short.  A smoothing coordinate makes the trace
finite but returns exactly to (8), and the off-line quartet supplies no
parity gain.

Thus the counting route has the same unique nonautomatic input as the
form, heat and boundary routes:

\[
 \boxed{
 \|\mathcal K_\lambda\|\leq1\quad(0<\lambda<1/2),
 }
 \tag{36}
\]

equivalently, nonnegativity of the complete signed Abel--Gamma--PNT
boundary form.  Counting changes neither the constant nor the sign which
must be proved.
