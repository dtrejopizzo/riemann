# Auditoría de fases 90–101: de la corriente Kato al muro de identificación del divisor

## Dictamen ejecutivo

El bloque 90–101 no demuestra RH. Su aporte válido es una larga secuencia de identidades finitas, continuaciones polinómicas, factorizaciones por cofactores, teoremas de clausura condicionales y no-go que eliminan atajos. La reducción es coherente: el objeto inicial, la línea Kato, el cociclo de Euler, el numerador bordeado, el Jacobiano característico, la respuesta von Mangoldt, el conmutador, la cáscara de Fourier y las corrientes Stieltjes/calor son coordenadas del mismo obstáculo, no pruebas acumulativas de menor fuerza.

El punto de fuerza-RH queda localizado de tres maneras equivalentes en contenido:

```text
DIRECT-BORDERED-ANCHOR / RDI-ANCHOR
        = identificación Gamma–Euler del determinante bordeado;

LOCAL-COVARIANT-IDENT / STIELTJES-IDENT
        = identificación de una transformada positiva en un intervalo seguro;

XI-PARITY-CURRENT-NULL
        = anulación de todas las corrientes principales separadoras del divisor de Xi.
```

La tercera es **EQUIVALENTE-A-RH**; `TRUE-DIVISOR-IDENT` (convergencia sensible al soporte y multiplicidad lineal antes de contraer) es una condición suficiente más fuerte. La convergencia de derivadas logarítmicas en cualquier intervalo seguro de E101.095 también tiene fuerza RH por propagación Pick–Nevanlinna. Las identidades, autoadjunciones finitas, cotas de colas, diagramas de cofactores y ensayos finitos no cubren esta identificación.

**Convención.** PROBADO designa una identidad o implicación con hipótesis expuestas y demostración interna. CONDICIONAL requiere sus hipótesis. NUMÉRICO es reproducible sólo a sección finita. CONJETURAL es un mecanismo aún no cerrado. REFUTADO es una inferencia o ruta descartada. EQUIVALENTE-A-RH es una reformulación que fuerza RH. INCOMPLETO es un programa con un hueco no convertido en teorema.

## Cobertura documental

Se leyeron los README, todos los cierres, el ledger de 101 y los documentos matemáticos `E90`–`E101`. La serie 101 contiene 96 documentos `E101.001`–`E101.096`; se inspeccionaron también sus tres sondas Python. La ejecución conjunta de las sondas disponibles terminó sin fallo, pero no produjo certificado asintótico adicional; sus salidas, cuando las hay en los textos, quedan clasificadas como NUMÉRICO. No se trató una sonda como prueba de un límite.

| Fase | Cobertura | Clasificación dominante | Resultado heredable |
|---|---:|---|---|
| 90 | 7/7 Markdown | PROBADO + INCOMPLETO | corriente Kato y defecto bilateral exactos |
| 91 | 6/6 Markdown | PROBADO + REFUTADO | equivalencia coborde/fuga y defecto de derivación |
| 92 | 9/9 Markdown | PROBADO + EQUIVALENTE-A-RH | numerador global proyectivo; ancla intacta |
| 93 | 7/7 Markdown | PROBADO + EQUIVALENTE-A-RH | teorema `DIRECT-BORDERED-ANCHOR ⇒ Omega7` |
| 94 | 8/8 Markdown | PROBADO + NUMÉRICO | corriente global de cofactores y polinomio de dos generadores |
| 95 | 7/7 Markdown | PROBADO + CONDICIONAL | Jacobiano característico en cartas simples |
| 96 | 7/7 Markdown | PROBADO + EQUIVALENTE-A-RH | respuesta global von Mangoldt acoplada |
| 97 | 8/8 Markdown | PROBADO + NUMÉRICO | sensibilidad canónica y conmutador Euler |
| 98 | 7/7 Markdown | PROBADO | división interna/cáscara exactamente emparejada |
| 99 | 8/8 Markdown | PROBADO + NUMÉRICO | sandwich bordeado y corrección característica separada |
| 100 | 7/7 Markdown | PROBADO | corrección característica = regla de la cadena |
| 101 | 98/98 Markdown, 3/3 sondas | PROBADO/NO-GO + EQUIVALENTE-A-RH | atlas de discriminantes, no identificación cofinal |

