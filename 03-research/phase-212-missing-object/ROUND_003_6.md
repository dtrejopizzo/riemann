# Ronda 3, opción 6 — Conversión conjunta de la identidad finita de Poisson–Chebyshev sin recombinar (memo de selección)

Memo de selección, no de construcción. Objetivo (★): λ_A(T) ≥ 0 para todo T, con las definiciones de
`../phase-211-sign-sandbox/STATEMENT_001.md`; N ≥ e^{2T}, M ≥ N. Notación de P47 §sec:firstcontact
(`04-papers/47-row-d-dual-certificates/main.tex`: S_N, S′_N, L_M, A_M = 𝓜 − L_M − L_M*, E_N = S_N𝓕 − JS_N,
H_{M,N} = L_MS_N − S′_N, thm:PCfinite). Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO /
NUMÉRICO.

Pregunta: ¿se puede mantener separado el bloque interior k ≤ N (anulado por Σ_{d|k}Λ(d) = log k) del
exterior, de modo que la suma (cola H_{M,N} + bloque de E_N + Tate) sea una forma hermítica explícita
sobre P_T con signo legible, usando la anulación interior como insumo de una desigualdad?

## Cotejo

Búsquedas hechas (grep por palabra clave y sinónimos, después lectura primaria de lo encontrado):
«envelope / envolvente / infimum over / supremum over / F-dependent test / test dependiente» en las
fases 161, 162, 170, 182, 211, 212, el grid y el índice (coincidencias sólo en usos ajenos: envolventes
de símbolo y de certificados en 211 y 162, ninguna sobre los parámetros (M, N, L, δ) de thm:PCfinite);
«(c − 1) / c > 1» en la fase 170 (sin coincidencias); «Möbius inverse / causal Möbius / M_N S_N» en
161, 162, 170, 182, 211 y P47 (coincidencias en R170_853–858, 860, 878, 883 y R161_066). Leídos en
primaria: P47 l. 6625–6946 (thm:PCfinite, eq:Gammaenergy, eq:collar, eq:Qbalance, eq:Qrecombine,
eq:Qspectral, prop:GEgap, eq:equivgate, prob:annihilate, rem:returnremarks); `R170_816` §§1–2;
`R170_819`, `820`, `821`, `835`, `838`, `856`, `900` en su planteamiento y veredicto; `R170_837` §§5–6
enteros; `R170_840` §§0–2; `R170_878` §0; `R161_033` §§5–8; `ROUND_002_A`, `REVIEW_002_A`, `LEDGER`.
No se abrieron en primaria `R162_405`–`408` ni `R182_201` más allá de su título; lo que de ellos se
dice abajo procede de `R170_840` §2, que cita `R162_406`. Una búsqueda sin coincidencias no prueba
novedad.

### (1) Antecedente más cercano

**`R170_837` §6, ecuaciones (6.1)–(6.10)** (leído en primaria). Es la pregunta de esta memo, escrita:
para un peso a, H^a_{M,N} = 𝒟_a^{≤N} + H^{a,>N}_{M,N} con 𝒟_a^{≤N} = Σ_{k≤N} δ_a(k)k^{−1/2}τ_{log k},
δ_a(k) = Σ_{d|k}a(d) − log k (6.2)–(6.4); el defecto interior entra en PC como −J𝒟_a^{≤N} − 𝒟_a^{≤N}𝓕
(6.5); tras sustituir S′_N = L_M^aS_N − H^a_{M,N} la forma mixta es **independiente de a** (6.7); y
«la aritmética sólo carga si la proyección de coeficientes interiores (6.8) se usa **antes** de (6.6)
… una forma que cumpla el requisito debe usar (6.8) para transformar un residuo, no sólo reescribir
(6.6)». El monitor (6.9) se anula para Λ (6.10) y «no da signo cuando es cero».

