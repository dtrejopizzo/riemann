# Phase 120 — diagonal-Casimir polarization

## Status

This is the active non-radial candidate after the residue and scalar-curvature
dichotomies. Its positive operator is constructed independently of the Weil
form and survives at infinite Frobenius depth. Three exact pieces are proved
below. The remaining gate is a coefficient identity, not an existence or
contractivity assertion.

This differs from the phase-67 coherent-kernel and quantum-Haar attempts. It
does not use a single coherent kernel as the archimedean metric and it does not
orthogonalize prime colours with a Haar state. The new datum is the positive
**diagonal Casimir excess** of a tensor product of positive discrete-series
modules, evaluated in a coherent, non-Haar channel.

## 1. Infinite polarized modules

Let \(D_k^+\), \(k>0\), denote the positive discrete series of
\(\mathfrak{su}(1,1)\), with self-adjoint convention

\[
 K_0^*=K_0,\qquad K_+^*=K_-,\qquad
 [K_0,K_\pm]=\pm K_\pm,\qquad [K_-,K_+]=2K_0.        \tag{1.1}
\]

The Casimir

\[
 \mathcal C=K_0(K_0-1)-K_+K_-                       \tag{1.2}
\]

acts on \(D_k^+\) by \(k(k-1)\). Every module is already infinite, so no
socle trace or depth transition is needed.

Use one finite-place module

\[
 \mathcal H_p=D_{1/2}^+                              \tag{1.3}
\]

per prime and the archimedean module

\[
 \mathcal H_\infty=D_{1/4}^+.                       \tag{1.4}
\]

The value \(1/4\) is not fitted: it is the Meixner--Pollaczek/Gamma module
whose boost spectral density contains

\[
 |\Gamma(1/4+i\tau/2)|^2.                            \tag{1.5}
\]

## 2. Exact recovery of the local Poisson contact

In the holomorphic model of \(D_k^+\), normalized coherent vectors obey

\[
 \langle z;k\mid w;k\rangle
 =\frac{(1-|z|^2)^k(1-|w|^2)^k}
        {(1-\bar zw)^{2k}}.                          \tag{2.1}
\]

For a prime \(p\), put \(r_p=p^{-1/2}\), \(\rho_p=p^{-1/4}\), and rotate
the coherent point by \(w_p(\tau)=\rho_p e^{i\tau\log p}\). At \(k=1/2\),

\[
 G_p(\tau):=\langle\rho_p;1/2\mid w_p(\tau);1/2\rangle
 =\frac{1-r_p}{1-r_pe^{i\tau\log p}}.               \tag{2.2}
\]

Consequently

\[
 \frac{2}{1-r_p}\Re G_p(\tau)-1
 =\frac{1-r_p^2}
        {1-2r_p\cos(\tau\log p)+r_p^2}
 =P_p(\tau).                                        \tag{2.3}
\]

Thus the physical place-Poisson multiplier is an exact affine coherent
matrix coefficient. Equivalently, after rescaling the coherent vector by
\((1-r_p)^{-1/2}\), it is \(2\Re\widetilde G_p-1\). The central
normalization \(p^{-j/2}\) is the square \(\rho_p^{2j}\), and no integer/norm
collapse is used.

## 3. A source-defined positive global operator

For a nonempty finite place set \(S\), form

\[
 \mathcal H_S=\mathcal H_\infty\widehat\otimes
               \bigwidehat\otimes_{p\in S}\mathcal H_p.           \tag{3.1}
\]

Let \(K_a^{\rm tot}=K_a^{(\infty)}+\sum_{p\in S}K_a^{(p)}\), and let
\(\mathcal C_{\rm tot}\) be its Casimir. Define the connected Casimir excess

\[
 \Omega_S=\mathcal C_{\rm tot}-\mathcal C_\infty-
          \sum_{p\in S}\mathcal C_p.                \tag{3.2}
\]

### Theorem 3.1 — positivity of the diagonal Casimir excess

On \(\mathcal H_S\), \(\Omega_S\) is strictly positive.

#### Proof

For positive discrete series, the tensor product decomposes into positive
discrete series with lowest weights

\[
 K+n,\qquad K=\frac14+\frac{|S|}{2},\qquad n\ge0,    \tag{3.3}
\]

with finite multiplicities. On such a summand the eigenvalue of (3.2) is

