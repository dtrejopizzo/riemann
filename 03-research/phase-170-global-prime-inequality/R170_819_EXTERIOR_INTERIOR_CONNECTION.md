# R170_819 — Exact connection between the exterior test and the interior contraction

This note builds the algebraic bridge requested in
R170_818, priority 1. The bridge does not by itself give a sign: it
identifies two concrete remainders that an arithmetic estimate would
have to control. The Tate port with (S_N^*), the domain (Q_{\log}), the
two Poisson–Chebyshev collars, and the first-contact quantifiers are
preserved.

## 1. Data and domains

Let (T) be a hypothetical real primitive first contact, and let

\[
 0\ne F\in\ker H_T,\qquad H_T\ge0,\qquad JF=\varepsilon F,
 \quad \varepsilon\in\{\pm1\}.
\]

Thus, moreover, the primitive minimum is negative for every window
larger than (T). Let (r=r_F) be the Tate vector of the weak equation.
We fix, as in R170_814,

\[
 N=\lceil e^{2T}\rceil,\quad M=N^2,\quad h=\frac1{2N^2},
 \quad \rho=1-h,
\]

and a single (L) that is injective on the whole radical. We set

\[
 g=S_LF,\qquad z=S_N\mathscr Fg,
 \qquad G=G_\rho F,\qquad \delta=G-F.
\tag{1}
\]

(L) is not chosen after inspecting a vector or a sign. By the
construction of R170_814, (G) and (delta) are primitive, supported on
(I_T), have the parity of (F), and belong to (Q_{\log}). Also
(g,z\in Q_{\log}). Hence every form pairing that follows is well
defined.

It is important that we do not use (P_Tz). In particular, we do not
assume that multiplication by the indicator of (I_T) preserves
(Q_{\log}).

Let

\[
 e_F(v)=a_M(F,v)-\langle r,v\rangle,
 \qquad
 \mathcal Q_{M,r}(v)=a_M(v,v)-2\Re\langle r,v\rangle.
\tag{2}
\]

If both arguments are supported on (I_T), then (a_M) coincides with the
compressed form (a_T): since (M\ge e^{2T}), the omitted prime shifts
cannot produce overlap inside the window, and the archimedean term is
the same full-line pairing. The weak equation therefore gives

\[
 e_F(v)=0
 \quad(v\in Q_{\log}\text{ primitive and supported on }I_T),
 \qquad e_F(\delta)=0.
\tag{3}
\]

## 2. A common variation identity

Polarizing (2), together with (3), gives two exact identities:

\[
 \boxed{
  2\Phi(F)=\mathcal Q_{M,r}(F+z)-\mathcal Q_{M,r}(F)-a_M(z,z)
 }
\tag{4}
\]

and

\[
 \boxed{
  hE_\rho(F)=\mathcal Q_{M,r}(G)-\mathcal Q_{M,r}(F)
             =a_M(\delta,\delta).
 }
\tag{5}
\]

In (5), (a_M(\delta,\delta)=a_T(\delta,\delta)), and this is precisely
the interior identity already proved. Formulas (4)–(5) place the
exterior test and the contraction within the same affine-quadratic
functional, without identifying their directions. In particular, they
show why a window derivative does not appear for free: (4) uses (z),
while (5) uses (\delta).

There is a more useful form for localizing the compatibility defect.
Define

\[
 \mathcal R_{\rho,N,L}F
 :=\delta-hz
 =(D_\rho-I)F-C(D_\rho F)p-S(D_\rho F)q
   -hS_N\mathscr F S_LF.
\tag{6}
\]

This remainder is not defined as "(\Phi+E_\rho)": it is the explicit
difference between the two variation operators. Since (G=F+\delta), we
have

\[
e_G(v):=a_M(G,v)-\langle r,v\rangle
       =e_F(v)+a_M(\delta,v).
\tag{7}
\]

Here \(r=r_F\) remains fixed. The notation \(e_G\) does not claim that
\(r_F\) is the Tate vector associated with \(G\), nor that \(G\)
satisfies a radical equation.

Applying (7) to (v=z), and using (5), we obtain the main bridge:

\[
 \boxed{
 \Phi(F)+E_\rho(F)
 =\Re e_G(z)
  +\frac1h\Re a_M\!\left(\delta,
       \mathcal R_{\rho,N,L}F\right).
 }
\tag{8}
\]

The check is direct:

\[
 \Re e_G(z)+h^{-1}\Re a_M(\delta,\delta-hz)
 =\Re e_F(z)+h^{-1}a_M(\delta,\delta).
\]

Hence (8) does not presuppose the sought sign. It leaves two
independently defined objects:

