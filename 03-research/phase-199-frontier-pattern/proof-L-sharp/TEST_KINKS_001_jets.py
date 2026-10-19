# TEST_KINKS_001 step 1 (mpmath, dps 130): edge jet of p = g*_50 (and g*) at T = log(15)/2, h(λ), h'(λ), h''(λ), and
# measured jet jumps of f1 = E^{-1}p = Σ_{mu<λ} μ(m)(mu)^{-1/2}p(log mu) at u = λ/m (black-box values + one-sided
# polynomial differentiation, no use of the term structure). Same Legendre normalisation as EXTERIOR_DATUM_001_exterior.py.
import json,os,pickle,mpmath as mp
from pathlib import Path
mp.mp.dps=130
SP=Path(os.environ['SP']); HERE=Path(__file__).parent; OUT=HERE/'TEST_KINKS_001_data'
mu=15; N=1664; L=mp.log(mu)/2; lam=mp.sqrt(mu)
mob=[0,1,-1,-1,0,-1,1,-1,0,0,1,-1,0,-1,1,1]
PV=pickle.load(open(SP/'rc'/'pvecs.pkl','rb')); E=json.load(open(HERE/'MORI15_EXTREMAL_001_data'/'p0_eig.json'))
def coefs(v): return [mp.mpf(str(x))*mp.sqrt(mp.mpf(2*j+1)/(2*L)) for x,j in zip(v,range(0,N,2))]
def gval(C,x):   # Σ C_t P_{2t}(x/L), Legendre recurrence
    xi=x/L; P0,P1=mp.mpf(1),xi; s=C[0]
    for n in range(1,N-1):
        P0,P1=P1,((2*n+1)*xi*P1-n*P0)/(n+1)
        if (n+1)%2==0: s+=C[(n+1)//2]*P1
    return s
res={}
for name,v in (('p',PV['pvecs']['p']),('g*',E['vectors'][0])):
    C=coefs(v); js=list(range(0,N,2))
    g0=sum(C); g1=sum(c*mp.mpf(j*(j+1))/2 for c,j in zip(C,js))/L
    g2=sum(c*mp.mpf((j-1)*j*(j+1)*(j+2))/8 for c,j in zip(C,js))/L**2
    # h(v)=v^{-1/2}g(log v): h'=v^{-3/2}(g'-g/2), h''=v^{-5/2}(g''-2g'+3g/4)
    h0=g0/mp.sqrt(lam); h1=(g1-g0/2)/lam**1.5; h2=(g2-2*g1+3*g0/4)/lam**2.5
    res[name]={'g(T)':mp.nstr(g0,25),"g'(T)":mp.nstr(g1,25),"g''(T)":mp.nstr(g2,25),"g'/g":mp.nstr(g1/g0,15),"g''/g":mp.nstr(g2/g0,15),
               'h(λ)':mp.nstr(h0,25),"h'(λ)":mp.nstr(h1,25),"h''(λ)":mp.nstr(h2,25)}
    if name!='p': continue
    f=lambda u: sum(mob[m]/mp.sqrt(m*u)*gval(C,mp.log(m*u)) for m in range(1,15) if mob[m] and m*u<lam)
    # check of the jet formulas against direct evaluation of h near λ
    d=mp.mpf(10)**-20; hv=lambda w: gval(C,mp.log(w))/mp.sqrt(w)
    res[name]["check h'(λ) by FD"]=mp.nstr((hv(lam)-hv(lam-d))/d/h1,12)
    jumps={}
    K=8; dl=mp.mpf(10)**-14
    for m in range(1,15):
        u0=lam/m; side={}
        for sg in (-1,1):
            us=[u0+sg*dl*k for k in range(1,K+1)]; fs=[f(u) for u in us]
            # interpolating polynomial in t=u-u0, read c0,c1,2c2
            A=mp.matrix([[ (sg*dl*k)**i for i in range(K)] for k in range(1,K+1)]); cc=mp.lu_solve(A,mp.matrix(fs))
            side[sg]=(cc[0],cc[1],2*cc[2])
        J=[side[-1][i]-side[1][i] for i in range(3)]
        pred=[mob[m]*h0,mob[m]*m*h1,mob[m]*m*m*h2]
        jumps[m]={'μ(m)':mob[m],'J0,J1,J2':[mp.nstr(x,20) for x in J],
                  'ratio J/pred':[mp.nstr(a/b,15) if b!=0 else None for a,b in zip(J,pred)],
                  '|J|/|h(λ)|,|J1|/|h1|,|J2|/|h2| (for μ=0)':[mp.nstr(abs(J[0]/h0),5),mp.nstr(abs(J[1]/h1),5),mp.nstr(abs(J[2]/h2),5)]}
        print(m,jumps[m],flush=True)
    res[name]['jumps']=jumps
json.dump(res,open(OUT/'jets.json','w'),indent=1); print(json.dumps({k:{a:b for a,b in v.items() if a!='jumps'} for k,v in res.items()},indent=1))
