# Auditoría RH4–RH6

## Dictamen ejecutivo

Los tres programas dejan una base útil de instrumentación, controles y
contraejemplos, pero no una cadena hacia RH. RH4 descarta su premisa central:
la covarianza interclase negativa y un papel singular de \(\omega=2\). RH5
identifica correctamente que las matrices de Gram de ceros son PSD por
construcción y, por ello, no pueden detectar una desviación horizontal. RH6
aporta una calibración numérica interesante del formulario localizado de
Weil, pero no resuelve —ni puede sustituir— el paso uniforme de datos finitos
a la positividad de Weil. Ese paso es precisamente equivalente a RH cuando
se formula para toda la clase de pruebas admisibles.

La lectura conjunta impone una separación estricta entre:

1. identidades y desigualdades elementales de la descomposición por
   \(\omega(n)\);
2. resultados numéricos de longitud, ventana, normalización y familia fijas;
3. equivalencias clásicas con RH; y
4. inferencias que no sobreviven controles de construcción, truncación o
   validación por familias.

## Convención de estados

| Estado | Sentido en este inventario |
|---|---|
| **PROBADO** | Derivación autocontenida o teorema clásico correctamente aplicado, sin paso numérico esencial. |
| **CONDICIONAL** | Válido al añadir una hipótesis explícita no demostrada. |
| **NUMÉRICO** | Observado en los datos, malla, precisión y controles indicados; no extrapolable por sí solo. |
| **CONJETURAL** | Propuesta sin demostración ni validación suficiente. |
| **REFUTADO** | Contradicho por la auditoría o por el control prescrito. |
| **REFORMULACIÓN-EQUIVALENTE-A-RH** | Criterio correcto cuyo cierre universal es RH bajo otra formulación. |

## Cobertura documental

Se leyeron los tres `README.md` y todos los `OVERVIEW.md` existentes. Los
cuadernos, archivos de resultados y fuentes matemáticas se usaron solamente
para comprobar puntos que cambian el dictamen: normalización DH, matrices PSD,
fórmula explícita, listas de ceros, momentos y escalas de desplazamiento.

| Programa | Directorios cubiertos | Directorios sin respuesta | Uso en la síntesis |
|---|---|---|---|
| RH4 | `task1`–`task83` | `task11`, `task19`, `task22`, `task35`, `task39`, `task46`, `task49`, `task60`, `task68`, `task70`, `task73` | Motor \(\omega\), clasificación, ablation aritmética, intentos de puente inverso y auditoría de supuestos heredados. |
| RH5 | `task1`–`task60` | `task5` | Reconstrucción por ceros, calibraciones de potencia, Jacobi/Gram/Weil, TDA y registro de cuellos de botella. |
| RH6 | `task1`–`task68` | `task7`, `task26` | Forma localizada de Weil, generación de ceros, momentos por \(\omega\), persistencia H0 y pruebas de sensibilidad. |

Los intervalos de la tabla son inclusivos: constituyen la lista completa de
directorios `task` de cada programa, incluidos los que no contienen respuesta.

## RH4 — reconstrucción

### Objetivo y método real

RH4 intentó convertir estadísticas de picos de polinomios de Dirichlet
estratificados por \(\omega(n)\) en una cadena analítica que distinguiera
funciones con y sin ceros fuera de la recta. El diseño combinó:

- una auditoría de la constante de Davenport–Heilbronn y de coeficientes;
- la descomposición \(D=\sum_k S_k\), matrices de picos
  \(M_{jk}=\mathbb E\,\Re(S_j\overline{S_k})\), razones de amplificación y
  entropías espectrales;
- clasificación con controles por familias y por ventana temporal;
- inyección de ceros en una fórmula explícita truncada; y
- ablaciones de coeficientes en primos ramificados.

El resultado metodológico importante es negativo: \(M_{jk}\) es, ante todo,
un observable de coeficientes, conductor, soporte y condicionamiento por
picos. No se comporta como una reconstrucción inversa de la parte real de un
cero.

### Ledger de claims

