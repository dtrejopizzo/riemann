# Ronda 3, opción 3 — el sector de paridad: productos mn mediante la reflexión J

Memo de selección, no de construcción. Notación de `../phase-211-sign-sandbox/STATEMENT_001.md`;
N = e^{2T}; S_aF(t) = F(t − a); JF(t) = F(−t); b_n = Λ(n)n^{−1/2}; X = Σ_{2≤n<N} b_n S_{log n};
Z = Σ_{1≤n<N} n^{−1/2}S_{log n}. Para un multiplicador Y con símbolo α escribo (YF)^ = αF̂. Etiquetas:
PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO.

Resultado adelantado: **el cotejo identifica repetición.** La forma graduada por J y el canal de
productos están escritos en las fases 161 (R161_032, R161_034, R161_035), 170 (R170_854 §6.3) y en
P47 thm:PCfinite; la dicotomía «métrica positiva ⇒ vuelven los cocientes; supertraza ⇒ forma
indefinida» está en R170_854 §6.3. La memo termina en el cotejo salvo por tres lemas cortos PROVED
(§1) que convierten esa dicotomía, para el álgebra generada por multiplicadores y J, en un enunciado
de clase, y por las respuestas a (i)–(v) (§2).

## 0. Cotejo

**Qué se buscó.** Grep en `03-research/` (todas las fases), `04-papers/47*`, `04-papers/48*`,
`05-meta-and-planning/` y los anexos de esta carpeta por: reflexión/reflection, «J S», paridad/parity,
graded/graduad, supertrace/supertraza, Kreĭn/Krein/indefinite metric, product channel/canal de
productos, product–ratio, hiperbola/hyperbola, PCfinite, «two-orientation». Coincidencias abiertas en
primaria: E70_10 (completo), R166_502 §§2, 5 (completos), R161_032 (completo), R161_034 (completo),
R161_035 §§0–1, R170_854 §6.3, R170_870 §§0–2, 106_50 §1, P47 thm:PCfinite (enunciado, prueba y
observación posterior). «Supertrace/indefinite metric» aparece además en las fases 122, 124, 137, 53
(no abiertas; por el título tratan puertos y conmutadores, no la forma Q_ε). No se abrieron
R161_030–031, 033, 036–039, 211/ROUND_005_A, P1_BBSTAR_001 ni R170_871–877 más allá de su
descripción en `REVIEW_002_BC.md` y `RULES_AVOID.md` I7; el cotejo no depende de ellos para el
veredicto, pero tampoco los descarta como antecedentes adicionales. Una búsqueda sin coincidencias
no prueba novedad.

**(1) Antecedente más cercano, leído en primaria.**
- `phase-161-*/R161_034_MELLIN_GRAM_AND_PRODUCT_RATIO_COLLISION.md` §§1–3 (PROVED allí): átomos
  orientados d_k = k^{−1/2}(τ_{log k}𝓕 − Jτ_{log k}), con símbolo q_k(τ) = k^{−s}u_∞(τ) − k^{−(1−s)}
  sobre F̂(−τ); su Gram tiene dos términos de igual orientación en log(k/l) (cocientes) y dos de
  orientación opuesta en log(kl) (productos), ecuación (3.2). Es exactamente «S_{log m} frente a
  J S_{log n}»: la reflexión es la que produce el canal de productos. Diagnóstico de la fuente (§4):
  en el álgebra de multiplicadores de toda la recta no hay identidad coeficiente a coeficiente que
  elimine los cocientes; lo único vivo es la versión comprimida a la ventana (5.2), OPEN allí.
- `phase-161-*/R161_032_PARITY_TURNS_THE_CROSSED_TATE_BLOCK_POSITIVE.md` Teor. 2.1: en un sector de
  paridad ε el término cruzado orientado se convierte en norma positiva multiplicando por ε,
  ε⟨v, G_TCv⟩ = ‖r‖². Es el mecanismo «el signo de paridad orienta el término cruzado», usado sólo
  en el bloque de Tate de rango dos; la identidad de contabilidad (4.2) queda OPEN/terminal.
- `phase-161-*/R161_035_*.md` §§0–1: las dos orientaciones coherentes K_N𝓕 y JK_N, con
  K_N = Σ_{k≤N}(log k)k^{−1/2}τ_{log k} obtenido por Λ∗1 = log en la hipérbola completa.
