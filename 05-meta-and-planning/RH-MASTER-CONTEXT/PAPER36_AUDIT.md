# Mathematical audit of paper 36

## Verdict

The central defensible result of the manuscript is the structural equivalence

\[
\mathrm{ARP\!\!-P}\Longleftrightarrow\mathrm{RH}.
\]

The forward direction uses Pick–Nevanlinna: ARP-P produces normal interpolants, the analytic identity extends the function, and the channels detect every non-real residue. The reverse direction uses the fact that, under RH, each channel is a Cauchy transform of a positive measure. This equivalence correctly localizes the difficulty in ARP-P, but does not prove ARP-P.

The stronger claim "everything except \(\Omega_7\) is proved" needs correction. There is a single central residual equivalent to RH, but several auxiliary pieces announced as closed are partial, conditional, or contain an invalid step. They must not be used as lemmas in a continuation.

## Step 1–15 column

| Block | Audited status | Exact content |
|---|---|---|
| Step 1 | **PROVED** | The change \(s=\tfrac12+iz\) translates RH into the reality of the zeros of \(\Xi\). |
| Steps 2–3 | **PROVED** | The channels defined by the zero side converge normally and have the stated residues. This defines the target; it does not realize it arithmetically. |
| Step 4 | **PROVED** with classical interface | The explicit formula acts on the stated test class. |
| Step 5 | **OPEN / RH-STRENGTH** | ARP-P requires positivity for every finite source plane and every finite set of nodes. |
| Steps 6–7 | **PROVED under a tower hypothesis** | A positive measure gives a positive Pick kernel and the PSD cone is closed. Tower-ARP is not constructed. |
| Steps 8–13 | **PROVED as a consequence of ARP-P** | Matrix NP, normality fixed by pinning, the analytic identity, residue detection, and symmetries eliminate poles off the axis. |
| Step 14 | **PROVED under RH** | The channel weights form positive measures and give ARP-P. |
| Step 15 | **PROVED** | Assembles the two implications. |

So "fourteen closed steps" is correct only if it is kept in mind that several are implications conditional on Step 5 or on an unconstructed tower. They are not fourteen independent sources of evidence.

## Corrected status of H0–H8

| Level | Status | Audit |
|---|---|---|
| H0 | **PROVED** | It is a logical conservation of difficulty. It serves as a circularity check, not as the localization of a new theorem by itself. |
| H1 | **PROVED, scalar** | One node for \(M_\Xi\) at \(\Re s>1\). Does not cover matrix channels with complex weights. |
| H2 | **PARTIAL** | The Gershgorin criterion for sufficiently separated, high nodes is valid. The extension to bounded heights is not proved. |
| H3 | **PARTIAL** | Closes a logarithmic region and an almost-everywhere statement; not the global two-node inequality. |
| H4 | **PROVED as serialization** | The determinants of an accumulating sequence characterize RH. Their sign is not proved. |
| H5 | **PROVED as equivalence** | Window positivity and ARP-P are two coordinates of the same condition. |
| H6 | **QUALITATIVE PROVED; QUANTITATIVE UNCONFIRMED** | If RH fails, some finite witness exists by contraposition. The concrete rational construction does not prove that its tail is smaller than the negative block. |
| H7 | **PARTIAL** | SOS under RH and closure of two nodes on an interior band, fixed box, and large height. There is no global arithmetic SOS. |
| H8 | **PARTIAL** | For fixed \(N\), interior band, and high translation there is positivity. Uniformity in \(N\) at a fixed height is missing, which is precisely the terminal burden. |

### Concrete failure of H2

For a Hermitian matrix \(K\),

\[
K_{ii}>0\quad\forall i
\]

does not imply \(K\succeq0\). Compactness only guarantees that \(\lambda_{\min}(K)\) attains a minimum over a compact set; it does not determine the sign of that minimum. Paper 36's proof does establish PSD-ness when the sum of off-diagonal entries is dominated by the diagonal via Gershgorin. It does not establish the added claim for bounded heights. That addition must be removed or turned into a verifiable hypothesis via principal minors or uniform domination.

### Concrete failure of H6

The proposition obtains a Rayleigh bound of the form

