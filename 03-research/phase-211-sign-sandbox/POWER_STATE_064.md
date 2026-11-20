# POWER_STATE_064 — Necesidad de escala cúbica para STRIP uniforme en todos los numeradores

Estado: **PROVED/APROBADO**, revisión independiente en POWER_STRIP_CUBIC_AUDIT_064.md; constructor, root y mapa verificaron también el umbral mejorado j≥10^6n. No nuevo signo de W. Papers intactos.

## Resultado probado

Fuente: POWER_STRIP_CUBIC_NECESSITY_064.md. Fijar u=63/2 y0<η<u. Para TODOS n≥4 y j≥10^6n se construye un polinomio REAL no nulo P_(n,j), grado<n, tal que la densidad del test s^jP/(s+u)^(n+j) satisface

    ∫|ρ(x+iη)|dx / ∫ρ(x)dx ≥1+η²n³/(1152u²j).

Por tanto no puede existir un D finito uniforme en todos los numeradores sobre un cono j≥C n^p con p<3: elegir j=max(ceil(Cn^p),ceil(10^6n)) hace divergir el lower. Esta conclusión se refiere únicamente al bound ABSOLUTO de contorno STRIP, no a negatividad de W ni a imposibilidad de un cono de signo más pequeño.

## Mecanismo y diferencia frente059

059 emplea P=1 y sólo fuerza exponente al menos2. Aquí P varía con n,j: en frecuencia inversa se toma el polinomio ortonormal Student de grado d=n−1. Su paridad produce un numerador real par. La recurrencia exacta tiene k/8≤β_k≤4k hasta n+4; proyectar el generador060 sobre el grado d+3 deja una componente≥n^(3/2)/24 y un resto≤n^(3/2)/48. Así ||H′||²/||H||²≥n³/(2304u²j). Como la densidad construida es H² con H real, la convexidad par de las normas desplazadas prueba el lower de STRIP.

No se usa un paquete gaussiano con colas no controladas ni se supone que un pico estrecho tenga varianza pequeña. La construcción y las cotas son analíticas; no hubo campaña numérica ni nuevo caso de signo.

## Qué sigue vigente

060 continúa probando STRIP uniforme y W>norma² para todos los numeradores en j≥10^12(nq_n)^3, q_n=ceil(log2(n+1)).064 muestra que la potencia3 es necesaria para esa estrategia absoluta; no decide los factores logarítmicos. Los segmentos iniciales y el objetivo global permanecen abiertos. La positividad de trece polos arbitrarios053 y el caso interior129,0 de061 no se modifican. No se amplía una ventana temporalT ni se toca ningún paper.

## Deduplicación adicional: recurrencia normalizada en el borde k0

Para la familia con tasa u, sea G_N(s)=(s+u)^−N y H_N(s)=s/(s+u)^(N+1). Definir con sus normas RESPECTIVAS

    A_N(u)=W[g_N]/||g_N||²,
    B_N(u)=W[h_N]/||h_N||².

Las identidades completas ya conocidas de016/036 y la relación de derivación029 son

    B_N=A_N+u∂_u A_N,
    A_(N+1)=(2N A_N−B_N)/(2N−1)
            =A_N−u∂_u A_N/(2N−1).

La derivada se toma en la familia de tasas y después puede evaluarse en u=63/2. Se conservan ARCH, polar y TODOS los contactos; no se supone un signo al derivar.

Propagar A_N≥0 al siguiente orden requiere el bound concreto B_N≤2N A_N. Un descenso monótono desde infinito podría usar B_N≥A_N junto con liminf_(N→∞)A_N≥0. Ninguna de esas nuevas desigualdades se ha demostrado aquí. La identidad y las diferencias del peine reproducen los antecedentes016/036 y Bessel019; no se presentan como nueva herramienta de signo ni se infiere que la positividad aislada de B_N las implique.

Esta revisión, coordinada entre insight048 y root, queda registrada como deduplicación. No añade cobertura W ni una entrada teoremática nueva a los índices.
