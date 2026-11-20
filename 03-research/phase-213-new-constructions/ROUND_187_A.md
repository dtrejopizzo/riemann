# Test suficiente de negatividad a una sola frecuencia en la banda crítica

Poner X=exp(2T), S_X(Γ)=Σ_{n≤X}Λ(n)log(X/n)n^{iΓ}. Para κ>0 fijo, G=exp(κ exp T), Γ∈[2G,3G], tomar el perfil exp(−(T−|t|)/2) en [−T,T], con fase 1 en la mitad izquierda y exp(iθ) en la derecha. Dividir por sqrt(B), B=2(1−exp(−T)), y modular por exp(iΓt) para obtener f_θ de norma uno. Uniformemente en la banda,

    min_θ W_T(f_θ)=log Γ−|S_X(Γ)|/sqrt(X)+O(T+1).

En particular una sucesión con |S_X(Γ)|/X≥κ+δ, para δ>0 fijo, daría valores negativos de la forma verdadera a escala grande. Para κ=1, agotar el margen principal en estos perfiles equivale a |S_X(Γ)|/X→1 (la masa total S_X(0)∼X por PNT). La igualdad asintótica por sí sola no decide el signo residual.

**Solapamiento exacto.** Para l=log n∈[0,2T] la autocorrelación desmodulada a desplazamiento positivo consta de dos partes. Entre mitades tiene longitud b(l)=min(l,2T−l), producto constante exp(−(2T−l)/2) y fase exp(iθ), hasta la convención de conjugación. Dentro de una misma mitad el solapamiento sumado, para l≤T, es 2 exp(−l/2)(1−exp(−(T−l))); para l>T es cero. Ambos términos llevan el divisor B. Al multiplicar por 2Λ(n)/sqrt(n) y tomar parte real, la parte cruzada resulta (2/B)exp(−T) Re[exp(iθ)ΣΛ(n)b(l)n^{iΓ}] con la convención de autocorrelación f(t+l)conj(f(t)). La parte interna cuesta O(Σ_{n≤exp T}Λ(n)/n)=O(T+1).

Reemplazar b(l) por 2T−l en la suma cruzada cuesta O(1) en la forma: exp(−T)Σ_{n≤exp T}Λ(n)(T−log n)=O(1) integrando ψ(y)/y y usando Chebyshev. Reemplazar 2/B por uno también cuesta O(1), pues Σ_{n≤X}Λ(n)log(X/n)≪X por la misma cuenta. Estos errores son absolutos incluso en frecuencias excepcionales.

**Forma completa.** La variación total de los perfiles desmodulados, su norma de supremo y su norma L¹ son O(1) uniformemente en θ. La mayoración arquimediana de 180 da log Γ+O(1); para la minoración, en |v|≤Γ/2 alrededor de Γ el símbolo es ≥log Γ−O(1), y fuera se pierde masa O(1/Γ) con piso absoluto. Los polos cuestan O(exp(T)/Γ²) por las dos integraciones por partes de 180. Optimizar la fase cruzada prueba la fórmula.

**Antecedentes y alcance.** El peso log(X/n) ya está en 212-57 C1 y SELECTION_092; esta última incluso da un criterio global con primos solos sin torsión. 180 modulaba un perfil impar y promediaba en Γ. Aquí se mantiene la torsión de la frecuencia individual y se optimiza la fase relativa de los dos extremos, con error absoluto O(T+1). A diferencia de la condición necesaria de 184 sobre un intervalo, superar este umbral en la suma completa sería suficiente para obtener un contraejemplo real (por realificación si hiciera falta). No se ha encontrado tal frecuencia ni se ha demostrado el techo requerido.

La auditoría independiente confirma la fórmula al primer orden y el sentido de la implicación. P47 thm:band ya usa dos direcciones y prop:wit-Egamma ya da obligaciones para sumas torcidas. El error absoluto más fino escrito arriba proviene de incluir también el solapamiento exacto dentro de cada mitad.
