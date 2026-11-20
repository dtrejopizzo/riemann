# POWER_GEOMETRIC_TRANSFER_015 — Mezcla positiva exacta, normalización y convergencia fuerte en todo orden fijo

Estado: PROVED (identidad infinita y normalización, todos N>=1 y u>1). No es por sí sola una prueba de signo. El resultado complementario de positividad eventual está en POWER_HIGHPASS_015. Papers intactos.

## 1. Corpus, alcance y diferencia

Consultados índice/grid/crucigrama buscando high-pass, highpass, resolvent powers, positive/geometric mixture y one-pole iteration; revisados POWER_SIGNED_TRANSFER_014 §9 y la derivación independiente de un polo del análisis por casos. La estructura de filtros y las identidades racionales tienen antecedentes; la diferencia nueva es demostrar la expansión infinita con convergencia en una topología donde la forma COMPLETA es continua, y obtener pesos normalizados que suman exactamente uno. No se usa densidad L2 como sustituto de continuidad de forma.

Fijamos u>1. Esta restricción asegura que existe eta con 1/2<eta<u/2. El valor de la fase es u=63/2. No se afirma esta convergencia infinita para todo u>1/2: en parte de ese rango el multiplicador polar de la órbita puede crecer. Las identidades FINITAS de 014 siguen teniendo su alcance anterior u>1/2.

## 2. Iteración exacta de un polo

Sean N>=1, P real de grado <N, v>=u, y

    F0(s)=P(s)/(s+u)^N,
    Fv(s)=P(s)/[(s+u)^{N-1}(s+v)],
    Q(s)=s/(s+u), rho=u²/v², a=1-rho.

Escriba h_k por la función con transformada Q^k F0, y g_{k,v} por la de transformada Q^k Fv. La identidad completa de un polo prueba, para cada K>=0,

    W[fv]=rho Σ_{k=0}^K a^k W[h_k]+a^{K+1}W[g_{K+1,v}]. (FIN)

El término residual es la órbita del OBJETIVO fv, no la de f0. En transformadas,

    h_k(s)=s^kP(s)/(s+u)^{N+k},
    g_{K+1,v}(s)=s^{K+1}P(s)/[(s+u)^{N+K}(s+v)].

Prueba: cambiar sólo el polo v de g_{k,v} a u conserva el mismo factor rho y produce h_k; el sumando de ganancia es g_{k+1,v}. Iterar W[g_{k,v}]=rho W[h_k]+a W[g_{k+1,v}]. Esta identidad vale también para la norma L2 al cuadrado.

## 3. Una topología que controla TODA la forma

Elija 0<t<1/2 y 1/2<eta<u/2. Para funciones causales, extendidas por cero al semieje negativo, use

    ||f||_X²=||f||_{H^t(R)}²+||exp(eta y)f||_2².

Todo dato racional propio de tasas >=u pertenece a X, incluso si tiene un salto en el origen: su transformada decae al menos como 1/|tau|, y t<1/2 es suficiente.

La forma W es continua en X. En efecto:

* |m(tau)|<=C_t(1+tau²)^t controla la parte arquimediana.
* Los momentos polares satisfacen |A(f)|<=||f||_eta/sqrt(2eta-1), |B(f)|<=||f||_eta/sqrt(2eta+1).
* La autocorrelación verifica |c_f(logq)|<=||f||_2||f||_eta q^-eta. Por tanto el peine absoluto está acotado por 2Σ_{q>=2}Lambda(q)q^{-eta-1/2}||f||_2||f||_eta, cuya serie converge porque eta>1/2.

Así |W[f]|<=C_X||f||_X², y por polarización la forma bilineal es continua. No se pierde el polar ni el peine infinito en esta elección de norma.

## 4. La órbita high-pass converge a cero fuertemente

En el eje de Fourier,

    |Q(i tau)|²=tau²/(u²+tau²)<=1,

con desigualdad estricta para todo tau finito. En la recta de Laplace desplazada s=-eta+i tau,

    |Q(-eta+i tau)|²=(eta²+tau²)/[(u-eta)²+tau²]<1,

