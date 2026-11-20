# POWER_AUDIT_004 — Movimiento de polos y cierre de dimensión tres

Estado: PROVED movimiento de polos, pérdidas exteriores, certificado confluente y signo de toda terna de potencias con exponentes >=32; revisión completa independiente. Papers intactos. Revisión de una construcción de dimensión fija; no se extrapola al orden arbitrario.

## 1. Movimiento de polos: prueba desde cero

Sea fhat(tau)=P(i tau)/prod_j(u_j+i tau), donde P es un polinomio de grado menor que n y u_j>0. Esta representación describe el span de n exponenciales si los polos son distintos y el correspondiente espacio confluyente si se repiten. Si v_j>=u_j para cada j, mantener P y reemplazar u_j por v_j multiplica |fhat|² por

    R(tau)=prod_j (u_j²+tau²)/(v_j²+tau²).

Cada factor es no decreciente en |tau|, por derivación directa. Para la medida de probabilidad p=|fhat|²/(2pi||f||²), el cociente arquimediano nuevo es E_p[mR]/E_p[R]. Como m y R son funciones no decrecientes de |tau|,

    Cov_p(m,R)=1/2 integral integral (m(t)-m(s))(R(t)-R(s)) dp(t)dp(s)>=0.

Las integrales convergen: las funciones racionales tienen cola O(1/tau), m=O(log(2+|tau|)) y R está acotado. Por tanto el cociente arquimediano no disminuye al aumentar cualquiera de los polos, para cada P fijo. Tomar ínfimo sobre TODOS los polinomios P del mismo grado permitido preserva esta comparación. En particular, para n<=3 y todas las tasas >=u, basta controlar el espacio confluyente de tasas u,u,u. No se usa una comparación punto a punto de matrices ni se supone que los coeficientes exponenciales permanezcan fijos.

## 2. Norma ponderada uniforme: constante 1302

En la base racional ortonormal de Malmquist ordene las tres tasas v_j>=u. Cada vector se obtiene aplicando j factores all-pass a sqrt(2v_j)e^(-v_j y). Para la norma ponderada ||e^(uy/2)f||_2, el primer vector tiene norma <=sqrt(2), pues 2v_j/(2v_j-u)<=2. El núcleo de cada factor all-pass es delta_0-2v e^(-vy), y después de ponderar su norma total de variación es

    1+2v/(v-u/2)<=5.

Young para convolución y Cauchy--Schwarz en los coeficientes ortonormales dan

    ||e^(uy/2)f||² <=2(1+25+625)||f||²=1302||f||².

La misma cota cubre dimensión uno o dos. No exige cota superior ni separación de las tasas, y admite directamente factores repetidos. Por restricción al intervalo [t,infinito),

    ||f 1_[t,infinito)|| <=sqrt(1302)e^(-ut/2)||f||.

## 3. Pérdidas de peine y polar a u>=63/2

Por Cauchy--Schwarz para la autocorrelación y la norma de cola,

    |comb|/||f||² <=2sqrt(1302) sum_{n>=2}Lambda(n)n^(-(u+1)/2).

Como u>=31.5, el exponente es >=16 y Lambda(n)<=log n. Comparación integral de log x/x^16, decreciente para x>=2, da

    sum log(n)n^-16 <=2^-16 log2+2^-15[(log2)/15+1/225]
                     <2^-16[1+2/15+2/225].

Usando 2sqrt(1302)<74, el peine es <.002||f||², mediante racionales únicamente.

Para los momentos A=integral f e^(y/2), B=integral f e^(-y/2),

    2AB >=-(A-B)²/2,
    integral_0^infinito 4sinh²(y/2)e^(-uy)dy=2/[u(u²-1)].

Cauchy--Schwarz ponderado implica

    polar >=-1302/[u(u²-1)]||f||²>-.042||f||²

para u>=63/2. La última comparación es racional: 1302/[u(u²-1)] en u=63/2 vale 10416/249795<21/500.

## 4. Obligación arquimediana y consecuencia condicional

Si la forma arquimediana sobre span{e^(-63y/2), y e^(-63y/2), y² e^(-63y/2)} es >=.1||f||², §1 la transporta a todo span de hasta tres exponenciales con tasas >=63/2. Las cotas independientes §§2–3 darían entonces

    W(f)>(.1-.042-.002)||f||²=.056||f||².

Esto cerraría el signo de todos los triples de potencias a_i>=32, incluyendo tasas arbitrariamente próximas o muy separadas. La cota confluente concreta queda revisada y aprobada en §5; por tanto esta conclusión es PROVED. El resultado de dimensión tres no implica el signo en dimensión arbitraria ni el cierre del paper.

## 5. Certificado confluente recibido y verificado: PROVED

Se revisó POWER_CONFLUENT_004.md desde el kernel arquimediano y se ejecutó independientemente su bloque Python de Fraction: todos los asserts racionales pasan. Los coeficientes se comprueban sin inferirlos desde diagonales: para p(u)=[psi((u+1/2)/2)-log pi]/2, la entrada entre la exponencial y su primer Laguerre es 2up'(u), y la entrada con el segundo es 2u[p'(u)+up''(u)]. Las diagonales iguales y la repetición de la primera banda resultan también del producto de las bases racionales all-pass. Así d=psi(16)-log pi, b=(63/4)psi'(16), c=b+(3969/16)psi''(16) son correctos.

Las cotas de gamma<H256-log256, pi<22/7, la serie atanh con r=1/3 para log2 y r=15/29 para log(22/7), y las colas integrales de S2/S3 son válidas con las direcciones declaradas. Producen d>159/100, 0<b<51/50, |c|<1/50. La cota final de la matriz es estrictamente mayor que

    159/100-(10/7)(51/50)-1/50=79/700>1/10.

Por §§1–4 queda probado Q[f]>(7/125)||f||² para las tres exponenciales con tasas arbitrarias >=63/2, usando nuestras pérdidas <.002 y <.042. La afirmación conservadora Q>=||f||²/20 del memo principal queda por tanto aprobada. Confluencia y ausencia de separación mínima no introducen un límite sin justificar: los espacios racionales y las bases permiten polos repetidos directamente.

## 6. Revisión del memo principal de movimiento

POWER_POLE_MOVEMENT_004.md §§2–5: APROBADO. Su formulación para todas las eigenenergías, además del mínimo, sigue del min–max en el mismo espacio vectorial de numeradores P, pues la comparación de Rayleigh es punto a punto para todo P. La derivada de Rayleigh conserva el término de normalización y tiene el signo correcto. Su cota algo más gruesa del peine <3/1000 es válida (74/28672<3/1000) y conduce al margen 11/200>1/20. No afecta la aprobación usarla en lugar de la cota .002 de esta auditoría.

La construcción consigue signo de dimensión tres para TODO el rango a_i>=32; no extrapola a todos los órdenes. En particular no se afirma que el bound ponderado B_n=(25^n-1)/12 se mantenga uniforme ni que la parte arquimediana confluente conserve su margen al crecer n.
