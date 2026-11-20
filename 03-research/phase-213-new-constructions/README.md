# Phase 213 — New constructions for global positivity

Working memos in this folder are written in Spanish.

## Aim

Prove positivity of the full form of Paper 47 on its whole admissible carrier. This phase continues that
goal; it does not restart earlier attempts, nor does it turn the partial results of phases 211 and 212
into a global proof. The sign is treated as a problem about the explicit form, without reasoning from
equivalences with other targets (sandbox). Elementary mathematics is preferred; small computations are
used only for concrete checks, and a sample never proves all orders.

Definitions: `../phase-211-sign-sandbox/STATEMENT_001.md` and Paper 47. The specification and
restrictions of `../phase-212-missing-object/OBJECT_SPEC.md` and `../phase-212-missing-object/RULES_AVOID.md`
remain references, with the scopes and corrections recorded in the current master index. No paper is
modified without the global proof.

## Status

- **Global positivity of the full form: OPEN.**
- Each `ROUND_*` memo states its own claim, proof or precise defect, scope and label (PROVED,
  CONDITIONAL, OPEN, NO-GO with class, NUMERICAL, CITED or ARGUED). PROVED requires a complete proof and
  independent review. None of the rounds closes global positivity.
- Results 212-95-A/B (in `../phase-212-missing-object/ROUND_095_A.md`, `ROUND_095_B.md`) refute PSD of
  J_sc and every repair J_sc + cA with fixed c; they do not refute the full form nor supply the missing
  compensation. That repair is not retried here.
- The record of every attempt (antecedent, difference, result, what worked, what failed, reopening
  condition, file) is in `05-meta-and-planning/ROUTES-MASTER-INDEX.md`, Part V.

## Before any construction

Consult `../../05-meta-and-planning/ROUTES-MASTER-INDEX.md` (especially Parts VII, VI and V), Paper 48 and
the relevant primary sources. Failed paths are not repeated or renamed; a variant is considered only if it
introduces a distinct mathematical operation and explains why it does not reproduce the earlier
obstruction. Changing dimension, threshold, basis, parameters or representation is not enough.

Each candidate specifies, before derivations:

1. The closest antecedent, with file and section.
2. The concrete operation and mathematical claim that are different.
3. Which difficulty of the antecedent that difference avoids, and why.
4. The precise identity or inequality connecting the attempt with the full form and all its orders; for an
   auxiliary falsifier, which useful class of proposals it would decide.

An independent review checks this comparison before building. Absolute novelty is not promised.

## Contents

- `ROUND_nnn_A.md` (plus `ROUND_001_B.md` and `ROUND_012_B.md`) — rounds 001–416: comparison, statement, proof or
  precise defect, scope and next step (full list below).
- `SELECTION_nnn.md` — selection-gate records (candidates examined before construction).
- `AUDIT_370_PHASE.md` — verification of the phase transfer in round 370.
- `SADDLE_FIXED_POWER_CALIBRATION.md` — saddle calibration for a fixed cut in powers of log x (used by
  round 390).
- `verify_*.py`, `verify_dyadic_gcd_subtotal.cpp`, `check_4944_blocks.py`, `probe_dilation_lp.py` — small
  verification scripts, each cited by the round with the same number or topic.

## Suggested reading order

1. This README and the Part V entries of the master index for phase 213.
2. `ROUND_001_A.md`, `ROUND_001_B.md`, then the `SELECTION_*` records.
3. Rounds in numerical order; the index below gives each title.

## Running the scripts

Python 3 with `numpy`, `scipy`, `mpmath` and `python-flint` (Arb); run from this folder, e.g.
`python3 verify_189.py`. The C++ check compiles with `g++ -O2 verify_dyadic_gcd_subtotal.cpp -o v && ./v`.
Outputs validate specific points of the corresponding memo; they are not proofs of the global sign.

## Full index of rounds and selection records

