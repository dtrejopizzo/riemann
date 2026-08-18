# 107.44 -- Paper C packet descent cocycle audit

## 1. Purpose

`107_42` exact-audited the local packet algebra of `107_20`, but it did
not yet pressure-test the descent protocol of `107_21`.  The purpose of
the present note is to audit the finite combinatorial shadow of that
descent step.

The exact question is:

\[
 \{\mathcal L_{m,\chi_1;n,\chi_2}^{\rm loc}\}
 \Longrightarrow
 \mathcal L_{m,n,T}^{\rm glob}
 \tag{1.1}
\]

Does the rooted transition system really behave like a descent cocycle,
with route-independent descended section and compatibility with the
finite visible action?

## 2. What is audited

The verifier `107_44_paper_c_packet_descent_cocycle_preflight.py`
checks four exact finite statements in the visible window
\(2\le n\le 12\).

1. For each fixed off-diagonal order pair \((m,n)\), the rooted packet
   labels form one connected descent groupoid over that order pair.
2. The rooted transition maps satisfy the cocycle condition on every
   composable triple of labeled packets over the same order pair.
3. The descended canonical section is route-independent and its norm is
   the same order-only norm already fixed by `107_20` and `107_04`.
4. The whole descent shadow is compatible with the finite action
   \(\mu_r\) whenever multiplication by \(r\) stays inside the visible
   window.

## 3. Finite shadow being tested

The audit uses the finite rooted coordinate of `107_18`,

\[
 \xi_T=(n,\chi),
 \tag{3.1}
\]

and the rooted transition unit of `107_21`,

\[
 g_{(\chi_1,\chi_2),(\chi_1',\chi_2')}
 :
 \mathcal U_{\chi_1,\chi_2}\to
 \mathcal U_{\chi_1',\chi_2'},
 \tag{3.2}
\]

modeled on the visible packet sets for each order pair.

In this finite shadow:

1. vertices are labeled packet pairs \((m,\chi_1;n,\chi_2)\);
2. edges are rooted transition isometries between vertices with the
   same order pair;
3. the descended norm is the order-only norm
   \(|\mathrm{Res}(\Phi_m,\Phi_n)|\);
4. the finite action is the level-window version of `107_18`'s
   \(\mu_r(n,\chi)=(rn,\chi^{(r)})\).

## 4. Result

The verifier passes exactly.

It confirms that:

1. every fixed order pair supports one connected packet descent
   groupoid;
2. every triple overlap composition agrees with the direct transition;
3. the descended section is independent of rooted-label path;
4. the cocycle remains stable under the visible finite action.

So `107_21` now has an exact audit for the part that is genuinely
finite: the rooted descent data over the visible packet cover.

## 5. Scope boundary

This is still not a proof of full global descent on an actual arithmetic
surface.  The audit does **not** establish:

1. algebraicity or regularity of \(\mathcal X_T^{(1)}\);
2. existence of the global line object in a proved surface category;
3. compatibility of the descended line with a genuine Deligne pairing;
4. admissibility of the later boundary-completed metric.

Its role is narrower and exact: it pressure-tests the finite cocycle
shadow that `107_21` uses before any of those genuinely global claims
can be taken seriously.
