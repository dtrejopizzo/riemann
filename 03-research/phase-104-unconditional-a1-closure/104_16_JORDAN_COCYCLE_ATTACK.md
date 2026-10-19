# 104_16 — Jordan cocycle: positive hierarchy and the exact loss of sign

**Status.** The cocycle

\[
 A_u(s):={\zeta(s-u)\over\zeta(s)}
 =\sum_{m\ge1}{J_u(m)\over m^s}
\]

extends the connection identity of E70.11 and the Riccati identity of
E70.12 to a complete hierarchy of non-negative arithmetic functions
\(\mu*\log^k\). This is an exact and useful fact. However, keeping the pole
coupled turns the positive hierarchy into a **difference** of
two positive hierarchies. Its first jet is exactly the regulated functional
\(C_{n,\varepsilon}\) from `104_12`, and its Cayley coefficients already have both
signs at \(n=1,6\), with a rational certificate.

Hence the proposed implication

\[
 \text{Jordan positivity on the real half-line}
 \quad\Longrightarrow\quad
 \text{sign/convexity of the Cayley–Laguerre coefficients}
\]

fails. Moreover, the region where the Dirichlet series retains that positivity
shrinks before the critical limit \(\varepsilon\downarrow0\). Extending the
cocycle as a holomorphic or contractive function over the whole Cayley disc
reintroduces exactly the zero localization. Neither A1 nor RH is proved.

## 1. Internal non-duplication audit

A literal search over phases 1–104 for

```text
zeta(s-u)/zeta(s),  ζ(s-u)/ζ(s),  J_u,  Jordan totient
```

returns no occurrences. The first two jets and their representation do exist:

* E70.11 proves \(\mu*\log=\Lambda\) and
  \(Z^{-1}\delta Z=V_\Lambda\);
* E70.12 proves
  \(\mu*\log^2=\Lambda\log+\Lambda*\Lambda\);
* E83.004 realizes the first jet via truncated shifts;
* `104_12` obtains its Laguerre pullback and the degree convolution.

