> **V1: registro histórico, revisado en V2.** No aplicar sus objeciones de caracteres ni sus estados de propagación a los manuscritos corregidos sin consultar el [estado V2](../revision-v2/ESTADO.md). La cancelación especializada de caracteres corrige el impacto global atribuido en V1; se están consolidando los demás resultados.

# Matriz de uniones: identidad, hipótesis y dependencias

Estado: 28-11-2026. Esta matriz actualiza los pendientes históricos de `../05-uniones.md`. Fuentes: `main.tex` locales, inventario `../evidencia/enunciados_compartidos.json` y ledgers profundos. «Unión (a)» significa que el traslado del resultado y sus hipótesis se comprobaron; **no convierte una prueba defectuosa del resultado importado en correcta**. Los errores de P53 se propagan como falta de justificación de la ruta, no como falsedad demostrada de cada conclusión descendiente.

## Qué mide el inventario textual

El JSON registra entornos con la **misma etiqueta**; no todas las importaciones conservan la etiqueta. Por ejemplo, `au:regular` aparece allí en 46:4921 y 58:4911, pero su fuente matemática en 55 es `pg:main` (55:440), `pg:sums` (493) y la deducción 535–545. Por tanto no existe una comparación automática 46↔55 que autorice decir «idéntico».

Se inspeccionaron las diferencias automáticas siguientes: `pg:III` 55:648/58:22611; `pki:data` 56:486/58:58602; `pki:data-sizes` 56:500/58:58616; `pki:align` 56:638/58:58754; `pll:status` 55:3511/58:25471. Son sustituciones de referencias externas por referencias internas; no cambian las fórmulas o hipótesis de esos entornos. En cambio, `pg:main`, `pg:I`, `pg:II`, `pg:loss`, `pg:odd`, `pll:exponent`, `pki:generic`, `pki:tame`, `pki:crys` y `pkw:G4` tienen igualdad tras normalización en las parejas 55/58 o 56/58. Ese hecho sólo certifica la copia del enunciado, no todas las definiciones de sus macros ni sus aplicaciones.

## Uniones 54–56 y retorno a 46: inspección directa