1. (e_G(z)), the exterior residue of the interior competitor (G),
   evaluated against the same nonlocal Poisson test;
2. (h^{-1}a_M(\delta,\mathcal R_{\rho,N,L}F)), the alignment error
   between the primitive contraction and the exterior test at scale
   (h).

The conjectural bound (Phi+E_\rho\le0) is now equivalent to a one-sided
bound on the sum of those two terms. This is a concrete obligation, not
a consequence of interior semidefiniteness.

## 3. PC expansion of the first remainder

Before using PC it is convenient to separate the universal part from
the specific one. Polarizations (4)–(5) hold for any (z\in Q_{\log}).
The choice (z=S_N\mathscr FS_LF) actually enters at (10), and the
specific choice of (G_\rho) enters through the following scale defect.

On the regular kernel, define the scaled operator

\[
 A_M^{(\rho)}=
 m(D/\rho)-\sum_{2\le d\le M}\frac{\Lambda(d)}{\sqrt d}
 \left(\tau_{\log d/\rho}+\tau_{-\log d/\rho}\right).
\tag{9a}
\]

With (D_\rho F(t)=\rho^{-1/2}F(t/\rho)), one checks directly that

\[
 m(D)D_\rho=D_\rho m(D/\rho),\qquad
 \tau_aD_\rho=D_\rho\tau_{a/\rho},\qquad
 A_MD_\rho=D_\rho A_M^{(\rho)}.
\tag{9b}
\]

Equivalently,

\[
[A_M,D_\rho]=D_\rho\bigl(A_M^{(\rho)}-A_M\bigr),
\tag{9c}
\]

For the archimedean block, the equivalent representation with the
dilation on the right is

