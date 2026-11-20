# Ronda 7, encargo C — relación no lineal en el peso entre convolución y ventana

Notación de la fase: a_T(F) = Arch(F) − Σ_n v_n c_F(log n), v_n = 2Λ(n)/√n, F real con soporte en
I = [−T,T], F ∈ P_T. Se escribe F̂(ξ) = ∫F(t)e^{−iξt}dt y g_F = c_F ∗ c_F (convolución aditiva), de modo que
ĝ_F = |F̂|⁴ y sop g_F ⊂ [−4T,4T].

## 0. Filtro de cuatro puntos

**(1) Antecedente más cercano, leído en primaria.**
`phase-161-*/R161_033_COHERENT_TO_DIRECT_SUM_GAP.md` §§2, 5A, 7 (salida A: dilatación de Parseval/Naimark con
etiquetas k, nunca construida) y, sobre todo, `R161_034_MELLIN_GRAM_AND_PRODUCT_RATIO_COLLISION.md` §0–1: el Gram
cruzado de las etiquetas se diagonaliza exactamente en frecuencia de Mellin y se parte en términos de igual
orientación, que dependen de k/l, y de orientación opuesta, que dependen de kl («canal cociente» y «canal
producto», ya aislados en la fase 106). RULES_AVOID K2, K3, L3 (BARRIER_D2_001), J2; 211
`POWER_GLOBAL_ROUTE_REVIEW.md`, «Extensión factorial antes de resonancia» (productos de frecuencias distintas
conservados antes de completar cuadrados).

**(2) Objeto propuesto.** La dilatación de la salida A con la regla «el contacto de mn es la composición de los
contactos de m y n», es decir la forma bilineal en el peso
Π_T(F) = Σ_{m,n} Λ(m)Λ(n)(mn)^{−1/2} g_F(log mn),
que por Λ ∗ Λ = μ ∗ log² − Λ·log vuelve a una expresión de grado uno en Λ más un término independiente del peso.

**(3) ¿Evita la dificultad del antecedente?** No. El §2 de esta nota prueba que el canal producto que ve
log m + log n = log(mn) es exactamente el de orientación opuesta de R161_034 y no tiene signo; el canal que
tiene signo manifiesto es el cociente, que no se compone con la incidencia de divisores. Es la misma colisión
producto–cociente. **Cotejo: repetición de R161_034 / fase 106 (K2–K3).** Se detiene la construcción; lo que
sigue sólo fija con precisión por qué, y la operación que reabriría.

**(4) Conexión con la positividad global.** La única identidad candidata sería
a_T(F) = α·Q_T(F) + R_T(F) con Q_T el canal cociente (≥ 0) y R_T el resto; el signo global queda entero en R_T
(patrón J2/L3). No hay desigualdad que conecte.

## 1. Las dos composiciones posibles (PROVED)

Sea a = (a_n) real de soporte finito, A(ξ) = Σ_n a_n n^{−1/2} n^{iξ}. Como g_F(u) = (2π)^{−1}∫|F̂(ξ)|⁴e^{iξu}dξ:

(1.1) Σ_{m,n} a_m a_n (mn)^{−1/2} g_F(log m − log n) = (2π)^{−1}∫|F̂|⁴ |A(ξ)|² dξ ≥ 0.

(1.2) Σ_{m,n} a_m a_n (mn)^{−1/2} g_F(log m + log n) = (2π)^{−1}∫|F̂|⁴ A(ξ)² dξ = (2π)^{−1}∫|F̂|⁴ Re A(ξ)² dξ,

la última igualdad porque F es real (|F̂|⁴ par) y A(−ξ) = conj A(ξ). Verificación formal: sustituir la
representación de g_F e intercambiar la suma finita con la integral.

(1.3) Re A² no tiene signo: con a soportado en un solo n, (1.2) vale a_n² n^{−1} g_F(2 log n), y g_F puede ser
negativo en 2 log n (F = bump·cos(ωt) con ω·2log n ≡ π da g_F(2 log n) < 0 para bump angosto). Por tanto la
composición aditiva de contactos log m + log n sólo aparece en una forma **holomorfa** (A², no |A|²).

## 2. El canal producto vía la convolución (PROVED salvo la identidad citada)

Con a = Λ y la identidad de Selberg Λ·log + Λ ∗ Λ = μ ∗ log² (CITED, clásica):

