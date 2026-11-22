# POWER_CONTACT_FLOOR_045 — What the cutoff240 stops certifying when5 enters

Status: **PROVED within the specific declared scope**, independent review approved in [POWER_PRIMAL_AUDIT_045.md](POWER_PRIMAL_AUDIT_045.md)§1; exact verifier PASS. Specific check of an EXISTING certificate; neither a new positive region nor a NO-GO for all truncations. Papers untouched.

## 1. Reading and exact scope

Consulted the ROUTES-TRIED-INDEX index, the master grid and CROSSWORD-TO-D; read Paper46 sec:log5/app:encllog5, ROUND_007_B and ROUND_008_A/C. The proof in Paper46 up to T5=log5/2 is a matrix-and-tail certificate, not an elementary sign mechanism that fails mathematically when5 enters. Paper46 cor:beyond5 even proves positivity on some later interval by continuity.

Origin of the data: Paper46/main.tex lines11233ff fix tau_N=240, k1=280,k2=330 and140 coordinates per parity. Its lowercert at11160 requires

    s_infty<=m(tau_N)−A_T,
    q_Y=s_infty−mu−omega_+ Lambda_(k1)(T tau_N)>0,
    A_T=sum_(n in N_T) 2Lambda(n)/sqrt(n).

For mu>=0, omega_+>=0 andLambda>=0, s_infty>0 is a necessary condition of that criterion. It is shown that the SAME cutoff and the SAME total-mass floor cannot be kept when5 enters.

Decisive antecedent: ROUND_026_A§§0–3 ALREADY replaces the floor m(tau_N)−A_T by an enclosure of the REAL symbol in a band and certifies windows T=1 and207/200 by computer (scope/status there). That campaign is not repeated nor is the change of floor presented as novel. The targeted search in007/008/026 and the index did not find the specific rational comparison of this memo.

## 2. Quantitative failure of the total-mass floor

If log5/2<T<=log7/2, the new nonzero contact is5 and

    A_T=A2345=sqrt2 log2+(2/sqrt3)log3+log2
                                      +(2/sqrt5)log5>17/4.

It suffices to use log2>69/100,log3>109/100,log5>8/5, sqrt2>7/5, sqrt3<7/4,sqrt5<9/4. The verifier checks the logarithmic bounds via the existing rational intervals and the final comparison is

    (12/5)(69/100)+(8/7)(109/100)+(8/9)(8/5)>17/4.

On the other hand, m(tau)=Re psi(1/4+i tau/2)−logpi. The elementary Euler integral for Re z>0 is

    psi(z)=logz−1/(2z)+int_0^infty B1({t})/(z+t)²dt.

It is obtained by integrating by parts the sum of1/(z+n) minus its integral; the periodic term has modulus<=1/2. At z=1/4+120i,

    |remainder|<=(1/2)int_0^infty dt/[(t+1/4)²+120²]
                        <pi/480<1/100.

Moreover Re[−1/(2z)]<0, |z|<121 andpi>3. Hence

    m(240)<log(121/3)+1/100<15/4.

The last inequality is certified without numerical logarithms: the positive Taylor sum of exp(187/50) up to degree14 is greater than121/3.

It follows that

    m(240)−A2345<−1/2,
    q_Y<=s_infty−mu<−1/2 for mu>=0.                 (FIXED-FLOOR-FAIL)

Thus a hypothesis of the certificate proposal fails BEFORE proving the finite matrix. It is not a negative value of the form. The total-mass estimate does not distinguish the spatial overlap that vanishes when a contact enters; that is why it contradicts neither continuity nor the windows already certified026.

## 3. The crossings a new representation must keep

At fixed T after5 enters, write in the frequency band of lowercert

    G=G0+v5 C5, v5=2log5/sqrt5,
    C5=Q_T[1_(|tau|<tau_N)cos(tau log5)](D)Q_T.

G0 includes the chosen floor and all previous contacts, not only the archimedean part. If A_i=P_Y G0 e_i and D_i=P_Y C5 e_i, the penalized Gram of the certificate is EXACTLY

    <A_i+v5D_i,A_j+v5D_j>
     =<A_i,A_j>+v5[<A_i,D_j>+<D_i,A_j>]
                                           +v5²<D_i,D_j>.

The remaining lower matrix contains

    R_ij=(s_infty−mu)delta_ij−<G e_i,e_j>
                    −<A_i+v5D_i,A_j+v5D_j>/q_Y,
    R_(i,xi)=<e_i,chi>+<A_i+v5D_i,P_Ychi>/q_Y,
    R_(xi,xi)=c−||P_Ychi||²/q_Y.

For the complete form c=−1/2 in even parity and c=+1/2 in odd; for the primitive one c=0. After the Haynsworth step of Paper46 the finite Schur complement whose sign must be proved remains, with these complete columns. The linear crossings, the quadratic one and the polar edge have been written: dominating only the diagonal contact matrix or suppressing D_i does not control them.

These formulas reuse lowercert; they are not a new reduction. They serve as a minimal obligation for evaluating a positive pair L55-B: it must offer a real lower bound of the WHOLE form with error/slack covering those columns and the tail, or a stronger inequality that legitimately avoids them. A pair with an artificially finite-mass measure is not imposed here; the infinite tail must be treatable in the authentic class.

## 4. Limited conclusion

The existing mechanism up toT5 is Slepian+Schur certification with controlled tail, not an identified extensible elementary pattern. FIXED-FLOOR-FAIL pins down the obstacle of the inherited cutoff240. Changing the cutoff, improving the floor or repeating certifications is recorded008/026 and is not proposed as sign progress. The L55-B representation must still supply a new bound of the complete form; this note claims neither that it does nor that it is impossible.
