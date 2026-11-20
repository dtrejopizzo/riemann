# POWER_DESCENT_016 — Defecto complementario, localización binomial y obstrucción precisa al descenso sólo estructural

Estado: PROVED (identidades completas, monotonía eventual de diferencias, localización de masa y falsificador de la inferencia estructural). Descenso aritmético global OPEN. Papers intactos.

## 1. Estado previo, corpus y razón nueva

Leídos POWER_STATE_015, POWER_HIGHPASS_015, POWER_GEOMETRIC_TRANSFER_015 y el índice/grid/crucigrama, buscando complementary filters, binomial mixtures/partitions, descent y constant shifts. Se conserva el signo global de ocho polos y la positividad eventual para todo orden fijo. No se interpreta esa cola como positividad de los pasos iniciales.

La diferencia nueva frente a 015 es calcular el DEFECTO exacto entre pasos high-pass, incluyendo el polar, y localizar cuantitativamente la masa de su refinamiento binomial. Esto permite probar qué parte de una tentativa de descenso está realmente controlada y cuál no. Las identidades de filtros no se presentan como una propiedad aritmética exclusiva.

## 2. Identidad complementaria con el polar completo

Fije u>1, Q(s)=s/(s+u), L(s)=u/(s+u). En el eje de Fourier,

    |Q(i tau)|²+|L(i tau)|²=1.

Además, poniendo a=1/2,

    Q(-a)Q(a)+L(-a)L(a)
       =[-a²+u²]/[u²-a²]=1.

Por tanto la misma partición vale EXACTAMENTE para la forma completa:

    W[f]=W[Qf]+W[Lf].                                    (DEF)

La parte arquimediana y cada contacto se verifican multiplicando sus integrandos espectrales; el polar usa la segunda identidad. Las sumas de contactos convergen absolutamente en la clase racional considerada. También se cumple la identidad para la norma L2. No se ha supuesto que W[Lf] sea no negativa.

Los filtros conmutan. Iterar (DEF) m veces da

    W[f]=Σ_{j=0}^m binom(m,j)W[Q^j L^{m-j}f],             (BIN)

y la misma fórmula para ||f||². Se incluyen todos los cruces a través de la identidad de filtros; no es un argumento de positividad de sumandos.

## 3. Resultado positivo adicional: diferencias finitas eventualmente positivas

Para f en V_N, sea a_k=W[Q^k f] y Δa_k=a_{k+1}-a_k. (DEF) implica, para cada entero r>=0,

    (-1)^r Δ^r a_k=W[L^r Q^k f].                          (FD)

Como L^r f=u^r P(s)/(s+u)^{N+r} pertenece a V_{N+r}, el teorema de positividad eventual de 015 prueba que, fijados N y r, el miembro derecho es positivo para k suficientemente grande, uniformemente sobre todos los numeradores de V_N. En particular a_k es eventualmente positiva y decreciente, y converge a cero por la convergencia fuerte ya probada.

Este enunciado es una monotonía de los VALORES CUADRÁTICOS SIN NORMALIZAR en la cola, no una monotonía global de los cocientes Rayleigh. Cada orden r tiene su propio umbral; no se ha probado un umbral común para todos r,N ni descenso hasta k=0.

Telescopar r=1 también da

    W[f]=Σ_{k>=0}W[LQ^k f],
    ||f||²=Σ_{k>=0}||LQ^k f||².

La serie de energías converge absolutamente: su cola es positiva por 015 y las sumas parciales convergen a W[f] por (DEF) y Q^k f->0 en norma fuerte. El prefijo finito todavía puede contener valores cuyo signo no está demostrado.

## 4. Localización binomial exacta: la cola conocida ocupa un borde de masa nula

Para f no nula, defina la probabilidad espectral dmu=|F(i tau)|²d tau/(2pi||f||²) y

    p(tau)=tau²/(u²+tau²),
    nu_m(j)=binom(m,j)||Q^j L^{m-j}f||²/||f||².

Entonces nu_m es una probabilidad sobre j=0,...,m y tiene la representación EXACTA

    nu_m(j)=∫binom(m,j)p(tau)^j[1-p(tau)]^{m-j}dmu.       (LAW)

Condicionada a tau, j es una variable binomial de m ensayos y parámetro p(tau). En consecuencia, para toda función Lipschitz phi sobre [0,1],

    |Σ_j nu_m(j)phi(j/m)-∫phi(p(tau))dmu|
       <=Lip(phi)/(2sqrt m).                              (LOC)

Prueba: la varianza condicional de j/m es p(1-p)/m<=1/(4m), y se aplica Cauchy--Schwarz. Así la ley de j/m converge a la imagen de la MEDIDA ESPECTRAL REAL de f por p; no se acumula automáticamente en j/m=1.

Para cada R fijo,

    Σ_{m-j<=R}nu_m(j)->0.                                 (EDGE)

