# Fase 212 — Lo que no se hace

Consolidado del índice de rutas (hoy incorporado íntegro en la Parte IV de `05-meta-and-planning/ROUTES-MASTER-INDEX.md`; citado «IDX»), el grid
maestro («GRID»), el crucigrama («CW»), los Papers 47–48 («P47», «P48»), la memoria de selecciones
rechazadas de las reglas del proyecto y la fase 211 («211/…»). Es una guía de lectura rápida, no sustituye a las
fuentes: antes de proponer algo se busca en ellas y en los anexos de lectura completa (§H), que
son la lista entera; las secciones A–G son el resumen. Una clausura se cita con su etiqueta
(PROVED / ARGUED); una reformulación exacta es un objetivo válido, no una clausura
(IDX `AUDIT_PHASE193_CERTAINTY.md`).

## A. Reglas duras

A1. **Sandbox.** (★) es el signo de una forma cuadrática explícita. No se nombra ni se usa ninguna
    equivalencia con otro enunciado; no se reduce a ceros; no se argumenta «esto es tan difícil como…».
A2. **Nada del índice se reintenta**, ni renombrado ni como variante, sin una razón escrita de qué
    hipótesis, objeto o clase de métodos cambia y por qué eso evita el motivo registrado del fracaso.
A3. **Filtro de cuatro puntos antes de construir**, verificado por un revisor independiente
    (README §4). Sin los cuatro puntos no hay derivaciones, cómputos ni certificados.
A4. **No cuenta como novedad:** otro nombre, otra notación, otro parámetro, otra base, otro cambio de
    variable (Mellin, theta, potencias, hiperbólico), otra normalización, otra dimensión, «hacerlo
    global / no lineal» sin operación explícita, otra energía auxiliar sin mecanismo de signo,
    reproducir un resultado externo, subir un orden finito más.
A5. **Batería de falsificadores obligatoria** en todo paso de signo (§E). Si el argumento sobrevive a
    alguno, está mal; se dice dónde.
A6. **No se toca ningún paper.** No se abre otra fase. Sin autores, fechas, nombres de modelos ni
    roles de proceso en los archivos.
A7. **No se propone un «cierre honesto»** ni un capítulo de barreras como final: las barreras son
    herramientas.

## B. Diez patrones de fracaso (si la candidata cae en uno, se detiene antes de derivar)

B1. **Identidad válida para todo peine.** No lleva signo (P47 lem:shape-ident, thm:shape (B″)).
    Ejemplos: IDX README EI_001–003; identidades tipo Selberg NODE_001 Prop N.2; gauge de divisores
    P47 thm:spec-gauge; identidades de la franja P47 §strip.
B2. **Estimación con holgura.** Para T ≥ 1 el margen es ≤ 4·10⁹Te^{−15.449T} (y, CONDITIONAL en P47
    thm:ext-half y una cota citada, λ_A ≤ 3.2·10²³N^{33/2}e^{−2πN}, N = e^{2T}; 211/ROUND_009_A Cor 7.1).
    P47 thm:shape(B′)/lem:shape-est prueba restricciones de precisión para decidir el signo en una
    ventana fija; la exclusión general de estimaciones con resto está etiquetada ARGUED, no PROVED.
    Las exclusiones de BARRIER_EST_001 conservan sus hipótesis de clase. Incluye las limitaciones
    registradas para cotas en valor absoluto de ψ(y) − y, gran criba y media cuadrática
    (P47 rem:wit-cheb). No se aplica a bloques fijos ya firmados con certificado.
    **Alcance:** B2 no excluye por sí sola la vía de P47 thm:wit-Tc(iv): una cota inferior uniforme
    λ_A(T_k) ≥ −ε_k, con T_k → ∞ y ε_k → 0, basta aunque ε_k supere el margen esperado.
    Encontrar esa cota sigue OPEN. También basta un error que desaparezca para cada test fijo de
    un núcleo de forma denso, por congelación (ROUND_022_B, Lema 1); no es necesario uniformarlo
    sobre todos los tests para ese argumento punto a punto. Controlar sólo tests seleccionados
    no basta. Estas son reducciones ya registradas, no mecanismos nuevos ni pruebas de signo.
B3. **Reformulación exacta presentada como avance.** Es objetivo válido, no resultado de signo. Hay 43
    reformulaciones distintas registradas (IDX README, fase 204); no se agrega la 44 sin mecanismo.
B4. **Modelo positivo + transferencia o comparación.** Excluido con prueba, cada uno en su clase:
    mezclas positivas y convoluciones con medida positiva finita del modelo hiperbólico
    (211/HYPERBOLIC §7); orden matricial del flujo de escala (§9); prefactores fijos, escalares o
    vectoriales, con o sin primera derivada (§§10–12.4); representación exacta por productos de cosh
    (§§11, 13; no decide si multiplicar por cosh conserva la positividad); comparación K_Φ ≥ εK_{2π}
    para todo ε > 0; comparadores aditivos Robin, asinh y 2π, también sobre primitivos; todo
    comparador aditivo D con D = o(1/u) y K_D semidefinido positivo es nulo; generadores normalizados
    o con gauge, para todo c y todo a; reparación diagonal real de la comparación BPY G1→G2 (cualquier
    factor diagonal real, no sólo holomorfo); dos transportes desde C_0 (multiplicador puntual,
    traslaciones imaginarias) y el cociente A/C_0; positividad importada de una construcción uniforme
    en el peine (P47 thm:noimport; IDX CPOS_CLASS_001).
    **No excluido:** transferencias no diagonales o triangulares (detenidas en selección por falta de
    coeficientes explícitos, no por imposibilidad); la interpolación geométrica con una cota relativa
    ∂_sK_{s,U} ≥ −C_U(s)K_{s,U}, C_U integrable, para cada lista finita U; otros modelos y
    compensaciones conjuntas; construcciones que usan la multiplicatividad exacta de Λ.
B5. **Clase cerrada por modificación finita, borrado o reescalado.** cor:void, a_P, cΛ, W-tail:
    cribas, progresiones, conos sobre log ζ, integralidad coeficiente a coeficiente, propiedades
    sparse-estables (P47 prop:spec (2)–(4)).
B6. **Vale para un modelo con ecuación funcional y sin producto de Euler** (Davenport–Heilbronn,
    Epstein x²+5y², f_t) **o con producto de Euler y sin ecuación funcional** (a_P).
B7. **Sólo monoide; ciego a Beurling** (IDX fase 193 frentes G1, H; INV_K).
B8. **Funcional acotado de los pesos, criterio local en el símbolo, patrón de observables, ley en un
    rango acotado de ventanas, determinante o momento del haz** (W-lin, W-det, W-fam, W-pat, W-loc,
    W-mom; P47 §barriers).
B9. **El signo queda en un funcional del minimizador** (IDX SPEC_A, BARRIER_W; P48 req:spec R10).
B10. **Dirección equivocada o sólo cotas superiores** (W4). La concavidad en el peine (Danskin) da
     sólo cotas superiores. Su representación dual Θ_T = max_c λ_A(T;cΛ) está PROVED
     (211/ROUND_002_D Thm 1) y sólo separa en ventanas de tangencia, donde Θ_T = λ_A
     (ROUND_002_E Cor 4): estado PIVOT, no terreno abierto.

## C. Familias ya recorridas (IDX README «Closed families» y catálogos 03–04)

Advertencia de lectura. «0 admisibles» en el índice significa «ninguna semilla, tal como se formuló,
pasó los filtros probados»; no significa imposibilidad. Sólo C1 es prohibición. C2–C4 no se relanzan
como estaban, pero son terreno legítimo con el cambio que se indica. La clasificación de la fase 193
candidata por candidata está en `ANNEX_PHASE_193_LABELS.md`, corregida en 22 puntos por la lectura
de las 128 memos primarias (`ANNEX_PHASE_193_PRIMARY.md`, que manda donde difieren).

### C1. Cerradas con falsificador explícito o NO-GO de clase PROVED

Estadística y fenomenología numérica · espectral inverso / Jacobi / Mercer · núcleos de Li y Bochner
en ordenadas · flujo de calor, Laguerre–Pólya, Jensen · positividad total de orden ≥ 5 (el núcleo no
es PF₅; falla en PF₂ en 104_21) · Baker · Fredholm, determinantes, Birman–Schwinger, Szegő–Widom ·
SOS aritmética pura para T ≥ ½log3, certificados exteriores positivos · cribas, progresiones,
intervalos cortos · información de ceros · promedios sobre caracteres · Sonin, prolatos, semilocal como
fuente de signo · coercividad, Schur, inercia, Wiener–Hopf, dos sectores de Nyquist como fuente de
signo · álgebra Euler/Möbius, particiones de operadores, conos · transporte en σ, reflexión,
conjugación · flujo de altura en σ = 1 · conjunto de invención de la fase 194 (Lévy/Hamburger,
superficie de pares, Farey/Möbius, Mp₂, Kronecker–Hurwitz, conos por ∂log, integralidad, entradas
aditivas, correlación de pares) · Petersson, Rankin–Selberg en la forma probada, Maass–Selberg ·
Bost–Connes, Araki/Petz, NC-SOS · trazas de Selberg/Arthur · p-derivaciones, Stepanov, suma-producto ·
Markov, principio del máximo, virial/Pohozaev, Almgren · OS/tablero, GKS, FKG · construcciones tipo
Viazovska (lo construible vale para Epstein) · aritmética de sitios primos (paridad, residuos, series
singulares) · estabilidad real / MSS, Bakry–Émery Γ₂, bootstrap, resurgencia, mezcla de bandas ·
defecto/continuación, índice de Morse, firma de Kreĭn, tangente integralidad+EF, Farkas {0,1} ·
programa L♯ (forma exterior, Grönwall, serrucho de Möbius, pasividad, ternas de borde) · objeto de
signo de la fase 200 (OS en el borde, Γ-límite, Fejér–Riesz, Cholesky, escalera Q2, cortes, dimensión
de von Neumann, medidas de Loeb, Rankin f×f̄) · rango no negativo, recurrencia {x+y,xy}, positividad
importada · tabla exterior de la fase 202 · composición E∧F encadenada y mecanismos continuos
uniformes (fases 205–207) · fase 211: dominaciones de escala fija, familias de palabras de (M,Π)
homogéneas, criterios de germen de Carleman, cierres por productos cosh, capa de Laplace D_{2π}.

