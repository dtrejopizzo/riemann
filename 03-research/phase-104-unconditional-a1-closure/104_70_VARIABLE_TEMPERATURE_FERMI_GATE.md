# 104_70 — Variable-temperature Fermi and universal polar no-go

**Result.** A subexponentially decreasing temperature does not destroy
the Fermi criterion. In particular,

\[
 t_n=e^{-\sqrt n},\qquad b_n=e^{2\sqrt n},                 \tag{1}
\]

gives

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 {1\over H_X}\sum_{n\le X}{1\over n}
 {1\over1+\exp(t_n(\lambda_n+b_n))}\longrightarrow0.}     \tag{2}
\]

A lower temperature also does not resolve the prime–pole
conditioning. There is an exact incompatibility: if \(\varepsilon_n\to0\)
and \(t_np_n(\varepsilon_n)\) stays bounded, then
\(t_nR^n\to0\) for every \(R>1\). But detecting any off-line mode of
rate \(R\) requires \(t_nR^n\to\infty\). No scale satisfies both
requirements.

The paired prime–Laguerre lift remains exact. For choice (1) it can be
diagonalized as in 104_69; for a general temperature a quantitative
condition like (21a) below is additionally needed. Conditions
(V1)--(V3) alone do not control the upper growth of \(t_n\), and hence
the Cauchy bound alone does not suffice to conclude that diagonal
approximation. The separated polar part
has, in example (1), cost \(\exp(X^2/100-\sqrt X)\), essentially the
same quadratic cost. This document proves the criterion and the no-go;
it does not prove its limit for zeta, A1, or RH.

---

## 1. General variable-temperature criterion

Let \(t_n>0\), \(b_n\ge0\), and set

\[
 a_n(t,b)={1\over1+\exp(t_n(\lambda_n+b_n))},\qquad
 \mathfrak F_{t,b}(X)
 ={1\over H_X}\sum_{n\le X}{a_n(t,b)\over n}.              \tag{3}
\]

The natural conditions are

\[
\begin{array}{ll}
 \text{(V1)}&t_nb_n\longrightarrow\infty,\\
 \text{(V2)}&t_nR^n\longrightarrow\infty
              \quad\hbox{for every }R>1,\\
 \text{(V3)}&b_n/R^n\longrightarrow0
              \quad\hbox{for every }R>1.
\end{array}                                                \tag{4}
\]

**Theorem 1.1.** Under (V1)--(V3),

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \mathfrak F_{t,b}(X)\longrightarrow0
 \quad\Longleftrightarrow\quad
 \liminf_{X\to\infty}\mathfrak F_{t,b}(X)=0.}              \tag{5}
\]

**Proof.** Under RH, \(\lambda_n\ge0\), so

\[
 0\le a_n(t,b)\le{1\over1+e^{t_nb_n}}\longrightarrow0.
 \tag{6}
\]

The logarithmic average of a bounded sequence tending to zero also
tends to zero.

If RH is false, 104_56 gives \(c>0\), \(R>1\), and a set \(D\) of
natural density \(d>0\) such that \(\lambda_n\le-cR^n\) on \(D\). By
(V3), \(b_n\le(c/2)R^n\) eventually. Then, on \(D\),

\[
 t_n(\lambda_n+b_n)
 \le-{c\over2}t_nR^n\longrightarrow-\infty               \tag{7}
\]

by (V2), and \(a_n(t,b)\to1\). The logarithmic density of \(D\) gives

\[
 \liminf_{X\to\infty}\mathfrak F_{t,b}(X)\ge d>0.
 \tag{8}
\]
\(\square\)

A sufficient, easier-to-check family is

\[
 0<t_n\le1,\qquad
 -\log t_n=o(n),\qquad
 \log(1+b_n)=o(n),\qquad
 t_nb_n\to\infty.                                         \tag{9}
\]

The two \(o(n)\) conditions imply (V2)--(V3). It is important to keep
the condition on \(b_n\): the hypotheses
\(-\log t_n=o(n)\) and \(t_nb_n\to\infty\) alone would allow a
superexponential barrier hiding every excursion.

Choice (1) satisfies (9), since

\[
 -\log t_n=\sqrt n=o(n),\qquad
 \log b_n=2\sqrt n=o(n),\qquad
 t_nb_n=e^{\sqrt n}\to\infty.                              \tag{10}
\]

