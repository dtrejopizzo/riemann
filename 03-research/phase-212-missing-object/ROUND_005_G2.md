# Ronda 5, semilla G2 — cierre bajo producto de factores de Euler aplicado a la signatura

Memo generativa. Notación de `../phase-211-sign-sandbox/STATEMENT_001.md`; N = e^{2T};
D_T = P_T ∩ H¹_0(I_T) real; 𝔪_T(F) = (1/2π)∫ m|F̂|²; Π_{T,p}(F) = −Σ_{k≥1} v_{p^k} Re c_F(k log p);
a_T = 𝔪_T + Σ_p Π_{T,p}. Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO.
Ningún cómputo en esta memo.

Resultado adelantado. No se logró escribir un objeto que cumpla A1–A6. Se prueban cinco lemas que
delimitan la semilla: (1) la operación sobre formas que corresponde a multiplicar factores de Euler es
la suma, por un homomorfismo explícito Φ_T de funciones meromorfas a formas; (2) toda clase cerrada
bajo ese producto (semigrupo) que contenga el objeto arquimediano y el de p = 2 contiene objetos que
violan la positividad y toda cota del índice negativo, para cada T > ½ log 2; (3) la condición «cada
factor local exactamente una vez por cada factor arquimediano» es exactamente la ecuación funcional de
la derivada logarítmica, dentro de la clase de productos Γ_ℝ^a ∏ Z_p^{b_p}; (4) restringida a los
objetos balanceados, toda afirmación sobre Φ_T es el objetivo mismo sobre un rayo de un cono convexo
(reformulación); (5) la propiedad no cónica que distingue «una vez» es la de coeficientes en {0, 1},
cerrada sólo bajo productos de soporte coprimo (monoide parcial). La inducción por primos con esa
operación parcial y la ecuación funcional como cociclo de las etapas intermedias ya está en la fase 122
(fases de dispersión b_∞, c_p). Queda abierto, sin objeto, un predicado de etapa no tautológico.

## 0. Cotejo

**Qué se buscó.** Grep en `03-research/` (todas las fases), `04-papers/47*`, `48*`, anexos de esta
carpeta, por: cociclo/cocycle, scattering, «twisted functional equation», Z_p(1−s), semigrupo de
factores, «product of Euler factors», local certificate, LK splitting, lem:shape-scale, integralidad
de coeficientes. Coincidencias de cociclo en fases 78, 122, 129, 136, 170 (Tate), 184.

**Abiertos en primaria.** Los obligatorios del encargo (BRIEF_CONSTRUCTOR, README, OBJECT_SPEC,
LEDGER, REVIEW_003, REVIEW_004, RULES_AVOID completo, ANNEX_COTEJO_LORENTZ_1 y _2, STATEMENT_001,
R160_C7_R1 §§5–6, ROUND_003_8 completo); `phase-159/G2_B8_R1.md` §§1–2 (Teoremas B, S, Cor. S′);
`G2_B8_R5.md` §§0–2 (definiciones, Teorema D); `phase-194/INV_F_001_DLOG_WALL_CONES.md` completo;
`phase-122/P122_018_GLOBAL_GAMMA_EULER_COCYCLE_PARITY_NO_GO.md` §§1–4; P47 `lem:shape-scale` y su
prueba, `cor:Tarch`; `ROUND_004_E.md` tabla de índices (líneas de 𝔪_T).

**No abiertos en primaria.** `INV_I_001` (sólo vía ANNEX_COTEJO_LORENTZ_2 fila 22); `BARRIER_W_001`
(vía el mismo anexo, fila 26); E70_10–12 (vía ROUND_003_8); fase 65; fase 120; P122_015, 017 y 014
(citados por P122_018); fase 129 y 78 (coincidencias de «cocycle» en otro sentido, no verificado).

**(1) Antecedentes más cercanos.**
- `G2_B8_R5` Teorema D: certificación local = reparto (C_p, K_p) de la parte arquimediana entre
  primos con formas locales q_p ≥ 0 sumadas; falla para T ≥ 0.5925. Es un cierre bajo **suma** de
  formas con el arquimediano repartido, no un cierre bajo producto con el arquimediano fijo.
- `INV_F_001` F0–F2 y §4: ∂log manda productos a sumas; toda premisa cónica en log ζ es ciega a cΛ;
  residuo declarado: una restricción curva que acople log ζ con exp(log ζ) (integralidad o ecuación
  funcional), OPEN.
