from mpmath import mp,mpf,quad,sin,cos,cosh,sqrt,pi,log,mangoldt,sinh
mp.dps=30
T=log(15)/2; X=15
w=lambda k: pi*k/(2*T)
e=lambda k,x: sin(w(k)*(x+T))/sqrt(T)
def Gq(k,l,u): return quad(lambda x:e(k,x)*e(l,x+u),[-T,T-u])
def Gc(k,l,u):
  a,b=w(k),w(l); s=(-1)**(k+l)
  if k==l: return ((2*T-u)*cos(a*u)+sin(a*u)/a)/(2*T)
  return ((sin(b*u)-s*sin(a*u))/(a-b)+(sin(b*u)+s*sin(a*u))/(a+b))/(2*T)
for k,l,u in [(1,3,0.7),(1,1,0.7),(2,5,1.1),(3,5,2.0),(4,4,0.3)]:
  print(k,l,u,Gq(k,l,u)-Gc(k,l,u))
ns=[n for n in range(2,X) if mangoldt(n)>0]; v={n:2*mangoldt(n)/sqrt(n) for n in ns}
D=lambda o: sum(v[n]*sin(o*log(n)) for n in ns)
C=lambda o: sum(v[n]*(1-log(n)/(2*T))*cos(o*log(n)) for n in ns)
for k,l in [(1,3),(3,5),(2,4),(1,1),(5,5)]:
  q=sum(v[n]*Gq(k,l,log(n)) for n in ns); a,b=w(k),w(l)
  f=(C(a)+D(a)/(2*T*a)) if k==l else ((D(b)-D(a))/(a-b)+(D(a)+D(b))/(a+b))/(2*T)
  print(k,l,q-f)
for k in [1,3,7]:
  ck=2*w(k)*cosh(T/2)/(sqrt(T)*(mpf(1)/4+w(k)**2)); print(k,quad(lambda x:cosh(x/2)*e(k,x),[-T,T])-ck)
print(quad(lambda x:cosh(x/2)**2,[-T,T])-(T+sinh(T)))
