# POWER_PRIME_TRANSFER_014 — Filtro de un polo, núcleo firmado y límite de ordenación con el contacto 2

Estado: PROVED identidades y falsificador explícito de una desigualdad universal concreta. OPEN transporte restringido al bloque aritmético positivo V12. No se declara NO-GO para esa restricción ni para el signo global. Papers intactos.

## 1. Antecedentes y diferencia

Consultados las reglas del proyecto, índice ROUTES-TRIED-INDEX (N_018, semilocal/exterior E/J, convexidad F), grid/crucigrama registrados en BRIDGE002; memos POLAR_MOVEMENT005, ARITHMETIC_BLOCK007, PRIME_PATTERN008, TATE_CHAIN009, COMMON_TRANSFER010 y el límite de envolventes013. Las identidades Euler/Möbius no aportan aquí nuevo signo, y la monotonía AP ya fue refutada.

La pregunta nueva es más específica: si el contacto 2, que rescata TODO V12, se conserva favorablemente al desplazar un polo. Se deriva su cambio conjuntamente con ARCH y POLAR, sin suponer que las evaluaciones de autocorrelación sean positivas. El resultado identifica el operador firmado exacto y refuta una ordenación universal más fuerte que sería tentador usar. No se confunde esa refutación con fracaso del problema restringido a V12, cuya base sí es coerciva.

## 2. Cambio exacto de la autocorrelación

Para v>u=63/2, filtre una función racional causal f0 por H(s)=(s+u)/(s+v), manteniendo el mismo numerador. Escriba f_v=Hf0, R0=u²/v². En Fourier,

    |H(i tau)|²−R0=(1−R0)tau²/(v²+tau²).

Sea P_v(t)=(v/2)e^(-v|t|), núcleo positivo de masa uno. Su transformada es v²/(v²+tau²). Por inversión,

    c_fv(t)−R0 c_f0(t)
      =(1−R0)[c_f0(t)−(P_v*c_f0)(t)].                   (C)

Equivalentemente, el corchete es

    (v/2)∫_0^infinito e^-vs
      [2c_f0(t)−c_f0(t+s)−c_f0(t−s)]ds.

El cambio NO es convolución por un núcleo positivo: su núcleo es delta−P_v, de masa cero y ambos signos. En particular el signo en t=log2 exige control de una segunda diferencia de la autocorrelación alrededor del contacto; la positividad definida de c no fija ese signo.

## 3. Cambio acoplado ARCH+contacto2+POLAR

Defina E2[f]=Arch[f]−v2 c_f(log2)+Polar[f], v2=2Lambda(2)/sqrt2=sqrt2 log2, y w2(tau)=m(tau)−v2 cos(tau log2). Los momentos bajo el filtro se multiplican por H(−1/2),H(1/2), y

    r0−R0=−(1−R0)/[4(v²−1/4)].

Por tanto se obtiene la identidad ACOPLADA exacta

    E2[f_v]−R0 E2[f0]
      =(1−R0){(1/2pi)∫w2(tau)tau²/(v²+tau²)|fhat0|²d tau
                        −Polar[f0]/[4(v²−1/4)]}.        (T2)

No se han sustituido términos por sus normas ni separado un polar de signo supuesto. Un eventual transporte coercivo con constante c usa la misma identidad con w2−c en la integral y E2−c||·||² en ambos lados.

Para la forma COMPLETA la versión temporal sustituye el término del contacto 2 por

    −Σ(q>=2)v_q[c_f0(logq)−(P_v*c_f0)(logq)].

Para cada función racional de orden fijo, las sumas convergen absolutamente. No se escribe un supuesto símbolo puntual de la suma infinita de cosenos, que no convergería de esa manera. La cancelación firmada requerida queda justamente en estas segundas diferencias en todos los contactos.

## 4. Falsificador explícito de ordenación universal E2[f_v]>=R0E2[f0]

La ordenación anterior es falsa si se afirma para TODOS los numeradores y órdenes. Use exactamente el test Tate de008:

    n=2^17, g_n=y^(n−1)e^-uy/(n−1)!,
    f0=(∂²−1/4)g_n,
    F0(s)=(s²−1/4)/(s+u)^n.

El filtro mantiene el numerador Tate, de modo que Polar[f0]=Polar[f_v]=0 para todo v>=u. El derivado derecho de T2 en v=u es

    d/dv [E2[f_v]−(u²/v²)E2[f0]]_(v=u)
      =(2/u)(1/2pi)∫w2(tau)tau²/(u²+tau²)|F0(i tau)|²d tau. (D)

La integral es estrictamente negativa por una cota racional, sin matriz ni barrido. Se sabe de008 que m(tau)≤m(0)+17tau² y m(0)<−4. Además v2<1 y log2<1; por cos x>=1−x²/2,

    w2(tau)<−4+18tau².

Normalice la medida de la integral D: su densidad es proporcional a

    tau²(tau²+1/4)²/(u²+tau²)^(n+1).

Los momentos beta de la probabilidad base de denominador (u²+tau²)^(n+1) dan, al dividir por su segundo momento,

    E_D tau²
      ≤3u²/n+120u^4/n²+1680u^6/n³
      <3/128+120/128²+1680/128³<1/25.

