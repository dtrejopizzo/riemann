
import os, sys, time, pickle
import cypari2 def worker(args): tmin, tmax, dps, idx = args pari = cypari2.Pari() pari.default("realprecision", dps) pari("L = lfunmf(mfinit([1,12],1), mfeigenbasis(mfinit([1,12],1))[1])") t0 = time.time() z = pari.lfunzeros(pari("L"), [tmin, tmax]) elapsed = time.time() - t0 n = len(z) out = [str(z[i]) for i in range(n)] return idx, tmin, tmax, elapsed, out
