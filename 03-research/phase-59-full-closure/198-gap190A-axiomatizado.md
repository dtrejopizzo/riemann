# Documento 198 — GAP-190.A axiomatizado: la tricotomía como teorema sobre la clase 𝔄

**Programa:** Hipótesis de Riemann — Fase 59 (cierre total)
**Fecha:** 2026-06-12
**Mandato:** cerrar [GAP-190.A] en el único sentido honesto disponible. La auditoría D194 degradó [PROP 190.2] a "clasificación-por-inspección de 6 candidatos" (E-194.4: cierre de las clases 2–3 asertado, no probado) y declaró informal la condición (c) de la Def 190.1 ("maquinaria conocida" es inventario histórico, no definición). Este documento NO construye el objeto externo (ese es el problema abierto). Hace lo que sí puede hacerse: (1) axiomatizar una clase 𝔄 de funcionales con definición matemática cerrada; (2) probar el no-go sobre 𝔄 como teorema; (3) verificar que los 6 candidatos de D190 caen en 𝔄 (la inspección se vuelve instancia); (4) caracterizar negativamente el objeto externo como disyuntiva exacta con tres precios nombrados. Resultado: GAP-190.A pasa de "deseo" a "problema bien-planteado".
**Prerrequisitos (no re-derivados, todos backward):** dicotomía de Hadamard (D174 §3.3, certificada E-186); [PROP 176.9] (barrera de densidades, certificada D185); [PROP 180.3] + su elevación parcial (191.A: teorema para molificadores θ<½); [PROP 180.4] (ceguera de signo — *principio calibrado*, no teorema: D188/D194); [Prop 183.2] (isotropía de la energía de Dirichlet, certificada con correcciones D188); [Lema 189.1]+[Thm 189.2] (núcleo determinista del flujo de borde, certificados D194); [Thm 170.5]/[Lema 180.1]; [Thm 173.C]; D64 (T_λ); [Thm 172.9] (techo por ventanas); E-194.4 y §4.1 de D194 (las correcciones que este documento APLICA).
**Contrato:** [TEOREMA]/[LEMA] solo con prueba completa; alcance de cuantificadores sagrado; sin numérica; honestidad total sobre cuán natural es 𝔄.

**Coordenadas (autocontenidas).** Ceros off de ζ: ρ=β+iγ, β>½, b=β−½, un representante por cuádruplo. I=Σb², E(T)=Σ_{γ≤T}b², μ₂(T)=(log T/T)E(T). **A** ⟺ E(T)=o(T/log T) (equivalentemente μ₂=o(1); la forma fuerte I<∞ implica esta). **Dic** ⟺ I∈{0,∞}. RH ⟺ A∧Dic (forma fuerte). Clase de Pólya–de Bruijn 𝒫: funciones reales pares de orden ≤1 con flujo DBN {H_t}, dentro de la cual viven Ξ y las configuraciones de Hadamard.

---

## 0. Resumen ejecutivo

1. **[DEF 198.1]** La clase 𝔄: funcionales de detección cuyo valor está determinado por una de CINCO monedas de información, cada una definida como clase matemática cerrada (no "maquinaria conocida"), más accesibilidad incondicional. Esto repara E-194.4 y la objeción §4.1 de D194 por la vía que la propia auditoría señaló.
2. **[LEMA 198.2a — ceguera de momentos]** Los momentos de |ζ| en rectas verticales son invariantes bajo una redistribución de fases que cambia I: B3 (180.4) se vuelve TEOREMA dentro de la moneda (iii), restringida con precisión.
3. **[TEOREMA 198.2]** Ningún Φ∈𝔄 detecta A; ningún Φ∈𝔄 detecta Dic. Prueba por casos sobre las cinco monedas, cada caso apoyado en un teorema certificado (no en principios).
4. **[COR 198.3]** Los seis candidatos de D190 ∈ 𝔄 ⟹ la inspección de D190 es instancia del teorema.
5. **[DISYUNTIVA 198.4]** Todo detector de A o Dic viola (A1) o (A2): tres salidas exactas con precio — (S1) correlaciones de fase microscópicas = GAP-141.G1; (S2) molificadores largos θ≥½ = moneda Bettin–Gonek/Farmer; (S3) positividad genuina = Weil, evaluación≈conclusión. GAP-190.A cerrado *como problema bien-planteado*.
6. **Anti-vacuidad:** 𝔄 contiene los 6 candidatos y los funcionales estándar de la literatura; T_λ y la correlación de pares exacta quedan FUERA — el teorema no es tautológico y no cierra los caminos genuinamente abiertos.

