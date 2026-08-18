#!/usr/bin/env python3
"""Directed polynomial enclosure of the D166 five-column continuum Gram.

Uses D156 after the D171 logarithm extraction.  The analytic kernels q and
R1 are replaced by exact Arb Taylor polynomials; their common Cauchy tail is
added as an L2 Gram error.  All remaining integrations are finite polynomial
and polynomial-log moments.
"""
import math, os
from pathlib import Path
import numpy as np
import sympy as sy
from flint import arb,arb_mat,arb_poly,ctx

ctx.dps=int(os.environ.get('D172_DPS','500'))
M=int(os.environ.get('D172_M','140'))
K=int(os.environ.get('D172_K','5'))
DIAGONAL_ONLY=os.environ.get('D172_DIAGONAL_ONLY','0')=='1'
XEND=int(os.environ.get('D172_X','5'));L=arb(XEND).log();T=L/2
src=np.load(os.environ.get('D172_GRAPH','/tmp/d166_nested200_directed_graph.npz'))
N=int(src['C'].shape[0])
assert src['C'].shape==src['R'].shape==(N,K)
assert src['K'].shape==src['KR'].shape==(K,K)
# Expand exact decimal centres only.  Independent coefficient balls are
# propagated later in the stable Legendre basis by a D156 action bound;
# expanding them into monomials would create artificial interval dependency.
if 'C_native' in src.files:
 native_strings=src['C_native'];knative_strings=src['K_native']
 assert native_strings.shape==(N,K) and knative_strings.shape==(K,K)
 native=[[arb(str(native_strings[i,j])) for j in range(K)] for i in range(N)]
 X=arb_mat([[arb(native[i][j].mid()) for j in range(K)] for i in range(N)])
 Xrad=[[arb(native[i][j].rad()) for j in range(K)] for i in range(N)]
 Kfinal=arb_mat([[arb(str(knative_strings[i,j])) for j in range(K)] for i in range(K)])
 print('loaded native post-Schur graph balls',flush=True)
else:
 X=arb_mat([[arb(repr(float(src['C'][i,j]))) for j in range(K)] for i in range(N)])
 Xrad=[[arb(repr(float(src['R'][i,j]))) for j in range(K)] for i in range(N)]
 Kfinal=arb_mat([[arb(repr(float(src['K'][i,j])),repr(float(src['KR'][i,j]))) for j in range(K)] for i in range(K)])

def padd(a,b):
 n=max(len(a),len(b));return [(a[i] if i<len(a) else arb(0))+(b[i] if i<len(b) else arb(0)) for i in range(n)]
def pscale(a,c):return [c*x for x in a]
def pmul(a,b):
 return list((arb_poly(a)*arb_poly(b)).coeffs())
def pshift(a,h): # p(x+h)
 out=[arb(0) for _ in a]
 hp=[arb(1)]
 for _ in range(1,len(a)):hp.append(hp[-1]*h)
 for k,c in enumerate(a):
  for j in range(k+1):out[j]+=c*math.comb(k,j)*hp[k-j]
 return out
def pone_minus_pow(p):return [arb(((-1)**j)*math.comb(p,j)) for j in range(p+1)]
def preflect(a): # p(1-x)
 out=[arb(0) for _ in a]
 for k,c in enumerate(a):
  for j,z in enumerate(OM[k] if 'OM' in globals() else pone_minus_pow(k)):out[j]+=c*z
 return out
def pder_divfac(a,r):
 out=a[:]
 for step in range(1,r+1):out=[arb(k+1)*out[k+1]/step for k in range(len(out)-1)]
 return out

# Exact shifted Legendre polynomials P_n(2x-1), then physical synthesis.
P=[[arb(1)],[arb(-1),arb(2)]]
for n in range(1,N-1):
 xp=[-z for z in P[n]]+[arb(0)]
 for k,z in enumerate(P[n]):xp[k+1]+=2*z
 num=padd(pscale(xp,2*n+1),pscale(P[n-1],-n))
 P.append(pscale(num,arb(1)/(n+1)))
