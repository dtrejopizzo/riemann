# POWER_CONTACT_DECISION_032 — Decisión del único átomo211,1

Estado: **PROVED y auditado en POWER_CONTACT_AUDIT_032.md**. Para el ÚNICO átomo

    F(s)=s/(s+63/2)^212, N211,k1,u63/2,
    3.4·10^(-15) < W[f]/||f||² < 4.5·10^(-15).             (DECISION)

El candidato no es un contraejemplo. No se afirma una fila, vecindario ni resultado uniforme. Papers intactos.

## 1. Antecedentes y razón precisa

Consultados ROUTES-TRIED-INDEX, grid maestro y CROSSWORD-TO-D sobre cancelación firmada, contactos, sumación y primitivas; leídos ARITHMETIC_DIFFERENCES019, SIGNED_BALANCE020 y CONTACT_BALANCE021. Este último dejó el mismo átomo sin decidir: parcial hasta300 aproximadamente−6.08e−14 y cola positiva acotada por5e−13. Su texto no afirmaba W negativo.

La diferencia032 es reemplazar la cuadratura arquimediana por una fórmula finita en valores Hurwitz con resto racional de Euler–Maclaurin y decidir ESE candidato, conservando todos los contactos. No es una campaña en N ni una búsqueda de cortes óptimos. La evaluación preliminar única a55 dígitos usa ARCH exacta y un corte512; su objeto es verificar viabilidad de un certificado pequeño. La prueba final no depende de números flotantes ni de cuadratura.

La corrección de ARCH frente a la cuadratura021 es de aproximadamente2.66e−28; por tanto NO explica el parcial negativo de orden1e−14. El cambio de signo lo producen contactos omitidos en aquella suma parcial. Se justifica extender el corte a512 porque aquí la cola restante tiene signo favorable ya probado019 y se certifica además su tamaño; se mantiene fijo ese corte en toda la prueba.

## 2. Normalización y ARCH sin cuadratura

Se utiliza exactamente la norma021,

    norm²=binom(420,210)/(211·2^422·u^421).

Todas las cantidades siguientes están divididas por esta norma. Para k0, sea p_j el coeficiente de rho_N(t)=exp(−ut)P_N(t), p0=1 y

    p_(j+1)=p_j·2u(N−1−j)/[(j+1)(2N−2−j)].

El kernel arquimediano geométrico da EXACTAMENTE

    A_(N,0)=psi(16)−logpi
            −sum_(j=1)^(N−1) p_j j! 2^(−j) zeta(j+1,16).

La identidad de densidades beta normalizadas es

    A_(N,1)=2N A_(N,0)−(2N−1)A_(N+1,0).

POWER_ARCH_EXACT_032 documenta su reorganización estable: sólo sumas positivas y diferencias positivas S_p−(u/2)S_(p+1), donde S_p=zeta(p,16). El módulo tools/power_arch_exact_032_verify.py evalúa racionalmente todos los S_p con Euler–Maclaurin de orden8, corte32, y RESTO ABSOLUTO del Bernoulli periódico16. No se supone el signo del siguiente término.

El ancho total certificado de ARCH es menor que1e−18. En particular, redondeando hacia afuera,

    −1094177384741806137370/10^21
      < ARCH < −1094177384741806136520/10^21.              (ARCH)

Las constantes gamma, logpi y logaritmos proceden de power_fixed_grid_003.py: series racionales con resto. No se cambia precisión global ni se utiliza biblioteca de funciones especiales en el verificador.

## 3. Polar exacto y contactos completos hasta512

El polar es la fracción exacta

    POLAR=−1/[2(u²−1/4)^212·norm²].

Por019, con

    K=211·2^210/[211! binom(420,210)],
    r_j=(422−j)!/[2^(211−j)(211−j)!j!]
        ·[j(j+1)−422]/[(422−j)(421−j)],

cada contacto q=p^a aporta

    P_q=2logp·q^(−32)·K sum_(j=0)^211 r_j(u logq)^j.

El factor q^-32 es EXACTO: combina q^-1/2 y exp(−u logq). La lista de todos q<=512 se genera por división entera determinista de cada candidato primo y luego TODAS sus potencias. No se omiten4,8,...,512 ni se asigna Lambda(q)=logq para potencias superiores.

Para evitar pérdida por coeficientes pequeños, el Horner usa potencias divididas: a_j=K j! r_j y

    v_211=a_211,
    v_j=a_j+[u logq/(j+1)]v_(j+1).

Todos los intervalos se redondean hacia afuera. La división por el enorme entero q^32 se hace PRIMERO sobre los extremos racionales y después se construye el intervalo, evitando redondear prematuramente un recíproco menor que10^-60.

Las salidas racionales con denominador10^35 son

    PRIME<=512 en
    [146021371429136986781362640154070978,
     146021371429136986781362640154070979]/10^35,

    POLAR en
    [−36603632954956029193069220397307442,
     −36603632954956029193069220397307441]/10^35.

El ancho interno certificado del peine finito es menor que1e−40. La impresión anterior es sólo su redondeo exterior.

## 4. TODA la cola restante

ARITHMETIC_DIFFERENCES019 prueba un único cambio de signo de la autocorrelación k1. Para N211,

    chi_211 < (1+sqrt(8·211−11))/2 <21<u log2.

La comparación central equivale a21²−21−(2·211−3)=1>0. Por tanto C''_(212)(logq)>0 en TODOS los contactos q>=2 y cada término del peine es estrictamente positivo. En especial, omitir q>512 da una cota INFERIOR válida de W.

Para la cota superior se conserva el bound completo021 con M512. Para ell=1,...,212, f_ell(x)=x^-32(logx)^ell es unimodal, y

    sum_(n>M) f_ell(n) <= (1+32/M) I_ell,
    I0=1/(31M^31),
    Iell=M^-31(logM)^ell/31+(ell/31)I_(ell−1).

La comparación suma–integral en ambas ramas da integral+sup; la derivada logarítmica>=−32/M en x>=M implica sup<=32Iell/M. Se sustituye el extremo racional superior de log512 en la recurrencia positiva. Usando Lambda(n)<=logn y los módulos de los coeficientes,

    0 < TAIL
      <=2(1+32/M)sum_(j=0)^211 |a_j|u^j I_(j+1)/j!
      <1.1·10^(-15).                                    (TAIL)

El bound racional intermedio es aproximadamente1.0592138782e−15. No se usa una cuadratura de cola, ni se concluye su signo de un prefijo.

## 5. Decisión exacta y alcance

El script principal importa ARCH, polar, peine y cola certificados y comprueba con Fraction

    (ARCH+POLAR+PRIME<=512).lower >34/10^16,
    (ARCH+POLAR+PRIME<=512).upper+TAIL <45/10^16.

Como TODA la cola es positiva, estas dos desigualdades prueban DECISION. El margen pequeño es genuino y está rodeado por errores rigurosos más pequeños; no se infiere signo por concordancia entre dos precisiones.

Reproducción:

    python3 03-research/phase-211-sign-sandbox/tools/power_contact_decision_032_verify.py

Resultado PASS. Módulos auxiliares: power_contact_decision_032_contacts.py y power_arch_exact_032_verify.py. La conclusión decide solamente este candidato pendiente021. No se extrapola positividad a N próximos, a u variables, a una fila o a todas las ventanas.
