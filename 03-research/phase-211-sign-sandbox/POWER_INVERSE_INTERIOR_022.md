# POWER_INVERSE_INTERIOR_022 — Un punto interior del inverso completo

Estado: PROVED un punto negativo del inverso COMPLETO, certificado racional ejecutado y revisión independiente final APROBADA. El constructor principal y el auditor reprodujeron el verificador. Papers intactos.

## Corpus y razón nueva antes de construir

Leídos las reglas del proyecto, SIGNED_MEAN019 (fallo SOLO de prefijos), INVERSE_KERNEL020 (positividad exterior completa), sus auditorías y búsquedas dirigidas en índice/grid/crucigrama sobre inverso/kernel/Möbius/signo. La diferencia exacta es decidir una suma COMPLETA en UN punto interior, con cola rigurosa; no se infiere nada desde el prefijo019 ni desde la región exterior020.

Se elige N=128,x=1 porque la aproximación gamma local del término derivativo en el contacto2 tiene escala (u²log2/(2N))exp(−u²(log2)²/(4N)), cuyo máximo en N cae cerca de u²(log2)²/4≈119. La aproximación solo motiva el punto; no participa en el certificado. El corte64 se fija por monotonía: log64>127/32, lo que permite cotar TODAS las colas de potencias logarítmicas de grado hasta127 por una integral.

## 1. Resultado sobre la suma completa

Con los kernels exactos de020, se prueba

    −2/3 <h_128(1)<−33/50<0.                            (NEG)

La suma incluye TODOS los enteros m de la inversión Möbius. En particular es falso el lema «h_N(x)>=0 para todos N>=2,x>=1». Esto refuta una premisa posible de la recuperación de signo por019; no refuta el signo de la forma de Weil ni de ERR.

El resultado complementa OUTER020: para N=128 se sabe h_128(x)>=H_128(x)/4>0 si logx>=127/30. La negatividad en1 y la continuidad implican una región interior negativa y al menos un cambio de signo antes de esa frontera. No se extrapola el signo a otros N.

## 2. Polinomio positivo exacto utilizado

Se reconstruyen los coeficientes racionales mediante

    p_0=1,
    p_(j+1)=p_j·[2u(N−1−j)]/[(j+1)(2N−2−j)],
    a_j=32p_j−(j+1)p_(j+1), j<127,
    a_127=32p_127,
    A_128(t)=Σ(j=0..127)a_j t^j.

La prueba de020 da a_j>0 y a_0=1/2; el script también verifica estos signos racionalmente. El kernel es

    H_128(x)=x^-33 A_128(logx),
    h_128(1)=Σ(m>=1)mu(m)m^-32 A_128(logm).

No se imprimen128 coeficientes extensos: la recurrencia racional los determina íntegramente sin parámetros numéricos.

## 3. Segmento finito con logaritmos encerrados

El script `tools/power_inverse_interior_022_verify.py` calcula mu(m) para1<=m<=64 por factorización entera elemental: un factor primo repetido da0, y cada factor primo distinto invierte el signo. No usa una tabla externa de valores Möbius.

Los logaritmos se encierran con el módulo racional explícito `power_fixed_grid_003.py`: reducción del argumento a[1,2], serie atanh y resto geométrico, con redondeo exterior en cada operación. Se evalúa A_128 por Horner intervalar y se acumula el segmento m<=64 conservando el signo de cada mu(m).

Todas las entradas y operaciones del certificado son Fraction; el valor decimal aproximado−.662345100449 se menciona solo como orientación y no participa en NEG.

## 4. Cola COMPLETA m>=65

Para0<=j<=127, la función x^-32(logx)^j decrece cuando logx>=j/32. Como log64=6log2>4>127/32,

    Σ(m>=65)m^-32(logm)^j
       <=∫_64^infinito x^-32(logx)^j dx.

Ponga L=21/5>log64. Por integración por partes y positividad, los mayores racionales de esas integrales se obtienen de

    I_0=64^-31/31,
    I_j=64^-31 L^j/31+(j/31)I_(j−1), 1<=j<=127.

Los coeficientes a_j positivos permiten cotar TODA la cola de Möbius, sin suponer cancelación:

    |Σ(m>=65)mu(m)m^-32 A_128(logm)|
       <=Σ(j=0..127)a_j I_j <10^-10.                    (TAIL)

El último signo es una comparación racional exacta ejecutada por el verificador. Este mayorante controla el complemento infinito del segmento calculado. Por ello NEG no es una inferencia desde un prefijo negativo.

Sumar el intervalo finito y el intervalo simétrico ±TAIL da los dos extremos racionales de NEG. El verificador ejecutado produce PASS.

## 5. Consecuencias limitadas para el emparejamiento con B

El signo B(x)<0 de019 no pasa al signo de F_N=2∫h_N B porque el inverso completo sí puede ser negativo. Por continuidad, para N128 existe un intervalo derecho de1 donde h_N<0 y B<0, de modo que el producto h_N B es positivo: aparece realmente una contribución adversa, no solo una pérdida de una cota.

Esto no determina el emparejamiento TOTAL: las regiones de h_N>0 aportan favorablemente y la región exterior positiva de020 se conserva. No se afirma W[g_128]<0 ni F_128>0. El dato nuevo es un falsificador completo y certificado de la hipótesis h_N>=0, con un solo N elegido analíticamente y una cola infinita rigurosa.
