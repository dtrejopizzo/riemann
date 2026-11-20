# Ronda 9, encargo G1 — objeto con papeles invertidos: la aritmética como fuente de signo

Notación de la fase: a_T(F) = Arch(F) − Σ_n v_n c_F(log n), v_n = 2Λ(n)/√n, F real, sop F ⊂ [−T,T], F ∈ P_T.
N_T: subespacio negativo de Arch sobre P_T (no depende del peso), no trivial para T por encima del umbral
arquimediano (Paper 47 cor:Tarch; umbral en [0.58, 0.60]).

## 0. Cotejo previo (en primaria y en el índice)

Lo que el corpus ya tiene sobre N_T y sobre los contactos como fuente:

- Paper 47 cor:Tarch y Theorem P (n₋ ≤ 5/7/8): N_T existe y su dimensión está acotada en los primeros
  umbrales; los invariantes enteros (índice de Pontryagin) quedan cerrados (BARRIER_W_001; índice 05b).
- phase-155 R155_029 («los primos son necesarios» pasado ≈0.596), R155_026/032 (reducción de Schur), R155_044
  (explicación nodal de la cancelación 2/3): describen N_T; no dan signo.
- phase-186 Thm A/B, Cor (L1): reducción exacta a la matriz finita S_{T,k}; (L2) OPEN. Las rondas de Schur de la
  fase 211 (ROUND_005_C, 007_B, 015_B, 017_A) terminan con el signo en el acoplamiento a la precisión del margen
  (excluido por el encargo, punto iv).
- **phase-188 N_BUILD_001 (A) y N_BUILD_011 (+ revisión):** este es el antecedente directo de la inversión de
  papeles. Sobre P_T, la parte media del peso, ρ_1 = 2e^{u/2}du, cumple ∫₀^{2T} c_F dρ_1 = −𝔭(F) ≤ 0, de modo que
  la densidad media de los contactos **aporta +𝔭(F) ≥ 0**: el símbolo pasa de m a m^♯ = m + 1/(¼+τ²). Es
  exactamente «la aritmética (su término principal) es fuente de positividad sobre las direcciones negativas
  de Arch». N_BUILD_011 Teorema 1: ρ_κ ∈ Pos ⟺ κ ≥ κ*, con κ* ≥ |C₀|/4 ≈ 1.343 > 1. La densidad media sola
  (κ = 1) no alcanza (índice 06, «pointwise symbol positivity (κ=1<κ*)», NO-GO; Paper 47 thm:nolocal, W-loc;
  thm:ceiling para densidades enteras).
- **phase-188 L2_BUILD_017:** identidad Λ = μ∗log en operadores de traslación,
  a_T(F) = 𝔞_∞(F) − 2Re⟨U_μF, U_logF⟩ (N_BUILD_002 §1, N_BUILD_005 §1), y certificados de partición tipo
  AM-GM con W. El residuo vivo registrado (índice 06, línea 56, (a)) es una **desigualdad de antialineación
  entre U_μF y U_logF sobre 𝒩_T**, cuantificada contra el símbolo de déficit (κ*−1)/(¼+τ²).
- Walls W-lin, W-det, W-fam, W-pat, W-loc, W-mom (fase 186): todo discriminante de primer orden es funcional de
  h*, no de σ; certificados lineales de marco fijo muertos; localidad muerta.
- RULES_AVOID §§O–R, REVIEW_007 R7-a (cotas por potencial mueren antes de 0.60), R7-c (canal de cocientes ∫ĝ|A|²
  ciego a la aritmética), ROUND_008_A (concomitante de borde = conmutador de soporte, fase 161).

Conclusión del cotejo: la inversión de papeles **ya está escrita en el corpus** en su forma natural (densidad
media → +𝔭; fluctuación Λ−1 como resto) y su residuo abierto es (a). Las candidatas siguientes se presentan
contra ese antecedente; ninguna se deriva más allá de la puerta.

## 1. Candidata C1 — densidad media como fuente, fluctuación como pago

1. Antecedente: N_BUILD_001 (A), N_BUILD_011 Teorema 1, L2_BUILD_018 (peines atómicos en Pos).
2. Objeto nuevo: ninguno. a_T = (1/2π)∫m^♯|F̂|² − ∫ Re c_F d(Λ-peine − ρ_1).
3. Esquiva: no. Como κ = 1 < κ*, m^♯ tiene parte negativa (m^♯(0) = C₀ + 4 < 0, CITED de la revisión de
   N_BUILD_011); la fluctuación debe aportar positivamente: es el problema original.
4. Conexión global: la de N_BUILD_011/012 (segmento λ_t entre ρ_κ y Λ; residuo t_∞ > 0, OPEN).
- Falsificadores, lectura (ARGUED): con cΛ, c = 2, la parte media es ρ_2; si κ* ≤ 2 la media sola es positiva y
  la ruptura ocurre en la fluctuación 2(Λ−1), cuyo término −2∫Re c_F d(Λ−1) deja de ser dominado (no se puede
  nombrar sin conocer κ*: sólo κ* ≥ 1.343 está probado). Borrar una potencia p^k: media intacta, la fluctuación
  gana el átomo +v_{p^k}c_F(k log p), indefinido en F. Peso de Beurling: cambia κ efectivo y la fluctuación.
- Dictamen: **repetición**. Se detiene.

## 2. Candidata C2 — polarización del par Möbius–log

