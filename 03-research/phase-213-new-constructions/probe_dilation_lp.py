"""Floating-point probe of the two-grid dilation problem in ROUND_195_A."""
import numpy as np
import mpmath as mp
from scipy.optimize import linprog
from scipy.sparse import csr_matrix, eye, hstack, vstack


def symbols(period, cutoff):
    step = 2 * np.pi / period
    tau = np.arange(int(cutoff / step) + 1) * step
    k_values, v_values = [], []
    for frequency in tau:
        s = mp.mpc(0.5, float(frequency))
        z = 2 ** (-s)
        factor = (1 - 2*z)**3 * mp.qp(z, mp.mpf('0.5'))
        v = mp.gamma(s) * mp.zeta(s, derivative=1) * factor
        v_values.append(complex(v))
        k_values.append(complex(v * mp.zeta(s)))
    weights = np.full(len(tau), 2 / period)
    weights[0] /= 2
    return tau, weights * k_values, weights * v_values


def readings(scale, nodes, count, data):
    tau, k_values, v_values = data
    left, right = np.log(1e-5 / scale), np.log(30.)
    step = (right - left) / count
    logs = left + (np.arange(count) + 0.5) * step
    phase = np.exp(-1j * np.outer(logs, tau))
    node_phase = np.exp(-1j * np.outer(tau, np.log(nodes)))
    matrix = (phase @ (k_values[:, None] * node_phase)).real / np.sqrt(nodes)
    normalization = np.exp(logs / 2) * step
    return matrix * normalization[:, None], (phase @ v_values).real * normalization


def solve(scale, data, check, cap_power=2, anchors=False):
    cosines = np.cos(np.pi * (np.arange(5) + 0.5) / 5)
    nodes = np.concatenate([2**j * (1.5 + 0.5*cosines)
                            for j in range(scale.bit_length() - 1)])
    if anchors:
        nodes = np.unique(np.r_[nodes, 1., 2., 3.])
    matrix, target = readings(scale, nodes, 350, data)
    design = csr_matrix(1e4 * np.column_stack([matrix, -matrix]))
    samples, columns = design.shape
    identity = eye(samples)
    constraints = vstack([hstack([design, -identity]), hstack([-design, -identity]),
                          csr_matrix(np.r_[np.ones(columns), np.zeros(samples)])])
    bounds = np.r_[1e4*target, -1e4*target, scale**cap_power]
    result = linprog(np.r_[np.zeros(columns), np.ones(samples)], A_ub=constraints,
                     b_ub=bounds, bounds=(0, None), method="highs")
    if not result.success:
        raise RuntimeError(result.message)
    positive, negative = np.split(result.x[:columns], 2)
    weights = positive - negative
    test, truth = readings(scale, nodes, 3501, check)
    b_one = -float(mp.log(2)**3 * mp.qp(mp.mpf("0.5"), mp.mpf("0.5")))
    mass_error = abs(b_one * np.dot(weights, 1/nodes))
    print(scale, cap_power, anchors, len(nodes), result.fun / 1e4, np.abs(test @ weights - truth).sum(),
          np.abs(weights).sum(), mass_error, flush=True)


if __name__ == "__main__":
    mp.mp.dps = 24
    training = symbols(64, 28)
    checking = symbols(80, 34)
    print("A cap_power anchors nodes training_L1 checking_L1 coefficient_TV mass_error")
    for scale in (4, 8, 16, 32, 64, 128):
        solve(scale, training, checking)
    for cap_power, anchors in ((1, False), (1, True), (2, True)):
        solve(128, training, checking, cap_power, anchors)
