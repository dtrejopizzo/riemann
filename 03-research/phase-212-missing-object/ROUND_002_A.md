# Ronda 2, candidata A — La cola exterior de la hipérbola como suma de cuadrados: memo de selección

Notación de `../phase-211-sign-sandbox/STATEMENT_001.md` y de P47 §sec:firstcontact (thm:PCfinite,
eq:Gammaenergy, eq:collar, eq:Qbalance, prop:GEgap). Se fija T > 0, enteros M ≥ N ≥ e^{2T}, L ≥ 1, y

    a_m = 2m + ½,  s_m = a_m + ½ = 2m + 1,  b_m = √a_m e^{−a_m(T+δ)},
    e_m^±(t) = e^{∓a_m t} 1_{I_T}(t),   μ_m^±(F) = ⟨F, e_m^±⟩,   α_m^±(F) = b_m μ_m^±(F),
    Σ_L = 𝒪_L*𝒪_L + J𝒪_L*𝒪_L J = Σ_{m≤L} b_m² ( |e_m^+⟩⟨e_m^+| + |e_m^−⟩⟨e_m^−| ),
    H_{M,N} = Σ_{N<k≤MN} h(k) k^{−1/2} τ_{log k},   h(k) = Σ_{dm=k, d≤M, m≤N} Λ(d) ≥ 0,
    C(F) = Re⟨H_{M,N} 𝓕F, Σ_L F⟩      (el apareamiento de cola de R170_816 (3)).

Esta memo no construye. Contiene el cotejo, un lema corto que decide la selección y el veredicto.

## Cotejo

### (1) Antecedente más cercano

a. `phase-170-global-prime-inequality/R170_816` §§2–7: salida exacta Φ = B − C sobre vectores de
   ventana; C sólo con cota bilateral; §4 falsifica «h(k) ≥ 0 ⟹ apareamiento ≥ 0»; §6 separa el canal
   d = 2 y quedan dos correlaciones de Fourier sin signo. `R170_819`–`821`: a dos escalas, los mismos
   coeficientes h(k), ΔH sin signo. `R170_837` §4 (incompatibilidad de casilla: el detector D_Δ sale
   de la casilla de momentos, la cola sale de otra), Teorema 5.1 (residuo común = cierre), (6.7)
   (tras recombinar K_N = L_MS_N − H la forma es independiente del peso). `R170_835` Prop. 4.1 y §9:
   «factorización universal por R_L con L finito: FALSA; restringida al radical: existe a posteriori»
   (su demostración no se usa aquí). `R170_841` §4.2: el completado positivo canónico es de segundo
   orden y par; no orienta. `R170_870`: clase de borde impar frente a datos pares.
b. **Suma directa en k ya intentada.** `phase-161-row-d-sum-product-square/R161_030`–`034`
   (índice, catálogo 04, filas G4C-R161_030-032, G4C-R161_033-034, G4C-R161_035-038, G8B-161):
   varianza orientada de divisores con cuadrados indexados por las fibras k = de y pesos Λ(d);
   `R161_033` retira la realización: (PC) suma en k de manera coherente y pasar a la suma directa
   Σ_k ‖·‖² borra los términos de Gram entre k distintos; `R161_037`–`039`: la saturación que falta
   es el enunciado final, con contramodelo matricial a que sea automática. P47 rem:returnremarks
   recoge lo mismo («la varianza de una suma etiquetada por caminos de divisores no es la norma de
   la suma coherente en k»).
c. **Cuadrados con pesos aritméticos no negativos sobre funcionales exteriores ya escritos.**
   P47 eq:Qbalance: c_{N,L}(F) = Σ_{m≤L} d_{m,N} |(𝒪_LF)_m|², d_{m,N} = Σ_{n≤N} Λ(n) n^{−s_m};
   eq:Qspectral: Q_{N,L} es negativo en todo autovector con λ ≥ 0 y no admite representación como suma
   de cuadrados sobre P_T; eq:equivgate: la desigualdad de retorno es la conclusión. `R161_071`–`072`,
   `R161_081`: el balance recompone la ecuación y vale para pesos no negativos arbitrarios.
d. Fase 212: `ROUND_001_A` §4, `REVIEW_001_ABD` §4 (R1–R4), LEDGER K1.