\[
 [m(D),D_\rho]=[m(D)-m(\rho D)]D_\rho.
\tag{9c'}
\]

The two representations are not mixed within a single term.

where the defect is the explicit operator

\[
\begin{aligned}
 A_M^{(\rho)}-A_M
 ={}&m(D/\rho)-m(D)\\
 &-\sum_{2\le d\le M}\frac{\Lambda(d)}{\sqrt d}
 \bigl(\tau_{\log d/\rho}-\tau_{\log d}
       +\tau_{-\log d/\rho}-\tau_{-\log d}\bigr).
\end{aligned}
\tag{9d}
\]

If one conjugates in the opposite direction, the same formula is
expressed with the symbol defect (m(\tau)-m(\rho\tau)); (9d) fixes
unambiguously the convention used here. Let

\[
 u_\rho=\alpha p+\beta q,\qquad
 \alpha=C(D_\rho F),\qquad \beta=S(D_\rho F),
 \qquad w=D_\rho^*z=D_{1/\rho}z.
\]

Transporting the dilation through the pairing, and adding and
subtracting the unscaled form, gives

\[
\boxed{
\begin{aligned}
 e_G(z)={}&e_F(w)
 +\bigl[a_M^{(\rho)}(F,w)-a_M(F,w)\bigr]\\
 &+\langle r,w-z\rangle
 -\alpha a_M(p,z)-\beta a_M(q,z).
\end{aligned}}
\tag{9e}
\]

This is a decomposition of the competitor's residue into four pieces:
the original residue evaluated on the transported test (w), the
Gamma–primes scale commutator (9d), the shift of the Tate port, and the
two terms of \(a_M(u_\rho,z)\), the exact primitivity correctors. The
first term does not vanish: (w) is a nonlocal test. Nor is (A_MF)
evaluated pointwise outside the window. For data in (Q_{\log}), (9e) is
interpreted via continuity of the complete forms; the difference
between scaled forms is kept grouped together, rather than separating
unjustified distributions.

Formula (9e) essentially uses the specific contraction. Even so, it
does not give a sign. The shifts $\log d/\rho$ do preserve the
multiplicative incidence, since
$\tau_{\log d/\rho}\tau_{\log m/\rho}=\tau_{\log(dm)/\rho}$; hence
$\Lambda*1=\log$ remains available in the fully conjugated identity.
What changes simultaneously is the Gamma–Poisson transport: $\mathscr
F$, $X$, and the finite defect are also conjugated. It is not justified
to mix the original PC with only the scaled prime block. Nor do the
Tate terms and the correctors cancel by the weak equation.

On the regular kernel, the PC identity applied to the first argument
(G) and to the fixed test (g=S_LF) gives

\[
\begin{aligned}
 \Re e_G(z)
 ={}&\Re\langle
  \{X,E_N\}G-L_M^*E_NG-JH_{M,N}G-H_{M,N}\mathscr FG,
  g\rangle\\
 &-\Re\langle S_N^*r,\mathscr Fg\rangle.
\end{aligned}
\tag{10}
\]

For general data, the right-hand side of (10) means the joint extension
(a_M(G,S_N\mathscr Fg)-\langle r,S_N\mathscr Fg\rangle). The terms with
(X) are not separated as supposedly continuous functionals on their
own. The Tate port is (S_N^*r), not (S_Nr).

The support geometry allows, after writing the complete identity, the
cancellation of

\[
 \langle JH_{M,N}G,g\rangle=0,
\tag{11}
\]

because $\log N\ge2T$, $G$ is supported on
$I_{\rho T}\subset I_T$ and $g$ on $I_T$. The collar of the other
orientation

\[
 -\Re\langle H_{M,N}\mathscr FG,g\rangle
\tag{12}
\]

remains. It has no sign deducible from (h_{M,N}(k)\ge0), since it
contains oscillating correlations. Formulas (9e)–(12) also preserve the
Poisson defect and the crossed Tate term; none is discarded before
seeking cancellations.

The second remainder of (8) likewise preserves the whole form:

\[
\begin{aligned}
 a_M(\delta,\mathcal R F)
 ={}&\mathfrak m(\delta,\mathcal R F)\\
 &-\sum_{2\le d\le M}\frac{\Lambda(d)}{\sqrt d}
 \bigl\langle\delta,
   (\tau_{\log d}+\tau_{-\log d})\mathcal R F\bigr\rangle,
\end{aligned}
\tag{13}
\]

where \(\mathcal R=\mathcal R_{\rho,N,L}\). Thus (8), (10), and (13)
offer an explicit interface for a joint comparison, without taking
absolute values term by term.

## 4. What the scale contributes and what it does not

The interior part of (6) is fully explicit:

\[
 \delta=(D_\rho-I)F-C(D_\rho F)p-S(D_\rho F)q.
\tag{14}
\]

For an (F) in the domain of the dilation generator, one can further
write, in (L^2),

\[
 D_\rho F-F
 =-\int_\rho^1 D_s\bigl(-\tfrac12-t\partial_t\bigr)F\,\frac{ds}{s},
\tag{15}
\]

with the sign subject to the convention
\(D_sF(t)=s^{-1/2}F(t/s)\). Identity (8) does not use (15), because a
general contact vector has not been proved to belong to that domain.
(14) is not replaced by an (O(h)) expansion without a uniform estimate
in the form norm.

In particular, there is no proved reason for
$\mathcal R_{\rho,N,L}F$ to be small. The operator $S_N\mathscr FS_L$
contains the finite arithmetic and a nonlocal direction, while
(G_\rho-I) is a geometric contraction followed by two Tate correctors.
The PC identity rewrites the former's response, but it does not prove
an approximation between the two operators.

## 5. Localized structural obstacle

The sought compatibility would reduce, by (8), to proving

\[
 \Re e_G(S_N\mathscr FS_LF)
 +\frac1h\Re a_M\bigl((G_\rho-I)F,
     [(G_\rho-I)-hS_N\mathscr FS_L]F\bigr)\le0.
\tag{16}
\]

The radical equation only annihilates (e_F) on interior primitive
tests. It does not annihilate (e_G), because (G) is not a radical
vector, nor does it make the test (z) interior. Semidefiniteness only
fixes the sign of
\(a_M(\delta,\delta)=hE_\rho\), not the cross term of (16). PC
identifies within (e_G(z)) the Poisson defect, the surviving Fourier
collar, and the crossed Tate term. No available identity turns those
terms into the cross product of (13) with the required sign. The scale
expansion (9e) localizes another incompatibility: one must compare the
original PC identity with its complete conjugate under $D_\rho$. The
divisor convolution survives the scaling; what is still missing is an
identity or estimate that reconciles both Gamma–Poisson transports,
including $X$, $\mathscr F$, Tate, and the correctors.

This is a more precise structural obstacle than saying the tests are
different: a one-sided law is missing for the coherent sum of (10) and
(13), or a new identity forcing alignment between
(G_\rho-I) and (hS_N\mathscr FS_L) on the first-contact radical. This is
not a refutation of such a law for the von Mangoldt coefficients, nor a
claim about RH.

## 6. Result and next obligation

Identities (4), (5), and (8) are proved, with explicit domains and
boundary terms. (8) does connect the exterior test with the interior
variation: both appear in a bilinear mismatch term, and the remaining
residue has the PC expansion (10) with (S_N^*), both collars before the
legitimate cancellation (11), and the Tate term.

The sign of (16) remains unproved. The next arithmetic step must
jointly estimate the Poisson–Tate defect of (10), the collar (12), and
the prime sum of (13). Separating them via absolute values would erase
the cancellations that the identity (\Lambda*1=\log) might contribute.
