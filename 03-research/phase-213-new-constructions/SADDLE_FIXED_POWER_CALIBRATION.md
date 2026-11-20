# Qué abscisa exige un corte fijo en potencias de log x

Para la suma S* de 368, escribir L=log x y fijar A≥2, z=L^A, b=log z. El punto real α de K'(α)=0 satisface

    α=1−1/A+(log A+o(1))/b,
    K(α)=(1−1/A)L+(1+log A+o(1))L/b.

Las estimaciones son para A fijo. En efecto, para σ=1−1/A+c/b y c acotado, la sumación parcial del teorema de los números primos da
Σ_{p≤z}(log p)p^(−σ)∼z^(1−σ)/(1−σ)∼Ae^(−c)L.
Las potencias superiores aportan O_A(log² z) a la derivada porque σ≥1/2−O(1/b). El signo de K' a c=log A±ε y K''>0 localizan su única raíz. La misma sumación parcial, con el peso adicional 1/log p, da log E_z(α)∼L/b. Esto da la segunda fórmula. El caso A=2 recupera 366–368.

Por tanto, en cualquier corte logarítmico de potencia fija A>2 el desplazamiento hasta la silla pasa a distancia asintótica 1/A a la izquierda de 1. Una franja libre de ceros de anchura decreciente con la altura deja sin controlar los posibles polos de 1/ζ en ese desplazamiento. Esto identifica una obligación precisa de esta deformación del contorno. No establece que toda prueba de signo deba satisfacerla.
