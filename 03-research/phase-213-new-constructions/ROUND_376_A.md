# Marcado logarítmico de la capa: crecimiento hasta (1−ε)log log x

**Estado: PROVED, con revisión independiente del momento común, las marcas y las exclusiones.**

Con la notación de 375, uniformemente para 1≤k≤2h,

    k M_(k+1)(x) ≥ (1−o(1)) h M_k(x).

Así cada prefijo impar hasta (1−ε)h tiene signo negativo para x suficientemente grande, para cada ε>0 fijo. En 375 dos elecciones posibles de primo costaban k(k+1). Aquí la masa total de una de esas marcas se normaliza exactamente.

**Una estimación prima común.** Para Y→∞ se tiene

    Σ_p (log p) g(log(Y/p)) ∼ J Y,   J=∫ g(u)exp(−u)du>0.

En |u|≤B fijo vale por el PNT, como convergencia de la medida θ(Ydt)/Y a dt en un compacto de t>0. Las colas son uniformemente pequeñas respecto de Y al hacer B grande, por θ(t)≪t y bandas unitarias con la gaussiana. El mismo equivalente vale recortando |u|≤2√L si Y→∞ uniformemente y L→∞. Sólo se utiliza para log Y≥L/(3kh), muy superior a √L.

**Entrada.** Descartar |log(n/x)|>2√L cuesta o(1) por 375. En cada producto restante repartir su masa g entre sus primos p con pesos log p/log n. Si se retienen sólo log p≥L/(kh), la pérdida relativa es O(1/h) por Σ log p=log n. Para cada cofactor distinto m=n/p así generado, escribir Y=x/m; entonces log Y≥L/(2kh). Sumando ahora sobre todos los p, incluso los descartados, y usando log n∼L en el tramo central original, se obtiene

    (1−o(1)) M_k ≤ (1+o(1)) (J/L) Σ_m Y.

La absorción del o(1) absoluto es uniforme por la construcción de 375, válida también para k≤2h porque kh=o(L).

**Salida.** Para cada m elegir q∤m en L²<q≤exp(L/(10kh²)). Poner Y'=Y/q. Para los primos r con |log(Y'/r)|≤2√L se tiene r>q y log(mqr)∼L. Borrar los r|m cuesta O(kL) en la suma con peso log r, pues g es acotada y log m≤2L. Como log Y'≥L/(3kh), ese coste es o(Y') uniformemente. Por la estimación prima, la suma para esta pareja m,q, con peso g(log(Y'/r))log r/log(mqr), es (1+o(1))JY/(qL). Mertens da Σ_q 1/q=h−O(log h) uniformemente, incluyendo la exclusión de los divisores de m.

Para un producto final N=mqr, fijado r, hay a lo sumo k elecciones de q entre los otros factores. Sumando en r, Σ_{r|N}log r/log N=1. Por tanto toda la salida marcada pesa a lo sumo k M_(k+1). Comparando entrada y salida se obtiene la desigualdad anunciada. La ganancia viene de conservar el mismo J en ambas estimaciones, además de recuperar una potencia de k en la multiplicidad.

**Registro de revisión.** El equivalente primo es uniforme porque el menor log Y' permitido es L/(3kh)≥L/(6h²)→∞ y supera sqrt L; por eso el mismo J aparece en entrada y salida, incluso después del recorte gaussiano. Al excluir q|m se pierde como máximo k/L² en la suma de recíprocos. Al excluir r|m se pierde O(kL)=o(Y') uniformemente, antes de dividir por L. Cada producto final fija m una vez designados q,r; para cada r hay a lo sumo k elecciones de q, y la suma de todas las marcas log r/log N es exactamente 1. Los términos no generados sólo reducen esta suma positiva, de modo que la cota kM_(k+1) no exige que todos los primos puedan actuar como r. La construcción inferior de 375 sigue siendo uniforme para k≤2h, con log M_k≥L−O(kh+h), y absorbe la cola o(1).

**Alcance.** Para k≤(1−ε)h, la razón supera 1 uniformemente al crecer x. Esto conserva el signo favorable en una franja mayor; el argumento pierde esa garantía cuando k/h supera 1. El saldo total y el control de las capas intermedias de 374 siguen abiertos.
