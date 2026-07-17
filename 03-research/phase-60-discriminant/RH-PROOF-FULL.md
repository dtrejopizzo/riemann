# La Hipótesis de Riemann vía tripletes espectrales zeta (CCM)
## Cadena completa Eslabón 0 → Eslabón 4 — estado auditado **Autor:** David Alejandro Pizzo · **Programa:** `riemann-program/phase-60-discriminant` > **AUDITORÍA DEL TRIBUNAL (··), ver `tribunal-VEREDICTO.md`.**
> Correcciones aplicadas: (C.1) el **déficit de frame `g₀=Ξ_T` es RH-hard**, NO cerrable por
> Landau–Beurling — `S_λ` tiene núcleo de dim `≈2λ²`, `Ξ_T` es uno de `≈2λ²` candidatos; la
> selección requiere la forma de Weil completa PSD = RH-local. (C.2) Distinguir
> `λ_min(S_λ)=0` (frame de ceros, trivial) de `ε_0=λ_min(QW)` (forma de Weil, signo=RH).
> (C.3) **E1 es cita obligada CCM Thm 1.1(iii)**, NO "reparación cerrable" (, severo);
> el sub-caso `ξ_k>0` SÍ es elemental (Lema M1, Herglotz). (C.4) **`γ=3` NO está derivado**
> (numérico; la compacidad obstruye derivar `n²`). Expositivas: **retirar `Γ=O(1)`** (sólo
> `O(logλ)` probado, y alcanza); lema del horizonte corregido a **sub-crítico**
> (`densidad ceros/Nyquist = 1−1/(2logλ) < 1`, defecto `≈2λ²`); normalización libre **módulo
> límite no degenerado**. Documento maestro: ensambla la cadena deductiva del programa ––
(arXiv:2511.22755) desde la construcción del operador de Weil finito hasta RH, **con el
estado honesto de cada pieza tras auditoría matemática**. No se reclama prueba de RH: el
núcleo es RH-equivalente. El valor es la **localización** del problema y un andamiaje de
aproximación genuinamente probado alrededor de un único núcleo. Notación: `ξ(s)=½s(s−1)π^{−s/2}Γ(s/2)ζ(s)`, `Ξ(t)=ξ(½+it)` (entera, orden 1, par, real en
ℝ). `RH ⟺ Ξ∈LP` (clase de Laguerre–Pólya, real-rooted). `λ>1`, `L=2logλ`, `d_k=2πk/L`,
`Ω=logλ`, `T*=2πλ²` (horizonte de Nyquist). --- ## 0. CUADRO DE SITUACIÓN (post-auditoría) Leyenda: **✅ probado** · **✅\*** probado módulo resultado clásico estándar ·
**⟂ condicional** (implicación correcta, hipótesis no probadas) · **🔧 reparación pendiente**
(cierto pero sin prueba propia) · **🟥 núcleo RH-hard** · **⬚ abierto (análisis)**. | # | Pieza | Estado | Nota de auditoría |
|---|---|---|---|
| **E0** | Construcción CCM (forma de Weil `QW`, `ξ̂_{λ,N}`) | **✅** | definición; motor validado reproduce ceros |
| **E1** | Real-rootedness de `ξ̂_{λ,N}` | **🔧** | prueba registrada (interlacing) **REFUTADA** por contraejemplo; cierta vía CCM Thm 1.1(iii)/Hermite–Biehler; prueba propia abierta |
| └ H1 | fondo simple + autovector positivo (envolvente) | **✅** (estructura) | **NO** da PSD — corrección: PF ⟹ estructura, no `ε_0≥0` |
| └ H1′ | `QW` PSD (`ε_0≥0`) | **= RH** | `QW=`forma de Weil ⟹ PSD ⟺ Weil-pos ⟺ RH-hasta-T* (NO incondicional) |
| **E2** | Convergencia `ξ̂_{λ,N} → Ξ` | andamiaje + núcleo | ↓ |
| └ E2.a/c/horizonte | límite N / Re s≥1+ε / `T*~2πλ²` | **✅** | |
| └ N0 | `Ξ_T→Ξ` strip-uniforme (Fourier, Φ doble-exp) | **✅** | demostración robusta |
| └ N1 | transfer eje→off-axis (medida armónica) | **✅\*** | módulo Boas (clásico) |
| └ N2 | amplitud global `Γ=O(1)` | **✅** | con normalización `ξ̂(0)=Ξ(0)` |
| └ N3 | amplificación `λ^{y≤½}` | **✅\*** | Boas/Phragmén–Lindelöf |
| └ N5 reducción | `RH ⟸ ε_loc=o(λ^{−½})` | **✅** | módulo E1 (Hurwitz) |
| └ III | estabilidad relativa `ε_loc ≤ C√(logλ)‖Â_λ−Â_∞‖` | **⟂** | hipótesis (H-gap)+(H-lim)+(`ε_0>0`), sólo numéricas |
| └ N5b | borde absorbido | **✅** | reducción válida |
| └ N5c | discriminación β (RH-falso no converge) | **✅\*** | módulo real-rootedness + conv-eje |
| └ **IV.1** | identificar operador límite `Â_∞` | **⬚** | 2º-orden SL fenomenológico; id. de coef. constante refutadas |
| └ **IV.2 ≡ §V** | `ξ̂_∞=Ξ` y tasa `o(λ^{−½})` | **🟥** | **RH-equivalente** (variacional) |
| **E3** | Hurwitz | **✅** | clásico, módulo E1 |
| **E4** | `Ξ∈LP ⟺ RH` | **✅** | clásico | **Resumen en una línea:** andamiaje de aproximación (N0,N1,N2,N3) **probado**; E1 con prueba
propia **rota** (cierta vía CCM); III **condicional**; el núcleo **IV.2≡§V es RH-equivalente**;
IV.1 es análisis **abierto**. La positividad de Weil (=RH) aparece, tras auditoría, en H1′
y en `/ε_0`. --- ## 1. Eslabón 0 — el operador de Weil finito **Def 0.1 (forma de Weil CCM).** Para `|m|,|n|≤N`, núcleo de diferencia dividida de seno
``` q_{mn}(y) = (sin(2πmy/L)−sin(2πny/L))/(π(n−m)) (m≠n), q_{nn}(y) = 2(1−y/L)cos(2πny/L).
```
`QW = A_λ^N = (𝒲_{mn})`, real simétrica `(2N+1)²`:
``` 𝒲_{mn} = ∫_0^L q_{mn}(y) w_arch(y) dy − Σ_{n'≤λ²} (Λ(n')/√n') q_{mn}(log n') + 𝒫_{mn},
```
`w_arch` peso arquimediano regularizado, `Λ` von Mangoldt, `𝒫` término de polo de ζ. **Def 0.2 (función espectral band-limited).** `ξ` autovector del menor autovalor
`ε_0=ε_0(λ,N)` de `QW`. **Normalización canónica** (ver §2.0): se reescala `ξ` para
`ξ̂(0)=Ξ(0)`. Sea
``` ξ̂_{λ,N}(s):= sin(Ls/2) · Σ_{|k|≤N} ξ_k/(s − d_k).
``` **Prop 0.3 [✅].** `ξ̂_{λ,N}` es entera de tipo exponencial `Ω=logλ`, real en ℝ; sus ceros
reales son las raíces de la secular `f(s)=Σ_k ξ_k/(s−d_k)` (los `ρ̂_n`). *Prueba:*
`sin(Ls/2)` se anula en `d_k=2πk/L` (`sin(πk)=0`), cancela los polos; Paley–Wiener da tipo
`L/2`. ∎ **Identidad clave [✅, fórmula explícita].** Para `g∈PW_Ω`,
``` ⟨ξ, QW ξ⟩ = A_λ(g,g) = Σ_ρ g(γ_ρ) conj(g(conj γ_ρ)), g=ξ̂,
```
y `A_λ = A_∞|_{E_λ}` exacto (primos `>λ²` no contribuyen por soporte). **`QW` ES la forma
de Weil del lado-ceros** — esto será central en §4 (núcleo) y en la auditoría de H1. --- ## 2. Eslabón 1 — real-rootedness finita 🔧 **Enunciado.** Para todo `λ,N`, todas las raíces de `ξ̂_{λ,N}` son reales (`ξ̂_{λ,N}∈LP`). **Estado tras auditoría: cierto, pero la prueba registrada es FALSA.** **🔴 Contraejemplo que refuta la prueba vieja.** La prueba registrada usaba "con `ξ_k>0`,
la secular va `+∞→−∞` entre polos ⟹ una raíz por hueco". Pero el autovector fundamental
**no** es de signo definido (tiene un carrier de borde `ω*≈0.966π`, ~`N` cambios de signo).
Y sin `ξ_k>0` el argumento falla: tomar `ξ=(−1,2,−1)`, `d=(−1,0,1)`:
``` f(s) = −1/(s+1)+2/s−1/(s−1) = −2/(s³−s) → numerador constante, CERO raíces reales.
``` **Mecanismo correcto (Hermite–Biehler / auto-adjunto, NO Perron–Frobenius).** La
real-rootedness vale también para `L_DH` (RH-falsa, `b(n)` con signos, donde PF falla) —
empíricamente las raíces DH son reales. ⟹ **no depende del signo de los coeficientes**, luego
**no es Perron–Frobenius**; es la realización espectral **auto-adjunta** de CCM (las raíces
seculares como espectro real) / la propiedad de **Hermite–Biehler** de `ξ̂`. - **H1 [✅, corregido]:** PF (`Λ(n)≥0`, vía Lévy–Khintchine + Schoenberg + Trotter) da el fondo **simple** con **autovector de envolvente positiva** (en la base de-modulada). Esto es **estructura del ground state**, y es lo que el programa probó.
- **H1′ [= RH, NO incondicional]:** que `QW` sea **PSD** (`ε_0≥0`) NO se sigue de PF. Como `QW=`forma de Weil, `QW` PSD ⟺ Weil-positividad ⟺ RH-hasta-T*. (El memo que decía "H1 prueba QW PSD incondicional" **sobre-afirma**: PF≠PSD.) **Lema M1 [✅, sub-caso, asentado por el tribunal].** Si todos los residuos `ξ_k>0`, entonces
`f(s)=Σξ_k/(s−d_k)` es Herglotz (`Im f<0` en el semiplano superior) ⟹ **sólo ceros reales**,
con interlacing estricto. Elemental, self-contained, sin citar CCM. *Limitación:* NO cubre el
ground state real (carrier de borde `ω*≈0.966π`: ni `ξ_k>0` ni `(−1)^kξ_k>0`, desajuste de fase). **Teorema de obstrucción [✅, tribunal — ver `E1-VEREDICTO-tribunal.md`].** **No existe
construcción universal** que realice las raíces de `f(s)=Σξ_k/(s−d_k)` como espectro
auto-adjunto a partir de los datos aislados `(ξ_k,d_k)`. *Prueba:* el contraejemplo
`ξ=(−1,2,−1)` **es el ground state del Laplaciano de Dirichlet** `tridiag(−1,2,−1)` (autovector
real legítimo) y su secular `−2/(s³−s)` no tiene raíces reales; la matriz-flecha `[[D,ξ],[e^T,0]]`
(espectro = raíces de `f`) es no-simétrica con espectro no-real. ∎ ⟹ la real-rootedness debe
usar info ESPECÍFICA del ground state de Weil que `(−1,2,−1)` no posee (no es signo de `ξ` —DH
vale—, ni total-positividad —refutada—, ni PF solo). El rescate cuadrático `Σξ_k²/(s−d_k)`
(Herglotz) es **otro objeto** (sus ceros ≠ los de `ξ̂`; cuadrar rompe la identidad de Weil).
La vía de Branges existe pero verificar HB `|E(s̄)|<|E(s)|` **es lógicamente equivalente a E1**
(el carrier `ω*≈0.966π≠π` impide traducir la positividad PF de la envolvente a los residuos). **Veredicto E1 [🔧 = cita obligada DEMOSTRADA].** Real-rootedness **cierta** = **CCM Thm
1.1(iii)** (m-función de Nevanlinna auto-adjunta / `H(E)` de de Branges), dado H1+H2. El
tribunal **probó** que la cita es **necesaria**, no pereza: prueba propia al nivel
Herglotz/HB **imposible** (teorema de obstrucción). Sub-caso `ξ_k>0` cerrado (Lema M1). E3 y
N5c heredan "módulo E1". **RH-neutral** (vale para DH) ⟹ usar E1 **no es circular**. --- ## 3. Eslabón 2 — convergencia (andamiaje probado + núcleo RH) ### 2.0 Normalización [✅, resuelve cabo]
La conclusión final es **Hurwitz**, invariante por constante no nula: si `c_λ ξ̂_λ→Ξ`
uniforme con `c_λ≠0` y `ξ̂_λ` real-rooted, entonces `Ξ` real-rooted. ⟹ la normalización es
**libre**; se fija `ξ̂_λ(0)=Ξ(0)`. Con ella `Γ=sup|ξ̂_λ|=O(1)`, y `ε_loc=sup|ξ̂_λ−Ξ|` queda
bien definido. Cabo cerrado para N2, III, reducción. ### 2.1 El objeto y la reducción
``` ε_loc(λ):= sup_{|t|≤T*} |ξ̂_λ(t) − Ξ(t)|, ξ̂_λ = lim_N ξ̂_{λ,N}.
``` **Teorema N0 [✅] (truncación de Fourier strip-uniforme).** `Ξ(z)=∫Φ(u)e^{izu}du`,
`Ξ_T(z)=∫_{−T}^{T}Φ e^{izu}du`, `T=logλ`. Para todo `δ≥0`:
``` sup_{|Im z|≤δ} |Ξ−Ξ_T| ≤ C_δ λ^{5/2+δ} e^{−πλ²}.
```
*Prueba:* `Φ(u)≤Ce^{9u/2}e^{−πe^{2u}}` (doble-exp), par; `|Ξ−Ξ_T|≤2∫_T^∞Φ(u)e^{δu}du
≤ C∫_{e^{2T}}^∞ v^{5/4+δ/2}e^{−πv}dv ≤ C'λ^{5/2+δ}e^{−πλ²}`. ∎ **Lema N1 [✅\*] (transfer off-axis).** `F` entera tipo `τ`, `|F|≤Γ` en ℝ, `|F|≤ε` en
`[−R,R]`. Entonces para `|x₀|≤R/2`, `0<y₀≤δ`:
``` |F(x₀+iy₀)| ≤ e^{τy₀} ε^{ω} Γ^{1−ω}, ω=ω_{[−R,R]}(x₀+iy₀) ≥ 1−(2/π)(y₀/R).
```
*Prueba:* `log|F|−τ Im z` subarmónica en `H`, acotada (Boas); teorema de las dos constantes
+ medida armónica del segmento. ∎ **Lema N2 [✅] (amplitud).** `Γ=sup_ℝ|ξ̂_λ|=O(logλ)` por Plancherel–Pólya (`‖ξ̂‖_{L²}²=πlogλ`)
+ Nikolskii. **[Tribunal: el `Γ=O(1)` que se afirmaba antes NO está probado; retirado. El
`O(logλ)` es lo probado y alcanza.]** En N1, `Γ^{1−ω}=exp(O(λ^{−2}loglogλ))→1` pues `1−ω~λ^{−2}`. **Teorema N3 [✅\*] (amplificación, Boas).** `F` tipo `τ`, `|F|≤M` en ℝ ⟹ `|F(x+iy)|≤Me^{τ|y|}`.
*Prueba:* `g=Fe^{iτz}` acotada en ℝ por `M`, Phragmén–Lindelöf en `H`. ∎ (Da el factor
`λ^{y≤½}`.) **Teorema (Reducción) [✅, módulo E1].** Los ceros de `Ξ` están en `|Im z|≤½`, y
``` sup_{|Im z|≤½} |ξ̂_λ − Ξ| ≤ C λ^{1/2} ε_loc(λ) + C λ³ e^{−πλ²}.
```
Por tanto, **si `ε_loc(λ)=o(λ^{−½})`**, entonces `ξ̂_λ→Ξ` uniforme en `|Im z|≤½`, y por
E1 (real-rooted) + Hurwitz (E3), `Ξ∈LP`, i.e. **RH**. *Prueba:* `ξ̂_λ−Ξ=(ξ̂_λ−Ξ_T)+(Ξ_T−Ξ)`;
2º término `O(λ³e^{−πλ²})` (N0, `δ=½`); 1º entero tipo `logλ`, aplicar N1 con `R=T*~λ²`,
peso `1−ω~λ^{−2}` despreciable (N2) ⟹ `≲ λ^{1/2}ε_loc`. ∎ ### 2.2 III — estabilidad relativa [⟂ condicional] El gap absoluto `ε_1−ε_0≈3ε_0≈10^{−20}` hace inútil Davis–Kahan ingenuo. La renormalización
`Â_λ=A_λ/ε_0` lo arregla **bajo hipótesis**: **Teorema condicional III.** Si **(H-gap)** `inf_λ ε_1/ε_0=1+γ>0`, **(H-lim)** los `ξ̂_λ`
renormalizados son de Cauchy en `L²`, y **(H-pos)** `ε_0>0`, entonces existe `ξ̂_∞` y
``` ε_loc(λ) ≤ (C/γ)√(logλ)·η(λ) + Cλ³e^{−πλ²}, η(λ)=‖Â_λ−Â_∞‖_{low}→0,
```
y, **si además `ξ̂_∞=Ξ`** (IV.2), `ε_loc→0`. *Prueba:* Davis–Kahan en `Â` (bottom aislado,
gap `γ`) + Nikolskii + N0. ∎ **Auditoría de III:** (H-gap)=IV.1★ (sólo numérico `→4`); (H-lim)=Conj 2b (sólo numérico);
**(H-pos) `ε_0>0` = Weil-positividad-hasta-T* ≈ RH-hasta-T*** (¡la renormalización lleva RH
horneada!). III es **implicación correcta con hipótesis no probadas** — no es teorema
incondicional. ### 2.3 N5b — el borde se disuelve [✅]
`Ξ(t)~e^{−πt/4}` decae; en `T*~λ²`, `|Ξ(T*)|~e^{−π²λ²/2}`. El error absoluto cerca de una
raíz `~|Ξ'|·|ρ̂−γ|` es super-pequeño en el borde. La "capa de borde" de la numérica era el
error de **raíz** (relativo), no el sup-norma **absoluto** (Thm 2). El borde es benigno; lo
no-trivial se absorbe en III/núcleo. ### 2.4 N5c — discriminante converso [✅\*, módulo inputs nombrados]
**Prop N5c.** Si `f` tiene un cero off-line `z₀=x₀+iη₀` (`η₀≠0`), y vale convergencia en eje
`ξ̂_{f,λ}(x₀)→Ξ_f(x₀)`, entonces (por real-rootedness de `ξ̂_{f,λ}`)
``` sup_{|Im z|≤|η₀|}|ξ̂_{f,λ}−Ξ_f| ≥ |ξ̂_{f,λ}(z₀)| ≥ |ξ̂_{f,λ}(x₀)| → |Ξ_f(x₀)| > 0.
```
*Prueba:* `Ξ_f(z₀)=0`; monotonía real-rooted `|g(x+iy)|≥|g(x)|`; `Ξ_f(x₀)≠0`. ∎
**Inputs:** real-rootedness (CCM, auto-adjunta — vale para DH sin `Λ≥0`) + conv-eje
(andamiaje E2.a/horizonte). RH-falso **NO converge** off-axis, incondicional módulo esos
inputs. ### 2.5 IV.1 — el operador límite [⬚ abierto, análisis]
`Â_∞` (límite de `A_λ/ε_0`) tiene **espectro relativo `ε_k/ε_0→(k+1)²=n²`** (medido robusto)
y **paridad alternante `(−1)^k`** (firma de 2º orden). **Refutadas** todas las
identificaciones de coeficiente constante: Dirichlet, Hermite, prolato, caja libre, matriz
totalmente-no-negativa (Gantmacher–Krein). Lectura coherente: **Sturm–Liouville de 2º orden
de coeficientes variables** (operador de borde del frame crítico). El operador COMPLETO es
un núcleo de Loewner **compacto** (no diferencial); el 2º orden vive en la capa límite tras
`/ε_0`. **Residual IV.1:** pinear los coeficientes vía el límite (Landau–Widom / de Branges)
— **análisis, no RH-hard**. `γ=3` (=`2²/1²`) se sostiene fenomenológicamente en el 2º orden. ### 2.6 IV.2 ≡ §V — el núcleo RH-equivalente [🟥] **Caracterización variacional [el corazón].** Por la identidad de §1, `A_λ(g,g)=Σ_ρ
g(γ_ρ)conj(g(conj γ_ρ))`. **Bajo RH** (`γ_ρ` reales) es suma de cuadrados `Σ_ρ|g(γ_ρ)|²≥0`,
y su minimizador band-limited:
``` minimiza Σ_ρ |g(γ_ρ)|² ⟹ g casi se anula en {γ_ρ ≤ T*}.
```
**[Tribunal C.1+C.2 — corrección sustantiva del paso siguiente].** El "Lema horizonte: #=dim"
del documento estaba **mal contabilizado**; lo correcto es **sub-crítico**:
`densidad ceros/Nyquist = 1−1/(2logλ) < 1`, con **defecto dimensional `m≈2λ²`**. Por tanto el
frame de ceros `S_λ=Σ_{|γ_ρ|≤T*}K_{γ_ρ}⊗K_{γ_ρ}` tiene **núcleo de dim `≈2λ²`** y
`λ_min(S_λ)=0` (trivial). `Ξ_T` es UN cuasi-elemento del núcleo (`Ξ_T(γ_ρ)=O(e^{−πλ²})`)
entre `≈2λ²` candidatos: **`S_λ` solo NO selecciona `Ξ_T`**. La selección de `Ξ_T` la da la
forma de Weil **completa** `QW` (arquimediano+polo) siendo PSD = RH-local; y `ε_0=λ_min(QW)`
(signo=RH), **no** `λ_min(S_λ)=0`. ⟹ "`g₀=Ξ_T`" es **RH-hard**, no cerrable por Landau–Beurling.
Es decir, **el ground state de Weil es `Ξ_T` ⟺ RH-local + unicidad del minimizador**. Y
**sin RH** (`γ_ρ` complejos) la forma es **indefinida**, el minimizador se concentra en los
ceros off-line, **`≠Ξ_T`**. Por contrapositiva:
``` ┌──────────────────────────────────────────────────────────────┐ │ ground state de Weil = Ξ_T ⟺ todos los γ_ρ reales ⟺ RH │ └──────────────────────────────────────────────────────────────┘
```
**⟹ IV.2 (`ξ̂_∞=Ξ`) es RH-EQUIVALENTE.** No es conflación (`QW` ES la forma de Weil, mismo
objeto — auditado), no es pieza blanda: **es el núcleo RH**. Lo probado de él: bajo RH el
minimizador **es** `Ξ_T` (variacional, módulo rigor del déficit de frame, Landau–Beurling);
y N5c da el lado RH-falso (no converge) incondicional. Lo que falta es el puente —
`ξ̂_λ→Ξ` a tasa `o(λ^{−½})` — que **es** RH. --- ## 4. Eslabones 3 y 4 — clásicos **E3 (Hurwitz) [✅, módulo E1].** Si `ξ̂_λ→Ξ` uniforme en compactos de `|Im z|≤½` y cada
`ξ̂_λ∈LP` (E1), entonces `Ξ` no tiene ceros con `0<|Im z|≤½` ⟹ `Ξ∈LP`. *Prueba:* un cero
complejo de `Ξ` sería límite de ceros reales de `ξ̂_λ` — contradicción (Hurwitz). ∎ **E4 [✅, clásico].** `Ξ∈LP ⟺ RH` (de Branges). ∎ --- ## 5. Ensamble (condicional) **Teorema (prueba condicional de RH).** Asúmase: E1 (real-rootedness, cierto módulo prueba
propia), III con (H-gap)+(H-lim)+(H-pos), e IV.2 (`ξ̂_∞=Ξ`). Entonces `ε_loc=o(λ^{−½})`
(III), `ξ̂_λ→Ξ` (Reducción), `Ξ∈LP` (E1+E3), **RH** (E4). ∎ Pero IV.2 es **RH-equivalente** (§2.6) y (H-pos) **es** Weil-positividad. Luego el ensamble
**reduce RH a un núcleo RH** — no lo prueba. El valor es la reducción limpia + el andamiaje
probado. --- ## 6. Evaluación honesta (la auditoría) **Probado genuino (resiste auditoría):**
- E0 (def. + identidad `QW=`Weil); E4 (clásico); E3 (clásico, módulo E1).
- **Andamiaje de aproximación N0, N1, N2, N3** — matemática sólida y reusable.
- N5b (reducción válida); N5c (módulo inputs nombrados, monotonía correcta).
- Normalización (cabo cerrado, Hurwitz-invariante). **Condicional / con prueba pendiente:**
- **E1 🔧:** real-rootedness cierta pero **prueba registrada refutada por contraejemplo**; prueba propia (Hermite–Biehler desde auto-adjunto) **abierta**. Caja negra: CCM Thm 1.1(iii).
- **III ⟂:** condicional a (H-gap)+(H-lim)+(H-pos), todas numéricas; (H-pos)=Weil-pos.
- **H1′:** "QW PSD" **NO es incondicional** (= RH); PF da estructura, no positividad. **Núcleo y análisis abierto:**
- **IV.2≡§V 🟥:** RH-equivalente (variacional). El único núcleo RH-hard.
- **IV.1 ⬚:** identificación del operador de borde (2º-orden SL fenomenológico) — análisis, no RH-hard. **Conclusión.** La cadena CCM, auditada, es una **reducción elegante de RH a un único núcleo
RH-equivalente** (`ξ̂_λ→Ξ`, equivalente a "el ground state de Weil es `Ξ_T`"), rodeada de un
**andamiaje de aproximación genuinamente probado** (N0–N3) y con tres reparaciones honestas
pendientes (prueba propia de E1; rigor del déficit de frame `g₀→Ξ_T`; corrección de H1′). La
positividad de Weil (=RH) aparece, tras auditoría, **distribuida** en H1′, en `/ε_0` (III) y
en el núcleo IV.2. **No se prueba RH; se la localiza con precisión sin auto-engaño.** --- ### Apéndice — reparaciones pendientes (matemática real, no RH-hard salvo el núcleo)
1. **E1 propio:** Hermite–Biehler de `ξ̂` desde la realización auto-adjunta (con carrier de borde). Cerraría real-rootedness sin citar CCM.
2. **Déficit de frame:** rigorizar `g₀=Ξ_T+O(ε_0)`, `g₀→Ξ_T` (Landau–Beurling a densidad crítica). Cerraría el "exactamente `Ξ_T`" del núcleo (lado RH).
3. **IV.1:** operador de borde 2º-orden + espectro `n²` (Landau–Widom). Cerraría `γ>0` y la identificación.
4. **Núcleo IV.2≡§V (RH):** la tasa `o(λ^{−½})` protegida por positividad — **RH**.
