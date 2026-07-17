# Doc 113 — LP-112 contra la literatura: ¿existe precedente de auto-aproximación secuencial sin recurrencia fuerte?

**Programa:** Hipótesis de Riemann — Phase 37, "modo físico"
**Fecha:** junio 2026
**Autor:** David Alejandro Trejo Pizzo
**Prerrequisitos:** Doc 112 (LP-112; Teorema 2.3: LP-112 ⟹ m∈{0,∞}; Prop. 2.6: bajo ¬RH los τ buenos tienen densidad superior cero; Obs. 2.4: la seminorma B² anula compactos; Lemas 2.1–2.2: B²-casi-periodicidad incondicional y densidad positiva de casi-períodos); Doc 102 (auditoría Bagchi: recurrencia fuerte ⟺ RH; la observable de Euler discontinua en ω₀; familia SR_d); Doc 104 (SR_d efectivo: degeneración lineal de la escala, ventana anclada, muro binario de Hurwitz); Doc 109 (identidad RH = (m<∞) ∧ D-109); P43 (Principio 3.1, cuantificador maestro).
**Naturaleza del documento:** cartografía de literatura y comparación fina. La verificación en fuente es central: cada enunciado externo fue contrastado contra la fuente accesible (texto completo, abstract o survey verificado); lo no verificado se marca [NO VERIFICADO]. Sin numéricos, sin simulaciones. Ninguna prueba se fabrica; los GAPs se declaran con localización exacta.

---

## 0. Resumen ejecutivo

**La pregunta.** LP-112 (Doc 112, §2.2): *existe una sucesión τ_k → ∞ tal que
ζ(s+iτ_k) → ζ(s) uniformemente en cada disco compacto de la franja crítica abierta* —
auto-aproximación puntual **secuencial**, sin pedir densidad del conjunto de τ, solo
no-vacuidad. Sabemos: RH ⟹ LP-112 (vía Bagchi); LP-112 ⟹ m∈{0,∞} (D112, Thm. 2.3);
LP-112 es estrictamente más débil que la recurrencia fuerte; bajo ¬RH sus testigos
forman un conjunto de densidad superior cero (D112, Prop. 2.6) cuya vacuidad es
desconocida. ¿Hay en la literatura ALGÚN precedente — para ζ, para L-funciones, para
alguna clase natural de funciones — de auto-aproximación secuencial probada SIN pasar
por recurrencia fuerte / sin un equivalente de RH? ¿Y hay alguna técnica (Montel+B²,
Stepanov, Birkhoff) con chance real de probar LP-112 incondicionalmente?

**Hallazgos, en orden:**

1. **(§2.1) El precedente de la equivalencia es 60 años más viejo que Bagchi: Bohr
   1922.** Para χ no principal, RH(L(·,χ)) ⟺ L(·,χ) es casi-periódica en σ > 1/2 en
   el sentido local-compacto de Bohr (casi-períodos **relativamente densos**). La
   densidad relativa es load-bearing en la dirección recíproca (amplificador contra
   Bohr–Landau); la versión secuencial del enunciado de Bohr es exactamente LP-112 y
   queda fuera de su teorema por la misma razón que queda fuera del de Bagchi.

2. **(§2.5–2.6) El inventario de lo probado en auto-aproximación de ζ es exhaustivo y
   no contiene ningún enunciado secuencial incondicional en ninguna banda σ₀ < 1.**
   Todo lo incondicional es de densidad positiva y vive en d ≠ 0 (Nakamura, Pańkowski,
   Garunkštis; Baker y seis exponenciales); todo lo que toca d = 0 es RH-equivalente
   (Bagchi 1987; intervalos cortos 2025; equivalentes de Laurinčikas 2025). La abscisa
   incondicional de la casi-periodicidad puntual de ζ es exactamente σ₀ = 1: por debajo,
   la versión relativamente densa en σ > σ₀ es **equivalente** a "ζ sin ceros en
   σ > σ₀" (circular), y la versión secuencial está abierta para TODO σ₀ < 1 — la
   franja entera es terra incognita, incluso pegada a σ = 1.

3. **(§3) Los precedentes en otras clases existen y todos usan la misma técnica:
   genericidad del punto (soporte pleno).** La zeta de Hurwitz ζ(s,α) con α
   trascendente (o racional ≠ 1/2, 1) es fuertemente recurrente incondicionalmente —
   una función CON ceros en la franja que se auto-aproxima con densidad positiva —
   porque su medida de Bagchi tiene soporte pleno: el punto es genérico para su propia
   estadística. No existe en la literatura NINGÚN caso de auto-aproximación certificada
   para un punto fuera del soporte de su estadística de shifts — que es exactamente lo
   que LP-112 pide bajo ¬RH.

4. **(§4 — corazón del documento) La cadena Montel+B² muere, y muere exactamente en el
   punto de D112 Prop. 2.6/Obs. 2.4.** Los eslabones de compacidad sobreviven
   íntegros: momentos incondicionales + Chebyshev dan densidad ≥ 1−δ de τ con cota
   local, la intersección con los casi-períodos B² (densidad positiva) tiene densidad
   positiva, y Montel extrae una sucesión τ_k → ∞ con ζ(·+iτ_k) → g. El eslabón que
   muere es la **identificación g = ζ**: la información B² es un promedio global en t
   que asigna peso idénticamente nulo a la ventana del disco, y la información
   compacto-abierta vive solo en esa ventana — los soportes de las dos informaciones
   son disjuntos. Bajo H(m) la muerte es teorema: el límite genérico es no-nulo en D
   (soporte de Bagchi + Hurwitz) mientras ζ|_D se anula. El intento de re-anclaje por
   composición de casi-períodos reproduce el colapso de la ventana anclada de D104
   §5.4. Lo que falta queda aislado como **LP-113 (lema de anclaje)**: localizar la
   bondad media de UN casi-período B² en la ventana compacta fija. LP-113 no es
   RH-equivalente por los diccionarios conocidos, pero sus testigos tienen densidad
   cero bajo ¬RH: es el mismo muro de selección no-genérica, en coordenada de ventanas.

5. **(§5) Stepanov: la salida estructural existe y está cerrada por crecimiento,
   incondicionalmente.** La seminorma S² (ventanas de tamaño fijo, sup sobre la
   posición) NO anula compactos — si ζ fuera S²-casi-periódica en una banda, el
   argumento de la Prop. 2.6 no se aplicaría y la subarmonicidad daría a Rouché el
   control puntual. Pero probamos (Teorema 5.2, incondicional): ζ NO es S^p-casi-
   periódica en ninguna sub-banda de la franja, para ningún p ≥ 1 — la
   S-casi-periodicidad implica S-acotación, la subarmonicidad convierte los valores
   grandes de ζ (Ω-teoremas incondicionales; Montgomery 1977, Aistleitner 2016) en
   ventanas de norma divergente. Y la seminorma de Weyl vuelve a anular compactos. La
   dicotomía resultante es exacta y es el hallazgo estructural del documento: **toda
   seminorma de casi-periodicidad que ve los compactos es destruida por el crecimiento
   de ζ en la franja; toda seminorma que sobrevive al crecimiento es ciega a los
   compactos.** El muro de P43, en coordenada de seminormas.

6. **(§6) Birkhoff no aplica:** la órbita {ζ(·+iτ)} no es relativamente compacta en
   H(franja) (Ω-teoremas), la recurrencia de Poincaré sobre la medida de Bagchi
   produce recurrencia c.t.p. — genérica — y la compacidad disponible vive arriba, en
   el toro de Kronecker, donde la obstrucción es la discontinuidad de la observable de
   Euler en ω₀ (D102 §7.3): nada nuevo respecto de D102, verificado.

**VEREDICTO (§8): SIN PRECEDENTE.** Ningún enunciado de la literatura prueba
auto-aproximación secuencial sin probar al mismo tiempo recurrencia con densidad
(positiva o relativa) vía genericidad del punto. LP-112 requiere una técnica nueva:
un mecanismo de **selección no-genérica** (anclaje de casi-períodos a una ventana
compacta fija — el lema LP-113), del que no existe instancia en teoría de funciones,
dinámica topológica ni teoría analítica de números.

---

## 1. El objeto y el criterio de comparación

### 1.1. LP-112, enunciado exacto (D112 §2.2)

**Lema LP-112 (ABIERTO).** *Para todo disco cerrado D ⊂ {½ < σ < 1} existe una
sucesión τ_k → ∞ tal que*
$$\sup_{s \in D} |\zeta(s + i\tau_k) - \zeta(s)| \;\longrightarrow\; 0.$$
(Versión débil LP-112⁻, suficiente para refutar cada H(m): para todo D y ε > 0 existe
UN τ > altura(D) con sup_D |ζ(s+iτ) − ζ(s)| < ε.)

