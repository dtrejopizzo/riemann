# Doc 165 — Destructor del import cuántico (Stone + ecuación de onda → ¿RH por unitariedad estructural?)

**Fase 53. Rol: DESTRUCTOR adversarial, independiente del constructor (Doc 164 aún no escrito al momento de redactar esto).**

## Afirmación bajo ataque

> Existe una evolución unitaria $U(t)=e^{itH}$ sobre un espacio natural, con $\operatorname{spec}(H)=\{\gamma_\rho\}$ (las ordenadas de los ceros de $\zeta$), donde la unitariedad — vía el **teorema de Stone** ($U(t)$ unitario fuertemente continuo $\Rightarrow$ $H$ autoadjunto $\Rightarrow$ $\operatorname{spec}(H)\subset\mathbb{R}$ $\Rightarrow$ RH) — proviene de una **simetría estructural RH-libre** (la ecuación funcional $s\leftrightarrow 1-s$, una involución), **no** de la métrica de Weil $\langle f,g\rangle_W=\sum_\rho \hat f(\gamma_\rho)\overline{\hat g(\gamma_\rho)}$ que ya enumera los ceros.

La esperanza concreta: que "unitario" sea una propiedad **gratuita** (heredada de la simetría funcional), de modo que la realidad del espectro caiga sin pagar el precio de positividad que es RH.

Resumen del veredicto, por adelantado: **las tres vías matan**, y las tres lo hacen reduciéndose a obstrucciones **YA CONOCIDAS** del programa (Krein-indefinido = la métrica de Phase 51; deficiencia = condiciones de borde; absorción = positividad de traza). El import cuántico **NO toca $\zeta$ en un nodo nuevo**: re-expresa en lenguaje de Stone/von Neumann el mismo nodo "$\zeta$ ES la dualidad" de Phase 52. Detalle abajo.

---

## Vía 1 — Unitariedad = la métrica de Weil disfrazada (Stone NO da espectro real en un espacio de Krein)

### El argumento de muerte (forma cerrada)

**Premisa estructural.** "$U(t)$ unitaria" no es una afirmación absoluta: es unitaria **respecto de un producto interno**. La pregunta operativa es: ¿qué forma sesquilineal $\langle\cdot,\cdot\rangle$ deja invariante la evolución candidata que tiene $\{\gamma_\rho\}$ por espectro?

La simetría estructural disponible y RH-libre es la ecuación funcional, encarnada como la involución $J:\;s\mapsto 1-s$ (equivalentemente, en variable espectral, $\xi(s)=\xi(1-s)$ con $s=\tfrac12+i\gamma$). Esta involución es **RH-libre**: vale incondicionalmente. Pero lo que produce sobre el espacio de prueba **no es un producto interno definido positivo**. Produce exactamente la **forma de Weil** $Q$, que es la forma cuadrática de la fórmula explícita:
$$
Q(\hat h,\hat h)=\sum_\rho \hat h(\gamma_\rho)\,\overline{\hat h(\gamma_\rho)}\quad\text{(esquemáticamente, con el término arquimediano + primos)}.
$$
El programa YA demostró (Phase 26, Phase 38 D63, Phase 51 D161) que esta $Q$ tiene **índice negativo $\kappa=2m$**, donde $m$ = número de ceros fuera de la recta crítica (contados con la simetría de Klein $V$, órbitas $\rho,1-\rho,\bar\rho,1-\bar\rho$). Es decir:
- $Q$ definida positiva $\iff \kappa=0 \iff m=0 \iff$ RH.
- Bajo no-RH, $Q$ es **indefinida**, con $\kappa=2m>0$ direcciones negativas: una **forma de Pontryagin** $\Pi_\kappa$ (espacio de Krein de índice finito).

**El golpe.** En este escenario, "$U(t)$ unitaria respecto de $Q$" significa **$J$-unitaria** (unitaria en el sentido de Krein), y el generador $H_C$ (Connes) es **$Q$-autoadjunto** (= $J$-autoadjunto), NO autoadjunto en sentido de Hilbert. Y aquí está el hecho de teoría de operadores que destruye la esperanza:

> **El teorema de Stone NO garantiza espectro real para generadores $J$-autoadjuntos en espacios de Krein con $\kappa>0$.** Los operadores $J$-autoadjuntos (= autoadjuntos respecto de una forma indefinida) admiten genéricamente **espectro complejo**, organizado en pares conjugados respecto del producto $J$ (i.e. $\lambda$ autovalor $\Rightarrow \bar\lambda$ autovalor, simetría espectral, NO realidad).

Más finamente (Bognár, *Indefinite Inner Product Spaces*, Springer 1974, Cap. VI; Azizov–Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric*, Wiley 1989, §II.6 y Cap. V): un operador $J$-autoadjunto en $\Pi_\kappa$ tiene a lo sumo $\kappa$ autovalores **no reales** (contando multiplicidades en el sentido del subespacio negativo maximal), y exactamente esos son los que pueden salirse de $\mathbb{R}$. **El número de autovalores potencialmente complejos está acotado por $\kappa=2m$** — que es precisamente la conjetura puente de Phase 26 (Teorema 26-C.2): los $2m$ autovalores complejos $\{\pm b_j+i\gamma_j\}$ corresponden a los ceros fuera de la recta.

**Esto es matemáticamente fatal para la esperanza, y lo es por la razón más limpia posible:** la versión de Stone que da espectro real exige un **espacio de Hilbert genuino**, i.e. forma **definida positiva**. La única forma para la cual la evolución es "unitaria" es $Q$ (forma de Weil), y $Q$ es definida positiva **si y solo si RH**. Por lo tanto:

$$
\boxed{\;\text{"unitario}\Rightarrow\text{espectro real"} \;\equiv\; \text{"}Q\text{ definida positiva"} \;\equiv\; \kappa=0 \;\equiv\; \text{RH}.\;}
$$

La importación cuántica no compra nada: **suponer la hipótesis de Hilbert (forma definida) ya es suponer RH.** El teorema de Stone es un bicondicional disfrazado, no una palanca.

### Por qué la versión de Krein de Stone no salva la situación

Existe una teoría de grupos uniparamétricos en espacios de Krein (teorema tipo Stone para $C_0$-grupos $J$-unitarios; ver Azizov–Iokhvidov §V.3, y la teoría de Langer–Najman de funciones definidas de operadores en Pontryagin). PERO su conclusión es justamente la opuesta a la deseada: el generador es $J$-autoadjunto y, **cuando $\kappa>0$, su parte no real es genérica y está soportada precisamente por el subespacio negativo de dimensión $\kappa$.** El grupo $J$-unitario $e^{itH}$ con $H$ teniendo autovalores complejos **NO es acotado en norma de Hilbert** (crece como $e^{|\operatorname{Im}\lambda|\,t}$), lo cual es consistente: no hay norma de Hilbert preservada porque la forma preservada es indefinida. Stone-en-Hilbert no aplica porque su hipótesis (unitariedad en norma) **falla**, y Stone-en-Krein sí aplica pero **no concluye realidad**.

### Veredicto Vía 1: **MATA.**
Y mata en el **nodo CONOCIDO de la métrica/orientación** (Phase 51 D161, Phase 52 D163 Vía 1). La "simetría estructural RH-libre" (ecuación funcional) entrega genuinamente una estructura — pero una estructura de **Krein/Pontryagin**, no de Hilbert. Convertirla en Hilbert (= elegir un producto definido positivo respecto del cual $U$ sea unitaria) es exactamente la métrica de Weil que carga $\zeta$, y su definitud es RH. **Esto es el κ=2m de Phase 26 reformulado como obstrucción de Stone.**

---

## Vía 2 — El generador no es esencialmente autoadjunto (la pared de Berry–Keating: índices de deficiencia = condiciones de borde = ζ)

### El argumento de muerte (forma cerrada, con cuantificación de índices)

El generador candidato natural en este círculo de ideas es el dilatador / Hamiltoniano de Berry–Keating $H_{BK}=\tfrac12(xp+px)=-i\left(x\partial_x+\tfrac12\right)$ sobre la semirrecta $x>0$ (o el operador de escala de Connes $H_C$, que es la versión adélica del mismo generador de dilataciones). El espectro clásico-semiclásico $\sim\frac{1}{2\pi}E\log E$ reproduce la cuenta de Riemann–von Mangoldt $N(T)\sim\frac{T}{2\pi}\log\frac{T}{2\pi}$. Berry–Keating (*SIAM Review* 41 (1999) 236–266; y Berry–Keating, "$H=xp$ and the Riemann zeros", en *Supersymmetry and Trace Formulae*, 1999) lo señalan explícitamente y nombran el obstáculo: **el operador no está definido sin condiciones de borde, y la cuantización exacta de los $\gamma$ exige una condición que codifica $\zeta$.**

