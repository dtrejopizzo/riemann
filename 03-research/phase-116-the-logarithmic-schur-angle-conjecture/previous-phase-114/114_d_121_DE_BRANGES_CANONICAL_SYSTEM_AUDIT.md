# D.121 — De Branges translation of the primitive prime--Gamma operator

## Verdict

There is an exact de Branges/canonical-system translation of the remaining
row-D assertion, but it does not provide a new proof of that assertion.

At finite window and arithmetic cutoff, Fourier--Paley--Wiener transform
turns the two Tate moments into evaluation at the two non-real points
\(\pm i/2\).  The primitive space is therefore the codimension-two ideal
of Paley--Wiener functions vanishing at those points.  On that ideal the
source-derived operator has the exact Toeplitz symbol

\[
 r_X(\tau)=\ell_X(\tau)-(2A_X+m_0),
\]

where \(\ell_X\) contains every \(p^k\) with coefficient
\((\log p)p^{-k/2}\) and the complete quarter-shift Gamma integral.  Thus

\[
 -B_{{\rm nuc},X}^{\rm prim}
 =P_TT_{r_X}P_T .
\]

After division by \(q(z)=z^2+1/4\), positivity of this form would make the
resulting weighted entire-function space a de Branges space (subject only
to the standard non-degeneracy/closed-evaluation condition).  Positivity is
exactly row D, so invoking the de Branges representation theorem at this
point is not an independent source of positivity.

Globally the conclusion is sharper.  Put

\[
 \boldsymbol\Xi(z)=\xi(1/2-iz),\qquad
 E_a(z)=\boldsymbol\Xi(z+ia)=\xi(1/2+a-iz).
\]

The A--B--C data determine this candidate and its functional equation.
They do not prove that \(E_a\) is Hermite--Biehler for every \(a>0\).  In
fact

\[
 \boxed{
 \text{row D}
 \Longleftrightarrow \mathrm{RH}
 \Longleftrightarrow E_a\text{ is Hermite--Biehler for every }a>0
 \Longleftrightarrow
 \text{positive canonical Hamiltonians }H_a\text{ exist for every }a>0.}
\]

Equivalently, the source-defined logarithmic derivative

