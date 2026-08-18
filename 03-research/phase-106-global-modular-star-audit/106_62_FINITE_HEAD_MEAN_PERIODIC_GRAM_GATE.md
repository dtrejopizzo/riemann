# 106.62 — The finite-head mean-periodic Gram gate

## Purpose

After exact radical shorting, it is natural to ask whether the continuous
Gamma channel, possibly supplemented by finitely many literal low
prime-power atoms, already has the sharp spectral floor on the
mean-periodic complement.  This note performs the semantic check, derives
the exact constrained Gram kernel, and tests the first candidate heads.

There are two distinct conclusions.

1.  The sign change of the translation-invariant archimedean multiplier at
    (r_0=6.2898\ldots<\gamma _1) does **not** imply the Gamma-channel
    Poincare estimate after the Doob transform.  The two spectral variables
    are different, and the Gamma-only estimate is already falsified by a
    four-mode complement vector at diagnostic precision.
2.  Adding the first few prime powers repairs every small zero span, but the
    minimum moves below the threshold when the span is enlarged.  The next
    literal atom then repairs the new direction.  Thus the observed finite
    head is a moving, atomwise phenomenon of the same type as 106.20 and
    106.32, not a proved finite reduction.

The exact formulas below are the reusable result.  The numerical rows are
diagnostic and are not interval certificates.

## 1. Semantic audit

The closest earlier constructions are the following.

* Phase 15, M4.1 studies the translation-invariant archimedean Weil form
  
  \[
  A_\infty(f,f)=\frac1{2\pi}\int_{\mathbb R}
  |\widehat f(t)|^2\Psi(t)\,dt,
  \qquad
  \Psi(t)=\mathrm{Re}\,\psi\!\left(\frac14+\frac{it}2\right)
  -\log\pi .                                           \tag{1}
  \]

  It proves that \(\Psi\) is positive for \(|t|>r_0\), where
  \(r_0=6.2898359888\ldots\).
* Document 106.20 already warns that high-frequency Gamma coercivity does
  not control the moving near-radical cluster.
* Document 106.32 proves that every von Mangoldt atom is load-bearing for
  the unshorted sharp inequality.
* Document 106.43 identifies the exact shorted complement with
  \((hq)*K=0\).

None of those documents proves or refutes a finite-head floor on the exact
complement.  The attack in this note is therefore not a duplicate.  The
M4.1 multiplier, however, cannot be imported as a proof of it.

## 2. Why the M4.1 support argument does not transfer

Put

\[
 h(x)=\cosh(x/2),\qquad c_K=\frac12,
 \qquad \chi_z(x)=\frac{\cos(zx)}{h(x)}.              \tag{2}
\]

If \(z\) is a zero of \(\Xi\), then

\[
 F_z=h\chi_z=\cos(zx),\qquad F_z*K=0.                 \tag{3}
\]

Thus it is \(F_z\), not the physical Weil test

\[
 f_z=K\chi_z=\frac K h\cos(zx),                       \tag{4}
\]

whose mean-periodic spectrum is concentrated at \(\{\pm z\}\).  If

\[
 \Phi(\zeta)=\widehat{K/h}(\zeta),                    \tag{5}
\]

then, up to the fixed Fourier normalization,

\[
 \boxed{
 \widehat f_z(t)=\frac12\{\Phi(t-z)+\Phi(t+z)\}.}     \tag{6}
\]

The function in (6) is entire.  Since \(f_z\ne0\), it cannot vanish on
the open interval \((-r_0,r_0)\); otherwise the identity theorem and
Fourier injectivity would give \(f_z=0\).  Therefore the zero-free gap
\(|z|\ge\gamma_1>r_0\) does not put \(\widehat f_z\) in the positive
spectral region of (1).

There is a second mismatch.  The Gamma Doob energy is the Picone
difference between two archimedean expressions, not merely
\(A_\infty(Kq,Kq)\).  The ground-state subtraction contains
\(K|q|^2\) and is not diagonalized by the point support of
\(\widehat{hq}\).  Consequently the scalar sign of \(\Psi\) cannot prove
the desired Poincare constant.

