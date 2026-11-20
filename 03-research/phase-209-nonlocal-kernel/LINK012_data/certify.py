# Validated ball integrals (Arb/acb); tails are explicit analytic bounds.
import flint,json
from flint import arb,acb
flint.ctx.prec=128
T=arb(4)/5; pi=arb.pi(); om=pi/(2*T)
r=3*(om*om+arb(1)/4)/(9*om*om+arb(1)/4)
norm=T*(1+r*r)
def F(z):return (3*om*z).cos()+r*(om*z).cos()
def FT(z):
    def term(w):return T*(((z-w)*T).sinc()+((z+w)*T).sinc())
    return term(3*om)+r*term(om)
def integ(fun,a,b):return acb.integral(lambda z,analytic:fun(z),a,b,rel_tol=arb('1e-18'),abs_tol=arb('1e-18'),eval_limit=100000)
# Rank-one coefficient M(F), grouping integer product k=dn.
K=12
b=[]
for k in range(1,K+1):
    b.append(sum((arb(d).rsqrt()-arb(1)/d for d in range(2,k+1) if k%d==0),arb(0)))
zc=(arb(3)/2).zeta()-arb(2).zeta()
def prof(z):
    y=(2*z).exp()
    v=sum((2*(bk-zc)*(-pi*k*k*y).exp() for k,bk in enumerate(b,1)),acb(0))
    return 2*(z/2).exp()*v
M=integ(lambda z:F(z)*prof(z),-T,T).real
# b_k<=k and sum_{k>K} k exp(-a k²)<=exp(-a K²)/(2a).
a=pi*(-2*T).exp()
tailM=4*T*(1+r)*(T/2).exp()*(-a*K*K).exp()/a*(1+zc/K)
# Gamma finite frequency integral with an analytic meromorphic real-part extension.
def mg(z):return ((acb(arb(1)/4,0)+acb(0,arb(1)/2)*z).digamma()+(acb(arb(1)/4,0)-acb(0,arb(1)/2)*z).digamma())/2-pi.log()
H=arb(100)
gam=arb(0)
for j in range(100):
    gam+=integ(lambda z:mg(z)*FT(z)**2,j,j+1).real/pi
# For t>=100>6*om: |FT|<=A/t², m(t)<=2log(t)+10.
Amp=arb(8)/3*om*(r+3)
gtail=Amp*Amp/pi/H**3*(arb(2)/3*H.log()+arb(2)/9+arb(10)/3)
comb=arb(0)
for n,lam in [(2,arb(2).log()),(3,arb(3).log()),(4,arb(2).log())]:
    sh=arb(n).log()
    cor=integ(lambda z:F(z)*F(z+sh),-T,T-sh).real
    comb+=2*lam/arb(n).sqrt()*cor
qupper=(gam+gtail-comb)/norm
mlower=(abs(M)-tailM)/norm.sqrt()
kappa=-2*pi**(-arb(1)/4)*(arb(1)/4).gamma()*(arb(1)/2).zeta()
elower=kappa*mlower*mlower
out={key:str(val) for key,val in [('T',T),('r',r),('norm',norm),('M_raw_ball',M),('M_tail_bound',tailM),('gamma_finite',gam),('gamma_tail_bound',gtail),('comb',comb),('Q_upper',qupper),('M_normalized_abs_lower',mlower),('kappa',kappa),('energy_lower',elower)]}
out['verified_Q_less_002']=bool(qupper<arb('0.02'))
out['verified_energy_greater_01']=bool(elower>arb('0.1'))
print(json.dumps(out,indent=2),flush=True)
open('03-research/phase-209-nonlocal-kernel/LINK012_data/certified.json','w').write(json.dumps(out,indent=2))
assert out['verified_Q_less_002'] and out['verified_energy_greater_01']