**`R170_840` §0** (leído en primaria): NO-GO con clase PROVED en la fase 170 para expresiones
bilaterales formadas con (1) la identidad de minimalidad entre ventanas, (2) las dos orientaciones del
collar y J, (3) **PC finita, cruda o renormalizada, antes o después de la cancelación Λ∗1 = log**,
(4) la identidad de Chebyshev comprimida, (5) el detector R_L, el collar Gamma–Euler y el
Schur/Feshbach de `R162_408`: toda tal expresión tiene la forma normal (0.1)/(0.3), y «(0.4) elimina
un bloque de coeficientes, pero no orienta ninguno de los tres términos». El dato mínimo que proponen
(0.5) es una ley virial bilateral que «debe obtenerse antes de recombinar PC y usar (0.4)
esencialmente»; OPEN, sin objeto.

**`R161_033` §5**: las dos salidas OPEN que deja al retirar la realización discreta son
**A. dilatación de fuente isométrica** (una isometría explícita V_N desde datos aditivos de
Poisson/Fourier cuya síntesis física sea el puerto coherente de (PC-ren)) y **B. compensación exacta
del Gram cruzado** I_N(f) = Σ_{k≠l}(log k)(log l)(kl)^{−1/2}Re⟨Δ_kf, Δ_lf⟩ por los términos polar/Gamma
y de Tate orientados por paridad. B fue tomada por `R161_034` (identifica el Gram cruzado con el canal
producto–cociente de la fase 106; fila del índice DEAD: no cancela con el Tate de rango dos en el
álgebra invariante por traslación). A no tiene objeto en el corpus consultado (ARGUED: búsqueda, no
prueba).

**Test de Möbius**: `R170_853` y `R170_878` (0.1)–(0.4) ya invierten la compresión de S_N* por el
peine de Möbius, (PS_N*P)^{−1} = PM*P para N ≥ e^{2T}, y obtienen un lazo exterior de Möbius. El test
que se usa abajo en §(4) es esa misma inversión, en la variante truncada.

### (2) Objeto realmente nuevo

No hay objeto (ℋ_T, V_T, ρ_T). Lo que esta memo escribe es:

(a) una identidad exacta sobre todo P_T, con un test explícito no local, que expresa a_T(F) por los
bloques de thm:PCfinite sin recombinar (identidad (4.3)); su contenido no es nuevo (es la inversión de
Möbius de `R170_878` aplicada a thm:PCfinite) y se escribe sólo para fijar los bloques;

(b) un lema corto, PROVED, de ceguera al peso de los bloques separados (Lema 1 y Corolario 2 de §(4)):
a lo largo de la familia cΛ, cada bloque separado es independiente de c o exactamente proporcional a c,
y la única cantidad escrita que separa c = 1 de c ≠ 1 es (c − 1) veces una forma que, como forma
cuadrática sobre P_T, es b_T(F) menos bloques exteriores (Lema 3). Consecuencia: toda propiedad
positivamente homogénea del bloque exterior separado —su signo, el de cualquier envolvente en
(M, N, L, δ), el de su límite L → ∞, el de su evaluación con un test elegido según F sin usar el peso,
su escritura como Σ h(k)|ℓ_k|² + ρ— es la misma para todo c > 0. Esto cierra, contra el falsificador
cΛ, tres de las operaciones que `REVIEW_002_A` §5.2 (puntos 1, 4 y 6) dejó sin examinar, en la clase
declarada en el Corolario 2. No aporta signo.

Lo que falta escribir para una candidata: una forma Ψ sobre P_T, construida con los bloques de (4.3),
que no sea afín en el peso (por ejemplo, con un test que dependa de los valores del peso), cuya
igualdad con a_T use δ_Λ = 0 en un término de grado ≥ 2 en el peso, y que sea manifiestamente ≥ 0.
Nada de esto está escrito, ni aquí ni en el corpus consultado.

### (3) ¿Evita la dificultad del antecedente?

