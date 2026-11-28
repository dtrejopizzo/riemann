> **V1: registro histórico, revisado en V2.** No aplicar sus objeciones de caracteres ni sus estados de propagación a los manuscritos corregidos sin consultar el [estado V2](../revision-v2/ESTADO.md). La cancelación especializada de caracteres corrige el impacto global atribuido en V1; se están consolidando los demás resultados.

# Uniones de los apéndices de P55 y P56

Fecha: 28-11-2026. Objeto: **fidelidad de todos los enunciados reproducidos en los apéndices de P55/P56**, cotejados con sus fuentes locales. Son 45 entradas (26 en55,19 en56), correspondientes a43 enunciados fuente distintos: la definición13.3 de46 aparece dos veces en56 y el lema13.4 de46 aparece en ambos papers. No se cuentan como enunciados reproducidos las simples menciones bibliográficas en prosa.

**Resultado de fidelidad: (a) en las45 entradas.** Hay23 coincidencias tras normalizar espacios y retirar etiquetas/títulos de entorno; las22 restantes sólo sustituyen referencias internas por números externos —o inversamente— y, en dos casos, convierten una ecuación numerada en ecuación con etiqueta explícita. Se inspeccionaron manualmente estas22 diferencias. Ninguna elimina una hipótesis, cambia una desigualdad, un cuantificador, una constante o un rango. Esto **no** otorga (a) a la demostración de cada resultado ni a toda utilización posterior.

Evidencia reproducible: [pares completos](../evidencia/uniones_selmer_hodge.json), [extractor/comparador](../evidencia/auditar_apendices_selmer_hodge.py). El comparador no acredita por sí solo equivalencia matemática: aquí se revisaron las diferencias. Las líneas son de `main.tex` en la revisión local auditada. «Exacta» no significa identidad byte a byte: se normalizan espacios y etiquetas.

## Inventario completo

En todas las filas el dictamen de **copia** es(a). Las diferencias indicadas son exclusivamente de referencias/presentación. Las condiciones de aplicación se separan debajo.

