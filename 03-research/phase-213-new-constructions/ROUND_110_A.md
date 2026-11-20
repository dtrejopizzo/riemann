# Sólo los centros con balance local de masas necesitan una cota recíproca

Usar r=exp(11/25), w,V y E de 109. Para un primo q llamar L,R a las sumas de log p en (q/r,q) y (q,rq), respectivamente, y l,s a las sumas de (log p)/p en los mismos intervalos. Sea d=log q. El signo global equivale a esta implicación para todo q primo suficientemente grande:

    Si −d ≤ R−rL ≤ rd, entonces r(s+d/q)−l ≤ 2√r V(1).

El filtro sólo usa masas de Chebyshev en los dos intervalos, con tolerancia de orden log q frente a masas de orden q. El techo usa sólo sus momentos recíprocos. No se afirma una densidad de centros que pasen el filtro.

**Cálculo.** Poner G(x)=E(x)/x. En cada tramo E(x)=Ax+B se tiene G'(x)=−B/x². En q los interceptos antes y después son, por las ramas de 109,

    B_−=(rL−R−d)/(2√r),     B_+=(rL−R+rd)/(2√r).

Los extremos q/r,rq no son primos pues r es trascendente. Un máximo local exige B_−≤0≤B_+, precisamente el filtro. La pendiente de E antes de q es A_−=[r(s+d/q)−l]/(2√r)−V(1). En un centro filtrado se tiene

    A_−−(r+1)d/(2√r q) ≤ G(q)=A_−+B_−/q ≤ A_−.

Bajo RH, 109 da G(q)≤−c/√q eventualmente, por lo que A_−≤0 en todos los centros filtrados.

**Vuelta.** Si falla RH, los polos de V P de 109 y Landau aplicado a uno u otro signo excluyen ambas posibilidades E≥0 eventualmente o E≤0 eventualmente. Luego existen, arbitrariamente tarde, tres puntos con signos −,+,− en ese orden. G tiene los mismos signos. En el intervalo cerrado entre los puntos negativos elegir el extremo derecho del conjunto de máximos de G; el valor es positivo. Las ramas son finitas en ese compacto y monótonas o constantes para G. Al salir de la meseta máxima el signo de la derivada pasa de no negativo a negativo (incluida una meseta de longitud cero). Esto sólo es posible en un salto descendente de pendiente de E, pues el salto de G' es el de E' dividido por x. Por 109 ese punto es un primo. Allí vale el filtro y A_−≥G(q)>0, contradicción.

**Relación con los antecedentes.** En 094 el cruce depende de la masa desde el origen; en 109 se comprueban todos los centros primos. Aquí el centro y ambas comparaciones sólo requieren vecinos dentro de la misma banda fija. Falta controlar la correlación entre el balance de masa y el de recíprocos en los centros seleccionados.
