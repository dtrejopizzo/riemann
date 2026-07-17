# Doc 139 — Auditoría adversarial de la equivalencia logística: RH ⟺ lim σ_loc^(k) = 0

**Programa:** Hipótesis de Riemann — Phase 46, "auditoría y ataques"
**Fecha:** junio 2026
**Mandato:** destruir la reparación del Teorema-puente 2.13(b). Objeto auditado: Doc 136
(Corolario 5.6 y toda su cadena: Defs. 3.1–3.2, Props. 3.3, 3.5, Teoremas 4.1–4.4, 5.4,
Prop. 5.5) y su versión publicada en P47 (`thm:logistic`, `def:cell`, `def:loc-scheme`,
`prop:loc-welldef`, `prop:loc-logistic`, `thm:weyl-stab`–`thm:mesh`, `lem:tail`,
`lem:vandermonde`, `thm:realiz`, `prop:RHbranch`, `thm:main`, `rem:key`).
**Insumo de contexto:** Doc 133 (ley logística, Thm. 2.10; Defs. 2.1–2.4), ERRATA.md
(auditoría Phase 38). Citas solo hacia atrás. Nada se fabrica; cada afirmación de error
viene con el cálculo o el contraejemplo de configuración.

---

## 0. Veredicto en una línea por rama

| Componente | Veredicto |
|---|---|
| **Ley logística** x_{k+1} = 2x_k(1−x_k) (núcleo algebraico, D133 Thm. 2.10 / P47 `thm:logistic`) | **SOBREVIVE** — exacta, re-derivada abajo sin hipótesis ocultas. Su *transplante* a σ_loc (Prop. 3.5 "verbatim" / `prop:loc-logistic`) contiene un error de normalización (radical) reparable: la fórmula cerrada es falsa tal como está escrita, la dicotomía 0 vs ½ sobrevive. |
| **Rama RH ⟹ lim σ_loc^(k) = 0** (D136 Prop. 5.5 / P47 `prop:RHbranch`) | **SOBREVIVE** — insumos verificados contra ERRATA, sin circularidad. |
| **Rama ¬RH ⟹ lim σ_loc^(k) = ½** (D136 Thm. 5.4 / P47 `thm:realiz`) | **MUERE como "teorema con prueba completa"** — dos huecos en la prueba: (GAP-A) el Paso 3 afirma θ(M,w) → 0 con constantes C_M, e^{a₀(M,w)}, b₀(M) que dependen de M y cuya uniformidad no solo no está probada sino que es **falsa** para toda familia de bumps de soporte fijo (Lema 139.1 abajo); (GAP-B) el Paso 1 no aniquila los **pares resonantes** con ambos miembros en S y σ ∈ {σ₀, σ₀′} distintos de la órbita objetivo, que existen para configuraciones ¬RH legítimas y aportan términos de signo no controlado. El **enunciado** no queda refutado: GAP-B es reparable con Vandermonde en la coordenada τ, y GAP-A es probablemente reparable importando el mecanismo clásico de dominancia exponencial del criterio de Weil (esbozo en §3.5), pero el estatus honesto hoy es **CONDICIONAL/ABIERTO**, no teorema. |

**Consecuencia para la equivalencia (D136 Cor. 5.6 / P47 `thm:main`):** queda con una rama
teorema y una rama con gap — exactamente el estatus asimétrico que tenía el Doc 133 antes
de la reparación. La reparación corrigió de verdad el error de normalización del 2.13(b)
(eso se confirma: la arquitectura localizada es sólida y la negatividad NO escapa a celdas
de dimensión creciente), pero introdujo un segundo error en otra coordenada — la
**uniformidad en M de las constantes de Paley–Wiener** — tal como el encargo anticipó que
suele ocurrir en las reparaciones.

---

## 1. Re-derivación de la ley logística (protocolo 1)

### 1.1. La identidad tensorial, desde cero

Sea Q̄ hermitiana **no degenerada** sobre V, dim V = n̄ < ∞, signatura (p, q). Por la ley
de inercia de Sylvester existe base Q̄-ortogonal {e_i} con Q̄(e_i, e_i) = ε_i ∈ {±1},
p positivos y q negativos. Para Q̄₁ ⊗ Q̄₂ sobre V₁ ⊗ V₂, la base {e_i ⊗ f_j} es
ortogonal con signos ε_i^{(1)}ε_j^{(2)}; ninguna entrada diagonal es 0 (no hay vectores
isótropos en la base) y la forma producto es no degenerada (el determinante de Gram
multiplica: det(G₁⊗G₂) = (det G₁)^{n₂}(det G₂)^{n₁} ≠ 0). Por Sylvester,
neg.ind = número de signos −1 = p₁q₂ + q₁p₂. Aplicado a la duplicación
Q̄^{⊗2^{k+1}} = Q̄^{⊗2^k} ⊗ Q̄^{⊗2^k}, con (P_k, K_k):

