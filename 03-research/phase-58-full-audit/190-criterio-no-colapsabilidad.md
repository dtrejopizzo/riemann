# Documento 190 — El criterio de no-colapsabilidad A↔B: ¿existe un objeto que produzca simultáneamente μ₂ e I?

**Programa:** Hipótesis de Riemann — Fase 58 (auditoría total)
**Fecha:** 2026-06-11
**Mandato del director (formalizado aquí):** RH se separa en dos demandas — **A** (segundo momento espectral: un funcional que distinga las fluctuaciones finas μ₂, lo que exige anisotropía, sensibilidad de signo y resolución de correlación) y **B/Dic** (pureza del estado: eliminación completa de los estados interiores 0<I<∞, lo que exige coercividad global y cierre dinámico). Hecho implícito a examinar: *no puede tenerse simultáneamente un sistema cerrado por coercividad y un sistema que reconstruya correlaciones de segundo orden exactas, porque la coercividad destruye exactamente la información que μ₂ necesita.* Test crítico: ¿existe algún objeto del sistema que produzca simultáneamente μ₂ e I sin pérdida de información? Si existe, RH es potencialmente cerrable en este marco; si no existe, el sistema está estructuralmente incompleto para RH.
**Prerrequisitos (no re-derivados):** clasificación estructural de la auditoría (D184–D188); [Thm 173.C] (Green–Littlewood); [Thm 170.5] (E(T)≪T/log T); [LEMA 180.1] (E=(T/log T)μ₂); barreras 176.9 / 180.3-condicional / 172.9; ley de balance İ=−2κ−D (D167/168, certificada); dicotomía de Hadamard en la clase (D174 §3.3, intacta tras E-186); [Cor 181.3] (condicional a A, LP-112 ⟺ RH); D64 (T_λ=0 ∀λ ⟺ RH); D152 (espectro de impureza); Rodgers–Tao 2020 (Λ≥0); Bagchi (universalidad/recurrencia).
**Contrato:** [TEOREMA]/[PROP] solo con prueba completa; **el alcance de los cuantificadores es sagrado** — todo no-go de este documento es sobre el repertorio examinado, NO universal; sin numérica.

**Coordenadas (autocontenidas, idénticas a D170/173/176/180).** Ceros off de ζ: ρ=β+iγ, β>½, b=β−½∈(0,½), un representante por cuádruplo. I(0⁺)=Σb² (la energía de inestabilidad). E(T)=Σ_{γ≤T}b². μ₂(T)=(log T/T)E(T) (desplazamiento cuadrático medio microscópico, D180). **A** ⟺ I<∞ ⟺ E(T)=O(1). **Dic** ⟺ I∈{0,∞}. **B** ⟺ (I<∞ ⟹ I=0) ⟺ Dic. **RH ⟺ A ∧ Dic.** Hechos auditados firmes que esta sesión usa como axiomas internos: (i) İ=−2κ−D es ζ-LIBRE (vale en toda la clase de Pólya; solo I(0) porta ζ); (ii) existe la configuración de Hadamard en la clase con 0<I<∞ (Dic es FALSA en la clase; toda prueba de Dic requiere aritmética ζ-específica); (iii) A ⟹ Lindelöf (176.7, certificado); (iv) condicional a A, LP-112 ⟺ RH (181.3, certificado); (v) las barreras de A post-auditoría: 1 teorema (176.9), 1 condicional-a-Farmer (180.3, → rendija R1), 1 principio (ceguera de signo 180.4), 1 corolario (población, D183 corregido); rendijas vivas R1 (molificador no-estándar) y R2 (flujo de borde anisótropo).

---

## 0. Resumen ejecutivo

