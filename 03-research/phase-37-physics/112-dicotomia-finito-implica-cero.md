# Doc 112 — La dicotomía: ataque riguroso a m < ∞ ⟹ m = 0

**Programa:** Hipótesis de Riemann — Phase 37, "modo físico"
**Fecha:** junio 2026
**Autor:** David Alejandro Trejo Pizzo
**Prerrequisitos:** Doc 109 (dicotomía D-109; identidad RH = (m<∞) ∧ (m∈{0,∞}); gap media-cuadrática→puntual, §4.4; precedente Bagchi, §4.3); Doc 110 (Prop. 4.5: rango finito a priori ⟹ inercia autónoma vía Newton/Jacobi–Frobenius; axioma L6; frontera rango-infinito/rango-finito-a-priori); Doc 111 (Prop. 2.2: cosh-ejemplos con m finito sin Euler; Cor. 2.3: toda prueba de la dicotomía necesita insumo aritmético; §6: dicotomía presupuesto/costo); Doc 104 (amplificador auto-bloqueante, vía P42 §2 y P43 Thm. C); Doc 102 (Bagchi: recurrencia fuerte ⟺ RH; ω₀ y la observable de Euler); Doc 98 (Cor. 2.4: costo 2δ²K_λ(γ₀) por cuádruplo); Doc 72 (T_λ vía fórmula de Weil; estructura verificada en fuente para este documento); Doc 105 (divergencia de la serie de primos de B_λ); P43 (Principio 3.1, cuantificador maestro; §4 valor/inercia).
**Regla absoluta:** ninguna prueba se fabrica. Cada paso es demostración completa, enunciado de literatura con referencia verificable, o GAP declarado con localización exacta. Sin numéricos, sin simulaciones. Citas backward-only; lo no verificado se marca [NO VERIFICADO].

---

## 0. Resumen ejecutivo

**El objetivo.** Hipótesis H(m): ζ tiene exactamente m cuádruplos de ceros off-críticos
{½ ± δ_j ± iγ_j : j = 1,…,m}, con 0 < m < ∞. Derivar una contradicción. Por la identidad
arquitectónica del Doc 109 (§4.5), esto es exactamente la mitad D-109 de RH:
RH = (m<∞) ∧ (m∈{0,∞}); el presente documento ataca la implicación m<∞ ⟹ m=0 con la
finitud como hipótesis de trabajo — la primera vez en el programa que la finitud está del
lado de los insumos y no de las metas.

**Hallazgos, en orden:**

1. **(§2) El argumento de Bohr–Rouché, congelado por H(m), se reduce a UN lema puntual
   (LP-112) y todo lo demás es teorema.** La casi-periodicidad B² de ζ en cada recta
   σ ∈ (½,1) es incondicional (Lema 2.1), sus casi-períodos son relativamente densos
   (Lema 2.2), y H(m) congela todas las constantes del paso de Rouché: si existe UNA
   sucesión no acotada τ_k con ζ(s+iτ_k) → ζ(s) uniformemente en un disco fijo alrededor
   de un cero off-crítico, entonces m = ∞ (Teorema 2.3, prueba completa). La hipótesis
   m < ∞ hace dos cosas reales: elimina toda necesidad de uniformidad en (δ, γ₀) — las
   constantes son números fijos positivos — y convierte UNA réplica en contradicción.

2. **(§2.4) El paso B²→puntual no es solo un gap: la dirección distribucional está
   probada EN CONTRA.** Proposición 2.6 (nueva en esta forma, ensamblada de Bagchi +
   Hurwitz): bajo H(m), el conjunto de τ buenos para Rouché en el disco del cero
   off-crítico tiene **densidad superior CERO**. Los casi-períodos B² tienen densidad
   positiva, pero su bondad es una media en t que asigna peso nulo a la ventana fija del
   cero (la seminorma de Besicovitch anula los compactos, Obs. 2.4); la bondad puntual en
   el disco fijo es un evento de densidad cero. La esperanza de "extraer un τ de un
   conjunto de medida positiva" es estructuralmente falsa: el conjunto relevante es de
   densidad cero, y exhibir un elemento suyo es el cuantificador maestro de P43 en
   coordenadas de casi-períodos.

