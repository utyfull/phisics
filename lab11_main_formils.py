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