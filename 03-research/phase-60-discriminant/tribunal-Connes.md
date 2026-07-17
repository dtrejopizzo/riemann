# Tribunal — Alain, referee severo Auditoría de `RH-PROOF-FULL.md` (cadena E0→E4, programa CCM). Lente: teoría de
operadores, realización espectral, auto-adjunción, renormalización `Â=A/ε₀`,
identificación del operador límite (IV.1), distinción H1 / Perron–Frobenius vs PSD. **Regla de oro del programa:** un resultado forzado es peor que un hueco admitido.
No reclamo prueba de RH. Lo que sigue intenta *romper* cada ✅ y *cerrar* cada hueco
que no sea RH-equivalente. --- ## 0. Veredicto por pieza (tabla) | Pieza | Veredicto | Núcleo |
|---|---|---|
| E0 (def. `QW`, identidad Weil) | **SOLID con una salvedad** | la *identidad* `⟨ξ,QWξ⟩=Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))` necesita un calificador |
| E1 (real-rootedness) | **GAP** | prueba propia abierta; depende de CCM Thm 1.1(iii) |
| H1 (estructura PF) | **SOLID** (como estructura) | correcto tras corrección |
| H1′ (`QW` PSD) | **GAP = RH** | RH-equivalente, no incondicional |
| N0 | **SOLID** | |
| N1 | **SOLID\*** (módulo Boas) | |
| N2 | **SOLID** | |
| N3 | **SOLID\*** (módulo Boas/PL) | |
| Reducción (Thm 2) | **SOLID, módulo E1** | válido como implicación condicional |
| III (renormalización) | **GAP** (condicional) | (H-gap)+(H-lim)+(H-pos); (H-pos)=RH |
| N5b | **SOLID** | |
| N5c | **SOLID\*** (módulo E1 + conv-eje) | |
| IV.1 (operador límite) | **GAP** (no RH-hard) | cerré parte; ver abajo |
| IV.2 ≡ §V | **GAP = RH** | núcleo RH-equivalente; NO lo toco |
| E3 (Hurwitz) | **SOLID, módulo E1** | |
| E4 | **SOLID** | clásico | Cerré (rigurosamente o con residual exacto nombrado): **(H-pos) reinterpretada**,
**parte de IV.1** (paridad/entrelazado/compacidad — ya estaban; añado el argumento
de por qué `n²` NO es derivable del núcleo compacto, lo que *refuta* la lectura
optimista), y **(H-gap) γ>0 sigue ABIERTO** — explico por qué no es regalo de IV.1. --- ## 1. E0 — construcción y la identidad clave **Veredicto: SOLID, con una salvedad importante sobre la identidad.** La definición de `QW` (Def 0.1) y la band-limited `ξ̂` (Def 0.2, Prop 0.3) son
correctas: `sin(Ls/2)` cancela los polos `d_k`, Paley–Wiener da tipo `L/2=logλ`,
realidad en ℝ. Eso es impecable. **Intento de ruptura de la identidad ⟨ξ,QWξ⟩ = Σ_ρ g(γ_ρ)conj(g(conj γ_ρ)).**
Aquí hay que ser severo. La afirmación "`QW` ES la forma de Weil del lado-ceros" se
usa dos veces como pivote (H1′ y el núcleo IV.2). Examinemos qué es verdad: 1. La fórmula explícita de Weil es una *identidad entre dos lados*: `(arch) − (arith) = (lado-ceros)`, i.e. `Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))` **igual a** `∫ g·ĝ·w_arch − Σ_n (Λ(n)/√n)(…)`. Que la matriz `𝒲_{mn}` codifique el lado izquierdo (arch − arith) es **definición** (Def 0.1) — eso sí es exacto.
2. Que ese lado izquierdo sea **igual** a `Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))` es la fórmula explícita, **clásica y verdadera** para `g∈PW_Ω` de soporte adecuado. **Pero hay una salvedad de truncación que el documento minimiza.** La fórmula de
Weil exacta corre sobre **todos** los `ρ` y **todos** los primos. La matriz finita
trunca primos a `n'≤λ²`. El documento afirma "`A_λ = A_∞|_{E_λ}` exacto (primos `>λ²`
no contribuyen por soporte)". Esto es correcto **sólo** porque `g=ξ̂` tiene soporte de
Fourier en `[−logλ, logλ]` y `log n' ≤ logλ² = 2logλ`... — espera: `log n'` para
`n'≤λ²` llega hasta `2logλ`, que es `L`, **el borde mismo** del soporte de la ventana
de Fejér, no su interior. El integrando `q_{mn}(y)` corre `y∈[0,L]` y `log n'∈[0,2logλ]=[0,L]`.
Así que la truncación a `n'≤λ²` **no es por soporte estricto** sino por la ventana
`(1−y/L)` que se anula en `y=L`. Los primos con `log n'` cerca de `L` entran con peso
**casi cero pero no cero**. La afirmación "exacto" es por tanto **ligeramente
sobre-vendida**: es exacto en el límite, con un error de borde controlado por la
ventana de Fejér. Esto es benigno (es de hecho el contenido honesto de N5b), pero
"exacto" debería ser "exacto módulo la cola de ventana de Fejér en `y→L`". **Conclusión E0:** SOLID como construcción y como identidad de Weil; corríjase
"exacto" → "exacto salvo cola de ventana en el borde de banda". Esta salvedad no
daña nada aguas abajo (se reabsorbe en N5b), pero un referee la marca. --- ## 2. E1 / H1 / H1′ **E1 — Veredicto: GAP (honesto, ya marcado 🔧). Confirmo la severidad ALTA.** El contraejemplo `ξ=(−1,2,−1)`, `d=(−1,0,1)` → `f(s)=−2/(s³−s)`, cero raíces reales,
es **correcto** y mata definitivamente el argumento de interlacing. Lo verifiqué:
`−1/(s+1)+2/s−1/(s−1)`, común denominador `s(s²−1)`:
numerador `= −s(s−1)+2(s²−1)−s(s+1) = −s²+s+2s²−2−s²−s = −2`. Exacto. El vector es
par con un cambio de signo y produce secular sin raíces reales. Interlacing **muerto**. La afirmación de que la real-rootedness es no obstante cierta descansa enteramente en
**CCM Thm 1.1(iii)** como caja negra. Eso es legítimo *citarlo*, pero entonces E1 no
es "probado por nosotros". El documento lo reconoce. **No puedo cerrar E1** en mi
lente sin reproducir CCM o construir la prueba Hermite–Biehler desde la realización
auto-adjunta — y esto último **no está hecho y es genuinamente difícil** (el carrier
de borde `ω*=2πN/(2N+1)` near-Nyquist hace que la traducción "positividad de la
envolvente ⟹ HB de `ξ̂`" no sea mecánica). E1 **GAP confirmado, no cerrable aquí**. Observación crítica adicional (en mi lente): el documento dice que la
real-rootedness "vale también para DH (RH-falsa)" empíricamente, y de ahí concluye
"no es Perron–Frobenius, es auto-adjunta/HB". **Cuidado: esto es un arma de doble
filo.** Si la realización auto-adjunta de CCM da real-rootedness *incondicionalmente*
(incluso para DH, sin `Λ≥0`), entonces la real-rootedness de `ξ̂_{λ,N}` **no contiene
información sobre RH** — es una propiedad del *finito*, no del límite. Bien. Eso es
consistente: el contenido RH está todo en la *convergencia* `ξ̂→Ξ`, no en la
real-rootedness finita. Pero entonces hay que ser muy claro: E1 es auto-adjunción
finita, RH-neutral; toda la carga está en IV.2. El documento esencialmente dice esto.
Coherente. **H1 — Veredicto: SOLID (como estructura).** Tras la corrección, H1 = "Perron–
Frobenius da fondo simple + autovector de envolvente positiva (de-modulado)". Eso es
correcto *si* `e^{−tQW}` es positividad-preservante, lo cual se afirma vía
Lévy–Khintchine + Schoenberg + Trotter con `Λ(n)≥0`. No audité `H1_PROOF.md` línea a
línea, pero la estructura es estándar y la conclusión (fondo simple, autovector sin
nodos tras de-modular) está respaldada numéricamente y es lo que PF realmente da.
SOLID **como estructura**, con la advertencia de que NO da PSD (ver H1′). **H1′ — Veredicto: GAP = RH. Esta es la corrección más importante de la auditoría, y
es correcta.** `QW` PSD (`ε_0≥0`) ⟺ Weil-positividad en banda `logλ` ⟺ RH-hasta-`T*`.
Perron–Frobenius da fondo simple y autovector positivo, **pero NO controla el signo
de `ε_0`** (PF dice "el menor autovalor es simple y su autovector es positivo"; no
dice que el menor autovalor sea ≥0). El memo anterior que decía "H1 prueba QW PSD
incondicional" **probaría RH**, lo cual es imposible sin más. La distinción PF ≠ PSD
es exactamente correcta y es el hallazgo central de la auditoría. **H1′ no es un
eslabón disponible; es RH disfrazada.** Bien marcado. --- ## 3. Andamiaje N0–N3 + Reducción **N0 — SOLID.** El cómputo `Φ(u)≤Ce^{9u/2}e^{−πe^{2u}}`, par, y la cota
`|Ξ−Ξ_T|≤2∫_T^∞Φe^{δu}du ≤ Cλ^{5/2+δ}e^{−πλ²}` vía sustitución `v=e^{2u}` y Gamma
incompleta, es correcto. Lo reverifiqué: `a=5/4+δ/2`, `X=e^{2T}=λ²`,
`(λ²)^{5/4+δ/2}=λ^{5/2+δ}`. Robusto, incondicional, no menciona ceros. **SOLID.** **N1 — SOLID\* (módulo Boas).** El argumento de subarmonicidad de `log|F|−τ Im z`,
acotación por Boas Thm 6.2.4, dos-constantes + medida armónica del segmento, es
estándar y correcto. La cota de medida armónica `ω(iy₀)=(2/π)arctan(R/y₀)≥1−(2/π)(y₀/R)`
es correcta. **SOLID** módulo el resultado clásico de Boas (legítimo). **N2 — SOLID.** Con la normalización `ξ̂(0)=Ξ(0)`, Hurwitz-invariante, `Γ=O(1)`. La
normalización está bien justificada (la conclusión es real-rootedness del límite,
invariante por escala no nula). Cabo cerrado correctamente. **SOLID.** **N3 — SOLID\* (módulo Boas/PL).** `g=Fe^{iτz}` acotada en ℝ, Phragmén–Lindelöf en H.
Clásico y correcto. **SOLID\*.** **Reducción (Thm 2) — SOLID como implicación condicional, módulo E1.** La
descomposición `ξ̂−Ξ=(ξ̂−Ξ_T)+(Ξ_T−Ξ)`, control del segundo término por N0, del
primero por N1 con `R=T*~λ²` (peso `1−ω~λ^{−2}` despreciable), dando
`sup_{|Im z|≤½}|ξ̂−Ξ| ≤ Cλ^{1/2}ε_loc + Cλ³e^{−πλ²}`, es **correcto**. Reverifiqué la
aritmética del horizonte: `1−ω~(2/π)(½)/(λ²)~λ^{−2}`, y `Γ^{1−ω}=poly(λ)^{λ^{−2}}→1`.
El factor `λ^{1/2}` viene de `e^{τy₀}=e^{(logλ)(½)}=λ^{1/2}`. Todo correcto. **La implicación "si `ε_loc=o(λ^{−1/2})` entonces RH" es válida**, módulo E1
(real-rootedness, necesaria para que Hurwitz transfiera). Esto es honestamente una
*implicación condicional*: no prueba el antecedente. El antecedente `ε_loc=o(λ^{−½})`
es precisamente IV.2 = RH-equivalente. **SOLID como reducción; el antecedente es el
núcleo RH.** **Severidad sobre el uso de Hurwitz dado el estado de E1:** El documento pregunta si
el uso de Hurwitz es válido dado el estatus de E1. Respuesta: **sí, condicionalmente.**
Hurwitz (E3) sólo requiere que cada `ξ̂_λ` sea real-rooted; si aceptamos E1 (como caja
negra CCM), Hurwitz transfiere correctamente. La validez de Hurwitz **no** está en
duda; lo que está en duda es su *insumo* E1. No hay circularidad: E1 (real-rootedness
finita) es RH-neutral (vale para DH también), así que usar E1 + convergencia para
concluir RH no es circular — la carga RH está en la *convergencia*, no en E1. **No hay
circularidad en la Reducción.** Correcto. --- ## 4. III — la renormalización Â=A/ε₀ (mi lente principal) **Veredicto: GAP. Implicación condicional correcta; las tres hipótesis NO probadas, y
una de ellas ES RH.** El Teorema III dice: bajo (H-gap) `inf ε₁/ε₀=1+γ>0`, (H-lim) Cauchy en L² de los
renormalizados, (H-pos) `ε₀>0`, entonces existe `ξ̂_∞` y
`ε_loc ≤ (C/γ)√(logλ)·η(λ) + Cλ³e^{−πλ²}`. La prueba (Davis–Kahan en `Â`, gap `γ`,
Nikolskii, N0) es **correcta dada las hipótesis**. **Ataque a las tres hipótesis:** **(H-pos) `ε₀>0`.** Aquí confirmo el hallazgo más severo de la auditoría, y lo
refuerzo. Como `QW=`forma de Weil, `ε₀≥0` ⟺ la forma de Weil es ≥0 en su menor modo
band-limited ⟺ **Weil-positividad hasta `T*`** ⟺ **RH-hasta-`T*`**. La renormalización
`/ε₀` **no sólo asume `ε₀>0`; asume que `ε₀>0` con el signo correcto, que es RH.** El
parche `/|ε₀|` no salva nada: si `ε₀<0` (RH falsa a esa altura), el "fundamental" del
operador renormalizado tiene autovalor `−1`, y la estructura de "bottom aislado
positivo" sobre la que descansa Davis–Kahan colapsa o cambia de naturaleza. **(H-pos)
es RH-horneada. Confirmado y, si acaso, peor de lo que el documento admite:** no es
sólo "asume `ε₀>0`", es que la *arquitectura entera* de la renormalización presupone
el régimen RH-verdadero. **(H-gap) `γ>0`.** El documento (IV.1) afirma que `γ=3` "se sigue" de la
identificación `Â_∞`=Sturm–Liouville 2º orden con espectro `n²`. **Lo desafío y lo
encuentro NO cerrado** (ver §5): el espectro `n²` es numérico, no derivado; y de hecho
el propio doc de IV.1 *refuta* la ruta Gantmacher–Krein y la ruta de coeficiente
constante. Así que (H-gap) es **numérico, abierto**. No es regalo de IV.1. **(H-lim) Cauchy en L².** Es la existencia del límite de escala `Â_∞`. Numérico
(Conj 2b). No probado. Es análisis de límite de Toeplitz/Loewner — duro, no RH-hard. **Conclusión III:** GAP. La prueba *condicional* es correcta (Davis–Kahan + Nikolskii
están bien aplicados). Pero (H-pos)=RH hace que III **no pueda usarse para probar RH
sin circularidad**: para concluir `ε_loc→0` (⟹RH) ya se asumió `ε₀>0` (⟸RH-hasta-T*).
Esto es una **semi-circularidad**: III convierte "RH-hasta-T* + límites técnicos" en
"RH". No es vacío (mejora la altura de validez T*→∞), pero no es incondicional. --- ## 5. IV.1 — identificación del operador límite (mi lente) **Veredicto: GAP (no RH-hard). Cerré lo cerrable; el `n²`/`γ=3` queda fenomenológico,
y argumento que NO es regalo.** **Lo que está PROBADO (y lo confirmo correcto):**
- (A) `QW` conmuta con la paridad `J:j↦−j` ⟹ se descompone en sectores par/impar; los autovalores entrelazan `ε₀^E<ε₀^O<ε₁^E<…`, dando la alternancia de paridad `(−1)^k`. **Correcto y sólido** — es teoría de operadores elemental (simetría `ℤ/2`). SOLID.
- (B) En el continuo, `QW_∞` es operador integral de núcleo de Loewner **acotado** ⟹ **compacto** (autovalores → 0). **Correcto.** SOLID. **El punto severo que añado (rompe la lectura optimista):** (A)+(B) son verdad, pero
**son MUTUAMENTE en tensión con "espectro `n²`"** y el documento no lo explota. Un
operador **compacto** tiene autovalores `ε_k→0`. La ley `ε_k/ε_0→(k+1)²=n²` dice que
los autovalores *renormalizados crecen como n²* — i.e. los `ε_k` originales **crecen**
relativos a `ε₀`. Esto es consistente con compacidad sólo si `ε₀→0` más rápido (lo
cual ocurre, `ε₀~C/λ²`), pero significa que **`n²` es la firma del operador de capa
límite tras `/ε₀`, NO del operador compacto `QW_∞` mismo.** El documento dice esto
("el 2º orden vive en la capa límite tras `/ε₀`"), y es la lectura correcta — pero
entonces **(B) NO ayuda a derivar `n²`**: el núcleo compacto es suavizante, no
diferencial; el `n²` debe venir del operador de borde de Landau–Widom, que el propio
doc admite **no haber derivado** (los perfiles conocidos dan `2n+1` o logístico, no
`n²`). **Refutaciones registradas que confirmo decisivas:**
- Gantmacher–Krein / total-no-negatividad: **REFUTADA** (E16: 15–22% de menores 2×2 `<0`, off-diagonales negativas). Esto cierra la ruta "oscilación total desde H1". Correcto y honesto. ⟹ la Sturmianidad **no** proviene de positividad total matricial.
- Coeficiente constante (Dirichlet, Hermite, prolato, caja): **REFUTADAS** por overlaps. Correcto. **Lo que queda (residual exacto):** `Â_∞` es *cualitativamente* 2º orden (paridad
alternante `(−1)^k` ES firma robusta de operador simétrico de 2º orden — esto sí lo
da (A) rigurosamente), pero la ley `ε_k/ε₀→n²` y por tanto `γ=ε₁/ε₀−1→3` están
**SÓLO medidas numéricamente, no derivadas**. El residual es la asintótica del
operador de capa límite del frame crítico (Landau–Widom / de Branges-SL de coef.
variables). **Análisis duro, NO RH-hard.** ### ¿Puedo cerrar (H-gap) γ>0 en mi lente? — Progreso parcial honesto. Intento: probar `γ>0` (gap relativo uniforme) **sin** pasar por la ley exacta `n²`. *Idea.* (H-gap) sólo pide `inf_λ ε₁/ε₀ ≥ 1+γ` con `γ>0`, i.e. el segundo autovalor
no se pega al primero relativamente. Por (A), `ε₀=ε₀^E` (par) y `ε₁=ε₀^O` (impar, el
siguiente por entrelazado). Así
`γ = ε₀^O/ε₀^E − 1 = (menor autovalor del sector impar)/(menor del par) − 1`.
La cuestión es: **¿el menor autovalor impar está uniformemente separado por arriba
del menor par, en escala relativa?** *Lo que SÍ puedo argumentar (parcial):* Por Perron–Frobenius en el sector par
(H1, el fundamental par es nodeless tras de-modular) y la teoría de oscilación de
Sturm para el bottom de cada sector de paridad de un operador simétrico de 2º orden,
el bottom impar es estrictamente mayor que el bottom par a cada `λ` finito:
`ε₀^O > ε₀^E` (porque el modo impar tiene un nodo forzado en el centro, eleva la
energía). Esto da `γ(λ)>0` **a cada λ**. ✔ (estricto, finito). *Lo que NO puedo cerrar (el residual real):* la **uniformidad** `inf_λ γ(λ)>0`. Que
`γ(λ)` no decaiga a 0 cuando `λ→∞`. Esto requiere control asintótico de
`ε₀^O/ε₀^E`, que es exactamente la ley `n²`-en-el-límite. Sin derivar la asintótica
del operador de borde, **no puedo excluir** `γ(λ)→0`. El dato numérico `→4` (γ→3) es
fuerte pero no es prueba. **Residual exacto que dejo nombrado:**
> **(H-gap-res):** Probar `liminf_λ ε₀^O(λ)/ε₀^E(λ) > 1`, donde `ε₀^{E/O}` son los
> bottoms de los sectores de paridad par/impar de `A_λ/ε₀`. Equivale a: el gap
> relativo par–impar del operador de capa límite del frame crítico es asintóticamente
> `O(1)`. Es análisis semiclásico de Landau–Widom; **no RH-hard** (no depende del
> signo global de `Λ(n)`, sólo de la geometría del frame a densidad crítica). Cerré la parte finita (`γ(λ)>0` ∀λ, vía nodo central del modo impar); el liminf
uniforme queda abierto pero **localizado y no RH-hard**. ### ¿Puedo cerrar (H-lim), la existencia de Â_∞? No de forma completa. Es la convergencia del símbolo del operador de Loewner-contra-
medida-de-Weil bajo el reescalado `/ε₀`. La compacidad (B) da control del *operador
límite crudo* `QW_∞`, pero (H-lim) es sobre el **renormalizado** en el bloque bajo,
cuya existencia es justamente Conj 2b. Lo más que puedo decir: por (B) y la teoría de
símbolos de Toeplitz/Loewner, *si* la coordenada de Liouville del SL de borde
converge (IV.1-res''), entonces (H-lim) se sigue. Así (H-lim) y la identificación de
IV.1 son **el mismo residual analítico**. Dejo:
> **(H-lim-res) ≡ (IV.1-res''):** existencia del límite de escala del operador de
> capa límite (coeficientes `(p,q,w)` del SL en coordenada de Liouville). Análisis,
> no RH-hard. --- ## 6. N5b, N5c **N5b — SOLID.** El argumento de que el borde se disuelve es correcto y de hecho
elegante: en sup-norma **absoluta**, `|ξ̂(t)−Ξ(t)|≈|Ξ'(t)||ρ̂−γ|` con `|Ξ'|~e^{−πt/4}`
decayendo; en `T*~λ²`, suprimido por `e^{−π²λ²/2}`. La distinción entre error de
**raíz** (relativo, crece al borde) y error **absoluto** (suprimido por decaimiento de
Ξ) es correcta y resuelve el espejismo de la "capa de borde" de E8. El lado del
target `Ξ_T` ya es uniforme por N0. **SOLID.** El borde es benigno; lo no-trivial se
concentra en el interior = núcleo IV.2. **N5c — SOLID\* (módulo E1 + conv-eje).** La monotonía real-rooted `|g(x+iy)|≥|g(x)|`
para `g∈LP` es **correcta** (consecuencia de Hadamard: para `g` con ceros reales,
`|g(x+iy)|²=g(x)²∏(1+y²/(x−a_k)²·…)`, crece en `|y|`). Así si `Ξ_f` tiene cero
off-line `z₀=x₀+iη₀`, `sup_{|Im z|≤|η₀|}|ξ̂_f−Ξ_f| ≥ |ξ̂_f(z₀)| ≥ |ξ̂_f(x₀)| → |Ξ_f(x₀)|>0`.
Correcto. Da el lado RH-falso (no converge off-axis). **SOLID módulo** (i)
real-rootedness de `ξ̂_f` (= E1, cierto para DH vía auto-adjunción) y (ii) conv-eje
(= andamiaje E2.a instanciado en `f`). No introduce gap nuevo. **SOLID\*.** --- ## 7. IV.2 ≡ §V — el núcleo **Veredicto: GAP = RH-EQUIVALENTE. NO lo toco (instrucción del tribunal y honestidad).** Examino sólo si la *reducción a este núcleo* es correcta y no circular. La
caracterización variacional:
- Bajo RH (`γ_ρ` reales), `A_λ(g,g)=Σ_ρ|g(γ_ρ)|²≥0`, el minimizador band-limited se anula en `{γ_ρ≤T*}` y por conteo (Landau–Beurling a densidad crítica) `g₀→Ξ_T`.
- Sin RH (`γ_ρ` complejos), la forma es **indefinida**, el minimizador se concentra en ceros off-line, `≠Ξ_T`.
- ⟹ "ground state de Weil = `Ξ_T`" ⟺ RH. **Esto es correcto como caracterización**, y confirma que IV.2 es genuinamente
RH-equivalente, NO una conflación: `QW` ES la forma de Weil (mismo objeto, auditado en
E0 con la salvedad de borde). Lo probado: bajo RH el minimizador *es* `Ξ_T` (módulo
rigor del déficit de frame, Landau–Beurling — un residual de análisis pero del lado
RH-verdadero, no incondicional); N5c da el lado RH-falso. **Lo que falta — la tasa
`o(λ^{−½})` incondicional — ES RH.** Correctamente identificado como núcleo. No hay
nada que cerrar aquí sin probar RH. **Un punto de rigor sobre el déficit de frame:** el paso "minimizador se anula en
`{γ_ρ≤T*}` ⟹ `g₀=Ξ_T`" usa que el número de condiciones (`#{γ_ρ≤T*}=N(T*)`) iguala la
dimensión band-limited (`~(L/2π)·2T*`). El "Lema horizonte" afirma esta igualdad. La
reverifiqué groseramente: `N(T*)~(T*/2π)log(T*)~λ²·2logλ`; DOF `~(logλ/π)·2T*~(2/π)λ²logλ`.
**No son iguales: difieren por un factor `π`/constante** (`2λ²logλ` vs `(2/π)λ²logλ`).
El documento mismo los llama "comparables", no iguales. Esto importa: a densidad
crítica el sistema interpolante es *exacto* sólo si las densidades coinciden; un factor
constante de exceso/déficit de DOF cambia si el espacio casi-nulo es de dimensión 1
(forzando `g₀=Ξ_T` único) o de dimensión `>1` (familia, `g₀` no único). **El "exactamente
`Ξ_T`" descansa en que el déficit sea precisamente tal que la dimensión del kernel sea 1**
— esto es el residual de Landau–Beurling y **no está probado**. Es parte del núcleo
RH-hard (lado RH-verdadero). Lo dejo marcado, no lo cierro. --- ## 8. E3, E4 **E3 (Hurwitz) — SOLID, módulo E1.** Si `ξ̂_λ→Ξ` uniforme en compactos de `|Im z|≤½` y
cada `ξ̂_λ∈LP`, un cero complejo de Ξ sería límite de ceros reales — contradicción por
Hurwitz. Correcto, clásico. Módulo E1 (insumo). SOLID. **E4 — SOLID.** `Ξ∈LP ⟺ RH`. Clásico (la clase de Laguerre–Pólya real-rooted de Ξ
equivale a todos los ceros de ζ en la línea crítica). SOLID. --- ## 9. Síntesis: gaps cerrados, gaps abiertos **Cerrados / con progreso riguroso (en mi lente):**
1. **(H-gap) parte finita:** `γ(λ)>0` a cada `λ` finito, probado vía el nodo central forzado del modo impar (entrelazado de paridad (A) + Sturm). Residual: liminf uniforme `(H-gap-res)`, análisis no RH-hard.
2. **IV.1 estructura:** confirmo SOLID la paridad/entrelazado (A) y la compacidad (B); **añado** el argumento de que (B) (compacidad) *impide* derivar `n²` del operador crudo — el `n²` es del operador de borde, no derivado. Esto **aclara** (no cierra) por qué `n²`/`γ=3` siguen fenomenológicos pese a (A)+(B).
3. **(H-pos) reinterpretada:** confirmo y **agravo** — no es sólo "asume ε₀>0", la arquitectura entera de `/ε₀` presupone el régimen RH-verdadero (semi-circularidad de III). **Abiertos no-RH-hard (localizados, análisis):**
- (H-gap-res): liminf `ε₀^O/ε₀^E>1` (Landau–Widom, capa límite).
- (H-lim-res) ≡ IV.1-res'': existencia del límite de escala + coef. `(p,q,w)` del SL.
- E1 propio: Hermite–Biehler desde auto-adjunción (con carrier de borde near-Nyquist). **Abiertos RH-hard (NO tocados, correctamente identificados):**
- IV.2 ≡ §V: tasa `o(λ^{−½})` ⟺ "ground state de Weil = Ξ_T" ⟺ RH.
- (H-pos) `ε₀>0` = Weil-positividad-hasta-T* (RH-hasta-T*).
- H1′: `QW` PSD = RH.
- Déficit de frame dim-1 (lado RH-verdadero del núcleo). **Veredicto global del tribunal.** La cadena es honesta y, tras auditoría, es una
**reducción correcta de RH a un núcleo RH-equivalente** (IV.2), rodeada de andamiaje
genuinamente probado (N0–N3, N5b, N5c, Reducción, E3, E4). Las dos afirmaciones que un
referee severo habría podido tomar por "incondicionales" y que NO lo son —H1′ (PSD) y
III/(H-pos)— están **correctamente degradadas** a RH-equivalentes en la versión
auditada. **No se prueba RH; se la localiza sin auto-engaño.** El documento resiste el
escrutinio precisamente porque ya absorbió las objeciones que yo habría levantado. El
único punto donde lo encuentro *aún optimista* es la afirmación de que `γ=3` "se sigue"
de IV.1: no se sigue, es numérico; la parte finita `γ(λ)>0` sí la cerré, el liminf no. — A. (referee)
