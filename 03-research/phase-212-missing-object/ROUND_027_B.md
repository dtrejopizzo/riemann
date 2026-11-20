# ROUND_027_B — Cotejo hostil de antecedentes: peso atenuado v_n·cos(ω log n) y clausura por K_T cerrado

Objeto cotejado: a^{(ω)}_T = Arch − Σ v_n cos(ω log n) c_F(log n) sobre P_T, ω = kπ/(4T); hechos (i)–(iii)
del enunciado de la ronda. No se calculó nada. No se editó ningún paper ni el índice.

Abierto en primaria: índice maestro (Parte V 212-25, 212-26-A/B, 212-cotejo-114, 212-cotejo-margen; filas de
W-lin, cor:void, thm:finmod, BARRIER_Y_001, Cesàro, Fejér); R160_M2_R1 (§§2–7 completos en lo pertinente);
P47 main.tex thm:Z (l.1240–1290), lem:degen (l.3294–3310), prop a_θ (l.4805–4860); OBJECT_SPEC O2, O4;
RULES_AVOID B5, W1; ROUND_005_G3 Lema 2; DOSSIER_001 (211) l.50–99; R186_051 §0; BARRIER_Y_001 §§0–2;
phase-62 README. No abierto: memos de fase 153–156 más allá de lo que cita P47; R160_D4_R2 (sin
coincidencias); fases 60–61; 183–185; Lemma T / W-mom sólo por sus filas del índice.

## 1. Antecedentes, uno por uno

**A1. Clausura (ii) = Teorema 5.3(a) y Proposición 6.1 de R160_M2_R1 (fase 160, M2).** §5: (𝒱_T) con las
restricciones π^{T′}_T es un sistema proyectivo de compactos convexos, π^{T′}_T(𝒱_{T′}) ⊂ 𝒱_T (PROVED).
Prop 6.1: si existe una selección v*_T ∈ 𝒱_T con v*_{T,n} → 2a*_n/√n coordenada a coordenada, entonces
λ^A_T(a*) ≥ 0 ∀T; la prueba es exactamente «𝒱_T cerrado + π^{T′}_T(v*_{T′}) → v_T(a*)». Con a* = Λ la
hipótesis (iii) de esa proposición es trivial y queda sólo la (i)+(ii): existencia de la selección. El memo
concluye: «relocates the sign … without weakening it». Ídem índice 212-25 (ROUND_025_A/B): límite inverso de
los compactos K_T = 𝒱_T, Tychonoff. **Se aplica íntegramente: (ii) es REPETICIÓN.** Lo único distinto es que
aquí la selección es explícita (w^{(ω_T)}), no tomada de un optimizador.

**A2. Fórmula (iii) = P47 lem:degen + R160_M2_R1 Lema 3.1 (Danskin–Kato) y Cor 3.3.** lem:degen (PROVED):
μ_T(w) ≤ λ_A − Σ (w_n − v_n) c_{F⋆}(log n), μ_T cóncava. Con w = w^{(ω)}:
μ_T(w^{(ω)}) ≤ λ_A + Σ v_n(1 − cos(ω log n)) c_{F⋆}(log n) = λ_A + (ω²/2)Q(F⋆) + O(ω⁴).
Lema 3.1 da la derivada direccional exacta V′(v; d) = −max_{F∈M_T(v)} ⟨d, κ_T(F)⟩ (PROVED, con fórmula de
segundo orden con hueco espectral g). Respuesta a (c): P47 no da dλ/dT, pero **la derivada respecto del
peso existe y está demostrada** (R160 Lema 3.1; P47 lem:degen como cota de un lado); Q es el caso
d = −(v_n(log n)²/2)ω². Nota: el índice (l.30802) registra para fase 153 una «fórmula de tasa dλ/dT
PROVED» y Hellmann–Feynman en un parámetro b (l.19087); no se cotejó con la afirmación de la ronda.
**REPETICIÓN** (como fórmula); la observación numérica Q(F⋆) > 0 sí es dato nuevo.

