# Anexo — Lectura en primaria de la cadena de Sonin semilocal

Nota de lectura. No se construye nada. Las únicas verificaciones propias son cortas y llevan la etiqueta ARGUED.
Rutas relativas a `03-research/`.

## 0. Filtro de cuatro puntos (anexo de lectura)

1. **Antecedente más cercano.** La identidad de traza de Sonin `E_S = Son + R_{S,T}` (R183_018 §3, Prop 3.1), su forma
   semilocal `(84)_S` (R186_015) y la descomposición de `W_T` de PROOF_L_SHARP_D_001 Thm 2.1. Todas se leyeron en primaria.
2. **Objeto nuevo.** Ninguno. Este anexo sólo informa.
3. **Dificultad evitada.** No corresponde.
4. **Conexión con el signo global.** En §6 se evalúa si queda algún enunciado sobre los restos que no esté en una clase
   cerrada. La respuesta es negativa.

## 1. (Q1) Identidades de tipo Sonin/concentración que hay en el corpus

**(I-1) Traza de Sonin arquimediana, nivel (1,1).** R183_018 §1 y §3, Prop 3.1, `PROVED` a partir de CC Thm 4.7 `CITED`.
- **Transformada:** `F = F_{e_R}`, Fourier par en `L²(R)^ev`.
- **Restricción:** `Π = proyección sobre S(1,1) = {ξ = 0 en |q| ≤ 1, Fξ = 0 en |p| ≤ 1}`, la parte de autovalor 1 de `P P̂ P`
  (CC (72), (81)).
- **Forma positiva:** `Son(h) = Tr(ϑ(g)Πϑ(g)*) = ‖Πϑ(g)*‖²_HS ≥ 0`. Es exactamente de la forma `‖Q U F‖²`.
- **Portador y conjunto S:** `h ∈ C_c^∞(I_T)`, sin condición de momentos, para todo `T` y todo `S ⊇ {∞} ∪ {p < e^{2T}}`.
- **Identidad:** `E_S(h) = Son(h) + R_{S,T}(h)`, con
  `R_{S,T}(h) = −∫_{−2T}^{2T} c_h(x) ε(e^{|x|}) dx − Σ_{p<e^{2T}} 2 log p Σ_{k log p<2T} p^{−k/2} Re c_h(k log p)`.

**(I-2) Forma con la torcedura separada.** PROOF_L_SHARP_D_001 Thm 2.1, `PROVED` dado CC Thm 4.7.
- **Portador:** núcleo `C²_c(I)` real, extendido a `E(core)` por densidad.
- **Identidad:** `W_T(g) = Son_{1,1}(g) + 2ε′(1⁺)𝔅(g) − ⟨g,K_s g⟩ − ⟨g,C_p g⟩ + 2Re(A(g)B̄(g))`.
- **Forma matricial (Cor 2.2):** en la base de prolatos, `𝔐 = 𝔖 + 2ε′𝔅 − 𝔎 − ℭ + 𝔓`.

**(I-3) Cadena semilocal para S finito cualquiera.** R186_009 (S = {∞,2}) y R186_015 (S general), tabla de estado.
- **Transformada:** `F_S = E_S F_∞ E_S^{−1} = I·m_∞(D)·U_S(D)`, con `U_S = e^{iφ_S(D)}` y
  `φ_S′ = −Σ_p Σ_k v_{p^k} cos(kt log p)`.
  - Es unitaria, involutiva y autoadjunta, y cumple `F_S ϑ(ρ) F_S = ϑ(ρ^{−1})` (U_S, L0: `PROVED`).
- **Restricción:** `Π_S = Q₁ ∧ Q₂`, con `Q₁ = 1−P` y `Q₂ = 1 − F_S P F_S`. Es una proyección de Riesz con hueco
  (R186_009 G, D: `PROVED`).
- **Identidad (84)_S:** `Tr ϑ(f)Π_S = W_∞(f) − Σ_{p∈S} comb_p(f) + ∫ f(ρ^{−1}) ε_S(ρ) d*ρ`. Está `PROVED` dado CC Thm 4.7
  (R186_015, filas C′_S y (84)_S). El peine de primos sale exacto y separado:
  `Tr ϑ(h)(P̂^S − P̂_∞) = Σ_p Σ_k (log p) p^{−k/2}(h(p^k) + h(p^{−k}))`.