### C2. Sólo argumentadas (falta la prueba del descarte; se reabren con objeto escrito)

Lewis–Zagier · entrada líquida arquimediana · KMS · Hodge–Riemann lorentziano · VOA y Soergel en forma
de monoide (descansan en cláusulas condicionales de P47) · lema del monoide G1 / derivada aritmética ·
Γ-convergencia · Dobrushin/TAP · Cheeger · Brascamp–Lieb geométrico · Vinogradov.

### C3. Reformulaciones exactas (objetivos válidos; falta el mecanismo, no están cerradas)

Certificados duales, de retículo y flat-top (la clase dual es el propio objetivo) · matrices de
retículo entero y conjuntos multiplicativos · cuerpos de funciones, Hodge, Arakelov, sitio aritmético ·
Floer, Bridgeland, motívico · supersimetría, Jordan · Lasserre, Guerra · flujo espectral · 𝖯⋆ ·
Arch ≥ Near en sitios primos · programa lineal en sitios primos sobre el toro · L*_j(θ) · las 43
reformulaciones de la fase 204.

### C4. Una línea o sin examen suficiente (no cuentan como intentadas)

Índice de Jones / Temperley–Lieb · t-concavidad · Rayleigh fuerte · Lee–Yang · Iwasawa · semillas
G11, L7, L9 de la fase 193 (F6, F7, F13, K7, M7, H3, I8 sí tienen pruebas o reducciones PROVED en sus
memos; C7 y CE6 fueron desarrolladas y quedan sólo argumentadas, con falsificador numérico) · autovectores en espacio equipado · repulsión
anti-Siegel. Verificar en el índice antes de usar.

Dos lemas faltantes cerrarían de una vez muchas filas de C2: un falsificador PROVED para sistemas de
Beurling o cuerpos de números (O11, O12 de P47 thm:shape), y un fondo primitivo negativo PROVED para
la forma de Epstein x²+5y² (hoy citado para la forma completa y argumentado para la primitiva).

### C5. Residuos abiertos de la fase 193

Rankin–Selberg en w (A1r: la parte w > 1 está cerrada, la continuación sólo argumentada) · paquete
metapléctico (A3r: rango uno PROVED, exclusión argumentada; su residuo es la variante de Kuznetsov) ·
Salié/Kuznetsov (A4r) · medias de Fejér en puntos fuera de la línea · factorización de Schur a M fijo · autovectores equipados
construidos con primos · residual de Δ ≡ 0 · objeto polarizado sobre ℤ con clase amplia (G-F) ·
positividad total de orden ≤ 4 (los cuatro generadores y el signo global del Wronskiano de cuatro
densidades están PROVED en 211; falta el transporte global) · transferencias no unimodulares · D_∃c · SPEC_A con sólo
identidades · el paso ½log5 → ½log7.

## D. No relanzar de la fase 211 (con condición de reapertura)

Resumen. La lista completa, deduplicada y con línea de origen, está en `ANNEX_211_GLOBAL_REVIEW.md` §A
(54 ítems) y `ANNEX_211_GRAM_HYPERBOLIC.md` §A (24 ítems); las de los demás archivos de la fase, en
`ANNEX_211_FILES_*.md`.

D1. Reconstruir el puente de densidad u otra parametrización de la escalera — falta el signo en todos
    los tamaños, no el puente.
D2. Añadir dimensiones de filtro, optimizar umbrales, extender la torre de órdenes finitos. TP2 no
    implica positividad total de todos los órdenes; pares no implican triples, ni concavidades
    cuatro nodos (contraejemplo 3×3 a «V‴ > 0 ⇒ orden tres», 211/074; ciclo (p,p,p²)).
D3. Inferir densidad o signo de una unión positiva. La densidad L² sola no da continuidad de la forma
    completa; reparar el momento con generadores positivos uno a uno no paga los cruces; variar la
    tasa no repara la densidad de la unión (211/096). Se reabre con liminf r(n)²/n = 0, un bloque
    que repare el momento **y** control de sus cruces.
D4. Recurrencia o descenso solos. Se reabre con una cota aritmética uniforme del resto promediado
    R_L ≥ −ε_L, ε_L → 0 (basta el promedio por entrada inicial, no cada átomo), o con una familia de
    subespacios conjuntamente positivos que aproxime en una topología donde la forma sea continua. La
    cota debe distinguir el multiplicador real del desplazado (falsificador W_4 = W − 4‖·‖²).
D5. Monotonías Schur–Green — sólo con un invariante conjunto distinto conservado por cada operación.
D6. Identidades de calor/Poisson/theta renombradas — sólo con una desigualdad conjunta concreta.
D7. Variantes del presupuesto del inverso acumulado (211/POWER_CUMULATIVE_INVERSE_022) — sólo si pagan también ARCH_♯ y justifican su alcance en k.
D8. Arch − Div − Near por Poisson/divisores, familia suave s_w, colas con gauge, patrones de casi
    coincidencias — sólo con hipótesis nueva que resuelva el fallo identificado.
D9. Comparar Off con la energía divisorial E_y, o A con una fracción fija de R_res: refutado por
    falsificador explícito (pares k, k+1; 211/GRAM_SLICES §17.6); tampoco hay cota superior uniforme
    en norma; no se paga por separado el operador de dilataciones (§17.7) ni por resolventes (§17.8).
    Atención: en y = 0 la desigualdad Off ≥ −R_res es exactamente A_0 ⪰ 0 sobre enteros, es decir el
    objetivo completo, a probar sin margen; no es una obligación más débil.
D10. Pequeñez puntual de la cola o un número fijo de derivadas como transferencia de todos los órdenes;
     margen de Cauchy uniforme entre capas (§8.11).
D11. Localización nodal de un testigo negativo; tasas positivas antes de T; partición par/impar BPY a
     escala ¼; concavidad de Jensen / de operadores (ésta con la condición de reapertura de
     211/GLOBAL «Control de duplicación posterior: cuatro propuestas sin construcción»).
D12. Ensamblar certificados PSD de soporte fijo (211/POWER_FIXED_BLOCK_ASSEMBLY_OBSTRUCTION);
     minorantes de soporte finito (211/GRAM_SLICES §18.7).
D13. Orden matricial por desplazamiento K − K_shift con desplazamiento 2: refutado
     (211/POWER_SIMULTANEOUS_SHIFT_OBSTRUCTION). Otros tamaños y normalizaciones quedan abiertos en
     la fuente; no relanzar sin operación nueva.
D14. Completitud de cuadrados / todas las potencias: la integralidad identifica, no firma. Los
     falsificadores de orden fijo valen con N ∈ {0,1}; el de todas las potencias necesita N(2) = ½;
     residuo exacto 1 y conteo x + O(1) tampoco bastan (211/SQUARE_COMPLETENESS_OBSTRUCTION §§6, 9–11).
D15. Métrica **local, positiva y acotada** para la realización theta, con coeficiente principal fijo y
     sin conexión nueva: excluida (211/HYPERBOLIC §12.7). No excluidas: métricas no acotadas o no
     locales, conexiones nuevas y otras realizaciones; la selección sin núcleo explícito ni identidad
     de Green ya se rechazó.
D16. Capas de Gram theta y sus variantes: modos individuales, prefijos finitos, cortes suaves
     positivos, prefijo más cola continua, simetrización, cortes de Jacobi, amortiguación n^{−δ},
     primitiva U, capas J_u; Hankel; CPD/TP2 («A no es TP2»); HCM; referencias G0/H0; ramificación
     theta; rigidez y contractividad BPY en la métrica recíproca; descenso B_1 → B_0; factores
     (D_t² + λ); dos fases A_0/A_π; colecciones fijas de ramas de G2. La capa de Laplace D_{2π} es
     indefinida, lo que refuta la premisa por capas; su compensación integrada sigue OPEN.
