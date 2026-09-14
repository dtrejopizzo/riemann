#!/usr/bin/env python3
"""Targeted V260 scalar-gap gate at T=log(5)/2.

This is a binary64 composite-Gauss/FFT diagnostic, not an interval
certificate.  It tests the *complete* sufficient condition

    B_260 - delta^(-1) (Q_260 A X)^*(Q_260 A X) > 0,

where delta=0.218 is inherited from the certified Q_200 gap because
Q_260 is a subspace of Q_200.  The frame contains the certified V200
primitive Ritz basis plus sixty Tate-corrected Legendre directions.
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "base", HERE / "p3_log5_full_residual_diagnostic.py"
)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(base)

T = 0.5 * np.log(5.0)


def tate_moments(n_modes: int) -> np.ndarray:
    """High-precision centres for the two exact Tate moment rows."""
    mp.mp.dps = 100
    t_ball = mp.log(5) / 2
    k = t_ball / 2
    rows = np.empty((2, n_modes), dtype=float)
    for n in range(n_modes):
        value = mp.sqrt(2 * mp.pi / k) * mp.besseli(mp.mpf(2 * n + 1) / 2, k)
        value *= mp.sqrt(t_ball * mp.mpf(2 * n + 1) / 2)
        rows[0, n] = float(value)
        rows[1, n] = -rows[0, n] if n % 2 else rows[0, n]
    return rows


def build_nested_frame(n_modes: int) -> np.ndarray:
    old = np.load(os.environ.get("P3_LOG5_FRAME", "/tmp/p3_log5_ritz200.npz"))
    x0 = np.asarray(old["vectors"], dtype=float)
    if x0.shape == (n_modes, n_modes - 2):
        # A directed D.148 physical Ritz frame is already an orthonormal
        # chart of the full primitive V_N space.
        return x0
    assert x0.shape == (200, 198) and n_modes >= 200
    padded = np.vstack((x0, np.zeros((n_modes - 200, x0.shape[1]))))
    jets = tate_moments(n_modes)
    high = np.zeros((n_modes, n_modes - 200), dtype=float)
    head = jets[:, :2]
    for j, degree in enumerate(range(200, n_modes)):
        high[degree, j] = 1.0
        high[:2, j] = np.linalg.solve(head, -jets[:, degree])
    raw = np.column_stack((padded, high))
    assert np.linalg.norm(jets @ raw, 2) < 2e-12
    q, _ = np.linalg.qr(raw, mode="reduced")
    assert np.linalg.norm(jets @ q, 2) < 2e-11
    return q


def main() -> None:
    n_modes = int(os.environ.get("P3_LOG5_N", "260"))
    points = int(os.environ.get("P3_LOG5_POINTS", str(2**20)))
    box = float(os.environ.get("P3_LOG5_BOX", "32"))
    cells = int(os.environ.get("P3_LOG5_CELLS", "6000"))
    qorder = int(os.environ.get("P3_LOG5_QORDER", "6"))
    batch = int(os.environ.get("P3_LOG5_BATCH", "10"))
    delta = float(os.environ.get("P3_LOG5_DELTA", ".218"))
    save = Path(os.environ.get("P3_LOG5_SAVE", "/tmp/p3_log5_v260_scalar_gap.npz"))

    xframe = build_nested_frame(n_modes)
    width = xframe.shape[1]

    # Composite Gauss chart avoids the unresolved endpoint mass of a uniform
    # Legendre rectangle rule.  Prime-shift breakpoints are inserted as cell
    # edges, so every contact translate is polynomial on each open cell.
    breaks = {-T, T}
    for integer in (2, 3, 4):
        shift = np.log(float(integer))
        for point in (-T + shift, T - shift, -T - shift, T + shift):
            if -T < point < T:
                breaks.add(point)
    coarse = np.linspace(-T, T, cells + 1)
    edges = np.unique(np.concatenate((coarse, np.array(sorted(breaks)))))
    nodes, weights = leggauss(qorder)
    midpoint = (edges[:-1] + edges[1:]) / 2
    half = (edges[1:] - edges[:-1]) / 2
    tq = (midpoint[:, None] + half[:, None] * nodes).reshape(-1)
    wq = (half[:, None] * np.broadcast_to(weights, (len(half), qorder))).reshape(-1)
    source_q = base.synthesize(tq / T, xframe)
    acted_q = np.empty_like(source_q)
    moment_q = np.column_stack((np.exp(tq / 2), np.exp(-tq / 2)))
    moment_gram = moment_q.T @ (wq[:, None] * moment_q)

    dx = box / points
    grid = (np.arange(points) - points // 2) * dx
    inside = np.flatnonzero(np.abs(grid) <= T)
    frequency = 2 * np.pi * np.fft.rfftfreq(points, d=dx)
    psi_q = base.digamma_complex(np.array([0.25]))[0].real
    symbol = base.digamma_complex(0.25 + 0.5j * frequency).real - psi_q
    m0 = np.log(np.pi) - psi_q

    for start in range(0, width, batch):
        stop = min(start + batch, width)
        full = np.zeros((points, stop - start), dtype=float)
        full[inside] = base.synthesize(grid[inside] / T, xframe[:, start:stop])
        image = np.fft.irfft(
            np.fft.rfft(full, axis=0) * symbol[:, None], n=points, axis=0
        )
        image -= m0 * full
        for integer, mangoldt in ((2, np.log(2.0)), (3, np.log(3.0)),
                                  (4, np.log(2.0))):
            shift = np.log(float(integer))
            coefficient = mangoldt / np.sqrt(float(integer))
            image[inside] -= coefficient * (
                base.shifted(full, grid, grid[inside] + shift)
                + base.shifted(full, grid, grid[inside] - shift)
            )
        acted_q[:, start:stop] = base.shifted(image, grid, tq)
        print("acted", start, stop, flush=True)

    # A is used only as a form on the two-Tate primitive Hilbert space.
    # Remove the polar component before measuring Q_N A V_N; retaining it
    # would charge leakage into directions to which the .218 gap does not
    # apply and is therefore not the Feshbach residual.
    acted_polar = np.linalg.solve(
        moment_gram, moment_q.T @ (wq[:, None] * acted_q)
    )
    acted_q -= moment_q @ acted_polar

    sw = np.sqrt(wq)[:, None]
    sq = sw * source_q
    aq = sw * acted_q
    gram = sq.T @ sq
    finite = sq.T @ aq
    action2 = aq.T @ aq
    gram = (gram + gram.T) / 2
    finite = (finite + finite.T) / 2
    action2 = (action2 + action2.T) / 2
    finite_square = finite.T @ np.linalg.solve(gram, finite)
    residual_raw = (action2 - finite_square)
    residual_raw = (residual_raw + residual_raw.T) / 2
    he, hv = np.linalg.eigh(residual_raw)
    residual = (hv * np.maximum(he, 0.0)) @ hv.T
    residual = (residual + residual.T) / 2
    gate = finite - residual / delta
    gate = (gate + gate.T) / 2

    # Generalized eigenvalues relative to the measured L2 Gram give the
    # coordinate-independent sign of both finite compression and gate.
    gl, gu = np.linalg.eigh(gram)
    invroot = (gu * (1 / np.sqrt(gl))) @ gu.T
    finite_phys = invroot @ finite @ invroot
    gate_phys = invroot @ gate @ invroot
    finite_e = np.linalg.eigvalsh((finite_phys + finite_phys.T) / 2)
    gate_e = np.linalg.eigvalsh((gate_phys + gate_phys.T) / 2)

    # Correct three-block diagnostic with D=the inherited primitive V200
    # span and S=the sixty promoted boundary directions.
    split = 198
    b11 = finite[split:, split:]
    h11 = residual[split:, split:]
    se, su = np.linalg.eigh((b11 + b11.T) / 2)
    sroot = (su * (1 / np.sqrt(se))) @ su.T
    kappa_260 = np.linalg.eigvalsh(sroot @ h11 @ sroot)[-1]

    # Optional one-step Green enrichment.  Select precisely the safe Ritz
    # combinations whose scalar leakage is largest, adjoin their Q-residual
    # responses to V_N, and retest against the same inherited delta.  The
    # new orthogonal complement is a subspace of Q_N, so the .218 theorem
    # remains applicable without any new coercivity assumption.
    enrich = int(os.environ.get("P3_LOG5_ENRICH", "0"))
    enriched_report = None
    if enrich:
        directed = np.load(os.environ.get(
            "P3_LOG5_DIRECTED", "/tmp/p3_log5_ritz260_directed.npz"
        ))
        exact_values = np.asarray(directed["values"], dtype=float)
        assert exact_values.shape == (width,)
        safe_start = int(os.environ.get("P3_LOG5_SAFE_START", "5"))
        safe_values = exact_values[safe_start:]
        inv_safe = np.diag(1 / np.sqrt(safe_values))
        leakage_safe = inv_safe @ residual[safe_start:, safe_start:] @ inv_safe
        leak_e, leak_u = np.linalg.eigh((leakage_safe + leakage_safe.T) / 2)
        take = min(enrich, len(leak_e))
        selected = leak_u[:, -take:] * (1 / np.sqrt(safe_values))[:, None]
        combinations = np.zeros((width, take))
        combinations[safe_start:, :] = selected

        def act_coefficients(coefficients: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
            polynomials = xframe @ coefficients
            full = np.zeros((points, coefficients.shape[1]), dtype=float)
            full[inside] = base.synthesize(grid[inside] / T, polynomials)
            image = np.fft.irfft(
                np.fft.rfft(full, axis=0) * symbol[:, None], n=points, axis=0
            )
            image -= m0 * full
            for integer, mangoldt in ((2, np.log(2.0)), (3, np.log(3.0)),
                                      (4, np.log(2.0))):
                shift = np.log(float(integer))
                coefficient = mangoldt / np.sqrt(float(integer))
                image[inside] -= coefficient * (
                    base.shifted(full, grid, grid[inside] + shift)
                    + base.shifted(full, grid, grid[inside] - shift)
                )
            image[:inside[0]] = 0.0
            image[inside[-1] + 1:] = 0.0
            return image, base.shifted(image, grid, tq)

        # Construct Q_N A applied to the selected safe combinations.
        response_grid, response_q = act_coefficients(combinations)
        response_polar = np.linalg.solve(
            moment_gram, moment_q.T @ (wq[:, None] * response_q)
        )
        response_q -= moment_q @ response_polar
        moment_grid = np.zeros((points, 2), dtype=float)
        moment_grid[inside, 0] = np.exp(grid[inside] / 2)
        moment_grid[inside, 1] = np.exp(-grid[inside] / 2)
        response_grid -= moment_grid @ response_polar
        projection = np.linalg.solve(gram, source_q.T @ (wq[:, None] * response_q))
        response_q -= source_q @ projection
        response_grid[inside] -= base.synthesize(
            grid[inside] / T, xframe @ projection
        )
        response_gram = response_q.T @ (wq[:, None] * response_q)
        re, ru = np.linalg.eigh((response_gram + response_gram.T) / 2)
        keep = re > max(re[-1] * 1e-11, 1e-14)
        whitening = ru[:, keep] * (1 / np.sqrt(re[keep]))
        w_grid = response_grid @ whitening
        w_q = response_q @ whitening
        # act_coefficients expects polynomial sources; W is a genuine
        # continuum response, so apply the operator directly on its grid.
        aw_grid = np.fft.irfft(
            np.fft.rfft(w_grid, axis=0) * symbol[:, None], n=points, axis=0
        )
        aw_grid -= m0 * w_grid
        for integer, mangoldt in ((2, np.log(2.0)), (3, np.log(3.0)),
                                  (4, np.log(2.0))):
            shift = np.log(float(integer))
            coefficient = mangoldt / np.sqrt(float(integer))
            aw_grid[inside] -= coefficient * (
                base.shifted(w_grid, grid, grid[inside] + shift)
                + base.shifted(w_grid, grid, grid[inside] - shift)
            )
        aw_grid[:inside[0]] = 0.0
        aw_grid[inside[-1] + 1:] = 0.0
        aw_q = base.shifted(aw_grid, grid, tq)
        aw_polar = np.linalg.solve(
            moment_gram, moment_q.T @ (wq[:, None] * aw_q)
        )
        aw_q -= moment_q @ aw_polar
        aw_grid -= moment_grid @ aw_polar

        extra_grid = [w_grid]
        extra_q = [w_q]
        extra_a_grid = [aw_grid]
        extra_a_q = [aw_q]
        reports = []
        levels = int(os.environ.get("P3_LOG5_ENRICH_LEVELS", "1"))

        def current_gate() -> tuple[np.ndarray, np.ndarray]:
            source_e = np.column_stack((source_q, *extra_q))
            acted_e = np.column_stack((acted_q, *extra_a_q))
            gram_e = source_e.T @ (wq[:, None] * source_e)
            measured_b = source_e.T @ (wq[:, None] * acted_e)
            measured_b = (measured_b + measured_b.T) / 2
            b_e = measured_b.copy()
            b_e[:width, :width] = np.diag(exact_values)
            projection_e = np.linalg.solve(
                gram_e, source_e.T @ (wq[:, None] * acted_e)
            )
            remainder = acted_e - source_e @ projection_e
            h_e = remainder.T @ (wq[:, None] * remainder)
            gate_matrix = (b_e - h_e / delta)
            gate_matrix = (gate_matrix + gate_matrix.T) / 2
            gg, gu = np.linalg.eigh((gram_e + gram_e.T) / 2)
            gi = (gu * (1 / np.sqrt(gg))) @ gu.T
            return gg[[0, -1]], np.linalg.eigvalsh(gi @ gate_matrix @ gi)

        gram_range, enriched_values = current_gate()
        reports.append((1, sum(x.shape[1] for x in extra_q),
                        gram_range, enriched_values[:16]))

        for level in range(1, levels):
            # Block-Lanczos continuation: the next columns are the part of
            # A W_level orthogonal to the entire current enriched chart.
            candidate_grid = extra_a_grid[-1].copy()
            candidate_q = extra_a_q[-1].copy()
            chart_q = np.column_stack((source_q, *extra_q))
            chart_gram = chart_q.T @ (wq[:, None] * chart_q)
            coefficients = np.linalg.solve(
                chart_gram, chart_q.T @ (wq[:, None] * candidate_q)
            )
            candidate_q -= chart_q @ coefficients
            candidate_grid[inside] -= base.synthesize(
                grid[inside] / T, xframe @ coefficients[:width]
            )
            offset = width
            for old_grid in extra_grid:
                stop = offset + old_grid.shape[1]
                candidate_grid -= old_grid @ coefficients[offset:stop]
                offset = stop
            cg = candidate_q.T @ (wq[:, None] * candidate_q)
            ce, cu = np.linalg.eigh((cg + cg.T) / 2)
            retain = ce > max(ce[-1] * 1e-11, 1e-14)
            if not np.any(retain):
                break
            transform = cu[:, retain] * (1 / np.sqrt(ce[retain]))
            new_grid = candidate_grid @ transform
            new_q = candidate_q @ transform

            new_a_grid = np.fft.irfft(
                np.fft.rfft(new_grid, axis=0) * symbol[:, None],
                n=points, axis=0
            )
            new_a_grid -= m0 * new_grid
            for integer, mangoldt in ((2, np.log(2.0)), (3, np.log(3.0)),
                                      (4, np.log(2.0))):
                shift = np.log(float(integer))
                coefficient = mangoldt / np.sqrt(float(integer))
                new_a_grid[inside] -= coefficient * (
                    base.shifted(new_grid, grid, grid[inside] + shift)
                    + base.shifted(new_grid, grid, grid[inside] - shift)
                )
            new_a_grid[:inside[0]] = 0.0
            new_a_grid[inside[-1] + 1:] = 0.0
            new_a_q = base.shifted(new_a_grid, grid, tq)
            new_polar = np.linalg.solve(
                moment_gram, moment_q.T @ (wq[:, None] * new_a_q)
            )
            new_a_q -= moment_q @ new_polar
            new_a_grid -= moment_grid @ new_polar
            extra_grid.append(new_grid)
            extra_q.append(new_q)
            extra_a_grid.append(new_a_grid)
            extra_a_q.append(new_a_q)
            gram_range, enriched_values = current_gate()
            reports.append((level + 1, sum(x.shape[1] for x in extra_q),
                            gram_range, enriched_values[:16]))

        enriched_report = (leak_e[-take:], reports)

    print("N/width points dx cells/order", n_modes, width, points, dx,
          len(edges) - 1, qorder)
    print("Gram range", gl[[0, -1]])
    print("finite primitive first", finite_e[:12])
    print("residual raw range/negative trace", he[[0, -1]],
          np.minimum(he, 0).sum())
    print("scalar-gap minimum/count negative", gate_e[0], int(np.sum(gate_e <= 0)))
    print("scalar-gap first 16", gate_e[:16])
    print("three-block promoted-tail kappa", kappa_260,
          "delta", delta, "margin", delta - kappa_260)
    if enriched_report is not None:
        print("selected safe leakage", enriched_report[0])
        for level, rank, gram_range, values in enriched_report[1]:
            print("enriched level/rank/Gram", level, rank, gram_range)
            print("enriched scalar gate first 16", values)
    np.savez(save, gram=gram, finite=finite, action2=action2,
             residual_raw=residual_raw, residual=residual,
             gate=gate, gate_eigenvalues=gate_e,
             finite_eigenvalues=finite_e, frame=xframe,
             points=np.array(points), dx=np.array(dx), delta=np.array(delta),
             kappa_260=np.array(kappa_260))
    print("saved", save)
    print("DIAGNOSTIC ONLY: binary64 FFT interpolation, no directed sign asserted")


if __name__ == "__main__":
    main()
