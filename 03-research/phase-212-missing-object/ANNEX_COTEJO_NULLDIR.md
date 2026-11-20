# Anexo de cotejo — direcciones casi nulas de a_T sobre P_T y ventana en c

Cotejo previo a toda construcción. No se deriva ni se calcula nada nuevo; se localiza lo que el corpus ya
contiene y se informa con etiqueta. Notación de `ROUND_006_WINDOW_SPLIT_NUMERIC.md`: a_T = Arch − Π,
Π(F) = Σ v_n c_F(log n), a_T^{(c)} = Arch − cΠ, Φ_T(c) = fondo de a_T^{(c)} sobre la esfera unidad de P_T.
Rutas relativas a la raíz del repositorio; «211/» = `03-research/phase-211-sign-sandbox/`, «P47» =
`04-papers/47-row-d-dual-certificates/main.tex`, «P48» = `04-papers/48-row-d-route-map/main.tex`, «IDX» =
`05-meta-and-planning/ROUTES-TRIED-INDEX/`.

**Pivote cotejado.** Tomar como objeto las direcciones casi nulas de a_T sobre P_T (el racimo de autovalores
diminutos) y buscar la relación exacta entre Arch y los términos de contacto sobre ese subespacio que hace
que el fondo toque (casi) cero en c = 1 por los dos lados.

**Resultado del cotejo, en una línea.** El pivote es repetición de la candidata C11 de la fase 211 («par casi
nulo y tangencia c* = 1», `211/ROUND_003_A.md`), con sus continuaciones C8, C12, C16, C19, C21, C35, C43 y C51
del mismo ledger; los datos de `ROUND_006` §10.3 reproducen los de esas memos. No se encontró ninguna
subpregunta que carezca de antecedente y a la vez tenga un mecanismo de signo.

Alcance de la lectura. Leídos en primaria (la memo, no el resumen): `211/ROUND_003_A.md` entera;
`211/ROUND_002_D.md` §§6–7; `211/ROUND_002_E.md` (Lemas 1–3, Cor. 4, corrección, §4, paso siguiente);
`211/ROUND_004_A.md` §§4–5; `211/ROUND_007_B.md` §§4.3–4.5; `211/ROUND_021_A.md` §§3.3–3.4 y resultado;
pasajes de `211/ROUND_005_C.md` §5, `ROUND_009_B.md` §3, `ROUND_015_B.md` §4, `ROUND_017_A.md`,
`ROUND_027_A.md`; `211/LEDGER.md` entero; P47 lem:contA, cor:Tarch, lem:degen, prop:wit-sens, rem:wit-sens,
lem:shape-scale, thm:X, rem:X, lem:flowdet, rem:bar-loc, rem:bar-fam; P48 req:spec (R10) y el párrafo de
sensibilidad; `phase-192-exact-identity/PHASE_192_REVIEW_SUMMARY.md`; `phase-162-…/R162_2902_P2_DEGEN.md`
§§2–3; cabeceras y veredictos de `R162_2101`, `R162_504`, `R186_018`, `R186_023`, `R186_025`, `R186_048`,
`R155_044`, `phase-198-parity-split/BB_001_…md`. Sólo por fila de índice (no en primaria): fases 154, 156,
164, 199, 200, 202, 203, 204, 205 en lo que se cita abajo; se dice en cada caso. La búsqueda fue por concepto
(minimizador, h*, g*, fondo, near-null, near-kernel, cluster, ladder, tangencia, pin, calibración, ventana en
c, J_T, Danskin, concavidad, sensibilidad), no exhaustiva. Una búsqueda sin coincidencias no prueba novedad.

---

## 1. Autovalores mínimos de a_T sobre P_T y sus autofunciones

### 1.1 Estructura del fondo