\[
\lambda_{\min}P
\le
\frac{
-2|\kappa|\,|r(w_0)|\,|r(\overline w_0)|
+B_{\mathrm{far}}\|r\|_{\mathrm{far}}^2
}{\|c\|^2}.
\]

The subsequent theorem erases \(|\kappa|\) even though the channel was not normalized. Moreover, adjusting the phase only makes the first term negative; it does not prove

\[
2|\kappa|\,|r(w_0)|\,|r(\overline w_0)|
>
B_{\mathrm{far}}\|r\|_{\mathrm{far}}^2.
\]

What is proved is a computable reduction to tail domination. It is not yet a quantitative negative witness for every configuration.

## Audited \(\Omega\) chain

| Link | Corrected status | Observation |
|---|---|---|
| \(\Omega_1\) | **PROVED** | RH is equivalent to all zeros of \(\Xi\) being real. |
| \(\Omega_2\) | **PROVED as equivalence** | Reality of the zeros is equivalent to ARP-P via Steps 1–15. |
| \(\Omega_3\) | **PROVED as equivalence via RH** | Positivity of all scalar jets at a regular point and ARP-P both characterize RH. There is no level-by-level transfer from all channels to a jet. |
| \(\Omega_4\) | **PARTIAL / REQUIRES REWRITING** | The reference-whitened defect exists for every \(N\); whitening by \(J_N^\infty\) only while \(J_N^\infty\succ0\), up to \(N_*(t_0)\). |
| \(\Omega_5\) | **CONTINUITY PROVED; POSITIVITY CONDITIONAL** | For each \(N\), the jets are continuous as \(y\downarrow\tfrac12\). Unconditional interior positivity is not proved, nor is uniformity as \(N\to\infty\). |
| \(\Omega_6\) | **PROVED for complete families via RH** | Positivity of all boundary jets and \(\lambda_n\ge0\) for all \(n\) are equivalent because both characterize RH. There is no level-by-level truncated positive transformation. |
| \(\Omega_7\) | **OPEN / RH-STRENGTH** | Positivity of Li's criterion for every index. |

The central chain still ends at \(\Omega_7\), but \(\Omega_4\to\Omega_5\to\Omega_6\) cannot be cited as an already-closed unconditional transport. The global characterization via RH must be distinguished from the constructive interior–boundary passage.

## Two defects that must not be mixed up

The global sign defect uses a positive reference:

\[
\delta_N^{\mathrm{ref}}(z_0)
=
\min_{c\ne0}\frac{c^*J_N(z_0)c}{c^*G_N(z_0)c},
\qquad G_N(z_0)\succ0.
\]

It is defined for every \(N\) in the stated domain, and

\[
\delta_N^{\mathrm{ref}}\ge0
\Longleftrightarrow
J_N\succeq0.
\]

The archimedean domination defect uses

\[
T_N=(J_N^\infty)^{-1/2}J_N^{\mathrm{prime}}(J_N^\infty)^{-1/2},
\qquad
\delta_N^{\mathrm{arch}}=1-\lambda_{\max}(T_N).
\]

It is typed only if \(J_N^\infty\succ0\). The pole-pair lemma itself shows that this positivity fails past a scale \(N_*(t_0)\). Any asymptotic claim as \(N\to\infty\) written with \(T_N\) at fixed \(t_0\) is left without an object. The restart must reserve distinct symbols and state the domain in every theorem.

## Realization, sampling, and cascade

The operator layer is valid under self-adjointness, a uniform bound on sources, and resolvent convergence, but the canonical construction of the operators is deferred outside the manuscript. The convergence

\[
(\Phi_P^F)^*(A_P^\circ-z)^{-1}\Phi_P^F
\longrightarrow G_\Xi^F
\]

is precisely a strong identification; it does not follow from \(\Lambda(n)\ge0\).

The sampling laws, factorial saturation, root recovery, and the de Bruijn–Newman cascade contain sketches or pending uniform estimates. They can be kept as conditional programs, but must not support a closure. In particular, the cascade \(t_N^*\to\Lambda_{\mathrm{dBN}}\) depends on detection and tail bounds that are not proved with sufficient uniformity.

