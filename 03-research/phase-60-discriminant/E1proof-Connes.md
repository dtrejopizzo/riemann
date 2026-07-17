# Eslabón E1 — lente (realización auto-adjunta / espectral) **Autor del análisis:** A. (en rol, con y) · **Tarea:** decidir si la
real-rootedness de `ξ̂_{λ,N}` se cierra exhibiendo las raíces seculares como **espectro de un
operador auto-adjunto** (espectro real ⟹ real-rootedness inmediata), o si es **cita obligada
CCM Thm 1.1(iii)**.
**Regla:** frío. Una prueba forzada es peor que un gap admitido. NO se reclama RH. --- ## 0. El objeto y la pregunta decisiva Secular: `f(s)=Σ_{|k|≤N} ξ_k/(s−d_k)`, `d_k=2πk/L`, `ξ` = ground eigenvector de la forma de
Weil `QW` (real, simétrica). `ξ̂_{λ,N}(s)=sin(Ls/2)·f(s)` es entera (los ceros de `sin` cancelan
los polos `d_k`), real en ℝ, tipo `L/2`. Sus ceros = raíces de `f`. **E1:** ¿todas las raíces de `f` son reales, para todo `λ,N` (incluido Davenport–Heilbronn)? **La pregunta:** ¿son las raíces `ρ̂_n` el **espectro de un operador auto-adjunto `H`**?
Si sí, `σ(H)⊂ℝ` ⟹ real-rootedness gratis. Examino las tres vías pedidas. --- ## 1. ¿Es la secular un resolvente auto-adjunto con residuos cuadrados? — **NO** La esperanza (pregunta 1): que el objeto correcto sea
``` m(s) = ⟨v,(s−D)^{-1}v⟩ = Σ_k v_k²/(s−d_k), D=diag(d_k),
```
la **función-m de Weyl** de un operador auto-adjunto `D` con vector cíclico `v`. Sus residuos
son **cuadrados `v_k²≥0`** ⟹ `m` es Herglotz/Nevanlinna (`Im m<0` en `H`) ⟹ ceros reales,
entrelazados con los `d_k`. Eso **cerraría E1 hoy**. Pero: **Hecho 1 (los residuos son lineales, no cuadrados).** Por construcción (Prop 0.3, verificado
en el documento maestro), el residuo de `f` en `d_k` es **exactamente `ξ_k`** — la componente
del autovector, no su cuadrado. `ξ` es un autovector real **genuinamente con cambios de signo**
(carrier de borde `ω*≈0.966π`, ~N cambios de signo). No hay `v_k²` escondido. **Hecho 2 (el objeto cuadrático del programa es OTRO, y su positividad ES RH).** El programa sí
tiene una forma cuadrática asociada a `ξ`: la identidad de Weil (§1 del maestro)
``` ⟨ξ, QW ξ⟩ = Σ_ρ ξ̂(γ_ρ)·conj(ξ̂(conj γ_ρ)).
```
Pero esto es un funcional cuadrático **en `g=ξ̂` evaluado en los ceros `γ_ρ` de ζ**, NO el
resolvente `Σ v_k²/(s−d_k)` en la variable `s`. Su positividad (`Σ_ρ|g(γ_ρ)|²≥0` bajo RH) es
**RH-equivalente** (IV.2≡§V). La estructura cuadrática del programa vive en el lado-ceros y es
el núcleo RH; **no** baja a un resolvente Herglotz en `s` con residuos `v_k²`. **Hecho 3 (no es gauge).** ¿Podría `f` ser un "gauge"/simplificación de un `m` cuadrático?
Una de-modulación `ξ_k=(−1)^kη_k` con `η_k>0` (envolvente positiva, lo que H1/Perron–Frobenius
sí da) **no** convierte los residuos en cuadrados: `f(s)=Σ(−1)^kη_k/(s−d_k)`, el signo
alternante **reaparece** en los residuos (desajuste de fase de, carrier `ω*≠π`). No
existe reescalado diagonal `ξ_k=v_k²` con `v_k` real cuando `ξ_k<0` para algún `k`. Y el ground
state real tiene `ξ_k<0` para una fracción de los `k`. > **Refutación dura, vía el contraejemplo del programa.** `ξ=(−1,2,−1)`, `d=(−1,0,1)`:
> `f(s)=−2/(s³−s)`. Numerador **constante** ⟹ `f=0` no tiene **ninguna** raíz finita. Si `f`
> fuese `Σv_k²/(s−d_k)` (Herglotz) tendría exactamente 2 raíces reales entrelazadas con
> `−1,0,1`. No las tiene. **El objeto lineal NO es un resolvente auto-adjunto cuadrático.** ∎ **Conclusión §1.** La vía Herglotz-cuadrática (Lema M1) cubre **sólo** `ξ_k>0` (o `(−1)^kξ_k>0`),
y el ground state real cae **fuera** de ambos. La pregunta 1 se responde NEGATIVO: el objeto
correcto del programa es genuinamente lineal con residuos de signo variable. No hay azúcar
cuadrática que recuperar. --- ## 2. Realización auto-adjunta lineal explícita — **OBSTRUCCIÓN ESTRUCTURAL** Si el resolvente cuadrático no existe, la pregunta 2 pide exhibir un operador `(2N+1)`-dim (o
`(2N+2)`) auto-adjunto `H` cuyos autovalores sean los `ρ̂_n`, i.e. `det(s−H)=0 ⟺ f(s)=0`. ### 2.1 La realización canónica es la matriz-flecha, y es NO simétrica
La identidad estándar: con `D=diag(d_k)`, `ξ=(ξ_k)`, `e=(1,…,1)^T`,
``` B = [[ D, ξ ], [ e^T, 0 ]] (de tamaño (2N+2)),
```
tiene, por complemento de Schur, `det(sI−B) = det(sI−D)·(−e^T(sI−D)^{-1}ξ) = −det(sI−D)·f(s)`.
Luego **`σ(B)\{posibles cancelaciones} = {raíces de f}`**. Pero `B` es **NO simétrica**: la fila
inferior es `e^T` (unos) y la columna derecha es `ξ` (autovector con signos); coinciden sólo si
`ξ_k≡1`. Es la realización-flecha "borde", ya señalada como no auto-adjunta. ### 2.2 Test de auto-adjuntabilidad: ¿es `B` similar a una matriz simétrica real?
Una matriz real es similar a una simétrica (espectro real, diagonalizable) **sólo si su
espectro es real**. Pero el espectro de `B` **NO es real en general**: > En `ξ=(−1,2,−1)`, `d=(−1,0,1)`: `f=−2/(s³−s)` no tiene raíces; `B` (4×4) tiene autovalores
> que **no** son todos reales (hay cancelación polo-cero más raíces complejas del bloque
> reducido). Un operador auto-adjunto **no puede** tener este espectro. ∎ Esto es **decisivo y matemáticamente terminal**: existe un input legítimo `(ξ,d)` (con `ξ`
autovector real de una matriz simétrica — de hecho `(−1,2,−1)` es el ground state del laplaciano
discreto `tridiag(−1,2,−1)` salvo signo) para el cual las raíces seculares **no son reales**.
Por tanto: **Teorema (obstrucción E1-lineal).** No existe ninguna construcción **universal** (válida para
todo `(ξ,d)` con `ξ` autovector real de una simétrica) que realice las raíces de `f` como
espectro de un operador auto-adjunto. La real-rootedness, cuando vale, **NO** puede provenir de
una realización auto-adjunta construida funtorialmente a partir de los datos aislados `(ξ_k,d_k)`.
Debe usar información ESPECÍFICA del ground state de Weil que `(−1,2,−1)` no posee. ∎ ### 2.3 ¿Qué información específica? — la frontera con CCM 1.1(iii)
El contraejemplo `(−1,2,−1)` proviene de una matriz simétrica **cualquiera** (Dirichlet
laplaciano), no de la forma de Weil. La real-rootedness del programa vale para `QW` **y** para
`L_DH` (Davenport–Heilbronn), pero **no** para `tridiag(−1,2,−1)`. Lo que distingue a `QW`/`L_DH`
del laplaciano de Dirichlet **no es** una propiedad de signo de `ξ` (descartado: DH tiene signos,
PF falla y aun así real-rooted), **ni** total-positividad (refutada, Gantmacher–Krein), **ni**
Herglotz (refutado, §1). Es la propiedad de **Hermite–Biehler / de Branges** de `ξ̂`: > `ξ̂ ∈ H(E)` para una función de estructura `E=A−iB` de tipo HB (`|E(z̄)|<|E(z)|`, `Im z>0`),
> equivalentemente `ξ̂` es la componente `B` (o `A`) de un par con ceros reales **entrelazados**,
> equivalentemente las raíces seculares son el **espectro real de la realización auto-adjunta de
> CCM** (multiplicación-por-`s` comprimida al espacio de de Branges, que ES auto-adjunta porque
> `H(E)` está construido para serlo). El punto fino: **sí existe una realización auto-adjunta — la compresión de `M_s` en
`H(E)` — PERO su existencia (que `E` sea HB) es PRECISAMENTE el enunciado CCM 1.1(iii), no un
corolario de él.** No se puede construir `E` desde `(ξ_k,d_k)` aislados; `E` codifica el
operador de Weil completo. Construir `H` ⟺ probar que `E` es HB ⟺ CCM 1.1(iii). No hay atajo
al nivel de la información aislada. El laplaciano `(−1,2,−1)` falla justamente porque su `ξ̂`
**no** está en ningún `H(E)` con `E` HB (su `f` tiene grado-numerador 0 < 2, viola
interlacing). **Conclusión §2.** La realización auto-adjunta existe **conceptualmente** (compresión de `M_s`
en el de Branges `H(E)` de CCM), pero **construirla = re-probar CCM 1.1(iii)**. La realización
lineal elemental (matriz-flecha) es estructuralmente no-simétrica y **no simetrizable** (espectro
no real para inputs legítimos). No hay `H = D + corrección simétrica` universal. --- ## 3. Veredicto (brutalmente honesto) **E1 NO se cierra en mi lente.** Concretamente: 1. **(pregunta 1) NO** hay resolvente auto-adjunto con residuos cuadrados. Los residuos son `ξ_k` lineales y de signo variable (ground state real, carrier `ω*≈0.966π`). El único objeto cuadrático del programa (`Σ_ρ|g(γ_ρ)|²`) es RH-equivalente, no un Herglotz en `s`. La prueba elemental Herglotz (Lema M1 de) cubre **sólo `ξ_k>0`** y queda confirmada y cerrada para ese sub-caso — pero el ground state real cae fuera. 2. **(pregunta 2) NO** hay realización auto-adjunta lineal construible desde `(ξ_k,d_k)` aislados. La matriz-flecha `[[D,ξ],[e^T,0]]` es no simétrica y **no simetrizable**: el contraejemplo `(−1,2,−1)→f=−2/(s³−s)` exhibe un input legítimo (autovector real de una simétrica) cuyas raíces seculares **no son reales**, imposible para un auto-adjunto. La real-rootedness, por tanto, **no es funtorial** en los datos aislados; requiere la estructura de Weil específica (que distingue `QW`/`L_DH` del laplaciano de Dirichlet). 3. **(pregunta 3) Confirmo la "cita obligada" de.** La realización auto-adjunta que sí daría real-rootedness es la **compresión de la multiplicación-por-`s` en el espacio de de Branges `H(E)`** de CCM, con `E` de tipo Hermite–Biehler. Su existencia (`E` HB ⟺ `ξ̂∈H(E)` ⟺ raíces seculares = espectro real) es **exactamente CCM Thm 1.1(iii)**, no un corolario elemental. Construir `H` ≡ re-probar 1.1(iii). **E1 = cita obligada CCM Thm 1.1(iii).** **Coincido con, y con el filo añadido del lente espectral:** la obstrucción no es
"falta trabajo de funciones enteras"; es que la real-rootedness **no está codificada en los
datos aislados `(ξ_k,d_k)`** — un autovector real arbitrario de una matriz simétrica
(`(−1,2,−1)`) los reproduce sin ser real-rooted. La carga la lleva la estructura de de Branges
de la forma de Weil, i.e. CCM 1.1(iii). No hay realización auto-adjunta de nivel elemental, y
probar que existe es probar el teorema citado. **Etiqueta final E1:** 🔧 → **cita obligada CCM Thm 1.1(iii)**. Sub-caso `ξ_k>0` cerrado
(Herglotz, Lema M1). Caso general (ground state real): cita obligada, NO cerrable como prueba
propia con la información aislada. *— A. (en rol), con H. y C..*