| Qué | Dónde | Enunciado | Etiqueta |
|---|---|---|---|
| Continuidad del fondo | P47 lem:contA (l.621) | T ↦ λ_A(T) es continua en (0,∞); la prueba usa sólo la masa absoluta total de los pesos | PROVED |
| Instante de entrada vacío | `phase-186-toolbox/R186_048_COMPONENT_BIRTH.md` Lema 2.2, 2.4 | 𝔞_{T_n⁺} ≡ 𝔞_{T_n⁻}; el contacto nuevo sólo es visible por collares de anchura 2ε, \|c_F(log n)\| ≤ masa de borde | PROVED |
| Paridad | P47 (párrafo tras prop:finite); `211/ROUND_003_A.md` Prop. 1 | a_T conmuta con J en P_T; λ_A = mín de los fondos par e impar; Φ_T = mín de los Φ por sector | PROVED |
| Simplicidad del fondo | `211/ROUND_003_A.md` §3 final; `211/ROUND_027_A.md` §1 | no hay Perron–Frobenius para a_T sobre P_T (todo F ∈ P_T cambia de signo; Π rompe la preservación de positividad). Simplicidad OPEN; fondo par y simple con razón de sectores 10–250 (0.6 ≤ T ≤ 1) y hueco 200–2000 (T = 0.8, 1.0, 1.2) | OPEN / NUMÉRICO |
| Perron–Frobenius en L²(I_T) | `phase-162-…/R162_504_SECOND_EIGENVALUE.md` Teor. 1–3, §5 | fondo simple y par de la forma sin restricción a P_T; escalera de paridad; el mecanismo de signo con Λ∗1 = log: NO-GO | PROVED (estructura) / NO-GO |
| Nodos | `phase-155-…/R155_044_ROUND6A_NODAL.md` Prop. N1–N2; P47 prop:nodes | todo F ∈ P_T no nulo tiene ≥ 2 cambios de signo; el k-ésimo autovector par de Arch\|P_T tiene k nodos (k ≤ 8, NUMÉRICO); la vía del núcleo PF₂ cerrada para K | PROVED / NUMÉRICO |
| Escalera superexponencial | `211/ROUND_003_A.md` §2.1, §2.3; `211/ROUND_007_B.md` §4.3 | los cuatro autovalores más bajos (dos por sector) decrecen de modo monótono y superexponencial; λ_ev,2 = 2.2·10⁻¹ (0.6), **1.7·10⁻³ (0.7)**, 6.4·10⁻⁷ (0.8), 1.9·10⁻¹¹ (0.9); en ½log5+ε la escalera es 3·10⁻¹², 6·10⁻¹⁰, 3·10⁻⁷, 3·10⁻⁵, 2·10⁻³ | NUMÉRICO |
| Tamaño del racimo | `211/ROUND_005_E.md` Teor. 3.1; `ROUND_006_A.md`; `ROUND_006_C.md` Teor. A–B | conteo de Weyl bilateral PROVED; m_δ(T) ≤ exp(2e^T(1+o(1))) PROVED (genérico en el peine); racimo observado ≈ 0.15e^{4T} (2, 4, 4, 6, 9, 16) NUMÉRICO | PROVED / NUMÉRICO |
| Cota superior del margen | P47 thm:margin, cor:margin1; RULES_AVOID B2 | λ_A(T) ≤ 4·10⁹Te^{−15.449T} para T ≥ 1; limsup λ_A ≤ 0. (La prueba del paper usa datos del otro lado; aquí sólo se cita la cota sobre la forma.) | PROVED |
| Ley bilateral | `211/ROUND_007_D.md` Lema 4.6; LEDGER 211 C20 | la mitad inferior de una ley λ_A = L(T)(1+o(1)) es el objetivo más un margen; ley exponencial simple NO-GO | PROVED / NO-GO |

El valor «1.7·10⁻³» que `ROUND_006` §10.3 da como tercer autovalor en T = 0.70 es el λ_ev,2(0.7) ya tabulado
en `211/ROUND_003_A.md` §2.3.

### 1.2 De dónde sale el casi-núcleo (explicaciones tipo radical, prolato, Sonin)

- `phase-162-…/R162_2101_*.md` §2 (PROVED como estructura; §4 NUMÉRICO sin certificar). La forma extendida a
  toda la recta tiene un radical par de dimensión infinita; las truncaciones a I_T de sus vectores son nulas
  salvo un error doblemente exponencial, y el radical contiene vectores primitivos; de ahí un casi-núcleo par
  de dimensión ≥ 2 con una dirección en P_T. Lema 3: en un contacto primitivo el minimizador cumple Wx = κφ̂ y
  \|κ\| = ‖Wx‖. La hipótesis de una identidad local entre el átomo en log 2 y el término arquimediano o polar:
  **NO-GO**. (La memo usa en §2 un encuadre externo; aquí sólo su contenido sobre la forma.)
- P47 thm:ext-half (l.9913; PROVED dadas cuatro citas): identidad de semirrecta, a_T(Ef) = forma exterior del
  dato fuera de banda. Es la relación exacta entre parte arquimediana y peine sobre las imágenes E: vale sólo
  con Λ∗1 = log y Poisson. `211/ROUND_001_B.md`: no hay vector radical común de 𝒲 y 𝒲^c para c ≠ 1 (PROVED);
  la lectura «fusión» NO-GO.
- `211/ROUND_008_E.md`, `ROUND_009_A.md`, `ROUND_009_B.md` (LEDGER C21–C23). Minimizador en el bloque prolato
  de dimensión 3 a 10⁻⁴; λ_A ≈ κ₈(1−χ₈) y λ_j^ev ≈ κ_j(1−χ_{4j+8}) (NUMÉRICO); mitad superior PROVED
  (λ_A ≤ 4KC₅N⁹(1−χ₈), dada thm:ext-half); regla clase–paridad de Fourier **libre de Λ, no es paso de signo**
  (PROVED, `ROUND_009_B` §3.1); la casi-nulidad de la clase autodual se rompe con todo falsificador; la mitad
  inferior es prob:ext-L, OPEN.
- Fase 199 (IDX README l.466–483; sólo por índice): vector extremal en ½log15, f* = E⁻¹g* autodual de Fourier,
  1.106ψ₀ − 1.822ψ₄ + …; «suelo rugoso = respuesta de primer orden del peine sobre la parte prolata»: NO-GO
  (NUMÉRICO, PROOF_L_SHARP_BB_001).
