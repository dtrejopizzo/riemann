# D.191 — The exact pre-trace Meyer operator and the Plancherel contractivity audit

## Verdict

There is a canonical operator-valued realization of every primitive A--B--C
test before taking Meyer's nuclear trace.  If

\[
 V=\mathcal H_-/(Z\mathcal H_\cap)                         \tag{0.1}
\]

is the odd Poisson quotient and \(a\in C_c^\infty(\mathbb R_+^\times)\), put

\[
 \boxed{\mathscr Q_-(a)=\int_0^\infty a(x)\rho_-(x)\,{dx\over x}
       \in\mathcal N(V).}                                  \tag{0.2}
\]

This is the requested exact primitive-to-quotient operator.  It is a
filtered convolution representation, preserves the Poisson relation, keeps
the two Tate jets, and is nuclear.  For primitive \(a,b\), the complete
A--B--C form is

\[
 \boxed{B_{\rm nuc}(a,b)
 =-\mathrm{Tr}_{\rm nuc,V}
   \bigl(\mathscr Q_-(a)\mathscr Q_-(b^\vee)\bigr).}        \tag{0.3}
\]

Thus every \(p^k\) and Gamma term is already present in a single operator
product before the trace; expanding its character gives the local formula
of D.74.

The decisive audit is negative but exact.  Equation (0.3) is an equality
for a **nuclear character pairing**, not a positive Hilbert trace identity.
In the canonical critical Plancherel completion, the completed Poisson
operator is multiplication by a function nonzero almost everywhere, so its
range is dense.  Hence the Hausdorff Hilbert cokernel is zero.  Keeping the
algebraic cokernel makes it non-Hausdorff and supplies no bounded adjoint or
contractive norm.  Consequently the source Plancherel identity cannot
simultaneously retain Meyer's odd quotient and turn (0.3) into
\(-\mathrm{Tr}(TT^*)\).

More generally, any faithful trace-compatible Hilbertization on which the
centrally normalized scaling group is contractive in both directions is
unitary and therefore already implies row D (equivalently RH).  This proves
that the missing contractivity is not hidden in the unconditional Poisson
identity.

No sign of the Weil form is assumed.  The paper is not modified.

## 1. The operator on the quotient

Let \(G=\mathbb R_+^\times\), with Haar measure \(d^*x=dx/x\), and let
\(\lambda\) be Meyer's scaling action on \(\mathcal H_-\).  The closed
Poisson range \(Z\mathcal H_\cap\) is \(G\)-invariant because \(Z\) is an
integrated scaling operator and all scaling operators commute.  Therefore
\(\lambda\) descends to the smooth representation \(\rho_-\) on (0.1).

For \(a\in C_c^\infty(G)\), define (0.2) as a bornological integral.  Meyer's
summability theorem states that this integrated operator is nuclear on the
nuclear Fréchet space \(V\).  It obeys

\[
 \mathscr Q_-(a*b)=\mathscr Q_-(a)\mathscr Q_-(b),          \tag{1.1}
\]

and is independent of representatives: if \(g=Zh\), then

\[
 \mathscr Q_-(a)g=\int a(x)\lambda_xZh\,d^*x
 =Z\int a(x)\lambda_xh\,d^*x\in Z\mathcal H_\cap.          \tag{1.2}
\]

This is the exact pre-trace operator, rather than a number extracted from
the explicit formula.

### Support filtration

Use the central logarithmic coordinate

\[
 F(u)=e^{u/2}a(e^u),\qquad a(x)=x^{-1/2}F(\log x).          \tag{1.3}
\]

If \(\mathrm{supp}\,F\subset[-T,T]\), then (0.2) is an integral only
over scalings \(e^{-T}\le x\le e^T\).  On representatives in logarithmic
coordinates it has propagation at most \(T\):

\[
 \mathrm{supp}\,g\subset K
 \quad\Longrightarrow\quad
 \mathrm{supp}\,\mathscr Q_-(a)g
 \subset K+[-T,T].                                        \tag{1.4}
\]

Thus \(a\mapsto\mathscr Q_-(a)\) preserves the natural support filtration.
It does not claim that a nonzero translation-covariant convolution operator
has range in one fixed compact interval; D.74 proves that stronger demand is
incompatible with exact convolution.

## 2. The jets and the central involution

The two quotient characters are

\[
 j_0(a)=\widehat a(0),\qquad j_1(a)=\widehat a(1),          \tag{2.1}
\]

where

\[
 \widehat a(s)=\int_0^\infty a(x)x^s\,d^*x.                \tag{2.2}
\]

By (1.3),

\[
 j_0(a)=\int_{\mathbb R}e^{-u/2}F(u)\,du=M_-(F),\qquad
 j_1(a)=\int_{\mathbb R}e^{u/2}F(u)\,du=M_+(F).            \tag{2.3}
\]