**Cuantificación de los índices de deficiencia.** Conjugando por la transformada de Mellin, $H_{BK}=-i(x\partial_x+\tfrac12)$ es unitariamente equivalente al operador de momento $-i\partial_u$ sobre $u=\log x\in\mathbb{R}$ (en toda la recta) — que es esencialmente autoadjunto, índices $(0,0)$, espectro $=\mathbb{R}$ entero (continuo). **Ese caso da espectro continuo, NO $\{\gamma\}$.** Para obtener un espectro discreto hay que **restringir el dominio** (semirrecta $x>0$, o introducir un corte/regularización tipo $|x|\geq\ell$, o la "caja" de Berry–Keating–Connes). En cuanto se restringe a una semirrecta $u\in(0,\infty)$ o a un intervalo, el operador de momento $-i\partial_u$ adquiere **índices de deficiencia no nulos**:

- Semirrecta $u\in(0,\infty)$, $-i\partial_u$: índices $(n_+,n_-)=(1,0)$ — **NO hay extensión autoadjunta** (índices desiguales). El operador es maximal simétrico pero no autoadjunto; genera un semigrupo de isometrías, no un grupo unitario. Esto es el clásico ejemplo de von Neumann/Reed–Simon (Reed–Simon, *Methods of Modern Mathematical Physics II*, 1975, ejemplo en §X.1, "momento en la semirrecta"). **Stone no aplica: no hay $U(t)$ unitario en absoluto.**
- Intervalo $u\in(a,b)$, $-i\partial_u$: índices $(1,1)$ — hay una **familia $U(1)$ de extensiones autoadjuntas** parametrizadas por $\theta\in[0,2\pi)$ (condición de borde cuasi-periódica $\psi(b)=e^{i\theta}\psi(a)$). Cada $\theta$ da un operador autoadjunto distinto con espectro $\{(2\pi n+\theta)/(b-a)\}$ — espectro **equiespaciado**, jamás $\{\gamma\}$.

**El golpe.** La simetría estructural (dilatación + ecuación funcional) fija el generador **solo hasta la elección de extensión autoadjunta**, i.e. hasta la condición de borde. Y:

1. Si el dominio natural da índices **desiguales** ($(1,0)$, caso semirrecta), **no existe ninguna extensión autoadjunta**: la evolución unitaria buscada **no existe**, Stone es inaplicable de raíz.
2. Si se fuerza un dominio con índices **iguales** ($(1,1)$ o $(n,n)$), existe una familia de extensiones, pero la condición de borde que produce el espectro $\{\gamma\}$ **no es la ecuación funcional sola** — es una condición de pegado/dispersión cuyo dato espectral es la **fase de $\zeta(\tfrac12+i\gamma)$** (el factor $\chi(s)$ de la ecuación funcional evaluado, que es donde $\zeta$ entra). La cuantización de Berry–Keating–Connes lo hace explícito: la condición de borde es $\frac{\zeta(\tfrac12-iE)}{\zeta(\tfrac12+iE)}$-tipo, i.e. **fijar la extensión = conocer $\zeta$ sobre la recta crítica = conocer los ceros.**

$$
\boxed{\;\text{"elegir la extensión autoadjunta que da }\{\gamma\}\text{"}\;\equiv\;\text{"condición de borde}=\text{fase de }\zeta\text{"}\;\equiv\;\text{conocer los ceros}.\;}
$$

La autoadjunción no es estructural: es una **elección de von Neumann** entre un continuo de operadores, y el único miembro de la familia con espectro $\{\gamma\}$ es el que tiene a $\zeta$ codificada en su frontera. La simetría funcional restringe pero **no determina** la condición de borde.

### Matiz honesto — [GAP]