- `04-papers/47-*/main.tex`, thm:PCfinite: S_NA_M𝓕 = {X,E_N} − L_M^*E_N − JH_{M,N} − H_{M,N}𝓕, con
  H_{M,N} sin coeficiente en k ≤ N porque Σ_{d|k}Λ(d) = log k; observación posterior: «el cuadrado de
  cualquiera de los dos lados es invariante por A_M ↦ −A_M». Es la identidad exacta por ventana sobre
  la hipérbola que el encargo pide en (iii).
- `phase-170-*/R170_854_*.md` §6.3: «con la métrica de Hilbert positiva reaparecen los cuadrados
  hermíticos con su peine de cocientes; con la supertraza los dos cuadrados se cancelan pero la forma
  queda indefinida». Es la pregunta (i), contestada en general.
- `phase-70-*/E70_10_*.md` «What remains possible», opción 1 (graded/supersymmetric cancellation),
  nunca construida; R166_502 §5.2: V*V vive en el álgebra de ℚ₊^×, V² en la de ℕ.
- `phase-106-*/106_50_*.md` §1: separación producto/cociente en la varianza de triángulos.

**(2) Objeto realmente nuevo.** Ninguno. La forma del encargo es

    Q_ε(F) = Σ_{m,n} Λ(m)Λ(n)(mn)^{−1/2}⟨S_{log m}F, J S_{log n}F⟩ = ⟨XF, JXF⟩,

y por el Lema P2 (§1), para JF = εF, Q_ε(F) = ε⟨X²F, F⟩ = ε Σ_{k<N}(Λ∗Λ)(k)k^{−1/2} c_F(−log k): una
forma lineal en c_F (un certificado, en el sentido de `OBJECT_SPEC.md` O2), que es el V² de
E70_12/R166_502 §5.2 llevado al espacio de F por J. La versión «cuadrado hermítico» ‖(A − JY)F‖²
se reduce, en cada sector, a un cuadrado sin J (Lema P1), es decir a la clase (i) de
`REVIEW_002_BC.md`. No se pudo escribir ℋ_T, V_T, ρ_T con mecanismo de signo. Lo que falta escribir
es un operador que **no** esté en el álgebra generada por multiplicadores y J: la compresión a la
ventana (R161_034 (5.2), ya propuesta y OPEN allí), M_t, o funcionales de borde.

**(3) Por qué el cambio evitaría la dificultad del antecedente.** No la evita. La dificultad de
R166_502 §5.2 es que un cuadrado hermítico ve cocientes; J cambia cocientes por productos sólo en el
emparejamiento indefinido ⟨·, J·⟩ (Lema P2), y en el emparejamiento positivo ‖·‖² la paridad
devuelve el problema a un multiplicador (Lema P1). Es la dicotomía de R170_854 §6.3.

**(4) Identidad que conectaría con la positividad global.** Ninguna con signo. Por el Lema P0 basta
cada sector, y por P1–P2 toda identidad a_T(F) = Σ_j‖Y_jF‖² + Σ_i ε_i⟨Y_iF, JY_iF⟩ + ρ(F) con Y en
el álgebra 𝒜 de §1 es, sobre P_T^ε, una partición puntual del símbolo par
s_T = σ_+ + ε σ_K + σ_ρ con σ_+ ≥ 0; el resto ρ es una forma de multiplicador cuya positividad sobre
P_T^ε es un enunciado del mismo tipo que (★) (Lema B-2 de `REVIEW_002_BC.md`, aplicado en el sector).
El signo no puede venir del álgebra 𝒜; sólo de P_T (las condiciones A = B = 0) y del soporte en la
ventana, que 𝒜 no ve.

**(5) Línea que se rompe para cΛ y a_P.** En los Lemas P1–P2 ninguna: valen para todo vector de
pesos (patrón B1 de `RULES_AVOID.md`). La única línea que se rompe es la identidad de la hipérbola
(§2 (iii)): ⟨X F, J Z F⟩ = ε Σ_{k<N}(log k)k^{−1/2}c_F(−log k) es falsa para cΛ (coeficiente
(c − 1)log k en todo k < N con algún divisor primo-potencia) y para a_P (coeficiente
−Σ_{d|k, d = p^j, p<P}Λ(d), no nulo en k = 2 si P > 2). Es el separador lineal Σ_{d|k}a(d) = log k,
el mismo que rompe P47 thm:PCfinite, y no ocurre en un paso de signo.

El cotejo identifica repetición. Lo que sigue sólo delimita.

## 1. Tres lemas cortos

