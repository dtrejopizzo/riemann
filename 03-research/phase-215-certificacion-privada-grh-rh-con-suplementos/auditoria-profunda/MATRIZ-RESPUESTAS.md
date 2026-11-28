> **V1: registro histórico, revisado en V2.** No aplicar sus objeciones de caracteres ni sus estados de propagación a los manuscritos corregidos sin consultar el [estado V2](../revision-v2/ESTADO.md). La cancelación especializada de caracteres corrige el impacto global atribuido en V1; se están consolidando los demás resultados.

# Respuestas a las preguntas del autor

Versión consolidada de la auditoría, 28-11-2026. Manuscritos en el commit `97fb4e78d5a858baa926829a42336ae3b914e59a`. Papers 47–48 excluidos. Esta matriz sustituye los dictámenes iniciales que sólo expresaban pendientes de lectura. Los registros detallados enlazados contienen las reconstrucciones y fuentes.

**Dictamen global vigente: la demostración presentada no puede certificarse tal como está escrita.** Hay un fallo algebraico demostrado en `pcu:product` de53, utilizado por el intercambio y por su no anulación. No es simplemente una limitación de tiempo o de especialidad del revisor. Tampoco es un contraejemplo a RH o al enunciado del intercambio. No se ha completado una reparación que conserve los períodos y los factores exactos requeridos.

Se usan las categorías solicitadas: **(a)** comprobado en el alcance indicado; **(b)** argumento escrito incorrecto, con primera línea defectuosa; **(c)** no verificado, con obligación identificada. Una prueba reconstruida después de corregir una línea falsa no recibe un «correcto como está escrito» global. Se informa por separado el resultado matemático reconstruido y la evaluación literal de la demostración. No se presenta una ejecución numérica como verificación de un argumento funcional que no cubra.

## 2. Paper 46: forma y ventanas

| Pregunta | Respuesta y alcance |
|---|---|
| 2.1 Positividad de W_T en toda ventana equivalente a RH | **(a).** Fórmula explícita, paso real/complejo, densidad de forma y test primitivo negativo fuera de la recta reconstruidos. «Toda ventana» es indispensable. La fórmula hermitiana auxiliar de46:277 contiene una errata, detallada abajo, que no cambia la diagonal W_T. |
| 2.2 Cotas 10⁻¹⁸ y 2.5·10⁻¹² | **(a) mediante reproducción independiente**, manteniendo T fijado. Se generaron las matrices Arb640, se justificó el resto <2·10⁻⁴² y se verificaron las cuatro inercias. El caso completo par requiere precondicionamiento certificado y Gershgorin; la eliminación intervalar directa se ensancha. No se certifican la cifra más fina 1.5·10⁻⁴³ ni la columna «fails at», innecesarias para estas cotas. Los decimales c_* y ω_- deben tratarse como abreviaturas, no como cotas superiores. |
| 2.3 Tres hechos sobre ceros y ventana 2.8022 | **(a) hechos y desigualdad reconstruida con anexos.** Z1 se aisló y contó con Arb, Z2 se cotejó con Platt–Trudgian y Z3 con la formulación publicada. El programa público localizado pasa 17 comprobaciones; el puente funcional fue reconstruido y revisado independientemente. **Lectura estrictamente autocontenida de46: (c) en1915–1930**, porque allí sólo se reporta el certificado. Incorporar o citar de forma precisa el programa y la prueba de los anexos resuelve esa omisión documental. |

Evidencia: [CHECKLIST-46-PURO](CHECKLIST-46-PURO.md), [NUMERICA-46](NUMERICA-46.md), [revisión cruzada](NUMERICA-46-REVISION-CRUZADA.md), [VENTANA-28022](VENTANA-28022.md), [puente funcional](VENTANA-28022-PUENTE.md), [ANALITICA](ANALITICA.md).

El criterio unilateral, la selección de datos admisibles, el uso de gran criba/densidad y el ensamblaje final de46 se reconstruyeron **condicionados a los tres inputs automorfos**. Esa condición no está descargada por el hecho de haber verificado las ventanas finitas. La proposición de Gram de todos los grados también declara su input aritmético: no es una prueba independiente que pueda suplir el fallo53.

## 3. Papers 43–45: filas A, B y C

