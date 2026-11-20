# POWER_INTERIOR_017 — Toda la fila escalar N=1, con margen uniforme y control de TODO el peine

Estado: PROVED, para todos k>=0 y todas u>=63/2. No resuelve el interior conjunto N,k crecientes. Papers intactos.

## 1. Resultado y razón nueva frente al corpus

Leídos POWER_STATE_015/016, POWER_TATE_CHAIN_009, POWER_PACKET_SCOPE_AUDIT_009, POWER_HIGHPASS_015, POWER_DESCENT_016 e índice/grid/crucigrama mediante búsquedas de cadenas racionales, high-pass, potencias de resolvente y paquetes beta. La familia Tate009 incrementa el orden con numerador fijo s²-1/4 y concentra en frecuencia cero; su identidad escalar no daba signo. Aquí se fija N=1 y se incrementa k en

    F_k(s)=s^k/(s+u)^{k+1}, u>=63/2.

La diferencia nueva es una cota EXACTA de norma ponderada relativa, UNIFORME EN TODO k, obtenida por una convolución de coeficientes binomiales. Permite controlar el peine completo y los pasos iniciales a la vez, sin un umbral asintótico desconocido. No se usa el valor límite E0 ni se reclama que una sola fila cierre todos los tests.

Para la función causal real h_k con transformada F_k se demuestra

    W[h_k]>(4/3)||h_k||², todos k>=0,u>=63/2.             (ROW1)

Son espacios confluentes de órdenes k+1 arbitrariamente grandes, aunque con un numerador específico. No se infiere signo para sus combinaciones arbitrarias.

## 2. Lema nuevo: cociente ponderado uniforme para toda la fila

Más generalmente, fije u>0 y 0<=eta<u/2. Ponga a=u-eta, b=eta y c_k=binom(2k,k)/4^k. Entonces

    ||h_k||²=c_k/(2u),
    ||exp(eta y)h_k||²/||h_k||²
       <=u(u-eta)/[u(u-2eta)]
       =(u-eta)/(u-2eta), todos k>=0.                    (WR)

Prueba. Plancherel en la recta s=-eta+i tau da

    N_k(eta)=(1/2pi)∫(tau²+b²)^k/(tau²+a²)^{k+1}d tau.

Para 0<=z<1, sumar la serie geométrica dentro de la integral produce exactamente

    Σ_{k>=0}N_k(eta)z^k
       =1/[2sqrt((1-z)(a²-b²z))].                        (GEN)

Todos los términos son no negativos y a>b. Expandiendo los dos factores binomiales,

    N_k(eta)=[1/(2a)]Σ_{j=0}^k c_{k-j}c_j(b²/a²)^j.

Cuando eta=0 esto da N_k(0)=c_k/(2u). La desigualdad combinatoria

    c_{k-j}c_j<=c_k

sale de Vandermonde: el producto binom(2j,j)binom(2k-2j,k-j) es UNO de los términos no negativos que suman binom(2k,k). Por tanto

    N_k(eta)/N_k(0)
       <=(u/a)Σ_{j>=0}(b²/a²)^j
       =u a/(a²-b²)=(u-eta)/(u-2eta).

No se ha tomado k grande ni estimado un coeficiente principal: (WR) vale simultáneamente en cada orden, incluyendo k=0.

Con eta=15 y u>=63/2, el miembro derecho es <=11, pues (u-15)/(u-30) decrece en u>30. De aquí

    ||exp(15y)h_k||<=sqrt11||h_k||.                       (W11)

## 3. Parte arquimediana: margen uniforme desde el primer paso

La densidad espectral de h_{k+1} repondera la de h_k por q(tau)=tau²/(u²+tau²), creciente en |tau|. Como m crece en |tau|, la covarianza positiva prueba que la energía arquimediana NORMALIZADA no disminuye con k. Así

    Arch[h_k]/||h_k||² >=psi((u+1/2)/2)-logpi
                         >=psi(16)-logpi>3/2.

La última cota es elemental: psi16=H15-gamma, gamma<3/5, logpi<6/5 y H15-9/5>3/2. Las cotas de gamma y logpi ya fueron certificadas racionalmente en las rondas previas; el verificador de esta nota las comprueba de nuevo con esos intervalos.

Esta comparación sólo afirma monotonía arquimediana. El polar alterna y el peine no tiene signo por covarianza.

## 4. Polar exacto, conservado y acotado uniformemente

Los dos momentos de h_k son F_k(-1/2) y F_k(1/2), de modo que

    Polar[h_k]=2(-1/4)^k/(u²-1/4)^{k+1}.

Dividir por c_k/(2u) da

    |Polar[h_k]|/||h_k||²
      =[4u/(u²-1/4)]*[1/(4u²-1)]^k/c_k.

