# POWER_REFLECTION_TEST_044 — La reflexión de densidades no conserva la forma real

Estado: **PROVED**, revisión independiente aprobada en [POWER_REDUCTION_AUDIT_044.md](POWER_REDUCTION_AUDIT_044.md); verificador exacto PASS. Tasa fija u=63/2. Papers intactos. No se refuta signo W ni toda posible reducción a subfamilias.

## 1. Corpus y propuesta falsable

Consultados ROUTES-TRIED-INDEX/README, grid maestro, CROSSWORD-TO-D y SCALAR_BRIDGE017; releídos los límites DESCENT016, TABLE_AUDIT018, ROW_PATTERN029 y MOVING_BALANCE036. Estos antecedentes impiden inferir densidad o signo desde una unión de familias positivas. Aquí no se vuelve a una mezcla de tasas grandes ni a una recurrencia positiva supuesta.

La propuesta concreta a probar/refutar es eliminar por una simetría REAL los sectores antisimétricos de las densidades racionales, reduciendo el blanco escalar a una diagonal equilibrada. Se demuestra una desigualdad ESTRICTA de la forma completa, con TODOS los contactos, que refuta esa simetría. La diferencia es sobre el funcional real dado, no sólo una obstrucción de densidad ni un modelo genérico. La entrada arquimediana se reutiliza de004; la recurrencia completa y la monotonía arquimediana normalizada ya constan en018. No se presentan esos cálculos como una técnica nueva. El chequeo nuevo es su aplicación exacta a la hipótesis de reflexión del puente017; no amplía las regiones de signo conocidas.

## 2. Por qué aparece la reflexión

Use q=tau²/(u²+tau²), t=q(1−q). Todo polinomio R(q) tiene una representación única

    R(q)=A(t)+(2q−1)B(t).

Prueba: descomponer R en partes simétrica y antisimétrica para q↔1−q. La simétrica es polinomio de t, porque q satisface q²−q+t=0. La antisimétrica es divisible por2q−1 y su cociente es simétrico.

Los átomos equilibrados k=N−1 de017 tienen, respecto a la densidad común |F1|², perfiles t^(N−1). Dos diagonales adyacentes permiten reconstruir el sector antisimétrico con coeficientes FIRMADOS. Esta reconstrucción lineal no preserva positividad. Para DESCARTAR ese sector mediante la reflexión haría falta que la forma anulara |F1|²(2q−1)B(t). Ya falla B=1 para el dato real.

No se afirma que cualquier reducción a una franja deba usar esta simetría ni que la representación firmada anterior sea un puente de positividad.

## 3. Desigualdad completa que falsifica la simetría

Tome dos funciones reales causales de norma L² uno:

    g_Q(y)=sqrt(4u)(1−uy)e^(−uy),
    g_L(y)=sqrt(4u)uy e^(−uy), y>=0.

Sus transformadas son sqrt(4u)QF1 y sqrt(4u)LF1, con Q=s/(s+u), L=u/(s+u), F1=1/(s+u). Las densidades se intercambian por q↔1−q. Se prueba

    W[g_Q]−W[g_L]>3/2.                              (ASYMMETRY)

### Arquimediano

La base ortonormal Laguerre de CONFLUENT004 es

    phi0=sqrt(2u)e^(−uy),
    phi1=sqrt(2u)(1−2uy)e^(−uy).

Aquí g_Q=(phi0+phi1)/sqrt2, g_L=(phi0−phi1)/sqrt2. La entrada arquimediana mixta, ya calculada exactamente allí, es

    b=(u/2)psi'((u+1/2)/2)=(63/4)sum_(r>=16)r^(−2).

La comparación integral de la cola da

    b>(63/4)[sum_(r=16)^31 r^(−2)+1/32]>1,

última desigualdad puramente racional. Por tanto el gap arquimediano es2b>2.

### Polar exacto

Evaluar las dos transformadas en s=±1/2 da

    Polar[g_Q]−Polar[g_L]
      =−2u(1+4u²)/(u²−1/4)²>−1/2.

No se omite la contribución polar ni se infiere su signo desde las densidades en el semieje: se evalúa exactamente la identidad racional fuera de él.

### Peine completo, con signo favorable

Integración elemental de las autocorrelaciones normalizadas produce para todo a>=0

    c_Q(a)=e^(−ua)(1−ua),
    c_L(a)=e^(−ua)(1+ua).

Así, con la convención Comb[g]=−2sum_(n>=2)Lambda(n)n^(−1/2)c_g(logn),

    Comb[g_Q]−Comb[g_L]
      =4u sum_(n>=2)Lambda(n)log(n)n^(−u−1/2)>0.

La serie es absolutamente convergente y TODOS sus términos son no negativos, con el de n2 estrictamente positivo. No se trunca ni se utiliza una cota numérica del peine. Sumando las tres partes se obtiene ASYMMETRY.

## 4. Alcance

El sector antisimétrico de las densidades no es invisible para la forma completa. En particular, la descomposición firmada del §2 no permite cerrar mediante sólo la diagonal equilibrada eliminando el sector restante por reflexión. El obstáculo proviene de una desigualdad del dato REAL y conserva su aritmética, no de un contraejemplo auxiliar.

ASYMMETRY compara dos valores W positivos ya incluidos en regiones probadas; no demuestra un valor W negativo ni excluye otra relación desigual entre franjas. No aporta por sí sola una nueva subfamilia suficiente. Una reducción válida tendría que controlar cuantitativamente el sector antisimétrico, no cancelarlo por una simetría inexistente. No hay campaña de parámetros.
