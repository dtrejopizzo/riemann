# Estado029 — Regiones uniformes en todos los órdenes y límite del puente positivo

Estado: tres resultados PROVED y auditados. Sustituye STATE028. Signo global OPEN; goal activo; papers intactos.

## Positividad real de W en regiones infinitas

POWER_ROW_PATTERN_029 demuestra para TODOS N>=2,k>=1,u²>=256N:

    W[f_(N,k,u)] > (7/10)||f_(N,k,u)||².

POWER_BOUNDARY_WEDGE_029 demuestra para TODOS N>=1,k>=0,u²>=4096N:

    W[f_(N,k,u)] > (2/5)||f_(N,k,u)||².

Ambos conservan TODO el peine aritmético y el término polar. Son teoremas uniformes, sin certificar dimensiones individuales. El segundo incluye k0, donde el momento espectral inverso utilizado por el primero diverge.

## Mecanismo elemental compartido

Cauchy–Schwarz con los dos pesos opuestos conserva el producto de sus normas. Comparar coeficientes de la serie WRN con los de (1−rho)^−(2N−1) da

    |c_f(t)|/norma² <= exp(−eta|t|)
       [(u²−eta²)/(u²−4eta²)]^(N−1/2), u>2eta.

Se cancela el coste lineal Neta/u de la estimación unilateral. El coste restante depende de Neta²/u². No contradice la obstrucción016 a uniformizar los pesos con u fijo y N/u² creciente.

Para k>=1, una cota inferior de digamma por sumación de Euler y los momentos beta dan ARCH>.9; el peine pierde menos de.16 y el polar adverso menos de.001. Para k0, se reemplaza el momento inverso singular por una cota de densidad espectral máxima y el resolvente1/(tau²+.25): ARCH>.45 en la región más fuerte; peine<.0002 y polar adverso<.001. La monotonía de ARCH en k extiende esa segunda prueba a todo k.

## Qué no aporta al puente a tasa fija

POWER_SCALE_BRIDGE_LIMIT_029 demuestra que las densidades normalizadas del dominio u>=C sqrtN tienen altura<=1/(C sqrtpi), incluso después de mezclarlas con pesos positivos. En un intervalo de longitud C/4 su masa es<1/4. Hay átomos de tasa fija u0=31.5 y orden grande con masa>3/4 en ese intervalo; su distancia L1 a todo ese cono es>1/2.

Por tanto no se puede sustituir automáticamente el cono de TODOS los átomos del puente017 por esta región de tasas crecientes. Es una obstrucción específica de aproximación positiva de densidades, no un contraejemplo de W ni un no-go para cualquier otro puente.

## Evidencia y región aún pendiente

POWER_SCALE_AUDIT_029 aprueba las tres pruebas; root leyó los textos y reprodujo ambos verificadores exactos: PASS. La uniformidad pertenece a las pruebas analíticas; los scripts sólo certifican constantes. El límite de puente usa una desigualdad integral, no una prueba numérica.

A u31.5, la región C16 sólo alcanza N<=3 y la C64 no añade órdenes. La cobertura de la tabla suficiente a esa tasa permanece: filas N1..5 para todo k y cono k>=10000N². También siguen los ocho polos arbitrarios y bloque fijo12. Resta N>=6,k<10000N²; no se ha certificado una nueva ventana T ni el signo global.

La continuación debe recuperar información en N/u² grande y conservar las cancelaciones aritméticas. Reducir constantes de estas regiones puede ampliar parámetros, pero no elimina por sí solo esa obligación.
