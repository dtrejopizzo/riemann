# Documento 196 — GAP-192.B: ¿los ceros off de Davenport–Heilbronn alcanzan la escala polilog?

**Programa:** Hipótesis de Riemann — Fase 59 (cierre total)
**Fecha:** 2026-06-12
**Mandato:** decidir el [GAP-192.B] (D192 §5): ¿existe sucesión de ceros off de la función de Davenport–Heilbronn con b_j·log γ_j → 0 (o b_j ≤ (log γ_j)^{−1−η})? Si SÍ, la repulsión polilog es propiedad-Euler y la [CONJ 179.6-fuerte] está bien apuntada; si NO, el mecanismo-Euler está mal apuntado. Dos vías: (1) CLT/cruce de niveles en la línea (principal); (2) universalidad efectiva (backup). Honestidad total; sin numérica; citas backward-only.
**Prerrequisitos:** D192 (GAP-192.B, test 192.2, E-192.1); D179 (Conj 179.6-fuerte/∞); **D150 (Prop 150.2 — DECLARACIÓN: D150 NO está auditado por tercero, deuda E-194.6 de D194 §5.3; riesgo calificado BAJO, input libro de texto; todo uso aquí queda marcado)**.

---

## 0. Convenciones y el objeto exacto

**La función de D–H** ([DH36]; forma estándar, Def. 146.2 / D150 §4.3):
$$f(s)\;=\;\frac{\sec\theta}{2}\Bigl(e^{-i\theta}L(s,\chi)+e^{i\theta}L(s,\bar\chi)\Bigr),\qquad \tan\theta=\kappa:=\frac{\sqrt{10-2\sqrt5}\,-2}{\sqrt5-1},$$
con χ el carácter primitivo complejo mod 5 con χ(2)=i. Escribo L₁:=L(s,χ), L₂:=L(s,χ̄).

**[Verificación 196.0 — corrección al encargo].** χ(−1)=χ(4)=χ(2)²=i²=−1: el carácter es **IMPAR** (a=1), la completación es Λ_j(s)=(5/π)^{(s+1)/2}Γ((s+1)/2)L_j(s), no Γ(s/2). El encargo decía "χ par, Γ(s/2)" con orden de verificar: verificado y corregido. La elección de θ ([DH36]; exposición en [Tit86 §10.25], [BG11]) hace que los coeficientes de f sean reales (a_n = secθ·Re(e^{−iθ}χ(n))) y que Λ_f(s):=(5/π)^{(s+1)/2}Γ((s+1)/2)f(s) satisfaga **Λ_f(s)=Λ_f(1−s)** — ecuación funcional riemanniana, SIN producto de Euler (f no es multiplicativa: a₆=a₂a₃ falla). Hechos heredados: infinitos ceros con β>1 [DH36] ("gordos"); liminf b=0 sobre los off [Prop 150.2, **no auditada**, E-194.6]. b:=β−½. **Escala polilog**: b ≤ (log γ)^{−1−η}, η>0.

---

## 1. Vía 1 (principal): estructura en la línea y el mecanismo de Lehmer invertido

### 1.1. [LEMA 196.1] (fases ancladas: las Z-funciones existen para χ complejo)

*Para j=1,2 y t real: Λ_j(½+it) = ε_j·conj(Λ_j(½+it)), con ε_j=ε(χ_j) la constante raíz (|ε_j|=1). En consecuencia Z_j(t):=ε_j^{−1/2}Λ_j(½+it) es REAL para todo t, y Λ_f(½+it) es real.*

