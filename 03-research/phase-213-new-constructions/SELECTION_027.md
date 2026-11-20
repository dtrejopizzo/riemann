# Selección de promedios de ancho creciente

Tras el óptimo en diámetro pequeño de 010-A se cotejaron dos opciones de ancho D arbitrario. Veredicto de los dos cotejos independientes: detener estas propuestas. No se añadió un mecanismo de signo.

* Promedio uniforme. Para un perfil primitivo suave y compacto F de masa logarítmica cero, su antiderivada G desde menos infinito también es compacta y primitiva por integración por partes. La integral de las traslaciones entre 0 y D es G−V_DG. Su signo ya cae en la banda de dos traslaciones de P47, lem:transl y thm:band. Para masa distinta de cero la antiderivada tiene una cola constante: separar las dos energías individuales sería inválido. El promedio sigue siendo un test legítimo; su signo sigue abierto fuera de las ventanas conocidas.
* Promedio con densidad exponencial e^(−s/2). Para F primitivo, G(t)=e^(−t/2)∫_{−∞}^t e^(u/2)F(u)du es compacto. La integral ponderada de las traslaciones entre 0 y D es G−e^(−D/2)V_DG. El operador es el resolvente causal de P47 rem:Sren y su uso como filtro tiene antecedente en POWER_DESCENT_016. Escribir A,B para los momentos con exponentes +1/2,−1/2. Por partes, F=G'+G/2 tiene A(F)=0 y B(F)=B(G). En particular la imagen del operador sobre perfiles primitivos suaves compactos abarca todo el sector suave compacto B(G)=0. Por el cruce de 018-A, e^(−D/2)a(G,V_DG) tiende a −conj(B(G))A(G)=0. Se recupera a(G)=W(G) como límite y queda por decidir su signo. Si A(G)≠0, otra aplicación del resolvente produce una cola exponencial de soporte infinito.

Reapertura para estas opciones: una cota firmada que controle la meseta de masa no nula o la energía en el sector filtrado, independiente de la reformulación. Sin nueva prueba de positividad.

## Qué se puede firmar en la meseta de masa no nula

Corolario de P47 prop:sharp y lem:transl(iv). Para F real, par, suave, compacto y primitivo, sea M=∫F≠0, w el diámetro de su soporte, c_F(v)=∫F(t)F(t−v)dt y H_D=1_[0,D]*F. Para D>w, escribir b=m^sharp(0)=C₀+4 y a_k=k+1/4. Se obtiene un mayorante exacto con un error de signo conocido:

    a^sharp(H_D) = b M² D + C_F − Σ_{k≥1} e^(−2a_kD) |∫F(t)e^(2a_kt)dt|²/(2a_k²),
    C_F = −b ∫ |v|c_F(v)dv + Σ_{k≥1} (1/(2a_k²)) ∫ e^(−2a_k|v|)c_F(v)dv.

En efecto ||H_D||²=∫(D−|v|)c_F(v)dv. En la serie de prop:sharp, |Ĥ_D|²=(2−2cos(Dτ))|F̂|²/τ². La transformada inversa de (τ²+4a_k²)⁻¹ es e^(−2a_k|v|)/(4a_k). La contribución desplazada factoriza al ser D>w; los dos momentos exponenciales coinciden por paridad. Las constantes de la serie son O_F(a_k⁻³) usando |c_F|≤||F||²; la serie desplazada converge por el hueco D−w. La clase incluye F=(1/4−∂²)G para bumps pares suaves de integral no nula.

En particular, si la fluctuación aritmética de prop:sharp para este H_D supera estrictamente bM²D+C_F en un D>w, la energía primitiva es negativa. La condición prescinde de una cota asintótica de error e incluye el término de densidad continua en la definición de fluctuación. Sigue pendiente una comparación para los pesos verdaderos. La identidad no establece positividad de ningún H_D de ventana grande por sí sola.

## Alcance de localizar la curvatura por contactos

Para el F real par no nulo de la sección anterior, sea E(D)=a(H_D). La invariancia por traslación da E(D)=2∫₀ᴰ(D−u)a(F,V_uF)du. El integrando es continuo en cada intervalo acotado por continuidad en norma de forma en una ventana común. Por P47 thm:band y lem:transl(iv), para D>w,
    
    E''(D)=−2[A_F(D)+Σ_{n≥2} Λ(n)c_F(D−log n)/√n],
    A_F(D)=Σ_{k≥1} e^{−(2k+1/2)D} |∫ F(t)e^{(2k+1/2)t}dt|² > 0.

La positividad estricta usa que la anulación de todos esos momentos aniquilaría los polinomios en e^(2t) contra F(t)e^(5t/2)dt. Son densos en las funciones continuas del intervalo compacto de soporte por el cambio de variable x=e^(2t). Por tanto un mínimo interior exige que la suma aritmética sea ≤−A_F(D); en un intervalo sin contacto de signo negativo E es estrictamente cóncava y el mínimo de cualquier subintervalo cerrado está en sus extremos.

La condición de existencia de al menos un contacto negativo pierde toda capacidad de excluir D lejanos. En efecto ∫c_F(u)e^(u/2)du=0 por los momentos, mientras c_F(0)>0. Por continuidad hay un intervalo abierto (a,b) con c_F<0. Para todo D suficientemente grande, PNT da un primo entre exp(D−b) y exp(D−a). La condición cuantitativa sobre la suma conserva contenido. El argumento localiza mínimos interiores, sin asegurar que una energía negativa en el semieje se alcance en un mínimo interior. Antecedente directo: el cruce de dos traslados de P47. Se descarta el cribado global basado sólo en presencia de contactos.
