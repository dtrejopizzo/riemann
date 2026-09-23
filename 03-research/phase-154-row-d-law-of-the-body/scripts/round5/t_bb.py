import sys, math, pickle, time, numpy as np
sys.path.insert(0,'../round4')
import r5core as C
r=pickle.load(open('../round4/lp_c24_it1.pkl','rb'))
T,v=r['T'],r['v']; tau1,P,N=float(r['tau1']),float(r['P']),int(r['N'])
a=np.asarray(r['a']); us=np.asarray(r['us']); b0,b1=float(r['b0']),float(r['b1'])
print("T",T,"atoms",len(us),"P",P,"L",C.lip(T,us,a,b0,b1,v),"M2",C.m2bound(T,us,a,b0,b1,v))
for which,lo,hi in [('f',0.0,tau1),('h0',tau1,tau1+P),('h1',tau1,tau1+P),('h2',tau1,tau1+P)]:
    fn=lambda t,w=which: C.hval(t,w,T,us,a,b0,b1,v,P,N)
    mu,arg=C.fine_min(fn,lo,hi,2e-5)
    print(which,"finemin",mu,arg)
t0=time.time()
tot=0
for which,lo,hi in [('f',0.0,tau1),('h0',tau1,tau1+P),('h1',tau1,tau1+P),('h2',tau1,tau1+P)]:
    res=C.bb_taylor(which,lo,hi,T,us,a,b0,b1,v,P,N,8.8578563e-05,wmin=1e-9)
    tot+=res['evals']
    print(which,res['lb'],res['evals'],res['final_intervals'],f"{time.time()-t0:.0f}s")
print("TOTAL evals",tot,"vs round4 2.372e8; time",time.time()-t0)
