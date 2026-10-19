from v11_rplus import *
L5,L15=float(mp.log(5)/2),float(mp.log(15)/2)
bat=[]
for T in (L5,L15,1.0,1.6,1.8): bat.append(('Lambda',T,lambda N:comb_Lambda(N)))
for P in ((2,),(2,3),(5,),(7,)):
    for T in (0.60,0.80,0.973): bat.append(('a_P'+str(P),T,(lambda P: lambda N:comb_Lambda(N,drop=P))(P)))
for c in (0.9,1.1,1.15,2):
    for T in (1.0,L5): bat.append(('cLambda c=%s'%c,T,(lambda c: lambda N:comb_Lambda(N,c=c))(c)))
bat.append(('Epstein',1.6,comb_epstein)); bat.append(('DH',1.8,comb_DH))
for T in (1.0,L5,L15): bat.append(('Beurling',T,comb_beurling))
tests=[('bump',[1])]+[('leg%d'%i,[random.choice([-1,1])*random.random() for _ in range(5)]) for i in range(5)]
kaps=[('k=%s'%k,(lambda k: lambda m,kk:k)(k)) for k in (0,0.05,0.2,0.5,-0.1)]
rc={}
def krand(m,k):
    key=(m,k)
    if key not in rc: rc[key]=random.uniform(-0.3,0.6)
    return rc[key]
kaps.append(('k=random_cell',krand))
res=[]; summary=[]
for (name,T,cf) in bat:
    N=int(mp.floor(mp.e**(2*T))); comb=cf(N+1)
    for tn,co in tests:
        g=gfam(T,co)
        for kn,kf in kaps:
            a=analyse(comb,T,g,kf)
            res.append(dict(X=name,T=T,g=tn,kappa=kn,**a))
            summary.append((name,round(T,4),tn,kn,a['N'],a['nnz'],a['rank'],a['rplus_upper'],a['I'],a['offblock']))
# diagonal invariance check
g=gfam(L15,[1]); comb=comb_Lambda(16)
a0=analyse(comb,L15,g,lambda m,k:0.05)
a1=analyse(comb,L15,g,lambda m,k:0.05,scale=lambda r:F(1+r[0]*r[1],3))
diag=dict(before=[a0['rank'],a0['rplus_upper']],after=[a1['rank'],a1['rplus_upper']],same_support=a0['support']==a1['support'])
# kappa/c changes support
sup={}
for c in (1,0.9,1.1,2):
    for kn,kf in kaps[:4]:
        sup[(c,kn)]=analyse(comb_Lambda(6,c=c),L5,gfam(L5,[1]),kf)['support']
supdiff={f"{c},{kn}":(sup[(c,kn)]!=sup[(1,kn)]) for (c,kn) in sup}
json.dump(dict(results=res,diag=diag,support_changes_vs_c1=supdiff),open('v11_results.json','w'))
import collections
print('rows',len(summary),'max rank',max(s[6] for s in summary),'I values',collections.Counter(s[8] for s in summary),'offblock',max(s[9] for s in summary))
agg=collections.defaultdict(lambda:[99,0,set()])
for s in summary:
    k=(s[0],s[1]); agg[k][0]=min(agg[k][0],s[6]); agg[k][1]=max(agg[k][1],s[6]); agg[k][2].add(s[8])
for k,v in agg.items(): print(k,'rows',[s[4] for s in summary if (s[0],s[1])==k][0],'rank',v[0],'-',v[1],'I',sorted(v[2]))
print('diag',diag); print('supdiff',supdiff)