---

## 2. Exact characterization of the polar cost

The regulated polar term is

\[
 p_n(\varepsilon)
 =1+(-1)^{n-1}
 \left({1-\varepsilon\over\varepsilon}\right)^n.           \tag{11}
\]

Set

\[
 A(\varepsilon)={1-\varepsilon\over\varepsilon}.
\]

For \(0<\varepsilon<1/2\),

\[
 |p_n(\varepsilon)-1|=A(\varepsilon)^n.                   \tag{12}
\]

If \(0<t_n\le1\), then

\[
 \left|\,t_n|p_n(\varepsilon_n)|
 -t_n|p_n(\varepsilon_n)-1|\,\right|\le t_n\le1.
 \tag{12a}
\]

Hence boundedness of the pole \(t_np_n\) and of its divergent part
\(t_n(p_n-1)\) are equivalent. We work with the latter since it has
the exact formula (12).

So, given \(K>0\),

\[
 t_n|p_n(\varepsilon_n)-1|\le K
\]

if and only if

\[
 A(\varepsilon_n)\le(K/t_n)^{1/n},
\]

or, equivalently,

\[
 \boxed{\varepsilon_n\ge
 {1\over1+(K/t_n)^{1/n}}.}                                \tag{13}
\]

If \(-\log t_n=o(n)\) and \(K\) is fixed, the right-hand side of (13)
tends to \(1/2\). So controlling the pole forces
\(\varepsilon_n\ge1/2-o(1)\), not sending it to zero.

For (1), with \(K=1\),

\[
 \varepsilon_n\ge
 {1\over1+e^{1/\sqrt n}}
 ={1\over2}-{1\over4\sqrt n}+O(n^{-3/2}).                  \tag{14}
\]

Lowering the temperature only moves the admissible regulator toward
\(1/2\); not toward the boundary \(\varepsilon=0\).

---

## 3. Universal temperature–regulator no-go

The incompatibility does not depend on the subexponential choice.

**Theorem 3.1.** Let \(t_n>0\) and \(\varepsilon_n\to0\). If there is
\(K<\infty\) such that

\[
 t_n|p_n(\varepsilon_n)-1|\le K                           \tag{15}
\]

eventually, then for every \(R>1\),

\[
 \boxed{t_nR^n\longrightarrow0.}                          \tag{16}
\]

In particular, (15) is incompatible with (V2).

**Proof.** From (12) and (15),

\[
 t_nR^n
 \le K\left({R\over A(\varepsilon_n)}\right)^n
 =K\left({R\varepsilon_n\over1-\varepsilon_n}\right)^n.
 \tag{17}
\]

Since \(\varepsilon_n\to0\), the base of the last term tends to zero;
it is, for example, less than \(1/2\) from some index on. This proves
(16). \(\square\)

The useful converse is equally strong. If (V2) holds, then for every
\(\varepsilon_n\to0\),

\[
 \boxed{t_n|p_n(\varepsilon_n)-1|\longrightarrow\infty.}  \tag{18}
\]

Indeed, given any \(R>1\), eventually
\(A(\varepsilon_n)\ge R\), and (12) dominates \(t_nR^n\).

So there is no temperature that simultaneously:

1. detects every off-line rate \(R>1\);
2. allows \(\varepsilon_n\to0\); and
3. keeps the polar channel bounded before combining it with the primes.

To allow (2)--(3) one would need

\[
 {-\log t_n\over n}\longrightarrow\infty,                 \tag{19}
\]

but then \(t_nR^n\to0\) for every \(R>1\), exactly the loss of the
detector.

---

## 4. The paired lift still exists

Although the separated pole diverges, the paired combination

\[
 \lambda_{n,\varepsilon}
 =A_n+p_n(\varepsilon)
 -\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m)                                    \tag{20}
\]

remains available. For a finite \(X\), use, as in 104_69,

\[
 \varepsilon_X=e^{-X/100}.                                \tag{21}
\]

Set

\[
 \Theta_X={1\over H_X}\sum_{n\le X}{t_n\over n}.
\]

The following diagonal approximation is guaranteed if