| Claim | Estado | Evidencia y alcance |
|---|---|---|
| \(\kappa\) DH real, aproximadamente \(0.28408\), y no \((1+i)/2\) | **NUMÉRICO** | La anulación en los cuatro ceros canónicos y la coherencia con la ecuación funcional resuelven la inconsistencia operativa. La derivación de la fase debe mantenerse separada de la verificación de sumas truncadas. |
| Validación Kahan/`mpmath` y \(\sum_kS_k=D\) | **NUMÉRICO** | Concordancia de alrededor de doce dígitos en la muestra completada; la auditoría registra que no se completaron todos los puntos previstos. Es un certificado de motor, no de una propiedad de RH. |
| La cota \(1+r\le K_N\) y \(|D|^2\le K_N^2\max_k|S_k|^2\) | **PROBADO** | Cauchy–Schwarz y conteo de clases. No depende de picos ni de ceros. |
| \(\max_{t,k}|S_k(t;N)|^2\le N^\varepsilon\Rightarrow\) Lindelöf | **CONDICIONAL** | La implicación es suficiente y es más fuerte que Lindelöf; no es una equivalencia y no implica RH. |
| Predominio de 67% de covarianzas fuera de diagonal negativas | **REFUTADO** | `task55` y la síntesis: intervalos de remuestreo incluyen 50% y excluyen el 67% en la corrida de mayor tamaño; el condicionamiento a picos desplaza el patrón hacia acoplamientos positivos. |
| \(\omega=2\) como causa única de un cambio de aproximadamente 30% | **REFUTADO** | `task47`: \(\omega=1,2,3\) tienen masas y ablaciones comparables; el máximo de Erdős–Kac explica una contribución grande, no una singularidad. |
| Modo principal positivo y de baja dimensión en matrices de picos | **NUMÉRICO** | Reaparece para \(\zeta\) y DH. Describe interferencia constructiva condicionada; no separa por sí mismo RH de no-RH. |
| Entropía espectral de matrices promediadas como separador de las clases disponibles | **NUMÉRICO** | Separación fuerte en el panel y resultado LOOCV cercano a 10/11, pero Liouville es un contraejemplo de la lectura “RH”; el tamaño de clase es pequeño y las funciones construidas no forman una muestra de la clase de Selberg. |
| Clasificador de picos como prueba de una firma universal | **REFUTADO** | Validaciones por familia, temporal y por clase muestran AUC que cae hacia azar o asimetrías F4/F12. Las cifras in-sample y bootstrap estratificado miden identidad de familia. |
| \(M_{kk}\) está escalado por \(C_k=\sum_{\omega(n)=k}|a_n|^2/n\) | **NUMÉRICO** | Relación log-log fuerte y relación lineal moderada; el condicionamiento de picos agrega amplificación dependiente de clase y estrato. |
| Los momentos cruzados no condicionados predicen \(M_{jk}\) | **REFUTADO** | El ajuste global es débil; el ajuste intraclase no autoriza una ley transversal. |
| La inyección de uno o cuatro ceros DH reproduce \(M_{jk}(DH)-M_{jk}(\zeta)\) | **REFUTADO** | `task25`; desajuste de signo y norma. El análogo F12 frente a \(\zeta\) también falla en `task26`. |
| La ablación de múltiplos de los primos de conductor reproduce diferencias DH/F12 frente a \(\zeta\) | **NUMÉRICO** | Similitudes coseno altas en los pares probados. Explica un mecanismo aritmético específico, no una ley de todos los \(L\)-funciones. |
| La localización de un cero fuera de recta puede recuperarse de normas/espectros de \(\Delta M\) | **REFUTADO** | No hay correlación estable con \(\beta\); tras retirar \(|\kappa|\), la señal desaparece. |
| El ajuste GEV heredado con bloques \(2\pi/\log N\) | **REFUTADO** | Cambiar a \(2\pi/\log T\) desplaza el parámetro fuera del intervalo heredado. |

### Dependencias, retiros y rutas cerradas

