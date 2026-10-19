# 104_98 — Mellin factorization of the prime energy and monodromy gate

## Result

Set

\[
 L_2(x)=\int_2^x{du\over\log u},\qquad
 P_m=\pi(m)-L_2(m),\qquad P_1=0,
 \tag{1}
\]

and \(a_m=P_m-P_{m-1}\). For \(N\ge2\), define

\[
 \Phi_N(s)=\sum_{m=2}^N P_m\{m^{-s}-(m+1)^{-s}\}.
 \tag{2}
\]

There is an exact, unconditional, finite spectral factorization:

\[
 \boxed{
 \sum_{m=2}^N{P_m^2\over m(m+1)}
 ={1\over2\pi}\int_{-\infty}^{\infty}
 \left|{\Phi_N(\tfrac12+it)\over\tfrac12+it}\right|^2dt.}
 \tag{3}
\]

The moving boundary is exactly contained in

\[
 \boxed{
 \Phi_N(s)=\sum_{m=2}^Na_m m^{-s}-P_N(N+1)^{-s}.}
 \tag{4}
\]

Taking \(N\to\infty\) initially in \(\Re s>1\), the literal symbol
of the ordinary primes is

\[
 \Phi(s)=\mathcal P(s)-D(s),\qquad
 \mathcal P(s)=\sum_p p^{-s},
 \tag{5}
\]

where

\[
 D(s)=\sum_{m=3}^{\infty}m^{-s}
       \int_{m-1}^{m}{dx\over\log x}.
 \tag{6}
\]

If \(E_1(z)=\int_z^\infty e^{-u}du/u\), on compatible branches one
obtains the regularized continuation

\[
 \boxed{
 \Phi(s)=
 \sum_{k\ge1}{\mu(k)\over k}\log\zeta(ks)
 -E_1((s-1)\log2)+R(s),}
 \tag{7}
\]

with

\[
 R(s)=\sum_{m=3}^{\infty}\int_{m-1}^{m}
       {x^{-s}-m^{-s}\over\log x}\,dx,
 \qquad R\in\mathcal O(\Re s>0).
 \tag{8}
\]

In the open half-plane \(\Re s>1/2\), all terms \(k\ge2\)
of (7) are regular. The pole at \(s=1\) cancels exactly with
\(E_1\). Hence a zero \(\rho\), \(\Re\rho>1/2\), of multiplicity
\(m_\rho\) produces, and can only produce, there

\[
 \boxed{
 \Phi(s)=m_\rho\log(s-\rho)+h_\rho(s),\qquad
 h_\rho\ \text{locally holomorphic}.}
 \tag{9}
\]

The monodromy is \(2\pi i m_\rho\). It has an exact positive diagonal:
on a small circle around \(\rho\), for all \(c\in
\mathbb C\),

\[
 {1\over2\pi}\int_0^{2\pi}
 |\Phi(\rho+re^{i\theta})-c|^2d\theta
 \ \ge\ {\pi^2m_\rho^2\over6}.
 \tag{10}
\]

But (10) lives on **all the sheets** of the continuation. The prime
energy (3) lives in a single physical approximation by Dirichlet
polynomials. If \(\Phi_\pm\) are the two sides of a cut and
\(\Phi_0=(\Phi_++\Phi_-)/2\), then exactly

\[
 \begin{aligned}
 { |\Phi_+|^2+|\Phi_-|^2\over2}
   &=|\Phi_0|^2+\pi^2m_\rho^2,\\
 |\Phi_+|^2-|\Phi_-|^2
   &=4\pi m_\rho\,\Im\Phi_0.
 \end{aligned}
 \tag{11}
\]

The first line has the diagonal sought; the second line is the
signed part that prevents transferring it to a single sheet. There is no sign
reason for \(\Im\Phi_0\). The explicit formula gives the same obstruction:
the zero--zero square is a positive Gram matrix as a whole, but
its off-diagonal entries, and even the double-frequency term
of a single conjugate pair, change sign.

