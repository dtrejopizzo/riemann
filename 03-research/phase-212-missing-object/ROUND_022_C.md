# Ronda 22, memo C — Postura «primer contacto»: inventario del vector nulo y cotejo de dos ideas

Notación de la ronda 7: `a_T(F) = Arch(F) − Σ_n v_n c_F(log n)` en `P_T = {∫F e^{±t/2} = 0}`, `λ_A(T)` el fondo
primitivo, `W_*` la forma global, `Π_T(M∗φ)` la familia casi radical de `ROUND_021_A` §1.

## Filtro de cuatro puntos (cotejo primero)

1. **Antecedentes, leídos en primaria.**
   - P47 §`sec:firstcontact`: `lem:firstcontact` (l.6591), ecuación débil `eq:localweak` (l.≈6620),
     `prob:annihilate` (l.6887), `prop:annihilate-equiv` (l.6914: el problema ES el objetivo).
   - `phase-197-*/BARRIER_W_001.md` Teoremas W1, W2, W3; en particular **W3(b)**: «para llevar un cruce por cero a
     codimensión ≥ 2 hace falta una condición extra `L(h)=0` en todo vector del núcleo, independiente de la ecuación
     de Euler–Lagrange; candidatos revisados […]; no existe condición independiente en 𝒮».
   - `phase-124-direct-first-contact/`: P124_004 §§4–6 (variación de ventana: sin derivada de forma; nacimientos
     sin tasa ni signo), P124_008 (regularidad nula sólo `H^s`, `s<½`), P124_011 §6 (colar = bloque cruzado
     `ρ_{+,T}`; obstrucción `Π_{ker L_T}ρ_{+,T}`; condición de rango `ρ ∈ Ran L_T^{1/2}` no suministrada),
     P124_012 (reducción a `𝒞_T(F) ≤ 0`, sin signo).
   - `phase-162-*/R162_502_MULTIPLICATIVE_EQUIVARIANCE.md` A5 (lema de la envolvente), `R162_590` §3(H).
   - Fase 114: `114_d_53_THRESHOLD_FLOW_*` (Feynman–Hellmann en umbrales: orientación libre),
     `114_d_134_CENTERED_SCREW_BIRMAN_SCHWINGER_AUDIT.md` (0.4): `‖𝒲_T𝓡_T^{−1/2}‖ ≤ 1 ⟺` objetivo.
   - Índice maestro: «Aniquilación de momentos Gamma en primer contacto» (ABIERTO = Gate 1 = REF-D), «P124 primer
     contacto directo» (NO-GO), «Detección radical finita» R161_046–051 (DEAD), «Candado Thm P» R162_1603 (DEAD),
     «Igualdad de Kadison» R180 (DEAD), D-E/P122.028 (ABIERTO, flujo constante no nulo).
2. **Lo nuevo propuesto por el encargo.** (i) las condiciones `a_{T_*}(F_*, Π_{T_*}(M∗φ)) = 0`, leídas por la
   identidad radical como funcionales de cola; (ii) una positividad de capa terminal.
3. **Resultado del cotejo.** (i) está **contenida en la ecuación de Euler–Lagrange** (§2, PROVED, elemental) y la
   pregunta de independencia es exactamente W3(b) de BARRIER_W_001, ya cerrada. (ii) repite P124_004 §5–6 /
   P124_011 y es ciega a la clase (§3). **Repetición en ambos casos.**
4. **Conexión global.** Ninguna: `prop:annihilate-equiv` hace de cualquier exclusión del primer contacto una
   reformulación del objetivo salvo que un lado tenga prueba independiente (F5); ninguna de las dos la aporta.

## §1 Tabla: lo que se sabe del vector nulo `F_*`

