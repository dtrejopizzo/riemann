# R162_301 — C1: the noncommutative Euler lift and its physical descent


Status: **NO-GO (with proved identities).** The root-valued lift of `A_P(S)` exists on `H_T` itself
and is the global Brown–Halmos identity. Its root is a Hankel operator. It carries none of the
Sonin/Gamma data, holds for every `g in H_T`, and holds for every bounded analytic Dirichlet symbol.
The global anomaly (root of the product minus the product of local roots) has a closed form.
It is **not** sign-definite: an explicit two-prime vector makes it negative. It is **not**
Λ-specific. The Gamma "descent" is one application of the unitarity of `C_log`. So this route
supplies no new input for Gate 1. Of the two options in R162_207 §4, only option 2 is left.

Corpus check: P122_013/015 (local line and cocycle `1-r^2`), P122_014 (naive assembly gives the
target form), P122_016 (the physical carrier is semifinite, so `[P_+,U_a]` has infinite
multiplicity), P122_018 (the symmetric Γ–Euler cocycle is zero), R161_045. Nothing below repeats
those results. §1 shows that R162_202 Thm 3.1 is a special case of §1 that needs no Sonin
hypothesis. §3–§4 are new: the ordered anomaly and its indefiniteness.

## 0. Filter (before building)

- **Not trivially F=0 (compare R162_203).** The lift is an operator identity on all of `H_T`. It
  does not rewrite `sup_P ||A_P g||<infinity` (which R162_203 showed is equivalent to F=0). Its
  hoped-for contribution was a *sign or Λ-rigidity* of the anomaly. §3–§5 decide that this
  contribution is absent.
- **F1.** The lift never uses λ=0. It could be useful only if the anomaly were Λ-rigid or had a
  sign that first contact could exploit. §4 refutes the sign; §5 refutes the rigidity.
- **F2.** `[A^*,A]` is oriented: it is `A^*A-AA^*`, not a square of (PC). But it is invariant under
  `A->-A`, so it cannot orient the (PC) sign. It fails F2 as a closing device.
- **F3.** Tested in §5. It fails: the identity is universal.
- **F4.** Every statement is a finite operator identity. No linear graph limit is used.

The construction was therefore expected to be at most a PARTIAL. The point of the note is to
settle (a), (b) and (c) exactly.

## 1. The global lift is Brown–Halmos on the half-line (PROVED)

Notation follows R162_202. `P=P_T` is the projection of `L^2(R)` onto `H_T`, and `U_a` is
translation. The forward delays satisfy `S_a = U_a|_{H_T}` and `S_a^* = P U_{-a}|_{H_T}`.

Let `f(U)=sum_n c_n U_{lambda_n}` be any absolutely convergent sum with `lambda_n>=0` and real
`c_n`. Put `T_f=f(U)|_{H_T}=f(S)`, so that `A_P=T_f` for `f=prod_p(1-r_pU_{a_p})`. The adjoint is
`f(U)^*=f^-(U)=sum c_nU_{-lambda_n}`, and the Hankel operator is

    H_f := (I-P) f^-(U) |_{H_T} : H_T -> L^2((-inf,T)).

**Theorem 1.1.** `T_f^*T_f - T_fT_f^* = H_f^* H_f`. Hence, for **every** `g in H_T`,

    ||T_f g||^2 - ||T_f^* g||^2 = ||(I-P_T) f^-(U) g||^2.          (1.1)

*Proof.* `f(U)` preserves `H_T`, so `T_f^*T_f = P f(U)^*f(U) P`. Also `T_fT_f^* = P f(U) P f(U)^* P`.
`f(U)` is a function of commuting unitaries, so it is normal. Therefore
`T_f^*T_f-T_fT_f^* = P f(U)(I-P) f(U)^* P = H_f^*H_f`. ∎

**Corollary 1.2.** R162_202 Theorem 3.1 holds for all `g in H_T`. The Sonin hypothesis (1.2) there
is idle: `||A_Pg||=||A_P^-(U)g||` is normality of `A_P(U)`, not unitarity of `C_log`.

So the "root" of the global self-commutator is the Hankel operator `H_P:=H_f`. This is the
continuous-time form of R161_045 (1.2). It is not rank one: by P122_016 each `Pi_a:=I-S_aS_a^*`
(the projection onto `L^2[T,T+a)`) has infinite rank. "Rank one" holds only fibrewise in the
Floquet decomposition over `[0,a_p)`.

## 2. Where Gamma/Tate enters: the descent is tautological (PROVED)

Let `K_T := (I-P_T) C_log |_{H_T}`, the Sonin defect of the Gamma kernel. A vector `g` satisfies
R162_202 (1.2) iff `g in H_T` and `C_log g=-eps g`. In that case `K_T g=0`.