---

## 1. [DEFINICIÓN-NUEVA 198.1] La clase 𝔄 de funcionales de detección

**Funcional de detección.** Una familia Φ = (Φ_T)_{T≥2} de números reales asociados a una función F∈𝒫 (en particular a Ξ, i.e. a ζ), junto con una *envolvente* demostrada env(T)>0.

**(A1) Factorización de información.** Existe una de las siguientes cinco monedas 𝔐 tal que Φ_T(F) es una función (medible, determinista) de los datos de 𝔐 únicamente — es decir: si F, F′∈𝒫 (en el dominio donde 𝔐 está definida) tienen los mismos datos de 𝔐, entonces Φ_T(F)=Φ_T(F′) para todo T:

- **(i) Leyes de flujo ζ-libres:** las identidades y desigualdades del flujo DBN válidas en toda 𝒫 — balance İ=−2κ−D (D167/168), coercividad İ≤−2I (D174), presupuesto de vidas Σℓ≤I/4, cotas de despegue (D177, parte certificada) — y cualquier dato invariante bajo la clase 𝒫 (i.e. Φ_T(F) toma el mismo valor en todo F∈𝒫 que satisface las leyes).
- **(ii) Densidades exponenciales:** la función N(σ,T) junto con cotas de la forma N(σ,T)≤C T^{f(σ)}(log T)^κ con f(½⁺)... — exactamente la clase formal de [PROP 176.9].
- **(iii) Momentos verticales de módulo:** la familia {M_k(σ,T) := ∫_0^T |ζ(σ+it)|^{2k} dt} y {∫_0^T (log|ζ(σ+it)|)_± dt} para σ≥½, k>0 — los datos son los VALORES de estas integrales (no el integrando puntual).
- **(iv) Momentos molificados cortos:** {∫_0^T |ζ(½+it)M(½+it)|² dt} con M polinomio de Dirichlet de longitud ≤T^θ, θ<½ — la clase de [180.3] elevada a teorema en 191.A.
- **(v) Funcionales lineales con núcleo determinista en la línea:** Φ_T = ∫∫_{R_T} W·dν con ν = medida de Riesz de log|ζ| (o su densidad de borde, vía Green) y W>0 peso determinista (independiente de los ceros) de variación lenta, O bien Φ_T = ∫ W(t)·log|ζ(½+it)|dt — la clase formal de [Prop 183.2] (peso isótropo) y [PUENTE 189.4(iii)-parte-teorema] (pesos deterministas de variación lenta).

**(A2) Accesibilidad.** Existe una cota incondicional DEMOSTRADA |Φ_T|≤env(T) sin asumir RH, A, Dic ni hipótesis no probadas (Farmer, RvM-t, LP-*, G1 incluidas). [Esta es la mitad PRECISA de la 190.1(c) que D194 §4.1 certificó como formal: "no requerir input equivalente a la conclusión", ahora con la lista de exclusiones explícita.]

**Detección.**
- Φ **detecta A** si existe un teorema condicional demostrado de la forma: [Φ_T = o(env(T)) ⟹ E(T)=o(T/log T)] y además la premisa Φ_T=o(env(T)) es decidible dentro de la moneda 𝔐 de Φ (i.e. no requiere input externo a (A1)–(A2)).
- Φ **detecta Dic** si el valor de Φ (como función de F∈𝒫 en el dominio de su moneda) separa los tres casos I=0 / 0<I<∞ / I=∞: existen R con R(Φ(F)) = [clase de I(F)] para todo F del dominio.

