# Four tails on a common window, even under partial collisions

There exist L₄>0 and c₄>0 such that W(F)≥c₄||F||₂² for any admissible datum on [−L₄,0] followed by any rational block of up to four real poles −u_i, u_i>1/2, with arbitrary multiplicities. Positivity of a block with five poles is not needed. It is an application of the certificates of POWER 084–085 and of the rate separation of 213-198. L₄ is not estimated numerically.

**A relative determinant that keeps the margin under collisions.** Write M(u)=(ξ'/ξ)(u+1/2), x_i=u_i², R(x)=u/M(u), S(x)=uM(u), P=∏_{i<j}(u_i+u_j) and Δx=∏_{i<j}(x_j−x_i). For four distinct rates, K_{ij}=(M(u_i)+M(u_j))/(u_i+u_j), G_{ij}=1/(u_i+u_j) is the temporal L² Gram. With D_f=det[1,x,f(x),xf(x)] evaluated at the four x_i one has exactly

    det K / det G = (∏_i 2M(u_i)) P² (D_R/Δx)(D_S/Δx).

Indeed 083–084 give det K=D_R D_S/(P²∏R_i); the Cauchy determinant gives det G=Δu²/(P²∏2u_i), where Δu=∏_{i<j}(u_j−u_i) and Δx=P Δu. The ratio of determinants is invariant under simultaneous change of basis.

**Explicit compact bound from three derivatives.** On a box of squares J=[1/4,V²], V>1/2 fixed, for f=R,S one knows f'>0, f''<0 and T_f=2f'f'''−3(f'')²>0 by POWER_FOUR_TURAN_084 and POWER_FOUR_GENERATORS_085. At the left endpoint f'>0 by monotonicity of f' and interior positivity; if f'' vanished there, T_f>0 would give f'''>0, incompatible with f''<0 immediately to the right. Let m_f=min_J |f''| and h_f=min_J T_f/(f'')², both positive. Then

    −D_f/Δx ≥ m_f² h_f/12.

To see this, subtract consecutive rows (from bottom to top), expand along the constant column and write each difference as the integral of its derivative. What remains is an integral of a determinant with columns [1,f',(xf)'] at three ordered points t_i∈[x_i,x_{i+1}]. Repeat the step: two points z_1≤z_2 remain and the integrand f''(z_1)f''(z_2)[H(z_2)−H(z_1)], H=(xf)''/f''. Its negative is ≥m_f² h_f(z_2−z_1) by H'=−T_f/(f'')². The integral of the factor z_2−z_1 is Δx/12, applying the same steps to the columns [1,x,x²/2,x³/6]. The lower bound of the relative determinant, strictly positive, is independent of any separation between rates.

In a basis of temporal divided differences both Gram matrices are continuous on the whole box, including the regularized endpoint and partial or total multiplicities. The L² Gram stays invertible by independence of the partial fractions in the Newton basis of 198. Since the W Gram is PSD by limit and its relative determinant stays away from zero, it is positive definite at each collision. By compactness there is a uniform floor relative to L² on each box. The determinant bound alone is not a lower bound for the smallest eigenvalue without control of the other three; that control here follows from continuity and compactness.

**Incorporating the arbitrary datum.** Apply the sequential contradiction of 198, now to lists of length ≤4. For bounded rates the floor just proved is used (for ≤3, 198 suffices). For those that escape, the weighted Hardy bound at σ=min(u_i)/2 is ≤3⁴ per unit norm. Again the archimedean floor of the fast component tends to infinity. All crossings of 198 remain bounded: in a box up to three derivatives in v are taken. In the slow-fast formula each additional derivative produces only a polynomial factor in t or log n, absorbable into exp(Ct); in the slow-compact one, an additional power of r in the integral of 197 is integrable and the regularized polar term is analytic in v. The compact floor grows as the length is reduced and, together with the fast floor, absorbs the three crossings by Young. This proves the statement, including complex coefficients. The procedure uses a differential inequality specific to order four; it does not give a limit in the number of poles.

**Antecedents.** 084 already computes the Wronskian and uses Rolle for the determinant at distinct nodes. The Δx-normalized bound quantifies the margin at every collision in the L² norm of the block; the new arbitrary datum preceding the four tails additionally requires the control of the crossings of phase 213.
