# POWER_CENTERED_CUTOFF_049 — Corte efectivo j=14 por integración por partes

Estado: **PROVED, revisión independiente APROBADA en POWER_R12_AUDIT_049.md y prueba revisada por root.** Cota de momento y ARCH para TODA la órbita Q^j V12, j>=14. Este lema aislado no prueba signo global de W ni R12; su ensamblaje con el segmento finito está en POWER_R12_TRANSPORT_049.md. Papers intactos.

## 1. Corpus y razón nueva

Consultados ROUTES-TRIED-INDEX/README, grid maestro, CROSSWORD-TO-D, HIGHPASS015 y R12_ENDPOINT048; búsqueda de Jacobi, Gegenbauer, Bernstein ponderada e inverse frequency. JOINT_SCALE016 y DESCENT_AUDIT016 ya contienen coordenadas Jacobi para sectores racionales; no se presentan como nuevas. HIGHPASS015 prueba positividad eventual uniforme a dimensión fija, pero sin corte efectivo. ENDPOINT048 da j=1 y una cola polar efectiva, dejando abierto ese corte.

La diferencia es una desigualdad FINITA cuantitativa de momento inverso para TODOS los numeradores de dimensión12 y TODOS j>=14. Se prueba con integración por partes y un bound polinómico ponderado demostrado abajo. No es una campaña de índices, ni un asintótico sin constante, ni una afirmación de uniformidad al crecer la dimensión.

## 2. Enunciado

Sea P un polinomio complejo no nulo de grado<=11 sobre el círculo, y

    q=(2+z+zbar)/4,
    dmu_j=q^j |P(z)|² dtheta / int q^j |P(z)|² dtheta.

Para TODO entero j>=14,

    E_mu_j[(1-q)/q] < 49/20.                              (MOMENT)

En la correspondencia exacta de ENDPOINT048, z=(i tau-u)/(i tau+u), u=63/2, se tiene q=tau²/(u²+tau²). Por tanto, para TODO F0!=0 en V12 y G=Q^j F0,

    E_G[tau^(-2)] < 1/405 < 1/400.                       (INVERSE)

La medida E_G es |G(i tau)|² d tau/(2pi ||G||²). Se permiten todos los coeficientes complejos; en particular se cubren los reales.

## 3. Bound polinómico ponderado, con prueba

Para a>0, w_a(y)=(1-y²)^a en[-1,1], y un polinomio p de grado<=d, defina

    M=int w_a |p|²,
    D=d(d+2a+1).

Se tiene

    int (1-y²)w_a |p'|² <= D M.                          (BERNSTEIN)

Prueba elemental: L_a p=-(1-y²)p''+(2a+2)yp' preserva cada espacio de polinomios de grado<=n. La integración por partes muestra que es simétrico en L²(w_a), y que su forma es el lado izquierdo de BERNSTEIN; el borde se anula porque a+1>0. Si p_n es el polinomio ortogonal mónico de grado n obtenido por Gram-Schmidt, L_a p_n es ortogonal a todos los grados inferiores por simetría y preservación del grado. Su coeficiente principal es n(n+2a+1). Así p_n es eigenpolinomio con ese eigenvalor. Expandir p en esta base y usar que esos valores crecen con n prueba BERNSTEIN, también para coeficientes complejos. No se requiere una cita externa.

Sea ahora

    r=int [y²/(1-y²)]w_a |p|² / M.

Integrar la derivada de y w_a |p|² da

    2a r = 1 + 2 Re int y w_a p' conj(p)/M
         <= 1 + 2sqrt(rD).                              (IBP)

Los bordes se anulan porque a>0; el integral con singularidad de orden(1-y²)^(-1) es finito por la misma condición. La desigualdad usa Cauchy sobre y p/sqrt(1-y²) y sqrt(1-y²)p', luego BERNSTEIN. Esta es una cota efectiva para TODOS los polinomios del grado indicado.

## 4. Reducción exacta del círculo a dos sectores