(2.1) Π_T(F) = Σ_k (Λ∗Λ)(k) k^{−1/2} g_F(log k) = Σ_k (μ∗log²)(k) k^{−1/2} g_F(log k) − Σ_k Λ(k) log k · k^{−1/2} g_F(log k).

Suma finita: k ≤ e^{4T}. Es exacta, no lineal en el peso (grado 2 a la izquierda) y usa la convolución. Pero
por (1.2)–(1.3) el lado izquierdo es ∫|F̂|⁴ Re D², sin signo. Y no involucra c_F en log n, sino g_F en log k con
peso Λ·log: no contiene a_T como sumando.

## 3. El canal cociente y los falsificadores

Q_T(F) := Σ_{m,n} Λ(m)Λ(n)(mn)^{−1/2} g_F(log(m/n)) ≥ 0 por (1.1). Cualquier identidad
a_T = αQ_T + R_T (α > 0) deja el signo en R_T:
- **cΛ, c = 2:** Q_T(2Λ) = 4Q_T(Λ) ≥ 0 sigue no negativo; R_T(2Λ) = Arch − 2·comb − 4αQ_T. El término que
  deja de ser ≥ 0 es R_T, no Q_T: el mecanismo de signo no está en el objeto nuevo. (ARGUED como lectura;
  la parte «Q_T ≥ 0 para todo c» es PROVED.)
- **Borrado de una potencia de primo / peso de Beurling:** Q_T ≥ 0 sigue valiendo (es un cuadrado para
  todo peso real); no distingue. El canal producto (2.1) sí se rompe (Λ'∗Λ' ≠ μ∗log² − Λ'log), pero sin
  signo que perder.

Conclusión: el canal con signo es ciego a la aritmética; el canal aritmético no tiene signo. Es la dicotomía de
R161_034 / fase 106, aquí en forma de lema de dos líneas (1.1)–(1.2).

## 4. Otras variantes descartadas en el cotejo

- Cuadrado de grado dos que suma (K2, R161_030): término ½ΣΣΛ(d)Λ(e)‖m_d − m_e‖², genérico en el peso.
- Defecto de divisores cuadrático exigido para todo peso: objetivo con margen (L3, BARRIER_D2_001).
- Productos de frecuencias distintas conservados antes de completar cuadrados: 211 «Extensión factorial».
- Pesos de criba (Selberg Λ_R) como test: L2, no elevan el grado.

## 5. Operación explícita que reabriría

Una identidad, con fórmula propia, que exprese el canal producto (2.1) **comprimido a la ventana** (con el
borde de [−T,T] y la restricción P_T) como canal cociente comprimido más un concomitante de borde con signo
nombrado — es decir, que convierta Re D² en |D|² usando Λ ∗ 1 = log y la ecuación funcional del factor
arquimediano (el multiplicador u_∞ de R161_034 (1.1), que intercambia orientaciones) — y cuyo resto falle en
signo para c = 2 en un término nombrado. Sin esa identidad, la dilatación de la salida A no aporta mecanismo.
Es la exigencia de R161_034 §0 («compressed ratio channel = boundary concomitant»), no una novedad.

## 6. Lista de afirmaciones

| # | Afirmación | Etiqueta |
|---|---|---|
| 1 | (1.1): canal cociente = ∫|F̂|⁴|A|² ≥ 0 | PROVED |
| 2 | (1.2): canal producto = ∫|F̂|⁴ Re A², forma holomorfa | PROVED |
| 3 | (1.3): el canal producto no tiene signo | PROVED |
| 4 | Identidad de Selberg Λ·log + Λ∗Λ = μ∗log² | CITED |
| 5 | (2.1): reducción exacta del canal producto a grado uno más término sin peso | PROVED (dado 4) |
| 6 | Q_T ≥ 0 para todo peso real, incluido cΛ, borrado y Beurling | PROVED |
| 7 | La dilatación de la salida A (contactos de mn compuestos) cae en la colisión producto–cociente | NO-GO (repetición de R161_034 / fase 106, K2–K3) |
| 8 | Toda identidad a_T = αQ_T + R_T deja el signo entero en R_T | ARGUED (patrón J2/L3) |
| 9 | Operación de reapertura del §5 | OPEN |