So the complete cocycle was not written in the repository, but its jets
\(k=1,2\) and the Euler–Gamma obstacle had already been identified. The
function \(J_k(n)=n^k\prod_{p\mid n}(1-p^{-k})\) is the classical Jordan totient;
for example, Moree–Saad Eddin–Sedunova–Suzuki, *Jordan totient quotients*,
[arXiv:1810.04742](https://arxiv.org/abs/1810.04742), uses that definition. No
bibliographic novelty is claimed for (1)–(4). The non-duplication claim is
purely internal and refers to the combination continuous cocycle–polar
pairing–Laguerre pullback.

## 2. Positive hierarchy theorem

For \(u\ge0\) and \(\Re s>1+u\), Möbius inversion gives

\[
 \boxed{
 A_u(s)={\zeta(s-u)\over\zeta(s)}
 =\sum_{m\ge1}{J_u(m)\over m^s},\qquad
 J_u(m)=\sum_{d\mid m}\mu(d)(m/d)^u.}
 \tag{1}
\]

If \(m=\prod_{p^a\parallel m}p^a\), then

\[
 J_u(m)=m^u\prod_{p\mid m}(1-p^{-u})
 =\prod_{p^a\parallel m}
   \left(e^{a u\log p}-e^{(a-1)u\log p}\right)\ge0.
 \tag{2}
\]

Moreover, each factor of (2) has a Taylor series with non-negative
coefficients, since its order-\(r\) coefficient is

\[
 { (a\log p)^r-((a-1)\log p)^r\over r!}\ge0.
 \tag{3}
\]

Multiplying the series gives, for every \(k\ge0\),

\[
 \boxed{
 j_k(m):=\left.\partial_u^kJ_u(m)\right|_{u=0}
 =\sum_{d\mid m}\mu(d)\log^k(m/d)
 =(\mu*\log^k)(m)\ge0.}
 \tag{4}
\]

For \(m>1\), the value is zero if \(k<\omega(m)\) and strictly positive if
\(k\ge\omega(m)\). In the region of absolute convergence,

\[
 D_k(s):=\left.\partial_u^kA_u(s)\right|_{u=0}
 ={(-1)^k\zeta^{(k)}(s)\over\zeta(s)}
 =\sum_{m\ge1}{j_k(m)\over m^s}\ge0.
 \tag{5}
\]

The cocycle also satisfies the exact law

\[
 A_{u+v}(s)=A_u(s)A_v(s-u).
 \tag{6}
\]

Equations (4)–(5) contain E70.11 at \(k=1\) and E70.12 at \(k=2\),
but now for all orders.

## 3. Pairing with the pole turns positivity into a difference

The polar model with the same shift is

\[
 A_u^0(s):={s-1\over s-u-1}.
 \tag{7}
\]

Setting \(F(s)=(s-1)\zeta(s)\), the paired quotient is

\[
 \boxed{
 H_u(s):={A_u(s)\over A_u^0(s)}
 ={F(s-u)\over F(s)}.}
 \tag{8}
\]

This is the normalization that does not separate two divergent quantities
at \(s=1\). Since

\[
 H_u(s)=\left(1-{u\over s-1}\right)A_u(s),
\]

its jets are

\[
 \boxed{
 Q_k(s):=\left.\partial_u^kH_u(s)\right|_{u=0}
 =D_k(s)-{k\over s-1}D_{k-1}(s)
 ={(-1)^kF^{(k)}(s)\over F(s)}.}
 \tag{9}
\]

Hence (4) gives no sign for the paired object: (9) subtracts two positive
series of the same critical order.

The loss is visible even at the regular point \(s=1\). With the convention

\[
 \zeta(1+t)={1\over t}+\sum_{r\ge0}{(-1)^r\gamma_r\over r!}t^r,
\]

one has

\[
 \boxed{Q_k(1)=-k\gamma_{k-1}.}
 \tag{10}
\]

The first four certified signs are

\[
 Q_1(1)<0,\qquad Q_2(1)>0,\qquad Q_3(1)>0,\qquad Q_4(1)<0.
 \tag{11}
\]

In particular, the pole–Euler quotient is neither completely monotone nor
absolutely monotone in the shift variable at the critical boundary. The
positivity of all the \(j_k(m)\) was consumed by the collision with the pole.

## 4. Exact Cayley–Laguerre pullback

Fix \(\varepsilon>0\) and

\[
 s_\varepsilon(z)=1+\varepsilon+{z\over1-z}.
 \tag{12}
\]

For \(0\le u<\varepsilon\) and \(z\) sufficiently small, the Laguerre
generating formula gives

\[
 {A_u(s_\varepsilon(z))\over1-z}
 =\sum_{n\ge0}\left\{
   \sum_{m\ge1}{J_u(m)\over m^{1+\varepsilon}}
          L_n(\log m)\right\}z^n.
 \tag{13}
\]

For the pole,

\[
 {A_u^0(s_\varepsilon(z))\over1-z}
 ={1\over1-z}+{u\over1-z}{1\over\varepsilon-u+z/(1-z)},
 \tag{14}
\]

and by

\[
 \int_0^\infty e^{-q x}L_n(x)\,dx
 ={(q-1)^n\over q^{n+1}},
\]

its degree-\(n\) coefficient is

\[
 1+u{(\varepsilon-u-1)^n\over(\varepsilon-u)^{n+1}}.
 \tag{15}
\]

Differentiating (13)–(15) at \(u=0\), and using that
\(A_0=A_0^0=H_0=1\), one obtains

\[
 \boxed{
 {1\over1-z}\left.\partial_uH_u(s_\varepsilon(z))\right|_{u=0}
 =\sum_{n\ge0}C_{n,\varepsilon}z^n,}
 \tag{16}
\]

where

\[
 \boxed{
 C_{n,\varepsilon}
 =\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}L_n(\log m)
 -{(\varepsilon-1)^n\over\varepsilon^{n+1}}.}
 \tag{17}
\]

This is exactly the regulated cost of `104_12`, equation (8). The complete
cocycle does not replace the gate: its first jet **is** the gate.

## 5. Rational stop-gate at degrees 1 and 6

The paired limit of (17) exists, and `103_59` proves

\[
 C_n:=\lim_{\varepsilon\downarrow0}C_{n,\varepsilon}
 =\lambda_n^{\rm prime}-\lambda_{n+1}^{\rm prime}.
 \tag{18}
\]

The verifier `tools/jordan_cocycle_sign_gate.py`, reusing the rational
intervals from Phase 102, certifies

\[
\begin{aligned}
 C_1&\in[-0.389669432061167636009309,
          -0.389669432061167636009308],\\
 C_6&\in[\phantom{-}0.008107486973374973910460,
          \phantom{-}0.008107486973374973910461].
\end{aligned}
\tag{19}
\]

