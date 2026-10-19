# R163_106 — Exponential torsion cocycle: exact sign and geometric gate

**Status:** identity and coercive bound proved; coupling with first contact **open**. Neither RH nor the closure of Row D is asserted. This memo returns to the specific ζ ingredient that survived in paper 48: the `×p` cocycle of `Φ_Λ` (paper 48, Thm `thm:cocycle`; `R162_1001`). Unlike the Paley–Wiener tests of `R162_2201`, the exponential test has infinitely many Fourier modes. That alone is not enough to get past `R162_2201` or the E1 wall.

**Later audit:** `R163_107` proves that the canonical Möbius lift `h_F` of `R162_1001` satisfies `h_F(0)−∫h_F=2||F||²` for every `F`, including in the radical. So **that** natural coupling is ruled out: the linear term does not vanish at contact. Only a genuinely different construction with a polar/exterior profile remains open.

## 1. Non-linear arithmetic identity

On `T=R/Z`, normalize `∫_T1=1`. The distribution `Φ_Λ` satisfies

```
⟨Φ_Λ,g(p·)−g⟩ = (log p)[g(0)−∫_T g(x)dx]
```

for each ordinary prime `p` and each smooth test `g`. Indeed, `Φ̂_Λ(k)=log|k|` for `k≠0`, `Φ̂_Λ(0)=0`, and `log|pk|−log|k|=log p`. Composition by `×p` is the adjoint of the transfer operator used in paper 48.

Now let `h∈C^∞(T;R)` and `g=e^h`. The exact identity is

```
E_p(h):=⟨Φ_Λ,e^{h(p·)}−e^h⟩
      = (log p)[e^{h(0)}−∫_T e^{h(x)}dx].                 (1)
```

Even though `h` is trigonometric, `e^h` generally has infinitely many non-zero coefficients, which decay rapidly; the pairing with the logarithmically-growing distribution is well defined. In particular, (1) is not an equality obtained by truncating the comb to a finite window.

## 2. Coercive sign on the zero-first-order section

If `h(0)=∫_T h=:\bar h`, strict convexity of the exponential gives

```
E_p(h) ≤ −(log p)e^{min h}/2 ·∫_T(h−bar h)² dx ≤ 0,       (2)
```

with equality only when `h` is constant. Proof: for `u,v∈[min h,max h]`, Taylor with integral remainder gives `e^u≥e^v+e^v(u−v)+(e^{min h}/2)(u−v)²`. Take `v=bar h`, integrate and use `∫(h−bar h)=0`; finally `h(0)=bar h`. For `h=εv`, `v(0)=∫v=0`, the oriented expansion is

```
E_p(εv)=−(log p) ε²/2 ·∫_T v²+O_v(ε³).                (3)
```

Identity (3) is an **exact arithmetic negative square**, not the square of `(PC-ren)`, which loses the orientation. It comes directly from the exact Euler/divisor cocycle before any regularization. Its sign does not use RH.

## 3. What first contact would need to contribute to close D

The candidate gate is to build, from a non-zero witness `F∈ker H_{T_*}` and the Poisson–Tate collars, a non-constant `h_F∈C^∞(T;R)` such that:

1. `h_F(0)=∫h_F` follows **from the contact equation `λ=0`**, and not from a normalization chosen afterward;
2. the full geometric identity (including exterior and Gamma poles) implies `E_p(h_F)≥0` for at least one prime `p`, or an equivalent bound contradicting (2);
3. step (2) uses the orientation and the exact values of `Λ`, and the geometric step does not transport to `M_m`, `Λχ_2`, Epstein or the Type I curve.

Then (2) would force `h_F` constant; if the construction is also faithful on the kernel (`h_F` constant ⇒ `F=0`), first contact would be excluded and D would close. **None of the three implications is proved here.** In particular, the phrase `E_p(h_F)≥0` is exactly the new inequality that must not be introduced as a hidden hypothesis.

**Check against an empty normalization.** For any `h`, the functional `h(0)−∫h` is the sum of its non-zero Fourier coefficients. It can be artificially annihilated by adding `−(h(0)−∫h)cos(2πx)`. So point 1 would only carry mathematical content if `F↦h_F` is prescribed before knowing the value of `W_T(F)` and a structural identity is proved (e.g. `h_F(0)−∫h_F=c_T W_T(F)` with `c_T≠0`) compatible with every Gamma and exterior correction. Choosing the first Fourier mode to impose it by hand does not count.

## 4. Falsifiers and non-circularity

- **Finite modification `a=Λ+η`:** the cocycle adds a defect with Fourier coefficients `(η*1)(p|k|)−(η*1)(|k|)`, so (1) changes. So the exact sign is sensitive to the values of Λ, not just to its support or to an approximation.
- **Non-integer Beurling:** torsions `ν_d` over `R/Z` are not defined for non-integer generalized indices; the object `Φ_a` does not transport without introducing other structure.
- **`M_m`:** if the same prime side of ζ is formally assigned to it, (1) still holds for any `h`. So (1) **does not by itself separate** the rational-zero model; the construction `F↦h_F` and the geometric inequality must also use ζ's genuine relation between Euler and the functional equation. This is a mandatory falsifier for the gate.
- **`Λχ_2`:** the ordinary cocycle fails (replaced by a twisted one); even so an analogue of (2) could exist, so the geometric step must fail there in a localizable way.
- **Arbitrary test:** e.g. `h(x)=ε sin(2πx)` satisfies `h(0)=∫h=0` and already makes (2) strict, with no relation to zeros. So (2) alone carries no new information about RH; the needed novelty lies in the non-formal coupling to the contact witness.

## 5. Judgment

The exponential avoids the *literal* band-limitation obstacle of polynomial tests: it reads every mode. But `Φ̂_Λ(k)=log|k|` is still a known identity; (1) may be a restatement unless an independent geometric inequality is obtained on the kernel. The development keeps exactly that separation. Next falsifiable test: try to build `h_F` from the witness and check point 1 **before** looking for point 2. If point 1 can only be imposed by arbitrary normalization, this route is discarded.

**Comparison with the earlier torsional no-go.** If `h_F` depends only on a finite list of scalars of the witness, `e^{h_F}` is an infinite kernel *separable* in the sense of `R162_1101 §5`: the exponential kernel is fixed and receives those scalars as parameters. Escaping band limitation does not prove escaping the result of `R162_1101` that localizes the Gamma residue in the identity atom. Moreover (1) does not yet contain a meromorphic parameter `s` nor a polar residue. So, for this route to be more than just a sign about torsion, the construction must explicitly show how physical compression and `(PC-ren)` turn (1) into a residue/exterior identity that does **not** reduce to the 0 atom. No such conversion appears in this memo.
