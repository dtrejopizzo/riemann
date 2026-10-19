# 104_113 — Classical-inputs gate for the deep box

**Question.** Once `104_112` reduces the Deep limit to excluding the box

\[
 R_X=\left\{\rho=\beta+i\gamma:\ 0<\gamma\lesssim X^{1/4},\quad
 \beta-\frac12\gtrsim \gamma^2X^{-1/2}\right\},
\]

can a classical zero-free region, a density theorem, a finite zero
verification, or a combination of these inputs close it?

**Result.** Not as standalone inputs. With \(T=X^{1/4}\), the box is

\[
 R_T=\left\{\rho:\ 0<\gamma\lesssim T,\quad
 \beta-\frac12\gtrsim{\gamma^2\over T^2}\right\}.        \tag{1}
\]

Its boundary touches \(\Re s=1/2\) in every regime
\(\gamma=o(T)\). Excluding \(R_T\) for every \(T\) is equivalent, letting
\(T\to\infty\) with \(\gamma\) fixed, to excluding every zero with
\(\beta>1/2\). That is why inputs that do not prove exact absence on the
critical line have nowhere to gain ground:

1. The known zero-free regions exclude only a neighborhood of
   \(\Re s=1\), the wrong transversal direction.
2. Density theorems bound how many zeros there are with
   \(\beta\ge\sigma\); they do not turn a counting bound into zero zeros
   at \(\sigma=1/2+o(1)\).
3. Verification up to height \(H\) only excludes the box for
   \(X\lesssim H^4\), not asymptotically.

This document neither proves nor refutes \(R_X=\varnothing\) for zeta. It
closes the route of using classical inputs as a substitute for the
literal arithmetic mechanism.

---

## 1. \(T\)-scaled form of the box

The scale \(Y=X^{1/4}\) of `104_76` and `104_112` is not decorative. If
\(T=X^{1/4}\), then \(X^{-1/2}=T^{-2}\), and the box becomes
(1). For a fixed zero \(\rho=\beta+i\gamma\), \(\beta>1/2\), the condition
\[
 \beta-\frac12\gtrsim{\gamma^2\over T^2}
\]
holds for every sufficiently large \(T\). Hence a uniform proof of
\(R_T=\varnothing\) as \(T\to\infty\) is already a proof that no zero
with \(\beta>1/2\) exists. By functional symmetry, that is RH.

The weakness of the deep detector is that, for each \(T\), it only looks
at heights \(\gamma\lesssim T\) and requires a radial precision of
\(\gamma^2/T^2\). But that precision tends to zero for each fixed zero.
There is no permanent margin between the box and the critical line.

## 2. Zero-free regions

A Vinogradov–Korobov/Mossinghoff–Trudgian–Yang zero-free region has the
form

\[
 \beta\le1-\Delta(\gamma),
 \qquad
 \Delta(\gamma)\asymp(\log\gamma)^{-2/3}(\log\log\gamma)^{-1/3}
\]

in the corresponding range. This excludes a strip attached to
\(\Re s=1\). Box (1), by contrast, contains points with
\[
 \beta=\frac12+C{\gamma^2\over T^2}.
\]

If \(\gamma=o(T)\), these points are arbitrarily close to the critical
line and very far from the boundary \(\Re s=1-\Delta(\gamma)\). The
classical zero-free region does not interact with that part of the box.
At the edge \(\gamma\asymp T\), the box requires excluding shifts of
constant size from \(1/2\); the zero-free region still does not reach
that scale except near \(1\).

Conclusion: a classical zero-free region can reduce the adversarial
radial bound of `104_90`, but it cannot make \(R_T\) empty.

## 3. Density theorems

A typical density theorem gives

\[
 N(\sigma,T)
 =\#\{\rho:\beta\ge\sigma,\ 0<\gamma\le T\}
 \le C\,T^{A(1-\sigma)}(\log T)^B .                    \tag{2}
\]

Excluding the box would require a statement of the type
\[
 N\!\left({1\over2}+c{\gamma^2\over T^2};\ \gamma\hbox{ local}\right)=0
\]
in every height subrange. Even if \(\gamma\) is replaced by a dyadic
subrange \(\Gamma<\gamma\le2\Gamma\), (2) at
\(\sigma=1/2+c\Gamma^2/T^2\) gives a right-hand side of positive size,
and huge in the regimes \(\Gamma=o(T)\):

\[
 T^{A(1/2-c\Gamma^2/T^2)}(\log T)^B .
\]

An upper bound larger than one does not exclude a single zero. But a
single zero in the box trips the deep detector on a syndetic set of
degrees. This is the exact mismatch: density controls aggregate counting;
Deep demands individual absence.

## 4. Finite verification

If RH is verified up to height \(H\), then the box is empty for every
\(X\) with \(X^{1/4}\le H\). That is, one obtains a range

\[
 X\le H^4 .                                             \tag{3}
\]

With \(H=3\cdot10^{12}\), this explains the diagnostic scale
\(\asymp8.1\cdot10^{49}\) for the pure boundary \(X^{1/4}=H\), and the
constants of `104_90` shift the practical crossover to
\(\asymp4H^4\). But no finite \(H\) reaches the limit
\(X\to\infty\). The zeros that matter beyond that scale are precisely
those immediately above the verified height, not a remote tail that can
be summed absolutely.

Finite verification is, therefore, a consistency test and a certified
finite range. It is not an asymptotic substitute for the exclusion of
\(R_T\).

## 5. Consequence

The deep box leaves only one class of successors: an inequality that
uses the literal ordinary weights \(\Lambda(p^k)=\log p\), the real
support of the primes, and the exact Riemann completion to exclude
interior poles. It must fail for the models of `104_78`, `104_81`,
`104_90`, and `104_91`, because all of them preserve broad packages of
positivity, PNT, or functional symmetry and still have exterior zeros.

In particular, there is no partial progress in improving a positive
density bound, nor in extending a finite verified height, except as
computational evidence. The remaining goal is exactly \(R_T=\varnothing\)
for every \(T\), with an arithmetic proof not reducible to counting.
</content>