No. La dificultad de `R170_837` (6.7) es que, recombinada, la forma olvida el peso; la de
`R170_840` es que, antes o después de la cancelación, (0.4) sólo borra un bloque. El Lema 1 muestra
que **no recombinar no cambia esa situación** para las operaciones listadas: los bloques separados
son afines en el peso, el bloque interior aparece con coeficiente (c − 1) delante de una forma fija, y
la anulación en c = 1 sólo puede actuar como borrado de un término de una identidad afín. Usarla como
insumo de una desigualdad exige una operación no afín en el peso, que esta memo no tiene.

### (4) Identidad que conecta con la forma completa sobre P_T

Trabajamos sobre el subespacio denso de P_T de funciones lisas con soporte en I_T = [−T, T]; la
extensión a P_T entero es la habitual del dominio de formas (CONDITIONAL a la continuidad de cada
bloque en la norma del grafo, que no se verifica aquí). Convenciones de P47: V_{−log n}F(t) = F(t + log n),
𝓕* = 𝓕^{−1} = 𝓕.

**Paso 1 (PROVED).** Para F con soporte en I_T y M ≥ N ≥ e^{2T},

    a_T(F) = Re⟨A_MF, F⟩.                                                      (4.1)

Los términos de L_M con log d ≥ 2T trasladan el soporte fuera de I_T y no aparean; los restantes son
los de B_N + B_N* (P47 §subsec:collars).

**Paso 2: el test de Möbius truncado (PROVED).** Sea M_N = Σ_{n≤N} μ(n)n^{−1/2}V_{−log n}. Los traslados
conmutan entre sí, con 𝓜 y con L_M, L_M*. Se tiene

    M_NS_N = I + U_N,    U_N = Σ_{N<k≤N²} c_N(k) k^{−1/2}V_{−log k},
    c_N(k) = Σ_{d|k, d≤N, k/d≤N} μ(d),

porque para 1 < k ≤ N todos los divisores aparecen y Σ_{d|k}μ(d) = 0. Por tanto

    Re⟨S_NA_MF, M_N*F⟩ = Re⟨M_NS_NA_MF, F⟩ = a_T(F) + R(F),                   (4.2)
    R(F) = Σ_{N<k≤N²} c_N(k)k^{−1/2} Re[ ⟨𝓜V_{−log k}F, F⟩
             − Σ_{d≤M, |log(k/d)|<2T} Λ(d)d^{−1/2}⟨V_{log d−log k}F, F⟩ ].

En R(F), V_{−log k}F tiene soporte en I_T − log k, disjunto de I_T (log k > 2T); el término L_M no aparea;
el término L_M* aparea sólo si |log(k/d)| < 2T: R ve exactamente las casi-coincidencias d ≈ k con
k ∈ (N, N²] y d potencia de primo ≤ M, con pesos de Möbius c_N(k) sin signo, más la parte no local de
𝓜 entre I_T y su traslado.

**Paso 3: sustitución de PC (PROVED sobre el núcleo de Schwartz; CONDITIONAL en el dominio de formas).**
Aplicando thm:PCfinite a 𝓕F y usando 𝓕² = I:

    a_T(F) = Re⟨({X, E_N} − L_M*E_N − JH_{M,N} − H_{M,N}𝓕)𝓕F, M_N*F⟩ − R(F).   (4.3)

Respuesta a «qué test»: el teorema se aparea con un test, y la identidad pedida sobre todo P_T exige
uno no local. El de R170_816 es z = S_N𝓕Σ_LF y conecta con a_T sólo sobre el radical (eq:Qbalance,
eq:Qrecombine). El de (4.3) es M_N*F con la variable desplazada a 𝓕F; **z = F no tiene sustituto
exacto por ventana**: el sustituto exacto (Möbius truncado) cuesta el resto R(F), que es otra cola
exterior k > N, con coeficientes c_N(k) de signo variable. Sobre todo P_T no aparece vector de Tate:
el Tate procede de la ecuación débil del radical y sólo entra en la versión eq:Qbalance.

