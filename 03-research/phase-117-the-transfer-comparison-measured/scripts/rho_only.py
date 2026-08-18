import math, numpy as np, rowd_source as RS
def rho_of(N, nc):
    EG,LL = RS.source_defect(N, ncell=nc)
    DN = EG-LL
    delta=0.5*math.log((N+1)/N)
    u=np.ones(nc)/math.sqrt(delta)
    E0=np.linalg.svd(np.ones((1,nc)))[2][1:].T
    dN=float(u@DN@u); bN=E0.T@DN@u; CN=0.5*(E0.T@DN@E0+(E0.T@DN@E0).T)
    rho=float(bN@np.linalg.pinv(CN,rcond=1e-11)@bN/dN)
    # also the two generalized minima quoted in the paper's table
    iL=np.linalg.pinv(LL,rcond=1e-11)
    import scipy.linalg as sla
    q_full=sla.eigh(0.5*(EG+EG.T),0.5*(LL+LL.T),eigvals_only=True).min()
    EG0=E0.T@EG@E0; LL0=E0.T@LL@E0
    q_zero=sla.eigh(0.5*(EG0+EG0.T),0.5*(LL0+LL0.T),eigvals_only=True).min()
    return rho,dN,q_full,q_zero
if __name__=='__main__':
    paper={10:(5.1436,8.2823,0.0156),20:(4.9506,8.9386,0.0175),40:(4.8129,9.6305,0.0150),
           80:(4.5263,10.2950,0.0116),120:(4.4563,10.6917,0.0118)}
    print("paper audit table (12 bins) vs mesh refinement")
    print(f"{'N':>4} {'bins':>5} {'minQ/A':>9} {'minQ/A|0':>9} {'rho_N':>9} | {'paper minQ/A':>12} {'paper rho':>10} {'1/(20lnN)':>10} {'viol':>5}")
    for N in (10,20,40,80,120):
        for nc in (12,20,32,48):
            rho,dN,qf,qz=rho_of(N,nc)
            b=1/(20*math.log(N))
            pm=f"{paper[N][0]:.4f}" if nc==12 else ""
            pr=f"{paper[N][2]:.4f}" if nc==12 else ""
            print(f"{N:>4} {nc:>5} {qf:>9.4f} {qz:>9.4f} {rho:>9.5f} | {pm:>12} {pr:>10} {b:>10.5f} {'YES' if rho>b else '':>5}")
        print()