Sea 𝒜 el conjunto de operadores Y = Y_0 + JY_1 sobre L²(ℝ; 𝒦), con 𝒦 un Hilbert auxiliar y Y_0, Y_1
multiplicadores (conmutan con todas las traslaciones) de símbolos α_0, α_1 : ℝ → 𝒦 medibles,
actuando sobre F ∈ L²(ℝ) escalar. Contiene X, Z, las traslaciones, J, la transformada 𝓕 = U_∞J de
R161_034 (1.1) y los átomos d_k; es cerrado por composición con multiplicadores escalares y por
conjugación con J, porque JS_aJ = S_{−a} y, en general, JY_1J es el multiplicador de símbolo
α_1(−τ) ((Jg)^(τ) = ĝ(−τ)).

**Lema P0 (la forma se parte por paridad). PROVED.** P_T es invariante por J y, con
F_± = (F ± JF)/2, a_T(F) = a_T(F_+) + a_T(F_−) y ‖F‖² = ‖F_+‖² + ‖F_−‖². Luego
λ_A(T) = min(λ_A^+(T), λ_A^−(T)), con λ_A^ε el ínfimo sobre P_T^ε = {F ∈ P_T : JF = εF}.

*Demostración.* A(JF) = ∫F(−t)e^{t/2}dt = B(F) y B(JF) = A(F), luego JP_T = P_T e I_T es simétrico.
(F_±)^(−τ) = ±(F_±)^(τ). La parte cruzada de a_T es 2Re(1/2π)∫s_T (F_+)^ conj (F_−)^ dτ; s_T es par
(m(τ) = Re ψ(¼ + iτ/2) − log π es par y cos es par), y el integrando es impar, luego se anula. Lo
mismo con s_T ≡ 1 da la norma. ∎ (Hecho elemental; casi seguramente usado en el corpus; no se
reclama novedad.)

**Lema P1 (en un sector, los cuadrados de 𝒜 son cuadrados de multiplicadores). PROVED.** Si JF = εF
y Y ∈ 𝒜, entonces YF = Y^εF con Y^ε el multiplicador de símbolo α^ε(τ) = α_0(τ) + εα_1(−τ), y

    ‖YF‖² = (1/2π)∫‖α_0(τ) + εα_1(−τ)‖²_𝒦 |F̂(τ)|² dτ.

En particular ‖(A − JY_1)F‖² = ‖(A − εJY_1J)F‖² para A multiplicador escalar; con A = I y
Y_1 = X: ‖(I − JX)F‖² = ‖(I − εX^*)F‖² (pues JXJ = X^* en la recta), y el desarrollo contiene
‖XF‖², el peine de cocientes de E70_10 con coeficientes ≥ 0.

*Demostración.* JY_1F = (JY_1J)(JF) = ε(JY_1J)F, y JY_1J tiene símbolo α_1(−τ). Plancherel. ∎

Consecuencia (PROVED, con el Lema B-2 de `REVIEW_002_BC.md`): si a_T(F) = Σ_j‖Y_jF‖² + ρ(F) en
P_T^ε con Y_j ∈ 𝒜 sin depender de F, entonces ρ(F) = (1/2π)∫(s_T − σ)|F̂|² con
σ(τ) = Σ_j‖α_j^ε(τ)‖² ≥ 0 (sólo cuenta su parte par, porque |F̂|² es par). La graduación por J no
amplía la clase (i). Por el Lema C-1 de la misma revisión, dentro de esa clase hay cuadrados con
cruces −w_pw_q cos τ(ℓ_p + ℓ_q) sin cocientes, a costa de masa; J no añade nada a eso.

**Lema P2 (el emparejamiento J es la convolución y no es un cuadrado). PROVED.** Si JF = εF y
Y ∈ 𝒜 tiene símbolo escalar α^ε (como en P1), entonces

    ⟨YF, JYF⟩ = (ε/2π)∫ α^ε(τ) conj(α^ε(−τ)) |F̂(τ)|² dτ.

Para Y = X: α(τ)conj α(−τ) = Σ_{m,n}b_mb_n (mn)^{−iτ} (con la convención n^{−iτ} de la traslación por
log n), luego

    Q_ε(F) = ⟨XF, JXF⟩ = ε⟨X²F, F⟩ = ε Σ_{k} (Λ∗Λ)(k) k^{−1/2} c_F(−log k),

lineal en c_F, con átomos en log k, k producto de dos potencias de primos. El símbolo
Re[α(τ)conj α(−τ)] = Re D(½ + iτ)² (D = Σ_{n<N}Λ(n)n^{−s}) no tiene signo.

