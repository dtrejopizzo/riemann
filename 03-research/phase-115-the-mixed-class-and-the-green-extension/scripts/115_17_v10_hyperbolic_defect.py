from mpmath import mp
mp.dps = 30

# F = normalized indicator of (-T,T):  F = (2T)^{-1/2} 1_{(-T,T)}
# Fhat(tau) = int F(t) e^{i tau t} dt = (2T)^{-1/2} * 2 sin(tau T)/tau
# h(tau) = |Fhat(tau)|^2 ;  h(+-i/2) analytic continuation:
#   Fhat(i/2)  = int F e^{-t/2} = M_-F ,  Fhat(-i/2) = M_+F
# Polar term of Riemann-Weil:  h(i/2)+h(-i/2) = 2 Re( M_-F conj(M_+F) )
#                            = 2( |<F,h_e>|^2 - |<F,h_o>|^2 ),  h_e=cosh(t/2), h_o=sinh(t/2)

def report(T, nz):
    T  = mp.mpf(T)
    c  = 1/mp.sqrt(2*T)
    Fh = lambda tau: c*2*mp.sin(tau*T)/tau
    Mm = c*2*(mp.e**(T/2) - mp.e**(-T/2))      # int_{-T}^{T} e^{-t/2} dt = 2(e^{T/2}-e^{-T/2})
    Mp = Mm                                     # F even  =>  M_+ = M_-
    he = (Mm+Mp)/2                              # <F,h_e>
    ho = (Mp-Mm)/2                              # <F,h_o>  = 0
    polar = 2*(he**2 - ho**2)
    S = mp.mpf(0); last = None
    for k in range(1, nz+1):
        g = mp.im(mp.zetazero(k))
        S += 2*Fh(g)**2                         # +-gamma
        if k in (10, 25, 50, nz): last = (k, g, S)
    print(f"T = {mp.nstr(T,8)}   (log 2 = {mp.nstr(mp.log(2),8)})")
    print(f"  sum_gamma |Fhat|^2  over {last[0]} zero pairs (gamma <= {mp.nstr(last[1],6)}) = {mp.nstr(S,10)}")
    print(f"  <F,h_e> = {mp.nstr(he,10)}   <F,h_o> = {mp.nstr(ho,10)}")
    print(f"  polar term 2(|<F,h_e>|^2 - |<F,h_o>|^2) = {mp.nstr(polar,10)}")
    print(f"  <A_T F,F> = sum - polar = {mp.nstr(S-polar,10)}\n")

for T in [mp.log(2), mp.mpf('0.35'), mp.mpf('0.20'), mp.mpf('0.10'), mp.mpf('0.05')]:
    report(T, 60)