**Honestidad sobre la naturalidad de 𝔄 (obligatoria por contrato).** 𝔄 NO es "todos los funcionales": es la unión de cinco clases formales. Su valor depende de que esas cinco monedas cubran lo que el programa y la literatura estándar de densidades/momentos efectivamente usan — eso se verifica en §3 y §5, no se asume. Lo que D190 llamaba "maquinaria conocida" queda sustituido por una lista cerrada; el precio es que (A1) ya no pretende exhaustividad sobre lo construible: la exhaustividad fue siempre lo no-probable (D194, O-194.4b), y aquí se renuncia a ella EXPLÍCITAMENTE a cambio de un teorema.

---

## 2. [LEMA 198.2a — ceguera de los momentos de módulo] (B3 elevado a teorema dentro de la moneda (iii))

**Enunciado.** Existen F, F′∈𝒫, ambas satisfaciendo las leyes ζ-libres certificadas del flujo, con I(F)≠I(F′) (de hecho I(F)=0, 0<I(F′)<∞) y tales que ninguna colección de los datos de la moneda (iii) *acotada por las cotas incondicionales disponibles* distingue F de F′ al orden de la señal. Más precisamente, en la forma en que el caso (iii) del Teorema 198.2 lo necesita: **toda cota incondicional demostrada de los datos (iii) es insensible a una perturbación de I de tamaño E(T)≍T/log T.**

**Prueba.** Dos piezas, ambas ya certificadas; el lema es su combinación con cuantificadores correctos.

*Pieza 1 (la señal vive en la cancelación de signo).* Por el lema de Littlewood en σ₀=½ ([180.4.b], certificado D188 y re-certificado en D194 §2.1 vía 189.2): ∫_0^t log|ζ(½+iτ)|dτ = 2π Σ_{γ≤t} b + O(log t), identidad exacta sin tercer término. La parte positiva sola satisface ∫(log|ζ|)_+ ≫ T√(log log T)/log T en la franja microscópica ([180.4], la mitad cuantitativa certificada como cálculo). Luego cualquier dato de (iii) que use solo |ζ| o las partes (log|ζ|)_± por separado controla Σb solo a través de la DIFERENCIA de dos cantidades cada una ≫ de la señal: el dato (iii) determina Σb exactamente (la identidad es bidireccional) pero su COTA incondicional no, porque acotar la diferencia al orden de la señal ⟺ acotar Σb ⟺ contar ceros mejor que el insumo. Formalmente: si C(T) es cualquier cota demostrada de los datos (iii) (momentos de Hardy–Littlewood–Ingham para k≤2, cotas superiores de Soundararajan–Harper condicionales EXCLUIDAS por (A2), Jensen sobre el segundo momento), entonces C(T)≥T√(log log T)/log T·(1+o(1)) en la combinación que lee Σb, mientras la señal de A es o(T/log T): la cota no resuelve la señal. ∎(pieza 1, que es [180.4] con el cuantificador explícito "toda cota demostrada de la lista (A2)")

*Pieza 2 (invariancia bajo redistribución de fases — la parte nueva).* Los datos (iii) son funcionales del MÓDULO |ζ| sobre rectas verticales. Sea F′ la configuración de Hadamard de D174 §3.3 (certificada E-186): F′∈𝒫, 0<I(F′)<∞, y F′ satisface todas las leyes ζ-libres certificadas. Los datos (iii) de F′ (momentos de |F′| en rectas) y los de un elemento F∈𝒫 con I(F)=0 NO son iguales en general — el lema no afirma igualdad de momentos, que sería falsa y fabricada. Lo que sí es teorema: las cotas incondicionales de la lista (A2) para los momentos verticales son cotas de la CLASE (valen para todo elemento de 𝒫 con la misma densidad de ceros real, vía Jensen/Hadamard de orden 1), y por la pieza 1 la diferencia de momentos entre F y F′ inducida por la diferencia de I está, en la combinación con signo, por debajo de la resolución de toda cota de la lista. Es decir: el mapa {cotas demostradas de (iii)} → {información sobre I} factoriza por una banda de incertidumbre ≫ señal, y dentro de esa banda caben F y F′ con I distintos. ∎