| Origen → destino | Identidad del contenido importado | Hipótesis y rango comprobados | Estado y obligación que permanece |
|---|---|---|---|
| 55 `pg:main` + `pg:sums` → 46 `au:regular` | Deducción, no igualdad literal. R1=(a), R2=(b), R3=(c),(d). | 55:535–545: θ_ι=τ, ambos signos y todas las potencias 1≤j≤m. β(ℓ)=(β_ℓ+v_ℓ(h₁))logℓ; se conservan falsos lifts y test forms. | **(a) la unión condicional.** No cerrado el input íntegro: depende de IM54 y multiplicidades, y requiere corregir las frases de P55 descritas en SELMER §§6,11. |
| 54 `pex:IM`/`pex:IM1` → 55 `pg:poly`, `pg:stick`, `pg:II` | Se conserva la expansión finita en caracteres, integridad en ι y ι∘c, cociente de valores y factores Euler omitidos. | SELMER §13: n_p puede depender del par crítico, pero no de θ,Q; v₀ se cancela. Incluye ℓ=d, todos j≤m y ampliaciones de módulo. Q es primo a ℓ. | **(a) traslado y deducción de II bajo IM.** Para z≥2 se reconstruyeron norma y expansión; z=1 usa exchange53 y queda afectado por su prueba defectuosa. No reducir arbitrariamente II al rango z≥2. |
| 55 M2/G4 → 56 `pki:data`/`pkw:G4` | Pesos, clases cristalinas/tame y parámetros identificados, no mera copia de nombres. | η=h²+1,W=4t,δ_j=jΔ+h−2t; duales −u−1; K(s⁻¹); q_s depende de s. Polinomios de grados ≤N,≤N,≤N² y e₀≤ℓ^(r²). | **(a) unión condicional**, HODGE §6 y SELMER §§6,12. En P55 hay frases incorrectas de normas de campos y órdenes; las correcciones no aumentan las cotas. El polinomio correcto de P56 NO repite el error de un polinomio fijo para todo s. |
| 56 `pki:crys`, tame, data → 55 `pll:exponent` | Mismos cuatro casos y constantes; no se confunde exponente con longitud en el caso (d). | HODGE §§1–6: todos ℓ mediante las alternativas autorizadas; NM para λ<h³, corte λ≥h³, duales y retículos. SELMER §14 verifica paso a D_ℓ y suma de lugares. | **(a) unión y segmento local** bajo los datos declarados de P46 y las clases M2/G4. No se necesita Fontaine–Laffaille como input oculto. |
| 55 `pll:ribet`, `pll:dual` → clases usadas en 56 y vuelta a `pri:loss` | La clase de cociclos es la producida por retículos u_x y la longitud se normaliza por [O:Z_ℓ]. | No se promedia integralmente dividiendo por el orden del grupo; la exactitud cristalina se usa racionalmente donde corresponde. El rango de Z_f sólo multiplica los casos de exponente. | **(a)**, SELMER §§1–4 y HODGE §§5–6. No es una hipótesis de irreducibilidad residual omitida. |
| 53 retículo/Gram → 55 pairing y Higman | Restricción de la forma tensorial estándar, no una escala indeterminada. | COVOLUMEN, «Unión 53→55»; SELMER §11: e_T duales integrales y G=H_μF_μ⁻¹. Estabilizadores eliminados por N_ch. | **(a) esta unión algebraica**, independiente de exchange53. Para aplicar denominadores en e_c, precisar base level y usar construcción que preserve e_c; reparación explícita en SELMER §11.2, no incorporada al paper. |
| 55 `pg:odd` y sumas → presupuesto regular46 | Mismos C_odd,e_ℓ,e′_ℓ,β_ℓ y logℓ. | Clases impares para ℓ=2 incluidas; Σλ_ℓlogℓ≤3b log b y Σb v_ℓ(M)logℓ≤22b log b. | **(a) ensamblaje** SELMER §§7,14. Su corrección no resuelve los inputs exchange/multiplicidades. |

## Citas mutuas: ciclo de bibliografía frente a ciclo lógico

**55↔56: no se identificó ciclo lógico en el segmento reconstruido.** P56 recibe definiciones de retículos, pesos y clases de P55, cuya construcción M2/G4 precede a la cota de pérdida. Produce los exponentes locales; P55 aplica después dualidad y suma. En particular la mención de `pll:main` en `pki:data` se usa para identificar L_c y C_v, no para asumir la conclusión δ_v≤D_ℓ que P56 debe demostrar. Esto se comprobó en HODGE §6 y SELMER §§6,12,14; no es sólo una declaración del autor.

**53↔54: la reciprocidad bibliográfica tampoco basta para afirmar circularidad.** La fórmula de producto interno `pc:SW/pc:rallis` de P53 utilizada en P54 se reconstruyó en THETA SW01 independientemente de exchange; vuelve a P53 mediante la fórmula explícita de un lift. El intercambio53, en cambio, entra además en z=1 de IM54. La rama auditada presenta un **fallo de una identidad**, no un ciclo lógico demostrado. El bounded descent de tower y todas las importaciones transitivas no quedan certificados por este análisis de orden.

**46↔55/56:** los datos y tamaños admisibles de46 se reciben antes de concluir regularidad. La regularidad no se usa en las comprobaciones locales de esos tamaños. Esto descarta el supuesto ciclo en esa unión concreta, pero no certifica la existencia global de los datos ni todas las dependencias de46; véase su auditoría analítica.

## Propagación del error de caracteres de P53

El fallo **(b)** está en `pcu:product`, 53:3351–3360; falta α(det g)α(det y)β(det l). En `pcu:period` aparece β(det u) dentro de la integral. El módulo uno no permite eliminarlo. Véase [cálculo completo](ERROR-53-CARACTERES.md).

