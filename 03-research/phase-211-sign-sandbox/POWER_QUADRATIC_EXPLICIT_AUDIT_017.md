# POWER_QUADRATIC_EXPLICIT_AUDIT_017 — Revisión independiente del cono eta=15

Veredicto: APROBADO, PROVED. Se leyó íntegramente POWER_QUADRATIC_EXPLICIT_017, su antecedente QUADRATIC017 y el verificador; se reejecutó el verificador con salida PASS. No se detectaron defectos. No modifica papers.

## 1. Densidad desplazada y medida normalizada

La identidad de módulo es exacta: con y²=x²+eta²,

    |u²+(x+i eta)²|²=(u²+y²)²-4u²eta².

El numerador tiene módulo y^{2k}; esto produce el factor (1-aT²)^(-M/2), a=400/441. En |x|>=eta el jacobiano es <=sqrt2<2. Al contar ambos semiejes y dividir por I=2∫_0^infinito rho, el factor principal es exactamente 2 veces una esperanza beta; no se pierde otro factor dos.

## 2. Dos estimaciones logarítmicas distintas

La estimación cercana usa -log(1-z)<=z/(1-z), y

    aM/[2k(1-a)]<=202/41<5.

Con T<=32N/k y k>=10000N², el exponente es <=64/125, cuya exponencial es <=125/61 por la serie geométrica. Para la cola se conserva la expresión original: convexidad de -log y f(0)=0 implican f(aT²)<=a f(T²)<=a f(T). Así el exponente de la nueva beta es k/2, no 5k; su parámetro a'=k/2+1/2 sigue positivo.

La razón de normalizaciones es <=exp(N²/k)2^N. Markov con el momento N da (1/8)^N. Su producto es <=exp(1/10000)4^-N<=625/9999 para N>=2. Todas las constantes y direcciones de desigualdad son correctas.

## 3. Región pequeña y cierre del contorno

El segmento |x|<=eta tiene longitud 2eta y utiliza |x+i eta|²<=2eta². Esto da exactamente A=441/341 y r=200/341. La cota beta inferior de QUADRATIC017 es válida aquí, pues k>=4N. Para t=k/N>=100, la función t/4-log(2t) crece, y en t=100 ya supera logA+2 usando log200<6 y logA<1. Por tanto los factores de normalización cuestan menos que exp(k/4).

Como r<3/5 y log(5/3)>1/2 (primer término atanh, con resto positivo), r^k<exp(-k/2). La contribución pequeña es <exp(-k/4)<1/100. Su suma con el segmento principal es <5.

Los polos de rho están en ±iu, fuera de la banda 0<=Im z<=15. El decaimiento racional O(|Re z|^-2N) hace desaparecer las caras verticales, y desplazar hacia arriba para t>=0 da exp(-15t). La simetría cubre t<0. No se usó una cota temporal ponderada que perdiera la compensación entre los dos factores de la densidad.

## 4. Todos los componentes de la forma

CORR15 controla el peine INFINITO: 10Σq^-14<=150/(13*2^14)<1/1000. La ley beta, las dos cotas de digamma probadas en el apéndice principal y pi<4 dan Arch>99/100: sqrt(k/N)>100, u*100/8>3^5>exp5 y 1/(2k)<1/100. El bound polar previo 400^-k es válido sin cambios porque k>=4N, y es menor que 1/1000.

Así W/||f||²>99/100-2/1000>49/50, para todos N>=2,k>=10000N². La prueba es uniforme en esos índices y suma todos los contactos. No afirma el resultado para numeradores arbitrarios ni para el interior k<10000N².

La revisión del memo principal QUADRATIC017 tampoco encontró defecto en su beta tilt .99k, región pequeña, aproximación gaussiana y paso a la serie infinita; la extensión explícita tiene su propio cierre de signo independiente de una suposición de oscilación favorable.
