import json, glob, numpy as np
rows=[]
order=["log3h","058","058_M16","062","065","log2","075","080"]
for n in order:
    try: r=json.load(open(f"win_{n}.json"))
    except: continue
    for L,d in r["L"].items():
        if "c" not in d: continue
        rows.append((n,r["T"],r["M"],r["h"],r["J"],r["U"],r["taumax"],float(L),
                     d["c"],d["l1x"],d["tail_mass"],d["tail_absmass"],
                     d["tail_centroid"],d["sign_changes_x"],d["last_sig_node"],
                     d["ncontacts"],d["argmin"]))
print(f"{'win':9s}{'T':>7s}{'M':>3s}{'h':>7s}{'U':>7s}{'taumax':>8s}{'L':>7s}{'c':>12s}{'l1x':>9s}{'mass':>9s}{'|mass|':>9s}{'cen':>6s}{'sgnchg':>7s}{'vlast':>7s}{'ncon':>5s}{'argmin':>8s}")
for r in rows:
    print(f"{r[0]:9s}{r[1]:7.4f}{r[2]:3d}{r[3]:7.4f}{r[5]:7.2f}{r[6]:8.2f}{r[7]:7.0f}{r[8]:12.4e}{r[9]:9.2f}{r[10]:9.3f}{r[11]:9.3f}{r[12]:6.2f}{r[13]:7d}{r[14]:7.2f}{r[15]:5d}{r[16]:8.2f}")
# contact positions at the largest L per window
print("\ncontacts (first 24) at L=100:")
for n in order:
    try: r=json.load(open(f"win_{n}.json"))
    except: continue
    d=r["L"].get("100.0")
    if d and "contacts" in d:
        print(f"{n:9s} {' '.join('%.2f'%t for t in d['contacts'][:24])}")