1. **[DEF 190.1]** se formaliza el "objeto colapsador": Φ debe satisfacer (a) recuperación de I, (b) recuperación de μ₂(T) para todo T, (c) accesibilidad incondicional. El multiconjunto de ceros se excluye como colapsador trivial: satisface (a)+(b) por definición y falla (c) por definición.
2. **Examen de los seis candidatos del repertorio** (Weil Q, balance İ, impureza D152, Green–Littlewood 173.C, flujo DBN {H_t}, momentos T_λ): **ninguno satisface (a)∧(b)∧(c)**. Cada veredicto identifica la condición que falla y la pieza auditada que lo prueba.
3. **[PROP 190.2 — tricotomía del repertorio]:** todo objeto Φ del repertorio examinado cae en exactamente una de tres clases: **(ζ-libre: pierde I(0))** ∪ **(promediado-incondicional: pierde μ₂)** ∪ **(exacto-no-accesible: evaluarlo equivale a RH o a un problema RH-difícil)**. La intersección de las tres demandas es vacía **en el repertorio**. Esto NO es un no-go universal.
4. **Respuesta binaria al director: el sistema actual es estructuralmente incompleto para RH** — no hay colapsador en el repertorio, y el mecanismo de exclusión es el que el director conjeturó (la coercividad/promediación destruye la información de segundo orden), con una precisión: la destrucción opera por DOS vías distintas (ζ-libertad para el lado coercivo, isotropía/promedio para el lado correlacional), no por una sola.
5. **[GAP-190.A]** especificación precisa del objeto externo que cerraría el marco (el "objeto Connes/Deninger" de fases previas, ahora con tres propiedades simultáneas nombradas). R2, si rindiera, sería colapsador *parcial de primer orden* — no resuelve μ₂ pero sería el primer funcional anisótropo accesible del programa.

---

## 1. [DEFINICIÓN 190.1] Objeto colapsador

Sea 𝔄 el repertorio de objetos construibles del programa: funcionales, operadores, medidas y flujos definidos a partir de ζ, de su flujo De Bruijn–Newman {H_t}, o de sus ceros, mediante las maquinarias del programa (forma de Weil, fórmula explícita, lema de Littlewood, momentos, densidades, polinomios C_λ/T_λ).

**Φ ∈ 𝔄 es un COLAPSADOR si satisface simultáneamente:**

- **(a) Producción de I (el dato coercivo/global).** Existe una operación determinista R_I con R_I(Φ)=I(0⁺). En particular Φ distingue I=0 de 0<I<∞ de I=∞: Φ porta la información de Dic.
- **(b) Producción de μ₂ (el perfil correlacional/local).** Existe R_μ con R_μ(Φ)(T)=μ₂(T) para todo T. En particular Φ resuelve el segundo orden transversal a escala microscópica u=b·log T≍1: Φ porta la información de A *con perfil*, no solo el valor límite.
- **(c) Accesibilidad (control incondicional).** Alguna norma, traza o momento de Φ es acotable **incondicionalmente** por la maquinaria conocida (momentos de ζ, teoremas de densidad, fórmula explícita con tests integrables, monotonía/balance del flujo DBN) a una escala comparable o inferior a la señal que (a) y (b) requieren leer. Formalmente: la evaluación de R_I(Φ) y R_μ(Φ) no debe requerir, como input, un enunciado equivalente a A, a Dic o a RH.

**Exclusión del colapsador trivial.** El multiconjunto Z={ρ} de los ceros satisface (a) y (b) tautológicamente (I y μ₂ son funciones de Z) y falla (c) tautológicamente: ninguna maquinaria incondicional evalúa b_j individual (el cuantificador maestro del programa, Phase 49: todo acceso incondicional a Z pasa por sumas Σg(γ) con g de la clase admisible, y la clase admisible promedia). La condición (c) es exactamente lo que separa "el objeto existe" de "el objeto sirve".

**La tensión que el mandato pide formalizar.** Accesibilidad ⟹ la evaluación es un promedio (fórmula explícita con test integrable, momento en T, traza) ⟹ pérdida de lo individual. Esto es el cuantificador maestro (media→uniforme, valor→inercia; Phase 49, D154–157) en versión segundo orden. La pregunta de este documento es si algún objeto del repertorio escapa: si la pérdida del promedio puede compensarse con estructura (anisotropía, signo, exactitud).

**Observación de calibre (por qué (a)∧(b) ya es casi RH-completo).** Si Φ satisface (a) y (b) con R_I, R_μ evaluables, entonces RH ⟺ (R_I(Φ)=0). Un colapsador no es un paso hacia RH: es un *reempaquetado completo* de RH con asa incondicional. Por eso la pregunta del director es la correcta forma del test estructural: no "¿podemos probar RH?" sino "¿el marco contiene siquiera un objeto cuya asa permita agarrarlo?".

---

## 2. Los seis candidatos del repertorio, uno por uno

### 2.1. La forma de Weil Q/W — falla (c); (a) solo en forma de índice

