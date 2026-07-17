# Doc 115 — Auditoría adversarial del Teorema 2.3 del Doc 112 (la dicotomía condicional)

**Programa:** Hipótesis de Riemann — Phase 38, auditoría final
**Fecha:** junio 2026
**Auditor:** adversarial — mandato: destruir el resultado, no confirmarlo
**Objeto:** Doc 112, Teorema 2.3 (LP-112 ⟹ m∈{0,∞}) y Proposición 2.6 (densidad cero de testigos);
Doc 113 (no-precedencia); P44 (`06-papers/P44-two-lemma-architecture/main.tex`), que apoya toda su
arquitectura sobre estos dos enunciados.
**Regla:** sin numéricos; honestidad absoluta; toda afirmación de literatura es verificable
(Bagchi 1987, Laurinčikas 1996, Titchmarsh 1986 — las mismas fuentes que el Doc 112 cita).

---

## 0. Resultado de la auditoría en una línea

**El Teorema 2.3 SOBREVIVE CON CORRECCIONES.** La prueba del condicional es esencialmente
correcta (Rouché, elecciones de constantes, novedad de la réplica, iteración: verificados);
hay UN desajuste real de enunciado en la versión débil LP-112⁻ (umbral de altura insuficiente,
reparable en una línea), una imprecisión conceptual repetida sobre "vacuidad desconocida"
(bajo H(m) la vacuidad del conjunto de testigos por encima del umbral es TEOREMA — corolario
del propio Thm. 2.3 por contraposición — y eso NO vacua el teorema, pero el lenguaje de
D112/D113/P44 debe corregirse), un descalce de cuantificadores entre Doc 112 (forma débil
∀D∃sucesión) y P44/D113-§0 (forma fuerte ∃sucesión∀D, no trivialmente equivalente), y un
sobreclamo sistemático en los titulares sobre la no-equivalencia con RH (que es NO-REFUTADA,
no PROBADA — y de hecho no puede ser probada en el sentido material). Ninguno de estos
defectos derrumba la arquitectura de P44; todos exigen corrección de texto.

---

## 1. Línea 1 — El margen η y el orden de las elecciones: VERIFICADO

La prueba (D112, §2.2) elige, bajo H(m) y con ρ₀ = β+iγ₀ = ½+δ+iγ₀ off-crítico fijo:

r := ½·min( δ, 1−β, dist(ρ₀, Z(ζ)∖{ρ₀}) ) > 0.

Auditoría de cada pieza:

1. **dist(ρ₀, Z(ζ)∖{ρ₀}) > 0.** Los ceros de ζ forman un conjunto discreto sin puntos de
   acumulación en ℂ (ζ ≢ 0, holomorfa salvo el polo); el conjunto es infinito pero sus
   elementos escapan a infinito en altura, de modo que la distancia de ρ₀ al resto se
   alcanza y es positiva. ✓. (Multiplicidad: si ρ₀ es múltiple, Rouché cuenta con
   multiplicidad y entrega ≥ 1 cero — sin problema.)
2. **D = D̄(ρ₀,r) dentro de la franja abierta y lejos de la línea.** Re s ∈ (β−r, β+r);
   r ≤ δ/2 da Re s > ½+δ/2 > ½ (el disco no toca Re = ½, donde viven los ceros on-line),
   y r ≤ (1−β)/2 da Re s < (1+β)/2 < 1. ✓.
3. **Sin otros ceros en D.** r es estrictamente menor que la distancia al cero más próximo
   distinto de ρ₀ (factor ½): D̄∖{ρ₀} no contiene ceros, ni on-line (excluidos por 2) ni
   off (excluidos por la distancia). Si dos cuádruplos estuvieran muy juntos, la distancia
   los registra y r se achica — finitos, sin degeneración. ✓.
4. **η = min_{∂D}|ζ| > 0.** ∂D es compacto y libre de ceros por 3. ✓.
5. **Orden de las elecciones, sin circularidad.** Bajo H(m) la configuración
   {(δ_j,γ_j)}_{j≤m} es un dato fijo del mundo hipotético; ρ₀, r, η son funciones de ese
   dato, elegidas ANTES de invocar LP-112; LP-112 está cuantificado universalmente sobre
   discos, así que aplicarlo al D dependiente de la configuración es legítimo. El punto que
   D112 subraya ("F1: constantes congeladas") es exactamente correcto: la finitud convierte
   δ_min, γ_max, r, η en números, no en parámetros que exijan uniformidad. ✓.

