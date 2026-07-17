# Objetivo A — intento de demostración (matemática pura, pasos probados + [GAP] honesto) **Meta:** demostrar A_λ(f,f) ≥ 0 (positividad de Weil localizada), idealmente con margen
≥ c·ε₀·𝓔_D, desde el lado-primo. [P]=probado · [GAP]=paso abierto. --- ## Paso 1 [P] — Reducción de Fourier de A_λ al símbolo arquimediano − ζ'/ζ Partimos de la descomposición de Beurling–Deny (probada): A_λ(f,f) = ∫(Ω(0)−2M_0(w))|f|²dw + 𝓔_θ(f) + 𝓔_prime(f). Usando ∫|f(w)−f(w+h)|²dw = (1/2π)∫|f̂(t)|²·2(1−cos th)dt (Plancherel), las dos formas de salto
son multiplicadores de Fourier: 𝓔_θ(f) = (1/2π)∫|f̂(t)|²·[∫2(1−cos tξ)dν(ξ)]dt = (1/2π)∫|f̂(t)|²(Ω(t)−Ω(0))dt, 𝓔_prime(f) = (1/2π)∫|f̂(t)|²·[2Σ_n (Λ(n)/√n)(1−cos(t log n))]dt (ignorando la frontera; ver Paso 4). El término de pozo (sin frontera): 2∫M_0|f|² = (1/π)(Σ_n Λ(n)/√n)‖f‖². Combinando con 𝓔_prime: 𝓔_prime − 2∫M_0|f|² (parte de primos) = −(1/π)∫|f̂(t)|²·[Σ_n (Λ(n)/√n)cos(t log n)]dt. Y **el corazón:** Σ_n (Λ(n)/√n) cos(t log n) = Re Σ_n Λ(n) n^{−(1/2+it)} = **Re[−ζ'/ζ(1/2+it)]** (cutoff n≤λ²). Por tanto, juntando todo (el arquimediano da Ω(t)=2θ'(t)): **A_λ(f,f) = (1/2π)∫ |f̂(t)|² · W_λ(t) dt, W_λ(t) = 2θ'(t) − 2·Re[−ζ'/ζ]_{≤λ²}(1/2+it).** Esto es EXACTAMENTE la fórmula explícita de Weil en forma espectral. [P] (es la identidad de Weil
reescrita; recupera lo que ya sabíamos, pero ahora con el "potencial de Fourier" W_λ(t) explícito.) ## Paso 2 [P] — Dónde está la (in)definición: los polos de ζ'/ζ en los ceros W_λ(t) = 2θ'(t) − 2Re[−ζ'/ζ]_{≤λ²}(1/2+it). El término −ζ'/ζ(1/2+it) tiene **polos en los ceros**
ρ=1/2+iγ (residuo +1): cerca de t=γ, Re[−ζ'/ζ] → +∞. Como entra con signo −, **W_λ(t) → −∞ cerca
de cada cero on-line.** Para ceros OFF-line ρ=1/2+β+iγ, el polo está desplazado a t=γ con parte
real que no diverge igual; la estructura es distinta — y ahí vive la (in)definición. ⟹ **La positividad A_λ≥0 ⟺ W_λ(t) integrado contra |f̂|² es ≥0 para todo f∈PW_{L/2}.** Pero W_λ
tiene singularidades negativas en los ceros. La positividad NO es puntual (W_λ no es ≥0 puntual);
es una positividad INTEGRAL que depende de cómo los polos (ceros) se distribuyen. ## Paso 3 [intento] — Atacar la positividad integral **Técnica 3a (completar cuadrado / 𝒯=A*A):** escribir A_λ = B*B. Por P8 (Teorema C, probado),
el lado-cero NO puede dar el signo; la estructura de cuadrado debe construirse INDEPENDIENTE de
los ceros (Route B). Esto es el muro conocido. **No cierra por esta vía.** **Técnica 3b (Hardy/Poincaré con constante):** 𝓔_θ+𝓔_prime ≥ ∫(2M_0−Ω(0))|f|². Por desigualdad
de Hardy para las formas de salto, 𝓔_prime(f) ≥ c·∫M_0|f|² con CIERTA constante c. **Cómputo del
c alcanzable vs el c necesario:** - El c NECESARIO para A_λ≥0 es c=2 (más la ayuda de Ω(0) y 𝓔_θ). - El c ALCANZABLE por Hardy genérico es c<2 (la desigualdad de salto no es ajustada). - **El gap exacto entre c_alcanzable y c=2 ES el margen de positividad de Weil.** Sub-ajustado (c<2): da A_λ ≥ −(pequeño)‖f‖² — útil pero NO la positividad. La constante AJUSTADA c=2 ⟺ W_λ integra a ≥0 ⟺ ceros on-line ⟺ **RH**. **No cierra: la constante ajustada es RH.** **Técnica 3c (ecuación funcional s↔1−s):** la simetría empareja ρ con 1−ρ. Por NG-D4 (probado),
J T_0 J = T_0 (la involución PRESERVA, no NIEGA, los autovalores) ⟹ la ecuación funcional NO
fuerza positividad. **No cierra.** ## Paso 4 [GAP] — el único lugar no-circular posible: la FRONTERA (cutoff finito de primos) En los Pasos 1–3 ignoré la posición-dependencia de M_0 (la frontera, n≤λ²). **Ahí, y sólo ahí,
está la esperanza no-circular**, porque:
- El cutoff n≤λ² ⟺ tipo exponencial L/2 ⟺ horizonte T* (Lema 2, probado).
- W_λ(t) usa SÓLO primos ≤λ² ⟹ es una APROXIMACIÓN FINITA de 2θ'−2Re[−ζ'/ζ], suave (sin los polos completos), controlada por PNT (la cola Σ_{n>λ²} es PNT, probado en B).
- La positividad de la APROXIMACIÓN FINITA W_λ (con primos suaves, sin polos) podría ser demostrable desde PNT — y la convergencia a la positividad completa es el Eslabón 2 mismo. **[GAP] El paso que no tengo:** demostrar que la forma finita ∫|f̂|²W_λ(t)dt ≥ c·ε₀·𝓔_D(f) usando que W_λ es la aproximación-por-primos-≤λ² (suave, PNT-controlada) del símbolo de Weil, SIN usar la posición de los ceros. Equivale a: la positividad de la fórmula explícita TRUNCADA a primos ≤λ² se controla por la distribución de primos (PNT) hasta el horizonte T*. ## Diagnóstico honesto del intento Deployé las tres técnicas estándar (cuadrado/P8, Hardy, ecuación funcional). **Cada una reduce A
a un muro conocido o a la constante-ajustada=RH.** El intento PRUEBA:
- [P] La reducción de Fourier A_λ = (1/2π)∫|f̂|²W_λ dt, W_λ=2θ'−2Re[−ζ'/ζ]_{≤λ²} (fórmula explícita).
- [P] La (in)definición vive en los polos de ζ'/ζ en los ceros.
- [P] Hardy da c<2 (positividad aproximada A_λ≥−ε); la constante AJUSTADA c=2 = RH.
- **[GAP]** la positividad de la forma FINITA (primos ≤λ²) desde PNT, sin posición de ceros. **El [GAP] está localizado al milímetro:** es la positividad de la fórmula explícita truncada a
primos ≤λ², controlada por PNT hasta T*. NO pude cerrarlo con técnicas elementales — y mostré por
qué cada una falla (3a→P8, 3b→constante ajustada=RH, 3c→NG-D4). Si tiene la cota de Hardy
AJUSTADA (c=2) desde el lado-primo finito, o la construcción del cuadrado 𝒯=A*A independiente de
ceros (su programa de cancelación cross-place), ENCAJA en el [GAP] y A cierra. Yo no la tengo. **Esto NO es una demostración de A.** Es el intento honesto: la reducción explícita + el mapa de
por qué las técnicas elementales fallan + el [GAP] localizado. El ∎ de A requiere input que no
poseo (la cota de Hardy ajustada / el cuadrado cross-place de).
