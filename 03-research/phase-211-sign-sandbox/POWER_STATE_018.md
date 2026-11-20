# State018 — Three full rows and pending arithmetic obligation

Status: partial results PROVED, global sign OPEN. Goal active. Papers untouched. Replaces STATE017 as the current summary.

## Sufficient target and proved region

By POWER_SCALAR_BRIDGE_017 it suffices to prove the sign of the WHOLE table H_(N,k)=s^k/(s+u)^(N+k), N>=1,k>=0, at a fixed rate u=63/2. The positive representation of densities by Bernstein elevation keeps all cross terms and the polar; the strong bridge014 connects to the data of Paper47.

Proved regions: N1 for ALL k with margin4/3; N2 and N3 for ALL k with margin1/8; and ALL N>=2,k>=10000N² with margin49/50 at u31.5. Rows1,2,3 also hold for all u>=31.5. In addition the certificates of eight arbitrary poles and of the fixed confluent block of dimension12 remain valid.

Missing, as sufficient target, N>=4 and 0<=k<10000N². It is not claimed that all those points lack any particular certificate; the region not covered by the earlier uniform theorems is identified.

## Positive progress018

POWER_TABLE_DESCENT_018 proves rows2/3 with the real multiplier and all contacts. Archimedean covariance reduces to k0, bounds of two digamma derivatives control ARCH, WRN017 controls the full comb, and keeping the parity of the polar avoids losing the margin at N3.

The exact recurrence a_(N,k)=a_(N,k+1)+u²a_(N+1,k) turns these theorems into strictly positive first and second differences of row1 for ALL k. It does not prove full monotonicity nor allow extrapolating to all orders. The proof was read and tools/power_table_descent_018_verify.py reproduced with PASS; an independent review approved the constants and the scope.

## Quantified limit of the absolute error

POWER_LOW_TABLE_018 computes for k0 the exact budget D_N(theta)=2+2theta J_N(theta−1/2), using E0(x)=psi_Lambda(x)−x+1 to fix the endpoint. D_N(0)=2; for theta<1/2 it tends to1/(1/2−theta); at theta1/2 it grows like sqrt(N); for theta>1/2 it grows like sqrt(N)[1−(theta−1/2)²/u²]^(-N), in the declared integrability range.

The central signed residue and the cancellation of the polar with the main term were known. The novelty is the exact budget for this row, not a new sign theorem nor a global prohibition. Endpoints, integration by parts and the three regimes were reviewed independently. The consolidated audit is saved in POWER_TABLE_AUDIT_018 and was read.

## What changes in the next construction

A campaign row4,row5,... will not be continued as a substitute for the universal step. Round019 looks for a SIGNED inequality of the arithmetic error or of the full differences that controls variable orders. It must be cross-checked against the corpus and keep the full comb. Recurrence identities and finite certificates alone do not supply that sign.

No earlier result by itself certifies a new window T>log(5)/2. Closure requires completing the sufficient target or proving the sign directly for all admissible data. There is no counterexample to the real form W nor global closure.

## Model delimiting structural descent

POWER_TABLE_AUDIT_018 §3 proves an explicit falsifier of the inference based only on recurrences and positive regions. V[f]=2||f||²−(u/100)|F(iu)|² keeps the filter identities, margins of all spaces of up to12 poles>=u, the three full rows and the positive cone. However its entry N40402,k40401 is negative, by an elementary inequality for central binomial coefficients. All those computations were reviewed independently, including the uniformity of rows as the pole varies.

V is NOT the form W of the paper; it does not keep the concrete arithmetic nor the precise logarithmic profile. The result shows exactly why those structural data do not suffice and forces the use of additional arithmetic information. The objective is not declared blocked and the real sign is not refuted.
