# 106.06 — Global curvature identification and the exact remaining estimate

## Result

This document completes the normalization and limit bookkeeping after the
fixed-\(L\) summability theorem of 106.05.

Let

\[
L=2\log\lambda,\qquad
s=\frac12+iz,\qquad
\Xi(z)=\xi\left(\frac12+iz\right).
\tag{1}
\]

For the CCM finite model there are two spectral objects which must be kept
distinct.

1. \(D^{\mathrm q}_{L,N}\) is the \(2N\)-dimensional physical
   quotient operator used in 106.04--106.05.
2. \(D^{\mathrm{full}}_{L,N}\) is the CCM self-adjoint operator obtained
   by adjoining the unperturbed exterior Fourier lattice.

Their second-resolvent traces differ by a completely explicit tail. At fixed
\(L\) that tail tends to zero as \(N\to\infty\), so the cofinal scalar
limit of 106.05 is exactly the curvature of the continuum ground transform.
For a diagonal limit, however, the correct sufficient mesh condition is

\[
\boxed{\frac{N(L)}{L^2}\longrightarrow\infty.}
\tag{2}
\]

After this correction, the desired global trace identity is equivalent to one
affine-free ground/model estimate:

\[
\boxed{
\partial_z^2\log
\frac{\widehat\phi_L(z)}{\widehat k_L(z)}
\longrightarrow0
}
\tag{3}
\]

locally uniformly away from the real zeros of the denominator. Here
\(\phi_L\) is the selected continuum Weil ground state supplied by
106.05 and \(k_L\) is the explicit prolate model of CCM. CCM prove the
corresponding curvature convergence for \(k_L\) to \(\Xi\); they do
not prove (3) for the actual ground state. Suzuki's proposed global Fourier
limit also does not prove (3).

Thus the global limit has now been identified without a sign, scale or
regularization ambiguity. The remaining mathematical input is (3), or any
stronger estimate implying it.

## 1. Full determinant versus quotient determinant

Put

\[
d_k=\frac{2\pi k}{L}.
\tag{4}
\]

Let \(\phi_{L,N}\) be a finite simple-even least Ritz vector and
write its Fourier transform in the CCM normalization as

\[
\widehat\phi_{L,N}(z)
=2L^{-1/2}\sin\left(\frac{Lz}{2}\right)
\sum_{k=-N}^{N}\frac{(\phi_{L,N})_k}{z-d_k}.
\tag{5}
\]

CCM's regularized determinant is

\[
F_{L,N}(z)
=\det_{\mathrm{reg}}(D^{\mathrm{full}}_{L,N}-z)
=-i e^{-iLz/2}\widehat\phi_{L,N}(z).
\tag{6}
\]

The exponential in (6) is affine after taking a logarithm and therefore
disappears after two derivatives. If \(Q_{L,N}\) denotes the quotient
characteristic and \(E^{\mathrm{ext}}_{L,N}\) the exterior-lattice
factor, then, up to a nonzero constant,

\[
F_{L,N}(z)
=e^{-iLz/2}E^{\mathrm{ext}}_{L,N}(z)Q_{L,N}(z),
\tag{7}
\]

and

\[
\frac{E^{\mathrm{ext}}_{L,N}(z)}
     {E^{\mathrm{ext}}_{L,N}(0)}
=\prod_{k>N}\left(1-\frac{z^2}{d_k^2}\right).
\tag{8}
\]

Consequently

\[
\begin{aligned}
\tau^{\mathrm q}_{L,N}(z)
&:=\operatorname{Tr}(z-D^{\mathrm q}_{L,N})^{-2},\\
\tau^{\mathrm{full}}_{L,N}(z)
&:=\operatorname{Tr}(z-D^{\mathrm{full}}_{L,N})^{-2},\\
\tau^{\mathrm{full}}_{L,N}(z)
&=\tau^{\mathrm q}_{L,N}(z)
  +\sum_{|k|>N}\frac1{(z-d_k)^2},\\
(\log F_{L,N})''(z)
&=-\tau^{\mathrm{full}}_{L,N}(z).
\end{aligned}
\tag{9}
\]

These are ordinary trace identities: the second resolvent of the exterior
lattice is trace class.

### Lemma 1 — Exterior-mesh curvature

For each compact \(K\subset\mathbb C\) there are constants
\(C_K\) and \(N_K\) such that

\[
\sup_{z\in K}
\left|\sum_{|k|>N}\frac1{(z-d_k)^2}\right|
\le C_K\frac{L^2}{N}
\tag{10}
\]

whenever \(N\ge N_KL\).

### Proof

