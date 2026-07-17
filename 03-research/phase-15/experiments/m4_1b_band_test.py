import mpmath as mp
mp.mp.dps = 30
logpi = mp.log(mp.pi)
Psi = lambda r: mp.re(mp.digamma(mp.mpf('0.25')+1j*mp.mpf(r)/2)) - logpi

# Primitive test vector: fhat(r) = (r^2 + 1/4) e^{-r^2/(2 sigma^2)}
# Then fhat(i/2) = ((i/2)^2 + 1/4) e^... = 0  => orthogonal to BOTH poles (s=0,1) => PRIMITIVE.
# For such f the M2 pole/ample term 2|fhat(i/2)|^2 = 0 identically.
def A_inf(sigma):
    fhat = lambda r: (r**2 + mp.mpf('0.25'))*mp.e**(-r**2/(2*sigma**2))
    integrand = lambda r: fhat(r)**2 * Psi(r)
    return (1/(2*mp.pi))*mp.quad(integrand, [-mp.inf,-20,-6.29,0,6.29,20,mp.inf])

def norm2(sigma):
    fhat = lambda r: (r**2 + mp.mpf('0.25'))*mp.e**(-r**2/(2*sigma**2))
    return (1/(2*mp.pi))*mp.quad(lambda r: fhat(r)**2, [-mp.inf,0,mp.inf])

print("Primitive vector fhat(r)=(r^2+1/4) e^{-r^2/2sigma^2}  (pole/ample term M2 = 0 exactly)")
print(f"{'sigma':>7} {'A_inf(f,f)':>22} {'||f||^2':>18} {'A_inf/||f||^2':>18}")
for s in ['0.5','1','1.5','2','3','4','6','8','12']:
    sig=mp.mpf(s)
    a=A_inf(sig); n=norm2(sig)
    print(f"{s:>7} {mp.nstr(a,12):>22} {mp.nstr(n,10):>18} {mp.nstr(a/n,10):>18}")

print("\nInterpretation:")
print("  if A_inf<0 for primitive f  => archimedean form is INDEFINITE on the primitive part,")
print("  and the M2 pole/ample cone (which vanishes on primitives) does NOT absorb the band.")
