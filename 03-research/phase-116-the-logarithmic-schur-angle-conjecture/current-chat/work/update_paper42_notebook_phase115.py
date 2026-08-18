"""Insert the phase-115 row-(d) chain into paper 42's Colab notebook.

The transformation is idempotent: cells whose ids start with ``p115-`` are
removed before the current version is inserted.  The notebook remains
self-contained.  Large-N runs are explicitly sampled numerical audits, not
certificates of the full infinite-dimensional statement.
"""

from __future__ import annotations

import json
from pathlib import Path


NOTEBOOK = Path(
    "/Users/davidalejandrotrejopizzo/Documents/riemann/04-papers/"
    "42-arithmetic-lefschetz-programme/certificates/"
    "arithmetic_lefschetz_certificates.ipynb"
)


def lines(text: str) -> list[str]:
    return [line + "\n" for line in text.strip("\n").split("\n")]


def md(cell_id: str, text: str) -> dict:
    return {
        "cell_type": "markdown",
        "id": cell_id,
        "metadata": {},
        "source": lines(text),
    }


def code(cell_id: str, text: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "id": cell_id,
        "metadata": {},
        "outputs": [],
        "source": lines(text),
    }


INTRO = r"""
### D.7 — Reciprocal bands and connected-cluster payment (**PAPER THEOREM + FINITE AUDIT**)

For $N\ge2$, put $\delta_N=\frac12\log((N+1)/N)$.  Rational leakage cells
are intervals $\log(a/b)+(0,\delta_N)$.  The proved reciprocal half-integer
band theorem says that no cell crosses any barrier

\[
1,\frac32,2,\frac52,\ldots,
\qquad
1,\frac23,\frac12,\frac25,\ldots.
\]

Indeed, the logarithmic distance from a reduced rational on the lower side
of a barrier is at least $\log(1+1/(2N))>\delta_N$.  Every connected cluster
therefore has hull

\[
D_C\le \log(3/2)+\delta_N
\le\frac32\log(3/2)<\sqrt{24}.
\]

The Gamma--Tate support-hull lemma consequently pays every connected
cluster, including all coherent interference inside it.  Positive
coefficients also give a uniform non-cancellation bound for each individual
band in the Gamma-deficit window.  The unresolved issue is recombination of
different bands, not another local-cell estimate.
"""


BAND_CODE = r"""
import numpy as np
from collections import defaultdict
from math import pi
import gc, random, time

def delta_N(N):
    return 0.5*np.log((N+1.0)/N)

def barrier_margin(N):
    return np.log1p(1.0/(2*N))-delta_N(N)

for N in [2,3,10,100,1000,10000,100000]:
    assert barrier_margin(N)>0
    diameter=np.log(1.5)+delta_N(N)
    assert diameter<=1.5*np.log(1.5)<np.sqrt(24)

print('D.7 EXACT FORMULA AUDIT PASS through N=100000')
print('  minimum displayed barrier margin =',barrier_margin(100000))
print('  universal hull bound =',1.5*np.log(1.5))
"""


SCHUR_MD = r"""
### D.8 — Exact constant/mean-zero Schur reduction (**EXACT**)

Define

\[
\mathfrak A_N[e]=\|\mathbf L_Ne\|^2,
\qquad
\mathfrak Q_N[e]=\mathcal E_{\Gamma T,N}(e),
\qquad
\mathfrak D_N=\mathfrak Q_N-\mathfrak A_N,
\]

and split

\[
E_N=\mathbb C u_N\oplus E_N^0,
\qquad
u_N=\delta_N^{-1/2}\mathbf1_{(0,\delta_N)},
\qquad
E_N^0=\{h:\int h=0\}.
\]

Then

\[
\mathfrak D_N=
\begin{pmatrix}d_N&b_N^*\\b_N&C_N\end{pmatrix}.
\]

The unit Gamma--Tate inequality is equivalent to

\[
C_N\ge0,
\qquad b_N\in\operatorname{Ran}C_N^{1/2},
\qquad d_N-b_N^*C_N^\dagger b_N\ge0.
\]

When $d_N>0$, define the squared Schur angle

\[
\rho_N=\frac{b_N^*C_N^\dagger b_N}{d_N}.
\]

The phase-115 candidate is $\rho_N\le(20\log N)^{-1}$ for $N\ge3$.
This bound is a **CONJECTURE**, not a consequence of the numerical cells.
"""