*Demostración.* La serie y el factor gamma dan Λ(s,χ̄)=conj(Λ(s̄,χ)) (coeficientes conjugados, gamma real en ℝ). La ecuación funcional Λ(s,χ)=ε(χ)Λ(1−s,χ̄) en s=½+it: Λ(1−s,χ̄)=Λ(½−it,χ̄)=conj(Λ(½+it,χ)). Sustituyendo, Λ₁(½+it)=ε₁·conj(Λ₁(½+it)); escribiendo Λ₁=Re^{iφ}: e^{2iφ}=ε₁, i.e. φ=½arg ε₁ mod π. Igual para j=2. La realidad de Λ_f(½+it) es la de Λ_f(s)=Λ_f(1−s) más coeficientes reales (Λ_f(½−it)=conj Λ_f(½+it)). ∎

**Consecuencia estructural (corrección al diseño del encargo).** El encargo proponía analizar arg g(½+it), g:=L₁/L₂, como proceso gaussiano vía "arg g = 2 Im log L + fase determinista". El Lema 196.1 muestra que el **valor** de arg Λ_j en la línea está anclado mod π (lo que fluctúa à la Selberg es la rama continua, i.e. el winding/conteo de ceros, no la dirección del valor): g(½+it) = (ε₁/ε₂)^{1/2}·Z₁(t)/Z₂(t) vive en una **recta fija** por el origen. La ecuación de ceros de f en/cerca de la línea no es un cruce de fase 2D sino **UNA ecuación real**: con w₀:=−e^{2iθ}, f=ce^{−iθ}(L₁−w₀L₂) y, en la línea,
$$\Lambda_f(\tfrac12+it)\;=\;c'\,\bigl(Z_1(t)-r_0\,Z_2(t)\bigr)\;=:\;c'\,H(t),\qquad r_0\in\mathbb R,\ H\ \text{real},$$
donde r₀∈ℝ es forzado por la realidad de Λ_f (la elección de θ de [DH36] es exactamente la rotación que alinea las dos rectas ancladas). Ceros de f EN la línea = cambios de signo de H; **casi-ceros** = mínimos locales positivos de |H|.

### 1.2. [LEMA 196.2] (conversión Rouché: mínimo positivo ⟹ par off, con b<r — PROBADO)

*Sea t₀ real, 0<r≤1/10. Supóngase: (i) Λ_f tiene exactamente 2 ceros (con multiplicidad) en el disco D:=D(½+it₀,r); (ii) Λ_f(½+it)≠0 para |t−t₀|≤r. Entonces los dos ceros forman un par off simétrico ρ=½+b+iγ, 1−ρ̄=½−b+iγ con 0<b<r y |γ−t₀|<r.*

*Demostración.* La involución σ(s):=1−s̄ fija D (centro en la línea, σ es isometría) y permuta los ceros de Λ_f (Λ_f(1−s̄)=conj Λ_f(s) por EF + coeficientes reales). Ningún cero está en el segmento crítico de D por (ii); un cero fijo por σ estaría en la línea — excluido. Luego σ empareja: con exactamente 2 ceros, o bien son un par σ-simétrico {ρ, 1−ρ̄} (misma ordenada γ, abscisas ½±b, 0<b<r ✓), o bien cada uno generaría su pareja distinta, dando ≥4 ceros en D — contradicción con (i). ∎

**Lectura cuantitativa (Lehmer invertido).** Un par de Lehmer es un casi-doble de H que SÍ cruza (dos ceros en línea pegados); el enemigo aquí es el mismo casi-doble cuando NO cruza: mínimo local |H(t₀)|=δ>0 con curvatura A≍|H''| ⟹ el modelo local H≈A((t−t₀)²+δ/A) continúa analíticamente a un par off con **b≈√(δ/A)**. Con A ≍ (log t)²·(amplitud local) — la derivada logarítmica típica es ≍ log t, dos veces — penetrar b ≤ (log γ)^{−1−η} pide solo **profundidad relativa δ/amplitud ≲ (log γ)^{−2η}**: un requisito *polinomialmente débil* en 1/log. El Lema 196.2 hace riguroso el paso casi-cruce→cero-off-genuino que el encargo pedía formalizar: la hipótesis (ii) garantiza off; la (i) da b<r sin cálculo de derivadas.

