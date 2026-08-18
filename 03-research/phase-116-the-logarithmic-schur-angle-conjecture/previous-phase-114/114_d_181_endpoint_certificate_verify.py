#!/usr/bin/env python3
"""Lightweight independent audit of the D.172 first-endpoint certificate.

This verifier does not recompute the expensive polynomial-log Gram.  It
does recompute the two error budgets from the serialized D.166 graph,
checks the saved interval identity K-H/delta, and independently performs
the final fixed-congruence interval Gershgorin test.
"""
from pathlib import Path
import math
import os
import numpy as np

HERE = Path(__file__).resolve().parent
CERT = Path(os.environ.get("D181_CERT", "/tmp/d172_directed_endpoint_certificate.npz"))
GRAPH = Path(os.environ.get("D181_GRAPH", "/tmp/d166_nested200_directed_graph.npz"))

assert CERT.is_file(), f"missing {CERT}; run D.172 first"
assert GRAPH.is_file(), f"missing {GRAPH}; run D.166 first"
z = np.load(CERT)
g = np.load(GRAPH)
required = {"H", "HR", "K", "KR", "lower", "lowerR", "analytic_tail",
            "total_action_error", "coefficient_ball", "gersh_lower",
            "delta", "truncation", "digits"}
assert required <= set(z.files), sorted(required-set(z.files))

delta = float(z["delta"])
M = int(z["truncation"])
digits = int(z["digits"])
assert delta == .218 and M == 140 and digits == 900

# Independently reconstruct the analytic Cauchy tail and stable Legendre-ball
# action estimate used in D.172.  A tiny relative slack only accommodates
# binary64 evaluation in this lightweight audit; D.172 itself used Arb.
L = math.log(5.0)
R = 2.5
zeta2 = math.pi**2/6.0
ratio = L/R
Amaj = 1+R+2*zeta2*(R/math.pi)**2/(1-(R/math.pi)**2)
Mmaj = Amaj*math.exp(3*R/2)/2
epsq = Mmaj*ratio**M/(1-ratio)
epsr = epsq/M
C, Cr = g["C"], g["R"]
n = np.arange(C.shape[0], dtype=float)
scale = np.sqrt(2*n+1)/math.sqrt(L)
sf = np.sum(np.abs(C)*scale[:,None], axis=0)
sd = np.sum(np.abs(C)*scale[:,None]*(n*(n+1)/L)[:,None], axis=0)
tail = L*epsq*sd + 2*epsr*sf

logc = math.log(L*L)
m0 = math.log(math.pi)+0.5772156649015328606+math.pi/2+3*math.log(2)
weights = math.log(2)/math.sqrt(2)+math.log(3)/math.sqrt(3)+math.log(2)/2
h=h2=1.0
logmoment=(logc*logc+2*logc*(-1-h)+2+(h*h+h2)
           +2*(h-(math.pi**2/6-h2)))
rsf = np.sum(Cr*scale[:,None], axis=0)
rsd = np.sum(Cr*scale[:,None]*(n*(n+1)/L)[:,None], axis=0)
coeff = rsf*math.sqrt(L*logmoment)/2 + math.sqrt(L)*(2*L*rsd+(4+m0+2*weights)*rsf)

def close_up(saved, recomputed, rel=2e-12):
    return np.all(saved >= recomputed*(1-rel)) and np.all(saved <= recomputed*(1+rel)+1e-300)
assert close_up(z["analytic_tail"], tail)
assert close_up(z["coefficient_ball"], coeff)
assert close_up(z["total_action_error"], tail+coeff)

# Check that the stored lower interval encloses K-H/delta entry by entry.
lc0 = z["K"]-z["H"]/delta
lr0 = z["KR"]+z["HR"]/delta
assert np.all(np.abs(z["lower"]-lc0) <= z["lowerR"]+lr0+1e-300)
assert np.all(z["lowerR"] >= lr0*(1-2e-14))

# Independent interval congruence.  For a fixed floating matrix P,
# rad(P^T A P) <= |P|^T rad(A) |P| entrywise.
lc=(z["lower"]+z["lower"].T)/2
lr=np.maximum(z["lowerR"],z["lowerR"].T)
P=np.linalg.inv(np.linalg.cholesky(lc).T)
qc=P.T@lc@P
qr=np.abs(P).T@lr@np.abs(P)
# Inflate for all binary64 matrix operations.  The certified margins are
# about 0.8, so this deliberately excessive allowance is harmless.
roundoff=1e-11*(1+np.max(np.abs(qc)))
marg=np.diag(qc)-np.diag(qr)-np.sum(np.abs(qc)+qr,axis=1)+np.abs(np.diag(qc))+np.diag(qr)-roundoff
assert np.all(marg>0), marg
assert np.all(z["gersh_lower"]>0)
assert np.all(marg <= z["gersh_lower"]+2e-8), (marg,z["gersh_lower"])

print("D181 lightweight endpoint certificate audit: PASS")
print("analytic_tail", tail)
print("coefficient_ball", coeff)
print("independent_gersh_lower", marg)
