# Ataque analítico a la desigualdad (1): ¿qué es δV, exactamente? Matemática pura sobre el último GAP de la cascada. Sin saltear pasos.
**[P]** probado · **[O]** abierto · **[!]** conclusión que hay que decir clara. --- ## 1. Las dos definiciones de V₀ y su acuerdo a orden líder La cascada define **V₀ = Kφ₀/φ₀** (potencial de estado fundamental, lado FLS).
Por otro lado, el **promedio PNT del pozo de primos** es otro objeto. Veamos que
coinciden a orden líder. **Promedio del pozo.** El pozo es V_λ = Σ_{n≤λ²} (Λ(n)/√n) · [masa en u=log n].
Para una función test suave f, por PNT (Σ_{n≤x} Λ(n) ~ x):
``` Σ_n (Λ(n)/√n) f(log n) ≈ ∫ (1/√x) f(log x) dx [x=e^u, dx=e^u du] = ∫ e^{u/2} f(u) du.
```
⟹ **El promedio suave del pozo de primos es la densidad e^{u/2} du** — que es
exactamente el peso del funcional-polo ℓ. **[P]** (es PNT). **Acuerdo.** A orden líder vale la balanza de Weil Kφ₀ ≈ V_λ φ₀ (es la cancelación
c=2). Luego V₀ = Kφ₀/φ₀ ≈ (V_λ aplicado a φ₀)/φ₀ ≈ promedio suave de V_λ = e^{u/2}.
**⟹ V₀ ≈ e^{u/2} (la media PNT), a orden líder.** Consistente con φ₀ = modo-polo. --- ## 2. Entonces δV es la FLUCTUACIÓN de los primos — y eso son los ceros ``` δV = V_λ − V₀ ≈ Σ_{n≤λ²}(Λ(n)/√n) δ_{log n} − e^{u/2} du = (medida de primos) − (su media PNT) = TÉRMINO DE ERROR del PNT.
``` Por la **fórmula explícita de Riemann–von Mangoldt**, el término de error del PNT
es una suma sobre los ceros:
``` ψ(x) − x = − Σ_ρ x^ρ/ρ − log(2π) − ½log(1−x^{−2}).
```
Pasando a la fluctuación de Λ(n)/√n (sumación de Abel, como en
weil-remainder-attack §2):
``` δV(u) ~ − Σ_ρ e^{(ρ−½)u} / ρ + (suave).
``` **[!] δV NO es un objeto "de densidad pura": su parte oscilatoria ES la suma sobre los
ceros Σ_ρ.** La media (e^{u/2}) es densidad; la fluctuación es posición. El audit había
marcado este riesgo ("δV podría retener un eco de Σ_ρ") — al hacer la cuenta, **el eco
es la fluctuación entera**. --- ## 3. La cota que necesitamos, y su tamaño Necesitábamos: ∫ δV |g|² ≤ β_λ ‖g‖² sobre ℓ^⊥, g band-limited de tipo L=2logλ. Para g band-limited, |g|² es suave con transformada soportada en [−L, L]. El
emparejamiento con la suma de ceros:
``` ∫ δV |g|² ~ − Σ_ρ \widehat{|g|²}(ρ)/ρ (proyectado a ℓ^⊥, sin el polo s=1).
```
La ventana band-limited sólo "ve" ceros bajo el horizonte γ_ρ ≲ λ² (Lema 2). Sobre
la recta crítica el módulo de cada término es
``` | e^{(ρ−½)u} | = (λ²)^{β−½}, β = Re ρ.
```
⟹ **la cota es del orden (λ²)^{Θ−½}, con Θ = sup_ρ Re ρ.** - **Θ = ½ (RH):** la fluctuación es O(1)·(suave) → δV ≪ β_λ, (1) cierra. Pero Θ=½ **es RH**.
- **Incondicional:** sólo Θ ≤ 1, dando (λ²)^{½} = λ → **δV puede ser ≫ β_λ ~ λ^{−2}.** **[!] La cota de δV es RH-equivalente en fuerza.** Es exactamente el mismo muro
(Θ=½) que ya apareció en weil-remainder-attack (el resto R_λ) y en la constante c=2
del Objetivo A. **La esperanza "δV es lado densidad" (audit §2) era optimista: al
calcularlo, la fluctuación es el sum-over-zeros.** --- ## 4. ¿La proyección a ℓ^⊥ o el suavizado salvan algo? Tres intentos de escape, los tres honestamente fallan: - **Proyección a ℓ^⊥:** sólo remueve el polo s=1 (la media), no las oscilaciones de los ceros. La fluctuación vive en ℓ^⊥. No ayuda.
- **Suavizado band-limited:** limita la suma a γ_ρ ≤ horizonte, pero cada cero bajo el horizonte sigue aportando (λ²)^{β−½}. No mata la dependencia en β.
- **Densidad de ceros (no regiones libres):** los teoremas de densidad (Selberg, Bohr–Landau) dicen que *casi todos* los ceros están cerca de la línea — controlaría δV en promedio. PERO un **único** cero fuera de línea ρ₀ bajo el horizonte permite construir g concentrada en γ₀ con A_λ(g,g) < 0. La positividad es sensible a ceros **individuales**, no al promedio. ⟹ densidad no alcanza. --- ## 5. Veredicto honesto del ataque con matemática pura **[!] La desigualdad (1), atacada con la fórmula explícita, es RH-hard.** δV es el
término de error del PNT = la suma sobre los ceros; su cota es (λ²)^{Θ−½}, ajustada en
Θ=½ = RH. La proyección a ℓ^⊥ y el suavizado no rompen la dependencia en la posición
de los ceros, y la sensibilidad a ceros individuales bloquea el argumento de densidad. **Esto NO contradice los avances previos — los precisa:**
- **[P]** Schur + FLS son correctos: la no-localidad se resolvió, el déficit se aisló al modo-polo, el complemento tiene margen 4× (Brezis–Vázquez real).
- **[!]** Pero el residuo aislado (δV sobre ℓ^⊥) **es** la positividad de la fórmula explícita = RH. La cascada **localiza el muro con una limpieza sin precedentes** (una única cota de fluctuación de primos), pero **no lo atraviesa**. ### Lo que esto significa para la estrategia La cascada es la **mejor reducción disponible**, pero su último eslabón es RH-equivalente,
no PNT-derivable. El "lado densidad" de δV (audit §2) era la media (e^{u/2}); el contenido
RH es la fluctuación, y la fluctuación son los ceros. **El muro Θ=½ es el mismo de
siempre, ahora con la mejor localización del programa.** **Honestidad (lección repetida):** igual que con "ε₀ density vs position", la cuenta
explícita muestra que el objeto candidato a no-circular contiene, al calcularlo, la
información de los ceros. No es un fracaso del programa CCM (que es sólido y dio
resultados incondicionales reales) — es que **la positividad de Weil localizada es
RH-equivalente, y ningún reagrupamiento (Schur, FLS, polo) cambia eso**: trasladan el
muro, lo aíslan limpio, pero el muro es la fluctuación de primos = Σ_ρ. --- ## 6. Lo que queda genuinamente abierto (sin auto-engaño) 1. **¿Hay ALGÚN funcional de δV que sea insensible a ceros individuales y aún suficiente?** (Improbable: positividad ⟺ sin ceros off-line ⟺ sensible a individuales.)
2. **La pieza incondicional real:** todo lo que NO es la cota de δV — Eslabón 1, FLS, improved-Hardy structure, ε₀^frame ~ C₀/λ² — son teoremas genuinos del lado densidad. El programa los entrega; RH (la fluctuación) queda fuera de alcance no-circular. **Veredicto final del frente analítico:** atacado con todo el poder (Schur exacto, FLS
clásico, fórmula explícita), el Eslabón 2 se reduce a una única cota de la fluctuación de
primos sobre ℓ^⊥, y esa cota es RH-equivalente (Θ=½). El programa CCM da la localización
más limpia conocida del muro, no su demolición.