ARITHMETIC_CODE = r"""
def von_mangoldt_np(N):
    lam=np.zeros(N+1,dtype=float)
    sieve=np.ones(N+1,dtype=bool); sieve[:2]=False
    for p in range(2,N+1):
        if not sieve[p]: continue
        q=p
        while q<=N:
            lam[q]=np.log(p)
            if q>N//p: break
            q*=p
        if p*p<=N: sieve[p*p:N+1:p]=False
    return lam

def divisors_up_to_np(N):
    divs=[[] for _ in range(N+1)]
    for d in range(1,N+1):
        for n in range(d,N+1,d): divs[n].append(d)
    return divs

def lambda_powers_exact(N,lam,divs):
    powers=[]; prev=np.zeros(N+1); prev[1]=1.0
    for _ in range(1,int(np.log2(N))+1):
        cur=np.zeros(N+1)
        for n in range(2,N+1):
            cur[n]=sum(prev[d]*lam[n//d] for d in divs[n])
        powers.append(cur); prev=cur
    return powers

def lambda_powers_fast(N,lam):
    prime_powers=np.flatnonzero(lam>0)
    powers=[]; prev=np.zeros(N+1); prev[1]=1.0
    for _ in range(1,int(np.log2(N))+1):
        cur=np.zeros(N+1)
        for q in prime_powers:
            cur[q::q]+=lam[q]*prev[1:N//q+1]
        powers.append(cur); prev=cur
    return powers

def leakage_coefficients_exact(N,lam,powers):
    out=[]; logN=np.log(N); prime_powers=np.flatnonzero(lam>0)
    for k,lk in enumerate(powers,start=1):
        coeff=defaultdict(float)
        ms=np.flatnonzero(lk>0)
        for m in ms:
            xm=lk[m]/(np.sqrt(m)*logN**k)
            for n in prime_powers:
                if m%n==0: continue
                g=np.gcd(m,n); a=m//g; b=n//g
                coeff[(int(a),int(b))]+=lam[n]*xm/np.sqrt(n)
        if coeff: out.append(coeff)
    return out

def sampled_leakage_coefficients(N,samples_per_depth=1500,seed=115):
    # Importance-sampled all-depth leakage; NUMERICAL AUDIT ONLY.
    rng=np.random.default_rng(seed+N)
    lam=von_mangoldt_np(N); powers=lambda_powers_fast(N,lam)
    ns=np.flatnonzero(lam>0); wn=lam[ns]/np.sqrt(ns); zn=wn.sum()
    pn=wn/zn; out=[]; diagnostics=[]; logN=np.log(N)
    for k,lk in enumerate(powers,start=1):
        ms=np.flatnonzero(lk>0)
        if not len(ms): continue
        wm=lk[ms]/np.sqrt(ms); zm=wm.sum(); pm=wm/zm
        draw=max(samples_per_depth,300)
        md=rng.choice(ms,size=draw,replace=True,p=pm)
        nd=rng.choice(ns,size=draw,replace=True,p=pn)
        valid=np.array([m%n!=0 for m,n in zip(md,nd)],dtype=bool)
        accepted=int(valid.sum())
        if not accepted: continue
        total_valid=zm*zn*(accepted/draw)/(logN**k)
        atom=total_valid/accepted
        coeff=defaultdict(float)
        for m,n in zip(md[valid],nd[valid]):
            g=np.gcd(int(m),int(n))
            coeff[(int(m)//g,int(n)//g)]+=atom
        out.append(coeff)
        diagnostics.append((k,accepted,len(coeff)))
    return out,diagnostics

print('D.8 arithmetic engines ready')
"""


