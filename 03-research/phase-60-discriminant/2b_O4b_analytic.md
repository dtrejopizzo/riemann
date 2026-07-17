# O-4b: derivación analítica del operador efectivo 𝓛 (en progreso, con marcadores) Meta (reformulación): identificar 𝓛 = lim (1/ε_0)A_λ. Método: dejar que el operador
revele su ecuación, derivando desde A_λ = M_θ − V en coordenada w (luego x=w/L). ## Paso 1 [DERIVADO] — el segundo orden viene de M_θ, coeficiente exacto Símbolo arquimediano Ω(t) = −logπ + Re ψ(¼+it/2). Por la representación de Lévy (probada en
H1): Ω(t) − Ω(0) = ∫_0^∞ (1−cos tξ) dν(ξ), dν(ξ)=2e^{−ξ/2}/(1−e^{−2ξ})dξ ≥ 0. Sobre modos semiclásicos (suaves en escala L; frecuencia t ~ (k+1)/L → 0), 1−cos(tξ)≈½(tξ)²: Ω(t) ≈ Ω(0) + (C_2/2) t², C_2 = ∫ξ² dν(ξ).
Multiplicar por t² ES −d²/dw². Por tanto: **M_θ ≈ Ω(0) I + c (−d²/dw²), c = C_2/2 = −ψ''(¼)/8 = 16.16597… (exacto).**
Verificado: C_2 (integral de Lévy) = −ψ''(¼)/4 = 32.33193498 (coinciden 12 díg). c>0 ⟹ elíptico. **Este es el origen analítico, no impuesto, del operador de 2º orden.** El coeficiente es un
valor especial de ψ. [Riguroso para M_θ sobre modos suaves.] ## Paso 2 [ESTRUCTURAL] — la frontera es esencial; el potencial nace de los primos Expansión análoga de V f(w)=Σ_{n≤λ²}Λ(n)n^{−1/2}[f(w−log n)+f(w+log n)] para f suave daría V ≈ 2P_λ I + Q_λ d²/dw², P_λ=Σ Λ(n)/√n ~ 2λ → ∞ (PNT).
⟹ A_λ tendría constante Ω(0)−2P_λ → −∞, **contradiciendo A_λ ≥ 0**. La expansión bulk FALLA. **Resolución:** las traslaciones por log n grande **salen del soporte** [−L/2,L/2]; la frontera
las trunca. Por eso (a) los modos son edge-localized; (b) el problema es de CAPA LÍMITE; (c) el
término de primos efectivo es **w-dependiente**: el conjunto {n: w±log n ∈ soporte} depende de
w. Cerca del centro w=0 (u=1) caben más primos (simétrico) ⟹ **acumulación ⟹ potencial W(w)
singular en el centro** = la singularidad central observada (reveal_L.py: V→∞ en x=0). ## Forma efectiva conjeturada (a derivar en Paso 3) 𝓛 ∝ (c) (−d²/dx²) + W(x), W(x) singular en x=0 (centrífugo/Bessel),
en x=w/L ∈ [−½,½]. El 2º orden [Paso 1, derivado]; W de la suma de primos truncada por
frontera [Paso 2, estructural]; espectro (k+1)² y escala ε_0~e^{−L} salen del balance
arquimediano↔primos (= fórmula explícita de Weil), residual = horizonte (Lema 2). ## Paso 3a [DERIVADO + VERIFICADO] — la ley aritmética de frontera N_λ(w) (Narrowing de: derivar primero el conteo de traslaciones permitidas desde w.) Soporte I=[−L/2,L/2]=[−logλ,logλ]. Condiciones w±log n ∈ I ⟺ n ≤ λe^{−|w|} (< λ², no binding).
Por sumación parcial con ψ(t)~t (PNT): Σ_{n≤X}Λ(n)/√n = 2√X − 1 + o(1) ~ 2√X. Con X=λe^{−|w|}: **N_λ(w) = Σ_{n≤λe^{−|w|}} Λ(n)/√n ~ 2√(λe^{−|w|}) = 2λ^{1/2−|x|}, x=w/L ∈[−½,½].** VERIFICADO numéricamente: ratio N_λ/(2λ^{1/2−|x|}) → 1 cuando λ→∞ (λ=50,200,1000 da 0.82,0.93,
0.96 en x=0; converge para cada x, más lento en x grande por subdominantes). DERIVADO de PNT. Refina la conjetura F(x)·λ: es **λ^{1/2−|x|}** (exponente variable). Explica:
- centro x=0: N~2√λ máximo ⟹ barrera ⟹ singularidad central.
- borde x=±½: N~O(1) mínimo ⟹ localización de borde. **Naturaleza:** N_λ(w) es la fuerza de HOPPING (peso total de traslaciones) desde w — término
cinético posición-dependiente, NO un potencial directo. ⟹ 𝓛 es Sturm–Liouville de coeficiente
variable −(p(w)u')'+… con p(w) ligado a N_λ(w), no −∂²+V con V=N_λ. (Consistente con:
"muchos −(pu')'+q dan espectro cuadrático".) ## Paso 3b [DERIVADO + corrección honesta]: momentos M_0,M_2 y la NO-LOCALIDAD (: computar momentos 0 y 2 de las traslaciones permitidas antes de identificar 𝓛.) M_0(w)=Σ_{n≤X}Λ(n)/√n ~ 2√X = 2λ^{1/2−|x|} (verificado, ratio→1).
M_2(w)=Σ_{n≤X}Λ(n)/√n(log n)² ~ 2√X(log X)² = 2λ^{1/2−|x|}(logλ)²(1−2|x|)² (verificado).
⟹ M_2/M_0 ~ (log X)² = (logλ)²(1−2|x|)². **Ambos con la geometría λ^{1/2−|x|}** (hope de ✓). **PERO la expansión local FALLA [corrección]:** el 85% del peso de V está en hops GRANDES
(log n > ½ log X), no pasos chicos. ⟹ Taylor f(w±log n)≈f+½h²f'' INVÁLIDA ⟹ **V es NO-LOCAL**,
NO el operador diferencial M_0+M_2∂². Tercera corrección conceptual (tras capa-fija y tunneling). **Distinción firme:**
- M_θ SÍ localizable: medida de Lévy con 2º momento finito C_2 (domina ξ→0) ⟹ c(−∂²) riguroso.
- V (primos) NO localizable: domina hop grande ⟹ operador NO-LOCAL. ⟹ **𝓛 = c(−∂²) − V_nonlocal** (cinético local vs término no-local de primos). El espectro
(k+1)² emerge de esa competencia, NO de una ODE local. Marco correcto: **no-local
(sampling / de Branges, P7/P8)**, no ecuación diferencial. Los momentos M_0,M_2 (geometría
λ^{1/2−|x|}) son los datos, pero la identificación de 𝓛 es como operador no-local. ## Paso 3c [MECANISMO + núcleo abierto] — confinamiento no-local ⟹ Dirichlet (k+1)² Mecanismo unificador: 𝓛 = c(−∂²) − V_nonlocal, con V_nonlocal ~ M_0(w)~2λ^{1/2−|x|} ENORME en
el bulk/centro, O(1) en el borde. V_nonlocal **confina** (mata modos donde M_0 grande) ⟹ impone
**Dirichlet efectivo** en la frontera de la región-soporte. ⟹:
- (k+1)² RELATIVO = espectro del cinético LOCAL c(−∂²) con esas BC Dirichlet (2º orden de M_θ, V sólo confina). Paridad alternante = autofunciones Dirichlet. Singularidad central = M_0 máx en x=0 ⟹ nodo. Localización de borde = modos donde M_0~O(1). TODO reconciliado. **Núcleo abierto (= missing step de), 2 asintóticas:**
- (3c-a) probar que el confinamiento no-local da EXACTAMENTE el espectro Dirichlet (k+1)².
- (3c-b) probar que el residual de muestreo (Lema 2) da ε_0 ~ e^{−L} con S=1. (La escala e^{−L} NO sale del confinamiento simple —ancho W~1/logλ daría autovalores crecientes en L— sino del residual del muestreo más allá del horizonte; mecanismo distinto.)
Ambas = asintótica de Branges/concentración, nivel investigación. NO fabricadas. ## SÍNTESIS HONESTA (tras todas las rondas)
Reducción lograda: RH ⟸ Eslabón 2 ⟸ (i) exacto + (ii) (1/ε_0)A_λ→𝓛, 𝓛 caracterizado con
coeficientes DERIVADOS: cinético c=−ψ''(1/4)/8, potencial aritmético no-local M_0~2λ^{1/2−|x|}
(PNT), horizonte T*~2πλ². El núcleo abierto: 2 asintóticas (3c-a),(3c-b) de un operador no-local
explícito. Convertimos "falta convergencia" (vago) en "faltan 2 asintóticas concretas con todos
los ingredientes derivados". Reducción real/publicable; el cierre es investigación genuina. ## Paso 4 [DERIVADO] — descomposición de Beurling–Deny (marco de Objetivo A,) Reorganización (): atacar EQUIVALENCIA DE FORMAS c₁𝓔_D≤A_λ≤c₂𝓔_D, no el espectro directo;
el espectro (k+1)² viene después por Mosco/Γ-convergencia. Usando la rep. de Lévy de M_θ (H1) y 2∫f(w)f(w+h)dw=2‖f‖²−∫|f(w)−f(w+h)|²: A_λ(f,f) = ∫(Ω(0)−2M_0(w))|f|²dw + 𝓔_θ(f) + 𝓔_prime(f), [RIGUROSO] - q(w)=Ω(0)−2M_0(w): potencial, M_0~2λ^{1/2−|x|} (PNT), pozo profundo máx en centro.
- 𝓔_θ(f)=½∫∫|f(w+ξ)−f(w)|²dν(ξ)dw ≥0 (salto arquimediano, ν de H1).
- 𝓔_prime(f)=Σ_n Λ(n)/√n ∫|f(w)−f(w+log n)|²dw ≥0 (salto de primos).
Dos formas de Dirichlet no-locales positivas + pozo aritmético. A_λ≥0 ⟺ saltos compensan pozo. **Cota superior [PROBADA]:** 𝓔_θ(f) ≤ C_2 ∫|f'|² (de ∫ξ²dν=C_2<∞ + Cauchy–Schwarz). ⟹ parte
arquimediana ≤ C_2·𝓔_Dirichlet. **Objetivo A [ABIERTO, bien enmarcado]:** cota inferior de forma + control de 𝓔_prime (no-local)
contra 𝓔_D efectiva en la región de borde ⟹ equivalencia de formas ⟹ (vía Mosco) espectro
(k+1)². = teoría de formas de Dirichlet / de Branges. Localizado, riguroso, no cerrado. **Objetivo B [ABIERTO]:** ε_0~e^{−L} = mínimo residual de f∈PW_{L/2} forzada a anularse en los
ceros hasta T*~2πλ² = problema extremal de Beurling–Selberg/de Branges. Localizado. ## (resto: identificación detallada del operador no-local) Derivar W(w) explícito = la suma de primos resuelta por la frontera (qué primos "caben" en
cada w), y mostrar que el bottom del operador resultante da ε_0 ~ e^{−L} con espectro relativo
(k+1)². Esto es el cálculo de capa límite / la asintótica del balance arquimediano−primos. Es
el corazón analítico restante de O-4b. NO cerrado. ## Estado honesto
- [DERIVADO] 2º orden desde M_θ, c=−ψ''(¼)/8 exacto.
- [ESTRUCTURAL] frontera esencial ⟹ potencial w-dependiente ⟹ singularidad central (coherente con el dato). Explica por qué NO es Dirichlet plano (cautela de confirmada).
- [ABIERTO] el balance de frontera explícito (W(w) + escala e^{−L} + espectro (k+1)²) = Paso 3.
- 𝓛 = operador de 2º orden con potencial central singular; coeficiente del 2º orden derivado; potencial caracterizado pero no derivado en cerrado.
