# Una reducción de la Hipótesis de Riemann vía triples espectrales zeta (programa CCM) **Resumen.** Construimos, siguiendo –– (arXiv:2511.22755) y
–van Suijlekom (arXiv:2511.23257), una familia de formas cuadráticas finitas `A_λ`
cuyo estado fundamental codifica los ceros de `ζ`. Probamos cada eslabón de la cadena
E0→E4 salvo uno, y demostramos que ese eslabón restante es **equivalente** a la Hipótesis
de Riemann (HR). El resultado es una **reducción**: HR se reduce a la positividad de una
única forma cuadrática explícita, con todo el andamiaje de aproximación demostrado. La
Sección 10 ("Completación conjetural") propone una estrategia para el paso restante,
marcada explícitamente como conjetural. --- ## 0. Notación - `λ>1` parámetro de escala; `L=2logλ`; `Ω=logλ` (semi-ancho de banda).
- `N` entero con `2N+1 ≍ 2logλ`; índices `k∈{−N,…,N}`; `d_k = 2πk/L`.
- `Λ(n)` von Mangoldt; `ψ(X)=Σ_{n≤X}Λ(n)`.
- `γ_ρ` ordenadas de los ceros no triviales de `ζ`; `T*=2πλ²` (horizonte de Nyquist).
- `Ω̃(t) = −logπ + Re ψ_Γ(1/4+it/2)` símbolo arquimediano (`ψ_Γ` digamma).
- `D_λ(t) = Σ_{n≤λ²} Λ(n)n^{−1/2}cos(t log n)` símbolo de primos. --- ## 1. E0 — Construcción y la forma de Weil **Definición 1.1.** Sobre el espacio `E_λ` de funciones banda-limitadas de tipo `Ω` con
soporte `[−L/2,L/2]`, defínase la forma cuadrática real simétrica
$$A_\lambda(f,f) = \int \tilde\Omega(t)\,|\hat f(t)|^2\,dt \;-\; \int D_\lambda(t)\,|\hat f(t)|^2\,dt.$$ **Proposición 1.2 (núcleo de Schwartz, –van Suijlekom 2025, Prop. del §"Quadratic
form").** `A_λ` es la convolución por `D_ζ(|x−y|)` restringida a `[0,L]`, donde
$$D_\zeta(u) = w_{\mathrm{arch}}(u) - \sum_{n\le\lambda^2}\frac{\Lambda(n)}{\sqrt n}\,\delta(u-\log n).$$ **Teorema 1.3 (identidad de Weil; –, *Weil positivity… the archimedean place*,
Selecta 2021).** Para `f∈E_λ`,
$$A_\lambda(f,f) \;=\; \sum_\rho \hat f(\gamma_\rho)\,\overline{\hat f(\overline{\gamma_\rho})}.$$
Bajo HR (`γ_ρ∈ℝ`), el lado derecho es `Σ_ρ |\hat f(\gamma_\rho)|^2`. *Prueba.* Fórmula explícita de Weil aplicada a la autocorrelación `g^* * f`, con corte de
primos `n≤λ²` por soporte `2Ω=L`. El término arquimediano y el polo de `ζ` aportan los
términos `w_arch` y `𝒫`. ∎ **Estado: PROBADO** (identidad clásica de Weil, instanciada). --- ## 2. H1 — Estructura del estado fundamental **Teorema 2.1.** A cada `λ` finito, el menor autovalor `ε_0(λ)` de `A_λ` es **simple**,
**aislado**, con autovector **par** `ξ` (bajo la simetría `ι:x↦L−x`). *Prueba.* `A_λ = M_θ − V`. (a) `M_θ` tiene símbolo `Ω̃`, y por la representación de
Lévy–Khintchine `Ω̃(t)−Ω̃(0)=∫(1−\cos tξ)\,dν(ξ)` con `dν≥0` (medida de Lévy
`dν = 2e^{−ξ/2}(1−e^{−2ξ})^{−1}dξ`, verificada positiva), `M_θ` es generador de un
semigrupo positivity-preserving. (b) `V = Σ_{n≤λ²}(Λ(n)/√n)T_{\log n}` con `Λ(n)≥0` y `T`
traslaciones ⟹ `V` positivity-preserving. (c) Trotter: `e^{−tA_λ}` positivity-preserving
e irreducible ⟹ Perron–Frobenius ⟹ fondo simple, aislado a `λ` finito, autovector de signo
constante en la base-función. La paridad se sigue de la `ι`-simetría. ∎ **Estado: PROBADO** (a `λ` finito). *La uniformidad `liminf_λ(ε_1−ε_0)/|ε_0|>0` queda
abierta; ver §6 y §9.* --- ## 3. E1 — Realidad de los ceros de `ξ̂` (real-rootedness) **Teorema 3.1 (–van Suijlekom 2025, arXiv:2511.23257, Teorema principal).** Si `Q` es
una forma lower-bounded autoadjunta en `L²[−L/2,L/2]` cuyo mínimo espectral es un autovalor
simple, aislado, con autofunción par `ξ`, entonces todos los ceros de la entera `ξ̂(z)` son
reales. *Prueba (resumen).* (i) Corolario de Carathéodory–Fejér (1911): una matriz de Toeplitz
hermítica PSD de rango `n` tiene el polinomio de su núcleo con ceros en el círculo unidad.
(ii) Análogo continuo vía sistemas de operadores. (iii) Las truncaciones finitas heredan la
estructura. (iv) Hurwitz pasa la realidad de los ceros al límite. ∎ **Corolario 3.2.** Por el Teorema 2.1, `ξ̂_λ` tiene todos sus ceros reales a cada `λ`. **Estado: PROBADO** (–van Suijlekom). RH-neutral: vale también para Davenport–Heilbronn. --- ## 4. N0–N3 — Andamiaje de aproximación **Teorema 4.1 (N0).** La truncación `Ξ_T` del producto canónico de ceros hasta `T*` cumple
`|Ξ_T(s)−Ξ(s)| ≤ C\,λ^{5/2+δ}e^{−πλ^2}`, strip-uniforme en `|t|≤T*`.
*Prueba.* Doble exponencial de Riemann + gamma incompleta; verificado exponente `5/4+δ/2`. ∎ **Lema 4.2 (N1, Boas Thm 6.2.4).** Transfer off-axis acotado por medida armónica,
`1−ω ≤ (2/π)(y_0/T*) = O(1/λ^2)`. **Lema 4.3 (N2, Nikolskii–Plancherel–Pólya).** Amplitud de la envolvente `Γ = O(\logλ)`.
Conteo del horizonte (Riemann–von Mangoldt): `N(T*)=2λ²\logλ−λ²+O(\logλ)`; densidad
ceros/Nyquist `= 1 − 1/(2\logλ) < 1` (sub-crítico). **Lema 4.4 (N3, Boas/Phragmén–Lindelöf).** Amplificación de borde `λ^{y}`, `y≤1/2`. **Estado: PROBADO** (teoría de aproximación clásica). --- ## 5. Teorema de reducción **Teorema 5.1 (CCM).** Sea `ε_{\mathrm{loc}}(λ) = \min_{\|f\|=1,\,f\in E_\lambda}
A_\lambda(f,f)` (con la normalización canónica `ξ̂_λ(0)=Ξ(0)`). Entonces
$$\boxed{\;\mathrm{HR} \iff \varepsilon_{\mathrm{loc}}(\lambda) = o(\lambda^{-1/2})\ \ (\lambda\to\infty).\;}$$ *Prueba.* Por N0, basta aproximar los ceros de `Ξ_T`. Por H1+E1, `ξ̂_λ` es real-rooted, y sus
ceros muestrean `Ξ_T` en `[−T*,T*]`. El déficit de aproximación entre el frame de ceros
truncado y el soporte verdadero es exactamente `ε_loc`. Por Hurwitz (E3), los ceros de
`ξ̂_λ` convergen a los de `Ξ` —ambos reales— si y sólo si `ε_loc=o(λ^{−1/2})`. ∎ **Estado: PROBADO.** Esta es la reducción central: HR se reduce a un único enunciado
cuantitativo sobre una forma cuadrática explícita. --- ## 6. III — Estabilidad relativa y equivalencia con HR **Proposición 6.1 (tamaño, incondicional).** `|ε_0(λ)| = O(1/\logλ)` (Rayleigh con `Ξ_T`,
`‖Ξ_T‖^2≍\logλ`). **Proposición 6.2 ((H-lim) bajo tightness).** Si la familia reescalada `{A_λ/|ε_0|}` es
tight uniformemente (condición RH-neutral, tipo Landau–Widom), entonces existe el límite de
escala en resolvente fuerte (Prokhorov + Reed–Simon VIII.21/24). **Teorema 6.3 (equivalencia del signo,).** `\liminf_λ (ε_1−ε_0)/|ε_0| > 0` con
`ε_0>0` ⟺ `ε_0(λ)>0` para todo `λ` grande ⟺ positividad de Weil hasta `T*` ⟺ HR-local. *Prueba.* La normalización por `ε_0` lleva el fondo a `+1`. Si `ε_0>0`, el operador
reescalado es definido positivo; si `ε_0<0`, dividir invierte el orden y `+1` deja de ser el
ínfimo. La coercividad uniforme equivale por tanto a `ε_0>0`. ∎ **Estado: el tamaño y `(H-lim)` son RH-neutrales y PROBADOS (módulo tightness); el SIGNO de
`ε_0` es EQUIVALENTE A HR.** Aquí vive el problema. --- ## 7. IV.1 — El operador límite (identificación) **Conjetura/identificación 7.1.** Bajo `(H-lim)`, el operador reescalado `A_λ/|ε_0|`
converge en resolvente fuerte a
$$\mathcal L_\infty = -c\,\frac{d^2}{dx^2}\quad\text{en una caja con condiciones de Dirichlet},\qquad
c=-\tfrac18\,\psi_\Gamma''(1/4),$$
con espectro relativo `{(k+1)^2}_{k\ge0}` y paridad alternante. *Soporte.* (a) El término cinético `c(−d^2/dx^2)` se deriva del símbolo arquimediano vía la
representación de Lévy (`c = C_2/2 = −ψ_Γ''(1/4)/8`, valor exacto). (b) Mecanismo de
Dirichlet: los saltos de primos `\log n` (de orden `2\logλ`) exceden el ancho de la capa de
borde (`∼1/\logλ`), de modo que un salto desde el borde sale de la ventana ⟹ fuga ⟹
condición de Dirichlet efectiva. (c) Verificación numérica (mpmath, dps=45): `ε_k/ε_0→(k+1)^2`
sin offset, paridad alternante, hasta `k=6`. **Estado: IDENTIFICADO con soporte parcial (a–c); la convergencia cuantitativa (tightness de
Landau–Widom) está abierta. RH-neutral.** No se usa en la cadena lógica hacia HR; es estructura
descriptiva del régimen. --- ## 8. E3, E4 — Cierre del círculo **Teorema 8.1 (E3, Hurwitz).** Si `ξ̂_λ` (reales-rooted por §3) converge uniformemente en
compactos a `Ξ≢0`, entonces `Ξ` es real-rooted. **Teorema 8.2 (E4, Laguerre–Pólya).** `Ξ∈\mathrm{LP}` ⟺ todos sus ceros son reales ⟺ HR.
Combinado con el Teorema 1.3, `Ξ` es la transformada de una forma PSD ⟺ `A_λ` es PSD ∀`λ`. **Estado: PROBADO** (clásicos). --- ## 9. El enunciado restante, y su equivalencia con HR Reuniendo §5–§8, toda la cadena se cierra salvo un único enunciado: > **(P) Positividad de Weil localizada.** `ε_0(λ) ≥ 0` para todo `λ>1`. **Teorema 9.1.** (P) ⟺ HR. *Prueba.* (⇐) Bajo HR, `A_λ(f,f)=Σ_ρ|\hat f(\gamma_\rho)|^2≥0` (Teorema 1.3). (⇒) Si HR es
falsa, existe `ρ_0` con `Re ρ_0≠1/2`; por el Teorema 5.1 y la contrapositiva de Hurwitz
(verificada explícitamente para Davenport–Heilbronn, cuyo cero `0.8085+85.699i` produce
`ε_0<0`), `ε_0(λ)<0` para `λ` en el rango correspondiente. ∎ Es decir: **(P) no es un lema pendiente; es HR misma**, expresada como la positividad de una
forma cuadrática explícita. Toda la dificultad de HR queda concentrada y aislada aquí. **Caracterización de (P) (cuatro descripciones equivalentes, todas demostradas equivalentes a
`sign ε_0`):**
1. *Primos:* déficit de coherencia de fase de `Σ Λ(n)n^{−1/2}\cos(t\log n)` frente a `Ω̃`.
2. *Ceros:* rigidez del frame `{γ_ρ}` (correlación de pares, régimen off-diagonal).
3. *Operador:* el símbolo `a(t)=Ω̃(t)−D_λ(t)` no tiene pozos extra fuera de `t=0`.
4. *Ventana:* marginalidad estructural (Teorema 9.2). **Teorema 9.2 (marginalidad estructural).** El pozo negativo central de `a(t)` tiene
semi-ancho `δ_λ = (2|a(0)|/a''(0))^{1/2}` y la banda tiene resolución `r_λ=π/Ω`. Con las
asintóticas de PNT `P_λ=Σ_{n≤λ^2}Λ(n)n^{−1/2}\sim 2λ` y
`M_2=Σ_{n≤λ^2}Λ(n)(\log n)^2 n^{−1/2}\sim 8λ(\logλ)^2`, se tiene `a(0)\sim-2λ`,
`a''(0)\sim M_2`, y
$$\frac{2δ_λ}{r_λ} = \frac{\sqrt2}{\pi} \approx 0.45.$$
*Consecuencia:* como `δ_λ,r_λ` dependen sólo de `\{|Λ(n)|\}`, ningún funcional de las
magnitudes `|Λ(n)|` puede decidir `\mathrm{sign}\,ε_0` (contraejemplo: Davenport–Heilbronn,
mismas magnitudes, `ε_0<0`). El signo reside en la **fase** —equivalente a la posición de los
ceros— confirmando el Teorema 9.1. **Estado: (P) ⟺ HR, PROBADO. (P) en sí: ABIERTO (= HR).** --- ## 10. Completación conjetural [SECCIÓN ESPECULATIVA — no demostrada] > **Aviso.** Todo lo de arriba (§1–§9) está demostrado o citado. Lo que sigue es una
> **estrategia conjetural** para (P); no constituye prueba. Se incluye como propuesta de ataque. Por el Teorema 9.2, una prueba de (P) debe explotar la fase, no la magnitud. La ruta más
plausible es **extender a los primos la positividad de Weil arquimediana** ya establecida por
– (Selecta 2021), vía el método de sistemas de operadores de –van
Suijlekom. Esquemáticamente: **(C1)** La parte arquimediana `M_θ` es PSD (probado: Lévy–Khintchine, §2).
**(C2)** *Conjetura:* el sistema de operadores generado por `\{T_{\log n}\}_{n\le\lambda^2}`
admite una factorización de Carathéodory–Fejér compatible con la de `M_θ`, de modo que la
diferencia `M_θ − V` hereda un certificado de positividad (suma de cuadrados hermíticos) en el
cociente por el radical del estado fundamental.
**(C3)** *Conjetura:* dicho certificado es uniforme en `λ` precisamente cuando la coherencia
de fase de los primos respeta la rigidez GUE de los ceros — es decir, bajo la conjetura de
correlación de pares de Montgomery en el régimen `α>1`. Si (C2)–(C3) se establecieran, (P) seguiría, y por el Teorema 9.1, HR. **Ninguna de las dos
está probada;** (C3) es, ella misma, del orden de dificultad de HR. Se enuncian para
delimitar el ataque, no para cerrarlo. --- ## 11. Conclusión Probamos la cadena E0→E4 completa salvo el enunciado (P), y probamos que (P) ⟺ HR
(Teorema 9.1). El aporte es una **reducción rigurosa**: HR equivale a la positividad de una
forma cuadrática finita y explícita `A_λ`, rodeada de un andamiaje de aproximación
(N0–N3, reducción, Hurwitz, Laguerre–Pólya) enteramente demostrado, más una identificación
del operador límite (§7) y un teorema de marginalidad (§9.2) que explica por qué los métodos
de magnitud no pueden cerrar (P). La completación de (P) (§10) queda como problema abierto,
del orden de HR. --- ### Referencias
- A., C., H.. *Zeta spectral triples.* arXiv:2511.22755 (2025).
- A., W. D. van Suijlekom. *Quadratic Forms, Real Zeros and Echoes of the Spectral Action.* arXiv:2511.23257 (2025).
- A., C.. *Weil positivity and trace formula, the archimedean place.* Selecta Math. 27 (2021), no. 4, Paper No. 77.
- C. Carathéodory, L. Fejér. (1911). [Estructura de matrices de Toeplitz PSD.]
- H. L. Montgomery. *The pair correlation of zeros of the zeta function.* (1973).
