# POWER_HIGH_ORDER_PM_NOGO_007 — Falsificador alto del movimiento arch+polar uniforme en dimensión

Estado: PROVED. NO refuta transporte de signo, ni el resultado local de orden cuatro, ni el signo completo. Papers intactos.

## 1. Corpus y razón nueva

Consultados índice ROUTES-TRIED-INDEX, grid maestro y crucigrama mediante búsquedas high-order pole, gamma packet, pole no-go, 131072 y derivadas de digamma; revisados POWER_POLE_MOVEMENT_004 y POWER_POLAR_MOVEMENT_005. El contraejemplo de orden uno de 005 sólo tenía tasas pequeñas (1 y 2). La razón nueva es un falsificador EXACTO dentro del rango u>=63/2, con dimensión explícita grande y una identidad escalar: no se buscan espectros de matrices grandes. Construcción propuesta por el constructor principal y verificada aquí.

## 2. Lema global arquimediano

Para m(tau)=Re psi(1/4+i tau/2)-log pi,

    0<=tau m'(tau)<4, tau real.                             (G)

Prueba. Ponga t=|tau|/2 y a_k=k+1/4. La serie de digamma derivada da

    tau m'(tau)=Σ_{k>=0} 2 a_k t²/(a_k²+t²)².

Si t<=1, el término k=0 es <=1/(2a_0)=2. El resto es a lo sumo

    2Σ_{k>=1}(k+1/4)^-3
      <=2[(5/4)^-3+∫_1^∞(x+1/4)^-3 dx]=208/125.

La suma es <=458/125<4. Si t>=1, f(a)=2at²/(a²+t²)² es no negativa y unimodal, con integral sobre (0,infinito) igual a 1 y máximo 3sqrt3/(8t)<1. Comparando por separado las ramas creciente y decreciente con integrales de paneles de longitud uno, y apartando a lo sumo dos términos próximos al máximo, la suma de cualquier retícula de paso uno es <=∫f+2max f<3. Esto se aplica a a_k. En t=0 el resultado es inmediato. La convergencia absoluta justifica derivar la serie.

## 3. Familia de numerador fijo y polar exacto

Para n>=1 entero, u>1/2, sea f_{n,u}(y)=y^{n-1}exp(-uy)1_{y>0}. Su transformada de Laplace es (n-1)!/(s+u)^n; el factor constante no altera cocientes. Es el numerador fijo 1 con n polos iguales u. Directamente,

    ||f||²=(2n-2)!/(2u)^{2n-1},
    A=(n-1)!/(u-1/2)^n, B=(n-1)!/(u+1/2)^n.

El cociente polar normalizado es

    P_n(u)=2AB/||f||²
      =4^n/[u binom(2n-2,n-1)]*(1-1/(4u²))^-n.            (P)

Por binom(2n-2,n-1)<=4^{n-1}, se tiene P_n(u)>=4/u. Además

    u d(log P_n)/du=-1-n/[2(u²-1/4)].                     (PD)

La probabilidad espectral normalizada es una constante por u^-1[1+(tau/u)²]^-n. Cambiar tau=ut en la energía arquimediana A_n(u) y usar (G) da

    u A_n'(u)=E[tau m'(tau)]<4.                           (AD)

La derivación bajo la integral se justifica por (G). No se evalúa una matriz de tamaño n.

## 4. Contraejemplo alto explícito, también para cada polo individual

Tome u=63/2, n=2^17=131072. Para E_n=A_n+P_n,

    u E_n'(u)<4-(4/u)[1+n/(2(u²-1/4))]
              =4-264/31=-140/31<0.                       (NEG)

La igualdad es aritmética racional exacta; no usa aproximaciones de factoriales ni potencias grandes.

Para pasar a movimientos INDIVIDUALES, defina E(u_1,...,u_n) con transformada 1/Π_j(s+u_j). Es diferenciable y simétrica para u_j>1/2. En confluencia todas las parciales son iguales, y

    E_n'(u)=Σ_j ∂E/∂u_j=n ∂E/∂u_1.

Por ello, en el punto declarado,

    u ∂E/∂u_j < -140/(31n), cada j.

Existe epsilon>0 tal que aumentar solamente UN polo desde 63/2 a 63/2+epsilon disminuye el cociente arch+polar del numerador fijo. Todos los polos siguen en el rango alto. No se confunde dilatación global con cambio individual: la simetría diferenciable es el argumento explícito que permite pasar entre ambos.

## 5. Alcance preciso

Queda FALSIFIED la afirmación «para todo n y todos los polos >=63/2, aumentar individualmente los polos no reduce el cociente arch+polar de ningún numerador». No se puede extender uniformemente en dimensión la derivada positiva de POWER_POLAR_MOVEMENT_005 §6.

NO se concluye que la energía sea negativa, ni se descarta un transporte que preserve sólo el signo: una energía positiva puede decrecer y seguir positiva. Tampoco se ha incluido el peine. El teorema arquimediano de covarianza permanece válido; el cambio de signo proviene de la derivada del polar positivo. El resultado local n=4 no está afectado.

Herramienta reutilizable nueva: la cota global (G) y el polar exacto (P) permiten auditar propuestas de transporte sin construir matrices grandes.

La afirmación falsificada es el cociente Rayleigh para TODO numerador bajo la identificación racional de numeradores fijos. No se proporciona aquí un contraejemplo a la monotonía de lambda_min ni de otras eigenenergías comprimidas: que disminuya el cociente de un vector particular no implica que disminuya el mínimo del espacio. La monotonía de eigenenergías de la parte ARQUIMEDIANA sigue probada por el argumento separado de 004.
