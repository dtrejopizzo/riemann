# A1 regulator-flow budget: exact pole--prime cancellation and split loss

## Result

The flow is expanded below with the pole and prime terms kept paired.
No proof of A1 or RH is claimed.

For every \(a>1\),
\[
 D_{n+1}(a)-D_n(a)
 =I_n^{\rm pp}(a)+I_n^\Gamma(a),                                \tag{1}
\]
where the pole--prime block is
\[
 \boxed{\quad
 I_n^{\rm pp}(a)
 ={2(-1)^n a\over(a-1)^{n+1}}
 -2a\sum_{m\ge2}{\Lambda(m)\over m^a}
 L_n(a\log m).
 \quad}                                                         \tag{2}
\]
The two terms in (2) must remain paired. Separating them makes the
positive-part budget infinite for every odd \(n\); even after excising
\((1,1+1/n)\), the positive pole budget for even \(n\) is
\(\asymp n^n\). In contrast, the completed high-regulator value at
\(A_n=n\) has the elementary bound \(O(n^3 9^n)\). Thus a termwise
positive-part proof cannot be compared with the high-\(a\) reserve.

The surviving route is a two-region, sign/saddle partition which keeps
\(I_n^{\rm pp}\) intact near \(a=1\), and uses the absolutely convergent
Laguerre sum only away from that endpoint.

## 1. The uniform target remains RH-strength

Put
\[
 D_n(a)=n[z^n]\log {Y(a/(1-z))\over Y(a)},\qquad
 Y(s)={\xi(s)^2\over s\pi^{-s/2}\Gamma(s/2)}.                  \tag{3}
\]
Then \(D_n(1)=D_n\), and 103_49 proves
\[
 D_n=D_n(A)-n\int_1^A{D_{n+1}(a)-D_n(a)\over a}\,da.             \tag{4}
\]
The sufficient positive-part budget is
\[
 D_n(A)>n\int_1^A{(D_{n+1}(a)-D_n(a))_+\over a}\,da.             \tag{5}
\]
If (5) held for every \(n\), then \(D_n\ge0\) for every \(n\).
The established positivity of \(\lambda_n^{\rm arch}\) for \(n\ge8\)
would give \(\lambda_n\ge\lambda_n^{\rm arch}/2>0\) there, and the finite
certificate completes Li positivity. Therefore a uniform proof of (5)
would prove RH. The analysis below is conducted on \(a>1\), with no
assumption about zeros.

## 2. Exact normal expansion of the flow increment