La cobertura de 101 se agrupa sólo para lectura; cada entrada `E101.001`–`.096` fue contrastada contra README y ledger, sin contar los resúmenes como resultado independiente.

| Serie E101 | Estado auditado | Contenido que sobrevive |
|---|---|---|
| .001–.009 | PROBADO | proyección horizontal/cotangente, factorización y corriente covariante exactas |
| .010–.023 | PROBADO; cierre final EQUIVALENTE-A-RH | compacidad y unicidad seguras; identificar el límite en un intervalo sigue siendo la carga |
| .024–.031 | PROBADO / REFUTADO | muros de signo, deriva a la derecha, resolvente y coherencia; las condiciones finitas no determinan el divisor |
| .032–.044 | PROBADO; objetivo EQUIVALENTE-A-RH | compactificación momento–calor–Weil, colas explícitas y estabilidad; falta la comparación central |
| .045–.053 | PROBADO + CONDICIONAL | atribución exacta de `DIRECTIONAL-IDENT`; reducción de colas a estimaciones cuantitativas no demostradas |
| .054–.061 | PROBADO / REFUTADO | puerta de novedad, holonomía plana, obstáculo Hardy y no-go Abel; no aparece una norma que cierre IDENT |
| .062–.070 | PROBADO / REFUTADO / INCOMPLETO | secantes, momentos mezclados, desplazamientos y Pearson; regresan al mismo residual firmado |
| .071–.085 | PROBADO / REFUTADO | falsadores de cuarteto, muros de jets, diagonal y grafo conjugado; el Gram de paridad separa sólo tras identificar el divisor |
| .086–.090 | PROBADO / INCOMPLETO | discriminantes Abel/Mellin y separación Toeplitz–Hankel; queda covarianza de cocientes de fuerza RH |
| .091–.092 | PROBADO / REFUTADO | auditoría de adjunto normal/no normal; métricas y correcciones universales no construyen el grafo conjugado |
| .093 | PROBADO bajo even-simple; EQUIVALENTE-A-RH | estrella finita y Hessiano nulo; corriente de Xi no transportada |
| .094 | PROBADO / CONDICIONAL | clasificación de normalidad de rasgos; normalidad cuadrada no identifica Xi |
| .095 | PROBADO; objetivo EQUIVALENTE-A-RH | defecto fuente exacto y propagación Pick–Nevanlinna; `C_core→0` tiene fuerza RH |
| .096 | PROBADO / REFUTADO | no-go de inversión de un nivel; `TRUE-DIVISOR-IDENT` permanece abierto y de fuerza RH |

## Reconstrucción por fase

