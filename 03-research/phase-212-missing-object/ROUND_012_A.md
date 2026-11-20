# Ronda 12, A: el residuo L161.4 y su paso a todo P_T

Notación del brief común. P_T es el portador primitivo y H_T el operador autoadjunto de la forma a_T sobre P_T.
El radical de primer contacto en T* es ker H_{T*}: PAPF = 0, es decir AF = r = αe^{−t/2} + βe^{t/2} sobre la ventana.

**Resultado.** L161.4 no se conecta con la positividad global por un camino propio. El cuadrado de fuga L^sc es
estrictamente positivo sobre todo F ≠ 0, y lo es para cualquier peso de la corriente: cΛ, borrado de una potencia
de primo, Λ exacto (Lema A). Por eso la cláusula «el primer contacto anula el miembro izquierdo» equivale, con
la cadena de primer contacto, a ker H_{T*} = {0}, que es el objetivo mismo. La versión sobre todo P_T existe
(Prop. B). Es un certificado de núcleo de tipo Lyapunov, L^sc(F) = Re⟨H_T F, M_T F⟩, y en ella L^sc puede
cambiarse por cualquier forma definida positiva (por ejemplo ‖F‖²). Las dos normalizaciones canónicas que dicta el
retículo recaen en R161_052 y R161_056 (tangente con orientación equivocada). Veredicto: NO-GO de selección. Es una
reformulación (B3, B9), y el cuadrado tiene un signo ciego al peso. Queda la operación de reapertura del §4.

## 0. Paso 0, en primaria

He leído completos R161_015, 016, 017, 018, 019, 020, 024, 052 y 075. De R161_003 leí §§0–1, de R161_040 §§2–6, de
R161_056 §§1 y 4, y de R161_073 y R161_081 los encabezados. Leí también ROUND_010_A, ROUND_011_A, RULES_AVOID
B, E, J, K, L, T y U, y ANNEX_161_FILES_1 §(c).

**Búsqueda.** Busqué «L161.4», «R161_020», «leakage square» y «cuadrado de fuga» en todo el corpus, en el índice y
en la grilla. Las citas que siguen son todas las que hay.
- R161_021, 024, 030, 034, 039, 049, 052.
- README 161 y R161_099 §269.
- Índice 04 G1C-R161_020-021, con estado PARTIAL.
- Índice README l.2454: «cuadrados correctos sin identidad con el defecto de PC».
- Grilla, celda 1C: residuo vivo X_T, no realizado.
- ANNEX_161_FILES_1 y _2, LEDGER l.45, RULES_AVOID K1 y U2, ROUND_011_A.

«C_log», «E_N^ren» y «graph limit» aparecen en unos cincuenta archivos (fases 106, 114, 116, 161 y 162). Los
pertinentes son los que se citan abajo.

### 0.1 Objetos

- **C_log.** Coseno logarítmico normalizado: autoadjunto, unitario e involutivo. En Mellin,
  M(C_log u)(s) = χ(s)M(u)(1−s) (R161_017 (1.6)).
- **Puerto producto g.** Es la transformada inversa de frontera de
  G_+^can(s) = −ζ'(s)K_F(s−½) − ζ(s)Q_+(s−½) − c_+(F)ζ(s)Θ_T(s), con Θ_T(s) = e^{−T(s−1)}/s (R161_015 (1.1)–(1.3)).
  - Q_+ es la transformada de la prehistoria compacta q_+ de la corriente de Euler derecha B_+F.
  - Por tanto G_+ = ζ·(transformada de la cola exterior h_+ de B_+F). g está soportado en [T,∞) y es lineal en el peso.
- **P_+.** Multiplicación por 1_{[T,∞)}. H_T^± son las proyecciones de Hardy correspondientes.
- **E_N^ren.** Es S_N^ren𝓕 − JS_N^ren, con S_N^ren = S_N − C_N(D). S_N tiene pesos unidad n^{−1/2} y C_N(D) es el
  continuo polar de Euler–Maclaurin (R161_003). En Mellin e_N = A_N u − B_N, con A_N = Z_N(s) y B_N = Z_N(1−s)
  (R161_052 (1.1)).
- **Radical.** El vector de primer contacto supuesto F ∈ ker H_{T*}, con paridad ε.
- **V_{M,N,T}.** Una normalización por definir, lineal en F, heredada del producto zeta y de los términos de Tate
  cruzados. No puede definirse a partir de L^sc.

### 0.2 Lo PROVED

