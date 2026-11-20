# POWER_SIGNED_TRANSFER_014 — Conservar la ganancia firmada mediante un cero de numerador; signo global de ocho polos

Estado: PROVED, con certificados racionales pequeños. Verificador: tools/power_signed_transfer_014_verify.py. Papers intactos.

## 1. Resultado

En TODO espacio racional de ocho polos reales v_j>=63/2, con multiplicidades permitidas, la forma completa satisface

    W[f]>(1/1000)||f||², f real no nula.                   (EIGHT)

Equivale aquí a positividad para cualquier mezcla de ocho potencias exteriores de exponentes >=32, sin separación mínima ni cota superior, y para sus límites confluentes. No se afirma signo en todos los órdenes.

## 2. Corpus y diferencia con el límite de 013

Consultados índice/grid/crucigrama buscando numeradores cero, constrained arch, telescoping filters y signed transfer; leídos POWER_POLE_MOVEMENT_004, POWER_DEFICIT_LIMIT_013 y POWER_COMMON_TRANSFER_010. Las identidades de filtros son conocidas; no se les atribuye signo automático. La diferencia nueva es la DESCOMPOSICIÓN de toda la corrección espectral firmada en energías de funciones racionales que tienen un CERO FORZADO DE NUMERADOR en s=0. La parte arquimediana es coerciva sobre ese subespacio concreto, aunque su multiplicador sea negativo cerca del origen.

No se optimiza la pérdida puntual excluida por 013. Se conserva la integral con ambos signos y se usa la restricción real de su densidad espectral; ésa es precisamente información que el NO-GO anterior descartaba.

## 3. Identidad positiva de la diferencia de filtros

Fije u>1/2 y dimensión n. Sean v_j>=u, P un polinomio real de grado menor que n, y

    F0(s)=P(s)/(s+u)^n,
    F(s)=P(s)/Π_j(s+v_j)=H(s)F0(s).

Con x=tau², defina R=|H(i tau)|², R0=Π_j u²/v_j² y

    A_j(x)=(1+x/u²)/(1+x/v_j²), R/R0=Π_j A_j.

Telescopar Π_j A_j-1=Σ_j(A_j-1)Π_{k<j}A_k y conservar la densidad racional da EXACTAMENTE

    (R-R0)|F0(i tau)|²
      =R0 Σ_{j=1}^n kappa_j |G_j(i tau)|²,                (TEL)

donde

    kappa_j=[(v_j²-u²)/u²]Π_{k<j}(v_k²/u²)>=0,
    G_j(s)=sP(s)/[(s+u)^{n-j+1}Π_{k<=j}(s+v_k)].

Cada G_j tiene n+1 polos reales >=u, numerador de grado <=n y numerador CERO en s=0. Aquí G_j(0)=0 es la evaluación de la TRANSFORMADA DE LAPLACE, equivalente a integral temporal cero; no significa que la función temporal se anule en y=0. La verificación de (TEL) es multiplicar denominadores: A_j-1=x(v_j²-u²)/[u²(x+v_j²)]. No se aproxima ningún filtro ni se toma un supremo puntual.

## 4. Nueva desigualdad operatorial: coercividad arquimediana sobre el numerador cero

Suponga que, en el espacio confluente de n+1 polos u restringido a Q(0)=0, se ha probado

    Arch[g]>=gamma||g||².                                (CZ)

La monotonía arquimediana de POWER_POLE_MOVEMENT_004 se aplica sobre ese MISMO espacio de numeradores Q de grado <n+1 y Q(0)=0: mover polos sólo repondera por una función creciente de |tau| y no altera la restricción Q(0)=0. Por tanto (CZ) vale para todos los n+1 polos >=u y, en particular, para cada G_j de (TEL).

Para cualquier c<=gamma, integrar (TEL) contra m-c prueba la desigualdad NUEVA

    ∫(R-R0)(m-c)|F0|²/(2pi)
      =R0 Σ_j kappa_j(Arch[G_j]-c||G_j||²)
      >=R0(gamma-c)Σ_j kappa_j||G_j||²>=0.                (SIGNED)