This is an exact obstruction to the proposed M4.1 shortcut.

## 3. Exact Hermitian Gram kernel on the zero divisor

Let \(S\) be a set of prime powers and put

\[
 d\nu_S(u)=\frac{e^{-u/2}}{1-e^{-2u}}\,du
 +\sum_{m\in S}\frac{\Lambda(m)}{\sqrt m}
 \delta_{\log m}(du).                                \tag{7}
\]

For complex \(z,w\), define

\[
\begin{aligned}
 \mathcal N(z,w)
 &=\frac1{c_K}\int_{\mathbb R}\frac{K(x)}{h(x)}
     \cos(\overline z x)\cos(wx)\,dx,\\
 \mathcal G_S(z,w)
 &=\int_{(0,\infty)}\!\int_{\mathbb R}
 K(x)K(x-u)\,
 \overline{\Delta_u\chi_z(x)}\,
 \Delta_u\chi_w(x)\,dx\,d\nu_S(u),\\
 \mathcal H_S(z,w)&=\mathcal G_S(z,w)-\frac12\mathcal N(z,w),
 \qquad
 \Delta_u\chi_z(x)=\chi_z(x)-\chi_z(x-u).
                                                               \tag{8}
\end{aligned}
\]

All three kernels are entire in \(w\), anti-entire in \(z\), and
Hermitian.  Moreover, with

\[
 \Phi_0(\zeta)=\int_{\mathbb R}\frac{K(x)}{h(x)}
 \cos(\zeta x)\,dx,
\]

the norm kernel has the closed form

\[
 \boxed{
 \mathcal N(z,w)=\frac1{2c_K}
 \{\Phi_0(w-\overline z)+\Phi_0(w+\overline z)\}.}   \tag{9}
\]

### Theorem 1 — Finite spectral-synthesis criterion

Let \(z_1,\ldots,z_d\) be zeros of \(\Xi\), repeated according to the
jets required by their multiplicities, and put

\[
 q=\sum_{j=1}^d a_j\chi_{z_j}.                       \tag{10}
\]

Then \(q\perp1\oplus\mathcal R\), and

\[
 \boxed{
 \mathscr E_S(q)-\frac12\|q\|_{L^2(\mu_K)}^2
 =\sum_{i,j=1}^d\overline{a_i}a_j
 \mathcal H_S(z_i,z_j).}                            \tag{11}
\]

For a zero of multiplicity \(m\), the corresponding rows and columns are
the derivatives
\(\partial_{\overline z}^k\partial_w^\ell\mathcal H_S(z,w)\),
\(0\le k,\ell<m\).

#### Proof

The zero identity gives

\[
 \int\chi_z\,d\mu_K
 =c_K^{-1}\int K(x)\cos(zx)\,dx
 =c_K^{-1}\Xi(z)=0.                                 \tag{12}
\]

Likewise, for every \(j\ge0\),

\[
 \langle\chi_z,K^{(2j)}/K\rangle_{L^2(\mu_K)}
 =c_K^{-1}(-1)^j\overline z^{,2j}\Xi(\overline z)=0. \tag{13}
\]

Thus (10) belongs to the exact complement.  Expanding its norm and every
jump square in the coefficients \(a_j\) gives (11).  Differentiation in
the zero parameter gives the standard polynomial-exponential jets at a
multiple zero.  Absolute convergence follows from the double-exponential
decay of \(K\).  \(\square\)

Consequently, a finite head has the sharp floor on the finite
mean-periodic synthesis space if and only if every matrix

\[
 \boxed{[\mathcal H_S(z_i,z_j)]_{i,j=1}^d\succeq0}   \tag{14}
\]

