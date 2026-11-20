# AUDIT_012 — Falsificador de la dominación del mapa011

2026-10-19. Revisor independiente. Leídos LINK012, certify.py, check_laplace.py y sus salidas. Ambos programas reproducidos con python-flint0.9.0, precisión Arb128bits; terminaron sin fallos.
**Veredicto: PROVED el falsificador para la normalización EXACTA de U de LINK011. No exclusión de todas las reescalas ni cierre de D.**

## 1. Corpus y clase nueva

Consultados índice (incluida entrada011 y P1/Gram), grid y crucigrama; cotejadas las definiciones de P47 y la auditoría011. La igualdad del mapa ya estaba refutada y no se reintenta. La pregunta nueva es la desigualdad TOTAL Q_T≥||UF||² para ese mismo U y escala, que seguía abierta. El test y la certificación responden exactamente esa pregunta; no se construye otra familia auxiliar ni se usan márgenes sobre ceros.

## 2. Test exacto, dominio y polar

T=4/5, ω=π/(2T), r=3(ω²+1/4)/(9ω²+1/4) definen números exactos. La aritmética de bolas los encierra; no se reemplaza r por un flotante independiente. Para f=cos(3ωx)+r cos(ωx), ortogonalidad da ||f||²=T(1+r²) y f(±T)=0.

Los momentos cosh de las dos frecuencias tienen los signos y factores escritos en LINK012. Sustituir r los cancela ALGEBRAICAMENTE. Que una bola contenga cero no sería prueba de esa identidad, pero aquí no se usa tal criterio: la cancelación es exacta por la fórmula. F=f/√N es par, polar libre y pertenece a H¹₀, luego al dominio de gamma y de Q_T.

La aproximación por C_c∞ par con corrección del momento es válida en H¹. Q_T es continuo para esa convergencia y U es L²-acotado. El margen negativo estricto sobrevive en un core suave. No se limita el falsificador a una realización de matrices sin dominio controlado.

## 3. Término de rango uno y cola gaussiana

De S=κG_s+κvv*+Π con las otras dos piezas PSD resulta ||UF||²≥κ|M(F)|². La suma M=Σa_d(d^(−1/2)−d^(−1)) converge absolutamente por las cotas011. Intercambiarla con la integral en un compacto es legítimo.

Agrupar k=dn produce exactamente b_k y la resta z_cτ, con z_c=ζ(3/2)−ζ(2)>0. La normalización por √N se aplica después a M(f). Los factores2 de τ y del mapa011 están correctos.

La cota 0≤b_k≤k basta para la cola. Para a=πexp(−2T), K=12 se verifica aK²>1/2, así xexp(−ax²) decrece para x≥K. Las dos comparaciones integrales dan las colas exp(−aK²)/a y exp(−aK²)/(aK). Al multiplicar por longitud2T, cota |f|≤1+r y el factor exterior2 del mapa, se obtiene EXACTAMENTE ε_M escrito. No se atribuye signo a f para descartar términos.

La integral truncada de M es de una función ENTERA: sumas finitas de exponenciales, cosenos y exp(exp(2z)). Ignorar el indicador analytic del callback no oculta una singularidad en esa integral. La evaluación validada y la cola positiva dan la cota de |M| con el sentido correcto.

## 4. Certificado principal de gamma y peine

La Fourier entera con sinc es correcta para la convención de P47. Sobre el eje real f es par real, luego fhat²=|fhat|² y la extensión simétrica de digamma coincide con m. Su extensión compleja es meromorfa, no entera; el cálculo por acb debe conservar las singularidades, como advierte el memo. El resultado final tiene además la verificación independiente sin esa cuadratura de §5.

Para t≥100>6ω, las fórmulas racionales de cada coseno dan |fhat|≤(8/3)ω(r+3)/t². La cota m(t)≤2logt+10 está demostrada por la separación de la energía de Lévy en tres intervalos. Verifiqué K≤1/u+1/2, las integrales 1/4+1/(12t) y 2logt+1−1/t y la cola ∫₁∞K<28/9. El C₀ negativo se omite sólo para una cota SUPERIOR. Integrar el majorante de frecuencia da ε_Γ con sus coeficientes2/3,2/9,10/3 correctos.

En T=4/5 los contactos son2,3,4. Los intervalos de autocorrelación y sus pesos Λ(2)=Λ(4)=log2, Λ(3)=log3 están correctos. La normalización por N afecta tanto gamma como peine.

## 5. Verificación independiente cerrada

La fórmula Laplace I(a) de §7 fue revisada por la ecuación diferencial del kernel exp(−a|x−y|). El particular, las condiciones Robin y el coeficiente homogéneo C producen exactamente el término cuadrado positivo con factor1+exp(−2aT). I=½〈F,v〉 lleva el factor1/2 correcto.

La energía gamma normalizada es C₀+2Σ_j[1/a_j−I(a_j)], a_j=2j+1/2. La desigualdad de traslaciones

    1−c_F(u)=||F−τ_uF||²/2≤u²||F'||²/2

vale para la extensión por cero H¹. De ahí la cola ≤2||F'||²Σ_{j≥J}a_j^(−3) y el majorante a_J^(−3)+1/(4a_J²) por suma-integral. El valor de ||F'||²=ω²(r²+9)/(1+r²) es correcto.

check_laplace.py emplea J=200 y el peine exacto de lem:combsine con coeficientes(r,−1)/√(1+r²); el signo negativo procede de e₃=−cos(3ωx). Reproducido:

    gamma parcial = −0.2361826974540901495…,
    cola superior <0.000098513228,
    peine = −0.2377321365688090439…,
    Q_T(F)<0.001647953.

El certificado principal produjo Q_T(F)<0.002351. Son cotas superiores compatibles; la segunda comprobación elimina toda dependencia de cuadratura para gamma y peine.

## 6. Resultado certificado y escala

La reproducción de certify.py dio bolas con

    |M(F)|>0.1812652378,
    κ>7.95393245,
    ||UF||²≥κ|M(F)|²>0.26134304.

Incluso usando la cota más débil Q<0.002351 se obtiene

    Q_T(F)−||UF||²<−0.25899<0.

Por tanto la desigualdad exacta planteada para U011 es falsa. No se necesitó conocer ||UF||² completa ni demostrar un signo de Q_T por separado.

Esto refuta la escala fija, no todos los c_T||UF||². El cociente exploratorio no es un umbral certificado para todas las reescalas. De las cotas conservadoras se podrían excluir algunas escalas grandes, pero no arbitrariamente pequeñas ni dependientes de T; el memo no pretende esa conclusión.

**Veredicto final:** igualdad011 ya refutada y dominación012 ahora refutada para ese mismo candidato. Los auxiliares −R/FE siguen válidos; ninguna conclusión general sobre otros mapas o sobre D. Objetivo D íntegro OPEN y activo.