**Forma hermítica que queda sin recombinar.** Con F ∈ P_T,

    f_0(F) = Re⟨{X, E_N}𝓕F, M_N*F⟩                         (bloque Poisson; no ve el peso)
    f_1(F) = Re⟨(L_M*E_N + JH_{M,N} + H_{M,N}𝓕)𝓕F, M_N*F⟩  (polar de E_N y cola k > N)
    g(F)   = Re⟨(JS′_N + S′_N𝓕)𝓕F, M_N*F⟩                  (jet interior de Chebyshev)
    R(F) = R_0(F) − R_1(F)                                  (parte 𝓜 y parte de primos de (4.2))

(4.3) dice a_T = f_0 − f_1 − R_0 + R_1. Cada una de las cinco es una forma hermítica explícita sobre
P_T; ninguna tiene signo conocido.

**Lema 1 (ceguera afín, PROVED).** Para el peso cΛ, c real, con a_T^{(c)} la forma con cΛ en lugar
de Λ, y todos los demás datos fijos,

    a_T^{(c)}(F) = f_0(F) − c f_1(F) − (c − 1) g(F) − R_0(F) + c R_1(F)    para todo F ∈ P_T,   (4.4)

con f_0, f_1, g, R_0, R_1 las formas de arriba, que no dependen de c.

*Demostración.* L_M^{cΛ} = cL_M, luego H^{cΛ}_{M,N} = cL_MS_N − S′_N = cH_{M,N} + (c − 1)S′_N, y
A_M^{(c)} = 𝓜 − c(L_M + L_M*). E_N, X, 𝓕, S_N, S′_N, M_N no dependen del peso. La demostración de
thm:PCfinite no usa los valores del peso (sólo [X,S_N] = −S′_N y las identidades de Fourier), luego
S_NA_M^{(c)}𝓕 = {X,E_N} − cL_M*E_N − JH^{cΛ} − H^{cΛ}𝓕. Los Pasos 1–2 valen para A_M^{(c)} con R^{(c)} =
R_0 − cR_1. Sustituyendo sale (4.4). ∎

**Corolario 2 (NO-GO con clase contra cΛ, PROVED).** Clase 𝒞_sep: afirmaciones de signo sobre el
bloque exterior separado f_1 (cola k > N más polar L_M*E_N), o sobre sus componentes (la cola sola, el
polar solo, o Σ_{k>N}h(k)|ℓ_k|² + ρ como escritura de la cola), obtenidas por cualquiera de estas
operaciones: (i) evaluación con cualquier test, también dependiente de F, siempre que su elección no
use los valores del peso; (ii) ínfimo, supremo o promedio con medida positiva sobre (M, N, L, δ, test);
(iii) límite L → ∞ o M → ∞ cuando exista; (iv) multiplicación por funciones positivas de F. Toda
afirmación de 𝒞_sep vale para cΛ con un c > 0 si y sólo si vale para todo c > 0. En particular ninguna
puede romperse en c ≠ 1 (cláusula O4), ni siquiera combinada con f_0, que no ve el peso.

*Demostración.* Por el Lema 1, f_1^{(c)} = c f_1 (y cada componente se multiplica por c: la cola tiene
coeficientes c·h_{M,N}(k), el polar −cL_M*E_N). Las operaciones (i)–(iv) conmutan con la multiplicación
por c > 0 y preservan el signo. ∎

Lo mismo vale, palabra por palabra, para el resto exterior R_1 de (4.2). Para el bloque f_0 la
afirmación es más fuerte: no depende de ningún peso (sólo del peine entero de S_N y de 𝓕), luego
sobrevive también a a_P, a borrados y amplificaciones finitos y a todo sistema con el mismo S_N.

