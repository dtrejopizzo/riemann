# Un baricentro de primos con pesos lineales y mínimo en extremos primos

Sea C(x)=Σ_{p≤x}(log p)(1−p/x)(3p/x−1). El signo global del paper 47 equivale a C(q)≥0 para todo primo q suficientemente grande. En cada extremo esto dice que el promedio de los primos p<q, ponderados por (q−p)log p, es al menos q/3. También equivale a una sola comparación de productos enteros, agrupando los factores p^|(q−p)(3p−q)| según el signo del exponente. El umbral q/3 es exactamente el baricentro del peso lineal continuo en [0,q].

**Elección del peso.** Frente al orden variable de 245, tres integraciones con polos distintos 0,−1,−2 dan un peso polinómico. La transformada K(s)=∫₀¹(1−y)(3y−1)y^(s−1)dy=2(s−1)/[s(s+1)(s+2)] mata el principal. Para la suma con von Mangoldt, Perron da bajo RH −Σ K(ρ)x^ρ+O(1+log²x). Se puede desplazar desde Re s=2 a −1/2: sólo se cruza además el origen; en la recta desplazada ζ'/ζ tiene crecimiento logarítmico y K decae cuadráticamente. Las horizontales desaparecen por las alturas libres de ceros de Z3. La inversión vale incluso en nodos al anularse el peso en 1. Los cuadrados retirados de la suma tienen contribución (K(1/2)/2+o(1))√x por el teorema de los primos y sumación parcial en p/√x; los exponentes superiores cuestan O(x^(1/3)polylog x).

En la línea |ρ−1|=|ρ| y |ρ+j|≥|ρ| para j=1,2. Por tanto

    |C(x)/√x−4/15| ≤ 2(2+γ_E−log(4π))+o(1)<0.094+o(1).

Aquí −K(1/2)/2=4/15 y se usó la suma de cuadrados recíprocos de los ceros de selección 092. En sentido inverso, la transformada en x de C para Re s>1 es K(s)Σ_p(log p)p^(−s); se prolonga a Re s>1/2, regular en la semirrecta real allí y con polos en todos los ceros fuera de la recta a la derecha. Landau como en 243 impide signo eventual si existe alguno de esos polos.

**Paso aritmético específico.** Entre dos primos consecutivos escribir x²C(x)=−A₀x²+4A₁x−3A₂, con A_j=Σ_{p≤x}p^j log p. La expresión es continua al entrar un primo y cóncava en todo el intervalo cerrado entre primos. Dos extremos no negativos garantizan todo el intervalo. La misma observación vale para cualquier margen constante en x²C(x), sin control adicional de los huecos entre primos.

**Comprobación y antecedentes.** verify_247.py encierra los logaritmos por enteros escalados y verifica los 9591 extremos desde 3 hasta 99991. Por concavidad esto certifica C(x)>0 en todo [3,99991]. El sesgo positivo por cuadrados, la dominación por la suma de Hadamard y la detección unilateral ya están en 092 y 127. La contribución aquí es el peso polinómico de dos momentos con cancelación exacta del principal y la reducción por concavidad a los primos mismos. Ninguna de estas identidades prueba por ahora la comparación de productos para primos arbitrariamente grandes.