Lo que se sabe (todo en D112): RH ⟹ LP-112 (recurrencia fuerte de Bagchi ⟹ densidad
positiva ⟹ sucesión); LP-112 ⟹ m ∈ {0,∞} (Thm. 2.3, Rouché con constantes congeladas
por H(m)); bajo H(m), el conjunto A_ε de τ buenos tiene densidad superior cero
(Prop. 2.6) pero su vacuidad es desconocida; LP-112 no implica RH por ningún
diccionario conocido (D112 §5.4).

### 1.2. Qué cuenta como precedente

Un precedente de LP-112 sería un teorema de la forma: *en alguna clase natural de
funciones, f(s+iτ_k) → f(s) en compactos para alguna sucesión τ_k → ∞, probado en un
régimen donde NO se sabe (o es falso) que el conjunto de τ buenos tenga densidad
positiva* — es decir, auto-aproximación certificada para un punto posiblemente
**no-genérico** de su propia estadística de shifts. Un teorema que prueba densidad
positiva (o densidad relativa) y deduce la sucesión como corolario NO es precedente:
es exactamente la maquinaria que la Prop. 2.6 de D112 clausura para ζ bajo ¬RH. La
distinción organiza todo el documento.

---

## 2. Mapa exacto de lo probado en auto-aproximación de ζ y L-funciones

### 2.1. El precedente de la equivalencia: Bohr 1922, sesenta años antes de Bagchi

**Teorema (Bohr, 1922).** *Sea χ un carácter de Dirichlet no principal. Entonces RH
para L(s,χ) es equivalente a la casi-periodicidad de L(s,χ) en el semiplano σ > 1/2,
donde "casi-periódica en una región E" significa: para todo ε > 0 y todo compacto
K ⊂ E existe un conjunto **relativamente denso** {τ_m} ⊂ ℝ con
sup_{s∈K} |f(s+iτ_m) − f(s)| < ε para todo m.*

*Verificación.* Enunciado verificado vía fuentes secundarias (Herichi–Lapidus,
arXiv:1305.3933, §2, que lo enuncia con la definición local-compacta citada; también
recogido en la exposición estándar de Steuding). El original: H. Bohr, *Über eine
quasi-periodische Eigenschaft Dirichletscher Reihen mit Anwendung auf die
Dirichletschen L-Funktionen*, Math. Ann. 85 (1922) [datos bibliográficos exactos vía
fuentes secundarias; texto original NO VERIFICADO en esta sesión]. La motivación
histórica registrada: Bohr introdujo la casi-periodicidad como herramienta para RH; el
enfoque "falló para ζ" (el polo en s = 1 y la estructura del problema) y quedó la
reformulación para L(s,χ) con χ no principal.

Tres observaciones de comparación fina, que son el contenido útil:

**(a) La noción de Bohr es local-compacta, no uniforme-en-la-recta.** No requiere
acotación de L en la franja (que es falsa, Ω-teoremas): pide casi-períodos por compacto.
Es exactamente la topología de LP-112 — con una diferencia: **densidad relativa** del
conjunto de casi-períodos, donde LP-112 pide solo una sucesión.

**(b) La densidad relativa es load-bearing en la dirección "casi-periodicidad ⟹ RH",
y lo es por el mismo amplificador que en Bagchi.** Si L tiene un cero ρ₀ con
Re ρ₀ > 1/2, Rouché transporta el cero a cada casi-período: un conjunto relativamente
denso de τ_m da ≫ T ceros hasta altura T en σ ≥ Re ρ₀ − ε, contradiciendo
N(σ,T) = o(T) (Bohr–Landau 1914 — disponible para Bohr en 1922). Con una mera
SUCESIÓN se obtienen infinitos ceros, es decir m = ∞ — ninguna contradicción: la
versión secuencial del teorema de Bohr no es equivalente a RH(χ), es exactamente el
análogo de LP-112 para L(s,χ), y está igual de abierta. **La frontera
densidad-relativa/sucesión ya estaba trazada en 1922; nadie la cruzó.**

**(c) La dirección "RH ⟹ casi-periodicidad" es el mismo mecanismo de D102
Prop. 7.2:** RH(χ) ⟹ Σ_p χ(p)p^{−s} converge en σ > 1/2 ⟹ log L hereda la
casi-periodicidad de la serie convergente (maquinaria de Bohr) ⟹ L = exp(log L) es
casi-periódica en compactos. La adaptación a ζ (con el polo excluido de los compactos,
o trabajando con (s−1)ζ(s)) da el folclore: **ζ es localmente casi-periódica (con
casi-períodos relativamente densos) en σ > σ₀ ⟺ ζ no tiene ceros en σ > σ₀** — ambas
direcciones por lo anterior. Esto se usa en §2.6. [Ensamblado aquí de piezas estándar:
la equivalencia para ζ con esta noción no la encontramos enunciada literalmente en la
literatura consultada; las dos direcciones son las pruebas de Bohr y el amplificador,
y el núcleo (b)⟺(a) es la Prop. 7.2 de D102.]

### 2.2. Bagchi 1981/1987: recurrencia fuerte ⟺ RH (verificado)

**Teorema (Bagchi).** *RH ⟺ para todo compacto K ⊂ D(1/2,1) con complemento conexo y
todo ε > 0:*
$$\liminf_{T\to\infty}\ \frac{1}{T}\,\mathrm{meas}\Big\{\tau\in[0,T] :
\sup_{s\in K}|\zeta(s+i\tau)-\zeta(s)|<\varepsilon\Big\}\;>\;0. \tag{SR}$$

*Verificación.* Verificado en D102 §2.3 contra el survey de Matsumoto
(arXiv:1407.4216, Thm. 20), que expone la tesis de Bagchi (Indian Statistical
Institute, 1981) y el paper B. Bagchi, *Recurrence in topological dynamics and the
Riemann hypothesis*, Acta Math. Hungar. 50 (1987), 227–240. La mejora de Bagchi sobre
Bohr 1922: (i) cubre ζ; (ii) reemplaza densidad relativa por densidad de medida
positiva; (iii) la prueba de RH ⟹ SR pasa por el teorema límite funcional y el
soporte S = {f ≠ 0 en D} ∪ {0} — el punto ζ es genérico bajo RH porque pertenece al
soporte. La estructura es idéntica a Bohr: genericidad en una dirección, amplificador
contra densidad o(T) en la otra. **En ambos teoremas, la cantidad de testigos exigida
(densidad relativa o de medida) es exactamente la que activa el amplificador; LP-112
está calibrado para desactivarlo (D112 Prop. 2.7), y por eso ninguno de los dos
teoremas lo alcanza.**

### 2.3. La familia SR_d, d ≠ 0: el estado incondicional completo (verificado)

Para d ∈ ℝ, (SR_d) es el enunciado (SR) con ζ(s+idτ) en lugar de ζ(s); (SR_0) = (SR)
= RH. Estado verificado en fuente (D102 §6.3, D104 §1.2, y re-verificado en esta
sesión contra los abstracts/textos accesibles):

- **d irracional algebraico:** (SR_d) incondicional — T. Nakamura, *The generalized
  strong recurrence for non-zero rational parameters*, Arch. Math. 95 (2010), 549–555
  (la parte algebraica), vía universalidad conjunta + **teorema de Baker** (formas
  lineales en logaritmos).
- **d trascendente:** (SR_d) incondicional — Ł. Pańkowski, vía el **teorema de los
  seis exponenciales** (en *Self-approximation of Dirichlet L-functions*,
  arXiv:1006.1507, y expuesto en Matsumoto §9).
- **d racional, d ≠ 0, ±1:** incondicional — Nakamura–Pańkowski, Arch. Math. 99
  (2012), 43–47 (corrigendum, verificado vía arXiv:1203.1393: ζ para |a−b| ≠ 1, log ζ
  para todo d ≠ 0) y Ł. Pańkowski, *Joint universality and generalized strong
  recurrence with rational parameter*, arXiv:1503.06931 (verificado: todo racional
  d ≠ 0, ±1).
- **d = 1:** trivial (las dos copias coinciden). **d = −1:** comparar ζ(s+iτ) con
  ζ(s−iτ); excluido de los teoremas anteriores; estado: abierto según las fuentes
  consultadas [NO VERIFICADO si existe trabajo posterior que lo cubra].
