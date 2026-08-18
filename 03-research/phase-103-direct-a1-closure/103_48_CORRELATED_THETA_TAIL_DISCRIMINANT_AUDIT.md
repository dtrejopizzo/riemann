# Correlated theta-tail expansion for the cubic discriminant

## Verdict

103_47 separated the theta moments into the first mode and a strictly
decreasing relative tail. This note keeps the four tail errors *without*
replacing them by their maximum. It obtains an exact correlated
homogeneous four-moment expansion of the cubic discriminant and hence an exact
first-mode-versus-tail test.

The natural hope that the signs of the theta tail—positive and monotone
decreasing likelihood ratio—would make the perturbation favourable is
false. An exact two-atom counterexample has a decreasing relative tail
bounded by \(1/300\), a strictly positive base cubic discriminant, and a
negative perturbed discriminant. Thus no determinantal or fourfold-integral
proof using only that order information can close the theta gate.

The actual theta translations retain more analytic structure than the
counterexample, and the correlated identity below is the legitimate next
quantitative target. It does not prove PF\(_3\), A1, or RH.

## 1. Four exact correlated theta tail errors

Keep the notation of 103_47:
\[
 b_N={A_{2N}\over(2N)!},\qquad
 {c_N\over2}=b_N(1+\epsilon_{2N}),\qquad
 A_p=\int_0^\infty u^pf_1(u)\,du.                              \tag{1}
\]
For a fixed cubic shift \(N\), abbreviate
\[
 \eta_j=\epsilon_{2N+2j},\qquad S_j=1+\eta_j\qquad(0\le j\le3).
                                                                    \tag{2}
\]
The translate formula of 103_47 makes every error fully explicit:
\[
 \boxed{\quad
 \eta_j={1\over A_{2N+2j}}
 \sum_{m\ge2}m^{-1/2}
 \int_{\log m}^{\infty}(v-\log m)^{2N+2j}f_1(v)\,dv.
 \quad}                                                        \tag{3}
\]
In particular these are not four independently enclosed numerical
remainders. They arise from one function
\[
 R(u)=\sum_{m\ge2}{f_m(u)\over f_1(u)}.                         \tag{4}
\]

For reference, their consecutive gaps have the positive two-copy
representation
\[
\begin{aligned}
 \epsilon_p-\epsilon_{p+1}
 ={}&{1\over2A_pA_{p+1}}
 \sum_{m\ge2}\iint_{(0,\infty)^2}
 u^pv^p(u-v)\\[3pt]
 &\hspace{17mm}\cdot\bigl(r_m(v)-r_m(u)\bigr)
 f_1(u)f_1(v)\,du\,dv>0.                                      \tag{5}
\end{aligned}
\]
Here \(r_m=f_m/f_1\). Formula (5) follows by substituting the theta sum in
the covariance identity of 103_47; it is legitimate termwise by positive
monotone convergence. Its integrand is nonnegative because every
\(r_m\) is strictly decreasing. Thus
\[
 1<S_3<S_2<S_1<S_0<1+{1\over300}.                              \tag{6}
\]
This is the available correlation from the exact theta translates.

## 2. Exact discriminant expansion, with no independent intervals

For brevity put
\[
\begin{array}{lll}
 P=3b_{N+1}^2b_{N+2}^2,&
 H=6b_Nb_{N+1}b_{N+2}b_{N+3},\\
 U=4b_{N+1}^3b_{N+3},&
 V=4b_Nb_{N+2}^3,&
 W=b_N^2b_{N+3}^2.
\end{array}                                                     \tag{7}
\]
All five quantities are positive. Direct substitution in the exact
discriminant formula of 103_36 gives
\[
\begin{aligned}
 {\Delta_N(\widehat c)\over27}
 ={}&P S_1^2S_2^2+H S_0S_1S_2S_3\\[3pt]
 &-U S_1^3S_3-V S_0S_2^3-W S_0^2S_3^2,                         \tag{8}
\end{aligned}
\]
where \(\widehat c_j=c_j/2\). This is the desired correlated
four-factor expansion: each occurrence of a moment carries its own
correlated theta-tail multiplier.