NUMERICS_CODE = r"""
def gamma_multiplier_np(tau):
    z=0.25+0.5j*tau.astype(float)
    correction=np.zeros_like(z,dtype=np.complex128)
    for _ in range(12):
        correction-=1.0/z; z+=1.0
    inv=1.0/z; inv2=inv*inv
    psi=(np.log(z)-0.5*inv-inv2/12+inv2**2/120-inv2**3/252+
         inv2**4/240-5*inv2**5/660+correction)
    psi_quarter=-0.5772156649015329-np.pi/2-3*np.log(2)
    return np.real(psi)-psi_quarter

def gram_tate_np(L,R):
    return np.array([[np.exp(R)-np.exp(L),R-L],
                     [R-L,np.exp(-L)-np.exp(-R)]],float)

def schur_scan_from_coefficients(N,coeffs,bins=4,points_per_bin=3,padding=1.1):
    delta=delta_N(N); L=-np.log(N); R=np.log(N/2)+delta
    dt=delta/(bins*points_per_bin); pad=padding*(R-L)
    grid_L=L-pad; grid_R=R+pad
    size=int(np.ceil((grid_R-grid_L)/dt)); fft_size=1<<(size-1).bit_length()
    t=grid_L+dt*np.arange(fft_size)
    tau=2*np.pi*np.fft.fftfreq(fft_size,d=dt)
    ggamma=gamma_multiplier_np(tau); Ginv=np.linalg.inv(gram_tate_np(L,R))
    A=np.zeros((bins,bins)); Qg=np.zeros_like(A); Qt=np.zeros_like(A)
    basis_amp=1/np.sqrt(delta/bins)
    for coeff in coeffs:
        B=np.zeros((fft_size,bins),dtype=float)
        for (a,b),val in coeff.items():
            start=int(round((np.log(a/b)-grid_L)/dt))
            for j in range(bins):
                lo=start+j*points_per_bin; hi=lo+points_per_bin
                if 0<=lo and hi<=fft_size: B[lo:hi,j]+=val*basis_amp
        A+=dt*(B.T@B)
        F=dt*np.fft.fft(B,axis=0)
        Qg+=np.real(F.conj().T@(ggamma[:,None]*F))/(fft_size*dt)
        moments=np.vstack([dt*(np.exp(t/2)@B),dt*(np.exp(-t/2)@B)])
        Qt+=moments.T@Ginv@moments
        del B,F,moments; gc.collect()
    A=(A+A.T)/2; Q=(Qg+Qg.T)/2+(Qt+Qt.T)/2; D=(Q-A+(Q-A).T)/2
    ae,au=np.linalg.eigh(A); keep=ae>max(ae[-1]*1e-10,1e-12)
    X=au[:,keep]@np.diag(1/np.sqrt(ae[keep]))
    ratios=np.linalg.eigvalsh((X.T@Q@X+(X.T@Q@X).T)/2)
    c=np.ones(bins)/np.sqrt(bins)
    O,_=np.linalg.qr(np.column_stack([c,np.eye(bins)[:,:-1]]))
    if O[:,0]@c<0: O[:,0]*=-1
    d=float(O[:,0]@D@O[:,0]); b0=O[:,1:].T@D@O[:,0]
    C=(O[:,1:].T@D@O[:,1:]); C=(C+C.T)/2
    ce=np.linalg.eigvalsh(C)
    schur=d-float(b0@np.linalg.solve(C,b0))
    rho=(d-schur)/d
    # Generalized quotient on the exact mean-zero coordinate subspace.
    Z=np.zeros((bins,bins-1))
    for j in range(bins-1): Z[j,j]=1; Z[-1,j]=-1
    Az=Z.T@A@Z; Qz=Z.T@Q@Z
    ze,zu=np.linalg.eigh((Az+Az.T)/2); zk=ze>max(ze[-1]*1e-10,1e-12)
    ZX=zu[:,zk]@np.diag(1/np.sqrt(ze[zk]))
    zero_ratios=np.linalg.eigvalsh((ZX.T@Qz@ZX+(ZX.T@Qz@ZX).T)/2)
    return dict(N=N,bins=bins,ratio_min=float(ratios[0]),
                mean_zero_ratio_min=float(zero_ratios[0]),d_N=d,
                C_min=float(ce[0]),schur=schur,rho=rho,
                rho_log_N=rho*np.log(N),fft_size=fft_size)

print('D.8 Gamma--Tate/Schur numerical engine ready')
"""