F=[]
for a in range(K):
 f=[arb(0) for _ in range(N)]
 for n in range(N):
  sc=arb(2*n+1).sqrt()/L.sqrt()*X[n,a]
  for j,z in enumerate(P[n]):f[j]+=sc*z
 F.append(f)

# q(z)=1/2 [2z/(e^(2z)-1)] e^(3z/2), with exact rational coefficients.
q=[]
for n in range(M):
 val=sy.Rational(0)
 for k in range(n+1):
  # SymPy uses the second Bernoulli convention B_1=+1/2, while
  # z/(exp(z)-1) requires the first convention B_1=-1/2.
  bk=-sy.Rational(1,2) if k==1 else sy.bernoulli(k)
  val+=bk*sy.Rational(2)**k/sy.factorial(k)*sy.Rational(3,2)**(n-k)/sy.factorial(n-k)
 val/=2
 q.append(arb(int(val.p))/int(val.q))
r1=[arb(2).log()+arb.pi()/4]+[-q[n]/n for n in range(1,M)]

# Polynomial analytic Gamma remainder.
OM=[pone_minus_pow(p) for p in range(M+N+2)]
Qleft=[]
for r in range(1,N):
 ql=[arb(0) for _ in range(M+r)]
 for n in range(M):ql[n+r]=q[n]*L**n/(n+r)
 Qleft.append(ql)
print('common Q polynomials ready',flush=True)

def left_operator(f):
 u=[arb(0)];dr=f[:]
 for r in range(1,N):
  dr=[arb(k+1)*dr[k+1]/r for k in range(len(dr)-1)]
  u=padd(u,pscale(pmul(dr,Qleft[r-1]),(-1)**(r+1)))
 return u

Ubase=[]
for a in range(K):
 f=F[a]
 u=padd(left_operator(f),preflect(left_operator(preflect(f))))
 rl=[r1[n]*L**n for n in range(M)]
 rr=preflect(rl)
 u=padd(u,pmul(f,padd(rl,rr)))
 m0=arb.pi().log()+arb.const_euler()+arb.pi()/2+3*arb(2).log()
 u=padd(u,pscale(f,-m0))
 Ubase.append(u)
 print('analytic polynomial column',a+1,'degree',len(u)-1,flush=True)

# Contact cells in x.  On each cell add the exact active translated
# polynomials.  Endpoints retain tags so logarithmic primitives use limits.
contacts=[];points=[(arb(0),'zero'),(arb(1),'one')]
for nn,lam in ((2,arb(2).log()),(3,arb(3).log()),(4,arb(2).log()),(5,arb(5).log())):
 if nn>=XEND:continue
 d=arb(nn).log()/L;w=lam/arb(nn).sqrt();contacts.append((d,w));points.extend([(d,'mid'),(1-d,'mid')])
points.sort(key=lambda z:float(z[0].mid()))

# Every translated source polynomial is reused on several contact cells.
# Cache the shifts once; recomputing the triangular Taylor transform inside
# cell_u multiplies the directed runtime by the number of cells.
FSHIFT={}
for a in range(K):
 for ic,(d,w) in enumerate(contacts):
  FSHIFT[(a,ic,1)]=pshift(F[a],d)
  FSHIFT[(a,ic,-1)]=pshift(F[a],-d)

def cell_u(a,mid):
 u=Ubase[a][:]
 for ic,(d,w) in enumerate(contacts):
  if mid < 1-d:u=padd(u,pscale(FSHIFT[(a,ic,1)],-w))
  if mid > d:u=padd(u,pscale(FSHIFT[(a,ic,-1)],-w))
 return u

def harmonic(a,p=1):return sum((arb(1)/arb(j)**p for j in range(1,a+1)),arb(0))
NCELL=len(points)-1
Ucells=[[cell_u(a,(points[ic][0]+points[ic+1][0])/2) for a in range(K)] for ic in range(NCELL)]
MAXDEG=2*(N+M)+8
def primitive_arrays(point):
 z,tag=point;plain=[];logx=[];log1=[];zp=arb(1);series=arb(0);harm=arb(0)
 for m in range(MAXDEG+1):
  aa=m+1;zp*=z;harm+=arb(1)/aa
  plain.append(zp/aa)
  logx.append(arb(0) if tag=='zero' else zp*(z.log()/aa-arb(1)/(aa*aa)))
  if tag=='zero':log1.append(arb(0))
  elif tag=='one':log1.append(-harm/aa)
  else:
   series+=zp/aa
   log1.append((zp-1)*(-z).log1p()/aa-series/aa)
 return {'plain':plain,'logx':logx,'log1':log1}
