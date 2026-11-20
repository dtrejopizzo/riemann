# Ronda 5, semilla G4: inducción que alarga la ventana con la identidad de divisores en el paso

Notación de `../phase-211-sign-sandbox/STATEMENT_001.md`. T_n := ½ log n. Para un vector de pesos real
v = (v_n) sumable en cada ventana, a_T^{(v)} y λ_A(T; v) son la forma y el fondo con ese peine; v^{(n,x)}
es v con la coordenada n sustituida por x. Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN /
NO-GO / NUMÉRICO.

## 0. Cotejo (se hace primero; manda sobre el resto)

**(1) Antecedente más cercano, leído en primaria.**

- `phase-162-row-d-first-contact-closure/R162_802_T_EVOLUTION.md` §4 punto 4 y §5. Ya plantea la primera
  integral de Riccati de Kreĭn–Bellman–Siegert para operadores de convolución truncados (la ventana como
  flujo en T) y concluye, en su metaenunciado, que Λ∗1 = log es una identidad de convolución sobre los
  tests que dentro del flujo actúa como un desplazamiento de ventana; por tanto sólo produce relaciones
  entre f(T) y f(T + ½ log m) lineales en el peso, y «una cantidad monótona que prohíba el contacto tendría
  que ser no lineal en el peso en las trazas de borde del encendido; no se identifica ninguna». Es
  exactamente la semilla G4 (identidad de divisores en el paso inductivo, dato de borde, Riccati).
- `phase-162-row-d-first-contact-closure/R162_2701_TATE_CANONICAL_SYSTEM.md` §§0–1: el sistema canónico
  2×2 de transferencia por primos; cada factor es un boost conjugado por propagación libre, J-unitario
  para todo valor del coeficiente de reflexión, y el sistema no detecta ningún falsificador (borrado,
  pesos atómicos arbitrarios, Beurling, Λχ₂). Es el «dato de puerto» con actualización exacta por cruce.
- `phase-197-barrier-theorem/BARRIER_W_001_…_NO_GO.md` §§1–6 (leído entero): toda invariante de la clase
  𝒮 (extensión por cero, concavidad en el peine, continuidad en T, invisibilidad de la entrada U0,
  paridad, resolvente compacta) vale para a_P, truncaciones, cΛ, O_6 y Beurling; el único dato que lee Λ
  en un cruce es el apareamiento de Hellmann–Feynman con el minimizador.
- `phase-211-sign-sandbox/ROUND_008_C.md` Prop. 2.3 y Prop. 5 (contactos entrantes aportan 0 a todo
  orden en el marco de extensión por cero; Grönwall en T = (★) más una tasa) y
  `phase-165-critical-interlacing/R165_202_NODE_FLOW.md` fila 1.4 (fórmula virial de variación).
- `ROUND_001_B.md` / LEDGER K2 (parámetros de Schur del problema de extensión desde Λ exacta) y
  `REVIEW_003.md` / `RULES_AVOID.md` J8 (Riccati/Darboux con el peine como superpotencial, fase 70).

**(2) Objeto o afirmación nuevos.** No logré escribir un invariante I_T con actualización Φ_n que cumpla
(a)–(c) de la semilla. Lo único nuevo son tres lemas cortos (§2) que explican por qué la exigencia (a)
—«Φ_n conserva la positividad cuando, y sólo cuando, el peso entrante es el dictado por los divisores»—
no puede satisfacerse en el instante del cruce por ninguna invariante cuyo signo determine λ_A, y por qué
la regla «el peso nuevo está determinado por los anteriores» no distingue Λ de ningún otro peso.

**(3) Por qué evitaría la dificultad del antecedente.** No la evita: los lemas de §2 confirman y precisan
el diagnóstico de R162_802 §5 y de BARRIER_W_001 §6; no aportan la cantidad no lineal en el peso que
ambos piden.

**(4) Identidad que conectaría con la positividad global.** Ninguna nueva. La reformulación por intervalos
admisibles de §2 (Lema 2) es una reescritura coordenada a coordenada del conjunto convexo K_T de la fase
197 (W2); B3 del índice: objetivo válido, no avance.

**Veredicto del cotejo: repetición** (R162_802 §§4–5 para el flujo de Riccati y el uso de Λ∗1 = log en el
flujo; R162_2701 para el dato de puerto por cruce; BARRIER_W_001 para la inducción en la ventana). Por la
regla 3 del brief la memo debería terminar aquí; se añaden sólo los tres lemas de §2 porque son cortos,
completos y delimitan qué parte de la semilla es imposible tal como se enunció.

