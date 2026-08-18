#!/usr/bin/env python3
"""Directed Gamma row-band cache for the stable post-cutoff residual."""
from __future__ import annotations
import importlib.util,os
from pathlib import Path
import numpy as np
from flint import arb,ctx

HERE=Path(__file__).resolve().parent
START=int(os.environ.get('D232_START','400'))
STOP=int(os.environ.get('D232_STOP','600'))
COLS=int(os.environ.get('D232_COLS','200'))
DPS=int(os.environ.get('D232_DPS','5000'))
ctx.dps=DPS;T=arb(6).log()/2
sp=importlib.util.spec_from_file_location('d147',HERE/'114_d_147_hurwitz_gamma_arb.py')
d=importlib.util.module_from_spec(sp);sp.loader.exec_module(d)
print('computing directed Gamma row band',START,STOP,COLS,flush=True)
G=d.exact_gamma_rowband(START,STOP,COLS,DPS,T)
c=np.array([[float(G[i,j].mid()) for j in range(COLS)] for i in range(STOP-START)])
r=np.array([[float(G[i,j].rad()) for j in range(COLS)] for i in range(STOP-START)])
assert np.isfinite(c).all() and np.isfinite(r).all()
r=np.nextafter(r+np.abs(np.spacing(c))/2,np.inf)
native_dps=int(os.environ.get('D232_NATIVE_DPS','250'));ctx.dps=native_dps
s=np.array([[str(G[i,j]+arb(0)) for j in range(COLS)] for i in range(STOP-START)],dtype=str)
save=os.environ.get('D232_SAVE','/tmp/t6_gamma_row400_600_col200.npz')
np.savez_compressed(save,C=c,R=r,G=s,start=np.array(START),stop=np.array(STOP),
 cols=np.array(COLS),source_digits=np.array(DPS),digits=np.array(native_dps))
print('max serialized radius',r.max(),flush=True)
print('saved',save,flush=True)
print('D232 DIRECTED GAMMA ROW BAND: PASS')