- P47 `lem:shape-scale`: el vector F_+ = φ + φ(· − log 2) hace 𝔪_T(F_+) − c v_2‖φ‖² → −∞.
- `P122_018` §§1–4: fases de dispersión b_∞(τ) y c_p(τ) (exactamente Γ_ℝ(1−s)/Γ_ℝ(s) y
  Z_p(1−s)/Z_p(s) normalizados en la recta), producto finito completado Θ_T = b_∞ ∏ c_p^{−1}; ningún
  cociclo simétrico global acopla Γ y Euler; el acoplamiento no nulo es causal y es la historia
  entrante 𝓛_{T,−}.

**(2) Qué es nuevo.** Lema 2 en su variante de índice (toda cota n₋ ≤ κ cae, no sólo la positividad);
Lema 3 (balance ⟺ ecuación funcional, con la prueba por residuos en Re s = 0 que separa cada primo);
Lema 5 (coeficientes {0,1} ⟺ b_p ∈ {0,1}, y la conjunción con el Lema 3 fija b ≡ a = 1); la
comprobación explícita de por qué c = 2 rompe el cierre (el semigrupo lo genera; el monoide parcial
coprimo no). Ninguno lleva signo.

**(3) Por qué evitaría la dificultad.** No la evita. La dificultad de G2_B8 (interferencia entre primos)
y la de INV_F_001 (homogeneidad) reaparecen: el Lema 2 es la homogeneidad en forma de semigrupo, y el
Lema 4 muestra que la única salida que conserva un homomorfismo a formas es la del rayo balanceado, que
es el objetivo.

**(4) Identidad que conecta con la positividad global.** a_T = Φ_T(Γ_ℝ ζ) (Lema 1). Es exacta, pero
Φ_T es lineal en el exponente: no hay desigualdad que conecte.

## 1. Objeto

**Espacio.** 𝔐 = grupo multiplicativo de funciones meromorfas generado por Γ_ℝ(s) = π^{−s/2}Γ(s/2) y
Z_p(s) = (1 − p^{−s})^{−1}; sus elementos con exponentes reales se entienden a nivel de derivada
logarítmica:

    𝒪_{a,b} := Γ_ℝ^a ∏_p Z_p^{b_p},   g_{a,b}(s) := a h(s) + Σ_p b_p z_p(s),
    h = Γ_ℝ′/Γ_ℝ = −½ log π + ½ ψ(s/2),   z_p = Z_p′/Z_p = −log p · Σ_{k≥1} p^{−ks},

con b = (b_p) de la forma b_p = β + d_p, β ∈ ℝ y d finitamente soportado (así g es meromorfa en ℂ:
g = β(h + ζ′/ζ) + (a − β)h + Σ d_p z_p).

**Aplicación a formas.** Para F ∈ L²(I_T):

    Φ_T(𝒪)(F) := (1/2π) ∫ 2 Re g_𝒪(½ + iτ) |F̂(τ)|² dτ ,

definida término a término: la parte h contribuye (1/2π)∫2Re h(½+iτ)|F̂|², la parte z_p contribuye
−Σ_k 2 log p · p^{−k/2} Re c_F(k log p), suma finita porque c_F = 0 fuera de [−2T, 2T].

**Operación.** ⊛ = producto de funciones (suma de exponentes). Variante parcial: ⊛_cop, definido sólo
entre objetos cuyos conjuntos de primos con exponente no nulo son disjuntos.

**Objetos.** 𝒪_∞ = Γ_ℝ; 𝒪_p = Z_p; vector de Tate: e^{±t/2}, que entra sólo por P_T.

## 2. Identidad

**Lema 1 (PROVED).** (i) Φ_T(𝒪 ⊛ 𝒪′) = Φ_T(𝒪) + Φ_T(𝒪′). (ii) Φ_T(𝒪_∞) = 𝔪_T,
Φ_T(𝒪_p) = Π_{T,p}. (iii) a_T = Φ_T(Γ_ℝ ∏_p Z_p) = Φ_T(Γ_ℝ ζ) sobre L²(I_T), y para cΛ,
a_T^{(c)} = Φ_T(Γ_ℝ ζ^c).

*Demostración.* (i): g es aditiva en los exponentes y Φ_T es lineal en g. (ii): 2 Re h(½+iτ)
= −log π + Re ψ(¼ + iτ/2) = m(τ). Para p: 2 Re z_p(½+iτ) = −Σ_k 2 log p · p^{−k/2} cos(kτ log p)
= −Σ_k v_{p^k} cos(τ log p^k), serie absolutamente convergente; y (1/2π)∫cos(τu)|F̂|² = Re c_F(u)
porque ĉ_F = |F̂|². (iii): suma de (ii) sobre p; sólo p^k < N contribuyen. ∎

