# Eslabón 2 (convergencia ξ̂_{λ,N} → Ξ): estructura, ataque y estado **Foco:** este es EL hueco del mapa a RH. Todo lo demás (Eslabones 1,3,4) está probado o es
clásico. Cerrar Eslabón 2 ⟹ RH. --- ## 0. Por qué pivotamos de numérico a teórico (honesto) E6 intentó medir el "horizonte" H(λ) = altura hasta la que los ceros se resuelven, como
medida empírica de 2b. **Bloqueado numéricamente:** cond(QW_λ^N) ≈ 10¹⁶–10¹⁷ (diagnóstico
directo). El primer cero sobrevive (1e-14 a N=70) pero los ceros altos —que dependen de las
componentes pequeñas del autovector del menor autovalor— se ahogan en ruido float64. La
medición de H(λ) salió no-monótona en λ (λ=3.0→H≈56 pero λ=3.7→H≈30): ruido, no señal.
Resolverlo exige mpmath a N~50-80 (caro). **El crux 2b no cede a fuerza bruta numérica acá.** Lo que el numérico SÍ dejó firme: 2a converge rápido (E4hp, geométrico), y el engine está
validado en ζ (a=1/4) y L(χ_-4) (a=3/4). --- ## 1. 2a (N→∞ a λ fijo): REDUCIDO a simplicidad. Casi cerrado. **Afirmación:** ξ̂_{λ,N} → ξ̂_{λ,∞} localmente uniforme, MODULO que el menor autovalor de A_λ
sea simple (= hipótesis H1 de Thm 1.1). **Argumento (sólido):** 1. **A_λ tiene resolvente compacta ⟹ espectro discreto.** El operador de scaling D_log = −i d/d(log u) sobre el intervalo COMPACTO [λ⁻¹,λ] con condiciones periódicas tiene espectro discreto {2πk/L}. La forma QW_λ (3.19) = archimedeana (θ-peso, define el dominio de forma) − parte de primos. La parte de primos es Σ_{n≤λ²} Λ(n) T(n), **suma FINITA de operadores acotados** (T(n) acotado: convolución de L² en grupo compacto es continua, evaluación acotada). Perturbación acotada y semiacotada inferiormente (Prop 3.3). El dominio de forma embebe **compactamente** en L²([λ⁻¹,λ]) por **Rellich–Kondrachov** (intervalo acotado). ⟹ A_λ tiene resolvente compacta ⟹ espectro **discreto**, cada autovalor aislado, incluido el ínfimo ε_∞. 2. **Galerkin/secciones finitas convergen al fondo aislado.** E_N = span{V_k: |k|≤N} ⊂ E_{N+1}, y E = ∪E_N es **core** de la forma (Prop 3.4). Por min-max, ε_N ↓ ε_∞ monótono. Como ε_∞ es autovalor **aislado** (paso 1), el proyector espectral de la sección converge en norma y el autovector ξ_N → ξ_∞ en norma de forma (teoría estándar de aproximación de Galerkin para formas semiacotadas con fondo aislado). 3. **Transformada continua ⟹ ξ̂_N → ξ̂_∞ localmente uniforme.** La transformada ξ ↦ ξ̂ (3.5) es continua en la norma relevante; convergencia de ξ_N ⟹ convergencia local-uniforme de ξ̂_N a ξ̂_∞ (funciones enteras, compactos). **Hueco residual de 2a:** simplicidad del fondo ε_∞ (H1). Reducible al **sector par** (H2,
ξ par por invariancia ι: u↦u⁻¹) + argumento nodal/Perron–Frobenius en el sector par. Es un
problema acotado y clásico, NO el muro. > **Estado 2a: esencialmente cerrado, módulo H1 (simplicidad).** Esto es matemática nueva y
> concreta del programa — la primera pieza del gap de convergencia con prueba real. --- ## 2. 2b (λ→∞): el crux. Mecanismo identificado, prueba abierta. **Fenómeno clave a explicar (de los datos):** el 1er cero sale a ~1e-18 con primos ≤13
(E4hp; paper: 1e-55). Esto es **muchísimo más rápido que la truncación del explicit formula**
(ψ(X)−X ~ O(1) en X=13). ⟹ **2b NO es truncación de primos.** La rigidez de
Carathéodory–Fejér extrae el cero con precisión que la truncación no explica. **La estructura real de 2b = crecimiento del HORIZONTE.** A λ fijo, ξ̂_λ es esencialmente
band-limited (banda ∝ L=2logλ); resuelve ceros hasta una altura H(λ) y los de más arriba no.
2b ⟺ **H(λ) → ∞**. **Mecanismo conjeturado (zero-independiente, la dirección prometedora):**
el nº de ceros hasta altura T es N(T) ~ (T/2π)log(T/2π); el nº de primos ≤λ² es
π(λ²) ~ λ²/(2logλ). El operador "fija" ceros mientras tenga constraints de primos suficientes.
Igualar N(H(λ)) ~ π(λ²) da el horizonte. Si esto es correcto, **H(λ)→∞ está gobernado por el
CONTEO de primos (PNT) — dato del lado-primo, independiente de la ubicación de ceros.** > **Si se prueba H(λ)→∞ desde π(λ²)→∞ (PNT), entonces 2b → RH es NO-circular.** Esa es la
> apuesta. El riesgo: que la "fijación" de cada cero requiera control fino del resto del
> espectro que secretamente equivalga a regiones libres de ceros (RH). Decidir esto es la
> pregunta de prueba pura central del programa. **Próximo paso 2b (cuando haya mpmath a N grande):** medir H(λ) limpio (alta precisión) y
contrastar su tasa con π(λ²) (predicción PNT) vs N(T) — si H(λ) ~ (la altura tal que
N(H)=π(λ²)), el mecanismo de conteo se confirma y la diana teórica queda fijada. --- ## 3. Estado del gap (resumen) | Sub-eslabón | Estado | Qué falta |
|---|---|---|
| 2a (N→∞) | **esencialmente cerrado** (compact resolvent + Galerkin) | simplicidad H1 (sector par + nodal) |
| 2b (λ→∞) | mecanismo identificado (horizonte ~ conteo de primos, PNT) | prueba de H(λ)→∞ zero-indep; medición mpmath del rate | Cerrar 2a (vía H1) es alcanzable y publicable. 2b es el crux real, ahora con una diana
concreta (H(λ)→∞ por PNT) en vez de "convergencia" abstracta.
