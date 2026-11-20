# Ronda 16, memo A — Curvatura (Γ₂, Bakry–Émery, Lichnerowicz) como fuente del signo

Notación del brief común: a_T(F) = Arch(F) − Σ_n v_n c_F(log n) sobre P_T, v_n = 2Λ(n)/√n. Controles: cΛ con c = 2,
borrado de una potencia de primo, peso de tipo Beurling. m(τ) = C_0 + ∫_0^∞(1 − cos τu)K(u)du es el símbolo de Arch.

## 0. Cotejo (leído en primaria)

Búsqueda en 03-research, índice y grid de «Bakry», «Γ₂», «Gamma_2», «carré du champ», «curvature», «Lichnerowicz»,
«Ollivier», «Erbar», «Beurling–Deny», «Dirichlet form», «log-Sobolev». Coincidencias que deciden:

- **Fase 64, `CURVATURE-computation.md`** §§2–5: Γ₂ exacto del generador de saltos primo, núcleo B^{∘2} con
  B(ξ,η) = ½[ψ(ξ)+ψ(η)−ψ(ξ−η)]; Teorema 2: CD(0,∞) por producto de Schur si los pesos son ≥ 0; §4: CD(0,∞) es
  marginal (ψ(0) = 0, sin hueco); §5: «el factor arquimediano aporta la curvatura» (suma de curvaturas). Índice
  04 (G2D-R160_S2 §3.1): DEAD [F3: cualquier peso no negativo].
- **Fase 195, `INV_N_001_BAKRY_EMERY_GAMMA2_GAP_CEILING_NO_GO.md`** §§1–3: exactamente la descomposición del
  encargo, a_T = E_T + ∫W_T F² con E_T forma de Dirichlet del proceso censurado de saltos (núcleo arquimediano ν
  más átomos ½v_n en ±log n) y potencial W_T; fórmula exacta de Γ₂, **cuadrática en J**, con términos mixtos
  arquimediano–primo y primo–primo (las composiciones de saltos log p, log q que el encargo propone como canal
  de productos y cocientes ya figuran ahí). Teorema 3.3 (techo de hueco): toda transferencia
  curvatura/Poincaré da ≤ g_T + ess inf W_T < 0 en T = ½log 3, donde la positividad está probada. Índice README:
  «no reintentar Γ₂/CD/log-Sobolev/Poincaré de la parte de saltos sin un insumo que acople E_T y W_T».
- **Fase 160, `R160_M10_R1.md`**: generador de Doob de la forma, T3 (forma Γ₂ del enunciado:
  ‖L r‖² ≥ ½E(r), i.e. integrado de Bakry–Émery), T4 (techo de curvatura puntual ρ ≤ ¼), P1 (gauge); líneas
  63 y 79: con medida ν con signo «E no es una forma de Dirichlet y el argumento Markov no aplica».
- `RULES_AVOID.md` W4 (Lema T, Lema K), X2, Y3; `ROUND_012_A` Prop. B (formato Lyapunov); `ROUND_013_C` O6
  (Mourre/virial = Lyapunov); `ROUND_015_C` (Lema A: afinidad en c; Prop. B de Prékopa). Conmutador [X, S_N] = −K_N
  de R161_001: familia R161_057–065 (X3, J5).

**Conclusión del cotejo.** Γ₂ de la parte de saltos con tasas positivas, su carácter cuadrático en el peso, los
términos mixtos entre primos y la transferencia Bakry–Émery ⇒ Poincaré son **repetición** (fase 64, INV_N_001,
R160_M10_R1). Lo único no registrado literalmente es la variante **con tasas primas negativas** (generador con
signo, no Markov), que R160_M10_R1 sólo señala como fuera de su argumento. Examino esa variante con la puerta y
la cierro con un lema de clase (§2). Ollivier y Erbar–Maas se tratan en §3.

## 1. Puerta de cuatro puntos (variante con signo)

1. Antecedente: INV_N_001 §§1–3; R160_M10_R1 T3–T4.
2. Afirmación nueva: escribir a_T = E^{(L)}(F) := ⟨−LF, F⟩ con L = L_∞ − L_arith (tasas primas negativas) y usar
   Bochner–Lichnerowicz (integrado o puntual) para L.
3. Por qué evitaría el techo: INV_N_001 separa E_T ≥ K·Var y W_T; con signo en las tasas, potencial y saltos
   quedarían acoplados dentro de un solo generador.