La frecuencia negativa no se elimina: su coste queda dentro de una energía arquimediana de promedio positivo por la estructura racional y el cero de numerador. (SIGNED) es una desigualdad sobre los filtros exactos, no el cambio de nombre de una identidad sin signo.

## 5. Criterio general firmado con polar

Suponga además en el espacio confluente de n polos u

    AP[f0]>=b||f0||², |Polar[f0]|<=p||f0||².

Defina eta_n=1-(1-1/(4u²))^n<=n/(4u²). Como antes, r0=H(-1/2)H(1/2) satisface R0>=r0>=R0(1-eta_n). Usando la identidad exacta de transporte y (SIGNED),

    AP[f]-c||f||²
       >=R0[(b-c-p eta_n)||f0||²
             +(gamma-c)Σ_j kappa_j||G_j||²].              (GAIN)

Así, si gamma>=c y b-c-p eta_n>0, se obtiene AP[f]>=c||f||² para TODOS los espacios de n polos >=u. Esta regla conserva la ganancia espectral positiva y el cambio polar en una misma desigualdad. No presupone monotonía de AP bajo movimientos individuales, que no vale en dimensión arbitraria.

## 6. Certificados concretos n=8, u=63/2

El verificador calcula mediante intervalos racionales las nueve bandas arquimedianas confluentes necesarias y las bandas polares exactas. Para g(s)=[psi((s+1/2)/2)-log pi]/2, la diagonal arquimediana es 2g(u), y la banda k>=1 es

    Σ_{j=1}^k g^(j)(u)(2u)^j binom(k-1,j-1)/j!.

La banda polar k es [2u/(u²-1/4)](-1)^k[(32/31)^k+(31/32)^k]. Las derivadas de psi en 16 se calculan con sumas racionales hasta 2000 y colas integrales; gamma, pi y logaritmos usan los intervalos ya auditados de fixed_grid_003. No se utilizan funciones especiales numéricas.

### Base completa de ocho polos

El LDL intervalar de AP8-(7/200)I tiene ocho pivotes con extremo inferior positivo. Por tanto b=7/200 es válido. Los vectores polares tienen normas al cuadrado

    AA=(63/31²)Σ_{j=0}^7(32/31)^{2j},
    BB=(63/32²)Σ_{j=0}^7(31/32)^{2j}.

La desigualdad racional 4AA BB<(3/2)² permite tomar p=3/2.

### Bloque arquimediano restringido de nueve polos

En la base Laguerre ortonormal, F_j(0)=sqrt(2/u)(-1)^j. Por ello Q(0)=0 equivale a Σ_{j=0}^8(-1)^j x_j=0. Una base racional de ese subespacio es

    B_i=e_i-(-1)^i e_8, i=0,...,7.

Su Gram es I+aa^t con a_i=(-1)^i. La eliminación LDL intervalar de

    B^t Arch9 B-(1/4)B^t B

tiene ocho pivotes con extremo inferior positivo. Así (CZ) vale con gamma=1/4. Es una desigualdad de forma en TODO el subespacio, no la evaluación de un vector particular.

### Margen firmado uniforme

Tome c=3/100. Las constantes racionales cumplen

    gamma>c,
    7/200-3/100-(3/2)*8/3969>1/1000>0.

Por (GAIN), AP[f]>(3/100)||f||² para TODOS los ocho polos >=63/2.

## 7. Peine infinito usando la traza ponderada exacta

POWER_COMMON_TRANSFER_010 §6 demuestra, con revisión independiente, que la traza ponderada es máxima en la confluencia. Para 0<alpha<1, sigma=alpha u, se puede usar uniformemente

    ||exp(sigma y)f||²<=T_n(alpha)||f||²,
    T_n(alpha)=Σ_{j=0}^{n-1}
       [Σ_{k=0}^j binom(j,k)^2 alpha^{2k}]/(1-alpha)^{2j+1}.

Con n=8, alpha=3/5, sigma=189/10 y beta=sigma+1/2=97/5, el verificador racional prueba 4T8<25000². Por tanto

    |Comb[f]|/||f||²<=25000Σ_{q>=2}(logq)q^-beta.

