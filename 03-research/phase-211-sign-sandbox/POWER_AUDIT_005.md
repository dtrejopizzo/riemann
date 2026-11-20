# POWER_AUDIT_005 — Alcance de movimiento de polos al conservar el polar

Estado: PROVED identidad exacta y falsificador de extensión irrestricta; OPEN comparación de orden cuatro en tasas >=31.5. No modifica papers.

## 1. Auditoría de antecedentes del lema arquimediano

Nueva búsqueda dirigida en índice, corpus, grid y crucigrama: pole movement, moving poles, movimiento de polos, covariance/covarianza, numerator fixed/numerador fijo y Rayleigh. No se encontró el lema específico de POWER_POLE_MOVEMENT_004 antes de esta ronda. E85_005_PATH_DECISION.md usa 'moving poles' para resolventes y complementos de paridad, no para polos racionales de funciones de prueba; E101_079 usa la frase para posibles polos móviles de núcleos interpoladores. Tampoco las monotonías por inclusión de subespacios son este resultado: los espacios racionales de polos distintos no están anidados, y la prueba nueva identifica el mismo numerador y compara probabilidades reponderadas.

Novedad defendible: lema específico de monotonía de eigenenergías de un multiplicador par creciente bajo incremento individual de polos reales de denominadores racionales, probado por covarianza. No se atribuye novedad al principio general de covarianza de dos funciones crecientes ni a las bases racionales. La búsqueda local no certifica novedad en toda la literatura.

## 2. Fórmula completa con el término polar

Para polos u_j>1/2 y numerador fijo P, escriba H_u(s)=P(s)/prod_j(u_j+s), transformada de Laplace de f_u. Entonces

    A_u=H_u(-1/2), B_u=H_u(1/2),
    2A_u B_u=2P(-1/2)P(1/2)/prod_j(u_j²-1/4).

Al aumentar u_j a v_j>=u_j,

    R(tau)=prod_j(u_j²+tau²)/(v_j²+tau²),
    r0=prod_j(u_j²-1/4)/(v_j²-1/4).

Si mu es la densidad espectral antigua normalizada y p_u=(2A_u B_u)/||f_u||², la diferencia del cociente arquimediano MÁS polar es exactamente

    E_v-E_u=[Cov_mu(m,R)+(r0-E_mu[R])p_u]/E_mu[R].       (AP)

Esto conserva la normalización de la norma: ||f_v||²=E_mu[R]||f_u||². Omitir ese factor cambiaría la comparación.

Cada factor (u²+t)/(v²+t) es no decreciente para t>-u²; por tanto r0<=R(tau) y r0<=E_mu[R], con desigualdad estricta si algún polo aumenta. Consecuencias comprobadas:

* Si p_u<=0, ambos términos del numerador de AP son no negativos: el movimiento sí preserva el cociente arquimediano+polar para ese numerador.
* Si p_u>0, el segundo término tiene signo opuesto. No se transporta automáticamente el teorema arquimediano a esa parte de la forma.
* La obligación suficiente y exacta para ese numerador es Cov_mu(m,R)>=(E_mu[R]-r0)p_u. Sigue siendo una desigualdad real que puede atacarse; no se declara falsa en el rango relevante de cuatro polos.

No se incluye aquí el peine, cuya variación introduce otro término distinto.

## 3. Falsificador elemental con el dato arquimediano REAL

Dimensión uno, numerador P=1. Para f_u(y)=e^(-uy), u>1/2, el cociente arquimediano+polar es

    E(u)=psi((u+1/2)/2)-log pi+4u/(u²-1/4).

Mover u=1 a v=2 aumenta el polo pero disminuye este cociente. En efecto

    psi(5/4)-psi(3/4)=4-pi,
    4*2/(2²-1/4)-4*1/(1²-1/4)=32/15-16/3=-16/5,
    E(2)-E(1)=4/5-pi<0.

La identidad de psi usa su recurrencia y los valores de reflexión en 1/4,3/4. Este es el multiplicador gamma y el polar exactos de la forma, no un modelo escalar sustituto. No usa cómputo numérico ni barrido.

**Alcance:** refuta la extensión del movimiento arquimediano a arquimediano+polar para TODOS los polos >1/2. Los polos 1,2 están fuera del rango >=31.5; no refuta una comparación de dimensión cuatro en dicho rango, ni el signo de esa familia, ni las cotas probadas para tres.

## 4. Próximo control acotado

Para el próximo teorema de cuatro generadores debe conservarse el polar positivo que rescata el bloque arquimediano bajo, y probarse su comparación por AP o por una desigualdad distinta. La propiedad p_u<=0 ya tiene transporte favorable y no es el sector difícil. Un candidato de movimiento en p_u>0 requiere la cota de covarianza compensatoria; no basta recordar que m es creciente. No se ha buscado un falsificador mediante barrido ni se afirma que lo haya para cuatro tasas >=31.5.

## 5. Certificado de cuatro polos confluentes: revisión completa

