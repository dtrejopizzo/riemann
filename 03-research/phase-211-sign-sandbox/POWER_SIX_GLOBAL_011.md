# POWER_SIX_GLOBAL_011 — Criterio general de transporte de déficit y signo global de seis polos

Estado: PROVED. Verificador íntegramente racional: tools/power_six_global_011_verify.py. Papers intactos.

## 1. Resultado

Para cualquier espacio racional de SEIS polos reales v_j>=63/2, con multiplicidades permitidas, la forma completa satisface

    W[f]>(1/25)||f||², f no nula.                          (SIX)

Se incluyen todas las mezclas de seis potencias exteriores con exponentes a_i>=32 y todos los límites confluentes. No hay separación mínima ni cota superior de los polos. El peine se controla completo, sin truncarlo.

La prueba aplica un criterio de transporte de déficit válido para cualquier dimensión declarada, con constantes que deben verificarse en cada caso. No afirma signo uniforme en dimensión arbitraria.

## 2. Antecedentes y diferencia

Consultados índice/grid/crucigrama y POWER_FOUR_GLOBAL_009, POWER_CONFLUENT_FOUR_005, POWER_HIGH_ORDER_PM_NOGO_007. No se vuelve a intentar monotonía arch+polar: se usa el transporte coercivo de 009 y se afina su control del sector negativo. La diferencia es obtener una regla cuantitativa explícita para n y verificarla a n=6; el coeficiente .12 del caso confluente se certifica por restos racionales, no se presupone desde el diagnóstico. No hay un barrido de tasas.

## 3. Criterio general de transporte del déficit

Fije u>1/2 y dimensión n. Suponga en el espacio confluente de n polos u:

    AP[f0]>=b||f0||², |Polar[f0]|<=p||f0||².

Suponga además constantes c, X>0 y D>=0 tales que

    m(tau)>=c para tau²>=X,
    tau²(c-m(tau))_+<=D.

Defina

    K_n=[(1+X/u²)^n-1]/X,
    eta_n=1-(1-1/(4u²))^n <=n/(4u²).

Si

    b-c-D K_n-p eta_n>0,                                 (CRIT)

entonces AP[f]>=c||f||² para TODOS los espacios de n polos reales v_j>=u.

Prueba. Para el mismo numerador racional use F0=P/(s+u)^n y F=H F0 con H=Π_j(s+u)/(s+v_j). Escriba R=|H(i tau)|², R0=R(0), r0=H(-1/2)H(1/2). Entonces

    1<=R/R0<=(1+tau²/u²)^n,
    1>=r0/R0>=(1-1/(4u²))^n.

La identidad exacta es

    AP[f]-c||f||²
     =R0(AP[f0]-c||f0||²)
      +∫(R-R0)(m-c)|F0|²/(2pi)
      +(r0-R0)Polar[f0].

La primera corrección sólo puede perjudicar en tau²<=X. Por convexidad, allí R-R0<=R0 K_n tau², de modo que cuesta a lo sumo R0 D K_n||f0||². La variación polar cuesta a lo sumo R0 p eta_n||f0||². (CRIT) demuestra la afirmación, conservando la norma OBJETIVO de f en la identidad. No se divide incorrectamente por R0 ni se necesita comparar R0 con la norma final.

## 4. Mejora general del control ponderado por filtros all-pass

Esta observación del constructor principal mejora la estimación Young anterior. Para 0<alpha<1, sigma=alpha u, sea

    r=(1+alpha)/(1-alpha),
    B_n(alpha)=[1/(1-alpha)]Σ_{j=0}^{n-1}r^{2j}.

En todo espacio de n polos >=u,

    ||exp(sigma y)f||²<=B_n(alpha)||f||².                  (WT)

Prueba. En la base racional ortonormal, cada factor all-pass es (s-v)/(s+v). Tras ponderar por exp(sigma y), Plancherel lo evalúa en s=-sigma+i tau, y su norma de multiplicador es

    sup_tau |(i tau-sigma-v)/(i tau-sigma+v)|
       =(v+sigma)/(v-sigma)<=(1+alpha)/(1-alpha).

La exponencial inicial normalizada tiene norma ponderada al cuadrado v/(v-sigma)<=1/(1-alpha). Se multiplican las cotas para cada miembro de la base y se aplica Cauchy--Schwarz a los coeficientes ortonormales. Esto prueba (WT) incluso con tasas repetidas.