| Fase | Claims clasificados y dependencia real |
|---|---|
| **90** | **PROBADO:** residuo espectral, fórmula Kato con cancelación exacta de `dot mu`, expansión finita por celdas primas y defecto de capa bilateral. **CONDICIONAL:** dominancia de una línea y comparación Feshbach estática requieren no anulación y resolvente complementario. **INCOMPLETO/EQUIVALENTE-A-RH:** `PROJECTIVE-KATO-EULER = RDI-ANCHOR` no es criterio nuevo. |
| **91** | **PROBADO:** `C_t dot v_t=Q_tH_Pv_t` y equivalencia exacta entre fórmula sin inversa y coborde con fuga reducida. **REFUTADO:** integrar la línea física por el gauge del vector base; el defecto `(I-Z^{-1})delta v` no desaparece porque `ker X` físico es trivial. **INCOMPLETO:** la fuga segura es el mismo cuello de botella. |
| **92** | **PROBADO:** el determinante bordeado global elimina el denominador de Feshbach, atraviesa singularidades y absorbe ambas paridades en una clase proyectiva. El diagonal cofinal sólo combina dos convergencias ya dadas. **REFUTADO como obligación mínima:** `DOM-E`, `DOM-M`, ventanas y anchuras pareadas. **EQUIVALENTE-A-RH:** `CLUSTER-RDI-ANCHOR`; la eliminación de coordenadas singulares no identifica el límite Euler–Gamma. |
| **93** | **PROBADO:** `DIRECT-BORDERED-ANCHOR ⇒ SR-SAFE ⇒ Omega7 ⇒ RH`, bajo los insumos citados de producto independiente, real-rootedness y normalidad. **EQUIVALENTE-A-RH:** el ancla es exactamente `RDI-ANCHOR`, no una relajación. **INCOMPLETO:** la frase “un solo teorema abierto” describe su contabilidad, no una reducción de dificultad. |
| **94** | **PROBADO:** `N=det M-h^T adj(M)b`, ley de desplazamiento y fórmula polinómica de dos generadores, válidas incluso en `det M=0`. **NUMÉRICO:** certificación multiprecisión de identidades finitas. **REFUTADO:** emparejar por separado cofactores derivados. **EQUIVALENTE-A-RH:** `COFACTOR-CELL-ANCHOR` equivale al ancla directa. |
| **95** | **PROBADO:** lift `(t,mu)`, fórmula `Jac(P,chi)/(P partial_mu chi)` y transición de cartas. **CONDICIONAL:** una prueba por tangentes exige rama simple o paso por cluster; no se permite dividir por `partial_mu chi=0`. **EQUIVALENTE-A-RH:** `CHARACTERISTIC-JACOBIAN-ANCHOR`. |
| **96** | **PROBADO:** polarización y expansión lineal de Jacobianos por celdas primas, manteniendo el acoplamiento no lineal completo. **REFUTADO:** matching célula por célula. **EQUIVALENTE-A-RH:** la suma firmada `BASE+SUMDEF→0` es el mismo ancla determinantal. |
| **97** | **PROBADO:** representante de traza único, identidad Euler–conmutador y reducción polinómica segura del adjugado bordeado. **NUMÉRICO:** residuos de trazas de dimensión finita. **INCOMPLETO:** el adjugado normalizado característico no se vuelve sandwich; introducir inversa en la curva singular sería inválido. |
| **98** | **PROBADO:** lift físico de rango finito y separación exacta `BJ=INT+SHELL`; hay cuatro cruces de Fourier, ni menos ni más. **INCOMPLETO/EQUIVALENTE-A-RH:** estimar antes del emparejamiento destruye la cancelación; la suma `SENSITIVITY-BOUNDARY-SHELL` es el ancla. |
| **99** | **PROBADO:** sensibilidad restringida, conmutador aumentado, identidad de sandwich y fuentes Gamma–Euler/borde/cáscara. **NUMÉRICO:** certificación en curva singular simple. **Corrección esencial:** `adj(K)[Z,H]adj(K)=0` es compatibilidad, no fórmula de `[Z,adj(K)]`; la corrección característica debe conservarse normalizada. |
| **100** | **PROBADO:** `adj(K)/partial_mu chi=-Pi`, y la traza del conmutador da `dot mu`. **PROBADO:** `Gamma_t dot mu_t` es exactamente la regla de la cadena. **REFUTADO:** contarlo como fuente aritmética adicional o exigir su pequeñez separada. |
| **101** | **PROBADO:** un gran atlas de coordenadas finitas, transformadas Stieltjes/momento/calor, reducción de rango dos, identidades duales y no-go de rutas que pierden conjugación, multiplicidad lineal o cancelación firmada. **CONDICIONAL:** las construcciones de estrella y operador de `.093` requieren even-simple cofinal. **NUMÉRICO:** perfiles de calor, Jacobi y Abel son diagnósticos. **EQUIVALENTE-A-RH:** `LOCAL-COVARIANT-IDENT`, `STIELTJES-IDENT`, `XI-PARITY-CURRENT-NULL` y el límite de derivada logarítmica segura. **REFUTADO:** inversión finita o holomorfa de un nivel como sustituto del divisor. |

## Matriz de dependencias 90→101