**Proposition 2.1 (crossed Γ–Euler identity).** For such `g`,

    K_T A_P(S) g = -eps H_P g,     so   ||H_P g|| = ||K_T A_P(S) g||.     (2.1)

*Proof.* `C_log A_P(S)g = A_P^-(U) C_log g = -eps A_P^-(U) g`, by R162_202 (1.1). Apply `I-P_T`. ∎

This is the only way the crossed Gamma term appears: the Γ-Hankel applied to the Euler-stripped
port equals the Euler-Hankel of the port. Combined with unitarity,
`||A_Pg||^2 = ||P_T C_log A_P g||^2 + ||K_T A_P g||^2`, which is again (1.1). The descent therefore
adds nothing: the Gamma operator only intertwines two Hankel squares of the same vector. No Tate
endpoint or polar term appears, because none is present in `A_P(S)` on `H_T`. That is consistent
with P122_018: the symmetric mixed cocycle vanishes.

## 3. Product of local roots vs root of the product: the anomaly in closed form (PROVED; answers (a))

**Bohr (doubly commuting) model.** On `H^2(D^P)`, take `A_p = 1-r_p T_{z_p}`, `Y_p = A_pA_p^*`
and `D_p = A_p^*A_p - Y_p = r_p^2 E_0^{(p)}` (rank one). The operators in different variables
commute, so

    [A^*,A]_Bohr = prod_p (Y_p+D_p) - prod_p Y_p
                 = sum_{nonempty Q ⊆ P} prod_{p in Q} D_p prod_{p notin Q} Y_p  >= 0.   (3.1)

This is the "product of local roots". Every term is a nonnegative product of commuting nonnegative
operators.

**Physical model.** The `S_{a_p}` commute, but they do not doubly commute. For `a>=b`:

    [S_b^*, S_a] = S_{a-b} Pi_b ,      [S_a^*, S_b] = Pi_b S_{a-b}^*.        (3.2)

*Proof.* We have `S_b^*S_a=S_{a-b}` and `S_aS_b^*=S_{a-b}S_bS_b^*=S_{a-b}(I-Pi_b)`. Take the
adjoint for the second identity. ∎

**Theorem 3.1 (two-factor anomaly).** Let `A_1,A_2` be commuting bounded operators and put
`C:=[A_2^*,A_1]`. Then

    [(A_1A_2)^*,A_1A_2] = A_2^*[A_1^*,A_1]A_2 + A_1[A_2^*,A_2]A_1^* + X_{12},
    X_{12} = CC^* + A_1A_2^*C^* + C A_2A_1^*.                                (3.3)

*Proof.* First,
`A_2^*A_1^*A_1A_2 - A_1A_2A_2^*A_1^* = A_2^*[A_1^*,A_1]A_2 + A_1[A_2^*,A_2]A_1^* + (A_2^*A_1A_1^*A_2 - A_1A_2^*A_2A_1^*)`.
Substitute `A_2^*A_1 = A_1A_2^*+C` and `A_1^*A_2 = A_2A_1^*+C^*` into the first term of the
bracket and expand. ∎

For Euler factors `A_p=I-r_pS_{a_p}` with `p<q`,

    C_{pq} = [A_q^*,A_p] = r_p r_q Pi_{a_p} S_{a_q-a_p}^*.

The Bohr formula (3.1) is the case `C=0`. For `|P|>2`, apply (3.3) recursively with
`A_1=A_p` and `A_2=prod_{q≠p}A_q`. Then `C=[A_2^*,A_p]` is a finite sum of words in the operators
(3.2), with shifts `log(n/m)` over squarefree `m,n | N_P`. So the global anomaly
`Anom_P := [A_P^*,A_P] - (local part)` is an explicit finite combination of the partial isometries
`S_{log(n/m)}Pi_{log m}`. The answer to (a) is YES. The scalar form is

    <g,[A_P^*,A_P]g> = sum_{m,n | N_P} mu(m)mu(n)(mn)^{-1/2}
                         <S_{|log(n/m)|}^{(*)} Pi_{log min(m,n)} g, g>.     (3.4)

Here `(*)` means the adjoint is taken when `m>n`. The diagonal of (3.4) is
`sum_{n|N_P} n^{-1}||Pi_{log n}g||^2`, and its prime part is exactly the local collars
`sum_p r_p^2||Pi_{a_p}g||^2`. (3.4) follows from
`<(I-P)U_{-α}g,(I-P)U_{-β}g> = int_T^{T+min} g(s) conj g(s+|β-α|) ds`.

## 4. The anomaly is not sign-definite (PROVED; answers (b))