**Verdict.** The requested exact Mellin representation was obtained and a
positive topological diagonal was isolated. It does not close the energy because the
diagonal belongs to the average of two sheets, while the ordinary
weights select a single sheet and leave the signed term of
(11). Proving that this term does not destroy the diagonal, uniformly for
the polynomials \(\Phi_N\), amounts again to proving the
subpolynomial bound of `104_93`--`104_94`. This document does not prove that
bound, Deep-\(\Lambda\), A1 nor RH.

---

## 1. Finite Plancherel without analytic continuation

For \(\sigma>0\), define on the logarithmic line

\[
 f_{N,\sigma}(y)=
 \begin{cases}
 e^{-\sigma y}P_m,&\log m\le y<\log(m+1),\quad2\le m\le N,\\
 0,&\text{outside those intervals}.
 \end{cases}
 \tag{12}
\]

With the convention
\(\widehat f(t)=\int_{\mathbb R}f(y)e^{-ity}dy\), an elementary
integration on each interval gives

\[
 \widehat f_{N,\sigma}(t)
 ={1\over \sigma+it}
 \sum_{m=2}^NP_m\{m^{-\sigma-it}-(m+1)^{-\sigma-it}\}
 ={\Phi_N(\sigma+it)\over\sigma+it}.
 \tag{13}
\]

Plancherel proves the more general identity

\[
 \boxed{
 {1\over2\sigma}\sum_{m=2}^NP_m^2
 \{m^{-2\sigma}-(m+1)^{-2\sigma}\}
 ={1\over2\pi}\int_{\mathbb R}
 \left|{\Phi_N(\sigma+it)\over\sigma+it}\right|^2dt.}
 \tag{14}
\]

Taking \(\sigma=1/2\) gives (3). No infinite sum and integral are
interchanged here, no explicit formula is used, and RH is not presupposed.

To obtain (4), write \(P_m=\sum_{r=2}^ma_r\) and telescope:

\[
 \begin{aligned}
 \Phi_N(s)
 &=\sum_{r=2}^Na_r\sum_{m=r}^N
   \{m^{-s}-(m+1)^{-s}\}\\
 &=\sum_{r=2}^Na_rr^{-s}-P_N(N+1)^{-s}.
 \end{aligned}
 \tag{15}
\]

Expanding the square also exactly recovers

\[
 \sum_{m=2}^N{P_m^2\over m(m+1)}
 =\sum_{r,q=2}^Na_ra_q
 \left\{{1\over\max(r,q)}-{1\over N+1}\right\}.
 \tag{16}
\]

Thus (3) is not a disguised new estimate: it is the exact Mellin
factorization of the `max` kernel from `104_93`.

## 2. The infinite symbol of the ordinary primes

For \(m\ge3\), set

\[
 d_m=L_2(m)-L_2(m-1)=\int_{m-1}^m{dx\over\log x},
 \qquad d_2=0.
 \tag{17}
\]

Then \(a_m={\bf1}_{\mathbb P}(m)-d_m\), also at \(m=2\), and
for \(\Re s>1\)

\[
 \Phi(s):=\sum_{m\ge2}a_mm^{-s}=\mathcal P(s)-D(s).
 \tag{18}
\]

On that half-plane \(P_m=O(m)\), so the boundary term of (4) tends to
zero. By (14), now without a cutoff,

\[
 {1\over2\sigma}\sum_{m\ge2}P_m^2
 \{m^{-2\sigma}-(m+1)^{-2\sigma}\}
 ={1\over2\pi}\int_{\mathbb R}
 \left|{\Phi(\sigma+it)\over\sigma+it}\right|^2dt
 \quad(\sigma>1).
 \tag{19}
\]

The continuous comparator satisfies

\[
 I(s):=\int_2^\infty{x^{-s}\over\log x}dx
 =E_1((s-1)\log2).
 \tag{20}
\]

Moreover,

\[
 I(s)-D(s)=\sum_{m=3}^{\infty}\int_{m-1}^{m}
 {x^{-s}-m^{-s}\over\log x}dx=R(s).
 \tag{21}
\]

If \(K\Subset\{\Re s>0\}\), then, uniformly for \(s\in K\),

\[
 |x^{-s}-m^{-s}|
 =\left|s\int_x^m u^{-s-1}du\right|
 \ll_K m^{-1-\inf_K\Re s}.
 \tag{22}
\]