- `ROUND_001_A.md` — Alcance de la equivalencia de inercia del sector par
- `ROUND_001_B.md` — Alcance de la desigualdad PRIME–ARCH recuperada de fase138
- `ROUND_006_A.md` — Una cola superior negativa en la matriz física de celdas
- `ROUND_007_A.md` — Pérdida del mayorante de Poisson bajo dilatación de celdas
- `ROUND_010_A.md` — Combinaciones de traslaciones próximas de un perfil escalonado
- `ROUND_011_A.md` — Dos tubos de saltos distantes impiden un piso uniforme para restos libres
- `ROUND_012_A.md` — Control del cruce aritmético ligado por el módulo de traslación
- `ROUND_012_B.md` — Límite de energía para una mezcla suave fija de traslaciones de BUILD084
- `ROUND_013_A.md` — Separación uniforme de cabeza y cola para mezclas de variación total acotada
- `ROUND_014_A.md` — Dos traslaciones con coeficientes arbitrarios y un radio común a todo k
- `ROUND_015_A.md` — Todos los coeficientes firmados en la escala de la celda lejana
- `ROUND_016_A.md` — Traslaciones firmadas sobre un número creciente de anchos de celda
- `ROUND_017_A.md` — Absorción del cruce por las dos energías localizadas
- `ROUND_018_A.md` — Recuperación de la energía completa por dos correctores remotos
- `ROUND_020_A.md` — Cabeza en dos celdas y cola arbitraria en una banda creciente
- `ROUND_021_A.md` — Un solo canal de posible negatividad en una banda de longitud proporcional a K
- `ROUND_022_A.md` — Varianza del cruce aritmético que toleraría el signo global
- `ROUND_023_A.md` — Coste de tomar valores absolutos entre dos bandas
- `ROUND_024_A.md` — Norma del cruce después de cancelar dentro de las ternas
- `ROUND_025_A.md` — Coercividad en una fracción de dimensiones que tiende a uno
- `ROUND_026_A.md` — Conteo espectral en el corte completo de celdas
- `ROUND_028_A.md` — Transferencia de un test negativo a la otra paridad por traslaciones
- `ROUND_029_A.md` — La recta de la meseta como criterio global
- `ROUND_030_A.md` — Un perfil de meseta fijo detectaría anchos arbitrariamente grandes
- `ROUND_031_A.md` — Umbral polinómico para un contraejemplo en celdas
- `ROUND_032_A.md` — Error uniforme al sustituir sólo la cola de primos por densidad continua
- `ROUND_033_A.md` — Límite del defecto normalizado en las matrices completas de celdas
- `ROUND_034_A.md` — Condición de borde de un extremizador negativo
- `ROUND_036_A.md` — Ceros de Mellin de un posible extremizador negativo
- `ROUND_037_A.md` — Un solo test compacto para todos los centros del primer filtro
- `ROUND_038_A.md` — Norma traza de la cola y traza exacta de la forma aritmética completa
- `ROUND_039_A.md` — Un criterio aritmético unilateral en las cuartas potencias
- `ROUND_041_A.md` — Pérdida óptima de un minorante divisorial positivo a escala variable
- `ROUND_042_A.md` — Un minorante explícito con un único corrector de criba
- `ROUND_043_A.md` — Cuánta inclusión-exclusión exige el valor de la criba original
- `ROUND_044_A.md` — Una desigualdad local en los primos equivalente al criterio de 039
- `ROUND_045_A.md` — El coste de reproducir la banda con una suma divisorial
- `ROUND_046_A.md` — El déficit se localiza en los primeros j−1 términos de la cuadratura
- `ROUND_047_A.md` — Un peso fijo con sólo O((log x)²) muestras exteriores pendientes
- `ROUND_048_A.md` — El criterio pendiente como una suma finita alternada
- `ROUND_049_A.md` — Criterio con dos factores de tamaño próximo a la raíz
- `ROUND_050_A.md` — Productos con parte libre de cuadrados pequeña
- `ROUND_051_A.md` — Cancelación firmada en filas cuyo primo se repite en el segundo factor
- `ROUND_052_A.md` — Cortar por la parte libre de cuadrados y una subsuma positiva después de emparejar
- `ROUND_053_A.md` — Dónde se compensa el término positivo de 052 en las filas 3L<p<4L
- `ROUND_054_A.md` — Segunda diferencia de escalas y eliminación de todas las filas pequeñas
- `ROUND_055_A.md` — Qué detectan las clases de residuos en el criterio de 054
- `ROUND_056_A.md` — Un criterio cuadrático de Möbius fuera de la diagonal
- `ROUND_057_A.md` — Cancelación de la diagonal por cocientes racionales en la forma de 056
- `ROUND_058_A.md` — El corte por tamaño de los cocientes da excesos de ambos signos
- `ROUND_059_A.md` — Un centro que anula el término principal en todos los cocientes
- `ROUND_060_A.md` — Promediar escalas cuartas elimina la condición de libre de cuadrados en cada pendiente
- `ROUND_061_A.md` — Hasta dónde se pueden retirar las pendientes sumando sus módulos
- `ROUND_062_A.md` — Compensación firmada en la banda de semiprimos de 061
- `ROUND_063_A.md` — Un único promedio para las bandas de toda anchura logarítmica fija
- `ROUND_064_A.md` — Banda de semiprimos con anchura superlogarítmica
- `ROUND_065_A.md` — Suma sobre filas con el corte pq ≥ L
- `ROUND_066_A.md` — Dos cortes de signo opuesto para el total de semiprimos
- `ROUND_067_A.md` — El sector completo de semiprimos excede la escala raíz tras cualquier número finito de diferencias
- `ROUND_068_A.md` — Una copia de cada producto reducido admite una cota inferior a la escala raíz
- `ROUND_069_A.md` — Filas de numerador reducido hasta potencias menores que la raíz
- `ROUND_070_A.md` — Qué filas completas se pueden pagar según su cofactor de primos grandes
- `ROUND_071_A.md` — En la frontera crítica las filas de cada signo exceden el margen raíz
- `ROUND_072_A.md` — Compensación firmada entre dos sectores complementarios de filas completas
- `ROUND_073_A.md` — El coste de todas las potencias primas compuestas en una recurrencia para el criterio completo
- `ROUND_074_A.md` — Basta una suma sobre primos y su escala logarítmica es necesaria en ambos sentidos
- `ROUND_075_A.md` — Qué se pierde al cortar la suma prima de 074 antes de centrarla
- `ROUND_076_A.md` — Un bloque fijo puede contener todo el criterio; también hay detección en el interior
- `ROUND_077_A.md` — Regularidad de los minimizadores y módulo de potencia para el fondo completo
- `ROUND_078_A.md` — Jensen en la frecuencia recíproca: piso exacto para el complemento de celdas
- `ROUND_079_A.md` — Cota uniforme del bloque cruzado y encierro explícito del mínimo completo
- `ROUND_080_A.md` — Corrección de Schur dependiente de los saltos de cada vector
- `ROUND_081_A.md` — Coste inevitable de separar el peine del símbolo arquimediano en el complemento
- `ROUND_082_A.md` — Energía necesaria para que sobreviva el coste exponencial del peine
- `ROUND_083_A.md` — Positividad del exponencial truncado y anchura de la franja de ceros
- `ROUND_084_A.md` — Trece tasas rápidas con el corte físico de cualquier ventana
- `ROUND_085_A.md` — Todas las dimensiones y ventanas con una suma acotada de tasas recíprocas
- `ROUND_086_A.md` — La suma de recíprocos es exactamente la semilongitud de la ventana límite
- `ROUND_087_A.md` — Un solo listado de polos: comparación bilateral con la ventana efectiva
- `ROUND_088_A.md` — Dos orientaciones: umbral exacto para encender el exponencial reflejado
- `ROUND_090_A.md` — Detección simultánea en una familia de pasos
- `ROUND_091_A.md` — El cosh con tasa 1/2 detecta un extremo alcanzado en toda rejilla
- `ROUND_093_A.md` — Una desigualdad de prefijos sin parámetro continuo
- `ROUND_094_A.md` — Sólo los cruces descendentes pueden albergar un máximo que viole el techo primo
- `ROUND_095_A.md` — Tamaño de los excesos en los cruces originales si hay un extremo alcanzado
- `ROUND_097_A.md` — Ganancia máxima al permitir compuestos coprimos dos a dos
- `ROUND_100_A.md` — Un corte conservativo para repartos que dependen de la escala
- `ROUND_101_A.md` — Mayoración sólo en muestras primas con repartos dependientes de x
- `ROUND_102_A.md` — Cuánto del coste de los cuadrados admite un certificado por divisibilidad
- `ROUND_103_A.md` — Los cubos deciden el contacto en el umbral de cobertura de cuadrados
- `ROUND_104_A.md` — Basta la banda prima superior a cualquier potencia fija menor que uno
- `ROUND_105_A.md` — Un techo sin tolerancia en una banda de razón cuatro
- `ROUND_106_A.md` — Ningún peso positivo de banda suficientemente estrecha admite el techo de su integral
- `ROUND_107_A.md` — Un peso de razón exp(0.88) con techo igual a su integral
- `ROUND_108_A.md` — Restricción conjunta de los armónicos del primer cero sobre el techo primo
- `ROUND_109_A.md` — Una desigualdad local que sólo hay que probar en centros primos
- `ROUND_110_A.md` — Sólo los centros con balance local de masas necesitan una cota recíproca
- `ROUND_111_A.md` — Techo primo certificado en un intervalo continuo y comparación con el filtro
- `ROUND_112_A.md` — Cota incondicional en todas las escalas entre 10¹⁰ y 10¹² para 109
- `ROUND_113_A.md` — El techo primo de 109 vale en todo el intervalo real desde 2 hasta 10¹²
- `ROUND_114_A.md` — Cola absolutamente controlada desde la altura de la raíz cuarta
- `ROUND_115_A.md` — Detección en cada intervalo de potencias sin máximo de partes reales
- `ROUND_116_A.md` — Intervalos largos de exceso y muestreo en una sucesión de bandas
- `ROUND_117_A.md` — Techo para el mínimo completo con masa local posiblemente no acotada
- `ROUND_118_A.md` — Ley exacta del fondo con una penalización de derivadas que puede tender a cero
- `ROUND_119_A.md` — La tasa exacta en matrices explícitas sin penalización
- `ROUND_120_A.md` — Cuántos datos de la matriz par bastan en cada ventana
- `ROUND_121_A.md` — Qué bloque aritmético conserva la tasa de la matriz completa
- `ROUND_122_A.md` — Detección con frecuencia máxima fija para cada exponente inferior
- `ROUND_123_A.md` — Interpolación del peine primo en los nodos cuartos
- `ROUND_124_A.md` — Qué pierde la masa sola entre dos cuartas potencias
- `ROUND_125_A.md` — Las masas de los primos verdaderos entre cuartas potencias conservan la tasa
- `ROUND_126_A.md` — Oscilaciones de Chebyshev sin peso en nodos dispersos
- `ROUND_127_A.md` — Signo eventual de la media firmada de los primoriales en las cuartas potencias
- `ROUND_129_A.md` — El resto factorial centrado desciende por debajo de la raíz
- `ROUND_130_A.md` — Supresión bilateral de escalas en el resto factorial
- `ROUND_131_A.md` — Una banda prima alrededor de la raíz cúbica
- `ROUND_132_A.md` — Una falla exige excursiones simultáneas de θ y de Mertens
- `ROUND_133_A.md` — Exponente exacto de la oscilación local de Mertens en cada banda de potencias
- `ROUND_134_A.md` — Bandas elegidas por un cruce armónico de Möbius
- `ROUND_135_A.md` — La oscilación máxima tiene escala raíz en una ventana trasladada típica
- `ROUND_136_A.md` — El anclaje con signos multiplicativos y el sector de dos primos reales
- `ROUND_137_A.md` — Un falsificador multiplicativo fijo con defecto de inversión arbitrariamente pequeño
- `ROUND_138_A.md` — Transferencia en la escala crítica del defecto de inversión
- `ROUND_139_A.md` — El borde de Liouville es lineal en la raíz con error uniforme
- `ROUND_140_A.md` — Un peso positivo de Möbius calculable con tres sumas de Liouville
- `ROUND_141_A.md` — Dos pesos positivos y una contribución de Möbius de signo determinado
- `ROUND_142_A.md` — Frecuencia de los cruces del nivel crítico
- `ROUND_143_A.md` — Frecuencia de los cambios de signo del momento crítico
- `ROUND_144_A.md` — Un solo criterio de signo para una media corta de Liouville
- `ROUND_145_A.md` — Un promedio completo de Liouville con signo incondicional y frontera de varianza
- `ROUND_146_A.md` — Un promedio positivo de Liouville con varianza uniformemente acotada
- `ROUND_147_A.md` — Un detector completo con la misma densidad límite que el promedio ya firmado
- `ROUND_148_A.md` — Un intervalo de grados certificado dentro de un criterio que detecta todos los ceros
- `ROUND_149_A.md` — Qué pendientes polinómicas se pueden certificar tras cancelar las ordenadas verificadas
- `ROUND_150_A.md` — Un promedio positivo fijo que conserva los polos de la suma de Liouville
- `ROUND_151_A.md` — Qué parte de la corrección impar escapa a la altura verificada
- `ROUND_152_A.md` — Deriva de los cuadrados en la corrección impar
- `ROUND_153_A.md` — Un techo de densidad para enteros cuya parte libre de cuadrados es prima
- `ROUND_154_A.md` — El déficit logarítmico de 153 es la masa exacta de los cuadrados perfectos
- `ROUND_155_A.md` — Cuánto se pierde al promediar el conteo completo sobre divisores
- `ROUND_156_A.md` — Qué afirmación exacta puede probar un número finito de momentos de divisores
- `ROUND_157_A.md` — Signo del error de cuadratura para la suma interior de divisores
- `ROUND_158_A.md` — La resta del peso elemental conserva el error crítico por unidad de inclinación
- `ROUND_159_A.md` — Un peso plano que supera la barrera gaussiana del prefijo y conserva la detección
- `ROUND_160_A.md` — Retirar las potencias primas pequeñas con sus dos sumas interiores completas
- `ROUND_161_A.md` — Dos contribuciones de signo determinado en la banda de 160
- `ROUND_162_A.md` — Qué correlación de primos simples necesita la banda
- `ROUND_163_A.md` — El bloque cercano es positivo incluso a distancia logarítmica
- `ROUND_164_A.md` — Hasta dónde llega la negatividad del bloque lejano
- `ROUND_165_A.md` — Medir el umbral del bloque lejano en una escala individual
- `ROUND_166_A.md` — Un criterio en una familia de bloques de densidad cero en la variable logarítmica
- `ROUND_167_A.md` — Precisión crítica de los pesos en los primos reales
- `ROUND_168_A.md` — Cuánta exactitud de la identidad de divisores exige el criterio de energía
- `ROUND_169_A.md` — Un defecto escaso invisible en el eje real y en cualquier lista finita de momentos en uno
- `ROUND_170_A.md` — Masa negativa mínima de un certificado truncado del paper 47
- `ROUND_171_A.md` — Radio del certificado y desplazamiento de una lista finita
- `ROUND_172_A.md` — Una extensión firmada para todos los ceros con costo ponderado sumable
- `ROUND_173_A.md` — Transferir la cola verificada a una cota en norma L²
- `ROUND_174_A.md` — Un umbral finito de verificación que basta para positividad estricta en cada ventana fija
- `ROUND_175_A.md` — Positividad estricta de la forma completa hasta T=6/5
- `ROUND_176_A.md` — Ley de altura suficiente para ventanas crecientes
- `ROUND_177_A.md` — El costo de altura usa la norma del peine comprimido
- `ROUND_178_A.md` — Positividad estricta de la forma completa hasta T=21/10
- `ROUND_179_A.md` — Positividad estricta hasta T=5/2 mediante una cota directa de fuga Fourier
- `ROUND_180_A.md` — Un cuarteto por encima de la altura puede costar (1+o(1))exp T
- `ROUND_181_A.md` — Signo de la forma verdadera en casi todas las modulaciones a la altura de 180
- `ROUND_182_A.md` — Margen en dos modulaciones vecinas en toda la banda de 181
- `ROUND_183_A.md` — Ley de masa necesaria para saturar el peine en la banda crítica
- `ROUND_184_A.md` — Alineación casi total en un intervalo multiplicativo de primos
- `ROUND_185_A.md` — Qué tamaño debe tener una muestra que detecte desalineación en toda la banda
- `ROUND_186_A.md` — Separación de las frecuencias que exige 184
- `ROUND_187_A.md` — Test suficiente de negatividad a una sola frecuencia en la banda crítica
- `ROUND_188_A.md` — El error lineal del test 187 se realiza con ambos signos
- `ROUND_189_A.md` — Positividad estricta de la forma completa hasta T=129/50
- `ROUND_190_A.md` — Positividad estricta hasta 131/50 con un filtro de Chebyshev
- `ROUND_191_A.md` — Positividad de la forma completa hasta T=67/25
- `ROUND_192_A.md` — Positividad estricta hasta T=68/25
- `ROUND_193_A.md` — Forma completa hasta T=553/200 con máscara plana en el extremo alto
- `ROUND_194_A.md` — De la ventana estricta a bloques de potencias de orden creciente y tasas desiguales
- `ROUND_195_A.md` — Corolario de 086–087 para el bloque sin recorte físico
- `ROUND_196_A.md` — Un polo que permanece fijo deja una cola en el problema límite
- `ROUND_197_A.md` — Cancelación exacta en la tasa crítica de la cola y una ventana común para toda tasa
- `ROUND_198_A.md` — Ventana arbitraria corta seguida de tres colas de tasas arbitrarias
- `ROUND_199_A.md` — Cuatro colas en una ventana común, incluso en colisiones parciales
- `ROUND_200_A.md` — Un bloque de dimensión arbitraria con cuatro tasas libres
- `ROUND_201_A.md` — Positividad para hasta 32 polos reales arbitrarios en todo el rango admisible
- `ROUND_202_A.md` — Muestreo cuadrático del numerador: hasta 4096 polos reales sin restricciones adicionales
- `ROUND_203_A.md` — Hasta 72 000 polos y altura suficiente cuadrática en el orden
- `ROUND_204_A.md` — Altura suficiente lineal y 500 millones de polos reales
- `ROUND_205_A.md` — Un cono completo en la tabla escalar y 10¹⁵ filas enteras
- `ROUND_206_A.md` — Para cerrar el puente bastaría el signo eventual sobre cada rayo diádico fijo
- `ROUND_207_A.md` — Una sola diagonal de POWER con tasa variable: intervalo exacto de detección
- `ROUND_208_A.md` — Suma prima centrada y finita que conserva el crecimiento de la diagonal
- `ROUND_209_A.md` — Perfil de cada cero verificado en una suma finita de primos sin centrar
- `ROUND_210_A.md` — Un promedio cuadrático primo sin parámetro libre mide el desplazamiento relativo máximo
- `ROUND_211_A.md` — Distribución de la masa diagonal en el criterio 210
- `ROUND_212_A.md` — Umbral de estabilidad del corte primo a escala lineal
- `ROUND_213_A.md` — El centrado cambia la estabilidad del corte crítico
- `ROUND_214_A.md` — En qué frecuencias del parámetro de tasa vive una posible violación del signo
- `ROUND_215_A.md` — Una banda de frecuencia de ancho uno detecta el ángulo extremo sin conocerlo
- `ROUND_216_A.md` — Coste exacto de separar los primos después de la oscilación de Mellin
- `ROUND_217_A.md` — Una sola muestra por orden, sin órdenes excepcionales
- `ROUND_218_A.md` — Cancelación obligatoria entre dos sumas ya firmadas de primos
- `ROUND_219_A.md` — Qué exige centrar y controlar por separado los extremos de 218
- `ROUND_220_A.md` — Balance incondicional y frecuencia condicional de las excursiones de signo
- `ROUND_221_A.md` — Los datos de conteo hasta x^(1/2+o(1)) permiten programar muestras en una perturbación sobre los mismos primos
- `ROUND_222_A.md` — Una escala de estabilidad para la muestra prima
- `ROUND_223_A.md` — La constante de estabilidad de 222 es exacta para perturbaciones sobre los primos
- `ROUND_224_A.md` — Un cambio de orden elimina la inestabilidad de 221 para una familia que sigue detectando todo el signo
- `ROUND_225_A.md` — Un modelo sobre celdas logarítmicas con datos enteros y error subexponencial
- `ROUND_226_A.md` — Conservar momentos exactos de cada celda no basta si su número crece sin tasa
- `ROUND_227_A.md` — Qué puede aportar un subconjunto de primos auténticos con pesos inalterados
- `ROUND_228_A.md` — Un promedio de cuadrados en la variable aritmética mide el desplazamiento horizontal absoluto
- `ROUND_229_A.md` — Diagnóstico sin núcleo: el error ordinario en cada banda de potencias
- `ROUND_230_A.md` — La media cuadrática en cualquier intervalo de razón fija detecta el desplazamiento completo
- `ROUND_231_A.md` — Detección local con primos simples después de ajustar una recta
- `ROUND_232_A.md` — Separación del coste de los huecos y una identidad con pesos sólo en primos
- `ROUND_233_A.md` — El promedio sobre direcciones modulares cumple el techo; la paridad obstruye trasladarlo a la dirección original
- `ROUND_234_A.md` — Por qué tampoco sirven los inversos impares pequeños y qué conserva una corrección por clases
- `ROUND_235_A.md` — Sólo los primeros η log q modos del orden original detectan el exponente completo
- `ROUND_236_A.md` — Un único coseno al variar el intervalo, y una subsucesión de falsos negativos
- `ROUND_237_A.md` — Ventanas de tamaño X^(2/3) donde la primera componente ya pasa el techo, incondicionalmente
- `ROUND_238_A.md` — La cancelación de incrementos alarga las ventanas de coste pequeño
- `ROUND_239_A.md` — Un mismo conteo suavizado con ajuste creciente en dos escalas casi lineales
- `ROUND_240_A.md` — Ley de transición para el ajuste polinómico de un conteo primo compacto
- `ROUND_241_A.md` — Prueba discreta con pesos binomiales y sin término continuo
- `ROUND_242_A.md` — Bastan muestras buenas dispersas en el bloque de dos conteos
- `ROUND_243_A.md` — Un nodo exacto a la escala detectora y bloques buenos en extremos del conteo primo
- `ROUND_244_A.md` — Cuántos nodos pequeños admitiría una recta extrema con ceros
- `ROUND_245_A.md` — Dos incrementos de un promedio positivo con datos de primos anteriores
- `ROUND_246_A.md` — Las dos lecturas tienen signo y término principal en un intervalo de pendientes
- `ROUND_247_A.md` — Un baricentro de primos con pesos lineales y mínimo en extremos primos
- `ROUND_248_A.md` — El baricentro queda del lado positivo hasta 10^20
- `ROUND_249_A.md` — Cuánto futuro admite el baricentro usando sólo los primos ya conocidos
- `ROUND_250_A.md` — Bloques de longitud p^a que conservan el baricentro al perder primos
- `ROUND_251_A.md` — Borrados dispersos y el coste de invertir el baricentro
- `ROUND_252_A.md` — Un producto regular y sin ceros a través de la recta que cambia el baricentro
- `ROUND_253_A.md` — Positividad simultánea de todos los momentos logarítmicos hasta s=9·10^24
- `ROUND_254_A.md` — Frontera exacta de todos los órdenes y tamaño del primer orden negativo
- `ROUND_255_A.md` — Una fila de diferencias finitas, con signo certificado hasta el orden 2^G
- `ROUND_256_A.md` — Un presupuesto de 1/3 para una suma finita de aportes primos positivos
- `ROUND_257_A.md` — Presupuesto positivo que sólo usa primos entre x y 2x
- `ROUND_258_A.md` — Pérdida óptima de los acarreos binomiales positivos en una octava
- `ROUND_259_A.md` — Restas binomiales para la octava: construcción y coste necesario
- `ROUND_260_A.md` — Qué parte de un binomial llega a los átomos primos de la octava
- `ROUND_261_A.md` — Binomiales enteros exactos y coste de su representación firmada
- `ROUND_262_A.md` — Ajuste en potencias primas: un escalar sustituye las ecuaciones compuestas
- `ROUND_263_A.md` — Corregir una unidad de masa a coste que tiende a cero
- `ROUND_264_A.md` — Corrección explícita con ganancia de al menos orden log log N
- `ROUND_265_A.md` — La corrección de potencias propias de un binomial, incluso en repartos decrecientes
- `ROUND_266_A.md` — Diferencias de filas con un extremo común
- `ROUND_267_A.md` — Una sola cima binomial reproduce la octava y amortigua los átomos pequeños
- `ROUND_268_A.md` — Separación necesaria de los extremos binomiales en un ajuste de coste de raíz
- `ROUND_269_A.md` — Un conjunto explícito de extremos basta para toda la representación calibrada
- `ROUND_270_A.md` — Coste óptimo para comprimir universalmente a un número fijo de extremos
- `ROUND_271_A.md` — Reparación por cadenas: sólo los primos mayores que √N requieren interpolación
- `ROUND_272_A.md` — Ajuste calibrado incondicional en todos los módulos por encima del corte de raíz
- `ROUND_273_A.md` — Interpolación calibrada a ambos lados de una banda de módulos
- `ROUND_274_A.md` — Una banda de razón logarítmica al cuadrado para el ajuste binomial calibrado
- `ROUND_275_A.md` — Un mismo peso para el signo unilateral en la octava y el residuo firmado de la banda
- `ROUND_276_A.md` — En los propios primos de la banda el error absoluto supera el presupuesto de raíz
- `ROUND_277_A.md` — Los dos signos de la banda se equilibran con un error relativo cuantificado
- `ROUND_278_A.md` — La parte con divisores pequeños ya satisface la cota de raíz
- `ROUND_279_A.md` — El exponente exacto de la masa absoluta en la banda
- `ROUND_280_A.md` — Un máximo sobre muestras prefijadas mide el exponente de los ceros
- `ROUND_281_A.md` — La diagonal de las muestras, incluidas las dos calibraciones, ya cuesta raíz
- `ROUND_282_A.md` — Los pares que comparten un divisor grande ya cumplen la cota de raíz
- `ROUND_283_A.md` — En una subsucesión incondicional desaparecen las dos colas infinitas
- `ROUND_284_A.md` — Hay un cruce auxiliar en cada intervalo de razón fija suficientemente grande
- `ROUND_285_A.md` — Una banda de Möbius de razón tendiente a uno basta para detectar un cero exterior
- `ROUND_286_A.md` — Bandas favorables probadas para μ y un falsificador multiplicativo del salto de longitud
- `ROUND_287_A.md` — Para los incrementos ordinarios de Möbius basta controlar una dirección
- `ROUND_288_A.md` — Mayorante unilateral para la paridad de Möbius y su primer fallo
- `ROUND_289_A.md` — Ensanchar el filtro con reparación local: ganancia logarítmica y barrera semiprima
- `ROUND_290_A.md` — Separación por congruencias de los divisores cercanos y coste mínimo de rango
- `ROUND_291_A.md` — El carácter principal a frecuencia fija oscila demasiado; se puede retirar del promedio completo
- `ROUND_292_A.md` — Qué hipótesis exigiría acotar un carácter no principal y cómo eliminar la condición auxiliar
- `ROUND_293_A.md` — Qué cofactores pueden retirarse a coste de raíz de la autoconvolución
- `ROUND_294_A.md` — Signo del bloque con un primo mayor que la raíz y cancelación con el complemento
- `ROUND_295_A.md` — Un corte próximo a la raíz equilibra el bloque sin primo grande a precisión de raíz
- `ROUND_296_A.md` — Dos cortes monótonos y el número de primos que los separa
- `ROUND_297_A.md` — Cuántos cortes independientes de la frecuencia permiten equilibrar el bloque
- `ROUND_298_A.md` — Muestreo del saldo en frecuencias donde el bloque suave vale exactamente cero
- `ROUND_299_A.md` — Una frecuencia explícita y el primer orden que detecta cada cero
- `ROUND_300_A.md` — Inversión positiva por dilataciones para la discrepancia impar de la primera fila
- `ROUND_301_A.md` — Familias positivas mayores que la raíz después de sumar todas sus partes cuadradas
- `ROUND_302_A.md` — Signo del bloque completo con un primo grande al acercarse a la frecuencia cero
- `ROUND_303_A.md` — Un corte macroscópico deja el bloque de primos grandes acotado por una constante
- `ROUND_304_A.md` — La primera fila admite cortes equilibrados con cofactores arbitrariamente grandes
- `ROUND_305_A.md` — Barrera para el corte equilibrado por encima de la raíz
- `ROUND_306_A.md` — El signo en cortes logarítmicos fijos detecta cualquier cero exterior
- `ROUND_307_A.md` — El extremo k=4 falla incondicionalmente, con oscilación mayor que el término principal
- `ROUND_308_A.md` — Cruces efectivos más allá de la cuarta potencia por un factor doblemente logarítmico
- `ROUND_309_A.md` — Una media positiva del saldo completo mantiene el techo de raíz tras cribar los divisores
- `ROUND_310_A.md` — Una criba positiva aísla la escala principal hasta cualquier umbral subpotencial
- `ROUND_311_A.md` — Recorte simultáneo de los argumentos grandes y pequeños en la media cribada
- `ROUND_312_A.md` — Signo negativo de la media cribada en intervalos relativos decrecientes
- `ROUND_313_A.md` — Signo negativo con un hueco creciente y pesos positivos fuera del hueco
- `ROUND_314_A.md` — Signo simultáneo en el espacio completo de coeficientes de divisores
- `ROUND_315_A.md` — Coste inevitable de las dos orientaciones del saldo para toda la matriz de divisores
- `ROUND_316_A.md` — Tres dilataciones cancelan el tramo de argumentos hasta una potencia fija
- `ROUND_317_A.md` — Corte en la raíz por dos convoluciones sucesivas de orden uno
- `ROUND_318_A.md` — Corte en X^(2/3) con error cuadrático medio suficiente para el signo global
- `ROUND_319_A.md` — Reducción a índices menores que una potencia arbitraria con observación local
- `ROUND_320_A.md` — Banda polilogarítmica con promedios locales positivos recombinables
- `ROUND_321_A.md` — El operador corto es pequeño en media de frecuencias, pero no admite contracción uniforme
- `ROUND_322_A.md` — Contracción uniforme del multiplicador observado en una franja explícita
- `ROUND_323_A.md` — Contracción en rectángulos de altura verificada mediante pesos explícitos de Taylor
- `ROUND_324_A.md` — Localización hasta la recta crítica sin suponer ceros simples
- `ROUND_325_A.md` — Una energía de pares próximos mide exactamente la abscisa extrema de los ceros
- `ROUND_326_A.md` — Cuándo la proximidad de los pares paga por sí sola el presupuesto
- `ROUND_327_A.md` — Cancelación relativa demostrada en la banda de pares que aún exige cancelación exponencial
- `ROUND_328_A.md` — La diagonal domina incluso al ensanchar la ventana crítica
- `ROUND_329_A.md` — Ahorro de toda potencia en la energía central de Möbius
- `ROUND_330_A.md` — Un contramodelo multiplicativo conserva los signos y todos los ahorros polinómicos
- `ROUND_331_A.md` — Recorte por divisor común en la energía de pares próximos
- `ROUND_332_A.md` — La clase de cocientes primitivos ya tiene toda la tasa absoluta
- `ROUND_333_A.md` — Cancelación simultánea en las clases de máximo común divisor exacto
- `ROUND_334_A.md` — Separar por máximo común divisor conserva la tasa que detecta los ceros
- `ROUND_335_A.md` — Umbral de los pesos en el divisor común
- `ROUND_336_A.md` — El coste exacto fuera de la diagonal, incluso con peso igual al mcd
- `ROUND_337_A.md` — Detección de la abscisa por una media local sin los pesos de Taylor
- `ROUND_338_A.md` — Dos copias del mismo bloque de Möbius en la media local
- `ROUND_339_A.md` — Una fase logarítmica compartida sobrevive al cuadrado del bloque
- `ROUND_340_A.md` — Un único subbloque aislado con los signos verdaderos ya exige RH
- `ROUND_341_A.md` — Cota puntual para todos los cocientes reducidos de altura pequeña en 338
- `ROUND_342_A.md` — Una segunda dilatación cancela la densidad de cada cociente por separado
- `ROUND_343_A.md` — El residuo de cocientes grandes en un rectángulo aislado aún detecta RH
- `ROUND_344_A.md` — Qué términos compensan el rectángulo aislado
- `ROUND_345_A.md` — Qué saldo tienen las primeras filas que sobreviven a la inversión
- `ROUND_346_A.md` — Compensación entre bandas en dos familias de productos impares
- `ROUND_347_A.md` — Emparejamiento entre productos impares distintos en el observable completo
- `ROUND_348_A.md` — Emparejamiento disjunto de masa comparable a toda la ventana
- `ROUND_349_A.md` — Un solo emparejamiento deja un residuo escaso y conserva cobertura en cada centro
- `ROUND_350_A.md` — Cobertura casi total en todos los centros usando dos momentos
- `ROUND_351_A.md` — Residuos de soporte primo prescrito y un criterio cruzado sin diagonal
- `ROUND_352_A.md` — Contraprueba para la decorrelación basada sólo en los portadores
- `ROUND_353_A.md` — Las potencias primas superiores consumen a lo sumo la mitad de la norma crítica
- `ROUND_354_A.md` — Dos sectores de primos simples se compensan en su media con signo
- `ROUND_355_A.md` — Compensación de los sectores de 354 en cada centro
- `ROUND_356_A.md` — Umbral de divisor liso para retirar términos al coste de raíz
- `ROUND_357_A.md` — Basta estimar cofactores sin primos pequeños, con un solo corte prescrito
- `ROUND_358_A.md` — Reconstrucción sin pérdidas por profundidad para cribas crecientes
- `ROUND_359_A.md` — Criterio con el producto entero libre de primos pequeños
- `ROUND_360_A.md` — Un único promedio lineal a anchura fija para los productos cribados
- `ROUND_361_A.md` — Cómo el corte amplifica la oscilación forzada de la ventana triangular
- `ROUND_362_A.md` — Cola de frecuencias por debajo de la raíz con el corte móvil
- `ROUND_363_A.md` — Ventana gaussiana y truncación a raíz de log x
- `ROUND_364_A.md` — Qué región de ceros detecta un gaussiano difusivo con criba móvil
- `ROUND_365_A.md` — Un solo corte móvil y una sola desigualdad para la gaussiana difusiva
- `ROUND_366_A.md` — El sesgo positivo del producto cribado y un criterio de signo sin barrera
- `ROUND_367_A.md` — Criterio de positividad con una gaussiana fija para el producto completo cribado
- `ROUND_368_A.md` — Una sola comparación de paridades, con corte y anchura fijados por x
- `ROUND_369_A.md` — Dominio impar incondicional en un rango creciente de capas
- `ROUND_370_A.md` — Silla incondicional hasta cortes exp(C(log log x)²)
- `ROUND_371_A.md` — La escala que alcanza la región de Vinogradov–Korobov
- `ROUND_372_A.md` — Exponentes de las dos excursiones en el corte móvil exacto
- `ROUND_373_A.md` — Anchura de las excepciones de paridad en la escala logarítmica
- `ROUND_374_A.md` — Coste de las capas de alta multiplicidad en el corte exacto
- `ROUND_375_A.md` — El prefijo creciente de capas tiene signo negativo en el corte exacto
- `ROUND_376_A.md` — Marcado logarítmico de la capa: crecimiento hasta (1−ε)log log x
- `ROUND_377_A.md` — El bloque intermedio tiene exceso positivo y compensa el prefijo
- `ROUND_378_A.md` — Una capa grande en cada escala y el límite de los momentos de multiplicidad
- `ROUND_379_A.md` — Signo de todo el sector con un único primo por encima de una segunda escala
- `ROUND_380_A.md` — Saldo del sector con exactamente dos primos grandes
- `ROUND_381_A.md` — Saldo de todos los sectores de orden fijo y obstrucción al truncamiento
- `ROUND_382_A.md` — Comparación uniforme de sectores a ambos lados del máximo del perfil principal
- `ROUND_383_A.md` — El cero real del peso de paridad cerca de uno
- `ROUND_384_A.md` — Inversión de signo del sector con un único primo macroscópico
- `ROUND_385_A.md` — Transición cuantificada y corte que neutraliza el sector de un primo
- `ROUND_386_A.md` — Neutralizar la unión de todos los primos grandes: reducción a un producto finito
- `ROUND_387_A.md` — El salto en el corte neutral es positivo y menor que la raíz
- `ROUND_388_A.md` — Coste inevitable de tomar módulos en una vertical del producto neutralizado
- `ROUND_389_A.md` — Una banda horizontal que ningún contorno simple de módulos puede rodear
- `ROUND_390_A.md` — Dos cruces en el orden de los primos y distancia entre ellos
- `ROUND_391_A.md` — Segundo cruce de la unión y un corte finito por debajo de la raíz
- `ROUND_392_A.md` — Cruces arbitrariamente lejanos y representación con primos x^o(1)
- `ROUND_393_A.md` — Qué tamaño de primo bastaría y qué tamaño es inevitable
- `ROUND_394_A.md` — En el extremo cuatro todavía falta masa
- `ROUND_395_A.md` — Umbral exacto de masa absoluta a segundo orden
- `ROUND_396_A.md` — Cancelación efectiva entre las clases de multiplicidad cerca de 4z
- `ROUND_397_A.md` — Las dos frecuencias dominantes del mayorante en la silla positiva
- `ROUND_398_A.md` — Dos sillas conjugadas y suficiencia condicional del umbral de masa
- `ROUND_399_A.md` — Inversión del tamaño del primo terminal en escalas individuales
- `ROUND_400_A.md` — Un techo explícito e incondicional para el primo terminal
- `ROUND_401_A.md` — La fase del corte determinista al mover la escala: ambos signos en cada bloque
- `ROUND_402_A.md` — Ventana de búsqueda en número de primos alrededor de una amplitud calculable
- `ROUND_403_A.md` — Separación incondicional del término negativo y de los polos a altura creciente
- `ROUND_404_A.md` — Una parte de la suma de residuos ya cumple un ahorro exponencial
- `ROUND_405_A.md` — Cuánto pierde el producto de Euler en las alturas verificadas y superiores
- `ROUND_406_A.md` — Un promedio positivo suprime todos los residuos en una ventana explícita
- `ROUND_407_A.md` — Quitar un par crítico del promedio conservando pesos positivos
- `ROUND_408_A.md` — Iteración del estrechamiento con ceros críticos suficientemente altos
- `ROUND_409_A.md` — El primer cero crítico se puede retirar antes de volver a estrechar
- `ROUND_410_A.md` — Qué mide exactamente la varianza después de retirar los pares críticos
- `ROUND_411_A.md` — Contraejemplo: quitar todos los pares críticos en orden con núcleos positivos
- `ROUND_412_A.md` — Comparación integrada en el eje real que recupera la suma sin peso de los desplazamientos
- `ROUND_413_A.md` — D(R) ya tiende a cero sin RH y el límite fuerte tiene una fórmula rectangular
- `ROUND_414_A.md` — Eliminar la normalización desconocida sin perder el signo de cada cero
- `ROUND_415_A.md` — Qué detectan las derivadas del déficit integrado
- `ROUND_416_A.md` — La segunda diferencia diádica ya cambia de signo si existe un cero exterior
- `SELECTION_002.md` — Selección: potencias y factoriales descendentes
- `SELECTION_003.md` — Selección: agrupación theta por sumas de dos cuadrados
- `SELECTION_004.md` — Dilataciones primas del perfil de saltos
- `SELECTION_005.md` — Dos perfiles de saltos con escalas 2 y 3
- `SELECTION_008.md` — Reflexión de las celdas en cero
- `SELECTION_009.md` — Eliminar el salto compuesto de índice máximo
- `SELECTION_019.md` — Cruce remoto después de cancelar el término polar
- `SELECTION_027.md` — Selección de promedios de ancho creciente
- `SELECTION_035.md` — Traslado directo de certificados por mezcla de cambios de escala
- `SELECTION_040.md` — Minoración divisorial del peso de 039
- `SELECTION_089.md` — Muestreo uniforme de la paridad impar de 088
- `SELECTION_092.md` — Límite de la lectura prima del cosh
- `SELECTION_096.md` — Igual masa, igual hueco y signos opuestos sin primalidad
- `SELECTION_098.md` — Coste local de mayorar el peso primo mediante recuentos positivos de múltiplos
- `SELECTION_099.md` — Un reparto binomial fijo no reproduce el peso logarítmico con dilataciones positivas
- `SELECTION_128.md` — Resolución necesaria de un mayorante factorial de la media prima
