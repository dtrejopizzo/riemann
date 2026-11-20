# La recta de la meseta como criterio global

**Cotejo.** P45 thm:sufficiency y P47 thm:parityschur distinguen la paridad global y la de una ventana fija. P47 thm:oneprofile fija un perfil y exige todas las matrices de traslaciones. Aquí varía el perfil, pero se evalúa una sola meseta por par de datos y se permite descartar el defecto exponencial firmado de 027. El paso adicional frente a 027 es construir una violación de la recta a partir de cualquier dirección negativa usando el cruce remoto de 028. No se afirma que la desigualdad de la recta esté probada.

Fijar cualquier umbral de ancho R≥0 y cualquier razón L≥1, finitos. Tomar todos los perfiles reales pares F suaves compactos primitivos de masa M=∫F≠0 y todos los D>max(R,L·diam supp F). Escribir H_D=1_[−D/2,D/2]*F, b=m^sharp(0), C_F como en 027 y Φ(H_D) para la fluctuación aritmética de P47 prop:sharp. El signo global equivale a

    Φ(H_D) ≤ b M² D + C_F     para todos esos pares (F,D).

Por homogeneidad puede fijarse M=1. No se prescribe que F sea positivo. Cada H_D es par y primitivo, con una meseta central de altura M. En una ventana común P47 da a(H_D)=a^sharp(H_D)−Φ(H_D). La traslación que centra el cajón no cambia estas formas. Por 027 la diferencia entre la recta y a^sharp es

    S_D(F)=Σ_{k≥1} exp(−2a_kD) |∫F(t)exp(2a_kt)dt|²/(2a_k²),   a_k=k+1/4.

Así, recta−Φ=a(H_D)+S_D(F). La positividad implica la desigualdad.

Recíprocamente, si hay un test negativo, 028 da un G real impar primitivo suave compacto con q=a(G)<0. Para ese G hay D_j→∞ con a(G,V_{D_j}G)→0. Sea F₀=G', par, de masa cero, con los momentos nulos por partes. Su meseta es exactamente G(t+D/2)−G(t−D/2); a lo largo de D_j su energía tiende a 2q. La identidad de 027 es válida para F₀ pues su derivación no divide por M. En particular S_D(F₀)→0: para soporte dentro de [−w/2,w/2], cada sumando está acotado por ||F₀||₁² exp(−2a_k(D−w))/(2a_k²). En consecuencia para j grande recta−Φ, evaluada en F₀, es estrictamente negativa, incluso después de descartar todo el defecto.

Elegir un bump par suave ψ de integral positiva y K=(1/4−∂²)ψ. Es primitivo y tiene masa (∫ψ)/4. Fijar j suficientemente grande para superar R y L veces el diámetro de un intervalo que contenga ambos soportes. Para D=D_j y F=F₀+εK, a(H_D) es un polinomio cuadrático en ε. S_D(F) también es continuo en ε por la mayoración sumable anterior en el soporte común. Para ε no nulo suficientemente pequeño persiste la violación estricta y M≠0. Normalizar la masa conserva el signo de la diferencia. Esto prueba la recíproca. La perturbación puede depender de D_j: la prueba no produce un único perfil de masa no nula con infracciones a anchos ilimitados.

Por el mismo argumento, positividad en todas las mesetas indicadas basta para el signo global. La versión con la recta exige únicamente el mayorante más débil; la obligación abierta es probarlo uniformemente en el perfil permitido. PROVED tras auditoría matemática independiente.
