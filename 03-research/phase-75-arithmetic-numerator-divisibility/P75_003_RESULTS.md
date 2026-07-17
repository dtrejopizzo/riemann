# P75.003 results

Command:

```text
python3 P75_003_bordered_determinant_probe.py
```

Result:

```text
P75.003 bordered determinant / adjugate identity
generic mu=-5.000000 tr_adj=4.236279e+09
  z=1.3          c_err=1.443e-15 p_abs_err=6.836e-02 p_rel_err=1.215e-14
  z=4.7          c_err=1.374e-15 p_abs_err=1.906e+00 p_rel_err=1.224e-14
  z=(1.8+0.2j)   c_err=1.001e-15 p_abs_err=5.865e-02 p_rel_err=1.969e-15
planted-like mu=-4.630000 tr_adj=1.651413e+09
  z=1.3          c_err=3.691e-15 p_abs_err=1.641e-01 p_rel_err=2.916e-14
  z=4.7          c_err=2.567e-15 p_abs_err=3.469e+00 p_rel_err=2.228e-14
  z=(1.8+0.2j)   c_err=2.649e-16 p_abs_err=2.431e-02 p_rel_err=8.160e-16
```

The adjugate identity removes the explicit eigenvector phase and holds at
roundoff for both generic and planted-like controls.  Therefore it cannot
itself be the zeta-discriminating arithmetic input; the discriminator must be
a divisibility theorem for the adjugate/minor expression.