En consecuencia

    |Comb[f]|<=2sqrt(B_n(alpha))
          *Σ_{q>=2}Lambda(q)q^{-(sigma+1/2)} ||f||².        (PC)

Así (CRIT) y cualquier cota de (PC) menor que c producen el signo completo en todo el dominio de tasas. La mejora r sustituye el factor mayor obtenido sumando las normas L1 del delta y la exponencial: aquí se conserva exactamente el multiplicador del filtro.

## 5. Certificado confluente n=6, u=63/2

El verificador obtiene por intervalos racionales las seis bandas de la matriz Toeplitz arch+polar. Use

    g(s)=[psi((s+1/2)/2)-log pi]/2, r0=32/31.

La diagonal es 2g(u)+4u/(u²-1/4), y las bandas k=1,...,5 son

    Σ_{j=1}^k g^(j)(u)(2u)^j binom(k-1,j-1)/j!
       +[2u/(u²-1/4)](-1)^k(r0^k+r0^-k).

Las derivadas de psi en 16 se calculan como

    psi^(j)(16)=(-1)^{j+1}j!Σ_{m>=16}m^{-j-1}.

Se suman m<=2000 y se encierra la cola entre las integrales desde 2001 y desde 2000. Gamma, pi y los logaritmos usan los intervalos racionales de power_fixed_grid_003, con series y restos explícitos ya auditados. La eliminación LDL INTERVALAR de AP-(3/25)I tiene seis pivotes con extremo inferior positivo. Queda certificado

    AP[f0]>(3/25)||f0||².                                 (BASE6)

Los momentos polares satisfacen, exactamente,

    AA=(63/31²)Σ_{j=0}^5(32/31)^{2j},
    BB=(63/32²)Σ_{j=0}^5(31/32)^{2j}, 4AA BB<1.

Por tanto se puede usar p=1.

## 6. Sector negativo con constante pequeña

Los intervalos racionales de las constantes prueban m(0)>-5373/1000. Con los mismos dieciséis términos de digamma,

    ell(x)=-5373/1000+Σ_{k=0}^{15}x/[a_k(4a_k²+x)], a_k=k+1/4,

se tiene m(tau)>ell(tau²), y ell es creciente. El verificador comprueba

    ell(49)>1/20,
    x(1/20-m(tau))_+<9, x=tau².

Para la segunda desigualdad sólo se necesitan los 25 paneles de extremos

    0,1/4,1,2,3,4,6,8,10,12,13,14,15,16,17,18,19,20,21,22,23,24,28,32,40,49.

En cada panel [a,b], se compara b*(1/20-ell(a))_+ con 9 mediante Fraction. Para x>=49 el multiplicador ya supera 1/20. Son desigualdades escalares exactas del único multiplicador; no son certificados muestreados de tasas.

Con b=3/25, c=1/20, D=9, X=49, n=6, p=1, el verificador comprueba

    3/25-1/20-9[(1+49/u²)^6-1]/49-6/(4u²)>3/500>0.

El criterio general da AP[f]>(1/20)||f||² para TODAS las seis tasas >=u.

## 7. Peine y cierre del caso seis

En (WT) elija alpha=3/4. Entonces sigma=189/8, r=7, y

    B6=4Σ_{j=0}^5 49^j=(49^6-1)/12=1153440600,
    2sqrt(B6)<68000, sigma+1/2>24.

Como Lambda(q)<=logq y (logx)x^-24 decrece para x>=2,

    Σ_{q>=2}(logq)q^-24
      <=2^-24[log2+2log2/23+2/23²].

Usando log2<7/10, la cota multiplicada por 68000 es menor que 1/250. Por (PC),

    |Comb[f]|<(1/250)||f||².

Finalmente W[f]>(1/20-1/250)||f||²=(23/500)||f||²>(1/25)||f||². Queda probado (SIX).

Comando reproducible: `python3 03-research/phase-211-sign-sandbox/tools/power_six_global_011_verify.py`. No utiliza coma flotante, optimizadores ni funciones especiales numéricas. Verifica BASE6, la norma polar, los 25 paneles, el margen del filtro y la cola infinita del peine.

## 8. Límite de la regla

El criterio es un teorema general condicional a b,p,D,X y a su desigualdad explícita; no asegura que esas constantes existan con margen para todos n. El test de orden doce con AP negativa impide reutilizar directamente una base AP positiva allí. La mejora ponderada ayuda a conservar la aritmética como pérdida cuando eso es legítimo, pero no reemplaza la compensación positiva del peine cuando resulta necesaria.
