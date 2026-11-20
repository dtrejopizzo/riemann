# POWER_ROW_SPLIT_028 — Separar el borde polar k=0 de la órbita k>=1

Estado: PROVED toda la fila N5 con margen uniforme en k y u, certificado racional ejecutado. Revisión independiente APROBADA en POWER_ROWS_AUDIT_028.md; root reprodujo el verificador PASS. No campaña. Papers intactos.

## Corpus y razón nueva antes de construir

Leídos las reglas del proyecto, INTERIOR017 (WRN), las filas completas N1–3 de018, LOW_TABLE018, ARCH_CELL026 y los estados vigentes; búsquedas en índice/grid/crucigrama (covarianza/primeras diferencias/polar/borde). La monotonía arquimediana y la cota WRN ya están probadas y no se presentan como novedades.

La diferencia aquí es una separación NUEVA de obligaciones: no se exige ARCH positiva en k=0. Allí se conserva el polar positivo, dividiendo u en dos intervalos por monotonías de componentes; desde k=1 se usa la ganancia de covarianza y se controla solamente el polar impar pequeño. Se intenta cerrar TODA la fila N5 con esos pocos extremos analíticos, no certificar una lista de k.

## 1. Resultado infinito

Para N=5, TODOS los enteros k>=0 y TODAS las tasas u>=63/2, sea f_(5,k,u) de transformada

    F(s)=s^k/(s+u)^(5+k).

Entonces

    W[f]>(1/25)||f||².                                  (ROW5)

Para todo k>=1 vale la cota más fuerte W[f]>(4/5)||f||². El caso k=0 se cubre conservando su polar positivo; de hecho ARCH_50(63/2)<−1/10, por lo que el argumento previo «ARCH positiva desde k0» no sirve para esta fila.

## 2. Dos monotonías que cubren parámetros infinitos

Escriba A_(N,k)(u)=Arch[f]/||f||². La probabilidad espectral es proporcional a tau^(2k)/(u²+tau²)^(N+k). Para u fijo, pasar de k a k+1 multiplica esa probabilidad por Z=tau²/(u²+tau²), normalizando. Como m(tau) y Z crecen en |tau|,

    A_(N,k+1)(u)−A_(N,k)(u)=Cov(m,Z)/E Z>0.

Por otro lado, tau/u tiene una ley independiente de u. Como m crece en |tau|, A_(N,k)(u) crece con u. Así para k>=1,u>=u0=63/2,

    A_(5,k)(u)>=A_(5,1)(u0).

No se afirma monotonía de la forma COMPLETA ni de AP; el polar se tratará aparte.

## 3. Constantes arquimedianas exactas, solo en los extremos necesarios

La base racional ortonormal Laguerre de tasa u tiene bandas arquimedianas Toeplitz

    r_0=psi((u+1/2)/2)−logpi,
    r_l=(1/2)Σ(j=1..l)binom(l−1,j−1)u^j
                             psi^(j)((u+1/2)/2)/j!.

Si z=(s−u)/(s+u), la transformada de f_(N,k,u) tiene en esa base los coeficientes del polinomio (1−z)^(N−1)(1+z)^k, salvo un factor común que cancela en Rayleigh. Para N5,

    k0: v0=(1,−4,6,−4,1), ||v0||²=70,
    k1: v1=(1,−3,2,2,−3,1), ||v1||²=28.

El verificador racional adjunto encierra las derivadas de psi mediante sumas positivas de256 términos más colas integrales; los valores psi16 y psi(127/4) se obtienen por recurrencia de los valores cuartos y constantes racionalmente encerradas. Evalúa SOLO los extremos usados por las monotonías y prueba

    −13/100 <A_(5,0)(63/2)<−1/10,
    A_(5,1)(63/2)>9/10,
    A_(5,0)(63)>1/2.                                    (ARCH)

No hay una lista de k ni una interpolación desde puntos. Los dos u son los extremos de los intervalos de la siguiente sección.

## 4. Polar exacto y separación de k0