En efecto p(tau)<1 para todo tau finito; la probabilidad binomial de tener a lo sumo R fracasos tiende a cero para cada p<1, y se aplica convergencia dominada. La afirmación es uniforme sobre la esfera unitaria de cualquier V_N fijo: el operador multiplicador del evento está entre 0 y 1, converge puntualmente a cero, y su compresión de dimensión N tiene traza que tiende a cero; su norma está acotada por esa traza.

La relación con 015 es precisa. El término de (BIN) con m-j=r fijo es Q^{m-r}(L^r f), cuyo orden base es N+r. Fijado R, 015 hace positivos todos los términos del borde r<=R para m suficientemente grande. Pero (EDGE) prueba que ese borde tiene PESO NORMALIZADO TOTAL que tiende a cero. En el interior j/m≈theta<1, el orden base N+m-j también crece: 015 no proporciona allí un umbral uniforme.

Esto no demuestra que los términos interiores sean negativos; demuestra que conocer sólo los bordes eventualmente positivos no controla por masa el resto de (BIN). La información pendiente permanece en la región macroscópica descrita por la medida p_#mu, que depende del numerador.

### También desaparece la contribución energética de un borde fijo

Para f=P/(s+u)^N fijo no nulo, ponga d=grado P y r0=N-d>=1. Los asintóticos de norma y cociente completo de POWER_HIGHPASS_015 dan, para cada r fijo,

    ||Q^{m-r}L^r f||²=O(m^{-(r0+r-1/2)}),
    W[Q^{m-r}L^r f]/||Q^{m-r}L^r f||²=O(logm).

Como binom(m,r)=O(m^r), resulta

    Σ_{r=0}^R binom(m,r)W[Q^{m-r}L^r f]
       =O(m^{1/2-r0}logm)->0.

Por tanto los términos positivos que controla directamente 015 sobre un número fijo de diagonales superiores no sólo tienen peso normalizado nulo: su contribución energética TOTAL también desaparece. El interior de (BIN) conserva la energía inicial. No se infiere su signo de esta localización.

## 5. Falsificador exacto al descenso que usa únicamente identidades y cola

Observación del constructor principal. Modifique sólo la constante de la parte arquimediana:

    W_4[f]=W[f]-4||f||².

El peine entero y el polar permanecen idénticos. Como la norma satisface todas las particiones, W_4 conserva EXACTAMENTE (DEF), (BIN), las mezclas geométricas y sus normalizaciones. También conserva el teorema de positividad eventual de 015: el cociente high-pass crece al menos (logk)/2-C_N, y restar 4 no altera su divergencia positiva. Por tanto también conserva todas las conclusiones eventuales de (FD).

Sin embargo, para f(y)=exp(-63y/2)1_{y>0}, la fórmula completa exacta da

    W[f]/||f||²=2L(32)<3,
    W_4[f]/||f||²<-1.

La cota es elemental: psi(16)=H15-gamma<H15, logpi>1 y zeta'(32)/zeta(32)<0. Por tanto 2L(32)<H15-1+1/16+2/31<3, y esta última comparación racional está verificada en tools/power_descent_016_verify.py. Se incluyen TODOS los contactos a través del signo exacto de la serie convergente de zeta'/zeta; no se emplean aproximaciones de constantes especiales.

Queda FALSIFIED la inferencia «particiones exactas completas + mezcla positiva + positividad eventual uniforme en cada orden fijo implican positividad inicial». Todos esos enunciados son verdaderos para W_4, pero su dato inicial explícito es negativo. Esta clase de descenso debe usar alguna estimación cuantitativa adicional que distinga el multiplicador real del desplazado. Incluso conservar exactamente Lambda no basta si su interacción con la constante arquimediana no aparece en esa estimación.

NO es un contraejemplo a la forma W del paper: W_4 es una forma modificada explícitamente. Tampoco se descarta un descenso que controle W[Lf] con el dato aritmético completo o utilice la distribución espectral del numerador. El resultado excluye sólo la inferencia basada en las propiedades estructurales y la cola ya disponibles.

## 6. Obligación que queda después del defecto exacto

El defecto W[f]-W[Qf] es la forma COMPLETA de Lf. Ni el filtro L estable, ni Lambda>=0, ni el signo de la cola high-pass prueban su positividad en los primeros pasos. Una nueva desigualdad de descenso tendría que controlar este bloque de baja frecuencia con el multiplicador real y las autocorrelaciones aritméticas, o acoplarlo explícitamente con el bloque high-pass; asumir ese signo reintroduce la obligación pendiente.

La localización (LOC) ofrece una restricción concreta para esa desigualdad: debe actuar sobre el interior j/m, no sólo sobre un número fijo de diagonales de la cola eventualmente positiva. Esta nota no aporta aún ese control aritmético y no declara cierre global.
