# P6 (fase 203): Δ_X(q) por clase (exterior) y pairing interior ⟨Λ_X−Λ, c_{g*}⟩. NUMÉRICO.
import json,math,sys,numpy as np
sys.argv=['x']; src=open('calib_r1.py').read()
exec("import json,math,numpy as np\nfrom sympy import factorint\nX=240.0\n"+src.split('# ---------- y-grid')[0].split('# ---------- combs: L_X = Λ_X * 1')[1])
Q=json.load(open('classes_Q_X240.json'))
cls={c:{} for c in COMBS}
for key,q in Q.items():
    a,b=map(int,key.split(',')); qq=f'{min(a,b)}/{max(a,b)}'
    for c in COMBS:
        L=Lconv[c]; tot=0.0
        for j in range(1,len(q)+1): tot+=sum(L[k*b]/k for k in range(1,j+1) if k*b<=240)*q[j-1]
        cls[c][qq]=cls[c].get(qq,0)+tot
out={}
for c in ('epstein','DH'):
    D={k:-2*(cls[c][k]-cls['zeta'][k]) for k in cls[c]}; T=sum(D.values())
    srt=sorted(D.items(),key=lambda kv:-abs(kv[1])); cum=0; top=[]
    for k,v in srt:
        cum+=v; top.append((k,v))
        if abs(cum-T)<=0.1*abs(T) and len(top)>=2: break
    out[c]=dict(total=T,n90=len(top),top=top,top20=srt[:20],sum_abs=sum(abs(v) for v in D.values()),
                exterior_by_d={d:(COMBS[c][d]-COMBS['zeta'][d]) for d in range(2,15)})
    print(c,T,len(top),sum(abs(v) for v in D.values())); print([(k,round(v,4)) for k,v in srt[:15]])
json.dump(out,open('P6_classes.json','w'),indent=1)
