import mpmath as mp
mp.mp.dps = 30
# Resonance kernel  K_{rho,sigma} = 1/(s_rho + conj(s_sigma) - 1),  s = rho/2.
# TEST: include a genuine OFF-LINE quartet and ask whether the signature flips (=> detects kappa?).
def Kmat(resonances):
    n=len(resonances)
    K=mp.zeros(n,n)
    for a in range(n):
        for b in range(n):
            K[a,b]=1/(resonances[a]+mp.conj(resonances[b])-1)
    return K
def sig(K):
    ev,_=mp.eig(K); ev=[mp.re(x) for x in ev]
    return sum(1 for x in ev if x>1e-9), sum(1 for x in ev if x<-1e-9), sorted(ev)

# on-line zeros (resonances at 1/4 + i gamma/2)
onl=[mp.mpf('0.25')+1j*mp.im(mp.zetazero(k))/2 for k in range(1,6)]
# a FAKE off-line quartet from rho=0.7+i*20 : zeros {0.7+20i, 0.3+20i (=1-0.7), 0.7-20i, 0.3-20i}
# resonances rho/2 : {0.35+10i, 0.15+10i, 0.35-10i, 0.15-10i}
b=mp.mpf('0.7'); g=mp.mpf('20')
quartet=[ (b+1j*g)/2, ((1-b)+1j*g)/2, (b-1j*g)/2, ((1-b)-1j*g)/2 ]

print("=== on-line only (5 resonances) ===")
p,n,ev=sig(Kmat(onl)); print(f"  signature: +{p} / -{n}   eigs={[mp.nstr(x,4) for x in ev]}")
print("\n=== on-line + OFF-LINE quartet (5+4=9 resonances) ===")
p,n,ev=sig(Kmat(onl+quartet)); print(f"  signature: +{p} / -{n}")
print(f"  eigs={[mp.nstr(x,4) for x in ev]}")

print("""
THEOREM (why this is structural, not luck):
  K_{rho,sigma} = 1/(s_rho + conj(s_sigma) - 1) = -1/(w_rho + conj(w_sigma)),  w := 1/2 - s.
  For any zero in the critical strip 0<beta<1, s=rho/2 => Re(w)=(1-beta)/2 > 0.
  1/(w + conj(w')) with Re(w)>0 is the POSITIVE-DEFINITE Cauchy/Hardy kernel of the right
  half-plane ( = int_0^inf e^{-w t} conj(e^{-w' t}) dt ).  Hence K is NEGATIVE-DEFINITE for
  EVERY configuration of zeros in the strip -- on-line OR off-line.
  => the resonance pairing CANNOT be indefinite. kappa is structurally absent. RH-independent.
""")