| Rama | Impacto probado | Lo que no se deduce |
|---|---|---|
| product→period→coeff→P-top→P-std→exchange `pcx:X` | Esa ruta escrita no prueba el intercambio. Hay que recalcular el período y su no anulación y conservar L_*. | No es un contraejemplo al enunciado de intercambio. |
| exchange→54 z=1→IM1→55 II→regular46 | La justificación de esa rama recibe el input no demostrado. El cotejo de hipótesis de IM y su uso permanece válido condicionalmente. | No se ha probado que todos los pares efectivamente usados puedan excluir z=1. |
| exchange→53 factorización/covolumen→46 | La cadena no queda certificada por esta prueba. | No implica que cada igualdad descendiente sea falsa. |
| 53 producto interno SW/Rallis→54 z≥2 | La revisión SW01 encuentra una ruta independiente; el doubling usa tensor con conjugada y cancela los caracteres. | No se extiende el cierre a todas las fuentes no compactas ni a todo tower. |
| 53 Gram→55; teoría local56 | No usan la identidad defectuosa. Sus cierres locales permanecen. | No reconstruyen por sí solos la regularidad o GRH. |

Los otros fallos53 tienen alcance distinto: P=∅ se corrige exigiendo no vacío, ya satisfecho en exchange por m≠(1); evaluación puntual no es Hilbert-acotada y necesita las normas de momentos/Schwartz. No deben agruparse con el error de caracteres como si una misma reparación resolviera los tres.

## Ramas restantes y límites de esta matriz

El responsable de theta confirmó los estados siguientes, cotejados con THETA; esta matriz no repite esa inspección independiente:

| Unión | Dictamen comunicado y obligación exacta |
|---|---|
| 49→50→49 | Aplicación abstracta reconstruida en HE01: root/count/av y rango aplicable. No hay un nuevo pendiente de rango identificado en esta unión. |
| 49→54 | Kernels, constante CS/CM y divisibilidad reconstruidos en CM01/KI01/LN01/BR01/AS01. La fórmula fuerte de δ_g no queda demostrada literalmente, pero las propiedades usadas se derivan independientemente; no confundir ambas afirmaciones. |
| 53 SW/Rallis→54 Prop.3.4→53 CL | SW01 reconstruye z≥2 sin exchange ni CL. Así, esta ruta no es circular. El cierre completo de CL exige además sus otros pasos; véase COVOLUMEN. |
| 54→55 | IM para z≥2 y la deducción desde IM están reconstruidos; z=1 continúa dependiendo del exchange53 defectuoso. |

 Para 52→51 y multiplicidades51→46/53/55, véanse SPANNING y MULTIPLICIDADES: una cota local cerrada no certifica la traza global. Para 43–45→46, véanse el informe de las filas y FORMA-COMPLETACION-43/HOCHSCHILD-43; su interpretación no sustituye la positividad de46.

**Estado de una unión no individualizada o no recorrida en los ledgers: (c).** Pendiente exacto general: identificar el enunciado fuente completo y las definiciones de sus símbolos, comprobar medidas/retículos/constantes/rangos en la instancia y rastrear que su prueba no presuponga la conclusión destino. El TSV no realiza ninguna de esas tres tareas. No se declara cerrada la red completa ni una ausencia universal de circularidad.

## Cotejos exhaustivos añadidos

[UNIONES-THETA](UNIONES-THETA.md) identifica275 reproducciones de los apéndices49/50/53/54, con cotejo de cuerpos, macros transitivas y referencias TeX. [UNIONES-SPANNING](UNIONES-SPANNING.md) identifica51 reproducciones de51/52, con inspección completa de sus21 diferencias de formato/referencias. El estado de fidelidad de una copia se mantiene separado del estado de su aplicación y de la corrección de la prueba fuente. Los inputs H/Hc/F de la cadena53 fueron reconstruidos posteriormente en [CADENA-53§6](CADENA-53.md); RS/T1 conserva la dependencia del exchange defectuoso.