La frase «ninguna memo intentó escribirla literalmente como Σ_{k>N} h(k)|ℓ_k(F)|²» es exacta sólo para
las fibras incompletas k > N con peso h(k). Para las fibras completas k ≤ N con pesos Λ(d), log k, la
conversión en suma directa sobre k es la ruta R161_030–039, cerrada en el índice. La candidata cambia
el rango de k y el peso; el obstáculo registrado (coherencia en k, dos vectores distintos en el
apareamiento) no depende de ninguna de las dos cosas.

### (2) Objeto o afirmación nuevos

Se buscaron los ℓ_k. Hay exactamente tres maneras de obtener cuadrados a partir de C, y ninguna es un
paso de signo.

**(D1) Diagonal en momentos Gamma.** Los únicos funcionales de F con soporte en la ventana que la
estructura ofrece con índice k son

    ℓ_k(F) = ( b_m k^{−s_m/2} μ_m^+(F) )_{m≤L} ∈ ℂ^L,     ‖ℓ_k(F)‖² = Σ_{m≤L} b_m² k^{−s_m} |μ_m^+(F)|²

(el vector 𝒪_L del trasladado de F por log k, con el factor k^{−1/2}). Con ellos vale la identidad
exacta (PROVED: es Λ∗1 = log leída sobre la serie de Dirichlet de los coeficientes de L_MS_N − S′_N
en s = s_m)

    Σ_{N<k≤MN} h(k) ‖ℓ_k(F)‖² = ⟨𝒪_LF, ( D_{M,L} Z_{N,L} − Z^{log}_{N,L} ) 𝒪_LF⟩,           (1)
    Z_{N,L} = diag(Σ_{n≤N} n^{−s_m}),   Z^{log}_{N,L} = diag(Σ_{n≤N} (log n) n^{−s_m}).

Es la familia de cuadrados de c_{N,L} de P47 eq:Qbalance (los mismos ℓ_n, peso Λ(n) en lugar de h(k)).
No es C: la diferencia C − (forma diagonal) es un término cruzado, y el Lema siguiente prueba que es
indefinido sobre P_T para cualquier elección de coeficientes diagonales.

**(D2) Cuadrado coherente por cambio de test.** Sustituyendo Σ_L por un test adaptado, W = P_T H𝓕,
resulta Re⟨H𝓕F, WF⟩ = ‖P_T H_{M,N}𝓕F‖² ≥ 0. Es un cuadrado de la suma coherente en k, no
Σ_k h(k)|ℓ_k|²; pierde la casilla de momentos que produce D_Δ (R170_837 §4) y no tiene relación
escrita con a_T. Es la brecha coherente/directa de R161_033.

**(D3) Polarización.** Re ᾱβ = ¼(|α+β|² − |α−β|²): diferencia de cuadrados, genérica.

**Lema (PROVED; clase: formas C − ⟨α, Bα⟩ con test Σ_L, L finito, pesos no negativos cualesquiera).**
Sea w(k) ≥ 0, no todos nulos, con soporte finito en k > N, H^w = Σ w(k) k^{−1/2} τ_{log k},
C^w(F) = Re⟨H^w𝓕F, Σ_LF⟩, y sea B cualquier matriz hermítica 2L × 2L. Entonces la forma
F ↦ C^w(F) − ⟨α(F), Bα(F)⟩, α = (α_m^±)_{m≤L}, no es semidefinida (de ningún signo) sobre P_T.
En particular, para ningún sistema de funcionales ℓ_k que factoricen por los momentos
μ_m^±, m ≤ L, y ninguna forma ρ ≥ 0 sobre P_T, vale ±C = Σ_k h(k)|ℓ_k(F)|² + ρ(F) sobre P_T; y cada
sumando Re⟨τ_{log k}𝓕F, Σ_LF⟩ es indefinido sobre P_T.

