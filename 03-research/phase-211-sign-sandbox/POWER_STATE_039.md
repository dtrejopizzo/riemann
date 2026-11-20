# Estado039 — Signo de los inversos aritméticos completos en una cola más amplia

Estado: PROVED y auditado. Sustituye STATE038 como resumen de trabajo. Goal activo, signo global OPEN, papers intactos.

## Producto infinito firmado: resultado uniforme

POWER_INFINITE_SHOULDER_039 demuestra, a u=63/2, para TODOS N>=4,000,000:

    h_N(x)>0 y K_N(x)>0 para TODO x>=exp(T_N),
    T_N=2(N−1)v_N/(u²−v_N²), v_N=1/2+1000/sqrt(N).

Son los inversos aritméticos COMPLETOS, con todos los enteros Möbius. No es un certificado de grupos finitos. El corte satisface

    T_N=(N−1)/992+(1985·1000/992²)sqrt(N)+O(1)<(N−1)/330.

Mejora el corte anterior026 para el MISMO K_N; h_N se trata explícitamente por separado. T_N es aquí el logaritmo de una coordenada x del núcleo, NO la ventana T del Paper47.

## Mecanismo y control cuantitativo

Se inclina el perfil gamma por v>1/2 y se centra en t_v=2(N−1)v/(u²−v²). En sigma=v+1/2>1, el producto Euler infinito, sus momentos y las sumas usadas convergen absolutamente. Se conserva su multiplicador firmado en Fourier, como038, pero ahora no queda una suma coprima exterior sin estimar.

Una prueba elemental de psi_Lambda(x)<=2x da A_sigma<=5/(sigma−1), B_sigma<=5/(sigma−1)² en el rango. El normalizador Fourier es uniforme para ambos perfiles c=1/2 y3/2 y para v<=2; se compara su modo con el centro mediante Riccati. El perfil trasladado permanece en su lado físico positivo. Para v entre v_N y2, ambos cocientes h/H y K/G están entre .9U_sigma y1.1U_sigma, donde U_sigma=prod(1−p^−sigma)>=(sigma−1)/sigma>0.

La monotonía de t_v cubre un intervalo entero. Desde t_2 hasta infinito, una cota de dilatación m^−2 controla el resto absoluto y da cocientes mayores que1/4. Se obtiene así TODA la cola, sin campaña de índices ni truncación aritmética.

## Evidencia y obligación restante

POWER_SHOULDER_AUDIT_039 aprueba prueba completa y constantes. Root y dos revisores independientes comprobaron Fourier, normalizador, momentos elementales, Fubini del producto infinito, argumento trasladado físico y unión de colas. Verificador exacto reproducido por root y auditor: PASS. No evalúa nuevos valores W ni listas de primos.

La mejora frente038 es el control del inverso infinito real en la región declarada. No demuestra el signo de esos núcleos en el interior, ni compara su contribución con la parte adversa interior y el término arquimediano de W. El centro crítico sigma=1 tampoco se incluye. No se ha probado nueva fila de W, combinación arbitraria ni ventana del Paper47.

Se conserva la cobertura035: átomos de filas1..17, cualquier k>=0, a u31.5 con W>norma²/40, además de las regiones anteriores y el átomo211,1. El cierre global requiere un balance interior firmado adicional. No se declara completo ni bloqueado el goal.