D17. Rondas 1–27: familias de Krylov y de palabras de (M, Π) a grado acotado u homogéneas; ventanas en
     c; regla Poisson/ℱ; 𝒜𝒫 − c𝒞 con c ≠ 1; cotas de Weyl desde Arch − θ; proceso B / Vaughan;
     planos Λ-libres E_k y todo subespacio fijo finito libre de Λ; clase suelo de Schur, también sobre
     bloques agrandados; ensamblajes de dos y tres bloques; truncación de Neumann del acoplamiento de
     Schur; clase 𝒦_S (estimaciones que sólo ven la masa del peine); clase 𝒦_gap (hueco espectral);
     Grönwall en T (reformulación); valores grandes con Kovrijkine / Logvinenko–Sereda; λ_max(A_τ)
     sin restricción de banda (falso como condición); signo sólo desde el bloque alto o sólo desde el
     bajo; captura del signo en E_T; ceguera de Lanczos; rayo de exponentes ℕ^{1+t}; maximización
     global de μ_T(v); producto de Schur local × arquimediano sobre la razón coprima. Precisión:
     «𝒜𝒫 − c𝒞» no está acotada inferiormente sobre la clase completa de colas, mientras que un
     representante fijo tolera c ∈ [0, 3.5]; por eso no es paso de signo. Nunca omitir el término
     polar 2AB.
D17b. Criterios puntuales de la serie POWER (lista completa en `ANNEX_211_FILES_1…5.md` §A):
     positividad de todos los T_m de Abel, componentes Erlang, Ω ≥ 0, I_* ≥ 0, h_N ≥ 0 y K_N ≥ 0
     universales, prefijos de Möbius, contracción absoluta de Möbius, criterio de primitivas
     positivas, monotonías al mover polos, herencia T_f ⇒ T_H, monotonía de Peano y de Loewner de
     contactos, reflexión q ↔ 1−q, descartar el término 2V de Selberg, reparar sólo con el contacto 2,
     base afín, Turán de los valores completos, convexidad del funcional gaussiano, núcleo de
     Volterra bruto.
D18. Las ocho selecciones de la memoria de las reglas del proyecto: cuadrados factoriales y proyecciones físicas;
     compensación entre escalas sin positividad por átomo; primitivas compensadas de capas; sumación
     por partes discreta en theta; cambio (m,n) → (m+n, m−n) y paridad; reserva de métricas no
     locales; transporte por desplazamiento y congruencia; cancelación conjunta de Pfaffianos por
     reciprocidad. Cada una se reabre sólo con una operación explícita y los cuatro puntos.

## E. Batería de falsificadores (P47 thm:shape; P48 tab:cert, tab:models)

Mínimo obligatorio: borrado finito Λ·1_{n≥N}; amplificación Λ + c·1_{n=n₀}; cΛ con c a ambos lados
de 1; a_P (potencias de primos p < P borradas: conserva producto de Euler, rompe sólo la ecuación
funcional); Davenport–Heilbronn; Epstein x²+5y²; modelos de cuarteto ξ_{z,k} (conservan Λ(n)
exactamente y la ecuación funcional); deformación autodual f_t (conserva Λ(n), n < λ₁, y la ecuación
funcional; rompe Euler e integralidad); sistemas de Beurling discretos; b_θ = Λ·½(1+cos(γ log n+ϑ)).
Para cada uno la memo dice **qué línea exacta del argumento falla**. Cuartetos y f_t tienen el mismo
nodo que Λ: una propiedad del peine solo no los separa (P47 cor:shape (a)).

## F. Lo que los papers declaran no excluido (el terreno de esta fase)

- Conjunción (E)∧(F)∧(I) con paso de signo no lineal (P47 rem:conjunctions).
- Construcciones que usan la multiplicatividad exacta de Λ en el paso de signo (P47 thm:noimport).
- Desigualdad exacta 𝓕_T ≤ 𝔞^♯ sobre P_T probada con el vector y la forma arquimediana juntos, sobre
  vectores que ven Near_M (P47 rem:bar-arith).
- Argumentos con la estructura atómica del lado aritmético y los valores exactos (P47 rem:bar-pat);
  clases que mezclan estimaciones con un axioma exacto de soporte en log ℕ (P47 thm:geo-tv).
- Uso de la parte positiva del símbolo en todo ℝ junto con el conjunto negativo; reducciones exactas
  que llevan todo el margen (P47 rem:bar-loc).
- Medidas exteriores con signo. (Los cuadrados aritméticos en (½log2, ½log3) no son terreno de
  esta fase: 211/DOSSIER_001 §6(e) los reduce a un solo autovalor.)
- Funcionales no distribucionales y funcionales que acoplan con ζ misma (P47 thm:geo-parity).
- Leyes bilaterales λ_A = L(T)(1+o(1)) en rangos no acotados (P47 rem:bar-fam): no excluidas, pero
  su mitad inferior es el objetivo más un margen (211/ROUND_007_D Lema 4.6), y la ley exponencial
  simple tiene NO-GO (211/LEDGER C20). No es terreno más fácil que el objetivo.
- Casilleros sin objeto: O166.802.1 (desigualdad multiescala no lineal, «completitud parcial más allá
  de X»), O2601.1 (propiedad individual de Euler), cláusula (5) de P47 prop:spec.

## G. Restricciones duras y prohibiciones explícitas de fases anteriores

G1. **Composición de Euler y ecuación funcional (regla O1).** Los dos canales deben acreditarse con
    falsificadores distintos: a_P para la ecuación funcional, cuartetos para el producto de Euler. Un
    argumento que sólo falla para uno de los dos está usando un solo canal.
G2. **Fases 199–200 (IDX README l.508–567):** R-K1 (no reflexiones de borde ni núcleos completamente
    monótonos en dato exterior); R-Q2 (escalera de mollifiers); R-Π y R-Π4 (el gauge Π_μ es común a
    todos los falsificadores; peine de saltos); R-Z1 (el portador Z es el multiplicador en la línea);
    C-Guo (toda fuente de signo por radical, gauge, polo o modo de Tate debe nombrar la propiedad
    ausente en Epstein); C-hom (no hay identidad cuadrática ni de cuatro puntos en los coeficientes
    theta; Bochner en θ excluido); R-MOM (las constantes de orden ≥ 2 de momentos entran con
    coeficiente neto cero); Teorema M200.
G3. **Hipótesis a romper para reabrir la fase 194:** H_cone (premisas cónicas en log ζ o su derivada
    logarítmica), H_mono (integralidad monótona), H_sparse (estabilidad por modificación rala).
G4. **Fase 204:** Lemma F en cualquier variante sobre representantes (uniforme: falso por falsificador
    explícito; existencial: vacío); Stein sobre F; Hardy sobre λ; el canal q_odd sin cota inferior
    independiente de ½ − q_odd en ½log15; entrelazado o primer cruce para (L2) como método; estabilidad
    real, hiperbolicidad o entrelazado sobre símbolos de Gram.
G5. **Fase 209:** núcleo no local, mapa U011, dominaciones LINK012–014, lema J+C (ver
    `ANNEX_INDEX_README.md`).
G6. **Muros con nombre** (enunciado de cada uno en `ANNEX_INDEX_04.md` §4.1): W1–W12, T1–T5,
    W-identification, W-jet, W-Sonin, W-factor, W-dither, W-coh, W-cont, W-sieve, W-tail, W-lin,
    W-det, W-fam, W-pat, W-loc, W-mom, (N′), thm:X como condición necesaria.
G7. **Falsificadores adicionales** a los de §E (definición en `ANNEX_INDEX_04.md` §4.2): Ξ_a, ζ_K/S₃,
    cuerpos de funciones, curva de dos átomos de tipo I, modelo 3×3, Λχ₂, M_m, Λ̃, ζ_θ, sustitución de
    raíces ℕ ∪ √2ℕ, K(s), f_χ, P_{a,c}, P_171, ζ̃, peines de Poisson, M₁, banda baja.

## H. Anexos de lectura completa (lista entera; mandan sobre este resumen)

| Anexo | Fuente leída línea por línea | Contenido |
|---|---|---|
| `ANNEX_INDEX_04.md` | IDX `04_PHASES_100-189.md`, 1058 líneas | las 824 filas asignadas a 38 familias; 227 filas que no son clausuras (416 con las parciales); etiquetas dudosas; muros y falsificadores |
| `ANNEX_INDEX_README.md` | IDX `README.md` l.366–2396 | unas 565 entradas; clausuras firmes y no-clausuras; bloques positivos |
| `ANNEX_PHASE_193_LABELS.md` | fase 193 (ledger, tablas de semillas, auditorías) | cada candidata en una de cinco clases |
| `ANNEX_211_GLOBAL_REVIEW.md` | 211 `POWER_GLOBAL_ROUTE_REVIEW.md`, 2611 líneas | 92 secciones; 54 «no relanzar»; 31 positivos; 30 obligaciones abiertas; 27 insumos que cambiarían la obligación |
| `ANNEX_211_GRAM_HYPERBOLIC.md` | 211 `POWER_GRAM_SLICES_OBSTRUCTION.md`, `POWER_HYPERBOLIC_MODEL_GRAM.md` | fórmulas de cada objeto; 24 «no relanzar»; 18 grupos positivos; 8 obligaciones abiertas |
| `ANNEX_211_FILES_1…8.md` | los 401 archivos restantes de la fase 211, en ocho bloques alfabéticos, todos leídos enteros | una entrada por archivo; unos 210 ítems «no relanzar» con condición de reapertura; positivos; obligaciones abiertas; pasos nombrados y nunca retomados |
| `ANNEX_PHASE_193_PRIMARY.md` | memos primarias y revisiones de la fase 193 | desacuerdos con `ANNEX_PHASE_193_LABELS.md` |
| `REVIEW_001_LC.md`, `REVIEW_001_ABD.md` | revisión hostil de la ronda 1 | enunciados corregidos y alcance |

