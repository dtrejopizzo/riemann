# POWER_FOUR_GLOBAL_AUDIT_009 — Revisión del transporte de déficit y cierre de cuatro polos arbitrarios

Estado: PROVED. Verificador tools/power_four_global_009_verify.py ejecutado con PASS. Se revisa el teorema de cuatro polos, no el signo de todos los órdenes. Papers intactos.

## 1. Identificación exacta de funciones y términos

Fije u=63/2, D0(s)=(s+u)^4. Para polos reales v_j>=u y cualquier polinomio real P de grado<4, compare fhat0=P(i tau)/D0(i tau) con fhatv=P(i tau)/prod(v_j+i tau). Son espacios de numeradores idénticos; los repetidos se admiten desde el principio. Defina

    R=prod_j(u²+tau²)/(v_j²+tau²),
    R0=prod_j u²/v_j²,
    r0=prod_j(u²-1/4)/(v_j²-1/4).

Si N0=||f0||² y Pv0=2A(f0)B(f0), entonces Nv=integral R|fhat0|²/(2pi) y el polar nuevo es r0 Pv0. Para cualquier c real,

    APv-cNv =R0(AP0-cN0)
       +integral (R-R0)(m-c)|fhat0|²/(2pi)
       +(r0-R0)Pv0.                                   (ID)

La identidad conserva todas las normalizaciones. No afirma que APv/Nv sea mayor que AP0/N0; es transporte de una desigualdad de déficit y no contradice los falsificadores de monotonía.

## 2. Filtros espectrales y polar

Cada factor satisface R>=R0 y

    R/R0<= (1+tau²/u²)^4,
    r0/R0=prod_j (1-1/(4u²))/(1-1/(4v_j²))
            >=(1-1/(4u²))^4>=1-1/u².

También r0<=R0. Los signos de cada comparación se verifican directamente de v_j>=u>1/2. La norma del polar en la base confluente se controla mediante los dos vectores de momentos: si AA=||A||²,BB=||B||², |2A(f)B(f)|<=2sqrt(AA BB)||f||². El script certifica 4AA BB<1 exactamente, con sus dos progresiones racionales, por lo que |Pv0|<N0. Así el último término de ID es mayor que -R0 N0/u² independientemente del signo del polar.

## 3. Auditoría de las cinco comparaciones escalares

Se ejecutó el código y se verificaron las constantes desde sus series:

* Tres términos de la serie atanh para log2 dan log2>693/1000. Luego gamma<H32-log32<H32-5(693/1000)<3/5.
* El primer término2/3 y el resto geométrico acotado por1/36 dan log2<25/36<7/10.
* La suma positiva hasta grado6 de exp(23/20) supera22/7; junto con pi<22/7 da logpi<23/20. Por tanto gamma+pi/2+3log2+logpi<11/2, y m(0)>-11/2.

Con x=tau², los dieciséis primeros sumandos positivos de digamma producen el lower(x) del script. Su fórmula x/[a(4a²+x)] tiene el factor4 correcto. Las cinco cotas inferiores en4,16,32,64,81 son racionales y sus asserts pasan. Como m crece en x, los paneles [0,4],[4,16],[16,32],[32,64],[64,81] certifican

    x(1/10-m(sqrt(x)))_+ <23.

El último sitio81 tiene m>.1, por lo que la parte negativa se anula para x>=81. No se usa un barrido numérico ni se interpola sin monotonía.

Para 0<=x<=81, el cociente [(1+x/u²)^4-1]/x es creciente por su expansión polinómica positiva. Así

    0<=R-R0<=R0 Kx,
    K=[(1+81/u²)^4-1]/81.

La pérdida integral de ID queda mayor que -23KR0 N0.

## 4. Margen final completo, incluyendo todos los contactos

El certificado confluente previamente auditado da AP0>(49/200)N0. Insertar c1/10 en ID y usar §§2–3 deja

    APv-(1/10)Nv
       >R0[49/200-1/10-23K-1/u²]N0.

El corchete es exactamente3669270349/93389776200>3/100. Por tanto APv>(1/10)Nv para TODO numerador y TODO cuádruple de tasas>=u, sin separación ni cota superior. Esta comparación utiliza una cota absoluta de déficit limitada a bajas frecuencias, no la monotonía del cociente AP.

La cota uniforme de Young/all-pass B4=32552 ya auditada vale para esos polos arbitrarios y da |Comb|<(13/1000)Nv. La suma de todos los contactos converge absolutamente para estas funciones racionales. En consecuencia

    W[fv]>(1/10-13/1000)Nv>(2/25)Nv.

Esto prueba positividad con margen uniforme en TODOS los espacios de cuatro polos reales>=63/2, incluidos polos repetidos y los correspondientes polinomios por exponenciales. Las mezclas de hasta cuatro potencias con exponentes>=32 son subcasos mediante la identificación diagonal con zeta(a). No se infiere el resultado para cinco polos ni para cualquier dimensión.

Se recibió y leyó después el memo final completo POWER_FOUR_GLOBAL_009.md: APROBADO íntegramente. La suma explícita759/140 y las cinco cotas112/5,344/15,112/5,112/5,81/50 coinciden con las comparaciones del verificador. El factor R0 pequeño está correctamente tratado porque la norma objetivo Nv figura ya en ID. No se encontró una restricción oculta de separación, acotación superior de tasas o positividad individual del peine.
