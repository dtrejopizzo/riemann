# Documento de diseño: operador candidato de Hilbert–Pólya

**Objetivo.** Un operador autoadjunto `H` cuyos autovalores sean los ceros `γ`
de `ζ(1/2+iγ)=0`, satisfaciendo la fórmula explícita de Weil (verificada
numéricamente en `selector_weil.py`).

**Advertencia franca.** Este es un *candidato / blueprint*, no una solución.
Diseñar el operador no es la parte difícil (se hizo varias veces). La parte
difícil —y no resuelta— es **probar que su espectro es real** (equivalente a RH).
Lo que sigue es la mejor ingeniería inversa disponible, con el hueco marcado.

---

## 1. Propiedades forzadas por la ecuación (spec)

De igualar la fórmula explícita con la fórmula de traza de Gutzwiller:

- Espacio: `L²(ℝ⁺, dx)` (semirrecta).
- Término de Weyl: `N(T) = (T/2π)(log(T/2π) − 1) + 7/8`.
- Núcleo dinámico: generador de dilataciones `H₀ = ½(xp + px) = −i(x d/dx + ½)`.
- Órbitas periódicas de longitud `log p^k`, inestabilidad de Lyapunov = 1.
- Simetría temporal **rota** (estadística GUE, no GOE).

## 2. Candidato explícito (Bender–Brody–Müller, 2017)

    H  =  1/(1 − e^{−ip}) · (x p + p x) · (1 − e^{−ip})

sobre `L²(ℝ⁺)` con la condición de contorno `ψ(0) = 0`, donde `p = −i d/dx`.

Propiedades demostradas por BBM:
- `H` es simétrico respecto de un producto interno modificado (PT-simétrico).
- Formalmente, `(1 − e^{−ip})` actúa como "peine" que introduce los enteros
  `n` (y por tanto los primos vía `Λ(n)`): ahí entran las órbitas `log p`.
- Los autovalores `E_n` satisfacen, formalmente, `ζ(1/2 + i E_n) = 0`.

## 3. El hueco (lo que tenés que probar)

**Lema abierto (= RH).** El espectro de `H` es **real**.

Equivale a: la simetría PT de `H` está **no rota** (autovalores reales, no en
pares complejos conjugados). BBM lo redujeron a mostrar que un cierto operador
de similaridad `e^{−? }` que "hermitiza" `H` está bien definido y es acotado.
Eso **no se probó**.

Rutas equivalentes al mismo lema (elegí tu frente):
- **(a) Autoadjunción real:** exhibir el producto interno respecto del cual `H`
  es genuinamente autoadjunto (no solo simétrico), y probar que es definido
  positivo. [Problema de dominio / extensiones autoadjuntas.]
- **(b) Positividad de Weil (tu MW-1):** probar `Σ_γ h(γ) ≥ 0` para toda
  `h = φ⋆φ̃`. Equivale a la realidad del espectro por la fórmula explícita.
- **(c) Órbitas de Connes:** realizar las `log p` como longitudes de geodésicas
  cerradas en el espacio de clases de adeles y probar la positividad de la traza.

## 4. Por qué "diseño → vos probás" no reduce la dificultad

Las tres rutas (a),(b),(c) son **la misma dificultad** con distinto disfraz, y
es la que resistió a Weil, Selberg, Berry, Keating, Connes, Bender–Brody–Müller.
El diseño está hecho; la obstrucción es un teorema de positividad/realidad que
nadie sabe probar. No es cuestión de esfuerzo de cálculo: es una barrera
estructural. Cualquiera que te entregue "el operador ya probado" te está dando
un candidato con el Lema §3 asumido, no demostrado.
