# Completed endpoint matching for the A1 regulator flow

## Verdict

This note fixes an explicit endpoint window and derives a Taylor--saddle
matching inequality that retains the completed pole--prime cancellation.
It does not prove the inequality uniformly and therefore does not prove
the strong margin, A1, or RH.

## 1. A shrinking endpoint window is incompatible with a split exterior

Let \(t=a-1\). The pole contribution to the flow increment, from 103_53,
is
\[
 I_n^{\rm pole}(1+t)=2(-1)^n(1+t)t^{-n-1}.                      \tag{1}
\]
If the exterior estimate takes a positive part after separating this term,
then for even \(n\) it pays at least
\[
 n\int_{1+\delta_n}^{1+2\delta_n}
 {I_n^{\rm pole}(a)\over a}\,da
 =2\delta_n^{-n}(1-2^{-n}).                                    \tag{2}
\]
The completed high-regulator estimate of 103_53 is
\[
 |D_n(n)|\le Cn^3 9^n.                                         \tag{3}
\]
Hence any split exterior budget comparable with (3) must satisfy
\[
 \delta_n^{-n}\ll n^3 9^n,\qquad
 \liminf_{n\to\infty}\delta_n\ge {1\over9}.                     \tag{4}
\]
In particular, the seemingly natural choices
\(\delta_n=n^{-1}\), \(n^{-1/2}\), or \(e^{-\sqrt{\log n}}\) are
inviable for every method that splits the pole before the positive part:
their cost in (2) is respectively \(n^n\),
\(n^{n/2}\), and \(e^{n\sqrt{\log n}}\).

This does not disprove a completed estimate, because the prime term cancels
(1) before a positive part is taken. It does prove that a matching scheme
must either retain that cancellation in the exterior or use a
non-shrinking endpoint window. We choose explicitly
\[
 \boxed{\qquad \delta={1\over8}.\qquad}                         \tag{5}
\]
This value is not asserted optimal; it is safely above the scale \(1/9\)
forced by the crude comparison (4).

## 2. The normalized Stieltjes Taylor block

Put
\[
 h(t)=\log\bigl(t\zeta(1+t)\bigr)
 =\sum_{r\ge1}p_rt^r.                                           \tag{6}
\]
The singularity at \(t=0\) is removable. The coefficients \(p_r\) are
obtained exactly from the normalized Stieltjes recursion of 103_52:
\[
 t\zeta(1+t)=1+\sum_{r\ge1}
 {(-1)^{r-1}\gamma_{r-1}\over(r-1)!}t^r,\qquad
 p_r=q_r-{1\over r}\sum_{k=1}^{r-1}kp_kq_{r-k}.                 \tag{7}
\]

The completed pole--prime contribution to the regulator generating
function is, exactly,
\[
 \mathcal F_{\rm pp}(1+t,z)
 =2\left[
 h\!\left(t+{(1+t)z\over1-z}\right)-h(t)\right].               \tag{8}
\]
Consequently its coefficient of index \(n\) is
\[
\begin{aligned}
 E_n(t):=D_n^{\rm pp}(1+t)
 ={}&2n\sum_{k=1}^n{(1+t)^k\over k!}
 {n-1\choose k-1}h^{(k)}(t)\\
 ={}&2n\sum_{k=1}^n{n-1\choose k-1}(1+t)^k
 \sum_{r\ge0}{r+k\choose k}p_{r+k}t^r.                         \tag{9}
\end{aligned}
\]
The second equality is an identity of Taylor series at zero. It is not a
prime rearrangement; its finite coefficient data are the normalized
Stieltjes data in (7).

The pole--prime flow increment is therefore
\[
 I_n^{\rm pp}(1+t)={1+t\over n}E_n'(t).                         \tag{10}
\]
If \(E_n(t)=\sum_{r\ge0}e_{n,r}t^r\), then the Taylor coefficients of
(10) are explicitly
\[
 \iota^{\rm pp}_{n,0}={e_{n,1}\over n},\qquad
 \iota^{\rm pp}_{n,r}={(r+1)e_{n,r+1}+re_{n,r}\over n}
 \quad(r\ge1).                                                   \tag{11}
\]
Thus every finite Taylor jet of the endpoint block is a finite rational
polynomial in \(\gamma_0,\ldots,\gamma_{n+J}\), with no divergent prime
sum.

Let \(I_n^\Gamma(1+t)\) be the Gamma increment from 103_53, equation
(15), and put
\[
 I_n(1+t)=I_n^{\rm pp}(1+t)+I_n^\Gamma(1+t)
 =\sum_{r\ge0}\iota_{n,r}t^r.                                  \tag{12}
\]
The coefficients in (12) are defined by (11) plus the corresponding
polygamma derivatives. This is the completed Taylor block: the pole and
prime terms have already cancelled before \(\iota_{n,r}\) is formed.