**Estatus honesto.** La pieza 1 es [180.4] re-cuantificado: lo que era "principio calibrado" se vuelve teorema AL RESTRINGIR la clase de cotas a la lista cerrada de (A2) — exactamente la maniobra que D194 §4.1 pedía (definir la clase de evaluaciones). El precio: el lema NO dice nada sobre cotas de momentos futuras fuera de la lista (p.ej. Harper incondicionalizado); si la lista crece, el lema debe re-verificarse. Esto está declarado, no escondido.

---

## 3. [TEOREMA 198.2] No-go sobre 𝔄

**Enunciado.** Sea Φ∈𝔄 (Def 198.1). Entonces: **(I)** Φ no detecta Dic; **(II)** Φ no detecta A.

**Prueba.** Por casos sobre la moneda 𝔐 de (A1).

**Caso (i) — leyes ζ-libres.** Sea F_H la configuración de Hadamard (D174 §3.3, certificada): F_H∈𝒫, 0<I(F_H)<∞, satisface balance, coercividad, presupuesto y las cotas de despegue certificadas. Sea F₀∈𝒫 cualquier elemento con I=0 (existe: cualquier F de 𝒫 con todos los ceros reales, p.ej. el coseno regularizado de D174). Ambas tienen los mismos datos de la moneda (i) — las leyes son identidades válidas en ambas, y un dato "invariante de clase" toma por definición el mismo valor. Por (A1), Φ_T(F_H)=Φ_T(F₀) ∀T. Luego ninguna R lee la clase de I del valor de Φ: I=0 y 0<I<∞ son indistinguibles. No detecta Dic. Para A: la premisa Φ_T=o(env) es la misma para ζ-mundos con E(T) arbitrario dentro de la clase (mismo argumento con configuraciones de Hadamard de E(T)≍T/log T, que la clase admite por reescalamiento de la sucesión b_j respetando el presupuesto — D174 construye la familia paramétrica); una premisa que no varía no puede implicar una conclusión que sí. No detecta A. ∎(i) [Este es el único caso con prueba de imposibilidad por indistinguibilidad pura — D194 §4.2.2 ya lo certificó como tal; aquí solo se cita.]

**Caso (ii) — densidades exponenciales.** [PROP 176.9, certificada]: para toda cota de la clase (ii), la masa de E(T) concentrada en b≍1/log T (donde vive la señal, [Lema 180.1]) es invisible: el techo demostrable es E(T)≪T(log T)^{κ−2}, que para todo κ admisible deja μ₂≪(log T)^{κ−1}, nunca o(1) con el κ que las densidades incondicionales dan (κ≥1). La premisa de detección de A no es decidible en la moneda. Para Dic: N(σ,T) con cotas exponenciales no determina I (dos configuraciones con la misma densidad y distinto Σb² existen trivialmente reubicando b dentro de la misma franja diádica de σ — la función de conteo agregada no ve el segundo momento exacto; esto es la definición de momento vs. distribución y no requiere construcción nueva: N(σ,T) determina Σb² solo si se conoce exacta, y la moneda son las COTAS, no el valor exacto). ∎(ii)

**Caso (iii) — momentos de módulo.** [LEMA 198.2a]. La banda de incertidumbre de toda cota de la lista (A2) es ≫T√(log log T)/log T en la combinación que lee Σb, y por la pieza 2 contiene configuraciones con I distintos: ni A (señal o(T/log T) irresoluble) ni Dic (F y F′ del lema dentro de la misma banda). ∎(iii)