**Lema 3 (qué separa c = 1 de c ≠ 1, PROVED).** Con b_T(F) = Re⟨(L_M + L_M*)F, F⟩ la forma de los
primos de a_T,

    g(F) = b_T(F) − f_1(F) + R_1(F)    sobre P_T.                                  (4.5)

*Demostración.* (4.4) en c = 0 y c = 1 da m_T = f_0 + g − R_0 y a_T = f_0 − f_1 − R_0 + R_1; se restan y se
usa a_T = m_T − b_T. ∎

Consecuencia: en (4.4) la diferencia entre c y 1 es a_T^{(c)} − a_T = −(c − 1)b_T(F), como debía; la
anulación interior no aporta otra cosa que el término (c − 1)g que, por (4.5), se reabsorbe en b_T con
los bloques exteriores. La cantidad escrita que distingue c > 1 de c = 1 es (c − 1)b_T(F); para que
una desigualdad lo use haría falta controlar b_T(F) con margen cero frente a f_0 − R_0, que es (★)
mismo. **Ninguna cantidad escrita en el corpus consultado distingue c > 1 de c = 1 por otro medio**
(ARGUED: resultado de búsqueda). Como la forma es afín en el peine (OBJECT_SPEC O2), toda cantidad
que sea afín en el peso tiene el mismo defecto; una que lo distinga por sí misma tiene que ser de
grado ≥ 2 en el peso, del tipo (c − 1)²‖v‖² o c(c − 1)X, y anularse en c = 1 por δ_Λ = 0. No hay
ninguna escrita.

**Qué operación podría dar el signo.** Las tres de la pregunta, sobre los bloques separados: la
envolvente en (M, N, L, δ) y el límite L → ∞ caen en 𝒞_sep si se aplican al bloque exterior solo; la
elección del test dependiente de F cae en 𝒞_sep si no usa el peso. Aplicadas a la suma completa
f_0 − f_1 − R_0 + R_1 no están excluidas, pero esa suma es a_T(F) por (4.3) para todo valor de los
parámetros: su envolvente en (M, N, L, δ) es a_T(F) misma (los parámetros no aparecen en el lado
izquierdo), y no hay nada que optimizar. Lo único que (4.3) deja variar es el reparto entre bloques.

### (5) Líneas que se rompen para cΛ y a_P

- **cΛ, c ≠ 1.** En (4.3) aparece el término −(c − 1)g(F) (Lema 1). Cualquier escritura de signo que
  sólo use f_1 o R_1 separados no se rompe (Corolario 2): sobrevive a cΛ y, por tanto, está mal como
  paso de signo. Una escritura que use la suma completa se rompe sólo por el término (c − 1)b_T(F) del
  Lema 3, es decir, por la recombinación.
- **a_P con P > N.** L_M^{a_P} no contiene d < P, de modo que dentro de la ventana a_T^{(a_P)} = m_T y
  H^{a_P}_{M,N} = −S′_N + (cola con d ≥ P). En (4.3) la línea que cambia es el bloque interior: aparece
  −Re⟨(J𝒟 + 𝒟𝓕)𝓕F, M_N*F⟩ con 𝒟 = 𝒟_{a_P}^{≤N} = −S′_N (para P > N, δ_{a_P}(k) = −log k en todo
  k ≤ N), es decir, el término +g(F) entero; la cola exterior pierde todos los términos con d < P y
  no es proporcional a la de Λ, de modo que el Corolario 2 no se aplica a a_P. La anulación del bloque
  interior es lo que se rompe. f_0 no cambia: el bloque de Poisson sobrevive a a_P, como a todo
  falsificador con el mismo peine entero.

## Resultado

Repetición en lo esencial, más un NO-GO corto con clase. La pregunta —usar la anulación interior antes
de recombinar, como insumo y no como cancelación— está planteada literalmente en `R170_837` §6
(6.8)–(6.9) y cerrada para expresiones bilaterales en la clase de `R170_840` §0; el test de Möbius que
da una identidad sobre todo P_T está en `R170_853`/`R170_878`. Sin mecanismo nuevo para el signo. No
hay candidata lista para construcción.

