#!/usr/bin/env python3
"""
S_pm-dimension of the norm-bounded modules ||H Z^r||_n  of Connes-Consani.

Definition (CC, arXiv:2205.01391, sec.3):
  I = ||H Z^r||_n (1_+) = { v in Z^r : |v|_1 <= n }
  F subset I  *linearly generates*  iff for every m in I there are
  alpha(f) in {-1,0,+1} with
        m = sum alpha(f) f        and       sum |alpha(f) f|_1 <= n.
  dim_{S_pm} := min |F|.

r = 1  is the published case: CC prove  dim = ceil( log(2n+1) / log 3 ).
r = 2  is the surface analogue.  Not in the literature.

Nothing here uses zeros of zeta, Li coefficients, or any Weil form.
"""
import itertools, math, sys, random
from functools import lru_cache


def ball(n, r):
    """ell^1 ball of radius n in Z^r, as a list of tuples (any rank)."""
    out = []
    def rec(prefix, rem, left):
        if left == 0:
            out.append(tuple(prefix)); return
        for c in range(-rem, rem + 1):
            rec(prefix + [c], rem - abs(c), left - 1)
    rec([], n, r)
    return out


def l1(v):
    return sum(abs(c) for c in v)


def reach(F, n):
    """All sums sum alpha_f f, alpha in {0,+-1}, with mass sum|alpha_f f|_1 <= n."""
    r = len(F[0]) if F else 1
    zero = tuple([0] * r)
    cur = {zero: 0}          # vector -> minimal mass achieving it
    for f in F:
        m = l1(f)
        nxt = dict(cur)
        for v, mass in cur.items():
            if mass + m > n:
                continue
            for s in (1, -1):
                w = tuple(v[i] + s * f[i] for i in range(r))
                nm = mass + m
                if nxt.get(w, n + 1) > nm:
                    nxt[w] = nm
        cur = nxt
    return set(cur)


def candidates(n, r):
    """One representative per +-pair (F and -F have the same reach)."""
    out = []
    for v in ball(n, r):
        if all(c == 0 for c in v):
            continue
        # keep v if first nonzero coordinate is positive
        for c in v:
            if c != 0:
                if c > 0:
                    out.append(v)
                break
    return out


def exact_dim(n, r, cap_k=8, budget=None):
    """Exhaustive minimum generating set.  Returns (dim, witness) or (None, None)."""
    B = set(ball(n, r))
    C = candidates(n, r)
    lb = math.ceil(math.log(len(B)) / math.log(3) - 1e-12)
    tried = 0
    for k in range(max(1, lb), cap_k + 1):
        for F in itertools.combinations(C, k):
            tried += 1
            if budget and tried > budget:
                return None, None
            if 3 ** k < len(B):
                break
            if reach(list(F), n) == B:
                return k, F
    return None, None


def greedy_dim(n, r, trials=4000, seed=0):
    """Randomised upper bound: repeatedly grow a set that maximises new coverage."""
    rng = random.Random(seed)
    B = set(ball(n, r))
    C = candidates(n, r)
    best = None
    for _ in range(trials):
        F = []
        cur = reach(F, n)
        while cur != B:
            pool = rng.sample(C, min(len(C), 14))
            gain = []
            for c in pool:
                if c in F:
                    continue
                g = len(reach(F + [c], n))
                gain.append((g, c))
            if not gain:
                break
            gain.sort(key=lambda t: (-t[0], t[1]))
            top = [c for g, c in gain if g == gain[0][0]]
            F.append(rng.choice(top))
            cur = reach(F, n)
            if best is not None and len(F) >= best[0]:
                break
        if cur == B and (best is None or len(F) < best[0]):
            best = (len(F), tuple(F))
    return best


if __name__ == "__main__":
    print("=" * 74)
    print("RANK 1  --  verification against Connes-Consani arXiv:2205.01391")
    print("           claim:  dim_{S_pm}(||HZ||_n) = ceil( log(2n+1)/log 3 )")
    print("=" * 74)
    print(f"{'n':>4} {'|I_n|':>7} {'computed':>9} {'CC formula':>11}  {'':>3} witness")
    ok = True
    for n in range(1, 41):
        d, F = exact_dim(n, 1, cap_k=6)
        cc = math.ceil(math.log(2 * n + 1) / math.log(3) - 1e-12)
        mark = "OK " if d == cc else "*** MISMATCH"
        if d != cc:
            ok = False
        w = "" if n > 30 else str([f[0] for f in F])
        print(f"{n:>4} {2*n+1:>7} {d:>9} {cc:>11}  {mark:>3} {w}")
    print()
    print("RANK 1 VERDICT:", "formula reproduced for n=1..40" if ok else "MISMATCH")