PRIMS=[primitive_arrays(z) for z in points]
def integrate_poly(p,ic,kind='plain'):
 vals0=PRIMS[ic][kind];vals1=PRIMS[ic+1][kind]
 return sum((c*(vals1[m]-vals0[m]) for m,c in enumerate(p)),arb(0))

# Exact singular-singular block on [0,1].
logc=(L*L).log();H=arb_mat(K,K)
for a in range(K):
 for b in (range(a,K) if not DIAGONAL_ONLY else (a,)):
  ff=pmul(F[a],F[b]);ss=arb(0)
  for m,c in enumerate(ff):
   aa=m+1;h=harmonic(aa);h2=harmonic(aa,2)
   lx=-arb(1)/(aa*aa);l1=-h/aa
   lx2=arb(2)/(aa**3);l12=(h*h+h2)/aa
   mix=h/(aa*aa)-(arb(2).zeta()-h2)/aa
   moment=logc*logc/aa+2*logc*(lx+l1)+lx2+l12+2*mix
   ss+=c*moment/4
  total=ss
  for ic in range(len(points)-1):
   ua,ub=Ucells[ic][a],Ucells[ic][b]
   total+=integrate_poly(pmul(ua,ub),ic)
   cross=padd(pmul(F[a],ub),pmul(F[b],ua))
   total-= (logc*integrate_poly(cross,ic)
            +integrate_poly(cross,ic,'logx')
            +integrate_poly(cross,ic,'log1'))/2
  H[a,b]=H[b,a]=L*total

# Uniform Taylor-tail bound.  On |z|=R=2.5 the absolute Bernoulli
# majorant of 2z/(e^(2z)-1) is bounded by the displayed geometric sum.
R=arb('2.5');zeta2=arb(2).zeta();ratio=L/R
Amaj=1+R+2*zeta2*(R/arb.pi())**2/(1-(R/arb.pi())**2)
Mmaj=Amaj*(3*R/2).exp()/2
epsq=Mmaj*ratio**M/(1-ratio);epsr=epsq/M
errs=[]
for a in range(K):
 sf=arb(0);sd=arb(0)
 for n in range(N):
  amp=abs(X[n,a])*arb(2*n+1).sqrt()/L.sqrt()
  sf+=amp;sd+=amp*n*(n+1)/L
 errs.append(L*epsq*sd+2*epsr*sf)
print('uniform analytic tail errors=',errs,flush=True)
analytic_tail=errs[:]

# Stable propagation of the serialized post-Schur graph balls.  On the real
# interval |P_n|<=1 and |dP_n/dt|<=n(n+1)/L.  D156 gives q<=2 and R1<=2;
# contacts are bounded translations.  The explicit logarithmic term is
# handled by its exact L2 moment.
input_err=[]
m0=arb.pi().log()+arb.const_euler()+arb.pi()/2+3*arb(2).log()
weights=sum((lam/arb(nn).sqrt() for nn,lam in
             ((2,arb(2).log()),(3,arb(3).log()),(4,arb(2).log()),(5,arb(5).log()))
             if nn<XEND),arb(0))
h=harmonic(1);h2=harmonic(1,2);aa=1
logmoment=(logc*logc+2*logc*(-1-h)+2+(h*h+h2)+2*(h-(arb(2).zeta()-h2)))
for a in range(K):
 sf=arb(0);sd=arb(0)
 for n in range(N):
  amp=Xrad[n][a]*arb(2*n+1).sqrt()/L.sqrt();sf+=amp;sd+=amp*n*(n+1)/L
 sing=sf*(L*logmoment).sqrt()/2
 regular=L.sqrt()*(2*L*sd+(4+m0+2*weights)*sf)
 input_err.append(sing+regular)
