# First-difference A1 gate: finite certificate, Abel identity, and VK scale no-go

## Verdict

The surviving elementary discrete induction is

\[
 \Delta D_n\ge0,\qquad D_n=2\lambda_n-\lambda_n^{\rm arch}.
\tag{1}
\]

It is rigorously true on the currently certified finite range:

\[
 \boxed{\quad \Delta D_n>0\qquad(1\le n\le148).\quad}
\tag{2}
\]

The proof uses interval subtraction in the safe direction (lower endpoint
at \(n+1\) minus upper endpoint at \(n\)); it does not subtract rounded
central values.  This finite fact does not establish eventual monotonicity.

There is an exact completed Abel formula for (1).  It retains the pole and
prime powers in one limiting expression.  An absolute application of a
Vinogradov--Korobov (VK) envelope to that formula has the wrong scale: its
Laguerre load is at least \(\exp((2/3+o(1))n\log n)\), while the available
right-hand barrier is only \(\frac14\log n+O(1)\).  This is a rigorous
no-go for the *absolute VK/Abel estimate*, not a statement that the actual
prime-power correlation has that size.  The remaining requirement is a
signed pole--prime cancellation theorem for the actual weights.

No uniform first-difference theorem, A1 proof, or RH proof is claimed.

## 1. Interval certificate for every available first difference

Put

\[
 M_n:=\lambda_n^{\rm prime}+\frac12\lambda_n^{\rm arch}=\frac{D_n}{2}.
\tag{3}
\]

It is enough to show \(M_{n+1}-M_n>0\).  If
\(M_n\in[L_n,U_n]\), the only safe interval decision is

\[
 M_{n+1}-M_n\ge L_{n+1}-U_n.
\tag{4}
\]

### 1.1 Indices \(1\le n\le20\)

For \(1\le n\le8\), the rational verifier of `217` was evaluated on the
margin (3), not merely on \(\lambda_n\).  For \(9\le n\le20\), the
fixed-point verifier `tools/fixed_margin_9_20.py` was evaluated at its native
scale \(10^{70}\).  Direct endpoint subtraction in those native intervals
gives

\[
 \min_{1\le n\le19}\bigl(L_{n+1}-U_n\bigr)
 >0.1410265624181258952,
\tag{5}
\]

the minimum occurring at \(n=5\).  Thus \(\Delta D_n>0\) for
\(1\le n\le19\).

The cross-certificate subtraction is also positive:

\[
 M_{21}-M_{20}
 >5.128680391459-4.7199648424461037847
 >0.4087155490128962.
\tag{6}
\]

The lower endpoint at 21 is from the independent eta/Hasse certificate;
the upper endpoint at 20 is the unrounded fixed-point endpoint.  Hence no
common floating-point representation is used in (6).

### 1.2 Indices \(21\le n\le149\)

Run

```bash
python3 tools/fixed_margin_eta_21_149.py --top 149 --first 21 --K 850 --terms 820
```

from the phase-103 directory.  This is the K850 outward certificate of
`103_51`.  Its printed integers \(\ell_n,u_n\) are, respectively, the
lower and upper decimal floors at scale \(10^{-12}\).  Therefore they
certify

\[
 {\ell_n\over10^{12}}\le M_n\le {u_n+1\over10^{12}}.
\tag{7}
\]

For all 128 adjacent pairs in this run, \(21\le n\le148\), the integer
test

\[
 g_n:=\ell_{n+1}-(u_n+1)>0
\tag{8}
\]

passes.  Its smallest certified value is

\[
 \min_{21\le n\le148}g_n=428815655222
 \quad\text{at }n=21.
\tag{9}
\]

Thus \(M_{n+1}-M_n>0.428815655222\) for every pair in that range.  As a
spot check at the curvature counterexample of `103_55`, (8) gives

\[
\begin{aligned}
10^{12}\Delta M_{147}&\ge817636096305,\\
10^{12}\Delta M_{148}&\ge817575900981.
\end{aligned}
\tag{10}
\]

