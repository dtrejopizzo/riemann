# R170_890 — Tate quadratization and the correct moving coordinate

## 0. Doubly audited result

Multiplying the EM functional by the Tate coordinate `rho_F` repairs its
parity and produces an explicit quadratic form of rank at most two. The
construction is correct. However, the physical ledger of the Tate
connection multiplies the defect by a different coordinate, `sigma_F`, and
minimality does not automatically sign either of the two mixed forms.

In a real parity sector, set

\[
 g_\epsilon=\|b_\epsilon\|^2,
 \qquad
 \rho(F)={ (b_\epsilon,PA_MF)\over g_\epsilon}=:(a,F),    \tag{0.1}
\]

and write the frozen functional as

\[
 \Omega_{\rm EM}(F)=(\omega_{\rm EM},F).                 \tag{0.2}
\]

Then

\[
\boxed{
 \rho(F)\Omega_{\rm EM}(F)=(F,K_{\rm EM}F),
 \qquad
 K_{\rm EM}={a\otimes\omega_{\rm EM}
                 +\omega_{\rm EM}\otimes a\over2}.}     \tag{0.3}
\]

## 1. The coordinate that actually appears in Tate

R170_852(3.1)--(3.3) uses

\[
 \sigma_\epsilon(F)
 :=2\operatorname{Re}(\dot\Pi F,b_\epsilon)
 =-2\operatorname{Re}(F,tb_\epsilon').                  \tag{1.1}
\]

Since `r_F=rho_F b_epsilon`, the Tate virial is

\[
 2\operatorname{Re}(\dot\Pi F,r_F)=\rho_F\sigma_\epsilon(F).
                                                                    \tag{1.2}
\]

If the extracted port has coefficient `rho_F+Delta(F)`, its literal
defect is

\[
\boxed{\mathfrak R_{\rm Tate}(F)=\Delta(F)\sigma_\epsilon(F).}\tag{1.3}
\]

Hence, even after identifying
`Omega_EM=g_epsilon Delta`, the physical form is
`sigma_epsilon Omega_EM/g_epsilon`, not `rho Omega_EM`. Substituting one
coordinate for the other would require a new law.

## 2. Exact sign criterion

Restrict the representatives `a,omega_EM` to the radical. The two possible
nonzero eigenvalues of (0.3) are

\[
 { (a,\omega_{\rm EM})
    \mathbin{\pm}\|a\|\,\|\omega_{\rm EM}\|\over2}.       \tag{2.1}
\]

Thus `K_EM` is semidefinite only if one of the representatives is zero or
if both are collinear. If `omega_EM=lambda a`, the sign is that of
`lambda`. When they are independent, the form takes both signs.

The same conclusion holds for
`sigma(F)Omega_EM(F)`: correcting the physical coordinate does not create a sign
without additional collinearity.

## 3. Finite counterexample

In the orthonormal basis `(e_1,e_2,b)`, let

\[
 \Pi=\operatorname{span}(e_1,e_2),
\]

\[
 A_0e_1=b,\qquad A_0b=e_1,\qquad A_0e_2=0.               \tag{3.1}
\]

For `F=xe_1+ye_2`, one has `PA_0F=xb`, hence `rho(F)=x`. Define the
self-adjoint operator `V=dot A` by

\[
 Ve_1=-e_1,\qquad Ve_2=-e_2-b,\qquad Vb=-e_2.             \tag{3.2}
\]

Then

\[
 \Pi(A_0+sV)\Pi=-sI\succeq0\qquad(s<0),                 \tag{3.3}
\]

so the minimal slope is strictly signed. With anchor `e=b`, `dot e=0`,

\[
 \Omega(F)=-(b,VF)=y,
 \qquad \rho(F)\Omega(F)=xy.                             \tag{3.4}
\]

The last form takes both signs. For `F=e_2`, `rho(F)=0` but
`Omega(F)=1`; hence the quadratization loses the linear law in that case.
The example refutes an abstract inference from minimality, although it is not
presented as an arithmetic model of zeta nor as a moving Tate residue
with nonzero `sigma`.

## 4. Normal Tate energy

The coordinate `rho` does enter exactly in another identity. Let
`r=PA_MF=rho b` at contact and

\[
 \beta(F)=(b,P\dot A_MF)-(h,P\mathcal C_{PC}F)-\rho g.    \tag{4.1}
\]

Then

\[
\boxed{
\begin{aligned}
 \rho\beta={}&{1\over2}D\|r\|^2
 -\rho(b,\dot P A_MF+PA_MDF)\\
 &-\rho(h,P\mathcal C_{PC}F)-\rho^2g.
\end{aligned}}                                           \tag{4.2}
\]

The proof is the product rule

\[
 {1\over2}D\|r\|^2
 =\rho(b,\dot P A_MF+P\dot A_MF+PA_MDF).                 \tag{4.3}
\]

No term `Db` is missing: if `r=rho b` is expanded, it is already inside
`D||r||^2`; adding it again would duplicate its contribution.

Equation (4.2) places the quadratization in the normal Tate energy,
accompanied by the branch response, the support, and PC. It is not the
derivative of the smallest eigenvalue and does not receive its sign.

## 5. Complex case and scope

In a complex sector one must use

\[
 \operatorname{Re}(\overline{\rho(F)}\Omega_{\rm EM}(F));\tag{5.1}
\]

the product without conjugation changes under the phase of `F`. Parities are
handled separately, and reflection does not orient the sign.

```text
quadratization rho*Omega                                   PROVED
symmetric operator of rank <=2                              PROVED
physical coordinate sigma                                   IDENTIFIED
semidefiniteness criterion                                  PROVED
sign from minimality alone                                  REFUTED
normal Tate energy (4.2)                                    PROVED
signed arithmetic relation between rho, sigma, and Omega     OPEN
covariant vanishing / VIR--LB / D                            OPEN
```
