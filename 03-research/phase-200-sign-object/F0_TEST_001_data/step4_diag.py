# F0_TEST_001 step 4: diagnostics from step3_F.json: convexity of F on the eps-mesh, Lemma-F bound, pair matrix <h_m,h_n>,
# predicted (1,2)-dominance, F'' split by n-cutoff. Units 1e-70. NUMERICO.
import json,sys,math,os
import numpy as np
import step3_F as s3
X=float(sys.argv[1]); Wtrue=float(sys.argv[2]); ell=[4.4,8.4394,8.6018]
eps=[round(-0.05+0.005*k,4) for k in range(61)]
o=s3.run(X,eps,dy=float(os.environ.get('DY','1.5e-5')),npair=8)
e=np.array(eps); F=np.array([o['Fe'][x] for x in eps]); h=0.005
d2=(F[2:]-2*F[1:-1]+F[:-2])/h**2
print('F(0),F1,F2,F3',o['F0'],o['F1'],o['F2'],o['F3']); print('F2 = 2||Z_log r||^2 + 2<Zr,Z_log2 r> =',o['F2a'],'+',o['F2b']); print('arch,2AB,A,B',o['arch'],o['twoAB'],o['A'],o['B'])
print('mesh F:',[(x,round(y,6)) for x,y in zip(e[::5],F[::5])])
print('F2 finite-diff on mesh: min %.4f at %.3f, max %.4f; at 0: %.4f'%(d2.min(),e[1:-1][d2.argmin()],d2.max(),d2[list(e[1:-1]).index(0.0)]))
print('convex on [0,0.186]?',bool(np.all(d2[(e[1:-1]>=0)&(e[1:-1]<=0.19)]>0)))
base=o['arch']+o['twoAB']
Lb=[(x,base+(o['F0']-Fx)/x) for x,Fx in zip(e,F) if x>0]
print('W_ext',o['W_ext'],'W_true',Wtrue)
print('Lemma-F bound L(eps)=||A_eps r||^2 - F(eps)/eps:',[(x,round(y,4)) for x,y in Lb[::4]])
print('inf L over (0,0.25]: %.4f at eps=%.3f; sup %.4f'%(min(y for _,y in Lb),min(Lb,key=lambda t:t[1])[0],max(y for _,y in Lb)))
De=[(x,(Fx-o['F0'])/x-o['F1']) for x,Fx in zip(e,F) if x>0]
print('Delta_eps = (F(eps)-F(0))/eps - F1:',[(x,round(y,4)) for x,y in De[::4]])
H=np.array(o['H']); ln=np.log(np.arange(1,len(H)+1))
print('H=<h_m,h_n> (m,n<=8):'); print(np.array2string(H,precision=5,suppress_small=True,max_line_width=200))
C=(ln[:,None]+ln[None,:])**2*H
print('F2 pair terms (log m+log n)^2 H: (2,2)=%.4f, (1,2)+(2,1)=%.4f, (3,3)=%.4f, (1,3)x2=%.4f, (2,3)x2=%.4f, sum m,n<=8=%.4f, total F2=%.4f'%(C[1,1],2*C[0,1],C[2,2],2*C[0,2],2*C[1,2],C.sum(),o['F2']))
print('memo prediction 2(log2)^2(||h2||^2+<h1,h2>) = %.4f; exact (1,2)-block 4(log2)^2||h2||^2+2(log2)^2<h1,h2> = %.4f'%(2*math.log(2)**2*(H[1,1]+H[0,1]),4*math.log(2)**2*H[1,1]+2*math.log(2)**2*H[0,1]))
for x in ell: print('F2/ell for ell=%.4f: %.3f'%(x,o['F2']/x))