Hay una sutileza que conviene declarar: la ecuación funcional **sí** impone una condición de borde (la involución $s\leftrightarrow 1-s$ se traduce en un emparejamiento de los dos extremos / de las dos asíntotas vía el factor $\chi$). En ese sentido, la simetría estructural **no deja la condición totalmente libre**. PERO el factor $\chi(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)$ es la parte **arquimediana/gamma** de la ecuación funcional; la información que falta para llegar a $\{\gamma\}$ es la parte **finita** (el producto de Euler / los primos). [GAP de literatura, honesto]: no conozco una prueba publicada de que la condición de borde fijada por la ecuación funcional completa (incluyendo el lado de Euler) determine unívocamente la extensión, **ni** una que muestre que queda un grado de libertad RH-dependiente. Lo que es sólido: el caso semirrecta da índices $(1,0)$ (no-autoadjunción total), y el caso intervalo da una familia donde el miembro correcto codifica $\zeta$. La esperanza de "autoadjunción gratuita" muere por cualquiera de estas dos.

### Veredicto Vía 2: **MATA** (con un [GAP] menor sobre la unicidad de la condición arquimediana).
Nodo **CONOCIDO**: condiciones de borde. Es la pared clásica de Berry–Keating, no una obstrucción nueva. El programa la había encontrado como "la elección de extensión autoadjunta de $H_C$ = RH" (implícito en Phase 26, $H_C$ $Q$-simétrico pero su autoadjunción genuina $\equiv$ RH).

---

## Vía 3 — El espectro de Connes es de ABSORCIÓN, no de EMISIÓN (positividad de traza = RH)

### El argumento de muerte (forma cerrada)

Connes (*Selecta Math.* 5 (1999) 29–106, "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function") **no** construye un operador autoadjunto cuyos autovalores sean los $\gamma_\rho$. Lo que construye es:

- Una acción del grupo de clases de idèles $C_\mathbb{Q}$ sobre $L^2(X)$ (cociente adélico), con generador de escala $H_C=D$.
- Los ceros aparecen como el espectro de $H_C$ **restringido al cociente** $L^2_\delta(X)$ tras quitar la contribución de polos — y crucialmente, aparecen como **huecos** (absorción) en un espectro **continuo** de $H_C$ sobre el espacio sin restringir. Connes mismo enfatiza: es un espectro de **absorción**, "missing spectral lines", no autovalores genuinos de emisión.

**La diferencia técnica decisiva.** 
- *Emisión*: $H$ autoadjunto en un Hilbert, $\{\gamma\}$ = espectro puntual genuino, Stone aplica, RH inmediata. Esto es lo que la esperanza necesita.
- *Absorción*: $\{\gamma\}$ = conjunto de frecuencias **ausentes** del continuo, o equivalentemente polos/ceros de un coeficiente de dispersión. **No hay operador autoadjunto cuyo espectro puntual sea $\{\gamma\}$**; hay un operador (autoadjunto, sí, con espectro continuo $=\mathbb{R}$) cuya **matriz de dispersión** $S(E)$ tiene fase relacionada con $\zeta$. La realidad de los $\gamma$ NO se sigue de la autoadjunción de ese operador (que es trivial, su espectro es toda la recta).

**El golpe.** Para pasar de absorción a emisión — i.e. para convertir los huecos en autovalores genuinos de un operador autoadjunto — hace falta exactamente una **positividad**: que el "núcleo" del cociente $L^2_\delta$ sea un espacio de Hilbert genuino (norma definida positiva). Y esa positividad es, palabra por palabra, la **positividad de la distribución de la fórmula de traza de Weil** (positividad de Weil), que es **equivalente a RH** (Weil 1952; Bombieri, *Problems of the Millennium: RH*, Clay, 2000, §explicit formula; Connes 1999, donde la fórmula de traza global con el término correcto $\equiv$ positividad $\equiv$ RH es el "missing ingredient" declarado por el propio Connes).

$$
\boxed{\;\text{"absorción}\to\text{emisión"}\;\equiv\;\text{positividad del término de Weil}\;\equiv\;\text{positividad de la fórmula de traza}\;\equiv\;\text{RH}.\;}
$$

**Por qué Connes no cerró RH (la lectura adversarial):** porque su fórmula de traza es **incondicional como identidad** (vale siempre, ceros como absorción), pero el paso a un operador autoadjunto de emisión requiere probar que cierto término (el término arquimediano/de la traza local) tiene el **signo correcto** — la positividad de Weil — que es RH. Connes redujo RH a esa positividad; no la probó. El import cuántico de "Stone + onda" no añade nada a este paso: Stone necesita un operador **autoadjunto en Hilbert con espectro puntual**, y producir ese operador (emisión) **es** la positividad faltante.