**A3. Peso óptimo ≈ v atenuado: índice 212-26-A (ROUND_026_A).** Con w ≥ 0 el óptimo de max_w λ_min(a^w_T)
es estable y «se parece a v atenuado» (w_n/v_n ≈ 0.87 … 0.22 en n = 2 … 11, T = 1.6), margen ≈ 0.08e^{−1.4T},
exponencial simple. El hallazgo actual es una versión explícita de esa observación: mismo orden de margen,
misma caída simple. **PARCIALMENTE EN CORPUS** (observación numérica previa, sin familia explícita ni ω²).

**A4. Modulación en el lado dual: P47 thm:Z (i).** f_w(τ) contiene −Σ v_n w(log n) cos(τ log n): es la
fórmula explícita evaluada en el test modulado w(u)cos(τu). El mecanismo algebraico de (i) (cos(ω log n)c_F =
Re c_{Fe^{iωt}}, desplazamiento del parámetro espectral, «familia ζ(s+iω)») es el mismo; allí se usa en un
certificado lineal (flat-top, w = 1 en la ventana) y su lectura se hace por el lado de ceros [H], que aquí no
cuenta. «One-sided smoothing» es esa lectura; no es un peso atenuado en la forma primal. **El hecho (i) está en
corpus; su uso como peso primal no.** DOSSIER_001 (211) l.50–54 y R186_051: C_T(ω) ∝ Σ v_n cos(ω log n) como
funcional lineal (coherencia/símbolo en la frecuencia ω), no como multiplicador del peso. ROUND_005_G3 Lema 2:
tests F_ω = g cos(ωt) a ω → ∞ para mostrar indefinición de Π_T; otro régimen (ω grande), no aplica.

**A5. a_θ (P47 l.4805–4860).** Baja un solo peso (n = 2) y prueba λ_A(T; a_θ) > 0 ∀θ ∈ [0,1] en T = ½log3
mientras λ^W falla; observación «clases cerradas bajo bajar pesos». Antecedente de «bajar el peine ayuda»,
en una ventana fija y un átomo. No cubre la familia ni la clausura.

**A6. Fejér / Cesàro.** Fases 60–62: promedio Cesàro en λ del Jacobi intrínseco (otro objeto); fracasa por
crecimiento secular λ^{2β−1} del promedio. No se aplica: aquí no se promedia en ninguna variable espectral, se
multiplica el peso. Filas Fejér (phase-102/103/104, L2_019, testigo Fejér de Theorem K, 212-24-C ítem 150):
transferencias de positividad o testigos de soporte; ninguna es un peso atenuado del peine en a_T. No aplican.

## 2. NO-GO de clase: ¿cubren el hallazgo?

- **«Afín en el peso» (OBJECT_SPEC O2; RULES_AVOID J2, W1, W3).** Esas cláusulas descalifican *identidades*
  (G) cuyo término cuadrado es afín/cuadrático en el peso, porque valen para todo peso y no ven el signo. El
  hallazgo no es una identidad: es la sustitución de la meta por otra desigualdad (positividad de a^{w^{(ω)}})
  más una clausura topológica. La afinidad en el peso sólo dice que K_T es convexo y que (iii) es lineal en el
  desplazamiento del peso; **no lo descalifica por sí sola**. Lo que sí hereda de W1: el conjunto de c con
  c·w^{(ω)} ∈ K_T es un intervalo con margen; nada obliga a usar c = 1 con exactitud a T fijo.
- **Cambio de operador de referencia (212-cotejo-114, D.186).** Es una congruencia exacta válida para todo
  peso; el atenuado no es una congruencia sino otro peso. **No aplica.**
- **W-lin / cor:shape.** Cierra certificados lineales en base fija. No aplica a la reducción; **aplica a cualquier
  intento de probar a^{(ω_T)}_T ≥ 0 por certificado lineal**.
- **cor:void, thm:finmod, B5.** No aplican a la reducción (ii), que es correcta para cualquier peso. **Aplican a la
  prueba que falta**: si a^{(ω_T)}_T ≥ 0 ∀T se demostrara con hipótesis cerradas por borrado finito, reescalado
  cΛ o a_P, la clausura (ii) daría la meta para esos falsificadores, lo cual es falso. Por tanto el enunciado
  atenuado ∀T está sometido a O4 completa: debe fallar para cΛ (c ≠ 1), a_P, Λ1_{n≥N} a T grande, con un
  margen que en esas familias se haga negativo. Que en T ≤ 2 el margen sea ≍ ω²e^{−cT} no dice nada aquí: los
  falsificadores también son positivos a T chico.
