# Ronda 23, memo C — Bloque interior I^λ con pesos de criba y lema 𝒩_k(ν): puerta de selección

Encargo: decidir si (a) el bloque interior I^λ de ROUND_004_A (4.3), (b) el lema OPEN 𝒩_k(ν) de la fase 211
ROUND_006_C §7, o su combinación, dan una desigualdad unilateral que vea Near_M junto con Arch_M en el mismo paso, que
no sea una cota en valor absoluto ni una gran criba estándar. Puerta de selección: sin derivaciones ni cómputos.

Lectura en primaria: ROUND_004_A completo (Lemas 1, 3, Prop. 2, (4.3)–(4.4), respuesta (iv), «NO excluido» 1–4);
fase 211 ROUND_006_C §§1–7 y resultado; fase 188 N_BUILD_021 completo (Prop. 1, Teor. 2, Prop. 3); ROUND_015_A completo
(clase 𝒮_Λ², §1); RULES_AVOID l.37, 57, 84, 440, 650, 668; NEAR_DOSSIER l.128–133, 162, 187, 304, 320, 356–385.
Grep en el índice maestro («criba», «sieve», «Selberg», «large sieve», «Montgomery–Vaughan», «Hilbert»; 469 líneas):
entradas pertinentes W-sieve (R167_102 Thm B/B′, R167_103 Thm S; l.3861, 4370), tabla 1.5 fila «Cribas (Selberg, gran
criba, Ramanujan)» (ronda 15, repetición; l.1914), l.1320–1323, l.20430–20431 (fase 116: large sieve peor, ortogonalidad
desde escala e^{2T}), l.23403–23409 (fase 104_35–38: Cholesky/gran criba, «toda inversión de Selberg pierde la cancelación
firmada»), l.23435–23436 (104_93: NO-GO de clase Selberg/Vaughan), l.5402 (Bessel/gran criba hasta Y^{1/2−ε}), l.5998
(estrategia J, Hilbert ponderado: «no reintentar cotas Hilbert…»), l.6135, l.6446 (MV+Sobolev NO-GO), l.866 (clase MV, gran
criba, Sobolev, Hölder). Ninguna entrada examina I^λ ni 𝒩_k por nombre: ambos figuran sólo como residuos en NEAR_DOSSIER.

## (1) Antecedente más cercano

- (a) ROUND_004_A, respuesta (iv) y «NO excluido» 4: con λ fijado sin el peso, I^λ es afín en c y el Corolario 2 de
  ROUND_003_6 (R3-e) se aplica literalmente: un signo de I^λ por separado vale para todo c > 0 o para ninguno. Para la
  versión cuadrática (4.4), ROUND_015_A §1 (clase 𝒮_Λ², PROVED): ningún certificado con cuadrados de criba de
  coeficientes Λ-libres falla bajo los tres controles. Para toda cota de I^λ obtenida de estadísticas de criba o
  progresiones: N_BUILD_021 Teor. 2 (clase cerrada bajo modificación finita) y W-sieve (R167_102 Thm B).
- (b) ROUND_006_C §§3, 5, 7 mismos: 𝒩_k(ν) es un recuento de energía multiplicativa con b_m ≥ 0; el memo declara en §5
  que es un enunciado de tamaño que sobrevive a cΛ, borrado y modificación finita, y que fallar en Beurling (por el
  espaciado entero) «no es un diagnóstico». Clase: MV/gran criba (índice l.866, l.20430–20431, l.23403–23409).

## (2) Objeto u operación nuevos

Ninguno. Lo único escribible es la composición
    |I^λ(F)| ≤ Σ_{1<k≤N} |θ^λ(k)| k^{−1/2} |⟨A_M τ_{−log k}F, F⟩|,