**(I-4) Diferencia semilocal−arquimediana.** R183_033 §1.1, `PROVED` (029 + 025):
`Son_S − Son_∞ = término primo exacto + ∫ c_h ε′_p + (1/2π)∫ |φ|² r_p`.

**(I-5) Identidad de concentración en el anillo de Sonin.** PROOF_L_SHARP_U_001.
- U.2.1, `PROVED` en L²: `ℓ(g) = λ‖Πρ‖²` y el dato vive en `𝒱_μ = 𝒮(1,1)⁺ ⊖ 𝒮(1,μ)⁺`.
- U.3.1, `CONDITIONAL` (cerrabilidad C1 y lema radical C2): `𝔔 = 𝒲_refl[σ_+] − 𝒲_refl[σ_−] + E`.
- U.1.3: el sector menos aporta −SOS forzado. Etiqueta REF-D.

**Términos de resto.** Las fuentes están en (I-2) y en R183_018 §4–5.

| término | origen | signo | tamaño cuando T crece |
|---|---|---|---|
| `2ε′(1⁺)𝔅(g)` | **borde de la ventana de Sonin**: la cáscara `λ/ρ < |x| < λ` da la torcedura en ρ = 1 (D_001 Prop 2.3) | `≥ 0` en `∫g = 0` (𝔅 = ‖G‖²) | a nivel 1, `ε′(1⁺) ≈ 22.9965` es constante (CC Lemma 5.4 `CITED`); a nivel `λ = e^T`, `2ε′_λ(1⁺) ≍ μ^{O(1)} e^{4πμ}` (D_001 Prop 2.3 `PROVED`); los pesos de fuga entran invertidos (`D^{−1}`) |
| `−⟨g,K_s g⟩` | parte lisa de ε: términos cruzados prolato/fuga `λ_n(1−λ_n²)^{−1/2}⟨ξ_n|ϑζ_n⟩` | **sin signo**; es Hilbert–Schmidt y compacto | en el registro, ε sólo hasta ρ ≤ 3 (R186_022); el número de autovalores sobre el piso de Sonin crece con T (R186_013 NUMÉRICO/ARGUED; R183_026 #{λ(K_{I_T}) > 1} ≈ 4T−2 NUMÉRICO) |
| `−⟨g,C_p g⟩` | aritmético: los primos con `k log p < 2T` | **indefinido**: suma medible de Toeplitz `T_n(σ_p)` de traza cero, con espectro ± de multiplicidad infinita (R183_018 Prop 4.1 `PROVED`) | aparece en cuanto `T > ½log 2`, y con él `n₋(R_{S,T}) = ∞` (R183_018 Thm 5.1 `PROVED`) |
| `𝔓 = 2Re(AB̄)` | **calibre** (momentos de Tate, polo) | indefinido, de rango 2 | se anula en `P_T` |
| `ε_S − ε_∞ = κ_S` | **S finito**: corrección de ángulo/compresión semilocal | sin signo | `∈ L^p_loc` y `R′_S` es HS para S fijo (`PROVED`); singularidades `log^r` en todas las S-unidades. Para S = S(T): peine en todos los enteros, singularidades de tipo `1/|ρ−n|`, **no uniforme en T** (R186_015 fila S(T), ARGUED) |
| corte arquimediano | `ε` truncado a `|a| < 2T`; el símbolo `ρ_T = m + ε̂_T` | **no es ≥ 0** (R186_022, NUMÉRICO; `ρ_T(0) = −2.36` en ½log3) | — |

## 2. (Q2) Qué significa «PROVED para todo S finito, sin signo»

**Lo que está probado para S finito** (R186_015 tabla, filas U_S hasta M_S):
- `F_S` es unitaria e involutiva.
- `A_S = P F_S P` es compacta, con `‖A_S‖ < 1`; no es HS y está en `S_p` para todo `p > 2`.
- Se cumplen TC_S y C′_S (peine exacto).
- Se cumple (84)_S.
- `κ_S ∈ L^p_loc` y `R′_S` es HS en `L²(I_T)` para todo T, con S fijo.

Índice 04_PHASES l.123: «PARTIAL (PROVED ∀S; no sign) | remainder inertia in P_T OPEN».

**Por qué no da el signo.** La identidad es `E_S = Son_S − C_{ε_S}`. Que `Son_S ≥ 0` vale por construcción, y vale igual
para toda involución F con `FϑF = ϑ^{−1}`. D_001 Thm 4.1 y Cor 4.2 (`PROVED`) muestran que `Son_c ≥ 0` existe para cΛ con
cualquier c real, para exponentes `c_p` por primo y para primos borrados (`c_p = 0`). La positividad de Sonin existe, por
tanto, para toda la familia de falsificadores. El signo queda entero en `Son_S ≥ C_{ε_S}` sobre `P_T`, que es la inercia
`N_T` del resto: OPEN (R183_028 §3.2; R183_033 §4).

**¿La positividad semilocal está probada, abierta o es falsa para S finito?**
- **S fijo que no contiene todos los `p < e^{2T}`:** falla.
  - S = {∞}: una dirección negativa desde T ≈ 0.596 y dos desde 0.80 (R183_026 §3, R183_033 §2; NUMÉRICO no certificado).
  - S = {∞,2}: se rompe en T ≈ 0.567 (R183_033 §2, NUMÉRICO).
- **S = S(T):** coincide con a_T.
  - Para `T ≤ ½log5`, `PROVED` dado Paper 47 (R183_030 Prop 3.1; `CITED`), con un hueco ≥ 6.25e-13‖ξ‖².
  - Más allá, OPEN.
  - Hasta 0.80, `n₋ = 0` es NUMÉRICO, con un hueco que cae superexponencialmente.

**El paso S → todos los primos.** Nunca hace falta dentro de una ventana: por soporte sólo actúan los `n < e^{2T}`
(R183_018 Prop 3.1; R183_001 Thm 1). Lo que falla es la **uniformidad en T** de la familia S(T). Las constantes contienen
`∏_{p∈S}(1−p^{−1/2})^{−1}` y `Ψ_S`, que divergen. El límite predicho es un peine de enteros con singularidades `1/|ρ−n|`
(R186_015 Veredicto, ARGUED).

## 3. (Q3) Coincidencia en la ventana finita

**Sí, está enunciada y se usa.**
- R183_030 §1.1: «With S = S(T) one has W_S = W_T, Paper 47's Weil form», con `S(T) = {∞} ∪ {p^k < e^{2T}}`. Etiqueta
  PROVED, bookkeeping.
- R183_018 Prop 3.1 exige `S ⊇ {∞} ∪ {p < e^{2T}}` precisamente por eso.
- R183_018 §6, cautela (ii), y R162_2602 Thm 4(b): toda prueba debe usar que S contiene **todos** los `p < e^{2T}`.

**En qué difiere el objeto semilocal de a_T en la ventana:**
- (a) **Factores de Euler completos.** `F_S` y `Π_S` usan `∏(1−p^{−s})^{−1}` sin truncar (R186_015 §1). En la forma sólo
  sobreviven los `k log p < 2T`, por soporte. En la parte positiva y en el resto, en cambio, entra la cola completa: `Son_S`
  y `ε_S` por separado **sí** ven las potencias `p^k > e^{2T}`. Sólo su diferencia no las ve.
- (b) **Portador y calibre.**
  - CC trabajan en la variable ξ (`h = (½−∂)ξ`), que impone un solo momento de Tate.
  - `P_T` impone dos: R183_030 §1.1 y §1.2. En `P_T` los términos polares se anulan.
  - D_001 §1: las condiciones de admisibilidad `f(0) = f̂(0) = 0` son las de CC (93) y no las de Sonin.
- (c) **Nivel.** La traza de Sonin está en el nivel `λ = 1`. La identidad completa a nivel `λ = e^T > 1` depende del
  diccionario D3 (R186_017), que es OPEN para `λ > 1` (R186_099; D_001 §5, CONDITIONAL).
- (d) **La parte positiva cambia con T.** `Son_{S(T)}` crece en S con T, así que la familia «finito-S» no es una sola forma
  positiva fija.

## 4. (Q4) Los tres controles frente a cada término

**Lo que dicen los memos.**
- D_001 Thm 4.1 y Cor 4.2 (`PROVED`):
  - Para cΛ y para el borrado de un primo, la identidad **no** falla.
  - `Son_c ≥ 0` sigue igual; el peine pasa a ser `c·comb`.
  - El fallo (λ < 0 certificado para c > 1 en T = 1 y en ½log5, CERT_FALSIFIERS_001) vive **dentro de**
    `C_{ε_c} = 2ε′_c(1⁺)𝔅 − K_s^{(c)}`.
- D_001 Prop 3.1: `𝔖, 𝔅, 𝔎, 𝔓` son ciegos al peine y `ℭ` es lineal en él. La barrera (B_001 Lemma 4.1) excluye toda prueba
  del tipo «piezas positivas + cota TV-robusta de `𝔎 + ℭ`».
- U_001 §4:
  - Con cΛ, la fórmula de sectores y el C1 se rompen con un defecto lineal en `(1−c)` (PROVED algebra).
  - Con `a_P` ocurre lo mismo (ARGUED).
  - Con Beurling no hay Poisson ni `𝔉_μ`; U.2 sobrevive.

**Análisis propio (ARGUED), término a término:**

| término | cΛ, c = 2 | borrado de una potencia prima | peso de tipo Beurling |
|---|---|---|---|
| `Son_S` | existe y es ≥ 0 (Cor 4.2, PROVED); **ciego** | existe y es ≥ 0 (`c_p = 0`, PROVED); **ciego** | ARGUED: `F = I m_∞(D) e^{iφ(D)}` con φ impar sigue siendo una involución unitaria con `FϑF = ϑ^{−1}`; la construcción de Halmos aplica; **ciego** |
| `2ε′(1⁺)𝔅` | la torcedura cambia de valor, `ε′_c(1⁺) = Σ χ_n ψ_n(λ)²/D_n` con prolatos de `F_c`; sigue ≥ 0 en ∫g = 0; no cambia de signo | ídem | ídem |
| `K_s`, `κ_S` | cambian de forma no lineal en c, porque `Π_c` no es lineal en c; no tienen signo ni antes ni después; aquí se esconde el fallo | ídem; el borrado elimina las singularidades de `ε_S` en las S-unidades que involucran a p | las singularidades se mueven a las «S-unidades» de Beurling, en general densas y no enteras; no se ve cambio de signo de un término individual |
| `C_p` | se duplica; indefinido antes y después | pierde un bloque Toeplitz; indefinido | indefinido |

**Conclusión ARGUED.** Ningún término individual cambia de signo bajo los controles. Los términos con signo (`Son`, `𝔅`) son
ciegos. Los que ven el control (`K_s`, `κ_S`, `C_p`) no tienen signo. La identidad es válida para los tres controles, así
que no se rompe. Esto contradice la premisa del argumento inverso («U unitaria sólo para los enteros verdaderos»): la U del
corpus, `F_S`, es unitaria para cualquier símbolo impar φ (R186_015 U_S; D_001 Thm 4.1(a)).

## 5. (Q5) Por qué se detuvieron estas fases

- **Traza de Sonin entera (η = 0).** NO-GO `PROVED` (R183_018 Thm 5.1; R183_019 Thm 4.1; R183_020).
  - Clase: «Son entero + resto con un número finito de direcciones negativas».
  - Falsificador explícito: pares `β(t−t_j) + β(t−t_j−log 2)` con `n₋ = ∞`.
- **η uniforme en T, (L-Son).** Falsa, CONDITIONAL sobre una hipótesis espectral externa (R183_027; R183_028 §2).
- **W-Sonin.** Índice 04 l.35; R183_031 Thm 1; R183_033.
  - Clase: parte positiva multiplicadora con resto de inercia acotada para todo T.
  - Resultado: la densidad límite queda soportada en el espectro; converge a la fórmula explícita. NO-GO.
- **W11′.** R184_015 Teorema 2 y Cor 3, `PROVED`.
  - Clase: toda descomposición `W_T = Pos_S + Δ_T` con `‖Δ_T‖ = e^{o(T)}`.
  - Si Δ se define desde la fuente, es ciega al falsificador `M_m`. Si se define desde la forma, es REF-D.
- **Alineación de un solo modo.** FALSIFIED, NUMÉRICO (R186_023 Estado, §2).
  - Clase: modo arquimediano frágil + fases primas.
  - Falsificador: `M(T) = W[h_a]` falla frente a `λ_min` por factores de hasta 10^10 en ½log5, y el rango necesario crece
    con T.
- **ρ*(T).** R186_021, NUMÉRICO: sube por colapso de `Son_S`, no por C.
  - Clase cerrada por Lemma H (iv) (R186_029 §1, `PROVED`): `1 − ρ* ≤ λ_A/λ_min(Son_S|P_T)`, hereda el margen.
  - R186_022: el símbolo truncado no es ≥ 0. NO-GO para argumentos de símbolo puntual.
- **Muros.** Índice 04 l.38–43:
  - **W-lin:** certificados lineales en una base fija, congruencia, Schur, inercia o cotas de norma. Razón: no deciden
    ventana nueva (R186_029–031).
  - **W-det:** todo determinante que decide el signo factoriza `λ_A·R` (R186_034 Thm 3.1).
  - **W-fam:** funcionales de `{λ_A(T′)}`. Falsificador acotado `f_t` (R186_036 Thm 3).
  - **W-pat:** observables de ventana. Falsificador: el modelo de cuarteto `M₁`, que coincide en todos los observables y es
    negativo (fase 187).
  - **W-loc:** criterios locales o de rango finito sobre `σ_T`. Falsificador `σ^{(η)} = min(σ_T, η)` (R186_043/044).
  - **W-mom:** momentos finitos. Margen `≤ k(1−β_max)` (R186_045 Lemma T/T′).
- **Teorema X** (R186_045 §2.2). `PROVED` como reformulación.
  - Como dato desde σ: OPEN.
  - Es ciego a la clase: `M₁` lo cumple bajo su contacto y `f_t` coincide con ζ hasta ½log λ₁.
- **Fase 199.**
  - D_001: NO-GO como ruta de cita.
    - Prop 3.1: las piezas positivas son ciegas al peine. Falsificador `ν′ = ν_Λ + mδ_{u_0}`.
    - Cor 4.2: el falsificador cΛ vive en `ε_c`.
  - U_001: REF-D. El sector menos es −SOS forzado.
- **Fase 158** (R158_005 §1, §3). Toda estructura de positividad examinada en el espacio de clases de adèles es una
  reformulación, una compresión, ciega a ceros, falsa o vacía. Etiqueta RESTATEMENT. MW-5 queda sin objeto.

## 6. (Q6) Evaluación propia (separada de lo anterior)

No encuentro ningún enunciado preciso sobre los restos que nadie haya intentado y que no caiga en una clase registrada.

- Todo enunciado de signo sobre `C_{ε_S}` frente a `Son_S` en `P_T` es `N_T`.
  - Como cota de norma o de inercia acotada, cae en W11′ o en W-Sonin.
  - Como desigualdad exacta, es REF-D.
- La «ceguera» de `Son` a los controles (D_001 Cor 4.2) impide que la parte positiva de Sonin lleve el signo, sea cual sea
  el S.
- Lo único abierto y no cerrado es sin signo:
  - la acotación (B) de `ε_S` (R186_009);
  - la no-uniformidad de `κ_{S(T)}` (R186_015 fila S(T), ARGUED);
  - el diccionario D3 para `λ > 1`.

  Probarlos daría identidades, no positividad. El argumento de ingeniería inversa sobre «U unitaria sólo para los enteros
  verdaderos» no se sostiene para la U del corpus. Un objeto con esa propiedad tendría que ser distinto de `F_S`. Para él no
  hay antecedente escrito en estas fases, y tampoco lo propongo aquí.
