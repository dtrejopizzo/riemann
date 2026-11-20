# CONTROL_001 — Apparent non-locality by compression

2026-10-18. PROVED, elementary observation; no new mechanism and no closing route.

Use the unitary Fourier transform and dt in frequency. Let P_T be the projection whose image
H_T is the transform of L²([-T,T]). Its kernel is

    s_T(t-u)=sin(T(t-u))/(π(t-u)).

For bounded real a, A=P_T M_a P_T has weak kernel

    K_a(t,t′)=∫ s_T(t-u)a(u)s_T(u-t′) du.

The integral converges by Cauchy–Schwarz. Although K_a generally depends on
both variables, for f,g∈H_T:

    ⟨f,Ag⟩=⟨f,M_a g⟩.

Proof: P_T is self-adjoint and P_T f=f, P_T g=g. Hence writing K_a does not
introduce any new sign relation on the effective domain. With a polar
restriction V_T⊂H_T the identity persists for f,g∈V_T.

The same computation holds for unbounded symbols when the multiplier form
is defined and the compression is interpreted as a form restriction; no
absolutely convergent integral formula is being claimed in that case.

**Novelty test required for O1:** it is not enough to exhibit K(t,t′) nor a
nonzero commutation in the ambient L². One must show that, restricted to the
relevant domain, the form is not just the previous multiplier after compression.
This does not exclude all non-local operators nor prove that the class O1
is empty. It avoids confusing the shape of the kernel with an additional mechanism.

It is also worth separating variables: Toeplitz/Hankel in the indices of the
Dirichlet basis, kernel in the coordinate x and kernel in the Mellin height t are three
different representations; translate them before attributing an obstruction.
