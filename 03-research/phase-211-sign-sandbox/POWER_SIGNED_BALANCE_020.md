# POWER_SIGNED_BALANCE_020 — El primer contacto no basta para el balance k1

Estado: **PROVED**, obstrucción cuantitativa concreta al balance con sólo contacto2; signo de la forma COMPLETA en este punto **no decidido aquí**. Papers intactos.

## 1. Corpus y razón nueva

Consultados las reglas del proyecto, STATE019, ARITHMETIC_DIFFERENCES019 y su auditoría, TABLE_DESCENT018, el índice de rutas (Euler/Möbius/momentos), grid maestro y CROSSWORD-TO-D.md (rondas018/019, test reparado por contacto2 en006). El signo positivo de TODO el peine para k1,N<=211 está probado019. Ese signo no da su magnitud. Tampoco se extrapola el vector particular006 donde el contacto2 sí reparaba una pérdida arquimediana-polar.

La diferencia específica consiste en enfrentar esa magnitud con una cota analítica de ARCH para un átomo de la MISMA columna firmada. Se prueba una obstrucción al lema concreto «basta el primer contacto positivo para reparar ARCH+POLAR a lo largo de la columna k1 hasta211». No se prueba una prohibición sobre todos los peines finitos ni sobre otras desigualdades aritméticas. No hay campaña de certificados ni nuevos conteos de raíces: se usa un solo punto, N=211,u=63/2,k=1, con todo el resto del peine conservado como positivo.

## 2. Una cota arquimediana analítica útil en N variable

Sea F_(N,1)(s)=s/(s+u)^(N+1), N>=2, y normalice su densidad de Fourier a una probabilidad. Escriba T=tau/2. La integral beta da exactamente

    E T² = V_N = 3u²/[4(2N−3)].                              (V)

Para a>0, la fórmula elemental de sumación de Euler para psi en Re z=a da

    psi(z)=log z−1/(2z)+R(z),   |R(z)|<=1/(2a).               (EM)

Por ejemplo R es, salvo signo, la integral de ({t}−1/2)/(z+t)²; su módulo está acotado por (1/2)int_0^infty(a+t)^(-2)dt. No se necesita signo de R complejo.

Trasladando cuatro pasos desde 1/4+iT hasta a+iT con a=17/4, tomando partes reales y usando (EM),

    Re psi(1/4+iT)
    <= (1/2)log(a²+T²) − a/[2(a²+T²)] + 1/(2a)
       − sum_(j=0)^3 b_j/(b_j²+T²),     b_j=j+1/4.

Las funciones log(A+x) y −b/(b²+x) son cóncavas para x>=0. Jensen y (V) prueban, UNIFORMEMENTE para N>=2,u>0,

    ARCH_(N,1)/norm² <= U_N(u)
      := (1/2)log(a²+V_N) − a/[2(a²+V_N)] + 1/(2a)
         − sum_(j=0)^3 b_j/(b_j²+V_N) − log pi.              (U)

Ésta es una cota unilateral real de la energía arquimediana, no una aproximación gaussiana. En N=211,u=63/2, la verificación racional de logaritmos da

    U_211(63/2)<−74/100.                                    (A)

## 3. Magnitud exacta del contacto2

Use los polinomios y normalización ya probados019:

    p_N(x)=sum_j (2N−j)!x^j/[2^(N−j)(N−j)!j!],
    r_N=p_N−2p_N'+p_N'',
    C_(N+1)''(t)=e^(−ut)r_N(ut)/[2^(N+1)u^(2N−1)N!].

La norma beta del átomo es

    norm²=binom(2N−2,N−1)/[N 2^(2N)u^(2N−1)].               (NORM)

Defina K_N=N2^(N−1)/[N!binom(2N−2,N−1)]. La autocorrelación normalizada es −e^(−ut)K_Nr_N(ut). En u=63/2 el contacto q=2 se simplifica EXACTAMENTE, pues 2^(−u)=2^(−31)/sqrt2:

    P_2/norm²
      = [log2/2^31] K_N r_N((63/2)log2).                    (P2)

No hay radical ni resto de cola en (P2). La identidad COEF019 da todos los coeficientes racionales de r_N. Evaluar (P2) mediante intervalos racionales para log2 prueba, en N=211,

    0<P_2/norm²<75/1000.                                   (B)

El cálculo usa Horner con extremos racionales SIN redondear en cada paso. Redondear prematuramente coeficientes factorialmente pequeños antes de elevar x a grado211 perdería información; el verificador evita esa pérdida. Sólo la evaluación final vuelve a los intervalos de003.

## 4. Balance y alcance exactos

Para k=1 el polar es estrictamente negativo:

    POLAR=2F(−1/2)F(1/2)=−1/[2(u²−1/4)^(N+1)]<0.

Combinando (A),(B), en este átomo concreto,

    [ARCH+POLAR+P_2]/norm² < −.74+.075 < −.66.               (FAIL2)

Por019, para N211,u31.5 TODOS los demás contactos son positivos. La identidad que conserva la obligación real completa es

    W = ARCH+POLAR+P_2 + sum_(q>=3) P_q,
    P_q>=0,   sum_(q>=3)P_q absolutamente convergente.

FAIL2 no dice que W sea negativa y no permite borrar los contactos q>=3. Prueba exactamente que una cota inferior basada sólo en P_2 y en ignorar los demás sumandos favorables NO puede reparar este átomo: incluso el valor real de la forma con sólo ese contacto es negativo. Cualquier balance positivo aquí debe utilizar más información cuantitativa del peine restante. Esto distingue la situación del caso006 reparado por contacto2.

No se registra una nueva fila de signo W ni se extiende cobertura de la tabla. El siguiente paso sustantivo requiere una cota unilateral de varios contactos o de su masa conjunta que conserve las compensaciones con ARCH y el polar. El argumento no convierte una identidad en ese bound.

Verificador: tools/power_signed_balance_020_verify.py, aritmética Fraction e intervalos exactos heredados003; PASS. Una única evaluación N211, no barrido. La cota U se demuestra para N variable, pero la obstrucción FAIL2 sólo se afirma en el punto declarado.
