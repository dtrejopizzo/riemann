# 104_100 — Functional two-sheet average and completion-corrector gate

## Result

This document carries out the average of the two sheets of `104_98` using
simultaneously the functional equation, conjugation, and the exact Riemann
completion. The monodromy diagonal is effectively centered for
\(\log\xi\), but it **does not** transfer to the arithmetic energy of
\(\Phi_N\).

Set

\[
 C(s)={1\over2}s(s-1)\pi^{-s/2}\Gamma(s/2),
 \qquad \xi(s)=C(s)\zeta(s),                              \tag{1}
\]

and, with the compatible branches of `104_98`,

\[
 \begin{aligned}
 A(s)&=\sum_{k\ge2}{\mu(k)\over k}\log\zeta(ks)
       -E_1((s-1)\log2)+R(s),\\
 G(s)&=A(s)-\log C(s).
 \end{aligned}                                             \tag{2}
\]

Then, locally in \(\Re s>1/2\), away from the zeros,

\[
 \boxed{\Phi(s)=\log\xi(s)+G(s).}                          \tag{3}
\]

Let \(\rho=1/2+b+i\gamma\), \(b>0\), be a zero of multiplicity
\(m\), and pair it with \(1-\bar\rho=1/2-b+i\gamma\). Grant the
method its most favorable case: \(s_\gamma=1/2+i\gamma\) is not also
a critical zero, and the two banks of the symmetric cut are centered by
reflection. Then one can write

\[
 (\log\xi)_\pm(s_\gamma)=\ell_\gamma\pm\pi i m,
 \qquad \ell_\gamma\in\mathbb R.                          \tag{4}
\]

Without that concession, at any nonzero crossing of the cut one has the
more general form \((\log\xi)_\pm=\ell_0\pm\pi i m\), with
\(\ell_0\in\mathbb C\), and in (6) the term \(4\pi m\Im\ell_0\) additionally
survives, also with no sign imposed by the symmetries. The rest of the
document studies the more favorable normalization (4), where that second
indeterminate is entirely eliminated.

Therefore the sheets of the prime symbol are exactly

\[
 \Phi_\pm(s_\gamma)=\ell_\gamma+G(s_\gamma)\pm\pi i m,    \tag{5}
\]

and satisfy

\[
 \boxed{
 \begin{aligned}
 { |\Phi_+|^2+|\Phi_-|^2\over2}
   &=|\ell_\gamma+G(s_\gamma)|^2+\pi^2m^2,\\
 |\Phi_+|^2-|\Phi_-|^2
   &=4\pi m\,\Im G(s_\gamma).
 \end{aligned}}                                             \tag{6}
\]

Thus completion kills the signed part **within**
\(\log\xi\), but upon decompleting it reappears exactly as
\(\pm2\pi m\Im G\). The functional equation does not determine its sign.

There are two further exact obstructions.

1. The transformations \(s\mapsto1-s\), conjugation, and their composition
   preserve, rather than invert, the local monodromy character
   \(2\pi i m\). Consequently none of them delivers the opposite sheet of
   the physical continuation.
2. The real corrector is not a finite-energy perturbation. When
   \(s=1/2+it\),

   \[
   \log|C(s)|=-{\pi\over4}|t|+{7\over4}\log|t|+O(1),        \tag{7}
   \]

   while \(A(1/2+it)=O(\sqrt{|t|}+\log(2+|t|))\) on continuous
   branches. Consequently

   \[
   \Re G(1/2+it)={\pi\over4}|t|+O(\sqrt{|t|}+\log(2+|t|)), \tag{8}
   \]

   and

   \[
   \boxed{
   \int_T^{2T}\left|{G(1/2+it)\over1/2+it}\right|^2dt
      \ge \left({\pi^2\over16}+o(1)\right)T.}              \tag{9}
   \]

Hence one cannot subtract the corrector via the triangle inequality in the
Plancherel space of `104_98`: the gamma term and the completed term have
a macroscopic cancellation that must be preserved.

