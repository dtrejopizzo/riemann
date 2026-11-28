# Dictamen matemático privado — segunda revisión

28 de noviembre de2026. Fuentes exactas: [manifiesto V2](revision-v2/fuentes-v2.json), catorce archivos cuyos hashes se comprobaron al cierre. No se modificaron los manuscritos ni se hizo commit. Papers47–48 excluidos.

## Resultado

**Dictamen favorable sobre la cadena matemática reconstruida con el suplemento explícito de esta revisión. Dictamen (b) sobre la versión actualmente escrita, que todavía contiene pasos incorrectos.** Son dos objetos distintos: los PDFs actuales y las fuentes identificadas más las sustituciones y demostraciones del suplemento.

La revisión reconstruyó las entradas necesarias y la deducción SF + Sp + Cv → desigualdad principal → GRH de Dirichlet → RH. Para esa reconstrucción se requieren las correcciones exactas de [SUPLEMENTO-MATEMATICO](revision-v2/SUPLEMENTO-MATEMATICO.md), con sus pruebas enlazadas. No se conserva como premisa pendiente el antiguo supuesto carácter residual de53. Tampoco se presenta la mera ausencia de un contraejemplo como verificación: las fichas detallan los cálculos, hipótesis, rangos y dependencias que justifican cada cierre.

Este es el alcance de la certificación matemática privada de esta revisión: **la deducción reconstruida, con el suplemento, tiene un dictamen positivo; los manuscritos sin incorporarlo no reciben “correctos como están escritos”.** No es un certificado formal Lean ni un aval de los matemáticos mencionados por el usuario. Ninguno de ellos fue contactado. Se aceptan los teoremas clásicos individualizados con sus hipótesis, como en una revisión matemática ordinaria; no se afirma haber reprobrado toda la literatura utilizada.

## Correcciones necesarias que siguen fuera de los manuscritos

| Lugar | Primera incompatibilidad o paso insuficiente | Reparación y alcance verificado |
|---|---|---|
| 54:2695,7584;58:51272,56151 | νflat=ν″υ^m/χ′ contradice54:2730 y el peso en6448 | Definir νflat=ν″/χ′; mantener los usos νflatυ^m. Se recuperan los tres intercambios, H5, generación y el mismo H_j. |
| 55:6104;58:67922 | J_O∩J1=J1 no tiene el cociente H que se usa después | Definir J_O^(1) mediante congruencia en los lugares auxiliares dentro de J_O. El promedio de Higman conserva integralidad, e_c y c0∣N_ch. |
| 49, fase δ_g | La clasificación fuerte atribuida a W4 no se prueba allí | Sustituirla por las dos consecuencias suficientes, demostradas aritméticamente: módulo en todos los conjugados y unidad sobre ℓ cuando g es integral. |
| 53, pcu:coeff | La fórmula impresa de κ0 conserva sólo el módulo infinito | Usar (ε_T/ε_U)|d0|_(A_E)^j. El factor finito adicional es fijo y se absorbe en K; no cambia la dependencia en el twist. |
| 54, ppe:harm/bottom | Generación de armónicos incompleta en una frase; inverso de A incorrecto | Añadir generación por la acción conjunta; corregir A y respetar conjugado-linealidad. Anulación y constantes conservadas. |
| 54, explicit/carriernz/psv:c | Algunas justificaciones usan una topología demasiado débil o una identificación innecesaria | Usar densidad y continuidad en Schwartz/momentos, y Parseval para no anulación. Pruebas suplementarias sin pérdida. |
| 56, apéndice BL/G4 | Citas no sincronizadas con55 | Copiar el dominio e_cF(O) y la formulación por el generador tame; sincronizar también58 cuando corresponda. |

El nuevo defecto54 tiene un efecto real sobre la prueba literal. Con la definición impresa, H5 recibe det(h)^−m y el integrando de F⁰(1) tiene carácter central z^−3m² en una plaza infinita. Como m>0, la invariancia de Haar y la convergencia absoluta fuerzan F⁰(1)=0, mientras la prueba necesita que sea distinto de cero. La reparación indicada elimina exactamente ese carácter; no se intenta absorberlo en una constante.

El [inventario V2](revision-v2/INVENTARIO-V2.md) y el suplemento contienen las ubicaciones y las pruebas. Las correcciones anteriores que el usuario ya incorporó se comprobaron en [REVISION-ANALISIS-SPANNING-V2](auditoria-profunda/REVISION-ANALISIS-SPANNING-V2.md) y [REVISION-55-56-V2](auditoria-profunda/REVISION-55-56-V2.md).

## Corrección del dictamen anterior sobre53

La objeción anterior sobre un carácter β(det u) residual en la aplicación de pcu:period **se retira**. La aplicación usa el mismo carácter γ de destino en los bloques. La nueva identidad de producto distribuye la fuente y conserva un único destino; el período es el que corresponde a θ_(γ,γ).

La contabilidad finita se recalculó: la razón Levi aporta ν_bc(det q), los datos finitos ν_bc(det x_f)^−1, el período ν_bc(ζ_B)^−1 y el cambio de destino ν(det y)^−2. Con B=y⁻¹Y y q=s0x_UY, su producto es ν_bc(det(s0x_U)), independiente de la variable integrada. La precisión del módulo fijo κ0 se distingue de aquella objeción refutada.

Por tanto, las antiguas clasificaciones(c) de inyectividad, factor de cadena, auxcore, IM54 y regularidad55 cuyo único motivo era ese carácter residual **no son el dictamen vigente**. Las aplicaciones se reconstruyeron con la fórmula corregida; no se las aprobó sólo por borrar la objeción. Evidencia: [caracteres53](auditoria-profunda/REVISION-53-CARACTERES-V2.md), [cadena53](auditoria-profunda/CADENA-53.md), [auxcore](auditoria-profunda/AUXCORE-53-54.md).