Q produce I indirectamente: κ=neg.ind(Q)=2m (Phase 26) cuenta los ceros off, y el Hessiano transversal lee b². Pero la evaluación de la positividad de Q **es** el criterio de Weil: RH ⟺ Q≥0. Aquí (c) falla en su forma más pura: la "norma controlable" de Q en la dirección que importa (el cono de tests) es exactamente la conclusión. Phase 53 lo dijo en lenguaje de Krein: definitizar (K,Q) ≡ κ=0 ≡ RH. Además (b) falla parcialmente: Q a través de tests integrables es isótropa en b a primer orden (no-go 141.B2: el primer orden integra a cero); el segundo orden existe en Q (el Hessiano) pero su extracción requiere tests localizados que la fórmula explícita no controla incondicionalmente (GAP-141.G1). **Veredicto: exacto-no-accesible — colapsador ⟺ conclusión.**

### 2.2. La ley de balance İ=−2κ−D — falla (a) por ζ-libertad

La ley es coerciva, certificada y ζ-LIBRE (D167/168): vale para toda la clase de Pólya. Por la configuración de Hadamard (D174 §3.3, intacta tras la auditoría E-186), existe en la clase un elemento con 0<I<∞ que satisface TODAS las leyes dinámicas probadas (balance, coercividad İ≤−2I, presupuesto de vidas, jerarquía de momentos en sus extremos certificados n=1,∞). Conclusión formal: **ningún funcional construido solo con la ley de balance determina I(0)** — dos condiciones iniciales de la clase con I(0) distintos satisfacen las mismas leyes. La ley pierde exactamente el dato que (a) pide; pierde también (b) (μ₂ es un perfil en T de la condición inicial, invisible para una ley de evolución). Esto es la mitad coerciva de la conjetura del director, probada: **el cierre dinámico se compró al precio de la ζ-libertad, y la ζ-libertad es la pérdida total del dato de estado.** Veredicto: **ζ-libre — pierde I(0).**

### 2.3. El espectro de impureza D152 / ventanas de segundo orden — falla (b)→(c) por ruido

Es el único candidato diseñado para μ₂: la ventana de segundo orden produce señal Θ(c²) por cero off. Pero el ruido por ventana es Θ(1) (S(t) domina, H1 muerta en cualquier mundo, D170/171), el colapso sobre E está probado (D172: el momento clavado ≡2/3 es ciego a los ceros; ceguera exacta de Poisson), y el techo 172.9 establece que ni con correlación de pares + G1 entero se supera E≪T/log T por ventanas. Es decir: D152 satisface una versión *promediada* de (b) — recupera E(T) hasta la precisión de Selberg y ni un log más — y esa precisión es exactamente μ₂≪1, no μ₂=o(1). No produce I (la suma total diverge del control por ventanas: no-go 170.8). Veredicto: **promediado-incondicional — pierde μ₂ (la resolución muere en el suelo de ruido, GAP-141.G1).**

### 2.4. La identidad Green–Littlewood 173.C — satisface (a) y (b) formalmente, falla (c): cambio de moneda

Φ = la medida de Riesz de log|ζ| (equivalentemente D(T)=∬log|ζ|). Por [Thm 173.C], I es su segundo momento transversal **exacto**; por el layer-cake 176.8 y 180.1, μ₂(T) también se recupera exactamente. Es el candidato más cercano a colapsador: (a)✓, (b)✓ sin pérdida (la identidad es exacta, certificada en D185). Pero (c) falla por [PROP 180.4] (ceguera de signo, auditada): toda evaluación incondicional de ∬log|ζ| por momentos es ciega al signo, la parte positiva sola vale ≫T√(log log T)/log T en la franja microscópica, y la cancelación de signo en t está codificada EXACTAMENTE en los ceros (Littlewood es identidad, no desigualdad: no hay tercer término). Evaluar Φ mejor que T/log T ⟺ contar ceros mejor que Selberg ⟺ el problema original. **Veredicto: exacto-no-accesible — otra moneda, mismo precio.** Este caso es el más instructivo: muestra que la exactitud no compra accesibilidad, porque la identidad transporta también la dureza.

### 2.5. El flujo DBN completo {H_t} — colapsador trivial disfrazado; falla (c)

