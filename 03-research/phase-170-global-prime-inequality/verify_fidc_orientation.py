"""Finite algebra falsifier for the Tate adjoint; not a zeta/contact model."""
import json
import numpy as np


def pair(x, y):
    return np.vdot(y, x)  # Linear in the first argument, as in Paper 47.


def run():
    n = 17
    eye = np.eye(n)
    shift = np.roll(eye, -1, axis=0)
    reflection = eye[(-np.arange(n)) % n]
    angles = 2 * np.pi * np.fft.fftfreq(n)
    def multiplier(symbol):
        return np.fft.ifft(symbol[:, None] * np.fft.fft(eye, axis=0), axis=0)
    u = multiplier(np.exp(0.8j * np.sin(angles)))
    fourier = u @ reflection
    a = multiplier(2 + np.cos(angles)) - 0.3 * (shift + shift.T)
    s = eye + 0.7 * shift + 0.2 * shift @ shift
    positions = np.minimum(np.arange(n), n - np.arange(n))
    window = positions <= 3
    f = np.where(window, np.cos(positions), 0)
    g = np.where(window, np.cosh(positions / 3), 0)
    r = np.where(window, np.cosh(positions / 2), 0)
    first = pair(s @ a @ fourier @ f, g)
    old = first - pair(s @ r, fourier @ g)
    corrected = first - pair(s.T @ r, fourier @ g)
    exterior = pair(a @ f - r, s @ fourier @ g)
    extra = pair((s.T - s) @ r, fourier @ g)
    algebra_errors = dict(
        involution=float(np.linalg.norm(fourier @ fourier - eye)),
        adjoint=float(np.linalg.norm(fourier - fourier.conj().T)),
        intertwining=float(np.linalg.norm(fourier @ s.T - s @ fourier)),
        commutation=float(np.linalg.norm(a @ fourier - fourier @ a)),
        corrected_identity=float(abs(corrected - exterior)),
        original_extra_identity=float(abs(old - corrected - extra)))
    assert max(algebra_errors.values()) < 1e-12
    assert abs(extra.real) > 1e-3
    v = np.array([1.0, -1.0])
    positive_weight_shift = np.array([[0.0, 1.0], [0.0, 0.0]])
    assert pair(positive_weight_shift @ v, v) == -1
    return dict(algebra_errors=algebra_errors,
                original_flux=float(old.real), corrected_flux=float(corrected.real),
                nonzero_tate_defect=float(extra.real),
                positive_weight_negative_pairing=-1,
                is_arithmetic_counterexample=False)


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