3. **(§2.5) El bloqueo de D104 NO aplica.** El amplificador de D104 se auto-bloqueaba
   porque necesitaba densidad positiva de réplicas y el techo N(σ,T) = O(T^κ) la capaba
   con el mismo exponente. La versión secuencial necesita densidad CERO de réplicas
   (#{k: τ_k ≤ T} arbitrariamente raro), que ningún teorema de densidad obstruye
   (Prop. 2.7). La ruta no es auto-contradictoria: está sin alimentar. Es una diferencia
   genuina y es la razón por la que LP-112 queda vivo como objetivo no-RH-equivalente.

4. **(§3) El producto de Euler entra en tres lugares exactos, y los cosh-ejemplos de
   D111 quedan excluidos en el primero.** (i) La serie de Dirichlet da la casi-periodicidad
   B² — los cosh-ejemplos ni siquiera son B² en rectas verticales (Lema 3.1) y no admiten
   ninguna sucesión de auto-aproximación (Lema 3.2: |F(s+iτ)| → ∞ en el disco). (ii) La
   independencia ℚ-lineal de {log p} — factorización única, aritmética pura e
   incondicional — hace que los casi-períodos sean relativamente densos y no-discretos
   (Lema 3.3): las réplicas caen en alturas NUEVAS, mientras que un grupo discreto de
   períodos exactos mapea el conjunto de ceros sobre sí mismo y no multiplica m.
   (iii) El producto de Euler aleatorio determina el soporte del teorema límite de Bagchi
   — el insumo de la Prop. 2.6 y de la dirección RH ⟹ recurrencia fuerte. El requisito
   del Doc 111 (Cor. 2.3) queda satisfecho por la RUTA: su insumo es exactamente lo que
   la clase ℰ no tiene.

5. **(§4) La línea de momentos/trazas de Newton colapsa en dos lugares independientes,
   ninguno donde se temía.** Verificado contra el Doc 72 en fuente: B_λ(log p) =
   ∫W_λ(s)cos(s log p) dm_∞(s) es transformada de Fourier del test — autónoma, NO depende
   de los ceros; el temor de que "B_λ dependa de todos los ceros" es infundado. Los muros
   reales: (i) la serie de primos Σ_p (log p/√p)B_λ(log p) **diverge** (Doc 105:
   ≍ (5√2/8)log X) — la fórmula aritmética de D72 es estrictamente formal y no hay valor
   autónomo que alimente el sistema de momentos; (ii) aun concediendo una regularización,
   la fórmula explícita es UNA identidad que la configuración verdadera satisface
   idénticamente — no sobredetermina los 4m parámetros (Prop. 4.2); el único contenido
   no-tautológico extraíble es de signo (positividad sobre un cono de tests), que es el
   criterio de Weil, es decir RH, es decir la inercia de P43. Además (Obs. 4.3) la
   precisión requerida no es fija: ínf sobre configuraciones del gap espectral
   ε₀ ≍ δ_min² e^{−πγ_min/2} es 0 — la uniformidad sobre el espacio de hipótesis
   restaura el muro que H(m) parecía haber removido. La Prop. 4.5 del Doc 110 no aplica:
   H(m) da rango finito, no rango finito **a priori** (la dimensión 4m es el desconocido,
   Obs. 6.3 de D111).

6. **(§5) El mejor teorema demostrable hoy es la reducción exacta** (Teorema 5.1):
   **LP-112 ⟹ D-109**; combinado con la diana L8: (m<∞) ∧ LP-112 ⟹ RH. LP-112 es
   estrictamente más débil que la recurrencia fuerte de Bagchi (sucesión no acotada vs
   densidad inferior positiva); está implicado por RH; y no implica RH por ningún
   diccionario conocido — su conclusión bajo ¬RH es m = ∞, consistente. El caso m = 1 no
   evita nada (§5.3); las versiones por regiones de parámetros no agregan nada a las
   regiones libres clásicas (§5.2).

**VEREDICTO (§7): IMPLICACIÓN PARCIAL** — probada condicionalmente a un único lema
abierto (LP-112), con prueba completa del condicional, con la demostración de que el
conjunto de testigos de LP-112 tiene densidad cero bajo ¬RH (el muro localizado con
signo: la inversión media→individual en su forma de conjunto excepcional), y con la
extensión del no-go: la hipótesis m < ∞ congela las constantes pero no alimenta la
construcción del τ excepcional; las líneas directa-B² y de momentos quedan BLOQUEADAS
con localización exacta.

---

## 1. Marco: la hipótesis H(m) y qué compra exactamente la finitud

### 1.1. Hipótesis y objetivo

**Hipótesis H(m).** ζ tiene exactamente m cuádruplos off-críticos, 0 < m < ∞:
$$Z_{\mathrm{off}} = \{\tfrac12 \pm \delta_j \pm i\gamma_j : j = 1,\dots,m\},
\qquad \delta_j \in (0,\tfrac12),\ \gamma_j > 0,$$
contados con multiplicidad (Doc 111, Def. 1.1; la estructura de cuádruplo es teorema:
ecuación funcional + reflexión de Schwarz + ausencia de ceros reales en (0,1)).

**Objetivo.** Derivar de H(m) una contradicción. Eso probaría m∈{0,∞} (D-109) y, con la
identidad del Doc 109 §4.5, reduciría RH a la diana L8 (m<∞).

### 1.2. Inventario de lo que H(m) pone sobre la mesa

H(m) es una hipótesis inusualmente rica; conviene listar con precisión qué da, porque
cada línea de ataque usará piezas distintas:

- **(F1) Parámetros congelados.** δ_min := min_j δ_j > 0, γ_max := max_j γ_j < ∞,
  γ_min := min_j γ_j ≥ 3·10¹² (Platt–Trudgian, vía D111 §2.4(c)). Son **constantes del
  mundo hipotético**: ningún argumento bajo H(m) necesita uniformidad en (δ, γ₀); las
  cotas pueden depender de la configuración entera.
- **(F2) Cola RH-pura.** Todo cero con |γ| > γ_max está sobre la línea crítica. Existe un
  "último" cero off-crítico.
- **(F3) Rango finito.** El subespacio off-crítico 𝒦_off tiene dimensión exactamente 4m
  y κ(Q) = 2m (P35); la masa off de la discrepancia está concentrada en los m puntos
  espectrales {γ_j} con pesos controlados por δ_j (Doc 98).
- **(F4) Umbral de contradicción mínimo.** Para refutar H(m) basta producir **UN** cero
  off-crítico adicional (un cuádruplo nuevo): m+1 > m. No hace falta densidad positiva,
  ni siquiera infinitud directa — una sola réplica por encima de γ_max, a distancia > 0
  de la línea, cierra el argumento.

(F4) es el cambio cualitativo respecto de todo lo anterior del programa: las metas
previas (densidad anclada en D104, cota uniforme de índices en D108, positividad
semilocal en D99/100) exigían enunciados uniformes o extensivos. Aquí la meta es un
único evento. La pregunta del documento es si alguna maquinaria incondicional produce
ese evento. Adelantamos la respuesta para fijar la lectura: **no — y la razón es que el
evento, aunque único, vive en un conjunto de densidad cero cuya no-vacuidad es
exactamente el tipo de enunciado que el cuantificador maestro bloquea; pero el modo de
fallar deja un residuo nuevo (la reducción a LP-112 y la no-aplicabilidad del
auto-bloqueo de D104).**

---

## 2. Línea (1): casi-periodicidad + finitud

### 2.1. Inventario incondicional exacto de la casi-periodicidad de ζ

**(a) Semiplano σ > 1: casi-periodicidad uniforme de Bohr.** En todo semiplano
σ ≥ 1+ε la serie de Dirichlet converge absolutamente; ζ es límite uniforme de los
polinomios trigonométricos Σ_{n≤N} n^{−σ}e^{−it log n} y por tanto **uniformemente
casi-periódica en el sentido de Bohr** [Boh: H. Bohr, *Zur Theorie der allgemeinen
Dirichletschen Reihen*, Math. Ann. 79 (1918); exposición en Besicovitch, *Almost
Periodic Functions*, Cambridge 1932]. Allí el argumento de réplica es vacuo: ζ no tiene
ceros en σ > 1 (producto de Euler). Nótese la ironía estructural: donde la
casi-periodicidad es uniforme, Euler ya mató los ceros; donde podría haber ceros, la
casi-periodicidad disponible se degrada a media cuadrática.

**(b) Franja ½ < σ < 1: NO hay casi-periodicidad uniforme, por razón trivial.** Una
función uniformemente casi-periódica sobre una recta vertical es acotada sobre ella
(Bohr). Pero lim sup_{t→∞} |ζ(σ+it)| = ∞ para todo σ ≤ 1 (Ω-teoremas clásicos;
[Tit86, Cap. VIII]). Por tanto ζ **no** es Bohr-casi-periódica en ninguna recta de la
franja, incondicionalmente. La ruta uniforme está cerrada de entrada — no por el muro,
sino por crecimiento.

**(c) Franja ½ < σ < 1: casi-periodicidad B² de Besicovitch — TEOREMA incondicional.**
Este es el enunciado exacto disponible:

**Lema 2.1 (ζ es B²-casi-periódica en cada recta de la franja).** Sea σ ∈ (½, 1) fijo y
$P_X(t) := \sum_{n\le X} n^{-\sigma - it}$. Entonces
$$\limsup_{T\to\infty} \frac1T \int_0^T \bigl|\zeta(\sigma+it) - P_X(t)\bigr|^2\,dt
\;\le\; C_\sigma \sum_{n > X} n^{-2\sigma} \;\xrightarrow[X\to\infty]{}\; 0.$$
En particular ζ(σ+i·) pertenece a la clase B² de Besicovitch y es B²-casi-periódica
(límite B² de polinomios trigonométricos con frecuencias {log n}).

*Demostración.* Por la fórmula aproximada ζ(s) = Σ_{n≤t} n^{−s} + O(t^{−σ}) para
σ ≥ σ₀ > 0, t ≥ 1 ([Tit86, Thm. 4.11] con x = t), la diferencia ζ(σ+it) − P_X(t) es,
para t > X, el polinomio de Dirichlet Σ_{X<n≤t} n^{−σ−it} más O(t^{−σ}). El teorema de
valor medio de Montgomery–Vaughan ([MV74]; o el cálculo clásico de [Tit86, §7.2]) da
$$\frac1T\int_X^T \Bigl|\sum_{X<n\le t} n^{-\sigma-it}\Bigr|^2 dt
\;\ll\; \sum_{X<n\le T} n^{-2\sigma}\Bigl(1 + \frac nT\Bigr)
\;\ll\; \sum_{n>X} n^{-2\sigma} + \frac{T^{1-2\sigma}\cdot T}{T},$$
y como σ > ½ el segundo término es T^{1−2σ} = o(1). El término O(t^{−σ}) contribuye
o(1) al promedio. Esto es el contenido del teorema clásico del valor medio cuadrático
∫₀^T|ζ(σ+it)|²dt ∼ ζ(2σ)T ([Tit86, Thm. 7.2]), refinado a la aproximación en media por
sumas parciales — todo incondicional. La pertenencia a B² y la B²-casi-periodicidad
siguen de la definición de la clase de Besicovitch como clausura B² de los polinomios
trigonométricos [Besicovitch 1932, Cap. II]. ∎

**Lema 2.2 (los casi-períodos B² son relativamente densos, con densidad inferior
positiva).** Para todo ε > 0, el conjunto
$$E_\varepsilon := \Bigl\{\tau \in \mathbb{R} :
\limsup_{T\to\infty}\frac1T\int_0^T |\zeta(\sigma+it+i\tau) - \zeta(\sigma+it)|^2\,dt
< \varepsilon^2\Bigr\}$$
es relativamente denso en ℝ y tiene densidad inferior positiva.

*Demostración.* Elíjase X = X(ε) con C_σ Σ_{n>X} n^{−2σ} < ε²/9 (Lema 2.1). El conjunto
$$K_\eta := \{\tau : \|\tau \log p / 2\pi\| < \eta \ \ \forall p \le X\}$$
(‖·‖ = distancia al entero más próximo) satisface, para η = η(ε, X) suficientemente
pequeño: |n^{-i\tau} − 1| < ε/(3‖P_X‖_{B^2} + 3) para todo n ≤ X — porque
log n = Σ_p a_p log p con Σ a_p ≤ log₂ X para n ≤ X, de modo que
‖τ log n/2π‖ ≤ (log₂X)·η. Para τ ∈ K_η, ‖P_X(·+τ) − P_X‖_∞ < ε/3, y por desigualdad
triangular en la seminorma B² (que es invariante por traslaciones fijas, pues el límite
del promedio sobre [0,T] no cambia al desplazar la ventana en una cantidad fija):
‖ζ(·+iτ) − ζ‖_{B²} ≤ ε/3 + ε/3 + ε/3. Falta ver que K_η es relativamente denso con
densidad positiva: los números {log p : p ≤ X} son linealmente independientes sobre ℚ
(factorización única: una relación Σ a_p log p = 0 con a_p ∈ ℤ da Π p^{a_p} = 1,
imposible salvo a_p ≡ 0). Por el teorema de Kronecker–Weyl, el flujo lineal
τ ↦ (τ log p/2π)_{p≤X} mod 1 es equidistribuido y minimal en el toro T^{π(X)} (es una
traslación de grupo de órbita densa); por minimalidad, todo segmento de órbita de
longitud ≥ L₀(η) visita el entorno básico, y por equidistribución la densidad de K_η es
(2η)^{π(X)} > 0. ∎

Hasta aquí todo es teorema. El insumo aritmético del Lema 2.2 es la independencia lineal
de {log p}: **factorización única — el esqueleto aditivo del producto de Euler — entra
ya en el nivel B², incondicionalmente** (registro para §3).

### 2.2. El argumento Bohr–Rouché congelado por H(m): el condicional es teorema

Aislamos primero el lema puntual que la línea entera necesita; después demostramos que,
con él, H(m) cae.

**Lema LP-112 (casi-periodicidad puntual secuencial; ABIERTO).** *Para todo disco
cerrado D ⊂ {½ < σ < 1} existe una sucesión τ_k → ∞ tal que*
$$\sup_{s \in D} |\zeta(s + i\tau_k) - \zeta(s)| \;\longrightarrow\; 0.$$

(Versión débil suficiente, LP-112⁻: para todo D y todo ε > 0 existe UN τ > altura(D)
con sup_D |ζ(s+iτ) − ζ(s)| < ε.)

**Teorema 2.3 (la implicación condicional, con prueba completa).** Si vale LP-112⁻
(en particular si vale LP-112), entonces ζ no puede tener un número finito y no nulo de
cuádruplos off-críticos: H(m) es contradictoria para todo 0 < m < ∞. Equivalentemente,
LP-112 ⟹ D-109 (m ∈ {0, ∞}), y por tanto LP-112 ∧ (m<∞) ⟹ RH.

*Demostración.* Supóngase H(m). Sea ρ₀ = β + iγ₀ un cero off-crítico, β = ½ + δ con
δ := δ_{j_0} > 0, γ₀ ≤ γ_max. Los ceros de ζ son aislados; elíjase
$$r := \tfrac12\min\bigl(\delta,\ 1-\beta,\ \mathrm{dist}(\rho_0,\, Z(\zeta)\setminus\{\rho_0\})\bigr) > 0,$$
de modo que el disco cerrado D := D̄(ρ₀, r) está contenido en la franja abierta
{½ + δ/2 < σ < 1} y ζ no se anula en D ∖ {ρ₀}; en particular
$$\eta := \min_{|s-\rho_0| = r} |\zeta(s)| > 0.$$
**Todas estas son constantes fijas del mundo H(m)** — este es el uso de (F1): sin H(m),
δ y η serían parámetros sobre los que haría falta uniformidad; con H(m) son números.

Aplíquese LP-112⁻ al disco D con ε := η/2 y con τ > γ_max + γ₀ + r + 1: existe τ con
$$\sup_{s \in D} |\zeta(s+i\tau) - \zeta(s)| < \eta/2 < \eta = \min_{\partial D}|\zeta|.$$
Por el teorema de Rouché aplicado en el contorno ∂D al par (ζ(s), ζ(s+iτ) − ζ(s)):
ζ(·+iτ) tiene en el interior de D el mismo número de ceros que ζ, es decir al menos uno
(la multiplicidad de ρ₀). Por tanto ζ tiene un cero ρ′ con |ρ′ − (ρ₀ + iτ)| < r.
Entonces:
- Re ρ′ ∈ (β − r, β + r) ⊆ (½ + δ/2, 1): el cero ρ′ es **off-crítico** (aquí se usa
  r < δ/2 ≤ δ_min/2 en el peor caso — la cuantificación pedida en el encargo: el radio
  de Rouché debe ser menor que la distancia del cero a la línea, y bajo H(m) eso es una
  elección admisible fija, no un límite degenerante);
- Im ρ′ > γ₀ + τ − r > γ_max: el cero ρ′ **no es ninguno de los 4m ceros de la lista**
  (F2): es un cero off-crítico nuevo.
Su cuádruplo {ρ′, ρ̄′, 1−ρ′, 1−ρ̄′} es un (m+1)-ésimo cuádruplo: contradicción con
H(m). Con LP-112 completo, la sucesión τ_k → ∞ produce (tomando τ_k con separaciones
> 2r) infinitos ceros off-críticos distintos, es decir m = ∞ directamente: esto da
D-109 en la forma m ≥ 1 ⟹ m = ∞. La última afirmación es la identidad del Doc 109
§4.5. ∎

**Observación (qué probó exactamente el Teorema 2.3).** La implicación objetivo
m<∞ ⟹ m=0 es, tal como anticipó el encargo, **exactamente** el enunciado que el
argumento Bohr–Rouché demuestra una vez que se dispone de la casi-periodicidad puntual
local. Más aún: H(m) hace el condicional **limpio** — sin uniformidades, sin constantes
que exploten, sin necesidad de densidad. Todo el peso del problema quedó comprimido en
LP-112. Las dos subsecciones siguientes miden ese lema con todas las herramientas
pedidas, y el resultado es negativo en una forma informativa.

### 2.3. El paso B² → puntual: tres intentos, tres fallas exactas

**(a) La seminorma de Besicovitch anula los compactos.**

**Observación 2.4.** Para toda ventana compacta fija K = [γ₀ − A, γ₀ + A] y toda
f localmente L²,
$$\|f \cdot \mathbf{1}_K\|_{B^2}^2 = \limsup_{T\to\infty}\frac1T\int_0^T |f|^2\mathbf{1}_K\,dt
= \limsup_{T\to\infty}\frac1T\int_K |f|^2\,dt = 0.$$
Por tanto la condición τ ∈ E_ε (Lema 2.2) **no contiene ninguna información** sobre
∫_K |ζ(σ+it+iτ) − ζ(σ+it)|²dt: una función puede tener seminorma B² arbitrariamente
pequeña y ser arbitrariamente grande sobre K. El cero off-crítico vive en la altura fija
γ₀ ≤ γ_max — un compacto. **La casi-periodicidad B² es ciega, por definición de la
seminorma, exactamente en el lugar donde está la señal.** Esta es la forma más desnuda
del gap del Doc 109 §4.4: no es que el control B² sea "demasiado débil" cuantitativamente
en la ventana — es que es idénticamente nulo sobre ella.

**(b) Subarmonicidad: el localizador funciona, el alimentador no existe.**

La herramienta sugerida en el encargo es correcta a medias, y conviene decir con
precisión cuál mitad. Para g holomorfa, |g|² es subarmónica, y para todo z ∈ D(ρ₀, r):
$$|g(z)|^2 \;\le\; \frac{1}{\pi r^2}\iint_{D(z,r)} |g|^2\,dA
\;\le\; \frac{1}{\pi r^2}\iint_{D(\rho_0, 2r)} |g|^2\,dA,$$
de modo que
$$\sup_{D(\rho_0,r)} |\zeta(\cdot+i\tau)-\zeta|^2 \;\le\; \frac{1}{\pi r^2}
\iint_{D(\rho_0,2r)} |\zeta(s+i\tau)-\zeta(s)|^2\,dA(s). \tag{2.1}$$
El paso media-local-L² → sup está, pues, GRATIS: **si** algún τ hace pequeña la
integral de área sobre el disco fijo D(ρ₀, 2r), Rouché se activa. El problema es
alimentar (2.1). Las dos fuentes disponibles fallan así:

**Lema 2.5 (el promedio completo en τ no es pequeño: cálculo cerrado).** Para s₀ = σ+it₀
fijo con ½ < σ < 1,
$$\lim_{T\to\infty} \frac1T \int_0^T |\zeta(s_0 + i\tau) - \zeta(s_0)|^2\,d\tau
\;=\; \zeta(2\sigma) - 1 + |\zeta(s_0) - 1|^2 \;\ge\; \zeta(2\sigma) - 1 \;>\; 0.$$

*Demostración.* Expandiendo el cuadrado, bastan dos valores medios clásicos e
incondicionales. (i) (1/T)∫₀^T |ζ(s₀+iτ)|²dτ → ζ(2σ) ([Tit86, Thm. 7.2]; el
desplazamiento fijo t₀ no altera el límite). (ii) (1/T)∫₀^T ζ(s₀+iτ)dτ → 1: por
Cauchy–Schwarz y el Lema 2.1, |media(ζ − P_X)| ≤ ‖ζ−P_X‖_{B²} → 0 cuando X → ∞,
mientras que la media de P_X(s₀+iτ) en τ es 1 + Σ_{2≤n≤X} n^{−σ−it₀}·media(n^{−iτ}) → 1
(cada n^{−iτ}, n ≥ 2, tiene media 0). Entonces el límite del promedio es
ζ(2σ) − 2Re(\overline{ζ(s₀)}·1) + |ζ(s₀)|² = ζ(2σ) − 1 + |ζ(s₀)−1|². ∎

Integrando el Lema 2.5 en s₀ sobre D(ρ₀, 2r) (convergencia dominada sobre el compacto,
con las cotas polinomiales estándar de ζ en la franja), el promedio en τ del lado derecho
de (2.1) tiende a un límite **estrictamente positivo y acotado por debajo**. Conclusión:
el promedio completo en τ no produce ninguna sucesión buena — y tampoco la prohíbe (un
promedio acotado por debajo es compatible con un conjunto de τ de densidad positiva donde
el integrando es minúsculo). La subarmonicidad reduce LP-112 a "hacer pequeña una
integral de área local para algún τ", pero ni el promedio total (Lema 2.5: no es chico)
ni el promedio restringido a E_ε (Obs. 2.4: no ve la ventana) la controlan. El
localizador existe; el alimentador, no.

**(c) Normalidad/Montel: compacidad sin selección.** La familia {ζ(·+iτ)}_τ restringida
a un entorno acotado de D es localmente acotada en media (Lema 2.5 + (2.1) dan cotas
local-uniformes a lo largo de sub-sucesiones de τ con integral de área acotada — que
existen por el propio Lema 2.5 y Chebyshev) y por tanto normal en sub-sucesiones: hay
τ_k → ∞ y g holomorfa con ζ(·+iτ_k) → g uniformemente en D. Montel **garantiza límites,
no identifica cuáles**: el conjunto de límites posibles es (por el teorema límite de
Bagchi, §2.4) el soporte de la medida de Bagchi, y la pregunta de si ζ|_D está entre
ellos es exactamente LP-112. La normalidad re-enuncia el problema; no lo resuelve.

### 2.4. La proposición de densidad cero: la dirección distribucional, probada en contra

Lo anterior muestra que las herramientas de promedio no alimentan a Rouché. Lo siguiente
muestra algo más fuerte y más interesante: bajo la hipótesis H(m) que queremos refutar,
**el conjunto de τ que alimentarían a Rouché tiene densidad cero** — la maquinaria
distribucional no es neutral: certifica que los testigos de LP-112 son excepcionales.

**Proposición 2.6 (densidad superior cero de los τ buenos).** Asúmase H(m) con m ≥ 1 y
sean ρ₀, r, η como en la prueba del Teorema 2.3. Para todo ε < η, el conjunto
$$A_\varepsilon := \Bigl\{\tau > 0 : \sup_{|s-\rho_0|\le r} |\zeta(s+i\tau) - \zeta(s)| \le \varepsilon\Bigr\}$$
tiene densidad superior cero:
$\limsup_{T\to\infty} T^{-1}\,\mathrm{meas}(A_\varepsilon \cap [0,T]) = 0$.

*Demostración.* Sea D′ un disco abierto con D̄(ρ₀,r) ⊂ D′ ⊂ D̄′ ⊂ {½<σ<1}. El teorema
límite funcional de Bagchi (incondicional; [Bag81], exposición completa en [Lau96,
Cap. 5]): las medidas Q_T(·) := T^{-1}\,\mathrm{meas}\{τ ∈ [0,T] : ζ(·+iτ)|_{D′} ∈ ·\}
convergen débilmente, en el espacio H(D′) de funciones holomorfas con la topología
compacto-abierta, a la ley Q del elemento aleatorio ζ(s,ω) = Π_p (1 − ω_p p^{−s})^{−1}
(producto de Euler aleatorio, ω = (ω_p) uniforme en el toro Π_p S¹; el producto converge
en H(D′) casi seguramente). El soporte de Q es
$$S \;=\; \{f \in H(D') : f(s) \ne 0 \ \forall s \in D'\} \cup \{0\}$$
([Bag81]; [Lau96, Cap. 6]; es el ingrediente estándar de los teoremas de universalidad:
los límites de productos de Euler no-nulos son no-nulos o idénticamente nulos, Hurwitz).

Considérese el conjunto C_ε := {f ∈ H(D′) : sup_{D̄(ρ₀,r)} |f − ζ| ≤ ε}, cerrado en
H(D′). Afirmamos C_ε ∩ S = ∅ para ε < η. En efecto, si f ∈ C_ε: sobre el círculo
|s−ρ₀| = r se tiene |f − ζ| ≤ ε < η = min |ζ|, y Rouché da a f un cero en D(ρ₀, r),
luego f ∉ S salvo que f ≡ 0; pero f ≡ 0 daría sup_{D̄}|ζ| ≤ ε < η ≤ sup_{∂D}|ζ|,
absurdo. Entonces Q(C_ε) = 0 (un cerrado disjunto del soporte tiene medida nula) y, por
el teorema de Portmanteau para cerrados,
$$\limsup_T \frac{\mathrm{meas}(A_\varepsilon\cap[0,T])}{T} \;\le\; \limsup_T Q_T(C_\varepsilon) \;\le\; Q(C_\varepsilon) \;=\; 0. \qquad\blacksquare$$

**Lectura.** La Proposición 2.6 es la mitad fácil de Bagchi (un cero off-crítico
destruye la recurrencia fuerte; Doc 102, Doc 109 §4.3) afilada a su forma cuantitativa:
no solo "la densidad no es positiva" — es cero. Sus consecuencias para este documento:

1. **La esperanza de la medida positiva era falsa.** El encargo preguntaba: "si los
   casi-períodos buenos existen (medida positiva) y cada uno produce una réplica, listo
   — ¿dónde exactamente puede fallar?". Falla aquí: los casi-períodos B² tienen densidad
   positiva (Lema 2.2), pero los τ útiles para Rouché en el disco específico tienen
   densidad cero (Prop. 2.6). No hay contradicción entre ambos enunciados porque la
   bondad B² es una media en t que pesa 0 sobre la ventana del cero (Obs. 2.4). **La
   positividad de medida vive en la coordenada equivocada.**
2. **El muro tiene signo.** No es solo que no sepamos probar LP-112: sabemos que sus
   testigos, si existen, forman un conjunto que toda la maquinaria distribucional
   (equidistribución de Bagchi, momentos, B²) clasifica como excepcional. Producir un
   elemento de un conjunto de densidad cero definido por una condición individual es el
   Principio 3.1 de P43 — "el objeto vive en el conjunto excepcional de su propio
   comportamiento genérico" — en coordenadas de casi-períodos.
3. **Simetría reveladora.** Bajo RH, el conjunto análogo A_ε tiene densidad inferior
   POSITIVA para todo disco (recurrencia fuerte, mitad difícil de Bagchi [Bag87], que
   usa que ζ|_D es no-nula y está en el soporte). La densidad de A_ε es, pues, un
   detector perfecto de los dos mundos: positiva bajo RH, cero bajo ¬RH. Como detector
   es inútil (evaluar la densidad requiere lo que queremos probar), pero explica por qué
   la recurrencia fuerte es RH-equivalente y la secuencial no: la frontera entre
   "densidad positiva" y "densidad cero pero no vacío" es exactamente la frontera entre
   RH y D-109.

### 2.5. ¿Aplica el auto-bloqueo de D104? No — y la diferencia es estructural

**Proposición 2.7 (la versión secuencial no se auto-bloquea).** La conclusión del
Teorema 2.3 bajo LP-112 (una familia de ceros off-críticos en las alturas γ₀ + τ_k,
k ∈ ℕ) es consistente con todos los teoremas de densidad de ceros conocidos, para
cualquier sucesión τ_k → ∞, incluso de contado arbitrariamente lento.

*Demostración.* Los ceros producidos hasta altura T son a lo sumo
#{k : τ_k ≤ T} + 4m = o(T^θ) para cualquier θ > 0 si τ_k crece suficientemente rápido,
y en todo caso O(#{k: τ_k ≤ T}), que no está acotado por debajo por ninguna función
creciente: la conclusión no impone densidad. Los teoremas de densidad
(N(σ,T) ≪ T^{κ(σ)}, D111 §2.3) acotan por arriba; una familia numerable rala los
satisface trivialmente. ∎

Contraste exacto con D104 (vía P43, Thm. C): el amplificador de la Forma C necesitaba
convertir un cero en una familia de **densidad positiva anclada**, y esa densidad estaba
capada por el techo incondicional N(σ,T) = O(T^{κ(σ)}) **con el mismo exponente**: la
mejora que alimentaba al amplificador alimentaba también al techo — auto-bloqueo. La
pregunta decisiva del encargo ("¿el bloqueo de D104 aplica cuando solo se necesita UNA
réplica?") tiene respuesta limpia: **no aplica**. La necesidad bajó de densidad positiva
a densidad cero, y contra densidad cero no hay techo. El precio: tampoco hay maquinaria
de producción — los métodos que fabrican τ's (equidistribución, medias) fabrican
genéricos, y el genérico es malo (Prop. 2.6). El bloqueo cambió de naturaleza: de
*auto-contradicción interna* (D104) a *ausencia de alimentador* (aquí). Esa diferencia
es la que deja vivo a LP-112 como objetivo (§5.4).

### 2.6. Cuantificación final del paso de Rouché bajo H(m)

Registro explícito de la cuantificación pedida, porque muestra qué compró exactamente la
finitud. Sin H(m) (es decir, atacando directamente m = 0 por recurrencia), el radio r y
el margen η degeneran con δ → 0 y γ₀ → ∞, y cualquier control debe ser uniforme en la
configuración — la situación de Bagchi, RH-equivalente. Bajo H(m):

- r < δ/2 garantiza réplica off-crítica; r es una constante fija (F1). **No hay
  explosión de constantes:** la pareja (ε, r) = (η/2, r(ρ₀)) es un dato fijo del mundo
  hipotético.
- El umbral de altura τ > γ_max + γ₀ + r + 1 garantiza novedad de la réplica (F2).
- UNA réplica basta (F4); infinitas dan m = ∞ directamente.

El gap restante es exactamente uno: **la existencia de un solo τ en el conjunto A_ε de
la Prop. 2.6.** Nada más falta. GAP ABIERTO (= LP-112⁻ para el disco D(ρ₀,r)).

---

## 3. Línea (2): el rol del producto de Euler — la separación de los contraejemplos

La Prop. 2.2 del Doc 111 obliga: los cosh-ejemplos F = P₁⋯P_m·cosh(a(s−½)) tienen
m cuádruplos, ecuación funcional, orden 1 — y m finito es REALIZADO en esa clase. Toda
prueba (aun condicional) de m<∞ ⟹ m=0 debe usar algo que ellos no tienen. Verificamos
que la línea (1) lo hace, localizando el insumo con precisión de lema.

### 3.1. Los cosh-ejemplos quedan fuera ya en el nivel B²

**Lema 3.1 (los cosh-ejemplos no son B² sobre rectas verticales).** Sea
F = P·F₀ con P = P₁⋯P_m (polinomio de grado 4m, m ≥ 1) y F₀(s) = cosh(a(s−½)).
Para todo σ ∈ (0,1) fijo,
$$\frac1{2T}\int_{-T}^{T} |F(\sigma+it)|^2\,dt \;\asymp\; T^{8m} \;\longrightarrow\; \infty.$$
En particular F(σ+i·) ∉ B² y F no es B²-casi-periódica en ninguna recta vertical.

*Demostración.* |P(σ+it)| ≍ |t|^{4m} cuando |t| → ∞ (término dominante del polinomio),
y |F₀(σ+it)|² = sinh²(a(σ−½)) + cos²(at) ∈ [sinh²(a(σ−½)), cosh²(a(σ−½))], acotado
entre constantes positivas para σ ≠ ½ (y entre 0 y 1 para σ = ½, con media ½ del
cos²). Entonces el integrando es ≍ t^{8m} y el promedio ≍ T^{8m}/(8m+1). ∎

**Lema 3.2 (los cosh-ejemplos no admiten ninguna auto-aproximación secuencial).** Con F
como arriba y D = D̄(ρ₀, r) un disco alrededor de un cero off-crítico ρ₀ de F con
D ∩ {σ = ½} = ∅: no existe ninguna sucesión τ_k → ∞ con
sup_D |F(s+iτ_k) − F(s)| → 0. Es decir, el análogo de LP-112 para F es **falso**.

*Demostración.* Para s ∈ D: |F(s+iτ)| ≥ |P(s+iτ)|·sinh(a·min_D|σ−½|) ≥ c_D·τ^{4m} → ∞
(P tiene grado 4m ≥ 4 y |s + iτ| ≥ τ − |ρ₀| − r), mientras sup_D |F| < ∞. La diferencia
no puede tender a 0. ∎

Esto disuelve el riesgo de circularidad señalado por D111: la ruta del Teorema 2.3 no
es un argumento "físico" (simetría + crecimiento) — su insumo, la auto-aproximación, es
falso en la clase ℰ con m ≥ 1. Consistencia perfecta: el Teorema 2.3 dice
"auto-aproximación ⟹ m ∈ {0,∞}", los cosh-ejemplos tienen m finito no nulo, y
efectivamente no se auto-aproximan.

### 3.2. Frecuencia única vs. toro de Kronecker: la no-discretitud como lema

La estructura de los cosh-ejemplos sin el factor polinómico ilumina el mecanismo. F₀ es
**exactamente periódica** en t con período 2π/a: su grupo de períodos es discreto, y la
traslación por un período mapea el conjunto de ceros sobre sí mismo — la "réplica" del
cero cae sobre un cero que ya estaba. Una casi-periodicidad de grupo discreto no
multiplica nada. La pregunta del encargo: ¿qué propiedad exacta del conjunto de
casi-períodos separa a ζ, y es incondicional?

**Lema 3.3 (no-discretitud aritmética de los casi-períodos de ζ).** (a) ζ no es
periódica en t en ninguna sub-banda de σ > ½: si ζ(s+iτ₀) = ζ(s) en un abierto,
entonces (continuación analítica al semiplano σ > 1 y unicidad de coeficientes de
series de Dirichlet) n^{−iτ₀} = 1 para todo n ≥ 2, es decir τ₀ log n ∈ 2πℤ para todo n;
con n = 2, 3 esto fuerza log 2/log 3 ∈ ℚ, es decir 2^q = 3^p con p, q ∈ ℤ no ambos
nulos — imposible por factorización única. Luego τ₀ = 0.
(b) Para todo ε > 0, el conjunto E_ε de casi-períodos B² (Lema 2.2) es relativamente
denso y **no está contenido en ningún subgrupo discreto de ℝ**: contiene al conjunto de
Kronecker K_η, y K_η ⊂ cℤ es imposible porque K_η tiene densidad (2η)^{π(X)} que, por
equidistribución, se realiza en intervalos de toda posición, mientras que la densidad de
cualquier subconjunto de cℤ está soportada en una progresión aritmética — basta tomar η
con (2η)^{π(X)} mayor que 0 y observar que K_η es abierto (unión de intervalos de
longitud positiva: si τ ∈ K_η, un entorno de τ está en K_{η'}, η' próximo), y un abierto
no vacío no cabe en un conjunto discreto.

*Demostración.* Contenida en el enunciado; el único insumo no trivial es la
irracionalidad de log 2/log 3 (factorización única) y la equidistribución de Weyl ya
usada en el Lema 2.2. ∎

**Síntesis de la separación (respuesta exacta a la pregunta (2) del encargo).** La
propiedad que separa a ζ de los contraejemplos, en cada nivel:

| nivel | ζ | cosh-ejemplos (m ≥ 1) | insumo de ζ |
|---|---|---|---|
| B²-casi-periodicidad en la franja | **teorema** (Lema 2.1) | falso (Lema 3.1) | serie de Dirichlet con Σ\|a_n\|²n^{−2σ} < ∞ |
| casi-períodos relativamente densos y no-discretos | **teorema** (Lemas 2.2, 3.3) | grupo de períodos discreto (solo F₀); ninguno (F) | independencia ℚ-lineal de {log p} = factorización única — incondicional, aritmética pura |
| réplicas en alturas NUEVAS | automático bajo H(m) (alturas γ₀+τ_k → ∞, lista off finita) | la traslación periódica fija el conjunto de ceros | — |
| soporte del teorema límite (Bagchi) | producto de Euler aleatorio: S = {no-nulas} ∪ {0} | sin análogo | **producto de Euler completo**, con coordenadas ω_p independientes |
| transferencia puntual (LP-112) | **GAP ABIERTO** | falso (Lema 3.2) | — |

El producto de Euler entra entonces en tres lugares, de fuerza creciente: como serie de
Dirichlet (nivel B²), como independencia de {log p} (nivel Kronecker: densidad relativa
y no-discretitud de los casi-períodos — el toro infinito-dimensional del encargo), y
como producto aleatorio de coordenadas independientes (nivel Bagchi: la estructura del
soporte, usada tanto en la Prop. 2.6 como en la dirección RH ⟹ recurrencia fuerte).
Los dos primeros son incondicionales y ya están al servicio del argumento; el tercero
es el que gobierna la frontera entre densidad positiva y cero.

### 3.3. Calibración con Davenport–Heilbronn: qué decide Euler y qué no

Control de sanidad. La función de Davenport–Heilbronn (serie de Dirichlet, ecuación
funcional tipo Riemann, SIN producto de Euler; D111 Obs. 2.4) es B²-casi-periódica en
la franja por el mismo Lema 2.1 (solo usa la serie y el valor medio cuadrático, válidos
para combinaciones lineales de L-funciones), y tiene **infinitos** ceros off-críticos
[DH36]. Es decir: en la clase "serie de Dirichlet + ecuación funcional", el patrón
m ∈ {0,∞} es hasta hoy consistente — el ejemplar sin Euler realizó la alternativa
m = ∞, no el m finito. Esto sugiere (no prueba) que la dicotomía D-109 podría valer en
la clase intermedia completa, con la casi-periodicidad de la serie como único motor; el
producto de Euler completo sería entonces el responsable no de la dicotomía sino de la
**alternativa** m = 0 (positividad de Weil / soporte de Bagchi). GAP declarado (D111
Obs. 2.4): no se conoce ejemplar de la clase intermedia con m finito no nulo, ni prueba
de su imposibilidad. Para este documento la calibración basta: la ruta del Teorema 2.3
usa insumos que la clase ℰ no tiene (Lemas 3.1–3.2), cumpliendo el requisito del
Cor. 2.3 de D111.

---

## 4. Línea (3): trazas de Newton y el sistema de momentos finito

### 4.1. Rango finito no es rango finito a priori

La Prop. 4.5 del Doc 110: en rango finito **conocido a priori** n, las n trazas
t_j = tr(Q^j) determinan la inercia (Newton + Jacobi–Frobenius, [Gan59, Vol. 2,
Cap. X]). Bajo H(m), la forma Q restringida a 𝒦_off tiene rango 4m — finito. Pero el
axioma L6 del Doc 110 pide dimensión acotada **por datos aritméticos, no por ceros**:
aquí la dimensión es 4m con m el desconocido del problema. La distinción no es
pedantería: el procedimiento Newton–Frobenius necesita saber cuántas trazas calcular y
contra qué Hankel testear; con n desconocido, el dato accesible es una sucesión infinita
de presuntas trazas cuya estabilización en rango ≤ 4m es indistinguible, a cualquier
etapa finita, de un rango mayor con autovalores pequeños. Esto es la Obs. 6.3 del
Doc 111 (el receptáculo mide, no acota) en versión de momentos. No obstante, hay un
matiz a favor que el encargo señala bien: para REFUTAR H(m) no necesitamos leer m —
necesitamos solo derivar una inconsistencia. Veamos si el sistema lo permite.

### 4.2. El sistema de momentos bajo H(m): el lado espectral es transparente

Lado espectral (de ceros): bajo H(m), el costo de cada cuádruplo en la traza CCM es
2δ_j²K_λ(γ_j)(1+o(1)) (Doc 98, Cor. 2.4, citado y usado en D111 §6.2(a)), con
K_λ(γ) > 0 explícito y decayendo como la densidad dm_∞ ≍ |γ|^{−1/2}e^{−π|γ|/2}
(Doc 95, Lema 2.2, vía D111). Por tanto
$$T_\lambda \;=\; \sum_{j=1}^{m} 2\delta_j^2\,K_\lambda(\gamma_j)\,(1+o(1))
\;>\; 0 \qquad \text{para todo } \lambda \text{ en el rango efectivo},\tag{4.1}$$
una **suma finita** de funciones explícitas de los 4m parámetros — exactamente la
estructura "momentos de una medida atómica finita" que el encargo pedía.

**Lema 4.1 (determinación finita; álgebra clásica).** Una medida atómica positiva
μ = Σ_{j≤k} c_j δ_{x_j} (c_j > 0, x_j distintos, k conocido) está determinada por sus
2k momentos de potencias s_i = Σ c_j x_j^i, i = 0,…,2k−1: el rango de la matriz de
Hankel (s_{i+i'}) detecta k, el polinomio nodal se recupera por el sistema de
Prony/Newton, y los pesos por Vandermonde. [Gan59, Vol. 2, Cap. X]; teoría clásica de
momentos finitos de Hamburger [Akh65]. El problema de momentos finito es **determinado**:
no hay indeterminación tipo Hamburger en rango finito. ∎

De modo que, en el plano idealizado: si un oráculo entregara los valores exactos de una
familia adecuada {T_{λ_i}} (o de T_λ y sus derivadas en λ — la familia de núcleos K_λ
jugando el papel de las potencias; la separación efectiva de parámetros por la familia
{K_λ(·)} es plausible pero NO la afirmamos: no es load-bearing, porque la ruta muere
antes), los parámetros {(δ_j, γ_j)} quedarían determinados, y "lista vacía" sería
detectable: T_λ ≡ 0. Esto está bien y es la traducción correcta de la Prop. 4.5 del
Doc 110 al problema. Todo el peso cae entonces en: ¿hay valores autónomos que alimenten
el sistema?

### 4.3. La estructura de D72, verificada en fuente, y los dos muros reales

Verificación directa contra el Doc 72 (hecha para este documento):

- **Thm. 4.1 (D72):** T_λ = A_λ^{off} − Σ_p (log p/√p)·B_λ(log p) + O(p^{−1}-colas),
  donde A_λ^{off} es la contribución de los ceros off-críticos (cero bajo RH) y
  $$B_\lambda(\log p) \;=\; \int W_\lambda(s)\cos(s\log p)\,dm_\infty(s).$$
- **Hallazgo de la verificación (el temor del encargo era infundado):** B_λ(log p) es la
  transformada de Fourier del test W_λ·w en la frecuencia log p — un objeto
  **completamente autónomo** (depende del núcleo CCM y de dm_∞, no de los ceros). El
  Doc 72 lo construye como Σ_{n≤N(λ)} n∫|P_n|²cos(s log p)dm_∞ — polinomios de Jacobi
  CCM, datos del operador, sin posiciones de ceros. La sospecha "B_λ depende de TODOS
  los ceros vía la fórmula explícita" es falsa: lo que depende de los ceros es el OTRO
  lado de la identidad.
- **El primer muro real (Doc 105, vía Doc 109 §6.1):** la serie de primos
  Σ_p (log p/√p)B_λ(log p) **diverge**, como (5√2/8)·log X sobre los primos p ≤ X: el
  test CCM W_λ·w está en la frontera de la clase de Weil y la fórmula de D72 es
  estrictamente formal. **No existe hoy el "valor aritmético de T_λ" que el sistema de
  momentos necesita como alimento** — ni siquiera regularizado sin pasar por los ceros.
  El sistema de la §4.2 está bien planteado y sin datos.

- **El segundo muro, independiente del primero (estructural):**

**Proposición 4.2 (la fórmula explícita no sobredetermina: tautología de identidades).**
Asúmase H(m) y concédase, contra el Doc 105, una regularización convergente de la
fórmula de D72 (o úsese cualquier test h de la clase de Weil legítima, donde la fórmula
explícita es un teorema). Entonces el sistema de ecuaciones obtenible evaluando la
fórmula explícita sobre cualquier familia {h_i} de tests es **consistente por
construcción** con la configuración verdadera de parámetros, y no puede derivar
contradicción de H(m) sin un insumo de signo. Con precisión: para cada test h, la
identidad de Weil dice
$$\underbrace{\widehat h(\tfrac i2) + \widehat h(-\tfrac i2)
- \sum_{n} \frac{\Lambda(n)}{\sqrt n}\,(h(\log n) + h(-\log n)) + \mathcal{A}_\infty(h)}_{\text{autónomo}}
\;=\; \sum_{\rho} \widehat h\Bigl(\frac{\rho - 1/2}{i}\Bigr)
= F_{\mathrm{on}}(h) + F_{\mathrm{off}}(h;\,\{\delta_j,\gamma_j\}),$$
y el único modo de eliminar el término no-autónomo F_on (los ceros on-line, que H(m) no
fija) es restarse la misma identidad — toda combinación lineal de instancias de la
fórmula explícita es otra instancia: hay **una sola** identidad aritmética independiente,
y la configuración verdadera la satisface idénticamente. Un sistema de identidades
satisfechas idénticamente no restringe los parámetros; restringe solo si se le añade
información de SIGNO (h en un cono con Σ_ρ ĥ ≥ 0 forzado u obstruido), y "el lado
aritmético es ≥ 0 para todo h del cono de Weil" es el criterio de Weil — equivalente a
RH (y su verificación es el problema de inercia: P43 §4, Doc 108).

*Demostración (estructural, con su estatus declarado).* (i) La fórmula explícita para ζ
es una identidad entre funcionales lineales del test, válida en todo mundo (RH o ¬RH):
evaluar ambos lados no produce condiciones sobre el mundo sino sobre el test. (ii) El
intento "global menos predicción on-line": defínase ξ_on := ξ/P_m con
P_m(s) = Π_j((s−½)² − (δ_j+iγ_j)²)((s−½)² − (δ_j−iγ_j)²) (el polinomio de D111
Prop. 2.2); ξ_on es entera de orden 1 con todos sus ceros on-line, y
Σ_{ρ on} ĥ = Σ_{ρ} ĥ − F_off(h; params). Sustituyendo en cualquier ecuación que
involucre "la predicción on-line", esta queda expresada como (lado autónomo de Weil)
menos F_off: al formar "valor global − predicción on-line" el lado autónomo aparece en
ambos términos con el mismo coeficiente y se cancela, dejando F_off = F_off — la
tautología anunciada. ξ_on NO tiene serie de Dirichlet ni producto de Euler propios
(dividir por un polinomio en s destruye la estructura multiplicativa), de modo que no
existe una segunda fórmula explícita independiente que romper la circularidad.
(iii) Que el contenido no-tautológico restante es exactamente el de signo: es el
contenido del criterio de Weil [Wei52] y de la cadena Doc 108 → P43 §4 (la detección de
F_off ≠ 0 mediante desigualdades es la lectura de la inercia, no del valor). Como en
D111 Prop. 6.2(c), esto se afirma con prueba sobre las manipulaciones catalogadas
(combinaciones lineales de instancias de la fórmula explícita y eliminaciones
algebraicas de F_on), no como clasificación de "toda manipulación concebible": GAP
declarado en esa generalidad. ∎

**Observación 4.3 (la precisión requerida, y dónde se esconde el cuantificador).** Aun
ignorando la Prop. 4.2 — supóngase que una regularización R del lado de primos fuera
computable y que "R = 0 vs R = T_λ > 0" fuera el test. Bajo H(m) el gap es
ε₀ = Σ_j 2δ_j²K_λ(γ_j) > 0 — **una constante positiva fija del mundo hipotético**, no
una precisión evanescente: esto parece esquivar el muro de segundo orden o(1/log T) del
Doc 108. Pero la contradicción debe derivarse para TODA configuración finita admisible
(H(m) cuantifica existencialmente sobre configuraciones), y
$$\inf_{\substack{m \ge 1,\ \delta_j > 0,\ \gamma_j > 3\cdot10^{12}}} \;\sum_j 2\delta_j^2 K_\lambda(\gamma_j) \;=\; 0$$
(δ → 0, o γ → ∞ con K_λ(γ) ≍ γ^{−1/2}e^{−πγ/2}: el costo evanescente de D111
Prop. 6.2(a)). El argumento por momentos necesitaría entonces evaluar R con error menor
que un ínfimo igual a cero — es decir, exactamente: la uniformidad sobre el espacio de
hipótesis restaura el cuantificador que la finitud parecía haber congelado. La
diferencia con la línea (1) es instructiva: allí H(m) congela las constantes PORQUE el
mecanismo (Rouché) es local al mundo hipotético y la contradicción es interna (m+1 > m);
aquí el mecanismo (evaluación aritmética) debe funcionar uniformemente sobre mundos,
porque el valor aritmético es uno solo y las configuraciones candidatas son todas.
**La finitud protege a los argumentos internos al mundo; no protege a los evaluadores
externos.**

### 4.4. Dictamen de la línea (3)

**BLOQUEADA, en dos lugares independientes y nombrados:** (i) el alimento del sistema de
momentos no existe — la serie de primos de D72 diverge (Doc 105) y no hay valor autónomo
de T_λ, ni formal-regularizado, sin pasar por los ceros; (ii) aun con alimento, las
identidades disponibles son tautológicas en los parámetros (Prop. 4.2) y el contenido
no-tautológico es el signo — la inercia de P43; además (iii) la precisión requerida se
des-congela al cuantificar sobre configuraciones (Obs. 4.3). El hallazgo positivo de la
línea: la estructura de momentos finitos es la correcta (Lema 4.1: determinación, sin
patología de Hamburger) y B_λ es autónomo — el problema NO está en la accesibilidad del
test sino en la del valor espectral. La línea (3) es la Prop. 4.5 del Doc 110 chocando
con la frontera exacta que el propio Doc 110 trazó: rango finito sí, a-priori no.

---

## 5. Línea (4): el mejor teorema demostrable hoy

### 5.1. Candidato (A): la implicación completa — NO demostrable hoy; búsqueda activa del error

Por disciplina del encargo, buscamos activamente el error en el camino que más cerca
estuvo de cerrar: el §2 completo. El punto exacto donde una prueba ingenua se fabrica
sola es el paso del Lema 2.2 al Teorema 2.3: "los casi-períodos tienen densidad
positiva, luego alguno sirve para el disco". La Prop. 2.6 demuestra que ese paso es
**falso como inferencia de medidas**: bondad-B² (densidad positiva) y bondad-en-el-disco
(densidad cero) son eventos casi disjuntos, y la intersección no está garantizada
no-vacía por ningún argumento de medida — al contrario, la bondad-en-el-disco es
excepcional. El precedente de D104 ("algo falla en el paso B²→puntual") queda confirmado
y precisado: lo que falla no es una estimación mejorable sino la dirección de la
maquinaria distribucional. No hay prueba de (A) hoy. Tampoco refutación de la
implicación: ningún contraejemplo es posible dentro de las clases construibles (un
contraejemplo sería un mundo con ζ teniendo m finito no nulo — eso es ¬RH constructivo).

### 5.2. Candidato (B): versiones por regiones de parámetros — vacías

¿Existe f tal que H(m) ∧ (δ_min > f(γ_max)) sea contradictorio? Inventario: la única
región (δ, γ₀) excluida incondicionalmente es la clásica
{γ₀ ≤ 3·10¹²} ∪ {δ > ½ − c(log γ₀)^{−2/3}(log log γ₀)^{−1/3}} (D111 §2.4), que no usa
ni necesita H(m). ¿Agrega H(m) palanca regional? Las palancas catalogadas: Siegel-repulsión
(no existe para cuádruplos: D111 §3, anti-Siegel), Turán (circular: D111 §4),
positividades parciales (regímenes disjuntos del de visibilidad: D111 §2.4(a)). Ninguna
mejora con m finito — todas fallan por razones independientes del cardinal (presupuesto
creciente, circularidad de la cota superior, sub-resolución). El §2 tampoco da región:
la Prop. 2.6 vale para todo (δ, γ₀) no excluido. **Nada que declarar: (B) coincide con
lo clásico.**

### 5.3. Candidato (C): m = 1 — el caso mínimo no evita nada

Con m = 1 las constantes del Teorema 2.3 son máximamente concretas (un solo cuádruplo,
r = δ/2 ∧ …) y el umbral de contradicción es mínimo (una réplica). Pero la Prop. 2.6 se
aplica verbatim: su prueba usa UN cero off-crítico en el disco — m = 1 es exactamente su
caso. El conjunto A_ε sigue siendo de densidad cero; el alimentador sigue sin existir.
La uniformidad nunca fue el problema bajo H(m) (ya estaba congelada para todo m finito,
§2.6); el problema es la existencia del τ excepcional, y esa dificultad es independiente
de m. **m = 1 no es más fácil que m finito general.** (Registro simétrico: tampoco es
más difícil — la anti-repulsión de D111 §3 dice que los cuádruplos no interactúan.)

### 5.4. Candidato (D): la reducción limpia — TEOREMA, y el análisis de no-equivalencia

**Teorema 5.1 (reducción exacta de la dicotomía).** Vale incondicionalmente:
$$\text{LP-112} \;\Longrightarrow\; \bigl(m \in \{0, \infty\}\bigr) = \text{D-109},
\qquad\text{y por tanto}\qquad
\bigl(m < \infty\bigr) \wedge \text{LP-112} \;\Longrightarrow\; \mathrm{RH}.$$
Con la identidad del Doc 109 §4.5: RH ⟺ (m<∞) ∧ D-109 ⟸ (diana L8) ∧ LP-112.

*Demostración.* Teorema 2.3. ∎

**Jerarquía de casi-periodicidad y posición exacta de LP-112.**

| enunciado | estatus | consecuencia sobre m |
|---|---|---|
| ζ uniformemente Bohr-a.p. en una sub-banda de la franja | **FALSO** (Ω-teoremas, §2.1(b)) | (vacuo) |
| recurrencia fuerte de Bagchi (densidad inferior positiva de τ buenos, todo disco) | ⟺ RH [Bag87] | m = 0 |
| **LP-112** (sucesión no acotada de τ buenos, todo disco) | **ABIERTO** | m ∈ {0,∞} (Thm. 5.1) |
| casi-periodicidad B² (densidad positiva de casi-períodos en media) | **TEOREMA** (Lemas 2.1–2.2) | ninguna (Obs. 2.4) |

LP-112 es el peldaño mínimo suficiente: estrictamente más débil que la recurrencia
fuerte (pide una sucesión donde aquella pide densidad inferior positiva) y estrictamente
más fuerte que B² (pide control puntual sobre un compacto, que B² no da).

**Análisis de no-equivalencia con RH (triple chequeo pedido):**

1. **RH ⟹ LP-112.** Bajo RH, ζ es fuertemente recurrente (mitad difícil de Bagchi
   [Bag87]: ζ|_D no se anula, está en el soporte S de la medida límite, y la densidad
   inferior de A_ε es positiva para todo ε): densidad positiva ⟹ conjunto no acotado ⟹
   LP-112. Luego LP-112 no es más fuerte que RH.
2. **LP-112 ⇏ RH por ningún diccionario conocido.** La consecuencia de LP-112 bajo ¬RH
   es m = ∞ (Thm. 5.1) — un mundo consistente con todo lo conocido (Bohr–Landau permite
   m = ∞ de densidad cero). El mecanismo que hace RH-equivalente a la recurrencia fuerte
   es exactamente el que LP-112 esquiva: densidad positiva de réplicas contradiría los
   teoremas de densidad N(σ,T) = O(T^θ) (clonación ≫ T vs techo o(T): Doc 109 §4.3,
   ítem 3), de modo que recurrencia fuerte fuerza m = 0; una sucesión de densidad cero
   no contradice nada (Prop. 2.7) y solo fuerza m ∉ (0,∞). Declaración honesta: esto
   muestra que LP-112 no implica RH *por la vía de densidades*; una implicación por vía
   desconocida no puede excluirse — pero la asimetría estructural (LP-112 es invariante
   ante quitar al conjunto bueno cualquier subconjunto de densidad positiva; la
   recurrencia fuerte no) hace implausible el colapso. GAP menor declarado.
3. **LP-112 vs. la versión secuencial de D109 §4.4.** Son el mismo enunciado; este
   documento lo bautiza, fija su forma exacta (con la versión débil LP-112⁻ que basta
   para refutar cada H(m) individualmente) y prueba la reducción con todas las
   constantes. La diferencia con Bagchi queda medida con precisión: Bagchi necesita
   auto-aproximación con densidad positiva (y por eso su negación es detectable por
   promedios y la equivalencia con RH cierra); LP-112 necesita UN representante puntual
   bueno por cota de altura — un enunciado Σ-existencial sobre un conjunto que la
   Prop. 2.6 declara de densidad cero bajo ¬RH.

**El mejor teorema del documento es, pues, el par (Teorema 5.1, Proposición 2.6):** la
reducción completa de la mitad-dicotomía de RH a un lema de casi-periodicidad puntual
secuencial no-RH-equivalente, junto con la demostración de que los testigos de ese lema
son excepcionales en el sentido exacto del cuantificador maestro. Ni más (no probamos
LP-112) ni menos (nada de lo anterior estaba escrito con estas constantes y este
perímetro).

---

## 6. Línea (5): análisis de bloqueo contra P43

### 6.1. ¿Es la misma inversión? Sí — y la asimetría del encargo, resuelta

La pregunta fina del encargo: la media B² es sobre τ ∈ ℝ con densidad positiva de
candidatos; extraer UN τ bueno de un conjunto de medida positiva no es un evento de
medida nula — ¿es esta ruta distinta del muro? Respuesta, con la disección hecha:

- **La premisa de la asimetría es falsa.** El conjunto de medida positiva (casi-períodos
  B², Lema 2.2) no es el conjunto del que hay que extraer. El conjunto relevante — τ
  buenos para Rouché en el disco fijo D(ρ₀, r) — tiene densidad superior CERO bajo H(m)
  (Prop. 2.6). La cadena "densidad positiva de candidatos → uno sirve" se rompe porque
  la candidatura B² no implica (ni correlaciona positivamente con, en el sentido de
  medidas) la bondad en la ventana fija: la seminorma B² asigna peso 0 a la ventana
  (Obs. 2.4). De los dos escenarios que el encargo pedía dirimir — "los buenos tienen
  medida positiva" vs "el conjunto útil es de medida nula aunque los B²-casi-períodos
  tengan densidad positiva" — vale el segundo, y no como sospecha sino como teorema.
- **Por tanto: la misma inversión.** Certificar A_ε ≠ ∅ con dens(A_ε) = 0 es certificar
  un evento individual dentro del conjunto excepcional de la estadística que lo
  gobierna — el Principio 3.1 de P43, literal. La coordenada es nueva (casi-períodos en
  τ, no ceros en γ ni ventanas en T), el muro es el mismo.
- **Pero una instancia estrictamente más débil, y sin el cortocircuito de D104.** Dos
  diferencias demostradas con las instancias anteriores: (i) el enunciado a certificar
  (LP-112) NO es RH-equivalente (§5.4) — a diferencia de la recurrencia fuerte; (ii) la
  ruta no se auto-bloquea (Prop. 2.7) — a diferencia del amplificador de D104, cuya
  meta chocaba con su propio techo. El estado comparado:

| ruta de réplica | requiere | bajo ¬RH ese conjunto es | bloqueo |
|---|---|---|---|
| recurrencia fuerte (Bagchi) | densidad inferior positiva de τ buenos | densidad 0 (Prop. 2.6) | la meta ES RH (equivalencia) |
| amplificador D104 (Forma C) | densidad positiva anclada de réplicas | capada por N(σ,T) = O(T^κ), mismo exponente | auto-bloqueante |
| **LP-112 (secuencial, este doc)** | UN τ por cota de altura (densidad 0 basta) | densidad 0, vacuidad DESCONOCIDA | sin auto-bloqueo; sin alimentador — muro P43 en forma de conjunto excepcional |

La forma del muro aquí es la más desnuda del programa: no falta una estimación (las
estimaciones relevantes están: Lemas 2.1, 2.2, 2.5), no hay colisión interna
(Prop. 2.7) — falta un mecanismo de **selección no-genérica**: algo que produzca un
punto de un conjunto de densidad cero definido por una condición individual. Ningún
método de la lista de P43 (propagación, amplificación, recurrencia, positividad, criba,
momentos) produce puntos excepcionales; todos producen genéricos.

### 6.2. La coordenada clásica del mismo muro: Jessen–Tornehave

Registro de erudición que confirma el diagnóstico desde la teoría clásica de ceros de
funciones casi-periódicas. La maquinaria canónica para "ceros de funciones holomorfas
casi-periódicas en bandas" es la teoría de movimientos medios y funciones de Jensen de
Jessen–Tornehave [JT45], extendida a ζ en la franja por Borchsenius–Jessen [BJ48]: la
función de Jensen φ(σ) = M_t(log|f(σ+it)|) es convexa y sus derivadas laterales miden
la **densidad media relativa** de ceros en cada abscisa. Para ζ con σ > ½, esa densidad
media es 0 (Bohr–Landau). Es decir: la teoría clásica de ceros de funciones a.p. es,
por construcción, una teoría de medias — y una configuración con m finito (densidad
media nula) es **invisible para la función de Jensen**, indistinguible de m = 0. El
aparato clásico entero vive del lado promediado del cuantificador; la dicotomía D-109
pregunta por el lado individual. [Alcance exacto de BJ48 en ½<σ<1: NO VERIFICADO en
detalle; el uso aquí es solo ilustrativo, no load-bearing.]

### 6.3. Saldo del análisis de bloqueo

El gap restante de la implicación m<∞ ⟹ m=0 contiene la inversión promedio→individual
— la misma de P43 — en la instancia precisa "no-vacuidad de un conjunto de densidad
cero de casi-períodos puntuales". Es una instancia estrictamente más débil que las
previamente bloqueadas (no-RH-equivalente, sin auto-bloqueo), lo que extiende el no-go
de P43 con una precisión nueva: **el muro no distingue entre pedir densidad positiva y
pedir un solo punto; distingue entre genérico y excepcional.** La cantidad de testigos
exigida es irrelevante; su excepcionalidad es lo que bloquea. (Esto refina la frase del
Doc 111 §6.4: el muro nunca fue sobre el valor de m — ni sobre el número de testigos —
sino sobre ver UNA unidad individual de cualquier cosa.)

---

## 7. VEREDICTO

**VEREDICTO: IMPLICACIÓN PARCIAL.**

La implicación m < ∞ ⟹ m = 0 no queda probada ni refutada. Queda **reducida, con prueba
completa, a un único lema abierto**, y todas las demás rutas quedan bloqueadas con
localización exacta:

**Lo probado (incondicional):**

1. **Teorema 2.3 / 5.1 (la reducción):** LP-112 (casi-periodicidad puntual secuencial de
   ζ en discos compactos de la franja) ⟹ m ∈ {0,∞}; en particular
   (m<∞) ∧ LP-112 ⟹ RH, y con la identidad del Doc 109: RH ⟸ (diana L8) ∧ LP-112.
   Bajo H(m) todas las constantes del paso de Rouché están congeladas (radio r < δ_min/2,
   margen η > 0, umbral de altura γ_max): no hay degeneración de uniformidad; falta
   exactamente UN τ.
2. **Proposición 2.6 (el muro con signo):** bajo H(m), el conjunto de τ buenos para
   Rouché en el disco del cero tiene densidad superior CERO (Bagchi + Hurwitz +
   Portmanteau). La esperanza "los buenos tienen medida positiva" es falsa: la medida
   positiva (casi-períodos B², Lema 2.2) vive en la coordenada media-en-t, que asigna
   peso nulo a la ventana del cero (Obs. 2.4). El gap B²→puntual no es una estimación
   faltante: es la certificación de no-vacuidad de un conjunto excepcional — el
   cuantificador maestro de P43, instancia secuencial.
3. **Proposición 2.7 (sin auto-bloqueo):** a diferencia de D104, la versión secuencial
   no choca con los teoremas de densidad — necesita densidad cero de réplicas, que nada
   obstruye. La ruta está sin alimentar, no auto-contradicha. LP-112 queda vivo, no
   RH-equivalente (RH ⟹ LP-112 vía Bagchi; LP-112 solo da la dicotomía, no m = 0).
4. **Lemas 3.1–3.3 (el requisito de Euler, satisfecho):** los cosh-ejemplos de D111
   quedan excluidos en el primer escalón (no son B² en rectas; no admiten ninguna
   auto-aproximación: |F(s+iτ)| → ∞); la separación de ζ es aritmética e incondicional —
   serie de Dirichlet (nivel B²), independencia ℚ-lineal de {log p} = factorización
   única (densidad relativa y no-discretitud de los casi-períodos: réplicas en alturas
   nuevas), y producto de Euler aleatorio (soporte de Bagchi). Davenport–Heilbronn
   calibra: sin Euler completo, la alternativa realizada es m = ∞ — el patrón
   m ∈ {0,∞} no tiene contraejemplo conocido en ninguna clase con serie de Dirichlet.
5. **Línea de momentos (§4), BLOQUEADA en dos lugares independientes:** (i) el alimento
   no existe — verificado contra D72 en fuente: B_λ(log p) = ∫W_λ cos(s log p)dm_∞ es
   autónomo (transformada del test, sin ceros — el temor del encargo era infundado),
   pero la serie de primos diverge (Doc 105) y no hay valor aritmético de T_λ;
   (ii) las identidades de la fórmula explícita son tautológicas en los 4m parámetros
   (Prop. 4.2: una sola identidad independiente, satisfecha idénticamente; ξ_on = ξ/P_m
   no tiene fórmula explícita propia); el contenido no-tautológico es el signo = criterio
   de Weil = RH = inercia (P43 §4). Además (Obs. 4.3) el gap espectral
   ε₀ = Σ 2δ_j²K_λ(γ_j) es positivo pero su ínfimo sobre configuraciones es 0: la
   finitud protege a los argumentos internos al mundo (Rouché), no a los evaluadores
   externos (trazas). La Prop. 4.5 del Doc 110 no se aplica: rango finito ≠ rango finito
   a priori — la frontera del Doc 110, confirmada desde el otro lado.

**El gap exacto restante (único):** LP-112⁻ — para el disco fijo D(ρ₀, r) alrededor de
un cero off-crítico hipotético y ε = η/2, exhibir UN τ > γ_max + γ₀ + r + 1 con
sup_D |ζ(s+iτ) − ζ(s)| < ε. Estatus: abierto; no-RH-equivalente por los diccionarios
conocidos; sus testigos forman un conjunto de densidad cero bajo la hipótesis a refutar
(Prop. 2.6), de modo que toda prueba deberá ser un mecanismo de selección no-genérica —
fuera de la lista de formas de argumento de P43.

**Respuesta a la pregunta decisiva del encargo** (¿el bloqueo de D104 aplica cuando solo
se necesita UNA réplica?): **no aplica** (Prop. 2.7) — pero su lugar lo ocupa un bloqueo
más limpio y más profundo: la réplica única es un evento de densidad cero, y el
cuantificador maestro bloquea la certificación de eventos excepcionales con total
independencia de cuántos se necesiten. La cantidad bajó de "densidad positiva" a "uno";
la dificultad no bajó nada. Esa invariancia — el muro es insensible al cardinal de lo
pedido, sensible solo a su excepcionalidad — es el hallazgo estructural del documento, y
extiende el no-go de P43 a la clase de los enunciados de réplica secuencial.

**Para la fase:** el frente queda mejor que antes en un sentido preciso: la mitad
analítica de la arquitectura (D-109) tiene ahora UN lema con nombre, forma exacta,
constantes congeladas, prueba condicional completa, certificado de no-equivalencia con
RH y certificado de no-auto-bloqueo. Es el objetivo intermedio más nítido que el
programa ha producido del lado de la rigidez. Lo que pide — seleccionar un punto
excepcional del flujo de Kronecker donde la observable de Euler se auto-encuentra — es
exactamente la versión secuencial del problema de la órbita individual ω₀ del Doc 102.
Las dos caras del programa (recurrencia del toro, dicotomía de defectos) han convergido
en el mismo punto: no es casualidad; es el muro, visto por su arista más delgada.

---

## Referencias

**Internas (backward-only):** Doc 109 (§4.3–4.6: D-109, identidad arquitectónica, gap
media→puntual, precedente Bagchi; §6.1: recapitulación de D70–72 y D105); Doc 110
(Prop. 4.5, axioma L6, §4.3–4.4); Doc 111 (Prop. 2.2, Cor. 2.3, Obs. 2.4, §2.3–2.5,
§3 anti-Siegel, Prop. 6.2, Obs. 6.3); Doc 108 (Teoremas 3.3, 3.4; Prop. 2.5; §7.4);
Doc 105 (divergencia (5√2/8)log X de la serie de primos; correcciones a D70–72);
Doc 104 (amplificador auto-bloqueante; vía P42 §2 y P43 Thm. C); Doc 102 (Bagchi en el
programa; ω₀ y la observable de Euler); Doc 100 (positividad semilocal); Doc 99
(CCM-ZST); Doc 98 (Hipótesis T1; Cor. 2.4: costo 2δ²K_λ(γ₀)); Doc 95 (Lema 2.2:
decaimiento de dm_∞); Doc 72 (Thm. 4.1: T_λ = A_λ^{off} − Σ_p(log p/√p)B_λ(log p);
§3–5: B_λ como transformada de Fourier del test — **verificado en fuente para este
documento**); P43 (Principio 3.1; §4 valor/inercia; Thm. C); P42; P41; P35 (κ = 2m).

**Literatura (verificable salvo marca):**

- A. S. Besicovitch, *Almost Periodic Functions*, Cambridge Univ. Press, 1932. (Clases
  B^p; casi-periodicidad de Besicovitch; clausura B² de polinomios trigonométricos.)
- H. Bohr, *Zur Theorie der allgemeinen Dirichletschen Reihen*, Math. Ann. 79 (1918),
  136–156; y la serie *Zur Theorie der fast periodischen Funktionen* I–III, Acta Math.
  45–47 (1924–26). (Casi-periodicidad uniforme de series de Dirichlet en semiplanos de
  convergencia absoluta; teoría general.)
- H. Bohr, E. Landau, *Ein Satz über Dirichletsche Reihen mit Anwendung auf die
  ζ-Funktion und die L-Funktionen*, Rend. Circ. Mat. Palermo 37 (1914), 269–272.
  (Densidad cero off-crítica.)
- B. Bagchi, *The statistical behaviour and universality properties of the Riemann
  zeta-function and other allied Dirichlet series*, Tesis, Indian Statistical Institute,
  Calcuta, 1981. [Bag81] (Teorema límite funcional en H(D), incondicional; soporte de la
  medida.)
- B. Bagchi, *Recurrence in topological dynamics and the Riemann hypothesis*, Acta
  Math. Hungar. 50 (1987), 227–240. [Bag87] (Recurrencia fuerte ⟺ RH.)
- A. Laurinčikas, *Limit Theorems for the Riemann Zeta-Function*, Kluwer, Dordrecht,
  1996. [Lau96] (Caps. 5–6: teorema límite en H(D) y soporte
  S = {f sin ceros} ∪ {0}; exposición estándar del aparato de Bagchi.)
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (rev.
  D. R. Heath-Brown), Oxford Univ. Press, 1986. [Tit86] (Thm. 4.11: fórmula aproximada;
  Thm. 7.2 y §7.2: valor medio cuadrático incondicional en σ > ½; Cap. VIII:
  Ω-teoremas, no-acotación de ζ en rectas de la franja.)
- H. L. Montgomery, R. C. Vaughan, *Hilbert's inequality*, J. London Math. Soc. (2) 8
  (1974), 73–82. [MV74] (Valor medio de polinomios de Dirichlet.)
- H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series*, J. London
  Math. Soc. 11 (1936), 181–185 y 307–312. [DH36]
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm.
  Sém. Math. Univ. Lund (1952), 252–265. [Wei52] (Fórmula explícita; criterio de
  positividad ⟺ RH.)
- F. R. Gantmacher, *The Theory of Matrices*, Chelsea, 1959, Vol. 2, Cap. X. [Gan59]
  (Identidades de Newton; formas de Hankel; Jacobi–Frobenius.)
- N. I. Akhiezer, *The Classical Moment Problem*, Oliver & Boyd, 1965. [Akh65]
  (Problema de momentos de Hamburger; el caso finito-atómico es determinado.)
- B. Jessen, H. Tornehave, *Mean motions and zeros of almost periodic functions*, Acta
  Math. 77 (1945), 137–279. [JT45] (Función de Jensen; densidades medias de ceros de
  funciones a.p. holomorfas.)
- V. Borchsenius, B. Jessen, *Mean motions and values of the Riemann zeta function*,
  Acta Math. 80 (1948), 97–166. [BJ48] [Alcance exacto en ½<σ<1: NO VERIFICADO en
  detalle; uso solo ilustrativo en §6.2.]
- D. Platt, T. Trudgian, *The Riemann hypothesis is true up to 3·10¹²*, Bull. London
  Math. Soc. 53 (2021), 792–797. (Vía D111 §2.4(c).)
- H. Weyl, *Über die Gleichverteilung von Zahlen mod. Eins*, Math. Ann. 77 (1916),
  313–352. (Equidistribución; Kronecker–Weyl en el toro.)

*Fin del Documento 112.*
