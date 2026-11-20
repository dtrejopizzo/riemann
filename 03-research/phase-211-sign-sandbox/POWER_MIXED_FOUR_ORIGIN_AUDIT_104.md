# Auditoría104 — gate puntual mixto y orientación exterior

Estado: **PROVED / auditoría aprobada. Constructor y reproducción independiente root exit0/PASS.** Fuente: `POWER_MIXED_FOUR_ORIGIN_DESIGN_104.md`. Se mantiene las reglas del proyecto y la consulta de antecedentes087/093/095/099/102/103 y tres índices. Papers intactos.

La familia es[K_even,J,Phi,J''], distinta del menor desplazado093. La matriz H incluye correctamente los factores de derivadas en lambda=t²: en particular tercera y cuarta filas de K son(az1+1/2)/6 y(az2+z1/4)/5. El cambio de Wronskiano es(2t)^6=64t^6, sin factor t común propio de funciones impares. El signo de Dmix será sólo el origen de W4, no su control global.

La recuperación autorizada087 debe conservar su hash, parámetros y cola completa. Los cuatro momentos103 se usarán como intervalos racionales outward, no como centros flotantes. La evaluación acepta ambos signos, sin campaña ni ajuste.

## Exterior analítico

Revisada la reutilización del strip holomorfo095 con todos los modos. Dos IBP horizontales dan T1=1/p²−integral R[2p'/p³+rp'/p²], con bordes exponencialmente dominados. Rep>=Y y|p'|<=5Y pagan|T1−1/p²|<=15/Y³. La representación directa de J paga|J/Phi|<=|z|/Y+1/Y²; al integrar rJ, el error de K es menor que(16+|z|)/Y³. No se deriva un O real.

Cauchy en radio1/32 controla hasta orden3 de los errores de columnas. El modelo[a/P²,t/P,1,tP] tiene W=128a(6t²+4t−1)/P². Verificados los máximos de entradas y la suma de los siete errores multilineales:61440H+6144H²+192H³. Con Cstar<2^98,y(64)>2^128 y crecimiento de y/t, el margen Wmixed/Phi⁴>6t²/y² vale TODOt>=64. Es prueba analítica, sin muestras theta.

Un Dmix negativo, junto a la cola positiva, descartaría sólo Chebyshev4 global de ESTA familia por orientaciones opuestas de determinantes cercanos a confluencia. Dmix positivo sólo verificaría una vecindad de origen sin radio. Ningún caso decide el cruce del forzante particular U ni su primitiva, kernel, W o todos los órdenes. Los tres primeros prefijos globales103 permanecen probados.

## Literal previo a ejecución

Leído completo `tools/power_mixed_four_origin_104_verify.py`. Comprueba el hash087 ANTES de runpy; extrae Phi0 y los coeficientes normalizados z1,z2,z3 de a[1:4], según el literal087. Los cuatro momentos103 y radios son Fraction exactos antes de su conversión outward a I70. Conserva las comprobaciones de denominadores y1/25<a<1, matriz de derivadas lambda y24 permutaciones con signo correcto. El assert admite cualquiera de ambos signos y no ajusta parámetros. Imprime extremos racionales recuperados para su persistencia posterior. Constructor autorizado a la recuperación y el único gate; el auditor no ejecutó todavía ningún dato ni anticipó su signo.

## Resultado y reproducción

El gate fijo terminó **POSITIVE**, tanto en constructor como en reproducción independiente root. Hash104 idéntico:`063ce9ba28dc9b0e3cca245018a968794b5b28c7a57df5da7a5c70d008b95105`. Extremos exactos copiados de `tools/power_mixed_four_origin_104_verify.log`:

- inferior: `20910875038731301173957476100644455719909401587771537215845430471153/5000000000000000000000000000000000000000000000000000000000000000000000`;
- superior: `41821750077462602464978622735022256356361140514400545338810504099651/10000000000000000000000000000000000000000000000000000000000000000000000`.

El mismo log conserva la recuperación087 completa y los extremos racionales Phi0,z1,z2,z3. No se repitió cuadratura103 ni se ajustó el diseño. Dmix>0 y ORIGIN prueban W4 mixto positivo en una vecindad existente del origen, SIN radio explícito. Junto con la prueba analítica exterior se tiene positividad para TODOt>=64. El compacto intermedio sigue OPEN; no hay falsificador, Chebyshev4 global, cruce de U finito, positividad Xi finita ni nueva cobertura W/T/allorders. No se autoriza otro test por esta conclusión.

## Auditoría de ampliación analítica: conservar potencias del resto reduce la cola a t>=16

**PROVED / revisión independiente root y mapa, sin datos theta nuevos.** En los siete términos multilineales de§5 no es necesario descartar todas las potencias adicionales de y. Conservándolas se obtiene

`error <=61440 Hstar t³/y³+6144 Hstar² t³/y⁴+192 Hstar³ t³/y⁵`.

Los tres términos simples tienen y^-3; los tres dobles tienen y^-4 y el triple y^-5. Se mantienen los mismos mayorantes de entradas y1+t<=2t. Para y>=Hstar, el error es menor que2^17 Hstar t³/y³, pues61440+6144+192=67776<2^17.

Con Hstar=39321600, Taylor positivo hasta grado5 prueba exp2>7; el cálculo entero exacto da

`3*7^16=99698791708803 >16*2^17*Hstar=82463372083200`.

Por tanto y(16)=pi exp32>3*7^16 y, como y/t crece para t>1/2, para TODOt>=16 se tiene y>=Hstar yerror<t²/y². El modelo anterior es mayor que7t²/y², de modo que

`Wmixed(t)/Phi(t)^4>6t²/y²>0 para TODOt>=16`.

Es una mejora del resto104, no una nueva evaluación de theta ni cambio de parámetros de110. La corrida110 se conserva intacta. No se infiere signo del compacto ni cobertura global sin sus pruebas y reproducción correspondientes.
