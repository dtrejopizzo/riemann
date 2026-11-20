# Un producto regular y sin ceros a través de la recta que cambia el baricentro

En 251 la retirada de primos hacía divergir la derivada logarítmica del factor modificador en 1/2. Ahora se permiten multiplicidades 0, 1 o 2 en primos verdaderos. Existe una elección fija, idéntica a los primos hasta cualquier prefijo inicial prescrito, para la cual la función zeta del producto modificado tiene exactamente los mismos ceros y polos, CON MULTIPLICIDADES, en Re s>1/3. La razón respecto a ζ es holomorfa y nunca nula allí. Aun así el baricentro modificado oscila de signo arbitrariamente lejos, sin asumir RH. Para los primos modificados contando multiplicidades vale

    C_mod(x)−C(x)=−√x cos(x^(1/24))+o(√x).

**Realización en primos enteros.** Fijar U=m₀³ grande y w(u)=u^(−5/12)cos(u^(1/24))/1152 para u≥U, cero antes. En cada [m³,(m+1)³), de extremo izquierdo b, tomar I=∫w y escoger floor(|I|/log b) primos distintos; duplicarlos si I>0, retirarlos si I<0. Hay suficientes por el PNT de intervalos de 238, ya que la longitud es comparable a b^(2/3). El número seleccionado es O(b^(1/4)/log b); se pueden escoger en índices equiespaciados como en 251. Cada logaritmo difiere de log b en O(b^(−1/3)), luego el error de redondeo en la masa firmada de toda la celda es O(log b). En una celda incompleta el error es O(b^(1/4)) por magnitudes absolutas. Escribir e_p para el cambio de multiplicidad. Resulta

    Σ_(p≤x)e_p log p = ∫_U^x w(u)du + O(x^(1/3)log x)    (x≥U),
    Σ_(p≤x)|e_p|log p ≪ x^(7/12).

La segunda cota sale sumando O(m^(3/4)) por celda. Los primos editados tienen separación en índices tendiente a infinito, tomando, por ejemplo, los puntos medios de sublistas equilibradas para evitar contacto entre celdas. Se conserva así también la proporción asintótica de conteos en todo intervalo móvil con cantidad de primos tendiente a infinito.

**Continuación del factor.** En Re s>1 su derivada logarítmica negativa es Σ e_p(log p)/(p^s−1). Los exponentes ≥2 convergen localmente en absoluto para Re s>7/24 por la cota absoluta anterior. En el primer exponente, la transformada de la discrepancia entre los átomos y w(u)du es holomorfa para Re s>1/3 por sumación parcial. La transformada del propio w se prolonga a función entera: con v=u^(1/24) se integra desde U^(1/24)>0 un múltiplo de v^(13−24s)cos v, inicialmente en convergencia absoluta. Integraciones por partes repetidas prolongan el resultado a cada compacto, con términos de borde inferior enteros. Así la derivada logarítmica modificadora es holomorfa en todo Re s>1/3. Tomar su primitiva con el signo apropiado y exponenciar desde s=2 prolonga el factor mismo sin ceros ni polos, y prueba la igualdad de divisores en ese dominio.

**Lectura del baricentro.** Por variación acotada de k de 247, la discrepancia discreta cuesta O(x^(1/3)log x). Con L=x^(1/24), la contribución continua es la integral contra cos v del polinomio

    g(v)=(24/1152)v^13 k((v/L)^24),   U^(1/24)≤v≤L.

En el extremo móvil g(L)=0 y g'(L)=−L^12. Dos integraciones por partes aportan g'(L)cos L; una tercera acota el resto por O_U(1+L^11) usando |g''(L)| y ∫|g'''|. Esto da la oscilación anunciada. Bajo RH, |C(x)|≤(4/15+0.094+o(1))√x por 247, de modo que las fases cos L=±1 dan signos opuestos. Si falla RH, las excursiones de 249 de orden estrictamente superior a √x sobreviven a la modificación.

**Qué discrimina la prueba.** La regularidad de la derivada logarítmica en la frontera, incluso simultáneamente en todas las alturas, no distingue ahora los dos sistemas por sus singularidades. La fórmula explícita de 247 usa además estimaciones en contornos que permiten representar el observable por los residuos y un resto pequeño. Aquí el factor holomorfo aporta por sí solo una oscilación de orden √x a esa misma lectura. No se atribuye al sistema modificado la ecuación funcional ni las estimaciones verticales de ζ. R163_102 ya trata la estabilidad de ceros por ediciones; 251 ya exhibe inversión por borrado. El paso adicional es realizar el término oscilante mediante átomos en primos conservando el divisor a través de toda la línea crítica.