4. Desigualdad global: Γ₂^L ≥ κΓ^L (+ N^{−1}(Lf)²) ⟹ «hueco» ⟹ a_T ≥ 0 para todo T.

El punto 4 falla por el Lema L (abajo): Lichnerowicz no produce signo sin Γ ≥ 0. **No pasa la puerta.**

## 2. Lema de clase

**Lema L (Lichnerowicz es ciego al signo; PROVED).** Sea L simétrico en L²(I) (o en P_T con la métrica L²), con
dominio D, y sean Γ, Γ₂ formas puntuales cualesquiera con ∫Γ(f) = ⟨−Lf,f⟩ =: E(f) y ∫Γ₂(f) = ‖Lf‖² (identidades
de integración que valen para todo generador simétrico de saltos con L1 = 0, con o sin signo en las tasas). Si
Γ₂ ≥ κΓ + N^{−1}(Lf)² puntualmente (o sólo integrado), con κ > 0, N ∈ (1,∞], entonces para cada autovector
−Lf = λf se obtiene λ(λ(1 − 1/N) − κ) ≥ 0, es decir
  spec(−L) ∩ (0, κN/(N−1)) = ∅,
y nada más: la condición es compatible con autovalores λ ≤ 0 arbitrarios.
*Prueba.* Integrar: λ²‖f‖² ≥ κλ‖f‖² + λ²‖f‖²/N. Recíprocamente, si spec(−L) ∩ (0,κN/(N−1)) = ∅, la desigualdad
integrada ‖Lf‖²(1 − 1/N) ≥ κE(f) vale por cálculo espectral (cada componente con λ ≤ 0 contribuye ≥ 0 a la
izquierda y ≤ 0 a la derecha). ∎

**Corolario L′ (PROVED).** En el caso Markov el signo de λ viene de Γ ≥ 0 puntual (tasas ≥ 0), no de Γ₂; con tasas
con signo, «E(f) ≥ 0» es el enunciado mismo (J3). Toda la información de signo de una cadena Bochner–Lichnerowicz
reside en Γ ≥ 0, y Γ ≥ 0 puntual exige tasas ≥ 0, que es ciego por el Lema K (vale para todo peso ≥ 0).
**Controles.** En c = 2 (forma con direcciones negativas), en el borrado y en Beurling, la versión integrada de
CD(κ,N) vale siempre que el espectro de −L_c evite (0, κN/(N−1)): la «desigualdad de curvatura» no se rompe en los
controles por estructura sino sólo por accidente espectral; por el Lema T de la ronda 13 un certificado que use
sólo CD más Γ₂ con signo prueba lo falso. (La razón explícita de que el resto deje de ser ≥ 0 no existe: no hay
resto que deje de serlo; el falso enunciado E ≥ 0 se infiere sólo si se agrega Γ ≥ 0, que también falla en c = 2.)

**Respuesta a (1), reconstrucción inversa (PROVED).** (a) Arch no es lado Γ₂ de ningún generador: ∫Γ₂ = ‖L′F‖² ≥ 0
mientras m(0) = C_0 < 0 y Arch tiene direcciones negativas sobre P_T por encima del umbral arquimediano. (b) Lo que sí
es cuadrado es Arch − C_0‖F‖² en ℝ: m − C_0 = ψ_∞ es negativa definida (Lévy–Khintchine con K > 0), y √ψ_∞ también lo
es (subordinación de Bochner, CITED), de modo que Arch − C_0‖·‖² = ‖L′F‖² con L′ de tasas positivas y símbolo √ψ_∞
(en la ventana, más términos de borde). Entonces a_T ≥ 0 se lee ‖L′F‖² ≥ |C_0|‖F‖² + Prime(F) + borde: Γ₂ de **un**
generador contra Γ de **otro**. Ningún teorema de Bakry–Émery compara Γ₂^{L′} con Γ^{L_arith} de un generador
distinto; es una comparación de dos formas, cada una ciega, es decir el enunciado (J3). (c) La identidad de
Tate–Beckner X + 𝓕X𝓕 = m(D) no da m = ℓ² por (a).