Finally an exact algebraic falsifier is given. There exists a family
with an exterior quartet, entire completion, functional equation, and
conjugation in which one of the two sheets cancels **exactly** while the
other duplicates the whole diagonal. This proves that the three
symmetries, even together, do not select the arithmetic sheet nor supply
the missing inequality.

**Verdict.** The functional two-sheet average does not prove subpolynomial
energy, Deep-\(\Lambda\), A1, or RH. The surviving term is
\(2\pi m\Im G(s_\gamma)\), and the corrector containing it has linear, not
finite, energy. Closing the route still requires a global arithmetic
estimate for the ordinary weights; the completion symmetry does not
replace it.

---

## 1. Exact decomposition of the prime symbol

Equation (7) of `104_98` states

\[
 \Phi(s)=\log\zeta(s)
 +\sum_{k\ge2}{\mu(k)\over k}\log\zeta(ks)
 -E_1((s-1)\log2)+R(s).                                  \tag{10}
\]

Since \(\log\zeta=\log\xi-\log C\), (10) is precisely (3).
In a disc containing neither \(0\), \(1\), gamma poles, nor another zero,
\(G\) is single-valued and holomorphic. All the right monodromy of \(\Phi\)
therefore lies in \(\log\xi\).

The functional equation and reality are

\[
 \xi(s)=\xi(1-s),\qquad
 \xi(\bar s)=\overline{\xi(s)}.                          \tag{11}
\]

If \(L=\log\xi\) is a local determination, then, modulo constants in
\(2\pi i\mathbb Z\),

\[
 L(1-s)=L(s),\qquad \overline{L(\bar s)}=L(s).             \tag{12}
\]

These equalities do not invert the monodromy. Indeed, around a
zero, write \(z=s-\rho\). The four relevant local coordinates are

\[
 \log z,\quad \log(-z),\quad
 \overline{\log\bar z},\quad
 \overline{\log(-\bar z)}.                               \tag{13}
\]

When \(z\) traces a positive loop, all four expressions gain
\(2\pi i\). In the last two cases, the orientation reversal caused by
conjugation is reversed again by conjugating the value. Hence the
group generated by (11) acts trivially on the monodromy character. Sheet
\(+\) and sheet \(-\) remain two distinct data; (11) does not average
them.

## 2. The symmetric quartet cut

The functional equation and conjugation force, together with \(\rho\), the
zeros

\[
 \bar\rho,\quad1-\rho,\quad1-\bar\rho.                    \tag{14}
\]

If \(s_\gamma\) is not another zero, in a neighborhood of the upper pair
one can factor

\[
 \xi(s)=\{(s-s_\gamma)^2-b^2\}^{m}H_\gamma(s),            \tag{15}
\]

where \(H_\gamma\) is holomorphic and nonzero. The symmetry
\(s\mapsto1-\bar s\) fixes \(s_\gamma\). In the most favorable cut
convention, the two traces are chosen conjugate and their midpoint is
real; this gives (4). If a critical zero occupies \(s_\gamma\), a
symmetric curve is routed through a nearby nonzero point on the critical
line. The general midpoint can have an imaginary part, but then the
additional signed term already recorded after (4) remains; the symmetry
does not fix its sign either.

Adding (2) at both banks gives (5), and expanding
\(|z\pm i d|^2=|z|^2+d^2\pm2d\Im z\) proves (6). Note
that no estimate was made here: the surviving signed residue is an
exact identity.

On the critical line one can also write, with real-type continuations,

\[
 \Phi(1-s)=\overline{\Phi(s)},\qquad s=1/2+it.             \tag{16}
\]

Therefore the functional average only produces

\[
 |\Phi(s)|^2
 =\left|{\Phi(s)+\Phi(1-s)\over2}\right|^2
 +\left|{\Phi(s)-\Phi(1-s)\over2}\right|^2.              \tag{17}
\]

This is the Pythagorean identity between real and imaginary part. Both
summands are positive, but (17) is a **lower decomposition** of the
energy, not a subpolynomial upper bound for it. Nor does it generate the
two banks of the same cut: it pairs the points \(t\) and \(-t\).

