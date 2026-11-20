# Ronda 20, nota A — índice negativo de la forma arquimediana en P_T para todo T

## 0. Filtro de cuatro puntos

1. **Antecedente más próximo (leído en primario).** Paper 47 (`04-papers/47-row-d-dual-certificates/main.tex`):
   thm:index (l. 2518, índice exacto en (0, 0.90]), subsec:negindex (l. 2630): prop:NC (l. 2638), cor:P3,
   rem:P4, thm:J (l. 2694), **cor:nasym (l. 2722)**, cor:H1; Paper 48 thm:archcount (l. 182);
   índice maestro, Parte VII §1.2 («conteo negativo arquimediano n_−(m_T) ≥ N(T) ≈ 4T», PROVED) y entrada
   «Índice negativo arquimediano, P47 thm:index/P/J/arena» (PARCIAL, herramienta PROVED).
2. **Objeto nuevo.** Ninguno. La pregunta asignada está **resuelta en el corpus**; ver §1.
3. **Por qué evita la dificultad del antecedente.** No aplica: es repetición. Se detiene aquí, sin derivaciones nuevas.
4. **Conexión con la positividad global.** Esto era el paso P1 de una descomposición (localización necesaria),
   no un resultado de signo; ningún peso entra y los tres controles no aplican. El resultado conocido
   **refuta P1 tal como se dibujó** («el signo vive en ≤ 2 direcciones»).

## 1. Lo que ya está probado (CITED, Paper 47)

Notación: m(τ) = Re ψ(¼ + iτ/2) − log π, m(0) = C_0 < 0, m par, creciente en [0,∞), m − C_0 = φ(τ²) con φ
Bernstein completa; τ_0 = 6.28983599… es el único cero positivo de m (la banda negativa del símbolo es |τ| < τ_0).

- **Cota inferior (thm:J, PROVED):** n_−(m_T) ≥ ⌈2Tτ_0/π⌉ − 1 en L²(I), y n_−(Arch|P_T) ≥ ⌈2Tτ_0/π⌉ − 3.
  Prueba: senos de Dirichlet hasta frecuencia < τ_0 más Jensen sobre φ cóncava; P_T quita a lo sumo 2.
- **Cota superior (prop:NC, PROVED):** para todo τ_1 > τ_0, con θ(τ_1) = m(τ_1)/(m(τ_1) − C_0),
  n_−(Arch|P_T) ≤ n_−(m_T) ≤ #{n : λ_n(S_{T,τ_1}) > θ(τ_1)} ≤ ⌊2Tτ_1/(πθ(τ_1))⌋ (operador de
  limitación tiempo–banda S_{T,τ_1}).
- **Asintótica (cor:nasym, PROVED vía Landau–Widom, CITED):**
  n_−(Arch|P_T) = (2τ_0/π) T (1 + o(1)) = 4.0042 T (1 + o(1)), igual para n_−(m_T).
- **Valores exactos (thm:index, PROVED con verificación en aritmética de intervalos):** n_− = 0 en (0, T*_ev),
  1 en (T*_ev, T*_odd), 2 en (T*_odd, 0.90]; T*_ev ∈ [0.58, 0.60], T*_odd ∈ [log 2, 0.81]; caso T = 0.80 abierto
  en el sector impar (rem:odd080).
- **Cotas explícitas (cor:P3):** n_− ≤ 5, 7, 8 en T = ½log3, log2, 0.80. rem:P4: el exceso sobre el valor
  real viene del minorante de dos valores y de codim P_T = 2, no de la teoría prolata (NUMÉRICO, no certificado).
- Por thm:J, n_−(Arch|P_T) ≥ 2 ya para T > π/τ_0 ≈ 0.4995… en L²(I) y ≥ 2 en P_T desde 2Tτ_0/π > 4,
  i.e. T > 2π/τ_0 = 0.99894; y ≥ 3 desde T > 5π/(2τ_0) ≈ 1.2487.

Comparación pedida: 2Tτ_0/π − 2 vale 0.20, 0.78, 1.20, 1.60 en T = ½log3, log2, 0.80, 0.90; los valores
probados 0, 1, {1,2}, 2 son compatibles (la predicción es asintótica; el ⌈·⌉ de thm:J es la versión rigurosa).

## 2. Respuesta

- **n_−(Arch|P_T) NO está acotado por 2 para todo T** (PROVED, thm:J): crece linealmente, con densidad
  exacta 2τ_0/π ≈ 4.004 por unidad de T (cor:nasym), mitad par y mitad impar (P48 thm:archcount).
- **Corrección de P1.** La localización correcta no es a ≤ 2 direcciones sino a un espacio negativo de
  dimensión (2τ_0/π)T(1+o(1)), descrito (ARGUED en cuanto a la descripción fina; la dimensión es PROVED)
  por las funciones prolatas de la banda |τ| < τ_0 en I, restadas las dos condiciones de Tate; el peine debe
  cancelar todas menos ninguna en P_T (P48 §2: «exact cancellation counted in directions»). La reducción
  par exacta es P48 thm:eveninertia: W^ev ⪰ 0 ∀T ⟺ n_−(A_ev) = 1 ∀T (A_ev = a_T par, sin Tate ni polo).
- **(L2) en estos términos.** La matriz S_{T,k} de tamaño 2k−2 (sec:coer, l. 4876; (L2), l. 10683) es el
  complemento de Schur de a_T (no de Arch) sobre las exponenciales de Tate a trozos, con k ≥ k_0(T) elegido
  para que Arch sea coercivo en el complemento 𝒱_k; por rem:coer-size, 2k−2 crece doblemente exponencial en T,
  muy por encima de ≈ 4T: contiene holgadamente el espacio negativo arquimediano, pero no es una base prolata
  de él. Ninguna identificación más precisa está probada (OPEN).

## 3. Qué debe re-derivar un revisor

Sólo la lectura: que thm:J, prop:NC y cor:nasym de Paper 47 dicen lo citado, con la misma forma Arch = 𝔞_∞ en
P_T (sin polo) y el mismo τ_0. Esta nota no prueba nada nuevo. Entrada para el índice (la hará quien
mantiene el índice): «P1 ≤ 2 direcciones: falso para T > 2π/τ_0 por P47 thm:J/cor:nasym — repetición, sin objeto».