- Fases 183–186 (IDX `04_PHASES_100-189.md` l.123–130; `phase-186-toolbox/`): cadena de Sonin semilocal PROVED
  para todo S finito, sin signo; invariante ρ*(T) = sup C/Son_S, positividad ⟺ ρ* < 1, 0 en ½log2 y 0.9437 en
  ½log3 con maximizador = h* (`R186_018`, reformulación); alineación de un modo **FALSIFIED** (`R186_023`:
  M(T) no sigue a λ_min, error de 1 a 12 órdenes; un vector con solape 0.96 da cociente de Rayleigh ~3·10⁻³,
  ya por encima de λ_min); fase del peine sobre componentes FALSIFIED (tautológica, `R186_044`).
- IDX `05b_LITERATURE_EXTENSION.md` L106 (CITED, sin arbitraje): ≥ m autovalores en [−δ, δ] con
  δ ≲ λ^{4m+17/2}e^{−πλ²}; registrado como cuantificador NO-GO («un portador debe resolver m autovalores
  agrupados a esa escala»).

### 1.3 Muros que caen sobre funcionales del minimizador

- P47 thm:X (l.8281; PROVED) y rem:X: lo que la positividad en una ventana mayor impone a los contactos
  nuevos es una desigualdad promediada sobre U_{T₀} a resolución π/T, nunca puntual; condición necesaria, y
  el modelo de cuarteto la satisface con fondo negativo (NUMÉRICO).
- P47 lem:flowdet y rem:bar-loc: el coeficiente de cualquier flujo de log det cerca de un fondo pequeño está
  dominado por ⟨A′h*, h*⟩/λ_A, funcional del minimizador; la diferencia con el modelo de cuarteto es una
  desigualdad entre dos funcionales de h*.
- P48 req:spec (R10) (l.552): el objeto no puede ser un funcional del minimizador solo; todo discriminante de
  primer orden es lineal en los pesos a través de c_{F*}(log n) y lo satisfacen modelos explícitos (PROVED a
  primer orden). RULES_AVOID B8 (W-lin, W-det, W-fam, W-pat, W-loc, W-mom) y B9.
- IDX README l.141–146 (SPEC_A): inducción exacta en T por contactos, NO ADMISIBLE; la conjetura residual es
  una propiedad del campo exterior del minimizador, no de Λ.
- **Fase 192** (`phase-192-exact-identity/PHASE_192_REVIEW_SUMMARY.md`): tres identidades exactas sobre el
  minimizador (campo exterior de h*, Mellin/Poisson sobre s_w, función de fase de la ventana). Las tres
  identidades PROVED y las tres **EXCLUDED** como portadoras: invariantes bajo todas las modificaciones del
  peine. El resumen registra sólo dos canales de no linealidad (h*(Λ) por la resolvente; un test construido
  con los coeficientes), «no añade un tercero y no prueba que no exista».
- `phase-198-parity-split/BB_001_…md`: Π = Arch(h*) − λ_A (PROVED, trivial); identidad de Euler–Lagrange al
  cuadrado (CONDITIONAL); **BB3 NO-GO PROVED**: toda identidad polinómica en los desplazamientos obtenida de
  Euler–Lagrange es genérica en el peine. CC_001: hessiana ∂²λ/∂κ_p∂κ_q = −2⟨C_p h*, R_⊥C_q h*⟩ ≼ 0, sin signo
  para el cruce, continua en las posiciones (NO-GO).
- `211/ROUND_007_B.md` §4.3 (**NO-GO de clase**: enunciados sobre valores de las piezas en «el minimizador»).
  (a) PROVED: el reparto depende de la densidad libre de Λ elegida en la contabilidad; (b) NUMÉRICO: sobre el
  tramo de los tres autovectores más bajos la pieza libre de Λ recorre [−0.11, +0.49] (½log5+ε),
  [−0.13, +0.46] (0.9), [−0.15, +0.44] (1.0), con huecos 10⁻¹⁰–10⁻¹⁵; un cambio de 10⁻⁷ en un peso o
  c = 1 ± 10⁻⁷ rota el minimizador dentro de la escalera. La escalera existe también para cΛ, a_P y el
  desplazamiento de Beurling, con fondo negativo: geometría genérica en el peine.

---

## 2. Dependencia en c

### 2.1 Umbral arquimediano

- P47 cor:Tarch (l.2562; PROVED, con verificación por intervalos): 0.58 ≤ T*_{∞,P} ≤ 0.60; el fondo de Arch
  sobre P_T es estrictamente decreciente, positivo antes y negativo después, y < 0 para todo T ≥ 0.60.
  P47 thm:index: n₋(Arch\|P_T) = 0, 1, 2 en (0, T*_ev), (T*_ev, T*_odd), (T*_odd, 0.90], con
  log 2 ≤ T*_odd ≤ 0.81 (PROVED, asistido).
- `05-meta-and-planning/ABCD-CLOSURE-PLAN/PATH-TO-D.md` l.71, 136;
  `phase-155-…/R155_031_CORPUS_SYNTHESIS_PATH_TO_D.md` l.158, 352; `R155_029` l.27: T*_{∞,P} ≤ 0.5958; «por
  debajo los primos son un coste, por encima son necesarios».