### Veredicto Vía 3: **MATA.**
Nodo **CONOCIDO**: positividad de la traza de Weil. Es exactamente la razón documentada por la que Connes (1999) no concluyó RH. El import cuántico no rodea esto; lo re-encuentra.

---

## Veredicto global

**Las TRES vías matan.** Ninguna falla; ninguna deja un escape. Y — esto es lo más importante para el programa — las tres matan **por reducción a la misma obstrucción, vista desde tres caras del dado**:

| Vía | Mecanismo de muerte | Nodo de $\zeta$ | ¿Nuevo? |
|---|---|---|---|
| 1. Krein | $Q$ indefinida ($\kappa=2m$); Stone no da espectro real en Pontryagin; la única forma invariante definida $\iff$ RH | **MÉTRICA / ORIENTACIÓN** (la forma de Weil) | CONOCIDO (Phase 51 D161, Phase 52 D163-Vía1, Phase 26 κ=2m) |
| 2. Deficiencia | Generador no esencialmente autoadjunto; extensión autoadjunta = condición de borde = fase de $\zeta$ | **CONDICIÓN DE BORDE / EXTENSIÓN** | CONOCIDO (pared de Berry–Keating; autoadjunción de $H_C \equiv$ RH) |
| 3. Absorción | Connes da absorción no emisión; pasar a emisión = positividad de traza | **POSITIVIDAD DE LA TRAZA DE WEIL** | CONOCIDO (el gap declarado de Connes 1999) |

### ¿Toca $\zeta$ en un nodo NUEVO? — **NO.**

El import cuántico (Stone + ecuación de onda) **NO abre un nodo nuevo**. Es una **traducción al lenguaje de mecánica cuántica matemática** de los tres nodos ya conocidos:
- "Krein-indefinido" = la **métrica** de Phase 51 (la métrica de polarización porta $\zeta$ vía la partición del peso dual; aquí, la única forma respecto de la cual $U$ es unitaria es $Q$, indefinida salvo RH).
- "índices de deficiencia" = las **condiciones de borde** (la elección de von Neumann entre extensiones autoadjuntas $\equiv$ codificar $\zeta$ en la frontera).
- "absorción vs emisión" = la **positividad de traza** (el gap de Connes).

Estos tres nodos son, en la síntesis de Phase 52, **manifestaciones del único nodo irreducible: "$\zeta$ ES la dualidad"** (la fórmula explícita en la clase fundamental del portador ceros↔primos ES la cuenta de ceros). El import cuántico confirma el muro de Phase 52 desde el ángulo de Stone/von Neumann: cada accesorio cuántico que se añade (unitariedad, autoadjunción, evolución) revela $\zeta$ un nivel más abajo:
- añades **unitariedad** → $\zeta$ reaparece en *qué forma* se preserva (Vía 1 = métrica);
- añades **dominio/dinámica** → $\zeta$ reaparece en *qué condición de borde* (Vía 2 = frontera);
- añades **espectro discreto genuino** → $\zeta$ reaparece en *la positividad que lo discretiza* (Vía 3 = traza).

Es el mismo patrón "quita un accesorio, $\zeta$ baja un piso" de Phase 51→52, ahora con accesorios cuánticos. **El import cuántico no escapa: re-deriva el muro en vocabulario de Hilbert–Pólya.**

### ¿Qué tendría que ser verdad para que el import escapara? (lista honesta)

Para que la esperanza sobreviviera, harían falta SIMULTÁNEAMENTE:
1. **(contra Vía 1)** Un espacio de Hilbert **genuino** (forma definida positiva) RH-libre respecto del cual la evolución sea unitaria, distinto de $(L^2(C_\mathbb{Q}),Q)$. Equivale a un triple espectral cuyo $D$ **NO** sea el flujo de los primos (espectro $\neq\{\log k\}$, partición $\neq\zeta$) con Chern/signatura $=\kappa=2m$. Es el [GAP central] heredado de Phase 49 D156 §4.5 / Phase 51 D161 — **no construido, [GAP de literatura]**.
2. **(contra Vía 2)** Que la ecuación funcional **completa** (lado arquimediano + lado de Euler) determine **unívocamente** una extensión autoadjunta sin libertad RH-dependiente. [GAP] no resuelto; la evidencia (Berry–Keating) sugiere lo contrario.
3. **(contra Vía 3)** Una construcción de **emisión** (autovalores genuinos) sin pasar por la positividad de Weil. Equivale a la positividad de la traza por una vía independiente = la **hebra diofántica** (GAP-157.A / GAP 162.D), fuera del toolbox actual.

