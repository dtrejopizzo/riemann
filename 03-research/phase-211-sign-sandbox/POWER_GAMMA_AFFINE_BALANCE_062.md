# POWER_GAMMA_AFFINE_BALANCE_062 — La parte afín042 no es una base positiva en el mismo129

Estado: PROVED, certificado racional PASS y revisión independiente aprobada en POWER_GAMMA_AFFINE_AUDIT_062.md. Diagnóstico de un único caso ya decidido061; no nuevo signo W ni criterio uniforme. Papers intactos.

## 1. Pregunta concreta y antecedentes

Después de061, el caso N129,k0 ya tiene W>0 con margen normalizado aproximadamente1.3456684·10^−10. Se pregunta ahora si la parte afín de RENORMALIZED042 puede servir como una base positiva desde la cual estimar su residuo, o si ese residuo es esencial incluso en ESTE caso.

Consultados ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID, CROSSWORD-TO-D y026/027/030/042/043. Sumar LOCAL024 con ARCHsharp vuelve a Omega026; invertir las escalas de027 vuelve a Hjoint030, como ya registraron043/046. No se presenta otra reagrupación como nueva herramienta.

La diferencia cuantitativa autorizada es evaluar separadamente, en el MISMO129 y reutilizando los intervalos completos024/061, el comparador afín y el residuo renormalizado completo. No se calcula130 ni otro orden, no se aumenta precisión y no se construye otro criterio general de signo.

## 2. Identidad global y qué residuo se mide

Conservar la normalización de061 y definir

    κ=(log(2π)−1)/2,
    β=2κ−γ=log(2π)−1−γ,
    J1=J129(1),
    AFF=ARCHsharp+2γ−βJ1.

La identidad global042, válida para cada N fijo por convergencia absoluta, es

    ERR/2=−γ+(κ−γ/2)J1+R,
    R=(ERR+2γ−βJ1)/2,
    W/||g129||²=AFF−2R.                                 (EXACT)

Aquí R es el residuo RENORMALIZADO COMPLETO:

    R=−∫_1^∞h129(x)B1({x})(logx+γ)dx +∫_1^∞h129(x)E(x)dx.

Incluye tanto el término periódico B1 como el error Euler E. No se atribuye a B1 por separado el beneficio obtenido. Tampoco se aplica ABS-TAIL042, que requiere N≥2^80 y no está disponible en129. Este cálculo usa R sobre TODA la semirrecta, no Rinside ni Rtail de aquel teorema.

## 3. Datos completos reutilizados, sin nuevos cortes

CELL_TEST024 ya calculó endpoint1=Σ_(m≤64)μ(m)m^−32P129(logm), aunque su salida no imprimía ese endpoint. Con su MISMO polinomio positivo y su mismo resto tailP,

    J1∈[endpoint1.lo−tailP,endpoint1.hi+tailP].

El resto controla TODOS los m≥65 por la integral gamma positiva de024. No se cambia la suma Möbius por un prefijo de signo supuesto.

GAMMA_129_DECISION061 proporciona ARCHsharp y ERR completos: ARCH estable032, polar racional, todos los contactos hasta512 y cola adversa rigurosa. Gamma y log(2π) usan los intervalos auditados003. El verificador062 importa esos dos módulos sin cambiar sus constantes, su precisión o sus parámetros, y después evalúa AFF y R mediante EXACT.

No se resta la nueva caja de AFF y la de2R como si fueran errores independientes para recertificar el pequeño margen W: comparten exactamente J1,γ,β. W conserva su certificado independiente061; la identidad EXACT explica su cancelación algebraica.

## 4. Resultado racional

La ejecución de tools/power_gamma_affine_balance_062_verify.py terminó exit0 y PASS. Redondeando hacia fuera a denominador10^12:

    J1 ∈[662483401466,662483401467]/10^12,
    AFF∈[−60446492280,−60446492279]/10^12,
    R  ∈[−30223246208,−30223246207]/10^12,
    −2R∈[60446492414,60446492415]/10^12.                 (BOXES)

En particular, sin depender de decimales flotantes,

    AFF<−1/100,
    R<−1/200.

La base afín tiene un déficit de aproximadamente0.06044649228. La corrección del residuo completo aporta aproximadamente0.06044649241, reparándolo casi exactamente y dejando el margen positivo de061. El diagnóstico utiliza sólo la precisión ya disponible024; no persigue más dígitos del residuo.

## 5. Consecuencia y límite

Para este comparador concreto, AFF NO es una base positiva de la prueba. Ignorar el residuo o tratarlo sólo como una perturbación sin cuantificar pierde el aporte que repara el déficit. No se concluye que un residuo renormalizado no pueda acotarse con signo ni que toda representación afín falle: se identifica el término esencial de ESTE balance real.

El dato R<0 no se extiende a otros N. Además R se encerró usando ERR061 ya conocido; no se obtuvo una estimación nueva independiente que permita propagar el signo en N. La comparación uniforme de las celdas con ARCHsharp sigue abierta. El resultado no refuta042, no usa K≥0 universal y no modifica el kernel, la constante arquimediana o Λ.

Por tanto se registra sólo el diagnóstico cuantitativo y su uso: cualquier continuación desde la parte afín debe conservar y estimar de verdad el residuo completo, incluso en129, donde su magnitud es de orden0.03 aunque W/norma² sea de orden10^−10. No hay nuevo caso de signo, ventana T ni conclusión global.
