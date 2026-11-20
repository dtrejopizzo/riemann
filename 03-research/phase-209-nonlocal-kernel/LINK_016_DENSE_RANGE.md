# LINK_016 — Rango denso del mapa011 sobre el portador par polar libre

2026-10-19. Constructor. **PROVED, revisión favorable en AUDIT_016.md:** en el parámetro crítico α=1/4, para cada T>0, el mapa U_T de LINK011 tiene rango denso en 𝓗_(1/4) cuando se restringe a F pares con momento cosh nulo. Lo mismo vale restringiendo el origen a un core suave.

Esto cierra, para ese mapa, el hueco «combinación firmada continua positiva sólo en su imagen» de015. No prueba que U sea inyectivo o sobreyectivo, no identifica V con todo el factor gaussiano y no obtiene signo para Q_T.

## 0. Corpus y diferencia escrita

Consultados las reglas del proyecto, índice ROUTES-TRIED-INDEX (Hamburger, Fourier anti, dominio015, LINK011–014), grid maestro y crucigrama base actual `05-meta-and-planning/ABCD-CLOSURE-PLAN/CROSSWORD-TO-D.md`. El archivo base reemplazó al nombre fechado; se verificó la entrada015.

Las rutas de identificación Hamburger/co-Poisson no se reabren como mecanismo de signo para D. **Razón nueva:** se calcula el anulador de la imagen del mapa011, cuyo dominio y kernel ya están fijados. La ecuación de Fourier aparece como consecuencia de ese anulador, y se usa sólo para probar densidad. El resultado responde una pregunta concreta que no se deducía de015: positividad en la imagen frente a positividad en todo el espacio. No se propone otra forma positiva ni una FE «con defecto» como prueba del nodo.

## 1. Objeto exacto y enunciado

Fijar α=1/4, s=1/2. En 𝓗=𝓗_(1/4), escribir

`f_d=X_d−1/d`, `||f_d||²=S(d,d)=O(d^(−1/2))`, d≥2.

Su span es denso por la definición de 𝓗 como completación del álgebra Haarcentrada. El mapa conservado es

`U_TF=Σ_(d≥2)a_d(F)f_d`,

`a_d(F)=2∫_(−T)^T F(x)e^(x/2)[τ(d²exp(2x))−τ(exp(2x))/d]dx`.

LINK011 probó convergencia absoluta en norma y acotación desde L²([−T,T]). Definir

`𝒫_T^ev={F∈L²([−T,T]):F(−x)=F(x), ∫F(x)cosh(x/2)dx=0}`.

**Teorema 1.** Para todo T>0,

`closure U_T(𝒫_T^ev)=𝓗`.                            (1)

Se permite complejificar los espacios; la afirmación real se obtiene del mismo argumento sobre sus partes reales.

## 2. Anulador del rango y su función analítica

Usar producto interno lineal en el primer argumento. Sea h∈𝓗 ortogonal a U_T(𝒫_T^ev). Poner

`η_d=⟨f_d,h⟩`, `c=Σ_(d≥2)η_d/d`.

Cauchy–Schwarz y la cota de diagonal de011 dan

`|η_d|≤C||h||d^(−1/4)`;

por ello la serie que define c converge absolutamente. La identidad del mapa y su convergencia permiten escribir

`⟨U_TF,h⟩=∫_(−T)^T F(x)b_h(x)dx`,

`b_h(z)=2exp(z/2)[Σ_(d≥2)η_d τ(d²exp(2z))−cτ(exp(2z))]`. (2)

La función b_h es holomorfa en la franja `|Im z|<π/4`: allí Re(exp(2z))>0, y en cada compacto de la franja las series gaussianas y la suma en d convergen uniformemente con todas sus derivadas.

El anulador en el subespacio par de la condición de momento único es el span de cosh(x/2). Por tanto existe λ∈C con

`[b_h(x)+b_h(−x)]/2=λcosh(x/2)`

para casi todo x∈(−T,T). Ambas partes son analíticas; la igualdad es puntual y el principio de identidad la extiende a toda la franja, en particular a todo x real.

## 3. Distribución aritmética de coeficientes explícitos

Definir una distribución par, puramente atómica y sin derivadas de deltas:

`μ=Σ_(n∈Z\{0}) a_|n| δ_n`,

`a_n=Σ_(d|n,d≥2)η_d−c`, `μ({0})=0`.

Los coeficientes tienen crecimiento polinomial: basta la cota |η_d|≤C y el hecho de que el número de divisores es ≤n. Por tanto μ es una distribución temperada par. Su transformada gaussiana es, para y>0,

`Θ_μ(y):=⟨μ,exp(−πy·²)⟩`

`=Σ_(d≥2)η_dτ(d²y)−cτ(y)`.

Las sumas dobles son absolutamente convergentes; (2) da

`b_h(x)=2y^(1/4)Θ_μ(y)`, `y=exp(2x)`.

La identidad par del apartado anterior equivale exactamente a

`Θ_μ(y)+y^(−1/2)Θ_μ(1/y)=(λ/2)(1+y^(−1/2))`, y>0. (3)

El factor λ/2 es importante. Definir

`μ′=μ−(λ/2)δ_0`.

Entonces (3) queda

`Θ_(μ′)(y)+y^(−1/2)Θ_(μ′)(1/y)=0`.                 (4)

## 4. Inyectividad gaussiana en distribuciones temperadas pares

Se incluye el argumento para no suponer una unicidad de medidas que no cubra distribuciones.

