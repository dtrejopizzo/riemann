# 107.54 -- Paper D A4 log-effectivity shadow audit

## 1. Purpose

`107_23` and `107_45` reduce the candidate metric to a logarithmic
normal-crossings template, but Route A item A4 of `107_12` still asks
for more than a mere singularity classification:
admissibility/semipositivity must not be destroyed by the visible
regularization steps.

The present note exact-audits the finite local shadow of that claim.  It
does not prove published semipositivity on a realized arithmetic
surface.  It proves something narrower and still load-bearing:
for every currently visible polarization-active center of `107_27`, the
candidate polarization

\[
 H_T^{(1)}=F_{{\rm v},T}^{(1)}+F_{{\rm h},T}^{(1)}
 \tag{1.1}
\]

keeps a nonnegative logarithmic support package after the corresponding
corner-preserving blow-up.

## 2. Shadow being tested

The audit uses the five local center classes A--E of `107_27`.

1. Type A: diagonal/vertical boundary center;
2. Type B: diagonal/horizontal boundary center;
3. Type C: graph/vertical boundary center;
4. Type D: graph/horizontal boundary center;
5. Type E: singular boundary point center, either on one ruling branch
   or at an isolated mixed-corner point.

The exact finite claim is:

\[
 \text{visible A1/A4 regularization center}
 \Longrightarrow
 \text{no negative coefficient enters the local log support of }H_T^{(1)}.
 \tag{2.1}
\]

Equivalently, in the local normal-crossings package
\((F_{\rm v}',F_{\rm h}',E)\) after one visible blow-up, the transformed
polarization still has coefficients in the nonnegative cone.

## 3. What the verifier checks

The script `107_54_paper_d_a4_log_effectivity_shadow_audit.py` exact-
audits four finite statements.

1. The exceptional multiplicity equals the number of polarization
   branches through the center:
   one for Types A--D and boundary-Type E, two for a mixed-corner
   Type E point.
2. After the visible blow-up, the strict transforms of both ruling
   branches keep coefficient \(1\), while the exceptional coefficient is
   that nonnegative multiplicity.
3. Because all centers are corner-preserving by `107_27`, both ruling
   branches remain visible after the blow-up.
4. The transformed support stays inside the expected normal-crossings
   package \((F_{\rm v}',F_{\rm h}',E)\), and multiplicity two occurs
   exactly at mixed-corner centers.

Everything is exact: the verifier compares integer coefficient data, not
floating approximations.

## 4. Result

The verifier passes exactly.

This means the current local regularization program has a real A4
shadow:
none of the presently visible polarization-active blow-ups forces the
candidate polarization out of the nonnegative logarithmic coefficient
cone.  In particular, the blow-up protocol now has an exact finite audit
showing that the visible exceptional package is compatible with a local
normal-crossings semipositivity template.

## 5. Scope boundary

This audit still does **not** prove the full published Route A
semipositivity/admissibility hypotheses.

It does not show:

1. positivity of the actual archimedean curvature current;
2. theorem-level semipositivity of the realized metric in a published
   Yuan--Zhang category;
3. global admissibility of the remainder term \(\psi\);
4. compatibility with a fully proved regular proper model.

Its force is finite and local:
the visible blow-up geometry of `107_26`--`107_27` no longer threatens
A4 by introducing negative logarithmic support in the candidate
polarization package.
