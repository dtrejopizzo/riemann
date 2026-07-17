# Tribunal — Auditoría severa (lente) del intento de prueba de RH vía CCM **Referee:** C. (rol asumido) · **Objeto:** `RH-PROOF-FULL.md` + soportes
(`E2-nucleo-proof.md`, `N5-analytic-loewner.md`, `N5-subpieces-proved.md`,
`AUDIT-repairs-E1-III.md`, `AUDIT-repairs-norm-N5c-IV2.md`).
**Veredicto global de entrada:** NO se prueba RH. El documento ya lo admite. Mi trabajo es
verificar que la honestidad de la auto-auditoría es *suficiente* —y dónde aún sobre-afirma—,
y cerrar lo cerrable. Spoiler: la auto-auditoría es en su mayoría correcta y notablemente
honesta, pero hay **dos sobre-afirmaciones residuales** en el núcleo variacional (§2.6) que
hay que marcar, y el "lema del horizonte" tiene un **factor de densidad equivocado** que
invalida el conteo `#{γ_ρ≤T*}=dim` tal como está escrito. Lo arreglo abajo (Tarea 3). Cold honesty primero: el corazón es RH-equivalente, así que **ninguna cantidad de análisis
cierra la cadena**. Lo que SÍ se puede cerrar rigurosamente es el andamiaje y —parcialmente—
el lema de déficit de frame, con un residual explícito que vuelve a ser RH. Lo hago. --- ## TAREA 1 — Veredicto pieza por pieza Convención: **SOLID** = resiste auditoría como matemática (posiblemente módulo un clásico
citado honestamente); **GAP** = falta prueba, o la prueba escrita es falsa, o la afirmación
es RH-equivalente disfrazada. ### E0 — Construcción CCM, identidad `QW=`forma de Weil — **SOLID (con una salvedad)**
La definición (Def 0.1, núcleos de diferencia dividida de seno, diagonal con ventana de
Fejér) es correcta y la lectura Loewner (II.1–II.2 de `N5-analytic-loewner.md`) es limpia y
correcta: `QW` es superposición de matrices de Loewner de `sin` contra la medida de Weil
`μ_W = w_arch dy − Σ_{n'≤λ²}(Λ(n')/√n')δ_{log n'} + 𝒫`. **La salvedad de:** la
identidad `⟨ξ,QWξ⟩ = Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))` se afirma "exacta", y el texto añade
`A_λ = A_∞|_{E_λ}` "exacto (primos >λ² no contribuyen por soporte)". El **soporte-argumento
es correcto en estructura pero está mal contabilizado en el documento maestro** — ver Tarea 2,
donde muestro que la afirmación "primos >λ² contribuyen cero" es verdadera *para la parte
aritmética* pero la igualdad con `Σ_ρ` requiere además el término de polo `𝒫` y el
arquimediano, que NO se truncan y que el documento esconde en "+𝒫". La identidad como
*forma* es correcta (es la fórmula explícita de Weil restringida a `PW_Ω`); como *suma sobre
ceros con esos constantes exactos* tiene un detalle (factor y el `conj γ_ρ`) que audito
abajo. Veredicto: SOLID como definición y como forma de Weil; la frase "=Σ_ρ... exacto"
necesita la calificación de Tarea 2. ### E1 / H1 / H1′ — real-rootedness finita — **GAP (correctamente auto-flagged)**
La auto-auditoría es **correcta y honesta**, y aquí la firmo sin reservas: la prueba
registrada (interlacing con `ξ_k>0`) **es falsa**, y el contraejemplo `ξ=(−1,2,−1)`,
`d=(−1,0,1)` → `f(s)=−2/(s³−s)` (cero raíces reales) la refuta de forma terminal. El
autovector fundamental NO es de signo definido (carrier de borde `ω*≈0.966π`), de modo que
Perron–Frobenius **no** entrega la propiedad. La distinción H1 (PF ⟹ estructura/nodeless de
la *envolvente*) vs H1′ (`QW` PSD ⟺ Weil-positividad ⟺ RH-hasta-T*) es **exactamente la
corrección correcta**, y es la observación más importante de toda la auto-auditoría: *PF ≠
PSD*. Que H1 "probara QW PSD" habría probado RH; es imposible, y el documento ahora lo
reconoce. La real-rootedness es cierta empíricamente y se puede citar como CCM Thm 1.1(iii)
caja negra; prueba propia (Hermite–Biehler desde la realización auto-adjunta) **abierta**.
Severidad ALTA pero honestamente declarada. **GAP.** ### N0 — `Ξ_T→Ξ` strip-uniforme — **SOLID**
La cuenta es correcta y la firmo línea por línea. `Φ(u)≤Ce^{9u/2}e^{−πe^{2u}}` (doble-exp,
par) es clásica (Riemann/Pólya). El cambio `v=e^{2u}` da `Γ(7/4+δ/2, πλ²)` y la cota de la
Gamma incompleta `∫_X^∞ v^a e^{−πv}dv ≤ C X^a e^{−πX}` para `X` grande es estándar. Resultado
`C_δ λ^{5/2+δ}e^{−πλ²}` correcto. El corolario (la franja puede crecer hasta `o(λ²/logλ)`)
es correcto y notable. Pieza genuinamente probada, incondicional, sin mención de ceros.
**SOLID.** ### N1 — transfer eje→off-axis (medida armónica) — **SOLID*** (módulo Boas, clásico)
Lema 2 correcto. `w=log|F|−τ Im z` subarmónica, acotada superiormente en `H` por Boas Thm
6.2.4 (tipo exponencial + acotada en ℝ ⟹ `|F(z)|≤Γe^{τ|Im z|}`), dos-constantes + medida
armónica del segmento `ω_{[−R,R]}(iy₀)=(2/π)arctan(R/y₀)≥1−(2/π)(y₀/R)`. Todo correcto. El
único matiz: requiere que `F=δ̂` sea *acotada en todo ℝ* por `Γ`, no sólo en `[−R,R]`; eso lo
da N2. Encaja. **SOLID* (clásico citado honestamente).** ### N2 — amplitud global — **SOLID**
Dos versiones conviven: `Γ=O(logλ)` (Nikolskii/Plancherel–Pólya, `‖ξ̂‖²_{L²}=πlogλ`) y
`Γ=O(1)` con la normalización `ξ̂(0)=Ξ(0)`. Ambas correctas; la primera es la robusta y es la
que necesita N1 (`Γ^{1−ω}=exp(O(λ^{−2}loglogλ))→1`). La ortogonalidad de los `sinc_k` y
Parseval están bien. **SOLID.** (Observo que la mejora a `O(1)` *asume* `ξ̂_λ≈Ξ`, que es lo
que se quiere probar; por eso la versión load-bearing es la `O(logλ)`, que es incondicional.
Bien que el documento use ésa en la Reducción.) ### N3 — amplificación `λ^{y≤½}` — **SOLID*** (Boas/Phragmén–Lindelöf)
Bernstein/Boas estándar: tipo `τ`, acotada por `M` en ℝ ⟹ `|F(x+iy)|≤Me^{τ|y|}`. Da el
factor `λ^{1/2}` para `|y|≤½`. Correcto. **SOLID*.** ### Reducción (Teorema 2) — **SOLID, módulo E1**
`ξ̂_λ−Ξ=(ξ̂_λ−Ξ_T)+(Ξ_T−Ξ)`; segundo término `O(λ³e^{−πλ²})` (N0, δ=½); primero por N1 con
`R=T*~λ²` da `≲λ^{1/2}ε_loc`. La conclusión condicional "`ε_loc=o(λ^{−½}) ⟹ ξ̂_λ→Ξ` en
`|Im z|≤½` ⟹ (E1+Hurwitz) RH" es **lógicamente correcta**. Esta es la joya del programa: una
reducción limpia de RH a *un único número real medible*. Es honesta porque NO afirma probar
`ε_loc=o(λ^{−½})`. **SOLID** como implicación (módulo E1 para el paso Hurwitz). El valor real
del programa vive aquí. ### III — estabilidad relativa — **GAP (condicional; correctamente degradado)**
La forma absoluta de Davis–Kahan es inútil (`ε_1−ε_0≈3ε_0≈10^{−20}`); la renormalización
`Â=A/ε_0` la arregla *bajo (H-gap), (H-lim) y (H-pos)*. La auto-auditoría ya lo bajó a
teorema condicional, **y además detectó lo crucial**: `(H-pos) ε_0>0 = Weil-positividad-
hasta-T* ≈ RH-hasta-T*`. Es decir, la renormalización *lleva RH horneada*. Esto es correcto
y severo: III no es incondicional ni "casi". Las tres hipótesis son numéricas o RH. **GAP
condicional.** Bien declarado. ### N5b — borde absorbido — **SOLID (como reducción)**
El argumento VIII (`N5-analytic-loewner.md`) es correcto: el target `Ξ_T` es uniforme en `t`
incluyendo el borde (cota `L¹` de la cola de `Φ`, `|e^{itu}|=1`), y `|Ξ(t)|~e^{−πt/4}` suprime
el borde en sup-norma *absoluta*; la "capa de borde" de la numérica era error de *raíz*
(relativo), no de sup-norma. La distinción raíz-vs-sup es correcta y la firmo. **PERO** —
salvedad de — "el borde se disuelve" reduce N5b a `sup|ξ̂−Ξ_T|`, que es **§V = núcleo**.
No es que el borde desaparezca como problema; es que se *fusiona* con el núcleo. El documento
lo dice ("se absorbe en §V"). SOLID como reducción, no como cierre. ### N5c — discriminación β (RH-falso no converge) — **SOLID*** (módulo real-rootedness + conv-eje)
Lema de monotonía real-rooted `|g(x+iy)|≥|g(x)|` para `g∈\overline{LP}`: la prueba por
factorización de Hadamard (cada factor `|1−(x+iy)/r_n|²≥(1−x/r_n)²`, `r_n∈ℝ`) es **correcta**.
La Prop N5c.2 (DH con cero off-line `z₀`: `ε_loc^{off}≥|ξ̂_λ(z₀)|≥|ξ̂_λ(x₀)|→|Ξ_f(x₀)|>0`) es
correcta *módulo* (i) real-rootedness de `ξ̂_{f,λ}` (CCM auto-adjunta, vale para DH sin Λ≥0)
y (ii) convergencia en eje. **Una objeción de severidad:** el argumento asume `Ξ_f(x₀)≠0`
"porque la proyección real de un cero off-line no es cero on-line". Esto es genéricamente
cierto pero NO es un teorema: si `Ξ_f` tuviera un cero real *casualmente* en `x₀`, el bound
se vacía. Para Davenport–Heilbronn esto se verifica caso por caso (los off-line conocidos no
proyectan sobre ceros reales), así que el bound es no-vacuo *en los casos exhibidos*, pero la
frase general necesita esa verificación. Menor. **SOLID*** con esa nota. ### IV.1 — operador límite `Â_∞` — **GAP (análisis abierto)**
El espectro relativo medido `ε_k/ε_0→(k+1)²=n²` con paridad alternante `(−1)^k` es un *dato*,
no un teorema. Todas las identificaciones de coeficiente constante (Dirichlet, Hermite,
prolato, caja libre, totalmente-no-negativa) están **refutadas** según el propio documento.
La lectura "Sturm–Liouville 2º orden de coeficientes variables en la capa límite tras `/ε_0`"
es fenomenológica. Honestamente marcado como análisis (Landau–Widom / de Branges), no RH-hard.
Coincido: es cerrable *en principio* pero está abierto. **GAP.** Nota: `γ=3` (=2²/1²) está
sólo medido; (H-gap) de III depende de esto. ### IV.2 ≡ §V — el núcleo — **GAP RH-EQUIVALENTE (correcto, pero con dos sobre-afirmaciones residuales)**
Esta es la pieza que audito a fondo en Tarea 2. Veredicto: **RH-equivalente, correctamente
identificada como el núcleo.** No es conflación (`QW` ES la forma de Weil — esto lo verifico
y lo confirmo). Pero la cadena `min Σ|g(γ_ρ)|² ⟹ g se anula en {γ_ρ≤T*} ⟹ (horizonte:
#=dim) g₀=Ξ_T+O(déficit) ⟹ g₀→Ξ_T` contiene **dos pasos sobre-afirmados** que detallo en
Tarea 2 y reparo (parcialmente) en Tarea 3. **GAP RH-hard.** ### E3 — Hurwitz — **SOLID, módulo E1**
Clásico: límite uniforme en compactos de funciones LP es LP (los ceros no pueden migrar fuera
del eje sin que un cero real los persiga). Correcto, módulo que cada `ξ̂_λ∈LP` (=E1). **SOLID.** ### E4 — `Ξ∈LP ⟺ RH` — **SOLID (clásico)**
Definición de RH vía clase de Laguerre–Pólya; de Branges/clásico. **SOLID.** --- ## TAREA 2 — Escrutinio del núcleo variacional (§2.6) ### 2.A ¿Es `A_λ(g,g)=Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))` exactamente correcto? **Veredicto: correcto como FORMA de Weil, pero el documento maestro sobre-simplifica los
términos no-aritméticos, y el "exacto" merece tres correcciones de bookkeeping.** La fórmula explícita de Weil dice, para `g` test par adecuada con transformada `ĝ`:
``` Σ_ρ ĝ(γ_ρ) = ĝ(i/2)+ĝ(−i/2) [polo] − Σ_{n} (Λ(n)/√n)(g(log n)+g(−log n)) [primos] + (1/2π)∫ ĝ(r)[ψ-término arquimediano] dr [archimedean].
```
Reordenando, la "forma de ceros" `Σ_ρ ĝ(γ_ρ)` IGUALA (arquimediano + polo) − (aritmético).
El documento escribe `QW[m,n]=∫q w_arch − Σ_{n'≤λ²}(Λ/√n')q + 𝒫`. Esto es **el lado
derecho** (arquimediano − aritmético + polo). Por tanto: 1. **El "+𝒫" (polo de ζ) NO es un detalle decorativo.** Es `ĝ(i/2)+ĝ(−i/2)`, y es justamente el término que rompe la positividad ingenua: la forma de Weil es PSD *sobre el subespacio donde el término de polo está controlado* (test functions con `ĝ(±i/2)` absorbido). El documento lo mete dentro de "+𝒫" sin exhibir que su contribución cuadrática es la que hace que "QW PSD ⟺ RH" en lugar de un PSD trivial. La identidad `=Σ_ρ` es correcta **sólo si** el polo y el arquimediano están del lado-ceros; el texto lo afirma pero no lo desglosa. No es un error; es una sobre-compresión que oculta dónde vive la dificultad. 2. **El `conj(g(conj γ_ρ))` y los constantes.** Bajo RH `γ_ρ∈ℝ` y `conj γ_ρ=γ_ρ`, luego el término es `Σ_ρ|g(γ_ρ)|²` — correcto, suma de cuadrados, PSD. **Sin RH**, `γ_ρ` complejo y `conj(g(conj γ_ρ))` es el factor que hace la forma *hermitiana indefinida* (los pares de ceros `ρ, 1−ρ̄` aportan términos cruzados de signo indefinido). Esto está **correcto** y es la observación clave: la estructura `g(γ_ρ)conj(g(conj γ_ρ))` es exactamente la forma cuadrática de Weil cuya positividad ⟺ RH (Weil 1952, Bombieri). **El documento acierta aquí.** El único reparo de constantes: falta el factor de la multiplicidad/medida (cada cero entra con peso 1 sólo si son simples; la forma correcta lleva la densidad `d N(t)`), irrelevante bajo RH-simple pero a registrar. 3. **La restricción `A_λ=A_∞|_{E_λ}` exacta por "primos >λ² no contribuyen".** Esto es **correcto para la parte aritmética y SÓLO para ella**: `g=ξ̂` tiene soporte de transformada en `[−Ω,Ω]=[−logλ,logλ]`, y `g(log n')` se evalúa en `log n'`; para `n'>λ²`, `log n'>2logλ=L`... pero ¡ojo! el soporte de `g` es `Ω=logλ`, no `L=2logλ`. El argumento de truncación de primos en `n'≤λ²` usa `log n'≤logλ²=2logλ`, que es `L`, **no** `Ω`. Hay una **inconsistencia de factor 2** entre el soporte `Ω=logλ` de `ξ̂` y el corte de primos `n'≤λ²` (que corresponde a longitud `2logλ`). Reviso: los `q_{mn}(y)` se integran en `[0,L]` con `L=2logλ`, y el aritmético resta en `log n'∈[0,L]`, i.e. `n'≤e^L=λ²`. Consistente con `n'≤λ²`. Pero entonces el *soporte efectivo de la forma* es `L=2logλ`, mientras `ξ̂` es de tipo `Ω=logλ=L/2`. La auto-convolución `g⋆g̃` (que es lo que la forma de Weil evalúa en `log n'`) tiene soporte `2Ω=L`. **Resuelto: no hay error**, porque la forma de Weil evalúa la *autocorrelación* `g⋆ḡ` de soporte `2Ω=L=2logλ`, y por eso el corte natural es `e^L=λ²`. Bien. Pero el documento debería decir "primos `>λ²` no contribuyen porque la autocorrelación de `ξ̂` tiene soporte `2Ω=L`", no "por soporte" a secas. Con esa lectura, **el soporte-argumento es SOLID.** **Conclusión 2.A:** la identidad `A_λ(g,g)=Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))` es **correcta como
la forma cuadrática de Weil restringida a `PW_Ω`**, con los constantes/peso bien si los ceros
son simples y con el polo+arquimediano contabilizados en el lado-ceros. La frase "QW ES la
forma de Weil" **se sostiene** (no hay conflación). Lo confirmo como referee. ### 2.B ¿Es "ground state = Ξ_T ⟺ RH" riguroso? ¿Dónde se usa RH? **Veredicto: la EQUIVALENCIA con RH es correcta y rigurosa en una dirección y media; el paso
"el minimizador es exactamente Ξ_T" NO es riguroso tal como está, y ahí —no en la
equivalencia— está el handwaving.** Desglosando la cadena del documento: - **"Bajo RH la forma es `Σ_ρ|g(γ_ρ)|²≥0`."** Correcto y trivial (2.A.2). RH se usa aquí: `γ_ρ∈ℝ`. - **"Su minimizador band-limited se anula en `{γ_ρ≤T*}`."** Aquí está la **primera sobre-afirmación**. El minimizador de una forma PSD `Σ_ρ|g(γ_ρ)|²` sobre `PW_Ω` con `‖g‖=1` es el **autovector del menor autovalor** del operador de frame `S=Σ_{γ_ρ≤T*}K_{γ_ρ}⊗K_{γ_ρ}`, que en general **NO es cero** (la forma es estrictamente positiva si los `{K_{γ_ρ}}` generan `PW_Ω`). "Se anula en `{γ_ρ≤T*}`" sólo es posible si `dim PW_Ω > #{γ_ρ≤T*}`, i.e. si hay *más grados de libertad que nodos*. El documento invoca el "Lema horizonte: #=dim" precisamente para esto — pero entonces el espacio nulo tiene dimensión `dim−#=0` (¡si #=dim exactamente!), y `g₀=Ξ_T` NO está forzado: con `#=dim` el frame es una *base* (densidad crítica exacta) y el único `g` que se anula en todos los nodos es `g≡0`, no `Ξ_T`. **El conteo `#=dim` es justamente el caso límite donde el argumento se rompe**, no donde funciona. Lo discuto en Tarea 3. - **"(Lema horizonte: #=dim) g₀=Ξ_T+O(déficit)."** El `+O(déficit)` reconoce que NO es exacto a `λ` finito (`AUDIT-repairs-norm-N5c-IV2.md` §3 ya lo bajó de "exacto" a "límite"). Bien. Pero el mecanismo por el cual el déficit `ε_0~C₀/λ²` y por el cual el minimizador *converge a `Ξ_T` específicamente* (en vez de a cualquier otra función casi-nula) **no está probado**. Es la afirmación del lema de déficit de frame, que ataco en Tarea 3. - **"Sin RH la forma es indefinida, el minimizador se concentra en ceros off-line, ≠Ξ_T."** Correcto en espíritu (N5c lo formaliza por el lado de la *no-convergencia*, con cota inferior `|Ξ_f(x₀)|>0`). Esta dirección **sí está probada** (módulo real-rootedness + conv-eje), y es lo mejor del núcleo: el lado RH-falso es incondicional. **¿Dónde se usa RH, exactamente?** En DOS lugares, y son el mismo: 1. Para que `Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))=Σ|g(γ_ρ)|²≥0` (positividad de la forma) — esto es `ε_0≥0`, **= Weil-positividad-hasta-T* = RH-hasta-T*** (no la RH completa, sino el truncado a altura `T*~2πλ²`). 2. Para que el límite `ξ̂_∞=Ξ` a tasa `o(λ^{−½})` — el "puente" de la Reducción. Y aquí está la **segunda sobre-afirmación residual** que debo marcar: el documento dice
"ground state de Weil = Ξ_T ⟺ todos los γ_ρ reales ⟺ RH". La equivalencia
`ε_0≥0 ⟺ RH-hasta-T*` es correcta (es Weil). Pero "ground state = Ξ_T" como afirmación
*más fuerte* (no sólo `ε_0≥0` sino que el autovector ES `Ξ_T`) **no es equivalente a RH-
hasta-T***: es equivalente a RH-hasta-T* **más** un teorema de unicidad/rigidez del
minimizador que es el contenido de Landau–Beurling a densidad crítica (Tarea 3). La cadena
mezcla "la forma es PSD" (=RH local, correcto) con "el minimizador es la función de Riemann
truncada" (=RH local + rigidez de frame, más fuerte de lo declarado). El documento **lo dice
honestamente en una línea** ("módulo rigor del déficit de frame, Landau–Beurling") pero el
recuadro `ground state=Ξ_T ⟺ RH` es por tanto **ligeramente sobre-afirmado**: lo correcto es
`ε_0≥0 ⟺ RH-hasta-T*`, y `ground state=Ξ_T ⟸ RH-hasta-T* + rigidez de frame`. **Conclusión 2.B:** la pieza es genuinamente RH-equivalente (no hay truco, no hay
circularidad oculta más allá de la confesada). El handwaving NO está en la equivalencia
`ε_0≥0⟺RH-local` (esa es Weil, sólida) sino en el salto a "el minimizador es exactamente
`Ξ_T`", que requiere el lema de déficit de frame. Eso es lo único atacable sin tocar RH, y es
la Tarea 3. --- ## TAREA 3 — El lema de déficit de frame + reparación del lema del horizonte Aquí hago matemática, no auditoría. Objetivo: probar rigurosamente, con teoría de
Landau–Beurling/interpolación, qué exactamente satisface el minimizador `g₀`, y exhibir el
**residual exacto** que vuelve a ser RH. También reparo el conteo del horizonte, que está
**mal por un factor crítico** en el documento. ### 3.1 Reparación del lema del horizonte (el conteo está equivocado) El documento (E2-nucleo §3, "Lema del horizonte") afirma:
> "Ξ tiene `~N(T*)~(T*/2π)log T* ~ λ²·2logλ` ceros bajo el horizonte; `ξ̂` de tipo `logλ`
> tiene `~(logλ/π)·2T* ~ (2/π)λ²logλ` grados de libertad reales — **comparables**." **Esto no es correcto como igualdad `#=dim`.** Calculemos las dos cantidades con cuidado. **(a) Conteo de ceros (Riemann–von Mangoldt).** Hasta altura `T`,
``` N(T) = (T/2π)log(T/2π) − T/2π + O(log T).
```
Con `T*=2πλ²`:
``` N(T*) = (2πλ²/2π)log(2πλ²/2π) − λ² + O(logλ) = λ²·log(λ²) − λ² + O(logλ) = 2λ²logλ − λ² + O(logλ) ≈ 2λ² logλ.
```
Es decir **`#{γ_ρ: 0<γ_ρ≤T*} ≈ 2λ²logλ`** (y el doble, `~4λ²logλ`, contando `±`). Bien:
el `2λ²logλ` del documento es correcto para el conteo de un lado. **(b) Dimensión / densidad de muestreo de `PW_Ω`.** `ξ̂∈PW_Ω` con `Ω=logλ` (tipo exponencial
`logλ`). Por Nyquist/Landau, el número de grados de libertad de una función de `PW_Ω`
*observada sobre un intervalo de longitud `2T*`* (de `−T*` a `T*`) es la **densidad de Nyquist
× longitud**:
``` densidad de Nyquist de PW_Ω = Ω/π = logλ/π (muestras por unidad de longitud), DOF efectivos en [−T*,T*] = (Ω/π)·(2T*) = (logλ/π)·(4πλ²) = 4λ² logλ.
```
(El documento escribe `(logλ/π)·2T* = (2/π)λ²logλ`, perdiendo un factor `2π` por usar `2T*`
en lugar de la longitud correcta `2T*=4πλ²`, y arrastrando el `1/π`. Recalculo limpio:
longitud `=2T*=4πλ²`, densidad `=logλ/π`, producto `=4λ²logλ`.) **(c) Comparación correcta.** Ambos lados:
``` #{γ_ρ: |γ_ρ|≤T*} = 2·N(T*) ≈ 4λ²logλ − 2λ², DOF(PW_Ω sobre [−T*,T*]) ≈ 4λ²logλ.
```
**Coinciden al orden líder `4λ²logλ`**, con **defecto** `DOF − # ≈ +2λ² + O(logλ) > 0`. **Lema del horizonte (versión corregida).**
> El número de grados de libertad de `PW_Ω` sobre `[−T*,T*]` **excede** al número de ceros
> `#{|γ_ρ|≤T*}` por exactamente `≈ 2λ²` (el término `−T/2π` de Riemann–von Mangoldt),
> a orden subdominante respecto al líder común `4λ²logλ`. **Consecuencia (crítica para el déficit de frame):** la densidad de los nodos `{γ_ρ}` respecto
de la densidad de Nyquist de `PW_Ω` es
``` ρ(nodos)/ρ(Nyquist) = [4λ²logλ − 2λ²] / [4λ²logλ] = 1 − 1/(2logλ) < 1.
```
Es decir, **los ceros de Riemann muestrean `PW_Ω` ESTRICTAMENTE POR DEBAJO de la densidad
crítica de Beurling**, con déficit relativo `1/(2logλ)→0`. Esto es lo opuesto a "#=dim
exacto": hay un *underspanning* que tiende a crítico por abajo. Esta es la versión correcta,
y —importante— **es la que hace que el argumento de déficit de frame funcione** (ver 3.3): si
fuera exactamente crítico (#=dim) el frame sería una base de Riesz justa y el único vector que
se anula en los nodos sería `0`; con déficit `>0` hay un espacio "casi-nulo" de dimensión
`≈2λ²` donde vive el minimizador. ### 3.2 Marco preciso del minimizador Sea `Ω=logλ`, `H=PW_Ω` (Paley–Wiener, tipo `Ω`, `L²(ℝ)`), con núcleo reproductor
`K_γ(s)=sin(Ω(s−γ))/(π(s−γ))`, `⟨g,K_γ⟩=g(γ)`. Definimos el **operador de frame finito**
``` S_λ:= Σ_{|γ_ρ|≤T*} K_{γ_ρ} ⊗ K_{γ_ρ}: H → H, ⟨g,S_λ g⟩ = Σ_{|γ_ρ|≤T*} |g(γ_ρ)|².
```
Bajo RH-hasta-T* (los `γ_ρ` reales hasta `T*`), `S_λ⪰0` y el ground state band-limited es
``` g₀:= argmin_{‖g‖=1, g∈H} ⟨g, S_λ g⟩, ε_0:= λ_min(S_λ).
```
La afirmación del programa es: `g₀ → Ξ_T` y `ε_0→0` (déficit). Probémoslo con el residual
explícito. ### 3.3 Teorema de déficit de frame (progreso parcial honesto) **Teorema (déficit de frame, versión).** Sea `Ω=logλ`, `T*=2πλ²`, y supóngase
**RH-hasta-T*** (i.e. `{γ_ρ}_{|γ_ρ|≤T*}⊂ℝ`). Sea `m:=DOF−# ≈ 2λ²` el déficit del Lema 3.1.
Entonces: **(i) Cota superior del menor autovalor.** El espacio
``` V_λ:= { g∈PW_Ω: g(γ_ρ)=0 ∀ |γ_ρ|≤T* }
```
tiene `dim V_λ ≥ m ≈ 2λ² > 0` (porque imponer `#≈4λ²logλ−2λ²` condiciones lineales sobre un
espacio de dimensión `≈4λ²logλ` deja un núcleo de dimensión `≥m`). Para todo `g∈V_λ` no nulo,
`⟨g,S_λ g⟩=0`, luego
``` ε_0 = λ_min(S_λ) = 0 sobre V_λ (¡el mínimo es exactamente 0 en el subespacio nulo!).
```
*Comentario severo:* esto dice que el minimizador `g₀∈V_λ` se anula en TODOS los `γ_ρ≤T*`
**exactamente**, NO "con `O(déficit)`". El `O(déficit)` del documento es engañoso: con
underspanning estricto el mínimo de la forma *finita* es 0 exacto, no pequeño. El "déficit
`ε_0~C₀/λ²`" del documento NO es `λ_min(S_λ)` (que es 0) sino `λ_min` de la **forma de Weil
completa `QW`** (que incluye arquimediano+polo, no sólo `S_λ`). Son objetos distintos. **Esta
es una tercera imprecisión del documento:** confunde `λ_min(S_λ)` (=0, el frame de ceros puro)
con `ε_0=λ_min(QW)` (la forma de Weil completa, cuyo signo ES RH). El frame de ceros solo es
PSD-degenerado trivialmente; lo que tiene signo no-trivial es `QW`. **(ii) ¿Por qué `Ξ_T` y no otro elemento de `V_λ`?** Aquí está el núcleo. `Ξ_T∈V_λ`
**aproximadamente**: `Ξ` se anula exactamente en los `γ_ρ` reales (bajo RH), y `Ξ_T=Ξ+O(e^{−πλ²})`
uniforme (N0), luego `Ξ_T(γ_ρ)=O(e^{−πλ²})` para `|γ_ρ|≤T*`. Por tanto
``` ⟨Ξ_T, S_λ Ξ_T⟩ = Σ_{|γ_ρ|≤T*} |Ξ_T(γ_ρ)|² = #·O(e^{−2πλ²}) = O(λ²logλ · e^{−2πλ²}) = O(e^{−πλ²}).
```
Así `Ξ_T` es un cuasi-elemento del núcleo de `S_λ`. **PERO `V_λ` tiene dimensión `≈2λ²≫1`**:
hay un espacio enorme de funciones band-limited que se anulan en los ceros de Riemann. `Ξ_T`
es UNA de ellas; nada en `S_λ` solo la distingue. **La distinción la debe dar `QW` completo
(arquimediano+polo), no `S_λ`.** Es decir: el minimizador de `QW` (no de `S_λ`) es el que el
programa quiere, y `QW=S_λ−(arch+polo)` reordenado; la positividad de `QW` (=RH) es lo que
selecciona. **No hay forma de probar `g₀=Ξ_T` usando sólo el frame de ceros + densidad
crítica.** El residual es exactamente la positividad de la forma de Weil completa. **Residual exacto (lo que NO se cierra):**
``` g₀ = Ξ_T ⟺ Ξ_T minimiza QW (no S_λ) sobre PW_Ω ⟺ QW ⪰ 0 con ground state Ξ_T ⟺ Weil-positividad-hasta-T* con rigidez del minimizador = RH-hasta-T* (+ unicidad).
``` **Conclusión Tarea 3 (honesta).** El "lema de déficit de frame" **NO es cerrable por
Landau–Beurling/interpolación sola**, contra lo que el apéndice del documento sugiere
("Landau–Beurling cerraría g₀→Ξ_T"). Razón estructural: el frame de ceros `S_λ` tiene un
*núcleo de dimensión `≈2λ²`* (underspanning, Lema 3.1 corregido), y `Ξ_T` es sólo uno de
`≈2λ²` candidatos casi-nulos. La selección de `Ξ_T` requiere la forma de Weil *completa*
(arquimediano + polo), cuya positividad es RH-hasta-T*. **Lo que SÍ cerré rigurosamente:** 1. **El lema del horizonte corregido** (3.1): densidad de ceros / densidad de Nyquist `= 1 − 1/(2logλ) < 1`, underspanning estricto que tiende a crítico por abajo; defecto dimensional `m≈2λ²`. (El documento tenía el factor de longitud mal y afirmaba `#=dim`, que es falso; el régimen correcto es sub-crítico, no crítico.) 2. **La identificación del residual exacto**: `g₀=Ξ_T` es RH-hasta-T* más unicidad del minimizador de `QW`, NO una consecuencia de teoría de muestreo. Esto *refuta* la esperanza del Apéndice-2 ("déficit de frame ⟹ Landau–Beurling cierra g₀→Ξ_T") y la reclasifica como **RH-hard**, no como análisis cerrable. 3. **La distinción de objetos** `λ_min(S_λ)=0` (frame de ceros, trivial) vs `ε_0=λ_min(QW)` (forma de Weil, signo = RH). El documento los conflaciona en "déficit `ε_0~C₀/λ²`". **Progreso parcial positivo que SÍ es matemática real:** bajo RH-hasta-T*, `Ξ_T` *es* un
cuasi-elemento del núcleo de `S_λ` con residuo `O(e^{−πλ²})` (3.3.ii), y `dim V_λ≈2λ²`. Esto
significa que **si** además se prueba que `QW⪰0` (RH-local) **y** que su ground state es único
en `V_λ`, entonces `g₀=Ξ_T+O(e^{−πλ²})` con la tasa super-exponencial que el programa midió.
La tasa `o(λ^{−½})` requerida por la Reducción se seguiría holgadamente — *condicional a RH-
local*. No es un cierre; es la localización limpia del residual. --- ## TAREA 4 — Cerrable vs RH-hard **Genuinamente cerrable (análisis, no RH):**
- **N0, N1, N2, N3, Reducción (Thm 2), E3, E4**: ya sólidos (algunos módulo clásicos honestamente citados). No requieren trabajo.
- **Lema del horizonte**: lo cerré aquí corregido (3.1). Cerrado.
- **N5c (lado RH-falso)**: sólido módulo real-rootedness + conv-eje; la cota inferior `|Ξ_f(x₀)|>0` es correcta (verificar `Ξ_f(x₀)≠0` caso por caso para DH).
- **IV.1 (identificación del operador límite)**: análisis duro (Landau–Widom/de Branges), abierto pero no RH-hard. Cerrable en principio.
- **E1 propio (Hermite–Biehler desde la realización auto-adjunta)**: cerrable en principio (es teoría de de Branges/HB), pero NO trivial — la prueba registrada es falsa y la correcta está abierta. Riesgo medio. **RH-hard (no cerrable sin probar RH):**
- **H1′ (`QW` PSD = `ε_0≥0`)**: = Weil-positividad-hasta-T* = RH-local. RH-hard.
- **III (vía `/ε_0` con (H-pos))**: la renormalización asume `ε_0>0` = RH-local. RH-hard (la implicación condicional es correcta; las hipótesis no lo son).
- **IV.2 ≡ §V (`ξ̂_∞=Ξ`, tasa `o(λ^{−½})`)**: RH-equivalente. El núcleo.
- **El "déficit de frame" `g₀=Ξ_T`**: contra lo que el documento sugería, **lo reclasifico de cerrable a RH-hard** (Tarea 3): la selección de `Ξ_T` es RH-local + unicidad, no muestreo. Esta es mi corrección más sustantiva al estatus del programa. --- ## VEREDICTO FINAL () El documento **NO prueba RH y no lo reclama** — eso lo respeto. La auto-auditoría es, en su
mayoría, honesta y técnicamente correcta; las degradaciones de E1, III y H1′ son las
correctas, y la observación `PF≠PSD` es excelente. El andamiaje de aproximación (N0–N3,
Reducción) es matemática sólida y reutilizable; la reducción de RH a "un único número real
`ε_loc=o(λ^{−½})`" es limpia y valiosa. **Mis tres correcciones de referee al estatus declarado:**
1. **El lema del horizonte estaba mal contabilizado** ("#=dim"); lo correcto es underspanning sub-crítico, `densidad ceros/Nyquist = 1−1/(2logλ)`, defecto `≈2λ²`. Lo reparé.
2. **El "déficit de frame" NO es cerrable por Landau–Beurling** (como el Apéndice esperaba): `S_λ` (frame de ceros) tiene núcleo de dimensión `≈2λ²` y `Ξ_T` es uno de `≈2λ²` candidatos; la selección requiere la forma de Weil completa = RH-local. Reclasificado a RH-hard.
3. **El documento conflaciona `λ_min(S_λ)=0` con `ε_0=λ_min(QW)`** (el que tiene signo=RH). El "déficit `ε_0~C₀/λ²`" es del `QW` completo, no del frame de ceros. La RH-hardness está **distribuida** (H1′, `/ε_0`, IV.2, y ahora también el déficit de frame),
más de lo que el cuadro original admitía, pero menos catastróficamente de lo que un referee
hostil temería: no hay circularidad oculta ni conflación `QW≠Weil` (verifiqué que `QW` ES la
forma de Weil). El programa es una **localización honesta y precisa de RH en un núcleo
variacional Weil-positividad**, no una prueba. Cold honesty: el "corazón" no se mueve un
milímetro con análisis; es RH.
