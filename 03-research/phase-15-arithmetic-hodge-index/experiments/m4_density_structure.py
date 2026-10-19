import mpmath as mp
mp.mp.dps = 40
logpi = mp.log(mp.pi)
Psi  = lambda r: mp.re(mp.digamma(mp.mpf('0.25')+1j*mp.mpf(r)/2)) - logpi
# Psi'(r) = -1/2 Im psi'(1/4+ir/2)
dPsi = lambda r: -mp.re(0.5*1j*mp.polygamma(1, mp.mpf('0.25')+1j*mp.mpf(r)/2))

print("=== (ii) strict monotonicity for r>0: Psi'(r) = -1/2 Im psi'(1/4+ir/2) > 0 ? ===")
print("   term sign check: Im (1/4+n+ir/2)^{-2} < 0 for r>0  =>  Psi' = -1/2 * (negative) > 0")
allpos = True
for r in [0.1,0.5,1,2,5,6.29,7,10,14.13,20,50,100,1000]:
    v = dPsi(r)
    allpos &= (v>0)
    print(f"   r={r:8}: Psi'={mp.nstr(v,8)}")
print("   all Psi'(r)>0 for r>0:", allpos)

print("\n=== (iii) unique positive zero r0 ===")
r0 = mp.findroot(Psi, 6.3)
print("   r0 =", mp.nstr(r0,18))

print("\n=== (iv) first zero of zeta vs r0  (the negativity band sits in the spectral gap) ===")
g1 = mp.im(mp.zetazero(1))
print("   gamma_1 =", mp.nstr(g1,15))
print("   r0       =", mp.nstr(r0,15))
print("   r0 < gamma_1 ?", r0 < g1, "  => negativity band (-r0,r0) is strictly inside the zero-free gap (-gamma_1,gamma_1)")
print("   Psi(gamma_1) =", mp.nstr(Psi(g1),10), "  (>0, archimedean density positive on the spectrum)")

print("\n=== Psi(r) is exactly the smooth zero-density: compare to N'(r)=(1/2pi)log(r/2pi) ===")
for r in [20,50,100,500,1000]:
    dens = Psi(r)/(2*mp.pi)
    vonmangoldt = mp.log(mp.mpf(r)/(2*mp.pi))/(2*mp.pi)
    print(f"   r={r:6}: Psi/2pi={mp.nstr(dens,10)}  N'(r)={mp.nstr(vonmangoldt,10)}  ratio={mp.nstr(dens/vonmangoldt,8)}")

# emit density CSV for the team
import csv
with open('m4_archimedean_density.csv','w',newline='') as fh:
    w=csv.writer(fh)
    w.writerow(['# M4.1 archimedean Kahler density  Psi(r)=Re psi(1/4+i r/2)-log pi'])
    w.writerow(['# r0(sign change)=%s ; gamma_1=%s ; Psi>0 exactly on |r|>r0 ; Psi<0 only in zero-free gap'%(mp.nstr(r0,12),mp.nstr(g1,10))])
    w.writerow(['r','Psi(r)','Psi_prime(r)'])
    r=mp.mpf('0')
    while r<=60:
        w.writerow([mp.nstr(r,6),mp.nstr(Psi(r),18),mp.nstr(dPsi(r),12)])
        r+=mp.mpf('0.25')
print("\n   wrote m4_archimedean_density.csv")
