# P203.1–2: escalera de contactos W^(N). NUMÉRICO (arb 420 bits para ζ/Beurling; mpmath 60 dígitos para DH).
import json,sys,math
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-200-sign-object/F0_TEST_001_data')
import step1_comb as S
from flint import arb,ctx
from multiprocessing import Pool
import mpmath as mp
F0='/home/trabajo/Documentos/research/riemann/03-research/phase-200-sign-object/F0_TEST_001_data/'
def cshift(args):
    n,dlt=args; ctx.prec=420; u=arb(n).log()+arb(dlt); lo=-S.L; hi=S.L-u; h=(hi-lo)/2; c=(hi+lo)/2
    return n,dlt,(sum(w*S.g_at(c+h*x)*S.g_at(c+h*x+u) for x,w in S.G)*h).str(60,radius=False)
if __name__=='__main__':
    ctx.prec=420; out={}
    cm=json.load(open(F0+'step1_comb.json')); ar=json.load(open(F0+'step1_arch_NQ110.json'))
    tail=arb('1.1142709162482563e-70')+arb('1.1866644139259083e-71')
    base=arb(ar['arch_Omega'])+tail+arb(cm['pole 2AB'])   # arch verdadero + polar
    vm={2:2,3:3,4:2,5:5,7:7,8:2,9:3,11:11,13:13}
    with Pool(14) as P:
        R=P.map(S.task,[n for n in range(2,15) if n not in vm])+[(n,cm[f'c(log {n})'],None) for n in vm]
        Rb=P.map(cshift,[(2,1e-5),(2,-1e-5),(3,1e-5),(3,-1e-5)])
    c={n:arb(a) for n,a,_ in R}
    W=base; lad=[]; prev=None
    for N in range(1,15):
        if N in vm: W=W-2*arb(vm[N]).log()/arb(N).sqrt()*c[N]
        lad.append(dict(N=N,W=W.str(25),sign=('+' if W>0 else '-' if W<0 else '?'),
                        ratio=(abs((W-prev)/prev).str(8) if prev is not None else None))); prev=W
    out['zeta']=dict(c_log_n={n:c[n].str(20) for n in sorted(c)},all_c_positive=all(c[n]>0 for n in c),ladder=lad,
                     W_inf_check=W.str(15),base=base.str(30))
    print(json.dumps(out['zeta'],indent=0)[:3000])
    # Beurling: Λ en posiciones log2+δ, log3+δ (mismo g*)
    bz={}
    for n,d,v in Rb:
        dW=-2*arb(n).log()/arb(n).sqrt()*(arb(v)-c[n]); bz[f'n={n},delta={d:+g}']=dict(c=v[:30],W_T=(W+dW).str(15),dW=dW.str(10))
    out['beurling']=bz; print(bz)
    # DH: testigo certificado T=9/5 impar
    mp.mp.dps=60; D=json.load(open('/home/trabajo/Documentos/research/riemann/03-research/phase-200-sign-object/CERT_DH_001_data/vec_T1.8_odd_N260.json'))
    T=mp.mpf(9)/5; leg={int(k):mp.mpf(v) for k,v in D['leg'].items()}
    def F(t): x=t/T; return mp.fsum(a*mp.legendre(j,x) for j,a in leg.items())
    xs,ws=zip(*[(mp.mpf(a),mp.mpf(b)) for a,b in zip(*__import__('numpy').polynomial.legendre.leggauss(1))])
    import numpy as np
    gx,gw=np.polynomial.legendre.leggauss(400)
    def cF(u):
        lo,hi=-T,T-u; h=(hi-lo)/2; m=(hi+lo)/2
        return h*mp.fsum(mp.mpf(w)*F(m+h*mp.mpf(x))*F(m+h*mp.mpf(x)+u) for x,w in zip(gx,gw))
    mp.mp.dps=30
    c0=cF(mp.mpf(0)); print('c0',c0)
    s5=mp.sqrt(5); kap=(mp.sqrt(10-2*s5)-2)/(s5-1); CH={1:(1,0),2:(0,1),3:(0,-1),4:(-1,0),0:(0,0)}
    a=lambda n: CH[n%5][0]+kap*CH[n%5][1]; b={}
    for n in range(2,37): b[n]=a(n)*mp.log(n)-mp.fsum(a(d)*b[n//d] for d in range(2,n) if n%d==0)
    terms={n:2*b[n]/mp.sqrt(n)*cF(mp.log(n))/c0 for n in range(2,37)}
    final=mp.mpf('-7.05197470947908e-9'); baseD=final+mp.fsum(terms.values())
    Wd=baseD; ld=[]; prev=None
    for N in range(1,37):
        if N>=2: Wd-=terms[N]
        ld.append(dict(N=N,W_over_normF2=mp.nstr(Wd,15),b_n=mp.nstr(b.get(N,0),8),cF=mp.nstr(cF(mp.log(N))/c0,8) if N>=2 else None,
                       ratio=(mp.nstr(abs((Wd-prev)/prev),6) if prev else None))); prev=Wd
    out['DH']=dict(base_C0_plus_levy=mp.nstr(baseD,15),cert_pieces='C0 -0.621152853202, levy+tail 3.00903502865 (cert_T9_5_odd_N260.txt)',
                   c0=mp.nstr(c0,15),ladder=ld,cF_signs={n:('+' if cF(mp.log(n))>0 else '-') for n in range(2,37)})
    for r in ld: print(r)
    json.dump(out,open('P203_ladders.json','w'),indent=1)