```text
90  corriente de línea / defecto de capa
     └─ 91  coborde = fuga reducida; no-go del vector base
         └─ 92  numerador bordeado global y continuación proyectiva
             └─ 93  DIRECT-BORDERED-ANCHOR = RDI-ANCHOR ⇒ Omega7
                 ├─ 94  cofactores + desplazamiento
                 │   └─ 95  Jacobiano en la curva característica
                 │       └─ 96  suma de respuesta von Mangoldt
                 │           └─ 97  sensibilidad y conmutador Euler
                 │               └─ 98  interno + cáscara Fourier
                 │                   └─ 99  sandwich de fuentes bordeadas
                 │                       └─ 100 regla de cadena de mu
                 │                           └─ 101 corriente covariante,
                 │                              Stieltjes/calor/divisor
                 └─ 101 rutas opcionales LP/prolate/radical y sus no-go

101: LOCAL-COVARIANT-IDENT = STIELTJES-IDENT
       = identificación del mismo ancla de 93 en otra coordenada
       └─ XI-PARITY-CURRENT-NULL ⇔ RH ⇔ Omega7
             ↑
   TRUE-DIVISOR-IDENT: suficiente más fuerte; no demostrada
```

No hay flecha demostrada desde `90`–`101` hacia la identificación final. Las flechas horizontales de 94–100 son cambios algebraicos de coordenada del defecto de 93. Las rutas de 101 que usan prolate, Fourier, Abel, jets, momento o transportes sólo son útiles si suministran una identidad firmada que falle en el control con cuarteto fuera de línea; hasta ahora no lo hacen.

## Controles de consistencia y hallazgos críticos

1. **Circularidad y equivalencias disfrazadas.** El propio E93.003 identifica `DIRECT-BORDERED-ANCHOR` con `RDI-ANCHOR`; E96.005, E98.005, E99.005 y E100.005 sólo reescriben su suma acoplada. Presentarlas como avances independientes inflaría la evidencia. E101.054 confirma que Stieltjes, momentos, beta, calor, Weil gaussiano, residuo direccional y corriente emparejada forman un atlas del mismo discriminante.

2. **El ancla directa tiene fuerza RH exacta.** E93.002 es una implicación correcta bajo sus hipótesis de familia finita y producto independiente. No autoriza tratar `DIRECT-BORDERED-ANCHOR`, `C_core→0`, `SR-LOG` o `STIELTJES-IDENT` como estimaciones auxiliares: E101.019/.021/.038/.095 las clasifican como **EQUIVALENTE-A-RH**.

3. **Adjugados y cofactores.** La continuación polinómica evita la inversa singular y es válida. Pero ni `B[W,adj(B)]B=-det(B)[W,B]` ni su versión sandwich resuelven el término característico: en `det K=0` sólo queda `adj(K)[W,K]adj(K)=0`. E99 conserva correctamente `[Z,adj(K)/partial_mu chi]`; E100 prueba que es la regla de la cadena y exige recombinación, no desaparición.

4. **Cambio de definición raw/core.** E101.025 y E101.095 obligan a retirar de los objetivos cualquier fórmula que confunda la masa hiperbólica cruda con la característica núcleo o que omita la malla exterior. El objeto fuente correcto es `C_core`, tras quitar exactamente el factor exterior; el producto bilateral y la antisimetrización lineal de dos bordes difieren por un defecto de fase explícito. No hay licencia para sustituir `T_+-T_+(-z)` por `T_+` ni por `T_+T_+(-z)`.

5. **Pick–Nevanlinna.** E101.095 prueba una propagación válida para enteras pares reales de orden a lo sumo uno con ceros reales. Su fuerza procede de las multiplicidades positivas del cociente logarítmico completo, no de una transferencia racional incremental. Un punto seguro no basta; un intervalo sí. La hipótesis de real-rootedness finita/even-simple sigue siendo CONDICIONAL a lo largo de una familia cofinal.

6. **Paridad, corriente y estrella finita.** E101.093 cierra la estrella positiva y el Hessiano sólo bajo even-simple. La contracción de átomo de rango uno es cero en toda sección finita porque cada fibra ya es real: es **PROBADO pero no discriminante**. `NA-4_F` no implica `NA-4_Xi`; confundirlos sería una sustitución circular del divisor límite por el hecho finito de autoadjunción.

