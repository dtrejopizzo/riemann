# Uniones individualizadas de51 y52

Se leyeron completos los dos apéndices y se extrajeron sus51 enunciados reproducidos (29 en51,22 en52). Se cotejaron con los entornos fuente en46,49,51,52.30 coinciden después de eliminar etiquetas, referencias y espacios; las21 diferencias restantes se inspeccionaron una por una. Son migraciones de referencias internas a citas externas, numeración de ecuaciones o formato. **No se encontró una modificación de fórmula, hipótesis o rango en los cuerpos de estas51 citas.**

Evidencia: `evidencia/comparar_apendices_spanning.py`, `uniones_spanning_copias.json`, `uniones_spanning_diffs.txt` y `mapa_numeros_spanning.json`. El extractor sólo sirve para cotejo: no demuestra la validez de los teoremas ni la corrección semántica de una aplicación. El control de los localizadores numéricos se registra separadamente de la igualdad de cuerpos.

## Hipótesis y aplicaciones principales

- **46→51/52, datos y tamaños:** permanecen D1–D8 y S1–S7 completos. No se reemplaza la ventana bilateral de logN por una mera existencia de N. S7 suministra n≥100, k≥512000n⁹, f≤b/1000, N≤b^(60n), separación Δ, normas de κ y las cotas de volumen y dimensión usadas. Su construcción independiente está en ANALITICA; su consumo local se recorrió en SPANNING.
- **49→51, coeficiente real y grado formal:** conserva h≥n²+1 y la medida compatible con volumen1 en el compacto, sin renormalizar una por plaza después de multiplicar. La prueba FJ requiere la reparación de orden documentada; fidelidad del enunciado no elimina ese defecto de prueba.
- **52→51, sistema real:** H0–H5 permanecen expresos; la masa es (1+b⁻¹⁰)/deg_τ, no una constante absoluta. Los dos enunciados de la forma superior (Gram global y a cabeza fija) se conservan. SPANNING reconstruye las hipótesis en las instancias usadas.
- **52→51, sistema finito:** T es finito, estable por conjugación y contiene MN; para Siegel además contiene los lugares donde B no es unidad. Se conserva la misma Z(A,d) entre la forma superior y el paso de Siegel, y la masa (1+b⁻⁶)b^(−6k#A). La familia de cuádruplas debe ser distinta y satisfacer |τ(t_j)|>N. No se sustituyen estas condiciones por un simple recuento sin multiplicidades.
- **51→52, Bessel:** B1–B5′ incluyen soporte compacto módulo U, no sólo módulo R. El paso usa que H real es compacto. El escalar c_W y la norma del período tienen el mismo grado formal; B6 y B7 vienen de la construcción antes de invocar los sistemas locales.
- **51→52, sieve y constantes:** la transformación inversa es w↦w⁻¹ en los lugares reales y w↦M⁻¹w⁻¹ en el lugar finito. Se mantiene el producto ∏c_a y el error b^(2403n⁹f). El retorno L2 recibe las mismas tres entradas R/F/S y las desigualdades de tamaños, no presupone ya el segundo momento final.
- **51↔52, Siegel y fibras:** el teorema fuente exige medidas y normalización expresas y convergencia absoluta del integral z. La dirección errónea del cutoff en una prueba auxiliar sigue requiriendo la reparación indicada en INVENTARIO-CORRECCIONES. Las citas no cambian ese enunciado ni reparan por sí solas su demostración.

Las importaciones que reproducen Spanning, moment, spreading o local systems en el paper que desarrolla sus inputs son enunciados de retorno/contexto: no se toman automáticamente como premisas independientes. La secuencia real auditada es datos y Bessel → sistemas/fibras → sieve y L2 → momento → spreading; las citas mutuas no prueban por sí solas un ciclo.

## Inventario de fidelidad de los enunciados

En la última columna **(a) copia** significa concordancia del cuerpo e hipótesis con la fuente inspeccionada; la validez de la aplicación se evalúa en las fichas anteriores y en SPANNING/MULTIPLICIDADES. No equivale a aprobar cada línea de la prueba fuente. Los localizadores numéricos no se dan por buenos sólo por haber sido borrados al normalizar.

| Destino y línea | Fuente | Etiqueta / línea | Cotejo |
|---|---|---|---|
| 51:10753 | 46 13.3 | `an:def-data` / 2954 | (a) copia; igual normalizada |
| 51:10787 | 46 13.4 | `an:lem-sizes` / 2989 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 51:10825 | 46 14.5 | `au:free` / 3598 | (a) copia; igual normalizada |
| 51:10830 | 46 14.14 | `thm:srcB` / 4012 | (a) copia; igual normalizada |
| 51:10838 | 46 14.29 | `au:ramcount` / 4619 | (a) copia; igual normalizada |
| 51:10842 | 46 14.30 | `au:onetranslate` / 4637 | (a) copia; igual normalizada |
| 51:10854 | 46 14.31 | `au:few` / 4666 | (a) copia; igual normalizada |
| 51:10868 | 46 14.32 | `au:moment` / 4692 | (a) copia; igual normalizada |
| 51:10882 | 46 14.34 | `au:spread` / 4778 | (a) copia; igual normalizada |
| 51:10887 | 46 14.36 | `au:mult` / 4812 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 51:10899 | 49 2.19 | `pwf:haar` / 1137 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 51:10908 | 49 3.17 | `pco:FJ` / 1876 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 51:10912 | 49 3.18 | `pco:minors` / 1898 | (a) copia; igual normalizada |
| 51:10927 | 49 3.19 | `pco:equiv` / 1938 | (a) copia; igual normalizada |
| 51:10941 | 49 3.21 | `pco:indep` / 2029 | (a) copia; igual normalizada |
| 51:10947 | 49 3.23 | `pco:K` / 2097 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 51:10959 | 49 3.25 | `pco:decay` / 2148 | (a) copia; igual normalizada |
| 51:10964 | 49 8.1 | `pz:def-type` / 7759 | (a) copia; igual normalizada |
| 51:10978 | 49 8.4 | `pz:types` / 8021 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 51:11000 | 52 2.17 | `pfr:R` / 926 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 51:11017 | 52 2.19 | `pfr:haar` / 1001 | (a) copia; igual normalizada |
| 51:11024 | 52 2.41 | `pfr:rearr` / 1472 | (a) copia; igual normalizada |
| 51:11028 | 52 4.1 | `prp:heis` / 2665 | (a) copia; igual normalizada |
| 51:11036 | 52 5.12 | `pff:massK` / 3725 | (a) copia; igual normalizada |
| 51:11041 | 52 5.13 | `pff:L1` / 3741 | (a) copia; igual normalizada |
| 51:11046 | 52 5.24 | `pff:fixed` / 4104 | (a) copia; igual normalizada |
| 51:11058 | 52 5.28 | `pff:F` / 4192 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 51:11073 | 52 5.29 | `pff:S` / 4223 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 51:11090 | 52 6.35 | `pfg:siegel` / 5462 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 52:5524 | 46 13.4 | `an:lem-sizes` / 2989 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 52:5562 | 46 14.5 | `au:free` / 3598 | (a) copia; igual normalizada |
| 52:5567 | 51 2.1 | `pb:KR` / 554 | (a) copia; igual normalizada |
| 52:5573 | 51 2.16 | `pb:bessel` / 1152 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 52:5610 | 51 2.21 | `pb:massratio` / 1336 | (a) copia; igual normalizada |
| 52:5621 | 51 3.6 | `pbv:haar` / 1777 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 52:5627 | 51 3.16 | `pbe:ds` / 2331 | (a) copia; igual normalizada |
| 52:5647 | 51 3.18 | `pbe:local` / 2376 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 52:5678 | 51 3.22 | `pbe:bessel` / 2622 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 52:5700 | 51 3.33 | `pbm:pos` / 3168 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 52:5712 | 51 3.39 | `pbm:E4` / 3396 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 52:5718 | 51 3.41 | `pbm:cell` / 3450 | (a) copia; igual normalizada |
| 52:5730 | 51 3.42 | `pbm:orbit` / 3525 | (a) copia; igual normalizada |
| 52:5740 | 51 3.44 | `pbm:system` / 3617 | (a) copia; igual normalizada |
| 52:5759 | 51 3.50 | `pbm:sieve` / 3813 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 52:5773 | 51 3.51 | `pbm:inputs` / 3890 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 52:5806 | 51 3.52 | `pbm:const` / 3928 | (a) copia; igual normalizada |
| 52:5818 | 51 3.53 | `pbm:L2` / 3994 | (a) copia; diferencias de referencias/formato inspeccionadas |
| 52:5828 | 51 7.2 | `pbp:main` / 6801 | (a) copia; igual normalizada |
| 52:5837 | 51 7.12 | `pbp:tb-witt` / 7062 | (a) copia; igual normalizada |
| 52:5846 | 51 8.80 | `pbo:GF` / 10235 | (a) copia; igual normalizada |
| 52:5854 | 51 8.81 | `pbo:append` / 10280 | (a) copia; diferencias de referencias/formato inspeccionadas |

## Control de referencias y macros completado

El agente theta reutilizó su verificador sobre estas51 filas: todas las referencias numéricas se resolvieron contra los auxiliares LaTeX de las fuentes, sin discrepancias. La comparación de macros, incluyendo su clausura transitiva, tampoco encontró diferencias. Evidencia: `cotejo_51_spanning_refs.json`, `cotejo_51_spanning_macros.json` y `check_spanning_aux_macros.py`. Esto completa la fidelidad semántica de las reproducciones, sin convertir en correctas las líneas defectuosas de las pruebas fuente.