{H_t}_{t>0} contiene TODA la información (H_0 determina ζ por continuidad; los ceros de H_t para t>0 son reales y computables en principio, y Λ≥0 [Rodgers–Tao 2020] dice que el presente t=0 es el borde exacto de la zona real). Satisface (a) y (b) trivialmente. Pero la información fina de H_t cuando t→0⁺ ES la información de ζ: la velocidad con que los pares complejos aterrizan (las "vidas" ℓ_j, el presupuesto Σℓ≤I/4) es una reparametrización biyectiva de los b_j. Lo accesible incondicionalmente del flujo es: Λ≥0, la ley de balance (ζ-libre, §2.2) y las cotas de gaps lejos de la esquina; la esquina (t→0⁺, donde vive la patología por D177, confinamiento certificado) es exactamente lo no controlado — 177.B es un GAP, y por [Thm 178.10-degradado, D187] su forma plena es cuasi-RH-difícil. **Veredicto: exacto-no-accesible — es Z con coordenada extra t; la condición (c) lo reduce a §2.2 (lo ζ-libre) más §2.1 (lo duro).**

### 2.6. Los momentos C_λ/T_λ (Phase 32, D64) — falla (c): evaluación ⟺ RH

[D64]: T_λ=0 ∀λ ⟺ RH. T_λ produce, por tanto, el bit I=0 (a, parcialmente) y su estructura como forma cuadrática en los c_k (D71) más la traza vía fórmula de Weil (D72: T_λ = A_λ^off − Σ_p(...)B_λ(log p)) lo conecta con el segundo orden. Pero su evaluación es una cancelación aritmética exacta ceros/primos: el lado de los primos es accesible, el lado A_λ^off es la incógnita, y la diferencia solo se controla probando la cancelación — que es RH (la dirección "T_λ accesible ⟹ RH" es el contenido de D64, no un atajo). Además (a) falla en sentido fino: T_λ es sensible al bit (¿hay ceros off?) pero no al valor I (la familia {T_λ} no separa configuraciones off con distinta energía sin resolver la transformada — de nuevo el multiconjunto). **Veredicto: exacto-no-accesible — equivalencia de RH con notación de momentos.**

---

## 3. [PROPOSICIÓN 190.2] El criterio de no-colapsabilidad (tricotomía del repertorio)

**Enunciado.** Sea Φ un objeto del repertorio examinado 𝔄* = {Q/Weil y sus formas equivalentes; leyes y funcionales del flujo DBN construidos con las leyes ζ-libres certificadas; funcionales de ventana/densidad/molificador/momento de las cuatro familias de barreras; identidades integrales del bloque 173/176; momentos C_λ/T_λ}. Entonces Φ cae en al menos una de tres clases, y por tanto NO es colapsador:

1. **(ζ-libre)** Φ es invariante bajo la clase de Pólya ⟹ Φ no determina I(0): falla (a).
2. **(promediado-incondicional)** Φ se evalúa por densidades exponenciales, momentos molificados estándar, ventanas de correlación, o momentos sin signo ⟹ Φ no resuelve μ₂=o(1): falla (b) a la resolución requerida.
3. **(exacto-no-accesible)** Φ determina I y μ₂ exactamente ⟹ toda evaluación de Φ a la escala de la señal equivale a contar ceros a esa escala: falla (c).

**Prueba.** (1) Es la dicotomía de Hadamard, certificada: la configuración de D174 §3.3 (intacta tras E-186) realiza 0<I<∞ dentro de la clase satisfaciendo todas las leyes ζ-libres probadas; dos elementos de la clase con I(0) distintos son indistinguibles para cualquier Φ clase-invariante, luego R_I(Φ) no existe. (2) Es la unión de las barreras auditadas, cada una un resultado probado sobre su familia: [PROP 176.9] (teorema: ninguna densidad exponencial da A — la masa fatal vive en s≍1/log T); [PROP 180.3] (condicional al suelo de Farmer para la clase estándar — de ahí la rendija R1, ver §4); [Thm 172.9] (teorema: techo T/log T por ventanas aun con correlación de pares + G1); [PROP 180.4] (principio probado: los momentos sin signo tienen suelo ≫T√(log log T)/log T, y la cancelación es idénticamente los ceros). En cada familia, la mejor salida es μ₂≪1, y GAP-180.1 pide μ₂=o(1): la resolución falta por un factor que las barreras prohíben recuperar dentro de la familia. (3) Para cada Φ exacto del repertorio el argumento es individual y está en §2: Weil (positividad=conclusión, Krein D164/165), Green–Littlewood (identidad bidireccional 180.4(b): cota⟺ceros, sin tercer término), DBN-fino (la esquina es 177.B, cuasi-RH-difícil por la ida certificada de 178.8), T_λ (D64 es la equivalencia). En los cuatro casos la "evaluación" requerida por (c) es un enunciado del género de la conclusión — verificado pieza a pieza, no por principio general. La cobertura de 𝔄* por las tres clases es por inspección de la lista (finita) de §2 más el cierre bajo las operaciones del programa: combinar objetos de la clase 1 entre sí queda en la clase 1 (la invariancia se preserva); combinar con evaluaciones promediadas hereda la clase 2; insertar el dato exacto cae en la 3. ∎

