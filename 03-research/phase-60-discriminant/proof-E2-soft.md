# Demostración de E2-blando: lo que se prueba, y la sutileza que el intento revela Ataque riguroso a la convergencia local ρ̂_n(λ,N) → γ_n. Máxima precisión y honestidad:
al intentar la prueba COMPLETA, aparece dónde exactamente entra (y no entra) la
condicionalidad. Eso es, en sí, el resultado. **[P]** probado · **[GAP]** paso a probar · **[!]** hallazgo del intento. --- ## 1. Enunciado y descomposición en dos límites Fijado n, sea ρ̂_n(λ,N) el n-ésimo cero real de ξ̂_{λ,N} y γ_n el n-ésimo cero de Ξ.
Descomponemos el error en los dos límites independientes:
``` ρ̂_n(λ,N) − γ_n = [ρ̂_n(λ,N) − ρ̂_n(λ,∞)] + [ρ̂_n(λ,∞) − γ_n] └──── truncación N ────┘ └── truncación λ ──┘
```
- **ρ̂_n(λ,∞)** = n-ésimo cero del modelo λ-truncado con N→∞ (banda completa, primos ≤λ²).
- Límite N: completitud de Fourier/banda. Límite λ: horizonte + Euler. --- ## 2. Límite N (banda completa a λ fijo) — **[P], demostrable** **Proposición N.** Para λ fijo, ρ̂_n(λ,N) → ρ̂_n(λ,∞) con
`|ρ̂_n(λ,N) − ρ̂_n(λ,∞)| ≤ C(λ,n) · η^N`, algún η<1. **Demostración.** El cero ρ̂_n es raíz de la función secular
f_{λ,N}(s) = Σ_{|k|≤N} ξ_k/(s − 2πk/L), donde ξ es el autovector del menor autovalor de
Q_W (dimensión 2N+1). Q_W es una sección finita del operador de Weil A_λ sobre
PW_{L/2}. Por la teoría de secciones finitas de operadores con núcleo de
Plancherel–Pólya (el núcleo q(U_m,U_n) decae como 1/|m−n| fuera de la diagonal y la
forma es acotada en PW_{L/2}):
1. El menor autovalor y su autovector convergen: ‖ξ^{(N)} − ξ^{(∞)}‖ ≤ Cη^N (gap espectral ε₁−ε₀ = 3ε₀ > 0 ⟹ separación ⟹ convergencia geométrica del autovector, teorema de perturbación de Davis–Kahan).
2. f_{λ,N} → f_{λ,∞} uniforme en compactos ⟹ raíces convergen (Hurwitz, **acá sí es lícito**: es convergencia en λ FIJO, sin tocar la franja crítica del límite λ→∞). El gap ε₁−ε₀ = 3ε₀ > 0 (torre (k+1)², medido) da la separación espectral necesaria. ∎
(El único punto fino: que el decaimiento del núcleo 1/|m−n| basta para Plancherel–Pólya
en PW_{L/2}; es clásico para tipo exponencial. **[P] módulo tecnicismo estándar**.) **[!] Nota:** este límite es genuinamente incondicional. No toca los ceros de ζ; es
álgebra lineal + completitud de Fourier a λ fijo. --- ## 3. Límite λ: horizonte (banda) — el esqueleto unconditional **Proposición λ-banda.** Una vez T*(λ)=2πλ² > γ_n (i.e. λ > √(γ_n/2π)), el cero γ_n
está "dentro del horizonte" y ρ̂_n(λ,∞) lo resuelve con error
`|ρ̂_n(λ,∞) − γ_n|_banda ≤ C_band · R(λ,γ_n)`, donde R es el residuo de interpolación
band-limited a densidad crítica. **Estructura de la prueba (lo que SÍ es incondicional).**
- La densidad de ceros hasta T es N(T) ~ (T/2π)log(T/2π) (Riemann–von Mangoldt, **incondicional — cuenta ceros, no usa su posición**).
- La densidad de muestreo de PW_{L/2} es L/2π = (log λ)/π.
- Igualan en T* ~ 2πλ² (Lema 2). El modelo band-limited interpola exactamente hasta T*.
- El cero γ_n (γ_n < T*) cae en la zona de sobre-muestreo ⟹ se resuelve. La tasa la da la "sala" T* − γ_n. **[GAP] el residuo extremal de de Branges.** El valor preciso de
R(λ,γ_n) = ‖proyección band-limited residual‖ es la asintótica del producto canónico
truncado a tipo L/2 evaluado en γ_n. Numéricamente R ~ e^{−c(T*−γ_n)} ~ e^{−cλ²}
(c≈11, medido). La prueba precisa = teoría extremal de de Branges / Beurling–Selberg a
densidad crítica. **Este es el [GAP] honesto del término dominante.** Es clásico en
sabor, no elemental. **[!] Crucial:** este esqueleto usa SÓLO la densidad (conteo de ceros) y el muestreo, NO
la posición (parte real β) de los ceros. **El término de banda es incondicional.** --- ## 4. Límite λ: corrección Euler — **[!] donde el intento REVELA condicionalidad** El modelo usa primos ≤ λ². Falta la cola. El efecto sobre el cero ρ̂_n:
``` |ρ̂_n(λ,∞) − γ_n|_Euler ≈ |R_λ(½+iγ_n)| / |Ξ'(γ_n)|, R_λ(s) = −ζ'/ζ(s) − Σ_{n≤λ²} Λ(n) n^{−s}.
```
**[!] Y acá la prueba se topa con lo no esperado.** Por la fórmula explícita
(weil-remainder-attack §2):
``` R_λ(½+iγ_n) ~ Σ_ρ (λ²)^{ρ−½−iγ_n}/(ρ−s) = Σ_ρ (λ²)^{β−½} · (fase), β=Re ρ.
```
**La corrección Euler en un cero fijo γ_n está gobernada por TODOS los ceros ρ, vía
(λ²)^{β−½}.** Si todos β=½ (RH), es O(1) y la corrección es chica (consistente con el
piso <1e-19 medido). PERO un cero off-line ρ₀ con β₀>½ contribuye (λ²)^{β₀−½}, que CRECE. **⟹ El término Euler NO es incondicional: hereda la sensibilidad RH de R_λ.** **Régimen donde SÍ es incondicional:** para Re s ≥ 1+ε la serie de Euler converge
absolutamente, R_λ → 0 geométrico, **sin condición**. Pero ahí no hay ceros. La cola en
la recta crítica (donde viven los γ_n) es condicional. --- ## 5. Veredicto honesto del intento de prueba completa Al intentar probar E2-blando con máxima precisión, la estructura se separa así: | Pieza | Estado | Condicional? |
|---|---|---|
| Límite N (banda completa, λ fijo) | **[P]** (Davis–Kahan + Plancherel–Pólya) | **No** |
| Banda/horizonte (término dominante ~e^{−cλ²}) | **[GAP]** extremal de Branges | **No** (sólo densidad/conteo) |
| Corrección Euler en γ_n | explícita | **[!] Sí** (R_λ ~ Σ_ρ (λ²)^{β−½}) |
| Euler en Re s ≥ 1+ε | **[P]** | No (pero sin ceros) | **[!] Hallazgo del intento:** la separación "blando = incondicional / duro = RH" era
**casi** correcta, pero no del todo. Con precisión:
- El **esqueleto dominante** (límite N + banda/horizonte) **es incondicional** — usa conteo de ceros (densidad), no posición. Tasa ~ e^{−cλ²}.
- La **corrección Euler** sobre cada cero **es RH-sensible** (sub-dominante cuando RH vale, por eso el piso medido es <1e-19, pero no incondicionalmente acotada). **Lo que esto significa.** E2-blando se prueba INCONDICIONALMENTE **a orden dominante**
(banda/horizonte, módulo el extremal de de Branges), pero la convergencia al cero EXACTO
incluye una corrección Euler que hereda la condicionalidad de R_λ. La frontera
blando/duro es más fina de lo que pensábamos: ``` ESQUELETO (densidad/Nyquist): incondicional ← E2-blando genuino CORRECCIÓN (Euler en γ_n): RH-sensible ← donde se cuela lo duro
``` Esto **confirma y precisa** el reencuadre de tu colaborador: el Mundo B (convergencia)
tiene un esqueleto de aproximación pura (densidad/Nyquist) que NO toca posición de ceros
— ése es real e incondicional. Pero la *última corrección* (Euler en el cero) reintroduce
los ceros. **La buena noticia:** el esqueleto incondicional existe y es robusto; **la
honesta:** no es la convergencia al cero exacto, es la convergencia a "el cero módulo la
cola de Euler". --- ## 6. Qué queda, con precisión 1. **[GAP] cerrable (clásico):** el residuo extremal de de Branges para el término de banda. Cerraría el esqueleto incondicional ~e^{−cλ²} con constante.
2. **[!] RH-sensible:** la corrección Euler R_λ(½+iγ_n). Acotarla incondicionalmente con la fuerza necesaria = controlar (λ²)^{β−½} = regiones libres de ceros → RH-óptimo.
3. **Pregunta limpia que queda (para el upgrade duro, §3 de eslabon2-soft-theorem):** ¿el esqueleto incondicional (banda, densidad) basta para forzar la convergencia uniforme-en-franja, dejando la corrección Euler como perturbación controlable? Si la banda domina lo suficiente (e^{−cλ²}) sobre la corrección Euler ((λ²)^{β−½}), podría haber un argumento donde el esqueleto incondicional "gana" antes de que la corrección importe. **Ése es el próximo cálculo: comparar e^{−cλ²} (banda) vs (λ²)^{Θ−½} (Euler/posición) y ver si la banda domina para todo Θ<1.**
