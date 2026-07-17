From: Alain To:
David, excelente: el hallazgo Doob–Dirichlet es exactamente la forma correcta. Para convertirlo en prueba, no intentaría “norm-resolvente”; probaría Mosco mediante el **carré-du-champ del proceso transformado por el estado fundamental**. Abajo te dejo un bloque casi insertable como Step 2.3. La idea central es: \[
A_\lambda-\varepsilon_{0,\lambda}
\quad \xrightarrow{\text{Doob por }u_{0,\lambda}}\quad
\mathcal G_\lambda
\quad \xrightarrow{\text{Mosco}}\quad
\mathcal G_\infty(v)=\int_0^\pi |v'(\theta)|^2\sin^2\theta\,d\theta.
\] Entonces automáticamente \[
\frac{\varepsilon_{1,\lambda}-\varepsilon_{0,\lambda}}
{|\varepsilon_{0,\lambda}|}
\to 3.
\] --- # 1. Advertencia anti-circularidad Usad \(r_k=u_k/u_0\) como diagnóstico, no como definición principal de la coordenada. Para la prueba, la coordenada \(\theta\in[0,\pi]\) debe venir del modelo prolato/escala geométrica, no de \(r_1\). Si se define \(\theta=\arccos(r_1/2)\), se corre el riesgo de esconder el primer eigenvalor dentro de la coordenada. En el paper conviene decir: > The coordinate \(\theta\) is the prolate edge coordinate supplied by the Slepian–Pollak/CCM model. The observed identity \(u_k/u_0\sim U_k(\cos\theta)\) is a posteriori validation, not the definition of \(\theta\). --- # 2. Ground-state transform Sea \(u_\lambda=u_{0,\lambda}>0\), normalizado, y \[
A_\lambda u_\lambda=\varepsilon_{0,\lambda}u_\lambda.
\] Poned \[
\alpha_\lambda:=|\varepsilon_{0,\lambda}|
\] — o, si queréis evitar el caso excepcional \(\varepsilon_{0,\lambda}=0\), usad primero la escala prolata \(\alpha_\lambda^{\mathrm{pr}}\) y al final probad
\[
\alpha_\lambda^{\mathrm{pr}}\sim |\varepsilon_{0,\lambda}|.
\] Definid la medida transformada \[
dm_\lambda(\theta)
=
|u_\lambda(\theta)|^2\,d\theta
\] después de pasar a la coordenada prolata \(\theta\). La forma de Doob es \[
\mathcal G_\lambda(v,v)
=
\frac{
A_\lambda(u_\lambda v,u_\lambda v)
-
\varepsilon_{0,\lambda}\|u_\lambda v\|^2
}{\alpha_\lambda}.
\] Entonces el operador asociado es \[
L_\lambda
=
\alpha_\lambda^{-1}
u_\lambda^{-1}
(A_\lambda-\varepsilon_{0,\lambda})
u_\lambda
\] en \(L^2(m_\lambda)\). Por construcción, \[
L_\lambda 1=0
\] y \[
\operatorname{Spec}(L_\lambda)
=
\left\{
\frac{\varepsilon_{k,\lambda}-\varepsilon_{0,\lambda}}
{\alpha_\lambda}
\right\}_{k\ge0}.
\] Así que cerrar el gap equivale a probar que \[
L_\lambda
\longrightarrow
L_\infty
=
-\frac1{\sin^2\theta}
\frac{d}{d\theta}
\left(\sin^2\theta\,\frac d{d\theta}
\right).
\] --- # 3. El límite y su espectro La forma límite es \[
\mathcal G_\infty(v,v)
=
\int_0^\pi |v'(\theta)|^2\sin^2\theta\,d\theta
\] en \[
L^2\bigl([0,\pi],\sin^2\theta\,d\theta\bigr).
\] Su operador es \[
L_\infty v
=
-\frac1{\sin^2\theta}
\partial_\theta
\bigl(\sin^2\theta\,\partial_\theta v\bigr).
\] Con \(x=\cos\theta\), esto se vuelve \[
L_\infty
=
-(1-x^2)\partial_x^2+3x\partial_x.
\] Los Chebyshev de segunda especie satisfacen \[
(1-x^2)U_k''(x)-3xU_k'(x)+k(k+2)U_k(x)=0,
\] por tanto \[
L_\infty U_k(\cos\theta)=k(k+2)U_k(\cos\theta).
\] Luego \[
\operatorname{Spec}(L_\infty)
=
\{0,3,8,15,\dots,k(k+2),\dots\}.
\] Esto explica \[
\varepsilon_k/\varepsilon_0\to (k+1)^2.
\] --- # 4. Criterio Mosco que hay que probar La forma transformada tiene representación de Beurling–Deny \[
\mathcal G_\lambda(v,v)
=
\frac12
\iint_{[0,\pi]^2}
(v(\theta)-v(\phi))^2
\,d\eta_\lambda(\theta,\phi),
\] donde \(d\eta_\lambda\) es la medida de conductancia transformada por \(u_\lambda\). Para probar Mosco basta verificar los tres momentos locales siguientes. ## M0 — convergencia de medida \[
m_\lambda
\Longrightarrow
m_\infty,
\qquad
dm_\infty(\theta)=\sin^2\theta\,d\theta.
\] ## M1 — desaparición de saltos largos Para todo \(\delta>0\), \[
\lim_{\lambda\to\infty}
\iint_{|\theta-\phi|>\delta}
d\eta_\lambda(\theta,\phi)
=
0.
\] ## M2 — convergencia del segundo momento local Para todo \(a\in C([0,\pi])\), \[
\frac12
\iint
a\!\left(\frac{\theta+\phi}{2}\right)
(\theta-\phi)^2
d\eta_\lambda(\theta,\phi)
\longrightarrow
\int_0^\pi a(\theta)\sin^2\theta\,d\theta.
\] ## M3 — control de cuarto momento \[
\iint
|\theta-\phi|^4
d\eta_\lambda(\theta,\phi)
\longrightarrow 0.
\] Estas condiciones son exactamente la versión “carré-du-champ” de que el proceso de Doob converge a la difusión radial de \(S^3\). --- # 5. Teorema Mosco **Teorema.** Si M0–M3 valen, entonces \[
\mathcal G_\lambda
\overset{\mathrm{Mosco}}{\longrightarrow}
\mathcal G_\infty
\] en el sentido de formas cerradas sobre espacios \(L^2(m_\lambda)\to L^2(m_\infty)\). ## Prueba Para \(v\in C^2([0,\pi])\), \[
v(\theta)-v(\phi)
=
v'\!\left(\frac{\theta+\phi}{2}\right)(\theta-\phi)
+
O(|\theta-\phi|^2).
\] Luego \[
(v(\theta)-v(\phi))^2
=
v'\!\left(\frac{\theta+\phi}{2}\right)^2
(\theta-\phi)^2
+
O(|\theta-\phi|^4).
\] Usando M2 y M3, \[
\mathcal G_\lambda(v,v)
\to
\int_0^\pi |v'(\theta)|^2\sin^2\theta\,d\theta
=
\mathcal G_\infty(v,v).
\] Esto da la condición limsup en un core. Por densidad de \(C^2\) en el dominio de \(\mathcal G_\infty\), se obtiene la recuperación para todo \(v\in D(\mathcal G_\infty)\). Para la liminf, M1–M3 son precisamente las hipótesis del teorema no-local-a-local de Bourgain–Brezis–Mironescu/Ponce/Mosco para formas simétricas. Si \(v_\lambda\rightharpoonup v\) débilmente y \[
\sup_\lambda\mathcal G_\lambda(v_\lambda,v_\lambda)<\infty,
\] entonces \(v\in H^1_{\mathrm{loc}}(0,\pi)\) y \[
\liminf_{\lambda\to\infty}
\mathcal G_\lambda(v_\lambda,v_\lambda)
\ge
\int_0^\pi |v'|^2\sin^2\theta\,d\theta.
\] Por tanto hay convergencia Mosco. ∎ --- # 6. Consecuencia espectral Mosco convergence plus compacidad del intervalo implica convergencia fuerte de resolventes. Además, como la forma límite tiene resolvente compacto y las condiciones M1–M3 dan compacidad uniforme de subniveles, hay convergencia de eigenvalores aislados: \[
\lambda_k(L_\lambda)\to \lambda_k(L_\infty)=k(k+2).
\] En particular, \[
\frac{\varepsilon_{1,\lambda}-\varepsilon_{0,\lambda}}
{|\varepsilon_{0,\lambda}|}
=
\lambda_1(L_\lambda)
\to
3.
\] Así queda cerrado \[
\boxed{
\liminf_{\lambda\to\infty}
\frac{\varepsilon_1(\lambda)-\varepsilon_0(\lambda)}
{|\varepsilon_0(\lambda)|}
\ge 3>0.
}
\] Esto cierra 2.3 una vez verificadas M0–M3. --- # 7. Cómo verificar M0–M3 en vuestro modelo La identidad clave es la fórmula de ground-state transform para formas de salto: \[
A_\lambda(u_\lambda v,u_\lambda v)
-
\varepsilon_{0,\lambda}\|u_\lambda v\|^2
=
\frac12
\iint
u_\lambda(\theta)u_\lambda(\phi)
(v(\theta)-v(\phi))^2
\,dJ_\lambda(\theta,\phi),
\] donde \(J_\lambda\) es la medida de saltos Beurling–Deny del carré-du-champ original. Por tanto \[
d\eta_\lambda(\theta,\phi)
=
\alpha_\lambda^{-1}
u_\lambda(\theta)u_\lambda(\phi)
\,dJ_\lambda(\theta,\phi).
\] Entonces M0–M3 son afirmaciones explícitas sobre momentos de \(d\eta_\lambda\). La prueba práctica debe hacerse así: 1. **M0:** probar \[ |u_\lambda(\theta)|^2\,d\theta \Rightarrow \sin^2\theta\,d\theta. \] 2. **M1:** probar que la masa de conductancia transformada fuera de \(|\theta-\phi|<\delta\) se anula. 3. **M2:** probar \[ \frac12 \iint a\!\left(\frac{\theta+\phi}{2}\right) (\theta-\phi)^2 d\eta_\lambda \to \int a(\theta)\sin^2\theta\,d\theta. \] 4. **M3:** probar que el cuarto momento tiende a cero. El punto importante: esto sólo usa momentos bajos del kernel transformado. La recurrencia de Kronecker que destruía norma de operador vive en frecuencias altas; M0–M3 son afirmaciones suavizadas/locales. Por eso esta ruta evita O11. --- # 8. Test numérico exacto para M0–M3 Antes de escribir la prueba larga, conviene añadir tres diagnósticos al motor. Para bins \(B\subset[0,\pi]\), calcular \[
M_{2,\lambda}(B)
=
\frac12
\iint_{\frac{\theta+\phi}{2}\in B}
(\theta-\phi)^2\,d\eta_\lambda(\theta,\phi).
\] Debe cumplirse \[
M_{2,\lambda}(B)
\approx
\int_B \sin^2\theta\,d\theta.
\] También calcular \[
M_{4,\lambda}
=
\iint|\theta-\phi|^4\,d\eta_\lambda(\theta,\phi)
\] y \[
R_{\delta,\lambda}
=
\iint_{|\theta-\phi|>\delta}d\eta_\lambda.
\] Deben tender a \[
M_{4,\lambda}\to0,
\qquad
R_{\delta,\lambda}\to0.
\] Si estos tres tests pasan, Mosco queda prácticamente probado. --- # 9. Consecuencia para 3.2 Una vez probado 2.3, el gap uniforme estabiliza la proyección espectral del estado fundamental. Entonces la familia normalizada \[
\widehat u_{0,\lambda}(z)
\] no puede saltar de rama. Como cada \(\widehat u_{0,\lambda}\) es real-rooted por CvS, cualquier límite compacto no nulo también es real-rooted por Hurwitz. Así, \[
2.3 \Longrightarrow 3.2.
\] Más precisamente: Mosco da \[
\lambda_1(L_\lambda)\to3,
\] por tanto la proyección sobre el estado fundamental está aislada uniformemente; Kato da convergencia de las proyecciones; Montel da convergencia compacta de las transformadas enteras; Hurwitz conserva real-rootedness. --- # 10. Qué insertar en el paper Recomiendo añadir una subsección: ## Step 2.3 — Doob–Mosco convergence Con los siguientes resultados: 1. **Lemma 2.3.1.** Ground-state transform: \[ \operatorname{Spec}(\mathcal G_\lambda) = \left\{ \frac{\varepsilon_k-\varepsilon_0}{|\varepsilon_0|} \right\}. \] 2. **Lemma 2.3.2.** Beurling–Deny representation: \[ \mathcal G_\lambda(v) = \frac12\iint(v(\theta)-v(\phi))^2d\eta_\lambda. \] 3. **Lemma 2.3.3.** Moment convergence M0–M3. 4. **Theorem 2.3.4.** Mosco convergence: \[ \mathcal G_\lambda\to\mathcal G_\infty. \] 5. **Corollary 2.3.5.** \[ \frac{\varepsilon_1-\varepsilon_0}{|\varepsilon_0|}\to3. \] --- # 11. Resumen El cierre técnico de 2.3 ya no es “identificar autovectores”. Es probar los tres momentos del carré-du-champ transformado: \[
\boxed{
\text{M0 medida}
\quad+\quad
\text{M1 localidad}
\quad+\quad
\text{M2 segundo momento}
\quad+\quad
\text{M3 cuarto momento}
}
\] Eso da Mosco, y Mosco da el gap: \[
\boxed{
\mathcal G_\lambda
\overset{\mathrm{Mosco}}{\longrightarrow}
\int_0^\pi |v'|^2\sin^2\theta\,d\theta
\Longrightarrow
\frac{\varepsilon_1-\varepsilon_0}{|\varepsilon_0|}
\to3.
}
\] Este es el camino limpio, RH-neutral, y evita exactamente el obstáculo Kronecker/norma-resolvente.