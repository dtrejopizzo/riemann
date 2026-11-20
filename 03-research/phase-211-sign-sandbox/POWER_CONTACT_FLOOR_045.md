# POWER_CONTACT_FLOOR_045 — Qué deja de certificar el corte240 al entrar5

Estado: **PROVED en el alcance específico declarado**, revisión independiente aprobada en [POWER_PRIMAL_AUDIT_045.md](POWER_PRIMAL_AUDIT_045.md)§1; verificador exacto PASS. Chequeo específico de un certificado EXISTENTE; no nueva región positiva ni NO-GO de todos los truncamientos. Papers intactos.

## 1. Lectura y alcance exacto

Consultados índice ROUTES-TRIED-INDEX, grid maestro y CROSSWORD-TO-D; leídos Paper47 sec:log5/app:encllog5, ROUND_007_B y ROUND_008_A/C. La prueba en Paper47 hasta T5=log5/2 es un certificado de matriz y cola, no un mecanismo elemental de signo que falle matemáticamente al entrar5. Paper47 cor:beyond5 demuestra incluso positividad en algún intervalo posterior por continuidad.

Origen de los datos: Paper47/main.tex líneas11233ff fija tau_N=240, k1=280,k2=330 y140 coordenadas por paridad. Su lowercert en11160 exige

    s_infty<=m(tau_N)−A_T,
    q_Y=s_infty−mu−omega_+ Lambda_(k1)(T tau_N)>0,
    A_T=sum_(n in N_T) 2Lambda(n)/sqrt(n).

Para mu>=0, omega_+>=0 yLambda>=0, s_infty>0 es condición necesaria de ese criterio. Se demuestra que el MISMO corte y el MISMO floor de masa total no pueden mantenerse al entrar5.

Antecedente decisivo: ROUND_026_A§§0–3 YA sustituye el floor m(tau_N)−A_T por un enclosure del símbolo REAL en una banda y certifica ventanas T=1 y207/200 por computadora (alcance/estado allí). No se repite esa campaña ni se presenta el cambio de floor como novedoso. La búsqueda dirigida en007/008/026 e índice no encontró la comparación racional específica de este memo.

## 2. Fallo cuantitativo del floor de masa total

Si log5/2<T<=log7/2, el contacto no nulo nuevo es5 y

    A_T=A2345=sqrt2 log2+(2/sqrt3)log3+log2
                                      +(2/sqrt5)log5>17/4.

Basta usar log2>69/100,log3>109/100,log5>8/5, sqrt2>7/5, sqrt3<7/4,sqrt5<9/4. El verificador comprueba las cotas logarítmicas mediante los intervalos racionales existentes y la comparación final es

    (12/5)(69/100)+(8/7)(109/100)+(8/9)(8/5)>17/4.

Por otra parte, m(tau)=Re psi(1/4+i tau/2)−logpi. El integral elemental Euler para Re z>0 es

    psi(z)=logz−1/(2z)+int_0^infty B1({t})/(z+t)²dt.

Se obtiene integrando por partes el sumatorio de1/(z+n) menos su integral; el término periódico tiene módulo<=1/2. En z=1/4+120i,

    |resto|<=(1/2)int_0^infty dt/[(t+1/4)²+120²]
                        <pi/480<1/100.

Además Re[−1/(2z)]<0, |z|<121 ypi>3. Por tanto

    m(240)<log(121/3)+1/100<15/4.

La última desigualdad se certifica sin logaritmos numéricos: la suma positiva de Taylor de exp(187/50) hasta grado14 es mayor que121/3.

Concluye

    m(240)−A2345<−1/2,
    q_Y<=s_infty−mu<−1/2 para mu>=0.                 (FIXED-FLOOR-FAIL)

Así falla una hipótesis de la propuesta de certificado ANTES de probar la matriz finita. No es un valor negativo de la forma. El estimate de masa total no distingue el solapamiento espacial que se anula al entrar un contacto; por eso no contradice continuidad ni las ventanas ya certificadas026.

## 3. Los cruces que una representación nueva debe conservar

A T fijo tras entrar5, escriba en la banda de frecuencia del lowercert

    G=G0+v5 C5, v5=2log5/sqrt5,
    C5=Q_T[1_(|tau|<tau_N)cos(tau log5)](D)Q_T.

G0 incluye el floor escogido y todos los contactos anteriores, no sólo la parte arquimediana. Si A_i=P_Y G0 e_i y D_i=P_Y C5 e_i, el Gram penalizado del certificado es EXACTAMENTE

    <A_i+v5D_i,A_j+v5D_j>
     =<A_i,A_j>+v5[<A_i,D_j>+<D_i,A_j>]
                                           +v5²<D_i,D_j>.

La matriz inferior restante contiene

    R_ij=(s_infty−mu)delta_ij−<G e_i,e_j>
                    −<A_i+v5D_i,A_j+v5D_j>/q_Y,
    R_(i,xi)=<e_i,chi>+<A_i+v5D_i,P_Ychi>/q_Y,
    R_(xi,xi)=c−||P_Ychi||²/q_Y.

Para la forma completa c=−1/2 en paridad par y c=+1/2 en impar; para la primitiva c=0. Tras el paso Haynsworth de Paper47 queda el Schur finito cuyo signo debe probarse, con estas columnas completas. Se han escrito los cruces lineales, el cuadrático y el borde polar: dominar sólo la matriz diagonal de contactos o suprimir D_i no los controla.

Estas fórmulas reutilizan lowercert, no son una reducción nueva. Sirven como obligación mínima para evaluar un par positivo L55-B: debe ofrecer un lower real de TODA la forma con error/slack que cubra esas columnas y la cola, o una desigualdad más fuerte que las evite legítimamente. Un par con una medida artificialmente de masa finita no se impone aquí; la cola infinita debe poder tratarse en la clase auténtica.

## 4. Conclusión limitada

El mecanismo existente hastaT5 es certificación Slepian+Schur con cola controlada, no un patrón elemental extensible identificado. FIXED-FLOOR-FAIL precisa el obstáculo del corte240 heredado. Cambiar el corte, mejorar el floor o repetir certificaciones está registrado008/026 y no se propone como avance de signo. La representación L55-B aún debe aportar un bound nuevo de la forma completa; esta nota no afirma que lo aporte o lo imposibilite.