| Destino:línea | Fuente:número (línea) | Etiqueta fuente | Copia / diferencia inspeccionada |
|---|---|---|---|
| 55:7739 | 46:13.4 (2989) | `an:lem-sizes` | Referencia §14.3 de46 |
| 55:7777 | 46:14.5 (3598) | `au:free` | Exacta normalizada |
| 55:7782 | 46:14.27 (4584) | `au:equiv` | Exacta normalizada |
| 55:7789 | 46:14.36 (4812) | `au:mult` | Exacta normalizada |
| 55:7801 | 46:14.37 (4850) | `au:factor` | Exacta normalizada |
| 55:7816 | 46:14.39 (4895) | `def:au-regular` | Exacta normalizada |
| 55:7837 | 46:14.40 (4921) | `au:regular` | Exacta normalizada |
| 55:7841 | 46:14.41 (4965) | `au:onelift` | Exacta normalizada |
| 55:7857 | 46:14.42 (4992) | `au:hecke` | Exacta normalizada |
| 55:7862 | 46:14.43 (5013) | `au:Zj` | Exacta normalizada |
| 55:7867 | 49:5.2 (3428) | `ps:weil` | Referencias eq.62, Prop.2.17, §5.2.1 y Rem.7.18 de49 |
| 55:7916 | 53:3.2 (1767) | `pcx:X` | Etiqueta/entorno eq.12 y referencia §2.3 de53 |
| 55:7940 | 53:5.26 (9837) | `pgs:pairing` | Referencia Lemma5.25 de53 |
| 55:7958 | 54:2.2 (544) | `po:facts` | Referencia eq.1 de54 |
| 55:7971 | 54:3.6 (1827) | `pex:dint` | Exacta normalizada |
| 55:7978 | 54:3.8 (1898) | `pex:IM` | Exacta normalizada |
| 55:7992 | 54:3.12 (2038) | `pex:IM1` | Referencia Lemma3.6 de54 |
| 55:8001 | 56:2.4 (416) | `pki:def-reads` | Exacta normalizada |
| 55:8011 | 56:2.5 (436) | `pki:generic` | Exacta normalizada |
| 55:8023 | 56:2.10 (486) | `pki:data` | Prop.5.2 de55 se vuelve referencia interna; Prop.2.8 de56 |
| 55:8037 | 56:2.13 (552) | `pki:crys` | Referencia Lemma2.12 de56 |
| 55:8054 | 56:7.1 (5892) | `pkj:conv` | Dos referencias Prop.2.9 de56 |
| 55:8073 | 56:7.9 (6095) | `pkj:chart` | Referencias Conv.7.1 y Def.2.4 de56 |
| 55:8080 | 56:9.2 (7399) | `pkw:def-pcris` | Dos referencias Lemma9.3(i) de56 |
| 55:8090 | 56:9.9 (7594) | `pkw:T2` | Referencias Defs.9.5 y3.4 de56 |
| 55:8098 | 56:9.23 (7937) | `pkw:G4` | Exacta normalizada |
| 56:8002 | 46:13.2 (2930) | `an:def-sparse` | Exacta normalizada |
| 56:8013 | 46:13.3 (2954) | `an:def-data` | Exacta normalizada |
| 56:8047 | 46:13.3 (2954) | `an:def-data` | Exacta normalizada |
| 56:8081 | 46:13.4 (2989) | `an:lem-sizes` | Referencia §14.3 de46 |
| 56:8119 | 55:2.5 (493) | `pg:sums` | Referencia Prop.2.27 de55 |
| 56:8128 | 55:2.6 (563) | `pg:def-summand` | Exacta normalizada |
| 56:8151 | 55:2.28 (1383) | `pg:loss` | Referencias Thm.2.10, Prop.4.5, Thm.5.8(d), Rem.5.7 de55 |
| 56:8165 | 55:4.5 (2223) | `pri:loss` | Referencias Def.2.7, Props.2.28 y4.6 de55 |
| 56:8192 | 55:4.6 (2260) | `pri:BL` | Referencia Def.8.42 de55 |
| 56:8207 | 55:5.1 (3213) | `pll:def` | Exacta normalizada |
| 56:8243 | 55:5.2 (3268) | `pll:main` | Referencia Prop.2.28, etiqueta/entorno eq.9 y §2.1 de55 |
| 56:8260 | 55:5.4 (3354) | `pll:dual` | Exacta normalizada |
| 56:8269 | 55:5.5 (3408) | `pll:ribet` | Exacta normalizada |
| 56:8280 | 55:5.6 (3448) | `pll:exp` | Exacta normalizada |
| 56:8286 | 55:5.8 (3487) | `pll:exponent` | Referencia Prop.5.2 de55 |
| 56:8304 | 55:5.10 (3528) | `pll:sum` | Referencia eq.9 de55 |
| 56:8309 | 55:6.4 (3763) | `pga:depth0` | Exacta normalizada |
| 56:8322 | 55:6.6 (3938) | `pga:G45` | Referencias Prop.6.2 y Lemma6.4 de55 |
| 56:8341 | 55:8.27 (7092) | `pay:eta` | Referencias Props.6.11 y4.6(c) de55 |

## Fidelidad frente a validez y rango de aplicación

Las referencias numéricas de la tabla se cotejaron con los entornos fuente. Los números de ecuación se identifican por las correspondientes etiquetas fuente (`pl:eq-w5`, `pcx` intercambio, `po:eq-w5`, `pll:eq-place`); los cambios de presentación no cambian sus términos. Las definiciones no se sustituyen por versiones más débiles en estas copias. Para el significado de los parámetros en las aplicaciones efectivas se usó además la lectura de las secciones principales registrada en los ledgers siguientes.

