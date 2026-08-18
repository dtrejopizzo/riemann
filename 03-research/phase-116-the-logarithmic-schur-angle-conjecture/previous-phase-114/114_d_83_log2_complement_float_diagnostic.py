#!/usr/bin/env python3
"""Floating diagnostic for the full P--Q coupling at T=log(2).

This is deliberately NOT a certificate.  It uses high-order Gauss--Legendre
quadrature to measure ||Q A P||_HS for the moderate 160-resolvent base plus
the one-anchor tail minorant.  The calculation is stable because Q is formed
by orthogonal subtraction on every cell, rather than by subtracting nearly
equal closed exponential moments.
"""
import math
import os
import numpy as np
from numpy.polynomial.legendre import leggauss, legvander

T = math.log(2.0)
LOG5 = os.environ.get("D83_LOG5", "0") == "1"
if LOG5:T=0.5*math.log(5.0)
DEG = int(os.environ.get("D83_DEG", "9"))
D = DEG + 1
MD = int(os.environ.get("D83_MD", "20"))
ME = int(os.environ.get("D83_ME", "8"))
d = 2*math.log(2.0)-math.log(3.0)
e = 2*math.log(3.0)-3*math.log(2.0)
if LOG5:
    g1=math.log(5/4);g2=math.log(4/3);g3=math.log(6/5)
    types=[g1/15]*15+[g2/20]*20+[g3/12]*12+[g1/15]*15+[g3/12]*12+[g2/20]*20+[g1/15]*15
else:
    types = [d/MD]*MD+[e/ME]*ME+[d/MD]*MD+[d/MD]*MD+[e/ME]*ME+[d/MD]*MD
NC = len(types)
left = np.r_[-T, -T+np.cumsum(types)[:-1]]
mid = left+np.asarray(types)/2
DIM = NC*D
HS_ONLY = os.environ.get("D83_HS_ONLY", "0") == "1"
terms = [(2*j+0.5, 1.0) for j in range(160)]+[(320.5, 80.125)]
RHO = 1000.0

NQ = int(os.environ.get("D83_NQ", str(max(40, 2*DEG+8))))
t, wg = leggauss(NQ)
P = legvander(t, DEG)
CONTACTS_LOG5=[(math.log(2),math.log(2)/math.sqrt(2)),
               (math.log(3),math.log(3)/math.sqrt(3)),
               (2*math.log(2),math.log(2)/2)]

# Per-cell physical quadrature and orthonormal Legendre evaluation.
xs=[]; ws=[]; bases=[]
right=left+np.asarray(types)
for qi,(h,m) in enumerate(zip(types,mid)):
    if LOG5:
        # Refine a target cell by every translated source endpoint.  On each
        # resulting open subcell all contact images are polynomials.
        cuts=[left[qi],right[qi]]
        endpoints=np.r_[left,right[-1]]
        for shift,_ in CONTACTS_LOG5:
            for sgn in (-1,1):
                z=endpoints+sgn*shift
                cuts.extend(z[(z>left[qi]+1e-14)&(z<right[qi]-1e-14)])
        cuts=np.asarray(sorted(cuts))
        cuts=cuts[np.r_[True,np.diff(cuts)>1e-13]]
        xx=[];ww=[]
        for aa,bb in zip(cuts[:-1],cuts[1:]):
            xx.extend((aa+bb)/2+(bb-aa)*t/2)
            ww.extend((bb-aa)*wg/2)
        xx=np.asarray(xx);ww=np.asarray(ww)
        uu=2*(xx-m)/h
        xs.append(xx);ws.append(ww)
        bases.append(legvander(uu,DEG)*np.sqrt(np.arange(1,2*D,2)/h))
    else:
        xs.append(m+h*t/2)
        ws.append(h*wg/2)
        bases.append(P*np.sqrt(np.arange(1,2*D,2)/h))

hs2 = 0.0
cell_hs=[]
S=None if HS_ONLY else np.zeros((DIM,DIM))
AP=None if HS_ONLY else np.zeros((DIM,DIM))
for q in range(NC):
    xq,wq,Bq=xs[q],ws[q],bases[q]
    Y=np.zeros((len(xq),DIM))
    for b,coef in terms:
        # Same-cell action, integrated by a separate copy of the quadrature.
        Kl=np.exp(-b*np.abs(xq[:,None]-xq[None,:]))
        Y[:,q*D:(q+1)*D] -= coef*(Kl*(wq[None,:]))@Bq
        # Strictly separated cells factor exactly into exponential features.
        exm=np.exp(-b*xq)
        exp_=np.exp(b*xq)
        for j in range(q):
            fj=(ws[j]*np.exp(b*xs[j]))@bases[j]
            Y[:,j*D:(j+1)*D] -= coef*exm[:,None]*fj[None,:]
        for j in range(q+1,NC):
            fj=(ws[j]*np.exp(-b*xs[j]))@bases[j]
            Y[:,j*D:(j+1)*D] -= coef*exp_[:,None]*fj[None,:]
    # The positive rank-two moment penalty.  Contacts and scalar terms map P
    # into P exactly on this shift-compatible mesh and hence have no Q part.
    for sig in (0.5,-0.5):
        gx=np.exp(sig*xq)
        for j in range(NC):
            fj=(ws[j]*np.exp(sig*xs[j]))@bases[j]
            Y[:,j*D:(j+1)*D] += RHO*gx[:,None]*fj[None,:]
    if LOG5:
        # Full truncated translation action.  Refinement above ensures that
        # the source cell is constant on each target quadrature subcell.
        for shift,c in CONTACTS_LOG5:
            for sgn in (-1,1):
                yy=xq+sgn*shift
                inside=(yy>=-T-1e-13)&(yy<=T+1e-13)
                ids=np.searchsorted(right,yy,side='right')
                ids=np.minimum(ids,NC-1)
                for j in np.unique(ids[inside]):
                    mask=inside&(ids==j)
                    uj=2*(yy[mask]-mid[j])/types[j]
                    Bj=legvander(uj,DEG)*np.sqrt(np.arange(1,2*D,2)/types[j])
                    Y[np.where(mask)[0],j*D:(j+1)*D]-=c*Bj
    # Cellwise Q subtraction; quadrature makes B^*WB the identity to roundoff.
    proj=Bq.T@(wq[:,None]*Y)
    if not HS_ONLY:
        AP[q*D:(q+1)*D,:]=proj
    R=Y-Bq@proj
    val=float(np.sum(wq[:,None]*R*R))
    if not HS_ONLY:
        S += R.T@(wq[:,None]*R)
    hs2 += val
    cell_hs.append(val)
    if q%12==11:
        print(f"cell {q+1}/{NC}: cumulative HS^2={hs2:.12g}",flush=True)