pues eta<u/2. Plancherel en esa recta representa la norma ponderada temporal. Convergencia dominada en las dos normas prueba, para todo dato racional f considerado,

    Q^k f ->0 fuertemente en X.

Los operadores Q^k son además contracciones de X. En particular h_k,g_{k,v}->0 en X y W[g_{k,v}]->0. Este resultado vale para TODOS los órdenes fijos N y todos los numeradores propios; no requiere que P se anule en el origen ni mayor regularidad temporal.

## 5. Mezcla infinita y normalización exacta

Pasando al límite en (FIN),

    W[fv]=rho Σ_{k>=0} a^k W[h_k],
    ||fv||²=rho Σ_{k>=0}a^k||h_k||².                     (MIX)

Ambas series convergen absolutamente. Para W, basta |W[h_k]|<=C_X||f0||_X² y Σ rho a^k=1; para la norma, son sumandos no negativos y el residuo converge a cero. Si v=u, sólo queda el término k=0.

Para P no nulo, todos h_k son no nulos. Los pesos

    pi_k=rho a^k||h_k||²/||fv||²

son no negativos y suman exactamente uno. Por tanto

    W[fv]/||fv||²=Σ_{k>=0}pi_k W[h_k]/||h_k||².           (RAY)

La suma de los valores absolutos ponderados también converge. Ésta es una mezcla de COCIENTES CUADRÁTICOS; no identifica fv con una suma de funciones ni autoriza ignorar términos cruzados de superposiciones arbitrarias.

## 6. Todos los polos: pesos homogéneos completos

Para tasas v_1,...,v_N>=u, f0=P/(s+u)^N y f=P/Π_j(s+v_j), ponga rho_j=u²/v_j², a_j=1-rho_j. Los filtros (s+u)/(s+v_j) conmutan con Q y son contracciones tanto en H^t como en la norma ponderada de §3. Aplicar sucesivamente (MIX), usando convergencia absoluta, da

    W[f]=Σ_{k>=0}w_k W[Q^k f0],
    ||f||²=Σ_{k>=0}w_k||Q^k f0||²,                       (MULTI)

donde

    Σ_{k>=0}w_k z^k=Π_j rho_j/(1-a_j z),
    w_k=(Π_j rho_j)Σ_{k_1+...+k_N=k}Π_j a_j^{k_j}.

Los pesos w_k son no negativos y Σw_k=1. El paso a sumas múltiples es legítimo porque todas las formas de las órbitas filtradas están uniformemente acotadas por C_X||f0||_X². También se puede verificar el generador directamente en el eje de Fourier:

    |(s+u)/(s+v_j)|²=rho_j/[1-a_j|Q(s)|²], s=i tau.

El polar está incorporado por la identidad completa finita antes de pasar al límite; no se deduce su signo de una medida espectral positiva.

Los pesos normalizados para el cociente de f son w_k||Q^k f0||²/||f||² y suman uno. Así, positividad de TODA la órbita high-pass Q^k V_N sería suficiente para todos los N polos >=u. La suficiencia no presupone signo de esos bloques.

## 7. Monotonía válida y el nodo que queda

Para un numerador fijo, el cociente arquimediano de h_k es no decreciente: el cambio k->k+1 repondera la probabilidad espectral por tau²/(u²+tau²), creciente en |tau|, y se aplica la covarianza positiva con m. El polar no tiene esa propiedad: exactamente

    Polar[h_k]=[-1/(4u²-1)]^k Polar[h_0].

Cada correlación prima contiene un coseno oscilante; no se ha probado monotonía del cociente COMPLETO en k. No se obtiene una regla de signo sumando sólo coeficientes Lambda>=0.

POWER_HIGHPASS_015 prueba por otro argumento que, para cada N fijo, los bloques completos Q^k V_N son uniformemente positivos para k suficientemente grande. En consecuencia, para cada orden fijo sólo un segmento FINITO de la órbita puede impedir la condición suficiente de (MULTI). No se dispone aquí de un extremo efectivo universal de ese segmento ni se ha verificado su signo para todos N. La mezcla exacta, la normalización y el control de la cola son herramientas demostradas; la positividad de los bloques iniciales que faltan sigue siendo el nodo aritmético.
