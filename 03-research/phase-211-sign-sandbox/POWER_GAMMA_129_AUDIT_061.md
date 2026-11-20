# POWER_GAMMA_129_AUDIT_061

Estado: **APROBADO** POWER_GAMMA_129_DECISION_061 y su certificado completo, tras lectura final de las seis secciones. Papers intactos.

El único objeto es el átomo histórico N=129,k=0,u=63/2, no una campaña de órdenes. Los antecedentes025/026 dejaron ERR<−.66 sin decidir W;032 decide otro átomo,211,k1, y035 otro extremo,17,k0. El nuevo certificado conserva todas las piezas de la MISMA forma y decide el signo pendiente.

## Reproducción y normalización

Leído íntegro tools/power_gamma_129_decision_061_verify.py. Reproducción independiente con python3, exit0: **PASS** y los mismos extremos racionales impresos. La norma de g=y^128 exp(−uy)/128! es comb(256,128)/63^257. Los a_r=p_r r! satisfacen exactamente la recurrencia de la autocorrelación normalizadarho(0)=1; el Horner dividido por r+1 reconstruye sum a_r t^r/r!, sin factorial perdido.

ARCH usa A0 estable032, con HurwitzEM8/CUT32 y resto periódico absoluto. Los coeficientes exactos multiplican los extremos antes de crear intervalos redondeados. Gamma y logpi conservan las fuentes003 ya auditadas. La anchura final ARCH<10^−18 se comprueba. El polar2/(u²−1/4)^129 dividido por la norma es exacto racional. Se enumeran todos los primos y sus potencias hasta512 sin duplicar pesos; cada átomo usa2logp·m^−32P(logm), con la raíz de m cancelada exactamente.

## Cola adversa completa

La positividad de los coeficientes de rho hace adversos todos los contactos de k=0. ROOT026 da q(t)>sqrt((128/t)²+u²)−128/t. En t=6 este lower supera16 porqueu²>256+4096/6. Como log512>6 y q′>0, toda la cola tiene q>16 y rho(t)<=rho(log512) exp(−16(t−log512)).

La comparación suma-integral para TODOS los enteros m>=513 empieza en512, sin omitir el primer término de esa cola. Da

    cola <=2rho(log512)sqrt512[2log512/31+4/961]
          =2·512·[P(log512)/512^32]·[2log512/31+4/961].

Éste es exactamente TAIL del programa; las raíces se cancelan antes del redondeo. El signo adverso se resta en el extremo inferior de W y no se añade al superior. No se presume que el prefijo sea la suma completa.

La salida de W se forma por suelo/techo EXACTOS de los extremos Fraction, no por impresión flotante:

    W/||g||² ∈[13456684165,13456684168]/10^20.

Por tanto el átomo es estrictamente positivo. Los decimales float auxiliares del tail no se usan como fuente de prueba.

## Compensación sharp y células

El resolvente exacto es2sum_(r=0)^128 a_r/32^(r+1), correspondiente a E[1/(tau²+1/4)]. ARCHsharp=ARCH+resolvente y ERR=ARCHsharp−W. El programa conserva las dependencias mediante la fórmula independiente ERR=PRIME_total−POLAR+resolvente. Se certifican

    ARCHsharp/||g||² ∈[−104219397018062543067,−104219397018062543064]/10^20,
    ERR ∈[−104219397031519227232,−104219397031519227231]/10^20.

La normalización de ERR es la de rho(0)=1 usada en024/025. No se suma el antiguo beneficio .66 como si fuera otro término. Usando .33<S129(2)<1/3 ya certificado024, el beneficio conjunto de TODAS las células n>=3 es−ERR−2S129(2), entre.3755 y.3822. Los signos y la resta de la primera célula son correctos.

La fuente final enuncia el tail sólo como<10^−24, exactamente la cota comprobada por Fraction; el decimal más ajustado está explícitamente marcado aproximado. Esta separación es correcta y no requiere cambiar ni repetir el verificador. Los intervalos estrechos impresos de W/ARCHsharp/ERR usan suelo y techo racionales exactos y sí son recintos certificados. La atribución del caso es documental: la ronda retoma una obligación histórica, sin atribuir al usuario la elección de N.

El resultado decide ese átomo y cuantifica su compensación real. No decide toda una fila, bloques generales, orden arbitrario ni una ventana temporal nueva.
