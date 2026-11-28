> **Actualización V2:** cualquier referencia de esta ficha al antiguo fallo global de caracteres53 queda retirada. El dictamen vigente y el nuevo inventario de reparaciones están en el reporte final V2. Esta ficha conserva el programa temático, no un aval externo.

# Expediente para revisión humana — versión de la auditoría

No enviado. Ninguna de las personas nombradas ha sido contactada por esta auditoría ni ha avalado los manuscritos. Los nombres son los referentes sugeridos por el autor; su inclusión no supone disponibilidad o aceptación de una revisión.

## Material y versión

Repositorio: dtrejopizzo/riemann, commit de referencia `97fb4e78d5a858baa926829a42336ae3b914e59a`. Los hashes y rutas de las fuentes examinadas figuran en `../evidencia/fuentes.json`. Papers 47 y 48 excluidos. El mapa es 57 y el volumen unificado es 58.

El autor fijó los valores de corte T=(log 5)/2 y T≈2.8022 y aclaró que sí solicita revisar las cotas y sus certificados. Las cuatro inercias de la primera ventana ya se reprodujeron con Arb, resto analítico y revisión cruzada: `NUMERICA-46.md` y `NUMERICA-46-REVISION-CRUZADA.md`. El programa de la segunda ventana se encontró en las carpetas de investigación y en la versión pública: sus17 comprobaciones y el puente funcional fueron reconstruidos y revisados; véanse `VENTANA-28022.md` y `VENTANA-28022-PUENTE.md`. La deducción global examinada no usa estas cotas como premisas.

## Solicitud de revisión

Se solicita revisar los enunciados y sus demostraciones **tal como están escritos**, con tres resultados posibles: (a) correcto, especificando las entradas admitidas; (b) incorrecto, identificando la primera inferencia inválida y por qué; (c) no verificado, identificando exactamente qué paso falta comprobar. Se pide separar errores de formulación, lagunas reparables, demostraciones sustancialmente incompletas y contraejemplos a enunciados.

No se solicita que un especialista avale áreas fuera de su competencia ni que la conformidad con un solo paper se interprete como certificación de RH. Para cualquier conclusión global se requiere comprobar también cada hipótesis y rango en las importaciones.

## Distribución propuesta por especialidad

| Frente | Papers y referentes sugeridos por el autor | Pregunta prioritaria y registro |
|---|---|---|
| Argumento completo | 46,49–56; Levent Alpoge | Deducción de los tres teoremas a GRH, y dependencia precisa de los pasos nuevos. `ANALITICA.md`, `ESTADO.md`. |
| Análisis de ceros | 46; Roger Heath-Brown, Kannan Soundararajan, Maksym Radziwiłł, James Maynard, Terence Tao | Criterio unilateral, gran criba/densidad, datos admisibles e inequación final. `ANALITICA.md`. |
| Marco de Weil | 43–45; Alain Connes, Caterina Consani, Enrico Bombieri, Ralf Meyer | Hochschild/topología, traza y normalización de la fórmula explícita; comparación con antecedentes. `../07-rows-a-b-c.md`, `HOCHSCHILD-43.md` y `FORMA-COMPLETACION-43.md`. |
| Theta y grupos unitarios | 49,53,54; Wee Teck Gan, Atsushi Ichino, Michael Harris, Stephen Kudla | Seesaw, exchange, factores de splitting y Rallis. `THETA.md`, `COVOLUMEN.md`, **`ERROR-53-CARACTERES.md`**. |
| CM y períodos exactos | 49,54; Kenichi Bannai, Shinichi Kobayashi, Haruzo Hida | Normalización exacta de Chowla–Selberg, conjugados, integridad y forma test que alcanza valoración. `THETA.md`. |
| Hecke integral | 50 y aplicación en49; Benedict Gross, Matthew Emerton | Divisores elementales truncados, rango y realización aritmética. `THETA.md` y primer informe `../02-theta-hecke-covolumen.md`. |
| Segundo momento y traza | 51,52; Wei Zhang, Paul Nelson, Philippe Michel, Akshay Venkatesh | Constante principal exacta, todos los pares y rangos, comparación de multiplicidades. `SPANNING.md`, `MULTIPLICIDADES.md`. |
| Galois/Selmer | 55; Christopher Skinner, Eric Urban, Kenneth Ribet, Frank Calegari, Ana Caraiani | Ribet a potencias, tipos locales y ámbito de los labels, twists para cada primo y suma de pérdidas. `SELMER.md`. |
| Hodge integral | 56; Laurent Berger, Tong Liu, Mark Kisin, Toby Gee | Aniquiladores y longitudes, NM, tame y rango fuera de Fontaine–Laffaille; novedad. `HODGE.md`. |
| Formalización | 06-alpoge-verification; Kevin Buzzard | Determinar qué teoremas están formalmente comprobados, qué axiomas o interfaces restan y si la traducción reproduce el enunciado matemático. `../08-registros-lean.md`. |