The same operation can be carried out before any limit, literally on the
ordinary weights. Since the coefficients of \(\Phi_N\) are real, define

\[
 S_N(s)={\Phi_N(s)+\Phi_N(1-s)\over2},\qquad
 T_N(s)={\Phi_N(s)-\Phi_N(1-s)\over2}.                    \tag{17a}
\]

If \(s=1/2+it\), then

\[
 S_N(s)=\Re\Phi_N(s),\qquad T_N(s)=i\Im\Phi_N(s),         \tag{17b}
\]

and the factorization of `104_98` becomes exactly

\[
 \sum_{m=2}^N{P_m^2\over m(m+1)}
 ={1\over2\pi}\int_{\mathbb R}
 { |S_N(1/2+it)|^2+|T_N(1/2+it)|^2\over t^2+1/4}\,dt.    \tag{17c}
\]

This is the full arithmetic average of two reflections. It contains no
new inequality: it is \(|z|^2=(\Re z)^2+(\Im z)^2\). Both \(S_N\) and
\(T_N\) are entire and single-valued, so neither possesses the
monodromy diagonal. That diagonal appears only when continuing the
infinite limit across its half-plane of convergence. Proving that it
survives uniformly across the prefixes would already be proving the
energy bound of `104_93`–`104_94`.

## 3. Exact falsifier within the symmetries

Set \(z=s-1/2\), choose \(b,\gamma>0\), and define

\[
 Q_{b,\gamma}(s)=
 -{\{(z-i\gamma)^2-b^2\}\{(z+i\gamma)^2-b^2\}
    \over b^2(4\gamma^2+b^2)}.                            \tag{18}
\]

This is an entire polynomial of real type and satisfies

\[
 Q_{b,\gamma}(1-s)=Q_{b,\gamma}(s),\qquad
 Q_{b,\gamma}(\bar s)=\overline{Q_{b,\gamma}(s)}.         \tag{19}
\]

Its zeros are exactly \(1/2\pm b\pm i\gamma\), and
\(Q_{b,\gamma}(s_\gamma)=-1\). For \(X=Q_{b,\gamma}^{m}\),
the two symmetric branches of \(L=\log X\) at the midpoint are

\[
 L_\pm(s_\gamma)=\pm\pi i m.                             \tag{20}
\]

Now, for \(c\in\mathbb R\), set

\[
 \Phi_c(s)=L(s)+c(s-1/2),\qquad G_c(s)=c(s-1/2).           \tag{21}
\]

Subtracting \(G_c\) exactly completes \(\Phi_c\) into the function \(L\),
which satisfies (19). The corrector is entire and of real type, but it
is antisymmetric under \(s\mapsto1-s\), as the part removed by a
completion can be. At \(s_\gamma\),

\[
 (\Phi_c)_\pm=i(c\gamma\pm\pi m).                         \tag{22}
\]

With \(c=-\pi m/\gamma\),

\[
 (\Phi_c)_+=0,
 \qquad
 (\Phi_c)_-=-2\pi i m.                                   \tag{23}
\]

The average diagonal is positive, but one sheet retains no positive
fraction of it at all. Flipping the sign of \(c\) swaps the sheets. This
falsifier does not aim to preserve the ordinary Mangoldt weights; it
proves exactly that **functional equation + conjugation +
completion** do not suffice to pick the sign in (6). The literal weights
remain the additional input that would be needed.

## 4. The Riemann corrector has macroscopic energy

Stirling's formula, uniform on the line \(\Re s=1/2\), gives

\[
 \log\left|\Gamma\left({1\over4}+{it\over2}\right)\right|
 =-{\pi\over4}|t|-{1\over4}\log|t|+O(1).                 \tag{24}
\]

Since \(|s(s-1)|=t^2+O(1)\), substituting (24) into (1) proves (7).

It remains to check that the other terms of (2) hide no other linear
term. For the discretized residue of `104_98`, at
\(s=1/2+it\),

