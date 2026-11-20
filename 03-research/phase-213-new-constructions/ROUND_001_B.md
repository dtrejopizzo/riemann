# Alcance de la desigualdad PRIME–ARCH recuperada de fase138

Estado: corrección documental; revisión independiente completada (PASS). No es un nuevo resultado de signo.

## Antecedente y decisión de selección

El índice maestro, Partes VI (registro20_02, fase138) y VII.C, enumera D.15.3(★)
como «PRIME ≤ ARCH + ½deg²» bajo PROVED. Se contrasta esa síntesis con
`../phase-138-row-d-detecting-cones/R138_001_ROUND1.md`, §0 y D.15.3(i),(ii),(v).
No se abre una construcción: la lectura de la fuente basta para decidir que no hay
una desigualdad global ya disponible que trasladar al Paper47.

## Alcance exacto

La fuente trabaja con F en D^W (Paper46, Definition11.1). Define

    deg⁺F = ∫F(t)e^(t/2)dt,
    deg⁻F = ∫F(t)e^(−t/2)dt,
    deg F = deg⁺F + deg⁻F,
    μ(F) = deg⁺F − deg⁻F.

Este grado es un funcional de momentos, no el grado de un polinomio ni el tamaño
de una matriz. El subespacio primitivo exige ambos momentos cero; deg F=0 por sí
solo no expresa esa doble condición.

D.15.3(i),(ii) prueban incondicionalmente la identidad del bloque polar:

    ½(deg F)² − B_pol(F,F) = ½μ(F)² ≥ 0.

D.15.3(v), para h=F⋆F^∨, prueba la equivalencia

    I_∞(F,F) ≤ ½(deg F)²
        ⇔ PRIME(h) ≤ ARCH(h) + ½(deg F)²,

usando la identidad I_∞(F,F)=PRIME(h)−ARCH(h).
La etiqueta PROVED corresponde a esta equivalencia. No afirma ninguno de sus
lados para todo F. Anular los momentos elimina el término de grado, pero no
proporciona la desigualdad que falta. Tampoco la holgura del bloque polar firma
la forma completa.

## Resultado del cotejo

Se aclaran las dos síntesis operativas y se registra la decisión en Parte V.
La equivalencia y la identidad polar siguen siendo herramientas válidas; no se
repite su derivación ni se presenta su lado derecho como un nuevo método.
No se refuta la desigualdad, no se añade un NO-GO matemático y no se altera ningún
paper. Una reapertura necesita una operación concreta que pruebe la comparación
completa, con el filtro de novedad de esta fase. Positividad global OPEN.