## Envelope route: convergence error

The separation

\[
O(n)=\sum_\rho\left(1-\frac1\rho\right)^n
\]

does not define a convergent sum. Under RH each term has modulus one and the pairs do not tend to zero. Li's combination

\[
\lambda_n
=
\sum_\rho
\left[1-\left(1-\frac1\rho\right)^n\right]
\]

is indeed interpretable with the appropriate symmetric convention. For that reason the stationary reductions that isolate \(O(n)\) must be withdrawn as written; the first failure occurs before any phase estimate.

The Laguerre identity at \(\Re s_0>1\) is reusable because there the prime sum converges absolutely. The limit \(s_0\downarrow1\) must keep the cancellation between the pole and the primes together.

## Correction of the prime target: the absolute bound is not \(\Omega_7\)

From the declared split

\[
\lambda_n=\lambda_n^{\rm arch}+\lambda_n^{\rm prime}
\]

it follows exactly that

\[
\lambda_n\ge0
\quad\Longleftrightarrow\quad
\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}.
\]

The equivalence with

\[
|\lambda_n^{\rm prime}|<\lambda_n^{\rm arch}.
\]

does not follow. When \(\lambda_n^{\rm arch}>0\), this latter bound is sufficient and stronger, because it also controls positive prime oscillations that do not threaten Li's criterion. With the manuscript's own split, the failure already appears at \(n=1\):

\[
\lambda_1^{\rm arch}
=1-\frac{\gamma}{2}-\log2-\frac12\log\pi
\approx-0.55412,
\qquad
\lambda_1^{\rm prime}=\gamma\approx0.57722,
\]

while

\[
\lambda_1\approx0.02310>0.
\]

The exceptional range can be determined exactly. The representation

\[
\lambda_n^{\rm arch}
=1-\frac n2(\gamma+\log(4\pi))
+\sum_{r\ {\rm odd}}
\left[\left(1-\frac1r\right)^n-1+\frac nr\right]
\]

has positive second differences:

\[
(\lambda_{n+2}^{\rm arch}-\lambda_{n+1}^{\rm arch})
-(\lambda_{n+1}^{\rm arch}-\lambda_n^{\rm arch})
=\sum_{r\ {\rm odd}}\frac{(1-1/r)^n}{r^2}>0.
\]

With \(d_3\in(0.0062,0.0063)\), \(\lambda_7^{\rm arch}\in(-0.356,-0.355)\), and \(\lambda_8^{\rm arch}\in(0.020,0.022)\), together with the direct values at \(n=1,2\), it follows that

\[
\lambda_n^{\rm arch}<0
\quad\Longleftrightarrow\quad
1\le n\le7.
\]

So the absolute bound written in the anatomy and prime-kernel sections cannot be "the exact inequality" for all \(n\). It must be rewritten as a sufficient strategy for a range where the archimedean part is positive, with the remaining indices treated separately. The minimal target of \(\Omega_7\) is the **one-sided lower bound** of the prime part.

This correction changes the scope of the no-go results: computations that take \(|\psi(x)-x|\), sum norms, or try to control \(|\lambda_n^{\rm prime}|\) rule out absolute routes, but do not rule out the signed lower bound. When \(\lambda_n^{\rm arch}\ge0\), that lower bound controls only the negative excursion; the indices with negative archimedean part require direct treatment.

## Correction of the Laguerre integration by parts

The regularized representation of the prime part keeps the pole–prime cancellation. Define

\[
f_{n,\varepsilon}(y)
=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y),
\qquad
f_{n,\varepsilon}(1)=L_{n-1}^{(1)}(0)=n.
\]

The polar polynomial of the paired limit is exactly

\[
\sum_{k=1}^n\binom nk\frac{(-1)^{k-1}}{\varepsilon^k}
=
\int_0^\infty L_{n-1}^{(1)}(x)e^{-\varepsilon x}\,dx
=
\int_1^\infty f_{n,\varepsilon}(y)\,dy.
\]