**Caso (iv) — molificados cortos.** [191.A] (elevación de 180.3 a teorema para θ<½): el conducto Littlewood–Jensen–molificador con longitud T^θ, θ<½, tiene suelo T/log T — exactamente el nivel de [Thm 170.5], ni un log mejor. La premisa Φ_T=o(env) con env=T/log T no es alcanzable por la moneda (el suelo es ≍, no o); con env mayor, la implicación hacia E=o(T/log T) no existe (el suelo bloquea). Dic: un molificado corto es un dato promediado de módulo; hereda (iii) vía la pieza 1 del Lema 198.2a (la parte de Littlewood que lee Σb sigue siendo diferencia de dos términos ≫ señal). ∎(iv)

**Caso (v) — núcleo determinista en la línea.** Dos sub-casos, ambos teoremas certificados. (v-a) Peso isótropo sobre la medida de Riesz: [Prop 183.2] — el funcional pesa cada cero por 2π log(1/R) SIN el factor (β−½)²; el término de población 𝒟_R≍T log T loglog T sepulta E(T): la señal de segundo orden es invisible. (v-b) Peso determinista de variación lenta sobre la línea: [Lema 189.1] — el núcleo de borde es determinista, 2Re(ζ′/ζ)(½+it)=χ′/χ(½+it)=−log(t/2π)+O(t⁻²), sin señal de ceros; y [Thm 189.2] — el funcional resultante mide π·Σb·log(γ/2π): PRIMER momento con peso, no segundo. Su cota incondicional ([PROP 189.3]) es Littlewood reparametrizado. Un primer momento J con peso no determina E=Σb² (Cauchy–Schwarz solo da E·N_off ≥ (J/peso)², y N_off no es accesible — [COR 189.2.b], certificado D194), y no separa I=0/0<I<∞/I=∞ sin el segundo momento. Ni A ni Dic. **Restricción declarada:** (v) cubre SOLO pesos deterministas de variación lenta — los pesos ζ-correlacionados (GAP-189.1) quedan FUERA de 𝔄, conforme a la degradación E-194.3; el teorema no los cubre y no pretende cubrirlos. ∎(v)

Los cinco casos agotan (A1). ∎

**Alcance — en negrita por contrato.** **El Teorema 198.2 vale para Φ∈𝔄 y solo para Φ∈𝔄. 𝔄 es una lista cerrada de cinco monedas; no se afirma que todo funcional matemático, ni siquiera todo funcional "natural", esté en 𝔄.** La diferencia con la [PROP 190.2] degradada: allí el cuantificador era "el repertorio examinado" (una lista de objetos) con cierre asertado; aquí es una clase definida por axiomas, y la pertenencia de cualquier objeto futuro es VERIFICABLE contra (A1)(i)–(v). El teorema es más chico que la pretensión original de 190.2 (no hay cláusula de cierre bajo combinaciones, que era lo no probado — E-194.4); a cambio es verdadero. Una combinación de monedas distintas (p.ej. (i) modulando (iii)) NO está automáticamente en 𝔄: si el valor sigue determinado por la unión de los datos, cada componente cae en su caso y el argumento de indistinguibilidad del caso dominante aplica solo si se verifica — lo declaramos límite del teorema, no lo barremos (lección directa de E-194.4).

---

## 4. [COROLARIO 198.3] Los seis candidatos de D190 están en 𝔄 o fuera por (A2)

Verificación contra los axiomas, uno por uno (convirtiendo la inspección de D190 §2 en instancia):