| Paper / pregunta | Respuesta y alcance |
|---|---|
| 43, teoremas principales | **(a)** en los enunciados `introA/H/B/C/D`: crossed product rápido, Hochschild torcido, símbolo completo, firma y completaciones fueron reconstruidos. La convolución de correspondencias es la definida en el texto; no constituye por sí sola una teoría geométrica de intersección sobre Spec Z. |
| 44, teoremas principales | **(a)** para `introA/B`: composición de Haar de cosets, recuperación del índice y coeficientes de contacto. La hipótesis P(n)⊂S_f permanece activa. No se evalúa una distribución sobre una medida fuera de su dominio. |
| 45, comparación y normalización | **(a)** para `thm:comparison`, fórmula explícita y criterio primitivo. Se conservaron signo, factor2π, inversión del perfil y término polar. El límite es estabilización para soporte fijo; no un límite espectral que autorice otra positividad. |
| Novedad de cada fila | La fórmula explícita y su lectura como traza tienen antecedentes en Connes, Meyer, Burnol y Connes–Consani. **(c)** para prioridad del paquete exacto de43 y de la presentación semilocal de44: no se estableció una ausencia de antecedentes equivalentes.45 es compatibilidad de normalizaciones de una fórmula clásica, no una nueva fórmula explícita. |

Evidencia: [filas A/B/C](../07-rows-a-b-c.md), [Hochschild43](HOCHSCHILD-43.md), [forma y completación43](FORMA-COMPLETACION-43.md). Estas filas no son premisas de la deducción automórfica de RH de46.

## 4. Paper 50: divisores elementales

| Pregunta | Respuesta y alcance |
|---|---|
| 4.1 Prueba en el rango ph:eq-large | **(a)** para el teorema con sus definiciones y su rango. Controla la colongitud truncada de Λ/(YΛ+pʲΛ), con exponente ≤(3c_d+θj)dimΛ; no afirma invertibilidad ni una media finita de exponentes sin truncar. Se reconstruyeron el argumento algebraico y su realización aritmética. |
| 4.2 ph:root, ph:count y ph:av | **(a)** en las instancias usadas: ciclos y arcos libres, aproximación débil, transposición y conteo se cotejaron con los datos suministrados por49. No se deduce la estimación para un operador de Hecke arbitrario. |
| 4.3 Coincidencia de rango posterior | **(a)** en la aplicación de49 `pa:partner/mark`, `pl:N/wa/wacor`: no se identificó una hipótesis estructural omitida. |

Evidencia: [THETA, HE01 y EX01](THETA.md), más el desarrollo algebraico del [informe50 inicial](../02-theta-hecke-covolumen.md). El alcance es el estadístico de divisores definido por el propio teorema; no sustituirlo por una media sin sus truncamientos o convenciones.

## 5. Paper 49: Short Forms

| Pregunta | Respuesta y alcance |
|---|---|
| 5.1 Seesaw y constante independiente del twist | Cadena de lifts, soporte, rigidez real, factores finitos y dependencia de constantes **reconstruidos**. **(b) local en la prueba FJ**,49:2248–2250: el orden de traslaciones en el producto interno no es el escrito. La sustitución directa F=R(e)F y x=gh da la fórmula correcta sin cambiar la constante. Por eso no se aprueba literalmente toda la prueba, aunque el resultado requerido se recupera con la reparación. |
| 5.2 Cota en cada conjugado con constante CS exacta | La constante exacta de Chowla–Selberg y su normalización **(a)**. **(c) para la descripción más fuerte de la fase δ_g en49:5472**: se atribuye a W4, que no la demuestra allí. La auditoría prueba por Rao y unitariedad algebraica las consecuencias efectivamente necesarias, incluido el módulo en todos los conjugados. Reemplazar esa frase por esa prueba descarga el paso necesario; no equivale a haber probado la clasificación más fuerte de la fase. |
| 5.3 Divisibilidad en todos los primos, no split y nivel | Argumentos locales, casos excepcionales, Fourier finito, nivelN, branching y ensamblaje **reconstruidos en el rango declarado**. Subsiste la misma salvedad literal sobre la fórmula de fase; la integralidad necesaria tiene una prueba independiente en el informe. No se encontró otro fallo de alcance en `pa:count` ni en las cuatro ramas de `pa:divis`. |

Evidencia: [THETA](THETA.md), CJ01–08, SS01, AR01–03, CM01, KI01, LN01, BR01, EX01 y AS01; [SPANNING](SPANNING.md) para FJ. Estos cierres no reparan el exchange53.

## 6. Papers 51–52: Spanning