**Dictamen línea 1: sin grieta.** La aritmética |Re s − ½| ≥ δ − r ≥ δ/2 > 0 es correcta tal
como está escrita.

## 2. Línea 2 — Rouché y la réplica off-crítica: VERIFICADO, con UNA falla de enunciado en LP-112⁻

**Rouché.** En ∂D: |ζ(s+iτ) − ζ(s)| < η/2 < η ≤ |ζ(s)| — desigualdad ESTRICTA en todo el
contorno, como Rouché exige. Conclusión: ζ(·+iτ) y ζ tienen el mismo número de ceros
(con multiplicidad) en el interior de D; ζ tiene ≥ 1 (ρ₀); luego existe z* interior con
ζ(z*+iτ) = 0. ✓.

**Off-criticidad.** Re(z*+iτ) = Re z* ∈ (β−r, β+r) ⊂ (½+δ/2, 1). ✓.

**Novedad.** Im(z*+iτ) > γ₀ + τ − r; con τ > γ_max + γ₀ + r + 1 esto excede γ_max, así que
el cero no pertenece a la lista de 4m y su cuádruplo es el (m+1)-ésimo (un cuádruplo tiene
exactamente UN miembro con Re > ½ e Im > 0, de modo que dos ceros distintos de ese tipo
generan cuádruplos distintos). ✓ — contradicción con "exactamente m". ✓.

**LA FALLA (reparable): el umbral de LP-112⁻ no alcanza tal como está enunciado.**
LP-112⁻ (D112, §2.2) dice: "para todo D y todo ε > 0 existe UN τ > altura(D)". Pero la
prueba lo aplica "con τ > γ_max + γ₀ + r + 1". Si altura(D) = γ₀ + r y γ_max > γ₀ (el cero
elegido no es el más alto), el τ que LP-112⁻ garantiza puede caer en
(γ₀+r, γ_max+γ₀+r+1] y la réplica podría aterrizar sobre un cero off-crítico YA listado:
sin contradicción. Tal como están escritos los dos enunciados, el paso "Aplíquese LP-112⁻
... con τ > γ_max + γ₀ + r + 1" usa más de lo que la hipótesis da. Dos reparaciones, ambas
de una línea:

- **(R1) Reparar el lema:** LP-112⁻ debe decir "para todo D, todo ε > 0 y todo T₀ existe
  τ > T₀ con sup_D |ζ(s+iτ)−ζ(s)| < ε". Esta es la forma natural, sigue igual de implicada
  por LP-112 completo (τ_k → ∞), y es la que la prueba realmente usa.
- **(R2) Reparar la prueba:** elegir ρ₀ con γ₀ = γ_max (el cero off-crítico MÁS ALTO, que
  existe por finitud). Entonces Im(z*+iτ) > γ₀ + τ − r > 2γ_max > γ_max para todo
  τ > γ_max + r = altura(D), y el enunciado actual de LP-112⁻ basta literalmente.

Con LP-112 completo (sucesión τ_k → ∞) no hay falla alguna: los τ_k superan eventualmente
cualquier umbral. La falla afecta SOLO a la variante débil tal como está redactada. P44
(sketch, líneas 158–165 de main.tex) usa LP-112 completo y dice "τ_k eventually exceeds
2γ_max" — correcto dado τ_k → ∞ (y de hecho basta superar γ_max + γ₀ + r).

**Dictamen línea 2: el mecanismo es correcto; el enunciado de LP-112⁻ debe corregirse por
(R1) o la prueba por (R2).**

## 3. Línea 3 — La iteración: VERIFICADO

- **Un solo τ ya contradice.** H(m) dice EXACTAMENTE m; un cuádruplo nuevo da m+1 > m:
  contradicción inmediata. La prueba lo dice bien (F4 del §1.2 y el cuerpo del Thm. 2.3);
  la iteración es solo la forma directa "m ≥ 1 ⟹ m = ∞".
- **Separación de réplicas en la forma iterada.** Para que las réplicas sean distintas
  basta τ_{k+1} − τ_k > 2r; como τ_k → ∞, extraer la subsucesión es trivial y la prueba lo
  registra ("tomando τ_k con separaciones > 2r"). ✓.