Let \(R=\sup_{z\in K}|z|\). Once \(d_N\ge2R\),
\(|z-d_k|\ge |d_k|/2\) for \(|k|>N\). Hence

\[
\sum_{|k|>N}\frac1{|z-d_k|^2}
\le\frac8{(2\pi/L)^2}\sum_{k>N}\frac1{k^2}
\le\frac{2L^2}{\pi^2N}.
\tag{11}
\]

This proves (10). \(\square\)

At fixed \(L\), (10) tends to zero along every cofinal sequence. For a
simultaneous limit it gives (2). The weaker condition
\(N(L)/L\to\infty\) only moves the first exterior node to infinity;
it does not make the total exterior curvature vanish.

## 2. The fixed-\(L\) limit is a ground-transform curvature

Choose one cofinal subsequence \(N_j\) as in Theorem 5 of 106.05, so that

\[
\phi_{L,N_j}\longrightarrow\phi_L
\quad\text{in }L^2([-L/2,L/2])
\tag{12}
\]

and the consecutive scalar trace differences are absolutely summable on
every compact subset of \(\mathbb C\setminus\mathbb R\). Compact
support turns (12) into locally uniform convergence, with all derivatives,

\[
\widehat\phi_{L,N_j}^{(r)}\longrightarrow
\widehat\phi_L^{(r)},\qquad r\ge0.
\tag{13}
\]

The finite transforms have only real zeros. Their nonzero locally uniform
limit therefore has no nonreal zero by Hurwitz. Combining (9), (10), and
(13) gives the exact fixed-\(L\) identity

\[
\boxed{
\tau_L(z)
:=\lim_{j\to\infty}\tau^{\mathrm q}_{L,N_j}(z)
=-\partial_z^2\log\widehat\phi_L(z)
}
\tag{14}
\]

locally uniformly on \(\mathbb C\setminus\mathbb R\).

Equation (14) identifies the sum constructed in 106.05; it is not merely a
subsequential abstract holomorphic function.

## 3. Exact conversion to the \(\xi\)-curvature

The chain rule applied to (1) gives