**Respuesta a (2) (PROVED).** Con L_c = L_∞ − cL_pr, ∫Γ₂^{L_c} = ‖L_∞F‖² − 2c⟨L_∞F, L_prF⟩ + c²‖L_prF‖², cuadrático en c
con acoplamiento primo–primo en los retardos log(pq), log(p/q) (como en INV_N_001 §2). Pero el enunciado es afín en c
(E^{(c)}), y la única desigualdad nombrada, CD(κ,N), equivale por el Lema L a una laguna espectral alrededor de 0,
que no distingue c = 1 de c = 2, ni el borrado, ni Beurling. Puntualmente, Γ₂ ≥ 0 en ℝ ⟸ B_c ⪰ 0 (Schur) ⟺ ψ_c
negativa definida ⟺ tasas ≥ 0 (Schoenberg, CITED); con c > 0 en tasas negativas B_c no es ⪰ 0 y no hay sustituto.

**Respuesta a (3) (ARGUED).** Γ es bilineal en funciones para un L fijo; [X, S_N] es una derivación sobre
operadores. Coinciden formalmente sólo si X es la derivación asociada a un L de difusión (Γ(f,g) = (Xf)(Xg)); el
formato resultante es el del conmutador de R161_057–065 (X3, J5) y el Lyapunov de ROUND_012_A Prop. B.
Λ∗1 = log no entra en ningún paso del Γ-cálculo (actúa en productos L·S_N, W3).

## 3. Otras curvaturas

- **Ollivier (W1-contracción) y Erbar–Maas/Mielke (curvatura entrópica):** definidas para semigrupos de Markov
  (núcleo de transición ≥ 0, medida reversible). Con tasas con signo e^{tL} no es Markov; una contracción en una
  norma, ‖e^{tL}‖ ≤ e^{−κt}, equivale a rango numérico de L ≤ −κ, que es el enunciado (J3). Con tasas ≥ 0 son
  ciegas (Lema K). PROVED en esa dicotomía; la «contracción entre escalas» de ROUND_009_G3 sigue sin objeto.
- **Bochner discreto / curvatura en grafos (Lin–Yau, Schmuckenschläger):** misma dicotomía, Lema L.

## 4. Veredicto y etiquetas

| # | Enunciado | Etiqueta |
|---|---|---|
| 1 | Γ₂/CD de saltos con tasas ≥ 0, términos mixtos entre primos, transferencia a Poincaré | repetición (fase 64; INV_N_001; R160_M10_R1) |
| 2 | Lema L: CD(κ,N) integrado ⟺ spec(−L) ∩ (0,κN/(N−1)) = ∅; ciego al signo | PROVED |
| 3 | Cor. L′: el signo de Bochner–Lichnerowicz viene sólo de Γ ≥ 0 (tasas ≥ 0: ciego; con signo: J3) | PROVED |
| 4 | Arch no es lado Γ₂ (C_0 < 0); Arch − C_0‖·‖² = ‖L′F‖² en ℝ con símbolo √ψ_∞ | PROVED mod. CITED (subordinación) |
| 5 | Comparar Γ₂^{L′} con Γ^{arith} es el enunciado | PROVED (J3) |
| 6 | Ollivier/Erbar–Maas: Markov ⇒ ciego; no Markov ⇒ rango numérico = enunciado | PROVED en la dicotomía |
| 7 | [X,S_N] como carré du champ: formato R161_057–065 | ARGUED |
| 8 | Curvatura con signo como fuente del signo | NO-GO en la clase Bochner–Lichnerowicz (Lema L) |

Para el revisor: rederivar el Lema L (incluida la recíproca espectral) y la afirmación de que las identidades
∫Γ = E, ∫Γ₂ = ‖Lf‖² valen para tasas con signo (sólo usan simetría y L1 = 0); y la cuenta de (2).

**Siguiente operación explícita (OPEN).** El Lema L muestra que el único insumo de signo en cualquier cálculo de tipo
Γ es una positividad puntual de primer orden. Lo que queda fuera de la clase es una forma puntual Γ̃(F)(x) ≥ 0
**no** asociada a tasas ≥ 0, con ∫Γ̃ = a_T + (término ciego ≥ 0), cuya positividad puntual en cada x sea una
desigualdad finita entre los v_n en el retardo x que use una relación aditiva exacta y falle en los tres controles.
No tengo tal Γ̃; si se propone, debe cotejarse antes con ROUND_015_C Cor. B′ (reparto puntual con signo, clase O/O3).
