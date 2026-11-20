# Auditoría106 — integral normalizada holomorfa

Estado: **LEMA ANALÍTICO APROBADO, sin ejecución ni signo global.** Fuente: `POWER_MIXED_NORMALIZED_INTEGRAL_106.md`. Se conservan las consultas y antecedentes103–105; el avance es un control de evaluación normalizada y sus errores, distinto del test104 o de una identidad usada como signo. Papers intactos.

## Dominio e identidades

Verificados Y>21/8, Rey>5/2 y la suma completa Rtheta<1/4 por ratios yexp(5/2)>8. No se trasladó indebidamente un lower real a complejo. Las cotas acopladas Theta(y+v)/[(y+v)Theta(y)] pagan el jacobiano exactamente, sin usar la desigualdad falsa|y+v|>=Y+v. La rama principal de Log(1+v/y) es holomorfa en el strip. NORMALIZED se prueba primero en reales; la dominación uniforme en compactos y ausencia de ceros justifican continuación analítica. La fórmula de K conserva su kernel a r−(z+r)r²/2, obtenido por Fubini.

## Colas y coeficientes

Recalculados los momentos5,11,38,174, las cotas COLUMN y los integrandos escalados2048e^-v(1+v)^5. La integral desde512 es menor que2^62e^-512<2^-450. La cola theta m>=17 se paga en numerador Y denominador; el error relativo<2^-698 y el coste de integral<2^20 implican errorfunción<2^-675. Cauchy en radio1/32 paga los errores de coeficientes32^j. Son cotas completas, no derivadas formales de un O real.

El complemento propuesto para la columna X es válido: log(1−delta) tiene módulo<2^-697; su derivada por Cauchy cuesta32, de modo que|p−p16|<2^-692 y|(X−X16)/Yc|<2^-687 en el dominio indicado. También queda por debajo de2^-675. La cota W de la fuente utiliza p EXACTO y no dependía de omitir ese error de aproximación.

## Wronskiano y origen

El pbound<10Y sigue del primer modo explícito y Cauchy del log de la corrección. Escalas de columnas constantes en cada centro preservan Yc²Wmixed/Phi⁴. Bounds de columnas y derivadas hasta3 dan24productos<2^108<2^120. Los cocientes son pares holomorfos cerca0: el factor(2t)^6 del cambio lambda=t² prueba divisibilidad por t6. Para|z|>=1/256 la división paga2^48; cerca0, círculo|z|=1/128 y principio del máximo, con Yc²/pi²<2, pagan de nuevo2^168. No se presupone un lower positivo del Wronskiano.

El futuro certificado aún debe fijar cuadratura finita, tolerancias, jets, precisión, partición y resto antes de datos. Si usa callback analítico, deben verificarse ramas y denominadores en las bolas, o devolver no finito. Este lema no autoriza ejecutar un diseño no auditado. Compacto intermedio, Chebyshev4 mixto, cruce de U finito y signo global W permanecen OPEN. No se ejecutó nuevo cálculo.

Root completó lectura independiente y aprobó106. Precisión del bound de primera columna: usar1000*66*(16/15)²<2^17; el factor preciso ya declarado, no el redondeo2, paga el margen. La fuente ahora lo explicita.

## Ampliación106§8 — Gauss vectorial fijo

Lectura literal completa APROBADA. Diez discos v de radio2h: primero Rev>=−1/2, restantesRev>=h. MinRe(v/y)=(bcosargy−2h)/Y pruebaRe(1+sv/y)>4/5 y|r|<|v|/Y. La cota Theta16 utilizaRe(y+v)>2, con suma m4 menor que2; el cociente acoplado paga22/Y. En discos temporales alrededor de TODOS los puntos de un parámetro de semiancho<=1/64, la unión cabe en|z−c|<=3/64, dentro del strip. Allí los factoresYc/Y ysu cuadrado siguen menores que2, por lo que el mismo mayorante4096e^(−Rev)(1+|v|)^5 es uniforme.

Recalculados Mfirst<2^20 yMrest<=4096·7^5·120<2^34. Cauchy temporal daM_j=2^34·32^j. ExactitudGauss64hasta127 ypesospositivos consuma2h pagan integral ycuadratura de la colaTaylor por4h M_j2^-128/(1−1/2). Suma semianchos256 da2^(−83+5j),<=2^-68 paraj<=3. La prueba separa erroranalítico de bolas de nodos/pesos ytodo error aritmético. El diseño107debe añadirlosjuntoacolasmodos/v ANTESdeterminante yfactoriales de derivadas. No se ejecutó la cuadratura ni se aprobó aún un diseño final de signo.