Sea a=u²−1/4. El polar normalizado tiene signo (−1)^k y magnitud

    p_(N,k)(u)= (4pi/u)(u²/a)^N
                      (4u²−1)^(-k)/B(k+1/2,N−1/2).

En particular

    p_(N,0)(u)=4^N/[u binom(2N−2,N−1)]·(u²/a)^N,
    p_(N,1)=p_(N,0)N/(2a),
    p_(N,k+1)/p_(N,k)=(k+N)/[(k+1/2)(4u²−1)].

Para N5, p_(5,0)(u) decrece con u, y el certificado racional da p_(5,0)(63)>23/100. En u∈[63/2,63], ARCH y polar se acotan entonces por extremos OPUESTOS:

    AP_(5,0)(u)>−13/100+23/100=1/10.

En u>=63, ARCH>1/2 y el polar sigue siendo positivo. Esta división no utiliza una monotonía AP no demostrada.

Para k>=1, el cociente sucesivo de las magnitudes polares es <=4/(4u0²−1)<1. Además p_(5,1)(u) decrece con u y p_(5,1)(u0)<1/500. Por tanto el polar impar de cualquier k>=1 es >−1/500; en k par se conserva su signo favorable.

## 5. Todo el peine, uniformemente en k y u

El teorema WRN auditado en INTERIOR017 da, con eta12,

    ||e^(12y)f_(5,k,u)||²/||f_(5,k,u)||²<=R5(u,12),
    R5(u,12)=[u/(u−12)]^9 S5([12/(u−12)]²),
    S5(r)=[1+4r−2r²+(4/5)r³−(1/7)r⁴]/(1−r)^5.

La función S5 es creciente en r porque su serie original tiene coeficientes B_l^(5)>0; no se infiere esa monotonía desde los signos mezclados del numerador cerrado. Todos los factores de R5 decrecen con u. Para u0=63/2, r=64/169 y el certificado prueba

    R5(u,12)<=R5(u0,12)<2500.

Cauchy–Schwarz desplazado y Lambda(q)<=q dan para TODOS los contactos

    |Comb[f]|/||f||²
      <100Σ(q>=2)q^-11
      <=100·2^-11(1+2/10)<3/50.                         (PRIME)

Se reemplazó q^-11.5 por q^-11 para simplificar. La suma infinita completa converge y se controla sin asumir signo favorable de ningún contacto.

## 6. Cierre de TODA la fila

En k0,u∈[63/2,63], §§4–5 prueban W/norma²>1/10−3/50=1/25. En k0,u>=63 prueban W/norma²>1/2−3/50>1/25. Para TODOS k>=1,u>=63/2, §§2–5 dan

    W/norma²>9/10−3/50−1/500>4/5.

Queda probado ROW5 con margen independiente de los dos parámetros. El script `tools/power_row_split_028_verify.py` ejecutado da PASS en todas las comparaciones racionales necesarias.

## 7. Patrón analítico reutilizable, sin extrapolar filas

Para un N dado, el mismo argumento funciona si se dispone de U>=u0, un coste uniforme L_N de WRN, cotas b0<=A_(N,0)(u0), bU<=A_(N,0)(U), b1<=A_(N,1)(u0), y un control impar p1 con cocientes polares sucesivos<1, tales que

    min(b0+p_(N,0)(U),bU)>L_N,
    b1>L_N+p1.

Éste es un criterio suficiente para la fila INFINITA, no una afirmación de que las premisas valgan para todos N. La identidad exacta

    A_(N,1)=A_(N,0)+u ∂_u A_(N,0)

explica por qué empezar en k1 puede ser sustancialmente mejor que exigir ARCH0>0. Se deriva de las integrales beta y la recurrencia de resolventes, no de un ajuste numérico; para N fijo y u grande la ganancia tiende a1. No se usa ese límite como una cota uniforme en N.

El cierre de filaN5 amplía la tabla suficiente de signos. No cubre todas las filas ni nuevas ventanas T por sí solo; las regiones interiores de N crecientes mantienen su obligación de una desigualdad aritmética adicional.