Los denominadores exactos 2(n+1)−5,−7,−9 son mayores que n, y u²<1024, n=128·1024. Se acotó el denominador ponderado por (1/16)M2, igual que en008. Así E_D w2<−4+18/25<0. La integral D tiene masa positiva y es negativa.

Consecuencia: existe epsilon>0 tal que para u<v<u+epsilon,

    E2[f_v]<(u²/v²)E2[f0].                               (FAIL)

También se obtiene un valor de v completamente explícito, sin determinar epsilon: tome v=65/2. La densidad de la integral de T2 dividida por la de D se multiplica por (u²+tau²)/(v²+tau²), entre u²/v² y1. Su segundo momento normalizado es por tanto menor que (v/u)²/25<1/20, pues (65/63)²<5/4. De nuevo E w2<−4+18/20<0. Así FAIL vale específicamente para v=65/2: se ha desplazado UN polo de63/2 a65/2 manteniendo los otros n−1 fijos y el numerador s²−1/4.

Se refuta exactamente la ordenación universal propuesta. NO se ha refutado transporte de coercividad sobre V12: este test tiene orden n enorme y E2[f0] ya es negativa. La hipótesis «base restringida positiva» cambia sustancialmente el problema y no está cubierta por FAIL.

## 5. Obligación restringida que sigue válida

Para obtener un paso de transporte desde el bloque aritmético positivo V12, una condición suficiente concreta sería demostrar, para todo f0∈V12 y todo v>=u,

    (1/2pi)∫[w2(tau)−c]tau²/(v²+tau²)|fhat0|²d tau
          −Polar[f0]/[4(v²−1/4)]>=0,                    (R12)

con c por debajo de su coercividad E2 certificada. Esto usaría el signo conjunto de ARCH+contacto2+POLAR y no una envolvente puntual independiente del numerador. La identidad T2 prueba su suficiencia para ese paso, pero aquí no se prueba R12.

Incluso resolver R12 solo para el primer movimiento desde V12 no autoriza mover doce polos sucesivamente: después del primer paso, el espacio base ha cambiado. Una inducción global necesitaría una versión para la familia de espacios intermedios o una desigualdad conjunta de producto de filtros. Ésta es una obligación explícita adicional, no un detalle omitido.

## 6. Interpretación exacta como forma de la corrección firmada G

La identidad nueva de SIGNED_TRANSFER014 identifica una estructura más útil que una ordenación genérica. Para un solo polo, defina la función causal G por

    Ghat_L(s)=s F0(s)/(s+v).

Su transformada de Laplace tiene numerador divisible por s, de modo que ∫G=Ghat_L(0)=0. Pertenece a un espacio racional de n+1 polos, con una restricción lineal. Además

    |Ghat(i tau)|²=tau²/(v²+tau²)|F0(i tau)|²,
    Polar[G]=−Polar[f0]/[4(v²−1/4)].

Por tanto el corchete completo de T2 es EXACTAMENTE E2[G], y la versión con TODOS los contactos da

    E2[f_v]−R0E2[f0]=(1−R0)E2[G],
    W[f_v]−R0W[f0]=(1−R0)W[G].                          (GAIN)

La convergencia ya justificada permite la segunda identidad sin un símbolo infinito puntual. En varios movimientos el producto de filtros se descompone en la suma de cuadrados |G_j|² de SIGNED014, y las contribuciones polares siguen la misma identidad por evaluar los factores racionales en ±1/2. Se conserva así la forma completa de cada corrección, no solo su parte arquimediana.

Esto aclara el alcance del falsificador§4: prueba E2[G]<0 para un G explícito de gran orden, pero NO prueba W[G]<0. Precisamente faltan todos los contactos que pueden repararlo, igual que en008. No constituye objeción a la ruta restringida con el peine COMPLETO ni se usa como un NO-GO adicional.

**Ruta precisa que sirve para todos los órdenes:** demostrar una desigualdad firmada para W sobre las correcciones racionales G_j de numerador divisible por s, conservando todos los contactos. Si se obtiene no negatividad en esos espacios restringidos para cada orden, GAIN transporta cualquier cota base no negativa correspondiente bajo movimientos de polos. Para transportar una coercividad c se utiliza W[G_j]−c||G_j||² en lugar de W[G_j]. Los certificados actuales de SIGNED014 resuelven casos de orden finito mediante la ganancia restringida arquimediana; el régimen en que esa ganancia también necesite aritmética pide una nueva desigualdad para estas MISMAS correcciones.

Esta ruta no omite la base: probar ganancias restringidas para todos los órdenes no prueba por sí solo todos los bloques confluentes iniciales, cuya positividad sigue requiriéndose si se quiere usar el puente de densidad. Tampoco permite inferir ganancias completas a partir de E2 ni de cada contacto favorable. Son obligaciones exactas que se pueden trabajar conjuntamente.

## Resultado y alcance

Se obtuvo el generador firmado exacto del cambio de autocorrelación, su identificación como forma completa de la corrección G y una refutación analítica de la ordenación universal para el peine PARCIAL {2}. El blanco útil es la desigualdad sobre las correcciones G_j con TODOS los contactos. Este blanco no queda refutado por el contraejemplo parcial ni por los límites de envolventes013. No se obtuvo aquí una nueva desigualdad aritmética de signo completa.