Hence the primitive ideal is

\[
 \mathcal A^0=\ker j_0\cap\ker j_1.                        \tag{2.4}
\]

Since Mellin transform turns convolution into multiplication, \(\mathcal
A^0\) is a two-sided ideal: \(j_i(a*b)=j_i(a)j_i(b)\).  Thus (0.2)
preserves the primitive condition under composition.

The Tate involution is

\[
 a^\vee(x)=x^{-1}\overline{a(x^{-1})}.                     \tag{2.5}
\]

It satisfies

\[
 \widehat {a^\vee}(s)=\overline{\widehat a(1-\bar s)}.     \tag{2.6}
\]

On the critical line it is the ordinary Hilbert involution.  On Meyer's
Fréchet quotient it is instead the transpose involution furnished by the
functional-equation/Tate pairing.  We denote the corresponding transpose
by \(\sharp\); then

\[
 \mathscr Q_-(a^\vee)=\mathscr Q_-(a)^\sharp.              \tag{2.7}
\]

Nothing in (2.7) asserts that \(\sharp\) is the adjoint of a positive
Hilbert metric.

## 3. Exact operator product before the character

Meyer's virtual representation is

\[
 \rho=\rho_+\ominus\rho_-,\qquad
 \rho_+\simeq\mathbb C(0)\oplus\mathbb C(1).               \tag{3.1}
\]

For any \(a,b\), its character on \(a*b^\vee\) is

\[
 \begin{aligned}
 \chi_M(a*b^\vee)
 ={}&j_0(a)\overline{j_1(b)}+j_1(a)\overline{j_0(b)}\\
 &-\mathrm{Tr}_{\rm nuc,V}
 \left(\mathscr Q_-(a)\mathscr Q_-(b^\vee)\right),
 \end{aligned}                                             \tag{3.2}
\]

with the placement of the two polar factors fixed by (2.6).  On the
primitive ideal the first line vanishes, proving (0.3).

The A--B--C realization theorem identifies \(\chi_M\) with \(B_{\rm nuc}\).
Expanding the same operator character, rather than redefining it, gives

