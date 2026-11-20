# Ronda 25, memo B — Ataque lógico al esquema «existencia + rigidez» (R)/(E)/(WF)

Notación del enunciado común: `a^w_T(F) = Arch(F) − Σ_{n≥2} w_n c_F(log n)` en `P_T`, `v_n = 2Λ(n)/√n`, `d = w − v`,
`D(τ) = Σ d_n (n^{iτ} + n^{−iτ})`. Fuentes abiertas: ROUND_021_A §1 (familia `Π_T(M∗φ)`, identidad (1.1), cotas
(1.2)–(1.3)), ROUND_022_A filtro, ROUND_024_A §2 (perfil de `M`, capa de borde), P47 `thm:coer-schur` (l.≈5239),
`rem:coer-size`, `thm:index` (l.2527–2532). No abiertos: ROUND_019_A completo, P46 thm:radical (sólo vía citas de 021_A).
Índice: sólo grep (l.486 «rigidez multigenerador», l.1861 «único peso δ_{N=1}», l.558–559 borrados/Beurling);
no se abrieron esos memos: el cotejo de novedad no es parte de este memo.

## Veredictos

| Paso | Veredicto |
|---|---|
| (R) rigidez | **FALSO tal como está argumentado** (hueco concreto §1); queda una versión débil correcta, y el resto es OPEN |
| (E) existencia | **CORRECTO** (con la cota de caja de §2, que hay que escribir) |
| (WF) dualidad | **CORREGIBLE**: vale con clausura; «v único multiplicador» es FALSO a T fijo |
| (d) circularidad | `K_T ≠ ∅` es **estrictamente más débil** a T fijo; ∀T equivale al objetivo sólo si vale (R) |
| (e) controles | coprimos-con-p: predicción no trivial (WF falla), consistente; Beurling: la cadena se corta en (R) |

## §1 (R): dónde se rompe

**Lo que sí funciona (ARGUED, sobre las cotas de ROUND_021_A).** Sea `φ ∈ C_c^∞` de longitud `ℓ` fija y `X = Π_T(M∗φ)`.
Por (1.3), `a^v_T(X)/‖X‖²` es doble-exponencialmente pequeño cuando `T → ∞` con `ℓ` fijo. Además `c_{M∗φ}` decae
doble-exponencialmente fuera de `[−2ℓ−C, 2ℓ+C]`, así que sólo entran los `n ≲ e^{2ℓ+C}`: es una suma finita, independiente
de `T`. El truncamiento `Π_T` cuesta `≤ (Σ_{n<e^{2T}} |d_n|)·e^{cT}e^{−2πe^{2(T−ℓ−O(1))}}`. Esto se absorbe si
`|d_n| ≲ log n`, cota que da §2 a partir de la propia hipótesis: **sí hace falta acotar w**, y la hipótesis lo hace.
El signo de `w` no interviene. Normalizando, `a^w_T ≥ 0 ∀T` da
`⟨|Φ_M|² D, |φ̂|²⟩ ≤ 0` para toda `φ ∈ C_c^∞`. Por Bochner–Schwartz, `−|Φ_M|²D` es una medida positiva. Luego:

  **(R′)** `D ≤ 0` como distribución en `ℝ \ Z`, donde `Z` es el conjunto (discreto) de ceros de `Φ_M(½+iτ)`.

