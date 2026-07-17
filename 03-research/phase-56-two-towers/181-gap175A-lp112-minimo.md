# Documento 181 — GAP 175.A: la instancia mínima de LP-112 es la dicotomía disfrazada

**Programa:** Hipótesis de Riemann — Fase 56 (dos torres)
**Fecha:** 2026-06-11
**Mandato:** atacar GAP 175.A (la instancia mínima de LP-112): probarla, probar la versión más débil que aún alimente la dicotomía de energía, o identificar la obstrucción exacta. Tres vías: Bagchi-sin-RH, Hurwitz/sin-Euler (test Davenport–Heilbronn), cuantitativa (medida de testigos).
**Prerrequisitos leídos en fuente:** Doc 175 completo (Lema 175.1, Thm 175.2, Obs 175.3, Cor 175.4–175.5, Thm 175.6, Prop 175.7–175.8, GAP 175.A/175.B, §4 estado honesto de LP-112), Doc 112 vía sus citas en D175.
**Contrato:** [TEOREMA]/[PROP]/[LEMA] solo con prueba completa; [GAP]/[GAP de literatura] declarados con forma de enunciado; sin numérica; honestidad total — falsa victoria peor que fracaso. Backward-only: Voronin 1975, Bagchi 1981/1987, Reich 1980, Steuding 2007, Garunkštis–Karikovas 2014, Selberg 1946, Docs 112/170/175.

**Coordenadas (idénticas a D170/D175).** Cero off $\rho=\tfrac12+b+i\gamma$, $b\in(0,\tfrac12)$, un representante por cuádruplo; $I=I(0^+)=\sum_j b_j^2$; $I=0\iff$ RH. Para un cero off $\rho_0$: constantes canónicas $r=r(\rho_0)\le b_0/2$, $D_0=\bar D(\rho_0,r)$, $\eta=\min_{\partial D_0}|\zeta|>0$ (D175 §2.2). **LP-112**: para todo disco cerrado $D\subset\{\tfrac12<\sigma<1\}$ existe $\tau_k\to\infty$ con $\sup_D|\zeta(s+i\tau_k)-\zeta(s)|\to0$. **LP-112[$\rho_0$]**: existe sucesión no acotada con $\sup_{D_0}|\zeta(\cdot+i\tau_k)-\zeta|\le\varepsilon$ para UN $\varepsilon<\eta$ fijo. **Dic** := $I(0^+)\in\{0,\infty\}$ (la dicotomía de energía).

---

## 0. Resumen ejecutivo y veredicto

**GAP 175.A NO se prueba — se DISUELVE.** El hallazgo central, que el Doc 175 ya contenía sin extraer:

1. **[TEOREMA 181.1] $0<I<\infty\;\Longrightarrow\;\neg$LP-112** (de hecho $\neg$LP-112[$\rho_0$] para TODO cero off). Es el cierre limpio de la Vía 3: la Prop 175.8 da finitud de testigos a *radio fijo* $r$ y *precisión fija* $\varepsilon<\eta$, y LP-112 (que pide convergencia, más fuerte) implica infinitos testigos a esa calidad fija. La prueba es de tres líneas pero la consecuencia es estructural.
2. **Por tanto LP-112 ⟹ Dic (Thm 175.2) NO es una implicación entre un axioma y una conclusión: es media equivalencia.** Lo probado queda: $\mathrm{LP\text{-}112}\Rightarrow\mathrm{Dic}$ y $\;\mathrm{Dic}\Rightarrow\mathrm{LP\text{-}112}$ *salvo el caso $I=\infty$* ([TEOREMA 181.2]: la vuelta en el caso $I=0$ es Bagchi). El residuo exacto es **[GAP 181.A]**: ¿$I=\infty\Rightarrow$ LP-112? Modulo ese gap, **LP-112 ⟺ Dic: LP-112 es OTRO NOMBRE de la dicotomía, no un input independiente.**
3. **Corolario brutal para la torre:** condicional a A ($I<\infty$), **LP-112 ⟺ RH** ([COR 181.3]). La "segunda flecha" no es un atajo: cualquier prueba de LP-112 debe, en el mundo $0<I<\infty$, ser falsa — luego **LP-112 es indemostrable sin antes excluir el estado intermedio**, que es exactamente lo que la torre quería usar LP-112 para hacer. GAP 175.A ("prueba la instancia mínima") pedía probar un enunciado que es FALSO en el único mundo donde la torre lo necesita con contenido. La torre se reconfigura: $\mathrm{RH}\Longleftarrow A\wedge\mathrm{Dic}$, y Dic hay que atacarla directamente (coercividad D174, Green–Littlewood D173/176), no vía recurrencia.
4. La paradoja del mandato queda resuelta (§1), el test D–H es consistente con la equivalencia (§3, con [GAP de literatura 181.C]), y el enunciado mínimo residual genuino es GAP 181.A — interesante solo como *certificado de reformulación*, no como ruta a RH.

