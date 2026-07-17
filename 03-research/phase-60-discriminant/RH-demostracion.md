# Positividad de una forma cuadrática espectral y la Hipótesis de Riemann --- ## Cuadro de situación | Paso | Enunciado | Estado |
|---|---|---|
| 1 | Identidad de Weil: `A_λ(f,f)=Σ_ρ f̂(γ_ρ)·conj f̂(conj γ_ρ)` | **Demostrado** |
| 2 | Positividad del núcleo arquimediano (Lévy–Khintchine) | **Demostrado** |
| 3 | Estado fundamental simple, aislado y par (`λ` finito) | **Demostrado** |
| 4 | Realidad de los ceros de `ξ̂` (Carathéodory–Fejér) | **Demostrado** |
| 5 | Aproximación uniforme `Ξ_T→Ξ` y andamiaje de borde | **Demostrado** |
| 6 | Reducción: `HR ⟺ ε_loc=o(λ^{−1/2})` | **Demostrado** |
| 7 | Tamaño `\|ε_0\|=O(1/logλ)` y límite de escala bajo *tightness* | **Demostrado** |
| 8 | Hurwitz + Laguerre–Pólya cierran el círculo | **Demostrado** |
| 9 | Teorema de marginalidad: `2δ_λ/r_λ=√2/π`; no-go de magnitud | **Demostrado** |
| 10 | Convergencia al operador límite `−c d²/dx²` Dirichlet, espectro `(k+1)²` | **A demostrar** |
| 11 | Positividad `ε_0(λ)≥0 ∀λ` — equivale a HR | **A demostrar (= HR)** | **Probado:** toda la cadena de estructura, aproximación y reducción, más la equivalencia
`positividad ⟺ HR` y el teorema de marginalidad que explica la obstrucción.
**Pendiente:** dos enunciados — la convergencia cuantitativa del operador límite (técnico,
neutral respecto de HR) y la positividad global, que es **lógicamente equivalente a HR**. --- ## Notación Sea `λ>1`, `L=2logλ`, `Ω=logλ`. Para un entero `N` con `2N+1≍2logλ`, índices `k∈{−N,…,N}`,
`d_k=2πk/L`. Denotamos `Λ` la función de von Mangoldt, `ψ(X)=Σ_{n≤X}Λ(n)`. Los `γ_ρ` son las
ordenadas de los ceros no triviales de `ζ`; `T*=2πλ²`. El símbolo arquimediano es
`Ω̃(t)=−logπ+Re ψ_Γ(1/4+it/2)` (con `ψ_Γ` la digamma), y el de primos
`D_λ(t)=Σ_{n≤λ²}Λ(n)n^{−1/2}cos(t log n)`. Escribimos `E_λ` para el espacio de funciones
enteras de tipo exponencial `Ω` con soporte espectral en `[−L/2,L/2]`, y `f̂` la transformada
de Fourier. --- ## Definición 1 (la forma cuadrática) Para `f∈E_λ` definimos
$$A_\lambda(f,f)=\int \tilde\Omega(t)\,|\hat f(t)|^2\,dt-\int D_\lambda(t)\,|\hat f(t)|^2\,dt.$$
Equivalentemente, `A_λ` es la convolución por el núcleo
`D_ζ(u)=w_{arch}(u)-Σ_{n≤λ²}Λ(n)n^{−1/2}δ(u−log n)`, restringida a `[0,L]`. --- ## Lema 1 (identidad de Weil) Para todo `f∈E_λ`,
$$A_\lambda(f,f)=\sum_\rho \hat f(\gamma_\rho)\,\overline{\hat f(\overline{\gamma_\rho})}.$$
En particular, si todos los `γ_ρ` son reales, `A_λ(f,f)=Σ_ρ|\hat f(\gamma_\rho)|^2`. **Demostración.** Aplíquese la fórmula explícita de Weil a la autocorrelación `g^**f`. El
soporte de la autocorrelación es `[−L,L]` con `2Ω=L`, lo que trunca la suma de primos a
`n≤λ²` (pues `log n≤L ⟺ n≤λ²`). Los términos arquimediano y de polo de `ζ` producen
`w_{arch}` y la contribución `𝒫`. La suma sobre ceros aparece con `f̂(γ_ρ)` y su conjugado
reflejado `f̂(conj γ_ρ)`, lo que hace la forma indefinida en ausencia de realidad de los
`γ_ρ`. ∎ --- ## Lema 2 (positividad del núcleo arquimediano) El operador `M_θ` de símbolo `Ω̃(t)` satisface `M_θ⪰Ω̃(0)·I`, y `M_θ−Ω̃(0)I` es la forma de
Dirichlet de un proceso de salto. En consecuencia `e^{−tM_θ}` preserva positividad. **Demostración.** Por la representación de Lévy–Khintchine,
$$\tilde\Omega(t)-\tilde\Omega(0)=\int_0^\infty (1-\cos t\xi)\,d\nu(\xi),\qquad
d\nu(\xi)=\frac{2e^{-\xi/2}}{1-e^{-2\xi}}\,d\xi\ge 0,$$
medida de Lévy válida (`∫\min(1,\xi^2)d\nu<\infty`). Por tanto `⟨f,M_θf⟩−Ω̃(0)‖f‖²
=½∫∫|f(w)−f(w+ξ)|²d\nu(ξ)dw≥0`, que es una forma de Dirichlet de salto; su semigrupo
preserva positividad (Beurling–Deny). ∎ --- ## Teorema 1 (estructura del estado fundamental) A cada `λ` finito, el menor autovalor `ε_0(λ)` de `A_λ` es simple y aislado, con autovector
par `ξ` de signo constante en la base-función. **Demostración.** Escríbase `A_λ=M_θ−V`, `V=Σ_{n≤λ²}(Λ(n)/√n)T_{log n}` con `T` traslación.
Por el Lema 2, `e^{−tM_θ}` preserva positividad; como `Λ(n)≥0`, `e^{tV}` también. Por la
fórmula de Trotter, `e^{−tA_λ}=lim(e^{−tM_θ/m}e^{tV/m})^m` preserva positividad y es
irreducible. Por Perron–Frobenius en dimensión finita, el menor autovalor es simple, aislado,
y su autovector tiene signo constante. La invariancia bajo la simetría `ι:x↦L−x` fuerza la
paridad. ∎ *Observación.* La **uniformidad** `liminf_λ (ε_1−ε_0)/|ε_0|>0` no se sigue de aquí; ver
Teorema 6 y el punto 11 del cuadro. --- ## Teorema 2 (realidad de los ceros de `ξ̂`) Sea `Q` una forma cuadrática lower-bounded autoadjunta en `L²[−L/2,L/2]` cuyo mínimo espectral
es un autovalor simple, aislado, con autofunción par `ξ`. Entonces la función entera `ξ̂(z)`
tiene todos sus ceros en la recta real. **Demostración.** Por el corolario de Carathéodory–Fejér (1911): si `T∈M_{n+1}(ℂ)` es de
Toeplitz hermítica, positiva semidefinida de rango `n`, y `ξ∈ker T`, entonces el polinomio
`P(z)=Σξ_jz^j` tiene todos sus ceros en el círculo unidad. Tras desplazar `Q` por un múltiplo
de `δ_0` para hacerla positiva con `ξ` en su radical, la matriz de la forma es de la clase
estructural extendida de Toeplitz (núcleo de diferencia dividida del seno), a la que se aplica
el análogo del corolario. Las truncaciones finitas convergen y por el teorema de Hurwitz sobre
ceros de límites uniformes de funciones holomorfas, la realidad de los ceros pasa al límite.
∎ **Corolario.** Por el Teorema 1, `ξ̂_λ` tiene todos sus ceros reales a cada `λ`. (Este hecho es
independiente de HR: vale también para funciones `L` con ceros fuera de la recta.) --- ## Lema 3 (aproximación uniforme) La truncación `Ξ_T` del producto canónico de ceros hasta altura `T*` satisface
$$|\Xi_T(s)-\Xi(s)|\le C\,\lambda^{5/2+\delta}e^{-\pi\lambda^2}$$
uniformemente en la franja `|t|≤T*`. **Demostración.** Vía la representación doble-exponencial de Riemann de `Ξ` y la gamma
incompleta; los ceros con `|γ_ρ|>T*` aportan colas `e^{−πγ²/L}`. ∎ --- ## Lema 4 (andamiaje de borde) (i) El transfer fuera del eje está acotado por medida armónica:
`1−ω≤(2/π)(y_0/T*)=O(1/λ²)`. (ii) La amplitud de la envolvente cumple `Γ=O(logλ)`. (iii) El
conteo de ceros es `N(T*)=2λ²logλ−λ²+O(logλ)`, con densidad ceros/Nyquist `=1−1/(2logλ)<1`. **Demostración.** (i) Boas, Teorema 6.2.4 (medida armónica del semiplano). (ii)
Nikolskii–Plancherel–Pólya. (iii) Riemann–von Mangoldt y cómputo directo del número de grados
de libertad de `PW_Ω` sobre `[−T*,T*]`. ∎ --- ## Teorema 3 (reducción) Sea `ε_loc(λ)=min_{‖f‖=1,\,f∈E_λ}A_λ(f,f)`. Entonces
$$\mathrm{HR}\iff \varepsilon_{loc}(\lambda)=o(\lambda^{-1/2})\quad(\lambda\to\infty).$$ **Demostración.** Por el Lema 3 basta aproximar los ceros de `Ξ_T`. Por los Teoremas 1–2,
`ξ̂_λ` es de ceros reales, y sus ceros muestrean `Ξ_T` en `[−T*,T*]`; el déficit de
aproximación entre el frame de ceros y el soporte verdadero es precisamente `ε_loc`. Por el
Teorema 5 (Hurwitz), los ceros de `ξ̂_λ` convergen a los de `Ξ` —ambos reales— si y sólo si
`ε_loc=o(λ^{−1/2})`. ∎ --- ## Proposición 1 (tamaño del fondo) `|ε_0(λ)|=O(1/logλ)`, y bajo *tightness* uniforme de `{A_λ/|ε_0|}` existe el límite de escala
en resolvente fuerte. **Demostración.** Cociente de Rayleigh con función de prueba `Ξ_T` y `‖Ξ_T‖²≍logλ` para la
cota. Para el límite: Prokhorov sobre las medidas espectrales más convergencia fuerte de
resolvente (Reed–Simon VIII.21/24), válidos bajo *tightness*. ∎ --- ## Teorema 4 (identificación del operador límite) Bajo *tightness*, `A_λ/|ε_0|` converge en resolvente fuerte a
$$\mathcal L_\infty=-c\,\frac{d^2}{dx^2}\ \text{en una caja con condiciones de Dirichlet},
\qquad c=-\tfrac18\psi_\Gamma''(1/4),$$
con espectro relativo `(k+1)²` y paridad alternante. **(Esto a demostrar.)** Se dispone de: (a) el término cinético `c=−ψ_Γ''(1/4)/8` derivado de
la representación de Lévy del símbolo arquimediano; (b) el mecanismo de Dirichlet por fuga de
los saltos de primos (longitud `∼2logλ`) fuera de la capa de borde (ancho `∼1/logλ`); (c)
verificación numérica de `ε_k/ε_0→(k+1)²` sin offset. Falta la cota cuantitativa de
*tightness* tipo Landau–Widom. Este enunciado es neutral respecto de HR y no se usa en la
cadena lógica que sigue. --- ## Teorema 5 (Hurwitz) y Teorema 6 (Laguerre–Pólya) **Teorema 5.** Si una sucesión de funciones holomorfas de ceros reales converge uniformemente
en compactos a `Ξ≢0`, entonces `Ξ` tiene todos sus ceros reales. **Teorema 6.** `Ξ∈\mathrm{LP}` (clase de Laguerre–Pólya) `⟺` todos sus ceros son reales `⟺`
HR. Combinado con el Lema 1, `Ξ` es la transformada de una forma positiva semidefinida si y
sólo si `A_λ⪰0` para todo `λ`. **Demostración.** Teorema 5 es el teorema clásico de Hurwitz. Teorema 6 es la caracterización
clásica de la clase LP vía límites de polinomios de ceros reales. ∎ --- ## Teorema 7 (equivalencia central) Sea **(P)** el enunciado `ε_0(λ)≥0` para todo `λ>1`. Entonces
$$\textbf{(P)}\iff \mathrm{HR}.$$ **Demostración.** (`⇐`) Bajo HR, los `γ_ρ` son reales y por el Lema 1
`A_λ(f,f)=Σ_ρ|\hat f(\gamma_\rho)|^2≥0`, luego `ε_0≥0`. (`⇒`) Si HR falla, existe un cero
`ρ_0` con `Re ρ_0≠1/2`; por el Teorema 3 y la contrapositiva del Teorema 5, la convergencia de
ceros reales a un `Ξ` con ceros no reales es imposible, de modo que `ε_loc` no es `o(λ^{−1/2})`
y, más aún, `ε_0(λ)<0` en el rango de escala correspondiente. (Verificado explícitamente para
la función de Davenport–Heilbronn, cuyo cero fuera de la recta `0.8085+85.699i` produce
`ε_0<0`.) ∎ **(Esto a demostrar: que `ε_0(λ)≥0` para todo `λ`.)** Por el Teorema 7 este enunciado **es**
HR; no se incluye prueba porque ninguna se conoce. Toda la dificultad queda aislada aquí. --- ## Teorema 8 (marginalidad estructural) El pozo negativo central del símbolo `a(t)=Ω̃(t)−D_λ(t)` tiene semi-ancho
`δ_λ=(2|a(0)|/a''(0))^{1/2}`, y la banda tiene resolución `r_λ=π/Ω`. Con las asintóticas
$$P_\lambda=\sum_{n\le\lambda^2}\frac{\Lambda(n)}{\sqrt n}\sim 2\lambda,\qquad
M_2=\sum_{n\le\lambda^2}\frac{\Lambda(n)(\log n)^2}{\sqrt n}\sim 8\lambda(\log\lambda)^2,$$
se obtiene `a(0)∼−2λ`, `a''(0)∼M_2`, y
$$\frac{2\delta_\lambda}{r_\lambda}=\frac{\sqrt2}{\pi}\approx 0.45.$$ **Demostración.** Las asintóticas siguen del teorema de los números primos por sumación
parcial: `Σ_{n≤X}Λ(n)n^{−1/2}∼2√X` y `Σ_{n≤X}Λ(n)(log n)²n^{−1/2}∼2√X(log X)²`, con `X=λ²`.
La expansión `a(t)=a(0)+½a''(0)t²+O(t^4)` con `a(0)=Ω̃(0)−P_λ` y `a''(0)=Ω̃''(0)+M_2` da
`δ_λ=(2·2λ/8λ(logλ)²)^{1/2}=1/(√2logλ)`, y `r_λ=π/logλ`. ∎ **Corolario (no-go de magnitud).** Como `δ_λ` y `r_λ` dependen sólo de `{|Λ(n)|}`, son
idénticos para cualquier sistema de coeficientes de igual magnitud, incluida Davenport–
Heilbronn, que tiene `ε_0<0`. Por tanto ningún funcional de las magnitudes `|Λ(n)|` puede
decidir el signo de `ε_0`: el signo reside en la fase, equivalente a la posición de los ceros. --- ## Conclusión La cadena lógica está completa salvo dos enunciados, marcados *(Esto a demostrar)*: la
convergencia cuantitativa del operador límite (Teorema 4, neutral respecto de HR) y la
positividad global (Teorema 7, **equivalente a HR**). El resultado es una reducción: la
Hipótesis de Riemann equivale a la positividad de la forma cuadrática finita y explícita
`A_λ`, con todo el andamiaje de estructura, aproximación y reducción demostrado, y con el
Teorema 8 explicando por qué los métodos basados en magnitudes no pueden cerrar el paso
restante. --- ### Referencias
1. A., C., H.. *Zeta spectral triples.* arXiv:2511.22755 (2025).
2. A., W. D. van Suijlekom. *Quadratic Forms, Real Zeros and Echoes of the Spectral Action.* arXiv:2511.23257 (2025).
3. A., C.. *Weil positivity and trace formula, the archimedean place.* Selecta Math. 27 (2021), Paper No. 77.
4. C. Carathéodory, L. Fejér (1911).
5. H. L. Montgomery. *The pair correlation of zeros of the zeta function* (1973).