7. **Borrador E101.094.** La desigualdad de solapamiento y la clasificación por normalidad de rasgo son resultados algebraicos demostrados en el texto. Su conclusión correcta es negativa: normalidad cuadrada de rasgos pares sólo cancela fuga en una métrica dada; construir una métrica por bloques de raíces es interpolación del divisor. No hay paso hacia `Xi`.

8. **Borrador E101.095.** Las factorizaciones, colas y teorema de propagación separan correctamente infraestructura de identificación. El salto abierto es precisamente `C_core_(L,N)→0` en intervalo seguro o la cota ponderada ground-model; ambos deben fallar en el control plantado. Toda lectura que concluya RH de la convergencia de la cola Euler o de la ecuación de autovalor es **REFUTADA** por sus secciones 9–10.

9. **Borrador E101.096 y `TRUE-DIVISOR-IDENT`.** La representación firmada real de cualquier cuarteto para un espacio holomorfo finito y la red de diferencias finitas muestran que los momentos holomorfos, aun cofinales, no controlan soporte transversal. Productos de trazas crean todos-los-pares y peso `m_rho^2`; restringir después al grafo conjugado no recupera multiplicidad lineal. Una convergencia Radon/distribucional de divisores finitos reales preservaría soporte real y por ello es **EQUIVALENTE-A-RH**, no un detalle topológico. Este no-go es decisivo contra declarar “corriente de divisor” a la matriz un-nivel.

10. **No-go de energía y soporte.** E101.088 invalida una cota media basada en sumar clases no alcanzadas de cocientes de piso. E101.089–.090 dejan como objeto vivo la covarianza hermítica de cocientes balanceados; la forma holomorfa de producto ya está acotada y no la sustituye. Estos resultados son **PROBADOS/REFUTADOS** dentro de sus clases, no una imposibilidad universal de una identidad aritmética firmada.

11. **Pruebas y datos.** Las certificaciones de E94, E97, E99, E101.016, .034, .040, .043, .061 y .064 comprueban signos, escalas, identidades y falsadores a precisión finita. Ninguna fija orden de límites, compactidad cofinal, multiplicidad del divisor ni el residual acoplado. Su estado no excede **NUMÉRICO**.

## Estado utilizable

**PROBADO:** todas las identidades lineales/polinómicas finitas indicadas, la eliminación segura de inversas singulares, las descomposiciones de fuente/cáscara, los teoremas abstractos de diagonal y clausura bajo hipótesis, las colas explícitas y los no-go que conservan sus clases de aplicación.

**CONDICIONAL:** dominio de rama simple, even-simple cofinal, no anulación de carta, convergencia de fuente/prolate/cola, identificación de modelo con vector base y cualquier uso de compactidad que presuponga el objetivo espectral.

**NUMÉRICO:** todas las certificaciones multiprecisión y falsadores de secciones finitas.

**REFUTADO:** gauge del vector base físico, matching término a término, estimar cáscaras antes del emparejamiento, borrar la corrección característica, sustituir antisimetrización por un borde o producto bilateral, inversión de un nivel, restricciones tensoriales con multiplicidad lineal y cotas de soporte no alcanzado.

**EQUIVALENTE-A-RH:** `RDI-ANCHOR`, `DIRECT-BORDERED-ANCHOR`, `LOCAL-COVARIANT-IDENT`, `STIELTJES-IDENT`, `C_core→0` en intervalo seguro, `SR-LOG`, `XI-PARITY-CURRENT-NULL` y toda convergencia de divisor sensible al soporte real.

**INCOMPLETO:** una identidad Gamma–Euler fuente-canónica que compare el defecto completo con `Xi`, mantenga multiplicidad lineal y detecte el control fuera de línea; en las coordenadas actuales, `TRUE-DIVISOR-IDENT`/`DIRECTIONAL-IDENT`/`DISCRIMINANT`.

La reutilización segura debe limitarse a las identidades finitas y a los no-go con hipótesis visibles. No debe reutilizarse como lema una convergencia observada, una carta singular, una métrica adaptada a raíces, un producto de dos trazas sin auditoría de pares, ni una condición de soporte cuya prueba ya sea RH.
