# Ronda 002 — Revisión de originalidad y primer problema aritmético concreto

28/11/2026. **Estado: revisión ampliada realizada; revisión universal exhaustiva y prioridad científica NO establecidas.** El objetivo de obtener una aportación original sigue abierto. No se propone todavía un epónimo ni se declara creado un subcampo.

## Qué cambió respecto de la ronda 001

Se pasó de fichas y resúmenes a lectura de textos completos o secciones de prueba de los antecedentes más próximos. Zhao se leyó completo para comparar alcance; Kalloniatis, Gao, Riedel, los textos de reconstrucción y las fuentes sobre diferentes se revisaron en las secciones identificadas en los registros. Se produjeron pruebas autónomas y verificaciones exactas. Esto permite descartar varias pretensiones de novedad y precisar preguntas más exigentes.

| Dirección | Resultado de esta ronda | Consecuencia |
|---|---|---|
| Períodos y alturas CM parciales | Zhao ya estudia datos parciales, redes y correcciones discriminantes. | «Períodos CM con control integral» no basta como novedad. Hace falta una comparación geométrica específica ausente allí. |
| Información de cuatro puntos | Se prueba una distancia L² exacta a todas las fórmulas de grado bajo: 1/(16√m) para cuatro posiciones consecutivas. | Hay una barrera cuantitativa real a sumas fijas de contribuciones de pares; su prueba usa Fourier–Walsh clásico. |
| Reconstrucción | Con soporte de Fourier impar completo, todas las correlaciones de cuatro puntos determinan el tipo CM hasta traslación. | Lema probado y revisado por otro agente; método clásico de recuperar fases, no prioridad reivindicada. |
| Denominadores del tensor CM | El ideal exacto del proyector diagonal de r factores es D^(r−1); su índice es |disc(E)|^(r−1). | El coste regular ya es álgebra clásica. Además el cociente tensorial integral no paga automáticamente ese coste de proyector. |
| Extensiones cristalinas | El coste c_cris es cero para los datos no ramificados descritos y para extensiones libres estrictas de rango uno en una misma ventana Fontaine–Laffaille. | Gran parte de la primera propuesta se resuelve por mecanismos conocidos; el avance de abajo elimina además todas las cadenas Tate consecutivas sobre Q_p con p impar. |

Las pruebas y sus hipótesis están en los cuatro informes enlazados abajo. No se extrapolan los resultados de álgebras diferenciales de la ronda 001 a Galois sin demostrar realización.

## Avance posterior: el ejemplo se resuelve y da una familia completa

El ejemplo p=3, graduados Z₃(3), Z₃(2), Z₃(1), Z₃ y clases Kummer de 4 empezó con la cota 0≤c_cris≤1. Durante la revisión se encontró una construcción mejor: **c_cris=0**. La prueba está en §8 del informe cristalino, revisada independientemente por el agente de ese frente.

Más generalmente, para cualquier primo impar p y cualquier n, todos los datos de clases cristalinas adyacentes con graduados Z_p(n), Z_p(n−1),…,Z_p admiten realización simultánea integral sin escalar. No se impone que n quepa en la ventana Fontaine–Laffaille.

El mecanismo es concreto. Para una extensión cristalina con matriz gX=χ(g)X, gY=Y+c(g)X, usar dentro de Sym^n la base

    v_j = X^n binom(Y/X,j),   j=0,…,n.

La acción se escribe χ^n P((t+c)/χ). Preserva los polinomios de grado≤n con valores en Z_p, porque χ es unidad y c es integral. La base binomial es una base integral de ese módulo por diferencias finitas. La clase adyacente es la de c+(j−1)(1−χ)/2, que coincide integralmente con [c] para p impar. Escalas diagonales por productos de a_j permiten prescribir los múltiplos a_j[c]; los ceros se tratan separando bloques. Por Kummer, H¹_f(Q_p,Z_p(1)) es libre de rango uno para p impar, así que esto cubre todas las clases adyacentes de esa familia.

**Estado:** demostración autónoma guardada; controles exactos de 7040 columnas de matrices aprobados. La base binomial y la teoría de polinomios de valores enteros son clásicas. No se ha establecido si esta aplicación y generalización exactas tienen prioridad; se debe completar la búsqueda antes de presentarlas como un teorema original. Es un resultado más fuerte que la mera cota anterior y elimina otra posible falsa obstrucción factorial.

La frontera siguiente debe incorporar datos que el argumento no resuelve: pesos no consecutivos, clases sobre una extensión K/Q_p que no pertenezcan a un único submódulo cíclico, o estructuras adicionales fijadas. No se presupone que allí el coste sea positivo. El caso p=2 exige además revisar el coborde con denominador 2; la prueba anterior no lo cubre.

## Qué contaría como aporte propio sustantivo

- Un ejemplo aritmético con coste positivo probado y una fórmula que se generalice a una familia, si los antecedentes no lo contienen.
- Un teorema de realización sin pérdidas fuera del rango conocido, con hipótesis nuevas y comparación exacta con teoremas existentes.
- Una relación demostrada entre un observable CM superior y un defecto integral geométrico que sobreviva después de descontar la diferente clásica.

En cada caso se necesita un manuscrito con enunciado, prueba, ejemplos y sección que compare literalmente hipótesis y conclusiones con los trabajos próximos. La denominación y atribución deben seguir a esa aportación. Que una fórmula concreta no aparezca en una búsqueda no basta para convertir una aplicación elemental en un nuevo campo.

## Cobertura y pendientes

Esta ronda no permite decir «no existe en ninguna bibliografía». Se revisaron fuentes primarias concretas; no todo arXiv ni todos los libros y artículos relacionados. Quedan, entre otros, la lectura directa de Grünbaum–Moore y Pebody 2004/2007, comparación completa con Gee–Liu–Savitt y otros levantamientos triangulares, y el seguimiento de citas de esos trabajos. Los registros distinguen lectura completa, lectura de secciones y lectura de resúmenes.

La revisión exhaustiva solicitada sigue pendiente. La forma verificable de continuar es por enunciado candidato: cerrar su árbol de antecedentes, comprobar todas sus hipótesis y buscar activamente una prueba ya existente, un contraejemplo o una consecuencia que lo haga trivial. La prioridad será provisional hasta contraste especializado independiente.

## Archivos

- [CM: revisión de Zhao y barrera exacta](ROUND-002-CM.md).
- [Reconstrucción por cuatro puntos: prueba](ROUND-002-RECONSTRUCTION.md).
- [Proyector integral: diferente y denominador óptimo](ROUND-002-INTEGRAL.md).
- [Cristalino: coste cero y primera frontera concreta](ROUND-002-CRYSTALLINE.md).
- [Cobertura central y consultas](bibliography/ROUND-002-ROOT-COVERAGE.md).
- [Cobertura CM](bibliography/ROUND-002-CM-SOURCES.md).
- [Cobertura cristalina](bibliography/round002-crystalline-lecturas.json).
- [Cobertura integral](bibliography/ROUND-002-INTEGRAL-COVERAGE.md).
- [Comprobación de la base binomial](experiments/check_binomial_lattice.py) y [salida](experiments/check_binomial_lattice.json).

La ronda anterior queda conservada como historial; esta ronda restringe sus propuestas de novedad. La fase 216 permanece abierta.
