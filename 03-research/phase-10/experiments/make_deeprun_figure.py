#!/usr/bin/env python3
"""Save the M10.1->M10.3 deep-run figure (N_BASIS=12, up to T=1e4, 10154 zeros cached)."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- deep-run data (reported by the user's Colab run) ---
d1   = np.array([1.0,1.5,2.0,2.5,3.0,3.5,4.0])
g1   = np.array([3.526e-1,5.377e-3,7.831e-11,1.143e-13,2.554e-15,1.305e-10,3.665e-11])  # |bare gap|
d2   = np.array([1.5,2.0,2.5,3.0,3.5,4.0])
g2   = np.array([0.1479,0.3257,0.4591,0.6199,0.7246,0.7397])
T3   = np.array([50,100,300,1000,3000,10000.])
g3   = np.array([0.2844,0.2810,0.2485,0.2904,0.2042,0.1108])
bmin = np.array([0.475,0.372,0.374,0.392,0.365,0.313])

fig,ax=plt.subplots(1,3,figsize=(17,4.6))
fig.suptitle("Phase 10 cohomological turn — deep run (M=25, T up to 1e4, 10154 zeros)", fontsize=13)

ax[0].semilogy(d1,np.maximum(g1,1e-16),'o-')
ax[0].axvspan(1.7,4.1,alpha=0.08,color='red')
ax[0].set_title("M10.1  bare Hodge gap → 0 (DEGENERATION)")
ax[0].set_xlabel("band d"); ax[0].set_ylabel(r"$\lambda_{\min}(\mathfrak{t})$")
ax[0].annotate("definite\n(curve-like)",(1.05,1e-1)); ax[0].annotate("degenerate\n(→ ζ)",(2.7,1e-13))

ax[1].plot(d2,g2,'s-',color='C2')
ax[1].set_title("M10.2  regularized gap SURVIVES (>0, definite)")
ax[1].set_xlabel("band d"); ax[1].set_ylabel(r"$\lambda_{\min}(G)$"); ax[1].set_ylim(0,1)

ax[2].plot(T3,g3,'^-',color='C3',label=r"$\lambda_{\min}(G)$ measured")
ax[2].plot(T3,(np.pi**2/6)*bmin**2,'k--',alpha=0.6,label=r"$(\pi^2/6)\,\beta_{\min}^2$ (tight-pair law)")
ax[2].set_xscale('log'); ax[2].set_title(r"M10.3  frame bound vs height — governed by $\beta_{\min}$")
ax[2].set_xlabel("height $T_0$"); ax[2].set_ylabel(r"$\lambda_{\min}(G)$"); ax[2].set_ylim(0,0.5)
ax[2].annotate("dip = tighter pair\n"+r"($\beta_{\min}=0.31$)",(3000,0.13))
ax[2].legend(fontsize=9)

plt.tight_layout(rect=[0,0,1,0.95])
out="../deeprun_M10.1-M10.3.png"
plt.savefig(out,dpi=130,bbox_inches='tight')
print("saved",out)