**ALCANCE — en negrita porque el contrato lo exige.** **Esto NO es un no-go universal. La Proposición 190.2 caracteriza el repertorio EXAMINADO: los objetos efectivamente construidos por el programa y sus combinaciones bajo las operaciones conocidas. No se afirma — ni puede afirmarse con las técnicas de este documento — que no exista ningún funcional matemático que satisfaga (a)∧(b)∧(c). El cuantificador es "para todo Φ∈𝔄*", no "para todo Φ".** La clase de todos los funcionales no es un objeto sobre el que sepamos cuantificar; lo que sí está probado es que los tres mecanismos del repertorio agotan los mecanismos *conocidos* (la exhaustividad de Phase 49 sobre los cinco cruces, más las barreras de Phases 54–58), y que dentro del repertorio la intersección (a)∩(b)∩(c) es vacía.

**[GAP-190.A] — especificación del objeto externo.** El colapsador, si existe, debe tener simultáneamente las tres propiedades que ningún objeto de 𝔄* combina:
1. **ζ-cargado en el estado:** distingue condiciones iniciales dentro de la clase de Pólya (no puede ser una ley de evolución ni un invariante de clase) — debe leer la aritmética de la condición inicial, cuyo único punto de entrada probado son las fluctuaciones de gaps (D174.7).
2. **Anisótropo con signo a escala microscópica:** su acoplamiento a un cero off es ∝b (o b²) con signo coherente, no |·|, resoluble en u=b·log T≍1 — la propiedad que las cuatro familias de barreras no tienen (isotropía, o signo cancelante, o saturación en línea).
3. **Con asa incondicional:** alguna traza/norma suya acotada por debajo de la señal SIN input del género RH/A/Dic — la propiedad que Weil, 173.C, DBN-fino y T_λ no tienen.
Este es el "objeto Connes/Deninger" de Phases 40–43 y 49, ahora con contrato: en lenguaje de aquellas fases, un invariante cohomológico sobre Spec ℤ que lea *inercia* (prop. 1) con *polarización* (prop. 2) y *finitud demostrable* (prop. 3). Las tres a la vez es precisamente lo que la métrica de polarización de Phase 43 no logró (portaba ζ: tenía 1 y 2 pero no 3).

---

## 4. Respuesta al director y consecuencia estratégica

**Respuesta binaria: el sistema actual es estructuralmente incompleto para RH.** No hay colapsador en el repertorio (Prop 190.2, alcance declarado). El hecho implícito del mandato queda examinado y *refinado*: es correcto que coercividad y reconstrucción de segundo orden no coexisten en el repertorio, pero el mecanismo no es uno sino dos. La coercividad del programa es ζ-libre (esa es su fuente de demostrabilidad) y la ζ-libertad — no la coercividad per se — es lo que borra I(0) y μ₂. Simétricamente, la accesibilidad correlacional es promediada (esa es SU fuente de demostrabilidad) y el promedio borra el segundo orden fino. **Lo que se demuestra se demuestra porque olvida; lo que recuerda no se demuestra.** Esa es la forma precisa del cuantificador maestro en esta fase.

**Las rendijas.** R1 (molificadores no-estándar): si rompiera el suelo de Farmer, rompería la barrera 180.3 — pero seguiría dentro de la clase 2 salvo que la familia nueva fuera además anisótropa; mejoraría μ₂≪1 hacia o(1) sin tocar (a): sería progreso en A, no un colapsador. R2 (flujo de borde σ=½): si produjera Σb·log γ incondicional, sería el **primer funcional anisótropo accesible del programa** — pero es primer orden con peso: un *colapsador parcial* que rompe la barrera de isotropía (prop. 2 de GAP-190.A a medias: signo sí, segundo orden no) sin dar μ₂ ni I. No es otra moneda (a diferencia de 173.C, su lado evaluable no sería idénticamente los ceros): es media propiedad nueva. Vale el medio documento que cuesta (D188).