print(f"HS^2(QAP) ~= {hs2:.17g}")
print(f"HS(QAP)   ~= {math.sqrt(hs2):.17g}")
print(f"largest cell contribution={max(cell_hs):.17g}")
if HS_ONLY:
    print("FLOAT_DIAGNOSTIC_ONLY")
    raise SystemExit(0)
# Add the scalar part and the shift contacts.  A translated cell need not be
# another cell of the mesh (this already occurs at T=log(5)/2).  We therefore
# integrate each overlap on the common refinement of the original endpoints
# and their translates.  Since both factors are degree DEG polynomials,
# DEG+1 Gauss points make every block exact up to floating roundoff.
M0=math.log(math.pi)+0.5772156649015329+math.pi/2+3*math.log(2.0)
AP += np.eye(DIM)*(sum(2*w/b for b,w in terms)-M0)

def add_translation_contact(matrix, shift, coeff):
    tq,wq=leggauss(DEG+1)
    right=left+np.asarray(types)
    # C_ij = integral phi_i(x) phi_j(x+shift) dx.  The quadratic contact is
    # -2 coeff <f,U_shift f>, hence its symmetric matrix is -coeff(C+C^T).
    C=np.zeros_like(matrix)
    for i in range(NC):
        lo_i,hi_i=left[i],right[i]
        for j in range(NC):
            lo=max(lo_i,left[j]-shift)
            hi=min(hi_i,right[j]-shift)
            if not hi>lo+2e-15:
                continue
            x=(lo+hi)/2+(hi-lo)*tq/2
            wi=(hi-lo)*wq/2
            ui=2*(x-mid[i])/types[i]
            uj=2*(x+shift-mid[j])/types[j]
            Bi=legvander(ui,DEG)*np.sqrt(np.arange(1,2*D,2)/types[i])
            Bj=legvander(uj,DEG)*np.sqrt(np.arange(1,2*D,2)/types[j])
            C[i*D:(i+1)*D,j*D:(j+1)*D]=Bi.T@(wi[:,None]*Bj)
    matrix -= coeff*(C+C.T)

if LOG5:
    # Already included in Y above, so both PAP and QAP contain the contact.
    pass
else:
    starts=[0,MD,MD+ME,2*MD+ME,3*MD+ME,3*MD+2*ME]
    for si,sj,n,c in [(starts[0],starts[3],MD,math.log(2)/math.sqrt(2)),
                      (starts[1],starts[4],ME,math.log(2)/math.sqrt(2)),
                      (starts[2],starts[5],MD,math.log(2)/math.sqrt(2)),
                      (starts[0],starts[5],MD,math.log(3)/math.sqrt(3))]:
        for u in range(n):
            i,j=si+u,sj+u
            AP[i*D:(i+1)*D,j*D:(j+1)*D]-=c*np.eye(D)
            AP[j*D:(j+1)*D,i*D:(i+1)*D]-=c*np.eye(D)
AP=(AP+AP.T)/2
S=(S+S.T)/2
if os.environ.get("D83_SAVE", "0") == "1":
    np.savez("/tmp/d83_degree%d.npz"%DEG, S=S, AP=AP)

# Parity compression.  The correction S/alpha is a rigorous *shape* to aim
# for; at this stage alpha is the analytic high-space lower bound computed
# from the local Robin gaps (its numerical value is inserted conservatively).
for name,sgn in (("even",1),("odd",-1)):
    cols=NC//2*D+(D//2 if NC%2 else 0)
    U=np.zeros((DIM,cols));col=0
    for ci in range(NC//2):
        for k in range(D):
            U[ci*D+k,col]=1/math.sqrt(2)
            U[(NC-1-ci)*D+k,col]=sgn*((-1)**k)/math.sqrt(2);col+=1
    if NC%2:
        ci=NC//2
        for k in range(D):
            if (-1)**k==sgn:U[ci*D+k,col]=1;col+=1
    assert col==cols
    Ap=U.T@AP@U; Sp=U.T@S@U
    ev=np.linalg.eigvalsh(Ap)
    # Lift the lowest mode by a large rank-one term, as in the capacity lemma.
    vv=np.linalg.eigh(Ap)[1][:,0]
    lifted=Ap+0.01*np.outer(vv,vv)-Sp/1.50
    print(f"{name}: projected first={ev[0]:.12g}, second={ev[1]:.12g}, "
          f"corrected/lifted min={np.linalg.eigvalsh(lifted)[0]:.12g}")
print("FLOAT_DIAGNOSTIC_ONLY")