### 1.3. La cuenta CLT — qué es teorema y qué no

**Insumos incondicionales disponibles:** (a) CLT de Selberg para Dirichlet L: log L(½+it,χ_j)/√(½loglog t) → gaussiana compleja estándar, INCONDICIONAL ([S46] para ζ; método extendido a L de Dirichlet — versiones cuantitativas en [Tsa84], [RS17]); versión **conjunta** para caracteres no equivalentes (χ≁χ̄): asintóticamente independientes, motor de [BH95] — luego log|Z₁/Z₂|(½+it) ≈ gaussiana real de varianza ~loglog t, y la condición de nivel |Z₁/Z₂|≈|r₀| se realiza con densidad ≍(loglog T)^{−1/2} — proporción casi-positiva de t. (b) Segundos momentos de L y L' en la línea (incondicionales, clásicos). (c) Conteo total N_f(T) ~ (T/2π)log(T·√5/2πe)·2 — Riemann–von Mangoldt para f (EF + serie de Dirichlet, sin Euler, estándar); ceros EN la línea: ≫ T·(log T)^{1/2}e^{−c√{loglog T}} ([Kar90-91]; cómputos a altura baja en [BS07]) — cota inferior, sin cota superior on-line.

**La cuenta heurística (etiquetada como tal, NO teorema).** Casi-cruces: H tiene ≍ log T puntos críticos por unidad de t; condicional a estar en la ventana de nivel (densidad (loglog)^{−1/2}), un mínimo local de |H| tiene profundidad relativa ≤ ε con probabilidad ≍ ε (densidad de valores acotada — aquí entra el CLT con tasa [Tsa84/RS17]); la mitad (no-cruce) produce, vía Lema 196.2, pares off con b ≍ √ε/log. Con ε=(log T)^{−2η}: **≍ T·log T·(log T)^{−2η}(loglog T)^{−1/2} pares off con b ≤ (log γ)^{−1−η} en [T,2T] — la cuenta CIERRA con abundancia**, consistente con [BH95] (casi todos los ceros de combinaciones lineales de productos de Euler pegados a la línea, bajo RH-para-las-L_j + hipótesis de espaciamiento; enunciado citado al nivel de su abstract — verificación a nivel de página pendiente, [GAP de literatura menor]) y con la distribución fina de [BG11].

**Dónde muere el rigor incondicional — identificación exacta.** Todo lo anterior es riguroso SALVO un único punto: garantizar, para infinitos t₀→∞, las hipótesis (i)+(ii) del Lema 196.2 con r=r(t₀)≤(log t₀)^{−1−η}. Eso exige un **casi-doble por debajo del espaciamiento medio** (dos ceros de Λ_f en un disco de radio (log)^{−1−η} ≪ 1/log) con evitación del segmento crítico. Los CLT/momentos dan distribuciones de VALORES; convertirlos en una configuración geométrica puntual garantizada es exactamente el problema de gaps pequeños — cuya maquinaria conocida (Montgomery, Conrey–Ghosh–Gonek) es condicional a RH y diseñada para ζ. **No fabrico el enunciado: queda como GAP nombrado.**

**[GAP-196.A — el insumo mínimo exacto].** *Para algún η>0 e infinitos t₀: Λ_f tiene exactamente 2 ceros en D(½+it₀,(log t₀)^{−1−η}) y ninguno en el segmento crítico del disco.* Estatus: abierto; estadísticamente "casi seguro" por la cuenta CLT; **estrictamente más débil que la universalidad efectiva** (que daría el control de valores en todo el disco, sobredeterminando la configuración) y de naturaleza segundo-momento, no universalidad.

**[REDUCCIÓN 196.3 — lo probado de la vía 1].** *GAP-196.A ⟹ existe sucesión de ceros off de f con b_j ≤ (log γ_j)^{−1−η}, en particular b_j·log γ_j → 0.* *Prueba: Lema 196.2 aplicado a cada t₀; los pares obtenidos en discos disjuntos son distintos y b_j<r(t₀_j)→0 con b_j log γ_j ≤ (log γ_j)^{−η}.* ∎