Lectura (respuesta a (d) del encargo). Multiplicar factores de Euler es, en las formas, sumar. La
clase 𝒦 hay que enunciarla sobre 𝒪 (sobre Z), no sobre g = V = Z⁻¹δZ: sobre g (o sobre Φ_T) toda
clase cerrada es aditiva, y el Lema 2 la cierra. Ésta es la misma ecuación V_{Z₁Z₂} = V_{Z₁} + V_{Z₂}
de E70_12 y de INV_F_001 Lema F0.

## 3. Mecanismo: qué clases cerradas existen

**Lema 2 (NO-GO con clase; PROVED relativo a la construcción de P47 lem:shape-scale).** Clase
declarada: (𝒦, ⊛) semigrupo, Φ: 𝒦 → formas sobre L²(I_T) aditiva (Φ(x ⊛ y) = Φ(x) + Φ(y)),
x_∞, x_2 ∈ 𝒦 con Φ(x_∞) = 𝔪_T y Φ(x_2) = Π_{T,2}, y un teorema de cierre «x ∈ 𝒦 ⟹ n₋(Φ(x)|P_T) ≤ κ»
para algún κ ≥ 0 fijo (κ = 0 es la positividad). Entonces para todo T > ½ log 2 la clase no existe.

*Demostración.* Sea ℓ < min(2T − log 2, log(3/2)), y φ_1, …, φ_{κ+3} reales no nulas con soportes
disjuntos dentro de un intervalo J ⊂ [−T, T − log 2] de longitud ℓ. Pongo F_j = φ_j + φ_j(· − log 2)
∈ L²(I_T) y V = span{F_j}. Para F = Σ a_jF_j, c_F(u) se anula salvo para u en (−ℓ, ℓ) ∪
(± log 2 + (−ℓ, ℓ)); como ℓ < log(3/2), ningún log n con n ≥ 3 cae ahí, y la única contribución
aritmética es la de n = 2: c_F(log 2) = ∫F(t)F(t − log 2)dt = Σ_j a_j² ‖φ_j‖² (los términos cruzados
se anulan por soportes disjuntos; ∫φ_i(t)φ_j(t − log 2)dt = 0 porque J ∩ (J + log 2) = ∅). Luego
Π_{T,2}|_V = −v_2 diag(‖φ_j‖²), definida negativa, y 𝔪_T|_V es una forma acotada en dimensión finita.
El semigrupo contiene x_∞ ⊛ x_2^{⊛n}, con Φ = 𝔪_T + nΠ_{T,2}, definida negativa en V para n grande.
V ∩ P_T tiene dimensión ≥ κ + 1, luego n₋(Φ|P_T) ≥ κ + 1. ∎

El lema no usa más primo que 2 ni ninguna propiedad de Λ salvo v_2 > 0: es una obstrucción de formato,
genérica en el peine (como R3-d). Cubre en particular «cierre bajo producto aplicado a la signatura»
con cualquier cota de índice. Su contenido es la homogeneidad de INV_F_001 F2 escrita como semigrupo.

**Respuesta a (a) del encargo.** 𝒪_∞ no puede estar en una clase de signo acotado para T grande: n₋(𝔪_T|P_T)
≥ ⌈2Tτ_0/π⌉ − 3 (P47 thm:J, thm:index, citados en `ROUND_004_E.md`, tabla; CITED) y 𝔪_T es negativa en
algún vector de P_T para T ≥ 0.60 (P47 cor:Tarch, CITED). Así, una clase 𝒦 definida por signatura de Φ
no contiene a 𝒪_∞ salvo para κ creciente con T. **(b)**: Π_{T,p} es indefinida en L²(I_T) (su
símbolo cambia de signo); está en una clase de índice acotado sólo si κ ≥ n₋(Π_{T,p}), que no es
finito en general (ARGUED: paquetes de onda de alta frecuencia donde el símbolo −Σ_k v_{p^k}
cos(kτ log p) es negativo). Ninguna clase de signatura sobre Φ cumple (a) y (b) con κ fijo.

**Lema 3 (balance ⟺ ecuación funcional; PROVED, con la ecuación funcional de Γ_ℝζ CITED).** En la clase
del §1, g_{a,b}(s) = −g_{a,b}(1 − s) idénticamente si y sólo si d ≡ 0 y a = β, es decir b_p = a para
todo p.

