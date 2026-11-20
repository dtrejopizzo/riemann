# POWER_FOUR_GENERATORS_AUDIT_085 — Auditoría independiente

Estado: **APROBADO / PROVED**, certificado constructor61911 exit0/FULL PASS para NR y NS en TODOS los16384paneles. Reproducción independiente root29132 exit0/FULL PASS de ambos numeradores en los16384paneles, con hash coincidente. No se duplicó innecesariamente el cálculo. Fuente `POWER_FOUR_GENERATORS_085.md` leída íntegramente; código literal auditado ANTES de la corrida. Papers intactos.

SHA256 comprobado localmente del script:

    4916689a48baf3164b8e99ff8ff7973dbd505367cf9ee46b17b7efc9845abf46

## Objeto y antecedentes

Consultados las reglas del proyecto, tres registros y080/083/084. Se certifican DOS obligaciones escalares completas de084 en un compacto fijo; no se buscan nodos ni autovalores.084 ya transporta estas condiciones locales a TODOS los conjuntos de cuatro nodos por Rolle y aporta el exterior;083 conserva exactamente el determinante de la forma completa y080 sus menores inferiores. La diferencia frente a sólo probar tres es la nueva desigualdad de Turán, no una extrapolación de concavidad.

## Función y truncación

Z se evalúa, salvo constante positiva irrelevante para M, por A[1+(A−1)zeta_deflate(A)]Gamma(A/2)pi^(−A/2), A=u+1/2. La API oficial deflate significa zeta−1/(A−1); el poloA1 queda regular. AutotestsA1/A2 complementan esa identidad, no la prueban por muestras. E0>0 habilita el log real. Jets sólo en centros EXACTOS, con errores arb outward512bits y cap45. LogZ44 deja M'''40, ambos numeradores.prec>=41 y finitud0..40 verificados; no se usa un coeficiente truncado como si fuera exacto.

Los polinomios NR/NS coinciden literalmente con REAL-TURAN084, cuyas fórmulas fueron derivadas independientemente. D=ud,E=u²e,F=u³f no cambian signos ni escala. Los coeficientes de serie son normalizados por k!, sin factorial adicional en PANEL.

## Resto uniforme revisado independientemente

En cada disco |z−c|<=r=1/32, el ancla realA130 y la monotonía073 dan M<2 hasta c+r+1. La razón Zextra/Zc<exp(33/16)<8 queda pagada por log2>56/81 y3·56/81>33/16. Positividad/paridadtheta dan |Zk|<16k!Zc y |Z−Zc|<Zc/2; así Z no se anula en TODO el disco y los cocientes están acotados por32k!.

Los bounds M<32,M'<1100,M''<72000,M'''<8e6 son correctos en módulo; el último coste exacto es7115520. Con |z|<128, la suma absoluta común NR/NS cuesta8901242950707612672<10^20. Cauchy paga TODA la cola desde grado41 por T=10^20(127/1024)^41/(1−127/1024)<10^−16 (aproximadamente7.7833e−18, sólo indicativo). Las constantes y fracciones fueron verificadas independientemente con Fraction exacta.

## Cobertura y ejecución

Los16384paneles con h=127/32768 y centros[16384+(2j+1)127]/32768 cubren exactamente[1/2,255/2]. Se verifica para ambas funciones N0−sum(k1..40)|Nk|h^k−T>0. El signo se prueba en TODO el panel, incluidos extremos; no por muestras centrales. Todas las constantes,512bits,cap45,grado40,dominio y malla quedaron fijados y auditados antes de ejecutar. Constructor61911 terminó exit0/FULL PASS y hash coincidente; no se modificó script durante la corrida.

## Consecuencia exacta

El compacto más OUTER-TURAN084 prueba TR,TS>0 para todo u>=1/2. Los signos R',S'>0,R'',S''<0 ya son073/080. Rolle084 hace positivos ambos Pfaffianos para TODOS los cuatro nodos distintos en ese intervalo;083 da determinanteK4>0 y los menores inferiores080 prueban PD. Por congruenciaCONE001 se obtiene W completa positiva en cualquier combinación no nula de hasta CUATRO potencias arbitrarias ai>1, incluyendo ARCH, polar y TODOS los contactos. Repetidos se agrupan y la matriz redundante es PSD.

Esto amplía exponentes pequeños/mixtos, más allá de la región de tasas grandes053. No se prueban cinco generadores, todos los órdenes, envolvente completa ni una nueva ventanaT. Signo global y obligaciones pfaffianas superiores siguen OPEN.
