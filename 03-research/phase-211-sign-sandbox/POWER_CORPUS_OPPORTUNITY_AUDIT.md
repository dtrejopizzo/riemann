# Auditoría de antecedentes y oportunidades tras la revisión de POWER

Estado: revisión estratégica, no nuevo teorema de signo. Participantes: root, casos, mapa e invariante_nuevo. No nuevos certificados ni cambios en papers.

## Alcance comprobado

Se realizaron búsquedas transversales en los archivos del índice ROUTES-TRIED-INDEX y en el corpus, contraste con el grid y el crucigrama, lectura del LEDGER C1–C51 y lectura selectiva de las fuentes primarias pertinentes y sus auditorías. No se afirma haber releído línea por línea todo el repositorio ni que la ausencia de una coincidencia de palabras pruebe novedad. Cada candidata futura requiere su propio contraste de objeto, hipótesis y conclusión.

Informe independiente complementario: `POWER_GLOBAL_ROUTE_REVIEW.md` (mapa), con fuentes primarias y alcances de cinco mecanismos globales fuera de la torre.

## Decisiones por mecanismo

| Mecanismo | Antecedentes concretos | Obstáculo verificado | Decisión actual |
|---|---|---|---|
| Densidad de escalera32+n o confluencia a tasa fija | POWER_BRIDGE_002 §6; CONFLUENT_BRIDGE_014 | Los puentes ya están probados; falta el signo en todos los tamaños | No reconstruir el puente ni presentar otra parametrización como cierre |
| Más dimensiones mediante filtros | GEOMETRIC_TRANSFER_015; FULL_THIRTEEN_053; UNIFORM_STRIP_060 | Transporte necesita toda la órbita; las colas dejan un interior creciente | No lanzar otra dimensión ni optimizar un umbral como estrategia global |
| Densidad de la unión de espacios filtrados | HIGHPASS_DIAGONAL_DENSITY_094; auditoría016 | Criterio L2 exige liminf r(n)^2/n=0; el puente de forma requiere además otra topología y cruces | No inferir densidad suficiente ni signo de una envolvente desde una unión positiva |
| Recurrencia desde el cono positivo | SCALAR_BRIDGE_017; RECURRENCE_BOUNDARY_036 §§5–7 | La energía del cono tiende a0; el resto converge exactamente al valor inicial | No repetir recurrencia sola. Una cota firmada del resto es una obligación conocida, no una oportunidad nueva sin mecanismo aritmético |
| Clase BASE o monotonías bajo Schur/Green | POWER074/081/101/111 | Falsificadores genéricos y fallos de herencia; incluso monotonía completa paramétrica no implica TP2 | Reabrir sólo con un invariante conjunto distinto, compatible con las identidades reales y preservado por cada operación |
| Continuación de MIXED4 | POWER112 §7 | El siguiente cociente finito exige una quinta función no controlada | No extender la torre por rutina. TP2 real no es TP de todos los órdenes |
| Representación positiva tipo Stieltjes/anti-Löwner | POWER083; E101_036 §§1–3,5 (N y su subordinación gaussiana literales), E101_042 §2; antecedente R162_803/D-16 | Una representación positiva bastaría, pero pedirla no construye su medida | Objetivo legítimo, sin nueva candidata identificada. Hace falta fórmula y prueba de signo independientes |
| Barrera global no lineal de defecto o continuación entre peines | BARRIER_D2_001; AUDIT_197_2 §§1–3 | Ya se estudiaron todos los defectos/caminos de la clase; el signo queda en la premisa pendiente | No recomendar sólo «hacerlo global/no lineal» como novedad. Usar la reducción auditada, no una imposibilidad universal |
| Completitud parcial fuera de una ventana | R186_005 §5; R186_092 §C | Existe una plantilla, no una selección E ni una desigualdad firmada que cierre el problema | Sólo investigación preliminar: especificar E y comprobar identificación, falsificadores y antecedentes antes de desarrollar |

## Correcciones de lectura que evitan reintentos

