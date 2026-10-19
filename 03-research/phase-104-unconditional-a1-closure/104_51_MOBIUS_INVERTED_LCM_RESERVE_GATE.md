# 104_51 — Möbius inversion of the `lcm` kernel and reserve gate

**Result.** The unnormalized Gram kernel associated with the two marks
of `104_50`,

\[
 K_s(d,e)=\zeta(s)\mathrm{lcm}(d,e)^{-s},
 \qquad s>1,                                               \tag{1}
\]

admits an exact Möbius inversion in both of its variables. On every finite
divisor poset, if \(Z\) is the zeta matrix, \(M=Z^{-1}\) its Möbius
matrix, and \(W\) the diagonal of the masses of the parent integers, then

\[
 \boxed{K=Z^{T}WZ,\qquad M^{T}KM=W.}                       \tag{2}
\]

Hence the inversion leaves no reserve between towers: it removes **all**
correlations between distinct primes and leaves only the diagonal energy.
Comparing the energy before and after inverting does not produce an
inequality either. The difference

\[
 \mathscr R_W(v)=\|Zv\|_W^2-\|v\|_W^2                    \tag{3}
\]

is indefinite already on the minimal tower
\(\{1,p,p^2\}\). For the von Mangoldt--Laguerre vector

\[
 v(p^k)=(\log p)L_{n-1}^{(1)}(k\log p)
\]

the **single-tower cutoff** reserve preserves phase exactly. At degree
\(n=2\), that local contribution is positive for the tower of \(2\) and
negative for the tower of \(5\). In the target range, \(n=151\), it is
positive at \(p=2\) and negative at \(p=7\). More generally, as a
continuous function of the position of a tower, it has both signs for
every \(n\ge2\).

This local statement must not be confused with the infinite zeta form: the
parents outside \(\{1,p,p^2\}\) contribute additional terms. The infinite
form is also indefinite, but requires another witness. At
\(s=2,p=2\), the abstract vector \((a,b)=(1,-1)\), supported on
\(\{2,4\}\), gives exactly \((3\zeta(2)-5)/16<0\), while
\((1,0)\) gives positive sign. Both signs of the infinite form were not
obtained here on the **fixed Laguerre vector**.

The simple inverse \(M\) does distinguish zeta from the falsifier
\(\zeta(s+c)\zeta(s-c)\): for the latter, the conditioned selector contains
cofactor coefficients and is not uniform. But the distinction does not
supply a sign, because (3) already fails for the real zeta weights. If the
diagonal is polarized to return to a linear form, one gets an unoriented
difference of two squares; if additivity is then required, Theorem
`104_53` forces a return to single-tower cumulants and to
\(B_n=A_n-\lambda_n\).

Thus the narrow mechanism

```text
two-mark Palm + double Möbius inversion
+ positivity of the resulting diagonal
=> oriented proportional reserve for the Laguerre vector.
```

is ruled out. A degree-specific non-additive inequality comparing two of
the energies **before** the congruence, failing for the shifted selector,
is not ruled out. This document does not prove

\[
 B_n\le {1501\over2002}A_n\quad(n\ge150),                 \tag{4}
\]

nor A1 nor RH.

## 0. Audit against `104_12`, `104_50`, and `104_53`

`104_50` builds the second-order Palm and writes the `lcm` kernel,
but does not invert it. `104_52` takes its connected part and proves that
pairs between distinct towers cancel. None of those results is recounted
here: incidence inversion is applied to the **uncentered** kernel and it is
decided whether its diagonal leaves an order reserve.

Congruence (2) also does not contradict Theorem 1 of `104_12`. There, a
fixed positive metric with \(M=Z^\dagger\) is ruled out. Here the inverse is
not identified with the adjoint: \(K=Z^TWZ\) is the Gram matrix created by
\(Z\), and \(M^TKM=W\) is only the inverse change of coordinates. Precisely
for that reason it does not imply \(K\succeq W\) nor \(K\preceq W\), as
Section 3 proves.

Finally, `104_53` classifies the additive recompositions after taking
moments. The new and narrow content of this document is that no automatic
reserve is left either if the connected projection is avoided first and the
full quadratic form is inverted directly.