\[
 (K+n)(K+n-1)-\sum_v k_v(k_v-1)
 =2\sum_{v<w}k_vk_w+2Kn+n(n-1)>0.                   \tag{3.4}
\]

Here \(v\) ranges over \(\infty\) and the primes, and all \(k_v>0\). QED.

This theorem supplies the missing kind of positivity: it is infinite-depth,
non-radial, cross-place, and fixed before any comparison with row (c).

## 4. Why a tensor norm is not used

The raw product coherent coefficient

\[
 \prod_{p\in S}G_p(\tau)                            \tag{4.1}
\]

contains mixed composite frequencies \(\log(p^iq^j)\). Those cannot occur
in the von Mangoldt contact, because \(\Lambda(p^iq^j)=0\) for \(p\ne q\).
Conversely,

\[
 \log\prod_pG_p=\sum_p\log G_p                     \tag{4.2}
\]

has exactly the correct primitive-place support, and logarithmic
differentiation cancels the \(1/j\) and produces
\((\log p)p^{-j/2}\). But declaring the logarithm of a Gram kernel to be a
Gram kernel would be invalid.

The role of \(\Omega_S\) is precisely to take the connected part inside a
genuine positive representation. It must reproduce the degree/contact
completion before the local tangent ports are eliminated; it must not be
replaced by the scalar logarithm (4.2).

## 5. The exact coefficient gate

Let \(U_S(t)\) rotate the \(p\)-th coherent coordinate with speed \(\log p\)
and act on the archimedean factor by its boost. Let

\[
 \mathcal I_SF=\int_{-T}^{T}F(t)U_S(t)\Omega_0\,dt                 \tag{5.1}
\]

on the smooth compact core, initially as a weak coherent integral. The
candidate positive form is

\[
 \mathcal Q_S(F,G)=
 \langle\Omega_S^{1/2}\mathcal I_SF,
        \Omega_S^{1/2}\mathcal I_SG\rangle.          \tag{5.2}
\]

Every object in (5.2) is source-defined and \(\mathcal Q_S\ge0\) follows from
Theorem 3.1. The decisive comparison is now the literal identity

\[
 \mathcal Q_S(L_0F,L_0G)
 \stackrel{?}{=}-B_{\rm nuc,S}(F,G)
      +\mathbf M_S(F)^*H_S\mathbf M_S(G),            \tag{5.3}
\]

where \(\mathbf M_S=(M_-,M_+)\) and \(H_S\) must be the matrix obtained from
the lowest-weight boundary vectors, not fitted afterward.

Equation (5.3) has three zero-tolerance tests:

1. its one-place connected coefficient must be exactly
   \((\log p)p^{-j/2}\), with no \(j\), \(1/j\), or factorial;
2. every mixed composite \(p^iq^j\), \(p\ne q\), must lie entirely in the
   coherent degree/tangent completion and vanish after the proved D.247
   elimination;
3. the archimedean connected coefficient must be
   \(\log\pi-\Re\psi(1/4+i\tau/2)\), including \(m_0\), from the
   \(D_{1/4}^+\) resolvent and the lowest-weight boundary only.

Failure of any item kills the candidate without modifying \(\Omega_S\).
Success proves the finite global square immediately from (5.2)--(5.3); the
already proved compact-support stabilization then supplies the cofinal limit.

## 6. Counterexample firewall

The shifted pair requires two inequivalent coherent radii
\(p^{-1/4-a/2}\) and \(p^{-1/4+a/2}\) at every place. It therefore has no
single cyclic lowest-weight contact vector of type (2.2); its local module is
reducible rank two and fails the input of (5.1). Davenport--Heilbronn lacks
the primitive-place logarithm (4.2). Dedekind zeta retains one module per
prime ideal, so success would correctly extend to GRH for number fields.

## 7. Ledger

- infinite positive modules and quarter-Gamma parameter: **CONSTRUCTED**;
- exact local Poisson contact (2.2)--(2.3): **PROVED**;
- positive diagonal Casimir excess (3.2)--(3.4): **PROVED**;
- raw tensor-product shortcut: **REJECTED**;
- connected coefficient comparison (5.3): **OPEN AND DECISIVE**;
- finite global square, cofinal limit, row (d): **CONDITIONAL ON (5.3)**.