Then

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\left[
\int_1^\infty f_{n,\varepsilon}(y)\,dy
-
\int_{1^-}^\infty f_{n,\varepsilon}(y)\,d\psi(y)
\right]
=-
\lim_{\varepsilon\downarrow0}
\int_{1^-}^\infty f_{n,\varepsilon}\,d(\psi-y).
\]

Since \(\psi(1)=0\), the lower endpoint contributes \(-n\). The correct integration by parts is

\[
\boxed{
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\left[
-n+
\int_1^\infty
(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy
\right]
}
\]

or, equivalently,

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\int_1^\infty
(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy.
\]

The formula printed in paper 36 uses

\[
-\lim_{\varepsilon\downarrow0}
\int_1^\infty(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy,
\]

which flips the sign and omits the boundary term. Already at \(n=1\) it fails to reproduce \(\lambda_1^{\rm prime}=\gamma\). If the manuscript's definition

\[
A_n=\int_1^\infty|\psi(y)-y|\,|f'_{n,0}(y)|\,dy,
\]

is kept, the correct formula only gives \(\lambda_n^{\rm prime}\ge-n-A_n\); the triangulation would need \(A_n+n\le\lambda_n^{\rm arch}\). Since the manuscript's own computation gives \(A_n\asymp0.27n^2\log n\), against an archimedean budget of order \(n\log n\), the qualitative deficit \(\Theta(n)\) survives. Its formulas and constants, however, must be recomputed. Any new signed route must start from the boxed identity, not from the printed version.

The asymptotic normalization of the envelope needs a further correction. For this split,

\[
\lambda_n^{\rm arch}
=
\frac n2\log\frac n{2\pi}
+\frac{\gamma-1}{2}n
+\frac34+O(n^{-1}).
\]

So a claim with error \(O(\sqrt n\log n)\) must keep the linear term \(\frac{\gamma-1}{2}n\); it cannot be absorbed into that error. Moreover, \(|\lambda_n^{\rm prime}|\le c\sqrt n\log n\) can only be stated from \(n\ge2\) on, because at \(n=1\) the right-hand side is zero while \(\lambda_1^{\rm prime}=\gamma\). These corrections do not rehabilitate the absolute route; they fix the statement that would need to be compared with the literature.

## Scope of paper 36's no-go results

The walls are filters on concrete classes, not universal impossibility theorems. They survive with this scope:

- a positivity built only after assuming a nonnegative symbol is circular;
- an abstract positive extension does not identify the required arithmetic kernel;
- magnitude bounds that tolerate an off-line zero cannot prove Li's criterion positive for every index;
- a prime sum taken term by term loses the interference that sustains the sign;
- the recurrence examined over all phases has too great a cost for the available detection rate;
- an unconstructed geometry or polarization is a sufficient condition, not an existing object.

What does not survive as universal claims: "no recurrence can work," "no geometry can exist," or "every classical method is excluded." Those quantifiers were never formalized.

The Castelnuovo/Minkowski closure also contains a sign failure: X3 is stated for classes of positive norm and then applied to a class obtained with negative norm. M2 and its consequences are not proved by that argument.

## Reusable core

The following can be kept:

1. the formal ARP-P–RH equivalence;
2. the scalar serialization by jets at a regular point;
3. the Cayley dictionary \(w=1-1/\rho\);
4. the full equivalence with Li's criterion;
5. the finite Cauchy, Pick, and Laguerre identities on their convergent domains;
6. the band closures with all their parameters fixed;
7. the one-sided prime target
   \(\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}\);
8. the no-go results restricted to the class actually proved.

The following must be repaired or downgraded before being cited:

1. the compact addition to H2;
2. the quantitative closure of H6;
3. the global identification of the two defects;
4. the positivity attributed to \(\Omega_5\);
5. sampling, saturation, and cascade;
6. the operator realization deferred elsewhere;
7. the envelope that splits a divergent sum;
8. the incorrect identification of \(\Omega_7\) with an absolute bound;
9. the sign and boundary term of the Laguerre integration by parts;
10. the asymptotic normalization of the envelope and its domain \(n\ge2\);
11. the Castelnuovo/Minkowski closure.

The full logical audit backing this document is at [`fragments/PAPER36_LOGIC_AUDIT.md`](fragments/PAPER36_LOGIC_AUDIT.md).