Combining (5)--(10) proves (2).  Notice the compatible facts
\(\Delta D_{147}>0\) and \(\Delta^2D_{147}<0\): the first-difference
gate correctly permits decreasing positive slopes.

## 2. Exact first-difference Abel identity

The correct regulator is the paired one from `103_54`:

\[
 f_\varepsilon(t)=\log\bigl((t+\varepsilon)\zeta(1+\varepsilon+t)\bigr),
 \qquad t={z\over1-z}.
\tag{11}
\]

Write \(P_n(\varepsilon)=n[z^n]f_\varepsilon(z/(1-z))\).  The local
analytic limit is \(P_n(\varepsilon)\to\lambda_n^{\rm prime}\).  With
\(E(u)=\psi(e^u)-e^u\), the exact Stieltjes identity is

\[
 f_\varepsilon'(t)=-1-(1+\varepsilon+t)
 \int_0^\infty E(u)e^{-(1+\varepsilon+t)u}\,du.
\tag{12}
\]

Taking the discrete difference after coefficient extraction gives, for
every \(\varepsilon>0\),

\[
 \boxed{\quad
 \Delta P_n(\varepsilon)=-1-\mathcal I_{n,\varepsilon}^{(1)},
 \quad
 \mathcal I_{n,\varepsilon}^{(1)}:=
 \int_0^\infty E(u)e^{-(1+\varepsilon)u}
 \bigl((1+\varepsilon)L_n^{(1)}(u)-\varepsilon L_{n-1}^{(1)}(u)\bigr)du.
 \quad}
\tag{13}
\]

Every integral in (13) is absolutely convergent.  Passing to the combined
Abel limit, never to the two terms separately, gives

\[
 \boxed{\quad
 \Delta D_n=\Delta A_n-2-2\mathcal I_n^{(1)},
 \qquad
 \mathcal I_n^{(1)}:=\lim_{\varepsilon\downarrow0}
 \mathcal I_{n,\varepsilon}^{(1)}.
 \quad}
\tag{14}
\]

The archimedean increment is explicit:

\[
 \Delta A_n=-{\gamma+\log(4\pi)\over2}
 +\sum_{\ell\ \rm odd}{1-(1-1/\ell)^n\over\ell}
 ={1\over2}\log n+O(1).
\tag{15}
\]

Therefore the exact first-difference barrier is

\[
 \boxed{\quad
 \mathcal I_n^{(1)}\le\frac12\Delta A_n-1
 ={1\over4}\log n+O(1).
 \quad}
\tag{16}
\]

If (16) were proved for every \(n\ge149\), then (2) and induction would
prove \(D_n>0\) for every \(n\).  It is a valid sufficient theorem, but
also RH-strength after the finite Li checks.

## 3. Completed partition for a prospective signed proof

For a fixed \(\varepsilon>0\), retain the completed kernel in (13) and
write

\[
 \mathcal I_{n,\varepsilon}^{(1)}
 =(1+\varepsilon)J_{n,\varepsilon}
 -\varepsilon J_{n-1,\varepsilon},
 \qquad
 J_{m,\varepsilon}:=\int_0^\infty
 E(u)e^{-(1+\varepsilon)u}L_m^{(1)}(u)\,du.
\tag{17}
\]

Let \(x_{m,1}<\cdots<x_{m,m}\) be the positive zeros of
\(L_m^{(1)}\), and choose one fixed \(B>\log2\) which is not a
prime-power logarithm.  Let \(\mathscr L_m(B)\) be the nonempty components
of \([B,x_{m,m}]\) after all zeros of \(L_m^{(1)}\) in that interval have
been inserted.  The identity (17) has the following complete,
endpoint-safe split (for the eventual range \(B<x_{m,m}\)):