Series (21) converges normally. This proves the holomorphy
claim of (8). Finally, the Möbius inversion of the Euler product gives

\[
 \mathcal P(s)=\sum_{k\ge1}{\mu(k)\over k}\log\zeta(ks),
 \qquad \Re s>1,
 \tag{23}
\]

and (7) follows from (18)--(23).

## 3. The only right branch points

In \(\Re s>1/2\), for \(k\ge2\) one has \(\Re(ks)>1\). Hence
\(\log\zeta(ks)\) admits a holomorphic branch there and the sum of those
terms converges normally on compacta. Near \(s=1\),

\[
 \log\zeta(s)=-\log(s-1)+O(1),
 \qquad
 E_1((s-1)\log2)=-\gamma-\log((s-1)\log2)+O(s-1),
 \tag{24}
\]

so their difference has a removable singularity.

Equivalently, differentiating (7),

\[
 \boxed{
 \Phi'(s)=
 \sum_{k\ge1}\mu(k){\zeta'(ks)\over\zeta(ks)}
 +{2^{1-s}\over s-1}+R'(s).}
 \tag{25}
\]

The residues \(-1\) and \(+1\) at \(s=1\) cancel. At a right
zero \(\rho\) of multiplicity \(m_\rho\), (25) has residue
\(m_\rho\). This proves (9) and shows that the proper powers do not
contaminate the diagnostic: their singularities \(\rho/k\), \(k\ge2\),
remain in \(\Re s<1/2\). This is the analytic-continuation version of the
elementary energy split from `104_94`.

## 4. A positive monodromy diagonal

Choose \(r>0\) so that the closed disk around \(\rho\) lies
in \(\Re s>1/2\) and contains no other singularity. On the universal
cover of the punctured disk,

\[
 \Phi(\rho+re^{i\theta})
 =m_\rho(\log r+i\theta)+h_\rho(\rho+re^{i\theta}),
 \quad0\le\theta<2\pi.
 \tag{26}
\]

With
\(\widehat g(n)=(2\pi)^{-1}\int_0^{2\pi}g(\theta)e^{-in\theta}d\theta\),

\[
 \widehat{i\theta}(n)=-{1\over n}\quad(n\ne0).
 \tag{27}
\]

The trace of a holomorphic function on the disk has only modes
\(n\ge0\). Consequently, for every \(k\ge1\), mode \(-k\) of the
right-hand side of (26) is exactly \(m_\rho/k\). No choice of
the holomorphic part nor of the constant \(c\) can cancel it. Parseval gives

\[
 {1\over2\pi}\int_0^{2\pi}|\Phi-c|^2d\theta
 \ge m_\rho^2\sum_{k\ge1}{1\over k^2}
 ={\pi^2m_\rho^2\over6},
 \tag{28}
\]

which proves (10).

This is indeed a positive diagonal mechanism, but it is not yet a bound
on the prime weights on the physical line. To go around \(\rho\) one must
traverse all determinations of \(\log(s-\rho)\). The polynomials
\(\Phi_N\) of (2) are entire and single-valued; the monodromy only emerges
in a non-uniform limit outside the half-plane of convergence. Proving
that this limit is of Hardy class on all of \(\Re s>1/2\) is already the continuation
that `104_93` obtains **assuming** subpolynomial energy.

Accounting for the two sides makes the loss visible. Write

\[
 \Phi_\pm=\Phi_0\pm\pi i m_\rho.
 \tag{29}
\]

Expanding the squares proves (11). The diagonal
\(\pi^2m_\rho^2\) appears only after averaging both sheets; on one
sheet the term \(\pm2\pi m_\rho\Im\Phi_0\) remains, without a sign.

## 5. The same signed part in the explicit formula

Let \(\Pi_0(x)\) be Riemann's function that counts \(p^k\) with weight
\(1/k\), using half weight at a jump. For \(x>1\), with the sum over
zeros taken symmetrically,

\[
 \Pi_0(x)=\mathrm{li}(x)
 -\sum_\rho^{*}\mathrm{li}(x^\rho)
 -\log2+\int_x^\infty{du\over u(u^2-1)\log u}.
 \tag{30}
\]

Outside the jumps, if

\[
 Q(x)=\sum_{k\ge2}{1\over k}\pi(x^{1/k}),
 \tag{31}
\]

then \(\Pi_0(x)=\pi(x)+Q(x)\), and hence

\[
 \boxed{
 \pi(x)-L_2(x)=C_0(x)-Q(x)
 -\sum_\rho^{*}\mathrm{li}(x^\rho),}
 \tag{32}
\]

where

\[
 C_0(x)=\mathrm{li}(x)-L_2(x)-\log2
       +\int_x^\infty{du\over u(u^2-1)\log u}
 \tag{33}
\]

is fully explicit. The block \(Q\) has finite energy by
`104_94`; the jumps and the half-weight convention do not alter an
integral in \(x\).

For a finite set of zeros \(\rho_j=\beta+i\gamma_j\), closed
under conjugation, the part of exponent \(\beta\) satisfies, with
\(x=e^y\),

\[
 -\sum_j\mathrm{li}(e^{\rho_jy})
 ={2e^{\beta y}\over y}\Re\sum_{\gamma_j>0}
 c_je^{i\gamma_jy}+O_{\mathcal Z}(e^{\beta y}/y^2),
 \qquad c_j=-{1\over\rho_j}.
 \tag{34}
\]

Set \(\alpha=2\beta-1\) and, for a positive weight \(w(y)\),

\[
 K_w(\omega)=\int {w(y)\over y^2}e^{\alpha y}e^{i\omega y}dy.
 \tag{35}
\]

The weighted square of the leading term of (34), including the
energy factor \(e^{-y}\), is exactly

\[
 2\Re\sum_{j,k}
 \left\{c_j\overline{c_k}K_w(\gamma_j-\gamma_k)
       +c_jc_kK_w(\gamma_j+\gamma_k)\right\}.
 \tag{36}
\]

The full matrix is Gram and the total is nonnegative. However:

* \(K_w(0)\sum_j|c_j|^2\) is only a part of (36);
* the difference entries with \(j\ne k\) have both signs;
* already for a single conjugate pair one is left with

\[
 2|c|^2K_w(0)+2\Re\{c^2K_w(2\gamma)\},
 \tag{37}
\]

and the second term changes sign when the window is shifted.

Thus, the explicit formula and the monodromy localize the same residue:
**a positive diagonal plus a signed interference of the same origin**. The
positivity of the full square does not allow one to discard the interference,
since bounding the full square from above for the ordinary weights is
precisely the missing energy.

## 6. No internal duplication

* `104_93` proves the energy equivalence and the `max` form, but does not
  factor the literal energy of \(\pi-L_2\) on the Mellin line nor
  compute its branches.
* `104_94` removes the proper powers by a finite-energy
  perturbation; (25) gives the analytic counterpart: \(\rho/k\), \(k\ge2\),
  stays strictly to the left of the boundary.
* `104_89` uses Mellin--Plancherel for the tail of
  \(J-L_2\) **under RH**. Here (3) is finite and unconditional and (7)--(11)
  describe exactly what happens if there is a right zero.
* `phase-49/157` records the Cramér identity for \(\psi-x\) at
  the exponent level. It does not contain the discretized prime-zeta
  symbol, boundary (4), the Hardy floor (10) nor the sheet
  split (11).
* The prime-zeta uses in `phase-14-off-diagonal-anchor-asymmetry` are self-referential and are not
  coupled to this energy.

Hence this document does not claim as new the Riemann formula nor
Mellin--Plancherel. What is new within the program is the exact chain
(2)--(11) for the literal observable of `104_94`, and the diagnosis
that the available positive diagonal is a sheet average, not a
one-sided inequality on the arithmetic sheet.

## 7. Reproduction

From `tools/`:

```bash
python3 prime_energy_mellin_monodromy_check.py
```

The checker:

1. verifies (4) and (16) exactly with `Fraction`;
2. reconstructs \(\pi(m)-L_2(m)\) and the moving boundary for a real prefix;
3. exhibits a window where the \(2\gamma\) frequency term of
   (37) is strictly negative;
4. certifies, by tail bounds of \(\sum k^{-2}\), the floor
   \(m^2\pi^2/6\) of (10).

The numerical evaluations illustrate already proved identities; they are not
asymptotic evidence nor an RH certificate.