on the zero divisor and all its multiplicity jets.  If exponential
spectral synthesis is dense in the full mean-periodic form domain, (14)
is also sufficient for the complete floor.  That density in the required
form norm is a separate theorem and is not assumed here.

Formula (14) is the exact finite-head target.  In particular, scalar
one-zero estimates do not suffice: the obstruction can first appear in a
higher Gram determinant.  Nor is \(\mathcal H_S\) automatically a Pick or
de Branges kernel; such a representation would itself prove (14).

## 4. Gamma-only obstruction

Use the first four rigorously located real zeros

\[
 \gamma_1,\gamma_2,\gamma_3,\gamma_4
 =14.134725\ldots,21.022039\ldots,
 25.010857\ldots,30.424876\ldots                       \tag{15}
\]

and the particularly simple vector

\[
 q_4(x)=\frac{
 \cos(\gamma_1x)-2\cos(\gamma_2x)
 +2\cos(\gamma_3x)-\cos(\gamma_4x)}{h(x)}.           \tag{16}
\]

Equations (12)--(13) prove **exactly**, without a numerical projection,
that \(q_4\perp1\oplus\mathcal R\).  Direct evaluation of the two
absolutely convergent theta/Gamma integrals gives, in double precision,

\[
 \|q_4\|^2=0.8840058566\ldots,\qquad
 \mathscr E_\Gamma(q_4)=0.432237\ldots,               \tag{17}
\]

and hence

\[
 \frac{\mathscr E_\Gamma(q_4)}{\|q_4\|^2}
 =0.488953\ldots<\frac12.                            \tag{18}
\]

The value is stable as the mesh is refined from \(0.004\) to
\(0.00025\), with the quotient moving from (0.488918) to (0.488953).
This is decisive diagnostic evidence against the Gamma-only conjecture.
To promote (18) to a computer-assisted theorem, the theta truncation,
the \(x,u\) tails and the quadrature must still be enclosed by outward
intervals.  The margin in (17) is about \(9.7\times10^{-3}\) in the
unnormalized defect, so that certification is a finite task; it is not
claimed completed in this note.

## 5. Why the first finite head looked successful

The weighted-QR calculation avoids inversion of the increasingly
ill-conditioned raw cosine Gram matrix.  At mesh (5\times10^{-4}), the
head containing Gamma and the atoms (2,3,4,5) gives

\[
\begin{array}{c|cccccc}
\text{number of real zero modes}&10&15&20&25&30&40\\ \hline
\lambda_{\min}&
0.50287&0.50020&0.50000&0.49998&0.49996&0.49987.
\end{array}                                           \tag{19}
\]

The rows below (1/2) move toward the threshold under mesh refinement,
so (19) alone is not a proof of failure.  Enlarging the span to 50--60
modes, however, makes the head-(5) deficit visible, while adding the atom
(7) repairs that direction to within the new discretization margin.
This is precisely the moving-load-bearing pattern:

\[
 \boxed{
 \text{larger zero span}\ \longrightarrow\
 \text{new near-threshold direction}\ \longrightarrow\
 \text{next literal prime atom becomes active}.}     \tag{20}
\]

Thus no fixed finite head has been validated.  Any proof that one exists
must establish the full matrix positivity (14), uniformly in the number
of zero modes and in hypothetical nonreal zero quartets.  Conversely, one
certified negative principal matrix is a complete falsifier for that head.

## 6. Reproduction and status

Run

```bash
cd 03-research/phase-106-global-modular-star-audit
python3 tools/finite_head_mean_periodic_gram.py --span 50 --heads 1,2,3,4,5,7
```

The calculation uses only NumPy and is explicitly labelled diagnostic.

The exact gain of this note is the kernel criterion (8)--(14) and the
proof that the Phase-15 multiplier support argument acts in the wrong
coordinate.  Gamma alone is numerically falsified by an exact complement
vector.  A fixed finite prime head is neither proved nor rigorously
falsified here; the diagnostic instead shows the same moving atomwise
criticality already seen before radical shorting.