EXACT_MD = r"""
### D.9 — Moderate-threshold full arithmetic scan (**NUMERICAL AUDIT**)

This cell reconstructs every arithmetic pair in the chosen thresholds,
includes all nonzero word depths, and evaluates the piecewise-constant
Galerkin Schur block.  Floating-point quadrature and finite cell profiles
make it an audit, not an interval proof or an infinite-dimensional theorem.
"""


EXACT_RUN = r"""
RUN_PHASE115_EXACT=True
PHASE115_EXACT_THRESHOLDS=[10,40,120,260,500,1000,2000]
phase115_exact=[]
if RUN_PHASE115_EXACT:
    for N in PHASE115_EXACT_THRESHOLDS:
        started=time.time(); lam=von_mangoldt_np(N)
        divs=divisors_up_to_np(N); powers=lambda_powers_exact(N,lam,divs)
        coeffs=leakage_coefficients_exact(N,lam,powers)
        row=schur_scan_from_coefficients(N,coeffs,bins=4,points_per_bin=3,padding=1.1)
        row['mode']='FULL ARITHMETIC / FINITE GALERKIN'
        row['seconds']=time.time()-started; phase115_exact.append(row)
        print(row)
        del lam,divs,powers,coeffs; gc.collect()
print('D.9 NUMERICAL AUDIT COMPLETE')
"""


LARGE_MD = r"""
### D.10 — Stratified attempt through $N=100000$ (**SAMPLED NUMERICAL AUDIT**)

The complete pair set grows too quickly for a Colab `Run all` computation.
For $N>2000$ this cell importance-samples the positive unaggregated
$(m,n)$ leakage measure at every word depth, aggregates equal reduced
rational labels, and evaluates a three-bin Schur model.  Two bins are not
used because reflection symmetry would force a spurious zero cross block.
The target list ends
at $100000$ as requested.

This experiment can reveal or refute numerical patterns.  It is **not** a
certificate of the full coefficient set, arbitrary cell profiles, the
infinite-dimensional range condition, or the Logarithmic Schur Angle
Conjecture.  Sparse sampling can underresolve near-colliding rational labels
and therefore bias the measured Schur angle downward.  Results from this
cell must not be compared to the complete moderate-$N$ scan without a
sample-size convergence study.  Increase `PHASE115_SAMPLES_PER_DEPTH` for
such tests.
The $N=100000$ FFT may require a high-memory Colab runtime.
"""


LARGE_RUN = r"""
RUN_PHASE115_100K_ATTEMPT=True
PHASE115_LARGE_TARGETS=[3000,10000,30000,100000]
PHASE115_SAMPLES_PER_DEPTH=1500
phase115_large=[]
if RUN_PHASE115_100K_ATTEMPT:
    for N in PHASE115_LARGE_TARGETS:
        started=time.time()
        coeffs,sampling=sampled_leakage_coefficients(
            N,samples_per_depth=PHASE115_SAMPLES_PER_DEPTH,seed=115)
        row=schur_scan_from_coefficients(N,coeffs,bins=3,points_per_bin=1,padding=0.05)
        row['mode']='IMPORTANCE-SAMPLED LEAKAGE / THREE-BIN GALERKIN'
        row['samples_per_depth']=PHASE115_SAMPLES_PER_DEPTH
        row['sampled_depths']=len(sampling); row['seconds']=time.time()-started
        phase115_large.append(row); print(row)
        del coeffs,sampling; gc.collect()
print('D.10 SAMPLED ATTEMPT COMPLETE')
"""