- Las réplicas distintas con Re > ½, Im > 0 generan cuádruplos distintos (un miembro de ese
  tipo por cuádruplo). ✓.

**Dictamen línea 3: sin grieta.**

## 4. Línea 4 (la central) — Prop. 2.6: ¿densidad cero o VACUIDAD?

### 4.1. La prueba de la Prop. 2.6, línea por línea

1. **Teorema límite de Bagchi.** Q_T(·) = T⁻¹·meas{τ∈[0,T] : ζ(·+iτ)|_{D′} ∈ ·} converge
   débilmente en H(D′) (topología compacto-abierta) a la ley Q del producto de Euler
   aleatorio. Incondicional; [Bag81], [Lau96, Cap. 5]. El polo de ζ no toca: D′ ⊂ {Re < 1}.
   ✓ VERIFICADO contra la literatura citada (consistente con Doc 102 §2.3 y el survey de
   Matsumoto que D102 usó como fuente).
2. **Soporte.** S = {f ∈ H(D′) : f ≠ 0 en D′} ∪ {0} ([Lau96, Cap. 6]; consecuencia de
   Hurwitz sobre límites de productos de Euler no nulos). ✓ estándar.
3. **C_ε es cerrado.** f ↦ sup_{D̄(ρ₀,r)}|f − ζ| es continua en compacto-abierta (el sup es
   sobre un compacto ⊂ D′) y C_ε = preimagen de [0,ε]. ✓.
4. **C_ε ∩ S = ∅ para ε < η.** Si f ∈ C_ε: en |s−ρ₀| = r, |f−ζ| ≤ ε < η = min|ζ|
   (desigualdad estricta), Rouché da a f un cero en D(ρ₀,r) ⊂ D′, luego f ∉ S salvo f ≡ 0;
   y f ≡ 0 daría sup_{D̄}|ζ| ≤ ε < η ≤ sup_{∂D}|ζ|, absurdo. ✓.
5. **Q(C_ε) = 0.** C_ε cerrado ⊂ (supp Q)^c, que es Q-nulo (definición de soporte en
   espacio polaco; H(D′) es separable metrizable). ✓.
6. **Portmanteau.** Para cerrados, limsup_T Q_T(C_ε) ≤ Q(C_ε) = 0; y
   meas(A_ε∩[0,T])/T = Q_T(C_ε) porque τ ∈ A_ε ⟺ ζ(·+iτ)|_{D′} ∈ C_ε. ✓.

**Conclusión técnica: la Prop. 2.6 prueba DENSIDAD SUPERIOR CERO y NADA MÁS.** La razón es
estructural, no de pereza: la convergencia débil de medidas es categóricamente incapaz de
detectar vacuidad — un conjunto de medida límite nula puede ser visitado por cada Q_T en un
conjunto de τ de medida positiva-pero-o(T), o en un conjunto numerable, o en ninguno; el
aparato de Bagchi+Portmanteau no distingue esos casos. **La Prop. 2.6 NO prueba vacuidad,
y ninguna mejora de la misma maquinaria podría probarla.**

### 4.2. PERO: la vacuidad bajo H(m) es teorema de todos modos — por el PROPIO Thm. 2.3

Aquí está el hallazgo conceptual de esta auditoría, y hay que decirlo con precisión porque
los tres documentos lo dicen MAL:

"LP-112⁻(D,ε,T₀) ⟹ ¬H(m)" es lógicamente equivalente, por contraposición, a
"H(m) ⟹ A_ε ∩ (T₀,∞) = ∅" (con ε = η/2 y T₀ el umbral de altura). Es decir: **en el mundo
H(m), el conjunto de testigos por encima del umbral no es "de densidad cero y vacuidad
desconocida" — es VACÍO, con certeza, por el propio Teorema 2.3.** Cada elemento suyo
produciría el cuádruplo m+1 y H(m) dice exactamente m.

Por tanto:

