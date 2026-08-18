# 107.42 -- Paper C local packet unit-factor audit

## 1. Purpose

This note adds an exact verifier for the finite local algebra used in
`107_20`.  The goal is narrower than Paper C as a whole:

\[
 \langle \mathcal P_{m,\chi_1},\mathcal P_{n,\chi_2}\rangle_{\rm pkt}
 \cong
 \langle Z_m,Z_n\rangle_{\rm fin}\otimes \mathcal U_{\chi_1,\chi_2},
 \qquad
 \|\mathcal U_{\chi_1,\chi_2}\|=1
 \tag{1.1}
\]

should survive as an exact finite audit in the local packet algebra
model, before any global descent or adelic metric claims are used.

## 2. What is audited

The verifier `107_42_paper_c_packet_unit_factor_preflight.py` checks
three exact statements for the local model of `107_20`.

1. The visible label census matches the finite rooted packet algebra:
   for each order \(n\le 12\), the labels split by exact character order
   with multiplicities \(\varphi(d)\) for each \(d\mid n\).
2. For every off-diagonal pair \(m>n>1\) with \(m,n\le 12\), and for
   every rooted label pair \((\chi_1,\chi_2)\), the packet norm equals
   the cyclotomic norm
   \(\left|\mathrm{Res}(\Phi_m,\Phi_n)\right|\), hence is
   independent of the rooted labels.
3. For every diagonal pair \((n,\chi_1),(n,\chi_2)\) with \(n\le 12\),
   the local packet norm still vanishes, so the packet refinement does
   not manufacture a finite scalar on the diagonal.

## 3. Finite model being tested

The script implements the exact finite shadow used by `107_20`:

\[
 B_{n,\chi}^{\rm pkt}=B_n\otimes_{\mathbf Z}\Lambda_{n,\chi},
 \qquad
 \Lambda_{n,\chi}=\mathbf Z\,e_{n,\chi},
 \qquad
 \|e_{n,\chi}\|=1.
 \tag{3.1}
\]

In this model the rooted label factor is rank one, so the packet
presentation matrix is the same Sylvester matrix that computes the
cyclotomic resultant.  The audit therefore tests, exactly and for all
visible labels in the window \(n\le 12\), that the label factor behaves
as a norm-one unit and does not alter off-diagonal support.

## 4. Result

The verifier passes exactly.

Its output reports:

1. the full visible-label census for each \(2\le n\le 12\);
2. the off-diagonal packet norm table for every pair \(m>n>1\);
3. the diagonal vanishing table for all labeled packet self-pairs.

In particular, the local statement of `107_20` is now pressure-tested in
the same style as the exact audits already added for Papers A and B:
the packet labels refine components, but they do not change the finite
norm, and they do not cure the diagonal excess-intersection stop.

## 5. Scope boundary

This audit does **not** prove any of the later global steps of Paper C.
It does not show:

1. that the packet line descends globally on \(\mathcal X_T^{(1)}\);
2. that the descended object is a genuine Deligne pairing;
3. that the boundary metric is admissible or integrable;
4. that the resulting adelic class realizes the Phase 107 source module.

So the effect of `107_42` is local and exact: it upgrades the concrete
finite algebra behind `107_20`, while leaving the globalization papers
where they already were.