Advertencias de los anexos. En el catálogo 04, 73 filas no registran motivo (el campo repite el
nombre), unas 17 rutas figuran con estados contradictorios en filas distintas, y varias filas «DEAD»
significan «superada» o «nunca ejecutada»: una fila sin motivo registrado no es una prohibición. Las
«43 reformulaciones» de B3 son las de la fase 204 y no se comparan con las 141 filas REF-D del
catálogo 04 sin deduplicar.

Límites conocidos de la cobertura. (1) El índice de rutas resume por fase y no por archivo: la mayoría
de las memos de las fases anteriores a la 190 no tienen fila propia. Caso comprobado: las memos
R170_811–840 de la fase 170 (entre ellas R170_816, que falsifica «h ≥ 0 ⟹ apareamiento ≥ 0», y
R170_819–823) no figuraban en el índice; la fase 170 se leyó entera después (sección I y
`ANNEX_170_FILES_1.md`–`_4.md`), pero otras fases grandes anteriores a la 190 siguen sin lectura por archivo. Una búsqueda sin coincidencias en el índice no prueba que la
idea no se intentó: hay que buscar también en las carpetas de fase. (2) `ROUND_008_A.md` de la fase 211
está truncado (termina en la Observación 3.3). (3) Los valores numéricos de validación de
`STATEMENT_001.md` §3 están pendientes de recomprobación (normalización de F_0).

## I. Fase 170 leída por archivo (112 memos; `ANNEX_170_FILES_1.md`–`_4.md`)

Toda la fase trabaja con un vector del radical de una ventana de primer contacto supuesta y con
funcionales lineales en F; ninguna memo escribe una identidad (G). Lo que sigue ya está recorrido y no
se relanza sin la condición indicada. Los cuatro puntos T1–T4 son el terreno que la ronda 1 dejó sin
excluir.

I1. **Incidencia de divisores como forma positiva (T2, T3).** R170_863–868. Con coordenadas libres el
    núcleo de ∂ = [B, −I] es el grafo universal y la forma no ve los pesos (865). Con una coordenada
    a_d repetida en todos los múltiplos, 𝒟_N(a,c) = k^{−1/2}((a∗1)(k) − c log k) tiene núcleo
    exactamente ℝ(Λ,1) (866, PROVED). Toda fila lineal que anula esa línea factoriza por 𝒟_N, y toda
    extensión lineal positiva es un cambio de métrica que pierde el primer jet (867–868, NO-GO de
    clase PROVED, también tras tensorizar con el espacio físico). La forma vive sobre coeficientes,
    no sobre F. Reabrir exige un objeto que no sea una fila lineal sobre ese espacio, o la coordenada
    de borde β_T(f) de 868 §5 construida desde la ecuación de primer contacto. La matriz
    [log mcd] = E diag(Λ) Eᵀ no fue usada sobre F en la fase 170, pero sí en la 211:
    `POWER_GLOBAL_ROUTE_REVIEW.md`, «Extensión factorial antes de resonancia» (Σ Λ P_m*KP_m con
    entrada K_{λμ} log mcd(q_λ,q_μ)) y `POWER_GRAM_SLICES_OBSTRUCTION.md` §17.2. Es la selección
    rechazada «cuadrados factoriales»; la única instancia con incidencia escrita es la modal theta, y
    las familias por ventana distintas de ella no fueron examinadas (`ROUND_002_B.md`,
    `REVIEW_002_BC.md` Parte B).
I2. **Identificación Λ∗1 = log usada linealmente (T3).** R170_101, 401 §4, 704, 814–816, 835 §2.2,
    837 §6, 838 §5, 840 §5, 878–884, 896–897. Anula exactamente el bloque k ≤ N; un monitor nulo no
    da signo, al recombinar la forma vuelve a ser independiente del peso (837 (6.7)), y todo uso
    lineal cae en el ideal factorizado Q𝒟_N y no determina la clase de borde (869, PROVED). Vía
    Cauchy–Schwarz con la probabilidad Λ(d)/log k: |β_Λ|² ≤ (log k)Σ_Λ, pero β_Λ es impar y cambia
    de signo (841 §4.2; β(12) < 0). γ = Λ·log − Λ∗Λ choca con el descarte de Selberg (850–851);
    γ + W = 2Λ·log no sobrevive al bloque de Poisson (856).
I3. **Paridad.** La clase de borde β_phys = 𝔚_K + Θ_ext es lineal e impar en F; minimalidad, virial y
    cono tangente son cuadráticos y pares. Un signo unilateral de β en el radical equivale a su
    anulación (870, PROVED). Variar β conservando Λ∗1 = log, PC lineal, el cociclo de Tate y la
    minimalidad diagonal es posible (874, PROVED).
I4. **Residuo común (T4).** La cola H_{M,N}, k > N, con h ≥ 0 aparece siempre como operador o
    apareamiento −Re⟨H_{M,N}𝓕F, S_L F⟩, sin signo y sólo con cota bilateral (816, 819–821, 841
    Teor. 6.1, 856). Exigir un residuo común entre +D_Δ y −‖W^{1/2}𝒢F‖² es exactamente el cierre
    (837 Teor. 5.1, PROVED): no es una pieza intermedia. La conversión literal en
    Σ_{k>N} h(k)|ℓ_k(F)|² no fue intentada en la fase 170; en la ronda 2 de la 212 quedó excluida
    para la cola aislada con finitos momentos Gamma y resto ≥ 0 (`ROUND_002_A.md`, Lema;
    `REVIEW_002_A.md`), obstrucción de formato genérica en el peso. La conversión conjunta con los
    bloques de E_N y de Tate sigue sin objeto y sin exclusión.
I5. **Cuadrados por canal primo y promedios en la dilatación (T1).** Σ(Λ(n)/√n)‖F − U_nF‖² da
    «cuadrados − constante» con constante divergente y es genérica en los pesos (201, 301;
    falsificador a₂ = 100). Promediar la dilatación sólo da suavizado y compacidad, sin signo ni
    uniformidad (823–826). La energía de Laplace en la retícula Gamma G_δ = 𝓡*𝓡 es positiva (843,
    positividad CITED) pero no separa Λ de pesos alterados, el residuo polar sale con el signo
    contrario (844) y la extracción da un virial filtrado, no el físico (849). Completar el cuadrado
    D*G⁻¹D con D aritmético es congruencia pura (860–861, PROVED). El término virial
    ∫τ m′(τ)|F̂|² de 840 (8.1) queda con signo OPEN sobre el radical.
I6. **Leyes bilaterales por composición lineal.** 840 Teor. 6.1 (NO-GO PROVED, puntual en T): ninguna
    ley bilateral de collar sale de composiciones lineales de PC, Chebyshev comprimido, reflexión,
    collares, ecuación débil y minimalidad.
I7. **Otros cierres.** Conjugación unitaria multiplicativa conserva el espectro; multiplicador local
    con fases para todo primo es e^{iφ+iθt} (501). Compensación no local Z − RZR ≥ I + R sólo suma
    coste positivo (601). Intercambio de factores (d,m) ↔ (m,d): coincide con el concomitante de
    soporte ya conocido y no fija el operador físico (871–872, 876–877).
I8. **Abierto con obstáculo exacto.** La identidad lineal 𝔚_K(f) + Θ_ext(f) = 0 (859; forma
    explícita 856 (8.7)); el «ancla nula con borde» e_T (862); la deformación lineal aritmética del
    complemento de Schur con primer jet no nulo (861); VIR–LB y VIR–DET (840 §8), que juntas tienen
    la fuerza del cierre; los dos momentos exteriores de 894; el canal de dos bases primas
    (850 §5): cotejado como repetición, lineal en el peso; residuo delimitado en
    `REVIEW_002_BC.md` C.3 punto 3. Varias memos dependen de (REG)/C¹, no probada.

Avisos. Los anexos registran inconsistencias entre memos (retiradas 844→846, 851→854→856, 861→862;
correcciones de 838 a 837; 870 §§6–7 copiado de 871). Los diez `verify_*.py` y los seis JSON de la
carpeta no fueron analizados. Varias memos usan una equivalencia externa del objetivo; se registró
sin desarrollarla y no se usa.

## J. Ronda 3 de la fase 212 (`REVIEW_003.md`): clases cerradas y antecedentes recuperados

No relanzar sin la condición indicada. Ninguno de estos resultados lleva signo.

J1. Multiplicadores y reflexión J en sectores de paridad: reparto puntual del símbolo (R3-a). Antecedentes
    de los productos mn: R161_032, 034, 035; E70_10 opción graduada. Reabrir: operador fuera de esa
    álgebra (compresión a la ventana, M_t, rango finito).
J2. Cuadrado afín en el peso con término cruzado igual al peine: ρ ≤ Arch, no ⪰ 0 (R3-b), también en (S).
    Reabrir: V sin emparejar, V_0 dependiente del peso o V no afín en Λ, con fórmula propia.
J3. Factorizaciones canónicas (raíz de la forma, LDL en cualquier orden, Fejér–Riesz, Wiener–Hopf):
    existen con resto ≥ 0 si y sólo si vale el objetivo (`ROUND_003_2.md` Lema 2; fase 200
    A_MU_FACTORIZATION_001 §1). Reabrir: factor con fórmula propia cuya igualdad se pruebe después.