- **BARRIER_Y_001.** Farkas sobre la clase {0,1} de borrados de la capa superior; recomienda no reintentar
  signos de primer orden de c_{F⋆} con movimientos de clase. (iii) es un signo de primer orden de c_{F⋆}
  (Q(F⋆) > 0) bajo un movimiento que baja la capa superior: **aplica a (iii) como herramienta de signo**; no a
  la reducción.
- **Lemma T, W-mom (sólo por las filas):** costo de cola lineal en ℓ¹; margen ≤ k(1−β_max) en momentos del haz.
  No se ve aplicación directa; no verificado en primaria.
- **Teorema M / cota doble exponencial (212-cotejo-margen).** Compatible: el atenuado vive a distancia
  ≍ e^{T} (en ℓ¹, Σ v_n(1−cos) con k = 1) de v, que está a distancia doblemente exponencial del borde de K_T.
  El atenuado no es una perturbación de v; es otro punto interior. La ganancia observable (∝ ω²) es la
  derivada de A2, no información sobre la cola que lleva el signo.

## 3. Observación hostil sobre la lógica

La meta pide v ∈ K_T ∀T. El hallazgo pide w^{(ω_T)}_T ∈ K_T ∀T. Esto implica la meta (A1) pero no es
implicado por ella (K_T no es cerrado bajo bajar pesos de forma no uniforme; A5 sólo lo ve en un átomo).
Es una **condición suficiente, posiblemente más fuerte en la cola**, de la misma forma («Arch − peine ≥ 0» en
P_T) con otro peso. El margen no diminuto en T ≤ 2 es NUMÉRICO y es exactamente lo que R160 H1 y 212-26-A
ya esperaban del problema con peso libre. Qué convierte el margen en prueba ∀T: no hay mecanismo propuesto.
La atenuación con cos anula el peso en el borde de la ventana (k = 1: ω·2T = π/2), es decir quita los
contactos superiores que producen la pequeñez doble exponencial (R160 H1, «tests that resolve the top
contacts»): es plausible que el margen venga de eso, y entonces el problema queda en controlar la cola, que
es el mismo resto.

## 4. Veredicto

**PARCIALMENTE EN CORPUS** (reducción y fórmula: repetición; familia explícita y números: nuevos).

Repetición: (ii) clausura por K_T cerrado y torre (R160_M2_R1 Thm 5.3(a), Prop 6.1; 212-25); (iii) derivada
respecto del peso (P47 lem:degen; R160 Lema 3.1, Cor 3.3); (i) modulación cos(τ log n) = test modulado (P47
thm:Z(i)); «peso óptimo ≈ v atenuado» (212-26-A).

Nuevo respecto del corpus (sin prioridad fuera de él):
1. La selección explícita w^{(ω)}_n = v_n cos(ω log n), ω = kπ/(4T), como candidata de Prop 6.1 con a* = Λ
   (en R160 la selección era abstracta en 𝒪^prim_T).
2. NUMÉRICO: margen positivo ∝ k² con caída exponencial simple hasta T = 2; la atenuación lineal
   v_n(1 − log n/2T) da negativos (no figura en corpus).
3. La lectura de (i) en el lado primal: polos desplazados a ½ ± iω más corrección arquimediana
   ∫[m(τ) − ½m(τ−ω) − ½m(τ+ω)]|F̂|² (ARGUED: es elemental; no cotejado contra P47 eq:m término a término).
   Esta corrección es ≍ −½ω²m″ y podría ser la fuente del término ω²; no comprobado.

Lo que falta para que no sea traslado del signo: una razón por la que a^{(ω_T)}_T ≥ 0 ∀T y que falle para
cΛ (c ≠ 1), a_P y Λ1_{n≥N} (O4). Prueba barata recomendada antes de cualquier derivación (cómputo chico, no
hecho): el mismo margen atenuado para (1 ± 0.05)v y para v con borrado de un primo de la capa superior en
T = 1.2–2.0; si el margen se comporta igual, el hallazgo es pérdida de margen (W1), no mecanismo.
