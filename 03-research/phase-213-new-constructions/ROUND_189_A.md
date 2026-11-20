# Positividad estricta de la forma completa hasta T=129/50

Para 0<T≤129/50, W_T(f)≥exp(−20000000001)||f||₂² en todo el dominio del paper 47. Se usan los datos Z1–Z3 de 175, incluida la altura verificada G=3·10¹². El nuevo tramo respecto de 179 es (2.5,2.58].

**Norma mediante dos aplicaciones del peine.** Sean s=14, U=log s, x=exp t, w(t)=(1+x)/√x y C el peine comprimido a [−U,U]. Con L(y)=Σ_{q≤y}Λ(q)/q y ψ(y)=Σ_{q≤y}Λ(q), la primera aplicación da √x Cw=F(x)=xL(sx)+ψ(sx)+L(s/x)+xψ(s/x). En la segunda se obtiene

    √x C²w = Σ_{q≤sx} Λ(q)F(x/q) + Σ_{q≤s/x} Λ(q)F(xq)/q.

C² tiene núcleo no negativo y es autoadjunto. Basta acotar este numerador por (16.72)²(1+x) para obtener ||C||≤16.72 mediante Schur y ||C²||=||C||². Por reflexión basta 1≤x≤s. Los quiebres internos b=q/s,s/q se reúnen de TODO [1/s,s]; hay que verificar los quiebres externos y todos los bq,b/q transportados que caen en [1,s]. Entre dos extremos el cociente es lineal fraccionario. El valor inclusivo en cada salto domina los dos límites, también para productos de indicatrices. Se verificaron 1758 extremos racionales con bolas Arb de 192 bits. Dos pasos conservan las restricciones de soporte entre desplazamientos sucesivos.

**Aplicación de la fuga y del filtro de 179.** Tomar R=128000000, k=20, m=1070000000 par, H=400000000000 y N=10¹⁰. El filtro de 178 tiene soporte adicional km/H y T+km/H<U; se conserva 2U<5.5. Con la nueva norma, el menorante del símbolo arquimediano menos el peine supera 1/10 para |τ|≥R. Globalmente supera −24 por el piso de 178. Poniendo a=kR²/(3H²), el mismo filtro escalar satisface u≤a en |τ|≤R y u≥(7/2)a para |τ|≥2R por el argumento de 179. Si η es la fuga a partir de Ω=2R, el certificado comprueba m log(7/2)+log η>10 mediante el menorante de 179. Reservada la mitad del margen alto, el piso restante es ≥a^m[(7/2)^mη/20−24]>3a^m. El costo polar es <a^m y a^m>exp(−20000000000). La misma extensión espectral y su máscara de 178–179 dan costo bajo ≤2π exp(−20000000002)<a^m, y densidad correctora alta <1/1000, absorbida por la reserva 1/(80π). Los átomos retenidos tienen peso positivo o cero. Así se obtiene el piso anunciado en ambas paridades. Inclusión de soportes extiende la cota a las ventanas menores.

**Reproducción.** Ejecutar python3 verify_189.py con python-flint. Se revisó independientemente la segunda fila y la necesidad de transportar también los quiebres por debajo de uno. La extensión hereda los lemas analíticos y las hipótesis verificadas de 175–179. La cota no es uniforme en todas las ventanas.
