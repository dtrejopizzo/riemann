# D.37 — Polarized Meyer cokernel theorem

## 1. The actual cohomological target

Let

\[
 V=\mathcal H_-^0=\mathcal H_-/Z\mathcal H_\cap       \tag{1.1}
\]

be the odd Poisson quotient of row C, with scaling action `lambda_t`.  The
functional equation supplies a nondegenerate Tate pairing

\[
 \omega:V\widehat\otimes V\longrightarrow\mathbb C(1),              \tag{1.2}
\]

so that

\[
 \omega(\lambda_tv,\lambda_tw)=t\,\omega(v,w).         \tag{1.3}
\]

At the real level this is the symplectic Poincare pairing on the Meyer
spectral realization.  It is source-defined from inversion, Poisson
summation and the trace quotient; no positivity or zero location is part of
its construction.

## 2. Weil-operator contract

A row-D Weil operator on `V` means a continuous real-linear operator

\[
 J:V_{\mathbb R}\longrightarrow V_{\mathbb R}          \tag{2.1}
\]

such that

\[
 J^2=-1,\qquad
 \omega(Jv,Jw)=\omega(v,w),\qquad
 J\lambda_t=\lambda_tJ,                               \tag{2.2}
\]

and

\[
 g(v,w):=\omega(v,Jw)                                 \tag{2.3}
\]

is a positive-definite Hermitian Hilbertizable form on the completed
quotient.  The last condition is the polarization/Hodge condition; it must
be proved from A--B periodic sections and the Gamma boundary, not from the
spectrum of `V`.

The Hilbertization is additionally required to be **trace compatible**:
for every compactly supported smooth test, the integrated scaling operator
extends to a trace-class operator on the Hilbert completion and its Hilbert
trace equals the nuclear Frechet trace of row C.  Nuclearity in the original
Frechet topology alone does not imply this extra assertion, so it is part
of the construction contract.

### Theorem 2.1 (polarization implies central unitarity)

If (2.1)--(2.3) hold, the centrally normalized action

\[
 \rho_t=t^{-1/2}\lambda_t                               \tag{2.4}
\]

is unitary for `g`.

### Proof

Using (1.3), commutation with `J`, and (2.3),

\[
 \begin{aligned}
 g(\rho_tv,\rho_tw)
 &=t^{-1}\omega(\lambda_tv,J\lambda_tw)\\
 &=t^{-1}\omega(\lambda_tv,\lambda_tJw)\\
 &=\omega(v,Jw)=g(v,w).
 \end{aligned}                                        \tag{2.5}
\]

Thus every `rho_t` extends to a unitary on the Hilbert completion.

## 3. The primitive Weil form becomes a negative trace square

For an original row-C test `f`, pass to its central normalization

\[
 g(t)=t^{1/2}f(t).                                     \tag{3.1}
\]

Then `rho(g)=lambda(f)`.  Let

\[
 T_g=\int_0^\infty g(t)\rho_t\,d^*t.                  \tag{3.2}
\]

Use the ordinary group involution
`g^sharp(t)=overline(g(t^(-1)))`.  The original Tate involution is
`f^vee(t)=t^(-1)overline(f(t^(-1)))`, and direct substitution gives

\[
 g\star g^\sharp(t)=t^{1/2}(f\star f^\vee)(t).        \tag{3.3}
\]

Unitarity of `rho` therefore gives

\[
 T_g^*=T_{g^\sharp},\qquad
 T_{g\star g^\sharp}=T_gT_g^*\ge0.                   \tag{3.4}
\]

Trace compatibility makes the displayed positive operator trace class on
the odd Hilbert quotient and identifies its trace with row C.  The even quotient consists of the two
polar characters `0,1`; hence its integrated operator vanishes when

\[
 \widehat f(0)=\widehat f(1)=0.                       \tag{3.5}
\]

The row-C supercharacter identity therefore gives, on primitive tests,

\[
 \boxed{
 B_{\rm nuc}(f,f)
 =-\mathrm{Tr}_{(V,g)}(T_gT_g^*)\le0.}          \tag{3.6}
\]

No spectral expansion is used in (3.6): it follows from the source quotient,
the polarization and the already-proved character comparison.