Hence the first Cayley jet has both signs. This exactly refutes either
of the inferences

\[
 H_u(s)\le1\text{ on a real ray}
 \Longrightarrow [z^n](1-z)^{-1}\partial_uH_u|_0\le0,
\]

or the same arrow with the opposite sign. The pointwise order in \(s\) and
the coefficient-by-coefficient order after Cayley are different orders. The
oscillation does not first appear in an asymptotic bound: it is already
certified at degrees \(1\) and \(6\).

The inequality that M6 would need remains

\[
 C_n\le{1\over2}\Delta A_n,
 \tag{20}
\]

equivalent to the strong gate \(\Delta D_n\ge0\) of `103_59`. Neither (4),
nor a real inequality for (8), nor convexity in \(u\) implies (20) after the
signed extraction (16).

## 6. Structural falsifier with the full Jordan hierarchy

The loss of sign is not a numerical peculiarity of the first few degrees.
For \(a>0\), consider

\[
 X_a(s)=\xi(s+a)\xi(s-a).
 \tag{21}
\]

It is a real entire function and satisfies

\[
 X_a(1-s)=X_a(s).
 \tag{22}
\]

Every known zero \(\frac12+i\gamma\) of \(\xi\) produces zeros of \(X_a\) at
\(\frac12-a+i\gamma\) and \(\frac12+a+i\gamma\). Hence \(X_a\) has zeros off
its line of symmetry for every \(a>0\).

However, its Euler part

\[
 Z_a(s)=\zeta(s+a)\zeta(s-a)
\]

has strictly positive logarithmic weights:

\[
 -{Z_a'\over Z_a}(s)
 =\sum_{m\ge2}{2\Lambda(m)\cosh(a\log m)\over m^s},
 \tag{23}
\]

and its cocycle is the product of two Jordan cocycles,

\[
 {Z_a(s-u)\over Z_a(s)}=A_u(s+a)A_u(s-a).
 \tag{24}
\]

In \(\Re s>1+a+u\), the coefficient of \(r^{-s}\) in (24) is

\[
 \sum_{mn=r}J_u(m)J_u(n)m^{-a}n^a\ge0.
 \tag{25}
\]

The correct polar normalization does not break the example either. It is

\[
 A^0_{u,a}(s)=
 {s+a-1\over s+a-u-1}{s-a-1\over s-a-u-1}.
 \tag{26}
\]

With

\[
 F_a(s)=(s+a-1)(s-a-1)Z_a(s),
\]

the paired quotient is again

\[
 {Z_a(s-u)/Z_a(s)\over A^0_{u,a}(s)}
 ={F_a(s-u)\over F_a(s)}.
 \tag{27}
\]

Thus, **a complete Jordan hierarchy, positive Euler coefficients, positive
von Mangoldt weights, conjugation, and the functional equation** coexist
with off-line zeros. Any argument that uses only those properties would also
apply to \(X_a\) and is false. A mechanism valid for zeta must use an
additional quantitative property of the real weights
\(\Lambda(p^k)=\log p\), not merely their membership in the Jordan cone.

## 7. Completing with Gamma produces a criterion equivalent to RH

One could try to repair the missing Euler–Gamma comparison by passing to the
completed cocycle

\[
 \Theta_u(s):={\xi(s-u)\over\xi(s)}=K_u(s)H_u(s),
 \qquad
 K_u(s)={s-u\over s}\,\pi^{u/2}
 {\Gamma((s-u)/2)\over\Gamma(s/2)}.
 \tag{28}
\]

The completed factor does supply an exact geometry. On

\[
 \Re s={1+u\over2}
 \tag{29}
\]

one has \(s-u=1-\bar s\), and by the functional equation and the Schwarz
reflection,

\[
 \xi(s-u)=\xi(1-\bar s)=\xi(\bar s)=\overline{\xi(s)}.
 \tag{30}
\]

So \(|\Theta_u(s)|=1\) at the points where the quotient is defined (with a
removable extension at common zeros). But interior contractivity is not a
new inequality:

**Theorem (completed Schur gate).** For \(u>0\), let

\[
 {\cal H}_u=\{s:\Re s>(1+u)/2\}.
 \tag{31}
\]

RH implies that \(\Theta_u\) is holomorphic and
\(|\Theta_u(s)|\le1\) on \({\cal H}_u\), for every \(u>0\). Conversely, it
suffices that there exist a sequence \(u_j\downarrow0\) for which each
\(\Theta_{u_j}\) is holomorphic on \({\cal H}_{u_j}\). Then RH holds. Hence
the Schur property for the completed family is equivalent to RH.

**Proof of the RH direction.** Write

\[
 \Xi(w)=\xi(1/2+w),\qquad c=u/2,\qquad
 w=s-(1+u)/2.
\]

Under RH, the convergent even product is

\[
 \Xi(w)=\Xi(0)\prod_{\gamma>0}\left(1+{w^2\over\gamma^2}\right),
 \tag{32}
\]

with multiplicities. Moreover,

\[
 \Theta_u(s)={\Xi(w-c)\over\Xi(w+c)}
 =\prod_{\gamma>0}
 {w-c-i\gamma\over w+c-i\gamma}
 {w-c+i\gamma\over w+c+i\gamma}.
 \tag{33}
\]

If \(\Re w>0\), each factor has modulus at most one because

\[
 |w+c\mp i\gamma|^2-|w-c\mp i\gamma|^2
 =4c\Re w>0.
 \tag{34}
\]

The product gives the contractivity.

**Proof of the converse.** If \(\rho\) were a zero with
\(\Re\rho>1/2\), for every sufficiently large \(j\) one would have

\[
 0<u_j<2\Re\rho-1.
 \tag{35}
\]

If the pole at \(\rho\in{\cal H}_{u_j}\) canceled for all those indices,
then \(\xi(\rho-u_j)=0\) would give a sequence of distinct zeros accumulating
at \(\rho\), impossible for a nonzero entire function. For some \(j\),
\(\Theta_{u_j}\) has a pole in \({\cal H}_{u_j}\), a contradiction. There are
no zeros to the right of the critical line, and the symmetry
\(\rho\mapsto1-\bar\rho\) also excludes those to the left. \(\square\)

So adding exactly the Gamma factor missing in (9) restores boundary
unitarity, but the needed interior property already contains RH. Using it
to deduce A1 would be circular. The isolated Euler factor has coefficient
positivity with no boundary control; the completed factor has the correct
boundary, but its contractivity is the whole problem.

### 7.1. How far the non-circular radial bounds reach

The two pieces do admit separate bounds in the half-plane of convergence.
By (1),

\[
 |A_u(\sigma+it)|\le A_u(\sigma)
 \qquad(\sigma>1+u).
 \tag{36}
\]

Moreover, the equivalent form of \(K_u\) is

\[
 K_u(s)=\pi^{u/2}{\Gamma((s-u)/2+1)\over\Gamma(s/2+1)}
 ={\pi^{u/2}\over\Gamma(u/2)}
 \int_0^1x^{(s-u)/2}(1-x)^{u/2-1}\,dx,
 \tag{37}
\]

so that \(|K_u(\sigma+it)|\le K_u(\sigma)\) when
\(\sigma>u-2\). These are genuine inequalities and use no zeros.

They do not automatically give a bound for \(\Theta_u=K_uH_u\), because

\[
 H_u(s)=\left(1-{u\over s-1}\right)A_u(s)
 \tag{38}
\]

and, for \(\sigma>1+u\),

\[
 \left|1-{u\over\sigma-1+it}\right|
 \ge 1-{u\over\sigma-1}.
 \tag{39}
\]

The polar factor moves in the direction opposite to the radial comparison.
Another cancellation would be needed to combine (36)–(39); even if obtained
in the safe half-plane \(\Re s>1+u\), extending it up to \({\cal H}_u\)
would return to the Schur gate above.

### 7.2. The exact Gamma budget is again \(\Delta D_n\)

The half of the completion corresponding to the strong margin also leaves
no intermediate inequality. Define, as a germ at \(u=0\),

\[
 B_u(s)=H_u(s)K_u(s)^{1/2}.
 \tag{40}
\]

In the critical coordinate \(s=(1-z)^{-1}\), the generating identities of
the prime and archimedean parts are

\[
 \log{F((1-z)^{-1})\over F(1)}
   =\sum_{n\ge1}{\lambda_n^{\rm prime}\over n}z^n,
 \qquad
 \log{Q((1-z)^{-1})\over Q(1)}
   =\sum_{n\ge1}{A_n\over n}z^n,
\]

where \(Q=\xi/F\). Differentiating in \(z\) and multiplying by \(-(1-z)\)
turns each sequence into the negative of its first difference. Since
\((1-z)^{-1}\partial_u\{G(s-u)/G(s)\}_{u=0}=-sG'(s)/G(s)\), one obtains, for
\(n\ge1\),

\[
\begin{aligned}
 [z^n]{1\over1-z}\left.\partial_uH_u\right|_0
   &=C_n=-\Delta\lambda_n^{\rm prime},\\
 [z^n]{1\over1-z}\left.\partial_uK_u\right|_0
   &=-\Delta A_n.
\end{aligned}
\tag{41}
\]

Since \(H_0=K_0=1\), it follows exactly that

\[
 \boxed{
 [z^n]{1\over1-z}\left.\partial_uB_u\right|_0
 =C_n-{1\over2}\Delta A_n
 =-{1\over2}\Delta D_n.}
 \tag{42}
\]

So the coefficient-by-coefficient bound that M6 would need to close the
Gamma budget is literally \(\Delta D_n\ge0\), the same gate from
`103_59`. The square root in (40) is not a global positive
factorization: it is only the algebraic germ assigning half the archimedean
contribution. Schur contractivity also imposes no individual sign on the
coefficients of (42), and obtaining it globally in this case is already
equivalent to RH.

## 8. The positive domain does not reach the critical boundary

The positive arithmetic expansion (1) requires

\[
 \Re s>1+u.
\tag{43}
\]

At the center of (12), \(s=1+\varepsilon\); hence a fixed \(u>0\) is only
admissible while \(u<\varepsilon\). There is no fixed neighborhood in the
cocycle variable that preserves the positive representation as
\(\varepsilon\downarrow0\). The jets at \(u=0\) do exist for each
\(\varepsilon>0\), but passing to the boundary requires exactly the
pole–prime cancellation of (17), where the sign has already been lost.

Meromorphic continuation is likewise no free shortcut. At \(\varepsilon=0\),
a zero \(\rho\) of the denominator \(F(s)\) transforms to

\[
 z_\rho={\rho-1\over\rho}=1-{1\over\rho}.
\tag{44}
\]

And

\[
 |z_\rho|<1\quad\Longleftrightarrow\quad\Re\rho>{1\over2}.
\tag{45}
\]

For generic \(u\), \(F(\rho-u)\ne0\), so the pole does not cancel in
\(H_u\). In the regulator \(\varepsilon>0\), the point is

\[
 z_{\rho,\varepsilon}
 ={\rho-1-\varepsilon\over\rho-\varepsilon},
 \qquad
 |z_{\rho,\varepsilon}|<1
 \Longleftrightarrow
 \Re\rho>{1\over2}+\varepsilon.
\tag{46}
\]

Thus, a uniform holomorphic extension of the cocycle over the whole critical
disc excludes precisely the zeros to the right of the critical line. Using
that extension to justify a coefficient theorem would be circular.

## 9. Exact scope of the stop-gate

What is proved:

1. the arithmetic hierarchy \(\mu*\log^k\ge0\) for every \(k\);
2. its cocycle law and its exact Cayley–Laguerre pullback;
3. that pairing with the pole turns that positivity into the
   difference (9);
4. that the first jet coincides with \(C_{n,\varepsilon}\);
5. with rational arithmetic, that this jet has both signs;
6. that the Dirichlet positivity domain does not survive the critical
   limit;
7. that uniform holomorphy of the cocycle on the disc is exactly sensitive
   to off-line zeros;
8. that the full Jordan hierarchy and the functional equation admit the
   explicit falsifier \(X_a\);
9. that completing the cocycle produces a Schur family equivalent to RH,
   not an independent bound.

What is ruled out:

```text
J_u >= 0 / mu*log^k >= 0
    -> real order of the cocycle
    -> sign or coefficient-by-coefficient convexity in Cayley
    -> A1.
```

Not ruled out is every conceivable identity that uses several values of
\(u\) simultaneously, but to be a new mechanism it must produce (20) without
invoking holomorphy/contractivity on the disc and without restating the
same gate. The Jordan cocycle, by itself, is a positive coordinate on the
Euler side; it does not supply the Euler–Gamma comparison already missing
in E70.12.

## 10. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 jordan_cocycle_sign_gate.py
```

All the signs in (11) and (19) are decided with `Fraction` over outward
decimal intervals; no floating point is involved.
</content>