---

## 1. Vía 3 primero (decide todo): la finitud de la Prop 175.8 a calidad fija

Releída en fuente, la prueba de la Prop 175.8 (D175 §5) opera así: para $\rho_0$ fijo con constantes canónicas $(r,\eta)$ y CUALQUIER $\varepsilon<\eta$ fijo, el mapa de réplica (Rouché, Lema 175.1(i) con $\delta=R=r$) inyecta los testigos $2r$-separados de $A_\varepsilon$ en cuádruplos con $b\ge b_0/2$, de los que hay $\le 4I/b_0^2<\infty$ por Chebyshev sobre la serie completa; $A_\varepsilon$ queda contenido en $\le 4I/b_0^2$ intervalos de longitud $\le 2r$, luego es acotado. **Confirmado: la finitud es para $r$ FIJO (el canónico) y $\varepsilon$ fijo — no requiere $\varepsilon\to0$ ni $r\to0$.** Esto responde la pregunta del mandato: en el estado $0<I<\infty$ queda excluida toda sucesión no acotada de testigos *ya a una sola calidad fija* $(r,\varepsilon)$ con $\varepsilon<\eta$; con mayor razón toda sucesión de convergencia uniforme (que exige calidad eventual $<\varepsilon$ para todo $\varepsilon$, en particular para uno fijo $<\eta$).

**[TEOREMA 181.1] (anti-recurrencia decide la instancia mínima).** *Si $0<I(0^+)<\infty$, entonces LP-112[$\rho_0$] es falsa para todo cero off $\rho_0$, y a fortiori LP-112 es falsa.*

*Demostración.* Sea $\rho_0$ cero off (existe: $I>0$), con $(r,\eta)$ canónicos. LP-112[$\rho_0$] afirma una sucesión no acotada $\{\tau_k\}\subset A_\varepsilon$ para algún $\varepsilon<\eta$. Por la Prop 175.8 (incondicional, válida bajo $0<I<\infty$), $A_\varepsilon\subset\bigcup_{z\in\mathcal Z}T_z$ con $\#\mathcal Z\le 4I/b_0^2<\infty$ y cada $T_z$ un intervalo acotado (contenido en $(\gamma_z-\gamma_0-r,\gamma_z-\gamma_0+r)$); un subconjunto de una unión finita de intervalos acotados está acotado: no admite sucesión no acotada. Contradicción. Para LP-112 pleno: aplicado al disco $D_0$ produce $\tau_k\to\infty$ con $\sup_{D_0}|\zeta(\cdot+i\tau_k)-\zeta|\to0$, en particular $<\eta/2$ para $k$ grande — una sucesión no acotada en $A_{\eta/2}$, imposible. $\blacksquare$

**Resolución de la paradoja aparente del mandato.** "Los ceros off raros ⟹ los trasladados genéricamente no tienen cero cerca de $\rho_0-i\tau$ ⟹ la auto-aproximación falla genéricamente" — correcto, y en el estado $0<I<\infty$ falla no solo genéricamente sino *cofinitamente* (Thm 181.1). No hay paradoja con el Thm 175.2: **175.2 y 175.8/181.1 son contrapositivas la una de la otra** (la Obs 175.3 ya lo decía a media voz). La lógica real de la dicotomía es: *LP-112 es un axioma que EXCLUYE el estado intermedio porque en el estado intermedio es falso.* No hay mecanismo positivo de replicación que LP-112 "active"; hay una incompatibilidad lógica entre recurrencia no acotada y presupuesto finito de energía.