**El hueco.** La familia casi radical tiene `|X̂|² = |Φ_M|²|φ̂|²`, que se anula en `Z`: **no ve `D` sobre `Z`**. El paso
«`D ≤ 0` en media local + media cero ⇒ `D = 0`» exige `D ≤ 0` en todo `ℝ`. Con `D ≤ 0` sólo fuera de `Z`, el argumento de
Fejér (`D̂` se anula en `(−log 2, log 2)`; se convoluciona con el núcleo de Fejér `K ≥ 0`, `supp K̂ ⊂ (−log 2, log 2)`, y
se obtiene `D∗K ≡ 0`) sólo prueba que la parte de `D` fuera de `Z` es compensada por una distribución soportada en `Z`.
**Contraejemplo al argumento (no al enunciado):** `d = −s v`, `0 < s < 1`, es decir `w = (1−s)v`. Por la fórmula explícita
(CITED, Weil), `D_v = A − (masas en Z)`, con `A > 0` una densidad lisa. Así `D = −sA + s·(masas en Z)`, que es `≤ 0`
fuera de `Z`: pasa todos los tests casi radicales. Directamente, `a^{(1−s)v}_T(X) = (1−s)a^v_T(X) + s·Arch(X)`, y `Arch(X) > 0`
en esa familia. Excluir `(1−s)v` exige información sobre las direcciones donde Arch es negativa
(`n_−(Arch|P_T) ≥ 1` desde `T*_ev`):
`a^{(1−s)v}_T ≥ 0 ⟺ s ≤ s_T := inf_{Arch(F)<0} a^v_T(F)/(a^v_T(F) − Arch(F))`, y (R) necesita `inf_T s_T = 0`. Ese
enunciado es cuantitativo, independiente y OPEN. Más en general, (R) se reduce a clasificar los pares `(D, Z)`:
distribuciones con espectro en `±log ℕ_{≥2}` que son `≤ 0` fuera de `Z` (tipo cuasicristal de Fourier). OPEN; ninguna fuente
del corpus abierta lo resuelve.
**Media cero y ventana T:** el argumento de media cero sobrevive (la suma es finita a `ℓ` fijo y Fejér la controla
exactamente), pero no es ahí donde falla.
**Pesos de otras funciones:** con el mismo factor arquimediano y conductor 1 no hay otro candidato en grado 1. Los
caracteres pares de conductor `q` añaden `(log q)c_F(0)`, que no está en la forma. No hay contradicción con lo conocido.

## §2 (E): cota de caja y límite inverso

**K_T acotado (sketch PROVED).** Para cada `n < e^{2T}` se toma `F = f ± f(·−log n)` con `f` de anchura
`h < min(log 2, min_{m≠n}|log m − log n|)/2 ≍ 1/n`. Se corrige con `u_±` fijos para entrar en `P_T`; la corrección es `O(‖f‖_{L¹}) = O(h^{1/2}‖f‖)`.
Entonces `c_F(log m) ≈ 0` para `m ≠ n` y `c_F(log n) = ±‖f‖²`, y `Arch(F) ≤ (log(1/h)+C)‖F‖²`.
Por tanto `|w_n| ≤ C(log n + 1)`. Además `K_T` es cerrado (intersección de semiespacios) y convexo.
**Restricción:** la extensión por cero preserva `∫F e^{±t/2}`, `c_F` y `Arch` (local, P47: `a_T = W_*` sobre funciones
soportadas en `I`). Así `a^{w}_{T'}(F) = a^{w|_{n<e^{2T}}}_T(F)` para `F ∈ P_T`, y la restricción manda `K_{T'}` en `K_T`. CORRECTO.
**Límite inverso:** basta una sucesión `T_k ↑ ∞`, porque toda ventana está contenida en alguna de ellas. Un límite inverso de
compactos no vacíos es no vacío (Tychonoff). Da `w` con `a^w_T ≥ 0` para TODO `T`. CORRECTO.

## §3 (WF): enunciado exacto

`C_T := {(Arch(ρ), (c_ρ(log n))_{2≤n<e^{2T}}) : ρ ⪰ 0 de traza finita, rango en P_T, Arch(ρ) < ∞} ⊂ ℝ^{1+N}`.
Separación en dimensión finita: existe `(1, −w) ∈ C_T*` ⟺ `C_T* ⊄ {λ ≤ 0}` ⟺ `(−1, 0) ∉ cl C_T`.

**Enunciado probable (PROVED, separación estándar):**
- Pesos con signo: `K_T ≠ ∅` ⟺ no existe una sucesión `ρ_k` con `Arch(ρ_k) → −1` y `c_{ρ_k}(log n) → 0` para todo `n < e^{2T}`.
- Pesos `w ≥ 0`: lo mismo con `c_{ρ_k}(log n) → p_n ≥ 0` (se usa el cono `C_T + {0}×(−ℝ^N_+)`).