1. O-151.4 no es una ruta nunca desarrollada: R168_202 ya analiza las familias declaradas. La entrada antigua de06 estaba desactualizada. Esa clasificación no prueba que cualquier objeto nuevo sea imposible.
2. La recomendación antigua de06R4 de buscar una barrera global no perturbativa debe leerse junto a fase197 y AUDIT_197_2. La auditoría distingue reducciones de verdaderas imposibilidades y corrige constantes y un argumento de agudeza.
3. R186_092 corrige TB3-neg(ii): no es válido inferir «la conclusión no es estable bajo borrado, luego su derivación usa completitud». El argumento válido usa premisas estables bajo borrado: el dato truncado las satisface y por ello satisface sus consecuencias. No ampliar el NO-GO fuera de esa clase.
4. REF-D significa reformulación; no es por sí misma un criterio de exclusión. Tampoco OPEN o «no candidate» significa que exista una oportunidad concreta.

## Resultado de la auditoría y próximo filtro

Entre los mecanismos examinados no se identificó una construcción nueva ya justificada para el cierre uniforme. Esto no afirma que no exista: identifica qué no debe repetirse y dónde falta todavía un objeto.

La comprobación de E igual al conjunto de cuadrados quedó resuelta en `SQUARE_COMPLETENESS_OBSTRUCTION.md`: el extremo de reemplazar2 por4 ya figuraba enR163_102 y admite transferencia del testigo negativo007_C. La condición sobre cuadrados, incluso con conteos enteros y coeficientes logarítmicos no negativos, no basta. La misma fuente prueba un falsificador no entero para completitud simultánea en TODAS las potencias perfectas; al añadir integralidad y positividad logarítmica, esas condiciones identifican el dato original, sin demostrar su signo. No se abre una construcción basada sólo en esta condición. La sección11 añade una deformación con residuo exactamente1 y conteo acumulado x+O(1), conservando ALL-POWERS y coeficientes logarítmicos no negativos: factores en primos fuera de la ventana normalizan el residuo sin cambiar el test negativo. Esta clase sólo exige N no negativa y acotada, no N<=1 ni integralidad. No hubo nueva cuadratura ni campaña; ninguna deformación se presenta como satisfaciendo la ecuación funcional original y el NO-GO sigue limitado a las hipótesis declaradas.

El objetivo global sigue OPEN. WM y112 permanecen válidos como resultados auxiliares registrados; no aportan una ventana nueva ni autorizan extrapolación a todos los órdenes.


## Contraste adicional: calor theta, Poisson y desigualdades conjuntas

Revisión por casos e invariante_nuevo, con lectura adicional de root de E101_070 y106_110. No se abre una construcción a partir de las identidades siguientes.

- `phase-101-covariant-bordered-current/E101_070_PEARSON_THETA_CLOSURE_NO_GO.md`, §§2–5: ya contiene la representación theta de dos variables y la proyección a una jerarquía infinita con flujo de borde. Su NO-GO de Pearson sólo excluye coeficientes polinómicos escalares fijos, por los átomos interiores; no excluye cualquier ecuación no local. La identidad de calor no entrega el cierre firmado.
- `phase-106-global-modular-star-audit/106_110_HEAT_PROFILE_COVARIANCE_FLOW_AND_DISSIPATION_BUDGET.md`, §7: Poisson completo actúa mediante una isometría y conserva ambas trazas del presupuesto. Reexpresar las fuentes no modifica la desigualdad pendiente. Sería necesaria una comparación nueva entre bloques, no sólo la identidad modular.
- `phase-192-exact-identity/EI_002_LATTICE_MELLIN_IDENTITY.md`: el uso conjunto de Poisson y Euler en una identidad exacta ya fue estudiado; no es por sí mismo una cota inferior.
- `phase-196-global-object/INV_V_001_HEISENBERG_HECKE_WINDOW_AND_SHA_FORM.md`, V1.3–V1.4: la positividad que factoriza por primos sobrevive a eliminaciones; el alcance de la obstrucción es esa clase, no toda utilización de Poisson.
- `phase-195-modern-tools/INV_N_001_BAKRY_EMERY_GAMMA2_GAP_CEILING_NO_GO.md`, §3: sumar ínfimos separados del salto y del potencial no entrega la cota requerida. No excluye una desigualdad conjunta; los números auxiliares no se promueven aquí a certificados intervalares.

No se identificó en estas lecturas un primer lema nuevo que pague el signo para todos los tamaños. Tampoco se convierte esa ausencia en un NO-GO general. La condición para reabrir sigue siendo exhibir una desigualdad conjunta concreta, con objeto y coeficientes definidos, y comprobar por qué no es sólo la identidad o el presupuesto ya registrado. No se propone volver al calor o a la disminución de variaciones por cambiarles el nombre o la variable.
