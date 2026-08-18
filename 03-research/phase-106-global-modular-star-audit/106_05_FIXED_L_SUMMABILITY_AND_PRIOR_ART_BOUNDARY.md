# 106.05 — Fixed-\(L\) summability and the prior-art boundary

## Result

This document separates three statements which must not be conflated.

1. The finite Weil matrices, their shifted radical quotients and the finite
   self-adjoint operators are due to Connes--Consani--Moscovici (CCM).
2. The consecutive radical connection of 106.03 and the exact
   transport--shell calculation of 106.04 do not occur in CCM or in Suzuki.
3. At fixed \(L\), scalar second-resolvent summability is proved on a cofinal
   subsequence. For consecutive Fourier cutoffs it follows from one explicit
   gap--drop series. The new-mode shell is not an independent obligation:
   once the transported resolvent defect is summable, shell summability follows
   from a uniform Weyl bound and an exact Hilbert--Schmidt identity.

The cofinal-subsequence theorem requires no rate estimate, but it retains the
same cofinal finite simple-even/source-overlap hypothesis as the quotient
construction. It does not identify the subsequent \(L\to\infty\) limit with
the divisor of \(\Xi\). That identification remains the global force-bearing
step.

## 1. What is and is not in the two source papers

CCM construct the restrictions \(W_N\) of the semilocal Weil form, prove the
rank-two commutator with the periodic derivative, shift by the least Ritz
value, quotient by the resulting radical, and construct the finite
self-adjoint rank-one perturbation. See their
[Section 5.1](https://arxiv.org/html/2511.22755v1#S5.SS1),
[equation (5.3)](https://arxiv.org/html/2511.22755v1#S5.E3),
[Lemma 5.4](https://arxiv.org/html/2511.22755v1#S5.Thmtheorem4), and
[Theorem 5.10](https://arxiv.org/html/2511.22755v1#S5.Thmtheorem10).
Their Section 7 proposes the two limits \(N\to\infty\) and then
\(\lambda\to\infty\); it does not contain the consecutive-cutoff estimates
proved in 106.04.

Suzuki constructs the continuous localized operator \(A_a\), proves several
finite-\(a\) statements and formulates the Fourier-transform limit in his
[equation (1.2)](https://arxiv.org/html/2606.09096v1#S1.E2). The strong
resolvent convergence in
[Section 7.5](https://arxiv.org/html/2606.09096v1#S7.SS5) is explicitly
described as expected and is discussed there under RH. The embedding in
[Section 7.6](https://arxiv.org/html/2606.09096v1#S7.SS6) is not a discrete
\(N\mapsto N+1\) transport.

The following objects were not found in either source:

\[
\begin{gathered}
\Delta_N,\quad
j_N=C_N(S_N+\Delta_NI)^{-1/2}S_N^{1/2},\quad
\mathcal R_N=D_{N+1}j_N-j_ND_N,\\
\text{the rank-two factorization of }D_{N+1}C_N-C_ND_N,\quad
\text{the Loewner formula for }[D_N,B_N],\\
\text{the ground-rotation identity, the consecutive arrowhead equation,}
\quad\text{and the new-mode shell identity.}
\end{gathered}
\tag{1}
\]

The divided-difference and resolvent tools used to derive them are standard.
The source-specific application and the complete package (1) are new relative
to the two audited papers. No claim of worldwide priority is made without a
broader literature gate.

## 2. Scalar characteristic identity

Fix \(L\), put \(c_L=2\pi/L\), and let \(\phi_N\) be an \(L^2\)-unit
least Ritz vector of \(W_N\), at a level where the ground state is simple and
has nonzero source overlap. Its scalar normalization is irrelevant below.
Write

\[
\mathcal C_N(s)
=\sum_{k=-N}^{N}\frac{(\phi_N)_k}{s-c_Lk},
\qquad s\in\mathbb C\setminus\mathbb R.
\tag{2}
\]

Let \(D_N\) be the physical quotient operator of 106.04 and set

\[
\tau_N(s)=\operatorname{Tr}(s-D_N)^{-2}.
\tag{3}
\]

### Theorem 1 — Exact Cauchy-transform formula

\[
\boxed{
\tau_N(s)
=\sum_{k=-N}^{N}\frac1{(s-c_Lk)^2}
-\bigl(\log\mathcal C_N(s)\bigr)'' .
}
\tag{4}
\]

### Proof

It is enough first to use the dimensionless diagonal operator
\(D_0e_k=ke_k\). Normalize \(\xi_N\) by
\(\langle\eta_N,\xi_N\rangle=1\), and put

\[
D'_N=D_0-|D_0\xi_N\rangle\langle\eta_N|.
\tag{5}
\]

The matrix determinant lemma gives

\[
\begin{aligned}
\det(s-D'_N)
&=\prod_{k=-N}^{N}(s-k)
 \left(1+\sum_{k=-N}^{N}\frac{k(\xi_N)_k}{s-k}\right)\\
&=s\prod_{k=-N}^{N}(s-k)
  \sum_{k=-N}^{N}\frac{(\xi_N)_k}{s-k}.
\end{aligned}
\tag{6}
\]

The factor \(s\) is the radical eigenvalue and is removed on the quotient.
Multiplying \(\xi_N\) by a nonzero scalar does not change the second
logarithmic derivative. Rescaling \(s\mapsto s/c_L\) and differentiating
\(-\log\det(s-D_N)\) twice proves (4). \(\square\)

Finite self-adjointness implies that \(\mathcal C_N\) has no zero off the real
axis. Formula (4) is therefore holomorphic on each compact subset of
\(\mathbb C\setminus\mathbb R\).

## 3. A sufficient consecutive rate

Let

\[
\Delta_N=\varepsilon_N-\varepsilon_{N+1}\ge0,
\qquad
g_{N+1}=\lambda_2(W_{N+1})-\varepsilon_{N+1}>0,
\tag{7}
\]

where \(\lambda_2\) is the second eigenvalue, counting multiplicity. Choose
the phase of \(\phi_{N+1}\) so that
\(\langle I_N\phi_N,\phi_{N+1}\rangle\ge0\).

### Lemma 2 — Ground-line rotation

\[
\boxed{
\|I_N\phi_N-\phi_{N+1}\|^2
\le \frac{2\Delta_N}{g_{N+1}}.
}
\tag{8}
\]

### Proof

Write \(I_N\phi_N=a\phi_{N+1}+h\), with
\(a\ge0\) and \(h\perp\phi_{N+1}\). Principal compression gives

\[
\varepsilon_N
=\langle W_{N+1}I_N\phi_N,I_N\phi_N\rangle
\ge\varepsilon_{N+1}+g_{N+1}\|h\|^2.
\tag{9}
\]

Thus \(\|h\|^2\le\Delta_N/g_{N+1}\). Since
\(a^2+\|h\|^2=1\) and \(1-a\le1-a^2\),

\[
\|I_N\phi_N-\phi_{N+1}\|^2
=2(1-a)\le2\|h\|^2,
\tag{10}
\]

which proves (8). \(\square\)

### Theorem 3 — Consecutive scalar summability criterion

If

\[
\boxed{
\sum_{N\ge N_0}\sqrt{\frac{\Delta_N}{g_{N+1}}}<\infty,
}
\tag{11}
\]

then, for every compact \(K\Subset\mathbb C\setminus\mathbb R\),

\[
\boxed{
\sum_{N\ge N_0}
\sup_{s\in K}|\tau_{N+1}(s)-\tau_N(s)|<\infty.
}
\tag{12}
\]

### Proof

For \(j=0,1,2\), the vectors

\[
\left(\frac{d^j}{ds^j}\frac1{s-c_Lk}\right)_{k\in\mathbb Z}
\tag{13}
\]

belong to \(\ell^2(\mathbb Z)\), uniformly for \(s\in K\). Equations
(8) and (11) therefore imply

\[
\sum_N
\|\mathcal C_{N+1}-\mathcal C_N\|_{C^2(K)}<\infty.
\tag{14}
\]

The nonzero limit \(\mathcal C\) is zero-free off the real axis by Hurwitz.
After deleting finitely many indices, \(\inf_K|\mathcal C_N|>0\); hence the
map \(f\mapsto(\log f)''\) is Lipschitz on the bounded subset in (14).
The two new lattice terms are \(O_K(N^{-2})\). Formula (4) now proves
(12). \(\square\)

CCM's monotone Ritz theorem gives

\[
\sum_N\Delta_N
=\varepsilon_{N_0}-\inf\operatorname{Spec}A_L<\infty,
\tag{15}
\]

but (15) alone does not imply (11). Thus (11) is an explicit sufficient
adjacent-cutoff rate. It is not necessary: direct bounded variation of the
Cauchy transforms can in principle hold even if (11) fails.

### Proposition 4 — Compactness and a limiting gap do not imply (11)

There is a closed positive quadratic form with compact form embedding, a
simple ground state, a positive limiting spectral gap and nested coordinate
cores for which

\[
\Delta_N\asymp N^{-2},
\qquad
g_N\ge g>0,
\qquad
\sum_N\sqrt{\Delta_N/g_N}=\infty.
\tag{15a}
\]

### Proof

On \(\mathcal H=\mathbb C\oplus\ell^2(\mathbb N)\), put

\[
q(x)=\sum_{n\ge1}n\,|x_n-n^{-3/2}x_0|^2.
\tag{15b}
\]

Its form embedding is compact: the \(x_0\)-direction is finite-dimensional,
while on \(x_0=0\) the form controls
\(\sum n|x_n|^2\). Its kernel is the simple line generated by
\(\xi=(1,n^{-3/2})\), and compactness gives a positive gap above that line.

Restrict \(q\) to the coordinates \(0,1,\ldots,N\). If \(\varepsilon_N\)
is its least Ritz value, the eigenvalue equations eliminate \(x_1,\ldots,x_N\)
and give exactly

\[
t_N=\varepsilon_N\left(
1+\sum_{n\le N}\frac1{n^2(n-\varepsilon_N)}
\right),
\qquad
t_N=\sum_{n>N}\frac1{n^2}.
\tag{15c}
\]

Hence

\[
\varepsilon_N\sim\frac1{(1+\zeta(3))N},
\qquad
\Delta_N=\varepsilon_N-\varepsilon_{N+1}
\sim\frac1{(1+\zeta(3))N^2}.
\tag{15d}
\]

This proves (15a). \(\square\)

Thus (11) must come from additional regularity of the actual Gamma--Euler
ground state, not from abstract Galerkin convergence. For example, a
source-specific Ritz error

\[
\varepsilon_N-\inf\operatorname{Spec}A_L
=O(N^{-p}\log N),\qquad p>1,
\tag{15e}
\]

together with a limiting positive gap would imply (11) by summation by
parts and Cauchy--Schwarz. Neither CCM nor Suzuki proves such a polynomial
ground-state approximation rate.

## 4. Rate-free cofinal-subsequence summability

The adjacent rate (11) is not needed to obtain a summable cofinal sequence.

### Theorem 5 — Fixed-\(L\) cofinal summability

Assume the finite quotient is defined on a cofinal set of levels (in
particular, the selected least Ritz vector has the required simple-even
property and nonzero source overlap). Then there is a cofinal sequence
\(N_j\to\infty\) such that, for every compact
\(K\Subset\mathbb C\setminus\mathbb R\),

\[
\boxed{
\sum_j\sup_{s\in K}
|\tau_{N_{j+1}}(s)-\tau_{N_j}(s)|<\infty.
}
\tag{16}
\]

### Proof

The unit Ritz vectors have uniformly bounded shifted form norm because their
Rayleigh values decrease to the lower bound of the closed semilocal Weil
form. CCM's compact form embedding makes them precompact in \(L^2\). Choose
a subsequence and coherent phases such that

\[
\phi_{N_j}\longrightarrow\phi,
\qquad
\|\phi_{N_j}-\phi\|_2\le2^{-j-2}.
\tag{17}
\]

The limit has norm one. Lower semicontinuity of the closed form and the Ritz
limit give

\[
\inf\operatorname{Spec}A_L
\le QW_L(\phi)
\le\liminf_j\varepsilon_{N_j}
=\inf\operatorname{Spec}A_L,
\]

so \(\phi\) is a continuum ground state.
Then
\(\sum_j\|\phi_{N_{j+1}}-\phi_{N_j}\|_2<\infty\). The argument of
(13)--(14) gives bounded variation of \(\mathcal C_{N_j}\) in \(C^2(K)\).
The limit Cauchy transform is not identically zero: otherwise all residues,
and hence \(\phi\), would vanish. Hurwitz again makes it zero-free off
\(\mathbb R\). Finally, the lattice shells

\[
\sum_{N_j<|k|\le N_{j+1}}(s-c_Lk)^{-2}
\tag{18}
\]

are disjoint and absolutely summable over \(j\), uniformly on \(K\).
Equation (4) proves (16) for the same sequence on every compact. \(\square\)

This proves scalar trace summability at fixed \(L\). It is weaker than the
canonical consecutive Schatten series in 106.04(42), but it is already the
topology relevant to the finite characteristic divisor.

### Corollary 6 — The selected continuum ground transform is real-rooted

For the continuum ground state \(\phi\) obtained in Theorem 5,
\(\widehat\phi\) has no nonreal zero.

### Proof

Compact support and \(L^2\)-convergence imply locally uniform convergence
\(\widehat\phi_{N_j}\to\widehat\phi\). Every finite transform has only real
zeros by CCM's finite determinant theorem. The limit is not identically zero,
so Hurwitz excludes every nonreal zero. \(\square\)

This corollary makes rigorous, along the selected cofinal subsequence, the
fixed-\(L\) limiting consequence suggested in CCM's Outlook. It is not the
global \(L\to\infty\) assertion.

## 5. Uniform Weyl bound and elimination of the independent shell

Return to the canonical consecutive isometries \(\mathsf U_N\) of 106.04 and
put

\[
G_N(z)=(\mathsf A_N-z)^{-1},\qquad
E_N=G_{N+1}\mathsf U_N-\mathsf U_NG_N,\qquad
H_N=\|G_N\|_{\mathcal S_2}^2.
\tag{19}
\]

All suprema and sums in this section range over levels at which the
simple-even/nonzero-overlap quotient construction is defined.

### Theorem 7 — Uniform fixed-\(L\) Weyl estimate

For every \(z\notin\mathbb R\),

\[
\boxed{
\sup_N H_N<\infty.
}
\tag{20}
\]

### Proof

Let \(\mathcal K_L\) be the \(L^2\)-closure of the unit Ritz vectors. The
same compact form embedding used above makes \(\mathcal K_L\) a compact set
of unit vectors; in particular it does not contain zero. The
Fourier transform maps it continuously and injectively into
\(\operatorname{Hol}(\mathbb C)\). After the harmless translation from
\([0,L]\) to \([-L/2,L/2]\), which only multiplies the transform by a
zero-free exponential, one has

\[
|\widehat f(w)|\le\sqrt L\,e^{(L/2)|\operatorname{Im}w|}.
\tag{21}
\]

Compactness and injectivity give finitely many sample points
\(w_1,\ldots,w_r\) and \(c>0\) such that

\[
\max_{1\le j\le r}|\widehat f(w_j)|\ge c
\qquad(f\in\mathcal K_L).
\tag{22}
\]

Let \(M=\max_j|w_j|\). For each \(f\), choose \(w_j\) satisfying (22), apply
Jensen's formula on the inner disk centered at \(w_j\) of radius \(R+M\),
and use (21) on the concentric disk of radius \(2(R+M)\). Counting zeros
with multiplicity gives, uniformly in \(N\),

\[
\#\{\theta\in\operatorname{Spec}\mathsf A_N:|\theta|\le R\}
\le C_L(1+R).
\tag{23}
\]

Indeed, with spectral multiplicity, the finite quotient characteristic is
encoded by the corresponding Fourier transform through the CCM determinant
identity. Splitting
\(\mathbb R\) into dyadic shells in (23) gives

\[
\sup_N\sum_{\theta\in\operatorname{Spec}\mathsf A_N}
\frac1{|\theta-z|^2}<\infty,
\tag{24}
\]

which is (20). \(\square\)

Let \(Q_N^{\rm new}=I-\mathsf U_N\mathsf U_N^*\). The shell has explicit
parity coordinates. Put \(M=N+1\),
\(r_N=I_N\xi_N\), \(g_N=\xi_{N+1}\), and

\[
e_M^\pm=\frac{U_M\pm U_{-M}}{\sqrt2}.
\]

In the ordinary \(K_{N+1}\) coordinate the complement of \(C_NK_N\) is
spanned by

\[
h_N^-=e_M^-,
\qquad
h_N^+=\langle g_N,r_N\rangle e_M^+
       -\langle g_N,e_M^+\rangle r_N.
\tag{25}
\]

Consequently an orthonormal basis of
\(\operatorname{Ran}Q_N^{\rm new}\) is

\[
q_N^\sigma=
\frac{S_{N+1}^{-1/2}h_N^\sigma}
{\langle h_N^\sigma,S_{N+1}^{-1}h_N^\sigma\rangle^{1/2}},
\qquad \sigma\in\{+,-\}.
\tag{26}
\]

In particular,

\[
\|G_{N+1}Q_N^{\rm new}\|_{\mathcal S_2}^2
=\sum_{\sigma=\pm}
\frac{\|G_{N+1}S_{N+1}^{-1/2}h_N^\sigma\|^2}
{\langle h_N^\sigma,S_{N+1}^{-1}h_N^\sigma\rangle}.
\tag{27}
\]

More importantly, no separate asymptotic estimate of (27) is needed.
The exact Hilbert--Schmidt telescoping identity is

\[
\boxed{
\begin{aligned}
\|G_{N+1}Q_N^{\rm new}\|_{\mathcal S_2}^2
={}&H_{N+1}-H_N\\
&-2\Re\operatorname{Tr}
   ((\mathsf U_NG_N)^*E_N)-\|E_N\|_{\mathcal S_2}^2.
\end{aligned}}
\tag{28}
\]

### Corollary 8 — The shell is not independent

If

\[
\sum_N\|E_N\|_{\mathcal S_1}
=\sum_N
\|G_{N+1}\widehat{\mathcal R}_NG_N\|_{\mathcal S_1}<\infty,
\tag{29}
\]

then

\[
\boxed{
\sum_N\|G_{N+1}Q_N^{\rm new}\|_{\mathcal S_2}^2<\infty.
}
\tag{30}
\]

### Proof

Since \(\|\mathsf U_NG_N\|\le|\operatorname{Im}z|^{-1}\),

\[
|\operatorname{Tr}((\mathsf U_NG_N)^*E_N)|
\le |\operatorname{Im}z|^{-1}\|E_N\|_{\mathcal S_1}.
\tag{31}
\]

Moreover (29) implies \(\sum_N\|E_N\|_{\mathcal S_2}^2<\infty\).
Sum (28), use (20), and note that its left side is nonnegative.
\(\square\)

Thus the two-series package 106.04(42) has been reduced to the single
canonical series (29).

## 6. Binding frontier

The fixed-\(L\) result is now:

\[
\begin{array}{ll}
\text{scalar trace summability on a cofinal subsequence} & \textbf{proved},\\
\text{uniform finite spectral/Weyl compactness} & \textbf{proved},\\
\text{new-shell summability from transported summability} & \textbf{proved},\\
\text{consecutive scalar summability under (11)} & \textbf{proved},\\
\text{the sufficient Gamma--Euler rate (11)} & \textbf{open},\\
\text{the canonical consecutive Schatten series (29)} & \textbf{open},\\
\text{the source identification as }L\to\infty & \textbf{open}.
\end{array}
\tag{32}
\]

One explicit route to the remaining adjacent-cutoff question is the
arithmetic estimate

\[
\sum_N\sqrt{
\frac{\varepsilon_N-\varepsilon_{N+1}}
     {\lambda_2(W_{N+1})-\varepsilon_{N+1}}}<\infty.
\tag{33}
\]

Alternatively, one can prove bounded variation of the Cauchy transforms or
prove (29) directly using the rank-two/Loewner formula of 106.04. Neither
audited source proves (33). Even a proof of (33) at every fixed
\(L\) would still leave the diagonal Gamma--Euler theorem identifying the
\(L\to\infty\) limit with \(-(\xi'/\xi)'\).

## Status

Proved: the prior-art boundary relative to CCM and Suzuki; the exact scalar
Cauchy-transform identity; the ground-line rotation inequality; the
consecutive criterion; cofinal-subsequence scalar summability; the uniform
Weyl/HS-resolvent bound; and elimination of the shell as an independent
summability obligation.

Open: the consecutive arithmetic rate (33), the canonical transported
Schatten series, and the global \(L\to\infty\) Xi identification. No RH
conclusion is claimed.
