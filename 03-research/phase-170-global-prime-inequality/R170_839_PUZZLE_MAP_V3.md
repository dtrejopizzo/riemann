# R170_839 — Puzzle map v3 for D

Updates R170_818 and R170_832 after audits
R170_833, R170_836, and R170_838. It does not prove D.

## A. Proved and available pieces

1. **Certified base.** Complete positivity for
   \(T\le\frac12\log5\), with a quantifiable local extension from the
   certified gap. Record: Paper 46 and R170_703.
2. **Reduction to first contact.** If D fails, there is a first window
   and a finite radical with a parity extremal vector. Record: Paper 46
   and phases 163--166.
3. **Faithful Gamma detector.** For some finite \(L\), \(R_L\) is
   injective on the radical. Proving \(R_LF=0\) excludes the contact.
   Record: Paper 46 and R170_702.
4. **Complete energy.** The archimedean, prime, and polar parts are
   transported within a single form, without losing their cross terms.
   Record: R170_805--810.
5. **Oriented finite PC.** Both orientations, the hyperbola, the
   collars, and the polar continuum are preserved before taking limits.
   Record: Paper 46, phase 161, and R170_819--826.
6. **Exact entry of the integers.** In the finite PC carrier,
   \(\sum_{d\mid k}\Lambda(d)=\log k\) eliminates, coefficient by
   coefficient, the interior defect \(\delta_\Lambda(k)\). Record:
   R170_835 and R170_837.
7. **Gamma--Euler reserve.** The matrix
   \(D_\Delta=R_L^*(I-D)R_L\) satisfies
   \(D_\Delta\succeq(1-q_0)B\succ0\) on the detected radical. Record:
   Paper 46 and R170_829--830.
8. **Matrix compression of the flux.** We have \(Q=P+E\), with
   \(E\succeq0\), and a finite spectral criterion on the radical.
   Record: R170_827--828.
9. **Exterior response.** The action of \(m(D)\) and of the prime
   translations on exponential tails is computed; the jump is
   logarithmic and belongs to \(L^2\). Record: R170_831 and R170_833.
10. **Hardy port of the source.** The polar/Tate correction of the port
    produced by the source is canonical. Record: R161_009, R161_015, and
    R170_834.
11. **Column Gram matrix.** The map to the Gamma columns has explicit
    Gram matrix
    \[
      G^{\rm col}_{mn}
      ={2b_mb_ne^{-(a_m+a_n)T}\over(a_m+a_n)^2}.
    \]
    Record: R170_835--836.
12. **Exact identity between windows.** Right-hand minimality produces
    \[
      \lambda_\delta\langle F_\delta,E_TF\rangle
      =\langle\xi_F^\delta,F_\delta|_{C_\delta}\rangle.
    \]
    Record: R162_405 and R170_837--838.
13. **Collar decomposition.** For each \(L\),
    \[
      \xi_F^\delta=-\ell_L(R_LF)+\xi_F^{>L}
    \]
    in the collar. Record: R162_406 and R170_838.

## B. Connections already refuted or exhausted

1. A purely interior lift cannot produce \(D_\Delta\): the weak equation
   annihilates it.
2. The canonical Hardy port of the source does not automatically define
   \(\langle r_F,z_{\rm ext}\rangle\) for arbitrary exterior columns.
3. Reflection, parity, and the bilateral sum do not remove the freedom
   of the Tate extension.
4. The Hardy port does not factor universally through a finite number
   of Gamma moments. Evaluation at critical zeros contradicts that
   factorization.
5. The factorization via \((R_L|_Z)^{-1}\) exists only a posteriori and
   is not a uniform arithmetic law.
6. The mixed difference--sum polarization at a fixed window coincides
   with the mixed Green forms already audited in phase 161; it
   recomposes an indefinite exterior commutator.
7. A single available slot does not simultaneously produce
   \(+D_\Delta\) and \(-\mathcal S_{\rm can}\). Demanding a common
   residual is already equivalent to the closure.
8. Minimality does not live in a form on \(Z_T\times Z_T\); it needs the
   state \(F_\delta\) of a larger window.
9. The two-window form of R170_837 does not by itself contain the
   minimality sign. It has Tate residues and \((Z_N-I)A_ME_TF\) without
   a sign.
10. Compressed Chebyshev in the collar was already carried out in
    R162_406. It localizes \(\Lambda*1=\log\), but does not turn the
    prime comb into Gamma energy.
11. The sign of the collar only gives a scalar inequality against the
    unknown profile of \(F_\delta\); it does not force the vector
    \(R_LF\) to vanish.
12. Compactness, Hilbert--Schmidt, tail decay, positivity of weights, or
    a finite matrix do not by themselves contribute the required sign.

## C. Pieces that are genuinely still missing

1. **Bilateral law of the collar.** An arithmetic estimate or identity
   that separates the contribution \(-\ell_L(R_LF)\) from
   \(\xi_F^{>L}\), Tate, and the nonlocal remainder, with enough
   orientation to use the sign of \(\lambda_\delta\).
2. **Domination of the complete tail.** Controlling
   \(\langle\xi_F^{>L},F_\delta|_{C_\delta}\rangle\) by a scale strictly
   smaller than the detected part, without absolute estimates that
   destroy the cancellations.
3. **Comb--Gamma conversion.** An identity converting the exact
   geometry of the integer divisors into coefficients of the Gamma
   moments. The local Chebyshev identity only decides which atoms
   appear.
4. **Control of the larger window's profile.** Relating
   \(F_\delta|_{C_\delta}\) to the limiting vector \(F\) in a
   quantitative and oriented way; currently that profile is an
   independent datum.
5. **Non-perturbative use of minimality.** The argument must fail for a
   positive eigenvector in a window where the eigenvalue decreases. The
   mere sign of the spectral difference does not distinguish the first
   contact.
6. **Separation of falsifiers.** The sign line must stop holding for
   arbitrary positive weights, Davenport--Heilbronn, and systems without
   the comb of \(\mathbb Z\). The exact operation that uses the integers
   must be pointed out.
7. **Uniformity in \(T\).** Choosing \(L,M,N,\delta\) and controlling
   all residues with uniform quantifiers. The existential injectivity of
   \(R_L|_Z\) does not give that control.
8. **Final vanishing.** From the preceding pieces,
   \(R_LF=0\) must follow; Gamma faithfulness then gives \(F=0\),
   excludes the first contact, and closes D.

## D. Immediate admissible piece

The next construction must not be another detector, port, or Green form
at a fixed window. It must formulate a bilateral law of the collar in
which the observed part \(\ell_L(R_LF)\) and the tail \(\xi_F^{>L}\)
appear on different sides or at different scales, and prove that the
separation uses the exact comb of \(\mathbb Z\). If that law is
formulated only with positive norms or with the compressed Chebyshev
identity, it repeats the corpus's no-gos.
