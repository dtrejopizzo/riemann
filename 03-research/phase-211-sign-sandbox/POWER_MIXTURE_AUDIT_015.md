# POWER_MIXTURE_AUDIT_015 — Identidad geométrica completa y convergencia en norma de forma

Estado: PROVED identidades, índices y convergencia para u>1; no demuestra signo de sus componentes. Papers intactos.

## 1. Índice exacto del resto finito

Fije v>=u>1/2 y una función racional causal f0, con todas sus tasas>=u y numerador de grado menor que el denominador. Escriba

    H(s)=(s+u)/(s+v), fv=H f0,
    R0=u²/v², a=1-R0,
    Q(s)=s/(s+u), q(tau)=|Q(i tau)|²=tau²/(u²+tau²).

La identidad escalar exacta es |H|²=R0/(1-aq). El resultado de PRIME_TRANSFER014 equivale a

    W[fv]=R0 W[f0]+a W[Q fv].

Los filtros Q,H conmutan. Iterar este resultado da, para TODO entero K>=0,

    W[fv]=R0 sum_(k=0)^K a^k W[Q^k f0]
              +a^(K+1)W[Q^(K+1)fv].                    (FIN)

El resto contiene la función OBJETIVO fv, no solamente f0. Se puede comprobar también por |H|²=R0 sum_(k0..K)(aq)^k+(aq)^(K+1)|H|² y la identidad polar correspondiente. Cada igualdad finita vale con todos los contactos: las funciones son racionales causales de tasa positiva y el peine converge absolutamente.

## 2. Espacio fuerte y convergencia del resto

Para el paso infinito se usa aquí la hipótesis suficiente u>1. Elija1/2<eta<u/2 y0<s<1/2, y tome la norma

    ||f||_(eta,s)=||e^(eta y)f(y)1_(y>0)||H^s(R).

Toda función racional causal de tasas>=u pertenece a este espacio: después de ponderar, su transformada racional tiene polos con tasas>=u-eta>0 y colaO(1/|tau|), suficiente para H^s cuando s<1/2. No se supone ausencia de salto temporal en0.

El multiplicador Q ponderado es

    Q(-eta+i tau)=(-eta+i tau)/(u-eta+i tau).

Su módulo es<=1 en toda la recta y<1 para todo tau finito, porque eta<u/2. Para f fijo, Parseval y convergencia dominada en la integral con peso(1+tau²)^s dan

    ||Q^k f||_(eta,s)->0,
    ||Q^k f||_(eta,s)<=||f||_(eta,s).

Las identidades de ponderación se aplican a funciones racionales causales con decaimiento exponencial, así no se ha supuesto antes una estimación de norma para justificar la recta desplazada.

La forma COMPLETA W es bilineal continua en este espacio. La parte gamma se controla por log(2+|tau|)<=C_s(1+tau²)^s, después de multiplicar por la función Lipschitz acotada e^(-eta max(y,0)). La correlación ponderada decae como e^(-eta t), por lo que sum2Lambda(q)q^(-eta-1/2) converge y controla el peine. Los dos momentos polares son continuos porque eta>1/2. Por tanto W[Q^k f]->0 y permanece uniformemente acotada.

Aplicar esto a fv en FIN elimina el resto. Se obtiene la identidad ABSOLUTAMENTE convergente

    W[fv]=R0 sum_(k>=0) a^k W[Q^k f0].                  (INF)

Los pesos R0 a^k son no negativos y suman1, pero los sumandos de W pueden tener ambos signos. No se normalizaron los vectores. Para una mezcla de cocientes Rayleigh deben introducirse además las normas² de los vectores, que también satisfacen su propia identidad de mezcla.

La restricción u>1 no es cosmética para esta prueba: si1/2<u<sqrt(1/2), el multiplicador polar de Q es -1/(4u²-1), de módulo>1, y una expansión infinita de la forma completa puede fallar para a grande. Las identidades finitas siguen correctas, pero no se extiende INF a todo u>1/2 sin otra hipótesis de estabilidad.

## 3. Todos los polos nuevos como una única mezcla de potencias high-pass

Desde f0=P/(s+u)^n hacia f=P/prod_j(s+v_j), v_j>=u>1, ponga a_j=1-u²/v_j² y R0j=1-a_j. Todos los filtros usan el MISMO Q. La iteración de INF y Fubini da

    W[f]=sum_(k>=0) w_k W[Q^k f0],
    w_k=(prod_j R0j)sum_(k1+...+kn=k)prod_j a_j^(kj),
    sum_k w_k t^k=prod_j R0j/(1-a_j t), sum_k w_k=1.

La convergencia absoluta no requiere un signo supuesto: cada operador H_j tiene norma ponderada<=1, y los términos Q^k f0 están uniformemente acotados en la norma fuerte anterior; el total de los pesos positivos es1. Esto justifica los intercambios de las series finitas por factores e infinitas por grados.

Para una dimensión n FIJA, una desigualdad W[Q^k f0]>=0 para TODOS los k y TODOS los numeradoresP de grado<n transportaría el signo a todas las tasas>=u. No basta demostrarla para un solo P ni para algunos k. Las funciones Q^k f0 están en los espacios confluentes de n+k polos y tienen numerador s^kP, con un cero de orden k.

## 4. Qué aporta y qué no aporta la identidad

Este desarrollo es una identidad de filtros y formas, compatible con el alcance de prop:opcalc. No crea una compensación aritmética. La obligación de signo está ahora explícita sobre subespacios racionales con ceros prescritos; demostrarla sería la desigualdad adicional y no una consecuencia de cambiar coordenadas.

Para la parte arquimediana hay un resultado finito inmediato: reponderar por q, creciente en |tau|, da

    Rayleigh_ARCH(Q^(k+1)f0)>=Rayleigh_ARCH(Q^k f0).

La comparación es estricta para un vector no nulo y se extiende a los eigenvalores ordenados de estos subespacios por min--max en el MISMO espacio de numeradoresP. No se afirma esa monotonía para W ni para AP.

La eventual positividad uniforme de W en toda la familia Q^k V_n es un objetivo separado. El escalamiento natural de frecuencia es sqrt(k), pero una afirmación uniforme debe controlar simultáneamente todos los coeficientesP, el cociente de la norma ponderada, los momentos y el peine. Un argumento sólo para el término de mayor grado de P no es uniforme cuando ese coeficiente se anula o depende de k. Esta nota no asume ese resultado futuro.
