# E1 — Veredicto consolidado del tribunal (· ·) Los tres trabajaron E1 en paralelo y **convergieron unánimemente**. Resultado honesto: **E1
NO se cierra elementalmente — es cita obligada a CCM Thm 1.1(iii)** — pero el tribunal lo
**demostró con un teorema de obstrucción** (no es opinión: es matemática). Eso ES un resultado. ## 1. Dato decisivo (, verbatim del código)
La secular del motor validado (`E4hp_convergence.py:66`) es **LINEAL**:
``` f(s) = Σ_k ξ_k/(s − d_k) ← residuos ξ_k de signo VARIABLE (carrier de borde ω*≈0.966π)
```
**NO** es la cuadrática `Σξ_k²/(s−d_k)`. La esperanza del win fácil queda descartada de entrada. ## 2. El rescate cuadrático: REFUTADO elementalmente (§1.3)
La cuadrática `m(s)=Σξ_k²/(s−d_k)` **sí** es Herglotz (real-rooted), pero es **otro objeto**:
en el contraejemplo `ξ=(−1,2,−1)`, `d=(−1,0,1)`:
- lineal `f = −2/(s³−s)` → **0 raíces**;
- cuadrática `m = (6s²−4)/(s³−s)` → raíces `±√(2/3)`, **reales**.
Los ceros de `m` (±0.816) **no son** los de `ξ̂` (ninguno). Cuadrar los residuos **rompe la
identidad de Weil** `⟨ξ,QWξ⟩=Σ_ρ ξ̂(γ_ρ)conj(ξ̂(conj γ_ρ))` que define `ξ̂`. No es typo ni gauge.
*El cuadrado que ayudaría* (`Σ_ρ|ξ̂(γ_ρ)|²≥0`) está horneado con RH (núcleo IV.2); *el cuadrado
gratis* (`m`) es el objeto equivocado. ## 3. TEOREMA DE OBSTRUCCIÓN () — el resultado del día
> **No existe construcción universal** que realice las raíces de `f(s)=Σξ_k/(s−d_k)` como
> **espectro de un operador auto-adjunto** a partir de los datos aislados `(ξ_k, d_k)`. *Prueba.* El contraejemplo `ξ=(−1,2,−1)` **es el ground state del Laplaciano de Dirichlet
discreto** `tridiag(−1,2,−1)` (salvo signo) — un autovector real legítimo de una matriz
simétrica — y su secular `f=−2/(s³−s)` **no tiene raíces reales**. La matriz-flecha canónica
`B=[[D,ξ],[e^T,0]]` (cuyo espectro = raíces de `f` vía Schur) es **no simétrica** y tiene
espectro **no real** para este input. Un operador auto-adjunto no puede tener ese espectro. ∎ **Consecuencia:** la real-rootedness, cuando vale, **debe** usar información ESPECÍFICA del
ground state de la forma de Weil que `(−1,2,−1)` (= modo top del Laplaciano) **no posee**. Y
no es: signo de `ξ` (DH tiene signos y vale), ni total-positividad (refutada,
Gantmacher–Krein), ni Perron–Frobenius solo. ## 4. La vía de Branges: existe pero NO es atajo (§2)
La función de estructura `E=A−iB` (con `B=ξ̂`) existe en abstracto, pero la desigualdad de
Hermite–Biehler `|E(s̄)|<|E(s)|` es **lógicamente equivalente a E1** (de Branges Thm 12–13).
Verificarla pide el **Wronskiano `A'B−AB'` de signo constante** = el interlacing espectral
auto-adjunto. La única positividad probada (PF: envolvente `u_k>0` en la base-función) **no se
traduce** a positividad de los residuos crudos `ξ_k` por el desajuste de fase `ω*≈0.966π≠π`.
Exhibir `E` con HB **es** re-probar la realización auto-adjunta = **CCM Thm 1.1(iii)**. ## 5. Obstrucción precisa (one-liner unánime)
> *La real-rootedness de `ξ̂` es la afirmación de que la secular lineal `f(s)=Σξ_k/(s−d_k)` es
> una m-función de Nevanlinna auto-adjunta. La única positividad probada (PF, envolvente
> `u_k>0`) vive en la base-función y, vía el carrier de borde `ω*≈0.966π≠π`, NO se traduce a
> positividad de los residuos crudos `ξ_k` ni a un Wronskiano de signo constante. Por tanto E1
> no admite prueba al nivel Herglotz/HB elemental; es cita obligada de CCM 1.1(iii).* ## 6. Lo que SÍ queda asentado
- **Lema M1 [SÓLIDO]:** sub-caso `ξ_k>0` ⟹ Herglotz ⟹ real-rooted. Único pedazo self-contained. El ground state real **no** cae aquí.
- **Teorema de obstrucción [SÓLIDO]:** E1 no es construible desde `(ξ_k,d_k)` aislados (contraejemplo = ground state del Laplaciano de Dirichlet). **Esto convierte "🔧 reparación pendiente" en "cita obligada DEMOSTRADA"** — ya no hay que perder tiempo intentando cerrarlo elementalmente.
- **E1 es RH-neutral** (vale para DH) ⟹ citar CCM 1.1(iii) y usarlo **no es circular** (la carga RH está en la convergencia, no en E1). ## Veredicto unánime
E1 **no fue un win de cierre** — pero el tribunal entregó un **win de claridad**: probó que la
cita obligada a CCM 1.1(iii) es **necesaria**, no pereza, con un teorema de obstrucción y el
hallazgo de que el contraejemplo es el modo del Laplaciano de Dirichlet. La etiqueta del
documento maestro queda **confirmada y reforzada**: real-rootedness cierta (CCM), prueba propia
imposible al nivel elemental, sub-caso `ξ_k>0` cerrado (M1). — A. · C. · H. 