## 1. Objeto

No hay objeto. Intenté tres invariantes; los tres caen en antecedentes:

- I_T = (a_T, P_T) con la regla de extensión por cero: es 𝒮 (BARRIER_W_001 §1).
- I_T = matriz de transferencia de Kreĭn de la ventana (o el resolvente de borde Γ_T(±T, ±T), dato de
  Dirichlet-a-Neumann de la ventana) con la corrección polar de rango dos de las condiciones de Tate: es
  R162_802 §4 punto 4 y R162_2701. Su ecuación de Bellman ∂_T Γ = −γ_T γ_T* tiene forzante de signo fijo
  para **todo** núcleo; el peso entra sólo linealmente en la ecuación integral de γ_T, y la pérdida de
  positividad no es salida de un cono sino explosión de la solución (anulación de un determinante:
  W-det, 𝒦_W). ARGUED aquí; los enunciados están en esos archivos.
- I_T = intervalo admisible de cada coordenada del peine dados los anteriores (§2, Lema 2): reescritura de
  K_T.

## 2. Tres lemas sobre la semilla (sin signo)

**Lema 1 (neutralidad del cruce; PROVED relativo a la continuidad en T, CITED P47 lem:contA, BARRIER_W_001
(S3)).** Sea I_T cualquier invariante tal que «I_T es positivo» ⟺ λ_A(T; v) ≥ 0, para todo T y todo v en
una clase que contenga v^{(n,x)} para x en un intervalo. Entonces la positividad de I_{T_n+} es la misma
para todos esos x; en particular ninguna regla Φ_n puede conservar la positividad «sólo cuando» x es el
valor dictado por los divisores.

*Demostración.* Para F ∈ L²(I_{T_n}), c_F es continua con soporte en [−2T_n, 2T_n] y c_F(±2T_n) = 0, luego
el término −x Re c_F(log n) es nulo y λ_A(T_n; v^{(n,x)}) no depende de x. Por la continuidad de
T ↦ λ_A(T; v^{(n,x)}) (lem:contA usa sólo la sumabilidad de los pesos, BARRIER_W_001 (S3)), el signo de
λ_A justo después de T_n es el de λ_A(T_n), igual para todo x, salvo en el caso de borde λ_A(T_n) = 0;
y en ese caso el módulo U2 (v_n C_T / log(1/2η), CITED en BARRIER_W_001 (S3)) es el mismo orden para todo
x ≥ 0. ∎

Lectura. La información del peso entrante no se decide en el cruce sino a lo largo de [T_n, ∞): el
«forzante» −x Re c_F(log n) sólo ve funciones con masa a distancia ≥ log n, y crece con el collar. Un Φ_n
puntual no puede llevar signo; el paso inductivo tiene que incluir la evolución arquimediana posterior, y
entonces deja de ser una función del peso entrante solo.

**Lema 2 (intervalo admisible; PROVED).** Para T y v fijos sea S_n(T) := {x ∈ ℝ : λ_A(T; v^{(n,x)}) ≥ 0}.
Entonces S_n(T) es un intervalo cerrado, y si λ_A(T; v) > 0 contiene [v_n − λ_A(T; v), v_n + λ_A(T; v)].

*Demostración.* x ↦ a_T^{(v^{(n,x)})}(F) es afín para cada F, luego x ↦ λ_A(T; v^{(n,x)}) es un ínfimo de
funciones afines: cóncava y semicontinua superior; su conjunto de superniveles {≥ 0} es un intervalo
cerrado. Como |Re c_F(log n)| ≤ ‖F‖² = 1, λ_A(T; v^{(n,x)}) ≥ λ_A(T; v) − |x − v_n|. ∎

Consecuencia. En toda ventana con λ_A(T) > 0 (en particular en todo T ≤ ½ log 5) la parte «sólo cuando»
de (a) es falsa: los pesos entrantes x con |x − v_n(Λ)| < λ_A(T) conservan la positividad. Coincide con
R4-f y A1 (el veredicto no distingue c cerca de 1). La inducción por intervalos se escribe: (★) ⟺ para
todo n, v_n(Λ) ∈ ⋂_{T ≥ T_n} S_n(T) con las demás coordenadas en Λ; es una reformulación (B3).