**Versión con «existe ρ exacto»:** exige que `C_T` sea cerrado. No está probado. `Arch` está acotada inferiormente en `P_T`,
pero la traza puede explotar: masa en las `n_−` direcciones negativas compensada por masa positiva. Además
`ρ ↦ c_ρ(log n)` no es débil-* continua, porque la traslación no es compacta. No hace falta Slater en el lado dual
(dimensión finita); la dificultad está en la clausura del primal. CORREGIBLE: enunciar con sucesiones o con `cl C_T`.
**«v es el único multiplicador»:** FALSO a `T` fijo. Para `T ∈ (½log3, T*_ev)`, `T*_ev ∈ (0.58, 0.60)`, P47 thm:index da
`n_−(Arch|P_T) = 0`, luego `0 ∈ K_T`; y `v ∈ K_T` (Teorema A hasta `log 2`). La unicidad sólo valdría en el límite y
depende de (R).

## §4 (d) Circularidad y T pequeño

- `T < ½log 2`: no entra ningún `n`. `K_T = {∅}` es no vacío ⟺ `Arch ≥ 0` en `P_T` ⟺ el objetivo en esa ventana: coinciden.
- `n = 2` entra en `T = ½log 2 ≈ 0.347`; `n = 3`, en `½log 3 ≈ 0.549`. Para `T < T*_ev` se tiene `0 ∈ K_T`: `K_T ≠ ∅` es
  **trivial**, mientras que `a^v_T ≥ 0` en esa ventana es contenido real (P47 Teorema A). Por tanto, a `T` fijo,
  `K_T ≠ ∅` es estrictamente más débil.
- `T > T*_ev`: `0 ∉ K_T`, y `K_T ≠ ∅` ya no es trivial. No conozco certificado de `K_T ≠ ∅` que no sea exhibir `v`.
- ∀T: `[K_T ≠ ∅ ∀T] ⟸ objetivo` siempre. `⟹` es CONDITIONAL a (R) completo, que hoy es OPEN (§1). La
  formulación sin peso no es circular por definición, pero su fuerza viene íntegra de (R).

## §5 (e) Controles

- **Retículo de los coprimos con `p`.** Las restricciones son menos, así que hay más estados admisibles y WF(coprimos) es
  más fuerte que WF(ℕ). Si `K^{(p)}_T ≠ ∅` para todo `T`, (E) daría un `w` con `w_{p^k} = 0`, y (R) forzaría `w = v`, con
  `v_p ≠ 0`: contradicción. Luego (R)+(E) **predicen** que WF(coprimos) falla en algún `T`. Esto es consistente con los
  borrados certificados (índice l.558). El paso (R′) ya lo ve: el símbolo `2Re Σ_k log p·p^{−k(½+iτ)}` tiene media cero y no es
  `≤ 0` fuera de `Z`. Buen control, pero el `T` concreto queda sin cuantificar.
- **Sistemas tipo Beurling.** No hay `Φ_M` entera con el mismo factor arquimediano y ecuación funcional, así que no existe
  familia casi radical. La cadena se corta en el primer paso de (R). (E) y (WF) siguen valiendo y sólo dan que algún `w` está
  en la intersección, sin identificarlo. Por tanto un sistema donde WF valga y `a^{v_N}` falle **no** falsifica la cadena.
  Es coherente: todo el peso aritmético está en (R).

## Conclusión

(E) y la dualidad, en su forma clausurada, son correctas, pero no transportan signo. El contenido está en (R), y (R) tiene un
hueco concreto: los tests casi radicales son ciegos sobre `Z` y no excluyen `w = (1−s)v`. Para cerrarlo hacen falta
(i) `inf_T s_T = 0` en las direcciones donde Arch es negativa y (ii) una clasificación de los pares cristalinos `(D, Z)`.
Ambos son OPEN y ninguno es más débil que lo que se busca en P_T.
Etiquetas: (R′) ARGUED; cota de caja PROVED (sketch); (E) PROVED; (WF) clausurada PROVED; (R) OPEN.