**Lema 2 (PROVED).** Si ν es temperada par y `⟨ν,exp(−πy·²)⟩=0` para todo y>0, entonces ν=0.

**Prueba.** Derivar en y en y=1 es legítimo en la topología de Schwartz. Se obtiene

`⟨ν,x^(2k)exp(−πx²)⟩=0`, k≥0.

Los momentos impares correspondientes también son cero por paridad. La función

`G(z)=⟨ν,exp(−πx²+zx)⟩`

es entera: en cada compacto de z, la gaussiana domina uniformemente todos los seminormas de Schwartz y permite derivar. Todos sus coeficientes de Taylor en0 son cero, así que G≡0.

Para z puramente imaginario, G es la transformada de Fourier de la distribución `exp(−πx²)ν`, representada por una función suave de crecimiento a lo sumo polinomial en el eje real. La igualdad también se verifica por dualidad contra tests de Schwartz; el intercambio está justificado por la continuidad temperada. Inyectividad de Fourier da `exp(−πx²)ν=0`.

Para cualquier test compacto φ, `exp(πx²)φ` es otro test compacto, de modo que ν(φ)=0. Luego ν=0 como distribución, y por continuidad temperada también en Schwartz. ∎

Tomar la convención Fourier `exp(−2πixξ)`. La dualidad y la transformada exacta de una gaussiana dan para toda distribución temperada

`Θ_(𝓕ν)(y)=y^(−1/2)Θ_ν(1/y)`.

Como μ′ es par, también lo es `μ′+𝓕μ′`. De (4) y el Lema2:

`𝓕μ′=−μ′`.                                        (5)

No interviene una fórmula explícita con ceros.

## 5. Atomicidad entera y el signo Fourier obligan a anulación

μ′ es una suma de **deltas puras en enteros**, con coeficientes de crecimiento polinomial. Su Fourier es una distribución1-periódica: cada delta δ_n se transforma en exp(−2πinξ), y la serie se interpreta temperadamente.

Por (5), μ′ también es1-periódica. Comparar sus masas en n y n+1 obliga a que todos los coeficientes sean una misma constante C, incluido el de0. Por tanto

`μ′=CΣ_(n∈Z)δ_n`.

En y=1, (4) da `Θ_(μ′)(1)=0`. Pero esa cantidad es `Cθ(1)` y θ(1)>0. Así C=0, y μ′=0.

Como μ tenía coeficiente0 nulo, la masa de μ′ en0 es −λ/2; luego λ=0. Se obtiene μ=0. En n=1, su coeficiente a_1 es −c, por lo que c=0. Entonces

`Σ_(d|n,d≥2)η_d=0` para cada n≥2.

Inducción en n da η_n=0: todos los divisores propios ya tienen coeficiente nulo. Así h es ortogonal a cada f_d; por densidad de su span, h=0. Esto prueba (1).

La restricción a deltas puras es parte de la prueba: no se ha afirmado una clasificación general de todas las distribuciones soportadas en Z con posibles derivadas de deltas.

## 6. Core suave y consecuencias para las formas firmadas

El espacio par C_c∞((−T,T)) con momento cosh nulo es denso en 𝒫_T^ev en L². Se aproxima por tests pares suaves y se corrige el momento con un test fijo de momento no nulo. Como U_T es acotado, su imagen también tiene clausura 𝓗. Por tanto la densidad no depende de permitir tests discontinuos ni de usar todo L² sin core.

Sea B una forma hermítica **continua en la norma de 𝓗**. De (1),

`B(U_TF)≥0 para todo F∈𝒫_T^ev`

`⇔ B(h)≥0 para todo h∈𝓗`.                           (6)

La dirección no trivial es continuidad y aproximación por el rango denso. Esto vale ya para una sola ventana T>0.

En particular, para una combinación real fija de las tres piezas de015,

`B_(a,b,c)=aκG_s+bκvv*+cΠ`,

positividad sólo en la imagen par polar libre de011 es equivalente a PSD global; por CONSTRUCTOR015 ocurre exactamente si a,b,c≥0. El hueco de combinaciones firmadas continuas en ese span, positivas únicamente en esa imagen, queda cerrado.

Con LINK014, ninguna combinación fija no nula de ese span que sea positiva en la imagen puede proporcionar una dominación uniforme positiva por Q_T usando el mismo mapa011. No se deduce esa conclusión para coeficientes dependientes de T sólo de014.

## 7. Límites precisos

- El resultado es exclusivo del mapa011, α=1/4 y sus tests pares polar libres; no se extiende a cualquier mapa que use −R.
- La prueba usa todos los modos del espacio par polar libre, o su core denso. No afirma densidad para la imagen de un bloque canónico finito E_N(T), ni permite inferir PSD global de positividad sólo en ese bloque.
- Rango denso no significa sobreyectividad, inyectividad ni una inversa acotada. La compacidad probada en011 no contradice la densidad.
- No se excluyen formas no continuas en la norma de 𝓗, cambios de mapa, otros kernels ni factores dependientes de T.
- No se identifica V con todo ℒ_α ni se prueba que la inversión gaussiana preserve V.
- No se obtiene igualdad, dominación ni signo del resto de Q_T. La densidad no transforma el kernel auxiliar en el nodo.

**Estado:** rango denso y cierre del hueco de positividad continua en la imagen PROVED, auditoría favorable en AUDIT_016.md. D permanece OPEN y activo; ningún paper modificado.
