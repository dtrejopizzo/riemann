# POWER_THETA_G_COMPACT_AUDIT_080 — Auditoría del certificado continuo

Estado: **APROBADO matemáticamente y en código; constructor FULL PASS.** Reproducción independiente root92790 exit0/FULL PASS de los4096paneles y hash coincidente. No se ha ejecutado una cuarta copia innecesaria. Fuente constructor `POWER_THETA_G_COMPACT_080.md` leída íntegramente y aprobada; código estable `tools/power_theta_g_compact_080_verify.py`.

Hash SHA256 comprobado localmente:

    640d8eb8ecf2bce7e782e08333a722171744af8fc0c9831582fcfcb796fb09bc

## 1. Objeto y diferencia respecto de los antecedentes

Consultados las reglas del proyecto y los tres registros,073/078/079. La obligación nueva es el signo de la curvatura REAL en un compacto fijo, no promoción de pares a mayor orden por monotonías genéricas.079 ya aporta una prueba algebraica de que BASE073 más g cóncava en cuadrados basta para tres generadores de la forma completa.078 cubre u>=63/2. El certificado presente cubre el intervalo restante [1/2,63/2], conservando toda la aritmética mediante la función entera real.

## 2. Función entera y jets

Con A=u+1/2, E(A)=A[1+(A−1)zeta_deflate(A)]Gamma(A/2)exp(−A log(pi)/2). La deflación oficial es zeta(A)−1/(A−1), por lo que E=A(A−1)zeta(A)Gamma(A/2)pi^(−A/2), regular también en A=1. E es un múltiplo constante positivo de la transformada Z de Phi real; por tanto sus derivadas logarítmicas coinciden con M,M',M'' del corpus. No se pierde un factor de escala dependiente de u.

La API REAL usada está documentada en https://arblib.org/arb_poly.html y https://flintlib.org/doc/arb_poly/_arb_poly_zeta_series.html. Los autotests A=1/A=2 son controles adicionales, no la prueba de la identidad de funciones. La rama real del log se autoriza sólo tras E[0]>0. Los jets se calculan con python-flint0.9.0,256bits y cap20. LogE hasta grado19 deja M'' hasta16; el código exige Delta.prec>=17 y finitud de todos los coeficientes0..16. No se rellenan coeficientes desconocidos con cero.

Delta=M²+uMM'+u²MM''−2u²(M')². Su positividad da g''=−a Delta/(4u³M³)<0, con a=M'(0)>0 y M>0. Todos los coeficientes Taylor están normalizados por k!, sin factorial extra.

## 3. Resto Cauchy uniforme, revisado independientemente

Para cada centro c de la malla, disco complejo |z−c|<=r=1/16. La positividad/paridad de Phi y M creciente dan Z(c+r+1)/Z(c)<exp(17/16)<3: en todo el intervalo real necesario M<1, pues el ancla real t=33+1/2, A=34 da M<log6/2+1/16<1 y cubre todos los puntos necesarios por monotonía.

Las desigualdades |x|^k<=k!exp(|x|) y simetría dan |Z^(k)(z)|<=2k!Z(c+r+1). También |Z(z)−Z(c)|<2r Z(c+r+1)<3Z(c)/8. Así Z no se anula en ese disco y las razones de sus tres primeras derivadas están acotadas por48/5,96/5,288/5. Resultan |M|<10, |M'|<120, |M''|<2700. Con |u|<32, |Delta|<60000000. Estas operaciones y constantes fueron comprobadas también por Fraction exacta.

Cauchy controla TODA la cola del Taylor de grado16 en |u−c|<=h=31/8192 por

    T=60000000(31/512)^17/(1−31/512)
     =5285183618944392932503807265625/
      41901009533176678637026095660718210485846016
     <10^−12.

No se necesita ningún jet de zeta en un intervalo ancho. La serie log local es válida en el disco porque Z no se anula, no sólo porque el centro sea positivo.

## 4. Malla y certificado

Los4096centros son dyádicos exactos c_j=1/2+(2j+1)31/8192 y el mismo h cubre exactamente[1/2,63/2], sin huecos. En cada panel el lower certificado es Delta0(c)−sum(k=1..16)|Deltak(c)|h^k−T>0. Todas las magnitudes se calculan outward mediante arb; ni un float ni un valor muestreado reemplazan la cota del panel. Constructor43260 terminó exit0/FULL PASS regularización y4096paneles, con hash arriba. Root92790 reprodujo exit0/FULL PASS y el mismo hash; no se necesitó otra corrida.

Se conserva la historia: los primeros encierros de resto por jets intervalares fallaron por dependencia, sin producir Delta negativa. Se cambiaron representaciones de resto (directo, Taylor2, Taylor4, finalmente Cauchy); no se cambiaron intervalo, malla4096, precisión256 ni margen de signo0. El certificado final es grado16/cap20 con resto analítico externo, no el fallido grado5. No se presenta ninguno de los FAIL como contraejemplo ni como PASS.

## 5. Consecuencia y límites

Empalmando este certificado con078 se obtiene g''<0 para todos u>=1/2. BASE073 y079 dan el kernel completo positivo definido para tres nodos distintos ui>1/2, es decir tres potencias arbitrarias ai=ui+1/2>1. Nodos repetidos se agrupan: positividad estricta para la función representada no nula. La congruencia con W es la deCONE001 y conserva ARCH, polar y TODOS los contactos; no se trata de positividad de un componente aislado.

Esta amplía triples a exponentes pequeños y mezclados, más allá de la región rates>=31.5 de053. NO prueba cuatro ni todos los órdenes, ni una ventana temporal nueva ni el objetivo global del Paper47.081/082 y las obligaciones recursivas permanecen separadas. Papers intactos.
