def tartiblash(massiv):
    n = len(massiv)
    i = 0  # Manfiy sonlar uchun indeks
    for j in range(n):
        if massiv[j] < 0:
            
            massiv[i], massiv[j] = massiv[j], massiv[i]
            i=i+1  

    return massiv
massiv = [3, -1, 90, -5, -2, 43, 6, 23]
print("Asl massiv:", massiv)
tartiblangan_massiv = tartiblash(massiv)
print("Tartiblangan massiv:", tartiblangan_massiv)
print(len(massiv))