J4. Ancla nula con borde y coordenada β_T dentro de una forma semidefinida: invisibles (R3-c).
J5. Virial de dilatación pura sobre todo P_T: sin identidad con resto acotado inferiormente (R3-d).
    Antecedentes: R162_501 Teor. 2.2 y Prop. 3.1; 106_124 §1; R165_202 1.4; 211 ROUND_008_C Prop. 5.
J6. Signo de un bloque exterior separado de la identidad de Poisson–Chebyshev, con cualquier test que no
    use el peso, envolvente en los parámetros o paso al límite: homogéneo en c (R3-e).
J7. 𝔸_M = WᵀDW con W soportada en la divisibilidad: no existe para M grande (R3-f). Arch_M es
    indefinida (CA_K_001 Prop. 1.3(a), CITED).
J8. Riccati/Darboux con el peine como superpotencial: fase 70, E70_10–12; R166_502 §5; CA_G_001 §2.
J9. Métrica no local en identidades de Green de tipo resolvente: determinada por M; su positividad es la
    de la escalera (R3-g). Precisa la entrada «reserva de métricas no locales».
J10. Incidencia de divisores en la malla de Nyquist: 211 ROUND_005_C Prop. 2 y §5.3 (vale para sistemas
     de Beurling y a_P). Valores y jets puntuales no son componentes admisibles de V_T (R3-h).

Regla de método precisada (R3-i): una ruptura formal aislada no prueba el signo. Se exige una identidad
completa demostrada con un lado derecho no negativo para Λ. En un falsificador puede fallar esa identidad
sin que pierda positividad el objeto auxiliar; no se exige que necesariamente cambie de signo el resto.
Véase la auditoría de O4/O17 y del Lema T al final de la Parte V del índice.

## K. Fase 161 leída por archivo (83 memos y README; `ANNEX_161_FILES_1.md`–`_3.md`)

Desde R161_004 la fase trabaja sobre un vector del radical de un primer contacto supuesto; ninguna memo
escribe (G) sobre todo P_T salvo la meta SP-161 de K7. Varias memos usan una equivalencia externa del
objetivo; se registró sin desarrollarla y no se usa.

K1. **Compresión a la ventana, fuga, posición, rango finito.** Recorridos a fondo. Cuadrados de fuga
    ‖(I−P_+)C_log g‖² (020), X_T = ½‖(I+εC)g‖² (021), fuga coherente comprimida (034 (5.2)), fuga
    exterior de Poisson (040): correctos, sin identidad que los conecte con el defecto finito de PC. El
    test Π_TP_TZ*g colapsa en el apareamiento mixto de (PC-ren) (023). Green mixto con X = M_t: piezas
    residuales sin signo (042); el término de Tate de Xf es 0 por paridad (043); el primitivo es una
    tautología de modulación (044). Toeplitz–Hankel local de rango uno no globaliza (045). Reescrituras
    de Green y de potencia terminan en el conmutador [P,S] (057, 059, 062–065). Rango finito: sólo el
    primer collar (013, 016); reducción a λ_max(M) < 1 sin cota (073–074). Reabrir exige una identidad que
    conecte un cuadrado de fuga con el defecto de PC, no otro cuadrado de fuga.
K2. **Varianza orientada de divisores (030).** Identidad PROVED con un término de grado dos en Λ que
    suma, ½ΣΣΛ(d)Λ(e)‖m_d − m_e‖². Se anula por coherencia de las traslaciones para cualquier peso, no por
    Σ_{d|n}Λ(d) = log n: genérica. La realización falla: los vectores de camino no dependen de d (031);
    la física es la suma coherente en k con Gram cruzado sin control (033); su diagonalización es canal
    cociente más canal producto (034; colisión con la fase 106).
K3. **Salida A de 033 (dilatación de Parseval/Naimark con etiquetas k).** Enunciada, nunca construida;
    035 la declara innecesaria y 052–053 construyen otra dilatación sin etiquetas, cuya tangente da la
    media U+V y no la diferencia (056). Exige compensar el Gram cruzado de 034. Sin prueba de
    imposibilidad.
K4. **Formas indefinidas.** Ω simpléctica retirada (diagonal nula, todo vector neutro; 061→062); B
    hermítica usada sólo en la diagonal (063); matriz cruzada de Tate indefinida, rechazada como Gram
    (023 §4; 032). Ninguna memo estudia un vector neutro no radical.
K5. **Resto de hipérbola.** h(k) = Σ_{dm=k, d≤M, m≤N}Λ(d) ≥ 0 (001 Teor. 2.1); ninguna ponderación
    w_N ≥ 0 lo cancela (002 Teor. 8.1). El Möbius truncado c_N(k) no aparece en la fase.
K6. **Q ≥ 0 sobre todo el espacio primitivo** para la Q de 071: excluido (081 (2.1): falla en autovectores
    con λ ≥ 0). Sólo podría valer en el radical. Contramodelos: 038 (2×2) a la saturación automática; 050
    (3×3) a la transferencia entre bloques.
K7. **Abierto.** SP-161 / L161.1 (002 §§4–5): a_T = Σ w_N Re⟨RF, S_N𝓕F⟩ + cuadrados de fuga de
    C_T = (1−P_T)𝓕P_T, sobre todo P_T; sólo murió la rama w_N ≥ 0; la versión con pesos con signo o
    derivadas discretas no fue escrita. Contabilidad conjunta 032 (4.2), no derivada. Saturación coherente
    (035, 037, 039), que exige una identidad de Green de borde física ausente del corpus.

Avisos. La exclusión de R161_018 («todo límite lineal del grafo de PC es tautológico») está declarada no
establecida por R161_075; no se usa como cierre. La síntesis R161_099 no cubre 046–081 y mantiene esa
exclusión. R161_010 Teor. 3.1 fue retractado por 011. No existen R161_082–098. Los cuatro scripts no
fueron analizados.

## L. Ronda 4 de la fase 212 (`REVIEW_004.md`): clases cerradas y antecedentes recuperados

L1. Meta L161.1 (R161_002 §§4–5) con pesos reales en el índice de corte, con signo o sin él: única
    solución trivial (R4-a). K7 de la sección anterior queda cerrada en esa clase.
L2. Pesos de criba (Selberg, Barban–Vehov, GPY, Λ_R) como test o inverso: fase 200 Q1–Q3, MULT_GAUGE,
    GG_001; R162_1003 §4. No elevan el grado en el peso (R4-b).
L3. Defecto de divisores cuadrático que suma, exigido para todo peso: objetivo con margen (R4-c); fase 197
    BARRIER_D2_001.
L4. Inversos aproximados invariantes por traslación, Möbius truncado incluido: reparto del símbolo; R ≤ 0
    falso (R4-d); fase 200 A_MU_FACTORIZATION_001 (d).
L5. Pivotes determinados por el patrón de casi-divisibilidad; núcleos totalmente positivos, de Pólya, de
    Green o función del mcd para 𝔸_M (R4-e).
L6. Conteo de inercia, signatura de Kreĭn o Pontryagin: P47 thm:parityschur, prop:polarcap,
    subsec:inertia-excl; fase 197 BARRIER_W_001. No distingue c = 1 (R4-f).

## M. Cotejo de mecanismos de signatura y de cierre (`ANNEX_COTEJO_LORENTZ_1.md`, `_2.md`)

Cotejo por grep en todo el corpus con 31 y 36 archivos abiertos en primaria; no es exhaustivo.

M1. La lectura «a lo sumo una dirección negativa por sector de paridad» ya está en `R160_C7_R1` §§5–6:
    la clase cuadrática lorentziana, el cierre por límites, Alexandrov–Fenchel y la versión combinatoria se
    reducen sobre la forma cuadrática al enunciado original (Prop. 6.2). §6.3(2) deja OPEN un objeto de
    grado ≥ 3 con hessiana −a_T, por falta de una fuente independiente de coeficientes no negativos.
M2. Mecanismos de cierre ya intentados: fase 120 (inducción combinatoria sobre un retículo de colisiones
    de potencias de primos; la iteración aditiva no se inyecta en un join idempotente, Φ(2i) = Φ(i));
    `114_d_244` (forma tangente con inercia (1, |S|−1); obstrucción de rango; no identificada con a_T);
    fase 197 `BARRIER_W_001` (inducción en la ventana; sus cinco propiedades valen para cΛ, a_P y
    Beurling); fase 65 (shorting de Schur sobre núcleos de un sistema canónico; refutada en R137_005);
    `G2_B8` (suma de formas locales; falla para T > 0.5925).
M3. Sobre 𝔸_M o 𝖡: estabilidad real, Gårding, MSS (`INV_M_001`, falsa); GKS/FKG (`CA_J_002`, frustración);
    positividad total (falla en orden 2); Perron–Frobenius (`H1_PROOF`, sólo simplicidad y paridad).
M4. El muro de la derivada logarítmica (`INV_F_001` F2) alcanza premisas cónicas sobre la serie o su
    derivada logarítmica; no alcanza formalmente propiedades de signatura de a_T ni la integralidad.
    Que sólo crucen las clases infinitamente divisibles y la de Pick es ARGUED fuera de la lista
    clasificada (P47 prop:spec (6)).
