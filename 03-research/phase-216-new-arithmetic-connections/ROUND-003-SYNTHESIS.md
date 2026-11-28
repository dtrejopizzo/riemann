# Ronda 003 — Costes aritméticos exactos y antecedentes de la construcción binomial

28/11/2026. **Fase abierta; aportación de prioridad establecida todavía no obtenida.** Esta ronda produce teoremas y ejemplos aritméticos adicionales, y muestra con mayor precisión qué parte del programa ya está contenida en mecanismos clásicos. La revisión bibliográfica no se declara exhaustiva.

## 1. Fórmula exacta para tres graduados

Sean K/Q_p finito y ξ,η clases cristalinas integrales de Tate 1. Si el cup ξ∪η tiene orden p^s, con s=0 para la clase cero, entonces existe una representación integral cuya racionalización es cristalina, con graduados Z_p(2),Z_p(1),Z_p y clases adyacentes p^aξ,p^bη, **si y sólo si a+b≥s**.

Por tanto:

    coste total mínimo = s;
    coste de escala común = ceil(s/2).

La prueba no confunde existencia galoisiana con cristalinidad. Primero calcula la obstrucción matricial integral; después construye una realización racional cristalina por módulos filtrados de Frobenius y demuestra que las demás realizaciones racionales difieren por extensiones cristalinas de Tate 2. Los detalles y las fuentes están en [ROUND-003-KUMMER.md](ROUND-003-KUMMER.md).

Un ejemplo explícito sobre K=Q₃(ζ₃), con π=ζ₃−1, usa

    α=ζ₃(1+π³)³,     β=1+π².

Sus clases Kummer son cristalinas y racionalmente independientes. Su cup tiene orden tres, de modo que el coste común es exactamente uno. Este ejemplo demuestra que la compatibilidad racional no garantiza compatibilidad integral con las clases fijadas. El mecanismo es cup/reciprocidad local clásico; la formulación de coste no basta para reivindicar originalidad.

## 2. La excepción dyádica es real y se calcula

Para Q₂, cualquier unidad u≡3 mod4 y cualquier cadena de al menos tres graduados Tate consecutivos con κ(u) repetida, el coste común es **exactamente uno**, independientemente de la longitud.

La cota inferior excluye todas las realizaciones: el cup mod2 es el símbolo de Hilbert (u,u)₂=−1. La cota superior se construye en una potencia simétrica; multiplicar las clases por 2 produce coeficientes 2^k/k! integrales para todo k.

El retículo binomial de la ronda002 no contradice esto. Para p=2, el medio coborde representa κ(−1), una clase integral de orden dos; las clases adyacentes que produce alternan κ(u) y κ(−u). La prueba y la comprobación reproducible están en [ROUND-003-DYADIC.md](ROUND-003-DYADIC.md).

## 3. El antecedente de la construcción binomial ya es identificable

Se obtuvo una identidad estructural exacta entre el retículo binomial y un dual truncado de Iwasawa:

    L ≅ Z_p(χ^n) ⊗ (Λ/I^(n+1))^∨.

Los módulos de Iwasawa, torres logarítmicas y matrices binomiales de Kummer/Massey son antecedentes directos, con pasajes leídos en de Shalit, Beilinson–Kings–Levin, Kubrak–Shuklin–Zakharov y Sharifi. No se localizó literalmente cada corolario cristalino de la ronda002; sí se identificó el mecanismo del que se deduce. Por ello se conserva como lema útil y no como fundamento de una nueva área. Véase [comparación de antecedentes](ROUND-003-BINOMIAL-PRIOR-ART.md).

## 4. La frontera queda más precisa

El objetivo siguiente es distinguir el coste de los cups del coste de compatibilidad superior. Si b es la mínima escala que anula todos los cups adyacentes, siempre c_cris≥b. Los ejemplos positivos de esta ronda tienen igualdad. Para tres graduados Tate consecutivos, la fórmula anterior demuestra esa igualdad en general.

Todavía no hay aquí un ejemplo aritmético con c_cris>b. Encontrarlo —o demostrar una igualdad en un rango no cubierto por los antecedentes— exige estudiar cuatro o más graduados y controlar la condición cristalina junto con las elecciones integrales. La anulación de Massey mod p no equivale automáticamente a una realización compatible sobre Z_p.

Como ensayo delimitado queda κ(5) repetida sobre Q₂: sus cups repetidos se anulan y el coste está entre cero y uno. Para tres graduados, la fórmula anterior da cero. Para cadenas más largas no se decide aquí. Antes de tratarlo como pregunta nueva debe compararse con Demuškin, Hilbert90 y módulos logarítmicos. El protocolo y las referencias pendientes están en [ROUND-003-NOVELTY-GATE.md](ROUND-003-NOVELTY-GATE.md).

## 5. Estado de las obligaciones

| Obligación | Evidencia / estado |
|---|---|
| Aportar matemática y no sólo nombres de programas | Pruebas completas de coste exacto y ejemplos no torsión guardados. |
| Contrastar antecedentes más próximos | Comparación estructural y lectura de pasajes completos documentadas. |
| Verificar fórmulas auxiliares | Script dyádico: 100 valoraciones factoriales, 128 ternas mod4, 256 identidades de cociclos; todas aprobadas. |
| Revisar literalmente toda la bibliografía hasta 28/11/2026 | NO completado; búsquedas y lectura seleccionadas, con cobertura explícita. |
| Establecer una aportación original | NO establecido; no se confunde derivación propia con prioridad. |
| Crear un campo o subcampo sustentado en resultados nuevos | NO establecido; requiere al menos un teorema original y aplicaciones independientes. |

La ronda cambia el siguiente paso de investigación: ya no basta encontrar un coste positivo, porque hemos visto que puede ser enteramente binario y clásico. El objetivo de originalidad sigue activo.
