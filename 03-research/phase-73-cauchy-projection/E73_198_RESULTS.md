# E73.198 results - digamma WR tail

Command:

```text
python3 E73_198_digamma_wr_tail_probe.py
```

Output:

```text
E73.198 digamma WR tail
Compares direct grouped tail with digamma/polygamma signed form.
 lam     L gamma row    R groupB digamB errB
  12   4.970   14.13   0   400  -15.05  -15.04  -17.70
  12   4.970   14.13   0  1000  -15.62  -15.60  -17.70
  12   4.970   14.13   0  2500  -16.21  -16.16  -17.70
  16   5.545   14.13   0   400  -14.69  -14.67  -16.61
  16   5.545   14.13   0  1000  -14.82  -14.79  -16.61
  16   5.545   14.13   0  2500  -15.28  -15.22  -16.62
```

Reading:

```text
The displayed error is mostly the algebraic tail omitted by the finite
`grouped` summation cutoff, not an error in the digamma formula.
```

For `lambda=12`, `R=400`, increasing the grouped cutoff gives:

```text
cutoff 30000   error scale L^-17.70
cutoff 100000  error scale L^-18.44
cutoff 300000  error scale L^-19.12
```

The digamma formula evaluates the infinite paired tail directly.

Conclusion:

```text
The signed WR tail now has a closed special-function form:

T_R(B)=sum c_omega D_1(R,omega)+sum l_omega D_2(R,omega)
      + exponentially small correction,

D_1=1/2[psi(R+1/2)-psi(R+1/4-iomega/2)],
D_2=1/4 psi_1(R+1/4-iomega/2).
```

This is the correct object for interval certification.
