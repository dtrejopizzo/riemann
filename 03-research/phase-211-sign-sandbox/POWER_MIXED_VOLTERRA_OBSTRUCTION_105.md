# POWER_MIXED_VOLTERRA_OBSTRUCTION_105 — The raw Volterra kernel changes sign

Status: **PROVED analytically; independent mathematical and literal audits approved.** No certificate is executed. The result only excludes treating the raw kernel specified below as positive. It does not refute other Volterra representations, gauges, compensations, the mixed Wronskian nor W. Papers untouched.

## 1. Consultation and difference from recorded routes

Consulted the project rules, ROUTES-TRIED-INDEX/README.md, R162_2300_MASTER_GRID.md and CROSSWORD-TO-D.md; cross-checked077/088/091/092/095 and102/103. The search for Volterra and for the kernel R(t)-T(t)tau(s) in those three indices and the POWER corpus did not find this equation for the real pair. The old Volterra references of the grid correspond to other objects.091 studies Pi(s)/s, a Peano kernel built with four-node cofactors; here there are no such nodes or cofactors. The new object is a differential kernel of the real time curvatures of103.

The motivation was to transport, via a Volterra equation with positive kernel, the original curvature comparison to the pending mixed comparison. It is proved that THAT raw kernel is not positive, using the real data and their complete tails. Impossibility of the transport after rearranging the equation is not claimed.

## 2. Real data and exact differential equation

Keep Phi,J,K of102/103, with K EVEN. For t>0 define

    V=-logPhi, p=V', q=V'', r=V''',
    tau=J/Phi, kappa=K/Phi,
    E=-tau'>0, X=tp-1, Y=p^2-q,
    R=X'/E, T=Y'/E,
    S=kappa'/tau', w=-S', D=tau S-kappa.

103 section11.4 proves S>0 and S'<0; hence w>0.102 proves (kappa/tau)'=(K/J)'<0. Since

    (kappa/tau)'=tau' D/tau^2,

one has D>0. Also R>0 because X'=p+tq>0. The data are smooth on the whole half-line; the real normalizations of the densities are kept.

From J'=-tPhi and K''=aPhi-J one obtains

    tau'=p tau-t,
    kappa''-2p kappa'+Y kappa=a-tau,
    a=M'(0)>0.

Substituting kappa'=S tau', kappa=tau S-D and w=-S' gives exactly

    E w+X S-Y D=a-tau,
    D'=-tau w, S'=-w.

Differentiating the first equality and using E'=1-q tau+pE yields

    E w'+(2-2q tau)w+X'S-Y'D=E.

Dividing by E, which is strictly positive, produces

    w'+B w+R S-T D=1,
    B=(2-2q tau)/E.                               (ODE)

No assumed sign is assigned to B nor to the combination R S-T D.

## 3. Boundary values of S,D and Volterra representation

103 already proves that tau,kappa tend to0. Since S>0 decreases strictly, there exists ell>=0 with S(t)->ell. Moreover

    kappa(t)=int_t^infinito S(s)(-tau'(s))ds,
    tau(t)=int_t^infinito(-tau'(s))ds.

The first identity uses kappa'=S tau' and the boundary value kappa(infinity)=0; its integral converges because it equals kappa(t). Hence kappa/tau is a tail average of S and lies between ell and S(t).102 proves kappa/tau=K/J->0, so that ell=0. Thus

    S(t)->0, 0<D(t)<tau(t)S(t)->0,
    S(t)=int_t^infinito w(s)ds,
    D(t)=int_t^infinito tau(s)w(s)ds.

Inserting these two identities in ODE gives the exact equation

    w'(t)+B(t)w(t)
       +int_t^infinito H(t,s)w(s)ds=1,
    H(t,s)=R(t)-T(t)tau(s), s>=t.                 (RAW-VOLTERRA)

The integral is absolutely convergent for each t: R(t),T(t) are constant with respect to s, w is integrable on the tail and tau(s)<=tau(t). The sign w>0 is proved; it is not obtained from an assumed positivity of H.

## 4. Real tail: H(t,t)<0 and H(t,s)>0 for s sufficiently large

The complete bounds of the theta jets of088/092 give, with y=pi exp(2t),

    p=2y+O(1), q=4y+O(1), r=8y+O(1), t->infinity.

Here the remainders come from the bounds already audited for the WHOLE series; no real equivalent is differentiated. In particular

    p->infinity, q/p->2, r/p^2->0.

We prove directly the only integral equivalent needed:

    tau(t)p(t)/t ->1.                            (TAU-LIMIT)

Indeed, changing s=t+u/p(t) in J(t)/Phi(t) gives

    tau(t)p(t)/t
      =int_0^infinito [1+u/(tp(t))]
                       Phi(t+u/p(t))/Phi(t)du.

For u in any compact set, the above bounds for p imply p(t+u/p(t))/p(t)->1 uniformly. Hence

    Phi(t+u/p(t))/Phi(t)
      =exp[-int_0^u p(t+v/p(t))/p(t)dv] -> exp(-u).

Since p is increasing by V''>0, the quotient of densities is at most exp(-u). For t sufficiently large, tp(t)>=1 and the whole integrand is dominated by (1+u)exp(-u), integrable. Dominated convergence proves TAU-LIMIT without any new pointwise datum.

Now X'=p+tq and Y'=2pq-r, so that

    [X'-tau Y']/(tp)
      =1/t+q/p-[tau p/t][2q/p-r/p^2]
      ->0+2-1*(4-0)=-2.                         (NEGATIVE-TAIL)

Hence X'-tau Y'<0 for all sufficiently large t. Since E>0,

    H(t,t)=R(t)-T(t)tau(t)
          =[X'(t)-tau(t)Y'(t)]/E(t)<0.

For each such fixed t, continuity in s also gives H(t,s)<0 on an interval immediately to the right of t. On the other hand tau(s)->0 and

    H(t,s)->R(t)>0 as s->infinity.

Hence H(t,s) changes sign for the SAME real pair for all sufficiently large t. Neither an optimal threshold nor point evaluations are needed.

## 5. Exact scope

RAW-VOLTERRA is not an equation with a pointwise nonnegative integral kernel. The step that would directly invoke that positivity to prove a curvature comparison or a preserved cone is excluded.

It is not claimed that the total integral has negative sign, nor that another equation obtained via gauge, integration by parts, compensation, change of unknown or rearrangement lacks a positive kernel. The sign of the fourth mixed Wronskian, the finite crossing of U, the preservation of pairs and the global sign of W remain open. All previous real results remain in force. No computation was run and no paper was modified.
