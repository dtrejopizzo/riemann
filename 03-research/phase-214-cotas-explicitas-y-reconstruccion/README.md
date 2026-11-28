# Fase 214 — Cotas explícitas por ventana y reconstrucción

**Estado: CERRADA.** El resultado principal es **CONDITIONAL**: toma como entrada la conclusión espectral del paper46. El cierre y sus límites se documentan en [MEMO-FINAL.md](MEMO-FINAL.md).

## Pregunta y objetivo

Obtener una cota inferior explícita para la forma completa W_T en cada ventana, partiendo de su representación espectral positiva, y reconstruir los insumos analíticos y aritméticos que intervienen en la conclusión del paper46.

## Qué se hizo

- Se construyó un filtro contractivo que anula los dos momentos de Tate y amplía el soporte de manera controlada.
- Se combinaron la fórmula explícita, una cota del operador primo, el crecimiento arquimediano y una estimación de fuga de masa en frecuencia.
- Se fijaron parámetros explícitos para una desigualdad W_T(f) ≥ exp(−K)‖f‖₂² y se preparó un programa Arb para evaluar el tamaño de K.
- Se desarrollaron notas de reconstrucción sobre medias, multiplicidad, determinantes, conteos, representaciones y períodos de cadenas theta, conservando las hipótesis y obligaciones de cada paso.

## Resultados y alcance

| Resultado | Estado |
|---|---|
| Cota estrictamente positiva explícita en cada ventana | **CONDITIONAL** a que los ceros no triviales estén en la recta crítica, según la conclusión espectral utilizada de46 |
| Parámetros para los radios5 y10 | Evaluación numérica reproducible mediante Arb; no sustituye la demostración funcional |
| Reconstrucción de los insumos de46 | Desarrollo por bloques; el documento conserva sus resultados parciales y obligaciones, sin atribuirle una prueba independiente global |

La comparación espectral del filtro utiliza precisamente la localización de ceros. Emplearla para demostrar esa misma entrada sería circular. El certificado de altura finita, por sí solo, no proporciona el signo de los términos correspondientes a ceros exteriores.

## Archivos y orden de lectura

1. [MEMO-FINAL.md](MEMO-FINAL.md): resultado de la fase y alcance del cierre.
2. [COTA-EXPLICITA.md](COTA-EXPLICITA.md): enunciado, parámetros y demostración; conserva íntegro el desarrollo que antes figuraba en este README.
3. [verify_bounds.py](verify_bounds.py): evaluación de log10 K con python-flint/Arb; ejecutar `python3 verify_bounds.py` desde esta carpeta.
4. [reconstruccion.md](reconstruccion.md): cuaderno matemático de reconstrucción de los insumos.

## Relación con otras fases

La fase213 contiene antecedentes de los filtros y de las estimaciones de fuga. La [fase215](../phase-215-certificacion-privada-grh-rh-con-suplementos/README.md) reúne la auditoría posterior de la cadena global con sus suplementos; ese dictamen no elimina las hipótesis que utiliza la demostración de esta fase.

La fase216 está prevista para desarrollar resultados autónomos a partir de esas conexiones; no se inicia aquí.
