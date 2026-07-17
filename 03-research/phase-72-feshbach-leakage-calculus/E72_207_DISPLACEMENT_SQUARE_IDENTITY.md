# E72.207 - Displacement-square identity

## Purpose

E72.206 identified the local character jet as the next finite object. This note writes the second
character derivative exactly as a displacement-square weighted Green-word sum.

For

```text
A(t)=sum_alpha exp(it d_alpha) A_alpha,
```

where each signed cell has displacement

```text
d_alpha = eps log n,
```

define

```text
F_r(t)=Tr(A(t)^r).
```

Then

```text
F_r''(0)
= - sum_{alpha_1,...,alpha_r}
    (d_{alpha_1}+...+d_{alpha_r})^2
    Tr(A_{alpha_1}...A_{alpha_r}).              (DSQ)
```

This follows by differentiating the character phase of each word:

```text
exp(it(d_1+...+d_r)).
```

## Verification

Script:

```text
E72_207_displacement_square_identity_probe.py
```

It compares finite differences of `F_r''(0)` to the explicit displacement-square sum.

Output:

```text
E72.207 displacement-square identity probe
checks F''(0) = -sum_words Delta(word)^2 Tr(word)
lam block r fdSecond negDispSq relErr
  6     0 2 -8.511696858e+00 -8.511696954e+00 1.126e-08
  6     0 3 -5.486213661e+00 -5.486213733e+00 1.301e-08
  6     1 2 -1.048778344e+01 -1.048778376e+01 3.019e-08
  6     1 3 +4.796594616e+00 +4.796594852e+00 4.918e-08
  8     0 2 -8.518666172e+00 -8.518666239e+00 7.825e-09
  8     0 3 -2.127323323e+00 -2.127323368e+00 2.108e-08
  8     1 2 -1.045802189e+01 -1.045802226e+01 3.544e-08
  8     1 3 +1.555042586e+00 +1.555042705e+00 7.653e-08
 10     0 2 -9.639026022e+00 -9.639026143e+00 1.256e-08
 10     0 3 -3.579222452e+00 -3.579222537e+00 2.391e-08
 10     1 2 -1.402470324e+01 -1.402470383e+01 4.198e-08
 10     1 3 +5.611540410e+00 +5.611540883e+00 8.431e-08
 12     0 2 -1.076725722e+01 -1.076725743e+01 1.980e-08
 12     0 3 -1.978561465e+00 -1.978561531e+00 3.356e-08
 12     1 2 -1.319644289e+01 -1.319644362e+01 5.481e-08
 12     1 3 +4.224921868e+00 +4.224922335e+00 1.106e-07
```

## Reading

The signs found in E72.206 now have exact Green-word meaning:

```text
F''_{j,2m}(0)<0
```

means the displacement-square weighted even trace sum is positive:

```text
sum Delta(word)^2 Tr(word) > 0.
```

For the high-block cubic moment,

```text
F''_{1,3}(0)>0
```

means

```text
sum Delta(word)^2 Tr(word) < 0.
```

This is the same sign as the high-block cubic moment itself, but now weighted by squared displacement.

## Consequence

The next proof target is a family of finite displacement-moment inequalities:

```text
M_{j,r}^{(2q)}
 =
sum_words Delta(word)^(2q) Tr(word).
```

The augmentation certificate uses `q=0`. The local character rigidity supplies information at `q=1`.
If one can prove a finite moment problem linking `q=1` signs back to the `q=0` certificate moments,
then the augmentation inequalities become accessible without a global torus norm bound.