- Observación de lectura: `ROUND_006` §10.3 afirma «Arch ⪰ 0 sobre P_T en T = 0.5925». 0.5925 está dentro del
  intervalo [0.58, 0.60] que cor:Tarch no decide; la afirmación es NUMÉRICO (compatible con la cota 0.5958).

### 2.2 Concavidad, derivada en c = 1, representación dual

- P47 lem:degen (l.3294; PROVED): μ_T(v) cóncava y finita en ℝ^{𝒩_T};
  μ_T(v) ≤ μ_T(v⁰) − Σ(v_n − v⁰_n)c_{F*}(log n). No se sabe si el caso degenerado (c_{F*} = 0 en todos los
  contactos) ocurre.
- P47 prop:wit-sens (l.7283; PROVED) y rem:wit-sens: λ_A(T; (1+ε)v) ≤ λ_A − εκ_T, κ_T = Σ v_n c_h(log n) = Π
  sobre el minimizador; si κ_T > 0, (1+ε)Λ viola la positividad para ε > λ_A/κ_T. NUMÉRICO: κ_{log 2} ≈ 0.09,
  un cambio relativo uniforme de ~10⁻⁶ destruye la positividad en T = log 2. P47 lem:shape-scale (l.8641):
  cΛ falla para c grande en todo T > ½log2 y para c pequeño en todo T ≥ 0.60 (PROVED); la versión con
  c ∈ (1−ε, 1+ε) es CONDITIONAL en κ_T ≠ 0, «no se sabe».
- P48 l.404–407: «la concavidad sólo da cotas superiores; las inferiores sólo salen de cuerdas, es decir de
  descomposiciones convexas del peine».
- `phase-162-…/R162_2902_P2_DEGEN.md` §3–4: D1 (V ½-Lipschitz, V → −∞), D2, D3; Danskin
  V′(v±) = −c_{F*_v}(log 2) ∈ [−½, ½] (PROVED); el caso de log 2 OPEN y ciego a Λ.
- Fase 198 BB_001 §2: λ_A(T; cΛ) cóncava en c, Π monótona en c (PROVED; sólo cotas superiores).
- Fase 203 (IDX README l.587–589; por índice): Danskin ∂λ_A/∂a(n) = −2n^{−½}c_{g*}(log n) (PROVED en la clase
  truncada; CONDITIONAL en P_T); Teorema 2.3 NO-GO: la concavidad en el peine sólo da cotas superiores.
  AUDIT_203_001: en ½log15 la pendiente en c = 1 es ≈ −0.063; «la función sube desde negativo, tiene un
  máximo y cae a ≈ 0 en c = 1»; (1+ε)Λ tiene fondo negativo para ε > 8·10⁻⁶⁹.
- **`211/ROUND_002_D.md` Teorema 1 (PROVED).** Rango conjunto de (Π, Arch) sobre la esfera de P_T convexo
  (Toeplitz–Hausdorff); Π toma ambos signos; Φ_T cóncava, → −∞ en ambos extremos;
  max_c Φ_T(c) = Θ_T := inf{Arch(F): Π(F) = 0}; J_T = {c: Φ_T(c) ≥ 0} intervalo cerrado y acotado; el objetivo
  en T ⟺ Θ_T ≥ 0 ∧ 1 ∈ J_T; Θ_T es invariante por c. Cor. 3: λ_A ≥ Θ_T − \|1 − c*_T\|π_T (estimación con
  holgura ≍ e^T). `211/ROUND_002_E.md` Lema 2 (𝒦_T compacto convexo), Lema 3 y **Cor. 4 (PROVED)**: donde
  Θ_T(Λ) > 0 la condición Θ_T ≥ 0 sobrevive modificaciones pequeñas; sólo separa en ventanas de tangencia,
  donde coincide con el objetivo. Corrección: c*_T = 1 ⟺ 0 ∈ rango de Π sobre el autoespacio del fondo.
  Estado en LEDGER 211: C8, PIVOT. RULES_AVOID B10 lo recoge con esa etiqueta.
- `211/ROUND_027_A.md` (C51; NO-GO NUMÉRICO): v_T(Λ) no es el maximizador global de μ_T; el fondo en v_T(Λ)
  es simple y el gradiente (c_{F*}(log n))_n es no nulo en T = 0.8, 1.0, 1.2; max μ_T = 0.047 frente a
  λ_A = 6.2·10⁻¹² (T = 0.8).

### 2.3 La ventana estrecha y bilateral en c: ya registrada