| Propiedad | Estado | Fuente |
|---|---|---|
| Existencia de `T_*>½log5` y `F_*≠0` en `ker H_{T_*}`, `H_{T_*} ≥ 0` | PROVED (condicional a que el objetivo falle) | P47 `lem:firstcontact`, `lem:contA`, `lem:monoT` |
| Paridad definida `JF_* = ±F_*` | PROVED | ídem |
| Envolvente convexa del soporte de longitud exactamente `2T_*` | PROVED (ciego al peso: `c_F` y las restricciones son covariantes por traslación; si cupiera en un intervalo más corto, trasladado daría `λ_A(T)≤0` con `T<T_*`) | R162_502 A5 |
| Ecuación de Euler–Lagrange: `a_{T_*}(F_*,G) = ⟨r,G⟩` ∀G del dominio, `r = α e^{t/2}+β e^{−t/2}` único (los dos multiplicadores de Lagrange) | PROVED | P47 `eq:localweak` |
| Forma de toda la recta: `(L+R_T)u = f_T`, `L = log⟨D⟩`, `u = E_TF_*` | PROVED | P124_008 (1.1)–(1.2) |
| Regularidad: `E_TF_* ∈ H^s`, `0≤s<½`; ninguna ganancia a `H^{1/2}` desde la ecuación sola (contramodelo de mapeo) | PROVED / NO-GO | P121, P124_008 |
| Borde en `±T_*`: un salto no nulo en `H^{1/2}` está prohibido por Lions–Magenes; suponer `H^{1/2}` mata el coeficiente de Tate (circular) | PROVED (condicional, circular) | P122.019/029, P124_008 §4 |
| Multiplicidad: `dim ker H_{T_*} < ∞`; 1 «genéricamente» | PROVED (finitud) / ARGUED (simplicidad: vNW, no prueba para la familia concreta) | `lem:compact`; W3(a),(c) |
| Pasado `T_*`: `n_−` no decrece, todos los cruces hacia abajo; salto `1 ≤ n_−(T_*+0) ≤ dim ker H_{T_*}` | PROVED (≥1, monotonía) / ARGUED (cota superior por semicontinuidad; `lem:contA` da sólo continuidad del fondo) | W1 |
| Toque tangencial unilateral | PROVED | W1, W3(c) |
| Fórmula de tipo Hadamard `dλ_A/dT` en valores de borde | **NO probada**: la parte de Euler no tiene derivada de forma en el dominio de `F_*` (modelo de paquetes (4.2)); nacimientos `= o(1)` sin tasa; con `H^1` supuesto, (4.3) daría la derivada, pero no está disponible | P124_004 §§4–5 |
| Primera variación en un umbral `p^k` | sin signo uniforme: `λ'(s) = ⟨f,W_af⟩`, `W_a = c_a(S_a+S_{−a})` indefinido | D.53 §2 (la nota D.134 es otra: factorización tornillo + BS, (0.4) ⟺ objetivo) |
| Relación con el bloque casi nulo | `a(F_*,Π(M∗φ)) = 0` ∀φ, por EL | §2 abajo |
| Colar | `c=0` en una rama ⟺ `Π_{ker L_T}ρ_{+,T} = 0`; ⟸ `ρ_{+,T} ∈ Ran L_T^{1/2}`, no probado | P124_011 §6 |
| Escalar de costura | `L_TF=0 ⇒ 𝒞_T(F) ≤ 0` sería suficiente; no probado | P124_012 |

**Rutas de contradicción intentadas y cómo terminaron.** Variación de ventana / virial (P124_004, P124_007):
NO-GO por regularidad y signo libre. Colar Schur/Douglas (P124_011): reducción exacta, condición de rango abierta =
REF. Costura causal (P124_012): reducción escalar sin signo. Detección radical finita (R161_046–051): contramodelo
unitario 3-dim, REF-D. Candado Thm P (R162_1603): = Gate 1. Kadison (R180): «primer contacto fuerza igualdad» no
probado. Paridad OS-2 (R166_202): vacío o REF-D. Flujo de umbrales (D.53): sin orientación. Invariantes de índice
(W1–W3): `n_−` es el único y es el objetivo. Aniquilación de momentos Gamma (`prob:annihilate`): equivalente al
objetivo (`prop:annihilate-equiv`), ABIERTO como ruta. Tangencia en `c_*` (fase 211 ROUND_003_A): estructural,
sin signo.

## §2 Idea (i): las condiciones de cola

**Lema 2.1 (PROVED, elemental).** Para todo `φ` admisible, `Π_{T_*}(φ) ∈ P_{T_*}` y está en el dominio de forma,
luego por `eq:localweak`, `a_{T_*}(F_*, Π_{T_*}φ) = ⟨r, Π_{T_*}φ⟩ = 0` (pues `r ⟂ P_{T_*}`). Con la identidad
radical de ROUND_021_A (1.1), polarizada, esto se lee `W_*(F_*, R̃_φ) = 0`, `R̃_φ = R_φ + A(R_φ)u_+ + B(R_φ)u_−`.