Parametrize z=exp(2ix), -pi/2<=x<=pi/2. Entonces q=cos²x. Multiplicar P(exp(2ix)) por exp(-11ix) conserva su módulo y deja solamente frecuencias impares entre-11 y11. Su parte par es una combinación de cos((2l+1)x), y su parte impar una combinación de sin((2l+1)x). Con y=sin x se escribe exactamente

    exp(-11ix)P(exp(2ix)) = cos x R(y)+S(y),

con R par de grado<=10 y S impar de grado<=11, permitiendo coeficientes complejos. Esto sigue de las fórmulas elementales de ángulo múltiple: cos((2l+1)x)/cos x es un polinomio par en sin x de grado2l, y sin((2l+1)x) es un polinomio impar de grado2l+1.

El término cruzado es impar en x, por lo que integra cero tanto en la norma como después de multiplicar por (1-q)/q. Usando dx=dy/sqrt(1-y²), ambos integrales son sumas de dos sectores:

    S: a=j-1/2, d<=11;
    R: a=j+1/2, d<=10.

La razón MOMENT es una mezcla positiva de las razones r de esos dos sectores; un sector idénticamente nulo simplemente se omite.

## 5. Uniformidad en TODOS j>=14 y constantes racionales

En el sector S, IBP implica

    r <= 1/(2j-1) + 2sqrt[11(2j+11)]/(2j-1) sqrt r.

Ambos coeficientes derechos decrecen para j>=14. Para el segundo, basta derivar (2j+11)/(2j-1)²: su derivada es negativa para j>=1. En el sector R se tiene un denominador mayor2j+1 y un D menor10(2j+12)<11(2j+11), así que la misma cota domina ambos sectores. Por tanto, para TODOS j>=14 y ambos sectores,

    27 r <= 1+2sqrt(429r).                               (UNIFORM)

La desigualdad cuadrática en sqrt r obliga r a estar por debajo de su única raíz positiva. Esa raíz es ESTRICTAMENTE menor que b=49/20, pues

    27b-1=1303/20>0,
    (27b-1)²-4·429·b=16129/400>0.

Equivalentemente, el polinomio27t²-2sqrt429 t-1 tiene una sola raíz positiva y es positivo en t=sqrt b. Así cada razón sectorial es menor que49/20, y su mezcla también. Esto prueba MOMENT.

Como u²=3969/4,

    (49/20)/u²=1/405,
    1/400-1/405=1/32400>0,

lo cual prueba INVERSE. No se ha evaluado una matriz de Gram por j ni se ha supuesto un límite uniforme.

## 6. Consecuencia arquimediana efectiva

El bound de digamma usado en QUADRATIC017§6 es

    m(tau)>=log(|tau|/(2pi))-1/|tau|-1/(2tau²), tau!=0.

Jensen para log y Cauchy, aplicados a INVERSE, dan

    ARCH[G]/||G||²
      >= -(1/2)log E_G[tau^-2]-log(2pi)
                   -sqrt(E_G[tau^-2])-(1/2)E_G[tau^-2]
      > log(10/pi)-1/20-1/800
      > 859/800.                                         (ARCH)

Para la última desigualdad basta log(10/pi)>9/8. Es elemental: pi<22/7 da10/pi>35/11. Además exp1<11/4 y exp(1/8)<8/7 implican exp(9/8)<22/7<35/11. El bound de exp1 se obtiene sumando hasta grado3 y dominando la cola desde grado4 por5/96, dando exp1<87/32<11/4; el de exp(1/8) se obtiene de la serie geométrica. Los logaritmos son integrables para estas funciones racionales; cerca de cero basta j>=1, y al infinito el decaimiento racional domina log.

Se ha obtenido un corte arquimediano efectivo J=14 para TODA Q^j V12. El contacto2 y el polar deben sumarse con sus bounds y los índices j<14 deben tratarse aparte antes de concluir una afirmación uniforme de E2 o transporte R12. Este memo no certifica esos índices ni controla la cola completa de los demás primos. Signo global OPEN.