## 2. Vía 2 (backup): universalidad efectiva — NO penetra la escala

La Prop 150.2 [**D150, no auditado, E-194.6**] da, para cada ε>0 FIJO, ≫_ε T ceros con b≍ε; penetrar polilog exige el régimen ε=ε(T)→0. Las efectivizaciones conocidas de Voronin ([Gar03]; tasas de discrepancia de [LLR17-19] para la distribución de valores de ζ/L) tienen calidad: para aproximación ε, la primera τ admisible y la densidad inferior dependen de ε de forma **al menos exponencial** (cotas tipo densidad ≥ exp(−c/ε^{B}) o peores; [GAP de literatura: los exponentes exactos de [Gar03] y el alcance de [LLR] a L de Dirichlet conjuntas no verificados a nivel de página esta sesión — la conclusión solo usa que NINGUNA tasa publicada es polinomial en ε]). Invirtiendo: a altura T la mejor ε(T) alcanzable es a lo sumo ≍(loglog T)^{−c}, luego b·log γ ≍ log T·(loglog T)^{−c} → ∞. **La vía 2 muere a distancia (loglog)^{−c} de la línea: dos escalas enteras por encima del objetivo.** Confirma el diagnóstico de D192: GAP-192.B *tal como fue formulado* (vía universalidad efectiva) no es decidible con la tecnología de esa área; la vía 1 lo **reformula** en teoría de valores en la línea, donde el déficit es un solo enunciado de configuración (GAP-196.A), no una tasa exponencialmente lejana.

## 3. Test anti-circularidad

| Objeto | ¿RH-libre? | ¿ζ-libre? | Dónde entra la aritmética |
|---|---|---|---|
| Verificación 196.0 (χ impar) | sí | sí (carácter mod 5) | tabla de caracteres |
| Lema 196.1 (fases ancladas) | sí | sí | solo EF + reflexión de Schwarz |
| Lema 196.2 (Rouché simétrico) | sí | sí | ninguna: análisis complejo puro |
| Reducción 196.3 | sí | sí | condicional a GAP-196.A |
| Cuenta CLT §1.3 | sí (CLT incondicional) | sí | heurística en el paso valores→configuración |
| Vía 2 §2 | sí | sí | usa D150 **no auditado** (declarado) |

Nada usa RH ni GRH; [BH95] se cita solo como corroboración condicional, no como insumo de ningún enunciado etiquetado. Sin numérica.

## 4. Veredicto

**GAP-192.B: NO DECIDIDO incondicionalmente, pero REDUCIDO con teorema de conversión probado y respuesta condicional/heurística unívoca: SÍ, D–H penetra la escala polilog.**