*Consecuencia.* Las `≍ e^{2T_*}` condiciones «funcional de cola_φ(F_*) = 0» son **casos particulares** de la
ecuación de Euler–Lagrange con `G = Π_{T_*}φ`; no sobredeterminan nada. La cuenta pedida: el conjunto de soluciones
de EL con `F ∈ P_{T_*}` es `ker H_{T_*}` (dimensión finita; la ecuación es de Fredholm con resolvente compacta,
no una ecuación de retardo con espacio de soluciones fijado por condiciones iniciales); el problema sin la
restricción `F∈P` añade a lo sumo los 2 parámetros `(α,β)`. Las condiciones de cola son `≤` que «todas las `G`»,
así que el número de condiciones independientes **nuevas** es 0. La pregunta «¿hay una condición lineal sobre el
núcleo independiente de EL?» es literalmente W3(b), cerrada en 𝒮 (BARRIER_W_001 §4).

Lectura en forma de anulador: `F_*` pertenece al complemento `a`-ortogonal del bloque casi nulo, que tiene
codimensión finita `≍ e^{2T}` y es enorme; estar ahí no es contradictorio. Convertir `W_*(F_*, R̃_φ) = 0` en
`F_* = 0` exigiría Cauchy–Schwarz con `W_* ≥ 0` (el objetivo: circular, F5) o un teorema de unicidad del tipo
«el `W_*`-anulador de `{R̃_φ}` en `P_T` es nulo», que es falso por lo anterior.

**Controles.** Con `2Λ`, borrado de una potencia de primo o peso de Beurling, `M∗φ` deja de estar en el radical y el
paso «identidad radical» se cae (la funcional deja de ser de cola); pero el Lema 2.1 sigue valiendo para sus vectores
nulos, que existen. Es decir: la parte que sobrevive es ciega (vale en los controles), y la parte que depende del
peso no aporta condición nueva.

## §3 Idea (ii): positividad de capa terminal

Lo cierto (ARGUED, de la forma de `W`): como `G′ = K ~ 1/u` en `0`, `π − G(T−t) ~ log(1/(T−t))`, y `Arch`
contiene un peso logarítmico positivo en las capas. Con el término de primos acotado en `L²` y `Arch` acotado
inferiormente, se obtiene una desigualdad de tipo Gårding

    a_T(F) + C_T‖F‖² ≥ c·log(1/δ)·‖F·1_{T−δ<|t|<T}‖².

En el vector nulo da `‖F_*‖²_{capa δ} ≤ C_T/log(1/δ)`: decaimiento de la masa de capa, compatible con
`H^s`, `s<½` (masa `O(δ^{2s})`). Para contradecir el primer contacto se necesitaría una **cota inferior**
cuantitativa de la masa de capa de `F_*`, y la minimalidad sólo da A5 (la envolvente toca los extremos: masa
positiva en toda capa, no grande). La versión cuantitativa —comparar `a(F_*) = 0` con `a(χF_*) ≥ λ_A(T_*−δ)‖·‖²`—
es exactamente la variación de ventana de P124_004 (términos cruzados de colar sin tasa ni signo) y el bloque
cruzado de P124_011.

**Desigualdad que contradiría el primer contacto** (enunciado preciso): existe `c(T)>0` y `δ>0` con
`a_T(F) ≥ c(T)‖F 1_{capa δ}‖² − (algo que se anula en ker H_T)` para `F ∈ P_T`, junto con
`F ∈ ker H_T, F≠0 ⇒ ‖F 1_{capa δ}‖ ≥ κ‖F‖`. La primera mitad es ciega (sólo usa `W`, vale en los tres controles);
la segunda es la minimalidad cuantitativa, que **falla en los controles**: allí hay primeros contactos con
vectores nulos de envolvente `2T_*` (A5 es ciego al peso), así que el par de desigualdades probaría algo falso en
los controles si no usa el peso, y no hay paso que lo use. Lema T (F1): falla.

El término `(2T+O(1))‖(1−χ)(M∗φ)‖²` de ROUND_021_A es un defecto del bloque casi nulo, no una cota inferior sobre
vectores generales: no se transfiere a `F_*`, que es `a`-ortogonal al bloque (Lema 2.1).

## §4 Veredicto

**REPETICIÓN.** (i) PROVED trivial: las condiciones de cola son instancias de EL; la independencia buscada es
W3(b) (BARRIER_W_001), cerrada. (ii) repite P124_004 §§5–6 / P124_011 §6; la parte positiva es arquimediana y
ciega, la parte que falta es minimalidad cuantitativa, falsa en los controles. Ningún resultado intermedio nuevo:
el decaimiento de masa de capa es consecuencia directa de P124_008 y no se registra como nuevo.
No encuentro dentro de esta postura una idea distinta defendible: toda contradicción desde `F_*` pasa por
`prop:annihilate-equiv`, y las propiedades de `F_*` probadas (tabla §1) son, salvo las identidades de P47
§`sec:firstcontact`, válidas en 𝒮 entero. **Próxima operación: ninguna en esta postura.**
