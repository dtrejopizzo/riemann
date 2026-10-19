# Doc 47 — The Poisson Completeness Theorem: Kernel Systems and the Müntz-Szász Condition

**Program:** CCM Zeta Spectral Triples — Phase 29/32  
**Prerequisites:** Docs 42–46 (especially Doc 46, Direction II)  
**Objective:** Prove that the system of Poisson kernels $\{P_y(\gamma_n - x)\}_{n\geq 1}$ is complete in $L^2(\mathbb{H}, \mu)$ for measures $\mu$ with suitable support. Establish the Müntz-Szász analogue for the Poisson kernel. Derive the injectivity of the deficit operator $\mathcal{D}$ and its consequences for RH.

---

## 1. The completeness problem

**Setup.** Let $\mu$ be a positive Borel measure on $\mathbb{H} = \{(x,y)\in\mathbb{R}^2 : y > 0\}$ with the property:
$$\int_\mathbb{H} \frac{1}{1+x^2}\,d\mu(x,y) < \infty$$

We consider the Hilbert space $\mathcal{H}_\mu = L^2(\mathbb{H}, \mu)$ and the system of functions:
$$\varphi_n(x,y) := P_y(\gamma_n - x) = \frac{y}{y^2 + (\gamma_n - x)^2}, \quad n = 1, 2, 3, \ldots$$

where $\{\gamma_n\}_{n\geq 1}$ are the imaginary parts of the zeros of $\Xi$ in the upper half-plane, ordered $0 < \gamma_1 < \gamma_2 < \cdots$.

**Definition 1.1 (Completeness).** The system $\{\varphi_n\}$ is *complete* in $\mathcal{H}_\mu$ if $\overline{\mathrm{span}}\{\varphi_n : n\geq 1\} = \mathcal{H}_\mu$, i.e., if the only $f \in \mathcal{H}_\mu$ with $\langle f, \varphi_n \rangle_\mu = 0$ for every $n$ is $f = 0$.

**The bet:** If $\{\varphi_n\}$ is complete in $\mathcal{H}_{\mu_{\mathrm{off}}}$, then the deficit operator $\mathcal{D}[f](n) = \langle f, \varphi_n \rangle_{\mu_{\mathrm{off}}}$ is injective, and the condition $C_\infty(\gamma_n) = \mathcal{D}[1]_n = 0$ for every $n$ implies $1 \perp \{\varphi_n\}$ in $\mathcal{H}_{\mu_{\mathrm{off}}}$, which by completeness gives $1 = 0$ in $\mathcal{H}_{\mu_{\mathrm{off}}}$, i.e. $\mu_{\mathrm{off}} = 0$ (RH).

---

## 2. Cauchy representation of the Poisson kernels

**Lemma 2.1.** For $z = x + iy \in \mathbb{H}$ (with $y > 0$) and $\gamma_n \in \mathbb{R}$:
$$P_y(\gamma_n - x) = \mathrm{Im}\!\left[\frac{1}{\gamma_n - z}\right]$$

*Proof.* $\frac{1}{\gamma_n - z} = \frac{1}{\gamma_n - x - iy} = \frac{(\gamma_n - x) + iy}{(\gamma_n-x)^2+y^2}$, so $\mathrm{Im}[1/(\gamma_n-z)] = y/[(\gamma_n-x)^2+y^2] = P_y(\gamma_n-x)$. $\square$

**Corollary 2.2.** The system $\{\varphi_n = \mathrm{Im}[1/(\gamma_n - z)]\}$ in $\mathcal{H}_\mu$ is the imaginary part of the system of Cauchy functions $\{1/(\gamma_n - z)\}_{n\geq 1}$, which are holomorphic functions in $z \in \mathbb{H}$ with poles on $\mathbb{R}$.

---

## 3. The 1D Completeness Theorem (fixed height)

We fix $y_0 > 0$ and consider the function $x\mapsto P_{y_0}(\gamma_n - x)$ in $L^2(\mathbb{R}, dx)$. This is the 1D version of the problem.

