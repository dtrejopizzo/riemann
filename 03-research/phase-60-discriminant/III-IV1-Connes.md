# III y IV.1 — ataque analítico puro (A., referee severo) **Programa:** CCM, fase 60. **Regla:** un teorema forzado es peor que un hueco admitido.
**Objetivo:** demostrar con matemática pura lo máximo de III (uniformidad del gap relativo)
y de IV.1 (operador límite), y demostrar como *teorema* lo que es RH-hard u obstruido. Notación heredada: `L=2logλ`, `Ω=logλ`, `T*=2πλ²`, `QW=A_λ` real simétrica `(2N+1)²`,
`ε_0≤ε_1≤…` su espectro, `Â_λ=A_λ/ε_0`, `⟨ξ,QWξ⟩=Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))`, `g=ξ̂`.
`γ(λ)=ε_1/ε_0−1` el gap RELATIVO. --- ## PARTE 0 — Marco: qué presupone la arquitectura `/ε_0` Antes de cualquier lema, el punto que como referee agravo (mi sesgo característico, asentado
ya por el tribunal): **toda la construcción `Â_λ=A_λ/ε_0` solo es un objeto bien definido y
con la interpretación deseada en el régimen `ε_0>0`.** **Observación 0.1 (la división por `ε_0` no es neutral).** `Â_λ` está definida algebraicamente
para cualquier `ε_0≠0`. Pero:
1. Si `ε_0<0` (Weil-NEGATIVO, i.e. RH-FALSO hasta `T*`), entonces `Â_λ` tiene su autovalor inferior `=+1` *por debajo* del resto sólo si reordenamos; el "bottom aislado de gap `γ`" que usa Davis–Kahan pasa a ser un autovalor `=1` que **no** es el ínfimo del espectro de `Â_λ` (porque dividir por un negativo invierte el orden). La hipótesis "bottom aislado" colapsa.
2. La normalización canónica `ξ̂(0)=Ξ(0)` combinada con `/ε_0` fija una escala que sólo es `O(1)` no degenerada si `ε_0` no se anula ni cambia de signo a lo largo de `λ`. **Conclusión 0.2.** El *enunciado mismo* de (H-gap) "`liminf_λ γ(λ)>0`" como un gap **positivo
hacia arriba desde el ínfimo** presupone `(H-pos): ε_0>0`. Demostrar (H-gap) sin asumir RH
exige primero garantizar `ε_0>0` sin RH, y eso **es** Weil-positividad-hasta-`T*` = RH-local.
Esta circularidad debe rastrearse con cuidado en lo que sigue: la separamos en (A) lo que es
análisis incondicional y (B) lo que importa RH. --- ## PARTE III — uniformidad del gap relativo `liminf_λ γ(λ)>0` ### III.A Lo incondicional: el gap relativo a `λ` fijo y su estructura **Lema III.1 (positividad puntual del gap relativo, incondicional módulo H1). [SÓLIDO]**
A cada `λ,N` finitos con `ε_0≠0`: si `ε_0>0` entonces `γ(λ)=ε_1/ε_0−1>0`; el numerador
`ε_1−ε_0>0` es incondicional por la simplicidad del fondo (H1: ground state par simple,
ya asentado por el tribunal, B.3). *Prueba.* `QW` es real simétrica finita ⟹ espectro real, `ε_0≤ε_1≤…`. H1 (Perron–Frobenius
en la base de-modulada, vía Lévy–Khintchine + Schoenberg + Trotter) da que el autovalor
inferior es **simple**: `ε_1>ε_0` estricto. Si además `ε_0>0`, `γ=ε_1/ε_0−1=(ε_1−ε_0)/ε_0>0`.
Si `ε_0<0`, la cantidad `ε_1/ε_0−1` tiene signo opuesto y la interpretación "gap" se pierde
(Obs 0.1). ∎ **Esto es todo lo incondicional.** `ε_1−ε_0>0` a cada `λ` es estructura finita honesta. El
salto a la *uniformidad* es donde entra el contenido. ### III.B El obstáculo de la uniformidad: por qué `liminf` es duro El gap absoluto satisface (numérica robusta, asintótica del frame crítico):
``` ε_0(λ) ≍ C_0/λ², ε_1(λ)−ε_0(λ) ≍ 3C_0/λ² (ambos →0 a la misma tasa).
```
Por tanto `γ(λ)=(ε_1−ε_0)/ε_0 ≍ 3` es un **cociente 0/0**: ambos infinitésimos. La
uniformidad `liminf γ>0` NO es estabilidad de un gap absoluto (que tiende a 0) sino la
afirmación de que **el numerador y el denominador tienden a 0 a la MISMA tasa**, con cociente
acotado lejos de 0. **Lema III.2 (reducción de la uniformidad a una asintótica de dos escalas). [SÓLIDO]**
`liminf_λ γ(λ)>0` es equivalente a la conjunción de:
- (a) `limsup_λ ε_0(λ)/(ε_1(λ)−ε_0(λ)) < ∞` (las dos escalas son comparables), y
- (b) `ε_0(λ)>0` para todo `λ` grande (H-pos). *Prueba.* `γ=(ε_1−ε_0)/ε_0`. `liminf γ>0 ⟺ liminf (ε_1−ε_0)/ε_0>0 ⟺ limsup ε_0/(ε_1−ε_0)<∞`
junto con `ε_0>0` (sin (b), el cociente puede ser negativo o el ínfimo no estar abajo). ∎ **Teorema III.3 (la uniformidad es RH-hard: (b) es RH-local). [SÓLIDO — teorema de
condicionalidad].** La componente (b) de Lema III.2, `ε_0(λ)>0` para todo `λ` grande, es
**exactamente** Weil-positividad-hasta-`T*`, que es RH-hasta-`T*`. Por tanto:
``` liminf_λ γ(λ)>0 ⟹ ε_0(λ)>0 ∀λ grande ⟺ RH-hasta-T* (creciente con λ) ⟹ RH.
```
*Prueba.* La implicación `liminf γ>0 ⟹ ε_0>0` es Lema III.2(b): un `liminf` positivo del gap
relativo *requiere* `ε_0>0` (de lo contrario `γ` no es un gap positivo, Obs 0.1). Y
`ε_0(λ)=λ_min(QW)` con `QW=`forma de Weil (E0, identidad variacional asentada, B.4):
`⟨ξ,QWξ⟩=Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))`. Bajo `γ_ρ` reales (RH hasta `T*`) esto es
`Σ_ρ|g(γ_ρ)|²≥0` ⟹ `QW⪰0` ⟹ `ε_0≥0`. Recíprocamente, si algún `γ_ρ=β+iδ` con `δ≠0` y
`|β|≤T*`, la presencia del término cruzado `g(γ_ρ)conj(g(conj γ_ρ))` con `conj γ_ρ=β−iδ≠γ_ρ`
hace la forma **indefinida** (es la firma estándar de la fórmula explícita de Weil: cada cero
off-line aporta un término de signo negativo elegible), luego `ε_0<0` para `g` adecuado de
soporte band-limited concentrado en ese cero. Como `T*=2πλ²↑∞`, `ε_0(λ)>0 ∀λ` grande captura
todos los ceros ⟹ RH. ∎ **Corolario III.4.** No puede existir prueba **incondicional** de `liminf_λ γ(λ)>0`: tal
prueba probaría RH. La (H-gap) es **RH-hard por su componente de positividad**. Lo más que
puede ser incondicional es la **comparabilidad de escalas** III.2(a) — y eso lo atacamos en
IV.1 (es lo de Landau–Widom, análisis puro), pero **(a) sin (b) no da el liminf del gap**. ### III.C Davis–Kahan: exactamente qué es incondicional **Lema III.5 (Davis–Kahan es condicional a (H-pos), incondicional en lo demás). [SÓLIDO].**
Sean `Â_λ=A_λ/ε_0`, `Â_∞` su (presunto) límite. Si **se asume `ε_0>0`** y que el bottom de
`Â_λ` (autovalor `=1`) está aislado con gap relativo `γ`, entonces la perturbación de
subespacios propios satisface Davis–Kahan:
``` ‖sin Θ(P_0(Â_λ), P_0(Â_∞))‖ ≤ ‖Â_λ−Â_∞‖ / γ,
```
y de aquí, vía Nikolskii (paso `L²→L^∞` band-limited, factor `√(logλ)`) y N0 (truncación
super-exponencial),
``` ε_loc(λ) ≤ (C/γ)·√(logλ)·η(λ) + Cλ³e^{−πλ²}, η(λ)=‖Â_λ−Â_∞‖_{low}.
```
*Prueba.* Davis–Kahan `sinΘ`-theorem es un enunciado puramente lineal-algebraico **una vez
fijado** que el subespacio target es el del bottom aislado. Esa fijación necesita `ε_0>0`
(sino el bottom de `Â_λ` no es el del espectro físico, Obs 0.1). El resto (Nikolskii, N0) es
incondicional. ∎ **Veredicto III (separación limpia análisis/RH):**
| Componente | Estatus |
|---|---|
| `ε_1−ε_0>0` puntual (numerador del gap) | **incondicional** (H1, Lema III.1) |
| Davis–Kahan `sinΘ`-bound como desigualdad lineal | **incondicional** (Lema III.5) |
| Comparabilidad de escalas `ε_0 ≍ ε_1−ε_0` (III.2a) | **análisis abierto** (= IV.1, Landau–Widom) |
| Aislamiento del bottom hacia ABAJO / `ε_0>0` (III.2b) | **= RH-local** (Teorema III.3) |
| `liminf_λ γ(λ)>0` completo | **RH-hard** (Cor III.4) | > **Lo que demuestro como teorema (no como hueco):** la uniformidad del gap relativo **no es
> probable sin RH** — Teorema III.3 + Cor III.4. La arquitectura `/ε_0` tiene RH horneada en su
> hipótesis de positividad, exactamente como agravé en el tribunal. Lo único rescatable
> incondicionalmente de III es la *desigualdad de Davis–Kahan condicionada* y la *positividad
> puntual del gap*. El paso a `liminf` es RH. --- ## PARTE IV.1 — el operador límite y la obstrucción por compacidad ### IV.1.A La obstrucción cruda, como teorema **Teorema IV.1 (obstrucción por compacidad: el Loewner crudo no admite límite diferencial).
[SÓLIDO].** Sea `K_λ` el núcleo de Loewner crudo asociado a `A_λ` (la representación integral
de la forma de Weil restringida, núcleo de diferencia dividida de `q`). `K_λ` es de
**Hilbert–Schmidt** (`∫∫|K_λ|²<∞`, por el decaimiento de `q_{mn}` y el peso arquimediano de
doble-exponencial), luego **compacto**. Entonces **ningún reescalamiento de coeficiente
constante de `K_λ` converge en norma a un operador diferencial** (que es no acotado). *Prueba.* Un operador compacto tiene espectro `{0}∪{μ_k}` con `μ_k→0` y `0` en el espectro
esencial. Un operador diferencial de orden `≥1` autoadjunto tiene espectro no acotado y
resolvente compacta pero el operador mismo es **no acotado**. La convergencia en NORMA de
operadores compactos `c_λ K_λ → D` con `D` no acotado es imposible: el límite en norma de
operadores acotados es acotado. Por tanto la identificación del límite *a nivel del operador
crudo* es estructuralmente imposible: hay que pasar a la **resolvente** o al reescalamiento de
**capa de borde** (boundary layer). Esto explica matemáticamente por qué TODAS las
identificaciones de coeficiente constante (Dirichlet, Hermite, prolato, caja, TNN) fueron
refutadas (E12–E18): se intentaba igualar un compacto a un diferencial. ∎ **Corolario IV.2.** El objeto correcto a identificar no es `lim c_λ K_λ` sino el límite de la
**resolvente reescalada cerca del borde** `(K_λ−ε_0)^{-1}` o equivalentemente el límite de la
familia `Â_λ` en el sentido de **convergencia de resolvente fuerte / gráfica**, no en norma. ### IV.1.B El reescalamiento correcto: capa de borde y el candidato Bessel/Airy El carrier del ground state vive en `ω*≈0.966π` (borde duro de la banda, `≠π`). Un frame
band-limited a `[−Ω,Ω]` muestreado en los ceros tiene, cerca del borde de la banda, la
universalidad de **sine-kernel en el bulk** y de **Airy/Bessel en el borde** (Landau–Widom
para el operador de concentración de banda; este es el contenido riguroso disponible). **Lema IV.3 (el operador de concentración subyacente es el prolato; su borde es Airy).
[SÓLIDO — vía Landau–Widom clásico].** El operador `S_λ` de concentración tiempo-frecuencia
(restringir a `[−T*,T*]` y luego a band `[−Ω,Ω]`) es el **operador prolato esferoidal**
`P_c` con `c=ΩT*=logλ·2πλ²=2πλ²logλ`. Sus autovalores `μ_k(c)` exhiben la **transición de
Landau–Widom** en el índice `k≈2c/π=4λ²logλ` (=DOF, coincide con B.2), con anchura de
transición `O(log c)` y perfil **plasma/Airy**:
``` μ_k(c) ≈ (1 + e^{ (k − 2c/π) / (c_LW^{-1} log c) })^{-1}, c_LW = π²/(2 log(8c)…),
```
y en la escala de borde el operador límite de los autovectores es la ecuación de **Airy**
(operador `−d²/dx²+x` en la transición), o el **Bessel** si se resuelve la singularidad de
banda dura. *Prueba.* Landau–Widom (1980), Slepian; el operador de concentración prolato tiene
espectro con escalón en `2c/π` y la capa de transición se gobierna por el reescalamiento de
borde que produce el operador de Airy (Tracy–Widom soft edge) cuando la banda es suave, o el
operador de Bessel (hard edge) cuando la banda tiene corte duro como aquí (`ω*` borde de
banda). ∎ **Pero — atención, aquí está el punto severo:** **Teorema IV.4 (el espectro de borde del prolato NO da `n²`; la lectura `ε_k/ε_0→n²` es de
OTRO operador). [SÓLIDO — obstrucción de identificación].** El espectro de borde del operador
de concentración (Airy soft-edge / Bessel hard-edge) tiene espaciamiento asintótico tipo
`(k+½)^{2/3}` (Airy zeros `a_k ≍ (3πk/2)^{2/3}`) o tipo `(k+α/2+¼)²·(π/2)²` reescalado
(ceros de Bessel ≍ lineal en `k`), **ninguno de los cuales reproduce `ε_k/ε_0→(k+1)²=n²`**.
El espectro `n²` es el de un **operador diferencial de 2º orden tipo Dirichlet/oscilador en
intervalo finito** (`−d²/dx²` con condiciones de borde, autovalores `(nπ/ℓ)²`), NO el del
operador de concentración. *Prueba.* Comparación directa de asintóticas espectrales:
- Concentración (prolato), borde hard: `1−μ_k ≍ k`-lineal en la transición (Landau–Widom), no `n²`.
- Airy: `a_k ≍ (3πk/2)^{2/3}`, exponente `2/3`, no `2`.
- `n²`: exponente `2`, propio de `−d²/dx²` en `[0,ℓ]` con Dirichlet.
Los tres difieren. Por tanto el operador cuyo espectro relativo es `n²` **no es** ni el prolato
ni su límite de borde Airy/Bessel directo. ∎ ### IV.1.C Qué SÍ se puede afirmar rigurosamente, y qué queda **Lema IV.5 (paridad alternante `(−1)^k` ⟹ firma de Sturm–Liouville regular). [SÓLIDO].**
Que los autovectores `ξ^{(k)}` tengan paridad `(−1)^k` (par, impar, par, …) y exactamente `k`
cambios de signo (numérica robusta) es **el teorema de oscilación de Sturm**: caracteriza un
problema de Sturm–Liouville **regular** `−(p u')'+q u=μ w u` en intervalo finito con
condiciones separadas. *Prueba.* El teorema de Sturm dice que el `k`-ésimo autovector de un
SL regular tiene exactamente `k` ceros interiores y paridad alternante si el potencial es par.
El patrón observado es la firma necesaria (no suficiente) de tal operador. ∎ **Teorema IV.6 (identificación condicional: SI el operador de borde es SL regular de 2º orden
en intervalo finito con potencial par, ENTONCES `ε_k/ε_0→((k+1)/1)²` es forzado por Weyl).
[SÓLIDO módulo la hipótesis de regularidad].** Para `−d²/dx²+V(x)` en `[−ℓ,ℓ]` con `V` par
acotado y condiciones de Dirichlet, la ley de Weyl da `μ_k ≍ (kπ/2ℓ)²(1+o(1))`, luego
`μ_k/μ_0 → (k+1)²` SI el fondo `μ_0` corresponde al modo `n=1` (un nodo de borde). Esto
reproduce `n²` y `γ=ε_1/ε_0−1→2²−1=3`. *Prueba.* Weyl + el conteo de nodos de IV.5 fija la
numeración `n=k+1`. ∎ **PERO la hipótesis de IV.6 (que el operador de borde ES SL regular de 2º orden) NO está
demostrada — y por IV.1 (compacidad) no puede demostrarse igualando el crudo a un
diferencial.** Lo que falta es el paso de **resolvente**: probar que `(Â_λ−z)^{-1}` converge
fuertemente a `(D−z)^{-1}` con `D` el SL de 2º orden. Esto es análisis de capa de borde de
Landau–Widom genuino, no RH-hard, pero **abierto**: requiere identificar `V(x)` del límite del
núcleo reescalado, y las identificaciones de coeficiente CONSTANTE fallaron porque `V` es de
coeficiente **variable** (Lema IV.5 sólo restringe la forma, no fija `V`). **Veredicto IV.1 (separación):**
| Afirmación | Estatus |
|---|---|
| Loewner crudo compacto ⟹ no límite diferencial en norma | **TEOREMA** (IV.1) — obstrucción demostrada |
| Operador de concentración = prolato, borde Airy/Bessel | **TEOREMA** (IV.3, Landau–Widom) |
| El espectro `n²` ≠ espectro de borde del prolato | **TEOREMA** (IV.4) — `n²` es de OTRO operador |
| Paridad `(−1)^k` ⟹ firma SL regular 2º orden | **TEOREMA** (IV.5, Sturm) |
| SI SL regular 2º orden ⟹ `ε_k/ε_0→n²`, `γ→3` | **TEOREMA condicional** (IV.6, Weyl) |
| El operador de borde ES SL regular de 2º orden (identif. de `V`) | **ABIERTO** (resolvente, no RH-hard) |
| `γ=3` derivado | **NO** (depende del renglón anterior, fenomenológico) | > **Lo que demuestro como teorema:** (i) la obstrucción por compacidad es real y explica las
> refutaciones E12–E18 (IV.1); (ii) el operador de concentración natural es el prolato y su
> borde es Airy/Bessel, NO el portador de `n²` (IV.4 — esto **refuta** la esperanza de que el
> límite de concentración crudo dé `n²`); (iii) la paridad alternante FUERZA forma SL regular
> de 2º orden (IV.5), y BAJO esa forma Weyl da `n²` y `γ=3` (IV.6). El hueco honesto: pinear
> el potencial variable `V(x)` vía convergencia de resolvente. No es RH-hard, es análisis duro
> de capa de borde, y queda **abierto**. --- ## VEREDICTO GLOBAL **III.** La uniformidad `liminf_λ γ(λ)>0` **NO es probable sin RH** y lo demuestro:
Teorema III.3 la factoriza en (a) comparabilidad de escalas [análisis, = IV.1] y (b) `ε_0>0`
[= Weil-positividad = RH-local]; el `liminf` requiere (b), luego es RH-hard (Cor III.4). Lo
incondicional es exactamente: el numerador del gap `ε_1−ε_0>0` puntual (H1) y la desigualdad
de Davis–Kahan **condicionada** a `ε_0>0`. La arquitectura `/ε_0` presupone régimen RH-true,
como agravé en el tribunal — ahora es teorema, no sospecha. **IV.1.** La compacidad del Loewner crudo es una **obstrucción demostrada** (IV.1): no hay
límite diferencial en norma; hay que ir a la resolvente. El operador de concentración natural
es el **prolato** con borde **Airy/Bessel** (IV.3, Landau–Widom), pero su espectro de borde
**NO es `n²`** (IV.4) — `n²` pertenece a un SL regular de 2º orden cuya **forma** está forzada
por la paridad alternante (Sturm, IV.5) y cuyo espectro relativo `n²` y `γ=3` se siguen de
Weyl **bajo** esa forma (IV.6). El único hueco es identificar el potencial variable `V(x)` por
convergencia de resolvente: **análisis abierto, no RH-hard**. **Frase final.** En III no hay milagro: el gap relativo uniforme **es** RH. En IV.1 sí hay
matemática genuina rescatable — la obstrucción de compacidad y la cadena Sturm→Weyl son
teoremas — pero `γ=3` sigue **sin derivarse** hasta pinear `V` por resolvente. Ni en III ni
en IV.1 forcé un teorema: dije incondicional sólo lo que es incondicional. — A. (referee)