| Pregunta | Respuesta y alcance |
|---|---|
| 6.1 Segundo momento uniforme y constante exacta | Resultado **reconstruido con las reparaciones locales** identificadas abajo. No se perdió un factor dependiente del rango en el término principal. Literalmente hay pasos **(b)** en las pruebas auxiliares, por lo que no corresponde un (a) indiscriminado de todas sus líneas. |
| 6.2 Celda abierta, Siegel y Poisson | Medidas, volumen unipotente, razón de masas, grado formal y cancelaciones de gauges reconstruidos. **(b)** en52 `pff:S`: el corte que tiende a cero no recupera la densidad pretendida. Se da un ejemplo local y una reparación con bolas crecientes; el lema posterior de fibras ya usa esa dirección correcta. |
| 6.3 Pares restantes y rangos | **(a) para la cobertura reconstruida**, incluidos pares no próximos, todos l≤n³ y bloques no concordantes. En51:10498 el exponente jacobiano de `pbo:tube` debe ser 2ρk+2ρ², no 2ρk+ρ²; el exponente corregido todavía satisface la cota global utilizada. No se encontró un intervalo de parámetros omitido que sobreviva a esa reparación. |
| 6.4 Multiplicidades y atribución | La igualdad se reconstruyó **con las hipótesis específicas de la comparación y sus tipos arquimedianos**; no para cualquier par de grupos simplemente isométricos en plazas finitas. En51:4453/4511 es falsa la convergencia uniforme de la serie sobre todo g; basta compactos en ambos argumentos y la cota total uniforme, que sí se justifican. Las fuentes clásicas de representación y masa se separan de la comparación nueva; no se atribuye a un autor citado un teorema más amplio. |

Evidencia: [SPANNING](SPANNING.md), [MULTIPLICIDADES](MULTIPLICIDADES.md). La afirmación auxiliar52 de que U(<l) fija cada e_b también necesita reemplazarse por la propiedad unitriangular realmente utilizada.

## 7. Papers 53–54: Covolume

| Pregunta | Respuesta y alcance |
|---|---|
| 7.1 Exchange y módulo de la constante | **(b), prueba incorrecta como está escrita.**53:3351–3352 omite α(det g)α(det y)β(det l); primera inferencia inválida3359–3360. En el período queda β(det u) dentro de la integral. Su módulo uno no permite sacarlo. No se certifica el módulo final de exchange por esta ruta. |
| 7.2 Inyectividad y Z(1)/Z(θ) | **(c) para una conclusión incondicional de esta prueba:** recibe el exchange sin demostrar. El álgebra de cadena fue comprobada condicionalmente en [CADENA-53](CADENA-53.md). Los inputs H/Hc/F se reconstruyeron posteriormente en CADENA-53§6. La relación RS/T1 sigue recibiendo el exchange defectuoso; no se confunde una identidad abstracta de Gram con la construcción completa del triángulo. No se declara falso el enunciado de inyectividad. |
| 7.3 Gram de un lift y valores L | **(c) para el Gram general `au:onelift`**, cuya deducción usa exchange53; la contabilidad algebraica y las constantes fueron reconstruidas condicionalmente. **(a) para la norma del lift de un carácter en la rama compacta z≥2**, mediante SW/Rallis, que alimenta CL sin usar el exchange defectuoso. La rama z=1 de IM54 sí lo usa. No extender el cierre de la norma de rango uno a todo determinante comprimido. |
| 7.4 Forma test y valoración alcanzada | Construcción local, doce factores y selección de un coeficiente de valoración mínima **reconstruidas**; no se confunde desigualdad ultramétrica con igualdad automática. La comparación arquimediana usa CL53, reconstruido con sus constantes independientes del carácter. El descenso acotado global de54 se reconstruyó y, con CL, `normL` y `psu:I`, cierra **(a) la comparación arquimediana reconstruida**. `pc:auxcore` no es una dependencia directa de ese argumento; se audita por separado para covolumen. Para las aplicaciones globales sigue siendo necesario el input de covolumen correcto. |

Evidencia: [error53](ERROR-53-CARACTERES.md), [COVOLUMEN](COVOLUMEN.md), [PLANO-53](PLANO-53.md), [THETA](THETA.md). Otros defectos53: `pcx:decay` requiere P≠∅, ya presente en la aplicación principal; sl(x) no es acotado de Hilbert a Hilbert y debe definirse con normas de momentos. La reparación de topología no repara los caracteres.

## 8. Paper 55: twists, Selmer y Ribet