$$K_{k+1} = 2P_kK_k, \qquad P_{k+1} = P_k^2 + K_k^2,$$

y dividiendo por n̄^{2^{k+1}}: x_{k+1} = 2x_k(1−x_k); 1−2x_{k+1} = (1−2x_k)², de donde
1−2x_k = (1−2x_0)^{2^k}. **Verificado: la recurrencia es una identidad exacta de
racionales.**

### 1.2. ¿Hay una hipótesis de no-interacción entre copias asumida sin prueba?

**No.** El producto tensorial de formas se define ortogonalmente por construcción; la
"no-interacción" no es una hipótesis sobre las copias sino el contenido de la definición
de Q⊗Q. Las dos hipótesis reales, ambas satisfechas y declaradas, son:

1. **No degeneración** (sin ella Sylvester no da neg.ind por conteo de signos): D136 la
   asegura pasando al cociente por el radical (Def. 3.2, "forma reducida no degenerada
   Q̄_N"). Correcto en sí — pero ver §2.3: el cociente cambia el denominador y rompe la
   fórmula de la Prop. 3.5.
2. **Dimensión finita por coordenada N**: satisfecha (celdas acotadas).

El paso a partes estándar es legítimo: st es homomorfismo de anillos sobre los limitados,
la identidad polinomial se usa un número finito (estándar) de veces por k, y cada
x_k(N) ∈ [0,1]. La errata conocida del Doc 106 (Cor. 3.2 requiere p₁,p₂ ≥ 1,
ERRATA.md §"índice tensorial") **no afecta**: la identidad (A) que se usa aquí está
declarada INTACTA en el ERRATA y además P47 la re-demuestra autocontenida
(`lem:whitney`).

**Advertencia de alcance (no error):** la torre es un amplificador *formal* — Q̄^{⊗2^k}
no es la forma de Weil de ningún espacio de tests duplicado. Ni D136 ni P47 afirman lo
contrario; el contenido aritmético entra solo por x_0(N). Correcto como está.

### 1.3. La dicotomía {0, ½}

Para σ⁰ ∈ (0,1): |1−2σ⁰| < 1 y la forma cerrada da ½. Para σ⁰ ∈ {0,1}: 0. El caso
borde σ⁰ = 1 queda excluido en la versión localizada por el relleno (x_0 ≤ ½). Todo
correcto **siempre que la base de la torre sea la cantidad correcta** — ver §2.3.

**Veredicto protocolo 1: la ley logística SOBREVIVE como álgebra exacta.**

---

## 2. Auditoría de σ_loc: buena definición, monotonía, canonicidad (protocolo 2)

### 2.1. Buena definición y monotonía de la grilla — VERIFICADAS

- **Inclusión 𝒢_N ⊆ 𝒢_{N+1}:** un perfil p = (D,w,M,b,c,c′) ∈ 𝒢_N tiene D,M ≤ N ≤ N+1;
  w,b ∈ {2^{−j}: j ≤ N} ⊆ {2^{−j}: j ≤ N+1}; centros en (bℤ)²∩[−2^N,2^N]² ⊆
  (bℤ)²∩[−2^{N+1},2^{N+1}]². Todas las restricciones se relajan: **inclusión verificada**.
  Como Q̃_p y dim Ṽ_p dependen solo de p (no de N), x_0(N) = max sobre familia creciente
  de conjuntos finitos es **no decreciente**. ✔
- **El orden parcial correcto:** la monotonía usada es de crecimiento de la grilla (max
  sobre más celdas), no interlacing de Cauchy entre subespacios. No hay dirección de
  desigualdad que verificar contra Cauchy; donde un interlacing sí se usa (Teorema 4.2 =
  estabilidad bajo rango), la prueba de tres líneas con N ∩ ker E es correcta y en la
  dirección correcta (verificada línea por línea). ✔
- **Canonicidad en 𝒰:** sucesión monótona acotada converge; st de convergente = límite
  para todo 𝒰. La Obs. 5.7 es correcta para σ_loc. ✔
- **Cota x_0(N) ≤ ½:** neg.ind(Q̃_p) ≤ dim V_p ≤ (D+1)² y dim Ṽ_p = dim V_p + (D+1)²,
  luego el cociente ≤ dim V_p/(dim V_p + (D+1)²) ≤ ½. ✔ (Vale incluso si los
  h_{g_a,φ_b} son linealmente dependientes y dim V_p < (D+1)².)

Dos observaciones de honestidad, no fatales:

- **(O-1) Canonicidad de diseño:** σ_loc es 𝒰-canónica pero NO diseño-canónica: depende
  de la familia de bumps B^{(M)}_w "elegida de una vez" y de la geometría de la grilla.
  La equivalencia del Cor. 5.6 vale para *cada* diseño admisible, lo cual basta; pero el
  paper no debe sugerir que σ_loc es un invariante de ζ — es un invariante del par
  (ζ, diseño).
- **(O-2) "neg.ind se computa exactamente":** las entradas del Gram son números reales
  computables (series sobre primos), no racionales; Lagrange–Sylvester es exacto solo
  sobre aritmética exacta. Lo verdadero y suficiente: "neg.ind(Q̃_p) ≥ 1" es
  **semidecidible** por aritmética de intervalos (un autovalor estrictamente negativo se
  certifica con precisión finita), que es exactamente lo que la lectura de §6.2 usa. La
  frase "se computa exactamente" (Prop. 3.3(a) / `prop:loc-welldef`(a)) es una
  sobreafirmación de redacción.

### 2.2. ⚠ E-139.1: la doble definición incompatible de x_0(N) (el bug del radical)

La Def. 3.2 de D136 (y P47 `def:loc-scheme`) define x_0(N) **dos veces, de forma
incompatible**:

1. En el display: x_0(N) := max_p neg.ind(Q̃_p)/**dim Ṽ_p**.
2. En la torre: "x_k(N) := neg.ind(Q̄_N^{⊗2^k})/**n̄_N**^{2^k}", que en k = 0 es
   neg.ind(Q̄_N)/n̄_N con n̄_N = dim Ṽ_{p*} − dim rad(Q̃_{p*}).

Como rad(Q̃_p) = rad(Q₂|_{V_p}) ⊕ 0 (el relleno Id es no degenerado y ortogonal al
bloque), se tiene n̄_N = dim V_{p*} − r_N + (D+1)² con r_N := dim rad ∈ [0, dim V_{p*}].
Si r_N > 0 — y nada lo excluye: bajo RH el Gram comprimido puede ser degenerado, y bajo
¬RH también — las dos definiciones difieren. Consecuencias exactas:

- **La fórmula de la Prop. 3.5 / `prop:loc-logistic` es FALSA tal como está escrita:**
  σ_loc^(k) = ½(1 − (1−2σ_loc)^{2^k}) requiere que la base de la torre sea σ_loc, y la
  base real es σ_base := st([neg.ind/n̄_N]), que puede diferir de σ_loc.
- **La 𝒰-independencia de σ_loc^(k) para k ≥ 1 queda sin prueba:** la sucesión de la
  torre no es monótona en N (el argumento de la Prop. 3.3(c) no la cubre), de modo que
  los valores intermedios σ_loc^(k) pueden depender de 𝒰.

**Por qué la dicotomía sobrevive (reparación que esta auditoría aporta, con prueba):**
el cociente de denominadores está acotado: dim Ṽ_p / n̄_N ∈ [1, 2] (porque
n̄_N ≥ (D+1)² = ½ dim Ṽ_p). Como st es multiplicativa sobre limitados,

$$\sigma_{loc} \;\le\; \sigma_{base} \;\le\; 2\,\sigma_{loc},$$

para todo 𝒰. Además x_base(N) = (dim V−r)/((dim V−r)+(D+1)²)-acotado ≤ ½ < 1, así que
σ_base ∈ [0, ½] y el caso σ⁰ = 1 sigue excluido. Entonces: σ_loc = 0 ⟺ σ_base = 0 ⟹
torre ≡ 0; y σ_loc > 0 ⟹ σ_base ∈ (0, ½] ⟹ torre → ½, **para todo 𝒰**. La dicotomía
final lim_k σ_loc^(k) ∈ {0, ½} con 0 ⟺ σ_loc = 0 es correcta; lo falso es la fórmula
cerrada *en términos de σ_loc* y la canonicidad de los pisos intermedios.

**Enunciado reparado de la Prop. 3.5:** "Para todo 𝒰 y todo k estándar,
σ_loc^(k) = ½(1 − (1−2σ_base^𝒰)^{2^k}) con σ_base^𝒰 ∈ [σ_loc, 2σ_loc] ∩ [0,½]; en
particular lim_k σ_loc^(k) = 0 si σ_loc = 0 y = ½ si σ_loc > 0, independientemente
de 𝒰." (Alternativa de diseño: definir x_0(N) directamente como neg.ind/n̄ de la celda
ganadora, restaurando la fórmula literal; entonces hay que re-verificar la monotonía en
N, que ya no es gratuita porque el maximizador de neg.ind/dim Ṽ no es el de
neg.ind/n̄.)

**Veredicto protocolo 2: σ_loc bien definida y 𝒰-canónica; la "ley logística verbatim"
contiene un error real (E-139.1) reparable sin pérdida de la dicotomía.**

---

## 3. La rama RH (protocolo 3) — SOBREVIVE

La cadena completa de la Prop. 5.5 / `prop:RHbranch`:

1. **Bajo RH, el lado espectral (1.1) es diagonal:** todo par (ρ₁,ρ₂) con ambos ceros
   on-line es ι-fijo (ι(ρ) = 1−ρ̄ = ρ si Re ρ = ½), luego Q₂(h,h) = Σ|ĥ(P)|² ≥ 0 sobre
   el span. Insumos: la representación espectral con convergencia absoluta
   [D107 Lemas 2.2(b), 5.2(b)] y la simetría ι del multiconjunto de ceros (ecuación
   funcional, incondicional). Citado vía D108 Prop. 2.2 — que es consecuencia inmediata
   del lado espectral de D107, no un insumo adicional. *Nota de higiene:* el resumen de
   D136 dice "insumos D107"; la cita literal de la rama RH es D108 Prop. 2.2. Inocuo,
   pero conviene unificar.
2. **Las celdas viven en el span:** B_w·(monomios) ∈ clase por cerradura bajo x∂ₓ
   [D107]. ✔
3. **Compresión y relleno:** toda compresión de una forma ≥ 0 es ≥ 0; ⊕ Id es ≥ 0;
   neg.ind = 0 en toda celda; x_0(N) ≡ 0; σ_loc = 0; la torre (con o sin el bug
   E-139.1) es idénticamente 0. ✔

**Cruce con ERRATA.md (Phase 38):** los objetos refutados son W_λ ≥ 0 (Doc 63 §7.1),
Doc 76, Doc 103 Thms 2.2/3.1, P39 dirección ⟸, P41 Thm 3.2, P43 ledger L2, Doc 106
Cor. 3.2. **Ninguno** aparece en la cadena de la rama RH: D107 y D108 Prop. 2.2 no están
tocados por el ERRATA; la identidad tensorial usada está declarada intacta y además
re-probada en P47. **Sin circularidad:** RH se usa una sola vez (diagonalidad), no se usa
ninguna cota uniforme RH-equivalente.

**Veredicto protocolo 3: rama RH SOBREVIVE sin reservas.**

---

## 4. El ataque al paso reparado: Teorema 5.4 / `thm:realiz` (protocolo 4)

### 4.1. Lo que la reparación SÍ logró (y esta auditoría confirma)

Antes de los hallazgos, lo justo: el ataque principal sugerido por el encargo — "¿la
negatividad se escapa a celdas de dimensión creciente, repitiendo el error del 2.13(b) en
otra coordenada?" — **falla contra la arquitectura**. La configuración local del defecto
mínimo (S, Z_σ, q, D₀ = q², μ₀, L_{p*}) está fijada por ζ, no por N: son constantes
estándar. La celda testigo tiene perfil fijo y entra en 𝒢_N para todo N ≥ N₀; la
dimensión por celda no crece nunca. La dilución densitaria del Teorema 2.5 no se aplica
(su hipótesis n_N → ∞ por celda falla adrede). La llave conceptual de la Obs. 5.1 — la
test-accesibilidad restringe la *especificación* del espacio, no al *vector testigo* — es
correcta y es matemática de verdad: neg.ind del Gram comprimido es una propiedad del
Gram, y el testigo es un objeto de la demostración. El paquete de perturbación
(Teoremas 4.1–4.3) está verificado línea por línea y es sólido (con un desliz de
constante en 4.4, E-139.5 abajo). **El error del 2.13(b) no se repite en la coordenada
dimensional.** Se repite en otra parte.

### 4.2. GAP-A (fatal para el estatus de "prueba completa"): el presupuesto de constantes del Paso 3

El Paso 3 necesita |(c)| = |cola en Ω₁| ≤ m₀²/4, y lo obtiene así: "el Lema 5.2 con
r = 1 […] da |(c)| ≤ C₃(perfil, C₁, C₂)·θ(M,w), donde θ(M,w) → 0 cuando M → ∞ con w
fijo (la cota del Lema 5.2 decae en M−D−4)". Esto es **lógicamente inválido**: "perfil"
incluye a M, de modo que C₃ = C₃(M); el límite M → ∞ con C₃ tratado como constante no
está justificado. Lo que la cota del Lema 5.2 realmente da en r = 1 es

$$|(c)| \;\le\; \underbrace{C_1^2C_2^2\,C_M^4\,e^{4a_0(M,w)\cdot\beta}\,b_0(M)^{-\text{(pot.)}}}_{\text{crece con } M}\cdot\;C^*(M{-}D)\,(\log(2{+}|\gamma_0|))^2\cdot\;2^{-(M-D-4)},$$

(β ≤ 1 el alcance en Re dentro de la franja; C₁ = constante de Vandermonde, que depende
de b₀(M) = min|B^{(M)}(z_i − ic*)|, también M-dependiente). La pregunta decisiva:
¿puede el producto tender a 0? La respuesta, en forma cerrada:

**Lema 139.1 (rigidez de Paley–Wiener; la afirmación θ → 0 es falsa para soporte
fijo).** *Sea B la transformada de un g ∈ C_c^∞ no nulo con soporte logarítmico
⊆ [−a₀, a₀] (a₀ fijo), y sean C_M las constantes óptimas en
|B(t)| ≤ C_M(1+|t|/w)^{−M} (t ∈ ℝ). Entonces para todo A > 1 existe M_A tal que
C_M > A^M para todo M ≥ M_A. En consecuencia C_M^4·2^{−M} → ∞.*

*Demostración.* Si C_M ≤ A^M para infinitos M, entonces para |t| > Aw se tendría
|B(t)| ≤ (Aw/|t|)^M → 0 a lo largo de esos M, luego B(t) = 0 para todo |t| > Aw. Pero B
es entera (Paley–Wiener, soporte compacto) y no idénticamente nula: sus ceros reales son
discretos — contradicción. ∎

Por tanto, **con cualquier bump fijo, la cota del Paso 3 diverge en M**. ¿Y con una
familia B^{(M)} (un bump distinto por M, soporte a₀(M) creciente)? El balance tampoco se
cierra con las construcciones estándar. Con potencias de sinc (B = (sinc(a₀t/M))^M, tipo
a₀, C_M = (M/(a₀w))^M) el factor por par en r = 1 es del orden

$$C_M^2\,e^{2a_0}\,(1+1/w)^{-2M} \;\asymp\; \Big(\frac{M}{a_0}\Big)^{2M} e^{2a_0},$$

cuyo mínimo sobre a₀ (en a₀ = M) vale e^{2M} → ∞. El factor de franja e^{c·a₀} —
inevitable porque los ceros de la cola pueden tener Re hasta los bordes de la franja y
|B(x+it)| ≤ B-en-Re crece como e^{a₀|x−½|} para g ≥ 0 — derrota siempre al decaimiento
polinomial en Im a distancia fija r = 1. Tomar w → 0 no ayuda: el soporte requerido
escala como M/w y e^{M/(2w)} gana a (1/w)^{M}. Ninguna familia con las uniformidades
requeridas se exhibe en el documento, y las naturales no las tienen.

**Alcance preciso del hallazgo:** esto NO refuta el Teorema 5.4 (la cota es superior; la
cola verdadera podría ser pequeña, y el enunciado es probablemente cierto — ver §4.4).
Refuta la *prueba*: el Paso 3, tal como está escrito, no establece |(c)| ≤ m₀²/4, y la
frase final del Lema 5.2 ("En particular Σ_tail(r) → 0 cuando M → ∞ a r fijo") es falsa
en su instanciación porque olvida que C_g = C_g(M). El mismo error está en P47
(`lem:tail` "In particular it →0 as M→∞ with r fixed" y `thm:realiz` Paso 3).

**Diagnóstico estructural:** es el mismo *género* de error que mató a W_λ ≥ 0 y al
2.13(b): una cantidad tratada como constante que en realidad es función del parámetro
que se hace tender a infinito. En el 2.13(b) era n_W (conteo) confundido con dim V_W
(dimensión); aquí es C₃("perfil") tratado como constante mientras el perfil contiene M.

### 4.3. GAP-B (reparable, pero real): los pares resonantes no aniquilados

El Paso 3(b) afirma: "pares con ambos miembros en S, distintos de la órbita objetivo: su
σ ∈ Z_σ, donde ĝ_v = 0: aportan 0". Falso en general, porque Z_σ se definió en el Paso 1
**excluyendo** σ₀ y σ₀′: un par no-objetivo con ambos miembros en S y σ ∈ {σ₀, σ₀′} no
es aniquilado ni por ĝ_v (que vale ±1 ahí) ni está en la cola Ω₁ (puede tener
|Im σ − γ₀| = 0 y |Im τ| arbitrariamente pequeño).

**Configuración que activa el hueco (legítima bajo ¬RH, que es una hipótesis sobre ζ con
configuración arbitraria):** además del cero mínimo ρ⁰ = ½+δ₀+iγ₀, un cero off
ρ₁ = ½+2δ₀+i(γ₀+ε) y un cero on-line ρ₂ = ½+i(γ₀−ε), con ε pequeño. Entonces
σ(ρ₁,ρ₂) = ½+δ₀+iγ₀ = σ₀ exactamente, ambos miembros están en S, el par no es la órbita
objetivo, y su contribución es

$$2\,\mathrm{Re}\big[\hat h(P)\overline{\hat h(\iota P)}\big] = -\tfrac12\,\mathrm{Re}\big[\hat\varphi_v(\delta_0+i\varepsilon)\,\overline{\hat\varphi_v(-\delta_0+i\varepsilon)}\big],$$

de signo y tamaño **no controlados** por la construcción (φ̂_v solo está prescrita en
τ = 0; en τ = δ₀+iε es O(1)). Sumado con multiplicidades adversariales puede superar a
−m₀²/2 y destruir la negatividad del testigo. Nótese que en el caso de defecto puro de
un solo cuádruplo no hay ofensores (verificado: ningún par del cuádruplo más on-line
produce σ ∈ {σ₀, σ₀′} salvo el objetivo), lo que explica que el error no se viera en el
caso juguete — otra vez el patrón "probado en el juguete, citado en general".

**Reparación (rigurosa, esta auditoría la valida):** los ofensores tienen τ ≠ 0 (τ = 0 y
σ = σ₀ fuerzan ρ₁ = ρ₂ = ρ⁰, la órbita objetivo) y forman un conjunto finito
Z_τ ⊂ ℂ∖{0} fijado por la configuración. Basta prescribir en el lado τ, vía el mismo
Lema 5.3 (Vandermonde con bump, ya disponible), φ̂_v = 0 sobre Z_τ y φ̂_v(0) = 1,
subiendo D a max(|Z_σ|+1, |Z_τ|) y D₀ en consecuencia (sigue estándar). Con esto el
Paso 3(b) vuelve a ser exhaustivo: σ ∈ Z_σ muere por ĝ_v, σ ∈ {σ₀,σ₀′} con τ ∈ Z_τ
muere por φ̂_v, y la imagen ι no agrega casos (σ(ιP) = 1−σ̄ intercambia σ₀ ↔ σ₀′, ya
cubiertos). GAP-B queda así reducido a una errata-con-parche; **pero el parche agranda D
y por tanto agrava el presupuesto de GAP-A** (C₁ y el grado del polinomio crecen):
los dos huecos no son independientes y la reparación debe cerrarlos juntos.

### 4.4. ¿Es verdadero el enunciado? La ruta de reparación honesta

El enunciado "¬RH ⟹ existe una celda acotada con neg.ind ≥ 1" es el análogo doblado del
sentido clásico del criterio de Weil ("¬RH ⟹ ∃f ∈ C_c^∞ con Q(f) < 0"), que es teorema
clásico, y cuyo mecanismo de prueba es **distinto** del de D136: no se normaliza el
término principal a tamaño 1 intentando hacer pequeña la cola en términos absolutos, sino
que se deja CRECER el término del cero off como e^{2δ·a₀} con el soporte a₀ → ∞
(eligiendo el cero off de parte real casi-extremal, no el de altura mínima), mientras los
términos on-line crecen polinomialmente: la dominancia es exponencial y las constantes
M-dependientes quedan absorbidas por e^{2δa₀}. Trasladar ese mecanismo a Q₂ con el
control de fase (1,−1) del plano hiperbólico, y verificar que el test resultante entra en
*alguna* celda de la grilla con perfil estándar (el soporte a₀ requerido es finito una
vez fijada la configuración), es el contenido real que falta. Esta auditoría **no** lo
ejecuta (sería fabricar una prueba nueva en un documento de auditoría); lo registra como
**Problema 139.A**: re-probar el Teorema 5.4 con presupuesto de constantes explícito,
por dominancia exponencial o por una familia de bumps con las uniformidades de §4.2
demostradas. Mientras 139.A esté abierto, la rama ¬RH es CONDICIONAL.

### 4.5. Nota sobre el Teorema 4.4 (constante de malla)

Menor pero exacto: con b ≤ μ/(2√2·L), la cota de la prueba da
‖G(p)−G(p*)‖ ≤ L·b√2·2 = 2√2·L·b ≤ μ, **no** ≤ μ/2 como se afirma; y el Teorema 4.1
exige desigualdad estricta < μ. Corrección trivial: b ≤ μ/(4√2·L). No afecta nada más
(E-139.5).

**Veredicto protocolo 4: la rama ¬RH MUERE como teorema (GAP-A + GAP-B); el enunciado
queda abierto-reparable, no refutado; la arquitectura de localización está confirmada.**

---

## 5. Efectividad Π₁ (protocolo 5) — VERIFICADA

- D136 §6.2(5) y P47 §`sec:honest`(a) declaran explícitamente: σ_loc = 0 es Π₁ sobre
  (x_0(N))_N, "exactamente tan inverificable como siempre"; N₀ y D₀ "no son efectivos a
  partir de m̄ o de nada". **Ningún corolario afirma efectividad.** ✔
- La única tensión de redacción: Teorema 4.4 / `thm:mesh` dice "N₀ **computable** desde
  (μ, L, posición)" — computable desde insumos no efectivamente conocibles. Es
  consistente (el estatus declarado del Thm. 5.4 lo aclara), pero la palabra "computable"
  en el enunciado del lema puede inducir a error a un lector del paper; sugerencia:
  "explícito en función de (μ, L, posición)". (E-139.6, cosmética.)
- La semidecidibilidad de ¬RH por Grams ("correr la grilla hasta certificar un autovalor
  negativo") sobrevive con la precisión de O-2 (§2.1): certificación por intervalos, no
  "aritmética exacta". **Importante:** esta semidecidibilidad depende de la rama ¬RH
  (Teorema 5.4) — con GAP-A abierto, "¬RH ⟹ la máquina para" es también condicional.

---

## 6. Erratas y consecuencias para P47

### 6.1. Lista de erratas (para ERRATA.md y para el .tex)

| # | Lugar | Error | Severidad / acción |
|---|---|---|---|
| **E-139.1** | D136 Def. 3.2 + Prop. 3.5; P47 `def:loc-scheme` + `prop:loc-logistic` | x_0(N) definido dos veces de forma incompatible (denominador dim Ṽ_p vs n̄_N tras cociente por el radical); la fórmula cerrada σ_loc^(k) = ½(1−(1−2σ_loc)^{2^k}) es falsa si el Gram ganador es degenerado; la 𝒰-independencia de σ_loc^(k), k ≥ 1, sin prueba | MEDIA. La dicotomía 0 vs ½ sobrevive vía σ_base ∈ [σ_loc, 2σ_loc] ∩ [0,½] (§2.2, prueba aquí). Reescribir Prop. 3.5/`prop:loc-logistic` con el enunciado reparado. |
| **E-139.2** | D136 Thm. 5.4 Paso 3 + Lema 5.2 (frase final); P47 `thm:realiz` Step 3 + `lem:tail` | "θ(M,w) → 0 cuando M → ∞" con C₃ = C₃(M): inválido; **falso** para familias de soporte fijo (Lema 139.1); uniformidad en M de C_M, e^{a₀(M,w)}, b₀(M), C₁(M) nunca establecida | **CRÍTICA**. La rama ¬RH baja de "teorema sobre insumos citados" a CONDICIONAL (Problema 139.A). |
| **E-139.3** | D136 Thm. 5.4 Pasos 1/3(b); P47 `thm:realiz` Steps 1/3(b) | Pares resonantes (ambos en S, σ ∈ {σ₀,σ₀′}, ≠ órbita objetivo) no aniquilados; existen bajo ¬RH general; signo no controlado | ALTA pero reparable: añadir aniquilación Vandermonde en τ sobre Z_τ (§4.3); D y D₀ crecen (estándar); interacciona con E-139.2. |
| **E-139.4** | D136 Prop. 3.3(a); P47 `prop:loc-welldef`(a) | "neg.ind se computa exactamente": las entradas son reales computables, no racionales; lo correcto es semidecidibilidad/certificación por intervalos | BAJA. Reformular. |
| **E-139.5** | D136 Thm. 4.4; P47 `thm:mesh` | 2√2·L·b ≤ μ, no μ/2; Thm. 4.1 pide < μ estricto | TRIVIAL: b ≤ μ/(4√2·L). |
| **E-139.6** | P47 `thm:mesh`, `rem:collapse` | (i) "computable N₀" engañoso (§5); (ii) `rem:collapse` atribuye el colapso global a \cite{P40}: el colapso es Teorema 2.5 de D136 — verificar que P40 realmente lo contenga o corregir la cita | BAJA. Higiene. |

### 6.2. Consecuencias para el texto de P47

1. **Abstract y `thm:main`:** la frase "with *both* branches theorems over cited inputs"
   y "realizability under ¬RH is now a theorem rather than a hypothesis" deben
   retirarse o condicionarse mientras 139.A esté abierto. Redacción honesta: "the RH
   branch is a theorem; the ¬RH branch is proved modulo a quantitative uniformity of
   Paley–Wiener constants in the witness construction (stated as Problem 139.A), which
   replaces the former realizability hypothesis by a strictly narrower, purely analytic
   gap". Lo mismo en §`sec:honest`(c) ítem 4 ("realizability is now a theorem") y en
   `rem:key` (la frase "dissolves it" es correcta para la Hipótesis D *como tal* — el
   régimen T → ∞ sí se disolvió — pero el caveat no desapareció: se transmutó en la
   uniformidad de constantes).
2. **`prop:loc-logistic`:** sustituir por el enunciado reparado de §2.2 (dicotomía con
   σ_base; canonicidad solo del límite).
3. **`lem:tail`:** borrar la frase final "In particular it →0 as M→∞ with r fixed" o
   condicionarla a C_g, C_φ independientes de M (que es exactamente lo que no se tiene).
4. **`thm:mesh`:** corregir la constante (E-139.5) y la palabra "computable" (E-139.6).
5. **Lo que NO cambia:** la sección Weil–Toeplitz/tricotomía (independiente, no
   auditada aquí salvo cruce de citas), `thm:logistic`, `prop:RHbranch`,
   `thm:weyl-stab`, `thm:rank-stab`, `thm:lipschitz`, `lem:vandermonde`, la Prop. 3.3
   (a,b,c) con la reformulación E-139.4, y todo el §2 de D136 (el colapso global y la
   refutación del 2.13(b), que esta auditoría confirma como correctos).

### 6.3. Estado final del criterio logístico

$$\mathrm{RH} \iff \lim_k \sigma_{loc}^{(k)} = 0:\qquad
\text{rama } \Rightarrow \text{ (es decir, RH} \Rightarrow 0\text{): TEOREMA};\qquad
\text{rama } \Leftarrow \text{ (¬RH} \Rightarrow \tfrac12\text{): ABIERTA (139.A)}.$$

La reparación del Doc 136 corrigió el error de normalización del Doc 133 e introdujo una
arquitectura (localización + grilla + monotonía) que esta auditoría confirma sólida; pero
el estatus de "equivalencia con ambas ramas teorema" anunciado en D136 §0.3, §6.1(2),
§7 y en el abstract de P47 **no es sostenible hoy**. La historia del programa se repitió
con precisión: la reparación de un teorema refutado contenía el segundo error, y estaba
donde siempre — en una constante que no era constante.

---

## Referencias

**Internas (backward-only):** Doc 136 (todo); Doc 133 (Defs. 2.1–2.4, Thm. 2.10,
Teorema-puente 2.13, §5.2); Doc 108 (Prop. 2.2); Doc 107 (Lemas 2.2(b), 5.2(b),
Thm. 5.5, Prop. 6.1, cerradura x∂ₓ); Doc 106 (identidad tensorial); P47 (main.tex,
junio 2026); 06-papers/ERRATA.md (Phase 38); P43 (autonomía del valor).

**Literatura:** R. Paley, N. Wiener (transformadas de soporte compacto: una función
entera no nula tiene ceros reales discretos — usado en el Lema 139.1; estándar, cf.
Hörmander I, Thm. 7.3.1); A. Weil, Comm. Sém. Math. Lund (1952) (criterio de
positividad; el sentido ¬RH ⟹ ∃f: Q(f)<0 y su mecanismo de dominancia exponencial,
citado en §4.4 como ruta de reparación, no como resultado usado); F. R. Gantmacher,
Vol. 2, Cap. X (Sylvester/inercia, §1.1); R. Bhatia, GTM 169 (Weyl/Courant–Fischer,
vía D136 §4).

*Fin del Doc 139.*