La comparación integral de la función decreciente (logx)x^-beta da

    Σ_{q>=2}(logq)q^-beta
       <=2^-beta[log2+2log2/(beta-1)+2/(beta-1)²].

Use beta-1>18, log2<7/10 y 2^-2/5<19/25, cuya última prueba es la desigualdad entera 25^5<4*19^5. Resulta la cota racional

    |Comb[f]|/||f||²
       <25000*(19/25)*2^-19[7/10+14/180+2/324]
       <29/1000.

La suma incluye TODAS las potencias primas; no se han supuesto signos favorables ni descartado una cola sin estimar. Finalmente

    W[f]>(3/100-29/1000)||f||²=(1/1000)||f||².

Esto prueba (EIGHT).

## 8. Alcance y próximo nodo

La regla general depende de dos bloques distintos: AP confluente de orden n y Arch confluente de orden n+1 restringido a numerador cero. Ambos se verificaron íntegramente para n=8. No se afirma que sus márgenes persistan a todo orden: el test de dimensión doce con AP negativa sigue vigente y obliga eventualmente a conservar aritmética favorable. El resultado supera el obstáculo puntual de 013 mediante una desigualdad acoplada concreta, sin contradecirlo.

Comando reproducible: `python3 03-research/phase-211-sign-sandbox/tools/power_signed_transfer_014_verify.py`. Usa sólo enteros y Fraction; verifica los dos bloques por LDL intervalar, la norma polar, el margen firmado y el coste infinito del peine.

## 9. Identidad exacta para la forma COMPLETA: el polar también se incorpora en los sumandos

La identidad racional (TEL) tiene una extensión algebraica adicional, independiente del certificado de orden ocho. Para numeradores reales, reemplace |F(i tau)|² por F(s)F(-s) y x=tau² por -s². Como todos los polos son mayores que 1/2, se puede evaluar en s=1/2 sin singularidades. Resulta

    Σ_j kappa_j Polar[G_j]=(r0/R0-1)Polar[f0].              (POLTEL)

En efecto el factor s del numerador de G_j produce s*(-s)=-1/4, exactamente el signo del miembro polar de (TEL) en x=-1/4. No se trata de una evaluación puntual de una medida espectral positiva: es una identidad entre funciones racionales.

Integrar (TEL) contra m y contra cada cos(tau logq) conserva la parte arquimediana y cada átomo primo. Las sumas de los átomos convergen absolutamente para estos datos racionales con polos >1/2, pues cada autocorrelación es un polinomio finito por una exponencial. Al añadir (POLTEL), se obtiene

    W[f]-c||f||²
       =R0[(W[f0]-c||f0||²)
              +Σ_j kappa_j(W[G_j]-c||G_j||²)].             (FULL)

También ||f||²=R0[||f0||²+Σ_j kappa_j||G_j||²], por (TEL) integrado contra uno. (FULL) no tiene una pérdida polar: la conserva exactamente dentro de las formas W[G_j], junto con toda la aritmética.

Por tanto un criterio completo es: si la base confluente de orden n y TODOS los espacios de n+1 polos >=u restringidos a transformada de Laplace cero en s=0 tienen W>=c||.||², entonces lo mismo vale para todos los espacios de n polos >=u. No se ha probado aquí la segunda premisa a todo orden. Su enunciado conserva Λ y las autocorrelaciones con ambos signos, a diferencia de un argumento que use sólo la positividad de los coeficientes aritméticos.

Para un único polo cambiado, con rho=u²/v², (FULL) se simplifica a

    W[f_v]=rho W[f_u]+(1-rho)W[sF_u(s)/(s+v)].             (ONE)

Esta identidad de un polo coincide con la derivación independiente del análisis por casos. Su iteración, la normalización de la mezcla y la convergencia fuerte se desarrollan en POWER_GEOMETRIC_TRANSFER_015; la positividad eventual de los bloques high-pass se trata por separado en POWER_HIGHPASS_015.