POWER_CONFLUENT_FOUR_005.md y el archivo real phase-211-sign-sandbox/tools/power_confluent_four_005_verify.py: APROBADOS. Se ejecutó el verificador con salida PASS. El cuarto coeficiente Toeplitz se comprueba desde el tercer Laguerre: 2up'+4u²p''+(4/3)u³p''' produce exactamente b+(3969/8)psi''(16)+(250047/96)psi'''(16). Los momentos sqrt(63)(-32)^j/31^(j+1) y sqrt(63)(-31)^j/32^(j+1) son la integral Laplace exacta de Laguerre; su producto polar es Toeplitz y racional.

La cota superior de d usa gamma>H256-log256-1/256 y pi>223/71; r=76/147 es exactamente el parámetro atanh de 223/71. Sus direcciones son correctas, al igual que las colas de S2,S3,S4 y los signos alternados de psi'',psi'''. La norma del error Toeplitz está controlada por máxima suma de fila <1/200. Las comprobaciones de LDL y de los dos bloques centrosimétricos son correctas. En LDL la columna del pivote no se modifica durante el paso.

Quedan certificados Arch+Polar>(49/200)I y |Comb|<(13/1000)I mediante B4=32552; por tanto W>(29/125)I>(1/5)I en el espacio confluente de cuatro polos u=31.5. El vector Laguerre (1,-1,1,-1) sí tiene Arch/||v||²<-.1, sin contradecir la compensación polar positiva. No se transfiere este resultado a cuatro tasas arbitrarias mediante el movimiento arquimediano: la advertencia AP de §2 sigue vigente.

## 6. Revisión de la cuártica confluente de transporte

POWER_POLAR_MOVEMENT_005 §§4–5: APROBADOS como identidades y como teorema escalar n=1,u>=8. La comparación de trigamma >=1/x, el bound 16/(17u) y la pérdida <5/u² dan E'>0 en ese rango.

Para verificar D4, ponga f=sum x_j F_j, g=sum x_j F_(j+1), ||x||=1. La derivada de un solo polo con numerador fijo es -(f-g)/(2u), mientras la derivada de la norma es -(1-c1)/u. De ahí

    uE'=inner(g,Mf)-E c1,
    inner(g,Mf)=m1+(m0+m2)c1+(m1+m3)c2+(m2+m4)c3,
    E=m0+2m1c1+2m2c2+2m3c3.

Sustituir da exactamente D4 y cancela m0. Las fórmulas de mk derivadas del kernel y su añadido polar coinciden con los casos hasta orden tres previamente auditados; el mismo desarrollo binomial produce la fórmula general declarada. La cuártica es un objetivo de signo finito real, no una consecuencia automática de las monotonías previas. Los diagnósticos de minimización no se usan en esta aprobación.

## 7. Antecedentes del próximo test aritmético de dimensión doce

La búsqueda local de un test Laguerre confluente específico en tasa31.5 y dimensión doce no encontró antecedente exacto. Hay usos anteriores de Laguerre con objetos diferentes: phase-104/104_46_FIXED_LAGUERRE_MARKOV_EXTREMAL_GATE usa L_(n-1)^(1)(s log d) como vector de transporte por divisores; phase-168/R168_203_LOCAL_LAGUERRE estudia una desigualdad diferencial de funciones enteras. Ninguno es el bloque universal exterior presente.

La necesidad general de una contribución prima cuando crece el número de direcciones arquimedianas negativas ya tiene antecedentes: los conteos negativos del Paper47 y el hecho de que el polar tenga rango finito impiden esperar positividad arquimediana+polar en todos los subespacios crecientes. Por tanto la eventual novedad de un test de dimensión doce debe declararse como vector racional explícito en ESTE espacio, con déficit AP y reparación del peine certificados; no como primer descubrimiento de que hace falta aritmética. Se espera el certificado concreto antes de registrar su signo.

## 8. Certificado SOS local exacto recibido y revisado

POWER_POLAR_MOVEMENT_005§6 y tools/polar_derivative_sos_005.py: APROBADOS y reejecutados con PASS. Las series de psi^(j)(16), j1..4, se suman hasta2000 y sus colas están correctamente entre las integrales desde2001 y2000; la clase intervalar racional I conserva el redondeo exterior. Los cuatro intervalos de radio10^-4 alrededor de (8887,1116,2213,1126)/10000 quedan probados.

El verificador construye la cuártica homogénea Dbar-.08N² y comprueba EXACTAMENTE todos sus coeficientes contra z^TQz. La matriz Q es simétrica y su LDL racional tiene diez pivotes>.2. La actualización in-place conserva las columnas del pivote. Las sensibilidades de D4 respecto de m1,m2,m3,m4 están acotadas por 4N²,4N²,3N²,N² respectivamente usando |c_k|<=N. Por tanto la pérdida total es <.0012N² y D4>.0788N²>.075N².

El factor de derivada se revisó explícitamente: al mover UN polo f'=-f/(s+u), de donde uE'=D4 para norma uno. Mover los cuatro simultáneamente daría CUATRO veces esa derivada. La afirmación individual dE/dv_j>3/(40u)=1/420 en u31.5 es por tanto correcta sin factor omitido. E significa aquí ARCH+POLAR, no incluye el peine. El paso por compactitud a una vecindad común de tasas es válido en el espacio fijo de numeradores, sin proporcionar radio cuantificado. No se infiere transporte en todo el ortante.
