# Uniones entre los papers

**Actualización vigente:** la revisión profunda reemplaza los pendientes históricos de esta tabla en los casos individualizados por [MATRIZ-UNIONES](auditoria-profunda/MATRIZ-UNIONES.md). Esa matriz distingue coincidencia textual, hipótesis y rango, prueba del input, ciclos lógicos y propagación del fallo de caracteres de P53. En particular, los anteriores (c) de mera falta de lectura de P55/P56 no siguen vigentes; la cadena local se reconstruyó, mientras la rama IM de z=1 depende del exchange defectuoso. Lo no individualizado sigue sin certificación.

La tabla de inputs del final de la sección automórfica de paper 46 (5055–5095) queda cubierta por la matriz de abajo y las comprobaciones específicas enlazadas. **No queda certificada toda la red de importaciones transitivas.** Se distingue la concordancia del enunciado importado de la prueba del enunciado y del cumplimiento de sus hipótesis en cada aplicación. Una cita mutua no prueba circularidad; la coincidencia textual tampoco prueba ausencia de ella.

## Inputs enumerados por paper 46

| Input | Origen | Concordancia comprobada | Dictamen de validez global |
|---|---|---|---|
| `au:seesaw` | 49 | El escalar es independiente del twist; el dato de cadena puede depender de él. | (c), falta certificar toda transferencia e integración. |
| `au:divis` | 49, 50 | Se mantienen excepción de nivel, truncación y pérdida de colongitud; no se afirma invariancia del subespacio ramificado por cada Hecke. | (c); argumento algebraico de 50 revisado aparte. |
| `au:count` | 49 | Se conservan las columnas anidadas y la deducción adicional en el primo ramificado. | (c), forma normal del kernel y ensamblaje. |
| `au:kernel` | 49 | Todo conjugado y la cota exponencial con `rs_j/2`. | (c), normalización exacta CM y reciprocidad. |
| `au:restrict` | 49 | Norma al cuadrado, pérdida `x^70` y término de nivel. | (c), branching integral pendiente. |
| `au:expansion` | 49 | Integralidad fuera del nivel y conductor; cota de tamaño para twist trivial. | (c), gluing y conteo. |
| `au:equiv` | 49 | Carácter tame y traslación derecha conservados. | (c), integralidad local de la traslación. |
| `au:shortbasis` | 49 | Base sobre E, no necesariamente base integral; constante `6c_0(fn)^2`. | (a) para el lema de geometría de números bajo sus hipótesis. |
| `au:moment` | 51, 52 | Tres cotas y constante `1+9b^-4` coinciden. | (c), estimaciones locales y uniformidad completas pendientes. |
| `au:mult` | 51 | Los supuestos de separación y proyección están presentes; `pm:rem-full` cubre lugares inertes. | (c), identidad orbital y justificación global de traza. |
| `au:inj` | 53, 54 | Triángulo y primer lift identificados; no se hizo comparación literal integral de todas sus entradas. | (c), realización automórfica; triángulo abstracto correcto. |
| `au:factor` | 53, 54, 51 | Se conservan twists m-fold y potencias; depende de la misma comparación de multiplicidades. | (c), exchange, factores y todas las sustituciones. |
| `au:aux` | 53 | Identificado origen en `pc:twistreduct`; comparación integral de hipótesis pendiente. | (c). |
| `au:regular` | 55, 56, 54 | R1–R3, factores `log ℓ`, denominadores y falsos lifts cotejados. | (c), Selmer, exponentes integrales y clases impares. |
| `au:onelift` | 54, 53 | Determinante comprimido, potencia `d_j` y factores independientes del twist coinciden. | (c), `po:glue` y sus antecedentes. |
| `au:hecke` | 54, 53 | `3x^35` ya propagado, no versión antigua; resto de aplicaciones de CL pendiente. | (c), test integral y comparación de normas. |

Los detalles y localizadores están en [theta y Hecke](02-theta-hecke-covolumen.md), [spanning](03-spanning.md) y [Selmer y Hodge](04-selmer-hodge.md).

## Uniones que requieren especial cuidado

**Rango de 50 hacia 49.** La igualdad del enunciado citado incluye la fracción excepcional y el término `θj`. No se puede reemplazar una colongitud truncada por una cota uniforme de todos los divisores elementales. Las sustituciones numéricas se verificaron; la realización aritmética de todos los datos queda (c).

**Retículos 49 y 51.** No son literalmente el mismo retículo. El manuscrito lo reconoce y proporciona transporte adélico y conjugación unitaria (`pb:lattice` de 51, 1027–1110; `au:two-lattices` de 46). La invariancia de normas Hilbert–Schmidt por ese transporte es correcta. Comprobarla no certifica por sí solo todos los datos de la construcción original de 49.

**52 hacia 51.** El rango incluye `ρ≥10^8` y condiciones H0–H5. La condición más débil `n≥100` no sería suficiente, pero la versión actual menciona y verifica el tamaño mayor en los datos. (R), (F), (S) usan las mismas medidas, masas y pesos; la auditoría completa de H1–H5 y de sus pruebas queda (c).

**56 hacia 55.** El texto distingue cuidadosamente exponente aniquilador de longitud del defecto: en un caso genérico sólo se obtiene la segunda. Los duales, cambios de pesos e inversión `K(s^-1)` de tipos tame están presentes. NM se verifica a partir de `λ<h^3` en la aplicación examinada. No se encontró la pérdida de hipótesis que sugeriría leer sólo el título «sin restricción Fontaine–Laffaille».

**43–45 hacia 46.** La fórmula explícita y el criterio primitivo sí coinciden, según [la revisión del marco de Weil](07-rows-a-b-c.md). Esas entradas se usan para interpretar la forma y la recíproca del criterio; no aportan la positividad que la cadena automórfica pretende demostrar.

## Inventario reproducible y límites

`evidencia/auditar_fuentes.py` genera:

- `fuentes.json`: hashes SHA-256, rutas y número de líneas de los catorce fuentes 43–46, 49–58, excluidos 47–48.
- `enunciados_compartidos.json`: texto y localizador de entornos con etiquetas compartidas.
- `uniones_textuales.tsv`: igualdad tras quitar etiquetas y normalizar espacios.
- `citas_internas.tsv`: referencias bibliográficas explícitas con claves P43–P56 o Paper43–Paper56, excluidos 47–48. No detecta claves con nombres alternativos como `Companion`.

La coincidencia de etiquetas es sólo una ayuda de navegación: etiquetas genéricas pueden nombrar resultados diferentes. Las macros también pueden cambiar de significado entre archivos. Por eso un `True` en el TSV **no es un dictamen (a)**, y un `False` no es un fallo matemático. Se inspeccionaron las diferencias de los principales inputs automórficos entre 46 y 58: las observadas son sustituciones de citas externas por referencias internas, no cambios demostrados de constante o rango.

**Estado de todas las uniones no individualizadas en las tablas:** (c), no verificado. Lo pendiente es comparar el enunciado completo, sus definiciones transitivas y la verificación de hipótesis en el lugar de aplicación. El inventario no reemplaza ese trabajo. No afirmo haber revisado semánticamente cada una de las miles de referencias de estos manuscritos.

Para cerrar la red hace falta una ficha por importación con origen, destino, correspondencia de símbolos, medidas, retículos, rango y prueba de las hipótesis de aplicación. Las fichas anteriores cubren las entradas centrales que 46 enumera; no bastan para certificar la conclusión GRH.