\[
\boxed{
\partial_z^2\log\Xi(z)
=-\left(\frac{\xi'}{\xi}\right)'
 \left(\frac12+iz\right).
}
\tag{15}
\]

If

\[
\Theta^{\mathrm{full}}_{L,N}
=\frac12+iD^{\mathrm{full}}_{L,N},
\tag{16}
\]

then \(s-\Theta^{\mathrm{full}}_{L,N}=i(z-D^{\mathrm{full}}_{L,N})\),
and therefore

\[
\operatorname{Tr}(s-\Theta^{\mathrm{full}}_{L,N})^{-2}
=-\tau^{\mathrm{full}}_{L,N}(z)
=(\log F_{L,N})''(z).
\tag{17}
\]

There is no missing sign or scale factor. The global trace target is exactly

\[
\boxed{
\operatorname{Tr}(s-\Theta_L)^{-2}
\longrightarrow
-\left(\frac{\xi'}{\xi}\right)'(s).
}
\tag{18}
\]

In the physical \(z\)-coordinate the same statement is
\(\tau_L(z)\to(\xi'/\xi)'(1/2+iz)\).

## 4. The CCM model and the affine-free global criterion

Let \(k_L\) be the explicit prolate model denoted \(k_\lambda\) in
CCM, with \(L=2\log\lambda\). CCM prove

\[
\widehat k_L\longrightarrow\Xi
\tag{19}
\]

locally uniformly on each closed substrip of
\(|\operatorname{Im}z|<1/2\). Thus, on compact sets avoiding the
zeros of \(\Xi\),

\[
\partial_z^2\log\widehat k_L
\longrightarrow
\partial_z^2\log\Xi.
\tag{20}
\]

Equations (14) and (20) imply the following exact reduction.

### Theorem 2 — Affine-free ground/model closure

Assume that a simple-even continuum ground state \(\phi_L\) is selected
for cofinally many \(L\). Then the desired global second-resolvent
identification (18) holds if and only if

\[
\partial_z^2\log
\left(\frac{\widehat\phi_L}{\widehat k_L}\right)
\longrightarrow0
\tag{21}
\]

locally uniformly on every simply connected compact set in the open strip
which avoids the zeros of the two transforms.

### Proof

On such a set choose compatible logarithms. The identity

\[
\partial_z^2\log\widehat\phi_L
-\partial_z^2\log\Xi
=\partial_z^2\log
 \left(\frac{\widehat\phi_L}{\widehat k_L}\right)
+\partial_z^2\log
 \left(\frac{\widehat k_L}{\Xi}\right)
\tag{22}
\]

is exact. The last term tends to zero by (19) and Cauchy's theorem. Hence
the first term tends to zero exactly when the first term on the right does.
Use (14)--(18) to translate the first term into the trace statement.
\(\square\)

Condition (21) is weaker than convergence of the ground transforms. It is
unchanged under the full admissible renormalization

\[
\widehat\phi_L(z)\mapsto e^{a_L+b_Lz}\widehat\phi_L(z).
\tag{23}
\]

If both the ground state and the model are even, the limiting affine freedom
reduces, after a consistent choice of logarithm, to a scalar normalization.

## 5. A quantitative sufficient estimate

The curvature criterion can be obtained from a relative holomorphic error
without differentiating noisy finite data.

### Lemma 3 — Relative-error transfer

Let \(K\) be compact and let \(K_r\) be its closed
\(r\)-neighborhood inside a zero-free domain. Put

\[
m_{L,K,r}:=\inf_{z\in K_r}|\widehat k_L(z)|,\qquad
\eta_{L,K,r}:=\sup_{z\in K_r}
|\c_L\widehat\phi_L(z)-\widehat k_L(z)|.
\tag{24}
\]

If \(\eta_{L,K,r}\le m_{L,K,r}/2\), then

\[
\sup_{z\in K}
\left|\partial_z^2\log
\frac{c_L\widehat\phi_L(z)}{\widehat k_L(z)}\right|
\le\frac{4}{r^2}
\frac{\eta_{L,K,r}}{m_{L,K,r}}.
\tag{25}
\]

### Proof

Write \(c_L\widehat\phi_L/\widehat k_L=1+h_L\). On
\(K_r\), \(|h_L|\le1/2\) and
\(|\log(1+h_L)|\le2|h_L|\). Cauchy's estimate for the second
derivative on disks of radius \(r\) gives (25). \(\square\)

Because (19) makes \(m_{L,K,r}\) uniformly positive on every compact
which avoids the zeros of \(\Xi\), locally uniform relative
ground/model convergence implies (21).

One source-side sufficient estimate is the weighted error already isolated
in E101.095:

\[
\sup_{|\beta|\le B}
\int_{\lambda^{-1}}^\lambda
|c_L\phi_L(u)-k_L(u)|u^\beta,d^*u
\longrightarrow0,\qquad B<\frac12.
\tag{26}
\]

Indeed, \(|u^{-iz}|=u^{\operatorname{Im}z}\), so (26) gives the
numerator in (24) uniformly on closed substrips. Condition (26) is stronger
than the curvature target (21); the latter is the minimal affine-invariant
statement needed by the second-resolvent route.

## 6. Prior-art boundary

The following ingredients belong to CCM:

- the semilocal Weil form and its compact-form operator at fixed \(L\);
- existence of a continuum least eigenvector;
- the finite self-adjoint perturbation and determinant formula (6);
- real-rootedness of every finite ground transform;
- construction of the explicit prolate model \(k_L\);
- the convergence (19);
- the explicit statement that comparison of \(k_L\) with the actual Weil
  ground state remains missing.

Suzuki proposes a global Fourier-transform limit and discusses an expected
strong-resolvent convergence; neither gives (21) for the CCM ground states.

The following statements are additions of Phase 106 relative to those two
sources:

- the canonical \(N\mapsto N+1\) quotient connections;
- the exact rank-two/Loewner intertwining defect;
- the fixed-\(L\) cofinal scalar summability theorem;
- the uniform fixed-\(L\) Weyl bound and dependent-shell theorem;
- the exact identification (14) of the sum with continuum-ground curvature;
- the full/quotient diagonal correction (2);
- the affine-free minimal criterion (21) and quantitative transfer (25).

The functional-analytic tools in the proofs are standard. The claims above
are novelty claims relative to the two audited papers, not an assertion of
worldwide priority without a broader literature search.

## 7. Binding frontier

The limit has now been reduced without ambiguity to

\[
\boxed{
\partial_z^2\log
\frac{\widehat\phi_L(z)}{\widehat k_L(z)}
\longrightarrow0.
}
\tag{27}
\]

Proving (27), (26), or a source-first estimate implying either would identify
the global summable limit with \(-(\xi'/\xi)'\). Since each finite
approximant has only real zeros, locally uniform determinant convergence
would then imply RH by Hurwitz. No result of CCM, Suzuki, or Phase 106 proves
(27) at present.

## Status

Proved here: the full/quotient curvature crosswalk; the exterior-tail bound;
the exact fixed-\(L\) ground-curvature identity; the sign-correct global
conversion; the affine-free equivalence; and the relative-error transfer
lemma.

Open and force-bearing: the actual ground/model curvature estimate (27).