errs=[errs[a]+input_err[a] for a in range(K)]
print('coefficient-ball action errors=',input_err,flush=True)

norms=[H[a,a].upper().sqrt() for a in range(K)]
for a in range(K):
 for b in range(K):
  if DIAGONAL_ONLY and a!=b:continue
  ea=L.sqrt()*errs[a];eb=L.sqrt()*errs[b]
  er=ea*norms[b]+eb*norms[a]+ea*eb
  H[a,b]+=arb(0,er)

DELTA=arb(os.environ.get('D172_DELTA','.218'))
if DIAGONAL_ONLY:
 trace_upper=sum((H[a,a].upper() for a in range(K)),arb(0))
 print('directed action trace upper=',trace_upper,flush=True)
 print('directed scalar-gap capacity trace upper=',trace_upper/DELTA,
       flush=True)
 target=os.environ.get('D172_TRACE_TARGET')
 if target is not None:assert trace_upper/DELTA<arb(target)
 np.savez(os.environ.get('D172_SAVE','/tmp/d172_directed_trace.npz'),
  Hdiag=np.array([float(H[a,a].mid()) for a in range(K)]),
  HdiagR=np.array([float(H[a,a].rad()) for a in range(K)]),
  trace_upper=np.array(str(trace_upper.upper())),
  capacity_trace_upper=np.array(str((trace_upper/DELTA).upper())),
  analytic_tail=np.array([float(x.upper()) for x in analytic_tail]),
  total_action_error=np.array([float(x.upper()) for x in errs]),
  coefficient_ball=np.array([float(x.upper()) for x in input_err]),
  delta=np.array(float(os.environ.get('D172_DELTA','.218'))),
  truncation=np.array(M),digits=np.array(ctx.dps),endpoint=np.array(XEND))
 print('D172 DIRECTED DIAGONAL ACTION TRACE: PASS')
 raise SystemExit(0)
lower=Kfinal-H/DELTA
def centre(A):return np.array([[float(A[i,j].mid()) for j in range(A.ncols())] for i in range(A.nrows())])
lc=centre(lower);lc=(lc+lc.T)/2
print('H centre diag=',np.diag(centre(H)),flush=True)
print('lower centre eig=',np.linalg.eigvalsh(lc),flush=True)
assert np.linalg.eigvalsh(lc)[0]>0
P0=np.linalg.inv(np.linalg.cholesky(lc).T)
P=arb_mat([[arb(repr(float(P0[i,j]))) for j in range(K)] for i in range(K)])
Q=P.transpose()*lower*P;marg=[]
for i in range(K):marg.append(Q[i,i]-sum((abs(Q[i,j]) for j in range(K) if j!=i),arb(0)))
print('directed final Gershgorin=',marg,flush=True)
print('directed Gershgorin lower endpoints=',[x.lower() for x in marg],flush=True)
assert all(x.lower()>0 for x in marg)

def pack(A):
 c=np.array([[float(A[i,j].mid()) for j in range(A.ncols())] for i in range(A.nrows())])
 r=np.array([[float(A[i,j].rad()) for j in range(A.ncols())] for i in range(A.nrows())])
 r=np.nextafter(r+np.abs(np.spacing(c))/2,np.inf)
 return c,r
HC,HR=pack(H);KC,KR=pack(Kfinal);LC,LR=pack(lower)
np.savez(os.environ.get('D172_SAVE','/tmp/d172_directed_endpoint_certificate.npz'),
 H=HC,HR=HR,K=KC,KR=KR,lower=LC,lowerR=LR,
 analytic_tail=np.array([float(x.upper()) for x in analytic_tail]),
 total_action_error=np.array([float(x.upper()) for x in errs]),
 coefficient_ball=np.array([float(x.upper()) for x in input_err]),
 gersh_lower=np.array([float(x.lower()) for x in marg]),
 delta=np.array(float(os.environ.get('D172_DELTA','.218'))),truncation=np.array(M),digits=np.array(ctx.dps),endpoint=np.array(XEND))
print('D172 DIRECTED CONTRACTED CONTINUUM GRAM AND FINAL SCHUR: PASS')