\[
 J_{m,\varepsilon}=
 \underbrace{\int_0^{\log2}\!\cdots}_{\text{empty arithmetic}}
 +\underbrace{\int_{\log2}^{B}\!\cdots}_{\text{fixed finite data}}
 +\underbrace{\sum_{I\in\mathscr L_m(B)}\int_I\!\cdots}_{\text{alternating lobes}}
 +\underbrace{\int_{x_{m,m}}^{\infty}\!\cdots}_{\text{final ray}}.
\tag{18}
\]

The first interval is explicit because \(E=-e^u\) below \(\log2\); the
second has only finitely many prime-power jumps and can be evaluated by
Stieltjes summation; the lobe signs alternate; and the final ray has the
fixed sign \((-1)^m\) of \(L_m^{(1)}\).  Formula (18), applied for both
\(m=n\) and \(m=n-1\) before taking the Abel limit, is the completed
partition required by (13).  It is a certificate *schema*: a future proof
must establish the signed comparison of the actual prime-power blocks and
the pole contribution on the final ray.  The partition itself supplies no
such comparison.

## 4. VK/Abel absolute-envelope no-go by scale

Consider the standard VK-shaped envelope

\[
 |E(u)|\le C e^u e^{-\eta(u)},
 \qquad
 \eta(u)=c\,u^{3/5}(\log u)^{-1/5}\quad(u\ \hbox{large}),
\tag{19}
\]

with fixed positive constants \(C,c\).  Replacing \(E\) by this absolute
envelope in (13), then letting \(\varepsilon\downarrow0\), asks one to
bound the positive load

\[
 \mathcal B_n:=\int_1^\infty e^{-\eta(u)}|L_n^{(1)}(u)|\,du.
\tag{20}
\]

This is also a lower bound for the limiting absolute completed-kernel load:
the kernel in (13) converges pointwise to \(L_n^{(1)}\), so Fatou's lemma
applied to its nonnegative absolute value gives \(\liminf_{\varepsilon\downarrow0}
\int e^{-\eta}|(1+\varepsilon)L_n^{(1)}-\varepsilon L_{n-1}^{(1)}|
\ge\mathcal B_n\).

This load is far larger than the target (16).  Here is an elementary scale
proof.  All zeros of \(L_n^{(1)}\) lie below \(6n\) for large \(n\) (the
standard explicit Laguerre edge bound used in `103_03`).  Since its leading
coefficient is \((-1)^n/n!\), for \(u\ge12n\),

\[
 |L_n^{(1)}(u)|={1\over n!}\prod_{j=1}^n(u-x_{n,j})
 \ge{(u/2)^n\over n!}.
\tag{21}
\]

Choose

\[
 U_n=n^{5/3}(\log n)^{1/3}.
\tag{22}
\]

On \([U_n,U_n+1]\), (19)--(22) and Stirling's elementary upper bound
\(n!\le n^ne^{-n}e\sqrt n\) give

\[
 \log\mathcal B_n
 \ge {2\over3}n\log n+{1\over3}n\log\log n-O(n).
\tag{23}
\]

Indeed \(\eta(U_n)=O(n)\), whereas the product term in (21) contributes
\(n\log(U_n/2)-\log n!\).  Hence

\[
 \mathcal B_n\ge
 \exp\!\left({2\over3}n\log n+{1\over3}n\log\log n-O(n)\right),
\tag{24}
\]

while the allowed upper bound in (16) is only \(O(\log n)\).

Thus a proof which takes absolute values after inserting a VK envelope is
not merely quantitatively loose: its own positive load has exponentially
wrong scale.  The conclusion is restricted to this envelope/absolute-value
method.  It does not preclude an argument which uses signed cancellation of
the actual \(\Lambda(p^k)=\log p\) blocks in (18).

## Status

First-difference monotonicity has passed every available exact finite
interval test, through \(n=148\).  The exact Abel identity and a completed
lobe/final-ray partition are in place.  The natural VK absolute estimate is
eliminated by the scale gap (24) versus (16); the missing ingredient is a
signed, arithmetic pole--prime comparison.  No eventual monotonicity, A1,
or RH conclusion has been established.
