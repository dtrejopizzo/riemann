# R170_821 — Uniformity of the scale remainders

Continuation of R170_819–820 and priority 3 of
R170_818. This note determines which convergences of the scale
remainders are uniform and which are only strong. The one-sided
inequality still missing in R170_820 is not assumed. In particular, the
following two-sided bounds do not give the sign of
\(\Phi(F)+E_\rho(F)\).

## 1. Parameters and form norm

For \(T>0\) we set

\[
 N=\lceil e^{2T}\rceil,\qquad M=N^2,\qquad
 h=\frac1{2N^2},\qquad \rho=1-h.
\tag{1}
\]

Then \(N\ge2\), \(\rho\ge7/8\),

\[
 0<h\le \tfrac12e^{-4T},\qquad
 |\log\rho|\le h/\rho\le \tfrac87h.
\tag{2}
\]

We use

\[
 Q_{\log}=\left\{f\in L^2(\mathbb R):
 \int \log(2+|\xi|)|\widehat f(\xi)|^2d\xi<\infty\right\},
\quad
 \|f\|_{Q_{\log}}^2=\int \log(2+|\xi|)|\widehat f(\xi)|^2d\xi.
\tag{3}
\]

Every claim about norms of translations holds equally in \(L^2\) and in
\(Q_{\log}\), because the weight in (3) is positive and the physical
translation is a unimodular multiplication in Fourier.

## 2. The exact obstruction from translations

Let \(\tau_a f(t)=f(t+a)\), with the Paper 46 convention. For any
\(a,b\in\mathbb R\),

\[
 \|\tau_b-\tau_a\|_{L^2\to L^2}
 =\|\tau_b-\tau_a\|_{Q_{\log}\to Q_{\log}}
 =\begin{cases}0,&a=b,\\2,&a\ne b.\end{cases}
\tag{4}
\]

Indeed, with the corpus's transform convention, the operator is
multiplication by
\(e^{-ib\xi}-e^{-ia\xi}\). If \(a\ne b\), its essential supremum is
\(2\), and the norm of a multiplier on either space is that supremum.
In particular, for \(a\ne0\) and \(\rho\ne1\),

\[
 \boxed{\ \|\tau_{a/\rho}-\tau_a\|=2.\ }
\tag{5}
\]

Hence it is false that
\(\tau_{a/\rho}-\tau_a=O(1-\rho)\) in operator norm, even when
\(a=\log d\) and \(1-\rho=1/(2N^2)\).

There is, however, strong convergence. For every \(f\in Q_{\log}\),

\[
 \|(\tau_{a/\rho}-\tau_a)f\|_{Q_{\log}}\longrightarrow0
 \quad(\rho\to1),
\tag{6}
\]

by dominated convergence. If in addition
\(Df\in Q_{\log}\), then the group's integral formula gives the rate

\[
 \|(\tau_{a/\rho}-\tau_a)f\|_{Q_{\log}}
 \le |a|\,|\rho^{-1}-1|\,\|Df\|_{Q_{\log}}.
\tag{7}
\]

R170_819 does not prove that additional regularity for a contact
vector. Thus, (7) cannot be applied to the general radical.

For the finite sums of R170_820, the only immediate universal bound is,
for example,

\[
 \|S_N^{(\rho)}-S_N\|
 \le2\sum_{n\le N}n^{-1/2},
\tag{8}
\]

and

\[
 \|H_{M,N}^{(\rho)}-H_{M,N}\|
 \le2\sum_{N<k\le MN}\frac{h_{M,N}(k)}{\sqrt k}.
\tag{9}
\]

These bounds are two-sided, grow with the cutoff, and carry no factor
\(h\). The cancellation \(\Lambda*1=\log\) removes exactly the part
\(k\le N\), but does not change (5) for the tail terms. Separating (9)
from the other PC terms loses precisely the correlations that R170_820
preserves.

## 3. The Gamma defect IS small in norm

The symbol

\[
 m(x)=\Re\psi(1/4+ix/2)-\log\pi
\]