*Demostración.* Por la ecuación funcional Γ_ℝζ(s) = Γ_ℝζ(1 − s), la función h + ζ′/ζ es impar respecto
de s ↦ 1 − s. Luego g(s) + g(1 − s) = (a − β)H(s) + Σ_p d_p [z_p(s) + z_p(1 − s)], H = h(s) + h(1 − s).
Fijo p con d_p ≠ 0 y s_0 = 2πi/log p. z_p tiene allí un polo simple de residuo −1 (cero simple de
1 − p^{−s}); z_p(1 − s) tiene polos en Re s = 1; z_q, q ≠ p, tiene polos en 2πik/log q ≠ s_0 porque
log q/log p ∉ ℚ; H es holomorfa en Re s = 0 salvo en s = 0 (polos de ψ(s/2) en 0, −2, …; de
ψ((1 − s)/2) en 1, 3, …). Si g(s) + g(1 − s) ≡ 0, el residuo en s_0 es −d_p = 0. Entonces
(a − β)H ≡ 0, y H tiene polo en s = 0, luego a = β. El recíproco es la ecuación funcional. ∎

Respuesta a (e) del encargo. La hipótesis del teorema de cierre que exige «cada factor local
exactamente una vez por cada factor arquimediano» es la autodualidad de la derivada logarítmica
g(s) = −g(1 − s) del compuesto. Para c = 2 (a = 1, β = 2) falla por el término (a − β)H = −H; para c no
entero, igual con −(c − 1)H; para a_P (d_p = −1, p < P) falla por los residuos en 2πik/log p. Para un
objeto con ecuación funcional sin producto (Davenport–Heilbronn) el lema no se aplica: no está en la
clase, porque su derivada logarítmica no es combinación de h y z_p. Esa exclusión es de pertenencia,
no de signo.

**Lema 4 (lo balanceado no lleva signo; PROVED).** E_T := {(a, b) ∈ ℝ × ℝ^{π(N)} : a𝔪_T + Σ_p b_pΠ_{T,p}
⪰ 0 en P_T} es un cono convexo cerrado (intersección de semiespacios, uno por F). Por el Lema 1, sobre
los objetos balanceados Φ_T(𝒪_{a,a}) = a·a_T, de modo que «todo objeto balanceado con a > 0 está en
E_T» equivale a (1, 1, …, 1) ∈ E_T, que es (★)_T. El semigrupo de objetos balanceados es {(Γ_ℝζ)^n}:
el cierre bajo ⊛ entre ellos sólo escala. Reformulación (patrón B3); no es un paso de signo.

**Lema 5 (la propiedad no cónica que distingue «una vez»; PROVED).** Para b_p ∈ ℝ, la serie de Dirichlet
de ∏_{p∈S} Z_p^{b_p} (S finito) tiene todos sus coeficientes en {0, 1} si y sólo si b_p ∈ {0, 1} para
todo p ∈ S. La clase 𝒦_{01} = {∏_{p∈S}Z_p : S conjunto de primos} es cerrada bajo ⊛_cop y no bajo ⊛.

*Demostración.* Por factorización única el coeficiente en p^k de ∏ Z_p^{b_p} es el de Z_p^{b_p} =
Σ_k binom(b_p + k − 1, k) p^{−ks}: en k = 1 vale b_p, en k = 2 vale b_p(b_p + 1)/2. Ambos en {0,1}
fuerzan b_p ∈ {0, 1}. Recíproco: ∏_{p∈S}Z_p = Σ_{n: primos de n en S} n^{−s}. Z_p ⊛ Z_p = Z_p² tiene
coeficiente 2 en p. ⊛_cop conserva la forma ∏_{p∈S}Z_p. ∎

Con el Lema 3: dentro de la clase del §1, {coeficientes de la parte finita en {0,1}} ∧ {g impar} fija
b_p ≡ a ∈ {0, 1}, es decir el objeto trivial o Γ_ℝζ (en el Lema 5 se aplica a cada subproducto finito
de la parte finita). Es la conjunción integralidad ∧ ecuación
funcional de INV_F_001 §4 e INV_I_001, ahora con la operación de cierre explícita: ⊛_cop.