*Demostración.* Como 𝓕* = 𝓕 en L², C^w(F) = Re Σ_{m,±} \overline{α_m^±(F)} β_m^±(F), con
β_m^±(F) = b_m⟨F, φ_m^±⟩, φ_m^± = 1_{I_T} 𝓕 (H^w)* e_m^±.
(i) Si q(F) = Re⟨α(F), β′(F)⟩ es semidefinida sobre un subespacio V con α(V) = ℂ^{2L}, entonces
β′ = B′α sobre V: para F ∈ V con α(F) = 0 es q(F) = 0, luego F está en el radical de q sobre V, y la
forma polar da ⟨α(G), β′(F)⟩ = 0 para todo G ∈ V, es decir β′(F) = 0. Sobre V = P_T la sobreyectividad
vale porque las exponenciales e^{±a_m t}, e^{±t/2} son linealmente independientes en I_T.
(ii) Aplicado a β′ = β − Bα: cada φ_m^± coincidiría en I_T con una combinación de e_j^±, j ≤ L, y de
e^{±t/2}. En la coordenada x = e^t, F(t) = e^{t/2}f(x), se tiene (H^w)*e_m^± = e^{t/2}g(x) con
g(x) = Σ_k w(k) k^{−1/2±a_m} x^{∓a_m−1/2} 1_{(ke^{−T}, ke^{T})}(x), acotada, de soporte compacto en
(0,∞), no negativa y no nula; y φ_m^± = e^{t/2} ĝ(e^t) en I_T, con ĝ la transformada coseno de g. La
condición dice que ĝ coincide en (e^{−T}, e^{T}) con un polinomio de Laurent en ξ (potencias
ξ^{−2j−1}, ξ^{2j}, 1, ξ^{−1}). ĝ es entera, luego la igualdad se extiende a ℂ∖{0} y el polinomio de
Laurent es un polinomio; ĝ es acotada en ℝ y tiende a 0, luego es nulo, y g = 0. Contradicción. ∎

**Observación (PROVED; reformulación exacta, sin signo).** Con L = ∞ la factorización sí existe y es
explícita. ĝ es entera y par, ĝ(ξ) = Σ_{j≥0} γ_j ξ^{2j} ∫g x^{2j}dx, γ_j = 2(−1)^j(2π)^{2j}/(2j)!
(normalización autodual e^{−2πixξ}); el término j = 0 da el vector de Tate e^{t/2} y se anula sobre
P_T. Para F ∈ P_T real,

    ⟨F, φ_m^+⟩ = Σ_{j≥1} γ_j Θ_j σ_{j−m}(T) μ_j^−(F),                                         (2)
    Θ_j = Σ_{N<k≤MN} h(k) k^{2j},    σ_r(T) = sinh(2rT)/r  (σ_0 = 2T),

y análogamente para φ_m^− con 2 sinh((2m+2j+1)T)/(2m+2j+1). La serie converge absolutamente. Así C es
una forma hermítica en la sucesión de momentos Gamma, con matriz explícita cuyas columnas alternan de
signo con j (factor (−1)^j) y en la que la aritmética entra sólo por las sumas de potencias Θ_j, es
decir por el polinomio de Dirichlet de la cola en los puntos s = −2j, duales de los s_m. Ésta es la
forma exacta de «ℓ_k explícitos»: no hay índice k con cuadrados; hay una matriz alternada en (m, j).
Lo que falta escribir, y no se encontró, es una operación que firme esa matriz junto con los bloques
de E_N y de Tate.

### (3) Por qué el cambio evitaría la dificultad del antecedente

No la evita.

- **Coherencia en k (R161_033, rem:returnremarks, REVIEW_001_ABD R3).** El Lema muestra que el
  obstáculo ya está en un solo k: cada sumando es indefinido. Pasar de fibras completas a incompletas
  y de log k a h(k) no cambia nada de lo que el Lema usa (sólo w ≥ 0, w ≠ 0).
- **Genericidad en el peso (R170_837 (6.7); LEDGER K1).** (1) y (2) valen para todo peso, con el
  defecto interior añadido; el Lema vale para todo w ≥ 0. Nada en (D1)–(D3) usa Λ∗1 = log antes de
  recombinar salvo para anular el bloque k ≤ N, que es el uso lineal ya registrado (RULES_AVOID I2).
- **Paridad (R170_870).** Las tres conversiones son cuadráticas y pares, de modo que la objeción de
  paridad no las alcanza directamente; pero lo que queda sin firmar es el término cruzado entre α y la
  parte de β que no factoriza por α, cuyo signo sobre el radical es lo que R170_837 Teor. 5.1 y P47
  eq:equivgate identifican con la conclusión. No se dispone de una operación que lo oriente; la
  candidata no esquiva R170_870, sólo no llega hasta ella.
- **Operación no lineal en F pedida.** No se encontró ninguna. Las operaciones que dependen de F
  (elegir el test, L o la fase según F) dan (D2) o enunciados por vector sobre el radical, donde la
  factorización existe a posteriori (R170_835) y construirla es el cierre.