1. Los controles DH, F12 y F14 son construcciones sin producto de Euler o
   combinaciones aditivas. Sirven para refutar inferencias, pero una etiqueta
   binaria “GRH verdadera/falsa” sobre ese conjunto no identifica una
   propiedad universal de la clase de Selberg.
2. Las columnas `S_0` y, para familias módulo 5 a esta longitud, `S_7`, son
   fugas estructurales. No deben entrar en un clasificador como evidencia
   aritmética.
3. Se retiran: señal negativa interclase, excepcionalidad de \(S_2\),
   predicción por grado/conductor, SVM in-sample/LOOCV como test honesto, y
   reconstrucción inversa de ceros desde \(M_{jk}\).
4. La herencia válida es más modesta: usar la descomposición \(\omega\) como
   contabilidad de energía y como banco de controles para distinguir efectos
   de coeficiente de efectos de ceros. No volver a presentar una firma de
   picos como puente a RH sin un teorema que elimine esos confusores.

## RH5 — reconstrucción

### Objetivo y método real

RH5 desplazó el foco a listas de ceros: reconstrucción de matrices de Jacobi,
coeficientes de Li, matrices de Mercer, formas de Weil y TDA. Introdujo una
calibración saludable: deformar ceros de \(\zeta\) y medir sensibilidad antes
de interpretar un observable. También documentó fallos de generación y
precisión de listas de ceros para DH, \(L(\chi)\) y \(L(\Delta)\).

### Ledger de claims

| Claim | Estado | Evidencia y alcance |
|---|---|---|
| Una matriz de Gram formada sólo con evaluaciones de ceros en recta puede generar negatividad | **REFUTADO** | Es PSD por construcción. La positividad de una matriz así es tautológica y no prueba RH. |
| Reconstrucciones Jacobi que sólo usan ordenadas detectan desplazamientos horizontales | **REFUTADO** | La coordenada real fue descartada; la calibración de potencia muestra ceguera estructural. |
| Coeficientes de Li finitos positivos verifican RH | **REFUTADO** | La positividad para todos los índices es el criterio de Li; verificar un tramo finito no transfiere al infinito. |
| Criterio de Li / positividad de Weil universal | **REFORMULACIÓN-EQUIVALENTE-A-RH** | Son equivalencias clásicas, útiles para localizar el obstáculo, no soluciones por truncación. |
| TDA H1 y varianza numérica separan DH de los controles disponibles | **NUMÉRICO** | Separación finita de un contraejemplo sin producto de Euler; no hay implicación de RH ni invariancia entre familias. |
| Forma localizada de Weil, restando lado aritmético completo, detecta una anomalía DH cerca de su altura | **NUMÉRICO** | La calibración local y los controles son informativos como detector de una anomalía conocida. No excluyen ceros desconocidos. |
| Una lista finita de ceros y corte finito de primos permiten concluir positividad/inexistencia global | **REFUTADO** | El propio Ledger reconoce colas de ceros, corte aritmético, dependencia de base y ausencia de cota uniforme. |
| Generación de los catálogos de tamaño objetivo | **REFUTADO** | Varias tareas terminan con listas parciales, precisión efectiva menor a la requerida o procesos interrumpidos. Cualquier análisis que presuponga los catálogos completos debe marcarse como incompleto. |

### Circularidad que debe corregirse

Hay dos objetos diferentes que deben mantenerse separados.

- La forma de Weil \(B(f,f)\), definida por la fórmula explícita, tiene
  positividad universal equivalente a RH.
- La discrepancia numérica “lado de ceros menos lado aritmético truncado” es
  un residuo de truncación. Cuando ambos lados están completos, la fórmula
  explícita los iguala; esa discrepancia no es por sí una nueva forma
  positiva.

Por tanto, una afirmación de que una cota uniforme del residuo de secciones
finitas implica la positividad universal debe demostrar una desigualdad nueva
que no presuponga el criterio de Weil. Si la cota uniforme equivale ya a la
positividad de Weil, el paso es **REFORMULACIÓN-EQUIVALENTE-A-RH**, no un
lema técnico disponible. Esta distinción impide confundir una excelente
calibración de detector con un avance deductivo hacia RH.

