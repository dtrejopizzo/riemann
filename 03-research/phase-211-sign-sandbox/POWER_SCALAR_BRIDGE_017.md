# POWER_SCALAR_BRIDGE_017 — Dos índices escalares bastan para todos los bloques

Estado: PROVED, revisión formal independiente por mapa; auditoría final en POWER_INTERIOR_AUDIT_017. No prueba todavía el signo de la familia escalar. Papers intactos.

## 1. Corpus y diferencia explícita

Consultados ROUTES-TRIED-INDEX, grid maestro, CROSSWORD-TO-D y POWER* buscando Bernstein, grado elevado, coeficientes positivos, partición y puente. Los usos registrados de Bernstein para medidas completamente monótonas, cotas de funciones enteras y límites de frecuencia no son este argumento. POWER_DESCENT016 localiza el interior binomial pendiente; CONFLUENT_BRIDGE014 demuestra suficiencia de todos los bloques, y JOINT_SCALE016 da coordenadas beta para sus sectores. No se reintenta inferir positividad de una envolvente lineal desde una unión de familias positivas.

La diferencia es una identidad FINITA de densidades racionales con coeficientes positivos obtenida por elevación de grado, después de una perturbación arbitrariamente pequeña. La identidad conserva también el polar por evaluación racional fuera del semieje espectral. El lema polinómico elemental es estándar; la aportación aquí es su aplicación exacta a la forma completa y el control de todos los cruces mediante esa identidad.

Antecedentes locales verificados por el auditor: `03-research/phase-114-closing-the-four-rows/114_d_180_BERNSTEIN_DIRECTED_ENDPOINT_GATE.md` §1 ya usa elevación positiva de grado para integración estable en coordenadas Bernstein; `03-research/phase-72-feshbach-leakage-calculus/E72_259_RATIONAL_BERNSTEIN_LM8_CERTIFICATE.md` certifica desigualdades polinómicas mediante coeficientes Bernstein y subdivisión exacta. Son antecedentes del instrumento, no del puente presente: ninguno de esos dos documentos transforma una densidad racional en el cono de átomos monomiales ni conserva explícitamente la polar por evaluación en x=-1/4.

## 2. Enunciado suficiente y necesario en los bloques confluentes

Fije u>1; puede tomarse u=63/2. Para N>=1,k>=0, sea h_(N,k) la función causal real de transformada

    H_(N,k)(s)=s^k/(s+u)^(N+k).

Son equivalentes:

(A) W[h_(N,k)]>=0 para todos N>=1,k>=0.
(B) W[f]>=0 para toda F(s)=P(s)/(s+u)^M, M>=1, P real, grado P<M.

B implica A inmediatamente. La demostración de A implica B ocupa §§3–5. Por CONFLUENT_BRIDGE014, A basta para el signo de todos los tests del portador declarado y, mediante el puente ya probado, el objetivo del Paper47. No se presupone A: sigue OPEN.

La condición A utiliza sólo un numerador monomial y DOS índices. No se ha reducido a la sola cadena k0, ni a N fijo, ni a los extremos eventualmente positivos de015.

## 3. Toda densidad racional es un polinomio no negativo sobre un peso común

Para F=P/(s+u)^M, ponga x=tau² y

    S(x)=P(i sqrt(x))P(-i sqrt(x)),
    q=x/(u²+x), F1(s)=1/(s+u).

S es un polinomio real de grado<=M−1, no negativo para x>=0. La identidad racional es

    |F(i tau)|²=|F1(i tau)|² R(q),
    R(q)=u^(2−2M)(1−q)^(M−1) S(u²q/(1−q)).           (R)

R es un polinomio real de grado<=M−1. Es no negativo en [0,1): todos los factores de (R) son no negativos allí. Por continuidad polinómica lo es también en1. Su valor en1 es cero si gradoP<M−1, y el cuadrado del coeficiente principal si gradoP=M−1. No se exige positividad estricta ni ausencia de raíces interiores.

## 4. Lema elemental de elevación de grado con umbral explícito

Sea R(q)=sum_(l=0)^d r_l q^l y R>=0 en [0,1]. Para epsilon>0, elija un entero D>=d. La expansión EXACTA de R+epsilon en la base Bernstein de grado D es

    R(q)+epsilon=sum_(j=0)^D b_(D,j) binom(D,j)q^j(1−q)^(D−j),
    b_(D,j)=epsilon+sum_(l=0)^d r_l (j)_l/(D)_l.      (BER)

Se entiende (j)_0/(D)_0=1 y (j)_l=0 para j<l. La fórmula se prueba contando subconjuntos marcados de tamaño l en una variable binomial, o expandiendo la identidad de su momento factorial.

