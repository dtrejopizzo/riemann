# Paper 16 — An unconditional finite bottom for the localized Weil form: a verified second-moment identity, an almost-everywhere clean bound, and the residue as a uniform short-interval prime variance

The paper studies semiboundedness of the localized Weil form (archimedean minus prime part): a finite lower bound, strictly weaker than finiteness of the negative index. It writes the controlling second moment V(d,T) as a band-limited square, shows the low-frequency part costs nothing, obtains an unconditional lower bound with a logarithmic loss, removes that loss off a super-polynomially sparse set of heights, and identifies the clean bound with a uniform short-interval prime variance. No claim is made about the sign of the form.

## Main results
- `thm:id` (Second-moment identity): V(d,T) = ∫_{-2d}^{2d} |Σ_γ e^{iγξ}|² dξ ≥ 0, diagonal 4dN. PROVED; checked against true zeros to 1e-6 (NUMERICAL).
- `prop:parseval` (Band-limited Parseval bound): a bound on V gives a lower bound for the form on the window. PROVED.
- `prop:low`: the low-frequency part is O(N) unconditionally. PROVED (uses cited Montgomery form-factor asymptotics).
- `prop:S` (Finite bottom modulo a logarithm): form ≥ −C(log T)^c ‖g‖². PROVED.
- `thm:ae` (Clean bound almost everywhere): the clean bound holds off a set of heights of super-polynomially small density. PROVED (via Selberg's moments, CITED).
- `thm:gm` (Goldston–Montgomery): clean bound ⟺ uniform short-interval prime variance. CITED.
- `cor:noncirc`: removing the logarithmic loss is equivalent to the uniform form factor; the target is non-circular. PROVED; the target itself OPEN.
- `prop:rfb` (Relative-form-bound reduction): a tail bound with constant < 1 gives finite negative index. PROVED (conditional on the hypothesis RFB_X, which is OPEN).

## Files
- `main.tex`, `main.pdf` — source and compiled paper.
- `code.py` — verification of the second-moment identity with real zeros.
- `atail.py` — numerical test of the prime-tail relative form bound a_tail(X).
- `near.py` — spectrum of the archimedean/prime pencil as the band grows.