| Grupo de importaciones | Resultado de la revisión de hipótesis/rango y límite de la conclusión |
|---|---|
|46 tamaños/datos/sparsity →55/56|Mismos datos admisibles y tamaños. La identificación de letras y ventanas de56 con los datos46 está reconstruida en [HODGE §6](HODGE.md). Reproducir `au:regular`, `au:factor`, `au:onelift` o `au:Zj` no demuestra esos teoremas ni constituye por sí solo un uso como premisa.|
|46 `au:regular` en55|La copia coincide; el resultado que55 debe aportar se deduce de `pg:main` y `pg:sums`, no de asumir su copia. Se verificó el paso R1–R3 para ambos signos y j≤m en [MATRIZ-UNIONES](MATRIZ-UNIONES.md). Su verdad global sigue dependiendo de los inputs allí indicados.|
|49 `ps:weil` →55|Las condiciones W y referencias de normalización se conservan. Las propiedades efectivamente utilizadas fueron reconstruidas en [THETA](THETA.md); la fórmula fuerte para la fase δ_g no debe confundirse con las propiedades más débiles utilizadas. La fidelidad de la copia no elimina esa distinción.|
|53 `pcx:X` →55|**Copia correcta de un enunciado cuya prueba escrita no quedó establecida:** el fallo `pcu:product` se detalla en [ERROR-53-CARACTERES](ERROR-53-CARACTERES.md). No es un cambio de rango de la cita ni un contraejemplo al enunciado de intercambio.|
|53 `pgs:pairing` →55|Identificación de retículo y forma tensorial verificada, independiente de exchange; véanse [COVOLUMEN](COVOLUMEN.md) y [SELMER §11](SELMER.md). La restricción a e_c exige la precisión/reparación de base level registrada allí; no queda subsanada por copiar el lema.|
|54 `po:facts`, `pex:dint`, `pex:IM`, `pex:IM1` →55|En la deducción de II se conservan ambos embeddings, integridad, factores omitidos y todos los pares críticos. Rama z≥2 reconstruida; z=1 de IM1 depende de exchange53. No se verificó que se pueda excluir z=1 de todos los usos. [SELMER §13](SELMER.md).|
|56 `pki:def-reads`, `generic`, `data`, `crys`, convenciones/cartas →55|Las copias conservan NM y ventanas: no se detectó una hipótesis NM suprimida en la transcripción. La aplicación al sistema de pesos y su alternativa para λ≥h³ se comprobó en [HODGE §§5–6](HODGE.md). NM es suficiente en el resultado pertinente; no es necesaria para que cada instancia tenga defecto cero.|
|56 `pkw:def-pcris`, `T2`, `G4` →55|Se conservan órdenes tame, conductor y clases permitidas. El polinomio q_s puede depender de s; este resultado no equivale a un polinomio fijo que mate todos los elementos de inercia. Cobertura de todos ℓ/retículos según [HODGE](HODGE.md), bajo sus hipótesis expresas.|
|55 `pg:sums`, `pg:loss`, `pri:loss`, `pll:main`, `exponent`, `sum` →56|Enunciados de aplicación global/contabilidad reproducidos fielmente. No deben usarse sus conclusiones de pérdida como premisa de la cota local que las demuestra. Se reconstruyó el orden de construcción de clases→cota local→dualidad/suma, sin ese ciclo, en [HODGE §6](HODGE.md) y [SELMER §§12,14](SELMER.md).|
|55 `pg:def-summand`, `pll:def`, `dual`, `ribet`, `exp` →56|Mismos retículos, normalización de longitud y clases. La revisión de Ribet reconstruyó la hipótesis residual M4 expresamente incluida; no se añadió una irreducibilidad residual inexistente a la unión. Véase [SELMER §§1–4](SELMER.md).|
|55 `pri:BL` →56|**El apéndice copia fielmente también la afirmación defectuosa sobre un mismo polinomio para todo s.** El defecto literal no es una discrepancia de copia; la aplicación local correcta usa q_s. El alcance base level/e_c y reparación no incorporada al paper están separados en [SELMER §11](SELMER.md).|
|55 `pga:depth0`, `pga:G45`, `pay:eta` →56|Se conservan las condiciones de etiqueta/profundidad y los mismos enunciados fuente. Las frases defectuosas sobre normas de extensiones de campos finitos y órdenes de raíces, y las reparaciones que conservan cotas, constan en [SELMER §§6,12](SELMER.md). La fidelidad no certifica la prueba fuente sin esas correcciones.|

## Citas mutuas y alcance exhaustivo

El inventario es exhaustivo para los **entornos de enunciados reproducidos en esos dos apéndices**. No pretende que cada referencia bibliográfica en las pruebas de55/56 sea uno de estos45 entornos ni que la igualdad del cuerpo audite automáticamente todas las convenciones transitivas de todos los papers. Las convenciones relevantes a las aplicaciones locales/automorfas señaladas arriba se verificaron separadamente en los ledgers; las no individualizadas no reciben certificación por este inventario.

Las flechas46→55→46 y55→56→55 no son por sí solas círculos. En los tramos reconstruidos, primero se fijan datos, retículos y clases; después56 prueba la cota local y55 concluye regularidad. La copia en apéndice de una conclusión global no se usa como su propia prueba. La ruta z=1 de54 sí recibe exchange53 no demostrado por la prueba escrita; esa dependencia permanece aunque todas sus copias sean fieles. Véase [MATRIZ-UNIONES](MATRIZ-UNIONES.md) para la propagación exacta.