\[
 \boxed{X e^{-\eta X}\Theta_X\longrightarrow0.}          \tag{21a}
\]

This condition holds, in particular, if \(0<t_n\le1\), and hence for
choice (1). It is not a consequence of (V1)--(V3): those conditions
allow temperatures \(t_n\) growing faster than \(e^{\eta n}\).

Define

\[
 \mathfrak F^{\mathrm{var}}_{\varepsilon_X}(X)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 {1\over1+\exp(t_n(\lambda_{n,\varepsilon_X}+b_n))}.
 \tag{22}
\]

The derivative with respect to \(\lambda\) has modulus at most
\(t_n/4\). The uniform bound of 104_69 gives, with

\[
 \eta={1\over100}-\log{200\over199}>0,\qquad M=M_{199/200},
\]

\[
 \boxed{
 |\mathfrak F^{\mathrm{var}}_{\varepsilon_X}(X)
 -\mathfrak F_{t,b}(X)|
 \le {M\over2}Xe^{-\eta X}\Theta_X\longrightarrow0.}      \tag{23}
\]

Substituting (20), the exact expression is

\[
\boxed{
\begin{aligned}
 \mathfrak F^{\mathrm{var}}_{\varepsilon_X}(X)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 \Bigg[1+
 &e^{t_n(A_n+b_n+p_n(\varepsilon_X))}\\
 &\times\prod_{m\ge2}
 \exp\!\left(
 -{t_n\Lambda(m)\over m^{1+\varepsilon_X}}
 L_{n-1}^{(1)}(\log m)\right)
 \Bigg]^{-1}.
\end{aligned}}                                            \tag{24}
\]

For each \(X\), all the products converge absolutely. The temperature
appears inside the complete phase and does not authorize separating
its factors.

At the endpoint \(n=X\), choice (1) and (21) give

\[
\begin{aligned}
 \log\{t_X|p_X(\varepsilon_X)-1|\}
 &=-\sqrt X+X\log(e^{X/100}-1)\\
 &={X^2\over100}-\sqrt X+o(1).
\end{aligned}                                             \tag{25}
\]

The \(-\sqrt X\) improvement is negligible against the \(X^2/100\)
cost. The prime channel must cancel the polar phase with relative
precision

\[
 \boxed{\exp\{-X^2/100+O(X)\}.}                            \tag{26}
\]

The factor \(t_X\) multiplies both large channels as well as their
difference; that is why it cancels exactly when measuring relative
precision. The temperature reduces the absolute magnitude of both
phases, but not their relative conditioning.

---

## 5. Off-line falsifier

For the quadruple

\[
 Q_n=4-2\mathrm{Re}\,\{(2i)^n+(2i)^{-n}\},            \tag{27}
\]

and choice (1):

* if \(n\equiv0\pmod4\), then
  \(t_n(Q_n+b_n)\to-\infty\);
* if \(n\equiv2\pmod4\), then
  \(t_n(Q_n+b_n)\to+\infty\);
* if \(n\) is odd, \(Q_n=4\) and
  \(t_n(Q_n+b_n)=4e^{-\sqrt n}+e^{\sqrt n}\to+\infty\).

Consequently,

\[
 \boxed{
 {1\over H_X}\sum_{n\le X}{1\over n}
 {1\over1+\exp(t_n(Q_n+b_n))}
 \longrightarrow{1\over4}.}                              \tag{28}
\]

The variable-temperature detector does not erase the off-line divisor.

---

## 6. Verdict

**Proved:** the general criterion (5), example (1), characterization
(13), the universal no-go (15)--(18), the paired lift (24), its
diagonal approximation under (21a), cost (25), and the falsifier (28).

**Gain:** lowering the temperature preserves the criterion and offers a
new family of bounded observables.

**No-go:** no temperature capable of detecting every \(R>1\) can,
simultaneously with \(\varepsilon_n\to0\), keep the regulated pole
bounded. The subexponential temperature saving never offsets the polar
charge.

**Not proved:** a bound for the complete product (24), the Fermi limit
for the real weights, A1, or RH.

---

## 7. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 variable_temperature_fermi_gate_check.py
```

The checker verifies the polar identity, threshold (13), divergence
(18), the \(1/4\) value of the quadruple, and scale (25). The
asymptotic theorems are proved in the text.