Write
\[
 L(s)={Y'(s)\over Y(s)}
 ={1\over s}+{2\over s-1}-{\log\pi\over2}
 +{1\over2}\psi(s/2)+2{\zeta'\over\zeta}(s).                    \tag{6}
\]
For \(a>1\), the prime series and each of its fixed derivatives converge
absolutely and locally uniformly:
\[
 {\zeta'\over\zeta}(a)
 =-\sum_{m\ge2}\Lambda(m)m^{-a},\qquad
 {d^j\over da^j}{\zeta'\over\zeta}(a)
 =(-1)^{j+1}\sum_{m\ge2}\Lambda(m)(\log m)^j m^{-a}.             \tag{7}
\]
Indeed, on \(a\ge1+\delta\) the terms are dominated by
\(\Lambda(m)(\log m)^j m^{-1-\delta}\), a convergent series. This proves
all coefficient and derivative interchanges below on compact subsets of
\((1,\infty)\).

The prime contribution to \(D_n(a)\), by the Laguerre generating identity,
is
\[
 P_n(a)=-2a\sum_{m\ge2}{\Lambda(m)\over m^a}
 L_{n-1}^{(1)}(a\log m).                                       \tag{8}
\]
The elementary identity
\[
 L_n^{(1)}(x)-L_{n-1}^{(1)}(x)=L_n(x)                           \tag{9}
\]
therefore gives
\[
 P_{n+1}(a)-P_n(a)
 =-2a\sum_{m\ge2}{\Lambda(m)\over m^a}L_n(a\log m).              \tag{10}
\]

The pole factor is \(2\log(s-1)\). Since
\[
 s-1={a-1+z\over1-z},
\]
its exact coefficient is
\[
 R_n(a)=2\left[1+{(-1)^{n+1}\over(a-1)^n}\right].               \tag{11}
\]
Consequently
\[
 R_{n+1}(a)-R_n(a)
 ={2(-1)^n a\over(a-1)^{n+1}},                                  \tag{12}
\]
which proves (2).

The remaining Gamma block is completely explicit. Put
\[
 G(s)={1\over s}-{\log\pi\over2}+{1\over2}\psi(s/2),             \tag{13}
\]
\[
 \Gamma_n(a)
 =n\sum_{k=1}^n{a^k\over k!}{n-1\choose k-1}G^{(k-1)}(a).
                                                                    \tag{14}
\]
Then
\[
 I_n^\Gamma(a)=\Gamma_{n+1}(a)-\Gamma_n(a),                    \tag{15}
\]
and (1) follows. Equations (2), (14), and (15) are an exact
prime--pole--Gamma expansion of the scalar flow increment.

## 3. Endpoint cancellation is compulsory

Let
\[
 F(a)=-{\zeta'\over\zeta}(a)
 =\sum_{m\ge2}\Lambda(m)m^{-a}.                                 \tag{16}
\]
The pole of zeta gives the local Laurent expansion
\[
 F(1+t)={1\over t}+O(1)\qquad(t\downarrow0).                    \tag{17}
\]
Using
\[
 L_n(x)=\sum_{k=0}^n(-1)^k{n\choose k}{x^k\over k!},             \tag{18}
\]
termwise differentiation in (16) gives
\[
 \sum_{m\ge2}\Lambda(m)m^{-a}L_n(a\log m)
 =\sum_{k=0}^n{n\choose k}{a^k\over k!}F^{(k)}(a)
 =(-1)^n t^{-n-1}+O_n(t^{-n}).                                  \tag{19}
\]
Thus the prime increment alone satisfies
\[
 P_{n+1}(1+t)-P_n(1+t)
 =2(-1)^{n+1}t^{-n-1}+O_n(t^{-n}).                               \tag{20}
\]
For odd \(n\), the right side is positive near \(t=0\). The termwise
prime positive part consequently obeys
\[
\begin{aligned}
 n\int_1^A {1\over a}
 \left(\sum_{m\ge2}
 \left[-2a\Lambda(m)m^{-a}L_n(a\log m)\right]_+\right)da
 &\ge n\int_1^A{(P_{n+1}-P_n)_+\over a}\,da\\
 &=+\infty                                                       \tag{21}
\end{aligned}
\]
for every \(A>1\) and every odd \(n\).

This divergence is spurious: (12) has the opposite leading Laurent term,
and
\[
 {2\over s-1}+2{\zeta'\over\zeta}(s)
\]
is analytic at \(s=1\). Hence the full block \(I_n^{\rm pp}\) is regular
there. Formula (21) proves that the cancellation must occur before a
positive part or an absolute value is taken.

## 4. Quantitative loss for \(A_n=n\)

The preceding obstruction is not limited to the literal endpoint. Take an
even \(n\) and excise the interval \((1,1+1/n)\). The positive pole term
alone contributes, on the first remaining interval,
\[
\begin{aligned}
 n\int_{1+1/n}^{1+2/n}
 {1\over a}\,{2a\over(a-1)^{n+1}}\,da
 &=2n\int_{1/n}^{2/n}t^{-n-1}\,dt\\
 &=2n^n(1-2^{-n}).                                               \tag{22}
\end{aligned}
\]
This is the exact split cost before any prime or Gamma term is bounded.

For comparison, the completed value at \(A_n=n\) grows at most
exponentially in \(n\). A deliberately coarse elementary estimate is
\[
 \boxed{\qquad |D_n(n)|\le C n^3 9^n\qquad(n\ge8),\qquad}        \tag{23}
\]
with an absolute constant \(C\).

Here is a self-contained derivation of the scale in (23). From the
polygamma series, the rational terms in (6), and (7), comparison of the
prime sum with its integral gives, for \(1\le j\le n-1\),
\[
 |L^{(j)}(n)|\le C_0n\,j!\left({8\over n}\right)^j,\qquad
 |L(n)|\le C_0\log n.                                           \tag{24}
\]
For the prime part, use \(\Lambda(m)\le\log m\) and
\[
 \int_1^\infty(\log x)^{j+1}x^{-n}\,dx
 ={(j+1)!\over(n-1)^{j+2}},                                    \tag{25}
\]
while unimodality bounds the discrete sum by this integral plus twice its
maximum. For \(k=j+1\le n\), the elementary inequality
\(k!\ge(k/e)^k\) shows that this maximum is at most \(n\) times (25).
After enlarging \(C_0\), (24) follows with the rounded constant \(8\).
Insert (24) in the exact formula
\[
 D_n(n)=n\sum_{k=1}^n{n^k\over k!}{n-1\choose k-1}L^{(k-1)}(n)
                                                                    \tag{26}
\]
to obtain
\[
 |D_n(n)|
 \le C_0n^2\log n+
 C_0n^3\sum_{k=2}^n{8^{k-1}\over k}{n-1\choose k-1}
 \le Cn^3 9^n.                                                   \tag{27}
\]

Since \(n^n/(n^3 9^n)\to\infty\), (22) eventually exceeds not merely the
actual high-\(a\) reserve but the absolute upper bound (23) for that
reserve. Thus the split pole estimate cannot prove the flow inequality at
\(A_n=n\). Together with (21), it eliminates the termwise positive-part
route for all parities.

## 5. The surviving sign/saddle partition

The only legitimate partition retains the completed pole--prime block:

1. On \(1<a\le1+\delta_n\), estimate \(I_n^{\rm pp}(a)\) as one analytic
   function, using the cancellation in (17)--(20); do not insert the
   Dirichlet series into a positive part there.
2. On \(a\ge1+\delta_n\), the prime series in (2) is normally convergent.
   Only in this outer region may one split it according to the actual sign
   of \(L_n(a\log m)\). Its positive contribution is supported on
   \(L_n(a\log m)<0\), the natural Laguerre saddle/lobe partition.
3. The Gamma increment (15) remains paired with the resulting outer block
   until after the scalar positive part in (5) is formed.

This formulation preserves the exact completed cancellation and turns the
remaining task into a correlated saddle estimate, rather than an absolute
prime sum. It is consistent with the cubic-scale warning in 103_40:
independent envelopes erase the cancellation that the target requires.

No estimate completing this sign/saddle partition is contained here. The
document establishes only the exact expansion, the mandatory cancellation,
and the \(n^n\) scaling obstruction to the naive budget.
