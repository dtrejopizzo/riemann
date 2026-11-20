# Ronda 16, memo B — estados KMS sobre álgebras donde actúan juntas la suma y el producto de ℕ

Idea sometida a la puerta: obtener el signo de `a_T` como `φ(x*x)`, o como derivada o valor de borde de expresiones de ese tipo, para un estado KMS `φ` de un sistema C*-dinámico en el que `+` y `·` de ℕ actúan juntos: Bost–Connes `(ℚ⋊ℚ_+^*, ℤ⋊1)`, el álgebra de Toeplitz `𝒯(ℕ⋊ℕ^×)` de Laca–Raeburn, `𝒬_ℕ` de Cuntz y las álgebras de anillo de Cuntz–Li.

**Veredicto: repetición.** La semilla figura casi literalmente en el corpus y la rama se detiene en el cotejo. Este memo deja tres observaciones nuevas y cortas: la §2 muestra por qué la propuesta concreta no puede funcionar, la §3 corrige el análisis del control `c = 2` y la §4 señala el único punto que queda sin excluir. No hay construcción.

## 0. Filtro de cuatro puntos

1. **Antecedente más cercano, leído en fuente primaria.**
   - `03-research/phase-193-creation-campaign/CA_E_000_SEEDS.md`, §E1: «KMS phase transitions beyond Bost–Connes (Laca–Raeburn Toeplitz algebra of ℕ⋊ℕ^×; Cuntz–Li ring algebras)». Se DESCARTÓ porque la positividad KMS sólo vale para `β` real, por O11 (Beurling), por (R)(2) (falta el factor Γ) y por ser un reintento de 114_d_116.
   - `03-research/phase-114-closing-the-four-rows/114_d_116_KMS_MODULAR_CONTACT_AUDIT.md` (Bost–Connes). Sus conclusiones:
     - el estado de Gibbs es de clase traza sólo para `β > 1`;
     - la varianza modular tiene coeficiente `Λ log n` y no `Λ`;
     - la invariancia temporal diagonaliza la matriz de dos puntos;
     - falta el determinante Γ.
   - Otros antecedentes:
     - `phase-67-quantum-q-index/E67_8_RESULTS.md`: las isometrías de semigrupo detectan divisibilidad y no distancia logarítmica.
     - `159 G1` (celda 4H): Bost–Connes, Borger/Witt, DEAD.
     - `G8H` Thm U: el flujo del núcleo es el mismo para ζ, Beurling y Bost–Connes.
     - R9-04 y P51-2: la función de partición es ζ(β).
     - README del índice, frente E de la fase 193: «KMS beyond Bost–Connes … dead».
   - `AUDIT_PHASE193_CERTAINTY.md`, fila 12: el descarte de E1 es «CIRC on O11; "real β only" ARG». Es decir, la parte Beurling del descarte era circular.
2. **Lo nuevo que propone la consigna.** Dos cosas:
   - la relación mixta exacta `v_p s = s^p v_p` como el lugar donde falla Beurling (esto responde precisamente a la cláusula CIRC O11);
   - el elemento suavizado `x_F = ∫F(t)σ_t(y)dt`.
3. **¿Esquiva la dificultad?** Sólo en parte:
   - sí responde a O11, porque Beurling no tiene anillo y por tanto no tiene relación mixta;
   - no responde a la diagonalidad de 114_d_116 ni a (R)(2);
   - la §2 prueba que la forma bilineal suavizada vive en la variable dual equivocada;
   - la §3 prueba que la estructura de anillo no rompe `c = 2`.
4. **Conexión global.** Haría falta una identidad `a_T(F) = φ(x_F*x_F) + (resto ≥ 0)` válida para todo `T`. La §2 descarta la forma de dos puntos KMS. No queda ninguna identidad candidata.

## 1. Cotejo: qué se hizo y qué clase cerró cada cosa