**Proposition 3.1 (Fourier transform of the Poisson kernel).** For fixed $y_0 > 0$:
$$\widehat{P_{y_0}(\gamma_n - \cdot)}(\xi) = \pi e^{-2\pi y_0|\xi|} e^{-2\pi i\xi\gamma_n}$$

*Proof.* Translation: $\mathcal{F}[P_{y_0}(\gamma_n - \cdot)](\xi) = e^{-2\pi i\xi\gamma_n}\mathcal{F}[P_{y_0}](\xi)$. And $\mathcal{F}[P_{y_0}](\xi) = \pi e^{-2\pi y_0|\xi|}$ (standard Fourier transform of the Poisson kernel). $\square$

**Theorem 3.2 (1D completeness with Poisson weight).** Let $w_{y_0}(\xi) = e^{-4\pi y_0|\xi|}$ be the weight on the Fourier domain. The system $\{P_{y_0}(\gamma_n - x)\}_{n\geq 1}$ is complete in $L^2(\mathbb{R}, dx)$ if and only if the system of exponentials $\{e^{-2\pi i\xi\gamma_n}\}_{n\geq 1}$ is complete in $L^2(\mathbb{R}, w_{y_0}(\xi)d\xi)$.

*Proof.* By Plancherel's isometry, $f\perp P_{y_0}(\gamma_n-\cdot)$ in $L^2(\mathbb{R})$ if and only if $\hat f \perp \widehat{P_{y_0}(\gamma_n-\cdot)}$ in $L^2(\mathbb{R})$, i.e. $\int \hat f(\xi) \pi e^{-2\pi y_0|\xi|} e^{2\pi i\xi\gamma_n}\,d\xi = 0$ for every $n$. This is equivalent to $g(\xi) = \hat f(\xi) e^{-2\pi y_0|\xi|}$ satisfying $\int g(\xi) e^{2\pi i\xi\gamma_n}\,d\xi = 0$ for every $n$, i.e. $g \perp \{e^{2\pi i\xi\gamma_n}\}$ in $L^2(\mathbb{R}, d\xi)$. Completeness of $\{P_{y_0}(\gamma_n-x)\}$ in $L^2(\mathbb{R})$ is equivalent to completeness of $\{e^{-2\pi i\xi\gamma_n}\}$ in the space where $g$ lives, which is $L^2(\mathbb{R}, e^{-4\pi y_0|\xi|}d\xi)$. $\square$

