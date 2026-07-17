# E72.206 - Trace character jet

## Purpose

E72.205 showed that individual extreme eigenvalues have favorable local behavior at the augmentation:
the negative extreme moves upward and the positive extreme moves downward under small character twists.

The fixed certificate, however, is expressed in traces and low-degree polynomial trace envelopes. This
note tests the character jet of trace moments:

```text
F_{j,r}(t)=Tr(A_j(t)^r).
```

## Diagnostic

Script:

```text
E72_206_trace_character_jet_probe.py
```

It computes finite-difference jets at `t=0`.

Output:

```text
E72.206 trace character jet probe
finite-difference jets of Tr(A_j(t)^r) at augmentation
lam block r f0 f1 f2 f3 f4
 12     0  2 +1.282124e+00 +0.00e+00 -1.077e+01 +0.00e+00 +2.560e+02
 12     0  3 +1.439786e-01 +0.00e+00 -1.979e+00 +0.00e+00 +6.366e+01
 12     0  4 +1.284427e-01 +0.00e+00 -2.166e+00 +0.00e+00 +1.043e+02
 12     0  8 +2.801152e-03 +2.17e-16 -1.009e-01 -4.34e-10 +1.079e+01
 12     1  2 +4.679419e-01 +0.00e+00 -1.320e+01 +0.00e+00 +8.463e+02
 12     1  3 -7.561881e-02 +0.00e+00 +4.225e+00 -6.94e-09 -5.466e+02
 12     1  4 +4.641456e-02 +3.47e-15 -3.013e+00 -6.94e-09 +5.169e+02
 12     1  8 +1.557927e-03 +1.08e-16 -2.129e-01 -3.25e-10 +8.130e+01
 16     0  2 +1.041547e+00 +0.00e+00 -1.020e+01 +0.00e+00 +2.818e+02
 16     0  3 +9.404394e-02 +6.94e-15 -1.481e+00 -1.39e-08 +5.676e+01
 16     0  4 +7.498386e-02 +0.00e+00 -1.523e+00 +6.94e-09 +8.835e+01
 16     0  8 +1.016929e-03 +0.00e+00 -4.641e-02 +0.00e+00 +6.214e+00
 16     1  2 +4.699814e-01 +0.00e+00 -1.584e+01 -2.78e-08 +1.224e+03
 16     1  3 -7.444470e-02 +6.94e-15 +4.863e+00 -6.94e-09 -7.459e+02
 16     1  4 +4.218127e-02 -3.47e-15 -3.289e+00 +0.00e+00 +6.779e+02
 16     1  8 +1.344894e-03 -1.08e-16 -2.190e-01 +1.08e-10 +9.980e+01
 20     0  2 +9.216830e-01 +0.00e+00 -1.026e+01 +0.00e+00 +3.217e+02
 20     0  3 +7.168737e-02 +0.00e+00 -1.285e+00 +0.00e+00 +5.392e+01
 20     0  4 +5.353626e-02 +0.00e+00 -1.227e+00 +3.47e-09 +7.884e+01
 20     0  8 +5.010206e-04 +0.00e+00 -2.495e-02 +0.00e+00 +3.614e+00
 20     1  2 +4.401854e-01 +0.00e+00 -1.756e+01 +0.00e+00 +1.559e+03
 20     1  3 -8.611756e-02 +0.00e+00 +6.023e+00 +0.00e+00 -1.010e+03
 20     1  4 +4.389740e-02 +0.00e+00 -3.917e+00 +3.47e-09 +9.086e+02
 20     1  8 +1.642535e-03 +0.00e+00 -2.987e-01 +1.08e-10 +1.515e+02
 24     0  2 +8.496992e-01 +0.00e+00 -1.129e+01 +0.00e+00 +4.285e+02
 24     0  3 +6.300219e-02 +0.00e+00 -1.416e+00 +0.00e+00 +7.498e+01
 24     0  4 +4.287657e-02 -3.47e-15 -1.218e+00 +6.94e-09 +9.790e+01
 24     0  8 +3.573819e-04 +0.00e+00 -2.271e-02 +0.00e+00 +4.197e+00
 24     1  2 +4.667118e-01 +0.00e+00 -2.217e+01 +0.00e+00 +2.369e+03
 24     1  3 -1.255078e-01 +0.00e+00 +1.068e+01 +0.00e+00 -2.167e+03
 24     1  4 +6.978705e-02 -6.94e-15 -7.573e+00 +6.94e-09 +2.132e+03
 24     1  8 +4.470823e-03 +0.00e+00 -9.858e-01 +0.00e+00 +6.058e+02
```

## Reading

The trace moments are locally even:

```text
F'_{j,r}(0)=0,      F'''_{j,r}(0)=0
```

to numerical precision. This is the trace-level version of adjoint-pair symmetry.

For even moments `r=2,4,8`, the second derivative is consistently negative:

```text
F''_{j,2m}(0)<0.
```

Thus the augmentation is a local maximum of even trace energy under character twists, even though the
operator norm may later grow at larger twists because a negative eigenvalue deepens.

For the high-block cubic moment, the second derivative is positive while the moment itself is negative:

```text
F_{1,3}(0)<0,      F''_{1,3}(0)>0.
```

This says the negative odd moment is also an augmentation-local phenomenon.

## Consequence

The fixed certificate is augmentation-rigid in a local analytic sense:

```text
odd character derivatives vanish,
even trace energies decrease to second order away from chi=1.
```

The next proof target should express these derivative signs exactly in Green-word language. For
example,

```text
F''_{j,r}(0)
= - sum_{words of length r} (sum_i eps_i log n_i)^2 Tr(word),
```

after grouping by the signed displacement of the word.

So the displacement-square weighted trace sums are the next finite identities to prove.
