# Varianza del cruce aritmético que toleraría el signo global

Cotejo independiente previo con 213-019/020/021, P47 (band, oneprofile, AM), L2_BUILD_019, R186_005 y P2_SCHUR_001. La selección de un vector de prueba por proyección es clásica. La aplicación específica mide simultáneamente los residuos de todas las celdas después de quitar dos momentos. El cotejo no localizó esta condición en esos antecedentes.

Fijar C>1. Para K entero grande usar las celdas completas de índices J=[K,floor(CK))∩ℤ. Usamos exactamente M, A, h y q de BUILD084 (3)-(4). Sean p=(log(3/2),−log 2) en las celdas 1,2 y d=log(4/3). Para j∈J escribir

    s_j = Σ_{i=1,2} p_i Σ_{ni≤j<n(i+1), n≥2} Λ(n)/n,
    r_j = Σ_{i=1,2} p_i A_ij,     l_j=log(1+1/j).

Sea H la matriz con filas 1 y K l. Definir b=Hᵀ(HHᵀ)⁻¹(d,0)ᵀ, v=s−Hᵀ(HHᵀ)⁻¹Hs, D=max(1,max_{i∈J} Σ_{j∈J}|M_ij|). Con al menos dos celdas H tiene rango dos. La cola x=b+v/D hace primitivo a p+x, pues Σp_i=−d, el momento inverso de p es cero y Hv=0. Los vectores b y v son ortogonales y ⟨s,v⟩=||v||². La fórmula matricial exacta de BUILD084 y la cota de suma por filas para la matriz simétrica dan

    a(U(p+x)) ≤ q(0)+D||b||²−2⟨s,b⟩+2⟨r,x⟩−||v||²/D.       (1)

Por tanto un miembro derecho estrictamente negativo para cualquier K con J separado de la cabeza (K≥4) y al menos dos celdas proporciona un contraejemplo completo. La prueba usa únicamente una cota superior de la energía de cola.

Para C fijo, HHᵀ/K converge por sumas de Riemann a la Gram de 1,1/u sobre [1,C], definida positiva. Así ||b||₂=O_C(K⁻¹ᐟ²) y ||b||₁=O_C(1). Por PNT y sumación parcial las dos sumas interiores en s_j tienden respectivamente a log 2 y log(3/2), uniformemente para j≥K; por tanto ||s||∞=o(1) y ||v||₂=o_C(√K). Además ||r||₂=O_C(K⁻¹ᐟ²) por (3) de BUILD084. En la matriz de cola la diagonal cuesta O_C(log K), la suma arquimediana fuera de diagonal cuesta O_C(log K) por h(0)=2log2 y h(m)≤1/m para m≥1. Para cada n con contacto en J se cumple n≤C. En una fila hay a lo sumo n columnas superiores y una inferior para ese n, de modo que toda la suma de pesos aritméticos es O_C(1). Luego D=O_C(log K).

En consecuencia (1) tiene la forma q(0)−||v||²/D+o_C(1). Si el signo global vale, necesariamente

    limsup_{K→∞} ||v||²/D ≤ q(0),    ||v||²=O_C(log K).

La primera cota es un umbral asintótico con normalización computable. La decisión finita usa (1) con todos sus términos. Satisfacer la condición deja abierta la energía de otras colas, incluso dentro de la misma banda. No se ha verificado una violación para los pesos de von Mangoldt. PROVED para la condición necesaria y el criterio finito tras auditoría matemática independiente.

## Evaluación finita del criterio

Con C=2 el peine interno es exactamente cero, pues j<2K≤2i en toda la banda. Se acumuló W(m)=Σ_{n≤m}Λ(n)/n por criba de potencias primas y se usó s_j=log(3/2)[W(j)−W(⌊j/2⌋)]−log(2)[W(⌊j/2⌋)−W(⌊j/3⌋)]. Se calcularon la proyección por QR, D por sumas absolutas de filas y la energía por la matriz exacta de BUILD084. Resultados en doble precisión, redondeados; no son certificados intervalares.

| K | D | Pérdida proyectada | Cota (1) | Energía del test |
|---:|---:|---:|---:|---:|
| 16 | 5.030073 | 0.015720 | 0.822007 | 0.183973 |
| 64 | 7.819384 | 0.014822 | 0.407719 | 0.149002 |
| 256 | 10.595623 | 0.010248 | 0.239676 | 0.146535 |
| 1024 | 13.369113 | 0.007644 | 0.185880 | 0.152829 |

La energía de cabeza vale aproximadamente 0.167101. En las tres últimas bandas la cola reduce esa energía; los cuatro tests quedan por encima de cero. La tabla concierne a una sola cola seleccionada por banda.

### Mínimo con la cabeza p fija

Cotejo previo. BUILD084 (16)–(18), 212-59/75, 212 ROUND_001_B, P47 prop:schur y la entrada de Schur en P48 ya contienen la eliminación. Se usa sólo para decidir si la elección de cola ocultó una energía negativa en los cuatro ejemplos.

Para Z con columnas ortonormales que generan ker H, escribir x=b+Zu, B=ZᵀAZ y g=Zᵀ(Ab+r−s), donde A es el bloque de cola. Si B es definida positiva el mínimo se alcanza en u=−B⁻¹g. Se construyó Z por SVD, se comprobó el menor autovalor de B y se resolvió el sistema por Cholesky. El mayor residuo euclidiano de estacionariedad fue 2.1×10⁻¹⁵. Diagnóstico en doble precisión.

| K | Menor autovalor de B | Energía mínima con cabeza fija |
|---:|---:|---:|
| 16 | 0.606024 | 0.156323 |
| 64 | 0.553454 | 0.116346 |
| 256 | 0.547662 | 0.107085 |
| 1024 | 0.547097 | 0.101826 |

Incluye todas las colas constantes por celda en cada banda con ambos momentos impuestos y esa cabeza. La tabla no controla simultáneamente varias bandas ni establece una cota uniforme en K. Se cierra aquí el barrido.