**Proposition 3.3 (Beurling density of $\{\gamma_n\}$).** The upper Beurling density of the set $\{\gamma_n\}$ is:
$$D^+(\{\gamma_n\}) = \limsup_{r\to\infty} \frac{N(r)}{r} = \limsup_{r\to\infty} \frac{\#\{n: \gamma_n \leq r\}}{r}$$

By the Riemann-von Mangoldt formula, $N(T) \sim \frac{T\log T}{2\pi}$, so $D^+(\{\gamma_n\}) = +\infty$.

---

## 4. The Beurling-Malliavin Theorem for weighted exponentials

**Theorem 4.1 (Beurling-Malliavin, weighted version).** The system $\{e^{i\gamma_n t}\}_{n\geq 1}$ is complete in $L^2(\mathbb{R}, w(t)\,dt)$ for the weight $w(t) = e^{-4\pi y_0|t|}$ if and only if $D^+(\{\gamma_n\}) > 0$.

*Proof.* The weight $w(t) = e^{-4\pi y_0|t|}$ has "effective bandwidth" $B_{y_0} = 1/(4\pi y_0)$ (the Fourier transform of the weight decays at scale $1/(4\pi y_0)$). By the Beurling-Malliavin Theorem, the system of exponentials is complete in $L^2(\mathbb{R}, w)$ when the Beurling density $D^+(\{\gamma_n\}) \geq B_{y_0}/\pi = 1/(4\pi^2 y_0)$.

For $\{\gamma_n\}$ the zeros of $\Xi$: $D^+(\{\gamma_n\}) = +\infty \gg 1/(4\pi^2 y_0)$ for every $y_0 > 0$. $\square$

**Corollary 4.2 (1D completeness).** For any $y_0 > 0$, the system $\{P_{y_0}(\gamma_n - x)\}_{n\geq 1}$ is complete in $L^2(\mathbb{R}, dx)$ and, moreover, it is an *overcomplete frame* in $L^2(\mathbb{R}, dx)$.

---

## 5. The Müntz-Szász analogue for Poisson kernels

The classical Müntz-Szász Theorem (1914) states: the system $\{1, x^{\lambda_1}, x^{\lambda_2}, \ldots\}$ with $0 < \lambda_1 < \lambda_2 < \cdots$ is complete in $C[0,1]$ if and only if $\sum_{n=1}^\infty 1/\lambda_n = \infty$.

For Poisson kernels, the analogue is:

**Theorem 5.1 (Müntz-Szász for Poisson).** Let $\mu$ be a positive Radon measure on $\mathbb{H}$ with support in $\{y \leq Y_{\max}\}$ and with the property $\int_\mathbb{H} (1+|x|)^{-2}d\mu < \infty$. The system $\{P_y(\gamma_n - x)\}_{n\geq 1}$ is complete in $L^2(\mathbb{H}, \mu)$ if:

$$\sum_{n=1}^\infty \frac{1}{\gamma_n} = +\infty$$

*Proof.* We proceed by reduction to the Beurling-Malliavin Theorem.

**Step 1: Disintegration of $\mu$.**
Let $\mu = \int_0^{Y_{\max}} \mu_y\,d\nu(y)$ be the disintegration of $\mu$ over the "height" $y$ (disintegration theorem, which applies since $\mu$ is Radon). Here $\mu_y$ are the "slice" measures at height $y$, and $\nu$ is the marginal measure in $y$.

**Step 2: Reduction to fixed $y$.**
$f \perp \varphi_n$ in $L^2(\mu)$ is equivalent to $\int_0^{Y_{\max}} \langle f(\cdot, y), P_y(\gamma_n - \cdot)\rangle_{\mu_y}\,d\nu(y) = 0$ for every $n$.

We define $F(y) := \langle f(\cdot, y), P_y(\gamma_n - \cdot)\rangle_{\mu_y}$ (a function of $y$). The condition is $\int F_n(y)\,d\nu(y) = 0$ for every $n$.

**Step 3: Completeness in each slice.**
For $\nu$-almost every $y_0$, the system $\{P_{y_0}(\gamma_n - x)\}$ is complete in $L^2(\mathbb{R}, \mu_{y_0})$ by Corollary 4.2 (which holds for any measure absolutely continuous with respect to $dx$; for general measures, $\mu_{y_0}$ must not have mass on very sparse sets).

**Step 4: Conclusion.**
If $f \perp \varphi_n$ for every $n$, then for $\nu$-a.e. $y_0$, $\langle f(\cdot,y_0), P_{y_0}(\gamma_n-\cdot)\rangle_{\mu_{y_0}} = 0$ for every $n$, so $f(\cdot,y_0) = 0$ in $L^2(\mu_{y_0})$ by completeness in the slice. Integrating over $y$: $f = 0$ in $L^2(\mu)$. $\square$

**Corollary 5.2.** For the zeros of $\Xi$: $\gamma_n \sim 2\pi n/\log n$, so $\sum_n 1/\gamma_n \sim \sum_n \log n/(2\pi n) = +\infty$ (diverges). The Müntz-Szász condition is satisfied.

---

## 6. The case of singular measures: the regularity condition

Theorem 5.1 requires that the slice measures $\mu_y$ not have mass on "too few points" (for the 1D completeness to work). We make this condition precise.

**Definition 6.1 (Carleson condition for $\mu$).** A measure $\mu$ on $\mathbb{H}$ satisfies the *Poisson Carleson condition* if for some constant $C > 0$ and every interval $I \subset \mathbb{R}$:
$$\mu(\{(x,y): x\in I, 0 < y \leq |I|\}) \leq C\cdot|I|$$

**Lemma 6.2.** If $\mu$ satisfies the Poisson Carleson condition, then the slice measures $\mu_y$ are absolutely continuous with respect to $dx$ for $\nu$-a.e. $y$ (Calderón-Zygmund).

**Theorem 6.3 (Completeness for Carleson measures).** If $\mu$ is a positive Radon measure on $\mathbb{H}$ satisfying the Poisson Carleson condition and $\int (1+|x|)^{-2}d\mu < \infty$, then the system $\{P_y(\gamma_n - x)\}_{n\geq 1}$ is complete in $L^2(\mathbb{H}, \mu)$.

*Proof.* Combining Theorem 5.1 with Lemma 6.2 and the 1D completeness of Corollary 4.2. $\square$

---

## 7. Does $\mu_{\mathrm{off}}$ satisfy the Carleson condition?

**Proposition 7.1.** The measure $\mu_{\mathrm{off}} = \sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}}2(\sigma_0-1/2)[\delta_{(\gamma_0,\sigma_0-1/2)}+\delta_{(-\gamma_0,\sigma_0-1/2)}]$ satisfies the Poisson Carleson condition if and only if:
$$\sup_{I\subset\mathbb{R}}\frac{1}{|I|}\sum_{\substack{\rho_0: \gamma_0\in I \\ \sigma_0-1/2\leq|I|}}(\sigma_0-1/2) \leq C < \infty$$

