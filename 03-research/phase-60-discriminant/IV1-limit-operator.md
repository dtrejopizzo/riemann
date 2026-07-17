# IV.1 — Identificación del operador límite `Â_∞` (espectro `n²`) > **AVISO (2026-06-18, cierre honesto): la identificación "Dirichlet Laplaciano" de abajo
> está REFUTADA por los autovectores.** El test E12 (mpmath, λ=7, dim 29) da: autovectores
> crudos con 15–18 cambios de signo, envelope de-modulado `v_k·(−1)^j` con **10–13 nodos**
> (no 0,1,2,…), y overlap con los modos de Dirichlet `sin((k+1)π·)` de **sólo 0.04–0.35**.
> Conclusión: **`Â_∞` comparte el espectro `{n²}` de `−d²/dx²` pero NO es ese operador**
> (mismo espectro, distintos autovectores). El análisis IV.1a–c de abajo (símbolo `W_λ`,
> KMS/Parter/Widom) **tampoco cierra** porque el símbolo de Weil `W_λ` es INDEFINIDO (toma
> valores muy negativos: `2θ'(0)≈−5.4`, parte aritmética `−2ΣΛ(n)/√n` grande negativa),
> mientras `QW` es PSD con `ε_0>0` — así que `QW` **no es** la sección finita de
> multiplicación por `W_λ`. Las dos imágenes (símbolo y Dirichlet) eran erróneas.
> **IV.1 queda ABIERTO.** Ver §"Estado honesto" al final. --- ## (Intento refutado, conservado) El operador límite como Laplaciano de Dirichlet Identificación del operador renormalizado límite desde la estructura de la forma de Weil.
Resultado: el espectro `n²` (medido en E11) **no es un misterio** — es el espectro de
autovalores pequeños de un operador de sección finita (Toeplitz) cerca de un mínimo
no-degenerado de su símbolo, vía la teoría clásica de Kac–Murdock–Szegő / Parter–Widom. Marcadores: **[P]** probado · **[P\*]** módulo resultado clásico estándar · **[GAP]** núcleo. --- ## IV.1a — `A_λ` es una sección finita con símbolo de Weil `W_λ` — [P] Por la fórmula explícita de Weil, la forma cuadrática sobre funciones band-limited
`g=ξ̂∈PW_Ω`, `Ω=logλ`, es
``` A_λ(g,g) = ⟨ξ, QW ξ⟩ = (1/2π) ∫_{-Ω}^{Ω} |ĝ(t)|² W_λ(t) dt, W_λ(t) = 2θ'(t) − 2 Re Σ_{n≤λ²} Λ(n) n^{-1/2-it},
```
donde `θ'(t)=½ Re ψ(¼+it/2) − ½logπ` es la densidad arquimediana. En la base de muestreo
`{sinc_k}` (nodos `d_k`, transformada `ê_k(t)=e^{-id_k t}1_{[-Ω,Ω]}`),
``` QW[m,n] = (1/2π)∫_{-Ω}^{Ω} e^{-i(d_m-d_n)t} W_λ(t) dt + (correcciones de ventana),
```
es decir `QW` es la **matriz de sección finita** (Toeplitz, módulo la ventana de Fejér
`(1−y/L)` y el intervalo `[0,L]` que la vuelven Loewner asintóticamente Toeplitz cuando
`L→∞`) del **símbolo de Weil `W_λ`**. **[P]** (es la fórmula explícita; la corrección
Loewner→Toeplitz se desvanece a tasa `1/L=1/(2logλ)`). --- ## IV.1b — `W_λ` tiene un mínimo no-degenerado, valor `≈ ε_0 ≈ 0`, curvatura `c_λ>0` — [P] `W_λ` es par y suave en `(-Ω,Ω)`. La parte arquimediana `2θ'(t)`:
``` 2θ'(t) = Re ψ(¼ + it/2) − logπ,
```
es **par, con mínimo en `t=0`** (`ψ(¼+it/2)` crece con `|t|`; `θ'(0)=½ Re ψ(¼)−½logπ` es
el valor de fondo) y **curvatura** `θ''’`-controlada: `(2θ')''(0) = −¼ψ''(¼) > 0`
(`ψ''(¼)<0`), no-degenerada. La parte aritmética `−2Re Σ Λ(n)n^{-½-it}` es una
perturbación acotada y oscilante; cerca del fondo del pozo arquimediano la suaviza pero no
borra el mínimo no-degenerado (es el contenido del *frame/Landau–Beurling deficit*:
`W_λ(t_0) = ε_0 = O(C_0/λ²) ≈ 0`, el déficit de positividad). Así
``` W_λ(t) = ε_0 + c_λ (t−t_0)² + O((t−t_0)³), c_λ = ½(2θ')''(t_0) + (arith) > 0.
```
**[P]** existencia de mínimo no-degenerado (arquimediano convexo + perturbación acotada);
**[GAP-menor]** que la perturbación aritmética no cree un mínimo más bajo en `t_0≠0`
— equivale a positividad local de Weil cerca del fondo, esperable pero a verificar. --- ## IV.1c — Autovalores pequeños de la sección finita `∝ n²` (Dirichlet) — [P\*] **Teorema (Kac–Murdock–Szegő / Parter 1961 / Widom).** Sea `T_N` la matriz de sección
finita `N×N` de un símbolo Hermitiano `W` que alcanza un **mínimo no-degenerado**
`W_min` en un punto interior, `W(t)=W_min + c(t−t_0)² + o(·)`. Entonces los autovalores
pequeños de `T_N` por encima de `W_min` satisfacen, para `j=1,2,3,…` fijos y `N→∞`,
``` λ_j(T_N) − W_min ~ c · (π j / (N+1))² · κ,
```
con `κ` constante de escala. **Son los autovalores del Laplaciano de Dirichlet discreto.** *Razón estructural.* El símbolo del Laplaciano discreto `2−2cosθ = θ²+O(θ⁴)` es el
prototipo de mínimo cuadrático; su matriz de Toeplitz **es** exactamente el Laplaciano de
Dirichlet con autovalores `2−2cos(πj/(N+1)) ~ (πj/(N+1))²`. Todo símbolo con mínimo
cuadrático no-degenerado tiene la misma asintótica de autovalores bajos (universalidad del
mínimo). **[P\*]** (Böttcher–Grudsky–Spitkovsky, *Spectral properties of banded Toeplitz
matrices*, SIAM 2005; KMS 1953; Parter 1961). **Aplicación.** Con `W_min = ε_0 ≈ 0` (IV.1b), `ε_j ~ ε_0 + c_λ κ (π j/(N+1))²`. En el
régimen renormalizado, dado que `ε_0 ≈ 0` está por debajo del primer modo de caja, los
autovalores se ordenan como `ε_n ∝ n²` (`n=1,2,3,…`, sin modo cero — **condición de
Dirichlet** del borde de banda `t=±Ω` / del tamaño finito `N`). Por tanto
``` ε_k / ε_0 → (k+1)² = n² (k=0,1,2,…↔ n=1,2,3,…).
``` --- ## IV.1 — Conclusión > **`Â_∞`** (límite del Weil operator renormalizado) **es el Laplaciano de Dirichlet**
> `−d²/dt²` en el intervalo efectivo `[−Ω,Ω]`, con espectro `{n²}_{n≥1}`. **[P\*]** Esto **convierte la Conjetura IV (Conj 4.12 del paper) en un teorema** módulo dos inputs
clásicos/menores:
1. **[P\*]** la asintótica de Toeplitz de mínimo (KMS/Parter/Widom) — clásica.
2. **[GAP-menor IV.1b]** que el mínimo de `W_λ` es interior, no-degenerado y no desplazado por la perturbación aritmética — positividad local de Weil, verificada numéricamente (E11: `n²` mejora con `λ`), a cerrar analíticamente con la convexidad de `θ'` + cota de la oscilación aritmética `‖Σ Λ(n)n^{-½-it}‖_{C²}` en una vecindad del fondo. **Núcleo mínimo de IV.1:** el único punto no clásico es IV.1b (mínimo no desplazado), y es
**la misma positividad de Weil localizada al fondo del pozo** — un eco del §V, pero
*local* (un solo punto `t_0`), mucho más débil que el §V global. La estructura `n²`
en sí es robusta y clásica (2º orden + sección finita = Dirichlet). ### Sub-división para el futuro (núcleo extremo)
| Sub-pieza IV.1 | Estatus |
|---|---|
| IV.1a símbolo `W_λ` (fórmula explícita) | **[P]** |
| IV.1b mínimo no-degenerado, no desplazado | **[P]** existencia · **[GAP-menor]** no-desplazamiento |
| IV.1c bajo-espectro `∝ n²` (KMS/Parter/Widom) | **[P\*]** clásico |
| **IV.1 ⟹ `Â_∞`=Dirichlet, espectro `n²`** | **[P\*]** (módulo IV.1b) | Queda IV.2 (rigidez `n² ⟹ ξ̂_∞=Ξ`) y §V (positividad global bajo `/ε_0`). --- ## Estado honesto de IV.1 (tras la refutación) **Refutado (dos identificaciones falsas):**
1. `Â_∞ = −d²/dx²` Dirichlet — NO (autovectores no coinciden, overlap <0.35, nodos 10–13).
2. `QW =` sección finita de mult. por símbolo `W_λ` — NO (`W_λ` indefinida, `QW` PSD). **Sólido (no refutado):**
- `ε_k/ε_0 → (k+1)² = n²`, **medido robusto y mejorando con λ** (E11). Es el dato más estable de todo el programa.
- Fondo simple (H1, Perron–Frobenius). *Caveat:* el autovector "positivo" de H1 vive en una representación transformada; el `v_0` crudo tiene cambios de signo (carrier). La relación entre ambas representaciones (qué similaridad lleva `QW` a su forma Perron–Frobenius) **no está identificada** — y es parte del mismo misterio del operador. **Lo que el chain NECESITA de IV.1 (mínimo):** sólo el **gap relativo `γ>0`**
(`ε_1/ε_0 → 1+γ`), hipótesis del Teorema III (estabilidad relativa). Si se acepta `n²`,
entonces `γ=3` automático. Pero `n²` es **medido, no probado**. **Núcleo mínimo abierto de IV.1 (sub-dividido al extremo):**
> **IV.1★ — Probar `ε_1(λ)/ε_0(λ) ≥ 1+γ > 1` uniformemente en λ** (gap relativo acotado
> lejos de 1). Equivalente fuerte: identificar el operador `Â_∞` (cuyo espectro `n²` daría
> `γ=3`). La simplicidad (H1) da `ε_1>ε_0` pero **no** la cota uniforme del cociente. **Veredicto:** IV.1 **NO se cierra** con identificación de operador (ambas refutadas). Su
contenido se reduce a IV.1★ (gap relativo uniforme), que **sigue abierto** — empíricamente
sólido (`ε_1/ε_0→4`, estable, mejora con λ) pero no demostrado. El Teorema III queda
**condicional a IV.1★**. **Lección (anti-auto-engaño):** registramos la refutación en vez de esconderla. El `n²` es
real pero su operador no es el ingenuo; forzar "Dirichlet" habría sido un gap que vuelve.
Mejor un gap nombrado y honesto (IV.1★) que una proposición falsa.
