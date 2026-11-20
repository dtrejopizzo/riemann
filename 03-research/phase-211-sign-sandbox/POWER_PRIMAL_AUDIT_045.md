# POWER PRIMAL AUDIT 045

Estado: CONTACT_FLOOR045 y PRIMAL_PAIR045 APROBADOS; inventario documental de ventanas revisado. Papers intactos. No se ejecutó una campaña de certificación.

## 1. Floor heredado y cruces — APROBADOS

Revisados `POWER_CONTACT_FLOOR_045.md`, su verificador exacto y Paper47 `prop:lowercert`. Ejecución independiente de `tools/power_contact_floor_045_verify.py`: PASS. La masaA2345 incluyeΛ4=log2 y sus cotas racionales dan>17/4. EulerB1 complejo en1/4+120i tiene resto<π/480<.01; el término−1/(2z) tiene parte real negativa. El bound de log(121/3) por Taylor positivo de exp(187/50) prueba m240<15/4. Así el CRUDO floor m240−A2345<−.5.

Bajo las condiciones admisibles explícitas mu≥0,omega+≥0 yLambda≥0, qY≤s∞−mu<−.5. Sólo falla ese criterio con el mismo corte240 y el floor de masa total. No se ha probado un símbolo real negativo, W negativo ni imposibilidad de otro par primal o certificado.

Los cruces lineales y cuadráticos de la nueva columna C5 y el borde polar coinciden con las fórmulas exactas de Paper47: R_ij tiene el Gram completo/qY con signo negativo y el borde mixto tiene signo positivo. Los valoresc−1/2 par,c+1/2 impar y c0 primitivo son correctos. Estas fórmulas son antecedentes, no una construcción nueva de lower.

## 2. Frontera DOCUMENTAL archivada: corrección de estado

`ROUND_026_A.md` ya distingue el floor CRUDO de una cota del símbolo REAL por intervalos en[τN,τB], seguida por el bound m(τB)−A. Su Theorem26A.1 declaraλ_A(1)≥10^−23 y Theorem26A.2 declaraλ_A(207/200)≥2·10^−26. Por monotonía enT, el segundo cubre todos0<T≤207/200 dentro de su marco.

Se leyeron los logs ARCHIVADOS:

- `tools/cert_window/log_cert_T1_p0_mu1e-23.txt` y `_p1_mu1e-23.txt`: ambos contienen `certified:true` para mu10^−23.
- `tools/cert_window/log_cert_T1035_p0_mu2e-26.txt` y `_p1_mu2e-26.txt`: ambos contienen `certified:true` para mu2·10^−26.

Los archivosJSON de resumen fueron sobrescritos por intentos con otros mu; por ejemplo `cert_G_T1035_par0_k2640.json` conserva mu6·10^−26 fallido. Esto no invalida los logs positivos a2·10^−26. No se interpreta un archivo último como historial completo.

ParaT1.098 se localizaron los30 logs de build,30 partesPKL y el ensamblado `G_T1098.pkl`. La búsqueda dirigida no encontró un log/JSON de certificación final ni una afirmación de teoremaT1.098. Un build de Gram y un scan de símbolo positivo no constituyen por sí solos el certificado de matriz/cola. Por tanto el mayor extremo documental PROVED de este pipeline localizado aquí es207/200, no1.098.

Esta revisión es DOCUMENTAL: no se reprodujo ahora la construcción ni la certificación larga026. Los resultados están etiquetados PROVED/computer-assisted en la fuente archivada; su reproducción actual independiente no se ha realizado en esta ronda. El alcance publicado dentro de Paper47, las certificaciones locales archivadas y los avances nuevos de potencias son capas distintas y no deben confundirse al describir la frontera.

## 3. Condiciones de transferencia L55-B

El candidato sigue requiriendo un par representante POSITIVO explícito que dé la identidad en TODO el portador primitivo, con crecimiento/convergencia adecuados, slack controlado y coincidencia aritmética inband de ambos contactos. Sólo la implicación hacia un floor está autorizada; no se infiere converso o existencia de extensión positiva desde un lower primitivo.