is \(C^1\), even, and satisfies
\(m(x)=\log(|x|/(2\pi))+O(|x|^{-1})\) as \(|x|\to\infty\).
The Bernstein series representation of Paper 46, or the derivation of
the digamma series, further shows that \(xm'(x)\) is continuous and
bounded (it tends to \(1\) at both infinities and to \(0\) at the
origin). Let

\[
 C_m:=\sup_{x\in\mathbb R}|xm'(x)|<\infty.
\tag{10}
\]

The fundamental theorem of calculus on the logarithmic variable gives,
for every \(0<\rho\le1\),

\[
 \sup_x|m(x/\rho)-m(x)|\le C_m|\log\rho|.
\tag{11}
\]

Consequently

\[
 \|m(D/\rho)-m(D)\|_{L^2\to L^2}
 =\|m(D/\rho)-m(D)\|_{Q_{\log}\to Q_{\log}}
 \le \frac87 C_mh.
\tag{12}
\]

This is an essential difference from the prime block: the Gamma
remainder is \(O(h)\) in operator norm, while each translation
difference does not converge in that norm. The sum
\(A_M^{(\rho)}-A_M\) does not inherit (12), since it contains the
latter.

## 4. Fourier, Tate, and the primitivity correctors

The dilation family is strongly continuous on \(L^2\) and on
\(Q_{\log}\). In particular, for fixed data,

\[
 \mathscr F_\rho f-\mathscr Ff
 =D_\rho^*\mathscr FD_\rho f-\mathscr Ff\longrightarrow0
 \quad\hbox{in }Q_{\log}.
\tag{13}
\]

The strong convergence of the dilations, used to prove (13), does not
by itself supply a rate uniform over the unit ball for
\(\mathscr F_\rho-\mathscr F\). Hence (13), without an additional
estimate specific to that conjugated family, likewise does not give a
useful uniform bound for \(\Delta E\) in (7) of R170_820.

For a fixed Tate vector \(r\in Q_{\log}^*\) and fixed tests converging
in \(Q_{\log}\),

\[
 |\Delta_{\rm Tate}(r;v_\rho,v)|
 \le \|r\|_{Q_{\log}^*}\|v_\rho-v\|_{Q_{\log}}=o(1).
\tag{14}
\]

There is no bound in R170_814–820 uniform in \(T\) for
\(\|r_F\|_{Q_{\log}^*}\), nor a uniform rate for the second factor.
Hence (14) is qualitative and contact-dependent.

The two corrector coefficients do admit an elementary bound for each
\(T\). If \(F\) is primitive, the change of variables in
\(C(D_\rho F)\) and \(S(D_\rho F)\), followed by the mean value
theorem, produces

\[
 |C(D_\rho F)|+|S(D_\rho F)|
 \le h\,K_T\|F\|_2,
\tag{15}
\]

where one may take

\[
 K_T=2\sqrt{2T}\sup_{|s|\le T,\,7/8\le u\le1}
 \left|\partial_u\bigl(u^{1/2}\cosh(us/2)\bigr)\right|
 +2\sqrt{2T}\sup_{|s|\le T,\,7/8\le u\le1}
 \left|\partial_u\bigl(u^{1/2}\sinh(us/2)\bigr)\right|.
\tag{16}
\]

The constant can be improved, and parity removes one of the two terms,
but (15) suffices to identify the quantifiers. Turning it into a bound
for \(C(D_\rho F)p+S(D_\rho F)q\) additionally requires the norms of
\(p,q\), which depend on \(T\) and on their denominators. This estimate
does not control \((D_\rho-I)F\): R170_819 correctly pointed out that a
rate \(O(h)\) for this term requires membership in the domain of the
dilation generator.

## 5. What improves at a first contact

For a fixed \(T\), the radical \(\ker H_T\) is finite dimensional.
Every strongly continuous, locally uniformly bounded family of
operators then converges uniformly on the unit sphere of that radical.
Thus, for each fixed contact and each fixed finite sum, there exists a
radical-dependent modulus

\[
 \omega_T(\rho)\to0\quad(\rho\to1)
\tag{17}
\]

that controls the differences of translations, dilations, and Fourier
applied to \(F\in\ker H_T\), \(\|F\|=1\). This avoids the operator-norm
obstruction (5) at an individual contact.

But (17) does not make recipe (1) uniform: the subspace, the test
\(S_L\), the cutoffs \(N,M\), the Tate vector, and the value
\(\rho(T)\) itself all change with \(T\). Finite dimensionality for
each \(T\) does not supply, for example,

\[
 \lim_{T_0\to\infty}\sup_{T\ge T_0}\omega_T(\rho(T))=0,
\tag{18}
\]

nor a comparison with the zero margin of the first contact. Even if
absolute smallness of the whole joint remainder were proved, a bound
\(|R_T|\le\varepsilon_T\) does not imply \(R_T\le0\). At the contact
there is no known positive gap to absorb \(\varepsilon_T\).

The special nature of the contact does supply
\(a_M(\delta,\delta)=hE_\rho(F)\ge0\) and the interior cancellations of
the weak equation. It supplies no sign for the nonlocal tests of (7),
(9) of R170_820, nor for \(a_M(\delta,\mathcal RF)\). Equality (5),
realized via functions concentrated at high frequency, proves the
absence of a universal bound tending to zero for each translation
difference; it does not refute a possible narrower law on first-contact
radicals. Such a law, however, remains unproved.

## 6. Diagnosis of step 3

The concrete remainders fall into three classes:

1. the Gamma defect has the uniform bound \(O(h)\) of (12);
2. each translation difference of the prime–collar block has norm
   exactly \(2\), although the complete sums could have cancellations;
   for fixed data, the translation differences and the dilations only
   have strong convergence here, with no additional regularity;
3. Tate and the correctors have contact-dependent bounds, but the
   corpus provides no joint uniformity in \(T\).

None of these estimates has a one-sided orientation. Since R170_820 did
not produce a sign inequality to transport, there is not yet a new
bound that could be made uniform. Global step 3 remains blocked on the
same precise obligation: proving, on the first-contact data and jointly
preserving PC, Tate, and the alignment error,

\[
 \Re e_G(z)+h^{-1}\Re a_M(\delta,\mathcal RF)\le0.
\tag{19}
\]

The bounds in this note are rigorous partial results about size and
topology. They do not prove (19), they supply no margin, and they do
not turn contact-by-contact convergence into uniformity across every
scale.