PATTERN_MD = r"""
### D.11 — Pattern test and the exact remaining theorem

The diagnostic quantity is

\[
\rho_N\log N.
\]

The phase-115 computations through $N=2000$ place it near
$0.03$--$0.047$ on the tested finite-dimensional spaces.  The candidate
$\rho_N\le(20\log N)^{-1}$ is accepted by a row below only when the computed
value is finite and below $1/20$.  Passing this executable assertion does
not promote the candidate to a theorem.
"""


PATTERN_CODE = r"""
phase115_rows=phase115_exact+phase115_large
for row in phase115_rows:
    row['candidate_finite_model_pass']=bool(
        row['C_min']>=0 and row['d_N']>0 and row['schur']>=0 and
        np.isfinite(row['rho_log_N']) and row['rho_log_N']<=1/20)
    print(row['N'],row['mode'],
          'Q/A=',row['ratio_min'],
          'zero Q/A=',row['mean_zero_ratio_min'],
          'rho log N=',row['rho_log_N'],
          'candidate finite-model pass=',row['candidate_finite_model_pass'])

PHASE115_LEDGER={
 'reciprocal_half_integer_bands':'PAPER THEOREM; formula audit PASS',
 'connected_cluster_gamma_tate_payment':'PAPER THEOREM',
 'constant_mean_zero_schur_reduction':'EXACT',
 'moderate_N_schur_scan':'NUMERICAL AUDIT',
 'N_100000_attempt':'SAMPLED NUMERICAL AUDIT',
 'logarithmic_schur_angle_bound':'CONJECTURE / OPEN',
 'row_d_global_positivity':'CONDITIONAL ON CONJECTURE',
 'RH':'NOT CLAIMED'}
print(json.dumps(PHASE115_LEDGER,indent=2))
"""


STATUS_MD = r"""
### D.12 — What is proved and what remains

| D component | Status | Notebook role |
|---|---|---|
| Gamma--Euler--Tate amplitude and exact rational leakage | **proved** | exact identities and finite arithmetic reconstruction |
| Reciprocal half-integer barriers | **proved** | exact formula audit through $N=100000$ |
| Uniform diameter and payment of every connected cluster | **proved** | theorem recorded; representative finite audit |
| No low-frequency fugitive inside one band | **proved** | positive-coefficient phase bound |
| Constant/mean-zero Schur decomposition | **proved** | exact block algebra |
| Finite-dimensional values of $C_N,d_N,\rho_N$ | numerical evidence | full moderate scan and sampled attempt through $100000$ |
| $C_N\ge0$, range condition and $\rho_N\le(20\log N)^{-1}$ for all $N$ and arbitrary profiles | **conjecture / open** | finite computations cannot establish the universal statement |
| Global row (d) | **conditional on the preceding conjecture** | construction complete; positivity not unconditional |
| RH | **not proved** | follows only after unconditional global row (d) and the audited A--C interfaces |

The remaining mathematical task is a weighted logarithmic uncertainty and
cross-functional estimate

\[
|b_N(h)|^2\le \frac{d_N}{20\log N}\,C_N[h]
\qquad(h\in E_N^0),
\]

including the actual Gamma, Tate and leakage cross terms.  This single
estimate would give the range condition and the scalar Schur inequality.
"""


NEW_CELLS = [
    md("p115-bands-md", INTRO),
    code("p115-bands-code", BAND_CODE),
    md("p115-schur-md", SCHUR_MD),
    code("p115-arithmetic-code", ARITHMETIC_CODE),
    code("p115-numerics-code", NUMERICS_CODE),
    md("p115-exact-md", EXACT_MD),
    code("p115-exact-run", EXACT_RUN),
    md("p115-large-md", LARGE_MD),
    code("p115-large-run", LARGE_RUN),
    md("p115-pattern-md", PATTERN_MD),
    code("p115-pattern-code", PATTERN_CODE),
    md("p115-status-md", STATUS_MD),
]


