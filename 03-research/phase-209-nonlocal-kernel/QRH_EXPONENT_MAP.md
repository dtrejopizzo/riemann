# QRH — mapa de exponentes y condiciones para una extrapolación

2026-10-19. Cálculo algebraico revisado por constructor y revisor.
**PROVED como lema condicional; estimaciones nuevas OPEN. No signo de D.**

## Alcance y diferencia

Consultados índice (L74 y familias de amplificación), grid y crucigrama.
No se reabre una familia cerrada ni se propone una nueva criba sin prueba.
La diferencia es analizar la extracción exacta de una fuente externa ahora
leída: ecuaciones2.3–2.5 del PDF OpenAI de5Oct2026. No se infiere una
recurrencia interpolando los números47/48,11/12,7/8.

Fuente: https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf

## Lema de réplicas

Supongamos, para D creciente y H=D^h en un rango autorizado, una familia
de números complejos A_j, una señal A y un subconjunto de J réplicas con,
para todo ε>0 (permitiendo constantes dependientes de ε),

    J >= H^κ D^(-ε),
    |A_j-A| <= C D H^(-δ) en cada réplica,
    sum_familia |A_j|² <= C_ε D^(a+ε) H^b.

Las constantes deben ser uniformes en D,H; h,κ,δ son positivos fijos.
Sumar |A|²<=2|A_j|²+2|A_j-A|² sobre las réplicas prueba

    |A| <= C_ε D^(θ+ε),
    θ = (1/2)max{a+(b-κ)h, 2-2δh}.

Por tanto, para que ESTA COTA certifique exponente1/2+ε, basta y es
algebraicamente necesario que

    h >= 1/(2δ),       a+(b-κ)h <= 1.

No son condiciones necesarias para cancelación real: el argumento puede
perder información y otro control puede mejorarla.

## Sustitución en el argumento publicado

Las réplicas son filas p^6: J es de orden H^(1/6)/log H y
A_(p^6)=A_1+O(D H^(-1/6)). Así κ=δ=1/6. La cota usada es
M(D,H)<=C_ε D^(1+ε)H, para H=D^(1+ϑ),0<ϑ<=1/10.
Luego a=b=1, h=1+ϑ y

    θ(h)=(1/2)max{1+5h/6,2-h/3}=11/12+5ϑ/12.

No hay una regla que tome este θ como entrada para una mejora siguiente.
Incluso concediendo CONTRAFACTUALMENTE la misma cota para todo h>0,
el mínimo algebraico sería θ=6/7 en h=6/7. Ese rango no está probado
por el resultado citado;6/7 no es un nuevo teorema externo ni nuestro.

Para h=3, el nivel crítico requeriría que el promedio total fuera
O(D^(3/2+ε)), frente a D H=D^4 en esa escala. No se afirma que tal
cota sea cierta o factible: cuantifica lo que esta extracción exigiría.

## Un objetivo alternativo preciso, todavía OPEN

En vez de estimar toda la familia, bastaría controlar sólo las réplicas
p^6 con Np entre Y/2 y Y, Y=D^(1/2), mediante

    sum_p |A_(p^6)(D)|² <= C_ε J D^(1+ε),
    J = #primos del intervalo, de orden Y/log Y.

El error conocido por réplica es O(D/Y)=O(D^(1/2)); el lema daría
|A_1|<=C_ε D^(1/2+ε). Este objetivo conserva la señal coherente;
la criba sobre la familia completa NO lo demuestra. Puede ser tan difícil
como controlar directamente la señal. No es una fuente nueva ya construida.

**Actualización tras el cálculo exacto:** QRH_REPLICA_COHERENCE.md prueba
que esas dos familias de estimaciones son de hecho equivalentes, para
todo ε>0 con renombre del exponente. La varianza de las réplicas es O(D)
sin cancelación; toda la dificultad restante está en su media coherente.
La selección, por sí sola, no aporta un mecanismo nuevo para acotarla.

## Las tres fracciones no son tres iteraciones

Kintali47/48 usa probe y comparación por densidad de ceros en un régimen
específico. El texto de30Sept2026 que da7/8 usa además un detector con
polinomios inversos y ordinarios y estimaciones separadas de momentos
(resumen introductorio y§§17–20). Esta lectura de estructura NO audita
sus199páginas. No se identifica una transformación común iterada.

Para D seguiría faltando una identidad que transfiera cualquier nueva
estimación a la cota inferior exacta de017. No se usa ninguna equivalencia
externa de D ni se atribuye a este lema un control del contratermino.
