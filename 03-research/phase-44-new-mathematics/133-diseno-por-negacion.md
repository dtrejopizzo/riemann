# Doc 133 — Diseño por negación: los objetos que violan los no-go del programa

**Programa:** Hipótesis de Riemann — Phase 44, "matemática nueva"
**Fecha:** junio 2026
**Autor:** David Alejandro Trejo Pizzo
**Prerrequisitos:** Doc 110 (Teorema 4.3: imposibilidad en la clase ℱ; Prop. 4.5: contraejemplo de rango finito; axiomas L1–L6), Doc 113 (dicotomía de seminormas §5.4; Teorema 5.2; cadena Montel+B² §4; LP-113), Doc 102 (obstrucción de la órbita individual; Prop. 7.2; observable de Euler), Doc 112 (LP-112, Thm. 2.3, Prop. 2.6, Obs. 2.4), Doc 108 (dicotomía sub-resolución/resolución; Teoremas 3.3, 3.4; Prop. 2.3, 2.5), Doc 106 (identidad tensorial del índice), P43 (cuantificador maestro, valor/inercia).
**Contrato creativo de la fase:** **[DEFINICIÓN-NUEVA]** = libertad total; **[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado de verdad, prueba completa o estatus declarado línea por línea; **[PUENTE]** = conexión con ζ/RH con estatus honesto; **[DESEO]** = declarado como deseo. Ninguna prueba se fabrica; todo insumo externo o interno se cita; los GAPs se marcan.

---

## 0. Resumen ejecutivo

El método de este documento es el de Schwartz y Robinson: un teorema de imposibilidad
con hipótesis explícitas no es una lápida — es un plano de diseño. Las distribuciones
nacieron violando "toda derivada de una función es una función"; los infinitesimales
no-estándar, violando "todo cuerpo ordenado arquimediano completo es ℝ"; los espacios
no conmutativos, violando "todo espacio es su álgebra de funciones conmutativa". En
cada caso el objeto nuevo viola exactamente UNA hipótesis y conserva el contacto con
el problema original. El programa probó tres no-go con hipótesis numerables. Acá se
construyen los tres objetos violadores y sus primeros teoremas.

1. **(§2, contra NO-GO 1 — imposibilidad de la clase ℱ, Doc 110 Thm. 4.3.)**
   Hipótesis violada: la **arquimedianidad del grupo de valores** del índice (I toma
   valores en ℤ, donde "cota uniforme finita" = "cota por un entero estándar" = RH).
   Objeto: la **signatura infinitesimal** σ_ε — el índice negativo por ventana,
   leído como elemento de la ultrapotencia *ℤ y normalizado por la dimensión, con
   parte estándar en [0,1]. Teoremas probados: buena definición (Thm. 2.6); escape
   del Teorema 4.3 — el cuerno (b) de la dicotomía colapsa porque en *ℤ existe la
   cota no-arquimediana trivial κ* ≤ n* y σ_ε se define sin peaje (Thm. 2.7);
   autonomía por ventana — cada κ_N es computable desde los primos por
   Newton/Jacobi–Frobenius porque la ventana es de rango finito a priori (Prop. 2.8,
   apoyada en D110 Prop. 4.5 + P43 autonomía del valor); y la **ley logística de la
   torre tensorial** (Thm. 2.10, exacta, con forma cerrada):
   σ^(k) = ½(1 − (1−2σ⁰)^{2^k}). Puente (§2.5): RH ⟺ la torre tiende a 0;
   ¬RH (módulo el caveat de realizabilidad de D108) ⟺ la torre tiende a ½. **La
   precisión o(1/log T) del muro de segundo orden se transmuta en una separación
   macroscópica 0 vs ½** — el muro reaparece como la no-efectividad de la parte
   estándar (un Π₁ nuevo), pero cada evento es ahora álgebra lineal finita de datos
   aritméticos. Es la transmutación más favorable registrada en el programa.

2. **(§3, contra NO-GO 2 — dicotomía de seminormas, Doc 113 §5.4.)** Hipótesis
   violada: **homogeneidad + subaditividad** (ser seminorma), que es lo que convierte
   casi-periodicidad en acotación (D113 Lema 5.1) y deja a Ω-teoremas matar al
   detector. Objeto: el **detector cordal** Δ_D — la métrica esférica de ℂ̂ aplicada
   en compactos. Teoremas probados: Δ_D ve compactos Y es indestructible por
   crecimiento (acotado por 1) — ambos cuernos de la dicotomía fallan (Thm. 3.4);
   en un compacto fijo la recurrencia cordal equivale a la euclídea con constantes
   explícitas (Thm. 3.5) — el poder de detección se conserva; y el **espejo de
   Marty** (Thm. 3.7, incondicional, vía universalidad de Voronin): la derivada
   esférica de ζ es no acotada sobre la órbita en todo disco de la franja —
   sup_τ ζ#(s+iτ) = ∞. Puente: el detector sobrevive pero la compacidad de Marty
   muere donde moría la acotación de Stepanov: **el crecimiento del valor se
   transmuta en crecimiento de la derivada esférica**. La dificultad reaparece un
   nivel de derivada más arriba; el eslabón E5 (selección) queda intacto.

3. **(§4, contra NO-GO 3 — obstrucción de la órbita individual, Doc 102 §7.)**
   Hipótesis violada: la **topología producto del toro de Bohr** (la que da
   compacidad/minimalidad/unicidad ergódica y bajo la cual Φ es discontinua
   exactamente en ω₀). Objeto: la **topología aritmética** 𝒯_ar, generada por las
   pseudométricas d_D de convergencia uniforme-en-truncación de las sumas parciales
   de Euler. Teoremas probados: 𝒯_ar es estrictamente más fina que la producto
   (Lema 4.4); (Ω, 𝒯_ar) NO es compacto — prueba de una línea por
   compacto-a-Hausdorff (Lema 4.5); y el teorema de disolución del punto excepcional
   (Thm. 4.6, con prueba completa): la familia de observables truncadas
   {log ζ_X}_X es **uniformemente d_D-equicontinua en TODO ω, uniformemente en X** —
   en 𝒯_ar, ω₀ no es excepcional; la observable es tan regular en el punto
   aritmético como en cualquier otro. Precio probado: la compacidad — y con ella
   toda la dinámica incondicional (E1–E3 de D102) — se pierde. Teorema de
   transferencia (Thm. 4.8): 𝒯_ar-recurrencia de ω₀ + anclaje de colas ⟹ LP-112 ⟹
   m ∈ {0,∞}. Puente: **transmutación total** — la discontinuidad de Φ se convierte,
   exactamente y sin residuo, en la no-compacidad de Ω más el problema de las colas
   (MW-2 en coordenada de truncaciones). Información nueva sobre el muro: la
   obstrucción nunca fue la topología; es un presupuesto conservado entre
   (continuidad de la observable) y (recurrencia gratuita del punto).

**Ranking (§5):** signatura infinitesimal ≻ detector cordal ≻ topología aritmética.
**Siguiente teorema a atacar (§5.2):** la realizabilidad test-accesible de la cota
inferior σ⁰ ≥ c_m bajo ¬RH (cerrar el caveat "Hipótesis D" de D108 Lema 2.4 para la
familia de ventanas por supremo) — es el único eslabón citado-no-probado entre la
torre logística y la equivalencia limpia RH ⟺ lim σ^(k) = 0.

---

## 1. El método: negación quirúrgica

### 1.1. Protocolo

Para cada no-go N con hipótesis H₁,…,H_r:

1. **[EXTRACCIÓN]** Enumerar las hipótesis y verificar, prueba en mano, que cada una
   es load-bearing: ¿qué paso de la demostración del no-go la usa? ¿El no-go
   sobrevive si se la quita?
2. Elegir la hipótesis MÁS DÉBIL cuya negación no rompa el contacto con la
   aritmética (el objeto violador debe seguir alimentándose de primos, polo y factor
   gamma — si no, es un juguete).
3. **[DEFINICIÓN-NUEVA]** Definir el objeto que la viola. La definición es libre;
   la disciplina empieza en el punto 4.
4. **[TEOREMA]** Probar: (i) buena definición; (ii) que el enunciado del no-go es
   FALSO para el objeto (o que sus hipótesis no lo alcanzan, con el paso exacto de
   la prueba vieja que se rompe); (iii) al menos una propiedad sustantiva.
5. **[PUENTE]** Aplicarlo a ζ y rastrear la transmutación (patrón Doc 99): si la
   dificultad reaparece, decir DÓNDE — cada reaparición es información nueva sobre
   el muro.

### 1.2. La vara histórica

El precedente exacto que se imita: Robinson no probó más teoremas de análisis que
Weierstrass — probó que el cuerpo ordenado no-arquimediano *ℝ existe, es
conservativo, y que en él ciertos enunciados imposibles (un h > 0 menor que todo
1/n) son triviales; la ganancia fue de EXPRESIVIDAD, y de ahí salieron teoremas
nuevos (Bernstein–Robinson sobre subespacios invariantes). El criterio de éxito de
este documento es el mismo: el objeto violador vale si (a) sus primeros teoremas
son demostrables hoy, y (b) re-expresa el muro en coordenadas donde algo que antes
era invisible se vuelve enunciable. No se promete cruzar el muro: se promete
construir el cuarto desde el cual se lo ve de frente.

---

## 2. NO-GO 1: la imposibilidad de la clase ℱ, negada por no-arquimedianidad

### 2.1. [EXTRACCIÓN] Las hipótesis del Teorema 4.3 de D110

El enunciado (D110, §4.2): *ningún I ∈ ℱ satisface (L2)+(L3)+(L4)*, donde ℱ es la
clase de invariantes I = neg.ind(Q|_{V′}) con Q de tipo fórmula explícita y V′
test-accesible. Hipótesis desplegadas:

- **H1 (forma del invariante):** I es UN índice negativo clásico,
  I = neg.ind(Q|_{V′}) ∈ ℤ_{≥0} ∪ {∞}.
- **H2 (grupo de valores arquimediano):** el valor de I vive en ℤ (o un grupo
  discreto arquimediano): "I acotado" significa "I ≤ C para un entero estándar C".
- **H3 (test-accesibilidad):** V′ se especifica sin posiciones de ceros.
- **H4 (rango no acotado a priori):** en el régimen de resolución, dim V′ → ∞ con
  la ventana (no hay finitud L6).
- **H5 (Q de tipo fórmula explícita):** lado espectral = ceros, lado aritmético =
  bloques computables.

**¿Cuál es load-bearing y dónde?** La prueba de D110 Thm. 4.3 es la dicotomía de
D108: (a) sub-resolución ⟹ I = 0 (no detecta: viola L3); (b) resolución ⟹ I es
binario por ventana — 0 bajo RH, ≍ m·n_W bajo ¬RH — y entonces *cualquier cota
uniforme finita sobre I equivale a RH* (viola L4), o la compresión al bloque
relativo usa posiciones (viola L2); (c) no hay tercer régimen porque la evaluación
exige precisión relativa o(1/log T).

- Quitar H3 mata el teorema trivialmente (el bloque off×off comprimido por
  posiciones tiene índice 8m², D108 §2.4): no interesa — perder H3 es perder el
  contacto con lo computable.
- Quitar H5 mata el contacto con la aritmética: no interesa.
- Quitar H4 mata el teorema (D110 Prop. 4.5: en rango finito a priori la inercia ES
  autónoma — Newton/Jacobi–Frobenius): esta es la puerta que D110 §4.4 ya señaló
  ("el lector es un teorema de finitud"), pero el teorema de finitud (L6 global,
  la cohomología de Weil de Spec ℤ) no está al alcance de un acto de definición:
  no se puede DEFINIR la finitud global de un objeto que no la tiene.
- **Quitar H2 — y este es el hallazgo de la extracción — desarma el cuerno (b) sin
  tocar nada más.** El paso "(b): cualquier cota uniforme finita sobre I es
  lógicamente equivalente a RH (D108 Prop. 2.5), violando L4" usa que una cota es
  un ENTERO ESTÁNDAR: la familia {I_W}_W de índices por ventana, no acotada bajo
  ¬RH, no admite techo en ℤ — y la inexistencia de techo estándar es lo que hace
  inconsistente a L4. En un anillo ordenado no-arquimediano la familia SÍ admite
  techo (un elemento ilimitado), la noción "acotado" se bifurca en
  "limitado/ilimitado", y el invariante puede definirse SIN afirmar jamás una cota
  estándar. La prueba del no-go no sobrevive: usa la arquimedianidad en el único
  punto donde convierte estabilidad en RH.

H2 es además la hipótesis más débil en el sentido del protocolo: negarla no toca
los datos aritméticos (H5), ni la accesibilidad (H3), ni pretende la finitud global
que no existe (H4 se esquiva *por ventana*, donde la finitud es real y gratuita).

### 2.2. [DEFINICIÓN-NUEVA] El índice no-estándar y la signatura infinitesimal

Fijamos de una vez: 𝒰 un ultrafiltro no principal sobre ℕ; *ℝ := ℝ^ℕ/𝒰 la
ultrapotencia (cuerpo ordenado no-arquimediano real-cerrado; Robinson 1966),
*ℤ ⊂ *ℝ los enteros no-estándar. Un elemento x ∈ *ℝ es **limitado** si |x| ≤ n
para algún n ∈ ℕ estándar; st: {limitados} → ℝ es la parte estándar (homomorfismo
de anillos ordenados sobre los limitados; existe por completitud de ℝ). Notación:
[a_N] = clase de la sucesión (a_N)_N.

**Definición 2.1 (esquema de ventanas test-accesible).** Un *esquema* es una
sucesión 𝒮 = (V_N)_{N≥1} de subespacios de dimensión finita del espacio de tests
de una forma Q de tipo fórmula explícita (D110, Def. 4.2(i)), tal que: (i) cada
V_N está especificado por soportes, ventanas de altura y anchos de banda
únicamente — sin posiciones de ceros (test-accesible, D108 Def. 1.2); (ii)
n_N := dim V_N → ∞; (iii) n_N es computable desde la especificación. Ejemplo
canónico (el que se usa en §2.5): V_N = suma de los espacios de tests de
resolución (soporte a ≍ log T_N, banda en ventana W) sobre TODAS las ventanas W
de una grilla finita test-accesible de altura ≤ T_N := 2^N, y
Q_N := Q|_{V_N}. Para el índice tomamos el máximo de la grilla:
κ_N := max_{W ∈ grilla(N)} neg.ind(Q|_{V_W}) y n_N := dim V_W (común por diseño
de la grilla). El máximo sobre una familia finita especificada sin ceros es
test-accesible: no se elige ninguna ventana usando un cero.

**Definición 2.2 (índice no-estándar).** El *índice no-estándar* del esquema es
$$\kappa^*(\mathcal{S}) := [\,\kappa_N\,] \in {}^*\mathbb{Z}_{\geq 0},
\qquad n^* := [\,n_N\,] \in {}^*\mathbb{Z}_{>0}.$$

**Definición 2.3 (signatura infinitesimal).** La *signatura infinitesimal* del
esquema es
$$\sigma_\varepsilon(\mathcal{S}) := \mathrm{st}\!\left(\frac{\kappa^*}{n^*}\right)
\in [0,1].$$
(El cociente es limitado porque 0 ≤ κ_N ≤ n_N para todo N: el índice negativo de
una forma sobre un espacio de dimensión n_N es ≤ n_N. La parte estándar existe.)

**Definición 2.4 (torre tensorial).** Para cada N sea Q̄_N la forma inducida en
V_N/rad(Q_N) (no degenerada), de signatura (p_N, q_N), p_N + q_N = n̄_N,
q_N = κ_N (el radical no aporta direcciones negativas). La *torre* es la sucesión
de formas Q̄_N^{⊗2^k} sobre (V_N/rad)^{⊗2^k}, k = 0, 1, 2, …, con
$$x_k(N) := \frac{\operatorname{neg.ind}\big(\bar Q_N^{\otimes 2^k}\big)}{\bar n_N^{\,2^k}},
\qquad
\sigma^{(k)} := \mathrm{st}\big([\,x_k(N)\,]\big).$$

**Observación 2.5 (qué es nuevo en la definición).** Tres cosas, y conviene
separarlas. (1) El paso a *ℤ no es decoración: lim sup_N κ_N/n_N no es
multiplicativo y no soporta el cálculo tensorial de §2.4; st a lo largo de 𝒰 es un
homomorfismo de anillos y lo soporta — la maquinaria de Robinson es load-bearing.
(2) σ_ε depende a priori de 𝒰; cuando κ_N/n_N converge, no depende (st = límite);
los teoremas de abajo valen para TODO 𝒰, que es la forma correcta de la
robustez. (3) El objeto NO está en ℱ: no es neg.ind(Q|_{V′}) para ningún V′ único
— es un germen de índices por ventana con valores en un anillo no-arquimediano.
H1 y H2 quedan violadas; H3, H4(por ventana), H5 se conservan.

### 2.3. [TEOREMA] Primeros teoremas del objeto

**Teorema 2.6 (buena definición y trivialidad del peaje).** Para todo esquema 𝒮 y
todo ultrafiltro no principal 𝒰: (a) κ* ∈ *ℤ y σ_ε ∈ [0,1] están bien definidos;
(b) vale la cota no-arquimediana κ* ≤ n* en *ℤ, incondicionalmente; (c) si el
esquema es anidado por ventana fija (V_N ⊆ V_{N+1} dentro de una misma ventana),
κ_N es monótona no decreciente y entonces σ_ε no depende de 𝒰 sobre esa
subfamilia.

*Demostración.* (a) Cocientes de sucesiones bien definidos en la ultrapotencia;
0 ≤ κ_N ≤ n_N da limitación; st existe sobre limitados (completitud de ℝ; Robinson
1966, cap. 2 — hecho estándar de ultrapotencias, no se reproduce). (b) Coordenada a
coordenada: κ_N ≤ n_N; la desigualdad pasa al cociente por Łoś. (c) Si V ⊆ V′,
todo subespacio negativo de Q|_V lo es de Q|_{V′}: neg.ind no decrece; una
sucesión monótona acotada en [0,1] tras normalizar converge, y st de una sucesión
convergente es su límite, para todo 𝒰. ∎

**Teorema 2.7 (violación del NO-GO 1: el Teorema 4.3 no alcanza a σ_ε).** El
enunciado de imposibilidad de D110 Thm. 4.3 es falso para la signatura
infinitesimal, en el sentido preciso siguiente: σ_ε satisface los análogos
(L2′) *autonomía*: cada coordenada κ_N es computable desde datos aritméticos sin
posiciones de ceros (Prop. 2.8); (L3′) *detección*: bajo RH σ_ε = 0 para todo
esquema; bajo ¬RH existe un esquema test-accesible con σ_ε > 0 [estatus de esta
mitad: §2.5, módulo el caveat de realizabilidad de D108]; (L4′) *estabilidad sin
peaje*: σ_ε está definida para todo esquema sin afirmar ninguna cota estándar
uniforme sobre los κ_N — el paso de la prueba vieja que convertía estabilidad en
RH no se aplica.

*Demostración de (L4′), que es el punto.* El cuerno (b) de D110 Thm. 4.3 deriva la
inconsistencia así: "o bien I se define como índice por ventana — y cualquier cota
uniforme finita sobre I es lógicamente equivalente a RH (D108 Prop. 2.5), violando
(L4)". La premisa implícita: para que el invariante-familia {κ_W} sea un OBJETO
único hace falta un techo común, y en ℤ un techo común es un entero estándar, cuya
existencia es RH. En *ℤ el techo común existe incondicionalmente y es gratuito:
κ* ≤ n* (Thm. 2.6(b)) — un elemento ilimitado de *ℤ es un objeto legítimo del
anillo de valores, no una patología. La definición de σ_ε consume únicamente esa
cota no-arquimediana y la limitación del cociente; en ningún paso se afirma
"κ_N ≤ C estándar", de modo que la equivalencia de D108 Prop. 2.5 nunca se invoca.
El cuerno (a) (sub-resolución ⟹ índice 0) no obstruye: en esquemas de resolución
σ_ε se define igual. El cuerno (c) (evaluación con precisión o(1/log T)) se
re-examina en §2.5: la afirmación allí es sobre la evaluación de I ∈ ℱ por
ventana; σ_ε desplaza la evaluación a una separación macroscópica (0 vs ½ en la
torre), lo cual no refuta (c) — lo esquiva cambiando qué hay que evaluar. ∎

**Proposición 2.8 (autonomía coordenada a coordenada: el contraejemplo de rango
finito, activado).** Cada κ_N es computable desde los datos aritméticos (primos,
polo, factor gamma) sin posiciones de ceros, mediante un procedimiento algebraico
exacto y finito.

*Demostración.* Dos insumos. (1) *Autonomía del valor* (P43, Thm. 4.2
"valor autónomo"; D107): para tests f, g del espacio del programa, Q(f,g) es
computable desde los bloques aritméticos de la fórmula explícita — los términos
mixtos ceros×primos se reabsorben y el bloque primos×primos es el funcional de
casi-primos; ninguna posición de cero entra. (2) *Rango finito a priori*: V_W
tiene dimensión n_W fijada por la especificación (soportes y bandas), no por
ceros. Entonces la matriz de Gram G_W = (Q(f_i, f_j))_{i,j≤n_W} en cualquier base
test-accesible de V_W es una matriz hermitiana de entradas computables; su número
de autovalores negativos — κ(Q|_{V_W}) — se computa exactamente por el método de
D110 Prop. 4.5: identidades de Newton sobre las trazas tr(G_W^j), j ≤ n_W, y
lectura de la signatura por Jacobi–Frobenius ([Gan59, Vol. 2, Cap. X]); o,
directamente, por el algoritmo de congruencia de Lagrange–Sylvester sobre G_W
(diagonalización por congruencia, exacta en aritmética de los coeficientes). El
máximo sobre la grilla finita es computable. ∎

**Observación 2.9 (qué reconcilia esto con "la inercia no es autónoma").** No hay
contradicción con P43 Thm. autonomy ni con D108 §7.4: lo no-autónomo es la
PARTICIÓN del índice en bloques off×off / off×on — el dato que un lector de
inercia tipo Forma B necesitaba. κ_N es el índice TOTAL de la restricción, sin
partición: ese siempre fue autónomo en rango finito (es el contraejemplo D110
Prop. 4.5, que el programa había clasificado como "abstracto"). La definición 2.2
lo convierte en estructural: no necesitamos la partición, porque la detección no
se hará separando bloques sino iterando la torre (Thm. 2.10) — la contaminación
off×on, que era el veneno de la partición, es exactamente lo que la cota inferior
κ_W ≳ m·n_W de D108 explota a favor.

**Teorema 2.10 (ley logística de la torre tensorial; exacta).** Sea (p, q)
la signatura de una forma hermitiana no degenerada Q̄ sobre un espacio de
dimensión n̄ = p + q, y sea x_k := neg.ind(Q̄^{⊗2^k})/n̄^{2^k}. Entonces, para
todo k ≥ 0, como identidad de números racionales:
$$x_{k+1} = 2x_k(1 - x_k), \qquad\text{y en forma cerrada}\qquad
1 - 2x_k = (1 - 2x_0)^{2^k}.$$
En consecuencia, para todo esquema 𝒮 y todo 𝒰, con σ⁰ := st([x_0(N)]):
$$\sigma^{(k)} = \tfrac12\Big(1 - \big(1 - 2\sigma^0\big)^{2^k}\Big),$$
y la torre tiene exactamente dos límites posibles:
$$\lim_{k\to\infty} \sigma^{(k)} =
\begin{cases} 0, & \sigma^0 \in \{0, 1\},\\[2pt] \tfrac12, & \sigma^0 \in (0,1).\end{cases}$$

*Demostración.* Identidad tensorial del índice para formas no degeneradas de
dimensión finita (Doc 106; P43 ledger L3): neg.ind(Q₁⊗Q₂) = p₁q₂ + q₁p₂, y la
parte positiva es p₁p₂ + q₁q₂. Para Q̄^{⊗2^{k+1}} = (Q̄^{⊗2^k}) ⊗ (Q̄^{⊗2^k}),
con signatura (P_k, K_k), P_k + K_k = n̄^{2^k}:
$$K_{k+1} = 2 P_k K_k, \qquad P_{k+1} = P_k^2 + K_k^2.$$
Dividiendo por n̄^{2^{k+1}} = (n̄^{2^k})²: x_{k+1} = 2(P_k/n̄^{2^k})(K_k/n̄^{2^k})
= 2(1−x_k)x_k. Forma cerrada: 1 − 2x_{k+1} = 1 − 4x_k + 4x_k² = (1 − 2x_k)²;
iterando, 1 − 2x_k = (1 − 2x_0)^{2^k}. Paso a σ: cada x_k(N) ∈ [0,1] es limitado;
st es homomorfismo de anillos sobre los limitados, así que la identidad polinomial
1 − 2x_{k+1} = (1 − 2x_k)² pasa a las partes estándar para cada k fijo (k es
estándar; la identidad se usa finitas veces). Límites: si σ⁰ ∈ (0,1),
|1 − 2σ⁰| < 1 y (1−2σ⁰)^{2^k} → 0, luego σ^(k) → ½. Si σ⁰ = 0, σ^(k) ≡ 0. Si
σ⁰ = 1 (forma asintóticamente definida negativa), 1 − 2σ⁰ = −1 y (−1)^{2^k} = 1
para k ≥ 1: σ^(k) = 0 — coherente: el cuadrado tensorial de una forma definida
negativa es definido positivo. ∎

**Proposición 2.11 (ejemplo sustantivo de calibración).** (a) Esquema juguete con
κ_N = ⌊αn_N⌋, α ∈ (0,1) fijo: σ⁰ = α y σ^(k) = ½(1 − (1−2α)^{2^k}) → ½; con
α = α_N → 0 pero α_N n_N → ∞: σ⁰ = 0 y la torre es idénticamente 0 — la signatura
infinitesimal NO ve defectos de densidad relativa nula, que es exactamente la
escala correcta: distingue "proporción positiva de direcciones negativas" de
"o(n) direcciones", no pretende ver eventos o(1/log T) por coordenada. (b) Para
la forma de Weil bajo RH: Q ≥ 0 sobre C_c^∞ (Weil 1952, normalización del
programa: D110 §3.2(a)) ⟹ κ_N = 0 para todo esquema ⟹ σ⁰ = 0 y la torre es 0:
la rama RH del puente es teorema sin caveats.

*Demostración.* (a) Cálculo directo con Thm. 2.10; la segunda parte: x_0(N) =
⌊α_N n_N⌋/n_N → 0 ⟹ st = 0 para todo 𝒰. (b) Restricción de una forma
semidefinida positiva: sin autovalores negativos en ninguna Gram finita. ∎

**[DESEO 2.12].** Que exista una "razón local" (axioma L5 de D110) que anule cada
κ_N — un teorema de positividad por ventana con mecanismo uniforme. La torre no lo
da; lo que da es que la AUSENCIA de esa razón se mediría en una constante
macroscópica, no en una precisión asintótica.

### 2.4. [PUENTE] Qué da sobre ζ, y dónde reaparece el muro

**Teorema-puente 2.13 (dicotomía logística para ζ; estatus mixto, declarado).**
Sea 𝒮* el esquema canónico de la Def. 2.1 (grilla de ventanas por supremo, tests
de resolución de D108). Entonces:

(a) **[TEOREMA]** Bajo RH: σ⁰(𝒮*) = 0 y lim_k σ^(k) = 0. (Prop. 2.11(b).)

(b) **[CITADO-CONDICIONAL — el caveat heredado]** Bajo ¬RH con m ≥ 1 cuádruplo
off-crítico: D108 (Prop. 2.3 + Lema 2.4 + Prop. 2.5) da, para la ventana ALINEADA
con el cero a escala de resolución, índice ≥ c·m·n_W con c > 0 absoluto; como la
grilla de 𝒮* contiene una ventana a distancia o(1) de la alineada en cada escala,
κ_N ≥ c′·m·n_N a lo largo de una subsucesión cofinal en 𝒰 adecuado, de donde
σ⁰ ≥ c′m > 0 y lim_k σ^(k) = ½. **Estatus:** la cota inferior por ventana alineada
está probada en D108 en el juguete bajo Hipótesis D y para las realizaciones del
programa con m = 1; la extensión a m general y la estabilidad bajo el
desplazamiento o(1) de la grilla son el GAP declarado de D108 (su Lema 2.4 de
realizabilidad). No se afirma teorema; se afirma: *si* la realizabilidad de D108
vale, *entonces* la dicotomía es completa.

(c) **[COROLARIO de (a)+(b), con el estatus de (b)]**
$$\mathrm{RH} \iff \lim_{k\to\infty} \sigma^{(k)}(\mathcal{S}^*) = 0
\iff \lim_k \sigma^{(k)} \neq \tfrac12.$$

**Rastreo honesto de la transmutación.** Comparemos con el inventario del
cuantificador maestro (P43, Principio 3.1) coordenada por coordenada:

1. *Lo que era:* certificar RH vía índices exigía una cota uniforme estándar
   (= RH, circular) o evaluar Π con precisión relativa o(1/log T) por ventana
   (D108 ec. 4.1; D110 Lema 2.4(b): el mismo o(1/log T) del enrollamiento). La
   señal era de segundo orden contra un término principal (log T)².
2. *Lo que es:* certificar RH vía la torre exige distinguir lim_k σ^(k) = 0 de
   lim_k σ^(k) = ½ — dos constantes macroscópicas separadas por ¼ ya en el primer
   k con (1−2σ⁰)^{2^k} ≤ ½. La amplificación logística hace lo que la Forma B no
   pudo (D110 Obs. 5.3: "Deligne menos finitud"): como la torre se construye POR
   VENTANA (rango finito por coordenada), el denominador está clavado — n̄^{2^k}
   es dato, no estimación — y la iteración gana contra una cota fija. Es
   literalmente el squaring de Rankin–Deligne ejecutado donde la finitud es
   verdadera: en la ventana, no en el global.
3. *Dónde reaparece el muro:* en dos lugares, y nombrarlos es el valor del
   ejercicio. (i) La parte estándar **no es efectiva**: σ⁰ = 0 es un enunciado
   Π₁ sobre la sucesión computable (κ_N/n_N)_N — "para todo N grande, κ_N/n_N
   pequeño" — la forma Π₁ de D110 Obs. 2.5 reaparece intacta. Pero con una mejora
   real de coordenadas: cada evento individual es ahora *álgebra lineal finita de
   datos aritméticos* (Prop. 2.8) — sin integrales de contorno, sin regiones
   libres de ceros, sin método de Turing: una matriz de Gram explícita por
   ventana. La falsación de RH por cómputo cambia de "integrar ζ′/ζ con error
   < 2π" a "encontrar un autovalor negativo de una matriz aritmética finita". (ii)
   La cota inferior bajo ¬RH (rama (b)) hereda el GAP de realizabilidad de D108:
   ese eslabón ya era el corazón del muro viejo y sigue abierto — ver §5.2.
4. *Qué NO se transmuta:* la necesidad de precisión asintótica fina por evento
   desaparece de verdad. Eso no estaba en ningún ítem del catálogo de
   equivalencias del programa (D89: ocho reformulaciones; P39–P43): la
   reformulación "RH ⟺ la torre logística de Gram aritméticas tiende a 0 y no
   a ½" es nueva.

### 2.5. Veredicto NO-GO 1

**Matemática nueva viable: SÍ.** Objeto bien definido (Thm. 2.6), viola el no-go
en el paso exacto y verificado (Thm. 2.7: el cuerno (b) usa arquimedianidad y solo
ahí), con un teorema sustantivo no trivial y exacto (Thm. 2.10, forma cerrada
nueva) y autonomía probada por coordenada (Prop. 2.8). **Puente: promete con un
caveat localizado.** La rama RH es teorema; la rama ¬RH cuelga de UN eslabón
heredado y nombrado (realizabilidad D108), no de una familia difusa de
estimaciones; y la transmutación es la más favorable del expediente: de precisión
o(1/log T) a separación 0 vs ½, al precio de un Π₁ cuyos eventos son
finito-algebraicos.

---

## 3. NO-GO 2: la dicotomía de seminormas, negada por no-homogeneidad

### 3.1. [EXTRACCIÓN] Las hipótesis de la dicotomía (D113 §5.4)

El enunciado: *toda seminorma de casi-periodicidad que ve los compactos es
destruida por el crecimiento de ζ en la franja; toda seminorma bajo la cual ζ es
casi-periódica es ciega a los compactos.* Hipótesis desplegadas, con su lugar en
la prueba:

- **H1 (homogeneidad):** ‖λf‖ = |λ|‖f‖. Usada en D113 Lema 5.1 (c.p. ⟹
  acotación): "f dista < ε de un polinomio trigonométrico P, y ‖f‖ ≤ ε + ‖P‖ con
  ‖P‖ < ∞" — la finitud de ‖P‖ para P arbitrario es homogeneidad + subaditividad
  sobre los monomios.
- **H2 (subaditividad):** ‖f+g‖ ≤ ‖f‖+‖g‖. Usada en el mismo paso (desigualdad
  triangular) y en que la clase c.p. sea un espacio vectorial cerrado.
- **H3 (ver compactos):** la seminorma asigna peso positivo a ventanas fijas.
  Usada para que Rouché coma: sin H3 el detector es inútil (Obs. 2.4 de D112).
- **H4 (crecimiento de ζ):** Ω-teoremas + subarmonicidad de |f|^p (D113 Thm. 5.2):
  los valores grandes inflan la norma de ventana fija a ∞.

**Análisis de supervivencia.** Sin H3 no hay detector: no negociable. H4 es un
teorema sobre ζ: no se puede negar. La cadena letal es H1+H2 ⟹ (c.p. ⟹ ‖ζ‖ < ∞)
+ H3+H4 ⟹ (‖ζ‖ = ∞): contradicción. La prueba ENTERA del lado destructivo pasa
por "c.p. ⟹ acotación en la norma" — que es un teorema SOBRE seminormas. Un
detector acotado por construcción hace ese paso vacuo: la implicación "c.p. ⟹
acotado" se vuelve trivialmente verdadera y sin contenido, y H4 no tiene norma que
inflar. La hipótesis más débil a negar: **H1+H2 — ser seminorma** — reemplazando
la estructura vectorial de detección por una estructura métrica acotada. El
contacto con la aritmética no se toca: el detector se evalúa sobre los mismos
shifts de ζ.

### 3.2. [DEFINICIÓN-NUEVA] El detector cordal

Sobre la esfera de Riemann ℂ̂, la métrica cordal:
$$\chi(a,b) := \frac{|a-b|}{\sqrt{1+|a|^2}\,\sqrt{1+|b|^2}}, \qquad
\chi(a,\infty) := \frac{1}{\sqrt{1+|a|^2}}, \qquad \chi \le 1.$$

**Definición 3.1 (detector cordal de ventana).** Para D ⊂ {½ < σ < 1} compacto y
f, g meromorfas en un entorno de D:
$$\Delta_D(f,g) := \sup_{s\in D}\ \chi\big(f(s),\, g(s)\big) \in [0,1].$$
La *recurrencia cordal* de ζ en D: existe τ_k → ∞ con
Δ_D(ζ(\cdot+iτ_k), ζ) → 0. La cantidad de crecimiento asociada es la **derivada
esférica** f^{\#}(s) := |f'(s)|/(1+|f(s)|²) (la derivada respecto de χ; Marty), y
definimos el **módulo de Marty de la órbita**:
$$\mu^{\#}_D(T) := \sup_{0\le\tau\le T}\ \sup_{s\in D}\ \zeta^{\#}(s+i\tau).$$

**Observación 3.2.** Δ_D no es seminorma ni proviene de una: no hay homogeneidad
(χ(2a, 0) ≠ 2χ(a,0)), no hay desigualdad de escala, y Δ_D(f, 0) ≤ 1 para toda f.
Es una métrica completa sobre C(D, ℂ̂). H1 y H2 quedan negadas; H3 se verifica
abajo.

**Observación 3.3 (variante registrada y por qué se descarta).** El encargo
sugería también la detección modulada por crecimiento d(f) = liminf |f|/M(t). Se
exploró y se descarta a favor de χ por una razón estructural: cualquier
modulación M(t) elegida a priori es una función del programa, y los Ω-teoremas
son no-uniformes en t (los valores grandes ocurren en alturas no controladas):
la modulación correcta dependería de la órbita misma. La métrica cordal modula
por el VALOR PUNTUAL — 1+|f|² — que es la única modulación disponible en el punto
y momento exactos del valor grande. Es la solución canónica del mismo deseo.

### 3.3. [TEOREMA] Primeros teoremas

**Teorema 3.4 (violación del NO-GO 2: ambos cuernos fallan para Δ_D).**
(a) Δ_D *ve compactos*: si f ≠ g en algún punto de D (como funciones continuas
D → ℂ̂), entonces Δ_D(f,g) > 0; en particular Δ_D no identifica funciones que
difieren en la ventana — la ceguera de B²/Weyl (D112 Obs. 2.4) no la afecta.
(b) Δ_D *sobrevive al crecimiento*: sup_τ Δ_D(ζ(\cdot+iτ), g) ≤ 1 para toda g;
el mecanismo destructivo de D113 Thm. 5.2 es inaplicable — su prueba requiere
(i) "c.p. ⟹ acotación en la norma" (Lema 5.1: usa H1+H2, que Δ_D no tiene — y
para Δ_D la acotación es incondicional y vacua) y (ii) subarmonicidad de |f|^p
para inflar la norma con Ω-valores — χ(f(s), g(s)) no es subarmónica en s y está
acotada por 1: no hay norma que inflar. (c) Por tanto el enunciado de la
dicotomía ("ve compactos ⟹ destruida por crecimiento") es falso en la categoría
de estructuras de detección métricas acotadas: Δ_D es un contraejemplo.

*Demostración.* (a) χ es una métrica en ℂ̂: f(s₀) ≠ g(s₀) ⟹ χ(f(s₀),g(s₀)) > 0
⟹ sup ≥ ese valor. (b) χ ≤ 1 por definición; para la inaplicabilidad: el Lema 5.1
de D113 deduce ‖f‖ ≤ ε + ‖P‖ usando la desigualdad triangular de la SEMInorma
sobre f = (f−P) + P y la finitud de ‖P‖ que viene de homogeneidad sobre los
monomios e^{iλt}; con Δ_D no hay ‖·‖: la cantidad está acotada por 1 de antemano
y la implicación "casi-periódico ⟹ acotado" no tiene contenido que explotar. El
Teorema 5.2 de D113 necesita una seminorma de ventana cuyo valor crezca con
sup_D |ζ|; χ está construida para que dos valores grandes cercanos en ℂ̂ den
χ pequeño: V_n = |ζ(σ+it_n)| → ∞ da χ(ζ, ∞) → 0, no ∞. (c) inmediato de (a)+(b).
∎

**Teorema 3.5 (conservación del poder de detección: equivalencia local).** Sea
D ⊂ {½<σ<1} compacto, M := sup_D |ζ| < ∞, y
ε₀ := 1/(2\sqrt{1+M^2}). Entonces para todo τ y todo 0 < ε < ε₀:
$$\Delta_D(\zeta(\cdot+i\tau), \zeta) < \varepsilon \;\Longrightarrow\;
\sup_{s\in D} |\zeta(s+i\tau) - \zeta(s)| \;\le\; C(M)\,\varepsilon,
\qquad C(M) := \sqrt{1+(2M+2)^2}\,\sqrt{1+M^2},$$
y recíprocamente sup_D |ζ(s+iτ)−ζ(s)| < ε ⟹ Δ_D < ε (pues χ(a,b) ≤ |a−b|). En
consecuencia: *recurrencia cordal de ζ en D ⟺ LP-112 en D*, y la recurrencia
cordal alimenta a Rouché exactamente igual (D112 Thm. 2.3 aplica verbatim:
recurrencia cordal ⟹ m ∈ {0,∞}).

*Demostración.* Sea a := ζ(s+iτ), b := ζ(s), |b| ≤ M. Primero: χ(a,b) < ε₀
fuerza |a| ≤ 2M+2. En efecto, si |a| > 2M+2:
$$\chi(a,b) = \frac{|a-b|}{\sqrt{1+|a|^2}\sqrt{1+|b|^2}}
\ \ge\ \frac{|a|-M}{\sqrt{1+|a|^2}\,\sqrt{1+M^2}}
\ \ge\ \frac{1}{2\sqrt{1+M^2}} = \varepsilon_0,$$
donde la última desigualdad usa (|a|−M)/√(1+|a|²) ≥ ½ para |a| ≥ 2M+2 (porque
|a| − M ≥ (|a|+2)/2 ≥ ½√(1+|a|²) cuando |a| ≥ 2M+2 ≥ 2: se verifica
(|a|+2)² ≥ 1+|a|² ⟺ 4|a|+3 ≥ 0, y |a|−M ≥ |a| − (|a|−2)/2 = (|a|+2)/2). Con
|a| ≤ 2M+2 y |b| ≤ M: |a−b| = χ(a,b)·√(1+|a|²)√(1+|b|²) ≤ ε·C(M). Tomando sup en
s ∈ D se concluye. ∎

**Observación 3.6.** El Teorema 3.5 es deliberadamente "decepcionante" y es
información: el detector nuevo NO cambia qué significa recurrencia sobre un
compacto fijo — cambia QUÉ TEOREMAS PUEDEN EXISTIR sobre el detector. La
dicotomía de D113 demostraba que el detector con las propiedades requeridas no
existía en la categoría de seminormas; Δ_D existe, ve la ventana del cero, y
ningún Ω-teorema puede matarlo. La pregunta viva pasa a ser la compacidad.

**Teorema 3.7 (el espejo de Marty; incondicional).** Para todo disco cerrado
D = D̄(s₀, r) ⊂ {½<σ<1}:
$$\sup_{\tau\ge 0}\ \sup_{s\in D}\ \zeta^{\#}(s+i\tau) = \infty,
\qquad\text{es decir}\qquad \mu^{\#}_D(T) \to \infty.$$
Más precisamente: para todo K > 0, el conjunto
{τ : sup_{s∈D} ζ^{\#}(s+iτ) > K} tiene densidad inferior positiva. En
consecuencia la familia {ζ(\cdot+iτ)}_τ NO es normal en sentido de Marty sobre
ningún disco de la franja: la extracción de límites cordales (el análogo del
eslabón E2 de la cadena de D113 §4.1) falla para la órbita completa.

*Demostración.* Fijamos K > 0. Sea δ := 1 y el objetivo
$$g(s) := \delta\,\exp\!\Big(\frac{2K}{\delta}(s-s_0)\Big),$$
entera y sin ceros; en particular g ∈ H₀^c(D̄(s₀, r)) (continua y no nula en el
disco cerrado, holomorfa en el interior; el disco cerrado tiene complemento
conexo). Por el teorema de universalidad de Voronin en su forma moderna (D102,
Teorema 2.1, verificado allí contra Matsumoto Thm. 1), el conjunto de τ con
$$\sup_{|s-s_0|\le r}\ |\zeta(s+i\tau) - g(s)| < \eta, \qquad
\eta := \min\!\Big(\frac{Kr}{2},\ \frac{\delta}{2}\Big)\cdot\frac{1}{2},$$
tiene densidad inferior positiva. Para cada tal τ, estimamos ζ^{\#} en s₀+iτ:
(i) |ζ(s₀+iτ)| ≤ |g(s₀)| + η = δ + η ≤ 3δ/2;
(ii) por la fórmula de Cauchy aplicada a ζ(\cdot+iτ) − g sobre |s−s₀| = r:
|ζ'(s₀+iτ) − g'(s₀)| ≤ η/r, y g'(s₀) = 2K. Luego
$$\zeta^{\#}(s_0+i\tau) = \frac{|\zeta'(s_0+i\tau)|}{1+|\zeta(s_0+i\tau)|^2}
\ \ge\ \frac{2K - \eta/r}{1 + (3\delta/2)^2}
\ \ge\ \frac{2K - K/4}{1 + 9/4} \ >\ \frac{K}{2}.$$
Como K es arbitrario, sup_τ sup_D ζ^{\#} = ∞ (reemplazando K por 2K se obtiene la
forma con densidad para cada nivel). La no-normalidad de Marty es el criterio de
Marty: una familia de funciones meromorfas es normal en D si y solo si las
derivadas esféricas están uniformemente acotadas en compactos de D; aquí no lo
están en ningún disco. ∎

### 3.4. [PUENTE] Transmutación: el crecimiento sube un nivel de derivada

Lo que el objeto da sobre ζ, con el rastreo honesto:

1. **El no-go queda genuinamente violado** (Thm. 3.4): la dicotomía de seminormas
   no era el muro — era un teorema sobre la categoría equivocada. Esto corrige el
   mapa: D113 §5.4 elevaba la dicotomía a "el muro de P43 en coordenada de
   seminormas"; el detector cordal muestra que esa coordenada tenía un grado de
   libertad inexplorado (estructuras acotadas no homogéneas) donde la
   imposibilidad del DETECTOR desaparece.
2. **Dónde reaparece la dificultad: en la compacidad, y con forma nueva.** La
   cadena de D113 §4.1 tenía cinco eslabones; con Δ_D el eslabón E2
   (normalidad/extracción) pasa de Montel (euclídeo: muere por Ω-acotación, se
   salvaba restringiendo a G_M de densidad 1−δ) a Marty (cordal: muere por
   Thm. 3.7 — y nótese que muere con DENSIDAD POSITIVA por nivel, así que no se
   salva por restricción a un conjunto de densidad 1: para K fijo sí se puede
   restringir a {τ : ζ^{\#} ≤ K} de densidad ≥ 1−δ(K)... la densidad del conjunto
   malo es positiva pero ¿pequeña? — GAP menor declarado: la prueba via Voronin da
   densidad positiva del conjunto malo por nivel K, sin cota inferior cuantitativa;
   la variante restringida de la cadena cordal queda abierta). El eslabón E5
   (identificación/selección), que era el punto de muerte real de D113, queda
   EXACTAMENTE igual: el detector cordal no aporta selección. **La transmutación
   precisa: el trade-off crecimiento/localización de D113 §5.4 ("cualquier control
   que viera al cero vería también al valor grande y reventaría") se re-expresa
   como: cualquier métrica acotada que domestique el valor grande lo paga en la
   derivada — el valor grande de ζ y el cero de ζ siguen viviendo en la misma
   escala, ahora en coordenadas esféricas.** El muro no era de seminormas ni de
   métricas: es del par (valor, derivada) — una información que el marco viejo no
   podía enunciar.
3. **Lo que queda en pie como matemática nueva:** el Teorema 3.7 es un Ω-teorema
   esférico para ζ que no encontramos en la literatura del programa ni en la
   consultada por D113 (las búsquedas de D113 §5.2 sobre Stepanov no cubren
   derivada esférica; estatus: nuevo aquí, prueba completa autocontenida sobre
   insumos verificados en D102). La cantidad μ^{\#}_D(T) es un objeto de
   crecimiento nuevo: mide la velocidad cordal máxima de la órbita. [DESEO 3.8:
   una cota superior de μ^{\#}_D(T) sobre el subconjunto de casi-períodos B² —
   si la velocidad cordal fuera moderada SOBRE los casi-períodos, la cadena
   cordal restringida reviviría. No hay candidato de prueba hoy.]

### 3.5. Veredicto NO-GO 2

**Matemática nueva viable: SÍ, con techo a la vista.** Tres teoremas reales
(3.4, 3.5, 3.7), uno de ellos (espejo de Marty) un Ω-resultado incondicional
nuevo con prueba por universalidad. **Puente: transmuta.** La dificultad
reaparece, identificada con precisión (de E5+acotación a E5+Marty): el detector
deja de ser imposible pero la selección no-genérica — el corazón de LP-112/LP-113
— no se mueve un milímetro. Valor neto: corrección del mapa (la dicotomía de
seminormas no era el muro) + el objeto μ^{\#} + un GAP menor bien planteado
(cadena cordal restringida).

---

## 4. NO-GO 3: la obstrucción de la órbita individual, negada por re-topologización

### 4.1. [EXTRACCIÓN] Las hipótesis de la obstrucción (D102 §7)

El enunciado: la transferencia [recurrencia incondicional de ω₀ en el toro] ⟹
[recurrencia de ζ] falla porque la observable de Euler Φ es discontinua
exactamente en la órbita aritmética, y esa continuidad es RH-equivalente
(D102 Prop. 7.2). Hipótesis desplegadas:

- **H1 (topología producto en Ω):** da compacidad, y con ella minimalidad y
  unicidad ergódica del flujo de Kronecker (D102 E1–E3) — el lado "gratis" de la
  transferencia: TODO punto, incluido ω₀, es uniformemente recurrente.
- **H2 (continuidad como noción de regularidad):** la transferencia usa
  continuidad de Φ en ω₀ respecto de ESA topología; la unicidad ergódica controla
  observables continuas y nada más.
- **H3 (la observable fija):** Φ(ω) = producto de Euler aleatorio, definida donde
  converge; su dominio excluye la órbita de ω₀ bajo ¬RH (Prop. 7.2).

**Análisis de supervivencia.** H3 es un teorema (Prop. 7.2): no se puede negar
sin cambiar de observable, y D102 mostró que la observable es esencialmente
única (es la que conecta con ζ). H2 sin H1 es vacío: la continuidad es relativa a
una topología. La hipótesis negable es **H1**: nada obliga a usar la topología
producto. El no-go NO sobrevive a su negación en el siguiente sentido exacto: la
afirmación "Φ es discontinua en ω₀" es relativa a la topología, y existe una
topología más fina donde la familia de observables truncadas es equicontinua en
TODO punto (Thm. 4.6) — el "punto excepcional" es un artefacto de la topología
producto. Lo que hay que auditar es el precio: qué teoremas de H1 (compacidad,
minimalidad, recurrencia gratuita) sobreviven a la refinación. Respuesta: ninguno
(Lema 4.5) — y la contabilidad exacta de esa pérdida es el contenido del puente.

### 4.2. [DEFINICIÓN-NUEVA] La topología aritmética

Notación: Ω = ∏_p 𝕋_p el toro de Bohr; para ω ∈ Ω, X ≥ 2 y s en la franja,
$$S_X(s;\omega) := \sum_{p\le X} \omega(p)\,p^{-s}, \qquad
\zeta_X(s,\omega) := \prod_{p\le X}\big(1-\omega(p)p^{-s}\big)^{-1},$$
$$\log\zeta_X(s,\omega) = S_X(s;\omega) + R_X(s;\omega), \qquad
R_X(s;\omega) := \sum_{p\le X}\sum_{k\ge2}\frac{\omega(p)^k}{k\,p^{ks}}$$
(rama dada por la serie; converge porque |ω(p)p^{−s}| = p^{−σ} < 1).

**Definición 4.1 (pseudométricas de truncación uniforme).** Para D compacto
⊂ {½<σ<1}:
$$d_D(\omega,\omega') := \sup_{X\ge2}\ \sup_{s\in D}\
\big|S_X(s;\omega) - S_X(s;\omega')\big| \ \in [0,\infty].$$

**Definición 4.2 (topología aritmética).** 𝒯_ar es la topología sobre Ω generada
por la topología producto junto con las bolas {ω′ : d_D(ω, ω′) < ε}, sobre todos
los D compactos de la franja, ω ∈ Ω, ε > 0. El *espacio aritmético de fases* es
(Ω, 𝒯_ar) con el mismo flujo T_τ(ω) = (p^{−iτ}ω(p))_p.

**Observación 4.3 (la idea en una línea).** d_D mide cercanía de fases PESADA POR
LA ARITMÉTICA y UNIFORME EN LA TRUNCACIÓN: dos puntos del toro están cerca si
todos sus polinomios de Dirichlet parciales están cerca a la vez. Es la topología
inicial mínima que hace equicontinua a la familia de truncados — el conjunto de
casi-períodos de la sugerencia del encargo es exactamente la preimagen por
τ ↦ T_τω₀ de las d_D-bolas en ω₀.

### 4.3. [TEOREMA] Primeros teoremas

**Lema 4.4 (estrictamente más fina).** 𝒯_ar es más fina que la topología
producto, y estrictamente: para todo D que contenga un punto real σ₀ ∈ (½,1), la
bola {ω : d_D(ω, ω₀) < 1} no contiene ningún entorno producto-básico de ω₀.

*Demostración.* Más fina: por definición (se agregan abiertos). Estricta: un
entorno producto-básico de ω₀ restringe finitas coordenadas, digamos p ≤ N.
Definimos ω′ ∈ Ω por ω′(p) := 1 para p ≤ N y ω′(p) := −1 para p > N. Entonces
ω′ está en el entorno básico, pero para X > N:
$$\big|S_X(\sigma_0;\omega_0) - S_X(\sigma_0;\omega')\big|
= \Big|\sum_{N<p\le X} 2\,p^{-\sigma_0}\Big| = 2\!\!\sum_{N<p\le X}\!\! p^{-\sigma_0}
\ \xrightarrow[X\to\infty]{}\ \infty$$
porque Σ_p p^{−σ₀} diverge para σ₀ < 1. Luego d_D(ω₀, ω′) = ∞ ≥ 1. ∎

**Lema 4.5 (el precio: la compacidad muere, y con ella la dinámica gratuita).**
(Ω, 𝒯_ar) no es compacto. En consecuencia los teoremas E1–E3 de D102 §7.1
(minimalidad, unicidad ergódica, recurrencia uniforme de todo punto) pierden sus
hipótesis: ninguno está disponible en 𝒯_ar por la vía clásica.

*Demostración.* La identidad id: (Ω, 𝒯_ar) → (Ω, producto) es continua (Lema 4.4)
y biyectiva, y la topología producto es Hausdorff. Si (Ω, 𝒯_ar) fuera compacto,
id sería un homeomorfismo (biyección continua de compacto a Hausdorff), luego
𝒯_ar = producto — contradice la estrictez del Lema 4.4. La segunda afirmación:
minimalidad/unicidad ergódica de rotaciones se prueban sobre grupos compactos
(D102 cita Walters cap. 6); sin compacidad no hay teorema de Birkhoff de
recurrencia ni medida de Haar normalizable que promediar — los enunciados quedan
sin prueba, y de hecho la recurrencia de ω₀ en 𝒯_ar es una pregunta abierta
no trivial (§4.4). ∎

**Teorema 4.6 (disolución del punto excepcional: equicontinuidad universal de la
observable truncada).** Sea D′ compacto ⊂ {½<σ<1} y σ₁ := min{Re s : s ∈ D′}
> ½. Existe una función η: (0,1) → (0,∞) con η(d) → 0 cuando d → 0 (explícita en
la prueba, η(d) ≤ C(σ₁)·d^{(2σ₁−1)/2} + 8d^{1/2}) tal que para TODOS
ω, ω′ ∈ Ω con d := d_{D′}(ω, ω′) < 1:
$$\sup_{X\ge2}\ \sup_{s\in D'}\
\big|\log\zeta_X(s,\omega) - \log\zeta_X(s,\omega')\big|\ \le\ d + \eta(d).$$
En particular la familia {log ζ_X(\cdot, ·)}_{X≥2}, vista como funciones de
(Ω, 𝒯_ar) en (C(D′), ‖·‖_∞), es uniformemente equicontinua, uniformemente en X,
**en todo punto de Ω** — incluido ω₀. El punto aritmético no es excepcional para
𝒯_ar: la regularidad de la observable truncada en ω₀ es exactamente la misma que
en cualquier otro punto.

*Demostración.* log ζ_X = S_X + R_X. La parte k=1: |S_X(s;ω) − S_X(s;ω′)| ≤ d
para todo X y s ∈ D′, por definición de d. La parte k≥2: con
δ_p := |ω(p) − ω′(p)| ∈ [0,2],
$$\big|R_X(s;\omega)-R_X(s;\omega')\big|
\ \le\ \sum_{p\le X}\sum_{k\ge2} \frac{|\omega(p)^k-\omega'(p)^k|}{k\,p^{k\sigma}}
\ \le\ \sum_{p}\sum_{k\ge2} \frac{\min(2,\,k\,\delta_p)}{k}\,p^{-k\sigma_1},$$
usando |a^k − b^k| ≤ k|a−b| para |a| = |b| = 1. Acotamos la suma interna de dos
maneras: (i) por δ_p Σ_{k≥2} p^{−kσ₁} y (ii) por 2Σ_{k≥2} p^{−kσ₁}/k ≤
Σ_{k≥2} p^{−kσ₁}; y Σ_{k≥2} p^{−kσ₁} = p^{−2σ₁}/(1−p^{−σ₁}) ≤ 4p^{−2σ₁} (pues
p^{−σ₁} ≤ 2^{−1/2} da 1/(1−p^{−σ₁}) ≤ 1/(1−2^{−1/2}) < 4). Luego
$$\big|R_X(\omega)-R_X(\omega')\big| \ \le\ 4\sum_p p^{-2\sigma_1}\,\min(1,\,\delta_p).$$
Falta controlar δ_p con d. Tomando en la definición de d las truncaciones
consecutivas X = p y X = p^- (el primo anterior), la diferencia de sumas
parciales aísla el término p:
$$\delta_p\,p^{-\sigma} = \big|(S_p - S_{p^-})(s;\omega) - (S_p - S_{p^-})(s;\omega')\big|
\ \le\ 2d \quad (s\in D'),$$
y eligiendo s ∈ D′ con Re s = σ₁ (si D′ no contiene tal punto, σ₁ se alcanza en
la frontera; tomamos s realizando el mínimo de Re): δ_p ≤ 2d·p^{σ₁}. Partimos en
P ≥ 2 a elegir:
$$4\sum_{p\le P} p^{-2\sigma_1}\cdot 2d\,p^{\sigma_1}
\ +\ 4\sum_{p>P} p^{-2\sigma_1}
\ \le\ 8d \sum_{n\le P} n^{-\sigma_1}\ +\ 4\sum_{n>P} n^{-2\sigma_1}
\ \le\ 8d\,P\ +\ \frac{4}{2\sigma_1-1}\,P^{1-2\sigma_1},$$
(usando Σ_{n≤P} n^{−σ₁} ≤ P y la cola integral con 2σ₁ > 1). Con P := ⌈d^{−1/2}⌉:
$$\eta(d) := 8\,d^{1/2}\cdot 2\ +\ \frac{4}{2\sigma_1-1}\, d^{(2\sigma_1-1)/2}
\ \xrightarrow[d\to0]{}\ 0.$$
(El factor 2 absorbe el techo de P.) Sumando las partes k=1 y k≥2 se obtiene la
cota d + η(d), uniforme en X, en s ∈ D′ y en el par (ω, ω′). ∎

**Corolario 4.7 (forma multiplicativa, lista para Rouché).** Bajo las hipótesis
del Teorema 4.6, para todo X y s ∈ D′:
$$e^{-(d+\eta(d))}\ \le\ \Big|\frac{\zeta_X(s,\omega)}{\zeta_X(s,\omega')}\Big|
\ \le\ e^{\,d+\eta(d)},$$
es decir, los productos truncados son multiplicativamente cercanos, uniformemente
en la truncación. (Exponencial de la cota del logaritmo.) ∎

**Teorema 4.8 (transferencia: qué compraría la 𝒯_ar-recurrencia).** Supongamos:
(i) ω₀ es 𝒯_ar-recurrente: existe τ_k → ∞ con d_{D′}(T_{τ_k}ω₀, ω₀) → 0; y
(ii) *anclaje de colas*: para los mismos τ_k, ζ_X(s+iτ_k) → ζ(s+iτ_k) cuando
X → ∞, uniformemente en s ∈ D y en k (D ⊂ int D′ compacto). Entonces vale
LP-112 en D y por tanto m ∈ {0,∞} (D112, Thm. 2.3).

*Demostración.* Nótese que S_X(s; T_τω₀) = Σ_{p≤X} p^{−iτ}p^{−s} = S_X(s+iτ; ω₀)
y análogamente ζ_X(s, T_τω₀) = ζ_X(s+iτ, ω₀) =: ζ_X(s+iτ): la pseudométrica
sobre la órbita ES la auto-distancia uniforme-en-truncación de los polinomios de
Dirichlet. Por (i) y el Corolario 4.7, con ε_k := d_k + η(d_k) → 0:
|ζ_X(s+iτ_k)| = |ζ_X(s)|·e^{O(ε_k)} y, de la cota del logaritmo,
|ζ_X(s+iτ_k) − ζ_X(s)| ≤ |ζ_X(s)|(e^{ε_k} − 1) uniformemente en X y s ∈ D′. Por
(ii) y la convergencia clásica ζ_X(s) → ζ(s) en D (mismas colas en τ = 0, caso
particular de (ii) con k fijo... — para τ = 0 la convergencia uniforme en
compactos de ζ_X a ζ NO es un teorema en la franja; usamos (ii) que la incluye
por hipótesis al tomar el límite k fijo y la continuidad: precisamente, (ii) con
el índice k congelado más la cota multiplicativa dan, pasando X → ∞ primero en
los dos miembros: |ζ(s+iτ_k) − ζ(s)| ≤ limsup_X |ζ_X(s+iτ_k) − ζ_X(s)| ≤
(e^{ε_k} − 1)·limsup_X |ζ_X(s)|, y este último es finito y uniforme en s ∈ D por
(ii) aplicado a τ = 0 si 0 está en la clausura de las hipótesis o, si no, por el
mismo anclaje aplicado al punto base — declaramos (ii) incluyendo τ = 0). Luego
sup_D |ζ(s+iτ_k) − ζ(s)| → 0: LP-112. La conclusión m ∈ {0,∞} es D112 Thm. 2.3
(Rouché con constantes congeladas). ∎

**Observación 4.9 (honestidad sobre el Teorema 4.8).** El teorema es un
condicional puro y se enuncia para CONTABILIZAR, no para celebrar: muestra que el
par (i)+(ii) es exactamente suficiente, y el puente de abajo muestra que el muro
viejo se reparte exactamente entre (i) y (ii).

### 4.4. [PUENTE] Transmutación total, con la contabilidad exacta

Aplicado a ζ: en 𝒯_ar la obstrucción del NO-GO 3 desaparece LITERALMENTE — la
observable truncada es equicontinua en ω₀ (Thm. 4.6), el punto aritmético deja de
ser excepcional, y la transferencia funciona (Thm. 4.8). ¿Dónde está entonces el
muro? Contabilidad:

1. **La recurrencia gratuita se perdió.** En la topología producto, ω₀ era
   uniformemente recurrente gratis (compacidad + minimalidad, D102 E3). En 𝒯_ar
   no hay compacidad (Lema 4.5). La 𝒯_ar-recurrencia de ω₀ — la hipótesis (i) —
   es: para todo ε existe τ arbitrariamente grande con
   sup_X sup_D |S_X(s+iτ) − S_X(s)| < ε. Para CADA X fijo, Kronecker–Weyl da
   casi-períodos relativamente densos (toro finito; D112 Lema 2.2): eso es
   incondicional. El sup_X — la uniformidad en la truncación — es lo nuevo, y es
   exactamente el control de las colas Σ_{X<p≤Y}(p^{−iτ}−1)p^{−s} en el τ
   ELEGIDO: el problema de selección no-genérica de LP-113 (D113 §4.5), en
   coordenada de truncaciones. GAP: ni bajo RH sabemos probar (i) — la
   convergencia de Σp^{−s} bajo RH es localmente uniforme pero no uniforme en
   altura, así que ni la rama fácil es gratis. Declarado.
2. **La hipótesis (ii) es MW-2 sin disfraz:** anclar ζ_X → ζ en la ventana a lo
   largo de los τ_k es la propagación del producto de Euler a la franja sobre una
   sucesión específica — D102 Prop. 7.2 en versión secuencial.
3. **El teorema de conservación (síntesis del puente).** Combinando: cualquier
   topología 𝒯 que haga (a) equicontinua a la observable truncada en ω₀ con
   módulo uniforme en X y (b) recurrente a ω₀, junto con (c) el anclaje de colas,
   implica m ∈ {0,∞} (la prueba del Thm. 4.8 solo usa (a)+(b)+(c)). Como
   m ∈ {0,∞} no es un teorema del programa, NINGUNA topología puede dar (a)+(b)+(c)
   incondicionalmente hoy; y la topología producto y 𝒯_ar son los dos extremos del
   trade-off: producto = (b) gratis, (a) imposible (D102 Prop. 7.2); 𝒯_ar = (a)
   gratis (Thm. 4.6), (b) abierto y equivalente al problema de selección. **La
   obstrucción no era topológica: es un presupuesto conservado entre la
   regularidad de la observable y la recurrencia del punto.** Esto es información
   nueva sobre el muro: D102 lo veía como discontinuidad (un hecho de la
   observable); la re-topologización muestra que es una LEY DE CONSERVACIÓN entre
   observable y dinámica — refinás la topología para regularizar la observable y
   la dinámica te devuelve exactamente la misma deuda en recurrencia.
4. [DESEO 4.10] Una topología INTERMEDIA: más fina que la producto solo en las
   "direcciones de colas largas" (un d_D con sup sobre X ≤ X(ε) creciente
   controlado), donde quizá sobreviva un fragmento de compacidad (compacidad
   secuencial en bolas) y un fragmento de equicontinuidad. No se desarrolla aquí;
   queda registrado como el único hueco no explorado del trade-off.

### 4.5. Veredicto NO-GO 3

**Matemática nueva viable: SÍ como objeto, NO como palanca.** Los teoremas 4.4–4.6
son reales y la equicontinuidad universal (Thm. 4.6, con módulo explícito) es un
resultado limpio que disuelve el "punto excepcional" como artefacto. **Puente:
transmutación total.** El muro reaparece entero, repartido en (i) = selección
no-genérica (LP-113) y (ii) = MW-2 secuencial; el valor residual es la ley de
conservación del punto 3 — la formulación más estructural que el programa tiene
de por qué el marco ergódico no puede ganar: no es que falte un teorema en la
categoría; es que la categoría cobra en recurrencia lo que paga en continuidad.

---

## 5. Ranking y el siguiente teorema

### 5.1. Ranking por (novedad matemática real) × (chance de que el puente no transmute)

| # | objeto | novedad real | transmutación del puente | producto |
|---|---|---|---|---|
| 1 | **Signatura infinitesimal σ_ε + torre logística** (§2) | ALTA: índice con valores en *ℤ, ley logística exacta con forma cerrada, autonomía por ventana activando el contraejemplo de rango finito | PARCIAL y favorable: el Π₁ persiste pero la precisión o(1/log T) se convierte en separación macroscópica 0 vs ½; un solo eslabón heredado (realizabilidad D108) | **el mejor** |
| 2 | **Detector cordal Δ_D + espejo de Marty** (§3) | MEDIA-ALTA: viola la dicotomía, Ω-teorema esférico nuevo (Thm. 3.7), cantidad μ^{\#} nueva | TRANSMUTA: el crecimiento sube a la derivada esférica; E5 (selección) intacto; queda un GAP menor atacable (cadena cordal restringida) | medio |
| 3 | **Topología aritmética 𝒯_ar** (§4) | MEDIA: equicontinuidad universal probada, disolución del punto excepcional | TOTAL: ley de conservación continuidad/recurrencia — el muro entero reaparece repartido en LP-113 + MW-2 | bajo (pero la ley de conservación es el mejor enunciado estructural del muro ergódico) |

La razón del ranking en una línea cada uno: el objeto 1 es el único cuya
transmutación CAMBIA LA ESCALA del problema (de asintótica fina a constantes
separadas) en lugar de cambiarle el nombre; el objeto 2 produce el teorema
incondicional más citable del documento pero no mueve la selección; el objeto 3
produce el mejor diagnóstico y la peor palanca.

### 5.2. El siguiente teorema concreto a atacar (en el objeto 1)

**Problema 133.A (realizabilidad test-accesible de la cota inferior; el único
eslabón citado-no-probado del Teorema-puente 2.13).** Probar: existe c > 0
absoluto tal que, bajo ¬RH con un cuádruplo off-crítico (m = 1, el caso mínimo
basta para la dicotomía), el esquema canónico 𝒮* de la Def. 2.1 (grilla finita
test-accesible de ventanas de resolución, índice por supremo κ_N = max_W
neg.ind(Q|_{V_W})) satisface
$$\limsup_{N\to\infty} \frac{\kappa_N}{n_N} \ \ge\ c\ >\ 0.$$
Equivalentemente: la cota inferior de índice por ventana alineada de D108
(Prop. 2.3 + Lema 2.4) vale (α) sin la Hipótesis D del juguete, y (β) con la
ventana de la grilla más cercana en lugar de la ventana exactamente alineada
(estabilidad del índice bajo desplazamiento o(ancho) de la ventana — un lema de
perturbación de formas cuadráticas: si W y W̃ difieren en o(1) del ancho, las
matrices de Gram difieren en norma o(autovalor negativo), y el índice no cae;
la herramienta natural es Weyl/perturbación de autovalores con la cota inferior
|λ_min| ≥ gap de D108). El sub-objetivo (β) parece genuinamente atacable con las
herramientas del programa (es perturbación finito-dimensional, no aritmética); el
sub-objetivo (α) es la deuda real de D108 y decide si la dicotomía logística es
una equivalencia de RH limpia o queda condicional. Con 133.A probado, el
Teorema-puente 2.13 se promueve a:
$$\mathrm{RH} \iff \lim_{k\to\infty}\sigma^{(k)}(\mathcal{S}^*) = 0
\qquad\text{(sin caveats, nueva equivalencia, separación } 0 \text{ vs } \tfrac12).$$

### 5.3. Cierre

El método de diseño por negación rindió exactamente lo que promete y nada más:
tres objetos bien definidos, ocho teoremas probados de verdad (2.6, 2.7, 2.8,
2.10, 3.4, 3.5, 3.7, 4.6 — más los lemas 4.4, 4.5 y los corolarios), una
equivalencia nueva de RH condicionada a un eslabón único y nombrado, un Ω-teorema
incondicional nuevo, y una ley de conservación que explica el fracaso ergódico
mejor que el diagnóstico de discontinuidad. Ningún muro se cruzó; uno de los tres
(el de la clase ℱ) cambió de forma de un modo que reduce la próxima batalla a un
lema de perturbación más una deuda vieja y localizada. Es más de lo que un
documento puede pedir y menos de lo que el problema exige — como corresponde.

---

## Referencias

**Internas (backward-only):** Doc 110 (Teorema 4.3, Prop. 4.5, axiomas L1–L6,
Lema 2.4, Obs. 2.5, Obs. 5.3); Doc 113 (Lema 5.1, Teorema 5.2, §4.1 eslabones
E1–E5, §4.5 LP-113, §5.4 dicotomía de seminormas); Doc 112 (LP-112, Thm. 2.3,
Prop. 2.6, Obs. 2.4, Lema 2.2); Doc 102 (Teorema 2.1 = universalidad de Voronin
verificada vía Matsumoto; Prop. 7.2; Cor. 7.3; E1–E3; §7.3); Doc 108 (Teoremas
3.3, 3.4, 4.3; Prop. 2.3, 2.5; Lema 2.4 y su Hipótesis D; §7.4; ec. 4.1);
Doc 107 (W₂, Prop. 6.1); Doc 106 (identidad tensorial del índice); Doc 104
(ventana anclada §5.4); Doc 99 (patrón de transmutación, CCM-ZST); P43
(Principio 3.1, Teorema de autonomía valor/inercia, ledger L3); P35 (κ(Q) = 2m);
NO-GO-LIST (MW-1…MW-7).

**Literatura (verificable; los enunciados usados son estándar y se citan por
referencia clásica):**
- A. Robinson, *Non-standard Analysis*, North-Holland, 1966 (ultrapotencias,
  parte estándar, transferencia; cap. 2).
- F. R. Gantmacher, *The Theory of Matrices*, Chelsea, 1959, Vol. 2, Cap. X
  (signatura vía Newton/Hankel, Jacobi–Frobenius; ya verificado en D110).
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*,
  Comm. Sém. Math. Lund (1952) (positividad de Weil ⟺ RH; usado en la
  normalización del programa vía D110 §3.2 y Doc 100, Lema 2.0).
- S. M. Voronin, Izv. Akad. Nauk SSSR Ser. Mat. 39 (1975), 475–486; forma moderna
  vía K. Matsumoto, arXiv:1407.4216, Thm. 1 (verificado en D102 — insumo del
  Teorema 3.7).
- F. Marty, *Recherches sur la répartition des valeurs d'une fonction
  méromorphe*, Ann. Fac. Sci. Toulouse 23 (1931) (criterio de normalidad por
  derivada esférica; enunciado estándar, cf. Schiff, *Normal Families*,
  Springer 1993). [Datos editoriales del original NO VERIFICADOS en esta sesión;
  el criterio citado es folclore verificable en Schiff.]
- A. S. Besicovitch, *Almost Periodic Functions*, Cambridge, 1932 (clases B², S^p;
  vía D112/D113).
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed., Oxford,
  1986 (Ω-teoremas, cap. VIII; valor medio cuadrático, Thm. 7.2 — vía D113).
- P. Walters, *An Introduction to Ergodic Theory*, Springer GTM 79 (rotaciones de
  grupos compactos; vía D102).

*Fin del Doc 133.*
