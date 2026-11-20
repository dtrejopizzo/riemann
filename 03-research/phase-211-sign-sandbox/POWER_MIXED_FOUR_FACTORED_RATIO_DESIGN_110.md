# POWER — Cociente theta factorizado, diseño110

## Actualización verificada: reproducción terminada y WM activada

Los logs constructor y reproducción independiente de110 son idénticos byte por byte, SHA256 `90a2ec137e806c8a7f8cce975f7af1cee375d9e48bdaf1c5bc302f7c06428539`. Driver: `c629d4ed4b5eeb625a69ee92f6000892b9493c50e825e9ade73bf3a5a9362108`; los cuatro módulos importados conservan los hashes auditados. Root comprobó por fracciones exactas el origen completo (16 hojas en lambda[0,1/4]) y 4198 hojas REST contiguas desde1/2 hasta845/32 en AMBOS logs. Ambos programas terminaron INCONCLUSIVE por8192 evaluaciones; no se cambia esa etiqueta ni se afirma FULLPASS hasta64.

La cola analítica104, auditada por root/casos/mapa, prueba Wmixed/Phi^4>6t^2/y^2 para todo t>=16. Por tanto la cobertura reproducida y esa cola se solapan y prueban WM para TODO t>0. Los tres prefijos103 completan MIXED4. Queda activada la aplicación real de las implicaciones auditadas112: segunda densidad Xi positiva para todos p,q>0, E/Psi decreciente, TP2 y confluencia estrictas. Root revisó también el literal§8 y las dos fuerzas verificadas independientemente por casos: se activan las comparaciones de la pareja límite estrella. No se afirma Xi_(p,q)/E_(p,q) decreciente para parámetros finitos, cinco potencias arbitrarias, todos los órdenes ni una ventana nueva.

Las menciones posteriores a réplica pendiente o aplicación condicional describen el estado anterior a esta actualización y quedan superadas exclusivamente por esta evidencia. El signo global permanece OPEN. Véase `POWER_REASSESSMENT.md` para el cambio de estrategia.


Estado: DISEÑO Y LITERAL AUDITADOS; constructor root52878 terminó exit2/INCONCLUSO; reproducción mapa12244 en curso, sin cierre independiente todavía.109 terminó exit2 sinFULLPASS, por lo que la condición previa se cumple. No se garantiza PASS.

## 1. Diferencia precisa

Se mantiene la consulta las reglas del proyecto y los tres índices del objeto mixto104–109. La rama restante107 evalúa el cociente Theta16(y+v)/Theta16(y) con numerador y denominador separados.110 usa una identidad exacta para conservar la dependencia del primer modo común. No cambia la función integrada, las hipótesis, el objetivo ni el presupuesto; no es una nueva prueba de signo ni una modificación de109 durante su corrida.

## 2. Identidad exacta y factores

Definir d=2y-3 y, para m=2..16, a_m=m^2-1,

 B_m(y)=m^4+3m^2 a_m/d,
 R16(y)=sum B_m(y)exp(-a_m y).

Entonces Theta16(y)=d(1+R16(y)). El factor m^4 es esencial: (2m^2 y-3)/(2y-3)=m^2+3(m^2-1)/(2y-3), y existe además el factor exterior m^2. Por ello

 Theta16(y+v)/Theta16(y)
 =(1+2v/d)*(1+R16(y+v))/(1+R16(y)).

Se usa esta identidad DENTRO del mismo integrando A16 de106/107. No se supone que los errores de las dos correcciones estén correlacionados: sus bolas se propagan normalmente. La conservación es algebraica en el factor principal explícito1+2v/d.

La derivada temporal total, con y'=2y, es

 R_t(y)=-sum exp(-a_m y)[2y a_m B_m(y)+12y m^2 a_m/d^2].

Así la misma columna local p16 puede evaluarse como

 p16=2y-9/2-6/d-R_t/(1+R16).

No confundir R_t con R_y. Los jets de p16 se obtienen con la misma precisión/cap y coeficientes conocidos de107. La fórmula no diferencia un equivalente asintótico ni descarta modos.

## 3. Presupuesto, dominio y errores conservados

El origen Cauchyclip109 queda INTACTO. En el resto se conservan precision512,cap4 de integrales/cap5 local,16 modos, Gauss64 en los mismos10 segmentos v hasta512, partición inicial508 celdas temporales de ancho1/8, profundidad10 y máximo8192 evaluaciones. Se conserva orden de recorrido y criterio de signo/inconcluso. Los nodos y pesos encerrados, ramas log/potencia y comprobaciones de denominadores se mantienen.

Los errores analíticos106 se aplican sin cambio porque las funciones son idénticas: Gauss2^(-83+5j), pago total de columnas2^-81*32^j y error X/Yc2^-687*32^j para j0..3, además del redondeo intervalar. No se acortan colas ni se eligen parámetros según la salida109. La factorización no extiende el dominio de holomorfía: d y1+R16 son no nulos en los dominios ya probados106. Se pueden reutilizar exp(-a_m y) y exp(-a_m v) para la corrección desplazada.

## 4. Condición de ejecución y alcance

Esperar la salida final109 sin intervenir en su proceso. Si es FULLPASS,110 no se ejecuta. Si no lo es, la nueva representación requiere primero auditoría del presente diseño y literal; sólo después podrá autorizarse una corrida. Un fallo de encierro posterior sigue siendo INCONCLUSIVE, no negativo matemático. Este diseño no añade cobertura W ni afirma que la factorización baste para terminar dentro del presupuesto.

## 5. Estado posterior a revisión, sin anticipar resultado

109terminóexit2porpresupuestoREST, noFULLPASS. Rootymapaaprobaronindependientementediseñoyliteral110antesdatos;rootautorizólaprimeracorridacoordinada. El auditornoejecutóreplicanianticipaPASS. Códigos107/108/109/110sinmodificacionesdurantelacorrida. Elresultadofinalyhashdeldriverseconsignaránsólotraslasalida real.

## 6. Resultado terminal del constructor y reproducción en curso

Root52878 terminó exit2/INCONCLUSIVE por presupuesto8192evaluacionesREST,4198hojasaceptadas. OrigenPASS16/16. AuditoríalogexactaFraction: las4198hojassoncontiguasREST[1/2,845/32],longitud829/32. La siguientecelda pendiente[845/32,3381/128],depth4,noquedóaceptada antesdelcap. NOFULLPASSdelprogramaconobjetivohasta64. Log:`tools/power_mixed_four_factored_110_root.log`,driverhashc629d4ed4b5eeb625a69ee92f6000892b9493c50e825e9ade73bf3a5a9362108.

La reproducciónindependiente mapa12244 sigue conelMISMOprograma,objetivo64ypresupuesto8192,sinparadaen16niotroajuste. El constructor cubre16,y104pruebacola16,pero la aplicaciónWMglobal112sigueCONDICIONALhasta confirmar lacoberturaindependiente16. No seconfunde ese posibleensamblaje conFULLPASSdelprograma,ni se anticipaelresultadofinaldelaréplica.