\[
 \left|\int_{m-1}^{m}{x^{-s}-m^{-s}\over\log x}\,dx\right|
 \ll \min\left\{{m^{-1/2}\over\log m},
                 {|s|m^{-3/2}\over\log m}\right\}.      \tag{25}
\]

Splitting the sum into \(m\le |s|\) and \(m>|s|\) gives

\[
 R(1/2+it)=O(\sqrt{|t|}).                                 \tag{26}
\]

The \(k\ge3\) block of (2) is uniformly bounded. At \(k=2\), classical
estimates for \(\zeta(1+2it)\), together with a continuous branch,
give \(\log\zeta(1+2it)=O(\log(2+|t|))\). Finally,
\(E_1((-1/2+it)\log2)=O(1/|t|)\) on the principal branch; any compatible
branch only adds a constant. This proves the stated bound
for \(A\), and (7) implies (8).

From (8), uniformly for \(T\le t\le2T\),

\[
 { |G(1/2+it)|^2\over t^2+1/4}
 \ge {\{\Re G(1/2+it)\}^2\over t^2+1/4}
 ={\pi^2\over16}+o(1).                                   \tag{27}
\]

Integrating proves (9). This is the decisive loss: the finite energy of
the proper powers of `104_94` does not mean that the **logarithmic
completion corrector** is finite. The gamma factor is linear in
\(|t|\), and it only cancels if all the terms are kept together.

## 5. Why BSY and Weil do not close either

### 5.1 BSY

In the disc coordinate of `104_89`,

\[
 w(s)={s-1\over s},\qquad w(1-s)={1\over w(s)}.           \tag{28}
\]

A right zero gives \(|w(\rho)|<1\); its functional reflection lies in
the exterior reciprocal. Poisson–Jensen counts the interior zero
one-sidedly and produces

\[
 D_B=\sum_{\Re\rho>1/2}m_\rho\log{1\over|w(\rho)|}.       \tag{29}
\]

Averaging the interior point with its exterior reciprocal would cancel
the deficit only by introducing a pole or an exterior factor that is no
longer a zero-free Euler truncation analytic in the disc. Hence (28) does
not control the one-sided leak of `104_89`; it simply rewrites the same
Blaschke factor.

### 5.2 Weil and Li

Grouping a quartet by functional equation and conjugation was already
done in `103_65`. If

\[
 1-{1\over\rho}=e^{-a+i\theta},\qquad a>0,
\]

its contribution to \(2\lambda_n\) is

\[
 8-8\cosh(na)\cos(n\theta).                              \tag{30}
\]

The factor \(\cosh(na)\cos(n\theta)\) has both signs. This is the
discrete version of the signed term in (6). Raising the sheet average to
positivity for all test functions would be precisely Weil positivity,
equivalent to RH; it is not an additional consequence of (11).

## 6. Exact scope of the no-go

The document proves three limited and rigorous claims:

1. the functional symmetries do not swap the two local determinations;
2. even after centering \(\log\xi\), exactly
   \(2\pi m\Im G\) remains in one sheet of the prime symbol;
3. \(G\) cannot be discarded as a finite perturbation in the energy of
   `104_98`.

It is not claimed that every two-sheet arithmetic inequality is
impossible. A new estimate that simultaneously uses all the ordinary
weights could control the cancellation between \(\log\xi\) and \(G\);
proving it would be precisely the energy theorem equivalent to RH of
`104_93`–`104_94`.

## 7. Reproduction

From `tools/`:

```bash
python3 functional_two_sheet_completion_check.py
```

The checker:

1. verifies that the four local actions of (13) have the same
   monodromy;
2. checks the two-sheet identities (6) and the finite arithmetic
   average (17a)–(17c);
3. verifies the symmetries, the quartet, and the exact cancellation
   (18)–(23);
4. evaluates by Stirling the coefficient \(-\pi/4\) and the term
   \((7/4)\log t\) of (7).

The numerical evaluations only check the algebra and the asymptotics
already proved; they do not constitute evidence for RH.
</content>