- **`211/ROUND_003_A.md` (C11).** Lema 3 («pin» de Weyl, PROVED): para un par ortonormal de P_T sobre el que Π
  es indefinida (autovalores μ₋ < 0 < μ₊), λ_A ≤ Θ_T ≤ Λ₂ y \|1 − c*_T\| ≤ (Λ₂ − λ_A)/min(\|μ₋\|, μ₊).
  **Lema 4 (rigidez, PROVED):** si a_T\|_S ≤ ε, entonces λ_A(T; cΛ) ≤ ε − \|c − 1\|·\|μ_∓(Π\|_S)\| (μ₋ para
  c > 1, μ₊ para c < 1); si Π\|_S es indefinida, todo c con \|c − 1\| > ε/min(\|μ₋\|, μ₊) da fondo negativo.
  NUMÉRICO: el par que fija la tangencia es el par PAR {e_ev,1, e_ev,2} (no una degeneración par–impar); Π es
  indefinida sobre él desde T ≈ 0.61 (el autovalor menor de M_ev cambia de signo entre 0.600 y 0.625) y
  decrece hasta −0.205 en T = 1; sobre el par impar Π es definida positiva en todo T probado. Cotas del pin:
  2.4·10⁻², 2.0·10⁻⁶, 7·10⁻¹¹, 2·10⁻¹⁴ en log 2, ½log5, 0.9, 1.0 (observado: 1.7·10⁻³, 1.3·10⁻⁷, redondeo).
  Inercia de Π sobre el tramo con autovalores < 10⁻³: (0,2), (1,3), (2,4), (2,7).
  Prop. 2 (PROVED dada Kato–Danskin, CITED): Φ′_±(1) = −max/−mín de Π sobre el autoespacio del fondo; la
  tangencia exacta c* = 1 es una coincidencia de codimensión uno. **Lectura registrada:** el fondo calculado
  es par y simple con Π(e_ev,1) > 0 (0.088, 0.062, 0.046), luego el maximizador exacto cumple c*_T < 1
  estrictamente; lo que se observa es tangencia aproximada.
- `211/ROUND_015_B.md` §4.2 y `ROUND_017_A.md` (C33b, C35; NUMÉRICO con fórmula PROVED de segundo orden):
  b(c) = λ_A + (1−c)P − (1−c)²X + O(\|1−c\|³), P = Π(F_b), X = Σ_g\|Π(F_b, g)\|²/(μ_g − λ_A). Dos umbrales de
  naturaleza distinta: c > 1 muere a primer orden en \|1−c\| ≈ λ_A/Π(F) (5·10⁻²² en T = 1, 10⁻¹⁰ en T = 0.8);
  c < 1 sobrevive el primer orden y muere a segundo orden por el acoplamiento con el peldaño siguiente,
  umbral ≈ Π(F)μ_g/X² (10⁻¹⁸–10⁻¹⁶ en T = 1; 10⁻⁸–10⁻⁶ en T = 0.8).
- **`211/ROUND_021_A.md` (C43; NO-GO con piezas PROVED).** Ventana J_R de la forma de R celdas: intervalo
  cerrado; ventanas de Galerkin son cotas exteriores; J_R → {1} por los dos lados y superexponencialmente
  (NUMÉRICO). **Lema 3.3 (PROVED):** λ₀/‖𝒦‖ ≤ c₊ − 1 ≤ λ₀/K₀ y análogos para c₋. §3.4: «el estrechamiento de
  la ventana no proporciona una cota inferior; es equivalente a la ausencia de una»; el mecanismo sobrevive a
  sistemas de Beurling, luego no es paso de signo. Prop. 3.2: P_w𝔇_R = [M_x, 𝔇_R] si y sólo si w ≡ 1 sobre
  potencias de primos < R: tras usar la identidad «no queda resto», la pregunta es el signo de la forma libre
  de Λ Q₀ − 𝒦_R.
- Fase 200, LEMMA_I3_001 (IDX README l.537; por índice): haz exacto en el gauge radical,
  A(c) = Lᵀ[(1−c)C ⊕ (A_⊥⊥(1) + (1−c)Q/C)]L con L fijo, complemento de Schur afín en c; salto de inercia en
  c = 1; «peine módulo gauge ≽ 0 sobre el casi-núcleo»: FALSO; NO-GO como objeto de signo.
- RULES_AVOID D17 lista «ventanas en c» y «𝒜𝒫 − c𝒞 con c ≠ 1» entre lo que no se relanza
  (`211/ROUND_019_B`, `ROUND_020_A`: márgenes en c de un representante son ℝ o ∅; multiplicador del S-lema
  forzado a 1; C39: positividad 2×2 de peldaños sobrevive c ∈ [0, 3.5]).
- «Control c = 2»: RULES_AVOID M5 (cierre bajo producto de factores, comprobación en c = 2, no encontrada) y
  N3; R3-i (`REVIEW_003.md`): no basta que la identidad deje de valer para cΛ; R3-e: bloques exteriores
  homogéneos en c; L6/R4-f: la inercia no distingue c = 1.

Sobre los valores concretos de `ROUND_006` §10.3 (T = 0.70 y 0.75, N = 30): no hay coincidencia textual de
esas dos filas, pero el fenómeno, su mecanismo (Lema 4 de 003_A, Lema 3.3 de 021_A) y sus tamaños están
registrados en T = log 2, ½log5, 0.8, 0.9, 1.0, 1.2 y ½log15. Los valores nuevos son compatibles con ellos
(en T = 0.70 el fondo en c = 0.999 es mayor que en c = 1, como exige c* < 1; el ancho ~10⁻³ coincide con el
1.7·10⁻³ observado en log 2). La frase «todo certificado exacto en T ≥ 0.70 distingue c = 1 con esa
precisión» es P47 rem:wit-sens y `211/ROUND_004_A` Prop. B.

---