M5. No encontrado (no prueba novedad): objeto de grado ≥ 3 con hessiana a_T construido con el peine y la
    ventana; cierre bajo producto de factores de Euler aplicado a la signatura con el factor arquimediano
    fijo, y su comprobación en c = 2; medidas de Lee–Yang o cierre de Newman/Lieb–Sokal construidos
    desde la forma; preservadores de estabilidad sobre s_T; inducción que alargue la ventana para la
    signatura por sector; borrado y contracción sobre el retículo de divisibilidad de [1, e^{2T}).
    Corrección de cita: el descarte F5 de la fase 193 usa «n₋ > 2 en el espacio entero», mal citado
    (`ROUND_004_E.md` Prop. 1).

## N. Ronda 5 de la fase 212 (`REVIEW_005.md`): mecanismos de signatura y de cierre

N1. Signatura de Lorentz o log-concavidad en un punto base: es (G) o el enunciado (R5-a).
N2. Polinomio hiperbólico de grado ≥ 3 con hessiana −a_T: grado dos, o el objetivo con margen (R5-b).
N3. Cierre bajo producto de factores de Euler sobre la signatura: imposible sin balance; con balance no
    queda operación (R5-c).
N4. Inducción en la ventana usando que «el peso entrante está determinado por los anteriores»: la premisa
    vale para todo peso; en el cruce el peso entrante no influye (R5-d).
N5. La forma como varianza de un modelo de valuaciones: es (G); las leyes de ζ^c son probabilidades para
    todo c (R5-e).


## O. Ronda 6 de la fase 212 (`ROUND_006_WINDOW_SPLIT_NUMERIC.md`, `REVIEW_006.md`): reparto por primo dependiente de la ventana

- O1. Regla «cada primo cede el núcleo en la distancia de su propio contacto» + potenciales `W_p(t)` libres:
  rechazada en la puerta. La parte de núcleo es la holgura complementaria del Teorema D de
  `phase-159-row-d-two-front-construction/G2_B8_R5.md` (el máximo interior se alcanza en el indicador del primo
  con mayor `ε_σ(u)`; los valores del §4 ya lo muestran). Como regla previa es circular (J3): las bandas las
  definen los estados obstructores. Con `W_p(t)` libre es la clase M de la ronda 6, `τ = −1.60·10⁻⁴` en
  `T = 0.5925` (NUMÉRICO, una resolución).
- O2. El enunciado literal «el núcleo en la distancia propia no aporta nada» es falso: añadir núcleo en una
  banda alrededor de `log p` sube estrictamente el fondo de la forma local (`REVIEW_006.md`; PROVED para
  `T > log p − δ` si el ínfimo se alcanza, ARGUED en el resto).
- O3. Partes con signo sin regla: reparto vacío (existencia = el objetivo), `G2_B8_R4.md` §1.
- O4. NUMÉRICO, sin antecedente textual: `θ_p(t,s)` de dos posiciones alcanza el techo hasta `T ≈ 0.69` y
  falla desde `0.70`; es genérico en `c`; el dual es un par de estados de igual densidad puntual.
- Reapertura: fórmula cerrada para `θ_p(t,s)` y `W_p(t)` no tomada de un optimizador, no afín en los pesos
  exactos o en relaciones entre contactos de primos distintos, con la ruptura para `cΛ` nombrada y enunciado
  de tres primos; o identidad que escriba la parte negativa de `θ_p` como un cuadrado compensado por un
  término nombrado de otro primo con resto manifiestamente no negativo. Primer falsificador: `T = 0.5925`.

## P. Cotejo del subespacio casi nulo (`ANNEX_COTEJO_NULLDIR.md`)

- P1. Tomar como objeto las direcciones casi nulas de `a_T` sobre `P_T` y buscar una identidad exacta en
  ese subespacio: repetición de la candidata C11 de la fase 211 («par casi nulo y tangencia»), con C8, C12,
  C16, C19, C21, C35, C43, C51. Antecedentes: 211 `ROUND_003_A.md` (paridad, tangencia, rigidez; PROVED, sin
  signo), `ROUND_002_D.md`, `ROUND_002_E.md`, `ROUND_004_A.md` Prop. B (planos finitos libres de `Λ`, NO-GO),
  `ROUND_021_A.md` Lema 3.3 (ancho de la ventana en `c` = margen); fase 192 (tres identidades exactas sobre
  el minimizador, excluidas); Paper 47 lem:contA, cor:Tarch, lem:degen, thm:X.
- Reapertura: un subespacio `S_T` escrito sin resolver el problema y de dimensión creciente, con la
  identidad sobre todo `P_T` y todo `T` y la línea que se rompe para `cΛ`. Sin ejecutar: las conjeturas
  (C1)–(C3) de `ROUND_003_A.md` como teoremas (estructurales; no dan el signo).

## Q. Ronda 7 de la fase 212 (`REVIEW_007.md`)

- Q1. Acotar cada contacto por un potencial `≥ 0` (gauge local, representación de estado fundamental con `φ_p`
  dependiente de la posición, cadenas de cualquier longitud, con cualquier reparto de núcleo): NO-GO con clase,
  PROVED relativo a Paper 47 cor:Tarch; muere antes de `T = 0.60` (R7-a).
- Q2. Predicado de etapa «forma + corrección en un cono convexo» con paso uniforme: equivale a un reparto local
  por contactos, PROVED (R7-b). Reapertura: paso dependiente de la historia con dato de fórmula propia.
- Q3. Dilatación con composición de contactos (salida A de R161_033): repetición de R161_034; el canal de
  cocientes es `∫ĝ|A|²` y no ve la aritmética, el de productos es `∫ĝ Re A²` y no tiene signo (R7-c).

## R. Ronda 8 de la fase 212 (`ROUND_008_A.md`)

- R1. Concomitante de borde que convierta el canal de producto en el de cocientes (demanda de R161_034 §0):
  ya ejecutada y cerrada en la fase 161. R161_035 (cuadrado del paralelogramo `¼‖(U_N − V_N)f‖²`, falta la
  saturación), R161_037–039 (contramodelo 2×2), R161_057–065 (el término de borde es el conmutador de soporte
  `⟨g,[P,S]w⟩`, sin signo; expansión positiva retirada), R161_050 (contramodelo 3×3). Repetición.
- R2. Residuo señalado: usar la ley de semigrupo `τ_{log k}τ_{log l} = τ_{log kl}` dentro del conmutador. Sumada
  con pesos `Λ∗Λ` la regla de Leibniz da `[P,S²]`; el cuadrado asociado, `PS²P − (PSP)² = |(1−P)SP|²`, es la
  identidad de Toeplitz–Hankel de R161_045, cuyo ensamblaje global ya está cerrado allí (fase 122). Lectura
  ARGUED; R161_045 no se releyó entero.

## S. Ronda 9 de la fase 212 (`REVIEW_009.md`)

- S1. Densidad media de los contactos como fuente de positividad y fluctuación como coste: repetición de 188
  N_BUILD_001 / N_BUILD_011 (`κ* > 1`). Polarización de `Λ = μ∗log`: repetición de L2_BUILD_017.
- S2. Recursiones de Schur, Verblunsky, Jacobi, Sturm, Darboux, sistemas canónicos, transferencia por primos:
  todas con antecedente; terminan en J3 o son ciegas al peso. Un paso que use sólo divisores no falla bajo
  Beurling (R9-b, Lema A): toda recursión debe acoplar la estructura aditiva.
- S3. Lista P1–P12 de propiedades del objeto y taxonomía de clases: `ROUND_009_G3.md`. Sin marca y sin objeto:
  contracción en métrica proyectiva con paso dependiente de la historia; funcional convexo con hessiano `a_T`.

## T. Lectura de la familia de Sonin, ronda 10 y literatura de concentración

- T1. (`ANNEX_SONIN_READING.md`) La identidad «forma = cuadrado de Sonin + restos» (R183_018 Prop 3.1,
  PROOF_L_SHARP_D_001 Thm 2.1, R186_015) usa una transformada unitaria para cualquier fase, también con `cΛ`,
  borrado y Beurling; su cuadrado es ciego y el signo queda en los restos (parte lisa y Toeplitz de primos, sin
  signo). `W_{S(T)} = W_T` ya está en R183_030 §1.1. Ningún enunciado sobre los restos fuera de clases cerradas.
- T2. (`ROUND_010_A.md`) La covarianza aditiva entra por tres canales: Tate–Beckner (sin pesos, ciego), Poisson
  sobre ℤ del peine sin pesos (sólo detecta Beurling), y el acople de éste con `Λ∗1 = log`, que es la identidad
  (PC) de R161_001 Thm 3.1. Los dos primeros PROVED; exhaustividad ARGUED. Factorización escalera, dominación por
  el operador prolato y Bochner mixto: repetición (R161_002, K2, J8; W-lin, W11′, B2; CPOS_CLASS_001).
- T3. El residuo que `ROUND_010_A.md` deja como OPEN (pesos `w_N` con signo en SP-161, K7) ya está cerrado en
  L1: con pesos reales en el índice de corte, con signo o sin él, la única solución es la trivial (R4-a de
  `REVIEW_004.md`; `N = 1` da `S_1 = I` y (PC) se reduce a `X + 𝓕X𝓕 = M`). No queda residuo de la ronda 10.
- T4. (`ANNEX_LITERATURE_CONCENTRATION.md`) Literatura de interpolación de Fourier, medidas cristalinas,
  funciones mágicas, prolatos, de Branges, `H²` de Dirichlet: ya en el índice o sin signo dependiente de los
  valores exactos del peso. Cinco mecanismos sin marca sustantiva, ninguno pasa la puerta: transferencia de tipo
  Gauss en densidad crítica; criterio de derivada de Serre con integralidad; reflexión de operadores de orden
  > 2 (residuo de CS0_COMMUTE_001); Borodin–Okounkov en intervalo finito; teoría local de Olsen. Citas sin
  verificar en primaria.

