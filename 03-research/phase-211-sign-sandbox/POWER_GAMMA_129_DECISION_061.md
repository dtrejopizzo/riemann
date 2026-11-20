# POWER_GAMMA_129_DECISION_061 — Decisión completa del caso interior pendiente129,0

Estado: PROVED, certificado racional PASS y revisión independiente aprobada en POWER_GAMMA_129_AUDIT_061.md. Un único átomo histórico; no campaña de órdenes ni afirmación uniforme. Papers intactos.

## 1. Resultado y motivo de este caso

Para u=63/2, N=129 y

    g_N(t)=t^(N−1)exp(−ut)/(N−1)! ·1_(t>0),
    G_N(s)=1/(s+u)^N,

se demuestra, con TODOS los contactos aritméticos y el polar,

    1.34·10^−10 < W[g129]/||g129||² <1.35·10^−10.       (DECISION)

Este caso estaba explícitamente pendiente en025/026/027.025 probó ERR129<−0.66;026 mostró que esa garantía gruesa no cubría el déficit ARCHsharp;027 controló sólo una cola conjunta. Una búsqueda en el corpus, el índice ROUTES-TRIED-INDEX, el grid R162_2300_MASTER_GRID y CROSSWORD-TO-D no encontró una decisión posterior en032/035/042. No se eligió un nuevo N: esta ronda retomó una obligación concreta ya registrada dentro del trabajo autorizado.

La diferencia es sustituir los bounds separados gruesos por ARCH estable032, polar racional, suma de todos los contactos hasta512 y una cola completa rigurosa. No se presenta como nuevo el método Euler–Maclaurin ni la identidad sharp018. Una evaluación preliminar única sólo verificó la viabilidad de un certificado pequeño; la prueba final no utiliza cuadratura ni números flotantes.

## 2. Norma y fórmula arquimediana estable

Poner d=128. La norma original, SIN renormalización adicional, es

    c0=||g129||²=binom(256,128)/63^257.

Escribir la autocorrelación normalizada exacta

    ρ(t)=c_g129(t)/c0=exp(−ut)Σ_(r=0)^128 a_r t^r/r!,
    a_0=1,
    a_r/a_(r−1)=2u(d−r+1)/(2d−r+1).

Todos los a_r son racionales positivos. ARCH_EXACT032§2 prueba

    ARCH/c0=ψ(16)−logπ−Σ_(r=1)^128(a_r/2^r)S_(r+1),
    S_p=Σ_(m=16)^∞m^−p.

Los sumandos restados son positivos; no se usa una combinación alternante de derivadas enormes. Como en032, S_p se encierra mediante suma directa16,...,31, Euler–Maclaurin con8 términos Bernoulli y resto periódico absoluto

    |B16|(p)_15/[16!·32^(p+15)].

Los coeficientes a_r/2^r multiplican los extremos racionales ANTES de redondearlos. Gamma, logπ y los logaritmos proceden del módulo auditado power_fixed_grid_003.py. El ancho final certificado de ARCH es<10^−18.

El polar normalizado es la fracción exacta

    POLAR/c0=2/[(u²−1/4)^129 c0].

## 3. Aritmética completa hasta512 y cola adversa

Todos los contactos de k0 son adversos: ρ(t)>0 para t≥0, por la fórmula gamma positiva018. Para cada potencia prima q=p^m, la magnitud normalizada es

    C_q=2logp ·q^−32 Σ_(r=0)^128 a_r(logq)^r/r!.

La potencia q^−32 es EXACTA: combina exp(−u logq) y q^−1/2, sin aproximar exponentes o raíces. El verificador tools/power_gamma_129_decision_061_verify.py genera todos los primos por división entera determinista y todas sus potencias hasta512, incluidos4,8,...,512. Para una potencia prima se usa Λ(q)=logp, no logq.

El polinomio se evalúa por Horner en potencias divididas, con todos sus coeficientes positivos. La división por q^32 se hace primero sobre los extremos racionales, como en032, evitando redondear prematuramente un recíproco muy pequeño.

Sea q_N(t)=−ρ′(t)/ρ(t). ROOT026 y q_N′>0 dan, para t≥log512>6,

    q_N(t)>16,

pues la condición suficiente exacta es

    u²>16²+2·128·16/6,