- Rigidez de compresión unitaria (R161_020 Lema 1.1).
- L^sc(g) = ‖(I−P_+)C_log g‖² = ‖g‖² − ‖P_+C_log g‖² (R161_020 (0.2)), y su forma de Hardy (4.3).
- Defecto exacto G_+ + χG_− = ζW_ε (R161_017 Teor. 2.1), con restricción interior W_ε^∨ = r_ε (R161_017 (3.3)).
- Red de polos Gamma: W^0 holomorfo en s = 3, 5, 7, … implica F = 0 (R161_019, R161_024 Teor. 1.1).
- Equivalencia de R161_024 §2: la removibilidad equivale a que el puerto reflejado se anule en los ceros triviales.
- Pendiente de norma N_T'(0+) = −2∫(t−T)|g|² (R161_015 Teor. 3.1).
- Colligación unitaria finita θ_N = A_N u/B_N, con |θ_N| = 1 y defecto de Toeplitz igual a fuga exacta
  (R161_052 §§1–2).

### 0.3 Enunciado abierto

lim ‖H_T^− E_N^ren V_{M,N,T}F‖² = L^sc_T(F) (R161_020 (5.2)), y además la identidad finita de primer contacto anula
el miembro izquierdo. La versión finita es R161_052 (5.1): ‖T_N x‖² − ‖x‖² → 0, con x = x_{M,N,T}(F) sacado de
(PC-ren).

### 0.4 Por qué se detuvo

E_N^ren F → 0 sobre datos de Schwartz (R161_003). En consecuencia, todo límite fuerte acotado de mapas lineales
construidos con E_N^ren tiene acción nula y mata ambos lados (R161_016 §3, PROVED en esa clase). Reescalar exigiría
una cota de grafo uniforme nueva más la tipificación inversa, y nada de eso sale de (PC-ren). Además, la tangente
unitaria de R161_052 lleva la media U+V y no la diferencia U−V (R161_056).

### 0.5 Exclusión de R161_018 y su auditoría

R161_018 afirma ZA_∞ = [Z,D_Γ] = 0, de donde todo límite lineal de (PC-ren) sería tautológico (Teor. 2.1, Cor. 5.1).

R161_075 muestra que esa identificación no está establecida. Producto en L², producto distribucional e identidad
meromorfa son tres cosas distintas: en L², ZAf = 0 implicaría Af = 0, y en el sentido distribucional
z·δ_γ = 0. La exclusión queda sin probar. No se usa abajo.

## 1. Filtro de cuatro puntos

1. **Antecedente más próximo.** R161_020 §5 y R161_052 §5 (la misma meta en forma finita), además de R161_024 §2.
   Para el paso a todo P_T: R161_073 (inverso estabilizado sobre ker H) y R161_081 (extensión de Q fuera del
   radical; falla en autovectores con λ ≥ 0).
2. **Lo nuevo.** (i) El Lema A: L^sc es definida positiva y su núcleo es trivial para todo peso de la corriente.
   (ii) La Prop. B: la forma exacta que tendría L161.4 sobre todo P_T.
   Ambas cosas son análisis de la meta. Ninguna es un mecanismo de signo.
3. **Por qué evitaría la dificultad.** No la evita. El Lema A muestra que el único eslabón abierto es justamente
   ker H_{T*} = {0}.
4. **Enlace con la positividad global.** Sería la cadena de primer contacto del §2(a). Su eslabón abierto es el
   objetivo mismo.

Mi propio cotejo hostil detecta repetición (B3/B9). No hago ninguna derivación larga más allá de los lemas
estructurales que lo prueban.

## 2. Paso 1

### (a) Qué daría L161.4 si fuera cierto

La cadena es la siguiente.

1. λ_A(T) > 0 para T pequeño. CITED: certificados de Paper 47.
2. T ↦ λ_A(T) es continua (P47 lem:contA) y decreciente; H_T tiene resolvente compacta, así que λ_A se alcanza
   (P47, párrafo previo a lem:contA). CITED.
3. Si a_T toma un valor negativo para algún T, existen T* y F* ≠ 0 con H_{T*}F* = 0. PROVED a partir de 1 y 2.
4. La reflexión t ↦ −t conserva W, K y P_T, así que ker H_{T*} se descompone por paridad y se puede tomar F* con
   paridad ε. PROVED. No hace falta simplicidad.
5. L161.4 (identidad más anulación en el radical) da L^sc(F*) = 0. OPEN: es la meta.
6. L^sc(F*) = 0 implica F* = 0, sin usar el signo σ. Es el Lema A, abajo: PROVED.
7. Contradicción, y por tanto a_T ≥ 0 sobre P_T para todo T.

