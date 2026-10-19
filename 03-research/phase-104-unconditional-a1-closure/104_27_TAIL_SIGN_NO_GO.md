# 104_27 — The VK envelope does not determine the tail's sign

**Role.** Audit whether the A0+ improvement can be strengthened by
replacing \(|R_n(T_n)|\) with the favorable sign \(R_n(T_n)\le0\). The
result is negative for the current inputs: the same
Vinogradov–Korobov envelope admits discrepancies with tails of both signs,
even if \(e^u+E(u)\) is required to be increasing on the final ray. Hence a
sign theorem for the tail would need arithmetic structure from the weights
\(\Lambda(m)\), not just A0, PNT, and monotonicity.

This document does not claim that the real arithmetic tail has both signs;
it is a logical no-go for a class of inputs.

## 1. The eventual sign of the kernel

Let \(x_{*,n}\) be the largest zero of \(L_{n-1}^{(2)}\) and
\(s_n=(-1)^{n-1}\). For \(u>x_{*,n}\),

\[
 K_n(u)=e^{-u}L_{n-1}^{(2)}(u)
       =s_ne^{-u}|L_{n-1}^{(2)}(u)|.              \tag{1}
\]

Write the PNT envelope as

\[
 W(u)=C_{\rm VK}e^{u-\eta(u)},\qquad
 |E(u)|\le W(u).                                   \tag{2}
\]

For \(\sigma\in\{-1,1\}\), define on the ray \(u\ge T>x_{*,n}\)

\[
 E_\sigma(u)=\sigma s_nW(u).                      \tag{3}
\]

Both functions satisfy exactly the same input (2), but

\[
 \boxed{
 R_{n,\sigma}(T)
 =-\sigma C_{\rm VK}\int_T^\infty
 e^{-\eta(u)}|L_{n-1}^{(2)}(u)|\,du.}             \tag{4}
\]

Thus, \(\sigma=-1\) gives \(R_{n,\sigma}(T)>0\), while
\(\sigma=1\) gives \(R_{n,\sigma}(T)<0\), for every finite cutoff.

## 2. Quantitative witness

Factoring over the positive real Laguerre zeros gives

\[
 |L_{n-1}^{(2)}(u)|
 ={1\over(n-1)!}\prod_{j=1}^{n-1}(u-x_{j,n})
 \ge{(T-x_{*,n})^{n-1}\over(n-1)!}
 \quad(T\le u\le T+1).                            \tag{5}
\]

If \(\eta\) is increasing on that ray, (4)–(5) imply

\[
 \boxed{
 |R_{n,\sigma}(T)|
 \ge {C_{\rm VK}e^{-\eta(T+1)}
             (T-x_{*,n})^{n-1}\over(n-1)!}.}      \tag{6}
\]

This is therefore not a defect that vanishes because the witness is
identically zero.

## 3. Smooth, monotone version

To share the initial datum \(E(T)=0\), set

\[
 \phi_T(u)=1-e^{-(u-T)},\qquad
 \widetilde E_\sigma(u)=\sigma s_nW(u)\phi_T(u).  \tag{7}
\]

The same computation, restricted to \([T+1,T+2]\), gives

\[
 |\widetilde R_{n,\sigma}(T)|
 \ge {C_{\rm VK}(1-e^{-1})e^{-\eta(T+2)}
        (T+1-x_{*,n})^{n-1}\over(n-1)!},          \tag{8}
\]

with opposite signs for the two values of \(\sigma\).

Moreover, if \(T\) is enlarged until

\[
 C_{\rm VK}e^{-\eta(u)}
 \bigl(\phi_T(u)+|\phi_T'(u)-\eta'(u)\phi_T(u)|\bigr)<1
 \qquad(u\ge T),                                  \tag{9}
\]

then

\[
 {d\over du}\bigl(e^u+\widetilde E_\sigma(u)\bigr)>0
\]

for both signs. The usual VK functions satisfy (9) on every sufficiently
distant ray, and enlarging a cutoff preserves A0. So adding monotonicity
does not determine the tail's sign within this class.

## 4. Scope

The witness is not supported on prime powers and does not claim to model
the von Mangoldt weights. It proves exactly the following:

\[
 \boxed{
 \text{A0/VK + monotonicity on the final ray}
 \ \not\Longrightarrow\ R_n(T_n)\le0.}            \tag{10}
\]

Choosing "the first \(T\) with \(R_n(T)\le0\)" is likewise not an
unconditional construction: the set can be empty within class (3), and
verifying that it is not empty for the real discrepancy already requires
new arithmetic information.

## Status

- **Proved:** witnesses of both signs (4), the quantitative bounds (6),
  (8), and their eventual compatibility with monotonicity.
- **Ruled out:** obtaining A1 from the quartic margin using only a
  favorable tail sign deduced from A0/VK.
- **Open:** any sign argument that essentially uses the support on prime
  powers and the exact values \(\Lambda(m)\).
</content>
