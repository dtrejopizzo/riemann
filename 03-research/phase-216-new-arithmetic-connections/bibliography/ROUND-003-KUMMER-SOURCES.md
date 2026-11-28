# Fuentes y cobertura — ROUND 003 Kummer

Fecha: 28/11/2026. La obstrucción inferior está calculada explícitamente. La suficiencia cristalina usa dos teoremas establecidos y una construcción de módulos filtrados desarrollada en el informe; no es una prueba autónoma de esos teoremas externos.

## Fuentes efectivamente consultadas

- [Milne, Class Field Theory, v4.03](https://www.jmilne.org/math/CourseNotes/CFT.pdf), I, Example 3.13(b), página impresa 44: lectura del pasaje del PDF sobre la acción ciclotómica de unidades. Con Frobenius aritmético actúa el inverso de la unidad. Se usa compatibilidad de reciprocidad con normas y la interpretación del símbolo normo-residuo. No se auditó la demostración completa de reciprocidad local.
- [Milne, Arithmetic Duality Theorems, segunda edición](https://www.jmilne.org/math/Books/ADTnot.pdf), I §2: fuente para dualidad local finita. Apertura del PDF y ubicación del capítulo; la fórmula compacta integral del informe se deriva por límites de la dualidad finita. No se presenta la prueba de Tate desde cero.
- [Berger, On p-adic Galois representations](https://mahalex.net/teaching/seminars/cristalline/Berger%20On%20p-adic%20Galois%20representations.pdf), §16, página 15: lectura del cuadro y observaciones sobre Tate 1 y Tate r≥2. El índice web leyó incorrectamente ≥ como >; se descargó el PDF y se comprobó con `pdftotext -layout` que el rango es **r≥2**, esencial para el argumento.
- [Colmez–Fontaine, Construction des représentations p-adiques semi-stables](https://webusers.imj-prg.fr/~pierre.colmez/CF.pdf): PDF de autores, apertura del enunciado de equivalencia. Se usa admisibilidad débil ⇒ admisibilidad y N=0 ⇒ cristalino. No se reauditaron las 37 páginas de la prueba.

## Consultas

1. `Hilbert symbol Q3 zeta3 units 1 uniformizer explicit Hilbert pairing units`
2. `Hilbert pairing local field contains p roots unity filtration U_i U_pe1-i`
3. `Kummer units crystalline extensions Qp(1) Bloch Kato H1f units`
4. `Milne class field theory local reciprocity cyclotomic Qp units inverse norm compatibility pdf`
5. `Colmez Fontaine construction representations p adiques semi stables weakly admissible admissible 2000`
6. `local Tate duality H2 Zp(2) H0 Qp/Zp(-1)`
7. `site:jmilne.org "Arithmetic Duality" "pdf"`
8. `site:jmilne.org "3.13" "inverse" cyclotomic`

La búsqueda sobre filtraciones de unidades localizó una descripción de ortogonales en MathOverflow. No se usó como fuente de la prueba: el ejemplo evita esa dependencia mediante la norma exacta 13 y reciprocidad ciclotómica. Tampoco se usan como autoridad páginas generadas o foros aparecidos entre los resultados.

## Separación de garantías

- Aritmética del ejemplo: π²=−3ζ, norma 13, exponente 7 módulo 9 y paridad de valoraciones: cuentas directas.
- Cup no nulo: depende del teorema clásico de reciprocidad/Kummer, con convención explícita.
- Orden exacto: depende de dualidad local; se calcula directamente su grupo dual de invariantes.
- Realización racional: construcción explícita de bandera filtrada, más Colmez–Fontaine.
- Suficiencia integral cristalina: ecuación de cocadenas, H¹=H¹_f para Tate 2 y estabilidad por subcocientes; no se afirma un control integral más fuerte de tipo Breuil/Kisin.
- Prioridad: no investigada exhaustivamente. El teorema de coste sintetiza mecanismos clásicos y no se anuncia como nuevo hasta comparar la literatura de extensiones mezcladas y obstrucciones de Yoneda.
