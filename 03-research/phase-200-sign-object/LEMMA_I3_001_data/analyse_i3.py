import numpy as np, json, scipy.linalg as sl
out={}
def inert(M,tol):
    e=np.linalg.eigvalsh((M+M.T)/2); return [int((e<-tol).sum()),int((abs(e)<=tol).sum()),int((e>tol).sum())],e
# 1. In(C_RR) vs discretisation and μ
for f,lab in [('gaugeK6_mu5.npz','K6'),('gaugeK8_mu5.npz','K8')]+[(f'../P2_GAUGE_RADICAL_001_data/gauge_mu{m}.npz',f'K10_mu{m}') for m in (5,10,15)]:
    d=np.load(f); Q=d['combL']; P=d['arch']+d['AB']
    i,e=inert(Q,1e-4); ia,ea=inert(d['arch'],1e-4)
    out['CRR_'+lab]=dict(In=i,eig=[float(x) for x in e],In_arch_only=ia,PminusQ=float(abs(P-Q).max()))
# 2-4. full block
for mu in (5,10,15):
    d=np.load(f'block_mu{mu}_J8.npz')
    C=d['QRR']; B=d['QRp'].T            # B = Q_⊥R  (J x Mg)
    Qpp=d['Qpp']; Ppp=d['Ppp']
    App1=Ppp-Qpp                           # A_⊥⊥(1)
    # quotient L2 metric on ⊥ modulo gauge
    G=d['G_pp']-d['G_Rp'].T@np.linalg.solve(d['G_RR'],d['G_Rp'])
    ev,U=sl.eigh(App1,G)
    QmodC=Qpp-B@np.linalg.solve(C,B.T)      # Schur complement Q/C ("peine módulo gauge")
    iQC,eQC=inert(QmodC,1e-6)
    # full Q on V and its inertia (Haynsworth: In Q = In C + In Q/C)
    Mg=C.shape[0]; Qfull=np.block([[C,B.T],[B,Qpp]]); iQ,_=inert(Qfull,1e-6)
    # first-order coefficient on lowest quotient eigvector
    u=U[:,0]; first=float(u@QmodC@u)
    # pencil check: A(c)=P-cQ with P_RR=Q_RR, P_R⊥=Q_R⊥ imposed exactly (Guo), vs congruence formula
    chk=[]
    for c in (0.5,0.9,0.99,1.01,1.1,1.5):
        A=np.block([[(1-c)*C,(1-c)*B.T],[(1-c)*B,App1+(1-c)*Qpp]])
        iA,_=inert(A,1e-9); iD1,_=inert((1-c)*C,1e-9); iD2,_=inert(App1+(1-c)*QmodC,1e-9)
        lmin=float(sl.eigh(App1+(1-c)*QmodC,G,eigvals_only=True)[0])
        chk.append(dict(c=c,InA=iA,In_1mc_C=iD1,In_S=iD2,lmin_S=lmin))
    # gen. eigen of QmodC on quotient
    eqg=sl.eigh(QmodC,G,eigvals_only=True)
    out[f'block_mu{mu}']=dict(App1_eig_quotientL2=[float(x) for x in ev],App1_In=inert(App1,1e-9)[0],
        QmodC_In=iQC,QmodC_eig_L2=[float(x) for x in eqg],Qfull_In=iQ,first_order_uQCu=first,pencil=chk,
        ARp1_rel=float(abs(d['PRp']-d['QRp']).max()/abs(d['QRp']).max()))
json.dump(out,open('analysis_i3.json','w'),indent=1)
for k,v in out.items(): print(k,json.dumps(v)[:900])