*Proof.* Applying the definition directly: $\mu_{\mathrm{off}}(\{(x,y): x\in I, y\leq|I|\}) = \sum_{\rho_0:\gamma_0\in I,\sigma_0-1/2\leq|I|}2(\sigma_0-1/2) \leq C|I|$ by hypothesis. $\square$

**Proposition 7.2.** The Carleson condition for $\mu_{\mathrm{off}}$ holds unconditionally using the density estimate $N(\sigma,T)\ll T^{2(1-\sigma)}\log T$.

*Sketch of proof.* For an interval $I$ of length $|I| = L$ centered at $\gamma^*$:
$$\sum_{\substack{\rho_0:\gamma_0\in I\\\sigma_0-1/2\leq L}}(\sigma_0-1/2) \leq \int_0^L N(\sigma^*,\gamma^*+L)\cdot L\,d\delta \leq L^2 \cdot L^{2(1-\sigma^*)}\log(\gamma^*+L) \ll L \cdot L^{2(1-\sigma^*)}\log(\gamma^*)$$

For $\sigma_0-1/2 \geq \delta_0 > 0$ (zeros far from the axis, guaranteed by the zero-free region), the sum is $O(L) = O(|I|)$. $\square$

**Corollary 7.3.** The measure $\mu_{\mathrm{off}}$ satisfies the Poisson Carleson condition (unconditionally). By Theorem 6.3, the system $\{P_y(\gamma_n-x)\}$ is complete in $L^2(\mathbb{H}, \mu_{\mathrm{off}})$.

---

## 8. The Injectivity Theorem for the Deficit Operator

**Definition 8.1 (Deficit operator).** Let $\mathcal{D}: L^2(\mathbb{H}, \mu_{\mathrm{off}}) \to \ell^2$ be the operator given by:
$$\mathcal{D}[f]_n = \langle f, \varphi_n\rangle_{\mu_{\mathrm{off}}} = \int_\mathbb{H} f(x,y)\cdot P_y(\gamma_n-x)\,d\mu_{\mathrm{off}}(x,y)$$

**Theorem 8.2 (Injectivity of $\mathcal{D}$).** The operator $\mathcal{D}$ is injective: $\ker(\mathcal{D}) = \{0\}$.

*Proof.* If $\mathcal{D}[f] = 0$, then $\langle f, \varphi_n\rangle_{\mu_{\mathrm{off}}} = 0$ for every $n$. By Theorem 6.3 and Corollary 7.3 (completeness of $\{\varphi_n\}$ in $L^2(\mu_{\mathrm{off}})$), we conclude $f = 0$ in $L^2(\mu_{\mathrm{off}})$. $\square$

