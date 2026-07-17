# Tres problemas sobre una familia de formas cuadráticas ## Marco común (válido para los tres) Para `λ>1` sea `L=2logλ`, `Ω=logλ`. Sobre el espacio `E_λ` de funciones enteras de tipo
exponencial `Ω` con soporte espectral en `[−L/2,L/2]`, definimos la forma cuadrática real
simétrica
$$A_\lambda(f,f)=\int a(t)\,|\hat f(t)|^2\,dt,\qquad a(t)=\tilde\Omega(t)-D_\lambda(t),$$
con símbolo arquimediano `Ω̃(t)=−logπ+Re ψ_Γ(1/4+it/2)` (`ψ_Γ` digamma) y símbolo de
"acoplamiento" `D_λ(t)=Σ_{n≤λ²}Λ(n)n^{−1/2}cos(t log n)` (`Λ` von Mangoldt). Equivalentemente
`A_λ` es la compresión a `[0,L]` de la convolución por `D_ζ(|x−y|)`. Hechos establecidos (a `λ` finito): `A_λ` es real simétrica, lower-bounded, con espectro
discreto `ε_0(λ)≤ε_1(λ)≤⋯`; el fondo `ε_0` es **simple, aislado y par** (Perron–Frobenius vía
la positividad del semigrupo arquimediano y `Λ(n)≥0`). Notación: `γ(λ):=(ε_1(λ)−ε_0(λ))/|ε_0(λ)|` (gap relativo); `Â_λ:=A_λ/|ε_0(λ)|` (familia
renormalizada por el valor absoluto del fondo). --- ## PROBLEMA III — Estabilidad relativa y gap uniforme **Enunciado.**
- **(III-a)** Probar que `Â_λ` converge, en sentido de resolvente fuerte, a un operador límite `𝓛_∞` cuando `λ→∞`.
- **(III-b)** Probar `liminf_{λ→∞} γ(λ) > 0` (el gap relativo no colapsa). **Qué hay que resolver para abrirlo.** Una **cota de tightness uniforme** sobre la familia
`{Â_λ}`: que la masa espectral del fondo no se escape ni a `0` ni a `∞` al renormalizar. En
términos de formas, una equivalencia uniforme `c_1 𝓔_D ≤ Â_λ ≤ c_2 𝓔_D` con la forma de
Dirichlet `𝓔_D(f)=∫|f'|²` y `0<c_1≤c_2<∞` independientes de `λ`. La cota superior es directa
(el símbolo arquimediano domina la derivada); el núcleo es la **cota inferior uniforme**. **Qué abre.** III es la **puerta de entrada a IV.1**: sin existencia y estabilidad del límite
(III-a) y sin gap uniforme (III-b), la identificación de IV.1 carece de sentido. Resuelta la
estimación de tightness, IV.1 queda planteable. **Naturaleza.** Análisis de operadores estándar (Prokhorov + convergencia fuerte de resolvente,
Reed–Simon VIII.21/24, una vez establecida la tightness). No interviene el signo de `ε_0`. --- ## PROBLEMA IV.1 — Identificación del operador límite **Enunciado.** Probar que el operador límite `𝓛_∞` de (III-a) es
$$\mathcal L_\infty=-c\,\frac{d^2}{dx^2}\quad\text{en un intervalo finito con condiciones de
Dirichlet},\qquad c=-\tfrac18\,\psi_\Gamma''(1/4),$$
con autovalores proporcionales a `(k+1)²` (`k=0,1,2,…`) y autofunciones de paridad alternante. **Qué hay que resolver para abrirlo.** La **asintótica cuantitativa de borde** (Landau–Widom)
de la compresión truncada: mostrar que el espectro bajo de `Â_λ` converge al de la caja de
Dirichlet `(k+1)²`. Ingredientes ya disponibles: (a) el coeficiente cinético
`c=−ψ_Γ''(1/4)/8`, derivado de la expansión de bajo orden del símbolo arquimediano (Lévy);
(b) el mecanismo de Dirichlet por fuga de los términos de acoplamiento (longitud `∼2logλ`,
mayores que el ancho de capa de borde `∼1/logλ`), que actúan como pared dura; (c) verificación
numérica `ε_k/ε_0→(k+1)²` sin offset, paridad alternante. Falta convertir (a)–(c) en la cota
de convergencia uniforme. **Qué abre.** IV.1 **implica III**: si el límite es `𝓛_∞`, entonces existe (III-a) y su gap
relativo es `(2²−1²)/1²=3>0`, luego `γ(λ)→3` y `liminf γ>0` (III-b). Es decir, **una misma
estimación de tightness resuelve III y IV.1 a la vez**, siendo IV.1 la versión más fina. **Dependencia.** Requiere III (la existencia que IV.1 refina). No requiere ni aporta nada sobre
el signo de `ε_0`. --- ## PROBLEMA (P) — Positividad **Enunciado.** Probar que `ε_0(λ) ≥ 0` para todo `λ>1`. **Qué hay que resolver para abrirlo.** Una **cota inferior sobre el mínimo de la forma**
`A_λ(f,f)` que controle su **signo**: equivalentemente, que la parte de acoplamiento `D_λ` no
domine a la parte arquimediana `Ω̃` sobre la banda. La obstrucción precisa está dada por el
**teorema de marginalidad**: el pozo negativo de `a(t)` tiene semi-ancho
`δ_λ=(2|a(0)|/a''(0))^{1/2}=1/(√2 logλ)` y la banda resolución `r_λ=π/logλ`, con cociente
`2δ_λ/r_λ=√2/π≈0.45`; ambos dependen **sólo de las magnitudes** `{|Λ(n)|}`. Por tanto ningún
funcional de esas magnitudes decide el signo (existen sistemas de igual magnitud con `ε_0<0`).
El signo reside en la **fase** de los términos de acoplamiento. Resolver (P) requiere una
estimación **sensible a la fase**, no de magnitud. **Qué abre.** Es el problema terminal de la cadena; nada más depende de él dentro de esta
estructura. **Dependencia.** **Independiente de III y IV.1.** Estos conciernen a `Â_λ=A_λ/|ε_0|`, que es
ciego al signo de `ε_0` por construcción. Resolver III y IV.1 **no avanza** (P), y (P) no
necesita ninguno de los dos. La única vía por la que IV.1 tocaría (P) sería dar la asintótica
de `ε_0` **con signo** (no `|ε_0|`), pero ese fortalecimiento ya es (P). --- ## Resumen de la estructura ``` ┌─ cota de tightness / Landau–Widom ─┐ │ │ ▼ ▼ PROBLEMA III ───────────────────────▶ PROBLEMA IV.1 (existencia + gap uniforme) (identificación de 𝓛_∞) gateway refinamiento; IV.1 ⟹ III PROBLEMA (P) ── cerradura independiente ── (signo de ε_0) no se abre con III ni IV.1; requiere una estimación de fase
``` - **III y IV.1:** acoplados. Una sola estimación (tightness/Landau–Widom) los abre a ambos; IV.1 ⟹ III. Naturaleza: análisis técnico estándar.
- **(P):** aislado. Es el problema profundo e independiente; ningún progreso en III/IV.1 lo acerca. Requiere control de **fase**, no de magnitud (teorema de marginalidad).
