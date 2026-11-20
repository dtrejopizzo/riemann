# POWER_PRIME_AUDIT_014 — Revisión del filtro acoplado con aritmética

Estado: PROVED identidades y falsificador universal de E2; OPEN sus desigualdades restringidas y completas. Revisa POWER_PRIME_TRANSFER_014.md. Papers intactos.

La identidad |H(i tau)|²-R0=(1-R0)tau²/(v²+tau²) es exacta. La inversa del complemento es delta-Pv con Pv=(v/2)e^(-v|t|), de masa1; por ello la diferencia temporal de autocorrelaciones, su fórmula de segunda diferencia y el signo firmado del núcleo son correctos. Se mantiene el factor1-R0 en todos los pasos.

El cambio polar es r0-R0=-(1-R0)/[4(v²-1/4)]. Esto produce exactamente T2, sin normalizar por una norma nueva de forma incorrecta. Para la suma completa de contactos se justifica trabajar en tiempo: cada correlación racional y su diferencia es exponencial por polinomio, y la suma ponderada por Lambda converge absolutamente. No se supone un símbolo puntual infinito de cosenos convergente.

El falsificador universal de E2 se revisó independientemente. La medida de su derivada tiene numerador tau²(tau²+1/4)^2 y denominador(u²+tau²)^(n+1). Acotar el normalizador por M2/16 deja

    E tau²<=16M8/M2+8M6/M2+M4/M2
       <1680/128³+120/128²+3/128<1/25.

Los factores de momentos beta y sus denominadores exactos son correctos. La cota w2<-4+18tau² sigue de m0<-4,m-m0<=17tau²,cos>=1-x²/2,v2<1,log2<1. En v65/2, el cociente de densidades respecto del caso derivado en u es entre u²/v² y1; el segundo momento aumenta a lo sumo por(v/u)^2 y permanece<1/20. Así la integral de T2 es estrictamente negativa y el fallo de E2new>=R0E2old queda certificado para un movimiento explícito. Este test no tiene base E2 positiva y no refuta la versión restringida a V12.

## Identidad completa nueva de §6

Sea G(s)=sF0(s)/(s+v). Su densidad es tau²/(v²+tau²)|F0|² y sus momentos satisfacen

    Polar[G]=-Polar[f0]/[4(v²-1/4)].

Cada término de la forma depende linealmente de esa autocorrelación, y el polar coincide con esa misma identidad. Por tanto

    W[fv]-R0W[f0]=(1-R0)W[G]

es EXACTA para la forma completa, al igual que su versión E2. El contraejemplo del memo sólo prueba E2[G]<0: la cola de contactos que distingue W de E2 no está evaluada y no puede inferirse W[G]<0. La identidad establece un objetivo acoplado legítimo para los subespacios G; no demuestra su signo.

La condición R12 es suficiente para el primer movimiento desde la base declarada, pero no para una secuencia global de movimientos si no se comprueba en los espacios intermedios. La advertencia del constructor es correcta. Ningún falsificador aquí cierra esas restricciones ni el signo completo.
