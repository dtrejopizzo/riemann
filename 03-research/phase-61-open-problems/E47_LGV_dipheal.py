"""
F (continuacion): rastrear e_k(t) = e_k(D - t Q) finamente para ZETA.
Hallazgo de E46: en t=1 todos e_k>=0 (A>=0) PERO e_5 cruza negativo en t~0.15.
=> el 'gas' tiene CANCELACION: e_k(t) baja a negativo en acoplamiento intermedio
   y SANA a positivo en t=1. No hay expansion cancelacion-libre (positiva termino a termino).
Esto es la sombra (en funciones simetricas) de la escalera kappa: positividad COLECTIVA.
Documentamos: para cada k, min_t e_k(t) y si recupera en t=1.
"""
import mpmath as mp
mp.mp.dps = 30
exec(open('E46_LGV_polymer.py').read().split('def report')[0])  # reusa helpers

def trace(lam,N,kind):
    D,Q,L=DandQ(lam,N,kind); n=D.rows
    print(f"\n=== {kind} lambda={lam} N={N} dim={n} ===")
    ts=[mp.mpf(i)/40 for i in range(41)]
    print("   k | min_t e_k |  t_min | e_k(t=1) | recupera?")
    anydip=False
    for k in range(1,n+1):
        vals=[(t,ek_from_eigs(D-t*Q)[k]) for t in ts]
        tmin,emin=min(vals,key=lambda tv:tv[1])
        e1=vals[-1][1]
        dip = emin<-mp.mpf('1e-9')
        rec = dip and e1>=-mp.mpf('1e-9')
        if dip: anydip=True
        if dip or k<=6:
            print(f"  {k:2d} | {mp.nstr(emin,3):>10} | {mp.nstr(tmin,3):>5} | {mp.nstr(e1,3):>9} | {'SI (dip&heal)' if rec else ('NO baja' if not dip else 'queda<0')}")
    print(f"  => {'HAY dip&heal (cancelacion real, no LGV-positivo)' if anydip else 'monotono positivo (LGV-positivo posible)'}")

trace('7.0',10,'zeta')