| Objeto | Lugar | Cierre |
|---|---|---|
| Gibbs de Bost–Connes, `H ε_n = log n ε_n`, energía media `Σ Λ n^{−β}` | 114_d_116 | NO-GO de la clase covarianza KMS: dos puntos diagonal, varianza con `Λ log n`, `β = ½` de tipo III |
| `𝒯(ℕ⋊ℕ^×)`, Cuntz–Li, transición de fase | CA_E_000 E1 | DESCARTE: `β` real, O11 (CIRC), (R)(2) |
| Bost–Connes, Witt, sitio de escala | 159 G1, G1_B5_R3–R5 | DEAD (muros OT-5′, instalación) |
| Isometrías de `ℕ^×` (semigrupo de Cuntz), Haar | phase-67 E67.4 y E67.8 | NO-GO: la ortogonalidad destruye la interferencia; se lee la divisibilidad |
| Flujo del núcleo III_1 | G8H, Thm U | DEAD (F3: el mismo para Beurling y Bost–Connes) |
| Espacio de clases de adeles (`ℚ⋊ℚ^*` sobre `𝔸`) | fases 158 y 159 | reformulación de la fila D, no cierre |
| Tomita, Araki/Petz, Golden–Thompson | frente E de la 193 | dead |

## 2. Lema V (variable dual). PROVED

**Enunciado.** Sea `(A, σ)` cualquier sistema C*-dinámico, `φ` un estado `σ`-invariante (en particular, un estado KMS_β), `y ∈ A`, y `x_F = ∫F(t)σ_t(y)dt`. Entonces existe una medida positiva finita `μ_y` en ℝ tal que

`φ(x_F* x_F) = ∫ |F̂(ξ)|² dμ_y(ξ)`.

En el sistema de Bost–Connes, con `y = Σ a_n μ_n` y el estado de Gibbs, se tiene `μ_y = Σ |a_n|² n^{−β} δ_{log n}`. Por tanto

`φ(x_F* x_F) = Σ |a_n|² n^{−β} |F̂(log n)|²`.

**Demostración.**
1. Por invariancia, la función de dos puntos `g(u) = φ(y* σ_u(y))` es definida positiva.
2. Por Bochner, `g = μ̂_y`.
3. Al integrar contra `F(t)F(s)` se obtiene la fórmula general.
4. En Bost–Connes, la invariancia hace ortogonales los `μ_n` de energía distinta, que es justamente lo que observa 114_d_116.

**Consecuencia.** El suavizado de la dinámica evalúa `|F̂|²` en las frecuencias `log n`. La parte prima de `a_T` es `Σ v_n c_F(log n)` y evalúa la autocorrelación en los retardos `log n`. Son transformadas de Fourier una de otra. Si se escribe la parte prima en frecuencia, queda `∫|F̂|² Σ v_n cos(ξ log n) dξ/2π`. Esa densidad no es positiva, así que no es la `μ_y` de ningún estado invariante.

El núcleo `Σ a_n n^{i(s−t)}` que sugería la consigna está, por tanto, en la variable equivocada. Pasar de una variable a la otra exige la fórmula explícita, es decir el lado espectral, y la reconstrucción desde ese lado ya está cerrada en el corpus (fase 155, vía inversa). Esto subsume la observación de diagonalidad de 114_d_116 y la extiende a todo estado invariante y a todo `y`.

**Restricción del lema.** Vale para la clase «forma cuadrática en `F` del tipo `φ(x_F*x_F)` con `x_F` un suavizado de la dinámica». No excluye un `x_F` que dependa de `F` de otra manera, por ejemplo por desplazamiento aditivo `s`. Ese caso queda abierto en la §4.

## 3. El control `c = 2`: corrección y lema. PROVED

**Corrección.** La consigna sugería que `c = 2` era un reescalado de `β` mediante `H ↦ 2H`. Es falso: `2H` tiene espectro `log n²`, que mueve las posiciones y no duplica el peso. El modelo correcto de `ζ(β)²` es el sistema producto tensorial.