- **Nota de cartografía (honestidad sobre la fragilidad de la frontera):** el preprint
  T. Nakamura, *A simple proof of the generalized strong recurrence for any non-zero
  parameter*, arXiv:1006.3184, que afirmaba todo d ≠ 0 de una vez, fue **retirado por
  el autor** ("the proof has a gap" — verificado en arXiv). La frontera d ≠ 0 se
  cerró por acumulación de técnicas diofantinas distintas por clase de d, no por un
  mecanismo unificado. El punto d = 0 no es el final de una rampa: es otra categoría.
- **Además:** Nakamura–Pańkowski, *Self-approximation for the Riemann zeta function*,
  Bull. Aust. Math. Soc. (2012/13; verificado vía Cambridge Core a nivel de abstract
  [volumen y páginas NO VERIFICADOS]): auto-aproximación en σ > 1 y en la mitad
  derecha de la franja crítica, con resultados de aproximación conjunta de
  ζ(s+λ+idτ) y ζ(s+iτ) — de nuevo, todos enunciados de densidad positiva con d ≠ 0
  o desplazamiento λ fijo no nulo.

**Lectura comparativa (D104, confirmada por la literatura):** todos los (SR_d) con
d ≠ 0 explotan **equidistribución relativa** — las fases p^{−i(1−d)τ} equidistribuyen
y Baker/seis-exponenciales certifican la independencia del sistema conjunto. En d = 0
la equidistribución relativa es idénticamente nula y el problema colapsa a la posición
absoluta del punto aritmético: el insumo diofantino se agota exactamente en la
frontera (D102 §6.3). D104 cuantificó el colapso: la densidad no degenera, la escala
degenera linealmente (T₀ ≍ 1/|d|), y la cantidad que Rouché necesita (densidad en la
ventana anclada J_d, de medida ≍ 1/|d|) es demostrablement exactamente 0 — muro
binario de Hurwitz, no cuantitativo.

### 2.4. d = 0 en intervalos cortos y los equivalentes de 2025: todo sigue siendo densidad

Verificado a nivel de abstract/fuentes secundarias: el trabajo reciente sobre
auto-aproximación de ζ en intervalos cortos (Andersson, Garunkštis, Kačinskaitė et
al., Symmetry 17 (2025), art. 2075 [lista de autores verificada parcialmente vía
buscador; texto completo NO VERIFICADO — el servidor rechazó el acceso]) prueba que
RH es equivalente a la positividad de la densidad inferior (y, con salvedades de
precisión, de la densidad) del conjunto de shifts aproximantes **en intervalos
cortos**; en la misma línea, A. Laurinčikas, *On equivalents of the Riemann
hypothesis connected to the approximation properties of the zeta-function*, Axioms 14
(2025), 169 [verificado a nivel de abstract]. Es decir: la investigación activa en
d = 0 produce **más equivalencias con RH**, todas en términos de densidad — ninguna
versión secuencial, ninguna incondicional. La dirección del campo confirma el
diagnóstico de D112: la frontera entre "densidad positiva" (RH-equivalente) y
"sucesión" (LP-112) no ha sido explorada porque no hay herramienta del lado
secuencial.

### 2.5. ¿Existe ALGÚN resultado secuencial incondicional para ζ en la franja? Inventario negativo

Buscamos sistemáticamente (sesiones de búsqueda sobre "self-approximation", "strong
recurrence", Nakamura/Pańkowski post-2011, Andersson, Garunkštis; survey de Matsumoto
§9 como mapa maestro). Resultado del inventario:

1. **τ_k de sucesiones especiales — casi-períodos de Bohr de la cola:** no existe.
   El único mecanismo que produce casi-períodos explícitos (Kronecker–Weyl sobre
   {τ log p/2π}_{p≤X}, D112 Lema 2.2) produce casi-períodos **B²**, cuya bondad es
   media en t y peso nulo en compactos (D112 Obs. 2.4). No hay en la literatura
   ningún teorema que promueva un casi-período de polinomio de Dirichlet truncado a
   casi-período puntual de ζ en la franja; el obstáculo es la cola
   ζ − P_X, que solo se controla en media (valor medio cuadrático) — el mismo punto
   donde D112 §2.3 localizó las tres fallas.
2. **τ_k de tiempos de retorno ergódico:** los tiempos de retorno del flujo de
   Kronecker en el toro (incondicionales, relativamente densos — D102 E3) no se
   transfieren a ζ porque la observable de Euler no es continua en ω₀ (D102
   Prop. 7.2/§7.3): la transferencia ES RH. Ningún trabajo de la literatura esquiva
   esto; Bagchi 1987 lo formuló (es el contenido de su título) y ahí quedó.
3. **Universalidad discreta (Reich):** shifts τ = nh, n ∈ ℕ — el enunciado vuelve a
   ser de densidad positiva (en n) y el objetivo debe ser no-nulo: A. Reich,
   *Werteverteilung von Zetafunktionen*, Arch. Math. 34 (1980) [vía Matsumoto §8;
   original NO VERIFICADO]. Sin contenido secuencial nuevo.
4. **Aproximaciones por productos de Euler híbridos (Gonek; Gonek–Hughes–Keating):**
   ζ ≈ producto truncado × factor de ceros, válido "para casi todo t" o fuera de
   conjuntos excepcionales — de nuevo enunciados c.t.p./densidad 1, jamás en la
   ventana fija. [Citado como contexto; detalles NO VERIFICADOS en esta sesión, no
   load-bearing.]

**Conclusión del inventario: no existe ningún resultado de auto-aproximación
secuencial incondicional para ζ en ninguna sub-región de la franja crítica.** Todo lo
publicado es: (i) densidad positiva con d ≠ 0; (ii) RH-equivalente con d = 0;
(iii) trivial en σ > 1.

### 2.6. La abscisa de la casi-periodicidad puntual: σ₀ = 1 es el borde exacto

**(a) σ > 1: trivialmente sí.** Convergencia absoluta ⟹ ζ es uniformemente
casi-periódica de Bohr en cada σ ≥ 1+ε (Bohr 1918; D112 §2.1(a)) ⟹ los casi-períodos
(relativamente densos) dan auto-aproximación secuencial en compactos de σ > 1.
LP-112 restringido a σ > 1 es teorema clásico — y vacuo para ceros (Euler).

**(b) ¿Hasta qué σ₀ < 1 se extiende incondicionalmente? Respuesta: ninguno.** La
situación, con precisión:

- **Versión uniforme (Bohr en la recta):** FALSA para todo σ ≤ 1 — ζ no es acotada en
  ninguna recta σ ≤ 1 (Ω-teoremas, incondicional; [Tit86, Cap. VIII]; en σ = 1,
  ζ(1+it) = Ω(log log t)). El borde de la casi-periodicidad uniforme es exactamente
  la abscisa de acotación, σ = 1.
- **Versión local-compacta relativamente densa (la noción de Bohr 1922):** por
  §2.1(c), su validez en σ > σ₀ es **equivalente** a "ζ sin ceros en σ > σ₀"
  (quasi-RH de abscisa σ₀). Como ninguna región libre de ceros de la forma σ > σ₀
  con σ₀ < 1 está probada (la región de Vinogradov–Korobov degenera con la altura y
  no da ninguna banda fija), **toda extensión incondicional a algún σ₀ < 1 es
  circular**: probaría quasi-RH. El supremo θ de las partes reales de los ceros es
  exactamente la abscisa crítica de esta noción, y "extender por debajo de 1" =
  "bajar θ" — el problema mismo.
- **Versión secuencial (LP-112 por bandas):** para σ > σ₀ con σ₀ < 1 implica solo
  "el número de ceros en σ > σ₀ es 0 o ∞" (el argumento del Thm. 2.3 de D112,
  verbatim por bandas). Esto NO es quasi-RH — no hay circularidad — y sin embargo
  **está abierto para todo σ₀ < 1**, incluso σ₀ = 1 − δ con δ minúsculo, donde los
  teoremas de densidad de ceros son fortísimos (N(σ₀,T) ≪ T^{κ} con κ pequeño). Ni
  siquiera se sabe que el número de ceros de ζ en σ > 0.99 sea 0 o infinito.
- **¿Vías de momentos/Carlson para alguna σ < 1?** Los momentos (Carlson, valor medio
  cuadrático, [Tit86, Thm. 7.2]) son exactamente el insumo del Lema 2.1 de D112: dan
  B², es decir, casi-periodicidad **en media** en toda la franja σ > 1/2 — más abajo
  y más débil de lo que la pregunta pide. No promueven a puntual en ninguna banda: la
  promoción es el problema (D112 §2.3). No existe resultado intermedio "puntual en
  σ > σ₀ para algún σ₀ ∈ (1/2,1) incondicional" — el salto de media a puntual no se
  ha dado en ninguna abscisa por debajo de 1.

