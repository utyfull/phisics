from sympy import symbols, diff, lambdify

j_d_sym, k_sym, m0_sym, r0_sym, R_i_sym = symbols('j_d k m0 r0 R_i')

J_sym = j_d_sym + k_sym * ((m0_sym * r0_sym**2 / 2) + (m0_sym * R_i_sym**2))

partial_jd = diff(J_sym, j_d_sym)
partial_k = diff(J_sym, k_sym)
partial_m0 = diff(J_sym, m0_sym)
partial_r0 = diff(J_sym, r0_sym)
partial_Ri = diff(J_sym, R_i_sym)

partial_jd_func = lambdify((j_d_sym, k_sym, m0_sym, r0_sym, R_i_sym), partial_jd)
partial_k_func = lambdify((j_d_sym, k_sym, m0_sym, r0_sym, R_i_sym), partial_k)
partial_m0_func = lambdify((j_d_sym, k_sym, m0_sym, r0_sym, R_i_sym), partial_m0)
partial_r0_func = lambdify((j_d_sym, k_sym, m0_sym, r0_sym, R_i_sym), partial_r0)
partial_Ri_func = lambdify((j_d_sym, k_sym, m0_sym, r0_sym, R_i_sym), partial_Ri)

def calculate_partials(j_d_val, k_val, m0_val, r0_val, R_i_val):
    partials = {
        '∂J/∂j_d': partial_jd_func(j_d_val, k_val, m0_val, r0_val, R_i_val),
        '∂J/∂k': partial_k_func(j_d_val, k_val, m0_val, r0_val, R_i_val),
        '∂J/∂m0': partial_m0_func(j_d_val, k_val, m0_val, r0_val, R_i_val),
        '∂J/∂r0': partial_r0_func(j_d_val, k_val, m0_val, r0_val, R_i_val),
        '∂J/∂R_i': partial_Ri_func(j_d_val, k_val, m0_val, r0_val, R_i_val)
    }
    return partials

def calculate_j(j_d, k, m0, r0, R_i) -> float:
    j = j_d + k * ((m0 * r0**2 / 2) + (m0 * R_i**2))
    return j

if __name__ == '__main__':
    j_d = 10.0  
    k = 1.5   
    m0 = 2.0    
    r0 = 3.0    
    R_i = 1.5   

    result = calculate_j(j_d, k, m0, r0, R_i)
    print(f"Результат: {result}")

    print("\nФормулы частных производных:")
    print(f"∂J/∂j_d = {partial_jd}")
    print(f"∂J/∂k = {partial_k}")
    print(f"∂J/∂m0 = {partial_m0}")
    print(f"∂J/∂r0 = {partial_r0}")
    print(f"∂J/∂R_i = {partial_Ri}")

    partials = calculate_partials(j_d, k, m0, r0, R_i)
    
    print("\nЧастные производные (числовые значения):")
    for var, value in partials.items():
        print(f"{var}: {value}")