## Qué se probó

1. (4.1)–(4.3), PROVED en el núcleo liso (CONDITIONAL en el dominio de formas): a_T expresada sobre
   todo P_T por los bloques de thm:PCfinite sin recombinar, con el test M_N*F y el resto R(F) de
   casi-coincidencias d ≈ k, k ∈ (N, N²], con pesos de Möbius. Contenido no nuevo (`R170_878`).
2. Lema 1, PROVED: a lo largo de cΛ los bloques separados son independientes de c o proporcionales a
   c; el interior entra con coeficiente (c − 1).
3. Corolario 2, NO-GO con clase 𝒞_sep, PROVED: ninguna afirmación de signo sobre el bloque exterior
   separado obtenida por test independiente del peso, envolvente o promedio positivo en (M, N, L, δ,
   test), límite L → ∞ o reescalado positivo se rompe en c ≠ 1.
4. Lema 3, PROVED: la forma interior g es b_T − f_1 + R_1; la única cantidad escrita que separa c = 1
   de c ≠ 1 es (c − 1)b_T.
5. Las dos salidas de `R161_033`: A (dilatación de fuente isométrica) sin objeto en el corpus
   consultado; B (compensación del Gram cruzado) tomada por `R161_034`, DEAD en el índice.

## Qué falló y por qué

- La separación no da signo porque la identidad es afín en el peso: el bloque interior es un término
  borrado de una identidad afín (Lema 1), no una ecuación que pueda usarse para orientar otro término.
- La envolvente en los parámetros es trivial sobre la suma completa (vale a_T para todo parámetro) y
  ciega al peso sobre el bloque exterior separado (Corolario 2).
- z = F no tiene sustituto exacto por ventana; el de Möbius cuesta otra cola exterior R(F) sin signo.

NO excluido (delimitación; nada de esto tiene objeto escrito):
1. tests o funcionales que usen los **valores del peso** (por ejemplo, construidos con L_M o con Λ en
   [2, N)), que hacen los bloques no afines en c y permiten que δ_Λ = 0 anule un término de grado ≥ 2
   en el peso; es la única vía que esta memo deja abierta para «anulación como insumo», y debe pasar
   OBJECT_SPEC O2 (no linealidad en cómo V_T actúa sobre F, no sólo en productos de pesos);
2. operaciones no lineales en F aplicadas a la suma completa con un reparto entre bloques dependiente
   de F (el Corolario 2 sólo cubre el bloque exterior solo);
3. la ley virial bilateral (0.5) de `R170_840`, OPEN, y la salida A de `R161_033`;
4. el resto R(F) de (4.2) como objeto propio: es una forma explícita de casi-coincidencias d ≈ k
   (cláusula O6) con pesos de Möbius; su signo no se examinó;
5. a_P y los falsificadores no proporcionales a Λ: el Corolario 2 no los cubre.

## Siguiente paso concreto

No construir sobre esta zona sin un test que dependa de los valores del peso y un término de grado
≥ 2 en el peso escrito explícitamente (punto 1 de la lista). Anotar en el índice y en el grid: «Fase
212, conversión conjunta PC sin recombinar: repetición de `R170_837` §6 y `R170_840` §0; NO-GO con
clase 𝒞_sep PROVED (`ROUND_003_6` Corolario 2): sin test dependiente del peso, envolventes, límites y
tests dependientes de F sobre el bloque exterior separado son ciegos a cΛ; Lema 3: la anulación
interior se reabsorbe en (c − 1)b_T. Signo global OPEN.» Antes de anotarlo, un segundo lector debe
verificar (4.2) (signo y rango de c_N(k), soporte de R) y el Corolario 2.