Con la identidad de L2_BUILD_017, −2Re⟨U_μF,U_logF⟩ = ‖U_μF − U_logF‖² − ‖U_μF‖² − ‖U_logF‖² (PROVED,
polarización), luego
  a_T(F) = [𝔞_∞(F) − ‖U_μF‖² − ‖U_logF‖²] + ‖U_μF − U_logF‖².
El cuadrado se construye con los contactos usando la estructura multiplicativa (μ∗log = Λ) y aditiva (traslaciones
τ_{log n}); el arquimediano «paga» las dos normas.

1. Antecedente: L2_BUILD_017 §2–§4 (certificados de partición, AM-GM con W; W = 1 es esta identidad).
2. Objeto nuevo: sólo el reparto inverso de la misma polarización. Con W general, la familia de L2_BUILD_017
   la contiene (signo opuesto en el término cruzado = cambio U_μ → −U_μ).
3. Esquiva: no. ‖U_logF‖² crece con N = e^{2T} (los pesos log n/√n no son sumables en ℓ²: ARGUED), así que el
   corchete es muy negativo y el cuadrado debe llevar todo el signo: traslada la obligación sin mecanismo.
4. Conexión global: ninguna nueva.
- Falsificadores (ARGUED): c = 2 duplica el término cruzado; la identidad pasa a llevar ‖U_μF − 2U_logF‖² y el
  pago crece en 3‖U_logF‖²; borrar p^k rompe μ∗log = Λ (el resto es +v_{p^k}c_F(k log p)); Beurling: la
  convolución μ_B∗log_B sigue valiendo, el término que cae es el arquimediano, que ya no ajusta la media.
- Dictamen: **repetición** (L2_BUILD_017; residuo (a) del índice 06). Se detiene.

## 3. Candidata C3 — antialineación restringida a N_T (la mejor; operación faltante)

Se busca: para F ∈ P_T, con proyección F₋ sobre N_T, una desigualdad
  −2Re⟨U_μF, U_logF⟩ ≥ −Arch₊-parte controlada + (cota inferior positiva en F₋)        (∗)
es decir, que sobre N_T el término cruzado de contactos sea **positivo** y supere |Arch(F₋)|, con las direcciones
de P_T ⊖ N_T pagadas por Arch.

1. Antecedente: índice 06, línea 56, residuo (a) (L2_017 lección; N_011). Sin ejecución registrada.
2. Lo nuevo exigible (no escrito): una identidad exacta que exprese Re⟨−U_μF₋, U_logF₋⟩ − |Arch(F₋)| como suma
   de cuadrados usando Σ_{d|n}Λ(d) = log n (aditivo en el exponente de traslación: τ_{log n} = Π τ_{log p^k}).
3. Por qué podría esquivar R7-a/R7-c: no acota contactos por arriba (aporte positivo en N_T) y no es el canal de
   cocientes (es cruzado μ–log, no |A|²).
4. Conexión global: (∗) con constante uniforme en T y dim N_T acotada (Theorem P sólo da cotas en los primeros
   umbrales; para T grande dim N_T crece, ARGUED) daría a_T ≥ 0 en P_T vía cuadrado de Schur 2×2 por bloques.
- Primer caso no trivial: T = 0.5925 (falsificador de §O), N_T de dimensión 1, donde (∗) se reduce a un número.
- Problema de fondo: un bloque 2×2 (N_T, su complemento) con el acoplamiento cruzado a la precisión del margen es
  precisamente la reducción excluida por el punto (iv). Sin la identidad de suma de cuadrados del punto 2, C3 es
  Schur con otro nombre.
- Dictamen: **no pasa** mi propio control.

## 4. Conclusión

Ninguna candidata sobrevive. La inversión de papeles en su forma natural existe en el corpus (N_BUILD_001 (A):
la densidad media de los contactos aporta +𝔭 ≥ 0 sobre P_T) y falla porque κ = 1 < κ*. **Operación faltante
precisa** (para C3): una identidad exacta, válida en todo P_T y todo T, que escriba
  −2Re⟨U_μF, U_logF⟩ − ∫Re c_F dρ_1 + (parte negativa de m^♯ en F)
como suma de cuadrados en las traslaciones τ_{log p^k}, compuestas por la ley τ_{log m}τ_{log n} = τ_{log mn}, cuyo
término que pierde el signo bajo c = 2, borrado de p^k y Beurling sea nombrable. Sin esa identidad el déficit
(κ*−1)/(¼+τ²) sigue en la fluctuación.

## 5. Lista de afirmaciones y etiquetas

| Afirmación | Etiqueta |
|---|---|
| Sobre P_T la densidad media ρ_1 aporta +𝔭(F) ≥ 0 (N_BUILD_001 (A)) | CITED |
| ρ_κ ∈ Pos ⟺ κ ≥ κ*, κ* ≥ 1.343 > 1 (N_BUILD_011 Teorema 1) | CITED |
| La inversión natural de papeles es repetición de N_BUILD_001/011 | ARGUED (cotejo) |
| Identidad de polarización de C2 | PROVED (trivial) |
| C2 contenida en la familia de L2_BUILD_017 | ARGUED |
| ‖U_logF‖² crece con T y el corchete de C2 se hace muy negativo | ARGUED |
| Lecturas de falsificadores (c = 2, borrado, Beurling) en C1–C2 | ARGUED |
| Para c = 2 la ruptura puede estar en la fluctuación y no en la media (si κ* ≤ 2) | CONDITIONAL (a κ* ≤ 2, OPEN) |
| C3 sin identidad nueva coincide con la reducción de Schur excluida | ARGUED |
| Desigualdad (∗) de antialineación sobre N_T | OPEN |
| Signo global de a_T en P_T | OPEN |
