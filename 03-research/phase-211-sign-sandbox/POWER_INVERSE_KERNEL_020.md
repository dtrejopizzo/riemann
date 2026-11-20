# POWER_INVERSE_KERNEL_020 — Positividad del inverso COMPLETO fuera de un intervalo explícito

Estado: PROVED positividad del inverso completo en una región explícita para TODOS N; PROVED positividad global del inverso para N=2. Revisión independiente aprobada en POWER_BALANCE_AUDIT_020.md; root también verificó la prueba y el certificado. No se prueba el signo de ERR para todos N. Sin tablas numéricas. Papers intactos.

## Antecedentes y razón nueva, antes de la construcción

Leídos las reglas del proyecto, SIGNED_MEAN019 y auditoría, LOW_TABLE018, TATE_CHAIN009; búsquedas dirigidas en índice ROUTES-TRIED-INDEX, grid parte3 y CROSSWORD-TO-D (Möbius/kernel/inversión/positividad/polinomios). Las identidades de inversión y sus limitaciones Euler/Möbius ya están registradas y no se relanzan como prueba de signo.

La diferencia nueva es aprovechar coeficientes POSITIVOS de un polinomio específico del kernel gamma para dominar la COLA COMPLETA de Möbius en un rango de x que depende explícitamente de N. No se infiere el signo del inverso desde un prefijo. Se busca además un caso en el que el inverso completo sea positivo para todo x.

## 1. Teoremas sobre el inverso COMPLETO

Mantenga u=63/2 y los kernels de019,

    H_N(x)=−[x^-1/2 C_N(logx)]'/C_N(0)>0,
    h_N(x)=Σ(m>=1)mu(m)m H_N(mx), x>=1.

Para todo N>=2 se prueba

    H_N(x)/4 <=h_N(x)<=7H_N(x)/4
       si logx>=(N−1)/30.                              (OUTER)

La serie de h_N es la COMPLETA. Como consecuencia, toda su parte negativa está contenida en1<=x<exp((N−1)/30).

Además, para N=2, se prueba positividad en TODA la semirrecta:

    h_2(x)>=H_2(x)/[2zeta(32)]>H_2(x)/4>0, x>=1.       (ROW2)

OUTER no declara el signo de h_N en el complemento. ROW2 no se extrapola a otros N.

## 2. Polinomio gamma con todos sus coeficientes positivos

Escriba rho_N(t)=C_N(t)/C_N(0)=e^-ut P_N(t), t>=0. La integral gamma de la autocorrelación da

    P_N(t)=Σ(j=0..N−1)p_j t^j,
    p_j=binom(N−1,j)(2u)^j Gamma(2N−1−j)/Gamma(2N−1)>0.

Ponga d=N−1, s=u+1/2=32. Se tiene

    H_N(x)=x^-33 A_N(logx),
    A_N(t)=sP_N(t)−P_N'(t).

Para0<=j<d,

    (j+1)p_(j+1)/p_j=2u(N−1−j)/(2N−2−j)<=u.

Así cada coeficiente de A_N es >=(s−u)p_j=p_j/2>0; el último es sp_d>0. Su grado es exactamente d. Para N>=2, p_0=1,p_1=u, por lo que A_N(0)=1/2. La derivación no se basa en signos numéricos de un polinomio grande.

## 3. Dominación de TODA la suma de Möbius

Si A es un polinomio de grado d con coeficientes no negativos y t>0,l>=0,

    A(t+l)/A(t)<=(1+l/t)^d<=exp(dl/t).

Se aplica término a término a los monomios; no se supone monotonía de las derivadas de un inverso. La serie completa se escribe

    h_N(x)/H_N(x)
       =1+Σ(m>=2)mu(m)m^-32
                     A_N(logx+logm)/A_N(logx).

Para logx>=d/30, el cociente de polinomios es <=m^30. Como |mu(m)|<=1,

    |h_N(x)/H_N(x)−1|
       <=Σ(m>=2)m^-2
       <=1/4+∫_2^infinito t^-2dt=3/4.

Esto prueba OUTER y controla la cola COMPLETA antes de extraer el signo. No se utiliza el signo de ningún prefijo Möbius. Más generalmente, si q=32−d/logx>1, la misma prueba da

    |h_N/H_N−1|<=2^-q[1+2/(q−1)].                      (RANGE)

La elección q>=2 produce el umbral simple de OUTER.

## 4. Estructura global y caso N=2

Expandiendo el polinomio finito A_N dentro de la serie absolutamente convergente, h_N(x)=x^-33 tildeA_N(logx), donde tildeA_N es un polinomio de grado d. Su coeficiente principal es el de A_N dividido por zeta(32), estrictamente positivo, pues Σmu(m)m^-32=1/zeta(32). En particular h_N tiene a lo sumo d raíces positivas en la coordenada logx; OUTER además da una ubicación uniforme explícita de todas las posibles regiones negativas.

Para N=2, P_2(t)=1+ut y

    A_2(t)=1/2+1008t.

Con M(s)=1/zeta(s), D(s)=Σ(q>=2)Lambda(q)q^-s, se cumple M'=DM. Así la suma COMPLETA se evalúa exactamente:

    h_2(x)=x^-33/zeta(32)
                 [1/2+1008logx−1008D(32)].             (H2)

La cota elemental Lambda(q)<=q y comparación integral dan

    0<D(32)<=Σ(q>=2)q^-31
         <=2^-31(1+2/30),
    1008·2^-31(1+2/30)<1/4.

Por H2, h_2(x)>x^-33[1/4+1008logx]/zeta(32)>=H_2(x)/[2zeta(32)]. Finalmente zeta(32)<2, por la misma cota de series positivas. Queda probado ROW2 sin descartar términos de la suma.

La existencia de prefijos negativos para N grande en019 es compatible con ROW2 y OUTER: son afirmaciones de N y regiones distintos. No se ha probado aquí que h_N completo sea negativo en ningún punto.

## 5. Parte negativa localizada y cola favorable del emparejamiento

Sea X_N=exp((N−1)/30), y B(x) el agrupamiento negativo de019. Allí se probó B(x)<=−a0(x−1), a0=1−log2>0, y F_N=2∫h_N B. Por OUTER,

    F_N <=2∫_1^X_N h_N(x)B(x)dx
                −(a0/2)∫_X_N^infinito H_N(x)(x−1)dx.   (LOCAL)

La cola de LOCAL es favorable y explícita. Escribiendo w_N(x)=x^-1/2 C_N(logx), integración por partes da

    ∫_X^infinito H_N(x)(x−1)dx
       =[(X−1)w_N(X)+∫_X^infinito w_N(x)dx]/C_N(0).

Las integrales restantes son incompletas gamma de un polinomio por exponencial conocido, sin suma aritmética. El término adverso h_N^- emparejado con −B está rigurosamente restringido al intervalo finito[1,X_N]. Esto NO es aún una cota que lo compense: queda estimar unilateralmente ese emparejamiento interior.

## 6. Resultado y alcance

Se estableció signo del kernel inverso COMPLETO en una región infinita explícita para todos N, y en toda la semirrecta para N=2. No se deduce positividad de h_N en todo x para todos N, ni el signo de ERR de la fila completa. ROW2 aporta una propiedad del kernel; aun F_N<=0 no compensaría automáticamente el déficit de Arch_sharp. La contribución que falta está localizada por LOCAL y debe conservar su signo aritmético.
