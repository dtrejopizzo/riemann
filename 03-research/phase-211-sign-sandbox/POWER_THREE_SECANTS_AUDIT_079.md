# POWER_THREE_SECANTS_AUDIT_079 — Independent audit

Status: **APPROVED / PROVED as implication and converse under BASE073.** Source: `POWER_THREE_SECANTS_079.md`. Two further independent checks in the same session. Papers untouched.

## Antecedents and difference

Read the project rules, the three mandatory records and the antecedents 003, 073–078. The falsifiers 003/074 remain in force: BASE alone does not suffice for three nodes. The new input is the exact comparison of secants of g(x)=a sqrt(x)/M(sqrt(x))−1. It turns its local concavity into a sufficient and necessary condition for all blocks of three, under BASE; it is not limited to the confluent jet 074. It needs neither 077 nor concavity of h=1/b.

## Algebraic checks and signs

For 0<u<v<w, beta=(g2−g1)/(v²−u²)>0, delta=beta−(g3−g2)/(w²−v²), alpha=1+g1−beta u². The positive diagonal congruence indicated in the source gives exactly T_ij=1+(ui gj+uj gi)/(ui+uj).

DET, CONC and GAP were reproduced by exact symbolic expansion; the printed factorizations constitute the proof and do not depend on that check. In particular:

- M increasing gives alpha>beta uv>0; neither alpha>=1 nor concavity between 0 and u² is needed.
- D2=w(alpha−beta uv)+beta uv(u+v)>0, even if w>u+v.
- Concavity of M gives delta<=delta_conc with the printed orientation.
- delta_crit−delta_conc=beta(w−u)uvw(alpha+beta u²)(alpha+beta v²)/[(alpha w²+beta u²v²)(v+w)D2]>0.

Thus delta>0 implies positive determinant; the positive two-point minors of 073 complete positive definiteness. If delta=0, T=alpha 11^t+beta uu^t is PSD of rank 2. The weak case beta=0 and repeated nodes are correctly separated; strict positivity refers to nonzero functions.

For the converse delta>=0 is not presupposed: alpha>beta uv still holds; if delta<0, the braces of DET are positive and the determinant is negative. Therefore all PSD 3-blocks are equivalent to concavity of g on the interval of squares, within BASE. That concavity has not been inferred from the pairs.

## Application and remaining obligation

BASE is proved for the real Phi by 073. The tail 078 g''<0 for u>=63/2 already gives strictly positive triples there, via this analytic proof. That coverage was already contained in 053 (thirteen arbitrary poles); it is not recorded as a new W region.

For admissible exponents ai=ui+1/2>1, it only remains to verify the real curvature on **1/2<u<63/2**. There is no need to resolve 0<u<1/2 for this goal. h concave ceases to be an obligation of criterion 3, although its exterior result 078 remains valid. Not claimed: compact sign, all admissible triples, higher orders, or a new time window.
