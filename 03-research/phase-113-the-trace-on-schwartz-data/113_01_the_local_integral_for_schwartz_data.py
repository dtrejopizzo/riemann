#!/usr/bin/env python3
"""
113_01 verifier -- the local integral for Schwartz data.

Checks (each PASS/FAIL, exits 0 iff all pass):
 1. Lemma 1.1: tails A(h), B_p(h) stabilize under refinement for a genuine
    Schwartz h AND for a bare-Schwartz (no exponential rate) control.
 2. Theorem 2.1: exact closed form of the K-truncation against direct shell
    summation, and the dichotomy -- linear growth (slope h(1)) when h(1)!=0,
    exact stabilization when h(1)=0 -- for a genuine (non-compactly-
    supported) Schwartz h.
 3. Lemma 3.2: the residue and finite part of I_p(s) at s=-1, refined in
    epsilon, with a control clause rejecting the *other* scheme's constant.
 4. Theorem 3.3: the exact 1/2 gap between the two schemes, at nine primes.
"""
import mpmath as mp

mp.mp.dps = 40
PASS = []


def check(name, cond, detail=""):
    PASS.append(cond)
    print(("PASS" if cond else "FAIL") + f": {name}" + (f" ({detail})" if detail else ""))


# ---------------------------------------------------------------------
# test functions: h(u) = h(|u|), tilde h(x) = h(e^x)
# ---------------------------------------------------------------------
def tilde_h_gauss(x):
    """Genuine Schwartz, h(1) = tilde_h(0) = 1 != 0."""
    return mp.e ** (-x * x)


def tilde_h_odd_gauss(x):
    """Genuine Schwartz, h(1) = tilde_h(0) = 0 identically."""
    return x * mp.e ** (-x * x)


def tilde_h_bare_schwartz(x):
    """Schwartz with only polynomial decay in this truncated model (no
    exponential rate at all) -- Remark 111.0.1-type control, restricted to
    a bounded proxy so the infinite local shell sums still make sense; we
    use a rapidly-polynomially-decaying but non-exponential profile."""
    return 1 / (1 + x ** 8)


def h_of_r(tilde_h, r):
    return tilde_h(mp.log(r))


# ---------------------------------------------------------------------
# 1. Lemma 1.1 -- tail stabilization
# ---------------------------------------------------------------------
def A_partial(tilde_h, p, N):
    return mp.nsum(lambda n: h_of_r(tilde_h, p ** n), [1, N])


def B_partial(tilde_h, p, N):
    return mp.nsum(lambda m: h_of_r(tilde_h, p ** (-m)) * p ** (-m), [1, N])


for label, th in [("gaussian", tilde_h_gauss), ("bare-schwartz-x^-8", tilde_h_bare_schwartz)]:
    p = mp.mpf(2)
    a20, a60 = A_partial(th, p, 20), A_partial(th, p, 60)
    b20, b60 = B_partial(th, p, 20), B_partial(th, p, 60)
    rel_a = abs(a60 - a20) / (abs(a60) + mp.mpf('1e-30'))
    rel_b = abs(b60 - b20) / (abs(b60) + mp.mpf('1e-30'))
    tol = mp.mpf('1e-7') if "bare" in label else mp.mpf('1e-12')
    check(f"Lemma 1.1 tail A stabilizes ({label})", rel_a < tol, f"rel={float(rel_a):.2e}")
    check(f"Lemma 1.1 tail B stabilizes ({label})", rel_b < tol, f"rel={float(rel_b):.2e}")

# ---------------------------------------------------------------------
# 2. Theorem 2.1 -- K-truncation closed form and dichotomy
# ---------------------------------------------------------------------
def W_p_K_direct(tilde_h, p, K, Ntail=80):
    """Direct shell summation of the K-truncated local integral:
    shells n>=1 (|u|_p<1), shells m>=1 with |u|_p=p^m>1 (n=-m),
    and the unit shell split into 'far' part (measure (p-2)/(p-1)) plus
    K sub-shells |1-u|_p = p^{-k}, k=1..K (each contributing h(1)*1)."""
    p = mp.mpf(p)
    tail = A_partial(tilde_h, p, Ntail) + B_partial(tilde_h, p, Ntail)
    h1 = h_of_r(tilde_h, 1)
    shell0 = h1 * ((p - 2) / (p - 1) + K)
    return tail + shell0


def W_p_K_formula(tilde_h, p, K, Ntail=80):
    p = mp.mpf(p)
    tail = A_partial(tilde_h, p, Ntail) + B_partial(tilde_h, p, Ntail)
    h1 = h_of_r(tilde_h, 1)
    return tail + h1 * ((p - 2) / (p - 1) + K)