### Herencia y no-go

Conservar: calibración mediante desplazamientos controlados, comparación de
resolución frente a \(\delta\), y la exigencia de curvas de convergencia para
objetos deterministas. No repetir: Gram PSD como detector, extrapolar signos
finitos de Li/Mercer, llamar “prueba” a TDA, ni regenerar en cada tarea listas
que deben ser un único artefacto validado.

## RH6 — reconstrucción

### Objetivo y método real

RH6 concentró el esfuerzo en una base Hermite–Gauss localizada para la fórmula
explícita, sensibilidad a desplazamientos de ceros y momentos de
\(\omega\)-clases. Es el programa con la mejor separación entre un detector
operativo y el salto de prueba, aunque sus propias tareas revelan
inconsistencias de escala y de datos que impiden elevar el resultado.

### Ledger de claims

| Claim | Estado | Evidencia y alcance |
|---|---|---|
| Una forma cero-sólo es PSD | **PROBADO** | Suma de productos exteriores. Explica el fallo de `task44` y elimina esa ruta. |
| La respuesta H0 a un corrimiento horizontal pequeño es cuadrática | **PROBADO** | Para el modelo de nube vertical, \(\sqrt{s^2+\delta^2}-s=O(\delta^2)\); las mediciones de bottleneck y Wasserstein concuerdan. |
| H0 separa DH de controles con alturas comparables | **REFUTADO** | Permutaciones no significativas y fuerte confusión por rango de alturas. |
| Fracciones de segundo momento por \(\omega\) convergen a una firma | **REFUTADO** | Migran con \(N\), como anticipa Erdős–Kac. |
| Exponentes de ajuste de momentos distinguen \(\zeta\), \(L(\Delta)\), DH en la malla disponible | **NUMÉRICO** | Ajustes descriptivos de pocos valores de \(N\); inestables al retirar un punto y dependientes de ventana. |
| Descomposición de cuarto momento ofrece huella finita de producto de Euler | **NUMÉRICO** | Los residuos cambian de signo y magnitud con ventana y longitud; es una descripción de régimen finito. |
| La forma localizada detecta una deformación prescrita de \(\zeta\) y la anomalía DH cuando se centra cerca | **NUMÉRICO** | Sensibilidad espacial y de base bien calibrada; depende de conocer altura, geometría y lado aritmético. |
| Ley cuadrática en \(\delta\) para un cuarteto simétrico desplazado | **NUMÉRICO** | `task32` da exponente cercano a dos en ese montaje. |
| Ley lineal universal en el desplazamiento real | **REFUTADO** | `task68` informa ley lineal en otro montaje; ambas no pueden ser la misma ley universal. La paridad, qué ceros se desplazan y la definición de matriz deben declararse antes de comparar. |
| Amplificación superpolinómica con dimensión de base | **NUMÉRICO** | Sensible a truncación, centro y aritmética incompleta; no es una cota uniforme en \(J\). |
| Cola de primos Hermite–Gauss controlada de modo suficiente para pasar a RH | **CONDICIONAL** | La caída gaussiana de un kernel puede acotar una cola para parámetros fijos, pero falta una cota conjunta en centro, ancho, dimensión, cola de ceros y normalización. Sin ella no hay transferencia global. |
| Positividad localizada finita implica RH | **REFUTADO** | Regla R6/R7 y los resultados lo reconocen: es una sección finita, no la forma en todas las pruebas. |
| Positividad de Weil para toda prueba admisible equivale a RH | **REFORMULACIÓN-EQUIVALENTE-A-RH** | Es el marco correcto del problema; la parte nueva debe ser una desigualdad independiente que permita alcanzar esa cuantificación. |

### Dependencias abiertas y errores operativos

- Los catálogos requeridos por la regla de caché no estaban todos presentes;
  repetidas tareas de generación DH terminaron en puntos de control parciales.
  No se deben mezclar listas de distinta completitud como si fueran el mismo
  experimento.
