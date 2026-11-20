# POWER_SCHUR_BASE_AUDIT_081 — Independent audit

Status: **APPROVED / PROVED in the declared class.** Source `POWER_SCHUR_BASE_OBSTRUCTION_081.md`, read in full. Papers untouched.

## Object and antecedents

The object is the exact remainder G_p of the REAL Phi constructed in075–077, not the generic model074. Cross-checked003,073–079 and the three mandatory records.079 uses BASE073;081 checks whether that BASE is literally inherited by G_p. The result discards that particular inheritance, not a broader Schur recursion.

## Verification

The positive normalization C_p=(p²B(p)²/a)G_p gives exactly C_p=z[B(z)−B(p)]/[1−g(z)/K_p], with g=z²B and K_p=p²B(p). The limits B(p)→0, K_p→infinity come from the full real bounds078, so C_p→F=zB=a/M−1/z locally with derivatives. The limit argument already contradicts universal increasing monotonicity because F>0 and F→0.

The effective version is correct. At z*=1024, a>1/25, M(z*)<3 and M'(z*)>1/[3(z*+1/2)] imply a z*²M'/M²>4/3, whence F'(z*)<−1/(3z*²). The bounds of psi and arithmetic series keep the full comb; no new theta diagnostic is used.

With L=2g*+24a²z*²/c*² and p0=[25(L+2)]², M(p)<sqrt(p) and a>1/25 give Kp>L for all p>=p0. Thus g*/Kp<1/2. The derivative of NORMAL is correctly computed. Its first term is less than F'(z*) and the second is less than4a²/(c*²Kp)<1/(6z*²), even if its numerator were negative. It follows that G_p'(1024)<0 for all p>=p0.

Since G_p>0 on the whole half-line by077, a negative derivative prevents global concavity: the tangent line would end up negative. For each of these pivots some later point has G_p''>0.

## Scope

Only imposing on ALL real remainders G_p the conditions G_p'>0 and G_p''<=0 of BASE073 is refuted. G_p>0 remains proved. The pair criteria allow negative derivatives, and the positive Schur residue is not eliminated. No negative kernel, negative W, impossibility of general recursion nor an obstruction to the global target is proved. The continuation can change the class of preserved hypotheses;082 is separate from this conclusion.