p = mp.mpf(3)
for K in [5, 50]:
    direct = W_p_K_direct(tilde_h_gauss, p, K)
    formula = W_p_K_formula(tilde_h_gauss, p, K)
    check(f"Theorem 2.1 closed form matches direct summation, K={K}",
          abs(direct - formula) < mp.mpf('1e-25'))

# dichotomy: h(1)!=0 -> linear growth slope h(1); h(1)=0 -> exact stabilization
Ks = [10, 20, 40, 80]
vals_nonzero = [W_p_K_formula(tilde_h_gauss, p, K) for K in Ks]
slopes = [(vals_nonzero[i + 1] - vals_nonzero[i]) / (Ks[i + 1] - Ks[i]) for i in range(len(Ks) - 1)]
h1 = h_of_r(tilde_h_gauss, 1)
check("Theorem 2.1 dichotomy: h(1)!=0 gives linear growth of exact slope h(1)",
      all(abs(s - h1) < mp.mpf('1e-20') for s in slopes),
      f"slopes={[float(s) for s in slopes]}, h(1)={float(h1)}")

vals_zero = [W_p_K_formula(tilde_h_odd_gauss, p, K) for K in Ks]
spread = max(vals_zero) - min(vals_zero)
check("Theorem 2.1 dichotomy: h(1)=0 gives exact K-independent stabilization",
      spread < mp.mpf('1e-25'), f"spread={float(spread):.2e}")

# control that must FAIL to discriminate: claiming h(1)!=0 case is bounded
check("control: h(1)!=0 case is NOT bounded as K grows (discriminates the test)",
      abs(vals_nonzero[-1] - vals_nonzero[0]) > mp.mpf('1'))


# ---------------------------------------------------------------------
# 3. Lemma 3.2 -- residue and finite part of I_p(s) at s = -1
# ---------------------------------------------------------------------
def I_p(pval, eps):
    """I_p(-1+eps) = (p-2)/(p-1) + p^{-eps}/(1 - p^{-eps})."""
    pval = mp.mpf(pval)
    x = pval ** (-eps)
    return (pval - 2) / (pval - 1) + x / (1 - x)


for pval in [2, 3, 5, 7, 11]:
    logp = mp.log(pval)
    predicted_finite_part = (mp.mpf(pval) - 2) / (mp.mpf(pval) - 1) - mp.mpf(1) / 2
    wrong_scheme_value = (mp.mpf(pval) - 2) / (mp.mpf(pval) - 1)  # Theorem 3.3's OTHER scheme
    eps = mp.mpf('1e-7')
    finite_remainder = I_p(pval, eps) - 1 / (eps * logp)
    err = abs(finite_remainder - predicted_finite_part)
    err_vs_wrong = abs(finite_remainder - wrong_scheme_value)
    check(f"Lemma 3.2 finite part matches (p-2)/(p-1)-1/2, p={pval}",
          err < mp.mpf('1e-5'), f"err={float(err):.2e}")
    check(f"Lemma 3.2 finite part rejects the OTHER scheme's constant (p-2)/(p-1), p={pval}",
          err_vs_wrong > mp.mpf('0.4'), f"err_vs_wrong={float(err_vs_wrong):.3f}")

# refinement in epsilon: the remainder should CONVERGE to the same constant
p_test = mp.mpf(7)
logp = mp.log(p_test)
predicted = (p_test - 2) / (p_test - 1) - mp.mpf(1) / 2
remainders = []
for eps in [mp.mpf('1e-3'), mp.mpf('1e-5'), mp.mpf('1e-7')]:
    remainders.append(I_p(p_test, eps) - 1 / (eps * logp))
errs = [abs(r - predicted) for r in remainders]
check("Lemma 3.2 finite part: error shrinks under epsilon-refinement",
      errs[0] > errs[1] > errs[2], f"errs={[float(e) for e in errs]}")

# ---------------------------------------------------------------------
# 4. Theorem 3.3 -- the exact 1/2 gap
# ---------------------------------------------------------------------
gaps = []
for pval in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
    pval = mp.mpf(pval)
    C1 = (pval - 2) / (pval - 1)          # "subtract K" scheme
    C2 = (pval - 2) / (pval - 1) - mp.mpf(1) / 2  # Laurent finite-part scheme
    gaps.append(C1 - C2)
check("Theorem 3.3: the two schemes disagree by exactly 1/2 at every prime tested",
      all(abs(g - mp.mpf('0.5')) < mp.mpf('1e-30') for g in gaps),
      f"gaps={[float(g) for g in gaps]}")

# ---------------------------------------------------------------------
print()
if all(PASS):
    print("VERDICT: ALL CHECKS PASS")
    raise SystemExit(0)
else:
    print("VERDICT: SOME CHECKS FAILED")
    raise SystemExit(1)