## Primer paquete prioritario: caracteres en 53

Asunto sugerido: «Solicitud de comprobación de una identidad de splitting en una propuesta de prueba de GRH — paper 53».

Adjuntar fuente53, definiciones 671/1732, lema `pcu:product` 3347–3361, aplicación `pcu:period` 3369–3415 e informe `ERROR-53-CARACTERES.md`. El hallazgo auditado es un cociente de caracteres α(det g)α(det y)β(det l) entre los dos lados impresos. Se solicita confirmar o refutar ese cálculo con las convenciones completas del manuscrito y, si se confirma, precisar si existe una reparación que conserve el período y el módulo exacto del escalar de exchange.

Este paquete es concreto y puede revisarse antes de la auditoría completa del resto de 53. La ausencia de un contraejemplo al enunciado de exchange no resuelve el defecto de su demostración.

## Registro de respuestas externas

Vacío: no hay respuestas externas. Cuando existan, deberán registrarse por separado de los dictámenes de agentes, con autorización de atribución, versión revisada y alcance exacto. El [inventario de correcciones](INVENTARIO-CORRECCIONES.md) y la [matriz de respuestas](MATRIZ-RESPUESTAS.md) contienen el dictamen vigente y sus obligaciones no resueltas.


## Texto de solicitud preparado para un especialista

Subject: Request for a focused mathematical review of a theta exchange identity

Dear Professor,

I am seeking a focused review of an identity in paper53 of the attached series, rather than an endorsement of its claimed GRH conclusion. The accompanying AI-assisted audit identifies a possible decisive error in the character factors of Lemma `pcu:product`, with its downstream use in `pcu:period`.

Using the displayed convention for ω_(α,β), the audit obtains the factor α(det g)α(det y)β(det l) between the two sides. In the subsequent period l is an integration variable, so the missing factor appears to change the period itself. The attached note gives the exact definitions, lines and dependency chain. Could you check that calculation against the full conventions, and assess whether a corrected identity can retain the nonvanishing and absolute constant required later?

A useful response would be: correct as written; incorrect with the first failing inference; or not verified with the specific missing step. The report distinguishes these statuses and includes independently reproduced finite-window certificates. No external expert endorsement is claimed.

Thank you for considering this request.

[Author name and contact information]

Este texto es un borrador de mensaje listo para adaptar por especialidad, **no un mensaje enviado**. Los demás paquetes deben sustituir la pregunta central por la fila correspondiente de la tabla y adjuntar el ledger específico. No conviene pedir a todos los destinatarios que certifiquen simultáneamente áreas ajenas ni enviar el informe como si fuera una demostración ya validada.

## Paquete mínimo de revisión

1. `../REPORTE-FINAL.md` y `INVENTARIO-CORRECCIONES.md`.
2. La versión exacta del manuscrito pertinente identificada en `../evidencia/fuentes.json`, con sus apéndices.
3. El ledger de la especialidad y las fichas de sus uniones; para exchange, `ERROR-53-CARACTERES.md`, `COVOLUMEN.md`, `PLANO-53.md`, `CADENA-53.md` y `AUXCORE-53-54.md`.
4. Para análisis46, scripts, salidas y demostración de los restos y del puente funcional; un log sin esa demostración no basta.
5. Una respuesta atribuible sólo con el consentimiento del revisor, que indique versión, enunciados revisados y alcance. Una respuesta favorable parcial no debe convertirse en aval global.

No se dispone en esta auditoría de una revisión humana externa completada. La entrega del expediente no obliga a ninguno de los especialistas nombrados a aceptarlo ni proporciona por sí misma una certificación.