## U. Ronda 11 de la fase 212 (`ROUND_011_A.md`): residuos abiertos de la fase 161

- U1. Signo de una discrepancia de retículo (test integral, Hermite–Hadamard, Euler–Maclaurin) aplicado a los
  restos de (PC): NO-GO de selección. `Δ^R ℓ_T(F)` es lineal en `F`; un signo para toda `F` sobre un funcional
  lineal lo anula (PROVED). `Δ^R` usa sólo el retículo entero con pesos `n^{−1/2}`, sin `Λ`: su signo sobrevive a
  `cΛ` y al borrado (PROVED). Cambiar `log n` por `Σ 1/m` colapsa a la clase escalar de Stieltjes (R161_004).
- U2. Estado de los cuatro residuos: L161.3 cuadrático cerrado por R161_029 (monotonía falsa), orientado OPEN;
  L161.5–6 tautológico (R161_023, R163_153); mínimo del puerto cerrado por R161_038 / R161_050; L161.4 OPEN sin
  no-go (falta una normalización `V` no circular). Los cuatro viven sobre el radical de un primer contacto
  supuesto, no sobre todo `P_T`. CITED por el memo; lectura parcial de varios memos.

## V. Ronda 12 de la fase 212 (`ROUND_012_A.md`): residuo L161.4

- V1. L161.4 (R161_020) no pasa la puerta: sobre el radical equivale a la meta. La anulación de la fuga
  `(I−P_+)C_log g` fuerza `F = 0` para cualquier peso (Lema A del memo; no rederivado aquí), de modo que la
  cláusula «el primer contacto anula el lado izquierdo» es `ker H_{T*} = {0}`. La versión sobre todo `P_T`
  existe sólo con `M_T = H_T^{−1}Ł`, circular (J3). `E_N^ren` no contiene `Λ`: los dos cuadrados son ciegos a
  `cΛ` y al borrado; lo que se rompe es la igualdad, no un resto con signo. Patrones B3/B9.
- Reapertura: `M_T` o `V` con fórmula propia a partir de `E_N^ren`, la corriente de Euler y los coeficientes de
  Tate, sin `H^{−1}`, que se rompa en `c = 2` en un paso nombrado que use `Σ_{d|n}Λ(d) = log n`.

## W. Ronda 13 de la fase 212 (`ROUND_013_A/B/C.md`): ventana chica y operaciones de combinación

- W1. «Prueba estructural en la ventana de contactos 2, 3, 4» es repetición de 211 `ROUND_003_A` (tangencia de
  codimensión uno en `c*`, sin cuadrado faltante) y `ROUND_021_A` (Prop. 3.2 en `R = 5`: la forma es
  `Q_0 − c𝒦_R` con ambas piezas libres de `Λ`; controles de §2.3). El conjunto de `c` con positividad es un
  intervalo cerrado que contiene `[1 − λ_0/‖𝒦‖, 1 + λ_0/‖𝒦‖]` (PROVED; la forma es afín en `c`). Por tanto
  ninguna prueba está obligada a usar `c = 1` con exactitud, sólo con precisión del orden del margen, y una
  identidad que meramente se rompe en `c ≠ 1` no es una razón del signo.
- W2. Combinar un cuadrado ciego y un objeto que ve el peso por Cauchy–Schwarz, Gram o complemento de Schur:
  los formatos concretos examinados repiten R170_861 (0.3) y R170_841 §4.2. La identidad del residuo de
  proyección y la equivalencia de Schur son válidas, pero no excluyen un Gram con fórmula propia cuya
  identificación con a_Λ se demuestre independientemente. Se corrige el antiguo veto universal: la
  positividad auxiliar puede sobrevivir a un control y fallar sólo la identificación con la forma.
  Construir el bloque suponiendo ya el signo buscado sigue siendo circular.
- W3. Un cuadrado `‖u_0 + u_Λ‖²` es cuadrático en el peso y la forma es afín: una identidad válida para todo
  `c` fuerza la anulación del término cuadrático (PROVED). Una identidad válida sólo para el peso verdadero
  no queda excluida por esto; exige una identidad cuadrática en `Λ` en el canal de cocientes, donde el
  coeficiente en `a/b` coprimos es `Λ(a)Λ(b)/√(ab)` y la diagonal `Σ Λ²/n` diverge, y donde `Λ∗1 = log` no
  actúa (gobierna productos `L S_N`, no cocientes `L^*L`) (PROVED). Choque ya registrado en I2/I5.
- W4. Mapa de catorce operaciones de combinación (`ROUND_013_C.md` §2): once con antecedente y cierre; el
  conmutador de Mourre/virial es el formato de Lyapunov de `ROUND_012_A` Prop. B. Lema T (PROVED en la clase
  declarada y precisada): un certificado transfiere positividad a un control sólo si sobreviven la identidad,
  las hipótesis de signo y el control de todos los términos adicionales. Lema K (PROVED): las dos fuentes
  de convexidad declaradas dan hessiano `≥ 0` cuando sus medidas o pesos son positivos. Esto no excluye
  identificarlas con la forma mediante una identidad específica de Λ que falle en el control. Que (PC) sea la única relación que
  falla en los tres controles a la vez es ARGUED (depende de la completitud de `ROUND_010_A` Lema C).
- Sin objeto escrito y sin cierre de clase: contracción de Birkhoff entre ventanas; funcional convexo con
  fuente de convexidad distinta de las examinadas o identificación aritmética específica aún no construida;
  emparejamiento impar y no lineal en `A_M`; bloque
  positivo no Gram con fuente propia de positividad; identidad cuadrática en `Λ` en el canal de cocientes.

## X. Ronda 14 de la fase 212 (`ROUND_014_A/B/C.md`): canal de cocientes, bloque no Gram, transición entre ventanas

- X1. Identidad cuadrática en el peso en el canal de cocientes: ninguna candidata pasa la puerta. Polarización
  (PROVED): `‖Lw‖² = 2⟨Lw,LB⟩ − ‖LB‖² + ‖L(w−B)‖²` para todo peso, de modo que «lineal en el peso más resto
  no negativo» existe siempre y el resto es ciego. Si `u_0` puede contener `Λ` como función fija, la
  identidad `a_T = ‖u_0 + u_Λ‖²` existe si y sólo si `a_T ≥ 0` (J3). Transporte del canal de productos al de
  cocientes por sumas finitas de traslaciones y `J` libres de peso: excluido por factorización única
  (PROVED para familias finitas y desplazamientos `±2 log r`; ARGUED con `𝓕`, ventanas o familias infinitas);
  clase distinta de R1. Dualidad `TT^*`: núcleo diagonal en `n`, sin canal de productos (PROVED). Cotejo de
  R161_034/035 y de la fase 106 indirecto (por anexos).
- X2. Positividad multiplicativa sobre primos (Schoenberg, producto de Schur, Pick, positividad total):
  repetición de `ROUND_013_C` O10, INV_F_001 (fila C5, Teorema F2), M3. En un semigrupo el parámetro hace de
  `c`; el producto de Schur pasa a potencias enteras de Hadamard. Clase 𝔖 (producto de Schur de factores
  exponenciales por primo, cada uno `⪰ 0`, por un factor arquimediano libre de peso): sigue `⪰ 0` con `2Λ`,
  con borrado y con Beurling (PROVED en puntos finitos). M4 queda PROVED sólo para 𝔖.
- X3. Transición `Φ: P_{T′} → P_T` con `a_{T′} = κ a_T∘Φ + R`: sin objeto. El resto satisface `R ≤ a_{T′}` y
  `κ s² ≤ λ(T′)/λ(T)` si `‖ΦF‖ ≥ s‖F‖` (PROVED); esto restringe el escalón (identidad exacta o pérdida igual
  al cociente de márgenes) pero no es un cierre de clase: lo que falta es un `R` manifiestamente no negativo.
  La ventana base no distingue los controles; el paso que debe romperse en `c = 2` es el certificado de `R`.
  `Φ` basada en `P_T S_N^*`: cae en el conmutador `[P_T, S_N]` de R161_057–065 (ARGUED).
- Sin objeto escrito y sin cierre de clase tras la ronda: transporte de retardos no afín (reindexación que
  depende de la factorización; cotejar antes con el rechazo «(m,n) a (m+n,m−n)»); positividad de Hadamard que
  acople primos distintos usando `m ≈ kn`; factores no exponenciales en el peso; mapas entre ventanas no
  lineales en `F`; funcional convexo con fuente de convexidad distinta de medida/pesos positivos;
  emparejamiento impar y no lineal en `A_M`.

## Y. Ronda 15 de la fase 212 (`ROUND_015_A/B/C/D.md`)

- Y1. Transporte de retardos no afín: repetición. La reindexación `m − kn = h` es 188 `L2_BUILD_030` §1(c); la
  variante de Farey, INV_C_001; sumas de Ramanujan, INV_H_001; gran criba, SPEC_SIGN_OBJECT_008 V3; pesos de
  Selberg, L2. Clase `Σ_n x_n Q_n` con `Q_n ≥ 0` libres de `Λ` y `x_n ≥ 0` afines en `Λ`: la no negatividad
  sólo usa `x_n ≥ 0`, que vale en los tres controles (PROVED, con el Lema T de la ronda 13).
