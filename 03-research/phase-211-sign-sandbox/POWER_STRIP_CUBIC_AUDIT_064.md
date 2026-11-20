# POWER_STRIP_CUBIC_AUDIT_064

Estado: **APROBADO** POWER_STRIP_CUBIC_NECESSITY_064, tras relectura de las reglas del proyecto y lectura completa de la fuente. Prueba analítica; no requiere tests numéricos. Sólo limita la clase STRIP uniforme declarada. Papers intactos.

Antecedentes cotejados: índice/grid/crucigrama, JOINT_SCALE016, STRIP_NECESSITY059 y UNIFORM_STRIP060. La diferencia efectiva frente059 es utilizar un numerador de mayor grado adaptado al peso Student exacto, en vez del numerador constante. No se deduce una concentración global de un pico de Christoffel ni se importa una aproximación gaussiana compleja no justificada.

## Recurrencia y grados

La construcción usa sólo grados hasta n+4 y momentos hasta n+5; todos existen ya bajo n>=4 y j>=10^6n. Los bordes Pearson se anulan. El coeficiente subprincipal y beta_k de060 siguen siendo correctos en ese rango ampliado. Para k<=n+4<=2n se tiene2M−k>=2j y los dos factores del denominador son positivos y al menosj. Sus majorantes por2M y M<=2j dan exactamente k/8<=beta_k<=4k.

Multiplicar cinco veces desde grado d=n−1 requiere MULT en grados de entrada hasta n+3 y beta hasta n+4, que son precisamente los cubiertos. La fuente no utiliza una recurrencia fuera de su rango de momentos.

## Proyección y constantes

Para R=e_d normalizado, y²R′+yR tiene grado<=d+1 y es ortogonal a e_(d+3). La componente superior de y³e_d sólo puede proceder de tres ascensos, por lo que su coeficiente es sqrt(beta_(d+1)beta_(d+2)beta_(d+3)). El lower supera n^(3/2)/24. El factor M/j>=1 conserva esta cota para el término principal.

La descomposición racional SPLIT es exacta. Su resto tiene norma<=2·4^5(n+4)^(5/2)/j<=12288n^(5/2)/j. Las hipótesis implican j>=589824n y permiten pagar este resto por n^(3/2)/48. Triángulo inverso en una ÚNICA proyección unitaria prueba ||AR||>=n^(3/2)/48. No se supone que el generador preserve el espacio original ni se ignoran términos capaces de cancelarse dentro de él.

## Numerador real y desplazamiento

La paridad d de R asegura que p(z)=(z/a)^dR(a/z) tiene únicamente potencias pares no negativas y coeficientes reales. Es no nulo y de grado<n; P(s)=p(−is) sigue siendo real. El cambio inverso recupera exactamente R y las normas de060, sin un factor2 extra. De allí ||H′||²/||H||²>=n³/(2304u²j).

Como p es real par, P(iz)=P(−iz)=p(z), H es real sobre la recta y la densidad analítica ORIGINAL es exactamente H². Esta propiedad especial justifica convertir su módulo desplazado en la norma² de H desplazada; no se hace esa identificación para un numerador complejo genérico.

En toda subfranja cerrada de|Imz|<u, H y sus derivadas tienen decaimiento suficiente para diferenciar e integrar por partes. N″(t)=4||H′(·+it)||² es correcto. Tanto N como D(t)=||H′(·+it)||² son pares, porque H y H′ son reales en la recta. D es convexa por D″=4||H″||²>=0, así que D(t)>=D(0). Integrar dos veces produce N(eta)>=N(0)+2eta²||H′||². Con la densidad H² se obtiene el factor1152 y exactamente LOWER de la fuente para cada altura fija0<eta<u.

## Clase refutada y alcance

Para cualquier p<3 y C>0, la sucesión entera j_n=max(ceil(Cn^p),ceil(10^6n)) satisface las hipótesis de construcción, pertenece al cono propuesto y es o(n³). El lower de STRIP diverge, descartando una constante finita uniforme en n,j y TODOS los numeradores a esa altura fija.

## Mejora del umbral de construcción

Root observó después de la primera aprobación que el umbral10^6n² era innecesario. Revisada la MISMA prueba paso a paso: sólo se usa j>=n para M<=2j, j>=9 para2j−9>=j, j>11/2 para los momentos hasta n+5, y j>=589824n para el restoREM. La identidad de normasGEN exige a lo sumo j>=n+8; también queda cubierta. Ningún paso de desplazamiento utiliza COARSE054 ni un contorno escalar que pida j>=10000n²: su integrabilidad se verifica directamente por el decaimiento analítico. Por tanto LOWER es válida ya para TODO j>=10^6n, sin cambiar constantes, objeto o lower. La aprobación de esta auditoría incluye esa versión mejorada.

No se afirma que esos tests tengan W negativa, que fallen sus autocorrelaciones aritméticas completas, ni que p>=3 sea necesario para un cono de SIGNO W. Tampoco se demuestra optimalidad logarítmica de060. El resultado sólo excluye la estimación ABSOLUTA de contorno uniforme descrita. Los métodos que conserven cancelación firmada y el problema del interior siguen abiertos.