Uniformemente en j,

    |(j)_l/(D)_l − (j/D)^l| <=l(l−1)/(2D).

Prueba elemental: extraer l índices uniformes con reemplazo de un conjunto de D, con j índices marcados. La probabilidad de que todos estén marcados es (j/D)^l. Condicionado a que no se repitan índices, es (j)_l/(D)_l. La diferencia entre ambas probabilidades es a lo sumo la probabilidad de alguna repetición, acotada por l(l−1)/(2D). Para l0 y l1 la igualdad es exacta.

En consecuencia, definiendo

    C_R=(1/2)sum_l |r_l|l(l−1),

se tiene b_(D,j)>=epsilon+R(j/D)−C_R/D. Si D>=max(d,1) y D>C_R/epsilon, TODOS los coeficientes son estrictamente positivos. El procedimiento es efectivo para cada R y epsilon. No se confunde el polinomio de Bernstein aproximante con la representación EXACTA por elevación de grado.

## 5. Identidad de la forma COMPLETA, incluido el polar

Defina Q=s/(s+u), L=u/(s+u), y g_(D,j) por

    G_(D,j)=Q^j L^(D−j) F1
            =u^(D−j)s^j/(s+u)^(D+1).

Es un múltiplo real positivo del átomo h_(D+1−j,j). En el eje espectral,

    |G_(D,j)|²=|F1|² q^j(1−q)^(D−j).

Multiplicar (BER) por |F1|² y usar (R) da

    |F|²+epsilon|F1|²
      =sum_j b_(D,j)binom(D,j)|G_(D,j)|².            (DEN)

Las partes arquimediana y de cada contacto son lineales en estas densidades, de modo que satisfacen DEN. Todas las series aritméticas convergen absolutamente para cada una de las funciones racionales de esta identidad finita; no se intercambia un límite de grado con una serie no controlada.

Para el polar, léase DEN como identidad racional en x. En x=−1/4, los denominadores no se anulan porque u>1, y

    F(i sqrt(x))F(-i sqrt(x))=F(-1/2)F(1/2).

La identidad es algebraica y no depende de elegir una rama: cada producto es racional en x. Multiplicar su evaluación por2 produce EXACTAMENTE la identidad de los polares. Aunque q=−1/(4u²−1) es negativo allí, los coeficientes b_(D,j) siguen siendo los mismos números positivos; no se atribuye signo separado al valor del polar.

Se concluye la identidad completa

    W[f]+epsilon W[f1]
      =sum_j b_(D,j)binom(D,j) W[g_(D,j)].            (FORM)

FORM es una igualdad de valores cuadráticos; el lado izquierdo NO es W[f+sqrt(epsilon)f1]. No se omitió ningún término cruzado: todos los cruces del numerador P ya están en S y R.

Bajo A, cada sumando derecho es no negativo. Por tanto W[f]>=−epsilon W[f1]. Hacer epsilon->0 prueba W[f]>=0. No se necesita un margen uniforme, una topología de aproximación de funciones, ni convergencia fuerte de g_(D,j).

## 6. Extracción finita de un átomo negativo, si existiera una dirección negativa

La prueba también es constructiva por contraposición. Si W[f]=−delta<0, elija epsilon>0 de modo que epsilon |W[f1]|<delta/2, y D>=max(d,1), D>C_R/epsilon. Entonces el lado izquierdo de FORM es negativo. Como todos los coeficientes son positivos, al menos uno de los D+1 átomos h_(D+1−j,j) tiene W negativo.

Esto no construye un contraejemplo real: no se conoce una dirección inicial negativa de W. Precisa que cualquier fallo en una matriz completa tendría un testigo escalar monomial a algún orden finito explícitamente acotable desde ese fallo. La representación permite tratar los cruces sin asumir que una unión de subespacios positivos sea positiva.

## 7. Relación exacta con016 y obligación pendiente

No hay contradicción con la obstrucción de momentos de016: aquí no se aproxima f mediante una sucesión high-pass. Se representa su densidad, con una perturbación de energía arbitrariamente pequeña, mediante un cono positivo de densidades; la identidad racional conserva el polar.

Tampoco basta EVENTUAL015. El triángulo de FORM contiene átomos con ambos índices variables, incluidos los iniciales. La masa y energía que016 localiza en el interior no están cubiertas por colas de dimensión fija. El blanco suficiente queda ahora explícito: probar el signo de toda la tabla escalar W[h_(N,k)] con el dato aritmético completo. Sólo identidades y colas siguen sin decidir esa tabla, como muestra el falsificador W4 de016.