If the integrated representation is faithful on compactly supported
primitive tests, equality in (3.6) forces `T_g=0` and then `f=0`.  The
separate argument of D.24 also proves strictness after the sign, so no new
conjecture is needed for the equality case.

## 4. Deduction of RH

Equation (3.6) is Weil's primitive criterion, so it implies RH.  There is
also a direct operator consequence.  By Theorem 2.1 the infinitesimal
generator of `rho` is skew-adjoint; equivalently the generator of
`lambda` has spectral real part `1/2`.  Row C identifies its transpose
spectrum, with multiplicities, with the nontrivial zeta zeros.  Therefore
every such zero has real part `1/2`.

This second deduction is downstream of the source polarization and is not
used to define `J`.

## 5. What is already available

For clarity, the finite positive polarization mentioned below is explicit.
For an ordered finite prime set `P`, put

\[
 \mathbb H_P=K_{Z_P}\oplus K_{B_P}
\]

and let `mathcal C_P:K_(Z_P)->K_(B_P)` be the Crofoot unitary of D.34.
Define

\[
 \begin{aligned}
 \omega_P((x,y),(x',y'))
   &=\langle\mathcal C_Px,y'\rangle
     -\langle y,\mathcal C_Px'\rangle,\\
 J_P(x,y)&=(-\mathcal C_P^*y,\mathcal C_Px).
 \end{aligned}                                      \tag{5.1}
\]

Then `J_P^2=-1`, `J_P` preserves `omega_P`, and

\[
 \omega_P(v,J_Pw)=\langle x,x'\rangle+\langle y,y'\rangle.       \tag{5.2}
\]

Thus the finite metric is positive before any comparison with row C.
If primes are added in the fixed increasing order, the product
decompositions of D.34 identify `mathbb H_P` with an orthogonal summand of
`mathbb H_(P')`, and `J_(P')` restricts to `J_P`.  The two-copy Gamma
oscillator carries the same standard symplectic complex structure.
Therefore the pre-quotient Crofoot--Gamma system has a genuine compatible
positive polarization.

What is not asserted here is scaling equivariance after Poisson descent:
model spaces for a finite exponential type are not invariant under every
boundary translation.  That is part of (6.1), not a consequence of (5.1).

Rows A--C and D.32--D.36 provide:

1. the quotient `V` and its summable scaling character;
2. the Tate pairing (1.2) and its similitude law (1.3);
3. the two primitive boundary values `widehat F(+/-i/2)`;
4. every local `p^k` Crofoot block;
5. the complete Gamma oscillator;
6. finite compatible positive model-space polarizations before passage to
   the Poisson cokernel;
7. the exact pullback of the resulting signed form to `B_nuc`.

## 6. Exact remaining construction

Let `J_Q` be the compatible complex structure on the finite Crofoot--Gamma
boundary module obtained by pairing the torsor model space with its
Frobenius Crofoot image and the two Hardy oscillator orientations.  To
state descent correctly one must first construct a scaling-equivariant
comparison map

\[
 q_Q:\mathbb H_Q^{\rm Crofoot\text{-}Gamma}
       \longrightarrow V_Q .                         \tag{6.1}
\]

The required descent equation would then be

\[
 J_Q(\ker q_Q)\subseteq\ker q_Q.                     \tag{6.2}
\]

The induced operators on the finite quotients would also have to commute
with the transition maps, and their cofinal limit `J` would have to satisfy
(2.2)--(2.3).
The divisibility audit D.36 shows why this must be proved on the
range--cokernel triangle rather than by choosing a right inverse of `Z`.

Condition (6.2) is a concrete descent statement.  Positivity before descent
is supplied by the Crofoot and oscillator Hilbert norms; what is not yet
proved is that the positive complex structure preserves the Poisson
relations.  D.38 proves that the literal blockwise `J_Q` is not continuously
scaling covariant and that a direct Gamma summand cannot repair this local
commutator.  Therefore the comparison map and Weil operator must be built
globally from the additive Poisson relation; the local Crofoot--Gamma blocks
remain its required trace decomposition, not its block-diagonal action.