## 3. «Identidad exacta sobre el subespacio casi nulo»: intentos bajo otros nombres

| Intento | Dónde | Qué se construyó | Dónde paró y por qué (registrado) |
|---|---|---|---|
| Desigualdad matricial sobre el par casi nulo | `211/ROUND_003_A.md` §4 | Σ v_n R_n(S) ⪯ Arch_S en 2×2, S = par par más bajo | circular: S depende de Λ; saturada a 18 cifras; (P1)–(P2) «tan fuertes como la positividad que servirían» |
| Planos libres de Λ (autovectores de Arch) | `211/ROUND_004_A.md` Prop. B, §5 | condiciones k×k explícitas en v_n | **NO-GO PROVED**: toda condición con holgura ε_E > 0 sobrevive \|c−1\|‖Π\|_E‖ < ε_E; el complemento de Schur exige precisión de margen; arena doblemente exponencial |
| Familia de respuestas del peine E_T | `211/ROUND_005_C.md` §§2, 5; `ROUND_007_E.md` | reducción exacta PROVED; lema de signo (SL_T), cúbico en v, sin holgura | mecanismos por identidades (Selberg, factores locales, núcleo de Lévy): NO-GO, valen para Beurling y a_P; λ_min(a\|E_T) excede λ_A en 6/13/31 órdenes: el signo vive en el acoplamiento de Schur |
| Presupuesto σ_T + κ − ℛ sobre el minimizador | `211/ROUND_007_B.md` §§3.3–4.3 | identificación con la forma sin polo y ℛ = Π + 𝔢; cúbica de respuesta | NO-GO: partes de grado ±1.4·10⁻³ cancelan a 3·10⁻¹²; valores sobre el minimizador no definidos por debajo de la escalera |
| Neumann del acoplamiento de Schur | `211/ROUND_008_D.md` | desigualdad polinómica finita 𝒫_K(v) ⪰ 0 | NO-GO: grado ∝ log(1/λ_A); grados bajos pares dan signo equivocado |
| Krylov y palabras desde semillas libres de Λ | `211/ROUND_005_A/B/E`, `ROUND_006_B` | álgebra de palabras, cuadrado tipo Widom | NO-GO: familias homogéneas invariantes por cΛ; no capturan el casi-núcleo Π-indefinido por debajo de la dimensión del racimo; Lanczos ciego al racimo |
| Vector de acoplamiento del superviviente; peldaños | `211/ROUND_017_A`, `ROUND_018_B` | forma de Schur partida en arch/peine/Tate; identidad radical de segundo nivel | PIVOT / NO-GO: partes arch y peine cancelan con cuotas ±10²…10³⁸; positividad 2×2 de peldaños genérica en c |
| Reducción de Schur par en log 2 | `phase-155-…/R155_032`, `R155_039`; PATH-TO-D (iii); `R162_2902` Teor. P2 | Prop 3c.1, Teor. 3c.3; W_{log 2} ≻ 0 sobre siete modos pares (certificado) | identidad estructural PROVED sólo para la parte de primos (cadenas de ≤ 4 vértices, espectro cerrado, 0.9009276…), **ciega a Λ**; «no existe identidad para S_even completa más allá del espectro arquimediano» |
| Explicación nodal de la cancelación | `R155_044`; `R162_2902` §2 | cancelación entre n = 2 y n = 3 = interferencia en la cadena P₄ | herramienta; la arena exige ≥ 12 modos (P47 thm:arena); ninguna truncación fija decide |
| Reducción finita (L1)/(L2) | `phase-186-toolbox/R186_025` Teor. A, B, Cor.; P47 thm:coer-schur | λ_A > 0 ⟺ S_{T,k} ≻ 0, dimensión 2k−2 | (L1) PROVED; (L2) OPEN: «es la positividad reescrita en una base explícita», hereda el decaimiento del margen; entrelazado/primer cruce NO-GO (fase 204, por índice) |
| Teorema P, índices negativos | P47 thm:index, thm:parityschur, prop:polarcap, subsec:inertia-excl | n₋ ≤ 5/7/8; capacidad polar | herramienta PROVED sin signo; el conteo de inercia no distingue c = 1 (RULES_AVOID L6) |
| Certificados duales flat-top | fase 154; P47 thm:Z, thm:C; RULES_AVOID C3 | certificados hasta ½log5 (propios) y ½log15 (CITED) | la clase dual es el propio objetivo; formato por ventana (W-fam) |
| Conversa por ventana | fase 156; P47 prop:onewindow, cor:convfail | condición 2×2 de capacidad polar | FALSIFIED en modelos de peine (IDX 04 l.204) |
| Teorema de cola | fase 164 (IDX 04 l.904–909; por índice) | reducción a una condición de cola | PARTIAL; la condición queda como reformulación (IDX 04 l.1029). Las memos usan encuadre externo; no se desarrolla |
| Tabla exterior | fase 202 (IDX README l.579–583; por índice) | forma por clases q = b/a y capas; Lema M | fase cerrada: X1 = partición de la desigualdad; «𝔅_n nunca es multiplicativa» |
| Objeto componente | fase 205 (IDX README l.626–632; por índice) | matriz del peine en senos de Dirichlet; función de Green del polo | esqueleto sin nodo de signo; la reformulación finita «n₋(𝔄_N) = 1» NO-GO como ruta |
| Identidades exactas sobre el minimizador | fase 192; fase 198 BB_001 | véase §1.3 | EXCLUDED / genéricas en el peine |
| Fórmula de variación de λ_A en T | `211/ROUND_008_C`, `ROUND_024_A` | corchete virial; salto −2v_nF*(T_n)² | NO-GO como ruta (reformulación; clase 𝒦_H); CONDITIONAL en regularidad de borde |

