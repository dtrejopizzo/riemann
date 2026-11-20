# POWER_SIGNED_AUDIT_014 — Revisión independiente del cierre global de ocho polos

Estado: PROVED. POWER_SIGNED_TRANSFER_014.md y tools/power_signed_transfer_014_verify.py revisados íntegramente. Ejecución independiente del verificador con PASS. Papers intactos.

## 1. Telescopaje exacto y restricción preservada

Para A_j=v_j²(u²+x)/[u²(v_j²+x)], se verifica A_j-1=x(v_j²-u²)/[u²(v_j²+x)]. Al multiplicar por el producto de los A_k anteriores y por |P|²/(u²+x)^n, los factores quedan exactamente

    kappa_j=(v_j²-u²)/u² prod_(k<j)v_k²/u²,
    |G_j|²=x|P|²/[(u²+x)^(n-j+1)prod_(k<=j)(v_k²+x)].

Así TEL conserva la constante R0, los exponentes y todos los términos cruzados del numerador; no hay una raíz o un factor de norma faltante. Cada kappa_j es no negativa y G_j tiene n+1 polos y numerador sP, de grado<=n y con cero en s0. La condición se refiere a la transformada Laplace, no al valor temporal del vector.

El movimiento arquimediano de004 se aplica al MISMO subespacio de polinomios Q de grado<n+1 con Q(0)=0: el mapa de denominadores mantiene Q exactamente. Por tanto la cota confluente restringida sí se transporta a todos los G_j. Al integrar TEL contra m-c, cada sumando es una forma arquimediana menos c veces su norma; el signo positivo deriva de la coercividad del bloque restringido, no de que m sea puntual positivo. Esta es una estimación distinta de la clase descartada en013.

## 2. Dos certificados intervalares y el Gram correcto

Las nueve bandas arquimedianas se forman con las derivadas psi en16 hasta orden8, sumadas16..2000 y encerradas mediante integrales desde2001/2000, con signos correctos. Los intervalos de gamma,pi y logaritmos fueron auditados previamente; todas las operaciones usan redondeo exterior racional. LDL intervalar de AP8-(7/200)I pasa con ocho pivotes inferiores positivos.

En el bloque restringido Arch9, evaluar Laplace de la base Laguerre en0 da sqrt(2/u)(-1)^j. Por ello la base B_i=e_i-(-1)^i e8, i0..7, describe exactamente el núcleo de esa evaluación. Las entradas comprimidas son

    Arch_|i-j|-a_j Arch_(8-i)-a_i Arch_(8-j)+a_i a_j Arch0.

El programa resta(1/4)(delta_ij+a_i a_j), que es EXACTAMENTE(1/4)B^t B y no una identidad indebidamente normalizada. Su LDL intervalar pasa. Así gamma1/4 es una cota de forma respecto de la norma física para TODO el subespacio.

Las dos normas de momentos de ocho componentes satisfacen4AA BB<(3/2)^2, justificando p3/2. El margen b-c-p*8/3969, con b7/200 y c3/100, es>1/1000. Integrar la descomposición y mantener el polar produce AP>.03 en todos los ocho polos reales>=31.5. No se presupone monotonía de AP.

## 3. Todos los contactos y margen final

La traza ponderada con alpha3/5 está cubierta por POWER_COMMON_TRANSFER_010§6; sigma189/10<min v_j. Su suma binomial exacta satisface4T8<25000². Con beta97/5, la cola conserva el factor fraccionario2^-2/5<19/25: elevar a quinta potencia equivale exactamente a25^5<4*19^5. La cota decreciente de(logx)x^-beta desde2 y beta-1>18 dan el mayorante racional del script<29/1000.

Por tanto la forma COMPLETA satisface W>.001||f||² para cualquier numerador real de grado<8 y cualquier conjunto de ocho tasas>=31.5, permitiendo multiplicidades, separación arbitraria y tasas sin cota superior. El peine es infinito completo, sin hipótesis de signo favorable de sus matrices individuales. No se infiere ningún resultado de dimensión mayor ni cierre del Paper47.

## 4. Alcance del avance frente al límite previo

La ronda013 seguía siendo correcta: prohibía reemplazar la densidad racional por un peor coste puntual y descartar ganancias positivas. La prueba actual conserva la integral firmada y demuestra su positividad sobre un subespacio racional restringido, usando TEL y un bloque certificado. Cambia explícitamente una hipótesis esencial de aquella clase, sin contradicción ni reinterpretación de un falsificador como signo negativo de la forma.