**Test anti-circularidad.** El Thm 181.1 no usa RH ni ζ-input más allá de: ceros aislados, Hadamard–dVP ($b<\tfrac12$), Rouché y la definición de $I$. La Prop 175.8 que invoca es incondicional (Chebyshev + Rouché). No hay circularidad: el teorema vale en cualquier mundo, y en cada mundo dice algo distinto sobre LP-112 (falsa en $0<I<\infty$; cierta en $I=0$ por Bagchi; abierta en $I=\infty$). Lo que sería circular es lo que GAP 175.A pedía: "probar LP-112[$\rho_0$]" incondicionalmente — eso EQUIVALE a probar que el mundo no es $0<I<\infty$ (más exactamente: implica que si hay cero off, $I=\infty$), que es la dicotomía misma. El input pedido era la conclusión.

---

## 2. Vía 1: la equivalencia y su residuo exacto

Reunimos las piezas en el enunciado de tres estados.

**[TEOREMA 181.2] (estado de LP-112 por estado de energía).**
1. $I=0$ (RH): **LP-112 es verdadera** — Bagchi: bajo RH, $\zeta|_D$ es no-nula para todo disco $D$ de la franja, está en el soporte de su medida límite, y la recurrencia fuerte da densidad inferior positiva de testigos para todo $\varepsilon$ [Bag81, Bag87; Ste07 §8.3]; en particular sucesiones no acotadas.
2. $0<I<\infty$: **LP-112 es falsa** (Thm 181.1).
3. $I=\infty$: **abierto** ([GAP 181.A]).

*Demostración.* (1) cita verificada contra D175 §4 (que la verificó en fuente); (2) Thm 181.1; (3) es declaración de gap. $\blacksquare$

**[COR 181.3] (LP-112 no es input independiente).**
1. $\mathrm{LP\text{-}112}\;\Longrightarrow\;\mathrm{Dic}$, y $\;\mathrm{Dic}\Rightarrow\mathrm{LP\text{-}112}$ en el caso $I=0$; por tanto **LP-112 ⟺ Dic modulo GAP 181.A**, y *incondicionalmente* $\;\neg(0<I<\infty)\;\Longleftarrow\;\mathrm{LP\text{-}112}\;$ con la recíproca rota solo en $I=\infty$.
2. **Condicional a A ($I<\infty$): LP-112 ⟺ RH.** (⟸: Bagchi. ⟹: con $I<\infty$, el caso (2) del Thm 181.2 queda excluido por la verdad de LP-112, luego $I=0$.)
3. Por tanto la torre $\mathrm{RH}\Longleftarrow A\wedge\mathrm{LP\text{-}112}$ es, *como objetivo de prueba*, idéntica a $\mathrm{RH}\Longleftarrow A\wedge\mathrm{Dic}$: cualquier demostración de LP-112 contiene una demostración de "no existe el estado $0<I<\infty$" (si existiera, lo demostrado sería falso). **LP-112 no es atajo: es la dicotomía con nombre de recurrencia.**

*Demostración.* (1) ida = Thm 175.2; vuelta-caso-$I=0$ = Thm 181.2(1); la identificación "LP-112 ⟹ ¬(0<I<∞)" es Thm 181.1 contrapuesto. (2) y (3) son lecturas directas. $\blacksquare$

**Honestidad sobre qué cambia y qué no.** El Thm 175.2 sigue siendo correcto tal cual; lo que muere es su *lectura estratégica* ("falta solo LP-112, un lema de universalidad plausiblemente atacable por teoría ergódica"). La vía Bagchi-sin-RH del mandato queda cerrada *en negativo* sin necesidad de entrar en el toro $\Omega=\prod_p\mathbb T$: no hay que examinar si la equidistribución de Kronecker–Weyl produce una sucesión excepcional, porque sabemos *a priori* que en el estado $0<I<\infty$ NO la produce (no existe), y en los otros dos estados LP-112 o ya es teorema o es GAP 181.A. El muro de P43 §3.1 ("producir un elemento de un conjunto excepcional") era el diagnóstico equivocado para este gap: el conjunto no es excepcional sino *finito* — no hay nada que producir. El error mejor (el muro real) está en GAP 181.A o, equivalentemente, en Dic directa.