| Pregunta | Respuesta y alcance |
|---|---|
| 8.1 Twist para cada ℓ, incluidos pequeños | Construcciones y presupuestos por primo reconstruidos. **(c) para la conclusión global sin inputs**, porque II recibe IM54, cuya rama z=1 usa exchange53. Además hay correcciones literales de órdenes e inercia que deben incorporarse; no se elimina el problema excluyendo primos pequeños. |
| 8.2 Ribet módulo potencias, retículos e irreducibilidad | **(a)** para los argumentos de retículos reconstruidos: no se identificó una hipótesis residual de irreducibilidad faltante. Se pagan los denominadores de separación; los promedios racionales no se confunden con divisiones integrales. La preservación del idempotente e_c en el argumento de Higman requiere precisar el nivel base y la construcción equivarante indicada en el informe. |
| 8.3 Pérdida local y clases impares | **(a)** para el segmento local con los datos declarados, incluyendo ℓ=2 en las alternativas autorizadas. Se reconstruyeron cup products, clases de detección, Kolyvagin, dualidad y paso de exponentes a longitudes. |
| 8.4 Suma sobre primos | **(a) como ensamblaje de las cotas locales**: pesos logℓ, denominadores y términos de M conservados. No convierte en demostrado el input IM defectuoso. |

Evidencia: [SELMER](SELMER.md), [HODGE](HODGE.md) y [uniones](MATRIZ-UNIONES.md). Errores literales: norma F_(q^n)→F_(q^d) no definida si d=lcm(d_k) no divide n; orden p_i^r−1 no cubre todos los grados mixtos; un polinomio fijo no mata todos los elementos de inercia. Los enunciados realmente necesarios usan el generador adecuado y órdenes que dividen N_ch; las reparaciones están desarrolladas sin aumentar ese presupuesto.

## 9. Paper 56: cup products integrales

| Pregunta | Respuesta y alcance |
|---|---|
| 9.1 Exponente para todo ℓ sin restricción FL | **(a)** para la cadena local bajo las hipótesis impresas: T3, I2, I4, I5, SCC y scheme reconstruidos. «Sin restricción Fontaine–Laffaille» no significa sin ninguna hipótesis sobre datos, pesos o ventanas. |
| 9.2 NM necesaria y suficiente | **Suficiente: (a). Necesaria: no.** El paper no necesita la recíproca. Hay ejemplo de emparejamiento nulo aunque NM falle; véase HODGE y el informe inicial. No presentar NM como caracterización si sólo se prueba suficiencia. |
| 9.3 Tame potencialmente cristalino | **(a)** en las alternativas y rangos expresos, con grados de los polinomios, cota e₀ y pérdidas de descenso comprobados. No se introduce una ampliación de coeficientes innecesaria ni dependencia oculta del rango de Y. |
| 9.4 Novedad y compatibilidad FL | Compatibilidad en el solapamiento: **(a)**. Prioridad absoluta: **(c)**. La teoría integral fuera de FL ya existe; el candidato específico a novedad son estos exponentes de cup products dependientes de ventanas y grosor, no la creación de toda la teoría integral. |

Evidencia: [HODGE](HODGE.md), especialmente §§6–7 y fuentes primarias Fontaine–Laffaille, Liu y Caruso–Liu.

## Uniones, conexiones y revisión externa

[MATRIZ-UNIONES](MATRIZ-UNIONES.md) distingue copia textual de comprobación semántica y documenta la propagación del fallo53. Las citas mutuas55↔56 y53↔54 no bastan para diagnosticar circularidad; se reconstruyeron los órdenes de dependencias concretos. La red completa no se certifica por un TSV de etiquetas: las uniones todavía no individualizadas conservan (c) hasta completar sus fichas.

La conexión propuesta que merece desarrollo es: datos theta integrales y control en todos los conjugados → divisibilidad/altura → retículos de rango suficiente → determinante/covolumen → desigualdad unilateral sobre primos. El puente de covolumen es precisamente donde está el fallo demostrado. Las filas A–C proporcionan una interpretación de Weil, pero no suministran la positividad usada por D. El [programa de conexiones](../06-conexiones-y-programa.md) distingue mecanismos comprobados, antecedentes y prioridad no establecida.

La revisión fue realizada por agentes de IA organizados por especialidad. Ningún matemático real de la lista fue contactado ni certificó estos resultados. El [expediente humano](EXPEDIENTE-REVISION-HUMANA.md) prepara las preguntas, fuentes y hallazgos para una revisión externa, sin atribuir avales ni disponibilidad.

## Cierre de auxcore

[AUXCORE-53-54](AUXCORE-53-54.md) completó la lectura de inversión de línea, G1–G4, giros y cotas. Auxcore permanece condicionado al intercambio defectuoso, no a una omisión de revisión de esos bloques. Se agregaron al inventario dos reparaciones locales que conservan constantes: orden r₀⁻¹r en la estimación de slices y cancelación de normas conjugadas en el determinante finito.