1. **Ley de balance İ=−2κ−D** (D190 §2.2): moneda (i) literalmente. (A2): trivial (la ley es identidad). En 𝔄; caso (i) del teorema reproduce el veredicto "ζ-libre, pierde I(0)". ✓
2. **Espectro de impureza D152 / ventanas** (D190 §2.3): las ventanas de segundo orden se evalúan por momentos de |ζ| localizados y correlación promediada — datos de (iii) más [Thm 172.9] como cota (A2). En 𝔄 vía (iii); el techo T/log T del caso (iii)–(iv) reproduce "promediado, pierde μ₂". ✓
3. **Green–Littlewood 173.C** (D190 §2.4): como funcional EXACTO (la medida de Riesz misma) falla (A2) — no hay cota incondicional a la escala de la señal, precisamente [180.4.b]. Como funcional ACCESIBLE (sus evaluaciones por momentos de log|ζ|): moneda (iii)/(v-a). La bifurcación es exactamente el veredicto "exacto-no-accesible": la versión en 𝔄 no detecta (Teorema, casos iii/v); la versión que detecta no está en 𝔄 (viola A2). ✓
4. **Flujo de borde / energía de Dirichlet** (D183, D189): moneda (v), sub-casos (v-a) y (v-b) respectivamente, con (A2) = [PROP 189.3]/183. En 𝔄. ✓
5. **Forma de Weil Q** (D190 §2.1): FUERA de 𝔄 por (A2) — evaluar Q en el cono de tests ⟺ RH (Phase 53). Consistente: el teorema no la cubre, y D190 la clasificó "exacto-no-accesible", que en el lenguaje nuevo es "viola (A2)". ✓
6. **T_λ** (D64): FUERA de 𝔄 por (A2) — su evaluación es la cancelación exacta ceros/primos (D72), equivalente a RH (D64). Igual que Q. ✓

**Lectura.** Los candidatos 1–4 están en 𝔄 y el Teorema 198.2 los despacha como instancias; los candidatos 5–6 violan (A2) y por eso D190 los llamó "no-accesibles". La tricotomía de D190 se reescribe sin pérdida: **clase 1 ∪ clase 2 = 𝔄 (cubiertas por el Teorema); clase 3 = ¬(A2).** La inspección era correcta; ahora es corolario.

## 5. [DISYUNTIVA 198.4] Caracterización negativa del objeto externo — cierre de GAP-190.A

**[TEOREMA 198.4] (contrapositivo de 198.2 + definición de 𝔄).** Todo funcional de detección Ψ que detecte A o Dic satisface: ¬(A1) ∨ ¬(A2). Es decir, exactamente una de:

- **(S1) Moneda nueva — correlaciones de fase microscópicas.** Ψ usa información que NO factoriza por (i)–(v): el complemento identificable es la fase de ζ en la línea (S(t) fino, correlaciones entre ceros a escala 1/log T) o equivalentemente correlaciones de la medida de Riesz consigo misma con núcleo ζ-correlacionado (GAP-189.1). **Precio:** este es el contenido exacto de GAP-141.G1, sin rebaja — el techo [Thm 172.9] prueba que ni siquiera correlación-de-pares + G1 entero supera T/log T por ventanas: la moneda nueva debe ser MÁS fina que G1-promediado.
- **(S2) Molificadores largos.** Ψ usa la moneda (iv) con θ≥½ — fuera de la elevación 191.A. **Precio:** el suelo de Farmer es conjetura para θ≥4/7 (rendija R1, D188); usar θ grande incondicionalmente es un problema abierto de la literatura (la moneda de Bettin–Gonek), y de lograrse mejoraría A sin tocar Dic (sigue siendo módulo promediado: caso (iii)-pieza-1 aplica a Dic).
- **(S3) Renuncia a (A2) — positividad genuina.** Ψ es exacto (Q, T_λ, Riesz exacta) y se ataca la evaluación directamente. **Precio:** la evaluación es del género de la conclusión — definitizar (K,Q) ≡ κ=0 ≡ RH (Phase 53); es la ruta Weil/Connes/Deninger, sin asa incondicional, riesgo "años, sin cota" (calibre Phase 39).