Se tiene c_k>=2^-k, ya que binom(2k,k)=Π_{j=1}^k(k+j)/j>=2^k. Por tanto el segundo factor es <=[2/(4u²-1)]^k<=1 en el rango declarado. Además 4u/(u²-1/4) decrece para u>1/2. En consecuencia

    |Polar[h_k]|/||h_k||²<=126/992=63/496.                (POL)

No se anula ni se omite el polar; se conserva su fórmula completa y se cuenta su peor signo.

## 5. TODOS los contactos aritméticos, sin truncamiento

De (W11), para cualquier t>=0,

    |c_hk(t)|<=||h_k||*||h_k 1_{y>=t}||
             <=sqrt11 exp(-15t)||h_k||².

Así el peine infinito, que converge absolutamente, cumple

    |Comb[h_k]|/||h_k||²
       <=2sqrt11 Σ_{q>=2}Lambda(q)q^{-31/2}
       <7Σ_{q>=2}q^-14
       <=105/[13*2^14]<1/2000.                           (PRIME)

Se usaron 2sqrt11<7, Lambda(q)<=logq<=q, q^-29/2<=q^-14 y la comparación integral Σ_{q>=2}q^-14<=2^-14(1+2/13). Esta estimación incluye todas las potencias primas; no presume que los contactos ayuden ni cambia los coeficientes de Lambda.

## 6. Cierre de la fila y alcance

Sumando los tres componentes completos,

    W[h_k]/||h_k||²
       >3/2-63/496-1/2000
       =42547/31000>4/3.

Esto prueba (ROW1) para TODOS los k, con un margen independiente de k y u>=63/2. El cálculo finito de constantes se reproduce con `python3 03-research/phase-211-sign-sandbox/tools/power_interior_017_verify.py`; las desigualdades de todos los k proceden de (GEN) y Vandermonde, no de una lista de comprobaciones.

La fila N=1 no cubre el régimen conjunto k/N finito cuando N también crece, que sigue pendiente. El puente escalar de la ronda017 requiere TODAS las filas N,k; no permite sustituirlas por esta fila, por la cola eventual ni por una unión densa de tests individuales. El avance reutilizable es (WR): un cociente ponderado uniforme que conserva toda la órbita, y podría servir como base de un descenso cuantitativo entre filas si se construye ese paso aritmético adicional.

## 7. Extensión cuantitativa a TODAS las filas: norma ponderada uniforme en k

Este lema adicional no afirma signo para todas las filas. Para enteros N>=1,k>=0, defina

    F_{N,k}(s)=s^k/(s+u)^{N+k},
    a=u-eta, b=eta, rho=b²/a², 0<=eta<u/2,
    B_l^(N)=Π_{r=0}^{N-2}(2l+2r+1)/(2r+1).

El producto vacío para N=1 vale uno. Entonces, para TODOS los k,

    ||exp(eta y)f_{N,k}||²/||f_{N,k}||²
      <=R_N(u,eta):=(u/a)^{2N-1}S_N(rho),
    S_N(rho)=Σ_{l>=0}B_l^(N)rho^l.                       (WRN)

La constante es explícita y calculable por un número FINITO de operaciones: B_l^(N) es un polinomio en l de grado N-1 y

    S_N(rho)=Π_{r=0}^{N-2}
       [(2rho d/drho+2r+1)/(2r+1)] (1/(1-rho)).

Por tanto S_N es una función racional con denominador que divide (1-rho)^N; no es una estadística aritmética desconocida ni un límite asintótico. Por ejemplo

    S_1=1/(1-rho), S_2=(1+rho)/(1-rho)².

Prueba de (WRN). Expandir el numerador positivo (tau²+b²)^k dentro de la integral de Plancherel y usar la integral beta da

    N_{N,k}(eta)=a^{1-2N}/(2pi)
       *Σ_{l=0}^k binom(k,l)rho^l
            Beta(k-l+1/2,N+l-1/2),
    N_{N,k}(0)=u^{1-2N}/(2pi)Beta(k+1/2,N-1/2).

El cociente de cada coeficiente beta se factoriza EXACTAMENTE como

    binom(k,l)Beta(k-l+1/2,N+l-1/2)
         /Beta(k+1/2,N-1/2)
       =[c_{k-l}c_l/c_k]B_l^(N).

Vandermonde acota el corchete por uno. Todos los términos son no negativos; extender la suma de l<=k a l>=0 demuestra (WRN). La serie converge porque rho<1 y B_l^(N) crece sólo polinómicamente.

Para eta>1/2, esta desigualdad ofrece inmediatamente el control del peine COMPLETO, uniforme en k,

    |Comb[f_{N,k}]|/||f_{N,k}||²
      <=2sqrt(R_N(u,eta))Σ_{q>=2}Lambda(q)q^{-eta-1/2}.

Así se dispone de una constante efectiva por fila N que controla también sus primeros pasos. Se distingue de 015, donde el cociente ponderado se controlaba asintóticamente para k grande mediante matrices límite. Aquí no hay un umbral en k; la dependencia en N permanece y no se ha probado que sea suficientemente pequeña para cerrar la tabla completa.
