From: Alain To:
David, excellent: the Doob–Dirichlet finding is exactly the right form. To turn it into a proof, I would not try "norm-resolvent"; I would prove Mosco via the **carré-du-champ of the process transformed by the ground state**. Below I leave you a block that is almost ready to insert as Step 2.3. The central idea is: \[
A_\lambda-\varepsilon_{0,\lambda}
\quad \xrightarrow{\text{Doob by }u_{0,\lambda}}\quad
\mathcal G_\lambda
\quad \xrightarrow{\text{Mosco}}\quad
\mathcal G_\infty(v)=\int_0^\pi |v'(\theta)|^2\sin^2\theta\,d\theta.
\] Then automatically \[
\frac{\varepsilon_{1,\lambda}-\varepsilon_{0,\lambda}}
{|\varepsilon_{0,\lambda}|}
\to 3.
\] --- # 1. Anti-circularity warning Use \(r_k=u_k/u_0\) as a diagnostic, not as the main definition of the coordinate. For the proof, the coordinate \(\theta\in[0,\pi]\) must come from the prolate/geometric scaling model, not from \(r_1\). If \(\theta=\arccos(r_1/2)\) is defined, there is a risk of hiding the first eigenvalue inside the coordinate. In the paper it is best to say: > The coordinate \(\theta\) is the prolate edge coordinate supplied by the Slepian–Pollak/CCM model. The observed identity \(u_k/u_0\sim U_k(\cos\theta)\) is a posteriori validation, not the definition of \(\theta\). --- # 2. Ground-state transform Let \(u_\lambda=u_{0,\lambda}>0\), normalized, and \[
A_\lambda u_\lambda=\varepsilon_{0,\lambda}u_\lambda.
\] Set \[
\alpha_\lambda:=|\varepsilon_{0,\lambda}|
\] — or, if you want to avoid the exceptional case \(\varepsilon_{0,\lambda}=0\), first use the prolate scale \(\alpha_\lambda^{\mathrm{pr}}\) and at the end prove
\[
\alpha_\lambda^{\mathrm{pr}}\sim |\varepsilon_{0,\lambda}|.
\] Define the transformed measure \[
dm_\lambda(\theta)
=
|u_\lambda(\theta)|^2\,d\theta
\] after passing to the prolate coordinate \(\theta\). The Doob form is \[
\mathcal G_\lambda(v,v)
=
\frac{
A_\lambda(u_\lambda v,u_\lambda v)
-
\varepsilon_{0,\lambda}\|u_\lambda v\|^2
}{\alpha_\lambda}.
\] Then the associated operator is \[
L_\lambda
=
\alpha_\lambda^{-1}
u_\lambda^{-1}
(A_\lambda-\varepsilon_{0,\lambda})
u_\lambda
\] on \(L^2(m_\lambda)\). By construction, \[
L_\lambda 1=0
\] and \[
\mathrm{Spec}(L_\lambda)
=
\left\{
\frac{\varepsilon_{k,\lambda}-\varepsilon_{0,\lambda}}
{\alpha_\lambda}
\right\}_{k\ge0}.
\] So closing the gap amounts to proving that \[
L_\lambda
\longrightarrow
L_\infty
=
-\frac1{\sin^2\theta}
\frac{d}{d\theta}
\left(\sin^2\theta\,\frac d{d\theta}
\right).
\] --- # 3. The limit and its spectrum The limit form is \[
\mathcal G_\infty(v,v)
=
\int_0^\pi |v'(\theta)|^2\sin^2\theta\,d\theta
\] on \[
L^2\bigl([0,\pi],\sin^2\theta\,d\theta\bigr).
\] Its operator is \[
L_\infty v
=
-\frac1{\sin^2\theta}
\partial_\theta
\bigl(\sin^2\theta\,\partial_\theta v\bigr).
\] With \(x=\cos\theta\), this becomes \[
L_\infty
=
-(1-x^2)\partial_x^2+3x\partial_x.
\] The Chebyshev polynomials of the second kind satisfy \[
(1-x^2)U_k''(x)-3xU_k'(x)+k(k+2)U_k(x)=0,
\] hence \[
L_\infty U_k(\cos\theta)=k(k+2)U_k(\cos\theta).
\] So \[
\mathrm{Spec}(L_\infty)
=
\{0,3,8,15,\dots,k(k+2),\dots\}.
\] This explains \[
\varepsilon_k/\varepsilon_0\to (k+1)^2.
\] --- # 4. Mosco criterion to be proved The transformed form has a Beurling–Deny representation \[
\mathcal G_\lambda(v,v)
=
\frac12
\iint_{[0,\pi]^2}
(v(\theta)-v(\phi))^2
\,d\eta_\lambda(\theta,\phi),
\] where \(d\eta_\lambda\) is the conductance measure transformed by \(u_\lambda\). To prove Mosco it suffices to verify the following three local moments. ## M0 — measure convergence \[
m_\lambda
\Longrightarrow
m_\infty,
\qquad
dm_\infty(\theta)=\sin^2\theta\,d\theta.
\] ## M1 — vanishing of long jumps For every \(\delta>0\), \[
\lim_{\lambda\to\infty}
\iint_{|\theta-\phi|>\delta}
d\eta_\lambda(\theta,\phi)
=
0.
\] ## M2 — convergence of the local second moment For every \(a\in C([0,\pi])\), \[
\frac12
\iint
a\!\left(\frac{\theta+\phi}{2}\right)
(\theta-\phi)^2
d\eta_\lambda(\theta,\phi)
\longrightarrow
\int_0^\pi a(\theta)\sin^2\theta\,d\theta.
\] ## M3 — control of the fourth moment \[
\iint
|\theta-\phi|^4
d\eta_\lambda(\theta,\phi)
\longrightarrow 0.
\] These conditions are exactly the "carré-du-champ" version of the statement that the Doob process converges to the radial diffusion on \(S^3\). --- # 5. Mosco theorem **Theorem.** If M0–M3 hold, then \[
\mathcal G_\lambda
\overset{\mathrm{Mosco}}{\longrightarrow}
\mathcal G_\infty
\] in the sense of closed forms on the spaces \(L^2(m_\lambda)\to L^2(m_\infty)\). ## Proof For \(v\in C^2([0,\pi])\), \[
v(\theta)-v(\phi)
=
v'\!\left(\frac{\theta+\phi}{2}\right)(\theta-\phi)
+
O(|\theta-\phi|^2).
\] Hence \[
(v(\theta)-v(\phi))^2
=
v'\!\left(\frac{\theta+\phi}{2}\right)^2
(\theta-\phi)^2
+
O(|\theta-\phi|^4).
\] Using M2 and M3, \[
\mathcal G_\lambda(v,v)
\to
\int_0^\pi |v'(\theta)|^2\sin^2\theta\,d\theta
=
\mathcal G_\infty(v,v).
\] This gives the limsup condition on a core. By density of \(C^2\) in the domain of \(\mathcal G_\infty\), recovery is obtained for every \(v\in D(\mathcal G_\infty)\). For the liminf, M1–M3 are precisely the hypotheses of the Bourgain–Brezis–Mironescu/Ponce/Mosco nonlocal-to-local theorem for symmetric forms. If \(v_\lambda\rightharpoonup v\) weakly and \[
\sup_\lambda\mathcal G_\lambda(v_\lambda,v_\lambda)<\infty,
\] then \(v\in H^1_{\mathrm{loc}}(0,\pi)\) and \[
\liminf_{\lambda\to\infty}
\mathcal G_\lambda(v_\lambda,v_\lambda)
\ge
\int_0^\pi |v'|^2\sin^2\theta\,d\theta.
\] Therefore there is Mosco convergence. ∎ --- # 6. Spectral consequence Mosco convergence plus compactness of the interval implies strong resolvent convergence. Moreover, since the limit form has a compact resolvent and the conditions M1–M3 give uniform compactness of sublevels, there is convergence of isolated eigenvalues: \[
\lambda_k(L_\lambda)\to \lambda_k(L_\infty)=k(k+2).
\] In particular, \[
\frac{\varepsilon_{1,\lambda}-\varepsilon_{0,\lambda}}
{|\varepsilon_{0,\lambda}|}
=
\lambda_1(L_\lambda)
\to
3.
\] Thus it closes \[
\boxed{
\liminf_{\lambda\to\infty}
\frac{\varepsilon_1(\lambda)-\varepsilon_0(\lambda)}
{|\varepsilon_0(\lambda)|}
\ge 3>0.
}
\] This closes 2.3 once M0–M3 are verified. --- # 7. How to verify M0–M3 in your model The key identity is the ground-state transform formula for jump forms: \[
A_\lambda(u_\lambda v,u_\lambda v)
-
\varepsilon_{0,\lambda}\|u_\lambda v\|^2
=
\frac12
\iint
u_\lambda(\theta)u_\lambda(\phi)
(v(\theta)-v(\phi))^2
\,dJ_\lambda(\theta,\phi),
\] where \(J_\lambda\) is the Beurling–Deny jump measure of the original carré-du-champ. Hence \[
d\eta_\lambda(\theta,\phi)
=
\alpha_\lambda^{-1}
u_\lambda(\theta)u_\lambda(\phi)
\,dJ_\lambda(\theta,\phi).
\] So M0–M3 are explicit statements about moments of \(d\eta_\lambda\). The practical proof should go as follows: 1. **M0:** prove \[ |u_\lambda(\theta)|^2\,d\theta \Rightarrow \sin^2\theta\,d\theta. \] 2. **M1:** prove that the transformed conductance mass outside \(|\theta-\phi|<\delta\) vanishes. 3. **M2:** prove \[ \frac12 \iint a\!\left(\frac{\theta+\phi}{2}\right) (\theta-\phi)^2 d\eta_\lambda \to \int a(\theta)\sin^2\theta\,d\theta. \] 4. **M3:** prove that the fourth moment tends to zero. The important point: this uses only low moments of the transformed kernel. The Kronecker recurrence that destroyed the operator norm lives at high frequencies; M0–M3 are smoothed/local statements. That is why this route avoids O11. --- # 8. Exact numerical test for M0–M3 Before writing the long proof, it is worth adding three diagnostics to the engine. For bins \(B\subset[0,\pi]\), compute \[
M_{2,\lambda}(B)
=
\frac12
\iint_{\frac{\theta+\phi}{2}\in B}
(\theta-\phi)^2\,d\eta_\lambda(\theta,\phi).
\] It must hold that \[
M_{2,\lambda}(B)
\approx
\int_B \sin^2\theta\,d\theta.
\] Also compute \[
M_{4,\lambda}
=
\iint|\theta-\phi|^4\,d\eta_\lambda(\theta,\phi)
\] and \[
R_{\delta,\lambda}
=
\iint_{|\theta-\phi|>\delta}d\eta_\lambda.
\] They must tend to \[
M_{4,\lambda}\to0,
\qquad
R_{\delta,\lambda}\to0.
\] If these three tests pass, Mosco is practically proved. --- # 9. Consequence for 3.2 Once 2.3 is proved, the uniform gap stabilizes the spectral projection of the ground state. Then the normalized family \[
\widehat u_{0,\lambda}(z)
\] cannot jump branches. Since each \(\widehat u_{0,\lambda}\) is real-rooted by CvS, any nonzero compact limit is also real-rooted by Hurwitz. Thus, \[
2.3 \Longrightarrow 3.2.
\] More precisely: Mosco gives \[
\lambda_1(L_\lambda)\to3,
\] so the projection onto the ground state is uniformly isolated; Kato gives convergence of the projections; Montel gives compact convergence of the entire transforms; Hurwitz preserves real-rootedness. --- # 10. What to insert in the paper I recommend adding a subsection: ## Step 2.3 — Doob–Mosco convergence With the following results: 1. **Lemma 2.3.1.** Ground-state transform: \[ \mathrm{Spec}(\mathcal G_\lambda) = \left\{ \frac{\varepsilon_k-\varepsilon_0}{|\varepsilon_0|} \right\}. \] 2. **Lemma 2.3.2.** Beurling–Deny representation: \[ \mathcal G_\lambda(v) = \frac12\iint(v(\theta)-v(\phi))^2d\eta_\lambda. \] 3. **Lemma 2.3.3.** Moment convergence M0–M3. 4. **Theorem 2.3.4.** Mosco convergence: \[ \mathcal G_\lambda\to\mathcal G_\infty. \] 5. **Corollary 2.3.5.** \[ \frac{\varepsilon_1-\varepsilon_0}{|\varepsilon_0|}\to3. \] --- # 11. Summary The technical closure of 2.3 is no longer "identify eigenvectors". It is proving the three moments of the transformed carré-du-champ: \[
\boxed{
\text{M0 measure}
\quad+\quad
\text{M1 locality}
\quad+\quad
\text{M2 second moment}
\quad+\quad
\text{M3 fourth moment}
}
\] That gives Mosco, and Mosco gives the gap: \[
\boxed{
\mathcal G_\lambda
\overset{\mathrm{Mosco}}{\longrightarrow}
\int_0^\pi |v'|^2\sin^2\theta\,d\theta
\Longrightarrow
\frac{\varepsilon_1-\varepsilon_0}{|\varepsilon_0|}
\to3.
}
\] This is the clean, RH-neutral path, and it avoids exactly the Kronecker/norm-resolvent obstacle.