1. **[Lo probado]:** [LEMA 196.1] (anclaje de fases — corrige el diseño del encargo: el proceso relevante no es arg g sino el par real (Z₁,Z₂)); [LEMA 196.2] (mínimo local positivo + casi-doble ⟹ par off genuino con b<r, vía simetría σ + Rouché/conteo); [REDUCCIÓN 196.3]: GAP-196.A ⟹ b_j log γ_j → 0 en D–H.
2. **[El déficit exacto]:** GAP-196.A — casi-dobles de Λ_f bajo el espaciamiento medio con evitación de línea. Estadísticamente abundante (cuenta CLT §1.3: ≍T(log T)^{1−2η} configuraciones esperadas); rigurosamente abierto — es un problema de gaps pequeños sin RH, no de universalidad. **Mejora neta sobre D192**: el test ya no cuelga de la universalidad efectiva (vía 2, muerta a (loglog)^{−c}: §2) sino de un enunciado segundo-momento con literatura activa.
3. **[Impacto sobre 179.6]:** la respuesta condicional es la favorable al mecanismo-Euler: D–H (sin Euler) viola la repulsión polilog en cuanto GAP-196.A se confirme — la 179.6-fuerte quedaría **bien apuntada** (la repulsión polilog sería genuinamente propiedad-Euler, no de la ecuación funcional). Mientras GAP-196.A esté abierto, el veredicto del test 192.2 sube de "abierto a escala polilog" a "abierto pero con mecanismo completo y un solo insumo faltante, con predicción unívoca". Ninguna evidencia apareció en la dirección (c) (demolición): al contrario, ningún término de la cuenta protege la escala polilog en ausencia de Euler.
4. **[Nota publicable potencial]:** "Off-line zeros of the Davenport–Heilbronn function at polylogarithmic distance" es viable como resultado condicional (a GAP-196.A o a las hipótesis de [BH95]) con el Lema 196.2 como pieza nueva; NO como teorema incondicional hoy.
5. **[Deudas]:** D150/Prop 150.2 usada y declarada no auditada (E-194.6, riesgo bajo); páginas exactas de [BH95], [Kar90-91], [Gar03], [LLR] pendientes de verificación a nivel de página ([GAP de literatura menor, no portante: ningún enunciado etiquetado depende de ellas]).

**GAPs numerados:** **[GAP-196.A]** (portante): casi-dobles sub-espaciamiento de Λ_f con evitación de línea — decide GAP-192.B vía 196.3. **[GAP-196.B]** (menor): densidad de ceros de f, N_f(σ>½+(log T)^{−1−η},T)=o(T log T) incondicional — daría "casi todos los ceros a distancia polilog" pero no la existencia de off (sin cota superior on-line, §1.3(c)); registrado como vía muerta parcial.

**Sucesor:** atacar GAP-196.A con segundos momentos de H y H' en intervalos cortos (método de Heath-Brown/CGG de momentos discretos adaptado a H=Z₁−r₀Z₂, donde la independencia-CLT de Z₁,Z₂ es ventaja, no obstáculo); si cae, auditar D150 antes de escalar a publicación (mandato E-194.6).

---

### Referencias

**Internas (backward-only):** D146 (Def. 146.2); D150 (§4.3 Prop 150.2 — **no auditado**, deuda E-194.6); D179 (Conj 179.6, Def. 179.1); D192 (test 192.2, GAP-192.B, E-192.1); D194 (§5.3, E-194.6).

**Literatura:** H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series* I, II, J. London Math. Soc. 11 (1936), 181–185, 307–312. — A. Selberg, *Contributions to the theory of the Riemann zeta-function* (1946), Coll. Works I. — K.-M. Tsang, *The distribution of values of the Riemann zeta-function*, tesis, Princeton, 1984. — M. Radziwiłł, K. Soundararajan, *Selberg's central limit theorem for log|ζ(1/2+it)|*, Enseign. Math. 63 (2017). — E. Bombieri, D. Hejhal, *On the distribution of zeros of linear combinations of Euler products*, Duke Math. J. 80 (1995), 821–862. — E. Bombieri, A. Ghosh, *Around the Davenport–Heilbronn function*, Russian Math. Surveys 66 (2011). — A. A. Karatsuba, sobre ceros de la función de D–H en la línea crítica, Izv. Akad. Nauk SSSR (1990–91). — R. Garunkštis, *The effective universality theorem for the Riemann zeta function*, Proc. "Probability in Number Theory" (2003). — Y. Lamzouri, S. Lester, M. Radziwiłł, *Discrepancy bounds for the distribution of the Riemann zeta-function* (y trabajos sobre universalidad efectiva, ~2017–2019). — E. P. Balanzario, J. Sánchez-Ortiz, *Zeros of the Davenport–Heilbronn counterexample*, Math. Comp. 76 (2007), 2045–2049. — E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed., Oxford 1986, §10.25. — S. M. Voronin (1975), universalidad (vía D150).