**Implicación estratégica.** Sin colapsador, las dos torres NO son dos rutas independientes: son dos PROYECCIONES del mismo déficit — la torre de energía proyecta el déficit sobre (b)+(c) (A: resolver μ₂ accesiblemente) y la torre dinámica/estática sobre (a)+(c) (Dic/178.C: cargar ζ en lo coercivo accesiblemente). Probar una no allana la otra: el déficit es el mismo objeto visto desde dos lados. Las tres salidas:
- **(i)** Buscar el objeto externo de GAP-190.A (tres propiedades simultáneas, contrato explícito) — la dirección Connes/Deninger, ahora con especificación verificable; riesgo: años, sin cota (calibre de Phase 39).
- **(ii)** Atacar los pilares aritméticos directamente: LP-134∞/CONJ 179.6 (categoría Euler), 178.C, μ₂=o(1) vía R1/R2 — progreso incremental medible, sin promesa de cierre.
- **(iii)** Declarar la clasificación estructural resultado final y publicar (P49 con D184–188 + este criterio como capítulo de cierre).
**Recomendación:** ejecutar R2 primero (coste: medio documento; rendimiento: o un funcional anisótropo nuevo — el primer ladrillo del género que GAP-190.A pide — o una barrera quinta que completa la clasificación); decidir entre (i) y (iii) con el resultado de R2 y R1 en mano. La salida (ii) sin R2 repetiría formulaciones que los techos 172.9/176.9 ya prohíben.

---

## 5. Test anti-circularidad

| Pieza | ¿Asume RH/A/Dic? | Insumos |
|---|---|---|
| [DEF 190.1] | No (definición) | — |
| §2 (seis veredictos) | No | Resultados certificados D64, D152/172, D167/168, D173/176 (auditados D185), D174 §3.3 (auditado D186), D178 (auditado D187), D180 (auditado D188), Rodgers–Tao |
| [PROP 190.2] clase 1 | No | Dicotomía de Hadamard (ζ-libre, certificada) |
| [PROP 190.2] clase 2 | No; 180.3 condicional-a-Farmer DECLARADO (rendija R1) | 176.9, 172.9, 180.3, 180.4 |
| [PROP 190.2] clase 3 | No — los cuatro casos verificados individualmente, sin principio general no probado | §2.1, 2.4, 2.5, 2.6 |
| §4 | Lectura estratégica, no teorema | — |

Ninguna pieza usa la conclusión como input; el único condicional (suelo de Farmer dentro de la clase 2) está declarado y es exactamente la rendija R1 ya registrada en D188.

## 6. Veredicto

| Etiqueta | Enunciado | Estatus |
|---|---|---|
| [DEF 190.1] | Colapsador: (a) produce I, (b) produce μ₂(T) ∀T, (c) accesible incondicionalmente; trivial excluido | Definición |
| §2 | Ninguno de los seis candidatos del repertorio es colapsador | Verificado pieza a pieza sobre resultados auditados |
| [PROP 190.2] | Tricotomía: 𝔄* ⊆ (ζ-libre: pierde I(0)) ∪ (promediado: pierde μ₂) ∪ (exacto: no-accesible ≈ RH); (a)∩(b)∩(c)=∅ **en el repertorio examinado, NO universal** | Probado (clase 2 módulo Farmer = R1, declarado) |
| [GAP-190.A] | Objeto externo: ζ-cargado en el estado + anisótropo-con-signo microscópico + asa incondicional — las tres a la vez | GAP (especificación del objeto Connes/Deninger) |
| [GAP-190.B] | ¿R2 (flujo de borde) produce Σb·log γ incondicional? Si sí: primer funcional anisótropo accesible (colapsador parcial de primer orden) | GAP (sucesor inmediato, D188) |
| Respuesta al director | El sistema es estructuralmente incompleto para RH en su repertorio actual; las dos torres son dos proyecciones del mismo déficit | Lectura de la Prop 190.2 |

**Documentos internos:** D64, D71–72, D112, D141, D152, D154–157 (Phase 49), D164–165, D166–169, D170–172, D173, D174, D175, D176, D177, D178–179, D180, D181, D183, D184–188.
**Literatura:** B. Rodgers, T. Tao, "The de Bruijn–Newman constant is non-negative", *Forum Math. Pi* 8 (2020). B. Bagchi, "A joint universality theorem for Dirichlet L-functions", *Math. Z.* 181 (1982) / tesis 1981 (recurrencia y universalidad). D. W. Farmer, *Bull. LMS* 25 (1993) (suelo del molificador; condicionalidad declarada vía D188/R1).
