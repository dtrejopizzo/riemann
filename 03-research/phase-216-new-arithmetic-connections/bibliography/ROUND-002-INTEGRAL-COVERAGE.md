# Cobertura de la revisión integral de ronda 002

Fecha: 2026-11-28. Frente: separabilidad, diferente y coste del componente diagonal de E^{⊗r}. Se consultaron textos completos relevantes, no sólo resúmenes. No se hizo una indexación exhaustiva de arXiv ni una revisión exhaustiva de aplicaciones a motivos CM.

## Fuentes primarias efectivamente leídas

| Fuente | Pasaje inspeccionado | Resultado para la originalidad |
|---|---|---|
| Knus–Merkurjev–Rost–Tignol, [The Book of Involutions](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/involutions.pdf), §18 | Texto completo pp. 285–286: definición diagonal, proposición 18.10 con prueba, ejemplo 18.11, proposición 18.12 y expresión por bases duales. Descarga temporal y extracción con pdftotext. | El proyector racional y su construcción por traza son clásicos. |
| [Stacks §49.6, tag 0BVK](https://stacks.math.columbia.edu/tag/0BVK) | Definición de diferente de Noether; lemas 49.6.6–49.6.7 y sus pruebas completas. | La intersección integral de la diagonal está ligada clásicamente al dual del módulo dualizante. |
| [Stacks §49.8, tag 0BW0](https://stacks.math.columbia.edu/tag/0BW0) | Definiciones del módulo complementario y diferente; lema 49.8.2 y prueba. | El dual de traza usado en la prueba es el módulo complementario clásico. |
| [Stacks §49.12, tag 0BWB](https://stacks.math.columbia.edu/tag/0BWB) | Lemas 49.12.1–49.12.4 y ejemplo 49.12.5. | La relación con f′ en una presentación monógena es clásica; nuestro argumento general no necesita monogeneidad. |

La consulta al PDF de Stacks localizó además la versión compilada el 30/01/2026: [Discriminants and Differents](https://stacks.math.columbia.edu/download/discriminant.pdf). El PDF del libro presenta algunas referencias internas como `??`; los números 18.10–18.12 y las páginas consultadas son legibles. Esa imperfección editorial no afecta a las fórmulas verificadas.

## Consultas web realizadas

1. `separability idempotent inverse different tensor product number field ring integers denominator discriminant`
2. `arxiv separability idempotent different tensor product orders number fields`
3. `site.stacks.math.columbia.edu different trace dual annihilator multiplication tensor`
4. `"separability idempotent" "different"`
5. `"diagonal" "inverse different" tensor`
6. `site.stacks.math.columbia.edu "The Noether different" "Dedekind"`
7. `site.mit.edu Sutherland different codifferent trace dual basis discriminant lecture 12`

Se descartaron como apoyo para el caso aritmético concreto resultados sobre C*-álgebras y multiplicadores: comparten vocabulario pero no resuelven la pregunta de retículos de O_E. Tampoco se usaron páginas secundarias como fundamento de las pruebas.

## Verificación propia y límites

La fórmula para r factores se demostró en ROUND-002-INTEGRAL.md expandiendo el producto de idempotentes de pares en bases integrales. Se comprobaron los denominadores escalares con fracciones exactas para Q(i) y Q(√5), r=2,…,5, mediante `python3 experiments/round002_projector.py`; todas las verificaciones pasaron. La primera invocación con el comando `python` falló porque sólo está disponible `python3`; no fue un fallo matemático.

No se encontró ni se necesita reclamar una referencia que escriba exactamente D^{r−1} con nuestra notación: la prueba es una consecuencia inmediata de construcciones clásicas. No se verificó que un retículo CM de los papers del repositorio sea T_r, P_r o J_r. Esa identificación queda como trabajo distinto, imprescindible antes de transferir el coste a theta lifts, periodos o covolúmenes.