**¿Es plausible GAP 181.A ($I=\infty\Rightarrow$ LP-112, o siquiera LP-112[$\rho_0$] para algún $\rho_0$)?** A favor: $I=\infty$ da presupuesto infinito de réplicas — las cotas 175.6/175.8 no obstruyen nada; con $E(T)\to\infty$ hay infinitos cuádruplos con $b\ge b_0/2$ disponibles a alturas no acotadas. En contra (la obstrucción exacta): Rouché solo da la dirección testigos⟹ceros; la dirección ceros⟹testigos exige que el trasladado aproxime *toda la función* en $D_0$, no solo que tenga un cero bien puesto — es el problema de universalidad fuera del soporte de Bagchi (Euler comprime el soporte a funciones no-nulas; D175 §4.3), ahora en el mundo $I=\infty$, donde la medida límite sigue teniendo soporte sin-ceros (los teoremas límite valen incondicionalmente en $\sigma>\tfrac12$ en media, [Lau96]) mientras la función real tiene infinitos ceros off. Nada en la maquinaria distribucional ve esos ceros. **No hay ruta visible; tampoco refutación: un mundo $I=\infty$ podría ser tan patológico que la auto-aproximación valga por abundancia bruta, o fallar igualmente.** Lo dejamos como gap genuino con las dos salidas etiquetadas abajo (Escenarios S1/S2).

---

## 3. Vía 2: el test sin-Euler (Hurwitz y Davenport–Heilbronn)

**Hurwitz.** Para $\zeta(s,\alpha)$ con $\alpha$ trascendente (y casos racionales $\ne\tfrac12,1$), la auto-aproximación es teorema *incluso en discos con ceros* — [GK14] (Garunkštis–Karikovas, *Self-approximation of Hurwitz zeta-functions*, Funct. Approx. Comment. Math. 51, 2014; verificado solo contra la cita ya auditada en D175 §4.3 — la atribución exacta del caso racional la dejamos en la cita de D175, no la re-auditamos). Mecanismo: sin producto de Euler, la medida límite tiene soporte pleno en $H(D)$ (universalidad fuerte de Bagchi): el target *con ceros* es genérico para su propio flujo. Consistencia con la equivalencia 181.3: $\zeta(s,\alpha)$ tiene infinitos ceros en $\tfrac12<\sigma<1$ con abscisas que NO se acumulan en $\tfrac12$ (hay franjas $\sigma\in(\tfrac12+\delta,1-\delta)$ con $\gg T$ ceros — clásico para Hurwitz, vía la misma universalidad fuerte), luego su análogo de $I$ es $\sum b_j^2=\infty$ trivialmente. **Hurwitz vive en el caso $I=\infty$ y SÍ tiene LP-112-análogo: el único dato externo disponible es consistente con "$I=\infty\Rightarrow$ auto-aproximación" (S1).** Pero el mecanismo (soporte pleno) NO se transfiere a ζ: es exactamente lo que Euler destruye. El test calibra, no prueba.

**Davenport–Heilbronn.** $f_{DH}$ (combinación de dos $L(s,\chi)$ mod 5 con ecuación funcional, sin Euler) tiene infinitos ceros off con $b$ acotado abajo — "ceros gordos", Doc 146/150 —, de hecho $\gg T$ ceros en franjas $\sigma>\tfrac12+\delta$; luego $I_{DH}=\infty$. ✓ Consistente con la dicotomía (si $f_{DH}$ satisface un LP-112-análogo, su $I$ debe ser $\infty$ — lo es). ¿Satisface auto-aproximación secuencial? El mecanismo esperado: la universalidad CONJUNTA de $L(s,\chi_1),L(s,\chi_2)$ [Vor75; Ste07 cap. 10] da universalidad fuerte (soporte pleno, targets con ceros permitidos) para la combinación lineal — es el mecanismo estándar con que se explican sus ceros off —, y soporte pleno + el propio $f_{DH}$ en el soporte daría recurrencia fuerte, luego LP-112-análogo. **[GAP de literatura 181.C]:** no puedo verificar en fuente aquí un enunciado publicado "auto-aproximación de $f_{DH}$ en discos que contienen sus ceros off" (los teoremas de universalidad fuerte para combinaciones lineales — línea Kaczorowski–Kulas y posteriores — los conozco solo de memoria; el paso "el target $f_{DH}$ mismo está en el soporte conjunto" requiere chequeo de no-degeneración). Lo registro como verificación pendiente, con predicción falsable: **si la equivalencia 181.3 + S1 es correcta, $f_{DH}$ DEBE tener auto-aproximación secuencial en sus discos off.** Una refutación de eso refutaría S1 (no la equivalencia: $f_{DH}$ no es ζ).