\[
\begin{aligned}
B_{\rm nuc}(F,G)={}&
 \sum_p\log p\sum_{k\ne0}p^{-|k|/2}
       \langle F,S_{k\log p}G\rangle\\
&+m_0\langle F,G\rangle
-\int_0^\infty{e^{-r/2}\over1-e^{-2r}}
 \langle F-S_rF,G-S_rG\rangle\,dr .                       \tag{3.3}
\end{aligned}

Thus (0.3) is exactly the operator sitting before all prime-power and Gamma
terms in (3.3).  It is stronger typing than a scalar coincidence, but it is
still a character identity.

## 4. What Plancherel proves on the ambient line

Let \(U_x=x^{-1/2}\lambda_x\) be the centrally normalized regular
representation on the critical Hilbert line.  In logarithmic coordinates
it is translation, hence unitary.  For

\[
 T_F=\int_{\mathbb R}F(u)U_{e^u}\,du,                       \tag{4.1}
\]

ordinary Fourier--Plancherel gives

\[
 \mathcal FT_F\mathcal F^{-1}=M_{\widehat F},\qquad
 \|T_F\|=\|\widehat F\|_\infty,\qquad
 T_{F^\star}=T_F^*.                                        \tag{4.2}
\]

Consequently

\[
 T_FT_F^*\ge0.                                             \tag{4.3}
\]

This is a genuine \(C^*\)-Hilbert statement.  It concerns the ambient
regular representation, not the quotient \(V\).

After the two Gamma charts are glued, the Poisson relation on the critical
line is multiplication by the completed characteristic \(\Xi(\tau)\).
The function \(\Xi\) is bounded there and is nonzero almost everywhere.
For a multiplication operator,

\[
 \overline{\mathrm{Ran}\,M_\Xi}
 =(\ker M_{\bar\Xi})^\perp=L^2(\mathbb R).                  \tag{4.4}
\]

Therefore

\[
 \boxed{L^2(\mathbb R)/\overline{\mathrm{Ran}\,M_\Xi}=0.} \tag{4.5}
\]

The range is not closed: \(\Xi(\tau)\to0\) exponentially along the
critical line because of the Gamma factor (and it also has critical-line
zeros).  Unit vectors concentrated where \(|\Xi|\) is small have images
tending to zero.  Hence the inverse on the range is unbounded.

Equations (4.4)--(4.5) give the exact alternatives:

* Hausdorff Hilbert quotient: the odd object vanishes;
* algebraic quotient by \(\mathrm{Ran}\,M_\Xi\): it is non-Hausdorff,
  so there is no Hilbert adjoint or bounded quotient norm;
* intrinsic nuclear Fréchet quotient: it is faithful and has the character
  (0.3), but Plancherel positivity does not descend to it.

Thus the ambient positivity (4.3) cannot be used as positivity of the
operator in (0.3).

## 5. Character pairing is not a Hilbert isometry

Define on the image of \(\mathscr Q_-\) the nuclear character pairing

\[
 \langle\mathscr Q_-(a),\mathscr Q_-(b)\rangle_{\rm char}
 :=\mathrm{Tr}_{\rm nuc,V}
 \bigl(\mathscr Q_-(a)\mathscr Q_-(b)^\sharp\bigr).         \tag{5.1}
\]

Equation (0.3) says that the primitive Weil form is the negative pullback
of (5.1).  The transpose \(\sharp\) comes from Tate duality, which pairs
spectral parameters \(s\) and \(1-\bar s\); it is not a positive
\(C^*\)-involution.  Cyclicity of the nuclear trace proves symmetry of
(5.1), but not

\[
 \mathrm{Tr}_{\rm nuc}(AA^\sharp)\ge0.              \tag{5.2}
\]

Even a finite-dimensional Krein model shows the logical distinction.  If
\(A^\sharp=JA^*J\) for a self-adjoint unitary \(J\), then
\(\mathrm{Tr}(AA^\sharp)\) takes both signs, whereas
\(\mathrm{Tr}(AA^*)\ge0\).  The companion verifier gives explicit
matrices.

Accordingly (0.3) is best called an exact character-pairing realization,
not an isometry into a positive Hilbert--Schmidt class.

## 6. Contractivity would already be row D

Suppose there were a faithful Hilbert completion \(H_V\) of \(V\) such
that:

1. the centrally normalized scaling \(\widetilde\rho_t=t^{-1/2}\rho_-(t)\)
   extends boundedly to \(H_V\);
2. both \(\widetilde\rho_t\) and \(\widetilde\rho_{t^{-1}}\) are
   contractions;
3. the Hilbert adjoint realizes the Tate transpose and Hilbert traces agree
   with Meyer's nuclear traces.

Because the two contractions are inverse,

\[
 \|v\|=\|\widetilde\rho_{t^{-1}}\widetilde\rho_tv\|
 \le\|\widetilde\rho_tv\|\le\|v\|,                        \tag{6.1}
\]

so \(\widetilde\rho_t\) is unitary.  Then

\[
 \mathscr Q_-(a^\vee)=\mathscr Q_-(a)^*,\qquad
 \mathrm{Tr}\,\bigl(
 \mathscr Q_-(a)\mathscr Q_-(a)^*\bigr)\ge0.              \tag{6.2}
\]

For primitive \(a\), (0.3) yields

\[
 B_{\rm nuc}(a,a)\le0.                                   \tag{6.3}
\]

This is exactly Weil's criterion.  Equivalently, the generator of the
unitary central scaling has imaginary spectrum; row C identifies its
transpose spectrum with \(\rho-\tfrac12\), forcing
\(\mathrm{Re}\,\rho=\tfrac12\).

Hence a faithful two-sided source contractivity theorem is neither supplied
nor suggested by Plancherel alone: if constructed with trace compatibility,
it is itself a complete construction of row D.

## 7. Consequence for the supported Poisson program

The exact pre-trace map (0.2) settles the operator typing and support
filtration.  It also shows why taking the trace too early loses the decisive
information.  What remains is not to reconstruct \(\mathscr Q_-\); it is
already constructed.  The missing datum is a positive Hilbert
polarization/comparison functor

\[
 \mathfrak P:V\longrightarrow H_V                              \tag{7.1}
\]

which is simultaneously:

* faithful to the Fréchet cokernel;
* compatible with the Tate transpose;
* trace compatible with (0.3);
* compatible with the finite-propagation filtration (1.4);
* source-positive without selecting zeta eigenspaces.

The critical Plancherel functor fails the first item by (4.5).  Meyer's
nuclear character satisfies the first, third and fourth items but supplies
no positive adjoint.  This isolates the next construction: a noncritical
rigged Hilbert polarization retaining the cokernel, rather than another
Poisson inversion or trace rearrangement.

## 8. Reproducible finite model

The script `114_d_191_pretrace_plancherel_verify.py` checks:

1. the exact convolution/propagation rule in logarithmic coordinates;
2. growth of the Moore--Penrose inverse for a dense nonclosed multiplication
   range model;
3. collapse of the Hausdorff cokernel at each finite section;
4. positivity of \(\mathrm{Tr}(AA^*)\);
5. both signs for the Tate/Krein pairing
   \(\mathrm{Tr}(AA^\sharp)\).

The model certifies the functional-analytic distinction; it is not a
numerical test of RH.