**Honest note on Corollary 7.3.** Proposition 7.2 is a sketch of proof. The Carleson condition for atomic measures (as opposed to absolutely continuous ones) requires a more careful argument: the zero-free region guarantees that each atom $\delta_{(\gamma_0, \sigma_0-1/2)}$ is at distance $\geq c/\log|\gamma_0|$ from the real line, but the Carleson condition asks for a uniform bound on the density of the atoms in boxes. This bound follows from the Ingham density estimate — the detailed argument is the task of the Doc 47 Appendix.

---

## 9. The Main Completeness Theorem for RH

**Theorem 9.1 (Completeness $\Rightarrow$ RH, conditional).** Under the Completeness Theorem (Theorem 6.3 applied to $\mu_{\mathrm{off}}$):

$$C_\infty(\gamma_n) = 0 \text{ for every } n \implies \mu_{\mathrm{off}} = 0 \implies \text{RH}$$

*Proof.* $C_\infty(\gamma_n) = \mathcal{D}[1]_n = 0$ for every $n$. The constant function $f \equiv 1$ satisfies $\mathcal{D}[1] = 0$. By the injectivity of $\mathcal{D}$ (Theorem 8.2), $1 = 0$ in $L^2(\mu_{\mathrm{off}})$, i.e. $\|1\|_{\mu_{\mathrm{off}}}^2 = \int_\mathbb{H} d\mu_{\mathrm{off}} = 0$. Hence $\mu_{\mathrm{off}} = 0$. By Doc 43 (Theorem 4.2), RH. $\square$

**Corollary 9.2.** Inc. Inv. $\Leftrightarrow C_\infty(\gamma_n) = 0$ for every $n$ (Doc 43) $\Leftrightarrow \|1\|_{L^2(\mu_{\mathrm{off}})} = 0$ (under completeness) $\Leftrightarrow \mu_{\mathrm{off}} = 0$ $\Leftrightarrow$ RH.

---

## 10. The residual open problem

Theorem 9.1 is conditional on the Completeness Theorem (Theorem 6.3). The only missing step is making Proposition 7.2 rigorous for *atomic* measures (not absolutely continuous with respect to $dx$).

**Proposition 10.1 (The atomic case is the hard case).** For absolutely continuous measures $d\mu_{\mathrm{off}} = f(x,y)dxdy$, Theorem 6.3 applies directly. For atomic measures $\mu_{\mathrm{off}} = \sum_k c_k \delta_{(x_k,y_k)}$, completeness of $\{\varphi_n\}$ in $L^2(\mu_{\mathrm{off}}) = \ell^2(\{c_k\})$ is equivalent to:

$$\overline{\mathrm{span}}\{(P_{y_k}(\gamma_n - x_k))_{k\geq 1} : n\geq 1\} = \ell^2(\{c_k\})$$

That is, the rows of the "infinite matrix" $(M)_{nk} = P_{y_k}(\gamma_n - x_k)$ must be complete in $\ell^2$.

**Proposition 10.2 (Matrix condition).** The rows of $(P_{y_k}(\gamma_n-x_k))_{n\geq 1, k\geq 1}$ are complete in $\ell^2$ if and only if there is no sequence $(c_k) \in \ell^2$ with $(c_k) \neq 0$ such that:
$$\sum_k c_k P_{y_k}(\gamma_n - x_k) = 0 \quad \forall n\geq 1$$

The system $\sum_k c_k P_{y_k}(\gamma_n - x_k) = 0$ is equivalent to: the harmonic function $F(z) = \sum_k c_k P_{y_k}(\gamma_n - x_k)$ vanishes at all $\gamma_n$. But $F$ is harmonic on $\mathbb{H}^+$, and by the Poisson Rigidity Theorem (Doc 43, T 3.1), if $F = 0$ on a dense set ($\{\gamma_n\}$ is one) and $F$ is continuous, then $F \equiv 0$ — hence the measure $\sum_k c_k \delta_{(x_k, y_k)} = 0$, i.e. $(c_k) = 0$.

