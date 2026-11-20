# POWER — Determinante polinómico correlacionado, diseño108

Estado: EJECUTADO / INCONCLUSO, reproducido independientemente. El diseño previo se conserva; signo compacto OPEN.

## 1. Antecedente y diferencia precisa

Se conserva las reglas del proyecto y la consulta de ROUTES-TRIED-INDEX/README, R162_2300_MASTER_GRID y CROSSWORD-TO-D para el objeto mixto104–107. La corrida107 y su reproducción independiente terminaron INCONCLUSIVE:11 evaluaciones,0 aceptadas, lambda[0,1/65536], profundidad10. No fue un signo negativo. No se repite como prueba el sistema impar093 ni se presume herencia de099.

El único cambio108 es algebraico: formar el determinante en el anillo de polinomios intervalares ANTES de evaluar lambda. Así las24 permutaciones mantienen la misma variable; no se asume correlación entre errores de coeficientes. Se conserva intacto el builder107 y toda su prueba de truncamiento.

## 2. Parámetros inalterados

Origen:1024bits,128 modos, cap t1025, grado lambda512; dominio[0,1/4],16 celdas iniciales de ancho1/64, profundidad10, máximo8192 evaluaciones. Resto: módulo107 INTACTO,512bits, Gauss64 en10 segmentos hasta512, cap4/cap5,508 celdas iniciales temporales de ancho1/8, profundidad10, máximo8192 evaluaciones. Ningún cambio de modos, precision, geometría o criterio de aceptación.

No se modifica power_mixed_four_origin_branch_107.py ni power_mixed_four_compact_107_verify.py. El nuevo controlador importa el builder sin ejecutar run_origin107. Antes de importar se comprueban hashes fijados al guardar el literal108. La importación107 no evalúa theta. La evaluación puntual de a y construcción de coeficientes ocurrirá sólo en la corrida108 autorizada, nunca durante este diseño.

## 3. Polinomio y errores

El builder entrega los polinomios conocidos para columnas K,J,phi,Q y sus derivadas lambda0..3. Formar mediante productos y sumas intervalares los24 términos del determinante y obtener un único polinomio P(lambda), conservando todos sus coeficientes. Su grado es finito y como máximo2048. No truncar el producto para reducir coste y no identificar coeficientes inciertos con cero.

Los errores de momentos103, a y modos theta están YA en los coeficientes intervalares del builder y se propagan por todos los productos. El error restante de función por entrada es epsilon=2^-400, según107 auditado. No se introduce esa bola como coeficiente constante de P: se paga después como error independiente del determinante.

Para lambda real[0,1/4], los discos de radio1/8 quedan en |lambda|<=3/8. J,K<=2^42 en |lambda|<=1/2; Cauchy hasta derivada4 cuesta menos que4!8^4<2^17. La combinación Q^(j)=-(2j+1)phi^(j)-2lambda phi^(j+1), j<=3, queda asimismo bajo B=2^62. Las entradas polinómicas están bajo B+1. Telescopar cada producto de cuatro entradas, sin suponer dependencia favorable de errores, da

 |det exacto-P| <=24*4*epsilon*(B+1)^3
                 =96*2^-400*(2^62+1)^3 <2^-200.

Esta cota es uniforme en todo el origen. No exige positividad previa del determinante.

## 4. Evaluación fijada antes de datos

Se elige traslado Taylor exacto del polinomio a cada centro racional c, y NO evaluación intervalar directa de sus24 términos. Si

 P(c+s)=sum b_j s^j,

se calcula el límite inferior b_0.lower - sum_(j>=1) abs(b_j).upper*h^j -2^-200, con h el semiancho exacto. Para un límite superior usar b_0.upper + la misma pérdida +2^-200. Todos los coeficientes del traslado son bolas outward, el centro y h son racionales dyádicos exactos. No se descartan coeficientes pequeños. La suma finita incorpora TODOS los grados conservados.

Se acepta una celda sólo si el límite inferior es positivo. Un límite superior negativo da NEGATIVE para toda esa celda; en otro caso subdividir izquierda primero con los mismos presupuestos107. Si se agotan, INCONCLUSIVE. Una salida del origen distinta de PASS impide ejecutar el resto. Si pasa, se usa certify_rest107 sin alterar sus parámetros. No se reinterpreta un encierro inconcluso como refutación.

## 5. Auditoría y tareas pendientes

Las cotas de entradas y de transferencia2^-200 fueron revisadas conceptualmente por mapa antes de datos. Pendiente: auditoría íntegra de este diseño, literal108 con hashes de los módulos107 y verificación de la API de traslado polinómico, auditoría literal y sólo después una corrida. El producto/traslado de grado hasta2048 puede ser costoso; el presupuesto matemático no implica garantía de viabilidad ni PASS.

No hay nueva evaluación theta, resultado de signo, cobertura W ni transferencia global en este documento. La ganancia propuesta es preservar la variable común al evaluar; los errores intervalares de coeficientes siguen siendo independientes salvo las identidades algebraicas exactas explícitas.

## 6. Ejecución fija y reproducción

Root82660 y reproducción independiente mapa28564 terminaron exit2/INCONCLUSIVE. Polinomio grado2042;15 evaluaciones,4 hojas aceptadas, cobertura lambda[0,141/8192]. Parada por profundidad10 en[141/8192,1129/65536], determinante impreso[+/−2.04e−4]. REST NO se ejecutó. No se cambiaron scripts ni presupuestos.

Hash driver108:`eb200a9061a3761d2b1a5dc5ca38def6c5c16e1e0901524c39969555eb791f6a`. Módulos107 verificadosintactos: origen15d6f12c197ef52c062a12c59ee4a7c5db94c74e0073e8463a7ce03dd613e553; REST2a7d147caf8181adb5aa29eb6fcbe356f625e2743ad6765e6ac543aacad23054. Logs:`tools/power_mixed_four_polynomial_108_root.log` y`tools/power_mixed_four_polynomial_108_audit.log`.

La reproducción añadió exclusivamente un perfil de los valores YA calculados al retornar evaluate, sin nuevas evaluaciones theta, centros, coeficientes ni parámetros. En la celda final, coefficient0 trasladado ya tiene bola[+/−1.79e−4]; radio adicional por variación de celda aproximadamente2.4560159427e−5. Esto distingue incertidumbre del coeficiente central de la variación añadida, sin identificar una única causa del ancho ni afirmar que exista un cero real. Las lecturas decimales describen el log; no son un certificado de signo.

Resultado INCONCLUSO: no signo contrario, falsificador, obstrucción matemática, Chebyshev4 global, Ufinito ni nueva cobertura W/T/allorders. Una representación posterior requerirá diseño y auditoría antes de otra corrida; no se reajusta ésta para forzar PASS.
