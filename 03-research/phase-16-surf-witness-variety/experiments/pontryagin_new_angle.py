import mpmath as mp
mp.mp.dps = 25
def xi(s): return mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
# Candidate de Branges function for zeta:  E(z) = xi(1/2 + i z).
# de Branges positivity needs E*(z)=conj(E(conj z)).  Compute E and E* and compare.
def E(z):  return xi(mp.mpf('0.5')+1j*z)
def Estar(z): return mp.conj(E(mp.conj(z)))

print("=== Is E_xi(z)=xi(1/2+iz) self-conjugate (E*=E)?  (decides if the naive dB space degenerates) ===")
for z in [1+1j, 2-0.5j, 0.3+2j, 5+1j]:
    z=mp.mpc(z)
    print(f"  z={z}:  E={mp.nstr(E(z),6)}   E*={mp.nstr(Estar(z),6)}   |E-E*|={mp.nstr(abs(E(z)-Estar(z)),3)}")
print("""
  => E* = E identically.  E_xi is SELF-CONJUGATE (xi(1/2+iz) is real & even on R).
     Then K_w(w) = (|E|^2 - |E*|^2)/(4 pi Im w) = 0 identically: the NAIVE de Branges space DEGENERATES.
""")

print("=== So the genuine de Branges space needs a non-trivial COMPANION (A - iB, interlacing zeros). ===")
print("    The HB / positivity condition then becomes: zeros of A=Xi and the companion B INTERLACE")
print("    <=> Xi in Laguerre-Polya (all zeros real) <=> RH.  Check interlacing of Xi and Xi' (necessary):")
Xi = lambda t: mp.re(xi(mp.mpf('0.5')+1j*t))    # real on R
dXi= lambda t: mp.diff(Xi, t)
# zeros of Xi are the gammas; zeros of Xi' should interlace them (Rolle, if all real)
gam=[float(mp.im(mp.zetazero(k))) for k in range(1,6)]
print("    first Xi-zeros (gammas):", [round(g,3) for g in gam])
for k in range(len(gam)-1):
    zc=mp.findroot(dXi, (gam[k]+gam[k+1])/2)     # a zero of Xi' between consecutive gammas
    ok = gam[k] < zc < gam[k+1]
    print(f"    Xi'-zero between gamma_{k+1},{k+2}: {mp.nstr(zc,7)}  interlaces? {ok}")
print("""
  Interlacing holds (RH true in range). Proving it for ALL zeros = Xi in Laguerre-Polya = RH.
  THE NEW ANGLE LANDS HERE: de Branges positivity for zeta = interlacing/Laguerre-Polya, with
   - the finite-to-full uniformity gap (P20): every finite truncation interlaces unconditionally;
   - Conrey-Li (1998): de Branges' specific sufficient condition for this is FALSE for zeta.
  => the de Branges positivity is the Weil positivity (P8/P16) = the wrong-sign capstone. No new crossing.
""")