**Lema A (anillo `ℤ×ℤ`).** El álgebra `ax+b` del anillo `R = ℤ×ℤ` es `𝒯(ℕ⋊ℕ^×) ⊗ 𝒯(ℕ⋊ℕ^×)`, con:
- grupo aditivo `ℤ²`;
- monoide multiplicativo `(ℕ^×)²` actuando coordenada a coordenada;
- energía `log(mn)`.

Sus relaciones mixtas `v s = s^p v` valen exactamente en cada coordenada, su función de partición es `ζ(β)²` (o `ζ(β−1)²` en la versión de Toeplitz) y `−∂_β log Z = Σ 2Λ(n) n^{−β}`.

**Demostración.** Se obtiene por la universalidad de Laca–Raeburn en cada factor (CITED), tomando el producto tensorial de los estados de Gibbs.

**Consecuencia: «suma y producto» no rompe `c = 2`.** Considérese un certificado cuyo signo use sólo cuatro ingredientes:
- positividad de estados;
- relaciones de anillo `+/·`;
- KMS;
- la identificación del peso con `−∂_β log Z_R`.

Aplicado a `R = ℤ×ℤ`, ese certificado produce la forma con peso `2Λ`. Por el Lema T de la ronda 13, entonces demuestra algo falso.

**Lo que sí separa `c = 2`.** Si el término arquimediano también se lee del anillo (`R⊗ℝ = ℝ²`, factor `Γ_ℝ²`), el anillo `ℤ×ℤ` produce `2a_T` y no el control. El control es `Arch − 2·primos`, y ningún anillo lo realiza: el rango de `R⊗ℝ` es 1 y el peso es 2, y esas dos cosas no concuerdan. Por lo tanto, la única palanca de signo contra `c = 2` dentro de esta clase es acoplar el factor Γ con el peso a través del rango del grupo aditivo.

- **Borrado de una potencia de primo (PROVED).** `ζ(s)·exp(−p^{−ks}/k)` no tiene coeficientes enteros no negativos. No es la función de partición de ningún semigrupo, así que ningún sistema de anillo lo realiza.
- **Beurling (ARGUED).** No hay anillo, y por tanto no hay `s` con `v_p s = s^p v_p`. Esto repara la cláusula CIRC O11 para esta clase, pero no basta por sí solo.

## 4. Lo que queda sin excluir, y sin objeto escrito

El cotejo de la §3 dice qué haría falta: un único objeto que lea el factor Γ y el peso de Euler en un mismo paso, a través del rango del grupo aditivo. En esta clase, ese objeto es la acción de `ℚ⋊ℚ_+^*` sobre `𝔸` con su lugar real. Eso es el espacio de clases de adeles, que las fases 158 y 159 ya cerraron como reformulación. Por eso no se construye.

Tampoco se excluyen los `x_F` construidos con el desplazamiento aditivo `s` en lugar del suavizado de `σ`. La §2 no los cubre. Pero no se dispone de una identidad que conecte `φ(x_F*x_F)` con `c_F(log n)`. Queda OPEN y sin candidato.

**Pregunta sobre `P_T` (ARGUED, sin identidad).** Las condiciones `∫F e^{±t/2} = 0` equivalen a `F̂(∓i/2) = 0`, es decir, a anular `x_F` continuado al tiempo imaginario `∓i/2`. Esto corresponde al borde de la banda KMS para `β = 1`, donde el estado de Gibbs muere por el polo. No se encontró ninguna identificación de `P_T` como núcleo de dos funcionales de polo en el espacio GNS que llevara a un signo.

## 5. Qué debe re-derivar el revisor

- El Lema V.
- El Lema A: que `𝒯(ℕ⋊ℕ^×)^{⊗2}` sea el álgebra `ax+b` de `ℤ×ℤ` con peso `2Λ`.
- El argumento de que `exp(−p^{−ks}/k)` rompe la integralidad.
