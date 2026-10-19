# AUDIT_L_SHARP_11: mpmath re-check of the constants of PROOF_L_SHARP_Z_001 (Clausen, D_layer by quadrature, w_n sums, bounds, D(15)).
import mpmath as mp
mp.mp.dps=30
cl=mp.clsin(2,2*mp.pi/3); print('Cl2',cl, cl/(2*mp.pi), cl/(4*mp.pi))
for mu in (4,15,100,1000):
    Dl=mp.mpf(2)/3*mp.log(4*mu)-cl/(2*mp.pi)
    # direct quadrature of layer diagonal
    q=2/mp.pi*mp.quad(lambda t: mp.log(2*mu)-mp.log(mp.sin(2*t)),[0,mp.pi/4,mp.pi/3])
    w=lambda n: n/((n*n+1)*mp.sqrt(n*n-1))
    B=4/mp.pi/mp.sqrt(mu)*mp.nsum(lambda n: w(n)*mp.log(mu*(1+n**-2)),[2,mp.inf])
    print(mu,'Dlayer',mp.nstr(Dl,8),'quad',mp.nstr(q,8),'bound',mp.nstr(B,6))
w=lambda n: n/((n*n+1)*mp.sqrt(n*n-1))
print('w2,w3,w5',w(2),w(3),w(5),'Σw',mp.nsum(w,[2,mp.inf]),'Σw log n',mp.nsum(lambda n:w(n)*mp.log(n),[2,mp.inf]))
# full D(15) with H cells: ∫_1^∞ [H(ω)log(μω²/√(ω²−1)) − 2H1(ω)] (2/π)dω/(ω√(ω²−1))
mu=15
def cell(n):
    H=mp.harmonic(n); H1=mp.fsum(mp.log(k)/k for k in range(1,n+1))
    f=lambda o:(H*mp.log(mu*o*o/mp.sqrt(o*o-1))-2*H1)*2/mp.pi/(o*mp.sqrt(o*o-1))
    return mp.quad(f,[n,n+1])
D=mp.nsum(cell,[1,mp.inf]) if False else mp.fsum(cell(n) for n in range(1,4000))
print('D(15) approx (cells<4000)',D)
# ratios
c=2*mp.pi*15; R2=4/mp.pi/mp.sqrt(15)*mp.log(15*1.25)*w(2); R3=4/mp.pi/mp.sqrt(15)*mp.log(15*(1+1/9.))*w(3)
print('R2,R3 per unit mass',R2,R3,'/log60',R2/mp.log(60),R3/mp.log(60),' s2 z=c/2',c/2)