que se verifica racionalmente. Por tanto para x≥512,

    ρ(logx)≤ρ(log512)(x/512)^−16.

La función logx·x^−33/2 decrece desde512. Como la cola comienza en513, primer término no adicional: la suma se limita directamente por la integral desde512. Así

    0≤Σ_(q>512)C_q
      ≤2ρ(log512)√512 [2log512/31+4/961]
      =2·512^−31 P(log512)[2log512/31+4/961],
    P(t)=Σa_rt^r/r!.

La última expresión tiene sólo intervalos racionales: √512 se cancela exactamente con el exponente de ρ. Su valor certificado es<10^−24, con evaluación decimal del majorante aproximadamente1.9408294·10^−26. La cola es ADVERSA y se resta para el lower de W; no se descarta por un signo favorable inexistente.

## 4. Salida racional y decisión

La ejecución final terminó exit0 y PASS. Redondeando hacia fuera, los intervalos normalizados son:

    ARCH/c0 ∈[−209403793025407910633,−209403793025407910630]/10^20,
    POLAR/c0 ∈[263311994766765745833,263311994766765745834]/10^20,
    Σ_(q≤512)C_q ∈[53908201727901151035,53908201727901151036]/10^20.

Se suma ARCH+POLAR−peine y se resta el majorante de TODA la cola para el extremo inferior. Resulta

    W[g129]/c0 ∈[13456684165,13456684168]/10^20,

que prueba DECISION. El intervalo tiene margen amplio respecto del error arquimediano y de la cola; no hubo necesidad de una precisión masiva ni de modificar cortes sucesivamente.

## 5. Compensación exacta que faltaba en025/026

El resolvente sharp se evalúa racionalmente:

    S=E[1/(τ²+1/4)]=2Σ_(r=0)^128 a_r/32^(r+1).

La identidad se obtiene del kernel exp(−|t|/2), por Plancherel y la misma autocorrelación. Así

    ARCHsharp/c0=ARCH/c0+S,
    ERR=Σ_(q≥2)C_q−POLAR/c0+S,
    W/c0=ARCHsharp/c0−ERR.

El ERR es el de018/025, con E0(x)=ψ_Λ(x)−x+1 y extremo E0(1)=0. No se añade otro término2 ni se suma de nuevo la garantía0.66 ya incluida en ese ERR.

El certificado obtiene

    ARCHsharp/c0 ∈[−104219397018062543067,−104219397018062543064]/10^20,
    ERR ∈[−104219397031519227232,−104219397031519227231]/10^20.

El beneficio real −ERR es aproximadamente1.04219397031519, y el déficit real −ARCHsharp es aproximadamente1.04219397018063. Su diferencia positiva es sólo1.3456684·10^−10. La afirmación ERR<−0.66 era correcta, pero perdía una parte sustancial del beneficio y toda esta precisión de cancelación.

Hay además un dato interior cuantificado sin recalcular otra celda.024 ya certificó33/100<S129(2)<1/3, mientras025 identifica exactamente −ERR=2Σ_(m≥2)S129(m). Por tanto el aporte de TODAS las demás celdas cumple

    0.3755 <2Σ_(m≥3)S129(m)<0.3822.

Estas contribuciones son las mismas del balance, no un beneficio sumable por segunda vez. Muestran que el resto interior, aunque favorable en025, aporta una cantidad esencial para superar el déficit; no basta quedarse con la primera celda ni con el mero signo de ERR.

## 6. Alcance y reproducción

Se decide un caso escalar INTERIOR k0 que seguía abierto, con la Λ real completa y la constante arquimediana original. En particular K129(1)<0 de023 no implicaba negatividad de W: el balance integrado completo es positivo. Esto no rehabilita K≥0 universal ni presume que el kernel pointwise tenga el signo deseado.

No se infiere una fila, una desigualdad de propagación en N, ni un resultado para130 o para otros órdenes. El dato que una propagación futura debe conservar es el balance firmado con precisión relativa al pequeño residuo, no sólo bounds separados de orden constante. No se deduce una nueva ventana temporal T ni signo global. Papers intactos.

Reproducción:

    python3 03-research/phase-211-sign-sandbox/tools/power_gamma_129_decision_061_verify.py