**Lema A (PROVED).** Sea F ∈ L²(I) con puerto g ∈ L² construido con cualquier sucesión de pesos de la corriente
(Λ, cΛ, o Λ con una potencia de primo borrada), manteniendo el multiplicador ζ de pesos unidad. Si
(I−P_+)C_log g = 0, entonces F = 0.

*Prueba.*
1. Si C_log g está soportado en [T,∞), su transformada H(s) es holomorfa de clase de Hardy en Re s > ½
   (Paley–Wiener, con la convención de R161_015 (2.2)).
2. Sobre la recta, sus valores de frontera coinciden a.e. con M(s) = χ(s)G^can(1−s) (R161_017 (1.6)).
3. M es holomorfa en una banda alrededor de la recta, porque los únicos polos de G^can están en s = 0 y s = 1.
4. Entonces H − M tiene límite no tangencial 0 a.e. en un lado de una banda. Por el teorema de unicidad de
   Lusin–Privalov, H ≡ M en la banda y, por continuación, en Re s > ½.
5. χ tiene polos simples con residuo no nulo en s_m = 2m+1, m ≥ 1. Luego G^can(1−s_m) = G^can(−2m) = 0.
6. En −2m se tiene ζ(−2m) = 0 (CITED: cero trivial simple, con ζ'(−2m) ≠ 0), mientras Q_+ es entera y Θ_T es
   finita. Por tanto G^can(−2m) = −ζ'(−2m)K_F(−2m−½), y queda ∫F(t)e^{(2m+½)t}dt = 0 para todo m ≥ 1.
7. El cambio x = e^{2t} y el argumento de completitud de R161_019 Teor. 3.1 (potencias x^m con m ≥ 1 sobre un
   intervalo compacto separado de 0) dan F = 0. ∎

El peso de la corriente sólo entra en Q_+ y en el residuo c_+. Los dos aparecen multiplicados por ζ(−2m) = 0.

**Consecuencias.**
- L^sc(F) > 0 para todo F ≠ 0, para Λ, para 2Λ y para el borrado. PROVED.
- El eslabón 5 equivale exactamente a que ker H_{T*} = {0}: L^sc(F*) = 0 es imposible para F* ≠ 0. La cláusula
  «el primer contacto anula el miembro izquierdo» es, por tanto, la afirmación de que no hay primer contacto.
- La cadena 1–4, 6–7 está PROVED o CITED, y todo el peso recae en el eslabón 5. Ese eslabón es el objetivo (B9:
  el signo queda en una afirmación sobre el minimizador). Me detengo, como pide el encargo.
- Ni σ ni la compresión de R161_020 (3.5) son necesarios. Basta que la fuga sea nula, como ya observaba
  R161_024 §2.

### (b) Enunciado fuera del radical

**Proposición B (PROVED).** Para cada T las afirmaciones (i) y (ii) son equivalentes. En (ii), Ł_T es cualquier
forma acotada definida positiva e inyectiva sobre P_T, por ejemplo L^sc (si es acotada en el dominio) o ‖·‖².
- (i) ker H_T = {0}.
- (ii) Existe un operador M_T, con dom H_T ⊂ dom M_T, tal que Ł_T(F) = Re⟨H_T F, M_T F⟩ para todo F ∈ dom H_T.

*Prueba.*
- De (ii) a (i): si H_T F = 0, entonces Ł_T(F) = 0 y F = 0.
- De (i) a (ii): con resolvente compacta y núcleo trivial, H_T^{−1} existe y es acotado. Basta tomar
  M_T = H_T^{−1}Ł_T. ∎

Así pues, el candidato es «L^sc_T(F) = lim‖H_T^−E_N^ren V F‖² + Re⟨H_T F, M_T F⟩ sobre todo P_T», con un término
extra que se anula en el radical. Existe en esa forma, y sólo en ella: cualquier término extra que se anule
exactamente en ker H_T es una función de H_T F.

Combinado con la cadena (a), que se aplica a todo T a la vez, da a_T ≥ 0 para todo T. Pero no añade mecanismo, por
tres razones.
1. La única solución general, M_T = H_T^{−1}Ł_T, invierte la forma. Es circular en el sentido de J3.
2. Por el Lema A, L^sc no tiene ningún papel privilegiado frente a ‖F‖². Elegir el cuadrado de fuga no aporta nada
   mientras M_T no tenga fórmula propia.
3. En dimensión finita, la identidad 2Ł = HM + M*H > 0 da In(H) = In(M) (Ostrowski–Schneider; CITED). La
   obligación de signo pasa al espectro de M. Esto entra en L6 (inercia) y en B3 (reformulación).

### (c) La normalización V

**Libertad.** V es una familia lineal V_{M,N,T}: P_T → L²(ℝ). Puede depender del corte de primos M, del corte
reticular N y de T, a través de S_N, de C_N(D), de B_± y de los coeficientes de Tate.

**No circularidad.** Quedan prohibidos H_T^{−1}, el minimizador, L^sc y cualquier raíz o factorización de la forma
(J3). La identidad tendría que probarse después de escribir V.

**Elecciones canónicas del retículo.**

1. *Renormalización polar a densidad mitad (R161_003).* Ya está dentro de S_N^ren y es justamente la que hace
   E_N^ren → 0. No deja libertad.

2. *División por la orientación opuesta (R161_052).* e_N = B_N(θ_N − 1), con θ_N unimodular. Es la única
   normalización dictada sólo por el retículo que deja un objeto de orden uno.
   - Como e_N → 0 y B_N → ζ(1−s) donde no se anula, se tiene θ_N → 1 en medida, y por convergencia dominada
     M_{θ_N} → I fuertemente. ARGUED: el paso «B_N → ζ(1−s) en medida» no está verificado en primaria.
   - Por tanto ‖(I−P)M_{θ_N}x‖ → 0 para x fijo. Para que el límite sobreviva, x_N tiene que moverse.
   - El reescalado por la tasa lleva a la tangente, es decir, a la corriente de fase (R161_052 §3), y esa
     corriente lleva U+V, no U−V (R161_056, PROVED allí).
   - Esta elección recae, entonces, en una tangente ya retirada.

3. *Reescalado escalar λ_N V con λ_N → ∞.* La tasa de E_N^ren V F → 0 la fija la regularidad de 𝓕VF en el extremo
   superior n ≈ N (Euler–Maclaurin) y depende de F.
   - Un límite finito y no nulo para todo F de un subespacio denso exigiría una tasa uniforme, es decir, un
     término de orden fijo. Ese término es otra vez el jet de la opción 2.
   - ARGUED, no PROVED: no tengo la prueba de que ningún λ_N dé un límite no trivial.

**Conclusión de (c).** Ninguna elección canónica escrita deja ambos lados finitos y no nulos con la orientación
correcta. Las que existen están registradas (R161_052, R161_056, R161_016 §3). ARGUED, con las piezas citadas
PROVED en sus memos.

### (d) Controles

- **Lado izquierdo.** E_N^ren no contiene Λ: sólo el retículo y n^{−1/2}. Así lo dicen el Lema 2 de ROUND_011_A
  y el canal (β) de ROUND_010_A. Λ sólo podría entrar por V.
- **Lado derecho.** g es lineal en el peso, así que L^sc se multiplica por c². Pero su positividad definida es
  ciega al peso (Lema A).

**cΛ con c = 2.** L^sc_2 = 4L^sc es definida positiva. Además, el enlace interior (R161_017 (3.3)) cambia: con
corriente 2B_± y una forma cuyo primer contacto es D_ΓF − 2(B_++B_−)F = r, la restricción interior de W pasa a
ser r + D_ΓF·(algo no nulo) en lugar de r. Así lo indica la cuenta de R161_017 (2.2) con c: queda (c−1)d_ΓK_F.
ARGUED: la normalización exacta de D_Γ frente a Arch no está recalculada.

Si existe T con λ_A(T; 2Λ) < 0 (batería E, CITED), hay un vector radical F_2 ≠ 0 con L^sc_2(F_2) > 0. Entonces
ninguna identidad de la Prop. B, con ningún M, puede valer para c = 2 en ese T. PROVED, condicionado a esa cita.

¿Qué término nombrado pierde el signo? Ninguno: los dos cuadrados siguen ≥ 0. Lo que falla es la igualdad (la
cláusula de anulación). Por la regla R3-i esto es lo automático. No hay resto con signo que deje de ser ≥ 0,
porque el enunciado no tiene resto firmado.

**Borrado de una potencia de primo.** Mismo análisis: L^sc sigue siendo definida positiva (Lema A), y la ruptura,
si existe primer contacto, está otra vez en la igualdad.

**Beurling.** No hay multiplicador ζ con ceros triviales ni ecuación funcional. g y C_log g no quedan definidos de
la misma manera, y el Lema A no se aplica. El enunciado no se formula: queda indefinido, no falsado.

**Conclusión de (d).** La parte con signo del enunciado (los dos cuadrados y la positividad estricta de L^sc) es
ciega a c y al borrado. Todo el contenido discriminante está en una igualdad cuyo único realizador conocido es
H_T^{−1}. Por el criterio del Lema 2 de la ronda 11, extendido de «libre de Λ» a «positividad invariante bajo los
controles», el enunciado es ciego y se rechaza como mecanismo de signo.

## 3. Paso 2: veredicto

L161.4 no se conecta con la positividad global por ninguna vía distinta de la cadena de primer contacto, y en esa
cadena su eslabón abierto es exactamente ker H_{T*} = {0} (Lema A). Su versión sobre todo P_T es la Prop. B: un
certificado de núcleo de tipo Lyapunov, que equivale a la inyectividad de H_T y cuya solución general es
M = H^{−1}Ł (J3).

**Clase que lo cierra.** «Identidades cuadrado = cuadrado con anulación en el radical, donde la positividad
estricta de los cuadrados es invariante bajo cΛ y el borrado.» Es una reformulación (B3) con el signo en el
minimizador (B9). Las normalizaciones canónicas recaen en R161_052 y R161_056.

## 4. Operación que lo reabriría

Hace falta un operador M_T (o una V) con fórmula propia, construido con E_N^ren, la corriente de Euler y los
coeficientes de Tate, sin H_T^{−1}. Para él habría que probar después la identidad L^sc = lim‖H^−E V F‖² +
Re⟨H_T F, M_T F⟩. Además, tiene que mostrarse por qué falla en c = 2, señalando la línea de su construcción que usa
Σ_{d|n}Λ(d) = log n y no sólo la linealidad en el peso.

**Primer caso.** Cámara 0.8 < T < ½log5, contactos 2, 3 y 4, con Z_{T,−}^{−1} = I − K + K² (R161_005 §4). Ahí M_T
sería una matriz explícita sobre los canales 2, 3, 4, más la cabeza Gamma. R161_016 §5 advierte que eso sólo
controla el primer collar.

**Falsificador.** c = 2 con δ = log 2 en k = 2 (R161_001 Teor. 4.1). Sin esa fórmula no hay candidata.

## Afirmaciones y etiquetas

1. Objetos y estados del Paso 0, según R161_015–020, 024, 052, 056 y 075: CITED.
2. La exclusión de R161_018 no está establecida (R161_075): CITED. No se usa.
3. Lema A: fuga nula implica F = 0, para todo peso de la corriente, sin σ: PROVED (usa el CITED ζ'(−2m) ≠ 0,
   Lusin–Privalov y R161_019 Teor. 3.1).
4. L^sc es definida positiva sobre P_T para Λ, 2Λ y el borrado: PROVED (corolario de 3).
5. Cadena de primer contacto, eslabones 1–2: CITED (P47 lem:contA, resolvente compacta, certificados).
   Eslabones 3–4 y 6: PROVED. Eslabón 5 (L161.4): OPEN, y equivale al objetivo: PROVED, por 3.
6. No hacen falta ni σ ni la compresión (3.5) de R161_020: PROVED (por 3; ya implícito en R161_024 §2).
7. Prop. B (versión sobre todo P_T ⇔ ker H_T = {0}; solución general H^{−1}Ł): PROVED.
8. Inercia: 2Ł = HM + M*H > 0 da In H = In M en dimensión finita: CITED (Ostrowski–Schneider).
9. θ_N → 1 en medida y M_{θ_N} → I fuertemente: ARGUED.
10. Las normalizaciones canónicas recaen en R161_052/056: ARGUED (las piezas citadas son PROVED).
11. Ningún reescalado escalar da un límite no trivial uniforme: ARGUED.
12. La interior de W bajo cΛ recibe un término proporcional a (c−1)d_ΓK_F: ARGUED (normalización no recalculada).
13. Bajo c = 2 la Prop. B falla para todo M si hay primer contacto: PROVED, condicionado a la batería E (CITED).
14. Positividad de los cuadrados ciega a c y al borrado; enunciado ciego como mecanismo de signo: PROVED (por 3)
    / NO-GO de selección.
15. Beurling: enunciado indefinido: ARGUED.
16. Veredicto: L161.4 no pasa la puerta. Es una reformulación con el signo en el radical (B3, B9): NO-GO de
    selección. Reapertura según el §4: OPEN.
17. Signo global de a_T: OPEN.