## 1. The `lcm` kernel is a divisor Gram matrix

Let \({\cal D}\) be a finite set closed under divisors. Index rows
and columns by \({\cal D}\) and set

\[
 Z_{m,d}={\bf1}_{d\mid m},\qquad
 W=\mathrm{diag}(w_m:m\in{\cal D}),\qquad w_m>0.  \tag{5}
\]

For two functions \(a,b\) on \({\cal D}\), their divisor renewal is

\[
 (Za)(m)=\sum_{d\mid m}a(d).                              \tag{6}
\]

The two-mark quadratic form equals

\[
 \begin{aligned}
 \langle Za,Zb\rangle_W
 &=\sum_{m\in{\cal D}}w_m
       \sum_{d\mid m}\sum_{e\mid m}a(d)b(e)\\
 &=\sum_{d,e\in{\cal D}}a(d)b(e)
       \sum_{\substack{m\in{\cal D}\\[d,e]\mid m}}w_m.
                                                               \tag{7}
 \end{aligned}
\]

Then, with

\[
 K_{d,e}:=\sum_{\substack{m\in{\cal D}\\[d,e]\mid m}}w_m,
                                                               \tag{8}
\]

one has \(K=Z^TWZ\). Removing the cutoff with \(w_m=m^{-s}\),
absolute convergence gives

\[
 K_{d,e}=\sum_{[d,e]\mid m}m^{-s}
 =\zeta(s)[d,e]^{-s},                                    \tag{9}
\]

The probabilistic kernel of `104_50`, equation (14), is
\([d,e]^{-s}\); (9) is exactly \(\zeta(s)\) times that kernel because
here the sum over parents was not divided by the normalization \(\zeta(s)\).

Equivalently, if

\[
 \widehat W_s=\zeta(s)^{-1}W_s,\qquad
 \widehat K_s=\zeta(s)^{-1}K_s,
\]

then the probabilistic kernel and its congruence are

\[
 \boxed{\widehat K_s(d,e)=[d,e]^{-s},\qquad
 M^T\widehat K_sM=\widehat W_s.}                          \tag{9a}
\]

The normalization multiplies both energies simultaneously by the
positive scalar \(\zeta(s)^{-1}\), so it changes no sign.

The incidence inversion matrix is

\[
 M_{m,d}=\mu(m/d){\bf1}_{d\mid m},\qquad ZM=MZ=I.        \tag{10}
\]

Consequently

\[
 M^TKM=M^TZ^TWZM=(ZM)^TW(ZM)=W,                          \tag{11}
\]

which proves (2). The conclusion is exact: a double inversion of the kernel
cannot simultaneously leave a positive diagonal and a residual correlation
between distinct primes. The first is all that remains after canceling the
second.

## 2. Application to the unit renewal

For a test \(f\), define

\[
 v_f(d)=\Lambda(d)f(\log d),\qquad
 J_f(m)=\sum_{d\mid m}\Lambda(d)f(\log d).               \tag{12}
\]

Then \(J_f=Zv_f\), and (7)--(9) give

\[
 \sum_{m\ge1}{J_f(m)J_g(m)\over m^s}
 =\zeta(s)\sum_{d,e\ge2}{\Lambda(d)\Lambda(e)
 f(\log d)g(\log e)\over[d,e]^s}.                        \tag{13}
\]

The inversion \(v_f=MJ_f\) fully uses
\(\Lambda*1=\log\). But substituting it into (13) only recovers

\[
 \langle J_f,J_g\rangle_W
 =\langle v_f,Kv_g\rangle;
\]

no third form appears. In particular, the diagonal of (11) contains
\(\Lambda(d)^2f(\log d)g(\log d)\), whereas the functional defining
\(B_n\) is linear in \(\Lambda(d)\). To return to a linear form one must
polarize against an anchor \(u\):

\[
 4\langle v,u\rangle_W
 =\|v+u\|_W^2-\|v-u\|_W^2.                               \tag{14}
\]