Un vector factible de la LP o un test primitivo da un upper, no ese lower. La positividad de una medida mismatch tampoco basta porque la autocorrelación puede tener signos. Al entrar otro contacto deben conservarse los nuevos overlaps yΛ de potencias primas; el traslado por TV/slack o continuidad necesita su propio margen y no evita los límites ya registrados.

No se halló antecedente que descarte toda construcción particular de par explícito. Tampoco se obtuvo aquí ese par ni un floor nuevo. El chequeo del corte240 no se registra como un no-go global, y la frontera026 archivada no se cuenta como un nuevo resultado045.


Precisión adicional de la frontera documental: la introducción actual de Paper47 registra el resultado de Mori hastaT=(1/2)log15 como CITED, con checker computacional reproducido y spot checks archivados, pero sin nueva revisión de sus lemas analíticos. También cita Liu hasta17/16. Por ello207/200 es el mayor extremo PROVED localizado en el pipeline LOCAL026 inspeccionado aquí, no una afirmación de que sea la mayor ventana citada conocida. Ninguna de esas verificaciones largas se reprodujo ahora en045.

## 4. Reparación compacta concreta — APROBADA

Revisados `POWER_PRIMAL_PAIR_045.md` y `tools/power_primal_pair_045_verify.py`; ejecución independiente PASS. T3/5 tiene exactamente contactos2,3 y se encuentra en una ventana ya cubierta. La identidad representante usa medidas positivas PARES, inband aritmético exacto y TODOS los tests primitivos. El polar se anula allí; q_T es el símbolo PRIMITIVO, sin una falsa representación del polar no primitivo por una densidad real.

Siη=µ−(q_T+epsilon)dτ es compacta y par, F=(D²−1/4)φ satisface exactamente las dos condiciones primitivas. La medida ponderada(tau²+1/4)²η anula todos los cuadrados de Fourier. Polarizar sobre funciones reales y localizar dos bumps suaves da su núcleo coseno nulo en todas las diferencias deI. Derivar en0 elimina todos los momentos pares; los impares se anulan por paridad. Densidad de polinomios y positividad estricta del factor implicanη0. Sin PAR sólo se concluiríaη_even0; la condición está correctamente explicitada.

El script certifica q_T(0)<−15/2. Paraepsilon≤15/2, la rigidez obligaría a una densidad negativa en un entorno de0, imposible paraµ≥0. Esto descarta el ansatz de reparación COMPACTA con cola exactamente fija, no la forma comprimida ni todo par L55-B. No se usa una restricción artificial de masa global finita.

En§5, para una correcciónr par continua templada, la localización da(D²−1/4)²k0 en la banda. Las soluciones pares sonalpha cosh(t/2)+beta t sinh(t/2). Si además el resto exterior es una medida finita par firmada, las fórmulas coinciden con el certificado(D) de Paper47 y su orientación lower. Esta identificación está limitada explícitamente a ese subcaso; no cubre todas las medidas singulares o distribuciones ni prueba converso entre lower primitivo y existencia de par.

La actualización al contacto4 tiene coeficienteΛ4=log2 y es global en frecuencia. No puede realizarse manteniendo fija la antigua cola y una modificación compacta. Si una representación extendida dejara mismatch4, la pérdidaTVlog2 sería sólo un piso conservador; la identidad previa no garantiza la extensión. No hay una continuación automática ni nueva cobertura.

## 5. Cierre de alcance

La ronda añade un chequeo racional del floor heredado y una obstrucción al ansatz PARTICULAR de cola fija compactamente reparada, con la identificación precisa de un subcaso que retorna al dual. No se construyó el par positivo faltante ni se prueba un no-go general de L55-B. El límite de masa total finita fue descartado como restricción artificial antes de formalizarlo como avance. La revisión de ventanas corrige el registro documental sin promover builds o logs nuevos a resultados reproducidos. Root coincide independientemente en ambos memos y verificadores.