def main() -> None:
    notebook = json.loads(NOTEBOOK.read_text())
    opening = "".join(notebook["cells"][0].get("source", []))
    opening = opening.replace(
        "standard library, SymPy and mpmath.",
        "standard library, NumPy, SymPy and mpmath.",
    )
    old_scope = (
        "Rows A, B and C are tested within the periodic–cohomological–nuclear contract\n"
        "stated in the paper.  For row D the notebook certifies the completed local\n"
        "and reduction steps, but it does **not** claim the still-missing global Hodge\n"
        "inequality or RH."
    )
    new_scope = (
        "Rows A, B and C are tested within the periodic–cohomological–nuclear contract\n"
        "stated in the paper. For row D the notebook records the completed boundary,\n"
        "band and Schur constructions and runs numerical diagnostics through a sampled\n"
        "attempt at $N=100000$. Global positivity remains conditional on the explicitly\n"
        "labelled Logarithmic Schur Angle Conjecture; RH is not claimed."
    )
    opening = opening.replace(old_scope, new_scope)
    notebook["cells"][0]["source"] = lines(opening)
    notebook["cells"] = [
        cell for cell in notebook["cells"]
        if not str(cell.get("id", "")).startswith("p115-")
    ]
    insertion = next(
        i for i, cell in enumerate(notebook["cells"])
        if (
            "### D.7 — What is proved and what remains" in "".join(cell.get("source", []))
            or "### D.13 — Scope note" in "".join(cell.get("source", []))
        )
    )
    notebook["cells"][insertion:insertion] = NEW_CELLS

    # Replace the old D status cell with a pointer to the expanded ledger.
    old_status = next(
        cell for cell in notebook["cells"]
        if (
            "### D.7 — What is proved and what remains" in "".join(cell.get("source", []))
            or "### D.13 — Scope note" in "".join(cell.get("source", []))
        )
    )
    old_status["source"] = lines(
        "### D.13 — Scope note\n\n"
        "Sections D.7--D.12 supersede the earlier short status table.  "
        "The executable evidence reaches a sampled attempt at $N=100000$, "
        "but the universal logarithmic Schur-angle estimate remains a "
        "conjecture."
    )

    final_code = next(
        cell for cell in notebook["cells"]
        if "CERTIFICATE_LEDGER={" in "".join(cell.get("source", []))
    )
    final_code["source"] = lines(
        "CERTIFICATE_LEDGER={\n"
        " 'A_periodic_DN_contract':'paper proof + exact/finite companion checks PASS',\n"
        " 'B_Witt_dynamic_contact':'paper proof + exact cyclotomic checks PASS',\n"
        " 'C_nuclear_Lefschetz':'paper/cited theorem + exact coefficient checks PASS',\n"
        " 'D_full_space_through_log2':'paper proof; COMPLETE',\n"
        " 'D_reciprocal_bands_and_connected_clusters':'paper theorem; COMPLETE',\n"
        " 'D_mean_zero_Schur_reduction':'exact algebra; COMPLETE',\n"
        " 'D_logarithmic_Schur_angle':'CONJECTURE / OPEN',\n"
        " 'D_global_Hodge_inequality':'CONDITIONAL ON CONJECTURE',\n"
        " 'RH':'NOT CLAIMED'}\n"
        "assert CERTIFICATE_LEDGER['D_logarithmic_Schur_angle']=='CONJECTURE / OPEN'\n"
        "assert CERTIFICATE_LEDGER['RH']=='NOT CLAIMED'\n"
        "RUN_ALL_OK=True\n"
        "print(json.dumps(CERTIFICATE_LEDGER,indent=2,ensure_ascii=False))\n"
        "print('\\nALL EXECUTABLE CELLS PASS — scope labels above remain binding.')"
    )

    notebook.setdefault("metadata", {})["phase115"] = {
        "updated": "2026-08-14",
        "large_n_target": 100000,
        "large_n_status": "sampled numerical audit",
        "global_row_d": "conditional on logarithmic Schur-angle conjecture",
    }
    NOTEBOOK.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n")
    print(NOTEBOOK)
    print("cells", len(notebook["cells"]))


if __name__ == "__main__":
    main()