**Síntesis de (i):** σ₀ = 1 es el borde demostrado de la casi-periodicidad puntual
(secuencial o relativamente densa) de ζ; la franja entera es terra incognita para la
versión secuencial, y territorio RH-circular para la versión relativamente densa. El
mapa tiene la forma exacta que el muro de P43 predice: lo puntual está probado donde
no hay ceros que encontrar, lo medio está probado en todas partes, y la promoción
media→puntual no está probada en ningún lugar donde importe.

---

## 3. Precedentes en otras clases de funciones

### 3.1. El precedente positivo real: Hurwitz y el soporte pleno

**Hecho (incondicional, literatura verificada).** La zeta de Hurwitz
ζ(s,α) = Σ_{n≥0}(n+α)^{−s} con α trascendente (Bagchi 1981; también Gonek para α
racional ≠ 1/2, 1 — vía Matsumoto §7, verificado en el survey) es **fuertemente
universal** en D(1/2,1): aproxima con densidad positiva de shifts cualquier
f ∈ H^c(K) — **sin restricción de no-anulación**, porque al no haber producto de
Euler el teorema límite funcional tiene soporte pleno (todo H(D)). Corolario
inmediato (tomando f = ζ(·,α)|_K): **ζ(s,α) es fuertemente recurrente — se
auto-aproxima con densidad positiva — incondicionalmente, a pesar de tener
infinitos ceros en la franja.** La línea de auto-aproximación específica:
R. Garunkštis, E. Karikovas, *Self-approximation of Hurwitz zeta-functions*, Funct.
Approx. Comment. Math. 51 (2014), 181–188 (verificado; tratan la familia con
parámetro d, con α trascendente), y Karikovas–Pańkowski para α racional [vía fuentes
secundarias].

**Lectura — por qué esto NO es precedente de LP-112 sino su contraste perfecto.** La
auto-aproximación de Hurwitz se prueba haciendo al punto **genérico**: ζ(·,α)
pertenece al soporte de su propia medida límite porque el soporte es todo. El milagro
no está en una técnica de selección sino en la geometría del soporte. Para ζ bajo
¬RH ocurre lo opuesto: el producto de Euler comprime el soporte a
{f ≠ 0} ∪ {0} y un cero off-crítico expulsa a ζ de él (D112 Prop. 2.6). La
comparación produce la ironía estructural del programa en su forma más nítida: **la
propiedad aritmética que hace plausible a RH (Euler ⟹ soporte sin ceros) es
exactamente la que hace indemostrable la auto-aproximación por genericidad.** Las
funciones sin Euler se auto-aproximan trivialmente (soporte pleno) Y tienen ceros
off-críticos a mansalva (m = ∞: Hurwitz, Davenport–Heilbronn) — realizan la rama
m = ∞ de la dicotomía con auto-aproximación incluida, en perfecta consistencia con
el Thm. 2.3 de D112.

### 3.2. Davenport–Heilbronn y la clase intermedia

La función de Davenport–Heilbronn (serie de Dirichlet con ecuación funcional, sin
Euler) tiene infinitos ceros off-críticos ([DH36], verificado en D111/D112). Su
fuerte recurrencia sería el mismo fenómeno de soporte pleno que Hurwitz (es una
combinación de L-funciones / zetas de Hurwitz con α racional) [universalidad fuerte
de la clase: plausible y citada en la literatura de universalidad mixta; estatus
exacto para DH NO VERIFICADO en esta sesión — no load-bearing]. El patrón confirmado:
en toda la clase "serie de Dirichlet + ecuación funcional sin Euler" donde la
auto-aproximación está probada, está probada por genericidad y coexiste con m = ∞.

### 3.3. Productos de Euler aleatorios: recurrencia c.t.p.

Para el elemento aleatorio ζ(s,ω) (producto de Euler aleatorio, ω en el toro
infinito), la medida de Bagchi es invariante bajo el flujo vertical y c.t. ω el punto
es genérico: la recurrencia fuerte de ζ(·,ω) vale para casi todo ω (teorema límite +
soporte; [Bag81], [Lau96]). El punto aritmético ω₀ es UN punto del espacio; bajo ¬RH
es exactamente un punto del conjunto nulo excepcional (D102 Cor. 7.3). **Precedente
de "c.t.p. del espacio se auto-aproxima": sí, estándar. Precedente de "ESTE punto se
auto-aproxima" cuando el punto puede ser excepcional: ninguno.**

### 3.4. Clase de Selberg y B²-casi-periódicas generales

- **Clase de Selberg:** la recurrencia fuerte d = 0 para elementos de la clase de
  Selberg es GRH-equivalente por el mismo mecanismo de Bagchi (extensiones: el propio
  Bagchi a L(s,χ); Steuding a clases más amplias — vía D102 §2.3 y Matsumoto). Nada
  secuencial.
- **Funciones B²-casi-periódicas con frecuencias ℚ-linealmente independientes (clase
  abstracta):** aquí la pregunta secuencial es FALSA en general sin hipótesis
  adicionales: los cosh-ejemplos de D111 ni siquiera son B² (D112 Lema 3.1), pero
  dentro de B² la teoría clásica (Besicovitch 1932; Jessen–Tornehave [JT45] para la
  estructura de ceros media) es íntegramente una teoría de medias — la función de
  Jensen ve densidades medias de ceros, no ceros individuales (D112 §6.2). No existe
  en la teoría clásica de funciones casi-periódicas holomorfas NINGÚN teorema de la
  forma "f ∈ B²(banda) ⟹ f(·+iτ_k) → f puntualmente en compactos para alguna
  sucesión": la clase B² identifica funciones que difieren en compactos (la seminorma
  anula compactos), de modo que el enunciado puntual **ni siquiera es una propiedad
  de la clase de equivalencia B²** — es una propiedad del representante. Ningún
  teorema sobre la clase puede probarlo. Esta observación trivial pero exacta explica
  por qué la búsqueda de precedentes en la teoría abstracta de casi-periodicidad está
  estructuralmente vacía: LP-112 es invisible en la categoría donde ζ tiene sus
  teoremas incondicionales.

---

## 4. La cadena Montel + B²: examen con máximo rigor y máxima sospecha

Esta es la línea señalada como más prometedora en el encargo, y el corazón del
documento. La desplegamos eslabón por eslabón, probamos lo que sobrevive, y
localizamos exactamente dónde muere.

### 4.1. Los cinco eslabones

Fijemos un disco cerrado D = D̄(s₀, r) ⊂ {½ < σ < 1} y un rectángulo compacto R con
D ⊂ interior(R) ⊂ R ⊂ {½ < σ < 1}; sea W = proyección en t de R (la "ventana").

- **(E1) Momentos ⟹ acotación local para casi todo τ.** Por el valor medio cuadrático
  incondicional ([Tit86, Thm. 7.2], integrado en σ sobre R con convergencia dominada
  — el cálculo del Lema 2.5 de D112), (1/T)∫₀^T (∬_R |ζ(s+iτ)|²dA(s)) dτ → c_R < ∞.
  Por Chebyshev, G_M := {τ : ∬_R |ζ(s+iτ)|² dA ≤ M} tiene densidad inferior
  ≥ 1 − c_R/M − o(1).
