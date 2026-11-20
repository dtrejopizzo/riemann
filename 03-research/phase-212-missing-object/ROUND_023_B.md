# ROUND_023_B — Puerta: (PC) comprimida antes de emparejar y orientación del salto terminal

Pregunta. ¿Existe una operación fuera de 𝒞_w, que no sea un cuadrado, que oriente el salto
h_p(p) − h_{p−1}(p) = −log p (R161_002 Cor. 8.2) usando la no conmutación de P_T con 𝓕, mediante
C_T = (1−P_T)𝓕P_T, C_T^{(N)} = (1−P_T)S_N𝓕Π_T y E_{N,T} = P_T(S_N𝓕 − JS_N)Π_T?

Veredicto: **NO PASA (sin mecanismo).** No es repetición literal: el terreno figura como abierto
(RULES_AVOID K7; ROUND_004_A, «No excluido»; índice maestro B.2 ítem 27). Pero no puedo escribir una
fórmula que oriente el salto sin caer en un formato afín en el peso, en un cuadrado o en un
peso que instala la respuesta.

## (1) Antecedente más cercano (abierto y leído)

- R161_002 §3: define C_T, C_T^{(N)} y E_{N,T}; único escape declarado = «keep the boundary compression
  before taking the square or the oriented pairing»; el resto sin compresión vuelve a R160_D4_R2 Teor. 5.1.
- R161_002 §4 (SP-161) y §5 (L161.1): a_T = Σ w_N Re⟨R_{M,N}F, S_N𝓕F⟩ + B_T(F); reglas: la norma
  falla por Teor. 1.1, los pesos espectrales instalan la respuesta y una factorización de Douglas es EQUIV.
- R161_002 §8: Teor. 8.1 (NO-GO, w ≥ 0) y Cor. 8.2 (−log p como derivada terminal).
- ROUND_004_A Lema 1, Cor., Prop. 2: en 𝒞_w (w reales) no hay telescopado interior más cancelación de
  cola (Σw = 1 contra Σw = 0); la derivada pura δ_{N+1} − δ_N da coeficiente G(1) = 0 (a_T no aparece).
- R161_032 §§4–6: (4.2) 0 = X_T + ‖r‖² + D^orient + 2D^Γ, OPEN/TERMINAL; RULES_AVOID K1 («reabrir exige
  una identidad que conecte un cuadrado de fuga con el defecto de PC, no otro cuadrado de fuga»), K2
  (varianza orientada 030, genérica), U2 (L161.3 orientado OPEN; R161_029 monotonía falsa).

## (2) Lo que sí se puede escribir y lo que no

Observación (ARGUED, cálculo de soporte, no derivado más allá de esto). Para un primo p > e^{2T}, el
salto en N de E_{N,T} es

  E_{p,T} − E_{p−1,T} = p^{−1/2} P_T(τ_{log p}𝓕 − Jτ_{log p})Π_T = p^{−1/2} P_T τ_{log p}(1−P_T)𝓕Π_T,

porque Jτ_{log p}Π_T y τ_{log p}P_T𝓕Π_T se soportan fuera de (−T,T). Es decir: tras comprimir,
**el salto terminal en los primos grandes vive entero en la fuga** (1−P_T)𝓕Π_T, y lo que no conmuta
(P_T con 𝓕) es lo único que lo ve. Esto es exactamente lo que R161_002 §3 dejó anunciado.

Lo que la operación pedida necesitaría: un funcional Φ_T(F), no cuadrado, fuera de 𝒞_w, con
Φ_T = a_T(F) + (términos ≥ 0), en el que la suma de esos saltos ponderados por Λ entre con signo fijo.
Las tres vías del encargo dan:

- (i) Tests distintos de S_N𝓕F: el par ⟨G, Σ_p Λ(p)p^{−1/2}P_Tτ_{log p}(1−P_T)𝓕F⟩ es lineal en Λ para
  G fijo (afín en el peso: F3); con G = G(F) cuadrático o normado reaparece un cuadrado (Teor. 1.1) o
  el test colapsa en el apareamiento mixto de (PC-ren) (R161_023; K1). No tengo un G que escape a ambos.
- (ii) Pesos w_N(F): para cada F fijo la identidad es escalar y el peso es un real por F; elegirlo para
  que la identidad cierre es resolver a_T(F) dentro del peso (SP-161: «installs the answer»). Sin una
  regla canónica previa a Λ (exigencia de L161.1) no hay fórmula.
- (iii) R161_032 (4.2): sigue sin derivar; la fuente exige partir de las dos orientaciones no
  recombinadas y polarizar con el puerto reflejado. No dispongo de la identidad de Green de borde que
  produzca ε⟨v,j⟩ junto a D^orient y D^Γ; no la invento.

## (3) Por qué no evita el fracaso del antecedente

El fracaso de 𝒞_w es aritmético en el índice N: cualquier peso fijo da log p·Σ_{N<p}w_N en p. La
compresión cambia el portador del salto (pasa a la fuga) pero no su forma: sigue siendo
Λ(p)·(operador fijo independiente de Λ). Orientarlo requiere grado ≥ 2 en Λ (F3: lo afín es ciego)
y el único término de grado 2 conocido en esta arquitectura es la varianza de divisores (K2), que se
anula para todo peso (genérica). Ninguna de (i)–(iii) aporta un término de grado 2 no genérico.

## (4) Conexión con 𝔸_M ⪰ 0 y controles

Identidad necesaria (no disponible): a_T(F) = Φ_T(F) − (suma de cuadrados de fuga de C_T, C_T^{(N)})
con Φ_T ≥ 0 por un signo orientado del salto comprimido; vía Paper 47 prop:AM daría 𝔸_M ⪰ 0 para M ≥ e^{2T}.
Controles: con la observación de (2) el salto comprimido es p^{−1/2}·w(p)·(operador fijo) para
cualquier peso w; por tanto (a) peso 2Λ sustituido, (b) potencia borrada y (c) Beurling pasan por el
mismo paso sin romperse: **ningún paso con nombre falla** bajo los tres controles (F1 incumplido). Esa es
la razón del veredicto.

## Estado

- Observación del salto en la fuga: ARGUED (soporte; sin uso como prueba).
- Operación orientadora fuera de 𝒞_w y no cuadrada: OPEN, sin fórmula.
- K7 sigue abierto; esta puerta no lo cierra ni lo excluye.
- Registro: no edito el índice (lo hace quien coordina).