Put `Delta_P(g) := ||H_Pg||^2 - sum_p r_p^2||Pi_{a_p}g||^2`. This is the leakage minus the local
rank-one collars.

**Proposition 4.1.** For `P={p,q}` with `p<q`, write `a=log p`, `b=log q`, `r=p^{-1/2}` and
`s=q^{-1/2}`. Then `Delta_P` takes both signs on `H_T`.

*Proof.* On `t<T`,

    (H_Pg)(t) = -r g(t+a) - s g(t+b) + rs g(t+a+b).

(i) Take `g=1_{[T,T+eps)}` with `eps<min(a,b-a)`. The three pieces have disjoint supports, so
`||H_Pg||^2 = (r^2+s^2+r^2s^2)eps` and `Delta_P = r^2s^2 eps > 0`.

(ii) Choose any `g_0 ≠ 0` on `[T,T+a)`. Extend it by `g(u+a)=g(u)/r` for `u in [T,T+b)`, and set
`g=0` beyond `T+a+b`. For `t in [T-b,T)` we have `t+b in [T,T+b)`, so
`-s g(t+b)+rs g(t+a+b)=0`. What remains is `rs g(t+a+b)` on `[T-a-b,T-b)` and `-r g(t+a)` on
`[T-a,T)`. Hence `||H_Pg||^2=(r^2+r^2s^2)||g_0||^2`. Therefore

    Delta_P(g) = r^2s^2||g_0||^2 - s^2||1_{[T,T+b)}g||^2 <= (r^2-1)s^2||g_0||^2 < 0. ∎

Only the total `||H_Pg||^2` is positive, and it is a square. The anomaly relative to the local
roots is indefinite. The same holds for the cross operator `X_{12}` in (3.3), because
`<g,X_{12}g> = ||C^*g||^2 + 2Re<C^*g, A_2A_1^*g>` is linear in `C` in its second term. The answer
to (b) is NO. Indefiniteness restricted to the Sonin subspace was not decided. Nothing hinges on
it: by §1–§2 the identity does not see Sonin membership except through the tautology (2.1).

## 5. The anomaly is not Λ-specific (PROVED; answers (c))

Theorem 1.1 holds for every absolutely convergent analytic symbol `f`. This includes:

- a finite modification: `f_a = f_Λ · exp(-sum_n eta(n)n^{-1/2}U_{log n}/log n)`, which is again
  analytic and bounded on the finite level;
- Davenport–Heilbronn truncations `sum_{n<=N} c(n)n^{-1/2}U_{log n}`, which have no factorization.

In each case the product rule `H_{f_1f_2} = tilde T_{f_1^-}H_{f_2} + H_{f_1}T_{f_2^-}` gives the
same kind of closed-form anomaly. Here `tilde T` is the compression to `(-inf,T)`, and the rule
follows from inserting `I=P+(I-P)`. The only Λ-dependent datum is structural: each prime factor
has degree one, so its local defect is fibrewise rank one. The modifier factor has local defects of
higher fibre rank. Rank structure carries no sign, and the ESB-type conclusion is insensitive to it
(R162_204 Thm 2.1). The answer to (c) is NO: the lift passes neither half of F3.

## 6. Verdict and next sub-lemma

- The global noncommutative lift is the half-line Brown–Halmos identity with Hankel root.
  **PROVED.** It is valid for all `g in H_T` and all analytic symbols.
- The Gamma/Tate descent is the tautology (2.1). **PROVED.** It is not new input.
- The anomaly has the closed form (3.3)–(3.4). **PROVED.**
- The anomaly is indefinite (Proposition 4.1). **PROVED.**
- The anomaly is universal, not Λ-specific. **PROVED.**
- Option 1 of R162_207 §4, restricted to Toeplitz/Hankel lifts on `H_T` or `H^2(D^P)`:
  **NO-GO.** No Toeplitz lift of the finite synthesis can separate Λ from its finite modifications,
  because the self-commutator identity (1.1) is symbol-independent.

**Exact next sub-lemma (option 2 of R162_207).** *Coefficient-direction stationarity at Λ.* For a
primitive first-contact `F` with `H_{T_*,Λ}F=0`, and every finitely supported `eta`, decide whether

    d/du <F, H_{T_*,Λ+u eta} F> |_{u=0} = Re <Delta_{N}^{eta}-type Ward vector (R162_205 (2.2)), F>

vanishes identically in `eta`. If it does, that would be an independent equality law, and it would
have to be derived from the Euler identity `Λ*1=log` rather than from (PC-ren). If some `eta`
makes it nonzero, then first contact is not stationary in coefficient direction, and option 2 is
closed as well. The computation is finite: expand R162_205 (2.2) against `F` using
`b_{u eta} = u(eta*1)`.

Gate 1 and row D: **OPEN**.