*Demostración.* ⟨YF, JYF⟩ = ⟨YF, (JYJ)JF⟩ = ε⟨Y^εF, (JY^εJ)F⟩ y JY^εJ tiene símbolo α^ε(−τ);
Plancherel. Para X, JXJ = Σ b_nS_{−log n} = X^*, de modo que ⟨XF, X^*F⟩ = ⟨X²F, F⟩, y
X² = Σ_k(b∗b)_kS_{log k} con (b∗b)_k = (Λ∗Λ)(k)k^{−1/2}. La forma escalar sale de
⟨S_aF, S_{−b}F⟩ = c_F(−a − b) (Lema 2 de `ROUND_003_8.md`). ∎

Lectura: en 𝒜, «productos» y «cuadrado» son excluyentes en el sentido siguiente. Los productos mn
con los pesos Λ(m)Λ(n) y sin cocientes aparecen en el emparejamiento ε⟨·, J·⟩, que es una forma de
multiplicador sin signo (P2); en el emparejamiento positivo la paridad lo reduce todo a un
multiplicador con símbolo ≥ 0 (P1), donde los productos sólo aparecen con cocientes positivos y masa
(`REVIEW_002_BC.md` C.3 punto 1) o con canales separados y masa (C-1). Es R170_854 §6.3 escrito como
enunciado para la clase 𝒜 en los sectores de paridad. **NO-GO con clase** (PROVED): ninguna
identidad a_T = Σ‖Y_jF‖² + Σ_i ε_i⟨Y_iF, JY_iF⟩ + ρ con Y_j, Y_i ∈ 𝒜 independientes de F lleva signo
propio: equivale a una partición puntual del símbolo par y deja en ρ un problema de multiplicador del
mismo tipo que (★). Clase declarada: 𝒜 sobre L²(ℝ) (sin compresión a la ventana, sin M_t, sin
funcionales de rango finito, sin dependencia de F).

## 2. Las cinco preguntas

(i) **¿Cuadrado de un operador explícito?** ‖(A − JV)F‖² en el sector ε es ‖(A − εV^*)F‖² (P1): el
cruce reproduce el peine de a_T con signo correcto sólo si se elige el signo de V según ε, y el
diagonal ‖VF‖² es el peine de cocientes de E70_10. Una superálgebra con J como graduación da, con
la supertraza, ε⟨V²F,F⟩ (P2): productos, pero sin signo. Ninguna de las dos contiene el peine de a_T
con un resto manifiestamente ≥ 0.

(ii) **Selberg y la diagonal arquimediana.** Con P2, ε⟨(δX + X²)F, F⟩ = ε Σ_k(μ∗log²)(k)k^{−1/2}c_F(−log k),
δ = ad M_t (`ROUND_003_8.md`). Es lineal en c_F: la relación Λ·log + Λ∗Λ = μ∗log² sólo reescribe un
certificado, y por el Lema A de `ROUND_001_D.md` es consecuencia de los átomos lineales. En la forma
J no hay diagonal que pagar; en la forma positiva la diagonal es ‖XF‖² (cocientes) o, en canales
separados, una masa (r/2)Σw_p² (C-1) que la parte arquimediana tendría que pagar con símbolo, de
nuevo el Lema B-2. Además a_T no contiene átomos en log k con k compuesto de dos primos distintos, de
modo que el término μ∗log² tendría que cancelarse con otro (R170_856 §4: se cancela con la rama de
Poisson, CITED en `REVIEW_002_BC.md` C.4 fila 11).

(iii) **Soporte.** Para F ∈ L²(I_T), c_F(u) = 0 si |u| ≥ 2T, luego Q_ε recorre exactamente la
hipérbola mn < N (PROVED, inmediato). Con Z en lugar de uno de los factores:

    ⟨XF, JZF⟩ = ε Σ_{k<N}(Λ∗1)(k)k^{−1/2}c_F(−log k) = ε Σ_{k<N}(log k)k^{−1/2}c_F(−log k),

exacta para todo F ∈ L²(I_T) de paridad ε (PROVED: P2 con dos símbolos distintos y la identidad de
divisores en cada k < N, todos cuyos divisores son < N). Se rompe para cΛ y a_P en la línea
indicada en el Cotejo (5). Es la identidad de la hipérbola de P47 thm:PCfinite (H_{M,N} sin
coeficiente en k ≤ N) en la forma de R161_035 (orientaciones K_N𝓕 y JK_N), y es lineal en c_F; por
R170_869 (`RULES_AVOID.md` I2) cae en el ideal factorizado y no fija signo.