## 3. An explicit endpoint--outer matching inequality

For an integer \(J\ge1\), Taylor's formula on the real interval
\([0,\delta]\) gives
\[
 I_n(1+t)=\sum_{r=0}^{J-1}\iota_{n,r}t^r+\mathcal R_{n,J}(t),
\]
\[
 |\mathcal R_{n,J}(t)|
 \le {t^J\over J!}M_{n,J}(\delta),\qquad
 M_{n,J}(\delta)=\sup_{0\le v\le\delta}
 \left|{d^J\over dv^J}I_n(1+v)\right|.                         \tag{13}
\]
This is a real Taylor remainder; it requires no unproved complex
zero-free disk around \(s=1\).

Define the inner positive-part cost by
\[
 B_n^{\rm in}(J,\delta)
 =n\sum_{r=0}^{J-1}{|\iota_{n,r}|\delta^{r+1}\over r+1}
 +{n\delta^{J+1}\over(J+1)!}M_{n,J}(\delta).                    \tag{14}
\]
Then
\[
 n\int_1^{1+\delta}{(D_{n+1}(a)-D_n(a))_+\over a}\,da
 \le B_n^{\rm in}(J,\delta).                                   \tag{15}
\]
All data in the finite sum in (14) are the normalized Stieltjes and
polygamma data specified in (7)--(12). The only non-finite input is the
explicit real derivative supremum \(M_{n,J}(\delta)\).

For the exterior, let
\[
 0=\alpha_{n,0}<\alpha_{n,1}<\cdots<\alpha_{n,n}
\]
be the zeros of \(L_n\), and put \(\alpha_{n,n+1}=\infty\). On
\(a\ge1+\delta\), define the absolutely convergent lobe sums
\[
 S_{n,j}(a)=
 \sum_{\substack{m\ge2\\
 \alpha_{n,j}<a\log m<\alpha_{n,j+1}}}
 {\Lambda(m)\over m^a}L_n(a\log m)
 \qquad(0\le j\le n).                                           \tag{16}
\]
The sign of every summand in a fixed lobe is fixed, but the positive part
must still be taken only after the lobe sums, the pole, and Gamma are
recombined. Accordingly set
\[
\begin{aligned}
 B_n^{\rm out}(\delta,A)
 =n\int_{1+\delta}^{A}{1\over a}
 \Bigg[
 I_n^\Gamma(a)+{2(-1)^na\over(a-1)^{n+1}}
 -2a\sum_{j=0}^nS_{n,j}(a)
 \Bigg]_+da.                                                     \tag{17}
\end{aligned}
\]
Normal convergence from 103_53 justifies (16), its finite lobe
partition, and the integral in (17) on every compact
\([1+\delta,A]\).

Combining (5), (15), and (17) gives the promised matching criterion:
\[
 \boxed{\quad
 D_n(A)>B_n^{\rm in}(J,\delta)+B_n^{\rm out}(\delta,A)
 \quad\Longrightarrow\quad D_n>0.
 \quad}                                                         \tag{18}
\]
With the explicit choice \(\delta=1/8\) and \(A=n\), (18) is a
completed endpoint--saddle inequality: the endpoint is expressed in
normalized Stieltjes data, while the exterior is expressed in actual
Laguerre sign lobes.

## 4. What the matching inequality does and does not close

The scale check has two concrete consequences.

1. A shrinking window can be used only if the *completed* outer block in
   (17) is estimated without splitting its pole. Equation (2) falsifies
   every outer method that tries to pay for the pole separately.
2. The fixed choice \(\delta=1/8\) avoids that immediate
   \(\delta_n^{-n}\) obstruction, but it transfers a real all-order task
   to (14). From (9)--(11), the coefficient
   \(\iota_{n,r}\) already uses normalized Stieltjes data through order
   \(n+r+1\). The remainder \(M_{n,J}(1/8)\) requires the corresponding
   derivative control on the whole interval.

Thus no fixed finite Stieltjes certificate can prove (18) for unbounded
\(n\). The finite eta/Stieltjes machinery of 103_51 can evaluate the
endpoint block over a prescribed finite range, but a uniform proof needs
an all-order bound on the completed function \(h\), not signs of isolated
Stieltjes constants.

This is not merely another cancellation restatement. Equations
(14), (17), and (18) specify the exact quantities that must match:
\[
 \underbrace{B_n^{\rm in}(J,1/8)}_{\text{completed Stieltjes jet}}
 +\underbrace{B_n^{\rm out}(1/8,n)}_{\text{completed Laguerre lobes}}
 <\underbrace{D_n(n)}_{\text{high-regulator reserve}}.          \tag{19}
\]

Every object in (19) is defined without a zero-location assumption.
Proving (19) uniformly would, by the implication in Section 1, prove RH;
the present work supplies the completed matching formulation and rules out
the shrinking-window split alternatives, but does not establish (19).