**Objeto intermedio (Euler parcial $\zeta_S\cdot$resto).** Sin desarrollar: cualquier Euler parcial sigue comprimiendo el soporte del factor $\zeta_S$ pero el resto lo descomprime; el objeto no hereda limpio ni el soporte pleno ni la compresión. No se ve palanca; no se persigue.

---

## 4. Veredicto

**GAP 175.A queda CERRADO EN NEGATIVO: el enunciado pedido es indemostrable-sin-probar-la-dicotomía porque es falso en el estado $0<I<\infty$** (Thm 181.1). No era "la instancia mínima de un lema de universalidad": era la dicotomía con disfraz. Resultados:

1. **[TEOREMA 181.1]** (incondicional): $0<I<\infty\Rightarrow\neg$LP-112[$\rho_0$] $\forall\rho_0$ $\Rightarrow\neg$LP-112. (Extracción de la Prop 175.8; la finitud a calidad fija $(r,\varepsilon<\eta)$ verificada en la prueba fuente.)
2. **[TEOREMA 181.2]** LP-112 por estados: verdadera en $I=0$ (Bagchi), falsa en $0<I<\infty$, abierta en $I=\infty$.
3. **[COR 181.3]** LP-112 ⟺ Dic modulo GAP 181.A; condicional a A, **LP-112 ⟺ RH**. La torre de energía se reconfigura: $\boxed{\mathrm{RH}\Longleftarrow A\wedge\mathrm{Dic}}$ con Dic = $I\in\{0,\infty\}$ como objetivo directo; LP-112 deja de ser atajo y pasa a ser *reformulación candidata* de Dic.

**GAPs numerados:**
- **[GAP 181.A]** (el residuo exacto de la equivalencia): *$I=\infty\Rightarrow$ LP-112* (basta: existe un cero off $\rho_0$ con LP-112[$\rho_0$]). Valor: certificaría LP-112 ⟺ Dic exacto. Escenarios: **S1** (cierto — apoyado por Hurwitz y presumiblemente D–H): LP-112 = otro nombre de Dic. **S2** (falso): LP-112 ⟺ RH a secas (¡LP-112 secuencial sería equivalente a RH, cerrando la pregunta abierta de D112 §4 — también valioso!). En ambos escenarios LP-112 NO es input independiente. Obstrucción identificada: universalidad fuera del soporte de Bagchi; la abundancia de ceros ($I=\infty$) da las réplicas pero no la aproximación de toda la función.
- **[GAP de literatura 181.C]**: auto-aproximación de Davenport–Heilbronn en discos con ceros off (universalidad fuerte de combinaciones lineales + $f_{DH}$ en el soporte). Test falsable de S1.
- GAP 175.B (automaticidad de densidad) queda *degradado*: en el estado $0<I<\infty$ no hay sucesión que densificar (181.1 lo hace vacuo ahí); solo conserva contenido en $I=\infty$.

**Dirección sucesora.** Todo el peso vuelve a **Dic directa**: excluir $0<I<\infty$ sin recurrencia. Los activos del programa para eso son los de la otra cara de la Fase 55: coercividad $\dot I\le-2I$ (D174), el límite Cesàro $\pi I-\pi/8$ (D176.4) y la torre dinámica (177.B∧LP-134 ⟹ $m<\infty$ — nótese que $m<\infty\Rightarrow I<\infty$, luego la torre dinámica empuja hacia el estado donde 181.1 hace falsa a LP-112: las dos torres ahora *cooperan* contra el estado intermedio en vez de compartir el axioma). Documento sucesor sugerido: 182 — ¿la coercividad de D174 ($\dot I\le-2I$, ley de balance D167) es compatible con un estado estacionario $0<I<\infty$, o el flujo mismo excluye el estado intermedio? Esa es ahora la pregunta de la dicotomía en su hábitat natural.
