# Tribunal — Auditoría (referee SEVERO)
## Programa CCM zeta spectral triples — cadena E0→E4 **Auditor:** Henri (en el rol de referee), lente: análisis complejo / funciones
enteras (Laguerre–Pólya, Hermite–Biehler, de Branges, Boas, Phragmén–Lindelöf).
**Documentos leídos:** `RH-PROOF-FULL.md`, `AUDIT-repairs-E1-III.md`, `E2-nucleo-proof.md`,
`N5-subpieces-proved.md`.
**Regla:** frío. Una prueba forzada es peor que un gap admitido. NO se reclama RH. --- ## 0. Resumen ejecutivo (per-pieza) | Pieza | Veredicto | Una línea |
|---|---|---|
| E0 | **SOLID** | Definición + identidad `QW=`Weil; correcta como definición. |
| E1 (real-rootedness) | **GAP** | Prueba propia abierta. **Cierro una mitad** (HB para envolvente positiva pura); la mitad con carrier de borde sigue abierta. Ver §2. |
| H1 | **SOLID** (estructura) | PF da fondo simple + envolvente positiva. NO da PSD. Correcto tras corrección. |
| H1′ (QW PSD) | **GAP = RH** | `ε_0≥0 ⟺` Weil-pos `⟺` RH-hasta-T*. No incondicional. Correctamente etiquetado. |
| N0 | **SOLID** | Φ doble-exp + Γ incompleta: la prueba es correcta y robusta. Ver §3.1. |
| N1 | **SOLID*** | Subarmonicidad + dos constantes + medida armónica correcto; Boas bien invocado. Una imprecisión de constante, inocua. Ver §3.2. |
| N2 (Γ=O(1)/O(logλ)) | **SOLID** | Plancherel–Pólya + Nikolskii correcto. El `O(1)` con normalización es más fuerte de lo probado (probado: `O(logλ)`); inocuo. Ver §3.3. |
| N3 | **SOLID** | Boas/Phragmén–Lindelöf correcto. Ver §3.4. |
| Reducción (Thm 2) | **SOLID*** (módulo E1) | El paso Hurwitz es válido; la cota `λ^{1/2}ε_loc` correcta. Ver §4. |
| III | **GAP (condicional)** | (H-gap)+(H-lim)+(H-pos) sólo numéricas; (H-pos)=RH. Implicación correcta. |
| N5b | **SOLID** | Borde benigno; reducción válida. |
| N5c | **SOLID*** (módulo E1) | Monotonía real-rooted correcta; lado DH demostrado. Ver §5. |
| IV.1 | **GAP (análisis)** | Operador límite no identificado; no RH-hard. |
| IV.2 ≡ §V | **GAP = RH-equivalente** | El núcleo. Correctamente etiquetado RH-hard. |
| E3 (Hurwitz) | **SOLID** (módulo E1) | Clásico, bien aplicado. Ver §4. |
| E4 | **SOLID** | `Ξ∈LP ⟺ RH`, clásico. | **Frase del referee:** El andamiaje analítico (N0–N3, Reducción, Hurwitz) **resiste la
auditoría severa** — es matemática correcta y reutilizable. El documento es **honesto** en
sus etiquetas: no hay auto-engaño en la localización. Los tres puntos vivos son (i) E1 sin
prueba propia, (ii) III condicional con (H-pos)=RH, (iii) el núcleo IV.2 RH-equivalente.
**No se prueba RH.** Abajo cierro parcialmente E1 y delimito *exactamente* qué falta. --- ## 1. Auditoría del andamiaje — veredictos detallados ### 1.0 E0 — SOLID (como definición)
La forma `QW=A_λ^N` está bien definida; la identidad `⟨ξ,QWξ⟩ = Σ_ρ g(γ_ρ)·conj(g(conj γ_ρ))`
con `g=ξ̂` es la fórmula explícita de Weil restringida a `PW_Ω`, y la afirmación "`QW` ES la
forma de Weil del lado-ceros" es **estructuralmente correcta** y central. No es una pieza que
"pruebe" nada; es el escenario. SOLID, sin objeción. --- ## 2. EL GAP CERRABLE EN MI LENTE — E1 real-rootedness ### 2.1 Planteamiento exacto y refutación de la prueba vieja
Se afirma: para todo `λ,N`, `ξ̂_{λ,N}(s) = sin(Ls/2)·Σ_{|k|≤N} ξ_k/(s−d_k)` tiene **sólo
ceros reales**. La prueba registrada (interlacing con `ξ_k>0`) está **correctamente refutada**
por `ξ=(−1,2,−1)`, `d=(−1,0,1)`: `f(s)=−2/(s³−s)`, numerador constante, **cero raíces**.
El contraejemplo es válido y demoledor para la prueba vieja. Acepto la refutación. Además el documento observa que la real-rootedness vale empíricamente también para
Davenport–Heilbronn (donde `Λ≥0` falla), luego **no puede provenir de Perron–Frobenius**.
Esto es un argumento correcto y honesto: descarta la vía de positividad de coeficientes. ### 2.2 La estructura real del problema (Hermite–Biehler)
Reescribo. Sea `f(s)=Σ_k ξ_k/(s−d_k)` la secular. Los ceros de `ξ̂` (aparte de cancelar los
polos `d_k`) son los ceros de `f`. La afirmación "`ξ̂∈LP`" equivale a "**`f` tiene sólo ceros
reales**", porque `sin(Ls/2)` ya es LP y entera de tipo `L/2`, el producto de dos funciones
con sólo ceros reales y orden ≤1 (con apareamiento correcto de polos) sigue siendo entera.
Precisamente: `ξ̂` es entera (los polos de `f` en `d_k` son cancelados por los ceros de
`sin(Ls/2)`), de tipo exponencial `L/2`, **real sobre ℝ** (coef. `ξ_k`, `d_k` reales). **Criterio HB clave (Hermite–Biehler real).** Una función entera real `g` de tipo
exponencial, real en ℝ y en la clase de Pólya–Laguerre cerrada, tiene **sólo ceros reales**
si y sólo si existe `E` (función de de Branges, `E=A−iB` con `A,B` reales en ℝ) tal que
`g=B` (o `g=A`), `E` de tipo HB (`|E(z̄)|<|E(z)|` para `Im z>0`), **y `A,B` tienen ceros
reales que se entrelazan (interlacing)**. Equivalentemente, vía el teorema de Hermite–Biehler
clásico: una función `A+iB` con `A,B` polinomios/enteras reales es Hurwitz-estable (ceros en
un semiplano) ⟺ los ceros de `A` y `B` son reales, simples y **se entrelazan**, con el
Wronskiano `A'B−AB' ` de signo constante. **El punto técnico decisivo:** la real-rootedness de `f` **NO** se sigue de ninguna propiedad
de signo de `ξ_k` sola; se sigue **si y sólo si** la función racional `f(s)=Σ ξ_k/(s−d_k)`
es una **función de Nevanlinna/Herglotz con signo constante de residuos**, o más
generalmente si `f` es la **función-m de un operador de Jacobi/Sturm–Liouville autoadjunto**. ### 2.3 Lo que SÍ puedo cerrar rigurosamente (mitad del gap) **Lema M1 (residuos positivos ⟹ real-rootedness, Herglotz).**
Sea `f(s)=Σ_{k} r_k/(s−d_k)` con `d_k∈ℝ` distintos y **todos los residuos `r_k>0`**.
Entonces `f` es una función de Herglotz–Nevanlinna (mapea el semiplano superior `H` en el
semiplano inferior): para `Im s>0`,
``` Im f(s) = Σ_k r_k · Im(1/(s−d_k)) = Σ_k r_k · (−Im s)/|s−d_k|² < 0.
```
Luego `f(s)≠0` para `Im s≠0` (su parte imaginaria no nula), i.e. **todos los ceros de `f`
son reales**. Además, entre dos polos consecutivos `f` decrece de `+∞` a `−∞`, dando
exactamente un cero por hueco: **interlacing estricto**. ∎ Este es el resultado clásico correcto (es exactamente el caso de la función-m de un Jacobi
con pesos positivos). Y ahora la conexión con `ξ̂`: **Lema M2 (traducción residuo↔valor band-edge).** Por la fórmula del residuo,
`ξ̂(d_k)=lim_{s→d_k}sin(Ls/2)·ξ_k/(s−d_k)`. Como `sin(Ls/2)` tiene un cero simple en `d_k`
con derivada `(L/2)cos(Ld_k/2)=(L/2)cos(πk)=(L/2)(−1)^k`, resulta
``` ξ̂(d_k) = ξ_k·(L/2)·(−1)^k. (correcta, coincide con la del documento)
```
El **residuo** de `f` en `d_k` es justamente `ξ_k`. Por tanto el Lema M1 da real-rootedness
**si y sólo si todos los `ξ_k` tienen el mismo signo** (WLOG `ξ_k>0`). **Conclusión parcial [CERRADO]:** Si el autovector fundamental tuviera **envolvente de signo
constante en la base sinc cruda** (`ξ_k>0` ∀k), la real-rootedness sería un **teorema
elemental** (Herglotz, Lema M1), self-contained, sin citar CCM. Esto es matemática limpia y
la doy por cerrada para ese caso. ### 2.4 Por qué el caso real NO está cubierto — y qué hipótesis falta exactamente
El obstáculo, identificado correctamente por el documento, es que el ground state **real**
tiene `ξ_k ≈ u_k cos(ω*k+φ)` con carrier de borde `ω*≈0.966π` (near-Nyquist), luego `ξ_k`
**cambia de signo ~N veces**. El Lema M1 **no aplica** y de hecho el contraejemplo
`(−1,2,−1)` muestra que con signos alternantes la real-rootedness **puede fallar**. Entonces, ¿por qué es cierta empíricamente? La respuesta correcta es de-modulación. Defino
el cambio `ξ_k = (−1)^k η_k` (modulación por el carrier Nyquist `ω=π`). El valor band-edge
se vuelve `ξ̂(d_k)=η_k(L/2)`, **sin el `(−1)^k`**. Pero esto NO cambia los residuos de `f`:
`f(s)=Σ(−1)^kη_k/(s−d_k)` — el signo alternante reaparece en los residuos. La de-modulación
que hace `η_k>0` (envolvente positiva, **lo que H1/PF sí da**) **no** es la que controla los
residuos de `f`. Hay un **desajuste de fase** estructural: la positividad que PF entrega vive
en la envolvente de-modulada (`η_k>0`), mientras que la real-rootedness vía Herglotz pide
positividad de los residuos crudos `ξ_k`. Con carrier `ω*` cerca de π (pero **no** exactamente
π), ni `ξ_k>0` ni `(−1)^kξ_k>0`. **Veredicto preciso de E1:** La real-rootedness **NO es self-contained al nivel Herglotz**.
Requiere uno de: - **(A)** una propiedad de **interlacing de de Branges**: que `ξ̂` sea la componente `B` de una `E=A−iB` de tipo HB, lo cual es *equivalente* a que los ceros seculares sean el **espectro de un operador autoadjunto** (la realización espectral de CCM). Esto es **exactamente CCM Thm 1.1(iii)**: las raíces seculares = espectro real de la realización autoadjunta. No es derivable de M1; es la afirmación espectral misma.
- **(B)** una hipótesis sobre el autovector fundamental: que el operador `QW` (real simétrico) sea tal que su ground state genere un **sistema de Chebyshev / núcleo totalmente positivo** en la base sinc. El documento reporta que esto fue **refutado** numéricamente (Gantmacher–Krein, totalmente-no-negativa, no encaja). Acepto ese hallazgo: la vía TP/TN está cerrada. **Por tanto, mi veredicto sobre E1 es (c) del enunciado de la tarea, afinado:**
> La real-rootedness es cierta como **CCM Thm 1.1(iii)** (espectro real de la realización
> autoadjunta = raíces seculares). **No admite prueba self-contained al nivel de funciones
> enteras elementales** (Herglotz/HB) con la información que el programa tiene aislada
> (envolvente positiva de-modulada), por el desajuste de fase carrier ω*≠π. La única vía
> propia sería **reconstruir la realización autoadjunta** (que `ξ̂` ∈ un espacio de de Branges
> `H(E)` con `E` HB explícita), lo cual es **re-probar CCM 1.1(iii)**, no un atajo. Esto **cierra la pregunta 2**: produzco (a) prueba correcta para el sub-caso `ξ_k>0`
(Herglotz, Lema M1), e identifico (c) que el caso real *debe* citarse de CCM 1.1(iii). La
hipótesis extra precisa que el ground state debe satisfacer es **membresía en un espacio de
de Branges `H(E)` con `E` de tipo HB** (equivalente: interlacing `A`/`B` de su función de
estructura), que es la realización autoadjunta — no una propiedad combinatoria de los signos. ### 2.5 Honestidad sobre la severidad
E1 alimenta Hurwitz (E3) y N5c. Ambos heredan "módulo E1". La etiqueta **🔧/GAP del documento
es correcta y no sobre-afirma**. Mi único refinamiento: el documento sugiere que la prueba
propia HB "queda abierta como reparación"; yo soy más duro: **al nivel de la información
aislada, la prueba propia es esencialmente CCM 1.1(iii)** y no un lema pendiente de azúcar.
Citarla como caja negra es **legítimo**; presentarla como "cerrable con más trabajo de
funciones enteras" sería **optimismo injustificado**. Bajar a: *cita obligada de CCM*. --- ## 3. Verificación rigurosa de los lemas analíticos ### 3.1 N0 (Φ doble-exp + Γ incompleta) — SOLID
La cota `Φ(u)≤Ce^{9u/2}e^{−πe^{2u}}` para `u≥0` es correcta: el término dominante de `Φ` es
`2π²n⁴e^{9u/2}e^{−πn²e^{2u}}`, y `Σ_n n⁴ e^{−π(n²−1)e^{2u}} = O(1)` uniformemente en `u≥0`
(la cola converge, dominada por `n=1`). Correcto. El cambio `v=e^{2u}`, `du=dv/(2v)`, da
`∫_T^∞ e^{(9/2+δ)u}e^{−πe^{2u}}du = ½∫_{e^{2T}}^∞ v^{(9/2+δ)/2−1}e^{−πv}dv
= ½∫ v^{5/4+δ/2}e^{−πv}dv = ½Γ(7/4+δ/2, πe^{2T})`. **Verificado el exponente:** `(9/2+δ)/2−1
= 9/4+δ/2−1 = 5/4+δ/2`. Correcto.
La cota de Gamma incompleta `∫_X^∞ v^a e^{−πv}dv ≤ C X^a e^{−πX}` para `X` grande es estándar
(integración por partes, el término de borde domina cuando `a/(πX)→0`). Con `X=e^{2T}=λ²`:
`(λ²)^{5/4+δ/2}e^{−πλ²}=λ^{5/2+δ}e^{−πλ²}`. **La prueba de N0 es correcta y robusta.** SOLID. Observación menor (no afecta): el corolario "franja crece hasta `λ²/logλ`" es correcto y de
hecho subraya que la truncación de Fourier **no** es el obstáculo. Bien. ### 3.2 N1 (transfer off-axis) — SOLID*, con un matiz de constante
La construcción `w(z)=log|F(z)|−τ·Im z` subarmónica en `H` es correcta (`log|F|` subarmónica,
`τ Im z` armónica). La invocación de **Boas Thm 6.2.4** (`|F(z)|≤Γ e^{τ|Im z|}` para `F` de
tipo `τ` acotada en ℝ) es **correcta y es exactamente la condición de crecimiento que hace a
`w` acotada superiormente**, habilitando Phragmén–Lindelöf / mayorante armónica. Bien invocado.
La cota de medida armónica del segmento desde `iy₀`:
`ω_{[−R,R]}(iy₀)=(2/π)arctan(R/y₀)`, y `(2/π)arctan(R/y₀)≥1−(2/π)(y₀/R)` para `y₀≪R`
(porque `arctan(R/y₀)=π/2−arctan(y₀/R)≥π/2−y₀/R`). **Verificado.** SOLID*. **Matiz (inocuo):** la cota `1−ω≤(2/π)(y₀/R)` es para el punto `x₀=0`. Para `|x₀|≤R/2` la
medida armónica del segmento sólo **aumenta** (el punto sigue "viendo" el segmento bajo ángulo
≥ comparable), luego `1−ω` sigue siendo `O(y₀/R)=O(λ^{−2})`. El documento usa esto
implícitamente; es correcto pero merecería una línea. No cambia nada: `Γ^{1−ω}→1`. ### 3.3 N2 (amplitud) — SOLID, con sobre-afirmación inocua
La identidad de Parseval `‖ξ̂‖²_{L²}=(πL/2)‖ξ‖²_{ℓ²}=πlogλ` (con `‖ξ‖_{ℓ²}=1`) es correcta
vía ortogonalidad de los `sinc_k`. Nikolskii/Plancherel–Pólya `‖g‖_∞≤C√τ‖g‖_{L²}` para
`g∈PW_τ`, `τ=logλ`, da `‖ξ̂‖_∞≤C√(logλ)·√(πlogλ)=O(logλ)`. **Esto está probado y es SOLID.** **Discrepancia que señalo:** el cuadro de `RH-PROOF-FULL.md` y la Reducción afirman a veces
`Γ=O(1)` "con la normalización `ξ̂(0)=Ξ(0)`". Lo **probado** es `Γ=O(logλ)`. El salto a
`O(1)` requiere que la normalización en un punto controle el sup global, lo cual **no está
demostrado** (es plausible pero no trivial: `Ξ(0)` es una constante fija, pero `‖ξ̂‖_∞`
podría exceder `|ξ̂(0)|`). **No importa para la cadena**, porque la Reducción sólo necesita
`Γ=poly(λ)` (para que `Γ^{1−ω}→1`), que `O(logλ)` da de sobra. Recomiendo al autor **retirar
la afirmación `Γ=O(1)`** y quedarse con el `O(logλ)` probado. Etiqueta correcta: SOLID para
lo que la cadena necesita. ### 3.4 N3 (amplificación, Boas/PL) — SOLID
`g(z)=F(z)e^{iτz}` en `H`: `|g(x)|=|F(x)|≤M` en ℝ; `|g(z)|=|F(z)|e^{−τ Im z}` acotado en
sectores por el crecimiento de tipo `τ`; Phragmén–Lindelöf en `H` (orden finito, acotado en
frontera) ⟹ `|g|≤M` en `H` ⟹ `|F(x+iy)|≤Me^{τy}` para `y≥0`; reflexión para `y<0`.
**Correcto, es Boas 6.2.4.** Da el factor `e^{τy}=λ^y≤λ^{1/2}`. SOLID. --- ## 4. Reducción + Hurwitz (E3) — SOLID (módulo E1). Validez del paso Hurwitz. **La cota de la Reducción** `sup_{|Im z|≤½}|ξ̂_λ−Ξ|≤Cλ^{1/2}ε_loc+Cλ³e^{−πλ²}` es la suma
de N0 (`δ=½`: `λ^{5/2+½}=λ³`) y de N1/N3 (`e^{τ·½}ε_loc^ω Γ^{1−ω}=λ^{1/2}ε_loc·(1+o(1))`).
**Aritméticamente y analíticamente correcta.** Verificado `5/2+δ=3` con `δ=½`. SOLID. **El paso Hurwitz (E3), auditado con severidad:**
> Si `ξ̂_λ→Ξ` **uniformemente en compactos** de la franja abierta `|Im z|<½` (de hecho
> `≤½+`), y cada `ξ̂_λ` tiene **sólo ceros reales**, entonces `Ξ` no tiene ceros en
> `0<|Im z|<½`. Esto es el teorema de Hurwitz correctamente aplicado: si `Ξ(z_0)=0` con `0<Im z_0<½`,
entonces por convergencia localmente uniforme (y `Ξ≢0`), para `λ` grande `ξ̂_λ` tiene un cero
en cualquier entorno de `z_0` — pero los ceros de `ξ̂_λ` son **reales**, contradicción.
**Válido.** Tres condiciones que verifico se cumplen:
1. **Convergencia localmente uniforme** en la franja: dada por la Reducción **si** `ε_loc=o(λ^{−½})` (esa es la hipótesis-núcleo, no probada). Correcto que es condicional.
2. **`Ξ≢0`** (límite no idénticamente nulo): sí, `Ξ` es la xi de Riemann. Correcto.
3. **Real-rootedness de los `ξ̂_λ`**: **es E1**, el gap. Hurwitz **hereda módulo E1**. **Subtileza de normalización/modo de convergencia (pregunta 3):** El documento afirma que la
normalización es "libre" por invariancia de Hurwitz: si `c_λ ξ̂_λ→Ξ` con `c_λ≠0` y `ξ̂_λ`
real-rooted, entonces `Ξ` real-rooted. **Esto es correcto** — multiplicar por `c_λ≠0` no crea
ni destruye ceros, y Hurwitz sólo mira ceros. **PERO** hay una sutileza real que el documento
roza pero no enfatiza: para aplicar Hurwitz se necesita convergencia **localmente uniforme con
límite ≢0**, y la cota `λ^{1/2}ε_loc` controla la diferencia `ξ̂_λ−Ξ` **ya normalizada**
(misma escala que `Ξ`). Si uno cambiara la normalización a `‖ξ̂_λ‖_{L²}=1` (como en III), el
límite sería `Ξ/‖Ξ_T‖_{L²}` y `‖Ξ_T‖_{L²}~√(logλ)→∞`, luego `c_λ→0` y el "límite" se
degenera a 0 — **Hurwitz no aplicaría** en esa normalización sin renormalizar de vuelta. El
documento es **consistente** (usa `ξ̂_λ(0)=Ξ(0)`, escala fija) pero la afirmación "la
normalización es libre" es **demasiado relajada**: es libre *módulo mantener el límite ≢0 y
finito*. Recomiendo precisar: la normalización debe ser tal que `c_λ ξ̂_λ` converja a un
límite **finito y no nulo** (i.e. `c_λ` acotado lejos de 0 e ∞ sobre la familia). Con
`ξ̂_λ(0)=Ξ(0)` esto se garantiza. **Veredicto: el paso Hurwitz es válido; la "libertad de
normalización" debe enunciarse como libertad módulo límite no degenerado.** SOLID módulo E1. **E4** (`Ξ∈LP ⟺ RH`): clásico (de Branges / Pólya). SOLID, sin objeción. --- ## 5. N5c (discriminante converso) — SOLID* módulo E1
**Lema N5c.1 (monotonía real-rooted `|g(x+iy)|≥|g(x)|`):** la prueba por el producto de
Hadamard es **correcta**: `g(z)=ce^{az+b}z^m∏(1−z/r_n)e^{z/r_n}` con `r_n,a∈ℝ`, y
`|1−(x+iy)/r_n|²=(1−x/r_n)²+(y/r_n)²≥(1−x/r_n)²`. El factor `e^{a(x+iy)}` tiene módulo `e^{ax}`
independiente de `y`. **Verificado.** (Requiere `g∈LP`, i.e. real-rooted, género ≤1 — esto es
E1, de nuevo.) La Prop N5c.2 (DH no converge off-axis) se sigue: en el cero off-line `z_0` de
`Ξ_f`, `|ξ̂_λ(z_0)−Ξ_f(z_0)|=|ξ̂_λ(z_0)|≥|ξ̂_λ(x_0)|→|Ξ_f(x_0)|>0`. La única hipótesis fina
es `Ξ_f(x_0)≠0`, que el documento justifica (proyección real de un cero off-line no es un cero
on-line). **Correcto, aunque conviene notar:** podría en principio existir un cero on-line de
`Ξ_f` que coincida con `x_0`; para DH esto es genéricamente falso y el argumento se sostiene,
pero es una hipótesis genérica, no incondicional al 100%. Inocuo. **SOLID* módulo E1.** Buen
resultado: certifica que `ε_loc` separa RH-verdadera de RH-falsa, con el lado falso probado. --- ## 6. Piezas RH-hard / condicionales — confirmación de etiquetas - **H1′ (QW PSD ⟺ RH-hasta-T*):** correctamente identificado como RH-equivalente. PF da estructura (fondo simple, envolvente positiva), **no** positividad espectral `ε_0≥0`. La corrección "PF≠PSD" es **correcta y honesta**. GAP=RH.
- **III:** teorema condicional correcto dado (H-gap)+(H-lim). La observación de que **(H-pos) `ε_0>0` ≈ Weil-pos ≈ RH-hasta-T*** ("la renormalización lleva RH horneada") es **aguda y correcta** — Davis–Kahan sobre `Â=A/ε_0` presupone `ε_0>0` con gap relativo, lo cual es justamente lo que se quiere demostrar. No es teorema incondicional. GAP condicional.
- **IV.1:** identificación del operador límite — refutadas las id. de coef. constante; la lectura "SL de 2º orden con coef. variables / núcleo de Loewner compacto" es razonable pero **no demostrada**. Es **análisis (Landau–Widom/de Branges), no RH-hard**. Coincido. GAP.
- **IV.2 ≡ §V:** la caracterización variacional ("ground state de Weil = `Ξ_T` ⟺ todos los `γ_ρ` reales ⟺ RH") es **correcta como equivalencia** y es **el núcleo RH**. Bajo RH, la forma `Σ_ρ|g(γ_ρ)|²≥0` es suma de cuadrados y su minimizador band-limited se anula en los `γ_ρ≤T*` (módulo rigor del déficit de frame Landau–Beurling). Sin RH es indefinida. **La etiqueta 🟥 RH-equivalente es correcta y honesta.** Lo que falta —la tasa `o(λ^{−½})`— **es** RH. Sin objeción a la etiqueta; el "rigor del déficit de frame" (`g_0=Ξ_T+O(ε_0)`) es un sub-gap real de teoría de Beurling–Landau, pero vive *bajo* la hipótesis RH, así que no rescata nada incondicionalmente. --- ## 7. Cerrable vs RH-hard (pregunta 4) **Cerrable (análisis genuino, no RH):**
- **IV.1** — identificar el operador de borde (Landau–Widom / de Branges). Análisis duro pero no RH. Cerrable en principio.
- **El "déficit de frame"** `g_0→Ξ_T` bajo RH (Beurling–Landau a densidad crítica). Cerrable, pero sólo refina el lado-RH del núcleo; no avanza incondicionalmente.
- **N1 matiz `x₀≠0`** y **retirar `Γ=O(1)`** → usar `O(logλ)`: correcciones expositivas triviales, cerrables ya. **Esencialmente cita obligada (no cerrable como prueba propia a este nivel):**
- **E1 real-rootedness** — al nivel de la info aislada (envolvente de-modulada positiva), el desajuste de fase carrier `ω*≠π` impide la vía Herglotz/HB elemental. Es **CCM Thm 1.1(iii)** (espectro real de la realización autoadjunta). Mi sub-caso `ξ_k>0` (Lema M1) está cerrado pero **no cubre el ground state real**. Cita obligada, no reparable con azúcar de funciones enteras. **RH-hard (el muro, no cerrable sin probar RH):**
- **IV.2 ≡ §V** — `ξ̂_∞=Ξ` / `ε_loc=o(λ^{−½})` / "ground state de Weil = `Ξ_T`". **Es RH.**
- **H1′ (`ε_0≥0`)** y **(H-pos) en III** — positividad de Weil = RH-hasta-T*. **Es RH.** --- ## 8. Conclusión del tribunal (fría) El programa CCM, auditado bajo lente de análisis complejo, es una **reducción correcta y
elegante de RH a un único núcleo RH-equivalente** (IV.2≡§V: el ground state de Weil es `Ξ_T`),
**rodeada de un andamiaje de aproximación genuinamente probado** (N0, N1, N2, N3, Reducción,
Hurwitz). Ese andamiaje **resiste la auditoría severa**: las pruebas de N0 (Γ incompleta),
N1 (medida armónica + Boas), N2 (Nikolskii) y N3 (Phragmén–Lindelöf) son **correctas**, y el
paso Hurwitz es **válido** módulo E1, con una precisión necesaria sobre la "libertad de
normalización" (debe preservar límite no degenerado). **Lo que cierro en mi lente (E1):** prueba elemental rigurosa (Herglotz, Lema M1) del sub-caso
`ξ_k>0`, e **identificación precisa** de por qué el ground state real (carrier `ω*≈0.966π`)
**no** cae en ese caso ni en su de-modulación, de modo que la real-rootedness **debe** citarse
de CCM Thm 1.1(iii) (realización autoadjunta / espacio de de Branges `H(E)`), no de un lema
de funciones enteras pendiente. Soy más severo que el documento aquí: **no es "cerrable con
más trabajo"; es cita obligada.** **Lo que permanece abierto:** (i) E1 sin prueba propia (cita obligada CCM 1.1(iii)); (ii) III
condicional con (H-pos)=RH; (iii) el núcleo IV.2≡§V que **es** RH. **No se prueba RH.** El
documento es **honesto**: no detecto auto-engaño en la localización. Las correcciones que pido
(retirar `Γ=O(1)`, precisar la libertad de normalización, severizar el estatus de E1 a "cita
obligada", marcar la hipótesis genérica en N5c) son **expositivas, no estructurales**. *— H., referee.*