**Lema 3 (la regla de divisores no restringe el peso; PROVED).** Para todo peso a: ℕ_{≥2} → ℝ, con
L_a := a ∗ 1 (a(1) := 0), vale a(n) = L_a(n) − Σ_{d|n, d<n} a(d). Luego «el peso nuevo está determinado
por los pesos en los divisores propios» es cierto para todo a con su propio L_a; la información específica
es L_Λ = log, es decir, que el coeficiente de la medida μ_Λ ∗ μ_1 en el desfase u = log n es u veces el de
μ_1 (μ_a := Σ a(n) n^{−1/2} δ_{log n}, μ_1 con coeficientes 1). *Demostración:* definición de ∗. ∎

Para cΛ: L = c·log; para a_P: L = log de la parte P-rugosa; para un sistema de Beurling: el logaritmo de
su norma. La regla «Λ(n) = log n − Σ_{d<n}Λ(d)» sólo dice L = log, que es una propiedad de la posición del
desfase, no de los pesos anteriores. En el flujo en T, la convolución μ_Λ ∗ μ_1 compone desfases (suma de
log d y log(n/d)), mientras que la recursión de la ventana compone longitudes (concatenación de
intervalos, producto de matrices de transferencia): las dos operaciones no coinciden. Que no exista un
diccionario no lineal entre ellas es ARGUED (es la lectura de R162_802 §5: dentro del flujo Λ∗1 = log es un
desplazamiento de ventana, lineal en el peso).

## 3. Mecanismo

Ninguno. La pregunta de la semilla sobre el forzante tiene esta respuesta (ARGUED, con las fuentes de §0):
en la ecuación de Bellman del resolvente de la ventana el término de Riccati −γ_Tγ_T* tiene signo fijo
para todo núcleo, de modo que el cono es invariante para cualquier peso; el peine entra sólo en la columna
de borde γ_T, linealmente, como una delta en el desfase log n que en T = T_n acopla exactamente los puntos
±T (factor J-unitario de tipo boost, R162_2701 §1, admisible para cualquier coeficiente). La identidad de
divisores no le da signo al forzante porque el forzante ya tiene signo fijo y no es lo que decide; lo que
decide es la ausencia de explosión, que es la anulación de un determinante (W-det) o el propio n₋(T) = 0
(BARRIER_W_001 W1).

## 4. Controles

No hay paso de signo; los tres lemas son estructurales y valen sin cambios para c = 2, c no entero, a_P
y Davenport–Heilbronn (Lema 1 sólo usa sumabilidad y soporte; Lema 2, afinidad en el peso; Lema 3, la
definición de ∗). Eso es lo esperado de lemas sin signo y confirma que ninguno es mecanismo. En particular
para c = 2 el peso 2Λ cumple la regla de divisores con L = 2 log = log(n²): el factor arquimediano fijo
no aparece en ninguna de las tres invariantes de §1 de modo que la rompa; un mecanismo correcto tendría que
romperse ahí y éste no lo hace.

## 5. Veredicto propio

**No logré escribir un objeto que cumpla A1–A6.** Repetición de R162_802 §§4–5, R162_2701 y BARRIER_W_001.

## Resultado

Sin mecanismo nuevo. Tres lemas sin signo: Lema 1 y Lema 2 PROVED (relativos a lem:contA y a U2, CITED);
Lema 3 PROVED; la lectura del forzante de Riccati ARGUED.

## Qué se probó

La exigencia «conservar la positividad en el cruce sólo con el peso dictado» es imposible para cualquier
invariante cuyo signo determine λ_A (Lemas 1–2); la regla de divisores, leída como regla de actualización,
vale para todo peso con su propio L_a (Lema 3), y su contenido L = log es posicional.

## Qué falló y por qué

Entre cruces el espacio crece y la forma no cambia; en el cruce el término entrante es invisible. El paso
de signo tendría que ser una cantidad no lineal en el peso sobre las trazas de borde del encendido, que
R162_802 ya pidió y no identificó; el dato de puerto de Kreĭn o Tate es ciego a los falsificadores.

## Siguiente paso concreto

Ninguno dentro de esta semilla. Lo único no cubierto es una relación entre la composición de desfases
(μ_Λ ∗ μ_1 = u·μ_1) y la composición de longitudes de la ventana que no sea lineal en el peso; requiere un
objeto escrito antes de cualquier derivación. No abrí en primaria: fase 64 (thm:KEP3), fase 70
(E70_10–12), R162_503, R162_903, ni los archivos de la fase 116/114 con «Dirichlet-to-Neumann».