- Y2. Reparto acoplado de dos primos y jerarquía por bloques: repetición de 159 G2_B8_R5 Obs. 4.3; el nivel
  de un bloque es la forma misma (J3). La pareja obstructora no es un problema de marginales (ARGUED).
  Factorización de Smith sobre potencias de primos: bloques por primo más un término de rango uno, libre de
  `Λ` (PROVED).
- Y3. Convexidad con otro punto base: dentro de R5-a/M1. Segunda variación de `log ζ^c` a lo largo de cualquier
  camino: afín en `c`, ambas piezas convexas (PROVED según el memo). Índice de un par de proyecciones, función
  de desplazamiento espectral, Cayley/signo: iguales a `n_−(a_T) − n_−(Arch)` (circular; BARRIER_W_001 W1/W2).
  `det(1 − cK_T)` y su expansión en ciclos: R186_034 y R186_045 §3.2 (W-det). Marginalización de Prékopa:
  `−D² log Z = E[complemento de Schur de D²V] + G`, `G ⪰ 0` ciego (PROVED módulo Brascamp–Lieb CITED).
- Y4. Umbral del reparto por primo de dos posiciones: `T_DIR ∈ (0.697, 0.699)` (NUMÉRICO); el contacto 4 no es
  la causa (falla también sin él). Lema R (PROVED): si `a = q_2 + q_3 ≻ 0`, el rango mínimo de una
  transferencia `X` con `q_2 + X ⪰ 0`, `q_3 − X ⪰ 0` es `ν_−(q_2) + ν_−(q_3)`. El vector del cuadrado faltante
  es `ℓ ∝ a·w` con `w` el fondo de `a w = μ q_3 w` (construcción PROVED; coincidencia con el óptimo
  NUMÉRICO). Sin forma cerrada. La ley «cuadrados faltantes = contactos en la ventana» es falsa en esta clase
  (NUMÉRICO: rango 0, 1, 2, ≤ 4 entre 0.697 y 0.80 con contactos fijos 2, 3, 4).
- Sin objeto escrito y sin cierre: pesos de criba definidos por un problema extremal sobre los valores
  exactos de `Λ`; potencial `V(x,F)` no cuadrático en `x`, convexo sólo para el peso verdadero; el invariante
  `n_miss(T) = min ν_−(q_2) + ν_−(q_3)` como función de `T`.

## Z. Ronda 16 de la fase 212 (`ROUND_016_A/B/C.md`): curvatura, estados, positividad por reflexión

- Z1. Curvatura (Bakry–Émery, Ollivier, Erbar–Maas): repetición de la fase 64 `CURVATURE-computation.md`, 195
  `INV_N_001` (Teorema 3.3) y `R160_M10_R1` (T3, T4). Con tasas con signo: para `L` simétrico con
  `∫Γ = ⟨−Lf,f⟩` y `∫Γ_2 = ‖Lf‖²`, la condición CD(κ,N) integrada equivale a que el espectro de `−L` no toque
  `(0, κN/(N−1))`; es una laguna, compatible con autovalores `≤ 0`, y no da signo (PROVED).
- Z2. Estados KMS sobre álgebras de Hecke / `𝒯(ℕ⋊ℕ^×)`: repetición de 193 `CA_E_000` §E1 y 114_d_116. El
  suavizado de la dinámica evalúa `F̂` en las frecuencias `log n`; la forma usa `c_F` en los retardos `log n`
  (variable dual) (PROVED según el memo). El control `c = 2` se realiza con el anillo `ℤ×ℤ` (peso `2Λ`,
  relaciones mixtas exactas), pero allí la parte arquimediana también se duplica: ningún anillo realiza
  «peso doble con Arch simple». El borrado de una potencia de primo rompe la integralidad (PROVED). Beurling:
  ARGUED.
- Z3. Positividad por reflexión, desigualdades de correlación, dominación gaussiana: repetición de 193
  `CA_A_007` §3 (Lema 1, Teorema 2), 200 `K1_OSG_001`, frente J de la fase 193 (`CA_J_000`–`002`), M3.
- Sin objeto escrito: elementos construidos con el desplazamiento aditivo en lugar de la dinámica; forma
  puntual `Γ̃ ≥ 0` que no venga de tasas no negativas con `∫Γ̃ = a_T +` término ciego.

## AA. Ronda 17 de la fase 212 (`ROUND_017_A.md`): el muro del reparto por primo

- AA1. Corrección de una premisa: el Teorema A de la fase 153 (`R153_001` §1.2) es una identidad de conjugación
  para la forma del falsificador `Ξ_a`, no una descomposición de `a_T`; la positividad en `log 2` proviene de
  un certificado en aritmética de intervalos. El corpus no contiene ninguna prueba por mecanismo de la
  positividad por encima del umbral arquimediano; nada prueba `T_DIR ≥ log 2`.
- AA2. `T_DIR ∈ (0.696, 0.698)` a dos resoluciones, sin acercarse a `log 2` al refinar, e igual sin el término
  `n = 4` (NUMÉRICO). La cadena doble `t, t+log 2, t+2 log 2` ya cabe en `0.694` y el reparto aún alcanza el
  techo: la hipótesis de cadena queda descartada. En `T_DIR` la pareja diagonal `Y_2 = Y_3 = ½e⊗e` deja de ser
  óptima en el dual y la pareja no diagonal nace a segundo orden (PROVED en Galerkin, ARGUED en el continuo).
- AA3. Permitir que el átomo de un contacto se reparta entre las dos piezas según la posición, con fracciones
  no negativas, recupera el techo en `T = 0.70, 0.72, 0.75` (NUMÉRICO; indeciso en `0.80`). Funciona
  disolviendo las etiquetas de primo; la versión bilateral es trivialmente exacta (`q_2 = q_3 = a/2`), patrón
  J3/O3. Lo que hace fallar a DIR es exigir que cada átomo esté entero en una pieza.
- AA4. Para todo reparto, el paso que falla en los controles es la existencia del reparto, que falla sólo
  porque la forma deja de ser `⪰ 0`: caso automático R3-i, no un paso nombrado. Reapertura: fórmula propia y
  explícita del peso unilateral del átomo que se rompa en `c = 2`.

## AB. Ronda 18 de la fase 212 (`ROUND_018_A.md`): mecanismo local para el reparto por primo

Meta local, con el punto (4) del filtro relajado para este caso: una prueba por mecanismo en un `T` sobre el
umbral arquimediano. No se obtuvo; no hay fórmula cerrada para `θ_p`, `W_p` ni prueba de `q_p ⪰ 0`.

- AB1. Identidad de estado fundamental (PROVED): para `φ` real no nula c.t.p.,
  `Q(F) = ∫(Qφ/φ)F² + ¼∬M φ(t)φ(s)(F/φ(t) − F/φ(s))²` en todo `L²(I)`. Un contacto es una tasa de salto
  positiva; su cuadrado lleva el signo de `φ(t)φ(t−log n)`. Una `φ` que cambia de signo a través del contacto
  lo vuelve negativo: la hipótesis de «estado fundamental con cambio de signo» tenía el signo al revés.
- AB2. `a_T(1) ≤ ∫W < 0` para `T ∈ [0.2, 0.75]` con cotas elementales (PROVED según el memo; en `T = 0.65`,
  `a_T(1) ≤ −2.17`). Corolario: ninguna representación «suma de cuadrados más potencial `≥ 0`» válida en todo
  `L²(I)` existe en ese rango, con `φ` de cualquier signo e independientemente del peso. Toda prueba local
  tiene que usar las restricciones de `P_T`. Cubre el hueco de `φ` con cambio de signo que dejaba
  `ROUND_007_A` §2.
- AB3. NUMÉRICO (modelo de Nyström grueso): estado fundamental positivo con las restricciones de `P_T` como
  términos de Lagrange de rango dos: margen `−0.28` en `T = 0.5` y `−0.80` en `T = 0.62`. El fondo de `a_T`
  en `P_T` para `T = 0.62–0.68` es par, con patrón `+ − +` y nodos cerca de `±0.2`, del mismo signo en las dos
  zonas extremas del contacto de 3.
- Sin intentar: desigualdad de tipo Poincaré/Wirtinger sobre `P_T` para el núcleo `K` con constante explícita
  obtenida a mano (el Paper 47 la tiene sólo por certificado).

## AC. Ronda 19 de la fase 212 (`ROUND_019_A.md`): lectura de escala del margen

- AC1. «El resto positivo es la cola de retículo más allá de `N = e^{2T}`»: REFUTADA. El exponente del margen
  es `(e^{−π e^{2T}})²`, la cola gaussiana del término `n = 1` de theta al cuadrado (PROVED, leído de
  R160_M4_R1), no un término de retículo en `k = N`; la cola de primos más allá de `N` entra con signo
  negativo (ARGUED). `ρ_T` no puede ser una cola de retículo con pesos no negativos.
- AC2. Bajo los controles el vector casi nulo `X_T` deja de serlo porque `M` sale del radical: `≈ +1.70` con
  `2Λ`, `≈ −9.56` borrando 2, `≈ +7.70` borrando 3 (NUMÉRICO). La ruptura la fijan los contactos chicos, no
  la cola.
