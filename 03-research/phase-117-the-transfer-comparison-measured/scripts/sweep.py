import math, csv, numpy as np, rowd_assembly as RA, measure_cN as MC
rows=[]
PP=RA.prime_powers_upto(40)
print(f"{'N':>4} {'ref':>4} {'nc':>3} {'src':>8} {'rho_N':>8} {'rho*lnN':>8} {'lam':>9} {'c_right':>8} {'c_sym':>8} {'c_anti':>8}")
for N in PP:
    for refine in (4,6,8):
        try:
            r=MC.measure(N,refine=refine)
        except Exception as e:
            print(f"{N:>4} {refine:>4}  FAIL {type(e).__name__}"); continue
        rows.append(r)
        print(f"{r['N']:>4} {r['refine']:>4} {r['nc']:>3} {r['src']:>8.4f} {r['rho']:>8.5f} "
              f"{r['rho']*math.log(N):>8.5f} {r['lam']:>9.5f} {r['c_right']:>8.4f} {r['c_sym']:>8.4f} {r['c_anti']:>8.4f}")
    print()
with open('cN_results.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("wrote cN_results.csv")