Equation (14) recovers the sought orientation only as a difference of two
positive energies. The positivity of each energy does not decide the sign
of their difference.

## 3. The supposed reserve: finite cutoff and infinite kernel

Consider the divisor poset

\[
 {\cal D}=\{1,p,p^2\}
\]

and a vector \(v=(0,a,b)^T\). Then

\[
 Zv=(0,a,a+b)^T,
\]

so that, for any positive diagonal \(W\),

\[
 \boxed{
 \mathscr R_W(v)
 =w_{p^2}\{(a+b)^2-b^2\}
 =w_{p^2}(a^2+2ab).}                                     \tag{15}
\]

With \((a,b)=(1,0)\), (15) is positive; with
\((a,b)=(1,-1)\), it is negative. Hence neither \(K-W\succeq0\) nor
\(W-K\succeq0\) uniformly over finite cutoffs, even restricting to vectors
vanishing at \(1\). This is a three-point witness, independent of any
analytic estimate.

To avoid extrapolating that computation to the infinite kernel, let us
compute the latter separately. With \(v\) supported on \(p,p^2\), (1) and
the diagonal \(W_s(m,m)=m^{-s}\) give

\[
\boxed{
 \begin{aligned}
 \mathscr R_s^{\infty}(a,b)={}&
 (\zeta(s)-1)p^{-s}a^2+2\zeta(s)p^{-2s}ab\\
 &+(\zeta(s)-1)p^{-2s}b^2.
 \end{aligned}}                                           \tag{15a}
\]

At \(s=2,p=2\), \((a,b)=(1,0)\) makes (15a) positive. For
\((a,b)=(1,-1)\),

\[
 \mathscr R_2^{\infty}(1,-1)={3\zeta(2)-5\over16}<0.      \tag{15b}
\]

The inequality is elementary and does not use a decimal evaluation:

\[
 \zeta(2)<1+{1\over4}+{1\over9}+{1\over16}+{1\over25}
                  +\int_5^\infty x^{-2}\,dx
 ={5989\over3600}<{5\over3}.                              \tag{15c}
\]

Thus the infinite zeta form also lacks a universal operator ordering.
Equations (15a)--(15c) still assert nothing about the fixed Laguerre
vector.

Now use the real A1 vector,

\[
 P_n(x)=L_{n-1}^{(1)}(x),\qquad
 a=(\log p)P_n(\log p),\quad
 b=(\log p)P_n(2\log p).                                 \tag{16}
\]

The cutoff reserve of that tower is exactly

\[
 \boxed{
 w_{p^2}(\log p)^2P_n(x)
 \{P_n(x)+2P_n(2x)\},\qquad x=\log p.}                  \tag{17}
\]

No higher power has been replaced, nor has the modulus of the
Laguerre polynomial been taken. At \(n=2\), \(P_2(x)=2-x\), and (17) has
the sign of

\[
 (2-x)(6-5x).                                             \tag{18}
\]

The elementary bounds

\[
 {1\over2}<\log2<1,\qquad {3\over2}<\log5<{5\over3}    \tag{19}
\]

show that (18) is positive for \(p=2\) and negative for \(p=5\).
Inequalities (19), for instance, follow from
\(8/3<e<11/4\), certified directly by the series for \(e\).

The local obstruction reaches directly into the target range.
The checker brackets \(\log2\) and \(\log7=3\log2-\log(8/7)\) via the
rational series for \(\mathrm{atanh}\,\), and evaluates \(P_{151}\) by
interval Horner with `Fraction`. It certifies

\[
\begin{array}{c|c|c}
p&P_{151}(\log p)\{P_{151}(\log p)+2P_{151}(2\log p)\}
&\text{sign}\\ \hline
2&[9.59561939937104,\,9.59561939937106]&+\\
7&[-6.33518557015695,\,-6.33518557015693]&-
\end{array}                                                \tag{20}
\]

The decimals in (20) are only a presentation of rational intervals:
the checker's assertions are \(q_{\rm low}>0\) and \(q_{\rm high}<0\).
Thus the **local cutoff reserve** fails in both directions on the
fixed real vector for \(n=151\), without altering
\(\Lambda(p^k)=\log p\). It does not follow from (20) that the full
infinite form has those signs on the same vector; that claim is withdrawn.