**Teorema de cierre que habría que probar (OPEN, sin candidato).** Enunciado con la única estructura
que pasa los Lemas 2–5: un predicado I(Q, S) sobre pares (forma, conjunto de primos ya añadidos) tal
que (i) I(𝔪_T, ∅); (ii) I(Q, S) ∧ p ∉ S ⟹ I(Q + Π_{T,p}, S ∪ {p}); (iii) I(Q, {p < N}) ⟹ Q ⪰ 0 en
P_T; (iv) I tiene una fórmula que no contiene la conclusión. Sin (iv) existe trivialmente:
I(Q, S) := «Q + Σ_{p∉S, p<N} Π_{T,p} ⪰ 0 en P_T», que es (★)_T (patrón J3). Verificado: la
estructura de monoide parcial (ii) es la de 𝒦_{01} (Lema 5). Abierto: (iv). Por el Lema 3, las etapas
intermedias Γ_ℝ ∏_{p∈S}Z_p no tienen ecuación funcional; la llevan sólo torcida por el cociclo finito
∏_{p∉S} Z_p(1 − s)/Z_p(s), es decir por las fases de dispersión c_p de `P122_018` (1.3). Esa
contabilidad ya está hecha allí: el acoplamiento simétrico Γ–Euler es nulo (Teor. 2.1) y el causal es
la historia entrante 𝓛_{T,−} (§4). Un I(Q, S) que lea el cociclo cae en esa fase.

## 4. Controles

| Falsificador | Lema 2 (semigrupo) | Lemas 3–5 (balance, {0,1}, ⊛_cop) |
|---|---|---|
| c = 2 | el semigrupo lo genera (x_2^{⊛2}); el cierre lo declara en 𝒦 y la conclusión es falsa para c grande en T > ½ log 2 (Lema 2). Que falle en c = 2 exactamente no se comprueba aquí | Lema 3: (a − β)H = −H ≠ 0; Lema 5: coeficiente 2 en p. No alcanzable por ⊛_cop. Pero la ruptura es de pertenencia, no de signo: R3-i no queda satisfecho, porque no hay resto ≥ 0 que deje de serlo |
| c no entero | igual (el semigrupo sólo genera enteros; el fallo de c pequeño, T ≥ 0.60, no lo da el semigrupo) | Lema 3 con −(c − 1)H; Lema 5: coeficiente c ∉ {0,1} |
| a_P | el semigrupo contiene Γ_ℝ ∏_{p≥P}Z_p | Lema 5 lo admite (coeficientes {0,1}); Lema 3 lo excluye por residuos en Re s = 0 |
| sin producto (Davenport–Heilbronn) | no está en 𝒦 | no está en la clase; exclusión de pertenencia |

Ninguna fila es la ruptura de un resto ≥ 0: no hay paso de signo que romper. La exigencia de A5 no se
cumple.

## 5. Cotejo final y qué cambia

Antecedente más cercano: G2_B8_R5 (suma de formas locales con reparto arquimediano) e INV_F_001 §4
(residuo no cónico). Lo que cambia aquí es sólo de formato: el cierre bajo producto con Γ_ℝ fijo se
reduce, por el Lema 1, a suma con 𝔪_T sin repartir, y entonces el Lema 2 lo cierra con un argumento más
corto que el Teorema D (no requiere T ≥ 0.5925, sólo T > ½ log 2, pero a cambio exige cerrar bajo
potencias). La versión parcial ⊛_cop con ecuación funcional es la arquitectura de la fase 122.

## 6. Veredicto propio

No logré escribir un objeto que cumpla A1–A6.

## Resultado

NO-GO con clase (Lema 2: semigrupos con aplicación aditiva a formas, positividad o índice acotado,
T > ½ log 2), más tres lemas PROVED de delimitación (3, 4, 5). Sin mecanismo nuevo.

## Qué se probó

Lema 1 (homomorfismo Φ_T; a_T = Φ_T(Γ_ℝζ)); Lema 2 (NO-GO de semigrupo, también para cotas de índice);
Lema 3 (exponentes balanceados ⟺ g impar; separación primo a primo por residuos en Re s = 0); Lema 4
(sobre lo balanceado, reformulación por cono convexo); Lema 5 ({0,1} ⟺ b_p ∈ {0,1}; cierre sólo bajo
⊛_cop).

## Qué falló y por qué

Toda clase que se lee a través de las formas es aditiva (∂log), y la aditividad con potencias genera
cΛ con c entero grande (Lema 2). Quitar las potencias exige el monoide parcial coprimo y la ecuación
funcional; ambas cosas fijan un único objeto, Γ_ℝζ, y un teorema cuya hipótesis fija un único objeto no
tiene contenido de cierre: el paso de signo vuelve a ser (★)_T. La inducción por primos con las etapas
torcidas por el cociclo de dispersión es la de la fase 122.

## Siguiente paso concreto

Ninguno en esta semilla sin un predicado de etapa I(Q, S) con fórmula propia que use algo de las
etapas distinto de Φ_T (por ejemplo, los coeficientes de la serie más allá de N), y antes cotejado con
P122_014, 015, 017 y la historia entrante 𝓛_{T,−} de la fase 121. Registrar el Lema 2 en el índice y el
grid como NO-GO de clase (semigrupo aditivo, índice acotado).
