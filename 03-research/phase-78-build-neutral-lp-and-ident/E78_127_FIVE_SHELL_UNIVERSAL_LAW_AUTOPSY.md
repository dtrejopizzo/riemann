# E78.127 - There is no simple universal sign-ratio law for the five-shell mode-2 profile

**Scope:** front B only, live object `FIVE-SHELL-MODE2(t)`.  
**Class:** AUTOPSIA theorem-grade.  
**What we know after this doc that we did not know before:** the five-shell
profile does not collapse to a simple universal alternating-geometric law across
the audited builds. The planted build has such a signature; zeta does not.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. This remains inside the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No lower-bound/sign mechanism is used.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral gap is assumed.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator,
       no ambient inverse norm is used as a theorem.
P76.061: respected. The autopsy concerns the explicit signed short profile
         already isolated on the safe axis.
E72.16/E77.7az: respected. This is front B; planted separation is admissible.
```

## 1. Starting point

E78.126 reduced the audited safe transform to the finite signed profile

```text
FIVE-SHELL-MODE2(t)
 = -v_2(0)/t + sum_{1<=n<=5} K_t(d_n) v_2(n).              (U-1)
```

The next obvious hope is that the coefficient vector

```text
(v_2(0),v_2(1),...,v_2(5))                                 (U-2)
```

might obey a short universal sign/ratio law, so that `(U-1)` collapses to a
one-parameter or geometric template.

## 2. Probe

Companion files:

```text
E78_127_five_shell_signature_probe.py
E78_127_five_shell_signature_results.json
```

After fixing the global sign by forcing the zero-shell coefficient positive, the
audited signatures are:

```text
BUILD zeta
N=8,12:
  signs = + - - + - +
  magnitude ratios =
    0.27, 3.28, 1.26, 0.55, 0.28
    0.43, 1.51, 1.80, 0.79, 0.47.                           (U-3)

BUILD plant
N=8,12:
  signs = + - + - + -
  magnitude ratios =
    0.83, 0.56, 0.37, 0.23, 0.12
    0.86, 0.62, 0.45, 0.31, 0.19.                           (U-4)
```

So the planted profile does look like a simple alternating decay law, but the
zeta profile does not: it has the different sign pattern `+ - - + - +` and its
ratios are neither monotone nor close to geometric.

## 3. Autopsy

This closes the route

```text
FIVE-SHELL-MODE2(t)  ?=  one universal alternating-geometric short law.      (U-5)
```

The exact failure is:

```text
the planted five-shell signature is simple alternating decay, but the zeta
signature is a different signed pattern with non-geometric ratios.           (U-6)
```

So any attempt to compress the zeta five-shell vector to a universal
alternating-geometric template is dead.

This does **not** kill the finite five-shell route itself. It only kills the
extra simplification to a one-parameter or universal sign-ratio law.

## 4. Consequence

The candid live object remains the full signed five-shell vector

```text
(v_2(0),v_2(1),...,v_2(5))                                 (U-7)
```

or a finite coupled coefficient carrying exactly that signed data.

So the next admissible question is not "what single ratio explains the five
shells?", but rather whether the five-shell vector can be recognized inside the
finite coupled package as a whole.

## 5. Status

```text
candidate closure - pending review

autopsied:
  the route "FIVE-SHELL-MODE2 obeys a universal alternating-geometric shell
  law";

proved:
  the planted and zeta five-shell signatures are structurally different, with
  the zeta vector refusing any simple geometric compression;

closed:
  one-parameter or universal sign-ratio explanations of the five-shell profile;

next:
  treat the full signed five-shell vector as the finite live object, or
  identify an equivalent finite coupled coefficient carrying it.
```
