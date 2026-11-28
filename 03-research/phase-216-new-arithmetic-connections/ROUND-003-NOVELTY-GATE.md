# Umbral de novedad después de las rondas 001–003

28/11/2026. Documento de control para no confundir un resultado comprobado en esta investigación con una aportación original. La revisión sistemática y el objetivo de originalidad permanecen abiertos.

## Qué quedó descartado como conexión general inédita

1. **CM y correlaciones:** el dato de pares ya es el de Colmez; reconstrucción y homometría tienen una literatura propia. El tensor de Hodge y la expansión de Walsh son herramientas existentes.
2. **Compatibilidad integral y matrices:** la estabilidad de retículos, los quivers, la altura de Plücker y el crecimiento de productos de matrices son antecedentes directos.
3. **Denominadores del proyector:** el coste regular es exactamente una potencia de la diferente; la prueba es de álgebra clásica.
4. **Polinomios binomiales y retículos cristalinos:** el mecanismo se identifica con el dual de un cociente de Iwasawa y torres logarítmicas. Sharifi ya relaciona matrices binomiales, Kummer y Massey.
5. **Un primer coste aritmético positivo:** la repetición de κ(3) sobre Q₂ tiene coste uno por un símbolo de Hilbert. Es una obstrucción binaria clásica, no evidencia de un fenómeno superior nuevo.

Estos descartes no invalidan las pruebas obtenidas. Determinan qué no debe presentarse como origen de un nuevo campo.

## Un objetivo que sí distingue los niveles

Para una cadena de retículos cristalinos T₀,…,Tₙ con clases adyacentes ξᵢ y realización racional, mantener la definición anterior c_cris: menor e que permite todas las clases p^eξᵢ simultáneamente.

Definir para comparación, sin pretensión de nueva terminología,

    b = mínimo e≥0 tal que p^(2e)(ξᵢ∪ξᵢ₊₁)=0 para todo i.

Siempre c_cris≥b: el bloque a distancia dos de cualquier realización proporciona una primitiva del cup correspondiente. El factor p^(2e) viene de escalar ambas entradas.

Lo que todavía no tenemos es un ejemplo aritmético con **c_cris>b**, o un teorema que fuerce igualdad en una clase de datos no cubierta por teoría existente. El ejemplo DGA de la ronda001 no resuelve este problema aritmético. El ejemplo dyádico de la ronda003 satisface c_cris=b=1 y tampoco lo resuelve.

Una primera prueba decisiva sería una cadena de cuatro graduados con los cups adyacentes integrales nulos y coste positivo. La alternativa igualmente válida es demostrar que el coste es siempre cero para una familia suficientemente amplia. Ambos resultados requieren comparación bibliográfica; una definición nueva no garantiza que el problema sea nuevo.

## Antecedentes que deben contrastarse antes de esa prueba

- [Sharifi, Massey Products and Ideal Class Groups](https://www.math.ucla.edu/~sharifi/publ/massey.pdf), §1.2 y comienzo de §2 leídos por el agente principal: construcción matricial, indeterminación, raíces de unidad de orden potencia de p y cocientes de aumentación. No se leyó el artículo completo. Sus hipótesis no deben sustituirse por una condición cristalina sin prueba.
- [Merkurjev–Scavia, Formal Hilbert 90](https://arxiv.org/html/2308.13682), introducción y Th.1.3–1.4 leídos: anulación de triples mod p y ciertos cuádruples. No identifican automáticamente un sistema integral compatible ni una realización cristalina.
- [Mináč–Tân, Triple Massey products and Galois theory](https://arxiv.org/abs/1307.6624): sólo resumen consultado en esta ronda, que anuncia anulación para grupos de Demuškin. La versión exacta, coeficientes y condición de definición deben leerse antes de extrapolarla.
- Los modelos integrales y levantamientos cristalinos de Gao, Kalloniatis y Riedel ya identificados en ROUND002.

La diferencia entre coeficientes mod p, mod p^m y Z_p es una obligación de prueba; también lo es la compatibilidad de las elecciones al variar m. No se deduce un contraejemplo integral de un resultado negativo abstracto de álgebras diferenciales.

## Ensayo concreto para la siguiente ronda

Sobre Q₂, repetir κ(5) con graduados Tate consecutivos de longitud al menos cuatro. El cup repetido es cero: el símbolo (5,5)₂ es trivial, y el grupo integral H²(Q₂,Z₂(2)) tiene orden dos con reducción inyectiva. La construcción por potencias simétricas garantiza coste≤1. Falta decidir si se puede construir coste cero para toda longitud o si alguna longitud fuerza uno.

Ésta es una pregunta de trabajo, no una conjetura de positividad ni una afirmación de que permanezca abierta en la literatura. Debe confrontarse con los resultados de Demuškin, Hilbert90 y realizaciones de retículos. Si se resuelve por una construcción clásica, se registrará y se abandonará como candidato de originalidad.

## Cobertura central de búsqueda de esta ronda

Consultas: `site:arxiv.org "crystalline" "Hilbert symbol" extensions`; `site:arxiv.org "integral logarithm" "Kummer"`; `site:arxiv.org "Massey" "crystalline" integral`; `site:arxiv.org "filtered" "crystalline" "obstruction" cup`; `"integral Massey products" "local"`; `"Massey products" "Z_p" "Galois"`; `"Massey" "crystalline representations"`; `"local fields" "Massey products" powers`; `site:arxiv.org Demushkin strong Massey vanishing property integral`; `site:arxiv.org "Massey" "Z/p^n"`; `site:arxiv.org "Massey" "cyclotomic" "orientation"`.

Hubo consultas vacías y resultados irrelevantes. Se siguieron sólo fuentes primarias para las afirmaciones matemáticas. También se abrieron Beilinson–Kings–Levin1410.4741 (§1.1) y Kubrak–Shuklin–Zakharov2308.01110 (introducción) para cotejar los antecedentes encontrados por el agente especializado. Los informes de cada frente detallan una cobertura mayor. Ninguna de estas búsquedas es un barrido exhaustivo de arXiv.
