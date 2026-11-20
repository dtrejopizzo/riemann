# Un bloque de dimensión arbitraria con cuatro tasas libres

Sean L₄,c₄ una longitud y un margen válidos en 199. Existe ε>0 tal que, al ordenar las tasas 1/2<v₁≤…≤v_n y contar multiplicidades, basta

    Σ_{j=5}^n 1/v_j ≤ ε

para obtener W(F)≥(c₄/4)||F||². Aquí F consta de cualquier dato de forma g en [−L₄,0] y cualquier función causal racional con denominador ∏(s+v_j) y numerador de grado menor que n. La cota admite cuatro tasas libres y n arbitrariamente grande. Los polos repetidos se interpretan en sentido confluente. El presupuesto suficiente no se evalúa numéricamente.

**Lema de concentración independiente de la dimensión.** Si un bloque rápido tiene presupuesto B=Σ 1/v>0, poner σ=1/(2B). Para cada polo σ/v≤1/2. Por reflexión de Hardy en 213-085,

    ||exp(σy)h||₂ ≤ exp(2σB/(1−1/4))||h||₂ = exp(4/3)||h||₂.

Así todo h unitario tiene ||h||₁≤exp(4/3)√B. Para B→0 su masa Fourier en cada intervalo fijo tiende a cero uniformemente. El piso global del símbolo arquimediano y su crecimiento a infinito implican que el ínfimo del arquimediano sobre esos h tiende a infinito. Para todo peso fijo b, eventualmente σ>b y la norma ponderada de h con exp(by) está uniformemente acotada. En particular las piezas prima y polar de W(h) están acotadas en valor absoluto por una constante usando b=1. El fondo rápido de W tiende a infinito, con independencia de la cantidad de polos.

**Conservar la ventana de 199.** Si ningún ε funcionara, habría listados con presupuesto después de la cuarta tasa tendiendo a cero y datos de norma uno con W(F)<c₄/4. Los casos de hasta cuatro polos satisfacen ya 199. Extraer una subsucesión en que cada una de las primeras cuatro tasas tenga límite finito o infinito. Los polos de límite finito quedan en una caja fija [1/2,V], y todos los demás forman un bloque rápido con presupuesto total B→0: a la suma recortada sólo se añaden hasta cuatro recíprocos que tienden a cero. Eventualmente los dos grupos son disjuntos y las fracciones parciales descomponen toda la cola como s+h. Una colisión exacta se conserva entera en su grupo. La norma unitaria inicial no exige que las fracciones parciales tengan coeficientes acotados.

Se tiene W(g+s)≥c₄||g+s||² por 199. Para algún C fijo en la subsucesión, |W(g+s,h)|≤C||g+s||·||h||. En efecto, g y s tienen soportes disjuntos; para g contra h se aplican Carleman y la cota ponderada de 198 (el intervalo es fijo). Para s contra h se usa la base de diferencias divididas de hasta cuatro tasas en caja compacta: el arquimediano de s actuando como operador está acotado en L², y su cruce no arquimediano, tras combinar ζ'/ζ y el polo, tiene densidad O(exp(C' y)) con las tres derivadas necesarias, como en 198–199. En esa estimación sólo se requiere ||exp((C'+1)y)h||₂=O(||h||₂), que acaba de probarse con constante independiente de la dimensión rápida. Por Young, si el piso rápido es al menos 2C²/c₄+c₄/2, se obtiene

    W(F) ≥ (c₄/2)(||g+s||²+||h||²) ≥ (c₄/4)||F||².

La contradicción demuestra la existencia uniforme. Una vez probado el enunciado en L₄, toda longitud menor entra por extensión por cero del dato a la izquierda.

**Consecuencia para el signo.** Un test racional negativo en esta clase necesitaría más de ε de presupuesto recíproco después de quitar sus cuatro tasas más lentas. Para cinco polos sin dato compacto, por ejemplo, existe un umbral absoluto para la tasa mayor por encima del cual todos los numeradores tienen signo estricto, con las otras cuatro tasas arbitrarias. No se concluye el signo de cinco tasas arbitrarias ni el del régimen denso del puente. 213-085 ya cubría todos los órdenes con presupuesto TOTAL ≤1/512; aquí se permite que las cuatro tasas libres consuman un presupuesto mucho mayor y se conserva un dato compacto arbitrario. No se afirma mejorar el valor 1/512 cuando no se excluyen tasas.
