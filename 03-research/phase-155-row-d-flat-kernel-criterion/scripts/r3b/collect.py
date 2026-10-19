import glob, json, math
rows=[]
for f in glob.glob('r3b_enclosure_*.json'):
    d=json.load(open(f))
    b=abs(d['b0'][1])+abs(d['b1'][1])
    rows.append(dict(T=d['T_name'],M=d['M'],tau0=d['tau0'],P=2*math.pi*d['M']/(2*d['T']),
        ceil_double=d['ceil_double'],a_lo=d['a'][0],a_hi=d['a'][1],b1norm=b,B=d['B'],
        beta_allow=b*d['B'],err_sigma=d['err_sigma'],err_g0=d['err_g0'],err_g1=d['err_g1'],
        bound=d['ceiling_upper_bound'],closed=d['ceiling_upper_bound']<0,
        rel_err=abs(d['err_sigma']/d['a'][1]),sec=d['sec_total'],N=d['N_panels'],p=d['p'],H=d['H']))
rows.sort(key=lambda r:(r['T'],r['M']))
json.dump(rows,open('r3b_summary.json','w'),indent=1)
for r in rows: r['B_tol']=abs(r['a_hi'])/r['b1norm'] if r['b1norm']>0 else float('inf')
json.dump(rows,open('r3b_summary.json','w'),indent=1)
print(r"| `T` | `M` | `tau0` | `Ceil` (double, DIAGNOSTIC) | `a` (upper end) | `\|b\|₁` | `B·\|b\|₁` | quad. err on `a` | **bound** | err/`\|a\|` | `B` tolerance | s |")
print('|'+'---:|'*12)
for r in rows:
    print("| %s | %d | %.3f | %+.4e | %+.6e | %.1e | %.1e | %.1e | **%+.6e** | %.1f%% | %.1e | %.0f |"%(
      r['T'],r['M'],r['tau0'],r['ceil_double'],r['a_hi'],r['b1norm'],r['beta_allow'],r['err_sigma'],
      r['bound'],100*r['rel_err'],r['B_tol'],r['sec']))
print()
print('not closed:',[(r['T'],r['M']) for r in rows if not r['closed']])
