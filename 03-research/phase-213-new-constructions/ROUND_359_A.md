# Criterio con el producto entero libre de primos pequeños

Sea Q_{z,h} la parte de P_h de 353 con p>z y con todos los factores primos de m mayores que z, incluido el caso m=1. Entonces RH equivale a

    ‖Q_{z,h}‖_Y ≪_η √(hY) Y^η

para cada η>0, todo Y grande, 0<h≤1 y uniformemente en (log Y)²≤z≤4(log Y)². Ahora es el entero completo n=pm el que debe carecer de primos pequeños. La familia de cortes tiene anchura multiplicativa cuatro; no se afirma aquí la equivalencia para un solo corte exacto de ambos factores.

**Identidad.** Escribir T_d para la dilatación de 357, L_z=Σ_{p≤z}(log p)T_p, K_z=Σ_{d z-liso}T_d y U_z=Σ_{d z-liso}μ(d)T_d. A corte fijo se tiene

    Q_z=K_z(P−L_z S),      P=L_z S+U_z Q_z.

En efecto L_z retira la etiqueta prima exterior, y K_z borra los factores de Euler del cofactor por la identidad de 357. Bajo RH las normas críticas de S y P se conocen por 353. En la norma de exponente σ=1/2+ε, el coste de K_z es ≤∏_{p≤z}(1−p^(−σ))^(−1)=Y^o(1) y el de L_z es polilogarítmico. Empezar con una pérdida menor que η y usar cuentas triviales en escalas acotadas prueba la dirección directa.

**Recuperar la suma.** Fijar 0<ε<1/4, σ=1/2+ε, y sea A(X) el supremo de ‖S_h‖_Y/(√(hY)Y^ε) para 1/2≤Y≤X y 0<h≤1. Es finito por 353. En lo que sigue todos los costes en el bloque X están normalizados por √(hX)X^ε. Tomar z=(log X)². El término L_z S cuesta a lo sumo

    A(X) Σ_{p≤z}(log p)p^(−σ) = O_ε(A(X)(log X)^(1−2ε)),

por Chebyshev y sumación parcial. Esto es o(A(X)log X).

Para d≤√X en U_z Q_z, el bloque Y=X/d satisface (log Y)²≤z≤4(log Y)². Aplicar la hipótesis con η=ε/2. El coste total normalizado de estas ramas es O(X^(−ε/2)∏_{p≤z}(1+p^(−1/2−ε/2)))=O(1).

Para los demás d necesitamos una estimación previa que pueda depender de A(X). En cada Y≤X con Y≥1/2, la identidad de 353 acota P en norma de exponente σ por O_ε(A(X)log(2X)): las potencias superiores suman Σ_{p,k≥2}(log p)p^(−kσ)<∞ y la integral de anchuras cuesta O(1). La misma estimación basta para L_z S. El operador K_z a este exponente cuesta X^o(1) incluso si el bloque hijo es pequeño, pues el corte z sigue congelado en el del padre. Así Q_z en cada hijo cuesta A(X)X^o(1) en su propia norma normalizada. Las escalas por debajo de 1/2 no aportan. El transporte de regreso al padre para d>√X tiene coste

    Σ_{d>√X, z-liso} μ²(d)d^(−σ)
       ≤ X^(−ε/4)∏_{p≤z}(1+p^(−1/2−ε/2)) = X^(−ε/4+o(1)).

Por tanto todo P cuesta O(1)+o(A(X)log X) en el bloque X. Reinsertar en la identidad de 353 y dividir por log X−1; a exponente σ los demás costes son O_ε(A(X)) antes de la división. Se obtiene una constante más o(1)A(X) para la norma normalizada de S_h. Aplicar bloque por bloque para Y≤X, eligiendo un umbral fijo a partir del cual el coeficiente es ≤1/2, y tomar el supremo: A(X) queda acotado uniformemente. Como ε puede ser arbitrariamente pequeño, la implicación inversa de 353 da RH.

**Qué cambia.** 358 elimina primos del cofactor mediante inversión. El mismo coste de Euler aplicado sin más a L_z S puede superar el margen de absorción. Aquí el término de primos exteriores pequeños se saca antes de invertir; sólo las ramas largas usan la envolvente A, y el peso extra en esas ramas paga su coste de Euler. Queda la estimación incondicional de la suma sobre productos enteramente cribados.