- La tabla de D112 §6.1 ("bajo ¬RH ese conjunto es: densidad 0, vacuidad DESCONOCIDA") y la
  frase de D113 §0 ("sus testigos forman un conjunto de densidad superior cero cuya vacuidad
  es desconocida") son **imprecisas**: confunden las dos ramas de ¬RH. Bajo 0 < m < ∞ la
  vacuidad (sobre el umbral) es TEOREMA; lo desconocido es la rama m = ∞, donde la Prop. 2.6
  también da densidad cero pero nada fuerza vacuidad. La redacción correcta: "bajo H(m) el
  conjunto es vacío sobre el umbral (contraposición del Thm. 2.3); bajo m = ∞ tiene densidad
  cero y vacuidad desconocida; la no-vacuidad EN EL MUNDO REAL es exactamente lo que LP-112
  pide".
- En particular, "exhibir un τ ∈ A_ε" no es un paso intermedio hacia refutar H(m): **ES
  refutar H(m)** — el mismo acto, en otra coordenada. El Doc 112 lo sabe a medias (lo llama
  "el cuantificador maestro en coordenadas de casi-períodos") pero el vocabulario de
  "densidad cero pero quizá no vacío bajo la hipótesis a refutar" sugiere un espacio lógico
  que no existe.

### 4.3. ¿Esto vacua el Teorema 2.3? NO — y la distinción es la clave de toda la auditoría

La pregunta del encargo: si bajo 0 < m < ∞ la hipótesis LP-112 es falsa, ¿el teorema es
"falso ⟹ cualquier cosa", vacuo, y P44 colapsa?

**No.** Hay que distinguir dos vacuidades:

- **Vacuidad relativa (inocua, universal):** en el mundo hipotético H(m), LP-112 es falso.
  Esto es cierto — por contraposición del propio teorema — y es la estructura de TODA
  reducción al absurdo: si "A ∧ B ⟹ ⊥" es teorema, entonces en todo mundo-B, A es falso.
  El teorema de Bagchi tiene exactamente la misma propiedad (bajo ¬RH la recurrencia fuerte
  es falsa) y nadie lo llama vacuo. La conclusión utilizable es la contrapositiva en el
  mundo REAL: quien pruebe LP-112 incondicionalmente habrá probado m ∈ {0,∞}.
- **Vacuidad absoluta (letal, NO ocurre):** LP-112 demostrablemente falso a secas. Eso sí
  mataría la arquitectura. No es el caso: RH ⟹ LP-112 (Bagchi, mitad difícil: bajo RH,
  ζ|_D no se anula, pertenece al soporte, los τ buenos tienen densidad inferior positiva),
  y RH no está refutada; además LP-112 es consistente con m = ∞ (el argumento de Rouché
  ahí solo produce más ceros de los infinitos que ya hay — sin contradicción, Prop. 2.7).
  LP-112 es exactamente tan refutable como RH: no más.

**RESPUESTA A LA PREGUNTA CENTRAL DEL ENCARGO: densidad cero, no vacuidad — en lo que
respecta a la Prop. 2.6, cuya prueba es correcta y estructuralmente incapaz de dar más.
La vacuidad bajo H(m) (sobre el umbral) vale de todos modos, gratis, por contraposición
del Thm. 2.3 — y es inocua: vacuidad relativa al mundo hipotético, no vacuidad del
condicional. El Teorema 2.3 NO es vacuo. La arquitectura de P44 no colapsa por aquí.**

Lo que SÍ exige este hallazgo: reescribir las frases de "vacuidad desconocida" (D112 §0.2,
§6.1 tabla, §7 gap; D113 §0 y §1.1) separando ramas, y reconocer en P44 que el contenido
real de la Prop. 2.6 vive en (i) la rama m = ∞ y (ii) la explicación de por qué ninguna
maquinaria de promedios puede probar LP-112 — no en la rama 0 < m < ∞, donde la
contraposición del teorema la supera trivialmente.

## 5. Línea 5 — ¿La no-equivalencia LP-112 ≠ RH es PROBADA o NO-REFUTADA?

**NO-REFUTADA. No probada — y, en el sentido material, IMPROBABLE DE PROBAR jamás.**

1. **El argumento real de D112 §5.4(2):** LP-112 no implica RH "por la vía de densidades"
   (su conclusión bajo ¬RH es m = ∞, consistente con Bohr–Landau; una sucesión de densidad
   cero no activa ningún amplificador contra N(σ,T) = o(T)). Eso es correcto y muestra
   exactamente lo que dice: que el ÚNICO diccionario conocido (densidad de réplicas contra
   teoremas de densidad) no convierte LP-112 en RH. El propio D112 lo declara: "una
   implicación por vía desconocida no puede excluirse — GAP menor declarado". **Esa frase es
   la verdad completa.**
2. **Observación que los documentos no hacen y deberían:** como enunciados cerrados sobre ζ,
   si RH es verdadera entonces LP-112 y RH son AMBAS verdaderas y por tanto materialmente
   equivalentes; "no-equivalencia" solo puede significar "no existe derivación conocida de
   RH desde LP-112" — un enunciado META-matemático sobre el estado de las pruebas, no un
   teorema sobre ζ. Probar la no-equivalencia material exigiría exhibir consistencia de
   LP-112 ∧ ¬RH (la rama m = ∞ con auto-aproximación), que está fuera de todo alcance.
   Más aún: nada excluye hoy que LP-112 sea materialmente equivalente a RH — que en la rama
   m = ∞ los testigos también falten (la Prop. 2.6 aplica verbatim ahí: densidad cero
   alrededor de cualquier cero off-crítico). El estatus honesto es: **LP-112 está implicado
   por RH, implica la dicotomía, y no se conoce ni implicación inversa ni obstrucción a
   ella.**
3. **Dónde sobreclama cada documento:**
   - D112 §0.3: "la razón por la que LP-112 queda vivo como objetivo no-RH-equivalente" —
     sobreclama (cae el "por los diccionarios conocidos").
   - D112 §7.3: "LP-112 queda vivo, no RH-equivalente" y §7 "certificado de no-equivalencia
     con RH" — **"certificado" es falso**: lo certificado es la no-equivalencia POR
     DENSIDADES, no la no-equivalencia.
   - D112 §5.4 cuerpo: correcto y honesto (hedge explícito + GAP declarado). El cuerpo y los
     titulares del mismo documento no dicen lo mismo; los titulares deben bajar al cuerpo.
   - D113: el cuerpo es honesto ("no ⟹ RH por diccionarios conocidos", tabla §7); el
     resumen §0.4 ("LP-113 no es RH-equivalente por los diccionarios conocidos, pero...")
     mantiene el hedge — aceptable.
   - **P44, §2.4 (línea 196 de main.tex): el título de sección es "LP-112 is not
     RH-equivalent" — sobreclamo en titular.** El cuerpo (líneas 142–144, 197–203) sí dice
     "as far as every known dictionary reaches" y "no known dictionary upgrades it to RH" —
     honesto. **Corrección requerida: retitular** ("LP-112 is not known to be
     RH-equivalent" o "No known dictionary upgrades LP-112 to RH") y revisar la línea 104
     ("strictly weaker than every previously identified sufficient condition" — "strictly
     weaker" solo está probado contra la recurrencia fuerte EN FORMA DE ENUNCIADO, sucesión
     vs densidad; la fuerza lógica estricta no está probada: si ambas resultaran
     equivalentes a RH la "estrictez" colapsaría).
4. **¿Circularidad oculta en la arquitectura?** No hay circularidad LÓGICA: RH ⟸ L8 ∧
   LP-112 es un condicional probado y usar la arquitectura exige probar LP-112 sin asumir
   nada sobre los ceros — un enunciado de auto-aproximación, sintácticamente independiente
   de la posición de los ceros. El riesgo es ESTRATÉGICO, no lógico, y D113 lo documenta
   con franqueza brutal: no hay precedente, no hay técnica, toda la maquinaria conocida
   produce genéricos y el testigo requerido es excepcional; en el peor mundo (que nadie
   puede excluir) probar LP-112 es exactamente tan difícil como RH. La arquitectura es
   honesta SI Y SOLO SI se presenta como apuesta: "el target es más débil como enunciado;
   no sabemos si es más débil como problema". P44 debe decir esa segunda mitad explícita.

**RESPUESTA A LA LÍNEA 5: no-equivalencia NO-REFUTADA, no probada; el lenguaje de los
titulares de D112 y del título de §2.4 de P44 debe degradarse al del cuerpo de D112 §5.4,
que ya es correcto.**

## 6. Línea 6 — Cuantificadores: P44 enuncia la forma FUERTE, Doc 112 la DÉBIL

- **Doc 112, §2.2 (oficial):** "Para todo disco cerrado D ⊂ {½<σ<1} existe una sucesión
  τ_k → ∞ tal que sup_D |ζ(s+iτ_k)−ζ(s)| → 0" — **∀D ∃sucesión (débil).**
- **Doc 113, §0 (resumen):** "existe una sucesión τ_k → ∞ tal que ζ(s+iτ_k) → ζ(s)
  uniformemente en cada disco compacto" — **∃sucesión ∀D (fuerte).** (Su §1.1 luego copia
  la débil de D112: inconsistencia interna de D113.)
- **P44, Definition def:lp112 (líneas 133–137):** "There exists a sequence τ_k → ∞ such
  that ζ(s+iτ_k) → ζ(s) uniformly on every compact disk" — **fuerte.**

Las dos formas NO son trivialmente equivalentes. Fuerte ⟹ débil, obvio. Débil ⟹ fuerte
NO se sigue por diagonal directa: la franja no se agota por una cadena creciente de DISCOS
(todo disco de la franja tiene diámetro menor que el ancho de la franja), y la débil da
sucesiones distintas para discos distintos sin testigo común — para fabricar un τ bueno
para D₁,…,D_n simultáneamente haría falta la versión con compactos arbitrarios (rectángulos)
o densidad positiva, que es justo lo que LP-112 evita pedir. (Bajo RH ambas valen: Bagchi da
densidad positiva por compacto con complemento conexo — rectángulos crecientes — y la
diagonal cierra. Incondicionalmente, débil y fuerte deben tratarse como enunciados
distintos.)

**Consecuencia para la corrección:** la prueba del Thm. 2.3 usa UN solo disco — la débil
basta. P44 asume la fuerte y por tanto su teorema vale a fortiori (sin error lógico), pero
enuncia como hipótesis-target algo más fuerte de lo necesario. **Corrección a favor del
programa: P44 debe enunciar la débil** ("for every compact disk D there exists a sequence…"),
que es (a) lo que la prueba usa, (b) lo que D112 enuncia, (c) el target más fácil. Y D113 §0
debe alinearse con su propio §1.1.

## 7. Ataques adicionales del auditor (fuera del mínimo obligatorio)

1. **¿El teorema límite de Bagchi vale en el disco D′ elegido?** Sí: D′ compacto-cerrado
   dentro de la franja, sin tocar el polo (Re < 1); [Lau96] lo da para regiones acotadas con
   clausura en la franja. Sin grieta.
2. **¿Portmanteau requiere algo de A_ε que falte?** No: A_ε es exactamente la preimagen de
   C_ε bajo τ ↦ ζ(·+iτ)|_{D′}, medible (continua en τ), y la identidad
   Q_T(C_ε) = meas(A_ε∩[0,T])/T es por definición. Sin grieta.
3. **¿La Prop. 2.6 usa η del Thm. 2.3 de forma circular?** No: η depende solo de la
   configuración H(m), fijada antes; ε < η es una restricción legítima del enunciado.
4. **¿El caso f ≡ 0 del soporte está bien excluido?** Sí (paso 4 de §4.1 supra); es el único
   punto donde se necesita que ζ no sea minúscula en TODO el disco, y el contorno lo da.
5. **¿"m ≥ 1 ⟹ m = ∞" requiere algo más cuando m = ∞ de partida?** No: vacuamente cierto;
   la forma con contenido es la contradicción bajo m finito, que es la probada.
6. **Consistencia D112↔P44 en el sketch:** P44 dice "new, since τ_k eventually exceeds
   2γ_max" — con γ₀ ≤ γ_max y r < ¼ se necesita τ_k > γ_max + γ₀ + r, y 2γ_max lo cubre
   solo si γ₀ + r ≤ γ_max, cierto salvo cuando γ₀ = γ_max y entonces falta el +r; como
   τ_k → ∞, irrelevante — pero el sketch ganaría escribiendo el umbral correcto
   γ_max + γ₀ + r de D112.

## 8. VEREDICTO

**SOBREVIVE CON CORRECCIONES.** El Teorema 2.3 del Doc 112 es correcto en su mecanismo
(elecciones de constantes, Rouché, off-criticidad, novedad, iteración: verificados línea
por línea) y la Proposición 2.6 es correcta en su prueba y en su alcance declarado
(densidad superior cero). El resultado NO está refutado y la arquitectura de P44 NO
colapsa. Correcciones exigidas, en orden de importancia:

1. **(Enunciado, real) LP-112⁻:** añadir el umbral arbitrario ("para todo D, ε y T₀ existe
   τ > T₀…") — reparación (R1) — o cambiar la prueba para elegir ρ₀ con γ₀ = γ_max —
   reparación (R2). Tal como está, la prueba invoca un umbral que el lema débil no provee.
   (§2 supra. Con LP-112 completo no hay falla.)
2. **(Lenguaje lógico, repetido) "Vacuidad desconocida":** bajo H(m) la vacuidad de A_{η/2}
   sobre el umbral es teorema (contraposición del propio Thm. 2.3), no incógnita; lo
   desconocido es la rama m = ∞ y la no-vacuidad en el mundo real. Corregir D112 §0.2,
   §6.1 (tabla), §7; D113 §0 y §1.1. Aclarar en P44 que "certificar un testigo" y "refutar
   H(m)" son el mismo acto. El teorema NO es vacuo: la falsedad de LP-112 es relativa al
   mundo hipotético (estructura de toda reducción al absurdo), no absoluta — RH ⟹ LP-112
   y LP-112 es consistente con m = ∞.
3. **(Sobreclamo) No-equivalencia con RH:** es NO-REFUTADA, no probada (y la versión
   material es indemostrable mientras RH siga abierta). Degradar: D112 §0.3 y §7
   ("certificado de no-equivalencia" → "no-equivalencia por los diccionarios conocidos");
   P44 título de §2.4 ("is not RH-equivalent" → "is not known to be RH-equivalent") y
   línea 104 ("strictly weaker" → calificar como fuerza de enunciado, no de problema).
4. **(Descalce de cuantificadores) P44 Definition def:lp112 y D113 §0** enuncian la forma
   fuerte (∃sucesión ∀disco); D112 y la prueba usan la débil (∀disco ∃sucesión), que no es
   trivialmente equivalente (la franja no se agota por discos). Enunciar la débil en P44 —
   corrección a favor: target más fácil, y es lo que el teorema necesita.
5. **(Cosmético) Sketch de P44:** umbral de novedad γ_max + γ₀ + r en lugar de "2γ_max".

**Respuestas a las dos preguntas centrales del encargo:** (línea 4) la Prop. 2.6 prueba
densidad cero y solo densidad cero — su maquinaria (convergencia débil + Portmanteau) es
estructuralmente incapaz de probar vacuidad; la vacuidad bajo H(m) vale igualmente por
contraposición del propio teorema y es INOCUA (vacuidad relativa, no absoluta): el
Teorema 2.3 no es vacuo y P44 no colapsa. (línea 5) la no-equivalencia LP-112/RH es
no-refutada, no probada; el cuerpo de D112 §5.4 ya lo dice bien y los titulares de D112 y
P44 deben bajar a ese lenguaje.

---

## Referencias

**Internas:** Doc 112 (§§0–7, objeto de la auditoría); Doc 113 (§§0–8); Doc 102 (Bagchi);
Doc 104 (ventana anclada); Doc 109 (identidad RH = (m<∞) ∧ D-109); Doc 111 (cosh-ejemplos);
P43 (cuantificador maestro); P44 (`06-papers/P44-two-lemma-architecture/main.tex`,
líneas 95–203 verificadas en fuente para esta auditoría).

**Literatura (todas ya citadas y verificadas en D112/D113; usadas aquí sin adición):**
B. Bagchi, tesis ISI 1981; B. Bagchi, *Recurrence in topological dynamics and the Riemann
hypothesis*, Acta Math. Hungar. 50 (1987) 227–240; A. Laurinčikas, *Limit Theorems for the
Riemann Zeta-Function*, Kluwer 1996, Caps. 5–6 (teorema límite y soporte); E. C. Titchmarsh,
*The Theory of the Riemann Zeta-Function*, 2.ª ed. 1986 (Thm. 7.2, Cap. VIII); H. Bohr y
E. Landau, Rend. Circ. Mat. Palermo 37 (1914); H. Davenport y H. Heilbronn, J. London Math.
Soc. 11 (1936). Para Portmanteau y soporte en espacios polacos: P. Billingsley, *Convergence
of Probability Measures*, 2.ª ed., Wiley 1999, Thm. 2.1 (forma estándar del teorema de
Portmanteau para cerrados).

*Fin del Documento 115.*
