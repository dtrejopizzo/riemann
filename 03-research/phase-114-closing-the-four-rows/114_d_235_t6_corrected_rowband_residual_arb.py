#!/usr/bin/env python3
"""Directed corrected D.210 residual on Legendre rows 400:600 at T6."""
from __future__ import annotations
import os,numpy as np
from flint import arb,arb_mat,ctx

ctx.dps=int(os.environ.get('D235_DPS','160'))
TARGET=arb(os.environ.get('D235_TARGET','.134139'))
src=np.load(os.environ.get('D235_SOURCE','/tmp/t6_finite_green400_arb.npz'))
g=np.load(os.environ.get('D235_GAMMA','/tmp/t6_gamma_row400_600_col400.npz'),allow_pickle=False)
c=np.load(os.environ.get('D235_CONTACT','/tmp/t6_contact_row400_600_col400.npz'),allow_pickle=False)
assert int(g['start'])==int(c['start'])==400 and int(g['stop'])==int(c['stop'])==600
assert int(g['cols'])==int(c['cols'])==400
def balls(cc,rr):
 return arb_mat([[arb(repr(float(cc[i,j])),repr(float(rr[i,j]))) for j in range(cc.shape[1])] for i in range(cc.shape[0])])
F=balls(src['corrected_source_c'],src['corrected_source_r'])
B=balls(src['old_safe_block_c'],src['old_safe_block_r'])
PB0=src['old_whitener'];PB=arb_mat([[arb(repr(float(PB0[i,j]))) for j in range(PB0.shape[1])] for i in range(PB0.shape[0])])
gs=g['G'];cs=c['A'];Arow=arb_mat([[arb(str(gs[i,j]))+arb(str(cs[i,j])) for j in range(400)] for i in range(200)])
R=Arow*F;Q=PB.transpose()*B*PB;RW=R*PB
H=RW.transpose()*RW
S=TARGET*Q-H;S=(S+S.transpose())/2
def centre(X):return np.array([[float(X[i,j].mid()) for j in range(X.ncols())] for i in range(X.nrows())])
sc=centre(S);sc=(sc+sc.T)/2
print('HEURISTIC centre residual generalized top',np.linalg.eigvalsh(centre(H))[-1],flush=True)
print('HEURISTIC centre target Schur minimum',np.linalg.eigvalsh(sc)[0],flush=True)
if np.linalg.eigvalsh(sc)[0]<=0:
 print('CENTRE FALSIFIES PROPOSED TARGET',flush=True);raise SystemExit(2)
P0=np.linalg.inv(np.linalg.cholesky(sc).T);P=arb_mat([[arb(repr(float(P0[i,j]))) for j in range(P0.shape[1])] for i in range(P0.shape[0])])
Z=P.transpose()*S*P;marg=[]
for i in range(Z.nrows()):marg.append(Z[i,i]-sum((abs(Z[i,j]) for j in range(Z.ncols()) if i!=j),arb(0)))
worst=min(marg,key=lambda z:float(z.lower()));print('directed residual Schur Gershgorin',worst,flush=True)
assert all(z.lower()>0 for z in marg)
save=os.environ.get('D235_SAVE','/tmp/t6_corrected_row400_600_residual_arb.npz')
np.savez_compressed(save,target=np.array(float(TARGET.mid())),gersh_lower=np.array([float(z.lower()) for z in marg]),digits=np.array(ctx.dps))
print('saved',save,flush=True);print('D235 DIRECTED CORRECTED ROW-BAND RESIDUAL: PASS')