acotando cada término por un recuento tipo 𝒩_k de casi-coincidencias m ≈ k·m′. Eso es exactamente una cota en valor
absoluto con pesos |θ^λ| y una gran criba sobre productos: la forma excluida por el encargo. No sé escribir una
desigualdad unilateral (sin |·|) que combine ambas piezas: 𝒩_k(ν) no contiene Arch (es Σ b_m b_{m′} sobre pares de
productos de N_T, sin núcleo arquimediano), y en I^λ el término Arch entra con coeficientes θ^λ que no ven el peso.

## (3) Por qué el cambio evitaría el fracaso del antecedente

No aplica: no hay cambio. Concretamente:
- (a) El motivo exacto de fracaso es el grado 0 en el peso de θ^λ (R3-e). Dar signo a I^λ no lo altera; sólo lo
  alteraría un λ dependiente de los valores exactos de Λ (problema extremal; RULES_AVOID l.668, ROUND_015_A «próxima
  operación»), que es otra operación, no I^λ con pesos de criba, y cae primero en ROUND_014_A Lema P(b) si la dependencia
  es por cociente afín.
- (b) El motivo de fracaso de 𝒩_k es que es de tamaño: vale para cualquier peso no negativo de soporte dado, y la
  pérdida C^k es fija por orden, incompatible con (F4) (margen ≈ M⁻³). Mejorar θ < 1 mejora el tope exp(2e^T) del
  conjunto de subnivel de ROUND_006_C, que no es una afirmación de signo sobre 𝔸_M.
- Combinación: componer una pieza afín en c con una cota de tamaño sigue siendo afín/en valor absoluto; no aparece
  ningún término cuya orientación dependa de que el peso sea exactamente 2Λ.

## (4) Conexión con 𝔸_M ⪰ 0 y controles

Conexión posible: 𝔸_M ⪰ 0 ⟸ Arch_M − Div_M − Near_M ≥ (cota de I^λ + resto R^λ), con a_T = Re⟨M^λS_NA_MF,F⟩ − I^λ − R^λ.
Paso con nombre en que habría que fallar y no falla:
- peso cΛ: «cota de I^λ» — afín en c (R3-e); una cota en |·| vale para todo c ≤ c₀ con el mismo λ: no falla.
- borrado de una potencia de primo: «recuento 𝒩_k» y «cota de I^λ» — cambian en O(1) por término; clase cerrada bajo
  modificación finita (N_BUILD_021 Teor. 2; thm:finmod): no falla.
- Beurling: 𝒩_k usa el espaciado entero 1/(m+1) y la unicidad de factorización (ROUND_006_C §5(c)), así que su prueba
  no se transfiere; pero esto es fallo de una cota de tamaño, no de un paso de signo, y I^λ con criba se transfiere
  (R167_103 Teor. S). (F2) tampoco se cumple: Arch y el peso no entran por el mismo objeto en el mismo paso.

## Veredicto

NO PASA (sin mecanismo; en la parte (a), repetición de ROUND_004_A (iv) + ROUND_015_A §1; en la parte (b), clase
MV/gran criba ya registrada). Ni I^λ, ni 𝒩_k(ν), ni su composición dan una desigualdad unilateral que vea Near_M y
Arch_M en el mismo paso: la única composición escribible es una cota en valor absoluto con pesos |θ^λ| y un recuento de
energía multiplicativa, que vale para todo peso de la clase y no falla en los controles.

Etiquetas: los dos residuos siguen OPEN como enunciados (signo de I^λ sin examinar en sí; lema 𝒩_k(ν) OPEN como
enunciado de tamaño), pero quedan descartados como vía hacia el signo global en esta puerta: el de I^λ por R3-e, el de
𝒩_k por ser de tamaño (F1, F4). Lo no excluido sigue siendo lo de ROUND_004_A «NO excluido» 1–3 (λ dependiente de los
valores de Λ o de F; Möbius del sistema μ_a), que no es la operación examinada aquí.

Para el revisor: comprobar que (4.3) de ROUND_004_A tiene θ^λ independiente del peso para todo λ de criba (Selberg,
Barban–Vehov, GPY, Λ_R), y que 𝒩_k(ν) en ROUND_006_C §7 no contiene núcleo arquimediano.