The sign change is not special to degree two. Let \(r_n\) be the largest
zero of \(P_n\), which is simple. For \(x<r_n\) sufficiently close to
\(r_n\), \(P_n(x)\) has sign opposite to the leading coefficient, while
\(P_n(2x)\) has the sign of the leading coefficient. Thus (17), as a
function of a continuous tower position, is negative. For \(x>r_n\)
sufficiently large, both \(P_n(x)\) and \(P_n(2x)\), and hence also
\(P_n(x)+2P_n(2x)\), have the sign of the leading coefficient; (17) is
positive. This proves both signs of the exact geometry for every
\(n\ge2\). The witness with
real primes in (19) suffices to rule out a universal operator ordering;
it does not claim to rule out a still-unknown special inequality only for
degrees \(n\ge150\).

## 4. The pole is diagonalized the same way

The continuous comparator of (9) is the Volterra operator

\[
 (Vh)(x)=\int_0^xh(y)\,dy
\]

on \(L^2(e^{-\varepsilon x}dx)\). Its Gram kernel is

\[
 K_0(y,z)=\int_{\max(y,z)}^\infty e^{-\varepsilon x}dx
 ={e^{-\varepsilon\max(y,z)}\over\varepsilon}.           \tag{21}
\]

The derivative is the inverse of \(V\) on its natural domain, and hence
diagonalizes (21) in exactly the same way that Möbius diagonalizes (9).
Subtracting the two channels after inverting produces a difference of
diagonal energies, not a joint positive energy. The Gamma channel of A1 is
another explicit diagonal, but (2) gives no comparison between those three
diagonals.

This localizes the failure without separating the pole in the original
identity: the inversion is compatible with both channels, but does not
orient their difference. A bound directly comparing those diagonals on
\(P_n\) would be an additional theorem, not a consequence of Möbius
incidence.

## 5. Shifted falsifier and closure trichotomy

For

\[
 Z_c(s)=\zeta(s+c)\zeta(s-c)
\]

the renewal conditioned on \(p^a\) is, with the notation of `104_49`,

\[
 \pi_{a,c}(k)
 ={(r^k+r^{-k})b_{a-k}(r)\over a b_a(r)},
 \qquad r=p^c.                                            \tag{22}
\]

At \(a=2\),

\[
 \pi_{2,c}(1)={1\over2}+{1\over2b_2(r)},\qquad
 \pi_{2,c}(2)={1\over2}-{1\over2b_2(r)}.                \tag{23}
\]

Thus the shifted conditioned renewal matrix is not the unit incidence
matrix \(Z\), and the simple inverse
\(M\) of (10) does not undo it. Congruence (2) uses a real property that
the falsifier does not have. However, it does not prove the margin: the
proposed reserve is indefinite as an operator ordering both on finite
cutoffs, by (15), and for the infinite zeta kernel, by (15a)--(15c). The
fixed test (20) refutes only the local tower version.

After the inversion only three options remain:

1. keep the quadratic diagonal: linear orientation is lost;
2. polarize it: one obtains the unoriented difference (14);
3. recompose an additive observable: by `104_53`, one returns to a
   combination of single-tower cumulants and, for Laguerre, to
   \(\mathcal B_{n,s}\to B_n\).

None of the three options supplies the reserve
\((1501/2002)A_n-B_n\). The only successor compatible with this gate is a
non-additive inequality, depending on the vector \(P_n\), applied
**before** the congruence and with an explicit term dominating the
Euler--pole--Gamma channel. No such inequality is constructed here.

## 6. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 mobius_inverted_lcm_reserve_gate_check.py
```

The checker uses only integers and `Fraction`. It verifies the Gram
factorization, the double inversion with and without normalization, the
two signs of the reserve on the minimal tower, the infinite witness
(15b)--(15c), the rational Laguerre witnesses at \(n=2\) and \(n=151\), and
the rational non-uniformity of the shifted selector.