---

## 4. Patrones cerrados de `RULES_AVOID.md` bajo los que cae el pivote

- **B9** «El signo queda en un funcional del minimizador (IDX SPEC_A, BARRIER_W; P48 req:spec R10).» El objeto
  propuesto es el autoespacio bajo, función de Λ por la resolvente.
- **B10** «La concavidad en el peine (Danskin) da sólo cotas superiores. Su representación dual
  Θ_T = max_c λ_A(T; cΛ) está PROVED y sólo separa en ventanas de tangencia, donde Θ_T = λ_A: estado PIVOT, no
  terreno abierto.» Es el enunciado literal del fenómeno de `ROUND_006` §10.3.
- **B3** «Reformulación exacta presentada como avance.» La relación exacta sobre S es
  Arch\|_S = Π\|_S + a_T\|_S; «el fondo toca cero en c = 1» es el objetivo restringido a S.
- **B8** (W-fam, W-loc): ley en un rango acotado de ventanas; criterio que se recalcula por ventana.
- **B1** en la variante de identidades: fase 192 y BB3 (genéricas en el peine).
- **D17** «ventanas en c», «planos Λ-libres E_k y todo subespacio fijo finito libre de Λ», «truncación de
  Neumann del acoplamiento de Schur», «captura del signo en E_T», «ceguera de Lanczos», «maximización global
  de μ_T(v)», «signo sólo desde el bloque alto o sólo desde el bajo».
- **D11** «Localización nodal de un testigo negativo».
- **J3** factorizaciones canónicas existen con resto ≥ 0 si y sólo si vale el objetivo; **J6** / R3-e;
  **R3-i**: «no basta señalar que la identidad deja de valer para cΛ; hay que señalar por qué el resto deja
  de ser ≥ 0».
- **L6** conteo de inercia o signatura: no distingue c = 1.
- **G6** muros con nombre: W-Sonin, W-fam, W-loc, thm:X como condición necesaria.
- `OBJECT_SPEC.md` O5 (uniformidad en T; no una familia cuya dimensión se recalcula por ventana), O8 («no es
  un funcional del minimizador»), O4.
- C1: «Sonin, prolatos, semilocal como fuente de signo»; «coercividad, Schur, inercia … como fuente de
  signo»; «defecto/continuación, índice de Morse».

---

## 5. Valoración (separada de los hallazgos)

**(a) ¿Repetición?** Sí. Entrada principal: LEDGER 211 **C11** (`211/ROUND_003_A.md`), cuyo título es el del
pivote. Piezas ya escritas que agotan su enunciado:

1. La relación exacta entre Arch y los contactos sobre el subespacio casi nulo es Arch\|_S = Π\|_S + a_T\|_S
   (003_A §2.1), y su origen es la identidad de semirrecta con el radical (P47 thm:ext-half; `R162_2101` §2;
   021_A Prop. 3.2). Esa identidad caracteriza c = 1 y, usada, no deja resto con signo.
2. Por qué el fondo se vuelve negativo a ambos lados de c = 1: Lema 4 de 003_A (casi-núcleo con Π
   indefinida) y Lema 3.3 de 021_A; ley de dos umbrales de 015_B/017_A.
3. Que esto no da cota inferior: 021_A §3.4(i), B10, P48 l.404–407.
4. Que la versión no circular (planos libres de Λ) es NO-GO: 004_A Prop. B.
5. Que la versión dependiente de Λ es el objetivo a precisión de margen: 005_C, 007_B, 007_E, 008_D.

Precisión sobre la premisa. «Toca (casi) cero exactamente en c = 1 por los dos lados» no es lo que el registro
dice. Lo registrado es: tangencia exacta = coincidencia de codimensión uno (003_A Prop. 2); numéricamente
Π(F*) > 0, luego el máximo de Φ_T está en c* < 1 estricto y Θ_T > λ_A; J_T es un intervalo que contiene a 1
en su interior si λ_A > 0, con c₊ − 1 ≈ λ_A/Π(F*) y 1 − c₋ del tamaño del peldaño siguiente. No hay un
«contacto bilateral exacto» que explicar; hay un intervalo cuyo ancho es el margen leído en la variable c.

Nota de consistencia (ARGUED; no figura escrita en el corpus, no se verificó con segundo lector y no se usa
como hallazgo). Con a_T\|_S entre 0 y ε, Π\|_S está entre Arch\|_S − ε y Arch\|_S, de modo que las direcciones
negativas de Π sobre el casi-núcleo están acotadas por el índice negativo de Arch sobre P_T (P47 thm:index:
0, 1, 2). Esto encaja con la tabla de inercias de 003_A §2.6 y con que el pin sea par desde T ≈ 0.61, justo
tras T*_ev ∈ [0.58, 0.60]. Si es correcta, la bilateralidad es consecuencia del índice arquimediano, que es
libre de Λ, más la casi-nulidad: genérica, sin mecanismo.

