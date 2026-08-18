#!/usr/bin/env python3
"""Verifier for the Hodge-index signature of the corner pairing.

Form on the numerical quotient, in evaluation coordinates
(v_0, v_1, (v_rho)_rho):

  Ibar(v,w) = v_0 conj(w_1) + v_1 conj(w_0) - sum_rho m_rho v_rho conj(w_{rho'})
  rho' = 1 - conj(rho)

Claim:  n_+ = 1 + P,  n_- = 1 + L + P,
where L = #distinct on-line zeros, P = #off-line mirror pairs.
No zeta zeros are used as input: configurations are synthetic.
"""
import itertools, math, cmath, numpy as np
FAIL=[]
def check(n, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {extra}")
    if not ok: FAIL.append(n)

def build(onlines, offpairs, mult=None):
    """onlines: list of gamma (zero = 1/2+i gamma). offpairs: list of (beta,gamma)
       giving the mirror pair {beta+i gamma, 1-beta+i gamma}, beta != 1/2."""
    zeros=[]
    for g in onlines: zeros.append(complex(0.5,g))
    for (b,g) in offpairs:
        zeros.append(complex(b,g)); zeros.append(complex(1-b,g))
    n=2+len(zeros)
    m = {z:(mult.get(z,1) if mult else 1) for z in zeros}
    idx={('pole',0):0, ('pole',1):1}
    for i,z in enumerate(zeros): idx[('zero',i)]=2+i
    M=np.zeros((n,n),dtype=complex)
    M[0,1]=1.0; M[1,0]=1.0                       # pole block
    for i,z in enumerate(zeros):
        zp = 1-z.conjugate()
        j = min(range(len(zeros)), key=lambda k: abs(zeros[k]-zp))
        assert abs(zeros[j]-zp) < 1e-12, "mirror not in the zero set"
        M[2+i, 2+j] -= m[z]
    return M, zeros

def inertia(M, tol=1e-9):
    assert np.allclose(M, M.conj().T), "not Hermitian"
    ev = np.linalg.eigvalsh(M)
    return int((ev> tol).sum()), int((ev< -tol).sum()), int((abs(ev)<=tol).sum())

cases = [
    ([], [], 0, 0),
    ([14.13, 21.02, 25.01], [], 3, 0),
    ([14.13], [(0.6, 30.0)], 1, 1),
    ([], [(0.7, 5.0), (0.55, 9.0)], 0, 2),
    ([14.13, 21.02], [(0.6, 30.0), (0.8, 40.0), (0.51, 50.0)], 2, 3),
    (list(np.linspace(10,60,12)), [(0.6,70.0),(0.9,80.0)], 12, 2),
]
allok=True; herm=True; nondeg=True
for onl, off, L, P in cases:
    M,_ = build(onl, off)
    if not np.allclose(M, M.conj().T): herm=False
    npos, nneg, nzero = inertia(M)
    if (npos, nneg) != (1+P, 1+L+P): allok=False; print("   MISMATCH", L,P,npos,nneg)
    if nzero != 0: nondeg=False
check("form is Hermitian on every configuration", herm)
check("form is nondegenerate (radical already quotiented)", nondeg)
check("n_+ = 1+P and n_- = 1+L+P on 6 configurations", allok)

# pole block is exactly the hyperbolic plane = ruling intersection matrix
M,_ = build([14.13],[(0.6,30.0)])
check("pole block equals [[0,1],[1,0]] (the two rulings)",
      np.allclose(M[:2,:2], np.array([[0,1],[1,0]])))

# multiplicities scale blocks but do not change the signature
M2,z2 = build([14.13,21.02],[(0.6,30.0)], mult={complex(0.5,14.13):3,
                                                complex(0.6,30.0):2,
                                                complex(0.4,30.0):2})
check("multiplicities do not change the inertia", inertia(M2)[:2]==(1+1, 1+2+1))

# RH <=> n_+ = 1
rh   = all(inertia(build(onl,[])[0])[0]==1 for onl in
           [[14.13],[14.13,21.02],[10,20,30,40]])
notrh= all(inertia(build(onl,off)[0])[0]>1 for onl,off in
           [([14.13],[(0.6,30.0)]),([],[(0.7,5.0),(0.55,9.0)])])
check("n_+ = 1 exactly when no off-line zeros; n_+ > 1 otherwise", rh and notrh)

# the primitive part (v_0=v_1=0) is negative semidefinite iff no off-line zeros
def prim_inertia(onl,off):
    M,_=build(onl,off); return inertia(M[2:,2:])
check("primitive part negative definite iff RH-configuration",
      all(prim_inertia(o,[])[0]==0 for o in [[14.13],[10,20,30]]) and
      all(prim_inertia(o,f)[0]>0 for o,f in [([14.13],[(0.6,30.0)]),([],[(0.7,5.0)])]))

# evaluation functionals f -> fhat(rho) are linearly independent on C_c^infty
def mellin(f, s, a=0.2, b=6.0, N=40001):
    u=np.linspace(a,b,N); return np.trapz(f(u)*u**(s-1), u)
bumps=[(lambda u,c=c: np.exp(-30*(u-c)**2)) for c in (0.8,1.2,1.7,2.3,3.1)]
pts=[complex(0.5,3.0),complex(0.5,7.0),complex(0.6,4.0),complex(0.4,4.0),complex(1.0,0.0)]
Mv=np.array([[mellin(f,s) for s in pts] for f in bumps])
check("evaluation functionals independent: quotient surjects onto blocks",
      abs(np.linalg.det(Mv))>1e-12, f"|det| = {abs(np.linalg.det(Mv)):.3e}")

print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
