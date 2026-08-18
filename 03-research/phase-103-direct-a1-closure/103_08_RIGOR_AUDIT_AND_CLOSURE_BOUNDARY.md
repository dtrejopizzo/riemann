# Rigor audit and closure boundary

## Conclusion

Phase 103 does **not** presently prove direct A1 unconditionally.  Its
remaining assertion
\[
  C_n(T_n)\geq0\qquad(n\geq8)
\]
implies RH by the established A0/Li chain, and `103_07` also presents an RH
to A1 implication subject to estimates and a finite certificate.  Thus an
unconditional completion here would constitute a proof of RH.  It cannot be
obtained merely by promoting the current numerical evidence to a theorem.

The exact telescoping reduction in `103_01` is a useful algebraic result,
but the claimed analytic and numerical closures below need the repairs
listed here before they can be called proved.

## What is rigorous, conditional, or diagnostic

| claim | current status | reason |
|---|---|---|
| Stieltjes identity, endpoint convention, and the cancellation giving the normal form for \(Q_n\) | algebraic, subject to the cited phase-102 identities | the derivation in `103_01` is symbolic and the moving-endpoint term vanishes because \(\omega_n(T_n)=0\). |
| \(Q_n\)'s leading archimedean scale | asymptotic only after supplying cited classical bounds with constants | `103_02` leaves \(c_1,c_2\) unspecified, so its advertised numerical threshold is not yet an effective theorem. |
| finite tests through \(n=1200\) and observed \(\mathcal J_n=O(1)\) | diagnostic | `103_06` explicitly uses floating point and says it is not certified.  A finite sample cannot establish an asymptotic \(O(1)\) statement. |
| Laguerre budget exponents \(I_2\ll N^{3/4}\), \(I_3\ll N^{5/4}\) | proved | `103_10` derives them from a standard uniform hard-edge/bulk/Airy bound.  The numerical constants and the threshold \(n_1=150\) remain unproved. |
| `103_04`, Theorem 2 | conditional *outline*, not a proved uniform theorem | it assumes RH, invokes the diagnostic budgets, and estimates only to about \(4.05N\), while the stated integral runs to \(T_n\gg4N\).  A separate rigorous tail estimate for the integration-by-parts term is required. |
| finite range \(9\le n\le149\) | open finite certification | the interval verifier has not been extended; numerical values are not certificates. |
| no-go with (M), (E), (B) | plausible restricted no-go, pending quantitative details | it does show why monotonicity plus an envelope cannot determine the answer in that abstract class, but it needs a uniform lobe-variation estimate for its stated constant. |
| no-go retaining actual prime-power support (S) | not established as written | `103_05` replaces lobe points by nearest \(\log m\) for arbitrary integers.  Those are not generally prime powers, so this does not prove the asserted prime-power-supported competitor. |

## Specific corrections required

1. The qualitative interior exponents have now been proved in `103_10`.
   Replace the measured bounds in any theorem proof by those estimates.
   A fit on \(50\le N\le800\) still cannot establish the displayed
   numerical constants or the threshold \(n_1=150\).

2. In the RH summation-by-parts argument, bound
   \[
     \int_{4N}^{T_n} e^{-u/2}\lvert L_{n-1}^{(3)}(u)\rvert\,du
   \]
   and the analogous elementary tail rigorously.  The scripts stop near
   \(4.05N\), whereas \(T_n\asymp n^{5/3}(\log n)^2\).
   This outer-tail obligation is supplied by `103_09`; the separate
   interior obligation remains.

3. State the conditional result accurately: after (1) and (2), and after
   an exact interval certificate for the finite range, it may establish
   **RH implies A1**.  This is not an unconditional proof and cannot be
   used to infer RH without circularity.

4. For the support-strengthened competitor, either remove (S) from the
   theorem's conclusion or prove a placement lemma for *actual prime-power*
   locations and nonnegative permitted weights.  The density of integers is
   irrelevant to that stronger claim.

5. Correct the sign wording in `103_03`: on the terminal ray,
   \(K_n\) has the sign \((-1)^{n-1}\), not always positive.

6. In `103_04`, the elementary explicit-formula term is bounded on an
   interval starting at \(\log2\), not at \(T_8\).  The displayed constant
   \(1.9\) is too small; the argument remains valid there with the uniform
   constant \(2\).  Replace its asserted monomial bound for
   \(L_N^{(2)}(T_n)\) by the valid coefficient bound in `103_09`.

## Candid closure statement

The phase can be closed as a **reduction and obstruction analysis**:

\[
  \text{direct A1} \quad\Longleftrightarrow\quad
  \mathcal J_n\le q(n)\ (n\ge9),
\]
with an exact reserve normal form, conditional/numerical evidence of a large
margin, and a restricted no-go for envelope-plus-monotonicity methods.

It cannot be closed as a proof of A1 or RH.  The remaining unconditional
task is genuinely RH-strength: obtain new information about the actual
zeta zeros (equivalently, a sufficient bound for the integrated explicit
formula), then prove it with uniform constants and certify the finite
range.  No currently documented calculation supplies that input.