(iv) **Relación con thm:PCfinite y R161_030–039.** thm:PCfinite es una identidad de operadores con
J cuyos dos lados elevados al cuadrado son ciegos al signo (observación de P47 tras la prueba);
R161_034 calcula el Gram de los átomos orientados y encuentra cocientes y productos a la vez; R161_035
construye el paralelogramo de las dos orientaciones. Q_ε es la parte de productos de ese Gram
restringida a un sector, y P1–P2 explican por qué los cocientes no se pueden quitar dentro de 𝒜. No
se repite ninguna derivación de esas memos; tampoco se aporta nada que las supere. Su residuo vivo es
la compresión R161_034 (5.2), ‖(I − P)Σ_k(log k)d_kPF‖², fuera de 𝒜.

(v) **Paridad de R170_870.** La paridad de 870 es F ↦ −F: una clase lineal (impar en F) no puede
tener signo unilateral salvo si es nula (Lema 2.1 allí). Q_ε es cuadrática en F, luego par en ese
sentido: el lema de 870 no la excluye. La paridad que importa aquí es la de J: el término de Kreĭn
ε⟨X²F,F⟩ cambia de signo con el sector. Por P0 hay que probar (★) en los dos sectores; un término
de Kreĭn con ⟨X²F,F⟩ = Σ(Λ∗Λ)(k)k^{−1/2}Re c_F(log k) sería útil en un sector sólo si en el otro
tuviera el signo opuesto, lo que exige a su vez una información de signo sobre un funcional lineal
de c_F en cada sector: el mismo tipo de enunciado que R161_032 resuelve para el bloque de Tate de
rango dos (por la identidad (2.2) allí, que es una igualdad de Gram) y que para el peine Λ∗Λ no tiene
análogo escrito. ARGUED.

## 3. Qué queda no excluido

- Operadores fuera de 𝒜: compresión a la ventana P = 1_{I_T} (la fuga ‖(I − P)·P F‖² de R161_034 (5.2)
  y del Lema B-1 de `REVIEW_002_BC.md`; palabras QV_aQ de 211/ROUND_005_A), el generador M_t, y
  funcionales de rango finito (A, B, muestreo de Nyquist, borde). Allí el NO-GO de §1 no se aplica.
- Identidades en que el término de Kreĭn y el de Tate de R161_032 aparezcan juntos con el mismo ε
  (la contabilidad (4.2) de R161_032, OPEN/terminal allí).
- Operadores que dependan de F (no lineales en F) o de los valores exactos de Λ de un modo que no sea
  un símbolo fijo.
Ninguno de estos tiene hoy objeto escrito con mecanismo de signo en esta memo.

## Resultado

Sin mecanismo nuevo; repetición de R161_032/034/035, R170_854 §6.3, P47 thm:PCfinite y E70_10 opción 1.
Un NO-GO con clase PROVED (graduación por J en el álgebra 𝒜 de multiplicadores y J, en sectores de
paridad) y un lema de partición por paridad. No lista para construcción.

## Qué se probó

Lema P0 (λ_A = min de los dos sectores de paridad; P_T invariante por J). Lema P1 (en un sector, todo
Y ∈ 𝒜 actúa como un multiplicador de símbolo α_0(τ) + εα_1(−τ); los cuadrados graduados son cuadrados
de la clase (i)). Lema P2 (el emparejamiento ⟨YF, JYF⟩ es el multiplicador ε α(τ)conj α(−τ); para X da
ε⟨X²F,F⟩ = ε Σ(Λ∗Λ)(k)k^{−1/2}c_F(−log k), sin signo). NO-GO con clase: ninguna identidad con
cuadrados y emparejamientos J de operadores de 𝒜 lleva signo propio. Soporte: la suma recorre
exactamente mn < N, y ⟨XF, JZF⟩ es la identidad Λ-libre de la hipérbola (lineal en c_F).

## Qué falló y por qué

J convierte cocientes en productos sólo en el emparejamiento indefinido; en el positivo, la paridad
reduce todo a un multiplicador y vuelven cocientes o masa. La identidad de divisores sobre la
hipérbola es exacta por ventana y se rompe para cΛ y a_P, pero es lineal en c_F (certificado) y es la
de thm:PCfinite. No se pudo escribir ℋ_T, V_T, ρ_T con paso de signo.

## Siguiente paso concreto

No relanzar la graduación por J dentro de 𝒜. Si se sigue en esta zona, el único contenido no
cubierto por §1 es la compresión: escribir para F ∈ P_T^ε la fuga coherente
‖(I − P)(X + εJX)PF‖² (o la de R161_034 (5.2)) y su desarrollo en c_F más términos de borde, y
comprobar, antes de cualquier derivación, si coincide con R161_034 §5 y con el Lema B-1 de
`REVIEW_002_BC.md`; abrir antes R161_030–031, 033, 036–039 y 211/ROUND_005_A Prop. 3.3, que esta
memo no leyó en primaria.