\[
 m_\Xi(z)=-{\boldsymbol\Xi'(z)\over\boldsymbol\Xi(z)}
\]

is the Weyl function of a positive canonical system if and only if RH
holds.  A--B--C supplies the meromorphic candidate \(m_\Xi\), but proving
that it is Herglotz is precisely the missing primitive sign.

There is a useful unconditional boundary: the classical zero strip implies
that \(E_a\) is Hermite--Biehler for \(a\geq1/2\).  Extending this positive
canonical chain through every \(0<a<1/2\), all the way to the central
boundary, is equivalent to excluding off-line zeros.  The de Branges route
therefore locates the obstruction exactly; it does not bypass it.

No statement about RH is assumed below, and the paper is not modified.

## 1. Fourier convention and the two Tate jets

For \(F\in L^2(-T,T)\), use

\[
 (\mathcal U_TF)(z)=G(z)=\int_{-T}^{T}F(t)e^{-izt}\,dt.       \tag{1.1}
\]

The Paley--Wiener theorem identifies \(\mathcal U_TL^2(-T,T)\) with
\(PW_T\), with

\[
 \|F\|_2^2={1\over2\pi}\int_{\mathbb R}|G(x)|^2\,dx.       \tag{1.2}
\]

The two moments from D.117 are literally

\[
 M_+(F)=G(i/2),\qquad M_-(F)=G(-i/2).                       \tag{1.3}
\]

Indeed \(e^{-i(i/2)t}=e^{t/2}\) and
\(e^{-i(-i/2)t}=e^{-t/2}\).  If the central Mellin variable is
\(s=1/2-iz\), these two points are respectively \(s=1\) and \(s=0\).
They are exactly the two Tate/polar evaluations, not an analogy with them.

Consequently

\[
 PW_T^0=\{G\in PW_T:G(-i/2)=G(i/2)=0\}                    \tag{1.4}
\]

is the Fourier image of the primitive space.  The common divisor is

\[
 q(z)=(z-i/2)(z+i/2)=z^2+1/4.                            \tag{1.5}
\]

Thus every \(G\in PW_T^0\) has a unique representation \(G=qH\), where
\(H\) is entire of exponential type at most \(T\) and \(qH\in PW_T\).
It is important not to replace this last condition by merely
\(H\in PW_T\): multiplication by \(q\) is unbounded in the ordinary
Paley--Wiener norm.

The reproducing kernel of \(PW_T\), in the normalization (1.1), is

\[
 K_T(z,w)={\sin T(z-\overline w)\over\pi(z-\overline w)}. \tag{1.6}
\]

The Gram matrix of the two evaluations is, up to the common Plancherel
normalization,

\[
 G_T=\begin{pmatrix}2\sinh T&2T\\2T&2\sinh T\end{pmatrix}. \tag{1.7}
\]

Its eigenvalues are \(2(\sinh T\pm T)>0\).  Hence the orthogonal projection
onto (1.4) is the intrinsic two-kernel projection

\[
 P_T=I-K_JG_T^{-1}K_J^*,                                \tag{1.8}
\]

which is the Fourier form of D.117, (4.7).  This is the exact place where
the two jets enter the de Branges formulation.

## 2. Exact Toeplitz form of the prime--Gamma operator

Let

\[
 w_{p^k}={\log p\over p^{k/2}},\qquad a_{p^k}=k\log p,
\quad
 A_X=\sum_{p^k\leq X}w_{p^k},                          \tag{2.1}
\]

and

\[
 g_\infty(r)={e^{-r/2}\over1-e^{-2r}},\qquad
 m_0=\log\pi-\psi(1/4).                                \tag{2.2}
\]

The Fourier multiplier of the positive jump Laplacian \(L_X\) is

\[
\begin{aligned}
 \ell_X(\tau)={}&
 2\sum_{p^k\leq X}{\log p\over p^{k/2}}
       \bigl(1-\cos(k\tau\log p)\bigr)\\
 &+2\int_0^\infty {e^{-r/2}\over1-e^{-2r}}
       (1-\cos(\tau r))\,dr.                           \tag{2.3}
\end{aligned}
\]

The integral is

\[
 \operatorname {Re}\psi(1/4+i\tau/2)-\psi(1/4).        \tag{2.4}
\]

Equations (2.1)--(2.4) include every prime power and the full Gamma
oscillator.  Put

\[
 c_X=2A_X+m_0,\qquad r_X(\tau)=\ell_X(\tau)-c_X.         \tag{2.5}
\]

Plancherel and D.117, (4.4), give, without an approximation,

\[
\begin{aligned}
 -B_{{\rm nuc},X}(F,F)
 &=\langle F,(L_X-c_XI)F\rangle\\
 &={1\over2\pi}\int_{\mathbb R}
       r_X(x)|G(x)|^2\,dx.                              \tag{2.6}
\end{aligned}
\]

Since multiplication by a symbol does not preserve \(PW_T\), the operator
on \(PW_T\) is the Toeplitz compression

\[
 T_{r_X}=P_{PW_T}M_{r_X}|_{PW_T}.                       \tag{2.7}
\]

Therefore the precise operator identity is

\[
 \boxed{
 -B_{{\rm nuc},X}^{\rm prim}=P_TT_{r_X}P_T
 =P_T\mathcal U_T(L_X-c_XI)\mathcal U_T^{-1}P_T.}       \tag{2.8}
\]

This is the requested translation of the primitive operator
\(L_X-c_XI\).  No zero of \(\xi\) was used to derive (2.8).

Dividing out the two fixed jets gives the signed entire-function form

\[
 [H,K]_{X,T}={1\over2\pi}\int_{\mathbb R}
 r_X(x)|q(x)|^2H(x)\overline{K(x)}\,dx,                \tag{2.9}
\]

on

\[
 \mathcal D_T(q)=\{H\text{ entire of type }\leq T:qH\in PW_T\}. \tag{2.10}
\]

The form (2.9) is invariant under conjugation and under every de Branges
zero flip

\[
 H(z)\longmapsto H(z){z-\overline w\over z-w}
 \quad(H(w)=0,\;w\notin\mathbb R),                     \tag{2.11}
\]

because the multiplier in (2.11) has modulus one on \(\mathbb R\).
The domain (2.10) is preserved as well.

If (2.9) is positive definite and its completion has continuous point
evaluations, the de Branges axioms and representation theorem produce an
entire Hermite--Biehler function \(E_{X,T}\) whose de Branges norm is
(2.9).  But positivity of (2.9) is, by (2.8), precisely

\[
 L_X|_{\ker(M_-,M_+)}\geq c_XI,                        \tag{2.12}
\]

the row-D inequality.  The representation theorem packages the desired
positive form after it is known; it does not prove (2.12).

## 3. The global Hermite--Biehler candidate

Use the entire completed function

\[
 \xi(s)={1\over2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)  \tag{3.1}
\]

and its central real-entire form

\[
 \boldsymbol\Xi(z)=\xi(1/2-iz).                        \tag{3.2}
\]

The functional equation and Real structure give

\[
 \boldsymbol\Xi(-z)=\boldsymbol\Xi(z),\qquad
 \boldsymbol\Xi^\#=\boldsymbol\Xi.                   \tag{3.3}
\]

For \(a>0\), define

\[
 E_a(z)=\boldsymbol\Xi(z+ia)=\xi(1/2+a-iz).            \tag{3.4}
\]

Then

\[
 E_a^\#(z)=\boldsymbol\Xi(z-ia)=\xi(1/2-a-iz),        \tag{3.5}
\]

and the associated transfer quotient is exactly

\[
 \Theta_a(z)={E_a^\#(z)\over E_a(z)}
 ={\xi(1/2-a-iz)\over\xi(1/2+a-iz)}.                  \tag{3.6}
\]

Thus \(E_a\) is Hermite--Biehler precisely when \(\Theta_a\) is Schur in
the upper half-plane:

\[
 |E_a(z)|>|E_a^\#(z)|\quad(\operatorname {Im}z>0)
 \quad\Longleftrightarrow\quad |\Theta_a(z)|<1.        \tag{3.7}
\]

This is the scalar de Branges--Rovnyak transfer already isolated in the
Krein--Langer audit, now with its exact entire endpoint.

## 4. Hermite--Biehler for all shifts is exactly RH

Suppose first that RH holds.  Then every zero of \(\boldsymbol\Xi\) is
real and, pairing the symmetric zeros, its Hadamard product has the form

\[
 \boldsymbol\Xi(z)=\boldsymbol\Xi(0)
 \prod_{\gamma>0}\left(1-{z^2\over\gamma^2}\right)^{m_\gamma}. \tag{4.1}
\]

The zeros of \(E_a\) are \(\pm\gamma-ia\), all strictly in the lower
half-plane.  Moreover

\[
 {E_a^\#(z)\over E_a(z)}
 =\prod_{\gamma>0}
 \left(
 {z-(\gamma+ia)\over z-(\gamma-ia)}
 {z-(-\gamma+ia)\over z-(-\gamma-ia)}
 \right)^{m_\gamma}.                                  \tag{4.2}
\]

Each factor in (4.2) has modulus strictly smaller than one in the upper
half-plane.  The canonical product limit preserves the Schur bound and is
not constant.  Hence \(E_a\) is Hermite--Biehler for every \(a>0\).

Conversely, assume \(E_a\) is Hermite--Biehler for every \(a>0\).  If
\(\lambda=x+iy\), \(y>0\), were a zero of \(\boldsymbol\Xi\), then for any
\(0<a<y\)

\[
 E_a(\lambda-ia)=\boldsymbol\Xi(\lambda)=0,
 \qquad \operatorname {Im}(\lambda-ia)=y-a>0,          \tag{4.3}
\]

contradicting the zero-free upper half-plane property of an
Hermite--Biehler function.  Real symmetry then excludes lower-half-plane
zeros as well.  Hence all zeros of \(\boldsymbol\Xi\) are real, which is
RH.  We have proved

\[
 \boxed{
 \mathrm{RH}\Longleftrightarrow
 E_a\text{ is Hermite--Biehler for every }a>0.}         \tag{4.4}
\]

More locally, if all zeros \(\rho=\beta+i\gamma\) satisfy

\[
 |\beta-1/2|<a,                                        \tag{4.5}
\]

then all zeros of \(E_a\) lie in the lower half-plane and the same
canonical-product argument gives the Hermite--Biehler property.  The
classical zero strip \(0<\beta<1\) therefore proves unconditionally that

\[
 E_a\text{ is Hermite--Biehler for every }a\geq1/2.    \tag{4.6}
\]

The missing statement is not existence of an initial positive de Branges
space.  It is continuation of this positive chain across every shift
\(0<a<1/2\).

## 5. Canonical systems and the logarithmic derivative

The de Branges kernel of \(E_a\) is

\[
 K_a(z,w)=
 {E_a(z)\overline{E_a(w)}-E_a^\#(z)\overline{E_a^\#(w)}
  \over2\pi i(\overline w-z)}.                         \tag{5.1}
\]

It is positive definite exactly when \(E_a\) is Hermite--Biehler.  At the
central boundary its first variation is

\[
 \lim_{a\downarrow0}{K_a(z,w)\over a}
 ={1\over\pi}
 {\boldsymbol\Xi'(z)\boldsymbol\Xi(\overline w)
       -\boldsymbol\Xi(z)\boldsymbol\Xi'(\overline w)
  \over\overline w-z}.                                 \tag{5.2}
\]

Thus positivity of the infinitesimal central kernel is the
Laguerre--Pólya/de Branges form of zero reality.

An equivalent Weyl-function formulation is

\[
 m_\Xi(z)=-{\boldsymbol\Xi'(z)\over\boldsymbol\Xi(z)}. \tag{5.3}
\]

Under RH, (4.1) gives

\[
 m_\Xi(z)=
 \sum_{\gamma>0}m_\gamma
 \left({1\over\gamma-z}+{1\over-\gamma-z}\right),    \tag{5.4}
\]

with the canonical convergence prescription.  Every summand has positive
imaginary part for \(\operatorname {Im}z>0\), so \(m_\Xi\) is a meromorphic
Herglotz function.  Conversely, poles of a meromorphic Herglotz function
are real, hence if (5.3) is Herglotz all zeros of \(\boldsymbol\Xi\) are
real.  Therefore

\[
 \boxed{
 \mathrm{RH}\Longleftrightarrow m_\Xi\text{ is Herglotz}.} \tag{5.5}
\]

The inverse theorem for canonical systems says that such a Herglotz
function is the Weyl function of a trace-normalized positive Hamiltonian

\[
 JY'(x,z)=zH(x)Y(x,z),\qquad H(x)\geq0,quad
 \operatorname {tr}H(x)=1                              \tag{5.6}
\]

(up to the standard reparametrization equivalence).  Equivalently, each
Hermite--Biehler \(E_a\) is the endpoint of a positive canonical system.
It follows that

\[
 \boxed{
 \mathrm{RH}\Longleftrightarrow
 \text{positive canonical Hamiltonians realizing }E_a
 \text{ exist for every }a>0.}                         \tag{5.7}
\]

An indefinite canonical system can always encode more general transfer
data, but its negative index is the off-line zero obstruction calculated
in D.100.  Positivity in (5.6), not mere existence of a system, is the
substantive assertion.

## 6. Exact relation with the Weil form

Let \(f\) be a multiplicative test and set

\[
 G(z)=\widehat f(1/2-iz).                               \tag{6.1}
\]

The two primitive conditions are, by Section 1,

\[
 G(-i/2)=\widehat f(0)=0,
 \qquad G(i/2)=\widehat f(1)=0.                        \tag{6.2}
\]

For the convolution square \(f*f^*\), the spectral side of the completed
explicit formula is

\[
 Q_\Xi(G)=\sum_\rho m_\rho
 G(z_\rho)\overline{G(\overline{z_\rho})},
 \qquad z_\rho=i(\rho-1/2).                            \tag{6.3}
\]

The polar terms vanish by (6.2), and the A--B--C Lefschetz identity gives

\[
 Q_\Xi(G)=-B_{\rm nuc}(f,f).                           \tag{6.4}
\]

If RH holds, every \(z_\rho\) is real and hence

\[
 -B_{\rm nuc}(f,f)
 =\sum_\gamma m_\gamma|G(\gamma)|^2\geq0.             \tag{6.5}
\]

The measure in (6.5) is exactly the positive pole measure of the Herglotz
function (5.4).  If a zero leaves the line, the corresponding Real orbit
in (6.3) becomes a hyperbolic block instead of a positive atom.  Thus the
Weil form, the Herglotz property, the Hermite--Biehler kernels and the
positive canonical Hamiltonian are four exactly equivalent descriptions
of the same missing sign.

This also shows why the two Tate jets do not by themselves prove
positivity.  They remove the known polar plane through (6.2); they do not
turn a free off-line zero orbit in (6.3) into a positive atom.

## 7. What A--B--C provides and what would be circular

The completed A--B--C construction provides, independently of row D:

1. the two evaluation jets (1.3);
2. every local prime-power coefficient and the Gamma density in (2.3);
3. the exact Toeplitz pullback (2.8);
4. the Euler--Gamma completed function \(\xi\), its Real functional
   equation and hence the candidates \(E_a,\Theta_a,m_\Xi\);
5. the nuclear Lefschetz/explicit-formula identity (6.4).

It does **not** independently provide:

1. positivity of (2.9);
2. the Schur bound \(|\Theta_a|<1\) for every \(a>0\);
3. positivity of the kernels (5.1) or (5.2);
4. the Herglotz property of (5.3); or
5. a positive Hamiltonian (5.6) through all central shifts.

Defining the Hilbert norm of a canonical system to be
\(-B_{\rm nuc}\), choosing \(E_a\) only after factoring its off-line
zeros, or taking \(H\) from the positive spectral measure of
\(-\Xi'/\Xi\) all assume the desired conclusion.  Each is circular.

The non-circular de Branges target is now precise: construct from the
prime--Gamma/Yoneda source a positive Hamiltonian whose Weyl function is
the already fixed meromorphic function (5.3), or prove directly that the
source transfer (3.6) is Schur for every \(a>0\).  Either theorem would
close D; neither follows formally from A--B--C.

## 8. Conclusion

The de Branges translation is exact at both levels:

\[
 \begin{array}{c|c}
 \text{row-D datum}&\text{de Branges/canonical datum}\\ \hline
 M_\pm&\text{evaluation at }\pm i/2\\
 \ker(M_-,M_+)&PW_T^0=q\mathcal D_T(q)\\
 L_X-c_XI&T_{r_X}\text{ compressed to }PW_T^0\\
 -B_{{\rm nuc},X}^{\rm prim}&P_TT_{r_X}P_T\\
 \text{completed transfer}&E_a^\#/E_a\\
 \text{primitive Weil positivity}&E_a\text{ Hermite--Biehler for all }a\\
 \text{positive spectral measure}&-\boldsymbol\Xi'/\boldsymbol\Xi
   \text{ Herglotz}\\
 \text{Hodge metric}&H(x)\geq0\text{ in a canonical system}
 \end{array}
\]

The route gives a particularly clean next theorem, but also a decisive
circularity audit: A--B--C constructs the candidate transfer and all of its
local coefficients; the assertion that the transfer belongs to the
positive de Branges class is itself equivalent to D/RH.