**(b) Subpregunta sin antecedente.** Ninguna que tenga a la vez ausencia de antecedente y mecanismo de signo.
Lo que queda sin ejecutar, con su estado:

- (C1)–(C3) de 003_A §4 como teoremas (Π indefinida sobre el par par con μ₋ ≤ −c₀ uniforme; λ_ev,2 → 0
  superexponencialmente; fondo par y simple). OPEN, sólo NUMÉRICO. Son enunciados estructurales cuya propia
  memo califica de tan fuertes como la positividad; probarlos daría c* → 1, no λ_A ≥ 0.
- La relación del umbral del pin (T ≈ 0.61) con T*_ev: no encontrada escrita (véase la nota anterior). Libre
  de Λ en su mitad arquimediana.
- Convergencia en c para T ∈ [0.60, 0.75]: `ROUND_006` §10.3 la declara sin control; es numérica.
- De la ronda 6 de esta fase, sin antecedente textual y fuera del pivote: la dirección ℓ de §10.2
  (solape 0.60–0.62 con el autovector más bajo) y el par obstructor de igual densidad. `REVIEW_006.md` ya los
  registra como «sin objeto».

Una búsqueda sin coincidencias no prueba novedad conceptual; aquí, además, las coincidencias son abundantes.

**(c) Qué tendría que decir el filtro de cuatro puntos** para la única variante que no es literalmente una
entrada cerrada (una identidad sobre el subespacio casi nulo dependiente de Λ, con fórmula propia):

1. *Antecedente más cercano.* `211/ROUND_003_A.md` §4 y Lema 4; `211/ROUND_005_C.md` §5 ((SL_T)); `211/ROUND_021_A.md`
   Prop. 3.2 y Lema 3.3; P47 thm:ext-half; fase 192.
2. *Objeto o afirmación nuevos.* Tendría que escribir S_T sin resolver el problema (no «los autovectores más
   bajos»): una familia explícita con dim S_T creciente (racimo ≈ 0.15e^{4T}), que no sea E(prolatos de la
   clase autodual) ni la familia de respuestas E_T ni un plano libre de Λ, junto con V_T sobre ella. Hoy no
   hay tal objeto; «el casi-núcleo» definido por el espectro es circular (J3).
3. *Por qué evita la dificultad del antecedente.* Tendría que responder a tres motivos registrados: (i) sobre
   S la identidad disponible ya es exacta y no deja resto (021_A §3.4); (ii) el signo no está en a_T\|_S sino
   en el acoplamiento de Schur con S^⊥, que hay que conocer a precisión relativa e^{−15.449T} (004_A §5(c);
   007_E); (iii) toda identidad sobre el minimizador obtenida de la ecuación de Euler–Lagrange o de las
   identidades del peine vale para Beurling y a_P (BB3; 005_C §5.3(iv); fase 192).
4. *Enlace con la positividad global.* Tendría que ser (G) de `OBJECT_SPEC.md` sobre todo P_T y todo T:
   a_T = ‖V_TF‖² + ρ_T. La información bilateral en c no lo da: por 021_A Lema 3.3 el ancho de la ventana es
   λ₀ salvo constantes, y por B10 la concavidad sólo acota por arriba. Haría falta una desigualdad del tipo
   «complemento de Schur de a_T respecto de S_T ⪰ 0 con S_T^⊥ coercivo», uniforme en T, y el punto (5) de
   `OBJECT_SPEC.md` §4: la línea donde el resto deja de ser ≥ 0 para cΛ con \|c − 1\| arbitrariamente pequeño
   y para a_P. Con dim S_T finita por ventana choca además con O5.

**Conclusión del cotejo.** El pivote, tal como está enunciado, no pasa la puerta: es C11 de la fase 211 con
sus cierres posteriores, y cae en B9, B10 y D17. No se autoriza derivación ni cómputo sobre él. Los datos de
`ROUND_006` §10.3 pueden anotarse como reproducción NUMÉRICO, en T = 0.70 y 0.75, de `211/ROUND_003_A` Lema 4
y `211/ROUND_021_A` Lema 3.3. Signo global: OPEN.

## Reservas

- No se ejecutó ningún script ni se recalculó ningún valor.
- Fases 154, 156, 164, 199, 200, 202, 203, 204 y 205: citadas por fila de índice salvo donde se indica
  lectura en primaria. Las memos `211/ROUND_005_C`, `008_D`, `008_E`, `009_A/B`, `015_B`, `017_A`, `018_B`
  se leyeron por pasajes, no enteras.
- `211/ROUND_008_A.md` está truncada (RULES_AVOID §H); no se usó.
- Varias memos anteriores a la fase 211 (R162_2101, R163–R165, fase 199) usan un encuadre externo del
  objetivo; se registró su contenido sobre la forma y nada más.
- El índice resume por fase; las carpetas anteriores a la fase 100 no se abrieron para este cotejo.
