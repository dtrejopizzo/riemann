
import sys, time, pickle
import cypari2
pari = cypari2.Pari()
pari.allocatemem(2<<30)
pari.default("realprecision", 50)
T = int(sys.argv[1])
out = sys.argv[2]
t0 = time.time()
pari("mf=mfinit([1,12],1); F=mfeigenbasis(mf)[1]; L=lfunmf(mf,F);")
print(f"setup time {time.time()-t0:.1f}s", flush=True)
t0 = time.time()
res = pari(f"lfunzeros(L, {T})")
print(f"lfunzeros T={T}: {time.time()-t0:.1f}s, count={len(res)}", flush=True)
zeros_str = [str(r) for r in res]
with open(out, 'wb') as f: pickle.dump(zeros_str, f)
print("saved", flush=True)
