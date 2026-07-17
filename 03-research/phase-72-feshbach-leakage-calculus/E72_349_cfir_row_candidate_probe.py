#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import build  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402


def setup_full(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    mu = vals[0]
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2
    xi = xi / norm(xi)
    d = 2 * np.pi * idx / L
    e = h_actual - mu * np.eye(len(idx))
    return idx, L, d, mu, xi, e


def k_row(z, L, d):
    return (1.0 - np.exp(z * L)) / (1j * z - d)


def k_kernel(z, w, L):
    if abs(w * w - z * z) < 1e-9:
        # Simple self-pair removable value for the row acting on G(w).
        return L + np.sinh(z * L) / z
    return (
        w * (1 + np.exp(z * L)) * (1 - np.exp(-w * L))
        + z * (1 - np.exp(z * L)) * (1 + np.exp(-w * L))
    ) / (w * w - z * z)


def e_lam(lam, L):
    if abs(lam) < 1e-10:
        return L + 0.5 * lam * L * L
    return (np.exp(lam * L) - 1.0) / lam


def p_infty(z, n_d, a, L):
    return 1j / (z + 1j * n_d) * (
        np.exp(z * L) * (e_lam(a - z, L) + e_lam(-a - z, L))
        - (e_lam(a + 1j * n_d, L) + e_lam(-a + 1j * n_d, L))
        + np.exp(z * L) * (e_lam(a - 1j * n_d, L) + e_lam(-a - 1j * n_d, L))
        - (e_lam(a + z, L) + e_lam(-a + z, L))
    )


def phi(a, dval):
    return dval / (a * a + dval * dval)


def phi_prime(a, dval):
    return (a * a - dval * dval) / (a * a + dval * dval) ** 2


def pair_cell(a, m_idx, n_idx, d_m, d_n, L):
    factor = 2.0 - np.exp(a * L) - np.exp(-a * L)
    if m_idx == n_idx:
        return factor * (-(2.0 / L) * phi_prime(a, d_n))
    return factor * (phi(a, d_m) - phi(a, d_n)) / (np.pi * (n_idx - m_idx))


def p_active(z, n_pos, a, idx, d, L):
    n_idx = idx[n_pos]
    n_d = d[n_pos]
    total = 0.0 + 0.0j
    for m_pos, m_idx in enumerate(idx):
        a_m = (1.0 - np.exp(z * L)) / (1j * z - d[m_pos])
        total += a_m * pair_cell(a, m_idx, n_idx, d[m_pos], n_d, L)
    return total


def tail_basis_row(z, window_nodes, idx, d, L):
    row = np.zeros(len(d), dtype=complex)
    for n_pos, n_d in enumerate(d):
        val = 0.0 + 0.0j
        for a in window_nodes:
            val += p_infty(z, n_d, a, L) - p_active(z, n_pos, a, idx, d, L)
        row[n_pos] = val
    return row


def rowspace_distance(row, e, xi):
    # For Hermitian rank n-1 E with normalized null vector xi, distance from
    # row to Row(E) is the null component row xi.
    amp = row @ xi
    return abs(amp), amp


def replace_det_scale(row, e):
    vals = []
    for i in range(e.shape[0]):
        m = e.copy().astype(complex)
        m[i, :] = row
        vals.append(abs(np.linalg.det(m)))
    return max(vals)


def candidate_rows(idx, L, d, xi, mu, roots, mode, node_kind):
    rows = []
    labels = []
    # Use critical-line shifted representatives w=i*tau from finite Cauchy roots.
    if node_kind == "root":
        nodes = [1j * t for t in roots]
    elif node_kind == "shift":
        nodes = [0.5 + 1j * t for t in roots]
    else:
        raise ValueError(node_kind)
    for a in nodes:
        base = mu * k_row(a, L, d)
        if mode == "base":
            row = base
        elif mode == "self":
            row = (mu - k_kernel(a, a, L)) * k_row(a, L, d)
        elif mode == "window":
            row = mu * k_row(a, L, d)
            for w in nodes:
                row -= k_kernel(a, w, L) * k_row(w, L, d)
        elif mode == "tail":
            row = tail_basis_row(a, nodes, idx, d, L)
        elif mode == "window_tail":
            row = mu * k_row(a, L, d)
            for w in nodes:
                row -= k_kernel(a, w, L) * k_row(w, L, d)
            row += tail_basis_row(a, nodes, idx, d, L)
        elif mode == "window_minus_tail":
            row = mu * k_row(a, L, d)
            for w in nodes:
                row -= k_kernel(a, w, L) * k_row(w, L, d)
            row -= tail_basis_row(a, nodes, idx, d, L)
        else:
            raise ValueError(mode)
        rows.append(row)
        labels.append(a)
    return labels, rows


def rowspace_invariance_rows(idx, L, d, xi, mu, e, roots, node_kind):
    """Add explicit rowspace rows to a defective candidate.

    If E xi=0, then adding alpha E to any candidate row cannot change the
    row-ideal defect row xi.  This mode checks that the numerical detector
    sees the same null component before and after the rowspace addition.
    """
    labels, rows = candidate_rows(idx, L, d, xi, mu, roots, "window_tail", node_kind)
    out = []
    for a, row in zip(labels, rows):
        k = k_row(a, L, d)
        rowspace_row = k @ e
        out.append((a, row, row + rowspace_row, rowspace_row))
    return out


def fitted_lambda_rows(idx, L, d, xi, roots, node_kind):
    if node_kind == "root":
        nodes = [1j * t for t in roots]
    elif node_kind == "shift":
        nodes = [0.5 + 1j * t for t in roots]
    else:
        raise ValueError(node_kind)
    if not nodes:
        return [], [], 0.0
    kxis = []
    rhs = []
    static_rows = []
    for a in nodes:
        k = k_row(a, L, d)
        static = np.zeros(len(d), dtype=complex)
        for w in nodes:
            static -= k_kernel(a, w, L) * k_row(w, L, d)
        static += tail_basis_row(a, nodes, idx, d, L)
        kxis.append(k @ xi)
        rhs.append(-(static @ xi))
        static_rows.append(static)
    kxis = np.array(kxis)
    rhs = np.array(rhs)
    denom = np.vdot(kxis, kxis)
    lam_fit = 0.0 if abs(denom) < 1e-300 else np.vdot(kxis, rhs) / denom
    rows = [lam_fit * k_row(a, L, d) + static for a, static in zip(nodes, static_rows)]
    return nodes, rows, lam_fit


def lambda_consistency(idx, L, d, xi, roots, node_kind):
    if node_kind == "root":
        nodes = [1j * t for t in roots]
    elif node_kind == "shift":
        nodes = [0.5 + 1j * t for t in roots]
    else:
        raise ValueError(node_kind)
    vals = []
    for a in nodes:
        k = k_row(a, L, d)
        static = np.zeros(len(d), dtype=complex)
        for w in nodes:
            static -= k_kernel(a, w, L) * k_row(w, L, d)
        static += tail_basis_row(a, nodes, idx, d, L)
        den = k @ xi
        if abs(den) > 1e-14:
            vals.append(-(static @ xi) / den)
    if not vals:
        return np.nan, np.nan, np.nan
    vals = np.array(vals)
    mean = np.mean(vals)
    spread = np.max(np.abs(vals - mean))
    rel = spread / max(abs(mean), 1e-300)
    return mean, spread, rel


def run():
    print("E72.349 CFIR row-candidate probe")
    print(
        " lam   N roots node       mode      maxNullAmp    maxRelNull    rmsRelNull"
    )
    for lam, n_modes in [(6, 10), (8, 12), (10, 14), (12, 16)]:
        idx, L, d, mu, xi, e = setup_full(lam, n_modes)
        roots = finite_roots(xi.real, d, hmax=8.0)[:3]
        for node_kind in ["root", "shift"]:
            for mode in [
                "base",
                "self",
                "window",
                "tail",
                "window_tail",
                "window_minus_tail",
            ]:
                _, rows = candidate_rows(idx, L, d, xi, mu, roots, mode, node_kind)
                if not rows:
                    continue
                amps = []
                rels = []
                for row in rows:
                    dist, amp = rowspace_distance(row, e, xi)
                    amps.append(dist)
                    rels.append(dist / max(norm(row), 1e-300))
                print(
                    f"{lam:5.1f} {n_modes:3d} {len(rows):5d} {node_kind:>5s} "
                    f"{mode:>8s} {max(amps):13.5e} "
                    f"{max(rels):13.5e} {np.sqrt(np.mean(np.square(rels))):13.5e}"
                )
            _, rows, lam_fit = fitted_lambda_rows(idx, L, d, xi, roots, node_kind)
            if rows:
                amps = []
                rels = []
                for row in rows:
                    dist, _ = rowspace_distance(row, e, xi)
                    amps.append(dist)
                    rels.append(dist / max(norm(row), 1e-300))
                print(
                    f"{lam:5.1f} {n_modes:3d} {len(rows):5d} {node_kind:>5s} "
                    f"{'fitLam':>8s} {max(amps):13.5e} "
                    f"{max(rels):13.5e} {np.sqrt(np.mean(np.square(rels))):13.5e}"
                )
            mean_lam, spread_lam, rel_lam = lambda_consistency(
                idx, L, d, xi, roots, node_kind
            )
            if np.isfinite(rel_lam):
                print(
                    f"{lam:5.1f} {n_modes:3d} {len(rows):5d} {node_kind:>5s} "
                    f"{'lamSpread':>8s} {abs(mean_lam):13.5e} "
                    f"{spread_lam:13.5e} {rel_lam:13.5e}"
                )
        print(" rowspace-invariance check on window_tail")
        print(
            " lam   N roots node   maxBaseRel   maxAddedRel   maxDeltaAmp   maxRowspaceAmp"
        )
        for node_kind in ["root", "shift"]:
            triples = rowspace_invariance_rows(idx, L, d, xi, mu, e, roots, node_kind)
            if not triples:
                continue
            base_rels = []
            added_rels = []
            delta_amps = []
            rowspace_amps = []
            for _, base, added, rowspace_row in triples:
                _, base_amp = rowspace_distance(base, e, xi)
                _, added_amp = rowspace_distance(added, e, xi)
                _, rowspace_amp = rowspace_distance(rowspace_row, e, xi)
                base_rels.append(abs(base_amp) / max(norm(base), 1e-300))
                added_rels.append(abs(added_amp) / max(norm(added), 1e-300))
                delta_amps.append(abs(added_amp - base_amp))
                rowspace_amps.append(abs(rowspace_amp))
            print(
                f"{lam:5.1f} {n_modes:3d} {len(triples):5d} {node_kind:>5s} "
                f"{max(base_rels):12.5e} {max(added_rels):12.5e} "
                f"{max(delta_amps):12.5e} {max(rowspace_amps):14.5e}"
            )


if __name__ == "__main__":
    run()