- La consistencia de signo y escala de \(Q\) requiere una especificación
  única de transformada, contribuciones polar/arquimediana, simetrización de
  cuartetos y error de cada truncación. La divergencia entre las leyes lineal
  y cuadrática es una alarma de especificación, no un nuevo fenómeno físico.
- Las afirmaciones sobre Keating–Snaith y sobre límites de momentos necesitan
  un régimen asintótico y cotas de error; los cuatro o menos valores de
  \(N\) no lo proporcionan.

### Herencia válida y rutas que no deben repetirse

Conservar la prueba de potencia local, los controles de base/corte, la
separación de error de datos y error de fórmula, y el no-go H0. No repetir:
usar DH como único sustituto de una alternativa general a RH, promover ajustes
de exponente a leyes asintóticas, o tratar la cancelación del residuo de
fórmula explícita como una nueva positividad.

## Dependencias transversales y mapa de decisión

| Componente | Resultado heredable | Límite no negociable |
|---|---|---|
| Descomposición \(\omega\) | Contabilidad de energía, controles de soporte y prueba de confusores aritméticos | No es criterio de RH ni predictor inverso de ceros. |
| Clasificación | Diagnóstico para construir controles y detectar fuga de variables | No sustituye una cuantificación matemática; clases construidas no son distribución de contraejemplos. |
| DH y combinaciones aditivas | Contraejemplos para invalidar inferencias que sólo usan ecuación funcional | No representan una familia de \(L\)-funciones con producto de Euler. |
| TDA | Medición geométrica auxiliar y no-go H0 | Ninguna distancia finita de nubes prueba una afirmación sobre todos los ceros. |
| Forma de Weil | Marco exacto en que RH es positividad | El paso uniforme de truncaciones a todas las pruebas es el problema, no una consecuencia de la simulación. |

## Replanteo global recomendado

1. Fijar un único objeto objetivo: la forma de Weil clásica, con dominio,
   convención de Fourier y términos completos escritos una vez. Distinguir
   explícitamente la forma de su residuo numérico truncado.
2. Formular cualquier lema nuevo como desigualdad uniforme verificable sin
   asumir positividad de Weil. Debe cuantificar simultáneamente dimensión de
   base, centro, ancho, corte de primos y cola de ceros. Si su conclusión es
   la positividad para toda prueba, clasificarlo desde el inicio como
   **REFORMULACIÓN-EQUIVALENTE-A-RH**.
3. Mantener RH4/RH6 sólo como banco de falsación: antes de atribuir un efecto
   a ceros, abatir coeficientes, conductor, soporte, ventana, selección de
   picos y normalización. La prueba mínima debe sobrevivir a controles con
   producto de Euler y a deformaciones sintéticas cuyo lado aritmético esté
   definido de forma coherente.
4. Congelar catálogos de ceros versionados, con certificado de cobertura y
   precisión. Ningún resultado posterior puede combinar puntos de control
   parciales con listas completas sin señalar el corte efectivo.
5. Tratar las huellas de momentos, entropía y TDA como resultados numéricos
   negativos o descriptivos, nunca como hitos de demostración. El único
   frente que conserva relevancia lógica es una estimación uniforme nueva para
   la forma de Weil, con auditoría adversarial previa de circularidad.

## Hallazgos críticos para no perder

- La hipótesis de interferencia negativa que motivó el frente omega está
  retirada; los picos observados son constructivos y la masa \(\omega=2\) no
  es singular.
- Las matrices de picos codifican principalmente aritmética de coeficientes;
  el éxito de ablaciones por primos ramificados y el fracaso de inyecciones de
  ceros cierran el puente inverso propuesto.
- Toda positividad de una Gram cero-sólo es tautológica. La forma de Weil y
  la discrepancia truncada deben dejar de intercambiarse en el lenguaje y en
  el código.
- La forma localizada es un detector numérico calibrado, no una exclusión de
  todos los ceros fuera de recta. Su obstáculo uniforme es el núcleo real de
  RH bajo esa formulación.
- H0, los clasificadores y los ajustes de momentos quedan como no-go o
  fenomenología finita; no deben recibir presupuesto de prueba.
