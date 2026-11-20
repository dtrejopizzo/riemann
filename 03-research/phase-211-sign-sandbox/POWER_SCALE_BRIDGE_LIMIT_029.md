# POWER_SCALE_BRIDGE_LIMIT_029 — Alcance del cono de tasas crecientes

Estado: PROVED obstrucción de aproximación por mezclas positivas de densidades normalizadas. Prueba completa revisada y APROBADA en POWER_SCALE_AUDIT_029.md. No refuta W ni otros puentes. Papers intactos.

## Corpus y diferencia

Consultados índice de rutas, grid y crucigrama; leídos SCALAR_BRIDGE017 y JOINT_SCALE016. La obstrucción de pesos centrados016 mantiene u fijo y deja crecer N/u². La presente obligación es distinta: determinar si el nuevo dominio u>=C sqrt(N), para un C>0 fijo, puede reemplazar TODOS los átomos del puente017 mediante aproximación positiva de densidades. Se demuestra una cota de concentración del cono completo, no una afirmación sobre signos de W ni una prohibición de otras representaciones.

## 1. Altura espectral uniforme

Para N>=1,k>=0 y u>0 la densidad de probabilidad espectral normalizada es

    p_(N,k,u)(tau)=1/[u B(k+1/2,N−1/2)]
       ·(tau/u)^(2k)/[1+(tau/u)²]^(N+k).

En tau=0 se toma el límite habitual cuando k=0. Su máximo está en tau²/u²=k/N. Defina h_N(k)=u sup p_(N,k,u), permitiendo k real>=0 sólo para demostrar la comparación. Para k>0,

    d log h_N(k)/dk
      =psi(k+N)−psi(k+1/2)+log[k/(k+N)].

Por convexidad de (x+t)^−2 en cada intervalo [j−1/2,j+1/2], para x>1/2,

    psi'(x)=sum_(j>=0)(x+j)^−2
       <=int_(-1/2)^infinito(x+t)^−2dt=1/(x−1/2).

Integrar entre k+1/2 y k+N prueba

    d log h_N(k)/dk
      <=log[(k+N−1/2)/(k+N)]<0.

La continuidad al llegar a k0 da

    sup p_(N,k,u)<=Gamma(N)/[u sqrt(pi) Gamma(N−1/2)].

Si G tiene densidad gamma de parámetro N−1/2, la razón de funciones gamma es E sqrt(G). Cauchy–Schwarz da E sqrt(G)<=sqrt(EG)=sqrt(N−1/2)<sqrtN. Así para TODO N,k,

    sup p_(N,k,u)<sqrtN/[u sqrt(pi)].                    (HEIGHT)

No se usa ninguna estimación asintótica ni un barrido en N o k.

## 2. Obstrucción cuantitativa del cono positivo

Fije C>0 y restrinja u>=C sqrtN. Por HEIGHT,

    p_(N,k,u)(tau)<=1/[C sqrt(pi)].

Toda mezcla positiva normalizada, finita o integral, satisface la misma cota por Tonelli. En I=[−C/8,C/8] su masa es como máximo1/(4sqrt(pi))<1/4.

En cambio fije u0=63/2 y considere la densidad objetivo p_(M,0,u0), un átomo permitido del puente017. Para M>=2,

    E tau²=u0²/(2M−3).

Elija un entero M tal que 2M−3>256u0²/C². Chebyshev da

    int_(fuera de I) p_(M,0,u0)<1/4,
    int_I p_(M,0,u0)>3/4.

Por tanto, para toda mezcla positiva normalizada q del dominio u>=C sqrtN,

    ||p_(M,0,u0)−q||_L1
       >=abs(int_I[p_(M,0,u0)−q])>1/2.                 (GAP)

La misma conclusión impide aproximaciones por conos no normalizados cuya masa tienda a1: normalizarlas conservaría cualquier supuesto límite L1. El uso de un intervalo evita inferir una obstrucción L1 a partir de valores en un solo punto.

## 3. Alcance exacto frente al objetivo

La positividad que se pruebe para todos N con u>=C sqrtN es una región real e infinita de la tabla de parámetros. GAP demuestra que NO basta trasladar automáticamente el puente positivo de densidades017 a esa región restringida. Hay átomos admisibles de tasa fija que no pueden aproximarse en L1 mediante ese cono.

No se afirma que la positividad de esa región sea inútil, que una identidad con estructura adicional sea imposible ni que W tenga valores negativos. Tampoco se excluyen otros tipos de aproximación, extrapolación o control directo. El objetivo global sigue requiriendo nueva información para N/u² grande y para las cancelaciones aritméticas correspondientes.