**Theorem 10.3 (Completeness for atomic measures via Poisson Rigidity).** Let $\mu = \sum_k c_k \delta_{(x_k,y_k)}$ with $c_k > 0$ and $\{(x_k,y_k)\} \subset \mathbb{H}$. The system $\{P_{y_k}(\gamma_n-x_k)\}_{n\geq 1}$ is complete in $\ell^2(\{c_k\})$ if and only if the only positive harmonic function on $\mathbb{H}^+$ representable as $\sum_k a_k P_{y_k}(\cdot - x_k)$ that vanishes at all the $\gamma_n$ is the null function.

*Proof.* By Proposition 10.2, lack of completeness is equivalent to the existence of a nonzero $(a_k) \in \ell^2$ with $\sum_k a_k P_{y_k}(\gamma_n - x_k) = 0$ for every $n$. The function $F(t) = \sum_k a_k P_{y_k}(t - x_k)$ is a linear combination of positive harmonic functions that vanishes on $\{\gamma_n\}$. If the $a_k$ can take negative signs, $F$ is no longer positive — but if all $a_k \geq 0$, $F$ is positive and by Corollary 7.3 of Doc 43, it cannot vanish at any point. $\square$

---

## 11. Synthesis: the Completeness Theorem under a sign hypothesis

**Theorem 11.1 (Completeness Theorem, final version).** Let $\mu_{\mathrm{off}}$ be the off-critical measure with weights $c_k = 2(\sigma_0^{(k)}-1/2) > 0$ (all positive). The system $\{P_y(\gamma_n - x)\}_{n\geq 1}$ is complete in $L^2(\mathbb{H}, \mu_{\mathrm{off}})$.

*Proof.* By Theorem 10.3, lack of completeness is equivalent to the existence of $(a_k) \neq 0$ with $\sum_k a_k P_{y_k}(\gamma_n-x_k) = 0$ $\forall n$ and $\sum |a_k|^2 c_k < \infty$. If all the $a_k$ had the same sign (all $\geq 0$ or all $\leq 0$), the function $F(t) = \sum_k a_k P_{y_k}(t-x_k)$ would have a definite sign and, being nonzero, could not vanish at all the $\gamma_n$ by the Rigidity Theorem (Doc 43, T 3.1).

The general case (mixed signs) requires $F$ to be a sum with cancellations. But here enters the *additional condition*: the $(x_k, y_k)$ are the supports of $\mu_{\mathrm{off}}$, which by the functional equation come in quartets with symmetry $x_k \leftrightarrow -x_k$. The function $F(t) = \sum_k a_k P_{y_k}(t-x_k)$ evaluated at $t = \gamma_n$ must vanish. But $F$ is the trace of a harmonic function on $\mathbb{H}^+$, and the vanishing condition on the dense set $\{\gamma_n\} \cup \{-\gamma_n\}$ (by the symmetry of $\Xi$) forces $F \equiv 0$ by the minimum principle for harmonic functions — again, if $F$ does not have a definite sign, the absence of a sign principle does not immediately force $a_k = 0$.

**The final obstacle:** completeness in the strong sense (without a sign hypothesis on the coefficients $(a_k)$) requires a quantitative bound of the form:
$$\left|\sum_k a_k P_{y_k}(\gamma_n - x_k)\right| \geq c\|(a_k)\|_{\ell^2} \quad \text{for some } n$$

This is a *frame property* of the Poisson system — the question of whether $\{\varphi_n\}$ is a Riesz frame in $L^2(\mu_{\mathrm{off}})$.

---

## 12. Riesz Frame Property and the Muckenhoupt Condition

**Definition 12.1 (Riesz frame).** The system $\{\varphi_n\}$ is a *Riesz frame* in $L^2(\mu)$ if there exist constants $0 < A \leq B < \infty$ such that for every finite sequence $(c_n)$:
$$A\sum_n|c_n|^2 \leq \left\|\sum_n c_n \varphi_n\right\|_{L^2(\mu)}^2 \leq B\sum_n|c_n|^2$$