### (4) Conexión con la positividad global sobre P_T

No hay identidad que la dé. thm:PCfinite es una identidad sobre la recta con test no local
z = S_N𝓕g; para que a_M(F, z) sea a_T(F) hace falta z = F, que no tiene solución con g en la ventana
(REVIEW_001_ABD §4.1). La única conexión escrita es sobre el radical de una ventana de contacto
(R170_816 (3), (11)), y allí exige además firmar B junto con C. Por el Lema, una identidad (G) cuyo
resto contenga la cola como Σ_k h(k)|ℓ_k|² con ℓ_k en momentos de orden ≤ L no existe sobre P_T; la
versión L = ∞ es la matriz alternada (2).

### (5) Líneas que se rompen para cΛ y a_P

No hay paso de signo que someter a la batería; se registra qué ocurre con las identidades escritas.

- cΛ: en (1) aparece el bloque interior (c − 1) Σ_{k≤N} (log k) ‖ℓ_k(F)‖². La igualdad se rompe para
  c ≠ 1, pero para c > 1 el lado izquierdo sigue siendo suma de cuadrados con pesos no negativos: la
  positividad no se rompe. Es la restricción K1 reproducida; (1) no puede ser paso de signo.
- a_P con P > N: el bloque interior es −Σ_{k≤N} (log k) ‖ℓ_k(F)‖² (todos los divisores borrados); se
  rompe la igualdad y el signo. Pero (1) no está ligada a a_T, de modo que esto no acredita nada.
- El Lema y (2) valen para todo peso no negativo: sobreviven a toda la batería. Por la regla 6 eso los
  descalifica como mecanismo; son obstrucción y reformulación.

El cotejo identifica repetición (R161_030–039; P47 eq:Qbalance–eq:equivgate; R170_816, 835, 837) y
no hay mecanismo de signo que escribir. La memo termina aquí.

## Resultado

**Sin mecanismo nuevo.** Además, NO-GO con clase (PROVED, Lema): sobre P_T, con el test de momentos
Σ_L de L finito y cualquier peso no negativo en k > N, la cola no es ± (suma de cuadrados en momentos
de orden ≤ L más resto no negativo), ni siquiera para un solo k, y ninguna corrección diagonal en
esos momentos la vuelve semidefinida.

## Qué se probó

- Identidad (1) (PROVED): la única suma Σ_{k>N} h(k)‖ℓ_k‖² con ℓ_k explícitos es diagonal en 𝒪_LF y
  coincide con la familia c_{N,L} de P47.
- Lema (PROVED): indefinición de C − ⟨α, Bα⟩ sobre P_T para todo B, L finito, w ≥ 0.
- Observación (2) (PROVED): con L = ∞, C es una forma explícita en los momentos Gamma, alternada en j,
  con la aritmética en Θ_j = Σ_{k>N} h(k)k^{2j}. Reformulación exacta; no lleva signo.

## Qué falló y por qué

- La conversión literal en Σ_k h(k)|ℓ_k|² falla porque los funcionales exteriores
  F ↦ ⟨τ_{log k}𝓕F, e_m^±⟩ no factorizan por un número finito de momentos Gamma (analiticidad de ĝ),
  y con todos los momentos factorizan con coeficientes de signo alternado.
- El paso a suma directa en k es la ruta R161_030–039 con otro rango y otro peso; el motivo
  registrado del fracaso no depende de ellos.
- No se encontró operación no lineal en F que diagonalice el par (𝓕F, Σ_LF); las disponibles cambian
  el test y pierden la casilla de D_Δ, o son a posteriori sobre el radical.
- No existe identidad que conecte ninguna de estas formas con a_T sobre todo P_T.

## Siguiente paso concreto

No relanzar «cola como cuadrados» en ninguna variante de rango de k, peso o test de rango finito.
Registrar en el índice (catálogo 04, junto a G4C-R161_030-034) y en el grid el Lema como NO-GO de
clase y la fila K1 del LEDGER como cerrada en la formulación de L finito. Lo único que queda sin
excluir es la matriz (2) completa: una candidata futura tendría que presentar, antes de derivar, una
identidad exacta que sume (2) con los bloques de E_N y de Tate en la misma base de momentos y cuyo
bloque interior (los coeficientes δ_a(k)k^{2j}, k ≤ N, que para Λ son nulos) entre con signo opuesto
al exterior; sin esa operación escrita no hay candidata.