- **(E2) Subarmonicidad ⟹ normalidad sobre G_M.** Para τ ∈ G_M, subarmonicidad de
  |ζ(·+iτ)|² da sup_{D'} |ζ(·+iτ)|² ≤ M/(π d₀²) con D' ⊃ D intermedio y d₀ =
  dist(D', ∂R): la familia {ζ(·+iτ) : τ ∈ G_M} es uniformemente acotada en D', luego
  **normal** (Montel).
- **(E3) Casi-períodos B².** E_ε (D112 Lema 2.2) tiene densidad inferior positiva
  d(ε) > 0, incondicionalmente (Kronecker–Weyl + factorización única).
- **(E4) Intersección y extracción.** Para M ≥ M(ε) := 2c_R/d(ε), el conjunto
  E_ε ∩ G_M tiene densidad inferior ≥ d(ε)/2 > 0; en particular es no acotado. Montel
  sobre él: existe τ_k → ∞, τ_k ∈ E_ε ∩ G_M, y g_ε ∈ H(D') holomorfa con
  ζ(·+iτ_k) → g_ε uniformemente en D.
- **(E5) Identificación.** ¿g_ε = ζ|_D (o al menos ‖g_ε − ζ‖_{∞,D} ≤ φ(ε) → 0)? Si
  sí, diagonal sobre ε → 0 produce la sucesión de LP-112. **Este es el eslabón en
  cuestión.**

**Lo que queda probado (registro honesto): E1–E4 son teoremas**, ensamblados de
piezas incondicionales (momentos, subarmonicidad, Montel, Kronecker–Weyl). El punto
delicado señalado en el encargo — compatibilidad entre el conjunto de normalidad
(densidad 1−δ) y el de casi-períodos B² (densidad positiva) — se resuelve LIMPIO a
favor: la intersección tiene densidad positiva, no hace falta nada fino. La cadena
entrega, para cada ε > 0, sucesiones τ_k → ∞ dentro de los casi-períodos B² a lo
largo de las cuales ζ(·+iτ_k) converge uniformemente en D a un límite holomorfo g_ε.

### 4.2. El eslabón E5 muere: los soportes de las dos informaciones son disjuntos

Lo que sabemos del límite g_ε, exactamente:

**(α) De la convergencia uniforme en D:** información sobre ζ(s+iτ_k) para
s ∈ D — es decir, sobre los valores de ζ en los trasladados D + iτ_k. Alturas:
t ∈ W + τ_k.

**(β) De τ_k ∈ E_ε:** $\limsup_T \frac1T\int_0^T |\zeta(\sigma+it+i\tau_k) -
\zeta(\sigma+it)|^2 dt < \varepsilon^2$ — un promedio sobre TODO t ∈ [0,T], T → ∞.

La pregunta de identificación es: ¿(β) fuerza g_ε ≈ ζ en D? La respuesta es no, y la
razón es la Obs. 2.4 de D112 en forma afilada:

**Proposición 4.1 (la bondad B² no contiene ni un bit de información sobre la
ventana).** Sea τ ∈ E_ε. La condición τ ∈ E_ε es invariante ante modificar
ζ(σ+i·) — o su trasladado — en cualquier conjunto compacto de alturas t: la
seminorma B² asigna peso superior cero a todo compacto (D112, Obs. 2.4). En
particular, para el funcional que LP-112 necesita —
sup_{s∈D}|ζ(s+iτ)−ζ(s)|, soportado en alturas t ∈ W, compacto fijo — la pertenencia
τ ∈ E_ε no impone ninguna cota, ni siquiera en promedio sobre τ ∈ E_ε. ∎

Es decir: **la información (β) vive en el promedio global de t y pesa cero en W; la
identificación pedida vive enteramente en W.** Los soportes en la coordenada t de lo
que sabemos y de lo que necesitamos son disjuntos (módulo peso nulo). No es que la
estimación sea insuficiente: es que el certificado τ_k ∈ E_ε ∩ G_M es lógicamente
compatible tanto con g_ε = ζ|_D como con g_ε arbitrariamente lejos de ζ|_D.

**Y bajo H(m) la dirección está probada EN CONTRA (el mismo teorema de D112):** la
Prop. 2.6 de D112 se aplica verbatim al disco D anclado en el cero off-crítico: el
conjunto A_ε' = {τ : sup_D |ζ(s+iτ)−ζ(s)| ≤ ε'} tiene densidad superior cero para
ε' < η. Como E_ε ∩ G_M tiene densidad inferior positiva, **casi todo τ de la cadena
es malo**: la proporción de τ ∈ E_ε ∩ G_M ∩ [0,T] cuyos trasladados se acercan a
ζ|_D tiende a 0. Los límites g que la cadena "ve" genéricamente son los del soporte
de Bagchi — no-nulos en D (Hurwitz) — mientras ζ|_D se anula en ρ₀. La cadena
Montel+B² muere, pues, **exactamente en el mismo punto que D112 Prop. 2.6/Obs. 2.4**:
no en la compacidad (E1–E4 sobreviven), sino en que la única información disponible
para seleccionar τ es ciega — por definición de la seminorma — al lugar donde está la
señal. La combinación con normalidad no la salva: la normalidad agrega compacidad
(límites existen), no selección (cuál límite). D112 §2.3(c) ya lo había dicho en una
línea ("Montel garantiza límites, no identifica cuáles"); el análisis fino confirma
que no hay resquicio: el insumo B² aporta exactamente cero al eslabón E5.

### 4.3. Segundo punto de muerte, independiente: la explosión M(ε) → ∞

Aun si E5 tuviera un mecanismo parcial ("g_ε está a distancia φ(ε) de ζ en alguna
norma débil"), la diagonal ε → 0 enfrenta una no-uniformidad cuantitativa: la cota de
normalidad es M(ε) = 2c_R/d(ε), y d(ε) — la densidad de los casi-períodos B² — es
del orden (2η)^{π(X(ε))} con X(ε) ≍ ε^{−2/(2σ−1)} (D112, Lema 2.2): super-exponencialmente
pequeña en 1/ε. La familia {g_ε} no tiene cota uniforme cuando ε → 0; el conjunto de
límites accesibles crece sin control exactamente cuando la precisión pedida aumenta.
Esto no es el muro principal (E5 muere antes), pero clausura también la variante
"identificación aproximada + diagonal". GAP cuantitativo declarado: no probamos que
ninguna diagonal funcione — probamos que esta cadena no la alimenta.

### 4.4. El intento de re-anclaje por composición — y su colapso a D104 §5.4

Queda una idea genuina por auditar: la bondad B² de τ, aunque pese cero en la ventana
fija W, garantiza bondad puntual en MUCHAS ventanas (densidad positiva de alturas t
donde |ζ(σ+it+iτ) − ζ(σ+it)| es pequeño — por Chebyshev sobre la integral en (β)).
¿Se puede componer dos casi-períodos para arrastrar la bondad hacia W? Esquema: si τ
y τ' son buenos en una misma ventana móvil W₁ (existe por densidad positiva de
ambos conjuntos de alturas), entonces τ − τ' es un "casi-período local en W₁ + τ'".
Esto produce, incondicionalmente, pares (τ̃, ventana) con auto-aproximación local —
**en ventanas de posición no controlada**. Para LP-112 se necesita la ventana FIJA W
(la del cero). El mecanismo de composición traslada el evento, nunca lo ancla: la
posición de W₁ la elige la densidad (genérica), no el argumento. Este es exactamente
el colapso de la **ventana anclada** de D104 §5.4: la auto-aproximación "en alguna
parte" es barata (de hecho es esencialmente el contenido del teorema límite de
Bagchi); la auto-aproximación "aquí" tiene densidad demostrable exactamente cero. El
re-anclaje reproduce el muro, no lo esquiva. Verificado contra D104: misma
estructura, otra coordenada (pares de casi-períodos en lugar de la copia lenta
ζ(s+idτ)).

### 4.5. El lema exacto que falta: LP-113

La disección anterior deja un único enunciado faltante, y conviene dejarlo nombrado y
aislado:

**Lema LP-113 (anclaje del casi-período; ABIERTO).** *Sea W ⊂ ℝ una ventana compacta
fija y B ⊂ (½,1) un intervalo compacto de abscisas. Existe una sucesión ε_k → 0 y
casi-períodos τ_k ∈ E_{ε_k}, τ_k → ∞, cuya bondad se localiza en W:*
$$\int_W \sup_{\sigma \in B} |\zeta(\sigma+it+i\tau_k) - \zeta(\sigma+it)|^2\,dt
\;\longrightarrow\; 0$$
*(o la versión de área ∬_{B×W}, que basta: subarmonicidad la promueve a sup en
discos interiores, y Rouché hace el resto — D112 §2.3(b), "el localizador existe").*

Relaciones (todas con prueba inmediata dadas las piezas de D112): LP-113 ⟹ LP-112
(para discos D ⊂ interior(B×W); subarmonicidad + extracción); RH ⟹ LP-113 (la
recurrencia fuerte da densidad positiva de τ con bondad sup en B×W, que contiene la
versión integrada; y A_ε ∩ E_ε ≠ ∅ bajo RH por densidades); bajo H(m) los testigos de
LP-113 para la ventana del cero forman un conjunto de densidad superior cero (la
condición de LP-113 implica la de A_ε vía subarmonicidad, y Prop. 2.6 de D112
aplica). LP-113 no implica RH por los diccionarios conocidos (mismo análisis que
D112 §5.4: su conclusión bajo ¬RH es m = ∞, consistente). **LP-113 es la forma
destilada del mecanismo de selección no-genérica que falta: convertir bondad media
global (teorema, densidad positiva) en bondad localizada en UNA ventana prescrita
(densidad cero bajo la hipótesis a refutar).** No es RH-equivalente; es exactamente
la arista del cuantificador maestro de P43 que LP-112 ya exponía, ahora en coordenada
de ventanas en lugar de discos.

### 4.6. Dictamen de la cadena

**La cadena Montel+B² NO cierra LP-112 y NO muere en un punto nuevo: muere en D112
Prop. 2.6/Obs. 2.4** (eslabón E5, identificación), con un segundo bloqueo
independiente en la diagonal (§4.3) y con el re-anclaje colapsando a D104 §5.4
(§4.4). Sobrevive como programa solo en la forma del lema LP-113 — que es una
reformulación más localizada del mismo gap, no un camino hacia él. El valor del
análisis: (i) E1–E4 son teoremas y quedan registrados (la compacidad nunca fue el
problema); (ii) el gap queda reducido a su forma mínima — un solo eslabón, una sola
ventana, un solo bit de localización; (iii) queda demostrado que **ninguna mejora de
las estimaciones de E1–E4 puede cerrar E5**, porque E5 no es una estimación: es una
selección dentro de un conjunto que toda la maquinaria de E1–E4 clasifica como
excepcional.

---

## 5. Stepanov y Weyl: la salida estructural y su clausura por crecimiento

### 5.1. Las clases intermedias y la propiedad decisiva

Entre Bohr (uniforme) y Besicovitch (B², media global) están las clases de Stepanov y
Weyl (Besicovitch 1932, Cap. II; Levitan–Zhikov, *Almost Periodic Functions and
Differential Equations*, referencia estándar):
$$\|f\|_{S^p}^p = \sup_{x\in\mathbb{R}} \int_x^{x+1} |f(t)|^p\,dt, \qquad
\|f\|_{W^p}^p = \lim_{L\to\infty}\ \sup_{x\in\mathbb{R}} \frac1L\int_x^{x+L} |f(t)|^p\,dt,$$
con f S^p- (resp. W^p-) casi-periódica si es límite en esa norma de polinomios
trigonométricos (equivalentemente, casi-períodos relativamente densos en esa norma).

**La propiedad decisiva, y la razón por la que el encargo señala esta línea:** la
seminorma S² **no anula compactos** — el sup sobre la posición x de la ventana
incluye la ventana W del cero. Si ζ fuera S²-casi-periódica (en versión banda, ver
abajo) en una sub-banda de la franja, entonces para los casi-períodos S² la integral
local ∫_W |ζ(σ+it+iτ)−ζ(σ+it)|²dt estaría controlada EN LA VENTANA DEL CERO, la
subarmonicidad la promovería a sup en discos (D112 §2.3(b): "el localizador
funciona") y Rouché cerraría: **S²-c.p. en banda ⟹ LP-112 (de hecho, con
casi-períodos relativamente densos — más que LP-112).** El argumento de D112
Prop. 2.6 no obstruiría la prueba de la premisa, porque la Prop. 2.6 obstruye
certificados de tipo medio-global, y S² es medio-local. La pregunta entera se reduce
entonces a: ¿es ζ S²-casi-periódica en bandas de la franja?

### 5.2. Respuesta: no — teorema incondicional, por crecimiento

Primero la forma correcta del enunciado que Rouché necesita. La subarmonicidad
promueve **integrales de área**, de modo que la versión útil es la de banda: para
una banda cerrada B = [σ₁,σ₂] ⊂ (½,1), considérese ζ como función
t ↦ ζ(·+it) ∈ L²(B) y la norma de Stepanov vectorial
$$\|\zeta\|_{S^2(B)}^2 := \sup_{x} \int_x^{x+1}\!\!\int_{\sigma_1}^{\sigma_2}
|\zeta(\sigma+it)|^2\,d\sigma\,dt.$$

**Lema 5.1 (casi-periodicidad ⟹ acotación; estándar).** Si f es S^p-casi-periódica
(escalar o vectorial), entonces ‖f‖_{S^p} < ∞: f dista < ε de un polinomio
trigonométrico P en norma S^p, y ‖f‖ ≤ ε + ‖P‖ con ‖P‖_{S^p} < ∞. [Besicovitch
1932, Cap. II; inmediato de la definición de clausura.] ∎

**Teorema 5.2 (ζ no es S^p-casi-periódica en ninguna sub-banda de la franja; p ≥ 1,
incondicional).** Para toda banda B = [σ₁,σ₂] ⊂ (½,1) con σ₁ < σ₂,
‖ζ‖_{S^p(B)} = ∞; en particular ζ no es S^p(B)-casi-periódica.

*Demostración.* Sea σ ∈ (σ₁,σ₂) y r := min(σ−σ₁, σ₂−σ, ¼)/2 > 0. Incondicionalmente
(Ω-teoremas: [Tit86, Cap. VIII]; cuantitativo y con método de resonancia:
H. L. Montgomery, *Extreme values of the Riemann zeta function*, Comment. Math.
Helv. 52 (1977) [vía Aistleitner, verificado como referencia previa];
C. Aistleitner, *Lower bounds for the maximum of the Riemann zeta function along
vertical lines*, Math. Ann. 365 (2016), arXiv:1409.6035, verificado: para
α ∈ (½,1) fijo, max_{t≤T}|ζ(α+it)| ≥ exp(c_α (log T)^{1−α}/(log log T)^α)) existe
una sucesión t_n → ∞ con V_n := |ζ(σ+it_n)| → ∞. Por subarmonicidad de |ζ|^p (p ≥ 1;
|g|^p es subarmónica para g holomorfa):
$$V_n^p \;\le\; \frac{1}{\pi r^2} \iint_{D(\sigma+it_n,\,r)} |\zeta|^p\,dA
\;\le\; \frac{1}{\pi r^2} \int_{t_n-r}^{t_n+r}\!\!\int_{\sigma_1}^{\sigma_2}
|\zeta(\sigma'+it)|^p\,d\sigma'\,dt,$$
y como r < ½, el dominio temporal cabe en una ventana [x_n, x_n+1] con x_n = t_n − r:
$$\|\zeta\|_{S^p(B)}^p \;\ge\; \pi r^2\, V_n^p \;\longrightarrow\; \infty. \qquad\blacksquare$$

**Corolario 5.3.** La implicación de §5.1 (S²-banda-c.p. ⟹ LP-112) es correcta y
vacua: su premisa es falsa. La ruta de Stepanov está cerrada incondicionalmente — y
nótese el modo: no por el muro del cuantificador (densidad cero, selección), sino por
**crecimiento**, igual que Bohr uniforme (D112 §2.1(b)). Los valores grandes de ζ —
que existen incondicionalmente en toda recta de la franja — son incompatibles con
cualquier seminorma de casi-periodicidad que vea ventanas de tamaño fijo.

**Sobre la versión de recta única (no de banda):** si ζ(σ+i·) es S²-acotada en UNA
recta fija no se sigue del Teorema 5.2 (la subarmonicidad reparte la masa en un
entorno bidimensional, no en la recta misma), y no encontramos en la literatura
ningún trabajo sobre S²-casi-periodicidad de ζ en rectas de la franja (búsquedas:
"Stepanov almost periodic zeta function" y variantes — sin resultados pertinentes;
la conexión Bohr/zeta aparece solo vía la noción local-compacta de §2.1).
Estado declarado: GAP menor, abierto — **e irrelevante para LP-112**: Rouché necesita
control de área (banda), y la banda es falsa.

### 5.3. Weyl anula compactos otra vez

Para W^p el sup sobre x se toma ANTES del límite L → ∞, pero el límite gana: para
todo compacto K, sup_x (1/L)∫_{[x,x+L]} |f·1_K|^p ≤ ‖f·1_K‖^p_{L^p}/L → 0. La
seminorma de Weyl anula compactos exactamente como la de Besicovitch; un teorema de
W²-casi-periodicidad de ζ tendría el mismo defecto que el Lema 2.1 de D112 para
alimentar a Rouché. (Si acaso vale: el cálculo de Montgomery–Vaughan que da B² NO da
W² — el término de error (x+L)^{2−2σ}/L de la fórmula aproximada no es uniforme en x
para L fijo; estado de W² para ζ: abierto, no perseguido aquí — sin valor para
LP-112 por la ceguera a compactos.) GAP menor declarado.

### 5.4. La dicotomía de seminormas: el muro en otra coordenada

Resumen estructural de §5, que es un hallazgo del documento:

| seminorma | ¿ve compactos? | ¿ζ es c.p. en la franja? | qué la mata |
|---|---|---|---|
| Bohr (sup global) | sí | NO (teorema) | crecimiento (Ω) |
| Stepanov S^p, banda | sí | **NO (Teorema 5.2, nuevo aquí)** | crecimiento (Ω + subarmonicidad) |
| Weyl W^p | **no** (anula compactos) | abierto | (inútil para Rouché aunque valga) |
| Besicovitch B² | **no** (anula compactos) | SÍ (teorema, D112 Lema 2.1) | — (pero ciega donde está la señal) |

**Toda seminorma que ve los compactos es destruida por el crecimiento de ζ; toda
seminorma bajo la cual ζ es casi-periódica es ciega a los compactos.** La frontera
entre las dos familias es exactamente el tamaño de la ventana de promedio: ventana
fija ⟹ muere por crecimiento; ventana → ∞ ⟹ sobrevive y se ciega. No es un
accidente: los valores grandes de ζ en la franja (incondicionales) y los ceros
off-críticos hipotéticos viven en la misma escala de localización — una ventana fija
— y cualquier control que viera al cero vería también al valor grande y reventaría.
El trade-off crecimiento/localización es el muro de P43 expresado en teoría clásica
de casi-periodicidad, y explica con un solo criterio por qué TODAS las nociones
clásicas fallan para LP-112: las que localizarían el cero no admiten a ζ; las que
admiten a ζ no localizan nada.

---

## 6. Dinámica topológica: Birkhoff y la recurrencia de puntos individuales

**(a) Birkhoff directo sobre la órbita de ζ: no aplica por no-compacidad.** El
teorema de recurrencia de Birkhoff (todo flujo sobre un compacto no vacío tiene
puntos uniformemente recurrentes; todo punto de un sistema minimal compacto es
uniformemente recurrente) requiere compacidad. La órbita {ζ(·+iτ) : τ ≥ 0} ⊂
H(D(½,1)) con la topología compacto-abierta NO es relativamente compacta: la
compacidad relativa en H equivale (Montel) a acotación local uniforme, y
sup_τ sup_K |ζ(s+iτ)| = ∞ para todo compacto K de la franja con interior (Ω-teoremas
de nuevo). La clausura de la órbita no es compacta; Birkhoff no produce nada sobre
ella sin más.

**(b) Birkhoff/Poincaré sobre los objetos compactificados: produce recurrencia
GENÉRICA, no la de ζ.** Dos sustitutos estándar: (i) la medida de Bagchi Q es
invariante bajo el flujo vertical y la recurrencia de Poincaré da: Q-c.t. punto f de
supp Q es recurrente — c.t.p., genérico; ζ bajo ¬RH está fuera de supp Q (D112
Prop. 2.6) y la recurrencia c.t.p. no lo toca. (ii) En el toro de Kronecker Ω
(compacto, minimal, únicamente ergódico — D102 §7.1, E1–E3) TODO punto es
uniformemente recurrente, incluido ω₀ — incondicional. La transferencia de la
recurrencia de ω₀ a la de ζ requiere la continuidad de la observable de Euler Φ en
ω₀, y eso es exactamente MW-2/RH (D102, Prop. 7.2 y dictamen §7.3). Verificado
contra D102: la obstrucción de la órbita individual es la misma, sin residuo nuevo.

**(c) El estado del arte dinámico sobre "recurrencia de un punto distinguido":** los
teoremas de existencia de puntos recurrentes (Birkhoff vía Zorn/minimalidad;
Poincaré vía medida) son intrínsecamente no-constructivos Y genéricos: producen
recurrencia "en algún punto del minimal" o "en c.t. punto", jamás en un punto
prescrito de antemano de un sistema no compacto. La pregunta "¿es ζ punto recurrente
de su propio flujo de traslaciones?" ES LP-112 (con la observación de que Bagchi
1987 tituló su paper exactamente en estos términos), y la dinámica topológica no
tiene un solo teorema que certifique recurrencia de un punto individual no-genérico
sin compacidad de su órbita. Sin precedente en esta categoría — y con el diagnóstico
de D102 intacto: la categoría no es donde el problema se gana; es donde mejor se ve
por qué se pierde.

---

## 7. Síntesis comparativa: la posición exacta de LP-112

Tabla de enunciados ordenados por fuerza (de mayor a menor), con estatus y técnica o
muro. "⟸ RH" = implicado por RH; los enunciados 1–2 son equivalentes a (quasi-)RH.

| # | enunciado | estatus | técnica que lo prueba / muro que lo bloquea |
|---|---|---|---|
| 1 | Recurrencia fuerte SR_0 (densidad inferior positiva, todo K) | ⟺ RH (Bagchi 1987; precedente: Bohr 1922 para L(χ), densidad relativa) | ⟸: soporte pleno bajo RH (genericidad). ⟹: amplificador Rouché × densidad contra N(σ,T)=o(T) |
| 2 | C.p. local rel. densa de ζ en σ>σ₀ (σ₀<1) | ⟺ "ζ sin ceros en σ>σ₀" (§2.1(c), §2.6) | circular: probarla para algún σ₀<1 es quasi-RH |
| 3 | **LP-112** (sucesión τ_k → ∞, todo D; d = 0) | **ABIERTO**; ⟸ RH; ⟹ m∈{0,∞} (D112 Thm. 2.3); no ⟹ RH por diccionarios conocidos | muro: testigos de densidad cero bajo ¬RH (D112 Prop. 2.6); selección no-genérica (P43); **sin precedente** (§§2–6) |
| 4 | S²(banda)-c.p. de ζ en la franja [implicaría LP-112 y más] | **FALSO** (Teorema 5.2, incondicional) | muerto por crecimiento (Ω + subarmonicidad) |
| 5 | SR_d, d ≠ 0, ±1 (densidad positiva, dos velocidades) | TEOREMA incondicional (Nakamura 2010; Pańkowski; N–P 2012; P. 2015) | equidistribución relativa + Baker / seis exponenciales; degeneración d→0 cartografiada en D104 (escala lineal, ventana anclada en 0) |
| 6 | Auto-aproximación d=0 de ζ(s,α) (Hurwitz, α trasc. o racional ≠ ½,1) | TEOREMA incondicional (universalidad fuerte; G–K 2014) | soporte pleno = genericidad del punto; **no transferible a ζ: Euler comprime el soporte** |
| 7 | B²-c.p. de ζ en rectas de la franja (casi-períodos de densidad positiva) | TEOREMA incondicional (D112 Lemas 2.1–2.2) | momentos + Kronecker–Weyl; ciega a compactos (Obs. 2.4) |
| 8 | Bohr-c.p. uniforme de ζ en alguna recta σ ≤ 1 | FALSO (Ω-teoremas) | crecimiento |

**Respuesta a la pregunta (iii):** LP-112 NO queda entre dos enunciados probados.
Queda **estrictamente por encima de todo lo probado para ζ en d = 0** (los teoremas
7, y los 5–6 que viven en d ≠ 0 o en otra clase) y **estrictamente por debajo de los
RH-equivalentes** (1–2). En la banda intermedia que habita — enunciados puntuales
secuenciales para el punto diagonal d = 0 — la literatura no tiene ni un teorema, ni
un contraejemplo, ni una técnica candidata viva: las cuatro entradas que la
rodearían (3, 4, y las versiones secuenciales de 1–2) están, respectivamente,
abierta, refutada, y abiertas sin trabajo publicado. La asimetría con la frontera
d ≠ 0 es total: allí el insumo diofantino real (Baker, seis exponenciales) llega
exactamente hasta el borde; aquí no hay insumo que llegue a ninguna parte del
interior.

---

## 8. VEREDICTO sobre LP-112

**VEREDICTO: SIN PRECEDENTE.**

1. **No existe en la literatura ningún teorema de auto-aproximación secuencial sin
   recurrencia fuerte.** El inventario (§2, exhaustivo sobre las fuentes accesibles:
   survey de Matsumoto, la cadena Nakamura–Pańkowski–Garunkštis completa con su
   corrigendum y su preprint retirado, los equivalentes de 2025) muestra que todo
   resultado positivo conocido de auto-aproximación es de densidad (de medida o
   relativa) y se prueba por **genericidad del punto** — pertenencia al soporte de la
   estadística de shifts —, sea porque el soporte es pleno (Hurwitz, clases sin
   Euler: §3.1), sea porque hay equidistribución relativa que explotar (d ≠ 0:
   §2.3), sea bajo RH (d = 0: Bohr 1922, Bagchi 1987). El enunciado secuencial puro —
   certificar no-vacuidad donde la densidad puede ser cero — no tiene ni una
   instancia probada en ninguna clase de funciones, y en la categoría B² donde ζ
   tiene sus teoremas incondicionales el enunciado ni siquiera es una propiedad de la
   clase de equivalencia (§3.4).

2. **La técnica que LP-112 requiere queda especificada por la negativa:** un
   mecanismo de **selección no-genérica con anclaje** — producir un casi-período
   cuya bondad media global se localice en una ventana compacta prescrita (el lema
   LP-113, §4.5). Las tres candidatas auditadas mueren en puntos exactos y
   distintos: **Montel+B²** muere en la identificación del límite (eslabón E5,
   §4.2) — el mismo punto que D112 Prop. 2.6/Obs. 2.4, con la información B² y la
   información compacto-abierta de soportes disjuntos en t, y con el re-anclaje por
   composición colapsando a la ventana anclada de D104 §5.4; **Stepanov** — la única
   seminorma clásica que vería la ventana — muere por crecimiento, incondicionalmente
   (Teorema 5.2, nuevo aquí; la dicotomía de seminormas de §5.4: lo que localizaría
   el cero no admite a ζ, lo que admite a ζ no localiza); **Birkhoff/Poincaré** muere
   por no-compacidad de la órbita y genericidad de sus conclusiones, con la
   obstrucción reducida — sin residuo — a la discontinuidad de la observable de Euler
   en ω₀ (D102).

3. **¿Chance real de prueba incondicional con lo examinado? No con estas cadenas.**
   La cadena Montel+B² no cierra y no puede cerrar mejorando estimaciones: E1–E4 son
   teoremas y E5 no es una estimación sino una selección en un conjunto excepcional.
   Sobrevive como programa únicamente en la forma del lema **LP-113** (anclaje del
   casi-período), que es estrictamente más localizado que LP-112, está implicado por
   RH, no es RH-equivalente por los diccionarios conocidos (su conclusión bajo ¬RH es
   m = ∞, consistente — mismo análisis que D112 §5.4) — y cuyos testigos, bajo la
   hipótesis a refutar, forman exactamente el mismo conjunto de densidad cero. LP-113
   no es un avance hacia LP-112: es su forma mínima. El muro entre ambos y la
   literatura es el cuantificador maestro de P43, y este documento agrega su
   coordenada de seminormas (§5.4) y su certificado de no-precedencia (§§2–3) al
   expediente.

4. **Para la fase:** LP-112 queda confirmado como objetivo genuinamente nuevo — no
   hay teorema que adaptar, no hay técnica que importar, no hay clase puente donde
   ensayarlo (la única clase con auto-aproximación d = 0 probada la obtiene por
   soporte pleno, que ζ pierde por tener producto de Euler — la ironía estructural de
   §3.1). Si el programa decide atacarlo, el frente es LP-113 y la pregunta física
   subyacente es la del anclaje: qué propiedad aritmética de ζ — más fina que la
   independencia de {log p}, que ya está toda gastada en el Lema 2.2 de D112 — podría
   correlacionar la fase del flujo de Kronecker con una ventana prescrita del eje
   vertical. Hoy no hay candidato.

---

## Referencias

**Internas (backward-only):** Doc 112 (LP-112, Thm. 2.3, Prop. 2.6, Obs. 2.4, Lemas
2.1–2.2, §2.3, §5.4); Doc 111 (cosh-ejemplos; Obs. 2.4); Doc 109 (identidad
arquitectónica); Doc 104 (SR_d efectivo; ventana anclada §5.4; degeneración lineal);
Doc 102 (auditoría Bagchi; Prop. 7.2; §6.3 familia d; §7 observable de Euler);
P43 (Principio 3.1); P41 (Problema 8.1).

**Literatura (estatus de verificación indicado):**

- H. Bohr, *Über eine quasi-periodische Eigenschaft Dirichletscher Reihen mit
  Anwendung auf die Dirichletschen L-Funktionen*, Math. Ann. 85 (1922). [Enunciado
  verificado vía Herichi–Lapidus y exposiciones estándar; original NO VERIFICADO.]
- H. Bohr, *Zur Theorie der allgemeinen Dirichletschen Reihen*, Math. Ann. 79 (1918).
  (C.p. uniforme en semiplanos de convergencia absoluta; vía D112.)
- H. Bohr, E. Landau, Rend. Circ. Mat. Palermo 37 (1914). (Densidad o(T) off-crítica;
  vía D112.)
- B. Bagchi, tesis, Indian Statistical Institute, 1981; y *Recurrence in topological
  dynamics and the Riemann hypothesis*, Acta Math. Hungar. 50 (1987), 227–240.
  [Verificado vía Matsumoto/D102.]
- K. Matsumoto, *A survey on the theory of universality for zeta and L-functions*,
  arXiv:1407.4216 (2014). [Texto completo consultado en sesiones previas (D102);
  fuente maestra de §2.]
- S. M. Voronin, Izv. Akad. Nauk SSSR Ser. Mat. 39 (1975), 475–486. [Vía
  Matsumoto/D102.]
- T. Nakamura, *The generalized strong recurrence for non-zero rational parameters*,
  Arch. Math. 95 (2010), 549–555. [Verificado (Springer).]
- T. Nakamura, Ł. Pańkowski, corrigendum, Arch. Math. 99 (2012), 43–47;
  arXiv:1203.1393. [Verificado.]
- T. Nakamura, *A simple proof of the generalized strong recurrence for any non-zero
  parameter*, arXiv:1006.3184. [**Retirado por el autor** — verificado en arXiv;
  citado como dato de cartografía, no como resultado.]
- Ł. Pańkowski, *Self-approximation of Dirichlet L-functions*, arXiv:1006.1507.
  [Título y contenido verificados a nivel de abstract.]
- Ł. Pańkowski, *Joint universality and generalized strong recurrence with rational
  parameter*, arXiv:1503.06931. [Verificado: todo racional d ≠ 0, ±1.]
- T. Nakamura, Ł. Pańkowski, *Self-approximation for the Riemann zeta function*,
  Bull. Aust. Math. Soc. (2012/13). [Abstract verificado vía Cambridge Core; volumen
  y páginas NO VERIFICADOS.]
- R. Garunkštis, E. Karikovas, *Self-approximation of Hurwitz zeta-functions*,
  Funct. Approx. Comment. Math. 51 (2014), 181–188. [Verificado (Project Euclid).]
- J. Andersson, R. Garunkštis, R. Kačinskaitė et al., *On self-approximation of the
  Riemann zeta function in short intervals*, Symmetry 17 (2025), art. 2075. [Existencia
  y tesis principal verificadas vía buscador; texto completo NO VERIFICADO (403);
  lista de autores parcialmente verificada.]
- A. Laurinčikas, *On equivalents of the Riemann hypothesis connected to the
  approximation properties of the zeta-function*, Axioms 14 (2025), 169. [Verificado
  a nivel de abstract.]
- A. Reich, *Werteverteilung von Zetafunktionen*, Arch. Math. 34 (1980). [Vía
  Matsumoto; original NO VERIFICADO.]
- A. Laurinčikas, *Limit Theorems for the Riemann Zeta-Function*, Kluwer, 1996.
  (Aparato de Bagchi; vía D112.)
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed., Oxford, 1986.
  (Thm. 7.2; Cap. VIII: Ω-teoremas.)
- H. L. Montgomery, *Extreme values of the Riemann zeta function*, Comment. Math.
  Helv. 52 (1977). [Citado como precedente del resultado de Aistleitner, según el
  propio Aistleitner; original NO VERIFICADO.]
- C. Aistleitner, *Lower bounds for the maximum of the Riemann zeta function along
  vertical lines*, Math. Ann. 365 (2016); arXiv:1409.6035. [Verificado: abstract y
  enunciado principal.]
- A. S. Besicovitch, *Almost Periodic Functions*, Cambridge, 1932. (Clases S^p, W^p,
  B^p, Cap. II; c.p. ⟹ acotación en la norma respectiva.)
- B. M. Levitan, V. V. Zhikov, *Almost Periodic Functions and Differential
  Equations*, Cambridge, 1982. [Referencia estándar para las clases de Stepanov/Weyl;
  no load-bearing.]
- H. Herichi, M. L. Lapidus, *Truncated infinitesimal shifts, spectral operators and
  quantized universality of the Riemann zeta function*, arXiv:1305.3933. [Fuente
  secundaria verificada del enunciado de Bohr 1922.]
- B. Jessen, H. Tornehave, Acta Math. 77 (1945). (Teoría de medias de ceros de
  funciones c.p.; vía D112 §6.2.)
- H. Davenport, H. Heilbronn, J. London Math. Soc. 11 (1936). (Vía D112.)
- H. Montgomery, R. Vaughan, J. London Math. Soc. (2) 8 (1974). (Vía D112.)

*Fin del Documento 113.*
