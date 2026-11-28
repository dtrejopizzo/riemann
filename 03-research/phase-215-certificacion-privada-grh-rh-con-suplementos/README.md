# Fase 215 — Certificación matemática privada de la cadena GRH/RH con suplementos

**Estado: CERRADA.** El expediente registra un dictamen matemático privado favorable para la cadena reconstruida con los suplementos explícitos. El objeto y alcance precisos están en [MEMO-FINAL.md](MEMO-FINAL.md); no se extienden automáticamente a versiones posteriores de los manuscritos.

## Pregunta y objetivo

Revisar las demostraciones de los papers43–46 y49–56, comprobar sus uniones y su propagación en58, identificar errores y obligaciones, y determinar si la cadena reconstruida permite deducir GRH para Dirichlet y RH. Papers47–48 quedaron fuera de la revisión.

## Qué se hizo

- Se organizó la revisión por especialidades: análisis, theta y Hecke, generación y multiplicidades, covolúmenes, Selmer y Hodge integral.
- Se reconstruyeron las entradas de Short Forms, Spanning y Covolume y el ensamblaje que conduce a la desigualdad principal y al criterio unilateral.
- Se revisaron hipótesis, rangos, caracteres, constantes, índices y cuantificadores de las aplicaciones entre papers, distinguiendo coincidencia textual de validez matemática.
- Se cotejaron las correcciones del autor y se recalculó la contabilidad finita de pcu:coeff53. Se retiró la objeción anterior sobre un carácter residual y sus consecuencias en cascada.
- Se documentaron reparaciones adicionales y sus pruebas: definición de νflat54, nivel auxiliar55, propiedades suficientes de la fase49 y precisiones de normalización y topología.
- Se identificaron conexiones conceptuales, antecedentes y proyectos autónomos para una futura fase216.

## Resultados y alcance

| Resultado | Estado en el expediente |
|---|---|
| Cadena reconstruida SF + Sp + Cv → desigualdad principal → GRH de Dirichlet → RH | Dictamen privado favorable mediante revisión matemática, con los suplementos identificados |
| Aprobación literal de las fuentes sin esos suplementos | No otorgada: el inventario conserva las líneas incorrectas y las reparaciones necesarias |
| Antigua objeción global al intercambio53 | Retirada tras revisar la aplicación especializada y sus caracteres |
| Fórmula fuerte de la fase49 | No certificada en toda su fuerza; se aportaron las dos consecuencias suficientes para la cadena |
| Prioridad bibliográfica y nuevas generalizaciones | Prioridad absoluta no establecida; programa de investigación formulado |

La certificación registrada corresponde a las fuentes identificadas por hashes más el suplemento y las demostraciones enlazadas. Es una revisión matemática privada asistida por agentes, no una certificación formal Lean ni un aval de los especialistas externos mencionados. La fase no modificó los manuscritos para incorporar sus reparaciones.

## Archivos y orden de lectura

1. [MEMO-FINAL.md](MEMO-FINAL.md): declaración de cierre, alcance y traspaso.
2. [00-dictamen.md](00-dictamen.md): conclusión breve.
3. [REPORTE-FINAL.md](REPORTE-FINAL.md): resultados por bloque y uniones.
4. [Suplemento matemático](revision-v2/SUPLEMENTO-MATEMATICO.md): sustituciones y demostraciones necesarias.
5. [Inventario V2](revision-v2/INVENTARIO-V2.md) y [mapa de cierre](revision-v2/MAPA-DE-CIERRE.md): obligaciones y dependencias.
6. [Ensamblaje global](revision-v2/ENSAMBLAJE-GLOBAL.md): deducción final, con [revisión cruzada](revision-v2/REVISION-CRUZADA-GLOBAL.md).
7. [Fuentes auditadas](revision-v2/fuentes-v2.json): identidad de los manuscritos considerados.
8. [Nuevas conexiones y programa](NUEVAS-CONEXIONES-Y-PROGRAMA.md): antecedentes, atribución, preguntas y criterios de éxito.

`auditoria-profunda/` contiene las fichas matemáticas por especialidad; `evidencia/`, scripts, salidas y datos; `revision-v2/`, los suplementos y controles de la segunda revisión; `historico/`, versiones anteriores preservadas. Los dictámenes V2 prevalecen sobre las objeciones históricas retiradas.

## Relación con otras fases y continuidad

La [fase214](../phase-214-cotas-explicitas-y-reconstruccion/README.md) conserva cotas condicionales y antecedentes de reconstrucción. La fase215 reúne el expediente de auditoría global.

La futura fase216 desarrollará tres trabajos: compatibilidad integral entre twists para uno y dos lifts; núcleos realizables mediante tres niveles de pesos CM y sus costes; y una extracción autónoma de los exponentes de cup products de56, su optimalidad y aplicaciones a congruencias. **La fase216 permanece prevista, no iniciada.**
