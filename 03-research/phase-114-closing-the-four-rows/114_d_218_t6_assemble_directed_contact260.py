#!/usr/bin/env python3
"""Assemble a directed symmetric V260 contact enclosure.

Inputs:
  * the already directed complete V200 contact block;
  * directed rows 200:260 against all columns 0:260.

For the duplicated high-high entries we average the two ball centres and
inflate by half their centre discrepancy plus both radii.  Thus symmetry
is imposed by an enclosure operation, never by discarding disagreement.
"""
from __future__ import annotations

import os
import numpy as np


N0, N1 = 200, 260
old_path = os.environ.get("D218_OLD", "/tmp/d185_contacts6_arb.npz")
high_path = os.environ.get(
    "D218_HIGH", "/tmp/t6_contact_high200_260_arb.npz"
)
save_path = os.environ.get("D218_SAVE", "/tmp/t6_contacts260_arb.npz")

old = np.load(old_path)
high = np.load(high_path)
assert old["C"].shape == old["R"].shape == (N0, N0)
assert high["C"].shape == high["R"].shape == (N1 - N0, N1)
assert int(high["row_start"]) == N0 and int(high["row_end"]) == N1

C = np.zeros((N1, N1), dtype=float)
R = np.zeros((N1, N1), dtype=float)

# Directed old block.  Symmetric inflation covers any serialization skew.
Co = np.asarray(old["C"], dtype=float)
Ro = np.asarray(old["R"], dtype=float)
C[:N0, :N0] = (Co + Co.T) / 2
R[:N0, :N0] = (Ro + Ro.T + np.abs(Co - Co.T)) / 2

Ch = np.asarray(high["C"], dtype=float)
Rh = np.asarray(high["R"], dtype=float)

# Old-high entries have one directed enclosure, mirrored exactly.
C[N0:, :N0] = Ch[:, :N0]
R[N0:, :N0] = Rh[:, :N0]
C[:N0, N0:] = Ch[:, :N0].T
R[:N0, N0:] = Rh[:, :N0].T

# Each high-high entry was computed twice.  Average balls with an explicit
# discrepancy allowance, then mirror the result.
B = Ch[:, N0:]
RB = Rh[:, N0:]
C[N0:, N0:] = (B + B.T) / 2
R[N0:, N0:] = (RB + RB.T + np.abs(B - B.T)) / 2

# Cover all binary operations used by this assembler.  The producer balls
# already cover their Arb-to-binary conversion; this final inflation covers
# the averaging and assignments above.
R += np.abs(np.spacing(C))
R = np.nextafter(R, np.inf)

assert np.isfinite(C).all() and np.isfinite(R).all()
assert np.array_equal(C, C.T)
assert np.array_equal(R, R.T)
assert (R >= 0).all()

np.savez(
    save_path,
    C=C,
    R=R,
    endpoint=np.array(6),
    N=np.array(N1),
    old_source=np.array(old_path),
    high_source=np.array(high_path),
)

print("old serialized max radius", float(R[:N0, :N0].max()))
print("old-high serialized max radius", float(R[:N0, N0:].max()))
print("high-high serialized max radius", float(R[N0:, N0:].max()))
print("high-high centre skew before enclosure", float(np.max(np.abs(B - B.T))))
print("saved", save_path)
print("D218 DIRECTED SYMMETRIC CONTACT260 ASSEMBLY: PASS")
