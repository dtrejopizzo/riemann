# POWER_CONFLUENT_FOUR_005 — Cuatro polos confluentes: polar rescata el signo

Estado: PROVED certificado exacto; revisado independientemente. No prueba cuatro tasas arbitrarias. Papers intactos.

Antecedentes: POWER_CONFLUENT_004, POWER_POLYNOMIAL_003, movimiento de polos y control ponderado de `signo`/POWER_AUDIT_004. Razón nueva: en dimensión cuatro falla la positividad arquimediana aislada; se conserva explícitamente la matriz polar antes de comparar. No se extrapola la prueba de dimensión tres ignorando ese cambio de signo.

## 1. Matrices exactas

Fije u=63/2 y phi_j(y)=sqrt(63)e^-uy L_j(63y), 0≤j≤3, base Laguerre ortonormal. La matriz arquimediana es Toeplitz con primera fila (d,b,c,e), donde

    d=psi(16)−log pi,
    b=(63/4)psi'(16),
    c=b+(3969/16)psi''(16),
    e=b+(3969/8)psi''(16)+(250047/96)psi'''(16).

La fórmula general del cuarto coeficiente es 2up'+4u²p''+(4/3)u³p''', con p=[psi((u+.5)/2)−log pi]/2. Se deriva diferenciando el mismo kernel [p(u)+p(v)]/(u+v) y conjugando por Laguerre.

Los momentos polares exactos son

    A_j=sqrt(63)(−32)^j/31^(j+1),
    B_j=sqrt(63)(−31)^j/32^(j+1),
    Polar_jk=A_j B_k+B_j A_k.

Así toda la matriz polar es racional, sin raíces tras multiplicar los momentos.

## 2. Intervalos racionales

Use J,E y H definidos en POWER_CONFLUENT_004, todos con 24 términos. Las cotas 223/71<pi<22/7, H256−log256−1/256<gamma<H256−log256 dan

    dlo=H15−H256+8J(1/3)−J(15/29)−E(15/29),
    dhi=H15−H256+8[J(1/3)+E(1/3)]+1/256−J(76/147).

Para r=2,3,4 defina

    Sr=Σ(k=16..255)k^-r,
    lo_r=Sr+1/[(r−1)256^(r−1)],
    hi_r=Sr+1/[(r−1)255^(r−1)].

Entonces b está entre (u/2)lo_2 y (u/2)hi_2; c entre blo−(u²/2)hi_3 y bhi−(u²/2)lo_3; e entre blo−u²hi_3+(u³/2)lo_4 y bhi−u²lo_3+(u³/2)hi_4. Son intervalos racionales exactos.

Tome el centro racional r=(1596/1000,1016/1000,−16/1000,349/1000) y T(r) la Toeplitz de orden cuatro. Aplicar los intervalos anteriores prueba que el error entre la matriz arquimediana verdadera y T(r) tiene máxima suma absoluta de fila menor que 1/200. Por simetría su norma es menor que 1/200.

El LDL exacto de T(r)+Polar−(1/4)I tiene cuatro pivotes positivos; el verificador adjunto lo comprueba exclusivamente con Fraction. Alternativamente, la polar también es Toeplitz: si (a,b0,c0,e0) es la primera fila de T(r)+Polar, la congruencia racional por los vectores (1,0,0,1),(0,1,1,0),(1,0,0,−1),(0,1,−1,0) separa los dos bloques

    [[a+e0−1/4,b0+c0],[b0+c0,a+b0−1/4]],
    [[a−e0−1/4,b0−c0],[b0−c0,a−b0−1/4]].

Ambos tienen primer pivote y determinante racionales positivos, comprobados también en el verificador. Por tanto

    Arch+Polar > (1/4−1/200)I = (49/200)I.                  (AP4)

## 3. Control del peine y resultado completo

El control ponderado de cuatro polos previamente auditado da ∫e^(uy)|h(y)|²dy≤32552||h||² para esta confluencia. Por Cauchy–Schwarz, |c_h(log n)|≤sqrt(32552)n^(-u/2)||h||². Usando Lambda(n)≤n, 2sqrt(32552)<362, (u−1)/2>15, y comparación integral,

    |Comb|≤362 Σ(n>=2)n^-15 ||h||²
           ≤362[2^-15+2^-14/14]||h||²
           =362/28672 ||h||² <(13/1000)||h||².

Junto a AP4 resulta

    W[h] > (49/200−13/1000)||h||² > (1/5)||h||².

Este teorema vale sobre span{e^-31.5y,ye^-31.5y,y²e^-31.5y,y³e^-31.5y}. Por continuidad en una base de diferencias divididas persiste en alguna vecindad de tasas confluentes; aquí no se obtiene un radio explícito. No prueba positividad de todos los cuádruples a>=32: la monotonía usada para ARCH no incluye automáticamente el término polar.

## 4. Falsificador exacto de ARCH positivo en orden cuatro

Para el vector Laguerre v=(1,−1,1,−1),

    Arch[v]/||v||² = d−(3/2)b+c−(1/2)e <−1/10,

por los mismos intervalos racionales. Así el método «ARCH positiva para cualquier cantidad de polos con tasas >=31.5 y resto pequeño» queda refutado ya en dimensión cuatro. No es negatividad de la forma completa: AP4 muestra explícitamente la compensación polar.
