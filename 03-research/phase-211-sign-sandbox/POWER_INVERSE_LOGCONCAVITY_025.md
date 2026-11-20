# POWER_INVERSE_LOGCONCAVITY_025 — Cierre del balance aritmético firmado para N129

Estado: **PROVED** logconcavidad de un polinomio compensado para todos N; **PROVED** corte exterior mejorado para K129; combinado con CELL_TEST024, **PROVED** ERR129<−33/50. Revisión independiente aprobada en POWER_INVERSE_LOGCONCAVITY_AUDIT_025.md, verificador PASS. No se afirma W>=0. Papers intactos.

## 1. Corpus y diferencia precisa

Leídos las reglas del proyecto, INVERSE_KERNEL020, CUMULATIVE_INVERSE022, CUMULATIVE_TEST023, CELL_BALANCE024 y CELL_TEST024. Consultados índice/grid/crucigrama sobre logconcavidad de coeficientes/polinomios y Möbius; encontrados antecedentes de logconcavidad genérica y su insuficiencia, contrastados también con CONE001§4. No se usa theta positiva ni se infiere positividad de un inverso desde logconcavidad genérica.

La diferencia matemática aquí es demostrar que el cociente logarítmico de un polinomio ESPECÍFICO decrece. Una única desigualdad racional en t0 entonces controla TODA la suma Möbius completa en una semirrecta muchísimo mayor que el corte de grado020. Esto permite combinar un solo balance interior integrado con todas las demás celdas, sin campaña de N y sin volver a exigir K>=0 donde ya fue refutado. El lema de covarianza y los criterios clásicos de cocientes no se presentan como herramientas nuevas; su aplicación produce el nuevo corte y un bound firmado de ERR real.

## 2. Coeficientes y logconcavidad para TODOS N

Fije u=63/2,N>=2,d=N−1. Con P_N(t)=sum_(j=0)^d p_jt^j, p0=1 y la recurrencia gamma020,

    (j+1)p_(j+1)/p_j=2u(d−j)/(2d−j),
    D_N(t)=33P_N(t)−P_N'(t)=sum_(j=0)^d c_jt^j,
    c_j=p_j(3d+30j)/(2d−j)>0.                              (COEF)

El inverso compensado COMPLETO de022 es

    K_N(x)=x^(−32)sum_(m>=1)mu(m)m^(−32)D_N(logx+logm).     (INV)

Defina r_j=(j+1)c_(j+1)/c_j para j<d y r_d=0. De COEF,

    r_j=2u [(d−j)/(2d−j−1)] [(3d+30(j+1))/(3d+30j)].        (RATIO)

La primera razón es no creciente en j: su derivada continua tiene numerador1−d<=0. La segunda es1+30/(3d+30j), estrictamente decreciente. Por tanto r_j decrece, incluido el paso final a0. Para t>0, los pesos omega_j=c_jt^j/D_N(t) forman una probabilidad y

    D_N'(t)/D_N(t)=sum_j omega_j r_j,
    (D_N'/D_N)'=Cov_omega(r_j,j)/t<=0.                     (LC)

El signo de la covarianza se prueba directamente como (1/2)sum_(i,j)omega_iomega_j(r_i−r_j)(i−j)<=0. Así log D_N es cóncava en t>0 y por continuidad en t>=0. No se afirma que esto por sí solo haga positivo el inverso.

## 3. Un certificado racional basta para una semirrecta completa

Si para cierto t0>0 se prueba D_N'(t0)<=30D_N(t0), LC implica para TODO t>=t0 y m>=1

    D_N(t+logm)/D_N(t)<=exp(30logm)=m^30.

Por INV y la suma COMPLETA de Möbius,

    |K_N(x)/[x^(−32)D_N(logx)]−1|
       <=sum_(m>=2)m^(−2)<=1/4+int_2^infty y^(−2)dy=3/4.

En particular,

    K_N(x)>=x^(−32)D_N(logx)/4>0 para logx>=t0.             (CUT)

La cota controla todos los m, no un prefijo, y no presupone cancelación Möbius favorable.

Para N129,t0=2/3, el verificador Fraction reconstruye exactamente los129 coeficientes de COEF y prueba

    D_129'(2/3)<30D_129(2/3).                              (CHECK)

No se usa un valor decimal del cociente en la prueba. Puesto que log2>2/3, CUT demuestra

    K_129(x)>0 para TODO x>=2.                            (TAIL-K)

La negatividad certificada K129(1)<−1/251 sigue intacta y es compatible con TAIL-K. No se afirma una única transición ni un signo uniforme en1<x<2.

## 4. TODAS las celdas restantes y el balance firmado completo

De J_N(x)=x int_x^infty K_N(t)/t²dt y TAIL-K, se tiene J129(x)>0 para x>=2 y J129(x)/x decreciente allí. Por el lema LOCAL024, para TODO n>=3,

    S_129(n)>=b_n J129(n)>0,
    b_n=H_(n−1)(1−1/(2n))−logn>=3/4−log2>0.

El certificado de la primera celda, CELL_TEST024, prueba con Möbius completo y cola rigurosa

    S_129(2)>33/100.

La suma de las celdas es absolutamente convergente. Por consiguiente el error aritmético NORMALIZADO de019/018 satisface sobre TODA la semirrecta

    F_129=ERR129=−2sum_(n>=2)S_129(n)<−33/50.               (FULL)

Ésta es una desigualdad firmada real integrada, no un signo de prefijo ni un criterio puntual: la primera celda compensa su región K negativa y todas las celdas restantes se controlan analíticamente, sin enumeración infinita. También se podría usar la representación C_B de022, pero no se suma su beneficio con S2: son asignaciones distintas del mismo emparejamiento.

## 5. Límite exacto frente a la forma W

FULL no es aún un certificado W>=0. La identidad018 conserva

    W[g129]/C129(0)=ARCH_sharp[g129]/C129(0)−ERR129.

Falta comparar cuantitativamente el déficit ARCH_sharp con el beneficio firmado completo; el bound ERR<−.66 no se declara suficiente para esa comparación. No se extiende el signo de ERR a otros N, ni la tabla completa, ni una nueva ventanaT. El resultado es un balance aritmético integrado completo en el mismo orden129 donde falló el criterio puntual.

Reproducción exacta:

    python3 03-research/phase-211-sign-sandbox/tools/power_inverse_logconcavity_025_verify.py
    python3 03-research/phase-211-sign-sandbox/tools/power_cell_test_024_verify.py

El primero certifica CHECK; LC/CUT prueban su extensión infinita. El segundo certifica la única celda interior y la cola Möbius que interviene en ella. No hay valores aproximados en la demostración.