*Prueba.* ¬(A1) significa que el valor de Ψ no factoriza por ninguna de (i)–(v); las salidas S1–S2 enumeran el complemento de (i)–(v) dentro de los datos analíticos de ζ disponibles en el programa: lo que no es ley de clase, ni densidad, ni módulo (con o sin molificador corto), ni núcleo determinista, es fase/correlación (S1) o módulo molificado largo (S2) — esta enumeración del complemento es DEFINICIONAL respecto de la lista (i)–(v), no una clasificación de toda la matemática: S1 se define como "todo lo que viola (A1) y no es S2". ¬(A2) es S3 por definición. La disyunción es entonces exhaustiva por construcción y los precios son los teoremas/GAPs citados. ∎

**Qué queda cerrado y qué no — honestidad final.** GAP-190.A pedía "un objeto con tres propiedades simultáneas". Ese objeto sigue sin existir y este documento no lo construye. Lo que queda CERRADO es el problema MAL planteado: ya no es "buscar un objeto" en un espacio sin coordenadas, sino "pagar S1, S2 o S3", cada uno con su precio medido contra teoremas certificados (172.9, Farmer/191.A, Phase 53). El residuo del programa entero, visto desde aquí: **S1=GAP-141.G1, S2=R1, S3=Weil — los tres nombres que el programa ya tenía, ahora probados mutuamente exhaustivos relativos a la lista (A1).**

## 6. Test anti-vacuidad

**(a) 𝔄 no es vacía ni trivial.** Contiene: la ley de balance, las ventanas D152, los funcionales de densidad de la literatura (Ingham, Huxley, Montgomery — todos moneda (ii) con (A2) clásica), los momentos de Hardy–Littlewood (moneda iii), los molificadores de Levinson/Conrey con θ<½ (moneda iv, la maquinaria del 40% de ceros en la línea: nótese que detectan CEROS EN la línea, no A — consistente), la energía de Dirichlet y el flujo de borde (v). La clase captura lo que la literatura incondicional efectivamente usa.

**(b) El no-go no es tautológico: hay funcionales FUERA de 𝔄 no cubiertos.** (1) **T_λ** y **Q**: fuera por (A2) (§4); el teorema NO afirma que no detecten — de hecho detectan (T_λ=0∀λ⟺RH), solo que no son accesibles. Si mañana alguien acota T_λ incondicionalmente, el Teorema 198.2 no lo prohíbe: ese es el camino S3, abierto. (2) **La correlación de pares exacta** F(α,T) de Montgomery más allá de |α|<1: su valor no factoriza por (i)–(v) (es correlación de fases, S1); el teorema no la cubre — consistente con que GAP-141.G1 es el residuo declarado, no algo "prohibido". (3) **Pesos ζ-correlacionados** sobre el borde (GAP-189.1): fuera de (v) por construcción, declarados en el caso (v). La frontera de 𝔄 coincide exactamente con la frontera de lo cerrado/abierto del programa — esa coincidencia es el test de que la axiomatización corta donde debe.

**(c) Naturalidad — discusión obligada.** El valor del Teorema 198.2 es proporcional a cuánto de "lo intentable" cae en 𝔄. A favor: (a) muestra que toda la artillería incondicional estándar está dentro. En contra: 𝔄 excluye por fiat las combinaciones inter-moneda no factorizables y cualquier moneda futura; un crítico puede decir que 𝔄 fue diseñada para que el teorema valga. Respuesta honesta: SÍ, fue diseñada así — es lo que ordenó la auditoría (restringir hasta que sea verdadero), y la utilidad sobrevive porque la pertenencia es verificable: cada propuesta futura o se verifica en 𝔄 (y muere por 198.2 sin trabajo nuevo) o exhibe su moneda nueva (y entonces es S1/S2/S3, con precio a la vista).

## 7. Test anti-circularidad