Las tres condiciones son **una sola disfrazada**: el objeto Connes/Deninger con espectro fuera de $\{\log k\}$ y partición fuera de $\zeta$. Mientras no exista, el import cuántico es circular.

---

## Mensaje final

**Cuál vía mata:** las **tres** matan, y son tres caras del mismo dado. La más limpia y fatal es la **Vía 1 (Krein)**: la unitariedad respecto de la única forma estructuralmente disponible (la de Weil $Q$) es *J*-unitariedad en un espacio de Pontryagin $\Pi_{\kappa}$ con $\kappa=2m$; el teorema de Stone **no da espectro real** ahí, y exigir que lo dé (forma definida positiva) **es** RH. Stone es un bicondicional disfrazado, no una palanca.

**Nodo de $\zeta$:** **CONOCIDO, no nuevo.** El import cuántico re-expresa los tres nodos ya cartografiados — métrica/orientación (Vía1=Phase 51 D161), condición de borde (Vía2=Berry–Keating), positividad de traza (Vía3=gap de Connes) — todos colapsando al nodo irreducible de Phase 52: **"$\zeta$ ES la dualidad"**. El vocabulario de Stone/von Neumann/Hilbert–Pólya no toca un escondite nuevo de $\zeta$; lo encuentra en los mismos tres lugares, en lenguaje cuántico.

**Tres hallazgos etiquetados:**

- **[HALLAZGO 165.A — Stone-es-bicondicional].** En el escenario de Weil/Connes, "$U(t)=e^{itH}$ unitaria $\Rightarrow$ $\operatorname{spec}(H)\subset\mathbb{R}$ (Stone)" es lógicamente **equivalente** a "$Q$ definida positiva" $\equiv \kappa=0 \equiv$ RH. La hipótesis de Stone (Hilbert genuino) ya contiene la conclusión. La unitariedad no es estructural-gratuita: es la métrica de Weil con otro nombre. Conexión exacta: el $\kappa=2m$ de Phase 26 = número de autovalores no reales del generador $J$-autoadjunto en $\Pi_\kappa$ (Bognár/Azizov–Iokhvidov), i.e. **el puente 26-C.2 ES el teorema de Stone-en-Krein aplicado.**

- **[HALLAZGO 165.B — deficiencia-bifurca].** El generador de dilataciones $-i(x\partial_x+\tfrac12)$ tiene índices de deficiencia $(1,0)$ sobre la semirrecta (autoadjunción **imposible**, Stone inaplicable de raíz) e índices $(n,n)$ sobre dominios truncados (familia de extensiones, donde la única con espectro $\{\gamma\}$ codifica la fase de $\zeta$ en su condición de borde). En ambas ramas la autoadjunción genuina **no es estructural**: o no existe, o exige conocer $\zeta$. La simetría funcional restringe la frontera (factor arquimediano $\chi$) pero **no la determina** (falta el lado de Euler) — [GAP] de unicidad declarado.

- **[HALLAZGO 165.C — absorción-es-el-gap-de-Connes].** El import cuántico colapsa al punto exacto donde Connes (1999) se detuvo: los $\gamma$ son espectro de **absorción** (huecos en un continuo), no de **emisión** (autovalores genuinos). El paso absorción→emisión = positividad de la fórmula de traza de Weil = RH. Stone exige emisión (operador autoadjunto con espectro puntual); producir emisión **es** la positividad faltante. El import no añade nada al gap de Connes: lo re-deriva. Escape único = construir emisión sin positividad de Weil = la hebra diofántica fuera del toolbox.

**Conclusión adversarial:** la esperanza de "RH por unitariedad estructural vía Stone" está **muerta**. La unitariedad estructural RH-libre existe — pero es *J*-unitariedad en Krein (Vía 1), o no fija la dinámica (Vía 2), o solo da absorción (Vía 3). Convertir cualquiera de las tres en "Hilbert + autoadjunto + emisión" es, en cada caso, exactamente RH. El import cuántico es un **espejo del muro**, no una puerta.