## Cierre de las entradas y sus uniones

En esta tabla, “reconstruido” incluye el suplemento expresamente señalado; no significa(a) literal de cada línea del manuscrito.

| Entrada necesaria | Comprobación positiva y evidencia |
|---|---|
| Datos, criterio unilateral y selección de twists46 | Existencia y tamaños, gran criba, densidad, transformada y Landau reconstruidos en [ANALITICA](auditoria-profunda/ANALITICA.md). C0 de49 se fija antes de los umbrales. |
| SF49/50 | Seesaw, Chowla–Selberg exacto, divisibilidad en todas las ramas y rango del Hecke truncado: [THETA](auditoria-profunda/THETA.md). FJ corregido por el usuario; fase suficiente: [FASE49](auditoria-profunda/REVISION-FASE49-V2.md). |
| Normalizaciones comunes49 | Levi, unipotente, Weyl, factor2, índice gaussiano, doubling y cambio de carácter reconstruidos en [SPLITTING](revision-v2/REVISION-SPLITTING-V2.md). No queda una fase arbitraria aceptada por unitariedad solamente. |
| Sp51/52 | Segundo momento, constante principal, cobertura de pares, Siegel/Poisson y rango: [SPANNING](auditoria-profunda/SPANNING.md), [correcciones V2](auditoria-profunda/REVISION-ANALISIS-SPANNING-V2.md). Multiplicidades sólo bajo las hipótesis específicas utilizadas. |
| Exchange, cadena y auxiliares53 | Caracteres finitos y módulo, inyectividad, H/Hc/F, determinante y auxiliares reconstruidos; referencias anteriores y [COVOLUMEN](auditoria-profunda/COVOLUMEN.md). |
| Gram general54 | Se revisó el rango general, no se extrapoló desde rango uno: [períodos](auditoria-profunda/REVISION-54-PERIODOS-GENERALES-V2.md), [tres intercambios](auditoria-profunda/REVISION-54-TRES-EXCHANGES-V2.md), [generación](auditoria-profunda/REVISION-54-SPAN-GENERAL-V2.md). Se conservan el determinante comprimido y la potencia d_j del producto L. |
| Valoración alcanzada54 y CL53 | Selección de coeficiente mínimo, comparación arquimediana y norma compacta z≥2 reconstruidas; la norma compacta alimenta CL antes del intercambio y evita circularidad. [THETA](auditoria-profunda/THETA.md), [AUXCORE](auditoria-profunda/AUXCORE-53-54.md). |
| Regularidad55 y pérdida local56 | Promedio integral, Ribet, cup products, todos los primos incluidos los pequeños, cuantificadores de las inmersiones y suma de presupuestos: [revisión55/56](auditoria-profunda/REVISION-55-56-V2.md), [SELMER](auditoria-profunda/SELMER.md), [HODGE](auditoria-profunda/HODGE.md). NM se usa como condición suficiente, no necesaria. |
| Alturas y Cv → desigualdad → GRH/RH | Producto con twist dependiente del primo, conjugación cσc, costes y signos: [ensamblaje](revision-v2/ENSAMBLAJE-GLOBAL.md), con [revisión cruzada](revision-v2/REVISION-CRUZADA-GLOBAL.md). |

Las uniones se revisaron por su contenido y sus aplicaciones: mismo rango, mismas hipótesis, independencia del twist, normalización de constantes y cuantificadores. Los recuentos antiguos de copias textuales no se usan como sustituto. Las dos citas desactualizadas de56 siguen siendo correcciones documentales necesarias, expresamente enumeradas.

## Alcance que no debe confundirse con la conclusión

La clasificación fuerte de δ_g permanece(c); las dos consecuencias suficientes tienen prueba suplementaria. Las comparaciones finitas de46 que el propio texto declara sin prueba y el enlace documental a los certificados de ventanas no se incorporan como premisas de esta deducción. Los valores de T no se volvieron a calcular en esta ronda. Las reproducciones numéricas previas quedan en el expediente y no son fundamento de la conclusión global.

Las filas43–45 permanecen separadas: sus resultados y normalización explícita se revisaron en [filas A/B/C](07-rows-a-b-c.md), [Hochschild](auditoria-profunda/HOCHSCHILD-43.md) y [completación](auditoria-profunda/FORMA-COMPLETACION-43.md). No aportan una premisa faltante a Row D. La prioridad bibliográfica absoluta no queda certificada, ni para esas filas ni para los nuevos exponentes integrales de56.

La conexión matemática identificada por la auditoría es la cadena de control integral y de todos los conjugados → divisibilidad y alturas → generación de rango suficiente → determinantes/covolúmenes → una cota unilateral sobre primos. El aporte candidato a novedad reside en esos puentes cuantitativos específicos, no en haber creado desde cero las teorías theta o Hodge integral. Véase el [programa de conexiones](06-conexiones-y-programa.md), conservando su separación entre mecanismo matemático y prioridad por establecer.

## Uso del dictamen

El objeto revisado favorablemente queda definido por los hashes V2 más el suplemento y las demostraciones enlazadas. Para afirmar lo mismo de los PDFs hay que incorporar esas sustituciones y comprobar la propagación del texto resultante. No se editó ninguna fuente durante esta revisión. Los informes anteriores se conservan en historico y las fichas antiguas se leen con las rectificaciones V2; sus objeciones superadas no deben citarse como actuales.