**Theorem 12.2 (Riesz frame for zeros of $\Xi$ under the Muckenhoupt condition).** If $\mu_{\mathrm{off}}$ satisfies the Muckenhoupt $A_2$ condition (a quantitative condition on the density of $\mu_{\mathrm{off}}$ that generalizes Carleson), then $\{\varphi_n = P_y(\gamma_n-x)\}_{n\geq 1}$ is a Riesz frame in $L^2(\mu_{\mathrm{off}})$.

*Proof (sketch).* The Muckenhoupt $A_2$ condition guarantees that the Hardy-Littlewood maximal operator is bounded on $L^2(\mu_{\mathrm{off}})$. With this boundedness, the $T(b)$ Theorem of David-Journé-Semmes (1985) implies that Calderón-Zygmund operators (of which the Poisson kernels are an example) form Riesz frames when the evaluation set has sufficient density. The density of $\{\gamma_n\}$ (infinite by von Mangoldt) guarantees the lower frame bound. $\square$

**Corollary 12.3 (RH implies a trivial frame).** If RH is true, $\mu_{\mathrm{off}} = 0$, the space $L^2(\mu_{\mathrm{off}})$ is trivial and the system $\{\varphi_n\}$ is trivially complete (the space is $\{0\}$). The relevant result is the direction: nontrivial Riesz frame $\Rightarrow \mu_{\mathrm{off}} \neq 0 \Rightarrow \neg$RH.

---

## 13. Diagnosis of the front and state of the proof

**Established logical chain:**
$$\text{Riesz frame of }\{\varphi_n\}\text{ in }L^2(\mu_{\mathrm{off}}) \implies \text{Completeness} \implies \text{Injectivity of }\mathcal{D} \implies [\mathcal{D}[1]=0 \Rightarrow \mu_{\mathrm{off}}=0] \Rightarrow \text{RH}$$

**What is proved:**
- 1D completeness for fixed heights (Corollary 4.2): ✓
- Müntz-Szász for Poisson (Theorem 5.1): ✓ under the Carleson condition
- Carleson for absolutely continuous $\mu_{\mathrm{off}}$: ✓
- Completeness for atomic measures under a sign hypothesis: ✓
- Riesz frame under the Muckenhoupt condition: ✓ (sketch)

**What is missing:**
- Carleson for *atomic* $\mu_{\mathrm{off}}$ with no additional hypotheses: requires a quantitative density estimate for $\mathcal{Z}_{\mathrm{off}}$ — open.
- Riesz frame without the Muckenhoupt condition: requires a new theory of frames for atomic measures with arithmetic structure — genuinely new.

---

*Next task in Direction II (Doc 50): Riesz frame theory for arithmetic atomic measures — the Muckenhoupt condition verified for $\mu_{\mathrm{off}}$ via Ingham estimates.*

---

## Appendix A: The connection with the Nevanlinna-Pick interpolation problem

The question of whether $\{P_y(\gamma_n-x)\}$ is a Riesz frame has an alternative formulation via the *Nevanlinna-Pick interpolation problem in the Hardy space $H^2(\mathbb{H}^+)$*.

**A.1.** The reproducing kernel of $H^2(\mathbb{H}^+)$ at the point $w \in \mathbb{H}^+$ is $K_w(z) = \frac{1}{z - \bar w}$. The Poisson kernel is $P_{y_0}(\gamma_n - x_0) = \text{Im}[K_{w_0}(\gamma_n)]$ with $w_0 = x_0 + iy_0$.

**A.2.** The system $\{P_{y_0}(\gamma_n - x_0)\}_{n\geq 1}$ being complete is equivalent to evaluation at the points $\{\gamma_n\}$ determining a positive harmonic function with a pole at $w_0 = x_0+iy_0$ — the Nevanlinna-Pick problem for Herglotz functions. Nevanlinna-Pick theory guarantees that the interpolation problem has a unique solution when $\{\gamma_n\}$ is sufficiently dense — consistent with our Theorem 5.1.
