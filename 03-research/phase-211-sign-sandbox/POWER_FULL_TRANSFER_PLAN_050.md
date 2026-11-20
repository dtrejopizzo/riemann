# POWER_FULL_TRANSFER_PLAN_050 — Alcance MULTI y contactos necesarios para la comparación de cola

Estado: EXPLORACIÓN SUPERADA por POWER_FULL_TWELVE_050. Los cálculos de este plan siguen siendo válidos, pero la obligación E_(2,3) propuesta como siguiente paso fue evitada mediante el margen reforzado0.02 y el transporte por trece polos con numerador cero. No tratar NEXT como la obligación vigente. Papers intactos.

## Antecedentes y diferencia

Consultados ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID, CROSSWORD-TO-D y COMMON_TRANSFER010§6, GEOMETRIC_TRANSFER015§6, ARITHMETIC_BLOCK007 y R12_TRANSPORT049. El filtro múltiple con pesos positivos es anterior; la consecuencia que ahora se puede aplicar es que049 y007 han probado TODA su órbita E2 positiva. No se reintenta una ordenación universal de contactos ni se supone que el contacto3 tenga signo favorable. La construcción posible siguiente debe conservarlo exactamente en matrices, y pagar sólo la cola desde4.

## Corolario MULTI que ya se obtiene

Sea u=63/2 y F0=P(s)/(s+u)^12, gradoP<12. La base007 y049 demuestran, con c=1/2500,

    E2[Q^jF0]>c||Q^jF0||², TODOS j≥0.

Para tasas arbitrarias finitas v1,...,v12≥u, sea F=P/∏(s+vi). MULTI015 demuestra

    E2[F]=Σw_j E2[Q^jF0],
    ||F||²=Σw_j||Q^jF0||²,
    Σw_j z^j=∏[ri/(1−(1−ri)z)], ri=u²/vi².

Los pesos son no negativos y suman1. La convergencia absoluta se conserva para E2 por la misma continuidad usada en049. Así

    E2[F] > ||F||²/2500, TODOS los doce polos≥u.         (MULTI-E2)

No hace falta iterar R12 en bases intermedias. Esta consecuencia es para ARCH+POLAR+contacto2, no para W completo.

## Cálculo previo de cola, antes de otro certificado finito

COMMON_TRANSFER010§6 prueba uniformemente en esos doce polos, con α=2/3 y σ=21,

    ||exp(21y)f||² ≤ B ||f||²,
    B=Σ_(j=0)^11 Σ_(k=0)^j binom(j,k)²(2/3)^(2k)/(1/3)^(2j+1)
     =1282776893780652,
    sqrt(B)<35815875.

Por Cauchy, |c_f(logn)|≤sqrt(B)n^−21||f||². Para todo entero M≥3 y cotas L≥logM, s≤sqrt(M),

    |Σ_(n≥M)2Λ(n)n^−1/2 c_f(logn)|/||f||²
      ≤ (2·35815875/s)M^−21[L+ML/20+M/400].             (TAIL-M)

En efecto n^−21.5≤n^−21/s, Λ(n)≤logn y logx·x^−21 es decreciente desde3. La comparación por primer término más integral da exactamente el corchete indicado. No se elimina ningún primo o potencia de primo en el rango.

Sólo se evalúan los tres cortes adyacentes que corresponden a conservar contactos2, luego2,3, luego2,3,4:

| Cola | L | s | Majorante TAIL-M |
|---|---|---|---|
| n≥3 | 11/10 | 17/10 | <0.005126 |
| n≥4 | 7/5 | 2 | <0.000013763 |
| n≥5 | 17/10 | 11/5 | <0.000000146 |

La primera cota calculada es mayor que c=0.0004; no permite concluir W desde MULTI-E2. Esto es insuficiencia de ESE majorante, no una cota inferior para la cola real ni necesidad absoluta de conservar3 bajo cualquier método. La segunda sí es menor que c. Por tanto el mínimo conjunto inicial de contactos que esta comparación justifica intentar es{2,3}: si se prueba

    E_(2,3)[Q^jF0]≥||Q^jF0||²/2500, TODOS j≥0,F0∈V12, (NEXT)

MULTI y TAIL-4 darían W[F]>(1/2500−0.000013763)||F||² para todos los doce polos. No sería necesario incluir4 para ese margen. NEXT sigue OPEN aquí; requiere un nuevo corte highpass analítico y el segmento exhaustivo que éste determine. El contacto3 no se ha separado por valor absoluto en esos bloques ni supuesto favorable. No se ha ejecutado una campaña para escoger índices o contactos.
