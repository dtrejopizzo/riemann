"""Algebra diagnostics for R170_809, not continuous/arithmetic certificates."""
import json
from fractions import Fraction as F
import numpy as np


def diagnostic(seed):
    rng = np.random.default_rng(seed)
    n, m = 12, 4
    raw = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    b = raw.conj().T @ raw + 4 * np.eye(n)
    raw = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    k = (raw + raw.conj().T) / 10
    w = b - k
    p = np.eye(n)[:, :m]
    q = np.eye(n)[:, m:]
    inverse_columns = np.linalg.solve(b, p)
    d = p.T @ inverse_columns
    v = inverse_columns @ np.linalg.inv(d)
    c = np.linalg.inv(d) - v.conj().T @ k @ v
    a = q.T @ k @ v
    block = q.T @ w @ q
    gap = float(np.linalg.eigvalsh(block)[0]) / 2
    exact = c - a.conj().T @ np.linalg.solve(block, a)
    lower = c - a.conj().T @ a / gap
    # Independently minimize the original W with Pf=x, without using V.
    direct_cross = q.T @ w @ p
    direct = p.T @ w @ p - direct_cross.conj().T @ np.linalg.solve(block, direct_cross)
    error = float(np.linalg.norm(exact - direct))
    difference_min = float(np.linalg.eigvalsh(exact - lower)[0])
    x = rng.normal(size=m) + 1j * rng.normal(size=m)
    y = rng.normal(size=n-m) + 1j * rng.normal(size=n-m)
    f = v @ x + q @ y
    lhs = np.vdot(f, w @ f).real
    rhs = np.vdot(x, lower @ x).real + gap * np.linalg.norm(y - a @ x / gap)**2
    omitted = np.vdot(y, (block - gap * np.eye(n-m)) @ y).real
    identity_error = float(abs(lhs - rhs - omitted))
    assert error < 1e-10
    assert difference_min > -1e-10
    assert identity_error < 1e-9
    return dict(seed=seed, schur_error=error, completion_error=identity_error,
                debit_difference_minimum_eigenvalue=difference_min)


if __name__ == '__main__':
    # Exact contact W=[[1/2,-1],[-1,2]], with b=diag(1,3).
    c, a, block, gap = F(1, 2), F(1), F(2), F(1)
    assert c - a*a/block == 0
    assert c - a*a/gap == -F(1, 2)
    print(json.dumps(dict(diagnostics=[diagnostic(s) for s in [17, 39, 83]],
                         exact_contact_schur=str(c-a*a/block),
                         sufficient_bound_at_contact=str(c-a*a/gap),
                         certification=False), indent=2))