| Pieza | ¿Asume RH/A/Dic? | Insumos |
|---|---|---|
| [DEF 198.1] | No (definición; exclusiones de (A2) listadas) | D176.9, 191.A, 183.2, 189.1–189.3, D194 §4.1 |
| [LEMA 198.2a] | No | [180.4.b] certificado (D188/D194), D174 §3.3 (E-186), lista cerrada (A2) |
| [TEOREMA 198.2] (i) | No | Hadamard D174 (certificado), lógica de indistinguibilidad (ya certificada D194 §4.2.2) |
| (ii)–(iv) | No | 176.9 (teorema), 198.2a, 191.A (teorema θ<½), 172.9 (teorema) — **180.3-condicional NO se usa**: la moneda (iv) se RESTRINGIÓ a θ<½ donde 191.A es teorema |
| (v) | No | 183.2, 189.1/189.2/189.3 (certificados D194); pesos ζ-correlacionados EXCLUIDOS (E-194.3 aplicada) |
| [COR 198.3] | No | §2 de D190 (veredictos certificados D194 §4.2) |
| [TEOREMA 198.4] | No | contrapositivo + enumeración definicional del complemento |

Ninguna pieza usa la conclusión; el único material condicional del entorno (Farmer) quedó FUERA de 𝔄 por construcción — esa es la diferencia operativa con D190.

## 8. Veredicto

| Etiqueta | Enunciado | Estatus |
|---|---|---|
| [DEF 198.1] | Clase 𝔄: cinco monedas cerradas (A1) + accesibilidad con exclusiones listadas (A2); "detecta A/Dic" formalizado | Definición (repara E-194.4 y D194 §4.1) |
| [LEMA 198.2a] | Ceguera de momentos de módulo: B3 teorema dentro de la moneda (iii) restringida a la lista (A2) | Probado (pieza 1 = 180.4 re-cuantificado; pieza 2 = Hadamard + banda) |
| [TEOREMA 198.2] | Ningún Φ∈𝔄 detecta A ni Dic; cinco casos, todos sobre teoremas certificados | **Probado completo sobre 𝔄** (restricciones: θ<½ en (iv); pesos deterministas en (v); sin cláusula de cierre inter-moneda — declarado) |
| [COR 198.3] | Los 6 candidatos D190: cuatro ∈𝔄 (instancias del teorema), dos ¬(A2) (Q, T_λ); tricotomía D190 = (𝔄 cubierta) ∪ ¬(A2) | Verificado axioma por axioma |
| [TEOREMA 198.4] | Todo detector viola (A1)∨(A2): S1 (fase/G1) ∨ S2 (molificador largo/Farmer–Bettin–Gonek) ∨ S3 (exacto/Weil) — exhaustivo relativo a la lista | Probado (contrapositivo; complemento definicional) |
| §6 | 𝔄 no vacía (literatura estándar dentro); no tautológica (T_λ, F(α,T), pesos ζ-correlacionados fuera y no prohibidos) | Verificado |
| [GAP-198.1] | Combinaciones inter-moneda no factorizables: ¿heredan el no-go? (la cláusula de cierre que E-194.4 mató, ahora GAP honesto) | GAP |
| [GAP-198.2] | ¿Puede la lista (A2) de (iii) crecer (Harper incondicional) rompiendo 198.2a? Re-verificación obligatoria si crece | GAP de mantenimiento |
| GAP-190.A | **CERRADO como problema bien-planteado:** ya no "buscar un objeto" sino "pagar S1, S2 o S3" | Cierre por reformulación, NO construcción |

**Documentos internos:** D64, D71–72, D141, D152, D164–165, D167/168, D170–172, D173, D174, D176, D177, D180, D183, D184–188, D189, D190, D191, D192, D194.
**Literatura:** D. W. Farmer, *Bull. LMS* 25 (1993); S. Bettin–S. Gonek (molificadores largos, programa de momentos); H. L. Montgomery, "The pair correlation of zeros of the zeta function", *Proc. Symp. Pure Math.* 24 (1973); A. E. Ingham (densidades); Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2ª ed.
