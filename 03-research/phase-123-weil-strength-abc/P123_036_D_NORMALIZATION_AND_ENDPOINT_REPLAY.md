# P123.036 — normalization reaches the existing D operator; endpoint replay

Status: PROVED for the scalar normalization dictionary
and its match to the inspected operator/assembly. Tier-1 endpoint
recombination and five manifest hashes PASS. All seven Tier-2 jobs have
completed successfully, their enclosures have been checked against the
budget inputs, and the final margins have also been recomputed with Arb.
No full A/B/C/D row is closed.

## 1. From scalar packets to the primitive form

For F in C_c^infinity((-T,T)), set F^dagger(t)=conjugate(F(-t))
and h=F*F^dagger. Then h_hat=|F_hat|^2 and h has support in [-2T,2T].
Let M_+(F)=integral F(t)exp(t/2)dt and similarly M_- with the minus sign.
The polar packet evaluated on h is

    M_+(F) conjugate(M_-(F))
      +M_-(F) conjugate(M_+(F)).

In particular it vanishes when both primitive moments vanish. It is
not a sum of the two squared absolute moments for general F.

Using P123.032's prime packet and P123.035's archimedean packet,
the resulting primitive scalar form is

    q(F)= (1/(2 pi)) integral
             [Re psi(1/4+i tau/2)-log pi] |F_hat(tau)|^2 dtau
          -sum_(2<=n<exp(2T)) Lambda(n)/sqrt(n)
                    <(S_log(n)+S_-log(n))F,F>.     (1.1)

Here S_aF(t)=F_tilde(t+a), with zero extension, and the inner product
is linear in the first entry. Direct substitution gives
h(a)=<S_aF,F>. At log n=2T the supports meet only on a null set,
which explains the strict cutoff in (1.1).

Equation (1.1) is a scalar calculation. Identifying the new carrier's
intersection with it is still the missing A/C theorem. Positivity of
this form for all primitive windows is still D, not a consequence of
its definition or its Fourier representation.

## 2. Compare the two Gamma splittings exactly

Put

    m0=log pi-psi(1/4)=log pi+gamma+pi/2+3 log 2,
    g_a(tau)=Re psi(a+i tau/2)-psi(a).

Then the first multiplier in (1.1) is g_(1/4)-m0. The recurrence
psi(z+1)=psi(z)+1/z gives the equivalent decomposition

    g_(1/4)(tau)-m0
      =g_(5/4)(tau)+psi(5/4)-log pi
                           -1/(tau^2+1/4).        (2.1)

The last term has convolution kernel exp(-|t|/2), with coefficient one.
This matches the shifted Gamma form and polar resolvent used in
P122.002. No doubling of that resolvent is required.

For b_j=2j+1/2 the convergent digamma difference series is

    g_(1/4)(tau)=sum_(j>=0)
                    [2/b_j-2b_j/(b_j^2+tau^2)].    (2.2)

Thus each summand is the multiplier of (2/b_j)I minus convolution
with exp(-b_j|t|). This supplies a direct check of the interval assembly's
Gamma coefficients, independently of the discrepant printed real kernel.

## 3. Inspected authoritative files

* Paper 42, main.tex, eq:localizedprimitiveoperator and its displayed
  g_Gamma: uses exactly g_(1/4)-m0 and the prime-power shifts of (1.1).
* P122.002: uses g_(5/4) for the form-domain/compactness argument and
  exp(-|t|/2) for the polar resolvent, consistently with (2.1).
* The packaged 114_d_77_log3_legendre_arb_verify.py sets
  M0=log(pi)+gamma+pi/2+3log(2), BVALS=2j+0.5, and assembles
  sum(2/b)I-M0 I minus the exponential kernels, matching (2.2).
* The D.84 and D.85 packaged drivers reuse that assembly through the
  declared source transformations. Their full interval replay is the
  next validation layer; this algebraic inspection is not that replay.

Therefore the real-source coefficient finding in P123.035 does not
require doubling or halving the inspected D operator. The existing
operator already uses the Fourier-normalized Gamma multiplier. This
claim covers these inspected definitions, not every historical document.

## 4. Endpoint verification layers

The five SHA-256 pins in the packaged log2 manifest all matched. The
original Tier-1 recombination script exited successfully:

    final capacity margin > 8.6338602209512485e-8,
    odd final lower       > 8.1385617547899804e-6.

These are recombinations of recorded enclosures. They do not regenerate
the input intervals. One reporting distinction matters: the recomputed
v2/complement bound is 0.002033697282469699814..., strictly below the
Rayleigh input 0.0020336972824697. The packaged README and paper appendix
use the latter as a complement lower bound; that particular stronger
rounded statement is not proved by this recombination. A conservative
complement bound is 0.00203369728246969, still well above the 0.0015
actually used in the remaining budget. The regenerated, less-rounded
Rayleigh enclosure, combined directly with its residual in Arb, DOES
recover a complement bound greater than 0.0020336972824697. Thus the
stronger published value is supported by the regenerated data, although
the rounded Tier-1 recombination alone is insufficient to show it. The old /tmp/d61-flint environment was absent, so
an isolated /tmp/p123-certificate-venv was created with python-flint
0.9.0 and numpy 2.5.2. No paper or pinned script was modified.

[p123_036_replay_endpoint.py](p123_036_replay_endpoint.py) runs the
manifest's seven interval jobs and its recombination command, using
at most two child processes, recording the complete Python input hashes,
package versions, process exits and logs in
[endpoint_replay_20260905/report.json](endpoint_replay_20260905/report.json).
Environment selectors are reset before each job. BLAS thread limits
change scheduling only; the certificate computations remain in the
original scripts. A zero exit is recorded as execution evidence and
must be accompanied by inspection of the asserted bounds and log scope.

Current Tier-2 verdict: PASS. All eight scheduled jobs (seven interval
jobs plus Tier 1) exited zero. The logs show positive directed congruence
disks for both lifted projected blocks, the three Rayleigh/residual
certificates, generic high-space bounds, and the capacity integral.

[p123_036_check_replay.py](p123_036_check_replay.py) independently parses
the printed Arb balls at 1024-bit precision, checks every relevant
inequality against the original budget inputs, and rechecks all Python
source hashes. It also recombines the final bounds using directed Arb
arithmetic rather than relying solely on Decimal output. Results and log
hashes are in [enclosure_check.json](endpoint_replay_20260905/enclosure_check.json).
The verified conservative margins are

    even capacity margin > 8.63386022095e-8,
    odd final lower      > 8.13856175478e-6.

This reproduces the recorded log2 endpoint certificate in its declared
full-space framework. It does not constitute a new global sign law,
prove the common A/B/C realization, or certify any window beyond log2.
The first-contact continuation still requires the independent law
identified in P122.028–029 and the approved plan.