Let
\[
 \mathscr D_N=P+H-U-V-W                                        \tag{9}
\]
be the first-mode discriminant divided by \(27\), and define the exact
positive and negative tail increments
\[
\begin{aligned}
 E_N^+={}&P(S_1^2S_2^2-1)+H(S_0S_1S_2S_3-1),\\
 E_N^-={}&U(S_1^3S_3-1)+V(S_0S_2^3-1)+W(S_0^2S_3^2-1).
                                                                    \tag{10}
\end{aligned}
\]
Then (8) is exactly
\[
 \boxed{\quad {\Delta_N(\widehat c)\over27}
 =\mathscr D_N+E_N^+-E_N^-.\quad}                              \tag{11}
\]
Since \(\Delta_N(c)=16\Delta_N(\widehat c)\), the actual theta cubic is
hyperbolic at this shift if and only if
\[
 \boxed{\qquad \mathscr D_N+E_N^+>E_N^-.\qquad}                 \tag{12}
\]

This is sharper than the bound in 103_47: it retains the favourable
increments \(E_N^+\) and every distinct translate error in (3). It is also
an exact comparison of the first-mode margin and the theta-tail
perturbation, rather than a Gaussian error budget for four unrelated
moments. No sign for \(E_N^+-E_N^-\) has been assumed.

## 3. Why decreasing likelihood ratio cannot fix the sign

One might try to derive a sign for \(E_N^+-E_N^-\) from (5), or from a
putative nonnegative fourfold determinant kernel. The following rational
example rules this out even with a uniformly tiny decreasing tail.

Let
\[
 \nu_w=w\delta_{1/2}+(1-w)\delta_{3/2},
 \qquad w={94591\over100000}.                                  \tag{13}
\]
For the central coefficients
\(c_j=\int u^{2j}\,d\nu_w(u)/(2j)!\), direct rational substitution in the
discriminant gives
\[
 \Delta(\nu_w)=
 {492605648663257\over96000000000000000000000}>0.              \tag{14}
\]
Add the positive tail measure
\[
 \tau={1\over5408}\delta_{1/2}.                                \tag{15}
\]
Relative to \(\nu_w\), its likelihood ratio is
\[
 {d\tau\over d\nu_w}(1/2)
 ={3125\over15985879}<{1\over300},
 \qquad
 {d\tau\over d\nu_w}(3/2)=0,                                  \tag{16}
\]
so it is nonnegative, bounded by the same rational constant as the theta
tail in 103_47, and decreasing on the ordered support.

After normalization, \(\nu_w+\tau\) is
\[
 {\nu_w+\tau\over1+1/5408}
 ={2956\over3125}\delta_{1/2}
  +{169\over3125}\delta_{3/2}.                                 \tag{17}
\]
Its discriminant is nevertheless
\[
 \Delta\!\left({\nu_w+\tau\over1+1/5408}\right)
 =-{8000158285741\over750000000000000000000}<0.                \tag{18}
\]
The base and tail are each individually PF\(_3\) at this shift: (14)
handles the base, while a point mass at \(a\) has discriminant
\(127a^{12}/9600>0\), as checked in 103_47. The failure is therefore
not caused by a negative component or by a large likelihood-ratio error.

Consequently, the facts
\[
 R\ge0,\qquad R\ \hbox{decreasing},\qquad \|R\|_\infty<1/300
                                                                    \tag{19}
\]
do not determine the sign of the correlated correction in (11). In
particular, a nonnegative determinant/Vandermonde representation for the
cubic discriminant cannot follow merely from (19): it would contradict
the exact moment calculation (14)--(18). This is a no-go for the proposed
order-only route, not for the particular analytic theta translations.

## 4. The remaining theta-specific comparison

Equations (3), (5), and (11) reduce the unresolved task to a concrete
one-mode calculation:

1. establish a lower bound for \(\mathscr D_N\) for the density \(f_1\);
2. estimate the four *correlated* quantities in (3), or directly the
   signed combination \(E_N^+-E_N^-\), at a precision below that margin.

The first item cannot be replaced by log-concavity: 103_36 and 103_39
already isolate the missing third-order information. The second cannot be
replaced by the order properties in (19), by Section 3. What remains
genuinely theta-specific is the explicit translated form
\(m^{-1/2}f_1(u+\log m)\) inside (3) and (5). A successful continuation
would need to exploit its exponential \(m^2\)-suppression at the common
moment saddle, with a correlated expansion accurate at the cubic scale
identified in 103_40.

No RH assumption entered this audit. Conversely, no all-shift PF\(_3\)
statement, and no conclusion about A1 or RH, follows from the identities
above without those missing quantitative estimates.
