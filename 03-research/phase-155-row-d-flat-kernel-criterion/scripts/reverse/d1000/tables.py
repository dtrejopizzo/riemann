"""tables.py -- render the R155_011 tables from d_*.json, chk_*.json, insight.json."""
import json, glob, numpy as np
print("== §3 results ==")
for f in sorted(glob.glob("d_*.json")):
    d = json.load(open(f)); n = d["name"]
    try: c = json.load(open(f"chk_{n}.json"))
    except Exception: c = None
    print(f"{n:12s} T={d['T']:.4f} tmax={d['taumax']:6.2f} b={'Y' if d.get('BETA') else 'N'} "
          f"NZ={d['nzeros']:5d} LP={d['c_lp']:+.4e} grid={d['f_fine_min']:+.4e} "
          f"cert={d['certified']:+.4e} " +
          (f"prime={c['min_f_prime_fine']:+.4e} certP={c['certified_prime_side']:+.4e} "
           f"|z-p|={max(v['max_abs_diff'] for v in c['ladder'].values()):.2e} "
           f"far={c['min_f_prime_far']:+.3e}@{c['argmin_far']:.2f} "
           f"E={c['E_total']:.2f} log10tenv={c['log10_tau_env_honest']:.1f}" if c else "no check") +
          f" M={d['M']} h={d['h']:.4f} |w|inf={d['winf']:.2f} int|w|={d['int_abs_w']:.3f} l1x={d['l1_x']:.1f}")
print("\n== §4 residual ladder ==")
for f in sorted(glob.glob("chk_*.json")):
    c = json.load(open(f))
    print(f"{c['name']:12s} " + "  ".join(
        f"N={k}(G={v['Gamma']:.1f}): |zero-prime|={v['max_abs_diff']:.3e}, min_fz={v['min_f_zero']:+.4e}"
        for k, v in c["ladder"].items()))
try:
    ins = json.load(open("insight.json"))
except Exception:
    raise SystemExit
print("\n== §5 insight ==")
for n, r in ins.items():
    fl = r["first_neg_lobe"]
    print(f"\n-- {n} T={r['T']:.4f} taumax={r['taumax']:.2f} fmin={r['fmin_fine']:+.4e} "
          f"contacts={r['n_contacts']} what(0)={r['what0']:.4f} neg_lobes={r['n_neg_lobes']}")
    if fl: print(f"   first negative lobe of what: t={fl['t']:.4f} depth={fl['val']:+.4f} "
                 f"(mean gap ~ {r['mean_gap_at_50']:.2f} at g=50, {r['mean_gap_at_1400']:.2f} at g=1400)")
    print("   lobes t/val:", ", ".join(f"{l['t']:.3f}/{l['val']:+.3f}" for l in r["kernel_lobes"][:8]))
    for c in r["contacts"][:6]:
        fr = c["frac_in_gap"]
        print(f"   tau={c['tau']:8.4f} f={c['f']:+.4e} gap=({c['gap_lo']:.3f},{c['gap_hi']:.3f}) "
              f"frac={fr if fr is None else round(fr,3)} top5share={c['top_share']:.3f} "
              f"top=" + ";".join(f"g{g:.2f}:{v:+.3f}" for g, v in c["top_terms"][:3]))
    print("   near log p:", {k: (round(v['log_p'],3), round(v['w_at_logp'],3), round(v['local_absmass_frac'],4))
                             for k, v in r["near_logp"].items()})
