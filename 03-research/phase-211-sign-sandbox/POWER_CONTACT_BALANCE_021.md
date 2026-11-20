# POWER_CONTACT_BALANCE_021 — Escala de cancelación en un único átomo k1

Estado: **PROVED** balance negativo usando sólo contactos2,3,4 y bound positivo de TODA la cola q>300. **NUMÉRICO** balance hasta300 con ARCH por cuadratura. No se decide el signo de W. Papers intactos; auditoría020 no modificada.

## 1. Objeto y autorización limitada

Se continúa FAIL2 de SIGNED_BALANCE020 en UN solo átomo, F(s)=s/(s+63/2)^212, N211,k1. Leídos STATE019, ARITHMETIC_DIFFERENCES019, SIGNED_BALANCE020 y su revisión; antecedentes de índice/grid/crucigrama son los declarados en020. La diferencia es medir pocos contactos reparadores, comprobar la escala residual y acotar analíticamente su cola, no lanzar una campaña en N ni optimizar filas fijas. Por019 TODOS los contactos son favorables, pero su magnitud conjunta es la obligación.

Todas las energías abajo están divididas por norm². ARCH, POLAR y P_q conservan la normalización020. Los q compuestos que no son potencias primas aportan0.

## 2. Resultado exacto con tres contactos

La cota U020 prueba ARCH<−.74. El polar exacto satisface POLAR<−.36. Para cada potencia prima q=p^a,

    P_q=2log(p) q^(−32) K_N r_N((63/2)log q),
    K_N=N2^(N−1)/[N!binom(2N−2,N−1)].

Esto incluye tanto q3 como q4, sin aproximar Λ ni olvidar las potencias. La evaluación racional por Horner prueba

    0<P_2+P_3+P_4<.89,
    ARCH+POLAR+P_2+P_3+P_4<−.21.                             (FAIL234)

Por tanto ignorar la magnitud de TODOS los contactos restantes no certifica este átomo. FAIL234 no es el valor de W: los contactos q>=5 siguen presentes y positivos.

## 3. Diagnóstico NUMÉRICO de escala, no certificado de signo

Una sola evaluación del átomo, mpmath a45 y65 dígitos; en65 dígitos:

    ARCH = −1.0941773847418061369452382637632905
    POLAR= −0.36603632954956029193069220397307442

La integral usa t=tau/u y la probabilidad beta exacta

    (2/B(3/2,N−1/2)) t²(1+t²)^(−N−1)dt, t>0,

contra m(ut). Se divide la cuadratura en0,.025,.05,.1,.2,.4,1,infinito. Las potencias primas hasta300 se evalúan por la fórmula polinomial anterior. No hay barrido de otros parámetros.

| Último contacto incluido | ARCH+POLAR+sum P_q, NUMÉRICO |
|---|---:|
|2|−1.3854051001619002770|
|4|−.57144083561183200587|
|5|−.22565929156781364596|
|13|−.0046372288392951004140|
|31|−.000029369239646495296493|
|97|−.0000000062920938255926665143|
|293 (todos q<=300)|−6.0812131368147274153·10^(−14)|

Los cálculos45/65 coinciden en los dígitos mostrados relevantes para la escala, pero no hay certificado de error de cuadratura. No se afirma que la suma COMPLETA sea negativa ni cero, ni se infiere signo de la diferencia de cantidades casi iguales. Se detiene aquí la enumeración: no se fuerza una verificación500/1000 ni una precisión masiva para perseguir un margen.

## 4. Bound analítico de la cola COMPLETA, sin enumeración adicional

Escriba r_N(x)=sum_j r_j x^j con coeficientes racionales conocidos. Usando Λ(q)<=log q,

    0<sum_(q>300)P_q
      <=2K_N sum_(j=0)^N |r_j|u^j sum_(q>300)q^(−32)(log q)^(j+1).

Para ell>=1, f_ell(x)=x^(−32)(log x)^ell es no negativa y unimodal en[300,infinito). Comparación de paneles en las dos ramas da

    sum_(q>300)f_ell(q)<=int_300^infty f_ell(x)dx+sup_(x>=300)f_ell(x).

Además (log f_ell)'=−32/x+ell/(x log x)>=−32/300. Si x0 es un máximo, integrar la cota f_ell(x0+t)>=f_ell(x0)e^(−32t/300) prueba sup f_ell<=(32/300)int f_ell. Por tanto la suma anterior es <=(83/75)I_ell, donde

    I_0=1/(31·300^31),
    I_ell=300^(−31)(log300)^ell/31+(ell/31)I_(ell−1).

La recurrencia usa sólo sumandos positivos. Sustituir la cota racional superior de log300, sumar coeficientes absolutos y operar con Fraction prueba

    0<sum_(q>300)P_q<5·10^(−13).                             (TAIL)

El bound intermedio es aproximadamente4.47·10^(−13); sólo la desigualdad racional TAIL se usa como teorema. Es una cota del peine, independiente del cálculo numérico de ARCH. No convierte la tabla NUMÉRICA de§3 en un intervalo certificado para W.

## 5. Resultado y paso que queda

FAIL234 y TAIL son pruebas exactas. El diagnóstico localiza una cancelación de componentes de orden1 hasta una escala de al menos10^(−13) en esta suma parcial. La cola favorable todavía importa en esa escala. El intento no obtiene W>0 ni W<0 y no elimina ninguna región admisible.

La información útil para la siguiente construcción es que el signo favorable del peine requiere conservar su cancelación conjunta con ARCH y POLAR. Separar esas componentes mediante cotas gruesas deja de resolver el balance. Esto describe el alcance de estos bounds en este átomo; no constituye un NO-GO para otras desigualdades aritméticas o para todos los peines finitos.

Reproducción:

    python3 03-research/phase-211-sign-sandbox/tools/power_contact_balance_021_verify.py
    python3 03-research/phase-211-sign-sandbox/tools/power_contact_balance_021_diagnostic.py 65

El primer script es Fraction/intervalos exactos y PASS. El segundo es explícitamente NUMÉRICO, depende de mpmath y no certifica error de cuadratura.


## Seguimiento032: candidato decidido

POWER_CONTACT_DECISION_032 y POWER_CONTACT_AUDIT_032 resuelven este mismo átomo mediante ARCH sin cuadratura y contactos hasta512 con cola completa: 3.4e−15<W/norma²<4.5e−15. El parcial negativo hasta300 de esta nota no era W total; la diferencia procede de contactos favorables omitidos, no de un signo global negativo previamente probado. Se conserva esta nota como registro histórico de021.
